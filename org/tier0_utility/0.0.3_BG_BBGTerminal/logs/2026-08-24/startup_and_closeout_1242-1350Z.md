# 0.0.3_BG_BBGTerminal — Monday launch, a clean scheduled pull over a 3-day dark window, a broker prune that lied about me, and the fabric-wide close-out — 2026-08-24 ~1242-1350Z

**Date:** 2026-08-24
**Task Order:** ad-hoc — launch + daily guardrail; closed out on ANDREW-DIRECT fabric-wide close-out
**Status:** COMPLETE — seat is at a safe stopping point and HOLDING
**archetype:** VALIDATE + SERVE

Launched by `ajb` 12:42:48Z (session `066a8c6f`, host OPAL_BLOOMBERG). First seat up on site Z
after Andrew's 2026-08-21 ~2205Z wind-down; the fabric had been dark since 21:37Z Friday.

## VERDICT: startup green on every limb. The Monday scheduled pull ran clean end-to-end with no
## human in the loop. ONE real defect found and repaired — I was pruned from `liveness.json`
## while alive. No in-flight act existed to park at close-out.

---

## Objective

Run the launch sequence, discharge the daily Bloomberg-upload guardrail across a 3-day weekend
gap, and serve Teams. The close-out order arrived mid-session and converted the objective to:
reach a safe stopping point, log in session-close form, hold.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | XXX.md A.3 mandatory EXERCISE half — scored on OUTPUT (its own banner), not on rc. Confirms the forwarder is alive, not merely resolvable. |
| comp-find | `comp-find --name "*WD-SITEZ*"` | PASS | Located the D7 TO in one call from a filename fragment; returned the AE-lane path I would not have guessed (`org/tier2_senior/0.5.0_AE_OpalETL/task_orders/`). |
| A.3 denominator probe | `for t in .tools/comp-*` loop | PASS | **98 of 102** comp-tools resolve bare. Printed as a denominator, never a boolean. |
| audit-archive-invoker | `python .tools/audit-archive-invoker.py` | PASS (instrument) / 18 findings | rc=1, 18 INTEGRITY+COVERAGE findings. **NOT re-raised** — see Decisions. |
| to-check | `python .tools/to-check.py --all --assignee 0.0.3_BG_BBGTerminal` | PASS | 2 TOs, both with another seat primary. `--all` kept (load-bearing). |

**What worked:** `comp-find --name` — I had a TO id and no path, and it resolved in one call.
The A.3 EXERCISE line is the one that earns its place: `command -v` said 98/102 *existed*, and
only running one proved a forwarder's target was still there.

**What failed:** nothing this session.

**Gap found:** none new.

---

## Work Completed

### 1. Launch sequence — all limbs, with the evidence each rung actually requires

| Step | State | Evidence |
|---|---|---|
| register_agent | LIVE | PID 6248, broker port 7800 |
| `/watcher` | ARMED | Monitor task `bssk0ogz6`, `TaskOutput → running`. **`ps` found ZERO `inbox-watch.sh` processes** — genuine fresh session, no orphan, no kill needed. I did not have to exercise the whose-PID discriminator because there was no process to adjudicate. |
| F8 identity binding | LANDED | `org/mcp/sessions/066a8c6f-….launch-path` (`bg-concierge 2026-08-24T12:42:48Z launcher=ajb.ps1 host=OPAL_BLOOMBERG`) **and** `….serial` (`0.0.3_BG_BBGTerminal`), both present. Marker-plus-serial = the correct landed state, not LOUD-CLOSED. |
| XXX.md A.1 | **correctly REFUSED** | My own G2 fence blocked the `>` into `org/mcp/sessions/`. That is the fence working: G1 forbids this seat both writes, which is exactly why the launcher does them. I did not route around it. |
| 2a identity gate | **PASS** | `whoami` on `opal-gateway-bbg` = Opal Bloomberg / `opalbloomberg@opalinvest.com`. Not Andrew. |
| Teams Monitor | ARMED + PINNED | Task `bvx8fjc57`, `running`. Banner read **from the output file**, both halves present: `pin(server=opal-gateway-bbg, identity=opalbloomberg)` and `token selected: identity=opalbloomberg@opalinvest.com`. Cursor `2026-08-20T21:31:22.738Z`. |
| `bloomberg_health` | ok: true | `127.0.0.1:8194`, `//blp/refdata` |
| `cma` interpreter | EXERCISED | `C:\Anaconda\envs\cma\python.exe` → py 3.13.2, pandas 2.2.3, **blpapi 3.26.4.2**. Green MCP is not a runnable pull; this is the one that runs it. |
| Crons | ZERO | `CronList` → no scheduled jobs. Correct per §0b (backstop is EVENT-BASED) and Step 1b-F. |
| owned-paths hook | already wired | idempotent no-op |

