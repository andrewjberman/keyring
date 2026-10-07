#!/usr/bin/env python3
"""Test for intake_receive.py: synthetic py3-none-any wheels and hand-written check records in temporary pack folders.
Runs with THIS interpreter. Every pip command goes to a local wheel file with --no-index --no-deps; no request leaves
this machine. LAST line: INTAKE-RECEIVE-TEST cases=<k>/<n> ok=<True|False>"""
import ast
import io
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import traceback
from contextlib import redirect_stdout

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import intake_check as ic  # noqa: E402
import intake_receive as ir  # noqa: E402

TOOL = os.path.join(HERE, "intake_receive.py")
RESULTS = []
TMP_ROOT = tempfile.mkdtemp(prefix="intake-test-")


def case(fn):
    name = fn.__name__
    try:
        fn()
        RESULTS.append((name, True, ""))
        print("PASS: %s" % name)
    except Exception as exc:  # noqa: BLE001 - a test harness reports every failure
        RESULTS.append((name, False, "%s: %s" % (type(exc).__name__, exc)))
        print("FAIL: %s: %s" % (name, exc))
        traceback.print_exc(file=sys.stdout)
    return fn


def new_pack(label, wheels, records=None, shape="list"):
    """wheels: {dist: {mod: src}}; records: {dist: verdict} (default checked). Returns (pack dir, {dist: wheel name})."""
    pack = os.path.join(TMP_ROOT, label, "pack")
    os.makedirs(pack)
    names = {}
    for dist, mods in wheels.items():
        names[dist] = os.path.basename(ir.build_synthetic_wheel(pack, dist, "1.0", mods))
        ir.write_check_record(pack, names[dist], verdict=(records or {}).get(dist, "checked"))
    ir.write_manifest(pack, shape)
    return pack, names


def scratch_for(label):
    return os.path.join(TMP_ROOT, label, "scratch")


def run_prove(pack, scratch, device="testbox"):
    buf = io.StringIO()
    old = os.environ.get("AGENTBUS_DEVICE")
    os.environ["AGENTBUS_DEVICE"] = device
    try:
        with redirect_stdout(buf):
            rc, summ = ir.prove_pack(pack, scratch)
    finally:
        if old is None:
            os.environ.pop("AGENTBUS_DEVICE", None)
        else:
            os.environ["AGENTBUS_DEVICE"] = old
    return rc, summ, buf.getvalue()


def read_receipt(pack, wheel, device="testbox"):
    with open(ir.receipt_path(pack, wheel, device), "rb") as fh:
        return json.loads(fh.read().decode("ascii"))


def cli(*args, env_extra=None, drop_device=False):
    env = dict(os.environ)
    if drop_device:
        env.pop("AGENTBUS_DEVICE", None)
    env.update(env_extra or {})
    cp = subprocess.run([sys.executable, TOOL] + list(args), capture_output=True, text=True, env=env, timeout=110)
    lines = [ln for ln in cp.stdout.splitlines() if ln.strip()]
    return cp.returncode, (lines[-1] if lines else ""), cp.stdout


GOOD = {"alphapkg": {"alphapkg": "NAME = 'alpha'\n"}, "betapkg": {"betapkg": "NAME = 'beta'\n"}}
PACK_GOOD, NAMES_GOOD = new_pack("good", GOOD)
SCR_GOOD = scratch_for("good")
MIXED = {
    "unchk": {"unchkpkg": "X = 1\n"},
    "flip": {"flippkg": "X = 1\n"},
    "needdep": {"needdeppkg": "import not_a_real_dep_zzz\n"},
    "ownfail": {"ownfailpkg": "import ownfailpkg.absent_submodule\n"},
    "nomod": {},
}
PACK_MIXED, NAMES_MIXED = new_pack("mixed", MIXED, records={"unchk": "not_checked"})
# one byte flipped AFTER the manifest and record were written
_fp = os.path.join(PACK_MIXED, NAMES_MIXED["flip"])
with open(_fp, "rb") as _fh:
    _b = bytearray(_fh.read())
