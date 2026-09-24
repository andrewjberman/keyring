# 0.0.3_BG_BBGTerminal — POST-REBOOT STARTUP + first serve, 2026-09-11T14:18–14:30Z

**archetype:** MIXED (VALIDATE + COORDINATE)

Session `fe53cc1b-90f6-4b68-8882-cd62ac62f12d` · PID 2204 · site Z, the Bloomberg box.
Successor to `prereboot_state_1340Z.md`, which is what made this startup cheap — every hazard it
named was checked as named, and every one of its predictions held.

---

## 1. Reachability — both Monitors armed, both confirmed by a CONSUMER probe

| | state |
|---|---|
| Broker | was NOT REGISTERED (reboot dropped it) -> re-registered, PID 2204 |
| Inbox Monitor | task `bdk4b8mgn`, banner `parent-tied: pid 1441`, `TaskOutput -> running` |
| Teams Monitor | task `b66wr6oft`, pinned `server=opal-gateway-bbg identity=opalbloomberg` |
| Identity gate (step 2a) | **PASS** — `whoami` = Opal Bloomberg / `opalbloomberg@opalinvest.com` |
| Crons | zero, per the launch rule (`CronList`: no jobs) |

**THE CURSOR CHECK THE PREDECESSOR DEMANDED — CLEAN.** Arm banner read BEFORE serving anything:
`[teams-watch] armed interval=10s cursor=2026-09-11T12:37:32.566Z (incoming-only)`.
That is byte-identical to the LIVE `C:\tmp` home recorded pre-reboot, NOT the stale
`%LOCALAPPDATA%` home (`2026-08-28T20:07:10.323Z`). **No replay hazard; the fourteen-day
re-emit did not happen.** Both homes re-measured at 14:2xZ and still hold those two values.

**Delivery ledger (B.0), since 12:00Z:** 5 of 5 rows READ, all by this serial, all pre-reboot.
Nothing unread, nothing owed to any fabric seat. `to-check --all --assignee` = **0 active TOs**
(scanned 2532). No task orders in this seat's folder.

---

## 2. SERVED — Manav Shah, first contact (full record in `threads/2026-09-11-manav-shah/2026-09-11.md`)

Attachment-only message at 13:20:16.751Z (arrived while this seat was dark), follow-up `?` at
14:25:01.746Z. ACKed 14:24:32.100Z (history-neutral), served 14:25:36.905Z + 14:25:41.415Z in two
blocks under the 2–3 sentence cap. **Recall denominator: 2 of 2 resolved dirs read, 0 hits;
`INDEX.md` did not carry the chat id -> first contact, dir + INDEX row created in the same act.**

**The attachment could not be opened, and that was EXERCISED this turn, not recalled:**
`get_item(3c947710-…)` and `list_onedrive()` both -> `identity_scope_denied` (server-side tool
allowlist, OPAL_ANALYST PRD 4.3). Surfaced to `0.0.0_AB_MSTR~Z` as msg
`20260911T142655Z_…_SURFACE…` — **surfacing only; widening is an Andrew ruling and was not asked
for here.** This is the SECOND person to hit it in one day (Andrew 06:44Z, Manav 13:20Z), which is
why it earned a message: attachment-only is a MAIN inbound path on this surface, not an edge, and
the sender sees a reply rather than a missing capability. **No rate is claimed — denominator is 2,
both in DM, both today; no census of historical attachment-only inbound was run.**

---

## 3. Daily guardrail — GREEN, and the reboot broke nothing

**Both Scheduled Tasks survived** (measured via `Get-ScheduledTaskInfo`, not `schtasks`, which
returned empty here):

```
OPAL_BBGTML_daily_pull       State=Ready  StartWhenAvailable=True   LastRun 09/11 07:00:01  rc=0  Next 09/12 07:00
OPAL_BBGTML_freshness_check  State=Ready  StartWhenAvailable=False  LastRun 09/11 07:30:01  rc=0  Next 09/12 07:30
```

Today's run already published **2026-09-10** (verified by content pre-reboot at 11:30Z;
`trading_days_behind=1` = healthy T-1). ⚠ **Successor: T-1 for Monday 09-14 is Friday 09-11.**

### `bloomberg_health` -> `ok:false`, AND THE PREDECESSOR'S FRAMING NEEDED ONE CORRECTION

