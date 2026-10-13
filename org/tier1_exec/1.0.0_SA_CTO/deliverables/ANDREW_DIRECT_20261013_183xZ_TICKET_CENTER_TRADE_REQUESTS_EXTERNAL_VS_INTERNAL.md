# ANDREW DIRECT -- trade requests in the Ticket Center: external vs internal, queued (2026-10-13 ~18:3xZ)

**Channel:** Andrew, at the dell2 terminal, in the session of `1.0.0_SA_CTO~DELL2`, during his localhost:5174 smoke of portal DEV `f6ef1d25`.
He filed a Trade Request (internal-test, PFDE, AAPL BUY 1%). The page showed "Ticket TCK-20261013-5c5c3916 created" and then "The trade
submit failed: Public API request failed: 409 Conflict - {"message": "ticket TCK-20261013-5c5c3916 is not a trade_request ticket"}". The
ticket reads `ticket_type trade_request`, `status open` (this seat's ConsistentRead). Its notification was refused with
`WE_DL_UNCONFIGURED`, so no mail was sent. **Verbatim:**

> I also tried the trade request option, actually running trade requests through here will require a decent amount of backend work because it will be entirely reliant on whether it is an external trade or an internal trade. An external trade would be firm-specific, e.g. a 49 Financial advisor submitting a trade would have to be able to type the name/account similarly to how its done on investor-reporting to find it. That same kind of engine would be needed here. The external advisors would be filing trade requests for clients. THe internal (Opal portfolio managers) trade requests would be filing for trades associated with the Opal ETFs, which would be DIVZ IDVZ PFDE PFOE only. The internal route however is already covered by the direct trade submission tool / dashboard page, so it's not a huge priority to build this out (although it should eventually be queued up as bandwidth thins).

## What it sets

- **External trade requests** come from partner-firm advisors, for their clients. They need the firm-scoped client and account search
  engine Investor Reporting uses (the same directory search, including the last-four lookup live since 17:35Z).
- **Internal trade requests** come from Opal portfolio managers, for the Opal ETFs only: DIVZ, IDVZ, PFDE, PFOE. That route is already
  covered by the direct trade submission tool and dashboard page.
- **Priority:** NOT now. It is queued as bandwidth allows, behind O1 and O2 of the dell2 pivot direction. Its home is NFRA_OPSWKF (the
  Trade Request form's project, parked).
- **Defect recorded, not fixed now:** the form's engine submit refuses its own ticket as "not a trade_request ticket". The ticket reads
  `trade_request`, so the engine reads a different field or route than the ticket writes.

-- recorded by 1.0.0_SA_CTO~DELL2

## Addendum ~18:4xZ, verbatim

> Yes I think all of this can be folded into the OPSWKF project which we will deal with in a couple weeks.

The external and internal trade-request design and the 409 defect fold into NFRA_OPSWKF, which resumes in about two weeks (around
2026-10-27). Nothing is cut before then.
