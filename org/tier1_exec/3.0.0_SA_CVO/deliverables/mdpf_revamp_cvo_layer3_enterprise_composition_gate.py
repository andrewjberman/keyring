"""
CVO Layer-3 ENTERPRISE-COMPOSITION gate -- from-scratch, independent (MDPF re-flip hard gate).
B-BASIS + mechanism-bound honest-None (Andrew-direct + CVO fork ruling, both 2026-07-22).

The class this catches (that a PARITY check cannot): the Global enterprise headline and its component
fields being INTERNALLY INCONSISTENT about whether inflection's non-model (cohort-2b) is in or out.
parity != consistency -- a defect present on BOTH served + published ties clean.

>> ANDREW-DIRECT RULING (2026-07-22, relayed by DS, grounded live by CVO) -- READ BEFORE EDITING <<
Andrew chose B / EXCLUDE: opal_aggregate_aua DELIBERATELY EXCLUDES inflection non-model (cohort-2b is
audit-only); non_model_aua is REDEFINED to 49F-only so the internal identity holds; inflection non-model
is a SEPARATE 2b audit field. The headline VALUE does not change (@2026-07-20 = $1,813,038,832.72 =
model $1,538,370,912.28 + 49F-only non_model $274,667,920.44). The FULL cross-firm sum ($1,877,516,932.06)
is NOT the headline. Corroborated: A4 non_model_assets.non_model_aum + the FE band are ALREADY 49F-only.
   >> DO NOT re-add a `headline == SUM_firms(model + FULL non_model)` clause. That is the A path Andrew
      did NOT choose; it fails BY DESIGN under B and would gate RED on a correct artifact. (Prior I2/I4
      encoded A and were RETRACTED at CVO's own catch after the ruling.)

>> FORK RULING (2026-07-22, CVO-verified, CTO-closed): the 3 inflection custody-only dates
   (2026-05-21/06-01/07-01) are HONEST-None, NOT a regression. CVO listed the source partitions:
   eclipse/inflection/silver/fact_portfolios_full (MODEL) is genuinely ABSENT on those dates (PRESENT on
   the bracketing days); orion custody PRESENT. No source measurement exists -> honest-None is correct;
   the legacy value is an imputation (do NOT restore -- that fabricates). Exemption is MECHANISM-BOUND:
   exempt a date IFF (inflection model_aua is None AND the eclipse partition for that date is ABSENT).
   A genuine producer gap (partition PRESENT + components None) still goes RED. This gate OWNS the
   lineage-verify leg -- it reads the eclipse partitions itself (that IS the CVO job; a parity harness
   must not, but the verifier must).

INVARIANTS checked per date, over the FULL series (a HOLD blocks publish / signals rollback):
  E1  enterprise 2-term identity : global.opal_aggregate_aua == global.model_aua + global.non_model_aua
  E2  model rollup (both firms)  : global.model_aua == SUM_component_firms(model_aua)  [inflection model IS in]
  E3  non_model is 49F-only      : global.non_model_aua == 49financial.non_model_aua   [inflection non_model OUT]
  E4  cohort-2b carried, not lost: inflection.non_model_aua present (non-None) every NON-honest-None date
E3 pins "never silently FOLD IN"; E4 pins "never silently DROP". E2/E4 are EXEMPT on a lineage-verified
honest-None date (inflection model None AND eclipse partition absent) -- and ONLY then.

Modes:
  (default)     read STAGED  s3://opal-data-assets/gold/mdpf_revamp/{firm}/aggregate_aua_timeseries.json
                + lineage-verify honest-None dates against live eclipse partitions.
  --served      read SERVED  s3://opal-data-portal-v2/json/mdpf/{firm}/aggregate-aua-timeseries.json
  --selftest    in-memory clean(B) + mutant assertions (NO S3): clean-B -> PASS; fold-in -> HOLD; drop -> HOLD;
                honest-None exempt -> PASS; honest-None-but-partition-PRESENT -> HOLD (real gap).

Provenance: 3.0.0_SA_CVO, 2026-07-22 (B-basis + honest-None revision supersedes the A-assumption original).
Layer 3 of the DS-producer / DT-harness / CVO-rederive defense-in-depth. Held for DS's B re-stage; RED on
the current pre-fix artifact by design (non_model still on the full basis).
"""
from __future__ import annotations

import sys

