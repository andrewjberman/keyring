#!/usr/bin/env python3
"""xadj.py -- CROSS-ADJUDICATION FILES: a box CTO's open-ended, architectural or cross-box call goes, as a written
position, to the laptop CTO (site Z CTO as backup), who rules it and records the ruling.

Andrew-direct 2026-10-09 ~00:0xZ (record org/tier1_exec/1.0.0_SA_CTO/deliverables/
ANDREW_DIRECT_20261009_000xZ_KEEP_WORK_DRIVING_OPEN_CALL_QUEUE_CROSS_ADJUDICATION_AND_NEXT_CALLS_ON_EMPTY_TICK.md): "that CTO
should write a file including the context, their position on it, and a breakdown of the reason why it gave them pause ...
Then that document gets transferred to the laptop CTO, or SiteZ CTO as a backup if the laptop is down, to ajudicate, and the
laptop CTO notes these adjudications in a document type somewhere (... cross-adjudication files)." Design:
org/tier1_exec/4.0.0_SA_CRO~B/deliverables/DESIGN_KEEP_WORK_DRIVING_20261009.md. Owner 4.0.0_SA_CRO~B.

    python .tools/xadj.py open --call-id <open-calls id> --body <submission.md> --by <serial>
    python .tools/xadj.py list [--state OPEN|RULED|ALL]
    python .tools/xadj.py show --id <XA id>
    python .tools/xadj.py rule --id <XA id> --by <serial> --ruling "<(a) ... because ...>" | --ruling-file <path>
    python .tools/xadj.py adjudicator             which box rules right now, and the measurement behind it
    python .tools/xadj.py --selftest              LAST line  XADJ-SELFTEST cases=<k>/<n> ok=<True|False>

THE SUBMISSION (the body file) must carry these headings, or `open` refuses it:
    ## Context / ## Position / ## Why it gave pause / ### Ambiguity / ### Out of pattern / ### Other solutions
THE TRANSPORT is S3, beside the open-calls cluster copy: s3://opal-313476888478-globgrph/fabric/xadj/v1/<XA id>.json
(schema "xadj/1"; every reader refuses a key it does not know). No bus line and no git lag.
THE RECORD is written by the adjudicating box only, one file per ruling, carried to every box by box-sync:
    org/critical_paths/cross_adjudication/<UTC stamp>_<XA id>.md   (the submission verbatim + the ruling)
THE ADJUDICATOR is measured, never chosen: the laptop, unless its open-calls scan heartbeat
(fabric/open-calls/v1/box=laptop/scan.json, written by .tools/open-calls-scan.py) is older than LAPTOP_DOWN_SEC or reads no
live CTO; then site Z. `rule` refuses on any other box, and on site Z while the laptop measures up.
`open` marks the call's row `escalation: {to: xadj, ref: <XA id>}`, so the box's scan stops nudging for it; the scan nudges
the originating CTO again once the file reads RULED, to close the row (`open-calls.py close ... --xadj <XA id>`).

Environment (tests only): OPAL_XADJ_LOCAL=<dir> replaces S3 with a directory; OPAL_XADJ_RECORD_ROOT replaces the record dir;
OPAL_STATE_ROOT is passed through to open-calls.py. Exit: 0 done, 1 refused, 2 usage, 3 store unreadable.
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import os
import re
import secrets
import sys
import tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(TOOLS)
SCHEMA = "xadj/1"
BUCKET = "opal-313476888478-globgrph"
PREFIX = "fabric/xadj/v1"
HB_PREFIX = "fabric/open-calls/v1"
KEYS = {"schema", "id", "call_id", "project", "subject", "scope_verdict", "from_device", "from_serial", "opened_at", "body",
        "state", "ruling"}
RULING_KEYS = {"at", "by", "device", "text", "record"}
STATES = ("OPEN", "RULED")
PRIMARY, BACKUP = "laptop", "sitez"
LAPTOP_DOWN_SEC = 1800
HEADINGS = ("## Context", "## Position", "## Why it gave pause", "### Ambiguity", "### Out of pattern", "### Other solutions")
ID_RE = re.compile(r"^XA-\d{8}T\d{6}Z-[0-9a-f]{4}$")
REC_DIR = "org/critical_paths/cross_adjudication"


class Refused(Exception):
    pass


def load_mod(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def now_dt() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


def stamp(dt: datetime.datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse(s: str) -> datetime.datetime:
    return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)


# ---------------------------------------------------------------- the store (S3, or a directory in tests)

def _local() -> str:
    return os.environ.get("OPAL_XADJ_LOCAL", "").strip()


def _s3():
    import boto3
    from botocore.config import Config
    return boto3.client("s3", config=Config(connect_timeout=5, read_timeout=15, retries={"max_attempts": 2}))


def _get(key: str):
    """The object's parsed JSON, or None when absent. Any other failure raises."""
    if _local():
        path = os.path.join(_local(), key.replace("/", os.sep))
        if not os.path.exists(path):
            return None
        return json.load(open(path, encoding="utf-8"))
    try:
        obj = _s3().get_object(Bucket=BUCKET, Key=key)
    except Exception as exc:  # noqa: BLE001
        code = ((getattr(exc, "response", None) or {}).get("Error") or {}).get("Code", "")
        if code in ("NoSuchKey", "404"):
            return None
        raise
    return json.loads(obj["Body"].read())


