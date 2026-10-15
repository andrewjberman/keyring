# DSGN_RBNDV2: CVO L8/L9 at the round-2 close (2026-10-15)

<sweep_watermark>2026-10-15T10:50Z</sweep_watermark>

Author: `3.0.0_SA_CVO~L` (laptop), on `2.0.0_SA_COO~RB` msg 109389 (close run `deliverables/2.0.0_SA_COO~RB/ROUND2_CLOSE_RUN_20261015.md` @ecf90e2a30).

**Result: of 3 JUDGMENT criteria, 2 are MET (RB2I1-AC3, RB2M1-AC2) and 1 is NOT MET (RB2M4-AC3: the Fear & Greed trend chart's axis labels are white on silver).
W7-S1 and W9-S1 meet their disarm conditions. W8-S1, W8-S6, W8-S9 and W8-S11 GRADUATE ARMED to REMEDIATION_v2. W2-S3 stays ARMED in REMEDIATION_v1.
Fourteen INERT notes are dismissed.**

Instrument. This seat's own walk: `node .claude/skills/ui-walk/walk.mjs --route /market --press "Fear & Greed"` at 2026-10-15 ~10:48Z. The output is in
`tmp/ui-walk/20261015T104746Z` (gitignored), and the post-disarm login was REFUSED. The build on port 5174 serves the bytes of `ajb_wk/rbndv2-int` @826551e2: the
served FearGreedModal.tsx and the worktree file each carry 9 matches of the same class. `bun test dsgn-rbndv2` in that worktree: 22 tests across 22 files, every
VERDICT line OK.

```json
[
 {
  "id": "DSGN_RBNDV2-C-S7",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T10:55Z",
  "one_line": "L9 round 2: RB2I1-AC3 MET (hairline sections, no inset card, no coloured bar); RB2M1-AC2 MET (the frame is white with a silver edge and violet eyebrow underline, no shadow); RB2M4-AC3 NOT MET (the Fear & Greed trend chart's axis labels are white on silver and cannot be read).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "spec_asserts": "RB2I1-AC3: Trending Topics and Top/Bottom Performers read as hairline-divided sections with no bordered inset card and no coloured left bar. RB2M1-AC2: the modal frame reads as the A-light panel (white, silver edge, eyebrow title with the violet underline, hairline rules, no shadow). RB2M4-AC3: a market modal (RSI, Fear and Greed or Market Regime) reads as the A-light panel with its content legible.",
  "world_is": "RB2I1-AC3 MET. Both panels render their two columns as plain sections under small headings with a vertical hairline between them, and no inset border or left bar remains. This cures round 1's RB1P-AC3 clause. RB2M1-AC2 MET. In the opened Fear & Greed modal the frame's header and footer bands are white rgb(255,255,255), the edge is rgb(196,203,219) (#C4CBDB), and the eyebrow underline is violet rgb(95,59,227). The 16px outside the edge is uniform overlay rgb(144,149,168), so no shadow is cast. Hairlines sit under the header and above the footer, and the close control is a square at the top right. RB2M4-AC3 NOT MET. The modal reads as the light panel: the body sections are silver rgb(238,241,246), and the old dark ground is gone. The text, figures and component cards are legible. But the 90-day trend chart's y-axis (100/75/50/25/0) and x-axis dates are painted rgba(255,255,255,0.6) (FearGreedModal.tsx:406 and :424, and :890 for the history chart) on that silver ground, so they are effectively invisible in the render. That is content, not the signal-colour population Andrew set aside for FWD-5. RSIModal and the Market Regime modal were not opened by this walk or the COO's.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "tmp/ui-walk/20261015T104746Z/shots/001--market-load.png and 002--market-press-Fear-Greed.png (gitignored; this seat's walk); pixel samples as quoted",
    "ajb_wk/rbndv2-int @826551e2: src/components/market-performance/FearGreedModal.tsx:406, :424, :890 (tick fill rgba(255,255,255,0.6)); src/ui/components/modal/ModalFrame.tsx:113",
    "curl http://localhost:5174/src/components/market-performance/FearGreedModal.tsx -> 9 matches, equal to the worktree file",
    "bun test dsgn-rbndv2 (worktree rbndv2-int) -> 22 tests across 22 files, every VERDICT OK"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A grade, not a hazard. RB2M4-AC3's repair is a tick-colour token in the chart, for the round-3 list; RSIModal and Market Regime are still unwalked."
 },
 {
  "id": "DSGN_RBNDV2-C-S8",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T10:55Z",
  "one_line": "W7-S1 and W9-S1 meet their disarm conditions: the authored rb-1-r3 test prints SIDEBAR-TOKEN-FORMAT-OK, and both rb-1-p and rb-2-i1 print their VERDICT under the ruled section contract.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["DSGN_RBNDV2-W7-S1", "DSGN_RBNDV2-W9-S1"],
  "spec_asserts": "W7-S1: confirm at the drain that the authored file is the test the order meant. W9-S1: rule RB1P-AC1 arm (f), then the panels test runs green on the branch.",
  "world_is": "bun test dsgn-rbndv2 here prints SIDEBAR-TOKEN-FORMAT-OK, PANEL-LIGHT-OK and SECTIONS-OK among its 22 VERDICT lines. The sidebar underlines also render violet in this walk (the round-1 RB1S-AC3 defect), which is what the token-format test was meant to guard.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "bun test dsgn-rbndv2 in ajb_wk/rbndv2-int @826551e2 (2026-10-15 ~10:5xZ)",
    "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md rows W7-S1, W9-S1"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Each row's disarm condition is met as measured; recorded for its owner, 2.0.0_SA_COO~RB."
 },
 {
  "id": "DSGN_RBNDV2-C-S9",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T10:55Z",
  "one_line": "W8-S1, W8-S6, W8-S9 and W8-S11 GRADUATE ARMED to REMEDIATION_v2. W8-S9 is met for FearGreedModal's ground but not for RSIModal (unwalked), so the row stays ARMED. W2-S3 stays ARMED in REMEDIATION_v1 (the popup restyle is class text only).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["DSGN_RBNDV2-W8-S1", "DSGN_RBNDV2-W8-S6", "DSGN_RBNDV2-W8-S9", "DSGN_RBNDV2-W8-S11"],
  "spec_asserts": "A row graduates when its mechanism is attributed and its remedy holder named.",
  "world_is": "None of the four is met in a browser. W8-S9: FearGreedModal's content ground now renders silver, not dark navy, but RSIModal was not opened. W8-S6 (autoFocus lost to the frame) and W8-S11 (a hidden Close) are source-text only. W8-S1 is an instrument blind spot that no cell can disarm: the commit checks graded 0 of 3 .tsx files.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md rows W8-S1, W8-S6, W8-S9, W8-S11",
    "tmp/ui-walk/20261015T104746Z (this seat's walk)",
    "remediations/REMEDIATION_v2.md"
   ]
  },
  "disposition": "GRADUATED"
 },
 {
  "id": "DSGN_RBNDV2-C-S10",
  "project": "DSGN_RBNDV2",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO~L",
  "surfaced_at": "2026-10-15T10:55Z",
  "one_line": "Round 2 worker notes dismissed with reason: W7-S2, W8-S2, W8-S3 (BLOCKING, cured by the issuer's amendment of RB2M2-AC2), W8-S4, W8-S5, W8-S7, W8-S8, W8-S10, W8-S12, W8-S13, W8-S14, W8-S15.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": ["DSGN_RBNDV2-W7-S2", "DSGN_RBNDV2-W8-S2", "DSGN_RBNDV2-W8-S3", "DSGN_RBNDV2-W8-S4", "DSGN_RBNDV2-W8-S5", "DSGN_RBNDV2-W8-S7", "DSGN_RBNDV2-W8-S8", "DSGN_RBNDV2-W8-S10", "DSGN_RBNDV2-W8-S12", "DSGN_RBNDV2-W8-S13", "DSGN_RBNDV2-W8-S14", "DSGN_RBNDV2-W8-S15"],
  "spec_asserts": "Each order's text as written.",
  "world_is": "W8-S3 is cured: TO-RV-m-2:42-43 carries the amended bound, and its test prints ADOPTION-BOUND-OK here. The rest are build notes or disclosed behaviour changes. W8-S5 and W8-S7 change close behaviour (a backdrop click no longer closes during a submission; Escape now closes ExportModal mid-submission). W8-S12 is a double onClose on one Escape. W8-S14 is an invisible hover on the popup. W8-S8 is DrilldownModal's own overlay, on no list. W8-S10 means the modal family now carries two designs (HeroDialog and ModalFrame). All are INERT in this round; W8-S7, W8-S8, W8-S10 and W8-S12 are round-3 candidates.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D13/DSGN/DSGN_RBNDV2/surprise-channel/investigations/INVESTIGATION_v1.md",
    "org/missions/D13/DSGN/DSGN_RBNDV2/task-orders/DSGN_RBNDV2.TO-RV-m-2.trade-modals.md:42-43",
    "org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ROUND2_CLOSE_RUN_20261015.md @ecf90e2a30 sections 3-4"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Cured by amendment, or a build note and behaviour change named for the CTO's round-3 list."
 }
]
```

-- 3.0.0_SA_CVO~L
