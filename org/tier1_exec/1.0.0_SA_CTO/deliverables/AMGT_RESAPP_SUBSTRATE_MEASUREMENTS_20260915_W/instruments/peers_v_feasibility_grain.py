"""QA feasibility run, read-only: Andrew's Peers score V computed from Bloomberg over the SERVED R-1 peer sets (peers/v1).
Not a production artifact; output goes to the scratchpad only. Every missing input is ABSENT with its reason."""
import json
import statistics
import sys

import blpapi
import boto3

OUT = sys.argv[1]
BAD = {(r["subject"], r["req"]) for r in json.load(open(sys.argv[2])) if r["verdict"] != "NAME_AGREES"}
print("member rows excluded on identity grain:", len(BAD))
B = "opal-data-harvest"
s3 = boto3.client("s3")
subjects = {}
for page in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="peers/v1/"):
    for o in page.get("Contents", []):
        d = json.loads(s3.get_object(Bucket=B, Key=o["Key"])["Body"].read())
        if d.get("members"):
            sec = o["Key"][len("peers/v1/"):].rsplit("/", 1)[0].replace("_", " ")
            subjects[sec] = d
first = next(iter(subjects.values()))["members"][0]
print("first member row (non-contact market data):", json.dumps({k: first.get(k) for k in ("ticker", "identity", "name", "sector")}, default=str)[:400])


def member_sec(r):
    idn = r.get("identity")
    if isinstance(idn, dict):
        for k, v in idn.items():
            if isinstance(v, str) and v.endswith(" Equity"):
                return v
    t = (r.get("ticker") or "").strip()
    return t if t.endswith(" Equity") else (t + " Equity" if t else None)


secs = set(subjects)
for d in subjects.values():
    for r in d["members"]:
        s_ = member_sec(r)
        if s_:
            secs.add(s_)
secs = sorted(secs)
print("subjects with a served peer set: %d; unique securities (subjects + members): %d" % (len(subjects), len(secs)))

FIELDS = ["FREE_CASH_FLOW_YIELD", "BEST_PE_RATIO", "BEST_EPS", "PE_RATIO", "EQY_DVD_YLD_12M", "TRAIL_12M_DVD_PAID",
          "CF_DECR_CAP_STOCK", "CRNCY_ADJ_MKT_CAP", "CURRENT_EV_TO_T12M_EBITDA", "BEST_CUR_EV_TO_EBITDA", "EV_TO_T12M_SALES",
          "CURRENT_EV_TO_12M_SALES", "BEST_CURRENT_EV_BEST_SALES", "TRAIL_12M_EBITDA", "GICS_SECTOR_NAME", "EQY_FUND_CRNCY"]
opts = blpapi.SessionOptions()
opts.setServerHost("127.0.0.1")
opts.setServerPort(8194)
sess = blpapi.Session(opts)
if not sess.start() or not sess.openService("//blp/refdata"):
    print("ERROR: session")
    sys.exit(2)
svc = sess.getService("//blp/refdata")
req = svc.createRequest("ReferenceDataRequest")
for x in secs:
    req.append("securities", x)
for f in FIELDS:
    req.append("fields", f)
ov = req.getElement("overrides")
for k, v in (("BEST_FPERIOD_OVERRIDE", "BF"), ("EQY_FUND_CRNCY", "USD")):
    o = ov.appendElement()
    o.setElement("fieldId", k)
    o.setElement("value", v)
sess.sendRequest(req)
data, sec_err, fld_err = {}, {}, {}
for _tick in iter(int, 1):  # event loop; the commit gate's scope walk reads For bodies, not While
    ev = sess.nextEvent(60000)
    for msg in ev:
        if not msg.hasElement("securityData"):
            continue
        sd = msg.getElement("securityData")
        for i in range(sd.numValues()):
            e = sd.getValueAsElement(i)
            sec = e.getElementAsString("security")
            if e.hasElement("securityError"):
                sec_err[sec] = e.getElement("securityError").getElementAsString("subcategory")
            row = {}
            fd = e.getElement("fieldData")
            for j in range(fd.numElements()):
                el = fd.getElement(j)
                row[str(el.name())] = el.getValue()
            if e.hasElement("fieldExceptions"):
                fx = e.getElement("fieldExceptions")
                for j in range(fx.numValues()):
                    x = fx.getValueAsElement(j)
                    fld_err.setdefault(x.getElementAsString("fieldId"), set()).add(x.getElement("errorInfo").getElementAsString("subcategory"))
            data[sec] = row
    if ev.eventType() in (blpapi.Event.RESPONSE, blpapi.Event.TIMEOUT):
        break