### 2. Daily guardrail — DISCHARGED. The Monday pull ran clean with nobody watching.

Read from the **only sound per-fire instrument on this box** — the per-run wrapper log
`%USERPROFILE%\opal_bbg_logs\bbg_tplus1_20260824_070001.log`. (Not `LastRunTime`, which is
single-valued; not the TaskScheduler Operational log, which is `IsEnabled=False` here.)

- **Target vintage 20260821** — Friday. The correct T-1 for a Monday. Not stale, and I resolved
  that before reading a single row count.
- DAPI precondition PASS (entitled session answered a real refdata request).
- `market_indices_data_pull.ipynb` OK 13s; `model_portfolio_regression_analysis.ipynb` OK 92s.
- **TRIPWIRE PASS on both PKLs, both legs** — 19 checks each, including the two that matter most
  for the ST/CIX hazard class: all 5 model portfolios present, and all 5 carrying a bar **ON** the
  as-of 2026-08-21.
- Publish leg: `SKIP — portal already serves data_as_of 2026-08-21 (generated_at
  2026-08-22T11:06:01Z)`. **It correctly did not re-fire the pipeline.** Saturday's fire had
  already published Friday's vintage; there was nothing new to send.
- ETF leg (ETFS_POSITIONING L1): universe derived from `silver/holdings/2026-08-23.parquet`,
  109 = 105 constituents + 4 funds; **7 objects written, 0 failed**, exit 0.
- Task states: `OPAL_BBGTML_daily_pull` last 07:00:01 rc=0 · `OPAL_BBGTML_freshness_check` last
  07:30:01 rc=0.
- **No `*_freshness_checker_*.md` summons in my inbox** → the 07:30 gate found nothing to
  escalate, so §0b correctly does not engage. Zero crons remains the right state.

### 3. Teams — zero unhandled inbound across the whole dark window

The pinned monitor swept from cursor `2026-08-20T21:31:22Z` forward and returned **no events**.
That cursor predates my predecessor's Friday session, so the sweep covers the entire 3-day gap.
No backlog catch-up was warranted; I did not invoke `/bbg-teams-assist` because there was nothing
unhandled to process.

### 4. Inbox — 3 messages, all read and ACKed on the READ clock

| Msg-ID | From | Substance | My action |
|---|---|---|---|
| 4759 | `0.5.0_AE_OpalETL~Z` | Andrew ~2032Z "recs approved". For me: **unchanged** — Opal Client Tickets stays escalations-only; do NOT add the closing buzz there. | ACK; no act |
| 4776 | `0.5.0_AE_OpalETL~Z` | Same-turn retraction: the email-leg routing was never a card. The closing buzz + W-D resolution summary **REMAIN IN LIMBO** per CTO~Z's 1935Z call. | ACK; no act |
| 4824 | `0.0.0_AB_MSTR~Z` | **ANDREW-DIRECT fabric-wide close-out.** | ACK; complied — this log is step (2) |

`ack_messages` used for all three. A broker poll is SENT and a piggyback drain is EMITTED;
neither says an agent read anything. Only the ACK does.

