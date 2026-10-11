# TO DSGN_IRPTV1.TO-IV-e-106 -- ONE PROD candidate record, written now and pushed by nobody: the exact commit, every page it changes with its class, the two missing status reads stated, and retained_ref carried by the sections reader

<to_id>DSGN_IRPTV1.TO-IV-e-106</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~59</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2's ROUND-23 ANALYSIS `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_DSGN_IRPTV1_ROUND_23_20261011.md` @b417e9ee3c, section 4 item 1, answering `org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/remediations/REMEDIATION_v9.md` @d0092958d1 | **Rows:** DSGN_IRPTV1-D2-W56-S3, DSGN_IRPTV1-D2-W56-S2 | **Decomp cell:** `IV-e-106` (decomposition v23) | **outcome_ref:** FWD-1 (the history reader on PROD; IRPT_ANLREQ release 5's return follows it) | **depends_on:** none; FIRST on slot A (thread-breaking: it is what Andrew's word would approve).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-dsgn-irptv1-49` (the slot's worktree; branch `wk-dsgn-irptv1-r14-49`); run everything from its root
unless a step says the portal. Your folder is `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~59/`.

**Two repos.** `C:/dev/wk-dsgn-irptv1-49/portal` is a PORTAL worktree (its own git repo) at the commit your spawn prompt names. Do not amend or
revert anything committed there. Portal files commit in the portal repo with plain git and your author line; records, rows and this order's
status commit in the workspace repo with `.tools/safe-commit.sh`. Never push either repo; never commit the workspace `portal` gitlink.
`node_modules` is a real local install that another worktree junctions to: no `bun install`, no package change, never delete it. Resolve bun
with `command -v bun`. COMMIT FIRST, then run, then make any temporary mutant, and revert a mutant only with `git checkout -- <file>` on a
file that has no uncommitted work of yours. One whole-scope run before any edit (`bun test src/pages/InvestorReporting`, output to a file
under `C:/dev/_irpt_private_evidence_20261009/DSGN_IRPTV1/0.9.0_WK_DSGN_IRPTV1~59/`) is your base for `new_failing_ids`.

**What this is for.** Portal PROD is at `37aa1247ee`. Portal DEV carries this project's changes of rounds 17 to 22, among them the
transitional history reader that IRPT_ANLREQ's release 5 needs on PROD before it can return. A PROD push that changes a client-facing page
waits on Andrew's word. The CTO: what this project owes before that word is "the thing he would be approving: one PROD candidate record,
written now and pushed by nobody." You push NOTHING, to DEV or PROD.

**The cell (`IV-e-106`).** Two parts, in this order.
1. **`retained_ref` carried (row D2-W56-S3; a product change).** On the v1 plane the sections reader drops `retained_ref`:
   `adaptAnalysisReportSlice` (`src/pages/InvestorReporting/contracts/adapt.ts`, near lines 1427-1447) reads named members and returns a
   view with no such member. Read the row and the contract first (the response schema
   `infra/aws/lambda/investor-reporting/_contracts/responses/analysis-report.response.schema.json` in the workspace, and the generated
   `contracts/wire/responses.ts`): carry `retained_ref` onto the view as an optional member, as supplied, when the answer has it; absent
   stays absent; nothing else about the view changes and no page prints it in this cell. A test under `__tests__/dsgn-irptv1/` holds it
   (an answer with the member -> the view carries it; without -> absent), with one temporary mutant. `retained_ref` {carried, where
   {file, line}, test {id, passes, mutant {what, failed}}}. Commit it.
2. **The candidate record**, `PROD_CANDIDATE.json` and a one-page `PROD_CANDIDATE.md` beside it in your folder, for the commit you just
   made (`candidate_commit`: your portal HEAD, 40 hex; `prod_commit`: `37aa1247ee...` in full; `pushed: false`):
   - `files_changed`: the count of `git diff --name-only 37aa1247ee <candidate>` (print the denominator).
   - `pages`: EVERY changed file is assigned to exactly one page (hunt the unassigned file by subtraction from that list; shared code
     imported by ONE page is assigned to that page; shared code imported by more than one page gets its own entry, named for the
     module, whose class is CLIENT_FACING if any importing page is). Each entry {page, class, files, how_class_was_decided}. `class` is `CLIENT_FACING` (a partner-firm or
     client login can open it) or `OPAL_INTERNAL` (staff only): decide it from the route's guard in the router and the role checks, by
     file and line, never from the page's name; unsure is `CLIENT_FACING`. The files sum to `files_changed`.
   - `status_reads`: for `analysis-request-pdf` and `analysis-request-original` (PROD lacks both, row D2-W56-S2): {state: CARRIED or
     NOT_CARRIED, where (file and line of the client method and its route-table row at the candidate)}.
   - `other_lanes`: commits in that range authored by other projects' seats (count, and their subjects): Andrew's word covers the whole
     range, not this project's part.
   - `unexercised`: what in this range has been read on synthetic data only (take it from the rows the analysis names: D2-S16, D2-W58-S4,
     D2-W57-S3; add any you find).
   The `.md` states the same in plain sentences a principal can read in two minutes: what changes on which page, what was and was not
   exercised, what release follows it.
3. `lint_errors`, `typecheck_errors`, one whole-scope run after (`suite_after` {pass, fail, new_failing_ids}).

<criterion id="IV106-AC1" cell_refs="IV-e-106"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r23/p23_round23.py" . IV106-AC1</invocation><expect>IV106-AC1 PASS</expect></criterion>
`IV106-AC1` -- the candidate commit is named with every changed file assigned to a page and its class, the two status reads stated, and retained_ref carried with a tested fix. Base: FAIL.

<expected_criteria>IV106-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. The contract and the producer's fixtures (workspace files)
  are read, never edited. No file under `contracts/wire/` is hand-edited (generated; one command regenerates it:
  `bun run src/pages/InvestorReporting/__tests__/fe-s-13/gen-all.ts`).
- **No deploy and no push.** No portal push, no DEV or PROD act, no AWS call, no live request, no vendor call, no secret read, no
  `bun install`, no package change, no dev server on any port.
- **Every portal commit is followed by `bun run lint` and `bun run typecheck`**; a lint ERROR is fixed before you report (the count goes in
  the record as `lint_errors`, and typecheck's as `typecheck_errors`).
- **Synthetic data only** in any fixture, screenshot or record: no real client name, account number or figure.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this
  order did not name. Never weaken an assertion this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W59-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~59/
portal/src/pages/InvestorReporting/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-106.prod-candidate-record-with-retained-ref.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v23 (round 23), cell `IV-e-106`.
<owned_cells>IV-e-106</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV106-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~59/DSGN_IRPTV1.TO-IV-e-106.prod-candidate-record-with-retained-ref.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV106-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the candidate commit; files changed and the page table (page, class, files, how decided); the two status reads; the retained_ref line, its test and mutant; other lanes' commits in the range; what is unexercised; lint, typecheck and suite; and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; one optional member carried by one reader, with a test; the record itself changes nothing. The candidate is read by the CTO before DEV, and PROD waits on Andrew's word.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; every criterion FAILS at base (no record).
lane: the <paths> block IS the grant.
</preflight>
