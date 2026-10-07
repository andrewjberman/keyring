"""test_intake_check.py -- cases for intake_check.py on SYNTHETIC wheels and hand-written fetch records in a temporary root.

No network, no package install, no import or execution of anything from a wheel. Check 7 uses a stub scanner except for
the ONE case that runs the real platform scanner on a tiny harmless synthetic wheel this file builds (skipped, and counted
as skipped, if the scanner is absent or refuses to run). LAST line:
  INTAKE-CHECK-TEST cases=<k>/<n> skipped=<s> ok=<True|False>
"""
from __future__ import annotations

import functools
import io
import itertools
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import traceback

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import intake_check as ic  # noqa: E402

BRIEF = ic.REPO_ROOT / "docs" / "briefs" / "nfra-ctlpln-package-intake-and-download-tiers-brief-20261007.md"
BATCH = "tb1"
SIGNER_TEXT = "I have read checks 1 to 7 for batch %s and sign file %s\n"


class Skip(Exception):
    pass


class Env:
    """A fresh temporary world: holding root, records, stub scanner, 'installed' site dir, approved list, signer dir."""

    def __init__(self, scanner_rc=0, installed=True, **wheel_kw):
        self.tmp = pathlib.Path(tempfile.mkdtemp(prefix="intake_test_"))
        self.site = self.tmp / "site"
        self.site.mkdir()
        self.signer_dir = self.tmp / "signer"
        self.signer_dir.mkdir()
        if installed:
            ic.build_installed_fixture(self.site)
        self.cfg = ic.Cfg(root=self.tmp / "root", records=self.tmp / "records",
                          scanner=ic.write_stub_scanner(self.tmp, scanner_rc), sites=[self.site], signer_dir=self.signer_dir)
        self.approved = self.tmp / "approved.txt"
        self.approved.write_text("# approved\n%s==%s\n" % (ic.SYN_NAME, ic.SYN_VERSION), encoding="ascii")
        self.batch = BATCH

    def add_wheel(self, name=ic.SYN_NAME, version=ic.SYN_VERSION, tags=ic.SYN_TAGS, fetch_kw=None, **wheel_kw):
        hold = self.cfg.holding(self.batch)
        hold.mkdir(parents=True, exist_ok=True)
        path = ic.build_synthetic_wheel(hold / ic.syn_file_name(name, version, tags), name=name, version=version, tags=tags,
                                        **wheel_kw)
        ic.write_fetch_record(self.cfg, self.batch, path, name=name, version=version, tags=tags, **(fetch_kw or {}))
        return path

    def sign(self, file_name, text=None):
        p = self.signer_dir / ("signature_%s.txt" % file_name)
        p.write_text(text if text is not None else SIGNER_TEXT % (self.batch, file_name), encoding="ascii")
        return str(p)

    def check(self, file_name, signed=True, approved=True, **kw):
        sink = io.StringIO()
        record, line = ic.run_check(self.cfg, self.batch, file_name,
                                    approved_by=str(self.approved) if approved else None,
                                    signed_by=self.sign(file_name) if signed is True else (signed or None), out=sink, **kw)
        return record, line

    def close(self):
        shutil.rmtree(str(self.tmp), ignore_errors=True)


def verdicts(record):
    return {c["n"]: c["verdict"] for c in record["checks"]}


def release(env, file_name):
    sink = io.StringIO()
    rc = ic.run_release(env.cfg, env.batch, file_name, out=sink)
    return rc, sink.getvalue()


def pack(env, out):
    sink = io.StringIO()
    rc = ic.run_pack(env.cfg, env.batch, out, out=sink)
    return rc, sink.getvalue()


def with_env(fn):
    @functools.wraps(fn)
    def runner(**kw):
        env = Env(**kw)
        try:
            fn(env)
        finally:
            env.close()
    return runner


