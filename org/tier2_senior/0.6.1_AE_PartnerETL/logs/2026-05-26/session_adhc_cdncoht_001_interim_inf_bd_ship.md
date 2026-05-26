# ADHC_CDNCOHT.001-INTERIM — INF + BD post-chain CF invalidation ship

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, COORDINATE
**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-26
**TO:** ADHC_CDNCOHT.001-INTERIM
**PRD:** docs/architecture/ADHC_CDNCOHT.md v0.1 (commit `1a61f61c3`)

---

## Summary

Shipped Layer-2 immediate fix for the 2026-05-14 ~19:4XZ 18hr CDN-staleness anchor (RD 0.4.2 NNA bell-curve "Analytics data unavailable" symptom; `x-cache: Hit ... age=64908s` on freshly-emitted platinum artifact). Added `aws cloudfront create-invalidation` post-chain hook to both INF + BD gold-chain dispatchers, scoped to portal-auth distribution `EVTSA9VEHNZVH`, path-scoped to `/api/scoped/advisor-intelligence/*`. Failure → WARN, chain continues (AC5 — invalidation MUST NOT introduce chain-failure regression class).

Structural class-eliminator is TO-001 (L@E success-path Cache-Control injection, AE 0.7 lane, post-AC9). This interim ships independently per PRD §4 Phase 2 + AC9-independent gating.

## Ships

| Pipeline | Commit | Tag | Apply | S3 dispatcher upload | Smoke invalidation |
|---|---|---|---|---|---|
| INF | `b00e2733e` | `inf-pipeline-v1.7.67` | 1 add 0 change 0 destroy; 0-diff post-apply ✓ | `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh` (70.9 KiB) | `I9SL0UBI5EL0HDQJY5GYFTBZ11` @ 2026-05-26T14:03:43.534Z |
| BD | `053bba6f7` | `bd-v2.24.9` | 1 add 0 change 0 destroy; 0-diff post-apply ✓ | `s3://opal-data-bd/code/gold/gold_dispatch.sh` (51.1 KiB) | `I7UM4P5I13VU9QL1H1307HCIXD` @ 2026-05-26T14:09:10.835Z |

Record-deploy commits: `731c62322` (INF CHANGELOG) + `0a5a85140` (BD CHANGELOG).

## Implementation pattern

Both pipelines use the same shape:

1. **IAM addition:** `aws_iam_role_policy.{pipeline}_cloudfront_invalidate` on the dispatcher EC2 instance role (NOT a Lambda role — see "Tooling gap" below). Sid `InvalidatePortalAuthCacheOnPlatinumEmit`, Action `cloudfront:CreateInvalidation`, Resource `arn:aws:cloudfront::${local.account_id}:distribution/EVTSA9VEHNZVH`. Distribution-scoped, single action, single resource — minimum-privilege.

