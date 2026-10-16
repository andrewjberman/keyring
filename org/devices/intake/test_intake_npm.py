#!/usr/bin/env python3
"""test_intake_npm.py -- the npm tarball limb of the intake route (CT-cc-1; CTO ruling 2026-10-16), proven against a LOOPBACK
registry. Nothing here contacts the public internet: every registry is a ThreadingHTTPServer this file starts on 127.0.0.1,
the public-host cases call the pure address policy and never a socket, and every tarball is synthetic (tarfile and gzip).

Arms (each prints PASS or FAIL with its detail):
  a  happy path, an unscoped and a scoped package: request filed and status read; fetch held; checks 1-8 as the limb defines them
  b  a name absent from the approval file is refused, a near-name (core@ against @babel/core@) too, with ZERO registry requests
  c  a dist.tarball on another host is refused with zero tarball requests; the public policy refuses a foreign host and admits
     registry.npmjs.org; --registry-base outside loopback is refused
  d  a tarball whose sha512 differs from the lockfile is refused at the digest check (the registry's integrity matches it)
  e  a tarball whose sha512 differs from the registry's dist.integrity is refused (the lockfile matches it)
  f  a missing --lockfile is a refusal (CLI: REFUSED, no record); the check function reads check 1 failed, never skipped
  g  a package.json naming another version fails identity (check 2)
  h  a postinstall script is LISTED; a .node member and an os/cpu restriction are NAMED (check 6), never executed
  i  check 8: a file with a lifecycle script or a native binary reads failed with only the batch line, and passed with its own lines
  j  an unsafe member name, a link leaving the package, an absolute member and a non-gzip file FAIL check 6 (nothing extracted)
  k  pack and verify round trip (tarballs=2 verified=2 checked=2 stray=0 ok=True); a tampered packed tarball is refused; the
     standalone lockfile mirror in intake_receive reads what intake_check reads
  l  the PyPI default is unchanged: a wheel flows as before (no ecosystem key in its records; the pypi argument errors stay)
  m  controls: a mutant that skips the lockfile comparison makes arm d fail (detected); the real code passes arm d

Standard library plus the intake tools; temporary folders only; ASCII output.
Last line: INTAKE-NPM arms=<k>/<n> ok=<True|False>
"""
import contextlib
import base64
import hashlib
import io
import json
import os
import shutil
import sys
import tarfile
import tempfile
import threading
import traceback
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import intake_check as C  # noqa: E402
import intake_fetch as F  # noqa: E402
import intake_receive as R  # noqa: E402
import intake_request as IR  # noqa: E402

SERIAL = "0.9.0_WK_NFRA_CTLPLN~147"
BATCH = "npm-limb-test"
UNSCOPED = ("limbprobe", "1.0.0")
SCOPED = ("@limbprobe/core", "7.29.7")
ENV_KEYS = ("OPAL_INTAKE_ROOT", "OPAL_INTAKE_RECORDS", "OPAL_INTAKE_AV_JSON", "OPAL_INTAKE_SITE", "OPAL_INTAKE_SIGNER_DIR",
            "OPAL_AGENT_SERIAL")


def sri(data):
    """The registry's integrity form of a byte string: sha512-<base64 of the digest>."""
    return "sha512-" + base64.b64encode(hashlib.sha512(data).digest()).decode("ascii")


def sha1_hex(data):
    return hashlib.sha1(data).hexdigest()


def make_tgz(members):
    """A gzip tar of synthetic members. A value is bytes (a regular file), or ('symlink', target) for a link."""
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tf:
        for name, value in members.items():
            info = tarfile.TarInfo(name)
            if isinstance(value, tuple) and value[0] == "symlink":
                info.type = tarfile.SYMTYPE
                info.linkname = value[1]
                tf.addfile(info)
            else:
                info.size = len(value)
                tf.addfile(info, io.BytesIO(value))
    return buf.getvalue()


def pkg_json(name, version, extra=None):
    doc = {"name": name, "version": version}
    doc.update(extra or {})
    return json.dumps(doc, sort_keys=True).encode("ascii")


def std_tgz(name, version, extra=None, more=None, pkg_version=None):
    members = {"package/package.json": pkg_json(name, pkg_version or version, extra),
               "package/index.js": b"module.exports = 1;\n"}
    members.update(more or {})
    return make_tgz(members)


