"""test_kit_python.py -- the Python kit's census, pack and install-verification, on this box and on stand-ins (cell CT-k-2).

    python org/devices/test_kit_python.py        # LAST line: KIT-TEST cases=<k>/7 ok=<True|False>

No network, no package index, no install on this box. Every artifact is written to a temporary directory. The only pip call is the
`--no-index --dry-run` the tools themselves make, and case 6 records every subprocess argv the pack and install run and asserts it.
"""
from __future__ import annotations

import ast
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import kit_python_census as census  # noqa: E402
import kit_python_install as install  # noqa: E402
import kit_python_pack as pack  # noqa: E402

CENSUS = str(HERE / "kit_python_census.py")
PACK = str(HERE / "kit_python_pack.py")
INSTALL = str(HERE / "kit_python_install.py")
TMP = pathlib.Path(tempfile.mkdtemp(prefix="kit_python_test_"))
STATE = {}


def run(script, *args, device="laptop"):
    env = dict(os.environ, AGENTBUS_DEVICE=device)
    r = subprocess.run([sys.executable, script] + list(args), env=env, capture_output=True, text=True, check=False)
    return r.returncode, (r.stdout + r.stderr)


def last(out, prefix):
    lines = [x for x in out.splitlines() if x.startswith(prefix)]
    return lines[-1] if lines else ""


def field(line, key):
    m = re.search(r"\b%s=(\S+)" % re.escape(key), line)
    return m.group(1) if m else None


def synthetic_from_here(device, lacking, bump=None):
    """An installed.json for a box that is THIS box minus `lacking` (distribution names), optionally with one version altered."""
    rc, out = run(CENSUS, "installed", "--out", str(TMP / "here.json"), "--required", str(TMP / "required.json"))
    doc = json.loads((TMP / "here.json").read_text(encoding="utf-8"))
    doc["device"] = device
    for k in lacking:
        doc["distributions"][k] = None
        doc["all_installed"].pop(k, None)
    for k in doc.get("modules_importable", {}):
        doc["modules_importable"][k] = True  # the stand-in has the modules that have no distribution anywhere
    if bump:
        doc["distributions"][bump] = "0.0.1"
    return doc


def pick_two_pure():
    req = census.load_required(str(TMP / "required.json"))
    cands = []
    for d in req["distributions"]:
        if d["kind"] != "import" or not d.get("version_here"):
            continue
        dist = pack.get_dist(d["distribution"])
        if dist is None or pack.is_compiled(dist):
            continue
        try:
            cands.append((len(pack.record_entries(dist)), d["distribution"]))
        except pack.Unpackable:
            continue
    cands.sort()
    return [n for _c, n in cands[:2]]


def case1():
    rc, out = run(CENSUS, "required", "--out", str(TMP / "required.json"))
    line = last(out, "KIT-REQUIRED")
    doc = json.loads((TMP / "required.json").read_text(encoding="utf-8"))
    STATE["required_line"] = line
    dists = {d["distribution"]: d for d in doc["distributions"]}
    pmc = dists.get("pandas-market-calendars")
    ruff = dists.get("ruff")
    mods = {m["module"]: m for m in doc["modules"]}
    checks = [
        ("last line ok=True with unparsed=0", rc == 0 and field(line, "unparsed") == "0" and field(line, "ok") == "True"),
        ("pandas_market_calendars module is OPTIONAL", mods.get("pandas_market_calendars", {}).get("usage") == "OPTIONAL"),
        ("pandas-market-calendars is a required distribution (OPTIONAL)", pmc is not None and pmc["usage"] == "OPTIONAL"),
        ("ruff is a required distribution with kind=tool", ruff is not None and ruff["kind"] == "tool" and bool(ruff["version_here"])),
        ("the scan counted the tracked files", int(field(line, "files") or 0) > 0),
    ]
    return checks, line


