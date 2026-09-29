# DSGN_AMGTV1 -- surprise channel, INVESTIGATION v1 (round 1, site Z). Append-only; rows below are minted by their own allocator (`.tools/surprise-row-gate.py` validates every NEW row).

```json
[
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
  }
]
```