def bun_lock_text(entries):
    """A bun TEXT lockfile in the real shape, with bun's trailing commas: "name": ["name@version", "", {deps}, "sha512-..."]."""
    rows = []
    for name, version, integ in entries:
        rows.append('    "%s": ["%s@%s", "", { "dependencies": { } }, "%s"],' % (name, name, version, integ))
    return ('{\n  "lockfileVersion": 1,\n  "configVersion": 1,\n  "workspaces": {\n    "": {\n'
            '      "name": "npm-limb-probe",\n      "dependencies": {\n        "@limbprobe/core": "7.29.7",\n      },\n'
            '    },\n  },\n  "packages": {\n' + "\n".join(rows) + "\n  }\n}\n")


class Registry:
    """A loopback npm registry: version documents and tarballs, keyed by the raw request path. Every request is counted."""

    def __init__(self):
        self.docs = {}
        self.blobs = {}
        self.requests = []
        reg = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, fmt, *args):
                return

            def do_GET(self):
                reg.requests.append(self.path)
                if self.path in reg.docs:
                    body, status = reg.docs[self.path], 200
                elif self.path in reg.blobs:
                    body, status = reg.blobs[self.path], 200
                else:
                    body, status = b"{}", 404
                self.send_response(status)
                self.send_header("Content-Type", "application/octet-stream")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.base = "http://127.0.0.1:%d" % self.server.server_address[1]
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def close(self):
        self.server.shutdown()
        self.server.server_close()

    def tarball_requests(self):
        return [p for p in self.requests if p.endswith(".tgz")]


class Env:
    """One arm's world: a temporary holding root, records folder, signer folder, stand-in antivirus answer and registry."""

    def __init__(self):
        self.tmp = tempfile.mkdtemp(prefix="intake_npm_")
        self.root = os.path.join(self.tmp, "root")
        self.records = os.path.join(self.tmp, "records")
        self.signer = os.path.join(self.tmp, "signer")
        self.site = os.path.join(self.tmp, "site")
        for d in (self.root, self.records, self.signer, self.site):
            os.makedirs(d)
        self.av = os.path.join(self.tmp, "av.json")
        with open(self.av, "w", encoding="ascii") as fh:
            json.dump([{"displayName": "Synthetic Antivirus (stand-in)", "productState": 266240}], fh)
        self.approved = os.path.join(self.tmp, "approved.txt")
        self.lock = os.path.join(self.tmp, "bun.lock")
        self.reg = Registry()
        self.saved = {k: os.environ.get(k) for k in ENV_KEYS}

    def close(self):
        self.reg.close()
        for k, v in self.saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        shutil.rmtree(self.tmp, ignore_errors=True)

    def environ(self):
        os.environ.update({"OPAL_INTAKE_ROOT": self.root, "OPAL_INTAKE_RECORDS": self.records,
                           "OPAL_INTAKE_AV_JSON": self.av, "OPAL_INTAKE_SITE": self.site,
                           "OPAL_INTAKE_SIGNER_DIR": self.signer, "OPAL_AGENT_SERIAL": SERIAL})

    def approve(self, lines):
        with open(self.approved, "w", encoding="ascii") as fh:
            fh.write("\n".join(lines) + "\n")

    def write_lock(self, entries):
        with open(self.lock, "w", encoding="ascii") as fh:
            fh.write(bun_lock_text(entries))

    def publish(self, name, version, data, reg_integrity=None, host_base=None):
        """Publish one version: the version document at /<name quoted, @ kept>/<version>, its tarball at the URL it names."""
        tar_path = "/%s/-/%s-%s.tgz" % (name, name.split("/")[-1], version)
        base = host_base or self.reg.base
        dist = {"tarball": base + tar_path, "integrity": reg_integrity or sri(data), "shasum": sha1_hex(data)}
        doc = {"name": name, "version": version, "dist": dist}
        key = "/%s/%s" % (urllib.parse.quote(name, safe="@"), urllib.parse.quote(version, safe=""))
        self.reg.docs[key] = json.dumps(doc).encode("ascii")
        self.reg.blobs[tar_path] = data
        return dist

    def fetch(self, name, version, registry_base=None, extra=()):
        self.environ()
        args = ["fetch", "--ecosystem", "npm", "--batch", BATCH, "--name", name, "--version", version,
                "--approved-by", self.approved, "--registry-base", registry_base or self.reg.base] + list(extra)
        out = io.StringIO()
        rc = None
        try:
            with contextlib.redirect_stdout(out):
                rc = F.main(args)
        except SystemExit as exc:
            rc = exc.code
        rec = self.fetch_record(name, version)
        return rc, rec, out.getvalue()

    def fetch_record(self, name, version):
        path = os.path.join(self.records, BATCH, F.npm_held_name(name, version) + ".fetch.json")
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)

    def held(self, name, version):
        return os.path.join(self.root, "holding", BATCH, F.npm_held_name(name, version))

    def signed_file(self, name, version, lines):
        path = os.path.join(self.signer, "signed-%s.md" % F.npm_held_name(name, version))
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        return path

    def check(self, name, version, signed_lines=None, lockfile=True):
        """The check CLI in npm mode. Returns (rc, the check record, stdout)."""
        self.environ()
        held = F.npm_held_name(name, version)
        args = ["check", "--batch", BATCH, "--file", held, "--approved-by", self.approved, "--ecosystem", "npm",
                "--scan-wait-seconds", "0"]
        if lockfile:
            args += ["--lockfile", self.lock]
        if signed_lines is not None:
            args += ["--signed-by", self.signed_file(name, version, signed_lines)]
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = C.main(args)
        return rc, self.check_record(name, version), out.getvalue()

    def check_record(self, name, version):
        path = os.path.join(self.records, BATCH, F.npm_held_name(name, version) + ".check.json")
        if not os.path.isfile(path):
            return None
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)


