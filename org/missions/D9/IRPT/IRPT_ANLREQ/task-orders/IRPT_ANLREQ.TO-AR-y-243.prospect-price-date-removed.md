# TO IRPT_ANLREQ.TO-AR-y-243.prospect-price-date-removed -- the prospect page drops the price date field, after the serving path is read

<to_id>IRPT_ANLREQ.TO-AR-y-243</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~75</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-243` (`decompositions/IRPT_ANLREQ_DECOMP_R22P_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~75`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-75` (branch `wk-IRPT_ANLREQ-75`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~75 <0.9.0_WK_IRPT_ANLREQ~75@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W75-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-243`, inlined) -- THE PRICE DATE FIELD GOES. A CANDIDATE on a portal branch; nothing is landed, pushed or deployed.

*Andrew's own test (row D2-S78), verbatim: "there is no point in picking a 'price data for share quantities' as the answer is always 'now', which will translate into market close of the prior trading day." The field is `ProspectComposer.tsx` :434-437 (a date input, default empty); its value is sent in the upload request (:281, `priceDate`) and recorded as `asOf` on the reviewed prospect (:210). Whether the serving path reads the date, ignores it, or REQUIRES it for share quantities is not read yet.*

1. **The branch.** The portal repository is `C:/dev/ajb_workspace/portal` (a separate git repository). `git -C C:/dev/ajb_workspace/portal fetch origin DEV` is permitted. Record `dev_tip` (full sha of `origin/DEV`). Make a worktree OUTSIDE the product tree: `git -C C:/dev/ajb_workspace/portal worktree add C:/dev/wk-portal-75 -b wk-IRPT_ANLREQ-75-portal origin/DEV`. Never check out, reset or commit anything else in the portal checkout, and never push. Commit the way an earlier candidate branch was made (`git -C ... log` of `wk-IRPT_ANLREQ-63-portal`); if a hook or a rule of the portal repository refuses your commit, STOP and file a row with the refusal text. Read the portal's own `CLAUDE.md` and `DESIGN.md` first: new text follows their clauses (navy ink on white panels, no light-on-light; cite the clause number in your record for each visual choice).
2. **Read the serving path FIRST (before you change the page).** Follow `priceDate` from the composer's request (:281, then the portal API client and its types) to the IRPT upload entry and the code that prices share quantities (`infra/aws/lambda/investor-reporting/intake/` and what it calls; `comp-find` and `Grep` over named folders, or the named files). State, with file and line for each: what the server does with a price date when it is sent; what it does when NO date is sent and a Shares column is present; whether a trading-day rule (the prior trading day's close, `lib/trading_calendar.py`) is applied server-side. Record this as `server_reads` {`what_the_server_does_with_a_date`, `what_the_server_does_without_a_price_date`, `trading_day_rule_where`, `files_read`}. **If the server REQUIRES a date for share quantities, or cannot price without one, STOP before step 3, file a BLOCKING row naming the file and line, and write the record with `candidate` absent: the issuer cuts a server cell. Do NOT compute a trading day in the portal.**
3. **The change (only if step 2 shows the server prices without a date).** Remove the Price date label and input; stop sending `priceDate` (omit the member, do not send an empty string); the reviewed prospect's `asOf` is `null` as it is today for an empty field. Remove `priceDate` state that nothing reads any more. Keep the reference notional field and everything else. Touch `src/` only and change no wire reader or contract file other than the request builder's own optional member.
4. **The test, before and after.** Tests in the portal's existing folder for this component that assert (a) the face carries no "Price date" text and no date input, (b) the upload request body carries no `priceDate` member, (c) a Shares-column file still reaches the upload call and its answer is shown as before, (d) the reference notional field is still there. `before_arm`: run on `origin/DEV` WITHOUT the change: (a) and (b) FAIL. `tests`: with the change all pass; the whole component folder (counts; known `dsgn-irptv1` failures stated with counts both ways). `bun`, `bun run typecheck`.
5. **Commit** in the portal worktree; record the full sha.
6. **Write `r22/PORTAL_PRICE_DATE_CANDIDATE.json`:** `server_reads`, `dev_tip`, `branch`, `commit`, `files_changed`, `tests` {`added`, `passed`, `failed`, `folders`}, `before_arm` {`failed`, `output_tail`}, `what_a_person_sees`, `design_clauses`, `claim`, `not_read`.
7. **In your report:** what the server does without a date (file:line), the branch, the commit, the counts.

### ACCEPTANCE

<criterion id="AR243-y-AC1" cell_refs="AR-y-243"><invocation>python C:/dev/wk-irpt-anlreq-75/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y243-portal --root C:/dev/wk-irpt-anlreq-75</invocation><expect>Y243-PORTAL-OK</expect></criterion>
`AR243-y-AC1`: the record states what the serving path does when no price date is sent, names a portal commit under `src/` only with added tests that fail on the DEV tip without the change and pass with it, and no failing test beyond the known pre-existing ones.

<criterion id="AR243-y-AC2J" cell_refs="AR-y-243" judgment="true"/>
`AR243-y-AC2J` (judgment, graded at L9, never by you): the serving path was READ (not assumed) and the field was removed only because it prices without one, the request carries no price date, no trading day is computed in the portal, and nothing was landed or pushed.

<expected_criteria>AR243-y-AC1 AR243-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~75/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22P_Y.md</decomp_doc>
<owned_cells>AR-y-243</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~75/IRPT_ANLREQ.TO-AR-y-243.prospect-price-date-removed.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-243`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR243-y-AC1,AR243-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- a branch and a worktree in the portal repository outside the product tree; read-only reads of the serving path's source; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading Andrew's own-test report (rows D2-S77, D2-S78) against the cell; the lens: a test that passes without the change, or a change that fixes the page the worker imagined and not the one Andrew saw. The order requires the new test to FAIL on the DEV tip without the change, and the words a person sees to be stated as rendered. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on Andrew's own upload test (rows `D2-S77`, `D2-S78`, msg 7105) as workstream `YR` round 18. Base: `AR243-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.

<!-- ISSUER NOTE 2026-10-13 (2.0.0_SA_COO~Y2): status flipped to complete because the worker ran the order to its stop and its proof instance reads VALID: step 2 read the serving path and the server REQUIRES a price date for share quantities (intake/portfolio.py :208-212; row IRPT_ANLREQ-D2-W75-S1), so step 3 was not run and AR243-y-AC1 stays FAIL (no portal candidate). The cell is re-cut after AR-y-245 (the server defaults the date); the portal field is removed only after that server leg is released. -->
