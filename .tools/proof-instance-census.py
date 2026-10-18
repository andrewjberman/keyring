#!/usr/bin/env python3
"""proof-instance-census.py -- DRY RUN of the newest-instance-only change (CVO~Z verdict 35689, CTO msg 35690).

For every order that has MORE THAN ONE tracked proof instance, print the verdict TODAY and the verdict under NEWEST-ONLY, then name
every order ALREADY FLIPPED complete whose NEWEST instance reads FAIL or INVALID (the CVO's addition: each gets ONE surprise row for
its issuer to rule on; reopening stays a ruling, never automatic). Writes nothing and arms nothing.

  python .tools/proof-instance-census.py [--root <repo root>] [--limit N] [--jobs N] [--json <out.json>]

Definitions (a verdict is the proof-of-spec-check.py return code: 0 VALID, 1 INVALID, 2 usage/read error, T timeout):
  flip gate TODAY       the instance to-pipeline-gate.py grades now: the FIRST match of glob.glob(deliverables/*/<name>) on THIS box;
  flip gate NEWEST      the instance proof_instance_select.py ranks first;
  round-close TODAY     OK when ANY instance reads VALID (round-close-check.py's loop returns at the first that passes);
  round-close NEWEST    OK when the newest instance reads VALID.
Round-close here uses the full checker (like its --deep mode), which is stricter than its structural default: the column says what
the newest instance would be held to, not what the structural pass reads today.
Denominators are printed first. Orders with no order file at HEAD, and instances outside deliverables/<serial>/, are counted, not graded.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import glob
import importlib.util
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SUFFIXES = (".proof_of_spec.json", "_PROOF_OF_SPEC.json")


def _load_select():
    spec = importlib.util.spec_from_file_location("proof_instance_select", os.path.join(HERE, "proof_instance_select.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _git(root, args, timeout=120):
    r = subprocess.run(["git", "-C", root] + args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
    return r.stdout if r.returncode == 0 else ""


def enumerate_pairs(root):
    """{(project_dir, instance file name): [instance dir paths, repo-relative]} for tree instances only."""
    out = _git(root, ["ls-files", "--", "org/missions/*/*/*/deliverables/*/*.proof_of_spec.json",
                      "org/missions/*/*/*/deliverables/*/*_PROOF_OF_SPEC.json"]).splitlines()
    pairs = {}
    for p in out:
        parts = p.split("/")
        if len(parts) != 8 or parts[5] != "deliverables":
            continue
        pairs.setdefault(("/".join(parts[:5]), parts[7]), []).append(p)
    return len(out), pairs


def order_for(root, project, name):
    stem = name
    for s in SUFFIXES:
        if name.endswith(s):
            stem = name[: -len(s)]
    rel = "%s/task-orders/%s.md" % (project, stem)
    text = _git(root, ["show", "HEAD:" + rel])
    return rel, text


def last_status(text):
    m = re.findall(r"<status>\s*([^<\s]+)\s*</status>", text or "")
    return m[-1].lower() if m else "?"


def issuer(text):
    m = re.search(r"<issued_by>\s*([^<\s]+)\s*</issued_by>", text or "")
    return m.group(1) if m else "?"


_cache = {}


def grade(root, inst_rel, order_rel):
    key = (inst_rel, order_rel)
    if key in _cache:
        return _cache[key]
    chk = os.path.join(root, ".tools", "proof-of-spec-check.py")
    try:
        r = subprocess.run([sys.executable, chk, os.path.join(root, *inst_rel.split("/")), "--governing-order", order_rel],
                           cwd=root, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
        v = r.returncode
        viol = [ln.strip()[len("VIOLATION: "):] for ln in (r.stdout or "").splitlines() if ln.strip().startswith("VIOLATION: ")]
        _cache[key] = (v, (viol[0][:110] if viol else ""))
    except Exception as exc:  # noqa: BLE001
        _cache[key] = ("T", str(exc)[:80])
    return _cache[key]


def short(p):
    return os.path.basename(os.path.dirname(p)).split("~")[-1] if "~" in p else os.path.basename(os.path.dirname(p))


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.dirname(HERE))
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--json", default="")
    a = ap.parse_args(argv)
    root = os.path.abspath(a.root)
    sel = _load_select()
    n_files, pairs = enumerate_pairs(root)
    multi = {k: sorted(v) for k, v in pairs.items() if len(v) > 1}
    print("CENSUS root=%s armed_now=%s" % (root, sel.armed(root)))
    print("DENOMINATOR tracked tree instance files=%d  (project, instance-file) pairs=%d  pairs with more than one instance=%d"
          % (n_files, len(pairs), len(multi)))
    work = []
    no_order = 0
    for (project, name), paths in sorted(multi.items()):
        order_rel, text = order_for(root, project, name)
        if not text:
            no_order += 1
            continue
        work.append((project, name, order_rel, text, paths))
    if a.limit:
        work = work[: a.limit]
    print("GRADED %d orders (no order file at HEAD, skipped: %d)" % (len(work), no_order))

    def job(w):
        project, name, order_rel, text, paths = w
        absn = [os.path.join(root, *p.split("/")) for p in paths]
        globbed = glob.glob(os.path.join(root, *project.split("/"), "deliverables", "*", name))
        today_inst = os.path.relpath(globbed[0], root).replace("\\", "/") if globbed else paths[0]
        ranked = sel.ranked(root, absn)
        newest_inst = os.path.relpath(ranked[0][1], root).replace("\\", "/")
        every = {p: grade(root, p, order_rel) for p in paths}
        return {
            "order": order_rel, "status": last_status(text), "issuer": issuer(text), "n": len(paths),
            "today_inst": today_inst, "today": every[today_inst][0] if today_inst in every else grade(root, today_inst, order_rel)[0],
            "newest_inst": newest_inst, "newest": every[newest_inst][0], "newest_why": every[newest_inst][1],
            "rc_any_valid": any(v[0] == 0 for v in every.values()),
            "rc_newest_valid": every[newest_inst][0] == 0,
        }

    rows = []
    with cf.ThreadPoolExecutor(max_workers=max(1, a.jobs)) as ex:
        for r in ex.map(job, work):
            rows.append(r)
    print("\norder | status | n | flip-gate TODAY (inst, rc) | flip-gate NEWEST (inst, rc) | round-close today -> newest | CHANGES")
    n_flip = n_rc = 0
    for r in rows:
        flip = r["today"] != r["newest"]
        rc = r["rc_any_valid"] != r["rc_newest_valid"]
        n_flip += flip
        n_rc += rc
        print("%s | %s | %d | ~%s rc=%s | ~%s rc=%s | %s -> %s | %s" % (
            r["order"].split("/")[-1][:58], r["status"], r["n"], short(r["today_inst"]), r["today"], short(r["newest_inst"]),
            r["newest"], "OK" if r["rc_any_valid"] else "NOT-OK", "OK" if r["rc_newest_valid"] else "NOT-OK",
            ("flip " if flip else "") + ("round-close" if rc else "") or "-"))
    flipped_bad = [r for r in rows if r["status"] in ("complete", "completed") and r["newest"] != 0]
    print("\nSUMMARY orders=%d flip-gate verdict changes=%d round-close verdict changes=%d" % (len(rows), n_flip, n_rc))
    print("CVO ADDITION: orders already flipped complete whose NEWEST instance reads FAIL or INVALID: %d" % len(flipped_bad))
    for r in flipped_bad:
        print("  ROW-CANDIDATE order=%s issuer=%s newest=~%s rc=%s why=%s" % (r["order"], r["issuer"], short(r["newest_inst"]),
                                                                              r["newest"], r["newest_why"]))
    if a.json:
        with open(a.json, "w", encoding="ascii", newline="\n") as fh:
            json.dump(rows, fh, indent=1)
        print("JSON %s" % a.json)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