_b[-30] ^= 0xFF
with open(_fp, "wb") as _fh:
    _fh.write(bytes(_b))
SCR_MIXED = scratch_for("mixed")
STATE = {}


@case
def case_two_checked_wheels_verify():
    res = ir.verify_pack(PACK_GOOD)
    assert res["ok"] and res["verified"] == 2 and res["checked"] == 2 and not res["stray"], res
    rc, last, _ = cli("verify", "--from", PACK_GOOD)
    assert rc == 0 and last == "INTAKE-VERIFY pack=pack wheels=2 verified=2 checked=2 stray=0 ok=True", last


@case
def case_manifest_shapes_both_accepted():
    pack, _ = new_pack("shape_obj", {"shapepkg": {"shapepkg": "X = 1\n"}}, shape="object")
    with open(os.path.join(pack, "MANIFEST.json"), "rb") as fh:
        assert isinstance(json.loads(fh.read().decode("ascii")), dict)
    assert ir.verify_pack(pack)["ok"], "object-with-files shape refused"
    assert ir.verify_pack(PACK_GOOD)["ok"], "bare list shape refused"


@case
def case_two_checked_prove_install_import_receipts():
    rc, summ, out = run_prove(PACK_GOOD, SCR_GOOD)
    STATE["good_out"] = out
    assert rc == 0 and summ["installed"] == 2 and summ["imported"] == 2 and summ["refused"] == 0 and summ["ok"], summ
    for dist, wheel in NAMES_GOOD.items():
        rec = read_receipt(PACK_GOOD, wheel)
        assert rec["schema"] == "intake-receipt/1" and rec["device"] == "testbox", rec
        assert rec["outcome"] == "installed_imported" and rec["install"]["rc"] == 0, rec
        assert rec["received_sha256"] == ir.sha256_file(os.path.join(PACK_GOOD, wheel)), rec
        assert rec["check_record_sha256"] == ir.sha256_file(os.path.join(PACK_GOOD, wheel + ".check.json")), rec
        assert rec["imports"] and rec["imports"][0]["module"] == dist and rec["imports"][0]["rc"] == 0, rec
        for key in ("python", "file_name", "at", "reason"):
            assert key in rec, key
        assert os.path.isfile(os.path.join(SCR_GOOD, ir.stem_of(wheel), dist, "__init__.py"))
    # each wheel in its OWN target: neither package leaked into the other's target
    assert not os.path.exists(os.path.join(SCR_GOOD, ir.stem_of(NAMES_GOOD["alphapkg"]), "betapkg"))
    # receipts live in the pack, and the pack verifies with receipts/ present
    assert ir.verify_pack(PACK_GOOD)["ok"]


@case
def case_prove_cli_last_line_shape():
    # a second prove on a fresh scratch through the CLI, device from the environment
    rc, last, _ = cli("prove", "--from", PACK_GOOD, "--scratch", scratch_for("good_cli"),
                      env_extra={"AGENTBUS_DEVICE": "clibox"})
    pre = "INTAKE-PROVE device=clibox python=%s wheels=2 installed=2 imported=2 import_missing_dep=0 failed=0 " % (
        ir.platform.python_version())
    assert rc == 0 and last == pre + "refused=0 ok=True", last
    assert os.path.isfile(ir.receipt_path(PACK_GOOD, NAMES_GOOD["alphapkg"], "clibox"))


@case
def case_mixed_pack_prove():
    rc, summ, out = run_prove(PACK_MIXED, SCR_MIXED)
    STATE["mixed_summ"] = summ
    assert rc == 1 and not summ["ok"], summ
    assert summ["refused"] == 2 and summ["installed"] == 3, summ
    assert summ["missing"] == 1 and summ["import_failed"] == 1 and summ["no_module"] == 1 and summ["failed"] == 0, summ


