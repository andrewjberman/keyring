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

IDENTITY PIN (OPAL_ANALYST PRD 4.1, 2026-08-10): optional `--server <substring>` /
`--identity <sub/UPN substring>` flags filter the mcpOAuth records to the named server/identity
BEFORE the freshest-expiring sort. No matching token after the filter -> LOUD exit 2 with a named
reason ([TEAMS-IDENTITY-FAIL] on stdout so the Monitor pings the agent) -- NEVER a fallback to
another identity. Expired-only matches and ambiguous multi-matches exit the same way (never
sort-and-hope). BARE invocation (no flag) keeps the legacy selection behavior byte-identical --
the engine is shared with the operator's /teams-assist; the pin is an additive argument.

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


def _flag_value(flag: str) -> str | None:
    """Value of `--flag VALUE` from argv, or None when the flag is absent. A flag present
    with no usable value is a pin the caller INTENDED and we cannot honor -> loud exit,
    never a silent fall-through to the identity-blind bare path."""
    if flag not in sys.argv:
        return None
    i = sys.argv.index(flag)
    if i + 1 >= len(sys.argv) or sys.argv[i + 1].startswith("--"):
        print(f"[TEAMS-IDENTITY-FAIL] {flag} requires a value", flush=True)
        print(f"[teams-watch] FATAL: {flag} requires a value", file=sys.stderr, flush=True)
        sys.exit(2)
    return sys.argv[i + 1]


PIN_SERVER = _flag_value("--server")
PIN_IDENTITY = _flag_value("--identity")


def now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _pin_fail(reason: str) -> None:
    """Die LOUDLY on a pin that cannot be satisfied. Stdout line so the Monitor pings the
    agent before the process exits; stderr for the human trace. Exit 2, never a fallback
    (OPAL_ANALYST PRD 4.1: polling as the wrong identity is the failure this exists to stop)."""
    print(f"[TEAMS-IDENTITY-FAIL] {reason}", flush=True)
    print(f"[teams-watch] FATAL: {reason}", file=sys.stderr, flush=True)
    sys.exit(2)


def _read_pinned_token() -> str | None:
    """Token selection under --server/--identity: filter the opalinvest.dev mcpOAuth records
    to the pinned server/identity BEFORE any expiry sort. Exactly one valid match is the only
    success; zero matches and ambiguous multi-matches die loudly.

    EXPIRED-ONLY IS THE ONE NON-FATAL CASE (OPAL_ANALYST.TO6, BG source-confirmed 20260811):
    a lapsed record is SELF-HEALING -- Claude Code re-mints it on the next MCP call -- so the
    pinned path returns None and the caller quiet-retries, exactly as the BARE path has always
    done (:119-121) and as the 401 handler does mid-poll. Exiting on it converted a transient
    idle lapse into an hourly process death plus a deaf window until someone re-armed.

    THE PIN SURVIVES THE RETRY BY CONSTRUCTION, and that is a property of this function's
    SHAPE, not of caller discipline: every call re-reads CREDS and re-derives `recs` from
    scratch, so the --server/--identity filters above are re-applied on every cycle; no token
    is cached across calls; and read_token() returns THIS function's result directly, with no
    fallback branch to the identity-blind bare selection. A None here can never widen the
    record set or select another identity -- it can only mean "poll as nobody this cycle."
    Do not add caching or a fallback: that is precisely the P0 that TO-1 closed."""
    pin = f"--server={PIN_SERVER} --identity={PIN_IDENTITY}"
    try:
        d = json.load(open(CREDS, encoding="utf-8"))
    except Exception as exc:  # a broken creds file yields no matching token -> same loud path
        _pin_fail(f"credentials-unreadable: {type(exc).__name__} ({pin})")
    recs = [v for v in d.get("mcpOAuth", {}).values() if "opalinvest.dev" in v.get("serverUrl", "")]
    if PIN_SERVER:
        recs = [r for r in recs if PIN_SERVER.lower() in str(r.get("serverName", "")).lower()]
    if PIN_IDENTITY:
        recs = [r for r in recs if PIN_IDENTITY.lower() in str(self_id(r.get("accessToken")) or "").lower()]
    if not recs:
        _pin_fail(f"no-token-for-identity: no mcpOAuth record matches the pin ({pin})")
    live = [r for r in recs if r.get("expiresAt", 0) / 1000 > time.time()]
    if not live:
        # QUIET RETRY, holding the pin. NOT _pin_fail: see the docstring. Deliberately no stdout
        # line -- stdout is the Monitor's agent-ping channel, and a self-healing lapse is not an
        # event to wake anyone for. The caller logs the lapse to stderr once and backs off.
        return None
    if len(live) > 1:
        names = ", ".join(sorted(str(r.get("serverName")) for r in live))
        _pin_fail(f"ambiguous-token-match: {len(live)} valid records match the pin ({names}) ({pin})")
    return live[0]["accessToken"]


