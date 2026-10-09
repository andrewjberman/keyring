# TO MDPF_DEMQUE.TO-DQ-t11 -- round 4 DQ-t-11: a match locks only when 90 pct of trade dates agree within its type's band
<to_id>MDPF_DEMQUE.TO-DQ-t11</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~10</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-11` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 4) |
**outcome_ref:** FWD-5, FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-11` (row MDPF_DEMQUE-D1-S1; CTO msg 1519 item 2 as corrected by msg 1522 "bands"). `data/mdpf/scripts/demque/lock.py` `check()` today LOCKS when
at least `min(3, available)` trade dates agree within the type's band (0.005 mutual funds, 0.02 listed) and one falls in the earliest
third. PONPX (72201M719) locks at 51 of 83 (61 pct). The ruling: **a match LOCKS only when at least 90 pct of the client's trade dates
agree within THAT security type's band (0.5 pct mutual funds at NAV, 2 pct listed)**, in addition to the existing conditions; below the
floor the state is `REJECTED:LOW_TRADE_AGREEMENT` (claim `measured`). Exactly 90 pct locks. The no-trade-prices case (claim `held`) is
unchanged.

**Build:** edit `check()` in `data/mdpf/scripts/demque/lock.py` for the floor (keep its signature and its returned keys). Add to `data/mdpf/scripts/demque/test_demque_lock.py`
exactly these names: `test_below_ninety_percent_agreement_is_rejected_low_trade_agreement`,
`test_ninety_percent_floor_counts_within_each_types_band` (a mutual fund at 1 pct error on every date is rejected; a listed security at
1 pct locks), `test_exactly_ninety_percent_locks`. Keep the round-1 names passing; if one encoded the old looser rule, change its
synthetic data, never its name, and say so in the report.

### ACCEPTANCE

<criterion id="DQ4-t11-AC1" cell_refs="DQ-t-11"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R4_CHECKS/dq_t11_tests.py</invocation><expect>FLOOR-OK</expect></criterion>
`DQ4-t11-AC1` -- the three new named tests and five round-1 names.

<expected_criteria>DQ4-t11-AC1</expected_criteria>

Run each invocation from the worktree root. At the base: `FLOOR-BAD not-passed=<the three new names>` with the five round-1 names passing.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No vendor call, no AWS call, no deploy.**
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W10-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/lock.py
data/mdpf/scripts/demque/test_demque_lock.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 4), cell `DQ-t-11`.
<owned_cells>DQ-t-11</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ4-t11-AC1. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~10/MDPF_DEMQUE.TO-DQ-t11.lock-agreement-floor.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ4-t11-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL code.
risk: LOCAL -- code, config and tests.
direct_act: false -- a worker order; worker-light (one function and tests).
</preflight>

Source: PRD v0.3 C-IDENTITY; CTO msgs 1519, 1522; row MDPF_DEMQUE-D1-S1; decomposition round 4.