# ------------------------------------------------------------------------------------------------------------ cases
@with_env
def case_clean_signed_checked_and_releases(env):
    w = env.add_wheel()
    record, line = env.check(w.name)
    assert verdicts(record) == {1: "passed", 2: "passed", 3: "passed", 4: "passed", 5: "not_applicable", 6: "passed",
                                7: "passed", 8: "passed"}, verdicts(record)
    assert record["verdict"] == "checked" and line.endswith("c8=passed verdict=checked"), line
    assert line.startswith("INTAKE-CHECK batch=%s file=%s c1=passed" % (BATCH, w.name)), line
    assert [c["n"] for c in record["checks"]] == list(range(1, 9)) and len(record["checks"]) == 8
    rc, msg = release(env, w.name)
    assert rc == 0, msg
    assert not w.exists() and (env.cfg.release(BATCH) / w.name).is_file(), "the file must be MOVED"
    deliv = (env.cfg.release(BATCH) / (w.name + ".delivery.txt")).read_text(encoding="ascii")
    assert ic.DELIVERY_SENTENCE in deliv
    for c in record["checks"]:
        assert c["leaves"] in deliv
    assert "not applicable: the project publishes none" in deliv


@with_env
def case_unsigned_not_checked_and_release_refuses(env):
    w = env.add_wheel()
    record, line = env.check(w.name, signed=False)
    assert "c8=unsigned verdict=not_checked" in line, line
    assert verdicts(record)[8] == "unsigned" and record["verdict"] == "not_checked"
    rc, msg = release(env, w.name)
    assert rc == 1 and "does not read 'checked'" in msg, msg
    assert w.exists() and not (env.cfg.release(BATCH) / w.name).exists()


