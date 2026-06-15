# CVO Deliverable — Opal Estate-Thread Inventory + comp-pipescript/graph coverage (2026-06-15)

**archetype:** VALIDATE
**secondary_archetypes:** EXPLORE, COORDINATE
**Trigger:** Andrew-direct ("establish every single thread — analytics enrichment,
backend AWS that resolves on the frontend — and make sure comp-pipescript traverses
them"). **Method:** orchestrated multi-agent census (Andrew opt-in), ground-truthed
against live AWS (Lambda/EC2/SQS/StepFn/DDB/API-GW) + repo + portal/src; F5 discipline.
Two passes: `wk26i786c` (11 families) + gap-closure `w7vgvpbwr` (2 missed families).
**Full per-thread data:** `logs/2026-06-15/estate_census/pass1_inventory.json` (113
threads, 118 manifest rows) + `pass2_gapfamilies.json` (21 threads).

## Headline

The estate is **13 thread-families / ~134 threads** spanning ~169 live Lambdas +
18 EC2 + Step Functions + DDB. **comp-pipescript models only ~13 of them** (the
medallion gold/silver/bronze DAGs). "Full coverage" is therefore NOT a
comp-pipescript extension — it is the **coverage-manifest + determination-guard**
CTO ruled (one source-of-truth all subcommands read; "Unknown" can never read as
"clean"), populated by this inventory, with each thread pointed at the RIGHT tool.

## The accounting result (the "no thread silently unknown" bar)

- **166 / 169 live Lambdas mapped** to a thread across both passes.
- **3 residual, ALL documented** (none silently unknown): `test-yfinance-simple` +
  `yfinance-aapl-test` (test/diagnostic -> EXPLICITLY_OUT, teardown candidates);
  `sentiment_query_api` (nodejs18, LastMod 2025-12-23 -> UNREVIEWED, needs an owner
  to confirm trigger+consumer).
- **EC2 (18):** all covered except `bd-exporter` (instance_id=null in manifest —
  verify live; likely a bd silver leg) and `m365-mcp-gateway` (unprovisioned, OUT).
- **The completeness gate earned its keep:** pass-1's total-accounting caught **two
  entire IN_SCOPE product families that the seed list missed** — the
  **trade-submission** product (7 lambdas, DDB `opal-trade-submissions`, mounted
  `/trade-submission` portal page, `/api/general/trades/*`) and the
  **YangDataPipeline** (Step Functions `YangDataPipeline`, ~20 `yang-*` lambdas ->
  `opal-data-portal-v2` json -> ModelPortfolios.tsx/FactorTilts.tsx). Both were
  100% unmodeled; without the gate they'd have stayed silently absent.

## Classification (combined, from the manifest population)

~96 IN_SCOPE / ~21 EXPLICITLY_OUT / ~10 UNREVIEWED across the 13 families.
(Per-thread rows in the JSON artifacts; the manifest population is the coverage-
manifest seed.)

## Tool-boundary (the architectural finding — for CTO)

By suggested_tool across the population:

| Layer / tool | ~threads | What belongs here |
|---|---|---|
| **comp-pipescript** (medallion DAG) | **~13** | bd/inf gold/silver/bronze ONLY |
| **globgrph-graph** (comp-kuzu, AWS-resource) | ~21 | lambda/EC2/StepFn dependency threads |
| **stitch** (cross-layer end-to-end) | ~9 | full producer->served->frontend chains |
| **portal-consumer-tools** (comp-routes/platinum/transform) | ~46 | frontend resolution (the bulk) |
| **none** (ops/local/test) | ~28 | monitoring, anomaly, teardown, local |

So comp-pipescript is correctly a **medallion specialist**; the estate's center of
gravity is the graph + stitch + portal-consumer tools. Recommend the manifest record
the tool per thread; comp-pipescript's mandate stays medallion, and its
false-clean-guard generalization (CTO G3) makes any non-medallion query return
"OUT-OF-SCOPE -> see {tool}" rather than a silent Unknown.

## Families (13) — one line each

bd-medallion (20) · inf-medallion (12) · cot+mdpf (2) · smartx (3) · causality-AI (8)
· market-analytics (9) · news+seeking-alpha (12) · pm-tool (12) ·
fred+generated-outputs (9) · partners+portal-infra (13) · graph+ops+casefind (13) ·
**trade-submission (7, NEW)** · **yang-datapipeline (14, NEW)**.

## UNREVIEWED — owner must confirm before classifying clean (do-not-guess)

All 5 causality interactive handlers (consumer page unmounted), `inf-client-detail`
(STUB), `bd-time-machine` (restore never implemented), FRED-02 macro json + FRED-07
deck-generation (no portal consumer), `sentiment_query_api`, `ycharts-session-*`,
trade TS parquet-export (no FRONTEND consumer — pipeline-tier artifact; IN under
"pipeline-consumer", OUT under strict "frontend-only").

## Debtscan-relevant flags (route to NFRA_DEBTSCAN owner)

Orphan/dormant/stranded/no-consumer: `bd-gold-layer` (orphaned legacy),
`bd-time-machine`+`portal-time-machine` (scaffolding-live, restore unbuilt),
`yang-generate-volatility` (frozen 2026-01-14, superseded), `ycharts-*` (dormant),
`semantic-pipeline` (no trigger ~4mo), `schwab-anonymizer` (0 invokes + non-ASCII
emoji in source = CLAUDE.md violation), `deck-generation` (manual Function URL only),
`test-yfinance-*`/`yfinance-aapl-test`, `opal-pm-snapshot-handler` (FE coded, API-GW
routes NOT registered), `smartx-model-monthly-pull` (DISABLED scheduler — confirm
intentional vs stranded). **Freshness:** FRED exec_summary.json (2026-05-04 stale),
smartx by_period/by_assetclass/timeseries views (Feb-2026 stale; live path now REST/DDB).

## Seams/overlaps (reconciled — right owner)

cot-bd-session-trigger -> cot+mdpf (firm-separated). historical-prices-scheduler ->
bd-medallion. opal-pm-snapshot-handler / opal-portfolio-funds-list -> pm-tool.
causality-market-update-generator -> causality-AI (reconcile to its UNREVIEWED, not
MA-07 IN_SCOPE — avoids inflated count). opal-portal-data-proxy -> partners-portal-infra.
The FRED family claimed a SUBSET of yang-* lambdas — the FULL YangDataPipeline DAG
should have ONE owner (yang family / stitch surface), not split FRED/yang.

## Recommendations (per driver)

- **CTO (P1):** (a) ratify the tool-boundary table above; (b) finalize the coverage-
  manifest schema (`org/modules/graph/comp-pipescript-coverage.yaml`) + the
  generalized false-clean guard (io+deployed), seeded with this 134-thread
  population; (c) rule the trade-TS-parquet-export and the FRED/yang split.
- **COO (P1):** decompose ONCE against this population (you're holding for it):
  register IN_SCOPE threads to their tool, author the manifest, + fold G1 (mdpf
  postdeps) / G2 (flag alias). The two NEW families (trade-submission, yang) are
  real deployed products — give each a registration TO.
- **AE:** verify `bd-exporter` (instance_id=null) live; the 2 test lambdas +
  `sentiment_query_api` need a keep/teardown call.
- **CVO (me):** verify each manifest determination + that the guard fires LOUD on an
  OUT/UNREVIEWED tree (exit 2, right label, never silent-clean).

## What you should have asked but did not

Whether the estate's frontend-resolution layer is itself auditable the way the
medallion pipelines are. ~46 threads resolve to the portal via scoped APIs / the
data-proxy / gold artifacts, but that producer->frontend edge lives across
comp-routes/comp-platinum/comp-transform + the (currently ESM-paused, 16:41Z-vintage)
globgrph graph — there is no single "does this backend thread actually reach a
MOUNTED, rendering portal component?" check. Several threads here are
backend-live-but-frontend-unconfirmed (causality handlers, pm-snapshot, bd-time-machine,
deck-generation). The highest-leverage follow-on after the manifest is a
**frontend-reachability gate** (thread -> served artifact -> mounted component that
reads it), so "IN_SCOPE" means "verified rendering," not "a lambda exists + a route
is declared." That is the frontend analogue of the absence-monitoring gap I found on
the graph platform this morning — the estate alerts/audits on presence, not on
whether the thread actually lands somewhere a user sees.

— 3.0.0_SA_CVO, 2026-06-15 estate-thread census (orchestrated, Andrew opt-in)
