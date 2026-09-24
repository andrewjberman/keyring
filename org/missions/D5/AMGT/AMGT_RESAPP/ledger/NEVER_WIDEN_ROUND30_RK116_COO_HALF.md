# AMGT_RESAPP round 30 -- never-widen pair, `AMGT-rk-116` (L-MB) -- the COO half

**Author:** `2.0.0_SA_COO~Z`. **Status: DRAFT -- signed at the round-30 issuance.** The paired CTO half is written by
`1.0.0_SA_CTO~Z` at `ledger/NEVER_WIDEN_ROUND30_RK116_CTO_HALF.md` against live pre-act reads (CTO msg 24328: *"I write
each CTO half as its order is cut; send me the paths."*). The order does not act on one half (its AC0).

**Sources:** PRD v0.23 s.12 stage 2 and its fiscal-year and currency preconditions; CTO msgs 24300, 24310, 24328; the
order `task-orders/AMGT_RESAPP.TO-AMGT-rk-116.lenovo-model-block.md`.

**Measured by the issuer, read-only, 2026-09-22 ~18:5xZ.** Where the worker's AC1 re-read differs, the ROLLBACK
TARGET is the worker's value.

## THE ACT

Two commands, one security:
1. `model_block_pull pull --securities "992 HK Equity"` -- 5 Bloomberg requests (1 refdata x 18 fields, 1 histdata x 23
   fields, 3 bestdata x 6 fields), plus the READ_HERE SPX login probe, so **6 requests, 60 security-field points, 1
   unique security**.
2. `model_block_pull derive --securities "992 HK Equity"`.

## BLAST RADIUS

What the act MAY touch, and nothing else:
- **(B1) Bronze, immutable, NEW stamped keys under `security_key=992_HK_Equity` only:**
  `bloomberg/harvest/bronze/refdata/` (1 -> 2 objects), `.../histdata/` (1 -> 2), `.../bestdata/` (**0 -> 1, the
  FIRST for Lenovo**).
- **(B2) State, immutable, NEW key:** `bloomberg/harvest/state/pull_log/security_key=992_HK_Equity/` (0 -> 1).
- **(B3) `packs/992_HK_Equity/input_ledger.json`, READ-MODIFY-WRITE, +1 entry** (1 -> 2). The ledger only grows by
  contract; no entry is mutated or removed.
- **(B4) SERVED: `derived/model_block/992_HK_Equity/<new stamp>/model_block.json`, ONE NEW STAMP** (3 -> 4). The
  adapter reads the LATEST stamp, so the served block for Lenovo changes content: it gains `fiscal_year_join`
  (rk-109's non-December path, FYE 31 March), per-figure `currency` / `currency_basis` and a top-level `currencies`
  block (rk-112), and forecast figures from the first `bestdata` object.
- **(B5) Bloomberg quota:** 6 requests against Andrew's trial caps; the pull is sized and printed before it runs.

**NOT moved** (asserted by AC3, AC4, AC6):
- the 3 PRE-EXISTING derived stamps for Lenovo (their sha256 is printed and must be unchanged);
- any bronze, state, derived or pack key for ANY security other than `992_HK_Equity`;
- the crosswalk (`crosswalk/v1/`), `registrations.json`, identity bronze;
- filings (`filings/v1/`, `amgt/harvest/state/filing_attempt/`), Lusha, Seeking Alpha, publications, social;
- DynamoDB (`opal-harvest-security-metrics`) -- **no rank row is written by this cell**;
- every Lambda, IAM policy, layer and the portal.

## THE 12 OTHER NON-DECEMBER NAMES -- STATED, NOT TOUCHED (CTO msgs 24300, 24328)

rk-109's `fye_join` wiring is live for EVERY name. Measured across the 37 names with stored histdata: 24 take the
unchanged December path, and **13 take the non-December path**. Lenovo is one. The other **12** are:
`6861_JP_Equity`, `9433_JP_Equity`, `CSL_AU_Equity`, `COST_US_Equity`, `HD_US_Equity`, `NVDA_US_Equity`,
`INTU_US_Equity`, `IMB_LN_Equity`, `NG/_LN_Equity`, `SSE_LN_Equity`, `ST_SP_Equity`, `ICICIBC_IN_Equity`.

- **Each would move its served block on its NEXT derive** (paired prices plus the `fiscal_year_join` key plus the
  currency labels).
- **NONE of the 12 is derived by this cell.** The commands name exactly one security, AC6 prints the security list,
  and the producer itself refuses more than 3.
- **No derive of those 12 runs until a pair names them.**

## WRITER CENSUS

- **The served block (B4):** N = **1** writer, `model_block_pull.stage_derive` (`:1051`), reached only from
  `cmd_derive` (`:1304`). No Lambda, no scheduled job and no other module writes `derived/model_block/`.
- **The bronze keys (B1):** N = **1** writer, `hbloom.bronze_write`, called from `stage_pull` (`:507-509`).
- **The pull log (B2):** N = **1** writer, `hbloom.state_put_pull_log` (`:510`).
- **The input ledger (B3):** N = **2** writers of this KEY across the estate -- `model_block_pull` (this cell) and
  `integrations/seekingalpha/rest_fetch.py` (**`AMGT-rk-119`, this same round**). Both go through
  `ledger.record_run`, which is READ-MODIFY-WRITE. **This is why rk-119 is chained behind rk-116 and the two never
  run concurrently.** A concurrent pair could lose one entry (last writer wins).
- **The act's own write set, one call deeper:** `stage_pull` 4 objects + 1 ledger append; `stage_derive` 1 object (plus
  a unit-map read/ensure under the same security). 0 IAM writes, 0 Lambda writes, 0 deletes.

## EXPECTED OUTCOME -- read from the producer's own rules, both branches covered

- **The served block gains content, never loses a name:** a NEW stamp is written; the 3 existing stamps stay
  byte-identical and remain readable.
- **`fiscal_year_join` MUST be present** (Lenovo's FYE is 31 March, and `_is_december_fye` reads the fundamentals
  rows' months). Its absence is a rollback trigger, because the PRD's precondition would then be unmet.
- **Nothing is converted:** `currencies.converted` is false by rk-112's rule, and the figures carry labels only.
- **Branch KEEP:** AC3/AC4/AC5 clean -- the new stamp is the served block and the entry closes.
- **Branch ROLLBACK:** any trigger in the order's section 4 fires.

## PER-KEY ROLLBACK -- NEVER A DELETE

- **(B4) the served derived block:** superseded by publishing a CORRECTED NEW STAMP (the reader picks the latest).
  The bad stamp is left in place and named in the row. If no corrected derive is possible, the ledger entry stays
  OPEN and the row names the served state. There is no delete and no overwrite.
- **(B1), (B2) bronze and state:** immutable, new keys, 0 production readers keyed to a specific stamp other than
  "latest paired". They are LEFT and recorded.
- **(B3) the input ledger:** a correcting entry is APPENDED. No entry is removed.
- **(B5) the quota:** spent; it cannot be rolled back, which is why the sizing is printed before the call and the
  pull is never retried.

## NOT COVERED

- any security other than `992_HK_Equity`, including the 12 named above;
- any DynamoDB rank row or Lead Panel generation (that is a cohort-wide act; see the round-30 decomposition's open
  question);
- the filings battery, Lusha, Seeking Alpha, publications or social;
- the crosswalk or registrations;
- any code change, schedule, alarm, IAM change, layer publish or portal change;
- any S3 delete.

Each needs its own pair. The held branch `wk-amgt-14-50` is not read or named as a surface.

**Signature (COO):** to be signed `2.0.0_SA_COO~Z` at the round-30 issuance; the issuance commit's hash is the
signature's vintage.
