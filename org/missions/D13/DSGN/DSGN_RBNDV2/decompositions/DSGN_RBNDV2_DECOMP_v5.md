# DSGN_RBNDV2 -- DECOMPOSITION (L5) -- ROUND 5, ANDREW'S MARKET OVERVIEW FIX LIST (PRD v0.1)

```json
{
 "project": "DSGN_RBNDV2",
 "directive": "D13",
 "macro": "DSGN",
 "fabric": "laptop",
 "decomp_version": "v5",
 "step": 5,
 "prd_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/prd/DSGN_RBNDV2_PRD.md@e71a48e4b0 (v0.1, RATIFIED; both halves signed)",
 "round_analysis_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/ledger/ROUND_ANALYSIS.round4.md@93c3fb9a2f (1.0.0_SA_CTO; CTO msg 109415) read with the Andrew-direct record org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_MARKET_OVERVIEW_FEEDBACK.md",
 "author": "2.0.0_SA_COO~RB",
 "round": 5,
 "rectangle": "Andrew's Market Overview comments (11 items, one message, 2026-10-15 ~10:2xET): the FWD-5 walk's first page, fed by his own eye; item 2 (tooltip placement) is held as an open call because his words fit two designs",
 "cells": 6,
 "chains": 6,
 "join_cells": 0,
 "portal_base": "feature/dsgn-rbndv2-light @7f8731df (local, no upstream, never pushed)",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~RB`. **Input:** Andrew's typed comments on the live Market Overview page (call `3c44` closed on his words "It largely looks good" plus the list) and the CTO's round-4 analysis, whose item 1 (the RSI Ranked view) was read by the COO with no defect. **Frozen at the cut.**

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

Denominator: Andrew's 11 numbered items (the record's section "How the COO reads it"). Each is placed or held:

| item | Andrew's words in brief | placed in |
|---|---|---|
| 1 | trend arrow white (Trending Topics tile) | `RV-x-6` (marker on the tile) + `RV-x-1` (the rule that keeps white on a marked fill) |
| 2 | tooltips left of the panel header title | HELD, open call `laptop-20261015T145235Z-002b` (his words fit two designs); the only item not cut |
| 3 | footers proper capitalization (panels and modals) | `RV-x-2` (panels; modal footers already read in mixed case in his own screenshots) |
| 4 | Trending Topics popup in light mode | `RV-x-6` |
| 5 | tooltip text white on indigo (Index Performance modal, RSI panel, Daily Cloud) | `RV-x-1` (one rule covers every indigo tooltip box in a light surface) |
| 6 | Daily Cloud: no glow | `RV-x-5` |
| 7 | text resolves to ink on white; the topic modal row title returns to white after a hover; no white gridlines on white | `RV-x-5` (the inline `onMouseLeave` write) and the literal whites of the charts in `RV-x-3`, `RV-x-4` |
| 8 | RSI panel labels white on white | `RV-x-3` |
| 9 | RSI Full view Trend value case; Asset Class dropdown width | `RV-x-3` |
| 10 | Fear and Greed dial and text white on white | `RV-x-4` |
| 11 | Component Indicators tile hover tint | `RV-x-4` |

Remainder after subtraction: item 2 only, held with its condition. **Measured causes** (source read at the feature tip 7f8731df, with live reads where the walker reaches): (a) the round-4 legibility rule maps `text-white*` to navy inside every light surface, so an indigo tooltip (`DataTooltip`, the Daily Cloud tooltip, the Fear and Greed methodology popover) and a coloured tile read navy on their fill; (b) `RSIBars.tsx` and `EmotionalIntensityMeter.tsx` draw literal whites in SVG and chart props that no class rule can reach; (c) `KeywordSentimentModal.tsx:538` writes `style.color = 'white'` on mouse leave, an inline value that beats the stylesheet (the only such assignment in `src`, one `git grep` over `src`); (d) `PanelFooter.tsx` forces `uppercase`; (e) `ExecutiveSummary.tsx` `DrilldownModal` keeps its own dark overlay (row `W8-S8`).

## 2. THE CELLS -- 6 (round 5)

