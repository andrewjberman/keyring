#!/usr/bin/env python3
"""seat-gates-dry-pass.py -- replay what the seat-gates block of safe-deploy.sh and safe-apply.sh WOULD read for a push or deploy
of a commit range, over real history, to count false stops BEFORE any ENFORCE switch exists (NFRA_CTLPLN cell CT-s-3, AMENDMENT 1
item 5). READ-ONLY: it runs no wrapper, no deploy core, no terraform and no AWS call; it reads git history and files, and it runs
the two read-only checks (apply-who-check.py, crossbox-deploy-check.py) exactly as the wrappers call them.

    python .tools/seat-gates-dry-pass.py --range <a>..<b> [--range ...] [--serial <serial>] [--device <box>]
    python .tools/seat-gates-dry-pass.py --last <n> [--ref CLOUD] [--serial <serial>] [--device <box>]

  --range    a commit range as a push or deploy carries it (repeatable).
  --last     the last n NON-MERGE commits of --ref (default CLOUD) that touch a deployable home (data/*/scripts/) or a Terraform root
             (infra/aws/terraform/), each replayed as the range <commit>^..<commit>.
  --serial   the acting seat for every range. Without it each range is attributed to its commit author's name: exactly one
             distinct author and it must be a serial (0.x.0_XX_Name[~lane]); otherwise the range is `skipped` with the reason.
  --device   the box whose view is replayed (sets AGENTBUS_DEVICE for the checks); default: the environment's.
  --repo-root  the tree whose register, projects, task orders, notices, calls, open deploys and deploy core are read (default:
             this tree); the two checks run are always the ones beside this file.

Per range it replays, with the wrappers' own rules:
  DEPLOY block (safe-deploy.sh): the files the deploy core would deploy for the range (crossbox-deploy-check.py
      --list-deployable, which imports the core's own detectors); apply-who runs only if at least one file deploys, else SKIP;
      the cross-box check runs per data/<pipeline> root (at most four) with the deployable files under that root.
  APPLY block (safe-apply.sh): each Terraform root the range touches (at most four), untargeted (the worst case), with the
      Terraform files of the root the range carries -- the replay of --files-vs-trunk.
It reads TODAY's register, projects, notices, calls and open deploys (the state a push would meet now), not the state of the day
the commit was made. One line per range; then `BY-SWITCH ...`; LAST line:
    SEAT-GATES-DRY ranges=<n> would_stop=<k> skipped=<s> ok=<True when k is 0>
A would-stop is a range where, with all four switches on, at least one check REFUSES/STOPS or gives no verdict (fail closed).
Exit 0 when k is 0, 1 otherwise, 2 on a usage error.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

TOOLS = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOLS)
SERIAL_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+_[A-Z]{2}_[A-Za-z0-9_]+(~[A-Za-z0-9]+)?$")
SCRIPTS_ROOT_RE = re.compile(r"^(?:.*/)?(data/[^/]*)/scripts/.*$")
TF_ROOT_RE = re.compile(r"^(infra/aws/terraform/[^/]+)/(.+)$")
TF_SUFFIXES = (".tf", ".tfvars", ".tf.json", ".hcl", ".tftpl")
MAX_ROOTS = 4


def run(argv, env, stdin_text=""):
    try:
        proc = subprocess.run(argv, input=stdin_text, capture_output=True, text=True, encoding="utf-8", errors="replace",
                              env=env, timeout=120)
        return proc.returncode, (proc.stdout + proc.stderr).replace("\r", "")
    except subprocess.TimeoutExpired:
        return 124, "timeout after 120 s"
    except OSError as exc:
        return 127, "%s: %s" % (type(exc).__name__, exc)


def last_line(text):
    lines = [ln for ln in text.splitlines() if ln.strip()]
    return lines[-1] if lines else ""


def git(repo, *args):
    proc = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    return proc.returncode, proc.stdout


def field(line, key):
    match = re.search(r"\b%s=(\S+)" % key, line)
    return match.group(1) if match else None


def who_verdict(repo, env, serial, root):
    rc, out = run([sys.executable, os.path.join(TOOLS, "apply-who-check.py"), "--serial", serial, "--root", root,
                   "--orders-root", os.path.join(repo, "org", "missions")], env)
    line = last_line(out)
    verdict = field(line, "verdict") if line.startswith("APPLY-WHO ") else None
    if verdict in ("ADMITTED", "REFUSED"):
        return verdict, line
    return "NO-VERDICT", "apply-who-check gave no verdict (rc=%d): %s" % (rc, line)


def cross_verdict(repo, env, serial, root, files):
    rc, out = run([sys.executable, os.path.join(TOOLS, "crossbox-deploy-check.py"), "--repo-root", repo, "--root", root,
                   "--serial", serial, "--files-from", "-"], env, "\n".join(files) + "\n")
    line = last_line(out)
    verdict = field(line, "verdict") if line.startswith("CROSSBOX-DEPLOY ") else None
    if verdict in ("CLEAR", "STOP"):
        why = next((ln[len("STOP: "):] for ln in out.splitlines() if ln.startswith("STOP: ")), "")
        return verdict, line, why
    return "NO-VERDICT", "crossbox-deploy-check gave no verdict (rc=%d): %s" % (rc, line), ""


def attribute(repo, rng, serial_arg):
    """(serial or None, author_text, skip_reason)."""
    rc, out = git(repo, "log", "--format=%an", rng)
    names = sorted({ln.strip() for ln in out.splitlines() if ln.strip()})
    author = ", ".join(names) if names else "(no commit)"
    if rc != 0 or not names:
        return None, author, "git log %s gave no commit (rc=%d)" % (rng, rc)
    if serial_arg:
        return serial_arg, author, ""
    if len(names) != 1:
        return None, author, "the range has %d distinct authors and no --serial was given" % len(names)
    if not SERIAL_RE.match(names[0]):
        return None, author, "author %r is not a serial" % names[0]
    return names[0], author, ""


def replay(repo, env, rng, serial_arg):
    serial, author, skip = attribute(repo, rng, serial_arg)
    rec = {"range": rng, "serial": serial, "author": author, "skip": skip, "stops": [], "switches": set(), "parts": []}
    if skip:
        return rec
    rc, out = git(repo, "diff", "--name-only", rng)
    if rc != 0:
        rec["skip"] = "git diff %s failed (rc=%d)" % (rng, rc)
        return rec
    changed = [ln.strip().replace("\\", "/") for ln in out.splitlines() if ln.strip()]
    # ---- DEPLOY block (the roots are the wrapper's: data/<pipeline> of every scripts path, plus the roots of what deploys)
    rc, listing = run([sys.executable, os.path.join(TOOLS, "crossbox-deploy-check.py"), "--list-deployable", "--repo-root", repo,
                       "--commit-range", rng], env)
    lines = [ln.strip() for ln in listing.splitlines()]
    count = next((int(m.group(1)) for m in (re.match(r"^DEPLOYABLE-COUNT n=(\d+)$", ln) for ln in lines) if m), None)
    deployable = [ln[len("DEPLOYABLE "):] for ln in lines if ln.startswith("DEPLOYABLE ")]
    droots = [ln[len("DEPLOY-ROOT "):] for ln in lines if ln.startswith("DEPLOY-ROOT ")]
    roots = sorted({m.group(1) for m in (SCRIPTS_ROOT_RE.match(p) for p in changed) if m} | set(droots))[:MAX_ROOTS]
    if count is None:
        rec["stops"].append("deploy: --list-deployable gave no count (rc=%d): %s" % (rc, last_line(listing)))
        rec["switches"].add("deploy-list")
        rec["parts"].append("deploy=NO-COUNT")
    elif not roots:
        rec["parts"].append("deploy=no-scripts-path(SKIP)")
    else:
        if count == 0:
            rec["parts"].append("deploy_apply_who=SKIP(deploys nothing)")
        else:
            verdict, line = who_verdict(repo, env, serial, roots[0])
            rec["parts"].append("deploy_apply_who=%s" % verdict)
            if verdict != "ADMITTED":
                rec["stops"].append("deploy apply-who: %s" % line)
                rec["switches"].add("apply-who.safe-deploy")
        for root in roots:
            files = [f for f in deployable if f.startswith(root + "/")]
            cv, cline, why = cross_verdict(repo, env, serial, root, files)
            rec["parts"].append("deploy_crossbox[%s]=%s(%d files)" % (root, cv, len(files)))
            if cv != "CLEAR":
                rec["stops"].append("deploy crossbox %s: %s" % (root, why or cline))
                rec["switches"].add("crossbox.safe-deploy")
    # ---- APPLY block
    tf = {}
    for path in changed:
        match = TF_ROOT_RE.match(path)
        if match and path.endswith(TF_SUFFIXES):
            tf.setdefault(match.group(1), []).append(path)
    if tf:
        roots = sorted(tf)[:MAX_ROOTS]
        verdict, line = who_verdict(repo, env, serial, roots[0])
        rec["parts"].append("apply_apply_who=%s" % verdict)
        if verdict != "ADMITTED":
            rec["stops"].append("apply apply-who: %s" % line)
            rec["switches"].add("apply-who.safe-apply")
        for root in roots:
            cv, cline, why = cross_verdict(repo, env, serial, root, tf[root])
            rec["parts"].append("apply_crossbox[%s]=%s(%d files)" % (root, cv, len(tf[root])))
            if cv != "CLEAR":
                rec["stops"].append("apply crossbox %s: %s" % (root, why or cline))
                rec["switches"].add("crossbox.safe-apply")
    if not rec["parts"]:
        rec["parts"].append("nothing deployable and no Terraform root")
    return rec


def usage(msg):
    print("ERROR: %s\nusage: seat-gates-dry-pass.py (--range a..b)... | --last n [--ref CLOUD] [--serial S] [--device D] [--repo-root DIR]" % msg,
          file=sys.stderr)
    return 2


def main(argv):
    ranges, last, ref, serial, device, repo = [], 0, "CLOUD", "", "", REPO
    i = 0
    try:
        while i < len(argv):
            arg = argv[i]
            if arg == "--range":
                ranges.append(argv[i + 1])
            elif arg == "--last":
                last = int(argv[i + 1])
            elif arg == "--ref":
                ref = argv[i + 1]
            elif arg == "--serial":
                serial = argv[i + 1]
            elif arg == "--device":
                device = argv[i + 1]
            elif arg == "--repo-root":
                repo = os.path.abspath(argv[i + 1])
            else:
                return usage("unknown argument %r" % arg)
            i += 2
    except (IndexError, ValueError) as exc:
        return usage(exc)
    if last:
        rc, out = git(repo, "log", ref, "--no-merges", "--format=%H", "-n", str(last), "--", ":(glob)data/*/scripts/**", ":(glob)infra/aws/terraform/**")
        if rc != 0:
            return usage("git log %s failed (rc=%d)" % (ref, rc))
        ranges += ["%s^..%s" % (sha, sha) for sha in out.split()]
    if not ranges:
        return usage("no range: give --range or --last")
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    if device:
        env["AGENTBUS_DEVICE"] = device
    with ThreadPoolExecutor(max_workers=6) as pool:
        recs = list(pool.map(lambda rng: replay(repo, env, rng, serial), ranges))
    stops = skipped = 0
    tally = {}
    for rec in recs:
        if rec["skip"]:
            skipped += 1
            print("RANGE %s verdict=SKIPPED author=%r reason=%s" % (rec["range"], rec["author"], rec["skip"]))
            continue
        verdict = "WOULD-STOP" if rec["stops"] else "PASS"
        stops += 1 if rec["stops"] else 0
        for name in rec["switches"]:
            tally[name] = tally.get(name, 0) + 1
        print("RANGE %s serial=%s verdict=%s %s" % (rec["range"], rec["serial"], verdict, " ".join(rec["parts"])))
        for stop in rec["stops"]:
            print("  WOULD-STOP %s | %s" % (rec["range"], stop))
    print("BY-SWITCH %s" % (" ".join("%s=%d" % kv for kv in sorted(tally.items())) or "none"))
    print("SEAT-GATES-DRY ranges=%d would_stop=%d skipped=%d ok=%s" % (len(recs), stops, skipped, stops == 0))
    return 0 if stops == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
