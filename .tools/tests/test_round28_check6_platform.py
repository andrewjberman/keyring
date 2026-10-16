#!/usr/bin/env python3
"""NFRA_CTLPLN round 28, TO-CT-aw-1 -- intake check 6, platform-aware (CTO round-27 analysis, ruling 3).

Two modes, both standard library plus org/devices/intake/intake_check.py:

  python .tools/tests/test_round28_check6_platform.py          synthetic arms (wheels and installed copies built in temporary
                                                               folders; no network; nothing outside those folders is written)
                                                               LAST line: CHECK6-PLATFORM arms=<k>/<n> ok=<True|False>
  python .tools/tests/test_round28_check6_platform.py --real4  READ ONLY: the four real yfinance wheels in the release folder are
                                                               checked in memory by check_3 then check_6; nothing is written.
                                                               LAST line: REAL4 passed=<k>/4 ok=<True|False>
                                                               (absent folder: REAL4 SKIPPED folder absent, exit 2)

WHAT THE ARMS DEFEND (cross-platform means the held wheel's platform tag differs from the installed copy's WHEEL Tag):
  a  a CRLF-only difference passes; the file is listed in platform_normalised_equal
  b  a delvewheel block present on one side only passes
  c  a differing numpy/__config__.py (the one build-metadata file) passes and is listed; the same kind of difference in an
     unlisted file fails
  d  a planted edited line fails, with or without CRLF and a delvewheel block beside it
  e  the same platform: a CRLF-only difference and a differing numpy/__config__.py still fail, and the rule is never called
  f  .data/scripts and .data/data members and over-size files keep failing across platforms
  g  controls: the rule does not pass a planted edit; a mutant rule that passes everything makes arm d fail (it is caught);
     CHECK6_BUILD_METADATA_FILES holds exactly one entry
"""
from __future__ import annotations

import pathlib
import shutil
import sys
import tempfile
import traceback
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[1]
INTAKE = ROOT / "org" / "devices" / "intake"
sys.path.insert(0, str(INTAKE))
import intake_check as ic  # noqa: E402

SYN, SYN_V = "selftestpkg", "1.0.0"
WIN = ("cp312", "cp312", "win_amd64")
LIN = ("cp312", "cp312", "manylinux_2_17_x86_64")
ENTRY = b"[console_scripts]\nselftest = selftestpkg:main\n"
BATCH = "check6-platform"
RELEASE = pathlib.Path("C:/opal-intake/release/intake-20261016-yfinance-linux")
REAL_NAMES = ("curl_cffi", "numpy", "pandas", "websockets")


def _wheel_text(tags):
    return "Wheel-Version: 1.0\nRoot-Is-Purelib: false\nTag: %s\n" % "-".join(tags)


def _meta(name, version):
    return ("Metadata-Version: 2.1\nName: %s\nVersion: %s\n\nsynthetic\n" % (name, version)).encode("ascii")


def run6(name=SYN, version=SYN_V, held_tags=LIN, installed_tag=WIN, wheel_files=None, installed_files=None, file_name=None):
    """Build a held wheel (zip, members = wheel_files plus its own dist-info) and an installed copy (site dir, members =
    installed_files plus its dist-info; its WHEEL file only when installed_tag is given); run check_3 then check_6 the way
    run_check builds the context, in memory and in temporary folders only. Returns (verdict, evidence)."""
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="check6_platform_"))
    try:
        di = "%s-%s.dist-info" % (name, version)
        whl = tmp / ("%s-%s-%s-%s-%s.whl" % ((name, version) + tuple(held_tags)) if file_name is None else file_name)
        members = dict(wheel_files or {})
        members[di + "/METADATA"] = _meta(name, version)
        members[di + "/WHEEL"] = _wheel_text(held_tags).encode("ascii")
        members[di + "/entry_points.txt"] = ENTRY
        members[di + "/RECORD"] = "".join("%s,,\n" % k for k in sorted(members)).encode("ascii") + (di + "/RECORD,,\n").encode("ascii")
        with zipfile.ZipFile(whl, "w", zipfile.ZIP_DEFLATED) as zf:
            for k in sorted(members):
                zf.writestr(k, members[k])
        site = tmp / "site"
        idi = site / di
        idi.mkdir(parents=True)
        (idi / "METADATA").write_bytes(_meta(name, version))
        (idi / "entry_points.txt").write_bytes(ENTRY)
        if installed_tag is not None:
            (idi / "WHEEL").write_text(_wheel_text(installed_tag), encoding="ascii")
        inst = dict(installed_files or {})
        for rel, data in inst.items():
            p = site / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(data)
        listing = sorted(set(inst) | {di + "/METADATA", di + "/entry_points.txt", di + "/RECORD"}
                         | ({di + "/WHEEL"} if installed_tag is not None else set()))
        (idi / "RECORD").write_text("".join("%s,,\n" % k for k in listing), encoding="ascii")
        cfg = ic.Cfg(root=tmp / "root", records=tmp / "records", av_json="", sites=[site], signer_dir=tmp / "signer")
        ctx = {"cfg": cfg, "batch": BATCH, "file_name": whl.name, "path": whl, "fetch": {"requested": {
                   "name": name, "version": version, "python_tag": held_tags[0], "abi_tag": held_tags[1],
                   "platform_tag": held_tags[2], "file_name": whl.name}},
               "approved_by": None, "signed_by": None, "min_age": 14.0, "min_earlier": 3, "scan_wait": 0, "wait_hook": None}
        v3, ev3 = ic.check_3(ctx)
        assert v3 == "passed", "check 3 must find the installed copy for the arm to mean anything: %r" % (ev3,)
        return ic.check_6(ctx)
    finally:
        shutil.rmtree(str(tmp), ignore_errors=True)


