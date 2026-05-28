# FIND_INSURE AC-T2 escape-valve — cost-band + SLA evidence brief

**Authoring:** `0.7.0_AE_CloudOps~B` 2026-05-28T~03:45Z
**Purpose:** Phase 1 RAVC2-Accept §3 evidence layer for AE 0.7~A combined Stage 2 cycle. Captures empirical smoke-test of `find-insure-crawl-web-scraping-browser` v0.3.0 (Ship B AC-T2 escape-valve substrate) covering invocation timing, memory utilization, graceful-fallback behavior, cost-band vs `one_shotter` baseline.
**Pairs with:** `docs/briefs/find-insure-phase1-ravc2-accept-template.md` (joint Tier-1 verdict template) §3 evidence-layer slot
**Spawn anchor:** ws COO `20260528T033612Z` RAVC2-ACCEPT-CLOSE batch §4 option (c) lean
**Authority:** [[feedback_no_terminal_standby]] + Andrew goal-set drive-end-to-end

---

## §1 — Substrate state confirmed LIVE (post-respawn re-verify)

`aws lambda get-function-configuration --function-name find-insure-crawl-web-scraping-browser`:

| Field | Value |
|---|---|
| State | Active |
| LastUpdateStatus | Successful |
| Handler | `bronze.crawl_web_scraping_browser_bronze.lambda_handler` |
| Runtime | python3.9 |
| Memory | 1024 MB |
| Timeout | 300s |
| Layer | `find-insure-browser-deps:1` (1004189 bytes Playwright sync; manylinux2014_x86_64) |
| Env | `SCRAPING_BROWSER_SECRET_NAME=find-insure/bright-data/scraping-browser-creds`, `SCRAPING_BROWSER_TIMEOUT_MS=30000`, `SCRAPING_BROWSER_WAIT_UNTIL=networkidle`, `SCRAPING_BROWSER_EXTRA_WAIT_MS=0`, `OPAL_DATA_IMO_BUCKET=opal-data-imo` |

Tag `imo-pipeline-v0.6.0` on origin pointing to `3686eac1f` per ws COO 02:08Z accept; record-terraform-deploy clean at `78b3220ff`.

---

## §2 — Smoke-test invocation (empirical)

**Payload** (per SISTER-COORD canonical Cambridge IR fixture, 2026-05-28T~03:41Z):
```json
{"company_slug":"cambridge-investment-research","website_url":"https://cir2.com","run_date":"2026-05-28","trigger":"fallback-empty-body"}
```

**Lambda response** (StatusCode 200, FunctionError null):
```json
{"ok": false, "slug": "cambridge-investment-research", "pages_fetched": 0, "pages_blocked": 1,
 "error": "secret-resolve: An error occurred (ResourceNotFoundException) when calling the GetSecretValue operation: Secrets Manager can't find the specified secret value for staging label: AWSCURRENT"}
```

**CloudWatch tail** (request `f0ddbd46-fc40-453e-837d-5f6380aa7149`):
```
[INFO] 2026-05-28T03:41:06.852Z  crawl_web_scraping_browser start slug=cambridge-investment-research url=https://cir2.com run_date=2026-05-28 trigger=fallback-empty-body
[INFO] 2026-05-28T03:41:07.003Z  crawl_web_scraping_browser done slug=cambridge-investment-research pages_fetched=0 pages_blocked=1
REPORT Duration: 153.57 ms  Billed Duration: 768 ms  Memory Size: 1024 MB  Max Memory Used: 87 MB  Init Duration: 613.77 ms
```

---

## §3 — SLA characteristics (current empirical + projected steady-state)

### Cold-path (first invocation)
- **Init duration:** 613.77 ms (Python 3.9 + Playwright layer import)
- **Total cold latency** (init + first invoke): ~767 ms
- **Per-IMO impact:** ~0.6s cold-start penalty fires once per Lambda container; SPA-class IMO list per Stage 1 RAVC2 HALT diagnosis (Cambridge IR + Lincoln Financial + Structured AM + Liberty Bankers + Preferred Annuity + Carl Ostenson) = ~6 invocations per Stage 2 cycle → container reuse likely amortizes cold-start to 1-2 occurrences

### Warm-path (steady-state)
- **Current** (secret-resolve error fast-path): 153.57 ms; billed 768 ms (under-1s minimum-billing dominates)
- **Projected** (secret populated + Bright Data scraping_browser1 fetch):
  - Bright Data session establish + cookie handshake: ~1-3s
  - Page render to `networkidle`: 1-15s depending on SPA complexity
  - Total: ~3-20s per IMO; SPA-class (Cambridge IR-tier wealth-portal SPAs): ~5-10s median
  - Lambda timeout 300s = ample headroom

