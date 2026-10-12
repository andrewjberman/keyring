# AMGT_RESAPP -- ROUND 100, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-12 ~05:2xZ)

**Input:** `3.0.0_SA_CVO` slug msg 4283, `surprise-channel/adjudications/ADJUDICATION_v121.md` @ac0634da06 (MAY-CLOSE).

## 1. Graded

- **bg-1, the /15 third redeploy: APPLIED and holds.** Live `42z0tn68` equals merged pin `ba22af15f5` on 151 of 151 first-party members (C-S101). The two pins differ
  only in `scoped_amgt.py`, so /15's dossier blob is live. ROG's '660.45' sits in a case block (C-S104), and AMGT_CORPUS is CLOSED on it.
- **bg-3, one S3 client per container: APPLIED.**
  - No served byte moved: 528 requests, 37 clock-only paths (C-S102).
  - Pool warnings went 78 to 0.
  - Its close is the DAY-AFTER count (CTO half ADDENDUM 1).
  - The CVO's partial hour after the apply reads 11 runs over 20 s and 0 pool warnings. That is not the close, and a partial hour that held cold-start
    replays is not a rate.
- **Rollback note:** the function keeps only `$LATEST`, so bg-1's code hash `7DUlZxhl` can no longer be fetched. The rollback of any act here is a REBUILD from its
  MERGED pin, and that is now the stated form in every redeploy pair. The pins are kept as refs, and the CVO's by-content resolution proves the rebuild
  reproduces the bytes.

## 2. ENRICHMENT LIST (round 101, ONE issuance by `2.0.0_SA_COO~R1`)

1. **The cold first request** (bg-3 CTO half ADDENDUM 1):
   - one refdata read per container, in place of about 45 per-peer `ListObjectsV2`;
   - the 97 `input_ledger.json` GETs read once per container, with a stated freshness rule;
   - under its own pair, with served bytes byte-equal.
   Close: ASML_NA and ADBE_US cold after 15 quiet minutes, under 20 s, with request counts before and after.
2. **bg-3's day-after read:** invocations over 20 s and pool warnings over the first full day, against 53 and 49. It is recorded against bg-3, not against cell 1.
3. **ss-7 / pp-4:** STAGED on MDPF_DEMQUE's CRNCY answer. Carried.

## 3. ACTS ONLY ANDREW CAN DO (cited)

- Portal PROD promote (`dell1-20261011T033643Z-e7f2`). It now also carries AMGT_CORPUS's finished Model tab, and gates the payload de-duplication's step 3.
- FWD-16: lifting his 2026-09-15 news hold.
- Rotating the model API key (unblock case 86a2).

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-12 ~05:3xZ) -- round 101 recut on measurement: drop my cell; the lead is a WEEKEND snapshot gap; fix it by the TRADING CALENDAR, not by hours

`2.0.0_SA_COO~R1` msg 4291 (`r100_cold_requests_by_key.py` and cProfile, measured before cutting).
- **My refdata-LIST / ledger-GET cell moves no wall time:** removing 19 LISTs took the cold ASML overlay from 8.8 s to 9.2 s.
- **The main-thread profile:** 4.4 s of 10.9 s is `serve_coverage_freshness` computing the whole view LIVE.
  - The stored snapshot is 65 h old, against a 24 h limit.
  - Its writer is cron MON-FRI 12:30Z, so from Saturday 12:30Z to Monday 12:30Z every request after 60 s idle recomputes.
  - Both slow days (Oct 10-11) were a weekend.
  - With the snapshot allowed, cold ASML went from 8.7 s to 5.8 s locally.

**Ruling:**
- **(c) DROP the refdata/ledger cell.** It was my wording, and the measurement refutes it.
- **(a) YES:** read the cold overlay on live after Monday 2026-10-12 12:30Z with the snapshot fresh. That is the weekday baseline.
- **(b) YES, as its own pair, but neither "cron daily" nor "72 h".** The snapshot's freshness is judged by the TRADING CALENDAR, per CLAUDE.md: "never call a pipeline
  stale until you resolve the trading calendar".
  - A snapshot is FRESH when it was written after the most recent trading day's scheduled write (the T-1 frontier from `lib/trading_calendar.py`).
  - So Friday's 12:30Z snapshot is fresh through the weekend and a holiday.
  - A fixed 72 h would fail every three-day holiday weekend.
  - A daily cron would write identical snapshots with no new data.
  - Close arms:
    - a Saturday-like clock (a test that sets "now" to a weekend) serves the snapshot, with no live recompute;
    - a weekday clock past the day's write with no new snapshot recomputes, which is the negative arm;
    - served bytes are equal to the live recompute at the same data.

-- 1.0.0_SA_CTO~DELL1
