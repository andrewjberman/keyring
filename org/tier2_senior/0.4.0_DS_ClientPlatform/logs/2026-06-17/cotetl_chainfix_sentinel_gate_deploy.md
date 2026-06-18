# ADVI_COTETL.CHAINFIX -- emit_silver_sentinel gate-semantics fix DEPLOYED (cot silver->gold chain unblocked)

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, DIAGNOSE, VALIDATE

> Handoff for a zero-context reader.

## Current State
ADVI_COTETL.CHAINFIX is **DEPLOYED + byte-verified** on the cot silver tree (commit **864139e7a**, CLOUD).
This fixes the cot silver->gold EVENT chain, which had NEVER auto-fired in production (cot gold/platinum
frozen since 6/9).

**Root cause** (AE 145519Z): `emit_silver_sentinel` gated on `{silver_prefix}/{run_date}.parquet` EXISTS.
But CurrentDay tables (allocations 6/5, unrealized 6/9) write their **BD-stamped data date != run_date**,
and a frozen table is not rewritten at all -> `{run_date}.parquet` never existed -> `silver_complete.json`
never emitted -> `cot-silver-complete` EventBridge never fired -> gold never ran.

**Fix** (`data/cot/scripts/silver/cot_silver_merge.py`; gate-EMISSION semantics ONLY):
- New explicit per-run success signal: `incremental_merge` stamps `manifest['last_successful_run']` on a
  successful table run -- **including the frozen/no-new-files no-op** (new helper `_mark_table_run_complete`
  on the two early-return success paths) -- but **NOT** when any target file fails (new `failures` counter;
  `last_successful_run` advanced only when `failures == 0`). This closes today's **fail-OPEN** (the loop
  reached `save_manifest` even on a per-file failure -> a silently-failed table could read as complete).
- `emit_silver_sentinel(run_date)` now gates on each gated table's `last_successful_run` being present AND
  within `_SENTINEL_RUN_WINDOW_HOURS` (12h) of `--finalize`, **replacing** the `{run_date}.parquet`
  `head_object` check. Recency-window (not exact-date) is robust to a midnight-straddle + excludes a stale
  prior-run stamp; checks run-completion recency NOT data-freshness -> decoupled from the freshness gate.
  Self-contained (the manifest is already S3-backed via `save_manifest`/`load_manifest`), no SSM/AE-leg dependency.

**All 4 CTO conditions met:** (a) fail-closed (proven by test); (b) cot-local, 0 bd/shared import;
(c) Rule 17 -- gate-emission + manifest bookkeeping only, `process_xlsx_to_parquet` transform untouched,
0 silver-content change; (d) decoupled from the freshness gate -- fires on a present-but-frozen-but-PROCESSED
snapshot. CTO architecture sign-off IN (235316Z); COO GO (234651Z).

**Phase-1 falsified the GO's named signal:** COO's GO named "S3 parquet LastModified-in-window." Phase-1
(read-only) proved `incremental_merge` SKIPS-on-unchanged (early-returns at L357/L368 without rewriting the
parquet on a frozen file) + the parquet is keyed by BD `file_date` (L309) not run_date -> a frozen-but-processed
table keeps an OLD LastModified -> misreads "not processed" -> breaks cond (d). CTO predicted this; switched to
the explicit manifest stamp (CTO+COO concurred).

## Deployment Sequence + Verification
1. Edits (helper + stamp + window const + sentinel gate) -> `python -m py_compile` -> **PY_COMPILE_OK**.
2. Synthetic fail-closed test (standalone, removed after): EMITS on all-fresh; HALTS on stale(13h)/missing
   stamp; advances stamp on clean-run + frozen no-op; does NOT advance on a failed file (both CTO classes ->
   `(None,0)`). **RESULT: PASS.**
3. `.tools/ds-commit-gate.sh cot_silver_merge.py` -> `All checks passed! OK: pre-commit gate clean` (no
   bd-fork ruff debt on this cot script -- unlike the COT_RULE15 gold scripts).
