# TO MDPF_DEMQUE.TO-DQ-t16 -- round 5 DQ-t-16: the standing request shape, quoted per run, and its one state writer
<to_id>MDPF_DEMQUE.TO-DQ-t16</to_id>
<project>MDPF_DEMQUE</project>
<issued_to>0.9.0_WK_MDPF_DEMQUE~14</issued_to>
<issued_by>2.0.0_SA_COO~Q1</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>5</round>
**Directive:** D8 | **Fabric:** dell1 (placement dell1) | **Decomp cell:** `DQ-t-16` (`decompositions/MDPF_DEMQUE_DECOMP.md`, ROUND 5 -- CUT) |
**outcome_ref:** FWD-4 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`DQ-t-16` (PRD `prd/MDPF_DEMQUE_PRD.md` ADDENDUM v0.4; CTO round-4 analysis
`org/missions/D8/MDPF/MDPF_DEMQUE/ledger/ROUND_ANALYSIS.round4.md` item 2). A STANDING request (one request file, `"shape": "standing"`)
is quoted PER RUN: its quote is its run cap, not one total. Each standing request has ONE readable state object, written only by the
queue, at the builder address
`lib.opal_naming.address("bloomberg","global","silver","request_state","request=<request_id>","state.json")`
(= `s3://opal-data-assets/bloomberg/global/silver/request_state/request=<request_id>/state.json`). It carries `state` in
`active | paused | stopped`, `as_of` (UTC ISO) and `reason`. ETFS_RIVALS' round-29 reader is cut against this address, and reads
nothing unless it reads `active`. `bbg_quote.py` belongs to DQ-t-15 this round: do NOT edit it.

**Build:**
1. NEW `data/mdpf/scripts/demque/standing.py`:
   - `quote_standing(request) -> dict`: requires `shape == "standing"` and an int `cap_cells_per_run`; returns `request_id`,
     `per_run: true`, `cells {"bloomberg_<channel>": cap}`, `claim` (the request quote's own claim), `basis`. A non-standing request is
     refused with a `ValueError`.
   - `state_address(request_id) -> str` from the builder (never a typed address).
   - `write_state(request_id, state, reason, s3=None) -> dict`: refuses a state outside `active|paused|stopped` and an empty reason;
     writes ONE object (the JSON above, `as_of` = now UTC) with `put_object`; returns what it wrote.
   - `read_state(request_id, s3=None) -> str`: returns the stored `state`; a missing object or a failed read returns `"unreadable"`,
     never `"active"`.
   - CLI: `--quote <request file>` prints ONE JSON line; `--set-state <request_id> <state> --reason "<text>"` writes and prints;
     `--read-state <request_id>` prints the state.
2. `org/missions/D8/MDPF/MDPF_DEMQUE/requests/ETFS_RIVALS-HISTORY-OWED-DAILY.json`: add `"shape": "standing"` (keep `"standing": true`
   and every other key).
3. NEW `data/mdpf/scripts/demque/test_demque_standing.py` (pytest; a stub S3 client object, no network) with exactly these names:
   `test_standing_request_quotes_its_per_run_cap`, `test_state_written_once_to_builder_address_with_state_as_of_reason`,
   `test_paused_reads_paused_and_unknown_state_refused`.

### ACCEPTANCE

<criterion id="DQ5-t16-AC1" cell_refs="DQ-t-16"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R5_CHECKS/dq_t16_tests.py</invocation><expect>STAND-OK</expect></criterion>
<criterion id="DQ5-t16-AC2" cell_refs="DQ-t-16"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_DEMQUE_Q1/R5_CHECKS/dq_t16_seam.py</invocation><expect>SSEAM-OK</expect></criterion>
`DQ5-t16-AC1` -- the three named tests. `DQ5-t16-AC2` -- the REAL rival-funds request file quoted per run at its cap (20,000).

<expected_criteria>DQ5-t16-AC1,DQ5-t16-AC2</expected_criteria>

Run each invocation from the worktree root. At the base: `STAND-BAD no file ...`, `SSEAM-BAD no file ...standing.py`.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Scaffolding goes under `.scratch/`, uncommitted.
- **No AWS write, no Bloomberg call, no deploy.** Never run `--set-state` against the real bucket: the first real state write is the
  issuer's run at close. Tests use a stub client.
- **You arm no timer, background task or OS task** unless this face names one.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `MDPF_DEMQUE-D1-W14-S<k>`, `fabric` `dell1`, `surfaced_at` = `date -u +%FT%TZ`, class `OBSERVATION` or `BLOCKING`) in the
  investigation file below, and do not weaken a check. Rows are APPEND-ONLY.

<paths>
data/mdpf/scripts/demque/standing.py
data/mdpf/scripts/demque/test_demque_standing.py
org/missions/D8/MDPF/MDPF_DEMQUE/requests/ETFS_RIVALS-HISTORY-OWED-DAILY.json
org/missions/D8/MDPF/MDPF_DEMQUE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_DEMQUE/decompositions/MDPF_DEMQUE_DECOMP.md</decomp_doc> (round 5), cell `DQ-t-16`.
<owned_cells>DQ-t-16</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DQ5-t16-AC1, DQ5-t16-AC2. Instance at `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~14/MDPF_DEMQUE.TO-DQ-t16.standing-request-and-state.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> DQ5-t16-AC1,DQ5-t16-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the files, every check's output, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule is changed.
comp-iam: DECLARED-NOT-APPLICABLE no AWS write by the worker; the issuer's one real state write at close names its one key.
comp-adversary: DECLARED-NOT-APPLICABLE LOCAL code, a request file and tests.
risk: LOCAL -- code and tests with a stub client.
direct_act: false -- a worker order.
</preflight>

Source: PRD ADDENDUM v0.4 @02df620d05; CTO round-4 analysis @91f3ee9da6 item 2; CTO msg 1752; decomposition round 5.
