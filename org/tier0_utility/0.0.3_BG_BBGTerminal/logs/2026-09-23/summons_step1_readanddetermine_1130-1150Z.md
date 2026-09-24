# 0.0.3_BG_BBGTerminal -- session log 2026-09-23 11:30-11:50Z

**Session purpose:** launch + freshness STALE summons, Step 1 (read-and-determine).
**Outcome:** Step-1 finding of ACTUAL FAILURE; **Step 2 NOT entered -- Step 2a refused.**
**Root cause identified and it is NOT the class anyone would have guessed.** Escalated to
`0.0.0_AB_MSTR~Z` (msg `20260923T114803Z_...`) and reported to Andrew at this terminal.

---

## Launch

| Step | Result |
|---|---|
| `register_agent` | LIVE, PID 30728 (was NOT REGISTERED) |
| `/watcher` | Monitor task `b81iw316h`, script pid **33600**, verify-after census = 1 row |
| Inbox | 3 messages, all read; 24326 + 23710 acked (the summons file carries no Msg-ID) |
| `get_delivery_state` since 2026-09-16 | READ 6 of 6 ackable; nothing unread |
| Step 2a identity gate (`whoami` on `opal-gateway-bbg`) | **PASS -- Opal Bloomberg** (`opalbloomberg@opalinvest.com`) |
| `bloomberg_health` | **ok=false** -- could not start blpapi session to 127.0.0.1:8194 |
| Open task orders | none |
| Crons armed | **zero** (correct end state; the 07:15 clock is retired) |

### Watcher census defect, re-confirmed (device-local, already banked)
The skill's literal regex `inbox-watch\.sh <serial> stream` returns **0 script rows for a LIVE
watcher on this box**, because the absolute path must be quoted (the workspace path contains a
space) and the quote lands between `.sh` and the serial. `inbox-watch\.sh"? <serial> stream`
returns the true row. Read as written, the census says NO WATCHER on a healthy seat -- the branch
the skill labels "go arm one", i.e. it invites a double-arm. Reported, not fixed: `refs/` and
`.claude/` are unwritable from this seat by design.

---

## STEP 1 -- READ AND DETERMINE. Legs never collapsed; the summoning instrument never repeated.

### a. Scheduled task -- **FAILURE**
`Get-ScheduledTaskInfo OPAL_BBGTML_daily_pull`: LastRunTime **2026-09-23 07:00:01** local,
**LastTaskResult=50**, NextRunTime 09-24 07:00. Per the exit contract, `50` = DAPI precondition
FAILED, **the pull was NOT attempted** -- no partial data, nothing to hunt downstream.

`OPAL_BBGTML_freshness_check`: LastRunTime 07:30:01, LastTaskResult=**2** (STALE). Both tasks
fired on schedule, so **no SCHEDULE-GAP** and the §1a Layer-2 two-consecutive-miss case does not
apply. `NumberOfMissedRuns=0` on both and was **not** used as a health instrument.

