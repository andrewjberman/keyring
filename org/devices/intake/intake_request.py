#!/usr/bin/env python3
"""Intake requests: file a request for a package, record its decision, answer status and show.

Stdlib only, ASCII. One JSON file per request under <root>/requests/REQ-<UTC stamp>-<name>.json.
The status answer reads those records and requirements.txt; it does not depend on which device or
serial asks. Subcommands: file, decide, status, show, downloads. A refusal prints REFUSED, exits 1.
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import sys

SCHEMA = "intake-request/1"
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT = HERE
DEFAULT_REQUIREMENTS = os.path.normpath(os.path.join(HERE, "..", "..", "..", "requirements.txt"))
NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
VERSION_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._+!-]*$")
ID_RE = re.compile(r"^REQ-[0-9TZ]+-[A-Za-z0-9._-]+$")
PIN_RE = re.compile(r"^([A-Za-z0-9][A-Za-z0-9._-]*)==([^\s;]+)")
DAY_RE = re.compile(r"^[0-9]{8}$")


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def utc_stamp():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def canon(name):
    return re.sub(r"[-_.]+", "-", name).lower()


def one_line(text):
    return " ".join(str(text).split())


def refuse(msg):
    print("REFUSED " + msg)
    return 1


def load(path):
    with open(path, encoding="utf-8") as fh:
        rec = json.load(fh)
    if not isinstance(rec, dict):
        raise ValueError("record is not a JSON object")
    return rec


def save(path, rec):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(json.dumps(rec, indent=2, ensure_ascii=True) + "\n")
    os.replace(tmp, path)


def req_dir(root):
    return os.path.join(root, "requests")


def request_path(root, rid):
    if not ID_RE.match(rid or ""):
        return None
    return os.path.join(req_dir(root), rid + ".json")


def all_requests(root):
    d = req_dir(root)
    if not os.path.isdir(d):
        return []
    return [load(os.path.join(d, f)) for f in sorted(os.listdir(d))
            if f.startswith("REQ-") and f.endswith(".json")]


def cmd_file(a):
    if not NAME_RE.match(a.name) or not VERSION_RE.match(a.version):
        return refuse("name or version has characters not allowed")
    if not (a.needed_by.strip() and a.why_no_approved.strip() and a.by.strip()):
        return refuse("--needed-by, --why-no-approved and --by are required")
    if not os.path.isdir(a.root):
        return refuse("intake folder missing: " + a.root)
    os.makedirs(req_dir(a.root), exist_ok=True)
    rid = "REQ-%s-%s" % (utc_stamp(), a.name)
    path = os.path.join(req_dir(a.root), rid + ".json")
    if os.path.exists(path):
        return refuse("request already exists: " + rid)
    rec = {"schema": SCHEMA, "id": rid, "name": a.name, "version": a.version,
           "needed_by": one_line(a.needed_by), "why_no_approved": one_line(a.why_no_approved),
           "requested_by": a.by, "requested_at": utc_now(), "decisions": []}
    save(path, rec)
    print("FILED id=%s package=%s==%s" % (rid, a.name, a.version))
    return 0


def cmd_decide(a):
    path = request_path(a.root, a.id)
    if path is None or not os.path.isfile(path):
        return refuse("no such request: %s" % a.id)
    rec = load(path)
    if rec.get("decisions"):
        return refuse("already decided: %s (a second decision is refused)" % a.id)
    if not (a.by.strip() and a.reason.strip()):
        return refuse("--by and --reason are required")
    if not os.path.isfile(a.evidence):
        return refuse("evidence file missing: " + a.evidence)
    with open(a.evidence, "rb") as fh:
        digest = hashlib.sha256(fh.read()).hexdigest()
    rec["decisions"].append({"verdict": a.verdict, "by": a.by, "at": utc_now(),
                             "reason": one_line(a.reason),
                             "evidence": {"path": os.path.abspath(a.evidence), "sha256": digest}})
    save(path, rec)
    print("DECIDED id=%s verdict=%s by=%s" % (a.id, a.verdict, a.by))
    return 0


def pinned(req_path, name, version):
    with open(req_path, encoding="utf-8") as fh:
        for line in fh:
            m = PIN_RE.match(line.split("#", 1)[0].strip())
            if m and canon(m.group(1)) == canon(name) and m.group(2) == version:
                return True
    return False


def cmd_status(a):
    if not os.path.isfile(a.requirements):
        return refuse("requirements file missing: " + a.requirements)
    if not os.path.isdir(a.root):
        return refuse("intake folder missing: " + a.root)
    pkg = "PACKAGE %s==%s" % (a.name, a.version)
    if pinned(a.requirements, a.name, a.version):
        print("%s APPROVED by=requirements.txt at=- reason=listed in requirements.txt" % pkg)
        return 0
    hits = [r for r in all_requests(a.root)
            if canon(str(r.get("name", ""))) == canon(a.name) and r.get("version") == a.version]
    decs = [d for r in hits for d in (r.get("decisions") or [])]
    if decs:
        d = max(decs, key=lambda x: str(x.get("at", "")))
        print("%s %s by=%s at=%s reason=%s" % (pkg, d.get("verdict"), d.get("by"), d.get("at"),
                                              one_line(d.get("reason", ""))))
    elif hits:
        print("%s REQUESTED by=- at=- reason=-" % pkg)
    else:
        print("%s UNKNOWN by=- at=- reason=-" % pkg)
    return 0


def cmd_show(a):
    path = request_path(a.root, a.id)
    if path is None or not os.path.isfile(path):
        return refuse("no such request: %s" % a.id)
    rec = load(path)
    lines = [
        "REQUEST %s" % rec.get("id"),
        "what: %s" % rec.get("name"),
        "exact version: %s" % rec.get("version"),
        "package: %s==%s" % (rec.get("name"), rec.get("version")),
        "needed by: %s" % rec.get("needed_by"),
        "why nothing approved will do: %s" % rec.get("why_no_approved"),
        "requested by: %s at %s" % (rec.get("requested_by"), rec.get("requested_at")),
    ]
    decs = rec.get("decisions") or []
    if not decs:
        lines.append("DECISION: NONE (still REQUESTED)")
    for d in decs:
        ev = d.get("evidence") or {}
        lines += ["DECISION: %s" % d.get("verdict"), "who decided: %s" % d.get("by"),
                  "when: %s" % d.get("at"), "why: %s" % d.get("reason"),
                  "evidence: %s sha256=%s" % (ev.get("path"), ev.get("sha256"))]
    print("\n".join(lines))
    return 0


def cmd_downloads(a):
    if not DAY_RE.match(a.day):
        return refuse("--day must be YYYYMMDD")
    if not os.path.isdir(a.root):
        return refuse("intake folder missing: " + a.root)
    rec_dir = os.path.join(a.root, "records")
    if not os.path.isdir(rec_dir):
        return refuse("record folder missing: " + rec_dir)
    requests = files = unattributed = 0
    for dp, _dn, fn in os.walk(rec_dir):
        for f in sorted(fn):
            if not f.endswith(".fetch.json"):
                continue
            try:
                rec = load(os.path.join(dp, f))
            except (OSError, ValueError) as exc:
                return refuse("fetch record unreadable: %s (%s)" % (f, exc))
            if str(rec.get("at") or "")[:10].replace("-", "") != a.day:
                continue
            if "device" not in rec:
                unattributed += 1
                continue
            if rec["device"] != a.device:
                continue
            files += 1
            requests += len(rec.get("requests") or [])
    if unattributed:
        print("NOTE: %d fetch record(s) on day %s carry no device field and are not counted"
              % (unattributed, a.day), file=sys.stderr)
    print("DOWNLOADS-TODAY device=%s day=%s requests=%d files=%d" % (a.device, a.day, requests, files))
    return 0


def main(argv=None):
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--root", default=DEFAULT_ROOT, help="intake folder (default: this folder)")
    p = argparse.ArgumentParser(prog="intake_request.py", description=__doc__.split("\n")[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("file", parents=[common])
    f.add_argument("--name", required=True)
    f.add_argument("--version", required=True)
    f.add_argument("--needed-by", required=True)
    f.add_argument("--why-no-approved", required=True)
    f.add_argument("--by", required=True)
    d = sub.add_parser("decide", parents=[common])
    d.add_argument("--id", required=True)
    d.add_argument("--verdict", required=True, choices=["APPROVED", "REFUSED"])
    d.add_argument("--by", required=True)
    d.add_argument("--reason", required=True)
    d.add_argument("--evidence", required=True)
    s = sub.add_parser("status", parents=[common])
    s.add_argument("--name", required=True)
    s.add_argument("--version", required=True)
    s.add_argument("--device", default=None, help="accepted; does not change the answer")
    s.add_argument("--requirements", default=DEFAULT_REQUIREMENTS)
    w = sub.add_parser("show", parents=[common])
    w.add_argument("--id", required=True)
    g = sub.add_parser("downloads", parents=[common])
    g.add_argument("--device", required=True)
    g.add_argument("--day", required=True)
    a = p.parse_args(argv)
    handlers = {"file": cmd_file, "decide": cmd_decide, "status": cmd_status,
                "show": cmd_show, "downloads": cmd_downloads}
    return handlers[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
