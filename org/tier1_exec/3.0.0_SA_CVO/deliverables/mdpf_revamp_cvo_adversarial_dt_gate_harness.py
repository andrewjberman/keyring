"""
CVO adversarial-verify harness for DT's internal-consistency gate (mdpf_parity_check.py --consistency).
Evidence for the ACCEPTED-CVO verdict (2026-07-22): a GENERATED boundary/edge sweep (measures the
INSTRUMENT, not DT's hand-picked mutants) + a live staged-vs-served look at the 3 PARTIAL_NULL dates +
an independent median. Imports DT's own pure comparators so the attack hits the real code path.

Run: python mdpf_revamp_cvo_adversarial_dt_gate_harness.py   (read-only S3; verifier-not-doer)
"""
from __future__ import annotations

import copy
import json
import statistics
import sys

import boto3

sys.path.insert(0, "C:/Users/AndrewBerman/Desktop/ajb_workspace/org/tier2_senior/0.2.0_DT_PortfolioAnalytics/deliverables")
import mdpf_parity_check as G  # noqa: E402

s3 = boto3.client("s3", region_name="us-east-1")


def load(bucket, key):
    return json.loads(s3.get_object(Bucket=bucket, Key=key)["Body"].read())


def _caught(base, hole):
    m = copy.deepcopy(base)
    m["opal_aggregate_aua"] = [t - hole for t in m["opal_aggregate_aua"]]
    v, _ = G._consistency_violations(m)
    return bool(v)


def q1_q2_boundary():
    print("Q1/Q2 -- GENERATED tolerance-boundary sweep (measures the INSTRUMENT):")
    base = {"dates": ["d1", "d2", "d3"], "opal_aggregate_aua": [300.0, 400.0, 500.0],
            "model_aua": [200.0, 250.0, 300.0], "non_model_aua": [100.0, 150.0, 200.0]}
    for h in [0.001, 0.5, 0.99, 0.999, 1.0, 1.001, 1.01, 2.0, 100.0]:
        print(f"  hole ${h:>8}: {'RED (caught)' if _caught(base, h) else 'green (ignored)'}")
    print(f"  total OVERSTATED -$1000000: {'RED' if _caught(base, -1_000_000.0) else 'MISS'}")
    # inputs DT did not hand-pick
    mnan = copy.deepcopy(base)
    mnan["non_model_aua"][1] = float("nan")
    vnan, snan = G._consistency_violations(mnan)
    print(f"  NaN non_model @d2: viol={len(vnan) if vnan else 0} checked={snan['checked']} -> "
          f"{'MISS -- BLIND SPOT (abs(nan)>tol is False)' if not vnan else 'caught'}")
    minf = copy.deepcopy(base)
    minf["non_model_aua"][1] = float("inf")
    vinf, _ = G._consistency_violations(minf)
    print(f"  inf non_model @d2: {'RED (caught)' if vinf else 'MISS'}")
    mcomp = copy.deepcopy(base)
    mcomp["model_aua"] = [x + 50.0 for x in mcomp["model_aua"]]
    mcomp["non_model_aua"] = [x - 50.0 for x in mcomp["non_model_aua"]]
    vcomp, _ = G._consistency_violations(mcomp)
    print(f"  compensating (model+50/non_model-50): per-firm identity "
          f"{'RED' if vcomp else 'green -- MISSES by design (cross-firm needed)'}")


def q4_partial_null():
    print("\nQ4 -- 3 inflection PARTIAL_NULL dates: STAGED vs SERVED:")
    st = load("opal-data-assets", "gold/mdpf_revamp/inflection/aggregate_aua_timeseries.json")
    # RETIRED READ 2026-08-30 (3.0.0_SA_CVO): the legacy served mirror this Q4 probe read is being
    # deleted on Andrew's word (json/mdpf/{firm} card, DS~V 87745); the served home moved
    # 2026-08-19 @12b93b59ba to portal/gold/mdpf/{firm}/aggregate-aua-timeseries/{D}.json with
    # different vintage semantics. This harness is the record of the P2F adversarial round and
    # REFUSES rather than silently re-pointing.
    raise RuntimeError(
        "RETIRED 2026-08-30: Q4's served-side read targeted the legacy mirror, retired "
        "@12b93b59ba. Re-derive against the dated gold home before re-running.")
    sv = None  # noqa: F841  (unreachable; kept so the diff shows the retired read)

    def at(a, key, d):
        di = {x: i for i, x in enumerate(a["dates"])}
        i = di.get(d)
        if i is None:
            return "ABSENT-DATE"
        arr = a.get(key)
        return arr[i] if (arr and i < len(arr)) else None

    for d in ["2026-05-21", "2026-06-01", "2026-07-01"]:
        print(f"  {d}:")
        print(f"    STAGED: custody={at(st, 'partner_custody_total', d)!r} "
              f"model={at(st, 'model_aua', d)!r} non_model={at(st, 'non_model_aua', d)!r}")
        print(f"    SERVED: custody={at(sv, 'partner_custody_total', d)!r} "
              f"model={at(sv, 'model_aua', d)!r} non_model={at(sv, 'non_model_aua', d)!r}")


def median_hole():
    print("\nmedian hole (staged global):")
    g = load("opal-data-assets", "gold/mdpf_revamp/global/aggregate_aua_timeseries.json")
    holes = []
    for i in range(len(g["dates"])):
        t, m, n = g["opal_aggregate_aua"][i], g["model_aua"][i], g["non_model_aua"][i]
        if None in (t, m, n):
            continue
        holes.append((m + n) - t)
    holes.sort()
    print(f"  n={len(holes)} min=${holes[0]:,.2f} median=${statistics.median(holes):,.2f} max=${holes[-1]:,.2f}")


if __name__ == "__main__":
    q1_q2_boundary()
    q4_partial_null()
    median_hole()
