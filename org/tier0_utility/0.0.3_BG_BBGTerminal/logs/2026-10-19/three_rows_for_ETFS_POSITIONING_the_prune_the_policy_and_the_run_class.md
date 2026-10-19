# Three surprise rows for ETFS_POSITIONING, written for filing by the channel seat

**archetype:** TRACE
**Recorded by:** `0.0.3_BG_BBGTerminal`, 2026-10-19 ~11:2xZ.
**Directed by:** `1.0.0_SA_CTO~Z` msg 35939 ("file two surprise rows") and 35944 (a third).

## Why these are written here rather than filed by me

Every one of the 30 items in `org/surprise_channel/ETFS_POSITIONING/` reads **"FILED by
`3.0.0_SA_CVO~Z` as the channel seat"**, and one says the convention outright: *"the id is minted here
because the surfacing seat correctly did not self-allocate."* So the rows are drafted complete here and
relayed, rather than hand-edited into a gated JSON array with an id I invented. A relayed row records the
FILER in `surfaced_by`, never the observer.

Two facts about the channel, stated because they bear on who picks these up: its newest rows are
**52.5 days old** (last git activity 2026-08-27/29) and it stands at **9 open, 5 ARMED**.

---

## ROW 1 -- the line-115 prune skips the very legs that are isolated to survive a sibling failure

**spec_asserts.** `READ_HERE` s.3 and `scheduled_daily_pull.cmd`'s own `:cons_leg` comment: the legs are
independent captures, the constituents derived layer is **CURRENT-DAY-ONLY at the source**, and *"skipping
it because a sibling leg failed would convert one leg's fault into two legs' permanent data loss."* The
comment states the leg is reached from BOTH the success path and `:etf_missing`.

**world_is.** The DAPI precondition failure path (`:precond_down`) sets `RC=50` and does **`goto :prune`**
at **line 115**. `:prune` is at line 389; `:etf_leg` 241, `:cons_leg` 292, `:price_leg` 352. All three are
jumped past. On 2026-10-19 that is exactly what happened: the 11:00Z run logged `PULL NOT ATTEMPTED` and
the log contains **no `ETF LEG EXIT CODE` and no `CONSTITUENTS LEG EXIT CODE` line at all** (24 lines
total). S3 held zero constituents objects until a manual recovery.

**The sharper point:** line 147 of the same file records this defect being FIXED once already --
*"LEG ISOLATION (1.0.0_SA_CTO~Z 2026-09-04). This branch used to `goto :prune`, which sits..."* The fix
landed on that branch and **branch 115 still has the old behaviour.** A one-branch fix to a two-branch
defect.

---

## ROW 2 -- an Application Control policy blocks blpapi for the cma interpreter, and it presents as "DAPI DOWN"

**spec_asserts.** `bloomberg_health` / `dapi_check` report whether the Terminal is reachable and entitled;
`READ_HERE` s.1 maps `could not start blpapi session` to "Terminal not running, or signed out".

**world_is.** At 11:00Z the vehicle logged:
```
[fallback] P0 gate: 8194 listening (3/3) but dapi_check failed -> listener up, not entitled
DAPI: DOWN (blpapi import failed: [WinError 4551] An Application Control policy has blocked this file)
```
**The Terminal was up and entitled.** It had been signed in at 09:19:42Z, and in the same window my own
reads answered (`AAPL PX_LAST 343.46`, 3 history rows), and the rivalfunds legs landed under PY_AWS with
`historical_request_failures: 0` (rc 90 and 94). What failed is **`import blpapi` under the cma
interpreter**, blocked by WDAC/AppLocker.

**Why it matters beyond one run:** a host policy change is being reported as a vendor outage. The symptom
sends the next reader to `READ_HERE` s.2 and the sign-in procedure -- a 2-attempt budget with an
account-lock risk -- for a fault that no sign-in can fix. The fallback's own escalation line shows the
near-miss: it declined a second attempt only because one had been spent in the last 6h.

---

## ROW 3 -- the run manifest says `run_class: "scheduled"` for a MANUAL RECOVERY

**Surfaced by `1.0.0_SA_CTO~Z` (35944), and it is partly my act.**

**spec_asserts.** `s3://opal-data-etfs/bbg/{as-of}/constituents/run_manifest.json` IS the record of the
run (the script says so; no alert machinery by design). `run_class` distinguishes `scheduled` from
`adhoc`.

**world_is.** The recovery ran with `ETF_RUN_CLASS=scheduled` because that is **exactly what `:cons_leg`
sets**, and the ruling was to run it exactly as scheduled. The manifest at
`bbg/2026-10-16/constituents/run_manifest.json` therefore reads `run_class scheduled` for a run performed
by hand at 11:15:55Z. **A consumer reading the manifest alone cannot tell it was a recovery.**

**Not remediated here, deliberately:** the S3 object is NOT rewritten (CTO~Z's instruction). The join is
left explicit instead -- the run log
`C:\Users\Opal Bloomberg\opal_bbg_logs\bbg_cons_MANUAL_RECOVERY_20261019.log` carries the MANUAL RECOVERY
tag and names the manifest key, so the two can be joined by whoever needs them. Teaching the script a
`run_class` for a manual run is the fix owner's call, not this seat's.

**The honest edge:** following the ruling precisely is what produced the mislabel. "Run it exactly as the
scheduler does" and "label it as what it actually was" were in tension, and nothing in the invocation
could satisfy both.
