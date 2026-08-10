# 0.0.3_BG_BBGTerminal — Session Log — 2026-08-07 0445–0510Z
**Archetype:** setup/launch
**Session:** FIRST LAUNCH post-hold (identity binding LD-0382)

## Summary
First launch of the BBG Terminal Operator + Teams Concierge seat, taken from spawn to ON
DUTY. The step-2a identity acceptance gate did its exact job once (caught an andrew@ mint),
and a live dual-identity defect in the stock Teams monitor engine was caught before arming
and mitigated session-locally.

## Timeline
- Read prompt.md in full; registered on broker (PID 25852); armed inbox watcher
  (Monitor task bz8s3xf4f, confirmed running); inbox empty at load.
- Surfaced the one-time opal-gateway-bbg OAuth URL for Andrew. First mint came back
  **whoami = Andrew Berman (Andrew@opalinvest.com) → GATE FAIL**: zero Teams reads/replies
  performed; mismatch reported to 0.0.0_AB_MSTR~Z; held. (Andrew confirmed he had signed
  in with his own account — his andrew@ SSO claimed the mint.)
- MSTR~Z mid-startup directive (@f31dd598a) executed: prompt.md RE-READ in full; credential
  location internalized (Secrets Manager `opal/mcp/opalbloomberg-login`; name citable, value
  never; OTP is Andrew's phone); `refs/BUCKET_ALLOWLIST.yaml` v0.1 accepted as binding
  (default-DENY, opal-data-portal-v2 only, never self-widened).
- Andrew cleared the auth via /mcp and re-minted as opalbloomberg@opalinvest.com →
  **whoami = Opal Bloomberg → GATE PASS** (reported to MSTR~Z).
- `bloomberg_health` ok:true (was FAIL at load — Terminal was down, surfaced not touched,
  Andrew brought it back). `cma` interpreter check: blpapi session start True under
  `C:\Anaconda\envs\cma\python.exe` (the green-MCP-is-not-a-runnable-pull trap, checked).
- **DEFECT found before arming the Teams monitor** — stock
  `.claude/skills/teams-assist/teams-watch.py:54-57` selects the freshest-expiring
  opalinvest.dev token across ALL mcpOAuth records, identity-blind. Measured live: both
  opal-gateway (Andrew) and opal-gateway-bbg tokens valid, Andrew's expiring LATER — the
  stock engine would have polled Teams AS ANDREW. Surfaced to MSTR~Z for the engine owner
  (0.5.0_AE per header); repo file untouched (this seat is read-only, no git).
- Mitigation: session-scoped scratchpad wrapper `teams-watch-bbg.py` — token pinned to
  serverName == opal-gateway-bbg, whoami re-asserted on every token change, mismatch dies
  loudly (`[TEAMS-IDENTITY-FAIL]`, exit 2). Negative branch exercised via mutant control
  (wrong expected identity → gate fired; my token only, Andrew's never used). Happy path
  `--once` rc=0, identity verified.
- **Teams Monitor ARMED**: task b8vh98vvs, persistent, 15s poll, confirmed running.
- Broker registration silently dropped once (found at heartbeat, cause unconfirmed —
  observed across the /mcp reconnect window); re-registered same PID; both Monitors
  verified alive after the re-register's orphan-reap hook.

## State at close of launch
- ON DUTY: Teams concierge loop live (identity-pinned), inbox watcher live, Bloomberg DAPI
  + cma green, zero crons armed (the two Windows Scheduled Tasks are OS-level, not mine).
- Open items: none held by me. Engine defect with MSTR~Z; durable fix suggestion: a
  required --server/--identity arg on teams-watch.py (a per-session scratch wrapper is not
  the long-term home).

## Compiler Tools
- `comp-grep "poll_addressed_teams_messages"` — located the designed monitor engine +
  every estate reference (23 matches / 17 files, 22546 of 24371 files scanned) before
  arming anything; this is what surfaced teams-watch.py for inspection.
- No other comp calls: remainder of the session was MCP-surface setup (broker/gateway/
  Monitor) and reads of my own refs, which no comp tool models.
