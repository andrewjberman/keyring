# TO IRPT_ANLREQ.TO-AR-y-35 -- the Analysis Request form's firm answer is a choice from the firms the caller's profile allows

<to_id>IRPT_ANLREQ.TO-AR-y-35</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~51</issued_to>
<issued_by>2.0.0_SA_COO~Y2</issued_by>
<issued_date>2026-10-11</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>Y</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Risk:** LOCAL (a portal product file; the candidate goes to the CTO before DEV, by the issuer) |
**Decomp cell:** `AR-y-35` (`decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md`) | **outcome_ref:** FWD-1 | **depends_on:** `AR-y-31` (same file)

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~51`. This is the SECOND order of your queue; start it only after `IRPT_ANLREQ.TO-AR-y-31` is committed, in
the same two worktrees (workspace `C:/dev/wk-irpt-anlreq-51`, portal `C:/dev/wk-irpt-anlreq-51/portal`), with the same commit commands.
Never run `bun install`. Run a test file as `bun test ./src/...`.

### THE CELL (`AR-y-35`, inlined)

*The Analysis Request form's firm answer is a choice from the firms the caller's profile allows; no free text.*

**What is wrong today** (portal `src/pages/TicketCenter/AnalysisRequestParts.tsx`): `AnalysisRequestFields` (:57) renders
`<input aria-label="Firm" ... placeholder="Firm id (required)">` (:74). The typed value becomes `answers.firm` (`answersFromForm`, :41-55)
and is sent to the upload door as the selected tenant. The door clamps the tenant by the token, so a wrong firm is refused, not leaked;
the defect is that a person can type something the system must then refuse.

**Build:**
1. `AnalysisRequestFields` takes a new prop `firms: readonly { id: string; label: string }[] | null` -- the firms the caller's own profile
   allows. `null` means "not loaded yet".
2. The Firm control is a `<select aria-label="Firm">` whose options are exactly `firms`. With `firms === null` it is disabled and reads
   "Loading firms...". With exactly one firm, that firm is chosen and the control is disabled. There is no text input for the firm.
3. `answersFromForm` is unchanged in shape. A `form.firm` that is not one of `firms` cannot be submitted: the existing submit guard
   (`canRequestReport` or the form's own required check; read which one gates the button) treats it as missing.
4. **Where the list comes from.** FIND where the portal already holds the firms the signed-in caller may act for, as its profile serves
   them (the header's tenant or firm selector and Investor Reporting's selected-tenant handling are the places to read first). Pass that
   list in from the component that mounts `AnalysisRequestFields`; that mounting file is in your `<paths>` only if it is
   `AnalysisRequestParts.tsx` itself. **If the mount is in another file, or the portal holds no served list of allowed firms, STOP:**
   file ONE BLOCKING row naming the files you read and what each holds, and do not invent an endpoint, a constant list or a new fetch.
5. New test file `src/pages/TicketCenter/__tests__/analysis-firm-choice.test.tsx` with EXACTLY these test names:
   - `the firm answer is a choice from the firms the profile allows`
   - `a caller with one allowed firm has it chosen and cannot type another`
   - `a firm outside the allowed list cannot be submitted`
6. `analysis-request.test.tsx` and `analysis-form-i1.test.tsx` render the form. Where they type into the Firm input, change ONLY that
   step to choose the option, and say so. They are in `<paths>` for that purpose alone.

Use the existing field classes (`FIELD`); add no colours.

---

**AMENDMENT 1 (issuer `2.0.0_SA_COO~Y2`, 2026-10-11 ~07:5xZ): the ruling on row `IRPT_ANLREQ-D2-W51-S1`. Step 4 is REPLACED; the grant gains
ONE file.** Your stop was right: the form's only mount is `src/pages/TicketCenter/TicketCenter.tsx:406`, outside the grant, and the page
holds no served list. Gate limb that graded this amendment: read from this commit's own output.

- **Where the list comes from (ruled):** the served directory context. The ticket page already builds an Investor Reporting client
  (`TicketCenter.tsx:148`, `const ir = useMemo(() => createInvestorReportingApi() ...)`). That client's EXISTING method
  `resolveDirectoryContext` (`src/api/endpoints/investor-reporting.ts:1238`) returns a `ResolvedScope` whose `permittedFirms`
  (`src/pages/InvestorReporting/contracts/adapt.ts:713-718`) is the list of firms the caller's own profile allows, as the server gives
  them. This is one existing call on an existing served route: no new endpoint, no constant list, no new client.
- **Build, in `TicketCenter.tsx`:** when the Analysis Request form is shown (`newType === 'analysis_request'`), call
  `resolveDirectoryContext` ONCE (not per render, not per keystroke; a retry only on the user's own action). Map
  `permittedFirms` to `firms = [{ id: <the firm's tenant>, label: <its displayName> }]`, keeping only firms whose `selectable` is true,
  and pass `firms` to `AnalysisRequestFields`. While the call is in flight, pass `null`.
- **If the call fails:** `firms` stays `null`, the form states "The firms you can file for could not be loaded." in its existing alert
  line, and the request cannot be submitted. Never fall back to free text or to the caller's single claim firm.
- `catalogueFirm` (`TicketCenter.tsx:198`) keeps reading `analysisForm.firm`; it now only ever holds a chosen firm.
- If `IrpAnalysisClient` (the type the page casts its client to) does not declare `resolveDirectoryContext`, widen that type where the
  page declares it. If it is declared in a file outside the grant, file a row naming the file and stop on that point only.
- **Tests:** the three named tests of step 5 stand. Add a FOURTH to the same file, named exactly
  `the ticket page loads the allowed firms once through the directory context`: mount the page's form path with a stubbed client and
  assert ONE call and the options rendered. Add its name to your report; criterion `AR35-y-AC1` checks the three names it lists and
  that the file passes, so the fourth is graded by passing.
- Steps 1, 2, 3, 5 and 6 stand as written.

### ACCEPTANCE

<criterion id="AR35-y-AC1" cell_refs="AR-y-35"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y35-page --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y35-PAGE-OK</expect></criterion>
`AR35-y-AC1`: the three named tests exist and pass.

<criterion id="AR35-y-AC2" cell_refs="AR-y-35"><invocation>python C:/dev/wk-irpt-anlreq-51/org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~Y2/checks/r3/ar3_checks.py y31-keep --portal C:/dev/wk-irpt-anlreq-51/portal</invocation><expect>Y31-KEEP-OK</expect></criterion>
`AR35-y-AC2`: the package tests that must not move still pass after the form change (the same file holds both).

<expected_criteria>AR35-y-AC1 AR35-y-AC2</expected_criteria>

The issuer runs the portal typecheck, lint and the whole TicketCenter test folder at the drain, and looks at the rendered form.

## BOUNDS

- **Grant:** exactly the `<paths>` below, plus `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/` and this order's
  file (status flip only).
- READ only: everything else in the portal.
- LOCAL: never push, never deploy, never call a live API. Port 5174 only. No non-ASCII.

<paths>
portal/src/pages/TicketCenter/AnalysisRequestParts.tsx
portal/src/pages/TicketCenter/TicketCenter.tsx
portal/src/pages/TicketCenter/__tests__/analysis-firm-choice.test.tsx
portal/src/pages/TicketCenter/__tests__/analysis-request.test.tsx
portal/src/pages/TicketCenter/__tests__/analysis-form-i1.test.tsx
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R3_Y.md</decomp_doc> (round 3, workstream Y), cell `AR-y-35`.
<owned_cells>AR-y-35</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR35-y-AC1 AR35-y-AC2. The instance is at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~51/IRPT_ANLREQ.TO-AR-y-35.analysis-form-firm-choice.proof_of_spec.json`.
Validate it AFTER its commit with `python .tools/proof-of-spec-check.py <instance> AR35-y-AC1,AR35-y-AC2`.
</proof_of_spec>

**REPORT (once):** each check line verbatim; the portal commit; where the firm list comes from (file and line) and the hookup line the
mounting file needs if it is outside your paths; every existing test step you changed; any row ids.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger. comp-iam: DECLARED-NOT-APPLICABLE -- no IAM; the door's token clamp is unchanged. comp-adversary: RUN -- sources read at the cut: portal origin/DEV 1cd1cf252e AnalysisRequestParts.tsx :57-75 and :41-55; row IRPT_ANLREQ-D2-S17; BLIND: where the portal holds the caller's allowed firms was searched by five name patterns in src/api, src/hooks, src/contexts and two page folders and NOT found, so step 4 makes the worker find it or stop.
lane: a portal product file on the CTO review route; the candidate is sent by the issuer after the drain.
</preflight>

Source: CTO round-3 analysis @430d79e86d section 2 row D2-S17 and section 4 Y5; row IRPT_ANLREQ-D2-S17 (carried from TCKT_VNEXT-D2-S3).
Checks dry-run at the base before the cut: AR35-y-AC1 base FAIL as expected (no test file); AR35-y-AC2 as on TO-AR-y-31.
