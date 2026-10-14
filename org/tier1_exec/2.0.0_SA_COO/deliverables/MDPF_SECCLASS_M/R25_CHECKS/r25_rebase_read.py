#!/usr/bin/env python3
"""r25_rebase_read.py -- MDPF_SECCLASS round 25, cell SC-e-101: the re-based acceptance read, read-only.

  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/r25_rebase_read.py capture --out <path>
  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/r25_rebase_read.py read --baseline <path>
  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R25_CHECKS/r25_rebase_read.py selftest

Run from the repo root. AWS is read-only: every read goes through the r24 module (r24_legg_read.py, imported by path,
not copied and not edited) and its head / get_json / get_bytes, which run .tools/aws(.cmd). Served keys are located
through lib/platinum_dest source() in canonical mode (r24.resolve_mode(None)). The one write is capture's --out file,
written once and only when ok. selftest makes no AWS call.

Reused from r24 (r24_legg_read.py): K_MDS, K_MIXSUM, K_FMV, K_CP (:52-55), LABEL_MAP (:77-78), resolve_mode (:316),
head (:324), get_bytes (:333), get_json (:340). Copied with citation: the AUA reader (r24 cmd_e97 :652-657, buried
inside that function) and the bar reader (r24 crit_bars :227-239, buried inside that function).

Exit: 0 ok, 1 not ok, 2 usage, 3 the baseline file is absent (read).
"""
import csv
import datetime
import importlib.util
import io
import json
import sys
import time
from pathlib import Path

ROOT = Path.cwd()
DELIV = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M"
R24_PATH = DELIV / "R24_CHECKS/r24_legg_read.py"
RADIUS = DELIV / "R23_RADIUS"

TOL_AUA = 1.00      # totals; also the STRICT threshold: a date is STRICT when abs(move) <= TOL_AUA
TOL_ROUND = 250.00  # the rounding the code carries (r24 constants; row D1-W85-S6)
TOL_S27 = 1000.00   # the owner's bound on C_06's total against its class sum (clause s27)

CLAUSES = ("totals", "classes", "advisors", "bars", "s27", "restated")
GRANS = ("quarterly", "monthly", "annually")

R24 = None


def load_r24():
    """The r24 module, imported by path. Its import loads lib/platinum_dest and reads nothing from AWS."""
    global R24
    if R24 is None:
        spec = importlib.util.spec_from_file_location("r24_legg_read", R24_PATH)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        R24 = mod
    return R24


def bar_labels():
    """The five bars, from r24's LABEL_MAP (r24_legg_read.py:77-78): 2026-Q3, 2026-09, 2026-Q4, 2026-10, 2026."""
    return list(load_r24().LABEL_MAP.values())


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


# ---------------------------------------------------------------- pure grading (no AWS; fixtures drive these)

def numeric_classes(day):
    """Every numeric value of a firm day except total: the class dollars (clause 2 and s27 read these)."""
    return {k: float(v) for k, v in day.items()
            if k != "total" and isinstance(v, (int, float)) and not isinstance(v, bool)}


def grade_move(pairs, mv):
    """pairs: [(live, baseline)] for one date; mv: that date's move (None when unknown).
    STRICT (abs(mv) <= TOL_AUA): every pair within TOL_ROUND of its baseline. MOVED: the sum of the pair deltas is
    within TOL_ROUND of mv (the move is conserved; nothing is claimed about which key takes it)."""
    if mv is None:
        return False
    deltas = [live - base for live, base in pairs]
    if abs(mv) <= TOL_AUA:
        return all(abs(x) <= TOL_ROUND for x in deltas)
    return abs(sum(deltas) - mv) <= TOL_ROUND


def read_bar(views, label):
    """r24 crit_bars bar reader (r24_legg_read.py:227-239), copied because it is buried in crit_bars: the entry whose
    period is the label, its end_date, its total_aua, and its class dollars read as ent[cls]["value"]. The three
    granularity lists are searched (r24 looks the list up by b["gran"], which this read does not carry)."""
    for gran in GRANS:
        ent = next((e for e in views.get(gran, []) if e.get("period") == label), None)
        if ent is not None:
            classes = {cls: float(v["value"]) for cls, v in ent.items() if isinstance(v, dict) and "value" in v}
            return {"end": ent["end_date"], "total": float(ent["total_aua"]), "classes": classes}
    return None


