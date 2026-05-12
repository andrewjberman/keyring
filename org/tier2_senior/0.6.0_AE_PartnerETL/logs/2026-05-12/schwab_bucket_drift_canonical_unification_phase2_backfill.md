# Schwab Bucket-Drift Canonical Unification — Phase 2 S3 Backfill (AE portion)

| Field | Value |
|-------|-------|
| Agent | 0.6.0_AE_PartnerETL |
| Date | 2026-05-12 |
| Trigger | DS~D RAVC1: 49F cert $50M+ gold gap traced to Schwab converter writing silver to non-canonical bucket; Andrew directive ~18:00Z "all of this should be in the same opal-data-bd bucket" |
| Scope (AE) | Phase 2 S3 backfill (4 tables) + Phase 3.5 yaml edit handoff + Phase 4 verify gate + RAVC close |
| Owner of .py edits | 0.4.0_DS_ClientPlatform~D (per CLAUDE.md Rule 13, COO RAVC2 routing 18:35Z) |

## Current State

**Phase 2-5 COMPLETE on AE side. RAVC CLOSED.** Awaiting DS~D Phase 6 (fresh bd-gold-trigger + 49F cert before/after gap measurement).

| Phase | Owner | Status |
|---|---|---|
| 1 — Audit (4-table drift confirmed) | 0.6.0_AE | COMPLETE |
| 2 — S3 backfill (canonical fresh thru 20260508) | 0.6.0_AE | COMPLETE |
| 3 — .py edits (10 files: converters + readers + chained) | 0.4.0_DS_ClientPlatform~D | COMPLETE — commit `7c030faee` |
| 3.5 — yaml edit | rerouted to DS~D (owned-paths POD4) | COMPLETE — included in 7c030faee atomic commit |
| 4 — verify (static + idempotent re-run + negative test) | 0.6.0_AE | COMPLETE — see Phase 4 section |
| 5 — RAVC close + session log finalize | 0.6.0_AE | COMPLETE — this log |
| 6 — Gold re-run + 49F cert before/after gap measurement | 0.4.0_DS_ClientPlatform~D | pending DS~D dispatch |

## Compiler Tools

