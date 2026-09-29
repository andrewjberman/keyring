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
  }
]
```
