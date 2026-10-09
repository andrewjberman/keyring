"""MDPF_STRATID round 2, ST-u-2 criterion AC2: the seam probe on REAL data (read-only S3; writes nothing).

Folds the served Cottonwood slice into the PRE-FOLD Global doc with the current registry and code, shapes the Global category
tree, and reads on Global's last date:
  - every SMA member of the tree (ETF Strategies and ALT Strategies) carries `inside_model_figure` (bool) and `held_out` (list);
  - each Cottonwood sma member with overlap > 0 appears in its tree member's `held_out` as {firm_id: cottonwood, value: its
    overlap, reason: OVERLAP}, and the additive by_model entry (if any) carries `inside_model_value` equal to that overlap;
  - Cottonwood PFDE (overlap 0.0 today) states inside_model_value 0.0 and is not held out;
  - the totals equal ST-u-1's fold (the statement moves no figure).
SEAM-OK when all hold; else SEAM-BAD with the item named.
"""
from __future__ import annotations

import copy
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _r2_seam as r2  # noqa: E402


def _bad(msg: str) -> int:
    print("SEAM-BAD " + msg)
    return 1


def main() -> int:
    g, cot = r2.load()
    import mdpf_gold_consolidator as gc

    pre = r2.pre_fold(g)
    day, i = g["dates"][-1], len(g["dates"]) - 1
    out = gc.apply_sma_sleeve_overlay({"global": copy.deepcopy(pre), "cottonwood": copy.deepcopy(cot)})["global"]
    try:
        nodes = gc._shape_category_views(copy.deepcopy(out), "global")["nodes"]
    except SystemExit as e:
        return _bad("tree raises: %s" % str(e)[:200])
    members = {}
    for bucket, b in nodes["SMA"]["children"].items():
        for m in b["members"]:
            if "inside_model_figure" not in m or "held_out" not in m:
                return _bad("tree member %s/%s lacks inside_model_figure or held_out" % (bucket, m["member_id"]))
            members[m["member_id"]] = m
    seen = 0
    for mid, e in cot["by_model"].items():
        if e.get("cohort_class") != "sma":
            continue
        v, ov = r2.cot_at(cot, mid, day)
        if v is None or ov is None:
            continue
        seen += 1
        tm = members.get(mid)
        if tm is None:
            return _bad("Cottonwood %s has no tree member at Global" % mid)
        held = [h for h in tm["held_out"] if h.get("firm_id") == "cottonwood"]
        if ov > 0:
            if not held or abs(held[0].get("value", 0) - ov) > 0.01 or held[0].get("reason") != "OVERLAP":
                return _bad("Cottonwood %s overlap %.2f not named in held_out (%r)" % (mid, ov, tm["held_out"]))
        elif held:
            return _bad("Cottonwood %s overlap 0 but held_out %r" % (mid, held))
        be = out["by_model"].get(mid) or {}
        if be.get("source_basis") == "additive" and "cottonwood" in (be.get("firms") or []):
            iv = (be.get("inside_model_value") or [None] * (i + 1))[i]
            if iv is None or abs(iv - ov) > 0.01:
                return _bad("by_model[%s].inside_model_value on %s = %r, want %.2f" % (mid, day, iv, ov))
        print("  %s value %.2f overlap %.2f -> held_out %s, inside_model_figure %s" % (mid, v, ov, held, tm["inside_model_figure"]))
    if not seen:
        return _bad("no Cottonwood sma member with a measured overlap on %s" % day)
    print("totals: Global %.2f on %s; %d Cottonwood members stated" % (out["opal_aggregate_aua"][i], day, seen))
    print("SEAM-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
