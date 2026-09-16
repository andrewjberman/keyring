# ANDREW-DIRECT 2026-09-14 ~18:2xZ (~2:2x PM ET) -- the one-off Bloomberg ETF pull today: YES, with backup and diff

**Received at:** the `1.0.0_SA_CTO~Z` terminal, in-session. **Recorded by:** `1.0.0_SA_CTO~Z`, same turn.

## HIS WORDS -- VERBATIM AND ENTIRE

> "I have no issue with this, go ahead, yes with backup and diff"

## WHAT HE WAS ANSWERING (as put to him by this seat)

After his ~18:1xZ question on call 2, this seat explained that a same-day ad-hoc run of
`integrations/bloomberg/pipeline/etf_daily_pull.py` lands under `bbg/2026-09-11/` in `opal-data-etfs`, the keys the 07:00
ET scheduled run already wrote:
- `history_topup` and `fund_daily` for 09-11 are closed-day values and should re-pull identical;
- `characteristics` is a live ReferenceDataRequest snapshot, so all 170 securities' values move from the morning to the
  afternoon, not only two data points added;
- the manifest relabels the partition `run_class=adhoc`;
- the ETF gold run reads that partition and would serve the afternoon values.
The option offered: back up the current objects locally, run the pull, print what changed beyond GLD/VXX, restore the
saved objects if anything looks wrong. **"yes (with that backup and diff) or no?"**

## READING

This is his per-use word for ONE download-class Bloomberg ETF pull today (CLAUDE.md: vendor egress needs his explicit
per-use word), under the stated controls: a local backup of every object under `bbg/2026-09-11/` taken BEFORE the run,
a diff after, and a restore by re-uploading the saved bytes if the diff shows a problem. No S3 delete is part of it.
Executed by `1.0.0_SA_CTO~Z` (lane `ANY_EXEC_OR_AE` for `integrations/**`; the script is already on disk at `ac3e03a317`).
It closes call 2 of the ~18:1xZ `/open-calls` frame.

## OUTCOME -- executed 2026-09-14 by 1.0.0_SA_CTO~Z

**Sign-in.** `bloomberg_health` first read `ok:false` twice (port 8194 not listening; `bbcomm` restarted 2:22 PM ET, no
Terminal UI). `0.0.3_BG_BBGTerminal` confirmed it restarted nothing and no sign-in was in progress (msg 22898). Andrew then
signed in himself, VERBATIM: *"I signed in to bloomberg, go ahead."* Health read `ok:true`, 8194 listening, `wintrv`
up at 2:28:56 PM ET.

**Backup (before the run).** The prefix `bbg/2026-09-11/` in `opal-data-etfs` is UNVERSIONED (`VersionId null`), so the
local copy is the only restore path. All 7 objects the pull writes were downloaded; each local md5 equals its S3 ETag.
Location: this seat's session scratchpad, `bbg_backup_20260911/` (session-local, not in the repo).

**The run.** `Python311 etf_daily_pull.py`, `ETF_RUN_CLASS` unset, 18:30:27Z-18:31:18Z, **exit 0**, 7 of 7 objects
written, 0 failed. Universe 172 = 166 constituents + 4 funds + 2 extra securities (GLD, VXX).

**The diff (07:00 ET scheduled bytes -> ad-hoc bytes)** -- by a script first run against the backup versus itself, which
printed zero changes on every file:

| object | result |
|---|---|
| `fund_daily.*` | **byte-identical** (same ETag) |
| `history_topup` | **+2 rows** (GLD and VXX for 2026-09-11); **0 values changed** on the 169 existing rows |
| `run_manifest.json` | `extra_securities` added, `run_class` scheduled -> adhoc, universe 170 -> 172, rows +2, `vendor_observations` +GLD +VXX, 0 existing counts changed |
| `characteristics` | **+2 rows** (GLD, VXX). Existing 170: `CUR_MKT_CAP` changed on 165 (median -0.04%, p10 -4.3%, p90 +2.7%, 2 above 10%), `EQY_DVD_YLD_IND_NET` changed on 135 (median -0.15%, 2 above 10%), `FUND_TOTAL_ASSETS` on 1 (negligible); every other field unchanged; 0 null/value flips |

**Assessment: nothing wrong as data, so NOT restored.** The market-cap and yield changes are price moves. The largest
movers are the same securities in both fields, and the yield change is the inverse of the price change. Corning: cap
-12.51%, yield +14.29%, and 1/0.8749 = 1.1429. Nokia and Lam Research pair the same way.
The one semantic shift, disclosed: the 07:00 ET run pulled before the open, so those two fields reflected Friday's
close, matching the 09-11 label; the ad-hoc run reflects Monday intraday under the same label. This lasts until
tomorrow's 07:00 ET scheduled run writes `bbg/2026-09-14/`. Restore = re-upload the 7 backed-up files (overwrite, no
delete), available on Andrew's word while the scratchpad copy exists.

**Card-4 ledger `posn-bbg-etf-pull-gld-vxx`:** L2 stays OPEN. Its proof requires the scheduled fire
(`run_class=scheduled`); this ad-hoc run exercised the same code path first.
