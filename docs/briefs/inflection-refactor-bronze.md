# Refactor SPEC-1: Inflection — BRONZE / Ingestion layer

**Author:** 3.0.0_SA_CVO (Andrew-direct refactor planning, ADVI_BREAKS unified-flow) | **Date:** 2026-06-30
**As-is reference:** `inflection-bronze.md` (audit) — its **Appendix A is the authoritative literal pull contract** (exact endpoints + file format per domain + the "portfolio" false-friend non-equivalence). **Next:** SPEC-2 silver.
**Status:** DRAFT for end-to-end validation → CTO PRD. Decisions marked [ANDREW-LOCKED] or [DECISION] (needs ratification).

---

## 0. Governing principles (Andrew-locked, this layer)

1. **Bronze is RAW. No conversion at bronze.** Each dim lands in **whatever format the endpoint returns** (CSV stays CSV, JSON stays JSON). Format normalization to parquet is a **SILVER** function, never bronze. *(Corrects the prior all-parquet-at-bronze proposal — that conversion belongs in silver.)*
2. **Bronze takes ALL FIELDS. No redaction, ever.** Bronze is raw + complete from each endpoint. Fact→dim selection, field choices, and slimming are SILVER decisions (Rule 17 governs silver). Bronze never drops a field.
3. **Bronze's only job = ingestion + consistent bucket structure.** The consistency we enforce at bronze is the **folder layout**, not the file format.
4. **Single execution layer = the EC2.** All pulls run unified on `inf-gold-layer-runner` EC2 (the same machine that will run silver+gold). No parallel cron-Lambda pull layer.
5. **Eclipse is kept and pulled in full daily**, raw, into a consistent bronze structure — downstream silver/gold use TBD (we decide later; we do not discard the data).
6. **The two source domains stay SEPARATE through bronze AND silver; they unify ONLY at gold.** Orion Connect (`api.cloud.orionadvisor.com`) and Eclipse (`www.orioneclipse.com`) are distinct products — different JWTs, different ID-spaces, and a deliberate naming false-friend (both expose a "portfolio" path that means different things: Orion `/api/v1/Portfolio/*` = custodial accounts+assets; Eclipse `/v1/portfolio/portfolios` = model-managed rebalancing portfolios). Keeping them in separate prefixes prevents the category error of treating them as one source. They are joined (account by `int()`-coercion, model by name; 96.6% reconcile, ~3.4% valuation-lag) only in the gold analytics layer.
   - **bronze:** `bronze/orion-api/` + `bronze/eclipse-api/`
   - **silver:** `silver/orion-api/` + `silver/eclipse-api/` (eclipse-api STUBBED/prospective for now — raw retained, no silver build required yet)
   - **gold:** unified analytics (the cross-domain join lives here, nowhere upstream)

## 1. Target bronze layout (structure is what we unify, not format)

```
 s3://opal-data-inf/bronze/orion-api/{YYYY-MM-DD}/        ← ONE folder for ALL Orion REST dims
   transactions.csv        tax_unrealized.csv   tax_realized.csv
   billing.csv             performance.csv      unified_account_dim.csv     (Envision ExcelReports → native CSV)
   representatives.json    household_rep_mapping.json     new_portfolio_accounts.json
   positions.json          assets.json                                       (v2 REST → native JSON, RAW — see §3)

 s3://opal-data-inf/bronze/eclipse-api/{YYYY-MM-DD}/      ← SEPARATE domain, consistent Eclipse raw landing
   portfolios_simple.json  portfolios.json   models.json   model_composition_{id}.json   [+ frontier — §4]
```
**Eliminated:** `bronze/orion-api-v2/` (merged into `bronze/orion-api/`), `bronze/positions/`, `bronze/assets/`, **`bronze/performance/`, `bronze/transactions/`** (all own-prefix parquet — the 4-dim inline-parquet double-write, §3), and the old `bronze/eclipse/` (renamed `bronze/eclipse-api/`). One datestamped folder per **source domain**; one file per endpoint in its native format; two domains never share a prefix (Principle 6).
> **Complete-prefix-census required (DS~A correction):** this list is illustrative, NOT exhaustive — the decommission/migration scope (R1–R3 / AC1) must be driven by a FULL `s3://opal-data-inf/bronze/` prefix census so no own-prefix tree silently survives. Request the exact census from DS~A and enumerate it in the PRD/TO.

