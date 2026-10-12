#!/usr/bin/env python3
"""r24_legg_read.py -- MDPF_SECCLASS round 24, cell SC-e-99: the two leg-G instruments, read-only.

  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py e91 [--since <ISO UTC>]
  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py e97
  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py selftest

Run from the repo root. AWS is read-only (s3 cp to stdout, head-object, list-objects-v2) through .tools/aws(.cmd).
Writes nothing. Every expected value is read from a committed file (the e91 baseline, R23_RADIUS, the SC-e-96 window
record, the request document, D_04 source) or from the order's stated tolerances; no expected dollar figure is typed.

Exit: 0 ok, 1 not ok, 3 the thing read has not happened yet (e91: the served mix daily summary still carries the
baseline VersionId; e97: no restated_through key on the served mix daily summary).
"""
import ast
import copy
import csv
import datetime
import io
import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path.cwd()
BUCKET = "opal-data-bd"
DELIV = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M"
BASELINE_PATH = DELIV / "LEGG_E91_PREFIRE_BASELINE_20261012.json"
RADIUS = DELIV / "R23_RADIUS"
REQUEST = DELIV / "NEVER_WIDEN_HALF_REQUEST_SECCLASS_C06_ROLLING_REDERIVE_20261012.md"
WINDOW_PATH = DELIV / "WINDOW_READ_C06_ROLLING_20261012.json"
D04_SRC = ROOT / "data/black_diamond/scripts/gold/D_04.client_portal_summary.py"

K_MDS = "gold/views/mix_daily_summary.json"
K_MIXSUM = "platinum/firm/mix_summary.json"
K_CP = "gold/timeseries/client_performance.parquet"
K_FMV = "gold/artifacts/firm_mix_views.json"
ENT_PREFIX = "gold/entities/clients/"

E91_FALL_DATES = ["2026-10-08", "2026-10-09"]
E91_CENSUS_DATES = ["2026-10-06", "2026-10-07", "2026-10-08", "2026-10-09"]
E91_NAMES = ["in_range", "census", "total_held", "advisors_same"]
E97_RESTATED = "2026-09-25"                        # criterion 5: the window cutoff (request: cutoff 2026-09-25)
E97_UNCLASS_RANGE = ("2026-09-30", "2026-10-06")   # criterion 1 dates
E97_W86_DATES = ["2026-10-03", "2026-10-04", "2026-10-05"]   # criterion 2 dates
E97_NAMES = ["unclassified_window", "w86_s5", "totals_aua", "bars", "restated", "advisors", "added_dropped"]
TOL_UNCLASS_MARGIN = 250.0     # criterion 1: "plus $250"
TOL_AUA = 1.00                 # criterion 2 ("under $1.00") and criterion 3 ("within $1.00")
TOL_BAR_CLASS = 250.0          # criterion 4 ("within $250")
TOL_ADVISOR = 250.0            # criterion 6 ("within $250")
TOL_HELD = 0.005               # "equals" to the cent
LABEL_MAP = {"Q3 2026": "2026-Q3", "September 2026": "2026-09", "Q4 2026": "2026-Q4",
             "October 2026": "2026-10", "2026 annual": "2026"}


# ---------------------------------------------------------------- committed inputs (no AWS)

