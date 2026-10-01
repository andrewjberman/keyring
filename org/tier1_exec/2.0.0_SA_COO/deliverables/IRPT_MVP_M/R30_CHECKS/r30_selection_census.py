"""Workstream ~M, STATUS~M.md item 1: the REAL RUN of the holdings route's projection over real built snapshots.

Input: one real local Holdings build per firm, saved as <dir>/<firm>.snapshot.json (built from the firm buckets and
the classifier tables by the producer at this tree; not committed -- it holds client positions). For each firm this
runs the route's own `snapshot.project()` once per account (a one-account selection) and once over every account,
and reads the two served blocks off each slice.

Per firm it counts: slices attempted; slices carrying the blocks; slices where none was served (actual positions
exceed the custody total); slices whose class_totals plus class_totals_remainder do not tie to the slice's custody
total within a cent; slices that do not validate against the contract; aggregate rows carrying no class because
their member nodes disagree; and the slices with a non-zero remainder (custody with no actual position under it).
It writes the census JSON and prints one line.

Usage, from the repo (or worktree) root:
  python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R30_CHECKS/r30_selection_census.py <dir> [--write]
Prints SELECTION-CENSUS <firm=slices/blocks/untied/invalid ...> or NOT-CENSUSED: <reason>. Exit 0 only when every
firm has zero untied and zero invalid slices.
"""
import json
import os
import sys

ROOT = os.getcwd()
FN = os.path.join(ROOT, "infra", "aws", "lambda", "investor-reporting")
for p in (os.path.join(FN, "holdings"), os.path.join(FN, "_authz"), os.path.join(FN, "_scope"),
          os.path.join(FN, "_ids"), os.path.join(FN, "_keys")):
    if p not in sys.path:
        sys.path.insert(0, p)

OUT = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R30_SELECTION_CENSUS_20261001.json"
FIRMS = ("49financial", "inflection", "cottonwood")


def scope_for(ids, firm_opaque):
    return {"verified_request_firm_id": firm_opaque, "permitted_account_set": sorted(ids),
            "permitted_account_set_fingerprint": "a" * 64, "principal_class": "FIRM_OPERATIONS"}


def census_firm(sn, firm, path):
    with open(path, encoding="utf-8") as fh:
        snap = json.load(fh)
    snap = {k: v for k, v in snap.items() if not k.startswith("_")}
    accounts = sorted({n["node_id"] for n in snap["nodes"] if n.get("node_kind") == "ACCOUNT"})
    firm_opaque = (snap.get("scope") or {}).get("firm_id")
    row = {"firm": firm, "business_date": (snap.get("clocks") or {}).get("business_date"),
           "accounts": len(accounts), "slices": 0, "refused": 0, "with_blocks": 0, "neither_served": 0,
           "untied": 0, "invalid": 0, "with_remainder": 0, "rows_without_class": 0,
           "aggregate_rows": 0, "max_tie_gap": 0.0, "invalid_examples": [], "refused_examples": []}
    # The route loads a publication bounded to the selected accounts (load_snapshot(account_ids=...)), so a
    # one-account selection is run over that account's own nodes: the same input the route gives project().
    parent_of = {n["node_id"]: n.get("parent_node_id") for n in snap["nodes"]}
    by_root = {}
    for n in snap["nodes"]:
        by_root.setdefault(sn._root_account(n["node_id"], parent_of), []).append(n)
    selections = [[a] for a in accounts] + [accounts]
    for ids in selections:
        row["slices"] += 1
        bounded = snap if len(ids) == len(accounts) else dict(snap, nodes=by_root.get(ids[0], []))
        try:
            out = sn.project(bounded, scope_for(ids, firm_opaque))
        except sn.SnapshotUnavailable as exc:
            row["refused"] += 1
            if len(row["refused_examples"]) < 3:
                row["refused_examples"].append(str(exc))
            continue
        if "class_totals" not in out:
            row["neither_served"] += 1
            continue
        row["with_blocks"] += 1
        total = out["custody_totals"]["total_market_value"]["value"]
        remainder = out["class_totals_remainder"]["amount"]["value"]
        gap = abs(sum(t["amount"]["value"] for t in out["class_totals"]) + remainder - total)
        row["max_tie_gap"] = max(row["max_tie_gap"], round(gap, 6))
        if gap > 0.01:
            row["untied"] += 1
        if remainder > 0.005:
            row["with_remainder"] += 1
        if len(ids) == len(accounts):
            row["firm_wide_rows"] = len(out["security_aggregates"])
            row["firm_wide_rows_without_class"] = sum("asset_class" not in r for r in out["security_aggregates"])
            row["firm_wide_class_totals"] = {t["asset_class"]: round(t["amount"]["value"], 2)
                                             for t in out["class_totals"]}
            row["firm_wide_remainder"] = round(remainder, 2)
            row["firm_wide_custody_total"] = total
        else:
            row["aggregate_rows"] += len(out["security_aggregates"])
            row["rows_without_class"] += sum("asset_class" not in r for r in out["security_aggregates"])
        verdict = sn.validate_slice(out)
        if not verdict["available"]:
            return None, "no contract or jsonschema on this runtime: %s" % verdict.get("reason")
        if not verdict["valid"]:
            row["invalid"] += 1
            if len(row["invalid_examples"]) < 3:
                row["invalid_examples"].append(verdict["errors"][:2])
    return row, None


def main():
    args = [a for a in sys.argv[1:] if a != "--write"]
    if len(args) != 1:
        print("NOT-CENSUSED: usage r30_selection_census.py <dir> [--write]")
        return 1
    import snapshot as sn
    if not sn.aggregates_admitted():
        print("NOT-CENSUSED: the contract this tree resolves does not admit the two blocks")
        return 1
    rows = []
    for firm in FIRMS:
        path = os.path.join(args[0], "%s.snapshot.json" % firm)
        if not os.path.exists(path):
            print("NOT-CENSUSED: %s absent" % path)
            return 1
        row, why = census_firm(sn, firm, path)
        if row is None:
            print("NOT-CENSUSED: %s" % why)
            return 1
        rows.append(row)
    if "--write" in sys.argv:
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            json.dump({"what": "real-build snapshots run through the holdings route's project(): one selection per "
                               "account plus one over every account", "firms": rows}, fh, indent=1)
            fh.write("\n")
    bad = any(r["untied"] or r["invalid"] for r in rows)
    print("%s %s" % ("NOT-CENSUSED: untied or invalid slices --" if bad else "SELECTION-CENSUS",
                     " ".join("%s=%d/%d/%d/%d" % (r["firm"], r["slices"], r["with_blocks"], r["untied"], r["invalid"])
                              for r in rows)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
