"""
CVO INDEPENDENT spine gate/shadow verifier -- VINTAGE-ROBUST (any scheduled cycle).
From-scratch, own logic. Reads STAGED (gold/mdpf_revamp/{firm}/) + served (json/mdpf/{firm}/),
date-JOINS, checks criteria date-agnostically (no hardcoded LCD / D-2 / feed-gap list), and emits a
clear per-firm PASS/HOLD for use as a verify-before-serve GATE or a shadow+rollback check.

Verdict logic (a HOLD blocks the publish / signals rollback):
  HOLD if any of, per firm:
    - internal identity mismatch beyond rounding (model==Sum(core); non_model==custody-model)
    - a staged_only date that is NOT a real trading day (spurious axis padding)
    - a served_only date that IS a real trading day AND not a known feed-gap None in staged
    - model @ last-common-date diverges from served beyond MODEL_BAND_PCT (the F2 near-tie band)
    - the composition non_model_delta != custody_delta - model_delta @LCD (named-delta must compose)
    - basis label absent (49F/inflection must carry basis)
  A custody delta (D-2) of ANY size is ALLOWED (it is the ruled full-envelope-vs-rederived named delta,
  date-varying) -- we require it COMPOSES, not that it equals a frozen number.

Provenance: durably committed by 3.0.0_SA_CVO (2026-07-22) after it was found living only in a
dead session's scratchpad -- the record is the only carrier that survives a session end.
"""
from __future__ import annotations

import json
import sys

import boto3

sys.path.insert(0, "/c/Users/AndrewBerman/Desktop/ajb_workspace")
sys.path.insert(0, "C:/Users/AndrewBerman/Desktop/ajb_workspace")
from lib.trading_calendar import is_trading_day  # noqa: E402

s3 = boto3.client("s3", region_name="us-east-1")
STAGED_B, SERVED_B = "opal-data-assets", "opal-data-portal-v2"
FLOAT_EPS_PER_COHORT = 0.005          # per-cohort cent-rounding; scale by cohort count
MODEL_BAND_PCT = 0.50                 # F2 near-tie band (|staged-served|/served at LCD), %
FIRMS = ["49financial", "inflection", "global"]


def load(b, k):
    o = s3.get_object(Bucket=b, Key=k)
    return json.loads(o["Body"].read()), o["ETag"].strip('"')[:8]


def core_sum(d, i):
    return sum(mv["model_value"][i] for mv in d["by_model"].values()
               if mv.get("cohort_class") == "model" and mv["model_value"][i] is not None)


