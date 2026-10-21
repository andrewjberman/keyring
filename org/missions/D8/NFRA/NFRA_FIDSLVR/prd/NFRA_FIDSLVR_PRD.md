# NFRA_FIDSLVR -- Fidelity silver formulated exactly as Schwab silver, and one gold layer built by config

```json
{
 "project": "NFRA_FIDSLVR",
 "directive": "D8",
 "fabric": "dell1",
 "prd_version": "v0.2",
 "step": 4,
 "brief_ref": "docs/briefs/nfra-fidslvr-fidelity-silver-to-schwab-schema-brief-20261021.md@cc707deac8",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~DELL1`, 2026-10-21 ~15:5xZ.

**Placement:** DELL1, directive D8, macro NFRA. Registered @5c8ca94a34, sibling of `NFRA_FIDUPL` (its bronze is this project's input
contract) and of the Schwab silver converter `opal-assets-silver-schwab` (its schema is matched, never altered).

**Records (Andrew-direct, recorded by `4.0.0_SA_CRO~FIDELITY`):**
- **~15:20Z,** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261021_1520Z_FIDUPL_ALL_FACT_TABLES.md` @abdd501318: every
  Fidelity fact table including open tax lots and realized and unrealized gain/loss; "silver fidelity and silver schwab formulated the
  exact same way ... a master gold layer".
- **~15:35Z and ~15:38Z,** `ANDREW_DIRECT_20261021_1535Z_GOLD_MASTER_CUSTODIAL_ATTRIBUTION_KEY.md`: "use the 'G Number' from Fidelity
  and the 'Master Account Number' from Schwab to be in some mapping config so that we'd be able to parse who is who at the Custodial level
  rather than rely on downstream data vendor inputs to assign accounts to advisors"; "we may not even need the master gold table because
  you could just construct the necessary tables in gold by the config".
- **CTO ruling** splitting bronze from silver: `CTO_RULING_NFRA_FIDUPL_ALL_FACT_TABLES_BRONZE_AND_FIDELITY_SILVER_SIBLING_20261021.md`
  @6180f77c84.

**Endpoint status:** written at L2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_NFRA_FIDSLVR_20261021.md` @5c8ca94a34).
Andrew's confirmation of the DONE WHEN lines is an act on the box's open calls; this PRD goes to L4-R after it. If he changes a line,
ENDPOINT is re-pasted here.

