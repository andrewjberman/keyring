"""
comp-drift -- the estate propagation-drift ORCHESTRATOR (NFRA_COMPDRIFT P2 / TO-2).

OWNS the propagation topology (drift-topology.yaml) + a normalized cross-seam
drift-record + the fan-out. It CALLS the existing seam engines (comp-heat drift,
comp-pipescript deployed, comp-lambdamap parity, comp-iam reconcile, comp-kuzu
provenance, iceberg_parity.py, code_heat_parity.py, comp-freshness) and NEVER
re-implements a seam's check logic (PRD arch-gate (b), the load-bearing line).

Surfaces:
  comp-drift coverage            -- the coverage ledger from the manifest (pure read).
  comp-drift <target>            -- walk one artifact's full propagation chain.
  comp-drift sweep [--deep]      -- fan out across every seam -> unified board.
  (--json on any; tri-state exit 0 clean / 1 integrity-break / 2 UNVERIFIABLE.)

Discipline: NEVER silently MATCH a seam it could not read -- an unreadable /
unwired / GAP seam is UNVERIFIABLE (exit 2), a FINDING, never false-clean
(PRD arch-gate (c) + the disposition model). Every record carries `grounding`.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_WORKSPACE = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
if os.path.join(_WORKSPACE, ".tools") not in sys.path:
    sys.path.insert(0, os.path.join(_WORKSPACE, ".tools"))
import _compbudget  # noqa: E402 -- NFRA_COMPEFFICACY CE-t-14: shared Rule-T carrier

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("comp-drift: PyYAML required (pip install pyyaml)\n")
    sys.exit(2)

WORKSPACE = _WORKSPACE
TOPOLOGY = os.path.join(WORKSPACE, "org", "modules", "graph", "drift-topology.yaml")

# Resolve the REAL Git Bash (NOT WSL bash) -- on Windows, bare subprocess(["bash"])
# resolves to the WSL relay (execvpe /bin/bash fails). The wrapper exports
# COMP_DRIFT_BASH; else shutil.which finds Git Bash; else fall back.
BASH_EXE = (os.environ.get("COMP_DRIFT_BASH")
            or shutil.which("bash")
            or "bash")
# comp-heat + comp-freshness are PYTHON scripts (#!/usr/bin/env python3); the rest are bash.
# Forcing a python tool through `bash <file>` mis-parses the source and HANGS (2min timeout in
# testing -> rc=124 -> false UNVERIFIABLE). So _bash() dispatches on each tool's shebang below.
PYTHON_EXE = (sys.executable or shutil.which("python3") or shutil.which("python") or "python")

# Tri-state exit (PRD arch-gate (c); manifest exit_contract).
# Complete-sweep verdicts retain the established 0/1/2 vocabulary.  A budget
# cut is a fourth state: it is not clean, an integrity break, or a seam that
# could not be read.  The rc is deliberately distinct so rc-only consumers
# cannot mistake a PREFIX for a complete verdict (FWD-10 / Rule T).
EXIT_CLEAN, EXIT_BREAK, EXIT_UNVERIFIABLE, EXIT_NOT_DECIDABLE = 0, 1, 2, 3
_ACTIVE_CLOCK = None
# Ratified PRD s.4.3 answer-state spellings.  comp-drift's budget-cut branch
# speaks the PARTIAL_OR_BLIND member; the remaining members are kept as data
# vocabulary for result consumers and planted-case reporting (not re-invented
# per seam).
STATE_SUBJECT_ABSENT = "SUBJECT_ABSENT_FROM_CORPUS"
STATE_PRESENT_ZERO = "PRESENT_WITH_ZERO_RESULTS"
STATE_PARTIAL_BLIND = "PARTIAL_OR_BLIND"
STATE_NOT_APPLICABLE = "NOT_APPLICABLE"

# Verdicts that are an integrity BREAK (exit 1). Everything else clean unless UNVERIFIABLE.
BREAK_VERDICTS = {
    "UNCOMMITTED", "STALE", "MISSING", "POSSIBLE-HALF-LANDED", "DIVERGED",
    "TF-ONLY", "LIVE-ONLY", "SCHEMA-DRIFT", "SCHEMA-MISMATCH", "HALF-LANDED",
    "STALE-GENUINE-IN-USE",
}
# Verdicts that are UNVERIFIABLE (exit 2) -- a finding, never silent-MATCH.
UNVERIFIABLE_VERDICTS = {
    "UNVERIFIABLE", "UNKNOWN-VINTAGE", "UNVERIFIABLE-CONSUMER", "NO-ENGINE",
}
# COST-GUARDED (NFRA_INSTDRILL item 4, 2026-07-14): a check DELIBERATELY DEFERRED because its
# engine is expensive in a plain sweep (full-repo scan / all-gold sweep / live network). This is
# NOT "could not read the seam" (UNVERIFIABLE) -- it is "did not attempt it; run --deep or a
# <target>". Conflating the two was the whole defect: a plain sweep read as all-UNVERIFIABLE (an
# alarming could-not-verify) when it had simply deferred every expensive check by design.
COST_GUARDED_VERDICTS = {"COST-GUARDED"}
# Operator action per verdict-class (the normalized "what do I do").
ACTION = {
    "clean": "none",
    "break": "reconcile -- redeploy/repoint/re-derive to restore parity",
    "unverifiable": "investigate -- could not read the seam; do NOT assume clean",
    "deferred": "run `comp-drift <target>` or `comp-drift sweep --deep` -- this check was skipped "
                "for cost, NOT attempted; it is neither clean nor broken",
    "dispositioned": "disposition -- abandoned artifact; clean up (not fix)",
    "self_heal": "none -- self-heals on HEAD-advance (informational)",
    "stale": "refresh -- vintage-stale DERIVED layer (behind the marker); re-derive it. NOT an "
             "integrity break, and does NOT auto-self-heal on read (unlike comp-kuzu's marker oracle)",
    "partial": "note -- partial coverage; the equality is not fully asserted",
}


def load_topology() -> dict:
    with open(TOPOLOGY, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _run(cmd: list[str], timeout: int = 120) -> tuple[int, str]:
    """Invoke an engine as a black box. Returns (returncode, combined stdout+stderr).
    A non-zero rc is NOT inherently a break -- each adapter maps the engine's OWN
    verdict; rc is only a fallback signal."""
    # Every child call in a budgeted walk inherits the shared wall-clock ceiling.
    # A remaining() timeout prevents a slow seam engine from silently running
    # past expiry and being reported as a complete verdict.
    global _ACTIVE_CLOCK
    if _ACTIVE_CLOCK is not None:
        remaining = _ACTIVE_CLOCK.remaining()
        if remaining is not None:
            if remaining <= 0:
                return 124, "budget exhausted before engine invocation"
            timeout = min(timeout, max(0.01, remaining))
    try:
        p = subprocess.run(
            cmd, cwd=WORKSPACE, capture_output=True, text=True, timeout=timeout,
        )
        return p.returncode, (p.stdout or "") + (p.stderr or "")
    except FileNotFoundError:
        return 127, "engine binary not found"
    except subprocess.TimeoutExpired:
        return 124, "engine timed out"
    except Exception as exc:  # noqa: BLE001 -- orchestrator must never crash on an engine
        return 125, "engine invocation error: %s" % exc


def _interp(tool_path: str) -> list[str]:
    """The interpreter for a .tools/ script, by its shebang (python tools must NOT run via bash)."""
    try:
        with open(tool_path, "r", encoding="utf-8", errors="replace") as fh:
            first = fh.readline()
    except OSError:
        first = ""
    return [PYTHON_EXE] if "python" in first else [BASH_EXE]


def _bash(tool: str, *args: str, timeout: int = 120) -> tuple[int, str]:
    # Name kept for call-site stability; dispatches by shebang (bash OR python), not always bash.
    tool_path = os.path.join(WORKSPACE, ".tools", tool)
    return _run(_interp(tool_path) + [tool_path, *args], timeout=timeout)


def _kuzu_scalar(out: str) -> str:
    """Extract a single scalar from a comp-kuzu table result -- the one value row between the
    dashed header/data separator and the trailing '(N rows)'. Empty string if no data row."""
    lines = out.splitlines()
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s and set(s) <= set("- ") and "-" in s:   # the header/data separator line
            for v in lines[i + 1:]:
                vs = v.strip()
                if vs and not vs.startswith("("):
                    return vs.split()[-1]
            break
    return ""


def _classify(verdict: str) -> str:
    v = (verdict or "").upper()
    if v in {x.upper() for x in COST_GUARDED_VERDICTS}:
        return "deferred"
    if v in {x.upper() for x in UNVERIFIABLE_VERDICTS}:
        return "unverifiable"
    if v in {x.upper() for x in BREAK_VERDICTS}:
        return "break"
    if v in {"ABANDONED-ARTIFACT", "DISPOSITIONED", "NOT-LIVE"}:
        return "dispositioned"
    if v in {"REFRESHING", "SELF-HEALING"}:
        return "self_heal"
    if v in {"BEHIND", "VINTAGE-STALE"}:
        return "stale"   # a vintage-stale DERIVED layer: a WARN finding, NOT a break, NOT self-healing
    return "clean"


def _record(seam: dict, target: str, verdict: str, grounding: str,
            disposition: str | None = None) -> dict:
    """The normalized cross-seam drift-record envelope (PRD arch-gate (c))."""
    cls = _classify(verdict)
    sev = {"clean": "OK", "self_heal": "OK", "partial": "INFO", "deferred": "SKIP",
           "dispositioned": "INFO", "stale": "WARN", "unverifiable": "WARN", "break": "ERROR"}[cls]
    return {
        "seam_id": seam.get("seam_id"),
        "stage_from": seam.get("stage_from"),
        "stage_to": seam.get("stage_to"),
        "target": target,
        "verdict": verdict,
        "severity": sev,
        "operator_action": ACTION[cls],
        "disposition": disposition,
        "grounding": grounding,
        "_class": cls,
    }


# ---- ENGINE ADAPTERS -------------------------------------------------------
# Each adapter INVOKES the existing engine and NORMALIZES its verdict. It never
# re-implements the check. If it cannot confidently read a verdict from the
# engine output, it returns UNVERIFIABLE (never guesses MATCH).
# (Historical: the adapters formerly shared a _first_token(vocab) helper; it was REMOVED after
# every adapter was hardened to parse each engine's AUTHORITATIVE rollup line / exit code. A
# token-first-scan false-flagged whenever a 0-count verdict token appeared in a summary line
# (or when the scanned vocab wasn't even what the tool prints) -- see the comp-lambdamap /
# comp-freshness / comp-iam adapter notes below. Do NOT re-introduce a token-scan.)


def adapter_comp_heat_drift(seam, target, ctx):
    # comp-heat drift scans the WHOLE repo (slow) -- cost-guard in plain sweep.
    if not ctx.get("deep") and not target:
        return _record(seam, "<working-tree>", "COST-GUARDED",
                       "comp-heat full-repo drift scan skipped (cost-guard; run a <target> or --deep)")
    rc, out = _bash("comp-heat", "drift", "--json", timeout=120)
    if rc in (124, 125, 127):
        return _record(seam, target or "<working-tree>", "UNVERIFIABLE",
                       "comp-heat drift unavailable (rc=%s: timeout/error)" % rc)
    try:
        data = json.loads(out[out.index("{"):out.rindex("}") + 1])
        uncommitted = [r.get("path", "") for r in data.get("uncommitted", [])]
    except Exception:  # noqa: BLE001 -- never guess a verdict from unparseable output
        return _record(seam, target or "<working-tree>", "UNVERIFIABLE",
                       "comp-heat drift --json unparseable (not assuming CLEAN)")
    if target:  # scope the seam-1 verdict to THIS artifact
        tnorm = target.replace("\\", "/")
        hit = any(tnorm == p or tnorm.endswith("/" + p) or p.endswith(tnorm) for p in uncommitted)
        verdict = "UNCOMMITTED" if hit else "CLEAN"
        ground = "comp-heat drift --json: target %s committed" % ("NOT" if hit else "is")
    else:
        verdict = "UNCOMMITTED" if uncommitted else "CLEAN"
        ground = "comp-heat drift --json: %d uncommitted write(s) in working tree" % len(uncommitted)
    return _record(seam, target or "<working-tree>", verdict, ground)


def adapter_comp_pipescript_deployed(seam, target, ctx):
    # the no-arg form sweeps ALL gold trees (slow) -- cost-guard in plain sweep.
    if not target and not ctx.get("deep"):
        return _record(seam, "<all-gold>", "COST-GUARDED",
                       "comp-pipescript all-gold deploy sweep skipped (cost-guard; run a <target> or --deep)")
    args = ["deployed"] + ([target] if target else [])
    rc, out = _bash("comp-pipescript", *args, timeout=120)
    # HARDENED: parse the Summary COUNTS, not token-presence -- the tokens STALE/MISSING_ON_S3/etc.
    # ALWAYS appear in the summary (with 0 counts), so a token-first-match would false-flag.
    m = re.search(r"Summary:\s*(\d+) MATCH,\s*(\d+) STALE,\s*(\d+) MISSING_ON_S3,"
                  r"\s*(\d+) LOCAL_MISSING,\s*(\d+) TIMEOUT,\s*(\d+) AWS_UNREACHABLE", out)
    if not m:
        return _record(seam, target or "<all-gold>", "UNVERIFIABLE",
                       "comp-pipescript deployed rc=%s (Summary unparsed -- not assuming MATCH)" % rc)
    match, stale, miss, lmiss, timeout, unreach = (int(x) for x in m.groups())
    if timeout or unreach:
        return _record(seam, target or "<all-gold>", "UNVERIFIABLE",
                       "comp-pipescript deployed: %d TIMEOUT / %d AWS_UNREACHABLE" % (timeout, unreach))
    if stale or miss or lmiss:
        verdict = "STALE" if stale else "MISSING"
        return _record(seam, target or "<all-gold>", verdict,
                       "comp-pipescript deployed: %d STALE / %d MISSING_ON_S3 / %d LOCAL_MISSING"
                       % (stale, miss, lmiss))
    return _record(seam, target or "<all-gold>", "MATCH",
                   "comp-pipescript deployed: %d MATCH, all up-to-date on S3" % match)


def adapter_comp_lambdamap(seam, target, ctx):
    if not ctx.get("deep"):
        return _record(seam, target or "<lambda>", "COST-GUARDED",
                       "live 3-leg sha read skipped (cost-guard; run with --deep or a <target>)")
    # parity is WHOLE-ESTATE (iam-style argparse rejects a positional target -> rc=2). Run --json
    # and, when a target is given, filter to THAT lambda's OWN verdict. (E3 fix: the old positional
    # `parity <target>` -> rc=2 -> unparsed counts -> false UNVERIFIABLE on a clean lambda.)
    rc, out = _bash("comp-lambdamap", "parity", "--json")
    try:
        payload = json.loads(out[out.find("{"):]) if "{" in out else {}
        verdicts = payload.get("verdicts") or {}
    except Exception:
        verdicts = {}
    if not verdicts:
        return _record(seam, target or "<lambda>", "UNVERIFIABLE",
                       "comp-lambdamap parity --json rc=%s (verdicts unparsed -- not assuming MATCH)" % rc)
    _BREAK = ("POSSIBLE-HALF-LANDED", "STALE-RECORD", "CORRUPT-RECORD")
    if target:
        fn = target.split(":function:")[-1].split(":")[0] if ":" in target else target
        entry = verdicts.get(fn)
        if entry is None:
            return _record(seam, target, "UNVERIFIABLE",
                           "comp-lambdamap parity: no verdict for '%s' (NO-RECORD/not-covered -- not assuming MATCH)" % fn)
        v = (entry.get("verdict") or "").upper()
        det = (" -- " + entry["detail"]) if entry.get("detail") else ""
        if v in _BREAK:
            return _record(seam, target, v, "comp-lambdamap parity[%s]: %s%s" % (fn, v, det))
        if v in ("NOT-LIVE", "UNVERIFIABLE", "NO-RECORD"):
            return _record(seam, target, "UNVERIFIABLE",
                           "comp-lambdamap parity[%s]: %s (not confirmed-clean)%s" % (fn, v, det))
        return _record(seam, target, "MATCH",
                       "comp-lambdamap parity[%s]: %s -- no integrity break" % (fn, v))
    # no target -> whole-estate rollup (aggregate the per-lambda verdicts; DISPOSITIONED =
    # intentional divergence, NO-RECORD = uncovered/unchecked -- never read as fully-verified-clean).
    counts = {}
    for e in verdicts.values():
        counts[(e.get("verdict") or "").upper()] = counts.get((e.get("verdict") or "").upper(), 0) + 1
    hot = [(t, counts[t]) for t in _BREAK if counts.get(t)]
    if hot:
        return _record(seam, "<lambda>", hot[0][0],
                       "comp-lambdamap parity: " + ", ".join("%d %s" % (c, t) for t, c in hot))
    if counts.get("NOT-LIVE") or counts.get("UNVERIFIABLE"):
        return _record(seam, "<lambda>", "UNVERIFIABLE",
                       "comp-lambdamap parity: %d NOT-LIVE / %d UNVERIFIABLE"
                       % (counts.get("NOT-LIVE", 0), counts.get("UNVERIFIABLE", 0)))
    note = "%d MATCH" % counts.get("MATCH", 0)
    if counts.get("DISPOSITIONED"):
        note += ", %d DISPOSITIONED (intentional)" % counts["DISPOSITIONED"]
    if counts.get("NO-RECORD"):
        note += ", %d NO-RECORD UNCHECKED" % counts["NO-RECORD"]
    return _record(seam, "<lambda>", "MATCH",
                   "comp-lambdamap parity: %s -- no integrity break" % note)


def adapter_comp_iam(seam, target, ctx):
    if not ctx.get("deep"):
        return _record(seam, target or "<iam>", "COST-GUARDED",
                       "live IAM reconcile skipped (cost-guard + stale-census caveat; --deep to run)")
    # reconcile is ESTATE-WIDE: iam_cli.py add_parser('reconcile') takes NO positional (unlike
    # service/role), so we never pass a target -- IAM drift is estate-scoped, not per-artifact.
    rc, out = _bash("comp-iam", "reconcile")
    if rc in (124, 125, 127):
        return _record(seam, target or "<iam>", "UNVERIFIABLE",
                       "comp-iam reconcile unavailable (rc=%s: timeout/not-found/error)" % rc)
    # HARDENED (grounded on iam_cli.py cmd_reconcile): the authoritative rollup is the
    # "Total: N live-only-role | M live-only-action | K over-perm" line (exit = 1 if
    # live-only-role+live-only-action else 0; over-perm does NOT gate exit). The old
    # _first_token([DIVERGED,TF-ONLY,LIVE-ONLY,MATCH]) scanned tokens the tool NEVER prints as a
    # verdict (only "DRIFT-LIVE-ONLY" carries "LIVE-ONLY" as a substring, and only when drift
    # exists) -- wrong vocabulary (read notes, not the verdict).
    m = re.search(r"Total:\s*(\d+) live-only-role \|\s*(\d+) live-only-action \|\s*(\d+) over-perm", out)
    if not m:
        return _record(seam, target or "<iam>", "UNVERIFIABLE",
                       "comp-iam reconcile rc=%s (Total rollup unparsed -- not assuming clean)" % rc)
    lo_role, lo_action, overperm = (int(x) for x in m.groups())
    if target:
        # E3 fix: SCOPE to the target's OWN role -- estate-wide drift in OTHER roles is not this
        # artifact's break (the old code gated a single clean lambda's verdict on whole-estate
        # 38/14 -> false DIVERGED). Resolve the target lambda -> its live execution role, then check
        # ONLY that role against reconcile's per-role DRIFT-LIVE-ONLY list ('!! <role>').
        fn = target.split(":function:")[-1].split(":")[0] if ":" in target else target
        # resolve the target lambda -> its execution role via the graph ASSUMES edge. comp-kuzu is a
        # .tools/ script _bash can dispatch (aws is NOT -- _bash only runs .tools/<tool>). The
        # lambda->role mapping is structural (not freshness-sensitive), so the graph is authoritative.
        _k_rc, k_out = _bash("comp-kuzu",
                             "MATCH (l:CloudNode)-[e:CloudEdge]->(r:CloudNode) WHERE l.node_type='LAMBDA' "
                             "AND r.node_type='IAM_ROLE' AND e.edge_type='ASSUMES' AND l.name='%s' "
                             "RETURN r.name LIMIT 1" % fn)
        role = _kuzu_scalar(k_out)
        if not role:
            return _record(seam, target, "UNVERIFIABLE",
                           "comp-iam: could not resolve execution role for '%s' via the graph ASSUMES edge" % fn)
        drifted = set(re.findall(r"!!\s*([A-Za-z0-9_+=,.@-]+)", out))
        if role in drifted:
            return _record(seam, target, "DIVERGED",
                           "comp-iam reconcile: target role %s is live-only (granted live, ABSENT from TF)" % role)
        ctx_note = (" (estate has %d live-only-role / %d live-only-action drift in OTHER roles -- "
                    "informational, not target-scoped)" % (lo_role, lo_action)) if (lo_role or lo_action) else ""
        return _record(seam, target, "MATCH",
                       "comp-iam reconcile: target role %s clean (TF-governed, not in live-only drift)%s" % (role, ctx_note))
    if lo_role or lo_action:
        return _record(seam, target or "<iam>", "DIVERGED",
                       "comp-iam reconcile: %d live-only-role / %d live-only-action drift "
                       "(census-backed; ground a FRESH IAM change on live get-role-policy, not this verdict)"
                       % (lo_role, lo_action))
    note = "no desired-vs-live drift"
    if overperm:
        note += ", %d over-perm (hygiene finding, non-drift)" % overperm
    return _record(seam, target or "<iam>", "MATCH",
                   "comp-iam reconcile: %s (census-backed; stale-census caveat applies)" % note)


def adapter_comp_kuzu_provenance(seam, target, ctx):
    """seam-3 + seam-4: read the comp-kuzu provenance header (marker-oracle)."""
    rc, out = _bash("comp-kuzu", "MATCH (n) RETURN count(n) LIMIT 1")
    low = out.lower()
    if "nessie head: current" in low or "pin == marker head" in low:
        verdict = "current"
        ground = "comp-kuzu provenance: HEAD current (pin == marker HEAD)"
    elif "behind" in low:
        # comp-kuzu BEHIND SELF-HEALS: the marker oracle auto-re-derives the Kuzu projection on the
        # next read after a HEAD-advance. So it is self_heal/OK -- NOT the same as code_heat's BEHIND
        # (a vintage-stale derived layer that classifies "stale"/WARN and needs a manual re-derive).
        verdict = "SELF-HEALING"
        ground = "comp-kuzu provenance: BEHIND -> SELF-HEALING (marker oracle re-derives on next read)"
    elif "unknown vintage" in low or "unknown-vintage" in low:
        verdict = "UNKNOWN-VINTAGE"
        ground = "comp-kuzu provenance: UNKNOWN VINTAGE (freshness unverifiable)"
    else:
        verdict = "UNVERIFIABLE"
        ground = "comp-kuzu provenance header unreadable rc=%s" % rc
    return _record(seam, target or "<graph>", verdict, ground)


def adapter_iceberg_parity(seam, target, ctx):
    if not ctx.get("deep"):
        return _record(seam, target or "<iceberg>", "COST-GUARDED",
                       "live S3 iceberg metadata read skipped (cost-guard; --deep to run)")
    rc, out = _run(["python", os.path.join(WORKSPACE, "infra", "aws", "globgrph", "iceberg_parity.py")])
    # HARDENED: parse the authoritative "NODE ROLLUP: <v> (worst-of)" line, not a per-table token-scan
    # (each of the 3 tables prints its own MATCH/SCHEMA-DRIFT; the rollup is the seam verdict).
    m = re.search(r"NODE ROLLUP:\s*(MATCH|SCHEMA-DRIFT|STALE|UNVERIFIABLE)", out)
    if not m:
        return _record(seam, target or "<iceberg>", "UNVERIFIABLE",
                       "iceberg_parity.py rc=%s (NODE ROLLUP unparsed -- not assuming MATCH)" % rc)
    return _record(seam, target or "<iceberg>", m.group(1),
                   "iceberg_parity.py -> %s (worst-of over graph_nodes/edges/contracts)" % m.group(1))


def adapter_code_heat_parity(seam, target, ctx):
    if not ctx.get("deep"):
        return _record(seam, target or "<code_heat>", "COST-GUARDED",
                       "live code_heat HEAD-pointer read skipped (cost-guard; --deep to run)")
    rc, out = _run(["python", os.path.join(WORKSPACE, "infra", "aws", "globgrph", "code_heat_parity.py")])
    # HARDENED: parse the authoritative "BINDING VERDICT: <v> (worst-of)" line, not a token-scan
    # (the per-catalog lines also carry BEHIND/current, so a token-scan could pick a non-rollup one).
    m = re.search(r"BINDING VERDICT:\s*(current|BEHIND|UNVERIFIABLE)", out)
    if not m:
        return _record(seam, target or "<code_heat>", "UNVERIFIABLE",
                       "code_heat_parity.py rc=%s (BINDING VERDICT unparsed -- not assuming current)" % rc)
    return _record(seam, target or "<code_heat>", m.group(1),
                   "code_heat_parity.py -> %s (worst-of rollup)" % m.group(1))


def adapter_tool_activity_parity(seam, target, ctx):
    """seam-6 tool-activity-behavior binding: the COMPLEARN derived-parquet vintage check
    (mirrors code_heat_parity -- VINTAGE-PRIMARY current/BEHIND/UNVERIFIABLE)."""
    if not ctx.get("deep"):
        return _record(seam, target or "<tool-activity>", "COST-GUARDED",
                       "live tool_activity vintage read skipped (cost-guard; --deep to run)")
    rc, out = _run(["python", os.path.join(WORKSPACE, "infra", "aws", "globgrph",
                    "tool_activity_parity.py")])
    m = re.search(r"BINDING VERDICT:\s*(current|BEHIND|UNVERIFIABLE)", out)
    if not m:
        return _record(seam, target or "<tool-activity>", "UNVERIFIABLE",
                       "tool_activity_parity.py rc=%s (BINDING VERDICT unparsed -- not assuming current)" % rc)
    return _record(seam, target or "<tool-activity>", m.group(1),
                   "tool_activity_parity.py -> %s (worst-of rollup)" % m.group(1))


def adapter_trino_catalog_parity(seam, target, ctx):
    """seam-6 iceberg-catalog legs (graph_nodes/edges/contracts): Trino-side catalog parity vs the
    live iceberg table (resolved snapshot + normalized schema). The engine checks all 3 catalogs in
    ONE in-VPC query, so it runs ONCE per sweep (memoized in ctx) and each binding-call returns the
    record for THIS binding's catalog (ctx['_binding'])."""
    catalog = ctx.get("_binding") or ""
    label = "<trino:%s>" % (catalog or "iceberg")
    if not ctx.get("deep"):
        return _record(seam, target or label, "COST-GUARDED",
                       "live Trino federation query skipped (cost-guard ~4min Fargate; --deep to run)")
    cache = ctx.get("_trino_parity")
    if cache is None:
        rc, out = _run(["python", os.path.join(WORKSPACE, "infra", "aws", "globgrph",
                        "trino_catalog_parity.py"), "--json", "-"], timeout=540)
        try:  # never guess a verdict from unparseable engine output
            data = json.loads(out[out.index("{"):out.rindex("}") + 1])
            cache = {c["catalog"]: c for c in data.get("detail", {}).get("catalogs", [])}
        except Exception:  # noqa: BLE001
            cache = {}
        ctx["_trino_parity"] = cache
    rec = cache.get(catalog)
    if not rec:
        return _record(seam, target or label, "UNVERIFIABLE",
                       "trino_catalog_parity produced no record for catalog '%s' (engine unreadable/failed)"
                       % (catalog or "?"))
    return _record(seam, target or ("trino:%s" % catalog), rec["verdict"], rec["grounding"])


