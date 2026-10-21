# NFRA_FIDSLVR -- Fidelity silver, custodian-native and lossless; one canonical gold built by config, seeded from the Schwab silver layout

```json
{
 "project": "NFRA_FIDSLVR",
 "directive": "D8",
 "fabric": "dell1",
 "prd_version": "v0.3",
 "step": 4,
 "brief_ref": "docs/briefs/nfra-fidslvr-fidelity-silver-to-schwab-schema-brief-20261021.md@3d94f8cbe0",
 "endpoint_outcomes": ["FWD-1", "FWD-2", "FWD-3", "FWD-4", "FWD-5", "FWD-6", "FWD-7"],
 "status": "DRAFT"
}
```

**Author:** `1.0.0_SA_CTO~DELL1`, v0.3 2026-10-21 ~16:5xZ (v0.1 ~15:5xZ).

**Placement:** DELL1, directive D8, macro NFRA. Registered @5c8ca94a34, sibling of `NFRA_FIDUPL` (its bronze is this project's input
contract) and of the Schwab silver converter `opal-assets-silver-schwab` (its layout is the SEED of the canonical gold schema, never altered).

**Records (Andrew-direct, recorded by `4.0.0_SA_CRO~FIDELITY`):**
- **~15:20Z,** `org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261021_1520Z_FIDUPL_ALL_FACT_TABLES.md` @abdd501318: every
  Fidelity fact table including open tax lots and realized and unrealized gain/loss; "silver fidelity and silver schwab formulated the
  exact same way ... a master gold layer".
- **~15:35Z and ~15:38Z,** `ANDREW_DIRECT_20261021_1535Z_GOLD_MASTER_CUSTODIAL_ATTRIBUTION_KEY.md`: attribution by the custodian-native
  grouping id (G Number, Master Account Number) through a mapping config, replacing vendor assignment; "we may not even need the master
  gold table because you could just construct the necessary tables in gold by the config".
- **~15:55Z, OPTION B,** `ANDREW_DIRECT_20261021_1555Z_FIDSLVR_OPTION_B_NATIVE_SILVER_CONFIG_GOLD.md`, VERBATIM: "Yse lets go with B here".
  Silver custodian-native and lossless; the matching config holds the conforming logic; gold constructed from the config; the canonical
  gold schema seeded from the Schwab silver layout. Option A (conform-at-silver) rejected: it strands Fidelity-only richness (household
  Groups, which Schwab has in neither silver nor bronze, measured) and bakes possibly-wrong equivalences into the durable layer.
- **CTO ruling** splitting bronze from silver: `CTO_RULING_NFRA_FIDUPL_ALL_FACT_TABLES_BRONZE_AND_FIDELITY_SILVER_SIBLING_20261021.md`
  @6180f77c84.

