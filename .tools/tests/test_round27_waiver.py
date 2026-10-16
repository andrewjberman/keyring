#!/usr/bin/env python3
"""test_round27_waiver.py -- NFRA_CTLPLN round 27, TO CT-av-1: a failed check 3 to 7 is carried to release only by a named,
reasoned WAIVE line in the signed check-8 file; a waiver never carries check 1 or check 2 (or check 8); check 6 records the
cross-platform comparison and the count after CRLF normalisation, and its verdict does not change.

SYNTHETIC wheels, a temporary signer directory and a temporary installed site only. No network, no install, no import or
execution of anything from a wheel, nothing under C:/opal-intake/ and no real batch. Standard library plus the two tools
beside org/devices/intake/. Every temporary folder is removed at the end. ASCII output only. LAST line:
  WAIVER arms=<k>/<n> ok=<True|False>
"""
import io
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import traceback

REPO = pathlib.Path(__file__).resolve().parents[2]
INTAKE = REPO / "org" / "devices" / "intake"
sys.path.insert(0, str(INTAKE))
import intake_check as ic  # noqa: E402
import intake_receive as ir  # noqa: E402

RECEIVE_TOOL = str(INTAKE / "intake_receive.py")
BATCH = "w134"
GOOD_STATE = 266240      # real-time on, definitions current
WAIVE_REASON = "synthetic cross-platform difference, read line by line in the cell"
SIGNER_TEXT = "batch %s\nfile %s\n\nCHECK 8 SIGNED -- synthetic signer for the waiver arms\n"
ARMS = []
ARM_TEMP = []


def arm(fn):
    ARMS.append(fn)
    return fn


class Env:
    """A fresh temporary world: a holding root, records, a Security Center stand-in, an installed site and a signer folder."""

    def __init__(self, installed_tag=None):
        self.tmp = pathlib.Path(tempfile.mkdtemp(prefix="waiver_t_"))
        ARM_TEMP.append(self.tmp)
        self.site = self.tmp / "site"
        self.site.mkdir()
        self.signer = self.tmp / "signer"
        self.signer.mkdir()
        self.dist = ic.build_installed_fixture(self.site)
        if installed_tag is not None:
            (self.dist / "WHEEL").write_text("Wheel-Version: 1.0\nGenerator: synthetic\nRoot-Is-Purelib: false\nTag: %s\n"
                                             % installed_tag, encoding="ascii")
        av = self.tmp / "av.json"
        av.write_text(json.dumps([{"displayName": "Synthetic Antivirus (stand-in)", "productState": GOOD_STATE}]), encoding="ascii")
        self.cfg = ic.Cfg(root=self.tmp / "root", records=self.tmp / "records", av_json=str(av), sites=[self.site],
                          signer_dir=self.signer)
        self.approved = self.tmp / "approved.txt"
        self.approved.write_text("%s==%s\n" % (ic.SYN_NAME, ic.SYN_VERSION), encoding="ascii")
        self.n_sig = 0

    def wheel(self, tags=ic.SYN_TAGS, py_bytes=ic.SYN_PY, extra=None, fetch_kw=None):
        hold = self.cfg.holding(BATCH)
        hold.mkdir(parents=True, exist_ok=True)
        path = ic.build_synthetic_wheel(hold / ic.syn_file_name(tags=tags), tags=tags, py_bytes=py_bytes, extra=extra)
        ic.write_fetch_record(self.cfg, BATCH, path, tags=tags, **(fetch_kw or {}))
        return path

    def sign(self, name, extra=""):
        """A signature file under the signer folder: the batch and file text, the CHECK 8 SIGNED line, then `extra`."""
        self.n_sig += 1
        p = self.signer / ("signature_%d.txt" % self.n_sig)
        p.write_text((SIGNER_TEXT % (BATCH, name)) + extra, encoding="ascii")
        return str(p)

    def check(self, name, extra="", signed=True, text=None):
        """Run the eight checks. `text` replaces the whole signature file; signed=False passes no signature."""
        if text is not None:
            self.n_sig += 1
            p = self.signer / ("signature_%d.txt" % self.n_sig)
            p.write_text(text, encoding="ascii")
            signed_by = str(p)
        else:
            signed_by = self.sign(name, extra) if signed else None
        sink = io.StringIO()
        record, _ = ic.run_check(self.cfg, BATCH, name, approved_by=str(self.approved), signed_by=signed_by, out=sink,
                                 scan_wait=0)
        return record

    def release(self, name):
        sink = io.StringIO()
        rc = ic.run_release(self.cfg, BATCH, name, out=sink)
        return rc, sink.getvalue()

    def pack(self, out):
        sink = io.StringIO()
        rc = ic.run_pack(self.cfg, BATCH, str(out), out=sink)
        return rc, sink.getvalue()

    def record_path(self, name):
        return self.cfg.records_dir(BATCH) / (name + ".check.json")

    def close(self):
        shutil.rmtree(str(self.tmp), ignore_errors=True)


