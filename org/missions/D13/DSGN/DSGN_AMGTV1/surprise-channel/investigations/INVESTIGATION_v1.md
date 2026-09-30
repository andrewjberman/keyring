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
  },
  {
    "id": "DSGN_AMGTV1-Z-S2",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "2.0.0_SA_COO~D",
    "surfaced_at": "2026-09-29T08:29Z",
    "one_line": "On the round-2 signed-in walk (localhost:5174, DEV 1a1e8162), selecting INTU US fired GET /api/scoped/advisor-intelligence/clients-tab and it answered HTTP 500 ([INFFIN#10] getClientsTab failed); the call is an Advisor Intelligence read, not a Security Analysis route, and the Security Analysis page rendered normally.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "the Advisor Intelligence clients-tab route's owner (not this project) -- who fires this read on a Security Analysis selection, and why it answers 500; nothing on the Security Analysis page depends on it.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "tmp/ui-walk/20260929T082619Z/findings.json api_issues: step 'amgt select INTU US', GET /api/scoped/advisor-intelligence/clients-tab, http 500; console_errors: '[INFFIN#10] getClientsTab failed: Error: API request failed: 500 Internal Server Error' at src/api/endpoints/advisor-intelligence.ts"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "The round's one real run reads the Security Analysis page on served data; the walker's API check lists every non-READY answer on the page's own steps.",
    "world_is": "One non-Security-Analysis read answered 500 during the INTU selection step; no Security Analysis route failed (the walk's other API answers were READY).",
    "notes": "Filed by the issuer at the round-2 close; off-task observation, routed through the channel, not a broker message."
  },
  {
    "id": "DSGN_AMGTV1-Z-W11-S1",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~11",
    "surfaced_at": "2026-09-29T11:10Z",
    "one_line": "AV-r-3 names the Model tab's data attributes as the ABSENCES keys, but the page's other absence gap (missing 2 of 7) is the Posture tab, which also words its absent state in plain sentences; keyed the harness on the Posture tab's own data-posture-reason as well, and the AC1 fixture (1299_HK_Equity) carries no thesis cites, so its CITES line reads 0=0 on both sides.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "portal/src/pages/SecurityAnalysis/tabs/PostureTab.tsx:452-454 (portal DEV 670f29e4): data-posture-status=\"ABSENT\" data-posture-reason=<served reason> on the block whose text reads 'Posture: ABSENT -- no posture has been drafted for this name yet; ...' -- the plain sentence replaces the served reason in the visible text; the export prints the raw reason twice (rich.md lines 259-260)",
        "exportCompare.harness.cjs on served_fixture.1299_HK_Equity.json before the change: ABSENCES page=7 rich=17 same=5 missing=2 extra=12; after keying the refused lines on data-model-line-refusal (inside data-model-row) and the posture absent state on data-posture-reason: page=17 rich=17 same=17 missing=0 extra=0; the export side and its 17 are unchanged",
        "vv-5.AC1.sh CITES page=0 rich=0 on 1299_HK_Equity because that fixture's thesis carries no evidence; the window read was exercised on the tabsFixture set instead (CITES page=43 BA, 28 COST, 30 BABA, 33 HD, 36 SAP) with an empty export, so the rendered cite windows are read"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-AV-r-3 section 1: the ABSENCES gap is the Model tab's refused lines and case formula, keyed on data-model-line-refusal / data-model-case-formula / data-model-row; CITES page 0 is the harness not rendering the card windows.",
    "world_is": "Two of the ABSENCES gaps were the Model tab's refused lines (11 of them, one page-side entry each once keyed on data) and the Posture tab's absent state; the second is outside the TO's named attributes, so data-posture-reason was used, an attribute the Posture tab already serves. No compared set dropped anything: the export's 17 stay 17."
  }
  ,{
    "id": "DSGN_AMGTV1-Z-W12-S1",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~12",
    "surfaced_at": "2026-09-29T10:40Z",
    "one_line": "AV-r-4 AC1 arm A cannot reach 3 of 3 from ExecManagementTab.tsx alone: the one remaining hit is crosswalk/v1 rendered by IdentityLine.tsx (AV-r-1) inside the tab.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {"status": "GROUNDED", "evidence": ["node round3/checks/exec.cjs after the Exec edit: ARM FAIL A hits=[crosswalk/v1]; arms B and C PASS; portal/src/pages/SecurityAnalysis/components/IdentityLine.tsx:73 renders identity.crosswalk_vintage"]},
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-AV-r-4 AC1 expects EXEC ABSENCE IN WORDS 3 of 3; the order says the exec check excludes nothing and the string is AV-r-1's.",
    "world_is": "Arm A reads hits=[crosswalk/v1] only; it clears when AV-r-1 lands IdentityLine, not by any change in this cell's paths."
  }
  ,{
    "id": "DSGN_AMGTV1-Z-W12-S2",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~12",
    "surfaced_at": "2026-09-29T11:10Z",
    "one_line": "Resolves DSGN_AMGTV1-Z-W12-S1: after AV-r-1 drained (DEV f0fbac5b, cb25695b) exec.cjs reads 3 of 3 arms, exit=0.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {"status": "GROUNDED", "evidence": ["node round3/checks/exec.cjs on portal branch wk-DSGN_AMGTV1-12-portal merged with DEV: EXEC ABSENCE IN WORDS: 3 of 3 arms, exit=0; issuer ruling to 0.9.0_WK_DSGN_AMGTV1~12"]},
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "Z-W12-S1: arm A clears when AV-r-1 lands IdentityLine.",
    "world_is": "Arm A hits=[] on the drained base; S1's cause is resolved by the re-grade."
  },
{
 "id": "DSGN_AMGTV1-Z-S3",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-09-29T11:21Z",
 "one_line": "On the round-3 close walk A (localhost:5174, walk build 80a0df1f), after VLO US the walker's session was lost: the INTU and SAP GY select steps logged HTTP 500 twice each and every later screenshot (041-052) is the sign-in page, while the step lines still read '0 finding(s)'; a fresh walk B two minutes later walked both names cleanly.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "disarm_owner": "the ui-walk skill's owner (.claude/skills/ui-walk/walk.mjs): a step that lands on the sign-in page reports 0 findings instead of failing the step, so a void walk reads clean in the log and the summary.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "tmp/ui-walk/20260929T111119Z/findings.json console_errors: steps 'amgt select INTU US' and 'amgt select SAP GY' each 'Failed to load resource: the server responded with a status of 500'; walker:control-missing 'tab not found: Thesis' (and Exec Management, Peers, Model, Posture)",
   "tmp/ui-walk/20260929T111119Z/shots/041-INTU-US-overlay.png and 047-SAP-GY-overlay.png: the 'Welcome back / Sign in' page",
   "tmp/ui-walk/20260929T111809Z/ (walk B, INTU + SAP GY only): 0 API issues, console = 2 login 401s, disarm REFUSED line printed"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "A walk's step line and SUMMARY describe the page the step looked at; a step that cannot reach the page fails loudly.",
 "world_is": "Twelve steps on the sign-in page each printed '0 finding(s)'; only the walker:control-missing findings and the screenshots show the walk was void. Walk A's disarm also printed no 'REFUSED' proof line (walk B's did).",
 "notes": "Filed by the issuer at the round-3 close; the close walk record uses walk A for VLO only and walk B for INTU and SAP GY. The 500 on the select step is likely the Z-S2 class (Advisor Intelligence clients-tab), unconfirmed: walk A's api_issues list was not read per URL."
},
{
    "id": "DSGN_AMGTV1-Z-W13-S1",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~13",
    "surfaced_at": "2026-09-29T14:45Z",
    "one_line": "Git Bash rewrites the walker's --route /security-analysis to C:/Program Files/Git/security-analysis, so walkvoid.sh reached page.goto with an invalid URL until walk.mjs undid the rewrite.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {"status": "GROUNDED", "evidence": ["node -e console.log(process.argv) -- --route /security-analysis under Git Bash prints C:/Program Files/Git/security-analysis", "walk.mjs --no-login --route /security-analysis before the fix: ERROR page.goto: Protocol error (Page.navigate): Cannot navigate to invalid URL, walk void: no, rc=0"]},
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "TO-AV-w-1 AC1 runs walk.mjs --route /security-analysis from bash and expects WALK VOID and a non-zero exit.",
    "world_is": "Under MSYS the route arrives mangled; walk.mjs now strips a leading drive-and-Git prefix from --route values (in the cell's paths), after which walkvoid.sh reads YES exit=0. A walk started from Git Bash without that strip would have failed on the goto, not on the sign-in page."
},
{
 "id": "DSGN_AMGTV1-Z-W23-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~23",
 "surfaced_at": "2026-09-29T16:00Z",
 "one_line": "modelPattern.harness.cjs check negative_values_signed is anchored on '<td data-model-cell=\"true\" class=' which M1 (data-model-cell carries the served value) necessarily removes; the harness is not in AV-u-5 <paths>, so it cannot be re-anchored.",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal wk-DSGN_AMGTV1-23-portal@ae1be3c8: node src/pages/SecurityAnalysis/__harness__/modelPattern.harness.cjs -> CHECKS-OK 11 of 12, CHECKS-WRONG-WAY negative_values_signed (0 of 155 cell texts match)",
   "modelPattern.harness.cjs:155 regex /<td data-model-cell=\"true\" class=\"[^\"]*\">([^<]*)/g"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "AV-u-5 AC2 expects modelPattern.harness.cjs:12 green, and the order lets a re-anchor happen only in a harness named in <paths>.",
 "world_is": "The harness is in portal/src/pages/SecurityAnalysis/__harness__/, not in <paths>. Needed re-anchor: cell regex to /<td data-model-cell=\"[^\"]*\"(?: data-model-year=\"[^\"]*\")? class=\"[^\"]*\">([^<]*)/g, claim unchanged."
},
{
 "id": "DSGN_AMGTV1-Z-W23-S2",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~23",
 "surfaced_at": "2026-09-29T16:00Z",
 "one_line": "attrs.cjs arm 3 compares posture visible text to fixtures/attrs.visible.base.json, captured on DEV 4f927ad0 before AV-u-2; AV-u-2 (already on this slot's branch) changed the posture words, so arm 3 reads 'visible changed: [posture]' regardless of this cell.",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "attrs.cjs on ae1be3c8: arm 3 reason attrs 12 of 12 and no-call reason OK; only visible changed: [\"posture\"]",
   "printed NOW vs BASE posture text differ only in 'Citation not resolved -- ...' vs 'cite not resolved -- ...' and the footer '9 of the 18 citations can be shown on this page' vs '9 of 18 cite(s) resolved' (AV-u-2's words)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "AV-u-5 AC1 expects 3 of 3 arms with each surface's visible text unchanged against the base snapshot.",
 "world_is": "The snapshot lives in the issuer's read-only round6/fixtures and pre-dates AV-u-2. It needs regenerating (ATTRS_SNAPSHOT=1) after AV-u-2, or the posture key excluded. Not writable by this worker."
},
{
 "id": "DSGN_AMGTV1-Z-W23-S3",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~23",
 "surfaced_at": "2026-09-29T17:00Z",
 "one_line": "Resolves Z-W23-S1 and Z-W23-S2: the issuer's AMENDMENT 1 granted the harness and re-took the base snapshot; the harness re-anchor landed and all three AV-u-5 criteria now read green.",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_AMGTV1/task-orders/DSGN_AMGTV1.TO-AV-u-5.the-data-attributes-fwd30-needs.md@c521a0b494 AMENDMENT 1: modelPattern.harness.cjs granted in <paths>; round6/fixtures/attrs.visible.base.json re-taken on this slot's base",
   "portal wk-DSGN_AMGTV1-23-portal@ecaa197e: modelPattern.harness.cjs:155 cell regex '<td data-model-cell=\"true\" class=' -> '<td data-model-cell=\"[^\"]*\"(?: data-model-year=\"[^\"]*\")? class=' ; CHECKS-OK 12 of 12",
   "attrs.cjs -> FWD-30 ATTRIBUTES: 3 of 3 arms, exit=0; bound.cjs U5 -> U5 BOUND: 7 of 7 harnesses green, exit=0; vv-5.AC1.sh -> FWD-30 HARNESS READS THE REDESIGNED PAGE: YES, exit=0"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "Rows DSGN_AMGTV1-Z-W23-S1 (harness outside <paths>) and DSGN_AMGTV1-Z-W23-S2 (stale base snapshot) blocked AC2 and AC1 of AV-u-5.",
 "world_is": "Both were cut defects, ruled and fixed by the issuer's AMENDMENT 1; with the grant the re-anchor is made and every AV-u-5 criterion passes. Resolves Z-W23-S1 and Z-W23-S2."
},
  {
    "id": "DSGN_AMGTV1-Z-W28-S1",
    "project": "DSGN_AMGTV1",
    "fabric": "site-z",
    "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~28",
    "surfaced_at": "2026-09-29T20:30:00Z",
    "one_line": "The task order says the walker has a 'timeline walk' to extend; walk.mjs at HEAD has none -- AV-u-4's timeline/thread/lead-lists code was dropped by the 8b3f8e8833 merge resolution while SKILL.md still documents it. This worker built only the --day step, as a new function.",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~D -- decide whether AV-u-4's walker code (--thread, lead-lists.json, <sec>-timeline-day / <sec>-timeline-event, timeline:no-event-element) is re-landed; until then SKILL.md documents flags walk.mjs rejects as 'unknown argument'",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "git diff --stat e26e817087 HEAD -- .claude/skills/ui-walk/: walk.mjs 141 lines changed (44 insertions, 103 deletions); grep -i 'thread|lead-lists|timeline' on HEAD walk.mjs before this worker's edit: 0 lines",
        "8b3f8e8833 (merge, 0.0.0_AB_MSTR~Z) took walk.mjs 'per 1.0.0_SA_CTO~Z @c6ebc1a8c5', whose resolved file is 572 lines and lacks e26e817087's 91 added lines; SKILL.md line 72 still documents --thread and the timeline-day/-event steps",
        "walkday.cjs arm 2 needs a function containing [data-day-bar=\"${date}\"]; none existed, so walkTimelineDays was added and called after each --security overlay step"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "AV-s-3 item 4: 'In the timeline walk, for each named day of an opened --security' -- an existing timeline walk in walk.mjs is presumed.",
    "world_is": "walk.mjs at base d3770fe501 has no timeline step (AV-u-4's was lost in the merge). The worker added --day, walkTimelineDays and the timeline-days.json write only; it did not restore AV-u-4's code (a neighbouring defect, outside this cell)."
  },
{
 "id": "DSGN_AMGTV1-Z-S4",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-09-30T01:22Z",
 "one_line": "Resolves Z-W28-S1: the integrator merge 8b3f8e8833 resolved .claude/skills/ui-walk/walk.mjs to the origin side and dropped AV-v-2's pick step and AV-u-4's --thread, lead-lists.json and timeline steps; the issuer restored them by a three-way merge onto HEAD (keeping AV-s-3's --day and origin's --settle-extra-ms / --periods-per-account).",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "git show HEAD vs 8b3f8e8833^1 of walk.mjs before the fix: Chart-picked|data-series-ticker 0 vs 2; opt.thread|--thread|lead-lists 0 vs 5; timeline-day|no-event-element 0 vs 2 (the w-1 sign-in guard survived: 4 vs 4)",
   "git merge-file HEAD(+AV-s-3) / merge-base 5b69865bc7 / 8b3f8e8833^1: 9 conflict hunks, each a union of independent additions (opt initialiser merged; hunk 6 taken from the site-Z side, which carries the closing braces); walkTimelineDays placed after walkTimeline so each static check reads its own function",
   "after the fix: round5 pickstep.cjs 3 of 3; round6 walkthread.cjs 3 of 3; round7 walkday.cjs 3 of 3; round4 detect.mjs 6 of 6; round7 walkvoid.sh signed-out control YES; node --check rc=0"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "Row DSGN_AMGTV1-Z-W28-S1 (ARMED, disarm owner this seat): AV-s-3's face presumed a timeline walk that the integrator merge had dropped from walk.mjs.",
 "world_is": "Restored at HEAD by the issuer, every walker feature of rounds 4-7 present and every walker check green; the file-level cause (a conflict resolved to one side) is the integrator's merge, noted for 0.0.0_AB_MSTR~Z. Resolves Z-W28-S1."
},
{
 "id": "DSGN_AMGTV1-Z-S5",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-09-30T06:12Z",
 "one_line": "Three literal BACKSPACE bytes (0x08) where regexes meant \b: tabs/ModelTab.tsx:295 (AV-o-3, portal cb14d218) makes AZN's Model tab read \"Opal's opal's historical-multiple reference\"; components/HeaderBrief.tsx:48-49 (since 2515f456, round 1) means no description source ever reads \"Company description from Bloomberg\". tsc and all 16 harnesses pass them.",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "walk I tmp/ui-walk/20260930T055658Z shot 192 (AZN Model): \"Opal's opal's historical-multiple reference: quote currency 'GBp' ...\"",
   "byte scan of portal/src/pages/SecurityAnalysis at DEV 5810586a: 3 bytes below 0x20 other than tab/LF/CR, at HeaderBrief.tsx:48, :49 and ModelTab.tsx:295, each 0x08 inside /^...<0x08>/",
   "round10/checks/bytes.cjs at DEV 5810586a: 0 of 3; on a scratch copy with the three bytes replaced by \b: 3 of 3, cases.cjs 3 of 3, ALL 16 of 16 harnesses, tsc -b rc=0",
   "cases.cjs arm 2 passed the defect: it asks that each rule line START with Opal's, which \"Opal's opal's ...\" does -- a check blind spot, closed by bytes.cjs arm 2"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "AV-o-3 item 2: a served label that already starts \"Opal's\" is kept as served; AV-e-1 (round 1): a Bloomberg description source reads \"Company description from Bloomberg\".",
 "world_is": "Both regexes carry 0x08 instead of \b, so neither ever matches: the label is prefixed twice and the source never names Bloomberg. Ruled by the issuer: AV-o-3 AMENDMENT 1 re-opens that order to replace the three bytes and nothing else (a new order file in an issued round is refused by to-pipeline-gate LIMB 6)."
},
{
 "id": "DSGN_AMGTV1-Z-S6",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-09-30T06:35Z",
 "one_line": "Resolves Z-S5: AV-o-3 AMENDMENT 1 (worker ~37, portal d11747a7, drained CLOUD 4813813e75 / site-Z DEV 2bb60cc3) replaced the three 0x08 bytes with a backslash-b word boundary and nothing else.",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "round10/checks/bytes.cjs on the merged bytes: 3 of 3 (0 control bytes over 56 source files; AZN's rule label read once; a Bloomberg description source reads 'Company description from Bloomberg')",
   "portal diff d11747a7: 2 files, 3 lines; cases.cjs 3 of 3; Q3 bound 3 of 3 (two issuer re-runs); portal tsc -b rc=0",
   "1.0.0_SA_CTO~Z msg 26978: a census over all 991 portal src code files reads 0 files with 0x08 at 2bb60cc3 -- the class is gone portal-wide"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "Row DSGN_AMGTV1-Z-S5 (ARMED, disarm owner this seat): three literal backspace bytes broke two regexes on the page.",
 "world_is": "Repaired and drained; bytes.cjs stays in round 10's checks so a reintroduced control byte in the page's source fails a check, not only a walk. Resolves Z-S5."
},
{
 "id": "DSGN_AMGTV1-Z-W47-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~47",
 "surfaced_at": "2026-09-30T11:38Z",
 "one_line": "AV-m-4 AC2: portal/src/pages/SecurityAnalysis/__harness__/timelineFourStates.harness.cjs cannot load TimelinePanel.tsx once it imports ./publisherNames; the harness is outside <paths>.",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "bound.cjs Q3 at worktree wk-DSGN_AMGTV1-47: 'HARNESS RED timelineFourStates.harness.cjs :: rc=1', 3 of 4 green; shell 10/10, posture 32/32, tabs 20/20 green",
   "node timelineFourStates.harness.cjs: 'Error: Cannot find module ./publisherNames' raised from its own source() loader (lines 106-113), which resolves only STUBS, ../../../lib/dateUtils, ../../lib/dateUtils and ../dateWords, else falls to require()",
   "publishers.cjs 3 of 3, bytes.cjs 3 of 3, portal tsc -b rc=0 on the same bytes"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "The cut: with an import-free shared module 'the issuer's helper measured no harness change' and Q3 stays green; a bound harness may be re-anchored only if named in <paths>.",
 "world_is": "timelineFourStates.harness.cjs loads TimelinePanel through its own loader with no './publisherNames' branch, so the required import fails it (the issuer's own _load.cjs resolves it, which is why the helper read green). Fix needs one line in that harness (a './publisherNames' branch returning source('src/pages/SecurityAnalysis/components/publisherNames.ts')), which <paths> does not grant. Worker did not duplicate the map inside TimelinePanel.tsx to dodge it."
},
{
 "id": "DSGN_AMGTV1-Z-W47-S2",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~47",
 "surfaced_at": "2026-09-30T12:05Z",
 "one_line": "Resolves DSGN_AMGTV1-Z-W47-S1: AMENDMENT 1 granted the one loader line; timelineFourStates.harness.cjs now resolves ./publisherNames and Q3 reads 4 of 4 green.",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "timelineFourStates.harness.cjs load(name): added after the ../dateWords line -- if (name === './publisherNames') return source('src/pages/SecurityAnalysis/components/publisherNames.ts');",
   "bound.cjs Q3 after the line: 'HARNESS GREEN timelineFourStates.harness.cjs :: rc=0' ... 'Q3 BOUND: 4 of 4 harnesses green', exit=0; publishers.cjs 3 of 3 and bytes.cjs 3 of 3, exit=0"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "AMENDMENT 1 of AV-m-4 (issuer 2.0.0_SA_COO~D, on row DSGN_AMGTV1-Z-W47-S1): one harness line makes the bound harness load the shared module and Q3 green.",
 "world_is": "The one line landed exactly as granted and nothing else in the harness moved; the S1 blocker is cleared and AC2 reads 4 of 4."
},
{
 "id": "DSGN_AMGTV1-Z-W45-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~45",
 "surfaced_at": "2026-09-30T12:16Z",
 "one_line": "AV-m-1's cell says ui-smoke.mjs writes the per-state grades, but ui-smoke.mjs is a one-route screenshot tool; the six-state driver is ui-contract-check.mjs, so grades.json is written there.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal/scripts/ui-smoke.mjs @DEV 846ecc6c takes ONE <route> <outfile.png> per run and has no state loop; portal/scripts/ui-contract-check.mjs lines 60-72 and 379-409 own the six states (list, thesis, exec, peers, model, posture) and spawn ui-smoke.mjs and ui-measure.mjs per state",
   "round12/checks/rendercontrol.cjs:55 invokes `scripts/ui-contract-check.mjs --dist <dir> --out <dir>` and reads <out>/grades.json -- the check itself already names the driver, so no criterion is affected",
   "--dist was added to all three scripts as asked (ui-dist.mjs helper); rendercontrol.cjs 3 of 3 arms, exit=0"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "AV-m-1 item 2: `<out>/grades.json`, beside the PNGs and per-state JSON and the printed table, is written by the instrument ui-smoke.mjs (driven by ui-contract-check.mjs and ui-measure.mjs).",
 "world_is": "grades.json is written by ui-contract-check.mjs, the only script that runs all six states; ui-smoke.mjs and ui-measure.mjs gained --dist and (measure) the readings the grades are made of. The CTO's PRD wording 'ui-smoke.mjs ... writes, for each of the six states' names the instrument as a family."
},
{
 "id": "DSGN_AMGTV1-Z-W45-S2",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~45",
 "surfaced_at": "2026-09-30T12:16Z",
 "one_line": "The cell names tabPanelsWhite ('the tab panel is white with a hairline border') without saying where the panel is; I read it as the tab's painted wrapper, else its top-level painted surfaces, and DEV passes it in all five Security states.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "DEV 846ecc6c build, exec.png of the DEV run (C:/tmp/dsgn-r12-devrun-final/exec.png): the [data-tab-panel] div is transparent and sits INSIDE a white hairline panel that wraps it (Exec, Peers, Model); in Thesis and Posture the [data-tab-panel] div is transparent and its children are the white panels",
   "a first reading that looked only inside [data-tab-panel] graded Exec, Peers and Model FAIL on DEV (a false alarm: zebra table rows and skeleton bars read as non-white surfaces); the final reading is in ui-measure.mjs section 8 (tabPanels)",
   "final DEV run: tabPanelsWhite PASS in thesis, exec, peers, model, posture; pre-redesign build (8fa7abde): PASS in all five as well (the clause does not discriminate the two builds -- darkContainers does)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "AV-m-1 item 3: tabPanelsWhite: the tab panel is white with a hairline border (N/A in list).",
 "world_is": "Reading used: the tab panel's surface is the nearest painted ancestor below <main> (>300px wide, >=40px tall), else the top-level painted surfaces inside it (table rows and skeleton bars excluded); PASS iff at least one exists, every one is opaque white (255,255,255) and carries a light (luminance >= 0.4) 1px+ border. Zero surfaces grades FAIL, never PASS. A different reading is a change to ui-measure.mjs section 8 only. Separately: the issuer's clean page grades bandIsIdentityHeader FAIL (a static page carries no data-starred-toggle Lead Panel marker); AV-m-1's arm 2 asks only the eight style clauses, so nothing is affected."
},
{
 "id": "DSGN_AMGTV1-Z-W51-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~51",
 "surfaced_at": "2026-09-30T17:18Z",
 "one_line": "AV-l-6's fwd14 names a sentence's PASS face and its passage and accession line; on DEV a PASS sentence paints no face and the page never prints an accession, so I graded the attribute and the citation line in words.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal/src/pages/SecurityAnalysis/components/ThesisCards.tsx SentenceBlock (lines 276-280 at DEV ba62e945): the sentence carries data-verbatim-check and renders a CheckFaceBadge only when the verdict is not PASS; ThesisTab.tsx header comment: the face 'never' prints the accession number",
   "DEV run (C:/tmp/dsgn-r13-dist/dev, three windows opened): 17 sentences, 17 read data-verbatim-check=PASS with no badge; 18 citation lines [data-citation-document] name the document in words (10-K, filing date, section path)",
   "reading used in ui-contract-check.mjs gradeFwd14: the FACE is the data-verbatim-check attribute (a non-PASS verdict must also show its badge) and the ACCESSION LINE is the [data-citation-document] line; a page whose PASS sentences must paint a visible face would need that reading changed in gradeFwd14 only"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "AV-l-6 fwd14: in the Thesis windows each sentence shows its PASS face and passage count; opening it reveals the passage and accession line from the DOM.",
 "world_is": "DEV paints no visible face on a PASS sentence (attribute only) and prints no accession number (the citation line names the filing in words), so the clause as worded has no literal DOM referent; the reading above grades what the page actually renders."
}
]
```
