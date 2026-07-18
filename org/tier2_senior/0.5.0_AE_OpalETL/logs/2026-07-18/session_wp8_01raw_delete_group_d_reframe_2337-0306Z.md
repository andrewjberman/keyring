# 0.5.0_AE_OpalETL -- 01_raw FATAL resolved + download-schedule disabled + 49F->Group-D reframe (2026-07-17 23:37Z - 2026-07-18 03:06Z)

**archetype:** MIXED (DIAGNOSE + COORDINATE + DEPLOY)
**secondary_archetypes:** SCRIBE (Andrew-direct records + 2 memory reframes)

Delta since the prior log (@ f80d73877). This window resolved a live client-data FATAL of my own making, disabled a dead rule, absorbed two Andrew-direct reframes, and confirmed the go-forward Schwab ingest. 2 commits + a 5,977-object S3 delete + 2 memory reframes.

## 1. 01_raw FATAL -- FULLY RESOLVED (my own migration debris; near-miss caught twice)

0.6.2's cell-3 cutover prove-on-fire surfaced a LIVE FATAL (paging opal-critical-surface-alerts since 07-16 22:15Z): my prior WP8 01_raw-history copy landed flat unzipped CRS{date}.{TYPE} objects into opal-data-assets/schwab/08242234/bronze/, colliding with the live Schwab-Box puller's zips -> landing-guard double-occupancy rc=6. Grounded: the puller lands a DOUBLE-zip (outer.zip->inner.zip->CRS); the flat copies are BYTE-IDENTICAL to the inner-unzipped content (md5 1e50949f... proven).

TWO SCOPE NEAR-MISSES CAUGHT by enumerating the FULL tree before deleting (CTO condition-1):
- NOT 209: the guard's collision_n=209 is only the current RUN-WINDOW subset; the true redundant set is 5,977 (double-occupancy across all history). Deleting only 209 = incomplete (re-FATAL as the window moves).
- NOT all 7,222 flats: 1,245 are the ONLY monolith copy of pre-puller history (no colliding zip) -> KEEP. A naive all-flats delete = data loss.

VERIFY (CTO-gated, full per-object; feasible because flat ETags are single-part md5s -> ~9.6GB of zips, not 100GB+ of flats; timeout-hardened + resumable after a first-run connection stall): **5977/5977 byte-identical, 0 excluded**, reconcile ties 5977+0+1245=7222.
DELETE (Andrew delete-word + CTO clean-verify->straight-to-delete): **5977/5977 deleted, 0 errors**, key-by-key from the verified list (batched, hard safety asserts, never a glob).
POST-DELETE estate-wide: **COLLISIONS=0**, flats 1245 (unique KEPT), zips 6011 (intact), 13233->7256, latest 20260716 intact. Guard clean, NEVER weakened. CTO ACCEPTED (030512Z).

## 2. download-schedule rule DISABLED (Andrew-direct, canonical TF)

Andrew-direct "disable the dead download-schedule rule". `canonical-schwab-si2-download-schedule` (dead GUI channel -> SchwabAutoDownload[frozen] -> SchwabS3Sync -> opal-data-schwab staging) is separate from the live monolith REST pull. Changed schedule.tf state ENABLED->DISABLED (commit 7a78bb537), safe-apply 0-add/1-change/0-destroy, 0-diff, LIVE describe-rule=DISABLED. Pushed 1ba779e0b. CTO informed.

## 3. TWO Andrew-direct reframes recorded + broadcast (same-turn law)