TOL = 1.00
ROLLUP = "global"
NONMODEL_FIRM = "49financial"     # under B, headline non_model == this firm's non_model (49F-only)
COHORT2B_FIRM = "inflection"      # its non_model is the excluded cohort-2b audit component
FIRMS = ["49financial", "inflection", "global"]
STAGED_B = "opal-data-assets"
SERVED_B = "opal-data-portal-v2"
ECLIPSE_MODEL_PREFIX = "eclipse/inflection/silver/fact_portfolios_full"   # inflection MODEL source partitions


def _at(art, key, date):
    idx = art["_idx"].get(date)
    if idx is None:
        return None
    arr = art.get(key)
    if arr is None or idx >= len(arr):
        return None
    return arr[idx]


def _bymodel_model_sum(art, date):
    """Sum of by_model model-cohort values at a date -> (sum_or_None, all_none). all_none=True when
    EVERY model cohort is None at this date (the model total is absent). A single cohort legitimately
    None (own launch depth) does not make the total absent -- only ALL-None does. This is the axis the
    by_model absent-leg-coalesced-to-zero defect lives on, which the value-only E1 identity cannot see."""
    bm = art.get("by_model") or {}
    idx = art["_idx"].get(date)
    if idx is None:
        return None, True
    vals = []
    for _k, v in bm.items():
        if v.get("cohort_class") != "model":
            continue
        series = v.get("model_value") or []
        vals.append(series[idx] if idx < len(series) else None)
    present = [x for x in vals if x is not None]
    all_none = (len(present) == 0)
    return (sum(present) if present else None), all_none


def check(arts, honest_none_dates=frozenset(), tol=TOL):
    """Pure B-basis invariant check. honest_none_dates = dates lineage-verified as source-absent
    (inflection model None AND eclipse partition absent) -> E2/E4 exempt there. Returns (verdict, holds, denom)."""
    comps = [f for f in arts if f != ROLLUP]
    g = arts[ROLLUP]
    holds = []
    n_checked = 0
    n_honest_none = 0
    for date in g["dates"]:
        head = _at(g, "opal_aggregate_aua", date)
        if head is None:
            # ALL-OR-NOTHING: a None-headline row must be FULLY None (model, non_model, and the
            # inflection_non_model_aua audit carrier). A partial row (headline None beside a populated
            # field) is the defect DS self-caught -- a populated non_model reads as real while the total
            # is a gap. My gate must catch it independently, not skip it.
            partial = [nm for nm, v in (("model_aua", _at(g, "model_aua", date)),
                                        ("non_model_aua", _at(g, "non_model_aua", date)),
                                        ("inflection_non_model_aua", _at(g, "inflection_non_model_aua", date)))
                       if v is not None]
            if partial:
                holds.append((date, "partial-row", f"headline None but {partial} populated -- must be all-or-nothing"))
            # A None headline is NEVER silently skipped: it must be a lineage-verified honest-None
            # (custody-only / feed-absent day, eclipse partition absent). Otherwise an unexplained None -> RED.
            if date in honest_none_dates:
                n_honest_none += 1
            else:
                holds.append((date, "headline-None-unverified",
                              "opal_aggregate None but NOT a lineage-verified honest-None (eclipse PRESENT or unchecked)"))
            continue
        exempt = date in honest_none_dates
        if exempt:
            n_honest_none += 1
        gmod = _at(g, "model_aua", date)
        gnm = _at(g, "non_model_aua", date)
        f49_nm = _at(arts[NONMODEL_FIRM], "non_model_aua", date) if NONMODEL_FIRM in arts else None
        inf_nm = _at(arts[COHORT2B_FIRM], "non_model_aua", date) if COHORT2B_FIRM in arts else None
        smod = 0.0
        model_missing = []
        for f in comps:
            m = _at(arts[f], "model_aua", date)
            if m is None:
                model_missing.append(f)
            else:
                smod += m
        n_checked += 1
        # E1 enterprise 2-term identity (global-internal; always checked when fields present)
        if gmod is not None and gnm is not None and abs(head - (gmod + gnm)) > tol:
            holds.append((date, "E1-2term", f"headline {head:,.2f} != model+non_model {gmod + gnm:,.2f} (d={head - (gmod + gnm):,.2f})"))
        # E2 model rollup -- EXEMPT on a lineage-verified honest-None date (inflection model legitimately absent)
        if not exempt and gmod is not None:
            if model_missing:
                holds.append((date, "E2-model-missing", f"model rollup blocked; {model_missing} model None (NOT a verified honest-None date)"))
            elif abs(gmod - smod) > tol:
                holds.append((date, "E2-model-rollup", f"global.model {gmod:,.2f} != SUM_firms.model {smod:,.2f} (d={gmod - smod:,.2f})"))
        # E3 non_model is 49F-only (catches a silent FOLD-IN); always checked
        if gnm is not None and f49_nm is not None and abs(gnm - f49_nm) > tol:
            folded = (inf_nm is not None and abs(gnm - (f49_nm + inf_nm)) <= tol)
            why = " (== FULL sum -- inflection non_model FOLDED IN; must be EXCLUDED per B)" if folded else ""
            holds.append((date, "E3-nonmodel-basis", f"global.non_model {gnm:,.2f} != 49F-only {f49_nm:,.2f} (d={gnm - f49_nm:,.2f}){why}"))
        # E4 cohort-2b carried (never silently DROPPED) -- EXEMPT on honest-None dates (legitimately None)
        if not exempt and inf_nm is None:
            holds.append((date, "E4-2b-dropped", f"{COHORT2B_FIRM} non_model absent on a NON-honest-None date -- cohort-2b dropped"))
    # E5 by_model ABSENCE-AGREEMENT (independent of E1: catches an absent firm-leg COALESCED-TO-ZERO in
    # by_model, which reads as a real per-model false-dip. E1's value identity is structurally blind to it
    # because opal_aggregate/model/non_model can all be individually correct while by_model is wrong.)
    n_absence = 0
    for fname, art in arts.items():
        if not art.get("by_model"):
            continue
        for date in art["dates"]:
            ma = _at(art, "model_aua", date)
            bm_sum, bm_all_none = _bymodel_model_sum(art, date)
            n_absence += 1
            if bm_all_none != (ma is None):     # absence limb -- EXACT, no tolerance
                holds.append((date, f"E5-absence[{fname}]",
                              f"by_model model-sum {'None' if bm_all_none else 'present'} but model_aua "
                              f"{'None' if ma is None else 'present'} -- absence DISAGREEMENT (coalesce-to-zero?)"))
            elif not bm_all_none and ma is not None and abs(bm_sum - ma) > tol:   # value limb -- rounding tol
                holds.append((date, f"E5-value[{fname}]",
                              f"sum(by_model model) {bm_sum:,.2f} != model_aua {ma:,.2f} (d={bm_sum - ma:,.2f})"))

    denom = {
        "component_firms": comps,
        "global_dates_total": len(g["dates"]),
        "dates_checked": n_checked,
        "honest_none_verified": n_honest_none,
        "absence_agreement_checks": n_absence,
    }
    verdict = "PASS" if not holds else "HOLD"
    return verdict, holds, denom


