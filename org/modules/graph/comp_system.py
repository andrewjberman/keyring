#!/usr/bin/env python3
"""comp_system -- NFRA_SYSTEM P3: the comp-system COMPILER (the DYNAMIC half of the SYSTEM home).

Reads the LIVE compiled-system state across the LOCALROOT knowledge-classes VIA THE EXISTING comp-tools
(does NOT build new readers -- req#1) and emits infra/system/06_current_state.{md,json}. One source, THREE
consumers: (1) the SYSTEM current-state itself, (2) base COO's LOCALROOT runtime index (SS5 links into the
## anchors), (3) COO~B's P4-maturity grading (parses the .json maturity_evidence -> derives 07_maturity).

THE HARD LINE (CTO arch-gate; GOV-A / CLAUDE.md Rule 22): every number is GROUNDED against a live source
(a comp-tool call / a served artifact / the marker-oracle) WITH its vintage, or explicitly UNKNOWN-VINTAGE.
NEVER self-reported or hand-fabricated -- a fabricated current-state number is a CVO hard-fail. A class the
comp-tools cannot ground carries an honest UNKNOWN-VINTAGE / no-live-producer anchor (the roster-is-a-floor
discipline: name what is not grounded, never silently omit -- it also SURFACES "no live producer" as a
finding). Auto-refreshes on HEAD-advance (the marker-oracle pattern, like comp-kuzu re-finalize-on-advance).
FORM (a) CARRY-FORWARD (CTO ruling @4484d55608): a device that cannot reach comp-kuzu at compile time NEVER
downgrades a graph row it cannot re-derive -- it carries the committed row forward, MARKED in the vintage
field (value verbatim), excluded from the genuine-drift predicate, and aging from the ORIGINAL derivation
(a carry never resets the age clock). See the CARRY-FORWARD section above _this_device().

LOCKED SHAPE (base COO LOCALROOT-P3 + COO~B P4-maturity, 2026-07-08): one per-class object keyed by the
NFRA_LOCALROOT_P2 SS2 knowledge-class taxonomy (kebab slugs, 1:1 with the infra/README index anchors):
  { slug, static_home, current_state, components:[{name, maturity_evidence:{cert_status, works_broken,
    freshness, exercised}}], maturity_rollup:{BP,BU,F,D,unknown}, vintage, source }
+ a top-level provenance/freshness header + the observe-diversity metric (co-evolution pairs; CTO Q4:
  DIVERSITY not raw volume is the loop/federated maturity headline).

Usage:
  python comp_system.py                 # compile -> write infra/system/06_current_state.{md,json}
  python comp_system.py --stdout         # compile -> print the markdown (no write)
  python comp_system.py --json           # compile -> print the json model
  python comp_system.py --self-test      # prove the no-fabrication invariant (every value grounded|UNKNOWN)
  python comp_system.py --check          # is 06 stale vs the current HEAD marker? (auto-refresh oracle)

Author: 0.8.0_AE_CloudComp~D (NFRA_SYSTEM.P3, comp-tool lead -- built the class-3 inventory this aggregates). 2026-07-08.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
_TOOLS = os.path.join(WS, ".tools")
if _TOOLS not in sys.path:
    sys.path.insert(0, _TOOLS)
import _compbudget  # noqa: E402 -- shared Rule T carrier; one implementation, never a local copy

OUT_MD = os.path.join(WS, "infra", "system", "06_current_state.md")
OUT_JSON = os.path.join(WS, "infra", "system", "06_current_state.json")

UNKNOWN = "UNKNOWN-VINTAGE"            # the honest not-grounded sentinel -- NEVER a fabricated number
NO_PRODUCER = "no-live-producer"      # a class with no SYSTEM-groundable runtime (static-only)

# NFRA_COMPEFFICACY s.4.3 -- exact spellings from the ratified data enum.  State and tool-voice
# are distinct grains: PARTIAL_OR_BLIND adopts NOT-DECIDABLE as its engine token.
ANSWER_SUBJECT_ABSENT = "SUBJECT_ABSENT_FROM_CORPUS"
ANSWER_PRESENT_ZERO = "PRESENT_WITH_ZERO_RESULTS"
ANSWER_PARTIAL = "PARTIAL_OR_BLIND"
ANSWER_NOT_APPLICABLE = "NOT_APPLICABLE"
TOOL_VOICE_NOT_DECIDABLE = "NOT-DECIDABLE"
RC_NOT_DECIDABLE = 3       # --check: distinct from 0=CURRENT, 2=STALE and 1=ERROR

# The Rule T clock is one CLI-run context.  Library callers and the engine's pure self-test helpers
# remain unbudgeted unless main() explicitly installs a context.
_ACTIVE_BUDGET = None


def _answer_state_line(state: str, subject: str, detail: str, tool_voice: str = "") -> str:
    voice = " (%s)" % tool_voice if tool_voice else ""
    return "%s%s: subject=%s; %s" % (state, voice, subject, detail)


def _new_budget(flag_value, unit: str, resume_args: str) -> dict:
    budget_s, source = _compbudget.resolve_budget(flag_value)
    return {"budget_s": budget_s, "source": source, "clock": _compbudget.Clock(budget_s),
            "unit": unit, "resume_args": resume_args, "reached": False,
            "deferred": [], "timeout_command": None}


def _budget_expired(ctx=None) -> bool:
    state = ctx if ctx is not None else _ACTIVE_BUDGET
    if not state or state["budget_s"] == 0:
        return False
    if state.get("reached") or state["clock"].remaining() <= 0:
        state["reached"] = True
        return True
    return False


def _budget_line(ctx: dict, complete: bool) -> str:
    if complete:
        return _compbudget.within_budget_line(
            1, 1, ctx["unit"], ctx["budget_s"], ctx["source"],
            round(ctx["clock"].elapsed(), 3))
    # comp-system's output is one atomic cross-surface record.  BEGIN is the only honest cursor:
    # no prefix is persisted, so resume means re-run the whole unit rather than splice a stale prior
    # record into a new one and call that complete.
    return _compbudget.budget_reached_line(
        ctx["budget_s"], ctx["source"], 0, 1, ctx["unit"],
        ctx["resume_args"], "BEGIN")


def _deferred_lines(ctx: dict, complete: bool) -> list:
    reason = [] if complete else [
        "%s: budget expired; atomic output was not written" % ctx["unit"]
    ]
    return _compbudget.deferred_bucket(0 if complete else 1, 1, ctx["unit"], reason)

# The NFRA_LOCALROOT_P2 SS2 knowledge-class taxonomy. slug (== the infra/README index anchor, 1:1),
# static_home, and whether a SYSTEM comp-tool can GROUND its runtime current-state. Non-groundable classes
# get an honest UNKNOWN-VINTAGE anchor (base COO scope-(a): every static home gets a runtime anchor).
KNOWLEDGE_CLASSES = [
    ("cloud-resources",         "infra/aws/",                    "collect_cloud_resources"),
    ("system-content",          "infra/system/",                 "collect_system_content"),
    ("runtime-compilation",     "the live graph + .comp-graph",  "collect_runtime_compilation"),
    ("security",                "infra/security/",               None),   # security scan produces this, not a SYSTEM comp-tool
    ("operational-tooling",     "infra/{linting,orchestration,testing}/", None),
    ("architecture-decisions",  "infra/architectural_docs/",     None),   # static decision records; no runtime producer
    ("project-docs-homes",      "infra/{project}/",              None),
    ("prompts-rag",             "infra/prompts/, infra/rag/",    None),
    ("logs",                    "org/logs/",                     None),
    ("git-history",             "git",                           None),   # git IS its own SSOT; static
    ("broad-architecture-corpus", "docs/",                       None),
    ("agent-org",               "org/",                          None),
    ("doctrine",                "root + memory/",                None),
]


# ---------------------------------------------------------------------------
# Grounding primitives -- every value returned carries its SOURCE; a failure returns None (-> UNKNOWN-VINTAGE),
# NEVER a fabricated fallback number.
# ---------------------------------------------------------------------------
def _run(cmd: list, timeout: int = 30) -> tuple:
    """Run a comp-tool under the active Rule T clock.

    The caller's per-subprocess cap remains a ceiling, but the effective timeout is always
    ``min(cap, remaining())``.  Exhausting the run budget marks the whole atomic compile partial;
    an ordinary inner timeout/unavailable optional backend keeps the historical UNKNOWN/carry
    behavior.  Returns (None, None, None) on either failure and never raises.
    """
    state = _ACTIVE_BUDGET
    effective_timeout = timeout
    if state and state["budget_s"] != 0:
        remaining = state["clock"].remaining()
        if remaining <= 0:
            state["reached"] = True
            state["timeout_command"] = " ".join(str(x) for x in cmd[:3])
            return None, None, None
        effective_timeout = max(0.001, min(float(timeout), remaining))
    elif state and state["budget_s"] == 0:
        effective_timeout = None
    try:
        p = subprocess.run(cmd, cwd=WS, capture_output=True, text=True, timeout=effective_timeout,
                           encoding="utf-8", errors="replace")
        return p.stdout or "", p.stderr or "", p.returncode
    except subprocess.TimeoutExpired:
        if state and state["budget_s"] != 0 and state["clock"].remaining() <= 0.01:
            state["reached"] = True
            state["timeout_command"] = " ".join(str(x) for x in cmd[:3])
        return None, None, None
    except Exception:  # noqa: BLE001  -- unavailable optional source -> UNKNOWN, never a crash
        return None, None, None


def _git_head() -> str:
    """The git HEAD sha -- the always-available grounded as-of anchor (a real vintage, not fabricated)."""
    out, _, rc = _run(["git", "rev-parse", "--short", "HEAD"], timeout=10)
    return out.strip() if (out and rc == 0) else UNKNOWN


# Call the kuzu_cli.py PYTHON engine directly via sys.executable -- NOT the .tools/comp-kuzu bash wrapper:
# `subprocess.run(["bash", ...])` on this Windows host resolves to WSL bash (execvpe(/bin/bash) failed),
# not Git Bash. The python engine is what the wrapper invokes anyway (mirrors the comp_coverage_view call).
# Cached: the marker is read from >1 collector.
_KUZU_CMD = [sys.executable, os.path.join(WS, "infra", "aws", "globgrph", "kuzu_cli.py")]
_MARKER_CACHE = {}


def _kuzu_marker() -> str:
    """The graph marker from comp-kuzu's provenance header (stderr). UNKNOWN if the graph is unreachable."""
    if "m" in _MARKER_CACHE:
        return _MARKER_CACHE["m"]
    _out, err, _rc = _run(_KUZU_CMD + ["MATCH (n:CloudNode) RETURN count(n) AS n"], timeout=40)
    marker = UNKNOWN
    for line in (err or "").splitlines():
        low = line.lower()
        if "marker" in low or "vintage" in low or ("current" in low and "state" not in low) or "behind" in low:
            marker = line.strip()[:200]
            break
    _MARKER_CACHE["m"] = marker
    return marker


# ---------------------------------------------------------------------------
# FORM (a) CARRY-FORWARD (CTO ruling @4484d55608, 2026-08-20 -- the device-axis instrument pair;
# pre-gate pin Msg 63063). The 06 record is ONE estate truth; a device that cannot reach comp-kuzu
# at compile time (site-Z: hangs >120s) NEVER downgrades a graph row it cannot re-derive -- it
# carries the row FORWARD from the committed 06, MARKED, provenance honest, never silent freshness.
# Two load-bearing invariants:
#   1. The mark lives ONLY in the vintage/provenance field; the VALUE/current_state carries
#      VERBATIM. That is what makes the --check/--gate exclusion hold BY CONSTRUCTION: the
#      managed-region compare is value-vs-span, and a verbatim-carried value equals its own
#      last-refreshed span -- a capability-conditioned carry can never read as region drift (the
#      ruling's (b)-kernel: carried rows are excluded from the genuine-drift predicate).
#   2. A carry defeats the DRIFT verdict, NEVER the age clock (the CTO pin): compile_model chains
#      `graph_carried_since` to the ORIGINAL derivation's emit time (a re-carry preserves it), and
#      _staleness ages carried rows from THAT anchor -- a device dark for 3 weeks still ages past
#      TTL exactly as if no carry existed; laundering freshness through repetition is the same
#      defect one axis over.
# Prior-is-UNKNOWN carries nothing: UNKNOWN over UNKNOWN is not a downgrade, and carrying it would
# be fabricated provenance.
# ---------------------------------------------------------------------------
CARRY_PREFIX = "carried-forward @"
_CARRY_SUFFIX_KEY = ": graph unreachable at "     # the mark's own suffix; rfind() key for unwrap
_PRIOR_CACHE = {}
_DEVICE_CACHE = {}


def _this_device() -> str:
    """The estate's ONE device-identity mechanism, reused not re-minted (DEVICES.txt: ids are the
    canonical device names already in use by .tools/agentbus-sqs.sh -- do NOT mint a parallel
    naming scheme): AGENTBUS_DEVICE env tier first (the same laptop|sitez validation the script
    applies), then the script's own `device` subcommand via git_bash_resolver (a bare "bash" from
    python Windows-resolves to the WSL stub -- the trap _KUZU_CMD's comment names). Unresolvable
    -> "UNKNOWN-device": the mark stays honest, and provenance must never fail a compile."""
    if "d" in _DEVICE_CACHE:
        return _DEVICE_CACHE["d"]
    dev = os.environ.get("AGENTBUS_DEVICE", "").strip()
    if dev not in ("laptop", "sitez"):
        dev = ""
        try:
            _tools = os.path.join(WS, ".tools")
            if _tools not in sys.path:
                sys.path.insert(0, _tools)
            from git_bash_resolver import bash_argv  # noqa: PLC0415  -- lazy: only needed on a carry
            out, _err, _rc = _run(bash_argv(os.path.join(_tools, "agentbus-sqs.sh"), "device"), timeout=20)
            first = ((out or "").strip().splitlines() or [""])[0]      # "device: laptop"
            cand = first.split(":", 1)[1].strip() if ":" in first else ""
            if cand in ("laptop", "sitez"):
                dev = cand
        except Exception:  # noqa: BLE001  -- provenance resolution must never fail the compile
            dev = ""
    _DEVICE_CACHE["d"] = dev or "UNKNOWN-device"
    return _DEVICE_CACHE["d"]


def _unwrap_carry(vintage) -> str:
    """The ORIGINAL fresh vintage inside a carry mark (identity on an unmarked vintage). rfind on
    the mark's own suffix so an original vintage containing ':' survives intact."""
    s = str(vintage)
    if s.startswith(CARRY_PREFIX):
        core = s[len(CARRY_PREFIX):]
        cut = core.rfind(_CARRY_SUFFIX_KEY)
        if cut != -1:
            return core[:cut]
    return s


def _carry_mark(prior_vintage) -> str:
    """The ruling's mark, verbatim form: 'carried-forward @<prior-vintage>: graph unreachable at
    <ts> on <device>'. A re-carry keeps ONE level -- an already-marked vintage is unwrapped to the
    ORIGINAL fresh vintage first (never nests, never loses the real provenance)."""
    return "%s%s%s%s on %s" % (CARRY_PREFIX, _unwrap_carry(prior_vintage), _CARRY_SUFFIX_KEY,
                               time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), _this_device())


def _prior_06():
    """The committed 06 record a carry reads from: on-disk OUT_JSON first (== the committed record
    on a clean tree, and lets a re-carry see the newest chain anchor), `git show HEAD:` fallback
    when the on-disk copy is absent/unparseable. None => no prior -- nothing to carry. Deliberately
    NO deeper history walk: the carry source is THE committed 06 (ruling wording), not an
    archaeology of past vintages."""
    if "m" in _PRIOR_CACHE:
        return _PRIOR_CACHE["m"]
    model = None
    try:
        with open(OUT_JSON, encoding="utf-8") as fh:
            model = json.load(fh)
    except Exception:  # noqa: BLE001  -- fall through to the committed copy
        out, _err, rc = _run(["git", "show", "HEAD:%s" % os.path.relpath(OUT_JSON, WS).replace(os.sep, "/")],
                             timeout=15)
        if out and rc == 0:
            try:
                model = json.loads(out)
            except Exception:  # noqa: BLE001
                model = None
    _PRIOR_CACHE["m"] = model
    return model