def _put(key: str, doc: dict) -> None:
    body = (json.dumps(doc, indent=1, ensure_ascii=True) + "\n").encode("ascii")
    if _local():
        path = os.path.join(_local(), key.replace("/", os.sep))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path + ".tmp", "wb") as fh:
            fh.write(body)
        os.replace(path + ".tmp", path)
        return
    _s3().put_object(Bucket=BUCKET, Key=key, Body=body, ContentType="application/json")


def _list_keys(prefix: str) -> list:
    if _local():
        d = os.path.join(_local(), prefix.replace("/", os.sep))
        if not os.path.isdir(d):
            return []
        return sorted("%s/%s" % (prefix, n) for n in os.listdir(d) if n.endswith(".json"))
    keys, token = [], None
    s3 = _s3()
    while True:
        kw = {"Bucket": BUCKET, "Prefix": prefix + "/"}
        if token:
            kw["ContinuationToken"] = token
        resp = s3.list_objects_v2(**kw)
        keys.extend(o["Key"] for o in resp.get("Contents", []) if o["Key"].endswith(".json"))
        if not resp.get("IsTruncated"):
            return sorted(keys)
        token = resp.get("NextContinuationToken")


def check(doc, where: str) -> dict:
    if not isinstance(doc, dict):
        raise Refused("%s: not an object" % where)
    unknown = sorted(set(doc) - KEYS)
    if unknown:
        raise Refused("%s: unknown key(s) %s (readers refuse a key they do not know)" % (where, ", ".join(unknown)))
    missing = sorted(KEYS - set(doc))
    if missing:
        raise Refused("%s: missing key(s) %s" % (where, ", ".join(missing)))
    if doc["schema"] != SCHEMA or doc["state"] not in STATES or not ID_RE.match(doc["id"]):
        raise Refused("%s: schema/state/id malformed" % where)
    r = doc["ruling"]
    if (doc["state"] == "RULED") != isinstance(r, dict) or (isinstance(r, dict) and set(r) != RULING_KEYS):
        raise Refused("%s: state %s does not match its ruling block" % (where, doc["state"]))
    return doc


def key_of(xid: str) -> str:
    return "%s/%s.json" % (PREFIX, xid)


def get(xid: str) -> dict:
    if not ID_RE.match(xid or ""):
        raise Refused("REFUSED: %r is not a cross-adjudication id (XA-<stamp>-<hex4>)" % xid)
    doc = _get(key_of(xid))
    if doc is None:
        raise Refused("REFUSED: no cross-adjudication file %s in the store" % xid)
    return check(doc, xid)


def list_all() -> list:
    return [check(_get(k), k) for k in _list_keys(PREFIX)]


