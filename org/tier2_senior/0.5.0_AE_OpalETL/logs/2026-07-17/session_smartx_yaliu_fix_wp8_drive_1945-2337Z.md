# 0.5.0_AE_OpalETL -- SmartX models_summary yaliu fix (deployed) + WP8-DECOM lead drive (2026-07-17 19:45-23:37Z)

**archetype:** MIXED (DIAGNOSE + DEPLOY + COORDINATE)
**secondary_archetypes:** IMPLEMENT (lambda fix), SCRIBE (Andrew-direct records + memory reframe)

Session opened on startup protocol; Andrew-direct took it into a SmartX diagnosis+fix+deploy, then a
WP8-DECOM lead drive. 8 commits + tag smartx-pipeline-v1.7.0. All destructive/scope-changed items HELD
correctly on human confirmation.

## 1. SmartX models_summary FIX -- diagnosed, deployed, verified (the Andrew-direct P0)

Andrew asked what SmartX was doing / why 500s / where. Diagnosed the daily `smartx-assets-daily-pull`
DirtyRunError: `models_summary` (GET performance.smartxadvisory.com/models/summary?platform={id}) HTTP
500. **Exercised 2x2 A/B (token x platform-id)** via the lambda's own auth_bundle:
- opal7 platform-id 27d20c6b -> 500 under BOTH tokens; yaliu platform-id 09a26328 -> 200 under BOTH.
- The **platform-id VALUE is the sole discriminator** -- NOT auth (both tokens accepted), NOT a vendor
  outage. Root: lambda_function.py:171 resolved roster.platform_id from opal7's users/access.
- Corrected my own prior "persistent vendor 500, wait for heal" disposition (wrong-axis: varied token/time,
  never platform-id). Andrew was right ("wrong endpoint vs auth; use yaliu not opal7").

**FIX (option a):** moved `models_summary` PLATFORM_FEEDS -> ACCOUNT_TIER_PLATFORM_FEEDS (identical bronze
key), pulled in `_pull_feed9` with the yaliu client + yaliu platform-id; removed from opal7 `_platform_urls`
(dropped now-unused PERF_HOST import); corrected the stale header premise + tests. 5 files, tests + ruff
0.15.11 green. **Deployed canonical TF** (below). **Verified exercised:** invoke -> {"status":"CLEAN"};
models_summary landed **5,230,241 B via yaliu** (head-object 21:20:12Z, == the HAR 5.2MB; the full sheet
needs Accept:application/json -- my earlier "375KB" probe was missing that header). CTO accepted; shape gate
CLOSED.

## 2. "ONLY yaliu" -- Andrew-direct recorded, then CTO two-axis CORRECTION (my mis-frame owned)

Andrew: "we should only be using yaliu ... memory locked ... no more opal-data-assets instances with this
latent issue." Locked memory; **sweep: the ONLY opal-data-assets SmartX producer is smartx-assets-daily-pull
(fixed); no other instance.** I first framed the owned-book as "yaliu needs a fullAccess grant" -- **CTO
source-grounded this WRONG (223133Z)** and I reframed the memory: it is a TWO-AXIS HYBRID, already deployed,
both correct: AXIS A model-DEFINITION ownership (opal7 OWNS our 11 defs -> needed to enumerate the owned
book; PERMANENT, expect_min_models>=11 enforces it); AXIS B account/client+platform DATA (yaliu has 452
accountAccess + holdings/client + models/summary that opal7 accountAccess=0 LACKS). "only yaliu" = the DATA
axis; NO fullAccess grant to pursue (catalog field, not data-access). Retracted the grant-request offer to
Andrew.

## 3. WP8-DECOM lead drive (Andrew-approved 6024e85ed)

- **Cell-3 (0.6.2 SI2 code re-home):** PART-2 confirmed (grounded download-schedule EventBridge ENABLED,
  retirement separable from the live REST pull). Additive IAM grant GO=(A) decoupled prep -> 0.6.2 applied +
  I independently validated (new home 9 artifacts, box-read 35842B, my simulate=allowed) -> RAVC CLOSED.
  **Cutover GO'd now (Andrew-prompted)** -- ruled the code-read flip ORTHOGONAL to the D1 parity clock;
  0.6.2 flipped (byte-identical, behavior-neutral) -> **cert ACCEPTED**. Old-grant retire + data decommission
  stay D5.
- **CTO six-prefix batch (203910Z):** ledgered -- CELL1(03_silver)+CELL3(_archive) RETIRE on D-seq; CELL2
  (anonymizer, 03_mappings=client re-id key) HELD security/Andrew; CELL4 (quartz SI2 live spike) HELD 0.7.0.
- **Step-5 producer retirement** (`convert_schwab_trn_to_nna_silver.py`, AE-owned /49-schwab-conv): DS~A
  delivered flip evidence (26,504 cells/0 mismatch seam parity); **CTO cleared the CORRECTNESS gate
  (224011Z)**; I execute the skill edit post-tonight-23:00Z-confirm (DS~A Monitor armed). PRESERVE the legacy
  bd trn_nna artifacts (SCHWAB_FLOW_SOURCE=legacy fallback), NOT a secure-delete.

## 4. 01_raw FATAL disposition -- HELD safely on a scope correction (near-miss caught)

