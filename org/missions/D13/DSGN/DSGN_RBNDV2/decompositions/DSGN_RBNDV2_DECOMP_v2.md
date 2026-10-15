# DSGN_RBNDV2 -- DECOMPOSITION (L5) -- ROUND 2, THE ENRICHMENT (PRD v0.1)

```json
{
 "project": "DSGN_RBNDV2",
 "directive": "D13",
 "macro": "DSGN",
 "fabric": "laptop",
 "decomp_version": "v2",
 "step": 5,
 "prd_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/prd/DSGN_RBNDV2_PRD.md@e71a48e4b0 (v0.1, RATIFIED; both halves signed)",
 "round_analysis_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/ledger/ROUND_ANALYSIS.round1.md@eea2fc50c2 (1.0.0_SA_CTO; CTO msg 109371)",
 "author": "2.0.0_SA_COO~RB",
 "round": 2,
 "rectangle": "the CTO's round-1 enrichment list: (1) the --rb-accent token fix (served by direct act RV-r-3, proof by a computed-style read), (2) the two inset-card panels, (3) C-MODAL: the shared frame and every modal's adoption; item 4 (FWD-4 heat maps) waits on Andrew's design call and a PRD addendum",
 "cells": 7,
 "chains": 2,
 "join_cells": 0,
 "portal_base": "feature/dsgn-rbndv2-light (local, no upstream, never pushed); every worker worktree branches from it",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~RB`. **Input:** the CTO's round-1 analysis (the three NOT MET grades `RB1S-AC3`, `RB1P-AC3`, `RB1H-AC3` and the process rows), the surprise rows
`DSGN_RBNDV2-W2-S3` (the account-menu popup), `W3-S1` (panel number) and the PRD's round arc ("round 2: C-MODAL across every modal"). Round 1 is spent: six orders complete and merged
into the local feature branch, three more direct acts and the CVO's L9 grades recorded. **Frozen at the cut.**

**Rulings reaching every cell:** PRD CONTRACTS C-BRANCH (one branch, no push), C-MODAL, C-PANEL; DEC-1 to DEC-5. TOKEN FORMATS (the cause of round 1's sidebar defect): `--rb-*` are HEX, read as `var(--rb-X)`;
`--bg-surface`, `--bg-page`, `--hairline`, `--semantic-*` are HSL triples, read as `hsl(var(--X))`. Workers get the worker face only (CTO, W6-S2), and every order carries `<round>2</round>`.

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

Denominator: the CTO's four enrichment items. (1) the accent token fix: PLACED as the direct act `RV-r-3` (cut at ~07:5xZ before the analysis landed, order `DSGN_RBNDV2.TO-RV-r-3.sidebar-token-format.md`, round-less by design);
its computed-style proof is the COO's close walk reading the current link's `border-bottom-color` equal to `rgb(95, 59, 227)`, recorded in the round-2 close record. (2) the inset cards: PLACED as `RV-i-1`. (3) C-MODAL: PLACED as `RV-m-1` (the frame)
and `RV-m-2` to `RV-m-6` (the adoption of every overlay file the census found). (4) FWD-4: HELD, no cell, by the CTO's own condition (Andrew's design call, then the PRD addendum). Remainder after subtraction: item 4 only, held with its reason.

**The modal census (measured, denominator printed).** A native Grep of `role="dialog"`, `aria-modal`, `fixed inset-0`, `catalyst/dialog`, `<Dialog`, `createPortal` over non-test `portal/src` at the feature branch @adc70061 returned 42 files.
Of the 42, 9 are excluded as infrastructure or not an overlay of their own: the four catalyst files (`dialog`, `alert`, `stacked-layout`, `sidebar-layout`), `Tooltip`, `LoadingSpinner`, `HeroGraphic`, one `.cjs` harness, and
`ExecutiveSummary.tsx` (it hosts the triggers of the market modals and is edited by no cell). The other 33 are placed below, and `src/App.tsx`, which holds the account-menu popup (row `W2-S3`) and was not in the 42, is placed too:
`RV-m-2` 4 files, `RV-m-3` 9, `RV-m-4` 5, `RV-m-5` 7, `RV-m-6` 9 including `App.tsx`; 4 + 9 + 5 + 7 + 9 = 34 = 33 census files + `App.tsx`; 42 - 9 excluded = 33. The census is a name-and-pattern search and is NOT exhaustive:
every adoption cell looks in its own directories for another overlay and names it in a surprise row, and the adoption list that results is the deliverable.

## 2. THE INTERFACE (declared so every adopter builds against one API)

`ModalFrame` at `portal/src/ui/components/modal/ModalFrame.tsx`, built by `RV-m-1`, props `open`, `onClose`, `title`, `size` (`sm|md|lg|xl`), `footer`, `closeOnBackdrop`, `className`, `children`; renders inline (no portal); the dialog surface carries
`data-panel-surface="light"` so the round-1 ink rule and the inner-surface token remap apply inside every modal. The adopters consume it and so form ONE CHAIN with it.

## 3. THE CELLS -- 7 (round 2)

Paths portal-relative; `RV-m-*` are one queue for one worker, `RV-i-1` is the other chain.

