# Drive log 2026-10-03 20Z-21Z -- 2.0.0_SA_COO~Y (IRPT_BCKEND~Y FAST; IRPT_YCDGEN)

**archetype:** DEPLOY
**secondary_archetypes:** DIAGNOSE, COORDINATE

## Ticks

| time (Z) | act | evidence |
|---|---|---|
| 20:26 | Andrew "all approved" (CTO 104738): the site-Z review does not cover ~Y's YCharts tests; the direct-generation DONE WHEN lines confirmed | CTO record ANDREW_DIRECT_20261003_203xZ |
| 20:29 | Solo gate clear; Aproxy go to 2.0.0_SA_COO~D | broker |
| 20:37-20:45 | Aproxy live run 1 refused at upload: no `selected_tenant` (portal f2d2f17c; run 3 of 10-02 had it); generate log IdRefused. Cause sent to ~D | ~D 104748; generate request 57fdbec1 |
| 21:01-21:05 | Re-fire with Cottonwood: UP-852105aa NEEDS_CORRECTION, row 100 TICKER_DATA_NOT_ENTITLED, value NULL, so no proxy box. Ruled a backend defect (the correction contract needs from_value = the symbol); ~D told to hold | ~D 104763 |
| 21:05 | IRPT_YCDGEN PRD v0.1 landed (CTO 104764); L5 is ~Y's | acked |
| 21:1x | Fix 1545ec3442: the four ticker findings carry value = the file's symbol; negative control 2 FAIL on HEAD, 32 pass; suites 272 / 396 pass. Merged a163441fb0 (after ~P committed its staged ledger) | 1545ec3442, a163441fb0 |
| 21:21 | Ledger irpt-y5v-20261003 opened before any act | fb7a256405 |
| 21:3x-21:5x | Generate row repinned (only this row; a foreign authorizer edit left in place) 095968d363; U1 zip YImF8vih (census 105 identical, 9 changed, 0 CRLF; smoke 3 PASS); U2 tar IJG0WnOf + script BHSM0RkX (gate PASS); packet blob 7d815d61db | 095968d363, 276bea84f6 |
| 22:00-22:17 | CTO half batch 233; before-read clean; D1 applied (jKsI7pZW); D2 installed (st19); Aproxy re-fire asked | 612a2ea014 |

## Compiler Tools

| tool | result | note |
|---|---|---|
| bundle_vs_live_census.py | PASS | 114 members, 9 changed, 0 CRLF |
| resident_package_gate.py | PASS | G1-G5; G5 changed 6 |
| zip_cold_start_smoke.py | PASS | 3 routes, built and deployed bytes |

## Current state

- Served: irpt-ycharts-generate `jKsI7pZW..`; resident `/opt/irpt-resident/a163441fb0-st19`. Rollback: S3 `w2yfewe..`; root
  `a6f6e7165e-st18` on the host. Ledger irpt-y5v-20261003: V1 open.
- Y-5 V1 waits on ~D's Aproxy re-fire; Y-4 V1 follows (the same fix lets the page name APPL as from_value).

## Next

- [2.0.0_SA_COO~D] Aproxy re-fire; ~Y records it and closes irpt-y5v and irpt-y5 V1.
- ~Y: IRPT_YCDGEN L5 decomposition and L6 issuance.
