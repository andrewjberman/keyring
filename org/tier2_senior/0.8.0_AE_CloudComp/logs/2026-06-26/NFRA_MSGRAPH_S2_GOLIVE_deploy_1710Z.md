# NFRA_MSGRAPH.S2 — MS doc-cloud ingest GO-LIVE (deploy session log)

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT (ALB rule + deploy-script + Dockerfile + task-def), VALIDATE (live smoke)
**Agent:** 0.8.0_AE_CloudComp (NFRA_GLOBGRPH owner per COO 165226Z) | **Date:** 2026-06-26 | **Window:** ~16:44–17:10Z
**Gates:** CTO deploy-go 164447Z + COO window/ownership 164439Z + 165226Z (ledger spans nightly by design)
**Ledger:** `org/critical_paths/change_management/20260626T1648Z_nfra-msgraph-s2-ms-ingest_deploy_completion.md` (L1-L5 CLOSED, L6 by-design-open)

## Outcome

NFRA_MSGRAPH.S2 MS doc-cloud ingest is **LIVE through deploy-activation**. The 02:00 UTC nightly is the first MS-enabled derive (no ad-hoc run — NEVER#4). Andrew's "no new registration" path + his read-only-at-server-layer refinement are both **live and proven on real data**.

## The 8-step deploy (executed steps 1-5; L6 = the scheduled nightly)

| Leg | What | Proof |
|---|---|---|
| L1 git | code+IaC committed+pushed | fb625d0f5/5fd78e01e/1a23a3ed4/cac16138a/+deploy commits |
| L2 secret | `opal/mcp/ms-ingest-token` minted out-of-band | ARN `...-mXFTKk`, value never in TF state/logs |
| L3 gateway TF | safe-apply: `/ms/health` 6h liveness probe + bearer grant | 6 add / 1 chg / 0 destroy — live gateway untouched |
| L4 gateway code | safe-ec2-deploy `i-07dccb1615503ac99` + ALB `/ms/*` OIDC-exempt rule | **GET /ms/health+bearer={ok:true}** (server-held token mints), no-bearer=401, /ms/sites=6 structure-only |
| L5 derive | task-def `:4` (GLOBGRPH_MS_ENABLED=1 + gateway URL + MS_INGEST_BEARER secret) + image rebuilt via CodeBuild + nightly target→:4 | describe-task-definition + ECR push + list-targets |
| L6 verify | the 02:00 nightly's artifacts → comp-kuzu `n.source='ms'` | **PENDING — by design, post-nightly ~tomorrow AM** |

## Two mid-deploy gaps found + fixed (grounding the mechanism, not assuming)

1. **ALB OIDC exemption** — `/otp/*` is ALB-exempted from `authenticate-oidc` so the headless box can reach it; the derive (machine, no OIDC) needs the same for `/ms/*`. Added `ms_ingest_capability` rule (priority 31, mirrors `otp_capability`). Without it the ALB would have blocked every derive call. Proven fixed by the live 200.
2. **deploy-to-ec2.sh + Dockerfile** — the gateway `.env` template didn't write `MS_INGEST_BEARER`/`MS_INGEST_IDENTITY` (→ 503 not_configured); the Dockerfile didn't COPY `ms_cloud_extract.py` (→ container ImportError). Both extended.

## Live de-risk (read-only — NOT an ad-hoc derive run, no Iceberg write)

`HttpMsGatewayCaller → build_ms_graph` against the LIVE gateway: **34 nodes / 39 edges**, node_types `MS_SITE`(6)/`MS_LIBRARY`(6)/`MS_FOLDER`(17)/`MS_DRIVE_ONEDRIVE`(1)/`MS_USER`(4), edges `CONTAINS`(23)+`OWNED_BY`(16), **SS4 cert PASS on live data**, all `layer=ms/source=ms`, exclusion policy fired, write-heat present. The derive→gateway→schema→cert path is proven end-to-end; the nightly only adds the Iceberg merge (offline 11/11).

## Safety shape carried through

Two fail-closed layers live: gateway `/ms/*` **read-only by construction** (`_read_get` GET-pin) + **structure-only** output allowlist (permission + data layer), AND the derive **SS4 emit cert** fails the derive closed on any leak. Additive-only: a gateway/MS failure is best-effort (AWS derive unaffected); MS-disabled is the byte-identical safe resting state. `/ms/health` 6h EventBridge→SNS probe guards a lapsed Andrew-refresh.

## Compiler Tools

| Tool | Result |
|---|---|
| `deploy_ledger.py open/close-leg` | ledger contract — opened 6-leg manifest, closed L1-L5 with proof, L6 by-design-open |
| `comp-kuzu n.source='ms'` | **DEFERRED to L6** — runs on the 02:00 nightly's artifacts (the TO mandate + AC#1); MS nodes not in the live graph until the nightly merges |
| native Grep / Bash (rail-checked) | TF resource/priority/codebuild-name lookups — `# rail-checked` markers logged (no comp-tool models TF plan-verbs / ALB rule priorities / codebuild project names) |
| native Read | gateway auth-layer source grounding (token_broker/server/otp) — Rule 22 mechanism grounding |

**comp-which gap (logged, S4):** still no m365-gateway route — that's the S4 findability deliverable.

## Next (L6 — the only remaining leg)

Post the 02:00 UTC nightly: content-verify its artifacts, run `comp-kuzu "MATCH (n) WHERE n.source='ms' RETURN labels(n), count(*)"` (MS first-class + AWS-count-unchanged superset), close the ledger, RAVC COO → unblocks the S3 heat-map cut. The ledger is by-design-open meanwhile (COO-flagged; not stranded).

Status: deploy activation COMPLETE; BLOCKED-BY-DESIGN on the 02:00 nightly for L6.
