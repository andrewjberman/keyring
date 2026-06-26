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

INCOMING ONLY (Andrew-direct 2026-06-26): the monitor fires on messages addressed TO you, never
on your OWN outgoing messages -- triggering on outgoing is noise (you don't need to be woken by
what you just sent). Each new message is filtered through `is_outgoing()` before it becomes an
agent ping: a message is dropped if the gateway flags it from-me, or if its sender resolves to the
authenticated user (the gateway-token `sub`). The exact gateway sender field is honored defensively
(see `is_outgoing`); a message with NO usable self-indicator is treated as incoming (fail-open to
not silently drop a real ask) and logged once to stderr so the sender schema can be confirmed.
"""
from __future__ import annotations

import base64
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
_SCHEMA_WARNED = False  # one-shot stderr note when a message carries no self-indicator field


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


def self_id(token: str | None) -> str | None:
    """The authenticated user's identity (gateway-token `sub`, lowercased) -- who 'me' is, so the
    monitor can drop my OWN outgoing messages. Best-effort JWT-claim read (no signature check: it's
    our own token, read only to know our identity); returns None on an opaque/unreadable token."""
    if not token:
        return None
    try:
        parts = token.split(".")
        if len(parts) < 2:
            return None
        pad = parts[1] + "=" * (-len(parts[1]) % 4)
        claims = json.loads(base64.urlsafe_b64decode(pad))
        sub = claims.get("sub") or claims.get("preferred_username") or claims.get("upn")
        return str(sub).strip().lower() if sub else None
    except Exception:
        return None


_ME_NAME: str | None = None       # cached authenticated-user display name (whoami)
_ME_NAME_FETCHED = False          # whoami attempted (don't retry every poll if it returned nothing)


def self_name(token: str | None) -> str | None:
    """The authenticated user's DISPLAY NAME (e.g. 'Andrew Berman') -- the only field that matches
    the gateway's per-message `from_name`, so the monitor can drop the user's OWN outgoing messages.
    The token has no `name` claim (sub=email only), so fetch it ONCE via the gateway `whoami` tool
    and cache it. Best-effort: on any failure returns None and the outgoing-filter falls back to the
    email/machine-id branches (effectively inert) -- never blocks the monitor."""
    global _ME_NAME, _ME_NAME_FETCHED
    if _ME_NAME_FETCHED:
        return _ME_NAME
    _ME_NAME_FETCHED = True
    res = _gateway_call(token, "whoami", {}) if token else None
    if isinstance(res, dict):
        nm = res.get("displayName") or res.get("display_name") or res.get("name")
        _ME_NAME = str(nm).strip() if nm else None
    return _ME_NAME


def is_outgoing(m: dict, me: str | None, me_name: str | None = None) -> bool:
    """True if message `m` was sent BY the authenticated user (an outgoing message we must NOT wake
    on). Honors an explicit gateway flag first; else matches the sender against `me` (token sub /
    email) and `me_name` (the authenticated user's DISPLAY NAME) across the plausible sender fields.
    Fail-open: if no flag and no usable sender field resolves, the message is treated as INCOMING
    (returns False) so a real ask is never silently dropped.

    GROUNDED SCHEMA (0.5.0_AE 2026-06-26, against the live gateway): poll_addressed_teams_messages
    returns ONLY {chat_id, chat_type, from_name, preview, timestamp_utc, is_mention} per message --
    NO is_from_me/direction flag and NO machine sender-id; the sole sender field is `from_name`, a
    DISPLAY NAME ("Andrew Berman"), sometimes null. The gateway token is also minimal (sub=email
    only, no `name` claim). So the ONLY workable self-match today is from_name vs the authenticated
    user's display name (`me_name`, fetched once via whoami). The branches below keep the email/
    machine-id matches for forward-compat if the gateway adds those fields; the server-side
    `is_from_me` boolean remains the durable fix (collision-proof) -- flagged to the gateway owner."""
    global _SCHEMA_WARNED
    # (1) explicit gateway flag -- the authoritative signal if the gateway ever sets one
    for k in ("is_from_me", "from_me", "is_outgoing", "outgoing"):
        v = m.get(k)
        if isinstance(v, bool):
            return v
    if str(m.get("direction", "")).strip().lower() == "outgoing":
        return True
    fname = str(m.get("from_name", "") or "").strip().lower()
    # (2) display-name match -- the ONLY self-indicator the current gateway schema actually carries
    if me_name and fname and fname == me_name.strip().lower():
        return True
    # (3) email / machine-id match against `me` (token sub) -- forward-compat for a richer schema
    if me:
        local = me.split("@")[0]
        for k in ("from_id", "from_email", "from_upn", "from_aad_id", "from_user_id", "from_name"):
            c = str(m.get(k, "")).strip().lower()
            if c and (c == me or c == local):
                return True
    # No machine sender-id AND no display-name to match on -> note once, then fail-open
    if not me_name and not any(
        m.get(k) for k in ("from_id", "from_email", "from_upn", "from_aad_id", "from_user_id")
    ):
        if not _SCHEMA_WARNED:
            print("[teams-watch] note: no machine sender-id and no self display-name resolved "
                  f"(keys={sorted(m.keys())}); outgoing-filter inert -- confirm whoami/gateway schema",
                  file=sys.stderr, flush=True)
            _SCHEMA_WARNED = True
    return False


def _gateway_call(token: str, name: str, arguments: dict) -> dict | None:
    """One stateless MCP tools/call to the gateway; returns the tool's parsed JSON result (or None)."""
    body = json.dumps({
        "jsonrpc": "2.0", "id": 1, "method": "tools/call",
        "params": {"name": name, "arguments": arguments},
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


def poll(token: str, since: str) -> dict | None:
    return _gateway_call(token, "poll_addressed_teams_messages", {"since_iso": since})


def main() -> None:
    if os.path.exists(CURSOR_FILE):
        cursor = open(CURSOR_FILE, encoding="utf-8").read().strip() or now_iso()
    else:
        cursor = now_iso()
        open(CURSOR_FILE, "w", encoding="utf-8").write(cursor)

    print(f"[teams-watch] armed interval={INTERVAL}s cursor={cursor} (incoming-only)", file=sys.stderr, flush=True)
    while True:
        tok = read_token()
        if tok:
            me = self_id(tok)
            me_name = self_name(tok)  # cached after first poll; the display-name self-match key
            try:
                res = poll(tok, cursor)
                if res:
                    for m in res.get("new_messages", []):
                        # INCOMING ONLY: skip my own outgoing messages (Andrew-direct 2026-06-26)
                        if is_outgoing(m, me, me_name):
                            continue
                        # one STDOUT line per new INCOMING message = one agent ping (work-intake signal)
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
