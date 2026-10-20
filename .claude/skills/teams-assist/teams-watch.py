# ============================================================================================
# LIVE PRODUCTION -- IMPORTED at every fire of the Windows Scheduled Task OPAL_D7_ticket_intake, EVERY 5 MINUTES,
# FROM THIS WORKING TREE. SAVING THIS FILE IS DEPLOYING IT: there is no build, no commit gate and
# no deploy step between this text and the client-facing ticket buzz, and the fuse is <= 5 min.
# ANY edit -- including a comment, a docstring or a typo fix -- is bound by bar A5-A7 (CTO~Z
# ruling 3a @123071c5cd): exercise it in the SAME CONTINUOUS ACT, in THIS tree (not a scratch
# copy), scored on OUTPUT. If you cannot finish the exercise inside the window, REVERT FIRST.
# ============================================================================================
# WHOSE FILE THIS IS: the OPERATOR's. It reads the operator's own Claude credential store, is imported by the D7
# ticket-intake runner integrations/ticketing/intake/runner.py, and is the engine of the operator's /teams-assist
# catch-up. It is NOT the Opal Analyst's: the Analyst has its OWN watch at
# opal_ai/opal/agent/teams_watch/teams-watch.py.

#!/usr/bin/env python3
"""teams-watch.py -- the /teams-assist monitor ENGINE (like org/mcp/inbox-watch.sh, but for Teams).

Run under the Monitor tool. Every INTERVAL seconds: polls the Opal M365 gateway's
`poll_addressed_teams_messages` via a single stateless MCP `tools/call` to /mcp/ (the
ALB-bypassed, gateway-Bearer-gated path), then prints ONE `[TEAMS] ...` line to STDOUT per NEW
addressed message -- so the Monitor wakes the agent ONLY when a real message lands (event-driven,
not an LLM self-poll).

MESSAGE-GRAIN INTAKE (P1 fix, CTO~Z ruling msg 2571 adopting BG's spec msg 2567, 2026-08-20 --
an Andrew message was LOST to the old shape that day):
`poll_addressed_teams_messages` is a CHAT-grain instrument -- its contract is latest-per-chat,
so reading its payload as the message stream silently drops every message but the newest per
chat per poll window, at ANY interval. Therefore:
  1. The poll is the CHANGE SIGNAL ONLY. Its result contributes touched chat ids (+ chat_type),
     never the message payload.
  2. The INTAKE is `read_chat_messages` per touched chat (bounded top): every message STRICTLY
     newer than the cursor is emitted, oldest-first.
  3. The cursor advances on MESSAGE timestamp -- the max PROCESSED (emitted or
     deliberately-skipped-outgoing) message's own createdDateTime -- never on poll time and
     never on the gateway poll's cursor. A crash between read and emit re-delivers rather than
     drops (duplicate-on-retry is the safe direction; the serve loop tolerates a re-ack).
  4. Frame discipline: when >1 message is emitted for one chat in one cycle, each [TEAMS] line
     carries its per-chat denominator ("2 of 2 since cursor") -- the output carries its own
     frame. A read page FULL to the bound, or a failed chat read, is reported loudly (the
     cursor is HELD on a failed read so nothing is skipped past).

Auth: PASSIVE token reader. Reads the gateway access token from Claude Code's
~/.claude/.credentials.json (mcpOAuth.m365.accessToken) on each poll; Claude Code owns the refresh
(rotating tokens), so this never refreshes itself -> no refresh-token fight. On a 401 (token lapsed
while the session was idle) it stays quiet and retries; the next agent MCP call re-freshens it.
Session-scoped: it dies with the Monitor / session.

CORRECTED 2026-08-27 -- this line read "Session-scoped, EXACTLY LIKE INBOX-WATCH.SH: it dies with
the Monitor / session." That comparison was true when written and INVERTED SILENTLY on 2026-07-14,
when inbox-watch.sh gained a PARENT-LIVENESS SELF-EXIT (inbox-watch.sh:113 opens it, inbox-watch.sh:161 runs
kill -0 "$WATCH_PARENT" then exits) and this engine did not. So the sentence had come to name the
one watcher that DOES self-exit as the model for the one that CANNOT.
A COMPARATIVE CLAIM GOES STALE WHEN ITS REFERENT MOVES, AND NOTHING TOUCHES THE FILE THAT CARRIES
IT. Measured at source 2026-08-27, and stated so that WRITING IT DOWN CANNOT FALSIFY IT:
  - `ppid` / `getppid` occurrences IN CODE: ZERO. There is no parent-liveness check of any kind.
    READ THE HITS, DO NOT COUNT THEM: a whole-file grep for those tokens now returns NONZERO
    because THIS DOCSTRING CONTAINS THEM. Every hit above the `import` block is prose. Positive
    control that the search reaches real code: the two `os.environ.get("TMPDIR", ...)` call sites
    that build CURSOR_FILE and CHANNEL_CURSOR_FILE.
  - The main loop is the module's single `while True:`; every `sys.exit(2)` is a STARTUP token/pin
    failure and sits BEFORE it. There is no exit path inside the loop. This process dies only if
    something else reaps it.

SAME-FILE CITATIONS HERE ARE BY ANCHOR, NEVER BY LINE NUMBER, AND THAT IS DELIBERATE. The first
version of this docstring cited lines 98, 101, 406, 437, 477 and 544; adding these 37 lines shifted every
one of them by +36 and the citations were wrong THE MOMENT THEY LANDED. A LINE NUMBER POINTING INTO
THE FILE THAT CARRIES IT IS SELF-INVALIDATING -- the edit that records it moves what it records.
Grep the anchor instead.

WHY THAT MATTERS MORE HERE THAN FOR inbox-watch.sh, which is the part not to skim: an orphaned
inbox watcher `mv`s a file to read/ -- visible, and the message still exists. An orphaned
teams-watch would hold a live pinned token and ADVANCE THE CURSOR (grep `open(CURSOR_FILE, "w"`
for DMs and `open(CHANNEL_CURSOR_FILE, "w"` for channels -- both INSIDE the loop, after the emits)
while echoing into a dead pipe. A CURSOR ADVANCE
IS NOT RECOVERABLE BY INSPECTION: the next legitimate session starts PAST those messages and they
are never re-emitted. That is silent LOSS, not a duplicate, and it would cover DMs and the
client-facing channel alike. It compounds with the two-cursor-home divergence (the CURSOR_FILE and
CHANNEL_CURSOR_FILE assignments BOTH build from TMPDIR): an orphan can advance one home while a
live session reads the other.

NOT ESTABLISHED, AND DELIBERATELY NOT CLAIMED: nobody has measured that teams-watch children
actually survive session end. Evidence against -- a 2026-08-25 launch found ZERO straggling
teams-watch processes despite prior sessions arming them. Evidence for risk -- by construction this
process cannot self-exit, so its survival depends ENTIRELY on whether the harness reaps the child,
and that is documented as VARIABLE (2026-07-10: wrapper reaped, inbox-watch child survived;
2026-08-20: TaskStop reaped both). The honest statement is the asymmetry, not an incident:
INBOX-WATCH.SH NO LONGER DEPENDS ON THAT VARIABILITY. THIS ENGINE STILL DOES, ENTIRELY.

Two OPEN items, both owned by 0.5.0_AE_OpalETL~Z, neither implemented here and neither a gate:
  (1) port the parent-liveness self-exit (with inbox-watch.sh:139's fail-open when PPID <= 1 --
      that guard is correct and must travel with it, or healthy watchers suicide under MSYS);
  (2) there is no arm-banner equivalent to inbox-watch.sh's STREAM-mode banner, so a seat CANNOT READ its own
      protection state here -- which is precisely what org/XXX.md now instructs agents to do.
Found by 0.0.3_BG_BBGTerminal (msg 9123) applying the @073b1679e2 law edit to its other watcher;
verified at source by 0.0.0_AB_MSTR~Z before this edit. Doc layer corrected; ENGINE UNCHANGED.

READ-ONLY: it only ever READS your own DMs/group chats -- and, with --channels, the CONFIGURED
Team channels -- via the per-user gateway. It never posts.
STDOUT = the new-message signal (one line each). STDERR = status/diagnostics (no agent ping).

CHANNEL WATCH (P1, CTO~Z ruling msg 2761/2888; BG source-confirmed the blindness in msg 2752 --
this engine had ZERO channel code while the estate's client-ticket buzzes post to a CHANNEL, so a
correct buzz woke nobody and every liveness probe read healthy). `--channels <config.json>` arms
it. Shape, and every clause is the S1 discipline re-aimed at a second surface:
  1. NO CHANGE SIGNAL EXISTS FOR CHANNELS -- poll_addressed_teams_messages is chats-only by its own
     contract -- so the channel leg is a DIRECT BOUNDED READ of each configured channel per cycle.
     That is honest about its own domain rather than pretending a poll covers it.
  2. Every message STRICTLY newer than that channel's cursor emits as its own [TEAMS-CHANNEL] line,
     oldest-first, with the "(i of k since cursor)" frame when a cycle carries more than one.
  3. PER-CHANNEL CURSOR IN ITS OWN FILE, never shared with the chat cursor: one shared cursor would
     let either surface's advance eat the other's window -- the S1 loss class rebuilt by accident.
     Cursor on MESSAGE timestamp, written AFTER the emits; a failed read HOLDS ONLY THAT CHANNEL's
     cursor (channels are independent keys, so one bad read cannot skip another channel's mail).
  4. Config is IDS, NEVER NAMES (a rename cannot break a watch), refuse-if-unset when the flag is
     present. FLAG ABSENT = zero channel code paths active and the bare engine byte-identical --
     which is load-bearing beyond tidiness: the D7 intake runner imports this module at every
     scheduled fire, so the import-time contract IS a production contract.
  5. DELIBERATELY NO SELF-IDENTITY FILTER ON THE CHANNEL PATH. The ticket buzz is posted AS the very
     identity this watcher pins, and that buzz is THE primary signal -- filtering own-authored posts
     would recreate the exact deafness this leg exists to close. Own-reply echoes are the accepted,
     bounded cost; the emit line carries from_name and the serve loop no-ops on them.

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
import re
import sys
import time
import urllib.error
import urllib.request

GATEWAY = "https://mcp.opalinvest.dev/mcp/"
CREDS = os.path.expanduser("~/.claude/.credentials.json")
CURSOR_FILE = os.path.join(os.environ.get("TMPDIR", "/tmp"), "teams-watch.cursor")
# SEPARATE FILE, deliberately (see the CHANNEL WATCH note): a shared cursor would let one
# surface's advance eat the other's window. JSON {channel_id: max_processed_message_ts}.
CHANNEL_CURSOR_FILE = os.path.join(os.environ.get("TMPDIR", "/tmp"), "teams-watch-channels.cursor")
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


def _channels_flag() -> str | None:
    """argv-only capture of `--channels <path>`; NO file IO at import time (the D7 intake runner
    imports this module at every scheduled fire, so import-time work is production work). A flag
    present with no value is a watch the caller INTENDED and we cannot honor -> loud exit, never a
    silent fall-through to an unwatched channel set. Separate from _flag_value only so the failure
    text names CHANNELS rather than IDENTITY; that function stays byte-unchanged."""
    if "--channels" not in sys.argv:
        return None
    i = sys.argv.index("--channels")
    if i + 1 >= len(sys.argv) or sys.argv[i + 1].startswith("--"):
        print("[TEAMS-CHANNEL-FAIL] --channels requires a config path", flush=True)
        print("[teams-watch] FATAL: --channels requires a config path", file=sys.stderr, flush=True)
        sys.exit(2)
    return sys.argv[i + 1]


CHANNELS_FLAG = _channels_flag()


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
    try:
        res = _gateway_call(token, "whoami", {}) if token else None
    except Exception:  # best-effort per the docstring: a transient TCP reset (URLError) must not kill the monitor
        res = None
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
    """CHANGE SIGNAL ONLY (msg-2571 ruling 1): the result's contract is latest-per-chat, so the
    caller takes touched chat ids from it and NEVER the message payload -- see the intake below."""
    return _gateway_call(token, "poll_addressed_teams_messages", {"since_iso": since})


READ_TOP = 25  # bounded per-chat intake read (the gateway tool's own default page)


def read_chat(token: str, chat_id: str) -> dict | None:
    """THE INTAKE (msg-2571 ruling 2): one bounded message-grain read of a touched chat. Returns
    the gateway's raw Graph page {"value": [...newest-first...]} or an error-shaped dict/None."""
    return _gateway_call(token, "read_chat_messages", {"chat_id": chat_id, "top": READ_TOP})


