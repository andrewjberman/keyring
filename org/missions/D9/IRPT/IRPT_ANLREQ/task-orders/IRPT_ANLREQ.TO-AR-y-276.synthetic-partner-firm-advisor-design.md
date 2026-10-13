# TO IRPT_ANLREQ.TO-AR-y-276.synthetic-partner-firm-advisor-design -- the synthetic partner-firm advisor that drives FWD-1: the design the never-widen pair rests on, predicted offline

<to_id>IRPT_ANLREQ.TO-AR-y-276</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~97</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>23</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL
**Decomp cell:** `AR-y-276` (`decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md`) | **outcome_ref:** FWD-1 (hop 2) | **depends_on:** none

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~97`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-97` (branch `wk-IRPT_ANLREQ-97`). Commit there with
  `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~97 <0.9.0_WK_IRPT_ANLREQ~97@opal.agent>" -F <msgfile> -- <paths>`.
- Write every message file with the Write tool. `surfaced_at` of any row = `date -u +%FT%TZ` at filing; a row id has the form
  `IRPT_ANLREQ-D2-W97-S<k>` (take the next free `<k>`). The worktree shows ` M portal` (and may show a modified `.parquet`
  fixture): never commit either to the WORKSPACE repository (a portal commit is made inside the portal repository, as the step says). Every `.py` you add or change passes `bash .tools/commit-gate.sh <file>` before its commit.
- The proof instance: artifact rows use a `kind` the schema admits; a judgment row needs `method`, `invocation` and `denominator`;
  every non-PASS row carries a `status_reason`; a `controls.mutant` MUST be a mutant that FIRES (a mutant that leaves your criterion passing makes the instance INVALID).
  No live call (a `git fetch` of the portal's remote-tracking refs is permitted), no push, no deploy, no upload, no apply, no invoke. No non-ASCII in what you add. If a scratch copy is needed, put it OUTSIDE the product tree and leave it (you may not delete recursively; say where it is).

### THE CELL (`AR-y-276`, inlined) -- THE DRIVEN ARM'S DESIGN. READ AND OFFLINE RUN ONLY. NOTHING IS MINTED, CALLED OR SIGNED IN.

*FWD-1 (PRD v0.5, ADMITTED @68115f2d84; CTO GO msg 7191): one Analysis Request goes from the Ticket Center form to FOUR attachments on the same OPEN ticket with no person in between: (1) the advisor's original upload, (2) the form as filled, (3) the Opal-generated report (the Opal producer, not YCharts), (4) the AI commentary draft. The driven arm is a SYNTHETIC partner-firm advisor under a never-widen pair. Binding constraints: C-FIRM (the firm is the signed-in user's, never a choice outside its domain; the staff picker stays out of the advisor path), the variant the advisor selects is the variant produced, Opal staff do not file in the Ticket Center, FWD-4 (a failed hop shows on the ticket). PRD: `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md` (ENDPOINT, C-PACKAGER, C-FIRM, C-ABSORB); the direction: `org/tier1_exec/1.0.0_SA_CTO/deliverables/PIVOT_DIRECTION_20261013/DIRECTION_DELL2_20261013.md` section 2 O1. Call 2 (Andrew ~17:4xZ, APPROVED): 'an agent files the end-to-end test as a synthetic partner-firm advisor, minted and deleted'. `2e30` (the Opal-staff filing) is superseded. Precedents: the TCKT_VNEXT R2-cw-1 crawl identity (`org/missions/D7/TCKT/TCKT_VNEXT/deliverables/2.0.0_SA_COO~V2/R2_RUN/R2_CW1_CRAWL_PAIR.md` and its CTO half) and this project's round-21 status-rule exercise (`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/release21/NEVER_WIDEN_PAIR_ANLREQ_STATUS_RULE_DRIVEN_EXERCISE.md`, run by `0.7.0_AE_CloudOps~AQ2`, record `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r21/EXERCISE_RESULT.txt`). In that exercise refusals travel as HTTP 200 envelopes and a users row must carry `email`.*

