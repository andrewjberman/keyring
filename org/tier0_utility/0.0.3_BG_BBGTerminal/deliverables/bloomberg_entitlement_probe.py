"""Decisive Terminal-entitlement probe.

Three layers, deliberately not one (per BLOOMBERG_TERMINAL_SIGNIN_RECOVERY.md):
  1. blpapi Session opens against //blp/refdata  -- transport
  2. a GENERIC ticker returns data              -- entitlement, positive control
  3. the .ST CUSTOM index resolves correctly    -- LOGIN-SCOPED resolution, the sharp test

Layer 3 is the one that carries information: CIX resolution is terminal/login-scoped,
so a correct .ST series is the only evidence that an entitled Terminal session backs
this bbcomm. Expected: inception 2023-12-29 @ 100.0000, latest ~112-113.
A 1449-row / ~1.9-price series is the KNOWN mis-resolution, not a pass.
"""
from __future__ import annotations

import blpapi

EXPECTED_INCEPTION = "20231229"


def fetch(session, ticker, start, end):
    """Return list of (date, px) or raise. Empty list means the ticker did not resolve."""
    svc = session.getService("//blp/refdata")
    req = svc.createRequest("HistoricalDataRequest")
    req.getElement("securities").appendValue(ticker)
    req.getElement("fields").appendValue("PX_LAST")
    req.set("startDate", start)
    req.set("endDate", end)
    req.set("periodicitySelection", "DAILY")
    session.sendRequest(req)

    rows, errors = [], []
    while True:
        ev = session.nextEvent(30000)
        for msg in ev:
            sd = msg.getElement("securityData") if msg.hasElement("securityData") else None
            if sd is None:
                continue
            if sd.hasElement("securityError"):
                errors.append(str(sd.getElement("securityError")))
                continue
            fd = sd.getElement("fieldData")
            for i in range(fd.numValues()):
                pt = fd.getValue(i)
                if pt.hasElement("PX_LAST"):
                    rows.append((pt.getElementAsString("date"), pt.getElementAsFloat("PX_LAST")))
        if ev.eventType() == blpapi.Event.RESPONSE:
            break
    if errors:
        raise RuntimeError("; ".join(errors))
    return rows


def main():
    opts = blpapi.SessionOptions()
    opts.setServerHost("127.0.0.1")
    opts.setServerPort(8194)
    session = blpapi.Session(opts)

    if not session.start():
        print("LAYER 1 FAIL: blpapi Session would not start")
        return 1
    if not session.openService("//blp/refdata"):
        print("LAYER 1 FAIL: could not open //blp/refdata")
        return 1
    print("LAYER 1 OK:   blpapi Session + //blp/refdata open")

    # Layer 2 -- positive control on a generic, always-entitled ticker. Run FIRST and
    # SEPARATELY so a layer-3 failure cannot be blamed on a dead transport.
    try:
        spx = fetch(session, "SPX Index", "20260804", "20260811")
        print(f"LAYER 2 OK:   SPX Index returned {len(spx)} rows, latest {spx[-1]}")
    except Exception as exc:  # noqa: BLE001
        print(f"LAYER 2 FAIL: generic ticker did not resolve -- {exc}")
        return 1

    # Layer 3 -- the login-scoped custom index. This is the test that discriminates
    # "entitled Terminal session" from "bbcomm is merely up".
    try:
        st = fetch(session, ".ST Index", EXPECTED_INCEPTION, "20260811")
    except Exception as exc:  # noqa: BLE001
        print(f"LAYER 3 FAIL: .ST Index raised -- {exc}")
        return 2

    if not st:
        print("LAYER 3 FAIL: .ST Index returned ZERO rows -- CIX did not resolve")
        return 2

    first_d, first_px = st[0]
    last_d, last_px = st[-1]
    print(f"LAYER 3:      .ST Index rows={len(st)} inception={first_d}@{first_px:.4f} latest={last_d}@{last_px:.4f}")

    ok = first_d.replace("-", "") == EXPECTED_INCEPTION and abs(first_px - 100.0) < 0.01
    if ok:
        print("LAYER 3 OK:   CIX resolved CORRECTLY -- an entitled Terminal session backs this bbcomm")
        return 0
    print("LAYER 3 FAIL: CIX MIS-RESOLVED (wrong inception/price) -- do NOT trust a pull from this session")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