def find_for_call(call_id: str):
    """The newest file naming this call, or None."""
    hits = [d for d in list_all() if d["call_id"] == call_id]
    return sorted(hits, key=lambda d: d["opened_at"])[-1] if hits else None


# ---------------------------------------------------------------- scan heartbeats and the adjudicator of record

def heartbeat_key(device: str) -> str:
    return "%s/box=%s/scan.json" % (HB_PREFIX, device)


def heartbeat_put(device: str, doc: dict) -> None:
    _put(heartbeat_key(device), doc)


def heartbeat_get(device: str):
    return _get(heartbeat_key(device))


def adjudicator(now: datetime.datetime | None = None) -> tuple:
    """(box, why). The laptop rules unless its scan heartbeat is stale or reads no live CTO; then site Z."""
    now = now or now_dt()
    hb = heartbeat_get(PRIMARY)
    if hb is None:
        return BACKUP, "laptop scan heartbeat ABSENT (%s)" % heartbeat_key(PRIMARY)
    age = (now - parse(hb["scanned_at"])).total_seconds()
    if age > LAPTOP_DOWN_SEC:
        return BACKUP, "laptop scan heartbeat %ds old (> %ds)" % (age, LAPTOP_DOWN_SEC)
    if not hb.get("cto_live"):
        return BACKUP, "laptop scan at %s reads no live CTO" % hb["scanned_at"]
    return PRIMARY, "laptop scan heartbeat %ds old, CTO %s live" % (age, hb.get("cto_serial"))


# ---------------------------------------------------------------- commands

def this_box() -> str:
    dev = load_mod("opal_devices", "lib/devices.py")
    name, basis = dev.this_device(dev.load())
    if name is None:
        raise Refused("ERROR: this box is unresolved: %s" % basis)
    return name


def oc_mod():
    return load_mod("opal_open_calls", ".tools/open-calls.py")


def cmd_open(args) -> int:
    device = this_box()
    body = open(args.body, encoding="utf-8").read()
    lacking = [h for h in HEADINGS if not re.search(r"^%s\s*$" % re.escape(h), body, re.M)]
    if lacking:
        raise Refused("REFUSED: the submission lacks heading(s) %s; a cross-adjudication file states its context, position and "
                      "why it gave pause (ambiguity, out of pattern, other solutions)" % ", ".join(lacking))
    oc = oc_mod()
    doc = oc.read_list(device)
    row = next((r for r in doc["rows"] if r["id"] == args.call_id), None)
    if row is None:
        raise Refused("REFUSED: no call %s on this box's list (%s)" % (args.call_id, oc.list_path(device)))
    if row["state"] != "OPEN":
        raise Refused("REFUSED: call %s is %s" % (args.call_id, row["state"]))
    if row.get("escalation"):
        raise Refused("REFUSED: call %s is already escalated (%s)" % (args.call_id, json.dumps(row["escalation"])))
    t = now_dt()
    xid = "XA-%s-%s" % (t.strftime("%Y%m%dT%H%M%SZ"), secrets.token_hex(2))
    xdoc = {"schema": SCHEMA, "id": xid, "call_id": row["id"], "project": row["project"], "subject": row["subject"],
            "scope_verdict": row["scope"].get("verdict", "?"), "from_device": device, "from_serial": args.by,
            "opened_at": stamp(t), "body": body, "state": "OPEN", "ruling": None}
    _put(key_of(xid), xdoc)
    oc.set_escalation(device, row["id"], {"to": "xadj", "ref": xid, "at": stamp(t), "by": args.by, "reason": None}, args.by)
    adj, why = adjudicator(t)
    print("XADJ-OPENED id=%s call=%s project=%s from=%s adjudicator=%s (%s)" % (xid, row["id"], row["project"], device, adj, why))
    return 0


