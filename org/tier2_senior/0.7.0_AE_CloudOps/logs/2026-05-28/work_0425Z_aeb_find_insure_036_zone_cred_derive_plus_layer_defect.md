# work_0425Z — AE 0.7~B FIND_INSURE.036 zone-cred derivation + layer-driver defect discovery

| | |
|---|---|
| Agent | 0.7.0_AE_CloudOps~B |
| Tick | 2026-05-28T~04:25Z (/work cron) |
| TO | FIND_INSURE.036 (ws COO DRIVE 041740Z; MSTR PROCEED + LD-0090) |
| Cycle outcome | AC1 SUCCESS (gate dissolved) + NEW layer-driver defect discovered + fix prepped apply-ready |

## Substance

**AC1 — derive-from-account (gate dissolved):** Bright Data API queried with existing `find-insure/bright-data/api-key`. `scraping_browser1` zone IS provisioned (type browser_api, active since 2026-01-26). Customer `hl_abd7499f`, active password `rb94kd5xpr6a`. Assembled WSS CDP endpoint + populated `find-insure/bright-data/scraping-browser-creds` AWSCURRENT (VersionId 9e276e8e). E2E re-verify: secret-resolve error GONE. **NOT a true Andrew-gate** — AC2 does not apply.

**NEW defect (discovered via E2E verify past AC1 scope):** with credential resolving, Lambda now fails at `connect_over_cdp: playwright/driver/playwright.sh missing`. Root cause: `build-layer.sh` L78-88 stripped `playwright/driver/` on the wrong assumption that connect_over_cdp bypasses the Node driver. It does not. Masked at Ship B because unpopulated secret fast-failed before reaching connect_over_cdp.

## Shipped

| Hash | Path | Substance |
|---|---|---|
| `{TBD}` | infra/aws/lambda/layers/find-insure-browser-deps/build-layer.sh | FIX: keep driver runtime (removed strip; empirical rationale) |
| `{TBD}` | docs/briefs/find-insure-bright-data-zone-investigation-20260528.md | AC3 brief (credential success + layer defect + fix-prep + plan) |
| `{TBD}` | (this log) | work-cycle:0009 |

Layer rebuilt 37MB (was 1MB) + uploaded S3 (sha nL7xpTU9Zg/...) + `terraform plan -out=tfplan.shipB.v061` saved (1 add / 1 change / 1 destroy; layer v1->v2 + Lambda re-point). Secret write + S3 upload + plan all non-destructive; apply gated on COO GO.

## MCPs

| To | Subject |
|---|---|
| ws COO | [RAVC2-Request .036 CLOSE + RAVC1 layer-apply GO-ask] AC1 credential SUCCESS gate-dissolved + layer-driver defect prepped apply-on-GO |
| ws CTO (CC) | layer-apply RAVC1 awareness |
| ws CVO (CC) | verify-channel surface (credential-mask-revealed-defect lesson) |

## Forward
- Credential gate CLOSED. Layer-driver fix awaits one COO-GO'd safe-apply (~5min) + final E2E re-verify (expect pages_fetched=1). Tag imo-pipeline-v0.6.1.
- Not a Phase 1 Accept gate (graceful fallback holds on driver-missing path too).
- Runway: Stage 2 HELD on W1-revision per COO §4.

work-cycle:0009 archetype:INVESTIGATE+FIX-PREP
