# Model overlay: current ownership snapshot and end-to-end connector brief

Prepared by 4.0.0_SA_CRO on 2026-09-22. Read-only assessment and proposed completion requirements. No application changes, vendor requests, deployment, or schedule activation.

## Product finding

The required product is a current snapshot of an investor's actual holdings, divided into model-associated and non-model assets, with dollar values, weights, and account/security drilldowns. The authoritative model sources are **SmartX for 49 Financial, Black Diamond Rebalancer for Cottonwood, and Eclipse for Inflection**, as Andrew confirmed. Model assignment is an overlay on the complete custody population; the model platform alone must not define which investor assets exist.

The implementation has substantial reusable pieces: three firm-specific snapshot builders, canonical account IDs, a common node contract, snapshot storage/serving, and a mounted holdings tab with summary, tables, and a drill tree. It does not yet deliver this product end to end. The current live serving prefixes are empty, publication is disabled, two firm builders emit no security detail, and the three builders have distinct valuation/classification defects. Enabling publication alone would not close the gap.

A third, explicitly labeled **unresolved** amount is necessary whenever model membership cannot be established. Missing or stale mapping is not evidence that an asset is non-model. Opal versus third-party model ownership, supervisory status, and fee/advisory classification are separate attributes; they must not substitute for model versus non-model membership.

## Current measurement

At **2026-09-22 19:39:15 UTC / 3:39 PM Eastern**, read-only AWS inspection found:

- Deployed `irpt-holdings` uses `entry.lambda_handler`, last modified September 21. The downloaded artifact's digest matches AWS, and deployed `entry.py` and `snapshot.py` match the local files ignoring newline representation.
- The configured `investor-reporting/holdings/` serving prefix contains **zero objects in all three firm buckets**: `opal-data-bd`, `opal-data-cot`, and `opal-data-inf`.
- The `irpt-holdings-snapshot` schedule is **DISABLED**.
- Each firm has a September 11 QA snapshot and pointer under `investor-reporting/qa/holdings/`. These are historical QA artifacts, not evidence of a current production snapshot.

| Firm | What the September 11 QA artifact actually contains | What this establishes |
|---|---|---|
| 49 Financial | 7,461 ACCOUNT nodes, 7,461 MODEL_LEAF nodes, 113,733 SECURITY nodes; 1,584 duplicate node IDs beyond the first occurrences | Security detail exists, but identity uniqueness fails. Account-node count is not a count of unique investor accounts |
| Cottonwood | 971 ACCOUNT nodes; no MODEL_LEAF or SECURITY nodes | The artifact cannot show either the requested model split or security drilldown |
| Inflection | 874 ACCOUNT, 790 SLEEVE, 790 MODEL_LEAF, 130 UNRESOLVED nodes; no SECURITY nodes | Assignment/sleeve structure exists, but security ownership drilldown does not |

Every node in all three QA snapshots has a null `pct_of_total`. Cottonwood's custody date is September 10 and its overlay date September 11; the two dates must remain distinct in the product.

This confirms a missing publication/data path independent of branch or push status. The deployed serving code already matches the examined local code; it has no current serving snapshot to read. This inspection does not establish the exact frontend build currently hosted on PROD.

## Firm-specific adapter map

| Firm / authoritative model connector | Inputs consumed by the current IRPT builder | Existing adapter | What remains incomplete |
|---|---|---|---|
| **49 Financial / SmartX** | `opal-data-assets/smartx/platform/silver/`: allocation-account map, model allocation roster, allocation positions, allocation valuation | Maps allocation/account/model IDs, attaches observed position values, emits account/model/security nodes | Obtain the complete custody account/position universe, including assets absent from SmartX. Preserve allocation/sleeve grain before aggregating accounts. Fix duplicate accounts, missing-model handling, and missing-valuation handling. Prove security membership rather than assign all account value by default |
| **Cottonwood / Black Diamond Rebalancer** | `opal-data-assets/blackdiamond/cottonwood/silver/`: model assignment, blend, roster, and custody holdings facts | Deduplicates custody holdings, expands nested target models, joins assignments and model roster | Complete stable Rebalancer assignment/model-ID mapping; prove actual sleeve/position membership. Emit securities from the holdings already read. Target weight times account value currently produces TARGET amounts, not observed model holdings. Fix total-weight denominator and explicit missing-map coverage |
| **Inflection / Eclipse** | `opal-data-inf/silver/eclipse/`: simple/full portfolios; `silver/api_dims/accounts_v2/` custody account values | Joins accounts to portfolios/models, emits managed sleeves and excluded/unresolved amounts, retains accounts outside Eclipse | Resolve shared portfolio versus account grain; stop repeating portfolio managed value per account. Connect actual custody positions and Eclipse membership at supported granularity. Include excluded assets correctly in totals; establish whether excluded means non-model before labeling it that way |

All three IRPT adapters consume already-landed data. This audit proves the downstream read paths and historical artifacts; it does not newly certify each upstream vendor extraction, authentication session, or current vendor-to-silver refresh. Fresh, complete extraction is a required acceptance check for each named model connector. A model-name match or old QA file is insufficient evidence of that connector being complete.

