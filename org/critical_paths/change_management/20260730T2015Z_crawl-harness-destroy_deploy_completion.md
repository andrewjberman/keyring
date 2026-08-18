# Deploy-completion ledger — crawl-harness stack DESTROY

**Status:** CLOSED 2026-07-30 ~20:2xZ (every leg finished in-session; 16 destroyed, live-plane verified)
<!-- scanner-alignment line added 2026-08-18 by 0.0.0_AB_MSTR (RED-disposition act, org/tier0_exec/0.0.0_AB_MSTR/deliverables/DEPLOY_LEDGER_RED_DISPOSITIONS_20260818.md): mirrors this file's own close declaration below; deploy_ledger.py's unindexed scanner could not read the original form (defects A/B/shape-C, see the disposition doc). Not a new closure. -->

**Opened:** 2026-07-30 ~20:15Z (at deploy-start, per CLAUDE.md NEVER#6)
**Owner:** `0.7.0_AE_CloudOps` · **Stack:** `infra/aws/terraform/crawl-harness/` (state key `crawl-harness/tfstate`)
**Authorization:** Andrew-direct 2026-07-30 ~19:2xZ verbatim *"I dont care about any of these crawl
functions, all of it can go"*; execution ordered ~20:1xZ *"do the crawl-harness destroy"*. CTO
endorsed under the approved tranche plan (TF-debt B1 + A3 + G1).

## Why this is safe to destroy (measured, not assumed)
- `orion-crawl-harness` `i-010f195f1798b40ad` — **stopped** since its 2026-06-29 launch.
- `orion-crawl-catalog` (DynamoDB, its output) — **NotFound**; positive control `opal-news-articles`
  → ACTIVE on the same probe shape.
- `opal-crawl-catalog` (S3, declared `main.tf:41`) — **404**; positive control `opal-data-assets` → 200.
- `dc2-test1-offpeak-harness` rule — applied but **DISABLED**.
- Recon-scope caveat SUPERSEDED by the Andrew ruling above; the DC-1/DC-2 TOs it rested on are
  among the 8 frozen orphans from dead COO seats.

## Legs
| # | Leg | Status |
|---|---|---|
| 1 | ledger opened | **DONE** |
| 2 | `terraform init` (stack was uninitialized) | **DONE** |
| 3 | `plan -destroy` reviewed -- **16 to destroy, EXACTLY the manifest, nothing outside it** | **DONE** |
| 4 | apply via `.tools/safe-apply.sh` (Rule 18) -- **Apply complete: 0 added, 0 changed, 16 destroyed** | **DONE** |
| 5 | **LIVE-PLANE verify** (not the apply's self-report): instance `i-010f195f1798b40ad` = **terminated**; rule `dc2-test1-offpeak-harness` = **ResourceNotFoundException**; `dc1-crawl-run` SSM docs = **0**; positive control `news-api-100pm` still **ENABLED** so the probe discriminates | **DONE** |
| 6 | **LEG 2 (C-6) -- MANDATORY, and it became acute:** post-destroy `plan` read **20 to add** (all resources gone, all still declared = the worst form of the resurrection hazard). Removed all 5 tracked TF sources + 7 `tfplan.*` artifacts (6 stale G1 + my own) | **DONE** |
| 7 | ledger **CLOSED 2026-07-30 ~20:2xZ** -- every leg finished in-session, nothing stranded | **DONE** |

## Expected destroy manifest (enumerated BEFORE, not after)
`aws_instance.crawl` · `aws_security_group.crawl` · `aws_iam_role.crawl` + policy +
`aws_iam_instance_profile.crawl` + SSM managed-policy attachment · 4 SSM documents
(`dc1_crawl_run`, `dc2_parker_run`, `dc2_crawl_run`, `dc2_test1_orchestrator`) ·
`aws_iam_role.dc2_orchestrator` + policy · `aws_iam_role.dc2_eventbridge_invoke` + policy ·
`aws_cloudwatch_event_rule.dc2_test1_offpeak` + target · `aws_s3_bucket.catalog` (+ PAB, versioning,
SSE) — the bucket is already absent, expect a state-only removal.

**STOP-AND-REPORT if the plan shows anything outside this manifest.**

## CLOSED — outcome

**16 resources destroyed, verified on the live plane, and the declaration removed in the same
session.** The only surviving artifact is the now-empty S3 state object `crawl-harness/tfstate` and
a stray `org/` telemetry dir left by a previous agent run (not mine, not in scope, left untouched).

**The lesson this leg produced, worth carrying:** a destroy makes the resurrection hazard WORSE
before it makes it better. Between the apply and the source removal, `terraform plan` read
**20 to add** — the stack was primed to rebuild the entire crawl estate, including the EC2 box,
on the next apply by anyone. **A destroy without its second leg is more dangerous than no destroy
at all**, because the resources are gone (so nobody is watching them) while the declaration is
fully armed. Leg 2 is not cleanup; it is the other half of the delete.
