# RESEARCH: a firm-neutral source for the five Opal models' {ticker: weight} (IRPT_ANLREQ FWD-10)

For `1.0.0_SA_CTO~DELL2`, msg 11370 (a design fork; the CTO rules). Author `4.0.0_SA_CRO~TCKT`, 2026-10-20 ~15:1xZ.
Read-only. Tags: M = measured (a code or registry line read at origin/CLOUD, or a live read-only list); I = inferred.

## The question
Where does the resident (`irpt-ycharts-runner-role`, i-0167fd745ad906a66) read the five Opal models' weights as of the
report window? The source must be held in no partner firm's bucket (CLAUDE.md section 5).
Input: `0.9.0_WK_IRPT_ANLREQ~304` MODEL_COMPOSITION_TRACE.md @ff04557258. It found no reader, no grant and no firm-neutral
bucket on the MDPF path.

## Sources found

| # | Source | Firm-neutral | Per-date history | Format | Current consumers | Registry |
|---|---|---|---|---|---|---|
| A | `opal-data-portal-v2/benchmarks/model_YYYYMMDD_v1.pkl`, frame `holdings` (long: date, ticker, weight, model; model in UST, ST, INT, LT, ULT) | YES: the yang/global scope (M) | YES (I) | pickle | `yang-generate-positioning`, `yang-model-portfolio-benchmarks`, `portal_data_proxy` | stem `benchmarks/model_` ruled "none owed, writer not ruled" (key_rulings.json:1172) (M) |
| B | `opal-data-portal-v2/json/positioning/positioning_data.json` (per-model current holdings with weights) | YES (M) | NO: newest date per model only (M) | JSON | the portal Positioning tab; gateway `portal_get_model_positioning` (I) | canonical `yang/global/platinum/positioning/positioning-data.json` (key_rulings.json:878) (M) |
| C | `opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json` (model RETURN series, built from the data pkl's `return_daily`) | YES (M) | YES, daily returns; carries NO weights (M) | JSON | the Performance and benchmark surfaces | canonical `yang/global/platinum/benchmarks/model-portfolio-timeseries.json` (key_rulings.json:821) (M) |
| D | MDPF silver `opal-data-mdpf/mdpf/feeds/model_composition/<firm>/<date>.parquet`; Orion bronze `opal-data-assets/mdpf/inflection/bronze/orion_model_composition/` | NO: keyed by firm; the bronze sits under R4's custodial spine with a literal firm segment (trace Q1-Q2) | YES, daily per firm | parquet / JSON | MDPF aggregate AUA; the gateway's `mdpf_get_model_composition` (one firm scope, newest partition, Opal principals) | silver address is hand-typed, not builder output (trace S3) |

Evidence for each source (M unless marked):
- **A.**
  - The 114 objects run through `benchmarks/model_20261019_v1.pkl`, listed 2026-10-20. They are written daily at about
    11:0xZ, and each is about 18 MB and grows every day.
  - The `holdings` frame and its per-model latest-date logic are read in
    `infra/aws/lambda/v2_portal/yang_pipeline/positioning/yang-generate-positioning/lambda_function.py:1806-1864`.
  - **I:** that every pkl carries the full holdings history. This follows from the per-model "latest date" selection and
    the growing size. No pkl was unpickled.
- **B.** The generator keeps each model's latest date only (same file, `:1842-1864`).
- **C.** `yang-model-portfolio-benchmarks/lambda_function.py:1-31` and `:46-49`.
- **D.** Trace Q1-Q2, Q5.

Other measured facts:
- **IAM.** The runner role holds five inline policies (list-role-policies, read 2026-10-20):
  - irpt-export-render-host-evidence;
  - irpt-export-render-host-parameter-fence-policy;
  - irpt-export-render-host-token-policy;
  - irpt-ycharts-runner;
  - irpt-ycharts-runner-resident-policy.

  Its resident policy grants S3 read only on the reporting families and `opal-data-etfs/bbg/*` (trace Q5, from
  Terraform). No grant reaches `opal-data-portal-v2` (I: the live policy documents were not re-read).
- **Cross-firm guard.** `.tools/ds-precommit-check.py:69-116` enumerates only `data/black_diamond/` and `data/cot/`.
  It would refuse nothing here: the guard is only as wide as its list. Section 5 still binds by reading, and D is the
  source it forbids.
- **Model codes.** The yang surfaces key the models as UST, ST, INT, LT, ULT. The catalogue's `templates.json` keys them
  as opal_* with four YCharts `P:` vendor ids. The code-to-catalogue map is not written down (trace Q6 and surprise
  W304-S1); a reader must carry it.

## Does the report need weights?
- **Core (O2 of the engine brief)** compares the portfolio with each Opal model by RETURNS: return, risk and the
  performance chart. Source C already holds those returns, firm-neutral and daily. **Core needs no weights** (I, from
  the brief's split).
- **Parity (O3)** needs weights for the model's exposures (sector, region, style), its holdings table and its
  fundamentals. FWD-10's weight read is a PARITY dependency, and it should not hold Core.

## Ranked recommendation
1. **For Core: read source C. No weights.**
   - It is a firm-neutral, registered, daily return series: the same numbers the Performance tab shows, so the report
     and the portal agree.
   - Act: one read grant (`s3:GetObject` on that one key) on the resident policy, by Terraform `safe-apply`. This is a
     `WORLD` deploy with a ledger entry. It widens access, not served output, so it is a COO+CTO packet like the
     10-20 IAM grant (I).
2. **For Parity weights: a dated JSON extract of A's `holdings`, written by the yang job that already unpickles it.**
   The extract is `{as_of: {UST|ST|INT|LT|ULT: {ticker: weight}}}`, keyed by the T-1 frontier date that C-PRICES uses.
   The resident then reads that JSON, never the pickle:
   - unpickling inside the resident is arbitrary code execution and couples it to the pandas version;
   - the pkl is 18 MB per read.

   The address is **builder output: registry row missing**. The natural family is under `yang/global/platinum/positioning/`
   (beside `positioning-data.json`). Add the row in `infra/logic/registry/` and print `address()` in the PRD. Do not
   hand-type a key.
3. **Interim for Parity, if 2 lags: source B (current weights only).**
   - The report's as-of is always the T-1 frontier (C-PRICES v0.16, no price-date input), so "current" equals the
     report window except across a rebalance on the boundary day.
   - It is registered and firm-neutral, but has no history.
- **Rejected: D (MDPF silver, Orion bronze, `mdpf_get_model_composition`).**
  - It is keyed by firm, so a report for one firm reading another firm's partition crosses firms (section 5).
  - The bronze sits in the custodial spine (R4).
  - The gateway tool returns one firm's newest partition only.
  - The silver address is hand-typed.

## What this does NOT claim
- No pkl was unpickled. That the `holdings` frame holds history on every date is inferred (see A).
- The live IAM policy documents, bucket policies and `positioning_data.json` contents were not read (only the object
  keys and the code).
- Whether the yang models (UST to ULT) are exactly the five Opal models of the catalogue rests on the display-name match
  (trace Q6). The map must be written down.
- No cost or latency was measured. The ruling is the CTO's.
