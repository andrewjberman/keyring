# 1.0.0_SA_CTO — Session 12: ADVI_INFETL PRD v0.1 — Daily ETL + Gold/Platinum Separation

**Date:** 2026-05-07 (continuation from session 11 dashboard refresh; post-/compact resume)
**Frame:** Andrew direct (post DS~A NMNC/NNA Joe Brandenburg discovery): "make sure that all pipelines are running daily, that our gold runner is running daily, and that we have proper separation between gold and platinum. ONLY PLATINUM OUTPUTS ARE FED TO PORTAL, PERIOD." New project ADVI_INFETL authored + RAVC1 to COO for immediate decomposition + multi-agent execution.

---

## Triggering incident

DS~A relayed earlier-AM Joe Brandenburg attribution discovery: Orion retroactively re-attributed Joe's accounts from rep_id=3 (IWM) → rep_id=6 within last few days. Bronze pull script `pull_inflection_transactions_v2.py` line 71 hardcodes `@RepIDs="3,11,12"` (excludes 6). silver/transactions + canonical_nna therefore carry stale IWM-aggregated data. Portal NMNC/NNA inconsistency ($19.7M NMNC vs -$1.36M NNA) is the surface symptom. Andrew framing: "I think what happened is that we are not actually running our full process end to end every single day."

**Five same-class incidents in 14 days:**
1. AUDIT-002 — canonical_prices stale 199.6h (2026-04-22 → ADHC_COMPIL.013 freshness gate)
2. AUDIT-008 — silver/assets_v2 stale 5d (2026-05-05 → ADVI_INFINGE Phase 1 TO-1 + AUDIT-008.PERM)
3. AUDIT-008 INF_B_00 blocker — silver/api_dims/positions_mv stale 5d (2026-05-05 → ADVI_RPBKTPI)
4. AUDIT-003 — joe_brunswick → joe_brandenburg attribution typo + INF_D_04 allowlist (2026-05-05/06)
5. INFNNA NMNC/NNA discovery (2026-05-07) — root cause identified by DS~A as **the structural class** itself

INFINGE addressed bronze tier specifically. INFETL extends the daily-runtime guarantee to gold + publish tiers AND enforces the gold/platinum separation architectural constraint Andrew locked.

---

## DS~A 5-gap MCP analysis (received 20260507T~early-AM)

DS~A surveyed BD (49F) daily ETL vs Inflection daily ETL. Identified 5 critical gaps:

1. **GAP 1 — Gold chain has NO scheduled trigger** (CRITICAL). `inf-gold-trigger` Lambda exists; no EventBridge cron. Manual SSM only.
2. **GAP 2 — No portal publisher trigger from gold completion** (HIGH). `inf-portal-publisher` defined; no S3 trigger.
3. **GAP 3 — Transactions rolling 7-day window** (CRITICAL — separately addressed by INFNNA.001 in flight DS~A).
4. **GAP 4 — No daily price refresh independent of gold chain** (HIGH).
5. **GAP 5 — No Time Machine / version capture** (MEDIUM).

Plus weekly parity check (LOW).

---

## CTO read-side audit — additional finding

CTO read the four critical Terraform + dispatch files in parallel:
- `infra/aws/terraform/inf-pipeline/eventbridge.tf` — CONFIRMED only 3 rules (jwt-fetch 12:13Z, bronze-runner 12:43Z, export-schedule 21:00Z); no gold cron.
- `infra/aws/terraform/inf-pipeline/s3-notifications.tf` — CONFIRMED only `eventbridge=true`; no Lambda function blocks.
- `infra/aws/lambda/inf-portal-publisher/lambda_function.py` — CONFIRMED 25 lines returning `{"status":"stub","statusCode":200}`; "DS populates publisher logic in W4.6" comment.
- `data/orion/scripts/gold/orion-gold-dispatch.sh` — **NEW finding beyond DS~A list**: chain has NO sentinel write at success. Even with cron + S3 rule wired, publisher could never fire. Structural prerequisite.

`aws_lambda_permission.s3_inf_portal_publisher` ALREADY EXISTS in `lambdas.tf:212-218` (statement_id `S3PipelineCompleteTrigger`) — Phase 1 work is ONLY the bucket-notification rule, not the Lambda permission. Saves a Terraform resource.

