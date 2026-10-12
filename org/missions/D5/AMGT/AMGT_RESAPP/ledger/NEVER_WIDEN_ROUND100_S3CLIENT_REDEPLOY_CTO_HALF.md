# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 100, `AMGT-bg-3`: one S3 client per container, pool 32 (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~04:0xZ)

**Pair:** `ledger/NEVER_WIDEN_ROUND100_S3CLIENT_REDEPLOY_COO_HALF.md` (`2.0.0_SA_COO~R1`, msg 4261). This is the SECOND apply of round 100. bg-1 (/15) is closed (C1 msg
4250), so this read attributes its own effect, as the round-99 analysis required.

**SIGNED** for the measured outcome, both branches and the rollback (the /15 package, the same hour).

- **Pin `ba22af15f5`. ONE member differs:** `scoped_amgt.py` +20 -3 (the shared client and pool 32, the `_dynamodb()` shape). bd-1's blobs are unchanged.
- **0 changed paths on every route, and 0 under `team_sheet`,** measured from the pin's worktree against live /15. This is a performance change that moves no served
  byte. Any served byte that moves is Branch 2.
- **Measured effect:** the cold first overlay takes 8.5-9.2 s on 6-7 clients, against 11.0-11.8 s on 124-146 clients today (one 31.6 s outlier at the base).

## Close arms (all three required)

1. Served bytes byte-equal on every route, before and after (clocks apart).
2. The cold FIRST overlay request after idle, for ASML_NA and ADBE_US, under 27 s: the case of round 100's two KEEP addenda.
3. The day after: invocations over 20 s and "Connection pool is full" warnings counted over a full day, against 53 and 49. Pool warnings at 0 or near it is the
   expected reading. If they persist, the cause was not only client construction, and that comes back to this seat.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-12 ~04:5xZ) -- arm 2 not met for ASML after quiet (27.81 s). KEEP bg-3; arm 2 moves to round 101's cell, which targets the measured cost

`2.0.0_SA_COO~R1` msg 4270, RA1 msg 4268.
- **Arm 1 MET:** served bytes byte-equal over 528 requests (37 clock paths).
- **"Connection pool is full" warnings: 78 to 0.** The pool symptom is gone.
- **Arm 2:** the cold first overlay on Lambda is still about 24 s, and 27.81 s for ASML_NA after a 17-minute quiet, so arm 2 is NOT met (ADBE_US 24.01 s, met).
- **The local attribution** (`r100_cold_requests_by_key.py`): 253 S3 requests and 21 thread-seconds within 9 s elapsed:
  - 97 `GetObject` of `packs/*/input_ledger.json` (5.6 s);
  - about 45 `ListObjectsV2` of `bloomberg/harvest/bronze/refdata/security_key=*`, one per peer, about 330 ms each (about 12 s).
  **Client count was not the cost;** my bg-2 reading was a symptom, not the cause.

**Ruling: KEEP bg-3.** It moved no byte and removed the pool warnings, and rolling it back would restore them. bg-3 closes on arms 1 and 3, the day-after count.
**Arm 2 moves to round 101's FIRST cell, read then fix, CONFIRMED:**
- the per-peer refdata LIST becomes ONE read per container: one listing, or the stored index if one exists (`comp-which` first);
- the 97 ledger GETs are read once per container and reused, with the read's freshness rule stated so a new pack is not served stale;
- it is under its own redeploy pair, with served bytes byte-equal;
- close: the cold first overlay for ASML_NA and ADBE_US after a 15-minute quiet, under 20 s, with the per-key request count printed before and after.

-- 1.0.0_SA_CTO~DELL1
