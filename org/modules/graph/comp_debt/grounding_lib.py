#!/usr/bin/env python3
"""grounding_lib -- the SHARED Rule-22 dual-evidence dead-confirm for comp-debt.

MILESTONE 1 (NFRA_COMPDEBT_PRD.md 8.1 / 2). This library LIFTS the dual-evidence
dead-confirm that already lived (DynamoDB-specific) inside
`org/modules/graph/debtscan/dup_scan.py` (graph_dead_confirm / metric_reads_sum /
windowed_dead_verdict / dead_prior) into a shared, GENERALIZED library that EVERY
comp-debt signal uses. It is the one place the Rule-22 discipline is encoded, so no
signal re-implements it and no signal can drift from it.

THE CORE INVARIANT (Rule 22, two-layer):
  A signal is a SYMPTOM = INFERRED, non-actionable. Promotion to a reserved word
  ("dead"/"unused"/"provably") REQUIRES a live/source confirm leg. The dual-evidence
  dead-confirm encodes exactly this: a resource is only CONFIRMED dead when BOTH
    (leg 1) the graph shows zero consumers   [the DESIRED/structural layer], AND
    (leg 2) a live metric shows zero activity over a window >= the longest plausible
            access cadence                    [the APPLIED/live layer].
  Either leg alone => INFERRED (never CONFIRMED). The verdict STRING carries the
  window, so a human adjudicating a removal-worklist sees exactly what "dead" rests on.

VINTAGE-CARRY (PRD 6): the graph leg is only as trustworthy as the graph it read.
A BEHIND / UNKNOWN-VINTAGE graph cannot support a CONFIRMED graph leg -> the fused
verdict degrades to UNVERIFIABLE, never clean.

This module makes ZERO decisions and NEVER acts. It computes grounded verdicts only.

Generalization notes vs the dup_scan original:
  - metric leg is now ANY CloudWatch metric (namespace/metric/dimensions/statistic),
    not just DynamoDB ConsumedReadCapacityUnits -- so cloudtrail.py (Lambda
    Invocations) and usage/tf_drift signals share the exact same combinator.
  - graph leg models four states (ZERO_CONSUMER / ZERO_PENDING / REACHABLE / UNKNOWN)
    so the combinator is explicit about "confirmed-zero" vs "dead-prior-but-unqueried".
  - a back-compat `windowed_dead_verdict()` shim preserves dup_scan's exact output
    strings, so dup_scan can later delegate here with zero behavior change.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]

# ---- comp-tool invocation (Windows-safe) --------------------------------------------------
# .tools/comp-* are extensionless bash scripts. A bare subprocess(["comp-blast", ...]) fails
# on Windows (CreateProcess can't launch a shebang script) and silently falls back -- so the
# graph/vintage legs would go permanently dark. Resolve the REAL Git Bash (NOT the WSL relay)
# and dispatch each tool by its shebang, mirroring org/modules/graph/drift_cli.py's pattern.
_BASH_EXE = (os.environ.get("COMP_DRIFT_BASH") or shutil.which("bash") or "bash")
_PYTHON_EXE = (sys.executable or shutil.which("python3") or shutil.which("python") or "python")


def _comp_cmd(tool: str) -> list[str]:
    """Return the argv prefix to invoke a .tools/<tool> script, chosen by its shebang."""
    tool_path = REPO / ".tools" / tool
    interp = _PYTHON_EXE
    try:
        first = tool_path.read_text(encoding="utf-8", errors="replace").splitlines()[:1]
        interp = _PYTHON_EXE if (first and "python" in first[0]) else _BASH_EXE
    except OSError:
        interp = _BASH_EXE
    return [interp, str(tool_path)]


# ---- levels + reserved-word guard (Rule 22) ----------------------------------------------
LEVEL_INFERRED = "INFERRED"   # a symptom; non-actionable on its own
LEVEL_CONFIRMED = "CONFIRMED"  # a live/source-confirmed leg; may contribute to a DEBT verdict
LEVEL_UNVERIFIABLE = "UNVERIFIABLE"  # could-not-verify (e.g. stale graph) -- a finding, never clean

# Reserved words are legal ONLY on a source/live-CONFIRMED claim (CLAUDE.md Rule 22).
RESERVED_WORDS = frozenset({"dead", "unused", "provably", "proof", "root cause", "definitively"})


def reserved_word_legal(level: str) -> bool:
    """A reserved word ('dead'/'provably'/...) is legal only on a CONFIRMED claim."""
    return level == LEVEL_CONFIRMED


# ---- graph leg: zero-consumer confirm (leg 1, the DESIRED/structural layer) ---------------
# A dead-prior path (deprecated//archive/...) RAISES the dead-prior but is never CONFIRMED
# on its own -- the graph reachability check is what promotes it.
_DEAD_PRIOR_RE = re.compile(r"(^|/)(deprecated|archive|archived|old|legacy|_attic|graveyard)(/|$)", re.I)

GRAPH_ZERO_CONSUMER = "ZERO_CONSUMER"   # comp-blast confirmed: 0 downstream consumers
GRAPH_ZERO_PENDING = "ZERO_PENDING"     # dead-prior path, but graph NOT conclusively queried
GRAPH_REACHABLE = "REACHABLE"           # graph shows >=1 consumer
GRAPH_UNKNOWN = "UNKNOWN"               # no dead-prior + no usable graph signal


def dead_prior(path: str) -> bool:
    """True if the path itself signals deprecation (deprecated//archive/old/legacy/...)."""
    return bool(_DEAD_PRIOR_RE.search(path or ""))


@dataclass
class GraphLeg:
    status: str                 # one of GRAPH_*
    grounding: str              # human-readable cite (resource id + what the graph said)
    raw: str = ""               # trimmed tool output, for audit

    @property
    def is_zero(self) -> bool:
        """0-or-pending consumers (either warrants pairing with a live metric leg)."""
        return self.status in (GRAPH_ZERO_CONSUMER, GRAPH_ZERO_PENDING)

    @property
    def is_confirmed_zero(self) -> bool:
        return self.status == GRAPH_ZERO_CONSUMER


_GRAPH_CACHE: dict[str, GraphLeg] = {}


def graph_zero_consumer(resource_id: str, path: str = "", *, timeout: int = 30,
                        repo: Path = REPO) -> GraphLeg:
    """Graph reachability leg via `comp-blast <node> --check-consumers`.

    Uses comp-blast's purpose-built consumer-check contract (not blast-radius text):
      rc 0 / CONSUMER-OK      -> GRAPH_REACHABLE   (>=1 downstream consumer)
      rc 1 / PHANTOM-CONSUMER -> GRAPH_ZERO_CONSUMER (zero EXTRACTED downstream edges)
      rc 3 / NOT-FOUND        -> GRAPH_UNKNOWN     (typo/missing node -- NEVER a false clear)
      timeout/error           -> GRAPH_ZERO_PENDING if the path is dead-prior, else UNKNOWN

    NOTE (Rule 22, echoed by comp-blast itself): a PHANTOM-CONSUMER "zero" means "no
    extracted edge", NOT "provably no consumer" -- a dynamic/FUNC-key consumer is invisible
    to the graph. That is why this is only leg 1 (structural/INFERRED): graph.py layers the
    14-class FP-suppression overlay, and the dual-evidence combinator requires the live
    metric leg before anything is CONFIRMED. Cached per resource_id.
    """
    if resource_id in _GRAPH_CACHE:
        return _GRAPH_CACHE[resource_id]
    prior = dead_prior(path)
    status = GRAPH_ZERO_PENDING if prior else GRAPH_UNKNOWN
    raw = ""
    try:
        r = subprocess.run(
            _comp_cmd("comp-blast") + [resource_id, "--check-consumers"],
            cwd=str(repo), capture_output=True, text=True, timeout=timeout,
        )
        out = (r.stdout or "") + (r.stderr or "")
        raw = out.strip()[:400]
        up = out.upper()
        if "CONSUMER-OK" in up or r.returncode == 0:
            status = GRAPH_REACHABLE
        elif "PHANTOM-CONSUMER" in up or r.returncode == 1:
            status = GRAPH_ZERO_CONSUMER
        elif "NOT-FOUND" in up or r.returncode == 3:
            status = GRAPH_ZERO_PENDING if prior else GRAPH_UNKNOWN
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError):
        pass  # no usable graph result -> keep the honest fallback (never CONFIRMED)
    leg = GraphLeg(status=status, raw=raw,
                   grounding=f"comp-blast {resource_id} --check-consumers -> {status}"
                             + (f"; dead-prior path {path}" if prior else ""))
    _GRAPH_CACHE[resource_id] = leg
    return leg


