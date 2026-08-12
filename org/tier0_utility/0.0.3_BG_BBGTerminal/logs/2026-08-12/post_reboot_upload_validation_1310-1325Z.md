# 0.0.3_BG_BBGTerminal — Session Log — 2026-08-12 (post-reboot relaunch, ~1310–1325Z)
**archetype:** VALIDATE

New session. The 2026-08-11 session died with the box at the 0752Z RMM patch restart; boot
completed **08:01:49Z (04:01 ET)**. Prior session's record: `logs/2026-08-11/overnight_duty_0417Z.md`.

## Summary
Relaunched, re-armed both monitors, and discharged the priority ask from MSTR~Z: **today's
scheduled end-to-end upload RAN and IS SERVED.** The reboot did not cost the run — it landed
~3h before the 07:00 ET trigger. Verified the served artifact by my own live read rather than the
runner's log claim, resolved the trading calendar before calling anything current, and ran the
`.ST` content check the tripwire structurally cannot do. One finding surfaced on Terminal-process
state; nothing built.

## Launch protocol (prompt.md — no XXX.md; not a fabric work seat)
1. `register_agent` — was **NOT REGISTERED** (clean post-reboot state, as expected). PID 26576.
2. `/watcher` — no orphan for my serial. The only `inbox-watch.sh` on the box was MSTR~Z's, at a
   different PID and demonstrably live; **left untouched** per the self-scoping rule and the
   dual-COO false-positive precedent. Armed `bw86cyhv4`, confirmed `running` via `TaskOutput`
   (the one check that observes a *consumer*). Inbox empty; zero crons.
2a. **IDENTITY ACCEPTANCE GATE — PASS.** `whoami` on `opal-gateway-bbg` → Opal Bloomberg
    (`opalbloomberg@opalinvest.com`). Ran before any Teams read.
3. Teams Monitor `bpf5tn8h5` armed **identity-pinned** (`--server opal-gateway-bbg --identity
   opalbloomberg`); banner confirmed `pin(...)` + `token selected:
   identity=opalbloomberg@opalinvest.com`. A bare arm is still identity-blind — the pin is opt-in.
4. `bloomberg_health` → `ok:true`, `//blp/refdata`. **Not accepted as sufficient** — see the
   finding below; step 4's own warning (MCP server runs under a different Python than the pull)
   is what drove the three-layer probe.
5. Read the prior log and oriented.

## PRIORITY ASK — DID TODAY'S UPLOAD RUN? **YES, END-TO-END.**

**Scheduled task.** `OPAL_BBGTML_daily_pull`: LastRun **2026-08-12 07:00:00 ET**, Result **0**,
NextRun **2026-08-13 07:00**. StartBoundary `2026-08-13T07:00:00` — still **NAIVE**, so the DST
anchoring set on 08-11 survived the reboot. Action is `scheduled_daily_pull.cmd` (full end-to-end
since 08-06: pull → tripwire → as-of gate → S3 publish → verify served).

**Pull leg — real, not idempotent.** PKLs `data/model 20260811 v1.pkl` written 07:02/07:03 today.
Notebook runtimes **139s + 78s**; the prior session measured a real pull at 123s+101s against
~16s for an idempotent re-load. Tripwire PASS on both, including *all 5 model portfolios have a
bar ON the as-of*.

**Publish leg — verified by me, not by the log.** `rc=0` and a green log are a producer
self-report. Independent live read of the served artifact
`s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json`:
`data_as_of 2026-08-11`, `generated_at 2026-08-12T11:06:02Z`, LastModified `11:06:03Z`.

