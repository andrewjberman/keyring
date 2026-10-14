# FB-j-3 -- the issuer's own read of the first BD gold chain after the text-only dispatcher deploy (2.0.0_SA_COO~B1, 2026-10-14 ~01:3xZ)

Read-only, from dell1. This is the issuer's measurement; `0.7.0_AE_CloudOps~FB1` owns the order and writes the order's record (`EMIT_ERROR_TEXT.json`). The issuer reads it too because FB-j-4's
cut depends on the cause, and a cause is taken from a measured text, never from the hypothesis.

| item | value |
|---|---|
| deploy read against | the text-only dispatcher, `s3://opal-data-bd/code/gold/gold_dispatch.sh`, deployed 2026-10-13T08:37:35Z (FB-j-3, FB1) |
| chain | the nightly BD gold chain started about 2026-10-13T23:03Z (runner telemetry A_00/A_02 at 23:03Z); `gold/logs/chain_full_20261013_230043.log` written 2026-10-14T01:14:38Z |
| log read | `s3://opal-data-bd/logs/gold-layer/gold_incremental_2026-10-14_20261014_012024.log` (664,863,477 bytes, LastModified 2026-10-14T01:20:26Z); the cumulative log, whose last lines read `SHUTDOWN_ARMED chain=chain:full` and `=== COMPLETE (exit code: 0) ===` at 01:20:24Z |
| the line (line 6,927,647 of 6,927,916) | `  WARN: EventBridge chain-complete put-events failed (non-fatal to chain close): rc=255 You must specify a region. You can also configure your region by running "aws configure".` |
| class | `NO_REGION` (a "must specify a region" class text, rc=255) |
| vintage test | the five earlier WARN lines in the same file carry the OLD text (no `rc=` and no CLI text); only this line carries the new format, so it was produced by the deployed text-only dispatcher, not an older copy |

What it settles: the put-events call fails BEFORE any API call because the CLI has no region; the hypothesis (REGION_UNSET) is now a measurement. No PutEvents reached EventBridge from this chain, so
`exec-summary-trigger` did not fire (consistent with CloudTrail holding no PutEvents).

What it does not show: that adding `--region "$EVENTS_REGION"` makes the runner's call succeed (the first chain after the fix deploy shows that; FB-j-7); nothing here is a fix.

Consequence: `FB-j-4` is un-parked as cut (the cause is the one it was cut on). Its merge is not a deploy; the deploy stays `FB-j-7`'s, after the sample read and both halves of the first-regeneration pair (the pair is signed; FB-j-7 also needs FB-j-4 merged and PASS).
