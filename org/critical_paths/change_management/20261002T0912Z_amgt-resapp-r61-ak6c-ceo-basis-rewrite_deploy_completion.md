# Deploy Completion Record
**Date opened:** 2026-10-02T09:12:21.304278+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 61 AMGT-ak-6 act (C) (AMENDMENT 2, its own never-widen pair): cell B5's STORED-FIELD REWRITE -- 7 keys under management/v1 in the versioned bucket opal-data-harvest, one field ceo_public_profile.basis, per key GET + assert before + set after + PUT whole at the same key. No redeploy, no code change, no model call. Never-widen pair COO 7bbf273c19 (correction) / CTO bbbda2e848 (re-signed with one named exception); plan m1_ceo_basis_plan.json frozen at sha256 b0c9b6dd..1401, re-hashed at act time and MATCHING; base + rollback appendix round61/AK6C_BASE_VERSIONS.json, 7 of 7 versioned, 0 before-mismatches at signing. VLO's base is the version act (A) wrote, so act (C) builds on it
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | the B5 stored-field rewrite: PUT 7 keys under management/v1 in s3://opal-data-harvest, each GET then asserted then whole-object PUT at the SAME key, only ceo_public_profile.basis set | ak6_store_writes_c.json lists 7 of 7 keys written with prior and new VersionId; every entry's declared before asserted EQUAL across all 7 keys BEFORE any put; a differing before is a STOP with nothing written |  | OPEN |
| L2 | verify | ak6_verify.py over the B5 plan and the act (C) appendix, read-only (CTO conditions 1-3 plus C4) | C1 the plan sha256 equals the half's value; C2 7 of 7 basis fields read their after; C3 7 of 7 objects with ceo_public_profile.basis masked equal their BASE VersionId object masked the same way, which for VLO also proves act (A)'s lusha_enrichment.reason and officers are intact; C4 7 of 7 moved off base; AK6 READ-BACK CLEAN: YES and exit=0 |  | OPEN |
| L3 | verify | ak6c_reading.py --what post against the pre captured off the deployed function, with the one named exception (CTO condition 4) | C1 reading STATE equal 7 of 7; C2 urls_returned equal on 6 of 7 with SAP_GY_Equity None to 10 as the named exception; C3 reason and basis carry neither SERP nor the contract's-search phrase 7 of 7; AK6C READINGS HOLD AND SPEAK WORDS: YES and exit=0. Any OTHER urls_returned move, or any state move, is a ROLLBACK |  | OPEN |
| L4 | verify | AC b5 b_served_text.py --cell b5 --where deployed, graded on the SERVED route (CTO condition 5) | C1 PASS 0 of 2 served basis strings on BA and VLO carry the code-shaped phrasing, from 2 of 2 at base; B5 verdict YES; exit=0 |  | OPEN |

## Log

- 20261002T091221Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
