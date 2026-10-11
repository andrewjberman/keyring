# TO MDPF_DEMQUE.TO-DQ-t30 -- round 9 DQ-t-30: the lock reads the latest transactions partition and claims only what the trades prove
<to_id>MDPF_DEMQUE.TO-DQ-t30</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~24</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-30` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT) |
**outcome_ref:** C-PRICES | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-30` (CTO round-8 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round8.md` R1 part (b), read it; row
`MDPF_DEMQUE-D1-W22-S1`). `data/mdpf/scripts/demque/lock.py` line 23 pins `TX_PARTITION = "date=2026-06-23"`, so every lock and every request
window is built from one June snapshot. The ruling: the lock reads the LATEST transactions partition, resolved through `opal_naming`, not a
pinned date. **Measured fact you must build around (the issuer, 2026-10-11):** the store
`s3://opal-data-assets/commonwealth/cottonwood/silver/transactions/` holds exactly ONE partition today, `date=2026-06-23`, whose largest
`Trade_Date` is 2026-06-22. The rule must therefore resolve to that partition today and advance by itself when a later one lands, and a
window that runs past the trades must not be claimed as proved.

**Build** (all in `data/mdpf/scripts/demque/lock.py` and a NEW test file):
1. Replace the pinned constant: `TX_PARTITION = None` (an explicit value, or the env var `OPAL_TX_PARTITION`, still wins, so a test or a
   rollback can pin). `latest_partition(s3=None) -> str`: derive the parent prefix of the transactions address from
   `opal_naming.address("commonwealth", "cottonwood", "silver", "transactions", <a partition token>)` (the canon builds the address; type no
   bucket or key), list its immediate `date=YYYY-MM-DD/` children, and return the greatest one that holds at least one `.parquet` object. No
   such partition is a loud `SystemExit`, never a default. `_load_transactions` uses it.
2. `trades_through(tx) -> str | None`: the largest `Trade_Date` of the loaded rows as ISO `YYYY-MM-DD`, or None for an empty frame.
3. `check(...)` gains an optional keyword `trades_through=None`. When it is given and `valid_to` is later than it, a result that would be
   `LOCKED` with claim `measured` returns claim `held` instead (the identity is proved through the trades only; the tail is carried).
   Every other outcome is unchanged. `ROW_KEYS` is unchanged (`test_demque_lock.py` asserts the row's key set equals it).
4. CLI `--partition`: prints ONE JSON line `{"partition": "date=...", "trades_through": "YYYY-MM-DD", "partitions": N}` where `partitions` is
   the number of `date=` partitions holding parquet; it reads the latest partition's `Trade_Date` column only (all cusips).
5. NEW `test_demque_lock_partition.py` (pytest; a stub S3 client with a fake paginator and fake parquet bytes; no network) with exactly these
   names: `test_latest_partition_is_the_greatest_date_partition_holding_parquet` (an empty newer partition is skipped),
   `test_trades_through_is_the_max_trade_date_of_the_loaded_rows`, `test_claim_is_held_when_the_window_runs_past_the_trades` (a locked name with
   `valid_to` after `trades_through` reads `held`; with `valid_to` on or before it, `measured`).

### ACCEPTANCE

<criterion id="DQ9-t30-AC1" cell_refs="DQ-t-30"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t30_tests.py</invocation><expect>LP-OK</expect></criterion>
<criterion id="DQ9-t30-AC2" cell_refs="DQ-t-30"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t30_real.py</invocation><expect>LP-REAL-OK</expect></criterion>
`DQ9-t30-AC1` -- the three named tests. `DQ9-t30-AC2` -- `lock.py --partition` on the REAL store equals the check's own listing and its own read
of the partition's largest `Trade_Date` (`date=2026-06-23`, 2026-06-22, one partition).

<expected_criteria>DQ9-t30-AC1,DQ9-t30-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `LP-BAD no file ...`; `LP-REAL-BAD tool rc=2 ... unrecognized arguments: --partition`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Read-only against S3; no AWS write, no Bloomberg call, no Yahoo call, no deploy.** Do not change `daily_draw.py` (a later order does).
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W24-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/lock.py
data/mdpf/scripts/demque/test_demque_lock_partition.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-30`.
<owned_cells>DQ-t-30</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t30-AC1, DQ9-t30-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~24/MDPF_DEMQUE.TO-DQ-t30.lock-reads-latest-partition.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t30-AC1,DQ9-t30-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the `--partition` line verbatim, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write; the partition listing uses the seat's existing S3 read.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL lock code and tests; the claim downgrade only narrows a claim.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order.
</preflight>

Source: CTO round-8 analysis @92a9b27704 R1 (b); row D1-W22-S1 (REMEDIATION_v7); row D1-S11 (the one-partition measure); decomposition round 9.
