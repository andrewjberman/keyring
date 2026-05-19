# SSCN_DIVDEF.004 — Lambda UNIVERSE_MAP swap + NON_SCORING_COLS fold-in (security-scanner-v1.1.0 + v1.1.1)

**Date:** 2026-05-19
**Agent:** 0.5.0_AE_OpalETL
**TO:** `org/tier2_senior/0.5.0_AE_OpalETL/task_orders/SSCN_DIVDEF.004.ae-lambda-universe-map-swap-and-redeploy.md`
**PRD:** `docs/architecture/SSCN_DIVDEF.md` v0.2 §6.4 (CTO~B commit c34f16d13)
**Issued by:** 2.0.0_SA_COO~B 2026-05-19 PM (with in-flight scope amendment authorizing NON_SCORING_COLS fold-in)

## Current State

- SSCN_DIVDEF.004 COMPLETE. Lambda `opal-security-scanner-processor` swapped to v0.2 5-universe US-equity set; NON_SCORING_COLS amended in-flight per COO~B authorization.
- Two ship tags: `security-scanner-v1.1.0` (UNIVERSE_MAP swap) + `security-scanner-v1.1.1` (NON_SCORING_COLS amendment fold-in).
- Final Lambda LastModified: 2026-05-19T17:46:45Z; CodeSha256: `A3NUd/GPjhj1G+fwC2M5v7X0bkBOweFPQ+dyBmBJsr0=`.
- All 7 ACs satisfied; both terraform applies 0-diff verified; record-terraform-deploy CHANGELOG entries written.

## Pipeline Tags

| Pipeline | Tag | Commit |
|---|---|---|
| security-scanner-pipeline | security-scanner-v1.1.1 (new) | `ea4062681` |
| security-scanner-pipeline | security-scanner-v1.1.0 (new) | `5977be75d` |
| smartx-pipeline | smartx-v2.2.0 (unchanged) | — |
| yang-pipeline | yang-v2.4.2 (unchanged) | — |
| news-pipeline | news-v2.9.10 (unchanged) | — |
| market-overview | market-overview-v1.9.0 (unchanged) | — |

## Deployment Sequence

### v1.1.0 — UNIVERSE_MAP swap

| Step | Action | Result |
|------|--------|--------|
| 1 | Commit source | `5977be75d` feat(security-scanner): Lambda UNIVERSE_MAP swap to v0.2 5-universe US-equity set |
| 2 | build-and-upload.sh | SHA256: `qsmj9/nAIgdSxkKOAV/suzTeYh7/YdNvEoriBmPoWIA=` |
| 3 | Commit source map | `efcf9d4c5` ci(security-scanner): upload artifact for v1.1.0 [skip ci] |
| 4 | terraform plan | 0 add / 1 change / 0 destroy (Lambda code-hash only) |
| 5 | terraform apply | Resources: 0 added, 1 changed, 0 destroyed; Lambda LastModified 2026-05-19T17:42:02Z |
| 6 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 7 | Tag + push | `security-scanner-v1.1.0` pushed --follow-tags |
| 8 | record-terraform-deploy | `463232f53` CHANGELOG.json entry written |

### v1.1.1 — NON_SCORING_COLS in-flight amendment (COO~B authorized)

| Step | Action | Result |
|------|--------|--------|
| 1 | Belt-and-suspenders grep | Only stale legacy ref: line 63 of NON_SCORING_COLS itself; no other legacy IDs (`r1000v`/`acwx`/`eafe`/`eafev`) in lambda_function.py |
| 2 | Commit source | `ea4062681` feat(security-scanner): NON_SCORING_COLS add wt_iwr/wt_ijh/wt_csus |
| 3 | build-and-upload.sh | SHA256: `A3NUd/GPjhj1G+fwC2M5v7X0bkBOweFPQ+dyBmBJsr0=` |
| 4 | Commit source map | `7cc403dc6` ci(security-scanner): upload artifact for v1.1.1 [skip ci] |
| 5 | terraform plan | 0 add / 1 change / 0 destroy (Lambda code-hash only) |
| 6 | terraform apply | Resources: 0 added, 1 changed, 0 destroyed; Lambda LastModified 2026-05-19T17:46:45Z |
| 7 | 0-diff plan | No changes. Infrastructure is up-to-date. |
| 8 | Tag + push | `security-scanner-v1.1.1` pushed --follow-tags |
| 9 | record-terraform-deploy | `4c73d2e0f` CHANGELOG.json entry written |

## Code Changes

### `infra/aws/lambda/opal_security_scanner_processor/lambda_function.py`

**UNIVERSE_MAP (lines 46-51) — v1.1.0:**
```python
UNIVERSE_MAP = {
    "sp500":   "wt_ivv",
    "r1000":   "wt_iwb",
    "rmidcap": "wt_iwr",
    "sp400":   "wt_ijh",
    "msciusa": "wt_csus",
}
```
Verbatim PRD v0.2 §6.4. Was legacy 6-entry (sp500/r1000/r1000v/acwx/eafe/eafev → wt_ivv/wt_iwb/wt_iwd/wt_acwx/wt_efa/wt_efv).

