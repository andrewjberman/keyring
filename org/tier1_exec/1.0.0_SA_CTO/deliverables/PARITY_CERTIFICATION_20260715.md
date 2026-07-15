# ALL-CHANNEL BRONZE/SILVER PARITY CERTIFICATION + TRIGGER-CONFIRMATION MATRIX

**Status: DRAFT — ASSEMBLING; completes at tonight's 22:00Z fire-read (two cells remain, both
mechanism-gated on tonight's artifacts). NOT YET CERTIFIED.**
**Certifying officer:** 1.0.0_SA_CTO. **Directive:** Andrew-direct 2026-07-14 ~18:5xZ (verbatim in
log 1d0f11228): ad-hoc drain every silver converter to bronze/silver parity + confirm scheduled-
ingest & silver-event triggers; certification flips OPAL_RUNNERS (now OPAL_CONSOLIDATION WS-C) to
FULL-RESOURCE. **Cert form:** (b) named-residual per the COO-conditions (163806Z, adopted as ACs):
residuals orion-pattern-explicit; the residual line rides IN the Andrew ping; no window-sprint.

---

## 1. Channel parity legs (6/6 CLOSED as of 18:35Z — every leg verified by the certifying officer's
own instruments, never a producer self-report)

| Leg | Silver/Denom | Closed | The verifying evidence (mine) |
|---|---|---|---|
| eclipse | 192/192 | 07-14 18:59Z | manifest 20260714T185950Z-e32751de; DS pins 4/4; 16:00Z int64-refusal HEALED under v0.10.0 |
| blackdiamond/cottonwood | 506/506 (+fwd dailies) | 07-14 | 506/506 census + 6 forward-motion dailies |
| schwab 0824 | 7,482 (shortfall_post=0) | 07-15 12:58Z | sweep manifest 20260715T122659Z: self-certifying zeros; +14 forward motion over the 7,468 backfill denom |
| orion | 4,640/4,640 | 07-15 16:35Z | FOUR-LEGGED: 0.7.0 drain 58/58 + independent sweep set-identity PASS (20260715T163036Z-d169038f: matched=4640, missing=[], alien=[], holes=0) + DS 1.39M content pin w/ streaming row-group provenance + MY listing 4,640 w/ no-shell byte-tie (min 27,183,918B both instruments) |
| schwab 0833 | 8,452 listed / 8,436 target (shortfall_post=0) | 07-15 18:30Z | sweep manifest 20260715T181504Z-64a7e1f5 read by my hand: shortfall_pre 344 -> post 0, surplus 0, collisions 0, ok:true; MY listing 8,452 == manifest silver_keys EXACT; holes_named=[tcf,tcfx,tnn] (delta-7 registered absences, manifest-visible, NOT shortfall); sampled per_type T1_RECONCILED |
| etf (bronze leg) | 4/4 vendor keys @ 20260715 | 07-15 18:34Z | **C4 AC1 CLOSED on the Andrew-NOW manual fire:** MY ListObjectsV2 ties producer attestation byte-exact (462,322+252,697+543+14,305 = 729,867B); TS_PATTERNS both funds, as_of 07-14 = T-1 correct; Q2 conservation ties in-file (85+23=108==delivered); **first monolith ETF bronze is REAL** |

## 2. The two OPEN cells (mechanism-gated on tonight — NOT calendar-deferred)

| Cell | Gate | Lands |
|---|---|---|
| ETF day-3 parity verdict | needs tonight's laptop-leg 07-15 artifact (2/3 GREEN at 18:32Z — 07-13 + 07-14 both 52-fields-0-mismatch; the 2/3 REFUSAL is the threshold working) | ~22:00-22:15Z |
| ETF SCHEDULED-trigger leg | tonight's 22:00Z scheduled fire on the SAME deployed v1.1.0 (live sha 40KaO/7j re-verified pre-manual-fire; the manual fire supplies the CODE-PATH proof, the scheduled fire supplies the TRIGGER proof — two data points by design, Andrew's NOW order + the standing schedule) | 22:00Z; evidence = refreshed LastModified >= 21:55Z + invocation log (never key-existence — same-key rewrite hazard self-caught by 0.5.0) |

## 3. Trigger-confirmation matrix (as of 18:35Z)

