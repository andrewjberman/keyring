"""test_intake_check.py -- cases for intake_check.py on SYNTHETIC wheels and hand-written fetch records in a temporary root.

No network, no package install, no import or execution of anything from a wheel. Check 7 reads a stand-in for the Security
Center answer (a JSON file named by OPAL_INTAKE_AV_JSON, wait 0) except for the ONE case that reads the REAL Security Center and
runs the real on-access read on a tiny harmless synthetic wheel this file builds, with the default wait (skipped, and counted
as skipped, only if the query itself cannot run). No test-virus file is used anywhere. LAST line:
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
import time
import traceback

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import intake_check as ic  # noqa: E402

BRIEF = ic.REPO_ROOT / "docs" / "briefs" / "nfra-ctlpln-package-intake-and-download-tiers-brief-20261007.md"
BATCH = "tb1"
GOOD_STATE = 266240      # 0x041000: real-time on, definitions current (the CTO's measured value)
OFF_STATE = 393472       # 0x060100: real-time off
AV_NAME = "Synthetic Antivirus (stand-in)"
SIGNER_TEXT = "I have read checks 1 to 7 for batch %s and sign file %s\n\nCHECK 8 SIGNED -- test signer\n"


class Skip(Exception):
    pass


class Env:
    """A fresh temporary world: holding root, records, Security Center stand-in, 'installed' site dir, approved list, signer
    dir."""

    def __init__(self, av_state=GOOD_STATE, installed=True, **wheel_kw):
        self.tmp = pathlib.Path(tempfile.mkdtemp(prefix="intake_test_"))
        self.site = self.tmp / "site"
        self.site.mkdir()
        self.signer_dir = self.tmp / "signer"
        self.signer_dir.mkdir()
        if installed:
            ic.build_installed_fixture(self.site)
        self.av = self.tmp / "av.json"
        self.set_av([{"displayName": AV_NAME, "productState": av_state}])
        self.cfg = ic.Cfg(root=self.tmp / "root", records=self.tmp / "records", av_json=str(self.av), sites=[self.site],
                          signer_dir=self.signer_dir)
        self.approved = self.tmp / "approved.txt"
        self.approved.write_text("# approved\n%s==%s\n" % (ic.SYN_NAME, ic.SYN_VERSION), encoding="ascii")
        self.batch = BATCH

    def set_av(self, obj):
        self.av.write_text(obj if isinstance(obj, str) else json.dumps(obj), encoding="utf-8")

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
        kw.setdefault("scan_wait", 0)
        self.last_out = sink
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
    assert ic.LIMIT_SENTENCE in deliv, "the limit of check 7 travels in the delivery text"
    assert not (env.cfg.release(BATCH) / (w.name + ic.SCAN_COPY_SUFFIX)).exists()


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


PASS_SENTENCE = ("on-access scan by %s, state enabled and current; file present and unchanged after %d s; "
                 "no on-demand verdict available")


def scan_copy_of(env, w):
    return w.with_name(w.name + ic.SCAN_COPY_SUFFIX)


@with_env
def case_check_7_on_and_current_passes_with_the_exact_sentence(env):
    w = env.add_wheel()
    record, line = env.check(w.name)
    c7 = record["checks"][6]
    assert c7["verdict"] == "passed", c7
    assert c7["evidence"]["summary"] == PASS_SENTENCE % (AV_NAME, 0), c7["evidence"]["summary"]
    assert c7["evidence"]["summary"] == ("on-access scan by Synthetic Antivirus (stand-in), state enabled and current; "
                                         "file present and unchanged after 0 s; no on-demand verdict available")
    ev = c7["evidence"]
    assert ev["scan_wait_seconds"] == 0 and ev["active"] == [AV_NAME] and ev["copy_cleanup"] == "removed"
    assert ev["products"][0]["hex"] == "0x041000" and ev["products"][0]["state"] == GOOD_STATE
    assert ev["products"][0]["realtime"] == "on" and ev["products"][0]["definitions"] == "current"
    assert "0x060100" in ev["decoding"] and "393472" in ev["decoding"] and "266240" in ev["decoding"]
    assert ev["limit"] == ic.LIMIT_SENTENCE and c7["leaves"] == "anything new or targeted", "brief's Leaves text unchanged"
    assert ev["held_after"] == "unchanged" and ev["copy_after"] == "unchanged"
    out = env.last_out.getvalue()
    assert "hex=0x041000" in out and ic.LIMIT_SENTENCE in out and "0x060100 -> off" in out
    assert not scan_copy_of(env, w).exists(), "the copy is gone after the check"
    # the record on disk carries the limit beside check 7
    saved = json.loads((env.cfg.records_dir(BATCH) / (w.name + ".check.json")).read_text(encoding="ascii"))
    assert saved["checks"][6]["evidence"]["limit"] == ic.LIMIT_SENTENCE


@with_env
def case_check_7_sentence_names_the_wait_in_whole_seconds(env):
    w = env.add_wheel()
    record, _ = env.check(w.name, scan_wait=1)
    assert record["checks"][6]["evidence"]["summary"] == PASS_SENTENCE % (AV_NAME, 1)
    assert record["checks"][6]["evidence"]["scan_wait_seconds"] == 1


@with_env
def case_check_7_product_off_fails(env):
    w = env.add_wheel()
    env.set_av([{"displayName": "Windows Defender", "productState": OFF_STATE}])
    record, _ = env.check(w.name)
    c7 = record["checks"][6]
    assert c7["verdict"] == "failed" and record["verdict"] == "not_checked", c7
    assert "no antivirus product is registered as on" in c7["evidence"]["summary"] and "0x060100" in c7["evidence"]["summary"]
    assert not scan_copy_of(env, w).exists() and "copy_name" not in c7["evidence"], "no copy is made when no product is on"


@with_env
def case_check_7_definitions_out_of_date_fails(env):
    w = env.add_wheel()
    env.set_av([{"displayName": AV_NAME, "productState": 0x041010}])
    record, _ = env.check(w.name)
    c7 = record["checks"][6]
    assert c7["verdict"] == "failed" and "definitions are not current" in c7["evidence"]["summary"], c7
    assert "out_of_date" in c7["evidence"]["summary"]


@with_env
def case_check_7_unknown_bytes_are_never_on_or_current(env):
    w = env.add_wheel()
    env.set_av([{"displayName": AV_NAME, "productState": 0x042000}])       # middle byte 0x20: unknown real-time
    record, _ = env.check(w.name)
    assert record["checks"][6]["verdict"] == "failed"
    assert record["checks"][6]["evidence"]["products"][0]["realtime"] == "unknown"
    env.set_av([{"displayName": AV_NAME, "productState": 0x041005}])       # last byte 0x05: unknown definitions
    record, _ = env.check(w.name)
    assert record["checks"][6]["verdict"] == "failed"
    assert record["checks"][6]["evidence"]["products"][0]["definitions"] == "unknown"


@with_env
def case_check_7_no_product_fails(env):
    w = env.add_wheel()
    for answer in ("[]", "", "   \n"):
        env.set_av(answer)
        record, _ = env.check(w.name)
        c7 = record["checks"][6]
        assert c7["verdict"] == "failed" and "no antivirus product" in c7["evidence"]["summary"], (answer, c7)
        assert c7["evidence"]["products_count"] == 0 and record["verdict"] == "not_checked"


@with_env
def case_check_7_unreadable_stand_in_fails(env):
    w = env.add_wheel()
    env.set_av("{this is not json")
    record, _ = env.check(w.name)
    c7 = record["checks"][6]
    assert c7["verdict"] == "failed" and "could not be read" in c7["evidence"]["summary"] and c7["evidence"]["query_failed"]
    env.set_av([{"displayName": AV_NAME}])                                   # an entry without productState
    record, _ = env.check(w.name)
    assert record["checks"][6]["verdict"] == "failed" and record["checks"][6]["evidence"]["query_failed"]
    env.av.unlink()                                                          # the stand-in file is gone
    record, _ = env.check(w.name)
    assert record["checks"][6]["verdict"] == "failed" and record["verdict"] == "not_checked"
    assert not scan_copy_of(env, w).exists()


@with_env
def case_check_7_held_file_changed_during_the_wait_fails(env):
    w = env.add_wheel()

    def change(held, copy):
        held.write_bytes(held.read_bytes() + b"\0")
    record, _ = env.check(w.name, wait_hook=change)
    c7 = record["checks"][6]
    assert c7["verdict"] == "failed" and "held file is changed" in c7["evidence"]["summary"], c7
    assert c7["evidence"]["held_after"] == "changed" and c7["evidence"]["copy_after"] == "unchanged"
    assert record["verdict"] == "not_checked" and not scan_copy_of(env, w).exists()


@with_env
def case_check_7_held_file_removed_during_the_wait_fails(env):
    w = env.add_wheel()
    record, _ = env.check(w.name, wait_hook=lambda held, copy: held.unlink())
    c7 = record["checks"][6]
    assert c7["verdict"] == "failed" and "held file is missing" in c7["evidence"]["summary"], c7
    assert not scan_copy_of(env, w).exists()


@with_env
def case_check_7_copy_removed_during_the_wait_fails(env):
    w = env.add_wheel()
    record, _ = env.check(w.name, wait_hook=lambda held, copy: copy.unlink())     # a quarantine, simulated
    c7 = record["checks"][6]
    assert c7["verdict"] == "failed" and "scan copy is missing" in c7["evidence"]["summary"], c7
    assert "has given a verdict" in c7["evidence"]["summary"] and c7["evidence"]["copy_cleanup"] == "already gone before cleanup"
    assert c7["evidence"]["held_after"] == "unchanged" and record["verdict"] == "not_checked"


@with_env
def case_check_7_copy_changed_during_the_wait_fails(env):
    w = env.add_wheel()

    def change(held, copy):
        copy.write_bytes(b"cleaned by a product")
    record, _ = env.check(w.name, wait_hook=change)
    c7 = record["checks"][6]
    assert c7["verdict"] == "failed" and "scan copy is changed" in c7["evidence"]["summary"], c7
    assert not scan_copy_of(env, w).exists()


@with_env
def case_check_7_copy_is_always_cleaned_up(env):
    w = env.add_wheel()
    copy = scan_copy_of(env, w)
    seen = []

    def watch(held, cp):
        seen.append(cp.is_file() and cp.read_bytes() == held.read_bytes())
    record, _ = env.check(w.name, wait_hook=watch)
    assert record["checks"][6]["verdict"] == "passed" and seen == [True], "the copy existed, byte-identical, during the wait"
    assert not copy.exists() and sorted(p.name for p in env.cfg.holding(BATCH).iterdir()) == [w.name]
    # a hook that raises: the check fails, the copy is still removed
    def boom(held, cp):
        raise RuntimeError("simulated failure during the wait")
    record, _ = env.check(w.name, wait_hook=boom)
    c7 = record["checks"][6]
    assert c7["verdict"] == "failed" and "simulated failure" in c7["evidence"]["summary"]
    assert not copy.exists() and sorted(p.name for p in env.cfg.holding(BATCH).iterdir()) == [w.name]
    # a removal that is refused is reported, as a failure
    real_unlink = pathlib.Path.unlink

    def refuse(self, *a, **k):
        if self.name.endswith(ic.SCAN_COPY_SUFFIX):
            raise PermissionError("simulated refusal")
        return real_unlink(self, *a, **k)
    pathlib.Path.unlink = refuse
    try:
        record, _ = env.check(w.name)
    finally:
        pathlib.Path.unlink = real_unlink
    c7 = record["checks"][6]
    assert c7["verdict"] == "failed" and "could not be removed" in c7["evidence"]["summary"], c7
    assert copy.exists(), "the refused removal left the copy: that is what the report says"
    real_unlink(copy)


@with_env
def case_check_7_stale_copy_from_an_earlier_run_is_removed_and_recorded(env):
    w = env.add_wheel()
    copy = scan_copy_of(env, w)
    copy.write_bytes(b"left behind by a crashed run")
    record, _ = env.check(w.name)
    ev = record["checks"][6]["evidence"]
    assert record["checks"][6]["verdict"] == "passed" and ev["stale_copy_removed"] is True and not copy.exists()


def case_check_7_worked_examples_decode_as_the_cto_measured():
    off = ic.decode_state(393472)
    assert off["hex"] == "0x060100" and off["realtime"] == "off" and off["definitions"] == "current", off
    on = ic.decode_state(266240)
    assert on["hex"] == "0x041000" and on["realtime"] == "on" and on["definitions"] == "current", on
    assert ic.decode_state(0x041100)["realtime"] == "on" and ic.decode_state(0x040000)["realtime"] == "off"
    assert ic.decode_state(0x041010)["definitions"] == "out_of_date"
    for odd in (0x042000, 0x04FF00, 0x041005, 0x0410FF):
        d = ic.decode_state(odd)
        assert "unknown" in (d["realtime"], d["definitions"]), (odd, d)
        assert not (d["realtime"] == "on" and d["definitions"] == "current"), "unknown is never on and current"
    assert ic.decode_state(-1)["realtime"] == "unknown" and ic.decode_state(0x1000000)["definitions"] == "unknown"
    assert ic.decode_state("266240")["realtime"] == "on", "a numeric string decodes the same"


@with_env
def case_check_7_one_object_a_list_and_several_active_products(env):
    w = env.add_wheel()
    env.set_av({"displayName": AV_NAME, "productState": GOOD_STATE})                      # one product: a bare object
    record, _ = env.check(w.name)
    assert record["checks"][6]["verdict"] == "passed" and record["checks"][6]["evidence"]["products_count"] == 1
    env.set_av([{"displayName": "Windows Defender", "productState": OFF_STATE},
                {"displayName": AV_NAME, "productState": GOOD_STATE}])                    # the measured shape of this laptop
    record, _ = env.check(w.name)
    ev = record["checks"][6]["evidence"]
    assert record["checks"][6]["verdict"] == "passed" and ev["products_count"] == 2 and ev["active"] == [AV_NAME]
    env.set_av([{"displayName": "Product One", "productState": 0x041000}, {"displayName": "Product Two", "productState": 0x041100}])
    record, _ = env.check(w.name)
    c7 = record["checks"][6]
    assert c7["verdict"] == "passed" and c7["evidence"]["active"] == ["Product One", "Product Two"]
    assert c7["evidence"]["summary"] == PASS_SENTENCE % ("Product One; Product Two", 0), "all active products are named"
    env.set_av([{"displayName": "Product One", "productState": 0x041000}, {"displayName": "Product Two", "productState": 0x041010}])
    record, _ = env.check(w.name)
    assert record["checks"][6]["verdict"] == "failed", "an active product with out-of-date definitions fails the check"


@with_env
def case_check_7_non_ascii_product_name_is_replaced_with_a_question_mark(env):
    w = env.add_wheel()
    env.set_av([{"displayName": "Anti" + chr(233) + "virus " + chr(252), "productState": GOOD_STATE}])
    record, _ = env.check(w.name)
    c7 = record["checks"][6]
    assert c7["verdict"] == "passed" and c7["evidence"]["summary"] == PASS_SENTENCE % ("Anti?virus ?", 0), c7
    assert c7["evidence"]["products"][0]["name_non_ascii_replaced"] is True
    (env.cfg.records_dir(BATCH) / (w.name + ".check.json")).read_bytes().decode("ascii")


@with_env
def case_leftover_scan_copy_can_never_be_released_or_packed(env):
    w = env.add_wheel()
    copy = scan_copy_of(env, w)
    record, _ = env.check(w.name)
    assert record["verdict"] == "checked"
    # a leftover copy (a crash after the copy was written) sits in holding beside the held file
    copy.write_bytes(w.read_bytes())
    sink = io.StringIO()
    assert ic.run_release(env.cfg, BATCH, copy.name, out=sink) == 1 and "scan copy" in sink.getvalue(), sink.getvalue()
    assert copy.exists() and not (env.cfg.release(BATCH) / copy.name).exists()
    # the genuine file releases; the leftover is still in holding, so pack refuses the batch and names the copy
    assert release(env, w.name)[0] == 0
    rc, msg = pack(env, env.tmp / "packout")
    assert rc == 1 and "files remain in holding" in msg and "leftover check-7 scan copy" in msg and copy.name in msg, msg
    assert not (env.tmp / "packout").exists()
    # even placed by hand in release/, it is refused and never copied
    shutil.move(str(copy), str(env.cfg.release(BATCH) / copy.name))
    rc, msg = pack(env, env.tmp / "packout")
    assert rc == 1 and "scan copy is never a released file" in msg, msg
    assert not (env.tmp / "packout").exists()
    # the check verb refuses a copy's name as a file to check
    r = subprocess.run([sys.executable, str(HERE / "intake_check.py"), "check", "--batch", BATCH, "--file", copy.name],
                       capture_output=True, text=True, timeout=60, stdin=subprocess.DEVNULL,
                       env=dict(os.environ, OPAL_INTAKE_ROOT=str(env.cfg.root), OPAL_INTAKE_RECORDS=str(env.cfg.records_base)))
    assert r.returncode == 1 and "REFUSED" in r.stdout and "scan copy" in r.stdout, r.stdout + r.stderr


def case_selftest_av_line_reads_the_stand_in():
    env = Env()
    try:
        sink = io.StringIO()
        rc = ic.selftest_av(env.cfg, out=sink)
        assert rc == 0 and sink.getvalue() == ("INTAKE-AV products=1 active=%s realtime=on definitions=current ok=True\n" % AV_NAME), sink.getvalue()
        env.set_av([{"displayName": "Windows Defender", "productState": OFF_STATE}, {"displayName": "Other", "productState": 0x041010}])
        sink = io.StringIO()
        rc = ic.selftest_av(env.cfg, out=sink)
        assert rc == 1 and sink.getvalue() == ("INTAKE-AV products=2 active=Other realtime=on definitions=out_of_date ok=False\n"), sink.getvalue()
        env.set_av([])
        sink = io.StringIO()
        rc = ic.selftest_av(env.cfg, out=sink)
        assert rc == 1 and sink.getvalue() == "INTAKE-AV products=0 active=NONE realtime=off definitions=unknown ok=False\n"
    finally:
        env.close()


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
    assert verdicts(record)[8] == "awaiting"
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


# ------------------------------------------------------------------------------------- AMENDMENT 3: item 1 (checks 3 and 6)
def make_editable(env, source="file:///gone/click-src", with_source_dir=False):
    """Turn the installed fixture into an editable install: direct_url.json says so; the source folder is gone."""
    di = env.site / ("%s-%s.dist-info" % (ic.SYN_NAME, ic.SYN_VERSION))
    (di / "direct_url.json").write_text(json.dumps({"dir_info": {"editable": True}, "url": source}), encoding="ascii")
    if not with_source_dir:
        shutil.rmtree(str(env.site / ic.SYN_NAME))


@with_env
def case_editable_install_makes_checks_3_and_6_not_applicable(env):
    make_editable(env)
    w = env.add_wheel()
    record, line = env.check(w.name)
    v = verdicts(record)
    assert v[3] == "not_applicable" and v[6] == "not_applicable", v
    assert record["checks"][2]["evidence"]["reason"] == (
        "the installed distribution is an editable install (source at file:///gone/click-src), not a copy of the published files")
    assert "editable" in record["checks"][5]["evidence"]["reason"]
    assert record["verdict"] == "checked", "not_applicable WITH a reason does not block"
    # the same when the editable source still exists on disk: an editable install is never 'an installed copy'
    env2 = Env()
    try:
        make_editable(env2, with_source_dir=True)
        w2 = env2.add_wheel()
        record2, _ = env2.check(w2.name)
        assert verdicts(record2)[3] == "not_applicable" and verdicts(record2)[6] == "not_applicable"
        assert (env2.site / ic.SYN_NAME / "__init__.py").is_file(), "the source files are still on disk in this arm"
    finally:
        env2.close()
    # an unreadable or non-editable direct_url.json does not make an install editable
    env3 = Env()
    try:
        di = env3.site / ("%s-%s.dist-info" % (ic.SYN_NAME, ic.SYN_VERSION))
        (di / "direct_url.json").write_text('{"dir_info": {}, "url": "file:///x"}', encoding="ascii")
        w3 = env3.add_wheel()
        assert verdicts(env3.check(w3.name)[0])[3] == "passed"
        (di / "direct_url.json").write_text("{not json", encoding="ascii")
        assert verdicts(env3.check(w3.name)[0])[3] == "passed"
    finally:
        env3.close()


def write_installed_record(env, *lines):
    """Rewrite the installed fixture's RECORD (lines as written in a real RECORD; none = delete the file)."""
    rp = env.site / ("%s-%s.dist-info" % (ic.SYN_NAME, ic.SYN_VERSION)) / "RECORD"
    if lines:
        rp.write_text("".join(ln + ",,\n" for ln in lines), encoding="ascii")
    else:
        rp.unlink()


