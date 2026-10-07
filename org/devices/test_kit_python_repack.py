"""test_kit_python_repack.py -- tests for org/devices/kit_python_repack.py on SYNTHETIC distributions in a temporary
site-packages (hand-made, tiny: no real package is read, nothing is fetched, nothing is installed in this machine's
environment). The one pip run (case 6) is `--no-index --no-deps --target <temporary directory>` of wheels the test made.

LAST line: PY-REPACK-TEST cases=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import base64
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import pathlib
import subprocess
import sys
import tempfile
import traceback
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("kit_python_repack", HERE / "kit_python_repack.py")
kr = importlib.util.module_from_spec(spec)
sys.modules["kit_python_repack"] = kr
spec.loader.exec_module(kr)

LABEL = "<site-packages:3.12>"


def b64sha(data):
    return base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b"=").decode()


def make_dist(base, name, version, files, tags=("py3-none-any",), entry_points=None, outside=None, extra_record=None,
              purelib=True):
    """Write a distribution into <base>/Lib/site-packages (and <base>/Scripts etc. for `outside`, a dict of
    '../../<rel>' -> bytes). RECORD is written correct. Returns (site, dist_info_name)."""
    site = pathlib.Path(base, "Lib", "site-packages")
    site.mkdir(parents=True, exist_ok=True)
    prefix = "%s-%s" % (name.replace("-", "_"), version)
    di = site / (prefix + ".dist-info")
    di.mkdir(exist_ok=True)
    rows = []
    allfiles = dict(files)
    for rel, data in allfiles.items():
        p = site / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        rows.append((rel, "sha256=" + b64sha(data), str(len(data))))
    for rel, data in (outside or {}).items():
        p = pathlib.Path(os.path.normpath(site / rel))
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        rows.append((rel, "sha256=" + b64sha(data), str(len(data))))
    meta = "Metadata-Version: 2.1\nName: %s\nVersion: %s\n" % (name, version)
    wheel = "Wheel-Version: 1.0\nGenerator: test\nRoot-Is-Purelib: %s\n" % ("true" if purelib else "false")
    wheel += "".join("Tag: %s\n" % t for t in tags)
    dist_files = {"METADATA": meta.encode(), "WHEEL": wheel.encode(), "INSTALLER": b"pip\n", "REQUESTED": b""}
    if entry_points:
        dist_files["entry_points.txt"] = entry_points.encode()
    for fn, data in dist_files.items():
        (di / fn).write_bytes(data)
        rows.append(("%s/%s" % (di.name, fn), "sha256=" + b64sha(data), str(len(data))))
    for extra in extra_record or []:
        rows.append(extra)
    rows.append((di.name + "/RECORD", "", ""))
    (di / "RECORD").write_text(kr.record_text([(r[0], r[1].replace("sha256=", ""), r[2]) for r in rows]), encoding="utf-8")
    return str(site), di.name


def classification(path, entries, extra_target=None):
    reqs = []
    for name, version, di_name, klass in entries:
        reqs.append({"name": name, "specifier": "==" + version, "class": klass, "evidence": "%s/%s" % (LABEL, di_name),
                     "found_version": version, "line": "%s==%s" % (name, version), "tags": []})
    doc = {"target": {"python_tag": "cp314", "platform": "win_amd64"}, "requirements": reqs,
           "requirements_file": {"sha256": "x"}}
    pathlib.Path(path).write_text(json.dumps(doc), encoding="utf-8")
    return str(path)


def run_repack(out, cls, site):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = kr.main(["repack", "--out", str(out), "--from-file", str(cls), "--root", "%s=%s" % (LABEL, site)])
    text = buf.getvalue()
    last = [ln for ln in text.splitlines() if ln.startswith("PY-REPACK ")][-1]
    return rc, text, last


def field(line, key):
    for part in line.split():
        if part.startswith(key + "="):
            return part.split("=", 1)[1]
    return None


def case1_pure_repack(tmp):
    base = tmp / "c1"
    site, di = make_dist(base, "Kit-Syn.One", "1.0", {"kitsynone/__init__.py": b"X = 1\n", "kitsynone/data.txt": b"hi\n"})
    cls = classification(tmp / "c1.json", [("Kit-Syn.One", "1.0", di, "PURE-INSTALLED")])
    rc, text, last = run_repack(tmp / "c1out", cls, site)
    wheel = tmp / "c1out" / "kit_syn_one-1.0-py3-none-any.whl"
    assert rc == 0 and field(last, "built") == "1" and field(last, "verified") == "1" and last.endswith("ok=True"), last
    assert wheel.is_file(), "wheel not named from the normalised name: " + str(sorted(os.listdir(tmp / "c1out")))
    sys.path.insert(0, str(HERE))
    kpw, target, supported = kr.tag_support("cp314", "win_amd64")
    probs, facts = kr.verify_wheel(wheel, supported, kpw)
    assert probs == [], probs
    assert facts["top_level"] == ["kitsynone"], facts
    names = zipfile.ZipFile(wheel).namelist()
    assert not any(n.endswith(("INSTALLER", "REQUESTED", "direct_url.json")) for n in names), names
    assert kit_req(tmp / "c1out") == ["Kit-Syn.One==1.0"]
    return last


def kit_req(folder):
    return [ln for ln in pathlib.Path(folder, "requirements-kit.txt").read_text().splitlines() if ln.strip()]


def case2_modified_left_out(tmp):
    base = tmp / "c2"
    site, di1 = make_dist(base, "modone", "1.0", {"modone/__init__.py": b"A = 1\n", "modone/b.py": b"B = 2\n"})
    _s, di2 = make_dist(base, "gonetwo", "2.0", {"gonetwo/__init__.py": b"A = 1\n", "gonetwo/c.py": b"C = 3\n"})
    _s, di3 = make_dist(base, "fine", "3.0", {"fine/__init__.py": b"A = 1\n"})
    pathlib.Path(site, "modone", "b.py").write_bytes(b"B = 'locally edited'\n")
    os.remove(pathlib.Path(site, "gonetwo", "c.py"))
    cls = classification(tmp / "c2.json", [("modone", "1.0", di1, "PURE-INSTALLED"), ("gonetwo", "2.0", di2, "PURE-INSTALLED"),
                                           ("fine", "3.0", di3, "PURE-INSTALLED")])
    rc, text, last = run_repack(tmp / "c2out", cls, site)
    assert field(last, "modified") == "2" and field(last, "built") == "1" and last.endswith("ok=True"), last
    assert sorted(os.listdir(tmp / "c2out")) == ["MANIFEST.json", "fine-3.0-py3-none-any.whl", "requirements-kit.txt"]
    man = json.loads((tmp / "c2out" / "MANIFEST.json").read_text())
    by = {r["name"]: r for r in man["left_out"]}
    assert by["modone"]["status"] == "MODIFIED" and "modone/b.py" in by["modone"]["problems"][0], by
    assert "gonetwo/c.py" in by["gonetwo"]["problems"][0] and "missing" in by["gonetwo"]["problems"][0], by
    assert "modone==1.0" not in kit_req(tmp / "c2out")
    return last


def case3_pyc_never_packed(tmp):
    base = tmp / "c3"
    pyc = b"\x00\x01compiled"
    site, di = make_dist(base, "pycone", "1.0", {"pycone/__init__.py": b"A = 1\n", "pycone/__pycache__/x.cpython-312.pyc": pyc,
                                                  "pycone/stray.pyc": pyc})
    pathlib.Path(site, "pycone", "__pycache__", "y.cpython-312.pyc").write_bytes(pyc)  # on disk, not in RECORD
    cls = classification(tmp / "c3.json", [("pycone", "1.0", di, "PURE-INSTALLED")])
    rc, text, last = run_repack(tmp / "c3out", cls, site)
    assert last.endswith("ok=True") and field(last, "built") == "1", last
    names = zipfile.ZipFile(tmp / "c3out" / "pycone-1.0-py3-none-any.whl").namelist()
    assert not [n for n in names if n.endswith(".pyc") or "__pycache__" in n], names
    return last


def case4_record_regenerated(tmp):
    base = tmp / "c4"
    site, di = make_dist(base, "recone", "1.0", {"recone/__init__.py": b"A = 1\n", "recone/big.bin": os.urandom(300000),
                                                 "recone/with,comma.txt": b"comma\n"})
    cls = classification(tmp / "c4.json", [("recone", "1.0", di, "PURE-INSTALLED")])
    rc, text, last = run_repack(tmp / "c4out", cls, site)
    assert last.endswith("ok=True"), last
    wheel = tmp / "c4out" / "recone-1.0-py3-none-any.whl"
    with zipfile.ZipFile(wheel) as zf:
        rec = {}
        import csv
        for row in csv.reader(io.StringIO(zf.read("recone-1.0.dist-info/RECORD").decode(), newline="")):
            rec[row[0]] = row[1:]
        assert rec["recone-1.0.dist-info/RECORD"] == ["", ""], rec["recone-1.0.dist-info/RECORD"]
        checked = 0
        for n in zf.namelist():
            if n.endswith("/RECORD"):
                continue
            data = zf.read(n)
            assert rec[n] == ["sha256=" + b64sha(data), str(len(data))], n
            assert "=" not in rec[n][0].split("=", 1)[1], "padding present"
            checked += 1
        assert checked == len(rec) - 1 and "recone/with,comma.txt" in rec
        for info in zf.infolist():
            assert info.date_time == (1980, 1, 1, 0, 0, 0) and info.compress_type == zipfile.ZIP_DEFLATED, info
    return "RECORD rows checked=%d" % checked


def case5_verify_refuses_tamper_and_stray(tmp):
    base = tmp / "c5"
    site, di = make_dist(base, "verone", "1.0", {"verone/__init__.py": b"A = 1\n" * 500})
    cls = classification(tmp / "c5.json", [("verone", "1.0", di, "PURE-INSTALLED")])
    out = tmp / "c5out"
    run_repack(out, cls, site)

    def verify_line():
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = kr.main(["verify", "--from", str(out)])
        return rc, buf.getvalue().strip().splitlines()[-1]

    rc, line = verify_line()
    assert rc == 0 and line == "PY-KIT-VERIFY wheels=1 verified=1 stray=0 ok=True", line
    wheel = out / "verone-1.0-py3-none-any.whl"
    raw = bytearray(wheel.read_bytes())
    raw[len(raw) // 2] ^= 0x01
    wheel.write_bytes(bytes(raw))
    rc, line = verify_line()
    assert rc == 1 and line.endswith("ok=False") and "verified=0" in line, line
    man = json.loads((out / "MANIFEST.json").read_text())
    raw[len(raw) // 2] ^= 0x01
    wheel.write_bytes(bytes(raw))
    rc, line = verify_line()
    assert rc == 0, line
    (out / "stray.txt").write_text("not in the manifest")
    rc, line = verify_line()
    assert rc == 1 and "stray=1" in line and line.endswith("ok=False"), line
    assert man["wheels"][0]["file"] == wheel.name
    return line


def case6_install_check(tmp):
    base = tmp / "c6"
    site, di1 = make_dist(base, "kitsynone", "1.0", {"kitsynone/__init__.py": b"VALUE = 1\n"})
    _s, di2 = make_dist(base, "kit-syn-two", "2.1", {"kitsyntwo.py": b"VALUE = 2\n"})
    _s, di3 = make_dist(base, "kitsynthree", "0.3", {"kitsynthree/__init__.py": b"import kit_absent_module_zz9\n"})
    cls = classification(tmp / "c6.json", [("kitsynone", "1.0", di1, "PURE-INSTALLED"),
                                           ("kit-syn-two", "2.1", di2, "PURE-INSTALLED"),
                                           ("kitsynthree", "0.3", di3, "PURE-INSTALLED")])
    out = tmp / "c6out"
    rc, text, last = run_repack(out, cls, site)
    assert last.endswith("ok=True") and field(last, "built") == "3", last
    scratch = tmp / "c6scratch"
    seen = []
    real_run = subprocess.run

    def spy(cmd, *a, **k):
        if isinstance(cmd, list) and "pip" in cmd:
            seen.append(list(cmd))
        return real_run(cmd, *a, **k)

    buf = io.StringIO()
    kr.subprocess.run = spy
    try:
        with contextlib.redirect_stdout(buf):
            rc = kr.main(["install-check", "--from", str(out), "--scratch", str(scratch)])
    finally:
        kr.subprocess.run = real_run
    text = buf.getvalue()
    last = text.strip().splitlines()[-1]
    want = "PY-KIT-INSTALL python=%d.%d.%d wheels=3 installed=3 imported=2 import_missing_dep=1 failed=0 ok=True" \
        % sys.version_info[:3]
    assert rc == 0 and last == want, (last, text)
    assert "kit_absent_module_zz9" in text and "import_missing_dep" in text, text
    assert "imported [kitsynone]" in text and "imported [kitsyntwo]" in text, text
    assert seen and all("--no-index" in c and "--no-deps" in c and "--target" in c for c in seen), seen
    assert (scratch / "kitsynone").is_dir() and (scratch / "kitsyntwo.py").is_file(), os.listdir(scratch)
    return last


def case7_every_pip_command_no_index(tmp):
    folder = tmp / "f7"
    cmds = [kr.pip_install_cmd(folder, tmp / "s7"), kr.pip_one_cmd(folder, tmp / "s7", "x==1")]
    for cmd in cmds:
        assert "--no-index" in cmd and "--no-deps" in cmd and "--target" in cmd, cmd
        assert not any(t in cmd for t in ("download", "wheel", "index", "--index-url", "-i")), cmd
    import re
    src = (HERE / "kit_python_repack.py").read_text(encoding="utf-8")
    lists = re.findall(r'\[[^\]]*"-m", "pip"[^\]]*\]', src)
    assert len(lists) == len(cmds) and all('"--no-index"' in item and '"--no-deps"' in item for item in lists), lists
    assert not re.search(r'"(download|wheel|index)"', src), "a pip verb that can reach an index"
    return "--no-index in %d of %d pip commands the tool constructs (source scan and built commands)" % (len(lists), len(lists))


def case8_scripts_launchers_partial(tmp):
    base = tmp / "c8"
    sheb = b"#!C:\\Users\\someone\\AppData\\Local\\Programs\\Python\\Python312\\python.exe\r\nprint('hi')\n"
    exe = b"MZ" + os.urandom(2000)
    site, di = make_dist(
        base, "scrone", "1.0", {"scrone/__init__.py": b"def main():\n    pass\n"},
        entry_points="[console_scripts]\nscrone = scrone:main\n[gui_scripts]\nscrone-gui = scrone:main\n",
        outside={"../../Scripts/scrone.exe": b"LAUNCHER", "../../Scripts/scrone-gui.exe": b"LAUNCHER2",
                 "../../Scripts/tool.py": sheb, "../../Scripts/realbin.exe": exe, "../../Include/scrone.h": b"/* h */\n"})
    cls = classification(tmp / "c8.json", [("scrone", "1.0", di, "PURE-INSTALLED")])
    rc, text, last = run_repack(tmp / "c8out", cls, site)
    assert field(last, "built") == "1" and field(last, "partial") == "1" and last.endswith("ok=True"), (last, text)
    man = json.loads((tmp / "c8out" / "MANIFEST.json").read_text())
    w = man["wheels"][0]
    assert sorted(w["launchers_skipped"]) == ["../../Scripts/scrone-gui.exe", "../../Scripts/scrone.exe"], w
    assert w["partial_paths"] == ["../../Include/scrone.h"] and w["partial"] is True, w
    assert sorted(w["scripts_placed"]) == ["../../Scripts/realbin.exe", "../../Scripts/tool.py"], w
    assert w["shebangs_restored"] == ["../../Scripts/tool.py"], w
    with zipfile.ZipFile(tmp / "c8out" / w["file"]) as zf:
        names = zf.namelist()
        assert not [n for n in names if ".." in n.split("/")], names
        assert "scrone-1.0.data/scripts/tool.py" in names and "scrone-1.0.data/scripts/realbin.exe" in names, names
        assert not [n for n in names if "scrone.exe" in n or "scrone-gui.exe" in n], names
        assert zf.read("scrone-1.0.data/scripts/tool.py") == b"#!python\nprint('hi')\n"
        assert zf.read("scrone-1.0.data/scripts/realbin.exe") == exe
    # a RECORD that lists the same script twice (wheel path hashed, installed path unhashed) merges to one packed file
    base2 = tmp / "c8b"
    data = b"BINARY" * 100
    site2, di2 = make_dist(base2, "twice", "1.0", {"twice/__init__.py": b"A = 1\n"}, outside={"../../Scripts/twice.exe": data},
                           extra_record=[("twice-1.0.data\\scripts\\twice.exe", "sha256=" + b64sha(data), str(len(data)))])
    rec = pathlib.Path(site2, di2, "RECORD")
    rec.write_text(rec.read_text().replace("../../Scripts/twice.exe,sha256=" + b64sha(data) + "," + str(len(data)),
                                           "../../Scripts/twice.exe,,"), encoding="utf-8")
    cls2 = classification(tmp / "c8b.json", [("twice", "1.0", di2, "PURE-INSTALLED")])
    rc, text, last = run_repack(tmp / "c8bout", cls2, site2)
    assert last.endswith("ok=True") and field(last, "built") == "1", (last, text)
    with zipfile.ZipFile(tmp / "c8bout" / "twice-1.0-py3-none-any.whl") as zf:
        assert zf.read("twice-1.0.data/scripts/twice.exe") == data
    man2 = json.loads((tmp / "c8bout" / "MANIFEST.json").read_text())
    assert man2["wheels"][0]["unverified_files"] == 0, man2["wheels"][0]
    return last


def case9_tags_and_names(tmp):
    assert kr.compress_tags(["py2-none-any", "py3-none-any"]) == "py2.py3-none-any"
    assert kr.compress_tags(["cp310-abi3-win_amd64"]) == "cp310-abi3-win_amd64"
    assert kr.compress_tags(["py3-none-win_amd64"]) == "py3-none-win_amd64"
    try:
        kr.compress_tags(["py2-none-any", "py3-abi3-win_amd64"])
        raise AssertionError("a non-product tag set must be refused")
    except ValueError:
        pass
    base = tmp / "c9"
    site, di1 = make_dist(base, "Tagged_Dist.Name", "1.0.post1", {"tagged_dist/__init__.py": b"A = 1\n"},
                          tags=("py2-none-any", "py3-none-any"))
    _s, di2 = make_dist(base, "abi3pkg", "4.2", {"abi3pkg/__init__.py": b"A = 1\n", "abi3pkg/_x.pyd": b"MZ" * 50},
                        tags=("cp39-abi3-win_amd64",), purelib=False)
    cls = classification(tmp / "c9.json", [("Tagged_Dist.Name", "1.0.post1", di1, "PURE-INSTALLED"),
                                           ("abi3pkg", "4.2", di2, "ABI3-INSTALLED")])
    rc, text, last = run_repack(tmp / "c9out", cls, site)
    got = sorted(n for n in os.listdir(tmp / "c9out") if n.endswith(".whl"))
    assert got == ["abi3pkg-4.2-cp39-abi3-win_amd64.whl", "tagged_dist_name-1.0.post1-py2.py3-none-any.whl"], got
    assert last.endswith("ok=True"), last
    return ", ".join(got)


def case10_byte_reproducible(tmp):
    base = tmp / "c10"
    site, di = make_dist(base, "repro", "1.0", {"repro/__init__.py": b"A = 1\n", "repro/z.py": b"Z = 26\n" * 1000,
                                                "repro/a.py": b"A = 0\n"})
    cls = classification(tmp / "c10.json", [("repro", "1.0", di, "PURE-INSTALLED")])
    run_repack(tmp / "c10a", cls, site)
    os.utime(pathlib.Path(site, "repro", "z.py"), (1_000_000_000, 1_000_000_000))
    run_repack(tmp / "c10b", cls, site)
    sa = hashlib.sha256((tmp / "c10a" / "repro-1.0-py3-none-any.whl").read_bytes()).hexdigest()
    sb = hashlib.sha256((tmp / "c10b" / "repro-1.0-py3-none-any.whl").read_bytes()).hexdigest()
    assert sa == sb, (sa, sb)
    return "sha256 %s identical across two runs (file mtime changed between them)" % sa[:12]


CASES = [("pure package re-packs and its wheel verifies", case1_pure_repack),
         ("a file that differs from RECORD, and a file that is missing, mark MODIFIED and leave the package out",
          case2_modified_left_out),
         ("a .pyc is never packed", case3_pyc_never_packed),
         ("the regenerated RECORD hashes match the members", case4_record_regenerated),
         ("verify refuses one flipped byte and a stray file", case5_verify_refuses_tamper_and_stray),
         ("install-check on three synthetic wheels with this interpreter: two import, one import_missing_dep",
          case6_install_check),
         ("every pip command constructed carries --no-index", case7_every_pip_command_no_index),
         ("launchers are not packed, scripts go under .data/scripts, other outside paths mark PARTIAL",
          case8_scripts_launchers_partial),
         ("tags compress as the wheel specification states and name the file", case9_tags_and_names),
         ("two builds of one package are byte-identical", case10_byte_reproducible)]


def main():
    passed = 0
    with tempfile.TemporaryDirectory(prefix="kit-repack-test-") as td:
        tmp = pathlib.Path(td)
        for i, (title, fn) in enumerate(CASES, 1):
            try:
                detail = fn(tmp)
                passed += 1
                print("PASS case %d: %s -- %s" % (i, title, detail))
            except Exception as exc:  # noqa: BLE001 - a failing case is reported, never raised
                print("FAIL case %d: %s -- %s: %s" % (i, title, type(exc).__name__, kr.asc(exc)[:300]))
                traceback.print_exc(limit=3, file=sys.stdout)
    ok = passed == len(CASES)
    print("PY-REPACK-TEST cases=%d/%d ok=%s" % (passed, len(CASES), ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
