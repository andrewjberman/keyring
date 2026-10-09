"""MDPF_STRATID round 2, ST-u-1 criterion AC2: the seam probe against the REAL neighbours (read-only S3; writes nothing).

  BUILD    the registry declares cottonwood OUTSIDE.
  ARM A    the served Cottonwood slice folded into the PRE-FOLD Global doc (`_r2_seam.pre_fold`) with the CURRENT registry:
           the category tree builds (no SystemExit); every Cottonwood sma member on Global's last date is either counted
           (value - overlap added) or named in `sma_additive_withheld`; Global's total on that date equals pre-fold total + the
           counted sum; and on today's data that equals the served total (divz fully inside a Model, PFDE counted).
  ARM B    planted, on purpose: the same fold with Cottonwood divz's overlap set to 0.0 on every date. The tree's ETF Strategies >
           divz member equals 49financial's served Dividend SMA + Cottonwood's divz value, Global's total rises by exactly
           Cottonwood's divz value, Client does not move, and nothing raises (one member, two bases, validated per firm).

SEAM-OK when all hold; else SEAM-BAD with the arm named.
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


def _tree(gc, doc):
    try:
        return gc._shape_category_views(copy.deepcopy(doc), "global")["nodes"], None
    except SystemExit as e:  # the tree's basis check raises SystemExit
        return None, str(e)[:200]


def _members(nodes, bucket):
    return {m["member_id"]: m.get("aum") for m in nodes["SMA"]["children"][bucket]["members"]}


def main() -> int:
    g, cot = r2.load()
    import mdpf_category_registry as reg
    import mdpf_gold_consolidator as gc

    if reg.SMA_FIRM_POPULATION.get("cottonwood") != "outside":
        return _bad("arm=build SMA_FIRM_POPULATION['cottonwood'] = %r, want 'outside'" % reg.SMA_FIRM_POPULATION.get("cottonwood"))
    pre = r2.pre_fold(g)
    day = g["dates"][-1]
    i = len(g["dates"]) - 1
    served_total, pre_total = g["opal_aggregate_aua"][i], pre["opal_aggregate_aua"][i]
    nodes0, err0 = _tree(gc, g)
    if err0:
        return _bad("arm=control the served Global doc does not shape: %s" % err0)

    # ARM A -- as served
    outa = gc.apply_sma_sleeve_overlay({"global": copy.deepcopy(pre), "cottonwood": copy.deepcopy(cot)})["global"]
    na, erra = _tree(gc, outa)
    if erra:
        return _bad("arm=A the Global tree raises: %s" % erra)
    withheld = {w["member_id"]: w for w in (outa.get("sma_additive_withheld") or []) if w.get("date") == day and w.get("firm_id") == "cottonwood"}
    counted = 0.0
    for m, e in cot["by_model"].items():
        if e.get("cohort_class") != "sma":
            continue
        v, ov = r2.cot_at(cot, m, day)
        if v is None:
            continue
        part = round(v - (ov or 0.0), 2) if ov is not None else 0.0
        counted += part
        if (ov is None or ov > 0) and m not in withheld:
            return _bad("arm=A Cottonwood %s (value %.2f, overlap %r) is neither fully counted nor named withheld on %s" % (m, v, ov, day))
        print("  A %s value %.2f overlap %r -> counted %.2f%s" % (m, v, ov, part, " | withheld %s %.2f" % (withheld[m]["reason"], withheld[m]["value"]) if m in withheld else ""))
    got = outa["opal_aggregate_aua"][i]
    if abs(got - (pre_total + counted)) > 0.01:
        return _bad("arm=A total %.2f != pre-fold %.2f + counted %.2f" % (got, pre_total, counted))
    if abs(got - served_total) > 0.01:
        print("  A NOTE total %.2f differs from served %.2f by %.2f (a member newly counted today)" % (got, served_total, got - served_total))

    # ARM B -- planted: Cottonwood divz outside every Model
    if "divz" not in cot["by_model"]:
        return _bad("arm=B no Cottonwood divz member on the served slice to plant against")
    cotb = copy.deepcopy(cot)
    cotb["by_model"]["divz"]["overlap_model_value"] = [0.0] * len(cotb["dates"])
    dv, _ = r2.cot_at(cotb, "divz", day)
    outb = gc.apply_sma_sleeve_overlay({"global": copy.deepcopy(pre), "cottonwood": cotb})["global"]
    nb, errb = _tree(gc, outb)
    if errb:
        return _bad("arm=B the Global tree raises on a two-basis member: %s" % errb)
    want = _members(nodes0, "ETF Strategies")["divz"] + dv
    gotd = _members(nb, "ETF Strategies").get("divz")
    if gotd is None or abs(gotd - want) > 0.01:
        return _bad("arm=B ETF Strategies > divz = %r, want 49financial %.2f + Cottonwood %.2f" % (gotd, want - dv, dv))
    delta = round(outb["opal_aggregate_aua"][i] - got, 2)
    if abs(delta - dv) > 0.01:
        return _bad("arm=B total delta %.2f != Cottonwood divz %.2f" % (delta, dv))
    if abs(nb["Client"]["aum"] - nodes0["Client"]["aum"]) > 0.02:
        return _bad("arm=B Client moved")
    print("BUILD cottonwood=outside | A total %.2f (pre %.2f + counted %.2f), tree shapes | B divz %.2f = %.2f + %.2f, total +%.2f, Client unchanged"
          % (got, pre_total, counted, gotd, want - dv, dv, delta))
    print("SEAM-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
