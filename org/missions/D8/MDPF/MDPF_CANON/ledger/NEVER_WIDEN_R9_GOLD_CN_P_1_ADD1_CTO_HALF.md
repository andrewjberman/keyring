# NEVER-WIDEN -- CTO half: ADDENDUM 1 to the round-9 CN-p-1 pair, the one-time publish of the Trend groups onto the as-of 2026-10-13 objects (`1.0.0_SA_CTO~DELL1`, 2026-10-14 ~23:0xZ)

**Signs these bytes:** `org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round9/NEVER_WIDEN_PAIR_R9_CN_P_1_ADDENDUM_1_PUBLISH_TONIGHT.md`
@`1e52755b27`, **sha256 `02b24fb33327a6e3c563050870a32afaf5414287c1a672a2d07ac93dd722b3d7`** (equal on disk at signing). Other bytes re-open this
half. Authority: Andrew-direct ~22:5xZ, "do it" (record @44eac4d919), and ~22:5xZ: "currently we're displaying a broken graph on the trend view on
PROD so better to just try and overwrite than leave this shit up". Pure ASCII.

## What I read

| claim | read | result |
|---|---|---|
| The CN-p-1 deploy is done | `lambda get-function-configuration mdpf-gold-lambda` | CodeSha256 `AEUuWyiM...7kM=`, LastModified 2026-10-14T22:49:55Z, `MDPF_GOLD_COMMIT` `8e2dd0fb36...` = the pin |
| The Global key is still at the baseline | `s3api head-object` `portal/gold/mdpf/global/aggregate-aua-timeseries/2026-10-13.json` | VersionId `VfcEmemcvHWpldKQD3tCsfhgxwAkOkT.` = section 2 prior |
| The lambda cannot overwrite | addendum section 1 (`conditional_put` read at the pin) | accepted: a re-run would log conflicts AND move the CN-h-1 counts early, so a splice is the narrower act |

## Ruling and why it is signed

- **The writer is a one-time splice, not a pipeline.** The CloudOps `put_object` writes eight bodies that equal the existing bodies plus exactly
  the CN-p-1 keys, and the builder refuses any other difference. Every body round-trips byte-equal through the producer's serializer. It is one act
  on Andrew's explicit word. It is not a standing writer, and it is not a shadow pipeline: the scheduled lambda remains the only producer, from the
  2026-10-15 fire on.
- **N, printed:** the Trend keys on these eight gold objects have 1 writer tonight (the splice); the served copies have 1 writer (the publisher, its
  existing path).
- **Both branches and every failure** are covered by section 3. The rollback is per key: copy the prior VersionId back, read the sha256 back, never
  a delete.

## Conditions

- **C1, provenance carries its claim.** The spliced objects keep the 2026-10-13 run's `_provenance`. The addendum record and the order's receipt
  are the claim that the Trend keys were spliced, not produced. The order's receipt cites this half and the addendum by commit. Tonight's objects
  are never cited as evidence of the lambda (section 1, accepted).
- **C2, nothing else moves.** The before-print reads all eight prior VersionIds unchanged, or the order STOPS. The publisher reports exactly the
  eight pairs `published` and every other pair `unchanged`. A ninth `published` is Branch B: restore that key by its prior version.
- **C3, PROD visibility is not claimed.** Tonight's publish changes nothing a PROD page draws until CN-p-2 lands (section 2). Andrew was asked
  whether CN-p-2 may go to PROD tonight without his smoke. That push is client-facing and is not covered by this half.

## SIGNED -- CTO half GIVEN

```
NEVER#1   "never move served output without never-widen sign-off (CTO+COO)"
ACT       ONE splice: CloudOps put_object of 8 builder bodies onto the as-of 2026-10-13 gold keys + ONE publisher hand-run
MOVES     4 Trend keys on 4 timeseries (Global values; firms all-None/[]); Global meta.trend_groups; "muni" ($0.00) off 4 category-views
CANNOT    every other key of the 8 bodies; counts (stay at the 10-15 fire); aum-metrics; account-distribution; parquet; staged objects
ROLLBACK  per key: copy-object of the recorded prior VersionId (section 2), sha256 read back; never a delete
BINDS     addendum sha256 02b24fb3...b3d7 @1e52755b27
CONDS     C1 provenance stated, not evidence; C2 8 prior VersionIds unchanged + exactly 8 published; C3 no PROD-visibility claim
COO half  2.0.0_SA_COO~D1, GIVEN
CTO half  1.0.0_SA_CTO~DELL1, GIVEN 2026-10-14 ~23:0xZ
```

-- 1.0.0_SA_CTO~DELL1

## AMENDMENT 1 (~23:08Z) -- C2 restated on the publisher's measured behaviour (`0.7.0_AE_CloudOps~DELL1` msg 5955)

**Measured by the CloudOps seat:** the publisher's role is denied `GetObject` on `latest.json`, so its `unchanged` branch never fires. Its last three
runs (10-13 13:50Z, 10-14 13:50Z, 10-14 16:34Z) each reported `published 18, unchanged 0`. A hand-run tonight therefore re-publishes all 18 pairs:
the 8 targets and 10 others. The 10 carry identical data; only `_provenance.written_at` moves, as on every daily run.

**C2 now reads:** the before-print reads the eight prior VersionIds unchanged. After the publisher run, for EVERY served pair, compare the data hash
of the body with `_provenance.written_at` excluded, old against new:
- exactly the 8 target pairs differ, and each equals its built body;
- the other 10 are data-identical.
Any data difference on a ninth pair is Branch B: restore that key by its prior version. The 18-of-18 `published` count is expected and is not
Branch B. Everything else in this half is unchanged.

**Defect noted, not fixed tonight:** the publisher's missing `GetObject` on `latest.json` turns every run into a full republish. It goes to
`2.0.0_SA_COO~D1` as an enrichment for the next MDPF_CANON round analysis.

-- 1.0.0_SA_CTO~DELL1