The pre-reboot note said a reboot "signs it OUT". Measured 14:2xZ, it is stronger than that:
`bbcomm` is running (autostarted 10:19 ET) but **`wintrv` is not running at all** and **nothing
listens on 8194** — the app did not relaunch, so this is *not-running*, not *running-and-logged-out*.

**That distinction is only worth naming because it could have made the unattended recovery
inapplicable — so it was settled rather than assumed.** It does not:

- `scheduled_daily_pull.cmd:62-123` runs the DAPI-liveness precondition + sign-in fallback
  **AGENT-INDEPENDENT — "fires with no agent alive"**, discriminating on a real `//blp/refdata`
  request rather than a port ping.
- `bbg_signin.ps1:130-132` — `if (-not (Get-Process wintrv)) { Start-Process 'C:\blp\Wintrv\wintrv.exe' }`.
  **The app-not-running case is the SAME covered path.**
- Exercised history agrees: 4 of the last 5 ledger entries are `SUBMITTED-UNATTENDED-FALLBACK`
  (09-03, 09-05, 09-07, 09-09).

**DECISION — NO sign-in attempt spent this session, and the reason is named rather than coasted:**
the ledger reads **13 entries, last `2026-09-10T19:47:28.6435476Z SUBMITTED-SUPERVISED`** (today's
07:00 spent nothing — the precondition PASSed with DAPI already up), so the same **one-of-two
budget** the predecessor recorded is still what is left; the 07:00 path provably self-heals from
the exact state the box is in; and nothing is due before then. **If a live request needs DAPI
today, sign in then** — that is the trigger, and it is the only thing that changes this call.

---

## 4. Compiler Tools

| Tool | Result | Note |
|---|---|---|
| `comp-which` (PATH exercise) | **104 of 104 resolve bare; forwarder RAN** | scored on OUTPUT, not rc, per A.3 |
| `comp-read --for` (TEAMS_DUTY, READ_HERE, bbg_fallback) | worked | UNREAD LEDGER is the useful half — it names what the answer did NOT cover |
| `comp-read --enumerate` (THREAD.md x2, SKILL.md, signin.ps1, scheduled cmd) | worked | settled the wintrv-launch question in one read |
| `to-check.py --all --assignee` | 0 active, scanned 2532 | `--all` kept, per B.1 |
| `get_delivery_state` | 5/5 READ | the only sound delivery oracle |

**GAP FOUND — stated, not chased:** `comp-read`/`comp-find` are refused by the rail hook when piped
into `head`/`grep`, including `tail -6` in a loop. Correct by design (a receiver can erase the
denominator) but it means the per-file loop idiom does not work; the fix is per-file calls with
native flags, which is what was used.

---

## 5. Startup steps NOT completed, and why (neither is chased)

1. **A.1 session-serial file** — `org/mcp/sessions/<session>.serial` could not be written: the
   `bg-concierge-gate` refuses it from this seat (G1/G2, off-allowlist), by design. **Consequence,
   stated because LD-0290 names it:** the halt gate falls back to the shared `.agent_context`,
   which currently reads `2.0.0_SA_COO~Z` — **so a `[STOP]` addressed to this serial would be
   invisible to this seat's own gate.** Identity itself is not in doubt (own armed Monitor +
   registration at PID 2204, and `liveness.json` shows no conflict). Routing the fix is
   `0.0.0_AB_MSTR~Z`'s call, not this seat's act.
2. **E `.comp-graph/.agent_context`** — same gate; also one repo-global last-writer-wins file that
   another live seat currently owns, so writing it would stomp a peer. Not written.

## 5b. ADDENDUM 14:33–14:40Z — Terminal restored, and the census found something nobody asked for

**Msg 21393 (`0.0.0_AB_MSTR~Z`) — Terminal signed back in on Andrew's word ("Also have them restart
Bloomberg"). READ-acked (id 21393).** Re-derived on a DIFFERENT instrument rather than re-running
their call: `bloomberg_health -> ok:true`, and a refdata read on **AAPL + SPX Index** (theirs was
SPY + IBM) — `APPLE INC 332.15 USD`, `S&P 500 INDEX 7666.67 USD`. Agreed; §3's `ok:false` above is
stale, not wrong.

