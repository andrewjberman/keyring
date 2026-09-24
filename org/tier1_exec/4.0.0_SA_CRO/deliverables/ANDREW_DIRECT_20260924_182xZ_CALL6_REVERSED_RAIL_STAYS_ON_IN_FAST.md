# ANDREW-DIRECT 2026-09-24 ~18:2xZ (~2:2x PM ET) -- call 6 reversed: the comp-tool rail stays on in FAST mode and blast mode

**Channel:** the `4.0.0_SA_CRO~A` terminal. **Recorded by:** `4.0.0_SA_CRO~A`, same turn, at 18:25Z by the system
clock.

## Verbatim

His question:

> Why would we allow for /freeform when that is not as good as using our comp-tools?

His answer to this seat's recommendation to reverse call 6:

> yes

## What it binds

1. **Call 6 of report 2 is REVERSED.** It was approved at ~15:3xZ in
   `ANDREW_DIRECT_20260924_153xZ_REPORT2_ALL_SEVEN_RECS_APPROVED.md` item 6.
   - A FAST lease no longer stands down the comp-tool rail.
   - `.tools/drive-mode.py read` no longer mirrors a lease into the session's `/freeform` marker.
   - `/closer-drive` step 0 and its FAST -> FULL `freeform.sh off` step lose their rail lines.
2. **The `/freeform` authorization attached to blast mode is withdrawn** for `2.0.0_SA_COO~P`, `~M`, `~Y` and `~D`.
   - The source is `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260924_174xZ_BLAST_MODE_P_M_Y_D_ONLINE_FAST_CLOSER.md`,
     "Blast mode is his word for speed. It authorizes /freeform ... for all four seats".
   - That line was the CTO's reading of "blast mode", not his wording. The rest of blast mode is unchanged.
3. **Why:** comp-tools print denominators and see gitignored content, so they are better when one fits.
   - The real cost the stand-down answered was false denials: 983 denials, 1,455 "no fit" results and 331 overrides
     in 7 days (report 3 section 1.5).
   - Report 3 item 1.6, built at `3c3df0fca2`, now admits a raw search for 10 minutes only when `comp-which` returns
     NO FIT. That fixes the real cost without giving up comp-tools where they fit.

## Unchanged

- `/freeform` itself stays, armed on his explicit per-session word as before.
- Every other part of FAST mode and blast mode stands.

Owner: `1.0.0_SA_CTO` (`drive-mode.py`, `/drive-mode`, `/closer-drive`, `org/ref/LIVE_ARMS.md`, spine FAST
paragraph); `0.0.0_AB_MSTR` for any live session marker already armed.
