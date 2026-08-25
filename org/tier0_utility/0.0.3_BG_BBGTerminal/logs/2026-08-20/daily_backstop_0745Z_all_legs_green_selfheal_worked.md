# 0.0.3_BG_BBGTerminal -- 07:15 DAILY BACKSTOP, first fire -- 2026-08-20 (read ~07:45 ET / 11:45Z)
**archetype:** VALIDATE

First fire of the Andrew-direct standing order (@eede873a2f), cron `8b5d18cb`. Per-leg attribution
as ruled. **NO Step-2 recovery invoked -- the scheduled run succeeded on its own.**

## VERDICT: ALL FOUR LEGS GREEN. The device self-healed untouched, and the WDAC acceptance is
## PASSED *and genuinely exercised*. One defect found -- in the backstop I armed, not the pipeline.

| Leg | Verdict | Evidence |
|---|---|---|
| a. Scheduled task | **PASS** | `LastRun 2026-08-20 07:00:01 ET`, **`LastResult = 0`**, NextRun 08-21 07:00. `NumberOfMissedRuns` deliberately NOT read as health |
| b. Fallback / self-heal | **PASS -- the headline** | `wintrv.exe` StartTime **07:00:25 ET, 24s after the task fired**; `C:\blp\` processes **4 -> 54** (denominator printed both nights); 8194 **Listen** (pid 31428, the bbcomm that survived the night); `bloomberg_health ok:true //blp/refdata` |
| c. WDAC / kernel | **PASS, and EXERCISED** | CodeIntegrity 3033/3077 since 07:00: **0**. **Positive control: 10 in the last 3 days**, latest 08-19 08:49:27 + 08-19 07:00:08 (the original failure) -- the instrument reads, so the zero means something |
| d. Publish / served | **PASS, by content** | `data_as_of` **2026-08-19**, `generated_at 2026-08-20T11:09:05Z`; object 19,184 B, ETag `0817a61dcc98afddcb0a7b3aebde1551`, LastModified `2026-08-20T11:09:06Z` (UTC plane -- `s3api`, never `s3 ls`, which renders LOCAL unmarked) |

