# MDPF_SECCLASS decomposition -- ROUND 7 (issuer 2.0.0_SA_COO~M; drafted and ISSUED 2026-10-05 ~06:4xZ)

**Status: ISSUED** in ONE issuance, as a workstream disjoint from the multi_asset packet (rule 27). CTO msg 105182: "FWD-9 and
FWD-10 are cuttable now ... leg V's 10:15Z read does not gate them".

**Cut on:**
- PRD v0.3 @ffb329af49, addendum v0.3 (C-BACKFILL; the input is ETFS_RIVALS' served artifact; vendor and moratorium notes).
- This seat's intake `decompositions/MDPF_SECCLASS_R7_INTAKE_FWD9_FWD10.md` @320b02aa6b: the measured universe and Q1-Q5.
- 1.0.0_SA_CTO RULINGS batch 257 @a272c26a75:
  - **Q1:** BLOOMBERG namespace, key `BBG:<ticker>:<exch>` with no whitespace; `security_bloomberg` verbatim in its own
    attribute; the reader census comes first.
  - **Q2:** history is site Z's input; this project reads coverage and routes gaps through `0.0.0_AB_MSTR`.
  - **Q3:** GICS where resolved; else the exchange country, held as data, mapped to the vocabulary's regional sub-class;
    else `low_confidence`.
  - **Q4:** "stock" = `provider_security_type` Equity and non-cash.
  - **Q5:** FWD-10 is a scheduled producer. Measure which Opal ETFs canonical_shape already carries; read the Opal silver
    holdings only for the rest.
  - The R7 row write runs under its own never-widen half, dry run first.

**Rule 24.** The domain is FWD-9 (rows + history) and FWD-10 (the routine).
- FWD-9 rows split into the namespace's precondition (the reader census, Q1) and the row set + writer.
- FWD-9 history is a READ of site Z's series (Q2).
- FWD-10 is one producer.
- That gives four cells, one intent each, with no remainder. The write ACT itself is not a worker cell: it is the issuer's act
  under its own half, after the census reads tolerated.

**Measured constraints (read at the base, 2026-10-05):**
1. **The input.** canonical_shape: 504 daily partitions, 2024-09-30 to 2026-10-02, 13 funds, 300,030 rows.
   - 822 distinct non-cash securities by `security_bloomberg`: US 178, non-US 516, `Index` futures 17.
   - 0 non-US rows carry an ISIN or CUSIP.
   - In the table, 139 of 177 US tickers have rows.
2. **The vocabulary.** The table's `equity` `sub_asset_class` values include the regional values `International` (238 rows),
   `Global` (67), `EM` (50) and `Developed` (45), and the GICS sectors used for single stocks (`Financials` 46,
   `Information Technology` 43, ...). So Q3's regional mapping has targets and no row is owed first. This mixes two axes
   (size/region and sector); it is pre-existing and noted, not changed here.
3. **History.** The only holding dialog with a series is Rival Funds'
   (`data/etfs/scripts/rivalfunds/render.py:1321-1368`). It reads G4 `security_market` at
   `opal-data-etfs/rivalfunds/etfs/gold/security_market/date=<D>/market-<rev>.parquet`. The producer is
   `enrichment_bloomberg.py`, with a 730-day backfill default, at site Z.
4. **The FWD-7 planner and writer** (`infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py`) put only on
   absence (`:506`) and call no LLM (`:30-31`). Wired through E_18, it never fills `instrument_kind` (`:405-420`).
5. **Opal ETF holdings:** `s3://opal-data-etfs/silver/holdings/{run_date}.parquet`
   (`infra/aws/lambda/etfs-pipeline/etfs-netassets-daily/lambda_function.py:1501-1508`), on `cron(0 22 * * ? *)`.

## The cells

| cell | what | serves | status | placement | risk | chain / slot |
|---|---|---|---|---|---|---|
| `SC-e-16` | The BLOOMBERG-namespace reader census: every reader of `etf-classifications` exercised on a `BBG:<ticker>:<exch>` row (`identifier_namespace BLOOMBERG`, a `security_bloomberg` attribute); a verdict per reader | FWD-9 (Q1 precondition) | NOT-EVALUATED | laptop | LOCAL | A, `0.9.0_WK_MDPF_SECCLASS~13` |
| `SC-e-17` | FWD-9 rows: the shared mapping module (one canonical_shape row -> one table item, Q1/Q3/Q4), the universe row set against the table, a dry-run writer through `etf_classification_scheduled.write`, and the R7 rows half | FWD-9 | NOT-EVALUATED | laptop | WORLD | B, `0.9.0_WK_MDPF_SECCLASS~14` |
| `SC-e-18` | FWD-9 history coverage: each FWD-9 security's G4 `security_market` coverage back to `min(3y, first trading day)`, the gaps listed for routing to site Z (Q2) | FWD-9 | NOT-EVALUATED | laptop | LOCAL | C, `0.9.0_WK_MDPF_SECCLASS~15` |
| `SC-e-19` | FWD-10: the scheduled producer. It detects stocks newly in the rival canonical_shape and in Opal ETFs (canonical_shape first, Opal silver holdings only for the ETFs it lacks), plans through `SC-e-17`'s module, and writes on absence. Built, tested and dry-run against live inputs. Runtime home, names and the read grant on `opal-data-etfs/rivalfunds/etfs/gold/` come from builder output in declared Terraform, not applied. | FWD-10 | NOT-EVALUATED | laptop | WORLD | B, after `SC-e-17`, `0.9.0_WK_MDPF_SECCLASS~16` |

## Write sets (disjoint)

- **SC-e-16:** `R7_CHECKS/r7_bbg_reader_census.py`, `R7_BBG_READER_CENSUS_20261005.json`, the surprise channel.
- **SC-e-17:**
  - `infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py` and
    `infra/aws/lambda/v2_portal/_shared/tests/test_rivalfunds_classification.py`;
  - `R7_CHECKS/r7_fwd9_row_set.py`, `R7_CHECKS/FWD9_ROW_SET_20261005.tsv`, `R7_CHECKS/r7_fwd9_write.py`;
  - `NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD9_ROWS_20261005.md`;
  - the surprise channel.
- **SC-e-18:** `R7_CHECKS/r7_fwd9_history_coverage.py`, `R7_FWD9_HISTORY_COVERAGE_20261005.json`, the surprise channel.
- **SC-e-19:**
  - `infra/aws/lambda/mdpf-secclass/new-security-classifier/` (`lambda_function.py`, `tests/`);
  - `infra/aws/terraform/mdpf-secclass/new-security-classifier/`;
  - `infra/logic/registry/` rows ONLY if the naming builder refuses (rule 30: a refusal is a missing row);
  - `R7_CHECKS/r7_fwd10_dry_run.py`;
  - the surprise channel.
- `R7_CHECKS/` and the `.md` / `.json` files sit under `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/`.

**Ordering and fan-out:**
- `fanout: 3` at issue: chains A (`SC-e-16`), B (`SC-e-17` then `SC-e-19`) and C (`SC-e-18`).
- `SC-e-19` imports `SC-e-17`'s module, so it starts after `SC-e-17` drains.
- The R7 rows ACT (the issuer's) runs after `SC-e-16` reads tolerated and both halves are signed.
- The FWD-10 apply is an issuer act under its own half after `SC-e-19` drains.
- `SC-e-18` is independent.

**Lane:** the new paths of `SC-e-17` and `SC-e-19` need a lane grant (`.owned-paths.yaml`, the CTO's carrier); it is asked in the
issuance message.