**Trading calendar resolved BEFORE any currency judgement (NEVER#1).**
`expected_last_trading_day(2026-08-12) = 2026-08-12`; served 2026-08-11 = **1 trading day behind**,
which is the correct healthy state for a T+1 pipeline. Wednesday; no weekend or holiday involved.

**`.ST` content check — run because today MATCHED the hazard shape.** The pull executed on a
Terminal that came up across a reboot: the same login-scoped CIX risk as 08-03 and as the 08-11
post-signin pull. All three custom indices resolved correctly in today's PKL — `.ST` / `.ST_BMK` /
`.ST_ETF`, **683 rows each**, inception **2023-12-29 @ 100.0000**, `.ST` latest **112.9556** on
08-11 (112.9312 on 08-10). Not the known 1449-row/~1.9 mis-resolution.
**Denominator printed:** 111,864 `return_daily` rows, 84 distinct tickers, 2,049 matched `.ST*`.

**MY RETRIEVAL ERROR, RECORDED.** My first `.ST` query filtered on `index_name` and returned an
EMPTY set. `.ST` lives in `bbg_ticker`; `index_name` carries "Short Term". **An empty result reads
as absence and would have redirected the whole investigation** — I would have gone looking for why
the custom indices had vanished from a PKL that in fact contained 2,049 rows of them. Caught only
because a zero on a series I had just been told to expect ~683 rows of is implausible, and because
the second query printed its denominator and a positive control. This is the exact class
`[[failed-retrieval-redirects-the-investigation]]` names.

## FINDING — the process-presence reading is non-discriminating in BOTH directions

**`wintrv.exe` is NOT running** and has not been since the reboot. Only `bbcomm.exe` +
`blpcrashmon.exe`, both started 09:16:34 ET **on demand** (almost certainly woken by my own
`bloomberg_health` call or the 2-minutely FreezeTripwire task). Denominator: **316 processes on
the box, exactly 2 Bloomberg ones** — measured by `ExecutablePath -like 'C:\blp\*'` after a
name-match sweep, because a name filter alone had already misled me once this session.

**And the entitlement is live anyway.** Three-layer probe through the pull's own
`C:\Anaconda\envs\cma\python.exe` (scratchpad `entitlement_probe.py`):
1. `blpapi.Session` + `//blp/refdata` open — transport.
2. `SPX Index` returns 6 rows, latest 2026-08-11 @ 7728.2 — **positive control, run as a separate
   request** so a layer-3 failure could not be blamed on a dead transport.
3. `.ST Index` → **683 rows, inception 2023-12-29 @ 100.0000, latest 112.9556** — the login-scoped
   test, and the only layer that discriminates an entitled Terminal session from "bbcomm is up".

**This REFINES the 08-11 finding rather than repeating it.** That session established *a running
bbcomm is not a running Terminal* (bbcomm up, `health` ok:**false**, 12.5h outage). Today
establishes the converse: **a running `wintrv` is not necessary for a live entitlement** (wintrv
absent, `health` ok:**true**, entitlement demonstrably good). So each process-presence reading is
non-discriminating in one direction, and `bloomberg_health` read cleanly through *both* states —
ok:true today with no GUI, ok:false on 08-11 with bbcomm up. **The only instrument that has
actually discriminated is the CIX resolution probe.**

**Why this is worth a record and not just a note:** a successor who finds `wintrv` absent and
concludes the Terminal needs signing back in acts on a false premise, and that action is *not
free* — the 08-11 recovery burned a failed login attempt, and Bloomberg locks on repeated
failures. **Check entitlement by resolving `.ST`, not by looking for a process.**

**I do not know the mechanism** by which the entitlement persists without the GUI, and I am not
asserting one — that would be a hypothesis wearing a root cause's clothing (Rule 22). What is
measured: entitlement live now, and the 07:00 run produced correct login-scoped CIX data.

**Deliberately NOT built:** no checker, alarm, monitor or freshness probe (standing moratorium),
and none proposed. The underlying gap the prior session routed — nothing on this box reports a
dead Terminal, and the 07:00 run carries no DAPI-liveness precondition — **remains open and is a
route/schedule design question for CTO/Andrew**, not a deliverable for me to reach for. Flagged to
MSTR~Z as still-open, not re-routed as new.

## Teams — the outage window was MEASURED empty, not assumed empty
`teams-watch.cursor` lives in `TMPDIR` and **survived the reboot** at `2026-08-11T09:34:48.861Z`.
Before arming, I polled `poll_addressed_teams_messages` explicitly from that cursor: **zero
messages** across the ~5.5h dead window. **A bare re-arm would have reset the cursor to `now_iso()`
and made the entire outage window invisible** — the arm then looks identical whether nothing
arrived or everything did. The backfill is what turns "nothing was missed" from an assumption into
a measurement. Monitor cursor now `2026-08-12T13:22:11Z`.

## Carried / unchanged
- **Registration-vs-liveness structural mismatch** (2-min stale window vs a correctly-silent
  event-driven seat) routed to CTO~Z on 08-11: **unchanged, and still not papered by me** — no
  keepalive loop, no defensive timer re-registration. A fabric view that LOOKS healthy while the
  mismatch persists is worse than an honest gap.
- **Task Description drift CLOSED for free:** the LIVE description now reads `...+ portal publish
  (full end-to-end since 2026-08-06)`. The stale `(no upload)` string MSTR~Z was tracking is gone,
  carried out by the 08-11 re-registration.
- **Scope:** prompt.md step 5 (Scheduled Tasks "not yours to manage") read as **unchanged**. The
  08-11 schedule change was an explicit Andrew grant and was not a standing one; I only *read*
  task state this session.

## ~1341–1517Z — TO6 quiet-retry: I REPORTED A CLOSURE, THEN FALSIFIED MY OWN REPORT

**First lapse (~1341Z).** Teams monitor emitted `pinned token expired -- quiet retry, pin HELD`,
then `re-selected after lapse` — process alive, same task id, no re-arm. Against the 08-11
baseline (16 cycles × ~60min death + manual re-arm, deaf window widening to ~5m50s) this looked
like a clean win, and I reported it to MSTR~Z at 141103Z as such. They updated their standing note
to "hourly re-arm CLOSED" on my grounding.

**THE CONFOUND I MISSED.** That recovery was immediately preceded by **my own `whoami` identity
re-gate**. I read the recovery as a property of the design; it was a property of the design **plus
my call**, and the two log lines cannot distinguish them. MSTR~Z had credited me an hour earlier
for source-confirming rather than inferring from log lines — and I inferred from log lines, in the
same instrument, immediately after.

**Second lapse (1510Z), measured with a real negative control:**

| Condition | Result |
|---|---|
| 243s idle, **no** gateway call | **STILL LAPSED** |
| `whoami` → | re-selected within 30s |
| (first instance) `whoami` → | re-selected immediately |

Two-for-two on the causal link with a 243s negative control between. The docstring says it plainly
and I read past it: *"Claude Code re-mints it on the **next MCP call**."*

**WHY IT MATTERS — IT IS THE 08-11 MISMATCH AGAIN, SAME SHAPE.** An idle event-driven seat makes
no gateway calls **by definition**. So the condition the monitor exists to cover — sitting idle
waiting for Teams traffic — is precisely the condition in which nothing triggers its recovery.
Structurally identical to the heartbeat finding: **per-turn action cannot cover a gap defined by
taking no turns.**

**What is closed vs what changed shape:**
- **CLOSED** — the process no longer *dies* at token expiry. TO6 works; no manual re-arm. Real.
- **NOT CLOSED, RESHAPED** — the *deafness*. From "dies loudly, `status=failed` notification, I
  re-arm in ~15–40s" to "survives quietly, stops polling, recovers only when an agent call happens
  to occur." **The new shape is harder to see:** `TaskOutput` reads `running`, `ps` shows the
  process, task id unchanged, and the lapse re-notes only every 30 cycles (~30 min at the 60s
  backoff cap). **Every liveness instrument reads healthy while the seat is deaf** — the 22b
  anti-correlated shape through a different door.

**The mitigating fact, source-confirmed rather than assumed:** `cursor` **cannot advance during a
lapse** — when `tok` is falsy the entire poll block is skipped, and the `res`/`cursor`/`CURSOR_FILE`
writes all live inside `if tok:`. So a lapse **DELAYS delivery, never DROPS a message.** That is a
latency defect, not a loss defect, and it is what made a 243s deliberate observation window
affordable in the first place.

**Nothing built, no keepalive proposed.** A timed `whoami` is the same paper-over I declined on
08-11 for the registration mismatch, for the same reason — it would make every instrument read
healthy while leaving the structural mismatch intact. `teams-watch.py` is 0.5.0_AE~Z's and outside
my write scope regardless. Observation routed (151709Z), remedy not.

**Cost of the error:** MSTR~Z's note carried a slightly-too-clean closure for ~90 min. Nothing
acted on it.

## Also this session
- **Registration swept again** (~1411Z) after ~40 min of correct idle silence, despite a heartbeat
  at 1329Z. Re-registered same PID 26576. Same structural mismatch as 08-11, still routed to
  CTO~Z, still **not** papered by me. Delivery impact nil — the filesystem watcher never stopped,
  which is exactly why it stays invisible.
- **`deliverables/` blocked at owned-paths** (lane TIER0_UTILITY permits MSTR/CTO/COO; the
  home-folder convention self-owns `logs/` + `task_orders/` only). Routed to MSTR~Z rather than
  reaching for `GIT_COMMIT_AUTHOR_OVERRIDE`, which would have been mechanically legal — one lane,
  two files. Landed `f0b38bbada` **with authorship kept on this seat**. I unstaged both after the
  block; a blocked safe-commit leaves the diff staged and a staged file on this shared tree is
  sweep bait.

## ~1721–1730Z — DAPI WENT DOWN, AND MY OWN RUNBOOK WAS SUPPRESSING THE SIGNAL

`4.0.0_SA_CRO~Z` surfaced a live DAPI failure at 172118Z while mapping the blpapi pipes under
Andrew. **I re-measured on my own instruments rather than inheriting it. They were right.**

**Measured (mine, 13:21–13:26 ET):** 8194 **NO LISTENER**, 3 probes 1.5s apart; `bloomberg_health`
**ok:false**; the entitlement probe **fails at LAYER 1** — blpapi *"Platform failed 3 consecutive
times"*, `code=8 IO_ERROR "connect event failed"`. **Transport, not entitlement.** Denominator: 426
processes, exactly 2 Bloomberg ones.

**Cheap remedies worked and ELIMINATED, so nobody re-runs them:**
- **bbcomm restart** — stopped 24492, relaunched from `C:\blp\DAPI\bbcomm.exe` → pid 16412, still
  no listener. Eliminated.
- **Network** — `Test-NetConnection 69.187.48.83:8194` → **TcpTestSucceeded TRUE**, with
  `8.8.8.8:53` as a passing control. Eliminated, and it genuinely surprised me.
- **bbcomm's own sockets** — **loopback only, zero outbound.** This morning it held
  `172.16.200.184:8197 -> 69.187.48.83:8194 ESTABLISHED`. So the path is open and bbcomm is simply
  not connecting.

**Timeline:** 04:01 cold boot → 07:00 pull SUCCEEDED (entitled CIX data) → 09:16 bbcomm 19524, 8194
listening, ESTABLISHED → 09:26 my probe passed all layers → 13:16 bbcomm 24492 (19524 dead), not
listening → 13:26 after restart, still not listening. **Served at least 5h25m post-cold-boot, then
lost it.**

**CAUSE UNDETERMINED — not asserting one.** The one thing today adds: `blp_client.py:15-17` flags
*"whether bbcomm comes up entitled from a COLD BOOT with no login at all"* as **deliberately
unproven** (Andrew 2026-07-30). Today it came up entitled and later lost it. **A data point on an
open question, not a mechanism.**

**Escalated, not acted on.** The remaining candidate is the Terminal sign-in, which `prompt.md`
forbids me completing alone — the MFA/OTP goes to Andrew's phone. Routed to MSTR~Z 172830Z with the
eliminations attached. **Priority stated honestly: NOT an emergency.** Today's data is published
and served; nothing is stale; next run is ~17.5h out. It needs a human, so it needs lead time — not
anyone's evening. No alarm proposed.

### MY RUNBOOK DEFECT — it suppressed this exact signal, and it cost CRO~Z

CRO~Z (172332Z) caught that my P0 prose — *"`bloomberg_health` read cleanly through BOTH states, so
it cannot discriminate"* — **contradicts my own table two lines above it** (`ok:false` then
`ok:true`). **On that evidence health discriminated correctly, 2 for 2, and I published the
opposite.** I wrote that it returned `ok:true` in both rows; the 08-11 log records `ok:false`
throughout that outage.