| cell | what it builds | serves | writes | risk | class |
|---|---|---|---|---|---|
| `RV-x-1` | inside an indigo-filled box or an element marked `data-ink="on-fill"`, the white idioms (`text-white`, `text-white/N`, `border-white/N`, `bg-white/N`, 19 alphas) stay white | FWD-3, FWD-5 | `src/index.css`, `src/__tests__/dsgn-rbndv2/` | LOCAL | worker-light |
| `RV-x-2` | the panel footer reads in mixed case (no `uppercase`) | FWD-3, FWD-5 | `src/ui/components/panels/`, `src/__tests__/dsgn-rbndv2/` | LOCAL | worker-light |
| `RV-x-3` | RSI panel chart literals to ink tokens; Trend value title case; Asset Class select wider | FWD-3, FWD-5 | `RSIBars.tsx`, `RSIModal.tsx`, tests | LOCAL | worker-light |
| `RV-x-4` | Fear and Greed dial and text to ink tokens; Component Indicators tile hover tint | FWD-3, FWD-5 | `EmotionalIntensityMeter.tsx`, `FearGreedModal.tsx`, tests | LOCAL | worker-light |
| `RV-x-5` | Daily Cloud glow removed; the modal row title no longer resolves to white after a hover | FWD-3, FWD-5 | `TopicCloud.tsx`, `KeywordSentimentModal.tsx`, tests | LOCAL | worker-light |
| `RV-x-6` | the Trending Topics popup on the shared modal frame; the tile and hero marked `data-ink="on-fill"` | FWD-2, FWD-5 | `ExecutiveSummary.tsx`, tests | LOCAL | worker |

## 3. PLACEMENT, EDGES, BATTERY

Six chains, six cells, disjoint write sets (each cell writes its own component files and its own new test file; only `RV-x-1` writes `index.css`). The one soft edge is `RV-x-6` -> `RV-x-1` at the live read only (the arrow reads white once both are merged); neither build waits on the other. **Spawn waves:** disk on this laptop is at 92 percent used with other seats' worktrees live, so at most TWO worker worktrees run at once (each about 3.7G): wave 1 `RV-x-1`, `RV-x-6`; wave 2 `RV-x-3`, `RV-x-4`; wave 3 `RV-x-2`, `RV-x-5`; each merged and removed before its slot's successor starts. The closing proof is the COO's live read after the drain: tooltip text white in three surfaces, a panel footer's computed `text-transform`, the RSI panel and modal, the Fear and Greed dial, the Component Indicators hover, the Daily Cloud filter, the Trending Topics popup; then the CVO's grade and Andrew's eye (DEC-5). comp-iam, comp-schedule: not applicable. comp-adversary: no other order is open; rule 20 graph check: every change is in portal source, no cloud or data surface.

## 4. RULE 24 FOUR-POSTULATE RECORD

(i) MECE over Andrew's 11 items by subtraction (section 1). (ii) One grain: a component or a stylesheet block per cell. (iii) One intent per cell: the ground-aware ink rule (x-1), the footer case (x-2), the RSI surfaces (x-3), the Fear and Greed surfaces (x-4), the cloud and hover (x-5), the Trending Topics popup (x-6). (iv) State coherence: x-1 moves only the white idioms inside an indigo box or a marked fill and leaves every other rule, token and chart colour; x-2 does not move the footer text, layout or the modal footers; x-3 and x-4 do not move the bar glow, the reference lines or the coloured gauge.

## 5. FINDINGS FOR THE CTO (at the cut)

- Andrew's principle, stated once so every later page applies it: text is black ink on a white ground and white on a coloured fill; a line is grey on white and black on a colour. Round 4's rule applied the first half everywhere and so broke the second half on tooltips and tiles; `RV-x-1` restores it at the seam.
- The hover bug is a CLASS: an inline `style.color = 'white'` on a mouse-leave handler. The only instance in `src` is `KeywordSentimentModal.tsx:538`; `RV-x-5`'s test walks every non-test `.tsx` file so a second instance fails the suite.
- Item 2 (tooltip placement) waits on his answer; the other ten are cut now.
