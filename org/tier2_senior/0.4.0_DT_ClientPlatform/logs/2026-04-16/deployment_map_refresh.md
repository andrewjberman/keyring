# Session Log -- 2026-04-16 -- deployment_map refresh (v3)

| Field | Value |
|-------|-------|
| Agent | 0.4.0_DT_ClientPlatform |
| Date | 2026-04-16 |
| TO | `1.0.0_SA_CTO-2026-03-02-deployment-map-client-platform` |
| Deliverable | `org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/deployment_map.xml` |

## Objective

Refresh the ClientPlatform pod deployment_map.xml to match the current pipeline state and
satisfy the full schema required by the CTO TO. Existing v2 file (last updated 2026-04-06)
covered Terraform modules + Lambda authority but was stale on tag versions and missing 8
required schema sections.

## Work Completed

- Read DS data_contract.xml (2026-03-04 + 2026-04-15 addenda) and DE pod_inventory.xml
  (2026-03-19) for the page-centric organizer.
- Independently verified portal endpoints by reading
  `portal/src/api/endpoints/advisor-intelligence.ts` (859 lines, current) and
  `portal/src/api/endpoints/aum.ts`. Found ~22 platinum-tier endpoints not yet in DS/DE
  deliverables -- catalogued in deployment_map under pages_served.
- Cataloged Lambda inventory across yang-pipeline (3 portal-facing of 26),
  bd-pipeline (19 functions including 6 ingestion triggers + Time Machine pair),
  partners-api (1), portal-auth (2 region + 5 Lambda@Edge).
- Cataloged 9 EC2 services (smartx-exporter + 7 BD instances + ephemeral
  historical-prices-fetcher) with instance IDs, instance types, and AE-coordinate flags.
- Documented 6 S3 notification triggers across opal-data-bd (3, bd-pipeline-owned)
  and opal-data-portal-v2 (3, portal-notifications-owned).
- Documented 11 EventBridge schedules including the 4 NEW MON-FRI ingestion windows
  (unrealized 21:38 / realized 21:45 / asset_dim 22:10 / fees 22:15) and the moved
  bd-canonical-prices-daily 04:00 UTC slot.
- Wrote separate Yang vs BD vs partners-api vs portal-auth deployment sequences.
- Documented 12 known gotchas including bd-gold-layer-runner EVENTBRIDGE-ONLY policy,
  publisher Lambda-to-Lambda fan-out vs S3 prefix collision, opal-portal-data-proxy
  ownership boundary, ML-Edge ignore_changes nuances, Yang tag version skip, bd_allocations
  shared-EC2 race, ModelPortfolios DEMO mode + 401 redirect disabled, shared-advisor-router
  v9 M1 PII gate, and Windows build-and-upload.sh TMPDIR pitfall.
- Flipped TO `<status>` to complete with completion note describing the rewrite scope.

## Decisions Made

- **Schema fidelity over brevity.** The v2 file was operational but did not satisfy CTO
  acceptance criteria id=2 (8 required sections) or id=3 (pipeline_split clarity). The
  refresh restores schema compliance even where it makes the file longer.
- **Recorded `<authority>` on every Lambda entry** (`full` / `coordinate`) so future
  diagnostic reads land on the right owner without parsing prose.
- **Marked opal-portal-data-proxy as `coordinate` in market-overview group**, not in any
  ClientPlatform-owned module, with a high-severity gotcha. This is the AUM data path for
  ModelPortfolios but lives outside our authority -- worth being explicit.
- **Did not modify any source code or Terraform state** per TO constraints. Read-only +
  document-only.

## Files Modified

- `org/tier2_senior/0.4.0_DT_ClientPlatform/deliverables/deployment_map.xml` (full v3 rewrite)
- `org/tier2_senior/0.4.0_DT_ClientPlatform/task_orders/deployment_map.md` (status: pending -> complete + completion note)
- `org/tier2_senior/0.4.0_DT_ClientPlatform/logs/2026-04-16/deployment_map_refresh.md` (this file)

## Compiler Tools

| Tool | Run | Result | Notes |
|------|-----|--------|-------|
| (none) | n/a | n/a | This TO is a documentation refresh, not a code/infra change. No comp-* tool from the DT minimum table applies (`comp-pipescript io` is for gold-script edits; `comp-iam service` is for new boto3 calls). I cross-checked Lambda counts against `lambda-source-map.json` directly via Grep, which is the authoritative source the comp-* tools also derive from. |

## Blockers

None.

## Current State

deployment_map.xml v3 reflects production reality as of 2026-04-16. All four
ClientPlatform-relevant modules are at current head:
- `yang-v2.3.8` (commit c9b382d5, 2026-04-13)
- `bd-v2.24.1` (commit d08d4bb7, 2026-04-15)
- `partners-api-v1.15.9` (2026-04-15)
- `portal-auth-v1.12.3` (commit 432d995f, 2026-04-15)

Working tree dirty with the three documentation files above and pre-existing pod work
(other agents). Will commit only my three files via `--only`.

## Next Steps

- [self] Commit deployment_map.xml + task_order status flip + this log via
  `git commit --only --author="0.4.0_DT_ClientPlatform <0.4.0_DT_ClientPlatform@opal.agent>"`.
  No tag (this is org-only documentation, not a pipeline deploy).
- [self] MCP CTO with completion + commit hash so RAVC closes.
- [1.0.0_SA_CTO] Validate that pages_served / pipeline_split / known_gotchas now meet the
  acceptance criteria. If anything still gaps, request specific fix not blanket rework.
