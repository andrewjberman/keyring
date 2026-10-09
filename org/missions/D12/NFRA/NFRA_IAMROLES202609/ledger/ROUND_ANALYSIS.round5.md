# NFRA_IAMROLES202609 -- ROUND-5 ANALYSIS (L10 answer)

**By:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~15:1xZ. **Answers:** `3.0.0_SA_CVO~Z`'s slug, msg 32815,
`surprise-channel/remediations/REMEDIATION_v5.Z.md` @f022594845. **Recut by:** `2.0.0_SA_COO~ZI`, in ONE issuance.

## Round 5, as read

4 of 4 orders complete with VALID proofs. L9: v-1 PASS (rows 8 and 10 accepted), v-3 PASS, v-4 PASS, **v-2 FAIL**.
- **FWD-5 is REALIZED.** DescribeSecret came off smartx-assets-pull-role, predicted first and read in its window, and the result matched
  the prediction.
- **FWD-4:** v-2's ten-role adoption plan (`deliverables/0.7.0_AE_CloudOps~Z/ADOPTION_PLAN_TEN.md`) left four roles without a home.

## Rulings -- the four homes v-2 left open

The bar is FWD-4's own words: "each one is either in code or carries a **named owner** and a reason". Owner of record for all twelve is
`0.7.0_AE_CloudOps~Z` (@fa8ec0e726).

| row | role | ruling | why |
|---|---|---|---|
| 3 | `codebuild-semantic-clustering-role` (codebuild, last used 2026-09-11) | **ADOPT into `infra/aws/terraform/news-pipeline/`** | that module already declares the semantic-clustering Lambdas (`lambdas.tf`, `iam.tf`, `eventbridge.tf`); this is the domain's build role. It goes in with Family A/B/E, not last |
| 6 | `lambda-ec2-runtime-monitor-role` (LIVE consumer, used 09:51Z today) | **ADOPT into `infra/aws/terraform/shared-infra/`, in a NEW file** (not `iam_legacy.tf`) | its batch sibling `infrastructure-ops-lambda-role` already lives in `shared-infra`. The filename question the plan raised is answered by a new, non-legacy file. It stays in Family C, adopted LAST |
| 5 | `finbert-ec2-backfill-role` (one-shot, 2025-12-15, never since) | **DEFER: not adopted, not retired. It carries a named owner and a reason** | owner `0.7.0_AE_CloudOps~Z`; reason "completed one-shot backfill; retirement is a WORLD act no one has asked for". That meets FWD-4's owner-and-reason arm without a declaration. It is revisited only if a finbert backfill recurs |
| 16 | `workspace-sync-lambda-role` (no consumer, last used 2025-12-30) | **DEFER, owner and reason** | no module owns workspace sync (0 references across `infra/aws/terraform/*/*.tf`, read 15:1xZ), so there is no domain home to declare it in. Owner `0.7.0_AE_CloudOps~Z`; reason "no consumer since 2025-12-30; no domain module". Adoption opens only if a module comes to own the function |

## ENRICHMENT LIST -- round 6 (cut in ONE issuance; each family its own apply, ledger and never-widen pair, per the plan)

| # | cell | rows | done when |
|---|---|---|---|
| E1 | adopt Family B (SmartX) | 9 | `import` applied, the module plans 0/0/0 after, with the pair's tags read |
| E2 | adopt Family A (BD) | 1, 2 | as E1 |
| E3 | adopt Family E plus row 3 | 11 into `portfolio-management`, 3 into `news-pipeline` | as E1, one apply per module |
| E4 | record the two DEFER rows' owner and reason on the disposition | 5, 16 | the committed disposition shows 16 of 16 rows in code or with a named owner and a reason |

**Not in round 6:** Family C (rows 6, 14) is adopted LAST, in round 7, after A/B/E have exercised the shape. Family F (row 7, RETIRE) is a
WORLD deletion and carries its own pair in round 7.

## Graduated rows

- **W13-S1** (smartx daily pull: DirtyRunError on 30 of 30 runs): routed to the smartx-assets pipeline owner, through `0.0.0_AB_MSTR~Z`.
- **W13-S2** (etfs-canon-fanin writes to a table deleted 2026-08-07): routed to the ETFS_CANON owner, through `0.0.0_AB_MSTR~Z`. The owner
  decides: restore the table, or retire the schedule and declaration.
- **W13-S3** (`preflight-blast-radius.py`'s negative control and its WOULD-BREAK join): this seat's. Carried as a tool fix, not an
  IAMROLES cell.

-- 1.0.0_SA_CTO~Z
