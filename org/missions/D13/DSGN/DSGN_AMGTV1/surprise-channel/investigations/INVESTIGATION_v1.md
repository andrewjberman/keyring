# DSGN_AMGTV1 -- surprise channel, INVESTIGATION v1 (round 1, site Z). Append-only; rows below are minted by their own allocator (`.tools/surprise-row-gate.py` validates every NEW row).

```json
[
  {
    "id": "DSGN_AMGTV1-Z-W2-S1",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~2",
    "surfaced_at": "2026-09-29T03:30:00Z",
    "one_line": "The project's surprise-channel tree did not exist -- this worker created the investigation file to have somewhere to append (the <paths> grant names it).",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- a sibling worker slot whose worktree branched before this commit lands may create the same new file under a different header; the drain reconciles by UNION of rows under one header, never by picking one side.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "ls org/missions/D13/DSGN/DSGN_AMGTV1/ at worktree start showed decompositions, deliverables, prd, project.json, task-orders and no surprise-channel directory",
        "the task order <paths> names org/missions/D13/DSGN/DSGN_AMGTV1/surprise-channel/investigations/INVESTIGATION_v1.md; the sibling DSGN_IRPTV1 file is the header precedent"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order says a surprise is appended to INVESTIGATION_v1.md under the project's surprise channel, as if it exists.",
    "world_is": "Neither the file nor its directories existed in the worktree; the worker created them."
  },
  {
    "id": "DSGN_AMGTV1-Z-W2-S2",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~2",
    "surfaced_at": "2026-09-29T03:31:00Z",
    "one_line": "AV-t-2's cell names a direct import of HeroDialog from @/ui/components/graphic/HeroGraphic, but the AC3 bound harness tabs.harness.cjs does not stub that module and stopped loading the page (Cannot find module) -- HeroDialog and DialogStamp are loaded with React.lazy on first card open instead.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "with a top-level import of HeroGraphic in HeaderCards.tsx, bound.cjs HEADER read 'HARNESS RED tabs.harness.cjs :: rc=1 (floor 20)' and the harness stderr read \"Error: Cannot find module '@/ui/components/graphic/HeroGraphic'\" (tabs.harness.cjs:192, its STUBS list names panels, Select, EmptyState, states, Controls, HelperTip, DataTooltip and no HeroGraphic)",
        "after the lazy form: bound.cjs HEADER -> 'HEADER BOUND: 2 of 2 harnesses green' (tabs 20 of 20, errorEmpty 12 of 12); t-2.AC1 3 of 3, t-2.AC2 5 of 5 -- the stub proxy in _load.cjs covers src/ui/ either way",
        "the harness is outside <paths> (bound 2: every harness unchanged), so the only in-grant way to keep AC3 green was to keep the module out of the load path until a card is opened"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Item 1 of the cell: the card's window is the estate's HeroDialog from @/ui/components/graphic/HeroGraphic; AC3 says the two page harnesses green at the base stay green; bound 2 forbids editing any harness.",
    "world_is": "tabs.harness.cjs resolves imports by name against a fixed stub list that omits HeroGraphic, so a static import makes it unloadable. Loaded lazily (React.lazy + Suspense, rendered only while a card is open) the header loads and the window is the same HeroDialog/DialogStamp. A later cell that adds HeroGraphic to the harness stub list could return to a static import."
  },
  {
    "id": "DSGN_AMGTV1-Z-W3-S1",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~3",
    "surfaced_at": "2026-09-29T04:30Z",
    "one_line": "AV-t-3's ThesisCards.tsx imports the estate HeroDialog, which the page harness __harness__/tabs.harness.cjs (unchanged, outside every order's paths) does not stub: that harness loads SecurityAnalysis.tsx -> ThesisTab -> ThesisCards and now dies at load with MODULE_NOT_FOUND, where it read CHECKS-OK 20 of 20 at the base.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- cut a cell whose <paths> grant portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs, adding one STUBS entry for '@/ui/components/graphic/HeroGraphic' ({ HeroDialog, DialogStamp }); until then any drain or QA run of tabs.harness.cjs reads RED for a reason that is not a page defect.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "node tabs.harness.cjs in this worktree (ThesisTab with ThesisCards): 'Error: Cannot find module @/ui/components/graphic/HeroGraphic ... at ThesisCards.tsx:33:23', exit 1; the same command with the base ThesisTab.tsx restored (git show HEAD:portal/src/pages/SecurityAnalysis/tabs/ThesisTab.tsx) printed 'CHECKS-OK 20 of 20', then the new ThesisTab.tsx was put back",
        "tabs.harness.cjs load(): a non-relative name not in its STUBS map goes to require(name); STUBS carries panels, states, Select, EmptyState, Controls but no graphic/HeroGraphic",
        "shell.harness.cjs and posture.harness.cjs also fail in this worktree, on '@/api/api-client' and TimelinePanel.tsx respectively -- neither trace touches ThesisCards or ThesisTab; not caused by this cell"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order's BOUNDS: only the four portal files change and 'every other tab, page and harness: unchanged'; the bound criterion AC3 names only drafting.harness.cjs and thesisLadder.harness.cjs. The cell's own build item requires ThesisCards to open the estate's HeroDialog imported from '@/ui/components/graphic/HeroGraphic'.",
    "world_is": "A third harness, tabs.harness.cjs, walks the whole page including ThesisTab, so the required HeroGraphic import breaks its load. The worker cannot edit it (outside <paths>) and did not; AC1-AC3 are unaffected (all three read green), so the order stays completable and the regression is left for the issuer.",
    "notes": "This file did not exist in the worker's worktree; the worker created it with this header, as the order's <paths> names it. A sibling slot creating the same file independently reconciles by union of rows under one header."
  },
  {
    "id": "DSGN_AMGTV1-Z-W3-S2",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~3",
    "surfaced_at": "2026-09-29T06:25Z",
    "one_line": "AV-t-4 cannot reach tabs.harness.cjs 20 of 20 by the stub alone: with the HeroGraphic stub the harness loads, but check thesis_sentences_and_one_chart reads false (markers 0 of 38 on BA) because AV-t-3 moved every drafted sentence off the Thesis face into card windows.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- amend AV-t-4 (or cut a follow-on) so the check is re-anchored to the face plus each ThesisCardDetail window body, as AV-t-3 did for drafting.harness.cjs and thesisLadder.harness.cjs; until then tabs.harness.cjs reads CHECKS-WRONG-WAY thesis_sentences_and_one_chart (19 of 20).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "in this worktree after merging CLOUD and portal DEV 5fac7a37 and adding the HeroGraphic STUBS entry: node tabs.harness.cjs prints 'CHECK thesis_sentences_and_one_chart false (expected true)' and 'CHECKS-WRONG-WAY thesis_sentences_and_one_chart'; every other check reads true; the per-name detail prints sentences 38, markers 0 (also 35/0, 38/0, 36/0, 38/0)",
        "tabs.harness.cjs:314-319 counts countOf(html, 'data-drafted-sentence=\"') === sentences over the thesis-tab render; the face carries no data-drafted-sentence since ThesisCards.tsx renders them only inside HeroDialog (closed in a static render)",
        "bound.cjs TABS tabs.harness.cjs:20 errorEmpty.harness.cjs:12 drafting.harness.cjs:8 thesisLadder.harness.cjs:10 -> 'TABS BOUND: 3 of 4 harnesses green', exit=1 (errorEmpty 12 of 12, drafting 8 of 8, thesisLadder 10 of 10 green; tabs.harness.cjs rc=1)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The task order: add ONE STUBS entry for HeroGraphic; 'No check is removed, re-anchored or loosened; the 20 claims stay exactly as they are'; AC1 expects TABS BOUND: 4 of 4 harnesses green (tabs 20 of 20).",
    "world_is": "The stub fixes the load only. The 20th claim, that every drafted sentence reaches the Thesis tab render, is false of the merged page as built and ruled by AV-t-3 (sentences live in windows), so 20 of 20 needs that one check re-anchored, which the order forbids. The worker did not re-anchor it; the stub is committed, W3-S1 is NOT dispositioned, and the order stays open."
  },
  {
    "id": "DSGN_AMGTV1-Z-W3-S3",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~3",
    "surfaced_at": "2026-09-29T06:50Z",
    "one_line": "DISARMED: DSGN_AMGTV1-Z-W3-S1 and DSGN_AMGTV1-Z-W3-S2 -- under TO-AV-t-4 (AMENDMENT 1) portal commit 36485a07 (stub 30f69ad0 plus the re-anchor) tabs.harness.cjs loads the merged page and reads CHECKS-OK 20 of 20, and the bound reads TABS BOUND: 4 of 4 harnesses green.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "node bound.cjs TABS tabs.harness.cjs:20 errorEmpty.harness.cjs:12 drafting.harness.cjs:8 thesisLadder.harness.cjs:10 -> tabs 20 of 20, errorEmpty 12 of 12, drafting 8 of 8, thesisLadder 10 of 10, 'TABS BOUND: 4 of 4 harnesses green', exit=0, in /c/tmp/wk-dsgn-amgtv1-3 at portal 36485a07",
        "W3-S1 cause (un-stubbed HeroGraphic import) removed by the STUBS entry in 30f69ad0; W3-S2 cause (sentence markers off the face) removed by the amended thesis_sentences_and_one_chart in 36485a07"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-AV-t-4 bound 4 and AMENDMENT 1: when AC1 passes, append a DISARMED disposition for W3-S1 and W3-S2 naming the order and the portal commit.",
    "world_is": "AC1 passes. The gate refuses `adjudicates` on a worker-surfaced row (L9 carrier), so this is a new OBSERVATION row of standing INERT that names both items; the formal disposition of S1 and S2 is the issuer's / L9's to stamp.",
    "notes": "Worker-authored record of the disarm, not an adjudication."
  },
  {
    "id": "DSGN_AMGTV1-Z-S1",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~D",
    "surfaced_at": "2026-09-29T07:15Z",
    "one_line": "FWD-1's thread name cannot carry hop 6: Valero's model.team_cases are ABSENT for base, upside and downside (so are PBR, BA, HD and NU; INTU's are SERVED), so even after AMGT_RESAPP vv-4 serves team cases, the Recommendation window on Valero can only say the research team's position is not in the pack.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "1.0.0_SA_CTO~Z -- an ENDPOINT-side decision: move FWD-1's thread to a name the team covers (INTU carries all three cases), or route Valero's dossier coverage to AMGT_CORPUS; until then FWD-1 cannot be graded REALIZED on hop 6 whatever the page renders.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PYTHONPATH=. python: scoped_amgt._team_cases(k) for VLO, PBR, BA, HD, NU -> base/upside/downside all ABSENT; INTU -> all SERVED (EPS/Multiple/Price/Return tables), 2026-09-29 ~07:1xZ",
        "the same read captured at model.team_cases in deliverables/2.0.0_SA_COO~D/round2/fixtures/thesisBundle.{VLO,INTU}_US_Equity.json"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD v0.3 FWD-1 DONE WHEN: one live walk ending in Valero's Recommendation card open, where the PM can say whose view it is; THE THREAD hop 6 makes the dossier route (the team's position) round 2's first enrichment input.",
    "world_is": "The team's position is now served as model.team_cases (AMGT_RESAPP vv-2), and Valero's are all ABSENT in the research dossier; the round-2 cell AV-e-2 renders the team's case where served and a plain ABSENT sentence where not.",
    "notes": "Filed by the issuer at the round-2 cut (decomposition v2). Not a DSGN cell: the page renders both states correctly."
  },
  {
    "id": "DSGN_AMGTV1-Z-W8-S1",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~8",
    "surfaced_at": "2026-09-29T08:10Z",
    "one_line": "AV-e-6: two posture.harness.cjs checks (coverage_line_per_side, comparable_incomplete_line) read the raw absent-source string with side.includes(esc(src)); after the build they still pass, but only because the raw string now sits in a data attribute, so no harness edit was made.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs:476 (pack.absent.every(src => side.includes(esc(src)))) and :480-485 (missing.every(src => incompleteRegion.includes(esc(src)))) at f1a90a9b",
        "bound.cjs E6 posture.harness.cjs:32 ... exit=0, posture.harness.cjs CHECKS-OK 32 of 32 on portal 9625bd28 on wk-DSGN_AMGTV1-8-portal; the raw strings are now emitted in data-posture-absent-source and data-posture-missing-sources"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-AV-e-6 section 1: if a bound harness check is anchored on the raw text this cell removes, re-anchor that ONE check onto the same fact as the page now states it and record old anchor -> new.",
    "world_is": "Two checks are anchored on the raw text; the harness file is outside this order's <paths> (a worker may not edit it) and needed no edit, since an HTML-escaped attribute value contains the same escaped string. Old anchor = the raw source string in the visible list item and in the incomplete line's text; new (effective) anchor = the same string in data-posture-absent-source / data-posture-missing-sources. The checks no longer assert the plain-words sentence; a later cell owning the harness may re-anchor them onto the words.",
    "notes": "Worker-authored record; form only, no significance judged."
  },
  {
    "id": "DSGN_AMGTV1-Z-W8-S2",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~8",
    "surfaced_at": "2026-09-29T08:12Z",
    "one_line": "AV-e-6: the Posture face can still print a vendor mnemonic (resolved F: cites read 'figure <MNEMONIC> FY..'), a fit preset code and the 'UNRESOLVED: <key>' comparable fallback; the raw census does not see them on Valero's fixture (0 figures, presets DIVZ/PFOE).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/SecurityAnalysis/postureCites.ts figure branch (hit('figure ${mnemonic}...')) and portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx comparableText() fallback, at portal 9625bd28 on wk-DSGN_AMGTV1-8-portal",
        "raw.cjs posture -> mnemonic=0; machine_word=0; storage_path=0 on the Valero + WMB fixtures: no fixture cite resolves an F: element, so the branch is unexercised by AC1"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-AV-e-6 section 1 and C-PRESENTATION-ONLY: a code or path may sit in a data attribute or in code, never in visible text; the page looks up no name.",
    "world_is": "The payload carries a figure's mnemonic but no plain label, so words for it would need a lookup the page may not make; left unchanged. A name whose model block is served would print its mnemonic in an F: cite.",
    "notes": "Worker-authored record; not fixed here (a label needs the payload to carry one)."
  },
  {
    "id": "DSGN_AMGTV1-Z-W5-S1",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~5",
    "surfaced_at": "2026-09-29T08:00Z",
    "one_line": "tabs.harness.cjs (a bound harness, outside AV-e-1's <paths>) anchors held_uncited_basis_not_a_zero on the raw visible text 'held_uncited_basis ABSENT_ON_OBJECT'; the cell removes that text, and the harness cannot be edited here.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs:329-330 (heldOk: html.includes('held_uncited_basis ABSENT_ON_OBJECT') && !html.includes('0 claims held uncited')) at f1a90a9b",
        "bound.cjs E1 drafting:8 thesisLadder:10 tabs:20 errorEmpty:12 after the edit: 4 of 4 green, tabs CHECKS-OK 20 of 20, using the data attribute below"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-AV-e-1 section 1: a bound check anchored on removed raw text is re-anchored onto the same fact (words or a data attribute), its claim kept; <paths> names drafting.harness.cjs and thesisLadder.harness.cjs, not tabs.harness.cjs.",
    "world_is": "tabs.harness.cjs cannot be re-anchored under this order's write grant. The fact is kept instead on the page: the held-uncited line carries data-held-uncited-basis=\"held_uncited_basis ABSENT_ON_OBJECT\" (an attribute, free under the raw-code rule), so the untouched harness still finds the substring and stays green at 20 of 20. The visible line is a plain sentence. A later cell that edits tabs.harness.cjs may re-anchor it on the attribute name and drop the value-shaped string.",
    "notes": "Worker-authored; not an adjudication."
  },
  {
    "id": "DSGN_AMGTV1-Z-W4-S1",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~4",
    "surfaced_at": "2026-09-29T09:10Z",
    "one_line": "AV-e-4 words the Model tab's refusal lines and case formula, so the page no longer matches the export's own lines that portal exportCompare.harness.cjs (not in the E4 bound) grades it against.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- decide whether the export (lib/research/print/render_pack.py, an AMGT_RESAPP surface) follows the page's wording in a later cell, or exportCompare.harness.cjs is re-scoped to compare on the served reason and formula in the data attributes the page now carries (data-model-line-refusal, data-model-case-formula); until then a run of exportCompare against a fresh export reads the two surfaces as different.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/SecurityAnalysis/__harness__/exportCompare.harness.cjs pageCases() reads each <p data-model-case> text and pageAbsences() reads /REFUSED\\s*--\\s*([^<\\n]+)/, both compared with the export's lines; lib/research/print/tests/test_model_cases_markdown.py pins _model_case_line to '<Name> case: SERVED -- 537.70 (f)' (the served formula, mnemonics included)",
        "AV-e-4 AC1 (raw.cjs model) demands 0 mnemonics and 0 NOT-YET-BUILT in visible text; Valero's served formula reads 'Bloomberg consensus EPS (FY1, BEST_EPS) x adjusted trailing-median P/E (PX_LAST / IS_COMP_EPS_ADJUSTED)' and the served check-face reason reads 'REVENUE_PER_SH: unit/sign convention is NOT-YET-BUILT, not MEASURED', so the page text can no longer be those bytes",
        "node exportCompare.harness.cjs with no arguments prints its usage line (it needs an --pack export path), so the harness was not run against a pack here; the divergence is read from its regexes and the export's pinned line, not from a run"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-AV-e-4 Bounds 2: every other page, component, tab and harness is unchanged; AC1 0 raw-code hits on the Model tab; FWD-30 (page and export read the same lines) is the standing parity the exportCompare harness grades.",
    "world_is": "The page's visible case line is now '<label>: SERVED -- <value> <currency> (<formula with vendor mnemonics removed>)' with the whole served formula in data-model-case-formula, and a refused line reads 'REFUSED -- <one plain sentence>' with the served reason in data-model-line-refusal; the export still prints the served formula and reason verbatim. The bound harnesses (modelPattern 12 of 12, tabs 20 of 20) read green; exportCompare is outside the bound and was not runnable without a pack."
  }
]
```