@with_env
def case_check_6_extra_module_in_wheel_fails(env):
    # the installed copy is complete (its RECORD lists only __init__.py, which is on disk); the wheel carries one more module
    w = env.add_wheel(extra={"%s/new_module.py" % ic.SYN_NAME: b"X = 1\n"})
    record, _ = env.check(w.name)
    c6 = record["checks"][5]
    assert c6["verdict"] == "failed" and record["verdict"] == "not_checked", c6
    ev = c6["evidence"]
    assert ev["py_extra"] == ["%s/new_module.py" % ic.SYN_NAME] and ev["py_extra_count"] == 1 and ev["py_missing_count"] == 0
    assert "compared=1 missing=0 extra=1 differ=0" in ev["summary"] and "new_module.py" in ev["summary"], ev["summary"]


@with_env
def case_check_6_missing_file_the_record_lists_is_not_a_difference(env):
    # the installed copy's RECORD lists new_module.py but the file is gone from disk: missing, never differ, never extra
    write_installed_record(env, "%s/__init__.py" % ic.SYN_NAME, "%s/new_module.py" % ic.SYN_NAME)
    w = env.add_wheel(extra={"%s/new_module.py" % ic.SYN_NAME: b"X = 1\n"})
    record, _ = env.check(w.name)
    c6 = record["checks"][5]
    assert c6["verdict"] == "passed", c6
    ev = c6["evidence"]
    assert ev["py_compared"] == 1 and ev["py_identical"] == 1 and ev["py_missing"] == ["%s/new_module.py" % ic.SYN_NAME]
    assert ev["py_extra_count"] == 0 and ev["py_differing_count"] == 0, ev
    assert "compared=1 missing=1 extra=0 differ=0" in ev["summary"], ev["summary"]


