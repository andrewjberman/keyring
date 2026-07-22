"""
CVO Layer-3 ENTERPRISE-COMPOSITION gate -- from-scratch, independent (MDPF re-flip hard gate).

The class this catches (that a PARITY check cannot): a component silently excluded from the
Global enterprise headline. parity != consistency -- a hole present on BOTH served + published
sides passes a staged-vs-served parity check clean. This gate re-derives the enterprise total
from COMPONENTS, by construction, so an excluded firm/cohort surfaces as a per-date mismatch
regardless of what the producer emits or a parity check says.

Incident: the coherent-9 that passed the 3-pass parity (global aggregate ETag 1b52211f) carried
Global opal_aggregate_aua = model + (49financial non_model ONLY), dropping inflection non_model on
ALL 421 headline dates (~$151M-$203M/date, ~$153M @2025-04-30). Andrew caught it post-flip -> the
flip rolled back. My prior gate checked model/non_model/custody but NEVER read opal_aggregate_aua.

INVARIANTS checked per date, over the FULL series (a HOLD blocks publish / signals rollback):
  I1  enterprise 2-term identity      : global.opal_aggregate_aua == global.model_aua + global.non_model_aua
  I2  independent component re-derive  : global.opal_aggregate_aua == SUM_component_firms(model_aua + non_model_aua)
  I3  model rollup                     : global.model_aua       == SUM_component_firms(model_aua)
  I4  non_model rollup                 : global.non_model_aua   == SUM_component_firms(non_model_aua)
I2 is the load-bearing catch: it rebuilds the total from the component firm artifacts and trusts NO
global field except the headline under test, so it fires even if global.non_model were ALSO corrupted.

Modes:
  (default)     read STAGED  s3://opal-data-assets/gold/mdpf_revamp/{firm}/aggregate_aua_timeseries.json
  --served      read SERVED  s3://opal-data-portal-v2/json/mdpf/{firm}/aggregate-aua-timeseries.json
  --selftest    in-memory clean+mutant assertions (NO S3): clean -> PASS, seeded-hole -> HOLD.
                An instrument that cannot fail the known-bad case is not an instrument -- run this first.

Provenance: 3.0.0_SA_CVO, 2026-07-22. Layer 3 of the DS-producer / DT-harness / CVO-rederive defense-in-depth.
"""
from __future__ import annotations

import sys

TOL = 1.00              # $ absolute; real holes are $151M+, a fixed artifact reconciles to the cent
ROLLUP = "global"
FIRMS = ["49financial", "inflection", "global"]
STAGED_B = "opal-data-assets"
SERVED_B = "opal-data-portal-v2"


def _at(art, key, date):
    idx = art["_idx"].get(date)
    if idx is None:
        return None
    arr = art.get(key)
    if arr is None or idx >= len(arr):
        return None
    return arr[idx]