**Endpoint status:** written at L2 and re-cut to Option B (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ENDPOINT_FORWARD_NFRA_FIDSLVR_20261021.md`,
this commit). **Andrew confirmed the DONE WHEN set with the Option B change** (the CRO's relay, msg 9141); open-calls act cc75 is closed on
the record. This PRD goes to L4-R now.

**The rule that binds every line:** silver is the custodian's own shape; the config is the only place conforming logic lives; gold is
built from it. A conforming transform written into a silver converter fails the cell.

## ENDPOINT (step 2, /endpoint --forward)

```
  FWD-1  A data engineer points the code that reads the canonical positions
         table at the Fidelity-derived GOLD positions table for one business
         date, and it runs unchanged
         DONE WHEN  EXERCISED -- one existing read written against the canonical
                    (Schwab-seeded) positions schema is run on demand against the
                    Fidelity-derived gold positions partition for one date and
                    returns rows; the same read against the Schwab-derived gold
                    positions for the same date is the positive control, printed
                    beside it; the Fidelity rows are traced back through the config
                    to the native silver row and the bronze file they came from
         ACCEPT     The engineer changed no code and no column name; the two
                    results have the same columns and types; the Fidelity rows carry
                    Fidelity's accounts and securities; silver underneath still holds
                    Fidelity's own fields, untouched
         SOURCE     brief Part I thread (Option B), O1; Andrew ~15:55Z "lets go with B"

  FWD-2  Every Fidelity fact family NFRA_FIDUPL lands in bronze reaches a
         native, lossless silver table AND a canonical gold table through the
         matching config
         DONE WHEN  APPLIED -- for each landed family (accounts, positions,
                    balances, securities and prices, transactions, open lots,
                    realized gain/loss, unrealized gain/loss): (a) the silver table
                    is read and every bronze field is found on it, unrenamed and
                    unretyped; (b) the gold table built from it is read against the
                    canonical schema -- column names, types, units, enum values,
                    grain -- and the config row that produced each column is
                    printed; the denominator (families compared of families landed)
                    is printed; a family bronze has not landed yet is named as such,
                    never counted
         ACCEPT     A reviewer finds nothing Fidelity provides stranded or
                    discarded: Fidelity-only richness (the household Groups) sits in
                    silver and surfaces in gold once a canonical table is defined
                    for it; every gold column traces to one config row
         SOURCE     brief O2, O2b; Part IV items 1-3

  FWD-3  Where the two custodians' fields do not map one to one, the gap is
         named in the matching config, never hidden
         DONE WHEN  APPLIED -- the matching config (the per-field reconciliation
                    map: custodian field -> canonical gold field, transform,
                    approximate-match note) is read, and one field known not to
                    map (a Fidelity field with no canonical column, and one
                    canonical column Fidelity cannot fill) is found there with its
                    disposition (custodian-specific column in gold, or left
                    unmapped with the reason)
         ACCEPT     No Fidelity field is silently lost and no canonical column is
                    silently null-filled; changing a mapping edits the config and
                    rebuilds gold, never silver; a query-time surprise about a
                    column is a failure of this outcome
         SOURCE     brief O2b, O4; Part VII first two items

  FWD-4  Silver, and the gold built from it, advance as bronze lands, for the
         daily pull and for the backfilled history
         DONE WHEN  EXERCISED -- one daily bronze landing is converted on demand
                    and its silver and gold partitions read; one backfilled date
                    (a date before the schedule began) is converted on demand and
                    read; one date bronze does not hold is run and the record names
                    the missing input instead of writing an empty partition
         ACCEPT     An analyst reading gold for a date finds it as soon as the
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
| C-NATIVE | every silver converter cell | **Silver is custodian-native and lossless.** Each Fidelity bronze family becomes one silver parquet table carrying Fidelity's OWN fields as the bronze carries them: no rename, no retype, no drop, no conforming; plus the provenance columns the Schwab silver carries (`_source_file`, `_source_as_of`, `_master_observed` as the native grouping id, `_section`, `_schema_version`). Fidelity-only richness (the household Groups) lands here. A silver table changes only when bronze does. | FWD-2 (a): every bronze field found on the silver row, unrenamed |
| C-CONFIG | the config cell (DS) | **The matching config is the project's central artifact**: one committed, versioned data file (not prose), one row per canonical gold column per custodian: `canonical_table, canonical_column, custodian, source_table, source_field (by position for the header-less exports), transform (rename / unit / enum map / date format), match_quality (exact | approximate | none), note`. Gold is constructed from it; changing a mapping edits the config and rebuilds gold, never silver. A canonical column no custodian fills, and a custodian field with no canonical column, are rows with `match_quality = none` and a disposition (custodian-specific gold column, or unmapped with reason). Schwab's own rows are near-identity. Every enum map arrives with its Rule 24 record. | FWD-3's read; FWD-2 (b): each gold column traced to one config row |
| C-CANON | the canonical-schema cell | **The canonical gold schema is SEEDED from the Schwab silver layout** (`schwab_schemas.py` `SPECS` and `PROVENANCE_COLS`, read at build, imported never copied) and is thereafter a deliberate canonical owned by this project: a column is added or changed only through the config and this PRD, never by one custodian's accident. A canonical table is defined for a Fidelity-only family (Groups) when a consumer names it; until then the richness stays in silver, named in the config. | the canonical schema file read beside `SPECS`; the delta named |
| C-GOLD | the gold constructor cell | **Gold is constructed from the config** (per canonical table: union over `custodian`, transforms applied, attribution joined); no per-custodian branch in the constructor; view or materialized set is the DS builder's call recorded at L5 and either passes. **Home: per firm** (`tiers.json` R5/R7): the gold assembly lives in each firm's scope bucket; the cross-firm gate covers it; an account the attribution config cannot place is listed UNATTRIBUTED and placed in no firm. | FWD-1's unchanged reader on the Fidelity-derived gold; FWD-5's both-custodians question |
| C-ATTRIB | the attribution cell | **Attribution by the custodian-native grouping id** through a committed mapping config `(custodian, native_group_id) -> advisor/firm` (Andrew ~15:35Z), never a vendor lookup. The native id rides every silver account row (C-NATIVE's `_master_observed`: the G Number for Fidelity, supplied by the per-G landing scope where the account file carries none; the Master Account Number for Schwab) and every gold row. | FWD-7's three attributions |
| C-NAMES | every cell | **Every address and resource name is `lib/opal_naming.py` output** (rule 30). Builder output, measured 2026-10-21 15:44Z: `address('fidelity','alongside','silver','fact_rps','20261015')` -> `s3://opal-data-assets/fidelity/alongside/silver/fact_rps/20261015`; `address('fidelity','cottonwood','silver','fact_rps','20261015')` -> `s3://opal-data-assets/fidelity/cottonwood/silver/fact_rps/20261015`; `name('fidelity','alongside','silver-convert','lambda')` -> `fidelity-alongside-silver-convert-lambda`. Silver table names follow the Schwab `fact_<feed>` / `_s{N}` rule only where a Fidelity family IS a Schwab feed; a Fidelity-only family takes the name the builder gives its registry row. The gold addresses are asked of the builder by the first gold cell with a PRODUCT source key; a refusal is a registry row (a canonical-gold product system), never a typed path. | `address()`/`name()` printed in each cell's proof |
| C-INPUT | every converter cell | **Input is NFRA_FIDUPL's bronze exactly as landed** (`fidelity/<scope>/bronze/<type>/<YYYYMMDD>/`: the six export families, the fixed-length Historical `position_balance_fl`, and the JSON families the bronze cells add: open lots, realized and unrealized gain/loss, household Groups). This project signs in nowhere and pulls nothing; a missing bronze date is named in the run record (FWD-4), never fetched. | FWD-4's missing-date run |
| C-PARTITION | every converter cell | **One date = one partition = one object** (the Schwab ruling 23, `conversion_manifest.py:477-481`) at silver and at gold; a re-run of a date replaces its one object. | FWD-4's partition reads |
| C-RECORD | every cell | **One run record per conversion** (tables written, rows, the bronze object read and its sha, the config version used, the missing inputs), read never sent (moratorium). | FWD-4's record |
| C-RISK | the issuer | Every task order carries its `<risk>` class (rule 22): the silver and gold cells are SERVED (they write the shared silver home and the firm gold homes); the config and canonical-schema cells are LOCAL until a constructor consumes them. | GATE xii |

## THE DECISIONS -- CLOSED AT L4

1. **Option B, taken literally (C-NATIVE, C-CONFIG, C-GOLD):** uniformity is a GOLD property produced by the config; silver is the
   custodian's own shape. v0.1's "Schwab pin imported as the law at silver" and "extensions as sidecars" (C-SCHEMA, C-EXT) are retired.
2. **The Schwab layout seeds the canonical and is not altered (C-CANON):** Schwab's own silver stays as is; its config rows are
   near-identity; a canonical change is a config-and-PRD change.
3. **The config is data, versioned, and the single source of conforming truth (C-CONFIG):** the reconciliation labor is written once,
   inspectable, and never baked into a durable layer.
4. **Gold by config, per firm, attributed by the native id (C-GOLD, C-ATTRIB):** Andrew's ~15:35Z and ~15:38Z words, unchanged by B.
5. **Unrealized gain/loss grain:** read from the Schwab seed (`fact_uln`/`fact_ult`); Fidelity's lot-level values map to that grain
   through the config; the config records whether a separate canonical table exists.
6. **Round 1 is one fact, one date, through all three layers:** positions, bronze to native silver to canonical gold, read by an
   unchanged canonical reader with the Schwab-derived gold as the positive control.
7. **No alert, no monitor** (moratorium): the run record is the whole failure surface.

## OPEN AT ANDREW (acts only he can do)

- None. His confirmation of the DONE WHEN lines was given with the Option B re-cut (msg 9141); cc75 is closed on the endpoint record.

## CELL CANDIDATES (round 1 builds the FWD-1 thread; the issuer decomposes)

0. **Prerequisite (CRO):** the positions export column list (the wizard's step-2 list) and the fixed-length `position_balance_fl` record
   layout, as data; the Schwab `SPECS[('RPS',1)]` column list read beside them.
1. **The native silver positions converter** (C-NATIVE, C-NAMES, C-INPUT, C-PARTITION, C-RECORD): one bronze position partition in, one
   lossless silver partition out at the builder's address.
2. **The canonical positions schema and the positions config** (C-CANON, C-CONFIG): the canonical seeded from `SPECS[('RPS',1)]`; one
   config row per canonical column for Fidelity (and the near-identity rows for Schwab), with units, enums and `match_quality`.
3. **The gold positions constructor** (C-GOLD, C-NAMES): the canonical positions table for one date from the Fidelity silver through
   the config, and from the Schwab silver through its rows, at the builder's gold address.
4. **FWD-1's trace:** an existing canonical-schema positions reader run on the Fidelity-derived gold partition, then on the
   Schwab-derived one for the same date, both printed, one Fidelity row traced back to its silver row and bronze file.

Later rounds enrich: accounts with the native id (C-ATTRIB), balances, securities and prices, transactions, open lots, realized and
unrealized gain/loss, the household Groups (FWD-2, FWD-3); the daily and backfill triggers (FWD-4); the attribution config and the gold
assembly for a both-custodians question (FWD-5, FWD-7).

## PATHS

- **This project:** `org/missions/D8/NFRA/NFRA_FIDSLVR/`.
- **Prior art, read at HEAD by the issuer before the first cell:**
  - `infra/aws/lambda/opal-assets/opal-assets-silver-schwab/` (`schwab_schemas.py` SPECS and PROVENANCE_COLS, `schwab_projections.py`,
    `silver_registry.py`, `conversion_manifest.py:477-481`, `set_identity_guard.py`);
  - `lib/opal_naming.py`, `infra/logic/registry/{systems,scopes,tiers}.json`, `infra/logic/02_DOCTRINE.md` R4-R7;
  - `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261021_NFRA_FIDUPL_FULL_FACT_TABLE_CATALOG.md` (the table map, Tier A2);
  - `org/missions/D8/NFRA/NFRA_FIDUPL/prd/NFRA_FIDUPL_PRD.md` C-TENANCY (the per-G landing that supplies the native id).

## SURFACE MANIFEST

- **AWS:** one new function in the `opal-assets` family for the native silver (name from the builder) and one gold constructor
  (function or query-side assembly, the DS call at L5), their roles with per-prefix grants on the Fidelity bronze (read), the silver
  (write) and the firm gold homes (write); a trigger on bronze landing ruled at L5; silver partitions under
  `address('fidelity', <scope>, 'silver', ...)`; gold under each firm's scope bucket at the builder's address.
- **Portal:** none.
- **Repo:** this tree, the converters, the canonical schema file, the matching config, the attribution config, and any registry rows the
  builders refuse without.

## CHANGE LOG

- **v0.3 (2026-10-21 ~16:5xZ, `1.0.0_SA_CTO~DELL1`), OPTION B (Andrew-direct ~15:55Z via the CRO, msg 9141):** FWD-1 and FWD-2 re-cut in
  the L2 record so the unchanged-reader and parity proofs sit at the Fidelity-derived GOLD; FWD-3 and FWD-4 re-worded to the config and
  to gold (FWD-5..7 unchanged); the ENDPOINT block re-pasted verbatim. C-SCHEMA and C-EXT retired; C-NATIVE, C-CONFIG, C-CANON, C-GOLD,
  C-ATTRIB in their place. Andrew confirmed the DONE WHEN set with this change: cc75 closed on the endpoint record; L4-R proceeds.
- **v0.2 (2026-10-21 ~15:5xZ, `1.0.0_SA_CTO~DELL1`):** CVO REFUSE @51518ac061 answered: FWD-2 names unrealized gain/loss (Andrew ~15:20Z verbatim; Schwab twins fact_uln/fact_ult) in the L2 record; FWD-6 and FWD-7 restored to the record's order; the ENDPOINT block re-pasted verbatim from the L2 record.
- **v0.1 (2026-10-21 ~15:5xZ, `1.0.0_SA_CTO~DELL1`):** DRAFT on endpoint @5c8ca94a34 and brief @cc707deac8. L4-R waits on Andrew's
  confirmation of the DONE WHEN lines; the CVO's ratified-text half is delivered now so it can be read in parallel.
