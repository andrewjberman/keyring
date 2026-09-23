# The CLOUD documents and the process worth repeating

All paths below are relative to the workspace repository **at CLOUD pin `365ab567ba1250a6a3569df38cb75d12fe2e8d0e`**. They were read through `git show`; they are not necessarily present in SITEZ's working tree. For example:

```powershell
git show 365ab567ba1250a6a3569df38cb75d12fe2e8d0e:org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md
```

## Guiding research

Under `org/tier1_exec/4.0.0_SA_CRO/deliverables/`:

| File | What it contributed |
|---|---|
| `PERFORMANCE_END_TO_END_GAP_BRIEF_20260922.md` | Requested accounts/dates -> provider calculation -> normalized result -> persistence -> browser -> exact export; each connector assessed separately |
| `MODEL_OVERLAY_END_TO_END_GAP_BRIEF_20260922.md` | Source custody/model truth -> normalized holdings -> published snapshot -> authorized selection -> page; fake completeness and absent serving outputs exposed |
| `SENSITIVITY_END_TO_END_GAP_BRIEF_20260922.md` | Input -> request/revision -> generation -> vendor output -> extracted report -> screen/export; connector-level work rather than feature labels |
| `IRPT_REPORTING_BACKEND_AND_LGIC_MODEL_BRIEF_20260922.md` | Shared backend, contracts and LGIC responsibilities across the three tabs |
| `IRPT_STORAGE_STATE_AND_END_STATE_20260922.md` | Measured buckets, prefixes, tables and pointers; retained research artifacts distinguished from served product artifacts |
| `SMARTX_49F_PERFORMANCE_ADAPTER_BRIEF_20260922.md` | Later provider direction, explicitly referenced as superseding the original Performance brief's 49F recommendation by the completion contract/mandate |

The relevant lesson is to follow the actual browser and data carriers. A field on a screen, a completed adapter test, or an existing bucket is not evidence that all connecting steps work.

## Direct completion authority and mandates

Under `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/`:

- `AUTHORITY.md`: Andrew's direct completion mandate and the operating boundaries.
- `CONTRACT.md` v1.2: three direct implementers, matched reviewers, sole shared-surface owners, concrete interfaces, complete journey ownership, evidence and conflict rules.
- `COO_P.md`: Performance **and** common report/export integration; matching reviewer CVO~P.
- `COO_M.md` and `COO_Y.md`: Model Overlay and Sensitivity lane mandates, with corresponding CVO files.
- `OVERSIGHT.md`, `RULINGS.md` and `LIVE_SCOPE_OWNERSHIP_TRANSFER_20260923.md`: oversight and subsequent scope decisions; ownership can transfer explicitly without silently expanding another seat's mandate.

The contract/authority and P mandate were read directly. The remaining mandate/oversight names are navigation pointers, not a claim that this audit independently verified every subsequent IRPT execution result. **This research establishes the precedent's structure, not that all IRPT acceptance gates are now green.**

## Adopt for AMGT

| IRPT practice | AMGT application |
|---|---|
| One implementer owns the full product path | Four pipeline mandates; frontend/backend boundary does not end ownership |
| Existing workers and accepted changes preserved | Reconcile current CORPUS c-11 and RESAPP rk-49 ownership before transferring work; preserve landed round-36 fixes |
| No subworker dispatch or repetitive recutting for routine defects | Closers implement personally and repair connector defects through their acceptance tests |
| One integrator for shared report/API/export surfaces | Report Experience closer R owns common API/frontend/IaC integration; other lanes supply concrete patches and fixtures |
| Early S1-S7 interface artifacts | AMGT I1-I7 contracts in the closer contract, based on existing types/builders |
| Workspace and deployed pins kept separate | Package hashes, deployed role/configuration, stored object hashes, actual browser request and export revision retained together |
| Independent outcome review | A reviewer who did not implement the path reproduces boundary cases; fixtures cannot establish live completion |
| Specific reserved external acts, independent work continues | Existing publisher, Bloomberg, model-data/model-tier, timeline and promotion gates have named downstream effects; they do not freeze unrelated code |

Do not copy IRPT's vendor contracts, bucket names, seat suffixes or three-tab staffing mechanically. AMGT's library, terminal-bound data sources and four substantial pipelines justify its own ownership map. The roles in this package are proposed responsibilities, not invented registered seats.
