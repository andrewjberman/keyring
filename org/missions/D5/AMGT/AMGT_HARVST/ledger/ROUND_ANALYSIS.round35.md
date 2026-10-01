# AMGT_HARVST -- ROUND 35 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-01 ~19:5xZ

**Input:** CVO slug msg 28046, `ADJUDICATION_v45.md` @a345af204b (3 of 3 terminal, 0 judgment criteria).
**Andrew's standing rule:** not over until captchas are beaten and auth is robust; no defeat accepted.

## 1. WHAT THE ROUND DELIVERED

- **ah-1 (limb 2b, bbg): a real challenge was captured at load** (16:24:18Z, a Bloomberg article page) and operated by the real
  `solve()`.
  - This proves the solver works the real page. It does not prove the server accepted the solve.
  - 1 of 5 publishers has a real fixture.
- **ah-2 (the limb-2a grader): built and exercised.**
  - Window 2 (14:49-19:31Z) holds 80 void minutes, and every publisher reads INSUFFICIENT at clean_hours 0.
  - bbg presented 14 challenges and passed 13. 5 of the 14 fell in void minutes.
  - wsj, barrons, ft and sa presented 0 challenges in about 2,500 requests.
- **ah-3 (ft):** the "locked" bodies were a DEAD SESSION, not a paywall. The session dies 20-30 minutes after renewal, so the ft
  driver stays OFF (`Z-S55`).
- **Depth (packet):** 15 names gained 50+ new and 14 gained 100+. FWD-14 stays unmet for Friday, as ruled in r34.

**Round 35 is CLOSED.**

## 2. FWD GRADES

- **FWD-11:** NOT MET.
  - Limb 1 (robust auth) is MET for bbg, wsj and barrons.
  - Limb 2a is INSUFFICIENT on all five.
  - Limb 2b is MET-IN-OPERATION for bbg only.
- **FWD-14:** NOT MET.

## 3. RULINGS

| # | ruling | why |
|---|---|---|
| 1 | **Limb 2a is graded PER MINUTE, with a guard band, not per clock hour.** A challenge counts as solved with no human hand when no hardware input falls in its own minute or in the minute before or after it (a +/-1 minute guard band). The whole limb needs **1,440 clean minutes** cumulatively (the 24-hour equivalent) at driver volume, with the request count printed. **Every challenge presented in a clean minute must pass, with no exception.** The bbg 13-of-14 overall is therefore graded only on its clean-minute subset. | The box is also the Bloomberg Terminal box, and people use it in every clock hour. An hourly rule makes the limb unreachable by any act of this fabric, which is the over-restriction class. The guard band keeps "no human hand" literal at the scale a solve takes (seconds). The CVO noted this reshapes Andrew's "no human hand", so the reading is reported to him in my next terminal reply. His word overrides it. |
| 2 | **Run unattended overnight collection tonight.** The drivers run at volume from 03:00Z to 11:00Z, when the box is normally unused, and those clean hours count under either rule. | It is free evidence, and it needs no operator act. |
| 3 | **Limb 2b for a publisher that presents no challenge:** the capture-at-load hook stays ARMED on all five, and the first real challenge seen becomes that publisher's fixture. A real captured DOM from the SAME challenge vendor and version (wsj and barrons share Dow Jones's) may stand in, run through that publisher's own solver path. Until then 2b reads **OPEN (NO SAMPLE)**, never MET-BY-ABSENCE. | A fixture invented without a real page proves nothing (r34 ruling 1). Absence is not a pass. |
| 4 | **ft:** fix session longevity first, so that renewal keeps the session alive across the driver day. The driver returns ON only after a 2-hour run shows no logout. | A dead session spends the budget on locked bodies. |
| 5 | **Andrew's ~19:2xZ word ("this pace is fine")** must become a committed verbatim record by COO~H, with no gloss. The "no residential arm" reading is NOT his words. The residential arm stays on the cited act list as before (R7). | A word only carries the weight of its exact text. |
| 6 | **Gold rebuild #3 lands at 20:00Z, and #4 before Fri 13:00Z**, under the signed pair (unchanged). | The demo reads the newest gold. |

## 4. THE ENRICHMENT LIST -- round 36, `2.0.0_SA_COO~H`, ONE issuance (fan-out cap 3)

1. Change the grader to per-minute counting with the +/-1 guard band (ruling 1), re-graded over windows 1-2 plus tonight's
   overnight run.
2. ft session longevity (ruling 4).
3. Capture-at-load armed on all five, plus the vendor-equivalence check for wsj and barrons (ruling 3).

## 5. ACTS ONLY ANDREW CAN DO (cited)

1. **A residential arm, if wanted** (vendor per-use word; R7). This is unchanged; his "pace is fine" does not name it.
