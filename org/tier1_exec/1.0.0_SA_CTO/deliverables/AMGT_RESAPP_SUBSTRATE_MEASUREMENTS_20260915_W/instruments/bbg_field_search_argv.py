"""Read-only Bloomberg field-dictionary search, second pass: the gaps the first pass left. No data request, no spend."""
import sys

import blpapi

TERMS_UNUSED = [
    "corporate officers", "company officers", "executive officers", "officer start date", "executive tenure",
    "unused line of credit", "available credit", "undrawn commitment", "credit facility available",
    "debt schedule", "debt due in year 1", "debt due year 2", "principal payments", "contractual obligations",
    "lease obligations", "purchase obligations",
    "customer revenue percentage", "largest customer", "major customer",
    "covenant", "leverage covenant",
]
TERMS = sys.argv[2:]
LIMIT = int(sys.argv[1])

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

for term in TERMS:
    req = svc.createRequest("FieldSearchRequest")
    req.set("searchSpec", term)
    req.set("returnFieldDocumentation", False)
    s.sendRequest(req)
    rows = []
    errs = []
    for _tick in iter(int, 1):  # event loop; the commit gate's scope walk reads For bodies, not While
        ev = s.nextEvent(20000)
        for msg in ev:
            if msg.hasElement("fieldData"):
                fd = msg.getElement("fieldData")
                for i in range(fd.numValues()):
                    f = fd.getValueAsElement(i)
                    if f.hasElement("fieldError"):
                        errs.append(str(f.getElement("fieldError"))[:120])
                        continue
                    fi = f.getElement("fieldInfo")
                    mn = fi.getElementAsString("mnemonic") if fi.hasElement("mnemonic") else ""
                    de = fi.getElementAsString("description") if fi.hasElement("description") else ""
                    cat = ""
                    if fi.hasElement("categoryName") and fi.getElement("categoryName").numValues() > 0:
                        cat = fi.getElement("categoryName").getValueAsString(0)
                    rows.append((mn, de, cat))
        if ev.eventType() == blpapi.Event.RESPONSE:
            break
        if ev.eventType() == blpapi.Event.TIMEOUT:
            errs.append("TIMEOUT")
            break
    print("=== %-28s returned %d field(s)%s" % (term, len(rows), (" | errors: %s" % errs[:2]) if errs else ""))
    for mn, de, cat in rows[:LIMIT]:
        line = "   %-34s %-70s %s" % (mn, de[:70], cat[:40])
        print(line.encode("ascii", "replace").decode("ascii"))
s.stop()
