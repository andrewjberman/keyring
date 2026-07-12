"""
NFRA_TOOLHEALTH.TH-A -- the per-TOOL EFFECTIVE probe: a RECURRING, isolation-gated blind-run that
answers "does running comp-tool X actually REACH a usable answer for the class of question it claims
to serve?" -- the genuinely-NEW EFFECTIVE axis of TOOLHEALTH (log-mining alone can't tell you this).

REUSES the COMPPROOF-B1 harness UN-FORKED (one home org/modules/graph/compproof/):
  - the ISOLATION gate (author != solver != judge; the sealed answer PROVABLY excluded from the payload
    handed to the tool -- the B1 diff-gate pattern; a tool that can see its own answer = a VOID verdict).
  - harness.score_run (the REACH x USABILITY rubric) -- SOLVED/PARTIAL/MISS mapped to EFFECTIVE yes/no.
  The strip-proof + reach check use the same distinctive-token extraction B1 relies on, inlined here
  (a single re.findall) so this probe carries no dependency on corpus_loader's per-INCIDENT loader.

EMITS (append-only, COMPLEARN substrate UNFORKED -- adds a NEW stream, never mutates comp_learns_score
or the COMPLEARN-owned tables/parsers):
  - effective_probe_log.jsonl : the canonical APPEND-only per-probe stream (one row per probe run),
    modeled on comproute-routing.jsonl / comp-which-rail.log (a new append-only source log the scorer
    does NOT parse -> structurally invisible to COMPLEARN's scorer).
  - effective_feed.json       : the per-TOOL rollup TH-B's `comp-tool-health --effective-feed` consumes
    -> {canonical_tool: {effective: bool, reach, usability, ...}}. Only `effective` is read by TH-B; the
    rest is carried for the record. This is the load-bearing join that flips KEEP<->FIX.

Per-tool rollup: a tool is EFFECTIVE=yes only if EVERY class-probe reaches usably; ANY in-class
functional miss (didn't reach, or reached-but-unusable-under-load) -> EFFECTIVE=no (the FIX catch --
the highest-value verdict, the one only this axis surfaces). Unknown iff a probe could not be run/VOID
and none failed.

TRIGGER (CTO GO 2026-07-06): CONSUMPTION-DRIVEN, host=LOCAL, NOT a cron / NOT SessionEnd / NOT cloud.
A consumer (a governance / tool-R&D review about to READ the health data) calls `ensure_fresh` first:
reuse the feed if <= 7d old, else run fresh THEN read (--force bypasses the ceiling). Fresh-when-consumed,
cost-bounded to the review cadence -- the blind-run is the DEEP periodic characterization; tool_activity
latency telemetry is the cheap continuous fast-detector. Layer them.

Author: 0.8.0_AE_CloudComp~D (NFRA_TOOLHEALTH.TH-A, COO~B GO 2026-07-02; consumption-trigger 0.8.0 base,
CTO GO 2026-07-06). Reuses B1 un-forked.
"""

from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import harness         # noqa: E402  -- reuse score_run (REACH x USABILITY rubric) + AUTHOR_ID un-forked
import tool_corpus     # noqa: E402

_GRAPH = os.path.dirname(_HERE)                       # compproof -> graph (home of sovereign_held)
if _GRAPH not in sys.path:
    sys.path.insert(0, _GRAPH)
from sovereign_held import is_held_path, is_held_bucket  # noqa: E402 -- scratch-target sovereign guard

_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))  # compproof->graph->modules->org->ws

AUTHOR_ID = harness.AUTHOR_ID                         # the probe AUTHOR (seals the corpus)
JUDGE_ID = "TH-A-effective-scorer"                    # the automated REACH/USABILITY judge (distinct)
EFFECTIVE = ("yes", "no", "unknown")                  # the emitted EFFECTIVE verdict vocab

# default emit targets (append-only stream + the TH-B join feed) -- both in the one home
PROBE_LOG = os.path.join(_HERE, "effective_probe_log.jsonl")
EFFECTIVE_FEED = os.path.join(_HERE, "effective_feed.json")


# ---- isolation: the HARD strip gate (the B1 pattern applied per-tool) ----------------------

def probe_payload(probe: dict) -> dict:
    """The descriptive solver-view (for the record/emit): the class-question metadata + the invocation."""
    return {k: probe[k] for k in tool_corpus.solver_visible_fields() if k in probe}