def signed_lines(name, version, waive=(4,), extra=()):
    held = F.npm_held_name(name, version)
    lines = ["# CTO check 8 -- batch %s" % BATCH, "CHECK 8 SIGNED -- release may proceed for this file.", held]
    for n in waive:
        lines.append("WAIVE %s check %d: the npm route reads no publish time (synthetic arm fixture)" % (held, n))
    lines.extend(extra)
    return lines


def verdicts(rec):
    return {c["n"]: c["verdict"] for c in rec["checks"]}


def ev(rec, n):
    return rec["checks"][n - 1]["evidence"]


def arm_a():
    """Happy path, unscoped and scoped: request and status, fetch held, checks 1-8 as the limb defines them."""
    env = Env()
    try:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc_f = IR.main(["file", "--root", env.root, "--name", SCOPED[0], "--version", SCOPED[1], "--needed-by", "t",
                            "--why-no-approved", "t", "--by", SERIAL, "--ecosystem", "npm"])
        filed = out.getvalue()
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            IR.main(["status", "--root", env.root, "--name", SCOPED[0], "--version", SCOPED[1], "--ecosystem", "npm"])
        status = out.getvalue()
        req_ok = rc_f == 0 and "package=@limbprobe/core@7.29.7" in filed and "PACKAGE @limbprobe/core@7.29.7 REQUESTED" in status
        details = ["request filed=%s status=%s" % (filed.strip(), status.strip())]
        good = req_ok
        for name, version in (UNSCOPED, SCOPED):
            data = std_tgz(name, version, extra={"description": "synthetic"})
            env.approve(["%s@%s" % (name, version)])
            dist = env.publish(name, version, data)
            env.write_lock([(name, version, dist["integrity"])])
            rc, fr, _o = env.fetch(name, version)
            held_ok = fr.get("outcome") == "held" and os.path.isfile(env.held(name, version))
            with open(env.held(name, version), "rb") as fh:
                disk = fh.read()
            lock_int = C.lock_integrities(C.load_bun_lock(env.lock), "%s@%s" % (name, version))
            both = sri(disk) == dist["integrity"] and lock_int == [sri(disk)]
            rc2, rec, _o2 = env.check(name, version, signed_lines=signed_lines(name, version))
            v = verdicts(rec) if rec else {}
            expect_v = {1: "passed", 2: "passed", 3: "not_applicable", 4: "failed", 5: "not_applicable", 6: "passed",
                        7: "passed", 8: "passed"}
            checks_ok = v == expect_v and rec.get("verdict") == "released-with-waiver" and rec.get("waived_checks") == [4]
            ok_one = held_ok and both and checks_ok
            good = good and ok_one
            details.append("%s@%s held=%s sha512_equal_registry_and_lockfile=%s verdicts=%s verdict=%s waived=%s" % (
                name, version, held_ok, both, json.dumps(v, sort_keys=True), rec.get("verdict") if rec else None,
                rec.get("waived_checks") if rec else None))
        return good, details
    finally:
        env.close()


