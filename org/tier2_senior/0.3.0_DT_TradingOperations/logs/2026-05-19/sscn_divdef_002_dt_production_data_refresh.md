# SSCN_DIVDEF.002 — DT Production Data Refresh 2026-05-18 — 0.3.0_DT_TradingOperations

**Date:** 2026-05-19
**Task Order:** SSCN_DIVDEF.002.dt-production-data-refresh-2026-05-18
**Status:** PENDING (RAVC2 BLOCKED — awaiting COO~B + CTO~B adjudication)
**TO_START_TS:** 2026-05-19T15:27:18Z

---

## Objective

Per PRD v0.1 (1.0.0_SA_CTO~B; `docs/architecture/SSCN_DIVDEF.md`, commit a5e1b7ef4 2026-05-19) and Andrew-direct directive 2026-05-19: refresh production SSCN data by uploading `Screening_DIVZ_IDVZ_20260518.xlsx` to `s3://opal-data-portal-v2/security_scanner/uploads/2026-05-18/` to event-trigger `opal-security-scanner-processor` (tag `security-scanner-v1.0.2`). No code/Terraform change. ~30min DT wall per CTO estimate.

This TO opens the `2026-05-18/` snapshot and gates TO-3 (DS validation pulls `latest/` post-upload). Phase 5 RAVC2 CC to DS 0.3.0 was the GO trigger for TO-3.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-iam service | `comp-iam service opal-security-scanner-processor` | PARTIAL | Resolved 3 operations on Lambda surface: `s3:PutObject` (line 128), `s3:GetObject` (lines 297, 401). Role: `sscn_processor`. Tool reports `[UNKNOWN]` for policy attachment — CTO PRD section 5 ran the same check at 11:13Z with attestation; relying on PRD baseline. |
| aws s3 ls (uploads pre-state) | `aws s3 ls s3://opal-data-portal-v2/security_scanner/uploads/` | PASS | Only `2026-02-26/` present; matches PRD section 2.2 baseline. |
| aws s3 ls (latest/factor_metadata.json pre-state) | `aws s3 ls s3://opal-data-portal-v2/json/security_scanner/latest/factor_metadata.json` | PASS | LastModified `2026-03-06 12:20:30 UTC`, 68541 bytes — matches PRD section 2.2 baseline. Recorded as AC4 "before" anchor. |
| aws s3 cp (upload) | `aws s3 cp Screening_DIVZ_IDVZ_20260518.xlsx s3://opal-data-portal-v2/security_scanner/uploads/2026-05-18/...` | PASS | Exit 0, 6.6 MiB uploaded. Required `unset MSYS_NO_PATHCONV` to avoid Python shim path doubling. |
| aws logs get-log-events | `aws logs get-log-events --log-group-name /aws/lambda/opal-security-scanner-processor --log-stream-name 2026/05/19/[$LATEST]60ad4a55c95349b2a4fc703e5300b005` | PASS (data: PARTIAL) | Lambda fired, completed without ERROR/Traceback, but processed only 2 of 6 universes. Switched to PowerShell to bypass Git Bash MSYS `/aws/lambda/...` path conversion. |
| aws s3 ls --recursive (post-state) | `aws s3 ls s3://opal-data-portal-v2/json/security_scanner/{2026-05-18,latest}/ --recursive` | PASS (data: FAIL) | 5 files in 2026-05-18/ (expected 13). 13 files in latest/ but split-vintage (3 fresh + 7 stale + 1 metadata + 2 sp500 + 2 r1000 = breakdown below). |
| jq .asOf on latest/factor_metadata.json | `aws s3 cp .../factor_metadata.json - | .tools/jq.exe .asOf` | PASS | Returned `"2026-05-18"` — AC5 met. |
| jq R1000 spot-check | `... universes/r1000/scanner_data.json - | .tools/jq.exe -r '.rows[0:3] ...'` | PASS | AAPL dy_ntm=34.97 ret_mom_252d=48.79; NVDA 29.02 99.19; MSFT 41.84 38.55 — all finite in [0,100]. AC6 met for r1000. |
| jq .asOf on latest/eafe/scanner_data.json | `... universes/eafe/scanner_data.json - | .tools/jq.exe -r '.asOf'` | PASS (data: STALE) | Returned `"2026-02-26"` — empirical proof of split-vintage corruption in latest/. |
| python pandas wt_* probe | `python -c "import pandas as pd; df=pd.read_excel(..., header=4, nrows=2); print([c for c in df.columns if str(c).startswith('wt_')])"` | PASS (root cause) | Source XLSX `wt_*` columns: `['wt_ivv', 'wt_csus', 'wt_iwb', 'wt_iwr', 'wt_ijh']`. Lambda required 6: only 2 present (wt_ivv→sp500, wt_iwb→r1000). Missing: wt_iwd, wt_acwx, wt_efa, wt_efv. Root cause empirically confirmed. |