def _expect(verdict, ev, want, **fields):
    assert verdict == want, "check 6 read %r, wanted %r: %s" % (verdict, want, ev.get("summary"))
    for k, v in fields.items():
        assert ev.get(k) == v, "%s is %r, wanted %r" % (k, ev.get(k), v)


def _init_pair(py_wheel, py_inst=None):
    """The synthetic package's __init__.py, held and installed (py_inst defaults to the same bytes)."""
    return {SYN + "/__init__.py": py_wheel}, {SYN + "/__init__.py": py_wheel if py_inst is None else py_inst}


# ------------------------------------------------------------------------------------------------------------ arms a to g
def arm_a_crlf_only_cross_platform_passes():
    w, i = _init_pair(b"VALUE = 1\n", b"VALUE = 1\r\n")
    v, ev = run6(wheel_files=w, installed_files=i)
    _expect(v, ev, "passed", compared_across_platforms=True, py_differing=[], py_differing_count=1,
            py_differing_after_platform_rules=0, platform_normalised_equal=[SYN + "/__init__.py"], build_metadata_residual=[])
    assert "platform-normalised-equal=1 build-metadata-residual=0" in ev["summary"], ev["summary"]


def arm_b_delvewheel_block_cross_platform_passes():
    block = b"import os\n# start delvewheel patch\nos.add_dll_directory('x')\n# end delvewheel patch\nVALUE = 1\n"
    w, i = _init_pair(b"import os\nVALUE = 1\n", block)
    v, ev = run6(wheel_files=w, installed_files=i)
    _expect(v, ev, "passed", py_differing=[], platform_normalised_equal=[SYN + "/__init__.py"])
    w2, i2 = _init_pair(block, b"import os\nVALUE = 1\n")      # the block on the WHEEL side only
    v2, ev2 = run6(wheel_files=w2, installed_files=i2)
    _expect(v2, ev2, "passed", py_differing=[], platform_normalised_equal=[SYN + "/__init__.py"])


def arm_c_numpy_build_metadata_file_passes_and_other_file_fails():
    init = b"VALUE = 1\n"
    w = {"numpy/__init__.py": init, "numpy/__config__.py": b"BUILD = 'gcc-linux'\n"}
    i = {"numpy/__init__.py": init, "numpy/__config__.py": b"BUILD = 'msvc-windows'\n"}
    v, ev = run6(name="numpy", version="2.4.2", wheel_files=w, installed_files=i)
    _expect(v, ev, "passed", py_differing=[], py_differing_count=1, build_metadata_residual=["numpy/__config__.py"],
            platform_normalised_equal=[])
    # the same kind of difference in a file NOT on the list: failed, and it is the residual
    w2 = {"numpy/__init__.py": init, "numpy/_build_info.py": b"BUILD = 'gcc-linux'\n"}
    i2 = {"numpy/__init__.py": init, "numpy/_build_info.py": b"BUILD = 'msvc-windows'\n"}
    v2, ev2 = run6(name="numpy", version="2.4.2", wheel_files=w2, installed_files=i2)
    _expect(v2, ev2, "failed", py_differing=["numpy/_build_info.py"], build_metadata_residual=[])
    # the listed file beside an unlisted residual: the listed one passes, the unlisted one still fails the check
    w3 = dict(w, **{"numpy/_build_info.py": b"BUILD = 'gcc-linux'\n"})
    i3 = dict(i, **{"numpy/_build_info.py": b"BUILD = 'msvc-windows'\n"})
    v3, ev3 = run6(name="numpy", version="2.4.2", wheel_files=w3, installed_files=i3)
    _expect(v3, ev3, "failed", py_differing=["numpy/_build_info.py"], build_metadata_residual=["numpy/__config__.py"])