def arm_b():
    """Refused before any socket: a name absent from the approval file, and a near-name, with zero registry requests."""
    env = Env()
    try:
        env.publish("limbprobe", "1.0.0", std_tgz("limbprobe", "1.0.0"))
        env.publish("core", "7.29.7", std_tgz("core", "7.29.7"))
        env.publish("@limbprobe/core", "7.29.7", std_tgz("@limbprobe/core", "7.29.7"))
        env.approve(["@limbprobe/core@7.29.7"])
        rc1, rec1, _o1 = env.fetch("limbprobe", "1.0.0")
        rc2, rec2, _o2 = env.fetch("core", "7.29.7")
        refused = rec1["outcome"] == "refused" and rec2["outcome"] == "refused"
        zero = env.reg.requests == [] and rec1["requests"] == [] and rec2["requests"] == []
        return refused and zero, ["absent: outcome=%s reason=%s" % (rec1["outcome"], rec1["reason"][:90]),
                                  "near-name core@7.29.7 vs @limbprobe/core@7.29.7: outcome=%s" % rec2["outcome"],
                                  "registry requests=%d" % len(env.reg.requests)]
    finally:
        env.close()


def arm_c():
    """A dist.tarball on another host: refused with zero tarball requests; the public policy and --registry-base limits."""
    env = Env()
    try:
        env.publish("limbprobe", "1.0.0", std_tgz("limbprobe", "1.0.0"), host_base="http://registry.elsewhere.invalid")
        env.approve(["limbprobe@1.0.0"])
        rc, rec, _o = env.fetch("limbprobe", "1.0.0")
        foreign = rec["outcome"] == "refused" and "outside the closed set" in rec["reason"]
        zero_tgz = env.reg.tarball_requests() == []
        # the public policy, pure (no socket): a foreign host is refused, registry.npmjs.org is admitted
        pol = F.Policy(F.NPM_PUBLIC_BASE, F.NPM_PUBLIC_HOSTS)
        refused_foreign = False
        try:
            pol.check("https://evil.example/x/-/x-1.0.0.tgz")
        except F.Refuse:
            refused_foreign = True
        admitted = True
        try:
            pol.check("https://registry.npmjs.org/limbprobe/-/limbprobe-1.0.0.tgz")
        except F.Refuse:
            admitted = False
        # --registry-base outside loopback is a refusal before any request
        rc3, rec3, _o3 = env.fetch("limbprobe", "1.0.0", registry_base="https://registry.npmjs.org")
        public_base_refused = (rec3["outcome"] == "refused" and "loopback" in rec3["reason"] and rec3["requests"] == []
                               and not any(r.get("url", "").startswith("https://registry.npmjs.org") for r in rec3["requests"]))
        good = foreign and zero_tgz and refused_foreign and admitted and public_base_refused
        return good, ["foreign dist.tarball: outcome=%s tarball_requests=%d" % (rec["outcome"],
                                                                              len(env.reg.tarball_requests())),
                      "public policy: foreign refused=%s registry.npmjs.org admitted=%s" % (refused_foreign, admitted),
                      "--registry-base https://registry.npmjs.org: outcome=%s" % rec3["outcome"]]
    finally:
        env.close()