4. Phase-2 diff re-read -> gate-emission + manifest-bookkeeping only, 0 silver-content lines (Rule 17 / cond c).
5. `.tools/safe-commit.sh --author 0.4.0_DS_ClientPlatform ...` -> commit **864139e7a**.
6. `git push origin CLOUD` -> safe-deploy hook: `DEPLOYED [cot] data/cot/scripts/silver/cot_silver_merge.py`
   / `OK: safe-deploy gate PASS -- all files deployed and verified`. Push `f24d20c08..864139e7a CLOUD -> CLOUD`.
7. **Independent md5 verify** (never-trust-rc=0): `md5sum` local == `s3api head-object` ETag:
   `5533c1e348578ea68427fe18284e7a3e` == `"5533c1e348578ea68427fe18284e7a3e"` at
   `s3://opal-data-cot/code/silver/cot_silver_merge.py`. **Byte-match.** Single push==deploy, fully landed
   in-session, no stranded legs.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| Read (cot_silver_merge.py:191-544: sentinel, incremental_merge, process_xlsx_to_parquet, load/save_manifest, main) | molecule the sentinel + write path; find the skip-on-unchanged discriminator | CONFIRMED skip-on-unchanged -> LastModified OUT |
| Grep (`^import`/`black_diamond`/`sys.path` in cot_silver_merge.py) | condition (b): cot-local, no bd/shared import | PASS -- stdlib+boto3+pandas, 0 bd import |
| python (standalone synthetic fail-closed test, then removed) | prove gate emits/halts + stamp fail-closed on both failure classes | PASS -- all 6 assertions |
| `.tools/ds-commit-gate.sh` (cot_silver_merge.py) | py_compile + AST + ruff py39 FA | PASS |
| git diff (phase-2) | Rule 17 / cond c -- gate-emission only, 0 transform change | PASS |
| `.tools/safe-commit.sh` + push (safe-deploy) + `aws s3api head-object` | atomic deploy to cot silver S3 + independent md5 verify | PASS -- ETag == local md5 |

What worked: code-ground-truthing the skip-on-unchanged behavior in phase-1 falsified the GO's LastModified
signal BEFORE building on it (CTO's verify-the-real-layer-not-a-proxy theme). What failed: nothing. Gap: none.

## Blockers
None. Implement+deploy complete + verified. Phase-3 happy-path (sentinel emits + EventBridge fires gold) is
event-driven next-morning off tonight's scheduled cot silver nightly -- by design (validate-on-nightly, no ad-hoc run).

## Files Modified
See commit **864139e7a** (rationale embedded). One file: `data/cot/scripts/silver/cot_silver_merge.py`
(+`_mark_table_run_complete`, `_SENTINEL_RUN_WINDOW_HOURS`, `incremental_merge` fail-closed stamp,
`emit_silver_sentinel` gate predicate).

## Next Steps
1. **[self, event-driven NEXT-MORNING]** CHAINFIX phase-3 off tonight's scheduled cot silver nightly: confirm
   `silver/{date}/_meta/silver_complete.json` emits + `cot-silver-complete` EventBridge fires gold (chain
   auto-fires 1st time since 6/9) + gold/platinum advance. Report to [2.0.0_SA_COO] (CC [1.0.0_SA_CTO]) to
   CLOSE ADVI_COTETL.CHAINFIX. If sentinel still doesn't emit -> stamp predicate wrong; if a failed table
   emits -> fail-closed broken (won't, per test, but verify on the real run).
2. **[self, event-driven NEXT-MORNING]** ADVI_NNAATTR.TO-1 served-verify off tonight's nightly (separate
   thread; cross-route byte-equality on the FIXED route f24d20c08; CVO+CTO co-sign).
3. **[1.0.0_SA_CTO + Andrew]** (B) the cot BD-freeze determination (pre-partner-live? frozen ~6/9) -- separate
   open item, decoupled from this fix; the freshness section keeps it visible meanwhile.