| Tool | Run | Result | Notes |
|---|---|---|---|
| comp-pipescript io | (deferred to DS~D's Phase 3 — they own gold-script edits) | n/a | AE scope this session was pure S3 ops + 1 yaml edit (rerouted); no AE .py change |
| comp-pipescript deployed | (Phase 4 — pending DS~D commit) | pending | Will run against B_00, A_03, B_01, lib/schwab_flows.py, all 4 converters once DS~D commit lands |
| comp-validate | n/a | n/a | No gold run dispatched this session |
| comp-blast | (informally referenced via DS~D RAVC1 cohort breakdown) | n/a | DS~D pre-computed blast radius: A_03/B_00/B_01/D_00/D_04/partner_analytics/leaderboards/client_performance |

No comp-* tools were structurally required for Phase 2 backfill (pure `aws s3 sync` ops with no script execution). Compiler-tools-log entries for Phase 4 deferred until verify gate runs.

## Phase 1 — Empirical Audit

**Diagnosis confirmed:** RPS canonical (opal-data-bd/schwab/silver/rps/) stopped writing 2026-04-22 (last partition `date=20260420`). RPS drifted (opal-data-schwab/silver/RPS/) continues through 20260508. Same pattern across 4 tables.

| Table | Drifted (opal-data-schwab) | Canonical pre-fix (opal-data-bd) | Action |
|---|---|---|---|
| **RPS** | `silver/RPS/` thru 20260508 | `schwab/silver/rps/` thru **20260420** (stopped 2026-04-22) | Backfill 20260421→20260508 |
| **ACC** | `silver/ACC/` thru 20260508 | (no prefix existed) | Full table cp (581 partitions) |
| **TRN** | `03_silver/TRN/` thru 20260508 | (no prefix existed) | Full table cp (509 partitions) |
| **ULN** | `silver/ULN/` thru 20260508 | `schwab/silver/uln/` thru **20260413** (stopped 2026-04-13) | Backfill 20260414→20260508 |
| ULT | (no drifted writer) | `schwab/silver/ult/` thru 20260407 (stale, no writer) | Out of scope — confirmed by DS~D, sourced from BD-side B_03 not Schwab |
| RLD | (canonical-only) | `schwab/silver/rld/` thru 20260508 ✓ | No action — `convert_schwab_lots_to_silver.py` already canonical |

**Cross-script bucket split (hidden in gold layer):**

| Reader | Bucket | Path | Effect |
|---|---|---|---|
| `B_00.canonical_holdings.py:73` | opal-data-bd | `schwab/silver/rps/` (canonical) | Read STALE → forward-fill path activates for every date after 2026-04-20 |
| `A_03.positions_cube.py:267,269` (env default) | opal-data-schwab | `silver/RPS/` (drifted) | Read FRESH → positions_cube includes new accounts but canonical_holdings doesn't |
| `B_01.holdings_lots.py:151,153` (env default) | opal-data-schwab | `silver/RPS/` (drifted) | Read FRESH |
| `gold_freshness_config.yaml:43 schwab_rps` | opal-data-schwab | `silver/RPS/` (drifted) | Freshness gate reports FRESH (lies about canonical) → dispatches gold runs against stale B_00 |
| `lib/schwab_flows.py:32` | opal-data-schwab | `03_silver/TRN_NNA/` (drifted) | Reads chained-drifted TRN_NNA |
| `build_schwab_bd_account_xref.py:36,40` | opal-data-schwab | drifted in + out | Chained — reads ACC drifted, writes xref drifted |

**Chained-drift writers** (discovered while answering DS~D's downstream-consumer audit):

| Script | Reads | Writes |
|---|---|---|
| `convert_schwab_trn_to_nna_silver.py` | drifted TRN | drifted TRN_NNA |
| `build_schwab_bd_account_xref.py` | drifted ACC | drifted xref |

**Sibling deprecation candidate:**

| Script | State | Recommendation |
|---|---|---|
| `convert_schwab_rps_to_silver.py` (DS-authored 2026-04-06, ADVI_GLDOPS) | Writes canonical RPS BUT reads from `opal-data-bd/schwab/bronze/` which has been stale since 2026-04-06. Two writers + abandoned bronze source = both paths broken in different ways. | Deprecate; primary `_to_parquet.py` becomes sole canonical writer post-flip |

## Phase 2 — S3 Backfill (executed this session)

```bash
aws s3 sync s3://opal-data-schwab/silver/RPS/      s3://opal-data-bd/schwab/silver/rps/ --exclude '_test_write*'  # EXIT 0
aws s3 sync s3://opal-data-schwab/silver/ULN/      s3://opal-data-bd/schwab/silver/uln/ --exclude '_test_write*'  # EXIT 0
aws s3 sync s3://opal-data-schwab/silver/ACC/      s3://opal-data-bd/schwab/silver/acc/ --exclude '_test_write*'  # EXIT 0
aws s3 sync s3://opal-data-schwab/03_silver/TRN/   s3://opal-data-bd/schwab/silver/trn/ --exclude '_test_write*'  # EXIT 0
```

All 4 syncs idempotent (additive only; pre-existing canonical RPS partitions untouched).

### Post-sync verification (tail of each canonical prefix)

```
opal-data-bd/schwab/silver/rps/   ...date=20260507/, date=20260508/   (was date=20260420 — backfill spanned 21..08)
opal-data-bd/schwab/silver/uln/   ...date=20260507/, date=20260508/   (was date=20260413 — backfill spanned 14..08)
opal-data-bd/schwab/silver/acc/   ...date=20260507/, date=20260508/   (new prefix; full table — 581 partitions)
opal-data-bd/schwab/silver/trn/   ...date=20260507/, date=20260508/   (new prefix; full table — 509 partitions)
```

## Phase 3.5 — gold_freshness_config.yaml rerouting (note for posterity)

Owned-paths.yaml lane for `data/black_diamond/scripts/gold/**` is POD4 (DS-owned). 0.6.0_AE_PartnerETL not in POD4, so commit would be BLOCKED by pre-commit hook (Phase-2 BLOCK mode since 2026-04-30). Rerouted to DS~D's atomic Phase 3 commit per clean-lane-discipline default; FORCE-BYPASS audit avoided. COO informed. Edit already applied to working tree; DS~D `git add`s + commits.

Edit content:
- Line 43: `s3_key_prefix: s3://opal-data-schwab/silver/RPS/` → `s3://opal-data-bd/schwab/silver/rps/`
- Lines 49-52: docstring updated — RPS is positions snapshot (not "realized proceeds + sells" which was wrong); added bucket-unification incident reference.

Future ADHC_OWNPTH consideration: `gold_freshness_config.yaml` may warrant a CLOUD_OPS_OR_ETL carve-out parallel to `gold_dispatch.sh` (both are AE-routine config / orchestration, not DS data scripts). Flagged in MCP to COO; not bundling into this incident.

## Phase 4 — Verify (COMPLETE)

DS~D commit `7c030faee` landed on origin/CLOUD head 14:29Z. 11-file atomic scope per their RAVC2 (4 converters + 2 chained writers + 3 gold readers + 1 deprecation docstring + 1 yaml — the yaml originally my edit, picked up via their POD4 pathspec).

### Static
- DST_BUCKET = `'opal-data-bd'` on all 4 primary converters ✓
- DST_PREFIX = `'schwab/silver/{rps,acc,trn,uln}/'` on all 4 ✓
- A_03 + B_01 env-var default flipped to `'opal-data-bd'`, RPS prefix `'schwab/silver/rps/'` ✓
- `lib/schwab_flows.py`: SCHWAB_BUCKET canonical, TRN_NNA prefix canonical ✓
- `gold_freshness_config.yaml:43`: `s3://opal-data-bd/schwab/silver/rps/` ✓

### Idempotent converter re-run (parallel, all exit 0)
```
RPS:  Available STANDARD RPS dates: 335   Already converted: 582   To convert: 0
ACC:  Found 581 ACC files                 Already converted: 581   Pending: 0
TRN:  Dest: s3://opal-data-bd/schwab/silver/trn/    Already converted: 509   To convert: 0
ULN:  Dest: s3://opal-data-bd/schwab/silver/uln/    Already converted: 365   To convert: 0
```

The "Already converted: N" skip counts come from each converter listing the canonical bucket — proves post-commit code path correctly queries `opal-data-bd/schwab/silver/{table}/`. TRN + ULN print canonical DST explicitly.

### Negative test — drifted bucket UNCHANGED post-rerun
| Path | Pre-rerun mtime | Post-rerun mtime |
|---|---|---|
| `opal-data-schwab/silver/RPS/date=20260508/data.parquet` | 2026-05-11 15:26:26 | 2026-05-11 15:26:26 |
| `opal-data-schwab/silver/ACC/date=20260508/data.parquet` | 2026-05-11 15:25:54 | 2026-05-11 15:25:54 |
| `opal-data-schwab/03_silver/TRN/date=20260508/data.parquet` | 2026-05-11 15:26:37 | 2026-05-11 15:26:37 |
| `opal-data-schwab/silver/ULN/date=20260508/data.parquet` | 2026-05-11 15:28:03 | 2026-05-11 15:28:03 |

Zero new writes to drifted bucket. Code path bypasses it entirely. RAVC CLOSED.

### Cosmetic follow-on (not blocking)
Two converters have stale log-string docstrings (code constants correct; only print/log strings carry old path):
- `convert_schwab_rps_to_parquet.py:183` — `'Building silver/RPS/...'` → should be `'schwab/silver/rps/'`
- `convert_schwab_uln_to_silver.py:246` — `'Converting Schwab ULN -> silver/ULN/ parquet'` → should be `'schwab/silver/uln/'`

Flagged to DS~D; trivial cleanup, can land in a follow-on hygiene commit.

## Next Steps

1. **[0.4.0_DS_ClientPlatform~D]** Phase 3 atomic commit (10 .py + 1 yaml) + `.tools/safe-deploy.sh` cycle + `comp-pipescript deployed` MATCH proof + RAVC2 to AE 0.6.0 + COO. Plus deprecation note in `convert_schwab_rps_to_silver.py` docstring.
2. **[0.6.0_AE_PartnerETL]** Phase 4 verify gate (post-commit). Idempotent converter re-run via DS dispatch. Post listings. RAVC close.
3. **[0.4.0_DS_ClientPlatform~D]** Phase 6 — fresh `bd-gold-trigger` dispatch (AE 0.7's mid-flight 17:31Z chain ran B_00 against stale data; cannot reuse). B_00 + cascade re-run for window 20260421..20260508. Brief #9 Part A 49F cert before/after gap measurement; residual expected from 46 positions-cube-missing + 355 zero-balance-shell cohorts (unaffected by Schwab fix).
4. **[2.0.0_SA_COO]** Closure ledger entry; consider retroactive ADHC_BUCKDR project for class-of-bug audit (other partners, other data layers).
5. **[0.6.0_AE_PartnerETL — follow-on, deprioritized]** Bronze layer unification: my `sync_schwab_onedrive_to_s3.py` still writes raw to `opal-data-schwab/01_raw/`. Andrew's directive favors full unification but doesn't strictly require bronze move. Defer until/unless explicitly requested.

## Deployment Tags

N/A — no Lambda / EC2 / Terraform changes this AE session. Pure S3 sync ops. DS~D Phase 3 commit will not bump `bd-vX.Y.Z` either (bronze/silver/gold .py edits don't tag; bronze-silver-gold layer evolution is per-commit, not per-tag).

## Verification

| Phase | Evidence | Status |
|---|---|---|
| 2-RPS sync | `aws s3 sync` exit 0; tail thru `date=20260508/` | DONE |
| 2-ULN sync | exit 0; tail thru `date=20260508/` | DONE |
| 2-ACC sync | exit 0; tail thru `date=20260508/` (new prefix) | DONE |
| 2-TRN sync | exit 0; tail thru `date=20260508/` (new prefix) | DONE |
| 3.5 yaml edit | working-tree diff captured; rerouted to DS~D | DONE |
| 4 static commit scope | `7c030faee` 11-file scope confirmed | DONE |
| 4 idempotent re-run | 4 converters exit 0; already-converted counts query canonical | DONE |
| 4 negative test | drifted bucket mtimes unchanged post-rerun (no writes to drifted) | DONE |
| 5 RAVC close | sent to DS~D + COO 19:15Z | DONE |
