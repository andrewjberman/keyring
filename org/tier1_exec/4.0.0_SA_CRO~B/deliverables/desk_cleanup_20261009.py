#!/usr/bin/env python3
"""desk_cleanup_20261009.py -- remove the laptop Desktop's stale worktree folders without touching what they link to.

Andrew-direct 2026-10-09 ~03:2xZ-03:3xZ, record ANDREW_DIRECT_20261009_033xZ_LAPTOP_DESKTOP_WORKTREE_CLEANUP.md (this folder):
"Have CVO work with you on this and be ginger about the dependencies ... the wk-tsc should not be touched for sure. also saving
the IRPT patch". One-shot tool, 4.0.0_SA_CRO~B; reviewed by 3.0.0_SA_CVO before --execute.

    python desk_cleanup_20261009.py            DRY RUN (default): print every target, every link inside it, and the baseline
    python desk_cleanup_20261009.py --execute  delete, then print the same baseline after

SAFETY, in order, per target:
  1. The target is a direct child of the Desktop, on the explicit list below, and never `wk-tsc` (refused by name).
  2. No running process has the target in its command line.
  3. Walk the target WITHOUT following links; every junction or symlink found is removed AS A LINK (os.rmdir/os.unlink on the
     link itself), and its target is checked to still exist right after.
  4. Re-walk: zero links must remain, or the target is skipped.
  5. A registered portal worktree is removed with `git worktree remove --force`; anything else with shutil.rmtree.
  6. The live ajb_workspace\\portal\\node_modules is measured (entries, files, bytes) before the first target and after the
     last; any difference fails the run loudly.
"""
import os
import shutil
import subprocess
import sys
import json

DESK = r"C:\Users\AndrewBerman\Desktop"
WS = os.path.join(DESK, "ajb_workspace")
PORTAL = os.path.join(WS, "portal")
LIVE_NM = os.path.join(PORTAL, "node_modules")
KEEP = {"wk-tsc"}
SHELLS = (["wk-advi-cotbkf-%d" % i for i in range(1, 17)] + ["wk-comm-%d" % i for i in range(1, 6)]
          + ["wk-ctlpln-%d" % i for i in range(37, 42)] + ["wk-irpt-p-61", "wk-irpt-p-85", "wk-irpt-p-86"]
          + ["wk-nfra-ctlpln-%d" % i for i in range(1, 4)] + ["wk-ycdgen-1", "wk-ycdgen-2", "wk-ycdgen-3"]
          + ["wk_irpt_bckend_93", "wk_mdpf_secclass_8"])
PORTAL_WT = ["portal-coo-d-p3", "portal-coo-d-r43", "portal-coo-d-regime", "portal-coo-d-holdings", "wt-cto-benchmark-si",
             "portal-f1-cd3924d5", "irpt-smoke-p-portal-20260923"]
PLAIN = ["portal-trade-vident"]
TARGETS = SHELLS + PORTAL_WT + PLAIN


def lp(p):
    """Windows long-path form, so a walk or delete never silently skips (or fails on) a path past 260 characters."""
    p = os.path.abspath(p)
    return p if p.startswith("\\\\?\\") else "\\\\?\\" + p


def is_link(p):
    return os.path.islink(p) or os.path.isjunction(p)


def links_in(root):
    found = []
    errors = []
    for cur, dirs, files in os.walk(lp(root), onerror=errors.append):   # never descends into links (followlinks=False)
        for d in list(dirs):
            fp = os.path.join(cur, d)
            if is_link(fp):
                found.append(fp)
                dirs.remove(d)
        for f in files:
            fp = os.path.join(cur, f)
            if os.path.islink(fp):
                found.append(fp)
    if errors:   # an unreadable subtree could hide a link: fail closed
        raise OSError("links_in(%s) could not read %d path(s), e.g. %s" % (root, len(errors), errors[0]))
    return found


