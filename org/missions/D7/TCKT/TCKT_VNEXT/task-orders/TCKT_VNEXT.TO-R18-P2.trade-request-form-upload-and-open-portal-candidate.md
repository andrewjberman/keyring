# TO TCKT_VNEXT.TO-R18-P2 -- BUILD the Trade Request as a form upload (firm, file, submit) and its open-from-the-ticket control as a portal CANDIDATE, with the engine submit unwired (nothing is pushed or landed)

<to_id>TCKT_VNEXT.TO-R18-P2</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~42</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** SERVED (a portal change that reaches users by a merge-forward and a promote; the worker lands, pushes and deploys NOTHING)
**Decomp cell:** `R18-tf-4` (`decompositions/TCKT_VNEXT_DECOMP_R18.md`) | **outcome_ref:** FWD-10 | **depends_on:** `R18-mt-3` (same slot, same files: start after `TO-R18-P1` is terminal and its commit is in your portal branch); the live routes are `R18-tf-2`'s, faked here

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~42` (the same worker, continued; worktree `C:/dev/wk-tckt-vnext-42`, portal worktree `C:/dev/wk-tckt-vnext-42/portal`).
Commit the workspace files with `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~42 <0.9.0_WK_TCKT_VNEXT~42@opal.agent>" -F <msgfile> -- <paths>` and the
portal source inside the portal worktree. The rules of `TO-R18-P1`'s face stand (Write tool for message files, rows `TCKT_VNEXT-D2-W42-S<k>`, each `.py` through
`bash .tools/commit-gate.sh`, no non-ASCII, a `controls.mutant` that FIRES, NO live call, NO PUSH, no deploy, no upload; read `portal/CLAUDE.md`).

### THE CELL (`R18-tf-4`, inlined) -- a portal CANDIDATE. Nothing is landed, pushed or deployed.

*PRD v0.6 C-TRADE-REQUEST and FWD-10: an Opal staff person chooses Trade Request, chooses the firm, uploads the trade request form and submits;
the OPEN ticket carries the form as an attachment opened from the ticket page. NO trade is sent anywhere: the engine submit that the held form
(`TradeRequestParts.tsx`, NFRA_OPSWKF, released to this project by the CTO msg 7818) made after creating the ticket is UNWIRED. Until the real form
arrives, a placeholder form is named as such on the screen; the real form is a swap of that one file.*

The contract is `decompositions/TCKT_VNEXT_DECOMP_R18.md`, section WIRE CONTRACT: item 2 (`POST /api/scoped/tickets/attachment-upload`), item 3
(`GET /api/scoped/tickets/{ticketId}/attachment`) and the `trade_request` CREATE paragraph. Read first: `src/pages/TicketCenter/TradeRequestParts.tsx`
(the whole file: its two calls, `submitBodyFromForm`, `submitTradeBody`, `TradeRequestForm`), `src/pages/TicketCenter/__tests__/trade-request.test.tsx` and
`commentary-sent.test.tsx` (they name `trade_request`), `TicketCenter.tsx` (the `trade_request` branches about lines 476-488 and 512), `tickets.ts`, and the
analysis form's firm-choice source (as in `TO-R18-P1`).

1. **The branch.** Record `base_tip`; after your commit create the LOCAL candidate branch `cand/dell2/tckt-trade-form-upload` at it (on top of the
   `TO-R18-P1` commit: say so in the record). Never push it.
2. **The change (`src/` only; the files you may touch are exactly):**
   - `src/api/endpoints/tickets.ts`: `TicketAttachment` gains the trade form's member set; `requestAttachmentUpload({firm, filename, content_type, size})`
     (POST to the upload route) and `getTicketAttachmentUrl(ticketId)` (GET the open route), same client and error handling as the neighbours.
   - `src/pages/TicketCenter/TradeRequestParts.tsx`: `TradeRequestForm` becomes: a firm choice (the served-firm source of the analysis form, with its failure
     state), a file input accepting `.pdf,.xlsx,.csv` with the 10 MB cap checked before any call, the placeholder note (`This is the placeholder form; the final
     trade request form replaces it.` or equivalent plain words), and a Submit that does, in order: (a) `requestAttachmentUpload`; (b) a `fetch` PUT of the
     file bytes to the returned `upload_url` with the same `Content-Type`; (c) `createTicket({ticket_type:'trade_request', title:'Trade request: <firm>', description:'',
     answers:{firm}, attachment})` with exactly the attachment object step (a) returned. A failure at any step stops there and says which step in words; a
     failure after (b) keeps nothing hidden (the file is uploaded, no ticket exists: say so and offer Retry of step (c) only). The engine call
     (`submitTradeBody`, `/api/general/trades/submit`, `submitBodyFromForm`) is REMOVED from this form's flow: delete what nothing else imports and list each
     remaining export you kept with the importer that needs it.
   - `src/pages/TicketCenter/TicketCenter.tsx`: for a `trade_request` ticket that carries an `attachment`, the board shows an `Open form` control that calls
     `getTicketAttachmentUrl` and opens the URL in a new tab (`window.open(url, '_blank', 'noopener')`), refusing in words when the call fails; the create panel's
     `trade_request` branch keeps its existing placement and `onFiled` handling. Touch no meeting, analysis, service or other branch.
   - `src/pages/TicketCenter/__tests__/trade-form-upload.test.tsx` (NEW), and the existing `trade-request.test.tsx` re-pinned ONLY where the engine flow it
     pinned is now unwired: list each re-pinned case with its old and new assertion, delete none silently, and keep every case that is still true.
   Any other file is a BLOCKING row.
