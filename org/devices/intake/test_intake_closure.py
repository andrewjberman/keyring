"""test_intake_closure.py -- tests for org/devices/intake/intake_closure.py on SYNTHETIC installed distributions in a temporary
directory (hand-made dist-info folders: no real package is read, nothing is fetched, nothing is installed).

LAST line: INTAKE-CLOSURE-TEST cases=<k>/<n> ok=<True|False>
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

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("intake_closure", HERE / "intake_closure.py")
ic = importlib.util.module_from_spec(spec)
sys.modules["intake_closure"] = ic
spec.loader.exec_module(ic)

TARGET = ic.make_target("cp314-win_amd64")
SUPPORTED = ic.kw.supported_tags(TARGET)


def make_dist(site, name, version, requires=(), tags=("py3-none-any",), purelib=True, record=True):
    """Write <site>/<name>-<version>.dist-info with METADATA (Requires-Dist lines), WHEEL and RECORD."""
    site = pathlib.Path(site)
    di = site / ("%s-%s.dist-info" % (name.replace("-", "_"), version))
    di.mkdir(parents=True, exist_ok=True)
    meta = "Metadata-Version: 2.1\nName: %s\nVersion: %s\n" % (name, version)
    meta += "".join("Requires-Dist: %s\n" % r for r in requires)
    (di / "METADATA").write_text(meta, encoding="ascii")
    wheel = "Wheel-Version: 1.0\nGenerator: test\nRoot-Is-Purelib: %s\n" % ("true" if purelib else "false")
    wheel += "".join("Tag: %s\n" % t for t in tags)
    (di / "WHEEL").write_text(wheel, encoding="ascii")
    if record:
        (di / "RECORD").write_text("%s/RECORD,,\n" % di.name, encoding="ascii")
    return di


def run(site, lines):
    """Run the pure core over a synthetic site and requirement lines. -> result dict with by_norm."""
    installed, _src = ic.load_installed([("<test-site:1>", site)])
    res = ic.compute([(i + 1, t) for i, t in enumerate(lines)], installed, TARGET, SUPPORTED)
    return res


def names(res, **want):
    return sorted(m["norm"] for m in res["members"] if all(m.get(k) == v for k, v in want.items()))


def case1_two_level_chain_closes(tmp):
    site = tmp / "c1"
    make_dist(site, "alpha", "1.0", ["beta>=1.0"])
    make_dist(site, "beta", "1.5", ["gamma"])
    make_dist(site, "gamma", "2.0")
    res = run(site, ["alpha==1.0"])
    assert names(res) == ["alpha", "beta", "gamma"], names(res)
    assert names(res, kind="line") == ["alpha"] and names(res, kind="dependency") == ["beta", "gamma"]
    assert res["by_norm"]["gamma"]["depth"] == 2 and res["by_norm"]["gamma"]["parents"] == ["beta"], res["by_norm"]["gamma"]
    assert res["fixed_point"] is True and res["conflicts"] == [] and all(m["class"] == "PURE" for m in res["members"])
    return "closure of 3 = 1 line + 2 dependencies; gamma at depth 2 through beta"


def case2_marker_for_other_target_not_followed(tmp):
    site = tmp / "c2"
    make_dist(site, "alpha", "1.0", ['old_py; python_version < "3.10"', 'only_linux; sys_platform == "linux"',
                                     'win_new; sys_platform == "win32" and python_version >= "3.14"',
                                     'plain_dep'])
    for n in ("old_py", "only_linux", "win_new", "plain_dep"):
        make_dist(site, n, "1.0")
    res = run(site, ["alpha"])
    # this interpreter is 3.12: a marker read for the RUNNING python would drop win_new and keep old_py
    assert names(res) == ["alpha", "plain-dep", "win-new"], names(res)
    # and a LINE whose marker excludes the target is counted, not followed
    res2 = run(site, ['alpha; sys_platform == "linux"'])
    assert names(res2) == [] and len(res2["not_applicable"]) == 1, res2["not_applicable"]
    return "followed: plain_dep, win_new (3.14, win32); not followed: old_py, only_linux"


def case3_extra_followed_only_when_asked(tmp):
    site = tmp / "c3"
    make_dist(site, "alpha", "1.0", ['fastlib; extra == "fast"', "base"])
    make_dist(site, "fastlib", "1.0")
    make_dist(site, "base", "1.0")
    make_dist(site, "asker", "1.0", ["alpha[fast]"])
    assert names(run(site, ["alpha"])) == ["alpha", "base"]
    assert names(run(site, ["alpha[fast]"])) == ["alpha", "base", "fastlib"]
    # a parent asks for the extra AFTER alpha was already expanded without it: the fixed point re-expands alpha
    res = run(site, ["alpha", "asker"])
    assert names(res) == ["alpha", "asker", "base", "fastlib"], names(res)
    assert res["by_norm"]["alpha"]["requested_extras"] == ["fast"] and res["fixed_point"] is True
    return "alpha: no extra -> base; [fast] -> base, fastlib; extra asked by a later parent -> re-expanded"


def case4_missing_copy_is_unknown_not_installed(tmp):
    site = tmp / "c4"
    make_dist(site, "alpha", "1.0", ["ghost>=1", "beta"])
    make_dist(site, "beta", "1.0")
    res = run(site, ["alpha"])
    g = res["by_norm"]["ghost"]
    assert g["class"] == "UNKNOWN-NOT-INSTALLED" and g["version"] is None and g["parents"] == ["alpha"], g
    assert names(res, **{"class": "UNKNOWN-NOT-INSTALLED"}) == ["ghost"] and "beta" in res["by_norm"]
    assert res["fixed_point"] is True
    data = {"members": res["members"], "fixed_point": True, "unparsed": [], "conflicts": res["conflicts"],
            "requirements_file": {"installable_lines": 1}, "target": {"label": "cp314-win_amd64"}}
    line, ok = ic.last_line(data)
    assert "unknown_not_installed=1" in line and "closure=3" in line and ok, line
    return "ghost counted and named, not expanded; the last line reads unknown_not_installed=1"


def case5_cycle_terminates(tmp):
    site = tmp / "c5"
    make_dist(site, "xx", "1.0", ["yy"])
    make_dist(site, "yy", "1.0", ["xx", "yy"])
    res = run(site, ["xx"])
    assert names(res) == ["xx", "yy"] and res["fixed_point"] is True, (names(res), res["fixed_point"])
    assert res["passes"] < 20, res["passes"]
    return "a two-package cycle plus a self-reference closes in %d passes" % res["passes"]


def case6_specifier_conflict_counted(tmp):
    site = tmp / "c6"
    make_dist(site, "alpha", "1.0", ["beta>=2.0", "gamma<2"])
    make_dist(site, "beta", "1.0")
    make_dist(site, "gamma", "1.5")
    res = run(site, ["alpha==1.0", "beta==1.0"])
    confl = res["conflicts"]
    assert len(confl) == 1, confl
    c = confl[0]
    assert (c["child"], c["parent"], c["specifier"], c["installed_version"]) == ("beta", "alpha", ">=2.0", "1.0"), c
    # a line pin that the installed copy does not meet is also counted, with requirements.txt as the parent
    res2 = run(site, ["gamma==9.9"])
    assert [(x["parent"], x["specifier"]) for x in res2["conflicts"]] == [("requirements.txt", "==9.9")], res2["conflicts"]
    return "beta 1.0 against alpha's >=2.0 counted once; gamma 1.5 against a line pin ==9.9 counted with requirements.txt"


def case7_names_normalised(tmp):
    site = tmp / "c7"
    make_dist(site, "Foo_Bar.baz", "3.1", ["Needs-More_Stuff"])
    make_dist(site, "needs.more-stuff", "1.0")
    res = run(site, ["foo-bar-baz"])
    assert names(res) == ["foo-bar-baz", "needs-more-stuff"], names(res)
    return "foo-bar-baz matches Foo_Bar.baz; Needs-More_Stuff matches needs.more-stuff"


def case8_classes_from_tags(tmp):
    site = tmp / "c8"
    make_dist(site, "purepkg", "1.0")
    make_dist(site, "abipkg", "1.0", tags=("cp311-abi3-win_amd64",), purelib=False)
    make_dist(site, "oldcompiled", "1.0", tags=("cp312-cp312-win_amd64",), purelib=False)
    make_dist(site, "norecord", "1.0", record=False)
    d = make_dist(site, "nometa", "1.0")
    (d / "WHEEL").unlink()
    res = run(site, ["purepkg", "abipkg", "oldcompiled", "norecord", "nometa"])
    got = {m["norm"]: m["class"] for m in res["members"]}
    assert got == {"purepkg": "PURE", "abipkg": "FITS", "oldcompiled": "COMPILED-OTHER-PYTHON", "norecord": "NO-METADATA",
                   "nometa": "NO-METADATA"}, got
    assert ic.wheel_name("Old.Compiled-Pkg", "1.0.post1") == "old_compiled_pkg-1.0.post1"
    assert ic.wheel_name("pdfminer.six", "20251230") == "pdfminer_six-20251230"
    return "pure, stable-ABI, cp312-only, no RECORD and no WHEEL each land in exactly one class; wheel names normalise"


def case9_cli_last_line_from_file_explain_fetchlist(tmp):
    site = tmp / "c9"
    make_dist(site, "alpha", "1.0", ["beta", "zed"])
    make_dist(site, "beta", "1.0", ["deep"])
    make_dist(site, "deep", "4.2", tags=("cp312-cp312-win_amd64",), purelib=False)
    make_dist(site, "zed", "1.0", tags=("cp312-cp312-win_amd64",), purelib=False)
    reqs = tmp / "c9req.txt"
    reqs.write_text("# header\nalpha==1.0   # one line\n", encoding="ascii")
    out = tmp / "c9closure.json"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = ic.main(["closure", "--target", "cp314-win_amd64", "--requirements", str(reqs), "--site-packages", str(site),
                      "--out", str(out)])
    last = buf.getvalue().strip().splitlines()[-1]
    want = ("INTAKE-CLOSURE target=cp314-win_amd64 lines=1 closure=4 dependencies_added=3 pure=2 fits=0 needs_fetch=2 "
            "unknown_not_installed=0 specifier_conflicts=0 fixed_point=True ok=True")
    assert rc == 0 and last == want, last
    text = out.read_text(encoding="ascii")
    assert str(tmp) not in text, "a temporary path was baked into the saved file"
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = ic.main(["closure", "--from-file", str(out)])
    assert rc == 0 and buf.getvalue().strip().splitlines()[-1] == want
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = ic.main(["explain", "deep", "--from-file", str(out)])
    assert rc == 0 and "chain: alpha -> beta (any) -> deep (any)" in buf.getvalue(), buf.getvalue()
    # the fetch list: both compiled members, approval read from a synthetic assessment table
    ass = tmp / "assessment.md"
    ass.write_text("| 1 | `deep==4.2` | x | yes | d | 1 | YES |\n| 2 | `other==1.0` | x | NO | d | 1 | **NO at this pin** |\n",
                   encoding="ascii")
    data = json.loads(text)
    fl = ic.build_fetchlist(data, ic.read_assessment(ass))
    st = {c["norm"]: (c["status"], c["file_name"]) for c in fl["compiled"]}
    assert st == {"deep": ("APPROVED", "deep-4.2-cp314-cp314-win_amd64.whl"),
                  "zed": ("NEW-REQUEST", "zed-1.0-cp314-cp314-win_amd64.whl")}, st
    assert [a["norm"] for a in fl["assessed_not_needing_fetch"]] == ["other"], fl["assessed_not_needing_fetch"]
    fl2 = ic.build_fetchlist(data, None)
    assert {c["status"] for c in fl2["compiled"]} == {"APPROVAL-UNREAD"}
    return "last line exact; --from-file re-prints it; explain names the chain; fetch list: APPROVED / NEW-REQUEST / UNREAD"


CASES = [("a two-level chain closes", case1_two_level_chain_closes),
         ("a marker that excludes the target is not followed (target read, not the running python)",
          case2_marker_for_other_target_not_followed),
         ("an extra is followed only when asked, and a late ask re-expands", case3_extra_followed_only_when_asked),
         ("a missing installed copy is UNKNOWN-NOT-INSTALLED, counted and not expanded",
          case4_missing_copy_is_unknown_not_installed),
         ("a cycle terminates at a fixed point", case5_cycle_terminates),
         ("a specifier conflict is counted with parent, specifier and installed version", case6_specifier_conflict_counted),
         ("names are matched after normalisation", case7_names_normalised),
         ("each member lands in exactly one class", case8_classes_from_tags),
         ("the saved file, its bounded re-print, explain and the fetch list", case9_cli_last_line_from_file_explain_fetchlist)]


def main():
    passed = 0
    with tempfile.TemporaryDirectory(prefix="intake-closure-test-") as td:
        tmp = pathlib.Path(td)
        for i, (title, fn) in enumerate(CASES, 1):
            try:
                detail = fn(tmp)
                passed += 1
                print("PASS case %d: %s -- %s" % (i, title, detail))
            except Exception as exc:  # noqa: BLE001 - a failing case is reported, never raised
                print("FAIL case %d: %s -- %s: %s" % (i, title, type(exc).__name__, ic.asc(exc)[:300]))
                traceback.print_exc(limit=4, file=sys.stdout)
    ok = passed == len(CASES)
    print("INTAKE-CLOSURE-TEST cases=%d/%d ok=%s" % (passed, len(CASES), ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