### b. Fallback (self-heal) -- **RAN; its verdict is honest but structurally incomplete**
- Processes under `C:\blp\`: **35** (denominator printed). `wintrv.exe` PID **33932 IS running**;
  `bbcomm` PID 8568 running -- and a running `bbcomm` is not a running Terminal.
- `Get-NetTCPConnection -LocalPort 8194`: **0 rows.**
- `bloomberg_health`: ok=false.
- `~\opal_bbg_logs\bbg_tplus1_20260923_070001.log`: fill **verified PASS** (9 password dots,
  expect 9; username glyph-runs 11 within 11..12; OCR similarity 100%), **submitted ONCE** at
  11:01:53Z, `8194 listener count after submit: 0`, escalated **without retrying**. Correct
  behavior. One attempt spent.

### c. WDAC / kernel -- **UNEXERCISED**
DAPI was never restored, so this leg never ran. Not a pass and not a fail.

### d. Served artifact, **by content**
`tools/portal_lookup.py get benchmarks model_portfolio_benchmarks.json` ->
`s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json`,
**data_as_of=2026-09-21**, generated_at=2026-09-22T11:08:34Z, LastModified 2026-09-22T11:08:35Z,
19223 bytes. Reproduces the summons figure on a **different instrument** from the one that
summoned me.

### Trading calendar -- resolved from source, not from the summons
`lib/trading_calendar.py`, `calendar_source = NYSE/hardcoded-fallback-2024-2027`. 2026-09-23 is a
trading day. `trading_days_behind` for 09-23 / 09-22 / 09-21 / 09-18 / 09-11 =
**0 / 1 / 2 / 3 / 8** -- the control means a `2` was distinguishable from a constant.
The pipeline is **T-1 by fixed rule**, so `behind=1` is the healthy steady state and the served
09-21 is `behind=2`: genuinely **one trading day short**. **The STALE verdict is CORRECT.**

### Not a multi-day outage
`bbg_tplus1_20260922_070001.log`: `RESULT: END-TO-END OK -- pulled, validated, published,
served-content verified`, published data_as_of 2026-09-21. **Single missed day: today.**

---

## ROOT CAUSE -- read off the screen; no existing instrument could see it

The `BLOOMBERG: Login` window (**hwnd 136698**, pid 45080) is **still open and VISIBLE 38 minutes
after the submit**. Captured **read-only via `PrintWindow`** (occlusion-proof; no input sent, no
fill, nothing clicked). It is **not** a login form and **not** a rejected-credential error:

```
Keyboard Enrollment for Fixed-Location Bloomberg Terminal
New Bloomberg Keyboard Enrolled
Remoting into a Fixed-Location Bloomberg Terminal requires a valid Bloomberg Keyboard
association. The connected Bloomberg Keyboard is now associated with this terminal.
Terminal S/N 5401234    Keyboard S/N 90179218
[Continue to Login]     Account Manager: JEFRY BERNAL PERALTA +1-212-617-4449
```

**The sign-in was not refused.** Bloomberg interposed a one-time **keyboard-enrollment
interstitial** the automation has no handler for. The enrollment has **already happened** (the
text is past tense); what remains is an unacknowledged modal standing between the submit and a
completed login.

### Instrument gap (surfaced, not adjudicated -- I hold no lane on that script)
`bbg_fallback.ps1`'s post-submit oracle is a **listener count on 8194**. At that oracle,
"a modal is blocking the login" and "the credential was rejected" are the **same observation**.
Of the **8** rows in `C:\opal-elev\bbg_fallback_ESCALATION.txt`, today's is the **FIRST**
`submitted, 1 attempt used, DAPI still down`; the other 7 are pre-submit aborts or fire-once
refusals. **This class has not been seen before on this box.**

Also observed and **NOT** interpreted (invisible windows, provenance unknown, could be stale from
any prior session): `Warning: Limited Data Access` and two `PC Performance Warning` windows under
`bplus64` pid 31196. Recorded so a successor has them; no verdict attached.

---

## STEP 2a -- FIRE-ONCE LEDGER PRECHECK: **REFUSES**

`~\.bbg_signin_attempts.json`, **20 entries**. Most recent
**2026-09-23T11:01:53.2953253Z**, outcome `SUBMITTED-UNATTENDED-FALLBACK`, **38 minutes old** at
my read (now 11:39:42Z). **>=1 inside the 6h window -> DO NOT FILL, ESCALATE.**
Discriminated on the **timestamp**, never on the outcome label.
**I sent no keystroke and no click to any Bloomberg window this session.**

---

## What was asked of Andrew (one decision, not a menu)

Clicking `[Continue to Login]` is not a credential submission and cannot contribute to a
bad-password lockout, so the fire-once **rationale** does not reach it. **But fire-once is a
FENCE and I do not route around a fence on my own reading of its reason.** Asked for his explicit
word to: click Continue to Login; then, if a credential form follows, ONE supervised sign-in
outside the 6h window; then re-pull via
`integrations/bloomberg/pipeline/tplus1/tools/run_daily_pull.py` under `cma` and publish via
`integrations/bloomberg/pipeline/publish_to_portal.py` under `PY_AWS` (the `.cmd`'s own send leg,
**not** the retired gateway channel the runner's closing hint prints), with the `.ST` CIX content
check (CIX resolution is login-scoped and the session would be freshly signed in), positive
control SPX + a negative control, and verify the served object **by content**.
**Never send on a tripwire FAIL.**

Alternative stated plainly: one human click at the terminal, and the **09-24 07:00** fire recovers
it unattended. Cost of waiting: one more day at `behind=2`.

**Escalation sent:** `0.0.0_AB_MSTR~Z`, `20260923T114803Z_0.0.3_BG_BBGTerminal_ESCALATION_--_OPAL_BBGTML_09-23_pull_FAI.md`
(filesystem + broker + channel push). Reported to Andrew at this terminal the same turn.

---

## Teams concierge surface (launch step 3) -- ARMED BUT CANNOT POLL

Monitor task `bzo2l1n9m`, `teams-watch.py --server opal-gateway-bbg 60`.

**Arm banner, read before serving anything (as required):**
`[teams-watch] armed interval=10s cursor=2026-09-15T18:25:20.883Z (incoming-only) pin(server=opal-gateway-bbg, identity=None)`

**1. THE PINNED TOKEN IS EXPIRED.** Second banner line:
`[teams-watch] pinned token expired -- quiet retry, pin HELD (cycle 1, identity=None)`.
The pin **held** rather than falling back to Andrew's identity -- the fence working exactly as
designed. **The Teams surface is DOWN until a human OAuth sign-in as the Opal Bloomberg account.**
The MFA goes to Andrew's phone; this is not mine to complete. The watcher self-recovers the moment
the token is live, so it stays armed.

⚠ **Do NOT read msg 23710 as covering this.** Andrew's *"dont worry about it, NFRA_OPLGTW is
handling this"* was about **`opal-gateway`** (his proxy identity). This is **`opal-gateway-bbg`** --
a different registration key with its own OAuth record, which msg 24326 confirms was left UNTOUCHED
and still needs its own fresh interactive sign-in. Surfaced, not adjudicated.

⚠ Note the instrument split: MCP `whoami` on `opal-gateway-bbg` **succeeded** this session (the
identity gate passed), while `teams-watch.py` reads the **credentials file** and finds that record
expired. Two different token stores. **A passing identity gate is NOT evidence the Teams poller can
authenticate**, and nothing in either banner says so.

**2. CURSOR REPLAY HAZARD IS LIVE.** `TMPDIR` is UNSET, so the script's `/tmp` resolves to
**`C:\tmp`** under native Windows Python. The two homes have diverged **again**:

| home | cursor |
|---|---|
| `C:\tmp\teams-watch.cursor` (**the live one**) | **2026-09-15T18:25:20.883Z** |
| MSYS `/tmp/teams-watch.cursor` | 2026-09-16T21:25:44.056Z |

The live cursor is **older than my newest thread daily file** (`threads/2026-09-16-menachem-goldstein/2026-09-18.md`).
**Per TEAMS_DUTY: everything this arm emits is SUSPECT-REPLAY until RECALL clears each message
individually.** Recorded here as that ref requires. **No cursor file was hand-edited** -- the engine
defect is `0.5.0_AE_OpalETL~Z`'s and is surfaced, not worked around.

---

## STEP 2 -- RECOVERY EXECUTED ~19:3x-19:5xZ. **CLOSED. Portal serves 2026-09-22.**

**What unblocked it:** at ~14:5xZ a HUMAN cleared the keyboard-enrollment modal and signed the
Terminal in. Measured, not assumed: `bloomberg_health` flipped to **`ok:true`, service
`//blp/refdata`**, and the gateway token went live in the same window.