# ---- vintage: how trustworthy is the graph we read? (PRD 6 vintage-carry) -----------------
VINTAGE_CURRENT = "CURRENT"
VINTAGE_BEHIND = "BEHIND"
VINTAGE_UNKNOWN = "UNKNOWN"


@dataclass
class Vintage:
    status: str                 # VINTAGE_*
    built_iso: str = ""
    age_hours: float | None = None
    raw: str = ""

    @property
    def trustworthy(self) -> bool:
        """A CURRENT (self-healed) graph is trustworthy; BEHIND/UNKNOWN is not."""
        return self.status == VINTAGE_CURRENT


_VINTAGE_CACHE: dict[str, Vintage] = {}
# comp-kuzu provenance header lines (captured 2026-07-02):
#   built: 2026-07-02T22:13:21.006295+00:00 (age: 0.0h)
#   Nessie HEAD: current (pin == marker HEAD)
_VINTAGE_HEAD_RE = re.compile(r"Nessie HEAD:\s*(current|behind|unknown)", re.I)
_VINTAGE_BUILT_RE = re.compile(r"built:\s*(\S+)\s*\(age:\s*([0-9.]+)h\)", re.I)


def read_graph_vintage(*, timeout: int = 90, repo: Path = REPO) -> Vintage:
    """Read the comp-kuzu provenance header and classify the graph vintage.

    comp-kuzu auto-refreshes on HEAD-advance, so a healthy call reads 'current'. If the
    header is unreadable, we fail to UNKNOWN (treat as a signal, never clean). Cached for
    the process lifetime (one graph vintage per run).
    """
    if "v" in _VINTAGE_CACHE:
        return _VINTAGE_CACHE["v"]
    status, built, age, raw = VINTAGE_UNKNOWN, "", None, ""
    try:
        r = subprocess.run(
            _comp_cmd("comp-kuzu") + ["MATCH (n) RETURN count(n) AS n LIMIT 1"],
            cwd=str(repo), capture_output=True, text=True, timeout=timeout,
        )
        out = (r.stdout or "") + (r.stderr or "")
        raw = out
        mh = _VINTAGE_HEAD_RE.search(out)
        if mh:
            token = mh.group(1).lower()
            status = {"current": VINTAGE_CURRENT, "behind": VINTAGE_BEHIND,
                      "unknown": VINTAGE_UNKNOWN}.get(token, VINTAGE_UNKNOWN)
        mb = _VINTAGE_BUILT_RE.search(out)
        if mb:
            built, age = mb.group(1), float(mb.group(2))
    except (FileNotFoundError, subprocess.TimeoutExpired, OSError, ValueError):
        pass
    v = Vintage(status=status, built_iso=built, age_hours=age, raw=raw[:400])
    _VINTAGE_CACHE["v"] = v
    return v