def _index(arts):
    for f in arts:
        arts[f]["_idx"] = {d: i for i, d in enumerate(arts[f]["dates"])}
    return arts


def _load_s3(served):
    import json

    import boto3
    s3 = boto3.client("s3", region_name="us-east-1")
    bucket = SERVED_B if served else STAGED_B
    arts = {}
    for f in FIRMS:
        if served:
            # RETIRED READ 2026-08-30 (3.0.0_SA_CVO): the legacy served mirror this gate compared
            # against is being deleted on Andrew's word (json/mdpf/{firm} card, DS~V 87745); the
            # served home moved 2026-08-19 @12b93b59ba to the dated gold path
            # portal/gold/mdpf/{firm}/aggregate-aua-timeseries/{D}.json (different vintage
            # semantics). This harness is the record of the P2F round; it REFUSES the served
            # branch rather than silently re-pointing.
            raise RuntimeError(
                "RETIRED 2026-08-30: the served-side read of this P2F gate targeted the legacy "
                "mirror, retired @12b93b59ba. Re-derive against the dated gold home before "
                "re-running with served=True.")
        key = f"gold/mdpf_revamp/{f}/aggregate_aua_timeseries.json"
        obj = s3.get_object(Bucket=bucket, Key=key)
        art = json.loads(obj["Body"].read())
        art["_etag"] = obj["ETag"].strip('"')[:12]
        arts[f] = art
    return _index(arts), bucket