def _parse_ts(ts: str | None) -> datetime.datetime | None:
    """Graph createdDateTime -> aware datetime; None when unparseable."""
    if not ts:
        return None
    t = str(ts).strip()
    if t.endswith("Z"):
        t = t[:-1] + "+00:00"
    try:
        d = datetime.datetime.fromisoformat(t)
    except ValueError:
        return None
    return d if d.tzinfo else d.replace(tzinfo=datetime.timezone.utc)


def _newer(ts: str | None, cursor: str) -> bool:
    """STRICT parsed compare -- never lexical: the seed cursor is second-grain while Graph carries
    milliseconds, and '...12.095Z' < '...12Z' lexically. An unparseable side reads NEWER (fail
    toward a duplicate emit, never toward a silent drop)."""
    a, b = _parse_ts(ts), _parse_ts(cursor)
    if a is None or b is None:
        return True
    return a > b


def _advance(max_ts: str, ts: str | None) -> str:
    """The newer of two timestamps by PARSED compare. An unparseable candidate never becomes the
    cursor (a corrupt cursor would re-emit forever), unlike _newer's emit-side fail-open."""
    p = _parse_ts(ts)
    if p is None:
        return max_ts
    q = _parse_ts(max_ts)
    return str(ts) if (q is None or p > q) else max_ts


