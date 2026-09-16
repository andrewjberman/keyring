"""Read-only: Bloomberg consensus inputs for the Divergence score over the 33 pool names, blended-forward 12m.
Candidate mnemonics are requested together and every field error is printed, so an invalid name reads as INVALID, not as absent data."""
import collections
import json
import sys

import blpapi
import boto3

s3 = boto3.client("s3")
names = set()
for page in s3.get_paginator("list_objects_v2").paginate(Bucket="opal-data-harvest", Prefix="peers/v1/"):
    for o in page.get("Contents", []):
        names.add(o["Key"][len("peers/v1/"):].rsplit("/", 1)[0].replace("_", " "))
names = sorted(names)
F = ["BEST_ESTIMATE_FCF", "BEST_PERIOD_END_DT", "BEST_CALCULATED_FCF", "BEST_SALES", "BEST_ESTIMATE_FCF_STDDEV", "BEST_FCF_STDDEV",
     "BEST_ESTIMATE_FCF_NUMEST", "BEST_FCF_NUMEST", "BEST_ESTIMATE_FCF_HI", "BEST_ESTIMATE_FCF_LO", "BEST_EPS_STDDEV",
     "BEST_EPS_NUMEST", "BEST_ANALYST_RATING", "BEST_CPS", "BEST_CPS_STDDEV", "BEST_CPS_NUMEST", "BEST_EST_FCF_MEDIAN",
     "BEST_ESTIMATE_FCF_MEDIAN", "EQY_FUND_CRNCY", "CRNCY"]
opts = blpapi.SessionOptions()
opts.setServerHost("127.0.0.1")
opts.setServerPort(8194)
sess = blpapi.Session(opts)
if not sess.start() or not sess.openService("//blp/refdata"):
    sys.exit("ERROR: session")
svc = sess.getService("//blp/refdata")
req = svc.createRequest("ReferenceDataRequest")
for x in names:
    req.append("securities", x)
for f in F:
    req.append("fields", f)
o = req.getElement("overrides").appendElement()
o.setElement("fieldId", "BEST_FPERIOD_OVERRIDE")
o.setElement("value", sys.argv[2])
sess.sendRequest(req)
data, ferr = {}, collections.defaultdict(collections.Counter)
for _tick in iter(int, 1):  # event loop; the commit gate's scope walk reads For bodies, not While
    ev = sess.nextEvent(60000)
    for msg in ev:
        if not msg.hasElement("securityData"):
            continue
        sd = msg.getElement("securityData")
        for i in range(sd.numValues()):
            e = sd.getValueAsElement(i)
            sec = e.getElementAsString("security")
            row = {}
            fd = e.getElement("fieldData")
            for j in range(fd.numElements()):
                el = fd.getElement(j)
                row[str(el.name())] = el.getValue()
            if e.hasElement("fieldExceptions"):
                fx = e.getElement("fieldExceptions")
                for j in range(fx.numValues()):
                    x = fx.getValueAsElement(j)
                    ferr[x.getElementAsString("fieldId")][x.getElement("errorInfo").getElementAsString("subcategory")] += 1
            data[sec] = row
    if ev.eventType() in (blpapi.Event.RESPONSE, blpapi.Event.TIMEOUT):
        break
sess.stop()
print("names %d; coverage with BEST_FPERIOD_OVERRIDE=%s:" % (len(names), sys.argv[2]))
for f in F:
    print("   %-28s values=%2d  errors=%s" % (f, sum(1 for s_ in names if f in data.get(s_, {})), dict(ferr.get(f, {}))))
for s_ in ["BA US Equity", "COST US Equity", "HD US Equity", "SAP GY Equity", "BABA US Equity"]:
    print("  ", s_, json.dumps(data.get(s_), default=str)[:420])
json.dump(data, open(sys.argv[1], "w"), indent=1, default=str)
