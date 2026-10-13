#!/usr/bin/env python3
"""r24_legg_read.py -- MDPF_SECCLASS round 24, cell SC-e-99: the two leg-G instruments, read-only.

  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py e91 --fire-start <ISO UTC> [--since <ISO UTC>] [--mode canonical|legacy]
  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py e91 [--since <ISO UTC>] [--mode legacy]
  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py e97 [--mode canonical|legacy]
  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R24_CHECKS/r24_legg_read.py selftest

Run from the repo root. AWS is read-only (get-object by VersionId, head-object, list-object-versions, list-objects-v2,
s3 cp to stdout) through .tools/aws(.cmd). Every served key is located through lib/platinum_dest.py source(key, mode)
(the gold runner's own mapping); the mode defaults to canonical, the destination the runner writes since the FB-f-9 mode
move. A version body is fetched into a system temp file that is deleted before the verdict; nothing is written to the repo.
Every expected value is read from a committed file (the e91 baseline, R23_RADIUS, the SC-e-96 window
record, the request document, D_04 source) or from the order's stated tolerances; no expected dollar figure is typed.

Exit: 0 ok, 1 not ok, 2 usage, 3 the thing read has not happened yet (e91: the served mix daily summary has not moved
since --fire-start, or still carries the baseline VersionId in the legacy baseline path; e97: no restated_through key on
the served mix daily summary).
"""
import ast
import copy
import csv
import datetime
import importlib
import io
import json
import os
import subprocess
import sys
import tempfile
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path.cwd()
GOLD = ROOT / "data/black_diamond/scripts/gold"
if not (GOLD / "lib/platinum_dest.py").is_file():
    sys.exit("usage: run from the repo root (lib/platinum_dest.py not found under %s)" % GOLD)
sys.path.insert(0, str(GOLD))
_PD = importlib.import_module("lib.platinum_dest")   # the gold runner's own mapping, imported by path
source, list_target, DEST_MODES = _PD.source, _PD.list_target, _PD.MODES

DEFAULT_MODE = "canonical"
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
K_WM = "gold/meta/client_timeseries_watermark.json"
ENT_PREFIX = "gold/entities/clients/"
C06_PREFIXES = ["gold/entities/clients/", "gold/client_timeseries/"]   # the two prefixes C_06 writes under
C06_EXCLUDE_SUFFIX = "_composition.json"                                  # not a C_06 key (AMENDMENT 1, item 3)

E91_FALL_DATES = ["2026-10-08", "2026-10-09"]
E91_CENSUS_DATES = ["2026-10-06", "2026-10-07", "2026-10-08", "2026-10-09"]
E91_NAMES = ["in_range", "census", "total_held", "advisors_same"]
TOL_IN_RANGE_MARGIN = 250.0    # e91 in_range: "0 <= fall <= bound + 250" (AMENDMENT 2, item 3; the rounding of row D1-W85-S6)
E97_RESTATED = "2026-09-25"                        # criterion 5: the window cutoff (request: cutoff 2026-09-25)
E97_UNCLASS_RANGE = ("2026-09-30", "2026-10-06")   # criterion 1 dates
E97_W86_DATES = ["2026-10-03", "2026-10-04", "2026-10-05"]   # criterion 2 dates
E97_NAMES = ["unclassified_window", "w86_s5", "totals_aua", "bars", "restated", "advisors", "added_dropped"]
TOL_UNCLASS_LOWER = -250.0     # criterion 1 (AMENDMENT 1, item 1): "-250 <= remainder"
TOL_UNCLASS_MARGIN = 250.0     # criterion 1: "plus $250"
TOL_W86 = 250.0                # criterion 2 (AMENDMENT 1, item 2): "< 250"
TOL_AUA = 1.00                 # criterion 3 ("within $1.00")
PERIOD_BARS_SECTION = "## Period bars"   # the request's section that carries the per-class after figures (S4)
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
        if line.startswith(PERIOD_BARS_SECTION):
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


def day_from_baseline(base, d):
    """The committed baseline's day for d as a firm day (classes plus total), the shape grade_e91 reads."""
    day = dict(base["firm_days"][d]["classes"])
    day["total"] = base["firm_days"][d]["total"]
    return day


