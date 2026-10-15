#!/usr/bin/env python3
r"""FWD-27 laptop-side read (NFRA_CTLPLN TO CT-ai-4, round 19).

Runs .tools/ssh-tailnet-verify.py from this laptop for site Z (sitez), dell1 and dell2 as a READ:
`hostname` by key, plus the tool's own no-password password_arm probe. No password is ever sent, no
write happens on any box, nothing is run elevated.

The login for each box is the client's own default login, as read by `ssh -G <box>` (a config read; no
connection is made). The CVO regrade row 27 (2026-10-13) measured key login with no login given
(`ssh -o BatchMode=yes <addr> hostname`, rc 0) on three boxes, so that default is the login those boxes
accept. The tool still checks the printed hostname against the register, so a wrong login or a wrong
machine reads as not done, never as done.

Last line:
    FWD27-LAPTOP-SIDE boxes=<n> key_ok=<k> password_refused=<p> ok=<True|False>
ok is True when key_ok equals boxes. password_refused counts boxes whose password_arm reads REFUSED or
KBDINT-NO-PROMPT, as measured; it is reported and is not a pass condition.
Exit 0 when ok, 1 otherwise.
"""
from __future__ import annotations

import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
TOOL = ROOT / ".tools" / "ssh-tailnet-verify.py"
BOXES = ["sitez", "dell1", "dell2"]
TOOL_TIMEOUT_S = 240
REFUSED_ARMS = ("REFUSED", "KBDINT-NO-PROMPT")


def field(line, name):
    """The value of `name=<v>` in a BOX line (the verdict has no spaces), or None."""
    for part in line.split():
        if part.startswith(name + "="):
            return part[len(name) + 1:]
    return None


def default_login(box):
    """The login ssh would use for BOX with no -l, read from client config (ssh -G opens no connection)."""
    out = subprocess.run(["ssh", "-G", box], capture_output=True, text=True, timeout=30)
    for line in out.stdout.splitlines():
        if line.startswith("user "):
            return line[len("user "):].strip()
    return ""


def main():
    cmd = [sys.executable, str(TOOL), "--box", *BOXES, "--timeout", "5"]
    for box in BOXES:
        login = default_login(box)
        if login:
            cmd += ["--user-for", "%s=%s" % (box, login)]
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=TOOL_TIMEOUT_S)
    lines = (proc.stdout + proc.stderr).splitlines()
    for line in lines:
        print(line)
    key_ok = 0
    password_refused = 0
    for line in lines:
        if not line.startswith("BOX "):
            continue
        key = field(line, "key") or ""
        if key.split(":")[0] == "ANSWERED":
            key_ok += 1
        if (field(line, "password_arm") or "") in REFUSED_ARMS:
            password_refused += 1
    ok = key_ok == len(BOXES)
    print("FWD27-LAPTOP-SIDE boxes=%d key_ok=%d password_refused=%d ok=%s"
          % (len(BOXES), key_ok, password_refused, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
