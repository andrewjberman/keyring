#!/usr/bin/env python3
"""claude-usage-statusline.py -- Claude Code status-line command that records the signed-in account and the
5-hour and weekly usage to a local snapshot (NFRA_MCPORTAL MP-pd-5, U2; PRD v0.8 FWD-22).

Claude Code runs this once per status-line refresh with the status-line JSON payload on stdin. It writes
<config dir>/usage_snapshot.json and prints ONE short line:

    <signed-in Claude account> | 5h N% wk N% | <agent serial>

(Andrew-direct 2026-10-15, site Z session of 4.0.0_SA_CRO~Z: "1.) Currently logged in Claude account, then 2.) the usage
info which is there currently, then 3.) the serial number the agent session is registered with", on every box.)
The account is the oauthAccount emailAddress (the line now prints it, on Andrew's word); a missing account prints
"account ?". The serial is the first line of <repo>/org/mcp/sessions/<session_id>.serial (the file every seat writes
at startup, org/XXX.md step A.1), the repo found by walking up from the payload's workspace.project_dir; else
$OPAL_AGENT_SERIAL; else "serial ?". It never prints a token, a path or a traceback, and it exits 0 on every path.

Snapshot (schema 1): {"schema", "written_at", "rate_limits_claim", "reason", "five_hour", "seven_day",
"account", "account_claim"}. rate_limits_claim is "measured" when at least one of rate_limits.five_hour /
rate_limits.seven_day is present as an object with a numeric used_percentage, else "absent" with a reason.
An absent result never replaces an existing measured snapshot.

The account is read from ~/.claude.json only (oauthAccount: emailAddress, organizationType, organizationName).
~/.claude/.credentials.json is never opened, listed or tested for existence.

The rate_limits field layout is INFERRED from the Claude Code binary's strings (U1 finding); the reader is
written defensively and assumes no member exists.

Standard library only. ASCII only.
"""
from __future__ import annotations

import datetime
import io
import json
import math
import os
import sys
import tempfile

SNAPSHOT_NAME = "usage_snapshot.json"
ABSENT_REASON = ("rate_limits member not in the status-line payload "
                 "(present only for a subscription login after the first API response)")
WINDOWS = ("five_hour", "seven_day")
SERIAL_MAX = 64


def _usable(member):
    """A window member is usable when it is an object with a finite numeric used_percentage (bool excluded)."""
    if not isinstance(member, dict):
        return False
    used = member.get("used_percentage")
    if isinstance(used, bool) or not isinstance(used, (int, float)):
        return False
    return math.isfinite(used)


def _window(member):
    used = member["used_percentage"]
    remaining = 100 - used
    if remaining < 0:
        remaining = 0
    return {"used_percentage": used, "remaining_percentage": remaining,
            "resets_at": member.get("resets_at")}


def build_rate_limits(payload):
    """Return (claim, reason, five_hour, seven_day) from the payload's rate_limits member."""
    rate_limits = payload.get("rate_limits") if isinstance(payload, dict) else None
    if not isinstance(rate_limits, dict):
        rate_limits = {}
    present = {name: rate_limits.get(name) for name in WINDOWS if _usable(rate_limits.get(name))}
    if not present:
        return "absent", ABSENT_REASON, None, None
    five = _window(present["five_hour"]) if "five_hour" in present else None
    seven = _window(present["seven_day"]) if "seven_day" in present else None
    missing = [name for name in WINDOWS if name not in present]
    reason = None
    if missing:
        reason = "%s missing from rate_limits" % " and ".join(missing)
    return "measured", reason, five, seven


def read_account(home):
    """Return (account, account_claim) from home/.claude.json oauthAccount, the three named keys only."""
    try:
        with open(os.path.join(home, ".claude.json"), encoding="utf-8") as fh:
            data = json.load(fh)
        oauth = data.get("oauthAccount") if isinstance(data, dict) else None
        if not isinstance(oauth, dict):
            return None, "absent"
        wanted = (("emailAddress", "email"), ("organizationType", "plan"), ("organizationName", "organization"))
        if not all(key in oauth for key, _ in wanted):
            return None, "absent"
        return {out: oauth[key] for key, out in wanted}, "measured"
    except Exception:
        return None, "absent"


