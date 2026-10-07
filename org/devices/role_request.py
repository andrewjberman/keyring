"""role_request.py -- a Dell writes in for a role (NFRA_CTLPLN PRD v0.8 C-ROLE-REQUEST (a), cell CT-c-2).

A Dell never creates, edits or attaches policy to a role. When work placed on a Dell needs a role, the Dell WRITES IN: one request
naming the project, the resource the role is for, the service that assumes it and the permissions asked, each permission tied to the
code line that needs it. The laptop reads the request, writes the role in that project's Terraform root and applies it. This file is
the request's writer, validator and lister. Shape: org/standards/ROLE_REQUEST.schema.json (the request AND the laptop's answer).

    AGENTBUS_DEVICE=dell1 python org/devices/role_request.py write --project <CODE> --root <dir under infra/aws/terraform/>
        --kind <k> --name <n> --service <s> --permission <action>,<arn>,<path>:<line> [--permission ...] [--dry-run]
    python org/devices/role_request.py validate <file>   # LAST line: ROLE-REQUEST-VALID <request_id> ok=<True|False>
    python org/devices/role_request.py list [--status <s>] [--records <dir>]   # LAST line: COUNT requested=N applied=N refused=N ...
    AGENTBUS_DEVICE=laptop python org/devices/role_request.py mark-applied <record> --role-arn <arn> --commit <hash>
    AGENTBUS_DEVICE=laptop python org/devices/role_request.py mark-refused <record> --reason <text>   # the laptop's answer verbs (CT-c-4)

The Dell's record is org/devices/role_requests/<device>/<request_id>.json (a per-box directory: only that box writes there). The
laptop's answer is a SEPARATE file, org/devices/role_requests/<laptop device>/answers/<request_id>.json (one writer per file); the
effective status of a request is its answer's status when an answer file exists, else `requested`.

No AWS call, no IAM act. The only side effect of `write` is the record file and ONE bus line to the laptop (the bus send is injectable
so the tests record it instead). The box's own name is AGENTBUS_DEVICE, never derived from a path (LD-0405).
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import pathlib
import re
import secrets
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
SCHEMA_PATH = ROOT / "org" / "standards" / "ROLE_REQUEST.schema.json"
RECORDS_REL = "org/devices/role_requests"
TF_BASE = "infra/aws/terraform/"
ANSWER_STATUSES = ("applied", "refused")
ACCOUNT = "313476888478"
ROLE_ARN_RE = re.compile(r"^arn:aws:iam::%s:role/([A-Za-z0-9_+=,.@-]+)$" % ACCOUNT)   # a literal role name: no wildcard, no path


# ----------------------------------------------------------------------------------------------------- register and project

def load_register(root: pathlib.Path) -> dict:
    """The device register: OPAL_DEVICE_REGISTER when set (fixtures and proofs only), else <root>/org/devices/DEVICES.json."""
    override = os.environ.get("OPAL_DEVICE_REGISTER", "").strip()
    path = pathlib.Path(override) if override else root / "org" / "devices" / "DEVICES.json"
    return json.loads(path.read_text(encoding="utf-8"))


def find_device(reg: dict, label: str):
    want = (label or "").strip().lower()
    for d in reg.get("devices", []):
        if want in [d["name"].lower()] + [a.lower() for a in d.get("aliases", [])]:
            return d
    return None


def project_placement(root: pathlib.Path, code: str):
    """(placement or None, project.json path or None) for a project code, from org/missions/D*/*/<CODE>/project.json."""
    hits = sorted(root.glob("org/missions/D*/*/%s/project.json" % code))
    if not hits:
        return None, None
    try:
        return json.loads(hits[0].read_text(encoding="utf-8")).get("placement"), hits[0]
    except (OSError, ValueError):
        return None, hits[0]


# ----------------------------------------------------------------------------------------------------- schema (plain Python)