**What worked:** Tail of `/aws/lambda/opal-security-scanner-processor` via PowerShell `aws logs get-log-events` was the decisive evidence — the 4 `WARNING: Universe column 'wt_X' not found in dataframe, skipping universe 'Y'` lines plus the terminal `INFO: Processing complete. universes processed=2` (NOT `Manifest updated`) revealed the partial-completion pattern. The pandas probe of source XLSX columns confirmed root cause as source-data drift.

**What failed:** `comp-iam service` reports `[UNKNOWN]` policy-attachment status — relies on PRD attestation. `MSYS_NO_PATHCONV=1` broke the `aws` Python shim (doubled the `\c\` drive prefix) — had to selectively unset for S3 calls and switch to PowerShell for CloudWatch calls.

**Gap found:** PRD section 5 empirical probe at 11:13Z verified header=4 + 13 SIGNAL columns, but did NOT enumerate the 6 universe weight columns (`wt_ivv`, `wt_iwb`, `wt_iwd`, `wt_acwx`, `wt_efa`, `wt_efv`). This is the audit-completeness gap that turned a source-data drift into production data corruption — generalizes to [[feedback-audit-completeness-vs-behavior-correctness]]. Additionally: `opal-security-scanner-processor` silent-WARN-skips missing universe columns rather than failing loud, structurally allowing partial completions to write to `latest/` without surfacing.

---

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 1 | Pre-state probe — uploads/ | Only `2026-02-26/` present |
| 2 | Pre-state probe — latest/factor_metadata.json LastModified | `2026-03-06 12:20:30 UTC`, 68541 bytes |
| 3 | comp-iam service opal-security-scanner-processor | 3 operations resolved; policy attachment UNKNOWN; relying on PRD section 5 attestation |
| 4 | Record TO_START_TS | `2026-05-19T15:27:18Z` |
| 5 | aws s3 cp upload | 6,929,919 bytes → `s3://opal-data-portal-v2/security_scanner/uploads/2026-05-18/Screening_DIVZ_IDVZ_20260518.xlsx`; exit 0 |
| 6 | AC1 verify | `aws s3 ls s3://opal-data-portal-v2/security_scanner/uploads/2026-05-18/` → 6,929,919 bytes; PASS |
| 7 | CloudWatch describe-log-streams | Latest stream `2026/05/19/[$LATEST]60ad4a55c95349b2a4fc703e5300b005`, lastEventTimestamp 1779204463791 (15:27:43.791Z) |
| 8 | CloudWatch get-log-events | RequestId 2430894c-c99e-4852-94f5-5f4a04827ebf, START 15:27:43.630Z, END 15:27:59.157Z, Duration 15596ms |
| 9 | Log scan — INFO markers | `asOf=2026-05-18` PASS; `Identified 287 scoring factor columns` (>=280) PASS; sp500 wrote both keys; r1000 wrote both keys |
| 10 | Log scan — WARNINGs | 4 `WARNING: Universe column 'wt_X' not found in dataframe, skipping universe 'Y'` for r1000v/acwx/eafe/eafev |
| 11 | Log scan — terminal marker | `INFO: Processing complete. asOf=2026-05-18, universes processed=2` (NOT `Manifest updated`) |
| 12 | Log scan — ERROR/Traceback | None — AC8 strict-PASS |
| 13 | Post-state — 2026-05-18/ | 5 files (factor_metadata + sp500/{universe,scanner} + r1000/{universe,scanner}); expected 13; **AC3 FAIL** |
| 14 | Post-state — latest/ | 13 files mixed-vintage: 3 fresh (factor_metadata + sp500 + r1000) + 8 STALE 2026-03-06 (r1000v + acwx + eafe + eafev = 4 universes x 2 files each) |
| 15 | Post-state — manifest.json | LastModified `2026-05-19 11:37:29 UTC` < TO_START_TS 15:27:18 UTC; **AC7 FAIL** |
| 16 | jq .asOf | `"2026-05-18"`; AC5 PASS |
| 17 | jq r1000 spot-check | AAPL/NVDA/MSFT dy_ntm + ret_mom_252d all finite in [0,100]; AC6 PASS (for r1000 only) |
| 18 | jq eafe .asOf (split-vintage proof) | `"2026-02-26"` — empirical confirmation that latest/ is corrupted split-vintage |
| 19 | Root-cause probe — source XLSX wt_* | `['wt_ivv', 'wt_csus', 'wt_iwb', 'wt_iwr', 'wt_ijh']` — only 2 of 6 universe weight columns present |
| 20 | RAVC2 BLOCKED — COO~B | Sent 20260519T154154Z + resend 154233Z |
| 21 | RAVC2 CC — CTO~B | Sent 20260519T154200Z + resend 154239Z |
| 22 | DS 0.3.0 CC | **Withheld** — TO-3 must not validate against corrupted latest/ |

---

## Verification

**Lambda invocation log excerpt (RequestId 2430894c-c99e-4852-94f5-5f4a04827ebf):**
```
[INFO] 15:27:43.791Z Processing s3://opal-data-portal-v2/security_scanner/uploads/2026-05-18/Screening_DIVZ_IDVZ_20260518.xlsx
[INFO] 15:27:43.791Z asOf=2026-05-18
[INFO] 15:27:51.238Z Loaded 3012 rows x 331 columns
[INFO] 15:27:51.239Z Identified 287 scoring factor columns
[INFO] 15:27:51.330Z Wrote s3://opal-data-portal-v2/json/security_scanner/2026-05-18/factor_metadata.json (68541 bytes)
[INFO] 15:27:51.360Z Wrote s3://opal-data-portal-v2/json/security_scanner/latest/factor_metadata.json (68541 bytes)
[INFO] 15:27:51.364Z Processing universe 'sp500' (column=wt_ivv)
[INFO] 15:27:51.368Z sp500: 502 securities after filter
... sp500 universe + scanner JSON writes to 2026-05-18/ and latest/ ...
... r1000 universe + scanner JSON writes to 2026-05-18/ and latest/ ...
[INFO] 15:27:59.156Z Completed universe 'r1000'
[WARNING] 15:27:59.156Z Universe column 'wt_iwd' not found in dataframe, skipping universe 'r1000v'
[WARNING] 15:27:59.156Z Universe column 'wt_acwx' not found in dataframe, skipping universe 'acwx'
[WARNING] 15:27:59.157Z Universe column 'wt_efa' not found in dataframe, skipping universe 'eafe'
[WARNING] 15:27:59.157Z Universe column 'wt_efv' not found in dataframe, skipping universe 'eafev'
[INFO] 15:27:59.157Z Processing complete. asOf=2026-05-18, universes processed=2
END RequestId: 2430894c-c99e-4852-94f5-5f4a04827ebf
REPORT RequestId: 2430894c-c99e-4852-94f5-5f4a04827ebf  Duration: 15596.39 ms  Billed Duration: 17915 ms  Memory Size: 2048 MB  Max Memory Used: 316 MB  Init Duration: 2318.44 ms
```

**S3 post-state at latest/ (split-vintage):**
```
2026-05-19 11:27:52   66.9 KiB  factor_metadata.json                  <- FRESH (asOf=2026-05-18)
2026-03-06 12:20:52   27.3 MiB  universes/acwx/scanner_data.json      <- STALE (asOf=2026-02-26)
2026-03-06 12:20:47   11.8 MiB  universes/acwx/universe_data.json     <- STALE
2026-03-06 12:20:56   11.0 MiB  universes/eafe/scanner_data.json      <- STALE (asOf=2026-02-26 jq-confirmed)
2026-03-06 12:20:54    4.7 MiB  universes/eafe/universe_data.json     <- STALE
2026-03-06 12:20:59    6.5 MiB  universes/eafev/scanner_data.json     <- STALE
2026-03-06 12:20:57    2.8 MiB  universes/eafev/universe_data.json    <- STALE
2026-05-19 11:27:59   16.4 MiB  universes/r1000/scanner_data.json     <- FRESH
2026-05-19 11:27:56    7.1 MiB  universes/r1000/universe_data.json    <- FRESH
2026-03-06 12:20:43   14.1 MiB  universes/r1000v/scanner_data.json    <- STALE
2026-03-06 12:20:40    6.1 MiB  universes/r1000v/universe_data.json   <- STALE
2026-05-19 11:27:55    8.2 MiB  universes/sp500/scanner_data.json     <- FRESH
2026-05-19 11:27:53    3.5 MiB  universes/sp500/universe_data.json    <- FRESH
```

**AC Scorecard:**

| AC | Status | Evidence |
|----|--------|----------|
| AC1 | PASS | `uploads/2026-05-18/Screening_DIVZ_IDVZ_20260518.xlsx` 6,929,919 bytes |
| AC2 | PARTIAL | asOf=2026-05-18 + 287 factors >=280 OK; NO `Manifest updated` final marker; 4 WARN-skips |
| AC3 | **FAIL** | 5 files in `2026-05-18/`; expected 13 (sp500 + r1000 only) |
| AC4 | PASS | `latest/factor_metadata.json` LastModified 15:27:52 UTC > TO_START_TS 15:27:18 UTC |
| AC5 | PASS | `jq .asOf` → `"2026-05-18"` |
| AC6 | PASS (r1000 only) | AAPL 34.97/48.79, NVDA 29.02/99.19, MSFT 41.84/38.55 — all in [0,100]. Other 4 universes have stale 2026-02-26 percentiles (out of scope for this spot-check). |
| AC7 | **FAIL** | `latest/manifest.json` LastModified 11:37 UTC < TO_START_TS 15:27 UTC — NOT updated by this invocation |
| AC8 | PASS strict | No ERROR or Traceback in Lambda log (4 WARNINGs, no ERRORs) |

**Root cause (empirical pandas probe of source XLSX):**
```
wt_* columns present: ['wt_ivv', 'wt_csus', 'wt_iwb', 'wt_iwr', 'wt_ijh']
Lambda requires:        wt_ivv (sp500), wt_iwb (r1000), wt_iwd (r1000v), wt_acwx (acwx), wt_efa (eafe), wt_efv (eafev)
Source provides:        wt_ivv, wt_iwb only
Missing:                wt_iwd, wt_acwx, wt_efa, wt_efv
```

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Do NOT trigger AC8 BLOCKED path despite materially failing ACs | AC8 strict-reads as "Lambda errors" → no ERROR/Traceback so AC8 strict-PASS. BUT the partial completion creates production data corruption that strictly exceeds AC8's scope. Per [[feedback-to-scope-none-of-above-space]], surface as BLOCKED-equivalent with empirical evidence + adjudication-path options rather than forcing into AC8 wording or closing as success. |
| Do NOT CC DS 0.3.0 on RAVC2 close | Per TO Phase 5: "The CC to DS 0.3.0 IS the GO for TO-3." With `latest/` corrupted split-vintage, TO-3 (DS DIVZ preset validation) would validate against partially-stale percentile distributions — silently false-passing/false-failing the DIVZ analysis depending on which universe DS samples. Withheld CC. |
| Do NOT roll back `latest/` autonomously | Rollback is reversible but destructive (would delete the 3 fresh files). Adjudication-path 1 (Andrew re-export with all 6 wt_* columns) would re-fire Lambda and overwrite ALL universes uniformly — making rollback wasted work. Surface to COO~B + CTO~B for decision first. |
| Do NOT manually invoke Lambda | TO `do_not` rule + the bypass would create different log entries and not solve the source-data drift. |
| Preserve `2026-05-18/` partial snapshot | TO `do_not` says preserve historical uploads. Even though 2026-05-18/ has only 5 of 13 files, it serves as evidence of the partial-completion state for audit trail. |
| Source XLSX in S3 remains in place | If Andrew chooses adjudication-path 1, Andrew can either re-upload to same key (auto-fires Lambda) OR upload to a new key and we point Lambda at it. Keeping the broken XLSX in place documents the source-data drift. |
| Use comp-iam UNKNOWN attestation as PRD-attestation-relay | comp-iam returned `[UNKNOWN]` for policy attachment status — the tool can resolve operations but can't fully chase the IAM policy graph for `sscn_processor`. PRD section 5 ran the same check at 11:13Z with attestation. Reasonable to rely on PRD baseline within the same UTC day. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier2_senior/0.3.0_DT_TradingOperations/logs/2026-05-19/sscn_divdef_002_dt_production_data_refresh.md` | New session log (this file) | This commit |
| `org/compiler-tools-log.md` | Session entry appended | This commit |

S3 changes:
- ADDED: `s3://opal-data-portal-v2/security_scanner/uploads/2026-05-18/Screening_DIVZ_IDVZ_20260518.xlsx` (6,929,919 bytes)
- ADDED: 5 files under `s3://opal-data-portal-v2/json/security_scanner/2026-05-18/` (partial)
- OVERWROTE: 5 of 13 files under `s3://opal-data-portal-v2/json/security_scanner/latest/` (factor_metadata + sp500/* + r1000/*)

NO code changes (`infra/aws/lambda/opal_security_scanner_processor/` untouched per TO `do_not` rule).
NO Terraform changes (`infra/aws/terraform/security-scanner-pipeline/` untouched).

---

## Blockers

RAVC2 BLOCKED — pending COO~B + CTO~B adjudication on one of 4 paths:

1. **Andrew re-exports XLSX with all 6 universe weight columns** (wt_ivv, wt_iwb, wt_iwd, wt_acwx, wt_efa, wt_efv). Re-PUT → Lambda re-fires → all 6 universes write uniformly. ~5min DT after Andrew delivers. Cleanest path.
2. **Roll back `latest/` to pure 2026-02-26 vintage** — revert factor_metadata + sp500/* + r1000/* via copy from 2026-02-26/ snapshot. Keep 2026-05-18/ partial as historical. ~3min DT. Restores uniform stale state while Andrew adjusts the export.
3. **Accept split-vintage as Pod 3 v0.1 scope** — PRD amendment required. NOT recommended (portal UI vintage misrepresentation).
4. **Lambda code change to fail-loud on missing universe column** — future PRD item. Silent-WARN-skip is the structural defect that allowed source-data drift to corrupt production.

---

## Current State

SSCN_DIVDEF.002 RAVC2 BLOCKED. Source file landed at canonical key. Lambda fired without ERROR but processed only 2 of 6 universes (sp500, r1000) — silently WARN-skipped r1000v/acwx/eafe/eafev because source XLSX missing those 4 universe weight columns. `latest/` is now split-vintage corruption: factor_metadata claims asOf=2026-05-18 but 4 of 6 universe-files carry 2026-02-26 vintage (jq-confirmed on eafe). AC3 FAIL, AC7 FAIL, AC8 strict-PASS. RAVC2 BLOCKED delivered to COO~B + CTO~B. DS 0.3.0 deliberately NOT CC'd — TO-3 must not start against corrupted latest/.

TO status: `pending` (will close after adjudication path executes).

---

## Next Steps

1. **[2.0.0_SA_COO~B + 1.0.0_SA_CTO~B] Adjudicate one of 4 paths** — top-level decision blocks both this TO close and TO-3 GO.
2. **[0.3.0_DT_TradingOperations] Execute selected adjudication path** — ~3-5min DT wall depending on path. Re-RAVC2 with full evidence on completion.
3. **[1.0.0_SA_CTO~B] PRD amendment if path 4 selected** — fail-loud Lambda behavior on missing universe columns; future TO into security-scanner-pipeline.
4. **[0.3.0_DS_TradingOperations] HOLD on TO-3** — DS GO is gated on this TO's RAVC2 with corrected `latest/`. DS receives GO via DS-direct CC only when DT re-RAVC2 confirms uniform 2026-05-18 vintage in latest/.
