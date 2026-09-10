# Investor Reporting — Holdings and model overlay — WS4 child brief

**Author:** 4.0.0_SA_CRO  
**Mode:** NEW child capability brief within the existing Lightweight Investor Reporting umbrella, D9 Opal Workflows; no separate project registration.  
**Commission:** Andrew's [September 10 direction](../../org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260910_HOLDINGS_MODEL_OVERLAY_V1.md), recorded at `f9761f444f`.  
**Parent:** [Lightweight Investor Reporting](investor-reporting-lightweight-brief-20260910.md), parent O5 / permanent endpoint FWD-5. Child O-n numbers below are local citations, not replacements for ratified FWD IDs.  
**Companion:** [Backend shapes, joins and presentation design](investor-reporting-model-overlay-design-20260910.md); [measured evidence](sources/INVESTOR_REPORTING_MODEL_OVERLAY_EVIDENCE_20260910.json).  
**Consumer:** Andrew's design review; CTO carries this research into the existing umbrella endpoint/PRD; COO owns subsequent decomposition.

The last tab presents **current holdings, led by models**, with pie/donut drilldowns through the existing asset taxonomy. Advisor identity determines the permitted population; the shared header supplies the selected client and accounts. The proposed opening view preserves that client selection. An advisor-book view can use the same unique-account aggregation when its scope is explicitly selected and authorized. Andrew was asked which opening view he prefers; preserving the shared selection is a design recommendation, not a reported answer.

The substantive work is three partner adapters and the account/model/position joins behind them. Existing daily silver provides substantial coverage. It does **not** yet establish complete current advisor bindings or equivalent observed model valuations across all partners. SmartX exposes allocation positions and valuations; Eclipse exposes account/portfolio assignments; Cottonwood's existing decomposition calculates target-based attribution. A common display must retain those meanings.

**V1 excludes time-series views.** It does not add historical attribution reconstruction, performance calculation, drift monitoring, proposed trades or rebalancing. Source revisions remain available for traceability and reproducible snapshots; retaining provenance is not a history feature.

# PART I — THE OUTCOME TERRITORY

### O1 — An advisor opens current holdings for the authorized client or account already selected

The advisor enters **Holdings**, the third tab after Reporting and Analysis, and sees the selected client's permitted accounts, total holdings value, account count and source dates. Changing the client or account refreshes this scope without a second selection workflow. An explicitly selected advisor-book view uses the unique union of permitted accounts, with client/account drilldowns; overlapping relationships never multiply value.

Terminated clients remain visible and marked terminated when the viewer remains entitled, carrying their actual available snapshot date. Termination is not access revocation. This follows CTO Base message 95374 and the parent ratification; this brief neither changes eligibility policy nor grants new access.

**Provable act:** open account, partial-relationship and multi-relationship fixtures; reconcile the visible account set to WS1's scope resolution, including a terminated-but-entitled client. Swap firm/advisor/account identifiers and revoke access against a warm cache; no protected holdings or chart totals become visible. WS1 owns authorization policy; WS4 enforces it for every summary and drill request.

### O2 — An advisor reads model and asset-category percentages with a clear value basis

The advisor sees model allocation first, then Models, SMAs, Client and other applicable categories, with the registered subcategories and members. Every percentage names its denominator and whether its numerator is observed holdings, observed allocation value, assigned-account value or target-based attribution. Actual custody holdings establish the selected scope's holdings total. A target allocation is never labeled an observed model sleeve.

The top-level mix includes the accounted-for remainder. Unavailable classification, unassigned assets and missing model mappings remain distinguishable. A models-only percentage is explicitly labeled as such; it does not replace percent of the client's total holdings.

**Provable act:** reconcile displayed values and percentages to a unique-holdings fixture and each adapter's attribution evidence. Exercise an unknown taxonomy member, cash, a target-based Cottonwood blend, an incomplete valuation and a signed position. No missing amount is silently redistributed and no negative value becomes positive to fit a pie chart.

### O3 — An advisor drills from a category into its models, accounts and securities without losing context

Pie/donut selection reveals the registered subtype and model/strategy composition, then the relevant accounts and securities, with breadcrumbs, consistent colors, value and percent labels, and a readable table equivalent. A model's target constituents are shown as target constituents. Securities actually attributed to that sleeve are shown only when that attribution is evidenced. Where only account assignment is known, the advisor can inspect that account's actual holdings without being told that each security is proven to belong to the assigned model.

**Provable act:** drill an observed SmartX allocation and a target-based Cottonwood blend to their underlying evidence. Parent and child totals reconcile on the declared basis; parent-percent and total-percent remain distinct. Returning to the parent restores the same snapshot and scope. A chart legend/table supports the same selection without requiring color recognition.

