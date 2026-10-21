# BRIEF -- NFRA_FIDSLVR: Fidelity silver, formulated the same as Schwab silver, for one gold union

**Author:** `4.0.0_SA_CRO~FIDELITY` (dell1) | **Date:** 2026-10-21 | **Mode:** NEW
**Ordered by:** `1.0.0_SA_CTO~DELL1` msg 9120 (ruling @ CTO_RULING_NFRA_FIDUPL_ALL_FACT_TABLES...20261021), on Andrew-direct
2026-10-21 ~15:20-15:28Z: every Fidelity fact table, and "silver fidelity and silver schwab formulated the exact same way ... a master
gold layer" (`org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261021_1520Z_FIDUPL_ALL_FACT_TABLES.md`).
**Research behind it:** `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_20261021_NFRA_FIDUPL_FULL_FACT_TABLE_CATALOG.md` (the full
Fidelity surface catalog + the Fidelity->Schwab table map). Sibling of NFRA_FIDUPL, which lands the bronze.

---

## PART I -- THE OUTCOME TERRITORY

**DESIGN: OPTION B (Andrew-direct ~15:5xZ).** Silver is **custodian-native and lossless** -- Fidelity silver carries Fidelity's own
fields as they come from bronze. A **matching config / canonical dictionary** holds the conforming logic, and the **gold** layer is built
from it. The uniformity is a GOLD property, produced by the config, not forced into silver. The canonical gold schema is **seeded from the
Schwab silver layout** (so existing Schwab readers meet a familiar shape and Schwab's own mapping is near-identity), but is now a
deliberate canonical, not one custodian's accident. Rejected alternative (Option A, conform-at-silver): it would strand Fidelity-only
richness -- e.g. household Groups, for which Schwab has NO table in silver OR bronze (measured) -- and bake a possibly-wrong field
equivalence into the durable layer.

**Candidate thread (FWD-1):** a data engineer who already reads the Schwab (canonical) positions table points the same code at the
**Fidelity-derived GOLD** positions table and it runs unchanged -- same columns, types, grain -- for one fact (positions), one business
date, end to end. Round 1 proves that one table conforms through the config; later rounds enrich to every table.

### O1 -- A reader cannot tell the custodian apart at GOLD
A data engineer reading the canonical gold tables (positions, accounts, securities, transactions, lots, realized G/L) gets the **same
schema** regardless of custodian; code written against the canonical (Schwab-seeded) schema runs on the Fidelity-derived gold with no
change. Silver stays custodian-native; the uniformity is produced at gold by the config.

### O2 -- Every bronze fact family reaches a native-faithful silver table AND a canonical gold table via the config
For each Fidelity bronze fact family NFRA_FIDUPL lands -- accounts, positions, balances, securities/prices, transactions, open tax lots,
realized gain/loss (and unrealized, at lot grain) -- there is (a) a silver parquet table carrying Fidelity's OWN fields losslessly, and
(b) a canonical gold table built from it by the matching config. Fidelity-only richness (the household Groups) is **preserved in silver**
and surfaced in gold when a canonical table is defined; nothing Fidelity provides is stranded or discarded.

### O2b -- The matching config is the single, readable source of conforming truth
A **config/matching table** records, per canonical gold field, which custodian field feeds it and the transform (rename, unit, enum map),
with a note where the match is only **approximate** (custodians word fields differently -- Andrew's caveat). Gold is constructed from this
config; changing a mapping edits the config and rebuilds gold, **never silver**. The config IS the coalescing logic -- explicit,
inspectable, versioned -- and it is the project's central artifact.

### O3 -- One gold layer serves both custodians from the uniform silvers + the config (no bespoke master required)
An analyst asking a cross-custodian question (holdings, lots, realized gains across a household that has both Schwab and Fidelity accounts)
reads one gold model that unions the two silvers on a `custodian`/`source` dimension, with no per-custodian branching in the gold logic.

**Attribution key (Andrew-direct 15:35Z):** the gold master attributes each account to its advisor/firm from the **custodian-native
grouping id** -- Fidelity **G Number**, Schwab **Master Account Number** -- via a **mapping config** `(custodian, native_group_id) ->
advisor/firm`, resolved at the custodial level and REPLACING any downstream data-vendor assignment. The native id travels on every silver
row (from `fact_acc`) so gold can join to the config without a vendor lookup.

**No standing master table presumed (Andrew-direct 15:38Z):** because the two silvers are formulated identically, gold can **construct
the needed tables by configuration** -- union the uniform silvers, attribute via the mapping config -- rather than materialize a bespoke
master. Whether gold is a config-driven assembly (views) or a materialized set is a gold-layer/DS decision; the uniform silver + config is
what makes either cheap.

### O4 -- The unmappable is named in the config, not hidden
Where a Fidelity field has no canonical gold field (or a canonical field no custodian fills), the gap is recorded **in the matching
config** -- surfaced as an extension/custodian-specific column in gold, or explicitly left unmapped with its reason -- so no field is
silently lost and no canonical column is silently null-filled. A query-time surprise about a column is a failure of this outcome.

### O5 -- Silver runs off bronze as landed, daily and for the backfill
The native silver converter consumes NFRA_FIDUPL's bronze exactly as it lands (daily and the backfilled history: transactions to
~2021-12, realized lots to 2018), partitioned by business date, so silver -- and the gold built from it -- advances automatically as
bronze does.

---

## PART II -- WHERE THE BOUNDARY SITS

| This project (NFRA_FIDSLVR) OWNS | Relies on, does not change |
|---|---|
| The Fidelity **native** silver converters (bronze -> parquet carrying Fidelity's own fields, lossless) | NFRA_FIDUPL's bronze landing (the raw .txt/JSON fact files) -- the input contract |
| The **matching config / canonical dictionary** (custodian field -> canonical gold field + transforms + approximate-match notes) -- the central artifact | The Schwab silver schema (`opal-assets-silver-schwab`), read as the SEED for the canonical gold schema, never altered |
| The **config-driven gold constructor** (canonical tables + `custodian` dimension + native-id attribution) | LGIC naming (`lib/opal_naming.py`), the `fidelity` scopes already registered |

**Named siblings:**
- **NFRA_FIDUPL** -- lands all the Fidelity bronze fact tables (incl. open lots, realized/unrealized G/L as build cells). Upstream; this
  project starts where its bronze ends.
- **The Schwab silver (`opal-assets-silver-schwab`)** -- the **seed** for the canonical gold schema. Not altered. Schwab may itself be
  re-expressed through the same config later (its mapping is near-identity); that is a joint decision, not a unilateral edit here.
- **The per-firm split** (NFRA_FIDUPL) -- orthogonal; silver is built on the Alongside bronze regardless of firm attribution.

---

## PART III -- THE QUALITATIVE BAR

- A Schwab (canonical) reader runs unchanged on the **Fidelity-derived gold** table of the same name -- the test Andrew set, applied at
  gold under Option B. Disputable: point real Schwab-reading code at the Fidelity gold table and see it run or fail.
- An analyst answers a both-custodians question from one gold layer without custodian-specific code.
- A reviewer reads the **matching config** and finds every Fidelity<->canonical divergence named there with its disposition, rather than
  discovering a column surprise at query time; Fidelity silver, read directly, is faithful to Fidelity's own field names.

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
- The **account->advisor/firm mapping config** keyed by `(custodian, native_group_id)` -- Fidelity G Number, Schwab Master Account Number
  -- as the attribution source of truth (who owns/populates it is a gold-layer decision).
- **Attribution and household are TWO SEPARATE canonical dimensions** (CTO ruling on P1 finding @41fa1eeff4, 2026-10-21). Firm/advisor
  **attribution** is keyed by the custodian-native grouping id above; a distinct **household** dimension is seeded from Fidelity's native
  Groups and from Schwab TIN synthesis (Schwab has no clean family grouping -- its `fam` table is stale and `slm` col_6 is the account TIN,
  per-taxpayer; `08335338` carries them, `08242234` does not), **each household row naming its rule**. They cannot share one key: 90
  Schwab households span more than one advisor group, and accounts sit under several masters (a double-count hazard, surprise D1-S19). The
  attribution cell reads this at L5.
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
- It does not confirm which Fidelity `account.txt` / `fact_acc` field carries the G Number (the native grouping id for attribution), nor
  Schwab's Master Account Number field -- that per-field confirmation is the gold attribution step's first check.

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