def _lineage_honest_none(arts):
    """CVO lineage-verify leg: for every date the global headline (opal_aggregate) is None -- a
    candidate honest-None -- check the eclipse MODEL partition. Return {source-absent dates}
    (-> lineage-verified honest-None) and {present dates} (-> a None headline whose source EXISTS =
    a real producer gap, NOT honest-None -> RED). Reads live S3 -- this IS the verifier's job.
    Keyed on the headline (the gate-relevant axis), so a None the gate would otherwise skip is verified."""
    import boto3
    s3 = boto3.client("s3", region_name="us-east-1")
    g = arts[ROLLUP]
    cand = [d for d in g["dates"] if _at(g, "opal_aggregate_aua", d) is None]
    absent, present = set(), set()
    for d in cand:
        r = s3.list_objects_v2(Bucket=STAGED_B, Prefix=f"{ECLIPSE_MODEL_PREFIX}/date={d}/", MaxKeys=1)
        (absent if r.get("KeyCount", 0) == 0 else present).add(d)
    return absent, present


def _report(verdict, holds, denom, bucket, present_gap):
    print(f"source={bucket} (B-basis: non_model==49F-only; inflection cohort-2b EXCLUDED from headline)")
    print(f"DENOMINATOR: global_dates={denom['global_dates_total']} checked={denom['dates_checked']} "
          f"honest_none_verified={denom['honest_none_verified']} (eclipse-absent, lineage-checked) "
          f"absence_agreement_checks={denom['absence_agreement_checks']}")
    if present_gap:
        print(f"LINEAGE ALERT: {len(present_gap)} None-headline date(s) whose eclipse partition is PRESENT "
              f"(real gap, NOT honest-None -> already RED above): {sorted(present_gap)[:8]}")
    if denom["dates_checked"] == 0:
        print("ZERO DATES CHECKED -- coverage failure, NOT a pass.")
    by_kind = {}
    for _d, kind, _m in holds:
        by_kind[kind] = by_kind.get(kind, 0) + 1
    if holds:
        print(f"HOLD count={len(holds)}  by_kind={by_kind}")
        for date, kind, msg in holds[:8]:
            print(f"    HOLD {date} [{kind}] {msg}")
        if len(holds) > 8:
            print(f"    ... +{len(holds) - 8} more")
    print(f"\nGATE VERDICT: {verdict}"
          + ("  -- B-basis enterprise composition consistent; publish OK / no rollback"
             if verdict == "PASS"
             else "  -- BLOCK publish / rollback signal (B-basis violated)"))
    return verdict


