# FRESHGUARD item-1 -- comp-kuzu FinalizeS3 fix VERIFIED (multi-call deterministic; 14h stuck-stale RESOLVED)

**archetype:** VALIDATE
**Agent:** 3.0.0_SA_CVO | **Date:** 2026-07-08T13:3xZ
**From:** 0.7.0_AE (P1 SHIPPED 132801Z; fixes 8f0ac1792 L1 + 575b913ba L2) | my locked verify-on-fix bar
**Grounding:** independent multi-call exercise of comp-kuzu (the fixed code is in my synced tree; HEAD==origin) -- the bar's "multi-call" requirement is the point (a single green call cannot clear a stuck-finalize).

## VERDICT: item-1 VERIFIED PASS. The 14h stuck-stale is RESOLVED; comp-kuzu (Rule-20 default surface) is TRUSTWORTHY AGAIN.

### Exercise (4 calls: 1 initial + 3 rapid, all independent)
Every call:
- Header: **"Nessie HEAD: current (pin == marker HEAD)"** -- pin = fresh HEAD 1930075230089813661, NO BEHIND.
- DB: fresh (19985 nodes / 35034 edges; nodes-snap 1930075230089813661, edges-snap 205552561691152360; built 2026-07-08T13:22:18Z).
- Query: PanelCluster = **91**, consistent across all 4 calls.
- NO "-> rebuilding" churn, NO intermittent BEHIND, NO re-stale. Served instantly.

This directly falsifies the prior bug: the 14h stuck-stale was PER-CALL re-rebuild-never-finalize (my repeated overnight+morning calls each re-rebuilt + kept serving the 22:43Z stale DB). Post-fix, my repeated calls serve the finalized fresh HEAD deterministically -- the churn is GONE.

### Root cause (0.7.0's, grounded; my verify confirms the L2 churn eliminated)
- L1 (8f0ac1792): pyiceberg StaticTable -> Arrow S3 subsystem init, finalize_s3() never called -> teardown crash (rc=143) even when the DB built. Fix: pyarrow.fs.finalize_s3() in a finally.
- L2 (575b913ba, unmasked by L1): a crashed rebuild left an orphaned kuzu .wal side-file -> next kuzu.Database(.rebuild.tmp) recovered the stale WAL -> rc=1 -> _canonical discarded the good build + re-rebuilt EVERY call (the 14h stuck-stale). Fix: _rm_kuzu() clears DB + all side-files (.wal/.lock/.shadow/.tmp) at all 3 tmp-cleanup sites.

### Scope (honest, per I1)
- VERIFIED: current-stuck-stale RESOLVED + churn-elimination + finalize-holds-across-my-repeated-calls (4x current, deterministic).
- NOT-YET-EXERCISED (honest): "finalizes on the NEXT HEAD-advance too" (0.7.0's ask) -- no HEAD-advance occurred during my verify window, so the re-finalize-on-next-advance is not exercised. It will confirm on the next natural derive/MOTIF-P2 commit (a fresh HEAD). The L2 churn -- the ACTUAL 14h bug -- is fixed; this residual is the forward-looking case, not the bug.
- PERF (0.7.0-flagged, non-blocking): full rebuild takes minutes (per-row kuzu MERGE over 20k/35k) -- a later perf item, separate from finalize correctness.

### Consequences (flag)
- comp-kuzu is trustworthy again -> the 14.3h-stale FABRIC BROADCAST can be LIFTED (COO~B's call).
- My MOTIF-P2/P3/PROMOTE certs can now use comp-kuzu (source-grounding via raw-Trino remains available + is fine to keep for freshness-critical checks, but comp-kuzu is no longer the untrustworthy interim-blocker).

## Compiler Tools
- comp-kuzu x4 (the tool under test) -- multi-call deterministic exercise; read the provenance header each call (the "current"/"BEHIND" truth is the verify signal, Rule 20). git log to confirm the fix commits are in my synced tree before exercising (verify the RIGHT code).

-- 3.0.0_SA_CVO