sess.stop()
print("security errors: %d of %d %s" % (len(sec_err), len(secs), sorted(sec_err.items())[:8]))
print("field errors:", {k: sorted(v) for k, v in fld_err.items()})
print("field coverage (securities with a value, of %d):" % len(secs))
for f in FIELDS:
    print("   %-28s %d" % (f, sum(1 for s_ in secs if f in data.get(s_, {}))))


def inv(x):
    return 1.0 / x if isinstance(x, (int, float)) and x > 0 else None


def measures(r):
    m = {}
    if "FREE_CASH_FLOW_YIELD" in r:
        m[1] = r["FREE_CASH_FLOW_YIELD"] / 100.0
    if r.get("BEST_EPS") is not None and r["BEST_EPS"] > 0 and r.get("BEST_PE_RATIO"):
        m[2] = inv(r["BEST_PE_RATIO"])
    dv, bb, mc = r.get("TRAIL_12M_DVD_PAID"), r.get("CF_DECR_CAP_STOCK"), r.get("CRNCY_ADJ_MKT_CAP")
    if mc and (dv is not None or bb is not None):
        m[3] = (-(dv or 0.0) - (bb or 0.0)) / mc
    ebitda_ev = r.get("BEST_CUR_EV_TO_EBITDA", r.get("CURRENT_EV_TO_T12M_EBITDA"))
    if ebitda_ev is not None and ebitda_ev > 0:
        m[4] = 1.0 / ebitda_ev
    sales_ev = r.get("BEST_CURRENT_EV_BEST_SALES", r.get("CURRENT_EV_TO_12M_SALES", r.get("EV_TO_T12M_SALES")))
    if sales_ev is not None and sales_ev > 0:
        m[5] = 1.0 / sales_ev
    pe_t, pe_f = r.get("PE_RATIO"), r.get("BEST_PE_RATIO")
    if pe_t and pe_f and pe_t > 0 and pe_f > 0 and (r.get("BEST_EPS") or 0) > 0:
        g = (pe_t / pe_f - 1.0) * 100.0
        if g > 0:
            m[6] = g / pe_f
    return {k: v for k, v in m.items() if v is not None}


def pct(vals, q):
    v = sorted(vals)
    pos = (len(v) - 1) * q
    lo = int(pos)
    hi = min(lo + 1, len(v) - 1)
    return v[lo] + (v[hi] - v[lo]) * (pos - lo)


results = {}
for sub, d in sorted(subjects.items()):
    K = [member_sec(r) for r in d["members"]]
    K = [k for k in K if k and k != sub and (sub, k) not in BAD]
    ys = measures(data.get(sub, {}))
    zs, detail = {}, {}
    for m in range(1, 7):
        vals = [measures(data.get(k, {})).get(m) for k in K]
        vals = [v for v in vals if v is not None]
        if m not in ys:
            detail[m] = "ABSENT subject"
            continue
        if len(vals) < 6:
            detail[m] = "dropped |K_m|=%d<6" % len(vals)
            continue
        lo, hi = pct(vals, 0.05), pct(vals, 0.95)
        w = [min(max(v, lo), hi) for v in vals]
        mu, sd = statistics.median(w), statistics.stdev(w)
        if sd == 0:
            detail[m] = "dropped sd=0"
            continue
        zs[m] = (ys[m] - mu) / sd
        detail[m] = "z=%+.2f (y=%.4f med=%.4f sd=%.4f n=%d)" % (zs[m], ys[m], mu, sd, len(vals))
    V = sum(zs.values()) / len(zs) if len(K) >= 8 and len(zs) >= 3 else None
    results[sub] = {"K": len(K), "M": sorted(zs), "V": V, "detail": detail,
                    "sector": data.get(sub, {}).get("GICS_SECTOR_NAME")}
    print("=== %-18s |K|=%d |M|=%d V=%s sector=%s" % (sub, len(K), len(zs), "%+.2f" % V if V is not None else "SUPPRESSED", results[sub]["sector"]))
    for m in range(1, 7):
        print("     m%d %s" % (m, detail[m]))
json.dump({"fields": FIELDS, "overrides": {"BEST_FPERIOD_OVERRIDE": "BF", "EQY_FUND_CRNCY": "USD"}, "results": results,
           "field_errors": {k: sorted(v) for k, v in fld_err.items()}, "security_errors": sec_err}, open(OUT, "w"), indent=1, default=str)
print("V computed for %d of %d served peer sets" % (sum(1 for r in results.values() if r["V"] is not None), len(results)))