def _selftest():
    dates = ["2025-01-02", "2025-01-03", "2025-01-06"]

    def firm(model, nonmodel):
        return {"dates": list(dates), "model_aua": list(model), "non_model_aua": list(nonmodel)}

    f49_m = [700.0, 710.0, 720.0]
    f49_nm = [200.0, 205.0, 210.0]     # under B this IS the headline non_model
    inf_m = [130.0, 131.0, 132.0]
    inf_nm = [60.0, 61.0, 62.0]        # inflection non_model = excluded cohort-2b (audit only)

    def build(global_nonmodel, inf_model=None, inf_nonmodel=None):
        im = inf_model if inf_model is not None else inf_m
        inm = inf_nonmodel if inf_nonmodel is not None else inf_nm
        gmod = [f49_m[i] + (im[i] or 0.0) for i in range(3)]
        gnm = list(global_nonmodel)
        head = [gmod[i] + gnm[i] for i in range(3)]
        arts = {
            "49financial": firm(f49_m, f49_nm),
            "inflection": firm(im, inm),
            "global": {"dates": list(dates), "model_aua": gmod, "non_model_aua": gnm, "opal_aggregate_aua": head},
        }
        return _index(arts)

    full = [f49_nm[i] + inf_nm[i] for i in range(3)]
    # CLEAN B
    v_clean, h_clean, _ = check(build(list(f49_nm)))
    ok_clean = (v_clean == "PASS" and not h_clean)
    # FOLD-IN (A artifact) -> RED on E3
    v_fold, h_fold, _ = check(build(full))
    ok_fold = (v_fold == "HOLD" and {d for d, k, _m in h_fold if k == "E3-nonmodel-basis"} == set(dates))
    # DROP inflection non_model on a NON-honest-None date -> RED on E4
    v_drop, h_drop, _ = check(build(list(f49_nm), inf_nonmodel=[None, None, None]))
    ok_drop = (v_drop == "HOLD" and {d for d, k, _m in h_drop if k == "E4-2b-dropped"} == set(dates))
    # HONEST-NONE: a custody-only / feed-absent day => global row FULLY None (all-or-nothing).
    hn_date = "2025-01-03"

    def build_hn(partial=False):
        a = build(list(f49_nm), inf_model=[130.0, None, 132.0], inf_nonmodel=[60.0, None, 62.0])
        j = a["global"]["_idx"][hn_date]
        a["global"]["opal_aggregate_aua"][j] = None
        a["global"]["model_aua"][j] = None
        if not partial:
            a["global"]["non_model_aua"][j] = None      # clean all-None honest-None row
        return a                                          # partial=True leaves non_model populated (the defect)

    # clean all-None + lineage-verified -> PASS, counted
    v_hn, h_hn, dn_hn = check(build_hn(), honest_none_dates={hn_date})
    ok_hn = (v_hn == "PASS" and dn_hn["honest_none_verified"] == 1 and not h_hn)
    # UNVERIFIED None headline (eclipse PRESENT, NOT in the set) -> RED, never silently skipped
    v_gap, h_gap, _ = check(build_hn(), honest_none_dates=frozenset())
    ok_gap = (v_gap == "HOLD" and any(d == hn_date and k == "headline-None-unverified" for d, k, _m in h_gap))
    # PARTIAL ROW (headline None beside a populated non_model) -> RED even on a verified honest-None date
    v_pr, h_pr, _ = check(build_hn(partial=True), honest_none_dates={hn_date})
    ok_pr = (v_pr == "HOLD" and any(d == hn_date and k == "partial-row" for d, k, _m in h_pr))

    # E5 by_model ABSENCE-AGREEMENT: a by_model model-leg coalesced-to-zero on a gap date -> RED (E1 is blind)
    gap = "2025-02-04"

    def build_bm(coalesce):
        dts = ["2025-02-03", gap]
        bm_d2 = 100.0 if coalesce else None    # coalesce=True: absent leg rendered as a value on the gap date
        gg = {"dates": list(dts), "model_aua": [300.0, None], "non_model_aua": [50.0, None],
              "opal_aggregate_aua": [350.0, None],
              "by_model": {"m1": {"cohort_class": "model", "model_value": [300.0, bm_d2]}}}
        f49 = {"dates": list(dts), "model_aua": [300.0, None], "non_model_aua": [50.0, None]}
        inf = {"dates": list(dts), "model_aua": [0.0, None], "non_model_aua": [0.0, None]}
        return _index({"global": gg, "49financial": f49, "inflection": inf})

    _vc, h_e5c, _ = check(build_bm(coalesce=False), honest_none_dates={gap})
    ok_e5_clean = not any(str(k).startswith("E5") for _d, k, _m in h_e5c)
    _vm, h_e5m, _ = check(build_bm(coalesce=True), honest_none_dates={gap})
    ok_e5_mut = any(d == gap and str(k).startswith("E5-absence") for d, k, _m in h_e5m)

    print(f"SELFTEST clean-B -> {v_clean} (expect PASS)                         : {'OK' if ok_clean else 'FAIL'}")
    print(f"SELFTEST FOLD-IN (A artifact, non_model=FULL) -> {v_fold} on E3      : {'OK' if ok_fold else 'FAIL'}")
    print(f"SELFTEST DROP cohort-2b (non-honest-None) -> {v_drop} on E4          : {'OK' if ok_drop else 'FAIL'}")
    print(f"SELFTEST honest-None VERIFIED (all-None, eclipse-absent) -> {v_hn}   : {'OK' if ok_hn else 'FAIL'}")
    print(f"SELFTEST None headline UNVERIFIED (eclipse present) -> {v_gap} (RED, not skipped): {'OK' if ok_gap else 'FAIL'}")
    print(f"SELFTEST PARTIAL ROW (None headline + populated non_model) -> {v_pr} (RED): {'OK' if ok_pr else 'FAIL'}")
    print(f"SELFTEST E5 by_model absence-agreement: clean no-E5={ok_e5_clean}; coalesce-to-zero -> E5-absence RED={ok_e5_mut}: {'OK' if (ok_e5_clean and ok_e5_mut) else 'FAIL'}")
    if not (ok_clean and ok_fold and ok_drop and ok_hn and ok_gap and ok_pr and ok_e5_clean and ok_e5_mut):
        print("SELFTEST FAILED -- do NOT trust the gate.")
        return 1
    print("SELFTEST OK -- GREEN clean-B + all-None honest-None; RED fold-in, drop, unverified None, partial row, by_model coalesce.")
    return 0


def main(argv):
    if "--selftest" in argv:
        return _selftest()
    served = "--served" in argv
    arts, bucket = _load_s3(served)
    absent, present = (frozenset(), frozenset()) if served else _lineage_honest_none(arts)
    verdict, holds, denom = check(arts, honest_none_dates=absent)
    _report(verdict, holds, denom, bucket, present)
    return 0 if (verdict == "PASS" and not present) else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
