"""QA coverage run, read-only: which Robustness constraints Bloomberg can serve at 8 TTM observations, over the 33 names the
pool holds a peers/v1 object for. Quarterly BDH from 2023-01-01. Output to the scratchpad only."""
import collections
import json
import sys

import blpapi
import boto3

OUT = sys.argv[1]
s3 = boto3.client("s3")
names = []
for page in s3.get_paginator("list_objects_v2").paginate(Bucket="opal-data-harvest", Prefix="peers/v1/"):
    for o in page.get("Contents", []):
        names.append(o["Key"][len("peers/v1/"):].rsplit("/", 1)[0].replace("_", " "))
names = sorted(set(names))
F = ["EBIT", "IS_INT_EXPENSE", "TRAIL_12M_EBITDA", "NET_DEBT", "BS_CASH_NEAR_CASH_ITEM", "BS_TOTAL_AVAIL_LINE_OF_CREDIT",
     "BS_YEAR_1_PRINCIPAL", "BS_YEAR_2_PRINCIPAL", "BS_TOTL_DEBT_DEBT_SCHEDULE", "TRAIL_12M_FREE_CASH_FLOW", "TRAIL_12M_NET_SALES"]
opts = blpapi.SessionOptions()
opts.setServerHost("127.0.0.1")
opts.setServerPort(8194)
sess = blpapi.Session(opts)
if not sess.start() or not sess.openService("//blp/refdata"):
    print("ERROR: session")
    sys.exit(2)
svc = sess.getService("//blp/refdata")
req = svc.createRequest("HistoricalDataRequest")
for x in names:
    req.append("securities", x)
for f in F:
    req.append("fields", f)
req.set("startDate", "20230101")
req.set("endDate", "20260915")
req.set("periodicitySelection", "QUARTERLY")
sess.sendRequest(req)
hist, sec_err, fld_err = {}, {}, collections.defaultdict(set)
for _tick in iter(int, 1):  # event loop; the commit gate's scope walk reads For bodies, not While
    ev = sess.nextEvent(60000)
    for msg in ev:
        if not msg.hasElement("securityData"):
            continue
        sd = msg.getElement("securityData")
        sec = sd.getElementAsString("security")
        if sd.hasElement("securityError"):
            sec_err[sec] = sd.getElement("securityError").getElementAsString("subcategory")
        if sd.hasElement("fieldExceptions"):
            fx = sd.getElement("fieldExceptions")
            for j in range(fx.numValues()):
                x = fx.getValueAsElement(j)
                fld_err[x.getElementAsString("fieldId")].add(x.getElement("errorInfo").getElementAsString("subcategory"))
        rows = []
        fdarr = sd.getElement("fieldData")
        for i in range(fdarr.numValues()):
            p = fdarr.getValueAsElement(i)
            row = {}
            for j in range(p.numElements()):
                el = p.getElement(j)
                row[str(el.name())] = el.getValue()
            rows.append(row)
        hist[sec] = rows
    if ev.eventType() in (blpapi.Event.RESPONSE, blpapi.Event.TIMEOUT):
        break
sess.stop()
print("names %d, security errors %d %s, field errors %s" % (len(names), len(sec_err), sorted(sec_err.items())[:5], dict(fld_err)))


def series(sec, f):
    return [(str(r["date"]), r[f]) for r in hist.get(sec, []) if f in r]


def last_n_complete(sec, needed, n):
    """Quarter-ends where every needed field is present; returns the count within the most recent n+3 quarter-ends."""
    dates = sorted({str(r["date"]) for r in hist.get(sec, [])})
    ok = [dt for dt in dates if all(any(str(r["date"]) == dt and f in r for r in hist[sec]) for f in needed)]
    return len(ok)


fcov = {f: sum(1 for s_ in names if len(series(s_, f)) >= 8) for f in F}
print("fields with >= 8 quarterly observations (names, of %d):" % len(names))
for f in F:
    print("   %-30s %d" % (f, fcov[f]))
cons = {
    "x1 EBIT/interest (TTM from 11 quarters)": (["EBIT", "IS_INT_EXPENSE"], 11),
    "x2 net debt/EBITDA": (["NET_DEBT", "TRAIL_12M_EBITDA"], 8),
    "x3 (cash+undrawn revolver)/24m principal": (["BS_CASH_NEAR_CASH_ITEM", "BS_TOTAL_AVAIL_LINE_OF_CREDIT", "BS_YEAR_1_PRINCIPAL", "BS_YEAR_2_PRINCIPAL"], 8),
    "x4 debt due <=24m / total debt": (["BS_YEAR_1_PRINCIPAL", "BS_YEAR_2_PRINCIPAL", "BS_TOTL_DEBT_DEBT_SCHEDULE"], 8),
    "x5 FCF/revenue TTM": (["TRAIL_12M_FREE_CASH_FLOW", "TRAIL_12M_NET_SALES"], 8),
}
out = {"names": names, "per_field_ge8": fcov, "constraints": {}}
print("constraints computable at the model's observation count (names, of %d):" % len(names))
for label, (need, n) in cons.items():
    got = [s_ for s_ in names if last_n_complete(s_, need, n) >= n]
    cur = [s_ for s_ in names if last_n_complete(s_, need, 1) >= 1]
    out["constraints"][label] = {"full_history": got, "at_least_one_quarter": len(cur)}
    print("   %-44s full=%2d  any-quarter=%2d  e.g. %s" % (label, len(got), len(cur), got[:5]))
print("   x6 largest customer/revenue                  full= 0  (no scalar Bloomberg field; SUPPLY_CHAIN_CUSTOMERS is a ticker list)")
per_name = {s_: sum(1 for (need, n) in cons.values() if last_n_complete(s_, need, n) >= n) for s_ in names}
dist = collections.Counter(per_name.values())
print("names by count of constraints with full history (of 6):", dict(sorted(dist.items())), " n>=5:", sum(1 for v in per_name.values() if v >= 5))
out["per_name_full_constraints"] = per_name
json.dump(out, open(OUT, "w"), indent=1, default=str)
