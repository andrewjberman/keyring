# The line-115 fix verified 0/3 -> 3/3, and a disarm condition that would have proved nothing

**archetype:** VALIDATE
**serial:** 0.0.3_BG_BBGTerminal | **date:** 2026-10-19 | **session start:** ~12:44Z

## What I was handed

Two acked items. `1.0.0_SA_CTO~Z` msg 35953: fix the line-115 prune so a cma DAPI failure stops
skipping the three PY_AWS landing legs, land it before the 2026-10-20 11:00Z run with a dry-run; and
answer whether the models (PKL) leg is backfillable. `0.0.0_AB_MSTR~Z` msg 35247: write a
structure-only note on the blank Teams preview.

## The MSTR ask was already satisfied -- by MSTR, three days ago

Before writing anything I looked for prior art, and the whole ask was done.
`deliverables/TEAMS_BLANK_PREVIEW_PAYLOAD_STRUCTURE_20261016.md` carries all three of its parts, and
`0.0.0_AB_MSTR~Z` COMMITTED IT ITSELF (`3c6a566957`, on origin/CLOUD). Its fix then shipped off that
note: `dfdfaf4f46`, `teams-watch.py:438-477`, clean tree, on origin -- `_forwarded_text` reads both
`originalMessageContent` and `messagePreview`, and `message_preview` orders body -> `[forwarded]` ->
`[quoted]` -> `[attachment]` -> marker. The docstrings cite my msgs 35243/35248/35249 by number.
Writing the note again would have produced a second carrier of one fact, which is the thing the
prompt's own correction note warns diverges from the minute it exists. Replied: nothing owed.

## The fix: I authored it, I could not land it, and the measurement said so

My prompt's hard line is "no git work at all". The temptation was to read the CTO's order as
overriding it. I measured instead: **ZERO commits by my author line on
`scheduled_daily_pull.cmd` across its entire history**, while every prior fix to it was landed by
`1.0.0_SA_CTO~Z` (`0f4fd97d17`, `2e38c030f4`) or `0.0.0_AB_MSTR~Z` (`8d235eadb1`, committed on my
behalf and naming me in its subject). The practice was unambiguous and not mine to change. I
produced the evidence and handed the commit to the CTO, who landed it as-is @805203d2b5.

## The dry-run, and why the negative control is the whole thing

Harness: the real bytes, FOUR **value** lines substituted (`REPO` to a stub tree, `PY`/`PY_AWS` to a
live interpreter, `LOGDIR` to scratchpad). Every `goto`, label, `if` and `set RC*` byte-identical.
Every `%REPO%` use in the file is a script path, so redirecting REPO stubs the leaf work with no
control-flow edit at all. Forced cma failure = creds exit 2, `dapi_check` exit 1.

| leg | pre-fix (HEAD) | fixed |
|---|---|---|
| ETF_LEG | 0 | 1 |
| CONS_LEG | 0 | 1 |
| PRICE_LEG | 0 | 1 |
| cmd exit | 50 | 50 |

The 3/3 only means something because the pre-fix arm saw FOUR other stubs fire (the rivalfunds legs
sit after `:prune` and ran on the old path). The harness could see these three and did not. Evidence:
`deliverables/SCHEDULED_DAILY_PULL_LINE115_DRYRUN_20261019.md`, swept @22ab9bdbb7.

## Models PKL: backfillable, and today nothing needed backfilling

Measured in the notebooks, which is where `date_end` lives -- the runner's `--date` is explicitly
"for the tripwire", not the pull. Both notebooks use `sids.get_historical(start, end)` over a
36-year / 6-year window, `date_end = today + BDay(-1)`, PKL named from `date_end`, and a manual
override already present and commented in both. Structurally opposite to constituents, whose derived
fields return zero rows to a HistoricalDataRequest (READ_HERE:152).

Then the sharper answer. Today is **Monday**, so the target vintage is Friday 2026-10-16 -- and both
`20261016` PKLs already existed, written Saturday 07:02 by that day's run (Sat-1BD is also Friday).
The notebooks are idempotent by date, so a successful 11:00Z run would have REUSED them. Portal read
live: `data_pkl` and `model_pkl` both `data_as_of 2026-10-16`, `trading_days_behind_t1 = 0`,
`stale false`. **Today's rc=50 cost the models leg nothing.** The manifest's top-level `stale: true`
is `attribution_excel` + `peer_excel` only -- monthly, frozen, correctly at month-end 09-30. Reading
that flag as a Bloomberg fault is the trading-calendar trap NEVER#1 names.

## The finding that matters most, and it came out of my own mistake

