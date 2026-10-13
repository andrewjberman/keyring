"""IRPT_DASHBD round 90, TO-DB-b-170: a reason from round 89's closed list for each of the 2 stored segments with no flow day.

Applies RULE.md (deliverables/0.9.0_WK_IRPT_DASHBD~133/RULE.md, sha256 fc50363a..., REUSED UNCHANGED: no rule file is
written here) to the 2 of the 90 stored tie-out segments whose window holds no flow day. Round 89's tracked module
tieout_neither_reasons.py is imported by path and not edited; its tests, corrections, relink and closes are the rule's
own code. Reads the stored tables of worker ~133's private COPY only (through round 89's prev module). No vendor call,
no secret read, no S3 access, no write to any served location. Prints COUNTS ONLY on stdout.

Usage: python -I tieout_noflow_reasons.py [<record_out_path>]
  With no argument, prints the counts and writes nothing. With the record path, writes NOFLOW_2_REASONS.json there.
"""
import collections
import hashlib
import importlib.util
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, *([os.pardir] * 6)))
RULE_REL = "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~133/RULE.md"
CODE_REL = "org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_noflow_reasons.py"
R89_FILE = "tieout_neither_reasons.py"
RULE_SHA = "fc50363af10dfad3d0088a4220c68132b8a02c41859941e8ab30c7be53361f55"
EXPECT_SEGMENTS, EXPECT_ACCOUNTS, EXPECT_NOFLOW, EXPECT_FLOW = 90, 86, 2, 88


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def import_by_path(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


r89 = import_by_path(os.path.join(HERE, R89_FILE), "tieout_neither_reasons")
prev = r89.prev
NAMES = r89.NAMES
TOL_PP = r89.TOL_PP


def fnum(x):
    return r89.fnum(x)


def bd_days(txn_by, acct):
    fl, inc = collections.defaultdict(float), collections.defaultdict(float)
    for t in txn_by[str(acct).strip().lstrip("0")]:
        rd = t.get("return_date")
        if not rd:
            continue
        d = str(rd)[:10]
        if t.get("external_flow") in ("Contribution", "Withdrawal"):
            fl[d] += fnum(t.get("market_value"))
        inc[d] += fnum(t.get("income"))
    return dict(fl), dict(inc)


def stop(msg):
    print("STOP: " + msg)
    sys.exit(2)


def main(argv):
    if sha256_file(os.path.join(REPO, RULE_REL)) != RULE_SHA:
        stop("RULE.md bytes differ from the rule committed for round 89 (reused unchanged)")
    code_sha = sha256_file(os.path.abspath(__file__))
    git_rc = subprocess.run(["git", "-C", REPO, "ls-files", "--error-unmatch", CODE_REL],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    git_dirty = subprocess.run(["git", "-C", REPO, "status", "--porcelain", "--", CODE_REL],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode("ascii", "replace").strip()
    tracked = git_rc == 0 and git_dirty == ""

    read = prev.load("read90.pkl")
    rows = prev.load("table90.pkl")
    gold, txn = read["gold"], read["txn"]
    txn_by = collections.defaultdict(list)
    for t in txn:
        txn_by[str(t["account_number"]).strip().lstrip("0")].append(t)

    accounts_all = set()
    flow_accts = set()
    n_flow, n_nofig_flow = 0, 0
    noflow = []
    for r in rows:
        acct, seg, o, b, v = r["a"], r["seg"], r["o"], r["b"], r["v2"]
        accounts_all.add(acct)
        series = gold[acct]
        window = [d for d in sorted(series) if seg["start"] <= d <= seg["end"]]
        has_fig = not (v.get("bdr") is None or b.get("fees") is None or o.get("mean") is None)
        if not any(series[d]["flow"] for d in window):
            noflow.append((acct, seg, o, b, v, series, window, has_fig))
            continue
        if not has_fig:
            n_nofig_flow += 1
            continue
        n_flow += 1
        flow_accts.add(acct)

    print("segments_total %d; accounts_total %d; flow_segments %d; no_flow_segments %d; flow_no_figure %d; accounts_among_flow %d" % (
        len(rows), len(accounts_all), n_flow, len(noflow), n_nofig_flow, len(flow_accts)))
    if len(rows) != EXPECT_SEGMENTS or len(accounts_all) != EXPECT_ACCOUNTS:
        stop("population does not reproduce: segments %d (expect %d), accounts %d (expect %d)" % (
            len(rows), EXPECT_SEGMENTS, len(accounts_all), EXPECT_ACCOUNTS))
    if len(noflow) != EXPECT_NOFLOW or n_flow != EXPECT_FLOW or n_nofig_flow != 0:
        stop("population does not reproduce: no_flow %d (expect %d), flow %d (expect %d), no-figure %d (expect 0)" % (
            len(noflow), EXPECT_NOFLOW, n_flow, EXPECT_FLOW, n_nofig_flow))
    if not all(item[7] for item in noflow):
        stop("a no-flow segment carries no BD figure; it is not gradable and the rule cannot grade it")

    by_reason = collections.Counter()
    evidence = collections.defaultdict(list)
    kinds = {}
    uncorr = 0
    tests_holding = collections.Counter()

    for acct, seg, o, b, v, series, window, _ in noflow:
        w0 = r89.make_w(series, window)
        before = [d for d in series if d < seg["start"]]
        prior_mv = series[max(before)].get("mv") if before else None
        base = o["mean"]
        add = b["fees"] / base if base > 0 else 0.0
        gross = (1.0 + v["bdr"]) * (1.0 + add) - 1.0
        days = [series[d] for d in window if series[d]["r"] is not None]
        c_bd = r89.closes(gross, prev.relink(days, "bd_default", prior_mv))
        c_end = r89.closes(gross, prev.relink(days, "end", prior_mv))
        if c_bd or c_end:
            uncorr += 1
        bdf, bdi = bd_days(txn_by, acct)
        seg_start = r89.day_of(seg["start"])

        t1 = r89.test_missing(w0)
        t2 = r89.test_flow_absent(w0, bdf)
        t3 = r89.test_non_trading(w0)
        t4 = r89.income_pairs(w0, bdi)
        t5 = r89.accrual_identity(o, b)
        hold = {1: len(t1) > 0, 2: len(t2) > 0, 3: len(t3) > 0, 4: len(t4) > 0, 5: t5}
        for k in hold:
            if hold[k]:
                tests_holding[k] += 1

        def apply_series(k, w_list):
            if k == 1:
                return r89.corr_missing(w_list, prior_mv)
            if k == 2:
                return r89.corr_flow_absent(w_list, bdf)
            if k == 3:
                return r89.corr_non_trading(w_list)
            return r89.corr_income(w_list, t4)

        def single_closes(k):
            if not hold[k]:
                return False
            if k == 5:
                ar = r89.accrual_r(r89.r_of(w0, prior_mv), o, b)
                return ar is not None and r89.closes(gross, ar)
            wk = apply_series(k, w0)
            return wk is not None and r89.closes(gross, r89.r_of(wk, prior_mv))

        taken = next((k for k in (1, 2, 3, 4, 5) if single_closes(k)), None)
        if taken is None:
            by_reason[NAMES[5]] += 1
            continue
        by_reason[NAMES[taken - 1]] += 1
        if taken == 1:
            evidence[NAMES[0]].append(len(t1))
            kinds[NAMES[0]] = "count"
        elif taken == 2:
            evidence[NAMES[1]].append(len(t2))
            kinds[NAMES[1]] = "count"
        elif taken == 3:
            evidence[NAMES[2]].extend((w["dt"] - seg_start).days for w in t3)
            kinds[NAMES[2]] = "day_offsets"
        elif taken == 4:
            evidence[NAMES[3]].extend((w0[j]["dt"] - w0[i]["dt"]).days for i, j in t4)
            kinds[NAMES[3]] = "day_offsets"
        else:
            evidence[NAMES[4]].append(1)
            kinds[NAMES[4]] = "count"

    unexpl = by_reason[NAMES[5]]
    reasoned = len(noflow) - unexpl
    print("by_reason %s (sum %d)" % (json.dumps({n: by_reason[n] for n in NAMES}, sort_keys=True), sum(by_reason.values())))
    print("uncorrected_closes_among_2 %d" % uncorr)
    print("reasoned (closed within %s pp when corrected) %d of %d" % (TOL_PP, reasoned, len(noflow)))
    print("tests holding (of the 2): %s" % json.dumps({NAMES[k - 1]: tests_holding[k] for k in (1, 2, 3, 4, 5)}, sort_keys=True))

    if len(argv) < 2:
        print("OK: counts printed; no record written (no record path given)")
        return
    record = {
        "tolerance_pp": TOL_PP,
        "rule": {"file": RULE_REL, "sha256": RULE_SHA, "reused_unchanged": True},
        "reasons_list": list(NAMES),
        "code": {"file": CODE_REL, "sha256": code_sha, "tracked": tracked},
        "population": {"segments": len(rows), "accounts": len(accounts_all),
                       "no_flow_segments": len(noflow), "flow_segments": n_flow},
        "by_reason": {n: by_reason[n] for n in NAMES},
        "evidence": {n: {"kind": kinds.get(n, "count"), "values": sorted(evidence[n])}
                     for n in NAMES[:-1] if by_reason[n] > 0},
        "corrected": {"reasoned": reasoned, "closed_within_tolerance": reasoned},
        "uncorrected_closes_among_2": uncorr,
        "reads": {"vendor_calls": 0, "secret_reads": 0, "s3_writes": 0},
        "served_values_changed": False,
        "limits": ("Counts only. A reason is a cause that, corrected alone in the recomputation, closes the segment within "
                   "tolerance; it is not proof that the cause is the only one, and each correction is a recomputation "
                   "change, not a statement of which system is right. Trading-day status is lib/trading_calendar as it stands."),
    }
    with open(argv[1], "wb") as fh:
        fh.write((json.dumps(record, indent=2, sort_keys=True) + "\n").encode("ascii"))
    print("OK: record written")


if __name__ == "__main__":
    main(sys.argv)