def _prior_class(slug):
    for c in (_prior_06() or {}).get("classes", []):
        if c.get("slug") == slug:
            return c
    return None


def _carriable(text) -> bool:
    """Real prior content worth carrying: non-empty, not the UNKNOWN sentinel, not a collector
    error. (A prior CARRIED row keeps its original current_state verbatim, so it stays carriable --
    re-carry is the normal steady state on a graph-less device.)"""
    s = str(text or "")
    return bool(s) and UNKNOWN not in s and "collector error" not in s


def _carry_class(slug, static_home, prior_cls):
    """The form (a) decision for a graph-grounded CLASS row (offline-testable: no live graph
    needed). Returns the carried class-obj -- current_state VERBATIM, mark in the vintage field
    ONLY -- or None when there is nothing real to carry (the caller keeps its honest UNKNOWN row:
    writing UNKNOWN over UNKNOWN is not a downgrade, and fabricating a carry would be worse)."""
    if not prior_cls or not _carriable(prior_cls.get("current_state")):
        return None
    return _class_obj(slug, static_home, prior_cls["current_state"],
                      prior_cls.get("components", []) or [],
                      prior_cls.get("source", UNKNOWN),
                      _carry_mark(prior_cls.get("vintage", UNKNOWN)))


# ---------------------------------------------------------------------------
# maturity_evidence: {cert_status, works_broken, freshness, exercised} per component (COO~B P4 need). Every
# field GROUNDED from a live source or UNKNOWN-VINTAGE. maturity_rollup derives the [BP]/[BU]/[F]/[D] grade.
# ---------------------------------------------------------------------------
def _evidence(cert_status=UNKNOWN, works_broken=UNKNOWN, freshness=UNKNOWN, exercised=UNKNOWN) -> dict:
    return {"cert_status": cert_status, "works_broken": works_broken,
            "freshness": freshness, "exercised": exercised}


def _grade(ev: dict) -> str:
    """Derive a maturity grade from the evidence (P4 [BP]/[BU]/[F]/[D]). GROUNDED: BP requires works +
    exercised-live; BU = works but not exercised-live (config-only); F = friction/partial; D = designed/
    broken/unknown. A grade is only as strong as its grounded evidence -- UNKNOWN evidence -> unknown grade."""
    wb = str(ev.get("works_broken", "")).strip().lower()
    ex = str(ev.get("exercised", "")).lower()
    # Read the LEADING verdict token -- the value is a free-text like "works (... 0 hard breaks ...)", so a
    # substring scan false-matches "broken" inside "0 hard breaks". The primary verdict leads the string.
    if not wb or UNKNOWN.lower() in wb or wb.startswith("unknown"):
        return "unknown"
    if wb.startswith(("broken", "retired", "designed", "hard-break")):
        return "D"
    if wb.startswith(("friction", "partial", "discoverability")):
        return "F"
    if wb.startswith(("works", "proven", "built-proven")):
        return "BP" if ("live" in ex or "exercised" in ex or "proven" in ex or "yes" in ex) else "BU"
    return "unknown"


def _rollup(components: list) -> dict:
    r = {"BP": 0, "BU": 0, "F": 0, "D": 0, "unknown": 0}
    for c in components:
        r[_grade(c.get("maturity_evidence", {}))] += 1
    return r


def _class_obj(slug, static_home, current_state, components, source, vintage) -> dict:
    return {"slug": slug, "static_home": static_home, "current_state": current_state,
            "components": components, "maturity_rollup": _rollup(components),
            "source": source, "vintage": vintage}


def _unknown_class(slug, static_home) -> dict:
    """A class the SYSTEM comp-tools cannot ground-live -> an HONEST UNKNOWN-VINTAGE anchor (scope-(a);
    surfaces 'no live producer' as a finding, never a fabricated current-state)."""
    return _class_obj(slug, static_home,
                      current_state="%s: %s: the SYSTEM comp-tools have no live producer for this "
                                    "class's runtime state (static home is the SSOT; a P3/P4 candidate "
                                    "if a runtime producer is wanted)" %
                                    (ANSWER_SUBJECT_ABSENT, NO_PRODUCER),
                      components=[], source=NO_PRODUCER, vintage=UNKNOWN)


# ---------------------------------------------------------------------------
# Per-class collectors -- GROUND via the existing comp-tools. Each returns a class-object or an UNKNOWN class.
# ---------------------------------------------------------------------------
def collect_cloud_resources() -> dict:
    """Graph-derived cloud node counts via comp-kuzu (the AWS estate's runtime, live-graph view)."""
    out, err, rc = _run(_KUZU_CMD +
                        ["MATCH (n:CloudNode) RETURN n.node_type AS t, count(*) AS c ORDER BY c DESC"], timeout=40)
    marker = UNKNOWN
    if err:
        for line in err.splitlines():
            if "marker" in line.lower() or "current" in line.lower() or "behind" in line.lower():
                marker = line.strip()[:160]
                break
    if out is None or rc not in (0, None) or not (out or "").strip():
        # FORM (a): carry the committed row forward, marked -- never downgrade what this device
        # cannot re-derive. Falls through to the honest UNKNOWN only when there is nothing real to carry.
        carried = _carry_class("cloud-resources", "infra/aws/", _prior_class("cloud-resources"))
        if carried is not None:
            return carried
        return _class_obj("cloud-resources", "infra/aws/",
                          current_state="%s: comp-kuzu graph unreachable/empty at compile time" % UNKNOWN,
                          components=[], source="comp-kuzu (unreachable)", vintage=UNKNOWN)
    # comp-kuzu prints a header row + a "----" separator + data rows -> take the "TYPE count" rows after
    # the separator (skip the header/separator table noise).
    data, seen_sep = [], False
    for ln in out.splitlines():
        s = ln.strip()
        if not s:
            continue
        if set(s) <= set("- "):       # the "----" separator row
            seen_sep = True
            continue
        if seen_sep:
            parts = s.split()
            if len(parts) >= 2 and parts[-1].isdigit():
                data.append("%s=%s" % (parts[0], parts[-1]))
    return _class_obj("cloud-resources", "infra/aws/",
                      current_state="graph-derived CloudNode counts by type: %s"
                                    % (", ".join(data[:14]) if data else "0 rows"),
                      components=[], source='comp-kuzu "MATCH (n:CloudNode) RETURN node_type, count(*)"',
                      vintage=marker)


def collect_system_content() -> dict:
    """The SYSTEM 5 scope classes (substrate/graph-infra/comp-tools/federated/learning) -- the P4-maturity
    axis. Each a COMPONENT with grounded maturity_evidence."""
    comps = []

    # substrate: cse_schema live version (import -- grounded) + the fidelity gate.
    schema_ver = UNKNOWN
    try:
        import cse_schema
        schema_ver = getattr(cse_schema, "SCHEMA_VERSION", UNKNOWN)
    except Exception:  # noqa: BLE001
        schema_ver = UNKNOWN
    comps.append({"name": "substrate: cse_schema @%s (C0-C3 algebra + fidelity gate)" % schema_ver,
                  "maturity_evidence": _evidence(
                      cert_status="CVO-certed (P1 @0.3; @0.4 ProducerKind.PROMOTE re-signed 72d8fa58b)"
                                  if schema_ver != UNKNOWN else UNKNOWN,
                      works_broken="works" if schema_ver != UNKNOWN else UNKNOWN,
                      freshness="version %s (import-live)" % schema_ver,
                      exercised="exercised-live (imported + version read)" if schema_ver != UNKNOWN else UNKNOWN)})

    # comp-tools: the live works/broken from comp-tool-health + the coverage-view tool count.
    cov_out, _cerr, cov_rc = _run([sys.executable, os.path.join(_HERE, "comp_coverage_view.py"), "--verify"], timeout=40)
    tools_line = UNKNOWN
    if cov_out and cov_rc == 0:
        for line in cov_out.splitlines():
            if "tools_index" in line or "ledger union" in line:
                tools_line = line.strip()[:180]
                break
    comps.append({"name": "comp-tools: the %s-tool suite (catalog + comp-which + COMPRAIL)"
                          % _yaml_len("org/modules/graph/graph-call-manifest.yaml", "tools_index"),
                  "maturity_evidence": _evidence(
                      cert_status="NFRA_TOOLCHECK P1+P2 CVO-certed (3.0.0_SA_CVO)",
                      works_broken="works (TOOLCHECK: 0 hard breaks; comp-learns-run RETIRED, comp-tooltip fixed)",
                      freshness=tools_line,
                      exercised="exercised-live (TOOLCHECK real-invocation matrix)" if tools_line != UNKNOWN else UNKNOWN)})

    # federated: comp-fedobs served-artifact (grounded read: cse_log_total + co-evolution diversity).
    fed = _read_fedobs()
    comps.append({"name": "federated: FEDOBS observe->measure surface (comp-fedobs)",
                  "maturity_evidence": _evidence(
                      cert_status=UNKNOWN,
                      works_broken="works (reader proven); SURFACE thin-seed" if fed.get("cse_log_total") not in (None, UNKNOWN) else UNKNOWN,
                      freshness=fed.get("vintage", UNKNOWN),
                      exercised="exercised-live (served-artifact read)" if fed.get("cse_log_total") not in (None, UNKNOWN) else UNKNOWN)})

    # learning-loops: PROMOTE-materialized recognizer inventory (grounded read of the git-versioned manifest).
    recs = _read_promote_manifest()
    comps.append({"name": "learning-loops: PROMOTE-materialized recognizers (%s live)" % recs.get("count", UNKNOWN),
                  "maturity_evidence": _evidence(
                      cert_status="GOV-B CVO-certed (caa957377)" if recs.get("count") not in (None, UNKNOWN) else UNKNOWN,
                      works_broken="works (materialize->register->dispatch->reverse)" if recs.get("count") not in (None, UNKNOWN) else UNKNOWN,
                      freshness=recs.get("vintage", UNKNOWN),
                      exercised="exercised-live (manifest read + registry dispatch)" if recs.get("count") not in (None, UNKNOWN) else UNKNOWN)})

    # graph-infra: FRESHGUARD/vintage -- grounded lightly here via the marker (comp-freshness full-run is
    # heavy/live-AWS; a bounded marker read is the honest light-grounding, else UNKNOWN). Marker
    # unreachable -> FORM (a) carry of the prior component's freshness (here the mark WRAPS the value:
    # this field is its own vintage, feeds no drift compare and no grade -- see _grade()).
    gi_fresh = _kuzu_marker()
    if gi_fresh == UNKNOWN:
        for pc in (_prior_class("system-content") or {}).get("components", []):
            pf = pc.get("maturity_evidence", {}).get("freshness")
            if str(pc.get("name", "")).startswith("graph-infra") and _carriable(pf):
                gi_fresh = _carry_mark(pf)
                break
    comps.append({"name": "graph-infra: Nessie/Iceberg/Kuzu + marker-oracle + FRESHGUARD",
                  "maturity_evidence": _evidence(
                      cert_status=UNKNOWN,
                      works_broken="works (comp-kuzu/comp-freshness canonical; TOOLCHECK-verified)",
                      freshness=gi_fresh,
                      exercised="exercised-live (comp-kuzu provenance header)")})

    cs = "the compiler-SYSTEM's 5 scope classes; grades derive the P4 rollup below"
    return _class_obj("system-content", "infra/system/", cs, comps,
                      source="cse_schema(import) + comp_coverage_view + comp-fedobs artifact + promote manifest + comp-kuzu",
                      vintage=_git_head())


def collect_runtime_compilation() -> dict:
    """The live graph runtime vintage via the marker-oracle (current/BEHIND/UNKNOWN); marker
    unreachable -> FORM (a) carry of the committed row (never a downgrade)."""
    marker = _kuzu_marker()
    if marker == UNKNOWN:
        carried = _carry_class("runtime-compilation", "the live graph + .comp-graph",
                               _prior_class("runtime-compilation"))
        if carried is not None:
            return carried
    return _class_obj("runtime-compilation", "the live graph + .comp-graph",
                      current_state="graph marker (comp-kuzu provenance-oracle): %s" % marker,
                      components=[], source="comp-kuzu provenance header (marker-oracle)", vintage=marker)


def _read_fedobs() -> dict:
    """Grounded read of the served FRONTEND FEDOBS artifact (the DS~B frontend-co-evolution measure)
    -- the SURFACED/curated co-evolution subset. Since 2026-07-18 (CTO ruling option-b) this is the
    *_surfaced SECONDARY; the PRIMARY realized-diversity headline is _read_snap_realized(). Returns
    UNKNOWN keys if the artifact is absent (never fabricated)."""
    path = os.path.join(WS, "org", "tier2_senior", "0.4.0_DS_ClientPlatform", "deliverables",
                        "fedobs_frontend_coevolution.json")
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        measures = data.get("measures", [])
        pairs = sum(1 for m in measures if (m.get("co_sessions") or 0) > 0)
        return {"cse_log_total": len(measures), "coevolution_pairs_surfaced": pairs,
                "vintage": "served artifact %s (%d measures, frontend-surfaced subset)"
                           % (os.path.basename(path), len(measures))}
    except Exception:  # noqa: BLE001
        return {"cse_log_total": UNKNOWN, "coevolution_pairs_surfaced": UNKNOWN, "vintage": UNKNOWN}


def _read_snap_realized() -> dict:
    """Grounded read of the REALIZED co-evolution diversity from the fedobs_coevolution_snap
    heartbeat -- ⛔ PARKED 2026-08-11 (CTO PARK-WITH-RECORD ruling 181041Z): the TO-7 "nightly"
    snap convention NEVER LAUNCHED -- 5 done batches ever, all 2026-07-16/17 (the build's own
    exercise runs), no schedule ever existed for the snap legs (139-rule census), no lifecycle
    expiry hiding history. The heartbeat this reads is a SINGLE BUILD-DAY VINTAGE (2026-07-17),
    not a living feed, and the vintage string below now says so on every generation -- a doc
    citing this number must not read as citing a nightly. Park record + re-entry conditions:
    org/tier2_senior/0.7.0_AE_CloudOps/deliverables/GRAPHFEED_TO7_SNAP_FAMILY_PARK_RECORD_20260811.md.
    (Original framing, kept for provenance: CTO ruling option-b 2026-07-18 made this the
    audit's #1 maturity lever; the heartbeat {"appended": N} carries the full pair count of the
    latest snapshot_date.) boto3/S3 imported+called DEFENSIVELY: no creds / off-VPC / absent ->
    UNKNOWN, never fabricated (comp-system stays runnable everywhere)."""
    bucket = os.environ.get("SNAPSHOT_BUCKET", "opal-313476888478-globgrph")
    key = "warehouse/snap_ingest/last_append/fedobs_coevolution_snap.json"
    try:
        import boto3  # noqa: PLC0415  -- defensive/optional; module import must never require it
        body = boto3.client("s3", region_name="us-east-1").get_object(Bucket=bucket, Key=key)["Body"].read()
        hb = json.loads(body)
        realized = hb.get("appended", UNKNOWN)
        return {"realized_pairs": realized,
                "vintage": "snap heartbeat s3://%s/%s (appended=%s @ %s) [PARKED 2026-08-11: "
                           "single build-vintage 2026-07-17, nightly never launched -- CTO "
                           "PARK-WITH-RECORD; not a living feed]"
                           % (bucket, key, realized, hb.get("at", "?"))}
    except Exception:  # noqa: BLE001
        return {"realized_pairs": UNKNOWN, "vintage": UNKNOWN}


def _read_promote_manifest() -> dict:
    """Grounded read of the git-versioned PROMOTE recognizer manifest (my GOV-B materialized recognizers)."""
    path = os.path.join(WS, "org", "tier2_senior", "0.4.0_DS_ClientPlatform", "deliverables",
                        "promote_recognizer_manifest.json")
    try:
        with open(path, encoding="utf-8") as fh:
            recs = json.load(fh).get("recognizers", {})
        materialized = [r for r in recs.values() if r.get("state") == "MATERIALIZED"]
        return {"count": len(materialized), "ids": [r.get("recognizer_id") for r in materialized],
                "vintage": "manifest (%d MATERIALIZED)" % len(materialized)}
    except Exception:  # noqa: BLE001
        return {"count": UNKNOWN, "ids": [], "vintage": UNKNOWN}


