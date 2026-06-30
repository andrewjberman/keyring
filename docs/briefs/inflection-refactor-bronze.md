# Refactor SPEC-1: Inflection — BRONZE / Ingestion layer

**Author:** 3.0.0_SA_CVO (Andrew-direct refactor planning, ADVI_BREAKS unified-flow) | **Date:** 2026-06-30
**As-is reference:** `inflection-bronze.md` (audit). **Next:** SPEC-2 silver.
**Status:** DRAFT for end-to-end validation → CTO PRD. Decisions marked [ANDREW-LOCKED] or [DECISION] (needs ratification).

---

## 0. Governing principles (Andrew-locked, this layer)

1. **Bronze is RAW. No conversion at bronze.** Each dim lands in **whatever format the endpoint returns** (CSV stays CSV, JSON stays JSON). Format normalization to parquet is a **SILVER** function, never bronze. *(Corrects the prior all-parquet-at-bronze proposal — that conversion belongs in silver.)*
2. **Bronze takes ALL FIELDS. No redaction, ever.** Bronze is raw + complete from each endpoint. Fact→dim selection, field choices, and slimming are SILVER decisions (Rule 17 governs silver). Bronze never drops a field.
3. **Bronze's only job = ingestion + consistent bucket structure.** The consistency we enforce at bronze is the **folder layout**, not the file format.
4. **Single execution layer = the EC2.** All pulls run unified on `inf-gold-layer-runner` EC2 (the same machine that will run silver+gold). No parallel cron-Lambda pull layer.
5. **Eclipse is kept and pulled in full daily**, raw, into a consistent bronze structure — downstream silver/gold use TBD (we decide later; we do not discard the data).

## 1. Target bronze layout (structure is what we unify, not format)

```
 s3://opal-data-inf/bronze/orion-api/{YYYY-MM-DD}/        ← ONE folder for ALL Orion REST dims
   transactions.csv        tax_unrealized.csv   tax_realized.csv
   billing.csv             performance.csv      unified_account_dim.csv     (Envision ExcelReports → native CSV)
   representatives.json    household_rep_mapping.json     new_portfolio_accounts.json
   positions.json          assets.json                                       (v2 REST → native JSON, RAW — see §3)

 s3://opal-data-inf/bronze/eclipse/{YYYY-MM-DD}/          ← consistent Eclipse raw landing
   portfolios_simple.json  portfolios.json   models.json   model_composition.json   [+ all other reachable endpoints — §4]
```
**Eliminated:** `bronze/orion-api-v2/` (merged into `bronze/orion-api/`), `bronze/positions/`, `bronze/assets/` (own-prefix parquet). One datestamped folder per source family; one file per dim in its native format.

## 2. Single pull layer on the EC2

- The EC2 pulls **all** dims into bronze (today the inline chain pulls only 6; `tax`, `billing`, `unified_account_dim` are cron-Lambda-only — they move onto the EC2).
- **Decommission** the 9 standalone cron Lambdas + their EventBridge rules (retro §5).
- **One pull script per dim** — retire the duplicate implementations: `transactions_v2.py` vs `transactions_rest.py`; `performance_dim.py` vs `performance_rest.py` (keep one each; the `_rest` copies live in `data/inf/manual_api/`).
- **Uniform resume/skip** [DECISION, rec: yes]: every dim skips re-pull if its `{date}` file already exists (idempotent re-runs); today only positions/assets have this guard.

## 3. positions + assets — the raw-bronze correction (grounded)

Both currently do `r.json()` (Orion returns **JSON**) → `pd.DataFrame` → `to_parquet` → own prefix. That is bronze doing format conversion. **Refactor:**
- Bronze lands the **raw JSON** response: `bronze/orion-api/{date}/positions.json`, `.../assets.json`. No parquet at bronze.
- The JSON→parquet conversion **moves to silver** (the `positions_mv` silver dim already emits parquet — repoint its converter to read the raw bronze JSON instead of a pre-made bronze parquet).
- Net: positions/assets stop being structurally + format special; they become ordinary raw-JSON bronze dims like representatives.

