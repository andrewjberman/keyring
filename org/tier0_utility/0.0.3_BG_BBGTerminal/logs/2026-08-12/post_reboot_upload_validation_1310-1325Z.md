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

## State
ON DUTY. Fabric inbox Monitor `bw86cyhv4`, Teams Monitor `bpf5tn8h5` (identity-pinned), broker
LIVE, **zero crons**. Bloomberg DAPI up and entitlement exercised. Portal serving current T-1
(`data_as_of 2026-08-11`). Next scheduled run 2026-08-13 07:00 ET.

## Compiler Tools
None. The surfaces touched this session — a Windows Scheduled Task execution record, local PKL
contents through the cma interpreter, a live `blpapi` session, a single served-artifact
`get-object`, and own-folder writes by exact path — are not modelled by any comp tool. The one
rail-adjacent call was reading one known S3 key by exact path (a served-artifact content read, not
an inspection or a prefix sweep), and `comp-freshness` answers a different question than "does the
JSON body carry today's `data_as_of`".
