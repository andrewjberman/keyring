# TO MDPF_DEMQUE.TO-DQ-t12 -- round 4 DQ-t-12: the FWD-5 unresolved list, one row per CUSIP and open period
<to_id>MDPF_DEMQUE.TO-DQ-t12</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~11</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-12` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 4) |
**outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-12` (CTO msg 1519 item 4; dell2 research s.2 and s.5). A security that cannot be matched, or is matched for only part of
the time it was held, appears on a list with its reason and the dates still open.

**Build** NEW `data/mdpf/scripts/demque/unresolved.py`:
1. One row per (CUSIP, open period): `cusip, symbol, period_start, period_end, priority (P1|P2|P3 or null), state, reason, next_act,
   attempts, last_attempt, source_tried`. States: `UNRESOLVED:NO_CANDIDATE`, `UNRESOLVED:YAHOO_NO_DATA`, `UNRESOLVED:PARTIAL_RANGE`,
   `REJECTED:PRICE_MISMATCH`, `REJECTED:LOW_TRADE_AGREEMENT`, `PARKED:LOW_PRIORITY`.
2. `update(rows, cusip, symbol, held_start, held_end, outcome)`, `outcome` a pull status (`FAILED_EMPTY`, `FAILED_REFUSED`) or a lock row
   (`state`, `valid_from`, `valid_to`): a failed pull opens/keeps the whole held period; a REJECTED lock opens it with the lock's state as
   reason; a LOCKED range closes exactly that range and leaves any uncovered remainder open as PARTIAL_RANGE; a fully LOCKED security
   leaves the list. Attempts count up per update.
3. `load(path)` / `save(path, rows)` (CSV + parquet, a local path). `seed(path_to_seed_csv)` loads rows from a CSV `cusip,symbol,reason`.
4. NEW `data/mdpf/scripts/demque/unresolved_seed.csv` with exactly these 5 rows (the round-2 scheduled draw's Yahoo no-data securities), reason
   `UNRESOLVED:YAHOO_NO_DATA`: `30254T643,FPNIX` / `302544101,FPNIX` / `69351J108,PIUIX` / `693391666,PFODX` / `03834A103,AREX`.
5. NEW `data/mdpf/scripts/demque/test_demque_unresolved.py` with exactly these names: `test_row_per_cusip_and_open_period_with_reason`,
   `test_failed_pull_and_rejected_lock_both_feed_the_list`, `test_partial_lock_leaves_only_the_uncovered_period_open`,
   `test_seed_file_loads_the_five_no_data_cusips`, `test_resolved_security_leaves_the_list`.
Do NOT edit `daily_draw.py` (the issuer wires the list into the draw at the merge).

### ACCEPTANCE

<criterion id="DQ4-t12-AC1" cell_refs="DQ-t-12"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R4_CHECKS/dq_t12_tests.py</invocation><expect>UNRES-OK</expect></criterion>
`DQ4-t12-AC1` -- the five named tests.

<expected_criteria>DQ4-t12-AC1</expected_criteria>

Run each invocation from the worktree root. At the base: `UNRES-BAD no file ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No vendor call, no AWS call, no deploy.**
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W11-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/unresolved.py
data/mdpf/scripts/demque/unresolved_seed.csv
data/mdpf/scripts/demque/test_demque_unresolved.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 4), cell `DQ-t-12`.
<owned_cells>DQ-t-12</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ4-t12-AC1. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~11/MDPF_DEMQUE.TO-DQ-t12.unresolved-list.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ4-t12-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL code.
risk: LOCAL -- code, config and tests.
direct_act: false -- a worker order.
</preflight>

Source: PRD v0.3 FWD-5, C-IDENTITY; CTO msg 1519 item 4; dell2 research s.2, s.5; decomposition round 4.
