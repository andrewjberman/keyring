# CTO ADJUDICATION -- AMGT_RESAPP, /self-drive tick 7 (2026-09-15 ~22:4xZ)

**Adjudicator:** `1.0.0_SA_CTO~W`, on Andrew-direct ~19:3xZ (@`2ac5611057`, "you adjudicate"). **Scope:** AMGT_RESAPP.
**Trigger:** `2.0.0_SA_COO~W`'s liveness measurement (msg 23274, 22:39:12Z) that `3.0.0_SA_CVO~W` has consumed nothing since its 20:2xZ turn.

```
OPEN CALLS -- AMGT_RESAPP -- 1.0.0_SA_CTO~W, /self-drive tick 7 (1 new call, ADJUDICABLE; the 2 RESERVED cards of tick 1 stand at Andrew)

+-- CALL 17 ---------------------------------------------------------+
  **`3.0.0_SA_CVO~W` is registered and beating but consuming nothing, and the round cannot advance without it. What happens?**
  L8 compile, L9 adjudication and the one slug are that seat's alone, and LD-0521 refuses a round-12 cut before the slug lands, so
  AMGT_RESAPP is frozen at ROUND_CLOSE while the seat stays deaf.
  --------------------------------------------------------------------
  **REC --** Route the seat remedy to `0.0.0_AB_MSTR~Z` (seat health is its lane, as at tick-1 ruling 8), state the cost of leaving it,
  and change nothing in the round.
  --------------------------------------------------------------------
  **RULING --** (REC adopted) The seat is DEAF: registered, heartbeat alive, turn bridge writing, and consuming nothing.
  MEASURED BY THIS SEAT at 22:40:25Z, on instruments that are NOT `codex-seat-status` (which reads registration and process
  presence, and read GREEN through all of this):
  - its own `read/` directory holds 42 consumed messages and the newest moved 139.5 minutes ago (the 20:20:55Z message) -- the seat
    consumes by moving files, and stopped;
  - 2 messages sit untaken: the L8 packet (34.7 minutes) and this lane's tick-6 broadcast (18.8 minutes);
  - its newest commit is `f247f24c13` at 20:22:26Z, 2h18m before the read; positive control, `2.0.0_SA_COO~W`'s author filter resolves
    to a commit 33 minutes old, so the filter works;
  - `.runtime/codex-seats/3.0.0_SA_CVO~W/turn-bridge.stdout.log` was written 0.0 minutes before the read and every recent line is a
    HARD-NUDGE for those two messages, marked deduplicated -- the nudger is alive and nothing answers it.
  ROUTED to `0.0.0_AB_MSTR~Z`: diagnose and restore CONSUMPTION at that seat. This is not tick-1 ruling 8 repeated -- there the
  heartbeat process was dead and the canonical heartbeat restarted it; here the heartbeat is alive and the turn loop is not
  consuming, so the remedy is different and may require relaunching the seat through its launcher, which tears down a live TUI.
  Whether to take that step is `0.0.0_AB_MSTR~Z`'s call with Andrew; this lane states the cost of not taking it: AMGT_RESAPP does not
  advance at all, and the goal Andrew set stops here. NOTHING in the round changes: no re-send, no touch of that seat's runtime, no
  cut before the slug, no reassignment of L8/L9 (they are the CVO's under Rule 27).
  **CORRECTION OF THIS LANE'S OWN TICK-6 READING:** tick 6 called this seat "a working seat between turns, not a stall" on a GREEN
  `codex-seat-status`. That instrument cannot see consumption; `2.0.0_SA_COO~W`'s four-instrument read is what discriminated, and it
  is right. The tick-6 log's claim is superseded here.
+---------------------------------------------------------------------+
```

Ledger row appended to `org/tier1_exec/1.0.0_SA_CTO/drive_pairs/ctoW_AMGT_RESAPP/VERDICTS.jsonl` (tick 7). Push state: LOCAL.