@with_env
def case_check_6_record_paths_are_normalised_before_comparing(env):
    write_installed_record(env, "./%s\\__init__.py" % ic.SYN_NAME, ".\\%s/new_module.py" % ic.SYN_NAME)
    shutil.rmtree(str(env.site / ic.SYN_NAME))
    w = env.add_wheel(extra={"%s/new_module.py" % ic.SYN_NAME: b"X = 1\n"})
    record, _ = env.check(w.name)
    c6 = record["checks"][5]
    assert c6["verdict"] == "not_applicable" and c6["evidence"]["py_missing_count"] == 2, c6


@with_env
def case_check_6_every_py_missing_on_disk_is_not_applicable(env):
    write_installed_record(env, "%s/__init__.py" % ic.SYN_NAME, "%s/other.py" % ic.SYN_NAME)
    shutil.rmtree(str(env.site / ic.SYN_NAME))      # a real (non-editable) dist-info whose files are gone
    w = env.add_wheel(extra={"%s/other.py" % ic.SYN_NAME: b"Y = 1\n"})
    record, _ = env.check(w.name)
    v = verdicts(record)
    assert v[3] == "passed" and v[6] == "not_applicable", v
    ev = record["checks"][5]["evidence"]
    assert ev["reason"] == "no installed file to compare (0 of 2 present)", ev["reason"]
    assert ev["py_missing_count"] == 2 and ev["py_differing_count"] == 0 and ev["py_compared"] == 0 and ev["py_extra_count"] == 0
    assert record["verdict"] == "checked"