def _load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _check(node: dict, value, defs: dict, path: str, errs: list) -> None:
    """A small interpreter for the keyword subset ROLE_REQUEST.schema.json uses; jsonschema is not assumed."""
    if "$ref" in node:
        _check(defs[node["$ref"].rsplit("/", 1)[1]], value, defs, path, errs)
        return
    t = node.get("type")
    kinds = {"object": dict, "array": list, "string": str}
    if t and not isinstance(value, kinds[t]):
        errs.append("%s: expected %s" % (path or "<root>", t))
        return
    if "const" in node and value != node["const"]:
        errs.append("%s: must be %r, got %r" % (path, node["const"], value))
    if "enum" in node and value not in node["enum"]:
        errs.append("%s: must be one of %s, got %r" % (path, node["enum"], value))
    if isinstance(value, str):
        if len(value) < node.get("minLength", 0):
            errs.append("%s: empty" % path)
        if "pattern" in node and not re.search(node["pattern"], value):
            errs.append("%s: %r does not match %s" % (path, value, node["pattern"]))
    if isinstance(value, list):
        if len(value) < node.get("minItems", 0):
            errs.append("%s: needs at least %d item(s)" % (path, node["minItems"]))
        for i, item in enumerate(value):
            if "items" in node:
                _check(node["items"], item, defs, "%s[%d]" % (path, i), errs)
    if isinstance(value, dict):
        for k in node.get("required", []):
            if k not in value:
                errs.append("%s: missing required field %s" % (path or "<root>", k))
        props = node.get("properties", {})
        if node.get("additionalProperties") is False:
            for k in value:
                if k not in props:
                    errs.append("%s: unknown field %s" % (path or "<root>", k))
        for k, sub in props.items():
            if k in value:
                _check(sub, value[k], defs, "%s.%s" % (path, k) if path else k, errs)
        for rule in node.get("allOf", []):
            cond = rule.get("if", {})
            probe = []
            _check({"type": "object", "properties": cond.get("properties", {})}, value, defs, path, probe)
            if not probe and all(k in value for k in cond.get("properties", {})):
                _check(rule["then"], value, defs, path, errs)


def shape_errors(doc, which: str) -> list:
    """Schema errors of one document against $defs/<which> ('request' or 'answer'); [] = the shape holds."""
    schema = _load_schema()
    errs: list = []
    _check({"$ref": "#/$defs/" + which}, doc, schema["$defs"], "", errs)
    try:  # a second, independent reading when jsonschema is installed; the plain check above is the floor
        import jsonschema
        v = jsonschema.Draft202012Validator({"$ref": "#/$defs/" + which, "$defs": schema["$defs"]})
        for e in v.iter_errors(doc):
            errs.append("jsonschema: %s" % e.message)
    except ImportError:
        pass
    return errs


# ----------------------------------------------------------------------------------------------------- the refusals

def parse_code_ref(ref: str):
    """(path, line) of '<repo path>:<line>', or None when it is not that shape."""
    if ":" not in ref:
        return None
    path, _, line = ref.rpartition(":")
    return (path, int(line)) if path and line.isdigit() else None


def refusals(rec: dict, root: pathlib.Path, reg: dict) -> list:
    """The semantic refusals shared by `write` and `validate`; each is one sentence. [] = none."""
    out = []
    dev = find_device(reg, str(rec.get("device", "")))
    if dev is None:
        out.append("device %r is not in the device register" % rec.get("device"))
    else:
        if dev.get("role") != "execution":
            out.append("device %s has register role %r; only an `execution` box writes a role request" % (dev["name"], dev.get("role")))
        if rec.get("tailnet_name") != dev.get("tailnet_name"):
            out.append("tailnet_name %r is not %s's register tailnet name %r" % (rec.get("tailnet_name"), dev["name"], dev.get("tailnet_name")))
        placement, pj = project_placement(root, str(rec.get("project", "")))
        if pj is None:
            out.append("project %s has no org/missions/D*/*/%s/project.json" % (rec.get("project"), rec.get("project")))
        else:
            pdev = find_device(reg, str(placement or ""))
            if pdev is None or pdev["name"] != dev["name"]:
                out.append("project %s is placed on %s, not on %s; a box writes in only for work placed on it"
                           % (rec.get("project"), placement, dev["name"]))
    tf = str(rec.get("terraform_root", ""))
    parts = tf.split("/")
    if not tf.startswith(TF_BASE) or ".." in parts or not (root / tf).is_dir():
        out.append("terraform_root %r is not an existing directory under %s" % (tf, TF_BASE))
    for i, p in enumerate(rec.get("permissions") or []):
        action = str(p.get("action", ""))
        if action == "*" or action.split(":")[0] == "*":
            out.append("permission %d: action %r is a wildcard; ask for the named action" % (i, action))
        if action.lower().startswith("iam:"):
            out.append("permission %d: %r is an iam: action; a Dell never asks for access-changing permissions" % (i, action))
        ref = parse_code_ref(str(p.get("code_ref", "")))
        if ref is None:
            out.append("permission %d: code_ref %r is not <repo path>:<line>" % (i, p.get("code_ref")))
            continue
        rel, line = ref
        target = (root / rel).resolve()
        try:
            target.relative_to(root.resolve())
        except ValueError:
            out.append("permission %d: code_ref path %r is outside the repo" % (i, rel))
            continue
        if not target.is_file():
            out.append("permission %d: code_ref file %s does not exist" % (i, rel))
            continue
        n = len(target.read_text(encoding="utf-8", errors="replace").splitlines())
        if line < 1 or line > n:
            out.append("permission %d: code_ref line %d is outside %s (%d lines)" % (i, line, rel, n))
    return out


