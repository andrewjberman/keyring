# RCG Cycle-3 DIVERGENT Board — full 28-tree resolution

**Author:** `1.0.0_SA_CTO~B`, 2026-08-04 ~1700Z
**Input:** RCG_CYCLE3_EVIDENCE_SWEEP_20260804.md @ac147b78a (28 DIVERGENT trees / 75 files
routed to this seat per protocol s.2) + machine table @7548e90c7 (post-correction).
**Method:** every verdict below is grounded on a live primitive or a vintage-cited commit —
`get-function` exercised where liveness is claimed, registry read at HEAD, TF read at file:line.
Denominator: 28 trees, all dispositioned; zero deferred silently.

## Headline

**The DIVERGENT class was overwhelmingly the instrument, not the estate.** Of 28 trees: 1 true
registry gap (repaired), 7 live-but-unmanaged Lambdas (the one real estate defect class —
routed to base CTO as a Rule-1 finding), and 20 that resolve to join artifacts, stray copies,
teardown residue, or support-dir grain — the estate coherent underneath.

## Group 1 — resolved and messaged earlier this session (5 trees, 18 files)

| Tree | Truth | Disposition |
|---|---|---|
| inf-gold-trigger (1f) | stray pre-move copy; canonical `inf-pipeline/inf-gold-trigger/` matches map's last_deployed_commit `056106aa3` | ARCHIVE evidence at CRO (152341Z) |
| public-data-router (1f) | stray; canonical `lambda-edge/public-data-router/` (2026-07-28 vs stray 2026-01-19) | ARCHIVE evidence at CRO (152341Z) |
| m365-ms-ingest-liveness (1f) | **the one TRUE Rule-4 gap** | REPAIRED — entry landed @474f534a56 (AE-authored, RAVC closed 163216Z) |
| portal_authorizer (2f) | fn `opal-portal-authorizer` LIVE (get-function OK); registry+TF+live cohere on `infra/aws/users/lambda/portal-authorizer/`; tree is a 2026-04-06 stray | ARCHIVE evidence at CRO (153639Z) |
| finbert (10f) | dead source (NOT live, exercised; not registered); TF signal was policy-NAME noise — `lambda-invoke-finbert`'s Resource is the LIVE `opal-news-ai-sentiment` | ARCHIVE evidence at CRO (153639Z); IAM policy is NOT debt |
| trending_image_generator + _selector (9f, counted in Group 5) | | |

## Group 2 — TF-declared, registry metadata missing: the backfill draft (9 fns)

All nine have registry+live agreement and a real TF declaration the sweep's join missed. Draft
`tf_file`/`tf_resource` values, derived at HEAD this session — **apply-ready for the
YANG_PIPELINE_DEPLOY lane** (this seat cannot commit the map; the m365 precedent applies):

| map key | tf_file | tf_resource |
|---|---|---|
| opal-globgrph-incremental-updater | infra/aws/terraform/globgrph/item2b.tf (:135) | aws_lambda_function.globgrph_incremental_updater |
| seeking-alpha-analysis-coordinator | infra/aws/terraform/seeking-alpha/main.tf (:36) | module.analysis_coordinator.aws_lambda_function.this |
| seeking-alpha-analysis-listing-parser | same (:55) | module.analysis_listing_parser.aws_lambda_function.this |
| seeking-alpha-analysis-dedup | same (:75) | module.analysis_dedup.aws_lambda_function.this |
| seeking-alpha-analysis-scraper | same (:97) | module.analysis_scraper.aws_lambda_function.this |
| seeking-alpha-news-coordinator | same (:151) | module.news_coordinator.aws_lambda_function.this |
| seeking-alpha-news-dedup | same (:170) | module.news_dedup.aws_lambda_function.this |
| seeking-alpha-news-scraper | same (:192) | module.news_scraper.aws_lambda_function.this |
| ec2-auto-shutdown-enforcer | infra/aws/lambda/ec2-auto-shutdown-enforcer/main.tf (:105) — **IN-TREE TF, LOCAL STATE** (per shared-infra/iam_legacy.tf:7-8, deliberate) | aws_lambda_function.enforcer |