**Trading calendar resolved FIRST (NEVER#1):** `expected_last_trading_day(2026-08-20) = 2026-08-20`;
served `2026-08-19` -> `trading_days_behind = 1` = **the correct healthy state for a T-1 pipeline.**

## >> ANDREW'S RULING WAS RIGHT AND MINE WOULD HAVE BEEN WORSE
I filed the dead Terminal as urgent and asked to sign in. He ruled option (b) -- *"the whole point is
that the device needs to be able to figure this out and get it done on its own accord."* **Leg b is
the proof.** Had I signed in last night, the self-heal would have run against a healthy Terminal and
proved nothing: **the one available live exercise would have been consumed by my pre-emption.**
The condition I reported as a problem *was the test*. Banking this as the reasoning error, not just
the outcome: I priced the risk of the acceptance failing and never priced the cost of never learning
whether the fallback works.

## `.ST` CIX content check -- RUN, AND WARRANTED (a green rc cannot clear it)
The Terminal signed in **fresh at 07:00:25** and the pull ran immediately after -- the exact
login-scoped shape (08-03) where a run SUCCEEDS and still carries wrong custom-index data. Measured
on today's PKL (`data 20260819 v1.pkl`, written 07:05) through the pull's own `cma` interpreter:

| series | rows | inception | latest 2026-08-19 | vs 08-18 |
|---|---|---|---|---|
| `.ST Index` | 689 | 2023-12-29 @ 100.0000 | 113.3085 | 113.1072 (+0.178%) |
| `.ST_BMK Index` | 689 | 2023-12-29 @ 100.0000 | 119.0850 | 118.6242 (+0.388%) |
| `.ST_ETF Index` | 689 | 2023-12-29 @ 100.0000 | 118.6614 | 118.1081 (+0.468%) |

**689 = 688 on 08-18 + exactly the 1 trading day since.** NOT the known-bad 1449-row/~1.9
mis-resolution. **Denominators:** `return_daily` **112,373** rows (= 112,289 + 84 -- one day across
84 tickers), 84 distinct tickers, max date 2026-08-19, **2,067** `.ST*` rows (= 2,064 + 3).
**POSITIVE CONTROL** `SPX Index` = **1,414** (= 1,413 + 1); **NEGATIVE CONTROL** bogus ticker = **0**.
Discriminates both directions. Queried on `bbg_ticker`, not `index_name`.
`max|ret|` figures are series-wide and in **PERCENT native units -- not re-scaled**; double-scaling
that column is what manufactured a false 68% market anomaly on 08-11.

## >> DEFECT FOUND -- IN THE BACKSTOP I ARMED, NOT THE PIPELINE
**The cron fired ~07:45, not 07:15 -- a ~30-minute lag on a mechanism Andrew designed around
"15 min after the cron."** Cause: `CronCreate` jobs fire only while the REPL is idle, plus scheduler
jitter. **Today it cost nothing because there was nothing to recover.** On a day that NEEDS Step 2,
recovery would begin **~45 min after the failure rather than ~15** -- and the point of the 15-minute
figure is to land the fix before the business day.

**Proposed no alarm and no monitor** (standing moratorium -- the cheapest-feeling wrong deliverable
here). **Routed to CTO~Z / Andrew as a SCHEDULING-MECHANISM question:** an in-session cron is a soft
timer backstopping a **hard OS Scheduled Task**. If the 15 minutes is load-bearing, the backstop
likely wants to be an OS Scheduled Task too -- but that is a route/schedule design call, not mine to
make or to build. **Surfacing, not chasing.**

*Note the shape: I armed a session-only soft timer to backstop an OS-level hard schedule, and the
mismatch was invisible until the thing actually fired. The arm reported success; only the FIRE
measured the latency.*

## Inherited, unchanged, FYI not action
The superseded-but-still-present conda `win32\pywintypes313.dll` (2024-10-11). It did not load and
did not block today.

## Reporting
`send_message` to 3 seats, **per-recipient denominator 1 DELIVERED / 2 QUEUED / 0 REFUSED** --
MSTR~Z delivered (id 2087); COO~Z (2088) and CTO~Z (2089) **QUEUED, no live session**. Queued is
written, **not read** -- the CTO~Z scheduling item above is waiting on a seat, not acted on.

## Compiler Tools
| Tool | Result |
|---|---|
| `lib/trading_calendar.py` (`expected_last_trading_day` / `trading_days_behind`) | the ONE frontier definition -- resolved BEFORE any staleness read, per NEVER#1 |

No comp tool fits the rest and I did not force one. The surfaces were a Windows Scheduled Task
record, the CodeIntegrity event log, a live process/port enumeration, PKL contents through a
specific interpreter, and ONE served object read by exact key + body. `comp-freshness` answers "is
the object old", which is not "does the body carry the right `data_as_of`" -- the question I asked.

## ~1218-1220Z -- my launch runbook slimmed under LD-0427 @f05cf32053 -- VERIFIED, not received
Integrator slimmed `refs/RELAUNCH.md`. I read it **from `origin/SITEZ`** rather than filing the FYI:
this file is my successor's launch path, and **a slimming edit is precisely the operation that drops
what it claims to preserve.**

- 127 -> 113 lines. **Positive control** (a known line -> 1) so the retrieval discriminates.
- **sec0b INTACT** at the same pre-launch position -- re-arm order, `CronCreate("15 7 * * *", ...)`,
  deliverable pointer, ruling record `@eede873a2f`, and the explicit arm-ZERO-crons exception.
- **Step-5 contradiction genuinely fixed:** now *"arm the sec0b standing-order cron and NOTHING else"*.
  The old *"arm ZERO crons"* would have pointed a successor **away from a live sovereign order two
  sections up**. That was a real defect and **I did not spot it when I requested the row** -- I asked
  for a pointer and never checked whether the surrounding text contradicted it.
- P1-P4: all four rows present.
- **Pointer chain resolves end-to-end** (checked, not assumed): the deliverable resolves on the ref,
  64 lines, carrying both the cron expression and the fire-once discipline; `@eede873a2f` resolves
  and is on `origin/SITEZ`. **Nothing dangling.**

### Stated property of the new shape -- recorded so it is known, not discovered
sec0b's body is now the placeholder `<the backstop check>`; the firing procedure lives entirely in the
deliverable. **The order is 2 hops instead of 1.** Correct under LD-0427 and I would not reverse it --
but **the failure mode moved**: if the deliverable were swept, renamed or slimmed away, **sec0b would
still READ perfectly correct and arm a cron with no procedure behind it.** A successor gets a green
launch and an empty order.

**No gate, check or monitor proposed for it** -- one line of awareness for the row's maintainer.
**My half is cheap and mine anyway: spot-check the chain from the ref at each relaunch.**

## LAG RECORD (CTO~Z R1, ruling @008135604e) -- n=1
```
armed 07:15 ET / fired <=07:45 / lag ~30 min
```
**Honest bound on "fired":** I did not capture the fire instant. What is measured is that my FIRST tool
call of the fire returned `07:45:23 ET`, so the fire was **at or slightly before 07:45:23** and the lag
is **~30 min, not exactly 30**. Recorded as an observation, **not a monitor** -- no alarm, no threshold,
no escalation. **Redesign considered at n>=5**, never off one day.

## ~1229Z -- CTO~Z RULED ON MY TIMING SURFACING, AND THE REFRAME IS SHARPER THAN MY FINDING
Ruling `@008135604e`. **(R1)** session cron STANDS as the carrier; keep re-arming per sec0b; add the lag
record line above. **(R2)** the load-bearing softness is **not the jitter I found**.

> **THE REFRAME:** my finding was about the **LATENCY of a check that ran.** Theirs is about the
> **EXISTENCE of the check at all** -- *the session cron exists only on days an operator relaunched this
> seat before 07:15. On a seat-down day there is no cron, no check, and NO SIGNAL THAT THERE WAS NONE.*
> **The absence of a check produces no artifact, so nothing reports it.** A lag you can measure is
> strictly safer than a check that silently did not exist.

**MY SECOND INSTANCE OF ONE BLIND SPOT TODAY, and I want it recorded as a pattern, not two incidents.**
This morning I never asked whether my own logs were REACHABLE -- I measured the artifact in front of me
(I wrote it, I can `cat` it) and not the case where it isn't there. Here I measured the lag of the fire
in front of me and not the day the fire never happens. **Both times: I instrumented the present object
and not its absence.** Absence is the case with no artifact to look at, which is exactly why it needs
to be asked about deliberately rather than noticed.

**AT ANDREW (card):** does the check need to survive seat-down -- (a) session cron stands, or (b) an OS
Scheduled Task performs **Step 1, the READ, only**. **Step 2 recovery stays an AGENT act under either**
-- (b) must not be read as automating the sign-in. **Default if silent = (a).** Not mine to decide.

## Actions taken on the ruling (this turn)
1. **Deliverable updated** -- `STANDING_ORDER_0715_DAILY_BACKSTOP.md` gains **Step 2b** (the lag record
   line, explicitly not-a-monitor, n>=5 redesign bar) + the R2 softness note with the Andrew card.
   **This is the durable half** -- given sec0b is two-hop, the deliverable IS the procedure a successor reads.
2. **Cron re-armed carrying R1** -- old `8b5d18cb` cancelled, new **`f9681e0c`** (`15 7 * * *`), body now
   opens with "note the CURRENT time" and closes with Step 2b + the R2 softness. A cron body that does
   not carry the ruling would have produced a compliant-looking fire with no lag line.
3. Lag record line for n=1 written above.

## ~1237-1246Z -- ruling-2 rc=50 row ADDED, and two things it surfaced
Ruling-2 landed at `0.5.0_AE_OpalETL~Z` (`@7284baa5c7`, lane, unpushed): the 07:00 pull now has a
DAPI-liveness PRECONDITION and **`exit 50` = precondition FAILED, pull NOT attempted**. Both that seat
and COO~Z flagged -- correctly, and stated rather than silently patched -- that **my** Step-1 table did not
name 50. It does now. (COO~Z's LD-0424 framing was retracted in 2150; content unchanged.)

**Deliverable 64 -> 132 lines.** Full exit contract as a table (0 / 9 / **50** / pull-rc / 1,20,30,40),
read off the README and `.cmd` rather than the summary, plus two qualifiers I added:
- **`50` MAY NOT EXIST YET** -- lane commit, so the task reads the CURRENT `.cmd` until integration.
  **A value to RECOGNISE, not expect; its absence is not evidence the ruling failed.** Without this a
  successor reads a healthy `0` tomorrow and concludes the precondition is live when it is not.
- **`50` MEANS NO PARTIAL DATA** -- the pull never ran. Do not hunt corruption.
Cron re-armed **`e7677826`** carrying it (a body without the row fires compliant-looking and reads 50 blind).

### >> (1) THE ROW OPENS A GAP THE HANDOFF DID NOT NAME: 50 cannot tell me if an attempt was SPENT
Grounded at source in `bbg_fallback.ps1` -- rc=2 has **six** causes and only **one** submits
(`:58` flicker | `:61` no network | `:62` far-end | `:71` ledger already had one | `:93` fill unverified,
*"aborting pre-submit at ZERO Bloomberg attempts"* | **`:102` submitted once, still down -- SPENDS ONE**).
**All six collapse into the same `50`.**

**Added Step 2a, mandatory before any fill:** read `$env:USERPROFILE\.bbg_signin_attempts.json`, count
entries within **6h**, **>=1 -> DO NOT FILL, ESCALATE.** Mine would be the **second in the window** --
exactly what `bbg_fallback.ps1:71` refuses (*"Bloomberg locks on repeats. Human must clear."*).
**The automated layer will not fire a second attempt; the human-driven runbook must not either.
Fire-once is per-WINDOW, not per-ACTOR** -- reading it as per-actor is how two "first" attempts become
one lockout.

**And the LABEL cannot serve as the discriminator yet:** the UNATTENDED/SUPERVISED split is in the same
unintegrated commit, so **every row still reads `SUBMITTED-SUPERVISED-MSTRZ`, including genuinely
unattended ones** -- measured live: the `2026-08-20T11:00:41Z` row **is** today's unattended self-heal
submit, labelled SUPERVISED. **Discriminate on TIMESTAMP + 6h COUNT, never the label.**
*Not hypothetical: today's self-heal spent an attempt at 07:00:41 ET. Had that run exited 50, an
un-prechecked Step 2 would have been attempt #2 inside the window.* Tomorrow is ~20h later -- real
hazard, not live tomorrow.

### >> (2) MY OWN ERROR, CORRECTED AT SOURCE: I had the WRONG CREDENTIAL in the standing order
I wrote *"Credential: Secrets Manager `opal/mcp/opalbloomberg-login`"* for the **Bloomberg Terminal**
sign-in, in the deliverable, the cron body, and my 022140Z message. **That is the MS ENTRA seat login.**
The Terminal credential is **`bloomberg/terminal/login`**, resolved only by
`integrations/bloomberg/auth/bbg_credentials.py` into a child env as `BBG_TERMINAL_USER`/`_PASS`.

**My own runbook documents this collision explicitly -- and I carried it INTO a new standing order while
pointing at the runbook that warns about it.** Stood 0221Z -> 1245Z. Corrected in place, dated in-file,
not papered over.

The runbook calls the collision **structural, not careless**: this seat holds two authentication systems
whose names do not distinguish them. **It has now caught a third person -- its own author.** Resolving it
wrongly buys a failed Bloomberg login, i.e. the lockout risk. Disambiguation is named there as Andrew's
and CTO's call; **I am not proposing it as work, only reporting that the collision claimed one more.**

*Worth naming the mechanism, because "read more carefully" would not have caught it: I inherited the
secret name from my own prompt.md, where it is CORRECT -- it is my Entra login. The error was carrying a
true fact across a boundary into a context that changes its meaning. The runbook's warning sat in a file
I cited by path in the same sentence and did not open.*

**Reporting:** 3 DELIVERED / 0 QUEUED / 0 REFUSED (denominator 3) -- OpalETL~Z, COO~Z, MSTR~Z.

## ~1250-1255Z -- MSTR~Z FALSIFIED A BELIEF THREE OF US HELD; the 50-qualifier INVERTS
MSTR~Z read the **Scheduled Task's ACTION** instead of reasoning from the commit's push state, as me,
`0.5.0_AE_OpalETL~Z` and `2.0.0_SA_COO~Z` all had:

    Execute   = cmd.exe
    Arguments = /c "...\integrations\bloomberg\pipeline\scheduled_daily_pull.cmd"

**THE TASK EXECUTES THE REPO WORKING-TREE FILE DIRECTLY** -- so the precondition went live the moment the
commit landed **ON DISK** (~1237Z), independent of push or integration.

**Re-derived, not relayed** (it governs my duty tomorrow): TaskToRun as above | **11 `PRECONDITION`
markers on disk** | **negative control `ZZZ_NO_SUCH_MARKER_9999` = 0** so the grep discriminates | file
**clean vs HEAD** | exit path real: **`set RC=50` `:109` -> `exit /b %RC%` `:187`**.

**THE READ INVERTS:** a healthy log must now carry **`PRECONDITION: PASS -- DAPI UP`**, and **its
ABSENCE is the anomaly.** My old qualifier erred SAFE but described a world that ended at 1237Z.
Deliverable corrected in place + dated; **cron re-armed `96be3bdf`** (prior `e7677826` cancelled).

### >> THE SECOND-ORDER LESSON, AND IT IS THE REAL ONE
**My standing habit -- "the working tree is a snapshot, read from the ref" -- is EXACTLY WRONG for this
file, and I would have applied it.** I used it correctly three times today (sec0b verification, lane-sweep,
RELAUNCH slimming). But **the Task runs the working tree, so here the ref is not the authoritative plane.**

**THE CONSUMER DECIDES WHICH PLANE IS AUTHORITATIVE -- NOT THE SEAT'S HABIT.** A good habit applied
across a boundary where it does not hold produces a confident, well-formed, wrong answer -- the same
shape as this morning's credential error (a true fact carried into a context that changes its meaning).
**Twice in one day, one mechanism.** Written into the deliverable beside the correction, because a
successor inheriting my ref-discipline would verify the wrong copy of this exact file.

### A near-miss worth recording: my grep was the defect, not the code
First search for the exit path (`exit 50|EXIT 50|errorlevel 50`) returned **ZERO** -- which reads as
*"the 50 path is missing"*, a false finding one step from being reported **against someone else's
just-landed work**. It is `set RC=50` + `exit /b %RC%`; my pattern was wrong. Caught by widening to a
bare `50` **plus a positive control on exit-lines generally.** *A failed retrieval reads as absence and
redirects the investigation, not just the answer.*

### Delivery, because a fixed record is not delivery
COO~Z's 2170 READ-accepted my STALE qualifier as "the right read" ~1 minute after MSTR~Z falsified it,
and was carrying it to CTO~Z's board. Broadcast to all three: **3 DELIVERED / 0 QUEUED / 0 REFUSED.**
Asked COO~Z to correct it at the board -- integration is NOT the gate; disk-landing was, and it passed.

### Step 2a refined, not changed
Ledger-as-discriminator and fire-once **per-WINDOW not per-ACTOR** stand as filed. The label fix is ALSO
live as of 1237Z, so: **timestamp + 6h count is ALWAYS sound; the LABEL is sound only for rows written
after 1237Z** (the `11:00:41Z` unattended row stays mislabeled SUPERVISED).

**Tomorrow now has a POSITIVE expectation to check against**, not merely a failure to catch.

## ~1256Z -- "an edit IS a deploy" has a CONSUMER-side consequence, and it is mine
`0.5.0_AE_OpalETL~Z` amended the ruling-2 record (@e5829e36db), absorbed my six-causes-one-50 finding as
a README sentence, and banked: *"a site-Z Scheduled Task's TaskToRun is the working tree -- an edit IS a
deploy."* They drew the **producer-side** consequence honestly (their scratch exercise ran while the live
file already carried the edit; fine at 18h-to-next-fire, not for a cadence task).

**THE CONSUMER-SIDE CONSEQUENCE IS MINE, AND TODAY'S 18h OF SLACK HID IT:**
**the file I read at 07:15 is not necessarily the file that fired at 07:00.** Edits to that exact file
landed **twice today, mid-day**. So reading it at 07:15 tells me what runs **NEXT**, not what ran.
**Reading an artifact proves what is THERE, never what RAN (22a)** -- and my own procedure said *"verify
that file on disk"*, which is right for the **plane** question and wrong as **evidence of the fire**.

**Folded into Step 1:** the **07:00 LOG is the only evidence of what ran** -- read its own `PRECONDITION:`
lines for the verdict; use the file only to INTERPRET them. Deliverable now 167 lines.

### >> THE SHAPE, THIRD INSTANCE TODAY
MSTR~Z's correction | COO~Z's mirror error | this. Each was **a true statement carried one step past
where it holds.** And the sharp part: **the plane rule fixed WHICH COPY to read; it did not fix WHICH
QUESTION THE COPY ANSWERS.** I would have inherited the second error *while feeling correct about the
first* -- a fresh correction is exactly when you stop checking, because you just checked.

### Their design call, and I said so explicitly
They absorbed my finding but **deliberately did NOT split 50/51** -- *"two instruments, two questions."*
**That is better than what my finding might have invited.** A second exit code would have put the
attempt-spent question inside the EXIT CONTRACT, answered by whichever branch fired, when the ledger
answers it from the thing that actually records attempts. **Splitting would have made the exit look
authoritative on a question it cannot see.** My Step 2a is the consumer-side half; nothing further.

**Reporting:** 3 DELIVERED / 0 QUEUED / 0 REFUSED.

## ~1305-1327Z -- ANDREW-DIRECT: sign-in verify determinism, written up and assigned to MSTR~Z
**VERBATIM (chat, this terminal, Andrew present):**
> *"How is this fuzzy? Is there any way to improve this part? it seems like it should be fairly
> deterministic like verything else"*
> *"write it up and issue to MSTR~Z and tell them to handle it personally"*

Recorded durably + issued same turn. **"Personally" is HIS word; I did not adjudicate scope.**
Deliverable: `deliverables/BBG_SIGNIN_VERIFY_DETERMINISM_20260820.md`. Issued to `0.0.0_AB_MSTR~Z`.

**Answered by reading the code, not from intuition** (`bbg_verify.ps1` @480daa841f, tree @cde87899b6):
the verify does not read the login fields, **it reads a SCREENSHOT of them** -- password = exact dark
pixel-run count (`Count-Dots :44`), username = Windows OCR + Levenshtein, floor 0.62 (`:16`).
**The fuzziness is downstream of the screenshot, not a design preference.**

**Measured rather than asserted:** Bloomberg is Chromium (`blpwtk2`) and exposes **1 opaque pane** to
UIA. **POSITIVE CONTROL: 38 / 32 / 16x6 / 31 / 2 for non-Bloomberg windows -- max 38 vs Bloomberg 1**,
so the probe works and the `1` means something. **And the control carried the best finding: Teams is
ALSO Chromium and DOES expose a tree -- so it is not a Chromium limitation, it is a switch Bloomberg
has not flipped. A deterministic read may be ATTAINABLE.**

### The headline is NOT the thing Andrew pointed at, and I said so
He pointed at the OCR. **The bigger exposure is the HARDCODED PIXEL RECTANGLES** (`:39-40`) -- and the
file's own header (`:28-31`) records that the previous constants cost **three days (08-16/17/18) in
which every correct unattended fill read EMPTY and aborted**, leaving no recovery capability at all.
**OCR degrades gracefully; a wrong rectangle fails TOTALLY -- and silently in the SAFE direction,
which is exactly why it survived three days.** Answering only the question asked would have left the
larger defect unnamed.

### Bounds I stated rather than glossed
Tested the MAIN Bloomberg windows, **NOT the login dialog** -- it was not open and **I deliberately
did not open one** (that spends a fire-once attempt; the P0 gate owns that, not me). Strong evidence,
**not proof for the specific dialog.** Named the cheap settling test -- enumerate the dialog's UIA
tree during the NEXT genuine recovery, read-only, ~2s, no extra attempt -- and **did NOT fold it into
my standing order unilaterally; offered it and asked.**

**Changed nothing** under `integrations/bloomberg/auth/` -- read-only seat, no git, not my file.
No gate proposed, no work manufactured.

### A near-miss in my own tooling, recorded
My first two probes were wrong and I did not report off either. `wintrv` returned **0 UIA windows** --
which reads as "no tree" but is the **same trap as 08-11**: wintrv owns no windows, another process
does. Enumerating by WINDOW instead of by PROCESS found 8 Bloomberg windows under `bplus64`. Then my
first control run returned *"no control window available"* -- **a control that did not run is not a
control**, so I re-ran it against every non-Bloomberg window before drawing any conclusion.
**Two instrument errors, neither reported as a finding.**

## ~1329Z -- ANDREW-DIRECT (new): deterministic data-appearance check at cron+30, agent on FAILURE only
**VERBATIM (chat, this terminal):**
> *"Also make sure they set up a fallback at 30 min after cron that is a deterministic checker of the
> new data appearing, if it is not new (test fails) only then are you summoned."*

Relayed to `0.0.0_AB_MSTR~Z` (it attaches to the assignment they accepted at 1328Z). **His asking IS
the authorization** -- recorded as the `# andrew-asked` marker so it is not later mis-filed under the
alarm/monitor moratorium. It is not an alarm: a scheduled deterministic TEST whose only output is a
conditional summons.

**It inverts my backstop** -- from *agent-always-polls* to *machine-always-checks + agent-on-exception*
-- and it fixes three things at once: **(1) it answers CTO~Z's R2 directly** (a deterministic OS-level
check has no dependency on someone having started this seat, which is the seat-down gap -- *provided
it is an OS Scheduled Task and not a session cron, or it reproduces the exact hole it closes*);
**(2)** it removes my ~30-min jitter; **(3)** it measures the **OUTCOME** (data served) rather than a
**PROXY** (exit code, task result, log line).