| Channel | Scheduled ingest | Silver event trigger | Basis |
|---|---|---|---|
| schwab (both masters) | CONFIRMED — real multi-file daily delivery converted live 07-15 (0824:11 / 0833:13) | CONFIRMED end-to-end (~10s, Andrew's event-trigger leg 07-14) + delta-7 EXERCISED on the deployed artifact + exact incident key (skipped_holes=[tnn], 0 DLQ) | exercised evidence, both paths |
| bd49f | CONFIRMED — 02:30Z daily fire served-verified 3/3 (07-15) | n/a (pull vehicle) | exercised |
| eclipse | sweep = the live mechanism (INF raw producer HELD) | event path CANNOT fire on new bronze under the hold — honest edge, **LIVE-GROUNDED** | **frontier check COMPLETE (0.6.2 @ 195653e85, Andrew-dispatched, read-only):** mirror ENABLED + 07-15 2 invocations/0 errors + exact set parity dst==src (4,640/4,640 gz; 624/624); trading-day frontier = 3 (calendar-resolved, NEVER#1); causal mechanism GROUNDED on the census discriminator — raw .gz stops 07-10 in ALL types while parquet runs to 07-15 in the SAME prefixes, a signature no dead schedule can produce + the hold doc Door-5 cites. **The something-is-broken hypothesis is REFUTED; the frontier IS the hold working.** Nothing INFERRED. |
| orion | same honest edge as eclipse; sweep exercised TODAY at scale (the 58-unit drain + set-identity sweep) | same | same artifact (all four orion types in the discriminator census) |
| etf | manual fire = code-path CONFIRMED (sec-1); scheduled leg TONIGHT (sec-2) | event rules registered (silver container); exercise rides first conversions | issuer-route-only per Andrew 18:2xZ (msn STRUCK) |
| smartx | ad-hoc-pull feeds, latest-available, NO scheduler yet — manifested honestly; TF event-rule note routed to 0.7.0 at wiring time | conversions run driver-side (v28); container events at wiring | honest state, not pretended |

## 4. Named residuals (per cert-AC (i): denominators + close conditions; NONE block the cert)

1. **smartx part-2 build wave** (6 ruled-FACT tables, 0 of 6 landed at draft time; wave EXECUTING
   under batch GO w/ halt-on-refuse; DS pins filed @ a289cc2fe, library PASS @ 6ce907696).
   Close: per-family landed read-back == DS pin. The RULING half of Andrew's
   table-or-exemption bar is fully satisfied (6 FACT + 1 exemption + meta exempt-by-construction);
   this residual is BUILD EXECUTION only. **This cert cannot be read as "smartx complete."**
2. **cell-3 floor-parser** (bd49f pull; inert-not-wrong, extent 92 > measured 70 floor): fix
   STAGED (plan 0/1/0, live sha unchanged); swap gates on tonight-clean; runtime-confirm rides
   tomorrow's 02:30Z fire.
3. **msn code strike** (issuer-route-only ruling): deployed v1.1.0 untouched until after tonight's
   scheduled fire (the certified artifact IS the firing artifact); strike rides my artifact-swap
   gate after.
4. **orion memory resize 10240->3008** (cost trim, correctness-neutral): double-grounded (runtime
   1,131 MB); rides 0.7.0's post-22:00Z batch.
5. **schwab CRS one-motion** (swap + resize): GO'd 18:30Z post-0833-read; AC-1 heaviest-unit
   runtime number pending — also canonical-stamp leg (ii) for the chunking pattern.

## 5. Standing holds — UNTOUCHED by this certification (the cert asserts nothing about them)

INF chain hold (Door 5/6, frozen-3, stamp order) · 0824/0833 NEVER-SUMMED (this doc lists the two
masters as SEPARATE legs and computes no combined total) · bronze-raw/17a · vendor egress.

## 6. What certification releases (ON COMPLETION — not yet)

OPAL_CONSOLIDATION WS-C (the RUNNERS scope) flips to FULL-RESOURCE per the standing Andrew gate
(~18:5xZ 07-14). The S2 architecture lock (ff6ae74d8 + 5dc153178) means the full-resource wave has
its architecture, box (TF @ 5fc641654, apply gate tomorrow AM), dims (D1 v1.1 LIVE), and dictionary
already in place — the flip releases BUILD EXECUTION, not design.

---
*Draft assembled 18:3xZ 07-15. Completion + certification + the Andrew PushNotification occur at
fire-read (~22:05-22:20Z) provided sec-2's two cells read clean; any FAIL branch holds the cert and
escalates instead.*
