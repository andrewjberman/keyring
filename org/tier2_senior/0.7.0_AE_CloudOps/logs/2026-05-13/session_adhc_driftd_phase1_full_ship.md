# AE 0.7.0 Session Log — ADHC_DRIFTD Phase 1 Full Ship + Validation Sweep
**Date:** 2026-05-13
**Agent:** 0.7.0_AE_CloudOps
**Trigger:** Andrew direct override 2026-05-13 ~20:20Z — "if its that serious then we should probably just address the drift project now because i dont want to come online tomorrow and forget about this and trash the infrastructure"
**Project:** ADHC_DRIFTD (PRD `911d3b69a`)
**Scope:** All 3 fix TOs (DRIFTD.001 + .002 + .003) + validation sweep (DRIFTD.VAL) against today's 3 historical incidents.

---

## TL;DR

Shipped all 3 ADHC_DRIFTD Phase 1 fixes in one atomic bundle plus a refinement commit + a defensive follow-on commit. Validation sweep run against today's 3 incident Lambdas + 19 BD-pipeline Lambdas + 14 INF-pipeline Lambdas. Result: every Lambda now records its true content-commit; sibling-Lambda trample eliminated; CHANGELOG.json writes succeed including on the legacy-array-schema inf-pipeline file. The "running record-terraform-deploy.sh would trash infrastructure" risk Andrew flagged is now closed.

---

## Sequencing

Per Andrew direct override, executed from PRD v0.1 without waiting for CTO's individual TO files. MCPed both COO + CTO at session-arrange to flag the override; proceeded immediately.

---

## DRIFTD.001 — record-terraform-deploy.sh per-Lambda content-commit derivation

### Bug

`record-terraform-deploy.sh` lines 145 (Python branch) + 188 (Node.js branch) unconditionally set `cfg["last_deployed_commit"] = sweep_commit_sha` for every Lambda matching `tf_file.startswith(tf_prefix)`. Side effect: sibling Lambdas not actually content-touched by this sweep had their content provenance destroyed. 3 empirical incidents earlier today required manual backfill.

### Fix (commit `c2a241a90`)

Both Python + Node.js branches refactored to:
1. For each Lambda matching the tf_prefix, derive `content_commit` via:
   ```
   git log -1 --format=%H -- <source_dir>/<files[*]>
   ```
   (CWD = workspace root)
2. Only write `last_deployed_commit` + `last_deployed_at` if `prior != content_commit` (conservative — preserves sibling-Lambda values + makes function idempotent on no-op deploys).
3. New reporting: `Updated N` (content changed), `Preserved N` (content unchanged), `Skipped N` (externally-managed).

### Refinement (commit `86516114f`)

First DRIFTD.VAL bd-pipeline run surfaced: `bd-allocation-file-checker` has `source_dir: "EXTERNAL"` + empty `files: []` (AWS-imported, TF lifecycle ignore_changes on code). The fallback in derive_content_commit returned the sweep commit, which differed from prior value → got written → SAME bug behavior. Refinement: skip externally-managed Lambdas entirely.

```python
if src_dir == 'EXTERNAL' or not files_array:
    skipped_external.append(fn)
    continue
```

Both language branches updated. Also restored bd-allocation-file-checker's prior `last_deployed_commit` (`1151f449...`) that the first VAL run had trampled.

### Empirical verification

3-incident dry-run test (run directly in Python against the source map state):
```
PASS inf-unified-account-dim-daily            expected=bc4759ad00  derived=bc4759ad00
PASS opal-smartx-ingestion-pipeline           expected=1444936425  derived=1444936425
PASS smartx-ec2-autostart                     expected=f46a3682e2  derived=f46a3682e2
```

All 3 incident Lambdas derive their correct content commits under the new logic.

EXTERNAL-skip path test: PASS (bd-allocation-file-checker correctly preserved).

---

## DRIFTD.002 — build-and-upload.sh source_dir → files[] parity check

### Bug

