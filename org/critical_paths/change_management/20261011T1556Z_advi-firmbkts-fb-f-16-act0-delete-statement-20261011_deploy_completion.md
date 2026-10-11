# Deploy Completion Record
**Date opened:** 2026-10-11T15:56:08.365305+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-16 (act 0 addendum, row D1-S29): ONE statement AdviPlatinumCanonicalDelete (s3:DeleteObject on two advisor-scoped prefixes of the canonical home) added in place to policy advi-49f-platinum-canonical-rw-policy on role bd-exporter-ec2-role (root infra/aws/terraform/bd-pipeline); pair: act-0 COO half ADDENDUM 1 @bda6f4ebc4 + CTO half ADDENDUM 2 @44e7a3f712; rollback = the prior two-statement document put back from the printed file; the QA runner shares the role and receives the same Allow; inert until a producer deletes at the canonical home
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-write reads: pair SIGNED at the current bytes, the prior two-statement policy printed to deliverables/PRIOR_advi-49f-platinum-canonical-rw-policy_<UTC>.json, role inline policy count | the entry carries the file path and the count |  | OPEN |
| L2 | activation | scoped plan of bd-pipeline reads Plan: 0 to add, 1 to change, 0 to destroy (one policy, in place); .tools/safe-apply.sh on the saved plan | plan summary line and apply result line |  | OPEN |
| L3 | verify | AC1 three Sids, AC2 the third statement's one action and two resources, AC3 scoped plan No changes; role policy count unchanged at 17 | the three outputs quoted |  | OPEN |
| L4 | git | proof instance and prior policy file written, status flipped complete in one commit | commit hash |  | OPEN |

## Log

- 20261011T155608Z OPENED by 0.7.0_AE_CloudOps~FB1 with 4 leg(s)