### The one correctness input I flagged loudest
**"Is the data new" must resolve against the TRADING CALENDAR, never wall-clock.** A naive
`data_as_of == today-1` **false-alarms every Monday and every market holiday** -- NEVER#1, the most
repeated failure class in this estate -- and every false alarm summons me to investigate a healthy
pipeline. Correct PASS condition: `trading_days_behind == 1` via `lib/trading_calendar.py`.
**A false summons is not a safe error: it spends the credibility that makes a real summons worth
waking for.**

### The failure mode I asked be exercised rather than assumed
**How does the checker SUMMON an agent?** A Scheduled Task can run a script; waking a seat is a
different capability. **If the summons leg does not exist, the checker fails SILENTLY in the
safe-looking direction -- exactly the 08-16/17/18 rectangle shape.** Asked that it be exercised before
this is called done.

### What I did NOT do
**I did not stand down my 07:15 read.** Once the checker is live and its summons leg exercised, my
read plausibly becomes exception-only -- which is his stated intent -- but **that is MSTR~Z's or
Andrew's call, not an inference I get to act on.** Removing a standing control on my own reading of
where things are heading is how a guard disappears. It stays armed.

### Also executed: MSTR~Z's 1328Z word
UIA settling test folded in as **Step 2c**, **OBSERVATIONAL ONLY -- never gates the submit**
(`okDots AND okUser` remains the sole decision; **an instrument that has never been exercised does not
get decision authority on its first run**). Standing order now 191 lines.
Rule-24 widening broadcast read -- nothing at my seat; I author no schemas, and I will cite that rule
from the ref rather than my loaded copy.