def grade_all(live, base, required_bars):
    """Pure. live: {mds_rt, mix_rt, firm, aua, advisors {key: {date: total}}, bars {label: {end, total, classes}}}.
    base: {restated_through, firm, aua, advisors}. Returns the window facts and one (ok, detail) per clause."""
    rt = live["mds_rt"] if live["mds_rt"] is not None else ""
    lf, bf = live["firm"], base["firm"]
    la, ba = live["aua"], base["aua"]
    la_adv, ba_adv = live["advisors"], base["advisors"]
    window = sorted(d for d in bf if d >= rt and d in lf)
    win = set(window)
    dropped = sorted(d for d in bf if d < rt)
    absent = sorted(d for d in bf if d >= rt and d not in lf)

    def move(d):
        return la[d] - ba[d] if (d in la and d in ba) else None

    def is_strict(mv):
        return mv is not None and abs(mv) <= TOL_AUA

    strict = [d for d in window if is_strict(move(d))]
    moved = [d for d in window if move(d) is not None and not is_strict(move(d))]
    unknown = [d for d in window if move(d) is None]

    # 1 totals
    t_vals = [abs(lf[d]["total"] - la[d]) for d in window if d in la]
    t_bad = [d for d in window if d not in la or abs(lf[d]["total"] - la[d]) > TOL_AUA]
    totals_ok = bool(window) and not t_bad
    totals = (totals_ok, "max_abs=%.2f n=%d bad=%s" % (max(t_vals) if t_vals else -1.0, len(window), t_bad))

    # 2 classes
    c_bad = []
    for d in window:
        lc, bc = numeric_classes(lf[d]), numeric_classes(bf[d])
        if set(lc) != set(bc):
            c_bad.append(d)
            continue
        if not grade_move([(lc[k], bc[k]) for k in sorted(bc)], move(d)):
            c_bad.append(d)
    classes_ok = bool(window) and not c_bad
    classes = (classes_ok, "strict=%d moved=%d bad=%s" % (len(strict), len(moved), c_bad))

    # 3 advisors
    keys = sorted(set(la_adv) | set(ba_adv))
    set_equal = set(la_adv) == set(ba_adv)
    a_bad = []
    for d in window:
        pairs = [(la_adv.get(k, {}).get(d, 0.0), ba_adv.get(k, {}).get(d, 0.0)) for k in keys]
        if not grade_move(pairs, move(d)):
            a_bad.append(d)
    advisors_ok = bool(window) and set_equal and not a_bad
    advisors = (advisors_ok, "keys_live=%d keys_base=%d set_equal=%s bad_dates=%s" % (
        len(la_adv), len(ba_adv), set_equal, a_bad))

    # 4 bars
    lb = live["bars"]
    b_bad, ungraded, b_rows = [], [], []
    for label in required_bars:
        b = lb.get(label)
        if b is None or b["end"] not in la:
            b_bad.append(label)
            b_rows.append("%s=MISSING" % label)
            continue
        end = b["end"]
        tot_ok = abs(b["total"] - la[end]) <= TOL_AUA
        if end in win:
            bc = numeric_classes(bf[end])
            cls_ok = set(b["classes"]) == set(bc) and grade_move(
                [(b["classes"][k], bc[k]) for k in sorted(bc)], move(end))
            graded = "graded"
        else:
            cls_ok, graded = True, "ungraded"
            ungraded.append(label)
        if not (tot_ok and cls_ok):
            b_bad.append(label)
        b_rows.append("%s=end:%s,total_ok:%s,classes:%s" % (label, end, tot_ok, graded))
    bars = (not b_bad, "rows=%s bad=%s bars_ungraded=%s" % (b_rows, b_bad, ungraded))

    # 5 s27 over EVERY live firm date
    worst = None
    for d in sorted(lf):
        diff = abs(lf[d]["total"] - sum(numeric_classes(lf[d]).values()))
        if worst is None or diff > worst[0]:
            worst = (diff, d)
    s27_ok = worst is not None and worst[0] <= TOL_S27
    s27 = (s27_ok, "max_abs=%.2f date=%s n=%d" % (worst[0] if worst else -1.0, worst[1] if worst else None, len(lf)))

    # 6 restated
    rs_ok = (live["mds_rt"] is not None and live["mix_rt"] is not None and live["mds_rt"] == live["mix_rt"])
    restated = (rs_ok, "mds=%s mix_summary=%s" % (live["mds_rt"], live["mix_rt"]))

    return {"rt": rt, "window": window, "strict": strict, "moved": moved, "unknown": unknown,
            "dropped": dropped, "absent": absent, "ungraded": ungraded, "max_s27": worst,
            "clauses": {"totals": totals, "classes": classes, "advisors": advisors, "bars": bars,
                        "s27": s27, "restated": restated}}


