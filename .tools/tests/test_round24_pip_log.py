#!/usr/bin/env python3
"""test_round24_pip_log.py -- the pip log beside the receipt (TO NFRA_CTLPLN.TO-CT-an-1, CT-an-1, FWD-15).

Runs intake_receive.py in-process with THIS interpreter on synthetic py3-none-any wheels in temporary folders. Every pip run
goes to a local wheel with --no-index --no-deps; no request leaves this machine. The check of a log is the function
check_log: it reads the log bytes and reports every forbidden value, every index line and every non-ASCII byte it finds.

HONEST LIMIT (as in the tool): the log shows the command, the pinned environment and what pip printed. It is not a network
trace. LAST line: PIP-LOG arms=<k>/<n> ok=<True|False>
"""
import hashlib
import io
import json
import os
import platform
import shutil
import sys
import tempfile
import traceback
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
INTAKE = os.path.join(REPO, "org", "devices", "intake")
sys.path.insert(0, INTAKE)
import intake_receive as ir  # noqa: E402

DEVICE = "boxlog"
PIN_URL = "http://127.0.0.1:9/simple"
SEP = "--- pip stdout+stderr ---"
RESULTS = []
STATE = {}
TMP_ROOT = tempfile.mkdtemp(prefix="pip-log-test-")


def case(fn):
    name = fn.__name__
    try:
        fn()
        RESULTS.append((name, True, ""))
        print("PASS: %s" % name)
    except Exception as exc:  # noqa: BLE001 - an arm reports every failure
        RESULTS.append((name, False, "%s: %s" % (type(exc).__name__, exc)))
        print("FAIL: %s: %s" % (name, exc))
        traceback.print_exc(file=sys.stdout)
    return fn


class env_set:
    """Sets environment variables for a block and restores the old values after it."""

    def __init__(self, pairs):
        self.pairs = pairs
        self.old = {}

    def __enter__(self):
        for k, v in self.pairs.items():
            self.old[k] = os.environ.get(k)
            os.environ[k] = v
        return self

    def __exit__(self, *exc):
        for k, v in self.old.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        return False


def make_pack(label, wheels, records=None):
    """wheels: {dist: {mod: src}}; records: {dist: verdict}. Returns (pack dir, {dist: wheel file name})."""
    pack = os.path.join(TMP_ROOT, label, "pack")
    os.makedirs(pack)
    names = {}
    for dist, mods in wheels.items():
        names[dist] = os.path.basename(ir.build_synthetic_wheel(pack, dist, "1.0", mods))
        ir.write_check_record(pack, names[dist], verdict=(records or {}).get(dist, "checked"))
    ir.write_manifest(pack)
    return pack, names


def run_prove(pack, scratch):
    buf = io.StringIO()
    with env_set({"AGENTBUS_DEVICE": DEVICE}), redirect_stdout(buf):
        rc, summ = ir.prove_pack(pack, scratch)
    return rc, summ, buf.getvalue()


def run_install(pack, target, dry_run):
    buf = io.StringIO()
    with env_set({"AGENTBUS_DEVICE": DEVICE}), redirect_stdout(buf):
        rc, summ = ir.install_pack(pack, dry_run, "target", None, target)
    return rc, summ, buf.getvalue()


def log_path(pack, wheel, kind):
    return os.path.join(pack, "receipts", "%s.%s-pip.%s.log" % (wheel, kind, DEVICE))


def read_bytes(path):
    with open(path, "rb") as fh:
        return fh.read()


def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()


def read_json(path):
    with open(path, "rb") as fh:
        return json.loads(fh.read().decode("ascii"))


def header_of(data):
    return data.decode("ascii", "replace").split(SEP)[0]


def field(data, key):
    """The value of a header line key=value (the header is the text before the pip separator)."""
    prefix = key + "="
    for line in header_of(data).split("\n"):
        if line.startswith(prefix):
            return line[len(prefix):]
    return None