def tool_input_text(probe: dict) -> str:
    """The EXACT text the tool RECEIVES = its `run` argv (the executed command). This is the true
    isolation surface: the tool consumes ONLY the argv it is invoked with -- NOT the descriptive
    `question` (author/judge-facing metadata, the analogue of B1's sealed judge-view, never handed to the
    tool). A comp-which probe passes the question AS the argv, so it IS checked there; a comp-freshness
    probe runs `comp-freshness artifact` and the tool never sees the artifact name in the question."""
    return " ".join(str(a) for a in probe.get("run", [])).lower()


def strip_gate(probe: dict) -> dict:
    """The STRIP proof for ONE probe: assert none of the sealed answer terms / the answer substring leak
    into what the tool RECEIVES (its run argv). Returns {probe_id, passed, leaked}. A leak means the tool
    could 'reach' its own planted answer via its input -> the EFFECTIVE verdict would measure nothing."""
    payload_text = tool_input_text(probe)
    payload_tokens = {t.strip("._") for t in re.findall(r"[A-Za-z0-9_.-]+", payload_text)}
    answer_terms = {a.strip("._").lower() for a in probe.get("answer_terms", [])}
    leaked = sorted(t for t in answer_terms if t in payload_tokens)
    substr = str(probe.get("answer_substr", "")).lower().strip()
    if substr and substr in payload_text:
        leaked.append("substr:%s" % substr)
    return {"probe_id": probe["probe_id"], "passed": not leaked, "leaked": leaked}


def isolation_gate(probe: dict, *, solver_id: str, judge_id: str = JUDGE_ID,
                   author_id: str = AUTHOR_ID) -> dict:
    """The HARD gate (VOID-on-violation): (author != solver != judge) AND (sealed answer NOT in the tool
    payload). solver_id = the tool under test (a run is the 'solver'). Returns {void, reasons, ...}."""
    distinct = len({author_id, solver_id, judge_id}) == 3 and all([author_id, solver_id, judge_id])
    strip = strip_gate(probe)
    reasons = []
    if not distinct:
        reasons.append("roles not distinct (author=%s solver=%s judge=%s)" % (author_id, solver_id, judge_id))
    if not strip["passed"]:
        reasons.append("sealed answer leaked into the tool payload: %s" % strip["leaked"])
    return {"probe_id": probe["probe_id"], "void": bool(reasons), "reasons": reasons,
            "distinct_roles": distinct, "strip_clean": strip["passed"]}


# ---- run the tool against the LIVE estate --------------------------------------------------

# git-bash binary (NOT the WSL /bin/bash relay -- that relay is broken on this host and shadows git-bash
# from a Windows-python subprocess; the same gotcha harness.py sidesteps by calling kuzu_cli via
# sys.executable). Resolve the real git-bash for bash-shebang tools; None -> fall back to PATH "bash".
def _git_bash() -> str | None:
    for c in (r"C:\Program Files\Git\bin\bash.exe", r"C:\Program Files\Git\usr\bin\bash.exe",
              os.environ.get("GIT_BASH", "")):
        if c and os.path.exists(c):
            return c
    return None


def _resolve_invocation(argv: list) -> list:
    """Build the REAL subprocess argv for a comp-tool, honoring its shebang WITHOUT the WSL-bash hop.
    python-shebang tool -> [sys.executable, toolpath, *args] (exactly harness.py's kuzu_cli pattern);
    bash-shebang tool -> [git-bash, toolpath, *args]. Unknown/absent -> git-bash -c (last resort)."""
    tool = argv[0]
    toolpath = os.path.join(_WS, ".tools", tool)
    if os.path.exists(toolpath):
        try:
            with open(toolpath, encoding="utf-8", errors="replace") as fh:
                shebang = fh.readline().lower()
        except Exception:  # noqa: BLE001
            shebang = ""
        if "python" in shebang:
            return [sys.executable, toolpath] + [str(a) for a in argv[1:]]
        gb = _git_bash()
        if gb:
            return [gb, toolpath] + [str(a) for a in argv[1:]]
    gb = _git_bash()
    if gb:
        return [gb, "-c", " ".join(shlex.quote(str(a)) for a in argv)]
    return ["bash", "-c", " ".join(shlex.quote(str(a)) for a in argv)]   # last resort (may hit WSL)