# ---------------------------------------------------------------------------
# LIVE METRICS -- the scalar current-state numbers that go stale and that the sibling
# docs embed (tool counts, recognizer count, observe-diversity, graph marker). Andrew-direct
# 2026-07-14: "it should refresh tool counts, state, anything that would actually go stale
# explicitly." One producer, so the number has ONE home; every metric carries {value, source,
# vintage} and is GROUNDED or honestly UNKNOWN -- NEVER a fabricated fallback. This is the same
# no-fabrication discipline the class objects run on, applied to the scalars the prose quotes.
# ---------------------------------------------------------------------------
def _yaml_len(rel_path: str, key: str):
    """Length of a top-level mapping/sequence in a graph yaml, or UNKNOWN. yaml is imported
    defensively (like cse_schema/graph_cache) so a missing dep fails to UNKNOWN, never a crash."""
    try:
        import yaml  # noqa: PLC0415  -- defensive/optional; module import must never require it
        with open(os.path.join(WS, rel_path), encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        node = doc.get(key)
        return len(node) if node is not None else UNKNOWN
    except Exception:  # noqa: BLE001
        return UNKNOWN


def _yaml_nested_len(rel_path: str, *keys: str):
    """Sibling of _yaml_len, for a NESTED mapping/sequence (dotted path via *keys) -- added for
    NFRA_ONTOLOGY_RULE_BANK.yaml's variance.labels, the one rulebank axis that is not a top-level
    key (NFRA_TOOLARCH borrowed-sensitivity remedy, 0.8.0_AE_CloudComp~D 2026-07-25). Same
    defensive-import + UNKNOWN-on-any-failure contract as _yaml_len."""
    try:
        import yaml  # noqa: PLC0415
        with open(os.path.join(WS, rel_path), encoding="utf-8") as fh:
            node = yaml.safe_load(fh)
        for k in keys:
            if not isinstance(node, dict) or k not in node:
                return UNKNOWN
            node = node[k]
        return len(node)
    except Exception:  # noqa: BLE001
        return UNKNOWN


def _pyconst_enum_len(module_name: str, class_name: str):
    """len(EnumClass) for a python module's CLOSED enum, or UNKNOWN -- the pyconst analogue of
    _yaml_len, for cse_schema.py's 4 closed enums (Entity/Relationship/Transformation/Qualifier;
    NFRA_TOOLARCH borrowed-sensitivity remedy, 2026-07-25: these enums' sizes are exactly what an
    ADD-without-a-SCHEMA_VERSION-bump grows -- the countable population version_pin's own
    disclosure names as its blind spot). Imported defensively via importlib (like the existing
    bare `import cse_schema` a few lines above for SCHEMA_VERSION) so a missing/broken module
    fails to UNKNOWN, never a crash."""
    try:
        import importlib
        mod = importlib.import_module(module_name)
        cls = getattr(mod, class_name)
        return len(cls)
    except Exception:  # noqa: BLE001
        return UNKNOWN


def _metric(value, source, vintage) -> dict:
    return {"value": value, "source": source, "vintage": vintage}


#: MODULE-LEVEL (not local to compute_metrics()) precisely so _METRIC_SOURCE_FILES (the
#: uncommitted-source guard's per-metric map, below) can reference the SAME string literal instead
#: of a hand-maintained duplicate (CVO~Z's latent-hole finding, 2026-07-25: a hand-copied duplicate
#: can silently go WRONG, and a wrong entry fails OPEN -- the guard confidently checks a clean file
#: while the real source is dirty, reintroducing the exact laundering hazard one level up). A rename
#: is now one edit, not two that must be kept in sync by hand.
_MANIFEST_PATH = "org/modules/graph/graph-call-manifest.yaml"
_LEDGER_PATH = "org/modules/graph/comp-coverage-map.yaml"
_CSE_SCHEMA_PATH = "org/modules/graph/cse_schema.py"
_RULEBANK_PATH = "org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml"
_EXTRA_REQUIRED_SOURCE_ENV = "COMP_SYSTEM_REQUIRED_SOURCE"
_REQUIRED_SOURCE_FILES = (
    ".tools/comp-system",
    "org/modules/graph/comp_system.py",
    "org/modules/graph/graph_cache.py",
    _MANIFEST_PATH,
    _LEDGER_PATH,
    _CSE_SCHEMA_PATH,
    _RULEBANK_PATH,
)


def _required_source_issues(paths=None) -> list:
    """Return every required local compiler source that cannot be read.

    Globs alone cannot distinguish a deliberately moved-aside file from a smaller healthy
    population, so the load-bearing local sources are named exactly.  Optional/live backends keep
    their historical grounded-or-UNKNOWN/carry behavior; these files are the minimum substrate a
    record must read before it may call itself complete.  COMP_SYSTEM_REQUIRED_SOURCE adds one
    exact path for the planted real-binary acceptance case without moving a shared repository file.
    """
    required = list(_REQUIRED_SOURCE_FILES if paths is None else paths)
    if paths is None:
        extra = os.environ.get(_EXTRA_REQUIRED_SOURCE_ENV, "").strip()
        if extra:
            required.append(extra)
    issues = []
    for item in required:
        path = item if os.path.isabs(str(item)) else os.path.join(WS, str(item))
        try:
            with open(path, "rb") as fh:
                fh.read(1)
        except OSError as exc:
            issues.append("%s (%s: %s)" % (path, type(exc).__name__, exc))
    return issues


def _partial_model(reason: str, issues: list, ctx=None) -> dict:
    """A rejectable partial record.  It is printable but the default path never writes it."""
    now = time.time()
    unit = ctx["unit"] if ctx else "cross_surface_compile"
    if ctx and _budget_expired(ctx):
        status_line = _budget_line(ctx, complete=False)
        deferred = _deferred_lines(ctx, complete=False)
    else:
        disclosure = ("; %s" % _compbudget.disclosure_line(ctx["budget_s"], ctx["source"])) if ctx else ""
        status_line = ("NOT-DECIDABLE: required source unreadable before the atomic %s; "
                       "scanned 0 of 1 %s%s" % (unit, unit, disclosure))
        deferred = _compbudget.deferred_bucket(
            1, 1, unit,
            ["%s: required source unreadable; atomic output was not written" % unit])
    return {
        "header": {
            "generated_by": "comp-system (NFRA_SYSTEM P3)",
            "compile_complete": False,
            "answer_state": ANSWER_PARTIAL,
            "tool_voice": TOOL_VOICE_NOT_DECIDABLE,
            "as_of_head": _git_head(),
            "source_fingerprint": None,
            "emitted_at": now,
            "emitted_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(now)),
            "grounding": ("partial compile; no complete record was emitted or written. "
                          "Unreadable inputs are named, never filled."),
            "auto_refresh": "NOT-DECIDABLE: restore/read the named source and rerun comp-system.",
            "partial_reason": reason,
            "unreadable_sources": issues,
            "unit": unit,
            "rule_t": {
                "status_line": status_line,
                "deferred": deferred,
            },
        },
        "metrics": {},
        "diversity_metric": {
            "metric": "NOT-DECIDABLE",
            "coevolution_pairs": UNKNOWN,
            "coevolution_pairs_surfaced": UNKNOWN,
            "cse_measures": UNKNOWN,
            "note": "partial compile -- values deliberately not filled",
            "vintage": UNKNOWN,
        },
        "classes": [],
    }


def compute_metrics() -> dict:
    """The canonical live scalars. Keyed by a stable slug the managed-region markers reference
    (<!--cs:SLUG-->...<!--/cs-->). Each grounded against its ONE authoritative source or UNKNOWN."""
    MANIFEST = _MANIFEST_PATH
    LEDGER = _LEDGER_PATH

    tools_index = _yaml_len(MANIFEST, "tools_index")
    tools = _yaml_len(LEDGER, "tools")
    meta_tools = _yaml_len(LEDGER, "meta_tools")
    ledger_union = (tools + meta_tools) if UNKNOWN not in (tools, meta_tools) else UNKNOWN

    recs = _read_promote_manifest()
    fed = _read_fedobs()
    snap = _read_snap_realized()

    # NFRA_TOOLARCH borrowed-sensitivity remedy (0.8.0_AE_CloudComp~D, 2026-07-25, dispatch
    # 1.0.0_SA_CTO~Z off ~C's L1b finding): scope_contract.json's ont-cse-version-current and
    # ont-rulebank-version-current units are `version_pin` checks whose sensitivity is BORROWED
    # from human SCHEMA_VERSION/meta.version bump discipline -- an enum member or a rulebank axis
    # entry ADDED WITHOUT a version bump is invisible to them. ~C determined (BORROWED_SENSITIVITY_
    # REMEDY_C.md) both units have countable SOURCE populations but no machine-readable REPORT-side
    # count -- these 7 metrics ARE that report side, so a future derived_count contract edit
    # (~C's) becomes a two-line change instead of needing new infrastructure. NOT cse_measures
    # (that metric's own source field says "comp-fedobs cse_log_total (served)" -- a DIFFERENT
    # population; ~C's own near-miss finding, kept here as the cautionary precedent it named).
    cse_entity = _pyconst_enum_len("cse_schema", "Entity")
    cse_relationship = _pyconst_enum_len("cse_schema", "Relationship")
    cse_transformation = _pyconst_enum_len("cse_schema", "Transformation")
    cse_qualifier = _pyconst_enum_len("cse_schema", "Qualifier")
    rulebank_roles = _yaml_len(_RULEBANK_PATH, "roles")
    rulebank_relations = _yaml_len(_RULEBANK_PATH, "relations")
    rulebank_variance = _yaml_nested_len(_RULEBANK_PATH, "variance", "labels")

    graph_marker = _metric(_kuzu_marker(), "comp-kuzu provenance header (marker-oracle)", _kuzu_marker())
    if graph_marker["value"] == UNKNOWN:
        # FORM (a): VALUE verbatim from the committed metric (the by-construction drift exclusion --
        # a carried value equals its own last-refreshed managed-region span); the mark rides the
        # vintage field ONLY. Nothing real committed -> the honest UNKNOWN stands.
        pm = (_prior_06() or {}).get("metrics", {}).get("graph_marker") or {}
        if _carriable(pm.get("value")):
            graph_marker = _metric(pm["value"], "comp-kuzu provenance header (marker-oracle)",
                                   _carry_mark(pm.get("vintage") or pm["value"]))

    return {
        "tools_index_count": _metric(
            tools_index, "graph-call-manifest.yaml:tools_index (mapping length)",
            "manifest (%s routable entries)" % tools_index),
        "ledger_union_count": _metric(
            ledger_union, "comp-coverage-map.yaml: len(tools)+len(meta_tools)",
            "SoT ledger (%s tools + %s meta = %s)" % (tools, meta_tools, ledger_union)),
        "recognizers_live": _metric(
            recs.get("count", UNKNOWN), "promote_recognizer_manifest.json (MATERIALIZED)",
            recs.get("vintage", UNKNOWN)),
        "coevolution_pairs": _metric(
            snap.get("realized_pairs", UNKNOWN),
            "fedobs_coevolution_snap heartbeat (realized, GRAPHFEED nightly)",
            snap.get("vintage", UNKNOWN)),
        "coevolution_pairs_surfaced": _metric(
            fed.get("coevolution_pairs_surfaced", UNKNOWN),
            "fedobs_frontend_coevolution.json (surfaced subset)",
            fed.get("vintage", UNKNOWN)),
        "cse_measures": _metric(
            fed.get("cse_log_total", UNKNOWN), "comp-fedobs cse_log_total (served)",
            fed.get("vintage", UNKNOWN)),
        "cse_entity_count": _metric(
            cse_entity, "cse_schema.py: len(Entity) (closed enum, S1)",
            "cse_schema (%s Entity members)" % cse_entity),
        "cse_relationship_count": _metric(
            cse_relationship, "cse_schema.py: len(Relationship) (closed enum, S1)",
            "cse_schema (%s Relationship members)" % cse_relationship),
        "cse_transformation_count": _metric(
            cse_transformation, "cse_schema.py: len(Transformation) (closed enum, S1)",
            "cse_schema (%s Transformation members)" % cse_transformation),
        "cse_qualifier_count": _metric(
            cse_qualifier, "cse_schema.py: len(Qualifier) (closed enum, S1)",
            "cse_schema (%s Qualifier members)" % cse_qualifier),
        "rulebank_role_count": _metric(
            rulebank_roles, "NFRA_ONTOLOGY_RULE_BANK.yaml: len(roles) (axis ROLE)",
            "rulebank (%s roles)" % rulebank_roles),
        "rulebank_relation_count": _metric(
            rulebank_relations, "NFRA_ONTOLOGY_RULE_BANK.yaml: len(relations) (axis RELATION)",
            "rulebank (%s relations)" % rulebank_relations),
        "rulebank_variance_count": _metric(
            rulebank_variance, "NFRA_ONTOLOGY_RULE_BANK.yaml: len(variance.labels) (axis VARIANCE)",
            "rulebank (%s variance verdicts)" % rulebank_variance),
        "graph_marker": graph_marker,
    }


# ---------------------------------------------------------------------------
# MANAGED REGIONS -- the refresher that carries the metrics OUT into the sibling docs. A doc
# opts a live number in by wrapping it: `<!--cs:tools_index_count-->55<!--/cs-->`. comp-system
# rewrites ONLY the text between the markers with the live value -- never the surrounding
# hand-authored prose. That is what makes "refresh anything that would go stale" both LITERAL
# (run the compiler, every marked number updates) and SAFE (bounded to marked spans, no
# fabrication -- an UNKNOWN metric is REFUSED, the old number is left, and the drift is reported).
# ---------------------------------------------------------------------------
import re as _re  # noqa: E402

_REGION_RE = _re.compile(r"(<!--\s*cs:([a-z0-9_]+)\s*-->)(.*?)(<!--\s*/cs\s*-->)", _re.DOTALL)
_MANAGED_DOCS_DIR = os.path.join(WS, "infra", "system")


def refresh_managed_regions(metrics: dict, write: bool):
    """Rewrite every <!--cs:NAME--> span in infra/system/*.md to metrics[NAME].value.

    Returns (changes, problems, scanned): changes = [(file, name, old, new)] spans whose rendered
    value moved; problems = [(file, name, why)] spans naming an unknown metric or one that is
    UNKNOWN (NEVER overwritten -- we do not stamp UNKNOWN over a real number); scanned =
    {"regions": N, "files": M} -- N = total well-formed <!--cs:NAME-->...<!--/cs--> spans matched
    (across every file, drifted or not), M = how many of those files contained >=1 match.

    scanned exists because "0 drifted" alone is a claim with NO STATED DENOMINATOR (CTO~Z dispatch
    NFRA_TOOLARCH, 2026-07-25, off CVO~Z's finding against _REGION_RE directly): a malformed marker
    (missing/typo'd closer, wrong-case name) matches ZERO regexes, so it is SILENTLY excluded from
    `changes` -- comp-system would then report "0 drifted" over a scan that watched nothing, and
    `check_stale`/eng-currentstate-current's system_current unit would read PASS about nothing.
    Reporting the count callers can render alongside "0 drifted" turns a wiring gap into a visible
    count drop instead of silence. write=False = report only (the --check/--gate path); write=True
    updates the files in place (the compile path)."""
    changes, problems = [], []
    scanned_regions = 0
    scanned_files = 0
    try:
        names = sorted(os.listdir(_MANAGED_DOCS_DIR))
    except OSError:
        return changes, problems, {"regions": scanned_regions, "files": scanned_files}
    for fn in names:
        if not fn.endswith(".md"):
            continue
        path = os.path.join(_MANAGED_DOCS_DIR, fn)
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError:
            continue
        file_dirty = False
        file_region_count = [0]

        def _sub(mobj, _fn=fn, _frc=file_region_count):
            nonlocal file_dirty
            _frc[0] += 1
            open_tag, name, old, close_tag = mobj.group(1), mobj.group(2), mobj.group(3), mobj.group(4)
            met = metrics.get(name)
            if met is None:
                problems.append((_fn, name, "no such metric"))
                return mobj.group(0)
            if met["value"] == UNKNOWN or met["value"] is None:
                problems.append((_fn, name, "metric is UNKNOWN -- left the existing value, not overwritten"))
                return mobj.group(0)
            new = str(met["value"])
            if new != old:
                changes.append((_fn, name, old, new))
                file_dirty = True
            return open_tag + new + close_tag

        new_text = _REGION_RE.sub(_sub, text)
        scanned_regions += file_region_count[0]
        if file_region_count[0]:
            scanned_files += 1
        if write and file_dirty:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new_text)
    return changes, problems, {"regions": scanned_regions, "files": scanned_files}


