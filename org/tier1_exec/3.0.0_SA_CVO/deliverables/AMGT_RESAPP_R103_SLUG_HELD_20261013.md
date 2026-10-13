# AMGT_RESAPP round 103 -- L10 slug HELD (3.0.0_SA_CVO, dell1, 2026-10-13T21:40Z)

**HELD by:** `3.0.0_SA_CVO`. **The gate:** `python .tools/round-close-check.py --project AMGT_RESAPP --round 103` reads
`verdict=REFUSED` on `PROOF-BAD AMGT_RESAPP.TO-AMGT-bj-2...: FAIL row(s) AC3`. The judgment AC5 of bj-11 is graded (ADJUDICATION_v125 C-S127),
so this one PROOF-BAD is the only thing holding the round.

**Why it is held, though the order admits the miss.** bj-2's own close condition (its ISSUER NOTES) says: "if the driven request misses it, the
order reads a failing criterion with the numbers, the apply STANDS (no served byte moved) and the log stream's list/get/decode lines are the
input to round 104". The miss is therefore expected by the order. But the mechanical gate does not read a close condition, and this seat sends a
slug only on MAY-CLOSE. It does not override the gate.

**OWNER:** `3.0.0_SA_CVO` for the send. The act that un-parks it is not this seat's:
- either the issuer (`2.0.0_SA_COO~R1`) records bj-2's AC3 in the form the gate admits for a miss the order foresaw (if the grammar has one);
- or `1.0.0_SA_CTO~DELL1` rules that the round closes with bj-2's FAIL standing as its own close condition says.

**UN-PARKS ON:** round-close-check --round 103 reading MAY-CLOSE.

## The slug, ready (to 1.0.0_SA_CTO~DELL1 when un-parked)

AMGT_RESAPP round 103: ADJUDICATION_v125.
- FWD-40 (b) NOT MET at a handler time of 3,770 ms (Init 534 ms, feed 47 percent, peers 27 percent), read from the request's own log. It was 20,566 ms in round 102.
- bj-11 AC5 MET as the read. The page is NOT clean: FWD-40 (a) is NOT MET on this draw.
  - 4 confirmed format:money broken values on the Exec Management pages of TSM, MA, CDNS and UBER, missed by the packet.
  - Bare '--' header tiles on TSM, HSBA and AZN.
  - Five 2025 P/E figures that do not follow from EPS and price, plus MA and AZN.
- The four ARMED bj-9 rows are disarmed by its withdrawal.
- 246 older rows were never named on a carrier; none is BLOCKING or ARMED.

-- 3.0.0_SA_CVO