def check_log(data, forbidden):
    """The instrument: (ok, reasons). A reason for each non-ASCII byte, each forbidden value found, each index line."""
    reasons = []
    if any(b > 127 for b in data):
        reasons.append("non-ASCII byte in log")
    text = data.decode("ascii", "replace")
    for value in forbidden:
        if value in text:
            reasons.append("log holds forbidden value %s" % value)
    for line in text.split("\n"):
        if line.startswith("Looking in indexes"):
            reasons.append("index line present: %s" % line)
    return (not reasons), reasons


@case
def arm_a_prove_writes_log():
    pack, names = make_pack("arm_a", {"logalpha": {"logalpha": "NAME = 'a'\n"}})
    rc, summ, out = run_prove(pack, os.path.join(TMP_ROOT, "arm_a", "scratch"))
    assert rc == 0 and summ["ok"] and summ["installed"] == 1, (rc, summ, out)
    wheel = names["logalpha"]
    path = log_path(pack, wheel, "prove")
    assert os.path.isfile(path), path
    data = read_bytes(path)
    assert all(b < 128 for b in data), "non-ASCII byte in the prove log"
    assert b"\r" not in data, "a CR in the log (LF line ends only)"
    assert header_of(data).startswith("INTAKE-PIP-LOG schema=1\n"), data[:80]
    command = json.loads(field(data, "command"))
    assert "--no-index" in command and "--no-deps" in command, command
    assert field(data, "rc") == "0", field(data, "rc")
    assert field(data, "device") == DEVICE and field(data, "kind") == "prove", data[:300]
    assert field(data, "python") == platform.python_version(), field(data, "python")
    assert "PIP_NO_INDEX=1" in field(data, "env_pins") and "PIP_DISABLE_PIP_VERSION_CHECK=1" in field(data, "env_pins")
    STATE["pack_a"] = pack
    STATE["wheel_a"] = wheel


@case
def arm_b_receipt_names_the_log_with_matching_hashes():
    pack, wheel = STATE["pack_a"], STATE["wheel_a"]
    rec = read_json(ir.receipt_path(pack, wheel, DEVICE))
    pl = rec.get("pip_log")
    assert isinstance(pl, dict), rec
    data = read_bytes(log_path(pack, wheel, "prove"))
    assert pl["file"] == "%s.prove-pip.%s.log" % (wheel, DEVICE), pl
    assert pl["sha256"] == sha_bytes(data), (pl["sha256"], sha_bytes(data))
    assert pl["bytes"] == len(data) == os.path.getsize(log_path(pack, wheel, "prove")), (pl["bytes"], len(data))
    assert rec["received_sha256"] == sha_bytes(read_bytes(os.path.join(pack, wheel))), rec["received_sha256"]


@case
def arm_c_install_writes_install_log_and_receipt_names_it():
    pack, wheel = STATE["pack_a"], STATE["wheel_a"]
    target = os.path.join(TMP_ROOT, "arm_c", "new_target")
    rc, summ, out = run_install(pack, target, False)
    assert rc == 0 and summ["ok"] and summ["installed"] == 1, (rc, summ, out)
    assert os.path.isfile(os.path.join(target, "logalpha", "__init__.py")), target
    path = log_path(pack, wheel, "install")
    assert os.path.isfile(path), path
    data = read_bytes(path)
    assert field(data, "kind") == "install" and field(data, "rc") == "0", header_of(data)
    rec = read_json(os.path.join(pack, "receipts", "%s.install.%s.json" % (wheel, DEVICE)))
    pl = rec.get("pip_log")
    assert isinstance(pl, dict) and pl["file"] == "%s.install-pip.%s.log" % (wheel, DEVICE), rec
    assert pl["sha256"] == sha_bytes(data) and pl["bytes"] == len(data), (pl, len(data))


@case
def arm_d_parent_index_values_never_reach_the_log():
    findlinks = tempfile.mkdtemp(prefix="pip-log-findlinks-")
    try:
        pack, names = make_pack("arm_d", {"logdelta": {"logdelta": "NAME = 'd'\n"}})
        with env_set({"PIP_INDEX_URL": PIN_URL, "PIP_FIND_LINKS": findlinks}):
            rc, summ, out = run_prove(pack, os.path.join(TMP_ROOT, "arm_d", "scratch"))
        assert rc == 0 and summ["ok"], (rc, summ, out)
        data = read_bytes(log_path(pack, names["logdelta"], "prove"))
        names_removed = (field(data, "inherited_pip_vars_removed") or "").split(",")
        assert "PIP_INDEX_URL" in names_removed and "PIP_FIND_LINKS" in names_removed, names_removed
        ok, reasons = check_log(data, [PIN_URL, "127.0.0.1", findlinks])
        assert ok, reasons
        assert "PIP_NO_INDEX=1" in field(data, "env_pins"), field(data, "env_pins")
    finally:
        shutil.rmtree(findlinks, ignore_errors=True)


