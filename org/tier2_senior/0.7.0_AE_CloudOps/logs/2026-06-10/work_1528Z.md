# Session Log — 0.7.0_AE_CloudOps~B
**Date:** 2026-06-10T15:28Z
**Tick type:** substantive (R2c merge-cases + Andrew-premise deployed+invoked re-verify)

---

## (a) abort-MPU 4 merge-cases — APPLIED (COO GO, all 4)
GET-append-PUT-GET-verify, format-aware, existing rules preserved:
- inf [otp-prefix-expiry], portfolio [DeleteAfter90Days], schwab [ArchiveOldSchwabData], trade-submissions [ArchiveToGlacier] — each +abort-MPU 7d, existing-preserved=True verified.
- All 15 lacker buckets now have abort-MPU (11 zero-rule + 4 merge). Non-gated, no data moved.

## (b) Deployed+INVOKED re-verification (Andrew premise correction: Time Machine never operationalized)
CloudWatch Invocations 90d per grep-flagged consumer. **4 of 5 were the Time Machine trap:**
- bd: bd-time-machine 10/90d (test-level; portal-time-machine user-entry=0; capture writes 447 for never-wired feature) -> 36d floor VOID -> TIGHTEN CANDIDATE (confirms Andrew)
- portal-v2: yang-time-machine 0 -> DEAD -> TIGHTEN CANDIDATE
- portfolio: opal-portfolio-versions-list **136/90d** -> GENUINELY LIVE -> KEEP floor (only survivor)
- cot: gldrst one-time migration + seed in git -> TIGHTEN CANDIDATE w/ care
- mdpf: count-backfill one-time recovery -> TIGHTEN CANDIDATE
- portfolio 90d expiry downgraded: versioned=delete-marker, recoverable, intent-confirm only.

Doc addendum 6dc46d2f3. RAVC2-COMPLETE (152804Z).

## Banked memory (reference_s3_noncurrent_retention_can_back_live_feature)
(1) verify deployed+INVOKED (CloudWatch), not just grep, before honoring "noncurrent load-bearing" — Time Machine trap. (2) versioned + current Expiration = delete-marker (recoverable); check versioning before flagging Expiration as data-loss.

## Standing
R2c fully delivered (audit + abort-MPU all 15 + deployed+invoked reframe). Andrew noncurrent tighten go/no-go = post-overnight. Next: 02:00Z GLOBGRPH watch.