def verdict_of(record, n):
    return {c["n"]: c["verdict"] for c in record["checks"]}[n]


def run_verify(pack):
    cp = subprocess.run([sys.executable, RECEIVE_TOOL, "verify", "--from", str(pack)], capture_output=True, text=True,
                        timeout=110, stdin=subprocess.DEVNULL)
    return cp.returncode, [ln for ln in cp.stdout.splitlines() if ln.strip()]


def released_waived(env):
    """A wheel whose check 6 fails, signed with a WAIVE line for check 6, released. Returns (file name, record)."""
    w = env.wheel(py_bytes=b"VALUE = 2\n")
    rec = env.check(w.name, extra="WAIVE %s check 6: %s\n" % (w.name, WAIVE_REASON))
    rc, msg = env.release(w.name)
    assert rc == 0, msg
    return w.name, rec


# ----------------------------------------------------------------------------------------------- the CTO's arms (a) to (g)
@arm
def arm_a_unwaived_failed_check_6_still_refuses_release():
    env = Env()
    try:
        w = env.wheel(py_bytes=b"VALUE = 2\n")
        rec = env.check(w.name)
        assert verdict_of(rec, 6) == "failed" and rec["verdict"] == "not_checked", rec["verdict"]
        rc, msg = env.release(w.name)
        assert rc == 1 and "does not read 'checked' or 'released-with-waiver'" in msg and w.exists(), msg
    finally:
        env.close()


@arm
def arm_b1_waiver_for_a_different_file_does_not_carry():
    env = Env()
    try:
        w = env.wheel(py_bytes=b"VALUE = 2\n")
        other = ic.syn_file_name(ic.SYN_NAME, "9.9.9")
        rec = env.check(w.name, extra="WAIVE %s check 6: %s\n" % (other, WAIVE_REASON))
        assert rec["checks"][7]["evidence"]["waivers"] == [], rec["checks"][7]["evidence"]
        assert verdict_of(rec, 6) == "failed" and rec["verdict"] == "not_checked" and rec["waived_checks"] == []
        assert env.release(w.name)[0] == 1
    finally:
        env.close()


@arm
def arm_b2_waiver_for_a_different_check_does_not_carry():
    env = Env()
    try:
        w = env.wheel(py_bytes=b"VALUE = 2\n")
        rec = env.check(w.name, extra="WAIVE %s check 5: %s\n" % (w.name, WAIVE_REASON))
        assert rec["checks"][7]["evidence"]["waivers"] == [{"check": 5, "reason": WAIVE_REASON}]
        assert verdict_of(rec, 6) == "failed" and verdict_of(rec, 5) == "not_applicable", rec["checks"][4]
        assert rec["verdict"] == "not_checked" and rec["waived_checks"] == [], rec["verdict"]
    finally:
        env.close()


@arm
def arm_c_waiver_line_in_a_file_without_the_check_8_marker_does_not_carry():
    env = Env()
    try:
        w = env.wheel(py_bytes=b"VALUE = 2\n")
        text = "batch %s\nfile %s\nWAIVE %s check 6: %s\n" % (BATCH, w.name, w.name, WAIVE_REASON)
        rec = env.check(w.name, text=text)
        assert verdict_of(rec, 8) == "failed" and "no line beginning" in rec["checks"][7]["evidence"]["summary"], rec["checks"][7]
        assert verdict_of(rec, 6) == "failed" and rec["verdict"] == "not_checked"
    finally:
        env.close()