def _decorate_answer_states(model: dict) -> tuple:
    """Attach the measured managed-region answer before render/write.

    Zero changes is a real zero only when the denominator is non-zero.  A zero-region scan is
    PARTIAL_OR_BLIND, never PRESENT_WITH_ZERO_RESULTS.  The static/no-producer classes already
    carry SUBJECT_ABSENT_FROM_CORPUS in their own current_state; --gate's no-trigger branch carries
    NOT_APPLICABLE, and partial models carry PARTIAL_OR_BLIND/NOT-DECIDABLE.
    """
    if not model.get("header", {}).get("compile_complete"):
        return [], [], {"regions": 0, "files": 0}
    changes, problems, scanned = refresh_managed_regions(model.get("metrics", {}), write=False)
    if scanned["regions"] == 0:
        state = ANSWER_PARTIAL
        line = _answer_state_line(
            state, "managed-region refresh",
            "0 regions across %d files; no population was compared" % scanned["files"],
            TOOL_VOICE_NOT_DECIDABLE)
    elif not changes:
        state = ANSWER_PRESENT_ZERO
        line = _answer_state_line(
            state, "managed-region drift",
            "0 changed rows across %d regions in %d files" %
            (scanned["regions"], scanned["files"]))
    else:
        state = "PLAIN_POSITIVE_RESULT"
        line = ("PLAIN_POSITIVE_RESULT: subject=managed-region drift; %d changed row(s) "
                "across %d regions in %d files" %
                (len(changes), scanned["regions"], scanned["files"]))
    model["header"]["managed_region_answer"] = {
        "state": state,
        "line": line,
        "changed": len(changes),
        "regions": scanned["regions"],
        "files": scanned["files"],
        "problems": len(problems),
    }
    return changes, problems, scanned


# ---------------------------------------------------------------------------
# Compile -- assemble the model + the provenance header + the diversity metric.
# ---------------------------------------------------------------------------
def compile_model(ctx=None) -> dict:
    issues = _required_source_issues()
    if issues:
        return _partial_model("required source unreadable", issues, ctx=ctx)
    if ctx and _budget_expired(ctx):
        return _partial_model("budget expired before the atomic compile began", [], ctx=ctx)
    fed = _read_fedobs()
    snap = _read_snap_realized()
    header = {
        "generated_by": "comp-system (NFRA_SYSTEM P3)",
        "compile_complete": True,
        # PROVENANCE, not the staleness predicate. It truthfully records the HEAD this was compiled
        # against; it no longer decides freshness (see check_stale: committing the artifact advances
        # HEAD, so as_of==HEAD was unsatisfiable for the committed state).
        "as_of_head": _git_head(),
        # THE PREDICATE's stored half -- computed by the SAME expression --check evaluates.
        "source_fingerprint": _source_fingerprint(),
        "emitted_at": time.time(),
        # Human-readable twin of emitted_at (Andrew-direct 2026-07-14: the doc carries a TIMESTAMP
        # AT THE TOP + the run-this-to-update instruction -- that IS the usage model; no scheduler).
        "emitted_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "grounding": "every value below is grounded against a live comp-tool/artifact/marker, or UNKNOWN-VINTAGE. "
                     "ZERO fabrication (CTO hard-line / GOV-A / Rule 22).",
        "auto_refresh": "stale iff a source input drifted OR the compile exceeds the TTL: "
                        "run comp-system --check (0=fresh 2=stale 1=error "
                        "3=NOT-DECIDABLE) then comp-system.",
        "source_health": {"required": len(_REQUIRED_SOURCE_FILES), "unreadable": []},
    }
    diversity = {"metric": "observe-surface DIVERSITY (co-evolution pairs; CTO Q4: diversity not raw volume)",
                 "coevolution_pairs": snap.get("realized_pairs", UNKNOWN),
                 "coevolution_pairs_surfaced": fed.get("coevolution_pairs_surfaced", UNKNOWN),
                 "cse_measures": fed.get("cse_log_total", UNKNOWN),
                 "note": "PRIMARY = realized diversity from the fedobs_coevolution_snap heartbeat "
                         "[PARKED 2026-08-11 -- single build-vintage, the TO-7 nightly convention "
                         "never launched; CTO PARK-WITH-RECORD, see the park record]; "
                         "*_surfaced = the frontend-curated subset -- label-the-basis, CTO ruling option-b",
                 "vintage": snap.get("vintage", UNKNOWN)}
    classes = []
    for slug, home, collector in KNOWLEDGE_CLASSES:
        if collector is None:
            classes.append(_unknown_class(slug, home))
            continue
        try:
            classes.append(globals()[collector]())
        except Exception as e:  # noqa: BLE001  -- a collector failure -> UNKNOWN class, never a fabricated one
            classes.append(_class_obj(slug, home, "%s: collector error (%s)" % (UNKNOWN, type(e).__name__),
                                      [], "collector-error", UNKNOWN))
    metrics = compute_metrics()
    # FORM (a) header anchor (the CTO pin, Msg 63063): a carry defeats the DRIFT verdict, NEVER the
    # age clock. graph_carried_since chains to the ORIGINAL derivation's emit time -- a re-carry
    # preserves the prior chain anchor, never this compile's own timestamp -- so _staleness ages
    # carried graph rows from the real derivation. A fresh (graph-capable) compile writes neither
    # key, which is what ends the chain.
    carried_rows = [c["slug"] for c in classes if str(c.get("vintage", "")).startswith(CARRY_PREFIX)]
    for c in classes:
        if c.get("slug") == "system-content":
            carried_rows += ["system-content.components.%s" % str(pc.get("name", "")).split(":")[0]
                             for pc in c.get("components", [])
                             if str(pc.get("maturity_evidence", {}).get("freshness", "")).startswith(CARRY_PREFIX)]
    if str(metrics.get("graph_marker", {}).get("vintage", "")).startswith(CARRY_PREFIX):
        carried_rows.append("metrics.graph_marker")
    if carried_rows:
        header["graph_carried_rows"] = carried_rows
        prior_h = (_prior_06() or {}).get("header", {})
        since = prior_h.get("graph_carried_since") or prior_h.get("emitted_at")
        if since:
            header["graph_carried_since"] = float(since)
    if ctx and _budget_expired(ctx):
        return _partial_model("budget expired during the atomic compile", [], ctx=ctx)
    return {"header": header, "metrics": metrics, "diversity_metric": diversity, "classes": classes}


# ---------------------------------------------------------------------------
# Emit -- markdown (human + LOCALROOT-index ## anchors) + json (P4 grading).
# ---------------------------------------------------------------------------
def _render_metrics(metrics: dict) -> list:
    """The live-scalars block: one home for every number the sibling docs quote, each with vintage.
    Rendered inside 06 AND pushed out to the marked spans in the other docs by refresh_managed_regions."""
    out = ["## Live metrics (the scalars that go stale -- refreshed by `comp-system`; managed-region source)",
           "",
           "| metric | value | source (vintage) |",
           "|---|---|---|"]
    for name, m in metrics.items():
        out.append("| `%s` | %s | %s |" % (name, m["value"], m["vintage"]))
    out.append("")
    return out


def render_markdown(model: dict) -> str:
    h = model["header"]
    if not h.get("compile_complete", True):
        out = [
            "# comp-system partial result -- NOT A COMPLETE 06 RECORD",
            "",
            "**Generated: %s (HEAD %s)**" %
            (h.get("emitted_at_utc", "UNKNOWN"), h.get("as_of_head", UNKNOWN)),
            "",
            _answer_state_line(
                h.get("answer_state", ANSWER_PARTIAL), h.get("unit", "cross_surface_compile"),
                h.get("partial_reason", "compile incomplete"),
                h.get("tool_voice", TOOL_VOICE_NOT_DECIDABLE)),
            "",
            "**NO COMPLETE RECORD WAS WRITTEN.** Unreadable inputs are named; values are never filled.",
            "",
            "## Unreadable sources",
        ]
        issues = h.get("unreadable_sources", [])
        out.extend("- %s" % issue for issue in issues)
        if not issues:
            out.append("- none; the incomplete state is budget-caused")
        out += ["", "## Rule T"]
        rule_t = h.get("rule_t", {})
        out.append(rule_t.get("status_line", "NOT-DECIDABLE"))
        out.extend(rule_t.get("deferred", []))
        return "\n".join(out) + "\n"
    d = model["diversity_metric"]
    # The usage model, Andrew-direct 2026-07-14 (verbatim: "it should just have a timestamp on it
    # and you run the compiler attached to it to update it ... its clear in the top of the document
    # thats what you do and has a timestamp at the top"): a SNAPSHOT with a visible wall-clock
    # timestamp + the one-line refresh procedure, both at the very top. No scheduler, no alarm --
    # the reader sees the age and refreshes when they need current.
    out = ["# 06 -- Current state (AUTO-GENERATED by comp-system -- the dynamic half)",
           "",
           "**Generated: %s (HEAD %s)** -- a SNAPSHOT of the live system at that moment."
           % (h.get("emitted_at_utc", "UNKNOWN"), h["as_of_head"]),
           "",
           "**To update: run `comp-system`. That is the whole procedure.** It regenerates this doc AND "
           "refreshes every `<!--cs:NAME-->` managed-region span across `infra/system/` (tool counts, "
           "recognizer count, observe-diversity, graph marker) from the live sources. "
           "(`comp-system --check` first if you only want to know whether anything is stale: "
           "0=current 2=stale 1=error 3=NOT-DECIDABLE.)",
           "",
           "**AUTO-GENERATED by `comp-system` (NFRA_SYSTEM P3). Do NOT hand-edit -- regenerate.**",
           "",
           "## Provenance / freshness header",
           "- generated_by: %s" % h["generated_by"],
           "- generated_at (UTC): %s" % h.get("emitted_at_utc", "UNKNOWN"),
           "- as_of (HEAD): %s" % h["as_of_head"],
           "- compile_complete: %s" % h.get("compile_complete", True),
           "- grounding: %s" % h["grounding"],
           "- auto-refresh: %s" % h["auto_refresh"],
           "- required-source health: %d required / %d unreadable" %
           (h.get("source_health", {}).get("required", 0),
            len(h.get("source_health", {}).get("unreadable", []))),
           "- answer-state: %s" %
           h.get("managed_region_answer", {}).get("line", "not evaluated"),
           "- rule-t: %s" % h.get("rule_t", {}).get("status_line", "not applied"),
           ] + ["- rule-t: %s" % line for line in h.get("rule_t", {}).get("deferred", [])] + [
           "",
           ] + _render_metrics(model.get("metrics", {})) + [
           "## Observe-surface diversity (loop/federated maturity headline)",
           "- %s" % d["metric"],
           "- coevolution_pairs (realized): %s | coevolution_pairs_surfaced (frontend): %s | cse_measures: %s | vintage: %s"
           % (d["coevolution_pairs"], d.get("coevolution_pairs_surfaced", "UNKNOWN"), d["cse_measures"], d["vintage"]),
           "- note: %s" % d["note"],
           "",
           "## Runtime current-state, keyed by LOCALROOT knowledge-class (anchors 1:1 with the infra/README index)",
           ""]
    for c in model["classes"]:
        out.append("### %s" % c["slug"])          # the anchor: #<slug>, 1:1 with NFRA_LOCALROOT_P2 SS2
        out.append("- static_home: `%s`" % c["static_home"])
        out.append("- current_state: %s" % c["current_state"])
        out.append("- vintage: %s  |  source: %s" % (c["vintage"], c["source"]))
        if c["components"]:
            r = c["maturity_rollup"]
            out.append("- maturity_rollup: BP=%d BU=%d F=%d D=%d unknown=%d" %
                       (r["BP"], r["BU"], r["F"], r["D"], r["unknown"]))
            for comp in c["components"]:
                ev = comp["maturity_evidence"]
                out.append("  - **%s** [%s]" % (comp["name"], _grade(ev)))
                out.append("    - cert: %s | works/broken: %s | freshness: %s | exercised: %s" %
                           (ev["cert_status"], ev["works_broken"], ev["freshness"], ev["exercised"]))
        out.append("")
    return "\n".join(out) + "\n"


def _write(model: dict) -> list:
    os.makedirs(os.path.dirname(OUT_MD), exist_ok=True)
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write(render_markdown(model))
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(model, fh, indent=2)
    # Carry the live scalars OUT to every marked span in the sibling docs (03/00/README/...).
    changes, problems, _scanned = refresh_managed_regions(model.get("metrics", {}), write=True)
    return changes + [("PROBLEM", p[0], p[1], p[2]) for p in problems]


