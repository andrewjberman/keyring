# Deploy Completion Record
**Date opened:** 2026-10-02T08:29:31.046084+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 61 AMGT-ak-6: the B2/B3/B4 STORED-FIELD REWRITE -- 251 distinct keys / 1,188 entries in the versioned bucket opal-data-harvest (8 management/v1, 234 peers/v1, 9 posture/v1), per key GET + assert every before + set after + PUT whole at the same key. ACT (A) ONLY per AMENDMENT 1: NO build, NO upload, NO apply -- 0 of 350 packaged members changed between the deployed ak-2 build and the merged round-61 tree. Never-widen pair COO fa9c914db9 / CTO af95b2f1c0; plans frozen at sha256 d373d061.. (B2, read from worker commit 25ac521b3d), 11518fd5.. (B3), 0e77bc0c.. (B4), all three re-hashed at act time and MATCHING; base + rollback appendix round61/AK6_BASE_VERSIONS.json, 251 of 251 keys versioned, 0 before-mismatches at signing
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | the stored-field rewrite: PUT 251 distinct keys in s3://opal-data-harvest (management/v1, peers/v1, posture/v1), each object GET then asserted then whole-object PUT at the SAME key, all entries for one key applied in ONE put | ak6_store_writes.json lists 251 of 251 keys written with prior and new VersionId and the fields set; every entry's declared before asserted EQUAL before any put to that key; 1188 of 1188 entries applied; a differing before is a STOP for the whole act with nothing further written |  | OPEN |
| L2 | verify | ak6_verify.py conditions 1-3 plus C4, read-only, over all three plans and the base appendix | C1 the three plan sha256 equal the halves table in order; C2 251-key/1188-field read-back, every planned field equals its after; C3 every object with its planned fields masked equals its BASE VersionId object masked the same way (the whole-object PUT changed nothing else); C4 every key moved off its base VersionId; AK6 READ-BACK CLEAN: YES and exit=0 |  | OPEN |
| L3 | verify | AC1 b_served_text.py --cell b2 --where deployed, graded on the SERVED route | C1 PASS 0 of the Lusha and peers absent reasons for BA and VLO carry a code-shaped token (base 11 of 26) and C2 PASS; B2 EVERY SERVED REASON IS WORDS: YES; exit=0 |  | OPEN |
| L4 | verify | AC2 b_served_text.py --cell b3 --where deployed, graded on the SERVED route | C1, C2 and C3 PASS: VLO officers carry person names and full titles with no trailing age, BA 12 unchanged; B3 EVERY OFFICER CARRIES A FULL TITLE AND NO AGE: YES; exit=0 |  | OPEN |
| L5 | verify | AC3 b_served_text.py --cell b4 --where deployed, graded on the SERVED route | C1 and C2 PASS 0 of BA's and VLO's posture claims carry a status token (base 2 of 12); B4 EVERY POSTURE CLAIM STATES A MISSING SCORE IN WORDS: YES; exit=0 |  | OPEN |

## Log

- 20261002T082931Z OPENED by 0.7.0_AE_CloudOps~A with 5 leg(s)
