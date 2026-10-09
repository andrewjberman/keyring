# HANDOFF -- the Bloomberg served-data staleness gate: what it checks, and the class it cannot see

**Written** 2026-10-07 ~05:3xZ by `0.0.3_BG_BBGTerminal` at Andrew's ask, for an agent to check out.
**Subject** `integrations/bloomberg/pipeline/freshness_check.py` (228 lines) + its wrapper
`freshness_check.cmd`. Scheduled Task `OPAL_BBGTML_freshness_check`, 07:30 ET daily, i.e. cron+30
after the 07:00 pull. Read at HEAD; cite by path and line, and re-print the bytes before quoting.

---

## 1. THE PREDICATE -- one field, one integer, two thresholds

It reads **exactly one value**: `data_as_of` from the BODY of
`s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json`
(`:47` BUCKET, `:48` SERVED_KEY), and resolves it against the trading calendar:

```
:190  expected = expected_last_trading_day(today)
:202  behind   = trading_days_behind(as_of, expected)
:209  if behind <= 1:  PASS, exit 0
      else:            STALE -> SUMMON, exit 2
```

Contract in its own header, `:10-21`. **`lib/trading_calendar.py` is the one frontier definition.**

**It is NOT a mixed-figures or cross-field comparison.** Nothing in the file compares two figures
against each other, or any figure against a prior run's value. There is one date and one threshold.

### Measured verdicts (my run, against frontier 2026-10-07)

| served `data_as_of` | `behind` | verdict |
|---|---|---|
| 2026-10-07 | 0 | PASS |
| 2026-10-06 | 1 | PASS |
| 2026-10-05 | 2 | STALE -> summon |
| 2026-10-02 | 3 | STALE |
| 2026-09-29 | 6 | STALE |