@with_env
def case_flipped_byte_fails_check_1(env):
    w = env.add_wheel()
    data = bytearray(w.read_bytes())
    data[len(data) // 2] ^= 0xFF
    w.write_bytes(bytes(data))
    record, line = env.check(w.name)
    assert verdicts(record)[1] == "failed" and record["verdict"] == "not_checked", line


@with_env
def case_differing_py_fails_check_6_and_is_listed(env):
    w = env.add_wheel(py_bytes=b"VALUE = 2  # differs from the installed fixture\n")
    record, line = env.check(w.name)
    c6 = record["checks"][5]
    assert c6["verdict"] == "failed" and record["verdict"] == "not_checked"
    ev = c6["evidence"]
    assert ev["py_differing"] == ["%s/__init__.py" % ic.SYN_NAME] and ev["py_differing_count"] == 1
    assert ev["py_in_wheel"] == 1 and ev["py_identical"] == 0
    assert ev["compiled_count"] == 1 and ev["compiled"] == ["%s/_ext.pyd" % ic.SYN_NAME]


@with_env
def case_py_absent_from_installed_copy_is_a_difference(env):
    w = env.add_wheel(extra={"%s/new_module.py" % ic.SYN_NAME: b"X = 1\n"})
    record, _ = env.check(w.name)
    assert record["checks"][5]["verdict"] == "failed"
    assert "%s/new_module.py" % ic.SYN_NAME in record["checks"][5]["evidence"]["py_differing"]


@with_env
def case_added_pth_fails_check_6(env):
    w = env.add_wheel(extra={"evil.pth": b"import os\n"})
    record, _ = env.check(w.name)
    c6 = record["checks"][5]
    assert c6["verdict"] == "failed" and "evil.pth" in c6["evidence"]["hooks_only_in_wheel"]


@with_env
def case_other_hooks_fail_and_known_hook_is_not_a_failure(env):
    w = env.add_wheel(extra={"sitecustomize.py": b"pass\n", "%s-%s.data/scripts/run.py" % (ic.SYN_NAME, ic.SYN_VERSION): b"x\n"},
                      entry_points="[console_scripts]\nselftest = selftestpkg:main\nextra = selftestpkg:other\n")
    record, _ = env.check(w.name)
    hooks = record["checks"][5]["evidence"]["hooks_only_in_wheel"]
    assert "sitecustomize.py" in hooks
    assert any("scripts/run.py" in h for h in hooks)
    assert any(h.startswith("entry_point console_scripts:extra") for h in hooks)
    assert not any("selftest " in h for h in hooks), "an entry point the installed copy has is not a failure"
    assert record["checks"][5]["evidence"]["hooks_also_in_installed_copy"], "the shared entry point is recorded"


@with_env
def case_release_two_days_old_fails_check_4_default_passes_with_flag(env):
    w = env.add_wheel(fetch_kw={"release_age_days": 2})
    record, _ = env.check(w.name)
    assert verdicts(record)[4] == "failed" and record["verdict"] == "not_checked"
    assert record["checks"][3]["evidence"]["min_release_age_days"] == 14
    record, _ = env.check(w.name, min_age=1, min_earlier=3)
    assert verdicts(record)[4] == "passed" and record["verdict"] == "checked"
    assert record["checks"][3]["evidence"]["min_release_age_days"] == 1
    record, _ = env.check(w.name, min_age=1, min_earlier=50)
    assert verdicts(record)[4] == "failed", "too few earlier releases fails check 4"


@with_env
def case_attestation_absent_not_applicable_unread_failed_present_passed(env):
    w = env.add_wheel(fetch_kw={"attestation": "absent"})
    record, _ = env.check(w.name)
    c5 = record["checks"][4]
    assert c5["verdict"] == "not_applicable" and c5["evidence"]["reason"] == "the project publishes none"
    assert record["verdict"] == "checked", "not_applicable WITH a reason does not block"
    env.add_wheel(fetch_kw={"attestation": "unread"})
    record, _ = env.check(w.name)
    assert verdicts(record)[5] == "failed" and record["verdict"] == "not_checked"
    env.add_wheel(fetch_kw={"attestation": "present"})
    record, _ = env.check(w.name)
    assert verdicts(record)[5] == "passed" and record["verdict"] == "checked"


@with_env
def case_file_changed_after_check_record_refused_by_release(env):
    w = env.add_wheel()
    record, _ = env.check(w.name)
    assert record["verdict"] == "checked"
    w.write_bytes(w.read_bytes() + b"\0")
    rc, msg = release(env, w.name)
    assert rc == 1 and "changed since its check record" in msg, msg
    assert w.exists() and not (env.cfg.release(BATCH) / w.name).exists()


@with_env
def case_pack_refuses_batch_with_one_unchecked_file(env):
    a = env.add_wheel()
    b = env.add_wheel(version="2.0.0")
    ic.build_installed_fixture(env.site, version="2.0.0")
    env.approved.write_text("%s==1.0.0\n%s==2.0.0\n" % (ic.SYN_NAME, ic.SYN_NAME), encoding="ascii")
    rec_a, _ = env.check(a.name)
    assert rec_a["verdict"] == "checked" and release(env, a.name)[0] == 0
    rec_b, _ = env.check(b.name, signed=False)
    assert rec_b["verdict"] == "not_checked"
    out = env.tmp / "packout"
    rc, msg = pack(env, out)
    assert rc == 1 and "files remain in holding" in msg and b.name in msg, msg
    assert not out.exists()
    # variant: the unchecked file sits in release/ (put there by hand) with an unchecked record
    shutil.move(str(b), str(env.cfg.release(BATCH) / b.name))
    rc, msg = pack(env, out)
    assert rc == 1 and b.name in msg and "does not read 'checked'" in msg, msg
    assert not out.exists()


@with_env
def case_pack_succeeds_when_every_file_checked(env):
    w = env.add_wheel()
    record, _ = env.check(w.name)
    assert release(env, w.name)[0] == 0
    out = env.tmp / "packout"
    rc, msg = pack(env, out)
    assert rc == 0, msg
    man = json.loads((out / "MANIFEST.json").read_text(encoding="ascii"))
    ent = man["files"][0]
    assert ent["name"] == w.name and ent["sha256"] == ic.sha256_file(out / w.name) == record["held_sha256"]
    assert ent["size"] == (out / w.name).stat().st_size
    assert (out / (w.name + ".check.json")).is_file() and (out / (w.name + ".delivery.txt")).is_file()


@with_env
def case_released_file_altered_before_pack_is_refused(env):
    w = env.add_wheel()
    env.check(w.name)
    release(env, w.name)
    dest = env.cfg.release(BATCH) / w.name
    dest.write_bytes(dest.read_bytes() + b"\0")
    rc, msg = pack(env, env.tmp / "packout")
    assert rc == 1 and "differs from the check record" in msg, msg


def case_no_installed_copy():
    env = Env(installed=False)
    try:
        w = env.add_wheel()
        record, _ = env.check(w.name)
        v = verdicts(record)
        assert v[3] == "not_applicable" and v[6] == "not_applicable", v
        assert "holds no installed copy" in record["checks"][2]["evidence"]["reason"]
        assert record["checks"][5]["evidence"]["reason"]
        assert record["verdict"] == "checked", "not_applicable with a reason does not block"
        rc, _ = release(env, w.name)
        assert rc == 0
        deliv = (env.cfg.release(BATCH) / (w.name + ".delivery.txt")).read_text(encoding="ascii")
        assert "not applicable: this machine holds no installed copy" in deliv
    finally:
        env.close()


def case_other_installed_version_only():
    env = Env(installed=False)
    try:
        ic.build_installed_fixture(env.site, version="0.9.0")
        w = env.add_wheel()
        record, _ = env.check(w.name)
        assert verdicts(record)[3] == "not_applicable" and "0.9.0" in record["checks"][2]["evidence"]["reason"]
    finally:
        env.close()


@with_env
def case_check_7_stub_scanner_exit_codes(env):
    w = env.add_wheel()
    for rc, want in ((0, "passed"), (2, "failed"), (5, "failed")):
        env.cfg.scanner = ic.write_stub_scanner(env.tmp, rc)
        record, _ = env.check(w.name)
        c7 = record["checks"][6]
        assert c7["verdict"] == want and c7["evidence"]["exit_code"] == rc, (rc, c7)
        assert c7["evidence"]["last_lines"], "last lines recorded"
        assert (record["verdict"] == "checked") == (want == "passed")
    env.cfg.scanner = str(env.tmp / "no_such_scanner.exe")
    record, _ = env.check(w.name)
    assert verdicts(record)[7] == "failed" and record["verdict"] == "not_checked"


@with_env
def case_check_2_wrong_requests_fail(env):
    # (a) not on the approved list
    w = env.add_wheel()
    env.approved.write_text("otherpkg==1.0.0\n", encoding="ascii")
    record, _ = env.check(w.name)
    assert verdicts(record)[2] == "failed" and "approved list" in record["checks"][1]["evidence"]["summary"]
    # (b) no approved list at all
    record, _ = env.check(w.name, approved=False)
    assert verdicts(record)[2] == "failed"
    # (c) near-name request: the wheel is selftestpkg but the record asks for another name
    env.approved.write_text("%s==%s\n" % (ic.SYN_NAME, ic.SYN_VERSION), encoding="ascii")
    rec_path = env.cfg.records_dir(BATCH) / (w.name + ".fetch.json")
    fr = json.loads(rec_path.read_text(encoding="ascii"))
    fr["requested"]["name"] = "selftestpkg2"
    rec_path.write_text(json.dumps(fr), encoding="ascii")
    record, _ = env.check(w.name)
    assert verdicts(record)[2] == "failed"
    # (d) the archive's own METADATA says another version than the file name
    env.add_wheel(extra={"%s-%s.dist-info/METADATA" % (ic.SYN_NAME, ic.SYN_VERSION):
                         b"Metadata-Version: 2.1\nName: selftestpkg\nVersion: 9.9.9\n\n"})
    record, _ = env.check(w.name)
    assert verdicts(record)[2] == "failed" and "METADATA Version" in record["checks"][1]["evidence"]["summary"]
    # (e) the WHEEL Tag line disagrees with the file name
    env.add_wheel(extra={"%s-%s.dist-info/WHEEL" % (ic.SYN_NAME, ic.SYN_VERSION):
                         b"Wheel-Version: 1.0\nTag: cp311-cp311-win_amd64\n"})
    record, _ = env.check(w.name)
    assert verdicts(record)[2] == "failed" and "WHEEL Tag" in record["checks"][1]["evidence"]["summary"]
    # (f) name normalisation: a differently-cased, underscore/dash-variant approved line still matches
    env.add_wheel()
    env.approved.write_text("SelfTestPkg==%s\n" % ic.SYN_VERSION, encoding="ascii")
    record, _ = env.check(w.name)
    assert verdicts(record)[2] == "passed", record["checks"][1]["evidence"]


def test_parse_wheel_name():
    p = ic.parse_wheel_name("foo_bar-1.2.3-1-cp312-cp312-win_amd64.whl")
    assert p["dist"] == "foo_bar" and p["build"] == "1" and p["platform_tag"] == "win_amd64"
    assert ic.parse_wheel_name("foo-1.0.tar.gz") is None and ic.parse_wheel_name("a-b-c.whl") is None


def case_parse_wheel_name():
    test_parse_wheel_name()


@with_env
def case_check_8_signature_rules(env):
    w = env.add_wheel()
    # a file whose text lacks the file name
    record, _ = env.check(w.name, signed=env.sign(w.name, text="batch %s only\n" % BATCH))
    assert verdicts(record)[8] == "failed" and record["verdict"] == "not_checked"
    # a file whose text lacks the batch id
    record, _ = env.check(w.name, signed=env.sign(w.name, text="file %s only\n" % w.name))
    assert verdicts(record)[8] == "failed"
    # a file that does not exist
    record, _ = env.check(w.name, signed=str(env.signer_dir / "absent.txt"))
    assert verdicts(record)[8] == "failed"
    # a file with the right text but OUTSIDE the required directory
    outside = env.tmp / "outside.txt"
    outside.write_text(SIGNER_TEXT % (BATCH, w.name), encoding="ascii")
    record, _ = env.check(w.name, signed=str(outside))
    assert verdicts(record)[8] == "failed" and "not under the required directory" in record["checks"][7]["evidence"]["summary"]
    # a traversal out of the directory
    record, _ = env.check(w.name, signed=str(env.signer_dir / ".." / "outside.txt"))
    assert verdicts(record)[8] == "failed"
    # the good one
    record, _ = env.check(w.name)
    ev = record["checks"][7]["evidence"]
    assert verdicts(record)[8] == "passed" and ev["signer"] and ev["path"]


@with_env
def case_default_signer_dir_is_the_ctos_deliverables(env):
    w = env.add_wheel()
    env.cfg.signer_dir = None
    # a real file, right text, wrong place (a scratch file inside the repository but not under the CTO's directory)
    scratch = ic.REPO_ROOT / ".scratch"
    scratch.mkdir(exist_ok=True)
    f = pathlib.Path(tempfile.mkdtemp(prefix="sig_", dir=str(scratch))) / "sig.txt"
    try:
        f.write_text(SIGNER_TEXT % (BATCH, w.name), encoding="ascii")
        record, _ = env.check(w.name, signed=str(f.relative_to(ic.REPO_ROOT)))
        assert verdicts(record)[8] == "failed" and record["verdict"] == "not_checked"
        assert "org/tier1_exec/1.0.0_SA_CTO/deliverables" in record["checks"][7]["evidence"]["summary"]
    finally:
        shutil.rmtree(str(f.parent), ignore_errors=True)


def case_no_path_to_checked_without_the_signature():
    """compute_verdict over EVERY combination of verdicts for checks 1 to 7 and every non-passing form of check 8."""
    n_checked = 0
    ev_ok = {"reason": "r", "signer": "s", "path": "p"}
    for combo in itertools.product(ic.VERDICTS, repeat=7):
        for c8 in ({"verdict": "unsigned", "evidence": ev_ok}, {"verdict": "failed", "evidence": ev_ok},
                   {"verdict": "not_applicable", "evidence": ev_ok}, {"verdict": "passed", "evidence": {"signer": "s"}},
                   {"verdict": "passed", "evidence": {"path": "p"}}, {"verdict": "passed", "evidence": {}}):
            checks = [{"n": i + 1, "verdict": v, "evidence": ev_ok} for i, v in enumerate(combo)] + [dict(c8, n=8)]
            if ic.compute_verdict(checks) == "checked":
                n_checked += 1
    assert n_checked == 0, "a non-passing check 8 reached 'checked' %d times" % n_checked
    # and the positive control: all passed + signed reaches it
    good = [{"n": i + 1, "verdict": "passed", "evidence": ev_ok} for i in range(8)]
    assert ic.compute_verdict(good) == "checked"
    # not_applicable WITHOUT a reason does not pass
    bad = [dict(c) for c in good]
    bad[2] = {"n": 3, "verdict": "not_applicable", "evidence": {"summary": "x"}}
    assert ic.compute_verdict(bad) == "not_checked"
    # malformed lists
    assert ic.compute_verdict(good[:7]) == "not_checked" and ic.compute_verdict(None) == "not_checked"
    # the tool source has exactly one place that can emit the string "checked" as a verdict value
    src = (HERE / "intake_check.py").read_text(encoding="ascii")
    assert len(re.findall(r'return "checked"', src)) == 1


@with_env
def case_hand_edited_record_cannot_release(env):
    w = env.add_wheel()
    record, _ = env.check(w.name, signed=False)
    p = env.cfg.records_dir(BATCH) / (w.name + ".check.json")
    edited = json.loads(p.read_text(encoding="ascii"))
    edited["verdict"] = "checked"   # a hand edit of the top-level verdict only
    p.write_text(json.dumps(edited), encoding="ascii")
    rc, msg = release(env, w.name)
    assert rc == 1 and "does not read 'checked'" in msg, msg
    assert w.exists()


@with_env
def case_missing_fetch_record_and_held_file_fail(env):
    w = env.add_wheel()
    (env.cfg.records_dir(BATCH) / (w.name + ".fetch.json")).unlink()
    record, _ = env.check(w.name)
    assert verdicts(record)[1] == "failed" and verdicts(record)[2] == "failed"
    assert record["verdict"] == "not_checked"
    record, _ = env.check("absent-1.0-py3-none-any.whl")
    assert record["verdict"] == "not_checked" and verdicts(record)[1] == "failed"


@with_env
def case_failed_fetch_outcome_fails_check_1(env):
    w = env.add_wheel(fetch_kw={"outcome": "failed"})
    record, _ = env.check(w.name)
    assert verdicts(record)[1] == "failed" and record["verdict"] == "not_checked"


def case_constants_appear_verbatim_in_the_brief():
    text = re.sub(r"\s+", " ", BRIEF.read_text(encoding="utf-8").replace("**", ""))   # the brief bolds the sentence's lead
    rows = {}
    raw = BRIEF.read_text(encoding="utf-8").splitlines()
    table = [ln for ln in raw if re.match(r"^\| [1-8] \|", ln)]
    assert len(table) == 8, "the brief's V.1 table no longer has eight rows"
    for ln in table:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        rows[int(cells[0])] = cells
    for row in ic.CHECK_TABLE:
        cells = rows[row["n"]]
        assert row["rules_out"] == cells[3], (row["n"], "rules_out", row["rules_out"], cells[3])
        assert row["leaves"] == cells[4], (row["n"], "leaves", row["leaves"], cells[4])
        assert row["rules_out"] in text and row["leaves"] in text
    assert re.sub(r"\s+", " ", ic.DELIVERY_SENTENCE) in text
    for s in [r["rules_out"] for r in ic.CHECK_TABLE] + [r["leaves"] for r in ic.CHECK_TABLE] + [ic.DELIVERY_SENTENCE]:
        s.encode("ascii")


def case_records_are_ascii_only():
    env = Env()
    try:
        w = env.add_wheel()
        env.check(w.name)
        for p in env.cfg.records_dir(BATCH).iterdir():
            p.read_bytes().decode("ascii")
        for p in pathlib.Path(__file__).resolve().parent.glob("*.py"):
            p.read_bytes().decode("ascii")
    finally:
        env.close()


def case_cli_honours_the_environment_names():
    """The CLI, in a subprocess, with the five environment overrides; check, release, pack end to end."""
    env = Env()
    try:
        w = env.add_wheel()
        sig = env.sign(w.name)
        e = dict(os.environ, OPAL_INTAKE_ROOT=str(env.cfg.root), OPAL_INTAKE_RECORDS=str(env.cfg.records_base),
                 OPAL_INTAKE_SCANNER=env.cfg.scanner, OPAL_INTAKE_SITE=str(env.site), OPAL_INTAKE_SIGNER_DIR=str(env.signer_dir))
        tool = str(HERE / "intake_check.py")

        def run(*args):
            return subprocess.run([sys.executable, tool] + list(args), capture_output=True, text=True, env=e, timeout=100,
                                  stdin=subprocess.DEVNULL)
        r = run("check", "--batch", BATCH, "--file", w.name, "--approved-by", str(env.approved))
        assert r.stdout.strip().splitlines()[-1].endswith("c8=unsigned verdict=not_checked"), r.stdout + r.stderr
        r = run("check", "--batch", BATCH, "--file", w.name, "--approved-by", str(env.approved), "--signed-by", sig)
        assert r.stdout.strip().splitlines()[-1].endswith("c8=passed verdict=checked"), r.stdout + r.stderr
        r = run("release", "--batch", BATCH, "--file", w.name)
        assert r.returncode == 0, r.stdout + r.stderr
        r = run("pack", "--batch", BATCH, "--out", str(env.tmp / "cliout"))
        assert r.returncode == 0 and (env.tmp / "cliout" / "MANIFEST.json").is_file(), r.stdout + r.stderr
        assert (env.cfg.records_base / BATCH / (w.name + ".check.json")).is_file()
    finally:
        env.close()


def case_selftest_unsigned_leaves_nothing_behind():
    def snap():
        return sorted(str(p) for p in ic.REPO_ROOT.joinpath("org", "devices", "intake").rglob("*"))
    before = snap()
    tmp_before = sorted(p.name for p in pathlib.Path(tempfile.gettempdir()).glob("intake_selftest_*"))
    sink = io.StringIO()
    rc = ic.selftest_unsigned(out=sink)
    assert rc == 0 and sink.getvalue().strip().splitlines()[-1].endswith("c8=unsigned verdict=not_checked"), sink.getvalue()
    assert snap() == before, "selftest left files under org/devices/intake"
    assert sorted(p.name for p in pathlib.Path(tempfile.gettempdir()).glob("intake_selftest_*")) == tmp_before


REAL_SCANNER_NOTE = []


def case_real_scanner_on_tiny_synthetic_wheel():
    sc = ic.find_scanner(ic.Cfg(scanner=""))
    if not sc:
        REAL_SCANNER_NOTE.append("scanner absent")
        raise Skip("the platform scanner was not found")
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="intake_real_"))
    try:
        w = ic.build_synthetic_wheel(tmp / ic.syn_file_name())
        cfg = ic.Cfg(root=tmp / "root", records=tmp / "rec", scanner="", sites=[])
        cfg.scanner = None
        ctx = {"cfg": cfg, "path": w}
        verdict, ev = ic.check_7(ctx)
        REAL_SCANNER_NOTE.append("verdict=%s exit_code=%s last_lines=%s" % (verdict, ev.get("exit_code"), ev.get("last_lines")))
        if ev.get("exit_code") is None or (verdict == "failed" and (ev.get("exit_code") not in (0, 2)
                                                                    or ev.get("scanner_output_shows_an_error"))):
            raise Skip("the real scanner refused or could not run: exit_code=%s %s" % (ev.get("exit_code"), ev.get("summary")))
        assert verdict == "passed" and ev["exit_code"] == 0, (verdict, ev)
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)