S3 layout reality (`aws s3 ls s3://opal-data-inf/{gold,platinum}/`):
- gold/ has 12 sub-prefixes (account_gains/, artifacts/, canonical/, classification/, dimensions/, holdings/, logs/, lots/, manifests/, positions_cube/, timeseries/, views/) — populated.
- platinum/ has {advisors/, clients/, firm/} — populated. Some `--upload`-flagged scripts in orion-gold-dispatch.sh CATALOG must be writing platinum directly today (not mediated by a publisher). Phase 0 audit enumerates which scripts write to which prefix.

BD reference confirmed: `bd-canonical-prices-daily` 04:00 UTC + `bd-gold-nightly-fallback` 23:00 UTC + `silver/prices/20*.parquet` ObjectCreated → `bd-gold-trigger` + `gold/pipeline-complete.json` ObjectCreated → `bd-portal-publisher` (fans out async to `bd-portal-advisor-publisher` start + `bd-capture-output-versions` end).

BD writes portal artifacts to `gold/artifacts/*.json` (NOT `platinum/`). INFETL adopts `platinum/` for INF only per Andrew's directive; BD harmonization is OUT OF SCOPE.

---

## Documents produced

- **`docs/architecture/ADVI_INFETL.md`** — PRD v0.1, ~600 lines. §1 Scope. §2 Existing State (with confirmed gaps + S3 layout + BD reference). §3 Architecture (extends INFINGE 5-tier to Tier 4 gold cron + Tier 5 publisher chain + Tier 5c Time Machine + Tier 6 portal-route platinum-only contract). §4 Component Specs (4.1 inf-canonical-prices-daily cron, 4.2 inf-gold-nightly-fallback, 4.3 sentinel write, 4.4 S3 ObjectCreated rule, 4.5 publisher impl, 4.6 advisor-publisher impl, 4.7 capture-output-versions Lambda, 4.8 portal-route migration, 4.9 weekly parity, 4.10 standalone prices conditional). §5 Compiler Evidence skeleton + minimum-viable evidence table sourced from CTO read-side audit + DS~A analysis. §6 9 TO candidates phased. §7 8 OQs. Appendices B (4 design alternatives rejected), C (9-row risk register), D (cross-domain coordination).
- **`org/projects/ADVI_INFETL.json`** — full project metadata; phase narrative; depends_on=[ADVI_INFINGE]; pods=[0.4, 0.7]; coo_lane=2.0.0_SA_COO.
- **`org/projects/REGISTRY.md`** — new active row inserted between INFINGE and RPBKTPI.
- **`org/tier1_exec/1.0.0_SA_CTO/prompt.md`** — dashboard active row added.
- **`org/tier1_exec/2.0.0_SA_COO/prompt.md`** — dashboard active row added; flagged "IMMEDIATE: TO decomposition + assignment + sequencing" in Pending Work column.
- **MCP send_message** to `2.0.0_SA_COO` — RAVC1 with full TO breakdown + bandwidth-conflict warning + Andrew-input OQs + status request.

---

## 9 TOs sized for parallel execution

**Phase 1 (UNBLOCKS DAILY E2E — 5 TOs):**
| TO | Receiver | Effort | Gates |
|----|----------|--------|-------|
| TO-1 EventBridge cron + nightly fallback (Terraform) | `0.7.0_AE_CloudOps` | ~0.25d | Independent |
| TO-2 orion-gold-dispatch.sh sentinel write | `0.4.0_DS_ClientPlatform~A` | ~0.25d | Independent |
| TO-3 inf-portal-publisher Lambda implementation | `0.4.0_DS_ClientPlatform~A` (CTO recommends DS~B) | ~1.5d | Largest TO; mirrors bd-portal-publisher |
| TO-4 inf-portal-advisor-publisher Lambda implementation | `0.4.0_DS_ClientPlatform~A` (CTO recommends DS~B) | ~0.75d | Per-advisor drill-down |
| TO-5 S3 ObjectCreated rule wiring sentinel → publisher | `0.7.0_AE_CloudOps` | ~0.25d | Gates on TO-2 + TO-3 |

