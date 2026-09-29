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
  }
]
```