def cmd_list(args) -> int:
    docs = list_all()
    want = args.state.upper()
    n = 0
    for d in sorted(docs, key=lambda d: d["opened_at"]):
        if want != "ALL" and d["state"] != want:
            continue
        n += 1
        tail = " ruled %s by %s on %s -> %s" % (d["ruling"]["at"], d["ruling"]["by"], d["ruling"]["device"],
                                               d["ruling"]["record"]) if d["ruling"] else ""
        print("%s [%s] %s %s call=%s from %s/%s opened %s | %s%s" % (d["id"], d["state"], d["project"], d["scope_verdict"],
                                                                    d["call_id"], d["from_device"], d["from_serial"],
                                                                    d["opened_at"], d["subject"][:120], tail))
    print("XADJ-LIST state=%s shown=%d total=%d" % (want, n, len(docs)))
    return 0


def cmd_show(args) -> int:
    d = get(args.id)
    print(render_record(d) if d["ruling"] else render_record(d, pending=True))
    return 0


def render_record(d: dict, pending: bool = False) -> str:
    out = ["# Cross-adjudication %s" % d["id"], "",
           "**Call:** %s (project %s, scope %s) on box %s" % (d["call_id"], d["project"], d["scope_verdict"], d["from_device"]),
           "**Subject:** %s" % d["subject"],
           "**Submitted by:** %s at %s" % (d["from_serial"], d["opened_at"]),
           "**State:** %s" % d["state"], "",
           "## Submission (verbatim)", "", d["body"].rstrip(), ""]
    if pending:
        out += ["## Ruling", "", "(pending)"]
    else:
        r = d["ruling"]
        out += ["## Ruling", "", "**Ruled by:** %s on box %s at %s" % (r["by"], r["device"], r["at"]), "", r["text"].rstrip()]
    return "\n".join(out) + "\n"


def record_root() -> str:
    return os.environ.get("OPAL_XADJ_RECORD_ROOT", "").strip() or os.path.join(ROOT, REC_DIR.replace("/", os.sep))


