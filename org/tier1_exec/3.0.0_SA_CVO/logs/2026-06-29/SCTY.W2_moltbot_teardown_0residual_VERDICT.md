# SCTY.W2 AWS-IAM-1 (Moltbot privesc-chain) Teardown — Independent 0-Residual VERDICT

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-06-29 | **For:** 0.7.0_AE_CloudOps~B (producer) + 1.0.0_SA_CTO (gate) · cc 2.0.0_SA_COO
**Verdict: SATISFIED — 0 active residual; AWS-IAM-1 privesc chain RETIRED; safety posture sound; loop CLOSED (independent CVO side).**

Verifier ≠ do-er: I re-ran every surface enumeration myself against LIVE AWS (acct `313476888478`),
not off AE's sweep table. Rail note: live `aws` is the correct ground-truth here — `comp-iam` parses
TF=DESIRED and cannot confirm LIVE deletion of a destructive teardown (rail-checked).

## 1. Active-surface sweep — INDEPENDENT re-run, all CLEAR
| Surface | My live query | Result |
|---|---|---|
| IAM roles `*oltbot*` | list-roles + `get-role MoltbotEC2Role` | `[]` ; **NoSuchEntity** (privesc-chain root gone) |
| IAM customer policies (Local) | list-policies --scope Local | `[]` (inline policy died with role) |
| IAM instance profiles | list-instance-profiles + `get-instance-profile MoltbotEC2Profile` | `[]` ; **NoSuchEntity** |
| EC2 instances (any state) | describe-instances Name tag | `[]` |
| Security groups | describe-security-groups + `sg-0e4cca6eb9743284b` | `[]` ; **InvalidGroup.NotFound** |
| Lambda functions | list-functions | `[]` |
| CodeBuild `moltbot-openclaw-build` | batch-get-projects | in **projectsNotFound** (gone) |
| Log group `/aws/codebuild/moltbot-openclaw-build` | describe-log-groups | `[]` |

**=> 0 active residual.** The `MoltbotEC2Role` that carried the dormant full-account-takeover chain
(`CreateRole/PutRolePolicy + PassRole->lambda + UpdateFunctionCode` on `Resource="*"`) no longer exists —
the finding is RETIRED, not merely mitigated.

## 2. Secrets — reversible recovery window CONFIRMED (not hard-deleted)
Both `github/moltbot-pat` + `opal/moltbot-anthropic-key` in scheduled-deletion state. Grounded the
recoverability precisely (initial field-label ambiguity resolved): `describe-secret` carries
`DeletedDate = 2026-06-29 13:15Z` (= schedule-delete REQUEST time, today); + the 30-day window =
permanent purge **2026-07-29** (arithmetic match to AE's "DeleteOn"). Secret MATERIAL is intact — both
`AWSCURRENT` + `AWSPREVIOUS` version stages present — so `restore-secret` recovers until 2026-07-29.
**Soft-delete, reversible by design.** ✓

## 3. Safety posture — HELD
- **Reversible-first ordering** (deploy ledger `20260629T1313Z`, CLOSED 7/7, every leg proof-carried):
  L1 git → **L2 profile detach+delete BEFORE L3 TF role-delete** (DeleteConflict guard correctly
  sequenced) → L4 directs → **L5 secrets WINDOW-delete (not hard)** → L6 git cleanup → L7 verify.
- **TOCTOU re-plan 0/0/3 + safe-apply HALTGT + post-apply 0-diff** (ledger L3 proof; `get-role`=NoSuchEntity).
- Destructive nature Andrew-cleared + CTO GATE-PASS'd. Nothing half-landed (ledger CLOSED, no stranded leg).
- Commits `0c5ead90c` / `a5c036ab6` / `d4bd61c49` all on origin/CLOUD; `MoltbotEC2Role` removed from
  `infra/aws/terraform/shared-infra/iam_legacy.tf` (intentional tombstone comment retained = good record,
  not a residual); dead ec2 dirs (`infra/aws/ec2/moltbot`, `infra/ec2/moltbot`) gone live.

## 4. Retained-out-of-scope — correctly retained
- `cost-anomaly-scanner` + `access-anomaly-scanner` lambdas PRESENT (functional, merely *reference*
  moltbot — correctly NOT moltbot-owned, out of scope). ✓
- `moltbot_alert.py` PRESENT (conservatively retained). ✓
- Historical docs PRESENT. ✓
- **`moltbot-safe-pull.py` PRESERVED in git history** — recoverable at `a5c036ab6~1` (also has its own
  commit `4cb0e2227`); the AF-1 injection-scanner template for SCTY.W1 is NOT lost. ✓

## Observations (non-blocking, P2 — surfaced not as residuals)
- **`moltbot_alert.py` ambiguity:** retained as "no live importer found, possibly a Lambda-layer member."
  This is a genuine open thread, not a 0-residual blocker: if it is NOT a layer member it is dead code to
  remove; if it IS, it is live and should be re-scoped/owned. Recommend AE confirm layer membership in a
  later pass and dispose accordingly. Correctly out of THIS teardown's scope.

## Compiler Tools
| Tool | Run | Result | Note |
|---|---|---|---|
| live `aws` (rail-checked) | independent 0-residual sweep: IAM/EC2/SG/Lambda/CodeBuild/logs/secrets enumeration + targeted get-role/get-instance-profile/describe-sg/describe-secret | PASS | the only ground-truth for live destructive-teardown residual; comp-iam=DESIRED-only can't confirm deletion |
| git (cat-file/log/grep) | commit existence on CLOUD + iam_legacy.tf removal + ec2-dir removal + safe-pull.py history-recoverability | PASS | confirmed 3 commits, TF tombstone, dirs gone, template preserved |

**What worked:** re-running the sweep independently (not reading AE's table) + grounding the secret
recovery-window arithmetic from raw `describe-secret` rather than the AE label — resolved an initial
field-semantic ambiguity (DeletedDate=request-time not purge-time) cleanly without a false flag.
**Gap:** none for AWS-IAM-1; one P2 thread (`moltbot_alert.py` layer membership) surfaced to AE.

## Blockers
None. Loop CLOSED from the independent CVO side.

— 3.0.0_SA_CVO
