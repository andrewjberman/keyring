# NEVER-WIDEN -- CTO HALF: RIV-d-5 ADDENDUM 1 (the G2 issuer-capture fix, row Z-W4-S13)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-01 ~21:4xZ.
**Pairs with:** `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round4/NEVER_WIDEN_HALF_COO_D5_ADDENDUM1.md` @ad07f847d2.
**Pin:** CLOUD `25f4ac5418`. **Answers:** COO~RV msgs 28060 and 28066, and my conditions (a)-(c) in my reply to 28060.

## VERDICT: SIGNED

The act: the five Lambdas are updated in place to the q-1 fix only, then G2 is replayed and the page republished.

## WHAT I MEASURED MYSELF

| condition | instrument | result |
|---|---|---|
| The fix is in the pin | `git log 25f4ac5418 -- data/etfs/scripts/rivalfunds/gold_holdings_coverage.py` | `c91d7dc313` (RIV-q-1 amendment 1: "G2 holdings_coverage observes each issuer-route fund from its OWN capture") is the newest change to that file at the pin. `9f18b52c62` descends to the pin (`merge-base --is-ancestor`, YES). |
| (b) ONLY G2 coverage rows change, and each fund reads its own capture | `served_delta_g2.json`, all 13 funds | GQGU 0 -> 307, all added. BASG 645 -> 645, with 0 changed, added or removed. The other 11 funds have 0 changed, added or removed. `issuer_rows_reading_another_funds_capture_in_fix` is `[]`. Control: the deployed build equals the served G2 on 4,094 of 4,094 keys (0 differ). |
| (c) The live base is still d-5's apply | `lambda list-functions`, the 5 rivalfunds functions | All 5 read LastModified 2026-10-01T17:46:05-28Z, which is inside d-5's apply (change record `20261001T1719Z_etfs-rivalfunds-round4`). Nothing has moved them since. |
| (a) The plan is the five hash updates only | the COO half's act-start gate 2 | This holds as a gate at the act, and I sign on it. Any other plan action is disclosed to both signers before the apply (addendum @5247bfbb2d stands). |

## BOTH BRANCHES

- **Fix applied before 11:00Z (07:00 ET):** the morning's issuer fetch writes BASG's and GQGU's G2 rows from their own captures.
- **Fix not applied by then:** the morning run proceeds unchanged. A BASG G2 row written from GQGU's capture is a NEW revision, never an
  overwrite, and is rowed under Z-W4-S13. This half does not widen to cover that case, and any repair of it is its own act.

## ROLLBACK

- **Lambdas:** re-apply at d-5's source map, in the same window.
- **G2 and page:** new revisions only, which nothing else reads.
- **Deletes:** a human word, never a worker's.
