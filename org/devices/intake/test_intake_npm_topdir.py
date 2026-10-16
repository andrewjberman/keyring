#!/usr/bin/env python3
"""test_intake_npm_topdir.py -- the npm PACKAGE ROOT (TO NFRA_CTLPLN.TO-CT-cf-1). npm and bun strip the FIRST path component of a
tarball, whatever its name; the package root of a tarball is therefore its single top-level folder, not a folder named package/.
Check 2, verify and install all take that one root; a tarball with no single top-level folder is refused by each of them, and
the install writes nothing. Proven against the loopback registry of test_intake_npm.py and temporary folders only: no network
request, no real cache, no held folder, no lifecycle script.

Arms (each prints PASS or FAIL with its detail):
  a  control: root package/ still passes check 2, verify clears and install places limbprobe@1.0.0@@@1 with its package.json
  b  root react/: check 2 passes, verify clears and install places limbreact@19.3.0@@@1 (the root folder itself is not in it)
  c  root 'node v24.13' (a space): check 2 passes, verify clears, install lands limbspace@1.0.0@@@1, and no root name is in any
     destination
  d  scoped @types/react with root react/: lands at <target>/@types/react@19.3.0@@@1/ with its package.json
  e  NO root (members at the archive root): check 2 refuses, verify refuses, install writes nothing
  f  TWO roots (a/package.json and b/x): refused the same three ways, nothing written
  g  an absolute first component and a '..' first component: refused the same three ways, nothing written
  h  a file where the top-level folder should be (file 'limbprobe' beside limbprobe/): refused the same three ways
  i  THE REAL PRECHECK reads the installed pack (roots package, react, 'node v24.13'): '3 of 3' and exit 0; the SAME script reads
     '0 of 3' and exits 1 on an empty cache
  j  mutant control: MUTANT literal_package_mutant (the old assumption: every member must sit under package/) makes arm b read
     refused, so arm b reads ok=False under the mutant; the real code reads arm b ok=True
  k  check 6 names a native and an os/cpu restriction at <root>/<file> for root react/ (react/build/probe.node and
     react/package.json os/cpu restriction), and names nothing under package/
  l  parity: the standalone mirror in intake_receive.py returns exactly what intake_check.npm_package_root returns, for every
     member list of PARITY_CORPUS (accepted and refused both present)

Standard library plus the intake tools and the fixtures of test_intake_npm.py and test_intake_npm_install.py; temporary folders
only; ASCII output.
Last line: INTAKE-NPM-TOPDIR arms=<k>/<n> ok=<True|False>
"""
import contextlib
import io
import os
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import intake_check as C  # noqa: E402
import intake_fetch as F  # noqa: E402
import intake_receive as R  # noqa: E402
import test_intake_npm as T  # noqa: E402
import test_intake_npm_install as I  # noqa: E402

LIMB = ("limbprobe", "1.0.0")
REACT = ("limbreact", "19.3.0")
SPACED = ("limbspace", "1.0.0")
SCOPED_REACT = ("@types/react", "19.3.0")
BY = "0.9.0_WK_NFRA_CTLPLN~150"
NO_ROOT = "no package root"
ORIGINAL_ROOT_FN = C.npm_package_root


def root_tgz(root, name, version, extra=None, more=None):
    """A synthetic npm tarball whose one top-level folder is root, whatever its name: package.json and index.js under it."""
    members = {"%s/package.json" % root: T.pkg_json(name, version, extra), "%s/index.js" % root: b"module.exports = 1;\n"}
    members.update(more or {})
    return T.make_tgz(members)


def literal_package_mutant(members):
    """MUTANT of npm_package_root: the literal assumption the batch exposed. Every member must sit under package/, else refused."""
    names = [n.rstrip("/") if is_dir else n for n, is_dir in members]
    if names and all(n == "package" or n.startswith("package/") for n in names):
        return "package", None
    return None, "no package/ folder: the members are not under package/ (the literal assumption)"


