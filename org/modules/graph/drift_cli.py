from __future__ import annotations

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

import argparse
import json
import os
import re
import shutil
import subprocess
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.stderr.write("comp-drift: PyYAML required (pip install pyyaml)\n")
    sys.exit(2)

WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
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
EXIT_CLEAN, EXIT_BREAK, EXIT_UNVERIFIABLE = 0, 1, 2

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
# Operator action per verdict-class (the normalized "what do I do").
ACTION = {
    "clean": "none",
    "break": "reconcile -- redeploy/repoint/re-derive to restore parity",
    "unverifiable": "investigate -- could not read the seam; do NOT assume clean",
    "dispositioned": "disposition -- abandoned artifact; clean up (not fix)",
    "self_heal": "none -- self-heals on HEAD-advance (informational)",
    "partial": "note -- partial coverage; the equality is not fully asserted",
}


def load_topology() -> dict:
    with open(TOPOLOGY, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def _run(cmd: list[str], timeout: int = 120) -> tuple[int, str]:
    """Invoke an engine as a black box. Returns (returncode, combined stdout+stderr).
    A non-zero rc is NOT inherently a break -- each adapter maps the engine's OWN
    verdict; rc is only a fallback signal."""
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


def _classify(verdict: str) -> str:
    v = (verdict or "").upper()
    if v in {x.upper() for x in UNVERIFIABLE_VERDICTS}:
        return "unverifiable"
    if v in {x.upper() for x in BREAK_VERDICTS}:
        return "break"
    if v in {"ABANDONED-ARTIFACT", "DISPOSITIONED", "NOT-LIVE"}:
        return "dispositioned"
    if v in {"REFRESHING", "SELF-HEALING"}:
        return "self_heal"
    return "clean"


def _record(seam: dict, target: str, verdict: str, grounding: str,
            disposition: str | None = None) -> dict:
    """The normalized cross-seam drift-record envelope (PRD arch-gate (c))."""
    cls = _classify(verdict)
    sev = {"clean": "OK", "self_heal": "OK", "partial": "INFO",
           "dispositioned": "INFO", "unverifiable": "WARN", "break": "ERROR"}[cls]
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
        return _record(seam, "<working-tree>", "UNVERIFIABLE",
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
        return _record(seam, "<all-gold>", "UNVERIFIABLE",
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
        return _record(seam, target or "<lambda>", "UNVERIFIABLE",
                       "live 3-leg sha read skipped (cost-guard; run with --deep or a <target>)")
    rc, out = _bash("comp-lambdamap", "parity", *([target] if target else []))
    # HARDENED (grounded on real parity output): parse per-verdict COUNTS, not a token-scan.
    # The summary line prints EVERY verdict token with its count ("MATCH: 131 | STALE-RECORD: 0
    # | ... | POSSIBLE-HALF-LANDED: 0 | ... | NO-RECORD: 40"), so a token-first-match ALWAYS
    # false-flags POSSIBLE-HALF-LANDED (present at 0-count) as an integrity BREAK. DISPOSITIONED
    # = intentional divergence (not a break); NO-RECORD = uncovered/unchecked (coverage note,
    # never-silent -- must not read as fully-verified-clean).
    counts = {m.group(1): int(m.group(2)) for m in re.finditer(
        r"(MATCH|STALE-RECORD|DISPOSITIONED|SETTLING|POSSIBLE-HALF-LANDED|"
        r"CORRUPT-RECORD|NOT-LIVE|UNVERIFIABLE|NO-RECORD):\s*(\d+)", out)}
    if not counts:
        return _record(seam, target or "<lambda>", "UNVERIFIABLE",
                       "comp-lambdamap parity rc=%s (verdict counts unparsed -- not assuming MATCH)" % rc)
    hot = [(t, counts[t]) for t in ("POSSIBLE-HALF-LANDED", "STALE-RECORD", "CORRUPT-RECORD")
           if counts.get(t)]
    if hot:
        return _record(seam, target or "<lambda>", hot[0][0],
                       "comp-lambdamap parity: " + ", ".join("%d %s" % (c, t) for t, c in hot))
    if counts.get("NOT-LIVE") or counts.get("UNVERIFIABLE"):
        return _record(seam, target or "<lambda>", "UNVERIFIABLE",
                       "comp-lambdamap parity: %d NOT-LIVE / %d UNVERIFIABLE"
                       % (counts.get("NOT-LIVE", 0), counts.get("UNVERIFIABLE", 0)))
    note = "%d MATCH" % counts.get("MATCH", 0)
    if counts.get("DISPOSITIONED"):
        note += ", %d DISPOSITIONED (intentional)" % counts["DISPOSITIONED"]
    if counts.get("NO-RECORD"):
        note += ", %d NO-RECORD UNCHECKED" % counts["NO-RECORD"]
    return _record(seam, target or "<lambda>", "MATCH",
                   "comp-lambdamap parity: %s -- no integrity break" % note)


def adapter_comp_iam(seam, target, ctx):
    if not ctx.get("deep"):
        return _record(seam, target or "<iam>", "UNVERIFIABLE",
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
        verdict = "BEHIND"
        ground = "comp-kuzu provenance: BEHIND (self-heals on next read)"
    elif "unknown vintage" in low or "unknown-vintage" in low:
        verdict = "UNKNOWN-VINTAGE"
        ground = "comp-kuzu provenance: UNKNOWN VINTAGE (freshness unverifiable)"
    else:
        verdict = "UNVERIFIABLE"
        ground = "comp-kuzu provenance header unreadable rc=%s" % rc
    return _record(seam, target or "<graph>", verdict, ground)


def adapter_iceberg_parity(seam, target, ctx):
    if not ctx.get("deep"):
        return _record(seam, target or "<iceberg>", "UNVERIFIABLE",
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
        return _record(seam, target or "<code_heat>", "UNVERIFIABLE",
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


def adapter_comp_freshness(seam, target, ctx):
    if not ctx.get("deep"):
        return _record(seam, target or "<served>", "UNVERIFIABLE",
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


def walk_seams(topo: dict, target: str | None, ctx: dict,
               only_seams: set[str] | None = None) -> list[dict]:
    records = []
    for seam in topo.get("seams", []):
        if only_seams and seam["seam_id"] not in only_seams:
            continue
        for sub_target, engine in _seam_engines(seam):
            adapter = _adapter_for(engine)
            try:
                rec = adapter(seam, target, ctx)
            except Exception as exc:  # noqa: BLE001
                rec = _record(seam, target or "?", "UNVERIFIABLE",
                              "adapter raised: %s" % exc)
            if sub_target:
                rec["target"] = "%s[%s]" % (rec["target"], sub_target)
                rec["_engine"] = engine
            records.append(rec)
    return records


def rollup_exit(records: list[dict]) -> int:
    classes = {r["_class"] for r in records}
    if "break" in classes:
        return EXIT_BREAK
    if "unverifiable" in classes:
        return EXIT_UNVERIFIABLE
    return EXIT_CLEAN


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

_SEV_TAG = {"OK": "OK  ", "INFO": "INFO", "WARN": "WARN", "ERROR": "FAIL"}


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
    ap = argparse.ArgumentParser(
        prog="comp-drift",
        description="Estate propagation-drift orchestrator (calls seam engines; never re-implements).")
    ap.add_argument("target", nargs="?",
                    help="artifact to walk (gold script / lambda / graph-node / s3 key), "
                         "or the literal 'sweep' / 'coverage'.")
    ap.add_argument("--deep", action="store_true",
                    help="invoke the live/network engines (lambda/iam/iceberg/code_heat/freshness); "
                         "default cost-guards them.")
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
        records = walk_seams(topo, None, ctx)
        code = rollup_exit(records)
        if args.json:
            print(json.dumps({"mode": "sweep", "exit": code, "records": _strip(records)}, indent=1))
        else:
            print(render_board(topo, records))
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
            2: "unverifiable"}.get(code, "?")


if __name__ == "__main__":
    sys.exit(main())
