# Deploy completion -- INF udf7ADVISOROF /Portfolio/Accounts roster pull

**Status:** COMPLETE + VERIFIED, INERT (bronze producer only) -- closed 2026-07-12T13:24Z
**Closed:** 2026-07-12T13:24Z

**Deploy:** inf-pipeline-v1.7.83 | **Owner:** 0.7.0_AE_CloudOps | **Completed:** 2026-07-12T13:24Z (in-session) | **Status:** COMPLETE + VERIFIED, INERT (bronze producer only)

## What
ADVI advisor-of-record daily-ETL (Andrew-direct 2026-07-12; explicit vendor word on /Portfolio/Accounts, CTO~B dispatch). Added the base-roster pull carrying udf7ADVISOROF (which NewPortfolio structurally omits) to the nightly inf-accounts-v2-daily Lambda via `--with-roster`, plus a fail-safe carry-forward and the required IAM grant. The durability upgrade inflection_rep_scope.py's own comment requested (static advisor-of-record snapshot -> live daily).

## Legs (all landed, none stranded)
1. Code commit `b71f4f7ca` -- Lambda bundle (pull_inflection_new_portfolio.py + lambda_function.py) + TF (BronzeAccountsRosterWrite IAM statement).
2. Source-map commit `32e3663da` (artifact_sha256).
3. `safe-apply` (0 add / 2 change / 0 destroy): IAM role-policy + Lambda source_code_hash.
4. Deploy record `2639ead16` + tag `inf-pipeline-v1.7.83` (pushed --follow-tags).

## Verification -- Rule 22a, 3-layer, all GREEN
- **desired** (TF): plan showed BronzeAccountsRosterWrite + Lambda hash `2sjnMP->klb5p7`.
- **applied** (live): `get-role-policy` shows BronzeAccountsRosterWrite live; `simulate-principal-policy` = ALLOWED on accounts_roster.json + marker + latest/ (Put+Get) WITH the POSITIVE CONTROL allowed on new_portfolio_accounts.json (proves the simulate is wired, not a silent implicitDeny).
- **exercised**: DEPLOYED-Lambda invoke -> StatusCode 200 -> the ROLE (not local creds) wrote a FRESH roster+marker+latest at 13:19:39Z (status=fresh, 3118 accts, 900 AoR, carried_forward=false). Local exercise also confirmed all 3 paths: fresh, carry-forward (401->latest/ copied), first-run-stale (roster_asof=null).
- **0-diff** verified (No changes on the targeted resources post-apply).

## Rule-22a-IAM catch (folded into runbook P4a by CTO~B)
The role's s3-accounts-v2 policy was FILENAME-scoped to new_portfolio_accounts.json (verified live `get-role-policy` on the (action,RESOURCE) pair, which comp-iam's (action)-only view clears green). The deployed Lambda would have 403'd on the roster write; the local exercise masked it (ran with local creds, not the role). Fixed by BronzeAccountsRosterWrite before deploy.

## Served impact: NONE (inert)
Gold fold gated OFF (INF_AOR_FOLD_ACTIVE); the deployed bundle's silver convert is the OLD serve-safe version (0 advisor_of_record_raw; DS's edit is serve-held in the DS-lane source, # DEPLOY-SERVE-HELD, base serve-gate d7359a797). The nightly now produces bronze/orion-api/{date}/accounts_roster.json + latest/ pointer daily; silver + gold stay inert until go-live.

## Remaining for go-live (CTO~B coordination, not this deploy)
DS daily-derived fold reproduces peter ~$135M/joe ~$29.2M/patrick ~$24.1M/noel ~$12.4M against live roster + assert_fold_landed adapts static->daily + silver serve-gate flip + INF_AOR_FOLD_ACTIVE=1 with never-widen (CTO+COO) sign-off.

## RAVC: CTO~B (1.0.0_SA_CTO~B). DS (0.4.0_DS_ClientPlatform) handed the live artifacts. Firm-sep inf-only throughout.
