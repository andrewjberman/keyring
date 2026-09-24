# ANDREW-DIRECT 2026-09-23 ~19:4xZ (~15:4x ET) -- IRPT Holdings uses the Opal taxonomy; Client is the plug

**Received by:** `4.0.0_SA_CRO~M`, at its own terminal, answering four numbered questions this seat put to
Andrew after its read-only deep dive of the Investor Reporting Holdings tab (same session).
**Recorded same turn per `org/XXX.md`.** Scope is NOT adjudicated here; the scope change is routed to
`1.0.0_SA_CTO`, owner of `org/tier1_exec/1.0.0_SA_CTO/deliverables/IRPT_MVP_COMPLETION_20260922/CONTRACT.md`.

## The four questions, verbatim as put to him (his answers are numbered replies to these)

> 1. Should the Opal taxonomy (Models / SMAs / Client, plus an "Unresolved" bucket) be the top level of Holdings?
> 2. Do third-party-model assets go under Client?
> 3. Should I run a check on each firm to see whether its model platform identifies SMAs?
> 4. Should this go to COO~M through the CTO as a scope addition?

## His answer, VERBATIM -- the phrasing is the ruling

> *"1.) Client is the plug figure so no need for "unresolved"; yes this should absolutely be included. 2.) Yes.
> 3.) Yes, this only applies for SmartX for 49 and Black Diamond Rebalancer endpoint for Cottonwood. 4.) Yes."*

## What it rules (restated only to index it; the quote above governs)

1. The Holdings view is placed in the Opal taxonomy: L0 **Models / SMAs / Client**, with the ruled L1s
   (Models: Primary {UST, ST, INT, LT, ULT} / Custom; SMAs: ETF Strategies {PFOE, DIVZ, IDVZ, PFDE} /
   ALT Strategies {Tax, Muni}; Client: Opal Supervised / Opal Unsupervised).
   **Client is the plug** (custody total minus Models minus SMAs). There is **no separate "Unresolved" bucket.**
2. Assets in **third-party (non-Opal) models go to Client.**
3. SMA identification applies **only** to SmartX for 49 Financial and the Black Diamond Rebalancer for
   Cottonwood (Inflection is not in this check).
4. The addition is routed to `2.0.0_SA_COO~M` **through `1.0.0_SA_CTO`** as a scope addition.

## Question 3 -- the check, run this turn (read-only, landed Opal S3 silver, zero vendor calls)

Source partitions: `s3://opal-data-assets/smartx/platform/silver/fact_model_allocation_roster/date=2026-09-23/`
and `s3://opal-data-assets/blackdiamond/cottonwood/silver/{fact_model_roster,fact_model_assignment,fact_model_blend}/date=2026-09-23/`.

**49 Financial / SmartX -- SMAs ARE identifiable, by SmartX model id (not by any type flag).**
7,497 open 49F allocations of 10,077 roster rows, 7 distinct models:

| SmartX model name | model_id (prefix) | open allocations | value (USD) | taxonomy |
|---|---|---|---|---|
| Opal Long Term | 74c119db | 3,456 | 812,052,995.67 | Models > Primary (LT) |
| Opal Intermediate-Term | 729210dd | 1,639 | 299,567,516.30 | Models > Primary (INT) |
| Opal Ultra Long Term | 69cc5e3b | 1,417 | 206,331,404.01 | Models > Primary (ULT) |
| Opal Short-Term | 0f76a5a0 | 729 | 106,984,197.90 | Models > Primary (ST) |
| Opal Ultra Short-Term Income | c000fe6a | 176 | 45,874,439.02 | Models > Primary (UST) |
| Opal Dividend Income | 48af6559 | 38 | 17,222,805.22 | SMAs > ETF Strategies (DIVZ) |
| Pathfinder Focused Opportunities | 843d875b | 42 | 4,078,067.11 | SMAs > ETF Strategies (PFOE; SmartX shows the fund name) |

Total open 49F SmartX value 1,492,111,425.23. The id-to-taxonomy map already exists and is certified in
`data/mdpf/scripts/gold/mdpf_revamp_model_crosswalk.py` (`cohort_class` "model"/"sma") and
`data/mdpf/scripts/gold/mdpf_category_registry.py` (`PRIMARY_MODEL_KEYS`, `SMA_MEMBERS`). **No Tax, Muni, IDVZ or
PFDE model exists in 49F SmartX.**

