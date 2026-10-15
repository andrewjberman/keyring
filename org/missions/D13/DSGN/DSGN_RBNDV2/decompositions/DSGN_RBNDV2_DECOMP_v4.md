# DSGN_RBNDV2 -- DECOMPOSITION (L5) -- ROUND 4, THE ALPHA-WHITE CLASS SWEEP (PRD v0.1)

```json
{
 "project": "DSGN_RBNDV2",
 "directive": "D13",
 "macro": "DSGN",
 "fabric": "laptop",
 "decomp_version": "v4",
 "step": 5,
 "prd_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/prd/DSGN_RBNDV2_PRD.md@e71a48e4b0 (v0.1, RATIFIED; both halves signed)",
 "round_analysis_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/ledger/ROUND_ANALYSIS.round3.md@4802286e30 (1.0.0_SA_CTO; CTO msg 109404)",
 "author": "2.0.0_SA_COO~RB",
 "round": 4,
 "rectangle": "the CTO's round-3 enrichment items 1 and 2: (1) the alpha-white class sweep across the modals, with before and after counts and the computed colour of an inactive chip; (2) the RSI modal read live through its real trigger (the COO's act, done before this cut); item 3 (the FWD-5 walk) starts on Andrew's YES to call 3c44",
 "cells": 1,
 "chains": 1,
 "join_cells": 0,
 "portal_base": "feature/dsgn-rbndv2-light @cf2bdeaa (local, no upstream, never pushed)",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~RB`. **Input:** the CTO's round-3 analysis (msg 109404) over the CVO's L9 grades (`ADJUDICATION_v4.md`, RB3C1-AC3 and RB3C2-AC2 both MET). **Frozen at the cut.**

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

Denominator: the CTO's three round-4 enrichment items. Item 2 (the RSI live read) is the COO's own act and is DONE before this cut: a scripted walk clicked a Global RSI chart bar (`.recharts-bar-rectangle path`, 3 matches), the
"Global RSI" dialog opened, it holds 53 text elements and 0 white-alpha text; recorded in `ROUND4_RSI_AND_ALPHA_READ_20261015.md`. Item 1 PLACED as `RV-w-1`. Item 3 (the FWD-5 walk) HELD by the CTO's own condition (Andrew's YES to call `3c44`). Remainder after
subtraction: item 3 only, held with its condition.

**The measured cause of item 1 (before counts, live, three opened modals; a text element is counted when its computed colour is white or white-alpha, `rgb(255,255,255` or `oklab(0.99...`):** the Index Performance modal (press "S&P 500") 3 elements: its inactive period chips `30D`, `90D`, `3Y`,
computed `oklab(0.999994 ... / 0.6)` (white at 60 percent) from `text-white/60`; the U.S. Regime: Momentum modal 4: two inactive chips (`1Y`, `3Y`) and two tooltip labels (`Score`, `RSI Score`, white 0.85 on the violet chart tooltip, which is legitimately white and stays); the Fear and Greed modal 0
(its chips carry no hover variant). **Why the round-1 legibility rule misses them:** the rule in `portal/src/index.css` (the RV-t-1 block, lines 546 to 555) selects `[class*="text-white/"]:not([class*=":text-white/"])`, and an element whose class list also holds a variant such as `hover:text-white` or `hover:bg-white/10` is excluded
by the `:not`, so the chip keeps white-at-60 on the silver surface. **A second defect, measured in the same read:** an ACTIVE chip (`bg-[hsl(var(--primary))] text-white`) computes to navy `rgb(10, 23, 51)` on the violet fill (about 2.6:1), because the same rule turns every `text-white` navy (row `DSGN_RBNDV2-W1-S2`, now measured).

## 2. THE CELL -- 1 (round 4)

| cell | what it builds | serves | writes | reads (never writes) | risk | class |
|---|---|---|---|---|---|---|
| `RV-w-1` | the legibility rule matches the white-alpha classes EXACTLY instead of by substring-with-exclusion: for every alpha 5, 10, ... 95 (19 values), `.text-white\/N`, `.border-white\/N`, `.bg-white\/N` and their `hover:` forms map to the ink, rule and no-fill tokens inside `[data-panel-surface="light"]`; a `text-white` element that also carries a solid action fill (`bg-[hsl(var(--primary))]` or `bg-[hsl(var(--semantic-action-primary))]`) stays white | FWD-3, FWD-5 | `src/index.css`, `src/__tests__/dsgn-rbndv2/` | `src/components/market-performance/IndexPerformanceModal.tsx` | LOCAL | worker-light |

## 3. PLACEMENT, EDGES, BATTERY

One portal cell, one worktree from the feature branch; M = 1 chain, N = 1, cap 8; no other order is open. The closing proof is the COO's live read: the computed colour of an inactive chip in the opened Index Performance modal (navy, not white-alpha), the active chip's text on its violet fill (white), the white-alpha text counts before
(3, 4, 0) and after in the same three modals, then the CVO's grade. comp-iam, comp-schedule: not applicable. comp-adversary: `index.css` is written by no other open order; the graph check (portal rule 20): the rule is scoped to `data-panel-surface="light"`, set by `Panel` and `ModalFrame` roots only.

## 4. RULE 24 FOUR-POSTULATE RECORD

(i) MECE over the CTO's list by subtraction (section 1). (ii) One grain, one cell. (iii) One intent: the white-alpha class family inside the light scope. (iv) State coherence: the rule moves only the three alpha-white class families (text, border, background) and their hover forms inside the scope; it does not move the dark band, chart colours,
the tooltip's own white, or anything outside `data-panel-surface="light"`.

## 5. FINDINGS FOR THE CTO (at the cut)

- The class sweep is done at the CSS seam (exact class selectors), not file by file: it covers every modal and panel at once, and the counts are measured live, not by grep.
- RSI is reachable: a chart-bar click opens it, so W10-S2's live read is done and no "no control reaches it" finding is owed.