**T-1 is the healthy state and passes by design.** `<= 1`, deliberately not `== 1`: the header
(`:15-18`) records that a Saturday pull yields Friday data against a Friday frontier = behind 0,
"fresher, never stale", so `== 1` would false-summon every weekend and a CALENDAR-day subtraction
would false-summon every Monday (CLAUDE.md NEVER#1).

## 2. THREE summons kinds, not one

| kind | trigger | exit | note |
|---|---|---|---|
| `STALE` | `behind >= 2` | 2 | the staleness verdict proper |
| `CHECK-ERROR` | the S3 read itself threw | 3 | `:196-201`. Explicitly labeled an INSTRUMENT error, NOT a staleness verdict -- "a checker that cannot check and stays silent is the absent-check class" |
| `SCHEDULE-GAP` | previous log stamp > 26h old | (no early return) | `:162-188`, a RAN-AT-ALL self-check. In a pure event design PASS and NEVER-RAN are both silence; this makes the second one speak. Note `:188` deliberately does NOT return -- today's freshness verdict still renders after it |

Summons legs (`:106-142`): append `C:\opal-elev\freshness_ESCALATION.txt`; write fabric inbox files
to `0.0.3_BG_BBGTerminal` AND `0.0.0_AB_MSTR/~Z`; then a process-truth scan -- BG live, the inbox IS
the summons; BG down, spawn the seat via `.tools/spawn-agent.ps1` with the summons as first message.

## 3. >> THE FINDING FOR THE CHECKING AGENT: the gate is BLIND TO CONTENT

**A fully-empty benchmark table with a current date passes cleanly.** This is not a hypothesis; it
happened for roughly nine hours on 2026-10-06 and no gate spoke.

Measured, both halves:
- At served `generated_at 2026-10-06T16:16:50Z` the artifact carried **`index_benchmark` null 50 of
  50, `index_spread` 50/50, `etf_benchmark` 40/50 -- 288 of 450 return cells null.**
- The SAME artifact carried `data_as_of 2026-10-05`, which against that day's frontier is
  `behind` 0-1 -> **PASS**.

So the checker would have reported fresh throughout, correctly by its own contract. The defect was
found only because nulls were counted in the artifact by hand. **The gate watches the DATE, never
the NUMBERS** -- and `data_as_of` is written by the producer alongside the broken cells, so it moves
whether or not the content is sound.

Related, same root: `publish_to_portal.py` GATE 3 (`:161-168`) skips on DATE EQUALITY alone, so it
could not republish a corrected same-date vintage either. **Three layers -- the notebook's
`if os.path.exists(pkl_data)`, the publisher's GATE 3, and this checker -- all treat a DATE as
identifying its CONTENT.** That shared assumption is the subject worth examining, not this one file.

## 4. HOW TO VERIFY SAFELY -- handles that touch nothing

- **`--verdict-only AS_OF [TODAY]`** (`:146-157`): computes the verdict for given operands with
  **no S3 read and no summons**. The calendar limb in isolation. Exit 0 PASS / 2 STALE. Use this
  first; it is the cheap, side-effect-free exercise.
- `--test-stale` (`:203-206`): injects `behind=99` to force the STALE path. **It DOES summon** --
  pair it with `--dry-summon`.
- `--dry-summon`, `--simulate-seat-down`: exercise the summons legs without the real spawn.
- Log: `C:\opal-elev\freshness_check.log` (`:49`). The task's own state:
  `Get-ScheduledTaskInfo -TaskName OPAL_BBGTML_freshness_check` (LastRunTime / LastTaskResult /
  NextRunTime). Print the total task count beside it as a denominator -- 208 on this box.

## 5. WHAT I VERIFIED vs WHAT I DID NOT -- do not inherit my coverage

**Verified by reading the bytes / running the code:** the predicate and both thresholds; the
constants at `:47-48`; the three summons kinds; the verdict table above (run against
`lib/trading_calendar.py`); the content-blindness claim (both the null counts and the concurrent
`data_as_of`).

**NOT verified -- open for you:**
1. I read **23 of 228 lines** via `comp-read` plus targeted `sed` ranges. **I did not read the file
   end to end.** The SCHEDULE-GAP limb (`:162-188`) and `summon()` (`:106-142`) I read only in part.
2. **I never exercised the STALE path, the CHECK-ERROR path, or any summons leg.** My only
   evidence that the summons works is that one arrived in my inbox at 2026-10-06 11:30Z. That is
   one observation of one leg (inbox write, seat live), not the spawn leg.
3. `expected_last_trading_day` across market HOLIDAYS: the header claims the calendar handles them;
   I confirmed only Tue/Wed behaviour. A holiday-boundary `--verdict-only` sweep is cheap and unrun.
4. Whether `SERVED_KEY` is the right single witness. **Beware: there are TWO served artifacts** --
   `json/benchmarks/model_portfolio_benchmarks.json` (this gate's key, and the publisher's) and
   `json/latest/manifest.json`. They carry DIFFERENT `generated_at`. I spent hours on 2026-10-06
   quoting the wrong one; re-reading the same wrong source four times is not corroboration.

## 6. GUARDRAIL -- read before proposing anything

**CLAUDE.md standing moratorium: NEVER build an alert / alarm / SNS / SES-send / notification /
freshness-checker / monitor unless Andrew explicitly asks.** This file is a conditional SUMMONS and
is `# andrew-asked 2026-08-20` (quoted in `freshness_check.cmd`), which is why it exists at all.
So: **characterise, do not build.** A content-level check (e.g. a null-count threshold) is a
PROPOSAL to Andrew, never an implementation. Proposing is legal; implementing is not.

Likewise do not edit `freshness_check.py` casually: **site-Z Scheduled Tasks run the WORKING TREE**,
so an edit to this file IS a deploy the moment it touches disk (`READ_HERE.md` section 3).

## 7. LIVE STATE at writing

Served `data_as_of 2026-10-05`; frontier rolled to 2026-10-07 at midnight, so it currently sits at
`behind 2`. The 07:00 run targets 2026-10-06. If it lands, 07:30 reads behind 1 -> PASS; if it
fails, the gate fires STALE and summons -- which is the design working, not a fault.

Standing risk beneath that (my own logs 2026-10-06/07): **R1, click-coordinate drift in
`bbg_signin.ps1`, is unfixed**, and `bbcomm` has been holding the entitled DAPI session with
`wintrv.exe` ABSENT across 7 samples. That MASKS R1 rather than fixing it. If the session did not
survive the night, 07:00 fails the way it did on 10-06.

**Owner of this file:** not me -- I hold no git lane and `integrations/bloomberg/` is outside my
write fence. Findings route to `0.0.0_AB_MSTR~Z`.
