#!/usr/bin/env python3
"""teams-watch.py -- the /teams-assist monitor ENGINE (like org/mcp/inbox-watch.sh, but for Teams).

Run under the Monitor tool. Polls the Opal M365 gateway's `poll_addressed_teams_messages` via a
single stateless MCP `tools/call` to /mcp/ (the ALB-bypassed, gateway-Bearer-gated path) every
INTERVAL seconds, and prints ONE `[TEAMS] ...` line to STDOUT per NEW addressed message -- so the
Monitor wakes the agent ONLY when a real message lands (event-driven, not an LLM self-poll).

Auth: PASSIVE token reader. Reads the gateway access token from Claude Code's
~/.claude/.credentials.json (mcpOAuth.m365.accessToken) on each poll; Claude Code owns the refresh
(rotating tokens), so this never refreshes itself -> no refresh-token fight. On a 401 (token lapsed
while the session was idle) it stays quiet and retries; the next agent MCP call re-freshens it.
Session-scoped, exactly like inbox-watch.sh: it dies with the Monitor / session.

READ-ONLY: it only ever READS your own DMs/group chats via the per-user gateway. It never posts.
STDOUT = the new-message signal (one line each). STDERR = status/diagnostics (no agent ping).
"""
from __future__ import annotations

import datetime
import json
import os
import sys
import time
import urllib.error
import urllib.request

GATEWAY = "https://mcp.opalinvest.dev/mcp/"
CREDS = os.path.expanduser("~/.claude/.credentials.json")
CURSOR_FILE = os.path.join(os.environ.get("TMPDIR", "/tmp"), "teams-watch.cursor")
_nums = [a for a in sys.argv[1:] if a.isdigit()]
INTERVAL = max(3, int(_nums[0]) if _nums else 10)
ONCE = "--once" in sys.argv


def now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def read_token() -> str | None:
    """The freshest non-expired gateway access token for the opalinvest.dev MCP server."""
    try:
        d = json.load(open(CREDS, encoding="utf-8"))
        recs = [v for v in d.get("mcpOAuth", {}).values() if "opalinvest.dev" in v.get("serverUrl", "")]
        recs = [r for r in recs if r.get("expiresAt", 0) / 1000 > time.time()]
        recs.sort(key=lambda r: r.get("expiresAt", 0), reverse=True)
        return recs[0]["accessToken"] if recs else None
    except Exception:
        return None


def poll(token: str, since: str) -> dict | None:
    body = json.dumps({
        "jsonrpc": "2.0", "id": 1, "method": "tools/call",
        "params": {"name": "poll_addressed_teams_messages", "arguments": {"since_iso": since}},
    }).encode()
    req = urllib.request.Request(GATEWAY, data=body, method="POST", headers={
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    })
    with urllib.request.urlopen(req, timeout=20) as r:
        raw = r.read().decode("utf-8", "replace")
    # Streamable-HTTP SSE: the JSON-RPC envelope is on a `data:` line; the tool result text is a
    # JSON string at result.content[0].text.
    for line in raw.splitlines():
        if line.startswith("data:"):
            env = json.loads(line[5:].strip())
            content = ((env.get("result") or {}).get("content") or [{}])
            txt = content[0].get("text", "") if content else ""
            return json.loads(txt) if txt else None
    return None


def main() -> None:
    if os.path.exists(CURSOR_FILE):
        cursor = open(CURSOR_FILE, encoding="utf-8").read().strip() or now_iso()
    else:
        cursor = now_iso()
        open(CURSOR_FILE, "w", encoding="utf-8").write(cursor)

    print(f"[teams-watch] armed interval={INTERVAL}s cursor={cursor}", file=sys.stderr, flush=True)
    while True:
        tok = read_token()
        if tok:
            try:
                res = poll(tok, cursor)
                if res:
                    for m in res.get("new_messages", []):
                        # one STDOUT line per new message = one agent ping (the work-intake signal)
                        print(f"[TEAMS] {m.get('chat_type')} from {m.get('from_name')}: "
                              f"{m.get('preview')} | chat_id={m.get('chat_id')} ts={m.get('timestamp_utc')}",
                              flush=True)
                    nc = res.get("cursor")
                    if nc and nc != cursor:
                        cursor = nc
                        open(CURSOR_FILE, "w", encoding="utf-8").write(cursor)
            except urllib.error.HTTPError as e:
                if e.code != 401:  # 401 = token lapsed; quiet retry (Claude Code refreshes on next use)
                    print(f"[teams-watch] HTTP {e.code}", file=sys.stderr, flush=True)
            except Exception as exc:  # noqa: BLE001 -- a monitor must never die on a transient error
                print(f"[teams-watch] {type(exc).__name__}: {exc}", file=sys.stderr, flush=True)
        if ONCE:
            return
        time.sleep(INTERVAL)


if __name__ == "__main__":
    main()