@with_env
def case_check_6_all_absent_but_one_never_listed_still_fails(env):
    shutil.rmtree(str(env.site / ic.SYN_NAME))      # RECORD lists only __init__.py; the wheel's other.py was never installed
    w = env.add_wheel(extra={"%s/other.py" % ic.SYN_NAME: b"Y = 1\n"})
    c6 = env.check(w.name)[0]["checks"][5]
    assert c6["verdict"] == "failed" and c6["evidence"]["py_extra"] == ["%s/other.py" % ic.SYN_NAME], c6
    assert c6["evidence"]["py_missing"] == ["%s/__init__.py" % ic.SYN_NAME]


@with_env
def case_check_6_without_a_readable_record_absent_is_extra_unless_all_absent(env):
    write_installed_record(env)                      # RECORD deleted
    w = env.add_wheel(extra={"%s/new_module.py" % ic.SYN_NAME: b"X = 1\n"})
    c6 = env.check(w.name)[0]["checks"][5]
    assert c6["verdict"] == "failed" and c6["evidence"]["py_extra"] == ["%s/new_module.py" % ic.SYN_NAME], c6
    assert c6["evidence"]["installed_record_readable"] is False
    shutil.rmtree(str(env.site / ic.SYN_NAME))       # now every .py is absent: nothing to compare
    c6 = env.check(w.name)[0]["checks"][5]
    assert c6["verdict"] == "not_applicable" and c6["evidence"]["reason"] == "no installed file to compare (0 of 2 present)", c6