def read_token() -> str | None:
    """The freshest non-expired gateway access token for the opalinvest.dev MCP server.
    Pinned (--server/--identity): identity-filtered selection via _read_pinned_token(), which
    returns None on a merely-expired pinned record (quiet retry, pin held) and exits non-zero on
    any pin it cannot satisfy -- never a fallback. Bare: legacy selection, unchanged."""
    if PIN_SERVER or PIN_IDENTITY:
        return _read_pinned_token()
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

    pin_note = f" pin(server={PIN_SERVER}, identity={PIN_IDENTITY})" if (PIN_SERVER or PIN_IDENTITY) else ""
    print(f"[teams-watch] armed interval={INTERVAL}s cursor={cursor} (incoming-only){pin_note}", file=sys.stderr, flush=True)
    selected_logged = False
    # Pin-scoped expiry backoff (TO6 req 1). Everything below is inert when bare: PINNED is False,
    # so lapse_cycles never leaves 0 and the sleep stays INTERVAL exactly as before (req 4).
    PINNED = bool(PIN_SERVER or PIN_IDENTITY)
    lapse_cycles = 0            # consecutive pinned cycles with no LIVE token; 0 == healthy
    LAPSE_BACKOFF_CAP = 6       # multiples of INTERVAL -- bounded, so recovery is never far away
    LAPSE_RENOTE_EVERY = 30     # a long lapse stays legible instead of looking like health (req 3)
    while True:
        tok = read_token()
        if tok:
            me = self_id(tok)
            if not selected_logged or lapse_cycles:
                # Evidence line: which identity this process is polling as. RE-EMITTED after a
                # lapse, because TO6 C2 asks who polled after the retry -- and "polling resumed"
                # cannot answer that. Without this, a recovery is invisible in the trace and the
                # only surviving evidence would be that the process stayed up, which is precisely
                # the failure mode C2 exists to catch.
                what = "re-selected after lapse" if lapse_cycles else "token selected"
                print(f"[teams-watch] {what}: identity={me}", file=sys.stderr, flush=True)
                selected_logged = True
            lapse_cycles = 0
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
        elif PINNED:
            # Pinned record exists but is expired -> hold the pin and wait it out. Stderr only:
            # stdout would ping the agent for a self-healing no-op.
            lapse_cycles += 1
            if lapse_cycles == 1 or lapse_cycles % LAPSE_RENOTE_EVERY == 0:
                print(f"[teams-watch] pinned token expired -- quiet retry, pin HELD "
                      f"(cycle {lapse_cycles}, identity={PIN_IDENTITY})", file=sys.stderr, flush=True)
        if ONCE:
            return
        # Backoff applies ONLY while a pinned token is lapsed; every other path sleeps INTERVAL.
        sleep_for = INTERVAL * min(2 ** (lapse_cycles - 1), LAPSE_BACKOFF_CAP) if lapse_cycles else INTERVAL
        time.sleep(sleep_for)


if __name__ == "__main__":
    main()
