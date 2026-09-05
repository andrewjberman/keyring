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

## 7. LAUNCH STEPS 2a + 3 — identity gate and the Teams arm

**2a IDENTITY ACCEPTANCE GATE: PASS.** `whoami` on `opal-gateway-bbg` → `Opal Bloomberg` /
`opalbloomberg@opalinvest.com`. Not Andrew's proxy identity. Gate cleared before any Teams surface
was touched.

**3 TEAMS MONITOR: armed WITH the mandatory pin**, task `b1866ois3`, `TaskOutput` → running.
Banner read at source before serving anything:

```
[teams-watch] armed interval=15s cursor=2026-08-25T21:11:24.527Z (incoming-only)
              pin(server=opal-gateway-bbg, identity=opalbloomberg)
[teams-watch] token selected: identity=opalbloomberg@opalinvest.com
```

**CURSOR ADJUDICATED, NOT ASSUMED.** `TEAMS_DUTY.md` requires SUSPECT-REPLAY treatment if the
banner cursor is OLDER than the newest entry in thread memory. Newest daily file is
`2026-08-25.md`, and its own record states I posted in-thread at **21:11:24Z** — the cursor is
`2026-08-25T21:11:24.527Z`, i.e. **exactly at my last served act, not behind it.** So this arm is
**NOT** suspect-replay, and the ~10-day window it opens is genuine, not history.

**Then measured rather than inferred from the Monitor's silence** (an early stop and a true absence
read identically): `poll_addressed_teams_messages(since_iso=2026-08-25T21:11:24Z)` → **count 1**,
and that one is `from_name: "Opal Bloomberg"` with an empty preview — **own-authored, correctly
suppressed by the incoming-only filter.** So the Monitor's quiet is right for the right reason.
**Zero inbound asks in the window; nothing owed on the Teams surface.** *(Its chat_id
`19:517aa5ee-...7aa72700-...` is not in `threads/INDEX.md`; not an inbound ask, so noted and not
chased.)*

**A standing item CLOSED by reading rather than left open:** the Andrew-direct of
2026-08-25T21:10:05Z ("tell MSTR he needs to adjust your startup/operating tenets") was broadcast
**QUEUED** to a non-live `0.0.0_AB_MSTR~Z`, and my 08-25 thread file lists it as owed. **It was
discharged:** both recommended tenets are now live in `refs/TEAMS_DUTY.md` (section marked *added
2026-08-25*) — "Let RECALL decide what is owed — never the emit" and "Never write a delay, an age,
or an apology into an ack on the strength of an emit." A QUEUED receipt is not undelivered, and
here it in fact landed.

## 8. STATE AT CLOSE

Registration LIVE (PID 17772). Inbox Monitor `bnl3oewlo` running, parent-tied pid 534938. Teams
Monitor `b1866ois3` running, pinned. **Zero crons** — correct end state; the 07:15 clock is retired
and a successor must not re-arm one. Inbox empty; msgs 20395 and 20397 ACKed on the READ clock.
Report delivered 2/2 (`0.0.0_AB_MSTR~Z`, `1.0.0_SA_CTO~Z`), denominator printed by the send.