@with_env
def case_check_6_one_present_file_differing_still_fails_beside_missing(env):
    write_installed_record(env, "%s/__init__.py" % ic.SYN_NAME, "%s/new_module.py" % ic.SYN_NAME)
    w = env.add_wheel(py_bytes=b"VALUE = 3\n", extra={"%s/new_module.py" % ic.SYN_NAME: b"X = 1\n"})
    record, _ = env.check(w.name)
    c6 = record["checks"][5]
    assert c6["verdict"] == "failed" and record["verdict"] == "not_checked", c6
    assert "compared=1 missing=1 extra=0 differ=1" in c6["evidence"]["summary"], c6["evidence"]["summary"]
    assert c6["evidence"]["py_differing"] == ["%s/__init__.py" % ic.SYN_NAME]
    assert "%s/new_module.py" % ic.SYN_NAME not in c6["evidence"]["py_differing"], "a missing file is never counted as differing"


# ------------------------------------------------------------------------------------------- AMENDMENT 3: item 2 (check 8)
CTO_DIR = ic.REPO_ROOT / "org" / "tier1_exec" / "1.0.0_SA_CTO" / "deliverables"
REAL_SIGNATURE = CTO_DIR / "CTO_CHECK_8_NFRA_CTLPLN_INTAKE_BATCH_20261008_A_RPDS_PY_ONLY.md"
REAL_APPROVAL = CTO_DIR / "CTO_APPROVAL_TO_FETCH_NFRA_CTLPLN_INTAKE_BATCH_20261008_A.md"
REAL_BATCH = "intake-20261008-a"
RPDS = "rpds_py-2026.6.3-cp314-cp314-win_amd64.whl"
CLICK = "click-8.3.1-py3-none-any.whl"


@with_env
def case_check_8_refuses_the_approval_file_as_a_signature(env):
    w = env.add_wheel()
    # (a) the signature file IS the --approved-by file (same path)
    sig = env.sign(w.name)
    env.approved = pathlib.Path(sig)
    record, _ = env.check(w.name)
    assert verdicts(record)[8] == "failed" and record["verdict"] == "not_checked"
    assert "is the --approved-by file" in record["checks"][7]["evidence"]["summary"], record["checks"][7]["evidence"]
    # (a) the same CONTENT under another path
    copy = env.tmp / "approval_copy.txt"
    copy.write_bytes(pathlib.Path(sig).read_bytes())
    env.approved = copy
    record, _ = env.check(w.name)
    assert verdicts(record)[8] == "failed" and "is the --approved-by file" in record["checks"][7]["evidence"]["summary"]
    # a genuinely different approved list leaves the signature good
    env.approved = env.tmp / "approved.txt"
    assert verdicts(env.check(w.name)[0])[8] == "passed"
    # (b) names the batch and the file but carries no signing line: an approval-shaped text
    text = "approved to fetch batch %s, file %s. It is NOT CHECK 8 SIGNED. Check 8 is a later file.\n" % (BATCH, w.name)
    record, _ = env.check(w.name, signed=env.sign(w.name, text=text))
    assert verdicts(record)[8] == "failed" and "no line beginning" in record["checks"][7]["evidence"]["summary"], record["checks"][7]
    # (b) the phrase must BEGIN a line; the CTO's own form is accepted too, with markdown emphasis in front
    ok1 = "batch %s\nfile %s\n\n**SIGNED, check 8, for the one file above** -- someone\n" % (BATCH, w.name)
    ok2 = "batch %s\nfile %s\n\nCHECK 8 SIGNED\n" % (BATCH, w.name)
    no = "batch %s\nfile %s\nsigned, check 8 (lower case)\nsee CHECK 8 SIGNED above\n" % (BATCH, w.name)
    assert verdicts(env.check(w.name, signed=env.sign(w.name, text=ok1))[0])[8] == "passed"
    assert verdicts(env.check(w.name, signed=env.sign(w.name, text=ok2))[0])[8] == "passed"
    assert verdicts(env.check(w.name, signed=env.sign(w.name, text=no))[0])[8] == "failed"


