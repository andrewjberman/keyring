# OPAL_CONSOLIDATION — Runner-refactor A/B/C scoping (Andrew-direct, 2026-07-21)

**Recorded by:** 2.0.0_SA_COO~A (registry-hygiene lane; Andrew engaged this directly during the OPAL close-out review). **Read-only investigation — no egress run, no build, no spawn from this lane.**
**Purpose:** capture Andrew's directive verbatim, ground A/B against the actual PRDs, and hand a *precise investigation map* for the net-new item C to whoever CTO/MSTR assign.

## Provenance — Andrew verbatim (this session, 2026-07-21)
1. *"one of the most important parts of this entire OPAL_CONSOLIDATION, and is existential to its completion and success, is the refactoring of the runners to A.) Take on Canonical formatting in titling/permission structure/daily ops/etc. whereby they are drawing against the relevant silver layers in opal-data-assets and fitting into OPAL_TAXONOMY OPAL_STNDRD formatting and record-keeping. B.) Finalize the refactoring of the 49F gold-runner. C.) Assign an agent specifically to investigate all Cottonwood Black Diamond data and figure out where their 'Model Portfolio' data is being held, so that we can fold them into the opal-data-assets DDB layer for Model Portfolio holdings in value and count. C.) Has not been established in the PRD for any of the OPAL macro projects, but it is important and we need to figure it out."*
2. *"Yes look into the PRDs for OPAL_RUNNERS OPAL_49METADATA and so on as well"*
3. *"The only way I can think to do it for Cottonwood is maybe to establish a local bd_identity token (or simply take the one we have in the cloud and employ it in a local scrape/curl) with the intent of just testing the endpoints we're aware of and querying to see what fields might be holding the opal model data."*

---