@case
def case_not_checked_refused_and_not_installed():
    wheel = NAMES_MIXED["unchk"]
    rec = read_receipt(PACK_MIXED, wheel)
    assert rec["outcome"] == "refused" and "not 'checked'" in rec["reason"], rec
    assert rec["install"]["command"] == [] and rec["install"]["rc"] is None, rec
    assert not os.path.exists(os.path.join(SCR_MIXED, ir.stem_of(wheel))), "scratch target exists"


@case
def case_flipped_byte_refused_and_not_installed():
    wheel = NAMES_MIXED["flip"]
    rec = read_receipt(PACK_MIXED, wheel)
    assert rec["outcome"] == "refused" and "differs from manifest" in rec["reason"], rec
    assert not os.path.exists(os.path.join(SCR_MIXED, ir.stem_of(wheel))), "scratch target exists"
    res = ir.verify_pack(PACK_MIXED)
    assert not res["ok"] and res["verified"] == 4, res


@case
def case_missing_dep_reads_import_missing_dep():
    wheel = NAMES_MIXED["needdep"]
    rec = read_receipt(PACK_MIXED, wheel)
    assert rec["outcome"] == "installed_import_failed", rec
    row = rec["imports"][0]
    assert row["class"] == "import_missing_dep" and row["missing_dep"] == "not_a_real_dep_zzz", row
    assert "ModuleNotFoundError" in row["first_error_line"] and rec["reason"].startswith("import_missing_dep"), rec


@case
def case_own_module_failure_is_a_failure():
    rec = read_receipt(PACK_MIXED, NAMES_MIXED["ownfail"])
    assert rec["outcome"] == "installed_import_failed", rec
    row = rec["imports"][0]
    assert row["class"] == "failed" and rec["reason"].startswith("import_failed"), rec


@case
def case_no_module_is_not_a_failure():
    rec = read_receipt(PACK_MIXED, NAMES_MIXED["nomod"])
    assert rec["outcome"] == "installed_imported" and rec["imports"] == [] and "no_module" in rec["reason"], rec


@case
def case_classify_import_unit():
    own = ["mypkg"]
    err = "Traceback (most recent call last):\nModuleNotFoundError: No module named '%s'\n"
    assert ir.classify_import(1, err % "other.sub", own)[:2] == ("import_missing_dep", "other.sub")
    assert ir.classify_import(1, err % "mypkg.sub", own)[0] == "failed"
    assert ir.classify_import(1, err % "mypkg", own)[0] == "failed"
    assert ir.classify_import(1, "ImportError: boom\n", own)[0] == "failed"
    assert ir.classify_import(0, "", own)[0] == "imported"


@case
def case_record_defects_each_refused():
    variants = {
        "wrong_sha": {"held_sha256": "0" * 64},
        "wrong_name": {"file_name": "other-1.0-py3-none-any.whl"},
        "seven_checks": {"drop_check": True},
        "check8_unsigned": {"c8": "unsigned"},
        "misnumbered": {"swap": True},
        "verdict_checked_but_failed_check": {"verdict": "not_checked"},
    }
    for label, spec in variants.items():
        pack = os.path.join(TMP_ROOT, "rec_" + label, "pack")
        os.makedirs(pack)
        wheel = os.path.basename(ir.build_synthetic_wheel(pack, "recpkg", "1.0", {"recpkg": "X = 1\n"}))
        ir.write_check_record(pack, wheel)
        rp = os.path.join(pack, wheel + ".check.json")
        with open(rp, "rb") as fh:
            rec = json.loads(fh.read().decode("ascii"))
        for key in ("held_sha256", "file_name", "verdict"):
            if key in spec:
                rec[key] = spec[key]
        if spec.get("drop_check"):
            rec["checks"] = rec["checks"][:7]
        if spec.get("c8"):
            rec["checks"][7]["verdict"] = spec["c8"]
        if spec.get("swap"):
            rec["checks"][0], rec["checks"][1] = rec["checks"][1], rec["checks"][0]
        with open(rp, "w", encoding="ascii") as fh:
            json.dump(rec, fh)
        ir.write_manifest(pack)
        res = ir.verify_pack(pack)
        assert not res["ok"] and res["checked"] == 0 and res["wheels"][0]["reasons"], (label, res)
    # a wheel with NO record at all
    pack = os.path.join(TMP_ROOT, "rec_none", "pack")
    os.makedirs(pack)
    ir.build_synthetic_wheel(pack, "norec", "1.0", {"norec": "X = 1\n"})
    ir.write_manifest(pack)
    res = ir.verify_pack(pack)
    assert not res["ok"] and "check record absent" in res["wheels"][0]["reasons"], res


