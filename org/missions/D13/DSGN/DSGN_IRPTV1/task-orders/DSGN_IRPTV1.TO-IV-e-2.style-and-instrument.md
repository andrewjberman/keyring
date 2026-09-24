# TO DSGN_IRPTV1.TO-IV-e-2 -- STYLE + INSTRUMENT: the two components onto the tokens; a smoke fixture that resolves a scope

<to_id>DSGN_IRPTV1.TO-IV-e-2</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~5</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-24</issued_date>
<status>pending</status>
<round>2</round>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.5 @1cccbe6bc6 | **Decomp cell:** `IV-e-2` (decomp v2 @2a26e433b3) | **outcome_ref:** FWD-5, FWD-6, FWD-10 | **rows:** C-S13, C-S14 | **depends_on:** IV-e-1 (same slot) | **slot:** ~5, queue position 2 of 3

---

## WORKER FACE

### THE CELL

`IV-e-2` -- the round's ONE batched style + instrument cell (spine L10; ROUND_ANALYSIS item 2).

**(a) STYLE (row C-S13).** `portal/src/pages/InvestorReporting/tabs/reporting/PerformanceHeadline.tsx` and `portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx` style their own text with `text-slate-*` and `font-semibold` (600). DESIGN.md C1 admits weights 400 and 700 only; C9 makes body ink navy with the darkGray secondary on a panel. `header/IdentityCard.tsx` is the REFERENCE (read, never edit): its ink is `text-[hsl(var(--palette-navy))]` / `text-[hsl(var(--palette-darkGray))]`, its weights `font-bold` / `font-normal`, its hairline `border-[hsl(var(--hairline))]`. Move both files' OWN classes onto those tokens: every `text-slate-*` -> the navy or darkGray token by role (primary figure/label = navy; secondary label = darkGray), every `font-semibold` -> `font-bold` (a heading/figure) or `font-normal` (body), every `border-slate-*` -> the hairline token, `bg-white` on a control stays. Shared components (`PanelHeader`, `PanelFooter`, `PageSurfaceControl`) are DSGN_REBRND's and are NOT touched. No wire fact's TEXT changes -- a class-only diff.

**(b) INSTRUMENT (row C-S14).** Every round-1 AC4 PNG was the "Scope could not be resolved" page because the smoke fixtures never drive `resolve-scope` to a resolved state (FIXTURES-MATCH 1 of 2 / 1 of 9). Build ONE new fixture `portal/src/pages/InvestorReporting/fixtures/smoke/dsgn-irptv1-cottonwood.json` in `scripts/ui-smoke.mjs`'s grammar (`{"<url-substring>": <response body>, ...}`; read the script's header and `fixtures/smoke/fe-s-14-cottonwood.json` as the seed) whose stubs let the page reach a RESOLVED scope with the Cottonwood account selected and BOTH tabs' bodies mounted: resolve-scope (Global context or a firm scope), directory-search / browse returning the account, selections (`POST` -> `sel_<64hex>`, `account_set_id`, fingerprint), holdings-snapshot (adapt the served-shape wire from `fixtures/wire/` or the round-1 capture `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/anna.holdings-nodes.dec293d6.json` -- note it is the PLATINUM node shape, not the API response; the API's wire shape is what the page adapts, so build the response from `fixtures/wire/` and name the seam honestly), performance-report (from the wire fixture). If the page needs a `--select`/`--click` sequence, put the exact `ui-smoke.mjs` command in the result file. The proof is a PNG that shows `IdentityCard`, and on the Holdings tab `SecurityList` (or on Performance `PerformanceHeadline`) -- measured by the script's own `FIXTURES-MATCH` line reading every route matched and by a DOM read: run the same page with `--fixtures` and print the count of `data-slot="identity-card"`-bearing markup (add that `data-slot` to the card's root ONLY if absent -- that is a one-attribute touch on `header/IdentityCard.tsx`, admitted here) via the script's console output or a second headless read. If the fixture cannot reach a resolved scope after an honest attempt, REFUSE IVE2-AC2 with the FIXTURES-MATCH measurement and the last unresolved route; the AC4 faces then keep the static markup as the instrument (the CTO's stated alternative).

### ACCEPTANCE

<criterion id="IVE2-AC1" cell_refs="IV-e-2"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~5; timeout 120 python -c "import io,re;fs=['src/pages/InvestorReporting/tabs/reporting/PerformanceHeadline.tsx','src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx'];tot={'slate':0,'semi':0};[tot.__setitem__('slate',tot['slate']+len(re.findall(r'\b(?:text|border|bg|ring)-slate-\d+',io.open(f,encoding='utf-8').read()))) or tot.__setitem__('semi',tot['semi']+len(re.findall(r'\bfont-semibold\b',io.open(f,encoding='utf-8').read()))) for f in fs];print('CLASS-CENSUS over',len(fs),'files: slate tokens',tot['slate'],'| 600 weights',tot['semi']);print('VERDICT:','TOKENS-ONLY' if tot['slate']==0 and tot['semi']==0 else 'SLATE-OR-600-REMAIN')"</invocation><expect>VERDICT: TOKENS-ONLY</expect></criterion>
`IVE2-AC1` -- the style census over the two files' own source: zero `slate` colour tokens, zero `font-semibold`. Denominator printed (2 files). **At issuance this reads 38 slate / 11 semibold (the CVO's census) -- the criterion detects the defect.**

