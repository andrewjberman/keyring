# CVO Cert — cot Lever A Belt CLOSE (both limbs independently grounded) — my last Lever-A item

**Date:** 2026-07-07T02:10Z
**Agent:** 3.0.0_SA_CVO
**Subject:** Cottonwood (cot) Lever A — cookie-first daily-OTP skip — belt on the NATURAL 02:00Z daily
**Verdict:** PASS — belt CLOSED. Firm-separated (cot tree only; zero bd cross-reference). 2 WARNs adjudicated NOT-Lever-A.

## LIMB 1 — SKIP-NOT-MINT (I pulled the cot session-trigger CloudWatch myself, /aws/lambda/cot-bd-session-trigger, 02:00-02:15Z via PowerShell)
```
Lever A: cot cookie POSITIVE-live (probe positive (captured_at=2026-07-06T02:02:47.724Z)) -> SKIP OIDC-login mint, direct bronze-run
Mode marker written: s3://opal-data-cot/blackdiamond/cot/session-trigger-mode.json mode=bronze-run
SSM RunCommand sent: 071b3558-4a4d-46fa-aafd-3010968bff0a document=opal-cot-bronze-run attempt=1
```
- ~24h-old cookie (captured 2026-07-06T02:02:47Z) still POSITIVE-live at 2026-07-07T02:00:14Z -> SKIP OIDC-login mint. ZERO OIDC-login/OTP. The redundant cot daily-OTP is DEAD on the natural cron.
- Firm-separation: mode marker -> opal-data-cot; SSM -> opal-cot-bronze-run (NOT opal-cot-bd-session-fetch). Correctly cot-bound. ("cot-bd-session-trigger" = the Black-Diamond-PLATFORM session-trigger for the cot firm; bd=platform not the bd/49F firm.)

## LIMB 2 — ALL-4-FRESH via the skip path (head-object UTC, opal-data-cot)
| table | forwardfill_v2 07-07 LastModified (UTC) |
|---|---|
| transactions | 02:01:41Z |
| allocations | 02:01:14Z |
| realized | 02:01:27Z |
| unrealized | 02:01:47Z |
Sentinel bronze/2026-07-07/_BRONZE_COMPLETE.json @02:01:46Z: overall=success, tables=[allocations,realized,transactions,unrealized], count=4, producer=cot_bronze_ingest.py (firm-correct name in the cot bucket). All in the 02:00Z window -> the SKIP-path runner did a REAL fresh pull, zero OTP. (comp-freshness cot_silver_{4} PASS, mtime 02:02Z -- chain advanced bronze->silver via skip.)

## WARN adjudication (both downstream/pre-existing, NOT Lever-A -- Lever A skips only OIDC-login; bronze/silver ran normally + fresh)
1. HOLDINGS-REJECT: holdings 07-07 NOT landed (head-object 404; prior snapshot held). Cause = deliberate data-quality gate ("non-zero-MV 0.0% < 50% floor, prices UNPOPULATED"). Fires on price-population, INDEPENDENT of auth -> would fire identically on a mint run. => NOT Lever-A. Real pre-existing cot holdings-prices item (cot_silver_holdings 72h-stale, as_of 07-03) -> track separately.
2. PLATINUM CONTENT-STALE: cot_platinum_{timeseries_overview,header_metrics,timeseries_chart} MTIME-fresh (02:03Z) but CONTENT as_of 07-02 (2td behind 07-07). Gold-stage content-lag; gold reads the FRESH 07-06 silver -> NOT a skip-path regression. => NOT Lever-A. Client-facing served content-staleness (2td) -> separate investigate-item (route to cot-gold owner; possible link to the holdings-reject gating gold, but content 07-02 predates holdings 07-03, so a distinct gold lag).

## Verdict
cot Lever A belt = PASS, CLOSED. Skip-not-mint (zero OTP) + all-4-fresh-via-skip (real pull) -- Andrew's BD/cot-auth thesis PROVEN in production for cot (long-lived cookie -> direct pull, OTP only on stale). Completes tonight's Lever-A work: 49F + cot BOTH certified. The 2 WARNs are Lever-A-orthogonal (data-quality + gold-stage), tracked as separate items -- NOT a Lever-A rollback. The platinum content-lag warrants a CVO-flagged separate look (client-facing 2td staleness).
