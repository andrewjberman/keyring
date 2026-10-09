"""The tie-out READER OF RECORD of IRPT_DASHBD (round 32, TO-DB-b-60 / TO-DB-b-61): the 49F-vs-Black-Diamond tie-out of served
account_return_daily, GROSS and COMPOUNDED, with the daily-mean fee base. Project-owned reconciliation code; nothing here is served,
deployed or written to S3. READ-ONLY: S3 GETs/LISTs only; zero vendor calls.

Promoted from round 31's tieout_compound_v2.py (~35, DB-b-57). This module is the ONE definition of the daily-mean fee base
(daily_mean_value, fee_addback_v2, fee_base_gross); the round 31 modules IMPORT it and define none of those names.
Round 18's and round 30's readers are imported for what v2 did not change: the not-gradable paths, the reason set, the tolerance, the tally
and the compounding (1 + net) * (1 + add_back) - 1.

Gross: BD gross = (1 + bd_net_twr) * (1 + fees / daily_mean_value) - 1; mean of the POSITIVE served market_value_eod over the segment's linked
days. A segment with no fee, or with no positive daily value, keeps round 30's add-back.

FLOW_CONVENTION is the reader's daily re-link convention (a reconciliation convention only; served values never change):
  "end"   the served behaviour: the segment is linked from the served total_return_daily (external flow at the END of its day).
  "start" a flow day's external flow is invested for that day: r = V_t / (V_(t-1) + F_t) - 1 (round 17's link_alt_flow START, used as it is;
          the segment's first day keeps its served return). GUARD (stated rule, never a silent fill): the START denominator
          V_(t-1) + F_t must be at least GUARD_FRAC (1%) of |V_(t-1)|; a day below that (a flow of about -100% of the prior value, or more)
          is NOT re-linked: it keeps its served return, and the day is counted in the row's `guard_days` and in the record.

Usage: python tieout_reader.py <repo_root> [--cache <pickle>] [--flow end|start] --record <REGRADE_*.json> [--prior <REGRADE_E1.json>]
Writes the record (segments, within, reader_sha256, files_read[, in_to_out]) and, beside it, a COUNTS-ONLY .md.
"""
import hashlib
import importlib.util
import json
import pickle
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROJ = HERE.parent
R30_PATH = PROJ / "deliverables" / "0.9.0_WK_IRPT_DASHBD~34" / "tieout_compound.py"
_spec = importlib.util.spec_from_file_location("tieout_compound_r30", str(R30_PATH))
r30 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(r30)
r18 = r30.r18
r17 = r30.r17
TOLERANCE_PP = r30.TOLERANCE_PP
FLOW_CONVENTION = "end"
GUARD_FRAC = 0.01
LARGE_FLOW = 0.25
FILES_READ = {"reader_of_record": "org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_reader.py",
              "round17_reader": "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~12/tieout_e2.py",
              "round18_reader": "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~13/tieout_e2_gross.py",
              "round30_reader": "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~34/tieout_compound.py",
              "plan": r17.PLAN_REL}


# ----------------------------------------------------------------------------------------------------------------- the fee base (ONE writer)
def daily_mean_value(days, positive_only=True):
    """Mean of the positive served market_value_eod over the linked days; None when there is none. positive_only=False keeps every non-zero
    value, negative ones included: round 31's classifier (~36) formed its mean that way, and its recorded output is kept by calling it so."""
    mvs = [d["mv"] for d in days if d.get("mv") and (d["mv"] > 0 or not positive_only)]
    return sum(mvs) / len(mvs) if mvs else None


def fee_addback_v2(bd, days):
    """(fees_reported, addback): fees / daily-mean value; round 30's add-back when there is no fee or no daily value."""
    fees = bd.get("fees")
    base = daily_mean_value(days)
    if not fees or base is None:
        return r18.fee_addback(bd)
    return fees, fees / base


def fee_base_gross(bd_net, fees, days, positive_only=True):
    """BD gross, compounded, with the fee add-back formed on the daily-mean value over the linked days:
    (1 + net) * (1 + fees / daily mean) - 1. No fee, or no positive daily mean: the net as it is (as round 30 does)."""
    avg = daily_mean_value(days, positive_only)
    if not fees or not avg or avg <= 0:
        return bd_net
    return (1.0 + bd_net) * (1.0 + fees / avg) - 1.0


# ----------------------------------------------------------------------------------------------------------------- the daily re-link
def guarded_days(days):
    """Indices (>= 1) of the flow-bearing days whose START denominator V_(t-1) + F_t is below GUARD_FRAC of |V_(t-1)|."""
    out = []
    for i in range(1, len(days)):
        v0, f = days[i - 1].get("mv"), days[i].get("flow")
        if v0 and f is not None and f != 0 and not (v0 + f >= GUARD_FRAC * abs(v0)):
            out.append(i)
    return out