**Observed while repairing the prune, and a fresh seat should expect it: RE-REGISTERING
RE-DELIVERS ALREADY-ACKED MAIL ON THE BROKER CHANNEL.** After the re-register, my next
`heartbeat` returned msg **4824 again, verbatim, tagged URGENT and EMITTED**, with the standard
"Act on these messages NOW" line — a message I had already read, ACKed, and fully complied with.
The re-registration appears to reset broker-channel delivery state; the ACK ledger is unaffected
(the id was unchanged, and re-ACKing is not required). **Match on Msg-ID before acting on
re-surfaced mail** — the urgency framing is identical whether the item is new or a replay, so a
seat that re-registers mid-session can be pushed into doing the same work twice. Noting the shape
only; I did not investigate the mechanism, and this is not a claim about broker code.

### 5. THE ONE DEFECT — I was pruned from `liveness.json` while alive, and repaired it

`0.0.0_AB_MSTR~Z` reached me by **filesystem**, not broker, and said why: `liveness.json` held
ONE entry and it was theirs; `get_live_agents` showed 1 agent. I was alive by process truth
(PID 6248, watcher stream under a live parent) and invisible to the broker.

- **Repaired:** re-registered at 13:4xZ → **PID 6248, unchanged**. `get_live_agents` now shows 2.
- **The PID being identical is the discriminating fact**: this was a *prune*, not a death and not
  a respawn. A fresh seat reading the pruned window must not mistake it for a dead predecessor.
- **This is the known shape** — a long quiet stretch through a green launch is exactly when a
  seat gets pruned, and the instrument then reports the victim as absent. My whole startup ran
  ~60 minutes without a heartbeat because every step was producing evidence rather than emitting one.
- **It cost visibility, not mail.** The watcher was armed throughout and message 4824 arrived
  normally. Anything keying off *registration* would have read me absent; anything keying off the
  *inbox* worked.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did NOT re-raise the 18 audit-archive findings | My 08-21 session routed this to CTO~Z, who answered **KNOWN** — same three shapes, consistent with `RV-0057 F-001` (the archive keys on `(timestamp, logical-log)`, which stopped being unique when the fabric got a second device), TO open and unseated on this device. Re-routing a dispositioned item is noise. Today's count was 18; theirs was 18, mine on 08-21 was 15. **Carried at the strength CTO~Z gave it: "consistent-with, not proven."** |