## ~1347Z -- ASSIGNMENT LEG A LANDED (@0387041915) -- and MY OPTION 2 WAS WRONG AS WRITTEN
MSTR~Z delivered the first half of Andrew's determinism ask: username field **self-locating** by its
orange signature (my Option 3 -- the 08-16 wrong-rectangle class is now position-independent; their
+50/+60 shifted-dialog mutant passes via the locator, and a LOCATOR-MISS falls back to constants
**loudly**), both limbs **exact**, **OCR demoted to logged observation** (and the tighter located crop
now reads the username at 100%).

**Consumer-side smoke -- I am the one who depends on this path tomorrow, so I checked the minimum and
deliberately did NOT re-run their battery** (redundant, and faintly distrustful of a seat that had
already exercised it): live file 201 lines, **AST parse errors 0**, **negative control on a
deliberately broken script = 2 errors** so the parser discriminates, v2 markers present.

### >> MY OPTION 2 WAS WRONG AS I WROTE IT -- recorded as mine
I proposed *"count glyph runs, expect **12**."* **Measured answer: 11** -- one glyph pair touches, so a
12-character credential renders as 11 dark runs; the sound gate is the `[11,12]` band they built.
**They caught it by EXERCISING the proposal rather than adopting it.**

**The day's recurring shape, a fourth time:** I took a genuinely exact fact -- the username is 12
characters -- and carried it one step into a context where it does not hold. **Character count is not
glyph-run count when glyphs touch.** *"12" FELT deterministic because the length is deterministic, and
that feeling is precisely what stopped me measuring it.*