def failing(res):
    return set(n for n in CLAUSES if not res["clauses"][n][0])


# ---------------------------------------------------------------- AWS reads (read-only, through r24)

def served_json(key, mode):
    """One served JSON object: head, get, head. The entry carries the first head's VersionId and LastModified; the
    object is stable when both heads agree (a fire between them makes the body and the entry disagree)."""
    r24 = load_r24()
    b, mk = r24.source(key, mode)
    h1 = r24.head(b, mk)
    body = r24.get_json(b, mk)
    h2 = r24.head(b, mk)
    entry = {"bucket": b, "key": mk, "VersionId": h1["VersionId"], "LastModified": h1["LastModified"]}
    return body, entry, (h1["VersionId"], h1["LastModified"]) == (h2["VersionId"], h2["LastModified"])


def served_aua(mode):
    """The AUA series: client_performance.parquet summed by date. Copied from r24 cmd_e97 (r24_legg_read.py:652-657):
    read columns date and total_aua, to_datetime(date), groupby("date")["total_aua"].sum()."""
    import pandas as pd
    r24 = load_r24()
    b, mk = r24.source(r24.K_CP, mode)
    h1 = r24.head(b, mk)
    raw = r24.get_bytes(b, mk)
    h2 = r24.head(b, mk)
    cp = pd.read_parquet(io.BytesIO(raw), columns=["date", "total_aua"])
    cp["date"] = pd.to_datetime(cp["date"])
    sums = cp.groupby("date")["total_aua"].sum()
    aua = {d.strftime("%Y-%m-%d"): float(v) for d, v in sums.items()}
    entry = {"bucket": b, "key": mk, "VersionId": h1["VersionId"], "LastModified": h1["LastModified"]}
    return aua, entry, (h1["VersionId"], h1["LastModified"]) == (h2["VersionId"], h2["LastModified"])


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------- subcommands

def cmd_capture(out):
    r24 = load_r24()
    mode = r24.resolve_mode(None)
    t0 = time.time()
    p = Path(out)
    if p.exists():
        print("R25-CAPTURE ok=False refused=exists out=%s (captured once; an existing baseline is not overwritten)" % out)
        return 1
    mds, s_mds, st_mds = served_json(r24.K_MDS, mode)
    mix, s_mix, st_mix = served_json(r24.K_MIXSUM, mode)
    fmv, s_fmv, st_fmv = served_json(r24.K_FMV, mode)
    aua_all, s_cp, st_cp = served_aua(mode)
    rt = mds.get("restated_through")
    labels = bar_labels()
    bars = {lb: read_bar(fmv["views"], lb) for lb in labels}
    csv_keys = set(r["advisor_key"] for r in read_csv(RADIUS / "advisor_window_table.csv"))
    served_keys = set(mds["advisors"])
    keys_agree = csv_keys == served_keys
    stable = all([st_mds, st_mix, st_fmv, st_cp])
    print("R25-CAPTURE-CHECK stable=%s csv_advisor_keys_agree=%s served_only=%d csv_only=%d" % (
        stable, keys_agree, len(served_keys - csv_keys), len(csv_keys - served_keys)))
    if rt is None:
        print("R25-CAPTURE ok=False restated_through=absent written=False out=%s" % out)
        return 1
    firm_all, advisors = mds["firm"], mds["advisors"]
    doc = {
        "captured_at": utc_now(),
        "served": {r24.K_MDS: s_mds, r24.K_MIXSUM: s_mix, r24.K_FMV: s_fmv, r24.K_CP: s_cp},
        "restated_through": rt,
        "aua_by_date": {d: aua_all[d] for d in sorted(aua_all) if d >= rt},
        "firm": {d: firm_all[d] for d in sorted(firm_all) if d >= rt},
        "advisor_days": {k: {d: float(day["total"]) for d, day in sorted(advisors[k].items()) if d >= rt}
                         for k in sorted(advisors)},
        "bars": {lb: bars[lb] for lb in labels},
    }
    n_bars = sum(1 for lb in labels if bars[lb] is not None)
    ok = stable and keys_agree and n_bars == len(labels) and bool(doc["firm"])
    written = False
    if ok:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes((json.dumps(doc, sort_keys=True, indent=2) + "\n").encode("utf-8"))
        written = True
    print("R25-CAPTURE ok=%s dates=%d advisors=%d bars=%d out=%s" % (
        ok, len(doc["firm"]), len(doc["advisor_days"]), n_bars, out))
    print("R25-CAPTURE-WRITE written=%s restated_through=%s aua_dates=%d" % (written, rt, len(doc["aua_by_date"])))
    print("R25-TIME capture_total_run_s=%.2f" % (time.time() - t0))
    return 0 if ok else 1