# ----------------------------------------------------------------------------------------------------- the bus

def bus_line(request_id: str, project: str, rec: dict, device: str) -> str:
    return "ROLE-REQUEST %s %s %s/%s %s/%s/%s.json" % (
        request_id, project, rec["resource"]["kind"], rec["resource"]["name"], RECORDS_REL, device, request_id)


def bus_send(root: pathlib.Path, to_device: str, from_serial: str, line: str):
    """The ONE live send, through the estate's agentbus script. Returns (rc, output). Tests replace this with a recorder."""
    sys.path.insert(0, str(root / ".tools"))
    import git_bash_resolver
    r = subprocess.run(git_bash_resolver.bash_argv(str(root / ".tools" / "agentbus-sqs.sh"), "send", to_device, from_serial, line),
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    return r.returncode, (r.stdout + r.stderr).strip()


# ----------------------------------------------------------------------------------------------------- verbs

def cmd_write(a, root: pathlib.Path, send) -> int:
    device_claim = os.environ.get("AGENTBUS_DEVICE", "").strip()
    if not device_claim:
        print("REFUSED: AGENTBUS_DEVICE is not set; a box's own name is its environment variable, never derived from a path", file=sys.stderr)
        return 2
    reg = load_register(root)
    dev = find_device(reg, device_claim)
    if dev is None:
        print("REFUSED: AGENTBUS_DEVICE=%s is not in the device register" % device_claim, file=sys.stderr)
        return 2
    perms, bad = [], []
    for raw in a.permission:
        bits = raw.split(",", 2)
        if len(bits) != 3 or not all(b.strip() for b in bits):
            bad.append("--permission %r is not <action>,<arn>,<path>:<line>" % raw)
            continue
        perms.append({"action": bits[0].strip(), "resource_arn": bits[1].strip(), "code_ref": bits[2].strip()})
    if bad:
        for m in bad:
            print("REFUSED: " + m, file=sys.stderr)
        return 2
    root_arg = a.root.strip().replace("\\", "/").strip("/")
    tf = root_arg if root_arg.startswith(TF_BASE) else TF_BASE + root_arg
    now = datetime.datetime.now(datetime.timezone.utc)
    rid = "%s-%s-%s" % (dev["name"], now.strftime("%Y%m%dT%H%M%SZ"), secrets.token_hex(2))
    rec = {
        "request_id": rid,
        "device": dev["name"],
        "tailnet_name": dev.get("tailnet_name", ""),
        "requested_by": os.environ.get("OPAL_AGENT_SERIAL", "").strip() or "device:" + dev["name"],
        "requested_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "project": a.project,
        "terraform_root": tf,
        "resource": {"kind": a.kind, "name": a.name},
        "assuming_service": a.service,
        "permissions": perms,
        "status": "requested",
    }
    problems = refusals(rec, root, reg) + shape_errors(rec, "request")
    if problems:
        for m in problems:
            print("REFUSED: " + m, file=sys.stderr)
        return 2
    laptop = next((d for d in reg["devices"] if d.get("role") == "control-plane"), None)
    if laptop is None:
        print("REFUSED: the device register holds no control-plane box to send the request to", file=sys.stderr)
        return 2
    line = bus_line(rid, a.project, rec, dev["name"])
    text = json.dumps(rec, indent=2)
    if a.dry_run:
        print("DRY-RUN: nothing written, nothing sent")
        print(text)
        print(line)
        return 0
    path = root / RECORDS_REL / dev["name"] / (rid + ".json")
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "x", encoding="utf-8", newline="\n") as fh:   # 'x': never overwrite a record
        fh.write(text + "\n")
    print(text)
    print(line)
    rc, out = send(root, laptop["name"], rec["requested_by"], line)
    if rc != 0:
        print("ERROR: the record is written at %s but the bus send to %s failed rc=%s: %s" % (path, laptop["name"], rc, out), file=sys.stderr)
        return 3
    return 0


