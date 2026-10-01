# DSGN_AMGTV1 -- ROUND 14 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-01 ~05:2xZ

**Input:** CVO slug msg 27537, `ADJUDICATION_v16.md` @8c81ecfc90 (7 of 7 terminal; AC4 5 MET, 2 PARTIAL; Z-S7 and Z-S8
graduate). Drain-end read @8a198b327b. PRD v0.6 ADMITTED (ratified-text signed bc4f634248). Shared CONTRACT
`org/tier1_exec/1.0.0_SA_CTO/deliverables/AMGT_FRIDAY_DEMO_20261001/CONTRACT.md` @b8c93f6342. Placement @e18d3a4e6a:
freeze Thu 18:00 ET, walk 18:00-21:00 ET, promote by 23:59 ET, PROD by Fri 09:00 ET.

## 1. WHAT THE ROUND DELIVERED

The round delivered served reasons as words, a designed ERROR state, a page-specific NO-PERMISSION, an empty state for
Peers, a settled Posture footer, sizes and radii, and a FWD-17 count a person can read. The close render passed 74 of 74,
and portal DEV is at a3f94ad3 and later. **Round 14 is CLOSED.**

## 2. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **k-5 PARTIAL is a round-15 cell.** On the Model face, the empty sentence and a printed figure must not both show. The face shows the figure with its label, or the empty sentence, never both. | It is on the demo thread (Model tab), so it is CORPUS's O5 territory rendered by DSGN. |
| 2 | **BA's pack absent/present split** (v16 section 2): DSGN maps each tab's sentence from the served reason. If the served reasons themselves disagree (Thesis "no research pack" vs Exec/Model presupposing one), that is a surprise row to `2.0.0_SA_COO~Z`, the writer, under CONTRACT section 0. It is never a page-side reconciliation. | One writer per surface; `C-PRESENTATION-ONLY`. |
| 3 | **k-1 PARTIAL** (Posture's served reason reads "ABSENT") is RESAPP's. This analysis routes it to `2.0.0_SA_COO~Z` as a round input under CONTRACT section 4. DSGN does not reword a served token. | The word reaches the page from the server. |
| 4 | **Round 14's polish of the list and line views is superseded** by v0.6 FWD-21/22 (those views are removed, R5). Nothing in round 15 maintains them. | Andrew: "No other views for chatter, no other views for price". |

## 3. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~D` cuts for round 15 in ONE issuance (fan-out cap 3)

Every cell is LOCAL on portal DEV. Each build order carries at most three mechanical criteria and builds against the
CONTRACT's shapes, with fixtures until RESAPP's routes land. **Shared-file serialization:** cells 1, 2 and 4 all touch
the Lead Panel files (`LeadPanel.tsx`, `RankedList.tsx`, `RankedChart.tsx`, `SecurityOverlay.tsx`). The COO derives the
chains from file overlap, so no two concurrent workers edit one file.

| # | cell | FWD | criteria shape |
|---|---|---|---|
| 1 | **Remove the List/Chart toggle, the list view and the line chart. Price becomes ranked horizontal bars** of `return_30d_pct`, longest first, sign by colour, reusing `RSIBars.tsx`. Trending only, with the Movement control absent. | 22, 18, 2 | the toggle and the line chart are absent from the render; bars render from the CONTRACT section 2 fixture in descending absolute order; values print as served (no x100) |
| 2 | **Chatter becomes one bubble per security**, sized by `collected` for the cursor's month, with a month cursor (this month, M-1, M-2, ...). Reuse `InflectionInsightsPanel.tsx:476-563` and `motion`. Caption "articles collected". | 21 | the bubbles render from the CONTRACT section 1 fixture; stepping the cursor changes the sizes; a partial month says so |
| 3 | **Lead Panel header and selected-name header in the /philosophy card family** (`PhilosophyPillars.tsx:183-214` card face, `chartColors.ts`, shared Segmented controls), with no visible "Lead Panel" label | 23 | no hard-coded colours in the Lead Panel files; no internal name on the face; the header cards use the shared card component |
| 4 | **The served-day header and labels:** the header renders `as_of`; "Breakout (price)" reads the breakout field; `places_moved` prints as served (`RankedList.tsx:265`); the empty state carries `absent_reason` | 24 | a fixture with T-1 `as_of` renders a populated header; no "not served" for a served field; the breakout label reads the breakout value |
| 5 | **k-5:** the Model face shows the figure or the empty sentence, never both. **BA pack split:** sentence mapping per ruling 2 | 15, 11 | BA's Model face carries no contradictory pair; Thesis/Exec/Model sentences derive from one served reason, or a row to COO~Z names the disagreeing fields |

**Wiring:** when RESAPP lands FWD-32 and FWD-35 on DEV, a wiring cell (the issuer's amendment, no CTO ruling)
swaps the fixture for the route, with no shape change.

**Judgment (L9):** for cells 1, 2, 3 and 5, the CVO reads the PNGs as a person: one design family with the rest of the
portal, nothing contradictory on the face. **Close walk:** CRO~Z `/ui-walk` 18:00-21:00 ET on the DEV build.

## 4. ACTS ONLY ANDREW CAN DO (cited)

1. **The PROD promote payload beyond Security Analysis** (CVO verdict 27503: his word names Security Analysis only).
2. **Recursive removal of the wk-dsgn-amgtv1-49..55 worktrees and the `C:/tmp/dsgn-r14-*` roots** (CLAUDE.md human
   confirmation for recursive deletion).
