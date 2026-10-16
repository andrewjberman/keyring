# Daily guardrail 2026-10-14: CLEAN on the first run, the pre-flight held, and a nested PARTIAL that is now 2-for-2

**archetype:** VALIDATE
**secondary_archetypes:** DIAGNOSE (the enrichment naming partial)

Companion to `preflight_0402Z_dapi_entitled_7h_before_the_1100Z_pull.md`, which measured the
precondition seven hours early. This is the owed read after the run.

## 1. THE RUN: clean on the first attempt, no backstop needed

`OPAL_BBGTML_daily_pull` fired **11:00:01Z** and the task returned **rc=0**. Log
`bbg_tplus1_20261014_070001.log` (15629 bytes, 183 lines), every leg read:

| leg | exit |
|---|---|
| precondition | **PASS -- DAPI UP, an entitled session answered a real refdata request** (`[fallback] DAPI UP -- proceed with pull, no sign-in needed`) |
| models pull | `0` |
| publish | `0`, **vintage 20261013 (2026-10-13)** |
| ETF L1 | `0` |
| constituents | `0` |
| price | `0` |
| rivalfunds collector | `90` -- landed, batch whole, marker written |
| rivalfunds enrichment | `94` -- landed |

**The 04:02Z pre-flight held.** Yesterday this exact precondition failed (`rc=4`, submit aborted
pre-click) and cost a backstop summons plus a 14:32Z recovery. I measured the session entitled at
04:02Z and said a ~7-hour hold to 11:00Z was inside observed behaviour; it held, and the log's own
line is the confirmation -- *no sign-in was needed*, so the sign-in path that broke yesterday was
never entered.

## 2. SECOND INSTRUMENT, by content -- because rc=0 is a self-report

Calendar resolved on the one frontier first (`lib/trading_calendar.py`): today Wed 2026-10-14 is a
trading day, `prev_trading_day = 2026-10-13` (Tue), so **T-1 today IS 2026-10-13** and the published
vintage matches it exactly.

`freshness_check.py` re-run read-only at **11:19:47Z -> PASS**:
`data_as_of=2026-10-13 expected_frontier=2026-10-14 trading_days_behind=1`, **series graded=10, every
graded series ends ON `data_as_of`.**

⚠ The `OPAL_BBGTML_freshness_check` TASK record still reads `rc=2` from **yesterday 11:30Z** -- its
own fire today is at 11:30Z and had not happened at the time of this read. **Same stale-task-record
trap logged yesterday:** the task result is a log line, the artifact is the state, and the artifact
says PASS.

## 3. ⚠ THE FINDING: a PARTIAL nested inside an OK leg, now measured on TWO consecutive days

Yesterday I surfaced this as a one-off and wrote that *"a PARTIAL nested inside an OK is the shape
that gets lost."* **It recurs today, identically, and two points make a line.** The rivalfunds
enrichment leg exits `94 -- landed` both days while its `names` sub-object reads `"status":
"PARTIAL"`:

| `names.detail` | 2026-10-13 | 2026-10-14 |
|---|---|---|
| candidates | 47 | **44** |
| already_named | 39 | **36** |
| asked | **8** | **8** |
| named | **0** | **0** |
| written | false | false |
| reason | "the fetch returned no usable name" | identical |

**Asked 8, named 0, two days running.** A single day's reading cannot tell a flaky fetch from a
broken one; **two identical days can, and this is the stable kind.** The leg reports "landed" each
time and nothing above it says otherwise.

**The arithmetic also says what moved and what did not.** `candidates` fell 47->44 and
`already_named` fell 39->36 -- **both by exactly 3, so the three that left the universe were all
already-named ones.** The unnamed gap is `47-39 = 8` and `44-36 = 8`: **unchanged.** So the drop is
universe churn, not progress, and nothing has been named in the interval.

**Not mine, and not acted on:** the rivalfunds legs belong to ETFS_RIVALS, and its S3 manifest is the
record by design. **What is new is the 2-for-2, which no single run could establish** -- that is the
part worth routing, because a stable 0 and a flaky 0 want different fixes.

### Also recurring, and NOT a fault: the constituents entitlement boundary

Line 142, inside a leg that exited `0`: `DIVZ`, `IDVZ`, `PFDE`, `PFOE` all `refused:entitlement` --
**the same four as yesterday.** This is the known no-BQL enumeration boundary
(`integrations/bloomberg/READ_HERE.md` section 4), an entitlement fact rather than a defect, and
stable across both days.

⭐ Worth knowing for serving, since it crosses two surfaces: **`PFDE` is in that refused list, yet
`bloomberg_reference_data` for PFDE answered fine yesterday** (28.37 / 28.5044 / 2026-10-12, served
to Andrew at 19:45Z). **Constituent ENUMERATION and single-security REFERENCE reads are different
entitlement surfaces**, so a refusal on one says nothing about the other -- and reading the refused
list as "we cannot get PFDE" would have been wrong.

## Compiler Tools

| tool | result | read |
|---|---|---|
| `Get-ScheduledTaskInfo` on both tasks | pull `lastrun 11:00:01Z rc=0`; freshness `lastrun 10/13 11:30Z rc=2` | The pull row is today's and usable. The freshness row is YESTERDAY's and is not evidence about today -- checked the clock before reading it as stale. |
| pull log, all 183 lines scanned for verdicts | 8 legs, all green | Denominator printed. Grepped for verdict tokens rather than slicing positionally. |
| `lib/trading_calendar.py` | `prev_trading_day(2026-10-14) = 2026-10-13`, behind=1 | Resolved BEFORE judging the vintage, per NEVER#1. |
| `freshness_check.py` (read-only) | **PASS**, 10 series, all ending on `data_as_of` | The content instrument. Chosen over the task's rc, which was yesterday's anyway. |
| nested-partial sweep (`status`/`reason`/`refused`/`written` regex) | 1 PARTIAL, 4 `refused:entitlement`, both recurring | **This is the sweep that found section 3.** A per-leg exit-code read alone reports 8-for-8 green and misses both. |

## Blockers

- **Nothing blocked on me for the pipeline.** Today's data is served and healthy at T-1 on the first
  run; no fallback, no escalation.
- The enrichment naming PARTIAL wants an owner at ETFS_RIVALS. **I cannot file its surprise row
  myself** -- my writable set is `logs/`, `threads/`, `deliverables/` and tmp, so the channel path is
  outside it. Routing to `0.0.0_AB_MSTR~Z` to carry or forward.
- Unchanged: 3 Teams items plus Alyssa's detail on Andrew's word; Graph TTL fix his; Z6 R5 draining
  under COO~ZB; the two serving-path fixes with CTO~Z; `bg-concierge-gate.sh` unwired with CTO~Z.