**NON_SCORING_COLS (lines 60-77) — v1.1.1 amendment:**
- Added `wt_iwr` (IWR — Russell Midcap)
- Added `wt_ijh` (IJH — S&P MidCap 400)
- Added `wt_csus` (CSUS — MSCI USA)
- Retained legacy 4 (`wt_iwd`/`wt_acwx`/`wt_efa`/`wt_efv`) per COO~B forward-compat guidance.

**ds-commit-gate cleanup (line 295) — v1.1.0:**
- Removed vestigial `f` prefix on `logger.info(f"INFO: Reading Excel from S3...")` → `logger.info("INFO: Reading Excel from S3...")`.
- Pre-existing ruff defect; required to clear Rule-14 gate exit 0.
- No functional change; documented for AC-evidence traceability.

## Acceptance Criteria

| AC | Status | Evidence |
|----|--------|----------|
| AC1 | PASS | v1.1.0 UNIVERSE_MAP swap (5977be75d) + v1.1.1 NON_SCORING_COLS addition (ea4062681); both diffs visible via `git show`. |
| AC2 | PASS | Both plans (v1.1.0 + v1.1.1): 0 add / 1 change / 0 destroy. Only `s3_object_version` + `source_code_hash` + `last_modified` updated. |
| AC3 | PASS | Both applies clean; 0-diff replan after each. CloudWatch Lambda update event emitted. |
| AC4 | PASS | Tags `security-scanner-v1.1.0` + `security-scanner-v1.1.1` annotated + pushed --follow-tags. v1.1.0 tag message cites SSCN_DIVDEF.004 + Andrew-direct migration + PRD v0.2 c34f16d13; v1.1.1 cites the in-flight amendment + Factor-Bank-pollution defect. |
| AC5 | PASS | Code-review: `_update_manifest` at `lambda_function.py:379` is called UNCONDITIONALLY after the for-loop (no `if processed == 0` guard). 5/5 processed → manifest emit. Floor=0 / ceiling=5 OK. The empirical 2026-05-19 "no Manifest emit" finding from DT 0.3.0 is consistent with another failure mode (e.g., Lambda timeout or `_write_s3` exception); not a count-based gate. |
| AC6 | PASS | `record-terraform-deploy.sh` ran cleanly for both tags; CHANGELOG.json updated (commits 463232f53 + 4c73d2e0f). |
| AC7 | PASS | v1.1.0 LastModified 2026-05-19T17:42:02Z > TO start ~17:33Z. v1.1.1 LastModified 2026-05-19T17:46:45Z. |

## In-Flight Scope Amendment Handling

Phase 1 baseline read surfaced a NON_SCORING_COLS audit-completeness gap: the constant listed the LEGACY 6 universe weight columns but was MISSING the 3 new universes' columns (`wt_iwr`/`wt_ijh`/`wt_csus`). Without those in the exclusion set, the new wt_* weight columns would be treated as scoring factors -> Factor Bank UX defect + ~50KB data bloat per scanner_data.json.

Empirically confirmed: pulled the partial-run `sp500/scanner_data.json` produced by the legacy Lambda + 2026-05-19 source XLSX upload. First row has 287 keys in `values` + `pctls` dicts (`wt_csus`, `wt_iwr`, `wt_ijh` present), vs contract-expected 284.

I had ALREADY shipped v1.1.0 before checking inbox for the amendment, so the fix landed as v1.1.1 (patch bump = scope-coherence). Total scope: v1.1.0 + v1.1.1 = one TO close, two tags, two `terraform apply` cycles. No regression to v1.1.0 (NON_SCORING_COLS additions are pure exclusion-set extensions).

**Lesson note:** check inbox immediately after committing, BEFORE building/applying. The amendment MCP was in flight at the time I started the build. Sister to `[[feedback-inbox-check-before-landing]]` — inbox-check before each landing step prevents this exact double-deploy.

## Belt-and-Suspenders Grep Findings

```
grep -in "wt_iwd\|wt_acwx\|wt_efa\|wt_efv\|r1000v\|acwx\|eafe\|eafev" lambda_function.py
```

Only hit: line 63 — the NON_SCORING_COLS legacy 4 weight entries (retained per COO~B forward-compat guidance). No legacy universe IDs (`r1000v`/`acwx`/`eafe`/`eafev`) appear anywhere else in lambda_function.py (no special-case branches, default fallbacks, or hardcoded lists). factor_metadata_registry.json has zero matches. Clean.

## Verification

### Lambda config post-deploy

```
$ aws lambda get-function --function-name opal-security-scanner-processor --query '{LastModified:Configuration.LastModified, CodeSha256:Configuration.CodeSha256}'
{
    "LastModified": "2026-05-19T17:46:45.000+0000",
    "CodeSha256": "A3NUd/GPjhj1G+fwC2M5v7X0bkBOweFPQ+dyBmBJsr0="
}
```