`1.0.0_SA_CTO~Z` (msg 20397) accepted both routed items and sharpened the second: the `.cmd`
contains **both sides** of the contradiction 50 lines apart — `:195-200` justifies the skip on
"Bloomberg is unreachable or broken", while `:252-256` names the exact harm it causes ("convert one
leg's fault into two legs' PERMANENT DATA LOSS"). That seat also **reframed my perishable ask
correctly**: I argued it from my S3-write fence, but the binding constraint is **vendor egress**,
reserved to Andrew's explicit per-use word — availability is not authorization. It is with Andrew,
not self-granted. My framing was not wrong, it was the weaker of the two reasons.

## 9. ANDREW-DIRECT 2026-09-04 ~13:00Z — both of my routed items RULED (via `1.0.0_SA_CTO~Z`, msg 20401)

**VERBATIM: "Approved for all of these"** — five words to a five-card `/open-calls` frame, so the
referent is the five RECs as written. Record @`c1c79c3729` (LOCAL; origin/SITEZ `360943fabb`,
3 unpushed — stated because a push state is perishable).

- **Call 1 — the perishable legs: EXECUTED, not merely authorised.** `1.0.0_SA_CTO~Z` fired both
  immediately and verified on the object store, not on the producers' success lines:
  **16 objects at `s3://opal-data-etfs/bbg/2026-09-03/`** (7 at 13:01:32Z, 9 under `constituents/`
  at 13:02:17Z, all non-zero), counted with `length(Contents)` rather than `KeyCount` — which is
  absent when the CLI auto-paginates. **Today's capture is SAVED.** Leg 1b's
  `refused:entitlement` on all four tickers is the documented BQL state, not a fault.
- **Call 2 — the duplicates are INTENTIONAL and the LOADER SUMS them.** That is Remedy A, the
  option I exercised and recommended, ruled in. Implementation is `1.0.0_SA_CTO~Z`'s work order
  along with the `:129` branch.

⛔ **CALL 1 IS SPENT, NOT STANDING.** It covered TODAY's two legs only. A future skipped day is a
fresh vendor-egress call until `:129` is fixed. Recorded so no successor reads it as permission.

### THE ITEM NEITHER RULING CLOSES, and it is the one I still own
Call 1 saved the **capture**; it did not produce the **models vintage**. The served object is
unchanged at `data_as_of 2026-09-02` — **so the condition that summoned me is still live.**
Projected rather than left to be rediscovered at 07:30 tomorrow: if the loader sum has not landed
by the 09-05 07:00 fire, that run reads the same template, dies at the same pivot, served stays
09-02, and `trading_days_behind` = **3** → a second summons **and a second `:129` skip that Call 1
does not cover.** The loader fix removes both triggers at once, so it is doing more work than the
branch fix alone.

**I am the seat that fires the re-pull. Blocked on exactly one thing: the loader sum landing.**

**Measured input handed to the implementer** (a real fork in the code — the loader rescales per
date *before* the point duplicates would be summed, so before-vs-after is a live choice):
**order-invariant.** Both orders built end to end on the live file — same 397-row key set, max
absolute difference **5.55e-17**, affected rows identical either way (SPHY 0.0556, SPYM 0.1160).
**Negative control so the equality is a result and not a test that cannot fail:** the same
comparison against a MAX-aggregated variant differs by **0.02625274**. Reason: summing duplicates
does not change the date's raw total, which is the rescale's divisor.

**Scope of the fix, censused across all five templates rather than the failing one:** UST 136/12,
ST 333/23, LT 378/28, ULT 301/23 all carry **zero** duplicate pairs; INT 399/25 carries the only 2.
A groupby-sum is a no-op for four of five models.

⚠ **LIMIT ON MY OWN EVIDENCE, stated not implied:** I exercised the **pivot step in isolation**.
That proves the fix clears the step that failed; it does **not** prove no later cell is
duplicate-sensitive. The re-pull is the exercise that settles it, and it is mine to run.

## 10. TWO RELAYS OF ANDREW, ONE FORK LANDING ON MY OWN NEXT ACT (msgs 20401 + 20405)

`0.0.0_AB_MSTR~Z` relayed a **second, EARLIER** Andrew-direct (~12:1xZ, *"Recs 1 and 2 approved"*,
a **four**-card frame) against `1.0.0_SA_CTO~Z`'s ~13:00Z (*"Approved for all of these"*, a
**five**-card frame). **Two different statements, two different frames — not necessarily a
contradiction in his word.** But they name **different unblock conditions for the re-pull I hold:**

| carrier | the remedy it names |
|---|---|
| 20401 | card 2 → **"(a) INTENTIONAL, loader SUMS them"** — duplicates STAY in the sheet |
| 20405 | *"models data stays at 2026-09-02 until **the template is de-duplicated**"* |

