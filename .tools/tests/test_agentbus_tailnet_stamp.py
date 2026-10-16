"""NFRA_CTLPLN TO-CT-b-3 CT2b3-AC2: every bus message carries the sender's and the recipient's tailnet names.

No real SQS call: a stub `aws` first on PATH records its arguments and answers send/receive/delete from fixtures.
The tailnet names are read from the device register (org/devices/DEVICES.json, or the fixture OPAL_DEVICE_REGISTER
points at) and never typed here.
"""
import json
import os
import pathlib
import shutil
import stat
import subprocess
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
SCRIPT = ROOT / ".tools" / "agentbus-sqs.sh"
REGISTER = ROOT / "org" / "devices" / "DEVICES.json"
BASH = shutil.which("bash")

FAKE_AWS = """#!/usr/bin/env bash
{ printf 'ARGS'; for a in "$@"; do printf '\\t%s' "$a"; done; printf '\\n'; } >> "$FAKE_AWS_LOG"
case "$2" in
  send-message) echo '{"MessageId": "11111111-2222-3333-4444-555555555555"}' ;;
  receive-message) cat "$FAKE_RECV_JSON" ;;
  delete-message) : ;;
  *) echo "stub aws: unexpected $*" >&2; exit 9 ;;
esac
"""

register = json.loads(REGISTER.read_text(encoding="utf-8"))
BOXES = [d["name"] for d in register["devices"]]
TAILNET = {d["name"]: d["tailnet_name"] for d in register["devices"]}


@pytest.fixture
def stub(tmp_path):
    bindir = tmp_path / "bin"
    bindir.mkdir()
    aws = bindir / "aws"
    aws.write_text(FAKE_AWS, encoding="utf-8", newline="\n")
    aws.chmod(aws.stat().st_mode | stat.S_IXUSR)
    log = tmp_path / "aws.log"
    log.write_text("", encoding="utf-8")
    recv = tmp_path / "recv.json"
    recv.write_text("{}", encoding="utf-8")
    return {"bindir": bindir, "log": log, "recv": recv, "tmp": tmp_path}


def run(stub, args, device, extra_env=None):
    env = dict(os.environ)
    env.update({
        "PATH": str(stub["bindir"]) + os.pathsep + env["PATH"],
        "FAKE_AWS_LOG": str(stub["log"]),
        "FAKE_RECV_JSON": str(stub["recv"]),
        "AGENTBUS_DEVICE": device,
        "AGENTBUS_REFUSED_DIR": str(stub["tmp"] / "refused"),
    })
    env.pop("OPAL_DEVICE_REGISTER", None)
    env.update(extra_env or {})
    return subprocess.run([BASH, str(SCRIPT)] + args, env=env, capture_output=True, text=True,
                          encoding="utf-8", cwd=str(ROOT), timeout=120)


def calls(stub, op):
    out = []
    for line in stub["log"].read_text(encoding="utf-8").splitlines():
        parts = line.split("\t")[1:]
        if len(parts) > 1 and parts[1] == op:
            out.append(parts)
    return out


def arg_after(parts, flag):
    return parts[parts.index(flag) + 1]


def test_register_holds_the_four_boxes():
    assert sorted(BOXES) == ["dell1", "dell2", "laptop", "sitez"]
    assert all(TAILNET[b] for b in BOXES)


@pytest.mark.parametrize("sender", BOXES)
def test_send_stamps_sender_and_recipient_tailnet_names(stub, sender):
    recipient = BOXES[(BOXES.index(sender) + 1) % len(BOXES)]
    serial = "0.9.0_WK_TEST~1"
    r = run(stub, ["send", recipient, serial, "hello bus"], sender)
    assert r.returncode == 0, r.stdout + r.stderr
    sent = calls(stub, "send-message")
    assert len(sent) == 1
    attrs = arg_after(sent[0], "--message-attributes")
    body = arg_after(sent[0], "--message-body")
    assert "from_tailnet={StringValue=%s,DataType=String}" % TAILNET[sender] in attrs
    assert "to_tailnet={StringValue=%s,DataType=String}" % TAILNET[recipient] in attrs
    assert "from={StringValue=%s,DataType=String}" % serial in attrs  # the existing attribute is kept
    assert "[from %s] [tailnet %s -> %s] hello bus" % (serial, TAILNET[sender], TAILNET[recipient]) in body