def chain(env, specs):
    """specs: (name, version, tarball bytes). Publish, lock, approve, fetch, check (signed), release, then pack. Returns the
    pack folder. Raises when a file does not hold, does not check or does not pack, so an arm reads failed with the cause."""
    entries, lines = [], []
    for name, version, data in specs:
        dist = env.publish(name, version, data)
        entries.append((name, version, dist["integrity"]))
        lines.append("%s@%s" % (name, version))
    env.write_lock(entries)
    env.approve(lines)
    for name, version, _data in specs:
        _rc, fr, _o = env.fetch(name, version)
        if fr.get("outcome") != "held":
            raise RuntimeError("fetch of %s@%s did not hold: %s" % (name, version, fr.get("reason")))
        _rc2, rec, _o2 = env.check(name, version, signed_lines=T.signed_lines(name, version))
        if rec is None or rec.get("verdict") != "checked":
            raise RuntimeError("check of %s@%s read %s" % (name, version, rec.get("verdict") if rec else None))
        env.environ()
        with contextlib.redirect_stdout(io.StringIO()):
            C.main(["release", "--batch", T.BATCH, "--file", F.npm_held_name(name, version), "--ecosystem", "npm"])
    pack = os.path.join(env.tmp, "pack")
    env.environ()
    with contextlib.redirect_stdout(io.StringIO()):
        rc = C.main(["pack", "--batch", T.BATCH, "--out", pack, "--ecosystem", "npm"])
    if rc != 0 or not os.path.isfile(os.path.join(pack, "MANIFEST.json")):
        raise RuntimeError("pack did not build (rc=%s)" % rc)
    return pack


def install_into(env, pack):
    """The real install verb into a fresh cache under the arm's folder. Returns (summary, verify result, items, cache)."""
    cache = os.path.join(env.tmp, "cache")
    summ, res, items = R.install_npm(pack, cache, env.lock, BY, os.path.join(env.tmp, "receipts"))
    return summ, res, items, cache


def placed(cache, name, version):
    """The destination folder of a package and whether its package.json is in it."""
    dest = I.dest_of(cache, name, version)
    return dest, os.path.isfile(os.path.join(dest, "package.json"))


def accepted_arm(name, version, root, extra=None, more=None):
    """Check 2 passes for a root, verify clears and install places the package. Returns (ok, details, env) with env open."""
    env = T.Env()
    try:
        data = root_tgz(root, name, version, extra=extra, more=more)
        pack = chain(env, [(name, version, data)])
        rec = env.check_record(name, version)
        summ, res, items, cache = install_into(env, pack)
        dest, has_pj = placed(cache, name, version)
        ok_c2 = T.verdicts(rec)[2] == "passed" and ("%s/package.json" % root) in rec["checks"][1]["evidence"]["summary"]
        ok = ok_c2 and res["ok"] and summ["ok"] and has_pj
        details = ["check 2 on root %r: %s; summary %r" % (root, T.verdicts(rec)[2], rec["checks"][1]["evidence"]["summary"]),
                   "verify ok=%s; install ok=%s unpacked=%d" % (res["ok"], summ["ok"], summ["unpacked"]),
                   "destination %s package.json present=%s" % (os.path.basename(dest), has_pj)]
    except Exception:
        env.close()
        raise
    return ok, details, env, cache, dest


def arm_a():
    """Control: the 45 batch tarballs with package/ still pass check 2 and install."""
    ok, details, env, _cache, _dest = accepted_arm(LIMB[0], LIMB[1], "package")
    env.close()
    return ok, details


def arm_b():
    """A root react/ passes check 2, verify clears and install places the package beneath react's name."""
    ok, details, env, cache, dest = accepted_arm(REACT[0], REACT[1], "react")
    index_placed = os.path.isfile(os.path.join(dest, "index.js"))
    env.close()
    return ok and index_placed, details + ["index.js placed beneath the destination=%s" % index_placed]


def arm_c():
    """A root with a space (node v24.13) passes check 2, verifies and installs; no root name is in any destination."""
    ok, details, env, cache, dest = accepted_arm(SPACED[0], SPACED[1], "node v24.13")
    names = []
    for dp, dns, fns in os.walk(cache):
        names.extend(dns + fns)
    no_root_name = all("node v24.13" not in n for n in names)
    env.close()
    return ok and no_root_name, details + ["entries under the cache=%d, none names the root=%s" % (len(names), no_root_name)]


def arm_d():
    """A scoped name with root react/ lands at <target>/@types/react@19.3.0@@@1/ with its package.json."""
    ok, details, env, cache, dest = accepted_arm(SCOPED_REACT[0], SCOPED_REACT[1], "react")
    expected = os.path.join(cache, "@types", "react@19.3.0@@@1")
    at_expected = os.path.normpath(dest) == os.path.normpath(expected) and os.path.isdir(expected)
    env.close()
    return ok and at_expected, details + ["destination is <target>/@types/react@19.3.0@@@1: %s" % at_expected]


