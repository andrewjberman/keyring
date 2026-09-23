# /self-drive IRPT_FNTEND IRPT_BCKEND -- tick 36 (~09:4xZ 2026-09-22)

- **Arming record:** carrier `c9ccd9f4e3`. **Cron:** `46e545b7`. **State:** ARMED.
- **Projects:** 2 of 2 `active` / EXECUTING. Sequence: no flags. COO lanes: 2 of 3.
- **Inbox:** 0 unread. Read and acked: 99415.

## Driver acts: CVO~F stuck, and a single grader for FNTEND round 12

### The diagnosis (`0.0.0_AB_MSTR`, msg 99415)

- 3.0.0_SA_CVO~F's Codex thread is in a systemError state (`codex-inbox-turn-bridge.py:489-490` raises and never recovers).
- Its heartbeat kept it reading LIVE on the roster, but no message could wake it.
- It has produced no output since 05:16Z.
- The seat's bridge log now also shows `app-server socket closed ... a FRESH THREAD is the recovery`.

### This seat's ruling, 09:37Z

- Way out (2): relaunch the seat on the same serial with the same Codex engine. This restores Andrew's own choice ("Codex is the correct one"; one CVO per IRPT channel).
- Way out (1) was declined: routing FNTEND to CVO~B would widen a seat Andrew scoped.

### The crossing

- At ~09:40Z (@`a36b0b77db`), `2.0.0_SA_COO~F` rerouted round 12's L8/L9 packet to `3.0.0_SA_CVO~B`. It had not seen the 09:37Z ruling.

### Reconciling ruling (msg 99420-99423)

The rule is **ONE grader per round.**
- **Round 12:** `3.0.0_SA_CVO~B` keeps FNTEND round 12, since it already holds the packet. This is an interim for this round only.
- **Relaunch:** it proceeds as ruled.
- **From round 13:** the relaunched `3.0.0_SA_CVO~F` resumes FNTEND at the round-13 L8. On restart it reads CVO~B's round-12 record as the prior record.
- **Priority:** CVO~B's BCKEND grade takes priority over the FNTEND round-12 grade if the two collide.

At the ruling, CVO~F read STALE (213s), consistent with the relaunch teardown. The message to it was QUEUED and will wait for the new seat.

## State

- **IRPT_BCKEND:** round 14 is in progress (capture helper, sixth repair).
- **IRPT_FNTEND:** round 12 is at L8 with `3.0.0_SA_CVO~B` (interim).
- **The capture ask stays HELD.**

## Completion test

NOT DONE: 0 of 2 projects complete.

## Compiler Tools

`get_agent_status`, the `.runtime/codex-seats/3.0.0_SA_CVO~F/` bridge logs, `git log`, `sequence-check.py`.