- **SmartX two-axis CORRECTION (CTO 223133Z, Andrew-challenged):** my "yaliu needs a fullAccess grant" was a mis-frame -- fullAccess/view is model-DEFINITION catalog ownership, NOT data access. Reframed memory (project_smartx_yaliu_account_of_record) to the TWO-AXIS HYBRID (opal7 owns our 11 model defs = permanent; yaliu has the account/client+platform DATA opal7 lacks). NO grant to pursue; retracted the grant-request offer to Andrew.
- **49F runner -> OPAL_CONSOLIDATION Group D (Andrew-direct 2026-07-18):** /49-schwab-conv skill OBSOLETE (programmatic Schwab Box); the 49F runner completely refactors into Group D platinum scripts (Group-A source files pull opal-data-assets/schwab/ 0833 silver); 49F+bd need NO Schwab reconciliation patches (0833-only). => trn_nna step-5 converter retirement (CTO/DS-GO'd) SUPERSEDED (I stopped it); gold-runner-pointing moot. Recorded feedback_49f_runner_refactor_into_group_d_platinum_0833_only; broadcast CTO+COO+MSTR + DS stand-down.
- **CELL-4 Schwab-box re-frame (Andrew-direct 234846Z):** the box (i-0f3d57a97f14727af) is the SCHWAB BOX = essential authenticated-REST endpoint, NOT a "quartz spike," NOT retire-able. "box disposition" STRUCK; residual = sever its opal-data-schwab data dependency before bucket delete. Ledgered 800fda5a7.

## 4. Go-forward Schwab ingest CONFIRMED (Andrew's ask)

Both 0824 + 0833 daily-pull schedules ENABLED (Schwab Box REST), both fresh at 20260716 = correct T-1 (trading frontier 07-17; Schwab T-1, 07-17's file not due until Sat/Mon -- NEVER#1 resolved). 0833 guard CLEAN; 0824 guard clean after the delete. canonical-schwab-runner (live opal-data-schwab/01_raw reader) censused as a hard BUCKET-delete prerequisite (repoint or Group-D-replace before the bucket dies).

## Compiler Tools

| Tool | Result | Note |
|---|---|---|
| comp-grep / Grep (targeted) | PASS | download-schedule TF locate (comp-grep over full infra TIMED OUT -> fell back to scoped ripgrep Grep -- gap: comp-grep too slow over infra/) |
| terraform plan / safe-apply | PASS | download-schedule disable: 0-add/1-change/0-destroy, 0-diff, live describe-rule=DISABLED |
| rail-checked raw aws | PASS | s3 list/head/delete-objects, events describe/list-rules, scheduler list-schedules, iam n/a; lib/trading_calendar (NEVER#1 frontier) |
| boto3 verify+delete scripts | PASS | 5977/5977 byte-identical (double-unzip + md5 + size); 5977 deleted 0 errors; estate-wide recount collisions=0 |

What worked: enumerate-the-full-tree-before-deleting caught BOTH the 209-incomplete and the 1245-data-loss traps; single-part ETag insight made full per-object verify cheap; timeout+resumable rewrite recovered from a connection stall. What failed: comp-grep over infra/ timed out (120s) -- used scoped Grep. Gap: comp-grep perf on large trees + still no comp-tool models the schwab monolith trees (12th+ log).

## AE Deployment + Destructive-Op Verification

```
download-schedule DISABLE: schedule.tf ENABLED->DISABLED (7a78bb537) -> safe-apply (1 changed) -> 0-diff -> describe-rule State=DISABLED -> push 1ba779e0b
01_raw DELETE: verify 5977/5977 byte-identical (0 excl) -> delete-objects 5977/5977 (0 err) -> estate-wide recount: collisions=0, flats 1245 kept, zips 6011 intact, latest 20260716 intact
```

## MCP traffic

~30 handled. Significant IN: Andrew-direct x4 (delete-word, yaliu-grant-yes[retracted-premise], 49F->GroupD x2, disable-download-schedule, confirm-ingest); CTO x8 (two-axis correction, CONCUR-A/5977, verify-plan gate, delete-GO, 01_raw guardrails+concur, download-schedule ack, delete ACCEPTED); 0.6.2 x6 (cutover URGENT FATAL, CELL-4 sever plan, canonical-schwab-runner nudge, ACKs); DS~A x3 (step-5 GO/supersede acks). Significant OUT: ~16 (49F->GroupD broadcast x3, step-5-superseded to DS, CTO disposition+scope-correction+verify-plan+delete-close, download-schedule FYI, canonical-schwab-runner census, 0.6.2 cutover cert). RAVC: cell-3 cutover cert CLOSED; 01_raw delete ACCEPTED by CTO.

## Current State (zero-prior-context)

- **01_raw FATAL: RESOLVED.** 5,977 redundant flat copies deleted from opal-data-assets/schwab/08242234/bronze/; 1,245 unique pre-puller history KEPT; guard clean (0 collisions estate-wide). 0824 ingest now fully robust. Next scheduled 0824 pull (10:15Z) = live guard re-confirm.
- **Schwab ingest:** both 0824+0833 daily via the Schwab Box (REST) to opal-data-assets/schwab/, fresh at T-1 (20260716), guards clean.
- **download-schedule:** DISABLED (canonical-schwab-si2-schedule module).
- **SmartX:** models_summary yaliu fix LIVE (v1.7.0); two-axis hybrid is the correct+deployed state; NO grant to pursue.
- **49F runner:** refactors into OPAL_CONSOLIDATION Group D (CTO's master); /49-schwab-conv obsolete; step-5 retirement dropped as moot.
- **opal-data-schwab teardown (WP8) remaining:** (a) canonical-schwab-runner reader repoint/Group-D-replace [censused prereq]; (b) sync_schwab_onedrive_to_s3.py writer retirement (L5b); (c) sever the Schwab-box's opal-data-schwab data dependency (verify none remains post cell-3); then the bucket deletes. Prefix cells: CELL1+3 RETIRE on D-seq, CELL2 anonymizer HELD (security/Andrew).

## Next Steps

1. [10:15Z] confirm the next scheduled 0824 pull's guard = clean (live re-confirm of the 01_raw fix).
2. [OPAL_CONSOLIDATION Group D, CTO's master] the 49F runner refactor -- Group-A source files -> opal-data-assets/schwab/ 0833 silver (Andrew step 1).
3. [WP8 bucket-delete census] resolve canonical-schwab-runner + sync_schwab_onedrive_to_s3.py + the box data-dependency before the opal-data-schwab delete.
4. [event-driven] cell-3 old-grant retire (D1 ~07-18/21); CELL2 anonymizer security cell (CTO->Andrew).
