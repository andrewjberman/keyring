# COO~M — complete Model Overlay and shared data/selection

Exact seat: `2.0.0_SA_COO~M`. Read AUTHORITY.md and CONTRACT.md. This is Andrew's current assignment for this suffix; historical MCPINDEX seating suggestions are superseded. Reviewer: `3.0.0_SA_CVO~M`. Implement directly; coordinate with COO~P and COO~Y.

Deliver a current investor ownership view showing actual model-associated, confirmed non-model, and unresolved assets, with reconciled dollars/weights and complete account/security drilldowns for 49F, Cottonwood and Inflection. Model feeds are SmartX, Black Diamond Rebalancer, and Eclipse respectively. Start from the entire custody population, never the model roster.

Your owned shared work is selection/grants/vendor crosswalks, accepted custody data, LGIC naming/firm publication, and the holdings API/UI. Publish S1/S2 interfaces early to P/Y. Coordinate prospect firm/advisor ownership with Y; coordinate reporting artifact placement with P. P integrates common frontend client/schema aggregator edits from your patches.

Latest performance decision: 49F SmartX primary with independent BD verification (desktop folder 06). Your custody census and **dated** account/allocation/model crosswalk must support P's historical actual-performance scope, including model changes, sleeve closures and non-model/cash accounts. A current model assignment cannot establish historical ownership. Model ownership sources and your snapshot product are otherwise unchanged.

## First actions

Read folders 03, 04 and 05 of the desktop package, the actual holdings builders/entry/projector and mounted UI. Reproduce the three synthetic math cases before repairing them. Record baseline pins and file claims, establish an isolated code branch, then implement one selected-investor journey through actual handler and UI. Do not spend a new round merely restating the audit.

## Acceptance

- **M1 Population:** all firm custody accounts are represented or explicitly accounted for, including entirely non-model, closed/zero and missing-input accounts. Unknown values are distinct from zero. Source completeness/freshness is independently measured.
- **M2 Identity/grain:** unique accounts/positions; multiple SmartX allocations do not duplicate accounts; shared Eclipse portfolio values are not repeated per account; Cottonwood targets are not passed off as observed holdings. Supported attribution grain is explicit.
- **M3 Economics:** model + non-model + unresolved known value equals independently enumerated unique custody value. Correct selected-set and parent denominators; separate source clocks; missing mappings remain unresolved. Fix the $100->$200 49F, $120->$200 INF, and 100%/75% COT probe cases with meaningful regressions.
- **M4 Publication:** canonical Gold Parquet history, bounded Platinum JSON and manifest; failed validation never advances current publication; same-day corrections have unique revisions; previous accepted output remains honestly stale after failed refresh.
- **M5 Scope/API:** real grants, exact requested subset, canonical-to-provider crosswalks, truthful availability/coverage, tenant separation and revocation. Filtering out unauthorized assets must not invent an unresolved remainder within the selected investor.
- **M6 UI:** dollar/weight split on first screen, all selected root accounts, complete drill tree and security detail where supported; missing finer membership is disclosed, not fabricated. Preserve custody/overlay dates and coverage; refresh/reopen returns the identified revision.
- **M7 Three-firm proof:** modeled, non-model, mixed, missing mapping, shared portfolio/multiple sleeves, subset and signed/cash cases. Actual fresh source-to-published-to-browser evidence for each firm is required for E2E PASS.

Publish INTERFACES/STATUS/evidence/COMPLETION in your base COO deliverables directory `IRPT_MVP_M/`. Handoff to CVO~M names candidate workspace/portal pins, test commands and result paths, accepted source revisions and deployed environment where measured. Surface any missing vendor data capability early with an exact example; continue the other firms and unaffected work. Do not enable schedules merely because the code builds.
