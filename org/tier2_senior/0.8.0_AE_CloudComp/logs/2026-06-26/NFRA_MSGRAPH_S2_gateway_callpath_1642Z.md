# NFRA_MSGRAPH.S2 — gateway call-path + read-only scoping + deploy prep (session log)

**archetype:** IMPLEMENT
**secondary_archetypes:** TRACE (gateway auth grounding), DEPLOY (TF + plan)
**Agent:** 0.8.0_AE_CloudComp | **Date:** 2026-06-26 | **Window:** ~16:07–16:42Z
**TO:** NFRA_MSGRAPH.S2 | **Gates cleared this window:** CTO S2 arch-gate PASS (162714Z) + Andrew sovereign auth ruling + Andrew read-only refinement (163709Z)

## What happened

Closed the S2 live-ingestion path end-to-end after the CTO S2 arch-gate PASS:

1. **Headless-auth grounded (Andrew's ruling, Rule 22):** read the gateway source — the `/otp/fetch` static-capability-bearer pattern (CTO-arch-GO'd) + `token_broker.get_token` (server-held, auto-refreshing delegated token) is exactly Andrew's "no new registration." The derive curls the gateway; the gateway holds Andrew's token. (`8fa70a76c` call-path doc.)
2. **Gateway `/ms/*` endpoint** (`5fd78e01e`): 4 read GETs (`ms_sites`/`ms_site_children`/`ms_onedrive_children`/`ms_search`) + `/ms/health`, static-capability-bearer gated, server-held `get_token(andrew)`, **output-allowlist** structure-only passthrough (drops content/comms, preserves Graph key names). Wired the production `HttpMsGatewayCaller`.
3. **CTO 3 rulings folded:** 4 thin per-tool GETs (gateway stays dumb), all READ/structure-only, server-side allowlist fail-closed.
4. **`/ms/health` liveness rider** (`1a23a3ed4`): mirror of the OTP probe — 6h EventBridge → SNS on `needs_login`; `MS_INGEST_BEARER` secret grant. TF authored, **not applied**.
5. **Andrew read-only refinement (163709Z)** (`cac16138a`): `_read_get` is the ONLY Graph-calling path on `/ms/*`, hard-pins `GET` → destructive is **impossible at the permission layer**, not just structure-asserted. Defense-in-depth with the SS4 emit cert. Read-only-token 3rd layer flagged to CTO (needs `Files.Read.All` consent; not required).
6. **Deploy plan** (`fd4894fe4`): 8 ordered steps, rollback-noted, MS-disabled = safe resting state. Held for the globgrph window + the CTO deploy-go.

## State

Full S2 code + IaC built, committed, proven offline (11/11 regression). MS-disabled (`GLOBGRPH_MS_ENABLED=0`) — nothing applied/deployed. **Blocked on two coordination gates** (RAVC'd): the NFRA_GLOBGRPH **deploy window + owner** (COO) and the **CTO deploy-go** (+ the read-only-scope-token ruling).

## Compiler Tools

| `<run>` | Result |
|---|---|
| `comp-to NFRA_MSGRAPH.S2` | OK — TO context. |
| `comp-blast commit_to_iceberg` / `run_full_derive` | NOT-FOUND (internal derive fns, not graph nodes — COO pre-flagged); real blast = the `graph_nodes`/`graph_edges` tables, kept byte-identical → consumers unaffected. Grounded by reading code. |
| `comp-kuzu "...n.source='ms'..."` | DEFERRED — post-deploy AC; MS not yet in the live graph (deploy-gated). Will run at step 7 of the deploy plan. |

No new comp-tool gaps. Source-grounding this window was native `Read` of the gateway app (auth layer) — the correct tool for a mechanism/why claim (Rule 22), not a comp-tool surface.

## Next

On the globgrph window + CTO deploy-go: execute the 8-step deploy (ledger-tracked, finished-in-session) → `comp-kuzu` live confirm → RAVC COO (unblocks S3). Status: BLOCKED-pending-globgrph-window + CTO-deploy-go (everything build/IaC done + reversible).
