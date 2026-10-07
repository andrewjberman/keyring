# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM K: sign-out clears the staged prospect

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "K",
 "prd_ref": "org/missions/D9/IRPT/IRPT_YCDGEN/prd/IRPT_YCDGEN_PRD.md (v0.8; ENDPOINT unchanged since v0.5 @e6a801f7f0)",
 "prd_version": "v0.8",
 "endpoint_outcomes": ["FWD-1"],
 "round_scope": ["FWD-1"],
 "author": "2.0.0_SA_COO~G2",
 "cells": 1,
 "chains": 1,
 "join_cells": 0,
 "frozen": true,
 "revision": "1.0",
 "parent_decomp": "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6J.md",
 "cell_ids": ["YCD-t-6"]
}
```

**Why an addendum.** 1.0.0_SA_CTO~DELL2 read the portal candidate `cand-r6-prospect-firm` @4d16a2a0 against origin/DEV 8ddfe409 (ruling msg 64, 2026-10-07 ~07:46Z). It ruled that e-6 and p-6 LAND, j-6 LANDS WITH A NOTE, and q-6 needs REWORK first. `stagedProspect.ts:84` keeps the staged file and its review result in module memory. `logout()` (`src/contexts/AuthContext.tsx` ~614-654) clears the query cache, but it neither reloads the page nor resets this store. The next user on the same tab therefore gets the previous user's prospect holdings back. The ruling's fix: export a full reset (firm, file, result, uploadAttempt, notedDropdownFirm) and call it in logout next to `clearCanonicalDataAsOf()`, with one pin that fails without it. Also align the `stagedProspect.ts` header comment with `ProspectComposer.tsx:156`, which preselects the tab's firm. If the diff is only this, the whole stack (e-6, j-6, p-6, q-6, this cell) lands on DEV with no second review.

## Cell

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-t-6` | 8 Open (page wiring) | `portal/src/pages/InvestorReporting/tabs/analysis/stagedProspect.ts`, `portal/src/contexts/AuthContext.tsx`, `portal/scripts/prospect-firm-exercise.mjs` | `tabs/analysis/ProspectComposer.tsx`, `src/lib/dataAsOfCanonicalStore.ts` | q-6's portal stack, merged with DEV as `cand-r6-prospect-firm` @4d16a2a0 (on origin) |

**Writer read.** No non-terminal task order of the project names these paths (q-6 is complete @f97c6374c6).

**Contract R18(d) Sign-out clears the staged prospect.** `stagedProspect.ts` exports one reset that returns every piece of module state the card holds to its fresh-page-load value: firm, file, result, uploadAttempt, parentInput, notedDropdownFirm and the published firm catalogue. `logout()` in `AuthContext.tsx` calls it in the same block as `clearCanonicalDataAsOf()`. After a sign-out, nothing a previous user staged can be read back from the module. The header comment no longer contradicts `ProspectComposer.tsx:156`.

## Edges and fan-out

M = 1, no dependency open. fanout: 1 of 1 chain, cap 8, reason: one portal wiring cell. It lands on portal DEV with e-6, j-6, p-6 and q-6 under the CTO's msg-64 ruling; F1 follows on the served DEV build.

## Four-postulate record (Rule 24)

MECE: the store has one writer set (the card), and this adds exactly one clearing event that was not covered before, sign-out. Same grain: one store, one reset. Intent: one outcome (no cross-user carry-over). State: the remount survival (R18 c) and the firm-change clear are not moved, and the exercise's `remount` arm still grades them.

## Battery

comp-schedule, comp-iam and comp-adversary DECLARED-NOT-APPLICABLE (a portal wiring change, no deploy, no grant).
