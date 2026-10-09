# TO MDPF_DEMQUE.TO-DQ-t10 -- round 4 DQ-t-10: the BQL reserve written as a HELD estimate from the tier-1 producers' code
<to_id>MDPF_DEMQUE.TO-DQ-t10</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~9</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-10` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 4) |
**outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-10` (C-RESERVE; CTO msgs 1519 item 1 and 1524 "held+ask"). The Bloomberg quote (`data/mdpf/scripts/demque/bbg_quote.py`, read it) gives a
finish date only when a channel's ceiling AND reserve are known; `data/mdpf/scripts/demque/bbg_allowance.json` has the BQL ceiling (2920000, measured floor)
and every reserve absent. The reserve is what tier-1 production draws each day. Its measured source is not yet ledgered, so this cell
writes a HELD estimate from the producers' own code.

**Build** NEW `data/mdpf/scripts/demque/reserve_estimate.py`:
1. The producer set is the steps of `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` (the 07:00 ET daily pull, which feeds ETF
   Positioning). Read that file and each producer it runs AS TEXT (`ast` / regex; never import). For each producer, estimate the cells
   one scheduled run draws per channel (`bql`, `reference`, `history`): names (the security list it pulls, from its code or the config
   file it reads) x fields x rows per name. Where a figure cannot be read from code, say so and leave that producer out of the sum with
   a named gap -- never guess a number.
2. `estimate() -> dict` per channel: `value` (int: round(sum of producer cells x (1 + margin))), `claim` "held", `basis` (text naming the
   files and lines read), `margin` (a stated float, default 0.25, overridable by `--margin`), `producers` ({name: cells}), `gaps` (list).
3. CLI `python reserve_estimate.py --print` prints ONE JSON line of `estimate()` (keys = channels); `--write` updates
   `bbg_allowance.json`'s `<channel>.reserve` to `{"value", "claim": "held", "basis"}` for every channel estimated (ceilings untouched).
4. Do NOT edit `bbg_quote.py`.
5. NEW `data/mdpf/scripts/demque/test_demque_reserve.py` (pytest; small synthetic producer files) with exactly these names:
   `test_reserve_is_names_times_fields_times_rows_per_producer_run`, `test_margin_is_stated_and_applied`,
   `test_reserve_written_with_claim_held_and_basis`, `test_quote_finish_date_carries_held_when_reserve_is_held` (it calls the existing
   `bbg_quote.quote()` with an allowance whose reserve is held and asserts the result exposes that claim; if `quote()` does not expose
   it, file a row and mark the test xfail citing the row id -- never edit `bbg_quote.py`).

### ACCEPTANCE

<criterion id="DQ4-t10-AC1" cell_refs="DQ-t-10"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R4_CHECKS/dq_t10_tests.py</invocation><expect>RESERVE-OK</expect></criterion>
<criterion id="DQ4-t10-AC2" cell_refs="DQ-t-10"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R4_CHECKS/dq_t10_seam.py</invocation><expect>RSEAM-OK</expect></criterion>
`DQ4-t10-AC1` -- the four named tests. `DQ4-t10-AC2` -- the estimate on the REAL producers: a bql entry, claim held, a basis, a margin, parts that sum to the value.

<expected_criteria>DQ4-t10-AC1,DQ4-t10-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `RESERVE-BAD no file ...`, `RSEAM-BAD no file ...`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No Bloomberg call, no import of any `integrations/bloomberg/` or `data/etfs/` module, no AWS write, no deploy.** Read producer files as text only.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W9-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/reserve_estimate.py
data/mdpf/scripts/demque/test_demque_reserve.py
data/mdpf/scripts/demque/bbg_allowance.json
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 4), cell `DQ-t-10`.
<owned_cells>DQ-t-10</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ4-t10-AC1, DQ4-t10-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~9/MDPF_DEMQUE.TO-DQ-t10.reserve-held-estimate.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ4-t10-AC1,DQ4-t10-AC2` BEFORE the flip.
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

Source: PRD v0.3 FWD-3, C-RESERVE; CTO msgs 1519, 1524, 1536; decomposition round 4.