**Phase 2 (Time Machine + portal route migration — 3 TOs):**
| TO | Receiver | Effort |
|----|----------|--------|
| TO-6 inf-capture-output-versions Lambda port from BD/Yang | `0.7.0_AE_CloudOps` | ~0.5d |
| TO-7 portal-route audit (gold vs platinum read matrix) | RD or DT (COO assigns) | ~0.5d (can ship pre-Phase-1) |
| TO-8 gold→platinum read-path migration | DS+RD multi-tranche | ~5-8d cumulative across 3-5 tranches |

**Phase 3 (ops hardening — 2 TOs):**
| TO | Receiver | Effort |
|----|----------|--------|
| TO-9 weekly parity EventBridge rule | `0.7.0_AE_CloudOps` | ~0.25d |
| TO-10 standalone INF historical prices cron (CONDITIONAL) | `0.4.0_DS_ClientPlatform~A` | ~0.25d Phase 0; ~0.75d if needed |

Total cumulative effort: ~12-15 effort-days across pods.

---

## Gold/platinum separation contract LOCKED

- `gold/` is a strict internal staging tier. Publisher Lambdas read from `gold/`. Portal API GW Lambdas + Lambda@Edge MUST NOT read from `gold/`.
- `platinum/` is the read-only contract surface for the portal. Publishers write `platinum/firm/`, `platinum/advisors/`, `platinum/clients/`. Portal endpoints read from these and only these.
- BD currently writes `gold/artifacts/*.json` for portal — does not honor this contract today. Harmonization OUT OF SCOPE for INFETL.

---

## Critical bandwidth conflict — DS~A overload

DS~A is named on TO-2 + TO-3 + TO-4 (Phase 1) AND is concurrently in flight on:
- INFNNA.001 transactions backfill (Joe Brandenburg / IWM rep_id correction; in flight today).
- INFLFE.006-data (_build_aua_view + _build_geo_view rep-coverage gate; pending HIGH).

CTO recommendation to COO in RAVC1: split TO-3 / TO-4 to DS~B / DS~C / DS~D — publisher logic is data-shaping, comparable to canonical_nna logic DS~B owns. COO calls.

---

## Cron-flip coordination note

TO-1 EventBridge cron should land DISABLED initially → flip ENABLED only AFTER INFNNA.001 backfill is ACK'd, otherwise the first cron run fires against partial backfill state and produces inconsistent platinum outputs. CTO can author the flip-ack TO post backfill if useful (relayed to COO in RAVC1).

---

## Carry-overs to next session

| Item | Owner | Status |
|------|-------|--------|
| COO decomposition + TO assignment + sequencing for ADVI_INFETL Phase 1 | COO | Pending RAVC1 ack |
| OQ1 + OQ8 from PRD §7 (cron timing + BD harmonization scope) | Andrew via CTO/COO | Pending |
| INFREL.001b cron empirical 2026-05-07 12:30Z (closes performance-silver consumer WARN paths) | DS~B + AE 0.6.1 | Awaiting empirical (carry from session 11) |
| INFREL.002 cron empirical 2026-05-07 12:43Z (clean fire, no missed start) | AE 0.7 | Awaiting empirical (carry from session 11) |
| ADVI_INFINGE Phase 1 TO-1 ASSETS_V2 first cron fire 2026-05-07 12:30Z (closes AUDIT-008) | AE 0.6.1 | Awaiting empirical (carry from session 11) |
| INFLFE.006-data DS~A surgical fix | DS~A | Pending HIGH (bandwidth conflict with INFETL TO-3/4) |
| ADVI_RPBKTPI TO-2 historical chain re-run authoring | CTO | Backlog |
| AGENT_CONTEXT_POISONING_RECOVERY.md playbook authoring | CTO | Backlog |
| INFINGE Risk Register C downgrade (vendor-rate-suspension MEDIUM → LOW) | CTO | Backlog (non-blocking) |
| ADVI_INFETL v0.2 ratchet (post Phase 0 portal-route audit + TO-1/2/3 ship; populate §5 with comp-iam / comp-pipescript io / comp-routes empirical) | CTO | Phase 1 ship-side |

— 1.0.0_SA_CTO 2026-05-07T~16:10Z