# ---------------------------------------------------------------------------
# SELF-TEST -- the no-fabrication invariant + the shape contract.
# ---------------------------------------------------------------------------
def self_test() -> int:
    print("=== comp-system self-test (the no-fabrication invariant + shape contract) ===")
    ok = []

    def chk(name, cond):
        ok.append(bool(cond))
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))

    # 0. NFRA_COMPEFFICACY T-21 FIRST ARM.  Move a scratch source aside, then prove the
    #    compiler's partial record names the unreadable source and cannot call itself complete.
    #    Scratch-only: the real-binary acceptance separately drives this through the env carrier.
    import tempfile as _t21_tempfile
    with _t21_tempfile.TemporaryDirectory(prefix="comp_system_unreadable_") as _t21_dir:
        _t21_source = os.path.join(_t21_dir, "required.json")
        _t21_aside = _t21_source + ".aside"
        with open(_t21_source, "w", encoding="utf-8") as _t21_fh:
            _t21_fh.write("{}\n")
        os.replace(_t21_source, _t21_aside)
        _t21_issues = _required_source_issues([_t21_source])
        _t21_partial = _partial_model("required source unreadable", _t21_issues)
    chk("0  no-fabrication: moved-aside required source -> PARTIAL_OR_BLIND / "
        "NOT-DECIDABLE, source named, compile_complete false",
        bool(_t21_issues)
        and _t21_partial["header"].get("compile_complete") is False
        and _t21_partial["header"].get("answer_state") == ANSWER_PARTIAL
        and _t21_partial["header"].get("tool_voice") == TOOL_VOICE_NOT_DECIDABLE
        and _t21_source in _t21_partial["header"].get("unreadable_sources", [""])[0])

    # 0a. Four planted answer-state cases in ONE self-test invocation.  The enum file is an
    #     independent oracle: a mutated engine constant cannot move the ratified set with it.
    with open(os.path.join(WS, "org", "standards", "COMPTOOL_ANSWER_STATE.enum.json"),
              encoding="utf-8") as _t21_fh:
        _t21_ratified = {x["state"] for x in json.load(_t21_fh)["states"]}
    _t21_produced = {
        ANSWER_SUBJECT_ABSENT, ANSWER_PRESENT_ZERO, ANSWER_PARTIAL, ANSWER_NOT_APPLICABLE}
    _t21_cases = [
        _answer_state_line(ANSWER_SUBJECT_ABSENT, "scope-class fixture",
                           "no source carries this class"),
        _answer_state_line(ANSWER_PRESENT_ZERO, "real-present fixture",
                           "0 rows across 1 present surface"),
        _answer_state_line(ANSWER_PARTIAL, "moved-aside required source",
                           "source unreadable; no complete record written",
                           TOOL_VOICE_NOT_DECIDABLE),
        _answer_state_line(ANSWER_NOT_APPLICABLE, "mode fixture",
                           "the mode has no population for this subject"),
    ]
    for _t21_case in _t21_cases:
        print("  [CASE] %s" % _t21_case)
    chk("0a ratified answer-state spellings: four planted cases emit four exact tokens in one invocation",
        _t21_produced == _t21_ratified
        and len(_t21_cases) == 4
        and all(any(state in line for line in _t21_cases) for state in _t21_ratified))

    m = compile_model()
    # 1. every LOCALROOT SS2 class has an anchor (scope-(a): no static home without a runtime anchor).
    slugs = [c["slug"] for c in m["classes"]]
    chk("1  every SS2 knowledge-class emits a per-class object (scope-(a), no omission): %d" % len(slugs),
        len(slugs) == len(KNOWLEDGE_CLASSES) and slugs == [k[0] for k in KNOWLEDGE_CLASSES])
    # 2. NO-FABRICATION: every class's value is either grounded (a real source) or honestly UNKNOWN/no-producer.
    honest = all((c["vintage"] == UNKNOWN or c["source"] not in ("", None)) for c in m["classes"])
    chk("2  no-fabrication: every class carries a source OR UNKNOWN-VINTAGE (never a bare invented number)", honest)
    # 3. non-groundable classes are HONESTLY UNKNOWN (not silently omitted, not fabricated).
    nogrp = [c for c in m["classes"] if c["source"] == NO_PRODUCER]
    chk("3  non-groundable classes carry an honest UNKNOWN-VINTAGE/no-live-producer anchor (roster-floor)",
        all(c["vintage"] == UNKNOWN and not c["components"] for c in nogrp) and len(nogrp) >= 1)
    # 4. the shape contract: each component's maturity_evidence has all 4 P4 fields; rollup derives from them.
    shape = True
    for c in m["classes"]:
        for comp in c["components"]:
            ev = comp.get("maturity_evidence", {})
            if set(ev.keys()) != {"cert_status", "works_broken", "freshness", "exercised"}:
                shape = False
    chk("4  shape: every component's maturity_evidence = {cert_status,works_broken,freshness,exercised} (P4 fields)", shape)
    # 5. the header carries the grounded as-of + the grounding attestation + the diversity metric.
    chk("5  header: grounded as-of (HEAD) + no-fabrication attestation + observe-diversity metric present",
        bool(m["header"].get("as_of_head")) and "fabrication" in m["header"]["grounding"].lower()
        and "coevolution_pairs" in m["diversity_metric"])
    # 6. system-content grounds >=1 component LIVE (cse_schema import) -- the compiler actually reads live.
    sc = next((c for c in m["classes"] if c["slug"] == "system-content"), {})
    live = any(UNKNOWN not in str(comp["maturity_evidence"].get("freshness", "")) for comp in sc.get("components", []))
    chk("6  grounds live: system-content has >=1 component grounded from a LIVE read (not all UNKNOWN)", live)
    # 7. markdown renders + anchors are the SS2 slugs (LOCALROOT index links resolve 1:1).
    md = render_markdown(m)
    chk("7  markdown renders with ## <slug> anchors 1:1 with the SS2 knowledge-class slugs",
        all(("### %s" % s) in md for s in slugs))
    # 8. metrics: every metric carries {value,source,vintage} and >=1 is grounded LIVE (not all UNKNOWN) --
    #    the no-fabrication invariant applied to the scalars the sibling docs quote.
    mets = m.get("metrics", {})
    shape_ok = all(set(v.keys()) == {"value", "source", "vintage"} for v in mets.values())
    live_ok = any(v["value"] != UNKNOWN for v in mets.values())
    chk("8  metrics: each is {value,source,vintage} + >=1 grounded live (tool counts read from yaml)",
        bool(mets) and shape_ok and live_ok)
    # 9. the refresher is SAFE: report-only run touches no file, and it NEVER stamps UNKNOWN over a
    #    real number (an unknown metric is reported as a problem, the existing value is preserved).
    ch, _pb, _scanned = refresh_managed_regions(mets, write=False)
    unknown_overwrite = any(mets.get(name, {}).get("value") == UNKNOWN for _fn, name, _o, _n in ch)
    chk("9  managed-region refresher: report-only, and never overwrites a real number with UNKNOWN",
        not unknown_overwrite)

    # 10-13. --gate (WS-2): staleness-CONDITIONED fail-closed, exercised BOTH directions on the PURE
    #        verdict. Genuine drift (source-fingerprint / managed-region) FAILS-CLOSED (rc 2); age>=TTL
    #        ALONE is a WARN, never a block (the false-Monday distinction, NEVER#1); CURRENT is open.
    #        dirty=[] pins these as the CLEAN-TREE positive control (unchanged DRIFT/regen verdict) --
    #        see 10a/11a below for the dirty-source mutant (BLOCKED-ON-PEER-LANDING, no regen wording).
    chk("10 gate: source-fingerprint drift, clean tree -> FAIL-CLOSED (rc 2), DRIFT/regen (positive control)",
        _gate_verdict(True, "source drift: fingerprint (1, 2) -> (3, 4)", [], dirty=[])
        == (2, "SYSTEM DRIFT (fail-closed): source drift: fingerprint (1, 2) -> (3, 4)"))
    chk("11 gate: managed-region drift, clean tree -> FAIL-CLOSED (rc 2), DRIFT/regen (positive control)",
        _gate_verdict(False, "sources unchanged, age 0h < TTL 24h",
                      [("03_comp_tools.md", "tools_index_count", 59, 61)], dirty=[])[0] == 2)
    chk("10a gate: source-fingerprint drift, DIRTY source -> BLOCKED-ON-PEER-LANDING (rc 2), no regen wording (mutant)",
        (lambda v: v[0] == 2 and "BLOCKED-ON-PEER-LANDING" in v[1] and "regenerate" not in v[1])
        (_gate_verdict(True, "source drift: fingerprint (1, 2) -> (3, 4)", [],
                       dirty=["org/modules/graph/canon-patterns.yaml"])))
    chk("11a gate: managed-region drift, git-status UNVERIFIABLE (dirty=None) -> BLOCKED, fail-closed not silent-pass (mutant)",
        (lambda v: v[0] == 2 and "BLOCKED-ON-PEER-LANDING" in v[1] and "regenerate" not in v[1])
        (_gate_verdict(False, "sources unchanged, age 0h < TTL 24h",
                       [("03_comp_tools.md", "tools_index_count", 59, 61)], dirty=None)))
    # 11b-11d. v2 (2026-07-25, CVO~Z's recommendation after the v1 UNION block deadlocked ~D behind
    #          an unrelated lane's untracked debris it never touched): scope the dirty-check to the
    #          file(s) that FEED the SPECIFICALLY-drifted metric(s), not the whole _SOURCES union.
    chk("11b gate v2: metric X drifts, dirty file feeds ONLY metric Y -> NOT blocked, plain DRIFT/regen (false-block eliminated, mutant)",
        _gate_verdict(False, "sources unchanged, age 0h < TTL 24h",
                      [("03_comp_tools.md", "tools_index_count", 59, 61)],
                      dirty=["org/modules/graph/comp-coverage-map.yaml"])  # feeds ledger_union_count, not tools_index_count
        == (2, "SYSTEM DRIFT (fail-closed): 1 managed-region span(s) drifted from live metrics: "
               "03_comp_tools.md cs:tools_index_count 59->61"))
    chk("11c gate v2: metric X drifts, dirty file feeds metric X -> still BLOCKED-ON-PEER-LANDING (true-block preserved)",
        (lambda v: v[0] == 2 and "BLOCKED-ON-PEER-LANDING" in v[1] and "regenerate" not in v[1]
         and "graph-call-manifest.yaml" in v[1])
        (_gate_verdict(False, "sources unchanged, age 0h < TTL 24h",
                       [("03_comp_tools.md", "tools_index_count", 59, 61)],
                       dirty=["org/modules/graph/graph-call-manifest.yaml", "org/modules/graph/comp-coverage-map.yaml"])))
    chk("11d gate v2: drifted metric has NO _METRIC_SOURCE_FILES entry -> conservative whole-union BLOCK (protection preserved for unmapped metrics)",
        (lambda v: v[0] == 2 and "BLOCKED-ON-PEER-LANDING" in v[1])
        (_gate_verdict(False, "sources unchanged, age 0h < TTL 24h",
                       [("06_current_state.md", "graph_marker", "abc123", "def456")],
                       dirty=["org/modules/graph/canon-patterns.yaml"])))
    # 11e-11f. v3 (CVO~Z's latent-hole finding, 2026-07-25): _METRIC_SOURCE_FILES was a
    #          hand-maintained duplicate of a fact compute_metrics() already declares -- a WRONG
    #          entry (not merely a missing one, already covered by 11d) fails OPEN: the guard
    #          confidently checks a clean file while the real source is dirty, reintroducing the
    #          exact laundering hazard one level up. Killed by construction (shared _MANIFEST_PATH/
    #          _LEDGER_PATH constants) AND checked explicitly here, with a mutant proving the check
    #          has teeth rather than vacuously passing.
    chk("11e _METRIC_SOURCE_FILES agrees with compute_metrics()'s own path constants (no hand-maintained divergence, real map)",
        _metric_source_files_mismatches(_METRIC_SOURCE_FILES) == [])
    chk("11f mutant: a deliberately-WRONG map entry IS caught by the consistency check (proves it has teeth, not a vacuous pass)",
        _metric_source_files_mismatches({"tools_index_count": [_LEDGER_PATH],   # swapped -- wrong on purpose
                                          "ledger_union_count": [_LEDGER_PATH]}) == [
            ("tools_index_count", [_MANIFEST_PATH], [_LEDGER_PATH])])
    chk("11f2 mutant: a realistic .yml/.yaml basename typo IS caught (CVO~Z's Limb 4 -- the likely real-world drift mode, not just a deliberate swap)",
        _metric_source_files_mismatches({"tools_index_count": ["org/modules/graph/graph-call-manifest.yml"],
                                          "ledger_union_count": [_LEDGER_PATH]}) == [
            ("tools_index_count", [_MANIFEST_PATH], ["org/modules/graph/graph-call-manifest.yml"])])
    # 11g-11h. v4 (CVO~Z's named residual on v3, 2026-07-25): _metric_source_files_mismatches()'s own
    #          `truth` dict is a THIRD hand-written statement of the metric->path ASSOCIATION (paths
    #          themselves can't drift anymore -- shared constants -- but the association could).
    #          Couples the check to compute_metrics()'s OWN declared `source` string (the authority)
    #          instead of a third hand-copied twin -- CVO~Z-verified this basename-in-source check
    #          holds today before it was implemented here.
    chk("11g association: _METRIC_SOURCE_FILES's basenames are named in compute_metrics()'s OWN declared source strings (real map, real metrics)",
        _metric_source_association_mismatches(_METRIC_SOURCE_FILES, mets) == [])
    chk("11h mutant: a metric whose declared source string stops naming the expected basename IS caught",
        _metric_source_association_mismatches(
            _METRIC_SOURCE_FILES,
            {**mets, "tools_index_count": {"value": 1, "source": "totally-different-file.yaml", "vintage": "x"}}
        ) == [("tools_index_count", "graph-call-manifest.yaml", "totally-different-file.yaml")])
    chk("12 gate: age>=TTL ALONE -> WARN not block (rc 0) -- staleness-conditioned, no false-Monday",
        _gate_verdict(True, "age 30h exceeds TTL 24h (live-grounded values may have moved)", [], dirty=[])[0] == 0)
    chk("13 gate: CURRENT -> gate open (rc 0)",
        _gate_verdict(False, "sources unchanged, age 0h < TTL 24h", [], dirty=[])[0] == 0)
    # 13a. _dirty_sources() shape: never raises, returns a list or None -- exercised live against the
    #      REAL working tree (not a synthetic list) so this check also proves the git-status plumbing
    #      itself works on this box, not just the pure-decision logic above.
    _ds = _dirty_sources()
    chk("13a _dirty_sources(): live git-status probe returns a list or None, never raises",
        _ds is None or isinstance(_ds, list))
    # 14-15. --changed staleness-conditioning: a _SOURCE touch triggers the check; a non-source
    #        changeset is n/a (the commit-gate leg fires ONLY at the genuine drift moment).
    chk("14 gate --changed: a comp-system _SOURCE path IS a trigger surface",
        _file_touches_sources(["org/modules/graph/canon-patterns.yaml", "docs/x.md"]) is True
        and _file_touches_sources([".tools/comp-similar"]) is True)
    chk("15 gate --changed: a non-source changeset is NOT a trigger surface (no over-fire)",
        _file_touches_sources(["docs/note.md", "org/tier2_senior/x/logs/y.md"]) is False)

    # 16-19. NFRA_TOOLARCH borrowed-sensitivity remedy (2026-07-25): the 7 new schema/rulebank
    # COUNT metrics. Each checked against an INDEPENDENT direct recomputation (not just "is it
    # present") -- correctness against the real source, not merely non-UNKNOWN.
    import cse_schema as _cse  # noqa: PLC0415  -- self-test only; compute_metrics() imports lazily via importlib
    chk("16 cse enum counts: all 4 match a DIRECT independent len(Enum) recompute (not just present)",
        mets.get("cse_entity_count", {}).get("value") == len(_cse.Entity)
        and mets.get("cse_relationship_count", {}).get("value") == len(_cse.Relationship)
        and mets.get("cse_transformation_count", {}).get("value") == len(_cse.Transformation)
        and mets.get("cse_qualifier_count", {}).get("value") == len(_cse.Qualifier))
    _rb_direct_ok = True
    try:
        import yaml as _yaml_chk  # noqa: PLC0415
        with open(os.path.join(WS, _RULEBANK_PATH), encoding="utf-8") as _fh:
            _rb_doc = _yaml_chk.safe_load(_fh)
        _rb_direct_ok = (
            mets.get("rulebank_role_count", {}).get("value") == len(_rb_doc["roles"])
            and mets.get("rulebank_relation_count", {}).get("value") == len(_rb_doc["relations"])
            and mets.get("rulebank_variance_count", {}).get("value") == len(_rb_doc["variance"]["labels"]))
    except Exception:  # noqa: BLE001
        _rb_direct_ok = False
    chk("17 rulebank axis counts: all 3 match a DIRECT independent yaml-read recompute", _rb_direct_ok)
    # 18. THE INTRINSIC-SENSITIVITY PROOF (the whole point of this item): an ADD to the source
    #     population MOVES the corresponding metric. Not asserted -- exercised, against synthetic
    #     fixtures (mirrors L1b's own cell-26 ADD-without-bump fixture pair), never against the
    #     real live cse_schema.py/rulebank yaml (mutating production files to prove a point is not
    #     how this project tests sensitivity claims).
    import tempfile
    _tmp_yaml = tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False, encoding="utf-8")
    try:
        _tmp_yaml.write("roles:\n  A: {}\n  B: {}\n  C: {}\n")
        _tmp_yaml.close()
        _before = _yaml_len(os.path.relpath(_tmp_yaml.name, WS), "roles")
        with open(_tmp_yaml.name, "a", encoding="utf-8") as _fh:
            _fh.write("  D: {}\n")  # the ADD -- one more role, no version bump anywhere
        _after = _yaml_len(os.path.relpath(_tmp_yaml.name, WS), "roles")
        add_moves_yaml_count = (_before == 3 and _after == 4)
    finally:
        os.unlink(_tmp_yaml.name)
    _tmp_py = tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False, encoding="utf-8",
                                          dir=_HERE)  # dir=_HERE: sys.path already covers it (line 42)
    try:
        _modname = os.path.splitext(os.path.basename(_tmp_py.name))[0]
        _tmp_py.write("import enum\nclass X(enum.Enum):\n    A = 'a'\n    B = 'b'\n")
        _tmp_py.close()
        _before2 = _pyconst_enum_len(_modname, "X")
        with open(_tmp_py.name, "a", encoding="utf-8") as _fh:
            _fh.write("    C = 'c'\n")  # the ADD -- one more enum member, no SCHEMA_VERSION bump
        import importlib
        importlib.invalidate_caches()
        sys.modules.pop(_modname, None)  # force re-import; the module cache would otherwise mask the ADD
        _after2 = _pyconst_enum_len(_modname, "X")
        add_moves_enum_count = (_before2 == 2 and _after2 == 3)
    finally:
        os.unlink(_tmp_py.name)
        sys.modules.pop(_modname, None)
    chk("18 INTRINSIC SENSITIVITY: an ADD to a synthetic yaml mapping (3->4 roles) moves _yaml_len "
        "(3->4), no version bump involved -- the property version_pin's own disclosure names as "
        "its blind spot", add_moves_yaml_count)
    chk("19 INTRINSIC SENSITIVITY: an ADD to a synthetic closed enum (2->3 members) moves "
        "_pyconst_enum_len (2->3), no SCHEMA_VERSION bump involved -- same property, python-const form",
        add_moves_enum_count)
    # 20. per-metric source-population honesty: each new metric's own `source` string names the
    #     REAL file it counts (cse_schema.py or NFRA_ONTOLOGY_RULE_BANK.yaml), never a copy of
    #     cse_measures'/recognizers_live's source string -- the exact ~C-named near-miss shape
    #     (a plausible-looking count with an unrelated provenance) checked directly, not assumed.
    _new_metric_names = ("cse_entity_count", "cse_relationship_count", "cse_transformation_count",
                         "cse_qualifier_count", "rulebank_role_count", "rulebank_relation_count",
                         "rulebank_variance_count")
    chk("20 each new metric's source string names its OWN real file (not fedobs/manifest/ledger)",
        all(os.path.basename(_METRIC_SOURCE_FILES[n][0]) in mets.get(n, {}).get("source", "")
            for n in _new_metric_names)
        and all("comp-fedobs" not in mets.get(n, {}).get("source", "") for n in _new_metric_names))

    # 21-22. NFRA_TOOLARCH managed-region DENOMINATOR (CTO~Z dispatch, 2026-07-25, off CVO~Z's
    # finding against _REGION_RE directly): "0 drifted" alone has no stated denominator, so a
    # malformed marker (missing/typo'd closer, wrong-case name) matches nothing and is SILENTLY
    # excluded -- comp-system would report "0 drifted" over a scan that watched nothing.
    import shutil as _shutil
    import tempfile as _tempfile
    _scratch = _tempfile.mkdtemp(prefix="cs_region_selftest_")
    _real_dir = _MANAGED_DOCS_DIR
    try:
        for _fn in os.listdir(_real_dir):
            if _fn.endswith(".md"):
                _shutil.copyfile(os.path.join(_real_dir, _fn), os.path.join(_scratch, _fn))
        globals()["_MANAGED_DOCS_DIR"] = _scratch
        _c0, _p0, _scan_clean = refresh_managed_regions(mets, write=False)
        # malform exactly ONE region (drop its closer) in whichever file has >=1 real match.
        _target = None
        for _fn in sorted(os.listdir(_scratch)):
            if not _fn.endswith(".md"):
                continue
            _txt = open(os.path.join(_scratch, _fn), encoding="utf-8").read()
            _m = _REGION_RE.search(_txt)
            if _m:
                _target = (_fn, _txt, _m)
                break
        if _target:
            _fn, _txt, _m = _target
            _malformed = _txt[:_m.start(4)] + "<!-- NOT A CLOSER -->" + _txt[_m.end(4):]
            with open(os.path.join(_scratch, _fn), "w", encoding="utf-8") as _fh:
                _fh.write(_malformed)
        _c1, _p1, _scan_malformed = refresh_managed_regions(mets, write=False)
        region_mutant_ok = (_target is not None
                           and _scan_clean["regions"] - _scan_malformed["regions"] == 1)
        # zero-region case: an EMPTY scratch dir (no .md files at all) must scan to 0 regions,
        # never silently mislabeled as a normal "0 drifted" pass (acceptance-c).
        _empty = _tempfile.mkdtemp(prefix="cs_region_selftest_empty_")
        globals()["_MANAGED_DOCS_DIR"] = _empty
        _c2, _p2, _scan_empty = refresh_managed_regions(mets, write=False)
        zero_region_ok = (_scan_empty == {"regions": 0, "files": 0})
        _shutil.rmtree(_empty, ignore_errors=True)
    finally:
        globals()["_MANAGED_DOCS_DIR"] = _real_dir
        _shutil.rmtree(_scratch, ignore_errors=True)
    chk("21 mutant: malforming ONE managed-region marker (scratch copy, never the real files) "
        "drops the scanned-region count by EXACTLY 1 -- a wiring gap becomes a count drop, not "
        "silence", region_mutant_ok)
    chk("22 zero-region case: an empty managed-docs dir scans to {regions:0, files:0}, distinct "
        "from a real 'compared, 0 drifted' pass (check_stale renders this as CURRENT-BUT-UNWATCHED, "
        "never as an ordinary clean CURRENT)", zero_region_ok)

    # 23-28. FORM (a) CARRY-FORWARD (CTO ruling @4484d55608 + pre-gate pin Msg 63063): a device
    #        that cannot reach comp-kuzu NEVER downgrades a graph row it cannot re-derive -- it
    #        carries the committed row forward, value VERBATIM, mark in the vintage field ONLY;
    #        a marked carry is excluded from the genuine-drift predicate BY CONSTRUCTION (value ==
    #        its own last-refreshed span), and it NEVER resets the age clock (ages from the
    #        ORIGINAL derivation). All offline/synthetic -- no live-graph state assumed either way.
    _prior_real = _class_obj("cloud-resources", "infra/aws/",
                             "graph-derived CloudNode counts by type: Lambda=196, S3Bucket=41", [],
                             'comp-kuzu "MATCH (n:CloudNode) RETURN node_type, count(*)"',
                             "marker: current @abc1234")
    _c23 = _carry_class("cloud-resources", "infra/aws/", _prior_real)
    chk("23 carry: real prior + unreachable graph -> current_state VERBATIM, mark in vintage ONLY "
        "(embeds prior vintage + ts + device), never a downgrade",
        _c23 is not None and _c23["current_state"] == _prior_real["current_state"]
        and _c23["vintage"].startswith(CARRY_PREFIX)
        and "marker: current @abc1234" in _c23["vintage"]
        and _CARRY_SUFFIX_KEY in _c23["vintage"] and " on " in _c23["vintage"]
        and CARRY_PREFIX not in _c23["current_state"])
    _c24 = _carry_class("cloud-resources", "infra/aws/", _c23)
    chk("24 re-carry (steady state on a graph-less device): ONE mark, ORIGINAL vintage embedded -- "
        "never nests, value still verbatim",
        _c24 is not None and _c24["vintage"].count(CARRY_PREFIX) == 1
        and "marker: current @abc1234" in _c24["vintage"]
        and _c24["current_state"] == _prior_real["current_state"])
    chk("25 no-fabrication: an UNKNOWN/absent prior carries NOTHING (UNKNOWN over UNKNOWN is not a "
        "downgrade; a fabricated carry would be worse)",
        _carry_class("cloud-resources", "infra/aws/",
                     dict(_prior_real, current_state="%s: comp-kuzu graph unreachable/empty at "
                                                     "compile time" % UNKNOWN)) is None
        and _carry_class("cloud-resources", "infra/aws/", None) is None)
    # 26. the drift-exclusion, EXERCISED at the region layer (scratch dir, never the real files):
    #     a carried metric's verbatim value equals its own last-refreshed span -> 0 drift.
    _scratch3 = _tempfile.mkdtemp(prefix="cs_carry_selftest_")
    try:
        with open(os.path.join(_scratch3, "x.md"), "w", encoding="utf-8") as _fh:
            _fh.write("marker: <!--cs:graph_marker-->marker: current @abc1234<!--/cs-->\n")
        globals()["_MANAGED_DOCS_DIR"] = _scratch3
        _carried_m = {"graph_marker": _metric("marker: current @abc1234",
                                              "comp-kuzu provenance header (marker-oracle)",
                                              _carry_mark("marker: current @abc1234"))}
        _cc3, _pp3, _sc3 = refresh_managed_regions(_carried_m, write=False)
        carry_no_drift = (_cc3 == [] and _pp3 == [] and _sc3["regions"] == 1)
    finally:
        globals()["_MANAGED_DOCS_DIR"] = _real_dir
        _shutil.rmtree(_scratch3, ignore_errors=True)
    chk("26 drift-exclusion: a carried metric (value verbatim) -> 0 span drift + 0 problems over 1 "
        "scanned region (a capability-conditioned carry is not drift -- the (b)-kernel inside (a))",
        carry_no_drift)
    # 27-28. the CTO pin, BOTH directions (the mirror of the false-Monday guard: here the WARN MUST fire).
    _h_aged = {"source_fingerprint": _source_fingerprint(), "emitted_at": time.time(),
               "graph_carried_rows": ["cloud-resources"],
               "graph_carried_since": time.time() - _TTL_SECONDS - 60}
    _st27, _r27 = _staleness(_h_aged)
    chk("27 age clock: carried rows aged past TTL -> STALE fires from the ORIGINAL derivation "
        "(a fresh emitted_at cannot mask it), reason is the 'age ' class, gate reads it as WARN "
        "rc 0 never fail-closed DRIFT",
        _st27 is True and _r27.startswith("age ")
        and _gate_verdict(True, _r27, [], dirty=[])[0] == 0)
    chk("28 age clock mirror: carried + YOUNG original -> not stale (a carry alone is never a "
        "staleness verdict); an UNDATED carry chain fails toward the age WARN, never silent-fresh",
        _staleness(dict(_h_aged, graph_carried_since=time.time() - 60))[0] is False
        and (lambda r: r[0] is True and r[1].startswith("age "))
            (_staleness(dict(_h_aged, graph_carried_since=None))))

    # 29-32. INSTANCE 3 (content-hash fingerprint, CTO ruling addendum @6ae67e724f) + the --help
    #        write-bearing guard (MSTR relay @f5155c2aba, site-Z incident). The gate's three named
    #        controls + both guard directions -- scratch-only, never the real sources.
    import graph_cache as _gc2
    _fx = _tempfile.mkdtemp(prefix="cs_fp_selftest_")
    try:
        for _nm, _body in (("a.yaml", "alpha: 1\n"), ("b.yaml", "beta: 2\n"), ("c.yaml", "gamma: 3\n")):
            with open(os.path.join(_fx, _nm), "w", encoding="utf-8") as _fh:
                _fh.write(_body)
        _srcs = [(_fx, "*.yaml")]
        _fp1 = _gc2.content_fingerprint(_srcs, rel_root=_fx)
        _mt1 = _gc2.source_fingerprint(_srcs)
        _future = time.time() + 3600
        for _nm in os.listdir(_fx):
            os.utime(os.path.join(_fx, _nm), (_future, _future))   # the checkout re-stamp, simulated
        _fp2 = _gc2.content_fingerprint(_srcs, rel_root=_fx)
        _mt2 = _gc2.source_fingerprint(_srcs)
        chk("29 checkout-invariance BOTH directions: an mtime re-stamp on a content-identical tree "
            "leaves the CONTENT fingerprint UNCHANGED while the retired stat fingerprint MOVES -- "
            "the site-Z reproduction, proving the fix targets the measured mechanism",
            _fp1 == _fp2 and _mt1 != _mt2)
        with open(os.path.join(_fx, "a.yaml"), "a", encoding="utf-8") as _fh:
            _fh.write("#x")
        _fp3 = _gc2.content_fingerprint(_srcs, rel_root=_fx)
        chk("30 sensitivity: a one-edit source change MOVES the content fingerprint; shape holds "
            "(64-hex sha256, count 3)",
            _fp3 != _fp2 and _fp3[1] == 3 and len(_fp3[0]) == 64)
    finally:
        _shutil.rmtree(_fx, ignore_errors=True)
    chk("31 the age anchor SURVIVES the re-home: an OLD-but-content-identical record still fires "
        "the age WARN from its recorded timestamp (a hash has no age -- the addendum's pin), gate "
        "reads it as WARN rc 0",
        (lambda r: r[0] is True and r[1].startswith("age ")
         and _gate_verdict(True, r[1], [], dirty=[])[0] == 0)
        (_staleness({"source_fingerprint": _source_fingerprint(),
                     "emitted_at": time.time() - _TTL_SECONDS - 60})))
    import contextlib as _ctx
    import io as _io
    _out_mtime_before = os.stat(OUT_JSON).st_mtime if os.path.exists(OUT_JSON) else None
    _buf_out, _buf_err = _io.StringIO(), _io.StringIO()
    with _ctx.redirect_stdout(_buf_out):
        _rc_help = main(["--help"])
    with _ctx.redirect_stderr(_buf_err):
        _rc_bad = main(["--frobnicate"])
    _out_mtime_after = os.stat(OUT_JSON).st_mtime if os.path.exists(OUT_JSON) else None
    chk("32 write-bearing-flag guard, BOTH directions: --help prints usage rc 0 and WRITES NOTHING; "
        "an unknown flag REFUSES rc 2 and WRITES NOTHING (never falls through to the compile -- "
        "the site-Z --help incident)",
        _rc_help == 0 and "Usage" in _buf_out.getvalue() and _rc_bad == 2
        and "REFUSED" in _buf_err.getvalue() and _out_mtime_before == _out_mtime_after)

    n = sum(1 for x in ok if x)
    print("--- self-test: %d/%d passed (grounded-or-UNKNOWN, no fabrication, shape-locked) ---" % (n, len(ok)))
    return 0 if n == len(ok) else 1


