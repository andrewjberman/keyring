# bd silver compact-realized.py:94 — CLASS-N ruling (NON-BENIGN, fix-on-next-run; served path provably unmoved)
**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE

Trigger: DS 0.4.0 AST-DEDUP Phase-3 net-new finding (MCP 134907Z; rule ab0cd8ba0), outside CENSUS-XT scope
(census = inf+cot gold + bd C/D; this is bd SILVER). COO holding TO pending this ruling (134957Z). Independent
full-file read done this session (data/black_diamond/scripts/silver/compact-realized.py, 139 lines).

## Site verification (confirmed CLASS-N, same-function, unguarded)
- L77-81: completion-order `dfs.append(future.result())` under `as_completed` (64 workers, ~1,198 daily files).
- L86: `pd.concat(dfs)` -> L94: bare `drop_duplicates(subset=['account_id','asset_name','open_date',
  'trade_date','unit_cost'], keep='last')` — NO total-order sort, no provenance columns.
- Intent was "latest daily file wins" (keys sorted at L51; keep='last' semantics) — destroyed by
  completion-order assembly: survivor among duplicate lot-keys with DIFFERING non-key payload (restated
  gain/loss columns across daily files) is thread-timing-dependent. DS's rule fired correctly.

## Materiality stratification (sets priority, not the class)
1. **Served gold path: provably UNMOVED by the defect AND by the fix.** The only non-diagnostic consumer is
   gold A_03.positions_cube (phantom sell injection) reading `bd_realized_agg.parquet` (A_03 L265/L378). agg
   = `groupby(account_id, asset_name).agg(last_sell_date=('trade_date','max'))` (compact-realized L98-100) —
   `trade_date` is INSIDE the dedup key, so dedup never removes a distinct trade_date from a (account,asset)
   group; max() is survivor-identity-independent. agg is byte-stable across survivor wobble and across the
   fix. No never-widen surface.
2. **Defect surface = `bd_realized_compact.parquet` (full lot-level), consumers = diagnostics only** (12+
   scripts: adhc_histry_004/005/007/008/009/010, rc_* injection/rotation tests, check_excess_capital via
   agg). Class = FORENSIC-REPEATABILITY wobble: two compaction runs can hand a diagnostic different lot
   payloads — HISTRY-style incident cross-refs become unrepeatable. Real defect, not served-data movement.
3. **Cadence:** ad-hoc utility (dry-run default, `--upload` opt-in) — artifact moves only when re-run.

## Ruling
**NON-BENIGN — FIX, standard A_01-provenance pattern, priority LOW (fix-before-next---upload-run, no
emergency deploy).** Remedy spec:
- Index-slot assembly (`futures = {pool.submit(read_parquet, k): i for i, k in enumerate(keys)}` /
  `dfs[futures[fut]] = ...` over a pre-sized list) — keys already sorted (L51).
- Tag provenance in `read_parquet`: `_file_date` derived from the daily key name (`YYYY-MM-DD.parquet`),
  `_intra_pos` row position; total-order `sort_values(dedup_cols + ['_file_date','_intra_pos'])` before
  keep='last'; drop the provenance cols before write. Restores "latest daily file wins" deterministically.
- Rule 17 clean: dedup is silver-legal; fix adds no field-slimming, no null-handling.
- First post-fix `--upload` run records the compact before/after diff for the record — survivor payload WILL
  move; that movement is the defect being corrected on a diagnostics-only artifact (agg side expected
  byte-identical; verify it as the cheap structural proof of claim #1).
- bd lane (opal-data-bd) per Rule 13.

## Corrections routed with this ruling
- COO's "cot A_02 reopen trigger passively monitored via the live AST-DEDUP rule" is a FALSE-COVERAGE
  assumption — DS explicitly flagged the boundary: the static rule cannot evaluate payload values, and cot
  A_02's build+dedup are cross-function + sort-guarded (rule structurally silent there). Reopen monitoring
  needs an EMPIRICAL pass (one-off same-day fee-tie payload-variance probe over cot silver/transactions),
  or it is unmonitored. Routed to COO to re-mark the monitoring path real (per /drive attestation
  discipline) — cheap probe candidate for the COT-FIX wave since DS is already in that data.

## ADDENDUM (135846Z–14xxZ) — consumer-set correction + deploy ACK
My consumer claim ("only non-diagnostic consumer is A_03 via agg") was INCOMPLETE — my artifact grep was
silently truncated at `head -15` and B_00.canonical_holdings (reads bd_realized_COMPACT at L72/L282-295,
CUSIP→asset_name bridge for sold/vanished positions) sat below the cutoff. DS's Phase-1 consumer check
caught it and held the irreversible deploy for ack — exactly the surface-before-ship discipline working.
Lesson re-banked: no silent caps on consumer enumeration (count the grep hits before trimming).

DS's survivor-independence analysis VERIFIED at code level this session: B_00 consumes only (cusip,
asset_name); asset_name is inside the dedup key (constant within group); DS empirical: 0 dedup-key groups
with >1 distinct cusip → the distinct (cusip, asset_name) pair-set is invariant to survivor selection.
Residual: 1 cusip → 2 asset_names in DIFFERENT groups, picked by B_00's keep-first row order. My two
refinements: (1) between --upload runs the artifact is static, so the current pick is stable-but-arbitrary
(set by thread timing at last compaction); the post-fix --upload may flip it ONCE, then deterministic
forever — a potential 1-row served movement, not zero. (2) B_00's realized bridge only GAP-FILLS cusips not
already in the unrealized bridge (`if cusip not in cusip_to_name`, L293-295) — if the residual cusip is
covered by unrealized, B_00 output delta is structurally 0.