def case2():
    rc, out = run(CENSUS, "installed", "--out", str(TMP / "here_installed.json"), "--required", str(TMP / "required.json"))
    rc2, out2 = run(CENSUS, "compare", str(TMP / "here_installed.json"), "--required", str(TMP / "required.json"))
    line = last(out2, "KIT-COMPARE")
    not_installed = int(field(STATE["required_line"], "not_installed_here"))
    missing = int(field(line, "missing"))
    STATE["base_missing"] = missing
    checks = [
        ("installed ran (rc 0)", rc == 0),
        ("compare missing agrees with required's not_installed_here (%d)" % not_installed, missing == not_installed),
        ("ok matches missing==0", (field(line, "ok") == "True") == (missing == 0)),
        ("version_differs=0 on the box that made the list", field(line, "version_differs") == "0"),
    ]
    # the refusal arm: no device name
    env = {k: v for k, v in os.environ.items() if k != "AGENTBUS_DEVICE"}
    r = subprocess.run([sys.executable, CENSUS, "installed"], env=env, capture_output=True, text=True, check=False)
    checks.append(("installed refuses when AGENTBUS_DEVICE is unset", r.returncode != 0 and "REFUSED" in r.stdout))
    return checks, line


def case3():
    two = pick_two_pure()
    STATE["two"] = two
    doc = synthetic_from_here("standin1", two)
    p = TMP / "standin1.json"
    p.write_text(json.dumps(doc), encoding="utf-8")
    rc, out = run(CENSUS, "compare", str(p), "--required", str(TMP / "required.json"))
    line = last(out, "KIT-COMPARE")
    # the version-mismatch arm: an altered version is reported, not failed
    ver = synthetic_from_here("standin1", [], bump=two[0])
    (TMP / "standin_ver.json").write_text(json.dumps(ver), encoding="utf-8")
    rc2, out2 = run(CENSUS, "compare", str(TMP / "standin_ver.json"), "--required", str(TMP / "required.json"))
    line2 = last(out2, "KIT-COMPARE")
    checks = [
        ("two pure-Python distributions were found to remove: %s" % two, len(two) == 2),
        ("compare reads missing=2", field(line, "missing") == "2" and field(line, "ok") == "False"),
        ("the two named MISSING", all(re.search(r"^MISSING\s+%s\s" % re.escape(n), out, re.M) for n in two)),
        ("version-mismatch arm: VERSION-DIFFERS=1, missing=0, ok=True",
         field(line2, "version_differs") == "1" and field(line2, "missing") == "0" and field(line2, "ok") == "True"),
    ]
    return checks, line


def case4():
    out_dir = TMP / "pack_standin1"
    rc, out = run(PACK, "--for", str(TMP / "standin1.json"), "--out", str(out_dir), "--required", str(TMP / "required.json"))
    line = last(out, "KIT-PACK")
    mp = out_dir / "MANIFEST.json"
    manifest = json.loads(mp.read_text(encoding="utf-8")) if mp.is_file() else {"files": []}
    names = {e["distribution"] for e in manifest["files"]}
    sums = all(install.sha256_file(out_dir / e["file"]) == e["sha256"] and (out_dir / e["file"]).stat().st_size == e["size"]
               for e in manifest["files"])
    checks = [
        ("pack last line ok=True, missing=2", rc == 0 and field(line, "ok") == "True" and field(line, "missing") == "2"),
        ("artifacts and MANIFEST.json written, one wheel per missing distribution", set(STATE["two"]) <= names and mp.is_file()),
        ("every manifest SHA-256 and size matches its file", bool(manifest["files"]) and sums),
        ("each manifest row carries how it was obtained", all(e.get("how") for e in manifest["files"])),
        ("the written wheels pass pip's --no-index --dry-run self-check", "pip self-check (--no-index --dry-run, rc=0)" in out),
    ]
    return checks, line


