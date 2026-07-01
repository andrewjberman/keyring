# ADVI_INFREF cutover LANDED (L5) + morning-pull retimed to 9:00 ET -- session 0315Z->1432Z (07-01)

**archetype:** MIXED
**secondary_archetypes:** DEPLOY (primary), DIAGNOSE, COORDINATE, VALIDATE

Agent: 0.6.1_AE_PartnerETL (INF-pipeline AE). Resume of the pre-reboot INFREF rebuild handoff; drove the one-time canonical rebuild through a 6-failure firefight to a to-the-cent atomic cutover, then applied an Andrew-direct morning-pull retiming. Served now delivers the rebuilt canonical INF data; project HELD OPEN for the multi-day tail per Andrew's tri-validation close gate.

## Summary of the window

1. **Resumed** the INFREF rebuild (SSM 29629fb9 on i-0ed5afded2ebd4ed4). Grounded LIVE: rebuild was mid-STEP2b, healthy.
2. **v3 (29629fb9) hit the 2h SSM executionTimeout** @03:48:02Z (Start 01:48:02 -> End 03:48:02 = 7200s exact) mid-STEP2b (txn/perf frozen at 06-14). Grounded as slow-compute NOT a hang (disproved CVO's inferred hang via live silver-mtime advance 05-28->06-14 during the S3-log-silent window; log only flushes at STEP boundaries).
3. **Relaunch #1 (f7bdc4a8)**: STEP2b-tail (txn/perf 06-13..06-30 overwrite) + STEP3, 4h ceiling, skips log-proven-complete STEP2a. STEP2b GREEN; STEP3 FAILED on `--stage compute --run-date` coherence-guard reject (latent wrapper bug -- v3 never reached STEP3).
4. **Relaunch #2 (71fec3f7)**: env-pin fix (rebuild-local dispatch copy honoring REBUILD_RUN_DATE=06-30 -> threads BOTH guards: coherence guard fires only on --run-date; pull-complete assert 06-30==06-30). Cleared the date catch-22 (07-01 UTC-roll made a bare --run-date drop resolve wrong-day). STEP3 FAILED on sync_scripts() basename collision (4 stale bronze/gold pull-script orphans vs newer manual_api de-convert versions).
5. **Relaunch #3 (2961fd47)**: DECLARED_PRECEDENCE(manual_api) in the rebuild-local dispatch (DS landed the durable shared orphan-delete in parallel). CLEARED all guards -> full re-derivation ran (~55min) -> STAGED @05:36:49Z.
6. **Keyspace gross-mismatch STOP** (staged 2090 vs served 6407) diagnosed to CRUFT not truncation: firm/ gap = _meta history; clients/ 600-vs-1302 = 690 stale-April detail.json orphans + 11 pre-06-30 dropout households; staged = EXACTLY the 600 06-30-active households (0 missing/0 spurious); firm AUA staged==served==$202,125,678.08 to the cent. Andrew's "suspicious 2x" catch forced the airtight proof, which CLEARED the rebuild.
7. **CVO L3 GREEN** (c5a4fc883): to-cent AUA + 419 client-grain + ~17,275 full-history pts, 0 diffs. **COO+CTO never-widen sign-off** (verified DELTA=0).
8. **L5 ATOMIC SWAP fired+landed @06:07:28Z**: `aws s3 cp --recursive platinum/_rebuild/20260630T234458Z/ -> platinum/` (additive, never-widen-safe; orphan 217.0 preserved). Verified served post-swap. Held rules re-enabled. _meta ACCEPT (benign, CVO-confirmed not portal-rendered).
9. **Tri-attested** (AE+DS+CVO GREEN); **CTO L5 co-signed+closed** (independently grounded via value-parity). Ledger L2/L2b/L3/L5 CLOSED.
10. **Andrew-direct morning-pull retiming**: process start 8:13->9:00 ET (+47min, all 12 morning-pull EventBridge rules commensurate) to avoid pulling before Orion settles prior-day close (~$440K/0.22% AUA understatement Andrew spotted vs Orion display). TF applied+live+pushed.

## MCP traffic

~45 messages handled. Significant: DS~A harness-fix c28755ccf + [STOP] timeout-correction + [STOP] keyspace-precheck-FAIL + validate_post_swap ALL-GREEN + closure-attestation + orphan-delete ownership; CVO L3-GREEN (c5a4fc883) + L5+verify-channel cutover-attestation (8605413bc) + required-closure-validator ACK; COO never-widen sign-off + tri-validation closure-gate CARRIED (holds REGISTRY flip) + L1-watch-adjust + L7-timing-carry-as-close-condition; CTO 3 relaunch guards + L5 co-sign+close + L7 carry-forward recorded in ledger. Outbound: per-terminal-step RAVCs (staged/L3/swap/L5), the tri-validation closure gate set to all closers/validators, pull-retiming RAVC + L7-carry flag.

## Compiler Tools

| Tool | Run | Result | Note |
|---|---|---|---|
| comp-which | routed platinum-consumer blast-radius Q | PASS | -> pipescript --resource + comp-platinum reverse |
| pipescript --resource platinum/firm/ | pre-swap blast radius | PASS | consumers = inf-portal-publisher / PPI-08 router / inf-client-detail / gold-dispatch; never-widen-safe confirmed |
| comp-platinum reverse | platinum/firm/dashboard.json | PASS | INF_D_04 -> CF /api/scoped/advisor-intelligence/* -> ClientsTab |
| pipescript advi-inf | ETL resources for the /draw diagrams | PASS | full estate: 2 EC2 runners, ~15 Lambdas, event-chain |
| comp-manifest/surface-check | via safe-commit (TF pull-retiming) | PASS | 10 files touch no critical surface |

What worked: pipescript/comp-platinum cleanly grounded the swap blast radius + the served-key -> portal trace pre-fire. What failed: none. Gap: none new. Rail note: extensive in-flight S3/SSM progress reads + the TF-comment residual-grep ran with inline `# rail-checked:` markers (in-flight rebuild progress/liveness + verify-own-change-vs-live = banked carve-outs; comp-tools model TF-desired + served-artifact, not SSM RunCommand state / in-flight staging accumulation / live EventBridge rule state). Native Grep used for TF-edit verification (nudge-and-proceed).

## Deployment Sequence + Verification (AE)

**A. INFREF cutover (S3/SSM, no git -- rebuild wrappers in s3://opal-data-inf/code/rebuild/):**
- Rebuild: SSM 2961fd47 (env-pinned RUN_DATE=06-30, DECLARED_PRECEDENCE-patched rebuild-local dispatch) rc=0, sentinel 05:36:49Z. `Apply` = additive swap cp --recursive @06:07:28Z, exit=0.
- Verify (served, post-swap): firm/dashboard.json mtime 06:07:28Z, total_aua 202125678.08 (==L3 baseline to cent); 32 firm views + 600 current hh refreshed; legacy orphan clients/217.0 preserved (06-02) = never-widen. DS validate_post_swap ALL-GREEN 2090/2090 byte-identical. CVO L5+verify-channel GREEN (live value-parity diff 0.0). CTO L5 co-sign independently grounded.
- Held rules re-enabled (verified ENABLED): inf-etf-ownership-on-gold-complete, opal-inf-value-parity-hourly.

**B. Morning-pull retiming (TF, inf-pipeline module):**
- Commits b2f61bed8 (schedules) + 35b6c9898 (description/comment sync). Pushed CLOUD 17eaca870. safe-deploy clean.
- `safe-apply` (HALT_ACK=1): `Apply complete! Resources: 0 added, 12 changed, 0 destroyed.`
- Live-verify (aws events describe-rule): opal-inf-jwt-fetch cron(0 13)=9:00 ET, inf-api-positions-daily cron(37 13)=9:37, inf-api-txn-daily cron(47 13)=9:47, inf-canonical-prices-daily cron(47 14)=10:47 -- all ENABLED. 0-diff vs TF-desired.

## Blockers

None. Cutover complete; project gated on the multi-day tail (external time-gate: L1 first-nightly-pull tomorrow, L6 day-over-day) -- not a blocker.

## Current State (zero-context handoff)

**ADVI_INFREF cutover = LANDED + LIVE + tri-attested. Project OPEN, riding the multi-day tail.**

- **Served:** s3://opal-data-inf/platinum/{firm,advisors,clients}/ IS the rebuilt canonical data (rebuild ts 20260630T234458Z), AUA $202,125,678.08 to the cent. Rollback snapshot intact: _pre_rebuild_backup/20260630T234458Z/ (6061 obj/5.74GB).
- **Ledger** `org/critical_paths/change_management/20260630T2035Z_advi-infref-cutover-rebuild_deploy_completion.md`: L2/L2b/L3/L5 CLOSED. OPEN: L1 (first-nightly-pull parity, ~tomorrow), L4 (perf-incremental), L6 (day-over-day temporal stability), L7 (cron-TF-delete for single-runner). CTO owns L1/L6/L7.
- **Closure gate (Andrew-direct, memory `project_advi_infref_no_close_until_tri_validated.md`):** COO HOLDS the REGISTRY flip until all tail legs close + a 2nd round of AE+DS+CVO project-COMPLETE attestations. Tonight's tri-attestation was for the CUTOVER ACTIVATION only.
- **Morning pull retimed:** all 12 inf-pipeline EventBridge morning-pull rules shifted +47min (start opal-inf-jwt-fetch cron(0 13)=9:00 ET). Effective tomorrow (July 2). L7 CARRY-FORWARD is a recorded close-condition (CTO ledger + COO REGISTRY-hold): the single-runner --chain full MUST adopt cron(0 13)=9:00 ET or the timing fix reverts at L7.
- **Follow-ups (tracked w/ COO, non-blocking):** (1) header_metrics_fresh.json PROD portal repoint (getHeaderMetricsFresh advisor-intelligence.ts:434; INF_D_00e removed a406ed891, DEV repointed) + GC -- DT lane. (2) CloudFront invalidation platinum/firm/* + 307 clients for immediate edge freshness (else TTL). (3) nightly orphan-GC broken since April (departed households never GC'd). (4) INF_B_00 honor OUTPUT_PREFIX (stop the _meta leak to served during rebuilds). (5) settlement-aware pull (Orion prior-day refresh undocumented/variable -- CTO spinning as its own charter; the fixed +47 offset is interim).

## Next Steps

1. **Tomorrow ~9:00-9:47 ET: watch L1 first-nightly-pull** (now at the new time; do NOT read old-8:30 silence as a miss). RAVC [2.0.0_SA_COO] + [1.0.0_SA_CTO] on L1 parity.
2. **Verify the AUA-vs-Orion gap** at the settled pull: does a 9:00-ET-settled 06-30/07-01 pull reproduce Orion's ~$202.57M (timing) or stay $202.13M (scope)? Disambiguates the ~$440K.
3. **L7 (after L6): confirm the single-runner adopts cron(0 13)=9:00 ET** before CTO closes L7 (the timing-carry close-condition).
4. Support [1.0.0_SA_CTO] on L4/L6/L7 tail + the 2nd-round project-COMPLETE tri-attestation before [2.0.0_SA_COO] flips REGISTRY.

## Contacts

CVO=3.0.0_SA_CVO (L3/L5/verify-channel + required closure-validator), DS~A=0.4.0_DS_ClientPlatform~A (validate_post_swap + data-correctness closure-attestor + orphan-delete owner), COO=2.0.0_SA_COO (never-widen sign-off, REGISTRY-flip holder, tail tracker), CTO=1.0.0_SA_CTO (L5 co-sign, L1/L6/L7 owner, L7 timing-carry enforcer).