def arm_d(mutant=False):
    """sha512 differs from the lockfile, the registry's integrity matches: refused at the digest check. Returns (ok, details)."""
    env = Env()
    orig = C.NPM_CHECKS
    try:
        name, version = UNSCOPED
        data = std_tgz(name, version)
        dist = env.publish(name, version, data)
        env.write_lock([(name, version, sri(b"a different tarball, not this one"))])
        env.approve(["%s@%s" % (name, version)])
        if mutant:
            def mutant_check_1(ctx):
                verdict, evidence = orig[0](ctx)
                if verdict == "failed" and all("lockfile" in p for p in evidence.get("problems", [])):
                    return "passed", evidence   # the mutant: the lockfile comparison is skipped
                return verdict, evidence
            C.NPM_CHECKS = [mutant_check_1] + list(orig[1:])
        rc, fr, _o = env.fetch(name, version)
        rc2, rec, _o2 = env.check(name, version, signed_lines=signed_lines(name, version))
        c1 = rec["checks"][0] if rec else {}
        problems = (c1.get("evidence") or {}).get("problems", [])
        good = c1.get("verdict") == "failed" and any("lockfile" in p for p in problems) and rec.get("verdict") == "not_checked"
        return good, ["registry integrity matches=%s lockfile differs=%s" % (dist["integrity"] == sri(data), True),
                      "check 1=%s problems=%s" % (c1.get("verdict"), "; ".join(problems)[:200])]
    finally:
        C.NPM_CHECKS = orig
        env.close()


def arm_e():
    """sha512 differs from the registry's dist.integrity, the lockfile matches: refused at the digest check."""
    env = Env()
    try:
        name, version = UNSCOPED
        data = std_tgz(name, version)
        env.publish(name, version, data, reg_integrity=sri(b"the registry describes some other bytes"))
        env.write_lock([(name, version, sri(data))])
        env.approve(["%s@%s" % (name, version)])
        env.fetch(name, version)
        rc, rec, _o = env.check(name, version, signed_lines=signed_lines(name, version))
        c1 = rec["checks"][0] if rec else {}
        problems = (c1.get("evidence") or {}).get("problems", [])
        good = c1.get("verdict") == "failed" and any("dist.integrity" in p for p in problems) and rec.get("verdict") == "not_checked"
        return good, ["check 1=%s problems=%s" % (c1.get("verdict"), "; ".join(problems)[:200])]
    finally:
        env.close()


def arm_f():
    """A missing --lockfile: CLI refusal with no record; the check function reads check 1 failed, never a skip."""
    env = Env()
    try:
        name, version = UNSCOPED
        env.publish(name, version, std_tgz(name, version))
        env.approve(["%s@%s" % (name, version)])
        env.fetch(name, version)
        rc, rec, out = env.check(name, version, signed_lines=signed_lines(name, version), lockfile=False)
        refused_cli = rc == 1 and "REFUSED" in out and "lockfile" in out and rec is None
        env.environ()
        cfg = C.Cfg()
        buf = io.StringIO()
        held = F.npm_held_name(name, version)
        crec, _line = C.run_check(cfg, BATCH, held, approved_by=env.approved, signed_by=None, scan_wait=0, out=buf,
                                  ecosystem="npm", lockfile=None)
        c1 = crec["checks"][0]
        good_fn = c1["verdict"] == "failed" and "refusal" in c1["evidence"]["summary"]
        return refused_cli and good_fn, ["CLI rc=%s record_written=%s" % (rc, rec is not None),
                                         "check 1 with no lockfile: %s" % c1["evidence"]["summary"][:120]]
    finally:
        env.close()


def arm_g():
    """package.json naming another version fails identity (check 2); the digests still agree."""
    env = Env()
    try:
        name, version = UNSCOPED
        data = std_tgz(name, version, pkg_version="1.0.1")
        dist = env.publish(name, version, data)
        env.write_lock([(name, version, dist["integrity"])])
        env.approve(["%s@%s" % (name, version)])
        env.fetch(name, version)
        rc, rec, _o = env.check(name, version, signed_lines=signed_lines(name, version))
        c2 = rec["checks"][1]
        good = c2["verdict"] == "failed" and "package.json version '1.0.1'" in c2["evidence"]["summary"]
        return good and verdicts(rec)[2] == "failed", ["check 2=%s summary=%s" % (c2["verdict"],
                                                                                   c2["evidence"]["summary"][:140])]
    finally:
        env.close()