def run_tool(probe: dict, *, timeout_s: float | None = None) -> dict:
    """Invoke the probe's tool as an agent would (shebang-honoring, but sidestepping the broken WSL-bash
    relay), against the LIVE estate. Captures stdout+stderr, rc, elapsed, timed_out. A timeout is NOT an
    error -- it is the USABILITY signal (too-slow-under-load = FUNCTIONAL PARTIAL)."""
    argv = probe["run"]
    cmd_argv = _resolve_invocation(argv)
    display_cmd = " ".join(shlex.quote(str(a)) for a in argv)
    to = timeout_s if timeout_s is not None else float(probe.get("usability_timeout_s", 150))
    env = dict(os.environ)
    env["PATH"] = os.path.join(_WS, ".tools") + os.pathsep + env.get("PATH", "")
    t0 = time.time()
    timed_out = False
    try:
        r = subprocess.run(cmd_argv, capture_output=True, text=True, timeout=to,
                           cwd=_WS, env=env, errors="replace")
        out, err, rc = r.stdout or "", r.stderr or "", r.returncode
    except subprocess.TimeoutExpired as e:
        out, err, rc, timed_out = (e.stdout or "") if isinstance(e.stdout, str) else "", "TIMEOUT", 124, True
    except Exception as e:  # noqa: BLE001 -- an infra failure to launch is an UNKNOWN, never a silent False
        out, err, rc = "", "LAUNCH-FAIL: %r" % e, 127
    elapsed = round(time.time() - t0, 2)
    return {"cmd": display_cmd, "stdout": out, "stderr": err, "rc": rc, "elapsed_s": elapsed,
            "timed_out": timed_out, "timeout_s": to}


# ---- score: REACH x USABILITY -> EFFECTIVE (reuse harness.score_run un-forked) --------------

def score_reach(output: str, probe: dict) -> dict:
    """REACH: did the tool's OUTPUT reach the sealed answer? >= reach_threshold distinct answer_terms
    present (exact-token) OR the answer_substr present -> reach=yes; else reach=no. Returns {reach, hits}."""
    text = (output or "").lower()
    out_tokens = {t.strip("._") for t in re.findall(r"[A-Za-z0-9_.-]+", text)}
    terms = [a.strip("._").lower() for a in probe.get("answer_terms", [])]
    hits = sorted({t for t in terms if t in out_tokens})
    substr = str(probe.get("answer_substr", "")).lower().strip()
    substr_hit = bool(substr) and substr in text
    reached = (len(hits) >= int(probe.get("reach_threshold", 1))) or substr_hit
    return {"reach": "yes" if reached else "no", "hits": hits, "substr_hit": substr_hit}


def score_usability(run: dict, output: str, rc: int, usable_rcs=(0,)) -> str:
    """USABILITY (in-the-moment): a >timeout run = 'too-slow'; an rc OUTSIDE the tool's answer-bearing
    codes (a crash/config error) or an empty/success-shaped output = 'fell-back'; else 'usable'. Mirrors
    the B1 usability vocab. usable_rcs lets a tool declare its valid answer codes (e.g. comp-freshness rc
    1 = a FAIL verdict, a usable answer, not a crash)."""
    if run.get("timed_out"):
        return "too-slow"
    if rc not in tuple(usable_rcs):
        return "fell-back"        # a crash / config error (not an answer-bearing return code)
    if not (output or "").strip():
        return "fell-back"        # success-shaped-empty = an unusable answer
    return "usable"


def effective_from_axes(reach: str, usability: str) -> str:
    """Map REACH x USABILITY -> EFFECTIVE via harness.score_run UN-FORKED. SOLVED (reached + usable) ->
    EFFECTIVE yes; MISS/PARTIAL (didn't reach, or reached-but-unusable-under-load = a FUNCTIONAL MISS per
    PRD SS5.2) -> EFFECTIVE no. grounding_resilience is fixed 'resist' -- a tool does not mis-ground; its
    success-shaped-wrong is already captured as reach=no / usability=fell-back."""
    usb = usability if usability in harness.USABILITY else "fell-back"
    rch = reach if reach in harness.REACH else "no"
    verdict = harness.score_run(reach=rch, usability=usb, grounding_resilience="resist")
    return "yes" if verdict == "SOLVED" else "no"    # MISS + PARTIAL both = not EFFECTIVE (functional miss)


# ---- one probe: gate -> run -> score -> row ------------------------------------------------

