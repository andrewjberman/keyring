# Drive log 2026-10-03 17Z -- 2.0.0_SA_COO~Y (IRPT_BCKEND~Y, FAST)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE

## Ticks

| time (Z) | act | evidence |
|---|---|---|
| 17:03 | Y-3 V1 READY on the HAR-restored session: REQ-329a56182b2668d44a28c8d7 (Multi, ULT + IWM, Cottonwood). QUEUED 16:45:31, SUBMITTING 16:45:50, DOWNLOADING 17:01:09, CERTIFYING 17:01:44, READY 17:03:14; report RPT-c8c4037aaf09c01cd6d7797eb28cc7f8 | `deliverables/IRPT_MVP_Y/Y3/V1A/V1A2_*` @ee801b0505 |
| 17:1x | Ledger irpt-y3-20261002 CLOSED, all 5 legs proven | @284667acb5 |
| 17:16 | Andrew's research request (direct YCharts API calls, response shapes mapped into the export for the three generation types, then an Opal-branded generator on the same endpoints, outputs in our buckets) filed and sent to 4.0.0_SA_CRO on Andrew's word | `deliverables/IRPT_MVP_Y/RESEARCH/CRO_REQUEST_YCHARTS_DIRECT_GENERATION_20261003.md` @ee801b0505; message 1056 bytes in the CRO's read dir |
| 17:29 | Y-5 V1 Case A: solo gate clear (no non-terminal job, queue 0/0); asked 2.0.0_SA_COO~D to add case `Aproxy` (TIMXX -> SGOV) to its page driver and run it once live | broker 20261003T172925Z |

## Compiler Tools

None run: this hour was live runs, a ledger close and two messages; no code or infra changed.

## Current state

- Y-3: closed. Y-5 V1: waits on 2.0.0_SA_COO~D's page run. Y-4 V1 follows Y-5, one at a time and spaced (CTO 104634).
- The SUBMITTING span (15 m 19 s of 17 m 43 s) is INFERRED to be mostly the recipe's 900 s read-back receive
  (`recipe.py:655-665`), not measured on this job; the CRO research request names it as the first thing to measure.

## Next

- [2.0.0_SA_COO~D] Case Aproxy live run; then record it and close irpt-y5-20261003 V1.
- Then Y-4 V1 (typo file, APPL -> AAPL), then Y-2 and Y-6.