2. **Dispatcher hook:** post-sentinel block firing only on `MODE=chain && DRY_RUN=0 && chain_exit==0` (and `TARGET in {full,incremental}` for orion). Path-scoped to `/api/scoped/advisor-intelligence/*` (matches PRD §6 example; covers the four shared-advisor-router-routed CF behaviors #2/#3/#4/#12 per `comp-routes behaviors`). Env overrides `CDNCOHT_DIST_ID` + `CDNCOHT_PATHS` for ad-hoc operator use. Failure captured via `|| _cdncoht_rc=$?` pattern → WARN log; chain `exit "$chain_exit"` at tail unchanged.

3. **Insertion point per dispatcher:**
   - `orion-gold-dispatch.sh`: after pipeline-complete sentinel write block (~line 1367), before ChainFailed CloudWatch metric block
   - `gold_dispatch.sh`: after EventBridge `emit_chain_complete 0` (~line 1148), before WP-10b recon harness

## Empirical verification

- IAM attachment confirmed via `aws iam get-role-policy` on both `inf-gold-layer-ec2-role` and `bd-exporter-ec2-role` — policies live, JSON matches authored Terraform
- Both smoke invalidations accepted by CloudFront API — confirms distribution-id valid, path pattern accepted, permission chain works at caller level
- AC1 end-to-end (EC2-role-side firing): pending next scheduled gold-chain run (daily cron); dispatcher code paths exercised + uploaded to S3 ahead of next run
- AC2 (portal `age<60s`): pending next chain run + portal pull anchor against 2026-05-14 NNA bell curve surface
- AC3 (24h regression soak): passive monitoring; chain-success-rate post-ship to be sampled

## Compiler Tools

| Tool | Use | Result |
|---|---|---|
| `comp-routes behaviors` | Enumerate CloudFront behaviors carrying shared-advisor-router origin-request to confirm path-scoping target | Behaviors #2/#3/#4/#12 (`/api/scoped/advisor-intelligence/{artifacts,entities,*.json}`) route via shared-advisor-router to S3-opal-data-bd origin; `/api/scoped/advisor-intelligence/*` covers all four |
| Direct grep on terraform iam.tf | Locate EC2 dispatcher roles needing `cloudfront:CreateInvalidation` | INF: `inf_gold_layer` (used by inf-gold-layer-runner EC2); BD: `bd_exporter` (used by bd-gold-layer-runner PROD + bd-gold-qa-runner QA per existing role doc); existing `cloudfront:CreateInvalidation` grants were on Lambda roles only |
| `bash -n` syntax check | Validate dispatcher edits before commit | Both dispatchers SYNTAX OK |
| `.tools/terraform.exe plan` | Pre-apply plan + post-apply 0-diff verify | INF: 1 add 0 change 0 destroy → 0-diff. BD: same shape → 0-diff |
| `.tools/safe-apply.sh` | HALTGT-gated apply per CLAUDE.md Rule 18 | Both applies passed HALTGT (no STOP-class messages pending); resources created successfully |
| `aws iam get-role-policy` | Post-apply IAM verification | Both policies confirmed live on respective EC2 roles |
| `aws cloudfront create-invalidation` | Smoke-test of distribution-id + path pattern + permission chain | Both invalidations accepted (InProgress) |
| `.tools/safe-commit.sh` | Index-contamination guard + author-scoped commit | Both commits clean post `git reset HEAD --` on concurrent-agent-staged files (TO file from COO + MSTR mstr-spawn SKILL.md) |

**`comp-iam service` could NOT be used** — it covers Lambda functions, not EC2 instance roles. The CLAUDE.md compiler-tools trigger table assumes Lambda boto3-call IAM coverage; EC2 dispatcher-side IAM is a tooling-coverage gap. Surfaced to ws COO (turn 3 ACK acknowledged); banked as `comp-iam` extension candidate post this TO close. Did NOT block dispatch — direct terraform grep + role-to-EC2 cross-ref is the workaround pattern.

## Cross-domain coordination

Both dispatchers share the same portal-auth CF distribution (`EVTSA9VEHNZVH`) and same path pattern; invalidations are idempotent + non-conflicting across chains. ADHC_LEDGEH (origin error envelope; SHIPPED `48977e269`) is orthogonal to this dispatcher-side fix — TO-001 (L@E success-path Cache-Control extension, AE 0.7 lane) is the structural Layer-2 follow-on. No conflict; CDNCOHT TO-001-INTERIM ships independently.

## Authority chain + dispatch

- ws COO `2.0.0_SA_COO` dispatched TO-001-INTERIM 2026-05-26T13:54Z via /drive #93 paired GO MCP (XXX.md Author+GO discipline). COO ACK'd parallel pre-work + INF-first plan via crossed-in-transit at ~13:57Z. COO RAVC2-ACCEPT-PARTIAL on INF chain 2026-05-26 ~14:06Z.
- ws CTO `1.0.0_SA_CTO` authored PRD `1a61f61c3` 2026-05-26 ~13:48Z via /ws-charter cycle #26; no architectural questions surfaced during execution (PRD §6 scope unambiguous).
- MSTR `0.0.0_AB_MSTR` /mstr-spawn fulfillment of ws COO /allocation v0.1 P1 ask 2026-05-26T13:46Z; spawn-with-direction first-message hint baked in.
- AE 0.7 PURE STANDBY per LD-0097 §B AC9-quiet-hold; AC9-independent fork for this INTERIM authorized me to ship without AE 0.7 coordination.

## Bookkeeping

- TO `<status>` left at `pending` (was already pending in dispatched file); will flip to `complete` post RAVC2-ACCEPT-FULL closure signal from COO.
- Post-deploy monitoring banked at COO side per RAVC2-ACCEPT-PARTIAL message: AC1 end-to-end + AC2 portal-pull + AC3 24h regression soak.

## Files changed

```
infra/aws/terraform/inf-pipeline/iam.tf            +24
data/orion/scripts/gold/orion-gold-dispatch.sh     +37
infra/aws/terraform/bd-pipeline/iam.tf             +25
data/black_diamond/scripts/gold/gold_dispatch.sh   +33
infra/aws/lambda/ci/lambda-source-map.json         (CHANGELOG record-deploy)
infra/aws/terraform/{inf,bd}-pipeline/CHANGELOG.json (CHANGELOG record-deploy)
```