def read_csv(path):
    with path.open(encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def canonical_six():
    """D_04.client_portal_summary.py CANONICAL_MIX_CLASSES, read by AST (the module is not imported)."""
    tree = ast.parse(D04_SRC.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "CANONICAL_MIX_CLASSES"
                                                for t in node.targets):
            return tuple(ast.literal_eval(node.value))
    raise RuntimeError("CANONICAL_MIX_CLASSES not found in D_04 source")


def after_table(text):
    """Per-class 'after' dollars of the request's Period bars table, keyed by bars.json label."""
    out, bar, in_sec = {}, None, False
    for line in text.splitlines():
        if line.startswith("## Period bars"):
            in_sec = True
            continue
        if in_sec and line.startswith("## "):
            break
        if not in_sec or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 8 or cells[0] == "bar" or cells[0].startswith("---"):
            continue
        if cells[0]:
            bar = cells[0]
        label = LABEL_MAP.get(bar)
        if label is None or cells[4] == "":
            continue
        slot = out.setdefault(label, {"total_after": None, "classes": {}})
        if cells[2]:
            slot["total_after"] = float(cells[3].replace(",", ""))
        slot["classes"][cells[4]] = float(cells[6].replace(",", ""))
    return out


def load_committed():
    base = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    window = json.loads(WINDOW_PATH.read_text(encoding="utf-8"))
    bars_doc = json.loads((RADIUS / "bars.json").read_text(encoding="utf-8"))
    aua_rows = read_csv(RADIUS / "aua_vs_firm_by_date.csv")
    d04_rows = read_csv(RADIUS / "d04_unclassified_by_date.csv")
    adv_rows = read_csv(RADIUS / "advisor_window_table.csv")
    dd_rows = read_csv(RADIUS / "added_dropped_top10.csv")
    dates = [r["date"] for r in aua_rows]
    unclass_dates = [d for d in dates if E97_UNCLASS_RANGE[0] <= d <= E97_UNCLASS_RANGE[1]]
    per_date = {r["date"]: float(r["rebuilt_unclassified"]) for r in window["per_date"]}
    bars = []
    for gran, label, end, tb, ta, ub, ua in bars_doc["bar_rows"]:
        bars.append({"gran": gran, "label": label, "end": end, "total_before": float(tb),
                     "total_after": float(ta), "unclass_before": float(ub), "unclass_after": float(ua)})
    return {
        "base": base,
        "dates": dates,
        "aua": {r["date"]: float(r["aua_cp"]) for r in aua_rows},
        "after": {r["date"]: float(r["would_be_d04_unclassified"]) for r in d04_rows},
        "adv_rows": adv_rows,
        "dd_rows": dd_rows,
        "six": canonical_six(),
        "unclass_dates": unclass_dates,
        "bound_max": max(per_date[d] for d in unclass_dates),
        "bound_src": "max of per_date[].rebuilt_unclassified over %d window dates of %d records" % (
            len(unclass_dates), len(window["per_date"])),
        "bars": bars,
        "after_table": after_table(REQUEST.read_text(encoding="utf-8")),
    }


# ---------------------------------------------------------------- pure graders

def d04_remainder(day, six):
    """D_04.client_portal_summary.py:440-462: firm total minus the canonical classes present in the day."""
    covered = sum(float(day[c]) for c in six if day.get(c) is not None)
    return float(day["total"]) - covered


def cents(x):
    return round(float(x) + 0.0, 2)


def grade_e91(firm, advisors_count, base, six, bounds):
    """firm: {date: day} for the census dates. Returns the verdict pieces and the failing criterion names."""
    falls, in_range = {}, True
    for d in E91_FALL_DATES:
        fall = cents(float(base["firm_days"][d]["d04_remainder_unclassified"]) - d04_remainder(firm[d], six))
        falls[d] = fall
        in_range = in_range and (0.0 <= fall <= cents(bounds[d]))
    base_keys, now_keys = set(), set()
    for d in E91_CENSUS_DATES:
        base_keys |= set(base["firm_days"][d]["classes"].keys())
        now_keys |= set(k for k in firm[d].keys() if k != "total")
    census_new = sorted(now_keys - base_keys)
    total_held = all(abs(float(firm[d]["total"]) - float(base["firm_days"][d]["total"])) < TOL_HELD
                     for d in E91_CENSUS_DATES)
    advisors_same = advisors_count == base["advisor_count"]
    failing = set()
    if not in_range:
        failing.add("in_range")
    if census_new:
        failing.add("census")
    if not total_held:
        failing.add("total_held")
    if not advisors_same:
        failing.add("advisors_same")
    return {"ok": not failing, "falls": falls, "in_range": in_range, "census_new": census_new,
            "total_held": total_held, "advisors_same": advisors_same, "failing": failing}


def crit_unclassified(firm, six, c):
    lo, hi = 0.0, c["bound_max"] + TOL_UNCLASS_MARGIN
    rows = [(d, cents(d04_remainder(firm[d], six))) for d in c["unclass_dates"]]
    ok = all(lo <= rem <= hi for _, rem in rows)
    return ok, rows, hi


def crit_w86(firm, six):
    rows = []
    for d in E97_W86_DATES:
        gap = abs(float(firm[d]["unclassified"]) - d04_remainder(firm[d], six))
        rows.append((d, gap))
    return all(g < TOL_AUA for _, g in rows), rows


def crit_totals(firm, aua, dates):
    rows = [(d, float(firm[d]["total"]) - aua[d]) for d in dates]
    return all(abs(x) <= TOL_AUA for _, x in rows), rows


def crit_bars(views, bars, after_table):
    rows, ok = [], True
    for b in bars:
        ent = next((e for e in views.get(b["gran"], []) if e.get("period") == b["label"]), None)
        if ent is None:
            rows.append((b["label"], "MISSING"))
            ok = False
            continue
        total_ok = abs(float(ent["total_aua"]) - b["total_before"]) < TOL_HELD
        table = after_table[b["label"]]["classes"]
        worst, cls_ok = 0.0, True
        for cls, after in table.items():
            if cls not in ent:
                cls_ok = False
                continue
            gap = abs(float(ent[cls]["value"]) - after)
            worst = max(worst, gap)
            cls_ok = cls_ok and gap <= TOL_BAR_CLASS
        unclass_agrees = abs(table.get("unclassified", float("nan")) - b["unclass_after"]) < TOL_HELD
        rows.append((b["label"], "total_ok=%s" % total_ok, "worst_gap=%.2f" % worst))
        ok = ok and total_ok and cls_ok and unclass_agrees
    return ok, rows


def crit_advisors(served_adv, adv_rows, advisor_count):
    keys_served = set(served_adv.keys())
    keys_table = set(r["advisor_key"] for r in adv_rows)
    set_ok = keys_served == keys_table and len(keys_served) == advisor_count
    beyond = 0
    for r in adv_rows:
        day = served_adv.get(r["advisor_key"], {}).get(r["date"])
        reb = float(r["rebuilt_total"])
        if day is None:
            if abs(reb) >= TOL_HELD:
                beyond += 1
        elif abs(float(day["total"]) - reb) > TOL_ADVISOR:
            beyond += 1
    return set_ok and beyond == 0, set_ok, len(keys_served), beyond, len(adv_rows)


def crit_added_dropped(dd_rows, rel_dates):
    bad = []
    for r in dd_rows:
        dates = rel_dates.get(r["relationship_id"])
        if dates is None:
            bad.append((r["relationship_id"], r["date"], "UNREAD"))
            continue
        if (r["date"] in dates) != (r["side"] == "added"):
            bad.append((r["relationship_id"], r["date"], r["side"]))
    return not bad, len(dd_rows), len(bad)


def grade_e97(mds, mixsum, fmv, aua, rel_dates, c):
    """Returns (shipped, criteria dict name -> (bool, detail)). shipped is False when no restated_through."""
    if "restated_through" not in mds:
        return False, None
    firm = mds["firm"]
    crit = {}
    ok1, rows1, hi = crit_unclassified(firm, c["six"], c)
    crit["unclassified_window"] = (ok1, "bound_max=%.2f hi=%.2f rem=%s" % (
        c["bound_max"], hi, " ".join("%s=%.2f" % (d, r) for d, r in rows1)))
    ok2, rows2 = crit_w86(firm, c["six"])
    crit["w86_s5"] = (ok2, " ".join("%s=%.2f" % (d, g) for d, g in rows2))
    ok3, rows3 = crit_totals(firm, aua, c["dates"])
    crit["totals_aua"] = (ok3, "max_abs=%.2f n=%d" % (max(abs(x) for _, x in rows3), len(rows3)))
    ok4, rows4 = crit_bars(fmv["views"], c["bars"], c["after_table"])
    crit["bars"] = (ok4, " ".join(" ".join(str(x) for x in r) for r in rows4))
    ok5 = mds.get("restated_through") == E97_RESTATED and mixsum.get("restated_through") == E97_RESTATED
    crit["restated"] = (ok5, "mds=%s mix_summary=%s" % (mds.get("restated_through"),
                                                         mixsum.get("restated_through")))
    ok6, set_ok, nkeys, beyond, nrows = crit_advisors(mds["advisors"], c["adv_rows"], c["base"]["advisor_count"])
    crit["advisors"] = (ok6, "keys=%d set_equal=%s rows_beyond_250=%d of %d" % (nkeys, set_ok, beyond, nrows))
    ok7, nread, nbad = crit_added_dropped(c["dd_rows"], rel_dates)
    crit["added_dropped"] = (ok7, "rows_read=%d disagree=%d" % (nread, nbad))
    return True, crit


def e97_failing(mds, mixsum, fmv, aua, rel_dates, c):
    shipped, crit = grade_e97(mds, mixsum, fmv, aua, rel_dates, c)
    if not shipped:
        return {"shipped"}
    return set(n for n in E97_NAMES if not crit[n][0])


# ---------------------------------------------------------------- AWS reads (read-only)

def _aws(args):
    exe = str(ROOT / ".tools" / ("aws.cmd" if sys.platform == "win32" else "aws"))
    out = subprocess.run([exe] + args, capture_output=True)
    return out.returncode, out.stdout, out.stderr.decode("utf-8", "replace")


def head(key):
    rc, out, err = _aws(["s3api", "head-object", "--bucket", BUCKET, "--key", key, "--output", "json"])
    if rc != 0:
        raise RuntimeError("head-object %s rc=%d %s" % (key, rc, err.strip()[:200]))
    j = json.loads(out.decode("utf-8"))
    return {"VersionId": j.get("VersionId"), "LastModified": j.get("LastModified"),
            "ETag": j.get("ETag", "").strip('"')}


def get_bytes(key):
    rc, out, err = _aws(["s3", "cp", "s3://%s/%s" % (BUCKET, key), "-"])
    if rc != 0:
        raise RuntimeError("get %s rc=%d %s" % (key, rc, err.strip()[:200]))
    return out


def get_json(key):
    return json.loads(get_bytes(key).decode("utf-8"))


def list_prefix(prefix):
    """Every key under the prefix, paginated to exhaustion by continuation token. Returns (keys, pages)."""
    keys, pages, token = [], 0, None
    while True:
        args = ["s3api", "list-objects-v2", "--bucket", BUCKET, "--prefix", prefix, "--no-paginate",
                "--output", "json"]
        if token:
            args += ["--continuation-token", token]
        rc, out, err = _aws(args)
        if rc != 0:
            raise RuntimeError("list %s rc=%d %s" % (prefix, rc, err.strip()[:200]))
        j = json.loads(out.decode("utf-8"))
        pages += 1
        keys.extend((c["Key"], c["LastModified"]) for c in j.get("Contents", []))
        if not j.get("IsTruncated"):
            break
        token = j.get("NextContinuationToken")
        if not token:
            raise RuntimeError("list %s truncated without NextContinuationToken" % prefix)
    return keys, pages


def parse_iso(s):
    s = s.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    dt = datetime.datetime.fromisoformat(s)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=datetime.timezone.utc)
    return dt


