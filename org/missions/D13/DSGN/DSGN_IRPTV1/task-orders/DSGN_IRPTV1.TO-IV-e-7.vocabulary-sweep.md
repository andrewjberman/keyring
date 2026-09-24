# TO DSGN_IRPTV1.TO-IV-e-7 -- FWD-11 sweep (the JOIN cell): the producer's vocabulary off every body

<to_id>DSGN_IRPTV1.TO-IV-e-7</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~7</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>superseded</status>
<round>2</round>
<placeholders>WS, PORTAL_REF</placeholders>

**TERMINAL: `superseded` -- SET BY THE ISSUER `2.0.0_SA_COO~D` 2026-09-24 ~17:5xZ, WITH ITS POINTER: superseded by FAST lease, org/mcp/drive-mode.log line 1** (Andrew-direct ~17:4xZ blast mode, record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_174xZ_BLAST_MODE_P_M_Y_D_ONLINE_FAST_CLOSER.md`). Never spawned. The FWD-11 sweep's work carries onto `org/missions/D13/DSGN/DSGN_IRPTV1/STATUS.md`'s next-list; the AC2 premise defect (row DSGN_IRPTV1-S7 notes) goes with it.

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.5 @1cccbe6bc6 | **Decomp cell:** `IV-e-7` (decomp v2 @2a26e433b3) | **outcome_ref:** FWD-11, FWD-10 | **depends_on:** IV-e-8, IV-e-6, IV-e-5 (the JOIN: spawned on the round-2 candidate after chains A, B, C merge) | **slot:** ~7, queue position 1 of 1

---

## WORKER FACE

### THE CELL

`IV-e-7` -- the FWD-11 SWEEP (PRD candidate C14; ROUND_ANALYSIS item 7), graded ONCE on the assembled round-2 candidate. Your portal worktree is based on the candidate `dsgn-irptv1-r2` AFTER the other seven cells merged into it, so every body you grade is the one that will land. Today the `AnswerStatus` band prints the envelope STATE and the public REASON CODE verbatim on every answer-bearing Performance and Holdings body (ruling H, FE-s-30/40), and `HoldingsQualification` prints "Classification unknown for N of M" on the Holdings body.

**What changes (CTO ruled touch T5).** (a) `tabs/reporting/ReportingTab.tsx`: the `<AnswerStatus report={report} complete={shownComplete} />` mount is replaced by a footer disclosure INSIDE the Performance headline's footer (`PerformanceHeadline.tsx`, this project's file, already carries a footer + popover: extend it to carry state, reason code, business date and the qualified-answer words); on a QUALIFIED answer (`!shownComplete`) a one-line marker in advisor words ("Qualified answer -- details below") stays visible at the top of the body, never the token or the code. (b) `tabs/holdings/HoldingsTab.tsx`: the `<AnswerStatus .../>` mount and the `<HoldingsQualification .../>` mount are replaced by a Holdings footer (`PanelFooter` + `HelperTip` popover, mounted at the bottom of the tab body) carrying state, reason, business date, the classification gap ("N of M holdings not yet classified") and the model-revision fact; the same qualified-answer marker rule. `tabs/reporting/AnswerStatus.tsx` is NOT edited (its export stays for the print plane and any other consumer). (c) The header: nothing -- `IdentityCard` already keeps the bookkeeping in its disclosure. (d) The Analysis tab: NOT touched (Y-written under the closer contract; the CTO placed its half in round 3 with the stepper) -- your census reports Analysis's leaks as a MEASUREMENT, not a defect of this cell.

**Ruling H's requirement is kept one click down:** every answer-bearing body still carries state, reason and business date SOMEWHERE on its face -- in the footer's popover -- and your census's positive control proves each fact is retained.

**Fixtures:** the adapted `performanceReport.*.json` / `holdingsSnapshot.*.json` set incl. a PARTIAL / NEEDS-CORRECTION variant (`fixtures/performance.partial-scope.json`, `fixtures/smoke/reporting-answer-bearing-partial.json`'s wire) so the qualified marker is exercised.

### ACCEPTANCE

<criterion id="IVE7-AC1" cell_refs="IV-e-7"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~7; timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-7.vocabulary-census.test.ts 2>&1 | tail -30</invocation><expect>VERDICT: BODIES-CLEAN</expect></criterion>
`IVE7-AC1` -- the census with its positive control: render the header + Performance body + Holdings body (static markup on the fixtures, complete AND qualified variants) and, over every element OUTSIDE a disclosure surface (`details`, the `HelperTip` popover content, any `data-slot` ending in `-disclosure` / `-detail` / `-footer`), assert ZERO occurrences of: the closed envelope states (`READY`, `PARTIAL`, `STALE`, `UNAVAILABLE`, `RETRYABLE`, `UNCERTAIN`, `NEEDS-CORRECTION`, `FAILED`, `LOADING`), any public reason code from `render/Page.tsx`'s generated set, any revision id (`rev-`, `revisionId` values), fingerprint (64-hex), `sel_` / `acc_` / `req_` ids, `sourceCoordinate` strings, `basis` / `denominator` / `provenance` words as labels; and assert that EVERY one of those facts present on the fixture IS found inside a disclosure surface (`RETAINED: r of r facts`). Print `BODY-LEAKS: <list or none>` per body and `ANALYSIS-LEAKS (measured, not graded): <count>`. `VERDICT: BODIES-CLEAN` only when the header, Performance and Holdings bodies leak nothing and every fact is retained.

<criterion id="IVE7-AC2" cell_refs="IV-e-7"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~7; timeout 240 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/ src/pages/InvestorReporting/__tests__/fe-s-7/ src/pages/InvestorReporting/__tests__/fe-s-30/ src/pages/InvestorReporting/__tests__/fe-s-32/ 2>&1 | tail -6</invocation><expect> 0 fail</expect></criterion>
`IVE7-AC2` -- the seam with everything this round built and the ruling-H suites: every dsgn-irptv1 suite plus the Holdings, FE-s-30 (answer-bearing states) and FE-s-32 suites pass at your tip (a directory absent at the base is named and skipped; a suite that asserts the band's verbatim text on the BODY is expected to move -- update ONLY the assertions inside `__tests__/dsgn-irptv1/`; a legacy suite that fails because it asserts the old on-body text is a REFUSAL reported with the file name, never edited, and the COO rules it).

<criterion id="IVE7-AC3" cell_refs="IV-e-7"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~7; timeout 120 python -c "import subprocess;b='<PORTAL_REF>';n=subprocess.run(['git','diff','--numstat',b,'--','src/pages/InvestorReporting'],capture_output=True,text=True).stdout.strip().splitlines();files=[l.split()[2] for l in n];allowed={'src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx','src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx','src/pages/InvestorReporting/tabs/reporting/PerformanceHeadline.tsx'};other=[f for f in files if f not in allowed and not f.startswith('src/pages/InvestorReporting/__tests__/dsgn-irptv1/')];print('FILES:',files);print('OUTSIDE-GRANT:',other);print('VERDICT:','SWEEP-IN-GRANT' if files and not other else 'TOUCH-WIDER-THAN-RULED')"</invocation><expect>VERDICT: SWEEP-IN-GRANT</expect></criterion>
`IVE7-AC3` -- the ruled touch T5: against `<PORTAL_REF>` (the round-2 candidate tip you were provisioned from) the only changed files are the two tab shells, the headline and your tests; `AnswerStatus.tsx`, `tabs/analysis/*`, `render/**` untouched.

<criterion id="IVE7-AC4" cell_refs="IV-e-7" judgment="true"/>
`IVE7-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the static markup of both bodies in the complete and the qualified variants (`iv-e-7.*.html`) and the smoke PNG if IV-e-2's fixture renders it: a client looking over the advisor's shoulder reads names, accounts and numbers and not one state token, reason code or hash (brief Part III); the qualified marker reads as advisor words. RECORD; NO VERDICT.

<expected_criteria>IVE7-AC1, IVE7-AC2, IVE7-AC3, IVE7-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `tabs/reporting/AnswerStatus.tsx`, `tabs/analysis/**` (Y's under the closer contract), `render/**`, `state/**`, `contracts/**`, `api/**`, every legacy `__tests__/fe-s-*` file are OUT (read them).
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal` based on `<PORTAL_REF>` = the round-2 candidate after the other seven cells merged). Same commit discipline. Never push, merge, rebase, `checkout --`, `clean`.
- **The rules:** facts MOVE, they never vanish (ruling H kept one click down); no new derived value; "not supplied", never zero.
- **Refusal clause.** As every order. **Your queue:** this order only.

<paths>
portal/src/pages/InvestorReporting/tabs/reporting/ReportingTab.tsx
portal/src/pages/InvestorReporting/tabs/holdings/HoldingsTab.tsx
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceHeadline.tsx
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v2 @2a26e433b3, cell `IV-e-7`.
<owned_cells>IV-e-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `IVE7-AC1` .. `IVE7-AC4`. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~7/DSGN_IRPTV1.TO-IV-e-7.vocabulary-sweep.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> IVE7-AC1,IVE7-AC2,IVE7-AC3,IVE7-AC4` BEFORE the flip. `IVE7-AC4` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`. Result file `vocabulary-sweep.result.md`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W7-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v2 as the gate register -- entry (4), the Analysis half of this sweep, is round 3's; measured here, not graded.
comp-iam: DECLARED-NOT-APPLICABLE -- the round-1 sweep stands.
comp-adversary: RUN at L5 v2 on the PRD (9/9 commits verified; 6 paths, 5 stable, 1 flagged).
lane: the <paths> block IS the grant. ReportingTab.tsx and HoldingsTab.tsx admitted for the AnswerStatus / HoldingsQualification mounts (CTO touch T5); AnswerStatus.tsx and tabs/analysis/** never.
</preflight>

Seating: slot ~7, the JOIN cell; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 7 --portal-ref <the round-2 candidate tip after chains A, B, C merged>`, spawned when those three chains have drained (decomp v2 section 8).