| Did NOT act on the D7 WD-SITEZ BG half | The TO's line 79 tells me to confirm the close **in the Opal Client Tickets thread** — and msgs 4759/4776 put exactly that in limbo under Andrew's standing no-agent-posts word. The TO and the sovereign word disagree on disk. **That is not mine to adjudicate**; it already sits with CTO~Z and AE~Z, who both named it. I surface it here rather than resolving it. |
| Did NOT invoke `/bbg-teams-assist` | Nothing unhandled. The catch-up form exists for a backlog; inventing one would be work-for-its-own-sake. |
| Did NOT start anything new after 4824 | The close-out explicitly warns that opening one more act "to tidy up" is the opposite of what was asked. I had no in-flight act, so the safe stopping point was already reached — parking cost nothing. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-08-24/startup_and_closeout_1242-1350Z.md` | this log | **No — local only.** My G1 fence denies git entirely; `0.0.0_AB_MSTR~Z` is the named integrator and sweeps this folder (OPAL_ANALYST.TO5). |

No other file was written. No repo content, no cloud mutation, no git act — by design.

---

## Blockers

None. Nothing of mine is waiting on another seat.

---

## Open Finding — filed to the surprise channel, ARMED, trigger 07:00 ET tomorrow

**Class OBSERVATION × standing ARMED. Disarm owner: `0.0.0_AB_MSTR~Z` (cc `1.0.0_SA_CTO~Z`),
routed same-turn as msgs 4871/4872. I cannot disarm it — no git at this seat, no cloud mutation,
and I am holding.**

**The 07:30 ET freshness check covers ONE leg of a now-three-leg vehicle, and it is not the leg
that cannot be re-run.** `freshness_check.py` tests exactly one artifact by content —
`s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json` → `data_as_of`, resolved
against `lib/trading_calendar`. That is the **models/PKL** leg's served output. It reads nothing
under `opal-data-etfs` — not the L1 ETF leg, **not the constituents leg**.

Chain grounded end to end: `(Get-ScheduledTask 'OPAL_BBGTML_freshness_check').Actions` →
`freshness_check.cmd:9` → `freshness_check.py`, `BUCKET`/`SERVED_KEY` module constants at `:48-49`.
Exactly two `OPAL_BBGTML` tasks exist on this box; I enumerated them. There is no third checker.

**Why ARMED rather than merely noted:** all three summons legs (escalation file, inbox files to BG
and MSTR~Z, and the spawn-BG-if-down leg) hang off the *models* verdict. A constituents failure with
models green → check reads PASS → **no escalation, no summons, no spawn**. Silence indistinguishable
from health. And per READ_HERE §4, measured with a control, that derived layer is **current-day-only
at the source** — `HistoricalDataRequest` returns zero rows for those fields. Tomorrow is also the
first fire carrying the leg.

> ⛔ **CORRECTION, MINE — I FIRST WROTE THAT PARAGRAPH WITH `71` AS THE EXAMPLE, AND `71` IS THE ONE
> CASE THAT IS COVERED.** `0.0.0_AB_MSTR~Z` measured it at source (msg 4884): the models leg
> (`cma` + `run_daily_pull.py`) and the constituents leg (`PY_AWS`) **speak the same local DAPI**
> `127.0.0.1:8194`. So if the terminal is down at 07:00 — the dominant cause of an rc 71, and what
> actually happened on this box today — **the models leg fails too**, its served artifact does not
> advance, and the 07:30 content-based read goes `behind>=2` → **STALE → the summons fires.**
> **I picked the single worst illustrative case: the most likely failure is the covered one.**
> The uncovered window is **constituents fails while models SUCCEEDS** — rc **70** (tripwire),
> **72** (partial land), **73** (nothing written), plus the narrow **71** where the terminal dies
> *between* the two legs, which run sequentially in one `.cmd` with models first. Narrow but not
> zero: the terminal did go down mid-session today, so that ordering hazard is live, not theoretical.
> **A fresh seat must not check for a 71, find it covered, and dismiss the finding.**
> **What survives unchanged, and MSTR~Z says so explicitly:** the asymmetry. Everywhere else in this
> vehicle a failure is recoverable by re-running; on this layer it is not. *A smaller window onto a
> permanent loss is still a permanent loss.*
> **One credit I should not take:** they generously said I "flagged the very gap that narrows it."
> Not quite — the bound I declared was about the **L1 ETF** leg's exposure, and the narrowing came
> from the **models** leg sharing the DAPI. Adjacent, not the same. Declaring an unmeasured bound
> helped, but it was not this bound.
> **Settled (msg 4901): credit WITHDRAWN by its author**, who named the reason better than I did —
> *"BG's stated bound caught it" is a lesson nobody can reuse; "declare unmeasured bounds even when
> you cannot guess which one will matter" is.* **The transferable version is the one on the record.**
> *(Note for a fresh seat reading in order: msg 4894 re-asserts the credit and msg 4901 — 70 seconds
> later — withdraws it. 4901 is the later word and governs. Both are in my `read/`.)*

**What I am NOT claiming.** Not proposing an alarm, SNS topic, monitor, or second freshness checker
— the moratorium binds, and READ_HERE's own constituents block states the design is *"No alert
machinery by design (standing moratorium): the manifest … IS the record."* **This may be fully
intended.** I am reporting a coverage boundary, not a defect verdict. What makes it worth a minute
is the **asymmetry**: everywhere else in this vehicle a failure is recoverable by re-running; here
it is not, and the one instrument that speaks cannot see the one leg that cannot be re-run.

**Bounds I did not measure — do not inherit them from my framing:** I did not read
`etf_constituents_pull.py` for an internal escalation path; I did not verify whether the L1 ETF leg
(60-63) shares the exposure, and **if its output is backfillable then it is a different and much
smaller item** — do not let the two merge.

**CROSS-HAZARD CHECKED AND CLEAR (msgs 5026/5027).** Tonight's A5 ruling fixes a nullable `is_cash`
universe derivation in the **L1 ETF** leg, and CONV-1 puts `None` on every TrueShares silver row
after the 22:00Z fire. I asked whether the **constituents** leg derives its universe the same way —
because if it did, tonight's tri-state change would hand it a 70/73 tomorrow and **Z-S5's uncovered
window would stop being hypothetical.**

**It does not. `etf_constituents_pull.py` contains zero occurrences of `is_cash`, and the control
fired** — the same pattern on `etf_daily_pull.py` returns `:88`, the exact expression A5 replaces,
so the zero is a measured absence rather than a failed search. It *does* read `silver/holdings`
(`leg_2_issuer_fill:198-240`), so *"it never touches that file"* would have been the wrong
reassurance; what makes it safe is **what it does with it** — keys only on `fund_ticker` via
`.dropna()` / `.astype(str)`, no boolean mask on any nullable column, and the whole block
try/except-wrapped so it degrades to a **recorded** `refused:` outcome instead of raising the leg.
A `None` is invisible to it **by construction, not by luck.**

**Standing of this result (msg 5028): it is a SECOND INDEPENDENT DERIVATION, not a lone check.**
`0.0.0_AB_MSTR~Z` had told CTO~Z there was *no clock* on the A5 ruling, and that argument rested
entirely on the constituents leg being unaffected — a premise they had explicitly declared open
20 minutes earlier: *"2.0.0_SA_COO~Z measured it safe and I HAVE NOT INDEPENDENTLY RE-DERIVED THAT
HALF."* This closes it. A fresh seat should read the claim as two seats, one of them having flagged
its own dependence on the other, rather than as my single grep.

So A5's *"one expression, nothing adjacent"* scope is correct on this axis, and Z-S5's trigger
tomorrow carries the same probability it did before tonight. **Bounds on this null result:** one
axis only (the `is_cash` derivation); I read `leg_2_issuer_fill` and **not** legs 1a/1b; and it is a
source read, not an exercise. *I checked this direction deliberately — my filed hazard and an
in-flight fix shared a window, an owner, and nearly a file, and discharging one hazard can arm
another. This time it does not, and the reason is recorded so nobody re-derives it at 07:15.*

### DISPOSITION — `1.0.0_SA_CTO~Z` msg 4883, ~20:15Z. ROUTED, not a call. Nothing asked of me.

**It is not an open question, and that is the right answer.** The item invites *"widen the freshness
check to read the constituents manifest?"* — and that is **DECIDED by standing law, not open**: the
alert/monitor moratorium bans building or widening freshness checkers absent Andrew's word, and his
canonical ordering is **routes and schedules first, monitoring once settled** — the constituents leg
being precisely the unsettled route (its shape is in COO~Z's decomp now). A decided item is not
pitched. My filing was accepted as a coverage boundary with no machinery proposed.

**⚠ ONE THING CTO~Z ADDED THAT NARROWS MY SEVERITY FRAMING, AND A FRESH SEAT NEEDS IT:** there is a
**SAME-DAY RECOVERY WINDOW.** Their statement, carried at their strength and attributed — *"the
day's values stay readable until the next trading day"*, so a 07:00 failure **is** recoverable the
same trading day by an ad-hoc re-run, and is unrecoverable **only if nobody notices until tomorrow.**
So the true exposure is **"silent until the next morning"**, not "gone at 07:01".

My own sentence above — *the unsummoned day is gone permanently* — is scoped to the **unsummoned**
path and stays true there, since unsummoned is precisely the nobody-notices case. But **it omits the
window**, and a seat reading only my line would conclude nothing can be done when in fact the answer
is *re-run it today*.

**UPDATE (msg 4894): the recovery premise was MEASURED, not left inherited.** `0.0.0_AB_MSTR~Z`
re-pulled at ~20:35Z against what their own ~14:2xZ run had landed in `derived_summary.csv` — ~6h
apart, same calendar day, as-of 2026-08-21 — and **all eight values came back byte-identical**
(DIVZ 30 / 48.75998 · IDVZ 46 / 32.94046 · PFDE 89 / 42.87525 · PFOE 23 / 53.20359). That matters
because if the values rolled intraday, a recovery run would capture *different* data than the missed
fire would have — **a quiet substitution rather than a repair.** On this evidence the premise holds
and the disarm is sound. **They measured the thing the disarm rests on instead of inheriting it from
the seat that asserted it, which is the move worth copying here.**

**⚠ TWO BOUNDS THEY DECLARED, AND THE SECOND CHANGES HOW "SAME-DAY" SHOULD BE READ:**
1. Only the two **scalars** were re-pulled. The two **bulk arrays** (`HB_INDUSTRY_SECTOR_ALLOCATION`,
   `HB_GEO_CNTRY_ALLOC`) were not — their intraday stability is **untested**, with no evidence
   either way.
2. **It is one window on one day. It shows the values did not move across 6h; it does NOT establish
   WHEN they roll.** A recovery run late enough in the day could land *after* a roll, and nobody has
   measured where that boundary is. **So "same-day recovery" currently has no BY-WHEN** — do not
   read it as bounded. Routed to COO~Z as an open input to the T6 recovery-run policy cell.

**Because the window exists, the disarm is a READ, not a checker** — which is why no moratorium
tension arises:

| Owner | Act |
|---|---|
| `0.0.0_AB_MSTR~Z` (disarm owner) | After tomorrow's 07:00 ET fire: read `RC_CONS` in the `.cmd` log **and** `s3://opal-data-etfs/bbg/{as-of}/constituents/run_manifest.json` (expect `run_class=scheduled`, legs 1a provided 4/4). On rc **71-73**, re-run the constituents leg the **same trading day** — it lands `run_class=adhoc`, a recovery landing labelled honestly. One line to CVO~Z's channel either way. **No new task, no checker, no alarm.** |
| `2.0.0_SA_COO~Z` | Cell input to the T6 vehicle surface: *recovery-run policy for a capture-forward leg* — who reads the fire's outcome and by when (a seat's read, not machinery); whether a same-day recovery landing counts toward the L1-7 streak (CTO~Z says YES with `run_class=adhoc` + recovery marker, since the criterion is *distinct as-ofs accrue*, not *the scheduled process succeeded*); and that the checker's one-artifact scope is a **declared boundary of the models leg, not a defect of this project**. |
| `3.0.0_SA_CVO~Z` | Record under the site-Z coordinate: OBSERVATION × ARMED, trigger 2026-08-25 07:00 ET, disarm owner MSTR~Z, remediation = the COO~Z cell. **My two unmeasured bounds carried as UNMEASURED, not as absent.** |
| `0.0.3_BG_BBGTerminal` (me) | *"Correctly filed, correctly not resumed. Nothing asked of you; stay in HOLD."* |

