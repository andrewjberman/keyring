"""comp_msbeff_rebaseline.py -- re-verdict historical comp-tool telemetry under the DERIVED output
contracts (NFRA_MSBEFF.R1R3 / M3 acceptance 6, 2026-07-23, 0.8.0_AE_CloudComp).

WHY: the M3 fix retired the hand-frozen VERDICT_EXIT_TOOLS set; classify_exit now DERIVES the result
class from comp-output-contracts.yaml. Rows written BEFORE the fix carry the class the frozen set gave
them -- so MSBEFF's own numbers (msbeff_log_audit.py per_result counts) stand on a mix of frozen-era and
derived-era classifications. This re-baseline re-verdicts every historical row from its `rc` (the
INVARIANT the appender preserves) under the CURRENT derived contracts, so the measurement stands on ONE
corrected appender.

NON-DESTRUCTIVE by design: the source of truth is org/mcp/comp-tool-runs.jsonl (the second-granular sink,
which carries `rc`). We re-derive `result` from `rc`; we never rewrite the append-only compiler-tools-log.md
(a shared, concurrently-appended record). `--write` emits a corrected sidecar
org/mcp/comp-tool-runs-rebaselined.jsonl for a consumer that wants the re-verdicted stream; default is a
report only.

GROUNDING: the re-verdict is `comp_output_contract.classify_exit(tool, rc)` -- the SAME single point the
live appender now uses. So the re-baseline and the going-forward appender cannot diverge (one function).
The markdown log carries NO rc column (only the already-classified token), so it is not re-baselineable and
is intentionally not touched -- the jsonl sink is the rc-bearing source the M3 ruling named.
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Optional

_WS = Path(__file__).resolve().parents[3]
if str(_WS) not in sys.path:
    sys.path.insert(0, str(_WS))

from org.modules.graph import comp_output_contract as oc  # noqa: E402

_RUNS = _WS / "org" / "mcp" / "comp-tool-runs.jsonl"
_OUT = _WS / "org" / "mcp" / "comp-tool-runs-rebaselined.jsonl"


def _rows():
    if not _RUNS.exists():
        return
    for line in _RUNS.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            yield json.loads(line)
        except Exception:
            continue  # a malformed row is a finding about the sink, counted below


def rebaseline(write: bool = False) -> dict:
    total = 0
    malformed = 0
    old_dist = Counter()
    new_dist = Counter()
    changed = 0
    change_by = defaultdict(Counter)   # (tool, rc) -> Counter("OLD->NEW")
    corrected_rows = []

    raw_lines = _RUNS.read_text(encoding="utf-8").splitlines() if _RUNS.exists() else []
    for line in raw_lines:
        line = line.strip()
        if not line:
            continue
        try:
            r = json.loads(line)
        except Exception:
            malformed += 1
            continue
        total += 1
        tool = r.get("tool", "?")
        rc = r.get("rc", 0)
        try:
            rc = int(rc)
        except (TypeError, ValueError):
            rc = 0
        old = str(r.get("result", "UNSTATED")).split()[0] if r.get("result") else "UNSTATED"
        new = oc.classify_exit(tool, rc)
        old_dist[old] += 1
        new_dist[new] += 1
        if old != new:
            changed += 1
            change_by[(tool, rc)][f"{old}->{new}"] += 1
        if write:
            r2 = dict(r)
            r2["result"] = new
            r2["result_prior"] = old
            r2["rebaselined"] = True
            corrected_rows.append(r2)

    if write and corrected_rows:
        _OUT.write_text("\n".join(json.dumps(x, ensure_ascii=True) for x in corrected_rows) + "\n",
                        encoding="utf-8")

    return {
        "total_rows": total,
        "malformed_rows": malformed,
        "changed_rows": changed,
        "old_distribution": dict(old_dist.most_common()),
        "new_distribution": dict(new_dist.most_common()),
        "changes_by_tool_rc": {f"{t}:rc{rc}": dict(c) for (t, rc), c in sorted(change_by.items())},
        "contract_summary": oc.coverage_summary(),
        "wrote_sidecar": str(_OUT) if (write and corrected_rows) else None,
    }


def refuse_enumeration() -> dict:
    """AC-6 deliverable for CVO~Z: the ROW-LEVEL enumeration of every jsonl row that re-verdicts to
    REFUSE, plus the binding rule (tool, rc) -> class with its source citation. 'Artifact not number':
    CVO~Z can verify each binding against source and each row against the sink. Off the RIGHT plane --
    comp-tool-runs.jsonl carries the real rc (no text inference), so no rc mis-binning is possible."""
    import yaml
    doc = yaml.safe_load((Path(__file__).resolve().parent / "comp-output-contracts.yaml").read_text(encoding="utf-8"))
    contracts = doc.get("contracts") or {}
    rows = []
    rules = {}
    for r in _rows():
        tool = r.get("tool", "?")
        try:
            rc = int(r.get("rc", 0))
        except (TypeError, ValueError):
            rc = 0
        if rc == 0:
            continue
        old = str(r.get("result", "UNSTATED")).split()[0] if r.get("result") else "UNSTATED"
        new = oc.classify_exit(tool, rc)
        if new != "REFUSE":
            continue
        key = f"{tool}:rc{rc}"
        if key not in rules:
            c = contracts.get(tool, {})
            spec = (c.get("exit_codes") or {}).get(str(rc), {})
            rules[key] = {
                "binding": f"({tool}, rc{rc}) -> REFUSE",
                "meaning": spec.get("meaning", "") if isinstance(spec, dict) else str(spec),
                "exit_source": c.get("exit_source", "UNCITED"),
            }
        rows.append({"ts_epoch": r.get("ts_epoch"), "session_id": r.get("session_id", ""),
                     "tool": tool, "rc": rc, "old_result": old, "new_result": "REFUSE",
                     "rule": key})
    by_rule = Counter(x["rule"] for x in rows)
    return {"snapshot": _snapshot_vintage(),
            "refuse_rows_total": len(rows), "by_rule": dict(by_rule.most_common()),
            "binding_rules": rules, "rows": rows}


def _snapshot_vintage() -> dict:
    """SNAPSHOT-level vintage header (CVO~Z rec, adopted): the artifact self-pins to its source vintage
    instead of relying on per-row ts_epoch. 'A row-count without its vintage is not a count.' The next
    re-derive is trivial: a differing jsonl_rows / sha means the sink advanced, not a classification miss."""
    import hashlib
    raw = _RUNS.read_bytes() if _RUNS.exists() else b""
    total = sum(1 for ln in raw.decode("utf-8", "replace").splitlines() if ln.strip())
    return {
        "source": "org/mcp/comp-tool-runs.jsonl",
        "jsonl_rows": total,
        "sha256_first16": hashlib.sha256(raw).hexdigest()[:16],
        "contract_summary": oc.coverage_summary(),
        # as_of is the sink's own newest ts_epoch (no wall-clock call -- deterministic, matches the data)
        "as_of_ts_epoch": max((r.get("ts_epoch") or 0 for r in _rows()), default=None),
    }


# ======================================================================================
# E4.1 CONDITION 3 -- DUAL-BASIS PRESERVATION + THE QUERY THAT READS IT BACK
# (NFRA_VELOCITY_ESTATE WS-E4.1, COO dispatch 20260730T053344Z; ~C clean-read finding 3)
#
# WHY A `verdict_basis` VERSION COLUMN AND NOT A `result_prior` FIELD:
# `result_prior` (above, the 07-23 shape) preserves the VALUE but not the LOGIC that
# produced it. A re-baselined series and an original series then differ by an unknown
# mixture of two causes -- "the verdict logic changed" and "the estate changed" -- and
# both move a re-baselined series IDENTICALLY. The discriminating residue is the BASIS
# IDENTITY, and it is unrecoverable if not captured at the moment of the re-baseline.
# With 51 tools still pending declaration the contract surface WILL move again, so
# `rebaselined: true` cannot separate a v1 re-baseline from a v2 one. The basis id below
# self-pins to the contract surface's own version AND content hash, so two re-baselines
# taken across a contract edit are distinguishable forever.
#
# ROWS ALONGSIDE ROWS, not fields alongside fields: each source row emits TWO rows, one
# per basis, each carrying its verdict in the SAME `result` field. A consumer therefore
# filters on one column and gets a complete, clean series -- it never needs per-basis
# field-selection logic, which is the shape that silently reads the wrong field.
# ======================================================================================

BASIS_AS_WRITTEN = "as-written"

# The FAIL predicate is PRINTED with every series, because two honest predicates sharing
# one word moved this population by 3 rows: C5 reported April FAIL=221/12.14% and a
# `startswith("FAIL")` predicate yields 224/12.30% -- the delta is exactly the 3
# `FAIL->FIXED` rows in the markdown corpus. Neither count is wrong; they answer
# different questions. An unstated predicate makes them look like a discrepancy.
FAIL_PREDICATE = ("result token == 'FAIL' exactly, after stripping a "
                  "'(SYNTHETIC TEST FIXTURE)' suffix; 'FAIL->FIXED' and any other "
                  "FAIL-prefixed token are NOT counted")


def _contract_surface_id() -> str:
    """DELEGATES to comp_output_contract (E4.3 element 1, 2026-07-30).

    This used to be a second implementation. It is now a thin forwarder, on purpose: the appender
    stamps the basis at write time and this module labels the re-derived series, and if those two
    ever computed the identity differently the whole discriminator would be worthless. One
    implementation, N consumers -- the same rule the contract helper's own docstring states, and the
    defect its supersession history records four generations of.
    """
    return oc.contract_surface_id()


def derived_basis_id() -> str:
    return oc.derived_basis_id()


# ======================================================================================
# E4.3 ELEMENTS 2 + 4 + 5 -- SPAN AS A PRECONDITION, AND THE DEVICE SCOPE AS A FIELD
# (COO rulings 20260730T072044Z)
#
# ELEMENT 4, RULED: "a series must assert its own span against the window it claims, and
# REFUSE to emit a claim over a window longer than the corpus it has. Refuse loudly; never
# silently narrow." A trend over 90 days computed from 40 days of retained rows is not a
# degraded trend -- it is A DIFFERENT NUMBER WEARING THE LABEL. And it is a live risk, not a
# hypothetical: no rotation logic exists today, but .gitignore:448 anticipates it
# (`comp-tool-runs.jsonl.*`), so a long window dies SILENTLY if rotation lands mid-window.
#
# ELEMENT 5, RULED: PER-DEVICE, with the device scope printed on every series. A rollup is
# BLOCKED, NOT DEFERRED -- the rc-bearing sink is gitignored and device-local, so there is no
# durable cross-device record to roll up FROM, and emitting one today would FABRICATE
# COVERAGE. That is the same class as quoting a conversion rate before R8 existed. A genuine
# rollup needs a durable cross-device sink, which is a NAMED DEPENDENCY and not E4.3's to
# invent.
# ======================================================================================

DEVICE_SCOPE = ("PER-DEVICE -- org/mcp/comp-tool-runs.jsonl is gitignored (.gitignore:447), so this "
                "series covers THIS DEVICE ONLY and is silently short by every other device's "
                "traffic. It is NOT 'the estate's comp-tool runs'. A cross-device rollup is BLOCKED "
                "(no durable cross-device sink exists to roll up from); that sink is a named "
                "dependency, not a deferred task.")


class TrendWindowUnsupported(Exception):
    """The corpus cannot support the window a claim asks for. A LOUD refusal, never a narrowing.

    Raised rather than returned so a caller cannot accidentally treat a short answer as the
    answer it asked for. Carries the numbers so the refusal is actionable, not merely a denial.
    """


def assert_window_supported(months_claimed: int, profile: Optional[dict] = None) -> dict:
    """PRECONDITION for any multi-month trend claim (element 2 + 4).

    Promotes corpus span from a disclosure line to a gate. Returns the profile on success so the
    caller cannot use it without having passed the check; RAISES TrendWindowUnsupported otherwise.
    """
    prof = profile if profile is not None else corpus_profile()
    have = len(prof.get("months_present") or {})
    if months_claimed > have:
        raise TrendWindowUnsupported(
            "REFUSED: a %d-month trend was requested but the corpus holds %d month(s) "
            "(rows=%s, span=%s days, %s -> %s). A trend over a window longer than its corpus is "
            "not a degraded trend, it is a different number wearing the label. Rebuild forward; "
            "the historical window is NOT recoverable (the pre-2026-07-14 corpus carries no rc "
            "column and cannot be re-verdicted). %s"
            % (months_claimed, have, prof.get("rows"), prof.get("span_days"),
               prof.get("earliest"), prof.get("latest"), DEVICE_SCOPE))
    return prof


def _fail_token(result_raw) -> tuple:
    """(bare_token, is_synthetic). Splitting this out is what makes the predicate auditable."""
    s = str(result_raw or "UNSTATED")
    synthetic = "SYNTHETIC" in s
    return (s.split()[0] if s.split() else "UNSTATED", synthetic)


def corpus_profile() -> dict:
    """WHAT THE NUMBER IS *OF*, before any rate is computed.

    This exists because C5's trend (12.14% -> 6.14%, four months) was computed over the
    day-granular markdown log, and the rc-bearing jsonl sink -- the ONLY corpus a derived
    verdict can be re-baselined from -- begins 2026-07-14. A four-month trend is not
    re-derivable on a 16-day corpus, and that is a structural fact about the population,
    not a disagreement about the rate. Printing the span is what surfaces it.
    """
    import datetime
    lo = hi = None
    months = Counter()
    n = 0
    for r in _rows():
        t = r.get("ts_epoch") or 0
        n += 1
        lo = t if lo is None or t < lo else lo
        hi = t if hi is None or t > hi else hi
        months[datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m")] += 1

    def _f(t):
        if t is None:
            return None
        return datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    return {
        "source": "org/mcp/comp-tool-runs.jsonl",
        "rows": n,
        "earliest": _f(lo),
        "latest": _f(hi),
        "span_days": round((hi - lo) / 86400.0, 2) if (lo is not None and hi is not None) else None,
        "months_present": dict(sorted(months.items())),
        "DEVICE_LOCAL": ("this sink is gitignored (.gitignore:447) and therefore DEVICE-LOCAL -- "
                         "it is short by every other device's traffic, silently. Never cite it as "
                         "'the estate's comp-tool runs'."),
        "TREND_CAPABILITY": ("a multi-month trend is NOT derivable here if months_present has one "
                             "entry; the corpus that carries C5's four-month trend is the retired "
                             "day-granular markdown log, which has NO rc column and so cannot be "
                             "re-verdicted under the derived contracts at all"),
    }


def dual_basis_rows():
    """Yield (basis, row) pairs -- the ORIGINAL preserved ALONGSIDE the re-derived.

    The as-written row is emitted VERBATIM (its `result` is never recomputed): it IS the
    historical record of what the appender concluded at run time. The derived row carries
    the same `rc` re-classified under the current contract surface.
    """
    dbid = derived_basis_id()
    for r in _rows():
        try:
            rc = int(r.get("rc", 0))
        except (TypeError, ValueError):
            rc = 0
        as_written = dict(r)
        as_written["verdict_basis"] = BASIS_AS_WRITTEN
        yield (BASIS_AS_WRITTEN, as_written)

        derived = dict(r)
        derived["result"] = oc.classify_exit(r.get("tool", "?"), rc)
        derived["verdict_basis"] = dbid
        derived["result_as_written"] = str(r.get("result", "UNSTATED"))
        yield (dbid, derived)


def write_dual_basis_sidecar() -> dict:
    """Write the dual-basis sidecar + a .meta.json carrying the supersession history.

    Preservation happens IN THIS SAME MOTION as the re-baseline -- after is too late,
    because by then the residue is already gone.
    """
    counts = Counter()
    with open(_OUT, "w", encoding="utf-8") as fh:
        for basis, row in dual_basis_rows():
            fh.write(json.dumps(row, ensure_ascii=True) + "\n")
            counts[basis] += 1
    meta = {
        "artifact": str(_OUT),
        "written_by": "comp_msbeff_rebaseline.write_dual_basis_sidecar",
        "bases": dict(counts),
        "basis_definitions": {
            BASIS_AS_WRITTEN: ("the verdict the appender recorded AT RUN TIME, preserved verbatim. "
                               "No claim is made about which generation of classifier produced it -- "
                               "rows before the M3 fix carry frozen-era verdicts, rows after carry "
                               "derived ones, and the sink does not record which."),
            derived_basis_id(): ("re-derived from the row's rc via comp_output_contract.classify_exit "
                                 "under the contract surface identified in this id"),
        },
        "supersession_history": [
            "1. M2 (CTO~Z): a census read the wrong artifact.",
            "2. CVO~Z: a census read 2 of 3 mapping surfaces.",
            "3. the appender's FROZEN VERDICT_EXIT_TOOLS set -- itself the fix for a prior "
            "nonzero->FAIL blanket miscount; a frozen set drifts from the source contracts silently.",
            "4. this TO's own first spec named comp-tools.yaml (a curated subset) as the derivation "
            "source, inside the TO whose subject is that exact class.",
            "5. 2026-07-23 M3: derivation from source contracts + a completeness gate (the fix).",
            "6. 2026-07-30 E4.1.3: dual-basis preservation -- the value was preserved from 07-23 "
            "(result_prior) but the BASIS IDENTITY was not, so a re-baselined series could not "
            "separate 'the verdict logic changed' from 'the estate changed'.",
        ],
        "corpus_profile": corpus_profile(),
        "fail_predicate": FAIL_PREDICATE,
        "DO_NOT": "do not re-freeze a verdict set anywhere; declare new tools in the contract yaml.",
    }
    meta_path = Path(str(_OUT) + ".meta.json")
    meta_path.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    return {"sidecar": str(_OUT), "meta": str(meta_path), "rows_by_basis": dict(counts)}


def series(basis: str, group_by: str = "month") -> dict:
    """The per-basis series query. `basis` is BASIS_AS_WRITTEN or derived_basis_id().

    Returns per-group n / FAIL / rate WITH the denominator, plus the per-series (per-tool)
    decomposition. NO AGGREGATE HEADLINE SHIPS WITHOUT IT (WS-E4.3): an aggregate that
    moves because the mix moved is a rigorous instrument on the wrong axis, and those
    survive review.
    """
    import datetime
    if basis == BASIS_AS_WRITTEN:
        def verdict(r):
            return _fail_token(r.get("result"))
    else:
        def verdict(r):
            tok = oc.classify_exit(r.get("tool", "?"), int(r.get("rc", 0) or 0))
            return (tok, "SYNTHETIC" in str(r.get("result", "")))

    per = defaultdict(Counter)      # group -> Counter(class)
    per_tool = defaultdict(Counter)  # tool  -> Counter(class)
    excluded_synthetic = 0
    for r in _rows():
        tok, synthetic = verdict(r)
        if synthetic:
            excluded_synthetic += 1
            continue
        t = r.get("ts_epoch") or 0
        if group_by == "month":
            g = datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m")
        else:
            g = datetime.datetime.fromtimestamp(t, datetime.timezone.utc).strftime("%Y-%m-%d")
        per[g][tok] += 1
        per_tool[r.get("tool", "?")][tok] += 1

    def _rate(c):
        n = sum(c.values())
        f = c.get("FAIL", 0)
        return {"n": n, "FAIL": f, "rate_pct": round(100.0 * f / n, 2) if n else None,
                "classes": dict(c.most_common())}

    return {
        "basis": basis,
        "device_scope": DEVICE_SCOPE,   # element 5: a FIELD, not a caveat a reader may drop
        "fail_predicate": FAIL_PREDICATE,
        "excluded_synthetic_rows": excluded_synthetic,
        "by_" + group_by: {g: _rate(c) for g, c in sorted(per.items())},
        "by_tool": {t: _rate(c) for t, c in sorted(per_tool.items(),
                                                   key=lambda kv: -sum(kv[1].values()))},
        "corpus_profile": corpus_profile(),
    }


def dual_basis_compare(group_by: str = "month") -> dict:
    """EXERCISE the preservation: run the series under BOTH bases and report where they
    disagree. A column nobody has read back is a passing assertion that has never been
    tested (COO refinement, 20260730T053709Z). If the two answers are IDENTICAL that is
    reported as a finding to investigate -- either the re-baseline changed nothing, or the
    basis switch is not wired -- never as a pass.
    """
    a = series(BASIS_AS_WRITTEN, group_by)
    b = series(derived_basis_id(), group_by)
    key = "by_" + group_by
    groups = sorted(set(a[key]) | set(b[key]))
    rows = []
    disagreements = 0
    for g in groups:
        ra, rb = a[key].get(g, {}), b[key].get(g, {})
        differs = (ra.get("FAIL") != rb.get("FAIL"))
        disagreements += 1 if differs else 0
        rows.append({group_by: g, "n": ra.get("n") or rb.get("n"),
                     "FAIL_as_written": ra.get("FAIL"), "rate_as_written": ra.get("rate_pct"),
                     "FAIL_derived": rb.get("FAIL"), "rate_derived": rb.get("rate_pct"),
                     "differs": differs})
    tool_rows = []
    for t in sorted(set(a["by_tool"]) | set(b["by_tool"])):
        ta, tb = a["by_tool"].get(t, {}), b["by_tool"].get(t, {})
        if ta.get("FAIL") != tb.get("FAIL"):
            tool_rows.append({"tool": t, "n": ta.get("n") or tb.get("n"),
                              "FAIL_as_written": ta.get("FAIL"), "FAIL_derived": tb.get("FAIL"),
                              "rate_as_written": ta.get("rate_pct"),
                              "rate_derived": tb.get("rate_pct")})
    return {
        "basis_a": BASIS_AS_WRITTEN,
        "basis_b": derived_basis_id(),
        "groups": rows,
        "group_disagreements": disagreements,
        "per_tool_disagreements": tool_rows,
        "VERDICT": ("EXERCISED -- the two bases return DIFFERENT series, so the basis switch is "
                    "wired and the re-baseline is material"
                    if disagreements or tool_rows else
                    "IDENTICAL -- NOT a pass. Either the re-baseline changed nothing on this "
                    "corpus, or the basis switch is not wired. Determine WHICH before citing "
                    "any trend."),
        "fail_predicate": FAIL_PREDICATE,
        "corpus_profile": corpus_profile(),
    }


def _print_dual_basis(rep, group_by="month"):
    print("=" * 92)
    print("E4.1.3 DUAL-BASIS EXERCISE -- the same trend claim re-derived under BOTH bases")
    print("=" * 92)
    cp = rep["corpus_profile"]
    print("corpus : %s" % cp["source"])
    print("rows   : %s   span: %s -> %s (%s days)" % (cp["rows"], cp["earliest"],
                                                      cp["latest"], cp["span_days"]))
    print("months : %s" % ", ".join("%s(n=%d)" % (k, v) for k, v in cp["months_present"].items()))
    print("basis A: %s" % rep["basis_a"])
    print("basis B: %s" % rep["basis_b"])
    print("FAIL predicate: %s" % rep["fail_predicate"])
    print("")
    print("  %-9s %8s | %9s %9s | %9s %9s | %s" % (group_by.upper(), "n", "FAIL(A)",
                                                   "rate(A)", "FAIL(B)", "rate(B)", "DIFFERS"))
    for r in rep["groups"]:
        print("  %-9s %8s | %9s %8s%% | %9s %8s%% | %s" % (
            r[group_by], r["n"], r["FAIL_as_written"], r["rate_as_written"],
            r["FAIL_derived"], r["rate_derived"], "YES" if r["differs"] else "no"))
    print("")
    print("-- PER-SERIES DECOMPOSITION (mandatory: no aggregate headline ships without it) --")
    print("   tools whose FAIL count MOVES between bases:")
    if not rep["per_tool_disagreements"]:
        print("     (none)")
    for t in rep["per_tool_disagreements"]:
        print("     %-24s n=%-6s FAIL %s -> %s   (%s%% -> %s%%)" % (
            t["tool"], t["n"], t["FAIL_as_written"], t["FAIL_derived"],
            t["rate_as_written"], t["rate_derived"]))
    print("")
    print("VERDICT: %s" % rep["VERDICT"])
    print("\nNOTE ON TREND CAPABILITY: %s" % cp["TREND_CAPABILITY"])
    print("DEVICE SCOPE: %s" % cp["DEVICE_LOCAL"])


def main(argv) -> int:
    write = "--write" in argv
    as_json = "--json" in argv
    group_by = "day" if "--daily" in argv else "month"
    if "--refuse-enum" in argv:
        print(json.dumps(refuse_enumeration(), indent=2))
        return 0
    if "--corpus-profile" in argv:
        print(json.dumps(corpus_profile(), indent=2))
        return 0
    if "--dual-basis" in argv:
        rep = dual_basis_compare(group_by)
        if as_json:
            print(json.dumps(rep, indent=2))
        else:
            _print_dual_basis(rep, group_by)
        if write:
            info = write_dual_basis_sidecar()
            print("\nwrote dual-basis sidecar: %s" % info["sidecar"])
            print("wrote basis metadata    : %s" % info["meta"])
            print("rows by basis           : %s" % info["rows_by_basis"])
        return 0
    if "--series" in argv:
        basis = BASIS_AS_WRITTEN
        for i, a in enumerate(argv):
            if a == "--basis" and i + 1 < len(argv):
                basis = derived_basis_id() if argv[i + 1] == "derived" else argv[i + 1]
        print(json.dumps(series(basis, group_by), indent=2))
        return 0
    rep = rebaseline(write=write)
    if as_json:
        print(json.dumps(rep, indent=2))
        return 0
    print("=" * 78)
    print("NFRA_MSBEFF telemetry RE-BASELINE -- historical rows re-verdicted under derived contracts")
    print("=" * 78)
    print(f"source: org/mcp/comp-tool-runs.jsonl   rows: {rep['total_rows']}   "
          f"malformed: {rep['malformed_rows']}   CHANGED: {rep['changed_rows']}")
    print(f"contracts: {rep['contract_summary']['declared']} declared / "
          f"{rep['contract_summary']['pending']} pending / "
          f"{rep['contract_summary']['registered']} registered (tools_index)")
    print("\n-- result-class distribution (OLD frozen-era token  ->  NEW derived) --")
    keys = sorted(set(rep["old_distribution"]) | set(rep["new_distribution"]))
    print(f"  {'CLASS':<10} {'OLD':>7} {'NEW':>7} {'DELTA':>7}")
    for k in keys:
        o = rep["old_distribution"].get(k, 0)
        n = rep["new_distribution"].get(k, 0)
        print(f"  {k:<10} {o:>7} {n:>7} {n - o:>+7}")
    print("\n-- rows that RE-VERDICTED, by (tool, rc) -- the corrections the derivation makes --")
    if not rep["changes_by_tool_rc"]:
        print("  (none -- the derived appender agrees with the historical classification)")
    for k, c in rep["changes_by_tool_rc"].items():
        for transition, n in c.items():
            print(f"  {k:<24} {transition:<18} {n:>5} row(s)")
    if rep["wrote_sidecar"]:
        print(f"\nwrote corrected sidecar: {rep['wrote_sidecar']}")
    print("\nNOTE: the append-only compiler-tools-log.md is intentionally NOT rewritten (shared, "
          "concurrently-appended, and it carries no rc column to re-derive from). The rc-bearing jsonl "
          "sink is the re-baselineable source, per the M3 ruling.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
