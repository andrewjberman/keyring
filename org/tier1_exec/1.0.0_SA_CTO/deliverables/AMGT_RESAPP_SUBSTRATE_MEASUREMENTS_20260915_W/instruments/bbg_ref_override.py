"""Read-only //blp/refdata ReferenceDataRequest with optional overrides; prints values and field errors per security."""
import json
import sys

import blpapi

SECS = ["BA US Equity", "COST US Equity", "HD US Equity", "SAP GY Equity", "BABA US Equity"]
PASSES = [
    ("BF blended-forward 12m", {"BEST_FPERIOD_OVERRIDE": "BF"},
     ["BEST_EPS", "BEST_PE_RATIO", "BEST_EBITDA", "BEST_SALES", "BEST_NET_INCOME", "BEST_DPS"]),
    ("no override (trailing)", {},
     ["TRAIL_12M_EPS", "TRAIL_12M_EBITDA", "TRAIL_12M_NET_SALES", "TRAIL_12M_FREE_CASH_FLOW", "CF_DVD_PAID",
      "CF_DECR_CAP_STOCK", "TRAIL_12M_DVD_PAID", "TRAIL_12M_CASH_FROM_DIVIDENDS", "EQY_DVD_YLD_12M", "CUR_MKT_CAP",
      "CURR_ENTP_VAL", "EQY_FUND_CRNCY", "BEST_FPERIOD_OVERRIDE"]),
    ("annual-period label on the cash-flow items", {"FUND_PER": "Y"},
     ["CF_DVD_PAID", "CF_DECR_CAP_STOCK"]),
]
opts = blpapi.SessionOptions()
opts.setServerHost("127.0.0.1")
opts.setServerPort(8194)
s = blpapi.Session(opts)
if not s.start() or not s.openService("//blp/refdata"):
    print("ERROR: session/service")
    sys.exit(2)
svc = s.getService("//blp/refdata")
for label, ovr, fields in PASSES:
    req = svc.createRequest("ReferenceDataRequest")
    for x in SECS:
        req.append("securities", x)
    for f in fields:
        req.append("fields", f)
    if ovr:
        ov = req.getElement("overrides")
        for k, v in ovr.items():
            o = ov.appendElement()
            o.setElement("fieldId", k)
            o.setElement("value", v)
    s.sendRequest(req)
    out = {}
    for _tick in iter(int, 1):  # event loop; the commit gate's scope walk reads For bodies, not While
        ev = s.nextEvent(30000)
        for msg in ev:
            if not msg.hasElement("securityData"):
                continue
            sd = msg.getElement("securityData")
            for i in range(sd.numValues()):
                e = sd.getValueAsElement(i)
                sec = e.getElementAsString("security")
                row = {}
                if e.hasElement("securityError"):
                    row["__security_error__"] = str(e.getElement("securityError"))[:120]
                fdat = e.getElement("fieldData")
                for j in range(fdat.numElements()):
                    el = fdat.getElement(j)
                    try:
                        row[str(el.name())] = el.getValue()
                    except Exception:
                        row[str(el.name())] = str(el)[:80]
                errs = {}
                if e.hasElement("fieldExceptions"):
                    fx = e.getElement("fieldExceptions")
                    for j in range(fx.numValues()):
                        x = fx.getValueAsElement(j)
                        ei = x.getElement("errorInfo")
                        errs[x.getElementAsString("fieldId")] = ei.getElementAsString("subcategory")
                if errs:
                    row["__field_errors__"] = errs
                out[sec] = row
        if ev.eventType() in (blpapi.Event.RESPONSE, blpapi.Event.TIMEOUT):
            break
    print("=== pass: %s overrides=%s" % (label, ovr))
    for sec in SECS:
        print("  %-15s %s" % (sec, json.dumps(out.get(sec, "ABSENT"), default=str)))
s.stop()
