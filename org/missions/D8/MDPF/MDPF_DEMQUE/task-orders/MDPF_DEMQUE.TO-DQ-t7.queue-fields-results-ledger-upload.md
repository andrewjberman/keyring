# TO MDPF_DEMQUE.TO-DQ-t7 -- round 2 DQ-t-7: the queue serves dividends and splits, hands what it drew onward, and uploads its ledger
<to_id>MDPF_DEMQUE.TO-DQ-t7</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~6</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `DQ-t-7` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 2) |
**outcome_ref:** FWD-2, FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-7`: three enrichments to the existing queue `data/mdpf/scripts/demque/demand_queue.py` (built in round 1; read it and its tests
`test_demque_queue.py` first). The queue already: validates a request (`fields` must be a subset of `SUPPORTED_FIELDS`, today `close`
only), quotes cells, draws in tier order through `yahoo_pull.run` under a `Pacer`, and appends one JSON-lines ledger row per request.
`yahoo_pull.pull` already returns `splits` and `dividends` frames with every request (one request per security). Keep every round-1
behaviour and test name passing.

1. **Fields.** Accept `dividends` and `splits` beside `close`. Quote: `close` counts weekdays in `[start, end]` per security, as now;
   `dividends` and `splits` cannot be known before the pull, so quote them as 0 cells and say so in the quote (`"unquoted": [...]`).
   Drawn: a `dividends` / `splits` field counts the event rows inside `[start, end]`. A request may ask for `dividends` alone.
2. **Hand results onward.** `draw(queue_dir, ledger_path, pacer, today, fetch=None, on_result=None)`: when `on_result` is given, call
   `on_result(cusip, result)` once for every security whose pull is `OK` (the issuer wires this to a price store at the merge; do not
   import or build any store here).
3. **Ledger upload.** `upload_ledger(ledger_path, day, dry_run=True, s3=None) -> str`: computes the target from the builder,
   `lib.opal_naming.address("yahoo", "global", "bronze", "demand_ledger", "dt=<day>")` (never type the address: the commit gate refuses
   it), returns the full key it would write (`.../ledger.jsonl`), and writes the day's rows there via `s3.put_object` only when
   `dry_run=False`. CLI: `python demand_queue.py --upload-ledger PATH --day YYYY-MM-DD [--apply]`; without `--apply` it prints the target
   and writes nothing.
4. Add to `data/mdpf/scripts/demque/test_demque_queue.py` (stubbed fetch, temp dirs, an S3 stub; no network) exactly these new names:
   `test_dividends_and_splits_fields_accepted_and_counted`, `test_draw_hands_each_ok_result_to_the_callback`,
   `test_ledger_upload_targets_builder_address_and_is_dry_by_default`. Keep the five round-1 names unchanged.

Do NOT edit `yahoo_pull.py`, `lock.py`, `land_cot.py` or any other file outside the grant, and do NOT create `__init__.py`.

### ACCEPTANCE

<criterion id="DQ2-t7-AC1" cell_refs="DQ-t-7"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R2_CHECKS/dq_t7_tests.py</invocation><expect>QUEUE2-OK</expect></criterion>
`DQ2-t7-AC1` -- the three new named tests pass AND the five round-1 names still pass (regression arm). At the base it reads
`QUEUE2-BAD not-passed=<the three new names>` with the five round-1 names passing.

<expected_criteria>DQ2-t7-AC1</expected_criteria>

Run the invocation from the worktree root.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS call (never `--apply`), no vendor call, no deploy.**
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W6-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the investigation
  file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/demand_queue.py
data/mdpf/scripts/demque/test_demque_queue.py
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 2, the enrichment), cell `DQ-t-7`.
<owned_cells>DQ-t-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ2-t7-AC1. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~6/MDPF_DEMQUE.TO-DQ-t7.queue-fields-results-ledger-upload.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ2-t7-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, the check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS call; the first --apply upload is the issuer's.
comp-adversary: DECLARED-NOT-APPLICABLE enrichment of LOCAL code.
risk: LOCAL -- code and tests.
direct_act: false -- a worker order; worker-light (an edit of under 100 product lines to one module).
</preflight>

Source: PRD v0.3 FWD-2, FWD-4, C-CELL, C-HOMES; CTO round-1 analysis item 4 (enrichment @5a392db104); decomposition round 2.