PREVIEW_CAP = 400
ATTACHMENT_ONLY_MARKER = "[attachment-only message]"


def _strip_html(raw: str | None) -> str:
    """Tags out, whitespace collapsed -- the gateway's own preview rule, kept byte-for-byte for a body with text."""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", raw or "")).strip()


def _forwarded_text(att: dict) -> str:
    """The text of a forwardedMessageReference attachment, or "" when it cannot be read. MEASURED 2026-10-16 on a real
    Alyssa 1:1 message (0.0.3_BG_BBGTerminal msg 35248, structure only): attachments[i].contentType is
    "forwardedMessageReference", contentUrl is null, and .content is a JSON STRING whose originalMessageContent holds the
    forwarded text as HTML. A malformed or unexpected shape yields "" so the caller falls through, never raises."""
    c = att.get("content")
    if isinstance(c, str):
        try:
            c = json.loads(c)
        except ValueError:
            return ""
    if not isinstance(c, dict):
        return ""
    for k in ("originalMessageContent", "messagePreview"):
        v = c.get(k)
        if isinstance(v, str) and _strip_html(v):
            return _strip_html(v)
    return ""


def message_preview(m: dict) -> str:
    """A preview that is NEVER blank (CTO~Z ruling 35245, row from 0.0.3_BG_BBGTerminal msg 35243). A message that is only an
    attachment or a forward has a body of attachment TAGS and no text, which the tag strip turned into "" -- a request
    with a deadline read as "Alyssa sent something". Order: body text; then forwarded-message text; then attachment names;
    then the literal ATTACHMENT_ONLY_MARKER. A message with body text is unchanged. A quote-reply (contentType
    "messageReference", same double-encoded shape, text at .content -> messagePreview; 0.0.3_BG_BBGTerminal msg 35249)
    with no text of the sender's own reads like a forward and is labelled "[quoted]"."""
    body = _strip_html((m.get("body") or {}).get("content"))
    if body:
        return body[:PREVIEW_CAP]
    atts = [a for a in (m.get("attachments") or []) if isinstance(a, dict)]
    fwd = [t for t in (_forwarded_text(a) for a in atts if a.get("contentType") == "forwardedMessageReference") if t]
    if fwd:
        return ("[forwarded] " + " | ".join(fwd))[:PREVIEW_CAP]
    quo = [t for t in (_forwarded_text(a) for a in atts if a.get("contentType") == "messageReference") if t]
    if quo:
        return ("[quoted] " + " | ".join(quo))[:PREVIEW_CAP]
    names = [str(a.get("name")).strip() for a in atts if str(a.get("name") or "").strip()]
    if names:
        return ("[attachment] " + ", ".join(names))[:PREVIEW_CAP]
    return ATTACHMENT_ONLY_MARKER