CASES = [
    case_clean_signed_checked_and_releases, case_unsigned_not_checked_and_release_refuses, case_flipped_byte_fails_check_1,
    case_differing_py_fails_check_6_and_is_listed, case_py_absent_from_installed_copy_is_a_difference,
    case_added_pth_fails_check_6, case_other_hooks_fail_and_known_hook_is_not_a_failure,
    case_release_two_days_old_fails_check_4_default_passes_with_flag,
    case_attestation_absent_not_applicable_unread_failed_present_passed,
    case_file_changed_after_check_record_refused_by_release, case_pack_refuses_batch_with_one_unchecked_file,
    case_pack_succeeds_when_every_file_checked, case_released_file_altered_before_pack_is_refused,
    case_no_installed_copy, case_other_installed_version_only, case_check_7_stub_scanner_exit_codes,
    case_check_2_wrong_requests_fail, case_parse_wheel_name, case_check_8_signature_rules,
    case_default_signer_dir_is_the_ctos_deliverables, case_no_path_to_checked_without_the_signature,
    case_hand_edited_record_cannot_release, case_missing_fetch_record_and_held_file_fail,
    case_failed_fetch_outcome_fails_check_1, case_constants_appear_verbatim_in_the_brief, case_records_are_ascii_only,
    case_cli_honours_the_environment_names, case_selftest_unsigned_leaves_nothing_behind,
    case_real_scanner_on_tiny_synthetic_wheel,
]


def main():
    passed = skipped = 0
    for fn in CASES:
        try:
            fn()
            passed += 1
            print("PASS %s" % fn.__name__)
        except Skip as exc:
            skipped += 1
            print("SKIP %s: %s" % (fn.__name__, exc))
        except Exception:
            print("FAIL %s" % fn.__name__)
            traceback.print_exc(file=sys.stdout)
    if REAL_SCANNER_NOTE:
        print("REAL-SCANNER: " + "; ".join(REAL_SCANNER_NOTE))
    total = len(CASES)
    ok = passed + skipped == total
    print("INTAKE-CHECK-TEST cases=%d/%d skipped=%d ok=%s" % (passed, total, skipped, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