@case
def case_stray_file_fails_verify_and_stops_prove():
    pack, names = new_pack("stray", {"straypkg": {"straypkg": "X = 1\n"}})
    with open(os.path.join(pack, "extra.txt"), "w", encoding="ascii") as fh:
        fh.write("not listed\n")
    rc, last, out = cli("verify", "--from", pack)
    assert rc == 1 and last == "INTAKE-VERIFY pack=pack wheels=1 verified=1 checked=1 stray=1 ok=False", last
    assert "STRAY: extra.txt" in out
    scratch = scratch_for("stray")
    rc2, summ, _ = run_prove(pack, scratch)
    assert rc2 == 1 and summ["installed"] == 0 and summ["refused"] == 1 and not summ["ok"], summ
    assert not os.path.exists(os.path.join(scratch, ir.stem_of(names["straypkg"])))
    # receipts/ is not a stray
    assert ir.verify_pack(PACK_GOOD)["stray"] == []


@case
def case_manifest_problems_refused():
    pack, _ = new_pack("nomanifest", {"nmpkg": {"nmpkg": "X = 1\n"}})
    os.remove(os.path.join(pack, "MANIFEST.json"))
    res = ir.verify_pack(pack)
    assert not res["ok"] and res["pack_defects"], res
    pack2, _ = new_pack("missingfile", {"mfpkg": {"mfpkg": "X = 1\n"}})
    os.remove(os.path.join(pack2, "mfpkg-1.0-py3-none-any.whl.delivery.txt"))
    res2 = ir.verify_pack(pack2)
    assert not res2["ok"] and any("absent" in d for d in res2["pack_defects"]), res2


def pack_by_check_tool(label, dist="checkpkg"):
    """A pack written by intake_check.run_pack itself (the check tool's own pack function), not by this file's writer."""
    base = pathlib.Path(TMP_ROOT) / label
    cfg = ic.Cfg(root=base / "root", records=base / "records", av_json="", sites=[], signer_dir=base / "signer")
    batch = "unit-batch"
    rel = cfg.release(batch)
    rel.mkdir(parents=True)
    cfg.records_dir(batch).mkdir(parents=True)
    wheel = os.path.basename(ir.build_synthetic_wheel(str(rel), dist, "1.0", {dist: "VALUE = 1\n"}))
    sha = ir.sha256_file(os.path.join(str(rel), wheel))
    checks = [{"n": n, "name": "check%d" % n, "verdict": "passed", "evidence": {"reason": "synthetic"},
               "rules_out": "synthetic", "leaves": "synthetic"} for n in range(1, 9)]
    checks[7]["evidence"] = {"signer": "synthetic signer", "path": "synthetic/signature.txt"}
    rec = {"schema": "intake-check/1", "batch": batch, "file_name": wheel, "held_sha256": sha, "checks": checks,
           "verdict": "checked", "checked_by": "synthetic", "at": ir.now_utc()}
    with open(str(cfg.records_dir(batch) / (wheel + ".check.json")), "w", encoding="ascii", newline="\n") as fh:
        json.dump(rec, fh, indent=2)
        fh.write("\n")
    with open(str(rel / (wheel + ".delivery.txt")), "w", encoding="ascii", newline="\n") as fh:
        fh.write("synthetic delivery note\n")
    out = base / "pack"
    sink = io.StringIO()
    rc = ic.run_pack(cfg, batch, str(out), out=sink)
    assert rc == 0, sink.getvalue()
    return str(out), wheel