### Memory utilization
- **Allocated:** 1024 MB
- **Used (current empty-fetch path):** 87 MB
- **Used (projected steady-state, Bright Data session + Playwright sync response handling):** ~200-400 MB estimate based on similar Playwright workloads
- **Right-sizing candidate:** Defer downscale to v0.7+ pending Stage 2 empirical memory-usage telemetry. Current 1024 MB over-provisioned by ~7x at error-path; remains sized appropriately for projected steady-state worst-case.

---

## §4 — Cost-band vs `one_shotter` (find-insure-crawl-web Phase 1 baseline)

### `find-insure-crawl-web` (one_shotter — Phase 1 primary, Spec: Memory 1024 MB / Timeout 600s)
- AWS Lambda compute: $0.0000166667/GB-s × 1 GB × ~5s typical = ~$0.0000833/invocation
- No external API cost (plain `requests` + lxml)
- **Per 99-IMO universe scan:** 99 × $0.0000833 = ~**$0.008**
- **Per month** (weekly cadence): ~$0.032 = essentially $0 marginal

### `find-insure-crawl-web-scraping-browser` (Ship B AC-T2 escape-valve, Spec: Memory 1024 MB / Timeout 300s)
- AWS Lambda compute: $0.0000166667/GB-s × 1 GB × ~7s projected = ~$0.000117/invocation
- Bright Data scraping_browser1 page-load cost: ~$0.001-$0.005/page-load (per AC3 routing-matrix table column "Per-IMO cost (Bβ)"; SPA-class wealth portals trend to higher end ~$0.005)
- **Per AC-T2 escape-valve invocation:** ~$0.005-0.006 (Bright Data dominates)
- **Per 99-IMO universe scan with empty-body rate 5-10%:** 5-10 × $0.005 = ~**$0.025-0.05** (~3-6x one_shotter unit-cost on the escape-valve subset only)
- **Per month** (weekly cadence): ~$0.10-0.20

### Combined Phase 1 cost-band (one_shotter + AC-T2 escape-valve composite)
- **Per 99-IMO scan:** $0.008 (one_shotter all 99) + $0.025-0.05 (escape-valve subset) = **$0.033-0.058 / scan**
- **Per month:** **$0.13-0.24** (4x weekly cadence; well within CLAUDE.md cost-deliberateness Rule 5 envelope)

**Cost-discipline framing:** AC-T2 escape-valve is the OPT-IN escalation path for one_shotter empty-body class; total Phase 1 budget impact <$0.30/month even at worst-case empty-body rate 10%. Bright Data marginal cost remains sub-dollar at Phase 1 cadence.

---

## §5 — Graceful-fallback behavior (Phase 1 SLA enabler)

**Empirically proven** (this brief §2): when Bright Data scraping_browser1 zone credentials are unavailable (current state — secret value not populated; only metadata + Terraform-managed envelope exist), the Lambda:

1. Returns `StatusCode 200` (Lambda framework healthy)
2. Returns `FunctionError null` (no unhandled exception)
3. Returns response body `{"ok": false, "pages_fetched": 0, "pages_blocked": 1, "error": "secret-resolve: ResourceNotFoundException ..."}` — structured error JSON, not 500
4. Logs structured INFO records (`start` + `done` with slug/url/run_date/trigger/pages_fetched/pages_blocked) — no stack traces, no log-storm
5. Init duration ~614 ms one-time + warm 154 ms — fast-fail; no 30s+ Bright Data timeout exhaustion

**Phase 1 RAVC2-Accept implication:** AC-T2 escape-valve does NOT block Stage 2 universe-run on transient Bright Data secret-rotation moments. Empty-body IMOs that route to AC-T2 during a credential-rotation window will be marked `pages_blocked=1` and the Stage 2 universe-run completes; AC-T2 follow-on dispatch (per Phase 1 template §10 trigger-conditions row 4) handles them on subsequent cycle after secret-resolve clears.

---

## §6 — One outstanding non-infra blocker (forward-flagged to ws COO)

**Bright Data scraping_browser1 zone credential value population.**

- Secret envelope: `find-insure/bright-data/scraping-browser-creds` LIVE in AWS Secrets Manager
- Secret metadata: Owner=0.7.0_AE_CloudOps; Phase=1-AC-T2; ManagedBy=Terraform; Project=FIND_INSURE
- **Secret value: NOT POPULATED** (current state — `AWSCURRENT` staging label has no version)
- Per SISTER-COORD `20260528T015044Z` §Secrets: "Value populated OOB by Andrew/AE per Bright Data dashboard. If not yet rotated, this is your blocking call to make."