def find_key(obj, name):
    """First value stored under `name` anywhere in a JSON object (printed only, never graded)."""
    if isinstance(obj, dict):
        if name in obj:
            return obj[name]
        for v in obj.values():
            hit = find_key(v, name)
            if hit is not None:
                return hit
    elif isinstance(obj, list):
        for v in obj:
            hit = find_key(v, name)
            if hit is not None:
                return hit
    return None


def fmt_usd(x):
    return "NONE" if x is None else "%.2f" % float(x)


# ---------------------------------------------------------------- subcommands

def cmd_e91(since):
    c = load_committed()
    base = c["base"]
    served = {k: head(k) for k in base["served_versions"]}
    for k in base["served_versions"]:
        print("E91-READ %s VersionId=%s baseline=%s LastModified=%s" % (
            k, served[k]["VersionId"], base["served_versions"][k]["VersionId"], served[k]["LastModified"]))
    if served[K_MDS]["VersionId"] == base["served_versions"][K_MDS]["VersionId"]:
        print("E91-LEGG state=NO-CHANGE-SINCE-BASELINE")
        print("E91-NOTE the mix daily summary carries the baseline VersionId: a fire that moved nothing and no fire "
              "at all look the same here; read the runner's C_06 telemetry beside this line")
        rc_final = 3
    else:
        mds = get_json(K_MDS)
        mixsum = get_json(K_MIXSUM)
        bounds = base["reach_bounds_usd"]
        g = grade_e91({d: mds["firm"][d] for d in E91_CENSUS_DATES}, len(mds["advisors"]), base, c["six"], bounds)
        print("E91-LEGG state=CHANGED ok=%s d10_09_fall=%s d10_08_fall=%s in_range=%s census_new=%d total_held=%s "
              "advisors_same=%s" % (g["ok"], fmt_usd(g["falls"]["2026-10-09"]), fmt_usd(g["falls"]["2026-10-08"]),
                                    g["in_range"], len(g["census_new"]), g["total_held"], g["advisors_same"]))
        print("E91-DETAIL census_new_keys=%s reach_10_09=%s reach_10_08=%s advisors_now=%d advisor_count=%d" % (
            g["census_new"], fmt_usd(bounds["2026-10-09"]), fmt_usd(bounds["2026-10-08"]),
            len(mds["advisors"]), base["advisor_count"]))
        un = find_key(mixsum, "Unclassified")
        now_line = find_key(un, "market_value") if isinstance(un, dict) else None
        print("E91-PRINTED d04_page_unclassified_now=%s baseline_line=%s (printed, not graded)" % (
            fmt_usd(now_line), fmt_usd(base["mix_summary_unclassified_line"]["market_value"])))
        rc_final = 0 if g["ok"] else 1
    if since:
        t = parse_iso(since)
        keys, pages = list_prefix(ENT_PREFIX)
        n_mod = sum(1 for _, lm in keys if parse_iso(lm) >= t)
        print("E91-LEGG-B keys_modified_since=%d of %d pages=%d mds_unchanged_since=%s" % (
            n_mod, len(keys), pages, parse_iso(served[K_MDS]["LastModified"]) < t))
    return rc_final