`build-and-upload.sh` verified manifest → disk (file in `files[]` missing from `source_dir` = ERROR + halt) but NOT disk → manifest (file in `source_dir` missing from `files[]` = silently excluded from zip; Lambda ImportErrors at invocation). DS-base `144493642` shipped Step 6 without registering `append_non_model_today.py` in source map; AE caught at pre-build review.

### Fix (in commit `c2a241a90`)

Post-existence-check, scan `source_dir/*.py` for any top-level `.py` file not present in `FN_FILES[]`. Ignore list: `__pycache__`, `*.pyc`, `test_*.py`, `*_test.py`. ERROR + halt with actionable message:

```
ERROR: ADHC_DRIFTD.002 parity check failed —
       Files present in source_dir but NOT in lambda-source-map.json files[]:
         + append_non_model_today.py
       Action: register each in functions["opal-smartx-ingestion-pipeline"].files[] in
               infra/aws/lambda/ci/lambda-source-map.json before re-running build.
       Override (rare): set BAU_PARITY_SKIP=1 + justify in commit message.
```

Per-build escape hatch via `BAU_PARITY_SKIP=1` env var.

### Empirical verification

```
POSITIVE (current smartx ingestion):  parity clean — PASS
NEGATIVE (simulated pre-144493642):   drift detected on append_non_model_today.py — PASS
                                       (would have caught the original gap)
```

### Pre-ship sweep finding

