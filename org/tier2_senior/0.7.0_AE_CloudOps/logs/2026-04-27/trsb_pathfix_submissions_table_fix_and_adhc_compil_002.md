# Session Log — TRSB_PATHFIX SUBMISSIONS_TABLE Fix + ADHC_COMPIL.002 Gate

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-27
**TOs:** TRSB_PATHFIX.TO-1 (browser smoke unblock), TRSB_PATHFIX.TO-3 (SES audit), ADHC_COMPIL.002
**Status:** COMPLETE (TRSB + ADHC_COMPIL.002)
**Tags:** trade-pipeline-v1.6.1, (ADHC_COMPIL.002 commit e32e1013)

---

## Part 1 — ADHC_COMPIL.002: Partial Chain Dep Gate (AUAGAP.002 class defense)

### Problem
`--chain partial` in gold_dispatch.sh had no gate checking required post-step deps.
AUAGAP.002 incident: split rerun stopped at B_03 without re-running C_00 (canonical_performance),
leaving portal performance figures stale against new gain values.

### Implementation

**BD dispatch (`data/black_diamond/scripts/gold/gold_dispatch.sh`):**
- Added `check_partial_deps()` function: calls `comp-pipescript postdeps` for each script ID
  in the partial set; checks all `[BLOCKING] Must run:` entries are included. Exits 1 with
  ERROR message + suggested corrected command if any are missing.
- Added `log_bypass_entry()` function: writes `[ADHC_COMPIL.002] BYPASS:` entry to
  `org/compiler-tools-log.md` when `--no-deps-check` flag is used.
- Added `--no-deps-check` flag parsing and `PARTIAL_IDS` capture for `--chain partial`.
- Gate placed before BG re-invoke (line ~906) so `exit 1` propagates to caller.

**Orion dispatch (`data/orion/scripts/gold/orion-gold-dispatch.sh`):**
- Same four changes mirrored.

**Deps yamls:**
- `data/black_diamond/scripts/gold/gold_pipeline_deps.yaml`: B_03 → C_00 BLOCKING post-step
  (incident: AUAGAP.002)
- `data/orion/scripts/gold/orion_pipeline_deps.yaml`: created; same B_03 → C_00 entry

**Test fixture (`data/black_diamond/scripts/gold/test_adhc_compil_002_gate.sh`):**
- 4 ACs, 8 assertions.
- Fixed `run_dispatch()` to accept timeout as first arg (previous run had hardcoded 8s;
  `comp-pipescript postdeps` takes ~5s per call on Windows → 2 calls = ~13s needed for AC1).
- Updated call sites: AC1/AC2 → 30s, AC3/AC4 → 10s.
- All 8 assertions PASS confirmed.

### S3 Uploads
```
s3://opal-data-bd/code/gold/gold_dispatch.sh     17:22:24Z
s3://opal-data-inf/code/gold/orion-gold-dispatch.sh  17:22:26Z
```

### Commit
```
e32e1013  feat(ADHC_COMPIL.002): partial chain dep gate -- BD + Orion dispatch
  5 files changed, 388 insertions(+), 8 deletions(-)
```
Note: lane violations (POD4 files authored by AE) — warn-only, cross-pod infra concern.

---

## Part 2 — TRSB_PATHFIX: SUBMISSIONS_TABLE Bug (trade-pipeline-v1.6.1)

### Root Cause Diagnosis

Andrew reported: `500 - {"message": "Error processing submission: An error occurred
(AccessDeniedException) when calling the PutItem operation: User: .../trade-submission-handler
is not authorized to perform: dynamodb:PutItem on resource: .../table/trade-submissions
because no identity-based policy allows the dynamodb:PutItem action"}`

Investigation:
1. API GW routes: 12 `/api/general/trades/*` routes confirmed live (CUSTOM+naqxlm) — TO-1 infra correct.
2. CloudFront: `/api/general/trades/*` behavior correctly routes to API GW 7k3ed8px20.
3. Lambda IS being invoked (gets to DDB call) — routing works.
4. Error: Lambda trying to write to `table/trade-submissions` (non-existent). Actual table: `opal-trade-submissions`.