def cmd_e97():
    import pandas as pd
    c = load_committed()
    t0 = time.time()
    h = head(K_MDS)
    mds = get_json(K_MDS)
    print("E97-READ mix_daily_summary VersionId=%s LastModified=%s" % (h["VersionId"], h["LastModified"]))
    if "restated_through" not in mds:
        print("E97-ACCEPT shipped=False ok=False")
        return 3
    mixsum = get_json(K_MIXSUM)
    fmv = get_json(K_FMV)
    t_cp = time.time()
    raw = get_bytes(K_CP)
    cp = pd.read_parquet(io.BytesIO(raw), columns=["date", "total_aua"])
    cp["date"] = pd.to_datetime(cp["date"])
    sums = cp.groupby("date")["total_aua"].sum()
    aua = {d: float(sums.loc[pd.Timestamp(d)]) for d in c["dates"] if pd.Timestamp(d) in sums.index}
    print("E97-READ client_performance rows=%d dates=%d read_s=%.2f column=total_aua groupby(date).sum "
          "(D_03.composition_artifacts.py:497-503)" % (len(cp), len(sums), time.time() - t_cp))
    print("E97-READ bound_source=%s bound_max=%.2f" % (c["bound_src"], c["bound_max"]))
    t_dd = time.time()
    rel_ids = sorted(set(r["relationship_id"] for r in c["dd_rows"]))

    def read_rel(rid):
        try:
            j = get_json(ENT_PREFIX + rid + ".json")
            return rid, set(e["date"] for e in j.get("mix", []))
        except Exception:
            return rid, None

    with ThreadPoolExecutor(max_workers=8) as pool:
        rel_dates = dict(pool.map(read_rel, rel_ids))
    dd_elapsed = time.time() - t_dd
    shipped, crit = grade_e97(mds, mixsum, fmv, aua, rel_dates, c)
    for name in E97_NAMES:
        ok, detail = crit[name]
        print("E97-C %s ok=%s %s" % (name, ok, detail))
    print("E97-TIME added_dropped_read_s=%.2f json_reads=%d rows=%d total_run_s=%.2f" % (
        dd_elapsed, len(rel_ids), len(c["dd_rows"]), time.time() - t0))
    ok = all(crit[n][0] for n in E97_NAMES)
    print("E97-ACCEPT shipped=True ok=%s unclassified_window=%s w86_s5=%s totals_aua=%s bars=%s restated=%s "
          "advisors=%s added_dropped=%s" % ((ok,) + tuple(crit[n][0] for n in E97_NAMES)))
    return 0 if ok else 1


