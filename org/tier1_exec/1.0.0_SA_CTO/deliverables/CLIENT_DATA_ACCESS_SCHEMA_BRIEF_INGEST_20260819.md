# CLIENT DATA ACCESS SCHEMA BRIEF -- INGESTED 2026-08-19 ~18:57Z (Andrew-direct at the CTO terminal)

**Delivery (verbatim):** *"C:\Users\AndrewBerman\Downloads\client_data_access_schema_brief (1).docx
I FORGOT TO GIVE YOU THIS, THIS IS GOING TO BE A CRUCIAL COMPONENT OF OPAL_ANALYST PROJECT"*
**Stored:** the .docx byte-copy sits beside this file
(`CLIENT_DATA_ACCESS_SCHEMA_BRIEF_20260819.docx`); full text extract in section 3 below
(word/document.xml extraction, 6,099 chars). **This CLOSES the D6/S5 open input slot** ("partner
GraphQL spec file -- pending"): D6's U1 BLOCKED-INPUT is discharged; the schema workstream
unblocks per the brief's own §10 initial scope.

## 0. SCOPE QUALIFICATION (Andrew-direct, same terminal, minutes after delivery -- BINDS the phasing)

VERBATIM: *"SOMETHING I WOULD QUALIFY ABOUT THIS IS THAT THE FIRST THING WE NEED TO COVER HERE IS
THE BASIC GRAPHQL TOOLING/LAYER, THE PARQUET ANALYSIS IS A NICE TO HAVE, SOMETHING WE ULTIMATELY
WILL SURELY DO, BUT THAT IS A DISTANT SECOND PRIORITY COMPARED TO THE THING TOOLING YAML LAYER FOR
ADDRESSING THE SURFACES WE HAVE BEEN PLUGGING THE BBG AGENT INTO. THE DEEP PARQUET ANALYSIS STUFF
IS SOMETHING THAT WILL COME LATER AS WE FINISH THE PARQUET STRUCTURING FOR THE CLIENTS (POST THE
FULL ADVISOR INTELLIGENCE REFACTOR WORK), THIS WILL REQUIRE A LOT OF EFFORT AND THOUGHT AS IT
TOUCHES CLIENT DATA, AND ITS 100% GOING TO BE SOMETHING WE WANT TO DEVELOP INTERNALLY FIRST FOR
OUR OWN FABRIC'S USE TO TEST OUT VERSUS TRYING TO TEST IT ON THE BG AGENT OUT THE GATE."*

**Scope reading (three rules):**
1. **PHASE 1 = the GraphQL TOOLING/YAML LAYER over the surfaces the BBG agent already consumes**
   -- the JSON/operational plane + the D6 W5 tooling-yaml index binding. The brief's schema +
   5-tool surface land HERE first.
2. **PHASE 2 (distant second) = the deep parquet-analysis plane** -- gated on the client parquet
   structuring finishing (POST the full Advisor Intelligence refactor); client-data-sensitive,
   heavy design effort.
3. **INTERNAL-FIRST LAW for phase 2:** developed for OUR OWN FABRIC'S use and tested internally
   BEFORE any exposure to the BG agent -- never tested on the client-facing agent out the gate.

## 1. What the brief specifies (faithful summary)

Two planes, deliberately separated:
- **CLIENT plane:** natural-language agent -> intent + ENTITY RESOLUTION (fuzzy name -> canonical
  ID, ambiguity asks a disambiguation question) -> a CONSTRAINED business-tool surface (5 named
  tools: find_account / get_account_details / get_account_performance /
  find_accounts_missing_fee_splits / get_account_data_issues) that COMPILES TO GraphQL internally
  -> GraphQL schema + resolvers -> JSON/operational OR parquet/analytical, storage-invisible to
  the client. Business-semantic types only: Account, FeeSplit, Performance, Benchmark, Advisor,
  Strategy, Household, Custodian, DataIssue.
- **INTERNAL plane:** SQL (DuckDB/Trino) directly over parquet -- the analytical escape hatch;
  never forced through GraphQL.
- **Guardrails (his §9):** tenant/client authorization SERVER-SIDE ON EVERY RESOLVER ("never rely
  on the model to scope access correctly"); depth/complexity/row/time/scan limits; canonical IDs
  after fuzzy resolution; schema exposes only approved fields; audit logging (entity, operation,
  identity, data accessed); READ-ORIENTED unless separately governed mutations arrive.
- **Initial scope (his §10):** narrow schema over the named types; fuzzy account resolution as a
  SEPARATE service/tool; master/current data stays operational-simple, history stays parquet;
  semantic boundary NOW, no storage migration required.
- **Core principle (his §11):** "The client agent should reason about the business schema, not
  the storage schema."

## 2. Bindings to live work (the reason this ingest note exists)

- **D6 (OPAL_ANALYST):** U1 discharged. TO-E's schema half unblocks; the brief ALSO reshapes the
  agent side: the Analyst consumes the 5-tool business surface, not raw GraphQL (fewer
  hallucinated fields -- his stated reason). Entity resolution = its own service/tool, sequenced
  BEFORE schema wiring. D6 PRD addendum applied same-turn (see the PRD's ADDENDUM section).
- **Storage mapping is ALREADY OUR MEDALLION:** "JSON/operational" = the platinum serving plane
  (17b: publisher = the JSON producer); "parquet/analytical" = silver/gold. The brief's
  storage-independence principle is 17b restated from the consumer side -- no migration demanded,
  resolvers choose the plane. Internal SQL-over-parquet: note sitez's resident stack already
  carries duckdb (MSTR envelope 184400Z) -- the internal analytical plane is sitez-native today.
- **Entity resolution feeds on measured work:** household/advisor relationships + aliases +
  account numbers are exactly the fam/BD identity plane CRO~A measured (households nest 96.8%;
  crosswalk a06; portfolio-group = advisor book). The resolver service consumes those dims; the
  D2-threaded dim_portfolio_group/bridge and D3's crosswalk-residual work are its data.
- **D7 (ticketing):** the DataIssue type + find_accounts_missing_fee_splits pattern = the same
  client-request universe the DL intake serves; a ticket and a DataIssue are adjacent record
  kinds -- watch for convergence at P3, do not couple in v1.
- **D1 (taxonomy):** `Strategy` in the schema binds to the D1 registry's strategy_id members --
  one vocabulary, no parallel minting (the registry is the schema's source for Strategy).
- **D8 precedent alignment:** "authorization enforced server-side... never rely on the model" is
  the same law D8's PUT path carries (client predicate advisory, server verifies). One auth
  doctrine across both PRDs.
- **Guardrails vs our laws:** read-oriented default + server-side scoping + audit logging align
  with the m365 gateway pattern (identity_scope + audit lake). No conflict found with 17/17a/17b
  or the moratorium (no alerting machinery specified).

## 3. Full text extract (byte-faithful rendering of word/document.xml, whitespace-normalized)

[see scratch extraction; canonical source = the .docx beside this file. Key structures reproduced:]

- Executive summary: semantic client layer vs analytical storage layer; agents resolve intent +
  entities then issue constrained typed GraphQL; GraphQL resolves from JSON or parquet without
  exposing storage; internal SQL (DuckDB/Trino) over parquet stays direct.
- Target architecture: CLIENT question -> agent (intent+entity) -> business tools/GraphQL ->
  schema+resolvers -> {JSON/operational + parquet/analytical}; INTERNAL: SQL -> DuckDB/Trino -> parquet.
- Design principles: business-semantic schema; storage independence; constrained client access;
  analytical freedom internally; entity resolution before retrieval; push computation down.
- Core schema (verbatim types): Account{id, name, advisor, strategy, custodian, feeSplit,
  performance(period), dataIssues}; Performance{return, benchmarkReturn, excessReturn,
  beginningMarketValue, endingMarketValue}; FeeSplit{status, components};
  Query{account(id), accounts(filter), dataIssues(filter)}.
- Query patterns (3 worked examples): missing fee splits (JSON/operational); QTD performance of
  the Henderson account (parquet, after entity resolution); advisor on the Smith account (JSON).
- Entity resolution: "hendrson acct" -> resolver -> Henderson Family Trust, confidence 0.94,
  account_id 18427 -> GraphQL by ID; material ambiguity -> ask, never guess.
- Storage responsibilities table; agent-facing tool surface (5 tools); guardrails (§1 above);
  recommended initial scope; core principle.
