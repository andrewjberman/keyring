# ANDREW-DIRECT 2026-09-30 ~22:5xZ -- NFRA_MCPMSP: the MSP calling identity, "Not yet"

**Where:** the site-Z `1.0.0_SA_CTO~O` terminal, answering this seat's question on `2.0.0_SA_COO~MS` msg 27412 (round 2
needs one Microsoft 365 identity for the `Opal_MSP` session to sign in to the gateway as, before G-USER exists).

**His words, VERBATIM:**
1. To the first question (options: create G-USER now / name an existing account / not yet), he answered with a question:
   > "why can this not be opalbloomberg?"
2. This seat answered with three reasons:
   - `opalbloomberg@` is the internal Analyst's (Opal_Agent's) gateway identity, so the gateway could not tell the two
     harnesses apart, and the pilot refusal of Opal-staff senders would also refuse them on the internal Analyst.
   - PRD contract C8 says "Partner traffic never runs as the internal Analyst's identity". C8 is in the CVO-signed half.
   - Since this afternoon's OPLGTW Part D, `opalbloomberg@` is one of the two write-capable principals.
3. To the same question re-asked, he selected **"Not yet"**. That option's text read: "E2's live arm and E4 are cut
   gated on this. Everything else in round 2 proceeds."

## What it covers (no wider, no narrower)

- `MSP_CALLING_IDENTITIES` (the mechanism, ruled by this seat in its reply to `2.0.0_SA_COO~MS` msg 27412) ships
  EMPTY in round 2.
- E2's live arm and E4's replayable run are cut with a named gate, **G-MSPID**: Andrew creates G-USER, or names an
  existing non-person account. Holder: Andrew.
- Everything else in round 2 proceeds: E1's census, internal role and query_v0 route; E2's code and tests; E3; E5; E6.
- `opalbloomberg@` is NOT an MSP calling identity. No MSP cell may use it.
