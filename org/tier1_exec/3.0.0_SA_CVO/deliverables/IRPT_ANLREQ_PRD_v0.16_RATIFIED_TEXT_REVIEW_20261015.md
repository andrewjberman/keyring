# IRPT_ANLREQ PRD v0.16 -- L4-R review, ratified-text half (no price-date input)

**Reviewer:** `3.0.0_SA_CVO~DELL2`, 2026-10-15 ~20:5xZ. **Delivery:** msg 8648 (ENDPOINT unchanged; CONTRACTS changed). **PRD:**
`org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` @a4af0e5bba. **Compared against:** v0.15 @1671e13361, which this seat signed.
**Authority read:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261015_204xZ_NO_PRICE_DATE_SELECTION_LATEST_CLOSE.md`
(@89c40cc943, confirmation @9f80e0deea):
- line 8: "there is no point in giving them date selection for prices. The prices should always be whatever the most recent data is";
- line 30, confirming the CRO's reading that "T+1" means the latest close, which is the T-1 frontier: "You are correct".

**Verdict: SIGN.** Only the C-PRICES row moved in this half. It gains one sentence:
- there is no price-date input;
- every price, share-quantity valuations included, is the T-1 frontier close of `lib/trading_calendar.py`;
- that close is stated in the report as the as-of.

This carries his word. It agrees with the rest of C-PRICES ("Yahoo, cut at T-1") and with FWD-7. Nothing else in the ENDPOINT or
CONTRACTS changed.

**Provenance point (for the addendum, not the half).** ADDENDUM v0.16, and the CTO's msg 8648, quote Andrew verbatim: "T-1 is the correct
terminology, let's just stick to that". No record in `org/tier1_exec/*/deliverables/` carries that sentence; the CRO's record carries "You are
correct". The substance (T-1) is confirmed by the record, so the half stands. Either the sentence is recorded (Andrew-direct, recorded the
same turn), or the addendum quotes "You are correct".

-- 3.0.0_SA_CVO~DELL2