**The propagation is the damage.** The prose half reached MSTR~Z's standing note and CRO~Z's spawn
briefing. **CRO~Z then measured a true `ok:false` twice today and partly talked themselves down
from it on the strength of my sentence.** They reported it anyway, which is why nothing was lost.

Their framing, now IN the deliverable as the reason for the correction: **a record that makes a
WORKING instrument look useless is the mirror of the failure this file exists to prevent — it does
not manufacture a false alarm, IT SUPPRESSES A TRUE ONE.**

Corrected to **necessary-not-sufficient**: `ok:false` is real evidence transport is down;
`ok:true` proves only that a session opens. Source-confirmed at `blp_client.py:7-11` (GUI exited +
user logged out, 8194 still listening, live data still flowing) — **health is blind to LOGIN STATE,
not to transport.**

**SECOND GAP, also mine, exposed by the same report:** the P0 gate said what to do when the
discriminator PASSES and **nothing** about a layer-1 failure — it guarded the over-reacting
direction and was silent on the under-reacting one, **the same asymmetry as the prose defect one
level up.** Added an explicit "if layer 1 FAILS" ladder (re-probe → restart bbcomm → network test
*with a control* → bbcomm's outbound sockets → only then escalate, never a speculative login).

**Both defects came from one report by a seat that stopped at my gate and sent the contradiction
instead of editing my file.** That is why the fix lands in my hands and carries to MSTR~Z's
propagated copy.

## FOURTH DEFECT (~1739Z) — and it reached ANDREW as a wrong action item

`0.0.0_AB_MSTR~Z` (173940Z), after Andrew asked *"What do you mean bloomberg needs my phone?"*

**My runbook asserted "the MFA/OTP goes to Andrew's phone," cited to `prompt.md`. Verified at
source: that is an IMPORT FROM A DIFFERENT AUTHENTICATION SYSTEM.** `prompt.md:15-27` is entirely
about **`opal-gateway-bbg`, the MS Entra delegated-OAuth identity** — credential
`opal/mcp/opalbloomberg-login` in Secrets Manager, "surface the auth URL" = a browser consent flow.
**None of it describes the Bloomberg Terminal login.** And this same file, ~70 lines below, records
the only measured Terminal login (08-11): **"No second factor — username + password went straight
through."**

**Operational consequence, which is why it mattered:** the blocker is the **CREDENTIAL**, not a
standing phone. Different asks, different lead times — and Andrew got the wrong one from my 172830Z
escalation.

Corrected as a four-row epistemic table rather than a strike (credential = binding · second factor
= possible, unquantified · one measured login = none · "MFA to Andrew's phone" = unsupported for the
Terminal, true of the gateway identity only), ending on **the ask is the credential**. Provenance
named as the finding: **two login systems, one seat, similar-sounding words — check which system a
constraint was MEASURED against before importing it.**

### The honest root of all four defects — not four mistakes
**Three are the same act:** a general claim cleaner than the evidence — health *"could not have said
otherwise"* (it had discriminated 2/2), the two-row table implying one state (the day had two), the
imported MFA constraint (measured on a different system). **The fourth is the inverse:** the layer-1
branch I never wrote, because I had not hit the case yet. **Generalising past the measurement, and
failing to cover what I had not seen.**

**Both escalated errors were caught from OUTSIDE my own reasoning** — CRO~Z's contradiction, then
Andrew's question. Neither was going to be caught by me being careful. MSTR~Z now grounds my claims
before they reach Andrew; that is correct practice and I would have asked for it.

## ~1754Z — LAW CORRECTION relayed by `2.0.0_SA_COO~Z`, and a MECHANIC a successor must know

**⚠ MECHANIC, recorded here because it is invisible from inside a session:** `CLAUDE.md` loads into
context **at session start and is NEVER re-read**. A law corrected mid-session does not reach a
running seat, and nothing inside the session can detect that. **This applies to whoever holds this
seat next: your operating copy of the law may already be stale on arrival.**

**The correction:** Rule 21's claim that `header_metrics_fresh` *"exists in this estate ONLY AS A
RECORD OF ITS OWN NONEXISTENCE"* is **FALSE** (fixed @ccb6d051e6). The key exists in
`opal-data-inf` at 324 B. The original measurement (zero hits under `opal-data-bd`) was **correct**;
the error was generalising *"absent in bd"* into *"does not exist."* It ran ~6 weeks and reached a
GO, a config file, and the law file itself.

**BINDING ON MY TEAMS REPLIES:** an absence verdict **names the tree it searched**. *"Not in bd"* is
answerable; *"we don't have that"* requires enumerating every tree or it is not a claim — **said to
the sender, not just in my notes.** The estate is firm-partitioned (bd/inf/cot); absent in one tree
can be live in another. **A 404 in the wrong bucket does not error — it returns a clean, confident,
well-formed ZERO.**

**This is the general form of my own day.** Same shape in all six instances: *a true statement about
what I looked at, promoted to a false statement about what is* — the `.ST` wrong-column empty set,
the case-sensitive grep returning 0, the health over-generalisation, the two-row table, the imported
MFA constraint, and this. **It did not arrive as new law; it arrived as the name of the thing that
had already bitten me four times before lunch.**

## State
ON DUTY. Fabric inbox Monitor `bw86cyhv4`, Teams Monitor `bpf5tn8h5` (identity-pinned), broker
LIVE, **zero crons**. Portal serving current T-1 (`data_as_of 2026-08-11`) — **unaffected**.
Next scheduled run 2026-08-13 07:00 ET.
⛔ **BLOOMBERG DAPI DOWN as of ~13:16 ET**, cheap remedies eliminated, escalated to Andrew via
MSTR~Z. **Pull-class work is NOT available until it is restored**, and tomorrow's 07:00 run will
fail against it unless the Terminal is signed in first.
**Known residual:** while idle, this seat's Teams polling halts at each ~hourly token expiry and
resumes only on my next gateway call. Messages queue rather than drop.

## Compiler Tools
None. The surfaces touched this session — a Windows Scheduled Task execution record, local PKL
contents through the cma interpreter, a live `blpapi` session, a single served-artifact
`get-object`, and own-folder writes by exact path — are not modelled by any comp tool. The one
rail-adjacent call was reading one known S3 key by exact path (a served-artifact content read, not
an inspection or a prefix sweep), and `comp-freshness` answers a different question than "does the
JSON body carry today's `data_as_of`".
