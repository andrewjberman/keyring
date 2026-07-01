# SEAM: inf_rebuild_step23.sh (SSM 29629fb9) -> STEP2 silver-backfill -> STEP3 gold-compute staging   (scale: MACRO)
**archetype:** DIAGNOSE (secondary: VALIDATE, TRACE)
**invoked:** Andrew-direct ("run /seams on it, probably bad paths or something dumb") 2026-07-01 ~0350Z
**serial:** 0.4.0_DS_ClientPlatform~A

## Seam definition
- **Side A (producer/driver):** `inf_rebuild_step23.sh` (deployed s3://opal-data-inf/code/rebuild/, LastMod 01:34:56Z), run via SSM RunCommand 29629fb9 on i-0ed5afded2ebd4ed4.
- **Side B (sinks):** LIVE silver (STEP2a positions_mv/assets_v2 via run_silver_backfill_parallel.py; STEP2b transactions/performance via run_silver_backfill.py -> convert_*_to_silver.py) then staged gold/platinum (STEP3 orion-gold-dispatch.sh --stage compute -> platinum/_rebuild/{ts}/ + _REBUILD_STAGED.json sentinel).
- **Boundary:** the SSM command execution window + the arg-contract/reader-format between the driver and each backfill script.
- **Expected contract:** the driver runs STEP2a -> STEP2b -> STEP3 to completion inside one SSM invocation, staging a full rebuilt platinum tree + writing the sentinel. Recorded in the deploy ledger `20260630T2035Z_advi-infref-cutover-rebuild` (leg L3 = the CVO parity input this must produce).

## Axis verdicts
| Axis | Verdict | Evidence | Delta |
|---|---|---|---|
| MECHANICAL | **FAIL** (3rd mode; 2 prior fixed) | v3 29629fb9 ExecutionEnd 03:48:02.752Z = EXACTLY 7200.0s after Requested 01:48:02Z = the 2h SSM exec ceiling; Status=TimedOut. STEP2a ate 5250s/87.5min (log "elapsed=5250.0s / STEP2a exit=0"), leaving ~1950s for STEP2b+STEP3 -> timed out mid-STEP2b. | contract="runs to completion in one window"; reality="full-history rebuild > 2h, cut off mid-STEP2b" |
| DECLARATIVE | **FAIL** (stale docstring) | `run_silver_backfill.py` L3 docstring: "converts historical bronze **parquet** partitions to silver" -- but BRONZE_PATHS (L55-59) are all `.jsonl.gz` and the actual readers (convert_*_to_silver.py) gunzip+read_json. Also `convert_transactions_to_silver.py` L250 retains a `pd.read_parquet` path alongside the L275 jsonl.gz path (dual-reader residual; not on the failing path). | believed "parquet reader"; actually jsonl.gz reader (map drifted) |
| SEMANTIC | **UNVERIFIED** (nothing staged) | STEP3 never ran; platinum/_rebuild/{ts}/ = 0 keys, sentinel absent. No staged payload exists to value-check. Served/platinum UNTOUCHED (LastMod 06-30 17:16Z) = zero served risk. | n/a until a clean stage exists |

## The three attempts (why it "keeps failing")
1. `7ef2220d` 01:32Z -- **arg-contract mismatch**: driver called `run_silver_backfill_parallel.py --dims (all 4)`; that script's argparse choices = {positions_mv, assets_v2} only -> "invalid choice: 'transactions'", exit 2. FIXED (driver split: STEP2a parallel 2 dims, STEP2b sequential txn+perf).
2. `677d1d35` 01:35Z -- **reader-format mismatch**: parallel reader still `pd.read_parquet` on `.jsonl.gz` bronze -> "Parquet magic bytes not found in footer" on positions_mv 2020-06. FIXED (par L165-169 gunzip+read_json, deployed 01:47:41Z, 14s before v3).
3. `29629fb9` 01:48Z -- **SSM ExecutionTimedOut** at the 2h ceiling, mid-STEP2b. NOT a code bug: STEP2a completed clean (err=0); the rebuild simply exceeds one command window. OPEN.

## Knowledge-parity delta
- BELIEVED (0.6.1 @03:47Z, relayed to Andrew): "rebuild HEALTHY + advancing, STEP2b done ~04:03Z, sentinel ~04:10Z." TRUE at 03:47Z; the command TimedOut 46s later @03:48:02Z. The reported ETA never occurred.
- BELIEVED (my prior session + status to COO): "rebuild riding, on-track." TRUE while running; the 2h ceiling was the unseen structural cap.
- TRUE: v3 dead (TimedOut), STEP2b froze at txn 2026-06-14 (mtime 03:47:16Z last write), STEP3 never ran, no sentinel will ever come from this command. Live silver partially rebuilt (positions/assets full via STEP2a; txn/perf partial to ~06-14) and likely NOT snapshot-rolled-back (SIGKILL skipped the L52 handler). Served safe.

## Verdict
**BROKEN@MECHANICAL** -- the rebuild chain does not carry to completion: the full-history STEP2 backfill (STEP2a 87.5min + STEP2b) plus STEP3 exceeds the 2-hour SSM execution ceiling; v3 cut off mid-STEP2b. The two earlier path/reader breaks are fixed; this third break is a time-budget/structural boundary, not a bad path.

## Fix (routed to 0.6.1_AE -- AE owns the rebuild SSM)
1. FASTEST: re-fire same driver with a larger execution timeout (~4-6h). STEP2a's silver is already converted this session -> re-run fast-skips it (VERIFY run_silver_backfill.py skips converted dates first), leaving the budget for STEP2b+STEP3.
2. ROBUST: split STEP2a / STEP2b / STEP3 into separate SSM commands (idempotent + --resume); STEP2a is done, so only STEP2b + STEP3 remain.
Pre-fire: confirm the partial live-silver state (STEP2b interrupted, no rollback) is value-consistent before the next nightly gold consumes it.

## grounding: (Rule 22, per causal claim)
- "v3 died on the 2h SSM exec ceiling" -- **SOURCE-CONFIRMED**: `aws ssm get-command-invocation` Status=TimedOut/ExecutionTimedOut + ExecutionEnd 03:48:02.752Z - Requested 01:48:02.522Z = 7200.0s (live API).
- "STEP2a consumed the budget" -- **SOURCE-CONFIRMED**: v3 S3 log rebuild_step23_20260630T234458Z.log "DONE ... elapsed=5250.0s / STEP2a exit=0" @03:15:36Z.
- "STEP2b froze at 06-14" -- **SOURCE-CONFIRMED**: silver/transactions/2026-06-14.parquet LastMod 03:47:16Z (last write); 06-20/25/30 carry pre-rebuild on-date mtimes.
- "snapshot-restore likely did NOT run" -- **INFERRED (live-state-only)**: SIGKILL-on-timeout skips the bash L52 handler; not source-traced on this box. Non-actionable claim -> VERIFY the live silver state before relying on it.

## Residual / unknowns
- Exact live-silver consistency after the interrupted STEP2b (rollback ran? partial-but-value-consistent?) -- must be checked before the next nightly gold run.
- Why STEP2a is 0.9 tasks/s (each ~18s) -- the deeper throughput constraint making the full rebuild a multi-hour job.
- convert_transactions_to_silver.py L250 residual read_parquet path -- is it dead or a live alt-input? (declarative cleanup, not on the failing path).

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| comp-which (implicit via HUD) | routed freshness/inspection nudges | rail-checked several aws calls -- no comp-tool models SSM invocation state or an in-flight rebuild silver keyspace |
| (raw aws ssm/s3, rail-checked) | SSM status/timing, S3 log, silver leading-edge mtimes, deployed-script pulls | the decisive grounding for the timeout root cause |
Gap: no comp-tool surfaces SSM RunCommand execution-timeout vs actual-runtime -- a candidate comp-freshness/comp-aws extension for long-running rebuild commands.
