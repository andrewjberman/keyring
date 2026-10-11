# Deploy Completion Record
**Date opened:** 2026-10-11T15:56:08.365305+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261011T160043Z
**Deploy:** ADVI_FIRMBKTS TO-FB-f-16 (act 0 addendum, row D1-S29): ONE statement AdviPlatinumCanonicalDelete (s3:DeleteObject on two advisor-scoped prefixes of the canonical home) added in place to policy advi-49f-platinum-canonical-rw-policy on role bd-exporter-ec2-role (root infra/aws/terraform/bd-pipeline); pair: act-0 COO half ADDENDUM 1 @bda6f4ebc4 + CTO half ADDENDUM 2 @44e7a3f712; rollback = the prior two-statement document put back from the printed file; the QA runner shares the role and receives the same Allow; inert until a producer deletes at the canonical home
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-write reads: pair SIGNED at the current bytes, the prior two-statement policy printed to deliverables/PRIOR_advi-49f-platinum-canonical-rw-policy_<UTC>.json, role inline policy count | the entry carries the file path and the count | act-0 COO half ADDENDUM 1 @bda6f4ebc4 and CTO half ADDENDUM 2 @44e7a3f712 SIGNED at the current bytes (0 uncommitted); prior policy printed to org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1/PRIOR_advi-49f-platinum-canonical-rw-policy_20261011T155645Z.json reading 2 statements (AdviPlatinumCanonicalObjects, AdviPlatinumCanonicalList) before any plan; role inline policy count 17 (paginated, client-side) | CLOSED 20261011T160043Z |
| L2 | activation | scoped plan of bd-pipeline reads Plan: 0 to add, 1 to change, 0 to destroy (one policy, in place); .tools/safe-apply.sh on the saved plan | plan summary line and apply result line | scoped plan Plan: 0 to add, 1 to change, 0 to destroy (1 resource in place, attribute policy; first two statements byte-equal to the prior, third exactly AdviPlatinumCanonicalDelete: s3:DeleteObject on the two advisor-scoped ARNs, no Condition); --dry-seat-gates read first, 8 hits read and disjoint (row ADVI_FIRMBKTS-D1-S31); .tools/safe-apply.sh on the saved plan 15:58:27Z-15:58:56Z: Apply complete! Resources: 0 added, 1 changed, 0 destroyed | CLOSED 20261011T160043Z |
| L3 | verify | AC1 three Sids, AC2 the third statement's one action and two resources, AC3 scoped plan No changes; role policy count unchanged at 17 | the three outputs quoted | AC1 AdviPlatinumCanonicalObjects AdviPlatinumCanonicalList AdviPlatinumCanonicalDelete; AC2 s3:DeleteObject on arn:aws:s3:::opal-data-49financial/advi/49financial/platinum/advisors/* and .../entities/advisors/*; AC3 No changes. Your infrastructure matches the configuration.; role policy count 17 unchanged; read 2026-10-11T15:59:06Z | CLOSED 20261011T160043Z |
| L4 | git | proof instance and prior policy file written, status flipped complete in one commit | commit hash | proof instance, prior policy file and act0_delete evidence committed with this entry; TO-FB-f-16 status flipped complete in the same commit; commit hash is this commit | CLOSED 20261011T160043Z |

## Log

- 20261011T155608Z OPENED by 0.7.0_AE_CloudOps~FB1 with 4 leg(s)
- 20261011T160043Z LEG L1 closed: act-0 COO half ADDENDUM 1 @bda6f4ebc4 and CTO half ADDENDUM 2 @44e7a3f712 SIGNED at the current bytes (0 uncommitted); p
- 20261011T160043Z LEG L2 closed: scoped plan Plan: 0 to add, 1 to change, 0 to destroy (1 resource in place, attribute policy; first two statements byte-
- 20261011T160043Z LEG L3 closed: AC1 AdviPlatinumCanonicalObjects AdviPlatinumCanonicalList AdviPlatinumCanonicalDelete; AC2 s3:DeleteObject on arn:aws:s
- 20261011T160043Z LEG L4 closed: proof instance, prior policy file and act0_delete evidence committed with this entry; TO-FB-f-16 status flipped complete
- 20261011T160043Z CLOSED -- all 4 legs proven

## ACT 0 DELETE STATEMENT OUTCOME (0.7.0_AE_CloudOps~FB1, 2026-10-11T16:00:42Z)

- **Pair:** COO half ADDENDUM 1 (`bda6f4ebc4`) and CTO half ADDENDUM 2 (`44e7a3f712`), SIGNED at the current bytes (0 uncommitted).
- **Prior policy printed first:** `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1\PRIOR_advi-49f-platinum-canonical-rw-policy_20261011T155645Z.json`: 2 statements (`AdviPlatinumCanonicalObjects`, `AdviPlatinumCanonicalList`); the role held
  17 inline policies (paginated count).
- **Plan (scoped, saved):** `Plan: 0 to add, 1 to change, 0 to destroy`, one resource in place, attribute `policy` only. The first two
  statements byte-equal to the prior; the third is exactly `AdviPlatinumCanonicalDelete`, Allow, `s3:DeleteObject`, the two ARNs
  `.../platinum/advisors/*` and `.../platinum/entities/advisors/*`, no Condition, no `DeleteObjectVersion`, no `s3:*`.
- **Seat gates:** `--dry-seat-gates` first. 8 hits (5 OPEN-CALL on this project or on NFRA_MCPINDEX, 1 OVERLAP, 2 OPEN-DEPLOY); every one
  read. The two deploys read CLOSED in this tree (`iamroles-r6-family-a`: other roles; `healgap-r3-act3-asset-dim-reattempt`: not this
  root's role). WARN mode; the OVERLAP is the code-not-on-CLOUD exposure in row `ADVI_FIRMBKTS-D1-S31`.
- **Apply:** 15:58:27Z to 15:58:56Z, `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`
- **After (15:59:06Z):** AC1 three Sids; AC2 `s3:DeleteObject` on the two ARNs; AC3 `No changes.`; role policy count 17 (unchanged).
- **QA runner:** shares this role and receives the same Allow (stated by the pair); `FB-g-15`'s guard keeps QA off `canonical`.
- **Rollback, unused:** put `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.7.0_AE_CloudOps~FB1\PRIOR_advi-49f-platinum-canonical-rw-policy_20261011T155645Z.json` back as the policy document through `safe-apply`; per object, versioning makes each delete a marker.