# ---- metric leg: zero-activity over a window (leg 2, the APPLIED/live layer) --------------
_AWS = shutil.which("aws.cmd") or shutil.which("aws") or os.path.expanduser(
    "~/AppData/Local/Programs/Python/Python312/Scripts/aws.cmd")

# Default window >= the longest plausible low-frequency access cadence. A 24h window would
# FALSE-CONFIRM a weekly/monthly-read resource (a billing job, a monthly report). CTO cond-1.
DEFAULT_WINDOW_DAYS = 30

METRIC_ZERO = "ZERO"        # queried, datapoints present, all zero over the window
METRIC_NONZERO = "NONZERO"  # queried, >0 activity
METRIC_PENDING = "PENDING"  # no usable metric result (error / no datapoints)


@dataclass
class MetricLeg:
    status: str                 # METRIC_*
    value: float | None         # summed statistic over the window (None on error)
    npts: int                   # number of datapoints returned
    window_days: int
    label: str                  # e.g. "reads", "invocations", "events"
    grounding: str = ""

    @property
    def is_zero(self) -> bool:
        return self.status == METRIC_ZERO


def _fmt_dims(dimensions: list[tuple[str, str]] | dict[str, str]) -> list[str]:
    if isinstance(dimensions, dict):
        items = list(dimensions.items())
    else:
        items = list(dimensions)
    return [f"Name={n},Value={v}" for n, v in items]


