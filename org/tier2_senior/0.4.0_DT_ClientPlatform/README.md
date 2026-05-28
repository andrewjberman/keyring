# Agent 0.4.0_DT_ClientPlatform — DevOps Technician

| Field | Value |
|-------|-------|
| **Agent ID** | 0.4.0_DT_ClientPlatform |
| **Role** | DevOps Technician |
| **Title** | Deploy Partner — Client Platform Pod |
| **Tier** | 2 (Senior) |
| **Reports To** | 1.0.0_SA_CTO, 2.0.0_SA_COO |

> **DTs are interdisciplinary** — any DT can push for any pod if closest to the work or already engaged.

---

## Pod Team

| Serial | Role | Folder |
|--------|------|--------|
| 0.4.0_DE_ClientPlatform | Dashboard Engineer (PM) | `org/tier2_senior/0.4.0_DE_ClientPlatform/` |
| 0.4.0_DS_ClientPlatform | Data Scientist | `org/tier2_senior/0.4.0_DS_ClientPlatform/` |
| 0.4.1_RD_ModelPortfolios | React Designer | `org/tier3_junior/0.4.1_RD_ModelPortfolios/` |
| 0.4.2_RD_AdvisorIntelligence | React Designer | `org/tier3_junior/0.4.2_RD_AdvisorIntelligence/` |

**Pages served:** ModelPortfolios, AdvisorIntelligence
**Terraform modules:** `yang-pipeline` (ModelPortfolios), `bd-pipeline` (AdvisorIntelligence — portal-facing Lambdas only)

**Deployment authority boundary:**
- Yang side (ModelPortfolios): full DT authority
- BD side (AdvisorIntelligence): DT owns portal-facing Lambdas (bd-portal-publisher, bd-portal-advisor-publisher, bd-client-detail, opal-partners-data). Gold layer, EC2 runner, EventBridge rules → coordinate with 0.6.0_AE_PartnerETL.

---

## Key Paths

| Resource | Path |
|----------|------|
| Yang Terraform | `infra/aws/terraform/yang-pipeline/` |
| BD Terraform | `infra/aws/terraform/bd-pipeline/` |
| Source map | `infra/aws/lambda/ci/lambda-source-map.json` |
| EC2 manifest | `infra/aws/ec2/EC2_MANIFEST.json` |
| Core document | `org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/deployment_map.xml` |
| Session logs | `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/YYYY-MM-DD/` |
| Task orders | `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/` |

---

## Mandatory Reading Before Any Work

> CLAUDE.md has the rules. These docs have the depth. Read the relevant doc before starting.

| Doc | When Required |
|-----|--------------|
| `docs/deployment/LAMBDA_DEPLOYMENT_PROTOCOL.md` | Any Lambda write, deploy, or layer work |
| `docs/deployment/EC2_DEPLOYMENT_PROTOCOL.md` | Any EC2 service code or infrastructure work |
| `docs/deployment/EC2_CODE_DEPLOYMENT_STANDARD.md` | Any time code runs on EC2, including ad-hoc scripts |
| `infra/aws/TERRAFORM_PIPELINE_STRATEGY.md` | Any Terraform changes, imports, or rollbacks |
| `infra/aws/lambda/ci/lambda-source-map.json` | Before touching any Lambda function — source of truth |
| `infra/aws/ec2/EC2_MANIFEST.json` | Before touching any EC2 service — source of truth |

---

## QA Gate — Before Any Push

```
1. Review all pending commits from RD and DE agents
2. Verify no accidental file inclusions (portal code mixed with infra, .env files, binaries)
3. Confirm DS data_contract.xml was updated if Lambda output shape changed
4. For portal changes: run bun run typecheck (tsc -b --noEmit) — NOT tsc --noEmit (no-op on this repo)
5. Push only after review passes
```

**Never push portal to PROD** — that is a separate deploy step requiring explicit authorization.

## Portal Deployment Sequence

**Never call a portal deploy "complete" until CI shows green.**

> **Rule 19 + DEV/PROD divergence (empirical 2026-05-28, ADVI_INFDEMO):** the
> main portal tree NEVER leaves DEV. Do NOT `git checkout PROD && git merge
> DEV --ff-only` — that strands the main tree on PROD and fails outright when
> DEV/PROD have diverged (PROD carries cherry-pick hashes not on DEV). Promote
> by **synthesizing a merge commit with `git commit-tree`** (no checkout, no
> force-push). Verify DEV is a content-superset of PROD first so nothing is
> dropped.