def adapter_comp_freshness(seam, target, ctx):
    if not ctx.get("deep"):
        return _record(seam, target or "<served>", "COST-GUARDED",
                       "live served-freshness read skipped (cost-guard; --deep to run)")
    # INVOCATION (grounded on comp-freshness argparse): no-arg prints help+exit2; the full-estate
    # sweep is `all` (bd+inf+cot S3 + DDB), a single artifact is `artifact <s3_prefix>`.
    # PERF: `all` is the SLOW seam engine (live S3 x3 firms + full DDB) -- can exceed the default
    # 120s, so it gets a 300s budget here; if even that is exceeded it returns UNVERIFIABLE-by-
    # timeout (rc=124, honest -- never-silent). seam-served is the sweep's heaviest --deep leg.
    rc, out = _bash("comp-freshness", *(["artifact", target] if target else ["all"]), timeout=300)
    # HARDENED (grounded on comp-freshness source): the tool's AUTHORITATIVE rollup is its EXIT
    # CODE, not a printed token -- print_results() returns `1 if any_fail else 0`, main() max()es
    # it across the bd/inf/cot/ddb chains, and 2 = config/arg error. Its per-row STATUS vocab is
    # PASS/WARN/FAIL/SKIP; it NEVER prints "STALE"/"FRESH" as a verdict (those appear only inside
    # note substrings like MTIME-FRESH-BUT-CONTENT-STALE), so the old _first_token([STALE,
    # UNVERIFIABLE,FRESH]) keyed off the WRONG vocabulary -- it read notes, not the verdict.
    if rc in (124, 125, 127):
        return _record(seam, target or "<served>", "UNVERIFIABLE",
                       "comp-freshness unavailable (rc=%s: timeout/not-found/error)" % rc)
    if rc == 0:
        return _record(seam, target or "<served>", "FRESH",
                       "comp-freshness exit 0: no FAIL row (served chain fresh; WARN=aging tolerated)")
    if rc == 1:
        return _record(seam, target or "<served>", "STALE",
                       "comp-freshness exit 1: >=1 FAIL row (a served artifact is stale/failed)")
    return _record(seam, target or "<served>", "UNVERIFIABLE",
                   "comp-freshness exit %s (config/arg error or unknown -- not assuming FRESH)" % rc)


