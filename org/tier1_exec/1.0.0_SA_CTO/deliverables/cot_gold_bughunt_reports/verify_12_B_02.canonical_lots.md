# VERIFY #12 -- target: B_02.canonical_lots.py

- is_real: **True**
- confidence: **confirmed**
- corrected_severity: high

## Reasoning
CONFIRMED as a real, currently-firing crash defect (the CRASH branch of the flag), though the flag's alternative SILENT-stale-data branch is refuted.

TRACE (all ground-truthed against live opal-data-cot):
1. The read is genuinely unguarded. B_02.canonical_lots.py:652 `bd_unrealized = _read_s3(S3_UNREALIZED_KEY)` and :674 `bd_realized = _read_s3(S3_REALIZED_KEY)` are bare calls in main(); `_read_s3` (:104-106) has no try/except; the only handler is the top-level wrapper at :850-856 which does `sys.exit(1)`. Line 652 runs first (before build_cusip_bridge at :657 whose realized read IS guarded), so B_02 dies at :652 on the unrealized read.
2. Target keys VERIFIED ABSENT: `aws s3api head-object` on `silver/unrealized/unrealized_gain_loss.parquet` AND `silver/realized/bd_realized_compact.parquet` both return 404 Not Found. Bucket resolves to opal-data-cot (lib/config.py:16 default). cot_silver_merge.py writes `silver/cot_unrealized.parquet`/`cot_realized.parquet` + per-day `silver/{unrealized,realized}/{date}.parquet` (fresh through 2026-07-07) — NEVER the legacy compact keys B_02 reads. B_01._resolve_unrealized_key (:460-482) documents the 2026-03-29 freeze/migration; B_02 was never migrated.
3. Concrete trigger reachable: B_02 is CATALOG line 87 with `--upload`, in CHAIN_CANONICAL/CHAIN_FULL (:139/:147, the dispatcher's documented "Daily run") and GROUP_B, running as PHASE_B4. On any such invocation main() reaches :652 → s3.get_object raises NoSuchKey → uncaught → sys.exit(1). Chain runner hard-fails on non-zero exit (wait_phase :359 `exit 1`; serial run_chain under `set -e`), so B_03/C/D in that invocation would not run.
4. Live evidence the crash is ALREADY active: B_02 served outputs gold/canonical/lots_unrealized/ and lots_realized/ are EMPTY (never written); B_03 account_gains/ (PHASE_B5, downstream of B_02) is frozen at 2026-06-09 (last date the chain completed through B_02); B_00 holdings/ (PHASE_B1, upstream) is fresh 2026-07-07. This is the exact signature of execution dying at B_02 since ~06-09 (legacy keys deleted after the last 06-09 full run).

REFUTED sub-claim: the reviewer's SILENT scenario (bd_unrealized = the frozen 2026-03-29 snapshot, emitting stale BD-only lots) does NOT occur — there is no frozen object; the key is deleted, so it crashes rather than serving stale data. The dominant, verified failure is the hard crash.

SEVERITY: corrected to HIGH (critical is defensible). It is a deterministic, currently-firing hard crash that leaves two canonical tax-lot tables entirely absent on served and freezes B_03 account_gains since 2026-06-09, and it WOULD abort the entire downstream if `--chain full`/`--chain canonical`/`--group B` is run. Tempering to high (not critical): the operational nightly evidently already routes around B_02 (platinum/firm + account_performance + partner_analytics are all fresh 2026-07-07 while B_02/B_03 are stale), so the catastrophic whole-chain-abort is currently masked; and for COT the tax-lot/gains branch is a degraded secondary product (empty advisor layer per pipeline context), bounding the live blast radius to the lots tables + account_gains rather than the primary served AUA path. Fix direction (report-only): migrate B_02 to the per-day partition resolution B_01 already uses (nearest-on-or-before silver/{unrealized,realized}/{date}.parquet) and/or guard the reads, mirroring build_cusip_bridge's try/except at :164-179.