def check(arts, tol=TOL):
    """Pure invariant check over loaded firm dicts. Returns (verdict, holds, denom)."""
    comps = [f for f in arts if f != ROLLUP]
    g = arts[ROLLUP]
    holds = []
    n_checked = 0
    n_skip_headline = 0
    n_skip_comp = 0
    for date in g["dates"]:
        head = _at(g, "opal_aggregate_aua", date)
        if head is None:
            n_skip_headline += 1
            continue
        gmod = _at(g, "model_aua", date)
        gnm = _at(g, "non_model_aua", date)
        smod = 0.0
        snm = 0.0
        missing = []
        for f in comps:
            m = _at(arts[f], "model_aua", date)
            nm = _at(arts[f], "non_model_aua", date)
            if m is None or nm is None:
                missing.append(f)
            else:
                smod += m
                snm += nm
        if missing:
            n_skip_comp += 1
            holds.append((date, "component-missing", f"cannot re-derive; missing {missing}"))
            continue
        n_checked += 1
        # I1 enterprise 2-term identity
        if gmod is not None and gnm is not None and abs(head - (gmod + gnm)) > tol:
            holds.append((date, "I1-2term", f"headline {head:,.2f} != model+non_model {gmod + gnm:,.2f} (d={head - (gmod + gnm):,.2f})"))
        # I2 independent component re-derive (load-bearing)
        if abs(head - (smod + snm)) > tol:
            holds.append((date, "I2-components", f"headline {head:,.2f} != SUM_firms(model+non_model) {smod + snm:,.2f} (d={head - (smod + snm):,.2f})"))
        # I3 model rollup
        if gmod is not None and abs(gmod - smod) > tol:
            holds.append((date, "I3-model-rollup", f"global.model {gmod:,.2f} != SUM_firms.model {smod:,.2f} (d={gmod - smod:,.2f})"))
        # I4 non_model rollup
        if gnm is not None and abs(gnm - snm) > tol:
            holds.append((date, "I4-nonmodel-rollup", f"global.non_model {gnm:,.2f} != SUM_firms.non_model {snm:,.2f} (d={gnm - snm:,.2f})"))
    denom = {
        "component_firms": comps,
        "global_dates_total": len(g["dates"]),
        "dates_checked": n_checked,
        "skipped_headline_none": n_skip_headline,
        "skipped_component_missing": n_skip_comp,
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
        key = (f"json/mdpf/{f}/aggregate-aua-timeseries.json" if served
               else f"gold/mdpf_revamp/{f}/aggregate_aua_timeseries.json")
        obj = s3.get_object(Bucket=bucket, Key=key)
        art = json.loads(obj["Body"].read())
        art["_etag"] = obj["ETag"].strip('"')[:12]
        arts[f] = art
    return _index(arts), bucket


def _report(verdict, holds, denom, bucket):
    print(f"source={bucket}  component_firms={denom['component_firms']}")
    print(f"DENOMINATOR: global_dates={denom['global_dates_total']} "
          f"checked={denom['dates_checked']} "
          f"skipped(headline_none={denom['skipped_headline_none']}, "
          f"component_missing={denom['skipped_component_missing']})")
    if denom["dates_checked"] == 0:
        print("ZERO DATES CHECKED -- coverage failure, NOT a pass.")
    by_kind = {}
    for _d, kind, _msg in holds:
        by_kind[kind] = by_kind.get(kind, 0) + 1
    if holds:
        print(f"HOLD count={len(holds)}  by_kind={by_kind}")
        for date, kind, msg in holds[:8]:
            print(f"    HOLD {date} [{kind}] {msg}")
        if len(holds) > 8:
            print(f"    ... +{len(holds) - 8} more")
    print(f"\nGATE VERDICT: {verdict}"
          + ("  -- enterprise composition consistent; publish OK / no rollback"
             if verdict == "PASS"
             else "  -- BLOCK publish / rollback signal (enterprise excludes a component)"))
    return verdict


def _selftest():
    dates = ["2025-01-02", "2025-01-03", "2025-01-06"]

    def firm(model, nonmodel):
        a = {"dates": list(dates), "model_aua": list(model), "non_model_aua": list(nonmodel)}
        return a

    f49_m = [700.0, 710.0, 720.0]
    f49_nm = [200.0, 205.0, 210.0]
    inf_m = [0.0, 0.0, 0.0]
    inf_nm = [150.0, 151.0, 152.0]

    def build(global_headline):
        gmod = [f49_m[i] + inf_m[i] for i in range(3)]
        gnm = [f49_nm[i] + inf_nm[i] for i in range(3)]
        arts = {
            "49financial": firm(f49_m, f49_nm),
            "inflection": firm(inf_m, inf_nm),
            "global": {"dates": list(dates), "model_aua": gmod, "non_model_aua": gnm,
                       "opal_aggregate_aua": global_headline},
        }
        return _index(arts)

    # CLEAN: headline = model + FULL non_model
    clean_head = [f49_m[i] + inf_m[i] + f49_nm[i] + inf_nm[i] for i in range(3)]
    v_clean, h_clean, _ = check(build(clean_head))
    # MUTANT: headline drops inflection non_model (the exact incident defect)
    mut_head = [f49_m[i] + inf_m[i] + f49_nm[i] for i in range(3)]
    v_mut, h_mut, _ = check(build(mut_head))

    ok_clean = (v_clean == "PASS" and not h_clean)
    mut_dates = {d for d, _k, _m in h_mut}
    ok_mut = (v_mut == "HOLD" and mut_dates == set(dates))
    print(f"SELFTEST clean -> {v_clean} (expect PASS, holds={len(h_clean)})  : {'OK' if ok_clean else 'FAIL'}")
    print(f"SELFTEST mutant(drop inflection non_model) -> {v_mut} on {len(mut_dates)}/3 dates "
          f"(expect HOLD on 3/3)  : {'OK' if ok_mut else 'FAIL'}")
    if not (ok_clean and ok_mut):
        print("SELFTEST FAILED -- the gate does not discriminate; do NOT trust it.")
        return 1
    print("SELFTEST OK -- gate REDs the known-bad case and GREENs the clean case.")
    return 0


def main(argv):
    if "--selftest" in argv:
        return _selftest()
    served = "--served" in argv
    arts, bucket = _load_s3(served)
    verdict, holds, denom = check(arts)
    _report(verdict, holds, denom, bucket)
    return 0 if verdict == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
