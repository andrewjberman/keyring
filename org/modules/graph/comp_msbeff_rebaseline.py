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
    return {"refuse_rows_total": len(rows), "by_rule": dict(by_rule.most_common()),
            "binding_rules": rules, "rows": rows}


def main(argv) -> int:
    write = "--write" in argv
    as_json = "--json" in argv
    if "--refuse-enum" in argv:
        print(json.dumps(refuse_enumeration(), indent=2))
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
