# D_00f series-tie + cot_transactions dup-header: two silent freezes root-caused, fixed, deployed

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, DEPLOY, VALIDATE

## Window
2026-06-18 ~1241Z -> ~1310Z. Fresh session (was OFFLINE ~10.4h). First log of session.
The two event-driven next-morning verifies on my pending TOs (ADVI_NNAATTR.TO-1 served-verify +
ADVI_COTETL.CHAINFIX phase-3) both surfaced LIVE silent-freeze defects -> turned into fix+deploy.

## Current State (zero-context handoff)

Two independent SILENT producer-freeze defects, both mine (DS code-owner), both FIXED + deployed
byte-verified today, both validate on TONIGHT's scheduled nightly (no ad-hoc gold run).

### THREAD A -- D_00f advisor_nna_canonical silent no-write (CVO P1, COO priority)
- SYMPTOM: `s3://opal-data-bd/platinum/firm/advisor_nna_canonical.json` frozen at 06-17 05:04Z
  (pre-fix vintage) while every sibling `platinum/firm/*` refreshed on the 06-18 nightly. D_00f
  ran heavy (6.1GB, telemetry 05:20Z) then exited WITHOUT writing -> F-0/F-1a NOT live, portal
  serves pre-fix dual-source NNA. CVO independently caught it (close-gate #9) + routed me the P1.
- ROOT CAUSE (exact, from `gold_incremental_2026-06-18_20260618_052024.log` line 2410303): the new
  all-roles+bucket path ran CLEAN (167 entries, 2 bucket rows [49F House, Unassigned], AC-F4b.1
  PASS), then `ERROR W1 partition-completeness ... W6 reconciliation all_pass=False
  (max_abs_delta=0.01, series_tie_max_abs_delta=74213255.51)` -> `sys.exit(1)` at line 886 BEFORE
  the write. rc=1 (the gate correctly refused to publish inconsistent data; the only thing missing
  was a dispatch-level rc!=0 ALARM). NOT an OUTPUT_PREFIX/dry-run misroute.
- WHY: F-2 moved the MAX window to 2021-Q1 (`_build_windows:334`) but left the per-period `series`
  (`_build_period_series`) spanning full inception (2020+). The W6 series_tie invariant
  (sum monthly == leaf MAX) then failed by the 2020 tail = $74.2M. F-2 was incomplete (window
  moved, series didn't).
- FIX (commit **708773e27**): clip the series frame to `windows['MAX'][0]` in
  `_series_block`/`_light_series_block` so series + MAX cover the same period. Restores
  sum(series)==MAX to-the-cent (synthetic validation: delta 18.18M -> 0.00). Matches the FE exactly
  (`ADVI_MAX_WINDOW_ANCHOR_ISO=2021-01-01`; `PartnerAnalytics.tsx:406,423` already filters series
  points to year>=2021) -> ZERO visible FE change. Every emitted window starts >= MAX_start -> no
  chart coverage lost. No transform/content change -- pure F-2 completion. Stale MAX docstring
  (since-inception) corrected.
- WRITE-SENTINEL folded in (CVO unknown-unknown + COO ask): post-write assert OUTPUT_KEY
  LastModified landed THIS run (<=600s) -> a silent no-write/misroute now fails LOUD.
- DEPLOYED byte-identical to `s3://opal-data-bd/code/gold/D_00f.advisor_nna_canonical.py`
  (md5 bbb9fdf94f7a9645d8a58680561f36b7, local==S3).

### THREAD B -- cot_silver_transactions merge-freeze (CHAINFIX phase-3 blocker)
- CHAINFIX gate-semantics fix (864139e7a) WORKS in production: on the 06-18 02:02Z cot silver
  nightly, allocations/realized/unrealized stamped `last_successful_run` but the sentinel correctly
  WITHHELD `silver_complete.json` because transactions did NOT stamp = **fail-closed VERIFIED on a
  REAL failed table** (stronger than the synthetic test the TO asked for; CTO conditions a+d held).
- transactions non-stamp = a 2nd silent freeze (frozen since 6/9). ROOT CAUSE: commit 58b27ad43
  (openpyxl `data_only` read, shipped for the qt1 holdings formula-cell fix) replaced `pd.read_excel`
  -- which auto-mangles duplicate xlsx headers -- with `pd.DataFrame(rows, columns=header)` which
  does NOT. COT TRANSACTIONS_DAILY carries a DUPLICATE raw header 'Tax Status' -> duplicate
  'tax_status' label -> `df[col].dtype` raises AttributeError -> `process_xlsx_to_parquet` returns
  None -> failures>0 every run from 6/12 (7 files 06-12..06-18 unprocessed; processed_files stops
  at 2026-06-09). allocations/realized/unrealized are dup-free so they kept processing.
- FIX (commit **db9521f3c**, pushed in **0d1c8e16f**): `_mangle_dupe_headers()` restores
  pd.read_excel's .1 behavior. Replayed the failing 06-18 file end-to-end -> 3823 rows/71 cols,
  schema BYTE-IDENTICAL to existing compacted silver (tax_status + tax_status_1, 0 missing/0 extra)
  -> compaction-safe. Rule 17 preserved (read-correctness/column-name disambiguation only; the file
  literally could not be read otherwise; zero transform/content change). No-op for dup-free tables.
- DEPLOYED byte-identical to `s3://opal-data-cot/code/silver/cot_silver_merge.py`
  (md5 d8bd6ec363f995815f9f73ef8f04b968, local==S3).

## Files Modified
See commit messages: 708773e27 (D_00f), db9521f3c/0d1c8e16f (cot_silver_merge.py).

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-pipescript io | D_00f.advisor_nna_canonical.py | PARTIAL | Reads (accounts_dim, account_team) correct; WRITES "(none detected)" -- misses the gzip `_write_json_s3` put_object pattern + no portal-consumer surfaced. Got consumers via portal grep instead. |
| ds-commit-gate.sh | D_00f.advisor_nna_canonical.py | PASS | py_compile+AST+ruff FA clean. |
| ds-commit-gate.sh | cot_silver_merge.py | PASS | clean (no bd-fork ruff debt on this silver file, unlike the gold COT_RULE15 case). |
| safe-deploy (push hook) | both | PASS | DEPLOYED [bd] + [cot]; md5 local==S3 byte-verified both. |
| comp-validate | (deferred) | N/A | Served artifacts regenerate on tonight's nightly; can't validate the stale pre-fix artifact. Post-nightly (CVO close-gate). |
| comp-pipescript deployed | (n/a) | SKIP | No gold run triggered (validate-on-nightly). cot is bd-only in this tool anyway (known gap); verified deploy via direct md5. |

- **What worked:** stream-grep of the 240MB gold log isolated D_00f's exact W6/series_tie exception
  (downloaded once locally for iteration; `grep -a` needed for the ✓/✗ unicode). Synthetic replay
  proved both fixes before deploy (series_tie 18.18M->0.00; cot 06-18 file -> schema-identical parquet).
- **What failed:** comp-pipescript io WRITES detection missed the gzip put_object (Thread A) -- the
  D-group writer pattern isn't recognized.
- **Gap found:** (1) comp-pipescript io should detect the `_write_json_s3`/gzip put_object write
  pattern + the platinum portal consumer for D_00f. (2) STRUCTURAL: both freezes were silent because
  a producer that runs heavy then exits rc=1 (D_00f) or returns None per-file (cot) reads as success
  at the dispatch level (no alarm) -- the "never trust rc=0, verify the served artifact" class. COO is
  decomposing the dispatch-level rc!=0 / artifact-landed alarm as a fast-follow TO; the in-D_00f
  write-sentinel only catches the post-write-no-land case (gates exit before it).

## MCP traffic
6 handled. IN: CVO P1 (D_00f stale, full localization) + COO priority (root-cause+redeploy before
tonight's nightly + write-sentinel ask). OUT: ACK to CVO; RAVC2 to COO (both threads); RAVC to CVO
(exact exception + close-gate #9 lands tonight); CC to CTO (COTETL architecture). All addressed to
base serials (no lane suffix).

## Blockers
None assumption-blocked. Both fixes deployed; served verification is event-driven on tonight's
scheduled nightly (validate-on-nightly + no-overnight-watcher, by design -- not a blocker).
Same-day re-run for the D_00f live-staleness = Andrew's call (COO surfacing); I'm ready to support a
targeted D_00f-only re-run IF authorized, but will NOT initiate (cost-governance).

## Next Steps
1. **[self, event-driven NEXT-MORNING]** Verify tonight's nightly: (a) served advisor_nna_canonical
   fresh (06-18+) + cross-route identity (Travis + 2 advisors, all-roles, 49F House + Unassigned as
   own bucket rows, MAX=2021-Q1, nna==inflows-outflows) -> ping **[3.0.0_SA_CVO]** to release
   close-gate #9 -> **[2.0.0_SA_COO]** closes ADVI_NNAATTR.TO-1; (b) cot `silver/{date}/_meta/
   silver_complete.json` emitted + `cot-silver-complete` EventBridge fired gold + gold/platinum
   advanced (chain auto-fires 1st time since 6/9) -> **[2.0.0_SA_COO]** (CC **[1.0.0_SA_CTO]**)
   closes ADVI_COTETL.CHAINFIX.
2. **[2.0.0_SA_COO]** Fast-follow TO: dispatch-level rc!=0 / artifact-landed alarm (the silent-freeze
   structural class) -- AE dispatch leg + the D_00f write-sentinel I shipped.
3. **[2.0.0_SA_COO]** Optional: distinct ADVI_COTETL TO retro-covering the transactions dup-header
   fix (beyond the gate-semantics TO scope, but it was the blocker + my silver lane).
