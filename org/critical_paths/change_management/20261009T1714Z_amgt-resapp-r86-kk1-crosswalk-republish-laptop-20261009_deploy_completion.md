# Deploy Completion Record
**Date opened:** 2026-10-09T17:14:41.838580+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T180023Z
**Deploy:** AMGT_RESAPP r86 AMGT-kk-1: same-key versioned re-put of s3://opal-data-harvest/crosswalk/v1/2026-10-09.json from the laptop so research_universe carries its live folder count (102); prior VersionId CHWQWAM0oNxOpU_5Hs8_fy5RUZ_Sgl20; rollback is a versioned re-put of the prior bytes, NEVER a delete
**Authored by:** 0.7.0_AE_CloudOps~AMG
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | AMENDMENT 3 ancestry print immediately before the put | 20e0b6408b, cb16f8b2f9, d2eb7316f2 each rc=0 against HEAD, 96a82dda90 rc=0 as the positive control | Printed in C:/tmp/amg-kk1 at HEAD 778e99abd8 immediately before the put: 20e0b6408b rc=0 / cb16f8b2f9 rc=0 / d2eb7316f2 rc=0 / 96a82dda90 rc=0 (positive control). Graph only -- no git show, no git log -p, no checkout of those commits or their paths. STOP had fired at f2dbac84a4 (three rc=1) and was cleared by merging origin/CLOUD @dbf224fbf1 (merge 80c910315f). | CLOSED 20261009T171942Z |
| L2 | verify | AC1 on the --out candidate with AMENDMENT 4's amended --admit, graded BEFORE the put | C1-C5 PASS and R85 CROSSWALK AC1: YES and exit=0 | r85_crosswalk.py --crit AC1 --path <candidate2> --reference crosswalk/v1/2026-10-07.json --admit <AMENDMENT 4 list incl research_universe.source>: PASS C1 (243 of 243 prior records present), PASS C2, PASS C3 (204 of 243 issuer.cik measured, 0 bad), PASS C4 (4 of 4), PASS C5 (0 not admitted; folders 102); R85 CROSSWALK AC1: YES; exit=0. Candidate rebuilt on post-merge code (850198 bytes, records=243, with_issuer_cik=204); the merge touched 0 files under lib/research/. | CLOSED 20261009T171942Z |
| L3 | activation | the same-key --write-pool put of crosswalk/v1/2026-10-09.json | the CLI OK line with the new document-sha256, plus head-object showing a NEW VersionId distinct from CHWQWAM0oNxOpU_5Hs8_fy5RUZ_Sgl20 | CLI: 'OK: uploaded s3://opal-data-harvest/crosswalk/v1/2026-10-09.json ContentLength=850198 document-sha256=0229681e6db25ab54f14c18d103180f4da7869f01f965b33527d24a719d9e52c schema-version=1 records=243 MEASURED=243 UNRESOLVED=0', exit=0. head-object read back: NEW VersionId d3y5Cbs6ygTMvKj28fSvbR4ciDsyPv.9, ETag 34365cc5a62fca5f33f4b122024cd5e4, SSE AES256, distinct from the prior CHWQWAM0oNxOpU_5Hs8_fy5RUZ_Sgl20. list-object-versions: DENOMINATOR 2 version(s) -- the prior version is still present with latest=false, so the rollback (a versioned re-put of its bytes) is intact and NO delete was made. | CLOSED 20261009T172518Z |
| L4 | verify | AC1 re-run against the SERVED key after the put | R85 CROSSWALK AC1: YES and exit=0 reading the live pool | AC1 re-run LIVE against the served key (no --path), AMENDMENT 4 --admit: PASS C1 (243 of 243 prior records present; latest reads crosswalk/v1/2026-10-09.json), PASS C2, PASS C3 (204 of 243, 0 bad), PASS C4 (4 of 4), PASS C5 (0 not admitted; folders 102); R85 CROSSWALK AC1: YES; exit=0. | CLOSED 20261009T172518Z |
| L5 | verify | AC2 and AC3 after the put | R84 LISTING AC1: YES exit=0; pytest guard arms 10 passed exit=0 | AC2: PASS R1/R2/R3 (3 of 3 byte-equal to base); R84 LISTING AC1: YES; exit=0. AC3: py -3.12 -m pytest lib/research/identity/tests/test_crosswalk_refuses_absent_library.py -q -> 10 passed; exit=0. Both run AFTER the put. | CLOSED 20261009T172518Z |

## Log

- 20261009T171441Z OPENED by 0.7.0_AE_CloudOps~AMG with 5 leg(s)
- 20261009T171942Z LEG L1 closed: Printed in C:/tmp/amg-kk1 at HEAD 778e99abd8 immediately before the put: 20e0b6408b rc=0 / cb16f8b2f9 rc=0 / d2eb7316f2 
- 20261009T171942Z LEG L2 closed: r85_crosswalk.py --crit AC1 --path <candidate2> --reference crosswalk/v1/2026-10-07.json --admit <AMENDMENT 4 list incl 
- 20261009T172518Z LEG L3 closed: CLI: 'OK: uploaded s3://opal-data-harvest/crosswalk/v1/2026-10-09.json ContentLength=850198 document-sha256=0229681e6db2
- 20261009T172518Z LEG L4 closed: AC1 re-run LIVE against the served key (no --path), AMENDMENT 4 --admit: PASS C1 (243 of 243 prior records present; late
- 20261009T172518Z LEG L5 closed: AC2: PASS R1/R2/R3 (3 of 3 byte-equal to base); R84 LISTING AC1: YES; exit=0. AC3: py -3.12 -m pytest lib/research/ident
- 20261009T180023Z CLOSED -- all 5 legs proven
