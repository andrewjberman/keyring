# COT_ADVI_DIAG -- "not run in a week" diagnosed: chain RUNS daily; gold halts at A_03 since 07-21 on a 2-cell vendor text-format drift amplified by silver's object-sweep
**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, VALIDATE
**serial:** 0.7.0_AE_CloudOps
**window:** 2026-07-22 ~22:24Z -> ~22:47Z (Andrew-direct via CTO 222113Z -> COO TO @f8f2fbea0; read-only throughout)

## VERDICTS (the TO's five steps)

1. **GROUNDED:** "Cottonwood ADVI" = the `cot-pipeline` advi-cot thread (pipescript): cot-bd-session-trigger
   Lambda 4-phase EventBridge chain (cron(0 2) -> SSM session-fetch on cot-exporter i-0643a5bee8a8feabf ->
   bronze -> silver -> gold), serving s3://opal-data-cot/platinum/** to the AdvisorIntelligence Cottonwood
   tenant. DISTINCT from the 49F/0833 ADVI surface (opal-data-bd tree); firm separation maintained -- zero
   bd resources touched.
2. **FIRE HISTORY (census, denominators):** EventBridge default bus 141 rules (100+41, two pages), 10
   cot-matched, ALL ENABLED incl cot-bd-session-daily cron(0 2). Scheduler namespace: 10 total, 0 cot.
   Rule Invocations Sum=1.0 daily 07-08..07-22 (15/15), FailedInvocations EMPTY; lambda 3/3 phases daily,
   Errors=0. THE SCHEDULE NEVER STOPPED.
3. **TRADING-DAY FRESHNESS (calendar first):** Andrew's "a week" REFUTED as stated. Served platinum last
   build 2026-07-20T02:04:47Z (explicit-Z listing); header_metrics data_as_of=2026-07-17 = **3 trading
   days** behind the 07-22 frontier; write-lag 2 trading days. The "week+" perception likely comes from
   the STILL-frozen allocations/unrealized snapshot legs (as_of 2026-07-08 = **10 trading days**).
4. **KNOWN-FREEZE POINTER:** the A_03 crash is **NOT downstream** of project_cot_snapshot_zero_row_freeze_
   20260709 -- transactions was the healthy leg. Live state: that freeze is PARTIALLY CURED (holdings
   partitions 07-16/07-17/07-20 advancing at BD D+2; 07-20 landed 07-22T02:04:25Z). allocations +
   unrealized remain frozen at 07-08. Record stays open; closed nothing on it.
5. **LD-0333 INTERACTION: NONE.** First failure 07-21T02:03Z, ~40h before the 1819Z hold; nothing disabled.
   The 07-21T2314Z cot-ws5-rebalancer deploy postdates the first failure by ~21h -- ruled out by timing.

## THE MECHANISM (every hop artifact- or source-cited)

BRONZE: forwardfill_v2/transactions/TRANSACTIONS_DAILY_2026-07-21.xlsx -- full-column scan: 12,840
non-null Units, **2 NON-NUMERIC: rows 157+158 = str '9.6E-05'** (fractional shares exported as text).
Control 07-20: 13,303 non-null, 0 non-numeric. Delivery drift, 2 cells.
SILVER: cot_silver_merge.py:417-419 @5930dd45d ("Convert remaining object columns to string") -- 2 text
cells -> pandas object column -> sweep stringifies ALL. Artifact: silver/transactions/2026-07-21.parquet
units 12,840/12,840 str (07-20: float64). Deployed copy CONSTANT (s3 code/silver LastModified
2026-07-15T21:56:27Z; ran clean 07-16..07-20) -- input changed, not code.
GOLD: A_03.positions_cube.py:1001 `unit_txns['units'].abs()` -> TypeError bad operand type for abs():
'str' -> "ERROR: A_03 exit 1 -- chain halted" (cot-gold-run-2026072{1,2} logs, verbatim). SSM
opal-cot-gold-run Failed 07-21 (cmd 1784599424) + 07-22 (9f09c1e1-efa9); 07-20 "GOLD CHAIN COMPLETE
(exit 0)". Recurs nightly (full-table re-export carries the cells).
SERVED: platinum frozen at the 07-20 build. Invisible failure: SSM Failed has no consumer.

MEASUREMENT NOTE: initial SSM stdout was 24KB-truncated mid-A_02 -- the real failing step (A_03) found
only via the untruncated on-bucket log (logs/cot-exporter/gold-run/). A truncated success-tail reads
like a later-step failure; the full log is the instrument.

## ESCALATION + REPAIR (separate, CTO-gated, NOT executed)
Escalated to CTO 224551Z + COO 224628Z as a NEW live defect per the TO clause. Recommendation: (a)
silver-side coerce-numeric-before-object-sweep (DS lane, Rule 13/17); (b) idempotent silver re-run
07-21/22, nightly gold rebuilds itself at 02:00Z (no ad-hoc gold run); (c) optional A_03 guard.