def adapter_uncovered(seam, target, ctx):
    """A GAP seam: no engine. Loud by construction -- UNVERIFIABLE, never MATCH."""
    return _record(seam, target or "<n/a>", "NO-ENGINE",
                   "seam coverage=GAP -- no checker wired (PRD: build a seam-tool in P3; comp-drift then CALLS it)")


# Engine-id -> adapter. The manifest names the engine; we route to its adapter.
ADAPTERS = {
    "comp-heat drift": adapter_comp_heat_drift,
    "comp-pipescript deployed": adapter_comp_pipescript_deployed,
    "comp-lambdamap parity": adapter_comp_lambdamap,
    "comp-iam reconcile": adapter_comp_iam,
    "comp-kuzu": adapter_comp_kuzu_provenance,
    "iceberg_parity.py": adapter_iceberg_parity,
    "code_heat_parity.py": adapter_code_heat_parity,
    "tool_activity_parity.py": adapter_tool_activity_parity,
    "trino_catalog_parity.py": adapter_trino_catalog_parity,
    "comp-freshness": adapter_comp_freshness,
}


def _engine_id(engine: str | None) -> str | None:
    """Map a manifest engine string to a registered adapter key (substring match)."""
    if not engine or engine.upper() == "UNCOVERED":
        return None
    for key in ADAPTERS:
        if key.split()[0] in engine:
            return key
    return None