@case
def case_pack_written_by_check_tool_verifies_and_proves():
    pack, wheel = pack_by_check_tool("bychecktool")
    with open(os.path.join(pack, "MANIFEST.json"), "rb") as fh:
        man = json.loads(fh.read().decode("ascii"))
    assert isinstance(man, dict) and len(man["files"]) == 1, man
    for key in ("name", "sha256", "size", "check_record", "check_record_sha256", "delivery", "delivery_sha256"):
        assert key in man["files"][0], key
    res = ir.verify_pack(pack)
    assert res["ok"] and res["verified"] == 1 and res["checked"] == 1 and res["stray"] == [] and not res["pack_defects"], res
    rc, last, _ = cli("verify", "--from", pack)
    assert rc == 0 and last == "INTAKE-VERIFY pack=pack wheels=1 verified=1 checked=1 stray=0 ok=True", last
    rc2, summ, _ = run_prove(pack, scratch_for("bychecktool"))
    assert rc2 == 0 and summ["installed"] == 1 and summ["imported"] == 1 and summ["refused"] == 0, summ


@case
def case_companion_absent_or_changed_refuses_that_wheel():
    base_pack, wheel = pack_by_check_tool("companion_base")
    arms = {"delivery_absent": ("delivery", "absent"), "delivery_changed": ("delivery", "changed"),
            "record_changed": ("check", "changed"), "bytes_synonym": (None, "synonym")}
    for label, (which, how) in arms.items():
        pack = os.path.join(TMP_ROOT, "companion_" + label, "pack")
        shutil.copytree(base_pack, pack)
        if how == "synonym":
            mp = os.path.join(pack, "MANIFEST.json")
            with open(mp, "rb") as fh:
                man = json.loads(fh.read().decode("ascii"))
            man["files"][0]["bytes"] = man["files"][0].pop("size")
            with open(mp, "w", encoding="ascii") as fh:
                json.dump(man, fh)
            assert ir.verify_pack(pack)["ok"], "bytes as a synonym of size was refused"
            continue
        target = os.path.join(pack, wheel + (".delivery.txt" if which == "delivery" else ".check.json"))
        if how == "absent":
            os.remove(target)
        else:
            with open(target, "ab") as fh:
                fh.write(b" ")
        res = ir.verify_pack(pack)
        assert not res["ok"] and res["wheels"][0]["reasons"], (label, res)
        rc, summ, _ = run_prove(pack, scratch_for("companion_" + label))
        assert summ["installed"] == 0 and summ["refused"] == 1, (label, summ)
        assert not os.path.exists(os.path.join(scratch_for("companion_" + label), ir.stem_of(wheel)))


@case
def case_pip_command_lines_never_reach_an_index():
    assert ir.COMMANDS_RUN, "no pip command was run in-process"
    for cmd in ir.COMMANDS_RUN:
        assert isinstance(cmd, list) and cmd[:5] == [sys.executable, "-m", "pip", "install", "--no-index"], cmd
        assert "--no-deps" in cmd and "--no-index" in cmd, cmd
        blob = " ".join(cmd).lower()
        assert "http" not in blob and "://" not in blob, cmd
        for banned in ("--index-url", "--extra-index-url", "--find-links", "-i", "-f"):
            assert banned not in cmd, (banned, cmd)
    built = ir.build_pip_command("w.whl", target="t")
    assert "--no-index" in built and "--no-deps" in built and "--target" in built and "--user" not in built
    built_user = ir.build_pip_command("w.whl", user=True)
    assert "--user" in built_user and "--target" not in built_user and "--no-index" in built_user
    # the tool exposes no flag that adds an index
    cp = subprocess.run([sys.executable, TOOL, "prove", "--help"], capture_output=True, text=True, timeout=60)
    low = cp.stdout.lower()
    assert "index" not in low and "find-links" not in low and "url" not in low, cp.stdout


