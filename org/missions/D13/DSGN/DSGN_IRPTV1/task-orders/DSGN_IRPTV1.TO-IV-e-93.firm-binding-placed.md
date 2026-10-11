# TO DSGN_IRPTV1.TO-IV-e-93 -- the FWD-1 walk's FIRM_BINDING refusal placed at the line that emits it: does the reporting read refuse because the firm selector sat at Global (All), and what does an Opal user who never touches that selector see -- read-only; no fix is cut before this read

<to_id>DSGN_IRPTV1.TO-IV-e-93</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~51</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>15</round>

**Directive:** D13 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 4407 (one read-only cell, before any fix) and msg 4427 (the two facts in the walk record), on row `DSGN_IRPTV1-D2-S7` | **Decomp cell:** `IV-e-93` (decomposition v15) | **outcome_ref:** FWD-1 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-dsgn-irptv1-51`; run everything from its root. Your folder is
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~51/`. Portal code is read at the walked commit by content:
`git -C C:/dev/ajb_workspace/portal show ab697ba120a6452bdcb634038d8114b88f18e4a9:<path>` and
`git -C C:/dev/ajb_workspace/portal grep -n <pattern> ab697ba120a6452bdcb634038d8114b88f18e4a9 -- <dir>`.

**The cell (`IV-e-93`).** The laptop's `/ui-walk` walked FWD-1 on portal DEV @ab697ba1, signed in for real. The record is in your tree:
`org/tier1_exec/4.0.0_SA_CRO/deliverables/UI_WALK_DSGN_IRPTV1_FWD1_20261011T0730Z.md`. Read it in full first. It broke at Performance on two
refusals. One is already placed and ruled: `OBJECT_NOT_COVERED` is the vendor per-use gate at
`infra/aws/lambda/investor-reporting/performance/authorization.py:90` (2.0.0_SA_COO~P2 msg 4414; the CTO retired that gate in msg 4417; it is
P2's cell). **Yours is the other: the reporting summary and manifest answered UNAVAILABLE with `FIRM_BINDING`.**

Two facts from the record the CTO asks you to settle (msg 4427):
1. **The walk left the firm selector at its default, `Global (All)`.** State whether the two reporting reads refuse BECAUSE no single firm is
   selected, and what an Opal user who never touches that selector sees. If the page offers a client of one firm while sending a request bound to
   none, that is the page's defect, not the service's.
2. **Hop 7 read PARTIAL:** the default Holdings face splits by ACCOUNT, and the Models / SMAs / Client split is one layer in. FWD-1's words name
   the category split. You change nothing: you put the PRD's sentence beside the walk's line for the reviewer.

In `FIRM_BINDING_PLACED.json`:
- `routes`: the summary and manifest route templates, and the Lambda source folder that serves them.
- `emitted_at` {file, line}: the line in the workspace repo at HEAD that produces `FIRM_BINDING` for those routes. Search the literal with
  `comp-find` over `infra/aws/lambda`; print the denominator and every hit; if several sites emit it, say which one these routes reach and why.
- `condition`: the test at that site, in plain words, with what it compares.
- `page_sends` {what, source: {file, line}}: what firm binding the PAGE puts on those two requests when the selector reads `Global (All)` and a
  client of one firm is picked (a `selected_tenant` parameter, a header, nothing), read from the portal at the walked commit; and what it sends on
  the reads that PASSED in the same walk (holdings, the directory), so the difference is visible.
- `reached_because`: the trace from the request the page sent to the refusing line, each step with file and line.
- `because_no_single_firm_selected`: `YES`, `NO` or `NOT_ESTABLISHED`, with `basis` [{file, line}].
- `whose`: `SERVICE` (the service should resolve the firm from the picked client and does not), `PAGE` (the page should bind the request to the
  picked client's firm and does not), `BOTH`, or `NOT_ESTABLISHED`. Say which contract or PRD line decides it; the PRD's ROUTE STRUCTURE section
  (`org/missions/D13/DSGN/DSGN_IRPTV1/prd/DSGN_IRPTV1_PRD.md`, about line 305) and the wire contract are where to look. You decide nothing that
  the text does not decide: if no line decides it, it is `NOT_ESTABLISHED` and the CTO rules.
- `opal_user_default_sees`: what an Opal user who never touches the selector sees on the Performance tab for a one-firm client, from the code.
- `also_live_state`: anything in the refusal that depends on live state (a published file, a table row) rather than on the request: named as
  INFERRED, with the one read that would measure it. You make no AWS call.
- `hop7` {prd_sentence, walk_line}: FWD-1's sentence from the PRD (lines 44-46; the client's name may be quoted as the PRD writes it) beside the
  walk record's hop-7 line, verbatim, with nothing added.
Then a one-page `FIRM_BINDING_PLACED.md`.

<criterion id="IV93-AC1" cell_refs="IV-e-93"><invocation>python "org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D2/checks/r15/p15_round15.py" . IV93-AC1</invocation><expect>IV93-AC1 PASS</expect></criterion>
`IV93-AC1` -- the FIRM_BINDING refusal is placed at a line at HEAD that contains it, with what the page sent, whether the missing firm selection is the cause, whose defect it is, and hop 7's two sentences side by side. Base: FAIL.

<expected_criteria>IV93-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Read-only.** No AWS call, no request to a deployed service, no token, no portal edit, no push, no package install, no dev server.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or widened. An edit outside the
  grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `DSGN_IRPTV1-D2-W51-S<k>`, with the real current UTC time; append as BYTES, never
  re-encode the existing content.

<paths>
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~51/
org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~51/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D13/DSGN/DSGN_IRPTV1/task-orders/DSGN_IRPTV1.TO-IV-e-93.firm-binding-placed.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v15 (round 15), cell `IV-e-93`.
<owned_cells>IV-e-93</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IV93-AC1. The instance goes at
`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~51/DSGN_IRPTV1.TO-IV-e-93.firm-binding-placed.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> IV93-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: commit hashes, the criterion's last line, the emitting line and its condition, what the page sent on the refused reads and on the reads that passed, the answer on the firm selector with its basis, whose defect it is and the line that decides that, what an Opal user sees by default, hop 7's two sentences, and any row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only placement of one refusal site; no product, contract or infra edit.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call.
comp-routes: RUN -- the two reporting routes are named with the Lambda that serves each; no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: RUN -- IV93-AC1 FAIL at base (no record). CTO msgs 4407 and 4427.
lane: the <paths> block IS the grant.
</preflight>
