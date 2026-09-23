# Holdings: firm journeys and current implementation decision

Owner: 2.0.0_SA_COO~M. Recorded 2026-09-23; source baseline 1fd1c8f0fb.
Authority: Andrew's direct Codex user message below, and the existing IRPT closer
CONTRACT.md / COO_M.md. No new round or general research project.

## Andrew-direct instruction (verbatim)

Channel: Codex user message, received during the September 23 session; exact
message timestamp unavailable. Recorded after the 19:27 UTC source inspection.

> For 49 Financial, their model data is in SmartX, they do not have model data outside of SmartX, we can use the 0833 account as a base for opal-data-assets for them, but that account does exceed smartx assets. Explain to me the issue with Cottonwood beter. Inflection also need to figure out. If you were to structure a workflow here to cut through the middle and make it to a functioning journey per firm, what would you need to have happen? Are you capable of making that plan right now or are there things that you still do not know, for which you could benefit from targeted research? We need to get this driving again and you are the agent responsible for this journey so need to make decisions now and proceed to implementation .

## Decisions

1. First live candidate: an Inflection account with reconciled positions and a
   single unambiguous Eclipse membership. Fresh research below establishes a
   stronger immediate data path than Cottonwood. Cottonwood's actual-tree code
   is the first implementation candidate; finish its source bindings alongside
   49 Financial's 0833 custody adapter. All three remain required. Research is
   limited to facts that change an adapter.
2. Every journey starts from unique actual custody positions and an independently
   selected account census. Model platforms are overlays, never the population.
3. 49F: the 08335338 custody master is the authorized baseline; SmartX is the sole
   model authority. Missing SmartX coverage is retained in custody. Exact source
   coverage determines confirmed non-model versus unresolved, not a second model feed.
4. Cottonwood: do not multiply account value by Rebalancer target weights and
   present it as observed model holdings. First expose validated custody securities
   with unresolved attribution; add account/sleeve membership only when evidenced.
   Preserve targets as a separate basis, not an additive actual-holdings partition.
5. Inflection: Orion positions supply custody; Eclipse supplies model membership.
   Shared portfolio values are never repeated or allocated proportionally without
   source evidence. Unknown membership does not suppress known custody securities.
6. Unknown values are not zero; signed positions are retained. Missing mapping
   and missing custody value are different conditions. A blocked account must not
   silently disappear or poison unrelated independently accepted accounts.

## Short execution sequence

| Step | Owner | Deliverable / stopping condition |
|---|---|---|
| Actual-position adapter | M | Existing public node contract, full selected custody tree, independent reconciliation; no targets relabeled as actual |
| Targeted source checks | M | COT currency declaration, null-value coverage and assignment key; INF position identity/account join and effective dates; 49F signed custody/cash tie and SmartX coverage |
| Wire and package integration | P, M supplies exact pin | Current status projection, selection/grants, accepted reader, matching dependency/IAM bundle; one callable real Holdings entry |
| Holdings presentation | M; P integrates shared adapter | Actual total, model/non-model/unresolved split, all selected account roots, security drill, both source clocks |
| One real Inflection account | M drives; P shared runtime | Reconciled custody, unambiguous Eclipse membership -> accepted publication -> authorized API -> real-login rendered screen, exact trace |
| Extend and exercise | M | Model/mixed/non-model/unknown/subset/signed cases, then equivalent 49F and INF journeys |

Publication and deployment are prepared as exact candidates and routed through
existing owners/gates; no schedule activation merely because tests pass. Existing
canonical private storage and contracts are reused. Security-reference services,
analysis/export enrichment and unrelated registry work are off this critical path.

## Measured blockers, not yesterday's assumptions

19:19 UTC: deployed legacy serving prefixes empty in all three firm buckets;
canonical accepted current indexes also absent. Scheduler remains DISABLED.
Deployed irpt-holdings artifact remains September 21 (previous incident capture).

19:27 UTC read-only exact-version source capture (private runtime evidence:
`.runtime/holdings-journey-20260923/source_audit.json`):

- COT holdings date September 22: 19,610 relationship-grain rows; 5,694 null
  Market Value rows. No Currency column. Independent account totals have no
  Currency column either. Null rows are not unique positions/accounts.
- COT assignments September 23: 973 rows, strategy/program names but no model_id;
  roster has 65 model IDs/names. Direct name-to-ID lookup remains unproven.
- INF September 23 partition: 36,044 position rows, source position id/product_id,
  account_id and current_value available; asset_level_strategy_id entirely null.
  A dated partition is not proof of current economic valuation dates.
- Eclipse simple: 844 rows, 58 missing account_id and 181 missing model_id;
  full portfolios: 858 rows, 195 missing model_id. Join/membership needs measurement.

Fresh five synthetic economic regressions pass at baseline. They do not establish
source acceptance or a deployed journey. M7 remains NOT_EVALUATED live.

## Targeted source results and first implementation

- COT has 981 unique custody accounts: 405 have no null Market Value row;
  576 have at least one. These are source completeness counts, not acceptance.
  The exact Bronze vendor workbook contains the same 5,694 blank value cells;
  currency is absent there too. Do not fix the silver parser by inserting zero.
- 971 of 973 Rebalancer external IDs match custody. Strategy name matches zero
  model IDs and 473 unique roster names. This proves the current lookup is wrong;
  name similarity alone is not a newly authorized model-membership rule.
- All 876 INF account-source accounts have positions and their summed values tie
  to account values within one cent. Positions include 82 additional accounts
  outside that account file; their boundary must be resolved, not silently dropped.
- Full Eclipse declares 14 multi-account portfolios. The flattened simple file
  exposes only one account per portfolio, so those 14 are a specific incomplete
  membership connector. Other portfolios can form the first bounded live case.

First code candidate: build_cot now emits ACCOUNT -> UNRESOLVED -> SECURITY over
validated actual rows. Equal relationship copies collapse only after existing
strict controls; signed/zero positions and separate same-ticker assets survive.
Target nodes stay private in the manifest, not the public actual tree. The
existing public schema is unchanged. Native quantity/name presentation still
needs the shared adapter contract; no field was invented to bypass that step.
Missing source currency/values still refuses. This is not current real admission.
68 economic tests and the full 180-test Gold suite pass.
