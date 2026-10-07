#!/usr/bin/env python3
"""named_commit_check.py -- the ONE reading both deploy wrappers call (NFRA_CTLPLN round 4, cell CT-d-3).

    python .tools/named_commit_check.py check --commit <40-hex> [--device <name>] [--remote origin] [--record]

CONTRACT (PRD v0.12 ADDENDUM v0.9 (a)): a Dell deploys a commit it NAMES BY FULL HASH and HAS PUBLISHED to a branch
of the remote, even when that commit is not yet on the trunk (<remote>/CLOUD); the trunk merge follows and is never a
precondition. Never-widen halves still bind every served move; this tool grades the commit's relation to the trunk
only and widens nothing.

FIRST READ (what the wrappers did before this tool): neither .tools/safe-deploy.sh, .tools/safe_deploy_core.py,
.tools/halt-gate-check.sh nor .tools/safe-apply.sh refused, warned or proceeded on a commit's relation to the trunk --
no is-ancestor, merge-base, origin/CLOUD or fetch anywhere in them. So for a box whose role is not `execution` an
OFF-TRUNK commit prints UNCHANGED and is admitted: today's behaviour, kept.

RESULT LINE (one, on stdout):
  NAMED-COMMIT <ADMITTED|REFUSED|UNCHANGED> commit=<h> device=<d> role=<r> trunk=<ON-TRUNK|OFF-TRUNK|-> branch=<b|-> reason=<text>
rc 0 for ADMITTED and UNCHANGED, 1 for REFUSED, 2 for a usage error.

--record (an OFF-TRUNK ADMITTED result only): carry `named_commit=<h> trunk=OFF-TRUNK branch=<b> device=<d>` into the
deploy ledger entry the actor opened. deploy_ledger.py has no note verb, and is not edited here, so this tool
appends one line to the open sentinel's `log` array (which deploy_ledger.py re-renders into the entry on every
mutation) and the same line to the entry's `## Log` section, and sets a `named_commit` key on the sentinel. The
sentinel is chosen by DEPLOY_LEDGER_SLUG, else by author == OPAL_AGENT_SERIAL among OPEN sentinels (and device when the
sentinel names one). No exactly-one match -> REFUSED: the actor opens the entry first (NEVER-2 already requires it).

Environment: AGENTBUS_DEVICE (the box's own name, environment only), OPAL_DEVICE_REGISTER (register override),
NAMED_COMMIT_LEDGER_ROOT (workspace root holding org/critical_paths; default: this file's checkout).
Git Bash 3.x callers, ASCII only.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
FULL_HASH = re.compile(r"^[0-9a-f]{40}$")
GIT_TIMEOUT = 120


def _git(repo, *args):
    env = dict(os.environ, GIT_TERMINAL_PROMPT="0")
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=GIT_TIMEOUT, env=env)


def _line(verdict, commit, device, role, trunk, branch, reason):
    return ("NAMED-COMMIT %s commit=%s device=%s role=%s trunk=%s branch=%s reason=%s"
            % (verdict, commit or "-", device or "-", role or "-", trunk or "-", branch or "-", reason))


def _register_role(device):
    """(canonical name, role) for a box name or alias, or (None, reason)."""
    override = os.environ.get("OPAL_DEVICE_REGISTER", "").strip()
    path = Path(override) if override else ROOT / "org" / "devices" / "DEVICES.json"
    try:
        reg = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return None, "device register unreadable at %s (%s)" % (path, exc)
    want = device.strip().lower()
    for d in reg.get("devices", []):
        if want in [d.get("name", "").lower()] + [a.lower() for a in d.get("aliases", [])]:
            return d["name"], d.get("role", "")
    return None, "device %s is not in the device register" % device


def _published_branch(repo, remote, commit, device):
    """The remote branch (short name below <remote>/) that contains the commit, or None. Excludes <remote>/HEAD."""
    r = _git(repo, "branch", "-r", "--contains", commit)
    if r.returncode != 0:
        return None, "git branch -r --contains rc=%s: %s" % (r.returncode, r.stderr.strip()[:160])
    found = []
    for raw in r.stdout.splitlines():
        ref = raw.strip()
        if not ref or " -> " in ref or not ref.startswith(remote + "/"):
            continue
        name = ref[len(remote) + 1:]
        if name != "HEAD":
            found.append(name)
    if not found:
        return None, ""
    mine = [b for b in found if ("/%s/" % device) in ("/" + b + "/")]
    return (mine or found)[0], ""


def _record(commit, branch, device, ledger_root):
    """Carry the named commit into the actor's open ledger entry. Returns (ok, message)."""
    state_dir = Path(ledger_root) / "org" / "critical_paths" / ".open_deploys"
    slug = os.environ.get("DEPLOY_LEDGER_SLUG", "").strip()
    actor = os.environ.get("OPAL_AGENT_SERIAL", "").strip()
    if not slug and not actor:
        return False, "no open ledger entry can be chosen: set DEPLOY_LEDGER_SLUG or OPAL_AGENT_SERIAL"
    hits = []
    for sp in sorted(state_dir.glob("*.json")) if state_dir.is_dir() else []:
        try:
            st = json.loads(sp.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if st.get("status") != "OPEN":
            continue
        if slug:
            if st.get("slug") != slug:
                continue
        elif st.get("author") != actor:
            continue
        if st.get("device") and st.get("device") != device:
            continue
        hits.append((sp, st))
    if len(hits) != 1:
        return False, ("an off-trunk deploy needs exactly ONE open ledger sentinel for this actor/device under %s "
                       "(found %d); open the entry first (NEVER-2), or name it with DEPLOY_LEDGER_SLUG"
                       % (state_dir, len(hits)))
    sp, st = hits[0]
    note = "named_commit=%s trunk=OFF-TRUNK branch=%s device=%s" % (commit, branch, device)
    if any(("named_commit=%s" % commit) in str(e) for e in st.get("log", [])):
        return True, "ledger entry %s already carries %s" % (st.get("slug"), commit)
    ev = "%s NAMED-COMMIT %s" % (datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"), note)
    st["named_commit"] = {"commit": commit, "trunk": "OFF-TRUNK", "branch": branch, "device": device}
    st.setdefault("log", []).append(ev)
    sp.write_text(json.dumps(st, indent=2), encoding="utf-8")
    entry = Path(ledger_root) / st.get("entry_path", "")
    if st.get("entry_path") and entry.is_file():
        text = entry.read_text(encoding="utf-8")
        m = re.search(r"^## Log\s*$", text, re.M)
        if m:
            nxt = re.search(r"^## ", text[m.end():], re.M)
            cut = m.end() + nxt.start() if nxt else len(text)
            head, tail = text[:cut].rstrip("\n"), text[cut:]
            text = head + "\n- " + ev + "\n" + ("\n" + tail if tail else "")
        else:
            text = text.rstrip("\n") + "\n- " + ev + "\n"
        entry.write_text(text, encoding="utf-8", newline="\n")
    return True, "ledger entry %s carries %s" % (st.get("slug"), note)


def check(args):
    repo = Path(args.repo or os.getcwd())
    given = args.commit or ""
    device_in = (args.device or os.environ.get("AGENTBUS_DEVICE", "")).strip()

    if not FULL_HASH.match(given):
        return 1, _line("REFUSED", given, device_in, "", "", "",
                        "the commit must be a full 40-character lowercase hex hash; a short or symbolic name moves")
    r = _git(repo, "rev-parse", "--verify", given + "^{commit}")
    if r.returncode != 0 or r.stdout.strip() != given:
        return 1, _line("REFUSED", given, device_in, "", "", "", "the commit does not resolve in this repository")
    if not device_in:
        return 1, _line("REFUSED", given, "", "", "", "", "device unset: pass --device or set AGENTBUS_DEVICE")
    device, role = _register_role(device_in)
    if device is None:
        return 1, _line("REFUSED", given, device_in, "", "", "", role)

    remote = args.remote
    f = _git(repo, "fetch", "--prune", remote)
    if f.returncode != 0:
        return 1, _line("REFUSED", given, device, role, "", "",
                        "git fetch %s failed rc=%s: %s (a failed fetch is never read as off-trunk)"
                        % (remote, f.returncode, f.stderr.strip()[:160].replace("\n", " ")))
    a = _git(repo, "merge-base", "--is-ancestor", given, "%s/CLOUD" % remote)
    if a.returncode == 0:
        return 0, _line("ADMITTED", given, device, role, "ON-TRUNK", "", "ancestor of %s/CLOUD" % remote)
    if a.returncode != 1:
        return 1, _line("REFUSED", given, device, role, "", "",
                        "merge-base --is-ancestor against %s/CLOUD rc=%s: %s"
                        % (remote, a.returncode, a.stderr.strip()[:160].replace("\n", " ")))

    if role != "execution":
        return 0, _line("UNCHANGED", given, device, role, "OFF-TRUNK", "",
                        "role %s: the wrappers never refused an off-trunk commit and this check does not start" % role)
    branch, err = _published_branch(repo, remote, given, device)
    if branch is None:
        return 1, _line("REFUSED", given, device, role, "OFF-TRUNK", "",
                        err or "not published: no other box can read the deployed bytes")
    line = _line("ADMITTED", given, device, role, "OFF-TRUNK", branch, "published on %s/%s" % (remote, branch))
    if args.record:
        ledger_root = args.ledger_root or os.environ.get("NAMED_COMMIT_LEDGER_ROOT") or str(ROOT)
        ok, msg = _record(given, branch, device, ledger_root)
        if not ok:
            return 1, _line("REFUSED", given, device, role, "OFF-TRUNK", branch, msg)
        line += "\nNAMED-COMMIT-LEDGER " + msg
    return 0, line


def main(argv):
    ap = argparse.ArgumentParser(prog="named_commit_check")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("check")
    p.add_argument("--commit", required=True)
    p.add_argument("--device")
    p.add_argument("--remote", default="origin")
    p.add_argument("--repo", help="repository to read (default: the current directory)")
    p.add_argument("--record", action="store_true", help="on an OFF-TRUNK admission, write the open ledger entry")
    p.add_argument("--ledger-root", help="workspace root holding org/critical_paths (default: NAMED_COMMIT_LEDGER_ROOT or this checkout)")
    args = ap.parse_args(argv)
    try:
        rc, out = check(args)
    except (OSError, subprocess.SubprocessError) as exc:
        rc, out = 1, _line("REFUSED", args.commit, args.device, "", "", "", "check could not run: %s" % exc)
    print(out)
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