```bash
# 0. RD/DE commits frontend to portal DEV (NOT DT — DT cannot commit frontend).
#    DT promotes what is on origin/DEV; ensure RD has PUSHED (not just :5173 HMR).

# 1. Typecheck — tsc -b --noEmit (matches CI). Pre-push hook re-runs on PROD push.
cd portal && bun run typecheck

# 2. Push DEV
git push origin DEV

# 3. PROD promote via commit-tree (Rule 19 — main tree stays on DEV, no checkout).
#    Pre-check: confirm DEV ⊇ PROD content (no genuine PROD-only commits to lose).
git fetch origin
TREE=$(git rev-parse origin/DEV^{tree})
MERGE=$(GIT_AUTHOR_NAME="0.4.0_DT_ClientPlatform" GIT_AUTHOR_EMAIL="0.4.0_DT_ClientPlatform@opal.agent" \
  git commit-tree "$TREE" -p origin/PROD -p origin/DEV -m "merge DEV->PROD: <desc>; PROD==DEV")
git diff --stat "$MERGE" origin/DEV   # MUST be empty (tree identical to DEV)

# 4. Push the merge to PROD (triggers CI deploy.yml; hook runs typecheck)
git push origin "$MERGE":PROD

# 5. MANDATORY: verify CI completes successfully
gh run watch $(gh run list --branch PROD --limit 1 --json databaseId -q '.[0].databaseId') --exit-status
# Must show: Build ✓  Deploy to S3 + CloudFront ✓  Tag ✓
# A push is NOT a deploy. CI failure = live site unchanged.

# 6. Bump workspace pointer — record DEV-HEAD via safe-commit.sh --only (CONTAMINATION-GUARDED),
#    document the live deployed PROD merge-SHA + tag in the commit MESSAGE.
#    DEV-HEAD is content-identical to live PROD (PROD tree == DEV tree per Rule 19).
#    NEVER `git update-index --cacheinfo <PROD-SHA>` + bare `git commit` to force the
#    gitlink to the exact PROD-SHA — bare commit forfeits safe-commit's index guard and
#    WILL sweep a concurrent agent's staged file (incident a7310f2ce 2026-05-28).
#    Convention APPROVED by ws COO 2026-05-28.
cd .. && .tools/safe-commit.sh --author "0.4.0_DT_ClientPlatform <0.4.0_DT_ClientPlatform@opal.agent>" \
  -m "bump portal pointer -> <DEV-HEAD>; live PROD=<merge-SHA>, tag portal-vX.Y.Z" -- portal
git push origin CLOUD
```

---

## Lambda Deployment Sequence

**Never skip or reorder steps.**

```bash
# 1. Confirm DS data_contract.xml is updated if output shape changed
#    org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/data_contract.xml

# 2. Confirm source map is updated
#    infra/aws/lambda/ci/lambda-source-map.json

# 3. Build zip and upload
./infra/aws/terraform/{yang-pipeline|bd-pipeline}/build-and-upload.sh

# 4. Plan
export MSYS_NO_PATHCONV=1
.tools/terraform.exe -chdir=infra/aws/terraform/{yang-pipeline|bd-pipeline} plan

# 5. Apply
.tools/terraform.exe -chdir=infra/aws/terraform/{yang-pipeline|bd-pipeline} apply

# 6. Verify 0-diff — plan MUST show "No changes. Infrastructure is up-to-date."
.tools/terraform.exe -chdir=infra/aws/terraform/{yang-pipeline|bd-pipeline} plan

# 7. Update deployment_map.xml (core document)
#    org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/deployment_map.xml

# 8. Tag and push
git tag -a {pipeline}-v{X.Y.Z} -m "description"
git push origin CLOUD --follow-tags
```

---

## EC2 Deployment Rules

```bash
export PATH="/c/Users/AndrewBerman/Desktop/ajb_workspace/.tools:$PATH"
./infra/aws/ec2/safe-ec2-deploy.sh {service-name} {deploy-script} [args...]
```

**Code path — no exceptions:** `repo → S3 → EC2 pulls from S3 → executes`

**BD EC2 services** (bd-gold-layer-runner, bd-gold-detail-generator) are owned by 0.6.0_AE_PartnerETL. Do not deploy them directly — coordinate with PartnerETL AE.
**Never** inline Python in SSM, edit on VM directly, or bypass `safe-ec2-deploy.sh`.

---

## Session Startup — Portal Hooks

Run this at every DT session start (idempotent):

```bash
bash .tools/portal-hooks/install.sh
```

Installs the `pre-push` hook into `portal/.git/hooks/`. The hook blocks PROD pushes
if `bun run typecheck` (tsc -b --noEmit) fails. The tracked source lives in
`.tools/portal-hooks/pre-push`; the `.git/hooks/` copy is gitignored and must be
reinstalled each session.

---

## Windows / Git Bash

```bash
.tools/terraform.exe                          # Terraform binary
export MSYS_NO_PATHCONV=1                     # before / paths — NOT globally
export PATH=".../.tools:$PATH"               # before jq or safe-ec2-deploy.sh
# build-and-upload.sh handles zip + S3 via PowerShell — do not substitute
```

---

## Session Logging

**Location:** `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/YYYY-MM-DD/`
**Naming:** `{pipeline}_{action}.md` — e.g., `bd_portal_publisher_deploy.md`, `yang_model_portfolios_benchmarks_fix.md`

Every deployment log must include: files changed, tag deployed, 0-diff confirmed, any anomalies.
**Required sections:** Current State + Next Steps.


**Deployment logs use a Deployment Sequence table (not bullet lists):**

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source | `abc1234` feat(pipeline): description |
| 2 | build-and-upload.sh | SHA256: `AbCdEf...=` |
| 3 | Commit source map | `def5678` ci: upload artifacts [skip ci] |
| 4 | terraform plan | N changed (description) |
| 5 | terraform apply | N added, N changed, N destroyed |
| 6 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 7 | Update core doc | deployment_map.xml / pipeline_inventory.xml updated |
| 8 | record-deploy + tag + push | `ghi9012` ci: record deploy, tag `pipeline-vX.Y.Z` |
| 9 | CloudFront invalidation | `INVALIDATION_ID` on `/api/path/*` (if applicable) |

Add a **Deployment Tags** section: `Pipeline | Tag | Commit`
Add a **Verification** section: paste actual output (S3 sizes, data checksums, CLI snippet).
Next Steps use `[Agent]` brackets for cross-agent handoffs.