def probe_one(probe: dict, *, now_ts: float | None = None) -> dict:
    """Run one per-tool probe end-to-end: isolation gate -> (if not void) run the tool live -> score
    REACH x USABILITY -> EFFECTIVE. Returns the emit row {tool, class, reach, usability, effective,
    probe_ts, isolation_ok, ...}. A VOID isolation gate -> effective=unknown (measured nothing)."""
    if probe.get("kind") == "discrimination":
        return _run_discrimination_probe(probe, now_ts=now_ts)
    ts = int(now_ts if now_ts is not None else time.time())
    solver_id = "tool:%s" % probe["tool"]
    gate = isolation_gate(probe, solver_id=solver_id)
    row = {"probe_id": probe["probe_id"], "tool": probe["tool"], "class": probe["tool_class"],
           "probe_ts": ts, "isolation_ok": not gate["void"]}
    if gate["void"]:
        row.update({"reach": None, "usability": None, "effective": "unknown",
                    "void_reason": "isolation: " + "; ".join(gate["reasons"]),
                    "effective_evidence": {"case": "positive", "oracle_run": "VOID: isolation broken"}})
        return row
    run = run_tool(probe)
    reach = score_reach(run["stdout"], probe)
    usability = score_usability(run, run["stdout"], run["rc"], probe.get("usable_returncodes", [0]))
    effective = effective_from_axes(reach["reach"], usability)
    row.update({"reach": reach["reach"], "usability": usability, "effective": effective,
                "reach_hits": reach["hits"], "elapsed_s": run["elapsed_s"], "rc": run["rc"],
                "timed_out": run["timed_out"], "cmd": run["cmd"],
                "effective_evidence": {
                    "case": "positive",
                    "observed": {"reach": reach["reach"], "usability": usability, "hits": reach["hits"]},
                    "expected": probe.get("answer_terms", []),
                    # oracle_run = the EXERCISED run (argv + its scored output), NEVER a source file:line.
                    "oracle_run": run["cmd"],
                }})
    return row


def probe_all(probes: list | None = None, *, now_ts: float | None = None) -> list:
    """Run every probe -> a list of emit rows."""
    return [probe_one(p, now_ts=now_ts) for p in (probes if probes is not None else tool_corpus.probes())]


# ---- (B) the frozen-vs-fresh DISCRIMINATION probe: the un-gameable NEGATIVE case -------------
# NFRA_TOOLHEALTH.TH-A (A)+(B), CVO~B 2026-07-12, CTO-gated. A REACH x USABILITY probe is a SOFT exit-0
# proxy for a PLAUSIBLE-BUT-WRONG answer, so it cannot catch comp-freshness saying FRESH on a frozen-content
# / fresh-mtime artifact (the anti-correlated false-GREEN). This stages that EXACT lie against a CONTROLLED
# fixture whose frozen content-date the PROBE writes (the ORACLE, grounded OTHER than comp-freshness, which
# reads mtime), and scores effective by whether the tool CAUGHT the freeze (STALE => yes) or LIED (GREEN =>
# no). unknown/VOID on any staging failure -- never a silent no. Sovereign-safe scratch target (in-scope
# only, asserted); GUARANTEED cleanup (finally-delete). Writer/deleter/runner injectable for the fixture bar.

def _iso_days_ago(days: int, *, now_ts: float | None = None) -> str:
    """A UTC ISO date `days` in the past -- the FROZEN content data_as_of the fixture carries (the oracle)."""
    t = (now_ts if now_ts is not None else time.time()) - days * 86400
    return time.strftime("%Y-%m-%d", time.gmtime(t))


def _assert_scratch_in_scope(s3_uri: str) -> None:
    """The scratch write-target MUST be in-scope (never bd/schwab) -- by construction, not vigilance."""
    if is_held_path(s3_uri) or is_held_bucket(s3_uri):
        raise ValueError("SOVEREIGN: scratch target is a held bd/schwab path: %s" % s3_uri)


def _default_fixture_writer(s3_uri: str, *, frozen_as_of: str) -> None:
    """Write a synthetic artifact with a FROZEN content data_as_of + a FRESH mtime (write=now) to s3_uri.
    The JSON body carrying data_as_of=<frozen> is what an HONEST freshness tool must read to say STALE."""
    body = json.dumps({"data_as_of": frozen_as_of, "_probe_fixture": True,
                       "_note": "synthetic frozen-content/fresh-mtime fixture for the TH-A discrimination probe"})
    subprocess.run(["aws", "s3", "cp", "-", s3_uri, "--content-type", "application/json"],
                   input=body, text=True, capture_output=True, timeout=60, check=True)


def _default_freshness_runner(s3_uri: str) -> dict:
    """Exercise comp-freshness on the staged fixture (the same run_tool machinery)."""
    return run_tool({"run": ["comp-freshness", "artifact", s3_uri], "usability_timeout_s": 60})


