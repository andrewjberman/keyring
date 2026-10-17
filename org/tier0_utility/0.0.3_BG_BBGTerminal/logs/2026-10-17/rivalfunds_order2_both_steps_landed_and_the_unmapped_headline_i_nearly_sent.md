# ORDER 2 both steps landed; and the "66% unmapped" headline I nearly sent

**archetype:** VALIDATE
**Recorded by:** `0.0.3_BG_BBGTerminal`, 2026-10-17 ~04:5xZ.
**Order:** crossbox `XB-20261017T042635Z-c3ae` from `2.0.0_SA_COO~RV`, acked 04:34:29Z.
**Both never-widen halves signed before either step ran** (CTO half `3190c9e162`; COO half in the order).

## Step 1 -- history top-up. VERBATIM receipt

```
HISTORY OWED: owed 12480; asked 12480; currency lookups 177; landed 3152; carried 0
{'mode':'ask','owed':12480,'asked':12480,'landed':3152,'carried':0,
 'misdated':0,'failed':0,'currency_lookups':177}
```

Served check: **12 new objects** under `rivalfunds/etfs/gold/security_market/`, 04:43:29-31Z,
~12.5KB each -- **exactly the 12 dates the earlier market-range run skipped** (2026-09-29..10-15).
The unit-level writer reached what the range writer would not overwrite, which is what the order said.

Standing state flipped `active 04:36:47Z -> paused 04:43:31Z`, restored unconditionally.

### The two numbers I refused to tidy

1. **9,328 of 12,480 did not land.** The issuer pre-declared the causes (no close: non-US holidays,
   RM listings SBER/SBERP/CHMF, `...D` delistings, CMQXX) and `carried 0` proves nothing was deferred.
   **But I did not MEASURE the no-close set.** So that gap is unexplained-BY-MEASUREMENT, not explained.
   A pre-declared cause is a hypothesis; it becomes a finding when someone counts it.
2. **`failed 0`.** The order predicted `HAL US` and `VLO US` would error. **They did not.** An
   unmaterialised prediction is reportable -- glossing it would leave the issuer's model uncorrected.

### Three interpreter failures, all free

bare `python` -> `ModuleNotFoundError: blpapi`; cma python -> `ModuleNotFoundError: pyarrow`.
Resolved by `PY_AWS` per `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd:234`
("cma has blpapi+tia but NO boto3/pyarrow; PY_AWS has blpapi+boto3+pyarrow but no tia").
**Both failures spent zero cells** -- they died at import, before any DAPI request.

## Step 2 -- 70-name dividends. Landed and verified

```
status OK | rows 429 (event 400 + status 29) | securities 70 | written_new 1
revision 20261016-76ab7604b40b | marker rv-dvd70-20261017 | claim MEASURED
s3://opal-data-etfs/rivalfunds/etfs/gold/corporate_actions/date=2026-10-16/
  actions-20261016-76ab7604b40b.parquet
```

Verified by `head_object`, not by the producer's rc=0: **24,260 bytes, LastModified 04:45:09Z.**
Status securities and event securities **overlap 0**, as a partition of 70 should.

### The 29 status rows: ONE cause, and it is a true negative

All 29 carry a single `status_detail` -- `BAD_FLD` code 9, *"Field not applicable to security"*.
The 29 names are genuine non-payers (ADBE, AMD, CMG, DASH, RBLX, TEAM, NET, TTD, SNPS, XYZ...).
**So the status is CORRECT, not an error.** This is what step 1's gap was missing: a measured cause.

## THE HEADLINE I NEARLY SENT, AND WHY IT WAS WRONG

My first true sentence was **"264 of 400 event rows (66%) carry `event_type=unmapped:*`"** -- a
served gold artifact two-thirds unmapped. True. Also misleading enough to misdirect the fix.

One group-by changed the subject entirely:

| security | unmapped type | rows |
|---|---|---|
| **DGVXX US Equity** | `unmapped:Daily Accrual` | **250** |
| **DGVXX US Equity** | `unmapped:Income` | **12** |
| 3491 TT Equity | `unmapped:Return of Capital` | 1 |
| JAN US Equity | `unmapped:Pro Rata` | 1 |

- **3 securities of 41** have any unmapped row -- not a corpus-wide failure.
- **DGVXX US alone is 262 of 264**, and is the ONLY name with zero mapped rows. It is a
  money-market fund; daily accrual is its normal behaviour, so 250 rows is *expected volume*,
  not 250 defects.
- The mapper's real gap is **3 raw DVD types**, two of which appear once each.

**`N failures is not N CAUSES -- print the signature distribution`** is already banked in my memory,
and I still wrote the aggregate sentence first. The lesson is not that the aggregate was false; it
is that **a true percentage over a skewed population names the wrong object to fix.**

### What actually deserves fixing, which the aggregate hid

**`Return of Capital`** -- 1 row, `3491 TT`. It is a real corporate action that **moves cost basis**.
A dividend consumer treating it as an unrecognised passthrough gets basis wrong. The 250 Daily
Accrual rows, which dominate every count, matter least.

### The design that made this visible at all

The producer writes `unmapped:<raw>` rather than dropping the row or guessing a mapping.
**Fail-visible, not fail-silent** -- the raw vendor type survives into gold where a reader can
count it. Had it mapped Daily Accrual to `cash_div` to keep the enum clean, this would be
invisible and wrong. Recorded as the good pattern it is.

## Scope I did not cross

- **TR-HELD (123,933 cells)** stays out. The issuer routed it to the CTO; it is not mine to take.
- **No rollback delete** of either artifact -- the order reserves that to Andrew.
- **I did not file the surprise row myself.** This seat is read-only outside its own
  `logs/`/`threads/`/`deliverables/`, so the row is ASKED of the issuer and CTO~Z. Per my own
  banked lesson, a relayed row records the FILER in `surfaced_by`, never the observer -- so if it
  lands it will carry their serial, and that is correct.

## Watcher continuity across this work

Teams watcher exited **124** (its own `timeout 1770`, by design, not a failure). Censused
`teams-watch.py` rows = 0 and `timeout.exe` rows = 0 **before** re-arming, because 0 reads as
"arm one" and a stale row would have stacked two watchers on one cursor. Re-armed pid **43364**,
receipt `identity=517aa5ee-... channels=1` -- both required values present. Backlog sweep
`poll_addressed_teams_messages` since 04:00Z returned **0**: the seat was not deaf during the gap.
