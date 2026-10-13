# TO IRPT_ANLREQ.TO-AR-y-244.proxy-suggestion-read -- where a proxy suggestion could come from -- a read, nothing built

<to_id>IRPT_ANLREQ.TO-AR-y-244</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~76</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>18</round>
<workstream>YR</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-244` (`decompositions/IRPT_ANLREQ_DECOMP_R22P_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~76`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-76` (branch `wk-IRPT_ANLREQ-76`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~76 <0.9.0_WK_IRPT_ANLREQ~76@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W76-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-244`, inlined) -- THE PROXY BOX: WHAT THE SERVER SUGGESTS TODAY, AND WHAT IT COULD. READ ONLY. NOTHING IS BUILT OR CHANGED.

*Andrew's own test (rows D2-S77, D2-S78): the ticker `TIMXX` (row 100, a money-market-class symbol) was not recognized by the data provider, and the proxy box said only "Ticker" -- what to type was unclear and no "Did you mean" appeared. He expected the page to find a similar security from the Opal database. The page shows a suggestion button only when the server sends one (`ProspectComposer.tsx` :484-493); the server's "provider-verified match for a likely typo" (Y-4) is the only source today. A prior live walk resolved TIMXX as SGOV (`IRPT_YCDGEN.TO-YCD-h-5` line 50).*

1. **Where the suggestion comes from.** Find the code that writes `suggestion` into a finding (the portal's reader is `ProspectComposer.tsx` :483-493 and the finding types; the writer is in `infra/aws/lambda/investor-reporting/`, probably `intake/` and the resolve path: `comp-find` over named folders, or `Grep` on a named folder; do not search the repo blind). Record `where_suggestion_comes_from` {`file_lines`, `rule_in_words`, `what_it_calls`, `when_none_is_sent`}.
2. **Why TIMXX got none.** From that code and its tests, say what input makes the rule send a suggestion and why a money-market ticker the provider does not know sends none (`why_timxx_got_none`: read from the code and a constructed case you run offline in the existing tests' harness if it is cheap; a case you did not run is labelled READ, not RUN).
3. **The sources a similar security could come from.** List at least two (`options`: each with `source`, `how_it_would_be_asked`, `what_it_returns`, `cost` in work and in risk, `already_in_the_estate` yes or no with the file or tool that proves it). Look first at what the estate already has: the YCharts search the gateway exposes (`ycharts_search`), the security master or asset dimension the IRPT resolve path reads, the earlier SGOV resolution in `IRPT_YCDGEN.TO-YCD-h-5` (line 50) and how it was reached, and the analysis form's own ticker resolution. Say which is a call the portal could not make from the browser (a secret or a server-only path) and which the server would have to make. Do NOT recommend building a new index or search service (the build ladder: the estate first); recommend one option or say none fits, with the reason.
4. **The wording.** `proxy_wording`: what the proxy row should say so a person knows what to type (two sentences at most), as a proposal for the CTO; do not change the page.
5. **Write `r22/PROXY_SUGGESTION_READ.json`:** `where_suggestion_comes_from`, `why_timxx_got_none`, `options`, `recommendation`, `proxy_wording`, `claim`, `not_read`.
6. **In your report:** the rule in one sentence, why TIMXX got none, the options in one line each, and your recommendation.

### ACCEPTANCE

<criterion id="AR244-y-AC1" cell_refs="AR-y-244"><invocation>python C:/dev/wk-irpt-anlreq-76/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y244-read --root C:/dev/wk-irpt-anlreq-76</invocation><expect>Y244-READ-OK</expect></criterion>
`AR244-y-AC1`: the record says where the suggestion is written and why TIMXX got none, and lists at least two sources of a similar security, each with its source and cost.

<criterion id="AR244-y-AC2J" cell_refs="AR-y-244" judgment="true"/>
`AR244-y-AC2J` (judgment, graded at L9, never by you): the writer of the suggestion was read in the code (not guessed), each option names what the estate already has, no new service is recommended where the estate has one, and nothing was built or changed.

<expected_criteria>AR244-y-AC1 AR244-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~76/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R22P_Y.md</decomp_doc>
<owned_cells>AR-y-244</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~76/IRPT_ANLREQ.TO-AR-y-244.proxy-suggestion-read.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-244`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR244-y-AC1,AR244-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reads of source files and tests in the worktree; a constructed offline case at most; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading Andrew's own-test report (rows D2-S77, D2-S78) against the cell; the lens: a test that passes without the change, or a change that fixes the page the worker imagined and not the one Andrew saw. The order requires the new test to FAIL on the DEV tip without the change, and the words a person sees to be stated as rendered. NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on Andrew's own upload test (rows `D2-S77`, `D2-S78`, msg 7105) as workstream `YR` round 18. Base: `AR244-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
