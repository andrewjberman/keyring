# IRPT_BCKEND PRD v0.49 and v0.50 -- ratified-text review (C-CHAINCLAIM item 2 split; C-VALUEFACTS)

**Reviewer:** `3.0.0_SA_CVO` (seated on dell2), 2026-10-12. **PRD:** `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` @2472c0cfab
(ADDENDUMS v0.49 and v0.50; ratified-text half hash `d114ddd62ae833f9c0be81f2c0fa97f6c0ed58899f8a6e87d2224216d44e2629`). **Asked by:**
`2.0.0_SA_COO~P2` msg 6495 (round 166 waits on this half). **Prior:** v0.48 SIGNED (half `7a30112fc915...`).
**Verdict: SIGNED. One condition on the C-VALUEFACTS pair; one note.**

IRPT_BCKEND is a long-running project, so the proportionate rule (one sign for a single-round project) does not apply. These two
addenda change contracts, so this is a real re-read, not a formality.

## v0.49 section 1 -- C-CHAINCLAIM item 2 split by the prior day's position

- The test is right. The base is built from the previous trading day's positions (round 161, `holdings_performance.py:856`,
  `:870-872`, read by the issuer). So "did the prior day hold a position row" is the question "was there capital whose valuation
  is missing", and that is what item 3 means by a return left out.
- It agrees with the measure. Round 164: 49F's NON-POSITIVE-BASE days are 1,219 of 1,223 cash debits with no position, and they
  stay `measured`. Orion's are 539,402 of 539,402 with a prior-day position row, and they go `inferred`. The claim-move counts the
  packet must print are round 164's third column: 49F SI 23, YTD 19, QTD 2, 1Y 20; orion SI 894, YTD 200, QTD 7, 1Y 240.
- The partition is complete. The assignment order is NO-PRIOR-HOLDINGS, then ALL-HOLDINGS-EXCLUDED, then NON-POSITIVE-BASE (round 164).
  So an account holding only excluded non-negative positions never reaches item 2, and every NON-POSITIVE-BASE day falls on one
  side of the prior-day test. Item 3's default for an unnamed status stands.
- A short-only account (negative keys only) has a position row, so it reads `inferred`. That is the conservative side, because a
  short does earn a return, and the text says so by its test. Accepted.

## v0.49 section 2 -- rulings

- D2-W322-S2 is ruled by v0.48 item 1, which says the position never decides. Agreed: I close it at this compile.
- D2-S83: 41b9fa7e01 is an ancestor of HEAD (this seat's read). `prd-signoff.py status` now prints "this half's text CHANGED
  since signed", so a contract-changing addendum is visible to the signer. The rule that withholds delivery still binds the
  ENDPOINT hash. That is the proportionate rule, and on a long-running project it rests on the signer reading the change. I read it here.
- D2-W312-S3 is parked on IRPT_YCDGEN with an un-park condition. Accepted. Nothing here may rely on the I3 gate being live.

## v0.50 -- C-VALUEFACTS

- The correction is right. Both schema copies type `value_facts` with no members (IB-pr-471), so v0.49's "the side that
  disagrees renames" decided nothing. Naming the three emitters' spelling moves the fewest bytes.
- **CONDITION (on the pair, not on the text):** today the portal adapter reads `beginning_market_value`/`ending_market_value`
  (row D2-W321-S1). So the bd firm's two value tiles WORK today, and the three conforming emitters' tiles read "not supplied".
  If `bd_adapter.py` renames before the portal reader accepts `start_value`/`end_value`, the bd tiles that work go dark. The pair
  sequences the reader first (or has it read both spellings for the window), and its rollback covers the bd rename alone.
  The portal half lands on DEV freely. A PROD push that changes a client-facing page waits on Andrew's word, so the Lambda half
  does not land before the reader is on PROD.
- **Note:** "No other spelling is a member" while the schema keeps the object open means the schema will not reject a stray
  `beginning_market_value`. That is fine for the window. Once the rename has landed, the schema can name the two retired spellings
  as forbidden, so a regression fails validation instead of rendering "not supplied".

-- 3.0.0_SA_CVO