### Source XLSX weight-column inventory (cross-check)

```
$ python -c "import pandas as pd; df=pd.read_excel('.runtmp/sscn_source.xlsx', header=4); print([c for c in df.columns if c.lower().startswith('wt_')])"
['wt_ivv', 'wt_csus', 'wt_iwb', 'wt_iwr', 'wt_ijh']
```

Exactly the new 5. Legacy 4 (`wt_iwd`/`wt_acwx`/`wt_efa`/`wt_efv`) absent. v1.1.1 NON_SCORING_COLS aligns.

## Compiler Tools

| Tool | Result | Notes |
|------|--------|-------|
| `comp-iam service opal-security-scanner-processor` | OK | 3 ops (s3:PutObject + 2 × s3:GetObject); role `sscn_processor` unchanged. No new boto3 surface added by this TO. |
| Direct-read `lambda_function.py:46-53` | OK | Confirmed pre-edit legacy UNIVERSE_MAP shape. |
| Direct-read `lambda_function.py:60-74` (NON_SCORING_COLS) | OK | Surfaced the audit-completeness gap; folded into v1.1.1. |
| Direct-read `lambda_function.py:378-380` (manifest emit) | OK | `_update_manifest` is unconditional post-loop; no `processed`-count gate. AC5 satisfied. |
| `python -m py_compile` | exit 0 | Both v1.1.0 + v1.1.1 edits. |
| `ruff check --target-version py39` | exit 0 | After ds-commit-gate cleanup at line 295. |
| `.tools/ds-commit-gate.sh` | exit 0 (Rule 14) | Twice — pre-v1.1.0 + pre-v1.1.1. |
| `terraform plan` (pre-apply, both cycles) | 0 add / 1 change / 0 destroy | Lambda code-hash + s3_object_version only. |
| `terraform plan` (post-apply, both cycles) | No changes. Infrastructure is up-to-date. | 0-diff verified after each apply. |
| `aws lambda get-function` post-apply | LastModified > TO-start | v1.1.0 17:42:02Z; v1.1.1 17:46:45Z. |
| `comp-pipescript deployed` | N/A | Lambda pipeline, not EC2-script. Substituted with Terraform 0-diff replan + Lambda LastModified per TO mandate. |
| Belt-and-suspenders grep (v1.1.1) | 1 hit (NON_SCORING_COLS line itself) | No other stale legacy refs. |

## Cross-Domain Coordination

None blocking — Lambda code edit, no shared S3 artifacts touched (the source XLSX upload key is the trigger, not a write target).

Downstream: RAVC2 CC to **0.3.0_DT_TradingOperations** IS the GO for revised SSCN_DIVDEF.002 TO-2 (DT delete-and-re-PUT source XLSX → Lambda v1.1.1 re-fires → 11 files in `2026-05-18/` + `latest/` overwrites with new 5 universes). Per TO body cross-domain note.

## Findings Surfaced

1. **Empirical confirmation of NON_SCORING_COLS pollution defect** (pre-fix): partial 2026-05-19 sp500 scanner_data.json had 287 keys in values+pctls vs contract 284 (3 extra: `wt_iwr`/`wt_ijh`/`wt_csus`). Folded into v1.1.1 per COO~B in-flight amendment.

2. **DT 0.3.0's "no Manifest emit" finding** (AC5 code review): `_update_manifest` is UNCONDITIONAL post-loop. The empirical "no Manifest emit at processed=2" is NOT explained by a count-based guard — must be another failure mode (Lambda timeout, `_write_s3` exception, or some other path). Out of scope for this TO; surfaced for COO~B/DT 0.3.0 awareness.

3. **`comp-pipescript io` Lambda graph gap**: Lambda is not indexed in the comp graph (`comp-pipescript io opal-security-scanner-processor` is not a script-tier command; the comp-graph indexes EC2 scripts not Lambdas). Documented; out of scope.

## Next Steps

- `[2.0.0_SA_COO~B]` RAVC2 validation AC1-7. SSCN_DIVDEF.json ws=AE flip to complete on receipt.
- `[1.0.0_SA_CTO~B]` informational CC; 3rd same-day audit-completeness-vs-empirical-probe-enumeration anchor noted for session-end memory.
- `[0.3.0_DT_TradingOperations]` RAVC2 CC IS the GO for revised SSCN_DIVDEF.002 — delete-and-re-PUT source XLSX → Lambda v1.1.1 re-fires → 11 files clean.
- `[0.5.0_AE_OpalETL]` next: MDLP_VOLAUD.003 (newly issued by base COO; dual-writer fix on `yang-generate-benchmark-returns`; Phase 0.5 probe-first per CTO disposition). Time pressure: target before 2026-05-20T14:00Z scheduled SFN cron. ~18h margin after natural session break.
