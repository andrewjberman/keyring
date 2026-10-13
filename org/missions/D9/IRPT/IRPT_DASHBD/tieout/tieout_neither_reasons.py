"""IRPT_DASHBD round 89, TO-DB-b-167: a stated reason for each of the 12 segments that neither flow convention closes.

Implements RULE.md (deliverables/0.9.0_WK_IRPT_DASHBD~133/RULE.md, committed before any read of the 12 segments' rows)
as written. The previous cell's module tieout_flow_timing.py is imported by path and not edited; its STORED folder is
pointed at a COPY of the stored tables held in the private folder of worker ~133. No vendor call, no secret read, no S3
access, no write to any served location. Prints COUNTS ONLY on stdout.

Usage: python -I tieout_neither_reasons.py <record_out_path> [<surprise_row_id>]
  With only the first argument, prints the counts. With the record path, writes NEITHER_12_REASONS.json there; the
  surprise_row key is carried only when UNEXPLAINED is above zero and the id is given.
"""
import collections
import datetime as dt
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, *([os.pardir] * 6)))
PRIV = "C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~133/"
COPY = PRIV + "copy/"
RULE_REL = "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~133/RULE.md"
CODE_REL = "org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_neither_reasons.py"
RULE_SHA = "fc50363af10dfad3d0088a4220c68132b8a02c41859941e8ab30c7be53361f55"
RULE_COMMIT = "99d37085ba7787bf1f4be6ae8f715d50f22dcf16"
TOL_PP = 0.35
NEAR_DAYS = 5
NAMES = ("MISSING_PRICE", "FLOW_ABSENT_ONE_SIDE", "FLOW_ON_NON_TRADING_DAY", "INCOME_OFF_FLOW_DAY",
         "BD_ACCRUED_INCOME", "UNEXPLAINED")


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def import_by_path(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


prev = import_by_path(os.path.join(HERE, "tieout_flow_timing.py"), "tieout_flow_timing")
prev.STORED = COPY
tc = import_by_path(os.path.join(REPO, "lib", "trading_calendar.py"), "trading_calendar")


def is_trading(d):
    return tc.is_trading_day(d)


def fnum(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return 0.0


def tie(p, q):
    return abs(p - q) <= max(1.0, 0.001 * max(abs(p), abs(q)))


def tie_amt(x, a):
    return abs(x - a) <= max(1.0, 0.001 * abs(a))


def day_of(s):
    return dt.date.fromisoformat(str(s)[:10])


def flagged(p):
    return p is not None and str(p) != ""


def closes(gross, r):
    return abs(gross - r) * 100.0 <= TOL_PP


def make_w(series, window):
    return [{"d": d, "dt": day_of(d), "r": series[d]["r"], "mv": series[d]["mv"], "flow": series[d]["flow"],
             "inc": series[d]["inc_recv"], "price": series[d]["price_reason"]} for d in window]


def d_of(w_list):
    return [{"r": w["r"], "mv": w["mv"], "flow": w["flow"]} for w in w_list if w["r"] is not None]


def r_of(w_list, prior_mv):
    return prev.relink(d_of(w_list), "bd_default", prior_mv)


# ---- tests (on the stored, uncorrected rows) -------------------------------------------------------------

def test_missing(w_list):
    return [w for w in w_list if flagged(w["price"])]


def test_flow_absent(w_list, bdf):
    return [w for w in w_list if w["r"] is not None and ((w["flow"] or 0.0) != 0) != (bdf.get(w["d"], 0.0) != 0)]


def test_non_trading(w_list):
    return [w for w in w_list if (w["flow"] or 0.0) != 0 and not is_trading(w["dt"])]


def income_pairs(w_list, bdi):
    pairs = []
    for i, w in enumerate(w_list):
        a = w["inc"] or 0.0
        if a == 0 or bdi.get(w["d"], 0.0) != 0:
            continue
        cands = []
        for j, x in enumerate(w_list):
            off = (x["dt"] - w["dt"]).days
            if j == i or abs(off) > NEAR_DAYS:
                continue
            if tie_amt(bdi.get(x["d"], 0.0), a):
                cands.append((abs(off), off, j))
        if cands:
            _, _, j = min(cands)
            pairs.append((i, j))
    return pairs


def accrual_identity(o, b):
    tb, te = tie(b["bmv"], o["bmv"]), tie(b["emv"], o["emv"])
    tn, tg = tie(b["nadd"], o["flow"]), tie(b["ngain"], o["gain"])
    dacc = b["eacc"] - b["bacc"]
    ok_b = tb or abs((b["bmv"] - o["bmv"]) - b["bacc"]) <= max(1.0, 0.001 * abs(b["bacc"]))
    ok_e = te or abs((b["emv"] - o["emv"]) - b["eacc"]) <= max(1.0, 0.001 * abs(b["eacc"]))
    ok_g = abs((b["ngain"] - o["gain"]) - dacc) <= max(1.0, 0.001 * abs(dacc))
    return bool(tn and not (tb and te and tg) and ok_b and ok_e and ok_g)


def accrual_r(r, o, b):
    if not (o["emv"] > 0 and o["bmv"] > 0):
        return None
    den = (o["bmv"] + b["bacc"]) / o["bmv"]
    if den == 0:
        return None
    return (1.0 + r) * ((o["emv"] + b["eacc"]) / o["emv"]) / den - 1.0


# ---- corrections (each returns a new window list, or None when not applicable) ---------------------------

def corr_missing(w_list, prior_mv):
    w_list = [dict(w) for w in w_list]
    for i, w in enumerate(w_list):
        if not flagged(w["price"]):
            continue
        p = next((w_list[j]["mv"] for j in range(i - 1, -1, -1) if w_list[j]["mv"] is not None), prior_mv)
        if p is None:
            return None
        w["mv"] = p + (w["flow"] or 0.0)
    return w_list


def corr_flow_absent(w_list, bdf):
    w_list = [dict(w) for w in w_list]
    for w in w_list:
        if w["r"] is None:
            continue
        f0, b0 = (w["flow"] or 0.0), bdf.get(w["d"], 0.0)
        if (f0 != 0) != (b0 != 0):
            w["flow"] = b0
    return w_list


def corr_non_trading(w_list):
    w_list = [dict(w) for w in w_list]
    d_idx = [i for i, w in enumerate(w_list) if w["r"] is not None]
    for i, w in enumerate(w_list):
        f0 = w["flow"] or 0.0
        if f0 == 0 or is_trading(w["dt"]):
            continue
        tgt = next((j for j in d_idx if j > i and is_trading(w_list[j]["dt"])), None)
        if tgt is None:
            tgt = next((j for j in reversed(d_idx) if j < i and is_trading(w_list[j]["dt"])), None)
        if tgt is None:
            return None
        w_list[tgt]["flow"] = (w_list[tgt]["flow"] or 0.0) + f0
        w["flow"] = 0.0
    return w_list


def corr_income(w_list, pairs):
    w_list = [dict(w) for w in w_list]
    for i, j in pairs:
        a = w_list[i]["inc"] or 0.0
        if j > i:
            for t in range(i, j):
                if w_list[t]["mv"] is not None:
                    w_list[t]["mv"] -= a
        else:
            for t in range(j, i):
                if w_list[t]["mv"] is not None:
                    w_list[t]["mv"] += a
    return w_list


def main():
    rule_path = os.path.join(REPO, RULE_REL)
    if sha256_file(rule_path) != RULE_SHA:
        print("STOP: RULE.md bytes differ from the committed rule")
        sys.exit(2)
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

    def bd_days(acct):
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

    pop = []          # (acct, uncorrected closes under bd_default and end)
    flow_accts = set()
    n_total, n_noflow, n_nofig = len(rows), 0, 0
    neither = []      # the 12: dicts holding every input needed for the classification
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
        w0 = make_w(series, window)
        before = [d for d in series if d < seg["start"]]
        prior_mv = series[max(before)].get("mv") if before else None
        base = o["mean"]
        add = b["fees"] / base if base > 0 else 0.0
        gross = (1.0 + v["bdr"]) * (1.0 + add) - 1.0
        days = [series[d] for d in window if series[d]["r"] is not None]
        c_bd = closes(gross, prev.relink(days, "bd_default", prior_mv))
        c_end = closes(gross, prev.relink(days, "end", prior_mv))
        pop.append({"a": acct, "bd_default": c_bd, "end": c_end})
        flow_accts.add(acct)
        if not (c_bd or c_end):
            bdf, bdi = bd_days(acct)
            neither.append({"acct": acct, "seg": seg, "o": o, "b": b, "w0": w0, "prior_mv": prior_mv,
                            "gross": gross, "bdf": bdf, "bdi": bdi, "c_bd": c_bd, "c_end": c_end})
    cross = prev.crosstab(pop)
    flow_n = len(pop)
    print("segments_total %d; no_flow %d; no_figure %d; flow_segments %d; neither %d" % (
        n_total, n_noflow, n_nofig, flow_n, cross["neither"]))
    print("accounts among flow segments %d" % len(flow_accts))
    if flow_n != 88 or len(neither) != 12:
        print("STOP: the population does not reproduce (flow %d, neither %d)" % (flow_n, len(neither)))
        sys.exit(2)

    uncorr_closes = sum(1 for s in neither if s["c_bd"] or s["c_end"])
    by_reason = collections.Counter()
    evidence = collections.defaultdict(list)
    kinds = {}
    demoted = 0
    combined = 0
    unexpl_accts = collections.Counter()
    any_test_counts = collections.Counter()

    for s in neither:
        o, b, w0, prior_mv, gross = s["o"], s["b"], s["w0"], s["prior_mv"], s["gross"]
        bdf, bdi = s["bdf"], s["bdi"]
        seg_start = day_of(s["seg"]["start"])
        t1 = test_missing(w0)
        t2 = test_flow_absent(w0, bdf)
        t3 = test_non_trading(w0)
        t4 = income_pairs(w0, bdi)
        t5 = accrual_identity(o, b)
        hold = {1: len(t1) > 0, 2: len(t2) > 0, 3: len(t3) > 0, 4: len(t4) > 0, 5: t5}
        for k in hold:
            if hold[k]:
                any_test_counts[k] += 1

        def apply_series(k, w_list):
            if k == 1:
                return corr_missing(w_list, prior_mv)
            if k == 2:
                return corr_flow_absent(w_list, bdf)
            if k == 3:
                return corr_non_trading(w_list)
            return corr_income(w_list, t4)

        def single_closes(k):
            if not hold[k]:
                return False
            if k == 5:
                ar = accrual_r(r_of(w0, prior_mv), o, b)
                return ar is not None and closes(gross, ar)
            wk = apply_series(k, w0)
            return wk is not None and closes(gross, r_of(wk, prior_mv))

        taken = None
        for k in (1, 2, 3, 4, 5):
            if single_closes(k):
                taken = k
                break
        if taken is not None:
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
            continue

        by_reason[NAMES[5]] += 1
        unexpl_accts[s["acct"]] += 1
        if any(hold.values()):
            demoted += 1
        holds = [k for k in (1, 2, 3, 4, 5) if hold[k]]
        pair_ok = False
        for pa, pb in combinations(holds, 2):
            ks = sorted(k for k in (pa, pb) if k <= 4)
            wk = w0
            for k in ks:
                wk = apply_series(k, wk)
                if wk is None:
                    break
            if wk is None:
                continue
            rk = r_of(wk, prior_mv)
            if 5 in (pa, pb):
                ar = accrual_r(rk, o, b)
                if ar is not None and closes(gross, ar):
                    pair_ok = True
                    break
            elif closes(gross, rk):
                pair_ok = True
                break
        if pair_ok:
            combined += 1

    unexpl = by_reason[NAMES[5]]
    reasoned = 12 - unexpl
    print("by_reason %s (sum %d)" % (json.dumps({n: by_reason[n] for n in NAMES}, sort_keys=True), sum(by_reason.values())))
    print("uncorrected_closes_among_12 %d" % uncorr_closes)
    print("demoted_to_unexplained %d; combined_only %d; closed_within_tolerance %d" % (demoted, combined, reasoned))
    print("tests holding (any segment of the 12): %s" % json.dumps({NAMES[k - 1]: any_test_counts[k] for k in (1, 2, 3, 4, 5)}, sort_keys=True))
    print("unexplained accounts %d; unexplained segments per account %s" % (
        len(unexpl_accts), sorted(unexpl_accts.values())))

    if len(sys.argv) < 2:
        print("OK: counts printed; no record written (no record path given)")
        return
    record = {
        "tolerance_pp": TOL_PP,
        "rule": {"file": "RULE.md", "sha256": RULE_SHA, "commit": RULE_COMMIT, "written_before_count": True},
        "reasons_list": list(NAMES),
        "code": {"file": CODE_REL, "sha256": code_sha, "tracked": tracked},
        "population": {"flow_segments": flow_n, "neither_segments": len(neither), "accounts": len(flow_accts)},
        "by_reason": {n: by_reason[n] for n in NAMES},
        "evidence": {n: {"kind": kinds.get(n, "count"), "values": sorted(evidence[n])} for n in NAMES[:-1] if by_reason[n] > 0},
        "corrected": {"reasoned": reasoned, "closed_within_tolerance": reasoned, "demoted_to_unexplained": demoted,
                      "combined_only": combined},
        "uncorrected_closes_among_12": uncorr_closes,
        "unexplained_per_account": sorted(unexpl_accts.values()),
        "fwd8_unmet_accounts": len(unexpl_accts),
        "reads": {"vendor_calls": 0, "secret_reads": 0, "s3_writes": 0},
        "served_values_changed": False,
        "on_a_copy": True,
        "limits": ("Counts only. A reason is a cause that, corrected alone in the recomputation, closes the segment within "
                   "tolerance; it is not proof that the cause is the only one, and each correction is a recomputation "
                   "change, not a statement of which system is right. Trading-day status is lib/trading_calendar as it stands."),
    }
    if unexpl > 0:
        if len(sys.argv) < 3:
            print("STOP: UNEXPLAINED is above zero and no surprise row id was given")
            sys.exit(2)
        record["surprise_row"] = sys.argv[2]
    with open(sys.argv[1], "wb") as fh:
        fh.write((json.dumps(record, indent=2, sort_keys=True) + "\n").encode("ascii"))
    print("OK: record written")


if __name__ == "__main__":
    main()