def cmd_rule(args) -> int:
    device = this_box()
    adj, why = adjudicator()
    if device != adj:
        raise Refused("REFUSED: box %s does not rule cross-adjudications now; the adjudicator is %s (%s)" % (device, adj, why))
    d = get(args.id)
    if d["state"] != "OPEN":
        raise Refused("REFUSED: %s is already %s" % (args.id, d["state"]))
    text = open(args.ruling_file, encoding="utf-8").read() if args.ruling_file else args.ruling
    if not (text or "").strip():
        raise Refused("REFUSED: an empty ruling is not a ruling")
    t = now_dt()
    os.makedirs(record_root(), exist_ok=True)
    name = "%s_%s.md" % (t.strftime("%Y%m%dT%H%MZ"), d["id"])
    rec_abs = os.path.join(record_root(), name)
    rec_rel = "%s/%s" % (REC_DIR, name)
    d["state"] = "RULED"
    d["ruling"] = {"at": stamp(t), "by": args.by, "device": device, "text": text, "record": rec_rel}
    with open(rec_abs, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(render_record(d))
    _put(key_of(d["id"]), d)
    print("XADJ-RULED id=%s call=%s by=%s on=%s record=%s" % (d["id"], d["call_id"], args.by, device, rec_rel))
    print("NEXT: commit the record with safe-commit (box-sync carries it); the %s box scan nudges its CTO to close %s." % (
        d["from_device"], d["call_id"]))
    return 0


def cmd_adjudicator(args) -> int:
    adj, why = adjudicator()
    print("XADJ-ADJUDICATOR box=%s why=%s" % (adj, why))
    return 0


# ---------------------------------------------------------------- selftest

SUBMISSION = ("## Context\nc\n## Position\n(a)\n## Why it gave pause\nw\n### Ambiguity\na\n### Out of pattern\no\n"
              "### Other solutions\ns\n")


def selftest() -> int:
    cases = []

    def rec(name, ok, detail=""):
        cases.append((name, bool(ok)))
        print("%s %s%s" % ("PASS" if ok else "FAIL", name, (" -- " + detail) if detail and not ok else ""))

    base = tempfile.mkdtemp(prefix="xadj_selftest_")
    keep = {k: os.environ.get(k) for k in ("OPAL_XADJ_LOCAL", "OPAL_XADJ_RECORD_ROOT")}
    os.environ["OPAL_XADJ_LOCAL"] = os.path.join(base, "store")
    os.environ["OPAL_XADJ_RECORD_ROOT"] = os.path.join(base, "records")
    try:
        t = now_dt()
        rec("no-heartbeat-means-backup", adjudicator(t)[0] == BACKUP)
        heartbeat_put(PRIMARY, {"scanned_at": stamp(t), "cto_live": True, "cto_serial": "1.0.0_SA_CTO"})
        rec("fresh-live-laptop-rules", adjudicator(t)[0] == PRIMARY)
        rec("stale-laptop-falls-to-sitez", adjudicator(t + datetime.timedelta(seconds=LAPTOP_DOWN_SEC + 60))[0] == BACKUP)
        heartbeat_put(PRIMARY, {"scanned_at": stamp(t), "cto_live": False, "cto_serial": None})
        rec("laptop-without-cto-falls-to-sitez", adjudicator(t)[0] == BACKUP)
        d = {"schema": SCHEMA, "id": "XA-20261009T000000Z-abcd", "call_id": "dell1-x", "project": "P", "subject": "s",
             "scope_verdict": "CROSS-BOX", "from_device": "dell1", "from_serial": "1.0.0_SA_CTO~DELL1",
             "opened_at": stamp(t), "body": SUBMISSION, "state": "OPEN", "ruling": None}
        _put(key_of(d["id"]), d)
        rec("round-trip-and-find", find_for_call("dell1-x")["id"] == d["id"] and find_for_call("nope") is None)
        bad = dict(d, extra=1)
        try:
            check(bad, "bad")
            rec("unknown-key-refused", False)
        except Refused:
            rec("unknown-key-refused", True)
        half = dict(d, state="RULED")
        try:
            check(half, "half")
            rec("ruled-without-ruling-refused", False)
        except Refused:
            rec("ruled-without-ruling-refused", True)
        lacking = [h for h in HEADINGS if not re.search(r"^%s\s*$" % re.escape(h), "## Context\n## Position\n", re.M)]
        rec("heading-check-names-the-missing", lacking == list(HEADINGS[2:]))
        r = dict(d, state="RULED", ruling={"at": stamp(t), "by": "1.0.0_SA_CTO", "device": "laptop", "text": "(a) yes",
                                           "record": REC_DIR + "/x.md"})
        rec("record-carries-submission-and-ruling", "### Out of pattern" in render_record(check(r, "r"))
            and "(a) yes" in render_record(r))
    finally:
        for k, v in keep.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        import shutil
        shutil.rmtree(base, ignore_errors=True)
    ok = all(c[1] for c in cases)
    print("XADJ-SELFTEST cases=%d/%d ok=%s" % (sum(1 for c in cases if c[1]), len(cases), ok))
    return 0 if ok else 1


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="xadj.py", description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    o = sub.add_parser("open", help="send this box's call to cross-adjudication")
    o.add_argument("--call-id", required=True)
    o.add_argument("--body", required=True)
    o.add_argument("--by", required=True)
    lst = sub.add_parser("list", help="every cross-adjudication file in the store")
    lst.add_argument("--state", default="ALL", choices=["OPEN", "RULED", "ALL", "open", "ruled", "all"])
    sh = sub.add_parser("show", help="one file, rendered as its record")
    sh.add_argument("--id", required=True)
    r = sub.add_parser("rule", help="rule an OPEN file (the adjudicating box only)")
    r.add_argument("--id", required=True)
    r.add_argument("--by", required=True)
    g = r.add_mutually_exclusive_group(required=True)
    g.add_argument("--ruling")
    g.add_argument("--ruling-file")
    sub.add_parser("adjudicator", help="which box rules now, and why")
    return ap


def main(argv: list) -> int:
    args = build_parser().parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.cmd:
        build_parser().print_help()
        return 2
    try:
        return {"open": cmd_open, "list": cmd_list, "show": cmd_show, "rule": cmd_rule,
                "adjudicator": cmd_adjudicator}[args.cmd](args)
    except Refused as exc:
        print(str(exc), file=sys.stderr)
        return 1 if str(exc).startswith("REFUSED") else 3


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
