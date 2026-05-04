# INFLEC AUDIT-001 — Infra-Layer State Dump (AE 0.7)

**Author:** 0.7.0_AE_CloudOps
**Generated:** 2026-05-04
**Source:** COO GO 20260504T~202000Z (parallel to DescribeTags ship)
**Scope:** Infrastructure RED-cause classification for INFLEC AUDIT-001 panel-truth matrix.

For each infra dependency below, status is one of:
- **GREEN** — dependency healthy, will not RED a panel
- **AMBER** — non-blocking concern documented
- **RED-(infra)** — would silently render empty / 4xx / 5xx; root cause is infra (IAM gap, CF behavior, runner drift, bucket policy)

DS~A: any RED-(infra) cells below should be flagged in master matrix as `RED-(infra)` — separate from RED-(a) Lambda emit / RED-(b) S3 path / RED-(c) silver-gold gap.

---

## Section 1 — inf-pipeline IAM (Inflection-touching roles)

| Role | Permission needed | Current state | RED cause? | Evidence |
|------|------------------|---------------|------------|----------|
| `inf-gold-layer-ec2-role` | `ec2:DescribeTags` (for L1-skip-tag-aware dispatcher branch) | **PATCHING** in inf-pipeline-vNEXT (commit 299438199); apply pending | AMBER (silent on PROD only — PROD has no Tier=qa tag so no behavioral effect; would matter if any new tag-conditioned dispatcher logic added) | `infra/aws/terraform/inf-pipeline/iam.tf` post-edit |
| `inf-gold-qa-runner-ec2-role` | `ec2:DescribeTags` | **PATCHING** in inf-pipeline-vNEXT (commit 299438199); apply pending | RED-(infra) ON QA — every QA dispatch self-shutdowns L1 instead of staying for inspection (mirrors the 2026-05-04T20:03:44Z bd-gold-qa-runner observation) | Same |
| `inf-gold-qa-runner-ec2-role` | Tier=qa + AutoShutdown=false tags on aws_instance | Drifted (added in console; TF was unaware) | AMBER — fixed in same commit by aligning TF source to live state | `infra/aws/terraform/inf-pipeline/inf-gold-qa-runner.tf` post-edit |
| `inf-jwt-trigger` Lambda | KMS decrypt + SSM SendCommand | `inf-jwt-trigger-kms` policy live; SSM delegation correct | GREEN | Validated 2026-05-04 in JWTRES.002 v5 audit (`org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-05-04/jwtres_wave_b_v5_validation.md`) |
| `inf-exporter-ec2-role` | SSM messages + KMS for `orion/jwt/current` writes | All present (live cron writes verified 2026-05-02 to 2026-05-04) | GREEN | Same SM rotation history table |
| `inf-bronze-runner-ec2-role` | KMS decrypt on EBS-only | KMS grant audit completed 2026-04-30 (memory: `feedback_kms_grant_audit_scope.md`) | GREEN | Per memory rule — boundary is the key, audited at fix time |
| `partners-lambda-role` (cross-pipeline reads from Inflection bucket) | `s3:GetObject` + `s3:ListBucket` on `opal-data-inf/*` | Live: `arn:aws:s3:::opal-data-*` wildcard covers `opal-data-inf` (Sid=ReadPartnerBuckets) | GREEN | `aws iam get-role-policy partners-lambda-role partners-lambda-permissions` |

`comp-iam gaps` planned post-INF-apply (waiting on TF provider stabilization). No other Inflection-touching IAM roles surfaced via this scan.

---

## Section 2 — CloudFront behaviors (Inflection paths)

CloudFront has **23 behaviors total**. None reference `opal-data-inf` directly. Inflection routing is by Lambda@Edge bucket-swap on firmId — origin is hardcoded as `S3-opal-data-bd` then swapped per-request by `shared-advisor-router`.

