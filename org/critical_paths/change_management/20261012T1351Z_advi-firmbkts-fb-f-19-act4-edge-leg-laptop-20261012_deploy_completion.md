# Deploy Completion Record
**Date opened:** 2026-10-12T13:51:19.414471+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-19 act 4 laptop leg (GO @8cd6a18a3b, crossbox ae20): rebuild and re-associate the 3 protected edge functions from the flipped tree (flip 69679b90e3 + re-pins e274a0e60c, HEAD 20215ccd98), via safe-apply on portal-auth, under the never-widen pair NEVER_WIDEN_ROUND4_ACT4_CUTOVER (COO half + ADDENDA 1,2, CTO half + ADDENDA 1-5, all SIGNED). PRE-ACT: distribution EVTSA9VEHNZVH Deployed ETag ELAAK8OWYOWV1 (30 behaviors); shared-advisor-router v27 CodeSha256 cOG/BuFhy9xcL7EF+4u5VexRZGjDdJq3h364PAPkYsw= x5 origin-request; shared-advisor-router-response v6 YIgGtFjZwFltdXbviIx5dOQbb6FsOAUtIB96caAI0xs= x5 origin-response; auth-validator-edge v22 eNvtV2EFQF/pnJCJQyXtEaiHSePaJNL56Cws7m8tf5w= x26 viewer-request; WAF opal-cloudfront-protection a09833c0 LockToken 848a6d0b (6 rules). ROLLBACK = re-associate router 27, guard 6, validator 22 on every behavior and read the associations, the same hour; Branch B also rolls back act 2 (gold_dispatch.sh re-deploy is the dell1 seat FB1, named in the report); WAF pre-act JSON re-apply. Dell1 leg is FB-f-11 (FB1), same minute, first and last unit times printed on both sides.
**Authored by:** 0.7.0_AE_CloudOps~FBL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | step 0 gate and step 1 pre-act reads: pair SIGNED both halves, flip+re-pins ancestor of HEAD, registry routed false, firm-config buckets, 12 of 12 simulate pairs + control, distribution/functions/WAF pre-state saved | files in deliverables/0.7.0_AE_CloudOps~FBL/evidence_f19/ |  | OPEN |
| L2 | verify | step 2 build of 3 artifacts from HEAD; router test 51 pass 0 fail; guard and validator counts; bytes above 127; sha256 each | 3 sha256 lines, counts, non-ASCII counts |  | OPEN |
| L3 | verify | step 3 pre-flip r4_oai.py on the built tree and step 4 scoped plan JSON read | ROUND 4 OAI PREFLIGHT 3 of 3 arms; plan names exactly 3 functions + distribution + WAF version rider |  | OPEN |
| L4 | activation | step 4 safe-apply of the saved plan; first and last unit time printed | apply summary rc=0 with start and end times |  | OPEN |
| L5 | verify | step 5 read after: CodeSha256 equals artifact for each, every association names the new version with counts, distribution Deployed, WAF rule-by-rule equality, post-apply plan line | per-function version+sha+association counts, plan line |  | OPEN |
| L6 | verify | step 6 validator CloudWatch log read in every edge region with denominator; first non-admin request line reading the ownership map at the canonical key | regions read N of M, line quoted or Branch B |  | OPEN |
| L7 | verify | step 7 ACT4_EDGE_EXPECT.json written then AC1 r4_act4.py --arms edge 6 of 6 and AC2 r4_oai.py 3 of 3 | both expect lines printed |  | OPEN |

## Log

- 20261012T135119Z OPENED by 0.7.0_AE_CloudOps~FBL with 7 leg(s)
