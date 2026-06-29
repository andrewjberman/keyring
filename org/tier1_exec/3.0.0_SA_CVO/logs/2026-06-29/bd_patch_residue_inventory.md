# BD-Patch Residue Inventory -- the DATA_SSOTMG TO-2 cleanup worklist (CVO pre-sweep for 06-30 AM)

**archetype:** TRACE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-06-29 | **For:** 1.0.0_SA_CTO (TO-2 audit+purge worklist + TO-1 advisor-dim question) | cc COO, DS, base-DS
**Scope:** the NEW custodian-native pipeline data/canonical/schwab/{silver,gold}/*.py (14 gold + the dim/fact silver). The OLD BD-SSOT pipeline (data/black_diamond/scripts/gold/B_*) is being SUPERSEDED, not cleaned.

## Headline: the financial core is ALREADY custodian-clean; the only real BD-dependency is the ADVISOR-SPLIT layer
The custodian-native gold scripts mostly already PURGED the BD patches (the matches are "we REPLACED the BD patch" comments, not live BD logic). The one genuine residual BD-DATA dependency is the advisor-split/attribution cluster -- because advisor splits ("who gets credit", architect/implementor) are BD-proprietary, NOT in the custodian feed. That is exactly CTO's TO-1 open question.

## GREEN -- custodian-native, CLEAN (verify-only; no purge needed)
These read the canonical Schwab silver (fact_position/fact_lot/fact_flow) + explicitly state they replaced the BD patch:
| Gold surface | Evidence it's clean |
|---|---|
| build_gold_holdings | "pure RPS, NOT a B_00 schwab_override / bd_stale-zeroed / reconcile-patched figure" -- PROVEN 0/5892 $0 vs rps |
| build_gold_canonical_lots | provenance schwab_lot_native -- PROVEN 0/3793 $0 vs uln |
| build_gold_realized_gains | schwab_realized_lots_multi_source (custodian rld + history) |
| build_gold_firm_composition | rps x security_master (custodian) |
| build_gold_client_performance / client_tax_liability / portal_aggregates | custodian-derived |
-> TO-2 action: VERIFY-ONLY (confirm no BD key in the read paths); no purge.

## AMBER -- a former BD-patch was REPLACED; verify the replacement is custodian-grounded
| Surface | The replacement | Verify |
|---|---|---|
| build_gold_account_gains | "REPLACES the misguided 90-day activity flag" -> excises rows flagged is_aberration in fact_transaction (counted, never silent) | confirm fact_transaction.is_aberration is CUSTODIAN-grounded (a clean custodial rule), not a ported BD heuristic |
| build_gold_canonical_nna | "sb-grounded flow classification that REPLACED the 49F 90-day-activity patch" | same: confirm the flow classification is custodian-sourced |
| build_dim_account | "the A_04 inferred-tax 'patch' is the proper derivation here" | confirm the inferred-tax is a clean derivation, not a BD carry |
-> TO-2 action: read each replacement; confirm the input is a custodian fact, not a BD-ported rule. Likely clean (the comments assert it) -- VERIFY + bless.

## RED -- genuine BD-DATA dependency (the advisor-split cluster) -- TO-1 architectural question, not a simple purge
The advisor SPLIT base (architect/implementor allocations + fee splits) is BD-PROPRIETARY -- the custodian's acc+account_xref gives advisor/relationship/tax_status, but NOT the split allocations. So these carry a "BD-base" with Andrew-curated overrides on top:
| Surface | BD-dependency |
|---|---|
| build_dim_advisor_role | the SPLIT base = "BD-base splits"; Andrew-curated advisor_split_overrides.csv override-wins on top; reject->"reverted to BD-base" |
| build_dim_advisor_fee | the fee-split tabs (BD-proprietary fee allocations) |
| build_gold_advisor_attribution / advisor_fee_efficiency / advisor_split_reconciliation / partner_analytics | all consume the advisor-split base |
-> TO-1 action (CTO's flagged question): the advisor-split/type layer is intrinsically non-custodial. Decision = make it a FENCED curated dim (a thin BD-metadata tether: advisor splits/types + the curated-override layer), explicitly NOT in the custodian core and NOT in the surplus BALANCES -- a third category: "fenced curated metadata." It rides ON the custodian core (keyed by Schwab account) but its SOURCE is BD+curated. This matches CTO's TO-1 framing exactly (fold into dim_advisor from a thin BD-metadata source, fenced).

## The clean 3-way fence (the model the inventory implies)
1. CUSTODIAN CORE -- positions/lots/flows/derived financials. Custodian-native, exact (proven), gated by comp-parity correctness track. (GREEN + AMBER-verified.)
2. FENCED CURATED METADATA -- advisor splits/types/fees. BD+Andrew-curated source, keyed onto the custodian core, explicitly fenced + labeled (NOT custodial-exact, NOT a balance). (RED.)
3. SURPLUS NON-CUSTODIAL BALANCES -- the held-away/non-Schwab account balances. BD-sourced, quality-tolerated, fenced. (the ~$269.5M staple.)

## TO-2 worklist (what to actually touch 06-30)
- VERIFY-ONLY (no purge): holdings, lots, realized, composition, client_performance, client_tax, portal_aggregates.
- VERIFY-THE-REPLACEMENT: account_gains, account_performance, canonical_nna, dim_account (confirm the ex-patch input is custodian-grounded).
- TO-1 DECISION (Andrew/CTO): the advisor-split cluster -> fence as curated metadata (category 2). NOT a purge -- an architectural placement.

## grounding: field (Rule 22)
- "the financial core already purged the BD patches" -- SOURCE-CONFIRMED (the in-script comments + the proven rps/uln ties; build_gold_holdings:17, account_gains:7-9, canonical_nna:7).
- "the advisor-split base is BD-proprietary / non-custodial" -- SOURCE-CONFIRMED (build_dim_advisor_role:199-240 "BD-base splits", the advisor_split_overrides.csv curated layer) + the custodian feed lacks a split field (acc/account_xref carry advisor identity, not credit-allocation).

## Compiler Tools
| Tool | Run | Result |
|---|---|---|
| comp-glob | locate canonical/schwab scripts | 14 gold + dim/fact silver |
| comp-grep | BD-patch/residue scan + real-dependency vs comment split | the 3-bucket inventory (GREEN/AMBER/RED) |

-- 3.0.0_SA_CVO
