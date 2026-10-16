#!/usr/bin/env python3
"""test_intake_npm_install.py -- the npm install verb of the intake route (the CTO ruling item 5, 2026-10-16): a verified npm
pack is unpacked into a bun install cache as <name>@<version>@@@1 folders, which the REAL ops/bun_cache_precheck.py reads as
present. Proven against a LOOPBACK registry and temporary folders only. Nothing here runs a lifecycle script, bun, a package
manager or a socket; the real bun cache is never written.

Arms (each prints PASS or FAIL with its detail):
  e  install of a 3-package pack (one scoped) lands <name>@<version>@@@1 folders whose package.json parse and name the package
  f  THE REAL PRECHECK reads them: bun_cache_precheck.py run as a subprocess reads "3 of 3" and exits 0; the SAME script reads
     "0 of 3" and exits 1 on an empty cache (negative control)
  g  a pack with one tarball whose sha512 differs from its record is refused as a whole: NOTHING is written to the target
  h  a '..' member and an absolute member (in tarballs that verify) are refused by the install's own member plan; nothing written
  i  an already-present folder is left byte-identical (bytes and mtimes) and reported already
  j  an existing EMPTY folder at a destination is refused, not overwritten; the other destinations are not written
  k  a run twice is idempotent: the first run unpacks 3, the second reads already=3 with unpacked=0, and the tree is unchanged
  l  a lifecycle script in the package is LISTED and NOT executed: a postinstall that would write a marker never writes it
  m  control: a mutant that writes the folders with no package.json makes the real precheck read 2 of 3 or fewer and exit 1

Standard library plus the intake tools and the fixtures of test_intake_npm.py; temporary folders only; ASCII output.
Last line: INTAKE-NPM-INSTALL-TEST arms=<k>/<n> ok=<True|False>
"""
import contextlib
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import intake_check as C  # noqa: E402
import intake_fetch as F  # noqa: E402
import intake_receive as R  # noqa: E402
import test_intake_npm as T  # noqa: E402

PRECHECK = os.path.normpath(os.path.join(HERE, "..", "..", "..", "infra", "aws", "ec2", "opal-gateway", "ops",
                                         "bun_cache_precheck.py"))
EXTRA = ("limbextra", "0.4.2")
TRIO = [T.UNSCOPED, T.SCOPED, EXTRA]


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def dest_of(cache, name, version):
    return os.path.join(cache, *("%s@%s@@@1" % (name, version)).split("/"))


def build_pack(env, specs, lifecycle=None):
    """The real chain for a list of (name, version, package.json extras, extra members): publish, fetch, check (signed),
    release, pack. lifecycle maps name -> the LIFECYCLE reason line to sign. Returns the pack folder."""
    entries, lines = [], []
    lifecycle = lifecycle or {}
    for name, version, extra, more in specs:
        data = T.std_tgz(name, version, extra=extra, more=more)
        dist = env.publish(name, version, data)
        entries.append((name, version, dist["integrity"]))
        lines.append("%s@%s" % (name, version))
    env.write_lock(entries)
    env.approve(lines)
    for name, version, _extra, _more in specs:
        _rc, fr, _o = env.fetch(name, version)
        if fr.get("outcome") != "held":
            raise RuntimeError("fetch of %s@%s did not hold: %s" % (name, version, fr.get("reason")))
        extra_lines = []
        if name in lifecycle:
            extra_lines.append("LIFECYCLE %s: %s" % (F.npm_held_name(name, version), lifecycle[name]))
        _rc2, rec, _o2 = env.check(name, version, signed_lines=T.signed_lines(name, version, extra=extra_lines))
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


def trio_specs(lifecycle_extra=None):
    specs = []
    for name, version in TRIO:
        extra = {"description": "synthetic"}
        more = None
        if (name, version) == T.UNSCOPED and lifecycle_extra:
            extra = dict(extra, scripts=lifecycle_extra)
        specs.append((name, version, extra, more))
    return specs


def run_install(pack, cache, lockfile, receipt_dir=None, by="0.9.0_WK_NFRA_CTLPLN~148"):
    """The CLI, captured. Returns (rc, the printed lines)."""
    args = ["install", "--ecosystem", "npm", "--pack", pack, "--lockfile", lockfile, "--target", cache, "--by", by]
    if receipt_dir:
        args += ["--receipt-dir", receipt_dir]
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        rc = R.main(args)
    return rc, out.getvalue().splitlines()


def last_line(lines):
    return lines[-1] if lines else ""