def metric_zero_over_window(namespace: str, metric_name: str,
                            dimensions: list[tuple[str, str]] | dict[str, str], *,
                            window_days: int = DEFAULT_WINDOW_DAYS,
                            statistic: str = "Sum", label: str = "events",
                            now: str | None = None, aws: str | None = None,
                            timeout: int = 60) -> MetricLeg:
    """Generalized CloudWatch 'zero-activity over a window' leg.

    Sums `statistic` of the metric over [now-window, now] as a SINGLE bucket (period =
    window*86400). Read-only operational metric query -- there is no graph edge over a
    CloudWatch datapoint, so raw aws is the correct primitive here (CLAUDE.md compiler-tools
    graph-presence principle). Returns a MetricLeg; ZERO requires datapoints present AND
    sum == 0 (npts==0 is PENDING, never a false-confirm).
    """
    aws = aws or _AWS
    end = (dt.datetime.strptime(now, "%Y-%m-%dT%H:%M:%S") if now
           else dt.datetime.now(dt.timezone.utc).replace(tzinfo=None))
    start = end - dt.timedelta(days=window_days)
    value: float | None = None
    npts = 0
    try:
        args = [aws, "cloudwatch", "get-metric-statistics",
                "--namespace", namespace, "--metric-name", metric_name]
        for d in _fmt_dims(dimensions):
            args += ["--dimensions", d]
        args += ["--start-time", start.strftime("%Y-%m-%dT%H:%M:%S"),
                 "--end-time", end.strftime("%Y-%m-%dT%H:%M:%S"),
                 "--period", str(max(window_days, 1) * 86400),
                 "--statistics", statistic, "--output", "json"]
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        if r.returncode == 0:
            pts = json.loads(r.stdout).get("Datapoints", [])
            npts = len(pts)
            value = sum(p.get(statistic, 0) for p in pts)
    except (OSError, subprocess.TimeoutExpired, ValueError):
        value, npts = None, 0
    if value is not None and npts > 0:
        status = METRIC_ZERO if value == 0 else METRIC_NONZERO
    else:
        status = METRIC_PENDING
    dim_s = ",".join(_fmt_dims(dimensions))
    return MetricLeg(status=status, value=value, npts=npts, window_days=window_days,
                     label=label,
                     grounding=f"CW {namespace}/{metric_name}[{dim_s}] {statistic}"
                               f"={value} pts={npts}/{window_days}d")


# ---- the fused dual-evidence dead-confirm (the lifted core) -------------------------------
@dataclass
class DeadConfirm:
    """The Rule-22 dual-evidence verdict. `verdict` is the human string (carries the
    window); `level` is INFERRED / CONFIRMED / UNVERIFIABLE / REACHABLE. `grounding`
    carries desired(graph) + applied(metric) cites so a signal object can quote it."""
    verdict: str
    level: str
    window_days: int
    graph: GraphLeg
    metric: MetricLeg
    grounding: dict = field(default_factory=dict)

    @property
    def is_confirmed_dead(self) -> bool:
        return self.level == LEVEL_CONFIRMED

    def to_dict(self) -> dict:
        return {"verdict": self.verdict, "level": self.level,
                "window_days": self.window_days, "grounding": self.grounding}