def arm_d_planted_edit_fails_across_platforms():
    # d1: a plain planted edited line
    w, i = _init_pair(b"VALUE = 2\n", b"VALUE = 1\n")
    v, ev = run6(wheel_files=w, installed_files=i)
    _expect(v, ev, "failed", py_differing=[SYN + "/__init__.py"], py_differing_after_platform_rules=1)
    # d2: the planted edit with CRLF on the installed side and a delvewheel block beside it
    w2, i2 = _init_pair(b"import os\nVALUE = 2\n",
                        b"import os\r\n# start delvewheel patch\r\nos.add_dll_directory('x')\r\n# end delvewheel patch\r\nVALUE = 1\r\n")
    v2, ev2 = run6(wheel_files=w2, installed_files=i2)
    _expect(v2, ev2, "failed", py_differing=[SYN + "/__init__.py"], platform_normalised_equal=[])
    # d3: the planted edit in an ordinary module, the block and CRLF beside it in that same module
    w3 = {SYN + "/__init__.py": b"VALUE = 1\n", SYN + "/mod.py": b"B = 2\n"}
    i3 = {SYN + "/__init__.py": b"VALUE = 1\n",
          SYN + "/mod.py": b"# start delvewheel patch\nA = 1\n# end delvewheel patch\nB = 1\r\n"}
    v3, ev3 = run6(wheel_files=w3, installed_files=i3)
    _expect(v3, ev3, "failed", py_differing=[SYN + "/mod.py"], py_differing_after_platform_rules=1)


def arm_e_same_platform_is_unchanged():
    spy = {"n": 0}
    real_rule = ic._platform_rule

    def spy_rule(*a, **k):
        spy["n"] += 1
        return real_rule(*a, **k)

    ic._platform_rule = spy_rule
    try:
        w, i = _init_pair(b"VALUE = 1\n", b"VALUE = 1\r\n")
        v, ev = run6(installed_tag=LIN, held_tags=LIN, wheel_files=w, installed_files=i)
        _expect(v, ev, "failed", compared_across_platforms=False, py_differing=[SYN + "/__init__.py"],
                platform_normalised_equal=[], build_metadata_residual=[])
        assert spy["n"] == 0, "the platform rule was consulted on a same-platform comparison"
        w2 = {"numpy/__init__.py": b"VALUE = 1\n", "numpy/__config__.py": b"BUILD = 'gcc-linux'\n"}
        i2 = {"numpy/__init__.py": b"VALUE = 1\n", "numpy/__config__.py": b"BUILD = 'msvc-windows'\n"}
        v2, ev2 = run6(name="numpy", version="2.4.2", installed_tag=LIN, held_tags=LIN, wheel_files=w2, installed_files=i2)
        _expect(v2, ev2, "failed", compared_across_platforms=False, py_differing=["numpy/__config__.py"],
                build_metadata_residual=[])
        assert spy["n"] == 0, "the platform rule was consulted on a same-platform numpy comparison"
    finally:
        ic._platform_rule = real_rule


def arm_e2_no_installed_wheel_tag_is_not_cross_platform():
    w, i = _init_pair(b"VALUE = 1\n", b"VALUE = 1\r\n")
    v, ev = run6(installed_tag=None, wheel_files=w, installed_files=i)
    _expect(v, ev, "failed", compared_across_platforms=False, py_differing=[SYN + "/__init__.py"], platform_normalised_equal=[])


def arm_f_scripts_data_and_oversize_keep_failing():
    for folder in ("scripts", "data"):
        member = "%s-%s.data/%s/tool.py" % (SYN, SYN_V, folder)
        w = dict(_init_pair(b"VALUE = 1\n")[0], **{member: b"X = 1\n"})
        i = dict(_init_pair(b"VALUE = 1\n")[1])
        v, ev = run6(wheel_files=w, installed_files=i)
        assert v == "failed" and member in ev["py_differing"], "%s member must keep failing across platforms: %r" % (folder, ev)
        assert ev["compared_across_platforms"] is True and ev["platform_normalised_equal"] == [], ev
    saved = ic.MAX_PY_BYTES
    try:
        ic.MAX_PY_BYTES = 4                                 # the over-size rule, lowered for this arm only
        w, i = _init_pair(b"VALUE = 1\n", b"VALUE = 1\r\n")  # CRLF-only, cross-platform, but over the size limit
        v, ev = run6(wheel_files=w, installed_files=i)
        _expect(v, ev, "failed", py_differing=[SYN + "/__init__.py"], platform_normalised_equal=[])
    finally:
        ic.MAX_PY_BYTES = saved


