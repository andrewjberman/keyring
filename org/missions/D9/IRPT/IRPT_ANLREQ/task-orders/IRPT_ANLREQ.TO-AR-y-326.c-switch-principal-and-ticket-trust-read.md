# TO IRPT_ANLREQ.TO-AR-y-326.c-switch-principal-and-ticket-trust-read -- the C-SWITCH read: which principal a ticket-filed Analysis Request reaches the producer as, and what in the accepted record can be trusted to say "this came from a ticket"; READ ONLY, one record, no source change

<to_id>IRPT_ANLREQ.TO-AR-y-326</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~135</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of source and a record; nothing is changed, called or deployed)
**Decomp cell:** `AR-y-326` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 (the producer switch for ticket-filed requests) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~135`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-135` (branch `wk-IRPT_ANLREQ-135`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~135 <0.9.0_WK_IRPT_ANLREQ~135@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W135-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`. No live call, NO PUSH, no AWS call of any kind, no edit of any source file. Scratch outside the product tree.

### THE CELL (`AR-y-326`, inlined) -- a READ. The product tree is not edited.

*Context. The Opal producer (the Opal engine's report and commentary) serves a request only when the producer switch says so. Today the switch is `OPAL_PRODUCER_PRINCIPALS = ("andrew@opalinvest.com",)` and `producer_for(record)` in `C:/dev/wk-irpt-anlreq-135/infra/aws/lambda/investor-reporting/ycharts/generate/resident_worker.py` (about lines 159-177) returns "OPAL" only when the accepted record's `owner.principal_id` is on that list. FWD-1's driven filer is a synthetic Opal STAFF user who files an Analysis Request in the Ticket Center; the request reaches the producer as whatever principal the accepted record carries. The CTO's ruling (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_DELL2_PIVOT_FIRST_ACTS_20261013.md`, "Act 2") asks for ONE read first: which principal does `producer_for` receive for a ticket-filed request, from code (the route, the entry and the worker)? If it is a service principal, that one principal is added to the list. If it is the filer's own principal, the switch is keyed on the request carrying a `ticket_id` that the ticket table confirms is an `analysis_request` ticket, and no human principal is added. Your record is the evidence that ruling needs.*

Answer these four questions from SOURCE, each with `file:line` evidence read from the worktree (print the lines you cite; a line you did not read is not cited):