def _existing_is_measured(path):
    try:
        with open(path, encoding="utf-8") as fh:
            prior = json.load(fh)
        return isinstance(prior, dict) and prior.get("rate_limits_claim") == "measured"
    except Exception:
        return False


def write_snapshot(config_dir, snapshot):
    """Atomic write: temp file in the same directory, then os.replace over the snapshot."""
    path = os.path.join(config_dir, SNAPSHOT_NAME)
    fd, tmp = tempfile.mkstemp(dir=config_dir, prefix=".usage_snapshot.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(snapshot, fh, indent=2, sort_keys=False)
            fh.write("\n")
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            try:
                os.unlink(tmp)
            except OSError:
                pass


def format_usage(claim, five, seven):
    if claim != "measured":
        return "usage n/a"

    def pct(window):
        if window is None:
            return "--"
        return "%d%%" % int(math.floor(window["used_percentage"] + 0.5))

    return "5h %s wk %s" % (pct(five), pct(seven))


def _clean(text):
    """One printable ASCII token, capped; anything else is treated as absent."""
    if not isinstance(text, str):
        return None
    text = text.strip()
    if not text or len(text) > SERIAL_MAX or any(ord(ch) < 33 or ord(ch) > 126 for ch in text):
        return None
    return text


def read_serial(payload, environ):
    """The agent serial this session registered: <repo>/org/mcp/sessions/<session_id>.serial, the repo found by walking
    up from workspace.project_dir (then current_dir, then cwd); else OPAL_AGENT_SERIAL; else None."""
    sid = _clean(payload.get("session_id")) if isinstance(payload, dict) else None
    if sid and all(ch.isalnum() or ch in "-_" for ch in sid):
        workspace = payload.get("workspace") if isinstance(payload.get("workspace"), dict) else {}
        for start in (workspace.get("project_dir"), workspace.get("current_dir"), payload.get("cwd")):
            if not isinstance(start, str) or not start:
                continue
            d = os.path.abspath(start)
            while True:
                candidate = os.path.join(d, "org", "mcp", "sessions", sid + ".serial")
                if os.path.isfile(candidate):
                    try:
                        with open(candidate, encoding="utf-8") as fh:
                            serial = _clean(fh.readline())
                        if serial:
                            return serial
                    except Exception:
                        pass
                    break
                parent = os.path.dirname(d)
                if parent == d:
                    break
                d = parent
    return _clean(environ.get("OPAL_AGENT_SERIAL", ""))


def format_line(account, claim, five, seven, serial):
    email = _clean(account.get("email")) if isinstance(account, dict) else None
    return "%s | %s | %s" % (email or "account ?", format_usage(claim, five, seven), serial or "serial ?")


def run(stdin_text, config_dir, home, out, environ=None):
    payload = json.loads(stdin_text)
    if not os.path.isdir(config_dir):
        return
    claim, reason, five, seven = build_rate_limits(payload)
    account, account_claim = read_account(home)
    snapshot_path = os.path.join(config_dir, SNAPSHOT_NAME)
    if claim == "absent" and _existing_is_measured(snapshot_path):
        pass
    else:
        snapshot = {
            "schema": 1,
            "written_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "rate_limits_claim": claim,
            "reason": reason,
            "five_hour": five,
            "seven_day": seven,
            "account": account,
            "account_claim": account_claim,
        }
        write_snapshot(config_dir, snapshot)
    serial = read_serial(payload, os.environ if environ is None else environ)
    out.write(format_line(account, claim, five, seven, serial) + "\n")


def main(stdin_text=None, config_dir=None, home=None, out=None, environ=None):
    """Return 0 always. Injected arguments exist for the tests; the status line passes none."""
    try:
        if stdin_text is None:
            stdin_text = sys.stdin.buffer.read().decode("utf-8")
        if home is None:
            home = os.path.expanduser("~")
        if config_dir is None:
            config_dir = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.join(home, ".claude")
        if out is None:
            out = sys.stdout
        # Buffer the line so a failure anywhere prints nothing.
        buf = io.StringIO()
        run(stdin_text, config_dir, home, buf, environ)
        out.write(buf.getvalue())
        out.flush()
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