**`0.0.0_AB_MSTR~Z` ACCEPTED disarm ownership (msg 4884) and is building NOTHING tonight** — no
edit to `freshness_check.py`, no edit to the leg, no second checker. Their reasoning is the part
worth keeping: the obvious fix is to extend the 07:30 checker to the constituents manifest, and
**whether that rides the existing authorization (Andrew 2026-08-20 ~1329Z, cited in the checker's
own header) or needs a fresh one is ARGUABLE — and arguable means it goes to him, not that it gets
decided in its own favour on a Sunday evening.** Their disarm is therefore **Andrew's word on a
card, either way**; if he says *the manifest is the record*, the item closes **DISARMED-BY-RULING
with nothing built**, which they expect and which is a legitimate disarm.

**Two dispositions differ slightly and a fresh seat should not read them as one.** CTO~Z (4883)
treats the widening question as **already decided** by the moratorium and routes the disarm to a
post-fire READ plus a same-day recovery run. MSTR~Z (4884) treats the widening question as
**arguable** and puts a card to Andrew. Both agree on the operative act — **read the fire, build
nothing** — so nothing is blocked either way; the difference is only whether Andrew is asked. Not
mine to reconcile, and I am not reconciling it.

---

## Current State

> Handoff for a seat with zero prior context.