def test_send_to_an_alias_stamps_the_register_tailnet_name(stub):
    alias = register["devices"][0]["aliases"][0]
    owner = register["devices"][0]["name"]
    r = run(stub, ["send", alias, "0.9.0_WK_TEST~1", "x"], "sitez")
    assert r.returncode == 0, r.stdout + r.stderr
    attrs = arg_after(calls(stub, "send-message")[0], "--message-attributes")
    assert "to_tailnet={StringValue=%s," % TAILNET[owner] in attrs


def test_send_to_an_inbox_carrying_sender_addresses_its_queue_and_stamps_its_tailnet(stub):
    # Andrew-direct 2026-10-16 ~09:1xZ ("give muse the inbox sqs"): ms stays a `senders` row but carries an inbound_queue.
    ms = [s for s in register["senders"] if s["name"] == "ms"][0]
    assert ms.get("inbound_queue")
    r = run(stub, ["send", "ms", "0.9.0_WK_TEST~1", "hello ms"], "sitez")
    assert r.returncode == 0, r.stdout + r.stderr
    sent = calls(stub, "send-message")
    assert len(sent) == 1
    assert arg_after(sent[0], "--queue-url").endswith("/" + ms["inbound_queue"])
    assert arg_after(sent[0], "--message-group-id") == "opal-sqschat"
    attrs = arg_after(sent[0], "--message-attributes")
    assert "to_tailnet={StringValue=%s,DataType=String}" % ms["tailnet_name"] in attrs
    assert "from_tailnet={StringValue=%s,DataType=String}" % TAILNET["sitez"] in attrs


def test_an_inbox_carrying_sender_is_still_not_a_box(stub):
    # the register's contract: a sender is never in devices[], so no box list or placement value sees it
    names = subprocess.run([sys.executable, str(ROOT / "lib" / "devices.py"), "names"], capture_output=True, text=True,
                           encoding="utf-8", cwd=str(ROOT), timeout=60).stdout.split()
    placement = subprocess.run([sys.executable, str(ROOT / "lib" / "devices.py"), "placement"], capture_output=True,
                               text=True, encoding="utf-8", cwd=str(ROOT), timeout=60).stdout.split()
    assert sorted(names) == sorted(BOXES)
    assert "ms" not in names and "ms" not in placement
    r = run(stub, ["send", "nobody", "0.9.0_WK_TEST~1", "x"], "sitez")
    assert r.returncode != 0 and calls(stub, "send-message") == []


def test_send_from_an_unregistered_box_is_refused_and_sends_nothing(stub):
    r = run(stub, ["send", "laptop", "0.9.0_WK_TEST~1", "x"], "not-a-box")
    assert r.returncode != 0
    assert calls(stub, "send-message") == []


def fifth_box_register(tmp_path):
    reg = json.loads(REGISTER.read_text(encoding="utf-8"))
    reg["devices"].append({
        "name": "dell3", "aliases": [], "role": "execution", "inbound_queue": "agentbus-global-dell3-queue.fifo",
        "tailnet_name": "dell3-tailnet-fixture"})
    path = tmp_path / "DEVICES.fixture.json"
    path.write_text(json.dumps(reg), encoding="utf-8")
    return path


def test_register_is_read_not_typed_a_fifth_box_stamps_without_a_script_edit(stub):
    fixture = fifth_box_register(stub["tmp"])
    env = {"OPAL_DEVICE_REGISTER": str(fixture)}
    r = run(stub, ["send", "laptop", "0.9.0_WK_TEST~1", "from the fifth"], "dell3", env)
    assert r.returncode == 0, r.stdout + r.stderr
    r = run(stub, ["send", "dell3", "0.9.0_WK_TEST~1", "to the fifth"], "laptop", env)
    assert r.returncode == 0, r.stdout + r.stderr
    first, second = calls(stub, "send-message")
    a1 = arg_after(first, "--message-attributes")
    a2 = arg_after(second, "--message-attributes")
    assert "from_tailnet={StringValue=dell3-tailnet-fixture," in a1
    assert "to_tailnet={StringValue=%s," % TAILNET["laptop"] in a1
    assert "from_tailnet={StringValue=%s," % TAILNET["laptop"] in a2
    assert "to_tailnet={StringValue=dell3-tailnet-fixture," in a2