### O4 — An advisor accounts for assets outside the resolved model overlay

The advisor can identify which holdings are model-attributed, known Client assets, intentionally unassigned, or not yet mapped/classified. The summary gives both account coverage and value coverage where valuations permit it; unavailable value is not reported as zero. Positions duplicated through relationship memberships count once in the holdings denominator. Parent portfolios, child sleeves and their model constituents are alternative aggregation levels, not additive assets.

**Provable act:** explain the entire unique-holdings total through the attribution and remainder ledger; then introduce a conflicting duplicate, missing assignment, unknown category and multi-account model portfolio. Each produces an explicit exception or partial result without double counting, silent exclusion or fabricated Client classification.

### O5 — An advisor can use current holdings while recognizing an older or incomplete model overlay

Holdings date, model-assignment date, model-definition date and valuation time remain visible at the appropriate level. A missing overlay does not erase otherwise authorized holdings. A carried model assignment is labeled with its original date and freshness state; a newer holdings snapshot does not make that assignment current. Missing, stale, partial and valid-zero are distinct states.

**Provable act:** combine a newer custody snapshot with an older model snapshot, remove one required source, and switch clients during a delayed response. Holdings remain scoped and usable, the overlay's limitations remain visible, and no late result changes the current client's view. Source selection rejects incomplete/conflicting inputs rather than promoting the newest key blindly.

### O6 — An operator explains a displayed allocation and resolves a failed join from its source evidence

An authorized operator can trace a displayed node to the source objects, account/model mapping, taxonomy version, valuation basis and transformation revision that produced it. A repair produces a new validated snapshot and cache revision. It does not rewrite the prior result's source dates or require refreshing the vendor while an advisor searches.

**Provable act:** reproduce one snapshot for each partner from its recorded inputs, identify a deliberately broken mapping, and rebuild after its correction. Published summary and drill data use the same revision; counts, values, exceptions and source fingerprints explain the change. Logs and ordinary monitoring output omit client payloads.

# PART II — WHERE THE BOUNDARY SITS

### II.1 Ownership within the one umbrella

**WS4 owns** partner model-overlay adapters, source selection for its snapshot, account/model/position attribution, valuation and taxonomy semantics, reconciliation, provenance, derived holdings projections, and the Holdings tab's content and drill behavior.

**WS1 owns** cached client discovery, firm/advisor identity binding, entitlement and selected account-set resolution, shared navigation, panel primitives, common lifecycle and shared export infrastructure. WS4 consumes its versioned scope contract and rechecks authorization on delivery. Advisor ID supplied by a browser is not authority. The source mappings described here inform WS1; they do not create a second identity system.

**WS2 owns** performance and its branded PDF/narrative content. **WS3 owns** YCharts intake, generation and sensitivity analysis. This brief does not expand the current commission into a new Holdings-specific PDF template. Any later Holdings export must reuse the shared scope and snapshot contract.

### II.2 Named prior art and adjacent owners

| Existing territory | Reuse / seam | Boundary preserved |
|---|---|---|
| **D1_CATVIEWS** and the D1 Asset Category Views PRDs | Registered category tree, display partitions, drill conventions and canonical model colors | Existing global page totals are not client-level holdings or entitlement evidence |
| **D3_MODELOVERLAY**, `D3_ACCOUNT_MODEL_OVERLAY_PRD.md` | Account-model grain, SmartX/Schwab joins, multi-membership cautions and value reconciliation | This child does not require completion of the older full feed migration to deliver a bounded current view |
| **OPAL_ASSETS** | Complete vendor silver, partner acquisition and schema contracts | WS4 business attribution belongs in derived gold; raw silver stays vendor-complete |
| **ADVI_ECLDAT** | Eclipse portfolio/model and Orion account/representative join precedent | Adapter must bridge actual current camelCase silver and legacy snake_case schemas explicitly |
| **WSE_COTMDL** | Rebalancer roster, assignments, recursive model composition and account-level aggregation | Target-based attribution retains that label; source repairs belong with the producer |
| **MDPF3FIRMS** | Shared category registry, canonical model identities and existing decomposition helpers | Do not copy firm-level model AUM into client totals, silently adopt page-specific exclusions, or create a competing registry |

The established movement remains complete source silver → business joins in gold → publisher-produced platinum serving projections → authorized API/UI. Existing pure transformation functions are candidates for reuse. A lightweight derived cache is not a license to put business logic into silver or introduce another stored serving-JSON writer.

# PART III — THE QUALITATIVE BAR