| cell | what it builds | serves | writes | reads (never writes) | risk | class |
|---|---|---|---|---|---|---|
| `RV-i-1` | the inset cards become hairline sections, AT THE PRIMITIVES: `NestedCard` renders a section (no box, no fill, no left bar), `PanelGrid` draws the hairlines between sections; no page file | FWD-3 | `src/ui/components/panels/NestedCard.tsx`, `PanelGrid.tsx`, `src/ui/components/panels/__tests__/dsgn-rbndv2/` | `src/components/market-performance/ExecutiveSummary.tsx` | LOCAL | worker-light |
| `RV-m-1` | the shared modal frame `ModalFrame` and its README | FWD-3 | `src/ui/components/modal/` | `src/ui/components/catalyst/dialog.tsx` | LOCAL | worker |
| `RV-m-2` | the 4 TradeSubmission modals adopt the frame | FWD-3 | `src/pages/TradeSubmission/components/{TradeDetailsModal,RejectModal,ExecuteModal,ApproveModal}.tsx`, `src/ui/components/modal/__tests__/dsgn-rbndv2/` | `ModalFrame.tsx` | LOCAL | worker |
| `RV-m-3` | the 8 PortfolioManagement modals and `tabs/TradeTab.tsx` adopt the frame | FWD-3 | `src/pages/PortfolioManagement/components/*Modal.tsx` (8 named files), `src/pages/PortfolioManagement/tabs/TradeTab.tsx`, tests dir | `ModalFrame.tsx` | LOCAL | worker |
| `RV-m-4` | the 5 market-performance modals (RSI, Market Regime, Fear and Greed, Index Performance, Keyword Sentiment) adopt the frame | FWD-3 | `src/components/market-performance/{RSIModal,MarketRegimeModal,FearGreedModal,IndexPerformanceModal,KeywordSentimentModal}.tsx`, tests dir | `ModalFrame.tsx`, `ExecutiveSummary.tsx` | LOCAL | worker |
| `RV-m-5` | 7 shared and page modals adopt the frame (UserSettings, SessionTimeoutWarning, ModelPortfolio, two AdvisorIntelligence, DataRefresh rollback, Macro time series) | FWD-3 | the 7 named files, tests dir | `ModalFrame.tsx` | LOCAL | worker |
| `RV-m-6` | 9 remaining overlays (InvestorReporting export modal, button and browse drawer; SecurityScanner two tabs; SecurityAnalysis print action; Correlation ticker selector; Philosophy pillars) adopt the frame or are named NOT-A-MODAL; `App.tsx` account-menu popup takes the A-light surface | FWD-3 | the 9 named files, tests dir | `ModalFrame.tsx` | LOCAL | worker |

## 4. PLACEMENT AND BASE

All cells are portal cells. Chain 1 (`RV-m-1` to `RV-m-6`) is ONE worker's queue in ONE worktree, the next order handed by continuing the same subagent (spine L7); chain 2 is `RV-i-1` in its own worktree. The disk line is 12G free: two worktrees, nothing else cut.
The drain merges each chain end into `feature/dsgn-rbndv2-light` by merge, never rebase. Nothing is pushed (C-BRANCH). The closing run is `/market` and one opened market modal on the live local build (C-LIVE), by the COO, then the CVO's grade and Andrew's read.

## 5. DEPENDENCY EDGES AND CHAINS

Real data edge: `RV-m-2` to `RV-m-6` consume `ModalFrame` from `RV-m-1`: ONE chain, six orders, N = 1 worker. `RV-i-1` shares no file with chain 1 (`panels/` against `modal/`, pages and components): its own chain.
M = 2 chains, N = 2, cap 8. File disjointness across chains: `NestedCard.tsx` and `PanelGrid.tsx` are written by no adopter; `ExecutiveSummary.tsx` is written by nobody (read only by `RV-i-1` and `RV-m-4`); `src/App.tsx` is written only by `RV-m-6` (round-1's sidebar cell is merged and its direct act `RV-r-3` writes `src/ui/components/sidebar/` only).

## 6. BATTERY DISPOSITION

comp-iam: not applicable (no AWS surface). comp-schedule: none owed. comp-adversary: every named existing file was measured present at the feature branch @adc70061 (the census above); the graph check (portal rule 20) before a frontend commit: `Panel` has 96 importers
and `NestedCard` two real users, read at the cut.

## 7. RULE 24 FOUR-POSTULATE RECORD

(i) MECE over the declared domain, the CTO's four items, by subtraction (section 1); the modal population is a census with its denominator and its stated bound. (ii) Same grain: one cell per directory group of modals, one for the frame, one for the section primitives.
(iii) One intent per cell. (iv) State coherence: `RV-i-1` does not move `SectionCard` or `DarkCard`; the adoption cells do not move any modal's state, handlers or content (their bound criterion counts the tokens that must not fall); `ModalFrame` moves no existing component until a cell adopts it.

## 8. FINDINGS FOR THE CTO (at the cut)

- `RV-i-1` is cut AT THE PRIMITIVES, not as a per-file page edit: the inset cards are the shared `NestedCard` inside `PanelGrid`, so one primitive edit retires the box-in-box for both users with no page file touched (C-PANEL's own wording).
- Process: `RV-r-1`, `RV-r-2` and `RV-r-3` are direct acts and carry no `<round>` because the L6 gate (x) refuses a second issuance into a round otherwise (it accepts a `<direct_act>` order as round-less by design); every round-2 order carries `<round>2</round>`.
- Process: the worker's worktree copy of its order file still holds the record face (W6-S2); this issuance gives the worker the worker face as its prompt and tells it not to read below `## RECORD FACE`. The template departure itself is the CTO's.
- Disk: the 12G line binds at two worktrees.
