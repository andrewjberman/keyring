# TO IRPT_ANLREQ.TO-AR-y-141 -- a READ: how the live provider is asked about a total label, and who can ask with no new grant

<to_id>IRPT_ANLREQ.TO-AR-y-141</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~53</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>14</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of code and Terraform text; in-process runs on synthetic sheets; NO live call)
**Decomp cell:** `AR-y-141` (`decompositions/IRPT_ANLREQ_DECOMP_R14_Y.md`) | **outcome_ref:** FWD-1 (hop 2, the upload door); TCKT_VNEXT FWD-3 by CTO msgs 5737 and 5849 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~53`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-53` (branch `wk-IRPT_ANLREQ-53`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~53 <0.9.0_WK_IRPT_ANLREQ~53@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W53-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either. Every `.py` you change passes `bash .tools/commit-gate.sh <file>` before its commit.
- **The background for every cell of this round** is one record, read it first:
  `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r13/ONE_ACCOUNT_CHECK_READ.json` (what the upload door does today, run in process on four synthetic sheets), and the CTO's rulings in
  `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_ANLREQ_Y_ROUND_14_20261011.md` section 2. Any sheet you build is SYNTHETIC: made-up tickers (`AAA`, `BBB`), made-up numbers, nothing that looks
  like a real account number or a person. No real uploaded file is ever read.

### THE CELL (`AR-y-141`, inlined) -- A READ. You make NO live call.

*How is the live provider asked about a symbol, what symbol does each total label become, and who can ask it with no new grant?*

Why. The door will refuse a row whose label is a total word. Before that is released, one question is owed a LIVE answer (the
CTO's ruling 2): what does the live provider answer for the symbol such a label would be taken for (for example the word `TOTAL`
in the ticker column)? Today's in-process run used an offline stub that admits any symbol-shaped word, so it could not say. A
worker makes no live call; this cell prepares the one read so that a seat that already can ask does so with one command.

1. `provider`: in `infra/aws/lambda/investor-reporting/intake/` (`upload_resolution.py`, `portfolio.py`, `uploads.py` `resolve_deferred`, and what they call): which
   function asks whether a ticker exists, what it calls (which service, table, API or function, with file and line), and where
   that runs (which Lambda function, read from `infra/aws/lambda/ci/lambda-source-map.json`: which entries package these files).
2. `labels_to_ask` and `symbol_each_label_becomes`: for the total labels a sheet would plausibly carry (`Total`, `Totals`,
   `Grand Total`, `Subtotal`, `Sum`, `Portfolio Total`, and any other found in the repository's fixtures -- say where), what the
   reader passes on as a symbol today (run `read_template` IN PROCESS on a synthetic sheet per label and record what reaches the
   provider stub; a label with a space may never reach it -- say which).
3. `who_can_ask`: every identity that could ask the live provider today WITHOUT a new grant, each `{"identity": "...", "how":
   "<the call>", "new_grant_needed": false|true, "evidence": "<file:line of the policy, role or earlier record that shows it>"}`.
   Read Terraform for the function's role and any earlier apply record under `org/tier2_senior/` that shows a seat invoking it.
   If the only way is to invoke a deployed function, say which, with what event, and what that invoke WRITES (an upload record? an
   input?): a read that writes is not a read, and the record must say so.
4. `exact_invocation`: the one command (or the smallest sequence) a seat would run, and what in its output answers the question;
   `in_process_stub_answer` for the same labels; `live_call_made`: false; `not_read`: a list.
5. Write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/r14/TOTAL_LABEL_PROVIDER_ASK.json` and commit it.

### ACCEPTANCE

<criterion id="AR141-y-AC1" cell_refs="AR-y-141"><invocation>python C:/dev/wk-irpt-anlreq-53/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r14/ar14_checks.py y141-ask --root C:/dev/wk-irpt-anlreq-53</invocation><expect>Y141-ASK-OK</expect></criterion>
`AR141-y-AC1`: the record names the provider call, the symbol each label becomes, at least one identity with whether a new grant
is needed, the exact invocation, and states that no live call was made. It grades the record's form.

<expected_criteria>AR141-y-AC1</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/` and this order's
  file (status flip only).
- READ only: everything else. No push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R14_Y.md</decomp_doc>
<owned_cells>AR-y-141</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR141-y-AC1. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~53/IRPT_ANLREQ.TO-AR-y-141.total-label-provider-ask.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-141`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR141-y-AC1`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading 1 record of round 13 (4 kinds run in process; it names upload_resolution.py:110-133 and uploads.py:423-488); NOT seen: the provider call itself and the function's role (the worker reads both). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or called. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger; 0 scheduled readers of what this cell writes. comp-iam: RUN -- by reading 0 policies at this cut; the cell READS which identity may ask and changes none; a row with new_grant_needed true is a finding, never an act.
comp-adversary: RUN -- by reading 1 ruling (CTO ruling 2: one live read first) against the face; the lens: a 'read' that writes an upload record when the function is invoked. The face makes the record say what an invoke writes. NOT seen: whether any seat on dell2 holds the invoke.
lane: the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-14 analysis @1edb90ada7, item 1. `AR141-y-AC1` base: FAIL as expected (no record).
- The live ask is ONE read-only Tier-2 order the issuer cuts from this record in this round.
- Seating: slot ~53 is reused; `TO-AR-y-145` queues behind this order in the same slot.
