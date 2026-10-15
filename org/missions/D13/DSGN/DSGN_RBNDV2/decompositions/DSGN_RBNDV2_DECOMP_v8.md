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