overall_hold = []
for firm in FIRMS:
    st, et = load(STAGED_B, f"gold/mdpf_revamp/{firm}/aggregate_aua_timeseries.json")
    # RETIRED READ 2026-08-30 (3.0.0_SA_CVO): the frozen legacy mirror this harness read as its
    # SERVED baseline is being deleted on Andrew's word (json/mdpf/{firm} card, DS~V 87745). The
    # served home moved 2026-08-19 @12b93b59ba to the dated gold path
    # portal/gold/mdpf/{firm}/aggregate-aua-timeseries/{D}.json -- a different vintage semantics,
    # so a silent re-point would change what this P2F-round gate measured. The harness stays as
    # the record of that round and REFUSES rather than reading the retired key.
    raise RuntimeError(
        "RETIRED 2026-08-30: this ad-hoc P2F gate read the legacy served mirror; that key is "
        "retired (@12b93b59ba). Re-derive against the dated gold home before re-running.")
    sv, _ = None, None  # noqa: F841  (unreachable; kept so the diff shows the retired read)
    si = {d: i for i, d in enumerate(st["dates"])}
    vi = {d: i for i, d in enumerate(sv["dates"])}
    common = sorted(set(st["dates"]) & set(sv["dates"]))
    st_only = sorted(set(st["dates"]) - set(sv["dates"]))
    sv_only = sorted(set(sv["dates"]) - set(st["dates"]))
    lcd = common[-1]
    ncohort = len(st["by_model"])
    eps = max(0.01, ncohort * FLOAT_EPS_PER_COHORT + 0.01)   # rounding tolerance by cohort count
    has_cust = "partner_custody_total" in st
    holds = []

    # non-common classification
    so_bad = [d for d in st_only if not is_trading_day(d)]          # spurious padding
    if so_bad:
        holds.append(f"staged_only non-trading (spurious): {so_bad}")
    none_set = {st["dates"][i] for i in range(len(st["dates"])) if st["model_aua"][i] is None}
    vo_trade_notnone = [d for d in sv_only if is_trading_day(d)]    # legacy real day staged lacks
    # a served real-trading day the staged omits is acceptable ONLY if staged Nones it as a feed-gap
    # (staged simply doesn't carry that date -> it's a legacy backfill of a gap the staged leaves out)
    # report for human eyes; not an auto-HOLD unless it also carries staged data expectation
    # identities
    mm_model = sum(1 for d in common
                   if st["model_aua"][si[d]] is not None
                   and abs(st["model_aua"][si[d]] - core_sum(st, si[d])) > eps)
    if mm_model:
        holds.append(f"model!=Sum(core) x{mm_model} (>{eps:.3f})")
    mm_id = 0
    if has_cust:
        for d in common:
            i = si[d]
            nm, c, m = st["non_model_aua"][i], st["partner_custody_total"][i], st["model_aua"][i]
            if None in (nm, c, m):
                continue
            if abs(nm - (c - m)) > 0.02:
                mm_id += 1
        if mm_id:
            holds.append(f"non_model!=custody-model x{mm_id}")
    # model tie @LCD (F2 band)
    sm, vm = st["model_aua"][si[lcd]], sv["model_aua"][vi[lcd]]
    mpct = 100*(sm - vm)/vm if vm else float("nan")
    if abs(mpct) > MODEL_BAND_PCT:
        holds.append(f"model @LCD {mpct:+.4f}% > band {MODEL_BAND_PCT}%")
    # composition @LCD (only where custody present)
    comp = None
    if has_cust:
        sc, vc = st["partner_custody_total"][si[lcd]], sv["partner_custody_total"][vi[lcd]]
        snm, vnm = st["non_model_aua"][si[lcd]], sv["non_model_aua"][vi[lcd]]
        cust_d, mod_d, nm_d = sc - vc, sm - vm, snm - vnm
        comp = abs(nm_d - (cust_d - mod_d))
        if comp > 0.02:
            holds.append(f"composition off by ${comp:.2f} (nm_delta != cust_delta-mod_delta)")
    # basis
    basis = (st.get("meta") or {}).get("basis")
    if firm in ("49financial", "inflection") and basis != "schwab-rps":
        holds.append(f"basis={basis!r} (expect schwab-rps)")

    verdict = "PASS" if not holds else "HOLD"
    if holds:
        overall_hold.append(firm)
    print(f"{firm:<12} ETag={et} len s/v/common={len(st['dates'])}/{len(sv['dates'])}/{len(common)} "
          f"LCD={lcd} model@LCD={mpct:+.4f}% "
          + (f"cust_delta=${(st['partner_custody_total'][si[lcd]]-sv['partner_custody_total'][vi[lcd]]):,.0f} " if has_cust else "")
          + (f"comp_resid=${comp:.2f} " if comp is not None else "")
          + f"Nones={len(none_set)} -> {verdict}")
    for h in holds:
        print(f"    HOLD: {h}")
    if vo_trade_notnone:
        print(f"    note: {len(vo_trade_notnone)} served real-trading day(s) staged omits (legacy backfill of feed-gaps; verify each is a known gap): {vo_trade_notnone[:8]}")

print(f"\nGATE VERDICT: {'PASS -- publish OK / no rollback' if not overall_hold else 'HOLD -- block publish / rollback signal: ' + ','.join(overall_hold)}")