def precheck(lock, cache):
    """The REAL precheck, as a subprocess. Returns (rc, stdout lines)."""
    proc = subprocess.run([sys.executable, PRECHECK, lock, cache], capture_output=True, text=True, timeout=120)
    return proc.returncode, proc.stdout.splitlines()


def snapshot(root):
    """{relative path: (kind, size, mtime_ns, sha256)} for every folder and file under root; {} when root is absent."""
    out = {}
    if not os.path.isdir(root):
        return out
    for dp, dns, fns in os.walk(root):
        for d in dns:
            p = os.path.join(dp, d)
            out[os.path.relpath(p, root)] = ("dir", 0, os.stat(p).st_mtime_ns, None)
        for f in fns:
            p = os.path.join(dp, f)
            with open(p, "rb") as fh:
                digest = sha256_bytes(fh.read())
            st = os.stat(p)
            out[os.path.relpath(p, root)] = ("file", st.st_size, st.st_mtime_ns, digest)
    return out


def fabricated_pack(folder, name, version, data):
    """A pack built by hand: one tarball whose check record reads checked and whose sha512 equals its lockfile entry, so
    verify passes; the install's own member plan is what must refuse the tarball. Returns (pack, lockfile)."""
    os.makedirs(folder)
    held = F.npm_held_name(name, version)
    tgz = os.path.join(folder, held)
    with open(tgz, "wb") as fh:
        fh.write(data)
    checks = [{"n": n, "name": "c%d" % n, "verdict": "passed", "evidence": {}} for n in range(1, 9)]
    checks[0]["evidence"] = {"computed_sha512": T.sri(data)}
    checks[1]["evidence"] = {"requested_name": name, "requested_version": version, "ident": "%s@%s" % (name, version)}
    checks[7]["evidence"] = {"signer": "fabricated", "path": "fabricated"}
    rec = {"schema": "intake-check/1", "batch": T.BATCH, "file_name": held, "held_sha256": sha256_bytes(data),
           "verdict": "checked", "waived_checks": [], "checks": checks}
    rec_bytes = (json.dumps(rec, indent=2) + "\n").encode("ascii")
    rec_path = tgz + ".check.json"
    with open(rec_path, "wb") as fh:
        fh.write(rec_bytes)
    manifest = {"schema": "fabricated", "batch": T.BATCH, "files": [
        {"name": held, "sha256": sha256_bytes(data), "bytes": len(data)},
        {"name": held + ".check.json", "sha256": sha256_bytes(rec_bytes), "bytes": len(rec_bytes)}]}
    with open(os.path.join(folder, "MANIFEST.json"), "w", encoding="ascii") as fh:
        json.dump(manifest, fh)
    lock = os.path.join(folder, "bun.lock")
    with open(lock, "w", encoding="ascii") as fh:
        fh.write(T.bun_lock_text([(name, version, T.sri(data))]))
    return folder, lock


def arm_e():
    """install of a 3-package pack: <name>@<version>@@@1 folders whose package.json parse and name the package."""
    env = T.Env()
    try:
        pack = build_pack(env, trio_specs())
        cache = os.path.join(env.tmp, "cache")
        rc, lines = run_install(pack, cache, env.lock)
        last = last_line(lines)
        want = {}
        for name, version in TRIO:
            pj = os.path.join(dest_of(cache, name, version), "package.json")
            with open(pj, "r", encoding="utf-8") as fh:
                doc = json.load(fh)
            want[name] = doc.get("name") == name and doc.get("version") == version
        scoped_path = os.path.join(cache, "@limbprobe", "core@7.29.7@@@1", "package.json")
        good = (rc == 0 and last == "INTAKE-NPM-INSTALL tarballs=3 unpacked=3 already=0 refused=0 present=3/3 ok=True"
                and all(want.values()) and os.path.isfile(scoped_path))
        return good, ["install rc=%s last line: %s" % (rc, last),
                      "folders name their package: %s" % json.dumps(want, sort_keys=True),
                      "scoped folder keeps its slash: @limbprobe/core@7.29.7@@@1/package.json exists=%s" % os.path.isfile(scoped_path)]
    finally:
        env.close()


def arm_f():
    """The REAL precheck reads the installed cache 3 of 3 and exits 0; the same script reads 0 of 3 and exits 1 on an empty cache."""
    env = T.Env()
    try:
        pack = build_pack(env, trio_specs())
        cache = os.path.join(env.tmp, "cache")
        run_install(pack, cache, env.lock)
        rc, out = precheck(env.lock, cache)
        empty = os.path.join(env.tmp, "empty-cache")
        os.makedirs(empty)
        rc_n, out_n = precheck(env.lock, empty)
        good = rc == 0 and out and out[0] == "3 of 3" and rc_n == 1 and out_n and out_n[0] == "0 of 3"
        return good, ["real precheck on the installed cache: rc=%s output=%s" % (rc, " | ".join(out)),
                      "negative control, empty cache: rc=%s output=%s" % (rc_n, " | ".join(out_n[:4]))]
    finally:
        env.close()