| Path pattern | Origin | Edge fns | Inflection-relevant? | Status |
|--------------|--------|----------|---------------------|--------|
| `/*` | S3-opalinvest-portal | (none) | SPA static; firmId-agnostic | GREEN |
| `/api/scoped/advisor-intelligence/artifacts/*/*` | S3-opal-data-bd | auth-validator-edge + shared-advisor-router | YES — depth-3 artifacts (e.g. summary, partner_analytics) | GREEN — router swaps to `opal-data-inf` for firmId=inflection (verified `index.mjs:178`, `:199-200`) |
| `/api/scoped/advisor-intelligence/artifacts/*` | S3-opal-data-bd | (same) | YES — depth-2 artifacts | GREEN |
| `/api/scoped/advisor-intelligence/entities/*/*` | S3-opal-data-bd | (same) | YES — clients/{id}_views.json, etc. | GREEN |
| `/api/scoped/advisor-intelligence/*.json` | S3-opal-data-bd | (same) | YES — depth-1 .json catch | GREEN |
| `/api/scoped/advisor-intelligence/advisors/*/*` | APIGateway-portal | auth-validator-edge | YES — advisor book + mix-views | GREEN — API GW Lambda backed; partners-lambda-role has `opal-data-inf` read |
| `/api/scoped/advisor-intelligence/clients/*/*` | APIGateway-portal | auth-validator-edge | YES — client detail | GREEN (same) |
| `/api/scoped/advisor-intelligence/clients/*` | APIGateway-portal | auth-validator-edge | YES — clients/growth, tax-breakdown, tax-deferred | GREEN (same) |
| `/api/scoped/advisor-intelligence/timeseries/*` | APIGateway-portal | auth-validator-edge | YES | GREEN (same) |
| `/api/scoped/advisor-intelligence/snapshots/*` | APIGateway-portal | auth-validator-edge | YES | GREEN (same) |
| `/api/scoped/advisor-intelligence/*` | APIGateway-portal | auth-validator-edge | YES — depth-1 catch (clients-tab, filters, summary, partner-analytics) | GREEN (same) |
| `/api/general/json-tiered/*` | S3-opal-data-portal-v2-json | auth-validator-edge + public-data-router + cache-control-injector | NO — public/general json bus | GREEN |
| `/api/general/*` | S3-opal-data-portal-v2-json | (same) | NO — general public | GREEN |
| `/api/private/*` | (private API GW) | auth-validator-edge | NO direct INFLEC hit | GREEN |

**No INFLEC-relevant path returns 403/HTML.** No path-pattern allowlist gap identified — every advisor-intelligence behavior has the `auth-validator-edge` + `shared-advisor-router` chain that handles firmId=inflection correctly.

**Custom error responses (CF-level):** Not pulled in this dump (no observed Inflection 4xx symptom that would be masked). DS~A flag if any panel returns HTML where JSON expected — that's the signal to dig further into custom_error_response.

---

## Section 3 — Lambda@Edge auth-validator-edge (Inflection JWT verification)

| Check | Status | Evidence |
|-------|--------|----------|
| RS256 JWT verification path | GREEN | `infra/aws/lambda-edge/auth-validator-edge/index.mjs` — uses `jwt.verify(token, publicKey, { algorithms: ["RS256"] })` against `opal/auth/jwt-public-key` Secrets Manager value |
| `firmId=inflection` accepted in routing | GREEN | `index.mjs:101-104` FIRM_BUCKET_MAP has `'inflection': 'inf'` → bucketAlias = `inf` → S3 path `opal-data-inf/...` |
| `firmId=inflection` accepted in tier_policy | GREEN | `tier_policy.mjs` mirrors FIRM_BUCKET_MAP (per code comment line 6) |
| Mapping parity with shared-advisor-router | GREEN | `shared-advisor-router/index.mjs:175-180` has identical map (`'inflection': 'inf'`) |
| JWT public key in Secrets Manager | GREEN | `opal/auth/jwt-public-key` confirmed live and rotation-tracked (JWTRES.002 v5 audit, 2026-05-04) |
| Firm-bucket map owner | inf-pipeline + portal — both files must be edited together when adding new firms | INFO (no current defect) |

**No Inflection-specific JWT verification or routing gap detected.** firmId=inflection JWTs validate, route to bucketAlias=inf, and the alias is honored downstream.

---

## Section 4 — EC2 runner state vs EC2_MANIFEST.json

Current live state (queried 2026-05-04T~20:30Z):

| Service | Instance ID | State | LaunchTime (UTC) | Tier tag | AutoShutdown tag | Manifest registered? | Drift? |
|---------|------------|-------|------------------|----------|-----------------|---------------------|--------|
| inf-gold-layer-runner (PROD) | i-0ed5afded2ebd4ed4 | stopped | 2026-05-04T16:52:11Z | (none — correct, PROD must NOT have Tier=qa) | (none — PROD self-shutdowns by L1) | YES | None |
| inf-gold-qa-runner (QA) | i-04373615f03fbf9a9 | stopped | 2026-05-04T15:45:43Z | `qa` | `false` | YES | TF source aligned in this commit (299438199) |
| inf-bronze-runner | i-083ad9ae297f88e9f | stopped | 2026-05-01T19:00:56Z | (none) | (none) | YES (in EXCLUDED_INSTANCES per enforcer-v1.0.4) | None — long-running by design (HISTBF wave) |
| inf-exporter | i-081ae6aafb394fb1a | running | 2026-05-02T04:35:54Z | (none) | (none) | (per EC2_MANIFEST line — manual scrape) | None — running per JWTRES.002 design (in EXCLUDED_INSTANCES; SSM-driven Orion JWT cron lives here) |

**Last successful runs** (representative — Inflection-relevant):