def arm_h():
    """A postinstall script is LISTED; a .node member and an os/cpu restriction are NAMED. Nothing is executed."""
    env = Env()
    try:
        name, version = UNSCOPED
        data = std_tgz(name, version, extra={"scripts": {"postinstall": "node setup.js"}},
                       more={"package/build/probe.node": b"synthetic native bytes\n"})
        dist = env.publish(name, version, data)
        env.write_lock([(name, version, dist["integrity"])])
        env.approve(["%s@%s" % (name, version)])
        env.fetch(name, version)
        rc, rec, _o = env.check(name, version, signed_lines=signed_lines(name, version, waive=(4,)))
        e6 = ev(rec, 6)
        listed = [s["name"] for s in e6["lifecycle_scripts"]] == ["postinstall"]
        named = "package/build/probe.node" in e6["native_binaries"]
        name2, version2 = SCOPED
        data2 = std_tgz(name2, version2, extra={"os": ["win32"], "cpu": ["x64"]})
        dist2 = env.publish(name2, version2, data2)
        env.write_lock([(name, version, dist["integrity"]), (name2, version2, dist2["integrity"])])
        env.approve(["%s@%s" % (name, version), "%s@%s" % (name2, version2)])
        env.fetch(name2, version2)
        rc2, rec2, _o2 = env.check(name2, version2, signed_lines=signed_lines(name2, version2, waive=(4,)))
        restricted = any("os/cpu restriction" in n for n in ev(rec2, 6)["native_binaries"])
        not_run = e6["executed"] is False and verdicts(rec)[6] == "passed"
        return listed and named and restricted and not_run, [
            "postinstall listed=%s .node named=%s os/cpu named=%s" % (listed, named, restricted),
            "check 6 verdict=%s executed=%s" % (verdicts(rec)[6], e6["executed"])]
    finally:
        env.close()


def arm_i():
    """Check 8: a lifecycle script or a native binary needs ITS OWN line; the batch line alone reads failed."""
    env = Env()
    try:
        name, version = UNSCOPED
        data = std_tgz(name, version, extra={"scripts": {"postinstall": "node setup.js"}},
                       more={"package/build/probe.node": b"synthetic native bytes\n"})
        dist = env.publish(name, version, data)
        env.write_lock([(name, version, dist["integrity"])])
        env.approve(["%s@%s" % (name, version)])
        env.fetch(name, version)
        held = F.npm_held_name(name, version)
        only_batch = signed_lines(name, version)
        rc1, rec1, _o1 = env.check(name, version, signed_lines=only_batch)
        c8a = rec1["checks"][7]
        names_both = "NATIVE" in c8a["evidence"]["summary"] and "LIFECYCLE" in c8a["evidence"]["summary"]
        only_native = signed_lines(name, version, extra=["NATIVE %s: synthetic probe binary, signed by the CTO" % held])
        rc2, rec2, _o2 = env.check(name, version, signed_lines=only_native)
        c8b = rec2["checks"][7]
        missing_lifecycle = c8b["verdict"] == "failed" and "LIFECYCLE" in c8b["evidence"]["summary"]
        both = signed_lines(name, version, extra=[
            "NATIVE %s: synthetic probe binary, signed by the CTO" % held,
            "LIFECYCLE %s: postinstall runs setup.js, signed by the CTO" % held])
        rc3, rec3, _o3 = env.check(name, version, signed_lines=both)
        c8c = rec3["checks"][7]
        passed_with_lines = c8c["verdict"] == "passed" and rec3["verdict"] == "released-with-waiver"
        failed_alone = c8a["verdict"] == "failed" and names_both
        return failed_alone and missing_lifecycle and passed_with_lines, [
            "batch line only: check 8=%s" % c8a["verdict"],
            "NATIVE only: check 8=%s (LIFECYCLE missing)" % c8b["verdict"],
            "both lines: check 8=%s verdict=%s" % (c8c["verdict"], rec3["verdict"])]
    finally:
        env.close()


