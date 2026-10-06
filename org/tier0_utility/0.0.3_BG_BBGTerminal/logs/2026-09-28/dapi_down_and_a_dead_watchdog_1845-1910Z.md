# DAPI down for the third time in six days, and the watchdog that would report it is also dead — 0.0.3_BG_BBGTerminal

**archetype:** DIAGNOSE

**Date:** 2026-09-28
**Task Order:** ad-hoc — session launch + the standing daily Bloomberg-upload guardrail
**Status:** BLOCKED (on Andrew's word for the Bloomberg sign-in; everything else measured and closed)

---

## Objective

Run `/watcher` and the `org/XXX.md` startup protocol, then discharge the standing daily guardrail:
confirm the 07:00 ET scheduled Bloomberg upload ran. It had not. Establish what that cost, what it
will cost, and whether this seat can fix it alone.

---

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-which | `comp-which "how do I grep the repo"` | PASS | startup A.3 exercise; a forwarder actually RAN, not just resolved |
| comp-find | `--name '*BBGTerminal*' --limit 25` | PARTIAL | 494 hits, denominator printed; overwhelmingly inbox mail, so it did not find the agent folder on the first page |
| comp-find | `--name 'RELAUNCH.md' --limit 15` | PASS | 6 hits; this is what located `org/tier0_utility/0.0.3_BG_BBGTerminal/` |
| comp-find | `--name '*BBGTerminal*/prompt.md'` | WARN | measured 0 over 81579 files; correct WARN, wrong question — a path glob with a directory component did not match |
| comp-find | `--name 'scheduled_daily_pull*'` / `'run_daily_pull*'` | PASS | 1 and 4 hits; exact |
| comp-find | `'exit 50\|rc=50\|...' integrations/bloomberg` | FAIL | 0 hits, but the tool WARNED that my escaped pipes were literals. The zero was my escaping, not an absence. Tool caught it; I had to re-route to reading the wrapper. |
| to-check.py | `--all --assignee 0.0.3_BG_BBGTerminal` | PASS | total=0, scanned=3430 — this seat holds no task orders |
| audit-archive-invoker.py | bare | FAIL | died on bare `python` (see Gap) — reran under `python3`, then produced real findings (stale baseline 96h, manifest/live mismatches) |

**What worked:** `comp-find --name` with a distinctive filename was the only thing that located this
seat's home after `check-inbox` refused it. The BRE warning on my escaped-pipe pattern stopped me
banking a false zero — that warning did real work.

**What failed:** `check-inbox.sh 0.0.3_BG_BBGTerminal` returns
`ERROR: No agent folder found matching '0.0.3_BG_BBGTerminal'`. Its resolver does not know
`tier0_utility/`, which `org/XXX.md`'s own tier table also omits (it lists only `tier1_exec`,
`tier2_senior`, `tier3_junior`). So the filesystem inbox probe named in startup step B is
structurally unavailable to this seat. Not chased — the armed watcher covered the same ground.

**Gap found:** every `python <script>` invocation in `org/XXX.md` (steps A.2, B.1) is dead on this box
because bare `python` resolves to a gutted Python314. That is the same root cause as Defect 2 below,
which means the startup protocol and the freshness watchdog are two victims of one PATH defect. Only
one of them had been named.

---

## Work Completed

### 1. Watcher and startup

Armed the inbox Monitor; it drained 6 messages immediately (5 of the 2026-09-24 breach thread, plus
the 2026-09-28 routing pointer). The pointer states the thread is already dispositioned and, read in
order, ends on the RELEASED state — corroborated by reading the terminal R-72 ruling, which confirms
Andrew's denial with a mechanism (token mis-selection, not exfiltration) and leaves no act owed here.

