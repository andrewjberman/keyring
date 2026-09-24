# Andrew-direct 2026-09-24 ~04:0xZ at the 1.0.0_SA_CTO terminal -- Anna's page on DEV: random strings, no holdings or model names

Seat: 1.0.0_SA_CTO (Claude).

## VERBATIM

"I want you to read the page that loads for anna so you can see how wonky it is, a lot of very random
strings involved, a lot of missing data, its coming together but dont really understand why we still dont
have holdings and model names pinned down"

## THE PAGE (transcribed from the paste)

Select Firm: Global (All). Client: Thiessen, Anna ****9237 / BROKERAGE. Accounts: acc_0698a3de842dbe7b3d48c787,
acc_d486fc9455d6b2aa18e13af1. Selection: one account; Permitted accounts 1 of 1 in scope (842 permitted);
Scope as of: unknown; Directory as of 2026-09-17; Scope match exact; Cohort (not asserted) supervision:
withheld, advisory: withheld. Holdings: Ready; Business date 2026-09-22; "HOLDINGS_READY [code not defined by
the v1 contract]"; "Classification unknown for 75 of 75 holdings nodes"; cottonwood; Current value USD
19,705,844.84; Unique accounts 1; Source dates Business 2026-09-22 / Observed 2026-09-24T03:49:35Z; Model
coverage 1 of 1 accounts. All Categories / Total Assets $19.71M; one card "1ae61190-70fb-4d6c-a259-cee9019ed125"
$19.71M 100% of total; "This block carries no L1 breakdown for this node."; the node table: one row
"1ae61190-70fb-4d6c-a259-cee9019ed125", basis assigned account, USD 19,705,844.84, 100% / 100%, Supervision
withheld, Advisory withheld, Provenance holdings_snapshot.build_cot.

## WHAT IT ESTABLISHES

1. Anna appears under Global on this load (Finding A's live symptom did not recur here).
2. The re-cut publication is SERVED: 75 nodes for d486 (the re-cut tree), "Model coverage 1 of 1".
3. Every row is an id (node id, model GUID, account id) because the v1 HoldingsSnapshot node contract carries
   NO display name: measured by the CTO -- node properties {node_id, parent_node_id, level, node_kind,
   model_id, security_id, basis, amount, percentages, provenance, drill_refs, classification, clocks,
   valuation_facts}, additionalProperties false; a SECURITY node in 2d067b4d carries security_id
   {CUSIP, 471023879} and nothing readable; a MODEL_WRAPPER carries its name only inside
   capability_facts ("strategy_name=..."). M's label rendering parses those strings and is not on DEV.
4. "HOLDINGS_READY [code not defined by the v1 contract]": the portal prints the reason code on a READY status
   and its named-code list lacks the data codes (row IRPT_BCKEND-S52).
5. "Scope as of: unknown": a resolve-scope field absent for the OPAL_GLOBAL cottonwood scope; measured next.
6. "withheld" columns and "Cohort (not asserted)": the producer's authoritative=false (no Opal supervision
   source resolved for Cottonwood); honest as rendered; enrichment with a data owner.

## RULING IRPT-HOLDINGS-DISPLAY-NAMES-20260924 (CTO 100156)

Additive `display` member on nodes {label, symbol?, description?}; portal validator/adapter accept it FIRST
(in the DEV consolidation, P), then the producer fills it (M: account label, "Rebalancer strategy: <name>",
model_name, sleeve labels, "<symbol> -- <description>" for securities) and republishes; M's render prefers
display.label. P names HOLDINGS_READY / PERFORMANCE_READY and prints no code on READY. P measures "Scope as
of". The category card's coarse "no L1 breakdown" is documented; the drill affordance (67158601) puts the
breakdown one click below. Push state LOCAL at write (origin/CLOUD 9fd480b74f per Y 100161).