@arm
def arm_d1_waiver_of_check_1_is_refused_and_check_8_fails():
    env = Env()
    try:
        w = env.wheel(py_bytes=b"VALUE = 2\n")
        rec = env.check(w.name, extra="WAIVE %s check 1: %s\n" % (w.name, WAIVE_REASON))
        c8 = rec["checks"][7]
        assert c8["verdict"] == "failed" and "can never be waived" in c8["evidence"]["summary"], c8
        assert c8["evidence"]["refused_waivers"] == [{"check": 1, "reason": WAIVE_REASON}]
        assert rec["verdict"] == "not_checked" and env.release(w.name)[0] == 1
    finally:
        env.close()


@arm
def arm_d2_waiver_of_check_2_is_refused_and_check_8_fails():
    env = Env()
    try:
        w = env.wheel()
        data = bytearray(w.read_bytes())
        data[len(data) // 2] ^= 0xFF          # check 1 fails: the held bytes differ from the published digest
        w.write_bytes(bytes(data))
        rec = env.check(w.name, extra="WAIVE %s check 2: %s\n" % (w.name, WAIVE_REASON))
        assert verdict_of(rec, 1) == "failed" and verdict_of(rec, 8) == "failed", rec["checks"][7]
        assert rec["checks"][7]["evidence"]["refused_waivers"] == [{"check": 2, "reason": WAIVE_REASON}]
        assert rec["verdict"] == "not_checked"
    finally:
        env.close()


@arm
def arm_e_four_style_line_releases_with_waiver_and_check_6_still_reads_failed():
    env = Env()
    try:
        name, rec = released_waived(env)
        assert rec["verdict"] == "released-with-waiver" and rec["waived_checks"] == [6], (rec["verdict"], rec["waived_checks"])
        assert verdict_of(rec, 6) == "failed", "the failure is kept, never edited to passed"
        assert rec["checks"][5]["evidence"]["summary"], rec["checks"][5]
        on_disk = json.loads(env.record_path(name).read_text(encoding="ascii"))
        assert on_disk["verdict"] == "released-with-waiver" and on_disk["waived_checks"] == [6]
        assert (env.cfg.release(BATCH) / name).is_file() and not (env.cfg.holding(BATCH) / name).exists()
        deliv = (env.cfg.release(BATCH) / (name + ".delivery.txt")).read_text(encoding="ascii")
        assert "overall: released-with-waiver" in deliv and "WAIVED BY THE SIGNED CHECK 8 FILE" in deliv and WAIVE_REASON in deliv
    finally:
        env.close()


@arm
def arm_f1_released_waived_pack_verifies_with_the_waived_line_before_the_last_line():
    env = Env()
    try:
        name, _ = released_waived(env)
        out = env.tmp / "pack"
        rc, msg = env.pack(out)
        assert rc == 0, msg
        code, lines = run_verify(out)
        assert code == 0 and lines[-1].startswith("INTAKE-VERIFY pack=") and lines[-1].endswith("checked=1 stray=0 ok=True"), lines
        hits = [i for i, ln in enumerate(lines) if ln == "INTAKE-VERIFY-WAIVED %s check 6: %s" % (name, WAIVE_REASON)]
        assert len(hits) == 1 and hits[0] < len(lines) - 1, lines
    finally:
        env.close()


@arm
def arm_f2_not_checked_record_still_refused_by_verify():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="waiver_pack_"))
    ARM_TEMP.append(tmp)
    try:
        pack = tmp / "pack"
        pack.mkdir()
        wheel = ir.build_synthetic_wheel(str(pack), "w134pkg", "1.0", {"w134pkg": "X = 1\n"})
        name = pathlib.Path(wheel).name
        ir.write_check_record(str(pack), name, verdict="not_checked")
        ir.write_manifest(str(pack))
        code, lines = run_verify(pack)
        assert code == 1 and lines[-1].endswith("ok=False"), lines
        assert any("not 'checked' or 'released-with-waiver'" in ln and name in ln for ln in lines), lines
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)