## 4. Eclipse — keep + pull everything (Andrew-locked)

- Pull **all reachable Eclipse endpoints** daily, raw, into `bronze/eclipse/{date}/<endpoint>.json`. Currently 4 are pulled (`/v1/portfolio/portfolios/simple`, `/v1/portfolio/portfolios`, `/v1/modeling/models`, `/v1/modeling/models/{id}`) + `/v1/admin/Token` (auth).
- [DECISION/spec task] **Enumerate the full Eclipse API surface** — the current 4 are what today's script happens to call, not a confirmed-complete set. Catalog the available endpoints and pull all that return firm data.
- Downstream: no silver/gold required yet (the existing `INF_E_00`/`silver/eclipse` flow stays as-is or idle); we retain the raw data and decide use later.

## 5. Retroactive / migration work

- **R1 — Decommission cron-Lambda pull layer:** disable + remove EventBridge rules `inf-api-reps`(30 12), `inf-accounts-v2-daily`(35 12), `inf-unified-account-dim-daily`(40 12), `inf-api-assets-v2-daily`(45 12), `inf-api-positions`(50 12), `inf-tax-daily`(55 12), `inf-api-txn`(0 13), `inf-billing-daily`(35 13), `inf-performance-daily`(40 13); retire the Lambda functions + their pull scripts (per Terraform `infra/aws/terraform/inf-pipeline/`). Move all pull logic onto the EC2 chain.
- **R2 — positions/assets de-convert:** stop the at-bronze parquet write; land raw JSON in the unified folder; update the silver positions_mv/assets converters to read the new raw JSON path. Validate the silver output is byte-equivalent to today's (parity gate).
- **R3 — Folder migration:** [DECISION] go-forward only (new layout from cutover date) + on-demand backfill, OR relocate existing `orion-api-v2/`, `positions/`, `assets/` history. Rec: **go-forward + on-demand backfill** — bronze history is already consumed into silver/gold, so a full relocate is low-value; keep old prefixes read-only until silver no longer references them.
- **R4 — Duplicate-script retirement:** pick one pull script per dim; delete the other; update the chain step registry.
- **R5 — Eclipse structure normalize** to `bronze/eclipse/{date}/` + endpoint enumeration (§4).

## 6. Acceptance criteria (machine-checkable → PRD/TO)

- AC1: every Orion REST dim lands under `bronze/orion-api/{date}/` — `bronze/orion-api-v2/`, `bronze/positions/`, `bronze/assets/` receive no new writes.
- AC2: `positions.json` + `assets.json` at bronze are valid raw JSON (NOT parquet); a `.parquet` for these appears no earlier than silver.
- AC3: a bronze file exists for all dims for the run date, produced by the EC2 (no cron-Lambda invocation in the window); the 9 EventBridge cron rules are `DISABLED`/removed.
- AC4: **completeness** — each bronze dim carries the full field set the endpoint returns (schema-completeness assertion per dim; no field dropped at bronze).
- AC5: exactly one pull script per dim in the chain registry.
- AC6: Eclipse — all enumerated endpoints land raw daily under `bronze/eclipse/{date}/`.
- AC7: silver outputs post-refactor are parity-equal to pre-refactor (the de-convert + repoint introduced no value change) — validated several days before cutover.

## 7. Noted for the FINAL refactor step (Andrew-flagged, NOT this layer)

**EC2 OTP fallback protocol.** The Orion JWT refresh depends on a human OTP relay (`inf-otp-relay`, `s3://opal-data-inf/otp/`). Once the unified EC2 flow is in place, assess a manual-OTP fallback solution modeled on the Black Diamond approach, so a JWT lapse has a defined recovery path. This is the LAST step of the overall refactor — recorded here, specced when we reach it.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| grep/read inf-pipeline pull scripts (positions/assets r.json→to_parquet; eclipse endpoints) | the raw-bronze correction + Eclipse endpoint set | PASS (rail-checked) |
| live S3 + TF (bronze layout, EventBridge rules) | as-is grounding (see inflection-bronze audit) | PASS |

— 3.0.0_SA_CVO