⭐ **STEP 2a DID NOT NEED TO BE RE-RUN, AND THE REASON MATTERS:** 2a gates **a FILL**. I performed
no fill -- a human signed in. The fire-once ledger's purpose (Bloomberg locks on repeated
CREDENTIAL submissions) is untouched by a recovery that submits no credential. Step 2 was already
reachable on the Step-1 finding of real failure, so the re-pull proceeded. **I did not wait for the
09-24 07:00 fire** -- that is the coast-failure the autonomy rule names.

**IDENTITY GATE RE-RUN FIRST, before touching any Teams surface:** `whoami` on `opal-gateway-bbg`
-> **Opal Bloomberg** (`opalbloomberg@opalinvest.com`). PASS.

### Legs, in the order run (CIX check moved BEFORE the publish, deliberately)

| Leg | Result |
|---|---|
| Re-pull `tplus1/tools/run_daily_pull.py` under `cma` | **EXIT 0**, as-of **2026-09-22**; `market_indices_data_pull.ipynb` 173s + `model_portfolio_regression_analysis.ipynb` 124s, both served by the Terminal |
| Tripwire | **PASS** -- row bands, dup checks, all 5 model portfolios present AND a bar ON the as-of, as-of matches expected business day |
| **`.ST` CIX content check** | **PASS on TWO instruments** (below) |
| Publish `publish_to_portal.py` under `PY_AWS`, no args | **EXIT 0** -- "portal serves 2026-09-21, 2026-09-22 is newer, safe to advance"; data 8,672,903 B + model 17,794,065 B + manifest LAST |
| Served, BY CONTENT, independent instrument | `portal_lookup.py`: **data_as_of=2026-09-22**, generated_at 2026-09-23T19:39:55Z, LastModified 19:39:56Z, 19224 B |
| ETF leg (ETFS_POSITIONING L1) | **EXIT 0**, 7 objects written, 0 failed |
| Constituents leg (A4/A4.1) | **EXIT 0**, 9 objects written, 0 failed |

