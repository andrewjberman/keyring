# TO IRPT_ANLREQ.TO-AR-y-71 -- the report read is refused when the ticket asking is not the ticket the request was filed under

<to_id>IRPT_ANLREQ.TO-AR-y-71</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~52</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>in_progress</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>7</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** WORLD by the L6 gate's floor for an `infra/` path. The cell is code, a contract document and tests: nothing is built into a zip, uploaded, applied or called live.
**Decomp cell:** `AR-y-71` (`decompositions/IRPT_ANLREQ_DECOMP_R7_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~52`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-52` (branch `wk-IRPT_ANLREQ-52`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~52 <0.9.0_WK_IRPT_ANLREQ~52@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing. The worktree shows ` M portal`:
  never commit it. The portal's code is readable at `C:/dev/wk-irpt-anlreq-51/portal` (READ ONLY, another worker is editing it: use
  `git -C C:/dev/wk-irpt-anlreq-51/portal show origin/DEV:<path>` and never touch its working files).

### THE CELL (`AR-y-71`, inlined)

*The owned report read the Ticket Center's Open control calls takes an OPTIONAL ticket id. When the caller sends one and the request's
acceptance record stores a DIFFERENT `ticket_id`, the read is refused with one typed reason. Sent and equal: it answers. Not sent: it
answers as today. No `ticket_id` stored on the request: it answers as today.*

Why: a ticket's `report_ref.request_id` is about to be writable by the ticket's creator (another team's change). The id a creator
records is the creator's own word, so a ticket could point at a report that is not its own. Every reader of these tickets is internal
and may already open any request, so no access widens; what is loose is the BINDING. A request filed from a ticket stores that
ticket's id on its acceptance record (`infra/aws/lambda/investor-reporting/ycharts/generate/acceptance.py:120-121`, admitted by
`submission.py:78-79`). So the place to check is the report read.

1. **Find the read.** In the portal (read-only), follow the Ticket Center's Open control to the Investor Reporting client call it makes
   (`src/pages/TicketCenter/AnalysisRequestParts.tsx` and `analysisRequest.ts`: `getOwnedAnalysisReport` / `openReport`) and from the
   client (`src/api/endpoints/investor-reporting.ts`) to the route. Then find that route's handler in
   `infra/aws/lambda/investor-reporting/ops/` (`entry.py` holds the route table; the report read is in `owned_report.py`). State in
   your report the operation name, the route, and how the handler receives its selectors today.
2. **Add the optional selector** `ticket_id` to THAT read only, in the carrier the route already uses for selectors (do not invent a
   second carrier). Malformed (not the ticket service's id form: read `TICKET_ID` in `ycharts/generate/submission.py` and use the SAME
   pattern object or an import of it if the packaging allows; if the modules are packaged separately, say so and restate the pattern
   with a comment naming its source) is refused as invalid input BEFORE any read.
3. **The check.** After the read has resolved the owned request by its existing rules (owner, tenant, retention: unchanged and
   FIRST), read the request's acceptance record's `ticket_id` the way this module already reads that record (find the existing read;
   do not add a second fetch if the record is already in hand). If the caller sent `ticket_id` and the record stores a `ticket_id`
   that is not equal: refuse with ONE new typed reason. Choose its name by the module's own refusal vocabulary (read how
   `RequestReadRefused` codes are declared and how a code becomes a public reason; follow the same rule a code like
   `ANALYSIS_ORIGINAL_NOT_APPLICABLE` follows) and state the name in your report. If the record stores none, or the caller sent none:
   exactly today's answer, byte for byte.
4. **The refusal must not tell the caller which ticket the request belongs to.** No stored id in the refusal's body or log line.
5. **Contract.** If the route's request or response has a contract document under `docs/contracts/investor-reporting/v1/` or
   `infra/aws/lambda/investor-reporting/_contracts/` (routes.json, a request schema, a refusal enum), add the selector and the reason
   there in the documents' own style, with a fixture each where the neighbours have fixtures. If a contract test pins the reason set,
   update the pin and say so.
6. **One new test file**, `infra/aws/lambda/investor-reporting/ops/tests/test_report_ticket_binding.py`, in the style of the folder's
   existing report-read tests (read `test_retained_ref_served.py` and one owned-read test first; use the folder's fakes), with tests
   named exactly:
   - `test_report_read_with_the_stored_ticket_id_answers`
   - `test_report_read_with_another_ticket_id_is_refused`
   - `test_report_read_with_no_ticket_id_answers_as_before`
   - `test_request_with_no_stored_ticket_id_answers_whatever_ticket_asks`
   - `test_malformed_ticket_id_is_refused_before_any_read`
   The third asserts equality with the answer of the unchanged path, not merely success.
7. Do not change who may read a request, any other route, the acceptance writer, or the source map (the irpt-status entry pins
   `owned_report.py` on purpose: do not touch `infra/aws/lambda/ci/`). Do not build, upload or apply.

---

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-11 ~13:2xZ): REOPENED by CTO ruling (`1.0.0_SA_CTO~DELL2` msg 4984): the mismatch is
served under a DISTINCT public reason, and only AFTER the caller is admitted to the request.** Gate limb that graded this amendment:
read from this commit's own output.

What you built (commit `420fc49e0e`, merged) serves the mismatch as public reason `NOT_FOUND`. The page cannot tell that from a report
that does not exist yet, and its Open path shows a waiting state for a missing report: a mis-recorded ticket would read "not ready"
forever, which is the failure this binding exists to make visible. The ruling, in its words: "Authorization first, the ticket
comparison second. A caller who may not open the request gets what it gets today and learns nothing about any ticket. Only a caller
already admitted to the request is told the ticket does not match."

**Do:**
1. Give the mismatch its own PUBLIC reason code (the value a caller reads in `status.public_reason_code`), named by the rules the
   existing public reasons follow. Find where the public-reason set is declared and how a refusal class or code maps to it (the entry
   boundary and its reason table; the status envelope's contract; any enum in `docs/contracts/investor-reporting/v1/` or
   `infra/aws/lambda/investor-reporting/_contracts/`). Add the value everywhere the set is declared, in each place's own style.
2. Keep the order you already have and PROVE it with one arm: a viewer NOT admitted to the request, sending a wrong `ticket_id`,
   reads exactly the same answer as when it sends the right one (and the same as with none). Only an admitted caller reads the new
   reason. The refusal still carries neither ticket id.
3. Two more tests in `test_report_ticket_binding.py`, named exactly:
   - `test_a_viewer_not_admitted_reads_the_same_answer_with_a_wrong_ticket_as_with_a_right_one`
   - `test_an_admitted_caller_is_told_the_ticket_does_not_match_by_its_own_public_reason`
   Update `test_report_read_with_another_ticket_id_is_refused` for the new public reason; the other four stay as they are.
4. **A public reason is a value in a closed set: census every reader of that set.** Write
   `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/r7/PUBLIC_REASON_READERS.json`:
   `{"new_public_reason": "<the value>", "declared_in": ["<file:line>", ...], "searched": "<what you searched, over what, with the
   count of files>", "readers": [{"side": "SERVICE"|"PORTAL", "file_line": "<file:line>", "what_it_does": "<one sentence>",
   "key_policy": "EXACT"|"TOLERANT", "meets_new_value": "PASS"|"REFUSES"|"NOT_REACHED", "why": "<one sentence>"}, ...]}`.
   SERVICE readers: every place in `infra/aws/lambda/investor-reporting` (non-test) and the contract tests that enumerates or
   validates public reason codes. PORTAL readers: read-only, by `git -C C:/dev/wk-irpt-anlreq-51/portal show origin/PROD:<path>` and
   `origin/DEV:<path>` (never touch that worktree's files): every place under `src` that reads `public_reason_code` or holds the set
   of reason codes (a union type, a validator, a switch, a message table). For each: EXACT means an unknown value is refused or
   throws; TOLERANT means it passes through or falls to a default. `meets_new_value` is what THAT reader does when it receives the
   new value (PROD and DEV as separate rows where they differ). A portal reader that REFUSES the new value is a FINDING to state
   plainly at the top of your report: it must be on PROD before this service change is released, exactly as happened with the
   history reader this morning.
5. Update the contract line you added to `routes.json` if it names the old reason. Do not build, upload or apply. Do not touch
   `infra/aws/lambda/ci/`.

AC1 now requires the seven named tests and the census file (the check `y71-bind` is amended). AC2 is unchanged. Update the proof
instance, validate it after its commit, and flip back to `complete` only then.

### ACCEPTANCE

<criterion id="AR71-y-AC1" cell_refs="AR-y-71"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r7/ar7_checks.py y71-bind --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y71-BIND-OK</expect></criterion>
`AR71-y-AC1` (AMENDMENT 1): the binding test file holds the seven named tests and passes, and the public-reason reader census exists with every row filled.

<criterion id="AR71-y-AC2" cell_refs="AR-y-71"><invocation>python C:/dev/wk-irpt-anlreq-52/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r7/ar7_checks.py y71-keep --root C:/dev/wk-irpt-anlreq-52</invocation><expect>Y71-KEEP-OK</expect></criterion>
`AR71-y-AC2`: the difference control -- the whole `ops/tests` folder passes (it passes at the base and must still pass).

<expected_criteria>AR71-y-AC1 AR71-y-AC2</expected_criteria>

The issuer runs the `_contracts`, `_authz` and `reports` test folders and a BUILD_ONLY of every investor-reporting function at the drain.

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/` and this order's
  file (status flip only).
