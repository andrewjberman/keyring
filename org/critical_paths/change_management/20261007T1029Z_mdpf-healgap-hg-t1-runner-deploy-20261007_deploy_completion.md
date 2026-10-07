# Deploy Completion Record
**Date opened:** 2026-10-07T10:29:30.327268+00:00
**Status:** OPEN
**Deploy:** MDPF_HEALGAP.TO-HG-d1: cot-rebalancer-runner code-only deploy on THE LAPTOP (box) -- guard-by-listing + induce hook @ca914096d7; expected artifact sha QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk=; both never-widen halves SIGNED (COO 2.0.0_SA_COO~G1, CTO 1.0.0_SA_CTO~DELL1 @dd0b78fde7)
**Authored by:** 0.7.0_AE_CloudOps~F
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | preconditions 1-3 of CTO_RULINGS_FOR_THE_DELLS_20261007_0930Z.md s2 + both never-widen halves read at their own bytes | all three PASS and the two half blobs identical at dell1 GO commit 297e25e870 and at HEAD |  | OPEN |
| L2 | git | BUILD_ONLY build of cot-rebalancer-runner, sha checked BEFORE any upload (CTO half condition 2) | printed sha equals QxLvPLTMO5YSkS+vaRXEkhaA78ZAr1arTyS0ADOOMvk= else refuse |  | OPEN |
| L3 | verify | terraform plan -target=module.cot_rebalancer_runner in infra/aws/terraform/opal-assets (CTO half condition 1: the plan is the scope) | 0 to add, 0 to destroy, code-only; the plan change lines printed here |  | OPEN |
| L4 | activation | .tools/safe-apply.sh -target=module.cot_rebalancer_runner, then live read-back and 0-diff re-plan | Apply complete + live CodeSha256 equals the build sha + re-plan No changes |  | OPEN |
| L5 | git | lambda-source-map.json via record-terraform-deploy.sh, committed under this lane author line | commit hash + push state measured by ls-remote |  | OPEN |

## Log

- 20261007T102930Z OPENED by 0.7.0_AE_CloudOps~F with 5 leg(s)