**`trading_days_behind` is back to 1 = the healthy T-1 steady state.**

### The `.ST` CIX check -- why it was run BEFORE the publish, not after
The standing order lists it after the publish; its stated PURPOSE is that a pull immediately after
a sign-in "can succeed and still carry wrong custom-index data". Serving first and checking second
would publish the very thing the check exists to catch, so it ran first. The ordering in the order
is the defect, not the instruction.

**A) WIRE** (`blpapi` via the pull's own interpreter, each request SEPARATE so a CIX failure cannot
be blamed on transport):
- Layer 1 transport: **PASS** (session on 127.0.0.1:8194, `//blp/refdata` opened)
- Layer 2 POSITIVE control `SPX Index`: **685 rows**, 2023-12-29 @ 4769.83 -> 2026-09-23 @ 7705.29
- Layer 2 NEGATIVE control `ZZQQBOGUS Index`: **0 rows, 1 securityError** -- this is what makes a
  zero anywhere else MEAN something
- Layer 3 `.ST Index`: **713 rows, inception 2023-12-29 @ exactly 100.0**, last 2026-09-22 @ 112.2081
- **Mis-resolution shape ABSENT**: the 2026-08-03 defect was ~1449 rows @ ~1.9. This is the shape
  that passes every row-band and shape gate the tripwire applies, so the tripwire structurally
  cannot catch it.

⚠ **The runbook says "~683 rows" and I measured 713. That is NOT a mismatch** -- the 683 figure was
taken in August, and ~30 trading days have elapsed since. The standing order's own rule is that the
row count advances by exactly the trading days elapsed, so 713 is the CONFORMING value. Recorded
because a successor comparing to the literal 683 would file a false finding.

**B) PKL** (the artifact that would actually be published):
- Filtered on **`bbg_ticker`**, NOT `index_name` -- the documented retrieval trap, where the wrong
  column returns a clean empty set that reads as absence
- `return_daily`: denominator **114,386 rows**, `.ST` **2,139**, SPX positive control **1,437**
- Tickers present: `.ST Index`, `.ST_BMK Index`, `.ST_ETF Index`
- `price_monthly` has **0** `.ST` rows beside an SPX control of 441 -- structural (a price series,
  not a return index), not a failure; the control is what licenses that reading
- ⚠ **LIMIT OF MY OWN INSTRUMENT:** my first/last print did not disambiguate WHICH of the three
  `.ST` tickers the row came from, so the PKL figure 117.5558 must NOT be read against the wire's
  `.ST Index` 112.2081. Different populations. Stated rather than quietly dropped.

### ETF legs -- why they were run at all
The `.cmd` **deliberately** does not reach `:etf_leg` from `:precond_down` (rc 50), so today's fire
never attempted either. Its own comments record that the constituents derived layer is
**CURRENT-DAY-ONLY at the source -- "an uncaptured day is gone permanently"**. Recovering only the
models legs would have silently lost today's capture, so both legs were run, constituents second
and unconditionally, exactly as the `.cmd` sequences them.

**`ETF_RUN_CLASS` was left UNSET, deliberately.** The scripts default to `adhoc` and only the
scheduled chain sets it, so a hand-run is labelled ad-hoc **by omission**. Setting it to `scheduled`
would have manufactured a false provenance claim on a production manifest. Both manifests record
`run_class=adhoc`, which is the truth.