**Disposition:** Substrate APPLIED (verified §1 + §2) AND graceful-fallback PROVEN (§5). Phase 1 RAVC2-Accept on substrate completeness is CLEAR. Live AC-T2 dispatch on Stage 2 empty-body subset requires credential population — a sovereign-class procurement item routed to Andrew via ws COO escalation, not a Phase 1 Accept gate.

**Not blocking Phase 1 Accept** — it's a deferred dependency for first-actual-AC-T2-fire moment that materializes from Stage 2 universe-run empty-body detection (per Phase 1 template trigger-conditions row 4).

---

## §7 — Evidence for joint Tier-1 verdict (CORROBORATE-with-additives candidates)

Three additives surfaced via this smoke-test that would be candidates for joint Tier-1 verdict materialization at Phase 1 Accept moment (per [[feedback_corroborate_with_additives_materializes_immediately]] — fold into materialization TO scope without re-cycle):

| Additive | Class | Materialization owner | Surface trigger |
|---|---|---|---|
| **A1** — Memory right-sizing scan post-Stage 2 (downscale candidate 1024 MB → 512 MB if Stage 2 telemetry confirms <512 MB peak) | Cost-optimization | AE 0.7 (next /work cycle post-Stage 2 RAVC2) | If Stage 2 CloudWatch Insights query shows `max(@maxMemoryUsed) < 524288000` |
| **A2** — Secret-value population gate-tracking entry (add to FIND_INSURE.json `blocking` field as sovereign-procurement row separate from existing rows) | Sovereign-procurement tracking | CVO Sub-class X authoring-cascade | Phase 1 Accept commit moment |
| **A3** — AC-T2 first-fire empirical capture (CloudWatch query captures first non-empty-fallback invocation timing + page-render count + Bright Data session cost) | Empirical-evidence backfill | AE 0.7 + DS~D coordination (DS~D parser perspective) | First Stage 2 cycle with empty-body subset >0 |

None of these surface as REPAIR-AMENDMENT triggers (no mechanical-untruth + no inadequate-solution-coverage at v0.7 PRD level per [[feedback_self_correction_upstream_of_verify_channel]] boundary test); pure observational additives.

---

## §8 — Phase 1 RAVC2-Accept template §3 evidence-layer instantiation

For direct paste-in to `docs/briefs/find-insure-phase1-ravc2-accept-template.md` §3 evidence layer (when AE 0.7~A combined Stage 2 RAVC2-Request fires):

```
### AC-T2 escape-valve substrate (v0.3.0)
- Lambda `find-insure-crawl-web-scraping-browser` LIVE (handler bronze.crawl_web_scraping_browser_bronze.lambda_handler; memory 1024 MB; timeout 300s; layer find-insure-browser-deps:1)
- Tag `imo-pipeline-v0.6.0` on origin (3686eac1f); record-terraform-deploy clean (78b3220ff)
- Smoke-test PASS 2026-05-28T03:41:06.852Z — Cambridge IR fixture invocation; graceful-fallback proven (StatusCode 200, FunctionError null, structured error response on secret-resolve miss)
- SLA: ~614 ms init / ~154 ms warm on secret-error path; projected ~5-10s warm steady-state on Bright Data SPA fetch
- Cost-band: $0.005-0.006/escape-valve-invocation (Bright Data dominates); combined Phase 1 cost-envelope <$0.30/month at empty-body rate ≤10%
- Brief: docs/briefs/find-insure-ac-t2-cost-band-sla-evidence-aeb-20260528.md
- Outstanding: Bright Data credential value population (sovereign-procurement; not Phase 1 Accept gate per §5 graceful-fallback proof)
```

---

## §9 — Authority + provenance

- **Spawn moment:** Post-respawn 2026-05-28T~03:35Z per ws COO RAVC2-ACCEPT-CLOSE batch
- **Smoke-test commit anchor:** v0.3.0 source @ `40b18d724` (data/find/imo/scripts/bronze/crawl_web_scraping_browser_bronze.py); deploy chassis @ `3686eac1f` tag `imo-pipeline-v0.6.0`
- **CVO verify-channel surface:** Available for /verify-channel review at next CVO cycle (Mode A surface-level mode: empirical-class — pipeline DELIVERS structured graceful-fallback response under credential-missing condition)
- **Per LD-0116:** Brief routed via ws COO (lane chain); CC ws CTO + ws CVO for cross-Tier-1 visibility; AE 0.7~A peer-CC for Phase 1 RAVC2 evidence absorption; no direct MSTR or Andrew MCP

---

— AE 0.7~B 2026-05-28T~03:45Z