- READ only: everything else, the portal included. No live call, no build, no upload, no apply. No non-ASCII in what you add.

<paths>
infra/aws/lambda/investor-reporting/ops/
infra/aws/lambda/investor-reporting/_contracts/
docs/contracts/investor-reporting/v1/
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R7_Y.md</decomp_doc>
<owned_cells>AR-y-71</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR71-y-AC1 AR71-y-AC2. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~52/IRPT_ANLREQ.TO-AR-y-71.report-read-bound-to-its-ticket.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-71`. Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> AR71-y-AC1,AR71-y-AC2`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: RUN -- by reading: 1 producer of the stored ticket_id (acceptance.py:120-121) and the report read's module named, read by the issuer; NOT seen by the issuer: the route the Open control calls and every other caller of that read (the worker finds both; the release pair will census the portal readers of the new refusal). comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or removed; one existing route gains an optional selector. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no identity or permission changes; who may read a request is unchanged and checked first.
comp-adversary: RUN -- by reading 2 files (acceptance.py, submission.py) of the 3 the cell touches; NOT seen: owned_report.py's read path. The lens: the check turning into an oracle (a refusal that names the request's real ticket), or a refusal for callers who send nothing. The face forbids the first and pins the second with a test of byte equality.
lane: the ops read and its tests, the route's contract documents, the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on CTO msg 4955 item (b). `AR71-y-AC1` base: FAIL as expected (no test file). `AR71-y-AC2` base: read in the issuance commit.
- The count of requests with no stored `ticket_id` is NOT this cell's: decomposition, last-but-one section.
- Seating: slot ~52 is reused; its earlier orders are terminal.
