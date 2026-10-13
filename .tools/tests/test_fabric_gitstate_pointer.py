"""Offline tests for the fabric-gitstate integrate pointer (NFRA_MCPORTAL MP-n-3)."""
import importlib.util
import json
import os
import sys
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = importlib.util.spec_from_file_location("fabric_gitstate", os.path.join(HERE, "..", "fabric-gitstate.py"))
fg = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fg)

BOX = "tbox"
PTR = fg.PREFIX + "/box=" + BOX + "/last_integrate.json"


class Fake:
    def __init__(self, fail_key=None):
        self.calls = []
        self.fail_key = fail_key

    def put_object(self, **kw):
        self.calls.append(kw)
        if kw["Key"] == self.fail_key:
            raise RuntimeError("boom")


def run(args, fake, capsys=None):
    made = []

    def mk(*a, **k):
        made.append(fake)
        return fake

    fake_boto = mock.MagicMock()
    fake_boto.client.side_effect = mk
    with mock.patch.dict(os.environ, {"AGENTBUS_DEVICE": BOX}), \
            mock.patch.object(fg, "git", return_value=(0, "")), \
            mock.patch.dict(sys.modules, {"boto3": fake_boto}):
        rc = fg.main(args)
    return rc, made


def keys(fake):
    return [c["Key"] for c in fake.calls]


def test_pointer_written_on_integrate_only():
    f = Fake()
    run(["--mode", "integrate"], f)
    assert PTR in keys(f)
    for args in (["--mode", "box"], ["--mode", "manual"], ["--mode", "integrate", "--dry-run"]):
        g = Fake()
        run(args, g)
        assert PTR not in keys(g)


def test_pointer_key_uses_prefix_and_box():
    f = Fake()
    _rc, made = run(["--mode", "integrate"], f)
    assert len(f.calls) == 3
    assert PTR in keys(f)
    assert all(c["Bucket"] == fg.BUCKET for c in f.calls)
    assert len(made) == 1 and made[0] is f


def test_pointer_rc_and_at_join_the_pass_record():
    f = Fake()
    rc, _ = run(["--mode", "integrate", "--rc", "3", "--note", "x" * 300], f)
    assert rc == 0
    ptr = json.loads([c for c in f.calls if c["Key"] == PTR][0]["Body"])
    rec = json.loads([c for c in f.calls if c["Key"].endswith("latest.json")][0]["Body"])
    assert set(ptr) == {"at", "rc", "note"}
    assert ptr["rc"] == 3 and ptr["at"] == rec["at"] and len(ptr["note"]) == 200
    [c for c in f.calls if c["Key"] == PTR][0]["Body"].decode("ascii")


def test_failed_pointer_put_reported_and_others_attempted(capsys):
    ok = Fake()
    rc_ok, _ = run(["--mode", "integrate"], ok)
    capsys.readouterr()
    f = Fake(fail_key=PTR)
    rc, _ = run(["--mode", "integrate"], f)
    last = capsys.readouterr().out.strip().splitlines()[-1]
    assert len(keys(f)) == 3 and keys(f)[-1] == PTR
    assert "pointer=no:RuntimeError" in last and "put=yes" in last
    assert rc == rc_ok
