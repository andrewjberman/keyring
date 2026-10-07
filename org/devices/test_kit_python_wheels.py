"""test_kit_python_wheels.py -- kit_python_wheels.py on synthetic fixtures (tiny hand-made wheel archives and dist-info folders).

No real package, no network, no pip call beyond the read-only allow-list. Seven cases; LAST line
PY-WHEELS-TEST cases=<k>/7 ok=<True|False>
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys
import tempfile
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("kit_python_wheels", HERE / "kit_python_wheels.py")
kw = importlib.util.module_from_spec(spec)
sys.modules["kit_python_wheels"] = kw
spec.loader.exec_module(kw)


def make_wheel(folder, dist, version, tag, purelib=True, requires=()):
    """A tiny hand-made wheel archive: only the dist-info members, no code."""
    folder = pathlib.Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / ("%s-%s-%s.whl" % (dist, version, tag))
    meta = "Metadata-Version: 2.1\nName: %s\nVersion: %s\n" % (dist, version)
    for r in requires:
        meta += "Requires-Dist: %s\n" % r
    wheel = "Wheel-Version: 1.0\nGenerator: synthetic\nRoot-Is-Purelib: %s\n" % ("true" if purelib else "false")
    wheel += "Tag: %s\n" % tag
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("%s-%s.dist-info/METADATA" % (dist, version), meta)
        zf.writestr("%s-%s.dist-info/WHEEL" % (dist, version), wheel)
        zf.writestr("%s-%s.dist-info/RECORD" % (dist, version), "")
    return path


def make_installed(sp, dist, version, tag, purelib=True, requires=(), record=True, wheel_file=True):
    d = pathlib.Path(sp) / ("%s-%s.dist-info" % (dist, version))
    d.mkdir(parents=True, exist_ok=True)
    meta = "Metadata-Version: 2.1\nName: %s\nVersion: %s\n" % (dist, version)
    for r in requires:
        meta += "Requires-Dist: %s\n" % r
    (d / "METADATA").write_text(meta, encoding="ascii")
    if wheel_file:
        (d / "WHEEL").write_text("Wheel-Version: 1.0\nRoot-Is-Purelib: %s\nTag: %s\n" % ("true" if purelib else "false", tag),
                                 encoding="ascii")
    if record:
        (d / "RECORD").write_text("", encoding="ascii")
    return d


def run_core(tmp, lines, wheels=(), installed=()):
    target = kw.parse_target("cp314", "win_amd64")
    supported = kw.supported_tags(target)
    roots = kw.Roots()
    roots.add("<fixture>", tmp)
    winfos, _u, _n = kw.scan_wheel_files([str(w) for w in wheels])
    inst = []
    for sp in installed:
        dists, _ = kw.scan_site_packages(str(sp))
        inst.extend(("<fixture-site>", d) for d in dists)
    entries, und = kw.classify_all([(i + 1, t) for i, t in enumerate(lines)], winfos, inst, target, roots, supported)
    return entries, und, roots


def case1(tmp):
    """a py3-none-any wheel fits (as a file); an installed pure copy is PURE-INSTALLED and prints its undeclared dependency."""
    w = make_wheel(tmp / "w1", "purepkg", "1.0", "py3-none-any")
    sp = tmp / "sp1"
    make_installed(sp, "installedpure", "2.0", "py3-none-any", requires=["extradep>=1", 'winonly; sys_platform == "linux"'])
    entries, und, _ = run_core(tmp, ["purepkg==1.0", "installedpure>=1.5", "extradep"], [w], [sp])
    by = {e["name"]: e for e in entries}
    ok = (by["purepkg"]["class"] == "WHEEL-ON-DISK" and by["installedpure"]["class"] == "PURE-INSTALLED"
          and by["installedpure"]["satisfies"] is True and by["extradep"]["class"] == "NEEDS-FETCH"
          and by["installedpure"]["undeclared_deps"] == [])
    # extradep is a line of the requirements, so it is not undeclared; the linux-only marker is evaluated for the target
    return ok, "%s/%s/%s" % (by["purepkg"]["class"], by["installedpure"]["class"], by["extradep"]["class"])


def case2(tmp):
    """a cp312-cp312-win_amd64 wheel does NOT fit; an installed cp312 build is NEEDS-FETCH 'compiled for another Python'."""
    w = make_wheel(tmp / "w2", "comp312", "1.0", "cp312-cp312-win_amd64", purelib=False)
    sp = tmp / "sp2"
    make_installed(sp, "inst312", "1.0", "cp312-cp312-win_amd64", purelib=False)
    entries, _und, _ = run_core(tmp, ["comp312", "inst312"], [w], [sp])
    by = {e["name"]: e for e in entries}
    ok = (by["comp312"]["class"] == "NEEDS-FETCH" and by["inst312"]["class"] == "NEEDS-FETCH"
          and "another Python" in (by["inst312"]["reason"] or ""))
    ok = ok and by["comp312"]["other_copies"] and by["comp312"]["other_copies"][0]["class"] == "wheel-not-fitting"
    return bool(ok), "%s/%s" % (by["comp312"]["class"], by["inst312"]["class"])


def case3(tmp):
    """a cp39-abi3-win_amd64 wheel fits (file); an installed abi3 build is ABI3-INSTALLED."""
    w = make_wheel(tmp / "w3", "abi3pkg", "1.0", "cp39-abi3-win_amd64", purelib=False)
    sp = tmp / "sp3"
    make_installed(sp, "abi3inst", "1.0", "cp310-abi3-win_amd64", purelib=False)
    entries, _und, _ = run_core(tmp, ["abi3pkg", "abi3inst"], [w], [sp])
    by = {e["name"]: e for e in entries}
    ok = by["abi3pkg"]["class"] == "WHEEL-ON-DISK" and by["abi3inst"]["class"] == "ABI3-INSTALLED"
    return ok, "%s/%s" % (by["abi3pkg"]["class"], by["abi3inst"]["class"])


def case4(tmp):
    """a cp314-cp314-win_amd64 wheel fits; a cp315-abi3 wheel (newer than the target) does not."""
    w = make_wheel(tmp / "w4", "native314", "1.0", "cp314-cp314-win_amd64", purelib=False)
    w2 = make_wheel(tmp / "w4", "future315", "1.0", "cp315-abi3-win_amd64", purelib=False)
    entries, _und, _ = run_core(tmp, ["native314", "future315"], [w, w2])
    by = {e["name"]: e for e in entries}
    ok = by["native314"]["class"] == "WHEEL-ON-DISK" and by["future315"]["class"] == "NEEDS-FETCH"
    return ok, "%s/%s" % (by["native314"]["class"], by["future315"]["class"])


def case5(tmp):
    """a cp314-cp314-manylinux wheel does not fit; an installed copy with no WHEEL file is NEEDS-FETCH 'no wheel metadata'."""
    w = make_wheel(tmp / "w5", "linuxpkg", "1.0", "cp314-cp314-manylinux_2_17_x86_64", purelib=False)
    sp = tmp / "sp5"
    make_installed(sp, "nometa", "1.0", "py3-none-any", wheel_file=False)
    entries, _und, _ = run_core(tmp, ["linuxpkg", "nometa"], [w], [sp])
    by = {e["name"]: e for e in entries}
    ok = (by["linuxpkg"]["class"] == "NEEDS-FETCH" and by["nometa"]["class"] == "NEEDS-FETCH"
          and by["nometa"]["reason"] == "no wheel metadata")
    return ok, "%s/%s (%s)" % (by["linuxpkg"]["class"], by["nometa"]["class"], by["nometa"]["reason"])


def case6(tmp):
    """a requirement whose marker excludes Windows is NOT-APPLICABLE, with the marker printed; one that includes it is not."""
    w = make_wheel(tmp / "w6", "winpkg", "1.0", "py3-none-any")
    entries, _und, _ = run_core(tmp, ['linuxonly==1; sys_platform == "linux"', 'winpkg; sys_platform == "win32"',
                                     'oldpy; python_version < "3.13"'], [w])
    by = {e["name"]: e for e in entries}
    ok = (by["linuxonly"]["class"] == "NOT-APPLICABLE" and "linux" in by["linuxonly"]["reason"]
          and by["winpkg"]["class"] == "WHEEL-ON-DISK" and by["oldpy"]["class"] == "NOT-APPLICABLE")
    return ok, "%s/%s/%s" % (by["linuxonly"]["class"], by["winpkg"]["class"], by["oldpy"]["class"])


def case7(tmp):
    """an unparseable line is counted (UNPARSED), the last line says unparsed=1 ok=False, and every pip command is allow-listed."""
    entries, und, _ = run_core(tmp, ["good-pkg", "this is !! not a requirement"])
    ll, ok_flag = kw.last_line("cp314-win_amd64", entries, und)
    pip_ok = all(tuple(a for a in cmd[3:]) in kw.PIP_ALLOWED for cmd in kw.PIP_LOG)
    kw.run_pip(["--version"])
    pip_ok = pip_ok and all(tuple(cmd[3:]) in kw.PIP_ALLOWED for cmd in kw.PIP_LOG)
    refused = False
    try:
        kw.run_pip(["install", "x"])
    except SystemExit:
        refused = True
    cls = [e["class"] for e in entries]
    ok = cls == ["NEEDS-FETCH", "UNPARSED"] and "unparsed=1" in ll and ok_flag is False and pip_ok and refused
    return ok, "%s | %s | pip install refused=%s" % (cls, ll[-40:], refused)


def main():
    cases = [case1, case2, case3, case4, case5, case6, case7]
    passed = 0
    with tempfile.TemporaryDirectory() as td:
        tmp = pathlib.Path(td)
        for i, fn in enumerate(cases, 1):
            try:
                ok, detail = fn(tmp)
            except Exception as exc:  # noqa: BLE001 - a case that raises is a failed case, printed
                ok, detail = False, "EXCEPTION %s: %s" % (type(exc).__name__, exc)
            passed += 1 if ok else 0
            print("case %d %s: %s" % (i, "PASS" if ok else "FAIL", fn.__doc__.strip().splitlines()[0][:100]))
            print("   " + str(detail).encode("ascii", "replace").decode("ascii"))
    ok = passed == len(cases)
    print("PY-WHEELS-TEST cases=%d/7 ok=%s" % (passed, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
