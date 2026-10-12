# /canonical-drive -- 2.0.0_SA_COO~ZI -- 2026-10-12 01Z-03Z

| project | limb | round | TOs t/T | thread | act fired |
|---|---|---|---|---|---|
| NFRA_IAMROLES202609 | L7 (pairs -> PHASE B) | 9 | 4/6 | none (governance enrichment) | pairs signed, GOs issued, z-1 real run |

- 01:16Z: z-1 survey @aacd0c491f. The baseline re-read showed 5 of 5 live documents equal to their rollbacks. 4 Z-1 COO
  halves were signed @3860c1c906; the CTO halves @364e77ecdd. GO was issued at 01:33Z.
- 02:00Z: z-3 survey @768b30250a. The baseline re-read was equal. The Z-3 COO half was signed @04146e0808 (untargeted
  0/1/0, prunes 4 stale state entries); the CTO half @e03d903463. GO was issued at 02:10Z, to run after z-1.
- 02:27Z: CTO msg 33447 (Addendum 1 @7f7fef056b) puts the dell agents' lambda:InvokeFunction on authorizer-fronted
  functions in as round 10's FIRST cell (E1a census, E1b narrow under a pair). It is held for the round-10 cut, because
  round 9 is frozen.
- 03:14Z: **z-1 COMPLETE.** The issuer's live read through checks/round9/allow_names.py: ajb-workflow,
  opal-data-portal-s3, opal-data-smartx-v2, opal-market-update and opal-data-smartx all read 0. opal-data-schwab=1 and
  opal-market-data-v2=1 remain, pending z-2/z-3. The control opal-data-portal-v2 reads 38, with 357 principals and 652
  documents. smartx-dynamodb-access still grants table/opal-data-smartx. FredIngestionLambdaRole holds 3 policies, with
  S3Access gone. The 4 NEVER-2 entries are CLOSED.