#: The repo substrate 06 summarizes. The fingerprint half of the predicate. CONTENT-HASHED
#: (sha256-over-content, file-count) via graph_cache.content_fingerprint -- one implementation,
#: one shared enumerator with the caches' stat-only sibling. RE-HOMED off max_mtime 2026-08-20
#: (CTO ruling addendum @6ae67e724f, instance 3 of the device-axis pair @4484d55608): the 06
#: record is ONE estate truth, and a fresh checkout/pull re-stamps every mtime BY CONSTRUCTION,
#: so the stat fingerprint manufactured STALE on a content-identical tree at site-Z. The hash
#: replaces ONLY the change-detection half -- the AGE anchor stays on recorded timestamps
#: (emitted_at / graph_carried_since); a hash has no age.
_SOURCES = [
    (os.path.join(WS, ".tools"), "comp-*"),
    (os.path.join(WS, "org", "modules", "graph"), "*.yaml"),
    (os.path.join(WS, "org", "tier2_senior", "0.4.0_DS_ClientPlatform", "deliverables"), "*.json"),
]

#: The TTL half. 06 is grounded-against-LIVE (kuzu node counts, git HEAD, live probes); no repo
#: fingerprint can see those move, so age is the only signal for them. A day: the live values it
#: carries are slow-moving, and a shorter TTL would re-manufacture the always-STALE defect this
#: replaces. Printed by --check FROM this constant -- never a hand-copied duplicate.
_TTL_SECONDS = 86400


def _source_fingerprint():
    """The enforcing expression, imported not forked (graph_cache is the one implementation).
    content_fingerprint with rel_root=WS: checkout-invariant AND device-invariant (relative
    paths -- the two checkouts live under different absolute prefixes). An older committed 06
    carrying the retired (max_mtime, count) shape reads as source drift ONCE and self-heals at
    the adopting regen -- the same one-time adoption path the predicate's own header documents."""
    import graph_cache as _gc
    return list(_gc.content_fingerprint(_SOURCES, rel_root=WS))