def dual_evidence_verdict(graph: GraphLeg, metric: MetricLeg, *,
                          vintage: Vintage | None = None) -> DeadConfirm:
    """Fuse the graph leg + the metric leg into a Rule-22 dead-confirm.

    CONFIRMED_DEAD  <- graph confirmed-zero-consumer AND metric zero over the window
                       AND the graph vintage is trustworthy (current).
    INFERRED_DEAD   <- exactly one leg fires (the other pending), OR the metric fires but
                       the graph is only dead-prior (ZERO_PENDING), OR graph-zero but the
                       metric is pending.
    UNVERIFIABLE    <- both legs would say dead but the graph vintage is BEHIND/UNKNOWN
                       (we cannot trust the structural leg) -- a finding, never clean.
    REACHABLE       <- the metric shows activity (live use contradicts dead).
    UNKNOWN         <- no dead-prior + no signal either way.

    Either leg ALONE never yields CONFIRMED (Rule 22). The window is in the string.
    """
    w = metric.window_days
    lbl = metric.label
    grounding = {"desired": graph.grounding, "applied": metric.grounding}
    if vintage is not None:
        grounding["vintage"] = f"graph vintage={vintage.status}" + (
            f" (age {vintage.age_hours}h)" if vintage.age_hours is not None else "")

    metric_dead = metric.is_zero
    graph_confirmed_zero = graph.is_confirmed_zero
    graph_zero = graph.is_zero
    vintage_ok = (vintage is None) or vintage.trustworthy

    # Both legs dead, but a BEHIND/UNKNOWN graph cannot support CONFIRMED -> UNVERIFIABLE.
    if graph_confirmed_zero and metric_dead and not vintage_ok:
        return DeadConfirm(
            verdict=f"UNVERIFIABLE (0 {lbl}/{w}d, 0 graph-consumers but graph vintage "
                    f"{vintage.status if vintage else 'UNKNOWN'})",
            level=LEVEL_UNVERIFIABLE, window_days=w, graph=graph, metric=metric,
            grounding=grounding)

    if graph_confirmed_zero and metric_dead:
        return DeadConfirm(
            verdict=f"CONFIRMED_DEAD (0 {lbl}/{w}d, 0 graph-consumers)",
            level=LEVEL_CONFIRMED, window_days=w, graph=graph, metric=metric,
            grounding=grounding)

    if metric_dead and graph_zero:  # metric confirmed, graph only dead-prior (pending)
        return DeadConfirm(
            verdict=f"INFERRED_DEAD (0 {lbl}/{w}d; graph-consumers PENDING)",
            level=LEVEL_INFERRED, window_days=w, graph=graph, metric=metric,
            grounding=grounding)

    if metric_dead:  # metric confirmed, graph reachable-or-unknown
        return DeadConfirm(
            verdict=f"INFERRED_DEAD (0 {lbl}/{w}d; graph REACHABLE-or-unknown)",
            level=LEVEL_INFERRED, window_days=w, graph=graph, metric=metric,
            grounding=grounding)

    if metric.status == METRIC_PENDING:  # no metric -> lean on the graph leg only
        if graph_zero:
            return DeadConfirm(
                verdict=f"INFERRED_DEAD (metric-pending; graph {graph.status})",
                level=LEVEL_INFERRED, window_days=w, graph=graph, metric=metric,
                grounding=grounding)
        return DeadConfirm(verdict="UNKNOWN", level=LEVEL_INFERRED, window_days=w,
                           graph=graph, metric=metric, grounding=grounding)

    # metric shows activity -> live use contradicts dead
    val = metric.value if metric.value is not None else 0
    return DeadConfirm(verdict=f"REACHABLE ({val:.0f} {lbl}/{w}d)",
                       level=LEVEL_INFERRED, window_days=w, graph=graph, metric=metric,
                       grounding=grounding)


# ---- shared Signal object (the vocabulary EVERY signal + fuse.py speaks) ------------------
@dataclass
class Signal:
    """One signal's contribution to a resource's debt verdict (PRD 4 schema).

    `level` is INFERRED (symptom only) or CONFIRMED (has a live/source confirm leg).
    Only CONFIRMED signals may contribute to a DEBT-DECOMMISSION verdict (>=2 required;
    fuse.py enforces the AC2 bar)."""
    signal: str                 # graph|duplicates|tf_drift|cloudtrail|git_heat|usage
    state: str                  # signal-specific state (orphan|cold|dead|duplicate|...)
    grounding: dict             # {desired:..., applied/exercised:...}
    level: str = LEVEL_INFERRED

    def to_dict(self) -> dict:
        return {"signal": self.signal, "state": self.state,
                "grounding": self.grounding, "level": self.level}