def opal_link(days, flow):
    """(opal_return, guard_day_indices) under the flow convention. A guarded day is handed to round 17's link_alt_flow with flow None,
    which keeps that day's served return; the START arithmetic itself is round 17's."""
    if flow == "end":
        return r17.link([d["r"] for d in days]), []
    if flow != "start":
        raise ValueError("flow convention must be 'end' or 'start', got %r" % (flow,))
    g = guarded_days(days)
    gs = set(g)
    use = [dict(d, flow=None) if i in gs else d for i, d in enumerate(days)]
    return r17.link_alt_flow(use, "START"), g


def flow_facts(days):
    """(flow_day_count, largest |flow| / prior-day value) over days 1.. (the same set link_alt_flow re-links)."""
    n, ratio = 0, 0.0
    for i in range(1, len(days)):
        f, v0 = days[i].get("flow"), days[i - 1].get("mv")
        if f:
            n += 1
            if v0:
                ratio = max(ratio, abs(f) / abs(v0))
    return n, ratio


# ----------------------------------------------------------------------------------------------------------------- grading
def grade_segment(acct, seg, days, bd, tolerance_pp=TOLERANCE_PP, flow=None):
    flow = flow or FLOW_CONVENTION
    if days is None or not days or bd is None or bd.get("twr") is None:
        return r30.grade_segment(acct, seg, days, bd, tolerance_pp)       # not-gradable paths unchanged
    row = {"account": acct, "segment": {"start": seg["start"], "end": seg["end"]}}
    opal, guard = opal_link(days, flow)
    fees, add = fee_addback_v2(bd, days)
    gross = r30.compound_gross(bd["twr"], add)
    diff = abs(gross - opal) * 100.0
    n_flow, ratio = flow_facts(days)
    row.update(bd_return=bd["twr"], opal_return=opal, opal_days=len(days), bd_days_held=bd.get("days_held"),
               bd_fees_reported=fees, bd_fee_addback=add, bd_gross_return=gross, abs_diff_pp=diff,
               flow_convention=flow, flow_days=n_flow, max_flow_ratio=ratio, guard_days=len(guard))
    if diff <= tolerance_pp:
        row["verdict"] = "WITHIN"
        row["reason"] = None
    else:
        row["verdict"] = "OUTSIDE"
        row["reason"], row["evidence"] = r17.explain(days, bd, gross, opal)
    return row


def build_rows(plan, bronze, gold, flow):
    """Round 18's build() with this module's grade_segment (round 18 resolves grade_segment in its own globals at call time)."""
    def gs(acct, seg, days, bd, tolerance_pp=TOLERANCE_PP):
        return grade_segment(acct, seg, days, bd, tolerance_pp, flow=flow)
    r18.grade_segment = gs
    return r18.build(plan, bronze, gold)


def load(root, cache):
    plan = json.loads((root / r17.PLAN_REL).read_bytes().decode("utf-8"))
    if cache and Path(cache).is_file():
        with open(cache, "rb") as f:
            n_obj, bronze, gold, n_part, n_gold_accts = pickle.load(f)
    else:
        import boto3
        from botocore.config import Config
        s3 = boto3.client("s3", region_name="us-east-1", config=Config(
            read_timeout=60, retries={"max_attempts": 8, "mode": "standard"}, max_pool_connections=32))
        n_obj, bronze = r17.read_bronze(s3, [r["bd_account"] for r in plan["request_list"]])
        gold, n_part, n_gold_accts = r17.read_gold(s3, [r["account"] for r in plan["request_list"]])
        if cache:
            with open(cache, "wb") as f:
                pickle.dump((n_obj, bronze, gold, n_part, n_gold_accts), f)
    return plan, (n_obj, bronze, gold, n_part, n_gold_accts)


def key(s):
    return (s["account"], s["segment"]["start"], s["segment"]["end"])


def move_reason(prior_row, now_row):
    """A traced reason for a segment WITHIN at the end-of-day convention and OUTSIDE at flow-start: the category and the numbers read."""
    nums = "%d flow day(s), largest flow %.1f%% of the prior day's value, %d guarded day(s); abs_diff %.4f pp at end-of-day -> %.4f pp at flow-start" % (
        now_row["flow_days"], now_row["max_flow_ratio"] * 100.0, now_row["guard_days"], prior_row["abs_diff_pp"], now_row["abs_diff_pp"])
    if now_row["guard_days"]:
        cat = "START_GUARD_DAY"
    elif now_row["max_flow_ratio"] >= LARGE_FLOW:
        cat = "START_LARGE_FLOW"
    else:
        cat = "START_SMALL_FLOW"
    return cat, nums


