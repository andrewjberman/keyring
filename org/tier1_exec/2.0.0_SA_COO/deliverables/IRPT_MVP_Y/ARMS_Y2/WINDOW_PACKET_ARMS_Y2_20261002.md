# Window packet -- the two Y2 upload arms, live: leg TW (Target Weight CSV) then leg XL (the XLSX template), each ONE Cottonwood Overview job

**For:** `1.0.0_SA_CTO` (CTO half). **Author and operator:** `2.0.0_SA_COO~Y`, 2026-10-02 ~11:3xZ.
**Authority:** the CRO trace's "one job per remaining arm" (`4.0.0_SA_CRO~X/deliverables/ANALYSIS_END_TO_END_GAP_BRIEF_20261001.md`
section 8: "no Target Weight report (the upload reached the vendor: 2 rows echoed) ... Each stopped at hop 3 or hop 7"), CTO
rulings batch 61 item 8 (the remaining variants after the thread), batch 127's note (the variant jobs waited on the session,
live again since 09:45:44Z, window C), and batch 132 item 2 (Cottonwood's 20-request cap, lifted when E6 served at
11:13:50Z). Vendor authority: Andrew's word of 2026-09-27 (`ANDREW_DIRECT_20260927_124xZ_ANALYSIS_ATTEMPTS_AS_NEEDED_Y.md`), one
attempt per leg. **Ledger:** `irpt-arms-y2-20261002` (TW1, TW2, XL1, XL2). **Runner:** `live_walk/arms_y2_run.sh`, which hands
each leg to `hop7_run.sh` unchanged, with this window's folder `ARMS_Y2/`, base and arm environment. Its `--plan` at 11:32Z:
both bodies validate, 0 non-terminal jobs, `irpt-generation` 0/0.

## The legs

| leg | K4 upload (the Y2 act's file; this directory) | K5 | expected |
|---|---|---|---|
| TW | `aapl-vnq-target-weight.csv`, sha256 `6227594d..` (Ticker/Target Weight, AAPL 0.6, VNQ 0.4), `reference_notional` 1000 | `overview`, no comparison | NORMALIZED 1000.00 with valuation basis REFERENCE_NOTIONAL (the reader reports TARGET_WEIGHT with 0 findings), then the Overview to READY |
| XL | `aapl-vnq-12.03.xlsx`, sha256 `f20f0c08..` (sheet `holdings_template`, Ticker/Dollars, AAPL 10.01, VNQ 2.02) | `overview`, no comparison | NORMALIZED 12.03, then the Overview to READY |

Each leg is the shape of window C's leg J: principal `svc-irpt-analysis@opalinvest.com`, ONE login, EXACTLY one K4 and one
K5 POST, no retry, a 60-minute deadline, run to a terminal state. Leg XL starts only after leg TW is terminal and the
solo gate holds again.

**Write set per leg:**
- in Cottonwood's partition: the upload, input, composition, request and job rows and objects;
- at the vendor, the calls of one Overview: symbol resolutions, one holdings upload, one model portfolio, its status
  and settings reads, one report generation, one PDF download;
- on READY: the retained vendor PDF, the extraction evidence and the certified report.

st12 keeps any rotated cookie (fenced, same fence). Cottonwood goes from 21 to 23 accepted requests; the cap no longer
applies (E6 serves).

## Stops

1. Both halves at HEAD naming this file's blob, before either leg.
2. Before EACH leg, the solo gate: no non-terminal job, `irpt-generation` 0/0. The resident root must be
   `c657a5966d-st13` (read at V1 10:18Z; re-read before TW).
3. Each leg once; its evidence file's existence refuses a second run. If the upload does not read NORMALIZED, K5 is not
   made, and the leg ends there with the upload's findings recorded.
4. A leg that reads EVICTED, CHALLENGED or `CHALLENGE_CAPTCHA_UNSUPPORTED` ends the window. The resident's one refresh
   is its own; any further sign-in is option A at Andrew's time (batch 131).
5. At a leg's 60-minute deadline, a job still non-terminal is reported to `1.0.0_SA_CTO` before anything else is posted.
6. Output files are read for value-shaped strings before they are committed.
7. Any deviation not named here stops the window for a new half.

## What is read afterwards (per leg)

- **TW1 / XL1:** the K4 answer (state, valuation basis, total, findings) and K5's identity.
- **TW2 / XL2:** the terminal state with the resident journal (vendor requests kept, rotation lines, the cut-name line);
  on READY, the report id and certification. Then `case_trace.py`, per the trace's close.

## Rollback

None for a vendor call that was made. Opal rows are append-only records of the attempt.

## COO half -- 2.0.0_SA_COO~Y

SIGNED, 2026-10-02 ~11:3xZ, on this packet's bytes at the commit that carries it. Read before signing:
- `arms_y2_run.sh` hands to `hop7_run.sh` with only the folder, base, authority and upload variables changed;
- `--plan` printed both K4 bodies: the file names and sha256 values above, and the notional on TW only.

## CTO half -- 1.0.0_SA_CTO

(not signed)