@case
def case_child_environment_pinned():
    old = {k: os.environ.get(k) for k in ("PIP_INDEX_URL", "PIP_FIND_LINKS")}
    os.environ["PIP_INDEX_URL"] = "https://example.invalid/simple"
    os.environ["PIP_FIND_LINKS"] = "https://example.invalid/links"
    try:
        env = ir.build_child_env()
    finally:
        for k, v in old.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
    assert env["PIP_NO_INDEX"] == "1" and env["PIP_DISABLE_PIP_VERSION_CHECK"] == "1", env
    assert env["PIP_CONFIG_FILE"] == os.devnull, env
    assert "PIP_INDEX_URL" not in env and "PIP_FIND_LINKS" not in env, env


@case
def case_install_refuses_without_receipts():
    pack, _ = new_pack("noreceipt", {"nrpkg": {"nrpkg": "X = 1\n"}})
    env = {"AGENTBUS_DEVICE": "testbox"}
    for extra in ((), ("--dry-run",)):
        rc, last, out = cli("install", "--from", pack, *extra, env_extra=env)
        assert rc == 1 and "installed=0" in last and "ok=False" in last, last
        assert "no receipt" in out and "DRY-RUN" not in out, out
    # a receipt for ANOTHER device does not clear this one
    rc, last, out = cli("install", "--from", PACK_GOOD, "--dry-run", env_extra={"AGENTBUS_DEVICE": "otherbox"})
    assert rc == 1 and "ok=False" in last, last
    # unproven (refused) wheel in the mixed pack: its receipt reads refused, so the whole install is refused
    rc, last, out = cli("install", "--from", PACK_MIXED, "--dry-run", env_extra=env)
    assert rc == 1 and "ok=False" in last and "DRY-RUN" not in out, out
    rc, last, out = cli("install", "--from", PACK_GOOD, "--dry-run", drop_device=True)
    assert rc == 2 and "AGENTBUS_DEVICE is not set" in out, out


@case
def case_install_dry_run_prints_user_command_after_receipts():
    rc, last, out = cli("install", "--from", PACK_GOOD, "--dry-run", env_extra={"AGENTBUS_DEVICE": "testbox"})
    assert rc == 0 and last.endswith("dry_run=True ok=True"), (last, out)
    cmds = [json.loads(ln[len("DRY-RUN: "):]) for ln in out.splitlines() if ln.startswith("DRY-RUN: ")]
    assert len(cmds) == 2, out
    for cmd in cmds:
        assert cmd[1:5] == ["-m", "pip", "install", "--no-index"] and "--no-deps" in cmd and "--user" in cmd, cmd
        assert "--target" not in cmd and "http" not in " ".join(cmd).lower(), cmd