@case
def arm_e_control_the_check_sees_an_index_line():
    hand = ("INTAKE-PIP-LOG schema=1\ndevice=x\nkind=prove\ncommand=[]\n%s\n"
            "Looking in indexes: %s\nSuccessfully installed x-1.0\n" % (SEP, PIN_URL)).encode("ascii")
    ok, reasons = check_log(hand, [PIN_URL, "127.0.0.1"])
    assert ok is False, "the check passed a log holding an index line"
    assert any(r.startswith("index line present") for r in reasons), reasons
    assert any("forbidden value" in r for r in reasons), reasons


@case
def arm_f_refused_run_writes_no_log_and_no_key():
    pack, names = make_pack("arm_f", {"refpkg": {"refpkg": "X = 1\n"}}, records={"refpkg": "not_checked"})
    rc, summ, out = run_prove(pack, os.path.join(TMP_ROOT, "arm_f", "scratch"))
    assert rc == 1 and summ["refused"] == 1 and summ["installed"] == 0, (rc, summ, out)
    wheel = names["refpkg"]
    assert not os.path.exists(log_path(pack, wheel, "prove")), "a refused prove wrote a log"
    rec = read_json(ir.receipt_path(pack, wheel, DEVICE))
    assert rec["outcome"] == "refused" and "pip_log" not in rec, rec
    assert not [n for n in os.listdir(os.path.join(pack, "receipts")) if "pip" in n], "a pip file for a refused prove"
    # a dry-run install of a proved pack writes no install log and no install record
    pack2, names2 = make_pack("arm_f_dry", {"drypkg": {"drypkg": "X = 2\n"}})
    rc2, _, _ = run_prove(pack2, os.path.join(TMP_ROOT, "arm_f_dry", "scratch"))
    assert rc2 == 0, rc2
    rc3, summ3, out3 = run_install(pack2, os.path.join(TMP_ROOT, "arm_f_dry", "target"), True)
    assert rc3 == 0 and summ3["ok"] and "DRY-RUN" in out3, (rc3, out3)
    assert not [n for n in os.listdir(os.path.join(pack2, "receipts")) if "install" in n], "a dry run wrote an install file"


@case
def arm_g_receipt_without_pip_log_still_clears_dry_run():
    src = STATE["pack_a"]
    pack = os.path.join(TMP_ROOT, "arm_g", "pack")
    shutil.copytree(src, pack)
    wheel = STATE["wheel_a"]
    rp = ir.receipt_path(pack, wheel, DEVICE)
    rec = read_json(rp)
    assert "pip_log" in rec, "the receipt to age has no pip_log key"
    del rec["pip_log"]
    with open(rp, "w", encoding="ascii", newline="\n") as fh:
        json.dump(rec, fh, indent=2, ensure_ascii=True)
        fh.write("\n")
    assert "pip_log" not in read_json(rp), "the key was not removed"
    rc, summ, out = run_install(pack, os.path.join(TMP_ROOT, "arm_g", "target"), True)
    assert rc == 0 and summ["ok"], (rc, summ, out)
    assert "RECEIPT-OK: %s" % wheel in out and "DRY-RUN" in out, out


def main():
    try:
        total = len(RESULTS)
        passed = sum(1 for _, ok, _ in RESULTS if ok)
        ok = passed == total and total > 0
    finally:
        shutil.rmtree(TMP_ROOT, ignore_errors=True)
    for name, good, why in RESULTS:
        if not good:
            print("FAILED ARM: %s -- %s" % (name, why))
    print("PIP-LOG arms=%d/%d ok=%s" % (passed, total, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
