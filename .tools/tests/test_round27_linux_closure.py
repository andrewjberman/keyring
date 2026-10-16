#!/usr/bin/env python3
"""test_round27_linux_closure.py -- NFRA_CTLPLN round 27, cell CT-ar-1 (ruling XB-983c): the linux x86_64 target of the
closure tool, its host-aware form, and the unchanged Windows closure.

NO NETWORK. Synthetic installed distributions in a temporary directory, the packaging library, and the two tools at their
own paths in this worktree. Nothing is fetched, installed or written outside a temporary folder.

Arms:
  1  supported_tags for cp312-linux_x86_64 holds (cp312,cp312,manylinux2014_x86_64) and (py3,none,any) and no win_amd64 triple
  2  linux_x86_64_platforms() equals packaging's own manylinux enumeration for glibc 2.34 (packaging reads the running
     host, so its glibc and ELF probe are pinned to 2.34 for this arm only); the Windows supported set is unchanged
  3  markers: sys_platform == "win32" excluded and == "linux" included for the linux target; the reverse for cp314-win_amd64
     (control); the linux target's python_full_version is 3.12.14
  4  host logic on a SYNTHETIC host file and synthetic parents: a satisfied pin is HOST-SATISFIED, an unsatisfied pin is
     HOST-CONFLICT, and the last line carries host_satisfied / host_conflicts / to_fetch
  5  CONTROL: closure --from-file closure_cp314_win_amd64.json prints the last line stored in that file
  6  the saved yfinance closure: root yfinance, one host class per member, to_fetch = closure minus host-satisfied
  7  the Windows target sets are byte-identical to packaging.tags called as the tool called them before the change

LAST line: LINUX-CLOSURE arms=<k>/<n> ok=<True|False>
Run: python .tools/tests/test_round27_linux_closure.py   (exit 0 = every arm PASS)
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import pathlib
import sys
import tempfile
import traceback

HERE = pathlib.Path(__file__).resolve()
REPO = HERE.parents[2]
INTAKE = REPO / "org" / "devices" / "intake"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


ic = _load("intake_closure", INTAKE / "intake_closure.py")
kw = ic.kw
from packaging import tags as ptags  # noqa: E402
from packaging import _manylinux as pml  # noqa: E402

LINUX = ic.make_target("cp312-linux_x86_64")
LINUX_SUPPORTED = kw.supported_tags(LINUX)
WIN314 = ic.make_target("cp314-win_amd64")
WIN314_SUPPORTED = kw.supported_tags(WIN314)
SAVED = INTAKE / "closure_cp312_linux_x86_64_yfinance.json"
HOST_FILE = INTAKE / "records" / "intake-20261016-yfinance-linux" / "HOST_PYDEPS.json"


def make_dist(site, name, version, requires=(), tags=("py3-none-any",), purelib=True):
    """Write <site>/<name>-<version>.dist-info with METADATA, WHEEL and RECORD (synthetic)."""
    site = pathlib.Path(site)
    di = site / ("%s-%s.dist-info" % (name.replace("-", "_"), version))
    di.mkdir(parents=True, exist_ok=True)
    meta = "Metadata-Version: 2.1\nName: %s\nVersion: %s\n" % (name, version)
    meta += "".join("Requires-Dist: %s\n" % r for r in requires)
    (di / "METADATA").write_text(meta, encoding="ascii")
    wheel = "Wheel-Version: 1.0\nGenerator: test\nRoot-Is-Purelib: %s\n" % ("true" if purelib else "false")
    wheel += "".join("Tag: %s\n" % t for t in tags)
    (di / "WHEEL").write_text(wheel, encoding="ascii")
    (di / "RECORD").write_text("%s/RECORD,,\n" % di.name, encoding="ascii")
    return di


def arm1_linux_tags(tmp):
    need = ("cp312", "cp312", "manylinux2014_x86_64")
    assert need in LINUX_SUPPORTED, need
    assert ("py3", "none", "any") in LINUX_SUPPORTED
    wins = [t for t in LINUX_SUPPORTED if "win" in t[2]]
    assert wins == [], wins[:3]
    assert all(t[2].endswith("x86_64") or t[2] == "any" for t in LINUX_SUPPORTED), "a non-x86_64 platform leaked"
    assert not any(t[2].startswith("musllinux") for t in LINUX_SUPPORTED)
    fits = sorted({t[2] for t in LINUX_SUPPORTED if t[2] != "any"})
    return "%d supported triples; manylinux2014_x86_64 and (py3,none,any) present; 0 win triples; platforms %s..%s" % (
        len(LINUX_SUPPORTED), fits[0], fits[-1])


def arm2_packaging_agreement(tmp):
    """packaging's own enumeration for glibc 2.34, with the running-host probes pinned (restored in finally)."""
    saved_glibc, saved_abi = pml._get_glibc_version, pml._have_compatible_abi
    try:
        pml._get_glibc_version = lambda: (2, 34)
        pml._have_compatible_abi = lambda executable, archs: True
        theirs = list(pml.platform_tags(["x86_64"]))
    finally:
        pml._get_glibc_version, pml._have_compatible_abi = saved_glibc, saved_abi
    ours = kw.linux_x86_64_platforms((2, 34))
    assert ours == theirs, (ours[:4], theirs[:4], len(ours), len(theirs))
    for want in ("manylinux_2_5_x86_64", "manylinux1_x86_64", "manylinux2010_x86_64", "manylinux2014_x86_64",
                 "manylinux_2_17_x86_64", "manylinux_2_28_x86_64", "manylinux_2_34_x86_64"):
        assert want in ours, want
    # the Windows target still goes to packaging.tags as the label itself (the same call as before the change)
    direct = set()
    for t in ptags.cpython_tags(python_version=(3, 14), abis=["cp314"], platforms=["win_amd64"]):
        direct.add((t.interpreter, t.abi, t.platform))
    for t in ptags.compatible_tags(python_version=(3, 14), interpreter="cp314", platforms=["win_amd64"]):
        direct.add((t.interpreter, t.abi, t.platform))
    assert direct == WIN314_SUPPORTED, (len(direct), len(WIN314_SUPPORTED))
    return ("%d manylinux platform strings for glibc 2.34 equal packaging's own list in order; "
            "cp314-win_amd64 supported set = %d triples, identical to the direct packaging call" % (len(ours), len(direct)))


