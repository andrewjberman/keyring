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


def test_receive_refuses_a_sender_tailnet_name_the_register_does_not_hold(stub):
    good = message("id-good", "handle-good", TAILNET["sitez"], "from a held box")
    rogue = message("id-rogue", "handle-rogue", "rogue-box.example", "from a stranger")
    bare = message("id-bare", "handle-bare", None, "no stamp at all")
    stub["recv"].write_text(json.dumps({"Messages": [good, rogue, bare]}), encoding="utf-8")
    r = run(stub, ["recv"], "laptop")
    assert r.returncode == 4, r.stdout + r.stderr
    # the held sender's message is delivered, with its id, and the other two are refused loudly with the reason
    assert "id-good" in r.stdout and "from a held box" in r.stdout
    assert "from a stranger" not in r.stdout and "no stamp at all" not in r.stdout
    assert "REFUSED [id id-rogue]" in r.stdout and "rogue-box.example" in r.stdout
    assert "REFUSED [id id-bare]" in r.stdout and "ABSENT" in r.stdout
    # only the delivered message is deleted; the refused two stay on the queue (no silent drop)
    deleted = [arg_after(c, "--receipt-handle") for c in calls(stub, "delete-message")]
    assert deleted == ["handle-good"]


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
    assert "fifth" in ok.stdout
    stub["log"].write_text("", encoding="utf-8")
    refused = run(stub, ["recv"], "laptop")
    assert refused.returncode == 4
    assert "REFUSED [id id-5]" in refused.stdout
    assert calls(stub, "delete-message") == []
