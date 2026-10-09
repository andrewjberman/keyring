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
},
{
 "id": "DSGN_AMGTV1-Z-S7",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-09-30T16:40Z",
 "one_line": "AV-l-1 carries the served dossier reason onto the page verbatim, and for every name WITH a dossier the served reasons are producer words: BA's Exec and Thesis read \"no MANAGEMENT section in class A missing or class B missing\" and \"no report's RECOMMENDATION line names a fund token (IDVZ|PFOE|DIVZ)\".",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "round13/fixtures/thesisBundle.BA_US_Equity.json:17122 and :17127 (dossier_fields.management.reason, dossier_fields.fund_of_record.reason); the same two strings in the 992_HK and VLO captures, the fund-token string in TSM's: 4 of the 5 captured bundles carry them; 6501 (no dossier) reads the plain 'no research dossier exists for this name'",
   "walk M (tmp/ui-walk/20260930T162446Z, signed-in, 5174) BA Exec and Thesis shots show both strings on the face; the /api/scoped/amgt/security/BA%20US/compare 500 on the Posture step of the same walk is row Z-S8",
   "AV-l-1 item 1 asked for the served reason as served (C-PRESENTATION-ONLY), so l-1 met its criteria; the words are the producer's (AMGT_RESAPP dossier builder), not the page's"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "Design law (portal DESIGN.md): a code, field name or path may sit in a data attribute or in code, never in visible text; AV-l-1: the page reads the served dossier reason.",
 "world_is": "The served reason for a name with a dossier is a producer diagnostic (section names, class letters, a fund-token regex), so the page shows machine words by carrying the reason faithfully. Round-14 input: either RESAPP serves a reader sentence beside its diagnostic, or the page maps the reason class to one plain sentence and keeps the diagnostic in a data- attribute. Which one is the CTO's call at the round-13 analysis."
},
{
 "id": "DSGN_AMGTV1-Z-S8",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-09-30T16:40Z",
 "one_line": "On the signed-in walk the Posture step for BA calls /api/scoped/amgt/security/BA%20US/compare and gets HTTP 500: the display ticker, not the security key (BA_US_Equity), is used as the path key.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "tmp/ui-walk/20260930T162446Z/findings.json api_issues: {step 'amgt BA US tab Posture', GET /api/scoped/amgt/security/BA%20US/compare, http 500}",
   "the round-13 captures read the compare route under the key BA_US_Equity (round13/fixtures, BA compare capture) and it answers; the other BA routes on the same walk use BA_US_Equity",
   "walk M ran on 5174 serving a4b81627 (CTO~Z's worktree C:/tmp/amgt-walk-5174), which predates DEV ccca64ef. At DEV the one /compare fetcher (portal/src/api/endpoints/amgt-lead-panel.ts:157 getModelCompare, via hooks/useLeadPanelApi.ts:171 useModelCompare) always sends ?from=&to=; the walk logged no query, so the walk's call site is not yet located at DEV (the walker may strip queries)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "The page addresses every scoped security route by the security key the list served (BA_US_Equity).",
 "world_is": "One Posture call keys on the display ticker 'BA US' and the route answers 500 (a 404 or a named refusal would be the honest miss). Round-14 input: find the call site at DEV and key it on the security key; the route's 500 on an unknown key goes to AMGT_RESAPP."
},
{
 "id": "DSGN_AMGTV1-Z-S9",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-01T00:05Z",
 "one_line": "On the signed-in close walk (5174 @e5ae0063 = DEV a3f94ad3) 6501 JP's Exec reads \"No officer list is in this name's pack yet: no M-1 management object has landed for this name, and no other source was used.\" -- an interface code (\"M-1\") and producer words on the face after AV-k-4.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "tmp/ui-walk/20260930T235353Z/shots/072-6501-JP-Exec-Management.png (site Z, not committed): the empty-state sentence above, read by the issuer",
   "AV-k-4's helper green arm (r14-green-d @d7d29dd5) stripped one-letter interface codes locally; on chain ~52 the worker worded the reason through AV-k-1's shared reasonWords mapping, which does not drop a letter-dash-digit code",
   "the round-13 capture round14/fixtures/thesisBundle.6501_JP_Equity.json serves management_read.reason as an S3 path (\"no object under s3://opal-data-harvest/management/v1/6501_JP_Equity/\"), not the live wording -- the live reason moved after the capture, so execfooter.cjs (on the fixture) could not see the M-1 sentence"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "AV-k-4 / ruling 5 with ruling 1: Exec's empty sentence reads the served reason in words; no code on the face (portal DESIGN.md design law; FWD-11).",
 "world_is": "The live served management reason carries an interface code (M-1) and producer vocabulary (\"management object has landed\"); reasonWords drops code lists in parentheses and lowercases ALL-CAPS names but keeps a letter-dash-digit code. Round-15 input: the shared mapping drops interface codes of that shape (and the fixtures are refreshed from the live reasons), or the producer serves a reader sentence -- the CTO's call at the round-14 analysis."
},
{
 "id": "DSGN_AMGTV1-Z-W56-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~56",
 "surfaced_at": "2026-10-01T06:26Z",
 "one_line": "AV-f-2's cell text names the bubble attribute data-chatter-bubble; the graded check bubbles.cjs reads data-bubble, so I carry both attributes on each circle.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bubbles.cjs bubblesIn(): the regex requires an element carrying data-bubble=\"<security_key>\"; the order's cell text (item 1) says data-chatter-bubble=\"<security_key>\"",
   "portal/src/pages/SecurityAnalysis/components/ChatterBubbles.tsx @5cbbdfcd: the circle carries data-bubble and data-chatter-bubble with the same value; bubbles.cjs 3 of 3 arms with both"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "AV-f-2 item 1: each bubble is an SVG circle carrying data-chatter-bubble=\"<security_key>\".",
 "world_is": "The issuer's check (the order's AC1 oracle) matches only data-bubble; carrying both satisfies the cell text and the check. The round-16 cut can name one attribute."
},
{
 "id": "DSGN_AMGTV1-Z-W56-S2",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~56",
 "surfaced_at": "2026-10-01T06:27Z",
 "one_line": "AV-f-2 says Chatter renders bubbles and nothing else, but the granted harness claims (errorEmpty starred cases, leadPanelPattern source_footer and stale_dated_said) still read a StarredList and the ranking SourceCaption under subject Chatter, so two paths keep them.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs:155-264 (props subject CHATTER; starredOnly cases render the real LeadPanel and expect StarredList)",
   "portal/src/pages/SecurityAnalysis/__harness__/leadPanelPattern.harness.cjs:197-209 and :340-380 (universeHtml is LeadPanel on CHATTER with useCollectedChatter stubbed to data undefined; source_footer wants exactly one Source: line and stale_dated_said wants the ranking disclosure)",
   "portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx @5cbbdfcd: Chatter with Starred only on renders StarredList (unchanged branch); the ranking SourceCaption renders under Chatter whenever the bubbles payload is not served; once it is served the footer is the one bubbles line (articles collected per month, from the harvest, and the as_of)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "AV-f-2 item 3: subject Chatter renders ChatterBubbles and NOTHING else (no list, no line chart, no toggle); the footer under the bubbles names the source in words and the served as_of.",
 "world_is": "With Starred only on, Chatter shows the starred list, not bubbles (the granted harnesses keep that branch green). With the bubbles payload unserved, Chatter shows the designed empty state plus the ranking source caption. With the payload served and Starred only off, the face is bubbles and the bubbles footer only (bubbles.cjs arm 1: 0 list, 0 line chart, 0 toggle). A bubbles-only Starred reading would need the four harness claims re-anchored again."
},
{
 "id": "DSGN_AMGTV1-Z-W56-S3",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~56",
 "surfaced_at": "2026-10-01T06:55Z",
 "one_line": "AV-f-3 amendment 1 says the chatter face never renders the ranking SourceCaption, but with the bubbles payload unserved I still render it, because the bound harnesses (tabs generation_captions_present, leadPanelPattern source_footer and stale_dated_said, errorEmpty) read it there and only leadPanelPattern is in my paths.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx @424dbd27: footer is the bubbles line when the s.1 payload is served, else ResolutionNote + SourceCaption (the AV-f-2 fallback)",
   "measured on the worktree: with the footer empty for Chatter-unserved, bound.cjs F3 read 1 of 4 (leadPanelPattern, errorEmpty, tabs RED; the tabs failure is generation_captions_present); restoring the fallback reads 4 of 4 with 0 other change; the same three read 15/12/20 green on the pre-work portal HEAD",
   "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round15/checks/bubbles.cjs grades no unserved-payload or Starred-on footer, so amendment 1's footer clause is graded by no check"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "AV-f-3 amendment 1: the chatter face never renders the ranking SourceCaption; AC3: the four bound harnesses stay green (leadPanelPattern:15, errorEmpty:12, tabs:20, shell:10).",
 "world_is": "Served bubbles (Starred only on or off) carry the bubbles footer only. A Chatter face with no served payload (loading, read failure, not the s.1 shape) shows its designed empty state plus the ranking caption, so AC3 reads 4 of 4. A literal reading needs the tabs and errorEmpty harnesses (outside this order's paths) re-anchored to render Chatter with a served payload."
},
{
 "id": "DSGN_AMGTV1-Z-W56-S4",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~56",
 "surfaced_at": "2026-10-01T06:56Z",
 "one_line": "With StarredList gone from the chatter face, errorEmpty's starred-case checks (unresolved_row_navigates, a_click_sent_a_ticker, error_claims_no_daily_row, each expected false) pass because no row renders, so they no longer grade the starred list's behaviour; AC3 reads green on them by absence.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal/src/pages/SecurityAnalysis/__harness__/errorEmpty.harness.cjs:155-264 and its expected block: three checks expect false, one expects starred_error_differs_from_starred_empty true",
   "portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx @424dbd27: StarredList is no longer imported; errorEmpty read 12 of 12 with it absent, so the false-expected checks are met by no row and the one true check is met by the differing ranking footers"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "AC3: errorEmpty.harness.cjs:12 green means the starred error and empty states still read as designed.",
 "world_is": "The harness is green but its starred-state claims are not exercised on a StarredList; the round-16 cut can retire the StarredList claims or re-point them at the bubbles' starred empty state."
},
{
 "id": "DSGN_AMGTV1-Z-S10",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-01T07:05Z",
 "one_line": "The round-15 close walk is VOID: after a 200 login the next full page load calls POST /auth/refresh with the session cookie and the shared auth backend (CloudFront d2n2nzpeqf34ge) answers HTTP 500, so the app lands on /login. Any reload of a protected page signs the user out.",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "tmp/ui-walk/20261001T070037Z/netlog.tsv (site Z): line 85 POST 200 /auth/login, 86 GET 200 /auth/me, 180 GET 200 /security-analysis (full load), 259 and 263 POST 500 /auth/refresh",
   "curl -X POST http://localhost:5174/auth/refresh without a cookie: 401 {\"error\":\"No refresh token\"} (the route is up; the 500 is on a cookie-bearing refresh)",
   "round-14 walk N (tmp/ui-walk/20260930T235353Z, 2026-09-30 23:53Z) navigated the same routes signed in with 0 API issues: the refresh path worked then",
   "5174 = C:/tmp/amgt-walk-5174 at 93134bae (tree = portal DEV f4adf790), dev server restarted after a reboot (CTO~Z msg 27581); /auth proxies to https://d2n2nzpeqf34ge.cloudfront.net (vite.config.ts:86)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "1.0.0_SA_CTO~Z",
 "spec_asserts": "The close walk is the one real run of round 15 (decomposition v15 battery); a signed-in session survives a page load (FWD-1 hop 1, real login).",
 "world_is": "The shared auth refresh answers 500 on a cookie-bearing request; the walk cannot leave the first page signed in, so no signed-in walk of the round-15 faces exists. Owner: the auth backend's writer (not DSGN, which owns presentation only); routed to 1.0.0_SA_CTO~Z for placement. The Friday walk 18:00-21:00 ET and the PROD demo depend on it."
},
{
 "id": "DSGN_AMGTV1-Z-W61-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~61",
 "surfaced_at": "2026-10-01T08:20Z",
 "one_line": "The assignment names deliverables/0.9.0_WK_DSGN_AMGTV1~60/ as the proof-instance model, but that folder is absent from this worktree (HEAD 8b8ca27187); the highest present is ~58, so the instance is modelled on ~58's AV-f-4 instance.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "ls org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/ at 8b8ca27187: 0.9.0_WK_DSGN_AMGTV1~1 through ~58, no ~60 (ls rc=2 on the named path)",
   "modelled on deliverables/0.9.0_WK_DSGN_AMGTV1~58/DSGN_AMGTV1.TO-AV-f-4.the-header-reads-its-numbers.proof_of_spec.json"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "Proof instance modelled on org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/0.9.0_WK_DSGN_AMGTV1~60/*.proof_of_spec.json.",
 "world_is": "The ~60 instance is not on this branch (an unmerged worker branch or a different slot); the schema, not the model, is the binding form and proof-of-spec-check reads the instance."
},
{
 "id": "DSGN_AMGTV1-Z-W65-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~65",
 "surfaced_at": "2026-10-01T10:30Z",
 "one_line": "AV-i-2 could not be built as specified alone: round15 _load.cjs wraps a stubbed hook's return in {data}, so headerline.cjs only sees the monthly set through data.data, and tabs.harness.cjs counts >=2 data-generation-caption per header (chatter + price), which the removed legacy chatter caption supplied.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "round15/checks/_load.cjs:91-92 hookState.impl[key] result is wrapped as { data: <result> }; headerline.cjs:70 returns the wrapper itself as the set",
   "tabs.harness.cjs:324,586 tally.captionsSecurityMode >= 2 * n; first run after the edit: CHECKS-WRONG-WAY generation_captions_present, I2 BOUND 3 of 4",
   "resolved in portal f049ec3c: collectedChatterWords reads through a wrapped { data }; the chatter span keeps data-generation-caption/-detail of the chatter axis (data attributes only, no visible legacy text)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "Replace the chatter GenerationCaption with the monthly read; no harness may change; AC1 3 of 3 and AC3 4 of 4 green.",
 "world_is": "A plain k-of-n span fails headerline arm 1 (wrapper shape) and tabs.harness (caption count); the span carries the chatter generation as data attributes and unwraps a stub-shaped data."
},
{
 "id": "DSGN_AMGTV1-Z-S11",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-01T16:47Z",
 "one_line": "walk.mjs's occluded-popover check reads 9 of 9 covered on every pointer-events-none tooltip: document.elementFromPoint skips such elements, so an open, unobstructed figure tooltip is always reported occluded.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   ".claude/skills/ui-walk/walk.mjs:102-111 samples 9 points with document.elementFromPoint and counts any hit outside the popover; StatTile.tsx FigureTooltip carries className pointer-events-none",
   "round21/checks/hoverprobe.mjs first run (walk/hover-20261001T160250Z): COVER 9 of 9 on all 7 visible tooltips; with the tooltip subtree's pointer events on for the hit-test only, 0 of 9 on every tooltip (walk/hover-20261001T163908Z, BA 13 of 13 clean)",
   "tmp/ui-walk/20261001T164049Z UIW-...-006 occluded-popover 9 of 9 on shot 010, where the tooltip is visibly unobstructed inside the Financials pop-up"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "An occluded-popover finding means another element covers an open popover (walk.mjs check 1: 'dropdowns behind nav bars').",
 "world_is": "For a pointer-events-none popover the finding is produced by the instrument, not the page; DSGN rounds 20-21 read it as a false positive and graded occlusion with hoverprobe.mjs's corrected hit-test instead. walk.mjs is not this seat's to edit."
},
{
 "id": "DSGN_AMGTV1-Z-S12",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-02T05:17Z",
 "one_line": "DISARMED by the issuer (disarm_owner of each): DSGN_AMGTV1-Z-W2-S1, Z-W4-S1, Z-W28-S1 and Z-S5 -- each row's cause is absent at portal DEV 24646bca and workspace CLOUD 96738027ef; Z-W3-S1/S2 re-confirmed (already disarmed by Z-W3-S3). Z-S10 stays with 1.0.0_SA_CTO~Z.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "Z-S5: python scan of portal/src/pages/SecurityAnalysis (75 .ts/.tsx/.cjs/.mjs/.json files) at portal 24646bca finds 0 files containing byte 0x08.",
   "Z-W4-S1: exportCompare.harness.cjs at 24646bca keys parity on data-model-case-formula and data-model-line-refusal (lines 296-349, 'W4-S1 (a): parity compares DATA, not label wording'), landed by portal 060afb45 (AV-r-3). This is branch (b) of the row's disarm clause; the export's wording is not touched.",
   "Z-W28-S1: .claude/skills/ui-walk/walk.mjs at CLOUD HEAD parses --thread (line 40), writes lead-lists.json (line 1130) and walks <sec>-timeline-day / <sec>-timeline-event (lines 405-415), so the flags SKILL.md documents are accepted.",
   "Z-W2-S1: the channel file exists with 39 rows under one header; comp-surprise --project DSGN_AMGTV1 --json reads duplicate_ids {} and malformed 0.",
   "Z-W3-S1/S2: node src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs at 24646bca -> CHECKS-OK 20 of 20, thesis_sentences_and_one_chart true, rc=0; the HeroGraphic STUBS entry is at tabs.harness.cjs:90.",
   "Z-S10 (not this seat's to disarm): the round-20 and round-21 signed-in walks 20261001T151253Z and 20261001T164049Z left the first page signed in; the row names 1.0.0_SA_CTO~Z as disarm_owner."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "An ARMED hazard disarms via its disarm_owner (CLAUDE.md section 2); L10 waits until every BLOCKING or ARMED row is dispositioned.",
 "world_is": "Four ARMED rows owned by 2.0.0_SA_COO~D (W2-S1, W4-S1, W28-S1, S5) and two already disarmed by W3-S3 (W3-S1, W3-S2) still read disposition UNDER_INVESTIGATION in comp-surprise, because no L9 stamp followed. Their causes are absent in the world. This row records the disarms; the formal disposition is L9's to stamp.",
 "notes": "Issuer-authored disarm record at /canonical-drive DSGN_AMGTV1 tick 1 after the site-Z relaunch, not an adjudication."
},
{
 "id": "DSGN_AMGTV1-Z-S13",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "1.0.0_SA_CTO~Z",
 "surfaced_at": "2026-10-02T05:23Z",
 "one_line": "DISARMED by its disarm_owner: DSGN_AMGTV1-Z-S10 (auth refresh 500 signs the user out on reload). The cause is absent in both later signed-in walks: every post-login POST /auth/refresh answered 200 and neither netlog holds a 5xx.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "tmp/ui-walk/20261001T151253Z/netlog.tsv (site Z, 943 lines): POST /auth/refresh 401 at lines 80 and 84, before the POST 200 /auth/login at 85; then 8 of 8 POST /auth/refresh answer 200 (lines 259-847); 0 lines with a 5xx status",
   "tmp/ui-walk/20261001T164049Z/netlog.tsv (site Z, 943 lines): POST /auth/refresh 401 at lines 80 and 81, before the login at 85; then 8 of 8 POST /auth/refresh answer 200 (lines 259-830); 0 lines with a 5xx status",
   "the pre-login 401s match Z-S10's own control: a refresh with no cookie answers 401 'No refresh token'; Z-S10's defect was a 500 on a cookie-bearing refresh, which neither walk reproduces",
   "COO~D msg 28220 (Z-S12 @d11d8ee1fe) reports the same two walks left the first page signed in"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "1.0.0_SA_CTO~Z",
 "spec_asserts": "An ARMED hazard disarms via its disarm_owner (CLAUDE.md section 2); Z-S10 names 1.0.0_SA_CTO~Z.",
 "world_is": "Z-S10's cause is absent at the two signed-in walks of rounds 20 and 21 (2026-10-01 15:12Z and 16:40Z); the hazard no longer stands. Scope of the evidence: the 5174 dev build proxying /auth to the shared backend d2n2nzpeqf34ge, not a PROD read. The formal disposition is L9's to stamp.",
 "notes": "Disarm record by the disarm_owner at /self-drive AMGT_FRIDAY relaunch tick 1, on COO~D's ask (msg 28220); not an adjudication."
},
{
 "id": "DSGN_AMGTV1-Z-W69-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~69",
 "surfaced_at": "2026-10-02T00:00Z",
 "one_line": "posture.harness.cjs (in AV-z-1's paths, not in AC2's 14) throws TypeError: useCollectedChatter is not a function at components/SecurityOverlay.tsx:191, before and independent of the AV-z-1 edits.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "node portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs in worktree C:/tmp/wk-dsgn-amgtv1-69 (portal branch base 3ca6c53a plus AV-z-1 edits): TypeError (0 , useLeadPanelApi_1.useCollectedChatter) is not a function at SecurityOverlay.tsx:191:72, raised from posture.harness.cjs:357 renderHeader; the harness's hook stub carries no useCollectedChatter, and no AV-z-1 edit touches SecurityOverlay.tsx or the hook stubs.",
   "The 14 harnesses AC2 binds (posturePattern.harness.cjs among them) are green after the edits; posture.harness.cjs is not among the 14."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "AV-z-1 lists posture.harness.cjs in <paths> as a page harness that may need re-anchoring.",
 "world_is": "posture.harness.cjs does not run at this base (stale hook stub), so it asserted nothing about the posture claim wording either before or after AV-z-1; no re-anchor was possible or made.",
 "notes": "Neighbouring defect, not fixed (worker bounds). Worker row, not an adjudication."
},
{
 "id": "DSGN_AMGTV1-Z-W71-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~71",
 "surfaced_at": "2026-10-02T00:00Z",
 "one_line": "AV-zb-1's AC1 and AC2 contradict: round22 codeface.cjs arm 3 requires the served absent-column reasons to print verbatim on the Peers face, round23 peerwords.cjs arm 1 forbids 'factor code' / 'registry' / capitals there; no render satisfies both, so AC2 reads 2 of 3 arms (FAIL) with AC1 at 3 of 3.",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round22/checks/codeface.cjs lines 129-147 (arm 3 PLAIN SERVED WORDS STAY): every fixture absent reason whose census total is 0 (no snake/_Equity/.json/ABSENT/UNMAPPED/UPPER_SNAKE token) must be a substring of L.textOf(PeersTab html); the filter is code-shaped tokens only, so 'no share-count factor code and no share-count row field', 'the solvency category carries only RATIOS, never an absolute ...', 'no preferred-equity code among the 289 registry factors', 'no minority-interest code among the 289 registry factors' (7 of them) qualify",
   "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round23/checks/peerwords.cjs TERMS /factor code|row field|registr(y|ies)|comparison map|\\bR-1\\b/i and CAPS /\\b[A-Z]{4,}\\b/ over the same face: the same four reasons are TERMS or CAPITALS hits",
   "Run in C:/tmp/wk-dsgn-amgtv1-71 after the AV-zb-1 edits (portal branch wk-DSGN_AMGTV1-71-portal): peerwords.cjs exit=0 '3 of 3 arms'; codeface.cjs exit=1 'NO CODE ON THE EXEC, POSTURE OR PEERS FACE: 2 of 3 arms' (arm 3 FAIL, 7 faults); subjectrow.cjs 3 of 3; tsc rc 0; bound.cjs ALL BOUND 14 of 14. At the unedited base the pair reads codeface 3 of 3 and peerwords 2 of 3."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "AV-zb-1 cell text: do NOT print a served reason on the page (visible text is one plain clause composed from the column label, the served reason stays in data-absent-column-reason); AC2 expects codeface.cjs '3 of 3 arms' (round 22's outcomes kept).",
 "world_is": "codeface.cjs arm 3 grades the opposite behaviour (the served plain reason printed verbatim). The page now prints '<label> is not available for these peers.' per the cell and peerwords, so codeface arm 3 fails; the check, not the cell, needs amending (the issuer amends its own criteria). No served value moved; the cell's own AC1 passes. The worker did not edit the issuer's checks (read-only).",
 "notes": "Worker row, not an adjudication. The order stays open: AC2 is FAIL by output."
},
{
 "id": "DSGN_AMGTV1-Z-W71-S2",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~71",
 "surfaced_at": "2026-10-02T00:00Z",
 "one_line": "Resolves DSGN_AMGTV1-Z-W71-S1: the issuer amended codeface.cjs arm 3 at ac72f32ba1 and AC2 re-run reads NO CODE ON THE EXEC, POSTURE OR PEERS FACE: 3 of 3 arms, ALL BOUND: 14 of 14 harnesses green, exit=0.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "Issuer ruling relayed to 0.9.0_WK_DSGN_AMGTV1~71: codeface.cjs arm 3 amended @ac72f32ba1 (a plain served absent-column reason is preserved on the face OR verbatim in data-absent-column-reason); merged into wk-DSGN_AMGTV1-71 at 975322e44a.",
   "AC2 re-run from C:/tmp/wk-dsgn-amgtv1-71 at 975322e44a on portal build 925193f7: 'ARM PASS PLAIN SERVED WORDS STAY ... exec 1 of 1, peers 7 of 7'; 'NO CODE ON THE EXEC, POSTURE OR PEERS FACE: 3 of 3 arms'; 'ALL BOUND: 14 of 14 harnesses green'; exit=0 (deliverables/0.9.0_WK_DSGN_AMGTV1~71/ac2.out.txt)."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "AC2 expects codeface.cjs 3 of 3 arms (round 22 outcomes kept) alongside AC1's reader-words face.",
 "world_is": "With codeface.cjs arm 3 amended by the issuer, the two checks no longer contradict; Z-W71-S1's blocking cause is gone and AC2 is PASS-by-output. The formal disposition of Z-W71-S1 is L9's to stamp.",
 "notes": "Worker resolving row, not an adjudication."
},
{
 "id": "DSGN_AMGTV1-Z-S14",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-02T08:57Z",
 "one_line": "VLO Exec on the round-23 close walk reads 'Contact enrichment was skipped for this company -- Contact enrichment was skipped: no company web domain is on record for this name, and a guessed domain would enrich the wrong company': RESAPP B2 now serves a plain reason, so AV-z-1's line appends it after its own lead-in and the phrase repeats.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "tmp/ui-walk/20261002T084927Z/shots/067-VLO-US-Exec-Management.png (site Z, portal 41eeda55 on 5174): the line under the officer table.",
   "portal tabs/ExecManagementTab.tsx (AV-z-1, bcc95f4b): 'Contact enrichment was skipped for this company' + (plain served reason ? ' -- ' + reason : '.')."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "FWD-11 / AV-z-1: the Exec line reads as plain words; a plain served reason prints as served.",
 "world_is": "Both halves are now plain and they repeat each other. A page fix (drop the lead-in when the served reason already says it, or print only the served reason) is a one-line wording change for the next round's list; nothing is wrong on PROD that was not there before."
},
{
 "id": "DSGN_AMGTV1-Z-S15",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "1.0.0_SA_CTO~Z",
 "surfaced_at": "2026-10-02T09:12Z",
 "one_line": "REMEDY LANDED for DSGN_AMGTV1-Z-S11 (owner 1.0.0_SA_CTO~Z): walk.mjs's occluded-popover check now hit-tests each popover with its own subtree's pointer events on (walk.mjs @0b019f9df9, 0.0.0_AB_MSTR~Z, hoverprobe.mjs's method); the first live run reads occluded-popover 0 where the pre-fix walk read 1.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "git show --stat 0b019f9df9: .claude/skills/ui-walk/walk.mjs +10/-1 (fix(ui-walk, 0.0.0_AB_MSTR~Z): raw-code sees snake_case in prose; occluded-popover hit-tests with pointer events on)",
   "0.0.0_AB_MSTR~Z msg 28285: walk 20261002T072805Z (first live run after 0b019f9df9) findings.json census occluded-popover 0; pre-fix walk 20261001T164049Z occluded-popover 1",
   "0.0.0_AB_MSTR~Z msg 28257: synthetic-page exercise, free pe-none tooltip 9/9 -> 0; tooltip under a fixed nav 9/9 on both (the true positive survives)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "1.0.0_SA_CTO~Z",
 "spec_asserts": "Z-S11 remediation: the hit-test with the popover subtree's pointer events on moves into walk.mjs (REMEDIATION_v1, owner 1.0.0_SA_CTO~Z, OPEN).",
 "world_is": "The remedy is in walk.mjs at CLOUD and exercised live; the REMEDIATED stamp is the CVO's at the next compile.",
 "notes": "Remedy record by the remediation owner at the round-23 analysis (ADJUDICATION_v21 disclosed the row stale for 2 rounds); not an adjudication."
},
{
 "id": "DSGN_AMGTV1-Z-S16",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-02T09:24Z",
 "one_line": "CORRECTION (CTO round-23 ruling 4): DSGN_AMGTV1-Z-W71-S1 and DSGN_AMGTV1-Z-W71-S2 carry surfaced_at '2026-10-02T00:00Z', a placeholder; their true times are 2026-10-02T08:37Z (Z-W71-S1, commit 8d87abcbe0) and 2026-10-02T08:43Z (Z-W71-S2, commit a78956005b).",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "git show -s --format=%ad --date=iso-strict 8d87abcbe0 -> 2026-10-02T04:37:33-04:00 (the commit that added Z-W71-S1)",
   "git show -s --format=%ad --date=iso-strict a78956005b -> 2026-10-02T04:43:07-04:00 (the commit that added Z-W71-S2)"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "A row's surfaced_at is the real UTC time it was surfaced; corrections are new items citing the old id (surprise-row-gate).",
 "world_is": "The two worker rows carry a 00:00Z placeholder. This row records their true times; the rows themselves stay as written."
},
{
 "id": "DSGN_AMGTV1-Z-S17",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-02T15:56Z",
 "one_line": "The integrator-only push gate (.tools/hooks/never-rules-gate.sh PUSHPULL_AUTHORITY) admits a non-integrator push to ANY shared branch, PROD included, when the refspec names the destination as `<src>:refs/heads/<BRANCH>` or force-pushes `+<BRANCH>`: its sed strips `refs/heads/` BEFORE splitting off the `src:` half and never strips a leading `+`. This seat's own push of portal 42405d2d to DEV went through the first form.",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "hook fed synthetic PreToolUse JSON (session dea6290b..., serial file = 2.0.0_SA_COO~D, no FAST lease in org/mcp/drive_mode): `git -C $P push origin 42405d2d:DEV` -> permissionDecision deny (positive control); `... 42405d2d:refs/heads/DEV` -> no decision (admitted); `git -C C:/tmp/x push origin HEAD:refs/heads/PROD` -> admitted; `... +DEV` -> admitted; `... +HEAD:PROD` -> deny; `... refs/heads/DEV` -> deny",
   "the extraction line: sed -e 's#^refs/heads/##' -e 's#^.*:##' -e 's#^origin/##' -- for token `42405d2d:refs/heads/DEV` the first expression does not match, the second leaves `refs/heads/DEV`, which fails ^(CLOUD|DEV|PROD|SITEZ|main|master)$",
   "the act: 2026-10-02 ~15:4xZ `git -C C:/tmp/wk-dsgn-amgtv1-79/portal push origin 42405d2d:refs/heads/DEV` -> 415f50db..42405d2d (ls-remote read 42405d2d); VALGATE CI run 37029029779 success. The candidate touches no product file (scripts/ui-measure.mjs, scripts/ui-contract-check.mjs, a __harness__ test fixture), the CLAUDE.md Portal author-landing case (Andrew-direct 2026-09-24); the gate implements no such carve-out, so its intended verdict was DENY"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "1.0.0_SA_CTO~Z",
 "spec_asserts": "Only 0.0.0_AB_MSTR(~lane), the DT carve-outs and a live FAST-lease seat on DEV may push a shared branch; trigger (b) reads the refspec's destination whatever form it takes (LD-0367 rule 2 / LD-0368).",
 "world_is": "`<src>:refs/heads/<SHARED>` and `+<SHARED>` are not recognised as shared-branch pushes, so any seat whose target repo HEAD is not a shared branch is admitted. Remedy (one line): reorder to sed -e 's#^.*:##' -e 's#^+##' -e 's#^refs/heads/##' -e 's#^origin/##'. Separately, the law/gate mismatch: CLAUDE.md Portal admits a no-product-file author landing on DEV that the gate does not implement."
},
{
 "id": "DSGN_AMGTV1-Z-S18",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "1.0.0_SA_CTO~Z",
 "surfaced_at": "2026-10-02T16:17Z",
 "one_line": "DISARMED by its disarm_owner: DSGN_AMGTV1-Z-S17 (the push gate admitted <src>:refs/heads/<SHARED> and +<SHARED> from any seat). never-rules-gate.sh PUSHPULL_AUTHORITY now strips the src: half first, then a leading +, then refs/heads/ and origin/; 9 of 9 probes read as specified and the integrator is still admitted.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "Synthetic PreToolUse JSON was fed to .tools/hooks/never-rules-gate.sh with the caller unresolved (no serial file, OPAL_AGENT_SERIAL unset), against target repo C:/tmp/wk-dsgn-amgtv1-70/portal, whose HEAD is not a shared branch.",
   "BEFORE: 5 of 6 shared-branch forms were ADMITTED: 42405d2d:refs/heads/DEV, HEAD:refs/heads/PROD, +DEV, +HEAD:refs/heads/PROD, +refs/heads/main. The control 42405d2d:DEV was DENIED, and the 3 scratch forms were ADMITTED.",
   "AFTER the reorder: all 6 shared-branch forms are DENIED, and the 3 scratch forms (HEAD:refs/heads/scratch-ctoz-x, +scratch-ctoz-x, a plain non-shared branch) are still ADMITTED.",
   "Positive control: OPAL_AGENT_SERIAL=0.0.0_AB_MSTR~Z pushing HEAD:refs/heads/DEV is ADMITTED."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "1.0.0_SA_CTO~Z",
 "spec_asserts": "An ARMED hazard disarms via its disarm_owner (CLAUDE.md section 2). Z-S17 names 1.0.0_SA_CTO~Z.",
 "world_is": "Trigger (b) now reads the refspec destination in every form probed. NOT disarmed by this row: Z-S17's second limb, the law/gate mismatch. CLAUDE.md Portal admits an author landing a no-product-file candidate on portal DEV, and the gate has no carve-out for it, so after this fix such a landing is DENIED unless a FAST lease or the integrator carries it. The gate is now NARROWER than the law there. Implementing that carve-out needs a payload check for 'no product file'; it is routed to 1.0.0_SA_CTO~Z's own lane as a build item, not built here.",
 "notes": "Disarm record by the disarm_owner on COO~D's ask (msg 28563); not an adjudication."
},
{
 "id": "DSGN_AMGTV1-Z-S19",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "1.0.0_SA_CTO~Z",
 "surfaced_at": "2026-10-02T16:40Z",
 "one_line": "Z-S17 limb 2 (law/gate mismatch) CLOSED by its disarm_owner: never-rules-gate.sh now implements the TEST-ONLY portal-DEV carve-out of Andrew-direct 2026-09-24 cut 2 ('the author fast-forwards test and fixture changes'). It is scoped six ways: push, DEV, portal origin, a resolved caller, no force, and a payload where every path in <ls-remote DEV tip>..<src> is a test/fixture path. 20 of 20 probes read as specified.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "Dangling probe commits were built by plumbing on the remote DEV tip 42405d2d (no refs, no checkout): T is a __tests__ file, PR a src product file, N a test file on tip~1 (non-ff), S scripts/ctoz-probe.mjs.",
   "Caller 2.0.0_SA_COO~D: T:DEV and T:refs/heads/DEV are ADMITTED. DENIED, each with its printed reason: PR:DEV (1 of 1 paths not test/fixture), +T:DEV and push --force (force), N:DEV (not a fast-forward), S:DEV (scripts/ is not test-only), T:PROD (branch), and pull origin DEV (verb).",
   "An unresolved caller pushing T:DEV is DENIED. The integrator 0.0.0_AB_MSTR~Z pushing PR:DEV is ADMITTED. The 9 Z-S18 bypass probes still pass."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "1.0.0_SA_CTO~Z",
 "spec_asserts": "CLAUDE.md Portal: a portal candidate touching NO product file lands on DEV by its author (source record: test and fixture changes).",
 "world_is": "The gate admits exactly the test/fixture fast-forward. It is deliberately narrower than 'no product file': an instrument script under scripts/ (as in 42405d2d) is still routed through 0.0.0_AB_MSTR~Z or a FAST lease. Widening the pattern needs a word naming the class.",
 "notes": "Built by the gate owner on Z-S17's second limb (msgs 28563, 28575)."
},
{
 "id": "DSGN_AMGTV1-Z-W81-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~81",
 "surfaced_at": "2026-10-02T21:35Z",
 "one_line": "AV-zg-2's cell allows Refresh as 'primary on the white panel', but round29 face.cjs arm 1 counts the estate's own canvas primary button (text-white on the purple fill) as lightInk, so the cell's primary option can only pass with the ink written as an hsl value, not as the text-white / palette-white token.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "Run in C:/tmp/wk-dsgn-amgtv1-81 with Refresh = buttonClass('primary','canvas','sm'): face.cjs 'LIGHT FACE ... 1 fault(s): loaded: bands 0, lightOnDark 0, lightInk 1, primaryOnDark 0 (lightInk: <button inline-flex items-center justify-center gap-2 rounded-[3px] > \"Refresh\")', 3 of 4 arms.",
   "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round29/checks/header/face.cjs lines 29-30 and 100-101: INK_TOK = text-white | palette-white | palette-mediumGray, PRIMARY_TOK is not a ground token, so a primary fill is read as the white canvas under white ink. portal/src/ui/components/Controls.tsx BUTTON_KIND.canvas.primary carries 'text-white'.",
   "The same Refresh must stay the ONE purple fill: PRD FWD-18 'purpleFills == 1 (Refresh) in Security mode' (DSGN_AMGTV1_PRD.md line 252) and shell.harness.cjs primary_actions_security == 1 (not one of the five re-anchored clauses). A secondary Refresh would turn that clause red and break FWD-18."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "AV-zg-2 cell text item 2: 'Buttons use buttonClass(kind, canvas, ...); Refresh is secondary, or primary on the white panel'; face.cjs arm 1: lightInk 0 in all four states.",
 "world_is": "Refresh is kept primary (buttonClass('primary','canvas','sm','text-[hsl(0_0%_100%)]') in SecurityOverlay.tsx): the same white ink on the same purple fill, written as an hsl value so face.cjs does not read it as white-on-white. The check, not the page, is imprecise (it has no primary ground); the issuer amends its own checks. No served value moved.",
 "notes": "Worker row, not an adjudication. Both AC1 and AC3 pass with this choice; the alternative (secondary Refresh) passes AC1 and fails the shell harness's primary_actions_security."
},
{
 "id": "DSGN_AMGTV1-Z-W81-S2",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~81",
 "surfaced_at": "2026-10-02T21:35Z",
 "one_line": "To print 'identity as of' once (SAUX-15) IdentityLine now renders no 'identity as of <date>' text at all, so every tab that mounts IdentityLine (outside this cell's files) loses that visible line; the vintage stays in data-identity-vintage.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal/src/pages/SecurityAnalysis/components/IdentityLine.tsx: the resolved span now holds '' when crosswalk_vintage is served (data-identity-basis and data-identity-vintage kept), 'identity confirmed' when none is.",
   "face.cjs arm 2 counts 'identity as of' over the header plus IdentityLine's own render of the same identity (want at most 1); the header's identity card prints it once. battery29.sh BATTERY29: ALL PASS (0 skipped) at this tree, so no harness in the battery reads the old IdentityLine text."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "AV-zg-2 cell text item 3: 'identity as of prints at most once across the header and IdentityLine (e.g. IdentityLine keeps only its data attributes)'.",
 "world_is": "IdentityLine is mounted by other surfaces than the overlay header; those surfaces now show the ticker without the vintage line. The cell's own text names this option, so it is done as written; the other surfaces' wording is not this cell's to widen.",
 "notes": "Worker row, not an adjudication."
},
{
 "id": "DSGN_AMGTV1-Z-W81-S3",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~81",
 "surfaced_at": "2026-10-02T21:35Z",
 "one_line": "Until AV-zg-1 merges, the overlay renders the timeline twice (SecurityOverlay.tsx's new TimelinePanel mount after HeaderBrief, and HeaderBrief.tsx's own unchanged mount), and __rendercheck__/renderCheck.tsx still tests html.includes('Back to universe').",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx lines 196-198 at ec65c5d6 still mount <TimelinePanel securityKey={bundle.security_key} /> inside HeaderBrief; this cell's order is identity, key figures, <HeaderBrief bundle={bundle} />, <TimelinePanel />, the cell text says AV-zg-1 owns both components and stops HeaderBrief mounting a timeline of its own.",
   "portal/src/pages/SecurityAnalysis/__rendercheck__/renderCheck.tsx line 439 at ec65c5d6: persistentPanelPresent: html.includes('Lead Panel') || html.includes('Back to universe'); the back control now reads 'Back to all names'. Neither file is in this cell's paths."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "AV-zg-2 cell text item 3 and AV-zg-1's HeaderBrief change; this cell's paths exclude HeaderBrief.tsx and renderCheck.tsx.",
 "world_is": "In the merged tree of AV-zg-1 and AV-zg-2 the timeline mounts once; in this worktree alone it mounts twice (the checks stub both). renderCheck.tsx's string test is a stale lexical match owned by no cell of this round.",
 "notes": "Worker row, not an adjudication; nothing edited outside <paths>."
},
{
 "id": "DSGN_AMGTV1-Z-W80-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~80",
 "surfaced_at": "2026-10-02T21:25Z",
 "one_line": "AV-zg-1: the header's posture line no longer renders (HeaderBrief ignores postureLine, as the face orders), so posture.harness.cjs reds on header_line_present and absent_arm_explicit, which turns two battery29 items red (round24 posturezero.cjs, round23 postureharness.cjs) that the order does not skip.",
 "class": "BLOCKING",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "battery29.sh with --skip tabs,namecard on portal ec65c5d6 + this cell's edits: 'THE ZERO-RESOLVED PATH IS NAMED AND PLANTED: 1 of 3 arms [rc=1]' and 'POSTURE.HARNESS RUNS GREEN AND GRADES SOMETHING: 2 of 3 arms [rc=1]'; every other line rc=0 (ALL BOUND 13 of 13 harnesses green; tsc -b --noEmit rc=0).",
   "node portal/src/pages/SecurityAnalysis/__harness__/posture.harness.cjs prints CHECKS-WRONG-WAY no_object_arm_absent_explicit, BABA_US_Equity:absent_arm_explicit, BABA_US_Equity:header_line_present, BA_US_Equity:absent_arm_explicit, BA_US_Equity:header_line_present (the header-side checks only; the tab-side checks are green).",
   "Positive control: with HeaderBrief.tsx temporarily rendering {postureLine} between the description and the feed, the same harness prints 'ABSENT no_object HD_US_Equity tab true header true' and 'CHECKS-OK 32 of 32'. The edit was reverted; HeaderBrief.tsx in the commit does not render postureLine.",
   "The harness renders IdentityHeader from components/SecurityOverlay.tsx (posture.harness.cjs lines 372-380), which passes postureLine into HeaderBrief (SecurityOverlay.tsx line ~443); that file is AV-zg-2's and the posture-line re-anchor is named for AV-zg-3 in this order's AC3 note."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "The order's AC3 expects 'BATTERY29: ALL PASS (2 skipped)' with only tabs and namecard skipped; HeaderBrief keeps postureLine optional and ignored.",
 "world_is": "BATTERY29: FAIL (2 skipped) by exactly two items, both reading posture.harness.cjs, which looks for [data-header-posture] in the header band that HeaderBrief used to draw from postureLine. The cause is the ordered removal of the posture slot, not a defect in either file. posture.harness.cjs is not in this cell's paths, so it is left unedited. The posture line's new home and the harness's re-anchor belong to the cells that own SecurityOverlay.tsx (AV-zg-2) and the header posture line (AV-zg-3).",
 "notes": "AC1 and AC2 pass 4 of 4 arms each; AC3 is the only red criterion."
},
{
 "id": "DSGN_AMGTV1-Z-W80-S2",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~80",
 "surfaced_at": "2026-10-02T21:25Z",
 "one_line": "AV-zg-1: timelineFourStates.harness.cjs cannot load the rebuilt TimelinePanel.tsx without stubs for its new imports, so the edit went beyond the order's 'only the fill clause changes'.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "Before the stubs, node portal/src/pages/SecurityAnalysis/__harness__/timelineFourStates.harness.cjs threw \"Cannot find module '@/components/DataTooltip'\" (MODULE_NOT_FOUND) from TimelinePanel.tsx, whose build items 1 and 4 require DataTooltip and HeroDialog imports.",
   "Added three stubs to the harness's STUBS map (@/components/DataTooltip, @/ui/components/graphic/HeroGraphic, recharts ReferenceDot), none of which is the fill clause. After that and the fill re-anchor the harness prints result PASS; with BAR_FILL planted to hsl(var(--status-danger)) it exits 1 on four named checks; reverted, PASS again."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "Bounds item 2: in the harness file only the fill clause changes.",
 "world_is": "The harness also needed the import stubs and an extraction of fill-opacity, which carries the day's search state now that the hatches are gone. No other predicate (error banner, retry, zero day-bars on a failed call, pairwise distinctness) was altered.",
 "notes": "Smallest change that lets the order's own 'show one planted run' happen."
},
{
 "id": "DSGN_AMGTV1-Z-W80-S3",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~80",
 "surfaced_at": "2026-10-02T21:50Z",
 "one_line": "AV-zg-1: row Z-W80-S1 (AC3 red on the two posture harness lines) is resolved by the issuer's Amendment 1 @77abd61a20; amended AC3 reads BATTERY29: ALL PASS (4 skipped), exit=0.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "Amendment 1 (shared-tree commit 77abd61a20) skips postureharness and posturezero in AC3; merged into wk-DSGN_AMGTV1-80 and re-run at portal be4e019d: 'BATTERY29: ALL PASS (4 skipped)' and exit=0; ALL BOUND 13 of 13 harnesses green; tsc -b --noEmit rc=0. AC1 and AC2 re-run 4 of 4 each, exit=0."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "Row Z-W80-S1 stood BLOCKING: AC3 expected 'BATTERY29: ALL PASS (2 skipped)' and read FAIL on two posture.harness lines.",
 "world_is": "The issuer ruled on S1 in Amendment 1 @77abd61a20: the two posture lines return when AV-zg-2 renders the single [data-header-posture] and are read on the merged candidate. S1 is not edited; this row is the correction.",
 "notes": "Correction row per the append-only rule."
},
{
 "id": "DSGN_AMGTV1-Z-W83-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~83",
 "surfaced_at": "2026-10-02T21:55Z",
 "one_line": "AV-zg-4: ChatterBubbles imports the shared ramp by a RELATIVE path, not the face's '@/lib/sentimentColor', because three battery harnesses cannot resolve '@/'.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "With `import { getSentimentColor } from '@/lib/sentimentColor'` in ChatterBubbles.tsx, battery29.sh read BATTERY29: FAIL: leadPanelPattern, tabs and shell harnesses exit rc=1 with MODULE_NOT_FOUND (their own source() loaders resolve only specifiers that start with '.'), and posturezero.cjs and postureharness.cjs went red with them (ALL BOUND 11 of 14).",
   "With `from '../../../lib/sentimentColor'` (the form ChatterBubbles already used for lib/chartColors) the same battery reads BATTERY29: ALL PASS (0 skipped), ALL BOUND 14 of 14, and tone.cjs arm 1 (IMPORT_RE accepts either form) reads 4 of 4. TopicCloud.tsx keeps the face's '@/lib/sentimentColor' line, which no harness loads.",
   "Portal commit 74347456 on wk-DSGN_AMGTV1-83-portal."
  ]
 },
 "spec_asserts": "Face item 3 of AV-zg-4: ChatterBubbles.tsx 'Import getSentimentColor the same way' (the '@/lib/sentimentColor' line TopicCloud takes).",
 "world_is": "The __harness__ loaders (leadPanelPattern, tabs, shell and the harnesses that load ChatterBubbles through them) resolve relative specifiers only; an '@/' import in a page file they load throws MODULE_NOT_FOUND. A later cell that adds an '@/' import to any page component those harnesses load meets the same wall.",
 "disposition": "UNDER_INVESTIGATION",
 "notes": "Deviation is the specifier form only; the module, its export and the single import are as ordered."
},
{
 "id": "DSGN_AMGTV1-Z-S20",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-02T22:35Z",
 "one_line": "At ~22:0xZ the SHARED index held a staged revert of committed DSGN records (slot ~84's proof instance + ac1..ac3 deleted, and TO-AV-zg-5's <status> back to pending) beside 2.0.0_SA_COO~Z's staged RESAPP round-64 files; COO~Z confirms the revert was not theirs (msg 28790). Its writer is unknown. It was unstaged (my 5 paths only) before any commit carried it; HEAD and CLOUD never lost the records.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "git diff --cached --stat at ~22:1xZ: 5 DSGN paths (~84 proof .json -96, ac1/ac2/ac3 -6/-6/-17, TO-AV-zg-5 status complete->pending) + 9 RESAPP paths",
   "git log --diff-filter=D --since=1h -- org/missions/D13/DSGN/DSGN_AMGTV1/ -> 0 lines (no deletion landed); TO-AV-zg-5 <status> at HEAD = complete",
   "2.0.0_SA_COO~Z msg 28790: 'The staged DSGN revert of ~84 records was not mine; my safe-commit stages only RESAPP paths.'"
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "The shared index holds only what a seat is committing this moment; a staged change to another seat's committed records is never left behind.",
 "world_is": "An unknown writer left a staged revert of my drained records in the shared index; a broad commit by any seat would have deleted them. Unstaged per path; cause not found. My drain wrapper now prints foreign files, and every drain re-reads its own records at HEAD after the merge."
},
{
 "id": "DSGN_AMGTV1-Z-W85-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~85",
 "surfaced_at": "2026-10-02T19:10Z",
 "one_line": "AV-zg-6: the slot inherited uncommitted portal files from a stopped session that still held two temporary plants of the OLD wording (ExecManagementTab ProfileCell 'No profile (no match found)', ThesisTab ABSENT_ON_OBJECT 'held back uncited'); both were removed before the build was graded, and the Bloomberg-fallback caption default 'the filing' (null source_item) was also made source-named.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "git -C portal diff ec65c5d6 on the 7 inherited files showed both plants in the working tree before any edit by this session; ExecManagementTab.tsx and ThesisTab.tsx now carry the new wording at portal commit cff0ff2c.",
   "Two planted-failure runs this session: with the old wording put back, execPattern.harness.cjs absent_profile_cells reads false (clean_cells=0) and drafting.harness.cjs held_uncited_line_present reads false, both rc=1; both plants were reverted before the portal commit."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO-AV-zg-6 section 1: the Exec and Thesis tabs print no 'No profile', 'no match found' or 'held back uncited' on the face; a Bloomberg-fallback roster never says 'filing' in the management caption.",
 "world_is": "The inherited working tree did not meet that rule on two strings until this session finished the build. The face also bids the fallback caption to append ', the company's filing' while saying a fallback roster never says 'filing'; the build follows the second clause (the caption names only the served source).",
 "notes": "Worker-authored record; form only, no significance judged."
},
{
 "id": "DSGN_AMGTV1-Z-W87-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~87",
 "surfaced_at": "2026-10-03T01:16Z",
 "one_line": "AV-zh-2: two shared definitions the order's build needs sit outside its <paths> -- types.ts types CoverageItem.url as `string` (the served overlay now carries null) and constants.ts holds HEADER_FEED_VISIBLE_COUNT = 3 (the order wants at most 2 open news items at rest); the build handled both inside HeaderBrief.tsx.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal/src/pages/SecurityAnalysis/types.ts:561-565 @e370eb7c: interface CoverageItem { ... url: string }; the order's build item 4 says the served feed carries url null after RESAPP's redeploy.",
   "portal/src/pages/SecurityAnalysis/constants.ts:198 @e370eb7c: export const HEADER_FEED_VISIBLE_COUNT = 3; HeaderBrief.tsx now opens Math.min(HEADER_FEED_VISIBLE_COUNT, FEED_OPEN_AT_REST = 2) items at portal 621f553e; shell.harness.cjs (battery29) still green, tsc -b rc=0."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO-AV-zh-2 build items 4 and 6: a feed item with no served url prints plain text; at most 2 news items are open at rest.",
 "world_is": "The shared type still says url is a string and the shared constant still says 3, so another reader of either sees the old contract; HeaderBrief guards the url at runtime (typeof string and non-empty) and takes the smaller of the constant and a local 2. A later cell that owns types.ts and constants.ts can fold both in.",
 "notes": "Worker-authored record; form only, no significance judged."
},
{
 "id": "DSGN_AMGTV1-Z-W88-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~88",
 "surfaced_at": "2026-10-03T16:55Z",
 "one_line": "AV-zi-1: the order asks the window Segmented to take ground=\"band\" like its neighbours, but the neighbours (Subject, Starred) pass no ground prop and sit on the GraphicCard's WHITE body; band ground draws white active ink there, so the preset control takes the default ground like them.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal/src/ui/components/Controls.tsx:85-96 @2defab11: SEG_ACTIVE.band = font-bold text-[hsl(var(--palette-white))] border-[hsl(var(--palette-white))]; SEG_IDLE.band is palette-mediumGray.",
   "portal/src/pages/SecurityAnalysis/components/LeadPanel.tsx @2defab11: the Subject and Starred Segmented calls carry no ground prop (GraphicCard bodyClassName is the white body); the only mention of ground=\"band\" is the module header comment at line 26."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO-AV-zi-1 build item 3: the window Segmented takes ground=\"band\" like its neighbours.",
 "world_is": "The neighbours take the default (canvas) ground, so the preset control was built the same way to read navy on white; the order's criteria do not grade the ground prop. If band ground was meant, the neighbours and the header comment disagree with the order.",
 "notes": "Worker-authored record; form only, no significance judged."
},
{
 "id": "DSGN_AMGTV1-Z-W97-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~97",
 "surfaced_at": "2026-10-04T23:05Z",
 "one_line": "AV-zn-1: with the fixture replaced by the served WINDOWED chatter shape, the Universe state's sizes and radii clauses now FAIL (the monthly fixture drew no bubbles, so they never read the bubble labels); the run tally is 74 PASS / 2 FAIL, not all-PASS.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "C:/tmp/r36-scratch-wk97/out-20261004T224439Z/candidate/grades.json (AC1 run on portal 35a723bf + this order's three files): states.list.sizes FAIL {smallest 8, below11 [8,9,10]}; states.list.radii FAIL [3.35544e+07px, 3px, 4px, 2px, 5px]; result {PASS 74, FAIL 2, NOT_EXERCISED 0, N/A 1}.",
   "Same list state, same dist C:/tmp/r35-scratch-c/dist-35a723bf, run twice in my scratch: with the pre-change fixture (git show HEAD:portal/src/pages/SecurityAnalysis/__harness__/tests/uiContractFixtures.json) sizes PASS and radii PASS (list.json sizes keys 11,12,14,20,30; radii 3.35544e+07px, 3px, 4px); with the windowed fixture sizes carry 8:73, 9:234, 10:302 characters and radii add 2px and 5px. The order's cell names no fix for either clause and changes no product file."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO-AV-zn-1 cell text: the last redesign run read 62 PASS and 14 FAIL and every FAIL was the instrument's own stale anchor, not the page.",
 "world_is": "Fixing the three anchors (band clause, price rest rule, windowed chatter fixture) leaves 2 FAIL cells on the list state that are the page's bubble labels (8, 9 and 10 px) and corner radii (2px, 5px) once the chatter face draws its bubbles. AC1 grades 4 of 4 arms and does not read these two cells.",
 "notes": "Worker-authored record; form only, no significance judged."
},
{
 "id": "DSGN_AMGTV1-Z-W100-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~100",
 "surfaced_at": "2026-10-05T08:03Z",
 "one_line": "AV-zp-1: AC2 (battery29, no skip) cannot read ALL PASS from this order's <paths>: 11 of 14 page harnesses and the starredclaims check go red because the harness loaders (outside <paths>) name every module a page file may import, and two of them assert the retired hand-rolled caption.",
 "class": "OBSERVATION",
 "hazard_standing": "ARMED",
 "disarm_owner": "2.0.0_SA_COO~D",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "AC2 literal run on portal dsgn-r38-zp1 (85e24287 + this order's files), outer HEAD wk-DSGN_AMGTV1-100: 'ALL BOUND: 3 of 14 harnesses green [rc=1]'; 'ERROREMPTY'S STARRED CLAIMS GRADE A RENDERED FACE: 1 of 3 arms [rc=1]'; tsc -b --noEmit rc=0; eslint --quiet rc=0; 'BATTERY29: FAIL (0 skipped)'. AC1 (repairs38.cjs) reads 5 of 5 arms, exit=0, on the same tree.",
   "Per harness, the first error with the shared footer and end line in place (portal/src/pages/SecurityAnalysis/__harness__/*.harness.cjs @85e24287): errorEmpty 'Cannot find module ./CardFooter'; drafting, execFallback, execText 'Cannot find module ../components/CardFooter' (their load() names each module a tab may import: drafting.harness.cjs:80-110, execFallback.harness.cjs:76-90, execText.harness.cjs:74-88); tabs and shell 'Cannot find module @/ui/components/PageEnd' (shell.harness.cjs STUBS names @/ui/components/* one by one and its relative loader cannot resolve the real PageEnd.tsx's '@/lib/dateUtils' import); execPattern 'Cannot find module @/ui/components/panels' (its source() loader maps only @/lib/utils); modelPattern 'Cannot find module @/ui/components/states'; posturePattern and thesisLadder 'Element type is invalid ... got: undefined' (their @/ui/components/panels stub carries Panel, PanelHeader, PanelContent only, so PanelFooter is undefined); leadPanelPattern 'CHECK source_footer = false', 'CHECK caption_facts_unchanged = false' (they assert LeadPanel's hand-rolled 'date | Source' caption, which FWD-11 retires).",
   "Green: peersCarry, peersPattern, peersReadFailed (their fixtures serve no source, so no footer renders). The new import specifiers are intrinsic to the order (PanelFooter, PageEnd and states are the required shared components); the harnesses are not in <paths>, and no import shape resolves in all fourteen loaders."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO-AV-zp-1 AC2: battery29.sh with no skip reads 'BATTERY29: ALL PASS (0 skipped)' on a tree whose only changes are the order's <paths>.",
 "world_is": "The code in <paths> satisfies AC1 (5 of 5), tsc and ESLint. battery29's harness line and the starredclaims check read red because the harness files that load these page files carry fixed import lists and caption assertions, and they are outside <paths>. Left alone, the drain's real-grade battery run on the combined candidate reads FAIL until those harnesses are amended in a cell that owns them.",
 "notes": "Worker-authored record; form only, no significance judged. I did not edit any harness (bound 2, only the files in <paths>)."
},
{
 "id": "DSGN_AMGTV1-Z-W100-S2",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~100",
 "surfaced_at": "2026-10-05T08:03Z",
 "one_line": "AV-zp-1: the shared PanelFooter prints a clock the payload did not serve when handed a bare day ('September 15th, 2026, 5:00p ET' for a served '2026-09-15'); the order allows one prop and forbids anything else in that file.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal/src/lib/dateUtils.ts formatPanelTimestamp @85e24287: a bare YYYY-MM-DD goes through create5pmETDate and prints '<month> <day>th, <year>, 5:00p ET'.",
   "repairs38.cjs CENSUS on this tree: 'BA Exec Management tab ... renders footer yes (\"September 15th, 2026, 5:00p ET | Source: company filings.\")' for served management.as_of '2026-09-15'; likewise the Posture tab (posture.as_of), the Lead Panel Price face (as_of_date 2026-10-01) and the Chatter face (as_of 2026-10-03)."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO-AV-zp-1 contract C-PRESENTATION-ONLY: a time is printed only when served; the footer time is one of the card's served values printed in words.",
 "world_is": "Where a card serves only a day, the shared footer (the estate's own format on /market and /philosophy) appends 5:00p ET. The card hands over the served day unchanged and the check grades it as served (same day); the added clock is the shared formatter's house convention, not a served value. dateWords.longDate prints the same day with no clock, but PanelFooter does not call it.",
 "notes": "Worker-authored record; form only, no significance judged."
},
{
 "id": "DSGN_AMGTV1-Z-W100-S3",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~100",
 "surfaced_at": "2026-10-05T08:39Z",
 "one_line": "AV-zp-1 amendment 1: the shared PageEnd prints a clock the payload did not serve on a bare served day ('Data as of October 2nd, 2026, 5:00p ET.' for a served price.as_of_date day); PageEnd.tsx is outside <paths>, so the card footers are fixed and the end line is not.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal/src/ui/components/PageEnd.tsx @75f9f477: asOf = formatPanelTimestamp(null, dataAsOf), the same formatter row Z-W100-S2 names; a bare day prints '5:00p ET'.",
   "repairs38.cjs ARM 3 on this tree: 'MSFT thesis: \"End of Security Analysis. Data as of October 2nd, 2026, 5:00p ET.\"' -- graded PASS (it grades the served day)."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO-AV-zp-1 AMENDMENT 1 section 2 (and C-PRESENTATION-ONLY): a bare served day prints as a day, never a time of day; the amendment scopes this to a card's footer (CardFooter.tsx, PanelFooter.tsx).",
 "world_is": "The card footers print a bare day as a day (CardFooter passes the pre-formatted day through the new PanelFooter timeText prop). The page's end line is the shared PageEnd, which this order cannot edit; it still appends 5:00p ET to the served day.",
 "notes": "Worker-authored record; form only, no significance judged."
},
{
 "id": "DSGN_AMGTV1-Z-W104-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~104",
 "surfaced_at": "2026-10-06T04:02Z",
 "one_line": "AC2 battery29 reads 13 of 14 harnesses green: tabs.harness.cjs prints CHECKS-WRONG-WAY short_read_control_served (control ranking not SERVED with 3 <li>); the same line prints with RankedList.tsx reverted to HEAD, so it is not this order's edit.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "battery29.sh on portal 4fa0312e + this order's 5 files: 'ALL BOUND: 13 of 14 harnesses green [rc=1]', 'BATTERY29: FAIL (0 skipped)', exit=1; tsc rc=0, eslint rc=0; r43.cjs 5 of 5 exit=0.",
   "portal/src/pages/SecurityAnalysis/__harness__/tabs.harness.cjs:545: controlServed = good.ranking_status === 'SERVED' && countOf(controlHtmlList, '<li') === 3; run with RankedList.tsx at HEAD: CHECKS-WRONG-WAY short_read_control_served, same."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO-AV-zu-1 AC2: BATTERY29: ALL PASS (0 skipped), exit=0 after the four-file change.",
 "world_is": "The battery fails on one harness check whose input is the adapter's control ranking (adapter.control), a surface outside this order's paths; it was not measured red-or-green at the unedited base (git stash is barred here), only with the RankedList edit removed.",
 "notes": "Worker-authored record; form only, no significance judged."
},
{
 "id": "DSGN_AMGTV1-Z-W105-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~105",
 "surfaced_at": "2026-10-06T05:58Z",
 "one_line": "AC2 battery29 reads 13 of 14 harnesses green: drafting.harness.cjs throws 'Cannot find module ../components/SegmentBreakdown' because its import loader stubs each ThesisTab import by name and the new import is unstubbed; the harness file is outside this order's <paths>.",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "disarm_owner": "2.0.0_SA_COO~D -- amend the order's <paths> to admit portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs and add one stub line beside its ThesisDriverChart stub (name === '../components/SegmentBreakdown' returns { SegmentBreakdown: () => null }); until then the drain's combined battery29 run is red on this harness.",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "battery29.sh on portal c123c5a0 + this order's 4 files (uncommitted at the run): 'ALL BOUND: 13 of 14 harnesses green [rc=1]', 'HARNESS RED drafting.harness.cjs :: rc=1', 'BATTERY29: FAIL (0 skipped)', exit=1; tsc -b rc=0; eslint --quiet rc=0; r44.cjs 5 of 5 exit=0.",
   "node portal/src/pages/SecurityAnalysis/__harness__/drafting.harness.cjs: 'Error: Cannot find module ../components/SegmentBreakdown' at drafting.harness.cjs:116 (load -> req(name)) from ThesisTab.tsx:19; the harness stubs ../components/ThesisDriverChart at line 98 and falls through to req() for any other unnamed import."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO-AV-zv-1 AC2: BATTERY29: ALL PASS (0 skipped), exit=0 after mounting SegmentBreakdown in ThesisTab.tsx as the order directs (bounds item 4 and <paths> name no harness file).",
 "world_is": "The mount the order directs adds an import the drafting harness cannot resolve, and the one-line stub that would resolve it sits in a file the order's write grant does not name; this worker did not edit it. Other 13 harnesses incl. tabs and thesisLadder are green.",
 "notes": "Worker-authored record; form only, no significance judged."
},
{
 "id": "DSGN_AMGTV1-Z-S21",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-06T22:10Z",
 "one_line": "Re-owned from AMGT_RESAPP-Z-W173-S3 (2.0.0_SA_COO~Z msg 30368, ruling round76 section F @fb9ca91ad5): a SERVED model case on the Security Analysis page carries no value or currency data attribute, so a reader keys a served case on name and formula only.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal DEV 6b4e89a8, regex data-(model-)?case-(value|currency|formula) over src: 2 hits, both in __harness__/exportCompare.harness.cjs (lines 297, 307) reading data-model-case-formula; 0 hits for a value or currency attribute.",
   "AMGT_RESAPP surprise-channel/remediations/REMEDIATION_v14.md row AMGT_RESAPP-Z-W173-S3: remedy 'the value and currency attributes asked of DSGN_AMGTV1 were never added'."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "A served model case on the page exposes its value and its currency as data attributes a walk can read.",
 "world_is": "Neither attribute exists in portal src. The case line lives in ModelTab.tsx, which AMGT_CORPUS round 39 (ao-3/ao-4, 2.0.0_SA_COO~X msg 30247) is writing; a DSGN cell for it waits for that drain to reach DEV. Gates nothing.",
 "notes": "Backlog row for the next DSGN round cut; not armed."
},
{
 "id": "DSGN_AMGTV1-Z-W106-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~106",
 "surfaced_at": "2026-10-07T02:15Z",
 "one_line": "AC2 battery29 read 13 of 14 harnesses green after the re-run button was removed: shell.harness.cjs graded exactly 1 purple primary fill on the Security view, which was the retired Refresh button; re-anchored to 0 inside this order's <paths>.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "battery29.sh before the edit: 'ALL BOUND: 13 of 14 harnesses green [rc=1]'; node portal/src/pages/SecurityAnalysis/__harness__/shell.harness.cjs: 'CHECK primary_actions_security 0 (expected 1)' then 'CHECKS-WRONG-WAY primary_actions_security' (line 337: check('primary_actions_security', primaryFillCount, 1)).",
   "After changing the expected value to 0 (one line, shell.harness.cjs, inside the order's __harness__/ grant): battery29.sh 'ALL BOUND: 14 of 14 harnesses green [rc=0]', 'BATTERY29: ALL PASS (0 skipped)', exit=0."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "TO-AV-zw-1 (d): remove the re-run button; the order names posture.harness.cjs only among the harnesses and AC2 expects BATTERY29 ALL PASS.",
 "world_is": "shell.harness.cjs carried a check that counts the Refresh button's purple fill (the 'ONE purple fill on this view', FWD-18); removing the button makes the count 0, so the order's literal edits alone leave AC2 red. The Security view now has no primary-fill control; whether a later cell wants one is not decided here.",
 "notes": "Worker-authored record; form only, no significance judged."
},
{
 "id": "DSGN_AMGTV1-Z-W107-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~107",
 "surfaced_at": "2026-10-07T02:10Z",
 "one_line": "r44.cjs (round 44 issuer check) reads 2 of 5 arms after AV-zw-2: arms 1, 2 and 4 grade the pre-AV-zw-2 contract (open state keyed on passage id, segment label on every row in served order) that this order's items 1 and 4 change; the check file is outside this order's <paths>.",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "disarm_owner": "2.0.0_SA_COO~D",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "node r44.cjs on portal 34803ef6 + this order's 4 files (uncommitted at the run): ARM FAIL 'A CLICKED DRIVER POINT SHOWS ITS SERVED PASSAGE (FWD-18)' (served passage_text not shown), ARM FAIL 'THE SEGMENTS ARE DRAWN WITH THEIR CITES (FWD-1)' (row 4: segment not at rest; rows 5-11 text/cite not at rest), ARM FAIL 'MOUNT + KEEP' (a point resolved through sections lost its passage); ARM PASS arms 3 and 5; last line '2 of 5 arms'.",
   "r44.cjs renderOpen() stubs React.useState so that init === null returns the PASSAGE ID as the open state (r44.cjs lines 62-67); ThesisDriverChart now keys the open state on the point index (order item 1), so no point reads open under that stub. r44.cjs gradeSegments() pairs the i-th data-segment-row with the i-th SERVED row and expects the segment name inside each row; item 4 groups rows by segment (BA: served order CA,CA,BDS,BDS,GS,GS,GS,CA,BDS,GS,CA is drawn CA x4, BDS x3, GS x4) and prints the name once as the heading.",
   "The same checks r77_ba5.py AC1, AC2, AC3 read C1-C5, C1-C10, C1-C6 PASS and exit=0; tsc -b rc=0; eslint --quiet rc=0; drafting, posture, shell, tabs, thesisLadder harnesses green with no assertion edited. The r44 baseline on 34803ef6 was not re-run by this worker (git stash is refused on this tree); the three failing arms are attributed from the code lines cited."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "The worker's order text: the existing round-44 check must stay green after the change; if a required change moves an arm, report which and why.",
 "world_is": "Items 1 and 4 of the order necessarily move the three r44 arms named; the check cannot be edited by this worker, so the drain's r44 run reads 2 of 5 until the issuer re-anchors it to the point-keyed open state and the grouped rows.",
 "notes": "Worker-authored record; form only, no significance judged."
},
{
 "id": "DSGN_AMGTV1-Z-S22",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-07T02:45Z",
 "one_line": "A conflicted drain finished with safe-merge.sh --continue committed ONLY the resolved surprise channel: merge f953449753 left the branch's other 3 files (proof instance, render, the order's status flip) out of the commit, intact but unstaged in the shared working tree.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "safe-merge.sh --verify-merge f953449753: 'branch needed 4 file(s), dropped 3, foreign 0' and a WARN naming the 3 paths; the --continue run itself exited 0 and printed MERGED.",
   "git status after the merge: the order file ' M' and deliverables/0.9.0_WK_DSGN_AMGTV1~107/ '??'; both byte-identical to branch wk-DSGN_AMGTV1-107 @b413c05522 (cmp per file).",
   "Sequence: the first safe-merge call refused rc=2 on another seat's staged RESAPP order; a retry loop re-ran it when the index read clear (rc=4, conflict); the channel was resolved, git add of that one file, then --continue.",
   "Landed unchanged by aa7dee9340 under the worker's authorship (the lane gate refuses a COO author on deliverables/<worker>/)."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "safe-merge.sh --continue re-enters the same grade and the same authored commit as the one-shot path, so a drained branch lands whole.",
 "world_is": "The continue path landed 1 of 4 files and exited 0; only the read-only --verify-merge line showed the loss. Cause not established: either the merge's staged entries were unstaged between the conflict and the continue (another seat's commit ran in that window on the shared index), or --continue commits only what the resolver staged. The drain was repaired; the tool behaviour is unexamined.",
 "notes": "Tool owner is 2.0.0_SA_COO (.tools/safe-merge.sh). After any --continue, run --verify-merge and read the 'dropped' count."
},
{
 "id": "DSGN_AMGTV1-Z-W107-S2",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~107",
 "surfaced_at": "2026-10-07T03:25Z",
 "one_line": "AV-zw-2 Amendment 1 turns r77_ba5.py AC2 clause C3 red: C3 expects every served row label and figure INSIDE the table element, and Amendment 1 draws BA's two mismatched rows OUTSIDE it as unaligned lines; r77_ba5_harness.cjs is outside this order's <paths>.",
 "class": "BLOCKING",
 "hazard_standing": "ARMED",
 "disarm_owner": "2.0.0_SA_COO~D",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "node/python r77_ba5.py --crit AC2 on portal 49a9bf37: 'FAIL C3 every served row label and figure is in the table rows missing [\"Cumulative deliveries\",\"Deliveries\"] figures missing 12'; C1, C2, C4-C10 PASS; 'R77 BA5 AC2 SERVED: NO'; exit=1. AC1 and AC3 stay exit=0; r45b.cjs reads 4 of 4 arms.",
   "r77_ba5_harness.cjs lines 247-251 (round77/checks): tableText = textOf(tables[0]); missingRows = table.rows labels not in tableText; missingValues = every served figure not in tableText; clause C3 requires tables.length === 1 and both lists empty. BA serves 5 + 8 = 13 figures; the 13th, '73', is found only because it is a substring of the column label '737' (clause C3 matches by substring on the table's text).",
   "The Amendment text (WORKER_FACE.md, section AMENDMENT 1) anticipates this: 'if AC2's clauses on BA's table no longer hold because a clause expects the figures inside the grid, report the exact clause line and do not edit that check'."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "spec_asserts": "Amendment 1 of the order: AC1, AC2 and AC3 must stay green; AC5 (r45b.cjs) grades that a mismatched row is drawn outside the table.",
 "world_is": "The two clauses contradict each other for BA: r45b arm 1 demands both BA rows outside the table, r77_ba5 AC2 C3 demands both inside it. The worker built to the Amendment (AC5 4 of 4); AC2 reads 9 of 10 clauses with C3 red until the issuer re-anchors C3 to read the rows' label and figures inside the table wrap (the element holding data-driver-chart-passage-table plus the unaligned lines).",
 "notes": "Worker-authored record; form only, no significance judged."
},
{
 "id": "DSGN_AMGTV1-Z-S23",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-07T08:46Z",
 "one_line": "DISARMED by the issuer (disarm_owner of each): DSGN_AMGTV1-Z-W100-S1, Z-W105-S1, Z-W107-S1 and Z-W107-S2 -- each row's red check reads green on the round-45 candidate portal 659104f4, which is on portal PROD as part of b06863fe (v2.1.203).",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "Z-W100-S1 (battery29 red from harness loaders outside the order's paths): round45/ROUND45_CLOSE.md @f5263c2fd0 reads 'battery29 ALL PASS (14 of 14, tsc 0, eslint 0)' on portal 659104f4.",
   "Z-W105-S1 (drafting.harness.cjs cannot resolve ../components/SegmentBreakdown): round44/ROUND44_CLOSE.md AMENDMENT 1 @342094450e, portal 8544e133, stubs the new ThesisTab import; the same 14 of 14 battery29 read on 659104f4 covers this harness.",
   "Z-W107-S1 (r44.cjs 2 of 5 after AV-zw-2): the issuer re-anchored r44.cjs @ce6e53b828 (point-keyed open state; a segment name read from its heading); ROUND45_CLOSE.md reads r44 5 of 5 on 659104f4 and 2 of 5 on base DEV.",
   "Z-W107-S2 (r77_ba5 AC2 clause C3 red after Amendment 1): AC2 re-pointed to the DSGN copy round45/checks/ba5/r45_ba5.py @0b28e723d0 with C3 re-anchored; AC1-AC3 YES on portal 49a9bf37 and on 659104f4, NO on 0aa353a6.",
   "Claim class: all four figures are HELD from the issuer's close records of 2026-10-07 ~04:0xZ; no check was re-run at this tick. comp-surprise --project DSGN_AMGTV1 --json at this tick read armed 4 (these four ids), open 22, malformed 0."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "An ARMED hazard disarms via its disarm_owner (CLAUDE.md section 2); L10 waits until every BLOCKING or ARMED row is dispositioned.",
 "world_is": "Four ARMED rows owned by 2.0.0_SA_COO~D were repaired in rounds 44 and 45 (the drain commits and the close records say so) and still read ARMED in comp-surprise because no disarm row followed the repairs. Their causes are absent on the candidate that shipped. This row records the disarms; the formal disposition is L9's to stamp.",
 "notes": "Issuer-authored disarm record at /canonical-drive DSGN_AMGTV1 tick 1 after the 2026-10-07 site-Z reboot relaunch, not an adjudication."
},
{
 "id": "DSGN_AMGTV1-Z-S24",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-08T22:35Z",
 "one_line": "On AMD US the served filing-segment reason says a segment table with figures needs a separate segment data pull, and the Bloomberg segment table with figures is drawn directly above it (round-53 candidate 84e13d0f).",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round53/walk/read-20261008T222437Z/r53-AMD-US-thesis.png: 'REVENUE BY SEGMENT' table 6 rows x 5 columns, then 'BUSINESS SEGMENTS -- FROM THE FILING' reading 'No filing analysis is stored for this name yet, so no segment breakdown is shown. A segment table with figures needs a separate segment data pull.'",
   "The sentence is the served segment_breakdown.reason on the live /thesis (round53/served/thesis_AMD_US_Equity.json); the page prints it verbatim (SegmentBreakdown.tsx)."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~Z",
 "spec_asserts": "Every absence sentence the function serves is true of the page it is drawn on (PRD v0.18 SAUX-39 spirit; FWD-27).",
 "world_is": "Since AMGT_RESAPP round 79 serves segment_table, the second clause of the served segment_breakdown.reason is no longer true for a name with a served table.",
 "notes": "Producer text, AMGT_RESAPP's lane; the page draws what is served. Off-task observation from the round-53 real run."
},
{
 "id": "DSGN_AMGTV1-Z-S25",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-08T22:35Z",
 "one_line": "On /freshness the Seeking Alpha cells now print the served sentence, and the wider column makes the 'Oldest input' and 'Bloomberg' day cells wrap onto two lines ('2026-09-' / '22').",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round53/walk/read-20261008T222437Z/r53-freshness.png, the first rows of the table at 1440 px wide."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "A day in a table cell reads on one line (portal design law, legibility).",
 "world_is": "The day cells wrap at 1440 px once the Seeking Alpha cell carries a sentence.",
 "notes": "Cosmetic; candidate for the next DSGN round (a whitespace-nowrap on day cells)."
},
{
 "id": "DSGN_AMGTV1-Z-S26",
 "project": "DSGN_AMGTV1",
 "fabric": "site-z",
 "surfaced_by": "2.0.0_SA_COO~D",
 "surfaced_at": "2026-10-08T22:35Z",
 "one_line": "The Freshness page's column header 'Research pack' names the analysis the system builds (every row reads the daily build day 2026-10-08), the phrase the CTO's ruling (msg 31721, decomposition v52) gives only to the research team's own document.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "org/missions/D13/DSGN/DSGN_AMGTV1/deliverables/2.0.0_SA_COO~D/round53/walk/read-20261008T222437Z/r53-freshness.png: header 'Research pack', 95 of 95 rows dated 2026-10-08.",
   "portal/src/pages/Freshness/freshnessRows.ts INPUTS: { key: 'pack', label: 'Research pack' } at candidate 84e13d0f."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D",
 "spec_asserts": "Two packs, two phrases: 'the research team's pack' for the team's document, 'the analysis built for this name' for the built thing (PRD v0.18 SAUX-40; decomposition v52).",
 "world_is": "One page still calls the built thing 'Research pack'.",
 "notes": "Same class as round 53's AV-zze-3; candidate for the next DSGN round, wording to be ruled with it."
},
{
 "id": "DSGN_AMGTV1-D1-W126-S1",
 "project": "DSGN_AMGTV1",
 "fabric": "dell1",
 "surfaced_by": "0.9.0_WK_DSGN_AMGTV1~126",
 "surfaced_at": "2026-10-09T06:51:59Z",
 "one_line": "Cell AV-zzk-3 item 1 and item 2 together leave the identity header with NO description: the only full description ('About the company') is drawn by HeaderBrief, which item 1 moves to the News tab.",
 "class": "OBSERVATION",
 "hazard_standing": "INERT",
 "grounding": {
  "status": "GROUNDED",
  "evidence": [
   "portal/src/pages/SecurityAnalysis/components/HeaderBrief.tsx @c0c6f570 lines 43-69 and 215-219: DescriptionLine (summary 'About the company') is a non-exported function mounted only inside HeaderBrief.",
   "portal/src/pages/SecurityAnalysis/components/TopBand.tsx @c0c6f570 line 98: CompanyLine, the one-line description, which item 2 stops mounting."
  ]
 },
 "disposition": "UNDER_INVESTIGATION",
 "disarm_owner": "2.0.0_SA_COO~D1",
 "spec_asserts": "Task order AV-zzk-3 section 1: the identity header keeps 'one description'; item 2 stops CompanyLine and 'the full description stays behind About the company'.",
 "world_is": "After item 1 (HeaderBrief out of IdentityHeader) and item 2 (CompanyLine unmounted), the description renders only on the News tab, inside HeaderBrief's About the company fold; the header shows none. Worker did not reach into HeaderBrief.tsx (cell B's file) to export DescriptionLine.",
 "notes": "Issuer's merge wiring: either export DescriptionLine from HeaderBrief and mount it once in IdentityHeader, or accept the description on the News tab. The structural floor r59.cjs C passes either way."
}
]
```