def cmd_read(path):
    r24 = load_r24()
    mode = r24.resolve_mode(None)
    t0 = time.time()
    p = Path(path)
    if not p.is_file():
        print("R25-REBASE ok=False baseline=absent path=%s" % path)
        return 3
    bdoc = json.loads(p.read_text(encoding="utf-8"))
    mds, s_mds, st_mds = served_json(r24.K_MDS, mode)
    mix, s_mix, st_mix = served_json(r24.K_MIXSUM, mode)
    fmv, s_fmv, st_fmv = served_json(r24.K_FMV, mode)
    aua, s_cp, st_cp = served_aua(mode)
    unstable = [n for n, st in (("mix_daily_summary", st_mds), ("mix_summary", st_mix),
                                ("firm_mix_views", st_fmv), ("client_performance", st_cp)) if not st]
    if unstable:
        print("R25-REBASE ok=False reason=unstable sources=%s (a served object moved during the read; read again)" % unstable)
        return 1
    for name, ent, bkey in (("mix_daily_summary", s_mds, r24.K_MDS), ("mix_summary", s_mix, r24.K_MIXSUM),
                            ("firm_mix_views", s_fmv, r24.K_FMV), ("client_performance", s_cp, r24.K_CP)):
        print("R25-SERVED %s bucket=%s key=%s VersionId=%s baseline_VersionId=%s" % (
            name, ent["bucket"], ent["key"], ent["VersionId"], bdoc["served"][bkey]["VersionId"]))
    live = {
        "mds_rt": mds.get("restated_through"),
        "mix_rt": mix.get("restated_through"),
        "firm": mds["firm"],
        "aua": aua,
        "advisors": {k: {d: float(day["total"]) for d, day in v.items()} for k, v in mds["advisors"].items()},
        "bars": {lb: b for lb, b in ((lb, read_bar(fmv["views"], lb)) for lb in bar_labels()) if b is not None},
    }
    base = {"restated_through": bdoc["restated_through"], "firm": bdoc["firm"], "aua": bdoc["aua_by_date"],
            "advisors": bdoc["advisor_days"]}
    res = grade_all(live, base, bar_labels())
    print("R25-WINDOW rt=%s window=%d dropped_from_window=%d absent_from_live=%d unknown_aua=%d" % (
        res["rt"], len(res["window"]), len(res["dropped"]), len(res["absent"]), len(res["unknown"])))
    for name in CLAUSES:
        ok, detail = res["clauses"][name]
        print("R25-C %s ok=%s %s" % (name, ok, detail))
    for lb in res["ungraded"]:
        cls = live["bars"][lb]["classes"]
        print("R25-BARS-UNGRADED %s end=%s classes=%s" % (lb, live["bars"][lb]["end"],
                                                         ",".join("%s=%.2f" % (k, cls[k]) for k in sorted(cls))))
    c = res["clauses"]
    ok = all(c[n][0] for n in CLAUSES)
    ms = res["max_s27"] if res["max_s27"] else (-1.0, None)
    print("R25-REBASE ok=%s window=%d strict=%d moved=%d dropped_from_window=%d totals=%s classes=%s advisors=%s "
          "bars=%s s27=%s max_s27=%.2f restated=%s" % (
              ok, len(res["window"]), len(res["strict"]), len(res["moved"]), len(res["dropped"]),
              c["totals"][0], c["classes"][0], c["advisors"][0], c["bars"][0], c["s27"][0], ms[0],
              c["restated"][0]))
    print("R25-TIME read_total_run_s=%.2f" % (time.time() - t0))
    return 0 if ok else 1


