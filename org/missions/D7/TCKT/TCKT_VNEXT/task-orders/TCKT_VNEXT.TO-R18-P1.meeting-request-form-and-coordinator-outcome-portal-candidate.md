# TO TCKT_VNEXT.TO-R18-P1 -- BUILD the Meeting Request form, the coordinator's confirm-or-propose controls and the filer's reading of the outcome as a portal CANDIDATE (nothing is pushed or landed)

<to_id>TCKT_VNEXT.TO-R18-P1</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~42</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** SERVED (a portal change that reaches users by a merge-forward and a promote; the worker lands, pushes and deploys NOTHING)
**Decomp cell:** `R18-mt-3` (`decompositions/TCKT_VNEXT_DECOMP_R18.md`) | **outcome_ref:** FWD-11 | **depends_on:** none (the wire shape is fixed by the contract; the live route is `R18-mt-1`'s and the release is `R18-mt-4`'s)

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~42`.
- **Worktree:** `C:/dev/wk-tckt-vnext-42` (branch `wk-TCKT_VNEXT-42`), with a portal worktree `C:/dev/wk-tckt-vnext-42/portal` (branch
  `wk-TCKT_VNEXT-42-portal`) provisioned by the issuer at the portal repository's `origin/DEV` tip. Commit the WORKSPACE files (the deliverables
  folder, this order's flip) with `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~42 <0.9.0_WK_TCKT_VNEXT~42@opal.agent>" -F <msgfile> -- <paths>`; the PORTAL
  source is committed INSIDE the portal worktree (`git -C C:/dev/wk-tckt-vnext-42/portal ...`), giving the committer identity on the command line if it has none.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ`; a row id has the form `TCKT_VNEXT-D2-W42-S<k>`
  (next free `<k>`). The workspace worktree shows ` M portal` (and may show a modified `.parquet` fixture): never commit either to the WORKSPACE
  repository. Every `.py` you add passes `bash .tools/commit-gate.sh <file>` (Python 3.9 syntax). No non-ASCII in what you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS
  row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call, NO PUSH of any branch, no deploy, no upload. Scratch
  outside the product tree. Read `portal/CLAUDE.md` (color law: new surfaces follow the neighbouring panel's idiom; typecheck is `bun run typecheck`).

### THE CELL (`R18-mt-3`, inlined) -- a portal CANDIDATE. Nothing is landed, pushed or deployed.

*PRD v0.6 C-MEETING-REQUEST and FWD-11: an Opal staff person files a Meeting Request (firm, who, purpose, up to three proposed times) in the
Ticket Center; the ticket lands in the meeting coordinator's queue; the coordinator CONFIRMS one proposed time or PROPOSES other times on the
ticket; the filer sees the outcome on the same ticket. In-house, no Calendly, no mail.*

The contract is `org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R18.md`, section WIRE CONTRACT: item 1 (the route
`POST /api/scoped/tickets/{ticketId}/meeting`, its two body shapes, the stored `meeting` member) and the `meeting_request` CREATE paragraph
(answers `firm`, `who`, `purpose`, `proposed_time_1`, optional `proposed_time_2` and `proposed_time_3`). Read first: `src/pages/TicketCenter/TicketCenter.tsx`
(the `showCreate` panel about lines 458-521, `handleCreate` about 383, the board rows about 589-637, `AnalysisRequestFields` and how `firms` /
`firmsFailed` are loaded for the analysis form), `src/pages/TicketCenter/AnalysisRequestParts.tsx` and `analysisRequest.ts` (the filer's firm
choice: reuse that source and its failure state), `src/api/endpoints/tickets.ts` (`Ticket`, `CreateTicketInput`, `createTicket`,
`recordCommentarySent` as the model of a POST on a ticket), and the tests in `src/pages/TicketCenter/__tests__/` (copy the style).

1. **The branch.** After a permitted `git fetch origin`, record `base_tip` (the full sha of the portal worktree's HEAD). After your commit,
   create the LOCAL candidate branch `cand/dell2/tckt-meeting-request` at that commit. Never push it.
2. **The change (`src/` only; the files you may touch are exactly):**
   - `src/api/endpoints/tickets.ts`: the `meeting_request` answer type, the `meeting` member on `Ticket`, and `recordMeetingOutcome(ticketId, body)`
     (a POST to the route, same client and error handling as `recordCommentarySent`).
   - `src/pages/TicketCenter/MeetingRequestParts.tsx` (NEW): `MeetingRequestForm` (firm choice from the same served-firm source as the analysis
     form, `who`, `purpose`, three time inputs of which the first is required; submit creates the ticket with those `answers` through
     `createTicket`, title built as `Meeting: <who>`), `MeetingOutcomeControls` (for one ticket: shows the proposed times, a Confirm button per time and
     a Propose control taking up to three times; calls `recordMeetingOutcome`; shows a refusal in words), and `MeetingOutcomeLine` (reads
     `ticket.meeting`: `Confirmed for <time> by <who> on <date>` or `New times proposed: <times>`; with no `meeting` it says `Waiting for the coordinator`).
   - `src/pages/TicketCenter/TicketCenter.tsx`: the create panel renders `MeetingRequestForm` when the chosen type is `meeting_request` (the generic
     title and details inputs are hidden for it, as for `trade_request`); the board shows, for a `meeting_request` ticket that is not completed, a row
     under it with `MeetingOutcomeLine` and, for the INTERNAL viewer, `MeetingOutcomeControls` (the server decides who may act: the page shows the
     controls to every internal viewer and shows the server's refusal in words). Touch no other branch of this file.
   - `src/pages/TicketCenter/__tests__/meeting-request.test.tsx` (NEW).
   Any other file is a BLOCKING row. `TradeRequestParts.tsx` and the trade branch of the file are `TO-R18-P2`'s: do not touch them.
3. **The tests (run with `bun test <file>` from the portal worktree).** One named test per case: the form refuses to submit without firm,
   `who`, `purpose` or the first time; a valid form calls `createTicket` once with `ticket_type` `meeting_request` and exactly the answers
   (empty optional times omitted); the firm list failing shows the words the analysis form shows and disables submit; the coordinator controls
   call `recordMeetingOutcome` with `{action:'confirm', time}` for the clicked time and `{action:'propose', times}` for 1 to 3 times, and refuse
   0 or 4 times before calling; a server refusal (403, 409) is shown in words and the board is not changed; `MeetingOutcomeLine` shows each of
   its three states; the controls do not render for a `completed` ticket or another ticket type; the trade, analysis, service and other branches of
   the create panel render as before (a test per branch).
4. **Commit** inside the portal worktree; record the full sha, and `git -C ... diff --name-only <base_tip> <commit>` printing exactly the paths of
   step 2. Run `bun run typecheck` once and record rc (a drain check, not a criterion).
5. **Write `r18/PORTAL_MEETING_CANDIDATE.json`** in your deliverable folder: `base_tip`, `branch`, `candidate_branch`, `commit`, `files_changed`, `tests`
   {`added`, `passed`, `failed`, `folders`}, `before_arm` (the new tests run on `base_tip` without your change: they FAIL), `what_a_person_sees` (the
   form, the controls and the outcome line, in words), `claim`, `not_read` (the live route and the rendered page: the issuer takes the screenshot).
6. **Write the three checker scripts** named in ACCEPTANCE into your deliverable folder.

### ACCEPTANCE

<criterion id="R18P1-AC1" cell_refs="R18-mt-3"><invocation>python C:/dev/wk-tckt-vnext-42/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~42/portal_check_mt3.py</invocation><expect>^PORTAL-TESTS-OK </expect></criterion>
`R18P1-AC1`: you write `portal_check_mt3.py`: it runs `bun test` on the new test file AND on the whole `src/pages/TicketCenter` folder in
`C:/dev/wk-tckt-vnext-42/portal`, parses the counts, and prints `PORTAL-TESTS-OK <new passed> new, <folder passed> folder, 0 failed` only when
the new file has every case of step 3 passing and the folder has 0 failed; otherwise `PORTAL-TESTS-BAD <why>` and exit 1.

<criterion id="R18P1-AC2" cell_refs="R18-mt-3"><invocation>python C:/dev/wk-tckt-vnext-42/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~42/mutant_check_mt3.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`R18P1-AC2` (the one mutant that fails): you write `mutant_check_mt3.py`: it copies `MeetingRequestParts.tsx` to a scratch folder OUTSIDE the product
tree with the confirm path changed to send the FIRST proposed time whatever was clicked, runs the new test file against the copy, and prints
`MUTANT-FIRES` only when that run FAILS (else `MUTANT-SURVIVES`, exit 1).

<criterion id="R18P1-AC3" cell_refs="R18-mt-3"><invocation>python C:/dev/wk-tckt-vnext-42/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~42/scope_check_mt3.py</invocation><expect>^SCOPE-OK</expect></criterion>
`R18P1-AC3` (a third check, with a reason: the cell is a client-facing page candidate, so its scope is what the approver reads): you write `scope_check_mt3.py`: it prints
`SCOPE-OK` only when `git -C C:/dev/wk-tckt-vnext-42/portal diff --name-only <base_tip> cand/dell2/tckt-meeting-request` is exactly the four paths of step 2 and the
diff of `TicketCenter.tsx` adds no line that mentions `trade_request`, `TradeRequestForm` or `analysis_request`; otherwise `SCOPE-BAD <why>`, exit 1.

<criterion id="R18P1-AC4J" cell_refs="R18-mt-3" judgment="true"/>
`R18P1-AC4J` (judgment, graded at L9, never by you): a staff person finds the Meeting Request form in the Ticket Center in plain words, the
coordinator's two actions are unmistakable, the filer reads the outcome on the same ticket, nothing says a mail or invite was sent, and nothing was
pushed or landed.

<expected_criteria>R18P1-AC1 R18P1-AC2 R18P1-AC3 R18P1-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~42/` and this order's file (status flip
  only), and the portal source and test files of step 2 INSIDE the portal worktree. If a test OUTSIDE the grant fails because of your change, STOP: file
  a BLOCKING row naming it; the issuer amends the grant.