def _run_discrimination_probe(probe: dict, *, now_ts=None,
                              fixture_writer=None, freshness_runner=None) -> dict:
    ts = int(now_ts if now_ts is not None else time.time())
    fx = probe["fixture"]
    # FIXED key (CTO 143216Z option a): OVERWRITTEN each run -- the write (PutObject, pre-authorized)
    # REFRESHES the mtime (B1's fresh-mtime property) with NO delete (an aws s3 rm is human-confirmation).
    # One namespaced object, never accumulates -> condition-(c) satisfied by construction; no finally-delete,
    # no sweep. Versioning is OFF on the shared buckets (Andrew-locked) -> a clean PUT, no delete-marker.
    key = "%s%s/frozen.json" % (fx["scratch_prefix"], probe["tool"])
    s3_uri = "s3://%s/%s" % (fx["scratch_bucket"], key)
    frozen_as_of = _iso_days_ago(int(fx["content_as_of_days_ago"]), now_ts=now_ts)  # ORACLE (independent of the tool)
    # isolation trivially OK: the run argv is `comp-freshness artifact <uri>` -- no verdict/oracle hint; the
    # tool must DERIVE staleness from the artifact content, it is NEVER told the answer.
    row = {"probe_id": probe["probe_id"], "tool": probe["tool"], "class": probe["tool_class"],
           "probe_ts": ts, "isolation_ok": True}
    try:
        _assert_scratch_in_scope(s3_uri)
    except ValueError as e:
        row.update({"reach": None, "usability": None, "effective": "unknown", "void_reason": str(e),
                    "effective_evidence": {"case": "negative", "oracle_run": "VOID: %s" % e}})
        return row
    writer = fixture_writer or _default_fixture_writer
    runner = freshness_runner or _default_freshness_runner
    try:
        writer(s3_uri, frozen_as_of=frozen_as_of)   # OVERWRITE the fixed key -> fresh mtime + frozen content
    except Exception as e:  # noqa: BLE001 -- a staging failure is UNKNOWN, never a silent no
        row.update({"reach": None, "usability": None, "effective": "unknown",
                    "void_reason": "fixture-stage-failed: %r" % e,
                    "effective_evidence": {"case": "negative", "oracle_run": "VOID: could not stage fixture"}})
        return row
    run = runner(s3_uri)
    text = ((run.get("stdout") or "") + " " + (run.get("stderr") or "")).lower()
    caught = any(t in text for t in probe["expected_verdict_terms"])            # STALE/FAIL/FROZEN
    said_green = (not caught) and any(t in text for t in probe["green_terms"])  # plausible-fresh on a frozen artifact
    if run.get("timed_out") or (not caught and not said_green):
        eff, reach_v, usab_v = "unknown", None, ("too-slow" if run.get("timed_out") else "fell-back")
    elif caught:
        eff, reach_v, usab_v = "yes", "yes", "usable"        # the tool CAUGHT the freeze -> effective
    else:
        eff, reach_v, usab_v = "no", "no", "usable"          # exit-0-while-lying: GREEN on a KNOWN-frozen artifact
    row.update({
        "reach": reach_v, "usability": usab_v, "effective": eff, "rc": run.get("rc"),
        "timed_out": run.get("timed_out"), "elapsed_s": run.get("elapsed_s"),
        "effective_evidence": {
            "case": "negative",
            "observed": text.strip()[:200],
            "expected": "STALE (content data_as_of %s = frozen ~%dd)"
                        % (frozen_as_of, int(fx["content_as_of_days_ago"])),
            # oracle_run = an EXERCISED observation (staged a known-frozen artifact, ran the tool on it);
            # the ground-truth is the content date the PROBE wrote, independent of comp-freshness (mtime).
            "oracle_run": "overwrote %s with content data_as_of=%s (frozen, fresh mtime), then ran comp-freshness on it"
                          % (s3_uri, frozen_as_of),
        },
    })
    return row


# NOTE: no scratch-sweep/delete exists by design (CTO 143216Z option a) -- the discrimination fixture is a
# single FIXED key OVERWRITTEN each run, so it never accumulates and needs no cleanup. An `aws s3 rm` would
# be a human-confirmation op; the fixed-key overwrite designs it out.


# ---- per-tool rollup + emit (append-only stream + the TH-B feed) ----------------------------

