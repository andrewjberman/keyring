# Deploy Completion Record
**Date opened:** 2026-10-09T12:47:39.891174+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261009T125053Z
**Deploy:** AMGT_RESAPP round 85 AMGT-jj-4: publish crosswalk/v1/2026-10-09.json (name list with measured issuer CIKs), ONE new key under s3://opal-data-harvest/crosswalk/v1/ via crosswalk --write-pool; pair COO @263271c6db + CTO @29112515f4. Prior latest 2026-10-07.json VersionId XledA4XthVEOE3snOolYp7lkbarhPNkx (243 records, 800952 bytes). Pre-publish diff: 243 of 243 prior records equal apart from issuer, 0 dropped, 204 issuer fields all measured+source. ROLLBACK (never a delete; bucket is versioned, bad version kept): re-put crosswalk/v1/2026-10-09.json with the byte content of 2026-10-07.json (VersionId XledA4XthVEOE3snOolYp7lkbarhPNkx), then check the served read the same hour; CTO half cond.3 governs (a newer dated key would be future-dated). Task family: none (no Lambda, no image, no schedule)
**Authored by:** 0.9.0_WK_AMGT_RESAPP~341
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | crosswalk/v1/2026-10-09.json put via crosswalk --write-pool, one new key under opal-data-harvest | crosswalk/v1/ listing before/after diff = one new key + VersionId + record count | listing crosswalk/v1/ before 7 keys, after 8; diff = ONE new key: 2026-10-09 08:48:27 850056 2026-10-09.json (VersionId CHWQWAM0oNxOpU_5Hs8_fy5RUZ_Sgl20, document-sha256 a03c8cac74f9ac439a325421683e9be4374b588815c65ef5e57060a97ec64d77, 243 records, 204 with issuer.cik); prior latest 2026-10-07.json VersionId XledA4XthVEOE3snOolYp7lkbarhPNkx 800952 bytes untouched, 243 records; pre-publish diff 243 of 243 equal apart from issuer, 0 dropped; evidence deliverables/0.9.0_WK_AMGT_RESAPP~341/listing_diff.txt | CLOSED 20261009T125052Z |
| L2 | verify | served read after the put | typed ASML still answers two candidates on the deployed function; r85_crosswalk AC1 YES; r84_store AC2 5 of 5 | deployed opal-amgt-scoped-api: typed ASML /resolve answers status candidates with 2 (ASML_US_Equity, ASML_NA_Equity), thesis/ASML 404 with the same 2; r85_crosswalk AC1 YES (C1 243 of 243, C2-C4 PASS) exit=0; r84_store AC2 ALL: YES 5 of 5 exit=0; C1 YES so rollback not executed; evidence AC1.out AC2.out asml_deployed.out | CLOSED 20261009T125053Z |

## Log

- 20261009T124739Z OPENED by 0.9.0_WK_AMGT_RESAPP~341 with 2 leg(s)
- 20261009T125052Z LEG L1 closed: listing crosswalk/v1/ before 7 keys, after 8; diff = ONE new key: 2026-10-09 08:48:27 850056 2026-10-09.json (VersionId 
- 20261009T125053Z LEG L2 closed: deployed opal-amgt-scoped-api: typed ASML /resolve answers status candidates with 2 (ASML_US_Equity, ASML_NA_Equity), th
- 20261009T125053Z CLOSED -- all 2 legs proven