def _adapter_for(engine: str | None):
    key = _engine_id(engine)
    return ADAPTERS.get(key, adapter_uncovered)


# ---- SEAM WALK -------------------------------------------------------------

def _seam_engines(seam: dict) -> list[tuple[str, str | None]]:
    """Yield (target_label, engine) for a seam: handles single-engine, multi-engine
    (seam-2), and fan-in bindings (seam-6)."""
    out = []
    if "engines" in seam:  # seam-2: one engine per target class
        for e in seam["engines"]:
            out.append((e.get("target", ""), e.get("engine")))
    elif seam.get("fan_in") and "bindings" in seam:  # seam-6: per physical catalog
        for b in seam["bindings"]:
            out.append((b.get("catalog", ""), b.get("engine", "UNCOVERED")
                        if b.get("coverage") == "COVERED" else "UNCOVERED"))
    else:
        out.append(("", seam.get("engine")))
    return out


def _unit_key(seam: dict, sub_target: str, engine: str | None) -> str:
    """Stable cursor key for one topology binding in deterministic scan order."""
    return "%s:%s" % (seam.get("seam_id", "?"), sub_target or engine or "default")


def _topology_units(topo: dict, only_seams: set[str] | None = None) -> list[tuple[str, dict, str, str | None]]:
    """Expand manifest seams into the exact units walked by the orchestrator."""
    units = []
    for seam in topo.get("seams", []):
        if only_seams and seam["seam_id"] not in only_seams:
            continue
        for sub_target, engine in _seam_engines(seam):
            units.append((_unit_key(seam, sub_target, engine), seam, sub_target, engine))
    return units