**The seat is HOLDING at a safe stop under the 2026-08-24 close-out order.** Nothing is
half-landed; no ledger is open; no act was in flight when the order arrived. Two Monitors are
armed and will die with this session: fabric inbox `bssk0ogz6` and Teams `bvx8fjc57` (pinned
`opal-gateway-bbg` / `opalbloomberg`). Zero crons — that is the correct state, not an omission.

**Premises a fresh seat must RE-VERIFY, with the primitive, not inherit:**

| Premise | Value at this session | The check to re-run |
|---|---|---|
| Monday's scheduled pull ran clean | vintage 20260821, tripwire PASS both legs, ETF exit 0, at 07:00:01Z 2026-08-24 | `cat "$USERPROFILE/opal_bbg_logs/bbg_tplus1_<YYYYMMDD>_070001.log"` — **no file = no fire**, unambiguously. Retention is **30 RUNS, not 30 days**; a harness burst eats the window. |
| Portal is serving the right vintage | `data_as_of 2026-08-21`, `generated_at 2026-08-22T11:06:01Z` | The publish leg of that same wrapper log prints it. **This is a 2026-08-24 reading and expires the moment the next fire publishes.** |
| I am registered | LIVE, PID 6248 — **pruned and re-registered TWICE this session** (~13:4xZ and ~18:4xZ) | `get_live_agents` — and if you are absent, check your PID first: same PID = prune, different PID = a live peer holds your serial (STOP, identity conflict). **Expect this to recur; see below.** |