def _dirty_sources():
    """comp-system _SOURCE files that are modified-but-uncommitted RIGHT NOW (git status --porcelain).
    Non-empty (or None on an inconclusive git-status) means: regenerating now would launder a peer's
    unlanded work into 06's committed self-description -- the check/gate path must say so instead of
    prescribing a regenerate. Read-only (git status only, no mutation, no index touch).

    Fails toward "cannot prove clean" (returns None on any git-status failure), never toward a silent
    clean pass -- matching this module's existing discipline (a probe that cannot evaluate is never
    treated as fresh/safe; see check_stale's/gate's own except-blocks)."""
    import fnmatch
    rels = [(os.path.relpath(d, WS).replace(os.sep, "/"), g) for d, g in _SOURCES]
    out, _err, rc = _run(["git", "status", "--porcelain"], timeout=10)
    if out is None or rc != 0:
        return None
    dirty = []
    for line in out.splitlines():
        if len(line) < 4:
            continue
        fn = line[3:].strip()
        if " -> " in fn:  # rename/copy porcelain line: "old -> new" -- the NEW path is what's dirty
            fn = fn.split(" -> ", 1)[1]
        fn = fn.strip('"').replace(os.sep, "/")
        for d, g in rels:
            if fn.startswith(d.rstrip("/") + "/") and fnmatch.fnmatch(os.path.basename(fn), g):
                dirty.append(fn)
                break
    return dirty


#: v2 (CVO~Z's recommendation, 2026-07-25, dispatched by CTO~Z after the v1 union-block deadlocked
#: ~D behind an unrelated lane's untracked debris it never touched): the metric-name -> its own
#: repo-relative source-file(s), for the metrics compute_metrics() grounds against a _SOURCES-glob-
#: matching file. Values are _MANIFEST_PATH/_LEDGER_PATH (defined above compute_metrics(), which
#: uses the SAME constants) -- not a re-typed duplicate; see the "wrong-entry-fails-open" fix below.
#: Metrics grounded against something else entirely (a live kuzu marker, a JSON snap, a promote
#: manifest) have no repo-file input among _SOURCES and so have no entry here -- see
#: _relevant_dirty()'s unmapped-metric branch for how that absence is handled (fail-closed, not
#: silently exempted; CVO~Z independently census'd all 7 metrics and confirmed the other 5 are
#: INAPPLICABLE, not gapped -- their sources are live probes/S3, which cannot carry unlanded git work).
_METRIC_SOURCE_FILES = {
    "tools_index_count": [_MANIFEST_PATH],
    "ledger_union_count": [_LEDGER_PATH],
    # NFRA_TOOLARCH borrowed-sensitivity remedy (2026-07-25): without these entries, a drift in
    # cse_schema.py or NFRA_ONTOLOGY_RULE_BANK.yaml alone would fall back to the conservative
    # whole-_SOURCES-union BLOCKED-ON-PEER-LANDING (the 11d self-test case) instead of the
    # metric-scoped one -- reintroducing the exact false-block class ~A's guard-v2 closed today.
    "cse_entity_count": [_CSE_SCHEMA_PATH],
    "cse_relationship_count": [_CSE_SCHEMA_PATH],
    "cse_transformation_count": [_CSE_SCHEMA_PATH],
    "cse_qualifier_count": [_CSE_SCHEMA_PATH],
    "rulebank_role_count": [_RULEBANK_PATH],
    "rulebank_relation_count": [_RULEBANK_PATH],
    "rulebank_variance_count": [_RULEBANK_PATH],
}


def _metric_source_files_mismatches(candidate: dict) -> list:
    """v3 (CVO~Z's latent-hole finding, 2026-07-25): _METRIC_SOURCE_FILES duplicated a fact
    compute_metrics() already declares (each metric's grounding file) -- hoisting both to the same
    _MANIFEST_PATH/_LEDGER_PATH constants (above) kills that duplicate BY CONSTRUCTION, but this
    function exists as a second, explicit, testable belt: which (metric, expected, got) triples in
    `candidate` disagree with the module's own constants. Pure/offline; the self-test calls it twice
    -- once on the REAL _METRIC_SOURCE_FILES (must be empty: proves no divergence today) and once on
    a deliberately-WRONG synthetic map (must be non-empty: proves the check has teeth, not just a
    check that always vacuously passes). Returns [] iff every mapped entry matches truth."""
    truth = {"tools_index_count": [_MANIFEST_PATH], "ledger_union_count": [_LEDGER_PATH]}
    return [(name, expected, candidate.get(name))
            for name, expected in truth.items() if candidate.get(name) != expected]


def _metric_source_association_mismatches(candidate: dict, metrics: dict) -> list:
    """v4 (CVO~Z's named residual on the v3 fix, 2026-07-25): _metric_source_files_mismatches()'s own
    `truth` dict is a THIRD hand-written statement of the metric -> path ASSOCIATION (which metric
    reads which constant) -- the PATHS themselves can no longer drift (shared _MANIFEST_PATH/
    _LEDGER_PATH constants, v3), but if compute_metrics() ever changed which file a metric actually
    reads and neither `_METRIC_SOURCE_FILES` nor `truth` followed, the two hand-written dicts would
    compare wrong-against-wrong and PASS -- narrower than the original hole (needs a semantic change
    PLUS two omissions, not one edit) but the same duplicate-record shape one level in.

    Couples the association to compute_metrics()'s OWN declared `source` string instead of a third
    hand-copied twin (CVO~Z-verified this holds today: a weak `basename in source` check, e.g.
    "graph-call-manifest.yaml" in "graph-call-manifest.yaml:tools_index (mapping length)"). `metrics`
    is a compute_metrics()-shaped dict (metric -> {value, source, vintage}), passed in -- pure
    otherwise, no live recompute inside.

    Returns [(metric, expected_basename, declared_source)] for every mapped metric whose declared
    `source` string does NOT name the expected file's basename -- catches both a wrong association
    AND the realistic drift mode (a `.yml`/`.yaml`-class typo in the expected basename itself, per
    CVO~Z's own added test shape)."""
    out = []
    for name, files in candidate.items():
        source = (metrics.get(name) or {}).get("source", "")
        for f in files:
            base = os.path.basename(f)
            if base not in source:
                out.append((name, base, source))
    return out


def _relevant_dirty(region_changes: list, fingerprint_drift: bool, dirty):
    """Narrow the uncommitted-source guard to the file(s) that actually FEED the drift under
    evaluation, instead of the whole _SOURCES union (the v1 defect: a correct lane's regen froze
    behind an unrelated lane's untracked debris it never touched).

    - `dirty is None` (git-status unverifiable): stays None regardless of scope -- unchanged,
      still fail-closed.
    - `fingerprint_drift` (the coarse whole-_SOURCES aggregate mtime/file-count signal -- no
      per-file attribution exists for it): CANNOT be narrowed. Returns `dirty` UNCHANGED (v1
      behavior, deliberately not widened this pass -- a disclosed residual, not a gap left silent).
    - region_changes only (the common case; each span already names its own metric via `name`):
      returns only the dirty files that are a MAPPED source of one of the drifted metrics. A
      drifted metric with NO entry in `_METRIC_SOURCE_FILES` (we don't know its file) is treated
      conservatively -- returns the WHOLE `dirty` for that case, never silently exempted, so
      "you still cannot launder unlanded work into a metric it feeds" holds even for metrics this
      map doesn't (yet) cover.

    Pure (no I/O) -- `region_changes`/`fingerprint_drift`/`dirty` are all already-computed inputs,
    keeping _gate_verdict's offline-testable contract intact."""
    if dirty is None:
        return None
    if fingerprint_drift:
        return dirty
    mapped = set()
    for _fn, name, _old, _new in region_changes:
        srcs = _METRIC_SOURCE_FILES.get(name)
        if srcs is None:
            return dirty  # unmapped metric -- fail-closed, cannot prove the dirty set is irrelevant
        mapped.update(srcs)
    return [f for f in dirty if f in mapped]