Root cause located in `config.py` (shared across all 3 trade Lambdas):
```python
# WRONG (all 3 Lambdas):
SUBMISSIONS_TABLE = os.environ.get('SUBMISSIONS_TABLE', 'trade-submissions')
# Should be:
SUBMISSIONS_TABLE = os.environ.get('SUBMISSIONS_TABLE', 'opal-trade-submissions')
```
No `SUBMISSIONS_TABLE` env var was set in Terraform for any of the 3 Lambdas.

**IAM policy on `trade-submission-lambda-role`:** correctly covers `opal-trade-submissions`
with `dynamodb:PutItem` — policy was never the problem.

### Affected Lambdas
| Lambda | Terraform env block | SUBMISSIONS_TABLE before | after |
|---|---|---|---|
| trade-submission-handler | had DASHBOARD_URL + EMAIL_FROM | missing | opal-trade-submissions |
| trade-workflow-handler | had DASHBOARD_URL + EMAIL_FROM | missing | opal-trade-submissions |
| trade-dashboard-api | no env block | missing | opal-trade-submissions |

`trade-identifier-cache`: uses `trade-security-identifiers` (hardcoded, correct). Not affected.

### Fix

**`infra/aws/terraform/trade-pipeline/lambdas.tf`:**
- `trade-submission-handler` environment block: added `SUBMISSIONS_TABLE = "opal-trade-submissions"`
- `trade-workflow-handler` environment block: added `SUBMISSIONS_TABLE = "opal-trade-submissions"`
- `trade-dashboard-api`: added new `environment { variables = { SUBMISSIONS_TABLE = "opal-trade-submissions" } }`

**`config.py` defaults fixed:**
- `infra/aws/lambda/trade-pipeline/trade-dashboard-api/src/config.py` line 8: `trade-submissions` → `opal-trade-submissions`
- `infra/aws/lambda/trade-pipeline/trade-submission-handler/src/config.py`: reclaimed + correct default
- `infra/aws/lambda/trade-pipeline/trade-workflow-handler/src/config.py`: reclaimed + correct default

**Note on source reclamation:** submission-handler and workflow-handler source was not in repo
(TRSB_TFIMPT.W2 had not yet reclaimed them). Downloaded from Lambda presigned URL, placed in
`infra/aws/lambda/trade-pipeline/{function}/src/`. These use `placeholder.zip` +
`lifecycle { ignore_changes = [filename, source_code_hash] }` in Terraform; env var is the
authoritative fix path for now.

**`trade-dashboard-api` code rebuild:**
- Rebuilt zip from local `src/` directory (22,436 bytes)
- Uploaded to `s3://opal-313476888478-lambda-artifacts/trade-pipeline/trade-dashboard-api.zip`
- Terraform detected new S3 version; applied 1 additional change.

### Terraform Apply

**First apply (env vars):**
```
Plan: 0 to add, 3 to change, 0 to destroy.
trade-submission-handler: Modifications complete after 6s
trade-workflow-handler: Modifications complete after 6s
trade-dashboard-api: Modifications complete after 6s
```

**Second apply (dashboard-api code):**
```
Plan: 0 to add, 1 to change, 0 to destroy.
trade-dashboard-api: Modifications complete after 6s
Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
```

**Final 0-diff plan:** `No changes. Your infrastructure matches the configuration.`

### Verification

**Post-apply env var confirm:**
```json
trade-submission-handler: { "DASHBOARD_URL": "...", "SUBMISSIONS_TABLE": "opal-trade-submissions", "EMAIL_FROM": "trades@opalinvest.dev" }
trade-workflow-handler:   { "DASHBOARD_URL": "...", "SUBMISSIONS_TABLE": "opal-trade-submissions", "EMAIL_FROM": "trades@opalinvest.dev" }
trade-dashboard-api:      { "SUBMISSIONS_TABLE": "opal-trade-submissions" }
```