def signal_from_dead_confirm(signal_name: str, state: str, dc: DeadConfirm) -> Signal:
    """Build a Signal from a dual-evidence DeadConfirm (level flows straight through:
    CONFIRMED only when both legs fired on a trustworthy graph)."""
    level = LEVEL_CONFIRMED if dc.is_confirmed_dead else (
        LEVEL_UNVERIFIABLE if dc.level == LEVEL_UNVERIFIABLE else LEVEL_INFERRED)
    return Signal(signal=signal_name, state=state,
                  grounding={**dc.grounding, "verdict": dc.verdict}, level=level)


# ---- back-compat shim: preserve dup_scan's EXACT output strings ----------------------------
# dup_scan.py can delegate its dual-evidence functions here with ZERO behavior change.
# (Kept faithful to dup_scan.windowed_dead_verdict so a future re-wire is a provable no-op.)
_LEGACY_GRAPH_MAP = {
    "CONFIRMED_DEAD": GraphLeg(GRAPH_ZERO_CONSUMER, "legacy: CONFIRMED_DEAD"),
    "INFERRED_DEAD_GRAPH_PENDING": GraphLeg(GRAPH_ZERO_PENDING, "legacy: dead-prior pending"),
    "REACHABLE": GraphLeg(GRAPH_REACHABLE, "legacy: REACHABLE"),
    "UNKNOWN": GraphLeg(GRAPH_UNKNOWN, "legacy: UNKNOWN"),
}


def windowed_dead_verdict_ddb(graph_status: str, table: str,
                              window_days: int = DEFAULT_WINDOW_DAYS,
                              now: str | None = None) -> str:
    """Back-compat: reproduce dup_scan.windowed_dead_verdict for a DynamoDB table using
    the generalized combinator. Returns the SAME string dup_scan emitted (reads label)."""
    metric = metric_zero_over_window(
        "AWS/DynamoDB", "ConsumedReadCapacityUnits", [("TableName", table)],
        window_days=window_days, statistic="Sum", label="reads", now=now)
    graph = _LEGACY_GRAPH_MAP.get(graph_status, GraphLeg(GRAPH_UNKNOWN, "legacy: UNKNOWN"))
    dc = dual_evidence_verdict(graph, metric)
    # map the generalized "metric-pending"/"UNKNOWN" wording back to the legacy strings
    if metric.status == METRIC_PENDING:
        return "INFERRED_DEAD (metric-pending)" if graph.is_zero else "UNKNOWN"
    return dc.verdict