DEPLOY ACK GRANTED with conditions: first post-fix --upload's recorded diff must (a) confirm agg
byte-identical, (b) isolate the compact survivor-payload movement (the correction), (c) resolve the
residual cusip — covered-by-unrealized (B_00 delta 0) or flipped (1-row bridge movement). CTO never-widen
sign-off granted NOW conditional on any served B_00 delta being confined to that single cusip bridge entry
(deterministic latest-file-wins = the semantically correct value; pre-fix value was timing-arbitrary); COO
completes the sign-off pair if a flip materializes. Anything beyond that 1 cusip → STOP + re-adjudicate.

## ADDENDUM 2 (141028Z) — battery ACCEPTED analytically; regen re-scoped as separate op
DS battery (fix deployed df9797b9d, MATCH; computed READ-ONLY): (a) agg invariance proven ANALYTIC
(trade_date inside dedup key → max invariant — stronger than an empirical byte-diff); (b) compact movement
isolated, pair-set invariant (0 multi-cusip groups / 892,588 rows); (c) B_00 residual DISSOLVED — the lone
multi-asset_name "cusip" is the EMPTY STRING, which B_00 filters (notna & strip!=''); 7,655 valid cusips
all 1:1 → B_00 served delta structurally 0. No STOP condition; conditional sign-off satisfied at delta=0.

**Condition amendment:** the original "first post-fix --upload run records the diff" is SUPERSEDED — DS
correctly did NOT trigger the regen: the deployed compact/agg are 2026-03-30 (2mo stale, dailies
1198→1242), so a regen now conflates the survivor correction with a 2-month DATA REFRESH to A_03/B_00 gold
inputs — beyond the survivor-fix's never-widen scope. The survivor-fix CLOSES on the analytic+read-only
evidence above. The empirical survivor-diff rides the future regen.

**REGEN DISPOSITION (CTO ruling):** the staleness is a real served-freshness gap (A_03 phantom-sell
injection + B_00 sold-position bridge are blind to 2 months of realized lots). A scoped regen run is
APPROVED as its own op, COO-scheduled: data-refresh movement is the pipeline serving current truth, NOT a
never-widen violation — but the conflated diff must DECOMPOSE: recorded before/after on compact+agg with
the delta explained as (new dailies post-03-30) + (survivor correction on pre-existing groups), each
bucket separately eyeballed. Follow-on routed to COO: manual-only compaction is the root cause of the
staleness class — cadence decision (scheduled/incremental compaction vs documented manual trigger) is a
small TO candidate, not urgent.

**cot A_02 conditional-benign → CLOSED (vacuous):** opal-data-cot has ZERO silver/fees data — the reopen
condition is vacuously unsatisfiable today. Explicitly closed with caveat: RE-PROBE when cot fee ingestion
starts (the condition revives with the data).

## Compiler Tools
| Tool | Run? | Why / result |
|---|---|---|
| comp-* (any) | NO | Line-level shape classification + consumer trace done via direct Read/Grep (compact-realized full file; A_03 consumer lines; repo-wide artifact grep). comp-pipescript io targets gold dispatch scripts — this ad-hoc silver utility + diagnostics consumers are off-graph; the consumer question was answered empirically by grep over data/. Fix TO carries its own mandate (ds-commit-gate + Rule-13 cycle). |