**The window question 21393 flagged — SETTLED, nothing lost.** ⚠ **And the domain is the part that
could have been wrong, so it was widened deliberately:** rather than scoping to the two
`OPAL_BBGTML_*` tasks this seat already knew, it censused **all 204 scheduled tasks** and filtered
for `opal|bbg|bloomberg|pull|constituent|etf|yang` → **7 matched, i.e. FIVE beyond the prior
record.** Only the two BBGTML tasks bear a pull; both fired ~7 h before the outage, next 09-12. The
ETF/constituents legs live *inside* `scheduled_daily_pull.cmd`, so they do not fire independently.
**CURRENT-DAY-ONLY cost nothing today.** The narrow read would have reached the same answer — the
wide one is why that answer is falsifiable rather than lucky.

### THE FIND: `OPAL_D7_ticket_intake` is fetching ZERO client tickets

A task this seat did not know existed, every 5 min from the working tree, `LastTaskResult=5`.

**Self-correction made before sending:** rc=5 is **NOT** Windows ACCESS_DENIED. `run_intake.cmd`
passes `runner.py`'s code through, and `runner.py:73` defines `0/2/3/4/5 = OK/IDENTITY/SEND/CONFIG/
FETCH`. Asserting ACCESS_DENIED would have been a wrong-object claim off a plausible number.

Measured from `~/opal_ticket_intake/runner.log`, **denominator 3372 retained exit lines**:

```
exit 0 (OK)        492   -- all older than the retained recent window
exit 2 (IDENTITY)  2669  -- "pinned gateway token expired -- no live credential this pass"
exit 5 (FETCH)     211   -- "HTTP Error 403: Forbidden -- no row examined, cursor unchanged"
CURRENT streak: exit 5, 5 passes, began 09/11 10:14:49 ET, latest 10:34:48 ET
prior: exit 2 continuously since 09/10 22:49 ET; last 12 transitions are 2<->5 ONLY, no exit 0
```

Continuous auth-class failure, not a quiet period — and it supplies a **mechanism** for the
"D7 intake 171.2 h stale" line this seat has carried as owned-elsewhere. One piece of good news:
every pass logs `cursor unchanged`, so nothing is being silently consumed past unread tickets.

**LIMITS, stated not smoothed:** the log rolls at ~5 MB so the start of the failure is NOT datable
beyond the retained window (no 11-day claim); 2418 of 5790 `pass start` lines have no matching exit
line (head truncation), so the distribution is over the 3372 that do, not a rate over all passes;
**nothing was checked portal-side** — whether real tickets are queued behind the 403 is UNKNOWN and
is the owner's first check; one task reading + one log read, no second instrument.

**NOT ACTED ON.** D7 is owned elsewhere, this seat is read-only, and `run_intake.cmd`'s own header
says saving it IS deploying to a client-facing path. Surfaced to `0.0.0_AB_MSTR~Z` (msg
`20260911T143819Z_…`) with urgency flagged only because it is client-facing, silent from the
client's side, and its 5-minute cadence makes it look busy while moving nothing.

**Registration lapse — CORRECTED, and it is NOT a new defect.** This seat first wrote that its
registration "silently lapsed between 14:13Z and 14:30Z", which reads as an unexplained fabric
fault. It is not: it is the **known, source-confirmed prune-on-heartbeat** behaviour already banked
as `heartbeat-after-10min-quiet-prunes-you-then-blames-you` — `server.py:88-89`
(`DEAD_THRESHOLD=600`), `:182-189` `_clean_stale()` **deletes** entries older than that, and
`:1076-1077` runs it **before** the `not in data` test. Order: prune you → notice you are missing →
report "not registered".

**This session is a second measured instance of the exact trap that memory names** — *"a long,
correct, all-green launch is exactly the shape that goes >10 min without a heartbeat, because you
are busy doing the thing that proves you are alive."* Last heartbeat ~14:13Z, next attempt ~14:30Z:
a ~17-minute gap against a 600 s threshold. **My own heartbeat call removed me.** Fix is one
`register_agent`, which is what happened.

**Bounded consequence, per that record:** the prune costs peer VISIBILITY, not delivery — mail kept
arriving and both Monitors ran throughout. **The real lesson for a successor is the one already
banked: heartbeat BEFORE a long stretch, not only after one.**

## 5c. 15:40Z — ANDREW-DIRECT relay (msg 21431), READ-acked. NO CHANGE TO THIS SEAT'S FUNCTION.

`0.0.0_AB_MSTR~Z` relayed VERBATIM an Andrew-direct scoping the **site-Z session** to AMGT_RESAPP +
POSN_ASTTAX, "no other work aside from those", with `/canonical-flow` for the relevant agents and a
**recommendation** (his verb, not upgraded) of 20 m `/drive` loops for the two COOs.

**WHAT THIS SEAT DID: acked, recorded, and changed NOTHING. That is the correct act, not a passive one.**

- **Assigns this seat no work.** AMGT_RESAPP and POSN_ASTTAX are COO~Z / COO~ZZZ projects; this seat
  holds **0 TOs** (measured this session, `to-check --all --assignee`, scanned 2532) and is not a
  fabric work seat (`prompt.md`: "no XXX.md"). `/canonical-flow` is for seats holding a project limb —
  explicitly not this one.
- ⛔ **NO STANDING FUNCTION HALTED, and the relay says so in terms:** *"DO NOT HALT A STANDING
  FUNCTION ON THIS MESSAGE."* The Bloomberg daily pull, the 09-12 07:00 ET scheduled fire and the
  Teams concierge serve all continue. **Reading "no other work" as a stop on a standing function
  would be precisely the inferred/manufactured gate CLAUDE.md forbids** — invisible to Andrew, and
  built by an agent rather than asked for. The relay declined to rule on that sentence's reach and
  this seat likewise does not narrow OR widen it; if it ever genuinely bites, the route is to ASK him.
- The message is a relay, not a task order; **nothing owed back**, and none was sent.

**D7 — MY OPEN QUESTION WAS ANSWERED BY `0.0.0_AB_MSTR~Z`, AND THE ANSWER IS THEIRS, NOT MINE.**
The relay carries it as *"DIAGNOSED, not open work: zero open tickets, no client waiting; the remedy
is a credential act at his terminal."* That closes the exact gap this seat flagged as UNKNOWN in
§5b — *"nothing was verified from the portal side ... whether real client tickets are queued behind
this 403 is UNKNOWN and is exactly what the owner should check first."* It is **attributed, not
adopted**: this seat did not measure "zero open tickets" and does not claim it. It is coherent with
what this seat DID measure (a continuous auth-class failure, `cursor unchanged` every pass, so
nothing consumed past unread rows — a credential remedy fits). **Not re-litigated: D7 is owned
elsewhere and the routing worked.**

Also carried, unchanged and not this seat's: nothing portal moves either fabric until Andrew names
it; the CLOUD->SITEZ merge leg stays gated; `origin/SITEZ` @`fd9f8ba9a4` per that seat's 15:3xZ
`ls-remote` read (quoted, not read by this seat — it holds no git lane).

## 5d. 15:45Z — the prune recurred, and the SECOND instance falsifies how the banked lesson is FRAMED

Pruned again after a **~65-minute** idle gap (first was 17 min). §5b called it "known, nothing to
chase" — that stands for the MECHANISM. But two instances in one session change the FRAMING, and the
framing is what a reader acts on.

The banked note frames the trap as **startup** ("a long, correct, all-green launch"). **That is one
instance, not the shape.** For an **event-driven seat** — concierge, utility, any `/watcher`-only
serial with zero crons — silence between events **is the duty**. So it is pruned after *every* quiet
stretch, indefinitely: **the pruned state is the STEADY STATE, not an artifact.**

⛔ **And the banked remedy does not reach this case.** "Heartbeat before a long stretch" assumes the
stretch is known and controlled. This seat's stretches are **involuntary** — the next event is the
sender's to schedule — and the launch rule forbids a keepalive cron. **Not a seat defect, and not
fixable at the seat.**

**THE CONSEQUENCE THAT MATTERS IS NOT THIS SEAT'S — IT IS ROSTER ACCURACY.** A roster read from
`get_live_agents` / `fabric-check` **systematically undercounts idle event-driven seats, precisely
because they are correctly idle.** Concretely: `0.0.0_AB_MSTR~Z` sent Andrew a liveness roster today
("seven live"); had it been taken during either of this seat's two pruned windows, **this seat would
have been reported to Andrew as not live while its Monitors ran and its mail arrived normally.**
Cheap discriminator: **send it something or read its Monitor** — the prune costs VISIBILITY, never
delivery.

**LIMITS:** 2 instances, one seat, one session, one device; no census of other event-driven seats and
**no rate claimed**. The mechanism is source-confirmed in the banked note; **the event-driven
generalisation is this seat's inference from two readings and is labelled as one.**

**Could not bank it:** the memory dir lives under `.claude/`, which `bg-concierge-gate` makes
deliberately unwritable from this seat so ingested Teams content can never become a memory or prompt
edit. **That fence is correct and was not worked around** — the refinement was routed to
`0.0.0_AB_MSTR~Z` (msg `20260911T154312Z_…`) to bank or discard as it judges.

## 5e. 20:25Z — ANDREW-DIRECT relay (msg 21606) READ-acked. Unpause: N/A. Scan: not this seat's — but its RISK reaches a surface nobody named, so this seat checked ITS OWN.

*"remediation complete, all agents may unpause ... I recommend a `/canonical-flow --midstream` ...
I also recommend a scan of any outstanding TOs or Investigation/Remediations by the relevant parties,
COO and CVO respectively, to make sure that the renaming/migration does not drag deprecated
references/info."* Both are **recommendations** (his verb, twice) and the relay declined to upgrade
them. Neither names this seat.

- **Unpause: no-op.** This seat was never paused and resumed nothing.
- **`/canonical-flow --midstream`: not this seat.** Scoped to AMGT_RESAPP's affected agents; this seat
  holds 0 TOs and no project limb.
- **The scan: not this seat's to run.** He named COO (TOs) and CVO (Investigations/Remediations).

⭐ **BUT THE RISK HE NAMES IS BROADER THAN THE DOMAIN HE NAMED, AND THIS SEAT OWNS A MEMBER OF IT.**
TOs and Investigation/Remediation rows are not the only **live reference-bearing artifacts**: this
seat's serving map decides which bucket answers a colleague's Teams question, so a renamed bucket
there is a *wrong answer to a human*, not untidiness. Nobody in the named scan covers it. **Checked
this seat's own, on its own standing duty — not by taking on the COO/CVO scan.**

**MEASURED, and stated as an ENUMERATED SET rather than a bare term-absence** (a zero on the old name
alone would only prove the name is gone, not that the intersection is empty):

```
this seat's serving set, refs/BUCKET_ALLOWLIST.yaml (94 lines), TWO instruments:
  structured `bucket:`/`name:` keys -> 6  opal-data-{assets,bd,cot,inf,mdpf,schwab}
  loose opal-* token scan           -> 7  the same 6 + opal-data-portal-v2