def arm_g_controls():
    # g1: the rule itself never clears a planted edit, and clears the three cases it should
    assert ic._platform_rule(SYN + "/mod.py", b"VALUE = 1\n", b"VALUE = 2\n") is None, "a planted edit was cleared"
    assert ic._platform_rule(SYN + "/mod.py", b"# start delvewheel patch\nA = 1\n# end delvewheel patch\nB = 2\r\n",
                             b"B = 1\n") is None, "a planted edit beside a delvewheel block was cleared"
    assert ic._platform_rule(SYN + "/x.py", b"A\r\n", b"A\n") == "equal", "CRLF-only was not cleared"
    assert ic._platform_rule("numpy/__config__.py", b"A\n", b"B\n") == "build", "the listed build-metadata file was not cleared"
    # g2: a mutant rule that clears everything makes the planted-edit arm fail, so the arm has teeth
    real_rule = ic._platform_rule
    ic._platform_rule = lambda rel, h, i: "equal"
    try:
        w, i = _init_pair(b"VALUE = 2\n", b"VALUE = 1\n")
        v, ev = run6(wheel_files=w, installed_files=i)
        assert v == "passed", "the mutant was expected to pass the planted edit (the arm's teeth): %r" % (v,)
    finally:
        ic._platform_rule = real_rule
    # g3: the constant holds exactly one entry, the numpy build-metadata file
    assert ic.CHECK6_BUILD_METADATA_FILES == ("numpy/__config__.py",), ic.CHECK6_BUILD_METADATA_FILES


ARMS = [arm_a_crlf_only_cross_platform_passes, arm_b_delvewheel_block_cross_platform_passes,
        arm_c_numpy_build_metadata_file_passes_and_other_file_fails, arm_d_planted_edit_fails_across_platforms,
        arm_e_same_platform_is_unchanged, arm_e2_no_installed_wheel_tag_is_not_cross_platform,
        arm_f_scripts_data_and_oversize_keep_failing, arm_g_controls]


def run_arms():
    ok_count = 0
    for fn in ARMS:
        try:
            fn()
            ok_count += 1
            print("PASS %s" % fn.__name__)
        except Exception as exc:  # an arm that raises is a failed arm
            print("FAIL %s: %s: %s" % (fn.__name__, type(exc).__name__, exc))
            traceback.print_exc(file=sys.stdout)
    n = len(ARMS)
    ok = ok_count == n
    print("CHECK6-PLATFORM arms=%d/%d ok=%s" % (ok_count, n, ok))
    return 0 if ok else 1


# ------------------------------------------------------------------------------------------------------------ --real4
def _real_wheel(name):
    hits = sorted(p for p in RELEASE.iterdir() if p.name.startswith(name + "-") and p.name.endswith(".whl"))
    return hits


def real4(out=None):
    """READ ONLY. For each of the four real wheels: the fetch record is read as run_check reads it, the context is built in
    memory, check_3 then check_6 run. Nothing is written: no record, no copy, no sidecar."""
    out = out or sys.stdout
    if not RELEASE.is_dir():
        print("REAL4 SKIPPED folder absent", file=out)
        return 2
    batch = RELEASE.name
    cfg = ic.Cfg()
    passed = 0
    for name in REAL_NAMES:
        hits = _real_wheel(name)
        if len(hits) != 1:
            print("REAL4 %s check6=unresolved compared_across_platforms=None residual=None metadata=None (%d wheels named)"
                  % (name, len(hits)), file=out)
            continue
        whl = hits[0]
        fetch, _ = ic.read_fetch_record(cfg, batch, whl.name)
        ctx = {"cfg": cfg, "batch": batch, "file_name": whl.name, "path": whl, "fetch": fetch or {},
               "approved_by": None, "signed_by": None, "min_age": 14.0, "min_earlier": 3, "scan_wait": 0, "wait_hook": None}
        ic.check_3(ctx)
        verdict, ev = ic.check_6(ctx)
        if verdict == "passed":
            passed += 1
        print("REAL4 %s check6=%s compared_across_platforms=%s residual=%s metadata=%d" % (
            name, verdict, ev.get("compared_across_platforms"), ev.get("py_differing_after_platform_rules"),
            len(ev.get("build_metadata_residual") or [])), file=out)
    ok = passed == len(REAL_NAMES)
    print("REAL4 passed=%d/%d ok=%s" % (passed, len(REAL_NAMES), ok), file=out)
    return 0 if ok else 1


if __name__ == "__main__":
    if "--real4" in sys.argv[1:]:
        sys.exit(real4())
    sys.exit(run_arms())