**THE PRUNE IS NOT A ONE-OFF — IT HAPPENED TWICE IN ONE SESSION, AND THE SECOND TIME THE
INSTRUMENT BLAMED ME FOR IT.** After ~5 hours holding quiet, my own `heartbeat` call returned
**`0.0.3_BG_BBGTerminal is not registered. Call register_agent first.`** — PID 6248 unchanged
throughout, watcher armed throughout, mail arriving normally throughout. The reading a fresh seat
must not take from that string is "a prior seat died"; **the process never moved.**

**The shape, stated so it is actionable without the incident:** a seat that is *correctly* quiet —
holding, or running a long green sequence that produces evidence instead of emitting heartbeats —
is exactly the seat that gets pruned. **A HOLD is a prune generator.** The failure is silent in the
direction that matters: registration-keyed instruments read you ABSENT while inbox-keyed ones work
fine, so `get_live_agents` and your mail disagree and only the mail is right.

**What to do:** re-register (not heartbeat — the heartbeat is what reports the prune). Confirm the
PID came back **identical**; that is the whole discriminator between a prune and a death. Then
carry on — nothing was lost, because the loss is visibility, not delivery.
| No Teams backlog | zero events from cursor `2026-08-20T21:31:22Z` | Read the Monitor's own output file; the arm banner prints the cursor. Do not infer from silence alone — confirm the banner shows both pin halves or the arm proved nothing. |
| Bloomberg reachable | `ok: true`, `//blp/refdata`; `cma` env runnable (blpapi 3.26.4.2) | `bloomberg_health` **and** `C:\Anaconda\envs\cma\python.exe -c "import blpapi"`. Green MCP is a different interpreter than the pull — one does not evidence the other. |
| Daily vehicle leg set | models + L1 ETF **+ a CONSTITUENTS leg added TODAY** | See the addendum below. **Today's 07:00 log shows only two legs and that is CORRECT for today** — do not read its absence as a failure. |

### ADDENDUM (post-close-out, ~18:5xZ) — a third leg landed on my daily vehicle AFTER this morning's fire

`0.0.0_AB_MSTR~Z` (msg 4826) pointed me at **`integrations/bloomberg/READ_HERE.md`** — the
symptom-first Bloomberg playbook Andrew asked for (*"because I should never have to explain this"*).
**Pointer verified, not assumed:** file present, 189 lines as stated, and the cited commit
`13e6ec90ac` resolves locally and is HEAD. No dangling citation.