@arm
def arm_f3_waived_record_whose_waiver_was_stripped_is_refused_by_verify():
    env = Env()
    try:
        name, _ = released_waived(env)
        out = env.tmp / "pack"
        assert env.pack(out)[0] == 0
        rp = out / (name + ".check.json")
        data = json.loads(rp.read_text(encoding="ascii"))
        data["checks"][7]["evidence"]["waivers"] = []       # the record still says released-with-waiver
        rp.write_text(json.dumps(data), encoding="ascii")
        ir.write_manifest(str(out))
        code, lines = run_verify(out)
        assert code == 1 and lines[-1].endswith("ok=False"), lines
        assert any("re-derive as 'not_checked'" in ln for ln in lines), lines
    finally:
        env.close()


@arm
def arm_g1_cross_platform_check_6_records_the_comparison_and_the_crlf_count():
    env = Env(installed_tag="cp312-cp312-win_amd64")
    try:
        init = env.site / ic.SYN_NAME / "__init__.py"
        init.write_bytes(b"VALUE = 1\r\n")                  # the installed copy: CRLF line ends
        w = env.wheel(tags=("cp312", "cp312", "manylinux_2_17_x86_64"), py_bytes=b"VALUE = 1\n")
        rec = env.check(w.name)
        c6 = rec["checks"][5]
        ev = c6["evidence"]
        # a cross-platform CRLF-only difference is platform-normalised-equal (check 6 is platform-aware, CT-aw-1)
        assert c6["verdict"] == "passed", c6["verdict"]
        assert ev["platform_normalised_equal"] == [ic.SYN_NAME + "/__init__.py"], ev["platform_normalised_equal"]
        assert ev["py_differing_count"] == 1, ev["py_differing_count"]
        assert ev["differ_after_crlf_normalisation"] == 0, ev["differ_after_crlf_normalisation"]
        assert ev["compared_across_platforms"] is True, ev
        assert ev["installed_platform"] == "win_amd64" and ev["held_platform"] == "manylinux_2_17_x86_64", ev
    finally:
        env.close()


@arm
def arm_g2_same_platform_is_not_recorded_as_cross_platform():
    env = Env(installed_tag="cp312-cp312-win_amd64")
    try:
        w = env.wheel()
        ev = env.check(w.name)["checks"][5]["evidence"]
        assert ev["compared_across_platforms"] is False and ev["installed_platform"] == ev["held_platform"] == "win_amd64", ev
        assert ev["differ_after_crlf_normalisation"] == 0 and ev["py_differing_count"] == 0, ev
    finally:
        env.close()


# ------------------------------------------------------------------------------------------------ controls and parity (K, P)
def checks_of(fail=(), c8="passed", waivers=None, refused=None):
    """A synthetic record's check list: checks 1 to 7 passed except `fail`; check 8 with a signer, a path and the given waivers."""
    out = []
    for n in range(1, 8):
        out.append({"n": n, "verdict": "failed" if n in fail else "passed", "evidence": {"summary": "synthetic"}})
    ev8 = {"signer": "s", "path": "p"}
    if waivers is not None:
        ev8["waivers"] = waivers
    if refused is not None:
        ev8["refused_waivers"] = refused
    out.append({"n": 8, "verdict": c8, "evidence": ev8})
    return out


@arm
def arm_k1_control_a_waiver_never_carries_failed_check_1():
    c = checks_of(fail=(1,), waivers=[{"check": 1, "reason": "r"}])
    assert ic.compute_verdict(c) == "not_checked" and ic.waived_checks_of(c) == []
    assert ir._derive_waived(c)[0] == "not_checked"


@arm
def arm_k2_control_a_waiver_never_carries_failed_check_2():
    c = checks_of(fail=(2,), waivers=[{"check": 2, "reason": "r"}])
    assert ic.compute_verdict(c) == "not_checked" and ic.waived_checks_of(c) == []
    assert ir._derive_waived(c)[0] == "not_checked"


@arm
def arm_k3_control_check_8_is_never_waivable():
    for c in (checks_of(c8="failed", waivers=[{"check": 8, "reason": "r"}]),
              checks_of(fail=(6,), waivers=[{"check": 8, "reason": "r"}]),
              checks_of(fail=(6,), c8="failed", waivers=[{"check": 6, "reason": "r"}])):
        assert ic.compute_verdict(c) == "not_checked", c[7]
        assert ir._derive_waived(c)[0] == "not_checked"


