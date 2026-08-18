# Deploy Completion — Cottonwood MDPF trio: staged → SERVED publish (json/mdpf/cottonwood/*)

**Status:** CLOSED 2026-07-23T~01:33Z (COMPLETE, content-verified; amendments 0405Z + 1202Z closed in-doc)
<!-- scanner-alignment line added 2026-08-18 by 0.0.0_AB_MSTR (RED-disposition act, org/tier0_exec/0.0.0_AB_MSTR/deliverables/DEPLOY_LEDGER_RED_DISPOSITIONS_20260818.md): mirrors this file's own close declaration below; deploy_ledger.py's unindexed scanner could not read the original form (defects A/B/shape-C, see the disposition doc). Not a new closure. -->

**Ledger opened:** 2026-07-23T~01:32Z (publish-start) · **Closed:** 2026-07-23T~01:33Z (COMPLETE, content-verified)
**Agent:** 0.4.0_DS_ClientPlatform (executor)
**Authorization chain (each half independently citable):**
- Andrew-direct override, 01:0xZ at CTO's terminal (verbatim in CTO 011006Z/011206Z; verified via
  confirm loop — CTO responsive ACK 011248Z + live-summary correction same minute).
- **CTO co-sign** 012337Z — ETag-pinned, conditions verified (identities PASS + DE green).
- **COO counter-sign** 013145Z — identities INDEPENDENTLY recomputed on the staged artifacts
  (model+non_model==total to the cent; count-axis 294 DISTINCT not the 442 sum — the S5-rollback
  class checked explicitly; by_model == PRD §1.2 to the dollar). One-flip reconciliation owned
  CTO+COO jointly as a scoped Andrew amendment of LD-0330 (legacy-family serve ahead of the revamp
  flip; revamp flip + gates untouched).

## What published (additive new-firm keys; no existing served output moved; no CF/TF change)

| Served key (opal-data-portal-v2) | Bytes | ETag (== staged pin, byte-identical) |
|---|---|---|
| json/mdpf/cottonwood/account-distribution.json | 6,269 | 67f32c56e6f76016c2b97bacb641b647 |
| json/mdpf/cottonwood/aum-metrics.json | 2,872 | 2ea36da99b3c9c1ca7f3a619aa00c071 |
| json/mdpf/cottonwood/aggregate-aua-timeseries.json | 39,154 | 7dfc132287ba1cbdd93050af109458fc |

**Verification per object:** pre-publish MD5 == co-signed pin asserted; post-publish fresh GET
byte-compare == source; ListObjectsV2 key+Size confirm. Naming = the live 49f/inflection serving
convention (hyphenated; their daily serving is the positive control on the path).

## Named conditions (from the co-sign, on the record)
1. Trend serves HONEST-ABSENT tonight (zero axis overlap); populates on the axis advance.
   **Must-resolve (COO→CTO, not a publish blocker): the nightly dispatcher has NO Cottonwood leg**
   — without the 6d wiring the trend stays empty tomorrow.
2. comp-validate NO_CONFIG — publish rests on the EXERCISED identities (verified by both signers);
   config authoring = DS follow-up debt, logged.
3. 294 (served model-participating accounts) vs 296 (bridge denominator) = two different
   quantities; reconciliation note = DS follow-up, not a defect.
4. Income treatment divergence pair-vs-trend (both meta-flagged) — harmonization rides CTO's
   canonical-key ruling (daylight).

## AMENDMENT — canonical re-emit REPUBLISH (0405Z, same ledger, superseding ETags)

**Authorization:** Andrew-direct 0351Z ("I need both right now immediately") -> CTO 035108Z order +
pre-signed half (5->4 count-condition SUPERSEDED by Andrew's direct "Yeah there's 5 models" via COO
0400Z) -> COO counter-sign 040340Z (independently verified: identities to the cent, 294-not-442,
5 CANONICAL keys, Income residual, ETag match, pending EMPTY).

| Served key | Bytes | New ETag (pin-verified, byte-compared) |
|---|---|---|
| account-distribution.json | 6,375 | 1b283841dd19d255fff22fb19e29775c |
| aum-metrics.json | 2,862 | 55b1f1a48e0089ec081798683ecca110 |
| aggregate-aua-timeseries.json | 35,311 | 3e555439135e43ff041615ef029cbc71 |

Content change: CG -> opal_long_term_conservative (display "Long Term"), Income out of trend
by_model into the named residual, pending_canonical_ruling EMPTY, canonical_merge authority in meta.
Numbers unchanged from the co-signed 0133Z publish (same partitions pinned). Producer @ab1f0074b.
04:00Z conditioned trend leg: pre-flight AXIS STALE -> correctly did not fire (COO concurs 040340Z).

## AMENDMENT 2 — INTERPOLATED BAND SERVED (1202Z, CTO serve-GO 120047Z)

**Authorization:** Andrew's band serve-word (050247Z via COO) → CVO 5-point cleared incl. mutant-d
→ COO counter-sign green (value limb byte-verified: early band $454K not $105M, ramp lands on
served $124.4M) → CTO gate fired 120047Z. Both notes closed (07-14 staircase = conscious-accept,
three-way converged; weekend wobble = DE trading-day x-axis @58a38078, render-not-data).

| Served key | Bytes | ETag (== staged pin, byte-compared) |
|---|---|---|
| json/mdpf/cottonwood/aggregate-aua-timeseries.json | 66,710 | 3c3879c0df26656150d4b0629da393ad |

Content: the measured-epsilon band (ε=0.10, bimodal-valley-measured, M6-pinned) — early band =
the 2 genuine accounts, onboarding staircase at real bronze createdAt steps, custody continuous,
$2.25B/5,473 acct-dates suppressed (denominator lands in-bytes on the next emit per NB-1
@e216b2b86). Supersedes the honest-absent trend served 0405Z. 3 re-emits, 5 byte-reads, 2
serve-defect catches preceded this publish; 19/19 mutants at @9ffa3ca6e lineage. DE live-render
verification follows.
