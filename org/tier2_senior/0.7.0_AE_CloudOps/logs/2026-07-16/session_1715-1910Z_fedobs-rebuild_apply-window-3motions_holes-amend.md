# 0.7.0_AE_CloudOps -- fedobs derive rebuild + a 3-motion apply window (all through CTO's gate) + eclipse holes-manifest AMENDED_2

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE, SCRIBE, COORDINATE
**serial:** 0.7.0_AE_CloudOps | **date:** 2026-07-16 | **window:** ~17:15Z -> ~19:10Z

## Summary

1. **FEDOBS DERIVE-IMAGE REBUILT (~Z routed, my standing rebuild lane; ledger 20260716T1740Z 2/2).**
   build-derive-image.sh --go -> CodeBuild globgrph-derive-build:1adef157 SUCCEEDED; ECR
   opal-globgrph-derive-runner:latest sha256:174ac79f (was ...94819df5), baking cca39dbe1 (fedobs
   coevolution OOM fix, source<>graph_head). RUNTIME-verified (not build log): read-only run-task on
   the NEW image (globgrph-fedobs-producer:1, python file-read override) -> exit 0, FIX_PRESENT. Did
   NOT run the producer (no served-artifact write; ~Z's in-VPC 949-pairs/no-OOM proof covers the
   logic; the nightly is ~Z's to verify). First nightly to serve healthy = 04:30Z 2026-07-17.
2. **APPLY WINDOW -- 3 motions, ALL through CTO's apply gate (he read every plan), sequence-by-care
   (mechanical first, careful last) as he ruled:**
   - **(a) bd-exporter monolith-schwab grant** (CTO-routed 181602Z; ledger 20260716T1823Z 3/3;
     bd-v2.52.0): NEW aws_iam_role_policy.bd_exporter_monolith_schwab_read, GetObject on
     opal-data-assets/schwab/08242234/silver/* + ListBucket (prefix-condition split to its OWN Sid so
     it cannot leak onto GetObject). Plan 1/0/0 pure-add. 22a VERIFIED: simulate ONE resource/call
     (GetObject exact key allowed; ListBucket +context allowed; positive control opal-data-bd separate
     invocation allowed) + APPLIED live get-role-policy (both Sids present). Target = monolith
     post-redirect home, NOT dying opal-data-schwab; cross-firm-cot deny is cot-scoped, not in play.
     Unblocks 0.4.0_DS~A's L4 trn_nna source-flip (last manual schwab chain leg) -- ~A notified, their
     exercised read on CTO's word.
   - **(b) ~Z P2-snap twin re-add** (6c65fb7a8; ledger 20260716T1842Z 2/2; globgrph-v0.1.19): +2
     freshness_stale alarms (code_heat_snap + fedobs_coverage_snap), plan 2/0/0. BREACH-RISK CHECKED:
     both landed State=OK not ALARM (live ProducerAgeHours datapoints [1.48,2.48]h << 30h, namespace
     Opal/FreshnessAlarm; ms_heat positive control [3.57,4.57]h). SELF-CATCH: my first datapoint query
     hit the WRONG namespace, read 0 for both snaps AND the ms_heat positive control -- the control's
     impossible-zero exposed the artifact before I wrongly flagged a false breach-risk (3rd wrong-axis
     catch today, all caught by a control not by care).
   - **(c) >=-token FRONTIER predicate** (the careful last one; ledger 20260716T1902Z 3/3;
     opal-assets-absence-v0.2.0): replaced exact-token match with frontier>=expected on the SHARED
     absence-checker (6 rows). Date regex pinned 20\d\d + date-validated so the schwab account number
     cannot masquerade as a token. PER-ROW MATRIX (both predicates vs all 6 rows' LIVE prefixes): ONLY
     inf-mirror/eclipse changes (MISS->PASS, the intended fix -- 07-15 hole-by-ruling + 07-16 present);
     ZERO false-clears (every healthy row stays PASS; etf genuinely-behind stays MISS under both).
     L3 BOTH-DIRECTIONS on the DEPLOYED lambda: inf-mirror dry_run=OK (fix live), etf dry_run=ALARM (no
     false-clear). Tomorrow's 15:45Z inf-twin runs the frontier predicate -- the false-Monday class is
     structurally dead for these rows.
3. **ECLIPSE HOLES-MANIFEST AMENDED_2** (CTO GO 164833Z condition 4, my authorship on 0.4.0_DS~B's
   landed evidence @ 4d085af8d; commit 6d6eba90d): residual FILLED-VIA-HISTORY-ARTIFACTS (55 keys under
   bronze/eclipse/_history/, event-history shape NOT snapshot time-travel); changed set corrected
   21->18 (union-vs-sum, created {1419,1420,1421} subset-of edited); model-static upgraded
   inference->vendor-surface grade (18/18 honest-zero auditlogs). Honest-holes + labeled-copies
   rejection explicitly PRESERVED. Synced additively to authoritative S3 holes.json (verified). ~B
   RAVC-closed on the SERVED object (condition 4 discharged; endpoints banner clause taken @ 31366663d).

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| build-derive-image.sh | dry-run then --go | SUCCEEDED | Dockerfile-COPY-derived zip (fail-safe), fedobs_observe.py fix verified pre-zip |
| deploy_ledger.py | 4 ledgers opened+closed (rebuild, bd-exporter, ztwin, frontier) | PASS | all legs proven; sentinels removed |
| terraform plan/safe-apply | 3 applies (bd-exporter 1/0/0, ztwin 2/0/0, frontier 0/1/0) all 0-diff after | PASS | each plan read at CTO's gate before apply |
| simulate-principal-policy | bd-exporter 22a suite (1 resource/call + isolated positive control) | allowed | + live get-role-policy for APPLIED truth |
| aws lambda invoke (dry_run) | frontier L3 both-directions on deployed lambda | OK + ALARM | pass-side AND alarm-side, no false-clear |
| ecs run-task (read-only) | fedobs image FIX_PRESENT check | exit 0 | runtime confirmation the rebuild baked the fix |
| local verify harness | OLD-vs-NEW per-row matrix (6 rows live) | 1 diff / 0 false-clear | the row-matrix CTO gated the frontier change on |

**What worked:** the per-row matrix turning a shared-instrument change into a verification not a demo
(the etf-behind row proving no detection was weakened); the breach-risk check before applying ~Z's
twins; runtime-verifying the rebuild rather than trusting the build log. **What I caught on myself:**
the wrong-namespace 0-datapoint false-breach (positive control caught it) -- third wrong-axis slip
today, each caught by a control. **Gap:** none open.

## MCP traffic
~12 in / ~10 out. In: CTO (bd-exporter route, sequence-by-care, 2x apply GO, frontier GO, D3-committed);
~Z (rebuild coord, P2-backout premise); ~B (manifest handoff + 2 RAVC closes); ~A (grant ACK). Out:
rebuild report (~Z); apply-gate plans x2 (CTO); grant verified-land (~A cc CTO); twins-healthy (~Z);
manifest authored (~B); frontier verified (CTO).

## Blockers
None. All apply-window motions closed. Staged-not-blocked: rps-row + WP8-DECOM cell 8 behind the decom
map-cells-4-5 ruling (CTO sequences).

## Current State (handoff surface)
- LIVE + verified: derive :latest sha256:174ac79f (fedobs fix); bd-exporter grant (bd-v2.52.0);
  code_heat_snap+fedobs_coverage_snap twins State=OK (globgrph-v0.1.19); frontier predicate on
  opal-assets-absence-check (opal-assets-absence-v0.2.0).
- All deploy ledgers CLOSED; all commits pushed (HEAD 4196b1468 + tags).
- Eclipse: catalog data/orion/api/ECLIPSE_API_V1_ENDPOINT_CATALOG.md + all 4 pointers landed; holes
  manifest AMENDED_2 on S3 + repo; verification circulation HELD for Andrew's word.

## Next Steps
- [04:30Z 2026-07-17] fedobs nightly -- first healthy coevolution served artifact ([0.8.0~Z] reads).
- [15:45Z 2026-07-17] inf-twin fire -- first run on the frontier predicate (expect OK, no false page).
- [22:00Z today] ETF AC3 cloud-guard verdict (FAIL re-enables laptop).
- [on CTO decom map-cells-4-5 ruling] rps absence-row + WP8-DECOM cell 8 revocations.
- [next natural box-up] boot-tail journal read (Residual B).
- [Andrew] Eclipse-verification circulation (cite 4c51b0a8b) -- on his word.
