"""IRPT_DASHBD round 88, TO-DB-b-166: the flow-timing tie-out decided by computing both conventions over the stored set.

Reads worker 108's STORED tables only, by path: members90.pkl, read90.pkl and table90.pkl in the private evidence folder
C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/. No S3, no vendor call, no secret read, no
write to any served location. Prints COUNTS ONLY and writes the same counts to the private folder of worker ~132.
Usage: python -I tieout_flow_timing.py

Conventions (a reconciliation convention only; served values never change):
  end         every flow at the END of its day: r_t = (V_t - F_t) / V_(t-1) - 1 (the served behaviour).
  bd_default  Black Diamond's published default (learn.bdreporting.com article/97): a flow day with F_t > 0 is linked at
              START, r_t = V_t / (V_(t-1) + F_t) - 1; a flow day with F_t zero or negative is linked at END, as above.
  start       CONTROL ONLY (the reader of record's START convention; never an input to the verdict): every flow day at START.

Rules carried over unchanged from flowtime_count.py (~127) and the reader of record (tieout/tieout_reader.py):
  day set     the days inside [start, end] that carry a served return r (the same set ~127's relink uses).
  first day   keeps its served return, EXCEPT under start, where the reader's FIRST_DAY_FLOW_AT_START predicate applies
              (flow at least 25 pct of the served value before the segment, START denominator clears the guard).
              The predicate is counted below; it is not applied under end or bd_default.
  missing     a day whose own or previous market value is missing or zero, or whose flow is None, keeps its served return.
  guard       a START-linked flow day (F_t non-zero) whose denominator V_(t-1) + F_t is below GUARD_FRAC (2 pct) of
              |V_(t-1)| keeps its served return (the reader's rule). A START denominator of exactly zero keeps it too (~127).
  gross       (1 + bdr) * (1 + fees / mean) - 1, with mean the stored segment mean market value (~127's fee base); a zero
              fee adds nothing (the reader's rule for a missing fee). The reader's BD_FEE_FIELD_IS_FLOW predicate is
              counted below; the module stops if it ever fires, because that branch is not implemented here.
  tolerance   a segment closes under a convention when |gross - relinked| * 100 <= TOL_PP (0.35 pp).

Population: FLOW-BEARING (a served flow is non-zero on some day inside the segment) and GRADABLE (the stored BD figure
and the stored fee are present). The contested 51 are the member list in members90.pkl.
Declared rule (fixed before the count): BD_DEFAULT iff only_end == 0 and only_bd_default >= 1; END iff only_bd_default == 0
and only_end >= 1; BOTH_TIE_INDISTINGUISHABLE iff only_bd_default == 0 and only_end == 0; MIXED_NEITHER_DECIDES otherwise.
"""
import json
import pickle
import sys

PRIVATE = "C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/"
STORED = PRIVATE + "0.9.0_WK_IRPT_DASHBD~108/"
OUT = PRIVATE + "0.9.0_WK_IRPT_DASHBD~132/"
TOL_PP = 0.35
GUARD_FRAC = 0.02
LARGE_FLOW = 0.25
FEE_IS_FLOW_ABS, FEE_IS_FLOW_REL = 1.0, 0.002
CONVENTIONS = ("end", "bd_default", "start")


def load(name):
    with open(STORED + name, "rb") as fh:
        return pickle.load(fh)


def first_day_start(day0, prior_mv):
    """The reader's FIRST_DAY_FLOW_AT_START predicate: the START return of the segment's first day, or None when it does not hold."""
    f, v1 = day0.get("flow"), day0.get("mv")
    if not prior_mv or prior_mv <= 0 or not f or v1 is None:
        return None
    if abs(f) < LARGE_FLOW * prior_mv or not (prior_mv + f >= GUARD_FRAC * prior_mv):
        return None
    return v1 / (prior_mv + f) - 1.0


def link_day(conv, v0, v1, flow, served):
    """Return of one day with previous value v0, value v1 and flow; `served` when the day keeps its served return."""
    if conv == "end" or (conv == "bd_default" and flow <= 0):
        return (v1 - flow) / v0 - 1.0
    den = v0 + flow
    if flow != 0 and not den >= GUARD_FRAC * abs(v0):
        return served
    return v1 / den - 1.0 if den else served


def relink(days, conv, prior_mv):
    """Compounded segment return under one convention. days: the segment's served days in date order."""
    p = 1.0
    for i, d in enumerate(days):
        if i == 0:
            r = d["r"]
            if conv == "start":
                s = first_day_start(d, prior_mv)
                if s is not None:
                    r = s
        elif not d.get("mv") or not days[i - 1].get("mv") or d.get("flow") is None:
            r = d["r"]
        else:
            r = link_day(conv, days[i - 1]["mv"], d["mv"], d["flow"], d["r"])
        p *= 1.0 + r
    return p - 1.0