def refused_three_ways(name, version, data):
    """One refused tarball, read three ways: check 2 (a real check run), verify (the record and the tarball) and install (a
    pack whose record claims checked, so the install's own plan must be the refusal). Returns (ok, details)."""
    env = T.Env()
    try:
        dist = env.publish(name, version, data)
        env.write_lock([(name, version, dist["integrity"])])
        env.approve(["%s@%s" % (name, version)])
        env.fetch(name, version)
        _rc, rec, _o = env.check(name, version, signed_lines=T.signed_lines(name, version))
        c2_summary = rec["checks"][1]["evidence"]["summary"]
        c2_refused = T.verdicts(rec)[2] == "failed" and NO_ROOT in c2_summary
        probs = R._npm_tarball_problems(rec, env.held(name, version), R.load_bun_lock(env.lock))
        verify_refused = any(NO_ROOT in p for p in probs)
        pack, lockfile = I.fabricated_pack(os.path.join(env.tmp, "refused_pack"), name, version, data)
        res = R.verify_pack(pack, "npm", lockfile)
        verify_pack_refused = (not res["ok"]) and any(NO_ROOT in r for w in res["wheels"] for r in w["reasons"])
        cache = os.path.join(env.tmp, "cache")
        summ, _res2, items = R.install_npm(pack, cache, lockfile, BY, os.path.join(env.tmp, "receipts"))
        install_refused = (not summ["ok"]) and any(NO_ROOT in (it.get("reason") or "") for it in items)
        wrote = os.path.isdir(cache) and bool(os.listdir(cache))
        ok = c2_refused and verify_refused and verify_pack_refused and install_refused and not wrote
        return ok, ["check 2 failed with no root=%s (%r)" % (c2_refused, c2_summary[:90]),
                    "verify refused (record and tarball)=%s, verify of the pack refused=%s" % (verify_refused, verify_pack_refused),
                    "install refused=%s, nothing written=%s" % (install_refused, not wrote)]
    finally:
        env.close()


def arm_e():
    """NO root: members at the archive root are refused by check 2, by verify and by install; the install writes nothing."""
    name, version = LIMB
    data = T.make_tgz({"package.json": T.pkg_json(name, version), "index.js": b"x\n"})
    return refused_three_ways(name, version, data)


def arm_f():
    """TWO roots (a/package.json and b/x) are refused the same three ways."""
    name, version = LIMB
    data = T.make_tgz({"a/package.json": T.pkg_json(name, version), "b/x": b"x\n"})
    return refused_three_ways(name, version, data)


def arm_g():
    """An absolute first component and a '..' first component are refused the same three ways; nothing is written."""
    name, version = LIMB
    pkg = T.pkg_json(name, version)
    ok_abs, det_abs = refused_three_ways(name, version, T.make_tgz({"/limbprobe/package.json": pkg, "/limbprobe/x": b"x\n"}))
    ok_dd, det_dd = refused_three_ways(name, version, T.make_tgz({"../limbprobe/package.json": pkg, "../limbprobe/x": b"x\n"}))
    return ok_abs and ok_dd, ["absolute first component:"] + ["  " + d for d in det_abs] + \
        ["'..' first component:"] + ["  " + d for d in det_dd]


def arm_h():
    """A file where the top-level folder should be (limbprobe beside limbprobe/) is refused the same three ways."""
    name, version = LIMB
    pkg = T.pkg_json(name, version)
    data = T.make_tgz({"limbprobe": b"a file, not a folder\n", "limbprobe/package.json": pkg, "limbprobe/index.js": b"x\n"})
    return refused_three_ways(name, version, data)


def arm_i():
    """THE REAL PRECHECK reads the installed pack: 3 of 3 and exit 0; the same script 0 of 3 and exit 1 on an empty cache."""
    env = T.Env()
    try:
        specs = [(LIMB[0], LIMB[1], root_tgz("package", LIMB[0], LIMB[1])),
                 (REACT[0], REACT[1], root_tgz("react", REACT[0], REACT[1])),
                 (SPACED[0], SPACED[1], root_tgz("node v24.13", SPACED[0], SPACED[1]))]
        pack = chain(env, specs)
        summ, _res, items, cache = install_into(env, pack)
        rc, lines = I.precheck(env.lock, cache)
        empty = os.path.join(env.tmp, "empty_cache")
        os.makedirs(empty)
        rc0, lines0 = I.precheck(env.lock, empty)
        first = lines[0] if lines else ""
        first0 = lines0[0] if lines0 else ""
        ok = summ["ok"] and summ["unpacked"] == 3 and first == "3 of 3" and rc == 0 and first0 == "0 of 3" and rc0 == 1
        return ok, ["install ok=%s unpacked=%d" % (summ["ok"], summ["unpacked"]),
                    "real precheck on the installed pack: rc=%d first line %r" % (rc, first),
                    "real precheck on an empty cache: rc=%d first line %r" % (rc0, first0)]
    finally:
        env.close()