# ---- self-test (deterministic, no live AWS) -----------------------------------------------
def _self_test() -> int:
    """Pure-function fixtures for the combinator -- no network. Proves the Rule-22 truth
    table: only both-legs-on-a-trusted-graph yields CONFIRMED; every single-leg case is
    INFERRED; a stale graph degrades to UNVERIFIABLE; activity is REACHABLE."""
    def mk_graph(s):
        return GraphLeg(s, f"test:{s}")

    def mk_metric(status, value, npts=1, w=30, label="events"):
        return MetricLeg(status, value, npts, w, label, grounding=f"test:{status}")

    cur = Vintage(VINTAGE_CURRENT, "2026-07-02T22:00:00", 0.0)
    behind = Vintage(VINTAGE_BEHIND, "2026-06-01T00:00:00", 720.0)
    cases = []

    # 1. both legs dead + trusted graph -> CONFIRMED
    dc = dual_evidence_verdict(mk_graph(GRAPH_ZERO_CONSUMER), mk_metric(METRIC_ZERO, 0), vintage=cur)
    cases.append(("both-dead+current => CONFIRMED", dc.level == LEVEL_CONFIRMED and "CONFIRMED_DEAD" in dc.verdict))

    # 2. both legs dead but BEHIND graph -> UNVERIFIABLE (never clean)
    dc = dual_evidence_verdict(mk_graph(GRAPH_ZERO_CONSUMER), mk_metric(METRIC_ZERO, 0), vintage=behind)
    cases.append(("both-dead+behind => UNVERIFIABLE", dc.level == LEVEL_UNVERIFIABLE))

    # 3. metric dead, graph only dead-prior -> INFERRED (single leg)
    dc = dual_evidence_verdict(mk_graph(GRAPH_ZERO_PENDING), mk_metric(METRIC_ZERO, 0), vintage=cur)
    cases.append(("metric-only+prior => INFERRED", dc.level == LEVEL_INFERRED and "PENDING" in dc.verdict))

    # 4. metric dead, graph reachable -> INFERRED (contradiction surfaced in string)
    dc = dual_evidence_verdict(mk_graph(GRAPH_REACHABLE), mk_metric(METRIC_ZERO, 0), vintage=cur)
    cases.append(("metric-dead+graph-reachable => INFERRED", dc.level == LEVEL_INFERRED))

    # 5. graph zero, metric pending -> INFERRED (single leg)
    dc = dual_evidence_verdict(mk_graph(GRAPH_ZERO_CONSUMER), mk_metric(METRIC_PENDING, None, npts=0), vintage=cur)
    cases.append(("graph-only+metric-pending => INFERRED", dc.level == LEVEL_INFERRED))

    # 6. metric shows activity -> REACHABLE regardless of graph
    dc = dual_evidence_verdict(mk_graph(GRAPH_ZERO_CONSUMER), mk_metric(METRIC_NONZERO, 42), vintage=cur)
    cases.append(("activity => REACHABLE", "REACHABLE" in dc.verdict and dc.level != LEVEL_CONFIRMED))

    # 7. nothing -> UNKNOWN
    dc = dual_evidence_verdict(mk_graph(GRAPH_UNKNOWN), mk_metric(METRIC_PENDING, None, npts=0), vintage=cur)
    cases.append(("nothing => UNKNOWN", dc.verdict == "UNKNOWN"))

    # 8. reserved-word guard
    cases.append(("reserved-word legal only on CONFIRMED",
                  reserved_word_legal(LEVEL_CONFIRMED) and not reserved_word_legal(LEVEL_INFERRED)))

    # 9. Signal level flows through from a CONFIRMED dead-confirm
    dc = dual_evidence_verdict(mk_graph(GRAPH_ZERO_CONSUMER), mk_metric(METRIC_ZERO, 0), vintage=cur)
    sig = signal_from_dead_confirm("cloudtrail", "cold", dc)
    cases.append(("signal_from_dead_confirm CONFIRMED", sig.level == LEVEL_CONFIRMED))

    # 10. dead_prior detection
    cases.append(("dead_prior deprecated/", dead_prior("infra/deprecated/foo.tf") and not dead_prior("infra/live/foo.tf")))

    npass = sum(1 for _, ok in cases if ok)
    for name, ok in cases:
        print(f"  {'OK  ' if ok else 'FAIL'} {name}")
    print(f"grounding_lib self-test: {npass}/{len(cases)} passed")
    return 0 if npass == len(cases) else 1


def _validate_dead_live() -> int:
    """Live metric fixture (mirrors dup_scan --validate-dead): opal-users v1 should read
    dead over the window, opal-users-v2 REACHABLE. Requires AWS creds."""
    print(f"=== LIVE DEAD-CONFIRM FIXTURE (window={DEFAULT_WINDOW_DAYS}d) ===")
    for table, graph_assume in [("opal-users", "CONFIRMED_DEAD"), ("opal-users-v2", "REACHABLE")]:
        v = windowed_dead_verdict_ddb(graph_assume, table)
        print(f"  {table:<16} graph_assume={graph_assume:<16} -> {v}")
    return 0


def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(
        prog="comp-debt.grounding_lib",
        description="Shared Rule-22 dual-evidence dead-confirm for comp-debt signals.")
    ap.add_argument("--self-test", action="store_true", help="run deterministic combinator fixtures (no network)")
    ap.add_argument("--validate-dead", action="store_true", help="run the live DynamoDB dead-confirm fixture")
    ap.add_argument("--vintage", action="store_true", help="print the current graph vintage")
    args = ap.parse_args(argv)
    if args.vintage:
        v = read_graph_vintage()
        print(f"graph vintage: {v.status} built={v.built_iso} age={v.age_hours}h trustworthy={v.trustworthy}")
        return 0
    if args.validate_dead:
        return _validate_dead_live()
    return _self_test()


if __name__ == "__main__":
    sys.exit(main())