def case_check_8_real_cto_files_in_a_temporary_directory():
    assert REAL_SIGNATURE.is_file() and REAL_APPROVAL.is_file(), "the two CTO files must be in this tree"
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="intake_c8_"))
    try:
        sd = tmp / "signer"
        sd.mkdir()
        sig = sd / REAL_SIGNATURE.name
        appr = sd / REAL_APPROVAL.name
        shutil.copy2(str(REAL_SIGNATURE), str(sig))
        shutil.copy2(str(REAL_APPROVAL), str(appr))
        other = tmp / "approved_list.txt"           # a different --approved-by file
        other.write_text("rpds-py==2026.6.3\nclick==8.3.1\n", encoding="ascii")
        cfg = ic.Cfg(root=tmp / "r", records=tmp / "rec", av_json="", sites=[], signer_dir=sd)

        def c8(file_name, signed, approved):
            return ic.check_8({"cfg": cfg, "batch": REAL_BATCH, "file_name": file_name, "signed_by": str(signed),
                               "approved_by": str(approved) if approved else None})
        got = {}
        for label, fn, signed, approved in (
                ("signature/rpds", RPDS, sig, other), ("signature/click", CLICK, sig, other),
                ("approval/rpds", RPDS, appr, other), ("approval/click", CLICK, appr, other),
                ("approval-as-both/rpds", RPDS, appr, appr), ("approval-as-both/click", CLICK, appr, appr)):
            got[label] = c8(fn, signed, approved)
        print("CHECK8-REAL-FILES: " + " | ".join("%s=%s" % (k, v[0]) for k, v in got.items()))
        assert got["signature/rpds"][0] == "passed", got["signature/rpds"]
        assert got["signature/rpds"][1]["signer"] and got["signature/rpds"][1]["path"] == sig.name
        assert got["signature/click"][0] == "failed" and "file name" in got["signature/click"][1]["summary"]
        for k in ("approval/rpds", "approval/click", "approval-as-both/rpds", "approval-as-both/click"):
            assert got[k][0] == "failed", (k, got[k])
        assert "no line beginning" in got["approval/rpds"][1]["summary"] and "no line beginning" in got["approval/click"][1]["summary"]
        assert "is the --approved-by file" in got["approval-as-both/rpds"][1]["summary"]
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)


# ----------------------------------------------------------------------------------------- AMENDMENT 3: item 3 (pack)
def two_files_one_released_one_held(env):
    a = env.add_wheel()
    b = env.add_wheel(version="2.0.0")
    ic.build_installed_fixture(env.site, version="2.0.0")
    env.approved.write_text("%s==1.0.0\n%s==2.0.0\n" % (ic.SYN_NAME, ic.SYN_NAME), encoding="ascii")
    rec_a, _ = env.check(a.name)
    assert rec_a["verdict"] == "checked" and release(env, a.name)[0] == 0
    rec_b, _ = env.check(b.name, signed=False)
    assert rec_b["verdict"] == "not_checked"
    return a, b


@with_env
def case_pack_released_only_packs_the_released_and_names_the_held(env):
    import intake_receive as rcv
    a, b = two_files_one_released_one_held(env)
    out = env.tmp / "packout"
    # without the flag: refused, as before
    rc, msg = pack(env, out)
    assert rc == 1 and "files remain in holding" in msg and b.name in msg and not out.exists(), msg
    sink = io.StringIO()
    rc = ic.run_pack(env.cfg, BATCH, out, out=sink, released_only=True)
    assert rc == 0 and "files=1" in sink.getvalue() and "held_back=1" in sink.getvalue(), sink.getvalue()
    man = json.loads((out / "MANIFEST.json").read_text(encoding="ascii"))
    assert [f["name"] for f in man["files"]] == [a.name], man["files"]
    assert sorted(p.name for p in out.iterdir()) == sorted(
        ["MANIFEST.json", a.name, a.name + ".check.json", a.name + ".delivery.txt"]), "the held file is not in the pack"
    assert len(man["held_back"]) == 1
    hb = man["held_back"][0]
    assert hb["name"] == b.name and hb["verdict"] == "not_checked" and hb["where"] == "holding/%s/" % BATCH, hb
    assert [(c["n"], c["verdict"]) for c in hb["failing_checks"]] == [(8, "unsigned")], hb
    # the receive tool, as merged, still verifies the pack: it reads only manifest['files'] and ignores 'held_back'
    res = rcv.verify_pack(str(out))
    assert res["ok"] is True and res["verified"] == 1 and res["checked"] == 1 and not res["stray"] and not res["pack_defects"], res
    r = subprocess.run([sys.executable, str(HERE / "intake_receive.py"), "verify", "--from", str(out)], capture_output=True,
                       text=True, timeout=100, stdin=subprocess.DEVNULL)
    last = r.stdout.strip().splitlines()[-1]
    assert r.returncode == 0 and last.endswith("wheels=1 verified=1 checked=1 stray=0 ok=True"), r.stdout + r.stderr
    print("PACK-RELEASED-ONLY-VERIFY: " + last)