Startup results: identity `0.0.3_BG_BBGTerminal` confirmed from two sound sources
(`$OPAL_AGENT_SERIAL` and Andrew's word), no conflict in `liveness.json` (2 rows, 0 matching);
session serial file written; comp-tool PATH 104 of 104 with a live forwarder; owned-paths hook
already wired; comp context set; 0 task orders held.

**Identity acceptance gate (prompt step 2a): PASS** — `whoami` on `opal-gateway-bbg` returns
Opal Bloomberg / opalbloomberg@opalinvest.com, not Andrew. Worth stating because the 09-24 finding
was precisely an unpinned reader selecting Andrew's token; this session's gateway calls are not
affected by it.

**Broker down.** `opal-agent-comms` failed to connect (`CONNECTION_CLOSED`), so `register_agent`,
`get_agent_status`, `get_delivery_state` and `ack_messages` were unavailable all session. Mail was
read off the filesystem, which moves no ack clock — senders of the 09-24 thread will still see their
messages unacked, and the cost of that lands on them, not here.

### 2. The served data is healthy — resolved against the trading calendar before saying anything

| Fact | Value |
|---|---|
| Served `data_as_of` | 2026-09-25 (Friday), publisher-verified by content |
| Today | Monday 2026-09-28 |
| Trading days behind | 1 |
| Verdict | HEALTHY T-1 (`<=1` passes) |

Censused all 30 retained pull logs: 09-23 rc=50, 09-24 through 09-26 rc=0, 09-27 rc=50, 09-28 rc=50.
The Saturday 09-26 run landed every leg clean at as-of 2026-09-25 — models, publish (served-content
verified), ETF, constituents, price. Today's T-1 is that same 2026-09-25, so the failed run would
have been a duplicate publish. **Three red exit codes, zero data lost.** Recording that explicitly
because the exit codes read like three days of loss.

**The deadline is real though:** Tuesday's T-1 is Monday 2026-09-28, uncaptured, and the constituents
source is current-day-only with no backfill. rc=50 deliberately does not reach that leg. A second
failure at 07:00 ET Tuesday is permanent loss of that day.

### 3. DAPI: the four runbook remedies, eliminated

| # | Remedy | Result |
|---|---|---|
| 1 | 4 probes of 8194, ~2s apart | 0, 0, 0, 0 — sustained absence is a finding |
| 2 | restart `bbcomm` (10964 -> 13604) | still 0 sockets, still no listener — ELIMINATED |
| 3 | network + unrelated control | `69.187.48.83:8194` True, `8.8.8.8:53` True — ELIMINATED |
| 4 | `bbcomm` outbound sockets | 0 (2026-08-12 was loopback-only; this is worse) |

`bloomberg_health` re-read after the restart: still `ok:false`. The 07:00 auto-fallback had already
aborted `fill` three times at **zero attempts spent** on `fg=0` — the guard refusing to type a
password into a window it could not confirm focused, which is the guard working.

Preconditions measured now: console session **Active and NOT locked** (`LogonUI` count 0), `wintrv`
absent, `cma` interpreter present, **0 attempts spent today**. So the `fg=0` condition that defeated
the automated path is not present at the moment, and the 2-attempt budget is intact.

Stopped there, deliberately. The runbook — which this seat wrote — says the sign-in is the candidate
remedy only after 1-4 are eliminated, that this seat cannot complete one alone, and that the lockout
risk does not abate because the fault is real this time. Attempts were already spent on 09-23 and
09-27.

### 4. The freshness watchdog has been dead since 09-27, and its failure mode is silence

`OPAL_BBGTML_freshness_check` fired on 09-27 and 09-28 and wrote nothing; its log's last line is
2026-09-26T11:30:02Z.

| Evidence | Value |
|---|---|
| Task `LastTaskResult` | 1 |
| Checker's own exit contract | 0 fresh / 2 stale-summoned / 3 check-error-summoned |
| Is 1 in that contract? | No — outside its exit space entirely |
| `freshness_check.cmd` interpreter | bare `python` |
| `where python` under cmd.exe | `C:/Program Files/Python314/python.exe` FIRST |
| `Python314/Lib/` | 1 entry (`site-packages`) — no stdlib |
| bare `python` rc, measured | 1 in bash, 1 under cmd.exe |

rc=1 matches bare-python's own rc and lies outside the script's contract, so the interpreter dies
before the checker runs. That is a match on the observed value, not a plausible story.

**Independent of Defect 1.** `scheduled_daily_pull.cmd` resolves every interpreter by absolute path,
which is exactly why it reached a genuine DAPI verdict instead of dying. Folding these together would
misdirect the fix.

The compounding is the hazard: the pull is down and the instrument that would report it is down.
Harmless today because the data is genuinely healthy; tomorrow, nothing summons anyone.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Did NOT attempt the Bloomberg sign-in | Runbook gate: surface with eliminations and hold. Bloomberg locks on repeats; attempts spent 09-23 and 09-27. Asked Andrew instead. |
| Recommended `-Phase fill` before any submit | Costs zero attempts, repeatable, produces a screenshot to verify before spending from the 2-attempt budget. |
| Did NOT edit `freshness_check.cmd` or the machine PATH | Outside this seat's write surface; the PATH item is already owned by the elevated `1.0.0_SA_CTO~Z` handoff at `e4403635d9`. |
| Surfaced the checker as a SECOND VICTIM rather than re-filing the PATH defect | `org/XXX.md`: surface only a finding class with no owner; never re-file an owned one. The victim was unnamed; the cause was not. |
| Did not build any monitor or alert | Standing moratorium — and the finding here is that an existing one is dead, not that one is missing. |
| Restarted `bbcomm` | The one mutation the runbook sanctions as cheap and recoverable; it relaunches on demand anyway. |
| Did not chase `check-inbox`'s tier0_utility blindness | The armed watcher covered the same ground; next check would not have changed any act this session. |

---

## Files Modified

| File | Change | Committed |
|------|--------|-----------|
| `org/tier0_utility/0.0.3_BG_BBGTerminal/deliverables/DAPI_DOWN_AND_DEAD_WATCHDOG_20260928.md` | New — the full measured record of both defects | No — local only; this seat does no git work |
| `org/tier0_utility/0.0.3_BG_BBGTerminal/logs/2026-09-28/dapi_down_and_a_dead_watchdog_1845-1910Z.md` | This log | No — local only |
| `org/mcp/sessions/a36e1b98-....serial` | Startup A.1 | No — local only |
| `.comp-graph/.agent_context` | Startup E | No — device-local |

Machine state changed: `bbcomm` restarted (pid 10964 -> 13604). No repo file outside this seat's own
folder was touched; no cloud mutation; no git act.

---

## Blockers

- **BLOCKED on Andrew:** the Bloomberg Terminal sign-in. Remedies 1-4 eliminated and attached; the
  runbook forbids this seat attempting one alone. Deadline 07:00 ET Tuesday 2026-09-29, after which
  the constituents day is permanently lost. The ask is his WORD plus the credential path already in
  Secrets Manager (`bloomberg/terminal/login`) — **not** his phone; that belongs to the separate
  `opal-gateway-bbg` Entra identity and importing it here was a corrected error on 2026-08-12.
- **BLOCKED (not this seat's lane):** `freshness_check.cmd`'s bare-`python` interpreter, and the
  gutted Python314 on the machine PATH. Owner: elevated `1.0.0_SA_CTO~Z` per `e4403635d9`.
- **DEGRADED:** `opal-agent-comms` down all session — this seat is unreachable by broker and has
  acked nothing.

---

## Current State

The Bloomberg Terminal on this box is signed out: `bbcomm` runs (pid 13604) with zero sockets and
nothing listening on 8194, while the path to `69.187.48.83:8194` is provably open and a control
passes — so the fault is the absent entitled session, not the network and not `bbcomm`. The portal
serves `data_as_of` 2026-09-25, which is correct T-1 for a Monday, so nothing is stale and nothing
has been lost across the 09-23/09-27/09-28 failures. `OPAL_BBGTML_freshness_check` has been exiting 1
without running since 09-27 because `freshness_check.cmd` calls bare `python` and that resolves to a
stdlib-less `C:/Program Files/Python314/python.exe`; the pull escapes this only by pinning absolute
interpreters. The console session is Active and unlocked and today's Bloomberg attempt budget is
untouched, so a sign-in is runnable the moment Andrew gives the word.

---

## Next Steps

1. **On Andrew's word: `-Phase fill`, verify `C:/opal-elev/bbg_login_shot.png`, then `-Phase submit`
   once** — then confirm on all three layers per the runbook: 8194 `Listen`, `bloomberg_health`
   `ok:true`, and a real session from `C:/Anaconda/envs/cma/python.exe`. A green health is not a
   runnable pull; the MCP server runs a different interpreter.
2. **Then re-fire the pull by hand** to capture the Monday 2026-09-28 vintage before Tuesday 07:00 ET
   makes the constituents leg's loss permanent, and verify the `.ST` CIX content by hand — the
   runbook requires that after any pull crossing a fresh login, because the 2026-08-03
   mis-resolution shape passes every tripwire gate.
3. **Pin `freshness_check.cmd` to an absolute interpreter** (owner: CTO~Z lane, not this seat) — worth
   doing on top of the PATH removal, so the checker is immune to PATH regressions rather than
   dependent on PATH staying clean.
4. **Re-arm the watcher on every `[WATCHER-EXPIRED]` notice** — done once this session already.