def arm_g():
    """One tarball whose bytes differ from its record (sha512 and sha256): the whole install is refused and nothing is written."""
    env = T.Env()
    try:
        pack = build_pack(env, trio_specs())
        victim = os.path.join(pack, F.npm_held_name(*T.UNSCOPED))
        with open(victim, "ab") as fh:
            fh.write(b"tamper")
        cache = os.path.join(env.tmp, "cache")
        rc, lines = run_install(pack, cache, env.lock)
        last = last_line(lines)
        nothing = not os.path.exists(cache) or os.listdir(cache) == []
        good = rc == 1 and last.endswith("unpacked=0 already=0 refused=3 present=0/3 ok=False") and nothing
        return good, ["tampered tarball install rc=%s last line: %s" % (rc, last),
                      "target written: %s (absent or empty = nothing written)" % (not nothing)]
    finally:
        env.close()


def arm_h():
    """A '..' member and an absolute member: the install's own member plan refuses each tarball; nothing is written."""
    results, good = [], True
    for label, members in (("dotdot", {"package/package.json": T.pkg_json("limbprobe", "1.0.0"),
                                        "package/../../escape.js": b"x"}),
                           ("absolute", {"package/package.json": T.pkg_json("limbprobe", "1.0.0"),
                                         "/etc/evil.js": b"x"})):
        base = tempfile.mkdtemp(prefix="intake_npm_install_h_")
        try:
            pack, lock = fabricated_pack(os.path.join(base, "pack"), "limbprobe", "1.0.0", T.make_tgz(members))
            cache = os.path.join(base, "cache")
            rc, lines = run_install(pack, cache, lock)
            refused = any(ln.startswith("PACKAGE limbprobe@1.0.0 refused") and
                          ("'..' component" in ln or "absolute" in ln) for ln in lines)
            nothing = not os.path.exists(cache)
            good = good and rc == 1 and refused and nothing
            results.append("%s member: rc=%s refused by the plan=%s target untouched=%s last line: %s" % (
                label, rc, refused, nothing, last_line(lines)))
        finally:
            shutil.rmtree(base, ignore_errors=True)
    return good, results


def arm_i():
    """An already-present folder is left byte-identical (bytes and mtimes) and reported already."""
    env = T.Env()
    try:
        pack = build_pack(env, trio_specs())
        cache = os.path.join(env.tmp, "cache")
        run_install(pack, cache, env.lock)
        before = snapshot(cache)
        rc, lines = run_install(pack, cache, env.lock)
        after = snapshot(cache)
        last = last_line(lines)
        already = [ln for ln in lines if ln.startswith("PACKAGE ") and " already " in ln]
        good = (rc == 0 and before and before == after and len(already) == 3
                and last == "INTAKE-NPM-INSTALL tarballs=3 unpacked=0 already=3 refused=0 present=3/3 ok=True")
        return good, ["second run rc=%s last line: %s" % (rc, last),
                      "tree byte- and mtime-identical across the second run: %s (%d entries)" % (before == after, len(before)),
                      "lines reporting already: %d of 3" % len(already)]
    finally:
        env.close()


def arm_j():
    """An existing EMPTY folder at a destination is refused, not overwritten; the other destinations are not written."""
    env = T.Env()
    try:
        pack = build_pack(env, trio_specs())
        cache = os.path.join(env.tmp, "cache")
        blocked = dest_of(cache, *EXTRA)
        os.makedirs(blocked)
        rc, lines = run_install(pack, cache, env.lock)
        last = last_line(lines)
        still_empty = os.path.isdir(blocked) and os.listdir(blocked) == []
        others_absent = not os.path.exists(dest_of(cache, *T.UNSCOPED)) and not os.path.exists(dest_of(cache, *T.SCOPED))
        refused_line = any(ln.startswith("PACKAGE limbextra@0.4.2 refused") and "empty" in ln for ln in lines)
        good = rc == 1 and still_empty and others_absent and refused_line and last.endswith("ok=False")
        return good, ["empty destination: rc=%s refused=%s still empty=%s others not written=%s" % (
            rc, refused_line, still_empty, others_absent), "last line: %s" % last]
    finally:
        env.close()


