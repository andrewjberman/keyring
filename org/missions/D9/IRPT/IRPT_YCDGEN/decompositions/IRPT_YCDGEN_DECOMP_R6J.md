# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM J: the Prospect card names the firm it is for, the firm dropdown lists real options, the staged upload survives a remount

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "J",
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.8; ENDPOINT unchanged since v0.5 @e6a801f7f0)",
 "prd_version": "v0.8",
 "endpoint_outcomes": ["FWD-1"],
 "round_scope": ["FWD-1"],
 "author": "2.0.0_SA_COO~Y",
 "cells": 1,
 "chains": 1,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "parent_decomp": "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6I.md",
 "cell_ids": ["YCD-q-6"]
}
```

**Why an addendum.** F1 walks of 2026-10-06 and the `/closer trace "analysis tab"` brief `org/tier1_exec/2.0.0_SA_COO/deliverables/ANALYSIS_TAB_END_TO_END_GAP_BRIEF_20261006.md` @3222740e0c found that FWD-1's own path (the Prospect portfolio upload, PRD v0.8 FWD-1 and s2 step 1) cannot run from the Analysis tab for an Opal (Global) principal: with no client picked the upload and the submit carry no `selected_tenant`, the server refuses a write whose owner firm is `global` or `opal-capital`, the Firm dropdown shows "Global (All)" once a firm is chosen (its option list is built from a Global context that is empty by then), and the staged upload is discarded by a remount. Andrew-direct 2026-10-06, VERBATIM: "Prospect card could ask for a firm, because it's going to be produced for a given firm inherently". CTO ruling msg 105720: cut one portal cell now under FWD-1, no contract change, no PRD change (the existing tenant contract).

## Cell

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-q-6` | 8 Open (page wiring) | `portal/src/pages/InvestorReporting/tabs/analysis/ProspectComposer.tsx`, `.../tabs/analysis/AnalysisTab.tsx`, `.../tabs/analysis/stagedProspect.ts` (new), `.../header/FirmDropdown.tsx`, `.../index.tsx`, `portal/scripts/prospect-firm-exercise.mjs` (new) | `header/search.ts`, `header/firm.ts`, `contracts/adapt.ts`, `api/endpoints/investor-reporting.ts` | p-6's portal commit e107538d (UNLANDED, branch wk-IRPT_YCDGEN-81-portal) |

**Writer read.** A scan of the non-terminal task orders of the project for these paths found 0 hits (p-6 is complete).

**Contract R18 The Prospect card names its firm.** (a) For an internal (Opal) principal the Prospect card shows a firm choice (the real firm options, from the same catalogue the Firm dropdown uses); it is preselected to the Firm dropdown's firm when that is not Global, and the card refuses to upload and says in plain words why while no firm is chosen. The chosen firm's tenant is sent as `selected_tenant` on the upload (`analysis-input-upload`), on the submit (`analysis-requests`) and on the comparison catalogue read; for a single-firm principal the card behaves exactly as before. (b) The Firm dropdown lists Global plus every firm of the catalogue at all times, so the selected value is always one of its options and it never shows "Global (All)" while the page is single-firm. (c) A staged file and its review result are held in memory above the keyed composer (a module-level store in the new `stagedProspect.ts`, never browser storage, never serialised) so a client pick or a tab switch does not discard them; a change of the card's firm or the explicit choice of a different file clears them. Client data never leaves memory.

## Edges and fan-out

M = 1, no dependency open. fanout: 1 of 1 chain, cap 8, reason: one portal wiring cell. It lands on portal DEV with e-6, j-6 and p-6 after the CTO's review; F1 retries from the CTO's server on port 5174.

## Four-postulate record (Rule 24)

MECE: the firm has one source on the card (its own choice, defaulted from the dropdown) and three consumers (upload, submit, catalogue read). Same grain: one value, one card. Intent: one outcome (a Prospect request names its firm). State: the picked-client path (p-6) and a single-firm context are not moved; history without a client is NOT in this cell (next-round row).

## Battery

comp-schedule, comp-iam and comp-adversary DECLARED-NOT-APPLICABLE (a portal wiring change, no deploy, no grant).