<criterion id="IVE2-AC2" cell_refs="IV-e-2"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~5; timeout 120 sh -c 'node scripts/ui-smoke.mjs investor-reporting <WS>/org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~5/iv-e-2.png --port 5181 --fixtures src/pages/InvestorReporting/fixtures/smoke/dsgn-irptv1-cottonwood.json 2>&1 | tail -12'</invocation><expect>FIXTURES-MATCH: matched</expect></criterion>
`IVE2-AC2` -- the instrument: with your fixture the smoke run's own `FIXTURES-MATCH` line reads every route matched (print it; the expectation anchors on the line, your result file states `matched N of N` with N = the fixture's route count) and the saved PNG is NOT the unresolved-scope page (state in the result file which components are visible; the CVO reads the PNG). Start your own dev server first (`bun run dev --port 5181` from `<WS>/portal`, in the background; never 5174/5175, other seats'); stop it when done. A partial match is a REFUSAL with the measurement, not a pass.

<criterion id="IVE2-AC3" cell_refs="IV-e-2"><invocation>cd <WS>/portal && export OPAL_AGENT_SERIAL=0.9.0_WK_DSGN_IRPTV1~5; timeout 180 /c/Users/AndrewBerman/.bun/bin/bun test src/pages/InvestorReporting/__tests__/dsgn-irptv1/ 2>&1 | tail -6</invocation><expect> 0 fail</expect></criterion>
`IVE2-AC3` -- the seam: a class-only diff moves no fact -- every dsgn-irptv1 suite (round 1's seven plus IV-e-1's two) still passes at your branch tip. The runner's summary line is the output.

<criterion id="IVE2-AC4" cell_refs="IV-e-2" judgment="true"/>
`IVE2-AC4` -- graded at L9 by `3.0.0_SA_CVO` from the PNG (if IVE2-AC2 passed) and the two components' static markup: C1, C3, C9 conformance -- navy ink on white, no slate, weights 400/700 only. RECORD; NO VERDICT.

<expected_criteria>IVE2-AC1, IVE2-AC2, IVE2-AC3, IVE2-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. `header/IdentityCard.tsx` is admitted for ONE root `data-slot` attribute only if absent; the panel primitives, `PageSurfaceControl`, `render/**`, `contracts/**`, `api/**`, `scripts/ui-smoke.mjs` are OUT.
- **Two repos, one worktree pair** (same pair as IV-e-1; your branch carries its commits). Same commit discipline. Never push, merge, rebase, `checkout --`, `clean`.
- **Toolchain.** As IV-e-1. A dev server you start is yours to stop.
- **The rules:** no wire fact's text changes in (a); the fixture in (b) proves a RENDER, never FWD-1 (the PRD's fixture rule stands); a firm token in a NEW file's text is refused by the naming gate -- the fixture file is JSON data, which the gate does not grade as a code literal; if it does refuse, file a row citing W3-S2 and name the fixture by a neutral filename.
- **Refusal clause.** As every order.
- **Your queue.** IV-e-6 follows.

<paths>
portal/src/pages/InvestorReporting/tabs/reporting/PerformanceHeadline.tsx
portal/src/pages/InvestorReporting/tabs/holdings/SecurityList.tsx
portal/src/pages/InvestorReporting/header/IdentityCard.tsx
portal/src/pages/InvestorReporting/fixtures/smoke/dsgn-irptv1-cottonwood.json
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v2 @2a26e433b3, cell `IV-e-2`.
<owned_cells>IV-e-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `IVE2-AC1` .. `IVE2-AC4`. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~5/DSGN_IRPTV1.TO-IV-e-2.style-and-instrument.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> IVE2-AC1,IVE2-AC2,IVE2-AC3,IVE2-AC4` BEFORE the flip. `IVE2-AC4` recorded `UNVERIFIABLE-BY-INSTRUMENT` naming `3.0.0_SA_CVO`. Result file `style-and-instrument.result.md`.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W5-S<k>`, continuing your slot's sequence).

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 v2 as the gate register; none owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- the round-1 sweep stands.
comp-adversary: RUN at L5 v2 on the PRD (9/9 commits verified; 6 paths, 5 stable, 1 flagged).
lane: the <paths> block IS the grant. All four portal files are this project's; the fixture folder is this project's write surface under the PRD's __tests__/fixtures grant.
</preflight>

Seating: slot ~5, queue position 2 (after IV-e-1, before IV-e-6), same worktree pair.