@arm
def arm_k4_control_refused_waiver_on_check_8_blocks_every_carry():
    c = checks_of(fail=(6,), waivers=[{"check": 6, "reason": "r"}], refused=[{"check": 1, "reason": "r"}])
    assert ic.compute_verdict(c) == "not_checked" and ir._derive_waived(c)[0] == "not_checked"


@arm
def arm_k5_control_out_of_range_and_empty_waivers_carry_nothing():
    for waivers in ([{"check": 9, "reason": "r"}], [{"check": 0, "reason": "r"}], [{"check": 6, "reason": "  "}],
                    [{"check": "6", "reason": "r"}]):
        c = checks_of(fail=(6,), waivers=waivers)
        assert ic.compute_verdict(c) == "not_checked", waivers
        assert ir._derive_waived(c)[0] == "not_checked", waivers


@arm
def arm_p0_positive_control_the_synthetic_model_releases_with_a_waiver():
    c = checks_of(fail=(6,), waivers=[{"check": 6, "reason": "r"}])
    assert ic.compute_verdict(c) == "released-with-waiver" and ic.waived_checks_of(c) == [6]
    assert ir._derive_waived(c) == ("released-with-waiver", [6])
    good = checks_of()
    assert ic.compute_verdict(good) == "checked" and ic.waived_checks_of(good) == []


@arm
def arm_p1_parse_waivers_reads_only_the_exact_form_for_this_file():
    text = "\n".join([
        "**WAIVE F check 6: reason one**",
        "WAIVE F check 1: refused",
        "WAIVE F check 8: ignored",
        "WAIVE F check 9: out of range",
        "WAIVE F check 6:",
        "waive F check 5: lower case",
        "WAIVE G check 5: another file",
        "WAIVE F check 3: a second reason",
        "A sentence with WAIVE F check 4: mid-line is not a waiver",
        "WAIVE F check 4:no space after the colon",
    ])
    waivers, refused, ignored = ic.parse_waivers(text, "F")
    assert waivers == [{"check": 6, "reason": "reason one"}, {"check": 3, "reason": "a second reason"}], waivers
    assert refused == [{"check": 1, "reason": "refused"}], refused
    assert [i["check"] for i in ignored] == [8, 9, 6], ignored
    assert ignored[2]["why"] == "empty reason", ignored[2]


@arm
def arm_p2_receive_mirror_agrees_with_the_check_tool_on_every_shape():
    shapes = [checks_of(), checks_of(fail=(6,)), checks_of(fail=(6,), waivers=[{"check": 6, "reason": "r"}]),
              checks_of(fail=(3, 7), waivers=[{"check": 3, "reason": "r"}, {"check": 7, "reason": "r"}]),
              checks_of(fail=(3, 4), waivers=[{"check": 3, "reason": "r"}]),
              checks_of(fail=(1,), waivers=[{"check": 1, "reason": "r"}]),
              checks_of(fail=(6,), c8="failed", waivers=[{"check": 6, "reason": "r"}]),
              checks_of(fail=(6,), waivers=[{"check": 6, "reason": "r"}], refused=[{"check": 2, "reason": "r"}])]
    for c in shapes:
        tool_verdict, tool_carried = ic._derive(c)
        ours_verdict, ours_carried = ir._derive_waived(c)
        assert (tool_verdict == "released-with-waiver") == (ours_verdict == "released-with-waiver"), (tool_verdict, ours_verdict)
        if tool_verdict == "released-with-waiver":
            assert tool_carried == ours_carried, (tool_carried, ours_carried)


def main():
    passed = 0
    try:
        for fn in ARMS:
            try:
                fn()
                passed += 1
                print("PASS: %s" % fn.__name__)
            except Exception as exc:  # a test harness reports every failure
                print("FAIL: %s: %s: %s" % (fn.__name__, type(exc).__name__, str(exc).encode("ascii", "backslashreplace").decode()))
                traceback.print_exc(file=sys.stdout)
    finally:
        for t in ARM_TEMP:
            shutil.rmtree(str(t), ignore_errors=True)
    ok = passed == len(ARMS)
    print("WAIVER arms=%d/%d ok=%s" % (passed, len(ARMS), ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