def arm_k():
    """A run twice is idempotent: 3 unpacked, then already=3 with unpacked=0 and an unchanged tree."""
    env = T.Env()
    try:
        pack = build_pack(env, trio_specs())
        cache = os.path.join(env.tmp, "cache")
        rc1, lines1 = run_install(pack, cache, env.lock)
        rc2, lines2 = run_install(pack, cache, env.lock)
        first_ok = last_line(lines1) == "INTAKE-NPM-INSTALL tarballs=3 unpacked=3 already=0 refused=0 present=3/3 ok=True"
        second_ok = last_line(lines2) == "INTAKE-NPM-INSTALL tarballs=3 unpacked=0 already=3 refused=0 present=3/3 ok=True"
        good = rc1 == 0 and rc2 == 0 and first_ok and second_ok
        return good, ["first: %s" % last_line(lines1), "second: %s" % last_line(lines2)]
    finally:
        env.close()


def arm_l():
    """A lifecycle script is listed and never executed: the marker it would write is never created."""
    env = T.Env()
    try:
        marker = os.path.join(env.tmp, "postinstall-marker.txt")
        command = '%s -c "import pathlib; pathlib.Path(r\'%s\').write_text(\'ran\')"' % (sys.executable, marker)
        pack = build_pack(env, trio_specs(lifecycle_extra={"postinstall": command}),
                          lifecycle={T.UNSCOPED[0]: "postinstall writes a marker (synthetic probe), signed by the CTO"})
        cache = os.path.join(env.tmp, "cache")
        rc, lines = run_install(pack, cache, env.lock)
        pj = os.path.join(dest_of(cache, *T.UNSCOPED), "package.json")
        listed = False
        if os.path.isfile(pj):
            with open(pj, "r", encoding="utf-8") as fh:
                listed = json.load(fh).get("scripts", {}).get("postinstall") == command
        marker_absent = not os.path.exists(marker)
        good = rc == 0 and listed and marker_absent and last_line(lines).endswith("ok=True")
        return good, ["install rc=%s last line: %s" % (rc, last_line(lines)),
                      "postinstall present in the unpacked package.json (not run): %s" % listed,
                      "marker absent (the script never ran): %s" % marker_absent]
    finally:
        env.close()


def arm_m():
    """Control: a mutant that writes the folders with no package.json is read by the real precheck as 2 of 3 or fewer, exit 1."""
    env = T.Env()
    real_place = R._npm_place

    def mutant_place(item, target):
        parent = os.path.dirname(item["dest"])
        os.makedirs(parent, exist_ok=True)
        tmp = tempfile.mkdtemp(prefix=".intake-unpack-", dir=parent)
        R._npm_unpack_into(item["pack_path"], tmp)
        os.remove(os.path.join(tmp, "package.json"))
        os.rename(tmp, item["dest"])

    try:
        pack = build_pack(env, trio_specs())
        cache = os.path.join(env.tmp, "cache")
        R._npm_place = mutant_place
        try:
            run_install(pack, cache, env.lock)
        finally:
            R._npm_place = real_place
        rc, out = precheck(env.lock, cache)
        first = out[0] if out else ""
        count = int(first.split(" of ")[0]) if " of " in first else -1
        good = rc == 1 and 0 <= count <= 2
        return good, ["mutant (no package.json) read by the real precheck: rc=%s first line=%s" % (rc, first)]
    finally:
        R._npm_place = real_place
        env.close()


ARMS = [
    ("e_three_packages_land_unpacked_folders", arm_e),
    ("f_real_precheck_reads_3_of_3_and_0_of_3", arm_f),
    ("g_sha512_mismatch_refused_nothing_written", arm_g),
    ("h_dotdot_and_absolute_members_refused", arm_h),
    ("i_already_present_left_byte_identical", arm_i),
    ("j_empty_destination_refused_not_overwritten", arm_j),
    ("k_run_twice_idempotent", arm_k),
    ("l_lifecycle_listed_not_executed", arm_l),
    ("m_control_mutant_without_package_json_detected", arm_m),
]


def main():
    passed = 0
    for label, fn in ARMS:
        try:
            ok, details = fn()
        except Exception:  # an arm that cannot run is a failed arm
            ok, details = False, [traceback.format_exc(limit=4).strip()]
        for line in details:
            print("  " + line.encode("ascii", "backslashreplace").decode("ascii"))
        print(("PASS " if ok else "FAIL ") + label)
        passed += 1 if ok else 0
    ok_all = passed == len(ARMS)
    print("INTAKE-NPM-INSTALL-TEST arms=%d/%d ok=%s" % (passed, len(ARMS), ok_all))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
