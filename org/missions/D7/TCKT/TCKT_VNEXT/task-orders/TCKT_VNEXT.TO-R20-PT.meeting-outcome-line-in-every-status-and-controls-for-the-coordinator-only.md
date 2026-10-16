# TO TCKT_VNEXT.TO-R20-PT -- BUILD the Ticket Center's meeting outcome line in every status that carries an outcome, and the coordinator's controls for a viewer in routing.primary only (FWD-11; portal source and tests only)

<to_id>TCKT_VNEXT.TO-R20-PT</to_id>
<project>TCKT_VNEXT</project>
<issued_to>0.9.0_WK_TCKT_VNEXT~50</issued_to>
<issued_by>2.0.0_SA_COO~V2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>20</round>

**Directive:** D7 | **Fabric:** dell2 | **Risk:** LOCAL (a portal change landing on DEV only, an Opal-internal product file; the worker pushes and deploys NOTHING)
**Decomp cell:** `R20-pt-1` (`decompositions/TCKT_VNEXT_DECOMP_R20.md`) | **outcome_ref:** FWD-11 (the CTO's rounds 18-19 rulings 2 and 4); rows `TCKT_VNEXT-D2-S57` | **depends_on:** none to build

---

## WORKER FACE

You are `0.9.0_WK_TCKT_VNEXT~50`.
- **Worktree:** `C:/dev/wk-tckt-vnext-50` (workspace, branch `wk-TCKT_VNEXT-50`) and its portal worktree `C:/dev/wk-tckt-vnext-50/portal` (the portal's own repository, branch `wk-TCKT_VNEXT-50-portal`, cut from portal `DEV` at the commit the issuer names in the issuance), both provisioned by the issuer. Work and commit only there:
  - Workspace files (your record, your mutant checker): `bash .tools/safe-commit.sh --author "0.9.0_WK_TCKT_VNEXT~50 <0.9.0_WK_TCKT_VNEXT~50@opal.agent>" -F <msgfile> -- <paths>` run in the workspace worktree.
  - Portal files: `git -c user.name=0.9.0_WK_TCKT_VNEXT~50 -c user.email=0.9.0_WK_TCKT_VNEXT~50@opal.agent commit -F <msgfile>` run in the PORTAL worktree, after staging only the files you changed. **Never push, never run `bun run dev`'s proxy against the live API, never call a live endpoint.**
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form `TCKT_VNEXT-D2-W50-S<k>`. Every `.py` you add passes `bash .tools/commit-gate.sh <file>`. No non-ASCII in the Python you add.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`; every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES. No live call of any kind. **Run portal tests with `bun test <file>` from the portal worktree only.** Scratch outside the product tree.
- **Portal law you obey:** the canvas is light `#F4F6FA`; containers are white panels with a `#C4CBDB` hairline and navy ink; no light text on a white panel; ONE `#5F3BE3` primary action per view. You add NO new colour, route, write or principal. Reuse the file's existing classes.

### WHY

The CVO's `ADJUDICATION_v8` and the CTO's rounds 18-19 analysis: FWD-11 is NOT REALIZED because (1) the board draws the meeting outcome line only while `t.status !== 'completed'`, so once a meeting ticket completes the filer can no longer read the outcome on the ticket (row `TCKT_VNEXT-D2-S57`), and (2) the coordinator's two actions render for EVERY internal viewer, though only a viewer in the ticket's `routing.primary` can use them (a non-coordinator is refused by the server's 403 sentence; the actions are offered to people who cannot use them).

### THE CELL (`R20-pt-1`, inlined) -- BUILD ONLY. Nothing is pushed, deployed or called.

In the PORTAL worktree, read first: `src/pages/TicketCenter/MeetingRequestParts.tsx` (`outcomeLineWords` about line 207 and `MeetingOutcomeLine` about line 220; `MeetingOutcomeControls` about line 272, whose first lines return null for any ticket that is not a `meeting_request` or is `completed`) and `src/pages/TicketCenter/TicketCenter.tsx` (the board row: after `<AnalysisPackageRow .../>` about lines 908 to 916 a block is mounted `{t.ticket_type === 'meeting_request' && t.status !== 'completed' && (<tr><td colSpan={8} ...><MeetingOutcomeLine ticket={t} />{internal && <MeetingOutcomeControls .../>}</td></tr>)}`; the viewer is `auth` from `const auth = useAuth()` near line 205; the viewer's email is `auth.user?.email`, as `src/pages/InvestorReporting/index.tsx` line 75 reads it). The ticket type (`src/api/endpoints/tickets.ts`) has `routing: { primary: string[]; secondary: string[]; visibility: string[] }` and `meeting?: TicketMeeting | null` with `status: 'confirmed' | 'rescheduled'`, `time`, `proposed_times`, `by`, `at`.

1. **The outcome line in every status that carries an outcome.** Add and EXPORT, in `MeetingRequestParts.tsx`, a small pure function `showsMeetingOutcome(ticket)` returning true for a `meeting_request` ticket when `ticket.status !== 'completed'` OR `ticket.meeting` is present (truthy), and false for any other type. The board's meeting block mounts `MeetingOutcomeLine` when `showsMeetingOutcome(t)` is true. A COMPLETED ticket with NO `meeting` outcome shows NOTHING (never the "waiting" words on a closed ticket); a not-completed ticket with no outcome still shows the waiting words as today; a completed ticket WITH a `confirmed` or `rescheduled` outcome shows the same words an open ticket shows (`outcomeLineWords`, unchanged).
2. **The controls for the coordinator only.** Add and EXPORT a pure function `viewerIsCoordinator(ticket, email)` returning true only when `email` is a non-empty string and, compared case-insensitively after trimming, equals one entry of `ticket.routing?.primary` (a missing `routing` or `primary` is false). The board mounts `MeetingOutcomeControls` only when `internal && viewerIsCoordinator(t, auth.user?.email)`; `MeetingOutcomeControls` itself keeps returning null for a completed ticket or a non-meeting type. Every other viewer sees the outcome line and no control.
3. **Nothing else changes.** The form, the labels, the words, the server calls, the 403 sentence and every other row keep their behaviour; `AnalysisPackageRow` and the hop-failure read are untouched; no new request is made. The ONE existing assertion you may need to touch is a test that expects the controls for a viewer who is not in `routing.primary`: change only that fixture or assertion and list the old and new lines in your record; no other existing test may change.
4. **Tests** in the new file `src/pages/TicketCenter/__tests__/meeting-outcome-visibility.test.tsx` (copy the style of `__tests__/meeting-request.test.tsx`: `renderToStaticMarkup`, no network). EXACTLY these ten test names (the issuer's check scans for them verbatim):
   - `shows the waiting words on an open meeting ticket with no outcome`
   - `shows the confirmed outcome on a completed meeting ticket`
   - `shows the proposed times on a completed meeting ticket`
   - `shows nothing for a completed meeting ticket that has no meeting outcome`
   - `shows the outcome line to a viewer who is not the coordinator`
   - `shows the coordinator's controls to a viewer in routing.primary`
   - `matches the viewer's email to routing.primary without regard to case`
   - `hides the coordinator's controls from a viewer who is not in routing.primary`
   - `never shows the coordinator's controls on a completed ticket`
   - `draws no outcome line for a ticket that is not a meeting request`
   Render the SAME mount the board uses (a small exported component or the two pure functions plus the two existing components), not a copy of the logic in the test.
5. **Write `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~50/mutant_check.py`** (AC3 below) and a short `R20_PT_RECORD.json`: the lines you changed, the test counts (this file and the whole `src/pages/TicketCenter` folder), the before-arm (the ten tests on the base: every one that exercises the change FAILS), the one existing-assertion change if any, `not_read`. Render the new outcome line once to markup for a confirmed completed ticket and save it as `render_markup.txt` beside the record (DOM text only; no screenshot is taken by you).

### ACCEPTANCE

<criterion id="R20PT-AC1" cell_refs="R20-pt-1"><invocation>python C:/dev/wk-tckt-vnext-50/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_CHECKS/r20_checks.py pt-outcome --portal C:/dev/wk-tckt-vnext-50/portal</invocation><expect>^R20-PT-OK</expect></criterion>
`R20PT-AC1`: the ten named tests exist and `bun test` of the new file passes with no failure.

<criterion id="R20PT-AC2" cell_refs="R20-pt-1"><invocation>python C:/dev/wk-tckt-vnext-50/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R20_CHECKS/r20_checks.py portal-tsc --portal C:/dev/wk-tckt-vnext-50/portal</invocation><expect>^R20-TSC-OK</expect></criterion>
`R20PT-AC2`: the portal typechecks (`tsc -b`). Also run, once, the existing TicketCenter tests in the portal worktree (`bun test src/pages/TicketCenter`) and record the counts in your record (a drain check; the issuer re-runs it).

<criterion id="R20PT-AC3" cell_refs="R20-pt-1"><invocation>python C:/dev/wk-tckt-vnext-50/org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~50/mutant_check.py</invocation><expect>MUTANT-FIRES</expect></criterion>
`R20PT-AC3` (the one mutant that fails): you write `mutant_check.py`. It records the sha256 of `MeetingRequestParts.tsx` in the portal worktree, changes `showsMeetingOutcome` so that a completed ticket never shows the outcome (the old behaviour), runs `bun test src/pages/TicketCenter/__tests__/meeting-outcome-visibility.test.tsx` from the portal worktree, prints `MUTANT-FIRES` only when that run FAILS, RESTORES the file byte for byte (sha256 equal to the recorded one) and prints `RESTORED`; else `MUTANT-SURVIVES`, exit 1.

<criterion id="R20PT-AC4J" cell_refs="R20-pt-1" judgment="true"/>
`R20PT-AC4J` (judgment, graded at L9, never by you): a completed meeting ticket that carries an outcome still shows it on its row; a completed ticket with none shows nothing; the coordinator's two actions render only for a viewer in `routing.primary`; every other viewer sees the outcome line without a control; no call, route, colour or principal was added.

<expected_criteria>R20PT-AC1 R20PT-AC2 R20PT-AC3 R20PT-AC4J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~50/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else. The meeting FORM, the labels, `analysisRequest.ts`, `AnalysisRequestParts.tsx`, the API client and every server call are not yours.

<paths>
portal/src/pages/TicketCenter/TicketCenter.tsx
portal/src/pages/TicketCenter/MeetingRequestParts.tsx
portal/src/pages/TicketCenter/__tests__/
org/missions/D7/TCKT/TCKT_VNEXT/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D7/TCKT/TCKT_VNEXT/decompositions/TCKT_VNEXT_DECOMP_R20.md</decomp_doc>
<owned_cells>R20-pt-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/0.9.0_WK_TCKT_VNEXT~50/TCKT_VNEXT.TO-R20-PT.meeting-outcome-line-in-every-status-and-controls-for-the-coordinator-only.proof_of_spec.json`.
Its `to_id` is exactly `TCKT_VNEXT.TO-R20-PT`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming
`3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "R20PT-AC1,R20PT-AC2,R20PT-AC3,R20PT-AC4J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a portal source change in a worker worktree; nothing is pushed, deployed or called. comp-routes: DECLARED-NOT-APPLICABLE -- no route is added or changed.
comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE. comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-adversary: RUN -- by reading the CVO's ADJUDICATION_v8, the CTO's rulings 2 and 4 and the two files against this cell; the lens: the "waiting" words drawn on a completed ticket that carries no outcome, a control shown to a non-coordinator, a case-sensitive email compare, the controls still shown on a completed ticket, and a test that copies the logic instead of rendering the board's mount. BLIND to: the rendered page (the issuer's later live read renders it).
</preflight>

---

## RECORD FACE

- Cut on the CTO's rounds 18-19 analysis (enrichment items 1 and 2, the code half) in round 20; fan-out 2 of 2 chains, cap 4. Base: `R20PT-AC1` FAILS as expected (no test file), `R20PT-AC3` FAILS (no checker file), `R20PT-AC2` PASSES at the base (a bound check).