@with_env
def case_pack_released_only_edges(env):
    # a failing file and a fetch-record-only file are both named as held back
    a, b = two_files_one_released_one_held(env)
    c_fn = "gone-1.0-py3-none-any.whl"
    fr = json.loads((env.cfg.records_dir(BATCH) / (b.name + ".fetch.json")).read_text(encoding="ascii"))
    fr["requested"]["file_name"] = c_fn
    fr["outcome"] = "refused"
    (env.cfg.records_dir(BATCH) / (c_fn + ".fetch.json")).write_text(json.dumps(fr), encoding="ascii")
    sink = io.StringIO()
    out = env.tmp / "packout2"
    assert ic.run_pack(env.cfg, BATCH, out, out=sink, released_only=True) == 0, sink.getvalue()
    man = json.loads((out / "MANIFEST.json").read_text(encoding="ascii"))
    by = {h["name"]: h for h in man["held_back"]}
    assert sorted(by) == sorted([b.name, c_fn]) and by[c_fn]["verdict"] == "no_check_record", by
    assert "fetch record only" in by[c_fn]["where"]
    # a released file that is not checked is still refused even with the flag
    shutil.move(str(b), str(env.cfg.release(BATCH) / b.name))
    sink = io.StringIO()
    assert ic.run_pack(env.cfg, BATCH, env.tmp / "packout3", out=sink, released_only=True) == 1
    assert "does not read 'checked'" in sink.getvalue() and not (env.tmp / "packout3").exists(), sink.getvalue()
    # an empty release folder is still refused
    env2 = Env()
    try:
        env2.add_wheel()
        sink = io.StringIO()
        assert ic.run_pack(env2.cfg, BATCH, env2.tmp / "p", out=sink, released_only=True) == 1 and "holds no files" in sink.getvalue()
    finally:
        env2.close()
    # the CLI flag
    env3 = Env()
    try:
        w = env3.add_wheel()
        env3.check(w.name)
        release(env3, w.name)
        env3.add_wheel(version="2.0.0")
        e = dict(os.environ, OPAL_INTAKE_ROOT=str(env3.cfg.root), OPAL_INTAKE_RECORDS=str(env3.cfg.records_base))
        tool = str(HERE / "intake_check.py")
        r = subprocess.run([sys.executable, tool, "pack", "--batch", BATCH, "--out", str(env3.tmp / "o1")], capture_output=True,
                           text=True, env=e, timeout=100, stdin=subprocess.DEVNULL)
        assert r.returncode == 1 and "files remain in holding" in r.stdout, r.stdout
        r = subprocess.run([sys.executable, tool, "pack", "--batch", BATCH, "--out", str(env3.tmp / "o2"), "--released-only"],
                           capture_output=True, text=True, env=e, timeout=100, stdin=subprocess.DEVNULL)
        assert r.returncode == 0 and "held_back=1" in r.stdout, r.stdout + r.stderr
    finally:
        env3.close()


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
                 OPAL_INTAKE_AV_JSON=str(env.av), OPAL_INTAKE_SITE=str(env.site), OPAL_INTAKE_SIGNER_DIR=str(env.signer_dir))
        tool = str(HERE / "intake_check.py")

        def run(*args):
            return subprocess.run([sys.executable, tool] + list(args), capture_output=True, text=True, env=e, timeout=100,
                                  stdin=subprocess.DEVNULL)
        r = run("check", "--batch", BATCH, "--file", w.name, "--approved-by", str(env.approved), "--scan-wait-seconds", "0")
        assert r.stdout.strip().splitlines()[-1].endswith("c8=unsigned verdict=not_checked"), r.stdout + r.stderr
        r = run("check", "--batch", BATCH, "--file", w.name, "--approved-by", str(env.approved), "--signed-by", sig,
                "--scan-wait-seconds", "0")
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


REAL_AV_NOTE = []


def case_real_security_center_and_on_access_read_on_tiny_synthetic_wheel():
    """Reads the REAL Security Center and runs the real on-access read with the DEFAULT wait (20 s). Skipped only if the query
    itself cannot run. If the query runs but shows no product that is on and current, this case FAILS (it is not adjusted)."""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="intake_real_"))
    try:
        cfg = ic.Cfg(root=tmp / "root", records=tmp / "rec", av_json="", sites=[])
        cfg.av_json = None                      # the real query, whatever the environment says
        hold = cfg.holding("real")
        hold.mkdir(parents=True)
        w = ic.build_synthetic_wheel(hold / ic.syn_file_name())
        before = ic.sha256_file(w)
        t0 = time.time()
        verdict, ev = ic.check_7({"cfg": cfg, "path": w})
        took = time.time() - t0
        if ev.get("query_failed"):
            REAL_AV_NOTE.append("query could not run: %s" % ev.get("summary"))
            raise Skip("the Security Center query could not run: %s" % ev.get("summary"))
        REAL_AV_NOTE.append("products=%s" % "; ".join("%s state=%d hex=%s realtime=%s definitions=%s" % (
            p["display_name"], p["state"], p["hex"], p["realtime"], p["definitions"]) for p in ev.get("products", [])))
        REAL_AV_NOTE.append("verdict=%s waited=%ss took=%.1fs copy_cleanup=%s" % (
            verdict, ev.get("scan_wait_seconds"), took, ev.get("copy_cleanup")))
        REAL_AV_NOTE.append("summary=%s" % ev.get("summary"))
        assert ev["scan_wait_seconds"] == 20 and took >= 19, "the default wait of 20 s was taken"
        assert w.is_file() and ic.sha256_file(w) == before and sorted(p.name for p in hold.iterdir()) == [w.name], \
            "the held file is unchanged and the copy is gone"
        assert verdict == "passed", (verdict, ev.get("summary"))
        assert ev["summary"].endswith("file present and unchanged after 20 s; no on-demand verdict available"), ev["summary"]
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)


# ------------------------------------------------- CT-av-1 (round 27): a named WAIVE line carries a failed check 3 to 7
@with_env
def case_waiver_line_releases_a_failed_check_6_and_keeps_the_failure(env):
    w = env.add_wheel(py_bytes=b"VALUE = 2  # differs from the installed fixture\n")
    text = SIGNER_TEXT % (BATCH, w.name) + "WAIVE %s check 6: synthetic cross-platform difference\n" % w.name
    record, line = env.check(w.name, signed=env.sign(w.name, text=text))
    assert verdicts(record)[6] == "failed" and record["verdict"] == "released-with-waiver", line
    assert record["waived_checks"] == [6] and "c6=failed" in line and line.endswith("verdict=released-with-waiver"), line
    rc, msg = release(env, w.name)
    assert rc == 0, msg
    deliv = (env.cfg.release(BATCH) / (w.name + ".delivery.txt")).read_text(encoding="ascii")
    assert "WAIVED BY THE SIGNED CHECK 8 FILE" in deliv and "synthetic cross-platform difference" in deliv


