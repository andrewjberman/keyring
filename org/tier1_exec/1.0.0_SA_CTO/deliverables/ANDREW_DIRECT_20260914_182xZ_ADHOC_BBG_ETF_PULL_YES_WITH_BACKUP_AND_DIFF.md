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