def walk_seams(topo: dict, target: str | None, ctx: dict,
               only_seams: set[str] | None = None) -> list[dict]:
    """LIVE PROGRESS ON STDERR + PER-ADAPTER TIMING (NFRA_COMPCLOSE 2026-07-14). The sweep used to
    collect everything and render one board at exit -- and python BLOCK-BUFFERS a piped stdout, so
    an agent's timed-out sweep (the runtime crosses 2-minute defaults on cold caches) showed ZERO
    output and rc=124: a mute death, logged as a tool FAILURE. Measured: that mute-timeout class +
    the honest rc=2 UNVERIFIABLE verdict (already VERDICT-classed in comp_log_auto since 07-08)
    jointly read as 'comp-drift fails ~half its runs' when neither is a defect in the checks
    themselves. Progress goes to STDERR so stdout stays a parseable board/JSON; each line carries
    the adapter's elapsed seconds, so a killed run now shows WHERE it died and WHICH leg is slow."""
    import time as _time
    records = []
    units = _topology_units(topo, only_seams)
    allowed = ctx.get("_allowed_units")
    clock = ctx.get("_clock")
    global _ACTIVE_CLOCK
    for key, seam, sub_target, engine in units:
        if allowed is not None and key not in allowed:
            continue
        if clock is not None and clock.remaining() is not None and clock.remaining() <= 0:
            ctx["_budget_partial"] = True
            ctx.setdefault("_deferred_units", []).append(key)
            continue
        adapter = _adapter_for(engine)
        ctx["_binding"] = sub_target   # per-binding catalog label for fan-in adapters (seam-6)
        t0 = _time.time()
        try:
            sys.stderr.write("  [sweep] %-8s %s ...\n" % (seam["seam_id"], engine or "?"))
            sys.stderr.flush()
        except Exception:  # noqa: BLE001 -- progress is advisory, never fatal
            pass
        try:
            _ACTIVE_CLOCK = clock
            rec = adapter(seam, target, ctx)
        except Exception as exc:  # noqa: BLE001
            rec = _record(seam, target or "?", "UNVERIFIABLE",
                          "adapter raised: %s" % exc)
        finally:
            _ACTIVE_CLOCK = None
        elapsed = _time.time() - t0
        try:
            sys.stderr.write("  [sweep] %-8s %s -> %s (%.1fs)\n"
                             % (seam["seam_id"], engine or "?", rec.get("verdict", "?"), elapsed))
            sys.stderr.flush()
        except Exception:  # noqa: BLE001
            pass
        # If the child was cut off by Rule T, the current binding is not a
        # fully processed cursor unit.  Keep only the completed PREFIX.
        if clock is not None and clock.remaining() is not None and clock.remaining() <= 0:
            ctx["_budget_partial"] = True
            ctx.setdefault("_deferred_units", []).append(key)
            continue
        if sub_target:
            rec["target"] = "%s[%s]" % (rec["target"], sub_target)
            rec["_engine"] = engine
        rec["_elapsed_s"] = round(elapsed, 1)
        records.append(rec)
        ctx.setdefault("_completed_units", []).append(key)
    return records