@with_env
def case_waiver_for_check_1_is_refused_and_check_8_fails(env):
    w = env.add_wheel()
    data = bytearray(w.read_bytes())
    data[len(data) // 2] ^= 0xFF
    w.write_bytes(bytes(data))
    text = SIGNER_TEXT % (BATCH, w.name) + "WAIVE %s check 1: synthetic\n" % w.name
    record, _ = env.check(w.name, signed=env.sign(w.name, text=text))
    assert verdicts(record)[1] == "failed" and verdicts(record)[8] == "failed", verdicts(record)
    assert "can never be waived" in record["checks"][7]["evidence"]["summary"] and record["verdict"] == "not_checked"
    assert release(env, w.name)[0] == 1


@with_env
def case_check_6_records_the_cross_platform_comparison_and_the_crlf_count(env):
    # the installed copy is tagged win_amd64 (its own WHEEL file) and the held wheel is a manylinux one
    (env.site / ("%s-%s.dist-info" % (ic.SYN_NAME, ic.SYN_VERSION)) / "WHEEL").write_text(
        "Wheel-Version: 1.0\nRoot-Is-Purelib: false\nTag: cp312-cp312-win_amd64\n", encoding="ascii")
    (env.site / ic.SYN_NAME / "__init__.py").write_bytes(b"VALUE = 1\r\n")
    w = env.add_wheel(tags=("cp312", "cp312", "manylinux_2_17_x86_64"), py_bytes=b"VALUE = 1\n")
    record, _ = env.check(w.name)
    ev = record["checks"][5]["evidence"]
    # round 28 (ruling 3, amendment 1): the CRLF-only difference across platforms is cleared by the platform rule, so check 6 passes
    assert record["checks"][5]["verdict"] == "passed", "a cross-platform CRLF-only difference is platform-normalised-equal"
    assert ev["compared_across_platforms"] is True and ev["installed_platform"] == "win_amd64", ev
    assert ev["held_platform"] == "manylinux_2_17_x86_64" and ev["py_differing_count"] == 1, ev
    assert ev["differ_after_crlf_normalisation"] == 0, ev
    assert ev["platform_normalised_equal"] == [ic.SYN_NAME + "/__init__.py"] and ev["py_differing_after_platform_rules"] == 0, ev


CASES = [
    case_clean_signed_checked_and_releases, case_unsigned_not_checked_and_release_refuses, case_flipped_byte_fails_check_1,
    case_waiver_line_releases_a_failed_check_6_and_keeps_the_failure, case_waiver_for_check_1_is_refused_and_check_8_fails,
    case_check_6_records_the_cross_platform_comparison_and_the_crlf_count,
    case_differing_py_fails_check_6_and_is_listed,
    case_added_pth_fails_check_6, case_other_hooks_fail_and_known_hook_is_not_a_failure,
    case_release_two_days_old_fails_check_4_default_passes_with_flag,
    case_attestation_absent_not_applicable_unread_failed_present_passed,
    case_file_changed_after_check_record_refused_by_release, case_pack_refuses_batch_with_one_unchecked_file,
    case_pack_succeeds_when_every_file_checked, case_released_file_altered_before_pack_is_refused,
    case_no_installed_copy, case_other_installed_version_only,
    case_check_7_on_and_current_passes_with_the_exact_sentence, case_check_7_sentence_names_the_wait_in_whole_seconds,
    case_check_7_product_off_fails, case_check_7_definitions_out_of_date_fails,
    case_check_7_unknown_bytes_are_never_on_or_current, case_check_7_no_product_fails,
    case_check_7_unreadable_stand_in_fails, case_check_7_held_file_changed_during_the_wait_fails,
    case_check_7_held_file_removed_during_the_wait_fails, case_check_7_copy_removed_during_the_wait_fails,
    case_check_7_copy_changed_during_the_wait_fails, case_check_7_copy_is_always_cleaned_up,
    case_check_7_stale_copy_from_an_earlier_run_is_removed_and_recorded,
    case_check_7_worked_examples_decode_as_the_cto_measured, case_check_7_one_object_a_list_and_several_active_products,
    case_check_7_non_ascii_product_name_is_replaced_with_a_question_mark,
    case_leftover_scan_copy_can_never_be_released_or_packed, case_selftest_av_line_reads_the_stand_in,
    case_check_2_wrong_requests_fail, case_parse_wheel_name, case_check_8_signature_rules,
    case_editable_install_makes_checks_3_and_6_not_applicable, case_check_6_every_py_missing_on_disk_is_not_applicable,
    case_check_6_extra_module_in_wheel_fails, case_check_6_missing_file_the_record_lists_is_not_a_difference,
    case_check_6_record_paths_are_normalised_before_comparing, case_check_6_all_absent_but_one_never_listed_still_fails,
    case_check_6_without_a_readable_record_absent_is_extra_unless_all_absent,
    case_check_6_one_present_file_differing_still_fails_beside_missing,
    case_check_8_refuses_the_approval_file_as_a_signature, case_check_8_real_cto_files_in_a_temporary_directory,
    case_pack_released_only_packs_the_released_and_names_the_held, case_pack_released_only_edges,
    case_default_signer_dir_is_the_ctos_deliverables, case_no_path_to_checked_without_the_signature,
    case_hand_edited_record_cannot_release, case_missing_fetch_record_and_held_file_fail,
    case_failed_fetch_outcome_fails_check_1, case_constants_appear_verbatim_in_the_brief, case_records_are_ascii_only,
    case_cli_honours_the_environment_names, case_selftest_unsigned_leaves_nothing_behind,
    case_real_security_center_and_on_access_read_on_tiny_synthetic_wheel,
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
    if REAL_AV_NOTE:
        print("REAL-SECURITY-CENTER: " + " | ".join(REAL_AV_NOTE))
    total = len(CASES)
    ok = passed + skipped == total
    print("INTAKE-CHECK-TEST cases=%d/%d skipped=%d ok=%s" % (passed, total, skipped, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