## A — Canonical runner refactor (titling / permission / daily-ops → silver in opal-data-assets, TAXONOMY/STNDRD fit)
**Where it lives:** `docs/architecture/OPAL_RUNNERS_PRD.md` §1 (INGESTION CANONICALIZATION — ETL + daily ops) + `OPAL_CONSOLIDATION_PRD.md` §5 **WS-C** (RUNNERS build + platinum cutover, S3–S5). OPAL_RUNNERS is `complete-as-superseded → OPAL_CONSOLIDATION`; the WORK is WS-C.
**Grounded scope (PRD §1.1 channel-box pattern + Andrew's 3 rulings 07-14):** one ingest vehicle per vendor CHANNEL; canonicalization is of **CONTRACTS (the A/B/C/D group shape) only — script forks stay per-partner** (cot/bd script-separation rule holds); runners draw against canonical silver and write partner platinum; incremental-daily design (≤$100/mo EC2, rust/polars for the heavy tables). **STNDRD/TAXONOMY fit** = exactly the standards that just folded into OPAL_TAXONOMY (medallion/trigger/lambda/EC2 grammar + the DC-1..DC-14 lints) — the runners must land on those naming/permission/record-keeping contracts, gate-enforced-not-big-bang.
**State:** DESIGN ratified (A→D build plan @baba79230); Wave-2 pure cores authored (a00_dim_account / a01_dim_relationship / c04_recon_guard, 16/16 fixtures) but **NO live runs**; flips to full-resource only on CTO cert of (1) bronze-backfill/silver parity all channels + (2) the trigger-confirmation matrix. **This is Andrew's "existential" A — it is scoped but pre-live.**

## B — Finalize the 49F gold-runner refactor
**Where it lives:** OPAL_RUNNERS_PRD §2–§4 (49F as the **case study**, "49F first because it is the most damaged") + the 49METATABLES convergence (`OPAL_ASSETS_49METATABLES_PRD.md`, D1–D4) feeding CONSOLIDATION WS-B / RUNNERS sec-4.3.
**Grounded scope (Andrew verbatim, PRD §0):** 49F today is *"riddled with patches for bad data … a transaction-engine canonical-holdings concept which is completely nonsensical … reconciliation layer and injections and phantom exclusions … not scalable and brittle."* Refactor draws against the **0833 account only, NO Black-Diamond direct exposure**, uses Schwab clean data as the canonical exemplar, step-by-step per gold layer so Inflection + Cottonwood inherit the shape.
**State:** convergence gate D2/D3/D4 delivered; **D1 (the dim bridge) is the last open finding** — D1a Apply-B LIVE @v0.11.0, first scheduled pull verified, dim build the remaining leg. **B = finish D1 → refactored 49F gold runner is the exemplar the others clone.**

## C — Cottonwood Model-Portfolio discovery + opal-data-assets DDB fold-in  ★ NET-NEW, in NO PRD
**The gap (confirmed):** OPAL_RUNNERS_PRD line 22 is Andrew's own *"Cottonwood we still don't know where they mark their models"* — an acknowledged unknown that was **never turned into a workstream**. Cottonwood's entire live pipeline (`advi-cot` / `cot-pipeline`, Black-Diamond-native, `s3://opal-data-cot/`) serves **AdvisorIntelligence only** (AUA, cohorts, leaderboards, mix) — **it has NO Model-Portfolio holdings layer at all.** So the model-portfolio data (which account → which model; model holdings in value + count) is neither served nor ingested today.

**The investigation toolchain ALREADY EXISTS (Andrew's method is largely pre-built):**
- **Credential:** `bd_identity` = the `.bd.identity` cookie, stored per-firm in Secrets Manager `blackdiamond/cot/session` (+ `blackdiamond/cot/credentials`). Captured by `data/cot/scripts/bronze/cot_bd_session_fetch.py`. (Firm-separated — cot, NEVER the 49f secret.)
- **Probe tool:** `data/black_diamond/API/tools/bd_endpoint_sweep.py` — reads the session secret, mints a bearer via `/datamining/auth/token`, and sweeps endpoints. Invocation already cot-shaped: `BD_S3_BUCKET=opal-data-cot BD_SESSION_SECRET_ID=blackdiamond/cot/session BD_FIRM_ID=cottonwood`. **This IS "test the endpoints we know about and query which fields hold the model data."**
- **Documented surface:** `data/black_diamond/API/` (README, AUTHENTICATION, `domains/datamining/{DOMAIN,QUERY_TYPES}.md`) — DataMining query types qt1–6 incl. **`allocations`** (`allocationMarketValueFactId`, `parentQueryAllocationLevelId`, `childQueryAllocationLevelId`). **Models/sleeves in BD are allocation structures — `allocations` is the first place to look for "where Cottonwood marks their models."**
- **Fold-in target:** DDB **`opal-assets-daily-aua`** (`infra/aws/terraform/opal-assets/main.tf:52`, PK=run_date). Currently AUA-cohort-shaped (the mdpf/model_aua feed), NOT model-portfolio-holdings — so C must **add a model-holdings (value + count) representation** to the DDB model-portfolio layer (the same layer SmartX's 11 opal models feed via smartx-pipeline; Cottonwood's BD models fold in alongside).

**Grounded refinement on Andrew's method:** the cloud mechanism is designed to run *where the token already lives* — `bd_endpoint_sweep.py` reads `blackdiamond/cot/session` via boto3. **Prefer running the sweep cloud-side (cot-exporter EC2 / a scoped Lambda) over exfiltrating the cloud token to a local machine** — same result, no credential leaves Opal infra. A local run is supported (set the 3 env vars + SM read) if that's faster to iterate; Andrew's call.

**Guardrails (bind the assigned agent):**
- **Vendor egress:** BD is a vendor. The cot BD channel already pulls daily (authorized/operational), so this is additional *read-only* endpoint probing on a live channel — but confirm Andrew's per-use word covers the *sweep* specifically before the run (CLAUDE.md vendor-egress law).
- **Firm separation:** `blackdiamond/cot/session` + `opal-data-cot` ONLY — never the 49f secret/bucket (gate + IAM enforced; the sweep tool already requires explicit env, no 49f default).
- **Read-only + no ingest-time coercion:** the sweep queries; any landed bronze is raw (Rule 17a) — model-portfolio parse-down is gold's job.
- **Lane:** this is a build/ops + egress task under CTO gate + the dedicated agent Andrew asked for — NOT this audit lane.

**Recommended shape:** a new **CONSOLIDATION WS-E — "Cottonwood model-portfolio discovery + DDB fold-in"** (or a RUNNERS sub-phase): (1) run the cot endpoint sweep against allocations/model query-types → locate where models are marked (account→model map + model holdings); (2) design the model-holdings (value+count) DDB representation extending `opal-assets-daily-aua`; (3) build the cot bronze→silver→gold path that populates it; (4) wire the DDB fold-in. Step 1 is the discrete "assign an agent to investigate" deliverable Andrew named.

---

## Routing / recommendation
- **→ CTO (1.0.0_SA_CTO), OPAL_CONSOLIDATION owner:** fold A/B/C into the CONSOLIDATION/RUNNERS PRD. A/B are already WS-C/WS-B — record Andrew's "existential" emphasis + TAXONOMY/STNDRD-fit binding. **C is net-new → author WS-E (or a RUNNERS sub-phase) with this scoping.**
- **→ MSTR (0.0.0_AB_MSTR):** assign the dedicated Cottonwood-model investigation agent Andrew named; this brief is its starting map (toolchain exists → step-1 is a sweep + field analysis, not a build-from-zero).
- **→ base COO (2.0.0_SA_COO):** coordination; the egress-word confirmation + cloud-side-vs-local method call route back to Andrew.
- **Andrew confirms:** (i) per-use egress word for the cot sweep, (ii) cloud-side vs local token, (iii) go on WS-E authoring + agent assignment.