def message(mid, handle, sender_tailnet, text="body"):
    attrs = {"from": {"StringValue": "0.9.0_WK_TEST~1", "DataType": "String"}}
    if sender_tailnet is not None:
        attrs["from_tailnet"] = {"StringValue": sender_tailnet, "DataType": "String"}
    return {"MessageId": mid, "ReceiptHandle": handle, "Body": text, "MessageAttributes": attrs}


def refused_records(stub):
    d = stub["tmp"] / "refused"
    return sorted(d.glob("*.json")) if d.is_dir() else []


def test_receive_refuses_records_and_deletes_an_unheld_sender_and_delivers_the_rest(stub):
    good = message("id-good", "handle-good", TAILNET["sitez"], "from a held box")
    rogue = message("id-rogue", "handle-rogue", "rogue-box.example", "from a stranger")
    bare = message("id-bare", "handle-bare", None, "no stamp at all")
    stub["recv"].write_text(json.dumps({"Messages": [good, rogue, bare]}), encoding="utf-8")
    r = run(stub, ["recv"], "laptop")
    assert r.returncode == 4, r.stdout + r.stderr
    # held sender and the UNSTAMPED message are delivered (the latter with a WARN naming the serial)
    assert "id-good" in r.stdout and "from a held box" in r.stdout
    assert "id-bare" in r.stdout and "no stamp at all" in r.stdout
    assert "WARN agentbus unstamped sender=0.9.0_WK_TEST~1" in r.stdout
    # the unheld sender is NOT delivered; it is REFUSED with the reason and a record path
    assert "from a stranger" not in r.stdout
    line = [ln for ln in r.stdout.splitlines() if ln.startswith("REFUSED agentbus")]
    assert len(line) == 1
    assert "sender_tailnet=rogue-box.example" in line[0] and "reason=" in line[0] and "record=" in line[0]
    # the whole message (body and attributes) is recorded at <stamp>_<message id>.json ...
    recs = refused_records(stub)
    assert len(recs) == 1 and recs[0].name.endswith("_id-rogue.json")
    assert recs[0].name in line[0]
    saved = json.loads(recs[0].read_text(encoding="utf-8"))["message"]
    assert saved["Body"] == "from a stranger"
    assert saved["MessageAttributes"]["from_tailnet"]["StringValue"] == "rogue-box.example"
    # ... and every message is deleted: the refused one (never blocks the FIFO group) and the two delivered
    deleted = sorted(arg_after(c, "--receipt-handle") for c in calls(stub, "delete-message"))
    assert deleted == ["handle-bare", "handle-good", "handle-rogue"]


def test_receive_delivers_unstamped_mail_with_a_warn_and_refuses_nothing(stub):
    stub["recv"].write_text(json.dumps({"Messages": [message("id-old", "handle-old", None, "from an old box")]}),
                            encoding="utf-8")
    r = run(stub, ["recv"], "laptop")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "WARN agentbus unstamped sender=0.9.0_WK_TEST~1" in r.stdout
    assert "from an old box" in r.stdout and "REFUSED" not in r.stdout
    assert refused_records(stub) == []
    assert [arg_after(c, "--receipt-handle") for c in calls(stub, "delete-message")] == ["handle-old"]


def test_receive_delivers_and_deletes_when_every_sender_is_held(stub):
    msgs = [message("id-%d" % i, "handle-%d" % i, TAILNET[b], "msg %d" % i) for i, b in enumerate(BOXES)]
    stub["recv"].write_text(json.dumps({"Messages": msgs}), encoding="utf-8")
    r = run(stub, ["recv"], "laptop")
    assert r.returncode == 0, r.stdout + r.stderr
    assert "REFUSED" not in r.stdout + r.stderr
    deleted = sorted(arg_after(c, "--receipt-handle") for c in calls(stub, "delete-message"))
    assert deleted == sorted("handle-%d" % i for i in range(len(BOXES)))


def test_receive_judges_by_the_register_it_reads(stub):
    stub["recv"].write_text(json.dumps({"Messages": [message("id-5", "handle-5", "dell3-tailnet-fixture", "fifth")]}),
                            encoding="utf-8")
    fixture = fifth_box_register(stub["tmp"])
    ok = run(stub, ["recv"], "laptop", {"OPAL_DEVICE_REGISTER": str(fixture)})
    assert ok.returncode == 0, ok.stdout + ok.stderr
    assert "fifth" in ok.stdout and refused_records(stub) == []
    stub["log"].write_text("", encoding="utf-8")
    refused = run(stub, ["recv"], "laptop")
    assert refused.returncode == 4
    assert "REFUSED agentbus sender_tailnet=dell3-tailnet-fixture" in refused.stdout
    assert len(refused_records(stub)) == 1
    assert [arg_after(c, "--receipt-handle") for c in calls(stub, "delete-message")] == ["handle-5"]


