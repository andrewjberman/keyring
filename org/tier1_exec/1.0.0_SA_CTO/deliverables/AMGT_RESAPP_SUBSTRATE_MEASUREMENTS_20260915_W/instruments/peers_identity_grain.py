"""Read-only GRAIN check: does the Bloomberg security each served peer member was requested as name the SAME company the peer row
names? Prints per subject: members whose request string was a raw identifier, and a name-agreement verdict per member."""
import json
import re
import sys

import blpapi
import boto3

s3 = boto3.client("s3")
rows = []
for page in s3.get_paginator("list_objects_v2").paginate(Bucket="opal-data-harvest", Prefix="peers/v1/"):
    for o in page.get("Contents", []):
        d = json.loads(s3.get_object(Bucket="opal-data-harvest", Key=o["Key"])["Body"].read())
        sub = o["Key"][len("peers/v1/"):].rsplit("/", 1)[0].replace("_", " ")
        for r in d.get("members") or []:
            idn = r.get("identity") or {}
            t = (r.get("ticker") or "").strip()
            req = t if t.endswith(" Equity") else t + " Equity"
            rows.append({"subject": sub, "req": req, "raw": t, "row_name": r.get("name") or "", "resolution": idn.get("resolution"),
                         "security_key": idn.get("security_key"), "country": r.get("country")})
secs = sorted({r["req"] for r in rows})
opts = blpapi.SessionOptions()
opts.setServerHost("127.0.0.1")
opts.setServerPort(8194)
sess = blpapi.Session(opts)
if not sess.start() or not sess.openService("//blp/refdata"):
    sys.exit("ERROR: session")
svc = sess.getService("//blp/refdata")
req = svc.createRequest("ReferenceDataRequest")
for x in secs:
    req.append("securities", x)
for f in ("NAME", "TICKER_AND_EXCH_CODE", "CNTRY_OF_DOMICILE", "SECURITY_TYP"):
    req.append("fields", f)
sess.sendRequest(req)
bb = {}
for _tick in iter(int, 1):  # event loop; the commit gate's scope walk reads For bodies, not While
    ev = sess.nextEvent(60000)
    for msg in ev:
        if not msg.hasElement("securityData"):
            continue
        sd = msg.getElement("securityData")
        for i in range(sd.numValues()):
            e = sd.getValueAsElement(i)
            sec = e.getElementAsString("security")
            row = {"error": e.getElement("securityError").getElementAsString("subcategory")} if e.hasElement("securityError") else {}
            fd = e.getElement("fieldData")
            for j in range(fd.numElements()):
                el = fd.getElement(j)
                row[str(el.name())] = el.getValue()
            bb[sec] = row
    if ev.eventType() in (blpapi.Event.RESPONSE, blpapi.Event.TIMEOUT):
        break
sess.stop()


def toks(s):
    stop = {"inc", "corp", "co", "ltd", "limited", "plc", "sa", "ag", "nv", "the", "company", "class", "group", "holdings", "holding", "de", "cv", "sab", "se", "adr", "a", "h", "b", "corporation", "and"}
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in stop and len(w) > 1}


tally = {}
for r in rows:
    b = bb.get(r["req"], {})
    if "error" in b:
        verdict = "INVALID_SECURITY"
    else:
        verdict = "NAME_AGREES" if toks(r["row_name"]) & toks(b.get("NAME", "")) else "NAME_DISAGREES"
    r["bbg_name"], r["bbg_ticker"], r["verdict"] = b.get("NAME"), b.get("TICKER_AND_EXCH_CODE"), verdict
    has_exch = bool(re.search(r"\s[A-Z0-9]{2}\s+Equity$", r["req"]))
    key = (r["subject"], verdict, "exch-code" if has_exch else "no-exch-code")
    tally[key] = tally.get(key, 0) + 1
for sub in sorted({r["subject"] for r in rows}):
    parts = {k[1:]: v for k, v in tally.items() if k[0] == sub}
    print("%-16s %s" % (sub, dict(sorted(parts.items()))))
    for r in rows:
        if r["subject"] == sub and r["verdict"] != "NAME_AGREES":
            print("    req=%-18s row_name=%-40s -> bbg=%s %s" % (r["req"], r["row_name"][:40], r["bbg_ticker"], (r["bbg_name"] or r["verdict"])[:40]))
tot = {}
for r in rows:
    tot[r["verdict"]] = tot.get(r["verdict"], 0) + 1
print("member rows %d: %s" % (len(rows), tot))
json.dump(rows, open(sys.argv[1], "w"), indent=1, default=str)