1. An advisor can identify the client's model mix without opening a vendor's model-management screen.
2. The first chart answers what the percentage is **of**, and whether it is observed or assigned.
3. A drill reveals the underlying explanation; it does not substitute firm-level model totals for the selected client's assets.
4. Missing attribution is more informative than a plausible but unsupported Client slice.
5. The interface reuses the portal's panels, colors and interaction patterns while honoring Andrew's pie/radial direction.
6. A holdings refresh cannot conceal an older model assignment or erase an entitlement change.
7. An operator can explain a value difference with source and mapping evidence instead of reverse-engineering the chart.

# PART IV — THE SUBSTRATE

### F1 — Current holdings and model sources are present, but their clocks differ

Read-only S3 inspection covered six named silver roots, **19 selected Parquet datasets in `opal-data-assets`**, and **four identity tables in two legacy firm buckets**. All 23 downloaded objects matched their recorded byte sizes and SHA-256 fingerprints on offline replay. They total 15,753,977 bytes. Source census and snapshot reads were measured September 10 at 17:27–17:36 UTC; exact clocks, schemas and keys are in the evidence manifest.

Latest independently observed holdings partitions were September 9 for Schwab 08335338 and Cottonwood, September 10 for Orion. SmartX and Eclipse selected partitions were September 10. Cottonwood's four Rebalancer tables were all **August 30**. These are measured source vintages, not a certified common completed snapshot or whole-pipeline freshness result.

### F2 — SmartX provides a substantial join and an observed-allocation substrate

Schwab 08335338 has 104,807 holdings rows across 6,237 holding accounts. Of 7,453 SmartX allocation/account map rows, 7,431 join the 08335338 account table through its declared eight-digit-to-ten-digit account-number normalization, covering 5,856 distinct accounts. All joined allocations have valuation rows; 7,402 have position rows. The separate `fact_account_allocations` table is empty and cannot be the sole bridge.

The existing `b04_account_model_membership.py` supplies useful join/status logic but explicitly marks advisor aggregation unavailable. The named legacy 49F group/account bridge's only observed dated partition was August 18: all 29,907 `is_primary` values were null. This corroborates a gap at that inspected home; it does not prove no newer advisor mapping exists elsewhere. Primary attribution is distinct from authorized visibility over a deduplicated account set.

### F3 — Eclipse needs both catalogs and explicit account scope

Orion positions contain 35,974 rows across 953 accounts. The parallel assets table matches those rows on position ID, account, product, value and shares; adding both feeds would double count. Eclipse simple portfolios contain 845 rows; all 790 populated account IDs join Orion holdings. Of 663 populated model assignments, **658 resolve against the union** of the 18-row models and nine-row composition catalogs after normalizing declared integral IDs. Five remain unresolved. A catalog name match does not prove full constituent coverage.

The full portfolio table has 858 rows, including 13 multi-account portfolios absent from the simple table. Their total values cannot be repeated for every child account. The inspected September 10 legacy account dimension contains 874 accounts, all with holdings, household IDs and representatives in the current 19-row representative roster. The other 79 Orion holding accounts are outside this inspected identity dimension; their reason and authorized population require resolution. This source roster is not a tested login-to-advisor binding.

### F4 — Cottonwood's existing overlay is target-based, with a stale assignment source

Cottonwood holdings contain 18,917 rows but 18,817 unique account/asset keys: 100 duplicated keys through the relationship-grain source. All duplicate keys agree on market value in this snapshot. The existing helper checks value agreement before collapsing; the new drill contract must also preserve the relevant units/date agreement.

Of 950 August 30 assignment rows, 946 join the September 9 holdings account universe; 23 of the 969 holding accounts have no assignment row. All 464 named assignments resolve uniquely to a roster name under the measured whitespace normalization. The model sources contain 65 roster rows, 118 blend edges and 1,595 definition rows. Existing decomposition multiplies account holdings value by recursive target weights. It does **not** measure the executed holdings of a model sleeve. Parent/leaf Opal membership handling and the newer Cottonwood SMA mapping are reusable; old “49F-only SMA” assumptions are not.

### F5 — The taxonomy and radial UI can be reused with explicit semantics

`mdpf_category_registry.py` separates stored categories from display groups and gives Client two alternative partitions: fee-taking and advisory. These must not be drawn as additive sibling partitions. Unknown registered-member lookups are errors, not automatic Client residual. The Opal fee-taking predicate is not interchangeable with a vendor's supervised flag.

`CategoryViewTree.tsx` provides panels, declared children, canonical model colors and unavailable states. Existing Advisor Intelligence components contain donut/drill precedents. One inspected donut uses absolute values; that behavior cannot be inherited for signed holdings. No portal was run or visually graded in this research.

# PART V — WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

These are dependencies, not a task sequence.