1. **Q1, the principal.** Trace a ticket-filed Analysis Request from the portal's three posts (`C:/dev/wk-irpt-anlreq-135/portal/src/pages/TicketCenter/analysisRequest.ts`: the ticket create, `deps.ir.uploadAnalysisInput`, the analysis submit) through the Investor Reporting entry (`infra/aws/lambda/investor-reporting/` handlers and `_scope/`), the acceptance writer (`ycharts/generate/acceptance.py`, `submission.py`, `composition_admission.py`) to the accepted record's `owner` and its `principal_id`. What value does `owner.principal_id` take for a signed-in Opal STAFF user (an internal, OPAL_GLOBAL-class viewer)? Is it the user's sign-in email, a user id, or a service principal? Name the function that sets it.
2. **Q2, the ticket marker.** Who sets `ticket_id` on the accepted record (`acceptance.py` about line 136; `submission.py` `PUBLIC_FIELDS` and the `ticket_id` rule about line 78)? Is it a field the CLIENT sends in the analysis submit body (so a request can carry any well-formed ticket id), or is it server-set after reading the ticket? State which, with the lines.
3. **Q3, confirmation against the ticket table.** Does ANY code in the Investor Reporting backend (the entry, the acceptance, the resident worker, `ycharts/research/opal_packager.py`'s `live_ticket_ports`) read the ticket table or the ticket service to confirm that a `ticket_id` names a real `analysis_request` ticket, before the producer is chosen? If a reader exists, name it and the identity it presents. If none exists, say so, and name the SMALLEST existing port or secret the resident already holds toward the ticket service (`live_ticket_ports` config keys `api_base`, `secret_name`; the packager's `svc-irpt-packager` token) and whether that identity could read a ticket by id (read the ticket service's route table in `infra/aws/lambda/ticket_center/lambda_function.py` for a GET by ticket id and who may call it). Do not call anything.
4. **Q4, the two shapes of the switch.** In one paragraph each, from Q1 to Q3: (A) what would adding the principal in Q1 to `OPAL_PRODUCER_PRINCIPALS` let through (every request that principal files, ticket or not)? (B) what would "key on `ticket_id` confirmed by the ticket table" need (a ticket read by the resident, which identity, which grant) and what remains forgeable without it? End with ONE line: `RECOMMEND: A` or `RECOMMEND: B` or `RECOMMEND: NEITHER <why>`, and the one fact that decides it. You recommend; the CTO rules.

### Deliverable and ACCEPTANCE

Write `C:/dev/wk-irpt-anlreq-135/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~135/r41/C_SWITCH_READ.json` with keys: `base` (the sha your branch started from), `q1` {`principal_id_value`, `kind` (`email`|`user_id`|`service`|`other`), `setter` (function name), `evidence` (list of `{file, line, text}`)}, `q2` {`set_by` (`client`|`server`), `evidence`}, `q3` {`reader_exists` (true|false), `reader` (name or null), `identity`, `could_read_by_id` (`yes`|`no`|`unknown`), `evidence`}, `q4` {`a`, `b`, `recommend` (`A`|`B`|`NEITHER`), `deciding_fact`}, `not_read` (what you did not read: the live system, the deployed bytes, the portal in PROD). Then write `deliverables/0.9.0_WK_IRPT_ANLREQ~135/cite_check.py` and `shape_check.py` named below.

<criterion id="AR326-y-AC1" cell_refs="AR-y-326"><invocation>python C:/dev/wk-irpt-anlreq-135/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~135/shape_check.py</invocation><expect>^SHAPE-OK </expect></criterion>
`AR326-y-AC1`: `shape_check.py` loads `r41/C_SWITCH_READ.json` and prints `SHAPE-OK q1 q2 q3 q4` only when every key above is present with an allowed value, `q1.kind`, `q2.set_by`, `q3.could_read_by_id` and `q4.recommend` are in their enums, each of `q1`, `q2`, `q3` has at least one evidence item, and `q4.deciding_fact` is a non-empty string; otherwise `SHAPE-BAD <why>`, exit 1.

<criterion id="AR326-y-AC2" cell_refs="AR-y-326"><invocation>python C:/dev/wk-irpt-anlreq-135/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~135/cite_check.py</invocation><expect>^CITES-OK </expect></criterion>
`AR326-y-AC2`: `cite_check.py` re-opens every `{file, line, text}` of the record (paths relative to the worktree root) and prints `CITES-OK <n> of <n>` only when each cited line number exists and the cited `text` is a substring of that line (after stripping); a miss prints `CITES-BAD <file>:<line>` and exits 1. It also prints the denominator n.

<criterion id="AR326-y-AC3J" cell_refs="AR-y-326" judgment="true"/>
`AR326-y-AC3J` (judgment, graded at L9, never by you): the four answers follow from the cited lines, Q3 states plainly whether a confirming reader exists, and the recommendation is the one the evidence supports.

<expected_criteria>AR326-y-AC1 AR326-y-AC2 AR326-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~135/` and this order's file (status flip only). You edit NO source file; the product tree is READ ONLY.
- If a cited file does not exist at the path named, find the file that now holds the function (a name search), cite that, and say so in the record.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-326</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~135/IRPT_ANLREQ.TO-AR-y-326.c-switch-principal-and-ticket-trust-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-326`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR326-y-AC1,AR326-y-AC2,AR326-y-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record; nothing is changed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading CTO Act 2 against the cell; the lens: an answer asserted without a read line, a `ticket_id` trusted though a client sends it, a recommendation that adds a human principal to the list, a "no reader exists" said without searching the packager and the entry. The cell requires cited lines checked by script, a stated set_by, a stated reader_exists, and a recommendation that names its deciding fact. NOT seen: the live system and the deployed bytes.
</preflight>

---

## RECORD FACE

- Cut on the CTO's round-41 path (msg 7723, item 2) and the CTO's Act 2 ruling. Workstream `ZM` of round 40. Risk LOCAL: the cell reads source and writes a record in its deliverable folder. Base: `AR326-y-AC1` and `AC2` FAIL as expected (no record, no checker files).
- Its output feeds a never-widen pair (the COO half) for the C-SWITCH release, which the CTO signs; nothing is changed by this cell.
