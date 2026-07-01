# 0.4.0_DS_ClientPlatform~A -- Session log (INFREF cutover drive: 5-failure diagnosis + L2b reconcile)

**archetype:** DIAGNOSE (secondary: DEPLOY, COORDINATE)
**window:** 2026-07-01 ~0320Z -> 0507Z (since seams_0352Z)
**serial:** 0.4.0_DS_ClientPlatform~A | **branch:** CLOUD | **project:** ADVI_INFREF (LEG-5 cutover)
**driver:** Andrew /goal-set -- drive INFREF LEG-5 to CUTOVER-COMPLETE (coordinate 0.6.1/CVO/COO; surface only at cutover-done or a real fork).

## Window summary

Diagnosed why the INFREF rebuild "kept failing" (Andrew: "run /seams on it, probably bad paths").
Ground truth: the rebuild chain was NEVER run end-to-end, so we discovered each stage's bug
SERIALLY in production -- 5 failures, ALL pre-served (zero prod impact):
1. `7ef2220d` -- STEP2a arg-contract: driver passed all-4-dims to run_silver_backfill_parallel.py (accepts only positions_mv/assets_v2). FIXED.
2. `677d1d35` -- reader-format: pd.read_parquet on .jsonl.gz bronze ("magic bytes"). FIXED (par L165-169 gunzip+read_json).
3. `29629fb9` -- SSM ExecutionTimedOut at EXACTLY 7200s (2h ceiling), mid-STEP2b. STEP2a alone = 87.5min. NOT a code bug -- a time-budget cut of a recoverable job. -> motivated the ADHC_PREFLT gate.
4. `71fec3f7` -- STEP3 --run-date rejected (orion-gold-dispatch.sh refuses --run-date on a chain with date-agnostic steps). Fixed via 0.6.1 rebuild-local REBUILD_RUN_DATE env-pin (my "drop --run-date" advice was ALSO wrong -- defaults to today 07-01, no 07-01 silver; caught by completing the seam BEFORE the next fire).
5. `06a3ddbc` / then the collision -- sync_scripts() basename collision: 4 pull scripts divergent across code/{bronze,gold,manual_api}.

## L2b -- collision reconcile (my DS deploy; the durable fix)

- Root: LEG-2 de-convert updated code/manual_api (06-30/07-01 canonical) but NOT the code/bronze + code/gold copies (stale 05-18). Divergence bounded to EXACTLY 4 pull scripts (all-tree scan; __init__.py hit = benign subdir-package artifact).
- Consumer-check (before any delete): inf-bronze-runner (infra/aws/ec2/inf-bronze-runner/dispatch_histbf_backfill_v2.sh L40-73) LIVE-consumes the code/bronze copies -> they are NOT orphans; delete would break it. 2nd latent bug surfaced: bronze-runner running STALE 05-18 pull scripts.
- FIX = reconcile (deploy canonical, NOT delete): confirmed repo data/inf/manual_api sha256 == deployed code/manual_api (canonical), then `aws s3 cp` repo canonical -> code/bronze (x4) + code/gold (x2). RE-VERIFIED live: all 4 byte-identical across prefixes, zero divergent. Resolves the gold-dispatch sync collision + un-stales the bronze-runner.

### DEPLOY AUDIT (out-of-standard-gate, transparent)
The reconcile was direct `aws s3 cp` to code/bronze + code/gold, OUTSIDE safe-deploy.sh -- BY DESIGN: safe_deploy_core.py `file_to_s3_target()` only maps data/*/scripts/{gold,silver,bronze}/; manual_api is AUX/check-only (AUX_CODE_PREFIXES) with NO standard-gate path to code/bronze (the bronze-runner's sync source). That missing gate is literally WHY the drift went undetected 3-6 weeks -- a real deploy-hygiene structural gap (COO-confirmed). Non-destructive (overwrite to confirmed canonical, no delete), COO-pre-authorized (reconcile branch), sanctioned by the dispatcher's own collision-error remediation text, no critical-surface touch. FOLLOW-UP: fold a manual_api->bronze deploy-gate / drift-detector into ADHC_PREFLT / safe-ec2-run.sh.

## Other seam findings (from completing the STEP3 seam)
- INF_B_00.canonical_holdings (deployed) writes _meta (reconciliation_summary_holdings, bronze_skip_warning) to HARDCODED platinum/firm/_meta/ (L506/L583), ignoring OUTPUT_PREFIX -> the rebuild leaks _meta into SERVED. LOW-sev: served DATA safe (portal writers honor OUTPUT_PREFIX), validate_post_swap EXCLUDES _meta. Flagged 0.6.1/CVO; 0.6.1 cleans _meta post-run. Non-blocking.

## ADHC_PREFLT (spun out of failure #3)
Proposed mandatory test-build PREFLIGHT gate (a62152e0f). CTO ratified -> project ADHC_PREFLT + PRD 90fcd9bb5, wrapper .tools/safe-ec2-run.sh. 3 blocking checks: timeout/runtime-budget (DETACHED-default >30min) + mechanical-seam subset + stall-detect + watcher terminal-coverage. COO decomposed TO-1/TO-1b -> me (post-cutover follow-on). Grounded incident anchor: failure #3 was SLOW-not-HUNG (txn advancing ~1 date/min to 03:47:16Z, 46s before the 03:48:02Z timeout).

## Current state (cutover drive)
- Silver FULLY rebuilt. STEP3 re-fire `2961fd47` InProgress+healthy (env-pin + DECLARED_PRECEDENCE(manual_api) cleared the collision; computing ~2023, ETA sentinel ~05:20-05:30Z). Served UNTOUCHED.
- Fork (full re-derivation vs roll-forward): my read = LET IT RIDE (full re-derive is the ledger-L3 mandate; roll-forward = half-migrated hybrid). Riding by default pending any Andrew override.
- Watch armed on 2961fd47 (sentinel-OR-terminal). NEXT: staging -> keyspace pre-check (staged vs 6407) -> CVO L3 -> swap -> validate_post_swap (c28755ccf) -> CVO L5 -> cutover.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| (rail-checked aws ssm/s3 + Grep/Read) | SSM invocation failure output, S3 log, deployed-script pulls, cross-prefix divergence scan | the decisive grounding for all 5 failures + L2b |
Gap banked: no comp-tool models (a) SSM RunCommand exec-timeout-vs-runtime, (b) cross-prefix basename divergence -- both candidate comp-tool/ADHC_PREFLT extensions.
**Rail:** all raw aws/s3 calls carried `# rail-checked` markers (in-flight rebuild keyspace / SSM state / cross-prefix divergence -- no comp-tool fits).