3. **The tests (run with `bun test <file>` from the portal worktree).** One named test per case: Submit is disabled until a firm and a file are chosen; a
   file over 10485760 bytes or of another extension is refused before any call; the three calls happen in order with the upload's returned attachment passed
   unchanged to `createTicket`; the PUT carries the file's content type; a failure of (a), of (b) and of (c) each stops with its own words, and after (b) a Retry
   calls only (c); NO call to `/api/general/trades/submit` happens on any path (a spy on the client); the placeholder note is on the screen; `Open form` appears only
   for a `trade_request` ticket with an attachment, calls `getTicketAttachmentUrl` once and opens the returned URL in a new tab; its failure is shown in words; the
   meeting, analysis, service and other branches render as before.
4. **Commit** inside the portal worktree; record the full sha, and `git -C ... diff --name-only <base_tip> <commit>` printing exactly the paths of step 2. Run
   `bun run typecheck` once and record rc (a drain check, not a criterion).
5. **Write `r18/PORTAL_TRADE_FORM_CANDIDATE.json`**: `base_tip`, `branch`, `candidate_branch`, `commit`, `files_changed`, `tests`, `before_arm`, `kept_exports` (each
   with its importer), `repinned` (case by case), `what_a_person_sees`, `claim`, `not_read` (the live routes, the bucket's CORS, the rendered page: the issuer takes
   the screenshot).
6. **Write the three checker scripts** named in ACCEPTANCE.

### ACCEPTANCE

<criterion id="R18P2-AC1" cell_refs="R18-tf-4"><invocation>python C:/dev/wk-tckt-vnext-42/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~42/portal_check_tf4.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`R18P2-AC1`: you write `portal_check_tf4.py`: it runs `bun test` on the new test file AND on the whole `src/pages/TicketCenter` folder in `C:/dev/wk-tckt-vnext-42/portal`,
parses the counts, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when the new file has every case of step 3 passing and the folder
has 0 failed; otherwise `PORTAL-TESTS-BAD <why>` and exit 1.

<criterion id="R18P2-AC2" cell_refs="R18-tf-4"><invocation>python C:/dev/wk-tckt-vnext-42/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~42/mutant_check_tf4.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`R18P2-AC2` (the one mutant that fails): you write `mutant_check_tf4.py`: it copies `TradeRequestParts.tsx` to a scratch folder OUTSIDE the product tree with the engine submit call
put back after the ticket is created, runs the new test file against the copy, and prints `MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="R18P2-AC3" cell_refs="R18-tf-4"><invocation>python C:/dev/wk-tckt-vnext-42/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~42/scope_check_tf4.py</invocation><expect>^SCOPE-OK</expect></criterion>
`R18P2-AC3` (a third check, with a reason: the cell is a client-facing page candidate and unwires an engine call, so its scope is what the approver reads): you write `scope_check_tf4.py`: it prints
`SCOPE-OK` only when `git -C C:/dev/wk-tckt-vnext-42/portal diff --name-only <base_tip> cand/dell2/tckt-trade-form-upload` lists only the paths of step 2 and the files of `TO-R18-P1`'s candidate (the
meeting files, which you inherit), AND no file under `src/` outside `src/pages/TicketCenter/` and `src/api/endpoints/tickets.ts` changed, AND `grep` of the candidate tree finds no import of
`submitTradeBody` in `src/pages/TicketCenter/`; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="R18P2-AC4J" cell_refs="R18-tf-4" judgment="true"/>
`R18P2-AC4J` (judgment, graded at L9, never by you): a staff person files a Trade Request by choosing a firm and uploading the form in plain words, the placeholder is named
as a placeholder, nothing on the page says a trade was sent, the ticket's form opens from its row, and nothing was pushed or landed.

<expected_criteria>R18P2-AC1 R18P2-AC2 R18P2-AC3 R18P2-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~42/` and this order's file (status flip only), and the portal
  source and test files of step 2 INSIDE the portal worktree. If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it.
- READ only: everything else, including the trade engine's backend and `NFRA_OPSWKF`'s tree (that project is on HOLD; its engine path and its 409 defect stay there).

<paths>
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R18.md</decomp_doc>
<owned_cells>R18-tf-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~42/TCKT_VNEXT.TO-R18-P2.trade-request-form-upload-and-open-portal-candidate.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R18-P2`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R18P2-AC1,R18P2-AC2,R18P2-AC3,R18P2-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a candidate branch in a worker worktree; nothing is landed, pushed or deployed. comp-routes: DECLARED-NOT-APPLICABLE -- the routes are `R18-tf-2`'s and `R18-tf-3`'s; this cell calls them only through a faked client. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: RUN -- by reading C-TRADE-REQUEST, C-ATTACH and the held form against this cell; the lens: an engine call that survives the rework, a firm typed rather than chosen, a retry that re-uploads or double-files, copy that says a trade was sent, a placeholder that reads as final. BLIND to: the live routes, the bucket's CORS (a laptop request) and the rendered page (denominator: 1 cell and 3 contract rows read).
</preflight>

---

## RECORD FACE

- Cut on PRD v0.6 @c578883de8 and the CTO's release of `TradeRequestParts.tsx` (msg 7818). Second order of slot 42's queue; round 18 chain C. Base: `R18P2-AC1`, `AC2` and `AC3` FAIL as expected (no test file, no checkers).
- Client-facing candidate by class: the DEV landing waits on Andrew's approval row; the issuer files it at the drain. The browser PUT to the bucket needs the bucket's CORS (the laptop's role request).
