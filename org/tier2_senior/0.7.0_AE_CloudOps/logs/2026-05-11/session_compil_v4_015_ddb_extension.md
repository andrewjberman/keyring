# AE 0.7.0 Session Log — ADHC_COMPIL_V4.015 DDB Extension
**Date:** 2026-05-11
**Agent:** 0.7.0_AE_CloudOps
**TO:** ADHC_COMPIL_V4.015

## Objective
Extend comp-freshness with `ddb <table>` subcommand + `all` combined-mode sweep.
Add DDB freshness checks for FIRMSEP/Cottonwood firm-config state surfaces.

## Work Completed

### Pre-work: DDB schema probe
- `aws dynamodb describe-table opal-users-v2`: PK (HASH), SK (RANGE); GSIs on email + firmId
- `aws dynamodb scan --filter begins_with(PK, :p)` with `":p":"FIRM#"`: confirmed 5 FIRM# META items with `createdAt` attribute; no `updatedAt` on META items
- `aws dynamodb describe-table opal-routing-config`: ResourceNotFoundException -- table does not exist

### Implementation: .tools/comp-freshness
Added DDB extension block (153 net new lines):
- `json` import; `DDB_CONFIG` constant pointing to `data/ddb_freshness_config.yaml`
- `_load_ddb_config()` -- loads + validates DDB config (required: table, pk_prefix, max_age_hours)
- `_get_ddb_items(table, pk_prefix, sk_filter)` -- aws dynamodb scan subprocess; returns None on ResourceNotFoundException (MISSING semantics), raises AwsUnreachable on credential/network errors
- `_extract_ddb_timestamp(item, primary_attr, fallback_attr)` -- extracts ISO-8601 timestamp from DDB {"S": "..."} format; tries primary then fallback
- `_check_ddb_entry(entry, now)` -- PASS/WARN/FAIL/SKIP status (same shape as S3 _check_artifact); MISSING if table not found; WARN if no items; WARN if no timestamp attrs
- `check_ddb_entries(entries)` -- parallel ThreadPoolExecutor (max_workers=8); same pattern as check_entries
- `cmd_ddb(table, pattern)` -- single table check; uses config thresholds if table in ddb_freshness_config, defaults (168h) otherwise
- `cmd_all()` -- sequential S3 BD + S3 INF + DDB sweep; max exit code propagation
- Extended `cmd_list()` -- shows DDB section after S3 sections
- Extended argparse -- `ddb <table> [--pattern]` + `all` subcommands

### New file: data/ddb_freshness_config.yaml
Two entries:
- `opal-users-v2`: FIRM# META, createdAt primary, updatedAt fallback, warn=120h fail=168h severity=WARN
- `opal-routing-config`: ROUTE#, updatedAt primary, createdAt fallback, warn=20h fail=24h severity=ERROR

### comp-tools.yaml update
Extended comp-freshness entry: ddb + all subcommands, DDB config path, schema convention (updatedAt/createdAt), updated note citing V4.015.

## Decisions Made
- DDB config is a SEPARATE file (`data/ddb_freshness_config.yaml`) -- keeps S3 gold_freshness_config.yaml backward-compatible (still a flat list). DDB targets are cross-pipeline infrastructure (firm config), not pipeline-specific.
- Timestamp convention: primary=`createdAt` for FIRM# META items (empirically confirmed no updatedAt), fallback=`updatedAt`. Config is flexible for tables with different conventions.
- MISSING (table not found): FAIL for ERROR-severity entries (opal-routing-config), WARN for WARN-severity. Symmetric with S3 "prefix not found" behavior.
- `all` mode exit code = max across all sections (consistent with chain behavior).

## Compiler Tools Run

| Tool | Command | Result |
|------|---------|--------|
| py_compile | python -m py_compile .tools/comp-freshness | OK |
| ruff | ruff check .tools/comp-freshness --target-version py39 | 1 warning fixed (unused variable `description`); re-run PASS |
| DDB Test 1 | comp-freshness ddb opal-users-v2 --pattern FIRM# | WARN (287h > 168h, severity=WARN) -- correct |
| DDB Test 2 | comp-freshness ddb opal-routing-config | FAIL (MISSING, severity=ERROR) exit 1 -- correct |
| Synthetic stale | max_age=1h on 287h-old data | FAIL -- correct |
| Combined mode | comp-freshness all | exit 1 (routing-config MISSING) -- correct |
| S3 regression | chain bd + chain inf | structure unchanged; pre-existing S3 FAILs unaffected |
| --list | comp-freshness --list | DDB section shown -- correct |
| index guard | safe-commit.sh | blocked DS~B contamination (ds-precommit-check.py staged); unstaged extras; re-run PASS |

6/6 ACs satisfied. Ruff false-positive (unused var) fixed before commit.

## Files Modified
- `.tools/comp-freshness` (extended -- 359 net insertions)
- `data/ddb_freshness_config.yaml` (new)
- `org/modules/graph/comp-tools.yaml` (comp-freshness entry updated)
- `org/tier2_senior/0.7.0_AE_CloudOps/task_orders/ADHC_COMPIL_V4.015.*.md` (status: complete)

## Blockers
- ADHC_DSFLOW.005 (safe-deploy gate): blocked by ID-DTYPE-ENFORCEMENT (STAGED for DS~B). Escalated to COO.
- ADHC_INFRUNNERPARITY: blocked by DSFLOW.005 (2-deep). COO notified.

## Current State
ADHC_COMPIL_V4.015 COMPLETE. Commit 6becc77e5, pushed to CLOUD.
2 remaining TOs dep-gated. Awaiting COO GO on ID-DTYPE-ENFORCEMENT to unblock DSFLOW.005.

## Next Steps
- RAVC2 to CTO + COO for ADHC_COMPIL_V4.015
- Monitor for COO unblock signal on DSFLOW.005