def case5():
    src = TMP / "pack_standin1"
    bad = TMP / "pack_tampered"
    shutil.copytree(src, bad)
    manifest = json.loads((bad / "MANIFEST.json").read_text(encoding="utf-8"))
    victim = bad / manifest["files"][0]["file"]
    data = bytearray(victim.read_bytes())
    data[len(data) // 2] ^= 0x01
    victim.write_bytes(bytes(data))
    rc, out = run(INSTALL, "--from", str(bad), "--dry-run", device="standin1")
    line = last(out, "KIT-INSTALL")
    n = len(manifest["files"])
    refused = [
        ("tampered pack: install refuses (rc 1, ok=False)", rc == 1 and field(line, "ok") == "False"),
        ("verified=%d/%d (the one flipped byte is the only failure)" % (n - 1, n), field(line, "verified") == "%d/%d" % (n - 1, n)),
        ("names the SHA-256 mismatch", "SHA-256 %s differs" % manifest["files"][0]["file"] in out),
        ("no pip command was run", "RUN:" not in out and "no pip command was run" in out),
    ]
    rc2, out2 = run(INSTALL, "--from", str(src), "--dry-run", device="standin1")
    line2 = last(out2, "KIT-INSTALL")
    control = [
        ("control: the untampered pack verifies %d/%d and the dry-run is ok" % (n, n),
         rc2 == 0 and field(line2, "verified") == "%d/%d" % (n, n) and field(line2, "ok") == "True"),
        ("control: the dry-run command carries --no-index and --dry-run", "--no-index" in out2 and "--dry-run" in out2),
    ]
    # an unlisted wheel and a wrong-device box are refused too
    extra = TMP / "pack_extra"
    shutil.copytree(src, extra)
    shutil.copy(extra / manifest["files"][0]["file"], extra / "stray-1.0-py3-none-any.whl")
    rc3, out3 = run(INSTALL, "--from", str(extra), "--dry-run", device="standin1")
    rc4, out4 = run(INSTALL, "--from", str(src), "--dry-run", device="someone-else")
    more = [
        ("an unlisted wheel in the directory refuses the install", rc3 == 1 and "UNLISTED stray-1.0-py3-none-any.whl" in out3),
        ("a pack for another device refuses", rc4 == 1 and "TARGET" in out4),
    ]
    return refused + control + more, line


def case6():
    cmds = [
        install.build_pip_cmd(["a==1"], find_links="x", user=True, dry_run=False),
        install.build_pip_cmd(["a==1"], find_links="x", user=True, dry_run=True),
        install.build_pip_cmd(["a.whl"], find_links=None, user=False, dry_run=True, extra=["--no-deps"]),
        pack.build_verify_cmd([pathlib.Path("a.whl")]),
    ]
    # every argv the pack and install actually run, recorded while they work on the stand-in
    seen = []
    real_run = subprocess.run

    def spy(argv, *a, **k):
        seen.append(list(argv))
        return real_run(argv, *a, **k)

    subprocess.run = spy
    old_env = os.environ.get("AGENTBUS_DEVICE")
    os.environ["AGENTBUS_DEVICE"] = "standin1"
    try:
        out_dir = TMP / "pack_spy"
        pack.pack(json.loads((TMP / "standin1.json").read_text(encoding="utf-8")), out_dir, required_path=str(TMP / "required.json"))
        sys_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")
        try:
            install.main(["--from", str(out_dir), "--dry-run"])
        finally:
            sys.stdout.close()
            sys.stdout = sys_stdout
    finally:
        subprocess.run = real_run
        if old_env is None:
            os.environ.pop("AGENTBUS_DEVICE", None)
        else:
            os.environ["AGENTBUS_DEVICE"] = old_env
    pips = [c for c in seen if "pip" in c]
    src = "\n".join((HERE / f).read_text(encoding="utf-8") for f in ("kit_python_pack.py", "kit_python_install.py"))
    subcmds = set(re.findall(r'"pip",\s*"(\w+)"', src))
    literals = []  # every string literal in the code, docstrings excluded
    for fname in ("kit_python_pack.py", "kit_python_install.py"):
        tree = ast.parse((HERE / fname).read_text(encoding="utf-8"))
        docs = {id(n.body[0].value) for n in ast.walk(tree)
                if isinstance(n, (ast.Module, ast.FunctionDef, ast.ClassDef)) and n.body and isinstance(n.body[0], ast.Expr)
                and isinstance(n.body[0].value, ast.Constant)}
        literals += [n.value for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docs]
    checks = [
        ("every built pip command string carries --no-index (%d built)" % len(cmds), all("--no-index" in c for c in cmds)),
        ("every pip argv actually run carried --no-index (%d run)" % len(pips), len(pips) >= 2 and all("--no-index" in c for c in pips)),
        ("the only pip subcommand in the sources is install", subcmds <= {"install"}),
        ("no source names an index URL, pip download or pip wheel",
         not any(re.search(r"index-url|https?://|^download$|^wheel$", x) for x in literals)),
        ("no pip run was a real install (each was --dry-run)", all("--dry-run" in c for c in pips)),
    ]
    return checks, "%d pip argv recorded" % len(pips)


def case7():
    minor = "3.9" if census.box_facts()["python_minor"] != "3.9" else "3.8"
    doc = synthetic_from_here("standin2", ["ruff"])
    doc["python_minor"] = minor
    doc["python_version"] = minor + ".0"
    (TMP / "standin2.json").write_text(json.dumps(doc), encoding="utf-8")
    out_dir = TMP / "pack_standin2"
    rc, out = run(PACK, "--for", str(TMP / "standin2.json"), "--out", str(out_dir), "--required", str(TMP / "required.json"))
    line = last(out, "KIT-PACK")
    # control: the same different-minor target, missing only a PURE distribution -> not refused
    doc2 = synthetic_from_here("standin3", [STATE["two"][0]])
    doc2["python_minor"] = minor
    doc2["python_version"] = minor + ".0"
    (TMP / "standin3.json").write_text(json.dumps(doc2), encoding="utf-8")
    out_dir3 = TMP / "pack_standin3"
    rc3, out3 = run(PACK, "--for", str(TMP / "standin3.json"), "--out", str(out_dir3), "--required", str(TMP / "required.json"))
    line3 = last(out3, "KIT-PACK")
    checks = [
        ("different python (%s) + missing compiled ruff: pack refuses (rc 1)" % minor, rc == 1 and "REFUSED" in out),
        ("refusal writes nothing (no MANIFEST.json, no wheel)", not out_dir.exists() or not any(out_dir.iterdir())),
        ("refusal last line ok=False packed=0", field(line, "ok") == "False" and field(line, "packed") == "0"),
        ("control: different python + only a pure distribution missing is packed, ok=True",
         rc3 == 0 and "REFUSED" not in out3 and field(line3, "ok") == "True" and (out_dir3 / "MANIFEST.json").is_file()),
    ]
    return checks, line


def main():
    cases = [("1 required on the real tree", case1), ("2 installed then compare on this box", case2),
             ("3 compare on a box lacking two pure distributions", case3), ("4 pack for that box", case4),
             ("5 install verification: tampered artifact refused", case5), ("6 every pip command carries --no-index", case6),
             ("7 a different python and a missing compiled distribution: pack refuses", case7)]
    passed = 0
    try:
        for name, fn in cases:
            try:
                checks, evidence = fn()
            except Exception as e:  # a case that cannot run is a FAIL, never a skip
                checks, evidence = [("case ran without an exception (%s: %s)" % (type(e).__name__, e), False)], ""
            bad = [c for c, ok in checks if not ok]
            print("%s case %s | %s" % ("PASS" if not bad else "FAIL", name, evidence))
            for c, ok in checks:
                print("    %s %s" % ("ok  " if ok else "FAIL", c))
            passed += 0 if bad else 1
    finally:
        shutil.rmtree(TMP, ignore_errors=True)
    print("KIT-TEST cases=%d/%d ok=%s" % (passed, len(cases), passed == len(cases)))
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    sys.exit(main())
