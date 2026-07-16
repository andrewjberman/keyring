# 0.5.0_AE_OpalETL -- WP5, the Andrew P0, closed end-to-end in 52 minutes (2026-07-16 05:03-05:55Z)

**archetype:** MIXED (DEPLOY + IMPLEMENT + DIAGNOSE)

Andrew verbatim (CTO terminal ~04:5xZ, his record): "Need backfill first and incremental pulls
scheduled henceforth, make it so." Both clauses are LIVE. The arc, compressed:

## 1. The wsb feeder (model AUA)

- FRESH partition 2026-07-16 landed first (~05:08Z): 1a $1,406.4M/7,041 + 1c $23.3M/85 --
  three-instrument tie (memory anchors + my 07-14 name-map within 0.3%); registry keys
  corroborate the SMA name-map (opal_div_sma/opal_growth_sma).
- THE FORK: the API is SNAPSHOT-ONLY; --date is a label. REFUSED to stamp five past dates
  (fabricated vintages closing an incident born of silent drift). CTO: "your refusal to
  fabricate is the correct reading of 'backfill'" -> ruling (b) TRUE-VINTAGE for 07-14/15
  from my C5-landed monolith bronze (the SAME API responses at genuine vintages).
- The transform (deliverables/wp5_true_vintage_transform.py, CTO diff-reviewed BEFORE any run,
  R1 fix folded @ 71f1e68ad): derivation-not-fabrication, every input cited bucket/key/ETag
  incl. roster+registry shared_inputs, R3 tie-check derived-0715-vs-fresh-0716 GATES publish
  (worst drift 0.8922% <= 2%), hole manifest for 07-09/10/13. PUBLISHED: 7,111 + 7,125 row
  partitions + manifests w/ 14 cited inputs each. Feed: 07-08 -> holes -> 07-14/15/16.

## 2. The wsd feeder (partner_held_etf -- THE LD-0292 CLOSE ARTIFACT; CTO-discovered leg)

- Input surface = Schwab RPS silver (LANDED, DATED) -> backfill is NATIVE derivation.
- Fresh 07-16 partition: DIVZ $175.86M / total $522.5M -- ties the LD-0292 baselines exactly.
- Label-fill 07-09..15 x7 (CTO grounded it in the consumer's own contract-3.4 semantics:
  per-date lookups + in-row rps_date_used = the feed working, not the injected-column class).

## 3. The bridge (CTO 053211Z: the SI2 channel is SUPERSEDED by consolidation)

- Drop-check found BOTH channels empty since 20260706 (7 trading days) -- filed as the
  unresolved 07-07 silent-miss class recurring; CTO grounded the cure: the monolith puller
  lands the SAME CRS deliveries (DOUBLE-zipped; verified on real bytes before designing).
- Bridge: 75 files unzip->01_raw (+6 RPS mirrors), ETag census per file, idempotent,
  listing-verified. SCOPE FENCE: 0824 ONLY -- caught CTO's own parenthetical naming both
  masters (0833 into the 0824 tree = the never-summed sum by the back door); CTO: "you were
  right and my parenthetical was wrong -- owned." 0833 needs NO bridge (its pipeline reads
  monolith bronze directly).
- All 7 converters -> silver @ 20260714. ONE CATCH: the TRN converter reads the LOCAL
  OneDrive folder (not S3) -- first pass found nothing; fixed bridge-consistently (files
  placed locally, TRN OK=6, trn_nna OK=6). Sharpens the end-state re-point WP: THREE source
  styles exist across the seven converters.
- partner_held_etf re-ran 07-09..16: the window upgraded to TRUE PER-DATE custody
  (<=2-day roll; DIVZ 176.5 -> 177.2 -> 177.8 -> 177.3M genuinely daily).

## 4. The schedulers ("incremental pulls scheduled henceforth")

- Two sibling Lambdas (CTO d: bd READ isolated off the smartx role): vendored BYTE-IDENTICAL
  feeders + registry w/ parity-test drift gates; handlers add listing-verified landings; wsd's
  main()-verification promoted to RAISE form (a polite rc=1 cannot alarm).
- cron(30 3 ? * TUE-SAT *) UTC per CTO's consumer-read correction (his (c): day-D 03:30Z
  labels D before any D-dated mdpf lookup; my 22:30Z proposal mis-timed it -- accepted).
- Applied 20/0/0 (pure add, new-territory shape) + 0-diff textual; 22a BATTERY 14/14 incl.
  the CROSS-ROLE pair (wsb-denied-on-bd + wsd-denied-on-secrets; banked as the sibling-role
  standard) + Door-6 x2; trigger-map rows AT APPLY (census honesty) w/ the rider-ii holiday
  disclosure; tag mdpf-wp5-feeders-v1.0.0. First fires: 2026-07-17 03:30Z.

## Open at close

- [bg] canonical 20260714 build running (skill 7.5 tail) -- completion evidence follows.
- [CTO] task 14 remaining cells (FE read + mdpf re-read); WP6 shape + the converter re-point
  WP paragraph owed by me next.
- [queued, my lane] smartx-assets-daily-pull artifact swap (deployed sha predates the
  e5855aad0 filter gate) at CTO's gate; 0.7.0 wiring the C5 schedule off my contract.
- [0.6.2-at-revival] SI2 legacy decommission + silent-miss post-mortem (demoted).

## Compiler Tools

comp-glob (feeder locate) + comp-pulse (auto x7, all measured-clean). Raw-aws = operational
(feeder runs, bridge, battery, apply verifies) + 3 rail-checked inventory listings (date-set
denominators, not freshness verdicts). Standing gap: no comp-tool covers the monolith
smartx/schwab feeder surfaces (fifth consecutive log).

## MCP traffic

In: CTO x7 (P0 dispatch, rulings x3 waves, R4 PASS-with-fix, bridge GO, apply GO), 0.7.0 x1
(C5 contract ask -- answered grounded on live config + the drift flag). Out: 12 (ACKs,
evidence bundles, the C5 invocation contract, DS/MSTR notifies). Every loop closed except
the canonical-build tail.
