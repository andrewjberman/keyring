# TO DSGN_IRPTV1.TO-IV-e-38 -- O2/O8 header: WHO is the client name, the firm by display name once, the firm control follows the client, client language in the empty state and the disclosure

<to_id>DSGN_IRPTV1.TO-IV-e-38</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~25</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-26</issued_date>
<status>complete</status>
<round>7</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.15 @f12fcbb16e | **Decomp cell:** `IV-e-38` (decomp v7; PRD C29 (header rows)) | **outcome_ref:** FWD-2, FWD-15, FWD-11, FWD-16, FWD-18 | **depends_on:** IV-e-37 (same slot, queue) | **slot:** ~25, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-38` -- O2/O8 header: WHO is the client name, the firm by display name once, the firm control follows the client, client language in the empty state and the disclosure. Andrew's UI review of the Investor Reporting page (PRD v0.15, the UI REVIEW FINDINGS table); each row
below is the register's acceptance line, verbatim, and it is this cell's bar:

- **UIR-05** -- The empty-state line uses client language only (no 'Resolution').
- **UIR-12** -- WHO shows the client's name only; accounts appear under Over what.
- **UIR-13** -- The line reads the firm's display name with normal punctuation.
- **UIR-14** -- After choosing a client the firm control shows that client's firm (or clearly says the list is all firms).
- **UIR-22** -- The disclosure uses client language, or moves behind the system-facts click.
- **UIR-30** -- The firm shows by display name, once.

**Where it lives** (a read-only map at DEV fdccc6e6; paths under `portal/src/pages/InvestorReporting/` unless they start `src/`):

- UIR-05: `index.tsx`:291 (the 'Resolution' copy).
- UIR-12: `header/IdentityCard.tsx` :435 (`who = row.label`). UIR-13: `IdentityCard.tsx` :436 and :464.
- UIR-14: `header/FirmDropdown.tsx` :75, plus `index.tsx`:264-268.
- UIR-22: `IdentityCard.tsx` :525-528 ('About this scope').
- UIR-30: `global/FirmAttribution.tsx` :54 (mounted at `tabs/holdings/HoldingsTab.tsx`:285 and `tabs/reporting/ReportingTab.tsx`:431: do not edit the mounts).
- Edit `index.tsx` only at the two places named; TO-IV-e-36 threads the Performance export target through `index.tsx` in parallel, and the issuer merges both.

**Environment:** the portal worktree is based on DEV `fdccc6e6` (round 6 merged). The test file does not exist at the base: write it from the rows above against
fixtures (`IR/fixtures`, discovered from disk) and a stubbed api (the pattern in `__tests__/dsgn-irptv1/iv-e-33.*` and `iv-e-34.*`), one
named arm per row (UIR-05, UIR-12, UIR-13, UIR-14, UIR-22, UIR-30); a row a render cannot decide (layout, overlap, wrapping) is asserted on the markup contract that produces
it (the class, attribute or element), and the row is also judged on the live walk. It prints the VERDICT only when every arm holds.
Do not start any server (dev builds run on port 5174 only, serving the main checkout). Other round-7 chains run in parallel on other
slots over other files; edit only your `<paths>`.

### ACCEPTANCE

<criterion id="IVE38-AC1" cell_refs="IV-e-38"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-25/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~25; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-38.header-identity.test.tsx 2>&1 | tail -25</invocation><expect>VERDICT: HEADER-IDENTITY-OK</expect></criterion>
`IVE38-AC1` -- one arm per row above, each named by its id, each asserting that row's acceptance line on the rendered page or the
code path that produces it. It prints `VERDICT: HEADER-IDENTITY-OK` only when every arm holds.

<criterion id="IVE38-AC2" cell_refs="IV-e-38" judgment="true"/>
`IVE38-AC2` -- graded at L9 by `3.0.0_SA_CVO` (PRD v0.15: "3.0.0_SA_CVO grades each id") on the issuer's live walk of portal DEV after
the drain: each row above, read on the running page at 1440 px. RECORD; never self-graded.

<expected_criteria>IVE38-AC1, IVE38-AC2</expected_criteria>

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
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/header/FirmDropdown.tsx
portal/src/pages/InvestorReporting/global/FirmAttribution.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-38.header-identity.test.tsx
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v7, cell `IV-e-38`.
<owned_cells>IV-e-38</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE38-AC1, IVE38-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~25/DSGN_IRPTV1.TO-IV-e-38.header-identity.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE38-AC1,IVE38-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W25-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN at L5 v7 -- a read-only write-set map of C26-C33 at portal DEV fdccc6e6 (every UIR row located to file:line; overlap matrix); round 7 is re-cut by write set from it.
lane: the <paths> block IS the grant; chain 25 (after IV-e-37 on the same worktree); disjoint from every other chain that runs in parallel with it.
</preflight>

Seating: slot ~25, queue position 2 of 2; start: after IV-e-37 on the same worktree.