# the classes that mean a seam was ACTUALLY EVALUATED (a verdict was read from an engine).
# "deferred" (cost-guarded) and "unverifiable" (could-not-read) are NOT among them -- neither
# produced a real parity reading.
_EVALUATED_CLASSES = {"clean", "self_heal", "stale", "break", "dispositioned", "partial"}


def rollup_exit(records: list[dict]) -> int:
    classes = [r["_class"] for r in records]
    cset = set(classes)
    if "break" in cset:
        return EXIT_BREAK
    if "unverifiable" in cset:
        return EXIT_UNVERIFIABLE
    # VERIFIED-NOTHING (NFRA_INSTDRILL item 4): no break, no could-not-read, but also nothing was
    # actually EVALUATED -- every seam was cost-guarded/deferred. A green exit 0 here is the lie
    # (it reads as "estate in parity" when the sweep checked nothing). Exit 2: run --deep.
    if records and not any(c in _EVALUATED_CLASSES for c in classes):
        return EXIT_UNVERIFIABLE
    return EXIT_CLEAN


def _sweep_summary(records: list[dict]) -> str:
    """The loud counts line + the VERIFIED-NOTHING banner when a plain sweep evaluated nothing."""
    from collections import Counter as _C
    c = _C(r["_class"] for r in records)
    evaluated = sum(c[k] for k in _EVALUATED_CLASSES)
    lines = ["",
             "  SWEEP ACCOUNTING: %d evaluated (clean/stale/break/dispositioned) | "
             "%d cost-guarded (deferred -- run --deep) | %d unverifiable (could-not-read)"
             % (evaluated, c.get("deferred", 0), c.get("unverifiable", 0))]
    if records and evaluated == 0:
        lines += [
            "",
            "  " + "!" * 66,
            "  !!  THIS SWEEP VERIFIED NOTHING. Every seam was cost-guarded or could not be",
            "  !!  read -- NOT ONE parity check actually ran. A green result here would be a",
            "  !!  lie. Run `comp-drift sweep --deep` (live engines) or `comp-drift <target>`",
            "  !!  (one artifact's chain) to get a real verdict. Exit 2.",
            "  " + "!" * 66]
    return "\n".join(lines)


# ---- P4: fold drift_producer.py's infra/repo drift legs into the sweep board ----------------
# PRD sec 8 (RULED: FOLD): drift_producer's checks (comp-manifest-check + comp-surface-check +
# terraform-plan) join the estate board. comp-drift ORCHESTRATES drift_producer's leg functions
# (import + call) -- it does NOT re-implement the checks (orchestrator-boundary 4b). The full sec-8
# end-state (sweep EMITS drift_state.json + the infra-monitor Lambda reads it + retire drift_producer)
# is the coordinated deploy-class follow-on; here the sweep FOLDS the disposition into one board.

def _infra_rec(seam_id, stage_from, stage_to, verdict, grounding) -> dict:
    cls = {"DRIFT": "break", "WATCH": "stale", "CLEAN": "clean",
           "UNVERIFIABLE": "unverifiable"}.get(verdict, "unverifiable")
    sev = {"clean": "OK", "stale": "WARN", "unverifiable": "WARN", "break": "ERROR"}[cls]
    return {"seam_id": seam_id, "stage_from": stage_from, "stage_to": stage_to, "target": "<infra>",
            "verdict": verdict, "severity": sev, "operator_action": ACTION[cls],
            "disposition": None, "grounding": grounding, "_class": cls, "_engine": "drift_producer.py"}


def _infra_findings(seam_id, stage_from, stage_to, leg) -> list[dict]:
    findings = leg.get("findings", [])
    if not findings:
        return [_infra_rec(seam_id, stage_from, stage_to, "CLEAN", leg.get("note") or "no drift")]
    out = []
    for f in findings:
        verdict = "DRIFT" if f.get("status") == "red" else "WATCH"  # drift_producer status: red|watch
        src = f.get("module") or f.get("source") or "?"
        out.append(_infra_rec(seam_id, stage_from, stage_to, verdict,
                              "%s: %s" % (src, f.get("reason", ""))))
    return out


def fold_infra_drift(ctx: dict) -> list[dict]:
    """P4: fold drift_producer's infra/repo drift legs into the board. The comp leg
    (manifest + critical-surface) runs in the standard sweep; the terraform leg (tf plan across
    modules -- slow) is cost-guarded to --deep. Never re-implements a check -- calls drift_producer."""
    def can_start(key: str) -> bool:
        allowed = ctx.get("_allowed_units")
        if allowed is not None and key not in allowed:
            return False
        clock = ctx.get("_clock")
        if clock is not None and clock.remaining() is not None and clock.remaining() <= 0:
            ctx["_budget_partial"] = True
            ctx.setdefault("_deferred_units", []).append(key)
            return False
        return True

    try:
        sys.path.insert(0, os.path.join(WORKSPACE, ".tools"))
        import drift_producer as dp
    except Exception as exc:  # noqa: BLE001 -- unavailable producer is a VISIBLE gap, never silent-clean
        return [_infra_rec("infra-comp", "REPO", "SURFACE", "UNVERIFIABLE",
                           "cannot import drift_producer: %s" % exc)]
    records = []
    if can_start("infra-comp"):
        try:
            global _ACTIVE_CLOCK
            _ACTIVE_CLOCK = ctx.get("_clock")
            records.extend(_infra_findings("infra-comp", "REPO", "SURFACE", dp.run_comp_leg()))
        except Exception as exc:  # noqa: BLE001
            records.append(_infra_rec("infra-comp", "REPO", "SURFACE", "UNVERIFIABLE",
                                      "run_comp_leg raised: %s" % exc))
        finally:
            _ACTIVE_CLOCK = None
        if ctx.get("_clock") is None or ctx["_clock"].remaining() is None or ctx["_clock"].remaining() > 0:
            ctx.setdefault("_completed_units", []).append("infra-comp")
        else:
            ctx["_budget_partial"] = True
    if ctx.get("deep") and can_start("infra-tf"):
        try:
            _ACTIVE_CLOCK = ctx.get("_clock")
            records.extend(_infra_findings("infra-tf", "CODE", "INFRA", dp.run_terraform_leg()))
        except Exception as exc:  # noqa: BLE001
            records.append(_infra_rec("infra-tf", "CODE", "INFRA", "UNVERIFIABLE",
                                      "run_terraform_leg raised: %s" % exc))
        finally:
            _ACTIVE_CLOCK = None
        if ctx.get("_clock") is None or ctx["_clock"].remaining() is None or ctx["_clock"].remaining() > 0:
            ctx.setdefault("_completed_units", []).append("infra-tf")
        else:
            ctx["_budget_partial"] = True
    elif not ctx.get("deep") and can_start("infra-tf"):
        records.append(_infra_rec("infra-tf", "CODE", "INFRA", "COST-GUARDED",
                                  "terraform-plan infra-drift leg skipped (cost-guard; --deep to run)"))
        ctx.setdefault("_completed_units", []).append("infra-tf")
    return records