# --- the consumer (`watch` primary path): the same check, through a fake boto3 --------------------------------
CONSUMER = ROOT / ".tools" / "agentbus-consumer.py"

FAKE_BOTO3 = r"""
import json, os, time
class _Client:
    def __init__(self):
        self.sent = False
    def receive_message(self, **kw):
        if not self.sent:
            self.sent = True
            return json.load(open(os.environ["FAKE_RECV_JSON"]))
        time.sleep(0.2)
        return {}
    def delete_message(self, **kw):
        with open(os.environ["FAKE_DELETE_LOG"], "a") as fh:
            fh.write(kw["ReceiptHandle"] + "\n")
def client(*a, **k):
    return _Client()
"""


def run_consumer(stub, messages, extra_env=None):
    fakedir = stub["tmp"] / "fakeboto"
    fakedir.mkdir(exist_ok=True)
    (fakedir / "boto3.py").write_text(FAKE_BOTO3, encoding="utf-8")
    stub["recv"].write_text(json.dumps({"Messages": messages}), encoding="utf-8")
    dlog = stub["tmp"] / "deleted.log"
    dlog.write_text("", encoding="utf-8")
    env = dict(os.environ)
    env.update({"PYTHONPATH": str(fakedir), "FAKE_RECV_JSON": str(stub["recv"]), "FAKE_DELETE_LOG": str(dlog),
                "AGENTBUS_MAX_SECONDS": "2", "AGENTBUS_REFUSED_DIR": str(stub["tmp"] / "refused")})
    env.pop("OPAL_DEVICE_REGISTER", None)
    env.update(extra_env or {})
    r = subprocess.run([sys.executable, str(CONSUMER), "--queue-url", "http://stub", "--device", "laptop"],
                       env=env, capture_output=True, text=True, encoding="utf-8", cwd=str(ROOT), timeout=60)
    return r, dlog.read_text(encoding="utf-8").split()


def test_consumer_refuses_records_and_deletes_an_unheld_sender_and_delivers_held_and_unstamped(stub):
    msgs = [message("id-good", "handle-good", TAILNET["dell1"], "from a held box"),
            message("id-rogue", "handle-rogue", "rogue-box.example", "from a stranger"),
            message("id-bare", "handle-bare", None, "no stamp at all")]
    r, deleted = run_consumer(stub, msgs)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "[AGENTBUS -> laptop] [id id-good] from a held box" in r.stdout
    assert "[AGENTBUS -> laptop] [id id-bare] no stamp at all" in r.stdout
    assert "WARN agentbus unstamped sender=0.9.0_WK_TEST~1" in r.stdout
    assert "from a stranger" not in r.stdout
    line = [ln for ln in r.stdout.splitlines() if ln.startswith("REFUSED agentbus")]
    assert len(line) == 1 and "sender_tailnet=rogue-box.example" in line[0] and "record=" in line[0]
    recs = refused_records(stub)
    assert len(recs) == 1 and recs[0].name.endswith("_id-rogue.json")
    assert json.loads(recs[0].read_text(encoding="utf-8"))["message"]["Body"] == "from a stranger"
    assert sorted(deleted) == ["handle-bare", "handle-good", "handle-rogue"]


def test_consumer_reads_the_same_register(stub):
    fixture = fifth_box_register(stub["tmp"])
    msgs = [message("id-5", "handle-5", "dell3-tailnet-fixture", "fifth")]
    r, deleted = run_consumer(stub, msgs, {"OPAL_DEVICE_REGISTER": str(fixture)})
    assert "[id id-5] fifth" in r.stdout and refused_records(stub) == [] and deleted == ["handle-5"]
    r, deleted = run_consumer(stub, msgs)
    assert "REFUSED agentbus sender_tailnet=dell3-tailnet-fixture" in r.stdout and "[id id-5]" not in r.stdout
    assert len(refused_records(stub)) == 1 and deleted == ["handle-5"]
