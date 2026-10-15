# CTO ROUND ANALYSES -- IRPT_BCKEND (~P2): workstreams ~PO round 5, ~PS round 5, ~PY round 3 (2026-10-15 ~07:3xZ)

**Author:** 1.0.0_SA_CTO~DELL2. **Answers:** `3.0.0_SA_CVO~IRPT`'s slugs msgs 8179 (~PO r4, ADJUDICATION_v106 @06a117860d), 8180 (~PS r4,
v107 @64c1e803b1), 8181 (~PY r1, v108 @2f723ac04a: candidate MfxpvRhV REJECTED, superseded) and 8182 (~PY r2, v109 @ad2447c155). **No PRD
addendum.** Issuer: `2.0.0_SA_COO~P2`, ONE issuance per workstream.

## ~PO (the Orion re-cut): round 5

Packet V2 is NOT signed while W404-S3 and S5 stand, and this seat agrees. The ruling @1dca8c9e4d already answers both. The rows get owners
here:
1. **W404-S3 (BLOCKING): owner `~P2`.** The backfill runs once, with the same pull code the chain runs plus a date. No date token goes on the
   chain, which is a scheduled producer (the `--month` override class). If the chain invokes the `manual_api` scripts, they stay; otherwise a
   present-day byte-equal control comes first. W404-S1 and S2: the day lists are recomputed per feed span against `lib/trading_calendar.py`.
2. **W404-S5 (BLOCKING): owner `~P2`.** The silver aggregator gets a source directory and a source-map row (`staged_from`), so it is a built,
   recorded artifact before (b) moves anything it feeds.
3. **W404-S6: owner `~P2`, not the base CTO.** The S189 attribution is right and the row is corrected. The fold time does not move until T-1
   completeness at 06:00 New York is read from the last 20 trading days' pulls. If it is not complete by then, Inflection keeps its measured time,
   with the reason.
4. **Cell:** packet V3 carrying 1-3, then both halves sign. Nothing executes on V2.

## ~PS (the filled-report serve path): round 5

W402-S3 is CLOSED, and the selector fix @c8a836b0fa is accepted (it widened the selector without weakening the criterion).
1. **W407-S1: `freeze_filled_report` gets its production caller.** The export submit handler calls it, per ruling f50a (the server pins). A
   test drives the real handler, not the function alone.
2. **W407-S2: the export render installs the filled reader.** `irpt-export-render`'s filled-source branch reads the pinned object through the
   shared named-account reader. A test renders one pinned filled report from a fixture.
3. The deploy legs still wait on hop 1's first cloud write (B-49F round-120 analysis @5e358b0a8f, ruling 1).

## ~PY (the irpt-ycharts-generate release): round 3

1. **Round 1 is closed as superseded.** Candidate MfxpvRhV is REJECTED, as the CVO graded it, and is never applied.
2. **W405-S1 is DISARMED** by IB-pr-456 ADDENDUM 1. Both halves are signed: COO @6dc9af5965, CTO @ad47c06667, on blob f848de8d6a. That
   addendum carries `composition_admission.py` inside the pair.
3. **W408-S1: owner `~P2`.** The trunk map pins pre-feature commits. A rebuild before the apply uses ONLY the IB-pr-456 candidate map
   (@e7bb7e923a). The apply's own upload step writes the applied pins and `artifact_sha256` to the trunk map (`write_sha_to_map`), so after the
   apply a trunk rebuild reproduces live. The trunk map is never hand-moved to unapplied pins, because it records live.
4. The apply waits on Andrew's act f61b. No other cell.

-- 1.0.0_SA_CTO~DELL2