# ---------------------------------------------------------------- selftest (no AWS)

SF_P, SF_D1, SF_D2, SF_D3, SF_N = "2026-09-24", "2026-09-25", "2026-09-28", "2026-09-29", "2026-09-30"
SF_WIN = (SF_D1, SF_D2, SF_D3)
SF_INDEX = {SF_P: 4, SF_D1: 0, SF_D2: 1, SF_D3: 2, SF_N: 3}   # P: before the baseline; N: a new date
SF_A1, SF_A2 = "fixture advisor one", "fixture advisor two"
SF_BARS = ("2026-Q3", "2026-10")          # bar A ends on D3 (graded); bar B ends on N (a new date, ungraded)
MOVE = TOL_ROUND * 6.0 / 5.0              # above TOL_ROUND: a STRICT reading of this move would fail


def sf_day(i):
    """Synthetic firm day i. Every value is an integer multiple of TOL_S27 so every fixture sum is exact in float."""
    u = TOL_S27 * (i + 1)
    return {"c1": 50.0 * u, "c2": 30.0 * u, "c3": 20.0 * u, "total": 100.0 * u}


def sf_classes(day):
    return {k: v for k, v in day.items() if k != "total"}


def sf_base():
    firm = {d: sf_day(SF_INDEX[d]) for d in SF_WIN}
    aua = {d: sf_day(SF_INDEX[d])["total"] for d in SF_WIN}
    adv = {SF_A1: {d: 20.0 * TOL_S27 for d in SF_WIN}, SF_A2: {d: 15.0 * TOL_S27 for d in SF_WIN}}
    return {"restated_through": SF_D1, "firm": firm, "aua": aua, "advisors": adv}


def sf_live(mds_rt=SF_D1, mix_rt=SF_D1):
    firm = {d: sf_day(i) for d, i in SF_INDEX.items()}
    aua = {d: sf_day(i)["total"] for d, i in SF_INDEX.items()}
    adv = {SF_A1: {d: 20.0 * TOL_S27 for d in SF_WIN}, SF_A2: {d: 15.0 * TOL_S27 for d in SF_WIN}}
    bars = {SF_BARS[0]: {"end": SF_D3, "total": aua[SF_D3], "classes": sf_classes(firm[SF_D3])},
            SF_BARS[1]: {"end": SF_N, "total": aua[SF_N], "classes": sf_classes(firm[SF_N])}}
    return {"mds_rt": mds_rt, "mix_rt": mix_rt, "firm": firm, "aua": aua, "advisors": adv, "bars": bars}


def sf_move_d2(live, extra_cls=0.0, extra_adv=0.0):
    """The positive MOVED date: AUA, total, class c1 and advisor A1 all move by MOVE (conserved). The extras are the
    negatives' overshoot, applied to one key only."""
    live["aua"][SF_D2] += MOVE
    live["firm"][SF_D2]["total"] += MOVE
    live["firm"][SF_D2]["c1"] += MOVE + extra_cls
    live["advisors"][SF_A1][SF_D2] += MOVE + extra_adv
    return live