def fresh_messages(page: dict | None, chat_id: str, chat_type: str | None, cursor: str) -> list[dict] | None:
    """Normalize ONE chat's read page to the poll's flat message shape -- {chat_id, chat_type,
    from_name, preview, timestamp_utc} with the gateway's own HTML-strip + 400-cap -- filtered to
    messages STRICTLY newer than the cursor, oldest-first (ruling 2: ordering preserved for the
    ACK-FIRST serve loop). Returns None on an error/absent page: the chat was NOT read, and the
    caller must HOLD the cursor (retry-not-drop)."""
    if not isinstance(page, dict) or "value" not in page:
        return None
    out = []
    for m in page.get("value", []):
        ts = m.get("createdDateTime")
        if not _newer(ts, cursor):
            continue
        usr = ((m.get("from") or {}).get("user")) or {}
        out.append({
            "chat_id": chat_id,
            "chat_type": chat_type,
            "from_name": usr.get("displayName"),
            "preview": message_preview(m),
            "timestamp_utc": ts,
        })
    out.sort(key=lambda m: str(m.get("timestamp_utc") or ""))  # one Graph page = one ts format
    return out


def _channel_fail(reason: str) -> None:
    """Die LOUDLY on a channel config the caller intended and we cannot honor. Stdout so the
    Monitor pings the agent before exit; exit 2, never a silent unwatched set."""
    print(f"[TEAMS-CHANNEL-FAIL] {reason}", flush=True)
    print(f"[teams-watch] FATAL: {reason}", file=sys.stderr, flush=True)
    sys.exit(2)