def fee_field_is_flow(fees, nadd):
    """The reader's BD_FEE_FIELD_IS_FLOW predicate: fees negative and equal to minus net additions (within the reader's tolerance)."""
    return fees is not None and nadd is not None and fees < 0 and abs(fees + nadd) <= max(FEE_IS_FLOW_ABS, FEE_IS_FLOW_REL * abs(nadd))


def crosstab(items):
    c = {"both": 0, "only_bd_default": 0, "only_end": 0, "neither": 0}
    for closes in items:
        a, e = closes["bd_default"], closes["end"]
        key = "both" if (a and e) else "only_bd_default" if a else "only_end" if e else "neither"
        c[key] += 1
    return c


def verdict_of(c):
    a, e = c["only_bd_default"], c["only_end"]
    if e == 0 and a >= 1:
        return "BD_DEFAULT"
    if a == 0 and e >= 1:
        return "END"
    if a == 0 and e == 0:
        return "BOTH_TIE_INDISTINGUISHABLE"
    return "MIXED_NEITHER_DECIDES"


def main():
    contested = set(load("members90.pkl")["FLOW_TIMING_CONVENTION_DOLLARS_TIE"])
    read = load("read90.pkl")
    rows = load("table90.pkl")
    gold = read["gold"]
    n_total, n_noflow, n_nofig, n_fee_flow, n_first = len(rows), 0, 0, 0, 0
    pop = []   # (is_contested, closes-by-convention)
    for r in rows:
        acct, seg, o, b, v = r["a"], r["seg"], r["o"], r["b"], r["v2"]
        series = gold[acct]
        window = [d for d in sorted(series) if seg["start"] <= d <= seg["end"]]
        if not any(series[d]["flow"] for d in window):
            n_noflow += 1
            continue
        if v.get("bdr") is None or b.get("fees") is None or o.get("mean") is None:
            n_nofig += 1
            continue
        days = [series[d] for d in window if series[d]["r"] is not None]
        before = [d for d in series if d < seg["start"]]
        prior_mv = series[max(before)].get("mv") if before else None
        if days and first_day_start(days[0], prior_mv) is not None:
            n_first += 1
        if fee_field_is_flow(b["fees"], b.get("nadd")):
            n_fee_flow += 1
        base = o["mean"]
        add = b["fees"] / base if base > 0 else 0.0
        gross = (1.0 + v["bdr"]) * (1.0 + add) - 1.0
        closes = {c: abs(gross - relink(days, c, prior_mv)) * 100.0 <= TOL_PP for c in CONVENTIONS}
        pop.append((r["idx"] in contested, closes))
    if n_fee_flow:
        print("STOP: the BD_FEE_FIELD_IS_FLOW predicate fired on %d segment(s); that branch is not implemented here" % n_fee_flow)
        sys.exit(2)
    flow_items = [c for _, c in pop]
    contested_items = [c for is51, c in pop if is51]
    cf, c51 = crosstab(flow_items), crosstab(contested_items)
    controls = {"start_within_contested_51": sum(1 for c in contested_items if c["start"]),
                "end_within_contested_51": sum(1 for c in contested_items if c["end"])}
    verdict = verdict_of(cf)
    negative_arm = {"BD_DEFAULT": cf["only_bd_default"] >= 1, "END": cf["only_end"] >= 1}.get(verdict, False)
    res = {"segments_total": n_total, "no_flow_segments": n_noflow, "no_figure_segments": n_nofig,
           "flow_segments": len(flow_items), "contested_in_population": len(contested_items),
           "crosstab_flow": cf, "crosstab_contested_51": c51, "controls": controls, "verdict": verdict,
           "negative_arm": negative_arm, "first_day_start_predicate_fired": n_first, "fee_field_predicate_fired": n_fee_flow}
    print("segments_total %d; no_flow %d; no_figure %d; flow_segments (flow-bearing and gradable) %d; contested in population %d of %d" % (
        n_total, n_noflow, n_nofig, len(flow_items), len(contested_items), len(contested)))
    print("crosstab_flow %s (sum %d)" % (json.dumps(cf, sort_keys=True), sum(cf.values())))
    print("crosstab_contested_51 %s (sum %d)" % (json.dumps(c51, sort_keys=True), sum(c51.values())))
    print("controls %s" % json.dumps(controls, sort_keys=True))
    print("verdict %s; negative_arm %s" % (verdict, str(negative_arm).lower()))
    print("predicates fired: first_day_start %d; fee_field_is_flow %d" % (n_first, n_fee_flow))
    with open(OUT + "flow_timing_counts.json", "w") as fh:
        json.dump(res, fh, sort_keys=True)
    print("OK: counts written to the private folder")


if __name__ == "__main__":
    main()