# ---------------------------------------------------------------- selftest (no AWS)

def build_e97_fixture(c):
    """A post-act served object set built from the committed radius files: totals = AUA, remainder = the
    would-be after figure, stored unclassified key = that remainder, advisor-days = rebuilt, restated set."""
    firm = {}
    for d in c["dates"]:
        rem = c["after"][d]
        total = c["aua"][d]
        firm[d] = {"total": total, "equity": total - rem, "fixed_income": 0.0, "alternatives": 0.0,
                   "commodities": 0.0, "structured": 0.0, "cash": 0.0, "unclassified": rem, "other": 0.0}
    advisors = {}
    for r in c["adv_rows"]:
        advisors.setdefault(r["advisor_key"], {})[r["date"]] = {"total": float(r["rebuilt_total"])}
    rel_dates = {}
    for r in c["dd_rows"]:
        s = rel_dates.setdefault(r["relationship_id"], set())
        if r["side"] == "added":
            s.add(r["date"])
    mds = {"firm": firm, "advisors": advisors, "restated_through": E97_RESTATED}
    mixsum = {"restated_through": E97_RESTATED}
    views = {"quarterly": [], "monthly": [], "annually": []}
    for b in c["bars"]:
        ent = {"period": b["label"], "total_aua": b["total_before"]}
        for cls, val in c["after_table"][b["label"]]["classes"].items():
            ent[cls] = {"value": val}
        views[b["gran"]].append(ent)
    return mds, mixsum, {"views": views}, c["aua"], rel_dates