def measure(p):
    n_files, n_bytes = 0, 0
    for cur, dirs, files in os.walk(p):
        dirs[:] = [d for d in dirs if not is_link(os.path.join(cur, d))]
        for f in files:
            n_files += 1
            try:
                n_bytes += os.path.getsize(os.path.join(cur, f))
            except OSError:
                pass
    return {"entries": len(os.listdir(p)), "files": n_files, "bytes": n_bytes}


def proc_lines():
    out = subprocess.run(["powershell", "-NoProfile", "-Command",
                          "Get-CimInstance Win32_Process | Select-Object CommandLine | ConvertTo-Json -Compress"],
                         capture_output=True, text=True, timeout=120).stdout
    try:
        return [(x.get("CommandLine") or "").lower() for x in json.loads(out)]
    except ValueError:
        return []


def registered_portal_wts():
    out = subprocess.run(["git", "-C", PORTAL, "worktree", "list", "--porcelain"], capture_output=True, text=True).stdout
    return {os.path.normcase(os.path.normpath(ln[9:])) for ln in out.splitlines() if ln.startswith("worktree ")}


def main(argv):
    execute = "--execute" in argv
    assert not (KEEP & set(TARGETS)), "a KEEP folder is on the target list"
    base = measure(LIVE_NM)
    print("LIVE node_modules BEFORE: %s" % base)
    print("KEEP (never touched): %s -> exists=%s" % (sorted(KEEP), all(os.path.isdir(os.path.join(DESK, k)) for k in KEEP)))
    procs = proc_lines()
    regs = registered_portal_wts()
    done, skipped = [], []
    for name in TARGETS:
        p = os.path.join(DESK, name)
        if name in KEEP or os.path.dirname(os.path.normpath(p)) != os.path.normpath(DESK):
            skipped.append((name, "refused by name or not a Desktop child"))
            continue
        if not os.path.isdir(p):
            skipped.append((name, "absent"))
            continue
        if any(p.lower() in c for c in procs):
            skipped.append((name, "a running process uses it"))
            continue
        lk = links_in(p)
        reg = os.path.normcase(os.path.normpath(p)) in regs
        print("%-30s %s links=%d %s" % (name, "portal-worktree" if reg else "folder", len(lk),
                                        "; ".join("%s -> %s" % (os.path.relpath(x, lp(p)), os.path.realpath(x)) for x in lk)))
        if not execute:
            continue
        for link in lk:
            tgt = os.path.realpath(link)
            if os.path.isdir(link):
                os.rmdir(link)          # removes the junction/link itself; never the target's contents
            else:
                os.unlink(link)
            if not os.path.exists(tgt):
                print("FATAL: link target %s vanished after removing %s; stopping" % (tgt, link))
                return 2
        if links_in(p):
            skipped.append((name, "links remain after unlinking"))
            continue
        if reg:
            r = subprocess.run(["git", "-C", PORTAL, "worktree", "remove", "--force", p], capture_output=True, text=True)
            if r.returncode != 0 and os.path.isdir(p):
                shutil.rmtree(lp(p))
        else:
            shutil.rmtree(lp(p))
        done.append(name)
    if execute:
        subprocess.run(["git", "-C", PORTAL, "worktree", "prune"], capture_output=True)
    after = measure(LIVE_NM)
    print("LIVE node_modules AFTER:  %s  %s" % (after, "UNCHANGED" if after == base else "CHANGED -- INVESTIGATE"))
    print("KEEP after: %s exists=%s" % (sorted(KEEP), all(os.path.isdir(os.path.join(DESK, k)) for k in KEEP)))
    for n, why in skipped:
        print("SKIP %s: %s" % (n, why))
    print("DESK-CLEANUP mode=%s targets=%d removed=%d skipped=%d node_modules=%s" % (
        "EXECUTE" if execute else "DRY-RUN", len(TARGETS), len(done), len(skipped), "UNCHANGED" if after == base else "CHANGED"))
    return 0 if after == base else 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