def cmd_selftest():
    base = sf_base()
    cases = []   # (kind, label, own clause or None, live, live rt used)
    cases.append(("POS", "live equals baseline", None, sf_live()))
    cases.append(("POS", "one date MOVED by MOVE (total, one class, one advisor-day)", None, sf_move_d2(sf_live())))
    cases.append(("POS", "one baseline date dropped below rt (rt moved to D2)", None,
                  sf_live(mds_rt=SF_D2, mix_rt=SF_D2)))

    def neg_totals():
        live = sf_live()
        live["firm"][SF_D1]["total"] += 5.0 * TOL_AUA
        return live

    def neg_classes_strict():
        live = sf_live()
        live["firm"][SF_D1]["c2"] += TOL_S27
        return live

    def neg_classes_moved():
        return sf_move_d2(sf_live(), extra_cls=TOL_S27)

    def neg_advisors_missing():
        live = sf_live()
        del live["advisors"][SF_A2]
        return live

    def neg_advisors_moved():
        return sf_move_d2(sf_live(), extra_adv=TOL_S27)

    def neg_bars():
        live = sf_live()
        live["bars"][SF_BARS[0]]["total"] += 5.0 * TOL_AUA
        return live

    def neg_s27():
        live = sf_live()
        live["firm"][SF_P]["total"] += TOL_S27 + TOL_AUA   # P is before the window: only s27 reads it
        return live

    def neg_restated():
        return sf_live(mix_rt=None)

    cases.append(("NEG", "total off the AUA by 5 on a STRICT date", "totals", neg_totals()))
    cases.append(("NEG", "class off by TOL_S27 on a STRICT date", "classes", neg_classes_strict()))
    cases.append(("NEG", "class moved by MOVE + TOL_S27 on a MOVED date (not conserved)", "classes",
                  neg_classes_moved()))
    cases.append(("NEG", "one advisor missing from the live set", "advisors", neg_advisors_missing()))
    cases.append(("NEG", "advisor sum moved by MOVE + TOL_S27 on a MOVED date", "advisors", neg_advisors_moved()))
    cases.append(("NEG", "bar total off the AUA by 5", "bars", neg_bars()))
    cases.append(("NEG", "firm date total differs from class sum by TOL_S27 + TOL_AUA", "s27", neg_s27()))
    cases.append(("NEG", "restated_through absent on the mix summary", "restated", neg_restated()))

    pos_ok, pos_n, neg_ok, neg_n = 0, 0, 0, 0
    for kind, label, own, live in cases:
        res = grade_all(live, base, SF_BARS)
        fail = failing(res)
        if kind == "POS":
            pos_n += 1
            good = not fail
            pos_ok += 1 if good else 0
            print("R25-FIX POS ok=%s failing=%s label=%s window=%d dropped=%d" % (
                good, sorted(fail), label, len(res["window"]), len(res["dropped"])))
        else:
            neg_n += 1
            good = fail == {own}
            neg_ok += 1 if good else 0
            print("R25-FIX NEG exact=%s own=%s failing=%s label=%s" % (good, own, sorted(fail), label))
    ok = pos_ok == pos_n and neg_ok == neg_n
    print("R25-SELFTEST ok=%s positives=%d of %d negatives=%d of %d" % (ok, pos_ok, pos_n, neg_ok, neg_n))
    return 0 if ok else 1


# ---------------------------------------------------------------- entry

def opt(argv, name):
    if name not in argv:
        return None
    i = argv.index(name)
    return argv[i + 1] if i + 1 < len(argv) else None


def main(argv):
    usage = ("usage: r25_rebase_read.py capture --out <path> | read --baseline <path> | selftest")
    if not argv:
        print(usage)
        return 2
    cmd = argv[0]
    if cmd == "selftest":
        return cmd_selftest()
    if cmd not in ("capture", "read"):
        print(usage)
        return 2
    if not R24_PATH.is_file():
        print("usage: run from the repo root (r24_legg_read.py not found under %s)" % R24_PATH.parent)
        return 2
    try:
        if cmd == "capture":
            out = opt(argv, "--out")
            if not out:
                print("usage: capture --out <path>")
                return 2
            return cmd_capture(out)
        base_path = opt(argv, "--baseline")
        if not base_path:
            print("usage: read --baseline <path>")
            return 2
        return cmd_read(base_path)
    except Exception as exc:   # an AWS or parse failure is a verdict line, never a traceback
        tag = "R25-CAPTURE" if cmd == "capture" else "R25-REBASE"
        print("%s ok=False error=%s: %s" % (tag, type(exc).__name__, str(exc)[:300]))
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
