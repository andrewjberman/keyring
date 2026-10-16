#!/usr/bin/env python3
"""crossbox-call.py -- a cross-box call or order travels as a FILE with an acknowledgement from the other side, and is
closed on both boxes or on neither (NFRA_CTLPLN workstream SEATS, cell CT-s-6; C-SEATS clauses 5 and 6).

WHAT THIS TOOL IS NOT. It does not send on the agent bus, it does not change the bus script, the consumer, the broker or
the manager-to-Tier-2 hook. It PRINTS the one line a box's manager puts on the bus with the existing
`bash .tools/agentbus-sqs.sh send <device> ...`, and it READS the line the consumer prints on the other box. The line
carries an id and a path, never the substance: the substance is a committed file the other box reads by pulling.

`receive` DELIVERS the order to the named seat by writing ONE file into that seat's broker inbox directory on its OWN box,
in the form `org/mcp/server.py` `_deliver_to_one` writes (the watcher `org/mcp/inbox-watch.sh` reads `*.md` in that
directory). That is a tool writing a file for a seat on its own box, NOT a manager sending a message, so the bar that keeps
a manager from messaging a Tier-2 seat (`.tools/hooks/mstr-no-tier2-writes.sh`) is not in play and is not touched.

  python .tools/crossbox-call.py open --kind CALL|ORDER --to-device <d> --to-serial <s> --from-serial <s> --subject <t> --body <path> [--call-id <id>]
  python .tools/crossbox-call.py line --id <id>                    the bus line, once the file AND its body are committed and on origin
  python .tools/crossbox-call.py issue --order <task-order path> [--to-device <d>]   open the file for an addressee on another box
  python .tools/crossbox-call.py send-pending [--dry-run]          a 0.0.0_AB_MSTR serial only: send every admitted OPEN file on the bus
  python .tools/crossbox-call.py sent --id <id> --bus-message-id <id>
  python .tools/crossbox-call.py receive --line "<line as the consumer printed it>"
  python .tools/crossbox-call.py ack --id <id> --by <serial>       prints  CROSSBOX-ACK <id> READ by <serial> at <UTC>
  python .tools/crossbox-call.py acked --id <id> --line "<reply line>" --bus-message-id <id>
  python .tools/crossbox-call.py close --id <id> --side from|to --by <serial>
  python .tools/crossbox-call.py status --id <id>
  python .tools/crossbox-call.py list [--open]
  python .tools/crossbox-call.py merge --id <id> --ref <git ref>   fold the other box's copy of the file into this one
  python .tools/crossbox-call.py --selftest                        LAST line  CROSSBOX-SELFTEST cases=<k>/<n> ok=<True|False>

THE FILE: org/devices/crossbox/<id>.json, JSON, ASCII, every reader refuses a key it does not know. Keys: schema
("crossbox/1"), id, kind (CALL|ORDER), call_id (the open-calls id a CALL settles, or null -- the EXPLICIT link
`.tools/open-calls.py close` finds), from_device, to_device, from_serial, to_serial, subject, body_path, opened_at, state
(OPEN|ACKED|CLOSED-BOTH, always recomputed from the fields below), sent {at, bus_message_id}, ack null|{at, by,
bus_message_id}, closed {from_at, from_by, to_at, to_by}. Each box writes only its own fields (the sending box: sent, the
bus id inside ack, closed.from_*; the receiving box: ack.at/by, closed.to_*), and `merge` folds the other copy in, so
the two copies reach CLOSED-BOTH by git carrying the file and never by one box writing the other's.

LAYOUT 2 (schema crossbox/2; CT-ba-1, NFRA_CTLPLN round 29, the CTO's ruling 1 @round-28 analysis): the two sides of a call
write two FILES, so a from-side write and an answer write never share a file and cannot conflict in box-sync. The
from-side file XB-<id>.json carries the from-side fields only (no state: derived): sent, ack_bus_message_id (the bus id of
the answer), closed_from, and closed_to_issuer (written only by the issuing box's withdraw or supersede). Each answering
box writes XB-<id>.<box>.json, schema crossbox-answer/1: ack and closed_to. The reader assembles the two into the crossbox/1
shape (load_call_path, assemble), so every reader of a call sees one record. The layout is chosen by the committed text
file org/devices/crossbox/LAYOUT (first line 2) at `open`; a crossbox/1 call keeps the single file and every writer on it
behaves as before. `merge` on a crossbox/2 call writes nothing: each side already wrote its own file.

The box is this checkout (--root, default: the repository this script lives in) and its device is AGENTBUS_DEVICE resolved
through lib/devices.py (--device overrides it: tests only). Exit codes: 0 done, 2 usage, 3 REFUSED, 5 PULL-FIRST.
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import json
import os
import re
import shlex
import shutil
import stat
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL_ROOT = HERE.parent
SCHEMA = "crossbox/1"
SCHEMA2 = "crossbox/2"
SCHEMA_ANS = "crossbox-answer/1"
REL_DIR = "org/devices/crossbox"
LAYOUT_FILE = "LAYOUT"
KEYS = ["schema", "id", "kind", "call_id", "from_device", "to_device", "from_serial", "to_serial", "subject", "body_path",
        "opened_at", "state", "sent", "ack", "closed"]
FROM2_KEYS = ["schema", "id", "kind", "call_id", "from_device", "to_device", "from_serial", "to_serial", "subject", "body_path",
              "opened_at", "sent", "ack_bus_message_id", "closed_from", "closed_to_issuer"]
ANS_KEYS = ["schema", "id", "box", "ack", "closed_to"]
ANS_ACK_KEYS = ["at", "by"]
PAIR_KEYS = ["at", "by"]
SENT_KEYS = ["at", "bus_message_id"]
ACK_KEYS = ["at", "by", "bus_message_id"]
CLOSED_KEYS = ["from_at", "from_by", "to_at", "to_by"]
BOX_RE = re.compile(r"[a-z0-9][a-z0-9_-]*")
ANSWER_RE = re.compile(r"(XB-\d{8}T\d{6}Z-[0-9a-f]{4})\.([a-z0-9][a-z0-9_-]*)\.json")
KINDS = ("CALL", "ORDER")
STATES = ("OPEN", "ACKED", "CLOSED-BOTH")
TIERS = ("tier0_exec", "tier0_utility", "tier1_exec", "tier2_senior", "tier3_junior")   # inbox-watch.sh and server.py TIER_DIRS
ID_RE = re.compile(r"XB-\d{8}T\d{6}Z-[0-9a-f]{4}")
SERIAL_RE = re.compile(r"\d+\.\d+\.\d+_[A-Za-z]+_[A-Za-z0-9_]+(?:~[A-Za-z0-9]+)?")
CALLID_RE = re.compile(r"[A-Za-z0-9._-]+")
BUSID_RE = re.compile(r"[0-9A-Za-z-]+")
LINE_RE = re.compile(r"CROSSBOX (XB-\d{8}T\d{6}Z-[0-9a-f]{4}) (CALL|ORDER) for (\S+): (.+?) \| file (org/devices/crossbox/\S+\.json) @([0-9a-f]{7,40})")
ACK_RE = re.compile(r"CROSSBOX-ACK (XB-\d{8}T\d{6}Z-[0-9a-f]{4}) READ by (\S+) at (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)")
UTC_FMT = "%Y-%m-%dT%H:%M:%SZ"


class Refused(Exception):
    pass


class PullFirst(Exception):
    pass


# ---------------------------------------------------------------- small helpers

def now_dt() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)


def stamp(dt: datetime.datetime) -> str:
    return dt.strftime(UTC_FMT)


def parse_utc(text) -> datetime.datetime | None:
    try:
        return datetime.datetime.strptime(str(text), UTC_FMT).replace(tzinfo=datetime.timezone.utc)
    except ValueError:
        return None


def age_text(text, now: datetime.datetime | None = None) -> str:
    then = parse_utc(text)
    if then is None:
        return "age unknown"
    secs = int(((now or now_dt()) - then).total_seconds())
    if secs < 90:
        return "%d s ago" % max(secs, 0)
    mins = secs // 60
    if mins < 120:
        return "%d min ago" % mins
    hours = mins // 60
    if hours < 48:
        return "%d h %d min ago" % (hours, mins % 60)
    return "%d d ago" % (hours // 24)


def base_of(serial: str) -> str:
    return serial.split("~")[0]


def devmod():
    """lib/devices.py of THIS script's repository -- the one reader of the device register."""
    spec = importlib.util.spec_from_file_location("opal_devices_cb", TOOL_ROOT / "lib" / "devices.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def git(root: Path, *args, extra_env=None, cwd=None):
    env = dict(os.environ)
    env.update(extra_env or {})
    proc = subprocess.run(["git", "-C", str(cwd or root), *args], capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=60, env=env)
    return proc.returncode, proc.stdout, proc.stderr


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    os.replace(tmp, path)


def check_ascii(text: str, what: str) -> None:
    if not text.isascii():
        raise Refused("%s holds non-ASCII text" % what)


# ---------------------------------------------------------------- the file

def check_call(doc, where: str) -> dict:
    """Validate a cross-box file's shape. A key this reader does not know is REFUSED."""
    if not isinstance(doc, dict):
        raise Refused("%s: top level is not an object" % where)
    unknown = sorted(set(doc) - set(KEYS))
    if unknown:
        raise Refused("%s: unknown key(s) %s (readers refuse a key they do not know)" % (where, ", ".join(unknown)))
    missing = [k for k in KEYS if k not in doc]
    if missing:
        raise Refused("%s: missing key(s) %s" % (where, ", ".join(missing)))
    if doc["schema"] not in (SCHEMA, SCHEMA2):
        raise Refused("%s: schema is %r, this reader reads %r and %r" % (where, doc["schema"], SCHEMA, SCHEMA2))
    if not (isinstance(doc["id"], str) and ID_RE.fullmatch(doc["id"])):
        raise Refused("%s: id %r is not an XB-<UTC>-<4 hex> id" % (where, doc["id"]))
    if doc["kind"] not in KINDS:
        raise Refused("%s: kind %r is not one of %s" % (where, doc["kind"], "/".join(KINDS)))
    if doc["call_id"] is not None and not (isinstance(doc["call_id"], str) and CALLID_RE.fullmatch(doc["call_id"])):
        raise Refused("%s: call_id must be null or a plain id" % where)
    for key in ("from_device", "to_device", "subject", "body_path", "opened_at"):
        if not (isinstance(doc[key], str) and doc[key]):
            raise Refused("%s: %s must be a non-empty string" % (where, key))
    for key in ("from_serial", "to_serial"):
        if not (isinstance(doc[key], str) and SERIAL_RE.fullmatch(doc[key])):
            raise Refused("%s: %s %r is not a serial" % (where, key, doc[key]))
    if doc["state"] not in STATES:
        raise Refused("%s: state %r is not one of %s" % (where, doc["state"], "/".join(STATES)))
    for key, allowed, nullable in (("sent", SENT_KEYS, False), ("ack", ACK_KEYS, True), ("closed", CLOSED_KEYS, False)):
        block = doc[key]
        if block is None and nullable:
            continue
        if not isinstance(block, dict):
            raise Refused("%s: %s must be an object%s" % (where, key, " or null" if nullable else ""))
        odd = sorted(set(block) - set(allowed))
        short = [k for k in allowed if k not in block]
        if odd or short:
            raise Refused("%s: %s has unknown key(s) %s / missing key(s) %s" % (where, key, ", ".join(odd) or "none", ", ".join(short) or "none"))
    check_ascii(json.dumps(doc), where)
    return doc


def derive_state(doc: dict) -> str:
    if doc["closed"]["from_at"] and doc["closed"]["to_at"]:
        return "CLOSED-BOTH"
    return "ACKED" if doc["ack"] and doc["ack"]["at"] else "OPEN"


def dump(doc: dict) -> str:
    doc["state"] = derive_state(doc)
    ordered = {k: doc[k] for k in KEYS}
    return json.dumps(ordered, indent=1, ensure_ascii=True) + "\n"


def fmt_line(doc: dict, commit: str) -> str:
    return "CROSSBOX %s %s for %s: %s | file %s/%s.json @%s" % (
        doc["id"], doc["kind"], doc["to_serial"], doc["subject"], REL_DIR, doc["id"], commit)


# ---------------------------------------------------------------- layout 2: one writer per side (CT-ba-1)

def layout_switch(root) -> bool:
    """True when the committed text file org/devices/crossbox/LAYOUT exists and its first line is 2. Absent, `open` writes
    crossbox/1 exactly as before."""
    path = Path(root) / REL_DIR / LAYOUT_FILE
    if not path.is_file():
        return False
    lines = path.read_text(encoding="utf-8").splitlines()
    return bool(lines) and lines[0].strip() == "2"


def answer_name(call_id: str, box: str) -> str:
    return "%s.%s.json" % (call_id, box)


def _pair(value, keys, where: str, name: str) -> None:
    """A {at, by} block: exactly these keys, each null or a non-empty string."""
    if not isinstance(value, dict) or sorted(value) != sorted(keys):
        raise Refused("%s: %s must be an object with exactly the keys %s" % (where, name, ", ".join(keys)))
    for key in keys:
        if value[key] is not None and not (isinstance(value[key], str) and value[key]):
            raise Refused("%s: %s.%s must be null or a non-empty string" % (where, name, key))


def check_from2(doc, where: str) -> dict:
    """The from-side file of a crossbox/2 call. A key this reader does not know is REFUSED."""
    if not isinstance(doc, dict):
        raise Refused("%s: top level is not an object" % where)
    unknown = sorted(set(doc) - set(FROM2_KEYS))
    if unknown:
        raise Refused("%s: unknown key(s) %s (readers refuse a key they do not know)" % (where, ", ".join(unknown)))
    missing = [k for k in FROM2_KEYS if k not in doc]
    if missing:
        raise Refused("%s: missing key(s) %s" % (where, ", ".join(missing)))
    if doc["schema"] != SCHEMA2:
        raise Refused("%s: schema is %r, the crossbox/2 from-side reader reads %r" % (where, doc["schema"], SCHEMA2))
    if not (isinstance(doc["id"], str) and ID_RE.fullmatch(doc["id"])):
        raise Refused("%s: id %r is not an XB-<UTC>-<4 hex> id" % (where, doc["id"]))
    if doc["kind"] not in KINDS:
        raise Refused("%s: kind %r is not one of %s" % (where, doc["kind"], "/".join(KINDS)))
    if doc["call_id"] is not None and not (isinstance(doc["call_id"], str) and CALLID_RE.fullmatch(doc["call_id"])):
        raise Refused("%s: call_id must be null or a plain id" % where)
    for key in ("from_device", "to_device", "subject", "body_path", "opened_at"):
        if not (isinstance(doc[key], str) and doc[key]):
            raise Refused("%s: %s must be a non-empty string" % (where, key))
    for key in ("from_serial", "to_serial"):
        if not (isinstance(doc[key], str) and SERIAL_RE.fullmatch(doc[key])):
            raise Refused("%s: %s %r is not a serial" % (where, key, doc[key]))
    _pair(doc["sent"], SENT_KEYS, where, "sent")
    if doc["ack_bus_message_id"] is not None and not (isinstance(doc["ack_bus_message_id"], str) and BUSID_RE.fullmatch(doc["ack_bus_message_id"])):
        raise Refused("%s: ack_bus_message_id must be null or a bus message id" % where)
    _pair(doc["closed_from"], PAIR_KEYS, where, "closed_from")
    _pair(doc["closed_to_issuer"], PAIR_KEYS, where, "closed_to_issuer")
    check_ascii(json.dumps(doc), where)
    return doc


def check_answer(doc, where: str) -> dict:
    """An answer file XB-<id>.<box>.json (crossbox-answer/1)."""
    if not isinstance(doc, dict):
        raise Refused("%s: top level is not an object" % where)
    unknown = sorted(set(doc) - set(ANS_KEYS))
    if unknown:
        raise Refused("%s: unknown key(s) %s (readers refuse a key they do not know)" % (where, ", ".join(unknown)))
    missing = [k for k in ANS_KEYS if k not in doc]
    if missing:
        raise Refused("%s: missing key(s) %s" % (where, ", ".join(missing)))
    if doc["schema"] != SCHEMA_ANS:
        raise Refused("%s: schema is %r, the answer reader reads %r" % (where, doc["schema"], SCHEMA_ANS))
    if not (isinstance(doc["id"], str) and ID_RE.fullmatch(doc["id"])):
        raise Refused("%s: id %r is not an XB-<UTC>-<4 hex> id" % (where, doc["id"]))
    if not (isinstance(doc["box"], str) and BOX_RE.fullmatch(doc["box"])):
        raise Refused("%s: box %r is not a device name" % (where, doc["box"]))
    if doc["ack"] is not None and not (isinstance(doc["ack"], dict) and sorted(doc["ack"]) == sorted(ANS_ACK_KEYS)
                                       and all(isinstance(doc["ack"][k], str) and doc["ack"][k] for k in ANS_ACK_KEYS)):
        raise Refused("%s: ack must be null or an object with at and by" % where)
    _pair(doc["closed_to"], PAIR_KEYS, where, "closed_to")
    check_ascii(json.dumps(doc), where)
    return doc


def assemble(raw: dict, ans, where: str) -> dict:
    """The crossbox/1 shape of a crossbox/2 call: the from-side file (raw) and its answer file (ans, or None when this copy
    has none yet). ack is the answer's ack with the from-side bus id; closed.to_* is the answer's closed_to, or the issuing
    box's closed_to_issuer when the answer has not closed. state is derived, as derive_state does for crossbox/1."""
    check_from2(raw, where)
    if ans is not None:
        check_answer(ans, where + " (answer)")
        if ans["id"] != raw["id"] or ans["box"] != raw["to_device"]:
            raise Refused("%s: its answer file names %s on %s; this call is answered by %s" % (
                where, ans["id"], ans["box"], raw["to_device"]))
    ack = None
    if ans is not None and ans["ack"]:
        ack = {"at": ans["ack"]["at"], "by": ans["ack"]["by"], "bus_message_id": raw["ack_bus_message_id"]}
    to_pair = ans["closed_to"] if (ans is not None and ans["closed_to"]["at"]) else raw["closed_to_issuer"]
    doc = {"schema": raw["schema"], "id": raw["id"], "kind": raw["kind"], "call_id": raw["call_id"],
           "from_device": raw["from_device"], "to_device": raw["to_device"], "from_serial": raw["from_serial"],
           "to_serial": raw["to_serial"], "subject": raw["subject"], "body_path": raw["body_path"],
           "opened_at": raw["opened_at"], "state": "OPEN", "sent": dict(raw["sent"]), "ack": ack,
           "closed": {"from_at": raw["closed_from"]["at"], "from_by": raw["closed_from"]["by"],
                      "to_at": to_pair["at"], "to_by": to_pair["by"]}}
    doc["state"] = derive_state(doc)
    return check_call(doc, where)


def dump2_from(raw: dict) -> str:
    check_from2(raw, "from-side file %s" % raw.get("id"))
    return json.dumps({k: raw[k] for k in FROM2_KEYS}, indent=1, ensure_ascii=True) + "\n"


def dump_answer(ans: dict) -> str:
    check_answer(ans, "answer file %s" % ans.get("id"))
    return json.dumps({k: ans[k] for k in ANS_KEYS}, indent=1, ensure_ascii=True) + "\n"


def refuse_unknown_schema(raw, where: str) -> None:
    """The schema is read FIRST by the layout-aware loaders, so an unknown schema is named as one, not as a key."""
    if isinstance(raw, dict) and raw.get("schema") not in (SCHEMA, SCHEMA2):
        raise Refused("%s: schema is %r, this reader reads %r and %r" % (where, raw.get("schema"), SCHEMA, SCHEMA2))


def load_call_text(text: str, where: str, answer_text=None) -> dict:
    """One call from its text: a crossbox/1 file is checked as before; a crossbox/2 from-side file is assembled with the
    answer text given (None: this copy holds no answer yet)."""
    raw = json.loads(text)
    refuse_unknown_schema(raw, where)
    if isinstance(raw, dict) and raw.get("schema") == SCHEMA2:
        return assemble(raw, None if answer_text is None else json.loads(answer_text), where)
    return check_call(raw, where)


def load_call_path(path: Path, where: str) -> dict:
    """One call from its from-side (or crossbox/1) file on disk; a crossbox/2 file's answer file is read beside it."""
    text = path.read_text(encoding="utf-8")
    raw = json.loads(text)
    refuse_unknown_schema(raw, where)
    if not (isinstance(raw, dict) and raw.get("schema") == SCHEMA2):
        return check_call(raw, where)
    check_from2(raw, where)
    apath = path.with_name(answer_name(raw["id"], raw["to_device"]))
    return load_call_text(text, where, apath.read_text(encoding="utf-8") if apath.is_file() else None)


def fold_texts(texts: dict) -> list:
    """Every call in one folder, given {file name: text}: one (name, record, error) per call, sorted by name. A crossbox/2
    from-side file is assembled with the answer file named for its to_device; a crossbox/1 record is returned as parsed (the
    consumers read it as they always did). An answer file that no from-side file claims is an error entry, never ignored."""
    out, claimed = [], set()
    for name in sorted(texts):
        if ANSWER_RE.fullmatch(name) or not name.endswith(".json"):
            continue
        try:
            raw = json.loads(texts[name])
            if isinstance(raw, dict) and raw.get("schema") == SCHEMA2:
                check_from2(raw, name)
                an = answer_name(raw["id"], raw["to_device"])
                if an in texts:
                    claimed.add(an)
                out.append((name, load_call_text(texts[name], name, texts.get(an)), None))
            else:
                out.append((name, raw, None))
        except ValueError as exc:
            out.append((name, None, "%s: %s" % (type(exc).__name__, exc)))
        except Refused as exc:
            out.append((name, None, str(exc)))
    for name in sorted(texts):
        if ANSWER_RE.fullmatch(name) and name not in claimed:
            out.append((name, None, "an answer file that no from-side file of its box claims (the from-side file is absent or names another box)"))
    return sorted(out, key=lambda e: e[0])


def fold_dir(cdir) -> list:
    """fold_texts over the *.json files of one folder (an absent folder holds no calls)."""
    cdir = Path(cdir)
    if not cdir.is_dir():
        return []
    texts, errs = {}, []
    for p in sorted(cdir.glob("*.json")):
        try:
            texts[p.name] = p.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errs.append((p.name, None, "unreadable (%s: %s)" % (type(exc).__name__, exc)))
    return sorted(fold_texts(texts) + errs, key=lambda e: e[0])


# ---------------------------------------------------------------- the box

class Box:
    """One checkout (root) on one device. Every method returns a list of output lines or raises Refused / PullFirst."""

    def __init__(self, root, device: str | None = None):
        self.root = Path(root)
        if device is None:
            dev = devmod()
            device, basis = dev.this_device()
            if device is None:
                raise Refused("this box is unresolved: %s" % basis)
        self.device = device

    # -- paths and git
    def rel(self, call_id: str) -> str:
        return "%s/%s.json" % (REL_DIR, call_id)

    def path(self, call_id: str) -> Path:
        return self.root / REL_DIR / ("%s.json" % call_id)

    def tracked_clean(self, rel: str) -> tuple:
        rc, _, _ = git(self.root, "ls-files", "--error-unmatch", "--", rel)
        if rc != 0:
            return False, "is not tracked by git"
        rc, out, _ = git(self.root, "status", "--porcelain", "--", rel)
        if rc != 0 or out.strip():
            return False, "has uncommitted changes"
        return True, ""

    def last_commit(self, rel: str) -> str:
        rc, out, _ = git(self.root, "log", "-1", "--format=%h", "--", rel)
        return out.strip() if rc == 0 else ""

    def read(self, call_id: str) -> dict:
        """The call in the crossbox/1 shape, whichever layout its files are in (the one reader)."""
        if not ID_RE.fullmatch(call_id or ""):
            raise Refused("%r is not a cross-box id" % call_id)
        path = self.path(call_id)
        if not path.is_file():
            raise Refused("no cross-box file %s in this tree (pull the commit that holds it first)" % self.rel(call_id))
        try:
            return load_call_path(path, self.rel(call_id))
        except ValueError as exc:
            raise Refused("%s is not JSON (%s)" % (self.rel(call_id), exc))

    def save(self, doc: dict) -> None:
        write_text(self.path(doc["id"]), dump(doc))

    # -- layout 2: each side's own file
    def layout2(self, call_id: str) -> bool:
        """True when this call's from-side file is crossbox/2. The one reader runs first, so an unreadable call refuses here."""
        self.read(call_id)
        return json.loads(self.path(call_id).read_text(encoding="utf-8")).get("schema") == SCHEMA2

    def from_raw(self, call_id: str) -> dict:
        """The from-side file of a crossbox/2 call as written (checked by check_from2)."""
        return check_from2(json.loads(self.path(call_id).read_text(encoding="utf-8")), self.rel(call_id))

    def answer_raw(self, call_id: str, box: str):
        """This box's answer file for the call as written, or None when it has not written one yet."""
        path = self.root / REL_DIR / answer_name(call_id, box)
        if not path.is_file():
            return None
        return check_answer(json.loads(path.read_text(encoding="utf-8")), "%s/%s" % (REL_DIR, answer_name(call_id, box)))

    def save_from2(self, raw: dict) -> None:
        write_text(self.path(raw["id"]), dump2_from(raw))

    def save_answer(self, ans: dict) -> None:
        write_text(self.root / REL_DIR / answer_name(ans["id"], ans["box"]), dump_answer(ans))

    def need_box(self, doc: dict, key: str, what: str) -> None:
        if doc[key] != self.device:
            raise Refused("%s runs on the %s box (%s); this box is %s" % (what, "sending" if key == "from_device" else "receiving",
                                                                         doc[key], self.device))

    # -- open / line / sent
    def open(self, kind, to_device, to_serial, from_serial, subject, body, call_id=None) -> list:
        dev = devmod()
        if kind not in KINDS:
            raise Refused("--kind must be CALL or ORDER")
        target = dev.resolve(to_device)
        if target is None:
            raise Refused("--to-device %r is not in the device register (holds: %s)" % (to_device, ", ".join(dev.names())))
        if target == self.device:
            raise Refused("--to-device %s is this box; a cross-box file travels to ANOTHER box" % target)
        for what, serial in (("--to-serial", to_serial), ("--from-serial", from_serial)):
            if not SERIAL_RE.fullmatch(serial or ""):
                raise Refused("%s %r is not a serial" % (what, serial))
        subject = (subject or "").strip()
        if not subject or "|" in subject or "\n" in subject or len(subject) > 120:
            raise Refused("--subject must be one line of 1 to 120 characters without '|'")
        check_ascii(subject, "--subject")
        if call_id is not None and not CALLID_RE.fullmatch(call_id):
            raise Refused("--call-id %r is not a plain id" % call_id)
        rel = str(body or "").replace("\\", "/")
        if not rel or rel.startswith("/") or ".." in rel.split("/") or re.match(r"[A-Za-z]:", rel):
            raise Refused("--body must be a path inside the repository, relative to its root")
        if not (self.root / rel).is_file():
            raise Refused("--body %s is not a file in this tree" % rel)
        ok, why = self.tracked_clean(rel)
        if not ok:
            raise Refused("--body %s %s; the other box reads it by pulling the commit, so an uncommitted body is unreadable there. Commit it first." % (rel, why))
        now = now_dt()
        doc = {"schema": SCHEMA, "id": "XB-%s-%s" % (now.strftime("%Y%m%dT%H%M%SZ"), os.urandom(2).hex()), "kind": kind,
               "call_id": call_id, "from_device": self.device, "to_device": target, "from_serial": from_serial,
               "to_serial": to_serial, "subject": subject, "body_path": rel, "opened_at": stamp(now), "state": "OPEN",
               "sent": {"at": None, "bus_message_id": None}, "ack": None,
               "closed": {"from_at": None, "from_by": None, "to_at": None, "to_by": None}}
        check_call(doc, "new file")
        if self.path(doc["id"]).exists():
            raise Refused("%s already exists" % self.rel(doc["id"]))
        if layout_switch(self.root):
            # layout 2: the from-side file only, with the from-side fields (state is derived by the reader, never stored)
            doc = {"schema": SCHEMA2, "id": doc["id"], "kind": kind, "call_id": call_id, "from_device": self.device,
                   "to_device": target, "from_serial": from_serial, "to_serial": to_serial, "subject": subject, "body_path": rel,
                   "opened_at": doc["opened_at"], "sent": {"at": None, "bus_message_id": None}, "ack_bus_message_id": None,
                   "closed_from": {"at": None, "by": None}, "closed_to_issuer": {"at": None, "by": None}}
            self.save_from2(doc)
        else:
            self.save(doc)
        return ["OPENED %s (%s, %s -> %s)" % (doc["id"], kind, self.device, target),
                fmt_line(doc, "UNCOMMITTED"),
                "NEXT: commit %s (with the body already committed), then `python .tools/crossbox-call.py line --id %s` prints the "
                "same line with the commit the other box pulls; THAT line goes on the bus, and the substance never does." % (
                    self.rel(doc["id"]), doc["id"])]

    def line(self, call_id: str) -> list:
        doc = self.read(call_id)
        self.need_box(doc, "from_device", "line")
        rel = self.rel(call_id)
        ok, why = self.tracked_clean(rel)
        if not ok:
            raise Refused("%s %s; commit it first so the other box can pull it" % (rel, why))
        commit = self.last_commit(rel)
        body_commit = self.last_commit(doc["body_path"])
        if not body_commit:
            raise Refused("body %s has no commit in this tree; commit it first so the other box can pull it" % doc["body_path"])
        for what, c in (("the crossbox file %s" % rel, commit), ("the body %s" % doc["body_path"], body_commit)):
            if not self.on_origin(c):
                raise Refused("commit %s is not on origin yet (no refs/remotes/origin/* ref contains it; %s was last changed there). "
                              "Push it and fetch origin, then run line again; this tool does not fetch, so the other box would sit in "
                              "PULL-FIRST." % (c, what))
        return [fmt_line(doc, commit)]

    def on_origin(self, commit: str) -> bool:
        """True when at least one refs/remotes/origin/* ref of this root contains the commit (as last fetched or pushed)."""
        rc, out, _ = git(self.root, "for-each-ref", "--contains", commit, "--format=%(refname)", "refs/remotes/origin/")
        return rc == 0 and bool(out.strip())

    # -- issue: a task order to an addressee on another box becomes a crossbox file
    def issue(self, order, to_device=None) -> list:
        dev = devmod()
        rel = str(order or "").replace("\\", "/")
        if re.match(r"[A-Za-z]:", rel) or rel.startswith("/"):
            try:
                rel = Path(rel).resolve().relative_to(self.root.resolve()).as_posix()
            except ValueError:
                raise Refused("--order %s is not inside this checkout (%s)" % (order, self.root))
        if not rel or ".." in rel.split("/") or not (self.root / rel).is_file():
            raise Refused("--order %s is not a file in this tree" % order)
        ok, why = self.tracked_clean(rel)
        if not ok:
            raise Refused("--order %s %s; read the order from its commit: commit it first" % (rel, why))
        text = (self.root / rel).read_text(encoding="utf-8", errors="replace")
        found = {}
        for key in ("issued_to", "issued_by"):
            m = re.search(r"<%s>\s*(\S+)\s*</%s>" % (key, key), text)
            if not m:
                raise Refused("--order %s carries no <%s>" % (rel, key))
            found[key] = m.group(1)
        m = re.search(r"^# TO (.+?)\s*$", text, re.M)
        if not m:
            raise Refused("--order %s carries no '# TO ...' title line" % rel)
        subject = re.sub(r"[^\x20-\x7e]", "?", m.group(1).replace("|", "/")).strip()[:120].strip()
        serial = found["issued_to"]
        if to_device:
            target = dev.resolve(to_device)
            if target is None:
                raise Refused("--to-device %r is not in the device register (holds: %s)" % (to_device, ", ".join(dev.names())))
        else:
            target = self.device
            lane = serial.split("~", 1)[1] if "~" in serial else ""
            for d in dev.devices():
                if any(lane.startswith(letter) for letter in (d.get("lane_letters") or [])):
                    target = d["name"]
                    break
        if target == self.device:
            return ["XBOX-ISSUE local %s" % serial]
        out = self.open("ORDER", target, serial, found["issued_by"], subject, rel)
        return ["XBOX-ISSUE opened %s %s %s" % (out[0].split()[1], target, serial)] + out

    # -- send-pending: the manager sends what the line check admits
    def acting_serial(self) -> str:
        serial = os.environ.get("OPAL_AGENT_SERIAL", "").strip()
        if not serial:
            sid = os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip()
            f = self.root / "org" / "mcp" / "sessions" / ("%s.serial" % sid)
            if sid and re.fullmatch(r"[A-Za-z0-9._-]+", sid) and f.is_file():
                serial = f.read_text(encoding="utf-8").strip()
        return serial

    def send_pending(self, dry_run: bool = False) -> tuple:
        """([lines], rc). rc 0 unless a send failed (a send whose bus id could not be read is NOT recorded as sent)."""
        actor = self.acting_serial()
        if not re.fullmatch(r"0\.0\.0_AB_MSTR(~[A-Za-z0-9]+)?", actor):
            raise Refused("send-pending is a manager's act: the acting serial (OPAL_AGENT_SERIAL, else the session serial file) is %r, "
                          "not a 0.0.0_AB_MSTR serial or lane. Nothing was sent or recorded." % (actor or "unset"))
        override = os.environ.get("CROSSBOX_SEND_CMD", "").strip()
        if override:
            cmd = shlex.split(override)
        else:
            # Never a bare `bash`: on Windows subprocess resolves it to System32\bash.exe (WSL), which fails with
            # "execvpe(/bin/bash) failed" and nothing goes out (LD-0643, 0.0.0_AB_MSTR 2026-10-11). The one resolver
            # (CLAUDE.md: .tools/git_bash_resolver.py) names Git Bash; absent, the send REFUSES loud rather than guess.
            if str(HERE) not in sys.path:
                sys.path.insert(0, str(HERE))
            import git_bash_resolver  # noqa: E402  (a .tools sibling; imported here so the tests' sandbox roots work)
            gb = git_bash_resolver.git_bash()
            if not gb:
                raise Refused("no Git Bash found by .tools/git_bash_resolver.py; set CROSSBOX_SEND_CMD to '<git-bash> "
                              "<repo>/.tools/agentbus-sqs.sh send'. Nothing was sent or recorded.")
            cmd = [gb, (TOOL_ROOT / ".tools" / "agentbus-sqs.sh").as_posix(), "send"]
        lines, sent_n, held_n, failed_n, seen = [], 0, 0, 0, 0
        cdir = self.root / REL_DIR
        for path in [p for p in sorted(cdir.glob("*.json")) if not ANSWER_RE.fullmatch(p.name)] if cdir.is_dir() else []:
            try:
                doc = load_call_path(path, path.name)
            except (ValueError, Refused) as exc:
                lines.append("SKIP %s unreadable: %s" % (path.name, exc))
                continue
            if doc["from_device"] != self.device or derive_state(doc) != "OPEN" or doc["sent"]["bus_message_id"]:
                continue
            seen += 1
            try:
                line = self.line(doc["id"])[0]
            except Refused as exc:
                held_n += 1
                lines.append("HELD %s %s" % (doc["id"], exc))
                continue
            if dry_run:
                lines.append("WOULD SEND %s to %s from %s: %s" % (doc["id"], doc["to_device"], doc["from_serial"], line))
                continue
            try:
                proc = subprocess.run([*cmd, doc["to_device"], doc["from_serial"], line], capture_output=True, text=True,
                                      encoding="utf-8", errors="replace", timeout=120)
            except (OSError, subprocess.SubprocessError) as exc:
                failed_n += 1
                lines.append("FAILED %s the send command did not run (%s); nothing recorded" % (doc["id"], exc))
                continue
            m = re.search(r"MessageId=([0-9A-Za-z-]+)", proc.stdout)
            tail = [x.strip() for x in proc.stdout.splitlines() if x.strip()]
            busid = m.group(1) if m else (tail[-1] if tail and BUSID_RE.fullmatch(tail[-1]) else "")
            if proc.returncode != 0 or not busid:
                failed_n += 1
                lines.append("FAILED %s send command rc=%d, bus id %s; NOT recorded as sent (check the bus before resending: it may have gone out)" % (
                    doc["id"], proc.returncode, busid or "unreadable"))
                continue
            self.sent(doc["id"], busid, at=stamp(now_dt()))
            sent_n += 1
            lines.append("SENT %s to %s (bus message %s) recorded at %s" % (doc["id"], doc["to_device"], busid, self.read(doc["id"])["sent"]["at"]))
        lines.append("SEND-PENDING %s candidates=%d sent=%d held=%d failed=%d" % ("DRY-RUN" if dry_run else "done", seen, sent_n, held_n, failed_n))
        return lines, (3 if failed_n else 0)

    def sent(self, call_id: str, bus_message_id: str, at: str | None = None) -> list:
        doc = self.read(call_id)
        self.need_box(doc, "from_device", "sent")
        if not BUSID_RE.fullmatch(bus_message_id or ""):
            raise Refused("--bus-message-id %r is not a bus message id" % bus_message_id)
        if doc["sent"]["bus_message_id"]:
            raise Refused("%s already records bus message %s as sent" % (call_id, doc["sent"]["bus_message_id"]))
        if self.layout2(call_id):
            raw = self.from_raw(call_id)
            raw["sent"] = {"at": at or stamp(now_dt()), "bus_message_id": bus_message_id}
            self.save_from2(raw)
        else:
            doc["sent"] = {"at": at or stamp(now_dt()), "bus_message_id": bus_message_id}
            self.save(doc)
        return ["SENT %s recorded (bus message %s). Sent is not read: status stays SENT, NOT ACKED until the reply line is recorded." % (
            call_id, bus_message_id)]

    # -- receive / ack / acked
    def resolve_seat(self, serial: str) -> Path:
        base = base_of(serial)
        lane = serial.split("~", 1)[1] if "~" in serial else None
        folder = None
        for tier in TIERS:
            cand = self.root / "org" / tier / base
            if cand.is_dir():
                folder = cand
                break
        if folder is None:
            raise Refused("no such seat on this box: no agent folder %s under org/<tier>/ in %s" % (base, self.root))
        inbox = self.root / "org" / "mcp" / "inbox" / folder.name
        if lane:
            inbox = inbox / ("~%s" % lane)
        if not inbox.is_dir():
            raise Refused("no such seat on this box: %s has no inbox directory %s (the seat's watcher creates it when armed)" % (
                serial, inbox))
        return inbox

    def receive(self, text: str, at: datetime.datetime | None = None) -> list:
        m = LINE_RE.search(text or "")
        if not m:
            raise Refused("no CROSSBOX line found in the text given")
        call_id, kind, to_serial, subject, rel, commit = m.groups()
        if rel != self.rel(call_id):
            raise Refused("the line names file %s, which is not the file of id %s" % (rel, call_id))
        rc, _, _ = git(self.root, "cat-file", "-e", "%s^{commit}" % commit)
        if rc != 0:
            raise PullFirst("PULL-FIRST: commit %s is not in this tree; pull (git fetch + merge) the sender's branch, then run receive "
                            "again. Nothing was written." % commit)
        rc, blob, _ = git(self.root, "show", "%s:%s" % (commit, rel))
        if rc != 0:
            raise Refused("file %s does not exist at commit %s: the line does not match what the sender committed (tampered or wrong commit)" % (rel, commit))
        try:
            doc = load_call_text(blob, "%s@%s" % (rel, commit))
        except ValueError as exc:
            raise Refused("%s@%s is not JSON (%s)" % (rel, commit, exc))
        for field, got, want in (("id", call_id, doc["id"]), ("kind", kind, doc["kind"]), ("to-serial", to_serial, doc["to_serial"]),
                                 ("subject", subject, doc["subject"])):
            if got != want:
                raise Refused("the line's %s %r does not match the committed file's %r (tampered line)" % (field, got, want))
        if doc["to_device"] != self.device:
            raise Refused("this order is for box %s; this box is %s" % (doc["to_device"], self.device))
        rc, _, _ = git(self.root, "cat-file", "-e", "%s:%s" % (commit, doc["body_path"]))
        if rc != 0:
            raise Refused("the body file %s is not in commit %s" % (doc["body_path"], commit))
        self.need_in_tree(doc, rel, commit)
        inbox = self.resolve_seat(doc["to_serial"])
        marker = "_CROSSBOX_%s_" % doc["id"]
        for where in (inbox, inbox / "read"):
            if where.is_dir() and any(marker in p.name for p in where.glob("*.md")):
                return ["ALREADY DELIVERED %s to %s (a file for it is already in %s or its read/); nothing written" % (doc["id"], doc["to_serial"], inbox)]
        when = at or now_dt()
        ts = when.strftime("%Y%m%dT%H%M%SZ")
        subj = "CROSSBOX %s %s: %s" % (doc["id"], doc["kind"], doc["subject"])
        safe_from = re.sub(r"[^a-zA-Z0-9._-]", "_", doc["from_serial"])
        safe_subject = re.sub(r"[^a-zA-Z0-9._-]", "_", subj)[:40]
        name = "%s_%s_%s.md" % (ts, safe_from, safe_subject)
        content = ("# Message from %s (box %s)\n**To:** %s\n**Date:** %s\n**Cross-box:** %s %s from box %s\n**Subject:** %s\n\n"
                   "file: %s\nbody: %s\n" % (doc["from_serial"], doc["from_device"], doc["to_serial"], ts, doc["id"], doc["kind"],
                                             doc["from_device"], subj, rel, doc["body_path"]))
        write_text(inbox / name, content)
        return ["DELIVERED %s to %s: %s" % (doc["id"], doc["to_serial"], inbox / name)]

    # The identity of a call: the fields a later `sent`/`ack`/`close` never rewrites.
    IDENTITY_FIELDS = ("id", "kind", "from_device", "to_device", "from_serial", "to_serial", "subject", "body_path")

    def need_in_tree(self, doc: dict, rel: str, commit: str) -> None:
        """CVO ruling @bf5cc9cb1e: the recipient reads the call and its body from the WORKING TREE, so a line is delivered
        only when both are here -- tested by CONTENT, never `merge-base --is-ancestor` (a cherry-pick or squash brings the
        bytes with no ancestry). Raises PullFirst (nothing written) otherwise.
        The call file is compared on its IDENTITY fields: its sent/ack/closed record advances by design in later commits, so
        a byte test would refuse every line once the sender's `sent` commit lands. The body passes when its working-tree
        bytes equal the commit's, or when the commit's blob is an earlier version of the same path in this tree's history
        (an amended order); a body whose committed bytes this tree never held refuses."""
        run_next = " RUN NEXT: the box pass (`bash .tools/box-sync.sh box`) or a merge of the sender's branch, then `receive` again. Nothing was written."
        here = self.root / rel
        if not here.is_file():
            raise PullFirst("PULL-FIRST: call file %s is not in this working tree (commit %s is known here but not merged)." % (rel, commit) + run_next)
        try:
            mine = json.loads(here.read_text(encoding="utf-8"))
        except ValueError as exc:
            raise Refused("the working-tree copy of %s is not JSON (%s)" % (rel, exc))
        for f in self.IDENTITY_FIELDS:
            if mine.get(f) != doc.get(f):
                raise Refused("the working-tree copy of %s has %s %r, the line's commit %s has %r" % (rel, f, mine.get(f), commit, doc.get(f)))
        body = doc["body_path"]
        bpath = self.root / body
        if not bpath.is_file():
            raise PullFirst("PULL-FIRST: body %s is not in this working tree (commit %s is known here but not merged)." % (body, commit) + run_next)
        rc, want, _ = git(self.root, "rev-parse", "%s:%s" % (commit, body))
        rc2, have, _ = git(self.root, "hash-object", "--", body)
        if rc != 0 or rc2 != 0:
            raise Refused("could not hash body %s (commit side rc=%s, working-tree side rc=%s)" % (body, rc, rc2))
        if want.strip() == have.strip():
            return
        rc, hit, _ = git(self.root, "log", "-1", "--format=%H", "--find-object=%s" % want.strip(), "HEAD", "--", body)
        if rc == 0 and hit.strip():
            return
        raise PullFirst("PULL-FIRST: body %s here differs from commit %s and this tree's history never held the committed bytes." % (body, commit) + run_next)

    def ack(self, call_id: str, by: str, at: str | None = None) -> list:
        doc = self.read(call_id)
        self.need_box(doc, "to_device", "ack")
        want = doc["to_serial"]
        if by != want and ("~" in want or base_of(by) != want):
            raise Refused("--by %s is not the named seat %s; the named seat acknowledges" % (by, want))
        if self.layout2(call_id):
            # layout 2: this box's own answer file; the from-side file is not touched
            ans = self.answer_raw(call_id, self.device) or {"schema": SCHEMA_ANS, "id": call_id, "box": self.device, "ack": None,
                                                           "closed_to": {"at": None, "by": None}}
            if not ans["ack"]:
                ans["ack"] = {"at": at or stamp(now_dt()), "by": by}
                self.save_answer(ans)
            ack = {"at": ans["ack"]["at"], "by": ans["ack"]["by"]}
        else:
            if not doc["ack"]:
                doc["ack"] = {"at": at or stamp(now_dt()), "by": by, "bus_message_id": None}
                self.save(doc)
            ack = doc["ack"]
        return ["ACKED %s at %s by %s on the receiving box. Put this reply line on the bus to the sending box:" % (
            call_id, ack["at"], ack["by"]), "CROSSBOX-ACK %s READ by %s at %s" % (call_id, ack["by"], ack["at"])]

    def acked(self, call_id: str, text: str, bus_message_id: str) -> list:
        doc = self.read(call_id)
        self.need_box(doc, "from_device", "acked")
        m = ACK_RE.search(text or "")
        if not m or m.group(1) != call_id:
            raise Refused("no `CROSSBOX-ACK %s READ by <serial> at <UTC>` line for this id in the text given" % call_id)
        if not BUSID_RE.fullmatch(bus_message_id or ""):
            raise Refused("--bus-message-id %r is not a bus message id" % bus_message_id)
        by, when = m.group(2), m.group(3)
        if base_of(by) != base_of(doc["to_serial"]):
            raise Refused("the reply is by %s, not by the named seat %s" % (by, doc["to_serial"]))
        if self.layout2(call_id):
            # layout 2: the bus id of the reply goes into the from-side file; the answer's own ack stays in its file
            raw = self.from_raw(call_id)
            if raw["ack_bus_message_id"] and raw["ack_bus_message_id"] != bus_message_id:
                raise Refused("a different reply bus message %s is already recorded" % raw["ack_bus_message_id"])
            raw["ack_bus_message_id"] = bus_message_id
            self.save_from2(raw)
            shown = doc["ack"] or {"at": when, "by": by}
            return ["ACK recorded for %s: read by %s at %s (reply bus message %s)" % (call_id, shown["by"], shown["at"], bus_message_id)]
        ack = doc["ack"] or {"at": when, "by": by, "bus_message_id": None}
        if ack["bus_message_id"] and ack["bus_message_id"] != bus_message_id:
            raise Refused("a different reply bus message %s is already recorded" % ack["bus_message_id"])
        ack["bus_message_id"] = bus_message_id
        doc["ack"] = ack
        self.save(doc)
        return ["ACK recorded for %s: read by %s at %s (reply bus message %s)" % (call_id, ack["by"], ack["at"], bus_message_id)]

    # -- close / status / list / merge
    def close(self, call_id: str, side: str, by: str, at: str | None = None) -> list:
        doc = self.read(call_id)
        if side not in ("from", "to"):
            raise Refused("--side must be from or to")
        self.need_box(doc, "%s_device" % side, "close --side %s" % side)
        if not by or not SERIAL_RE.fullmatch(by):
            raise Refused("--by %r is not a serial" % by)
        if not (doc["ack"] and doc["ack"]["at"]):
            raise Refused("%s is not acknowledged yet (no ack recorded in this copy); a call closes after the other side has read it" % call_id)
        if doc["closed"]["%s_at" % side]:
            raise Refused("the %s side is already closed (%s)" % (side, doc["closed"]["%s_at" % side]))
        if self.layout2(call_id):
            # layout 2: the from side writes the from-side file; the to side writes its own answer file
            stamped = {"at": at or stamp(now_dt()), "by": by}
            if side == "from":
                raw = self.from_raw(call_id)
                raw["closed_from"] = stamped
                self.save_from2(raw)
            else:
                ans = self.answer_raw(call_id, self.device)
                if ans is None:
                    raise Refused("%s has no answer file of this box (%s); the to side closes where it acknowledged" % (call_id, answer_name(call_id, self.device)))
                ans["closed_to"] = stamped
                self.save_answer(ans)
            return self.status(call_id)
        doc["closed"]["%s_at" % side] = at or stamp(now_dt())
        doc["closed"]["%s_by" % side] = by
        self.save(doc)
        return self.status(call_id)

    def withdraw(self, call_id: str, by: str, ruling: str, at: str | None = None) -> list:
        """The issuing box retires an ORDER its named seat never read (the seat is absent), on a committed ruling.
        No new key and no new state: the withdrawing seat writes BOTH closed sides, so every crossbox/1 reader on every
        box reads CLOSED-BOTH, and status prints WITHDRAWN because the two closers are one seat and no ack exists."""
        doc = self.read(call_id)
        self.need_box(doc, "from_device", "withdraw")
        if doc["kind"] != "ORDER":
            raise Refused("withdraw retires an ORDER; %s is a %s (a CALL is answered or closed, never withdrawn)" % (call_id, doc["kind"]))
        if doc["ack"] and doc["ack"]["at"]:
            raise Refused("%s was read by %s at %s; a read order closes with `close`, it is not withdrawn" % (call_id, doc["ack"]["by"], doc["ack"]["at"]))
        if doc["closed"]["from_at"] or doc["closed"]["to_at"]:
            raise Refused("%s already has a closed side" % call_id)
        if not by or not SERIAL_RE.fullmatch(by):
            raise Refused("--by %r is not a serial" % by)
        if base_of(by) not in {base_of(doc["from_serial"]), "1.0.0_SA_CTO", "0.0.0_AB_MSTR"}:
            raise Refused("--by %s is neither the issuer %s nor the issuing box's CTO or MSTR" % (by, doc["from_serial"]))
        rel = str(ruling or "").replace("\\", "/")
        if not rel or rel.startswith("/") or ".." in rel.split("/") or re.match(r"[A-Za-z]:", rel) or not (self.root / rel).is_file():
            raise Refused("--ruling must be a file inside the repository, relative to its root")
        ok, why = self.tracked_clean(rel)
        if not ok:
            raise Refused("--ruling %s %s; the other box reads the ruling by pulling it. Commit it first." % (rel, why))
        when = at or stamp(now_dt())
        if self.layout2(call_id):
            # the issuing box's act: both closed sides go in the from-side file (no answer file exists: nothing was read)
            raw = self.from_raw(call_id)
            raw["closed_from"], raw["closed_to_issuer"] = {"at": when, "by": by}, {"at": when, "by": by}
            self.save_from2(raw)
        else:
            doc["closed"] = {"from_at": when, "from_by": by, "to_at": when, "to_by": by}
            self.save(doc)
        return self.status(call_id) + ["WITHDRAWN %s by %s on ruling %s; the named seat %s never read it" % (call_id, by, rel, doc["to_serial"])]

    SUPERSEDED_MARK = "superseded-by "

    def sent_commit(self, doc: dict) -> str:
        """The commit that recorded this file's `sent` block (the oldest commit introducing its bus id), else the file's
        last commit. The body blob is pinned HERE, never at HEAD (CVO verdict @a803dad6ae condition 1)."""
        rel = self.rel(doc["id"])
        busid = (doc.get("sent") or {}).get("bus_message_id")
        if busid:
            rc, out, _ = git(self.root, "log", "--format=%H", "-S", busid, "--", rel)
            hits = out.split()
            if rc == 0 and hits:
                return hits[-1]
        return self.last_commit(rel)

    def supersede(self, call_id: str, by: str, ruling: str, successor_id: str, at: str | None = None) -> list:
        """The sending box closes a CALL its addressee never read because the SAME body reached a live seat on the same box
        under a later file that seat ACKED (CVO verdict @a803dad6ae, 2026-10-12: a manager ack for a dead seat is a forged
        READ; a withdraw is the wrong fact; the true fact is 'superseded'). Conditions: (1) the body blob is compared at each
        file's own sent commit, not at HEAD; (2) the close is terminal for every reader -- both closed sides are written, the
        to side by the marker `superseded-by <id>`, so crossbox/1 readers see CLOSED-BOTH with NO new key; (3) the successor's
        to_device equals the original's, and only the sender file is written."""
        doc = self.read(call_id)
        self.need_box(doc, "from_device", "close --superseded-by")
        if doc["kind"] != "CALL":
            raise Refused("close --superseded-by closes a CALL; %s is an %s (an unread ORDER is withdrawn)" % (call_id, doc["kind"]))
        if doc["ack"] and doc["ack"]["at"]:
            raise Refused("%s was read by %s at %s; a read call closes with `close --side`, it is not superseded" % (call_id, doc["ack"]["by"], doc["ack"]["at"]))
        if doc["closed"]["from_at"] or doc["closed"]["to_at"]:
            raise Refused("%s already has a closed side" % call_id)
        if not by or not SERIAL_RE.fullmatch(by):
            raise Refused("--by %r is not a serial" % by)
        if base_of(by) not in {base_of(doc["from_serial"]), "1.0.0_SA_CTO", "0.0.0_AB_MSTR"}:
            raise Refused("--by %s is neither the issuer %s nor the issuing box's CTO or MSTR" % (by, doc["from_serial"]))
        rel = str(ruling or "").replace("\\", "/")
        if not rel or rel.startswith("/") or ".." in rel.split("/") or re.match(r"[A-Za-z]:", rel) or not (self.root / rel).is_file():
            raise Refused("--ruling must be a file inside the repository, relative to its root")
        ok, why = self.tracked_clean(rel)
        if not ok:
            raise Refused("--ruling %s %s; the other box reads the ruling by pulling it. Commit it first." % (rel, why))
        if successor_id == call_id:
            raise Refused("a call cannot supersede itself")
        succ = self.read(successor_id)
        if succ["kind"] != doc["kind"]:
            raise Refused("successor %s is an %s, %s is a %s" % (successor_id, succ["kind"], call_id, doc["kind"]))
        if succ["to_device"] != doc["to_device"] or succ["from_device"] != doc["from_device"]:
            raise Refused("successor %s runs %s -> %s, %s runs %s -> %s; reachability is box to box, so a successor on another "
                          "box does not answer this call (to_device must match)" % (successor_id, succ["from_device"], succ["to_device"],
                                                                                   call_id, doc["from_device"], doc["to_device"]))
        if not (succ["ack"] and succ["ack"]["at"] and succ["ack"]["by"]):
            raise Refused("successor %s is not acknowledged; a superseded close rests on a READ by a live seat" % successor_id)
        blobs = {}
        for d in (doc, succ):
            commit = self.sent_commit(d)
            if not commit:
                raise Refused("%s has no commit in this tree; commit it first" % self.rel(d["id"]))
            rc, blob, err = git(self.root, "rev-parse", "%s:%s" % (commit, d["body_path"]))
            if rc != 0 or not blob.strip():
                raise Refused("could not read the body blob of %s at its sent commit %s (%s)" % (d["id"], commit[:10], err.strip()[:80]))
            blobs[d["id"]] = (commit[:10], blob.strip())
        if blobs[call_id][1] != blobs[successor_id][1]:
            raise Refused("the body of %s at %s (%s) differs from the body of %s at %s (%s): not the same call" % (
                call_id, blobs[call_id][0], blobs[call_id][1][:10], successor_id, blobs[successor_id][0], blobs[successor_id][1][:10]))
        when = at or stamp(now_dt())
        if self.layout2(call_id):
            # the sending box's act: the from-side file carries both closed sides (the marker is the issuing box's to_by)
            raw = self.from_raw(call_id)
            raw["closed_from"] = {"at": when, "by": by}
            raw["closed_to_issuer"] = {"at": when, "by": self.SUPERSEDED_MARK + successor_id}
            self.save_from2(raw)
        else:
            doc["closed"] = {"from_at": when, "from_by": by, "to_at": when, "to_by": self.SUPERSEDED_MARK + successor_id}
            self.save(doc)
        return self.status(call_id) + ["SUPERSEDED %s by %s on ruling %s: the same body (blob %s) reached %s under %s, acked by %s at %s" % (
            call_id, by, rel, blobs[call_id][1][:10], doc["to_device"], successor_id, succ["ack"]["by"], succ["ack"]["at"])]

    def status_of(self, doc: dict, now: datetime.datetime | None = None) -> str:
        cid, c = doc["id"], doc["closed"]
        if c["from_at"] and c["to_at"] and str(c["to_by"] or "").startswith(self.SUPERSEDED_MARK) and not (doc["ack"] and doc["ack"]["at"]):
            return "STATUS %s SUPERSEDED by %s (closed %s by %s; the body reached %s under the acked file; reads CLOSED-BOTH to every crossbox/1 reader)" % (
                cid, c["to_by"][len(self.SUPERSEDED_MARK):], c["from_at"], c["from_by"], doc["to_device"])
        if c["from_at"] and c["to_at"] and c["from_by"] == c["to_by"] and not (doc["ack"] and doc["ack"]["at"]):
            return "STATUS %s WITHDRAWN by %s at %s (ORDER never read by %s; reads CLOSED-BOTH to every crossbox/1 reader)" % (
                cid, c["from_by"], c["from_at"], doc["to_serial"])
        if c["from_at"] and c["to_at"]:
            return "STATUS %s CLOSED-BOTH (from %s by %s, to %s by %s)" % (cid, c["from_at"], c["from_by"], c["to_at"], c["to_by"])
        if c["from_at"] or c["to_at"]:
            side = "from" if c["from_at"] else "to"
            return "STATUS %s HALF-CLOSED (%s only, %s); the call is NOT settled until both sides are recorded" % (cid, side, c["%s_at" % side])
        if doc["ack"] and doc["ack"]["at"]:
            return "STATUS %s ACKED (read by %s at %s); not closed on either side" % (cid, doc["ack"]["by"], doc["ack"]["at"])
        if doc["to_device"] == self.device:
            return "STATUS %s AWAITING ACK by %s (this is the receiving box; opened %s)" % (cid, doc["to_serial"], age_text(doc["opened_at"], now))
        if doc["sent"]["bus_message_id"]:
            return "STATUS %s SENT, NOT ACKED (sent %s, bus message %s) -- sent is not read" % (
                cid, age_text(doc["sent"]["at"], now), doc["sent"]["bus_message_id"])
        return "STATUS %s OPEN, NOT YET PUT ON THE BUS (opened %s)" % (cid, age_text(doc["opened_at"], now))

    def status(self, call_id: str) -> list:
        doc = self.read(call_id)
        lines = [self.status_of(doc)]
        if doc["state"] != derive_state(doc):
            lines.append("NOTE: the file's state field says %s but its fields read %s; the next write recomputes it" % (doc["state"], derive_state(doc)))
        return lines

    def listing(self, only_open: bool = False) -> list:
        lines, shown, total = [], 0, 0
        names = sorted((self.root / REL_DIR).glob("*.json")) if (self.root / REL_DIR).is_dir() else []
        claimed = set()   # the answer files a readable from-side file of its box claims
        for path in [p for p in names if not ANSWER_RE.fullmatch(p.name)]:
            total += 1
            try:
                doc = load_call_path(path, path.name)
            except (ValueError, Refused) as exc:
                lines.append("UNREADABLE %s: %s" % (path.name, exc))
                shown += 1
                continue
            if doc["schema"] == SCHEMA2:
                claimed.add(answer_name(doc["id"], doc["to_device"]))
            if only_open and derive_state(doc) == "CLOSED-BOTH":
                continue
            shown += 1
            lines.append("%s %s %s %s -> %s to %s opened %s" % (doc["id"], derive_state(doc), doc["kind"], doc["from_device"],
                                                                 doc["to_device"], doc["to_serial"], age_text(doc["opened_at"])))
        for path in [p for p in names if ANSWER_RE.fullmatch(p.name) and p.name not in claimed]:
            total += 1
            shown += 1
            lines.append("UNREADABLE %s: an answer file that no readable from-side file of its box claims" % path.name)
        lines.append("CROSSBOX-LIST files=%d shown=%d root=%s" % (total, shown, self.root))
        return lines

    def merge(self, call_id: str, ref: str) -> list:
        mine = self.read(call_id)
        if self.layout2(call_id):
            # layout 2: every side already wrote its own file, so there is nothing to fold (a git merge carries both)
            return ["CROSSBOX-MERGE %s NOTHING-TO-FOLD (layout 2: each side writes its own file)" % call_id]
        rc, blob, err = git(self.root, "show", "%s:%s" % (ref, self.rel(call_id)))
        if rc != 0:
            raise Refused("no %s at %s in this tree (%s)" % (self.rel(call_id), ref, err.strip()[:120]))
        try:
            other = check_call(json.loads(blob), "%s@%s" % (self.rel(call_id), ref))
        except ValueError as exc:
            raise Refused("the file at %s is not JSON (%s)" % (ref, exc))
        for key in KEYS:
            if key in ("state", "sent", "ack", "closed"):
                continue
            if mine[key] != other[key]:
                raise Refused("the other copy differs in %s (%r vs %r): not the same call" % (key, mine[key], other[key]))
        merged = dict(mine)
        for key in ("sent", "ack", "closed"):
            if other[key] is None:
                continue
            block = dict(mine[key] or {})
            for sub, val in other[key].items():
                if val is None:
                    block.setdefault(sub, None)   # a null the other copy carries stays null: the schema allows it
                    continue
                if block.get(sub) not in (None, val):
                    raise Refused("both copies hold a different %s.%s (%r vs %r): resolve by hand" % (key, sub, block[sub], val))
                block[sub] = val
            merged[key] = block
        # validate the WHOLE merged result in memory, then write exactly the bytes that were validated: a refusal here
        # writes nothing, and a null bus_message_id from either copy stays null (the schema allows it)
        text = dump(merged)
        check_call(json.loads(text), "%s (merged from %s)" % (self.rel(call_id), ref))
        changed = json.loads(text) != mine
        write_text(self.path(call_id), text)
        return ["MERGED %s from %s (%s)" % (call_id, ref, "fields folded in" if changed else "nothing new")] + self.status(call_id)


# ---------------------------------------------------------------- the selftest harness (two scratch checkouts)

GIT_ENV = {"GIT_AUTHOR_NAME": "crossbox-selftest", "GIT_AUTHOR_EMAIL": "selftest@example.invalid",
           "GIT_COMMITTER_NAME": "crossbox-selftest", "GIT_COMMITTER_EMAIL": "selftest@example.invalid"}
GIT_FLAGS = ["-c", "core.hooksPath=%s" % os.devnull, "-c", "commit.gpgsign=false", "-c", "core.autocrlf=false"]
SEAT = "9.9.0_ZZ_Selftest"
SEAT_LANE = "~X"
BODY = "docs/selftest_body.md"
CALL_ID = "OC-SELFTEST-0001"


def sgit(root: Path, *args):
    return git(root, *GIT_FLAGS, *args, extra_env=GIT_ENV)


def rmtree_force(path) -> None:
    def onerr(func, target, _exc):
        os.chmod(target, stat.S_IWRITE)
        func(target)
    shutil.rmtree(path, onerror=onerr)


class Harness:
    """Two scratch git checkouts standing for two boxes; the bus is replaced by handing a printed line across."""

    def __init__(self, tmp):
        names = devmod().names()
        if len(names) < 2:
            raise Refused("the device register holds fewer than two boxes")
        self.tmp = Path(tmp)
        a_root, b_root = self.tmp / "boxA", self.tmp / "boxB"
        a_root.mkdir()
        sgit(a_root, "init", "-q")
        (a_root / "docs").mkdir()
        (a_root / BODY).write_text("selftest body\n", encoding="utf-8")
        sgit(a_root, "add", BODY)
        sgit(a_root, "commit", "-q", "-m", "body")
        origin = self.tmp / "origin.git"
        subprocess.run(["git", *GIT_FLAGS, "init", "-q", "--bare", str(origin)], capture_output=True, text=True,
                       env={**os.environ, **GIT_ENV}, timeout=60, check=True)
        sgit(a_root, "remote", "add", "origin", str(origin))
        self.push(a_root)
        subprocess.run(["git", *GIT_FLAGS, "clone", "-q", str(a_root), str(b_root)], capture_output=True, text=True,
                       env={**os.environ, **GIT_ENV}, timeout=60, check=True)
        (b_root / "org" / "tier2_senior" / SEAT).mkdir(parents=True)
        (b_root / "org" / "mcp" / "inbox" / SEAT / SEAT_LANE).mkdir(parents=True)
        self.a = Box(a_root, names[0])
        self.b = Box(b_root, names[1])

    def push(self, root) -> None:
        """Push HEAD to the scratch bare origin (what makes a commit readable by the other box); updates refs/remotes/origin/main."""
        rc, _, err = sgit(Path(root), "push", "-q", "origin", "HEAD:refs/heads/main")
        if rc != 0:
            raise Refused("selftest push to the scratch origin failed: %s" % err.strip()[:120])

    def commit(self, box: Box, *paths) -> None:
        sgit(box.root, "add", "--", *paths)
        sgit(box.root, "commit", "-q", "-m", "step", "--", *paths)

    def pull(self, dst: Box, src: Box, ff: bool) -> None:
        sgit(dst.root, "fetch", "-q", str(src.root), "HEAD")
        if ff:
            sgit(dst.root, "merge", "-q", "--ff-only", "FETCH_HEAD")


_ENV_LOCK = threading.Lock()   # the reader takes its directory from an environment variable; two threads must not swap it


def open_calls_reader(crossbox_dir: Path, call_id: str = CALL_ID):
    """The REAL reader in .tools/open-calls.py (its `close` limb for a CROSS-BOX call): the file name that reads CLOSED-BOTH for the call, None when none does,
    or an ERROR: string when the reader could not be loaded or run."""
    try:
        spec = importlib.util.spec_from_file_location("open_calls_cb", HERE / "open-calls.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        with _ENV_LOCK:
            old = os.environ.get("OPAL_CROSSBOX_ROOT")
            os.environ["OPAL_CROSSBOX_ROOT"] = str(crossbox_dir)
            try:
                found, _lines = mod.crossbox_closed_both(call_id, None)
            finally:
                if old is None:
                    os.environ.pop("OPAL_CROSSBOX_ROOT", None)
                else:
                    os.environ["OPAL_CROSSBOX_ROOT"] = old
        return found
    except Exception as exc:   # a reader that cannot load is reported, never read as a clean refusal
        return "ERROR:%s" % exc


def raises(kind, fn, needle: str = "") -> tuple:
    try:
        fn()
    except kind as exc:
        return needle in str(exc), str(exc)
    return False, "no %s raised" % kind.__name__


MERGE_BUS = "0a1b2c3d-0000-4000-8000-0000000000a1"
MERGE_REPLY = "0a1b2c3d-0000-4000-8000-0000000000b2"


def merge_cases(tmp) -> list:
    """The merge arms (CT-am-3, S9121). A null bus_message_id folds in both ways and stays null where the other copy holds
    null; a merge refused for ANY reason -- the other copy fails validation, the merged result fails the validator, the
    copies conflict -- writes nothing: both copies stay byte-identical. Each arm is its own two-checkout exchange under tmp."""
    out = []

    def rec(name, ok, detail=""):
        out.append((name, bool(ok), str(detail)[:200]))

    seat = SEAT + SEAT_LANE

    def fresh(arm):
        root = Path(tmp) / "merge-arms" / arm
        root.mkdir(parents=True)
        return Harness(root)

    def exchange(h):
        a, b = h.a, h.b
        cid = a.open("CALL", b.device, seat, "1.0.0_SA_CTO", "merge arm", BODY)[0].split()[1]
        h.commit(a, a.rel(cid))
        h.push(a.root)
        a.sent(cid, MERGE_BUS)
        h.commit(a, a.rel(cid))
        h.push(a.root)
        h.pull(b, a, ff=True)
        b.receive(a.line(cid)[0])
        return cid

    def both_copies(h, cid):
        """The receiving copy's bytes and the other copy's bytes (the blob FETCH_HEAD names); a missing blob reads as None."""
        rc, other, _ = sgit(h.a.root, "show", "FETCH_HEAD:%s" % h.a.rel(cid))
        return h.a.path(cid).read_bytes(), (other if rc == 0 else None)

    # arm 1: the sending copy merges a receiving copy whose ack carries bus_message_id null
    try:
        h = fresh("arm1")
        cid = exchange(h)
        h.b.ack(cid, seat)
        h.commit(h.b, h.b.rel(cid))
        h.pull(h.a, h.b, ff=False)
        h.a.merge(cid, "FETCH_HEAD")
        got = h.a.read(cid)
        rec("a-null-bus-id-merges-into-the-sending-copy", got["ack"]["bus_message_id"] is None and got["ack"]["by"] == seat
            and got["sent"]["bus_message_id"] == MERGE_BUS, json.dumps(got["ack"]))
    except Exception as exc:
        rec("a-null-bus-id-merges-into-the-sending-copy", False, "%s: %s" % (type(exc).__name__, exc))

    # arm 2: a null on the receiving copy takes the reply bus id the sending copy has recorded since
    try:
        h = fresh("arm2")
        cid = exchange(h)
        h.b.ack(cid, seat)
        h.commit(h.b, h.b.rel(cid))
        h.pull(h.a, h.b, ff=False)
        h.a.merge(cid, "FETCH_HEAD")
        h.a.acked(cid, "[x] [from %s] CROSSBOX-ACK %s READ by %s at %s" % (seat, cid, seat, stamp(now_dt())), MERGE_REPLY)
        h.commit(h.a, h.a.rel(cid))
        h.pull(h.b, h.a, ff=False)
        h.b.merge(cid, "FETCH_HEAD")
        got = h.b.read(cid)
        rec("a-null-bus-id-on-the-receiving-copy-takes-the-reply-bus-id", got["ack"]["bus_message_id"] == MERGE_REPLY,
            json.dumps(got["ack"]))
    except Exception as exc:
        rec("a-null-bus-id-on-the-receiving-copy-takes-the-reply-bus-id", False, "%s: %s" % (type(exc).__name__, exc))

    # arm 3: the other copy fails validation (an unknown key in its ack): refused, and both copies stay byte-identical
    try:
        h = fresh("arm3")
        cid = exchange(h)
        h.b.ack(cid, seat)
        doc = json.loads(h.b.path(cid).read_text(encoding="utf-8"))
        doc["ack"]["extra"] = 1
        h.b.path(cid).write_text(json.dumps(doc), encoding="utf-8")
        h.commit(h.b, h.b.rel(cid))
        h.pull(h.a, h.b, ff=False)
        before = both_copies(h, cid)
        ok, why = raises(Refused, lambda: h.a.merge(cid, "FETCH_HEAD"), "unknown key")
        rec("a-merge-of-a-copy-that-fails-validation-writes-nothing", ok and both_copies(h, cid) == before and before[1] is not None, why)
    except Exception as exc:
        rec("a-merge-of-a-copy-that-fails-validation-writes-nothing", False, "%s: %s" % (type(exc).__name__, exc))

    # arm 4: the validator refuses the MERGED result (the other copy is valid): refused after the merge is computed, nothing written
    real_check = check_call

    def refuse_merged(doc, where):
        if "merged from" in where:
            raise Refused("forced: the validator refuses the merged result of %s" % where)
        return real_check(doc, where)

    try:
        h = fresh("arm4")
        cid = exchange(h)
        h.b.ack(cid, seat)
        h.commit(h.b, h.b.rel(cid))
        h.pull(h.a, h.b, ff=False)
        before = both_copies(h, cid)
        globals()["check_call"] = refuse_merged
        try:
            ok, why = raises(Refused, lambda: h.a.merge(cid, "FETCH_HEAD"), "forced")
        finally:
            globals()["check_call"] = real_check
        rec("a-merged-result-the-validator-refuses-writes-nothing", ok and both_copies(h, cid) == before, why)
    except Exception as exc:
        rec("a-merged-result-the-validator-refuses-writes-nothing", False, "%s: %s" % (type(exc).__name__, exc))

    # arm 5: the copies hold different values for one field: refused, and both copies stay byte-identical
    try:
        h = fresh("arm5")
        cid = exchange(h)
        mine = h.a.read(cid)
        mine["ack"] = {"at": "2026-10-08T02:00:00Z", "by": seat, "bus_message_id": None}
        h.a.path(cid).write_text(json.dumps(mine), encoding="utf-8")
        h.b.ack(cid, seat, at="2026-10-08T01:00:00Z")
        h.commit(h.b, h.b.rel(cid))
        h.pull(h.a, h.b, ff=False)
        before = both_copies(h, cid)
        ok, why = raises(Refused, lambda: h.a.merge(cid, "FETCH_HEAD"), "different ack.at")
        rec("a-conflicting-merge-is-refused-and-writes-nothing", ok and both_copies(h, cid) == before, why)
    except Exception as exc:
        rec("a-conflicting-merge-is-refused-and-writes-nothing", False, "%s: %s" % (type(exc).__name__, exc))
    return out


def run_cases(tmp) -> list:
    """The whole exchange. Returns [(name, ok, detail)] in order; a step that cannot run reports itself as a failed case."""
    out = []

    def rec(name, ok, detail=""):
        out.append((name, bool(ok), str(detail)[:200]))

    h = Harness(tmp)
    a, b = h.a, h.b
    seat = SEAT + SEAT_LANE

    (a.root / "docs" / "loose.md").write_text("not committed\n", encoding="utf-8")
    ok, why = raises(Refused, lambda: a.open("CALL", b.device, seat, "1.0.0_SA_CTO", "subject", "docs/loose.md"), "Commit it first")
    rec("open-refuses-an-uncommitted-body", ok, why)
    ok, why = raises(Refused, lambda: a.open("CALL", a.device, seat, "1.0.0_SA_CTO", "subject", BODY), "is this box")
    rec("open-refuses-this-box-as-the-target", ok, why)

    opened = a.open("CALL", b.device, seat, "1.0.0_SA_CTO", "Close the dell fence call", BODY, call_id=CALL_ID)
    cid = opened[0].split()[1]
    doc = a.read(cid)
    rec("open-writes-the-file-with-state-OPEN", doc["state"] == "OPEN" and doc["call_id"] == CALL_ID and doc["ack"] is None
        and opened[1].startswith("CROSSBOX %s CALL for %s: Close the dell fence call | file org/devices/crossbox/%s.json @" % (cid, seat, cid)), opened[1])
    ok, why = raises(Refused, lambda: a.line(cid), "commit it first")
    rec("line-refused-until-the-file-is-committed", ok, why)
    h.commit(a, a.rel(cid))
    ok, why = raises(Refused, lambda: a.line(cid), "is not on origin yet")
    rec("line-refused-while-the-commit-is-local-only", ok, why)
    h.push(a.root)
    bus_line = a.line(cid)[0]
    rec("line-carries-the-commit-and-no-substance", re.search(r" @[0-9a-f]{7,}$", bus_line) is not None and len(bus_line.split()) < 40, bus_line)

    a.sent(cid, "0a1b2c3d-0000-4000-8000-000000000001", at=stamp(now_dt() - datetime.timedelta(minutes=5)))
    st = a.status(cid)[0]
    rec("status-reads-SENT-NOT-ACKED-with-its-age", "SENT, NOT ACKED (sent 5 min ago" in st, st)

    consumer_line = "[2026-10-08T01:02:03Z] [from 1.0.0_SA_CTO] [tailnet a -> b] " + bus_line
    try:
        b.receive(consumer_line)
        rec("receive-before-the-pull-reads-PULL-FIRST", False, "delivered without the commit")
    except PullFirst as exc:
        inbox_dir = b.root / "org" / "mcp" / "inbox" / SEAT / SEAT_LANE
        rec("receive-before-the-pull-reads-PULL-FIRST", "PULL-FIRST" in str(exc) and not list(inbox_dir.glob("*.md")), str(exc)[:80])
    h.pull(b, a, ff=False)   # the commit object is here, the working tree is not merged: the CVO @bf5cc9cb1e case
    try:
        b.receive(consumer_line)
        rec("receive-with-the-commit-fetched-but-not-merged-reads-PULL-FIRST", False, "delivered onto a path not in the working tree")
    except PullFirst as exc:
        inbox_dir = b.root / "org" / "mcp" / "inbox" / SEAT / SEAT_LANE
        rec("receive-with-the-commit-fetched-but-not-merged-reads-PULL-FIRST",
            "not in this working tree" in str(exc) and "box-sync" in str(exc) and not list(inbox_dir.glob("*.md")), str(exc)[:100])
    h.pull(b, a, ff=True)
    forged = consumer_line.replace(cid, "XB-20200101T000000Z-dead")
    ok, why = raises(Refused, lambda: b.receive(forged), "")
    rec("a-tampered-line-with-the-id-altered-is-refused", ok, why)
    forged = consumer_line.replace(" for %s:" % seat, " for 2.0.0_SA_COO:")
    ok, why = raises(Refused, lambda: b.receive(forged), "")
    rec("a-tampered-line-with-the-seat-altered-is-refused", ok, why)
    res = b.receive(consumer_line)
    inbox_dir = b.root / "org" / "mcp" / "inbox" / SEAT / SEAT_LANE
    landed = list(inbox_dir.glob("*.md"))
    body = landed[0].read_text(encoding="utf-8") if landed else ""
    rec("receive-lands-one-file-in-the-seats-watched-inbox", len(landed) == 1 and res[0].startswith("DELIVERED") and body.startswith("# Message from 1.0.0_SA_CTO")
        and ("body: " + BODY) in body, res[0])
    rec("receive-twice-delivers-once", b.receive(consumer_line)[0].startswith("ALREADY DELIVERED") and len(list(inbox_dir.glob("*.md"))) == 1, "")

    # Present by CHERRY-PICK: B holds the same bytes in a commit of its own, with no ancestry link to A's commit.
    body2 = "docs/body2.md"
    (a.root / body2).write_text("second body\n", encoding="utf-8")
    h.commit(a, body2)
    cid2 = a.open("CALL", b.device, seat, "1.0.0_SA_CTO", "Second call", body2)[0].split()[1]
    h.commit(a, a.rel(cid2))
    h.push(a.root)
    line2 = a.line(cid2)[0]
    sgit(b.root, "fetch", "-q", str(a.root), "HEAD")   # the object is here; nothing merged
    (b.root / body2).write_text("second body\n", encoding="utf-8")
    shutil.copyfile(a.path(cid2), b.path(cid2))
    h.commit(b, body2, b.rel(cid2))
    rc_anc, _, _ = sgit(b.root, "merge-base", "--is-ancestor", line2.rsplit("@", 1)[1], "HEAD")
    res2 = b.receive(line2)
    rec("receive-accepts-a-body-present-by-cherry-pick-with-no-ancestry", rc_anc != 0 and res2[0].startswith("DELIVERED"), "is-ancestor rc=%s; %s" % (rc_anc, res2[0][:80]))

    ok, why = raises(Refused, lambda: a.ack(cid, seat), "receiving box")
    rec("the-sending-box-cannot-ack", ok, why)
    ack_lines = b.ack(cid, seat)
    reply = ack_lines[-1]
    rec("ack-sets-ACKED-and-prints-the-reply-line", b.read(cid)["state"] == "ACKED" and re.fullmatch(
        r"CROSSBOX-ACK %s READ by %s at \d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ" % (cid, re.escape(seat)), reply) is not None, reply)
    a.acked(cid, "[x] [from %s] %s" % (seat, reply), "0a1b2c3d-0000-4000-8000-000000000002")
    st = a.status(cid)[0]
    rec("acked-records-the-reply-on-the-sending-box", a.read(cid)["ack"]["bus_message_id"] and st.startswith("STATUS %s ACKED" % cid), st)

    a.close(cid, "from", "1.0.0_SA_CTO")
    st = a.status(cid)[0]
    rec("one-side-closed-reads-HALF-CLOSED", "HALF-CLOSED (from only" in st and a.read(cid)["state"] == "ACKED", st)
    found = open_calls_reader(a.root / REL_DIR)
    rec("the-open-calls-close-reader-refuses-a-half-closed-call", found is None, "reader returned %r" % (found,))

    h.commit(a, a.rel(cid))
    h.pull(b, a, ff=False)
    b.merge(cid, "FETCH_HEAD")
    merged = b.read(cid)
    rec("merge-folds-the-other-boxs-fields-in", merged["sent"]["bus_message_id"] and merged["closed"]["from_at"] and merged["ack"]["by"] == seat, json.dumps(merged["closed"]))
    b.close(cid, "to", seat)
    st = b.status(cid)[0]
    rec("both-sides-recorded-reads-CLOSED-BOTH", st.startswith("STATUS %s CLOSED-BOTH" % cid) and b.read(cid)["state"] == "CLOSED-BOTH", st)
    found = open_calls_reader(b.root / REL_DIR)
    rec("the-open-calls-close-reader-accepts-CLOSED-BOTH", found == "%s.json" % cid, "reader returned %r" % (found,))

    h.commit(b, b.rel(cid))
    h.pull(a, b, ff=False)
    a.merge(cid, "FETCH_HEAD")
    st = a.status(cid)[0]
    rec("the-sending-box-reads-CLOSED-BOTH-after-the-merge", st.startswith("STATUS %s CLOSED-BOTH" % cid), st)

    opened2 = a.open("ORDER", b.device, seat, "1.0.0_SA_CTO", "Order to an absent seat", BODY)
    cid2 = opened2[0].split()[1]
    h.commit(a, a.rel(cid2))
    ok, why = raises(Refused, lambda: a.withdraw(cid, "1.0.0_SA_CTO", BODY), "is a CALL")
    rec("withdraw-refuses-a-CALL", ok, why)
    ok, why = raises(Refused, lambda: a.withdraw(cid2, "0.4.0_DS_ClientPlatform", BODY), "neither the issuer")
    rec("withdraw-refuses-a-seat-that-is-not-the-issuer-or-its-box-lead", ok, why)
    (a.root / "docs" / "loose2.md").write_text("not committed\n", encoding="utf-8")
    ok, why = raises(Refused, lambda: a.withdraw(cid2, "1.0.0_SA_CTO", "docs/loose2.md"), "Commit it first")
    rec("withdraw-refuses-an-uncommitted-ruling", ok, why)
    wd = a.withdraw(cid2, "1.0.0_SA_CTO", BODY)
    st = a.status(cid2)[0]
    rec("withdraw-reads-WITHDRAWN-and-CLOSED-BOTH-with-no-new-key", st.startswith("STATUS %s WITHDRAWN by 1.0.0_SA_CTO" % cid2)
        and a.read(cid2)["state"] == "CLOSED-BOTH" and a.read(cid2)["ack"] is None and wd[-1].startswith("WITHDRAWN"), st)

    # Superseded close (CVO verdict a803dad6ae): an unread CALL closes on the ACKED successor that carried the same body.
    cid3 = a.open("CALL", b.device, seat, "1.0.0_SA_CTO", "Unread call to an absent seat", BODY)[0].split()[1]
    h.commit(a, a.rel(cid3))
    h.push(a.root)
    a.sent(cid3, "0a1b2c3d-0000-4000-8000-000000000003")
    h.commit(a, a.rel(cid3))
    cidx = a.open("CALL", b.device, seat, "1.0.0_SA_CTO", "A different body", body2)[0].split()[1]
    h.commit(a, a.rel(cidx))
    cid4 = a.open("CALL", b.device, "%s~P2" % SEAT.rsplit("~", 1)[0], "1.0.0_SA_CTO", "Same call re-addressed to a live seat", BODY)[0].split()[1]
    h.commit(a, a.rel(cid4))
    h.push(a.root)
    a.sent(cid4, "0a1b2c3d-0000-4000-8000-000000000004")
    h.commit(a, a.rel(cid4))
    h.push(a.root)
    a.sent(cidx, "0a1b2c3d-0000-4000-8000-000000000006")
    a.acked(cidx, "[x] [from %s] CROSSBOX-ACK %s READ by %s at %s" % (seat, cidx, seat, stamp(now_dt())), "0a1b2c3d-0000-4000-8000-000000000007")
    ok, why = raises(Refused, lambda: a.supersede(cid3, "1.0.0_SA_CTO", BODY, cidx), "differs from the body")
    rec("supersede-refuses-a-successor-whose-body-blob-differs-even-when-acked", ok, why)
    ok, why = raises(Refused, lambda: a.supersede(cid3, "1.0.0_SA_CTO", BODY, cid4), "not acknowledged")
    rec("supersede-refuses-an-unacked-successor", ok, why)
    live = "%s~P2" % SEAT
    reply4 = "CROSSBOX-ACK %s READ by %s at %s" % (cid4, live, stamp(now_dt()))
    a.acked(cid4, "[x] [from %s] %s" % (live, reply4), "0a1b2c3d-0000-4000-8000-000000000005")   # the manager records the reply
    other = json.loads(a.path(cid4).read_text(encoding="utf-8"))
    other["id"] = cid5 = cid4[:-4] + "beef"
    other["to_device"] = "some-other-box"
    a.path(cid5).write_text(json.dumps(other), encoding="utf-8")
    ok, why = raises(Refused, lambda: a.supersede(cid3, "1.0.0_SA_CTO", BODY, cid5), "to_device must match")
    rec("supersede-refuses-a-successor-on-another-box", ok, why)
    ok, why = raises(Refused, lambda: b.supersede(cid, seat, BODY, cid4), "sending")
    rec("supersede-is-a-sending-box-act", ok, why)
    sp = a.supersede(cid3, "1.0.0_SA_CTO", BODY, cid4)
    st = a.status(cid3)[0]
    rec("supersede-reads-SUPERSEDED-and-CLOSED-BOTH-with-no-new-key-and-no-ack",
        st.startswith("STATUS %s SUPERSEDED by %s" % (cid3, cid4)) and a.read(cid3)["state"] == "CLOSED-BOTH"
        and a.read(cid3)["ack"] is None and a.read(cid3)["closed"]["to_by"] == "superseded-by " + cid4 and sp[-1].startswith("SUPERSEDED"), st)
    found = open_calls_reader(a.root / REL_DIR, cid3)
    rec("the-open-calls-close-reader-accepts-a-superseded-close-as-CLOSED-BOTH", found == "%s.json" % cid3, "reader returned %r" % (found,))
    ok, why = raises(Refused, lambda: a.supersede(cid3, "1.0.0_SA_CTO", BODY, cid4), "already has a closed side")
    rec("supersede-twice-is-refused", ok, why)

    bad = json.loads(a.path(cid).read_text(encoding="utf-8"))
    bad["surprise"] = 1
    a.path(cid).write_text(json.dumps(bad), encoding="utf-8")
    ok, why = raises(Refused, lambda: a.read(cid), "unknown key")
    rec("an-unknown-key-in-a-file-is-refused", ok, why)
    out.extend(merge_cases(tmp))   # its own checkouts, under tmp/merge-arms; a merge arm that cannot run is a failed case
    return out


def selftest() -> int:
    tmp = tempfile.mkdtemp(prefix="crossbox-selftest-")
    try:
        cases = run_cases(tmp)
    except Exception as exc:   # a harness that cannot run is a failed selftest, never a pass
        print("ERROR: the selftest could not run: %s: %s" % (type(exc).__name__, exc))
        cases = []
    finally:
        rmtree_force(tmp)
    for name, ok, detail in cases:
        print("%s %s%s" % ("ok  " if ok else "FAIL", name, "" if ok or not detail else "  -- " + detail))
    good = sum(1 for _, ok, _ in cases if ok)
    print("CROSSBOX-SELFTEST cases=%d/%d ok=%s" % (good, len(cases), bool(cases) and good == len(cases)))
    return 0 if cases and good == len(cases) else 1


# ---------------------------------------------------------------- CLI

def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(prog="crossbox-call.py", description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--root", help="the checkout this box is (default: the repository this script lives in); tests only")
    ap.add_argument("--device", help="this box's device name (default: AGENTBUS_DEVICE through lib/devices.py); tests only")
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("open")
    p.add_argument("--kind", required=True)
    p.add_argument("--to-device", required=True)
    p.add_argument("--to-serial", required=True)
    p.add_argument("--from-serial", required=True)
    p.add_argument("--subject", required=True)
    p.add_argument("--body", required=True)
    p.add_argument("--call-id")
    for name in ("line", "status"):
        sub.add_parser(name).add_argument("--id", required=True)
    p = sub.add_parser("sent")
    p.add_argument("--id", required=True)
    p.add_argument("--bus-message-id", required=True)
    p = sub.add_parser("issue")
    p.add_argument("--order", required=True)
    p.add_argument("--to-device")
    sub.add_parser("send-pending").add_argument("--dry-run", action="store_true")
    sub.add_parser("receive").add_argument("--line", required=True)
    p = sub.add_parser("ack")
    p.add_argument("--id", required=True)
    p.add_argument("--by", required=True)
    p = sub.add_parser("acked")
    p.add_argument("--id", required=True)
    p.add_argument("--line", required=True)
    p.add_argument("--bus-message-id", required=True)
    p = sub.add_parser("close")
    p.add_argument("--id", required=True)
    p.add_argument("--side", required=True)
    p.add_argument("--by", required=True)
    p.add_argument("--superseded-by", help="(sending box, --side from) the id of the ACKED file that carried the same body to the same "
                                           "box; closes an unread CALL as SUPERSEDED, on a committed --ruling (CVO verdict a803dad6ae)")
    p.add_argument("--ruling", help="repo-relative path of the committed ruling (required with --superseded-by)")
    p = sub.add_parser("withdraw", help="the issuing box retires an ORDER its named seat never read, on a committed ruling")
    p.add_argument("--id", required=True)
    p.add_argument("--by", required=True)
    p.add_argument("--ruling", required=True, help="repo-relative path of the committed ruling that withdraws it")
    sub.add_parser("list").add_argument("--open", action="store_true")
    p = sub.add_parser("merge")
    p.add_argument("--id", required=True)
    p.add_argument("--ref", required=True)
    return ap


def main(argv: list) -> int:
    args = build_parser().parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.cmd:
        print("usage: crossbox-call.py <open|line|issue|send-pending|sent|receive|ack|acked|close|withdraw|status|list|merge> ... | --selftest", file=sys.stderr)
        return 2
    try:
        dev = devmod()
        box = Box(args.root or TOOL_ROOT, dev.resolve(args.device) if args.device else None)
        if args.cmd == "open":
            lines = box.open(args.kind, args.to_device, args.to_serial, args.from_serial, args.subject, args.body, args.call_id)
        elif args.cmd == "line":
            lines = box.line(args.id)
        elif args.cmd == "issue":
            lines = box.issue(args.order, args.to_device)
        elif args.cmd == "send-pending":
            lines, rc = box.send_pending(args.dry_run)
            print("\n".join(lines))
            return rc
        elif args.cmd == "sent":
            lines = box.sent(args.id, args.bus_message_id)
        elif args.cmd == "receive":
            lines = box.receive(args.line)
        elif args.cmd == "ack":
            lines = box.ack(args.id, args.by)
        elif args.cmd == "acked":
            lines = box.acked(args.id, args.line, args.bus_message_id)
        elif args.cmd == "close" and args.superseded_by:
            if args.side != "from":
                raise Refused("--superseded-by is a sending-box act: --side must be from")
            if not args.ruling:
                raise Refused("--superseded-by needs --ruling (the committed ruling the close rests on)")
            lines = box.supersede(args.id, args.by, args.ruling, args.superseded_by)
        elif args.cmd == "close":
            lines = box.close(args.id, args.side, args.by)
        elif args.cmd == "withdraw":
            lines = box.withdraw(args.id, args.by, args.ruling)
        elif args.cmd == "status":
            lines = box.status(args.id)
        elif args.cmd == "list":
            lines = box.listing(args.open)
        else:
            lines = box.merge(args.id, args.ref)
    except PullFirst as exc:
        print(str(exc))
        return 5
    except Refused as exc:
        print("REFUSED: %s" % exc)
        return 3
    except Exception as exc:   # an unreadable register must stop the tool, never fall back to a built-in list
        if type(exc).__name__ == "RegisterError":
            print(str(exc), file=sys.stderr)
            return 3
        raise
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
