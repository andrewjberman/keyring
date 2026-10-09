# Deploy Completion Record
**Date opened:** 2026-10-09T13:17:36.979388+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T132039Z
**Deploy:** AMGT_RESAPP round 85 AMGT-jj-2 (narrowed, CTO ADDENDUM 2): repair s3://opal-data-harvest/drafting/v1/NU_US_Equity.json in place -- filing's verbatim sentence kept, paraphrase dropped; no fetch, no model call, no other key; dell1
**Authored by:** 0.9.0_WK_AMGT_RESAPP~339
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | drafting/v1/NU_US_Equity.json repaired in place (prior VersionId xe0hxE3lFtEuonqh_ij9dIqQnWUC7Qrt, 2026-10-09 09:51:55Z, 38 sentences, 112123 bytes); ROLLBACK = re-put the prior VersionId's bytes (never a delete) | AC1 YES before the write; new VersionId; drafting-prefix listing before/after (only this key changes); AC2 and AC3 YES on the live function, else rollback | NU drafting repaired in place, 38 sentences kept, 0 dropped, no fetch, no model call. AC1 YES before the write (K1 38 of 38, K2 0 restated 0 glued, K3 38 of 38 verbatim, K4 38 of 38 evidence intact). Prior VersionId xe0hxE3lFtEuonqh_ij9dIqQnWUC7Qrt (112123 bytes, untouched, rollback = re-put its bytes). New: first put bl_O3NCt4.nTV9MlX.vMAlEKfeICF9XR carried a stale document-sha256 (row AMGT_RESAPP-D1-W339-S1); corrected by a re-put of the same 107028 bytes = I.NWiDvQCJPaU6FLUMRycOhwkVGzWxUb (LATEST, sha256 f6b95671... read back). drafting/v1 listing before 45 versions / after 47: diff = 2 added versions, both NU_US_Equity.json, 0 other keys (listing_diff.txt). AC2 YES (S1-S3 PASS, 0 of 123 restated, 0 of 123 glued, 5 names at or above base, NU 38 of 38); AC3 YES (200, 3 business locations, 53 of 53 English). | CLOSED 20261009T132039Z |

## Log

- 20261009T131736Z OPENED by 0.9.0_WK_AMGT_RESAPP~339 with 1 leg(s)
- 20261009T132039Z LEG L1 closed: NU drafting repaired in place, 38 sentences kept, 0 dropped, no fetch, no model call. AC1 YES before the write (K1 38 of
- 20261009T132039Z CLOSED -- all 1 legs proven