# ---- TARGET CLASSIFY (which seams apply to an artifact) ---------------------

def applicable_seams(target: str) -> set[str] | None:
    t = target.lower()
    if t.endswith(".tf") or "/terraform/" in t or "iam" in t:
        return {"seam-1", "seam-2", "seam-3"}
    if "lambda" in t:
        return {"seam-1", "seam-2", "seam-3"}
    if t.endswith(".py") or "/scripts/gold" in t or t.startswith("gold:"):
        # a gold script: committed -> deployed -> its output flows the full chain
        return None  # full chain
    if t.startswith("s3:") or t.startswith("platinum/") or t.startswith("gold/"):
        return {"seam-5", "seam-6", "seam-7"}
    return None  # unknown -> full chain (loud)


# ---- RENDER ----------------------------------------------------------------

_SEV_TAG = {"OK": "OK  ", "INFO": "INFO", "SKIP": "SKIP", "WARN": "WARN", "ERROR": "FAIL"}


def render_chain(target: str, records: list[dict]) -> str:
    lines = ["comp-drift <target>: %s" % target, ""]
    for r in records:
        lines.append("  [%s] %-7s %s->%s  %-18s  %s" % (
            _SEV_TAG[r["severity"]], r["seam_id"], r["stage_from"], r["stage_to"],
            r["verdict"], r["operator_action"]))
        lines.append("        grounding: %s" % r["grounding"])
    return "\n".join(lines)


def render_board(topo: dict, records: list[dict]) -> str:
    lines = ["comp-drift sweep -- estate propagation board", ""]
    lines.append("  SEAM     STAGE              VERDICT             COVERAGE   ENGINE")
    cov_counts = {}
    for seam in topo.get("seams", []):
        cov = seam.get("coverage", "?")
        cov_counts[cov] = cov_counts.get(cov, 0) + 1
    for r in records:
        seam = next((s for s in topo["seams"] if s["seam_id"] == r["seam_id"]), {})
        cov = seam.get("coverage", "?")
        eng = r.get("_engine") or seam.get("engine", "")
        lines.append("  [%s] %-8s %-18s %-18s %-10s %s" % (
            _SEV_TAG[r["severity"]], r["seam_id"],
            "%s->%s" % (r["stage_from"], r["stage_to"]), r["verdict"], cov, eng))
    # coverage line (the "what's unguarded today" map)
    lines.append("")
    lines.append("  COVERAGE LEDGER: " + " ".join(
        "%s=%d" % (k, v) for k, v in sorted(cov_counts.items())))
    return "\n".join(lines)


def render_coverage(topo: dict) -> str:
    lines = ["comp-drift coverage -- the propagation topology coverage ledger",
             "  (drift-topology.yaml is the SSOT; any GAP is unguarded drift you cannot see)", ""]
    for seam in topo.get("seams", []):
        eng = seam.get("engine", "")
        if "engines" in seam:
            eng = ", ".join(e.get("engine", "?") for e in seam["engines"])
        elif seam.get("fan_in"):
            eng = "fan-in: " + ", ".join(
                "%s=%s" % (b.get("catalog"), b.get("coverage", "GAP")) for b in seam.get("bindings", []))
        lines.append("  %-8s %-16s %-10s %s" % (
            seam["seam_id"], "%s->%s" % (seam["stage_from"], seam["stage_to"]),
            seam.get("coverage", "?"), eng))
        lines.append("        invariant: %s" % seam.get("invariant", ""))
    return "\n".join(lines)