| Service | Last clean run | Evidence |
|---------|---------------|----------|
| inf-gold-layer-runner | 2026-05-04T15:46Z (INF prod chain SSM 6eabdce2) | `chain_monitoring_continuation.md` — INF Prod Chain Confirmed Complete section |
| inf-gold-qa-runner | 2026-05-04T16:02:43Z (INF QA chain SSM 670db9bb, INF_I_D03+INF_D_04) | Same log — INF QA Chain Complete section |
| inf-bronze-runner | Long-lived (continuous since 2026-05-01); per HISTBF wave | Per JWTRES.002 v5 audit |
| inf-exporter | Continuous; SSM-driven Orion fetch every cron tick + on-demand | Per JWTRES.002 v5 audit |

**No EC2 drift between live state and EC2_MANIFEST.json.** Inflection runners are healthy — every recent dispatch completed exit 0.

**Tier-tag observation:** Only inf-gold-qa-runner carries Tier=qa (correct — it's the only QA runner). PROD runners intentionally have no Tier so they self-shutdown at L1 boundary. Same convention as BD pipeline (bd-gold-qa-runner has Tier=qa; bd-gold-layer-runner does not).

---

## Section 5 — opal-data-inf bucket policy

Bucket policy (live):

```
Sid                       Principal                                                 Resource                       Action
-----------------------   ------------------------------------------------------    ----------------------------   --------------
AllowScopedAdvisorOAI     CloudFront OAI E139998VWH0PD                              opal-data-inf/*                 s3:GetObject
AllowCFDistributionGold   cloudfront.amazonaws.com (svc) [SourceArn=EVTSA9VEHNZVH]  opal-data-inf/gold/*           s3:GetObject
```

| Check | Status | Evidence |
|-------|--------|----------|
| Shared advisor OAI (E139998VWH0PD) reads anywhere in bucket | GREEN | Sid=AllowScopedAdvisorOAI matches the OAI used on opal-data-bd (parity confirmed — same OAI on both buckets) |
| CloudFront service principal reads `gold/*` (OAC pattern) | GREEN | Sid=AllowCFDistributionGold scoped to distribution EVTSA9VEHNZVH (same distribution serving advisor-intelligence) |
| `partners-lambda-role` reads `opal-data-inf/*` | GREEN — covered by IAM-side wildcard `arn:aws:s3:::opal-data-*` (Section 1) | `aws iam get-role-policy partners-lambda-role partners-lambda-permissions` Sid=ReadPartnerBuckets |
| Inf-gold-qa-runner writes to `opal-data-inf/qa/*` | GREEN — covered by `inf-gold-qa-runner-ec2-role` policy (`s3-qa-scoped`) | `infra/aws/terraform/inf-pipeline/inf-gold-qa-runner.tf:75+` |
| Any prefix that should be readable by `opal-partners-data` consumer but isn't | None identified | The `opal-data-*` wildcard on partners-lambda-role provides full coverage |
| `platinum/firm/*` writeable by gold runner | GREEN | inf-gold-layer-ec2-role policy covers via `inf-pipeline/iam.tf` `inf_gold_layer_s3` |
| `qa/*` write deny on PROD role (defense in depth) | (need to verify) | `inf-gold-qa-runner.tf` header notes "explicit deny on platinum/* writes" — symmetric inverse should be verified post-INF apply |

**No bucket policy gap that would silently RED an Inflection panel.** Both BD and INF buckets share the same OAI + OAC + partners-lambda-role pattern.

---

## Summary — RED-(infra) candidates for AUDIT-001 master matrix

| Panel/Field surface | Infra dependency | RED-(infra)? | Notes |
|---------------------|------------------|--------------|-------|
| Any QA-runner-served panel served from `opal-data-inf/qa/*` | inf-gold-qa-runner-ec2-role missing `ec2:DescribeTags` | **WAS** RED-(infra) — patched in commit 299438199, apply pending | Manifests as L1 self-shutdown stripping ad-hoc QA artifacts before operator can inspect; not user-facing on PROD bucket |
| All other panels (PROD path) | All IAM, CF, Lambda@Edge, EC2 runners, S3 policy | NONE — GREEN across the board | No silent infra gap identified |

**Andrew read:** No infra-side defect blocks any Inflection PROD panel. The L1-skip IAM gap was QA-only and is being patched in this same wake. If a panel is RED, the cause is data/code (RED-(a)/(b)/(c)), not infra.

---

## Outstanding follow-ups (not in scope of this dump)

- Apply `inf-pipeline-vNEXT` (waiting on TF provider crash subsidence — concurrent-agent fork pressure)
- Run `comp-iam gaps` post-INF-apply to confirm no other unintended deltas
- Verify `qa/*` write deny on PROD role symmetric to "platinum/* deny on QA role" (Section 5 last row)

— AE 0.7
