# NFRA_IAMROLES202609 -- ROUND-6 ANALYSIS (L10 answer)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-11 ~04:3xZ. **Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 33175,
`surprise-channel/remediations/REMEDIATION_v6.Z.md` @bd4025ade2. **Recut by:** `2.0.0_SA_COO~ZI`, in ONE issuance.

## Round 6, as read

4 of 4 orders are complete with VALID proofs (`ledger/COMPLETION_REPORT.round6.json` @dfe1a35d13). L9 AC4 x4 PASS (C-S28..S31).
The custody grades rest on CloudTrail: each of the five adopted roles carries exactly one IAM write since 10-09 (a TagRole),
and the account-wide TagRole count is the same five. C-S32 dismisses 12 rows. Z-S37 is OVERTAKEN by Andrew's ~03:2xZ yes
and the R20 entries @bd2cacee69. C-S33 graduates 5 rows.

**FWD-4 is REALIZED.** Its bar is "each one is either in code or carries a named owner and a reason". 6 of 16 rows are in
code, and the other 10 each carry the named owner `0.7.0_AE_CloudOps~Z` and a recorded reason (the CVO: "every row is
owned"). The work below enriches FWD-4 and does not re-open it.

## Rulings on the slug

| item | ruling |
|---|---|
| Family C: rows 6 `lambda-ec2-runtime-monitor-role` and 14 `sentiment_query_api-role` (the last two ADOPT rows) | **Round 7, E1**, the same shape as round 6: one apply, ledger and never-widen pair per module, in the A4-r6 order (commit the declaration first, then import, then drain). Row 6 goes into a NEW file in `shared-infra` (round-5 ruling). Row 14's module is named by the survey. **Its name carries an underscore, so the survey runs the real commit path before touching AWS** (Z-S27's lesson). If the naming gate refuses it on a limb no override reaches, the cell stops and the issuer brings it here, before any import |
| Family F: row 7 `lambda-test-role`, RETIRE | **Andrew's word first.** Deleting an IAM role cannot be undone: a re-created role gets a new role id, so trust and resource policies that pin the old principal break. The issuer files the call with the disposition's three-plane evidence. E3 is cut only on his yes |
| Z-S23 (`opal-smartx-lambda-role`) and Z-S32 (`codebuild-semantic-clustering-role`): grants on resources that do not exist | **NARROW, round 7 E2.** S3 bucket names are global, so an Allow on a bucket that does not exist grants access to whoever creates that name later. Removing the dead statements is a narrowing, a WORLD act under its own pair. The pair names what remains and shows the removed ARNs resolve to nothing (NoSuchBucket, absent secrets) |
| GOVERNANCE_DISPOSITION.md still reads ADOPT for the five adopted rows | **Batch repair at the drain:** the five tokens move to the in-code value, each citing its round-6 order. Record hygiene only, no WORLD act |
| Z-S21 (smartx-pipeline's three pre-existing Lambda drifts) | **Not this project's cell.** It routes to the smartx pipeline's owner through `0.0.0_AB_MSTR~Z` (as W13-S1 did). Until it is resolved, every apply of that module is `-target` scoped |
| Z-S25, Z-S34 (naming-gate pre-image; the R20 bridge, cutoff 2026-12-31) | **Carried, no cell.** Both close when dell1 serves LGIC_ENFORCE FWD-8 (XB-dcb5). The issuer's close note carries the 2026-12-31 date: before that date, either FWD-8 is served and the two R20 entries retire, or Andrew re-decides the exception |

## ENRICHMENT LIST -- round 7 (cut in ONE issuance)

| # | cell | rows | done when |
|---|---|---|---|
| E1 | adopt Family C, one apply per module | 6, 14 | the declaration commits through every gate BEFORE the import; `import` applied; the targeted re-plan reads 0/0/0; live tags equal the module's `default_tags`; the shared-tree plan reads `0 to destroy` after the drain |
| E2 | narrow the dead grants | Z-S23, Z-S32 | the removed statements named only non-existent resources (read live, with a positive control on one existing resource); the role's remaining policy is unchanged apart from them |
| E3 | **conditional on Andrew's yes**: retire `lambda-test-role` | 7 | the role is absent; three planes read 0 references both before and after |

The batch repair at the drain is the five disposition tokens.

-- 1.0.0_SA_CTO~Z
