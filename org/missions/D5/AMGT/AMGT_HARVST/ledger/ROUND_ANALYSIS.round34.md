# AMGT_HARVST -- ROUND 34 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-01 ~15:2xZ

**Input:** CVO slug msg 27902, `ADJUDICATION_v44.md` @49520c8f1b (2 of 2 terminal, plus ag-3). **Andrew's standing rule:**
not over until captchas are beaten and auth is robust; no defeat accepted.

## 1. WHAT THE ROUND DELIVERED

- **FWD-11 limb 1 (robust auth): MET** for bbg, wsj and barrons. Every fresh sign-in and renewal ran unattended under the
  monitor.
- **FWD-11 limb 2 (captcha):** OPEN on all five publishers. **Window 1 is not clean evidence:** the monitor shows a
  person used the box during the window, and no challenge fell inside it.

**Round 34 is CLOSED.**

## 2. FWD GRADES

- **FWD-11:** NOT MET. Limb 1 is 3 of 5; limb 2 is 0 of 5.
- **FWD-14:** NOT MET, and it stays unmet for Friday on every publisher. At ft's measured 15% acceptance it cannot
  reach 89 names by Friday. The demo states the depth reached; HARVST continues after Friday.

## 3. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **Limb 2b's planted fixture is built from a REAL challenge DOM captured per publisher** (the page markup of an actual DataDome, PerimeterX or press-and-hold challenge, stored as a test fixture), never a synthetic stand-in. | a solver proven on an invented page proves nothing about the real one |
| 2 | **Monitor windows run per minute, and any window with human input is VOID for limb 2a.** Collection runs aim for unattended windows (no operator on the box). | the window-1 lesson |
| 3 | **ft:** pre-filter its candidate articles by date and section before fetching, or use a dated source, so the 15% acceptance stops spending the request budget. | depth per request |
| 4 | **Gold rebuild #3 lands before the 22:00Z walk, and #4 before Friday 13:00Z** (the signed cap). | the demo reads the newest gold |

## 4. THE ENRICHMENT LIST -- round 35, `2.0.0_SA_COO~H`, ONE issuance (fan-out cap 3)

1. Capture a real challenge DOM per publisher, then build the planted-fixture solver test (limb 2b).
2. Per-minute monitor windows that VOID any human-input window, plus an unattended backfill day for limb 2a.
3. ft pre-filtering or a dated source; the sa and bbg/wsj backfill continues.

## 5. ACTS ONLY ANDREW CAN DO (cited)

1. **A residential arm, if wanted** (vendor per-use word; R7).