Scanning all 137 zip-based Lambdas found 4 with pre-existing parity gaps (NONE in today's 3 incident Lambdas):

| Lambda | Extra files |
|--------|-------------|
| `bd-price-update` | `lambda_function_v1_backup.py`, `lambda_function_v2.py` |
| `opal-infrastructure-monitor` | `typing_extensions.py` (Layer 3 violation candidate) |
| `seeking-alpha-news-scraper` | `backfill-noon-published-at.py` |
| `yang-generate-allocation-summary` | `etf_classification.py`, `etf_classifications_dynamodb.py` |

These 4 will block their next build until either (a) cleaned up or (b) `BAU_PARITY_SKIP=1` per-build override. Surfaced separately for COO cleanup-TO routing. Not blocking the DRIFTD ship.

---

## DRIFTD.003 — CHANGELOG.json gitLogJson escaping fix

### Bug

`record-terraform-deploy.sh` lines 282-292 built `GIT_LOG_JSON` via:
```bash
git log --pretty=format:'{"sha":"%H",...,"message":"%s"}' | awk ...
```
which broke on any commit subject containing `"`, `\`, or newline. `bun JSON.parse(GIT_LOG_JSON)` then failed, CHANGELOG.json write silently skipped. Observed in smartx-pipeline v2.1.0 deploy + likely unknown count of prior deploys.

### Fix (in commit `c2a241a90`)

Removed the awk-based shell-level JSON construction. Moved git log fetch INTO the CHANGELOG writer JS via `execSync` with a Unit Separator (`\x1f`) field delimiter, then `JSON.stringify` each record. Field-count guard skips malformed records; never writes corrupt JSON.

### Empirical verification

```
PASS: 15 real recent commits, JSON round-trip OK
PASS: synthetic stress (quote + backtick + backslash + newline in subject) round-trips OK
```

---

## DRIFTD.001 Follow-on — CHANGELOG.json array-form defensive handler

### Bug surfaced during DRIFTD.VAL inf-pipeline run

First inf-pipeline record-deploy attempt under DRIFTD.001/.003 fixes:
```
TypeError: cl.entries.unshift is not a function
```

Root cause: inf-pipeline's CHANGELOG.json is a legacy array-form (the lone outlier across 14 pipelines; 13 use canonical `{_description, _pipeline, entries}` object form). The writer assumed object form and crashed on `unshift` against an array.

### Fix (commit `197952903`)

Defensive load: detect schema. Array-form gets wrapped into canonical object form (existing entries preserved verbatim). Object-form loads as-is. Unknown shape warns + replaces with empty canonical form.

### Empirical verification

Re-ran inf-pipeline record-deploy under defensive fix:
```
✓ CHANGELOG.json updated
```
Schema after: object form, 3 entries (2 legacy preserved + 1 new for inf-pipeline-v1.7.55).

---

## DRIFTD.VAL — Validation Sweep

### Phase 1: bd-pipeline (commit `ebe570ee2`)

Sweep produced clean per-Lambda content-commit attribution across 19 BD Lambdas:
```
Updated 19 function(s) (content-commit changed):
  + bd-allocation-file-checker -> c2a241a9   ← FALLBACK (refined later)
  + bd-allocation-processor    -> 2f97f315
  + bd-allocation-trigger      -> d42ada6d
  + bd-asset-dim-trigger       -> 2c981c5d
  + bd-capture-output-versions -> b3207410
  + bd-client-detail           -> 5fa9cfa8
  + bd-fees-trigger            -> 1bc64829
  + bd-gold-detail-checker     -> d42ada6d
  + bd-gold-foundation         -> d42ada6d
  + bd-gold-layer              -> d42ada6d
  + bd-gold-trigger            -> 946f0e0e
  + bd-portal-advisor-publisher-> 26eff434
  + bd-portal-publisher        -> 31479a7c
  + bd-price-update            -> 83d3a260
  + bd-realized-trigger        -> 158a0026
  + bd-time-machine            -> 233da228
  + bd-transactions-trigger    -> d42ada6d
  + bd-unrealized-trigger      -> 158a0026
  + historical-prices-scheduler-> 9fb52be0
✓ CHANGELOG.json updated
```

`bd-allocation-file-checker` initially got sweep commit (EXTERNAL Lambda fallback bug); fixed in refinement + manual restoration (commit `86516114f`).

### Phase 2: inf-pipeline (commits `bbd9ff461` + `bf7a2721e`)

Run #1 (under array-form CHANGELOG crash): source map updated (13 Lambdas updated, 1 preserved); CHANGELOG write failed.

Run #2 (under defensive fix): source map fully synced — all 14 Lambdas were "Preserved" since their content commits already matched (run #1 had set them). CHANGELOG.json written + migrated to object form.

```
Preserved 14 function(s) (content unchanged since last deploy):
  = inf-assets-trigger
  = inf-billing-daily
  = inf-bronze-trigger
  = inf-ec2-launch-monitor
  = inf-ec2-retry-launch
  = inf-gold-trigger
  = inf-jwt-trigger
  = inf-otp-relay
  = inf-performance-daily
  = inf-portal-advisor-publisher
  = inf-silver-aggregator
  = inf-silver-chain
  = inf-tax-daily
  = inf-unified-account-dim-daily      ← preserved at bc4759ad0 (today's manual restore intact)
✓ CHANGELOG.json updated
```

Conservative-update idempotence confirmed empirically.

### Phase 3: shared-infra

Expected failure mode (no Lambdas in `infra/aws/terraform/shared-infra/`). Existing WARN-no-functions-found + exit-1 behavior preserved. Acceptable — shared-infra audit trail is the git tag `shared-infra-v1.10.0` itself; no Lambda-source-map entry to update.

---

## Commit Trail

```
197952903 ADHC_DRIFTD.001 follow-on: defensive CHANGELOG.json array-form handler
bf7a2721e ci: record deploy inf-pipeline @ bbd9ff46 [skip ci]            ← DRIFTD.VAL Phase 2 run #2
bbd9ff461 ci: record deploy inf-pipeline @ 86516114 [skip ci]            ← DRIFTD.VAL Phase 2 run #1 (partial)
86516114f ADHC_DRIFTD.001 refinement + bd-allocation-file-checker restoration
ebe570ee2 ci: record deploy bd-pipeline @ c2a241a9 [skip ci]              ← DRIFTD.VAL Phase 1
c2a241a90 ADHC_DRIFTD.001+002+003 (full Phase 1 fix bundle): deploy-record drift hardening
```

All commits on origin/CLOUD.

---

## Acceptance Criteria (project-level, per PRD §8)

| AC | Result |
|----|--------|
| 1. TO-1 dry-run on 3 historical incidents reproduces correct `last_deployed_commit` | PASS — all 3 derive expected values |
| 2. TO-2 dry-run on `144493642` reproduces parity-gap detection | PASS — would have caught the original gap |
| 3. TO-3 dry-run on quote-in-subject commit produces valid CHANGELOG.json entry | PASS — synthetic stress + 15 real commits round-trip |
| 4. TO-VAL sweep confirms zero manual backfills needed under fixed logic on 3-incident regression test set | PASS — 3 incident Lambdas correctly preserved + INF-pipeline 14 Lambdas correctly preserved on re-run |
| 5. No regression on legitimate single-Lambda-tf-touch case; sibling Lambda preservation verified | PASS — bd-pipeline run gave each of 19 Lambdas its own content commit (no uniform sweep value) |
| 6. AE 0.7 session log captures 3-incident-day pattern + memory entry candidate | This file (+ candidate memory after session) |
| 7. Existing standalone TO redirected (record-terraform-deploy-content-commit-fix.md) | Absorbed into DRIFTD.001 — TO file remains in task_orders/ as historical reference; no new ship from it |

---

## Open Items Post-Session

| Item | Status |
|------|--------|
| 4 pre-existing source_dir/files[] parity gaps (bd-price-update + opal-infrastructure-monitor + seeking-alpha-news-scraper + yang-generate-allocation-summary) | Surface to COO for separate cleanup-TO routing. Next build of each will halt with actionable error until either registered or `BAU_PARITY_SKIP=1` override. Not blocking — but worth proactive cleanup. |
| inf-pipeline CHANGELOG.json schema migrated array→object | Done automatically by defensive handler on first record-deploy invocation under the fix. Historical entries preserved. |
| shared-infra-v1.10.0 audit trail | Git tag is canonical (no CHANGELOG.json in shared-infra by design). Acceptable. |
| Tag updates | None needed — `bd-v2.24.8` / `inf-pipeline-v1.7.55` / `shared-infra-v1.10.0` already tagged at the IAM commits before DRIFTD.VAL. Tags cover what was deployed; record-deploy commits are CI metadata. |

---

## Compiler Tools

| Tool | Use | Result |
|------|-----|--------|
| `python3` direct test of `derive_content_commit` | DRIFTD.001 dry-run on 3 historical incidents | PASS — all 3 derive expected values |
| `bun .runtmp/driftd003_test.js` | DRIFTD.003 dry-run on real + synthetic commits | PASS — JSON round-trip OK incl. quote/backtick/backslash/newline |
| Inline bash parity check simulation | DRIFTD.002 dry-run positive + negative cases | PASS — current state clean; simulated historical-incident gap detected |
| Live `record-terraform-deploy.sh` execution on bd-pipeline + inf-pipeline | DRIFTD.VAL end-to-end | PASS — content provenance recorded correctly; CHANGELOG written including array→object migration |

---

## RAVC Trail (Summary)

| RAVC | Direction | Time | Content |
|------|-----------|------|---------|
| Andrew direct override | Andrew → AE 0.7 | ~20:20Z | "address the drift project now" |
| Override-FYI to COO | AE 0.7 → COO | 20:16Z | Proceeding from PRD without waiting for individual TO files |
| Override-FYI to CTO | AE 0.7 → CTO | 20:16Z | Scope check against PRD; greenlit-by-Andrew context |
| Final RAVC2 ship | AE 0.7 → CTO + COO + Andrew | (this commit) | All 3 TOs shipped + DRIFTD.VAL PASS |

---

## Session Status: COMPLETE — ADHC_DRIFTD Phase 1 SHIPPED; DRIFTD.VAL PASS on 3 historical incidents + bd-pipeline 19 Lambdas + inf-pipeline 14 Lambdas; the "run record-deploy = trash infrastructure" risk is structurally closed
