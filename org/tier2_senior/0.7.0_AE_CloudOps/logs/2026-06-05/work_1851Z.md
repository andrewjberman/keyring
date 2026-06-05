# work-cycle 0014 — INF_D_04 geo regen+publish (DS RUN-NOW, Andrew-direct) + MDPF CDN-flush correction

**archetype:** DEPLOY (trigger/publish) **secondary:** DIAGNOSE, VALIDATE
**Date:** 2026-06-05 ~1842-1851Z
**Trigger:** DS 0.4.0 RUN-NOW COORD 184229Z (Andrew-direct, run-on-deploy) — served ADVI Inflection Segment Analytics geo P10 stuck $8.42; I3 fix DEPLOYED but served platinum not regenerated (publish gap, same class as MDPF_COUNTS).

## INF_D_04 geo publish — DONE + verified
Pre-flight (stale-deployed discipline): deployed s3://opal-data-inf/code/gold/INF_D_04.client_portal_summary.py (13:12Z, 205KB) sha **95c5833b == repo HEAD**, carries MDLP_DISTFIX I3 (line 55 imports floored_percentiles; _build_geo_view -> floored_distribution_stats >=$1K). floored_percentiles.py dep deployed alongside.

Ran: started inf-gold-layer-runner i-0ed5afded2ebd4 -> SSM `bash orion-gold-dispatch.sh --single INF_D_04` (canonical single-script path; syncs scripts itself; SKIP_EXISTING=0 default = no marker-skip; OUTPUT_PREFIX=platinum/ PROD; --upload). RC=0, wall 25.4s. Runner AUTO-SHUTDOWN (2min self-stop) — right-sized, single script NOT the chain, cost-clean.

VERIFIED served s3://opal-data-inf/platinum/firm/partner_analytics_monthly.json (18:48:39Z) views.geo.{w}.distribution.total:
- current: min $1,052.42 / p10 **$11,729.60** / p25 $36,869.62 / p50 $106,531.29 / p75 $310,590.92 / p90 $733,522.72
- m1 p10 $11,760.09 / m2 $11,849.57 / m3 $10,951.73 (all min ~$1,04x)
P10 flipped $8.42 -> $11,729.60 EXACTLY per DS's recompute proof; all 4 windows floored to >=$1K. quarterly/annual rewritten same run.

## MDPF_COUNTS CloudFront CORRECTION (self-caught — verify-the-actual-path)
My earlier MDPF flush hit E398SP0DG1ME0Y for /api/general/mdpf/* — but E398 serves only /v1/*,/metadata/*,/auth/* (NOT /api/general/*). The dist serving /api/general/* AND /api/scoped/advisor-intelligence/* is **EVTSA9VEHNZVH** (opalinvest.dev portal dist; confirmed via get-distribution-config behaviors). So that flush was an ineffective NO-OP — same class as the yield-curve wrong-path incident. The S3 counts artifacts were correct the whole time (account_count verified 18:37Z); only the CDN flush was misrouted. RE-FLUSHED /api/general/mdpf/* on EVTSA9VEHNZVH (combined with the ADVI path, inv I8CCWQF1NCHBVX3AA7WR68D0KC).

## CloudFront (both on correct dist EVTSA9VEHNZVH)
inv I8CCWQF1NCHBVX3AA7WR68D0KC: /api/scoped/advisor-intelligence/* + /api/general/mdpf/*.

## Routing
DS pinged (verify served + relay CTO->Andrew). COO notified (correction + INF_D_04 done). Runner self-stopped (confirmed `stopped`).

## Lesson banked
Always confirm a dist's path-patterns (get-distribution-config CacheBehaviors) BEFORE invalidating — a path on the wrong dist silently no-ops. Pairs with the yield-curve FE-path-vs-S3-key lesson.

## Compiler tools
sha byte-verify deployed-vs-HEAD, SSM send-command/get-command-invocation, s3api head-object + content verify, cloudfront get-distribution-config (behavior audit) + create-invalidation (PowerShell, leading-slash paths).
