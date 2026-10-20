# L4-R review -- NFRA_SCHWABBF PRD v0.7 @ad57e2f73a, ratified-text half

**archetype:** VALIDATE
**Reviewer:** 3.0.0_SA_CVO (laptop), 2026-10-20 ~16:4xZ. Delivered by 1.0.0_SA_CTO msgs 109928 and 109929 (both acked). Half hash `1ec6f36e9425`.
**Graded:** the diff 0fd3b119fd -> ad57e2f73a. ENDPOINT: FWD-2, FWD-4 and FWD-6 narrow; the rest are unchanged. CONTRACTS: C-SCOPE, C-KEYFORM,
C-MOVE, C-BACKFILL and C-RECORD narrow to the in-scope masters; decision 6, OPEN AT ANDREW and the surface manifest follow.

## Verdict: SIGN

## The ENDPOINT change against Andrew's word

- **The word** (`ANDREW_DIRECT_20261020_163xZ_SCHWABBF_0824_OUT_FOCUS_COTTONWOOD_AND_0840.md`): "I dont care about that 0824, I want the new
  Cottonwood accounts taken care of and the 0840 tax sma account sorted out."
- **What changed:**
  - FWD-2 goes from "each of the three entitled account groups" to "the 0840 Tax SMA account group";
  - FWD-4 goes from any Schwab file to "an 0840 or Cottonwood" file;
  - FWD-6 goes from each new business day to "each new 0840 business day".
  Each removes masters from a confirmed outcome and adds nothing. FWD-1, FWD-3, FWD-5, FWD-7 and FWD-8 are unchanged.
- **0824 out:** his words exactly.
- **0833 out:** NOT his words. He named 0824 out and named Cottonwood and 0840 as the work; the CTO reads 0833 as held out with 0824
  and puts it to him under OPEN AT ANDREW. The narrowing promises less, writes nothing to 0833 (its daily pull and keys are unchanged,
  per C-SCOPE), and can be widened back. So it is signable on the record's own terms, as an inference pending his line (carried item 1).

## CONTRACTS agree with the narrowed ENDPOINT

- C-SCOPE holds five masters: 0840 on the 49F box, and the four Cottonwood masters on the Alongside box.
- C-KEYFORM applies the firm form per master and returns today's key for any other, so one master is never stored in two forms. The v0.6
  legacy-member rule is withdrawn, and with it this seat's v0.6 carried items (they concerned 0824 only).
- C-MOVE moves 0840 only; 0840's count is re-measured at the cut (this seat listed 6,074 objects under `schwab/08403355/bronze/` at ~16:3xZ).
- C-BACKFILL covers 0840 and the Cottonwood four; C-RECORD covers in-scope masters.

## Carried, not grounds

1. **0833: CLEARED before the stamp.** At e8d796975f (same v0.7; ENDPOINT and CONTRACTS byte-identical to ad57e2f73a) the CTO records
   Andrew's ~16:4xZ "1.) Yes that is correct": 0833 is out with 0824. The narrowing of FWD-2, FWD-4 and FWD-6 is now his word in full.
   The stamp binds e8d796975f.
2. **The silver/meta/`_ops` call (row 6814) now covers 0840 only,** as the PRD says. Its answer still re-opens this half.

-- 3.0.0_SA_CVO
