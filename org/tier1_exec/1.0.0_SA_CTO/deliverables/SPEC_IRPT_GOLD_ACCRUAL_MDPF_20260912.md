# SPEC FOR REVIEW -- `opal-data-mdpf/investor-reporting/` : the IRPT gold accrual layer

⛔ **THIS IS A SPECIFICATION FOR ANDREW'S REVIEW. IT IS NOT LAW, NOT A PRD ADDENDUM, AND AUTHORIZES
NOTHING.** Nothing is built, moved or deployed from this document. It exists so the shape can be
argued with before it becomes binding. Author `1.0.0_SA_CTO`, 2026-09-12.

**Andrew-direct that produced it** (~15:0xZ, this terminal, VERBATIM): *"if there is actually model
portfolio data that needs to be presented (i.e., the third tab in Investor reporting dashboard page),
then the shape for that needs to be designed within an investor reporting sub folder in
opal-data-mdpf."* And: *"all references for the data in the first place should be in opal/data-assets."*

---

## 1. WHY THIS LAYER EXISTS -- one sentence

The Holdings tab needs three firms' model data in **one shape**; the estate forbids one principal
holding three firms' identity data; **an accrual layer resolves both**, because each firm's
silver -> gold run reads only its own firm and the consumer then reads one derived, firm-partitioned
plane instead of reaching into three vendors' silver.

⭐ **This is the layer the current build SKIPS.** `directory_runner.py` reads three firms' silver
directly in one process and writes platinum straight out. That skip is the whole reason the
cross-firm wall was hit at all.

## 2. THE PLANE MODEL THIS SITS IN

| plane | home | form | who writes |
|---|---|---|---|
| bronze | `opal-data-assets/<vendor>/<firm>/bronze/` | vendor drop | vendor ingest |
| silver | `opal-data-assets/<vendor>/<firm>/silver/` | parquet, `date=` partitioned | firm pipelines |
| **gold (this spec)** | **`opal-data-mdpf/investor-reporting/`** | **parquet, firm-partitioned** | **one accrual run PER FIRM** |
| platinum | `opal-data-portal-v2` *(or firm bucket -- §7, UNRESOLVED)* | JSON | IRPT publisher |

⚠ **DEPENDENCY, NOT PART OF THIS SPEC:** inflection's `silver/api_dims/` is in `opal-data-inf`, not
assets. Andrew has ruled it repointed for pattern. **This spec assumes silver reads resolve in
`opal-data-assets` and does NOT specify the repoint** -- that is its own scope with a live consumer
and three years of dead partitions in the same plane (D10 lane).

## 3. FOLDER LAYOUT

```
opal-data-mdpf/investor-reporting/
  gold/
    dim_model/            firm_id=<firm>/date=<YYYY-MM-DD>/data.parquet + manifest.json
    fact_model_holding/   firm_id=<firm>/date=<YYYY-MM-DD>/data.parquet + manifest.json
    dim_account_model/    firm_id=<firm>/date=<YYYY-MM-DD>/data.parquet + manifest.json
    dim_security/         firm_id=<firm>/date=<YYYY-MM-DD>/data.parquet + manifest.json
  _manifests/
    <firm>/<date>/accrual.json
```

**`firm_id=` IS THE FIRST PARTITION KEY, DELIBERATELY.** It makes the per-firm IAM condition a
prefix condition (`investor-reporting/gold/*/firm_id=<firm>/*`), which is CLAUDE.md's named
shared-bucket shape. A firm-second layout would make the fence unexpressible.

**`date=` IS THE BUSINESS DATE, never the run date** -- `directory_runner.py` already resolves a
business date by intersecting source partition completeness, and that discipline carries.

## 4. THE FOUR TABLES

Fields below are grounded in the `HoldingsSnapshot` contract's eleven required-meaning items and in
`dim_model_portfolio`'s twelve REAL columns, read from `blackdiamond/cottonwood/gold/` this session.
⛔ **Nothing here is invented vocabulary.**

