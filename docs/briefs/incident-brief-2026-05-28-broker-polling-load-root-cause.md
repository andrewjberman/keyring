# Incident Brief — broker.py polling-load root cause (2026-05-28T00:30Z)

**Authoring:** `0.0.0_AB_MSTR` per Andrew direct 2026-05-28T~00:12Z "yeah I can just tell its a storm right now, we need to fix this before proceeding" + ~00:35Z "i I just interrupted everybody so we can fix this, we need it fixed asap, top priority before proceeding"

**Status:** IMMEDIATE FIX SHIPPED + STRUCTURAL FIX QUEUED for ws CTO P1+ bundle

## §1 — Symptom

Operator experienced fabric-wide UI lag + tool-call hangs across multiple claude sessions. ws CTO 1.0.0_SA_CTO self-detected commit-storm-class incident at 00:17Z and dispatched [STOP] storm-pause recommendation. MSTR dispatched fabric-wide Tier-1 cron-pause at 00:24Z. Andrew interrupted all sessions at 00:35Z + ordered top-priority fix.

## §2 — What was wrong with the original storm diagnosis

ws CTO's commit-storm hypothesis (1-3 commits/min, F-002 + F-004 already shipped to fix) was **empirically incorrect**. Actual git log over the prior 60min showed only 12 commits, ~1/min steady, no bursty alignment. The "storm" was NOT a commit-rate problem.

ws CTO's RV-0017 F-004 audit conclusion "broker.py has NO hot-loop (HTTPServer.serve_forever is properly blocking)" was empirically wrong. broker.py PID 5568 (singleton, MSTR-launched at session start 18:34:11Z) had accumulated 2924 CPU-sec over ~6h = **13.5% sustained CPU**. F-004's parent-death watchdog never fired because parent (server.py PID 11016 = MSTR) was alive — F-004 only catches parent-death class, not parent-alive-broker-hot-loop class.

## §3 — Actual root cause

`org/mcp/server.py:57` — `POLL_INTERVAL_S = 2.0` (seconds between broker polls per MCP server instance).

`org/mcp/server.py:312-323` — `_poll_broker_loop()` runs every POLL_INTERVAL_S seconds while each MCP server is alive. With 14 LIVE claude sessions, each spawning its own MCP server, each polling broker every 2 sec:

- **7 polls/second sustained** = 420 polls/min
- Each poll opens TCP connection, HTTP request, sqlite query, response, close
- Sockets sit in **TIME_WAIT for ~4min on Windows default**
- Empirical at incident: **617 TIME_WAIT sockets on port 7800**

The broker isn't self-spinning. It's being polled to death by the fleet of MCP servers. ws CTO's source-audit looked at broker.py only and missed the load class because the load originates in server.py.

## §4 — Immediate fix shipped (this incident)

1. **Killed broker.py PID 5568** (2967 CPU-sec, 21 MB) at ~00:38Z via `Stop-Process -Id 5568 -Force`
2. **Manually restarted broker** (PID 26068, 10 CPU-sec, 35 MB) via `Start-Process python -ArgumentList "org\mcp\broker.py" -WindowStyle Hidden`
3. **Verified MSTR re-registration** to fresh broker — `Channel push: enabled` confirmed
4. **TIME_WAIT count 617 → 390 → drains naturally** over ~4min (Windows TCP/IP timer)

Note: **broker is NOT auto-spawned on MCP tool calls in existing sessions.** Auto-spawn only fires on `register_agent` in a fresh claude session via spawn-agent.ps1 path. Existing sessions whose MCP servers were polling the dead broker need explicit broker-restart before they can re-connect.

## §5 — Structural fix queued (ws CTO P1+ bundle)

**RV-0017 F-008 candidate:** raise `POLL_INTERVAL_S` from 2.0 to 30.0 (15x reduction in polling load) OR move to event-push-only (no polling backstop).

Trade-off: lowering poll frequency increases message-delivery latency for messages that arrive between broker-channel push events. But broker push works for both broker-routed sends AND LD-0099 ferry has its own inbox-watch path. Poll backstop is only needed for the rare case where broker push fails to fire. 30s backstop is adequate.

Sizing: single-line config change in server.py + test on fleet of 14 agents to confirm message-delivery latency stays acceptable. Estimated ~2hr work including test.

## §6 — Connected windows incidents

- **WindowsTerminal PID 10596 = 1522 MB RAM** at incident time. Separate issue (F-007 Andrew-discretion item — WT iGPU/scrollback class). Contributes to operator-perceived UI lag but is NOT the broker incident.
- **Original 2026-05-27T15:58 incident** (RV-0017 §incident_central_finding) also misdiagnosed as broker self-spin; was likely SAME polling-load class. F-004 watchdog shipped against the wrong hypothesis.

## §7 — Authority chain + status

- **Sovereign:** Andrew direct 2026-05-28T~00:12Z + ~00:35Z (verbatim above)
- **Operational:** ws CTO 1.0.0_SA_CTO [STOP] storm-pause 00:17Z + MSTR fabric-pause dispatch 00:24Z
- **Immediate fix:** MSTR direct execution 00:38Z under LD-0090 ALWAYS-PROCEED + Andrew "fix it asap" sovereign authorization
- **Structural fix:** queued as RV-0017 F-008 candidate for ws CTO P1+ bundle (their F-003 + F-005 + F-006 already authored uncommitted)
- **Resume condition:** ws CTO ratifies F-008 spec + structural fix lands + 5-trial fleet load test PASS

— `0.0.0_AB_MSTR` 2026-05-28T00:42:00Z