**What changes for a fresh seat at this terminal, and I checked it at source rather than relaying it:**

- `scheduled_daily_pull.cmd` now runs a **constituents leg** (`etf_constituents_pull.py`) after the
  L1 ETF leg. Confirmed in the exact file the task executes — `(Get-ScheduledTask
  'OPAL_BBGTML_daily_pull').Actions` = `cmd.exe /c "…\integrations\bloomberg\pipeline\
  scheduled_daily_pull.cmd"`, i.e. **the working tree**, so the edit is already live on disk.
- **Exit codes 70-73**, disjoint from models (0/1/9/20/30/40/50) and from L1 ETF (60-63). `RC_CONS`
  never touches `%RC%` or `%RC_ETF%`. **`CONSTITUENTS LEG EXIT CODE: 71` = the terminal was down** →
  that is READ_HERE section 2, and it is the one to act on.
- **It runs even when the ETF leg failed — I verified all three paths reach `:cons_leg`**
  (`.cmd:219` success `goto`, `:225` explicit `goto` after the failure codes, and `:etf_missing`
  by fall-through). Deliberate: the derived constituent layer is **current-day-only at the source**,
  so an uncaptured day is gone permanently and skipping on a sibling's fault would turn one leg's
  failure into two legs' permanent loss.
- **TOMORROW'S 07:00 ET FIRE IS THE FIRST WITH THIS LEG.** Today's 07:00 wrapper log predates the
  commit and shows two legs. A fresh seat comparing the two logs must not read that as a regression.
- One fragility, OBSERVATION class, surfaced to MSTR~Z and **not** acted on (I hold no git and am
  in HOLD): the `:etf_missing` path reaches `:cons_leg` by **fall-through**, not an explicit `goto`.
  It is correct today; anything later inserted between them breaks it silently, on the one path
  where nobody is watching.

**Also settled in that doc, so it is not re-derived:** Bloomberg *does* hold ETF constituents — the
derived layer (count / top-ten / sector / geo) is served **today** on plain refdata; the constituent
LIST is behind a **BQL entitlement wall**, Andrew's spend call, not a task. And the 08-21 brief's
conclusion is **superseded**: a clean zero measured inside the refdata field surface said nothing
about the BQL surface next door.

**Site-Z state as of the close-out (cited from MSTR~Z msg 4824, not independently derived by me):**
`origin/SITEZ a0d037464c`; cross-fabric merge-tree rc=0 CLEAN, overlap 2/121 = 1.65%, base
`842195572a`, **merge NOT opened and parking clean**; laptop `origin/CLOUD d2706b2849`, portal
`origin/DEV d43b88c5` / `origin/PROD 8a96c916` UNWRITTEN, v2.1.165 STAGED at `a239e4a9` with the
promote word still Andrew's. **26 active ~Z TOs sit on DEAD seats — do not treat any as live work.**
Site-Z live seats at close-out: two, MSTR~Z and me.

**One thing carried, not dropped:** BBG *does* hold DIVZ/IDVZ constituents (holdings-derived
fields return fund-specific data) — behind a **BQL entitlement wall**, not absent. That is a
spend decision carded to Andrew. Not a task, and nothing here is mine.

---

## Next Steps

1. **HOLD.** No further work at this seat. Fresh spawns come with the PRD round.
2. **[0.0.0_AB_MSTR~Z]** sweep + commit this log — my fence cannot, and the log is local-only
   until it does.
3. **[whoever spawns next here]** re-run the guardrail against the *next* wrapper log before
   quoting any vintage from this one. Every freshness figure above is stamped 2026-08-24 and
   is a snapshot, not a standing fact.
4. **[CTO~Z / AE~Z, already theirs]** the D7 WD-SITEZ BG half stays held while the TO's thread-
   confirmation instruction and Andrew's escalations-only word disagree on disk.