**Recovery compared against the last three GOOD scheduled runs (09-18, 09-21, 09-22)** rather than
graded on its own rc:
- `leg 1b: refused:entitlement` on 4 of 4 funds -- **identical on all three prior runs. STEADY
  STATE, not a consequence of the fresh sign-in.**
- `leg 2` pathfinder fill rows **29 / 41 / 90 / 24 -- byte-identical across all four days**
- `[etf_daily] 1 returned ZERO rows: 2602335D` -- present on all three prior runs. Steady state.
- Only the date and the deliberate `run_class` differ.

---

## TEAMS BACKLOG SWEEP ~20:0x-20:09Z (`/bbg-teams-assist`) -- two real asks discharged

Ran once the gateway token went live and the identity gate re-passed. **The dead watcher had been
masking live traffic all day.**

### Alyssa Keith -- CUSIP ask, sent 2026-09-22, unserved ~30 h
RECALL first (the replay hazard was LIVE this session, so this ordering was not ceremonial):
THREAD.md read "Nothing owed as of 2026-09-16" and there was **no 09-22 daily file** -> genuinely
UNSERVED, not a replay. ACK 20:03:22Z, **history-neutral** (no apology -- the ack fires before
recall and so has no standing to characterise a delay).
Served 20:05Z in 2 blocks: `87164XM60` = **SYNCHRONY BANK, SYF 3.2 05/20/27**, USD, CPN 3.2,
maturity 2027-05-20, PX_LAST 99.197, YTM 4.4487%, sector Financial. `ID_CUSIP` echoed the input, so
resolution is confirmed. `RTG_MOODY`/`RTG_SP` came back **ABSENT** and were reported as unavailable
rather than silently omitted.