def arm_j():
    """Unsafe member names, a link leaving the package, an absolute member and a non-gzip file FAIL check 6."""
    env = Env()
    results = []
    try:
        cases = [
            ("1.0.1", make_tgz({"package/package.json": pkg_json("limbprobe", "1.0.1"), "package/../../escape.js": b"x"}),
             "unsafe"),
            ("1.0.2", make_tgz({"package/package.json": pkg_json("limbprobe", "1.0.2"),
                                "package/link": ("symlink", "../../../outside")}), "unsafe"),
            ("1.0.3", make_tgz({"package/package.json": pkg_json("limbprobe", "1.0.3"), "/etc/evil.js": b"x"}), "unsafe"),
            ("1.0.4", b"this is not a gzip file at all\n", "gzip"),
        ]
        good = True
        for version, data, kind in cases:
            env.publish("limbprobe", version, data)
            env.approve(["limbprobe@%s" % version])
            rc, fr, _o = env.fetch("limbprobe", version)
            if fr.get("outcome") != "held":
                good = False
                results.append("%s: not held (%s)" % (version, fr.get("outcome")))
                continue
            rc2, rec, _o2 = env.check("limbprobe", version, signed_lines=signed_lines("limbprobe", version))
            c6 = rec["checks"][5]
            hit = c6["verdict"] == "failed" and ((kind == "unsafe" and c6["evidence"]["unsafe_member_names"]) or
                                                 (kind == "gzip" and "not a readable gzip tar" in c6["evidence"]["summary"]))
            good = good and bool(hit) and rec["verdict"] == "not_checked"
            results.append("%s (%s): check 6=%s unsafe=%s" % (version, kind, c6["verdict"],
                                                              c6["evidence"]["unsafe_member_names"]))
        scratch_left = os.path.exists(os.path.join(env.tmp, "root", "release"))
        return good and not scratch_left, results + ["nothing released (no release folder): %s" % (not scratch_left)]
    finally:
        env.close()


def arm_k():
    """Pack and verify round trip; a tampered packed tarball is refused; the lockfile mirror reads what the check reads."""
    env = Env()
    try:
        names = [UNSCOPED, SCOPED]
        entries = []
        for name, version in names:
            data = std_tgz(name, version)
            dist = env.publish(name, version, data)
            entries.append((name, version, dist["integrity"]))
        env.write_lock(entries)
        env.approve(["%s@%s" % nv for nv in names])
        for name, version in names:
            env.fetch(name, version)
            rc, rec, _o = env.check(name, version, signed_lines=signed_lines(name, version))
            if rec.get("verdict") != "released-with-waiver":
                return False, ["check of %s@%s read %s" % (name, version, rec.get("verdict"))]
            env.environ()
            with contextlib.redirect_stdout(io.StringIO()):
                C.main(["release", "--batch", BATCH, "--file", F.npm_held_name(name, version), "--ecosystem", "npm"])
        pack = os.path.join(env.tmp, "pack")
        env.environ()
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc_p = C.main(["pack", "--batch", BATCH, "--out", pack, "--ecosystem", "npm"])
        pack_ok = rc_p == 0 and os.path.isfile(os.path.join(pack, "MANIFEST.json"))
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc_v = R.main(["verify", "--from", pack, "--ecosystem", "npm", "--lockfile", env.lock])
        last = out.getvalue().strip().splitlines()[-1]
        verify_ok = rc_v == 0 and last == "INTAKE-VERIFY pack=pack tarballs=2 verified=2 checked=2 stray=0 ok=True"
        # a tampered packed tarball: the manifest sha no longer matches, and the tarball no longer matches its lockfile entry
        tgz = os.path.join(pack, F.npm_held_name(*UNSCOPED))
        with open(tgz, "ab") as fh:
            fh.write(b"tamper")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc_t = R.main(["verify", "--from", pack, "--ecosystem", "npm", "--lockfile", env.lock])
        tamper_last = out.getvalue().strip().splitlines()[-1]
        tamper_ok = rc_t == 1 and tamper_last.endswith("ok=False")
        # the standalone mirror in intake_receive reads the lockfile as intake_check does
        mirror_ok = (R.load_bun_lock(env.lock) == C.load_bun_lock(env.lock)
                     and all(R.lock_integrities(R.load_bun_lock(env.lock), "%s@%s" % (n, v))
                             == C.lock_integrities(C.load_bun_lock(env.lock), "%s@%s" % (n, v)) for n, v in names))
        good = pack_ok and verify_ok and tamper_ok and mirror_ok
        return good, ["pack rc=%s manifest=%s" % (rc_p, pack_ok), "verify last line: %s" % last,
                      "tampered tarball verify rc=%s last line: %s" % (rc_t, tamper_last),
                      "lockfile mirror parity=%s" % mirror_ok]
    finally:
        env.close()


