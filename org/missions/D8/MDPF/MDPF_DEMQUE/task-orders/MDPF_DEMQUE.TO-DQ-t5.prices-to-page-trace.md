# TO MDPF_DEMQUE.TO-DQ-t5 -- round 1 DQ-t-5: from Cottonwood's canonical prices to the client's page, traced and answered
<to_id>MDPF_DEMQUE.TO-DQ-t5</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~4</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-08</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
**Directive:** D8 | **Fabric:** laptop (placement dell1) | **Decomp cell:** `DQ-t-5` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 1) |
**outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-5`, hop 6 of the FWD-1 thread, READ-ONLY: if a new Yahoo row lands in `s3://opal-data-cot/silver/historical_prices.parquet`
tonight, does a scheduled run carry it to a Cottonwood client's page with no person running anything -- and if not, what breaks.

**What is already measured (2026-10-08, do not re-measure):** `silver/prices/canonical_prices.parquet` in `opal-data-cot` was last written
2026-06-09T20:42:16Z, while `gold/positions_cube/2026-10-07.parquet` was written 2026-10-08T11:34:14Z. `data/cot/scripts/gold/gold_dispatch.sh`
:1069-1071 runs the silver-prep step `S_00` (`build_canonical_prices_v2.py`) only when invoked `--chain full`. `opal-data-cot` has NO
`silver/historical_prices.parquet` and NO `config/ticker_lookup.json`, both of which `build_canonical_prices_v2.py` reads with
`get_object` (:283, :298). The dependency graph does not hold the Cottonwood copy of the price build (`comp-blast` sees only the `bd` and
`inf` copies), so read the code directly.

**Answer five questions** in NEW `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~4/FWD1_HOP6_PRICES_TO_PAGE_TRACE.md`:

- **Q1** Which schedule fires Cottonwood's gold run, and with which `gold_dispatch.sh` arguments (`--chain full` or another)? Ground it in
  the scheduler (EventBridge rule or Scheduler schedule, read with `aws events list-rules` / `aws scheduler list-schedules`, all pages) and
  the runner that receives it (Terraform under `infra/aws/terraform/`, user-data / runner scripts under `infra/aws/ec2/`).
- **Q2** Does that run execute `S_00`?
- **Q3** Would `S_00` succeed today with the two Tier-2 objects absent (read `build_canonical_prices_v2.py`'s handling of a missing key),
  and is there run-log evidence (S3 run logs or CloudWatch, read-only) of its last attempt and outcome?
- **Q4** Which portal page shows a Cottonwood client's per-security daily prices (or values held positions from them)? Name the page, the
  API route, and the gold artifact it reads (`comp-routes trace`, `comp-transform fields`, the portal source under `portal/src`).
- **Q5** The artifact chain from `canonical_prices.parquet` to that page, one line per step, each with file:line.

The document carries: a markdown table with columns `hop | question | answer | grounding` and one row per Q1..Q5 (the `hop` cell starts
`Q1` .. `Q5`); then one line `VERDICT: BUILD-NEEDED -- <what must change for hop 6 to work>` or `VERDICT: NO-BUILD-NEEDED -- <why>`;
then the commands you ran with their times.

### ACCEPTANCE

<criterion id="DQ1-t5-AC1" cell_refs="DQ-t-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R1_CHECKS/dq_t5_trace.py</invocation><expect>TRACE-OK</expect></criterion>
<criterion id="DQ1-t5-AC2" cell_refs="DQ-t-5" judgment="true"/>
`DQ1-t5-AC1` -- the trace has the table, Q1..Q5 each answered and grounded, and a verdict line. `DQ1-t5-AC2` -- JUDGMENT, graded by the
CVO at L9: each answer is correct against the code and the live schedule.

<expected_criteria>DQ1-t5-AC1,DQ1-t5-AC2</expected_criteria>

Run the invocation from the worktree root. AC1 FAILS at the base: `TRACE-BAD no file ...`. Record AC2 as `UNVERIFIABLE-BY-INSTRUMENT`
with `status_reason` naming `3.0.0_SA_CVO`; give it no verdict.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **Read-only:** no AWS write, no Lambda invoke, no EC2 start, no run of `gold_dispatch.sh` or any producer, no vendor call, no
  `secretsmanager:GetSecretValue`. Do not start the portal dev server.
- **Cottonwood (cot) is its own firm:** read only Cottonwood's planes.
- **You arm no timer, background task or OS task.**
- **Refusal clause.** If a question cannot be answered from what is readable, answer `UNREAD because <reason>` in that row, file a surprise
  row (id `MDPF_DEMQUE-W4-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and keep going. Rows are APPEND-ONLY.

<paths>
org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~4/FWD1_HOP6_PRICES_TO_PAGE_TRACE.md
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 1, the thread), cell `DQ-t-5`.
<owned_cells>DQ-t-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ1-t5-AC1, DQ1-t5-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~4/MDPF_DEMQUE.TO-DQ-t5.prices-to-page-trace.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ1-t5-AC1,DQ1-t5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the file, the check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed; the cell reads the cot gold schedule (Q1).
comp-iam: DECLARED-NOT-APPLICABLE read-only calls.
comp-adversary: DECLARED-NOT-APPLICABLE read-only.
risk: LOCAL -- a document; read-only AWS calls.
direct_act: false -- a worker order.
</preflight>

Source: PRD v0.2 FWD-1; decomposition round 1 hop 6.
