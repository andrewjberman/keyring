# TO DSGN_IRPTV1.TO-IV-e-80 -- Identity shows WHO, HOW MUCH, AS OF and OVER WHAT only; "About this scope" goes (AD-13)

<to_id>DSGN_IRPTV1.TO-IV-e-80</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~42</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>true</direct_act>
<risk>LOCAL</risk>
<worker_class>worker-light</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Decomp cell:** `IV-e-80` (decomp v10) | **outcome_ref:** FWD-1 (the header's identity reads in client words) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IV-e-80` -- master brief AD-13 (`docs/briefs/irpt-master-guidance-brief-20260928.md`, Andrew-direct via CTO 102455):
"The 'About this scope' dropdown and its fields go." Acceptance, verbatim: "Identity shows WHO, HOW MUCH, AS OF and OVER WHAT only;
no 'About this scope' control or its fields; one date format on the card." It supersedes UIC-17's "show a real date or omit the
field" (the walk found "Scope as of unknown" and "Cohort (not asserted) supervision: withheld, advisory: withheld" inside it on all
three clients).

At portal DEV `29b33ef1` (IR = portal/src/pages/InvestorReporting): `IR/header/IdentityCard.tsx` renders, at :625-632,

```
<details className="mt-4" data-slot="about-scope-disclosure">
  <summary ...>About this scope</summary>
  <div className="mt-2"><ScopeSummary scope={scope} selection={selection} row={row} /></div>
</details>
```

**Build:** remove that `<details>` block from IdentityCard, and the `ScopeSummary` import if nothing else in the file uses it (leave
`IR/header/ScopeSummary.tsx` itself in place, unedited -- other surfaces may import it). The card keeps WHO, HOW MUCH, AS OF and OVER
WHAT exactly as they render today, and the OVER WHAT account disclosure stays (it is the OVER WHAT field's own list, not "About this
scope"). Update the file's header comment that describes the disclosure. Tests that pin the disclosure's presence (at least
`__tests__/dsgn-irptv1/iv-e-38.header-identity.test.tsx` UIR-22, `iv-e-86.scope-dates.test.ts`, `iv-t-1.indicator-and-vocabulary.test.ts`,
`iv-e-23.identity-firm.test.ts` -- find every test whose assertions break) are re-goldened to AD-13: each keeps its claim where the claim
still stands elsewhere, or asserts the field's absence, and each rewrite names AD-13 in a comment. Never delete a test file.

**Environment:** base your portal worktree on local DEV `29b33ef1`. Do not start any server. Work ONLY in your own <WS>.

### ACCEPTANCE

<criterion id="IVE80-AC1" cell_refs="IV-e-80"><invocation>cd <WS>/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-100.identity-four-fields.test.ts 2>&1 | tail -12</invocation><expect>VERDICT: IDENTITY-FOUR-FIELDS-OK and 0 fail</expect></criterion>
`IVE80-AC1` -- write `iv-e-100.identity-four-fields.test.ts`: render `IdentityCard` (`createElement(IdentityCard, { scope, selection,
row })` with `fixtures/resolvedScope.success.json`, `fixtures/directoryEntry.success.json` through `header/search.ts`'s `toOptionRow`
and `selectionFor`, as `iv-e-38` / `iv-e-72` already do) and assert: no `data-slot="about-scope-disclosure"`, no "About this scope"
text, none of "Scope as of", "Cohort", "withheld"; CONTROL (must hold at the base too): the four labels WHO, HOW MUCH, AS OF and OVER
WHAT are present. Print `VERDICT: IDENTITY-FOUR-FIELDS-OK` only when every arm holds.

<criterion id="IVE80-AC2" cell_refs="IV-e-80"><invocation>cd <WS>/portal && timeout 580 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting 2>&1 | grep -E "^ *[0-9]+ fail$"</invocation><expect> 5 fail (the known five: fixture set smoke map, source bounds, F25-AC2 x2, F25-AC3 -- list them by name in your report)</expect></criterion>
`IVE80-AC2` -- the IR suite after the re-goldens: exactly the known five fail, each named in your report (a process-spawning test
cut at its time cap under load, if any, is named and re-run alone). One-line reason for a second criterion: the removal breaks
pinned tests by design, and the re-golden set is part of the build.

<expected_criteria>IVE80-AC1, IVE80-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `ScopeSummary.tsx`, `src/lib/**`,
  `src/components/**` and every other page are read, never edited.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on local DEV `29b33ef1`). Commit through `.tools/safe-commit.sh`. Never
  push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** synthetic ids only; never type a firm token or a real client figure into a new file (the LGIC naming gate refuses
  hand-typed firm tokens -- read fixtures by path, never by a firm name).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not
  weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-100.identity-four-fields.test.ts
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v10, cell `IV-e-80`.
<owned_cells>IV-e-80</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE80-AC1, IVE80-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~42/DSGN_IRPTV1.TO-IV-e-80.identity-four-fields.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE80-AC1 IVE80-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id
`DSGN_IRPTV1-W42-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read at portal DEV 29b33ef1: IdentityCard.tsx:625-632 about-scope-disclosure with ScopeSummary; the four identity fields render above it; pinned tests found by grep: iv-e-38, iv-e-86, iv-t-1, iv-e-23.
lane: the <paths> block IS the grant; IV-e-81 (same slot, next in queue) re-touches __tests__/ header pins and runs after this order drains.
</preflight>

Authority: 1.0.0_SA_CTO 102636 (cut AD-10..13 as the next round). Seating: slot ~42, `.tools/wk-provision.sh provision DSGN_IRPTV1 42
--path <abs> --portal-ref 29b33ef1`.
