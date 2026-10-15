# DSGN_RBNDV2 -- DECOMPOSITION (L5) -- ROUND 8, THE PANEL TONE (PRD v0.1)

```json
{
 "project": "DSGN_RBNDV2",
 "directive": "D13",
 "macro": "DSGN",
 "fabric": "laptop",
 "decomp_version": "v8",
 "step": 5,
 "prd_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/prd/DSGN_RBNDV2_PRD.md@e71a48e4b0 (v0.1, RATIFIED; both halves signed)",
 "round_analysis_ref": "org/missions/D13/DSGN/DSGN_RBNDV2/deliverables/2.0.0_SA_COO~RB/ANDREW_DIRECT_20261015_PANEL_TONE.md (Andrew's words, verbatim); the CTO's round-7 analysis (msg 109487) says park until his words",
 "author": "2.0.0_SA_COO~RB",
 "round": 8,
 "rectangle": "Andrew's two messages: 'everything is blinding white' and 'Try your recommendation' (a soft off-white panel, #F8F8FD, over the #EAEAF7 ground)",
 "cells": 1,
 "chains": 1,
 "join_cells": 0,
 "portal_base": "feature/dsgn-rbndv2-light @3509eae8 (local, no upstream, never pushed)",
 "frozen": true
}
```

**Author:** `2.0.0_SA_COO~RB`. **Input:** Andrew's words (record above), which release the CTO's "park" for this one change. Round 7 (the local candidate rehearsal) awaits the CVO's grade in parallel; round 8's order is a direct act (round-less, LOCAL, about 40 product lines) so it does not enter round 7's gate. **Frozen at the cut.**

## 1. THE DOMAIN, BY SUBTRACTION (Rule 24(i))

Denominator: Andrew's two messages: (a) the question whether the sidebar and background use #EAEAF7 (answered by measurement: they do, on six pages); (b) "everything is blinding white" with "Try your recommendation" (the soft off-white panel). Placed: (b) as `RV-b-1`. Remainder: none.

**Measured cause:** every `Panel` and `ModalFrame` root paints `bg-[hsl(var(--bg-surface))]` (`--bg-surface: 0 0% 100%`), and the inner-surface remap block (`:root [data-panel-surface="light"]` in `src/index.css`) sets the five nested grounds to white; panels cover 64 to 78 percent of the viewport, so the page reads white. `--bg-surface` is ALSO the text colour of an action-fill chip (`hsl(var(--bg-surface))` in the exception rule) and the focus-ring inner colour, so it must not change value.

## 2. THE CELL -- 1 (round 8)

| cell | what it builds | serves | writes | risk | class |
|---|---|---|---|---|---|
| `RV-b-1` | a new token `--bg-panel: 240 55.6% 98.2%` (#F8F8FD); an unlayered rule `[data-panel-surface="light"] { background-color: hsl(var(--bg-panel)) }` that repaints every panel, modal and popup root; the five nested panel grounds of the remap block read `--bg-panel`; `DarkCard` and `SectionCard` read `--bg-panel`; `--bg-surface` unchanged | FWD-3, FWD-5 | `src/index.css`, `src/ui/components/panels/`, `src/__tests__/dsgn-rbndv2/` | LOCAL | worker-light (direct act) |

## 3. PLACEMENT, EDGES, BATTERY

One cell, one chain. The proof is the COO's live read after the merge (computed backgrounds of a panel, a modal and a nested card; the ground unchanged) and Andrew's own smoke test on `localhost:5174`. After it lands the local candidate (`cand/laptop/dsgn-rbndv2-light`) is stale against the feature branch; per the CTO's round-7 message it is re-cut from the last PROD (a short local rehearsal) before any push word. comp-iam, comp-schedule: not applicable. comp-adversary: no other order is open; rule 20 graph check: portal CSS and component classes only.

## 4. RULE 24 FOUR-POSTULATE RECORD

(i) MECE over Andrew's two messages (section 1). (ii) One grain: the panel surface tone. (iii) One intent: soften the panel white. (iv) State coherence: the tone moves panels, modals, popups and their nested grounds; it does not move `--bg-surface`, any text colour, the action-fill exception, the focus ring, the ground `#EAEAF7`, the header band `#EEF1F6`, tooltips or any chart colour.

## ADDENDUM 1 (2026-10-15 ~19:4xZ, 2.0.0_SA_COO~RB, issuer ruling inside its own decomposition) -- cells `RV-g-1` and `RV-n-1`, direct acts

Input: Andrew's third and fourth messages (record `ANDREW_DIRECT_20261015_PANEL_TONE.md`, sections 3 and 4, verbatim): the darker positive and negative pair ("rec approved keep going", after the COO measured the signed figures at 1.94 and 2.56 to 1 contrast and proposed #14713B and #BB1B30), and a silver step for the contained internal panels with a depth strategy for multiple layers of nesting.

| cell | what it builds | serves | writes | risk | class |
|---|---|---|---|---|---|
| `RV-g-1` | `--success` and `--danger` re-set darker (`145 70% 26%`, `352 75% 42%`) inside every `[data-panel-surface="light"]` root; tokens only, no component edit | FWD-3, FWD-5 | `src/index.css`, `src/__tests__/dsgn-rbndv2/` | LOCAL | worker-light (direct act) |
| `RV-n-1` | tokens `--bg-nest-1` (#EEF1F6) and `--bg-nest-2` (#E6EBF4); the four item-container grounds read the first step, a container nested in another reads the second step by a descendant selector; the panel's general space stays the panel tone; no border | FWD-3, FWD-5 | `src/index.css`, `src/__tests__/dsgn-rbndv2/` | LOCAL | worker-light (direct act) |

**Order of work:** `RV-b-1` (in flight; its worker was re-seated on the issuer's ruling for two existing test arms) merges first; then `RV-g-1`; then `RV-n-1`; each worktree is cut from the feature tip after the previous merge (all three write `src/index.css`; at most two worktrees live at once). `RV-n-1` supersedes what `RV-b-1` sets for four of the five nested grounds (panel tone -> first silver step) and supersedes, for CONTAINERS THAT HOLD ITEMS, round 2's hairline-section treatment; hairline sections inside a panel body stay. Gate limb that graded the addendum: none graded the modification (direct-act orders are round-less; the gate checked grammar, `<decomp_ref>` and preflight).

## ADDENDUM 2 (2026-10-15 ~20:3xZ, 2.0.0_SA_COO~RB, issuer ruling inside its own decomposition) -- cell `RV-g-2`, a direct act

Found at the drain of `RV-g-1`: a live read after its merge showed the signed figures on `/market` unchanged (`+2.31%` `rgb(45, 205, 136)`, `-10.73%` `rgb(251, 112, 132)`). The COO's earlier measurement named the wrong pair: the signed figures read the return-delta tokens `--delta-positive` / `--delta-negative` and their `-hover` steps (consumed by `src/lib/performanceUtils.ts` lines 74-75 and `ExecutiveSummary.tsx` lines 696-697; a lightened set for the named-layer scope sits at `index.css` lines 401-403), not `--success` / `--danger` (which paint titles and status chips). `RV-g-2` adds the four delta tokens, darker, to `RV-g-1`'s block (green `#14713B`, red `#BB1B30`, hovers `#0F5C2F` and `#9F1426`). It follows `RV-n-1` (both write `src/index.css` at adjacent places). Gate limb that graded the addendum: none graded the modification.