## 2. Single pull layer on the EC2 — also a STRUCTURAL DURABLE FIX for the recurring freeze

**Promoted from cleanup to durable fix (source-confirmed, commit `9ea447b3a`, 2026-06-30):** the recurring inf nightly freeze is the gold chain's **REDUNDANT inline perf re-pull** (`pull_inflection_performance_rest.py`) HANGING (103/41min on the Orion perf endpoint, before positions/B_00, blocking B_00 under `set -e`). The deployed `timeout-tolerate` is the *tactical* fix (time-box the inline pull, fall back to cron-landed bronze). **This single-pull-layer is the STRUCTURAL fix:** collapsing to ONE timeout-guarded pull per dim on the EC2 removes the duplicate-pull hang class entirely — there is no redundant second pull left to hang the chain. (Carry the dispatch-level `timeout(-k30,600s)` onto the unified pull so the one pull can never block the chain.)

- The EC2 pulls **all** dims into bronze (today the inline chain pulls only 6; `tax`, `billing`, `unified_account_dim` are cron-Lambda-only — they move onto the EC2).
- **Decommission** the 9 standalone cron Lambdas + their EventBridge rules (retro §5).
- **One pull script per dim** — retire the duplicate implementations: transactions has **THREE** variants in `data/inf/manual_api/` (`pull_inflection_transactions.py`, `_rest.py`, `_v2.py`); performance has `performance_dim.py` vs `performance_rest.py`. Keep exactly one per dim.
- **Uniform resume/skip** [DECISION, rec: yes]: every dim skips re-pull if its `{date}` file already exists (idempotent re-runs); today only positions/assets have this guard.

## 3. The parquet-at-bronze + double-write correction — FOUR dims (DS~A validation 2026-06-30)

The parquet-at-bronze violators are **{positions, assets, performance, transactions}** — NOT just positions/assets. LIVE EVIDENCE (DS~A): `bronze/performance/2026-06-30.parquet` (3.2MB, 11:59Z) + `bronze/transactions/2026-06-30.parquet` (34MB, 12:13Z) — fresh PARQUET own-prefix (the **inline `_rest` path**) — coexisting with the cron-Envision CSVs at `bronze/orion-api/2026-06-30/{performance_dim,transactions}.csv`.
- So **perf + txn are DOUBLE-WRITTEN in two formats to two locations**: cron CSV (`orion-api/{date}/`) + inline parquet (`bronze/{dim}/{date}.parquet`). This is STRONGER than the "6-dim same-format double-pull" framing — it's **same-dim / different-format / different-location**. (And the inline `_rest` parquet path is the SAME redundant layer whose perf re-pull is the source-confirmed hang locus — §2.)
- positions/assets: `r.json()` → `to_parquet` → own prefix (`pull_inflection_{positions_daily,assets_v2}.py` L227/433, L228/401).
**Refactor (R2 covers all 4):**
- Bronze lands the **raw native** response (JSON) under the unified `bronze/orion-api/{date}/<dim>` — no parquet at bronze, for ANY of the 4.
- The →parquet conversion moves to silver (repoint the silver converters to read the raw bronze).
- Net: positions/assets/performance/transactions stop being format-special; the inline-parquet double-write is eliminated (it collapses into the single-pull-layer, §2).

## 4. The endpoint surface — ALREADY ENUMERATED (DATA_PLATFORM), pull it all