**Smoke test (boto3 direct invoke):**
```
StatusCode: 200
submission_id: TRADE-20260427-205554-E5FD51
status: PENDING_APPROVAL
fund: PFDE
initiator: andrew@opalinvest.com
```

**DDB verify:**
```
opal-trade-submissions.get_item('TRADE-20260427-205554-E5FD51')
  status: PENDING_APPROVAL
  fund: PFDE
  initiator: andrew@opalinvest.com
  FOUND
```

**Dashboard read (trade-dashboard-api GET /submissions):**
```
StatusCode: 200
Submissions returned: 1
First item ID: TRADE-20260427-205554-E5FD51
First item status: PENDING_APPROVAL
```

### Commit + Tag
```
fb1e0df0  fix(TRSB_PATHFIX): SUBMISSIONS_TABLE env var -- opal-trade-submissions
  4 files changed, 133 insertions(+), 5 deletions(-)
tag: trade-pipeline-v1.6.1 (pushed with --follow-tags)
```

---

## Part 3 — TRSB_PATHFIX.TO-3: SES Alyssa Verify Audit

**Pre-state audit:**
- `aws sesv2 get-account ProductionAccessEnabled: False` — sandbox mode
- All 9 AJ spec members verified in SES (including alyssa@opalinvest.com):

```
adam@opalinvest.com       Success
aj@opalinvest.com         Success
alyssa@opalinvest.com     Success  ← already done, no AE action needed
andrew@opalinvest.com     Success
austin@opalinvest.com     Success
lauren@opalinvest.com     Success
manav@opalinvest.com      Success
menachem@opalinvest.com   Success
yang@opalinvest.com       Success
```

**AE actions:** All complete. Alyssa was already verified.

**Prod-access packet:** `infra/aws/ses/trade-pipeline-prod-access-request.md` — complete
and ready. Prepared by 0.5.0_AE_OpalETL on 2026-04-24.

**Sandbox interim decision:** Acceptable. All 9 spec members verified. BROKERAGE_EMAILS in
config.py routes all brokerage emails to andrew@opalinvest.com — no external SES send needed.

**Andrew action required:**
Submit SES production-access form via AWS Console > SES > Account Dashboard > Request Production Access.
Use packet at `infra/aws/ses/trade-pipeline-prod-access-request.md`.
(Account-root console action — cannot be delegated to agent.)

**TO-3 AC status at RAVC4:**
- AC1: alyssa@opalinvest.com VerificationStatus = Success ✓
- AC2: ProductionAccessEnabled = False; sandbox + all-9-verified is deliberate interim state pending Andrew form submission ✓ (documented)
- AC3: Andrew flagged to submit form today; ticket number TBD (pending Andrew action)
- AC4: Deferred until TO-2 DDB adds all 9 rows + Andrew triggers end-to-end test

---

## Open Items

| Item | Owner | Status |
|---|---|---|
| Browser smoke: Submit + Approvals + Execution + History tabs | Andrew | Pending |
| SES production-access form submission | Andrew | Pending (packet ready) |
| TO-2: trade-users DDB reconcile (9 rows, dual-write) | 0.3.0_DT_TradingOperations | Gate released |
| TO-3 AC4: end-to-end email CloudWatch evidence | After TO-2 | Deferred |
| submission-handler + workflow-handler: migrate from placeholder.zip to S3 artifacts | AE | Deferred (TRSB_TFIMPT.W3) |
| Lambda Function URL 403 (inf-otp-relay) | Andrew | Pending AWS Console check |

---

## ORNREN.002 (prior session, logged here for completeness)

**Status:** COMPLETE
- `infra/aws/ec2/inf-gold-layer-runner/watchdog-shutdown.sh` GOLD_REGEX: `inf_gold_scripts/` → `orion_gold_scripts/`
- `infra/aws/ec2/inf-gold-layer-runner/RUNBOOK.md`: all `inf-gold-dispatch` refs → `orion-gold-dispatch`
- S3: `s3://opal-data-inf/code/watchdog-shutdown.sh` uploaded
- Committed in prior sweep commit (ORNREN.002)