### 4.1 `dim_model` -- one row per model, per firm, per date
Carried from source where it exists (cottonwood's `dim_model_portfolio` supplies all twelve):
`model_id`, `model_name`, `rebalance_model_type`, `is_opal`, `account_count`, `dollar_value`,
`accounts_with_value`, `accounts_missing_value`, `is_decomposed_target`, `is_direct_assignment`,
`assignment_date`, `value_date`.
Added by the accrual: `firm_id`, `model_id_ns` (namespaced -- §5), `category_node`, `category_axis`,
`source_revision`.

### 4.2 `fact_model_holding` -- the tab's substance
`firm_id`, `model_id_ns`, `security_id_ns`, `account_id_ns`, `basis` (observed | assigned | target),
`amount`, `denominator`, `pct_of_parent`, `pct_of_total`, `as_of`, `business_date`,
`source_revision`, `coverage_flag`.
⛔ **`amount` NEVER travels without `denominator`.** The contract names "amount + denominator" as one
item; splitting them is how a percentage becomes unfalsifiable.

### 4.3 `dim_account_model` -- the drill path
`firm_id`, `account_id_ns`, `model_id_ns`, `assignment_basis`, `assignment_date`, `is_unassigned`.
⛔ **`is_unassigned` IS A FIRST-CLASS ROW, NOT AN ABSENCE.** FWD-5 requires unassigned assets
*preserved*; an account missing from this table and an account explicitly unassigned must not read
the same.

### 4.4 `dim_security` -- the underlying
`firm_id`, `security_id_ns`, `display_name`, `category_node`, `category_axis`, `source_revision`.

## 5. THE FIVE RULES THAT MAKE IT SAFE

1. **ONE FIRM PER RUN.** The accrual is invoked per firm and reads only that firm's silver. No
   process ever holds two firms' identity data. This is the whole isolation argument.
2. **NAMESPACED IDS ONLY.** `model_id_ns`, `security_id_ns`, `account_id_ns`. The contract says
   "namespaced model/security ids" and "vendor ids server-side". ⛔ A raw vendor id must never appear
   in a gold row that a platinum publisher can reach.
3. **TAXONOMY IS RESOLVED, NEVER RE-COINED.** `category_node` / `category_axis` come from
   `mdpf_category_registry` via `resolve()` / `axis_of()`. ⛔ **Residual is ARITHMETIC, never a
   registered member** -- the registry's `residual_is_arithmetic()` says so and an accrual that
   writes a Residual row breaks its own coverage check.
4. **COVERAGE AND REMAINDERS ARE CARRIED, NOT RECONCILED AWAY.** `coverage_flag` plus the manifest's
   remainder totals. An accrual that silently balances is the failure this estate has spent the week
   naming.
5. **EVERY TABLE CARRIES `source_revision`.** Provenance is a contract item, and the platinum layer
   must be able to state which silver vintage it rests on.

## 6. THE ACCRUAL MANIFEST

`_manifests/<firm>/<date>/accrual.json` -- the run's own record: business date and how it was
resolved, per-source partition vintages, row counts per table with denominators, coverage and
remainder totals, registry version, `source_revision`, and the schema version. **A downstream reader
should never have to open a parquet to learn whether the day is complete.**

## 7. ⛔ FOUR THINGS THIS SPEC DOES NOT DECIDE

1. **Where platinum lands.** Your law says `opal-data-portal-v2`. The live estate serves *scoped*
   platinum from firm buckets behind the validator (AdvisorIntelligence, behaviors 2/3/4/16/27), and
   the ownership map that gates it is itself stored that way. **Holdings carries names and values, so
   it is scoped-shaped.** That is your call and this spec is written to work either way -- the gold
   layer does not change.
2. **Whether the other two tabs accrue here too.** This spec covers Holdings (the third tab) because
   that is what you named. Reporting and Analysis have different sources and may not want this shape.
3. **The inflection repoint** (§2).
4. **Who runs it.** Your dedicated-runner ruling stands; which host, and whether one runner invoked
   three times or three runners, is an infra cut.

## 8. WHAT I WOULD WANT CHALLENGED

- **Is four tables right, or is `dim_security` premature?** It may belong to an existing security
  master rather than to IRPT.
- **`firm_id=` first** costs a slightly awkward path; I chose it because it makes the IAM fence a
  prefix condition. If you would rather fence by bucket later, the layout should change now.
- **Does `fact_model_holding` need account grain at all**, or is model-grain enough with accounts
  reached by drill ref? The contract names "drill refs" separately, which hints the latter.