`20405` also declines the sheet half (*"NOT TAKEN BY THIS SEAT … Read as his or OCIO's; one word
redirects it"*) while authorising the loader half — so it carries both, then states the precondition
as the sheet. **A reader taking that sentence literally waits for an edit the other ruling does not
call for.** Surfaced to both seats; **not adjudicated** — relaying is mine, adjudicating is not
(CLAUDE.md: never widen or narrow Andrew's word to one seat into a gate on another).

⭐ **The practical resolution needs no ruling: EITHER remedy clears me.** Both remove the duplicate
pairs before the pivot. I am not waiting on the fork, I am waiting on a change. **The fork still
matters to somebody** — if each half is left because the other is assumed to cover it, the models
leg sits at 09-02 indefinitely. Named so that cannot happen quietly.

**Correction I owe on my own wording:** I used both framings — "the moment the template is
de-duplicated" to Andrew, "blocked on the loader sum landing" to CTO~Z. **The accurate statement is
that either clears it.**

### ONE RUN, TWO SEATS EACH DESCRIBING ITSELF AS ITS CAUSE
Both relays cite **identical object timestamps to the second** — 7 at `13:01:32Z`, 9 under
`constituents/` at `13:02:17Z`. So there was **ONE run, not two** (the good outcome — no double-fire
against the vendor), yet two separate Andrew vendor grants exist for it and each seat reports having
spent its own on it. **Reading the objects cannot tell you which process wrote them** — the banked
producer-attribution class, live again. Nothing needs redoing; both treat their grant as SPENT,
which is the conservative direction. Raised only because two seats moving to fire within the same
minute is a race against a vendor API and a shared S3 prefix that happened to resolve cleanly.

**Accepted from 20405 without note:** as-of `2026-09-03` on a capture made at 13:0xZ on 09-04 is
CORRECT (the pipeline lands under `prev_trading_day`); what was perishable was *today's run of a
current-day-only source*, not a file named for today. Constituents fill DIVZ 29 / IDVZ 44 / PFDE 90
/ PFOE 24; leg 1b's entitlement refusal on all four is the documented state, not a fault.

## 11. STEP 2 EXECUTED — THE RE-PULL. Fired 13:39Z, the turn the loader landed.

✅ **CLOSED — the section was written open, mid-poll, and is now FINAL. THE SUMMONS IS DISCHARGED.**
*(Written before the outcome because this log is this seat's only durable carrier and a session
ending mid-poll would have left the whole recovery unrecorded.)*

**Fork resolved by both seats, in my favour and against MSTR~Z's own rec:** `0.0.0_AB_MSTR~Z`
(20415) **withdrew the sheet half on the merits** — merging intentional split lots destroys real
information to work around a loader defect — and `1.0.0_SA_CTO~Z` (20417) landed the loader sum
`@cd6dddab6f`, **dissolving** the fork rather than ruling it. Verified on disk before firing
(`holdings_summed` groupby at nb line 431, pivot reads it at 432); the working tree is the plane
that executes, so push state is irrelevant to whether it was live.

```
runner  integrations/bloomberg/pipeline/tplus1/tools/run_daily_pull.py  (cma env)
target  20260903          PULL EXIT CODE: 0
  market_indices_data_pull.ipynb            OK 16s
  model_portfolio_regression_analysis.ipynb OK 99s   <- died this morning
  TRIPWIRE PASS, 18/18
```

⭐ **The fix is now EXERCISED END-TO-END, which is the thing neither seat had.** CTO~Z tested the
extracted function against the five real templates — that proves the failing step clears. **I named
the residual myself in 20408: it could not prove no LATER cell was duplicate-sensitive.** The full
chain now runs, and `model.etf_returns: no duplicate ['date','ticker'] rows` + `model.summary: shape
(25,10) exact` settle it. **Residual discharged by exercise, not argument.**

⚠ **`model.holdings: 1547` looks like the fix did not apply, and it is the opposite.** 1547 is the
UNSUMMED total (136+333+399+378+301). The fix assigns to a NEW variable and only the *pivot* reads
it, so the stored artifact keeps both split-lot rows. **The merge happens where the math requires it
and nowhere else** — exactly MSTR~Z's reasoning for withdrawing the sheet edit.

### ⛔ WHAT I WILL NOT LET PASS AS A RE-PULL WHEN IT WAS NOT
`market_indices_data_pull.ipynb` ran in **16s**; this morning the same notebook took **134s**. And
`data 20260903 v1.pkl` carries mtime **07:02:25** — this morning's artifact, *not* rewritten by my
09:39–09:41 run. Only `model 20260903 v1.pkl` (09:41:03) is mine.
**So the re-pull did NOT re-fetch market-index data.** It reused the PKL the scheduled run's own
successful first leg had already written before the model notebook killed the chain. **I did not
establish the mechanism** (an idempotence check on an existing target is the obvious candidate; I
did not read the notebook to confirm) **and am not asserting one.** Sound on the merits — it is a
legitimate 09-03 vintage that passed the full tripwire in my run, identical to what the scheduled
run would have published — and one fewer vendor call on a day that already had a double-fire. But
*"ran in 16s"* and *"re-fetched"* are different claims and only the first is measured.

### PUBLISH LEG — channel chosen against the runner's own instruction
Ran the **production publisher** (`publish_to_portal.py` under PY_AWS, no args) — the exact form
`scheduled_daily_pull.cmd`'s send leg uses, so this completes the failed scheduled run rather than
opening a new path. It re-runs the as-of-scoped tripwire itself and refuses backward publishes
(rc 40). **Pre-announced on the broker (20422) before firing**, per the remedy adopted in 20420
after today's double-fire — though the re-pull itself was announced *mid-flight*, not pre-flight,
and I said so rather than letting the timestamp imply otherwise.

⛔ **A FOURTH STALE POINTER, and this one routes to the wrong channel.** `run_daily_pull.py`'s
closing NEXT hint says to publish via `opal_data_refresh_upload(...confirm=True)` — the **old
m365-gateway path**, which the `.cmd` deliberately abandoned because it "returns transport dropped,
response lost on calls that ALREADY SUCCEEDED server-side" and "a scheduled retry against that shape
double-fires the pipeline." **The runner's closing instruction points at a channel its own wrapper
retired for double-fire reasons — on the day we already had one.** I took the `.cmd`'s path.

**Today's tally of stale pointers, all in recovery-path documents:** STANDING_ORDER's rc=1 exit
table · its §3a label caveat · its `workflows/` runner path (measured ABSENT) · `run_daily_pull.py`'s
NEXT hint. Flagged, not fixed — no git lane.

Publisher: `as-of-scoped tripwire PASS` · `portal currently serves 2026-09-02 -- 2026-09-03 is newer,
safe to advance` · both PKLs uploaded (8,633,578 + 17,626,699 bytes) · `manifest.json uploaded LAST
-- pipeline fired` · `served data_as_of 2026-09-03` · `served 1D matches the PKL for all five
models` · **PUBLISH EXIT CODE: 0**.

## 12. DISCHARGE — measured on a second instrument, not on the publisher's rc

```
portal_lookup.py (a different code path from the publisher and from freshness_check's boto3 read)
  data_as_of    2026-09-03      (was 2026-09-02)
  generated_at  2026-09-04T13:48:15Z
  LastModified  2026-09-04 13:48:17Z
  size          19172 bytes     (was 19194) -- CHANGED, so new content, not a re-upload
                                of identical bytes wearing a fresh timestamp

freshness_check --verdict-only (the checker's OWN logic, no S3, no summons fired)
  as_of 2026-09-03 / today 2026-09-04 -> frontier 2026-09-04, behind=1 -> PASS  rc=0
  CONTROL  as_of 2026-09-02 same day -> behind=2 -> STALE rc=2
```
The control matters: **PASS is not a constant** — the instrument still refuses the exact state it
summoned me on. The publisher also ran a check the runner's tripwire does not — *"all 5 model
portfolios have a bar ON the as-of 2026-09-03"* — so the advance is not merely a date field moving.

### ⛔ A FIGURE I SENT TWO SEATS WAS WRONG — `behind=3` IS ACTUALLY `2`
I projected in 20407/20408 and again in 20422/20423 that a 09-05 fire with nothing landed would read
`trading_days_behind=3`. **Measured: 2.** `2026-09-05 IS A SATURDAY`, so
`expected_last_trading_day` does not advance to 09-05 — it stays at 2026-09-04.

**This is the exact failure CLAUDE.md NEVER#1 exists to prevent, and I walked into it after
correctly avoiding it once the same session.** I resolved the calendar properly for the BACKWARD
verdict this morning, with a four-point control sweep — then computed the FORWARD projection by
counting calendar days, which is the *"a calendar-day subtraction would false-summon every Monday"*
error the checker's own header names. **Direction right, magnitude wrong.** Corrected to both seats
(20430/20431) because the wrong number reached their records, not because it still gates anything.

The fuller picture, which changes the shape of any future projection:

| date | trading day | frontier |
|---|---|---|
| Fri 2026-09-04 | yes | 2026-09-04 |
| Sat 09-05 / Sun 09-06 / **Mon 09-07 (Labor Day)** | **no** | 2026-09-04 (flat) |
| Tue 2026-09-08 | yes | 2026-09-08 |

**The frontier is FLAT Friday through Monday.** Today's 2026-09-03 reads PASS across the whole long
weekend; the next real test is Tuesday's fire.

## 13. THE MIRROR RE-DERIVED — and a correction about my OWN fence

`1.0.0_SA_CTO~Z` (20439) closed both routed items — the `:129` leg-isolation branch `@0f4fd97d17`
(four-cell truth table, pre-fix control reading REACHED/SKIPPED/REACHED/SKIPPED, so *exactly one
cell changed* is a measurement) and the rc=1 contract `@d776b21d98` — **and assigned one act back
to me:** *"the standing order's table is the mirror and should be re-derived from the corrected
text; that re-derivation is 0.0.3_BG_BBGTerminal's."* Done, from README.md read **at source**, not
from 20439's summary of it.

### ⛔ THE CORRECTION THAT MATTERS MORE THAN THE EDIT
All day I reported four stale pointers as *"I hold no git lane; flagging, not fixing"* and listed
all four as **UNOWNED** in 20430/20431. **That was wrong about three of them.** They live in
`deliverables/STANDING_ORDER_0715_DAILY_BACKSTOP.md`, and `deliverables/` is one of the four paths
my own mechanical fence **explicitly permits me to write**. The file sits there *precisely because*
`refs/` is unwritable from this seat — **its own placement note says so, and I read that note this
morning.**

**I conflated "I cannot COMMIT" with "I cannot FIX."** Two different fences. The write was always
mine; only durability depends on a sweep. I spent the day routing my own writable file's defects to
other seats as unowned. Only the fourth pointer (`run_daily_pull.py`'s NEXT hint) genuinely is not
mine.

**Fixed in that document:** (1) the rc=1 table, re-derived — `1` now its own row marked TWO-VALUED
with the two disambiguating log strings verbatim, `20/30/40` left as publisher codes; (2) the runner
path, `workflows/…` (measured ABSENT) → `integrations/…`; (3) §3a's label caveat — **instruction
kept, only its reason corrected**, because the label encodes *how* an attempt was made and never
*when*, and the fire-once window is a TIME window. Plus a new PUBLISH bullet naming
`publish_to_portal.py` and warning off the runner's retired-gateway hint.

**Verified IN POSITION, not by counting.** A census for the old strings returns non-zero **because
my own correction notes quote them** — the marker-matching-inside-its-own-negation shape, where a
count reads as a failed edit. At their line numbers: `:103` is the live row now listing only
`20/30/40`; `:123`, `:172`, `:217` are each inside a correction block quoting what the line used to
say. **No live instruction in that file still routes `rc=1` to the publisher.**

## 14. FINAL STATE

**Summons `20260904T113002Z` DISCHARGED**, Step 1 → Step 2 → Step 3 complete in one session, and
the recovery doctrine that misrouted me is corrected in the same session.
Registration LIVE; inbox Monitor `bnl3oewlo` and Teams Monitor `b1866ois3` both running; zero crons;
msgs 20395/20397/20401/20405/20415/20417/20420/20439 ACKed on the READ clock.

**Closed elsewhere today:** `1.0.0_SA_CTO~Z` fixed the `:129` leg-isolation branch `@0f4fd97d17` and
the rc=1 exit contract `@d776b21d98` — both from this seat's 12:01Z investigation, both exercised.

**Open and genuinely not mine — ONE item, not four:** `run_daily_pull.py`'s closing hint pointing at
the retired m365 gateway. *(The other three were always mine to write; see §13. That
mis-attribution is the correction I most want a successor to read.)*

⚠ **BOTH FILES BELOW ARE UNCOMMITTED** and `0.0.0_AB_MSTR~Z` holds the paths (msgs 12:04Z + 20442):
```
deliverables/STANDING_ORDER_0715_DAILY_BACKSTOP.md      <- recovery doctrine, RELAUNCH §0b resolves it BY PATH
logs/2026-09-04/freshness_summons_step1_1139-1203Z.md   <- this file
```
The standing order matters more than the log: it is what a successor reads at 07:30 on a dark
morning, and an unswept tree would lose **the corrected version of the exact instrument that
misrouted me today.**

---

**Incidental live positive for a peer's fix, offered not claimed:** `0.0.0_AB_MSTR~Z` reported
fixing a Tier-2 write-gate CRLF defect (`@fe85e5bf6c`) whose unexercised cell was *(to_agents ARRAY
× Tier-0 recipient)*. My 20407/20408 send is exactly that shape from an **independent** seat and
returned **2 DELIVERED / 0 REFUSED**. That is corroboration through a different actor than the
author's own battery — which is the distinction their own note about the battery's uncrossed
dimensions was making.

**Open, owned elsewhere:** (1) de-duplicate the INT template or add the loader groupby-sum, then a
re-pull — which I can fire the moment the input is fixed; (2) today's ETF + constituents capture,
perishable at end of day; (3) the `rc=1` exit-table ambiguity.

**This file is uncommitted.** This seat holds no git lane; `0.0.0_AB_MSTR~Z` is the named integrator
and sweeps `logs/`. On the shared site-Z tree an unswept file is at risk, which is why the path is
stated in the report rather than left to be discovered.