def build_e91_fixture(c):
    base = c["base"]
    firm = {}
    for d in E91_CENSUS_DATES:
        day = dict(base["firm_days"][d]["classes"])
        day["total"] = base["firm_days"][d]["total"]
        firm[d] = day
    for d in E91_FALL_DATES:
        firm[d]["equity"] = firm[d]["equity"] + base["reach_bounds_usd"][d] / 2.0
    return firm, base["advisor_count"]


def cmd_selftest():
    c = load_committed()
    base = c["base"]
    bounds = base["reach_bounds_usd"]
    firm, advc = build_e91_fixture(c)
    e91_pos = grade_e91(firm, advc, base, c["six"], bounds)["failing"]
    rows = []   # (label, kind, own, failing set, base failing set of its family)
    rows.append(("e91 positive (fall = half the bound on 10-08 and 10-09)", "POS", None, e91_pos, set()))

    def e91_neg(label, own, mutate):
        f2, a2 = copy.deepcopy(firm), advc
        mutate(f2)
        rows.append((label, "NEG", own, grade_e91(f2, a2, base, c["six"], bounds)["failing"], e91_pos))

    def m_in_range(f):
        f["2026-10-09"]["equity"] += bounds["2026-10-09"] + 1.0
    e91_neg("e91 neg in_range (10-09 fall = bound + $1)", "in_range", m_in_range)

    def m_census(f):
        f["2026-10-07"]["structured_new_key"] = 1.0
    e91_neg("e91 neg census (new class key)", "census", m_census)

    mds, mixsum, fmv, aua, rel_dates = build_e97_fixture(c)
    e97_pos = e97_failing(mds, mixsum, fmv, aua, rel_dates, c)
    rows.append(("e97 positive (post-act set from R23_RADIUS)", "POS", None, e97_pos, set()))

    def e97_neg(label, own, mutate):
        m2, x2, f2, a2 = copy.deepcopy(mds), copy.deepcopy(mixsum), copy.deepcopy(fmv), dict(aua)
        r2 = copy.deepcopy(rel_dates)
        mutate(m2, x2, f2, a2, r2)
        rows.append((label, "NEG", own, e97_failing(m2, x2, f2, a2, r2, c), e97_pos))

    def m_totals(m, x, f, a, r):
        d = "2026-10-02"
        m["firm"][d]["total"] += 5.0
        m["firm"][d]["equity"] += 5.0
    e97_neg("e97 neg totals_equal_aua (total off AUA by $5 on 10-02)", "totals_aua", m_totals)

    def m_w86(m, x, f, a, r):
        m["firm"]["2026-10-04"]["unclassified"] += 50.0
    e97_neg("e97 neg w86_s5 (key gap $50 on 10-04)", "w86_s5", m_w86)

    def m_bars(m, x, f, a, r):
        f["views"]["quarterly"][0]["structured"]["value"] += 1000.0
    e97_neg("e97 neg bars (2026-Q3 structured $1,000 off)", "bars", m_bars)

    def m_adv(m, x, f, a, r):
        del m["advisors"][sorted(m["advisors"].keys())[0]]
    e97_neg("e97 neg advisors (one advisor key missing)", "advisors", m_adv)

    def m_dd(m, x, f, a, r):
        row = next(rw for rw in c["dd_rows"] if rw["side"] == "dropped")
        r.setdefault(row["relationship_id"], set()).add(row["date"])
    e97_neg("e97 neg added_dropped (dropped relationship still carries its date)", "added_dropped", m_dd)

    def m_restated(m, x, f, a, r):
        del m["restated_through"]
    e97_neg("e97 neg restated absent (shipped=False)", "shipped", m_restated)

    print("R24-SELFTEST-FIXTURES built from %s and %s" % (BASELINE_PATH.name, RADIUS.name))
    pos_ok, pos_n, neg_strict, neg_delta, neg_n = 0, 0, 0, 0, 0
    for label, kind, own, failing, base_fail in rows:
        if kind == "POS":
            pos_n += 1
            pos_ok += 1 if not failing else 0
            print("R24-FIX %s ok=%s failing=%s" % (label, not failing, sorted(failing)))
        else:
            neg_n += 1
            strict = failing == {own}
            delta = (failing - base_fail) == {own}
            neg_strict += 1 if strict else 0
            neg_delta += 1 if delta else 0
            print("R24-FIX %s failing=%s strict=%s delta_vs_positive=%s" % (label, sorted(failing), strict, delta))
    print("R24-SELFTEST-DELTA negatives_relative_to_their_positive=%d of %d" % (neg_delta, neg_n))
    ok = (pos_ok == pos_n) and (neg_strict == neg_n)
    print("R24-SELFTEST ok=%s positives=%d of %d negatives=%d of %d" % (ok, pos_ok, pos_n, neg_strict, neg_n))
    return 0 if ok else 1


def main(argv):
    if not argv:
        print("usage: r24_legg_read.py e91 [--since <ISO UTC>] | e97 | selftest")
        return 2
    cmd = argv[0]
    if cmd == "e91":
        since = argv[argv.index("--since") + 1] if "--since" in argv else None
        return cmd_e91(since)
    if cmd == "e97":
        return cmd_e97()
    if cmd == "selftest":
        return cmd_selftest()
    print("unknown subcommand %s" % cmd)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
