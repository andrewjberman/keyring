# Deploy Completion Record
**Date opened:** 2026-09-30T15:07:35.925267+00:00
**Status:** OPEN
**Deploy:** ONE WINDOW: IRPT_BCKEND IB-mr-291 narrowed Holdings release (IAM CanonicalClassifierLookup + re-mint 3 bundles + QA + served publication) with MDPF_SECCLASS BD_THREAD_R2 (5 BD files deployed + chain run + FWD-1 page read) -- halves COO 6d44575a7f / CTO b4cd4a46ba; packet ONE_WINDOW_PACKET_BD_THREAD_R2_AND_IB_MR_291_20260930.md
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| H1 | verify | terraform plan investor-reporting/directory from CLOUD | in-place policy updates for the Holdings principals only; 0 add 0 destroy; changed resources named | terraform plan investor-reporting/directory from CLOUD (HEAD past 9fef6a7e9c, init -reconfigure) 15:1xZ: Plan 0 to add, 3 to change, 0 to destroy -- aws_iam_role_policy.irpt_holdings[49financial], [cottonwood], [inflection] updated in-place (the CanonicalClassifierLookup statement); nothing else | CLOSED 20260930T151315Z |
| H2 | activation | safe-apply investor-reporting/directory | apply rc 0; re-plan 0-diff; per-firm get-role-policy names Sid CanonicalClassifierLookup | HALT_ACK=1 safe-apply 15:13:15Z investor-reporting/directory: aws_iam_role_policy.irpt_holdings[49financial\|inflection\|cottonwood] Modifications complete; Apply complete 0 added 3 changed 0 destroyed; re-plan -detailed-exitcode 0. Read-back get-role-policy irpt-49f/inf/cot-holdings-role x irpt-<f>-holdings-policy: Sid CanonicalClassifierLookup, Actions Query+GetItem, Resources table/etf-classifications + index/asset-class-index + index/sub-asset-class-index, at all three | CLOSED 20260930T152621Z |
| H3 | s3-prefix | safe-deploy --mint-bundle irpt_holdings_49f/inf/cot from CLOUD 9fef6a7e9c+ | BUNDLE MINTED x3 + head-object members-sha256 + member-count; closure carries bd_securities_fallback.py + etf_classifications_dynamodb.py |  | OPEN |
| H4 | verify | QA fire irpt-holdings-refresh-lambda {qa:true} | 3 of 3 Success; holdings_qa per firm: PHYS/GLD commodities/Metals, VXX structured/Hedge, to_unclassified 0; served manifests VersionId unchanged |  | OPEN |
| H5 | verify | served Holdings publication | served manifest advances per firm; PHYS reads commodities/Metals on the IR Holdings page |  | OPEN |
| B1 | s3-prefix | safe-deploy 5 BD files to opal-data-bd code/{gold,silver} | DEPLOYED + VERIFY OK per file, bytes = CLOUD HEAD |  | OPEN |
| B2 | verify | live IAM read bd-exporter-ec2-role | bd-securities-access attached with GetItem on etf-classifications; no new inline policy added |  | OPEN |
| B3 | activation | BD chain run (ordinary gold-layer trigger; ad-hoc QA fire the exercise, scheduled fire the acceptance) | build_bd_assets_dim, C_06 --upload, D_03 --upload, D_04; served firm_composition.json + platinum/clients/z08327149/summary.json advance; prior VersionIds recorded |  | OPEN |
| B4 | verify | COO's one live FWD-1 run to the page | z08327149: VXX structured/Hedge, GLD/PHYS commodities/Metals on the real page; bd_securities_reads 0 |  | OPEN |

## Log

- 20260930T150735Z OPENED by 2.0.0_SA_COO~M with 9 leg(s)
- 20260930T151315Z LEG H1 closed: terraform plan investor-reporting/directory from CLOUD (HEAD past 9fef6a7e9c, init -reconfigure) 15:1xZ: Plan 0 to add, 
- 20260930T152621Z LEG H2 closed: HALT_ACK=1 safe-apply 15:13:15Z investor-reporting/directory: aws_iam_role_policy.irpt_holdings[49financial|inflection|c
