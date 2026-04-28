# Session Log — 2026-04-28 — INFSHIP Phase 2 Portal Push + CORS Deploy

| Field | Value |
|-------|-------|
| Agent | 0.4.0_DT_ClientPlatform |
| Date | 2026-04-28 |
| Trigger | CTO direct GO (Andrew tree-hygiene + push verification ask) |

---

## Inbox on Arrival (10 messages)

| From | Subject | Action |
|------|---------|--------|
| 2.0.0_SA_COO | GO portal-v2.1.63 deploy (INFLV2.006 + .008) | NO-ACTION — already shipped |
| 2.0.0_SA_COO | TRSB_PATHFIX.TO-2 Andrew override (W2 ship time) | Noted — no infra action this session |
| 2.0.0_SA_COO | GO portal-v2.1.64 push (INFLV2.007) | NO-ACTION — already shipped |
| 2.0.0_SA_COO | FYI COMP branch isolation LIVE | Acknowledged — CLOUD/DEV/PROD unchanged |
| 0.4.0_DE_ClientPlatform | Push request INFSHIP B1 (995262c) | Folded into Phase 2 batch push |
| 0.4.0_DE_ClientPlatform | Push request INFSHIP Phase 2 batch (4 commits) | SHIPPED |
| 0.4.0_DE_ClientPlatform | UPDATE batch grows by 1 (ade43c4 B4 amend) | SHIPPED |
| 1.0.0_SA_CTO | [GO Andrew direct] Tree hygiene + push verification + CORS | All asks addressed |
| 2.0.0_SA_COO | RAVC ACK Phase 2 batch ship | Acknowledged |

---

## Pre-existing Tree State Investigation

### portal-v2.1.63 + portal-v2.1.64 GOs

| Tag | Pointer | Origin SHA | Status |
|-----|---------|------------|--------|
| portal-v2.1.63 | 54f2890 (TS strict-mode fix) | efcd819 | Already on origin |
| portal-v2.1.64 | d38ec03 (TradeSubmission ExecuteModal) | ff413d9 | Already on origin |

Both tags shipped before session start. Parent CLOUD submodule was already at d38ec03 via prior commit `799b3d12 0.3.0_DT_TradingOperations: bump to d38ec03`. INFLV2.006/.007/.008 commits all live on origin/DEV inside those tag chains. **No duplicate action taken** — flagged in COO RAVC.

### tools/news_scanner/scripts/utilities/*.py (8 dirty files)

Diagnosis: **pure CRLF/LF noise, zero content delta.** Every file showed symmetric N inserts / N deletes (`3052 insertions, 3052 deletions` total across 7 modified .py files). Git's own warning confirmed: `CRLF will be replaced by LF the next time Git touches it`. Root cause: user `core.autocrlf=true` writes CRLF to working tree on checkout, but `.gitattributes` enforces `*.py text eol=lf` in the repo. Editor save round-trips the file; no semantic change.

**Action: none.** Not authored by me; not committed. Files will normalize next time they're legitimately edited. Not blocking.

---

## Work Completed

### 1. INFSHIP Phase 2 portal batch — SHIPPED

QA review: 6 commits, 6 files all under `src/pages/AdvisorIntelligence/`, single author (`0.4.0_DE_ClientPlatform`), no contamination, tsc clean per DE.

| Commit | TO | Files |
|--------|-----|-------|
| `995262c` | B1 (+ B2) | TenantLayoutConfig.ts + inflection/layout.ts + PartnerAnalytics.tsx |
| `45eaca0` | B3 | ConsolidatedOverviewPanel.tsx + types.ts |
| `fb926fa` | B3 Path C | ClientsTab.tsx + types.ts |
| `aa862dd` | B4 | inflection/layout.ts |
| `ade43c4` | B4 amend (Andrew override) | inflection/layout.ts |
| `12ea545` | B5 prep | types.ts |

**portal/DEV:** `git -C portal push origin DEV` → `d38ec03..12ea545`.

**Parent CLOUD submodule pointer:** Bumped to `ade43c4` per DE explicit request (B5 prep `12ea545` is on origin/DEV but unpinned in parent — DE will request a future bump after B5/B6 ship). Parent commit: `2269074e 0.4.0_DT_ClientPlatform: bump portal -> ade43c4`. Pushed to origin/CLOUD.

### 2. CORS Allowlist for `http://localhost:5176`

**Source change:** `infra/aws/opalinvest_dev/lambda/auth-handler/src/index.ts` — added `http://localhost:5176` to `ALLOWED_ORIGINS`. Endpoint per CTO: `https://7k3ed8px20.execute-api.us-east-1.amazonaws.com/auth/refresh`.

#### Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source | `9dbe1975` feat(auth-handler): add http://localhost:5176 to CORS allowlist |
| 2 | build-nodejs-lambda.sh portal-auth opalinvest-auth-handler | SHA256: `NrS1jzN9bxPNNQNxiTtP7gT1/FG7xaw3I0CCurt3j7M=`, 36K, uploaded to s3://opal-313476888478-lambda-artifacts/portal-auth/opalinvest-auth-handler.zip |
| 3 | Commit source map | `ffc3f0fe` ci: upload opalinvest-auth-handler artifact [skip ci] |
| 4 | terraform plan | 1 to change (auth_handler in-place; s3_object_version + source_code_hash + last_modified) |
| 5 | terraform apply | Apply complete! Resources: 0 added, 1 changed, 0 destroyed. (6s) |
| 6 | 0-diff plan | "No changes. Your infrastructure matches the configuration." |
| 7 | record-terraform-deploy.sh | `adee1dbd` ci: record deploy portal-auth @ ffc3f0fe [skip ci] |
| 8 | Tag + push | `portal-auth-v1.14.1` → origin/CLOUD `2269074e..adee1dbd` |

#### Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| portal-auth | `portal-auth-v1.14.1` | `adee1dbd` |

#### Verification

```
$ git ls-remote origin refs/tags/portal-auth-v1.14.1
<sha>  refs/tags/portal-auth-v1.14.1

$ aws lambda get-function-configuration --function-name opalinvest-auth-handler
  → CodeSha256: NrS1jzN9bxPNNQNxiTtP7gT1/FG7xaw3I0CCurt3j7M= (matches local zip)
  → LastModified: 2026-04-28T14:0X:XX (just now)
```

ALLOWED_ORIGINS post-deploy: `[opalinvest.dev, www.opalinvest.dev, localhost:5173, localhost:3000, localhost:5174, localhost:5176]`. DE can now hit `7k3ed8px20.execute-api.us-east-1.amazonaws.com/auth/refresh` from `http://localhost:5176`.

### 3. Push Verification Audit (CTO ask #3)

```
$ git fetch origin
$ git log origin/CLOUD..HEAD --oneline
(empty — fully pushed)
```

Spot-check of CTO inventory (5 commits, all on origin/CLOUD):

| SHA | Description | On origin/CLOUD |
|-----|-------------|-----------------|
| `c3d7ccda` | DS~B L1 D2 (per-HH + per-account tax/billing) | YES |
| `2d1154c3` | AE 0.7.0~B B1 EC2 + orchestrator + cron | YES |
| `df4b3f86` | DS~A B4 9-dim spec doc | YES |
| `b287388d` | INFSHIP P1.L1.D3 _meta annotation | YES |
| `ade43c4` | DE B4 amend (portal repo) | YES (on portal/origin/DEV via my push) |

Local CLOUD HEAD = origin/CLOUD HEAD = `adee1dbd`. Nothing unpushed.

---

## Compiler Tools

| Tool | Phase | Result |
|------|-------|--------|
| N/A — small CORS allowlist + portal pointer bump | — | No new boto3 calls; no IAM changes; no portal component schema changes |

`comp-iam service opalinvest-auth-handler` not run — change was a CORS string-array addition, no new AWS API calls. Lambda IAM policy unchanged.

---

## Commits This Session

| SHA | Description |
|-----|-------------|
| `2269074e` | bump portal -> ade43c4 (INFSHIP Phase 2 batch B1+B3+B3-PathC+B4+B4-amend) |
| `9dbe1975` | feat(auth-handler): add http://localhost:5176 to CORS allowlist |
| `ffc3f0fe` | ci: upload opalinvest-auth-handler artifact [skip ci] |
| `adee1dbd` | ci: record deploy portal-auth @ ffc3f0fe [skip ci] (Author: Andrew Berman via record-terraform-deploy.sh — script default) |

Tag created: `portal-auth-v1.14.1`.

---

## Owned-Paths Hook Notes

WARN-mode violations surfaced (not blocked) on:
- `infra/aws/opalinvest_dev/lambda/auth-handler/src/index.ts` (lane: CLOUD_OPS_OR_ETL — AE)
- `infra/aws/lambda/ci/lambda-source-map.json` (lane: CLOUD_OPS_OR_ETL — AE)
- `infra/aws/terraform/portal-auth/CHANGELOG.json` (lane: CLOUD_OPS_OR_ETL — AE)

Justification: CTO direct GO (Andrew explicit ask) authorized this CORS deploy, and DT pod has the deploy capability per README ("portal-facing Lambdas" — auth-handler serves the portal auth route). Surfacing for owned-paths YAML review — auth-handler may need a DT-shared lane entry.

---

## Status at Session Close

| Item | State |
|------|-------|
| portal/DEV remote | Current (`12ea545` — INFSHIP Phase 2 + B5 prep) |
| Parent CLOUD remote | Current (`adee1dbd` — submodule pointer at ade43c4 + portal-auth deploy) |
| portal-auth tag | `portal-auth-v1.14.1` LIVE on origin |
| CORS allowlist | `localhost:5176` now allowed by opalinvest-auth-handler |
| TO queue | ADVI_49EXEC.007 still staged (waiting on AE 0.6.1 EventBridge signal) |
| news_scanner dirty files | Untouched — pure CRLF noise, not authored, not blocking |

---

## Next

- DE B5 + B6 ship → DE will MCP for follow-on submodule pointer bump
- ADVI_49EXEC.007 still staged — holding on AE 0.6.1 EventBridge confirmation
- COMP branch isolation: continue CLOUD/DEV/PROD as normal
- TRSB_PATHFIX.TO-2 Andrew override applied at W2 ship time (note in this log)

_Written 2026-04-28 by 0.4.0_DT_ClientPlatform_