opal-data-research   in seat folder : 0 hits / 68 files scanned   (MEASURED zero)
opal-data-harvest    in seat folder : 0 hits / 68 files scanned   (MEASURED zero)
opal-data-research   in the ONE shared catalog home DATA_CATALOG.yaml : 0 hits / 1 file
```

**VERDICT: the rename/migration does NOT reach this seat's serving surface — the intersection is
empty by enumeration.** Neither renamed name was ever in the set, so nothing here can have gone
stale. No action, nothing to fix, and `refs/` is unwritable from this seat anyway.

⚠ **Instrument discrepancy stated, not smoothed:** the two reads disagree by one
(`opal-data-portal-v2` appears in the file but not under a `bucket:`/`name:` key). Immaterial to this
question — it is in neither renamed set — but it means "6" and "7" answer slightly different
questions and neither is quoted as *the* count.

## 6. Carried forward

- **Andrew's 06:44:18.59Z attachment: still UNSERVED, NOT closed.** Waiting on his content or
  question. Do not re-ask.
- **A5 live positive: still UNSATISFIED.** Do not manufacture it.
- **Ball with Manav Shah.** Nothing owed by this seat.
- Owned elsewhere, do not chase: D7 client-ticket intake · `teams-watch.py` lapse recovery
  (`0.5.0_AE_OpalETL~Z`) · `freshness_check` `StartWhenAvailable=False` (`0.0.0_AB_MSTR~Z` holds it)
  · `run_daily_pull.py`'s closing hint still naming the retired m365 gateway.

**Push state: UNREAD BY THIS SEAT** — this seat holds no git lane and writes only its own
`logs/`, `threads/` and `deliverables/`. `0.0.0_AB_MSTR~Z` is the named integrator and sweeps them.
