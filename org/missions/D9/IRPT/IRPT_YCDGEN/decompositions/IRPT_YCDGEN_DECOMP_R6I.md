# IRPT_YCDGEN -- DECOMPOSITION, ROUND 6 ADDENDUM I: the Analysis tab sends the picked client's own firm, never an empty one

```json
{
 "project": "IRPT_YCDGEN",
 "round": 6,
 "addendum": "I",
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
 "parent_decomp": "org/missions/D9/IRPT/IRPT_YCDGEN/decompositions/IRPT_YCDGEN_DECOMP_R6H.md",
 "cell_ids": ["YCD-p-6"]
}
```

**Why an addendum.** F1 walk 2026-10-06 ~13:03Z: Andrew, signed in as an Opal (Global) principal, picked a Cottonwood client and pressed Generate; the page showed "Needs attention -- areq-efd72c44". The resident host saw no job. `irpt-ycharts-generate` logged `comparison-catalogue` `BucketUnmapped` (the request carried no firm, so the server read the principal's own tenant, `opal-capital`, which the directory bucket map does not hold). CTO ruling msg 105563: `GenerateComposer.tsx:226-230` calls `fetchCatalogue(scopeRef.selectedTenant)` with no guard, and `selectedTenant` is `selectedScope.registryTenant` (`index.tsx:222-225`), which in Global scope arrives empty after a client is picked. `ProspectComposer.tsx:160-161` already carries the guard (item 89). Andrew also reports the firm selector reverts to Global when he picks a client; that reversion is expected for a Global principal and is not the fault.

## Cell

| cell | hop | writes | reads | depends on |
|---|---|---|---|---|
| `YCD-p-6` | 8 Open (page wiring) | `portal/src/pages/InvestorReporting/index.tsx`, `portal/src/pages/InvestorReporting/tabs/analysis/GenerateComposer.tsx`, `portal/scripts/global-tenant-exercise.mjs` (new) | `ProspectComposer.tsx`, `contracts/adapt.ts`, `header/ClientSearch.tsx` | j-6's portal commit cd3924d5 (UNLANDED, branch wk-IRPT_YCDGEN-70-portal) |

**Writer read.** A scan of the non-terminal task orders of the project for the three paths found 0 hits.

**Contract R17 The tenant sent with the catalogue read and the submit is the picked client's own firm.** For a principal in Global scope who has picked a client, `selectedScopeRef.selectedTenant` is the firm tenant of that client's entry (the `firm.tenant` of the global firm context whose `verifiedRequestFirm.firmId` equals the picked row's `firmId`), never empty and never the principal's own tenant. `GenerateComposer` (a) does not read the catalogue when it holds no tenant and (b) refuses to submit with no tenant and says on the page why, in plain words, with no internal code. A single-firm (non-Global) context behaves exactly as before.

## Edges and fan-out

M = 1, no dependency open. fanout: 1 of 1 chain, cap 8, reason: one portal wiring fix. The fix lands on portal DEV with e-6 and j-6 after the CTO's review (product files); F1 runs from the local dev build at port 5174 on the worker's portal commit until then.

## Four-postulate record (Rule 24)

MECE: the tenant has one source (the picked entry's firm) and one consumer pair (catalogue read, submit). Same grain: one value, two call sites. Intent: one outcome (a request names its firm). State: a single-firm context and the ProspectComposer guard are not moved.

## Battery

comp-schedule, comp-iam and comp-adversary DECLARED-NOT-APPLICABLE (a portal wiring change, no deploy, no grant).