- **WS1 scope binding:** current authenticated advisor/firm → permitted unique accounts, relationship intersections, termination visibility and revocation behavior. Resolve the measured 49F and INF identity gaps without treating missing identity as broad access.
- **Source producer contracts:** completed-snapshot selection, business/value dates, required table availability and explicit carried-source behavior. Cottonwood needs its older model-source state explained or refreshed by its owner; this brief does not assert the cause.
- **Value and attribution contract:** custody price/cash/accrual/currency basis, SmartX allocation reconciliation, Eclipse multi-account membership and managed/excluded values, Cottonwood target-weight semantics. Unknown values and signed exposures remain representable.
- **Taxonomy ownership:** versioned canonical member maps, current per-account Client predicates, registered SMA/alternative mappings, and unresolved-member handling. The 08335338 scope does not automatically include the separate 08242234 custody master.
- **Publishing and cache integration:** established gold/platinum ownership, immutable source/scope/taxonomy revision binding, authorized delivery and consistent summary/drill invalidation. Measure runtime/payloads before selecting Lambda limits, refresh TTLs or performance targets.
- **Representative validation:** each partner's ordinary assignment, unassigned assets, blends, overlaps, source lag, missing values and malformed keys; a current advisor-scope sample and expected memberships. No invented monetary tolerance or coverage threshold is ratified here.

# PART VI — STATUS — NOT OUTCOME-BEARING

At the September 10, 2026 evidence cut, this is a research and proposed-design delivery. Direct source measurements are timestamped at 17:27:01 UTC (prefix census), 17:28:57 UTC (silver snapshot profile), and 17:36:14 UTC (legacy identity profile); the evidence JSON records the later offline replay clock and current source fingerprints.

Delivery checks passed: all 23 private object hashes/sizes on replay, 23 repository source fingerprints, the cited structural join counts, all seven brief parts and six local outcome headings, 25 local links across the child/parent documents, and Python syntax. A bounded scan against private account/allocation/household identifiers and long account/advisor names found no matches in the new deliverables. This is artifact validation, not a production data or authorization test.

Andrew's scope record was committed at `f9761f444f`. CTO Base message 95374, received at 17:36:40 UTC, reports all eight parent outcomes ratified and supplies the terminated-client visibility ruling. This child neither edits nor renumbers that endpoint. No new project code, task order, source data, cloud resource, API or portal page was created by this brief. Publication state belongs to the delivery receipt's measured `origin/CLOUD` ancestry, not to this status paragraph.

# PART VII — WHAT THIS BRIEF DOES NOT CLAIM

1. Key-join counts are not monetary reconciliation, current permission verification, complete taxonomy coverage or model-definition completeness.
2. Independently newest partitions do not prove same-day economic alignment. SmartX's intraday valuation clock and prior-day custody values require explicit treatment.
3. Four inspected legacy identity prefixes are a bounded sample, not proof that the required identity data is absent estate-wide or all present in `opal-data-assets`.
4. No live vendor request, cloud mutation, trading action, served API test, cross-firm security test or UI usability test was performed for this child.
5. Existing source code is prior art, not proof that its current deployed output meets this new view. The compiler's held freshness configuration was not overridden; no compiler freshness certification is claimed.
6. Current account assignments and model targets do not establish historical ownership, realized performance or actual per-security model attribution.
7. The advisor-book opening default remains a proposed alternative pending Andrew's preference. The shared selected-client default keeps the established three-tab interaction coherent without blocking the backend design.

## REFS TO CARRY

```text
BRIEF PATH       docs/briefs/investor-reporting-model-overlay-brief-20260910.md
DESIGN           docs/briefs/investor-reporting-model-overlay-design-20260910.md
EVIDENCE         docs/briefs/sources/INVESTOR_REPORTING_MODEL_OVERLAY_EVIDENCE_20260910.json
REPRODUCTION     docs/research/investor_reporting_model_overlay_20260910/profile_snapshot.py
PROJECT          Existing Lightweight Investor Reporting umbrella, D9; use CTO L3 code, no child registration
EXISTING PRD     Umbrella PRD is CTO-owned; D1/D3 documents in II.2 are prior art, not this child's PRD
PARENT OUTCOME   Parent O5 / permanent FWD-5; shared FWD-1/FWD-2/FWD-6/FWD-7 seams retained
SIBLINGS         WS1, WS2, WS3; D1_CATVIEWS, D3_MODELOVERLAY, OPAL_ASSETS, ADVI_ECLDAT, WSE_COTMDL, MDPF3FIRMS
PRIOR ART        F1-F5, companion design and source-list.json with targeted read scopes
MEASURED AT      Individual UTC clocks and fingerprints in evidence; current facts qualified in VI/VII
```