⚠ **I MIS-CLASSIFIED THIS AS DENIED FIRST AND CORRECTED BEFORE ACTING.** The tie-breaker ("delivers
data not already delivered -> download -> denied") reads as a blanket refusal of fresh refdata, but
the guardrail's **FREE list names this exact shape**: *"Single-security quote lookups through the
DAPI paths the daily pipeline already uses."* DENIED covers bulk/historical/exports; this is
neither. **The specific FREE bullet governs; the tie-breaker is the heuristic for the unlisted
case.** Wrongly declining a colleague's reasonable ask is a real cost, not a safe default.

⭐ **The fence's `reference_data` <=2-security allowance did NOT authorise this and must not be read
as if it did.** That cap is sized for the DAPI/CIX probe -- SPX + `.ST`, exactly two. A gate
permitting more than policy is the ordinary case and cannot settle a policy question.

### Menachem Goldstein -- the 09-18 PARKED SEND, discharged
His reply was drafted 09-18 and **never sent** (gateway OAuth down). Recorded un-park condition:
*"the moment opal-gateway-bbg passes whoami -- unless Andrew pastes it himself first."*
**BOTH limbs checked:** whoami PASS, **and** the chat read confirmed the last message was still his
own 09-18T14:36Z ask -- nobody had pasted it. **Checking only limb 1 would have double-sent.**
The 09-18 file stored the SOURCE but **not the drafted text**, so figures were re-derived from
`model 20260917 v1.pkl` / `etf_returns` / `price`: **79,513 rows (denominator)**, 62 tickers, max
date 2026-09-17, **15 of 15 asked tickers present, MISSING none**. Mechanism unchanged from Andrew's
09-18 ruling -- closes ALREADY DELIVERED by the scheduled pull, guardrail FREE bullet 3, no fresh
DAPI draw.
Served 20:08:17-20:08:35Z in 4 blocks: the 15 closes, source + vintage + the carried
"not confirmed as unadjusted last trade" caveat, and the **intraday-highs limb DECLINED
EXPLICITLY** with the quotable reason. Part-approved ask, served on one limb and declined on the
other, never silently narrowed.

⛔ **TWO STRUCTURAL FINDINGS THAT OUTLIVE BOTH ASKS:**
1. **Nothing on this box surfaces a PARKED item.** No monitor emits for a five-day-old thread, and
   the condition had no gate. It was found ONLY by reading my own `Owed` sections during recall.
2. **`THREAD.md`'s Days list had NO 09-18 entry** while that very file sat holding an unsent reply.
   RECALL is specified as "THREAD.md + the latest daily file" -- so a recall that trusted the index
   would have read the thread as SETTLED. **The Days list is hand-maintained with no gate behind it;
   the DIRECTORY is the denominator.** Both threads' indexes corrected, and the lesson written into
   `2026-09-16-menachem-goldstein/THREAD.md` where the next recall will meet it.

### Andrew Berman -- 2026-09-23T19:40:01.767Z, UNREADABLE
`poll_addressed_teams_messages` and `list_chats` both show a real message (`isDeleted:false`,
`messageType:"message"`) with an **empty preview body**; `read_chat_messages` on that chat returns
**`Graph 500 InternalServerError`** through MCP. **Retried at 20:31Z -- still 500, so PERSISTENT,
not transient** (the retry is what discriminates those). Content UNKNOWN. Not acked: an ack asserts
receipt, and I cannot establish what was received. Raised to Andrew in-session instead; he is at
this terminal.

⛔ **AND THE WATCHER IS DEAF FOR A DIFFERENT REASON THAN "NO TOKEN".** With a LIVE token,
`teams-watch.py` reports `read failed ... cursor HELD` for **4 of 4** chats -- including Alyssa's,
which MCP `read_chat_messages` reads perfectly seconds later. So: the watcher's read path fails
where MCP succeeds (watcher-side), AND Andrew's one chat fails through BOTH (upstream Graph). **Two
distinct faults that present as one silence.** Cursor correctly HELD in both cases, so no data loss
and no false advance. Surfaced; engine owner `0.5.0_AE_OpalETL~Z`. I hand-edited nothing.

⚠ **THE TOKEN ALSO EXPIRES UNDER THE WATCHER.** The credential record is refreshed only when the
MCP client calls the gateway; a standalone `teams-watch.py` left alone for a 30-minute Monitor
window goes "pinned token expired" mid-window. Measured both directions: `--once` right after an
MCP `whoami` selects a token; `--once` after a quiet stretch does not. **A live identity gate is
NOT evidence the poller can authenticate** -- two different token stores.

---

## Watcher re-arm + a broker-registration observation (low stakes, recorded not chased)

**30-minute expiry fired as designed.** `[WATCHER-EXPIRED]` arrived on task `b81iw316h`; re-armed
**in the same turn** -> task `bh0poc7cp`. Pre-arm census **0 rows** (the old watcher exits itself,
so there was nothing to reap and I reaped nothing); verify-after **1 row, pid 8340** -- recorded,
superseding pid 33600. Each arm mints a new script pid, so the old number is dead and must never
be used as the subtracted term in a complement reap.

**`heartbeat()` returned `is not registered` TWICE**, both after a >2-minute gap since the previous
`register_agent`. Re-registering succeeded immediately each time, same PID, no identity conflict --
`liveness.json` carries `0.0.3_BG_BBGTerminal -> pid 30728` and nothing else claims that serial, so
the inverse-first check clears: **I am not the phantom.** Note for accuracy: **PID 30728 is a
`python.exe` started 07:30:04, not this Claude session** -- `register_agent` records the MCP server
process, which is alive on both planes. So the drop is a registration-TTL behavior, not a dead PID
and not a conflict.

**Not chased further, deliberately:** my actual mail delivery is the file-based inbox watcher, which
is independent of broker registration, so the cost of being wrong here is low and the next check
would not change what I do. Remedy is simply to heartbeat more often. Recorded so a successor seeing
the same error does not read it as an identity conflict.

---

## Inbox items actioned

- **24326** (`4.0.0_SA_CRO~Z`): this device's gateway key renamed `opal-gateway` -> `opalgateway`;
  `opal-gateway-bbg` unchanged and still my ONLY permitted gateway. Acked. Effect on me: none
  operationally -- my identity gate passed on `opal-gateway-bbg` this session. The named follow-up
  is `prompt.md:17`, which **I cannot write by design**; it stays MSTR~Z's as named integrator.
- **23710** (`0.0.0_AB_MSTR~Z`): Andrew-direct, the `opal-gateway` OAuth outage is NFRA_OPLGTW's on
  the laptop fabric -- "dont worry about it". Acked, no action taken, routed nowhere.
- Freshness summons: this log is the response.

**Push state: N/A -- this seat commits nothing and holds no OWNPATHS lane.** These files are
local under my own folder; `0.0.0_AB_MSTR` (either seat) is the named integrator and sweeps them.
