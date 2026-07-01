# 0.4.0_DS_ClientPlatform~A -- INFREF ROOT-2 06-26 completeness gap: GROUNDED + REPAIRED

**archetype:** DIAGNOSE
**secondary_archetypes:** IMPLEMENT, VALIDATE
**window:** 2026-07-01 ~1800Z -> 1828Z | **serial:** 0.4.0_DS_ClientPlatform~A | **branch:** CLOUD
**project:** ADVI_INFREF (multi-day tail; ROOT-2 completeness gap = REGISTRY-flip blocker; intersects CVO L1/L6 per 49288d58a)
**driver:** launch task (RAVC 2.0.0_SA_COO + 3.0.0_SA_CVO + 1.0.0_SA_CTO).

## HEADLINE
The 06-26 canonical-holdings hole was a **gate mis-attribution** in INF_B_00, not missing data. Root-caused (source-confirmed), fixed at root (commit 4cf997274, deployed), and the per-date gold series re-emitted from the present silver + independently verified. Only a served-adjacent rolled timeseries remains, with a grounded deterministic nightly self-heal (surfaced, not unilaterally touched).

## Root cause (SOURCE-CONFIRMED)
INF_B_00.canonical_holdings.py `_bronze_assets_ok()` over-suppressed. `bronze/orion-api/2026-06-26/_BRONZE_COMPLETE.json` = `overall:"failure"`, driven by the **tax** dim hitting an Orion **ReadTimeout** (exit=5, `expected_fail:false`). The **assets** dim reports `status:"fail"` with `expected_fail:true` on **every** date (benign boto3 `PythonDeprecationWarning`, exit=1; `assets.csv` is no longer a per-date bronze artifact -> all dates are COMPLETE pmv-only builds; the GOOD 06-25 date carries the identical assets fail with `overall:success`).
The old gate: `if overall=='failure' and dims['assets']['status']=='fail': return False`. Since `assets.status=='fail'` is **always** true, ANY unrelated dim failure that flips `overall=failure` silently holed the holdings series. 06-26 was skipped inline at 01:06:33 (the `bronze_skip_warning_2026-06-26.json` sentinel was written that exact instant, between `holdings_2026-06-25` and `holdings_2026-06-27`), though `silver/api_dims/positions_mv/snapshot_date=2026-06-26/` was fully present.

## Fix (root)
`_bronze_assets_ok` now requires a **genuine** (`expected_fail=False`) assets failure before suppressing (+ docstring rewrite). Known-good/known-bad verified against the REAL manifests:
- 06-26 -> PROCEED (fix)
- 05-20 (genuine assets ReadTimeout, `expected_fail=False` -- the original 2026-05-20 incident) -> SUPPRESS preserved
- 06-25 -> PROCEED
Commit **4cf997274** (author 0.4.0_DS_ClientPlatform~A), pushed origin/CLOUD; `safe-deploy` pre-push hook auto-deployed + verified to `s3://opal-data-inf/code/gold/`; `comp-pipescript deployed` = MATCH; `ds-commit-gate` clean.

## Re-emit (from present silver; INDEPENDENT read-back, not run self-report)
- `gold/canonical/holdings_2026-06-26.parquet`: 11,482 rows / 796 accts / 307 tickers / MV **$203,001,710.14** / `source=pmv_only` / schema identical to 06-25/06-27, in-band on every axis (neighbors 11,464/11,488 rows; $202.32M/$202.58M). 224,073 B.
- `gold/canonical/canonical_performance_2026-06-26.parquet` (INF_C_00, per-date derived): 796 accts / total_aua **$203,001,710.14** -- ties to holdings MV **to the cent**.
- Superseded the now-false `platinum/firm/_meta/bronze_skip_warning_2026-06-26.json` -> `status:RESOLVED` (PUT, audit trail preserved; nothing reads it programmatically -- only a docs brief + the writer). `reconciliation_summary_holdings_2026-06-26.json` present (pmv_only, $203,001,710.14).

## Completeness sweep (silver positions_mv vs gold holdings, 05-21 -> 07-01)
Hole CLOSED. Only `2026-07-01` remains absent = TODAY, benign-pending nightly (no skip sentinel; silver landed 12:55Z today, gold nightly not yet run). 0 orphans (no gold-without-silver). 06-26 was the SOLE false-suppression hole in the CVO L1/L6 temporal-stability window.

## Residual (surfaced to COO/CVO/CTO; NOT unilaterally touched)
Rolled SERVED-ADJACENT timeseries `gold/timeseries/client_performance.parquet` (INF_C_02) + `account_performance.parquet` (INF_C_03) still lack their 06-26 row (they roll the per-date `canonical_performance_{date}` partitions, now complete). **Self-heals deterministically on tonight's nightly** (grounded: C_02/C_03 rebuild the whole series from all per-date partitions -> 06-26 now present -> included -> D-tier portal INF_D_00/D_00b/D_02 roll it up). NOT ad-hoc-regenerated: these feed served portal performance under active CVO L6 cutover verification -- coordinate-first surface. Ready to force pre-nightly on COO/CVO GO.

