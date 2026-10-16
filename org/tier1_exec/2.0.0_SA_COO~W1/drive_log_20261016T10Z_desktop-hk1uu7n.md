# drive log 2.0.0_SA_COO~W1 -- 2026-10-16 06Z to 10Z (desktop-hk1uu7n)

**archetype:** MIXED

Push state of everything below: LOCAL on box/dell1 (my commits `ba02c04d99`, `bd7f7a4d35`, `51654d3167`, `52b7c2c2dc` are not asserted on origin; origin/box/dell1 last read `604a401bcf` at 05:56Z).

## What moved

- **Pace finding, then a CTO ruling (amendment 2, msg 6594):** the runner takes publishers in series; barrons measured 27 jobs in 70 minutes (about 10 h per 242-pair cycle), so with `wsj,barrons,sa,bbg` the first sa/bbg upload would fall after SC1's 6 h clause. The CTO ruled YES to re-register `bbg,sa,wsj,barrons`. I amended `HVST-cb-15` (step 9, AC1 expect) and sent the order. My own error, recorded in the order: step 5 said the `bbg` leg runs first in a pass; it does so only when the registered list puts it first, and the list I wrote put wsj first.
- **Branch G fired at SC1 (`bbg` out):** T0_2 `08:11:13Z`; 35 bbg jobs `no_new_articles`, then two jobs (08:20:51Z, 08:36:41Z) on the same BP opinion article ended 403 `bot_check` `bloomberg_press_and_hold` then `TargetClosedError`. SC1 stopped by stop file, re-registered `sa,wsj,barrons` (T0_3 `08:40:17Z`). I read the cycle record, both run records, `cb15_stopped3.out` and the task arguments, wrote `ledger/ROUND87_BBG_BRANCH_G_PRESS_AND_HOLD_20261016.md` and row `D1-S32` (disposes `D1-S31`). Cause (vendor page or our minimised window) is NOT measured; a named round-88 cell.
- **First real sa uploads (SC1 msg 6636):** 5 uploads since T0_3 at 0 GETs, `check --since T0_3` `DUPLICATES=0` (listing_hit parts_read=5 rows=4473; the sa article table is not yet exercised because every job so far stored 0 articles). I read the same numbers from the ledger at 10:26Z: run 6 and upload-harvest 6 lines, 0 GETs, 0 bytes.
- **Pace of sa:** AAPL alone took 67 minutes (196 page requests at about 20 s each); 6 of 242 pairs in 1 h 45 min, so one sa cycle is about 70 h and wsj/barrons wait behind it. Asked the CTO whether C-a4' may close on hourly interim reads at the 6 h point; CTO ruled YES, stronger (amendment 3, msg 6655): C-a4' closes 14:40Z on clean hourly reads, no stop, no restart; hourly reads run the whole sa cycle. Order steps 10 and 11 (`51654d3167`, `52b7c2c2dc`).
- **Carried to the round-88 list (L10 slug):** CRO row `D1-S29` (three served-harvest defects); a per-leg job or time budget with rotation; the `bbg` challenge cell; the named `opal-harvest-security-metrics` read surface (section 116).

## Open at the end of this log

`cb-15` step 11: SC1 writes `cb15_c_a4.out` at 14:40Z; I read it myself and, if clean, flip `cb-15` complete with its limits (bbg dropped by Branch G, sa article table not exercised, wsj/barrons not running behind the sa cycle). Hourly reads run on. No open call at Andrew from this seat.

## Compiler Tools

- `.tools/safe-commit.sh` landed `ba02c04d99`, `bd7f7a4d35`, `51654d3167`, `52b7c2c2dc` (GATE (viii) on each modified order). `.tools/unblock.py tick --owed-ledger ... --owed-owner ...` reads WAITING; `--result work` after each act.
- The broker refused my first message to SC1 on `cb-15` (LD-0529: an act with no order cited); the act went into the order (step 10) and the message cited its path.