## Start-to-finish walk

### 1. Header registry -> selected investor -> selected accounts

Use the shared client/relationship/household registry and its account drilldown. Resolve the chosen investor and account subset to canonical IDs server-side. Relationship is the shared business grain despite vendor terminology.

The selected set and the user's entire permitted account universe must remain separate. Holdings currently inherits the same unfinished scope transport as the other tabs: the browser's scope fingerprint is not a resolved account-set ID. Finish this shared connector once and reuse it.

### 2. Vendor extraction -> complete custody holdings and model feeds

The baseline is every holding in the selected custody accounts, with stable account/position IDs, security identity, quantity where supplied, observed value, currency, and source date. Join the appropriate SmartX, BD Rebalancer, or Eclipse overlay onto that baseline.

The current 49F builder starts from SmartX's allocation map, so accounts outside that map cannot become non-model holdings in the result. Cottonwood reads custody positions but does not emit them. Inflection reads account totals and Eclipse portfolio facts but no actual security positions. These are different unfinished connectors, not one generic display problem.

### 3. Vendor IDs -> canonical account, sleeve, model, and security identity

Canonical opaque account IDs and node IDs exist. Complete the joins at their actual economic grain: one custody account can have multiple model allocations; one Eclipse portfolio can reference multiple accounts; the same security can occur in several accounts/models.

Keep source position identity and membership so each holding contributes once to selected custody value. Supply friendly model/security names from the corresponding registries. Cottonwood currently chooses strategy/program names when finding a model roster keyed by model ID; the exact live reference mapping must be reconciled. Its QA artifact's absence of model nodes is observed, but the precise upstream cause was not independently isolated in this audit.

### 4. Joined facts -> actual model/non-model/unresolved ownership

Classify observed assets using supported vendor membership evidence. A model assignment alone does not prove that every asset in that account belongs to that model. Account-level assignments may be displayed at that explicit granularity when the vendor has no finer membership, without inventing security-level attribution.

For 49F, missing model IDs currently still create a model child before the holdout path runs. For Cottonwood, recursive blend expansion preserves unresolved mass and avoids renormalization, which is useful, but its dollar amounts are target allocations. For Inflection, managed and excluded portfolio amounts need both correct allocation to custody accounts and a documented interpretation. Excluded is not automatically confirmed non-model.

### 5. Classified positions -> dollars, weights, and reconciliation

The required invariant is:

**model-associated actual value + confirmed non-model actual value + unresolved actual value = unique selected custody value.**

Show weight of selected investor/account-set total and weight within the current parent, with explicit denominators. Preserve cash, signed values, and currency treatment. A signed or invalid denominator should use the existing table alternative rather than a misleading donut.

Network-free probes of the exact current builder functions confirmed these defects using synthetic inputs:

| Builder | Synthetic input | Current output | Required correction |
|---|---|---|---|
| 49F | One unassigned account worth $100 | Two ACCOUNT nodes with the same account identity, totaling $200, plus a model child | Emit the account once and represent absent membership truthfully |
| Inflection | One portfolio: $100 managed + $20 excluded, associated with two custody accounts totaling $120 | ACCOUNT roots total $200; each account has $120 of managed/excluded children | Allocate/resolve portfolio facts to the actual accounts and reconcile root/child values |
| Cottonwood | Two accounts worth $100 and $300, each entirely assigned to one model | Model weights of total: 100% and 75%, instead of 25% and 75% | Calculate denominators after the complete selected total is known |

These examples prove code behavior, not the monetary size of any customer impact. The 49F historical QA duplicate IDs independently demonstrate a real artifact identity issue.

Current snapshot reconciliation is insufficient: it sums emitted account nodes without deduplicating while declaring custody totals deduplicated, and compares values derived from the same builder. Reconcile against independently enumerated custody positions, not two totals that can share the same error.

### 6. Validated snapshot -> storage -> current publication

The builder supports separate custody and overlay clocks, source revisions, schema validation, reconciliation, and landing. However, `run_firm` computes validation/reconciliation flags and still calls `land`; holdout enforcement follows landing. Publication must be conditional on the required checks succeeding, with an atomic pointer to an accepted snapshot.

Use immutable source revisions that distinguish same-day rebuilds. Establish source freshness and completeness for each firm, preserve both clocks, then publish to the actual serving prefixes. Only after those checks should the recurring snapshot schedule be enabled. A new build timestamp does not make old custody or model data current.

### 7. Selected scope -> holdings API -> correctly projected response

The deployed handler has a placeholder `_no_grant` dependency rather than the real advisor-account grant loader. Its path `accountSetId` is compared with an individual permitted account ID; if it passes, projection uses the entire permitted set rather than narrowing to the requested selection. Complete grant resolution and the account-set contract together.

Projection currently copies node percentages without recalculation. It also uses values dropped by permission filtering as a coverage remainder; those values are not unresolved holdings of the selected investor. Separate excluded scope from within-scope unresolved attribution. Projection's replacement reconciliation, with before equal to after, must not substitute for independent economic reconciliation.