def main():
    argv = sys.argv
    root = Path(argv[1]).resolve()

    def opt(name, default=None):
        return argv[argv.index(name) + 1] if name in argv else default
    cache, flow = opt("--cache"), opt("--flow", FLOW_CONVENTION)
    record, prior = opt("--record"), opt("--prior")
    if not record:
        raise SystemExit("ERROR: --record <path of the JSON record to write> is required")
    plan, (n_obj, bronze, gold, n_part, n_gold_accts) = load(root, cache)
    rows, planned = build_rows(plan, bronze, gold, flow)
    graded = [x for x in rows if x["verdict"] in ("WITHIN", "OUTSIDE")]
    within = sum(1 for x in graded if x["abs_diff_pp"] <= TOLERANCE_PP)
    by_reason = {}
    for x in graded:
        if x["abs_diff_pp"] > TOLERANCE_PP:
            by_reason[x["reason"]] = by_reason.get(x["reason"], 0) + 1
    sha = hashlib.sha256(Path(__file__).resolve().read_bytes()).hexdigest()
    files = dict(FILES_READ, bronze_prefix="s3://%s/%s" % (r17.BRONZE_BUCKET, r17.BRONZE_PREFIX), bronze_object_count=n_obj,
                 served_series="s3://%s/%sdate=<YYYY-MM-DD>/data.parquet (%d partitions; total_return_daily, market_value_eod, external_flow)" % (
                     r17.GOLD_BUCKET, r17.GOLD_PREFIX, n_part), served_accounts=n_gold_accts)
    rec = {"measured_by": "0.9.0_WK_IRPT_DASHBD~38", "claim": "measured", "vendor_calls": 0, "tolerance_pp": TOLERANCE_PP,
           "basis": "GROSS, COMPOUNDED, fee base = mean positive daily market_value_eod over the linked days",
           "flow_convention": flow, "guard_rule": "flow-start only: a day whose V_(t-1) + F_t < %.2f * |V_(t-1)| keeps its served return and is counted" % GUARD_FRAC,
           "segments_planned": planned, "graded": len(graded), "within": within, "outside": len(graded) - within,
           "outside_by_reason": by_reason, "guard_days_total": sum(x.get("guard_days", 0) for x in graded),
           "segments_with_guard_day": sum(1 for x in graded if x.get("guard_days")),
           "reader_sha256": sha, "files_read": files, "segments": graded}
    in_to_out, by_cat = None, {}
    if prior:
        prow = {key(s): s for s in json.loads(Path(prior).read_bytes().decode("utf-8"))["segments"]}
        in_to_out = []
        for x in graded:
            p = prow[key(x)]
            if p["abs_diff_pp"] <= TOLERANCE_PP and x["abs_diff_pp"] > TOLERANCE_PP:
                cat, nums = move_reason(p, x)
                in_to_out.append({"account": x["account"], "segment": x["segment"], "reason": cat + ": " + nums, "reason_class": cat,
                                  "abs_diff_pp_before": p["abs_diff_pp"], "abs_diff_pp_after": x["abs_diff_pp"],
                                  "verdict_reason_after": x["reason"]})
                by_cat[cat] = by_cat.get(cat, 0) + 1
        out_to_in = sum(1 for x in graded if prow[key(x)]["abs_diff_pp"] > TOLERANCE_PP and x["abs_diff_pp"] <= TOLERANCE_PP)
        rec.update(within_before=sum(1 for s in prow.values() if s["abs_diff_pp"] <= TOLERANCE_PP), out_to_in=out_to_in,
                   in_to_out=in_to_out, in_to_out_by_reason_class=by_cat)
    rp = Path(record)
    rp.write_bytes((json.dumps(rec, indent=1) + "\n").encode("utf-8"))
    md = ["# %s -- counts only" % rp.stem, "",
          "Reader of record `tieout/tieout_reader.py` (sha256 in the record). Flow convention: %s. Tolerance %.2f pp. S3 reads only; zero vendor calls." % (
              flow, TOLERANCE_PP), "",
          "Graded %d of %d planned segments: within %d, outside %d." % (len(graded), planned, within, len(graded) - within), "",
          "| outside reason | segments |", "|---|---|"]
    md += ["| %s | %d |" % (k, v) for k, v in sorted(by_reason.items(), key=lambda kv: (-kv[1], kv[0]))]
    if flow == "start":
        md += ["", "Guard (denominator V_(t-1) + F_t below %.0f%% of |V_(t-1)|; the day keeps its served return): %d day(s) in %d segment(s)." % (
            GUARD_FRAC * 100.0, rec["guard_days_total"], rec["segments_with_guard_day"])]
    if in_to_out is not None:
        md += ["", "Within before (end-of-day, REGRADE_E1): %d; within after (flow-start): %d. Out to in: %d. In to out: %d." % (
            rec["within_before"], within, rec["out_to_in"], len(in_to_out)), "", "| in-to-out reason class | segments |", "|---|---|"]
        md += ["| %s | %d |" % (k, v) for k, v in sorted(by_cat.items())]
    rp.with_suffix(".md").write_bytes(("\n".join(md) + "\n").encode("utf-8"))
    print("OK: flow=%s planned %d graded %d within %d outside %d%s" % (
        flow, planned, len(graded), within, len(graded) - within,
        ("; in_to_out %d %s out_to_in %d" % (len(in_to_out), by_cat, rec["out_to_in"])) if in_to_out is not None else ""))


if __name__ == "__main__":
    main()
