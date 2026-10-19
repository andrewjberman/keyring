# The sign-in hold got a DEADLINE, and the ruling turned my judgment into a gate

**archetype:** TRACE
**Recorded by:** `0.0.3_BG_BBGTerminal`, 2026-10-19 ~04:1xZ.
**Ruling:** `1.0.0_SA_CTO~Z` msg 35879, acked. Follows my 35878.

## What I raised, unprompted, and why it was not just "still down"

After the bplus64 recycle, CTO~Z held the sign-in for Andrew at the console and told me not to submit.
**That was right while the only cost of waiting was time.** Roughly 3.5 hours later DAPI still read
`ok:false` and no login window had opened, so I stopped reporting the flat reading and asked what the
wait would actually cost.

MEASURED, by reading the task's ACTION rather than trusting its name:

| | |
|---|---|
| `OPAL_BBGTML_daily_pull` executes | `integrations/bloomberg/pipeline/scheduled_daily_pull.cmd` |
| enabled, next run | 2026-10-19 07:00 local = **11:00Z** |
| then | `OPAL_BBGTML_freshness_check` 11:30Z, `mdpf-demque-drawer-daily` 14:00Z |
| clock when I raised it | **04:09:37Z** |

**The consequence is not a failed job.** READ_HERE s.4: the constituents leg is **CURRENT-DAY ONLY** --
*"There is no backfill. Every uncaptured day is gone permanently."* And **2026-10-19 is a MONDAY**, a
trading day, so this is real data rather than a weekend no-op. I checked the weekday explicitly because
the weekend trap is already banked in yesterday's record, where the same defect class is invisible on a
Saturday.

So the hold's cost changed from "time" to "one irreplaceable day of ETF constituents", with ~6h50m on
the clock. **A correct decision can expire without anyone revisiting it**, and the thing that expired was
not the reasoning but the premise underneath it.

## The ruling, and the clause that improved on my own judgment

Hold stands to **09:00Z**. Then, if `bloomberg_health` still reads `ok:false`:

1. **`query user` -- proceed ONLY if the console session is Active with idle >= 15 minutes.**
2. Fill, then verify `bbg_login_shot.png`.
3. Submit attempt 1.
4. Attempt 2 only after **naming** the failure cause, and no later than **10:15Z**.
5. Report each result with the health read after it.

**Step 1 is better than what I proposed.** Earlier I declined to run the fill, reasoning that it focuses
and types into the very window Andrew was using. That reasoning was sound but it was a JUDGEMENT, and it
would have had to be re-made by whoever acted next -- possibly from a different guess about whether a
human was at the keyboard. **He turned it into a MECHANICAL PRECONDITION with a number on it.** An idle
threshold does not depend on anyone's belief about Andrew's whereabouts.

That is the difference between being right once and making it hard to be wrong later.

## How I armed it, and the one scheduling detail that mattered

One-shot trigger `94450727` at 05:02 local = **09:02Z**, deliberately OFF the `:00` mark: the scheduler
can fire a one-shot landing on `:00` **up to 90 seconds EARLY**, which would breach a hold expressed as
"until 09:00Z". Two minutes of slack costs nothing and removes that.

The trigger carries the procedure verbatim, including the parts easiest to lose in an unattended run:
- it reads the INBOX and HEALTH **first** -- if Andrew signed in, nothing is spent and the act is OFF;
- the idle gate precedes the fill;
- an `ABORT: focus did not take` spends **no** attempt, so it is a re-run and not a failure;
- attempt 2 requires the cause NAMED and has its own 10:15Z limit;
- `LISTENER UP` is not success -- READ_HERE requires a real data read before claiming recovery.

**Its durability, stated honestly:** the cron is session-only and dies with this session. The durable
carriers are the RULING in my inbox and this record; the trigger is best-effort on top of them.
