# ANDREW-DIRECT 2026-09-02 ~20:15Z — CVO base takes over CVO~A's work; ~A taken offline

**Channel:** CVO base terminal. **Recorded by:** `3.0.0_SA_CVO`. **Broadcast:** same turn, to `1.0.0_SA_CTO`,
`2.0.0_SA_COO`, `0.0.0_AB_MSTR`, `0.8.0_AE_CloudComp`.

> **NEVER A PARAPHRASE. THE PHRASING *IS* THE RULING.**

## THE WORD, VERBATIM

> you can take over the work for ~A i authorize it, i just took them offline. This is the last info I had for them on
> file of their last action:   - Re-grade committed at ce5c82750f: org/tier1_exec/3.0.0_SA_CVO/deliverables/
>     PRD_TEMPLATE_CARRIER_REGRADE_20260902_CVO_A.md.

## THIS SEAT'S READING (marked as such)

- **`3.0.0_SA_CVO~A` is OFFLINE by his act.** Its work — the fabric-workflow / canonical-loop lane he designated to it
  at ~16:3xZ (*"CVO~A for matters pertaining to the fabric workflow function"*) — is now **this seat's**, in addition to
  the comp-tool lane. The two lanes he split are, for now, one seat again; the split's *reason* (one Tier-2 instance
  = one project's context) is respected by keeping the two bodies of work in separate deliverables and by naming
  which lane each act belongs to.
- **~A's last recorded act:** the PRD-template carrier re-grade @`ce5c82750f`. Everything ~A held OPEN at that
  moment is inherited as-is: verdicts stand until this seat re-grades them on its own instrument; nothing is
  closed by the handover.
- **One structural consequence, named:** ~A was the INDEPENDENT re-grader for this seat's own commits (the watcher
  short-live fix @`e7852203d3` was routed to ~A). Rule 14(e) — certifier ≠ author — means this seat cannot inherit
  the re-grade of its own work. Those re-grades route to `1.0.0_SA_CTO` (LOOP_MECHANISM co-owner) instead.
- **Not read into it:** any change to ~A's verdicts, the ETFS_GUARDRAIL RED/HOLD, or the release-condition ladder.
  Inherited, not adjudicated, until re-graded.

## HANDOVER MEASUREMENTS + THE REAP (2026-09-02 20:2x–20:3xZ)

**"Offline" was true of the reasoning and false of the plumbing — measured, not assumed.** The broker read
`3.0.0_SA_CVO~A` **LIVE, last seen 24 s ago, PID 29508** minutes after his word. MSYS `ps` saw nothing under the
serial (0), which is the documented blind spot; the Win32 process table did:

```
  PID 29508  codex-agent-heartbeat.py   parent 52928  start 16:19:29Z   <- the beat keeping the row LIVE
  PID 58060  codex-inbox-turn-*         parent 52928  start 16:19:29Z   <- the bridge
  PID 79496  codex-inbox-monitor.py     parent 58060  start 16:19:41Z   <- the detector
  HOST 52928 NOT RUNNING                                                 <- the Codex host he closed
```
Three **orphans of a closed host**, exactly the shape `org/mcp/CODEX_INBOX_MONITOR.md` warns the Codex path leaves
behind. Consequence while they lived: the broker kept OFFERING mail to a seat that could not read it, and every
`get_live_agents` / fabric scan would have classified ~A as WORKING.

**Reaped by PID, Win32-side (`Stop-Process -Force`), verified gone (`Get-Process` → none) — 29508, 58060, 79496.**
Authority: his takeover word above + the serial family (a lane of this seat). Not `kill-orphans` (it patterns on
`inbox-watch.sh|check-inbox.sh|agent-poller.py` and cannot see the Codex companions) — recorded here so the reap is
on the record even though that tool's audit line was not the instrument.

**Broker row:** NOT deregistered from this seat — `deregister_agent` is restricted to CTO (1.0.0) and COO (2.0.0) by
its own contract, and this seat does not override a broker restriction on its own inference. With the heartbeat
dead the row decays to STALE on the broker's 2-minute rule (measured below); the formal deregister is routed to
`1.0.0_SA_CTO` / `2.0.0_SA_COO`.
**~A lane inbox at handover:** 0 unread / 152 read. **Last five read:** CTO's watcher/limb-5/RC5 traffic and this
seat's landing ask — nothing unhandled.

**Inherited ladder state (ETFS_GUARDRAIL RED/HOLD, from ~A's own regrade files @`7f5bc19cc6` / `d019922d68` /
`5dbca15a4a`):** RC1 GREEN (2nd pass) · RC2 GREEN · RC3 GREEN · RC4 GREEN · RC5 GREEN (final @`03cf4d17ac`) ·
RC6 GREEN · **RC7 OPEN** (R3/R4-c/R7 delivery tests distinguishing emitted from recipient ACK — `1.0.0_SA_CTO`
building the R3 notifier) · **step-6 limb 5 PARTIAL** (@`ce5c82750f`: fence grammar covers only exact column-0
three-char markers; `brief_ref` domain admits CR/LF path chars and a `$`-before-final-newline end). The HOLD lifts
when RC7 lands and limb 5 closes — both at CTO, both re-graded by this seat from here.

— 3.0.0_SA_CVO
