"""one-writer-check.py -- pre-commit stage: an append-only file has ONE writer box (NFRA_CTLPLN FWD-8, C-ONE-WRITER).

Append-only files (surprise channels, audit logs) are kept per box: a box appends only to ITS OWN file,
`<stem>.<device>.<ext>`, where <device> is the box's name (or alias) in the device register org/devices/DEVICES.json. The
control-plane box (the laptop) keeps the unsuffixed file (1.0.0_SA_CTO msg 105634); existing `.Z` files read as sitez's
through the register alias.

Per staged ADDED or MODIFIED append-only path:
  suffix names ANOTHER box          -> BLOCK (exit 1): that file is that box's; write your own
  suffix names THIS box             -> OK
  unsuffixed, this box = control plane -> OK
  unsuffixed, any other box         -> WARN (until C-QUEUE lands; site Z writes the shared files today)
  this box unresolved               -> WARN once (the check cannot judge without AGENTBUS_DEVICE)
A MERGE commit (MERGE_HEAD present) is exempt: integrating another box's round carries that box's own files.

Input: STAGED (newline list, the precomp_v1 orchestrator's env) or `git diff --cached`. Pure decision: decide().
    python .tools/git-hooks/one-writer-check.py              # the hook stage
    python .tools/git-hooks/one-writer-check.py --self-test  # planted cases, both arms of every branch
"""
from __future__ import annotations

import importlib.util
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
APPEND_ONLY = (
    re.compile(r"^org/surprise_channel/[^/]+/(INVESTIGATION|REMEDIATION|ADJUDICATION)_v[^/]*$"),
    re.compile(r"^org/missions/D[^/]*/[^/]+/[^/]+/surprise-channel/(investigations|remediations|adjudications)/[^/]+$"),
    re.compile(r"(^|/)[^/]*-audit(\.[^/.]+)?\.(log|jsonl)$"),
)