## ENDPOINT (step 2, /endpoint --forward)

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
                    realized gain/loss, unrealized gain/loss) a schema parity
                    read compares the
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

  FWD-6  Every home, address and name of the Fidelity silver and the gold
         union comes from the canon's builders
         DONE WHEN  APPLIED -- each silver and gold address is printed by
                    lib/opal_naming.py address() and each resource name by
                    name(), cited in the PRD; a builder refusal is a registry row
                    added, never a typed path
         ACCEPT     A reader of the PRD finds builder output beside every new
                    address and name; the naming gate refuses nothing at commit
         SOURCE     CLAUDE.md rule 30; brief Part II third row

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
```

## CONTRACTS

| row | owner | rule | proven by |
|---|---|---|---|
| C-SCHEMA | every converter cell | **The Fidelity `fact_<x>` table carries EXACTLY the Schwab silver pin for the same name** -- the column pairs in `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/schwab_schemas.py` `SPECS[(feed, section)]` (names, types, order) plus `PROVENANCE_COLS` (`_source_file`, `_source_as_of`, `_master_observed`, `_section`, `_schema_version`) -- no rename, no retype, no added column. The pin is IMPORTED from its one source, never copied into the Fidelity converter (a copy drifts). The `_s{N}` section rule and the `dim_` projection law (`schwab_projections.py`, `silver_registry.py:75-81`) apply as written. The Schwab silver is never altered by this project; a change the shared schema would need is a joint decision recorded here, not an edit. | FWD-2's parity read prints the pin's column list beside the Fidelity table's; FWD-1's unchanged reader |
| C-EXT | the map cell | **A Fidelity field the pin lacks goes to a sibling extension table `fidx_<fact_table>` at the same grain and key, never into the `fact_` table** (so O1 holds strictly: a Schwab reader cannot tell the custodian apart). A Schwab column Fidelity cannot fill is NULL in the fact table AND named in the reconciliation map with its reason; an unnamed NULL column is FWD-3's failure. The DS builder's extension-table proposal arrives with its Rule 24 record. | FWD-3's map read; one known-unmapped field each way |
| C-MAP | the map cell (DS) | **One committed reconciliation map per fact table**, data not prose: Fidelity field (by position, the export files carry no header; the wizard's step-2 column list names them, CRO research), Schwab column, type, unit normalization (bond price basis per 100, date formats, enum codes such as covered status and wash flags), disposition (mapped / extension / dropped with reason). It is the artifact FWD-3 reads. | the map file read at FWD-3 |
| C-NAMES | every cell | **Every address and resource name is `lib/opal_naming.py` output** (rule 30). Builder output, measured 2026-10-21 15:44Z: `address('fidelity','alongside','silver','fact_rps','20261015')` -> `s3://opal-data-assets/fidelity/alongside/silver/fact_rps/20261015`; `address('fidelity','cottonwood','silver','fact_rps','20261015')` -> `s3://opal-data-assets/fidelity/cottonwood/silver/fact_rps/20261015`; `name('fidelity','alongside','silver-convert','lambda')` -> `fidelity-alongside-silver-convert-lambda`. Tier home: `infra/logic/registry/tiers.json` FIRM silver = shared `opal-data-assets` (R4), gold = the firm's scope bucket (R5, R7). A refusal is a registry row, never a typed path. | `address()`/`name()` printed in each cell's proof |
| C-INPUT | every converter cell | **Input is NFRA_FIDUPL's bronze exactly as landed** (`fidelity/<scope>/bronze/<type>/<YYYYMMDD>/`, the six export families, the fixed-length Historical `position_balance_fl`, and the JSON families the bronze cells add: open lots, realized and unrealized gain/loss). This project signs in nowhere and pulls nothing; a missing bronze date is named in the run record (FWD-4), never fetched. | FWD-4's missing-date run |
| C-PARTITION | every converter cell | **One date = one partition = one object** (the Schwab ruling 23, `conversion_manifest.py:477-481`): `.../silver/<table>/date=<D>/<name>.parquet`, the firm form where the bronze is per firm. A re-run of a date replaces its one object; two objects under one date is a defect. | FWD-4's partition reads |
| C-NATIVE-ID | the accounts converter cell | **The custodian-native grouping id travels on every silver account row**: Fidelity's G Number in the SAME column the Schwab `fact_acc` uses for the Master Account Number (read from `SPECS[('ACC',1)]` at build, never assumed; brief Part VII names the confirmation). Where the Fidelity account file carries no G Number (measured 2026-10-19: 0 of 5,007 standard-file accounts), the id comes from the bronze's landing scope (the per-G pull of NFRA_FIDUPL v0.4.5) and the map says so. | FWD-7's attribution read |
| C-GOLD | the gold cell | **Gold is constructed by configuration from the uniform silvers**: a union over `custodian` plus the attribution config `(custodian, native_group_id) -> advisor/firm`; no per-custodian branch; no bespoke master table presumed (view or materialized set is the DS builder's call, recorded at L5). **Home: per firm** -- R5/R7 make a slice attributable to one firm that firm's data, so the gold assembly lives in each firm's scope bucket and the cross-firm gate covers it; an account the config cannot attribute is listed UNATTRIBUTED and placed in no firm. The attribution config is a committed registry-shaped data file, authored under C-NAMES, never a vendor lookup. | FWD-5's both-custodians question; FWD-7's three attributions |
| C-RECORD | every cell | **One run record per conversion** (tables written, rows, the bronze object read and its sha, the missing inputs), read never sent (moratorium). | FWD-4's record |
| C-RISK | the issuer | Every task order carries its `<risk>` class (rule 22): the converter cells are SERVED (they write the shared silver home); the map and config cells are LOCAL until a converter consumes them. | GATE xii |

## THE DECISIONS -- CLOSED AT L4

1. **Conformance, not invention (C-SCHEMA):** the Schwab pin is the law and it is imported, not copied. The Fidelity converter is a new
   function in the `opal-assets` family beside `opal-assets-silver-schwab`, named by the builder, sharing the schema module as a package
   (how the share is packaged -- a layer, a vendored module with a build-input hash, or a shared lib -- is the issuer's cut, with the
   constraint that the pin has ONE source).
2. **Extensions are sidecars (C-EXT):** O1 is strict. A Schwab reader must not see a column it does not know.
3. **Gold by config, per firm (C-GOLD):** Andrew's ~15:38Z refinement is taken literally; no master table is built in round 1. The gold
   question for FWD-5 is answered by an assembly over the two silvers and the attribution config. The home is the firm bucket by R7.
4. **Unrealized gain/loss grain:** read from the Schwab twin (`fact_uln`/`fact_ult`); Fidelity's lot-level values map to that grain; the
   map records whether a separate table exists.
5. **Round 1 is one table, one date:** positions (`fact_rps`) for one business date, plus the positions map; FWD-1's trace is the reader
   run twice (Fidelity, then Schwab as the positive control).
6. **No alert, no monitor** (moratorium): the run record is the whole failure surface.

## OPEN AT ANDREW (acts only he can do)

- **Confirm the DONE WHEN lines FWD-1..FWD-7** (Andrew-direct 2026-09-03: "i will confirm CTO's 'DONE WHEN' from their /endpoint
  --forward"). Nothing else.

## CELL CANDIDATES (round 1 builds the FWD-1 thread; the issuer decomposes)

0. **Prerequisite (CRO):** the positions export column list (the wizard's step-2 list for the Fidelity custom position file) and the
   fixed-length `position_balance_fl` record layout, as data.
1. **The positions reconciliation map** (C-MAP, C-EXT): Fidelity position fields -> `SPECS[('RPS',1)]` columns, with units and enums;
   the extension sidecar named; the Rule 24 record for any enum.
2. **The `fact_rps` converter for one date** (C-SCHEMA, C-NAMES, C-INPUT, C-PARTITION, C-RECORD): one bronze position partition in,
   one silver partition out at the builder's address, the run record written.
3. **FWD-1's trace:** an existing Schwab `fact_rps` reader run on the Fidelity partition, then on the Schwab partition for the same
   date, both printed.

Later rounds enrich: accounts with the native id (C-NATIVE-ID), balances, securities and prices, transactions, open lots, realized and
unrealized gain/loss (FWD-2, FWD-3); the daily and backfill triggers (FWD-4); the attribution config and the gold assembly (FWD-5,
FWD-7).

## PATHS

- **This project:** `org/missions/D8/NFRA/NFRA_FIDSLVR/`.
- **Prior art, read at HEAD by the issuer before the first cell:**
  - `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/` (`schwab_schemas.py` SPECS and PROVENANCE_COLS, `schwab_projections.py`,
    `silver_registry.py`, `conversion_manifest.py:477-481`, `set_identity_guard.py`);
  - `lib/opal_naming.py`, `infra/logic/registry/{systems,scopes,tiers}.json`, `infra/logic/02_DOCTRINE.md` R4-R7;
  - `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261021_NFRA_FIDUPL_FULL_FACT_TABLE_CATALOG.md` (the table map, Tier A2);
  - `org/missions/D8/NFRA/NFRA_FIDUPL/prd/NFRA_FIDUPL_PRD.md` C-TENANCY (the per-G landing that supplies the native id).

## SURFACE MANIFEST

- **AWS:** one new function in the `opal-assets` family (name from the builder), its role with per-prefix grants on the Fidelity bronze
  (read) and silver (write) addresses, a trigger on bronze landing ruled at L5; silver partitions under `address('fidelity', <scope>,
  'silver', ...)`; gold under each firm's scope bucket.
- **Portal:** none.
- **Repo:** this tree, the converter, the reconciliation maps, the attribution config, and any registry rows the builders refuse without.

## CHANGE LOG

- **v0.2 (2026-10-21 ~15:5xZ, `1.0.0_SA_CTO~DELL1`):** CVO REFUSE @51518ac061 answered: FWD-2 names unrealized gain/loss (Andrew ~15:20Z verbatim; Schwab twins fact_uln/fact_ult) in the L2 record; FWD-6 and FWD-7 restored to the record's order; the ENDPOINT block re-pasted verbatim from the L2 record.
- **v0.1 (2026-10-21 ~15:5xZ, `1.0.0_SA_CTO~DELL1`):** DRAFT on endpoint @5c8ca94a34 and brief @cc707deac8. L4-R waits on Andrew's
  confirmation of the DONE WHEN lines; the CVO's ratified-text half is delivered now so it can be read in parallel.