@case
def case_install_refuses_when_receipt_stale_or_hard_import_failure():
    # tamper with a copy of the good pack's wheel after its receipt: the receipt no longer matches the bytes
    pack = os.path.join(TMP_ROOT, "stale", "pack")
    shutil.copytree(PACK_GOOD, pack)
    wheel = NAMES_GOOD["alphapkg"]
    rec_path = ir.receipt_path(pack, wheel, "testbox")
    with open(rec_path, "rb") as fh:
        rec = json.loads(fh.read().decode("ascii"))
    rec["received_sha256"] = "1" * 64
    with open(rec_path, "w", encoding="ascii") as fh:
        json.dump(rec, fh)
    res = ir.verify_pack(pack)
    os.environ["AGENTBUS_DEVICE"] = "testbox"
    gate = {n: (ok, why) for n, ok, why in ir.receipt_gate(pack, "testbox", res)}
    assert gate[wheel][0] is False and "bytes" in gate[wheel][1], gate
    # a hard import failure is not an acceptable receipt; a missing-dep one is
    own = ir.receipt_gate(PACK_MIXED, "testbox", {"wheels": [
        {"name": NAMES_MIXED["ownfail"], "reasons": [], "wheel_sha256": ir.sha256_file(os.path.join(PACK_MIXED, NAMES_MIXED["ownfail"])),
         "check_record_sha256": ir.sha256_file(os.path.join(PACK_MIXED, NAMES_MIXED["ownfail"] + ".check.json"))},
        {"name": NAMES_MIXED["needdep"], "reasons": [], "wheel_sha256": ir.sha256_file(os.path.join(PACK_MIXED, NAMES_MIXED["needdep"])),
         "check_record_sha256": ir.sha256_file(os.path.join(PACK_MIXED, NAMES_MIXED["needdep"] + ".check.json"))},
    ]})
    verdicts = {n: ok for n, ok, _ in own}
    assert verdicts[NAMES_MIXED["ownfail"]] is False and verdicts[NAMES_MIXED["needdep"]] is True, own


@case
def case_scratch_must_be_new_and_empty():
    scratch = scratch_for("dirty")
    os.makedirs(scratch)
    with open(os.path.join(scratch, "leftover"), "w", encoding="ascii") as fh:
        fh.write("x\n")
    pack, names = new_pack("dirty", {"dirtypkg": {"dirtypkg": "X = 1\n"}})
    rc, summ, out = run_prove(pack, scratch)
    assert rc == 2 and summ["installed"] == 0 and "REFUSED: --scratch" in out, out
    assert not os.path.exists(os.path.join(pack, "receipts"))


@case
def case_no_device_refuses_to_write_a_receipt():
    pack, _ = new_pack("nodevice", {"ndpkg": {"ndpkg": "X = 1\n"}})
    rc, last, out = cli("prove", "--from", pack, "--scratch", scratch_for("nodevice"), drop_device=True)
    assert rc == 2 and "AGENTBUS_DEVICE is not set" in out, out
    assert last.startswith("INTAKE-PROVE device=UNSET ") and "installed=0" in last and "ok=False" in last, last
    assert not os.path.exists(os.path.join(pack, "receipts")) and not os.path.exists(scratch_for("nodevice"))


@case
def case_selftest_unchecked_cli():
    before = sorted(os.listdir(HERE))
    rc, last, _ = cli("selftest-unchecked")
    assert rc == 0 and "installed=0" in last and "refused=1" in last and last.startswith("INTAKE-PROVE "), last
    assert sorted(os.listdir(HERE)) == before, "selftest left files behind"


@case
def case_tool_has_no_network_module_and_no_url():
    with open(TOOL, "rb") as fh:
        src = fh.read()
    assert all(b < 128 for b in src), "non-ASCII byte in the tool"
    tree = ast.parse(src.decode("ascii"))
    banned = {"socket", "urllib", "http", "ftplib", "smtplib", "requests", "ssl", "imp", "distutils", "cgi", "pipes"}
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            found.add(node.module.split(".")[0])
    assert not (found & banned), found & banned
    assert b"http" not in src.lower().replace(b"https_proxy", b""), "an http string in the tool"


def main():
    shutil_ok = True
    try:
        total = len(RESULTS)
        passed = sum(1 for _, ok, _ in RESULTS if ok)
        ok = passed == total and total > 0
    finally:
        shutil.rmtree(TMP_ROOT, ignore_errors=True)
        shutil_ok = not os.path.exists(TMP_ROOT)
    if not shutil_ok:
        print("WARN: temporary folder not removed: %s" % TMP_ROOT)
    for name, good, why in RESULTS:
        if not good:
            print("FAILED CASE: %s -- %s" % (name, why))
    print("INTAKE-RECEIVE-TEST cases=%d/%d ok=%s" % (passed, total, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