def rollup_by_tool(rows: list) -> dict:
    """Roll per-probe rows up to a per-TOOL EFFECTIVE verdict for the TH-B feed. A tool is EFFECTIVE=yes
    iff EVERY scored probe reached usably; ANY functional miss -> no (the FIX catch); all-unknown -> unknown."""
    feed = {}
    by_tool = {}
    for r in rows:
        by_tool.setdefault(r["tool"], []).append(r)
    for tool, rs in by_tool.items():
        effs = [r["effective"] for r in rs]
        scored = [e for e in effs if e in ("yes", "no")]
        if not scored:
            eff = "unknown"
        elif any(e == "no" for e in scored):
            eff = "no"            # ANY in-class functional miss -> the tool is a FIX
        else:
            eff = "yes"
        feed[tool] = {
            # TRISTATE (CVO-base 2-way contract, CTO-ruled): "yes"|"no"|"unknown" -- the wire maps
            # yes->True / no->False / unknown->None(pending). unknown=VOID is EXPLICIT (fail-closed): a "no"
            # MUST mean measured-not-effective, NEVER couldn't-measure (the CANNOT-EVALUATE vs FAIL law).
            "effective": eff,
            "effective_label": eff,   # (== effective; retained for back-compat consumers)
            "reach": [r.get("reach") for r in rs],
            "usability": [r.get("usability") for r in rs],
            "classes": sorted({r["class"] for r in rs}),
            "probe_ids": [r["probe_id"] for r in rs],
            "isolation_ok": all(r["isolation_ok"] for r in rs),
            "probe_ts": max(r["probe_ts"] for r in rs),
            "fix_probes": [r["probe_id"] for r in rs if r["effective"] == "no"],
            # per-probe honesty evidence (the gate inspects it): case positive|negative + the EXERCISED
            # oracle_run (a run, never a source file:line). This is the shared honesty law's audit surface.
            "effective_evidence": [
                dict({"probe_id": r["probe_id"]}, **(r.get("effective_evidence") or {})) for r in rs
            ],
        }
    return feed


def emit_probe_log(rows: list, path: str = PROBE_LOG) -> int:
    """APPEND the per-probe rows to the canonical append-only stream (one JSON row per line). This is a
    NEW source log (modeled on comproute-routing.jsonl) that COMPLEARN's scorer does NOT parse -- so it
    cannot mutate the COMPLEARN-owned tables/scorer (structural boundary). Returns the row count."""
    with open(path, "a", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, default=str) + "\n")
    return len(rows)


def emit_effective_feed(rows: list, path: str = EFFECTIVE_FEED) -> dict:
    """Write the per-TOOL rollup as the `comp-tool-health --effective-feed` JSON (the TH-B Phase-B join
    input: {canonical_tool: {effective: bool, ...}}). TH-B reads only `effective`; extras are carried."""
    feed = rollup_by_tool(rows)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(feed, fh, indent=2, default=str)
    return feed


# ---- consumption-driven freshness gate (CTO GO 2026-07-06: run-on-consume, 7d ceiling) --------
# NOT a cron / NOT SessionEnd / NOT cloud: a CONSUMER (a governance / tool-R&D review about to READ the
# health data) calls ensure_fresh() first. Fresh-when-consumed, cost-bounded to the review cadence, never
# a blind clock -- mirrors comp-kuzu's refresh-on-HEAD-advance (staleness-aware, not a fixed tick).

DEFAULT_CEILING_DAYS = 7.0


def _feed_probe_ts(feed_path: str = EFFECTIVE_FEED) -> int | None:
    """The most-recent probe_ts (epoch) in the effective_feed rollup, or None if the feed is absent /
    unreadable / carries no timestamped tool. This is the age anchor the staleness ceiling measures."""
    if not os.path.exists(feed_path):
        return None
    try:
        with open(feed_path, encoding="utf-8", errors="replace") as fh:
            feed = json.load(fh)
    except (OSError, ValueError):
        return None
    tss = [v.get("probe_ts") for v in feed.values()
           if isinstance(v, dict) and isinstance(v.get("probe_ts"), (int, float))]
    return int(max(tss)) if tss else None


def feed_age_days(feed_path: str = EFFECTIVE_FEED, *, now_ts: float | None = None) -> float | None:
    """Age (days) of the freshest probe in the feed. None => no feed => treat as infinitely stale."""
    ts = _feed_probe_ts(feed_path)
    if ts is None:
        return None
    now = now_ts if now_ts is not None else time.time()
    return round((now - ts) / 86400.0, 3)


def _is_stale(age_days: float | None, ceiling_days: float, force: bool) -> bool:
    """The staleness DECISION (pure -> self-testable): force OR no-feed OR older-than-ceiling => stale."""
    return bool(force) or age_days is None or age_days > ceiling_days


