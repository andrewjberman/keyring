#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""prd-signoff.py -- the reviewer's STAMP for L4-R (spine v3.15), and the one status read for it.

    python .tools/prd-signoff.py status [<CODE>]
        Every tree project at dep_stage PRD or later: prd_version, each half's state (SIGNED / STALE /
        REFUSED / MISSING / NOT-PERMITTED), who signed, and what is owed by whom. The read Andrew, the CTO
        and the reviewers all run instead of asking each other.

    python .tools/prd-signoff.py sign   <CODE> --half brief|ratified-text --review <path>@<pin> [--for 4.0.0_SA_CRO]
    python .tools/prd-signoff.py refuse <CODE> --half brief|ratified-text --review <path>@<pin> --reason "<one line>"
        Writes org/missions/D<n>/<MACRO>/<CODE>/prd/signoff/<your serial>.json bound to the HASH of the half's
        sections at HEAD (not to prd_version), and commits it through .tools/safe-commit.sh under your serial.
        Your serial is OPAL_AGENT_SERIAL. --for names the primary reviewer you are substituting for
        (2.0.0_SA_COO signing the brief half in the CRO's stead); the file records it.
        A REFUSED verdict carries --review (the pinned review with the corrections by line) and --reason.

    python .tools/prd-signoff.py --self-test

WHO SIGNS WHAT (prd_signoff_lib.REVIEWERS):
    ratified-text (ENDPOINT + CONTRACTS)   3.0.0_SA_CVO, always; nobody substitutes
    brief (every other section)            4.0.0_SA_CRO; 2.0.0_SA_COO in its stead (never the COO lane holding this project's round)
The CTO never signs. A tilde lane signs for its base.

The gate (`to-pipeline-gate.py` LIMB 6), the notifier (`prd-header-notify.py`) and this tool all call
prd_signoff_lib -- one rule, three consumers. After a sign, this tool prints the gate's own verdict.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))


def _lib():
    spec = importlib.util.spec_from_file_location("prd_signoff_lib", os.path.join(HERE, "prd_signoff_lib.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _git(*args):
    return subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")


def _projects():
    """{CODE: (project_json_rel, prd_rel)} for every tree project row that names a PRD."""
    out = {}
    base = os.path.join(ROOT, "org", "missions")
    if not os.path.isdir(base):
        return out
    for d in sorted(os.listdir(base)):
        dp = os.path.join(base, d)
        if not os.path.isdir(dp) or not d.startswith("D"):
            continue
        for macro in sorted(os.listdir(dp)):
            mp = os.path.join(dp, macro)
            if not os.path.isdir(mp):
                continue
            for code in sorted(os.listdir(mp)):
                pj = os.path.join(mp, code, "project.json")
                prd = os.path.join(mp, code, "prd", code + "_PRD.md")
                if os.path.isfile(pj) and os.path.isfile(prd):
                    out[code] = (os.path.relpath(pj, ROOT).replace("\\", "/"), os.path.relpath(prd, ROOT).replace("\\", "/"))
    return out


def _project_doc(rel):
    try:
        with open(os.path.join(ROOT, rel), "r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:  # noqa: BLE001
        return {}


def _evaluate(lib, code, prd_rel, pj_rel):
    with open(os.path.join(ROOT, prd_rel), "r", encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    files = lib.read_signoff_files(os.path.join(ROOT, os.path.dirname(prd_rel), lib.SIGNOFF_DIR))
    doc = _project_doc(pj_rel)
    return lib.evaluate(text, files, coo_lane_of_project=doc.get("coo_lane"), designated=lib.designated_brief_signer(doc)[0]), text, doc


def cmd_status(lib, code=None):
    projects = _projects()
    if code:
        if code not in projects:
            print("ERROR: no tree project %s with a PRD" % code, file=sys.stderr)
            return 2
        projects = {code: projects[code]}
    rows = 0
    for c, (pj_rel, prd_rel) in projects.items():
        doc = _project_doc(pj_rel)
        if doc.get("dep_stage") in (None, "REGISTERED"):
            continue
        rows += 1
        r, _, _ = _evaluate(lib, c, prd_rel, pj_rel)
        last = _git("log", "-1", "--format=%h", "--", prd_rel).stdout.strip()
        bound, why = lib.bound_by_law(ROOT, prd_rel)
        if not bound:
            print("%s  %s @%s  dep_stage=%s  ->  GRANDFATHERED (%s)" % (c, r["prd_version"], last, doc.get("dep_stage"), why))
            continue
        print("%s  %s @%s  dep_stage=%s  ->  %s" % (c, r["prd_version"], last, doc.get("dep_stage"), "ADMITTED" if r["admitted"] else "WITHHELD"))
        live = lib.live_serials(ROOT)
        for half in lib.HALVES:
            st = r["halves"][half]
            if st["state"] == "SIGNED":
                owed = ""
            else:
                who, reason = lib.route_half(half, live, coo_lane_of_project=doc.get("coo_lane"), designated=lib.designated_brief_signer(doc)[0])
                owed = "   OWED BY %s (%s)" % (who, reason)
            print("    %-14s %-13s %-22s %s%s" % (half, st["state"], st["by"] or "-", st["detail"][:90], owed))
        for n in r["unreadable"]:
            print("    UNREADABLE   %s" % n)
    if not rows:
        print("no tree project at dep_stage PRD or later (denominator: %d project rows with a PRD)" % len(projects))
    return 0


def cmd_stamp(lib, verdict, code, half, review, reason, substitute_for, expect_half_hash=None):
    serial = os.environ.get("OPAL_AGENT_SERIAL", "").strip()
    if not serial:
        print("ERROR: OPAL_AGENT_SERIAL is not set -- a stamp carries the signer's identity and refuses to guess it", file=sys.stderr)
        return 2
    projects = _projects()
    if code not in projects:
        print("ERROR: no tree project %s with a PRD" % code, file=sys.stderr)
        return 2
    pj_rel, prd_rel = projects[code]
    doc = _project_doc(pj_rel)
    designated, designated_why = lib.designated_brief_signer(doc)
    is_designated = bool(designated) and str(serial) == str(designated) and half == "brief"
    ok, why = lib.permitted_signer(half, serial, coo_lane_of_project=doc.get("coo_lane"), designated=designated)
    if not ok:
        print("REFUSED: %s" % why, file=sys.stderr)
        return 3
    if is_designated:
        substitute_for = None  # a designated signer signs in its own name; the file records the designation instead
    elif lib.base_serial(serial) == lib.SUBSTITUTE.get(half) and not substitute_for:
        print("REFUSED: %s signs the %s half only in a primary's stead -- pass --for %s" % (serial, half, lib.PRIMARY[half]), file=sys.stderr)
        return 3
    if "@" not in review:
        print("ERROR: --review must be <path>@<pin> (the pinned review record)", file=sys.stderr)
        return 2
    # THE REVIEW-ARTIFACT GUARD. "@" in the string is not a review: --review accepted ANY value and
    # never checked that the path resolves, so a stamp could cite a review that DOES NOT EXIST and
    # still read structurally immaculate -- review_ref populated, half_hash present, verdict SIGNED.
    # Measured by 4.0.0_SA_CRO~Z 2026-09-12 over all 7 stamps on the POSN record (5 clean, 1
    # unread-bytes, 1 no-artifact): stamp 9a2e542c0b's review_ref is a PROSE SENTENCE with a pin
    # appended, whose "path" is a sentence fragment and whose git show returns ZERO BYTES. The gate
    # had counted it a signed half since 08:52:52Z. A real verification had happened; NONE OF IT WAS
    # AUDITABLE, which is the whole property this field exists to provide.
    # --expect-half-hash CANNOT see this class: the bytes can be current and genuinely reviewed and
    # there is still no durable artifact to re-read.
    _rpath, _, _rpin = review.rpartition("@")
    _probe = _git("cat-file", "-e", "%s:%s" % (_rpin, _rpath))
    if _probe.returncode != 0:
        print("REFUSED: --review does not resolve to an artifact.", file=sys.stderr)
        print("  path: %s" % _rpath, file=sys.stderr)
        print("  pin : %s" % _rpin, file=sys.stderr)
        print("A review nobody can re-read is not a review. Pass <path>@<pin> naming a file that "
              "exists at that commit; prose belongs in --reason.", file=sys.stderr)
        return 3
    if verdict == "REFUSED" and not reason:
        print("ERROR: a REFUSED verdict carries --reason (one line; the corrections live in the review by pinned line)", file=sys.stderr)
        return 2
    # the PRD is read at HEAD, never the worktree: the stamp binds to committed bytes
    head = _git("rev-parse", "HEAD").stdout.strip()
    shown = _git("show", "%s:%s" % (head, prd_rel))
    if shown.returncode != 0:
        print("ERROR: cannot read %s at HEAD: %s" % (prd_rel, shown.stderr.strip()[:200]), file=sys.stderr)
        return 2
    text = shown.stdout
    with open(os.path.join(ROOT, prd_rel), "r", encoding="utf-8", errors="replace") as fh:
        wt = fh.read()
    if lib.half_hashes(wt) != lib.half_hashes(text):
        print("REFUSED: the PRD's worktree copy differs from HEAD in a half's bytes -- an uncommitted edit is not a thing to sign; commit or discard it first", file=sys.stderr)
        return 3
    # THE REVIEWED-BYTES GUARD. Without it a stamp binds to whatever the half is AT STAMP TIME, so a
    # half that moved WHILE THE REVIEWER WAS READING is signed by a seat that never saw it -- and
    # nothing refuses, because the worktree/HEAD check above compares the file to itself, not to what
    # was reviewed. `--review <path>@<pin>` pins the REVIEWER'S OWN DOCUMENT, never the PRD half it
    # covers. Found by 4.0.0_SA_CRO~Z 2026-09-12; the consumer is the COO cut, which treats ADMITTED
    # as its precondition to commit and spawn. Measured the same night: a brief half moved
    # f5bbef8c9 -> d64247e7f WHILE its reviewer held it, and only a hand-sent message prevented the
    # stale signature. OPT-IN so every existing caller is unchanged; FAIL-CLOSED when supplied.
    if expect_half_hash:
        _now = lib.half_hashes(text).get(half, "")
        _want = expect_half_hash.strip()
        if not (_now == _want or _now.startswith(_want) or _want.startswith(_now)):
            print("REFUSED: the %s half has MOVED since the bytes you reviewed." % half, file=sys.stderr)
            print("  reviewed: %s" % _want, file=sys.stderr)
            print("  current : %s" % _now, file=sys.stderr)
            print("A signature binds to the CURRENT bytes, so stamping now would certify a half you "
                  "did not read. Re-read the current half and re-run with its hash.", file=sys.stderr)
            return 3
    pin = _git("log", "-1", "--format=%H", "--", prd_rel).stdout.strip()
    sdoc = lib.build_doc(os.path.basename(prd_rel), text, pin, half, verdict, review, serial, substitute_for=substitute_for, reason=reason)
    if is_designated:
        sdoc["designated_by"] = designated_why
    sdir = os.path.join(ROOT, os.path.dirname(prd_rel), lib.SIGNOFF_DIR)
    os.makedirs(sdir, exist_ok=True)
    out_rel = os.path.relpath(os.path.join(sdir, serial + ".json"), ROOT).replace("\\", "/")
    with open(os.path.join(ROOT, out_rel), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(sdoc, fh, indent=2)
        fh.write("\n")
    msg = ("L4-R %s(%s %s half, %s): %s %s @%s\n\nhalf_hash %s; review %s%s\n" % (
        verdict.lower(), code, half, serial, os.path.basename(prd_rel), sdoc["prd_version"], pin[:10],
        sdoc["half_hash"][:12], review, ("; reason: " + reason) if reason else ""))
    fd, mpath = tempfile.mkstemp(prefix="prd-signoff-", suffix=".txt")
    with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(msg)
    author = "%s <%s@opal.agent>" % (serial, serial)
    sys.path.insert(0, os.path.join(ROOT, ".tools"))
    from git_bash_resolver import git_bash  # bare "bash" Windows-resolves to the System32 WSL stub (measured by 3.0.0_SA_CVO 2026-09-11)
    bash = git_bash()
    if not bash:
        print("ERROR: no Git-for-Windows bash.exe found; the stamp file is written at %s but NOT committed" % out_rel, file=sys.stderr)
        return 2
    sc = subprocess.run([bash, os.path.join(ROOT, ".tools", "safe-commit.sh"), "--author", author, "-F", mpath, "--", out_rel],
                        cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    lines = (sc.stdout + sc.stderr).strip().splitlines()
    # a refusal prints every line: safe-commit's closing reminder alone is six lines and pushed the reason out of a tail
    tail = lines if sc.returncode != 0 else lines[-6:]
    for ln in tail:
        print("  " + ln[:200])
    if sc.returncode != 0:
        print("ERROR: safe-commit refused (rc=%d); the stamp file is written at %s but NOT committed -- fix the refusal and re-run" % (sc.returncode, out_rel), file=sys.stderr)
        return sc.returncode
    r, _, _ = _evaluate(lib, code, prd_rel, pj_rel)
    print("STAMPED %s %s half %s by %s -> PRD now %s" % (code, half, verdict, serial, "ADMITTED" if r["admitted"] else "WITHHELD (%s still owed)" % ", ".join(lib.missing_halves(r))))
    return 0


def main(argv):
    lib = _lib()
    if "--self-test" in argv:
        return 1 if lib.self_test() else 0
    ap = argparse.ArgumentParser(prog="prd-signoff.py")
    sub = ap.add_subparsers(dest="verb")
    s = sub.add_parser("status")
    s.add_argument("code", nargs="?")
    for v in ("sign", "refuse"):
        p = sub.add_parser(v)
        p.add_argument("code")
        p.add_argument("--half", required=True, choices=list(lib.HALVES))
        p.add_argument("--review", required=True, help="<path>@<pin> of the review record")
        p.add_argument("--reason", default=None)
        p.add_argument("--for", dest="substitute_for", default=None, help="primary reviewer you substitute for")
        p.add_argument("--expect-half-hash", dest="expect_half_hash", default=None,
                       help="the half_hash you ACTUALLY REVIEWED. If the half has moved since, the stamp "
                            "is REFUSED instead of silently binding to bytes you did not read.")
    a = ap.parse_args(argv)
    if a.verb == "status":
        return cmd_status(lib, a.code)
    if a.verb in ("sign", "refuse"):
        return cmd_stamp(lib, "SIGNED" if a.verb == "sign" else "REFUSED", a.code, a.half, a.review, a.reason,
                         a.substitute_for, a.expect_half_hash)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