def arm3_markers(tmp):
    site = tmp / "a3"
    site.mkdir()
    win_only = kw.parse_requirement('wx; sys_platform == "win32"', LINUX)
    linux_only = kw.parse_requirement('lx; sys_platform == "linux"', LINUX)
    assert win_only["ok"] and win_only["applicable"] is False, win_only
    assert linux_only["ok"] and linux_only["applicable"] is True, linux_only
    win_on_win = kw.parse_requirement('wx; sys_platform == "win32"', WIN314)
    lin_on_win = kw.parse_requirement('lx; sys_platform == "linux"', WIN314)
    assert win_on_win["applicable"] is True and lin_on_win["applicable"] is False, (win_on_win, lin_on_win)
    env = LINUX["env"]
    assert (env["python_full_version"], env["implementation_version"], env["sys_platform"], env["os_name"],
            env["platform_machine"], env["platform_system"], env["python_version"]) == \
        ("3.12.14", "3.12.14", "linux", "posix", "x86_64", "Linux", "3.12"), env
    assert ic.make_target("cp312-win_amd64")["env"]["python_full_version"] == "3.12.0"
    return "linux: win32 excluded, linux included; win314 control reversed; linux env 3.12.14 / linux / posix / x86_64"


def arm4_host_logic(tmp):
    site = tmp / "a4"
    make_dist(site, "alpha", "1.0", ["beta>=1.0"])
    make_dist(site, "beta", "1.5", ["gamma<2"])
    make_dist(site, "gamma", "1.5")
    host = tmp / "a4_host.json"
    host.write_text(json.dumps({"schema": "intake-host-pydeps/1", "host": "synthetic", "python": "3.12.14",
                                "dists": {"beta": "1.2", "gamma": "2.0"}}), encoding="ascii")
    out = tmp / "a4_closure.json"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = ic.main(["closure", "--target", "cp312-linux_x86_64", "--root", "alpha==1.0", "--site-packages", str(site),
                      "--host-pydeps", str(host), "--out", str(out)])
    text = buf.getvalue()
    last = text.strip().splitlines()[-1]
    want = ("INTAKE-CLOSURE target=cp312-linux_x86_64 lines=1 closure=3 dependencies_added=2 pure=3 fits=0 needs_fetch=0 "
            "unknown_not_installed=0 specifier_conflicts=0 fixed_point=True ok=True host_satisfied=1 host_conflicts=1 "
            "to_fetch=2")
    assert rc == 0 and last == want, last
    assert "HOST-SATISFIED beta closure=1.5 host=1.2" in text, text
    assert "HOST-CONFLICT gamma host=2.0 closure=1.5 unmet_by=beta <2 STOP" in text, text
    data = json.loads(out.read_text(encoding="ascii"))
    assert data["requirements_file"]["name"] == "<--root>" and data["requirements_file"]["form"] == "root"
    assert [m["name"] for m in data["members"] if m["kind"] == "line"] == ["alpha"]
    assert data["host"]["to_fetch"] == ["alpha", "gamma"], data["host"]["to_fetch"]
    assert str(tmp) not in out.read_text(encoding="ascii"), "a temporary path was baked into the saved file"
    # the same run a second time gives the same last line (determinism)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        ic.main(["closure", "--target", "cp312-linux_x86_64", "--root", "alpha==1.0", "--site-packages", str(site),
                 "--host-pydeps", str(host), "--out", str(out)])
    assert buf.getvalue().strip().splitlines()[-1] == want
    return "beta 1.2 satisfies >=1.0 (SATISFIED); gamma 2.0 breaks <2 (CONFLICT); last line %s" % want.split(" ")[-3:]


