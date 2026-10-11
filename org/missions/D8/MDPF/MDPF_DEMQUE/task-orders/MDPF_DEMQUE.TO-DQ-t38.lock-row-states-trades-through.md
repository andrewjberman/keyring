# TO MDPF_DEMQUE.TO-DQ-t38 -- round 9 DQ-t-38: each lock row states the date its identity was proved through
<to_id>MDPF_DEMQUE.TO-DQ-t38</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~30</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>LOCKTHRU</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-38` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 3) |
**outcome_ref:** C-PRICES, C-IDENTITY | **depends_on:** DQ-t-30 (merged @1961d4ee7a)

---

## WORKER FACE

### THE CELL

`DQ-t-38` (CTO round-8 analysis `org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round8.md` ADDENDUM 1: "The lock record states `trades_through`
and the claim per window"). DQ-t-30 made `lock.check` claim `held` when a window runs past the trades, but the lock ROW does not say through
which date the identity was proved; a reader of `lock.json` sees `held` with no date. The row's key set is the closed tuple `lock.ROW_KEYS`
(`test_demque_lock.py` asserts `set(row) == set(lock.ROW_KEYS)`).

**Build** (in `data/mdpf/scripts/demque/lock.py` and a NEW test file):
1. `ROW_KEYS` gains one key, `trades_through`, placed after `observations_passed`'s group where it reads naturally; the row `lock.check`
   returns always carries it: the ISO date `YYYY-MM-DD` passed in as `trades_through`, or `None` when none was passed (a name with no trade rows).
   The claim logic of DQ-t-30 (`_proved_through`) is unchanged. No other key, state or claim changes.
2. `price_store.py` reads no new key and writes the row as it is; confirm `price_store._same_lock` and `price_store.index` still work with the
   extra key (a re-draw of an unchanged input stays "unchanged"). Edit `price_store.py` ONLY if a test shows it must; say so in the report.
3. NEW `test_demque_lock_through.py` (pytest; synthetic frames, `tmp_path`, no network) with exactly these names:
   `test_the_lock_row_states_trades_through_beside_its_claim` (a name locked with trades through 2026-06-22 and a window to 2026-10-09 reads
   `trades_through` "2026-06-22" and claim `held`; the same name with a window ending 2026-06-22 reads the same date and claim `measured`),
   `test_a_name_with_no_trades_states_null_and_keeps_its_claim` and
   `test_the_row_key_set_is_the_declared_one_and_the_store_writes_it` (the row's key set equals `lock.ROW_KEYS`; `price_store.write` of
   such a row to a `tmp_path` root writes a `lock.json` carrying `trades_through`; a second write is `unchanged`).
   Every existing `test_demque_*.py` keeps passing unedited except where one hard-codes the old key count: if so, that is a surprise row, not
   an edit (`test_demque_lock.py` compares against `lock.ROW_KEYS`, so it should pass as it is).

### ACCEPTANCE

<criterion id="DQ9-t38-AC1" cell_refs="DQ-t-38"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t38_tests.py</invocation><expect>THRU-OK</expect></criterion>
`DQ9-t38-AC1` -- the three named tests, with the whole folder `pytest data/mdpf/scripts/demque` reported once in your report (it collected 130 passed
at the last merge).

<expected_criteria>DQ9-t38-AC1</expected_criteria>

Run the invocation from the worktree root. At the base: `THRU-BAD no file ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No S3 write, no write to the served store, the real pacer or queue, no AWS write, no Yahoo or Bloomberg call, no deploy.**
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W30-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/lock.py
data/mdpf/scripts/demque/test_demque_lock_through.py
data/mdpf/scripts/demque/price_store.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-38`.
<owned_cells>DQ-t-38</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t38-AC1. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~30/MDPF_DEMQUE.TO-DQ-t38.lock-row-states-trades-through.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t38-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, the check output, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call.
comp-adversary: DECLARED-NOT-APPLICABLE one additive key on a lock row; the claim logic is unchanged.
risk: LOCAL -- code and tests. The row reaches the served lock.json at the extension's apply (SERVED, under the t-31 pair).
direct_act: false -- a worker order.
</preflight>

Source: CTO round-8 analysis @92a9b27704 ADDENDUM 1 (msg 3956); TO-DQ-t30; decomposition round 9.
