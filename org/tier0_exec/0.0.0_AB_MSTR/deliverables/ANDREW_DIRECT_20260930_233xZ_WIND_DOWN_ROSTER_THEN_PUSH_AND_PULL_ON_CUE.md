# ANDREW-DIRECT 2026-09-30 ~23:3xZ -- note the online roster; wind-down and relaunch; push then pull on cue

**Channel:** the `0.0.0_AB_MSTR` Claude Code terminal (laptop). **Recorded by:** `0.0.0_AB_MSTR`, same turn.

## Verbatim

> Keep a note of all the workers online right now, im going to wind down this fabric (no broadcast necessary), and
> bring it back online. Once everyone here is done, I want you to do a push to Cloud and pull afterward. I will cue you
> on that when it is time.

## Scope as given

1. This file is the note: the laptop fabric online at 23:39Z, measured below.
2. Andrew winds the fabric down himself. No broadcast from MSTR.
3. On Andrew's cue, once every seat here is done: push local `CLOUD` to origin, then pull-merge origin (site Z's
   pushes; origin was 85a765dbcd at the last read, 21:45Z). MSTR does not push or pull before the cue.
4. Andrew brings the fabric back online. This roster is the relaunch list.

## Roster at 23:39Z (broker `org/mcp/liveness.json` + OS process table, both read)

| Serial | Broker | Process | Launched by | Project(s) and last summary |
|---|---|---|---|---|
| `0.0.0_AB_MSTR` | LIVE | claude.exe 20360 | Andrew | integrator; this record |
| `1.0.0_SA_CTO` | STALE (329 s), pid 22696 not running | none | MSTR 13:03Z | laptop directives `/self-drive 30m`; last commit 7add544a20 at 23:25Z (ticks 62-64). **Died before the wind-down.** |
| `2.0.0_SA_COO~P` | LIVE | claude.exe 22148 | MSTR 13:03Z | IRPT_BCKEND workstream P + IRPT_DASHBD workstream B; r27 WK~98 on amendment 1 |
| `2.0.0_SA_COO~M` | LIVE | claude.exe 23960 | MSTR 13:03Z | IRPT_BCKEND workstream M + MDPF_SECCLASS; round 6 terminal 3/3 |
| `2.0.0_SA_COO~Y` | LIVE | claude.exe 24296 | MSTR 13:03Z | IRPT_BCKEND workstream Y (YCharts owner); r29 closed, W27 on gate |
| `2.0.0_SA_COO~D` | LIVE | claude.exe 22540 | MSTR 13:03Z | DSGN_IRPTV1 (FAST lease) + IRPT_DASHBD hop 5; portal PROD promote routed to MSTR, awaiting Andrew's re-smoke |
| `2.0.0_SA_COO~T` | LIVE | claude.exe 15512 | MSTR 13:03Z | NFRA_TRNSPT; round 2 in flight (f-2, w-2, v-2 terminal) |
| `3.0.0_SA_CVO` | LIVE | claude.exe 22660 | Andrew | L8/L9 across the laptop projects; idle, slugs sent |
| `4.0.0_SA_CRO` | LIVE | claude.exe 25000 | Andrew | MDPF_TAXSMA FAST + briefs (client reporting dashboard, transcripts) |
| `0.4.0_DS_ClientPlatform~S` | LIVE | claude.exe 23156 | `2.0.0_SA_COO~P` 14:31Z | IRPT_DASHBD TO-DB-b-1, held on Andrew's word |

Relaunch pointers: loop rows in `org/ref/LIVE_ARMS.md` (the 2026-09-28 RELAUNCH rows and the CTO laptop-directives row);
the post-crash brief of this morning, `RELAUNCH_BRIEF_20260930_130xZ_POST_CRASH.md`, still reads correctly as the
first message (assess from logs and commits, clean residue, continue `/canonical-drive`).

## Open items carried across the wind-down

- Portal PROD promote of DEV (57cf660e at 22:0xZ) waits on Andrew's re-smoke; no DT seat is live.
- Four gateway scratch branches (gw-*) on origin wait on site Z's NFRA_OPLGTW order 4.
- Laptop-local trunk: local `CLOUD` ahead of origin, 0 conflicts against 85a765dbcd at the last dry run.