def arm_j():
    """Mutant control: under literal_package_mutant arm b must read ok=False; the real code reads arm b ok=True."""
    ok_real, det_real = arm_b()
    C.npm_package_root = literal_package_mutant
    try:
        try:
            ok_mut, det_mut = arm_b()
        except Exception as exc:  # the mutant refuses the chain's check, so the arm raises; that is the read ok=False
            ok_mut, det_mut = False, ["mutant chain raised %s: %s" % (type(exc).__name__, str(exc)[:120])]
    finally:
        C.npm_package_root = ORIGINAL_ROOT_FN
    return ok_real and not ok_mut, ["real code arm b ok=%s" % ok_real,
                                    "MUTANT literal package/ assumption: arm b ok=%s" % ok_mut] + ["  " + d for d in det_mut]


def arm_k():
    """Check 6 names a native and an os/cpu restriction at <root>/<file> for root react/, and nothing under package/."""
    env = T.Env()
    try:
        name, version = REACT
        data = root_tgz("react", name, version, extra={"os": ["win32"], "cpu": ["x64"]},
                        more={"react/build/probe.node": b"synthetic native bytes\n"})
        dist = env.publish(name, version, data)
        env.write_lock([(name, version, dist["integrity"])])
        env.approve(["%s@%s" % (name, version)])
        env.fetch(name, version)
        _rc, rec, _o = env.check(name, version, signed_lines=T.signed_lines(name, version))
        e6 = T.ev(rec, 6)
        native_named = "react/build/probe.node" in e6["native_binaries"]
        restriction_named = "react/package.json os/cpu restriction: cpu, os" in e6["native_binaries"]
        none_under_package = not any(n.startswith("package/") for n in e6["native_binaries"])
        c2_passed = T.verdicts(rec)[2] == "passed"
        ok = native_named and restriction_named and none_under_package and c2_passed and e6["executed"] is False
        return ok, ["check 2=%s; native named at react/=%s; restriction named at react/=%s; none under package/=%s"
                    % (T.verdicts(rec)[2], native_named, restriction_named, none_under_package),
                    "check 6 executed=%s" % e6["executed"]]
    finally:
        env.close()


PARITY_CORPUS = [
    [("package/package.json", False), ("package/index.js", False)],
    [("react/package.json", False)],
    [("node v24.13", True), ("node v24.13/package.json", False)],
    [("react/", True), ("react/a", False)],
    [("x", True)],
    [("package.json", False)],
    [("a/package.json", False), ("b/x", False)],
    [("/abs/x", False)],
    [("../x", False)],
    [("./x", False)],
    [("C:/x", False)],
    [("a\\b", False)],
    [("react", False), ("react/package.json", False)],
    [("", False)],
    [],
]


def arm_l():
    """Parity: the intake_receive mirror of npm_package_root returns exactly what intake_check's function returns, for every
    member list of PARITY_CORPUS (accepted and refused both present)."""
    diffs = [m for m in PARITY_CORPUS if C.npm_package_root(m) != R.npm_package_root(m)]
    accepted = sum(1 for m in PARITY_CORPUS if C.npm_package_root(m)[1] is None)
    ok = not diffs and 0 < accepted < len(PARITY_CORPUS)
    return ok, ["%d member lists; accepted=%d refused=%d; disagreements=%d"
                % (len(PARITY_CORPUS), accepted, len(PARITY_CORPUS) - accepted, len(diffs))]


ARMS = [("a", arm_a), ("b", arm_b), ("c", arm_c), ("d", arm_d), ("e", arm_e), ("f", arm_f), ("g", arm_g), ("h", arm_h),
        ("i", arm_i), ("j", arm_j), ("k", arm_k), ("l", arm_l)]


def main():
    passed = 0
    for label, fn in ARMS:
        try:
            ok, details = fn()
        except Exception as exc:  # an arm that raises is a failed arm, with its cause printed
            ok, details = False, ["raised %s: %s" % (type(exc).__name__, exc)]
            traceback.print_exc(file=sys.stdout)
        for d in details:
            print("  %s" % d.encode("ascii", "replace").decode("ascii"))
        print("%s arm_%s" % ("PASS" if ok else "FAIL", label))
        passed += 1 if ok else 0
    total = len(ARMS)
    ok_all = passed == total
    print("INTAKE-NPM-TOPDIR arms=%d/%d ok=%s" % (passed, total, ok_all))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
