# TO MDPF_DEMQUE.TO-DQ-t39 -- round 9 DQ-t-39: a name whose pull adds a split row keeps its prior files and says so
<to_id>MDPF_DEMQUE.TO-DQ-t39</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~31</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-11</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>9</round>
<workstream>SPLITHOLD</workstream>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-39` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 9 -- CUT, amendment 4) |
**outcome_ref:** C-PRICES | **depends_on:** none (the extension tool is merged)

---

## WORKER FACE

### THE CELL

`DQ-t-39` (CTO half of the t-31 never-widen pair, msg 4028,
`org/missions/D8/MDPF/MDPF_DEMQUE/ledger/NEVER_WIDEN_ROUND9_T31_EXTENSION_CTO_HALF.md`: "`commonwealth_daily_valuation.py:469` reads
`splits.parquet` in production, so this run writes a name's `splits.parquet` only where the extension adds no split row. A name that gains a split
keeps its prior file and is listed with the split date and ratio"). `price_store.write` (`data/mdpf/scripts/demque/price_store.py`, :112) writes a
name's `prices.parquet`, `splits.parquet`, `dividends.parquet` and `lock.json` together whenever its lock is LOCKED and the pull is OK. The issuer
holds a stricter reading than the half's letter, because `close_served` is split-adjusted from the same pull: a name that gains a split would get
restated prices beside a `splits.parquet` that lacks the split. So the whole name stays as it is.

**Build** (in `price_store.py` and a NEW test file):
1. In `write`, after the lock and pull-status checks and BEFORE any put: when the store already holds `cusip=<CUSIP>/splits.parquet`, compare the
   new `result.splits` rows (date, ratio) with it. A row in the new frame that is not in the stored one (same date, ratio within 1e-9) is a GAINED
   split. When any exists, write NOTHING for that name (no parquet, no lock.json) and return `{"written": False, "reason": "split gained: the
   name keeps its prior files (pair held)", "split_rows": [{"date": ISO, "ratio": float}, ...]}`. A name with no prior `splits.parquet` (a first
   write) is not held; a stored empty frame with a new split IS held. `daily_draw` already carries each `write` return into its `stored` list, so
   the run output lists them; do not edit `daily_draw.py`.
2. Every other behavior of `write` is unchanged: the unchanged short-circuit, the LOCKED and OK gates, the clip to `[valid_from, valid_to]`.
3. NEW `test_demque_split_hold.py` (pytest; a LOCAL store root under `tmp_path`, synthetic frames, no network) with exactly these names:
   `test_a_name_that_gains_a_split_row_is_not_written_and_says_why` (the store's files are byte-identical afterwards and `split_rows` names
   the date and ratio), `test_a_name_with_no_new_split_row_is_written_as_before` (extended prices written, splits unchanged),
   `test_the_first_write_of_a_name_with_no_prior_file_is_unaffected` (a new CUSIP with a split writes).
   Every existing `test_demque_*.py` keeps passing unedited (`test_demque_store.py` writes a first copy then re-writes; if an existing test adds
   a split on a re-write, that is a surprise row, not an edit).

### ACCEPTANCE

<criterion id="DQ9-t39-AC1" cell_refs="DQ-t-39"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t39_tests.py</invocation><expect>SPLIT-OK</expect></criterion>
<criterion id="DQ9-t39-AC2" cell_refs="DQ-t-39"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R9_CHECKS/dq_t39_real.py</invocation><expect>SPLIT-REAL-OK</expect></criterion>
`DQ9-t39-AC1` -- the three named tests. `DQ9-t39-AC2` -- one REAL served name copied to a scratch root (S3 read only): a result carrying its stored
splits plus a gained split row is held and every scratch file stays byte-identical; the same result without the gained row writes and advances
`max(date)`. Report the whole folder `pytest data/mdpf/scripts/demque` once (133 passed at the last merge).

<expected_criteria>DQ9-t39-AC1,DQ9-t39-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `SPLIT-BAD no file ...`; `SPLIT-REAL-BAD arms=a_not_written,a_bytes_identical`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No write to the served store (the AC2 write is to a LOCAL scratch root), the real pacer or queue, no AWS write, no Yahoo or Bloomberg call, no
  deploy.**
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W31-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/price_store.py
data/mdpf/scripts/demque/test_demque_split_hold.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 9), cell `DQ-t-39`.
<owned_cells>DQ-t-39</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ9-t39-AC1, DQ9-t39-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~31/MDPF_DEMQUE.TO-DQ-t39.hold-a-name-that-gains-a-split.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ9-t39-AC1,DQ9-t39-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, the folder count, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write by the worker; the S3 read in AC2 is the seat's existing read.
comp-adversary: DECLARED-NOT-APPLICABLE a narrowing guard on the served write path: it can only withhold a write.
risk: LOCAL -- code and tests. The condition it implements is the CTO half's: a name that gains a split keeps its prior files and waits on its own pair.
direct_act: false -- a worker order.
</preflight>

Source: CTO half NEVER_WIDEN_ROUND9_T31_EXTENSION_CTO_HALF.md (msg 4028); COO half @b3baaeb04c; decomposition round 9.