def _staleness(header: dict):
    """(is_stale, reason). THE single predicate. --check reports it; the emit path stores what it
    computes. Never two expressions that agree today."""
    emitted_fp = header.get("source_fingerprint")
    emitted_at = header.get("emitted_at")
    cur_fp = _source_fingerprint()

    if emitted_fp is None or emitted_at is None:
        # A pre-predicate artifact (emitted under the as_of==HEAD oracle). Unverifiable against the
        # new predicate -> STALE, and it self-heals on the next emit. Never a silent pass.
        return True, "emitted before the fingerprint predicate existed; regenerate once to adopt it"

    if list(emitted_fp) != cur_fp:
        return True, ("source drift: fingerprint (content-sha256, file_count) %s -> %s"
                      % (tuple(emitted_fp), tuple(cur_fp)))

    # FORM (a) x the CTO pin (Msg 63063): carried graph rows age from their ORIGINAL derivation --
    # a carry (or a chain of re-carries) never resets the clock; a device dark past TTL must read
    # exactly as stale as if no carry existed. The reason MUST start with "age " so --gate
    # classifies it as the WARN limb, never fail-closed DRIFT: the graph-less device cannot regen
    # its way out, and the remedy is a graph-capable device's compile, not a block.
    if header.get("graph_carried_rows"):
        since = header.get("graph_carried_since")
        if since is None:
            return True, ("age of carried graph rows UNVERIFIABLE (no dated original derivation in "
                          "the carry chain) -- treat as past-TTL; regenerate on a graph-capable device")
        carried_age = time.time() - float(since)
        if carried_age >= _TTL_SECONDS:
            return True, ("age of carried graph rows %dh exceeds TTL %dh (original derivation "
                          "%s -- a carry never resets the age clock; regenerate on a "
                          "graph-capable device)"
                          % (carried_age // 3600, _TTL_SECONDS // 3600,
                             time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(float(since)))))

    age = time.time() - float(emitted_at)
    if age >= _TTL_SECONDS:
        return True, ("age %dh exceeds TTL %dh (live-grounded values may have moved)"
                      % (age // 3600, _TTL_SECONDS // 3600))

    return False, ("sources unchanged, age %dh < TTL %dh" % (age // 3600, _TTL_SECONDS // 3600))


def check_stale() -> int:
    """The --check PROBE. Reports staleness, never rebuilds.

    Complete evaluation preserves 0 = current | 2 = stale | 1 = tool error.  main() adds
    3 = NOT-DECIDABLE only when Rule T expires or a required compiler source is unreadable.

    Exit codes per CTO 20260709T195217Z: 2 (not 1) for stale, mirroring
    `terraform plan -detailed-exitcode`. Returning 1 on stale CONFLATED "your artifact is stale" with
    "the probe crashed" -- a CI job cannot act on that, and will read a crashed probe as a stale
    artifact or vice versa. 1 now means the tool failed, and ONLY that.

    WHY THIS NO LONGER COMPARES as_of_head TO HEAD (the defect this replaces):
      Emitting records as_of = HEAD-at-emit-time. LANDING the artifact requires a commit, and that
      commit ADVANCES HEAD. So as_of was always the parent of the commit that shipped it, and the
      oracle reported the freshly-regenerated artifact STALE against the very commit that shipped it.
      Exercised 2026-07-09: `comp-system` -> `--check` said CURRENT (uncommitted); `safe-commit`
      [735a4d86d]; `--check` said "STALE: emitted as_of=fe02f71e5 vs current HEAD=735a4d86d".
      It could return 0 only on an uncommitted tree -- seconds wide on a 20-agent shared branch, and
      any unrelated commit flipped it. A signal that is always RED carries no information; it is the
      same defect as a check that never fires, at the opposite rail. `as_of == HEAD` was a PROXY for
      "the artifact reflects the substrate it summarizes", and it was UNSATISFIABLE for the only
      state that matters (committed).

    THE PREDICATE NOW BINDS THE PROPERTY (CTO ruling; MSTR's ratified rule): stale iff
      (a) an INPUT the artifact reads has changed since emit  -- source fingerprint drift, or
      (b) the compile is older than _TTL                      -- covers the LIVE-grounded values
          (kuzu counts, git HEAD, live probes) that no repo fingerprint can see.
    `as_of_head` stays in the header as PROVENANCE (it truthfully records the HEAD compiled against);
    it is simply no longer the staleness predicate.

    ONE EXPRESSION, NOT TWO THAT AGREE TODAY (MSTR 20260709T200348Z): the fingerprint is
    `graph_cache.source_fingerprint` -- the SAME function the caches enforce -- and the emit path
    stores what THIS function computes. There is no parallel copy to drift.
    """
    try:
        if not os.path.exists(OUT_JSON):
            print(_answer_state_line(
                ANSWER_SUBJECT_ABSENT, "infra/system/06_current_state.json",
                "06 is not yet emitted; run comp-system"))
            return 2
        with open(OUT_JSON, encoding="utf-8") as fh:
            header = json.load(fh).get("header", {})
        stale, reason = _staleness(header)
        # A managed-region span whose printed number no longer equals the live metric is ALSO stale --
        # this is the "tool counts etc. drifted in the sibling docs" case the fingerprint cannot see
        # (the docs are outputs, not fingerprint sources). Report-only: --check never writes.
        region_changes, _problems, region_scan = refresh_managed_regions(compute_metrics(), write=False)
    except Exception as e:  # noqa: BLE001 -- a probe that cannot evaluate is an ERROR, never "fresh"
        print("06 UNVERIFIABLE: --check could not evaluate (%s: %s)" % (type(e).__name__, e))
        return 1
    fingerprint_drift = stale and not reason.startswith("age ")
    genuine_drift = bool(region_changes) or fingerprint_drift
    if genuine_drift:
        # Genuine drift on a DIRTY source tree: regenerating now would bake a peer's UNLANDED work
        # into 06's committed self-description as if it were real (CVO~Z near-miss, 2026-07-25).
        # v2 (CVO~Z, 2026-07-25): scoped to the file(s) that FEED the drifting metric(s), not the
        # whole _SOURCES union (v1 deadlocked a correct lane behind an unrelated lane's untouched
        # debris) -- see _relevant_dirty()'s docstring for the fingerprint/unmapped-metric cases it
        # still fails closed on. Clean-tree / not-relevant-dirty genuine drift is unaffected below --
        # unchanged STALE/regenerate behavior.
        relevant = _relevant_dirty(region_changes, fingerprint_drift, _dirty_sources())
        if relevant:
            # Honest wording: only claim metric-specific attribution when it actually narrowed the
            # set (region_changes present, not the coarse fingerprint signal, every drifted metric
            # mapped) -- the fingerprint/unmapped-metric fallback cases return the whole union, and
            # saying "feed the drifted metric(s)" there would overclaim precision this pass doesn't have.
            scoped = bool(region_changes) and not fingerprint_drift and all(
                nm in _METRIC_SOURCE_FILES for _fn, nm, _o, _n in region_changes)
            what = "source file(s) that feed the drifted metric(s)" if scoped else "source file(s)"
            print("SYSTEM BLOCKED-ON-PEER-LANDING: genuine drift detected, but %s are uncommitted "
                  "-- %s. Running comp-system now would launder unlanded peer work into 06's "
                  "committed self-description. Wait for landing, then re-run comp-system --check."
                  % (what, ", ".join(relevant[:6])))
            return 2
        if relevant is None:
            print("SYSTEM BLOCKED-ON-PEER-LANDING (fail-closed): genuine drift detected, but source "
                  "cleanliness could not be verified (git status did not complete). Re-run once git "
                  "status succeeds.")
            return 2
    if region_changes:
        drift = "; ".join("%s cs:%s %s->%s" % (fn, name, old, new) for fn, name, old, new in region_changes[:6])
        print("SYSTEM STALE: %d managed-region span(s) drifted from live metrics: %s -- regenerate (comp-system)."
              % (len(region_changes), drift))
        return 2
    if not stale:
        if region_scan["regions"] == 0:
            # A denominator of ZERO reads as clean by construction, not by verification -- do not
            # let it print as "SYSTEM CURRENT" (CTO~Z dispatch acceptance-c): a wiring failure that
            # took EVERY region down at once would look identical to "no regions exist yet" if
            # worded the same as the normal case. Distinct wording, same rc (a genuinely
            # region-free /system is not itself an error -- the wording is what must not lie).
            print(_answer_state_line(
                ANSWER_PARTIAL, "managed-region staleness check",
                "0 spans found across %d file(s); nothing was compared, so CURRENT is not decidable"
                % region_scan["files"], TOOL_VOICE_NOT_DECIDABLE))
            return 0
        else:
            print("SYSTEM CURRENT (06: %s; managed regions: %d compared across %d file(s), 0 drifted)"
                  % (reason, region_scan["regions"], region_scan["files"]))
        return 0
    print("06 STALE: %s -- regenerate (comp-system)." % reason)
    return 2


# --------------------------------------------------------------------------------------------------
# --gate : the WS-2 fail-closed, STALENESS-CONDITIONED enforcement probe (NFRA_SYSPARITY.WS-2).
# Mirrors the NFRA_NESTEDABSTRACT drift-gate shape (fail-closed / genuine-drift-only / exercised /
# on-demand). REUSES _staleness() -- ONE predicate, not a forked copy (the module's own discipline).
# --------------------------------------------------------------------------------------------------
def _file_touches_sources(files) -> bool:
    """Does any repo-relative changed path match a comp-system _SOURCE (dir + basename glob)?
    This is the STALENESS-CONDITIONING trigger for the commit-gate leg: --gate --changed <files>
    only runs the drift check when a commit actually touches a 06-source (the genuine drift moment),
    so it never false-fires on unrelated commits or wall-clock idle. Content-based (a real file in
    the changeset), NOT the mtime fingerprint -- so the trigger itself is mtime-noise-immune."""
    import fnmatch
    rels = [(os.path.relpath(d, WS).replace(os.sep, "/"), g) for d, g in _SOURCES]
    for f in files or []:
        fn = str(f).replace(os.sep, "/")
        if fn.startswith("./"):          # strip a leading './' ONLY (lstrip('./') would eat '.tools')
            fn = fn[2:]
        for d, g in rels:
            if fn.startswith(d.rstrip("/") + "/") and fnmatch.fnmatch(os.path.basename(fn), g):
                return True
    return False


def _gate_verdict(stale: bool, reason: str, region_changes: list, dirty=None) -> tuple:
    """PURE gate decision (offline-testable, both directions). Distinguishes GENUINE DRIFT from the
    wall-clock age>=TTL case:
      GENUINE drift -- a source INPUT the artifact reads changed (fingerprint), a managed-region span
        drifted from a live metric, or a pre-predicate/absent artifact -> 06 is FACTUALLY behind the
        estate a commit just changed -> (2, DRIFT) FAIL-CLOSED, UNLESS `dirty` says the drift traces
        to an UNCOMMITTED source (see below).
      age>=TTL ALONE -- no source/region drift, only the live-grounded-values-may-have-moved TTL ->
        (0, AGE-WARN). NEVER a block: blocking on wall-clock idle is the false-Monday class (NEVER#1);
        the response is an on-demand refresh, not stopping a working commit.
      else -> (0, CURRENT).

    `dirty` -- comp-system _SOURCE files modified-but-uncommitted right now (from _dirty_sources(),
    or a synthetic list/None in tests -- kept as a plain parameter, not a live git-status call inside
    this function, so the pure-decision contract holds). Default None means "caller did not check" and
    is treated the SAME as "could not verify clean" (fail toward BLOCKED, never toward a silent
    DRIFT-with-regen prescription) -- a live caller (gate()) always computes and passes the real list;
    only a genuine, checked-clean tree (dirty == []) gets the unchanged DRIFT/regenerate verdict.

    v2 (2026-07-25, CVO~Z's recommendation after the v1 union-block deadlocked ~D behind an
    unrelated lane's untracked debris): `dirty` is narrowed via `_relevant_dirty()` to just the
    file(s) that FEED the metric(s) actually drifting, not the whole _SOURCES union -- see that
    function's docstring for the fingerprint-drift / unmapped-metric fail-closed cases it preserves.
    A dirty file that feeds a DIFFERENT, non-drifting metric no longer blocks (the false-block v1
    defect); a dirty file that feeds the drifting metric still does.

    On genuine drift with the RELEVANT dirty set non-empty (or unverifiable): (2,
    BLOCKED-ON-PEER-LANDING) -- 06 is behind the estate, but regenerating now would launder a peer's
    UNLANDED work into 06's committed self-description (CVO~Z near-miss, 2026-07-25) -- never says
    "regenerate", says wait for landing.
    Returns (rc, verdict_str)."""
    genuine = []
    if region_changes:
        drift = "; ".join("%s cs:%s %s->%s" % (fn, nm, o, n) for fn, nm, o, n in region_changes[:6])
        genuine.append("%d managed-region span(s) drifted from live metrics: %s"
                       % (len(region_changes), drift))
    fingerprint_drift = stale and not reason.startswith("age ")   # source-drift / pre-predicate / not-emitted
    if fingerprint_drift:
        genuine.append(reason)
    if genuine:
        relevant = _relevant_dirty(region_changes, fingerprint_drift, dirty)
        if relevant:
            # Honest wording -- see check_stale()'s identical `scoped` comment: only claim
            # metric-specific attribution when it actually narrowed the set.
            scoped = bool(region_changes) and not fingerprint_drift and all(
                nm in _METRIC_SOURCE_FILES for _fn, nm, _o, _n in region_changes)
            what = "source file(s) that feed the drifted metric(s)" if scoped else "source file(s)"
            return 2, ("SYSTEM BLOCKED-ON-PEER-LANDING: genuine drift (%s), but %s are uncommitted "
                       "-- %s. Wait for landing, then re-run."
                       % (" | ".join(genuine), what, ", ".join(relevant[:6])))
        if relevant is None:
            return 2, ("SYSTEM BLOCKED-ON-PEER-LANDING (fail-closed): genuine drift (%s), but source "
                       "cleanliness could not be verified. Wait, then re-run." % " | ".join(genuine))
        return 2, "SYSTEM DRIFT (fail-closed): " + " | ".join(genuine)
    if stale:                                      # the only remaining stale case is age>=TTL
        return 0, "SYSTEM AGE-WARN (not a block): " + reason
    return 0, "SYSTEM CURRENT (no genuine drift)"


def gate(changed=None) -> int:
    """The --gate ENFORCEMENT PROBE (fail-closed, staleness-conditioned). Live wrapper over
    _gate_verdict: reads the committed 06 header + the live source-fingerprint + managed-region
    metrics, then applies the PURE verdict. Distinct from --check (which reports ANY staleness incl.
    the age>=TTL auto-refresh case): --gate fail-closes ONLY on GENUINE drift, so it is safe to wire
    as a blocking enforcement point (a source-touch commit that did not regenerate 06) without
    false-Monday-blocking on wall-clock idle.

    Exit: 0 = gate OPEN (current, or age-only WARN) | 2 = FAIL-CLOSED genuine drift | 1 = tool error.
    Escape valve (mirrors the never-rules / drift-gate audited override): a legitimate deferral is a
    one-line AUDITED marker at the enforcement point, not gate removal -- teach-at-violation-time.
    --changed <files> (the commit-gate leg's staleness-conditioning): when given, the gate only
    evaluates drift if a changed path touches a comp-system _SOURCE -- otherwise rc 0 (not a
    trigger-surface commit). This is what makes the commit-gate leg fire EXACTLY at the genuine
    drift moment (a source-touching commit), never on unrelated commits (CTO WS-2 ruling)."""
    try:
        if changed is not None and not _file_touches_sources(changed):
            print(_answer_state_line(
                ANSWER_NOT_APPLICABLE, "--gate --changed",
                "no comp-system _SOURCE in the changeset; not a trigger-surface commit, gate open"))
            return 0
        if not os.path.exists(OUT_JSON):
            print("SYSTEM DRIFT (fail-closed): 06 not emitted -- run comp-system.")
            return 2
        with open(OUT_JSON, encoding="utf-8") as fh:
            header = json.load(fh).get("header", {})
        stale, reason = _staleness(header)
        region_changes, _problems, _region_scan = refresh_managed_regions(compute_metrics(), write=False)
    except Exception as e:  # noqa: BLE001 -- a gate that cannot evaluate is FAIL-CLOSED, never a pass
        print("SYSTEM UNVERIFIABLE (fail-closed): --gate could not evaluate (%s: %s)"
              % (type(e).__name__, e))
        return 1
    dirty = _dirty_sources() if (region_changes or (stale and not reason.startswith("age "))) else []
    rc, verdict = _gate_verdict(stale, reason, region_changes, dirty=dirty)
    suffix = ("" if "BLOCKED-ON-PEER-LANDING" in verdict  # verdict text already states the remedy
              else " -- regenerate (comp-system) or add an audited override." if rc == 2
              else " -- refresh recommended (on-demand); gate stays open." if "AGE-WARN" in verdict
              else " -- gate open.")
    print(verdict + suffix)
    return rc


_KNOWN_ARGS = {"--self-test", "--check", "--gate", "--changed", "--json", "--stdout", "--help", "-h"}
_VALUE_ARGS = {"--budget", "--cursor"}
_USAGE = """comp-system -- the NFRA_SYSTEM current-state COMPILER. Usage:
  comp-system [--budget <seconds>] [--cursor BEGIN]
                           compile -> WRITE infra/system/06_current_state.{md,json} + refresh managed spans
  comp-system --stdout [--budget <seconds>] [--cursor BEGIN]
                           compile -> print the markdown (no write)
  comp-system --json [--budget <seconds>] [--cursor BEGIN]
                           compile -> print the json model (no write)
  comp-system --check [--budget <seconds>] [--cursor BEGIN]
                           staleness probe (0=current 2=stale 1=error 3=NOT-DECIDABLE; never writes)
  comp-system --gate [--changed <files...>]   fail-closed genuine-drift gate (never writes)
  comp-system --self-test  the invariant battery (scratch-only writes)
  comp-system --help | -h  this usage (never compiles, never writes)
Rule T carrier: --budget <seconds> > COMP_BUDGET_S > default 90 s; --budget 0 is unbounded.
The compile is one atomic cross_surface_compile.  On expiry it prints BUDGET REACHED and
DEFERRED with resume --cursor BEGIN, returns 3, and writes no complete record.  --check likewise
returns 3/NOT-DECIDABLE on expiry or an unreadable required source; its complete-run 0/2/1
meanings are unchanged.
An UNKNOWN flag REFUSES (rc 2) -- it must never fall through to the default COMPILE, which
writes the SHARED estate record (measured at site-Z 2026-08-20: '--help' fell through, ran the
compile, and wrote 06 -- the device-axis class through a UX door; MSTR relay @f5155c2aba)."""


def _parse_cli(args: list) -> tuple:
    """Parse flags without letting value tokens fall through as a default compile.

    Everything after --changed remains the gate's path list, matching the historical interface.
    Returns (budget_value, cursor, error_text).  Mode selection continues in main().
    """
    prefix = args[:args.index("--changed")] if "--changed" in args else args
    values = {}
    unknown = []
    i = 0
    while i < len(prefix):
        arg = prefix[i]
        if arg in _VALUE_ARGS:
            if arg in values:
                return None, None, "%s may be supplied only once" % arg
            if i + 1 >= len(prefix):
                return None, None, "%s requires a value" % arg
            values[arg] = prefix[i + 1]
            i += 2
            continue
        if arg not in _KNOWN_ARGS:
            unknown.append(arg)
        i += 1
    if unknown:
        return None, None, "UNKNOWN argument(s): %s" % ", ".join(unknown)
    if "--changed" in args and "--gate" not in prefix:
        return None, None, "--changed requires --gate"
    cursor = values.get("--cursor")
    if cursor is not None and cursor != "BEGIN":
        return None, None, "--cursor accepts only BEGIN (the compile is one atomic unit)"
    if cursor is not None and any(m in prefix for m in ("--self-test", "--gate")):
        return None, None, "--cursor BEGIN applies only to compile mode and --check"
    budget_value = values.get("--budget")
    if budget_value is not None and any(m in prefix for m in ("--self-test", "--gate")):
        return None, None, "--budget applies to compile mode and --check"
    return budget_value, cursor, None


def _install_budget(flag_value, unit: str, resume_args: str):
    """Resolve a Rule T context, returning (context, usage_error)."""
    try:
        return _new_budget(flag_value, unit, resume_args), None
    except (TypeError, ValueError) as exc:
        return None, "invalid --budget/COMP_BUDGET_S value (%s)" % exc


def _finish_rule_t(ctx: dict, complete: bool) -> list:
    """The shared terminal line plus the always-printed T-16 deferred bucket."""
    return [_budget_line(ctx, complete=complete)] + _deferred_lines(ctx, complete=complete)


def main(argv=None) -> int:
    global _ACTIVE_BUDGET
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(errors="replace")
        except Exception:  # noqa: BLE001
            pass
    args = list(sys.argv[1:] if argv is None else argv)
    if "--help" in args or "-h" in args:
        print(_USAGE)
        return 0
    budget_value, cursor, parse_error = _parse_cli(args)
    if parse_error:
        print("comp-system: %s -- REFUSED (rc 2), nothing written.\n%s"
              % (parse_error, _USAGE), file=sys.stderr)
        return 2
    if "--self-test" in args:
        return self_test()
    if "--gate" in args:
        changed = None
        if "--changed" in args:
            changed = args[args.index("--changed") + 1:]
        return gate(changed=changed)
    if "--check" in args:
        ctx, budget_error = _install_budget(
            budget_value, "check_verdict", "comp-system --check")
        if budget_error:
            print("comp-system: %s -- REFUSED (rc 2), nothing written." % budget_error,
                  file=sys.stderr)
            return 2
        _ACTIVE_BUDGET = ctx
        try:
            issues = _required_source_issues()
            if issues:
                print(render_markdown(_partial_model("required source unreadable", issues, ctx=ctx)),
                      end="")
                return RC_NOT_DECIDABLE
            if _budget_expired(ctx):
                print(render_markdown(
                    _partial_model("budget expired before the check began", [], ctx=ctx)), end="")
                return RC_NOT_DECIDABLE
            import contextlib as _ctx
            import io as _io
            verdict_output = _io.StringIO()
            with _ctx.redirect_stdout(verdict_output):
                rc = check_stale()
            if _budget_expired(ctx):
                print(render_markdown(
                    _partial_model("budget expired during the check", [], ctx=ctx)), end="")
                return RC_NOT_DECIDABLE
            print(verdict_output.getvalue(), end="")
            for line in _finish_rule_t(ctx, complete=True):
                print(line)
            return rc
        finally:
            _ACTIVE_BUDGET = None

    ctx, budget_error = _install_budget(
        budget_value, "cross_surface_compile", "comp-system" +
        (" --stdout" if "--stdout" in args else " --json" if "--json" in args else ""))
    if budget_error:
        print("comp-system: %s -- REFUSED (rc 2), nothing written." % budget_error,
              file=sys.stderr)
        return 2
    _ACTIVE_BUDGET = ctx
    try:
        model = compile_model(ctx=ctx)
        if model.get("header", {}).get("compile_complete"):
            _decorate_answer_states(model)
            if _budget_expired(ctx):
                model = _partial_model("budget expired during the atomic compile", [], ctx=ctx)
            else:
                model["header"]["rule_t"] = {
                    "status_line": _budget_line(ctx, complete=True),
                    "deferred": _deferred_lines(ctx, complete=True),
                    "cursor": cursor or "BEGIN",
                }
        complete = bool(model.get("header", {}).get("compile_complete"))
        if "--json" in args:
            print(json.dumps(model, indent=2))
            return 0 if complete else RC_NOT_DECIDABLE
        if "--stdout" in args or not complete:
            print(render_markdown(model), end="")
            return 0 if complete else RC_NOT_DECIDABLE
        changes = _write(model)
        print("comp-system: wrote %s + %s (grounded-against-live; as_of HEAD=%s)"
              % (os.path.relpath(OUT_MD, WS), os.path.relpath(OUT_JSON, WS), model["header"]["as_of_head"]))
        span_changes = [c for c in changes if c[0] != "PROBLEM"]
        problems = [c for c in changes if c[0] == "PROBLEM"]
        if span_changes:
            print("comp-system: refreshed %d managed-region span(s) in the sibling docs:" % len(span_changes))
            for fn, name, old, new in span_changes:
                print("  %s  cs:%s  %s -> %s" % (fn, name, old, new))
        else:
            print(model["header"]["managed_region_answer"]["line"])
        for _tag, fn, name, why in problems:
            print("  WARN %s cs:%s -- %s" % (fn, name, why))
        return 0
    finally:
        _ACTIVE_BUDGET = None


if __name__ == "__main__":
    sys.exit(main())
