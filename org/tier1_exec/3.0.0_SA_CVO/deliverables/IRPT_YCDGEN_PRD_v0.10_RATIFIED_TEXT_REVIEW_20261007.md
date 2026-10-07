# IRPT_YCDGEN PRD v0.10 -- ratified-text half review (L4-R)

**archetype:** VALIDATE

Reviewer: `3.0.0_SA_CVO` (seated on dell2), 2026-10-07 ~13:4xZ. Subject: `org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md` v0.10
@5a04dc8c4a (`1.0.0_SA_CTO~DELL2`), read as the diff against v0.9 @8499df49ce, which this seat signed @954ef14c6b. Asked by msgs 619/620.

**Verdict: SIGN.** One wording finding (P3), and v0.9's P2 is still open.

## What changed

FWD-18's ACCEPT is amended in place. "One action accepts every suggestion" becomes "one action accepts every corrected-ticker suggestion
... a stand-in for a different security is always accepted one at a time". Nothing else in ENDPOINT or CONTRACTS moved. The provenance
gains the v0.10 line.

## Checks

1. **The amendment is coherent with the rest of the ENDPOINT.** FWD-20 already separates "ticker corrected" from "stand-in". FWD-18 now
   bulk-accepts only the first. "Nothing is accepted unless the advisor chose it" is kept.
2. **The source reads true at its bytes.** Brief @f9386e5865, section 4.3b (:162, "added 2026-10-07 ~13:4xZ, on Andrew's word"), row E7
   (:178, the Spread.ai piece against accept-all), and :183: "Stand-ins (R5, R10) are never bulk-accepted: a stand-in changes what the
   report measures". The brief's own scope line (:245) says the external pass read result summaries only.
3. **Not added, and so stated:** R13 (a per-firm remembered correction) is left for Andrew. That is a product call, not an omission.

## Findings

- **P3 (wording): the traceability row S34 still reads "one-action accept and accept-all on the review card"** (PRD :389). It should say
  accept-all covers corrected tickers only, or a page cell built from S34 alone would rebuild the v0.9 behaviour.
- **v0.9's P2 is still open:** brief R7 and R8 have no carrier although section 8 says R1-R12 are carried (review @bcac50ac02).

-- 3.0.0_SA_CVO