def devices_module():
    spec = importlib.util.spec_from_file_location("opal_devices", os.path.join(ROOT, "lib", "devices.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def is_append_only(path: str) -> bool:
    return any(p.search(path) for p in APPEND_ONLY)


def suffix_box(path: str, resolve) -> str | None:
    """The register box a file's `<stem>.<x>.<ext>` suffix names, or None when unsuffixed."""
    parts = os.path.basename(path).split(".")
    return resolve(parts[-2]) if len(parts) >= 3 else None


def decide(path: str, me: str | None, control_plane: str, resolve) -> tuple:
    """('OK'|'WARN'|'BLOCK'|'SKIP', reason) for one staged path."""
    if not is_append_only(path):
        return "SKIP", ""
    owner = suffix_box(path, resolve)
    if me is None:
        return "WARN", "%s: this box is unresolved, so its writer cannot be checked" % path
    if owner is not None and owner != me:
        return "BLOCK", ("%s is %s's append file; this box is %s. Append to this box's own file (%s)"
                         % (path, owner, me, "the unsuffixed one" if me == control_plane else "<stem>.%s.<ext>" % me))
    if owner is None and me != control_plane:
        return "WARN", ("%s is the %s's (unsuffixed) file, written from %s; per-box file <stem>.%s.<ext> "
                        "(WARN until C-QUEUE)" % (path, control_plane, me, me))
    return "OK", ""


def staged_paths() -> list:
    env = os.environ.get("STAGED")
    if env is None:
        r = subprocess.run(["git", "-C", ROOT, "diff", "--cached", "--name-only", "--diff-filter=AM"], capture_output=True,
                           text=True, encoding="utf-8", errors="replace")
        env = r.stdout
    else:
        # The orchestrator's STAGED is unfiltered: keep only paths present in the index (drop deletions).
        r = subprocess.run(["git", "-C", ROOT, "diff", "--cached", "--name-only", "--diff-filter=D"], capture_output=True,
                           text=True, encoding="utf-8", errors="replace")
        gone = set(r.stdout.split())
        env = "\n".join(p for p in env.splitlines() if p.strip() and p.strip() not in gone)
    return [p.strip().replace("\\", "/") for p in env.splitlines() if p.strip()]


def merging() -> bool:
    r = subprocess.run(["git", "-C", ROOT, "rev-parse", "-q", "--verify", "MERGE_HEAD"], capture_output=True, text=True)
    return r.returncode == 0


def run() -> int:
    paths = [p for p in staged_paths() if is_append_only(p)]
    if not paths:
        return 0
    if merging():
        print("[one-writer] OK: merge commit -- %d append-only path(s) carried from the merged side, exempt" % len(paths))
        return 0
    dev = devices_module()
    try:
        reg = dev.load()
    except dev.RegisterError as exc:
        print("[one-writer] WARN: %s -- the check cannot run" % exc, file=sys.stderr)
        return 0
    me, basis = dev.this_device(reg)
    cp = next((d["name"] for d in reg["devices"] if d.get("role") == "control-plane"), None)
    blocks = 0
    warned_unresolved = False
    for p in paths:
        verdict, why = decide(p, me, cp, lambda x: dev.resolve(x, reg))
        if verdict == "BLOCK":
            blocks += 1
            print("[one-writer] BLOCKED: " + why, file=sys.stderr)
        elif verdict == "WARN" and (me is not None or not warned_unresolved):
            warned_unresolved = warned_unresolved or me is None
            print("[one-writer] WARN: " + (why if me is not None else "%s (%s)" % (why, basis)), file=sys.stderr)
    print("[one-writer] %s: %d append-only path(s) graded on box %s (%s), %d blocked"
          % ("BLOCKED" if blocks else "OK", len(paths), me or "UNRESOLVED", basis, blocks))
    return 1 if blocks else 0


def self_test() -> int:
    names = {"laptop": "laptop", "sitez": "sitez", "site-z": "sitez", "z": "sitez", "dell1": "dell1"}

    def res(x):
        return names.get((x or "").lower())

    ch = "org/missions/D0/NFRA/X/surprise-channel/investigations/"
    cases = [
        (ch + "INVESTIGATION_v1.sitez.md", "laptop", "BLOCK", "another box's suffix blocks"),
        (ch + "INVESTIGATION_v1.Z.md", "laptop", "BLOCK", "the .Z alias reads as sitez's"),
        (ch + "INVESTIGATION_v1.sitez.md", "sitez", "OK", "own suffix passes"),
        (ch + "INVESTIGATION_v1.Z.md", "sitez", "OK", "own alias suffix passes"),
        (ch + "INVESTIGATION_v1.md", "laptop", "OK", "control plane keeps the unsuffixed file"),
        (ch + "INVESTIGATION_v1.md", "dell1", "WARN", "unsuffixed off the control plane warns"),
        (ch + "INVESTIGATION_v1.laptop.md", "dell1", "BLOCK", "a dell writing the laptop's suffixed file blocks"),
        ("org/surprise_channel/P/INVESTIGATION_v2.dell1.md", "sitez", "BLOCK", "flat channel root graded too"),
        ("org/law-edit-audit.sitez.log", "laptop", "BLOCK", "audit log per box"),
        ("org/law-edit-audit.log", "laptop", "OK", "laptop's audit log"),
        ("org/mcp/agent-spawn-audit.log", "sitez", "WARN", "shared audit log written off the control plane"),
        (ch + "INVESTIGATION_v1.sitez.md", None, "WARN", "unresolved box warns, never blocks"),
        ("org/devices/DEVICES.json", "dell1", "SKIP", "not an append-only file"),
        (ch + "INVESTIGATION_v1.notabox.md", "laptop", "OK", "an unknown middle token is not a suffix"),
    ]
    fails = 0
    for path, me, want, label in cases:
        got, _ = decide(path, me, "laptop", res)
        ok = got == want
        fails += not ok
        print("  %s  %s (%s -> %s, want %s)" % ("PASS" if ok else "FAIL", label, me, got, want))
    print("one-writer-check --self-test: %d/%d PASS" % (len(cases) - fails, len(cases)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(self_test() if sys.argv[1:] == ["--self-test"] else run())