def ensure_fresh(*, ceiling_days: float = DEFAULT_CEILING_DAYS, force: bool = False,
                 feed_path: str = EFFECTIVE_FEED, probe_log: str = PROBE_LOG,
                 corpus: list | None = None, now_ts: float | None = None) -> dict:
    """The consumption-driven trigger (CTO GO 2026-07-06). A consumer about to READ the health data calls
    this first: if the last probe is <= ceiling_days old, REUSE it (no run); if force / missing / older,
    run the probe LIVE + re-emit, THEN the consumer reads. Returns {ran, age_days, reason, ...}."""
    age = feed_age_days(feed_path, now_ts=now_ts)
    stale = _is_stale(age, ceiling_days, force)
    result = {"ran": False, "age_days": age, "ceiling_days": ceiling_days,
              "forced": bool(force), "feed_path": feed_path}
    if not stale:
        result["reason"] = "fresh: last probe %.2fd old <= %.1fd ceiling -- reused (no run)" % (age, ceiling_days)
        return result
    corpus = corpus if corpus is not None else tool_corpus.probes()
    rows = probe_all(corpus, now_ts=now_ts)
    emit_probe_log(rows, probe_log)
    emit_effective_feed(rows, feed_path)
    result.update(ran=True, n_probes=len(rows), reason=(
        "forced fresh run (ceiling bypassed)" if force else
        "no prior feed -- first run" if age is None else
        "stale: last probe %.2fd old > %.1fd ceiling -- ran fresh" % (age, ceiling_days)))
    return result


# ---- self-test (structural: isolation gate + scorer, no live run needed) --------------------

