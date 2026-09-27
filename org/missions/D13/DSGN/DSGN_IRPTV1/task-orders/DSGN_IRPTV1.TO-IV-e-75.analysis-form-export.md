# TO DSGN_IRPTV1.TO-IV-e-75 -- Analysis setup behaves like a form; Export on Analysis follows an answer-bearing signal (UIC-18..22, W35-S2)

<to_id>DSGN_IRPTV1.TO-IV-e-75</to_id>
<project>DSGN_IRPTV1</project>
<issued_to>0.9.0_WK_DSGN_IRPTV1~39</issued_to>
<issued_by>2.0.0_SA_COO~D</issued_by>
<issued_date>2026-09-27</issued_date>
<status>pending</status>
<round>9</round>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>WS</placeholders>

**Directive:** D13 | **Fabric:** laptop | **PRD:** v0.18 @5d44d0fa62 | **Round:** 9 (CTO analysis @071e09aa18, msg 102160) | **Item:** E8 | **Decomp cell:** `IV-e-75` (decomp v9) | **outcome_ref:** FWD-7, FWD-8, FWD-9, FWD-18 | **depends_on:** IV-e-74 (same slot) and TO-IV-e-67 drained (export/ExportButton.tsx, export/submit.ts) | **slot:** ~39, queue position 2 of 2

---

## WORKER FACE

### THE CELL

`IV-e-75` -- Rows (acceptance lines verbatim, PRD v0.18): UIC-18 "Pressing a card selects it visibly and the form asks for what that variant needs (for example 'Add at least two models'); no system sentence."; UIC-19 "The default title names the client (and the variant), never one account of several."; UIC-20 "Required-field messages appear after the user tries to generate (or leaves the field), not on load."; UIC-21 "No placeholder or label is truncated at 1440 px."; UIC-22 "Analysis shows a loading state until the snapshot read answers; a refusal only after it answers."

File:line facts: `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round9-writeset-map-20260927.md` rows UIC-18..22 (composer.ts, GenerateComposer.tsx, VariantCards.tsx, AnalysisTab.tsx) and 'Analysis Export signal' (AnalysisTab report :116 is always null live; TabShell.tsx :55/:164; index.tsx gate :270 and ExportButton mount :272-291; submit.ts buildAnalysisSubmitRequest :100). W35-S2: index.tsx closes Analysis Export outright (analysisExportGateOk).

**Build:** Meet each UIC line. Export on the Analysis tab opens only when the tab holds an answer-bearing report (from the reopened/READY request), carrying that report's refs, and uses buildAnalysisSubmitRequest; closed otherwise.

**Environment:** the portal worktree is based on the local DEV the issuer names in the spawn prompt (local DEV 3b98939b (round 8 drained), plus any chain this one follows). Other round-9 workers run in parallel on disjoint files; edit only your `<paths>`. Do not start any server. Work ONLY in your own <WS>. A workspace history rewrite runs ~03:00-05:00Z: commit before 03:00Z.

### ACCEPTANCE

<criterion id="IVE75-AC1" cell_refs="IV-e-75"><invocation>cd C:/Users/AndrewBerman/Desktop/wk-DSGN_IRPTV1-39/portal && timeout 120 /c/Users/AndrewBerman/.bun/bin/bun test ./src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-75.analysis-form-export.test.tsx 2>&1 | tail -20</invocation><expect>VERDICT: ANALYSIS-FORM-EXPORT-OK</expect></criterion>
`IVE75-AC1` -- the built behaviour: one arm per UIC row (18..22); (f) Analysis Export open with an answer-bearing report and closed without; control: Performance Export unchanged. Print `VERDICT: ANALYSIS-FORM-EXPORT-OK` only when every arm holds.
<criterion id="IVE75-AC2" cell_refs="IV-e-75" judgment="true"/>
`IVE75-AC2` -- judgment: the rows above read on the running page (round-9 walk), graded by 3.0.0_SA_CVO at L9. Record it as UNVERIFIABLE-BY-INSTRUMENT with a status_reason naming the CVO; never PASS or FAIL.

<expected_criteria>IVE75-AC1, IVE75-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Every file not named is read, never edited. The `__tests__/` grant (where named) is for re-goldening a pinned test that asserted the old behaviour, each re-golden naming its row.
- **Two repos, one worktree pair** (`<WS>`, `<WS>/portal`). Commit through `.tools/safe-commit.sh`. Never push, merge, rebase, `checkout --` or `clean`. Never stage the workspace `portal` gitlink.
- **Fixtures:** discover fixture names from disk; never type a firm token or a real client figure into a new file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row, and do not weaken the test to pass.

<paths>
portal/src/pages/InvestorReporting/tabs/analysis/composer.ts
portal/src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx
portal/src/pages/InvestorReporting/tabs/analysis/VariantCards.tsx
portal/src/pages/InvestorReporting/tabs/analysis/AnalysisTab.tsx
portal/src/pages/InvestorReporting/tabs/TabShell.tsx
portal/src/pages/InvestorReporting/index.tsx
portal/src/pages/InvestorReporting/export/ExportButton.tsx
portal/src/pages/InvestorReporting/export/submit.ts
portal/src/pages/InvestorReporting/__tests__/dsgn-irptv1/iv-e-75.analysis-form-export.test.tsx
portal/src/pages/InvestorReporting/__tests__/
org/missions/D13/DSGN/DSGN_IRPTV1/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D13/DSGN/DSGN_IRPTV1/decompositions/DSGN_IRPTV1_DECOMP.md</decomp_doc> v9, cell `IV-e-75`.
<owned_cells>IV-e-75</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IVE75-AC1, IVE75-AC2. Instance at `org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/0.9.0_WK_DSGN_IRPTV1~39/DSGN_IRPTV1.TO-IV-e-75.analysis-form-export.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IVE75-AC1,IVE75-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape; surprise rows in the investigation file (id `DSGN_IRPTV1-W39-S<k>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no scheduled producer or schedule surface is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- no cell writes an AWS surface.
comp-adversary: RUN -- read-only write-set map at portal DEV 3b98939b (org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/round9-writeset-map-20260927.md, @51ec23d744); CTO analysis org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_N_ANALYSIS_DSGN_IRPTV1_ROUND8_20260927.md @071e09aa18.
lane: the <paths> block IS the grant; disjoint from every parallel round-9 chain (decomp v9 table).
</preflight>

Seating: slot ~39, queue position 2 of 2; worktree pair provisioned by `.tools/wk-provision.sh provision DSGN_IRPTV1 39 --path <abs> --portal-ref <DEV at seating>`.