The enumeration is NOT an open task — comprehensive reverse-engineering work exists under DATA_PLATFORM. Authoritative sources of record:
- **`docs/architecture/INFLEC_API_ENDPOINTS_CATALOG.md`** — the Orion endpoint catalog (Envision/ExcelReports, Custom Reports, Portfolio/Accounts, Portfolio/Assets families).
- **`docs/architecture/DATA_PLATFORM_D3_orion_eclipse_arch_spec.md`** (v1.2, CTO-gated + CVO-reconciled) — the 3-surface span (S1 Orion REST dims, S2 per-day Assets snapshot, S3 Eclipse) with grounded endpoints, auth, and **§14 observed-but-unused frontier**.
- **`docs/architecture/ADVI_ORIAPI.md`** — the full Orion Connect HAR-captured contract (Appendix A/B).
- **DC1/DC2 crawler** (`run-orion-bfs-crawl.ts`, observe-only bounded-BFS) → self-catalogs to **`opal-crawl-catalog/eclipse/`** — the standing mechanism that EXPANDS the known surface.

**Rule-22 honesty (from D3 §1):** Orion/Eclipse publish **no developer API catalog** — the surface is reverse-engineered from the web UI's calls. So "pull all we can get" = the full **cataloged + crawled** surface, NOT a vendor-exhaustive list (unknowable). The DC1/DC2 crawler is how the frontier grows; the bronze refactor pulls everything currently cataloged AND ingests newly-crawled endpoints as they're confirmed.

**Orion (S1/S2) — pull the FULL cataloged surface, not just today's 9 dims.** Beyond the 9 production pulls, the catalog documents: `Portfolio/Assets` per-client/per-account snapshot (the `canonical_holdings` source, S2); `Trading/Models` + `Trading/Models/{id}` (139 models, ticker-level composition); `Reporting/Custom/{id}/Generate/csv` (per-transaction grain); plus aux (`Authorization/User`/`Privileges`, SignalR completion, the `Homepage/Action/DataSources` stored-proc back-door). The unified EC2 pull lands each cataloged endpoint raw + datestamped under `bronze/orion-api/{date}/`.

**Eclipse (S3) — structure is ALREADY the target; keep + expand.** `pull_eclipse_portfolios.py` already lands RAW JSON, datestamped, consistent: `bronze/eclipse-api/{date}/{portfolios_simple,portfolios_full,models,model_composition_{id}}.json` + `_meta/pull_complete.json` (4 artifact classes, 11 calls/run, 9 Opal model IDs `{3,5,6,7,8,9,10,28,29}`, on `inf-bronze-runner` EC2). It is the clean shape Orion-side bronze should match (just relocated to its own `eclipse-api/` domain prefix per Principle 6). Refactor = keep it, move it onto the unified EC2, and extend to the §14/crawler frontier. Pull everything reachable now; silver/gold use decided later. Downstream silver/gold for Eclipse stays TBD (we retain the raw data and decide later — Andrew-locked).
- **Durable risk to record (D3 §5.1):** the Eclipse JWT needs Andrew on the Eclipse firm roster (firmId 209900); if de-listed the pull goes dark (`422 No Firm Associated`). Record the Eclipse-admin contact — same fragility class as the OTP dependency (§7).

## 5. Retroactive / migration work

- **R1 — Decommission cron-Lambda pull layer:** disable + remove EventBridge rules `inf-api-reps`(30 12), `inf-accounts-v2-daily`(35 12), `inf-unified-account-dim-daily`(40 12), `inf-api-assets-v2-daily`(45 12), `inf-api-positions`(50 12), `inf-tax-daily`(55 12), `inf-api-txn`(0 13), `inf-billing-daily`(35 13), `inf-performance-daily`(40 13); retire the Lambda functions + their pull scripts (per Terraform `infra/aws/terraform/inf-pipeline/`). Move all pull logic onto the EC2 chain.
- **R2 — positions/assets de-convert:** stop the at-bronze parquet write; land raw JSON in the unified folder; update the silver positions_mv/assets converters to read the new raw JSON path. Validate the silver output is byte-equivalent to today's (parity gate).
- **R3 — Folder migration:** [DECISION] go-forward only (new layout from cutover date) + on-demand backfill, OR relocate existing `orion-api-v2/`, `positions/`, `assets/` history. Rec: **go-forward + on-demand backfill** — bronze history is already consumed into silver/gold, so a full relocate is low-value; keep old prefixes read-only until silver no longer references them.
- **R4 — Duplicate-script retirement:** pick one pull script per dim; delete the other; update the chain step registry.
- **R5 — Eclipse structure:** rename `bronze/eclipse/` → `bronze/eclipse-api/` (the format + `{date}/` foldering are ALREADY correct — live-verified 2026-06-30: all-JSON, datestamped partitions, one file per endpoint incl. `model_composition_{id}.json` ×9). Move the pull onto the unified EC2 + extend to the §14 frontier. No format/foldering change needed — Eclipse is already the clean target.

