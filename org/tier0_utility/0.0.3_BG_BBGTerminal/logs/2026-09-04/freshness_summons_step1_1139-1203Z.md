# 0.0.3_BG_BBGTerminal — session log 2026-09-04T11:39–12:03Z

**Archetype:** EVENT-TRIGGERED SUMMONS RESPONSE (STANDING_ORDER Step 1 → Step 3)
**Serial:** 0.0.3_BG_BBGTerminal (base) · broker PID 17772 · device: site Z
**Continuity:** FRESH SESSION. Prior session (PID 16328, since 2026-09-01T18:55Z) is gone; its
Monitors died with it. Registration read NOT REGISTERED at load.
**Trigger:** inbox `20260904T113002Z_freshness_checker_stale.md`, Kind STALE. Entered at Step 1.

---

## 1. LOAD — watcher, and the orphan question answered by measurement not inference

`ps` showed **23 `inbox-watch.sh` lines across 11 other serials and ZERO for this one**, and
`get_agent_status` read NOT REGISTERED. Both limbs of the PID discriminator therefore agree: no live
peer holds this serial, and there was nothing of mine to reap. **No kill was issued** — the other
serials' watchers were left untouched, which is the self-scoping rule, not a courtesy.

Armed Monitor task `bnl3oewlo`; `TaskOutput` → `running`; arm banner read at source:
`parent-tied: pid 534938` — a real pid, so the self-exit path is armed rather than fail-open.
The Monitor delivered the summons within seconds of arming, then delivered msg 20395 mid-session.
**ACKed 20395 on the READ clock** (the checker's own file carries no broker id).

## 2. STEP 1 — READ AND DETERMINE. Four legs, never collapsed.

**Calendar resolved FIRST, from `lib/trading_calendar.py`, not from the summons** (CLAUDE.md NEVER#1):
today 2026-09-04 Fri, `is_trading_day` True, `prev_trading_day` = 2026-09-03,
`expected_last_trading_day` = 2026-09-04, served 2026-09-02 → **2 behind**.
Control sweep so a constant would have been visible: 09-03→0, 09-02→1, 09-01→2, 08-28→4 against the
T-1 target. The function discriminates.

**The fork `0.0.0_AB_MSTR~Z` named in 20395 is settled, and settled AGAINST the benign reading.**
That seat correctly declined to guess whether a T-1 basis makes this 1-behind rather than 2. The
answer is at `freshness_check.py:14/154`: `PASS = behind <= 1`. **The checker already grants the T-1
day.** So `behind = 2` is one day worse than the pipeline's own contract, not a basis artefact.

| leg | verdict | evidence |
|---|---|---|
| a. scheduled tasks | both fired on time | `daily_pull` 07:00:01 rc **1**, `freshness_check` 07:30:01 rc 2, MissedRuns 0 both, Next 09-05 |
| b. fallback / DAPI | **NOT the fault** | 07:00 log `PRECONDITION: PASS -- DAPI UP`; now: health ok + a REAL read, SPX `PX_LAST` 7747.71 `LAST_UPDATE_DT` 2026-09-03 |
| c. WDAC / kernel | **UNEXERCISED** | reachable only if DAPI had been restored; it never went down. Not a pass. |
| d. served artifact | one vintage behind, untouched today | `data_as_of` 2026-09-02, `generated_at` 2026-09-03T11:09:24Z, LastModified 11:09:26Z |

Leg b process census **with the denominator printed**: 3 processes under `C:\blp\` out of **541**
total `Win32_Process` rows — `clientratermgr`, `clientrater`, `bbcomm`. **`wintrv.exe` ABSENT**, and
the 8194 listener is owned by `bbcomm` (pid 33264). Per the standing order's own trap a running
bbcomm is not a running Terminal, so **the heuristic reads DOWN while the decisive test reads UP**.
Both are recorded rather than smoothed; the real refdata request is authoritative.

Leg d was deliberately taken through `portal_lookup.py` — **a different code path from the boto3 read
inside `freshness_check.py` that summoned me**. Re-running the summoning instrument would have been
repetition, not corroboration.

### 2a. A CORRECTION I OWE, and it is the one that changes routing
I first read leg (a) as a **publisher** failure, because the standing order's `LastTaskResult` exit
table maps `1` to "publisher failures (`:pub_failed`) — pull succeeded". **The log inverts it:**
`PULL EXIT CODE: 1` / `RESULT: PULL FAILED rc=1 -- nothing sent, publish NOT attempted.`

`scheduled_daily_pull.cmd` sets `RC=1` on **two disjoint paths** — `:pull` (runner's own rc) and
`:pub_failed` (`RC_PUB`, where 1 = a gate refused). **The table names only one of the two meanings.**
The file's own design claim is that exit codes are "deliberately disjoint so a reader of one log can
always tell which leg spoke"; for `rc=1` that property does not hold, and an operator obeying the
table diagnoses the publisher while the pull is what died. Routed to `1.0.0_SA_CTO~Z` (pipeline
work-order owner). I hold no git lane and did not edit my own deliverable to patch it.

## 3. ROOT CAUSE — reproduced, not inferred

Pull died in `model_portfolio_regression_analysis.ipynb`:
`ValueError: Index contains duplicate entries, cannot reshape` at
`model_holdings.pivot(index='date', columns='ticker', values='weight')`. Failing model **INT** (each
iteration prints its header before the call; INT's is the last emitted).

Replayed the notebook's own transform chain over all five templates under the `cma` interpreter:

```
UST 136 rows / 12 dates   dup 0        LT  378 / 28   dup 0
ST  333 rows / 23 dates   dup 0        ULT 301 / 23   dup 0
INT 399 rows / 25 dates   dup 2   <-- both on 2026-08-18
        SPHY 0.0281 + SPHY 0.0275   |   SPYM 0.1010 + SPYM 0.0150
```

**`dup_before_override = 2`** — the duplicates are in the RAW sheet before any ticker rename, so this
is **not** the `$:CASH→ICSH` / `SPLG→SPYM` override collapsing two tickers. *That was my first
hypothesis and the measurement killed it;* I had reasoned from the rename's existence to its guilt.

**Why today and not before — the discriminating fact.** `YC Intermediate Term template.xlsx` mtime
**2026-09-03 10:50:25 ET**; the 09-03 run ran 07:00:01–07:10:11 and PASSED. The edit landed ~3h40m
after it finished, so **09-04 07:00 was the first run to read the edited file.** Controls: last 8
runs are 7× `PULL 0 / PUBLISH 0` then today; and of 7 sibling templates INT is the **only** one
modified on 09-03 (others 07-02, 08-07, 08-12, 08-18, 08-19, 08-19).

**Remedy exercised both ways in memory, nothing written.** Reproduced the production error verbatim
first, so the test discriminates:
- **A — sum the duplicate pairs:** pivot OK, shape (25,39); 2026-08-18 still sums to **exactly 1.0**;
  merged SPHY 0.0556, SPYM 0.1160.
- **B — `drop_duplicates(keep='first')`:** 2026-08-18 → 0.9575. **Breaks the invariant. REJECTED.**

The raw column already sums to 1.0 *with both pairs present* and the paired weights differ, so these
read as intentionally split lots on separate lines, not a copy-paste. That is why summing is faithful.
Whether the fix belongs in the spreadsheet (OCIO Models / 49 Models) or the loader (a groupby-sum
before the pivot) is not mine and I hold no lane for either.

## 4. WHY STEP 2 WAS **NOT** FIRED, though it was formally reachable

Step 1 found a genuine failure, so Step 2 unlocked. **Step 2a run anyway and recorded:** fire-once
ledger 9 entries, **0 within 6h** (most recent 2026-09-03T11:02:06Z, 24.8h) — a fill would have been
*permitted*. **I did not take it.** DAPI passed its precondition at 07:00 and answers a live request
now; there is no sign-in fault, and spending a fire-once attempt against a spreadsheet defect buys a
lockout risk for nothing. A re-pull before the input is fixed fails identically and deterministically.
**Step 2's recovery is shaped for a Terminal fault and this is not one.**

*Incidental:* that same ledger falsifies my standing order §3a, which says every row reads
`SUBMITTED-SUPERVISED-MSTRZ` until an unintegrated lane commit lands. **5 of 9 now read
`SUBMITTED-UNATTENDED-FALLBACK`** — that commit has landed and the caveat is stale. Discriminating on
timestamp rather than label was correct regardless, which is why the stale text cost nothing here.

## 5. ⚡ THE PERISHABLE FINDING — routed, not actionable by this seat

Models pull failed → `.cmd` went `:pull` → `:prune`. **The ETF LEG and CONSTITUENTS LEG never ran.**
Measured with a control: today's log contains `ETF LEG` **0**× and `CONSTITUENTS LEG` **0**×;
yesterday's contains each **2**×.

The `.cmd` skips those legs on a failed pull, reasoning "Bloomberg is unreachable or broken, so the
ETF pull would fail for the same reason." **That premise is false today** — Bloomberg is up and
answering; the pull died on a spreadsheet. The isolation rule fired on a failure mode it was not
reasoning about. Per `READ_HERE.md` §4 the derived layer is **current-day-only: "There is no backfill.
Every uncaptured day is gone permanently."** Running the legs later today still captures today.

Both write to S3 → denied by my mechanical fence and forbidden by prompt.md (read-only, no S3
writes). **I did not attempt them and did not route around the gate.** Named as an ask to
`0.0.0_AB_MSTR~Z` + `1.0.0_SA_CTO~Z` with the exact two commands and the `PY_AWS` interpreter.

## 6. COMPILER TOOLS

- `comp-read integrations/bloomberg/pipeline/freshness_check.py --for "..."` — gave the shape, and the
  **qualifier at line 14 (`PASS = behind <= 1`) is what settled the T-1 fork**. A grep for the served
  key would have returned the key and not that line.
- `comp-find 'model_holdings' integrations/bloomberg/pipeline/tplus1` — 15 hits / 4 files, denominator
  printed; located the pivot and the loader in one pass.
- **Rail fired twice against me and both times it was right:** a `find`-based log hunt (routed to
  `comp-find`), and a `comp-read | head` (a census piped into a receiver that erases its denominator).
  I re-ran the second without the `head` rather than marking it rail-checked.

## 7. STATE AT CLOSE

Registration LIVE (PID 17772). Monitor `bnl3oewlo` running, parent-tied. **Zero crons** — correct end
state; the 07:15 clock is retired and a successor must not re-arm one. Inbox empty. Report delivered
2/2 (`0.0.0_AB_MSTR~Z`, `1.0.0_SA_CTO~Z`), denominator printed by the send. Nothing blocking this seat.

**Open, owned elsewhere:** (1) de-duplicate the INT template or add the loader groupby-sum, then a
re-pull — which I can fire the moment the input is fixed; (2) today's ETF + constituents capture,
perishable at end of day; (3) the `rc=1` exit-table ambiguity.

**This file is uncommitted.** This seat holds no git lane; `0.0.0_AB_MSTR~Z` is the named integrator
and sweeps `logs/`. On the shared site-Z tree an unswept file is at risk, which is why the path is
stated in the report rather than left to be discovered.