def grade_e91(before, firm, advisors_count, base, six, bounds):
    """before, firm: {date: day} for the census dates, BEFORE the fire and AFTER it (AMENDMENT 2, items 2-3).
    The fall is BEFORE's remainder minus AFTER's; in_range is 0 <= fall <= bound + $250. Returns the verdict pieces."""
    falls, in_range = {}, True
    for d in E91_FALL_DATES:
        fall = cents(d04_remainder(before[d], six) - d04_remainder(firm[d], six))
        falls[d] = fall
        in_range = in_range and (0.0 <= fall <= cents(bounds[d] + TOL_IN_RANGE_MARGIN))
    base_keys, now_keys = set(), set()
    for d in E91_CENSUS_DATES:
        base_keys |= set(k for k in before[d].keys() if k != "total")
        now_keys |= set(k for k in firm[d].keys() if k != "total")
    census_new = sorted(now_keys - base_keys)
    total_held = all(abs(float(firm[d]["total"]) - float(before[d]["total"])) < TOL_HELD
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
    lo, hi = TOL_UNCLASS_LOWER, c["bound_max"] + TOL_UNCLASS_MARGIN
    rows = [(d, cents(d04_remainder(firm[d], six))) for d in c["unclass_dates"]]
    ok = all(lo <= rem <= hi for _, rem in rows)
    return ok, rows, hi


def crit_w86(firm, six):
    rows = []
    for d in E97_W86_DATES:
        gap = abs(float(firm[d]["unclassified"]) - d04_remainder(firm[d], six))
        rows.append((d, gap))
    return all(g < TOL_W86 for _, g in rows), rows


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


def resolve_mode(mode):
    """The destination mode of a read: the flag, else DEFAULT_MODE (canonical). The environment is never consulted."""
    mode = DEFAULT_MODE if mode is None else mode
    if mode not in DEST_MODES:
        raise ValueError("mode %r is not one of %s" % (mode, DEST_MODES))
    return mode


def head(bucket, key):
    rc, out, err = _aws(["s3api", "head-object", "--bucket", bucket, "--key", key, "--output", "json"])
    if rc != 0:
        raise RuntimeError("head-object %s rc=%d %s" % (key, rc, err.strip()[:200]))
    j = json.loads(out.decode("utf-8"))
    return {"VersionId": j.get("VersionId"), "LastModified": j.get("LastModified"),
            "ETag": j.get("ETag", "").strip('"')}


def get_bytes(bucket, key):
    rc, out, err = _aws(["s3", "cp", "s3://%s/%s" % (bucket, key), "-"])
    if rc != 0:
        raise RuntimeError("get %s rc=%d %s" % (key, rc, err.strip()[:200]))
    return out


def get_json(bucket, key):
    return json.loads(get_bytes(bucket, key).decode("utf-8"))


def get_version_json(bucket, key, version_id):
    """One VERSION's body. s3api get-object writes the body to a file (its stdout carries only metadata), so the body
    goes to a system temp file that is read and deleted before this returns."""
    fd, path = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    try:
        rc, _out, err = _aws(["s3api", "get-object", "--bucket", bucket, "--key", key,
                              "--version-id", version_id, path])
        if rc != 0:
            raise RuntimeError("get-object %s VersionId=%s rc=%d %s" % (key, version_id, rc, err.strip()[:200]))
        return json.loads(Path(path).read_text(encoding="utf-8"))
    finally:
        os.remove(path)


def list_versions(bucket, key):
    """Every version and delete marker of exactly this key, newest-first is the caller's sort. The CLI auto-paginates
    this call; the rows are filtered to the key (--prefix matches longer keys too)."""
    rc, out, err = _aws(["s3api", "list-object-versions", "--bucket", bucket, "--prefix", key, "--output", "json"])
    if rc != 0:
        raise RuntimeError("list-object-versions %s rc=%d %s" % (key, rc, err.strip()[:200]))
    j = json.loads(out.decode("utf-8"))
    ents = []
    for v in j.get("Versions", []):
        if v["Key"] == key:
            ents.append({"VersionId": v["VersionId"], "LastModified": v["LastModified"],
                         "IsLatest": bool(v.get("IsLatest")), "IsDeleteMarker": False})
    for v in j.get("DeleteMarkers", []):
        if v["Key"] == key:
            ents.append({"VersionId": v["VersionId"], "LastModified": v["LastModified"],
                         "IsLatest": bool(v.get("IsLatest")), "IsDeleteMarker": True})
    return ents


def list_prefix(bucket, prefix):
    """Every key under the prefix, paginated to exhaustion by continuation token. Returns (keys, pages)."""
    keys, pages, token = [], 0, None
    while True:
        args = ["s3api", "list-objects-v2", "--bucket", bucket, "--prefix", prefix, "--no-paginate",
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


def latest_entry(entries):
    return max(entries, key=lambda e: parse_iso(e["LastModified"]))


def pick_before(entries, t):
    """The newest version (not a delete marker) whose LastModified is earlier than t, or None."""
    cands = [e for e in entries if not e["IsDeleteMarker"] and parse_iso(e["LastModified"]) < t]
    return max(cands, key=lambda e: parse_iso(e["LastModified"])) if cands else None


def fire_locate(versions_of, t, mode):
    """{legacy_key: (bucket, key, AFTER entry, BEFORE entry)} for the two e91 objects, located through source(key, mode).
    versions_of(bucket, key) returns the version entries of that exact object."""
    out = {}
    for k in (K_MDS, K_MIXSUM):
        b, mk = source(k, mode)
        ents = versions_of(b, mk)
        after = latest_entry(ents)
        if after["IsDeleteMarker"]:
            raise RuntimeError("%s carries a delete marker as its newest version" % mk)
        out[k] = (b, mk, after, pick_before(ents, t))
    return out


def fire_state(located):
    """CHANGED when the mix daily summary's newest version is not its newest version before the fire. The mix summary's
    own move is printed beside the line and not graded here: the leg-G object is the mix daily summary."""
    _b, _mk, after, before = located[K_MDS]
    if before is None:
        return "NO-BEFORE-VERSION"
    return "NO-CHANGE-SINCE-FIRE" if before["VersionId"] == after["VersionId"] else "CHANGED"


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


def num(x):
    return 0.0 if x is None else float(x)


def c06_eligible(entries, prefix):
    """C_06's keys under a prefix: no further '/' after the prefix, ending .json, not _composition.json.
    Subdirectory keys ({rid}/detail.json, written by D_02) are not C_06's and do not count (AMENDMENT 1, item 3)."""
    out = []
    for key, lm in entries:
        if not key.startswith(prefix):
            continue
        rest = key[len(prefix):]
        if "/" in rest or not rest.endswith(".json") or rest.endswith(C06_EXCLUDE_SUFFIX):
            continue
        out.append((key, lm))
    return out


def since_count(entries, prefix, t):
    """(keys modified at or after t, C_06 keys in the denominator) for one prefix's listing."""
    elig = c06_eligible(entries, prefix)
    return sum(1 for _, lm in elig if parse_iso(lm) >= t), len(elig)


# ---------------------------------------------------------------- subcommands

def print_verdict(g, base, mixsum, mds_advisors):
    bounds = base["reach_bounds_usd"]
    print("E91-LEGG state=CHANGED ok=%s d10_09_fall=%s d10_08_fall=%s in_range=%s census_new=%d total_held=%s "
          "advisors_same=%s" % (g["ok"], fmt_usd(g["falls"]["2026-10-09"]), fmt_usd(g["falls"]["2026-10-08"]),
                                g["in_range"], len(g["census_new"]), g["total_held"], g["advisors_same"]))
    print("E91-DETAIL census_new_keys=%s reach_10_09=%s reach_10_08=%s advisors_now=%d advisor_count=%d "
          "in_range_tolerance=bound+%.2f" % (g["census_new"], fmt_usd(bounds["2026-10-09"]),
                                             fmt_usd(bounds["2026-10-08"]), mds_advisors, base["advisor_count"],
                                             TOL_IN_RANGE_MARGIN))
    un = find_key(mixsum, "Unclassified")
    now_line = find_key(un, "market_value") if isinstance(un, dict) else None
    print("E91-PRINTED d04_page_unclassified_now=%s baseline_line=%s (printed, not graded)" % (
        fmt_usd(now_line), fmt_usd(base["mix_summary_unclassified_line"]["market_value"])))


def baseline_verdict(c, served, mode):
    """The amendment-1 comparison against the committed baseline: legacy mode only (the baseline VersionIds were read
    at the legacy destination; a canonical VersionId never equals them)."""
    base = c["base"]
    if served[K_MDS]["VersionId"] == base["served_versions"][K_MDS]["VersionId"]:
        print("E91-LEGG state=NO-CHANGE-SINCE-BASELINE")
        print("E91-NOTE the mix daily summary carries the baseline VersionId: a fire that moved nothing and no fire "
              "at all look the same here; read the runner's C_06 telemetry beside this line")
        return 3
    b, mk = source(K_MDS, mode)
    mds = get_json(b, mk)
    mixsum = get_json(*source(K_MIXSUM, mode))
    before = {d: day_from_baseline(base, d) for d in E91_CENSUS_DATES}
    g = grade_e91(before, {d: mds["firm"][d] for d in E91_CENSUS_DATES}, len(mds["advisors"]), base, c["six"],
                  base["reach_bounds_usd"])
    print_verdict(g, base, mixsum, len(mds["advisors"]))
    return 0 if g["ok"] else 1


def fire_verdict(c, t_fire, mode, served):
    """Leg G against the fire: BEFORE = the newest version before t_fire, AFTER = the current version (AMENDMENT 2, item 2)."""
    base = c["base"]
    bounds = base["reach_bounds_usd"]
    located = fire_locate(list_versions, t_fire, mode)
    state = fire_state(located)
    for k in (K_MDS, K_MIXSUM):
        b, mk, after, before = located[k]
        print("E91-VERSIONS %s bucket=%s key=%s after_VersionId=%s after_LastModified=%s head_agrees=%s "
              "before_VersionId=%s before_LastModified=%s" % (
                  k, b, mk, after["VersionId"], after["LastModified"], served[k]["VersionId"] == after["VersionId"],
                  before["VersionId"] if before else None, before["LastModified"] if before else None))
    if state == "NO-BEFORE-VERSION":
        print("E91-LEGG state=NO-BEFORE-VERSION fire_start=%s (no version of the mix daily summary is earlier than the "
              "fire start: the comparison cannot be graded)" % t_fire.isoformat())
        return 1
    if state == "NO-CHANGE-SINCE-FIRE":
        print("E91-LEGG state=NO-CHANGE-SINCE-FIRE fire_start=%s mds_VersionId=%s (the newest version is the newest "
              "before the fire: nothing at this destination moved since the fire start; a fire that moved nothing and "
              "no fire at all look the same here; read the runner's C_06 telemetry beside this line)" % (
                  t_fire.isoformat(), located[K_MDS][2]["VersionId"]))
        return 3
    b_mds, mk_mds, after, before = located[K_MDS]
    mds_before = get_version_json(b_mds, mk_mds, before["VersionId"])
    mds_after = get_version_json(b_mds, mk_mds, after["VersionId"])
    b_mix, mk_mix = source(K_MIXSUM, mode)
    mixsum = get_json(b_mix, mk_mix)
    bf, af = mds_before["firm"], mds_after["firm"]
    print("E91-BEFORE-AFTER mds BEFORE=%s AFTER=%s firm_dates BEFORE=%d AFTER=%d" % (
        before["VersionId"], after["VersionId"], len(bf), len(af)))
    # every firm day that changed between BEFORE and AFTER, printed with its fall and whether the day is named
    moved = []
    for d in sorted(set(bf) | set(af)):
        if d not in bf or d not in af:
            print("E91-MOVED date=%s absent_in=%s (printed, not graded)" % (d, "BEFORE" if d not in bf else "AFTER"))
            moved.append(d)
            continue
        keys = set(bf[d]) | set(af[d])
        changed = set(bf[d]) != set(af[d]) or any(
            abs(num(bf[d][k]) - num(af[d][k])) >= TOL_HELD for k in bf[d])
        if not changed:
            continue
        moved.append(d)
        fall = cents(d04_remainder(bf[d], c["six"]) - d04_remainder(af[d], c["six"]))
        same_total = abs(num(af[d]["total"]) - num(bf[d]["total"])) < TOL_HELD
        print("E91-MOVED date=%s fall=%s named=%s total_held=%s keys=%d (printed, graded only as the named pair)" % (
            d, fmt_usd(fall), d in bounds, same_total, len(keys)))
    print("E91-MOVED-COUNT firm_days_changed=%d of %d firm dates in BEFORE or AFTER; named=%d unnamed=%d" % (
        len(moved), len(set(bf) | set(af)), sum(1 for d in moved if d in bounds),
        sum(1 for d in moved if d not in bounds)))
    # the committed baseline against BEFORE, per census date: the same day values must read the same to the cent
    for d in E91_CENSUS_DATES:
        b_rem = float(base["firm_days"][d]["d04_remainder_unclassified"])
        v_rem = d04_remainder(bf[d], c["six"])
        print("E91-BASE-VS-BEFORE date=%s baseline_d04=%.2f before_d04=%.2f diff=%.2f baseline_total=%.2f "
              "before_total=%.2f moved_by_fire=%s" % (d, b_rem, v_rem, v_rem - b_rem,
                                                      float(base["firm_days"][d]["total"]), num(bf[d]["total"]),
                                                      d in moved))
    before_days = {d: bf[d] for d in E91_CENSUS_DATES}
    after_days = {d: af[d] for d in E91_CENSUS_DATES}
    g = grade_e91(before_days, after_days, len(mds_after["advisors"]), base, c["six"], bounds)
    print_verdict(g, base, mixsum, len(mds_after["advisors"]))
    return 0 if g["ok"] else 1


def since_block(t, mode):
    """The idempotence count on both destinations (AMENDMENT 2, item 4): C_06 keys only, each C_06 prefix listed where
    list_target maps it, every listed key mapped back to the legacy shape before the C_06 filter."""
    tot_mod, tot_n = 0, 0
    for legacy_prefix in C06_PREFIXES:
        bucket, prefix, to_legacy = list_target(legacy_prefix, mode)
        keys, pages = list_prefix(bucket, prefix)
        mapped = [(to_legacy(k), lm) for k, lm in keys]
        n_mod, n_elig = since_count(mapped, legacy_prefix, t)
        tot_mod += n_mod
        tot_n += n_elig
        print("E91-LEGG-B destination bucket=%s prefix=%s legacy_prefix=%s c06_keys_modified_since=%d of %d "
              "listed_total=%d pages=%d" % (bucket, prefix, legacy_prefix, n_mod, n_elig, len(keys), pages))
    return tot_mod, tot_n


def cmd_e91(since, fire_start, mode):
    c = load_committed()
    base = c["base"]
    t0 = time.time()
    t_fire = parse_iso(fire_start) if fire_start else None
    t_since = parse_iso(since) if since else None
    served = {}
    for k in base["served_versions"]:
        b, mk = source(k, mode)
        served[k] = head(b, mk)
        print("E91-READ %s bucket=%s key=%s VersionId=%s baseline=%s LastModified=%s" % (
            k, b, mk, served[k]["VersionId"], base["served_versions"][k]["VersionId"], served[k]["LastModified"]))
    if t_fire is not None:
        rc_final = fire_verdict(c, t_fire, mode, served)
    elif mode == "legacy":
        rc_final = baseline_verdict(c, served, mode)
    else:
        print("E91-LEGG state=FIRE-START-REQUIRED mode=%s (the baseline VersionIds were read at the legacy destination; "
              "a canonical VersionId cannot equal them: pass --fire-start)" % mode)
        rc_final = 2
    if t_since is not None:
        tot_mod, tot_n = since_block(t_since, mode)
        print("E91-LEGG-B keys_modified_since=%d of %d (C_06 keys, both destinations) mds_unchanged_since=%s" % (
            tot_mod, tot_n, parse_iso(served[K_MDS]["LastModified"]) < t_since))
    print("E91-TIME total_run_s=%.2f" % (time.time() - t0))
    return rc_final


def cmd_e97(mode):
    import pandas as pd
    c = load_committed()
    t0 = time.time()
    b_mds, mk_mds = source(K_MDS, mode)
    h = head(b_mds, mk_mds)
    mds = get_json(b_mds, mk_mds)
    print("E97-READ mix_daily_summary bucket=%s key=%s VersionId=%s LastModified=%s" % (
        b_mds, mk_mds, h["VersionId"], h["LastModified"]))
    if "restated_through" not in mds:
        print("E97-ACCEPT shipped=False ok=False")
        return 3
    b_mix, mk_mix = source(K_MIXSUM, mode)
    mixsum = get_json(b_mix, mk_mix)
    print("E97-READ mix_summary bucket=%s key=%s" % (b_mix, mk_mix))
    b_fmv, mk_fmv = source(K_FMV, mode)
    fmv = get_json(b_fmv, mk_fmv)
    print("E97-READ firm_mix_views bucket=%s key=%s" % (b_fmv, mk_fmv))
    t_cp = time.time()
    b_cp, mk_cp = source(K_CP, mode)
    raw = get_bytes(b_cp, mk_cp)
    cp = pd.read_parquet(io.BytesIO(raw), columns=["date", "total_aua"])
    cp["date"] = pd.to_datetime(cp["date"])
    sums = cp.groupby("date")["total_aua"].sum()
    aua = {d: float(sums.loc[pd.Timestamp(d)]) for d in c["dates"] if pd.Timestamp(d) in sums.index}
    print("E97-READ client_performance bucket=%s key=%s rows=%d dates=%d read_s=%.2f column=total_aua groupby(date).sum "
          "(D_03.composition_artifacts.py:497-503)" % (b_cp, mk_cp, len(cp), len(sums), time.time() - t_cp))
    print("E97-READ bound_source=%s bound_max=%.2f" % (c["bound_src"], c["bound_max"]))
    t_dd = time.time()
    rel_ids = sorted(set(r["relationship_id"] for r in c["dd_rows"]))
    rel_loc = {rid: source(ENT_PREFIX + rid + ".json", mode) for rid in rel_ids}
    by_bucket = Counter(b for b, _k in rel_loc.values())
    print("E97-READ relationship JSONs: %d objects, key template %s{relationship_id}.json, source() bucket counts %s"
          % (len(rel_ids), ENT_PREFIX, dict(by_bucket)))

    def read_rel(rid):
        b, mk = rel_loc[rid]
        try:
            j = get_json(b, mk)
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
    """BEFORE = the committed baseline's census days; AFTER = the same days with equity raised on 10-08 and 10-09 by half
    the bound, so each fall is half the bound."""
    base = c["base"]
    before = {d: day_from_baseline(base, d) for d in E91_CENSUS_DATES}
    after = copy.deepcopy(before)
    for d in E91_FALL_DATES:
        after[d]["equity"] = after[d]["equity"] + base["reach_bounds_usd"][d] / 2.0
    return before, after, base["advisor_count"]


def fire_store_fixture():
    """A versions store keyed by (bucket, key) as source() maps the served keys. The CANONICAL copies moved at the fire
    (newest version after 23:00Z, a pre-fire version at 07:29Z); the LEGACY copies carry one old version and did not move."""
    store = {}
    for k in (K_MDS, K_MIXSUM):
        cb, ck = source(k, "canonical")
        store[(cb, ck)] = [
            {"VersionId": "canon-after", "LastModified": "2026-10-13T00:23:32+00:00", "IsLatest": True, "IsDeleteMarker": False},
            {"VersionId": "canon-before", "LastModified": "2026-10-12T07:29:12+00:00", "IsLatest": False, "IsDeleteMarker": False}]
        lb, lk = source(k, "legacy")
        store[(lb, lk)] = [
            {"VersionId": "legacy-only", "LastModified": "2026-10-11T05:23:28+00:00", "IsLatest": True, "IsDeleteMarker": False}]
    return store


def fire_store_unmoved():
    """The canonical copies with no version after the fire start: the newest is the 07:29Z version (fire start 23:00Z)."""
    store = fire_store_fixture()
    for k in (K_MDS, K_MIXSUM):
        cb, ck = source(k, "canonical")
        store[(cb, ck)] = [{"VersionId": "canon-before", "LastModified": "2026-10-12T07:29:12+00:00",
                            "IsLatest": True, "IsDeleteMarker": False}]
    return store


def fire_failing(store, mode):
    """The fire-state grader: CHANGED passes; any other state, or a mode other than the default, is the failing 'state'."""
    located = fire_locate(lambda b, k: store[(b, k)], parse_iso(FIXTURE_FIRE_START), mode)
    st = fire_state(located)
    failing = set()
    if st != "CHANGED":
        failing.add("state")
    if resolve_mode(None) != DEFAULT_MODE:
        failing.add("mode")
    return failing, st


FIXTURE_FIRE_START = "2026-10-12T23:00:00Z"


def cmd_selftest():
    c = load_committed()
    base = c["base"]
    bounds = base["reach_bounds_usd"]
    before, firm, advc = build_e91_fixture(c)
    e91_pos = grade_e91(before, firm, advc, base, c["six"], bounds)["failing"]
    rows = []   # (label, kind, own, failing set, base failing set of its family)
    rows.append(("e91 positive (fall = half the bound on 10-08 and 10-09)", "POS", None, e91_pos, set()))
    rem_gap = {d: abs(d04_remainder(before[d], c["six"]) - float(base["firm_days"][d]["d04_remainder_unclassified"]))
               for d in E91_CENSUS_DATES}
    rows.append(("e91 positive (baseline day values reproduce the committed D_04 remainder to the cent)", "POS", None,
                 set() if max(rem_gap.values()) < TOL_HELD else {"baseline_remainder"}, set()))
    fire_ok, fire_st = fire_failing(fire_store_fixture(), resolve_mode(None))
    rows.append(("e91 fire positive (default mode reads the canonical destination; state %s)" % fire_st,
                 "POS", None, fire_ok, set()))
    t_fix = parse_iso("2026-10-12T05:00:00Z")
    fix_entries = [("gold/entities/clients/z1.json", "2026-10-12T06:00:00+00:00"),
                   ("gold/entities/clients/z1_views.json", "2026-10-12T06:00:00+00:00"),
                   ("gold/entities/clients/z1/detail.json", "2026-10-12T06:00:00+00:00"),
                   ("gold/entities/clients/z1_composition.json", "2026-10-12T06:00:00+00:00"),
                   ("gold/entities/clients/z2.json", "2026-10-11T06:00:00+00:00")]
    got = since_count(fix_entries, "gold/entities/clients/", t_fix)
    rows.append(("e91 --since counting fixture (2 modified of 3 C_06 keys; subdir and _composition excluded)",
                 "POS", None, set() if got == (2, 3) else {"listing"}, set()))

    def e91_neg(label, own, mutate):
        f2, a2 = copy.deepcopy(firm), advc
        mutate(f2)
        rows.append((label, "NEG", own, grade_e91(before, f2, a2, base, c["six"], bounds)["failing"], e91_pos))

    def m_in_range(f):
        # AMENDMENT 2, item 3: the tolerance is bound + $250, so the negative is the fall of bound + $251 (the old
        # "bound + $1" is inside the tolerance now and could not fail; it is replaced, not weakened)
        f["2026-10-09"]["equity"] = before["2026-10-09"]["equity"] + bounds["2026-10-09"] + (TOL_IN_RANGE_MARGIN + 1.0)
    e91_neg("e91 neg in_range (10-09 fall = bound + $251)", "in_range", m_in_range)

    def m_census(f):
        f["2026-10-07"]["structured_new_key"] = 1.0
    e91_neg("e91 neg census (new class key)", "census", m_census)

    # AMENDMENT 2, item 6: a fire-state negative per control. Each must fail on exactly the 'state' criterion.
    unmoved_failing, st_unmoved = fire_failing(fire_store_unmoved(), resolve_mode(None))
    rows.append(("e91 neg canonical BEFORE equal to AFTER (state %s)" % st_unmoved, "NEG", "state",
                 unmoved_failing, set()))
    st_legacy_failing, st_legacy = fire_failing(fire_store_fixture(), "legacy")
    rows.append(("e91 neg legacy-mode read of a canonical-only move (state %s, a read the default must not make)"
                 % st_legacy, "NEG", "state", st_legacy_failing, set()))

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
        m["firm"]["2026-10-04"]["unclassified"] += TOL_W86 + 1.0
    e97_neg("e97 neg w86_s5 (key gap = tolerance $250 + $1 on 10-04)", "w86_s5", m_w86)

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


def opt(argv, name):
    """The value after a --flag, or None. A flag without a value is a usage error (returns the sentinel 'MISSING')."""
    if name not in argv:
        return None
    i = argv.index(name)
    return argv[i + 1] if i + 1 < len(argv) else "MISSING"


def main(argv):
    if not argv:
        print("usage: r24_legg_read.py e91 [--fire-start <ISO UTC>] [--since <ISO UTC>] [--mode canonical|legacy] | "
              "e97 [--mode canonical|legacy] | selftest")
        return 2
    cmd = argv[0]
    if cmd in ("e91", "e97"):
        mode_arg = opt(argv, "--mode")
        if mode_arg == "MISSING" or (mode_arg is not None and mode_arg not in DEST_MODES):
            print("usage: --mode takes one of %s" % (DEST_MODES,))
            return 2
        mode = resolve_mode(mode_arg)
    if cmd == "e91":
        since, fire_start = opt(argv, "--since"), opt(argv, "--fire-start")
        if "MISSING" in (since, fire_start):
            print("usage: --since and --fire-start take an ISO UTC value")
            return 2
        return cmd_e91(since, fire_start, mode)
    if cmd == "e97":
        return cmd_e97(mode)
    if cmd == "selftest":
        return cmd_selftest()
    print("unknown subcommand %s" % cmd)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
