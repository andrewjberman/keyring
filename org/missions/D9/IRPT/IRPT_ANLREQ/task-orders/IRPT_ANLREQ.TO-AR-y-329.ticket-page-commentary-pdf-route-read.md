# TO IRPT_ANLREQ.TO-AR-y-329.ticket-page-commentary-pdf-route-read -- the ticket page's commentary PDF reader read: what `analysis-request-pdf` serves, whether it can serve the standalone commentary PDF named by `pdf_ref`, what the portal client lacks, and the smallest change set; READ ONLY, one record, no source change

<to_id>IRPT_ANLREQ.TO-AR-y-329</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~137</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>40</round>
<workstream>ZO</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a read of source and a record; nothing is changed, called or deployed)
**Decomp cell:** `AR-y-329` (`decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~137`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-137` (branch `wk-IRPT_ANLREQ-137`), provisioned by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~137 <0.9.0_WK_IRPT_ANLREQ~137@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `IRPT_ANLREQ-D2-W137-S<k>` (take the next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`. No live call, NO PUSH, no AWS call of any kind, no edit of any source file. Scratch outside the product tree.

### THE CELL (`AR-y-329`, inlined) -- a READ. The product tree is not edited.

*Context. PRD ADDENDUM v0.10 makes the AI commentary a STANDALONE branded Opal PDF, which `AR-y-327` (merged) retains under family `YCHARTS_OPAL_REPORT`, logical id `<request_id>-commentary-<sha256 of the commentary ref>`, and which `opal_packager.handle_commentary_ready` attaches to the ticket as the `pdf_ref` pointer (an I7 ref `{artifact_id, sha256, version_id}` as a canonical JSON string). The Ticket Center page (`C:/dev/wk-irpt-anlreq-137/portal/src/pages/TicketCenter/AnalysisRequestParts.tsx`, about lines 308-338 and 495-520) lists four attachments; its 'Commentary' item points at `commentary_ref` (the draft JSON) and has NO reader; a separate kind `pdf` has a reader slot `getAnalysisRequestPdf` described as 'the signed-link reader for `.../requests/{requestId}/pdf`; the client has no such call TODAY'. The issuer must know what the backend route serves and what the portal client lacks, before the ticket-page reader is cut.*

Answer these four questions from SOURCE, each with `file:line` evidence read from the worktree (print the lines you cite; a line you did not read is not cited):

1. **Q1, what the route serves.** The operation `analysis-request-pdf` (`GET /api/scoped/investor-reporting/analysis/requests/{requestId}/pdf`, registered in `infra/aws/lambda/investor-reporting/reports/status_installed.py` about line 61 and `ops/entry.py` about line 240). Find its HANDLER (a name search over `infra/aws/lambda/investor-reporting/`). Which artifact does it return for a request id: the Overview `overview.pdf`, the packager's retained PDF, or something else, and how is it keyed (by request id alone, by artifact id, by family and logical id)? Who may call it (the principal classes and the firm binding)? What does it return (the shape of `signedUrl`)? Say if the route is registered in the portal's served table as well.
2. **Q2, can it serve the commentary PDF.** Given a ticket whose `package.pdf_ref` is an I7 ref to the commentary PDF of `AR-y-327`, can this route return THAT PDF today? If it serves another artifact for the request id (for example the report's `overview.pdf`), say exactly which and what change would make it serve the artifact named by `pdf_ref` instead: a backend change (name the file and function), a portal change, or both; and say whether the backend change is a member of the investor-reporting RESIDENT or LAMBDA package (so it rides a release).
3. **Q3, the portal client.** Does `C:/dev/wk-irpt-anlreq-137/portal/src/api/endpoints/investor-reporting.ts` (and the client factory `createInvestorReportingApi`) already define `getAnalysisRequestPdf` and `getAnalysisRequestOriginal`? Where is the operation table the client reads (file:line), and what exactly is missing for `PackageFiles` in `AnalysisRequestParts.tsx` to open a PDF through the viewer's own session? Cite the existing `packageFileHasReader` / `openPackageFile` lines and the tests that pin the 'Commentary' item (names under `src/pages/TicketCenter/__tests__/`: `commentary-package.test.tsx`, `package-open*.tsx`, `package-form-item.test.tsx`) and say which assertions a change of the Commentary item to the PDF would re-pin.
4. **Q4, the smallest change set.** In one paragraph: the SMALLEST set of changes (portal-only, or backend plus portal) that makes the ticket page's 'Commentary' item open the standalone commentary PDF through the viewer's session, with the file and function of each change, and whether each can ride the J7/AR-y-317 portal candidates or needs its own. End with ONE line: `RECOMMEND: PORTAL_ONLY` or `RECOMMEND: BACKEND_AND_PORTAL` or `RECOMMEND: OTHER <why>`, and the one fact that decides it. You recommend; the CTO rules.


### Deliverable and ACCEPTANCE

Write `C:/dev/wk-irpt-anlreq-137/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~137/r41/COMMENTARY_PDF_ROUTE_READ.json` with keys: `base` (the sha your branch started from), `q1` {`handler` {file, line, text}, `serves` (`overview_pdf`|`package_pdf`|`by_ref`|`other`), `keyed_by` (string), `callers` (string), `returns` (string), `evidence` (list)}, `q2` {`can_serve_commentary_pdf` (`yes`|`no`|`unknown`), `serves_instead` (string or null), `change_needed` (string), `rides` (`resident`|`lambda`|`portal`|`none`|`unknown`), `evidence`}, `q3` {`client_has_getAnalysisRequestPdf` (true|false), `client_has_getAnalysisRequestOriginal` (true|false), `op_table` {file, line, text}, `missing` (string), `tests_to_repin` (list of strings), `evidence`}, `q4` {`change_set` (list of {file, function, change}), `recommend` (`PORTAL_ONLY`|`BACKEND_AND_PORTAL`|`OTHER`), `deciding_fact` (string)}, and `not_read` (what you did not read: the live system, the deployed bytes). Then write `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~137/shape_check.py` and `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~137/cite_check.py` named below. Every cited `{file, line, text}` is a path relative to the worktree root.

<criterion id="AR329-y-AC1" cell_refs="AR-y-329"><invocation>python C:/dev/wk-irpt-anlreq-137/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~137/shape_check.py</invocation><expect>^SHAPE-OK </expect></criterion>
`AR329-y-AC1`: `shape_check.py` loads `r41/COMMENTARY_PDF_ROUTE_READ.json` and prints `SHAPE-OK <keys>` only when every key above is present with an allowed value (`q1.serves`, `q2.can_serve_commentary_pdf`, `q2.rides`, `q4.recommend` in their enums) and every answer block has at least one evidence item; otherwise `SHAPE-BAD <why>`, exit 1.

<criterion id="AR329-y-AC2" cell_refs="AR-y-329"><invocation>python C:/dev/wk-irpt-anlreq-137/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~137/cite_check.py</invocation><expect>^CITES-OK </expect></criterion>
`AR329-y-AC2`: `cite_check.py` re-opens every `{file, line, text}` of the record and prints `CITES-OK <n> of <n>` only when each cited line number exists and the cited `text` is a substring of that line (after stripping); a miss prints `CITES-BAD <file>:<line>` and exits 1. It prints the denominator n.

<criterion id="AR329-y-AC3J" cell_refs="AR-y-329" judgment="true"/>
`AR329-y-AC3J` (judgment, graded at L9, never by you): the answers follow from the cited lines, a "not found" is said plainly with what was searched, and the recommendation is the one the evidence supports.

<expected_criteria>AR329-y-AC1 AR329-y-AC2 AR329-y-AC3J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~137/` and this order's file (status flip only). You edit NO source file; the product tree is READ ONLY.
- If a cited file does not exist at the path named, find the file that now holds the function (a name search), cite that, and say so in the record.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R40A_Y.md</decomp_doc>
<owned_cells>AR-y-329</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~137/IRPT_ANLREQ.TO-AR-y-329.ticket-page-commentary-pdf-route-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-329`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR329-y-AC1,AR329-y-AC2,AR329-y-AC3J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a read of source and one record; nothing is changed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no policy change.
comp-adversary: RUN -- by reading the cell against the answer shape; the lens: an answer asserted without a read line, a 'not found' said without a search, a binding assumed set because a name exists, a recommendation that widens beyond the cell. The cell requires cited lines checked by script, a stated search for every absence, and a stated recommendation. NOT seen (blind): the live system and the deployed bytes; denominator: 4 questions, each answered with cited lines.
</preflight>

---

## RECORD FACE

- Cut on the CTO's ADDENDUM v0.10 item 2 (the ticket page's reader for the commentary PDF) after `AR-y-327` merged (`6240c0530d`). Workstream `ZO` of round 40. Risk LOCAL: the cell reads source and writes a record. Base: `AR329-y-AC1` and `AC2` FAIL as expected.
- Its output decides whether the ticket-page reader cell is portal-only or also needs a backend member in the resident release; nothing is changed by this cell.