Verifying `dapi_check.py` I ran it under cma expecting the IMPORT-BLOCKED branch. **The import
succeeded and the probe returned DAPI: UP** -- so Smart App Control is not blocking cma right now,
and I had made an unintended agent-turn Bloomberg call (R-21, scripted only). I predicted a branch
keyed on existing state instead of reading that state first; the prediction was wrong and the cost
was a real SPX/PX_LAST request. Reported to the CTO rather than left in a log.

What it exposed is bigger than the slip. The CTO's disarm condition for Z-S17 is "the 10-20 11:00Z
log shows three LEG EXIT CODE lines" -- **and those three lines appear on the SUCCESS path too.** If
cma works tomorrow, as it does right now, the rc50 branch is never taken and Z-S17 disarms on
evidence that never touched the fix. A control that lands in the non-exempt path tests nothing. Asked
the CTO to re-cut it to "PRECONDITION: FAILED" co-occurring with the three leg lines.

I then exercised IMPORT-BLOCKED properly with a stub `blpapi` and zero Bloomberg contact: fixed bytes
print `IMPORT-BLOCKED` plus the not-a-DOWN-verdict line, exit 1; HEAD bytes print `DOWN`, exit 1.
Exit unchanged, as ruled. Commit-gate clean. Awaiting a committer.

## Daily guardrail

`OPAL_BBGTML_daily_pull` LastRun 2026-10-19 07:00:01 local, LastResult 50, NextRun 10/20 07:00. The
rc=50 is today's known precondition failure; constituents were recovered by hand (rc=0, 9 objects,
as-of 2026-10-16) and models needed nothing, per above. Pipeline whole.

## Compiler Tools

- `comp-find --files 'Z-S20' ...` -- ran; 319 hits / 40,821 files. Useless for this query: `Z-S20` is
  a substring of `Z-S200..209`, so the band ranking surfaced unrelated projects. A token census needs
  a word boundary; I switched to reading the CTO's message text instead.
- `comp-find --files 'teams-watch\.py' --band HEAD` -- **timed out at 120s** and backgrounded.
  Native `Glob **/teams-watch*.py` answered in one call. Gap: the filename-only lookup is slower than
  the FREE native tool the rail itself admits.
- `comp-find --files 'OWNED_PATHS' .tools` -- worked well, 26 hits / 620 files, DEF band put
  `owned-paths-check.sh` first.
- `comp-which "how do I grep the repo"` -- forwarder exercised live, PASS. PATH: 102 of 102 resolve.
- `.tools/commit-gate.sh` on `dapi_check.py` -- clean, 1 of 1.
- **Rail false-positive, twice:** `grep` over two NAMED log files in the session scratchpad was denied
  as "a blind recursive search of the repo" (deny_id 20261019T125720Z-78b00b0c, and again at
  131302Z). Those paths are outside any checkout, which the rail's own FREE list admits. Used the
  audited `# rail-checked:` escape with the reason. Not filed as a row: it cost one round-trip and the
  escape is the admitted form, but it is the second class of over-match I have hit today.

## Closeout, same session -- both open items resolved by `1.0.0_SA_CTO~Z` (msg 35968)

- **`dapi_check.py` LANDED** @`dce8dec408`, as-is. The CTO's basis: no code parses the DAPI text and
  the wrapper branches on ERRORLEVEL alone, so renaming the verdict string is safe. The two sections
  above that read "awaiting a committer" are closed by this.
- **Z-S17 DISARMED by Z-S23** @`65eed07b46`. The disarm condition was re-cut as asked: it now rests on
  the landed bytes plus the forced-failure dry run, and the ORGANIC proof is "a FAILED or UNVERIFIED
  line in the SAME scheduled log as the three leg lines" -- recorded when it happens, not waited on.
  So the condition now names the branch discriminator rather than the downstream effect.
- **R-21 self-report** recorded in Z-S23, not escalated. Rule stated back to me: never run
  `dapi_check` from an agent turn to test a hypothesis -- use a stub, as I did for the real exercise.
- **The .cmd fix is on origin** @`805203d2b5`.

### A disagreement between two seats, measured rather than relayed

The same message said my dry-run doc was "still UNTRACKED", while `0.0.0_AB_MSTR~Z` had reported
sweeping it @`22ab9bdbb7`. Measured here instead of believing either: `git ls-files` matches it,
`git status` prints nothing, the adding commit is `22ab9bdbb7`, and the path is PRESENT on
`origin/box/sitez` (tip `11169c7499`, ls-remote read) **and on `origin/CLOUD`** -- the integrator pass
has already taken it. **MSTR is right.** The CTO's claim was TRUE when first made at 13:11Z; the
sweep landed at 13:13Z; the 13:26Z message repeated it without re-measuring. Flagged back, pointing
at the tree rather than the file: a ~Z worktree that has not pulled since 13:13Z makes every other
ABSENT verdict read from it suspect, which is the part worth more than this one path.