Return a common answer-bearing availability/status envelope. The handler currently returns the projected snapshot directly, whereas the UI expects availability information before showing an answer. Preserve the chosen scope, snapshot revision, custody date, overlay date, and classification coverage through this boundary.

### 8. API snapshot -> frontend adapter -> investor summary

`adaptHoldingsSnapshot` translates nodes, values, and percentages, but drops distinct custody/overlay dates and attribution holdouts/capability facts. It stamps nodes with the common snapshot revision/build time and initializes uncovered accounts as empty. Carry the original source/coverage facts through instead of erasing them.

The summary currently shows total value and account counts; it does not provide the central model-dollar versus non-model-dollar split. Its model account coverage checks direct model children, which misses Inflection's account -> sleeve -> model hierarchy.

The first screen should show selected investor/accounts, total custody value, model-associated dollars/weight, confirmed non-model dollars/weight, unresolved dollars/weight, and both source dates. Model-provider and Opal/third-party labels can be attributes of model detail.

### 9. Summary -> complete holdings drilldown

The drill tree currently chooses the first node with no parent. Builders emit multiple root accounts, so this is not a complete investor-level tree. Add a selected-scope root and a complete navigable hierarchy, such as:

`Investor / selected accounts -> model, non-model, unresolved -> model -> account / sleeve -> security holdings`

An account-first alternative can present the same facts. Show security/ticker, quantity where available, dollars, weight of parent, and weight of selected total. Preserve position ownership while aggregating repeated tickers; never add a model's value to its constituent securities as if they were separate assets. Cottonwood and Inflection need backend security nodes before frontend drill work can complete their paths.

Make snapshot refresh/invalidation explicit; the current tab fetch reacts to firm/scope/revision and has no manual refresh control. This product's critical path is the ownership snapshot, not a performance calculation, sensitivity run, rebalance optimizer, or new export workflow.

## Recommended completion sequence and acceptance

1. Agree the compact common contract: complete custody baseline, actual membership, three coverage buckets, canonical identity, values/weights, and separate source clocks.
2. Repair each firm's adapter at its actual account/portfolio/allocation grain; add missing position membership and security output. Retain useful parsing, target expansion, and existing UI components.
3. Correct uniqueness, denominators, and independent custody reconciliation. Require successful checks before landing or advancing the latest pointer.
4. Finish registry selection, real account grants, selected-set serving, response availability, and frontend preservation of coverage/dates.
5. Complete the dollar split and full investor drill tree; verify a fresh snapshot through the deployed path for all three firms, then activate publication/refresh.

Acceptance must cover fully modeled, confirmed non-model, and mixed investors at each firm; missing/stale mappings; multiple allocations in one account; a shared Eclipse portfolio; selected subsets; cash/signed holdings; and security-level reconciliation. Every displayed value must trace to the selected unique custody population. Known unresolved assets may remain visibly unresolved under an explicit coverage policy; fabricated precision is not an acceptable substitute.

No defensible calendar estimate follows from existing task completion counts. The remaining work is a bounded snapshot product, but economic correctness and connector completeness must precede production enablement.

## Evidence anchors and limits

- `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`: `expand_model`, `build_49f`, `build_inf`, `build_cot`, `build_snapshot`, and `run_firm`.
- `infra/aws/lambda/investor-reporting/holdings/entry.py`: grant dependency, selected-scope handling, load/project/response.
- `infra/aws/lambda/investor-reporting/holdings/snapshot.py`: projection, totals, remainder, and reconciliation.
- `portal/src/pages/InvestorReporting/contracts/adapt.ts`: `adaptHoldingsSnapshot`.
- `portal/src/pages/InvestorReporting/tabs/holdings/`: `HoldingsTab.tsx`, `HoldingsSummary.tsx`, `DrillTree.tsx`, and `slices.ts`.
- Local machine-readable audit: `.runtime/codex-seats/4.0.0_SA_CRO/holdings_product_audit_20260922.json`; aggregate findings reproduced above so they remain in the committed brief.
- Local reproducible synthetic probe and results: `.runtime/codex-seats/4.0.0_SA_CRO/holdings_math_probe_20260922.py` and `.json`. The probe extracts the existing builder functions and substitutes synthetic data readers; it performs zero network calls.
- Workspace HEAD recorded before drafting: `11644be83b9446fb25590d71b9081595a5bc0d8f`. Shared workspace files can advance independently; deployment comparison covers the two named serving files, not every upstream ingestion or frontend artifact.

## Andrew-direct requests — verbatim record

> Now, finally, I want you to create a third brief for the model overlay function. keep in mind the goal of this function, we essentially want to be able to see investor ownership by way of model versus non-model assets. The model view should just be a snapshot of current model versus non-model holdings with drilldowns/weights/dollar value/etc for those holdings.

> Yes so Keep in mind the model data comes from SMartX for 49 Financial, Black Diamond Rebalancer for COttonwood, and Eclipse for Inflection.