def arm5_control(tmp):
    stored = json.loads((INTAKE / "closure_cp314_win_amd64.json").read_text(encoding="utf-8"))["last_line"]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = ic.main(["closure", "--from-file", str(INTAKE / "closure_cp314_win_amd64.json")])
    printed = buf.getvalue().strip().splitlines()[-1]
    assert rc == 0 and printed == stored, (printed, stored)
    assert "host_satisfied" not in printed, printed
    return "re-printed == stored: %s" % printed


def arm6_saved_yfinance(tmp):
    data = json.loads(SAVED.read_text(encoding="ascii"))
    assert data["target"]["label"] == "cp312-linux_x86_64" and data["running_python"].startswith("3.12")
    lines = [m for m in data["members"] if m["kind"] == "line"]
    assert [m["name"] for m in lines] == ["yfinance"] and lines[0]["line"] == "yfinance==1.2.0", lines
    assert data["requirements_file"]["name"] == "<--root>"
    h = data["host"]
    classes = {}
    for m in data["members"]:
        assert m.get("host_class") in ("HOST-SATISFIED", "HOST-CONFLICT", None), m.get("host_class")
        classes[m["norm"]] = m["host_class"]
    sat = [r["norm"] for r in h["satisfied"]]
    conf = [r["norm"] for r in h["conflicts"]]
    assert set(sat) == {k for k, v in classes.items() if v == "HOST-SATISFIED"}
    assert set(conf) == {k for k, v in classes.items() if v == "HOST-CONFLICT"}
    assert not (set(sat) & set(conf)), "a member classed both ways"
    assert len(h["to_fetch"]) == len(data["members"]) - len(sat), (len(h["to_fetch"]), len(data["members"]), len(sat))
    assert data["last_line"].endswith("host_satisfied=%d host_conflicts=%d to_fetch=%d"
                                      % (len(sat), len(conf), len(h["to_fetch"]))), data["last_line"]
    line, ok = ic.last_line(data)
    assert line == data["last_line"] and ok is True, line
    return ("%s; members=%d host_satisfied=%d host_conflicts=%d to_fetch=%d; conflicts=%s"
            % (line, len(data["members"]), len(sat), len(conf), len(h["to_fetch"]), conf or "none"))


def arm7_windows_unchanged(tmp):
    # the cp312 Windows target: the same set as before the change (packaging called with the label as the platform)
    direct = set()
    for t in ptags.cpython_tags(python_version=(3, 12), abis=["cp312"], platforms=["win_amd64"]):
        direct.add((t.interpreter, t.abi, t.platform))
    for t in ptags.compatible_tags(python_version=(3, 12), interpreter="cp312", platforms=["win_amd64"]):
        direct.add((t.interpreter, t.abi, t.platform))
    got = kw.supported_tags(ic.make_target("cp312-win_amd64"))
    assert got == direct, (len(got), len(direct))
    return "cp312-win_amd64 supported set = %d triples, identical to the direct packaging call" % len(got)


ARMS = [("linux target tags: manylinux2014 and any in, win out", arm1_linux_tags),
        ("manylinux list equals packaging's own for glibc 2.34; Windows set unchanged", arm2_packaging_agreement),
        ("markers follow the target; linux python_full_version 3.12.14", arm3_markers),
        ("host logic on a synthetic host file: SATISFIED and CONFLICT, last line fields", arm4_host_logic),
        ("CONTROL: the stored Windows closure re-prints its stored last line", arm5_control),
        ("the saved yfinance closure: one host class per member, to_fetch = closure minus satisfied", arm6_saved_yfinance),
        ("the cp312 Windows set is identical to the direct packaging call", arm7_windows_unchanged)]


def main():
    passed = 0
    with tempfile.TemporaryDirectory(prefix="round27-linux-closure-") as td:
        tmp = pathlib.Path(td)
        for i, (title, fn) in enumerate(ARMS, 1):
            try:
                detail = fn(tmp)
                passed += 1
                print("PASS arm %d: %s -- %s" % (i, title, ic.asc(detail)))
            except Exception as exc:  # noqa: BLE001 - a failing arm is reported, never raised
                print("FAIL arm %d: %s -- %s: %s" % (i, title, type(exc).__name__, ic.asc(exc)[:400]))
                traceback.print_exc(limit=4, file=sys.stdout)
    ok = passed == len(ARMS)
    print("LINUX-CLOSURE arms=%d/%d ok=%s" % (passed, len(ARMS), ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
