# TO DSGN_IRPTV1.TO-IV-e-39 -- O3/O4: the account picker tells accounts apart by label and value, lists accounts only, and sits with the period controls; refusals in plain words beside a status icon

<to_id>DSGN_IRPTV1.TO-IV-e-39</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~26</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>complete</status>
<round>7</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.15 @f12fcbb16e | **Decomp cell:** `IV-e-39` (decomp v7; PRD C30 (UIR-15, 16, 18, 19, 21)) | **outcome_ref:** FWD-19, FWD-5 | **depends_on:** TO-IV-e-36 merged to DEV (both edit ReportingTab.tsx) | **slot:** ~26, queue position 1 of 2

---

## WORKER FACE

### THE CELL

`IV-e-39` -- O3/O4: the account picker tells accounts apart by label and value, lists accounts only, and sits with the period controls; refusals in plain words beside a status icon. Andrew's UI review of the Investor Reporting page (PRD v0.15, the UI REVIEW FINDINGS table); each row
below is the register's acceptance line, verbatim, and it is this cell's bar:

- **UIR-15** -- Each picker entry shows a distinct label and the account's value.
- **UIR-16** -- The Performance picker has no 'All accounts' option; it lists accounts only.
- **UIR-18** -- The refusal says in plain words why the figure is not available for this account and what makes it available; no raw code on the face.
- **UIR-19** -- A canvas-level refusal is a status icon beside navy text, never a tinted block.
- **UIR-21** -- The account picker and the period controls sit together inside one panel.

**Where it lives** (a read-only map at DEV fdccc6e6; paths under `portal/src/pages/InvestorReporting/` unless they start `src/`):

- UIR-15 / UIR-16: `tabs/holdings/AccountFilter.tsx` :151-153 (options are 'All accounts' plus `account.label`). The value is on each entry of `header/IdentityCard.tsx` `accountListFromSnapshot` :171 (read, never edited). Holdings also mounts `AccountFilter` (`HoldingsTab.tsx`:297): the Performance change is an additive prop; the Holdings picker keeps its current options.
- UIR-18: `tabs/reporting/ReportingTab.tsx` `WORDED_REFUSAL_WORDS` :188-191 and `ReportingRefusal` :206-218. Each refusal says why and what makes the figure available; no raw code anywhere on the face.
- UIR-19: `ReportingTab.tsx` :210 (the amber block) and `tabs/StatusPanel.tsx` :81-89. Portal law: a canvas-level error is a `status.danger` icon beside navy text, never a red or tinted block (portal DESIGN.md C12, C5.8).
- UIR-21: `ReportingTab.tsx` :390-410 plus `tabs/reporting/PerformanceControls.tsx` :69: the picker and the period controls sit together inside one `Panel`.

**Environment:** the portal worktree is based on the portal DEV the issuer names when this slot is provisioned (DEV after TO-IV-e-36); `git -C <WS>/portal log -1` is your base. The test file does not exist at the base: write it from the rows above against
fixtures (`IR/fixtures`, discovered from disk) and a stubbed api (the pattern in `__tests__/dsgn-irptv1/iv-e-33.*` and `iv-e-34.*`), one
named arm per row (UIR-15, UIR-16, UIR-18, UIR-19, UIR-21); a row a render cannot decide (layout, overlap, wrapping) is asserted on the markup contract that produces
it (the class, attribute or element), and the row is also judged on the live walk. It prints the VERDICT only when every arm holds.
Do not start any server (dev builds run on port 5174 only, serving the main checkout). Other round-7 chains run in parallel on other
slots over other files; edit only your `<paths>`.

### ACCEPTANCE

<criterion id="IVE39-AC1" cell_refs="IV-e-39"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-26/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~26; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-39.account-picker-refusal.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: PICKER-REFUSAL-OK</expect></criterion>
`IVE39-AC1` -- one arm per row above, each named by its id, each asserting that row's acceptance line on the rendered page or the
code path that produces it. It prints `VERDICT: PICKER-REFUSAL-OK` only when every arm holds.

<criterion id="IVE39-AC2" cell_refs="IV-e-39" judgment="true"/>
`IVE39-AC2` -- graded at L9 by `3.0.0_SA_CVO` (PRD v0.15: "3.0.0_SA_CVO grades each id") on the issuer's live walk of portal DEV after
the drain: each row above, read on the running page at 1440 px. RECORD; never self-graded.

<expected_criteria>IVE39-AC1, IVE39-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `contracts/**`, `api/**`, `src/lib/**`,
  `src/ui/**`, `src/components/**` (except a file the block names) and every other page are READ, never edited. A needed edit outside
  the grant is a surprise row, not an edit.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`.
  Never push, merge, rebase, `checkout --` or `clean`.
- **Fixtures:** discover fixture names from disk (row W3-S2); never type a firm token or a real client figure into a new file.
- **Portal law:** light canvas `#F4F6FA`, white panels with a hairline, navy ink, one band per page; no light text on the canvas or a
  panel (portal `CLAUDE.md` and `DESIGN.md`). No ids on screen or in the URL; accounts keyed by the drill_refs id, never by label.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row,
  and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/holdings/AccountFilter.tsx
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/tabs/StatusPanel.tsx
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceControls.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-39.account-picker-refusal.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7, cell `IV-e-39`.
<owned_cells>IV-e-39</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE39-AC1, IVE39-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~26/DSGN_IRPTV1.TO-IV-e-39.account-picker-refusal.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE39-AC1,IVE39-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W26-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v7 -- a read-only write-set map of C26-C33 at portal DEV fdccc6e6 (every UIR row located to file:line; overlap matrix); round 7 is re-cut by write set from it.
lane: the <paths> block IS the grant; chain 26 (after TO-IV-e-36 drains; the slot is provisioned on that DEV); disjoint from every other chain that runs in parallel with it.
</preflight>

Seating: slot ~26, queue position 1 of 2; start: after TO-IV-e-36 drains; the slot is provisioned on that DEV.