def arm_l():
    """The PyPI default is unchanged: a wheel flows as before, its records carry no ecosystem key, and argparse still
    refuses a pypi fetch without its tags."""
    tmp = tempfile.mkdtemp(prefix="intake_npm_pypi_")
    saved = {k: os.environ.get(k) for k in ENV_KEYS}
    try:
        root, records, signer = (os.path.join(tmp, d) for d in ("root", "records", "signer"))
        site = os.path.join(tmp, "site")
        for d in (root, records, signer, site):
            os.makedirs(d)
        av = os.path.join(tmp, "av.json")
        with open(av, "w", encoding="ascii") as fh:
            json.dump([{"displayName": "Synthetic Antivirus (stand-in)", "productState": 266240}], fh)
        cfg = C.Cfg(root=root, records=records, av_json=av, sites=[site], signer_dir=signer)
        hold = cfg.holding(BATCH)
        os.makedirs(hold)
        wheel = C.build_synthetic_wheel(os.path.join(str(hold), C.syn_file_name()))
        C.write_fetch_record(cfg, BATCH, wheel)
        approved = os.path.join(tmp, "approved.txt")
        with open(approved, "w", encoding="ascii") as fh:
            fh.write("%s==%s\n" % (C.SYN_NAME, C.SYN_VERSION))
        buf = io.StringIO()
        rec, line = C.run_check(cfg, BATCH, wheel.name, approved_by=approved, signed_by=None, scan_wait=0, out=buf)
        pypi_shape = ("ecosystem" not in rec and "approved_line_sought" in rec["checks"][1]["evidence"]
                      and rec["checks"][0]["verdict"] == "passed" and rec["checks"][1]["verdict"] == "passed"
                      and rec["verdict"] == "not_checked")
        # the argparse error of a pypi fetch without its tags is unchanged (exit 2 from argparse)
        err = io.StringIO()
        exit_code = None
        try:
            with contextlib.redirect_stderr(err):
                F.main(["fetch", "--batch", BATCH, "--name", "x", "--version", "1", "--approved-by", approved])
        except SystemExit as exc:
            exit_code = exc.code
        argparse_ok = exit_code == 2 and "--python-tag" in err.getvalue()
        return pypi_shape and argparse_ok, ["pypi check: verdict=%s c1=%s c2=%s" % (
            rec["verdict"], rec["checks"][0]["verdict"], rec["checks"][1]["verdict"]),
            "pypi fetch with no tags: exit=%s stderr names --python-tag=%s" % (exit_code, "--python-tag" in err.getvalue()),
            "record line: %s" % line]
    finally:
        for k, v in saved.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v
        shutil.rmtree(tmp, ignore_errors=True)


def arm_m():
    """Controls: the real code passes arm d; a mutant that skips the lockfile comparison makes arm d fail (is detected)."""
    real_ok, _d = arm_d(mutant=False)
    mutant_ok, _md = arm_d(mutant=True)
    detected = not mutant_ok
    return real_ok and detected, ["real code arm d=%s" % real_ok,
                                  "mutant (lockfile comparison skipped) arm d=%s detected=%s" % (mutant_ok, detected)]


ARMS = [
    ("a_happy_path_unscoped_and_scoped", arm_a),
    ("b_unapproved_name_zero_requests", arm_b),
    ("c_foreign_tarball_host_refused", arm_c),
    ("d_tarball_differs_from_lockfile", lambda: arm_d(False)),
    ("e_tarball_differs_from_registry_integrity", arm_e),
    ("f_missing_lockfile_refused", arm_f),
    ("g_package_json_identity", arm_g),
    ("h_lifecycle_listed_native_named", arm_h),
    ("i_check8_needs_own_lines", arm_i),
    ("j_unsafe_member_and_non_gzip", arm_j),
    ("k_pack_verify_round_trip", arm_k),
    ("l_pypi_default_unchanged", arm_l),
    ("m_controls_mutant_detected", arm_m),
]


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
    print("INTAKE-NPM arms=%d/%d ok=%s" % (passed, total, ok_all))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