## 5b. Complete prefix census — AC1 authority (DS~A live census 2026-06-30)

Every `s3://opal-data-inf/bronze/` prefix classified — the decommission/migration scope; no tree may survive unclassified:

| bronze prefix | disposition |
|---|---|
| `orion-api/` | **KEEP/TARGET** — unified Orion bronze; all dims land here |
| `orion-api-v2/` | **ELIMINATE** → merge into `orion-api/` |
| `positions/` | **ELIMINATE** → raw JSON in `orion-api/` (own-prefix parquet) |
| `assets/` | **ELIMINATE** → raw JSON in `orion-api/` |
| `performance/` | **ELIMINATE** → de-convert (CSV copy already at `orion-api/{date}/performance_dim.csv`) |
| `transactions/` | **ELIMINATE** → de-convert (CSV copy already at `orion-api/{date}/transactions.csv`) |
| `eclipse/` | **RELOCATE** → `bronze/eclipse-api/` |
| `orion/` | **NON-DIM, KEEP** — auth state (`jwt/current.json`, `browser-profile/state.json`, `otp/`); exempt from the layout refactor but it is the SPEC-4 auth surface |
| `logs/` | **NON-DIM, KEEP** — runner logs |

## 6. Acceptance criteria (machine-checkable → PRD/TO)

- AC1: every Orion REST dim lands under `bronze/orion-api/{date}/` — `bronze/orion-api-v2/`, `bronze/positions/`, `bronze/assets/` receive no new writes.
- AC2: `positions.json` + `assets.json` at bronze are valid raw JSON (NOT parquet); a `.parquet` for these appears no earlier than silver.
- AC3: a bronze file exists for all dims for the run date, produced by the EC2 (no cron-Lambda invocation in the window); the 9 EventBridge cron rules are `DISABLED`/removed.
- AC4: **completeness** — each bronze dim carries the full field set the endpoint returns (schema-completeness assertion per dim; no field dropped at bronze).
- AC5: exactly one pull script per dim in the chain registry.
- AC6: every endpoint in the DATA_PLATFORM catalog (INFLEC_API_ENDPOINTS_CATALOG + D3 S1/S2/S3 + the crawler-confirmed frontier) lands raw daily — Orion under `bronze/orion-api/{date}/`, Eclipse under `bronze/eclipse-api/{date}/` (the two domains never share a prefix) — including the currently-unpulled S1 surface (Trading/Models, Custom Reports, per-client Assets snapshot).
- AC8: domain separation holds downstream — `silver/orion-api/` and `silver/eclipse-api/` are distinct trees (eclipse-api stubbed); NO cross-domain join exists before gold.
- AC7: silver outputs post-refactor are parity-equal to pre-refactor (the de-convert + repoint introduced no value change) — validated several days before cutover.

## 7. Noted for the FINAL refactor step (Andrew-flagged, NOT this layer)

**EC2 OTP fallback protocol.** The Orion JWT refresh depends on a human OTP relay (`inf-otp-relay`, `s3://opal-data-inf/otp/`). Once the unified EC2 flow is in place, assess a manual-OTP fallback solution modeled on the Black Diamond approach, so a JWT lapse has a defined recovery path. This is the LAST step of the overall refactor — recorded here, specced when we reach it.

## Compiler Tools
| Tool | Use | Result |
|---|---|---|
| grep/read inf-pipeline pull scripts (positions/assets r.json→to_parquet; eclipse endpoints) | the raw-bronze correction + Eclipse endpoint set | PASS (rail-checked) |
| live S3 + TF (bronze layout, EventBridge rules) | as-is grounding (see inflection-bronze audit) | PASS |

— 3.0.0_SA_CVO
