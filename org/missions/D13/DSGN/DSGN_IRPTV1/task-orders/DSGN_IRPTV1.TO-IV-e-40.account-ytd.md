# TO DSGN_IRPTV1.TO-IV-e-40 -- FWD-20: each account's own year-to-date return beside its name in the account chooser, filling in as it arrives

<to_id>DSGN_IRPTV1.TO-IV-e-40</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~26</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>pending</status>
<round>7</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.15 @f12fcbb16e | **Decomp cell:** `IV-e-40` (decomp v7; PRD C26) | **outcome_ref:** FWD-20 | **depends_on:** IV-e-39 (same slot, queue) | **slot:** ~26, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-40` -- FWD-20: each account's own year-to-date return beside its name in the account chooser, filling in as it arrives. Andrew's UI review of the Investor Reporting page (PRD v0.15, the UI REVIEW FINDINGS table); each row
below is the register's acceptance line, verbatim, and it is this cell's bar:

- FWD-20 ACCEPT (PRD v0.15): each of the client's accounts shows its own year-to-date return beside its name where the advisor chooses accounts; the figures fill in as they arrive, and the page stays usable while they do; an account that cannot be computed says so in plain words in its place; there is still no single return for the whole client.

**Where it lives** (a read-only map at DEV fdccc6e6; paths under `portal/src/pages/InvestorReporting/` unless they start `src/`):

- The chooser label: `tabs/holdings/AccountFilter.tsx` :151-153 (after IV-e-39's change on this worktree).
- The fetch belongs in `tabs/reporting/ReportingTab.tsx` :251-293 (the account list and the focus effect). Per-account selection: `tabs/reporting/accountFocus.ts` `resolveAccountFocus` :54, `preselectAccountId` :85. The YTD window: `tabs/reporting/period.ts` `dateWindowForPreset` :78 and `performanceReportRequest` :126; it ends on the data's as-of date as the tab's own presets do.
- Every YTD request is ONE account (its own selection, keyed by the drill_refs id); never a client-set request and never a client total. Requests run without blocking the page; an account whose figure cannot be computed shows plain words in its place.

**Environment:** the portal worktree is based on the portal DEV the issuer names when this slot is provisioned (DEV after TO-IV-e-36); `git -C <WS>/portal log -1` is your base. The test file does not exist at the base: write it from the rows above against
fixtures (`IR/fixtures`, discovered from disk) and a stubbed api (the pattern in `__tests__/dsgn-irptv1/iv-e-33.*` and `iv-e-34.*`), one
named arm per row (FWD-20); a row a render cannot decide (layout, overlap, wrapping) is asserted on the markup contract that produces
it (the class, attribute or element), and the row is also judged on the live walk. It prints the VERDICT only when every arm holds.
Do not start any server (dev builds run on port 5174 only, serving the main checkout). Other round-7 chains run in parallel on other
slots over other files; edit only your `<paths>`.

### ACCEPTANCE

<criterion id="IVE40-AC1" cell_refs="IV-e-40"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-26/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~26; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-40.account-ytd.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: ACCOUNT-YTD-OK</expect></criterion>
`IVE40-AC1` -- one arm per row above, each named by its id, each asserting that row's acceptance line on the rendered page or the
code path that produces it. It prints `VERDICT: ACCOUNT-YTD-OK` only when every arm holds.

<criterion id="IVE40-AC2" cell_refs="IV-e-40" judgment="true"/>
`IVE40-AC2` -- graded at L9 by `3.0.0_SA_CVO` (PRD v0.15: "3.0.0_SA_CVO grades each id") on the issuer's live walk of portal DEV after
the drain: each row above, read on the running page at 1440 px. RECORD; never self-graded.

<expected_criteria>IVE40-AC1, IVE40-AC2</expected_criteria>

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
portal/src/pages/InvestorReporting/tabs/reporting/accountFocus.ts
portal/src/pages/InvestorReporting/tabs/reporting/period.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-40.account-ytd.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7, cell `IV-e-40`.
<owned_cells>IV-e-40</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE40-AC1, IVE40-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~26/DSGN_IRPTV1.TO-IV-e-40.account-ytd.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE40-AC1,IVE40-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W26-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v7 -- a read-only write-set map of C26-C33 at portal DEV fdccc6e6 (every UIR row located to file:line; overlap matrix); round 7 is re-cut by write set from it.
lane: the <paths> block IS the grant; chain 26 (after IV-e-39 on the same worktree); disjoint from every other chain that runs in parallel with it.
</preflight>

Seating: slot ~26, queue position 2 of 2; start: after IV-e-39 on the same worktree.
