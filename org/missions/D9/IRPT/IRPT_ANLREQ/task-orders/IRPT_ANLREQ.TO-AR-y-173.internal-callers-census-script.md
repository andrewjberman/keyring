# TO IRPT_ANLREQ.TO-AR-y-173.internal-callers-census-script -- a read-only census script: internal users rows that are not active, and internal callers with no row

<to_id>IRPT_ANLREQ.TO-AR-y-173</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>17</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-173` (`decompositions/IRPT_ANLREQ_DECOMP_R17_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-51` (branch `wk-IRPT_ANLREQ-51`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~51 <0.9.0_WK_IRPT_ANLREQ~51@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W51-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`. No live call, no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

### THE CELL (`AR-y-173`, inlined) -- BUILD ONLY. You call nothing live; no boto3 client is created in `--self-test`.

*A read-only script that counts, for the release pair of `AR-y-172`: (a) internal users rows whose `status` is not exactly `active`; (b) where the logs carry the caller, the distinct internal callers with no users row.*

**Read first:** the AR-y-163 read `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r16/INTERNAL_READER_NO_ROW_READ.json` (the `not_read` member lists what could not be counted), the stored-input count script
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r16/count_stored_inputs.py` (copy its shape: argparse, `--self-test` on in-memory fakes, only read calls, a denied or failed read is
reported by error code and never counted as zero, last stdout line one JSON object), and the users-table shape in `org/tier2_senior/0.7.0_AE_CloudOps~DELL2/deliverables/irpt_y75/y75_x1_arms.py`.

Build `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/r17/count_internal_callers.py` (ASCII only):
1. Part (a): scan the users table (`opal-users-v2`); an INTERNAL row is one whose `firmId` is `opal-capital` or whose `userType` is `Dev` or `service`; count them by `firmId`,
   `userType` and `status` value (the status string as it is, `absent` when missing); report how many are exactly `active`. Counts only: NO address, name or id.
2. Part (b): only if the function's request logs carry the caller's identity (read the code of the log line in `_authz/served.py` and `_scope/` and say what a line carries): a
   CloudWatch Logs read over the last 30 days of the investor-reporting status, directory and export functions, counting DISTINCT caller identities that appear in an internal
   context and match NO users row, bucketed by selected firm; the identities are hashed in memory with sha256 and only the COUNT leaves. If the logs do not carry the caller, the
   script prints `part_b: NOT_AVAILABLE` and says why; never a zero.
3. `--self-test` on in-memory fakes: rows of every status shape (active, disabled, absent, `Active`, `ACTIVE`, wrong type) counted right; a denied scan reported as a code and exit
   non-zero; the part (b) NOT_AVAILABLE branch; no address in the printed JSON. Print `CENSUS-SELFTEST-OK` on success.
4. The script's boto3 surface is READ calls only (`scan`, `get_item`, `query`, `filter_log_events`, `start_query`, `get_query_results`); no put, update, delete, send, publish, create
   or invoke call name appears anywhere in it (the check greps for them; `start_query` is a read).
5. Write `r17/CENSUS_SCRIPT_RECORD.json` with the members `script_blob`, `what_it_reads`, `what_it_cannot_read`, `output_members`, `no_address_in_output` (true/false with the line that guarantees it).
6. In your report: what a log line carries; whether part (b) can run at all; the command line a later applier runs.

### ACCEPTANCE

<criterion id="AR173-y-AC1" cell_refs="AR-y-173"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r17/ar17_checks.py y173-census --root C:/dev/wk-irpt-anlreq-51</invocation><expect>Y173-CENSUS-OK</expect></criterion>
`AR173-y-AC1`: the script exists, is ASCII, holds no write-shaped or invoke call, its `--self-test` prints `CENSUS-SELFTEST-OK`, and its record is complete.

<criterion id="AR173-y-AC2J" cell_refs="AR-y-173" judgment="true"/>
`AR173-y-AC2J` (judgment, graded at L9, never by you): the script's output can carry no address, name or id, and a row or log it cannot read is never counted as active or as a known caller.

<expected_criteria>AR173-y-AC1 AR173-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's file (status flip only).
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R17_Y.md</decomp_doc>
<owned_cells>AR-y-173</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-173.internal-callers-census-script.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-173`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> <the criterion ids>`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a script in the worker's deliverables; nothing is changed or called. Its one run is a separate order to an applier.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading the CTO's ruling (the census is the never-widen pair's input) against the cell; the lens: a count that holds an address, or an unreadable row counted as 'active'. The check refuses write-shaped calls and invokes; the script counts an unreadable row as unreadable by its error code. NOT seen: the real users table, the function logs and any real row (0 live rows read; the lens is blind to what the live data holds).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-17 analysis item 2 ("its pair carries the census"). Base: `AR173-y-AC1` FAIL as expected (no script).
- The RUN is not this order: when the script is proven, the issuer cuts one read-only order to an applier that can read the users table and the logs.
