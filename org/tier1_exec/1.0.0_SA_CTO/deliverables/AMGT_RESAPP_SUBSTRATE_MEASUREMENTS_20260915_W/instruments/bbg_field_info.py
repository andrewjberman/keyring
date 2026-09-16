"""Read-only Bloomberg FieldInfoRequest with documentation for named mnemonics. No data request, no spend."""
import sys

import blpapi


def _s(fi, k):
    return fi.getElementAsString(k) if fi.hasElement(k) else ""


FIELDS = sys.argv[1:] or [
    "EXECUTIVE_AVERAGE_TENURE", "TOTAL_TENURE_OF_CEO_COMPANY", "CHIEF_EXECUTIVE_OFFICER_TENURE",
    "BOARD_AVERAGE_TENURE", "CFO_TENURE_AS_OF_FY_END", "BS_TOTAL_LINE_OF_CREDIT", "BS_TOTL_DEBT_DEBT_SCHEDULE",
    "INTEREST_COVERAGE_RATIO", "NET_DEBT_TO_EBITDA", "TRAIL_12M_FREE_CASH_FLOW",
]

opts = blpapi.SessionOptions()
opts.setServerHost("127.0.0.1")
opts.setServerPort(8194)
s = blpapi.Session(opts)
if not s.start():
    print("ERROR: could not start session")
    sys.exit(2)
if not s.openService("//blp/apiflds"):
    print("ERROR: could not open //blp/apiflds")
    sys.exit(3)
svc = s.getService("//blp/apiflds")
req = svc.createRequest("FieldInfoRequest")
for f in FIELDS:
    req.append("id", f)
req.set("returnFieldDocumentation", True)
s.sendRequest(req)
seen = 0
for _tick in iter(int, 1):  # event loop; the commit gate's scope walk reads For bodies, not While
    ev = s.nextEvent(20000)
    for msg in ev:
        if not msg.hasElement("fieldData"):
            continue
        fd = msg.getElement("fieldData")
        for i in range(fd.numValues()):
            f = fd.getValueAsElement(i)
            seen += 1
            fid = f.getElementAsString("id") if f.hasElement("id") else "?"
            if f.hasElement("fieldError"):
                print("=== %s ERROR %s" % (fid, str(f.getElement("fieldError")).replace("\n", " ")[:200]))
                continue
            fi = f.getElement("fieldInfo")
            doc = _s(fi, "documentation").replace("\r", " ").replace("\n", " ")
            line = "=== %s | %s | ftype=%s datatype=%s\n    %s" % (_s(fi, "mnemonic"), _s(fi, "description"), _s(fi, "ftype"), _s(fi, "datatype"), doc[:900])
            print(line.encode("ascii", "replace").decode("ascii"))
    if ev.eventType() in (blpapi.Event.RESPONSE, blpapi.Event.TIMEOUT):
        break
print("fields requested %d, entries returned %d" % (len(FIELDS), seen))
s.stop()