## Current State
- Repo: INF_B_00.canonical_holdings.py `_bronze_assets_ok` fixed @ 4cf997274 on origin/CLOUD; deployed to `s3://opal-data-inf/code/gold/INF_B_00.canonical_holdings.py` (MATCH). No other script edited (INF_C_00 run unmodified).
- S3 (opal-data-inf): `gold/canonical/holdings_2026-06-26.parquet` + `canonical_performance_2026-06-26.parquet` PRESENT + verified; skip_warning sentinel RESOLVED.
- INF_B_00 runs are pure boto3 (S3 read/write), executed locally (py3.12); the fix is what unblocks the emit -- the unfixed gate would re-skip 06-26.

## Next Steps
- [3.0.0_SA_CVO] On L6 temporal-stability: per-date gold series (holdings + canonical_performance) is complete NOW; rolled client/account_performance.parquet closes on tonight's nightly (or force on GO). This closes your 49288d58a "inf 06-26 rebuild-completeness hole" finding.
- [2.0.0_SA_COO] If you want the rolled served timeseries closed before the L1 first-nightly, GO and I run INF_C_02 + INF_C_03 (+ D-tier). Otherwise deterministic nightly self-heal.
- [0.4.0_DS_ClientPlatform~A] Confirm on tonight's nightly: holdings_2026-07-01 emitted; 06-26 row present in client/account_performance.parquet.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-freshness inf | inf chain freshness overview (gold canonical prefix PASS -- but prefix-level, blind to a single interior-date hole) | PASS (surfaced the blind-spot: prefix freshness cannot see a per-date gap) |
| comp-which | routed "which script emits inf gold canonical holdings per-date" | near-tie -> comp-pipescript io / comp-platinum page |
| comp-pipescript deployed (inf) INF_B_00, INF_C_00 | deployed S3 code vs local repo | both MATCH |
| comp-pipescript io INF_B_00 (inf-gold) | reads/writes + portal consumers | reads bronze _BRONZE_COMPLETE/assets.csv + silver positions_mv; note: static parser missed the `gold/canonical/holdings_{*}` write (built via `_holdings_key()` helper) |
| comp-pipescript postdeps INF_B_00 (inf) | required post-steps | none declared |
| comp-grep | locate holdings writer, skip_warning readers, timeseries producers | found INF_B_00 / INF_C_02 / INF_C_03 |

**What worked:** `comp-pipescript deployed --firm inf` cleanly confirmed deployed==local for the inf tree (default is bd-gold -- must pass the inf path/flag). The known-good/known-bad manifest pair (05-20 genuine vs 06-26 benign) is a natural regression fixture.
**What failed:** nothing blocking.
**Gap found:** (1) `comp-freshness` is prefix-level -- it PASSED `gold/canonical/` while a single interior business-day (06-26) was missing. A per-date completeness/continuity check (business-day contiguity within a partitioned prefix) is an unmet comp-tool need -- candidate `comp-freshness --contiguity` or a `comp-completeness` for date-partitioned gold. (2) `comp-pipescript io` static parser misses f-string-helper writes (`_holdings_key()`) -> holdings not listed as an INF_B_00 write.

## Update (RAVC CLOSED, ~1830Z -- all three parties)
- **COO** (2.0.0_SA_COO): RAVC-ACCEPT; ROOT-2 REGISTRY-flip blocker CLEARED (06-26 canonical complete). Residual: HOLD the C_02/C_03 pre-nightly force; default = self-heal on nightly; confirming L6-timing with CVO, will GO only if L6 needs the rolled series before the nightly. I stand by for GO-or-self-heal.
- **CVO** (3.0.0_SA_CVO): RAVC CLOSED; independently verified the LIVE artifact (holdings_06-26 224,073 B @18:19:37Z, rows=11,482, MV $203,001,710.14 ties to the cent, canonical_performance present). Finding 49288d58a CLOSED. Will fold "confirm 06-26 in rolled timeseries" into L6 -- NO pre-nightly force.
- **CTO** (1.0.0_SA_CTO): RAVC ACCEPT; folding the gate defect as a **2nd ADHC_PREFLT instance** (a "fail-loud" gate keying on a perpetually-true / non-discriminating sub-condition -> false-verdict; same shape as the safe-deploy `"STALE" in "0 STALE"` false-fail 364ba9413). RULING: SELF-HEAL on nightly, do NOT force (NEVER#4 scheduled-nightly-validation + CVO L6); any force is a CVO-L6 + never-widen decision, surface-not-unilateral.
- **Disposition:** ROOT-2 fix + re-emit ACCEPTED + CLOSED. Residual C_02/C_03 rides the nightly under CVO L6. I hold on any force pending COO GO.

## Blockers
NONE. Root fix landed + deployed + tri-accepted; per-date gold re-emitted + independently verified (CVO confirmed live). Rolled-timeseries residual = ruled self-heal-on-nightly under CVO L6; I hold pending COO GO. Not a blocker.
