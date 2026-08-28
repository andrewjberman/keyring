# /self-drive D2 & D3 — tick 9 (2026-08-28 15:46Z) — state: ARMED (RE-ARMED, fresh session)

Covers tick 9 (tick 8 logged @6062b28375 by the predecessor session, which stood down at ~00:5xZ for
the device reboot). Fresh `1.0.0_SA_CTO` session loaded 15:25Z (PID 19996, watcher task bszsawoxl).
Re-armed from the XXX.md CTO-row carrier clause @310a20e38c (UNSTRUCK) on Andrew's fresh word at
this terminal 15:32Z, VERBATIM: *"We need to get back to work on D2 and D3, I'll pull COO online."*
Cron **bde882a4** at :07/:37, cadence 30m. Paired: `/drive D2 & D3 @ 2.0.0_SA_COO` (+15m, :22/:52)
— the COO half RE-ARMED 15:41Z off the COO-row clause (2.0.0_SA_COO 78180, READ-acked).

## Scope (register-read, §0)

`D2 & D3` -> 2 of 12 live directives -> 10 projects (D2 9: 1 complete [ADVI_BDPLAT_RESTORE]; D3 1:
0 complete). Open TOs 27 (D2 20, D3 7). Flags: none. Device LAPTOP (agentbus-sqs device read:
inbound queue `sitez-to-laptop`). Claims scan 342 of 342 project JSONs: D2 7 claims / D3 1 claim,
**0 claimed-not-member** (no register lag).

## Calls pitched (§1-2)

None — zero open calls in scope on this seat's record (predecessor tick 8: zero; nothing routed in
since except an Andrew-direct relay on comp-find, 77189). `3.0.0_SA_CVO` (this fabric's CVO) is NOT
LIVE on the broker; with zero adjudicable calls there is no pitch to hold. The seating need is
surfaced to `2.0.0_SA_COO` (spawn is a COO function as of 15:32Z) — not a demand, a note that the
next tick with a call needs a live CVO.

## Verdicts since last tick (§3)

None. Ledger `org/tier1_exec/1.0.0_SA_CTO/drive_pairs/D2-D3/VERDICTS.jsonl`: 9 rows, 0 unconsumed
(COO 78180 read the same at load).

## Finding routed (driver's own lane, §3.3)

**Campaign driver seat DARK; campaign state UNMEASURED at this seat.** The ADVI_49F 533-date TWR
backfill campaign STARTED 00:52Z (~L 77170 @3fa0cc63c7; ~17.1h at 115.8s/date). Design: the driver
is strictly sequential and **PAUSES ITSELF at the pre-fire blackout ahead of the 12:45Z nightly
(~371 dates in) and needs RE-INVOCATION by ~L** (handoff @fc1f987418 UPDATE 00:52Z). Measured now:
`0.7.0_AE_CloudOps~L` NOT REGISTERED (broker) and absent from `liveness.json`; **0 messages from ~L
after 00:52Z across the three base inboxes** (1.0.0_SA_CTO, 2.0.0_SA_COO, 0.0.0_AB_MSTR — read/ +
top-level); the per-100-date reports the driver promised have not landed anywhere this seat can
read. So either the driver reached the blackout pause and has been waiting for a dead seat since
~12:2xZ, or it is still running unattended — **neither is known from here; the artifact is the
oracle.** REC (routed to `2.0.0_SA_COO`, whose act it now is): respawn `0.7.0_AE_CloudOps~L` via
`/mstr-spawn` with `--say` = read the campaign oracle (dates complete / paused / last artifact
timestamp) and report to COO + CTO before any re-invocation; a HARD-STOP row, if one exists, stops
the pass for operator judgment per the driver's own contract.

## Driver acts this tick

- Andrew-direct 15:32Z recorded + executed: `/mstr-spawn` + `/mstr-kill` widened to COO
  @b3f9f207da (7 files; broadcast 78186 MSTR / 78187 COO). Not in D2/D3 scope — it was his second
  instruction in the same word, executed before the arm.
- Re-arm: cron bde882a4; carrier RE-ARMED note appended to the XXX.md CTO row (this commit);
  scope statement to `0.0.0_AB_MSTR` (§6); ~L finding to `2.0.0_SA_COO`.

## Completion test (§4)

NOT DONE — 1 of 10 projects complete. REACHABLE 10 / UNREACHABLE 0.

## RESERVED at Andrew

None open in scope. (Outside the loop, his alone: the arm-(a) serve read after the post-campaign
P1.5 re-grade; the $51.8M insurance-attribution question to Mike, brief @45c46236fc.)

state: ARMED · push state of this log: LOCAL (origin/CLOUD @f8e1eeea7c, ls-remote read 15:29Z)

## Compiler Tools

- `python .tools/directives-check.py --json` (scope, member status, open TOs, flags — 12 live, 342 JSONs) · `bash .tools/agentbus-sqs.sh device` (device guard) · claims scan over `org/projects/*.json` `prds[]` (dict + bare-string shapes handled, denominator printed) · `comp-find --files --all` for the spawn/kill carrier census (raw estate grep timed out at 120s — Rule 21 stands) · `get_agent_status` / `get_live_agents` / `liveness.json` for ~L (three planes, all absent) · inbox listings across three base inboxes for the ~L message census.