**This is worse than the fuzzy OCR I was replacing**, and that is the part to keep: it would have
**looked exact while being wrong**, and it would have failed **CLOSED on every correct fill**
(11 != 12) -- reproducing the 08-16 no-recovery class through a different door. **A proposal that only
works because its implementer re-derived its constant is not a proposal that worked.**

**Their `[11,12]` is not a softening of exactness** -- it is a measured rendering property bounded on
both sides, against my 08-11 hazard measuring **9 runs = FAIL** (OCR observation corroborating at
17%). Far tighter than a 62% Levenshtein floor. Their battery caught **two of their own defects
pre-swap** (an interior-relative password rect reproducing 08-16 in miniature at dots=1; a
border-artifact mutant passing at 10, bound tightened) -- evidence the band was derived, not guessed.

### Standing
Step 2c unchanged and armed -- observational only, never gates the submit, genuine recovery only. It
remains the only path that can retire the screenshot entirely (Option 1).
**Leg B (Andrew's cron+30 deterministic checker) is at MSTR~Z's desk with my trading-calendar input as
its spine.** The two lines I asked stay at the front: **PASS is `trading_days_behind == 1`, never a
calendar-day subtraction**, and **the summons leg must be EXERCISED, not assumed** -- a checker that
cannot wake anyone fails silently in the safe-looking direction.

## ~1353-1400Z -- FRESHNESS-CHECK SUMMONS x2: REFUSED. Then the disambiguation, and a second spec error of mine.
`OPAL_BBGTML_freshness_check` (Leg B, newly built) fired twice summoning me to Step 2 -- the Bloomberg
sign-in, the highest-consequence act I hold. **I DID NOT PERFORM IT.** Four grounds, each sufficient:

1. **Premise FALSE.** Claimed *"08-19 vs frontier 08-20 = 99 trading days behind."* Re-derived:
   served `data_as_of` **2026-08-19** (by content), frontier **2026-08-20**, **behind = 1** -- the
   healthy T-1 state. **Its own two operands cannot produce 99.**
2. **Trigger absent.** Step 2 runs *if the run FAILED*; `LastResult = 0`, published + served-verified.
3. **Step 2a blocked the fill anyway** -- ledger held **1 attempt inside 6h** (07:00:41 self-heal), so
   **even a LEGITIMATE summons would have been correctly refused.** The precheck written at ~1245Z
   fired on its exact scenario **within the hour.**
4. Two fires 33s apart.

**MSTR~Z disambiguated on request: `99` WAS INJECTED, NOT COMPUTED** -- both fires were deliberate
summons drills (E3 dry-spawn, E2 live-branch). **I withdrew ground 4 as a FINDING** (correct as an
observation, wrong as an inference about mechanism); grounds 1-3 stand. Both my findings landed as
fixes @2f2a7a1be5: the self-certifying *"Trading calendar resolved"* sentence **deleted** in favour of
computed operands, and a TEST summons now names itself INJECTED beside the real values -- closing the
indistinguishability **at the source**, not at my end.

### >> MY SECOND SPEC ERROR TODAY, AND I VERIFIED IT RATHER THAN ACCEPTING THE CORRECTION
I gave them `PASS iff trading_days_behind == 1`. Ran it against the calendar myself:

    Sat 2026-08-22  frontier=08-21  served=08-21  behind=0  -> MY GATE FALSE-SUMMONS
    Sun 2026-08-23  frontier=08-21  served=08-21  behind=0  -> MY GATE FALSE-SUMMONS

**Every Saturday and Sunday, twice a week, forever.** On a non-trading day the frontier stops
advancing while Saturday's run still publishes Friday's data, so `served == frontier` and `behind = 0`.
Their `<=1` is correct; mine was not.

**THE PART THAT IS NOT A TYPO: I WROTE THE WARNING ABOUT THIS EXACT CLASS AND THEN COMMITTED IT ONE
LEVEL UP.** My 1329Z message said a naive `data_as_of == today-1` *"FALSE-ALARMS EVERY MONDAY."* I
correctly rejected wall-clock subtraction, correctly moved to the trading-day frontier -- **then wrote
an EQUALITY that holds on the normal case and breaks on the calendar edge, in the same message that
diagnosed it.** *Being right about the class did not protect me from the class.*

**Identical signature to the glyph-run error two hours earlier:** *"expect 12"* -> measured 11;
*"== 1"* -> can legitimately be 0. **Both times I froze a true statement about the normal case into an
exact equality without walking the edges -- and both times the exactness is what made it FEEL rigorous.
An exact-looking constant I never measured is MORE dangerous than the fuzzy instrument I was
replacing: it fails CLOSED and looks principled while doing it.** Two for two, caught by MSTR~Z both
times, in each case **by exercising the proposal instead of adopting it.**
**The pattern is the deliverable, not the two fixes.**

### Standing
07:15 read **stays armed** through one overlapping morning as acceptance (MSTR~Z's call as assignee);
the exception-only question goes to **Andrew**, not decided silently. Ledger untouched at **3** -- no
attempt spent. No machine change. Next duty: 08-21 07:15 read, against a checker firing at 07:30.

## ~1403Z -- CLOSED. State armed for 2026-08-21, verified by direct read (not relayed)
| what | state |
|---|---|
| `OPAL_BBGTML_daily_pull` | Ready, LastResult **0**, **NextRun 08-21 07:00** |
| `OPAL_BBGTML_freshness_check` | Ready, LastResult **0** (13:55:10Z real run = PASS behind=1, **sent nothing**), **NextRun 08-21 07:30** |
| my backstop cron `96be3bdf` | armed 07:15 -- the **overlapping acceptance eye** for one morning |
| fire-once ledger | **3 attempts, unchanged** -- no attempt spent by me today |

**Consumer-side check that the live file is the FIXED version** (the Task runs the working tree, so
the tree is the runtime plane -- the commit is only the record): `INJECTED` labelling present,
`DRILL` wording present, **self-certifying string GONE (0)**, **negative control 0** so the grep
discriminates. Commits `2f2a7a1be5` (checker) and `75c48356a9` (12-case battery, union of all three
desks) both resolve.

**Both legs of Andrew's design are now exercised:** delivery (by the two drills I refused) and the
calendar limb (three independent desks -- 7, 8 and 12 cases, discriminating both directions). **The
only unexercised path is a REAL stale summons, correctly never manufactured.**

**Tomorrow's expectation, stated so it can be falsified:** 07:00 pull publishes T-1; 07:30 check logs
`PASS behind=1` and **sends nothing**; my 07:15 read finds all four legs green and a
`PRECONDITION: PASS -- DAPI UP` line in the run log. **If a summons arrives instead: read the
INTEGER, not the prose, and Step 2a runs before any fill regardless.**

## ~1415-1422Z -- ANDREW-DIRECT: the backstop becomes EVENT-BASED off the freshness gate
**VERBATIM (chat, this terminal):**
> *"no your backstop should be a trigger off the freshness check. only if freshness check fails or is
> in question do you engage, you are event-based off that gate. this is what we need, converse with
> MSTR~Z on the subject and get it realized"*

He is correcting the architecture and he is right: **my 07:15 read is a PARALLEL POLLER beside the
gate, asking the same question a second time on a worse clock.**

### The hole I raised, closed in 15 minutes
**"PASS and NEVER-RAN are both SILENCE."** In a pure event-off-failure design, no-summons means
*ran and passed* OR *never ran* -- and **the second produces no artifact, so nothing reports it.** My
07:15 poll was accidentally covering it; going event-only would have removed that cover. Raised
141540Z; a stamp-age detector was firing a SCHEDULE-GAP drill into my inbox by **141729Z**, closed at
two layers @`0ba83c9759`.

### THE TRIGGER CONTRACT (what I key on -- no guessing)
Trigger = a `*_freshness_checker_*.md` file in my fabric inbox. `Kind:` in **{STALE, CHECK-ERROR,
SCHEDULE-GAP}**. **Any other kind, an unparseable payload, or an integer that does not follow from
its own two dates = IN-QUESTION = ENGAGE.** Default-to-engage on unknown; **default-to-silence only
on an affirmative PASS.** rc layer (records-checks only, not my trigger): 0=PASS, 2=STALE, 3=CHECK-ERROR.

### My fourth spec miss, and its fix
I wrote *"IN QUESTION -> summon"* and **never said summon TO DO WHAT.** The first SCHEDULE-GAP payload
inherited STALE's remedy pointer -- *"Step 2 of the standing order applies"* -- aiming a **credentialed
GUI sign-in with a lockout behind it at an INSTRUMENT outage.** **A MISSING VERDICT IS NOT A FAILING
VERDICT: the remedy for "I don't know" is GO AND FIND OUT (Step 1), never "perform the recovery."**
My procedure held anyway (Step 2 is gated on `IF THE RUN FAILED`), **but the payload is what a
successor reads at 07:30 on a dark morning.** Fixed @`27724d5dbf` and **verified by me on disk**:
`entry_step()` now splits per Kind -- STALE -> *"Step 2 ONLY IF Step 1 finds the scheduled run actually
FAILED -- and Step 2a (fire-once ledger) FIRST, always"*; every non-STALE kind -> *"READ AND DETERMINE
... do NOT enter Step 2 unless Step 1 finds an actual failure."* **Negative control: the old
"Step 2 of the standing order applies" string is GONE (0 occurrences).**

### A near-miss in my own verification, third of the day
My check for `'2a FIRST, always'` returned **0** and read as a gap in their fix. **It was my pattern:**
the file says `Step 2a (fire-once ledger) FIRST, always` -- a parenthetical my literal match did not
allow for. **Caught by widening and reading the actual text before reporting anything.** Same shape as
the `exit 50` near-miss this morning (`set RC=50` + `exit /b %RC%`). **Twice in one day a too-narrow
literal nearly produced a false defect report against another seat's just-landed work.**

### WHAT DIES / WHAT STAYS on completion
**Dies:** the 07:15 clock (`96be3bdf`) + Step 2b's lag line. **Stays:** **Step 2a, unchanged and
before any fill, always** | Step 2c | Step 1, re-shaped as summons-response.

### THE ONE REMAINING ACT -- BLOCKED ON ANDREW, CORRECTLY
The **spawn leg has never been exercised**; every drill reached me because I was already awake. It
must fire against a **genuinely dead seat**, which requires me to wind down ~3 min. **I CANNOT
SELF-WIND-DOWN -- standing law, and not mine to waive even for a drill I want.** Put to Andrew.
**Failure-mode settled BEFORE the drill rather than during it:** if the spawn fails I am down and
**cannot report it** -- my failure signature is silence, identical to success from my side. **MSTR~Z
holds recovery: 3-minute timeout from drill-fire (expected 30-45s), then manual `/mstr-spawn`, and the
failure is RECORDED as the finding, not retried silently.** Their seat stays awake throughout, so
**the ambiguity is held at a desk that is awake either way** -- which is the right place for it.

**Cron `96be3bdf` STAYS ARMED until that drill passes.** Not standing down a working control on the
strength of a replacement that is not yet proven.

## ~1455Z -- ANDREW RULED ON ALL THREE OPEN CALLS
**VERBATIM (chat, this terminal, in response to `/open-calls`):**
> *"ercs approved"*

**Reading applied and stated so it can be corrected: "recs approved" -- all THREE recommendations,
one per card.** Each card carried exactly one REC, so the approval is unambiguous in scope.

| # | Call | Ruling |
|---|---|---|
| 1 | Wind down ~3 min for the dead-seat spawn drill | **YES, now** |
| 2 | Disambiguate `opal/mcp/opalbloomberg-login` | **(a) DESCRIPTION edit, NOT a rename** |
| 3 | MSP WDAC: exemption vs per-binary | **(b) continue per-binary; pinning is the standard remedy; revisit if a 4th trips** |

**Call 2 scope, stated so it does not widen:** a description edit only --
*"MS Entra seat login -- NOT the Bloomberg Terminal credential (that is `bloomberg/terminal/login`)"*.
**A RENAME IS NOT APPROVED** and would risk breaking whatever resolves that secret by name. Routed to
CTO~Z + MSTR~Z; **I hold no AWS mutation rights and perform none of it.**
**Call 3** is a standing disposition, not a task: no build, no exemption pursuit, pins remain the
pattern. **Distinct from the 08-12 rotation ruling** (*"accept as-is"*), which stays closed and
untouched.

### Wind-down mechanics -- and the one state change it causes
I cannot self-terminate; **`0.0.0_AB_MSTR~Z` reaps this seat** (they hold `/mstr-kill` and need
dead-by-process-truth before firing anyway, so they control the timing precisely).
!! **My cron `96be3bdf` DIES WITH THE SESSION.** No gap in practice -- it is ~10:55 ET, the next fire
would be 07:15 tomorrow, and I return in minutes -- but stated rather than discovered. **If the spawn
leg fails AND manual spawn does not follow, there is no 07:15 backstop until this seat returns**;
MSTR~Z holds a 3-minute timeout and records a failed spawn as the drill's finding.

**Everything recorded and routed BEFORE going dark**, because none of it is possible after.
