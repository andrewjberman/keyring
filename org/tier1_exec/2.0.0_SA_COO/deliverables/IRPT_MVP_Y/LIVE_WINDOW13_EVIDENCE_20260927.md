# Window 13 (the Analysis chain, fifth attempt, resident `cw`): both window 11 fixes worked live; one setting value differs, and the re-capture met an unexpected screen

Author `2.0.0_SA_COO~Y`, 2026-09-27 ~14:4xZ. Packet blob `49ee40b0` (CTO @99311001d3, CRO @ce115a43f1). Word: Andrew at
~Y, "as many analysis attempts as needed" (@460e2ae8cb). Log: `LIVE_CHAIN_1203_20260927_W13.json` (scrubbed).

## The acts

| Time | Act | Answer |
|---|---|---|
| 14:12:36Z | login | 200 |
| 14:14:42Z | K4 upload | NORMALIZED at 14:14:44Z, input `portfolio_a61c028d..` |
| 14:14:48Z | K5 Overview | QUEUED, `REQ-2119def4de9e8fea43abb6fe`; portfolio 2363820 |

## The resident journal

1. **14:15:26Z** `STEP_WAF_REFRESH step=read_back status=202 source=status polls=3 wall_s=32.0`: the WAF challenged the
   3rd status GET again.
2. **14:16:02Z** `retained_for_retry ... CAPTURE_FAILED:UNEXPECTED_CHALLENGE`:
   - **`capture_env` worked live.** The runner ran for about 36 s, past its AWS calls and into the browser sign-in,
     with no `LEASE_NOT_HELD`.
   - The sign-in then met a screen the runner does not handle.
   - The runner names that screen with a closed reason (`CHALLENGE_CAPTCHA_UNSUPPORTED`, `CHALLENGE_WAF_INTERSTITIAL`,
     ...), but `failure_code` kept only the class. Fixed below.
3. **14:30:33Z** (redelivery, 15 min later) `STEP_REFUSED step=read_back status=200 portfolio_status=available
   source=saved_portfolio polls=1 drifted=level_as_of_type absent=-`:
   - **The saved-portfolio read works live.** All 7 fields are present, and 6 of 7 match.
   - Only `level_as_of_type` differs. The recipe sends `prior_close`, which is what the advisor's own UI sends in all 5
     captured creates (HAR evidence). The research worker never set or checked it.
   - What YCharts stores is not on record, because the journal logs names only.

## Measured pattern: the status poll and the WAF

The 3rd status GET is challenged in every multi-poll run: research at 5 s spacing, window 8 at 5 s, window 11 at 15 s,
window 13 at 15 s. The first status GET on a redelivery about 15 min later answered `available` with no challenge,
in both window 11 and window 13.

## Changes on the Y branch (@230999b568, @e8e5767b22) -> `P_W13_CHALLENGE_REASON_STORED_VALUE_20260927.patch`

The patch applies cleanly (apply-check rc=0) to P's `c6b66059ec`.

- `failure_code` appends the runner's closed `record.reason`, for example
  `CAPTURE_FAILED:UNEXPECTED_CHALLENGE:CHALLENGE_CAPTCHA_UNSUPPORTED`, so the screen is named next time.
- A drifted setting prints the value the vendor stored, as a closed token only: for example
  `drifted=level_as_of_type=<stored>`, `null`, or `?`. It never prints free text.
- Tests: test_host_capture 10/10, test_resident_main 7/7, test_read_back_poll plus test_resident_worker 41 passed and
  8 skipped; ruff clean.

## Decision for 1.0.0_SA_CTO: the poll design

- The evidence says polling itself triggers the challenge, so a 6-poll bound does not help: the 3rd poll is challenged
  whatever the spacing.
- A 15-minute wait worked twice.
- **REC:** at most 2 status GETs per delivery. If the portfolio is still `calculating`, the resident releases the
  message (retained, not ATTENTION), and the queue redelivers after its 900 s visibility timeout. The job resumes at
  the read-back checkpoint with no mutation replay, up to the queue's 5 receives.
- The re-capture then stays for a real eviction, not for a poll the job itself provoked.
