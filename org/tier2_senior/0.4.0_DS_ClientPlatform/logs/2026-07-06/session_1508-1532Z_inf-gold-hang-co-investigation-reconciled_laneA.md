# INF gold-hang co-investigation (Andrew incremental-steer) — converter-side EXONERATED, reconciled to env-bump
**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, COORDINATE

**Serial:** 0.4.0_DS_ClientPlatform~A | **Window:** 2026-07-06T15:08Z -> 15:32Z | **Driver:** COO [DRIVE] co-investigate + [ANDREW STEER] incremental-chain hypothesis. Co-investigator: 0.6.1 (runtime/dispatcher lead); me (converter/silver side). Delta since c81494033.

## Current State (handoff surface)

Andrew flagged inf AUM stale @07-02 vs Orion 202.58M; DE grounded (live SSM, i-0ed5afded2ebd4ed4) the gold runner HUNG -- "2 --single ASSETS_V2 wrappers (pull+silver) alive at 0 CPU, no full chain." Andrew steer: investigate the INCREMENTAL chain logic first. COO framed my angle = converter-reachability + hang-site.

### The investigation arc (converter side)
1. **Reachability (chain source):** orion-gold-dispatch.sh CHAIN_PULL/CHAIN_INCREMENTAL order = ...ASSETS_V2 (early) ... PERF (late). So a hang at assets_v2 would mean perf is never reached -> env-bump + perf_dim guard would be moot for today. Reported; COO RAVC-ACK'd.
2. **Converter EXONERATED (Rule 22, live S3):** convert_assets_v2_to_silver.py is code/silver MATCH (current, comp-pipescript deployed) AND working -- silver/assets_v2/2026-07-06.parquet exists (written 07-06 10:49:32Z; bronze 07-06 present 09:38Z). The SAME converter produced fresh 07-06 assets silver via the standalone runner. So the gold-chain hang (if real) is EXECUTION-ENVIRONMENT-specific, not converter code.
3. **No-timeout amplifier (grounded, orion-gold-dispatch.sh run_script L580-598):** ONLY INF_API_PULL_* steps are timeout-bounded (`timeout -k30 600s` + tolerate); ALL silver/A/B/C/D steps run with NO timeout. So a hung non-pull step would hang the chain FOREVER. Real robustness gap. COO APPROVED bounding silver steps (durable).
4. **gold_prof.py mechanism (grounded, data/black_diamond/scripts/gold/gold_prof.py -- no data/inf source copy, itself a gap):** the gold chain wraps every step `subprocess.Popen(stdout=sys.stdout) + proc.wait()` (L153-176), NO timeout on wait, inheriting the run_chain|tee pipe. A child blocking on a stdout write (pipe full, reader stalled -- the documented chain #28 do_wait/tee deadlock, L809-813) hangs wrapper+child at 0 CPU. Real-in-principle deadlock class.
5. **0.6.1 DEFINITIVE disambiguation (live, 2 verbatim logs) -- REFUTES the hang-at-assets_v2:** both 07-06 --chain-full logs (chain_full_20260706_133348 + _144739) "FAILED at INF_API_SILVER_PERF (exit=1)" -- the chain RUNS end-to-end, PASSES assets_v2, aborts LATE at perf (the staleness-ceiling BLOCK = my ORIGINAL read). The 0-CPU hung procs (PID 3139 --single PULL_ASSETS_V2, 5184 --single SILVER_ASSETS_V2) are STANDALONE inf-api-assets-v2-daily dim-cron jobs in the designed post-bg do_wait keep-alive, lingering after the aborts -- NOT the --chain-full. DE conflated them.

### RECONCILED CONCLUSION
- Today's un-freeze IS the env-bump PERF_SILVER_STALENESS_CEILING_DAYS 2->10 (perf DEFERs -> --chain-full completes). 0.6.1 RAVC'd COO GO. My gold_prof/no-timeout hang is a LATENT risk, not today's cause.
- Converter side clean + exonerated.
- DURABLE split (both approved): 0.6.1 bounds silver/A/B/C/D dispatch steps with a timeout (the L580-598 amplifier); I add a bounded botocore Config (connect/read timeout + capped retries) to my silver converters (convert_assets_v2/orion_api/performance) as the converter self-defense complement -- sequenced with the CTO durable pass.
- Minor fail-loud gap flagged: the 07-06 SILVER_PERF aborts did NOT update gold/meta/pipeline-failed.json (still 07-02) -> the meta oracle silently reads 07-02-good. A dated pipeline-failed write on perf-surface aborts would fix it.

## Compiler Tools
| tool | invocation | result | note |
|---|---|---|---|
| comp-pipescript deployed | convert_assets_v2_to_silver.py | MATCH | exonerated the converter (current on code/silver) -- key to proving code-vs-execution-env |
| (live S3) | list bronze/assets + silver/assets_v2 | PASS | silver/assets_v2/2026-07-06.parquet @10:49Z = converter WORKS (fresh output) |
| (source grounding) | orion-gold-dispatch.sh run_script L580-598; gold_prof.py L153-176 | PASS | no-timeout on silver steps + gold_prof no-wait-timeout = the latent hang mechanism |

**What worked:** the fresh-07-06-silver + code/silver-MATCH pair decisively exonerated the converter (code-vs-execution-environment split); source-grounding run_script/gold_prof surfaced the real latent gap (no silver-step timeout). **What failed:** my initial gold_prof pipe-deadlock hang-site was real-in-principle but not today's cause (0.6.1's verbatim logs showed assets_v2 passed) -- withdrew it cleanly. **Gap:** silver-step no-timeout (0.6.1 durable dispatch fix); no data/inf gold_prof.py source copy; perf-surface aborts don't write dated pipeline-failed meta.

## MCP Traffic (summary)
~12 messages. Significant: COO [DRIVE] co-investigate + [ANDREW STEER] incremental-first + 3 RAVC-ACCEPTs (reachability, converter-exoneration, reconciled); 0.6.1 CO-VERIFY (definitive 2-log disambiguation) + durable-split-confirm. Sent: RAVCs to COO (x3) + 0.6.1 (x2, incl. alignment).

## Files Modified
None (diagnosis + coordination only; no code change this window -- the durable converter-timeout + holiday-fix + convert_performance redesign are queued for the CTO durable pass).

## Blockers
NONE. env-bump un-freeze is 0.6.1's execution lane (GO'd). Durable converter-side timeout is gated on the CTO durable-pass ring (convert_performance under HOLD).

## Next Steps
- [0.6.1_AE_PartnerETL] Execute env-bump 2->10 -> confirm --chain-full completes to gold tonight; bound silver/A/B/C/D dispatch steps with a timeout (durable); reap the 3139/5184 --single-cron do_wait leak; add a dated pipeline-failed write on perf aborts.
- [1.0.0_SA_CTO] Ring the durable pass -> I add the bounded botocore Config to my silver converters + the holiday-overcount fix + the convert_performance block->defer-loud redesign.
- [3.0.0_SA_CVO] (unchanged) 3-check served-cert on tomorrow's post-env-bump artifacts (WS-4 AC-2 3-limb as_of_by_dim + perf DEFER live-fire + gold data_as_of advance).
- [0.4.0_DS_ClientPlatform~A] (me) Event-driven: converter-timeout complement on the durable-pass ring; ping-on-dispatch-complete for CVO.