0.6.2's cutover prove-on-fire surfaced a LIVE FATAL (pre-existing since 07-16 22:15Z, orthogonal to the
flip): my prior WP8 01_raw copy landed flat unzipped CRS{date}.{TYPE} objects into 08242234 monolith bronze,
colliding with the puller's zips -> landing-guard double-occupancy rc=6 (paging critical-surface-alerts).
Grounded: the flat objects are BYTE-IDENTICAL to the puller's inner-unzipped content (puller lands a
DOUBLE-zip; md5 1e50949f... matches) -> redundant, removable without data loss. **Andrew confirmed the delete;
CTO concurred (bucket owner) -- BUT scoped to "209".** Enumerated the full tree FIRST (CTO condition):
**the real redundant set is 5,977 (double-occupancy across all history), not 209 (the guard's current
run-window subset); 1,245 flat objects are the ONLY monolith copy of pre-puller history -> KEEP.** HELD the
delete + re-surfaced the corrected scope to Andrew+CTO rather than delete on a stale number. Double-zip
routed to 0.7.0 (puller-format finding, possible 17a). **Nothing deleted.**

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-glob / comp-grep (x12+) | PASS | SmartX probe/endpoint provenance, opal7-instance sweep, WP8 touch-point census, /49-schwab-conv step-5 -- all on-rails, denominators printed |
| ruff 0.15.11 | PASS | 5 edited lambda files "All checks passed" (matches the Rule-14 pin) |
| py_compile + test_key_mapping/test_pull/test_silver | PASS | grammar + engine + converter suites green post-edit |
| terraform plan / safe-apply | PASS | 1-change (source_code_hash K2WLxWKs->4Iw0TWc), 0-diff confirmed, HALTGT clean |
| rail-checked raw aws | PASS | EventBridge describe-rule, CloudWatch, s3 ls/cp/head-object, iam simulate-principal-policy (1 --resource-arns), lambda invoke, secretsmanager (vendor probes, egress lifted) -- markers logged |

What worked: the lambda's own auth_bundle reused for a faithful A/B (no divergence); enumerate-before-delete
caught the 209-vs-5,977 scope near-miss. What failed: build-and-upload.sh needed TMPDIR=C:/Windows/Temp +
no MSYS_NO_PATHCONV (node temp-path). Gap (11th+ consecutive log): still no comp-tool models the monolith
schwab/smartx trees OR the dying-bucket prefixes -- census was comp-grep + rail-checked raw aws.

## MCP traffic

~28 handled. Significant IN: Andrew-direct x4 (SmartX diag ask, yaliu-only, cutover-prompt, delete-confirm +
yaliu-yes); CTO x6 (models_summary ruling, deploy-accept, two-axis correction, prefix batch, step-5 gate,
01_raw guardrails+concur x2); DS~A x3 (step-5 route, flip evidence, coordination ACK); 0.6.2 x8 (cell-3
proposal, sequencing, DONE(A), cutover URGENT finding, cert ACKs). Significant OUT: ~14 (Andrew-direct
broadcasts x3 to CTO/COO/MSTR, 0.6.2 GO(A)+cert, CTO disposition+scope-correction, DS step-5 coord, 0.7.0
double-zip). RAVC: models_summary deploy (CTO-accepted); cell-3 additive-IAM + cutover cert (CLOSED);
prefix batch + step-5 (ledgered/ACK'd).

## AE Deployment Sequence + Verification (smartx-pipeline-v1.7.0)

```
code(01f54452a) -> build-and-upload.sh (sha 4Iw0TWc, write VERIFIED) -> source-map commit(6d89f32d6)
-> terraform plan (1 to change: assets_daily_pull source_code_hash) -> safe-apply (Apply complete! 1 changed)
-> plan (No changes) -> record-terraform-deploy(e42e8fc0c) -> tag smartx-pipeline-v1.7.0 -> push --follow-tags
Verify: aws lambda invoke -> {"status":"CLEAN","scopes_total":12,"scopes_clean":12,"failed":[]}
        head-object smartx/platform/bronze/models_summary/20260717/summary.json -> 5,230,241 B (via yaliu)
```

## Current State (zero-prior-context)

- **SmartX:** models_summary fix LIVE + CTO-accepted (tag smartx-pipeline-v1.7.0, commit 01f54452a). Owned
  book stays opal7 PERMANENTLY (two-axis hybrid, memory reframed). NO yaliu grant to pursue on the corrected
  framing. C5 daily pull now runs CLEAN.
- **WP8 cell-3:** cutover flip DONE + cert ACCEPTED; old SchwabOpsCodeRead grant + opal-data-schwab data
  decommission still D5-gated (D1 clean cycles ~07-18/~07-21).
- **WP8 step-5:** correctness CLEARED; the /49-schwab-conv skill edit (remove convert_schwab_trn_to_nna_silver.py
  invocation + reconcile ~6 mandatory-trn_nna assertions; KEEP the converter script as legacy fallback) executes
  on DS~A's 23:00Z-nightly confirm.
- **01_raw FATAL:** HELD. Real redundant set = 5,977 flat copies (double-occupancy, byte-identical to puller
  zips); 1,245 unique pre-puller-history copies KEEP. Delete keys computed at scratchpad/delete_keys.txt (209
  window subset) + scope_collisions.py (full 5,977). CTO just CONCUR'd (A) full root fix @233653Z (unread at
  log time). Awaiting Andrew scope re-confirm. Nothing deleted.

## Next Steps

1. [NOW] Read CTO 233653Z (CONCUR A) + Andrew scope re-confirm -> per-object verify the 5,977, delete EXACTLY
   the verified-redundant set (never the 1,245 unique, never the puller zips), post-delete guard re-run.
2. [on DS~A 23:00Z ping] execute the /49-schwab-conv step-5 edit (preserve the converter script + bd artifacts).
3. [Andrew] yaliu owned-book grant: draft the SmartX request ONLY if he confirms it is single-account
   consolidation (not the retracted data-gap premise).
4. [D1 ~07-18 12:15 UTC] cell-3 old-grant retire + opal-data-schwab data decommission sequence (D5).