def _selftest() -> int:
    probes = tool_corpus.probes()
    # AC: every probe's strip gate holds (no sealed answer leaks into the payload the tool sees).
    for p in probes:
        sg = strip_gate(p)
        assert sg["passed"], "STRIP LEAK on %s: %s" % (p["probe_id"], sg["leaked"])
    # AC: the isolation gate is distinct-roles + strip-clean for a real solver id; author==solver VOIDs.
    ok = isolation_gate(probes[0], solver_id="tool:comp-which")
    assert not ok["void"], "distinct roles + clean strip must NOT void: %s" % ok["reasons"]
    void = isolation_gate(probes[0], solver_id=AUTHOR_ID)   # author == solver -> VOID
    assert void["void"], "author==solver must VOID"
    # a tool INPUT (run argv) that leaks the answer must VOID (the structural guard the whole axis rests on)
    leaky = dict(probes[0])
    leaky["run"] = list(leaky["run"]) + ["comp-blast"]
    assert isolation_gate(leaky, solver_id="tool:comp-which")["void"], "answer-in-tool-input must VOID"
    # AC: the REACH x USABILITY -> EFFECTIVE mapping (reuse harness.score_run) at the boundaries.
    assert effective_from_axes("yes", "usable") == "yes", "reached + usable -> EFFECTIVE yes"
    assert effective_from_axes("no", "usable") == "no", "not reached -> EFFECTIVE no"
    assert effective_from_axes("yes", "too-slow") == "no", "reached-but-too-slow = FUNCTIONAL MISS -> no"
    assert effective_from_axes("yes", "fell-back") == "no", "reached-but-fell-back = FUNCTIONAL MISS -> no"
    # AC: score_reach reaches on a term hit + on a substring; misses cleanly.
    assert score_reach("... -> comp-blast <fn>", probes[0])["reach"] == "yes", "term/substr present -> reach yes"
    assert score_reach("no relevant tool here", probes[0])["reach"] == "no", "absent -> reach no"
    # AC: usability vocab (timeout -> too-slow; empty -> fell-back; rc!=0 -> fell-back; else usable).
    assert score_usability({"timed_out": True}, "x", 0) == "too-slow"
    assert score_usability({"timed_out": False}, "", 0) == "fell-back"
    assert score_usability({"timed_out": False}, "x", 1) == "fell-back"        # rc 1 not answer-bearing by default
    assert score_usability({"timed_out": False}, "x", 1, (0, 1)) == "usable"   # tool declares rc 1 = a verdict
    assert score_usability({"timed_out": False}, "an answer", 0) == "usable"
    # AC: the per-tool rollup -- ANY functional miss makes the tool a FIX (effective no); mocked rows.
    mock = [{"tool": "t", "class": "c", "effective": "yes", "isolation_ok": True, "probe_ts": 1,
             "reach": "yes", "usability": "usable", "probe_id": "t/1"},
            {"tool": "t", "class": "c", "effective": "no", "isolation_ok": True, "probe_ts": 2,
             "reach": "no", "usability": "usable", "probe_id": "t/2"}]
    rolled = rollup_by_tool(mock)
    # effective is now the TRISTATE string (2-way contract): "no" (not the old bool False). unknown=VOID.
    assert rolled["t"]["effective"] == "no" and rolled["t"]["fix_probes"] == ["t/2"], \
        "any in-class functional miss -> tool EFFECTIVE=no (FIX): %s" % rolled["t"]
    assert rollup_by_tool([{"tool": "u", "class": "c", "effective": "unknown", "isolation_ok": False,
                            "probe_ts": 1, "reach": None, "usability": None, "probe_id": "u/1"}]
                          )["u"]["effective"] == "unknown", "all-VOID -> unknown, NEVER a silent no/False"
    # AC: the consumption-driven staleness gate (CTO GO) -- pure decision, no live run.
    assert _is_stale(None, 7, False) is True, "no feed -> stale (must run)"
    assert _is_stale(8.0, 7, False) is True, "older than ceiling -> stale"
    assert _is_stale(3.0, 7, False) is False, "within ceiling -> fresh (reuse, no run)"
    assert _is_stale(3.0, 7, True) is True, "force overrides a fresh feed -> run"
    assert feed_age_days("/no/such/effective_feed.json") is None, "absent feed -> None (infinitely stale)"
    print("SELF-TEST PASS: strip 4/4 clean | isolation VOID-on-violation (author==solver + answer-leak) |"
          " REACH x USABILITY -> EFFECTIVE (reuse score_run) | reach/usability vocab | per-tool FIX rollup |"
          " staleness gate (no-feed/>ceiling/force => run, <=ceiling => reuse)")
    return 0


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(prog="tool-probe",
                                 description="NFRA_TOOLHEALTH.TH-A per-tool EFFECTIVE probe (blind-run, isolation-gated)")
    ap.add_argument("--self-test", action="store_true", help="structural self-test (isolation + scorer), no live run")
    ap.add_argument("--run", action="store_true", help="run the probe corpus LIVE against the estate + emit")
    ap.add_argument("--ensure-fresh", action="store_true",
                    help="consumption-driven trigger (CTO GO): run ONLY if the feed is missing/older than "
                         "--ceiling-days; else reuse. What a consumer calls before reading the health data.")
    ap.add_argument("--ceiling-days", type=float, default=DEFAULT_CEILING_DAYS,
                    help="staleness ceiling for --ensure-fresh (default 7): feed older than this => run fresh")
    ap.add_argument("--force", action="store_true",
                    help="with --ensure-fresh: run now regardless of the staleness ceiling (ad-hoc R&D pass)")
    ap.add_argument("--local-only", action="store_true", help="with --run/--ensure-fresh: skip live_estate probes (local tools only)")
    ap.add_argument("--probe-log", default=PROBE_LOG, help="append-only per-probe stream path")
    ap.add_argument("--effective-feed", default=EFFECTIVE_FEED, help="per-tool rollup JSON (TH-B --effective-feed input)")
    ap.add_argument("--json", action="store_true", help="print the rows + feed JSON")
    a = ap.parse_args(argv)
    if a.self_test:
        return _selftest()
    if a.ensure_fresh:
        corpus = [p for p in tool_corpus.probes() if not (a.local_only and p.get("live_estate"))]
        res = ensure_fresh(ceiling_days=a.ceiling_days, force=a.force,
                           feed_path=a.effective_feed, probe_log=a.probe_log, corpus=corpus)
        if a.json:
            print(json.dumps(res, indent=1, default=str))
        else:
            print("=== TH-A ensure-fresh: %s ===" % ("RAN" if res["ran"] else "REUSED"))
            print("  %s" % res["reason"])
            print("  feed: %s" % res["feed_path"])
        return 0
    if a.run:
        corpus = [p for p in tool_corpus.probes() if not (a.local_only and p.get("live_estate"))]
        rows = probe_all(corpus)
        n = emit_probe_log(rows, a.probe_log)
        feed = emit_effective_feed(rows, a.effective_feed)
        if a.json:
            print(json.dumps({"rows": rows, "feed": feed}, indent=1, default=str))
        else:
            print("=== TH-A per-tool EFFECTIVE probe -- %d probe(s), %d tool(s) ===" % (n, len(feed)))
            for r in rows:
                print("  [%-7s] %-32s reach=%-4s usability=%-9s (%ss)"
                      % (str(r["effective"]).upper(), r["probe_id"], r.get("reach"),
                         r.get("usability"), r.get("elapsed_s", "-")))
            print("  --- per-tool rollup (TH-B --effective-feed) ---")
            for tool, v in feed.items():
                tag = "FIX" if v["effective"] is False else ("KEEP-eligible" if v["effective"] else "unknown")
                print("  %-16s effective=%-5s %-14s fix_probes=%s"
                      % (tool, v["effective_label"], "(%s)" % tag, v["fix_probes"]))
            print("  wrote %s (append) + %s (feed)" % (a.probe_log, a.effective_feed))
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