- **Shared files:** `tickets.ts` and `TicketCenter.tsx` are also edited by your next order (`TO-R18-P2`, the trade form). Touch only the meeting
  parts so the two merge cleanly. READ only: everything else.

<paths>
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R18.md</decomp_doc>
<owned_cells>R18-mt-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~42/TCKT_VNEXT.TO-R18-P1.meeting-request-form-and-coordinator-outcome-portal-candidate.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R18-P1`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R18P1-AC1,R18P1-AC2,R18P1-AC3,R18P1-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a candidate branch in a worker worktree; nothing is landed, pushed or deployed. comp-routes: DECLARED-NOT-APPLICABLE -- the route is `R18-mt-1`'s and `R18-mt-2`'s; this cell calls it only through a faked client. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: RUN -- by reading C-MEETING-REQUEST, C-FIRM-CHOICE and `portal/CLAUDE.md` against this cell; the lens: a firm typed into the body instead of chosen from the served list, a Confirm that sends a different time than the clicked one, controls shown on a completed or other-type ticket, copy that says a mail or invite was sent, a light-on-white idiom on a white surface. BLIND to: the live route and the rendered page (denominator: 1 cell and 3 contract rows read).
</preflight>

---

## RECORD FACE

- Cut on PRD v0.6 @c578883de8. First of the two orders in slot 42's queue; round 18 chain C with `TO-R18-P2`. Base: `R18P1-AC1`, `AC2` and `AC3` FAIL as expected (no test file, no checkers).
- It is a client-facing candidate by class: the DEV landing waits on Andrew's approval row (`open-calls.py approval-lease`); the issuer files it at the drain. Portal law: `portal/CLAUDE.md` and CLAUDE.md "Portal".
