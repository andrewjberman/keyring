# SIGN-OFF (1.0.0_SA_CTO half) -- bd-securities write, batch A, with the three preferreds struck

**Request:** `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_BD_SECURITIES_WRITE_20260925.md`
@`368950498a` (2.0.0_SA_COO~M). **Order:** Andrew-direct ~14:4xZ ("Yes, one run"; held-away = Other; investment real
estate = alternatives), record `ANDREW_DIRECT_20260925_144xZ_CLASSIFIER_OTHER_OPENAI_RUN_AND_DEV_PUSH.md` @`705be61575`.
**Signed:** 1.0.0_SA_CTO, 2026-09-25 ~15:3xZ.

## Signed: batch A minus three keys = 204 keys

**Struck:** the three preferred-stock keys whose class would FLIP from today's `fixed_income`:
- `GLADSTONE CAP 6.25% PFD PFD SER A`
- `MORGAN STANLE 4.25% PFD PFD SER O`
- `VORNADO REALTY 5.4% PFD PFD SER L`

A preferred is an income instrument whose served class today is `fixed_income`. Andrew's real-estate rule names REITs
(the investment), not a REIT's preferred paper. So a contested reclassification of a served value does not ride this
act. It moves only on Andrew's word.

**The one flip that remains:** `Ft Unit 9273 Int Rate Hedge Port Ser 135`, `fixed_income` -> `alternatives`. It is a
hedge portfolio, which is the class Andrew's rule and the classifier's own taxonomy give it.

**The act:**
- A conditional `PutItem` per key, `attribute_not_exists(ticker)`, carrying `classified_run = irpt-m-once-20260925`.
- The keys are the literal list, minus the three above.
- The census re-runs against a fresh scan first, and the act refuses on a key-list sha mismatch. The sha is recomputed
  over the 204-key list and stated in the receipt.

## Blast radius (read from the producer's rules in the request)

- **The table:** DynamoDB `bd-securities`, 204 net-new `NAME::` keys. No overwrite and no delete.
- **What moves:**
  - COT `C_06` client mix at its next scheduled run: about $21.18M from equity to alternatives and about $0.41M from
    equity to fixed_income, for the clients holding those securities. This is a correction of today's NONE -> equity
    fallback.
  - Holdings classes up to 204 securities from NONE at its next publication.
- **What does not move:**
  - the 41 existing items;
  - `etf-classifications` and the whole Positioning family;
  - INF composition;
  - Schwab composition.
- **One writer of the property:** the loader's `classify()`, in two byte-identical copies.

**Rollback, per key:** `DeleteItem` with the condition `classified_run = irpt-m-once-20260925`, over the same list.
No key existed before, so the prior state restores exactly. The delete takes a human confirmation per the autonomy
rules.

## Batch B (the 37 `other` keys): NOT signed

Held exactly as the request orders it. The prerequisites land first:
1. C_06 admits `other`.
2. D_03 and D_04 separate their unknown sentinel.
3. The Holdings enum and the v1 contract admit `other`.
4. ~D maps `other`.

Then batch B returns as its own half.
