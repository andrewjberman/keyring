# FIND_INSURE.023 — serving-consolidate empirical run (W3 structural close)

| | |
|---|---|
| **Agent** | 0.1.0_DS_MarketIntelligence~E |
| **Date** | 2026-05-28T~14:13Z |
| **TO** | FIND_INSURE.023 (serving-consolidate W3) |
| **Trigger** | RESPAWN GO — `.008` AC7 cleared (Phase 1 closed `d2033738c`); HARD INPUT blocking DS~C `.024` Phase-2A |
| **Result** | DONE — 99/99 consolidated, `serving/scoring.json` + history uploaded to S3, round-trip verified |

## What ran

`python data/find/imo/scripts/serving/consolidate_scoring.py --root <local> --run-date 2026-05-27`
→ `OK: consolidated 99 IMOs (scored=99 blocked=0 no_pages=0)`

The script is a LocalStorage skeleton (boto3 wiring deferred to AE build-moment), so the
empirical run was executed as: pull gold score.json from S3 → local-fs root → run → upload
serving outputs to S3. Authorized by respawn GO ("via consolidate_scoring.py --root; upload").

## Roster provenance (the 99)

- Canonical universe = `s3://opal-data-imo/serving/_meta/source-list-2026-05-27.json` (`imo_count: 99`).
- S3 had **100** `corp/{slug}/gold/web-scrape/2026-05-27/score.json` files. Derived slugs from the
  99 source-list `company_name`s → matched **exactly** 99 of the 100 S3 slugs. The single stray was
  `carl-ostenson` (a 362-byte dup variant of the real roster member `carl-ostenson-associates`).
- Excluded `carl-ostenson` before the run so `list_slugs()` returned exactly the canonical 99.
  (The skeleton derives its roster from corp/ dirs present on disk, so roster control = download control.)

## run_date discipline

Pinned `--run-date 2026-05-27` per respawn — did NOT default to wall-clock 2026-05-28. This is the
exact date-partition footgun I caught earlier (logged `work_1238Z`); the empty 2026-05-28 partition
would have produced a false NO_PAGES universe. (That footgun is being hardened structurally under
FIND_INSURE.037, assigned to DS base.)

## Output (verified, then round-tripped from S3)

```
schema_version: v0.2          run_date: 2026-05-27
taxonomy_version: v3          scoring_weights_version: v0.3   mixed_warning: False
universe_size: 99   scored: 99   blocked: 0   no_pages: 0
ranked_companies: 99   ranks contiguous 1..99: True
wm_classification_distribution: {present: 7, adjacent: 17, absent: 75, null: 0}
wm_drift_warning: NONE        SCORED w/ null am_prominence: NONE
```

- `taxonomy v3 / weights v0.3` consistent across all 99 → confirms these are v0.7.3 gold outputs
  (post AE env-pin fix `cb07bb8a8`), not stale v1/v0.1. No mixed-version warning.
- 78 serving unit tests PASS pre-run (code-health gate).

Uploaded (overwrite-in-place + append-by-date), both 128861 bytes, S3 round-trip parse OK:
- `s3://opal-data-imo/serving/scoring.json`
- `s3://opal-data-imo/serving/_history/scoring/2026-05-27.json`

## FLAG (non-blocking) — rank key vs v0.7.3 decision driver

Ranking sorts by `rollup_score` desc (design §4, written pre-v0.7.3 and NOT updated by the §0
v0.7.3 read-contract addendum). But v0.7.3 made **`am_prominence`** the decision driver
(`class_diversity` retired). Consequence in the live table: the top 3 are high-volume / low-amp
**adjacent** IMOs (allianz-life amp=0.0117 #1, eagle-strategies amp=0.0327 #2,
senior-market-sales amp=0.3443 #3), while the 4 **present**-class IMOs (amp≈0.94–1.0) rank #4–7.
For an IR-team-facing "ranked wealth-management targets" artifact this ordering may not reflect
v0.7.3 intent. Surfaced to COO + CVO: should the W3 table re-sort by `am_prominence` in v0.2+?
This is a code+test+sign-off change, out of `.023` empirical-run scope — flag, not a self-fix.

## Unblocks

DS~C FIND_INSURE.024 Phase-2A — `serving/scoring.json` is the HARD INPUT it gated on.
