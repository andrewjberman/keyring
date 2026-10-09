# ANDREW-DIRECT 2026-10-09 ~00:4xZ -- at the `0.0.0_AB_MSTR~Z` terminal (site Z)

Answering `0.0.0_AB_MSTR~Z`'s three open items (Bloomberg seat `--strict-mcp-config`; the puller's end state after the
2026-10-09 07:00 ET pull; the opal-gateway-bbg sign-in).

## His words, verbatim

> 1.) Don't care, this should all be adjudicated by the CTO internally. 2.) Whats the difference? 3.) I have done this
> over and over again, why does it keep losing connection?

> Gateway is signed in, why did you ask this?

## What was measured and done on them, by `0.0.0_AB_MSTR~Z`

1. **`--strict-mcp-config` for `0.0.3_BG_BBGTerminal`:** passed to `1.0.0_SA_CTO~Z` to adjudicate (site-Z seat config).
2. **The puller:** the working copy of `integrations/bloomberg/pipeline/etf_daily_pull.py` differs from trunk by 15 lines,
   dell1's SH-t-4 run-record block (19e50528d3). It logs the backfill-budget remainder after the run and changes neither
   the data pulled nor the exit code. The one-shot task `OPAL_restore_etf_daily_pull_20261009` restores trunk at 08:00
   local. Answered at the terminal; no act taken.
3. **opal-gateway-bbg:** measured 00:4xZ in `~/.claude/.credentials.json` without printing values: an access token
   (expired 00:35Z) and a refresh token are both present, so it is signed in and renews on use. The sign-in was asked of
   him on a relayed claim (`1.0.0_SA_CTO~O` msg 32075) that this seat did not measure. The ask is withdrawn and the
   carrier corrected.