1. **Read first:** the two precedents above, the exercise's trace and scripts under `org/tier2_senior/0.7.0_AE_CloudOps~AQ2/deliverables/irpt_anlreq_r21/`, `infra/aws/lambda/ticket_center/lambda_function.py` (principal classes, SUBMIT-FORM), the authorizer's token contract as the repo holds it (the claims a partner-firm human carries: `firmId`, `allowedFirmIds`, `userType`, `tier`; search `infra/aws/lambda/` for the authorizer by name: `comp-find` over a named folder), and the PRD's eligible-advisor rule (E5: `org/missions/D9/IRPT/IRPT_ANLREQ/prd/IRPT_ANLREQ_PRD.md`). Record `read`.
2. **The identity.** Specify the synthetic partner-firm advisor: the users row (`PK USER#<synthetic>@opal.invalid`, `SK PROFILE`, `email`, `firmId` = the partner firm 49financial, `status active`, `userType`, `allowedFirmIds` naming that firm only, whatever the eligibility rule E5 requires of an advisor), the token claims (`sub`, `iss`, `aud`, `firmId`, `tier`, `role`, `userType`, `exp` at most 20 minutes after `iat`), and the sign-in method (a minted token held in memory, as in the precedents; say whether the Ticket Center page can be driven by a token alone or needs a browser session: READ it; the precedents used a bare HTTP drive, FWD-1 needs the FORM to be exercised, so say how the form's submit is driven: the portal's own request builder run headless, or the routes the form calls, in order).
3. **The drive and the reads.** The ordered list of calls the form makes from Submit to the finished package (upload, create ticket, POST analysis, record the id, READY, drafter, commentary-draft, package) with, for each: the route, the principal that signs it, the expected outcome and the artifact that proves it; the end-state reads an Opal person's equivalent would make (one ticket read: `report_ref` set, four package pointers, the commentary DRAFT; each of the four opened by an internal human); and the log reads (the Opal producer, not YCharts, served the request). Codes and names only in any record; no client figure.
4. **Predict offline.** Run what can be run without a token, a key or an AWS call: the form's request builder (`fileAndRequestAnalysis`) against fakes with the synthetic principal's claims, to list the exact requests it would send for one Comparison request with two Opal models and a small synthetic holdings CSV (a constructed file with synthetic tickers only; put it OUTSIDE the repository tree and describe it by shape). Record `offline_run` (the request sequence as method, route, body member NAMES, no values) and say what it cannot predict.
5. **Removal and bounds.** `removal` (delete the users row after `exp`, GSI and ConsistentRead ABSENT; the ticket the drive creates is a real ticket: say whether it is deleted or closed, by whom and how, and what stays as evidence), `bounds` (what the identity may do: one filing; what it may not: any other firm, any other route, a second token, any client data), `blast_radius` (keys and items touched, rollback per key), `executor` (a Dell CloudOps lane: AQ2), `grants_needed`.
6. **Write `r23/SYNTHETIC_ADVISOR_DESIGN.json`:** `read`, `identity`, `drive`, `offline_run`, `removal`, `bounds`, `blast_radius`, `claim`, `not_read` (the live edge, the live tables, the live authorizer config).
7. **In your report:** the identity in one line, the drive's call sequence, what the offline run showed, what only the live drive can show.

### ACCEPTANCE

<criterion id="AR276-y-AC1" cell_refs="AR-y-276"><invocation>python C:/dev/wk-irpt-anlreq-97/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r21/ar21_checks.py y276-design --root C:/dev/wk-irpt-anlreq-97</invocation><expect>Y276-DESIGN-OK</expect></criterion>
`AR276-y-AC1`: the record specifies the identity (row and token claims), the ordered drive from Submit to the package with the principal and proof per call, an offline run of the request sequence, the removal and the bounds with blast radius and executor.

<criterion id="AR276-y-AC2J" cell_refs="AR-y-276" judgment="true"/>
`AR276-y-AC2J` (judgment, graded at L9, never by you): the identity's claims were read from the authorizer contract and the precedents (not recalled), the drive exercises the FORM's own request sequence, the end-state reads are the four attachments, the removal covers the row and the ticket it creates, and nothing was minted, called or signed in.

<expected_criteria>AR276-y-AC1 AR276-y-AC2J</expected_criteria>

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~97/` and this order's file (status flip only). If a test OUTSIDE the grant fails because of your change, STOP: file a BLOCKING row naming it; the issuer amends the grant.
- READ only: everything else.

<paths>
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R23_Y.md</decomp_doc>
<owned_cells>AR-y-276</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: see ACCEPTANCE. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~97/IRPT_ANLREQ.TO-AR-y-276.synthetic-partner-firm-advisor-design.proof_of_spec.json`.
Its `to_id` is exactly `IRPT_ANLREQ.TO-AR-y-276`. The judgment criterion is recorded under `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` (never PASS or FAIL). Validate it AFTER its commit with
`python .tools/proof-of-spec-check.py <instance> "AR276-y-AC1,AR276-y-AC2J"`; flip `<status>` to `complete` only when it prints VALID.
</proof_of_spec>

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reads and offline runs in a worktree; nothing is minted, called or applied; nothing is landed, pushed, deployed or called.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is called or changed. comp-cache: DECLARED-NOT-APPLICABLE. comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- this order makes no AWS call and changes no policy.
comp-adversary: RUN -- by reading PRD v0.5 FWD-1 and the pivot direction O1 against the cell; the lens: a hop that is read from a route table and not from the code that runs it, a widened authorization, a fix for a hop that already works, a failure that is silent. The order requires the hop to be READ before it is changed, a stop-and-row where the cause is in another lane, and every failure visible on the ticket (FWD-4). NOT seen: the live PROD and DEV bundles; Andrew's screenshots (they are in his chat).
lane: the files named in <paths> and the worker's deliverables.
</preflight>

---

## RECORD FACE

- Cut on the CTO's GO (msg 7191): PRD v0.5 ADMITTED, the FWD-1 hop cells in ONE issuance (ADDENDUM v0.5 item 4), workstream `Y` round 23. Each grant names every file the cell writes. Base: `AR276-y-AC1` FAIL as expected (no record).
- Any portal candidate goes to `1.0.0_SA_CTO`'s review lane through the issuer; the worker lands nothing.
