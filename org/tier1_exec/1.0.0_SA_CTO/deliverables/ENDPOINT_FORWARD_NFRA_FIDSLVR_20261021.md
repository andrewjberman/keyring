# ENDPOINT (step 2, /endpoint --forward) -- NFRA_FIDSLVR: Fidelity silver formulated exactly as Schwab silver, for one gold union (`1.0.0_SA_CTO~DELL1`, 2026-10-21 ~15:4xZ)

**Brief:** `docs/briefs/nfra-fidslvr-fidelity-silver-to-schwab-schema-brief-20261021.md` @cc707deac8 (`4.0.0_SA_CRO~FIDELITY`, measured
2026-10-21 ~15:30Z; amended ~15:37Z with the gold attribution key and the no-bespoke-master refinement, Andrew-direct ~15:35Z and ~15:38Z,
`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261021_1535Z_GOLD_MASTER_CUSTODIAL_ATTRIBUTION_KEY.md`).

**Order:** Andrew-direct 2026-10-21 ~15:20Z via `4.0.0_SA_CRO~FIDELITY`
(`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261021_1520Z_FIDUPL_ALL_FACT_TABLES.md` @abdd501318): every Fidelity fact table
including open tax lots and realized and unrealized gain/loss; "silver fidelity and silver schwab formulated the exact same way ... a
master gold layer". CTO ruling splitting bronze (NFRA_FIDUPL) from silver (this project):
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_NFRA_FIDUPL_ALL_FACT_TABLES_BRONZE_AND_FIDELITY_SILVER_SIBLING_20261021.md` @6180f77c84.

**Project code (registered at L3 in this commit):** `NFRA_FIDSLVR`, macro NFRA, directive D8, placement DELL1. Sibling of `NFRA_FIDUPL`
(its bronze is this project's input contract) and of the Schwab silver converter `opal-assets-silver-schwab` (its schema is matched,
never altered).

**Thread (round 1):** ONE fact table end to end -- Fidelity positions (`fact_rps`) for one business date, read by code written for Schwab.
Later rounds enrich to every table, then the gold union.

```
  FWD-1  A data engineer points the code that reads Schwab silver positions
         at the Fidelity silver positions table for one business date, and
         it runs unchanged
         DONE WHEN  EXERCISED -- one existing Schwab-reading read (a query or
                    reader the estate already runs against Schwab fact_rps) is
                    run on demand against the Fidelity fact_rps partition for
                    one date and returns rows; the same read against the Schwab
                    fact_rps for the same date is the positive control, printed
                    beside it
         ACCEPT     The engineer changed no code and no column name; the two
                    results have the same columns and types, and the Fidelity
                    rows carry Fidelity's accounts and securities
         SOURCE     brief Part I, candidate thread; O1; Part III first test

  FWD-2  Every Fidelity fact family that NFRA_FIDUPL lands in bronze has a
         silver table of the matching Schwab schema
         DONE WHEN  APPLIED -- for each landed family (accounts, positions,
                    balances, securities and prices, transactions, open lots,
                    realized gain/loss) a schema parity read compares the
                    Fidelity table against its Schwab twin -- column names, types,
                    units, enum values, grain -- and prints the denominator
                    (tables compared of tables landed)
         ACCEPT     A reviewer finds the same columns, types and grain on every
                    compared pair, and no family stranded in bronze with no silver
                    table; a family bronze has not landed yet is named as such,
                    never counted as matched
         SOURCE     brief O2; Part IV items 1-3

  FWD-3  Where the two custodians' fields do not map one to one, the gap is
         named per table, never hidden
         DONE WHEN  APPLIED -- the per-field reconciliation map is read, and
                    one field known not to map (a Fidelity field the Schwab
                    schema lacks, and one Schwab column Fidelity cannot fill) is
                    found there with its disposition (extension column, or
                    dropped with the reason)
         ACCEPT     No Fidelity field is silently lost and no Schwab column is
                    silently null-filled; a query-time surprise about a column is
                    a failure of this outcome
         SOURCE     brief O4; Part VII first two items

  FWD-4  Silver advances as bronze lands, for the daily pull and for the
         backfilled history
         DONE WHEN  EXERCISED -- one daily bronze landing is converted on demand
                    and its silver partition read; one backfilled date (a date
                    before the schedule began) is converted on demand and read;
                    one date bronze does not hold is run and the record names the
                    missing input instead of writing an empty partition
         ACCEPT     An analyst reading silver for a date finds it as soon as the
                    bronze for that date exists, partitioned by business date, and
                    can tell a date Fidelity never served from a date not yet
                    converted
         SOURCE     brief O5; Part V first item

  FWD-5  An analyst answers a both-custodians question from one gold layer
         built by configuration from the two uniform silvers
         DONE WHEN  EXERCISED -- one cross-custodian question (holdings for one
                    household that holds both Schwab and Fidelity accounts, one
                    date) is run on demand over the gold assembly and returns
                    rows from both custodians, the custodian dimension read on
                    each; whether the assembly is a view or a materialized set is
                    the DS builder's call, recorded in the PRD, and either passes
         ACCEPT     The gold logic carries no per-custodian branch and presumes
                    no bespoke master table; adding a third custodian is one more
                    silver conforming to the same schema plus config, not a
                    change to gold
         SOURCE     brief O3; Andrew-direct ~15:38Z ("construct the necessary
                    tables in gold by the config")

  FWD-7  Every account in gold is attributed to its advisor or firm from the
         custodian's own grouping id, never from a downstream vendor
         DONE WHEN  EXERCISED -- the mapping config (custodian, native group id)
                    -> advisor/firm is read; one Fidelity account is attributed on
                    demand by its G Number and one Schwab account by its Master
                    Account Number; one account whose native id the config does
                    not hold is returned UNATTRIBUTED by name, never guessed
         ACCEPT     An analyst reading who-is-who at the custodial level sees the
                    native id on every silver account row and the attribution it
                    resolved to, with no vendor assignment consulted; the config
                    is the single source of attribution
         SOURCE     brief O3 attribution key; Andrew-direct ~15:35Z ("use the
                    G Number from Fidelity and the Master Account Number from
                    Schwab ... in some mapping config ... rather than rely on
                    downstream data vendor inputs")

  FWD-6  Every home, address and name of the Fidelity silver and the gold
         union comes from the canon's builders
         DONE WHEN  APPLIED -- each silver and gold address is printed by
                    lib/opal_naming.py address() and each resource name by
                    name(), cited in the PRD; a builder refusal is a registry row
                    added, never a typed path
         ACCEPT     A reader of the PRD finds builder output beside every new
                    address and name; the naming gate refuses nothing at commit
         SOURCE     CLAUDE.md rule 30; brief Part II third row
```

## Questions the brief leaves open, and who settles them (none is an outcome)

- **Whether unrealized gain/loss is its own silver table or lot-level inside open lots** (`fact_uln`/`fact_ult` split): the DS builder's
  call at L4/L5, read from the Schwab twin's grain; the PRD records it.
- **Which account field carries each native id** (brief Part VII): read from the landed bronze and the Schwab silver `fact_acc` at L4,
  never assumed.
- **Where the gold union lives** (tier home, tenancy): rule 30, the canon's builders at L4; not a seat's choice.
- **A true shared-schema change** (the Schwab silver would have to move): a joint decision with the Schwab silver's owner, named in the
  PRD as out of scope for round 1.
- **Andrew's confirmation of these DONE WHEN lines** (Andrew-direct 2026-09-03: "i will confirm CTO's 'DONE WHEN' from their
  /endpoint --forward"): the L4 PRD is drafted on this endpoint now; L4-R waits on that word and on nothing else.

-- 1.0.0_SA_CTO~DELL1