def load_channels(path: str) -> list[dict]:
    """The watched-channel set: [{team_id, channel_id, label}]. IDS NEVER NAMES. refuse-if-unset --
    an unreadable file, a non-list, an empty list or a row missing either id is a REFUSAL, because
    a watcher that silently watches nothing is the deafness this leg exists to close."""
    try:
        doc = json.load(open(path, encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 -- loud named reason beats a stack trace here
        _channel_fail(f"channels config unreadable: {type(exc).__name__} ({path})")
    rows = doc.get("channels") if isinstance(doc, dict) else doc
    if not isinstance(rows, list) or not rows:
        _channel_fail(f"channels config carries no channel rows ({path})")
    for r in rows:
        if not (isinstance(r, dict) and r.get("team_id") and r.get("channel_id")):
            _channel_fail(f"channels config row missing team_id/channel_id: {r!r} ({path})")
    return rows


def load_channel_cursors() -> dict:
    """{channel_id: max_processed_ts}. Absent file = first arm (the caller seeds each watched
    channel at NOW, exactly as the chat cursor seeds -- no history backfill, no flood)."""
    try:
        d = json.load(open(CHANNEL_CURSOR_FILE, encoding="utf-8"))
        return d if isinstance(d, dict) else {}
    except Exception:  # noqa: BLE001 -- absent or corrupt reads as "nothing processed yet"
        return {}


def save_channel_cursors(cursors: dict) -> None:
    open(CHANNEL_CURSOR_FILE, "w", encoding="utf-8").write(json.dumps(cursors, sort_keys=True))


def read_channel(token: str, team_id: str, channel_id: str) -> dict | None:
    """THE CHANNEL INTAKE: one bounded message-grain read. No change-signal exists for channels,
    so this runs every cycle rather than on a poll hint."""
    return _gateway_call(token, "read_channel_messages",
                         {"team_id": team_id, "channel_id": channel_id, "top": READ_TOP})


def main() -> None:
    if os.path.exists(CURSOR_FILE):
        cursor = open(CURSOR_FILE, encoding="utf-8").read().strip() or now_iso()
    else:
        cursor = now_iso()
        open(CURSOR_FILE, "w", encoding="utf-8").write(cursor)

    # CHANNEL WATCH init -- entirely inert when --channels is absent (the import-time/bare contract
    # the D7 runner depends on). A newly watched channel SEEDS AT NOW, exactly as the chat cursor
    # does: arming a watch is not a request to replay history.
    channels = load_channels(CHANNELS_FLAG) if CHANNELS_FLAG else []
    chan_cursors = load_channel_cursors() if channels else {}
    if channels:
        seeded = [c["channel_id"] for c in channels if c["channel_id"] not in chan_cursors]
        for cid in seeded:
            chan_cursors[cid] = now_iso()
        if seeded:
            save_channel_cursors(chan_cursors)

    pin_note = f" pin(server={PIN_SERVER}, identity={PIN_IDENTITY})" if (PIN_SERVER or PIN_IDENTITY) else ""
    chan_note = (f" channels={len(channels)} watched ({', '.join(c.get('label') or c['channel_id'][:24] for c in channels)})"
                 if channels else "")
    print(f"[teams-watch] armed interval={INTERVAL}s cursor={cursor} (incoming-only){pin_note}{chan_note}", file=sys.stderr, flush=True)
    # ARM RECEIPT (Z6 R5): the banner above is stderr, which a Monitor does not deliver, so from
    # inside an armed session a healthy watcher and a dead one read identically. ONE stdout line,
    # emitted only here in main() -- never at import time (the D7 intake runner imports this module
    # every 5 minutes and its stdout must stay empty). It is a receipt, not a message event.
    print(f"[TEAMS-ARMED] pid={os.getpid()} identity={PIN_IDENTITY or 'BARE'} "
          f"channels={len(channels)} cursor={cursor}", flush=True)
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
                    # MESSAGE-GRAIN INTAKE (msg-2571): the poll payload contributes TOUCHED CHAT
                    # IDS only -- its latest-per-chat contract drops every earlier message in the
                    # window, which is the exact loss this intake closes (BG msg 2567, measured).
                    touched = {}
                    for m in res.get("new_messages", []):
                        cid = m.get("chat_id")
                        if cid and cid not in touched:
                            touched[cid] = m.get("chat_type")
                    max_seen = cursor
                    all_read = True
                    for cid, ctype in touched.items():
                        fresh = fresh_messages(read_chat(tok, cid), cid, ctype, cursor)
                        if fresh is None:
                            # this chat was NOT read: hold the cursor for the WHOLE cycle (the
                            # cursor is global, so advancing on a sibling chat's messages would
                            # skip past this one's forever). Duplicates on retry are the safe side.
                            all_read = False
                            print(f"[teams-watch] read failed for chat {cid} -- cursor HELD, "
                                  "retry next cycle", file=sys.stderr, flush=True)
                            continue
                        if len(fresh) >= READ_TOP:
                            # window FULL to the bound: messages since the cursor may exist BELOW
                            # the read page. A possible loss is never silent -- loud on stdout so
                            # the agent backfills with a manual read_chat_messages.
                            print(f"[TEAMS] note: chat {cid} read window FULL ({len(fresh)} of "
                                  f">={READ_TOP} since cursor) -- backfill via read_chat_messages",
                                  flush=True)
                        emit = []
                        for m2 in fresh:
                            # cursor advances over PROCESSED messages: emitted OR deliberately
                            # outgoing-skipped (else my own reply leaves the chat perma-touched);
                            # never past an unemitted incoming -- the write is after the emits.
                            max_seen = _advance(max_seen, m2.get("timestamp_utc"))
                            # INCOMING ONLY: skip my own outgoing messages (Andrew-direct 2026-06-26)
                            if not is_outgoing(m2, me, me_name):
                                emit.append(m2)
                        k = len(emit)
                        for i, m2 in enumerate(emit, 1):
                            frame = f" ({i} of {k} since cursor)" if k > 1 else ""
                            # one STDOUT line per new INCOMING message = one agent ping (work-intake signal)
                            print(f"[TEAMS] {m2.get('chat_type')} from {m2.get('from_name')}: "
                                  f"{m2.get('preview')} | chat_id={m2.get('chat_id')} ts={m2.get('timestamp_utc')}{frame}",
                                  flush=True)
                    # cursor advance: MESSAGE timestamp only (max processed), single write per
                    # cycle AFTER all emits, and only when every touched chat was actually read.
                    # The gateway poll's own cursor is deliberately ignored -- a poll-time cursor
                    # advancing past unemitted messages IS the loss vector (msg-2571 ruling 3).
                    if all_read and max_seen != cursor:
                        cursor = max_seen
                        open(CURSOR_FILE, "w", encoding="utf-8").write(cursor)
            except urllib.error.HTTPError as e:
                if e.code != 401:  # 401 = token lapsed; quiet retry (Claude Code refreshes on next use)
                    print(f"[teams-watch] HTTP {e.code}", file=sys.stderr, flush=True)
            except Exception as exc:  # noqa: BLE001 -- a monitor must never die on a transient error
                print(f"[teams-watch] {type(exc).__name__}: {exc}", file=sys.stderr, flush=True)
            # ---- CHANNEL INTAKE: its OWN try, deliberately AFTER the chat work. A channel-side
            # failure must never be able to take down the chat intake (the failure-isolation
            # discipline the D7 sweep ruling makes binding, applied to this engine's two duties).
            try:
                dirty = False
                for ch in channels:
                    cid, tid = ch["channel_id"], ch["team_id"]
                    ccur = chan_cursors.get(cid, "")
                    # fresh_messages is REUSED byte-unchanged (chat_id slot carries the channel id,
                    # chat_type "channel") -- same strict-newer, same parsed compare, same
                    # oldest-first ordering, so the two surfaces cannot drift apart in semantics.
                    fresh = fresh_messages(read_channel(tok, tid, cid), cid, "channel", ccur)
                    if fresh is None:
                        # HOLD ONLY THIS CHANNEL's cursor -- keys are independent, so a bad read
                        # here can never skip another channel's mail (the S1 global-hold, narrowed
                        # correctly because the state is per-key rather than shared).
                        print(f"[teams-watch] channel read failed for {ch.get('label') or cid} "
                              "-- that channel's cursor HELD, retry next cycle",
                              file=sys.stderr, flush=True)
                        continue
                    if len(fresh) >= READ_TOP:
                        print(f"[TEAMS-CHANNEL] note: {ch.get('label') or cid} read window FULL "
                              f"({len(fresh)} of >={READ_TOP} since cursor) -- backfill via "
                              "read_channel_messages", flush=True)
                    k = len(fresh)
                    for i, m2 in enumerate(fresh, 1):
                        frame = f" ({i} of {k} since cursor)" if k > 1 else ""
                        # NO is_outgoing filter here, by design: the ticket buzz is posted AS the
                        # pinned identity and IS the signal (see the CHANNEL WATCH note).
                        print(f"[TEAMS-CHANNEL] {ch.get('label') or 'channel'} from "
                              f"{m2.get('from_name')}: {m2.get('preview')} | channel_id={cid} "
                              f"ts={m2.get('timestamp_utc')}{frame}", flush=True)
                        chan_cursors[cid] = _advance(chan_cursors.get(cid, ""), m2.get("timestamp_utc"))
                        dirty = True
                if dirty:
                    save_channel_cursors(chan_cursors)   # AFTER the emits, same as the chat path
            except Exception as exc:  # noqa: BLE001 -- never let the channel leg kill the monitor
                print(f"[teams-watch] channel intake {type(exc).__name__}: {exc}",
                      file=sys.stderr, flush=True)
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