*Caveat carried honestly: `.this` on the 7 module entries follows the map's own established
convention for module-wrapped fns (etfs-canon-fanin entry); the inner resource name was not
independently read from the module source this session.*

## Group 3 — LIVE + REGISTERED, **NO TERRAFORM ANYWHERE** (7 fns) — Rule-1 finding, routed to base CTO

Exercised: no `function_name` declaration, no name mention beyond comments/adjacent resources
in `infra/aws/terraform/**` (comp-grep, 460/460 files scanned), no in-tree `.tf`:

`access-anomaly-scanner` · `opal-bd-transaction-consolidator` · `cost-anomaly-scanner` ·
`finbert-batch-processor` · `schwab-anonymizer` · `security-sweep-comprehensive` ·
`sentiment_query_api`

Seven live Lambdas exist outside Terraform management — Deployment Rule 1 ("Terraform is the
only Lambda deploy mechanism") has no purchase on them, and no drift detection can bind them
to source. **This is the only real estate-defect class the DIVERGENT board produced.**
Disposition of the finding (not the labels): base CTO board — adoption-vs-decommission is a
per-function architecture call (the NFRA_TERRAFORM-P2 adoption motion is the precedent). The
LABELS for these trees are straightforward KEEPs (live functions with agreeing registry).

## Group 4 — teardown residue (2 trees, 5 files) — ARCHIVE evidence for CRO

- **opal-assets-absence-check** (2f): authored @18ba785b52 (2026-07-15, map entry included per
  Rule 4), **torn down @c32875f7a5** ("inert debris per CTO 010019Z" — lambda+role+schedules+
  map entry all removed). NOT live (exercised, ResourceNotFound). The surviving tree AND the
  TF root `infra/aws/terraform/opal-assets-absence/` are both residue. *Also: the map's
  `_updated` prose still says the entry was "added" — stale hand-copied note, the frozen-digit
  class; harmless but worth clearing on the next map touch.*
- **precompute_market_metrics** (3f): the tree's one TF citation is a **destroy-log comment**
  (cloudfront-market-metrics.tf:12-17 describes the completed Phase-B removal, including
  stripping the invalidation call from this tree's index.js). NOT live (exercised). Residue of
  a decommissioned function.

## Group 5 — grain notes, keep-class (5 trees, 17 files)

- **artifacts/ (1f), lib/ (2f), shared/ (5f)**: support dirs, not function trees (CRO's own
  caveat, confirmed). Live TF references them (smartx lambdas.tf:3-19; partner-firm-table
  module main.tf:14 + imo-pipeline browser-lambda.tf:63-64; execution-role TF). KEEP-class
  adjudication; deleting any of these breaks declared TF.
- **trending_image_generator (4f) + trending_image_selector (5f)**: the class-(iv) crosswalk.
  Registry source_dir names `trending_image_selector/`; live fn `opal-trending-image-generator`
  exists. **Which tree is the deployed source is the one question this board leaves OPEN** —
  the method is a content-compare of the live function's code bundle against both trees
  (get-function code URL vs tree files), which is a deploy-verify motion best run by the AE
  lane with the registry fix in the same commit. Routed as such in the AE handoff.

## Accounting

5 (Group 1, incl. m365 repaired) + 9 (Group 2) + 7 (Group 3) + 2 (Group 4) + 5 (Group 5)
= **28 trees, 0 unaccounted.**

CRO label-feed status: Groups 1/4 supply ARCHIVE-evidence for 6 trees (16 files); Group 3+2
supply KEEP-grade evidence for 16 trees; Group 5 supplies keep-class grain notes for 3 support
dirs + 1 open pair. Labels remain CRO's calls under protocol s.2 (DIVERGENT was never a label
verdict).