**Cottonwood / Black Diamond Rebalancer -- the Rebalancer's own SMA flags identify NOTHING; one Opal SMA is
identifiable by model name.**
- `fact_model_assignment.is_sma` and `allow_sma` are **False on 973 of 973** assignments (every other flag
  column likewise all False).
- `fact_model_roster`: 65 models, every one `rebalance_model_type = Strategy`, `provider = Firm`; 23 carry
  `is_opal = True`. Exactly ONE SMA-named Opal model: **"Opal Pathfinder Disciplined Equity SMA"** (4 accounts),
  whose blend child is "Pathfinder Disciplined US Equity" at 100% -> **SMAs > ETF Strategies (PFDE)**.
- The "Core | Satellite (CA) Tax-Free NN" models are `is_opal = False` -> third-party -> **Client** per answer 2.
  "Opal Moderate Income Portfolio (Tax Efficient)" is an Opal model, not an SMA.
- Assignment -> model link is by NAME: 473 of 973 assignments carry a strategy, 500 carry "--" (no model);
  **473 of 473 match a roster `model_name` exactly (trimmed), and the 65 roster names are unique** -- so the join
  is unambiguous on this date. There is no model_id on the assignment row.
- Opal "Satellite" models are **blends of the Primary models** (`fact_model_blend`): e.g. Opal Satellite 50 =
  75% Opal Intermediate-Term + 25% Opal Short-Term; Opal Satellite 80 = 100% Opal Conservative Growth; Opal Ultra
  Short Term = 100% Opal Ultra Short-Term Income. Some blends mix Opal children with non-Opal sleeves
  (e.g. Blended Opal / Satellite 50).

## SURFACED, NOT ADJUDICATED -- for `1.0.0_SA_CTO` (contract owner) and, where marked, Andrew

- **(a) Contract collision.** CONTRACT v1.3 S2 and COO_M.md M3/M6 require "model + confirmed non-model +
  unresolved". Answer 1 replaces that partition with Models + SMAs + Client (plug). Contract text is the CTO's.
- **(b) Unknown VALUES are a different condition from unattributed MEMBERSHIP.** The plug absorbs assets not
  attributed to Models/SMAs; it does not supply a value that the custody source leaves blank (e.g. COO~M measured
  5,694 blank Cottonwood Market Value rows and no currency column). How the plug treats an unknown custody value is
  open.
- **(c) 49F Tax SMA -- question for Andrew.** The Tax SMA is sourced today from a SharePoint workbook
  (`org/standards/MDPF_TAXSMA_DATA_CONTRACT.json`, reporting master 0008335338), not SmartX. Read literally,
  answer 3 puts Tax SMA dollars in Holdings under **Client**, while Model Portfolios shows them under
  SMAs > ALT Strategies > Tax (registry basis `additive`, 5 accounts, in the 0833 master and not the 0824 one).
  If Holdings' 49F custody base is the 0833 master (Andrew's word to COO~M today), those accounts are inside the
  population either way; only their label differs.
- **(d) Cottonwood Primary/Custom placement needs the blend expansion** (Opal parent -> Primary children; non-Opal
  sleeves -> Client), and model dollars there are an ASSIGNED/TARGET-weight split of account value, not observed
  positions -- COO~M's 2026-09-23 decision 4 (targets never presented as observed holdings) bears on this.
- **(e) Taxonomy source.** Read from the MDPF registry + crosswalk (one carrier). The Holdings builder
  (`data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`) declares a stale five-value list
  (`models, strategy, alternative, insurance, client`) that nothing uses, and writes every node's
  `classification.hierarchy_path` empty and `fee_taking_status` UNKNOWN (measured on CLOUD and on
  `codex/irpt-m-completion` @35999d31a4).

## Evidence of the prior state (same session, read-only)

No holdings snapshot published in `opal-data-{bd,cot,inf}` (legacy prefix and `irpt/`) or
`opal-data-{49financial,cottonwood,inflection}/irpt/` (positive control: 2 objects under
`opal-data-bd/investor-reporting/qa/holdings/`); `irpt-holdings-snapshot` schedule DISABLED; `irpt-holdings`
Lambda last modified 2026-09-21T15:04:24Z. The portal Holdings summary (`portal/src/pages/InvestorReporting/tabs/
holdings/HoldingsSummary.tsx`, unchanged since 2026-09-12) shows no model/non-model dollar split.
