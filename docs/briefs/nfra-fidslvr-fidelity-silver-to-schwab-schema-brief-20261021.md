# BRIEF -- NFRA_FIDSLVR: Fidelity silver, formulated the same as Schwab silver, for one gold union

**Author:** `4.0.0_SA_CRO~FIDELITY` (dell1) | **Date:** 2026-10-21 | **Mode:** NEW
**Ordered by:** `1.0.0_SA_CTO~DELL1` msg 9120 (ruling @ CTO_RULING_NFRA_FIDUPL_ALL_FACT_TABLES...20261021), on Andrew-direct
2026-10-21 ~15:20-15:28Z: every Fidelity fact table, and "silver fidelity and silver schwab formulated the exact same way ... a master
gold layer" (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261021_1520Z_FIDUPL_ALL_FACT_TABLES.md`).
**Research behind it:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261021_NFRA_FIDUPL_FULL_FACT_TABLE_CATALOG.md` (the full
Fidelity surface catalog + the Fidelity->Schwab table map). Sibling of NFRA_FIDUPL, which lands the bronze.

---

## PART I -- THE OUTCOME TERRITORY

**Candidate thread (FWD-1):** a data engineer who already reads a Schwab silver `fact_*` table points the same code at the Fidelity
silver `fact_*` table of the same name and it works unchanged -- same columns, same types, same grain -- for one fact table
(`fact_rps`, positions) end to end, one business date. Round 1 proves that one table matches; later rounds enrich to every table.

### O1 -- A reader cannot tell the custodian apart at silver
A data engineer reading `fact_acc`, `fact_rps`, `fact_rps_s2`, `fact_sec`, `fact_trn`, `fact_uln`/`fact_ult`, `fact_rld` for Fidelity gets
the **same schema** (column names, types, units, enum values, grain) as the Schwab silver tables of those names. Code written for Schwab
runs on Fidelity with no change.

### O2 -- Every bronze fact table reaches a silver table of the Schwab schema
For each Fidelity bronze fact family NFRA_FIDUPL lands -- accounts, positions, balances, securities/prices, transactions, open tax lots,
realized gain/loss (and unrealized, at lot grain) -- there is a corresponding silver parquet table built to the matching Schwab silver
table's schema. Nothing Fidelity provides is stranded in bronze.

### O3 -- A master gold layer serves both custodians from one model
An analyst asking a cross-custodian question (holdings, lots, realized gains across a household that has both Schwab and Fidelity accounts)
reads one gold model that unions the two silvers on a `custodian`/`source` dimension, with no per-custodian branching in the gold logic.

### O4 -- The unmappable is named, not hidden
Where a Fidelity source has a field the Schwab schema lacks (or vice versa), the gap is recorded per table -- carried in an extension
column, or explicitly dropped with its reason -- so no field is silently lost and no Schwab column is silently null-filled.

### O5 -- Silver runs off bronze as landed, daily and for the backfill
The converter consumes NFRA_FIDUPL's bronze exactly as it lands (daily and the backfilled history: transactions to ~2021-12, realized
lots to 2018), partitioned by business date, so silver advances automatically as bronze does.

---

## PART II -- WHERE THE BOUNDARY SITS

| This project (NFRA_FIDSLVR) OWNS | Relies on, does not change |
|---|---|
| The Fidelity silver converters (bronze -> parquet `fact_*`/`dim_*` to the Schwab schema) | NFRA_FIDUPL's bronze landing (the raw .txt/JSON fact files) -- the input contract |
| The per-field reconciliation map (Fidelity field -> Schwab silver column) | The Schwab silver schema (`opal-assets-silver-schwab`), which it matches and never alters |
| The master gold union model across custodians, on a `custodian` dimension | LGIC naming (`lib/opal_naming.py`), the `fidelity` scopes already registered |

**Named siblings:**
- **NFRA_FIDUPL** -- lands all the Fidelity bronze fact tables (incl. open lots, realized/unrealized G/L as build cells). Upstream; this
  project starts where its bronze ends.
- **The Schwab silver (`opal-assets-silver-schwab`)** -- the schema template. This project conforms to it; if a true shared-schema change
  is needed, that is a joint decision, not a unilateral edit here.
- **The per-firm split** (NFRA_FIDUPL) -- orthogonal; silver is built on the Alongside bronze regardless of firm attribution.

---

## PART III -- THE QUALITATIVE BAR

- A Schwab silver reader runs unchanged on the Fidelity silver table of the same name -- the test Andrew set ("formulated the exact same
  way"). Disputable: point real Schwab-reading code at the Fidelity table and see it run or fail.
- An analyst answers a both-custodians question from one gold model without custodian-specific code.
- A reviewer comparing a Fidelity `fact_*` table against its Schwab twin finds the same columns/types/grain, and every divergence named in
  the reconciliation map rather than discovered at query time.

No row counts or tolerances are set here; the quantitative parity bars are the PRD's.

---

## PART IV -- THE SUBSTRATE: is this in a canonical pattern?

1. **The Schwab silver already has every target table** (M, `schwab/.../silver/`): `fact_acc, fact_sec, fact_trn, fact_rps, fact_rps_s2,
   fact_uln, fact_ult, fact_rld, fact_rlu, fact_rlw, fact_rly, fact_rtu, fact_rty, fact_upn, fact_upt`, plus `dim_*`. The schema to match
   exists and is deployed -- this is conformance, not invention.
2. **A silver converter pattern exists** (`opal-assets-silver-schwab`), registry keyed by source+feed. The Fidelity converter registers
   beside it (a new source `fidelity`, already a registry scope).
3. **The Fidelity->Schwab table map is drafted** (catalog Tier A2): account->fact_acc, position->fact_rps, balance->fact_rps_s2,
   security+prices->fact_sec, transact->fact_trn, open-lots->fact_uln/ult, realized->fact_rld(+variants); no Fidelity analog for
   fact_upn/upt yet.
4. **The hard part is field-level reconciliation** (I): Fidelity's custom CSV columns (no header; schema from the wizard's step-2 column
   list) vs Schwab's silver columns -- names, types, units (e.g. bond prices per 100), enum codes, date formats. This is the real labor,
   per table.

---

## PART V -- WHAT MUST BE TRUE, WITHOUT SCOPING IT NOW

- The bronze fact tables land (NFRA_FIDUPL): the 6 export files are landing; open lots + realized/unrealized G/L bronze cells are being cut.
- The Fidelity column schemas: the export files have no header; the wizard's step-2 column list names them. The JSON surfaces' shapes are
  in the endpoint map.
- The Schwab silver per-table column schema, read as the conformance target (not altered).
- The gold union's `custodian`/`source` dimension and where the gold model lives (LGIC homes).
- The unit/enum normalizations (bond price basis, covered-status codes, wash flags, date formats) that make the two custodians'
  values comparable.

---

## PART VI -- STATUS (NOT OUTCOME-BEARING)

Measured 2026-10-21: Fidelity bronze is landing (6 export families daily; positions backfilled to ~2026-06-15; transactions reach
~2021-12; realized lots to 2018 closes / 2013 acquisitions). No Fidelity silver exists yet. Schwab silver is live as the template. The
`fidelity` and firm scopes are registered.

---

## PART VII -- WHAT THIS BRIEF DOES NOT CLAIM

- It does not claim the Fidelity and Schwab columns already align -- the reconciliation is the work; some fields will not map 1:1 (O4).
- It does not claim unrealized G/L is a distinct Fidelity table -- it is lot-level inside open-lots; whether `fact_uln`/`fact_ult` split
  is a PRD/DS call.
- It does not size the per-account extraction cost for the lot/G-L bronze (that is NFRA_FIDUPL's).
- It did not re-verify each Schwab silver column this pass; the table list is measured, the per-column schema is read at build.

---

## REFS

```
  BRIEF PATH    docs/briefs/nfra-fidslvr-fidelity-silver-to-schwab-schema-brief-20261021.md
  PROJECT       NFRA_FIDSLVR (working code; CTO registers at L3)
  PARENT        NFRA_FIDUPL (bronze; input contract)
  RESEARCH      org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261021_NFRA_FIDUPL_FULL_FACT_TABLE_CATALOG.md
                org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261019_FIDELITY_WEALTHSCAPE_HAR_ENDPOINT_MAP.md
  SCHEMA TEMPLATE  infra/aws/lambda/opal-assets/opal-assets-silver-schwab/ ; s3://opal-data-assets/schwab/<master>/silver/
  INPUT CONTRACT   s3://opal-data-assets/fidelity/alongside/bronze/<type>/<YYYYMMDD>/ (as NFRA_FIDUPL lands)
  DONE WHEN        a parity read against Schwab silver per fact table (CTO's L2 cut)
  MEASURED AT      2026-10-21 ~15:30Z
```