# ---- MAIN ------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    # Line-buffered, uncrashable streams (NFRA_COMPCLOSE 2026-07-14): a piped stdout block-buffers,
    # so a sweep killed mid-run (agent timeout) printed NOTHING -- a mute death indistinguishable
    # from a crash-before-start. Line buffering makes every already-printed row survive the kill.
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(line_buffering=True, errors="replace")
        except Exception:  # noqa: BLE001
            pass
    ap = argparse.ArgumentParser(
        prog="comp-drift",
        description="Estate propagation-drift orchestrator (calls seam engines; never re-implements).")
    ap.add_argument("target", nargs="?",
                    help="artifact to walk (gold script / lambda / graph-node / s3 key), "
                         "or the literal 'sweep' / 'coverage'.")
    ap.add_argument("--deep", action="store_true",
                    help="invoke the live/network engines (lambda/iam/iceberg/code_heat/freshness); "
                         "default cost-guards them.")
    ap.add_argument("--budget", metavar="N", default=None,
                    help="RULE T wall-clock ceiling in seconds for sweep "
                         "(carrier: --budget > env COMP_BUDGET_S > default "
                         "%ss; --budget 0 = unbounded). "
                         "Budget expiry returns rc=3 (PARTIAL_OR_BLIND), distinct from "
                         "rc=0 clean and rc=1 integrity-break; complete rc vocabulary: "
                         "0 clean, 1 integrity-break, 2 unverifiable, 3 partial-budget."
                         % _compbudget.fmt(_compbudget.DEFAULT_BUDGET_S))
    ap.add_argument("--cursor", metavar="UNIT", default=None,
                    help="resume sweep after the last fully processed unit named by a "
                         "BUDGET REACHED line")
    ap.add_argument("--json", action="store_true", help="emit the normalized records as JSON (CI mode).")
    args = ap.parse_args(argv)

    topo = load_topology()
    ctx = {"deep": args.deep}

    mode = args.target
    if mode == "coverage":
        if args.json:
            print(json.dumps({"coverage": [
                {"seam_id": s["seam_id"], "coverage": s.get("coverage"),
                 "stage": "%s->%s" % (s["stage_from"], s["stage_to"])}
                for s in topo["seams"]]}, indent=1))
        else:
            print(render_coverage(topo))
        return EXIT_CLEAN

    if mode == "sweep" or mode is None:
        # sweep: cheap seams always; live engines only under --deep (cost-guard)
        try:
            budget_s, budget_source = _compbudget.resolve_budget(args.budget)
        except ValueError as exc:
            print("comp-drift: ERROR: --budget %s" % exc)
            return EXIT_NOT_DECIDABLE
        planned = [u[0] for u in _topology_units(topo)] + ["infra-comp", "infra-tf"]
        requested = planned
        if args.cursor:
            if args.cursor in planned:
                requested = planned[planned.index(args.cursor) + 1:]
            else:
                print("comp-drift: WARNING: --cursor %r does not match any sweep unit -- "
                      "running the full requested set (no units skipped)." % args.cursor)
        total_units = len(requested)
        clock = _compbudget.Clock(budget_s)
        ctx.update({"_clock": clock, "_budget_s": budget_s, "_budget_source": budget_source,
                    "_allowed_units": set(requested), "_completed_units": [],
                    "_deferred_units": [], "_budget_partial": False})
        records = walk_seams(topo, None, ctx)
        records.extend(fold_infra_drift(ctx))   # P4: fold drift_producer's infra/repo drift legs (PRD sec 8)
        completed = list(ctx.get("_completed_units", []))
        partial = bool(ctx.get("_budget_partial")) or len(completed) < total_units
        code = EXIT_NOT_DECIDABLE if partial else rollup_exit(records)
        used_s = round(clock.elapsed(), 2)
        if args.json:
            print(json.dumps({"mode": "sweep", "exit": code, "records": _strip(records),
                              "budget": {"scanned": len(completed), "total": total_units,
                                         "deferred": len(ctx.get("_deferred_units", [])),
                                         "budget_s": budget_s, "source": budget_source,
                                         "used_s": used_s,
                                         "state": STATE_PARTIAL_BLIND if partial else None,
                                         "cursor": completed[-1] if completed else None}}, indent=1))
        else:
            print("  " + _compbudget.disclosure_line(budget_s, budget_source))
            print(render_board(topo, records))
            print(_sweep_summary(records))
            if partial:
                if completed:
                    args_repr = "comp-drift sweep --deep" if args.deep else "comp-drift sweep"
                    print("  " + _compbudget.budget_reached_line(
                        budget_s, budget_source, len(completed), total_units, "sweep_unit",
                        args_repr, completed[-1]))
                else:
                    print("  BUDGET REACHED: %s s (%s); scanned 0 of %d sweep_unit(s); results are "
                          "a PREFIX, not the answer; NO CURSOR YET: no unit completed before "
                          "the budget hit, so there is no last-processed unit to resume from; "
                          "resume: re-run with a larger --budget."
                          % (_compbudget.fmt(budget_s), budget_source, total_units))
                print("  ANSWER-STATE: %s" % STATE_PARTIAL_BLIND)
                print("  STATE: %s (rc=%d, distinct from clean rc=0, integrity-break rc=1, "
                      "and seam-unverifiable rc=2 -- a PREFIX carries no verdict)"
                      % (STATE_PARTIAL_BLIND, EXIT_NOT_DECIDABLE))
            else:
                print("  " + _compbudget.within_budget_line(
                    len(completed), total_units, "sweep_unit", budget_s, budget_source, used_s))
            print("\n  EXIT: %d (%s)" % (code, _exit_label(code)))
        return code

    # <target> mode: walk the artifact's applicable seams
    only = applicable_seams(mode)
    records = walk_seams(topo, mode, ctx, only_seams=only)
    code = rollup_exit(records)
    if args.json:
        print(json.dumps({"mode": "target", "target": mode, "exit": code,
                          "records": _strip(records)}, indent=1))
    else:
        print(render_chain(mode, records))
        print("\n  EXIT: %d (%s)" % (code, _exit_label(code)))
    return code


def _strip(records: list[dict]) -> list[dict]:
    return [{k: v for k, v in r.items() if not k.startswith("_")} for r in records]


def _exit_label(code: int) -> str:
    return {0: "clean-or-dispositioned", 1: "integrity-break",
            2: "unverifiable", 3: "partial-budget"}.get(code, "?")


def _drift_self_test() -> int:
    """Offline: the classifier + rollup + verified-nothing banner (NFRA_INSTDRILL item 4). No engines."""
    results = []
    def ck(name, ok, detail=""):
        results.append(ok)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"   ({detail})" if detail else ""))

    def rec(cls_verdict):
        return _record({"seam_id": "s", "stage_from": "a", "stage_to": "b"}, "t", cls_verdict, "g")

    # 1. cost-guarded is DEFERRED, not unverifiable -- the whole point of the fix.
    ck("deferred.distinct_from_unverifiable",
       _classify("COST-GUARDED") == "deferred" and _classify("UNVERIFIABLE") == "unverifiable")

    # 2. VERIFIED-NOTHING: a plain sweep of only cost-guarded seams exits 2 (not a green 0).
    all_deferred = [rec("COST-GUARDED") for _ in range(6)]
    ck("verified_nothing.all_deferred_exits_2", rollup_exit(all_deferred) == EXIT_UNVERIFIABLE)
    ck("verified_nothing.banner_fires", "VERIFIED NOTHING" in _sweep_summary(all_deferred))

    # 3. >=1 real evaluation flips it to a real verdict: deferred + one CLEAN -> exit 0, no banner.
    mixed = [rec("COST-GUARDED"), rec("COST-GUARDED"), rec("CLEAN")]
    ck("one_real_eval.exits_clean", rollup_exit(mixed) == EXIT_CLEAN)
    ck("one_real_eval.no_banner", "VERIFIED NOTHING" not in _sweep_summary(mixed))

    # 4. a genuine break still dominates; a genuine unverifiable still exits 2.
    ck("break.dominates", rollup_exit([rec("COST-GUARDED"), rec("STALE")]) == EXIT_BREAK)
    ck("genuine_unverifiable.exits_2",
       rollup_exit([rec("CLEAN"), rec("UNVERIFIABLE")]) == EXIT_UNVERIFIABLE)

    # 5. empty (no records) is not a false verified-nothing.
    ck("empty.no_false_banner", "VERIFIED NOTHING" not in _sweep_summary([]))

    # T-14 AC-2 fixture control: keep the four ratified answer-state spellings
    # machine-visible and pairwise distinct in one invocation.  Production
    # sweep records retain their engine-native verdicts; this control prevents
    # a future result consumer from collapsing the state vocabulary.
    planted_states = [STATE_SUBJECT_ABSENT, STATE_PRESENT_ZERO,
                      STATE_PARTIAL_BLIND, STATE_NOT_APPLICABLE]
    for state in planted_states:
        print("  ANSWER-STATE: %s" % state)
    ck("answer_state.four_distinct_tokens",
       len(planted_states) == 4 and len(set(planted_states)) == 4)

    ok = all(results)
    print("\n" + ("OK: all comp-drift self-test cases pass" if ok else "ERROR: comp-drift self-test FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(_drift_self_test())
    sys.exit(main())
