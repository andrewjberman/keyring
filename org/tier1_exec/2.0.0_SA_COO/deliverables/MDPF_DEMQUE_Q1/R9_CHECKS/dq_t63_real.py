"""MDPF_DEMQUE round 9, DQ-t-63 criterion AC2 (REAL S3 reads of the Rival Funds stores, READ ONLY, NO vendor call, writes only the scratch directory it is given).

`etfs_rivals_intake.py --build --day 2026-10-13 --out-dir <scratch>` builds the seven Bloomberg requests for the ETFS_RIVALS backfill gaps (Andrew-direct 2026-10-14 via CTO msg 5713; rows cited in
BACKFILL_GAPS_FOR_DEMQUE.md @c9e98081a6): total return on held days in three disjoint newest-first stages (D30, D90, D365), the close on dialog-curve days in the same three stages, and DVD_HIST_ALL for the
securities with no corporate-actions row. The check requires: seven request files with the ids below; every request validates under bbg_quote._validate; need_class non_client, tier 3, vendor bloomberg;
every dates entry on a trading day on or after 2025-10-13 with the stage's window; the three stages of one field disjoint per (security, date); the TR 365-day union within 1 percent of the measured 123,933
units; the close 365-day union within 1 percent of the measured 89,216 units (the 2026-10-13 page); the dividend request holds exactly the 70 securities of the pinned names file, as one reference cell each;
the build line's cell counts equal bbg_quote's own count per request; two builds are byte-identical; no key naming an account and zero hits from the account-id oracle where its hash list is present.
INTAKE-REAL-OK; else INTAKE-REAL-BAD <why>.
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
from datetime import date, timedelta

D = os.path.join("data", "mdpf", "scripts", "demque")
NAMES = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "deliverables", "2.0.0_SA_COO~Q1", "ETFS_RIVALS_DVD70_NAMES.json")
DAY = "2026-10-13"
ASOF = date(2026, 10, 12)  # the previous trading day of the page day
TR, CL, DV = "ETFS_RIVALS-C1-TR-HELD", "ETFS_RIVALS-C1-CLOSE-CURVES", "ETFS_RIVALS-C1-DIVIDENDS"
IDS = [TR + "-D30", TR + "-D90", TR + "-D365", CL + "-D30", CL + "-D90", CL + "-D365", DV]
FLOOR = "2025-10-13"


def _bad(why):
    print("INTAKE-REAL-BAD " + why)
    return 1


def _build(out_dir):
    r = subprocess.run([sys.executable, os.path.join(D, "etfs_rivals_intake.py"), "--build", "--day", DAY, "--out-dir", out_dir],
                       capture_output=True, text=True, timeout=250, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip())
    return json.loads(ls[-1]), ""


def _keys(o):
    if isinstance(o, dict):
        for k, v in o.items():
            yield str(k)
            yield from _keys(v)
    elif isinstance(o, list):
        for v in o:
            yield from _keys(v)


def _units(req):
    return {(s.get("bloomberg"), d) for s in req["securities"] for d in (s.get("dates") or [])}


def main() -> int:
    d = tempfile.mkdtemp(prefix="dq_t63_")
    a, b = os.path.join(d, "a"), os.path.join(d, "b")
    os.makedirs(a)
    os.makedirs(b)
    line, e = _build(a)
    if line is None:
        return _bad("build " + e)
    print("build " + json.dumps(line, sort_keys=True)[:600])
    line2, e = _build(b)
    if line2 is None:
        return _bad("second build " + e)
    reqs = {}
    for rid in IDS:
        p = os.path.join(a, rid + ".json")
        q = os.path.join(b, rid + ".json")
        if not os.path.isfile(p) or not os.path.isfile(q):
            return _bad("missing request file " + rid + ".json")
        if hashlib.sha256(open(p, "rb").read()).hexdigest() != hashlib.sha256(open(q, "rb").read()).hexdigest():
            return _bad("not byte-identical across two builds: " + rid)
        reqs[rid] = json.load(open(p, encoding="utf-8"))
    sys.path.insert(0, os.getcwd())  # the worktree root, so `lib` resolves on a plain run (row W55-S4)
    sys.path.insert(0, D)
    import bbg_quote
    from lib import trading_calendar as tc
    arms = {}
    arms["valid"] = True
    arms["fields_class_tier"] = True
    for rid, r in reqs.items():
        try:
            bbg_quote._validate(r)
        except Exception as exc:  # noqa: BLE001
            print("validate %s: %s" % (rid, str(exc)[:200]))
            arms["valid"] = False
        want = {TR: ["DAY_TO_DAY_TOT_RETURN_GROSS_DVDS"], CL: ["PX_LAST"], DV: ["DVD_HIST_ALL"]}[rid.rsplit("-D", 1)[0] if "-D3" in rid or "-D9" in rid else DV]
        if not (r.get("need_class") == "non_client" and r.get("tier") == 3 and r.get("vendor") == "bloomberg" and r.get("fields") == want and r.get("request_id") == rid):
            arms["fields_class_tier"] = False
    # the stage windows (calendar days before the as-of day) and the floor
    win = {"D30": (ASOF - timedelta(days=30), None), "D90": (ASOF - timedelta(days=90), ASOF - timedelta(days=30)), "D365": (date.fromisoformat(FLOOR), ASOF - timedelta(days=90))}
    ok_dates = True
    sets = {}
    for base in (TR, CL):
        for st, (lo, hi) in win.items():
            u = _units(reqs[base + "-" + st])
            sets[(base, st)] = u
            for _, x in u:
                xd = date.fromisoformat(x)
                if not (xd >= max(lo, date.fromisoformat(FLOOR)) and (hi is None or xd < hi) and tc.is_trading_day(xd)):
                    ok_dates = False
    arms["stage_windows_and_trading_days"] = ok_dates
    arms["disjoint"] = all(not (sets[(b0, "D30")] & sets[(b0, "D90")]) and not (sets[(b0, "D30")] & sets[(b0, "D365")]) and not (sets[(b0, "D90")] & sets[(b0, "D365")]) for b0 in (TR, CL))
    tr_total = sum(len(sets[(TR, s)]) for s in win)
    cl_total = sum(len(sets[(CL, s)]) for s in win)
    print("TR union units %d (measured 123,933); close union units %d (measured 89,216)" % (tr_total, cl_total))
    arms["tr_within_1pct"] = abs(tr_total - 123933) <= 1240
    arms["close_within_1pct"] = abs(cl_total - 89216) <= 893
    names = {n["bloomberg"] for n in json.load(open(NAMES, encoding="utf-8"))["names"]}
    dv = reqs[DV]
    arms["dividends_exact_70_reference"] = (dv.get("channel") == "reference" and {s.get("bloomberg") if isinstance(s, dict) else s for s in dv["securities"]} == names and len(names) == 70)
    # the build line's counts equal bbg_quote's own count (the allowance is not needed for the cell count)
    try:
        allow = json.load(open(os.path.join(D, "bbg_allowance.json"), encoding="utf-8"))
        counted = {rid: list(bbg_quote.quote(r, allow, 0, date.today())["cells"].values())[0] for rid, r in reqs.items()}
        said = {x["request_id"]: x["cells"] for x in line["requests"]}
        arms["cells_equal_bbg_quote"] = counted == said
        if counted != said:
            print("cells differ: counted %s said %s" % (counted, said))
    except Exception as exc:  # noqa: BLE001
        print("count compare error %s" % str(exc)[:200])
        arms["cells_equal_bbg_quote"] = False
    blob = json.dumps(reqs).encode("utf-8")
    oracle = True
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("cdc", os.path.join(".tools", "git-hooks", "client-data-check.py"))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        hashes = m._load_hashes(m._hash_list_path())
        hits = len(m.hits_in(blob, hashes))
        print("account-id oracle: %d hit line(s) against %d hashes" % (hits, len(hashes)))
        oracle = hits == 0
    except Exception as exc:  # noqa: BLE001
        print("account-id oracle NOT RUN on this device (%s)" % str(exc)[:80])
    arms["no_account_key"] = not any("account" in k.lower() for r in reqs.values() for k in _keys(r)) and oracle
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms failed: " + ",".join(bad))
    print("INTAKE-REAL-OK 7 requests, TR %d units, close %d units, 70 dividend securities, cells %s" % (tr_total, cl_total, json.dumps({x["request_id"]: x["cells"] for x in line["requests"]}, sort_keys=True)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
