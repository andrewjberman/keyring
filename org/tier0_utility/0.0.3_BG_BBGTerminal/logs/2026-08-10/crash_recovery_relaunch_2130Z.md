# 0.0.3_BG_BBGTerminal — Session Log — 2026-08-10 ~2125-2135Z (crash recovery)
**archetype:** VALIDATE

## Summary
IT antivirus crash killed the box ~2023Z while ON DUTY (concierge b7043cgjl lineage ->
bj1efdgfu, watcher by0h9zuz9, cursor 17:12:19Z). Operator relaunch per MSTR~Z directive.
Full On-Launch sequence re-run: watcher + identity gate + pinned Teams Monitor all green;
cursor continuity CLEAN (no inbound missed). bloomberg_health FAIL — Terminal not
relaunched post-crash; surfaced, not touched.

## Timeline
- /watcher: registered LIVE (PID 10676, was NOT REGISTERED — crash confirmed; no orphan
  watcher process found, no identity conflict). Inbox Monitor b8xo0f7fk armed, TaskOutput
  running. Zero crons. One inbox message delivered: MSTR~Z [MSTR-DIRECT] crash-recovery
  directive (20260810T212020Z) — this session is the action.
- 2a IDENTITY GATE: whoami on opal-gateway-bbg = Opal Bloomberg
  (opalbloomberg@opalinvest.com) — PASS before any Teams read.
- Teams Monitor re-armed with RELAUNCH.md pinned line verbatim (TMPDIR, 15s,
  --server opal-gateway-bbg --identity opalbloomberg; Monitor tool, persistent, no
  wrapper). Task bhqv65yhv running; banner: pin(server=opal-gateway-bbg,
  identity=opalbloomberg) + "token selected: identity=opalbloomberg@opalinvest.com".
- CURSOR CONTINUITY: cursor file 2026-08-10T17:12:19.012Z — identical to pre-crash
  (bj1efdgfu's). First polls surfaced ZERO [TEAMS] events → no inbound missed
  2008Z-now; nothing addressed to the account since the last handled message.
- bloomberg_health: ok=false ("could not start blpapi session to 127.0.0.1:8194") —
  Terminal down post-crash. Per RELAUNCH.md error path: SURFACED to MSTR~Z/Andrew (the
  Terminal is Andrew's to bring back); cma interpreter check deferred until Terminal up.
- Daily upload guardrail (Andrew-asked @e77bec6e5): OPAL_BBGTML_daily_pull execution
  record = LastRun 2026-08-10 07:00:01 ET, LastResult 0, NextRun 08-11 07:00 ET —
  scheduled upload RAN as scheduled, no fallback needed. Data point: OPAL_vendor_watch
  last run 17:09 ET ended 0xC000013A (crash-killed mid-run), self-reschedules 18:09 ET —
  OS-level task, not the seat's; noted only.
- Shared-tree check: 1700-1715Z log's uncommitted post-window deltas still present in
  working tree (survived the crash); sweep/commit of today's thread+log files remains
  open with MSTR~Z (this file joins that sweep).

## State at close of window
ON DUTY: Teams concierge loop live (identity-pinned, bhqv65yhv), inbox watcher live
(b8xo0f7fk), broker LIVE, zero crons. Bloomberg DAPI DOWN (Terminal not running —
surfaced, blocked on operator/Andrew). Steady-state policy unchanged: whoami-then-re-arm
on each token-expiry death (~55-60m cycle; durable fix with 0.5.0_AE~Z). Open with
MSTR~Z: 2-3-sentence skill edit + sweep of today's thread/log files.

## Post-window delta (~2127Z): token-expiry death #4, cycle continues — log-only
- bhqv65yhv died exit 2 expired-token-for-identity ~2127Z, minutes after arm — consistent
  with the stored token's own expiry clock (running since the ~2008Z-cycle refresh), not
  the arm time. whoami re-gate PASS (Opal Bloomberg); re-armed bll2fl4bi, banner pin +
  token confirmed, cursor 17:12:19.012Z continuous. No inbound missed. Cadence not
  tightening → log-only per stated policy.

## Post-window delta 2 (~2131Z): rapid death #5, re-arm holds
- bll2fl4bi died exit 2 expired-token within ~2 min of arm — second rapid death; watched
  for a pattern change (whoami PASS but stored record still expired = re-mint territory).
- whoami re-gate PASS; re-armed b6mfvaas0 — SURVIVED past multiple polls (>50s, banner
  pin + token confirmed, cursor 17:12:19.012Z continuous). Read: the prior arm raced the
  whoami-triggered store refresh; the store did refresh. Not a re-mint case.
- Escalation tripwire set: a third rapid (<5 min) death → stored-record refresh is
  broken → surface to MSTR~Z for the P2 re-mint path (auth URL to Andrew), stop
  re-arm-cycling.

## Compiler Tools
None this window — MCP-surface work (whoami, Monitor arms, broker mail), Windows
Scheduled Task records, and own-folder reads/writes by exact path; no comp tool models
these surfaces.