def cmd_validate(a, root: pathlib.Path) -> int:
    rid, problems = "unreadable", []
    try:
        rec = json.loads(pathlib.Path(a.file).read_text(encoding="utf-8"))
        rid = rec.get("request_id", "missing") if isinstance(rec, dict) else "missing"
    except (OSError, ValueError) as exc:
        rec = None
        problems.append("cannot read %s: %s" % (a.file, exc))
    if rec is not None:
        problems += shape_errors(rec, "request")
        if isinstance(rec, dict) and not shape_errors(rec, "request"):
            if not str(rec["request_id"]).startswith(rec["device"] + "-"):
                problems.append("request_id %s does not begin with device %s-" % (rec["request_id"], rec["device"]))
            problems += refusals(rec, root, load_register(root))
    for m in problems:
        print("INVALID: " + m)
    print("ROLE-REQUEST-VALID %s ok=%s" % (rid, not problems))
    return 0 if not problems else 1


def effective_status(records: pathlib.Path, request_id: str) -> str:
    """The answer's status when an answer file exists under <records>/*/answers/<request_id>.json, else `requested`.
    An answer that does not hold the answer shape, or answers a different request, reads `answer-invalid`, never `requested`."""
    answers = sorted(records.glob("*/answers/%s.json" % request_id))
    if not answers:
        return "requested"
    try:
        ans = json.loads(answers[0].read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return "answer-invalid"
    if shape_errors(ans, "answer") or ans.get("request_id") != request_id:
        return "answer-invalid"
    return ans["status"]


def cmd_list(a, root: pathlib.Path) -> int:
    records = pathlib.Path(a.records) if a.records else root / RECORDS_REL
    counts = {"requested": 0, "applied": 0, "refused": 0}
    for f in sorted(records.glob("*/*.json")):
        try:
            rec = json.loads(f.read_text(encoding="utf-8"))
            rid = rec["request_id"]
            status = effective_status(records, rid)
            row = "%s %s %s %s/%s %s" % (rid, status, rec["project"], rec["resource"]["kind"], rec["resource"]["name"], rec["device"])
        except (OSError, ValueError, KeyError, TypeError):
            status, row = "unreadable", "%s unreadable" % f.as_posix()
        counts[status] = counts.get(status, 0) + 1
        if not a.status or a.status == status:
            print(row)
    total = sum(counts.values())
    print("COUNT " + " ".join("%s=%d" % (k, v) for k, v in counts.items()) + " total=%d" % total)
    return 0


# ----------------------------------------------------------------------------------------------------- THE ANSWER VERBS (CT-c-4)
# `mark-applied` and `mark-refused` are the LAPTOP's verbs. They write the ANSWER document ($defs/answer in ROLE_REQUEST.schema.json) to
# answer_path() below, one file per request, in the laptop's own directory; they never touch a Dell's record under
# <records>/<device>/<request_id>.json. `list` reads those answer files.

def answer_path(root: pathlib.Path, laptop_device: str, request_id: str) -> pathlib.Path:
    """Where the laptop's answer to a request lives: org/devices/role_requests/<laptop device>/answers/<request_id>.json."""
    return root / RECORDS_REL / laptop_device / "answers" / (request_id + ".json")


def _answer_setup(a, root: pathlib.Path):
    """(laptop device, request record) for an answer verb, or (None, message). Refuses unless AGENTBUS_DEVICE names the control-plane box."""
    claim = os.environ.get("AGENTBUS_DEVICE", "").strip()
    if not claim:
        return None, "AGENTBUS_DEVICE is not set; a box's own name is its environment variable, never derived from a path"
    dev = find_device(load_register(root), claim)
    if dev is None:
        return None, "AGENTBUS_DEVICE=%s is not in the device register" % claim
    if dev.get("role") != "control-plane":
        return None, "device %s has register role %r; only the `control-plane` box answers a role request" % (dev["name"], dev.get("role"))
    try:
        rec = json.loads(pathlib.Path(a.record).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return None, "cannot read request record %s: %s" % (a.record, exc)
    errs = shape_errors(rec, "request")
    if errs:
        return None, "request record %s does not hold the request shape: %s" % (a.record, "; ".join(errs[:3]))
    if pathlib.Path(a.record).stem != rec["request_id"]:
        return None, "request record file name %s is not its request_id %s" % (pathlib.Path(a.record).name, rec["request_id"])
    return (dev, rec), ""


def _write_answer(root: pathlib.Path, dev: dict, rec: dict, ans: dict) -> int:
    errs = shape_errors(ans, "answer")
    if errs:
        for m in errs:
            print("REFUSED: answer shape: " + m, file=sys.stderr)
        return 2
    path = answer_path(root, dev["name"], rec["request_id"])
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(path, "x", encoding="utf-8", newline="\n") as fh:   # 'x': one answer per request, never overwritten
            fh.write(json.dumps(ans, indent=2) + "\n")
    except FileExistsError:
        print("REFUSED: request %s already has an answer at %s" % (rec["request_id"], path), file=sys.stderr)
        return 2
    print(json.dumps(ans, indent=2))
    print("ROLE-REQUEST-ANSWER %s %s %s" % (rec["request_id"], ans["status"], path.relative_to(root).as_posix()))
    return 0


def cmd_mark_applied(a, root: pathlib.Path) -> int:
    got, msg = _answer_setup(a, root)
    if got is None:
        print("REFUSED: " + msg, file=sys.stderr)
        return 2
    dev, rec = got
    m = ROLE_ARN_RE.match(a.role_arn.strip())
    if not m:
        print("REFUSED: --role-arn %r is not arn:aws:iam::%s:role/<literal role name> (no wildcard, no path)" % (a.role_arn, ACCOUNT), file=sys.stderr)
        return 2
    now = datetime.datetime.now(datetime.timezone.utc)
    ans = {"request_id": rec["request_id"], "status": "applied", "role_name": m.group(1), "role_arn": a.role_arn.strip(),
           "applied_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
           "applied_by": os.environ.get("OPAL_AGENT_SERIAL", "").strip() or "device:" + dev["name"], "commit": a.commit.strip()}
    return _write_answer(root, dev, rec, ans)


def cmd_mark_refused(a, root: pathlib.Path) -> int:
    got, msg = _answer_setup(a, root)
    if got is None:
        print("REFUSED: " + msg, file=sys.stderr)
        return 2
    dev, rec = got
    now = datetime.datetime.now(datetime.timezone.utc)
    ans = {"request_id": rec["request_id"], "status": "refused", "reason": a.reason.strip(),
           "applied_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
           "applied_by": os.environ.get("OPAL_AGENT_SERIAL", "").strip() or "device:" + dev["name"]}
    return _write_answer(root, dev, rec, ans)


def main(argv=None, root: pathlib.Path = ROOT, send=bus_send) -> int:
    p = argparse.ArgumentParser(prog="role_request.py", description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="verb", required=True)
    w = sub.add_parser("write", help="write a request record and send one bus line to the laptop")
    w.add_argument("--project", required=True)
    w.add_argument("--root", required=True, help="the Terraform root, under infra/aws/terraform/")
    w.add_argument("--kind", required=True)
    w.add_argument("--name", required=True)
    w.add_argument("--service", required=True)
    w.add_argument("--permission", action="append", required=True, help="<action>,<arn>,<path>:<line>; repeatable")
    w.add_argument("--dry-run", action="store_true")
    v = sub.add_parser("validate", help="schema plus the writer's refusals")
    v.add_argument("file")
    ls = sub.add_parser("list", help="every request with its effective status")
    ls.add_argument("--status")
    ls.add_argument("--records")
    ma = sub.add_parser("mark-applied", help="the laptop answers a request: the role is applied")
    ma.add_argument("record")
    ma.add_argument("--role-arn", required=True)
    ma.add_argument("--commit", required=True)
    mr = sub.add_parser("mark-refused", help="the laptop answers a request: refused, with the reason")
    mr.add_argument("record")
    mr.add_argument("--reason", required=True)
    a = p.parse_args(argv)
    root = pathlib.Path(root)
    if a.verb == "write":
        return cmd_write(a, root, send)
    if a.verb == "validate":
        return cmd_validate(a, root)
    if a.verb == "mark-applied":
        return cmd_mark_applied(a, root)
    if a.verb == "mark-refused":
        return cmd_mark_refused(a, root)
    return cmd_list(a, root)


if __name__ == "__main__":
    sys.exit(main())