## Compiler Tools
| tool | invocation | result | note |
|---|---|---|---|
| comp-which | cot ADVI question | PARTIAL | routed to raw hits, no curated rule -- coverage gap recorded per TO |
| pipescript | --list + advi-cot | PASS | named the full thread: producer/trigger/served/frontend |
| comp-pipescript deployed | cot_silver_merge.py | PARTIAL | scans opal-data-bd roots only -- cot code prefix uncovered (tool gap); vintage grounded via s3api on opal-data-cot/code/ instead |
| comp-grep | astype/object in cot_silver_merge | PASS | located the object-sweep :417-419 |
| aws events/scheduler/cloudwatch | census + fire metrics (rail-checked) | PASS | denominators printed; both namespaces |
| aws logs + ssm + s3api | lambda logs, command history, explicit-Z listings | PASS | the mechanism chain |
| openpyxl + pandas (scratchpad) | direct cell-type + parquet dtype reads | PASS | the decisive 2-cell finding + both controls |

**Gap found:** (1) comp-pipescript deployed does not cover the opal-data-cot code prefix; (2) SSM
gold-run failures have NO consumer -- a nightly deterministic FATAL was invisible until a sovereign
noticed the screen; (3) comp-which has no curated cot-ADVI rule.

## Next Steps
- **[1.0.0_SA_CTO]** gate the repair (silver coerce-numeric fix is DS-lane); route the three gaps.
- **[0.4.0_DS_ClientPlatform]** on CTO GO: the one-function silver fix + idempotent 07-21/22 re-run.
- **[0.7.0_AE_CloudOps]** back to IDLE: available after this log commits; nothing further without cascade.

---

## CLOSURE 2026-07-23 ~1028Z -- VERIFIED, mechanism proven by the cure

DS fix @2ed963ef6 landed 23:10Z (2.5h ahead of window; his ledger 20260722T2310Z closed). The 02:04Z
nightly then self-healed with ZERO ad-hoc runs: cot-gold-run-20260723-020651.log ends "=== COT GOLD
CHAIN COMPLETE (exit 0) ===" (Completed 02:08:57Z); platinum/firm/* advanced to 2026-07-23T02:08:56Z;
header_metrics data_as_of 2026-07-17 -> 2026-07-21 (T-2, inside the BD D+2 holdings contract, inside
CTO's 07-21/22 bar). Reported CTO 102905Z + COO 102911Z; MEMORY.md trigger discharged (deleted).
allocations/unrealized remain frozen at 07-08 -- standing record open, separate defect.

ALSO CLOSED same window (MSTR relay of CVO~Z finding): the stranded eclipse-converter artifact_sha256
in lambda-source-map.json -- live CodeSha256 grounded the WORKING-TREE value (deployed 07-22T14:50:08Z,
1 min after predecessor's 010d458e5 rebuild); committed @192d065c0 with consistent last_deployed_* .
ERROR OWNED: 192d065c0's last_deployed_commit tail was expanded FROM MEMORY (fabricated); self-caught
same turn vs git rev-parse, corrected @3c680049e (verified ancestor-of-HEAD). A provenance field is a
RETRIEVAL, not a recollection.

---

## 6d DISPATCHER WIRING 2026-07-23 ~1052-1102Z (morning batch, joint DS+AE) -- LANDED, ledger 5/5

**archetype for this arc:** DEPLOY. DS's revamp_stage 6d block (patch @3e7a59502) landed in
mdpf-daily-dispatch.sh @4528fa154 + AE PYTHONPATH resolution (the pair's ../../../mdpf repo-relative
insert cannot mirror on the runner; COT_PYPATH resolves imports from the synced canonical dirs, zero
module duplication). Six artifacts staged to s3://opal-data-mdpf/code/ ETag==md5 verified per key
(dispatcher 6f26beac; bdmp/pair/slice; silver/rebalancer_schemas; gold/dim_mdpf_aum_metrics).
**The import-chain EXERCISE caught 2 gaps a config-read missed:** dim_mdpf_aum_metrics ABSENT from S3
(pair imports it -- tonight's 6d would have died) + the unlisted transitive dep
mdpf_revamp_model_crosswalk (verified already on S3). Runner-sim probe: pair resolves bdmp +
_distribution_stats + calc_metric + quarter_ends clean. Ledger 20260723T1052Z CLOSED 5/5; NO schedule
change, NO TF, NEVER#4 held (the scheduled 02:04Z run IS the exercise); outcome banked as MEMORY.md
trigger 07-24 post-02:10Z (marker keys_staged=11, slice covered_dates nonempty). Compiler tools:
deploy_ledger x7, safe-commit x2, git apply --check, bash -n, s3api listing-verify x8, comp-glob/grep
(dispatcher + import discovery), runner-sim import probe.
