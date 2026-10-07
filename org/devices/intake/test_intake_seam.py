#!/usr/bin/env python3
"""THE SEAM TEST (TO NFRA_CTLPLN.TO-CT-e-4, amendment 1): the four intake tools run as one on a synthetic wheel, through
their command lines, against a fake package index on 127.0.0.1. Six stages: fetch, check, release, pack (intake_fetch.py,
intake_check.py), verify, prove (intake_receive.py). Then three negative arms, each on a fresh copy of the good pack:
a wheel byte flipped, the check record edited to 'not_checked', the delivery text removed; each must be refused by verify.

Nothing leaves this machine: the only HTTP listener is the one this file starts on 127.0.0.1, and the only pip command is the
receiving tool's own (--no-index --no-deps --target <temporary dir>) on the synthetic wheel. The installed copy, the
antivirus answer and the signer are stand-ins reached through the tools' own environment variables (OPAL_INTAKE_ROOT,
OPAL_INTAKE_RECORDS, OPAL_INTAKE_SITE, OPAL_INTAKE_AV_JSON, OPAL_INTAKE_SIGNER_DIR) and AGENTBUS_DEVICE. No argument; the
repository root is derived from this file's own location. Standard library only.
LAST line: INTAKE-SEAM-TEST stages=<n> negative_arms=<k>/3 index_requests=<r> ok=<True|False>"""
import base64
import hashlib
import http.server
import io
import json
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import threading
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[3]
INTAKE = ROOT / "org" / "devices" / "intake"
NAME, VER, TAGS = "seamprobe", "1.2.3", ("py3", "none", "any")
FN = "%s-%s-%s-%s-%s.whl" % ((NAME, VER) + TAGS)
BATCH = "seam-run-1"
EXPECTED_REQUESTS = 4
DIST_INFO = "seamprobe-1.2.3.dist-info"


def rec_hash(data):
    return "sha256=" + base64.urlsafe_b64encode(hashlib.sha256(data).digest()).rstrip(b"=").decode("ascii")


def build_wheel():
    files = {
        "seamprobe/__init__.py": b"VALUE = 41 + 1\n",
        DIST_INFO + "/METADATA": b"Metadata-Version: 2.1\nName: seamprobe\nVersion: 1.2.3\n",
        DIST_INFO + "/WHEEL": b"Wheel-Version: 1.0\nGenerator: seam\nRoot-Is-Purelib: true\nTag: py3-none-any\n",
        DIST_INFO + "/top_level.txt": b"seamprobe\n",
    }
    record = "".join("%s,%s,%d\n" % (k, rec_hash(v), len(v)) for k, v in files.items()) + DIST_INFO + "/RECORD,,\n"
    files[DIST_INFO + "/RECORD"] = record.encode("ascii")
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for key, value in files.items():
            zf.writestr(zipfile.ZipInfo(key, (2020, 1, 1, 0, 0, 0)), value)
    return buf.getvalue(), files


WHEEL, FILES = build_wheel()
SHA = hashlib.sha256(WHEEL).hexdigest()
HITS = []


class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def reply(self, code, body=b""):
        self.send_response(code)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        HITS.append(self.path)
        base = "http://127.0.0.1:%d" % self.server.server_address[1]
        ent = {"filename": FN, "url": base + "/files/" + FN, "digests": {"sha256": SHA}, "size": len(WHEEL),
               "upload_time_iso_8601": "2025-01-10T00:00:00Z", "yanked": False, "requires_python": ">=3.8"}
        if self.path == "/pypi/%s/%s/json" % (NAME, VER):
            self.reply(200, json.dumps({"info": {"name": NAME, "version": VER}, "urls": [ent]}).encode("ascii"))
        elif self.path == "/pypi/%s/json" % NAME:
            years = (("1.0.0", "21"), ("1.1.0", "22"), ("1.2.0", "23"), ("1.2.2", "24"), (VER, "25"))
            rel = {v: [dict(ent, upload_time_iso_8601="20%s-01-10T00:00:00Z" % y)] for v, y in years}
            self.reply(200, json.dumps({"info": {"name": NAME}, "releases": rel}).encode("ascii"))
        elif self.path == "/files/" + FN:
            self.reply(200, WHEEL)
        else:
            self.reply(404)


def last_line(proc):
    lines = [x for x in (proc.stdout + proc.stderr).strip().splitlines() if x.strip()]
    return lines[-1] if lines else ""


def run_tool(env, script, args):
    cmd = [sys.executable, str(INTAKE / script)] + args
    return subprocess.run(cmd, cwd=str(ROOT), env=env, capture_output=True, text=True, timeout=100)


def build_stand_ins(tmp):
    """An installed copy of the same version (so checks 3 and 6 are exercised), an antivirus answer, a signer."""
    site = tmp / "site"
    for key, value in FILES.items():
        path = site / key
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(value)
    av = tmp / "av.json"
    av.write_text(json.dumps([{"displayName": "Seam Stand-in AV", "productState": 266240}]), encoding="ascii")
    signer = tmp / "signer"
    signer.mkdir()
    approved = tmp / "approved.txt"
    approved.write_text("%s==%s\n" % (NAME, VER), encoding="ascii")
    signed = signer / "BATCH_SIGNED.md"
    signed.write_text("batch %s\nfile %s\nsigned for the seam run only\n" % (BATCH, FN), encoding="ascii")
    env = dict(os.environ)
    env.update({"OPAL_INTAKE_ROOT": str(tmp / "intake-root"), "OPAL_INTAKE_RECORDS": str(tmp / "records"),
                "OPAL_INTAKE_SITE": str(site), "OPAL_INTAKE_AV_JSON": str(av), "OPAL_INTAKE_SIGNER_DIR": str(signer),
                "AGENTBUS_DEVICE": "laptop"})
    return env, approved, signed


def run_stages(tmp, base, env, approved, signed, pack):
    """Returns the list of (label, rc, passed, last line) for the six stages."""
    scratch = tmp / "scratch"
    plan = [
        ("fetch", "intake_fetch.py", ["fetch", "--batch", BATCH, "--name", NAME, "--version", VER, "--python-tag", TAGS[0],
                                      "--abi-tag", TAGS[1], "--platform-tag", TAGS[2], "--index-base", base],
         ["outcome=held"]),
        ("check", "intake_check.py", ["check", "--batch", BATCH, "--file", FN, "--approved-by", str(approved),
                                      "--signed-by", str(signed), "--scan-wait-seconds", "1"], ["verdict=checked"]),
        ("release", "intake_check.py", ["release", "--batch", BATCH, "--file", FN], ["released"]),
        ("pack", "intake_check.py", ["pack", "--batch", BATCH, "--out", str(pack)], ["INTAKE-PACK", "files=1"]),
        ("verify", "intake_receive.py", ["verify", "--from", str(pack)],
         ["wheels=1", "verified=1", "checked=1", "stray=0", "ok=True"]),
        ("prove", "intake_receive.py", ["prove", "--from", str(pack), "--scratch", str(scratch)],
         ["wheels=1", "installed=1", "imported=1", "refused=0", "ok=True"]),
    ]
    rows = []
    for label, script, args, want in plan:
        proc = run_tool(env, script, args)
        last = last_line(proc)
        good = proc.returncode == 0 and all(w in last for w in want)
        rows.append((label, proc.returncode, good, last))
        print("%-8s rc=%s %s | %s" % (label, proc.returncode, "OK " if good else "BAD", last[:230]))
        if not good:
            break
    return rows


def flip_wheel_byte(pack):
    path = pack / FN
    data = bytearray(path.read_bytes())
    data[len(data) // 2] ^= 0xFF
    path.write_bytes(bytes(data))


def edit_record_verdict(pack):
    path = pack / (FN + ".check.json")
    rec = json.loads(path.read_text(encoding="ascii"))
    rec["verdict"] = "not_checked"
    path.write_text(json.dumps(rec, indent=2) + "\n", encoding="ascii")


def remove_delivery(pack):
    (pack / (FN + ".delivery.txt")).unlink()


def run_negative_arms(tmp, env, good_pack):
    arms = (("wheel_byte_flipped", flip_wheel_byte), ("record_verdict_not_checked", edit_record_verdict),
            ("delivery_text_removed", remove_delivery))
    refused = 0
    for label, tamper in arms:
        copy = tmp / ("arm_" + label) / "pack"
        shutil.copytree(str(good_pack), str(copy))
        tamper(copy)
        proc = run_tool(env, "intake_receive.py", ["verify", "--from", str(copy)])
        last = last_line(proc)
        good = proc.returncode != 0 and "ok=False" in last
        refused += 1 if good else 0
        print("arm %-28s rc=%s %s | %s" % (label, proc.returncode, "REFUSED" if good else "NOT REFUSED", last[:200]))
    return refused


def main():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="seamtest_"))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = "http://127.0.0.1:%d" % srv.server_address[1]
    stages_ok = 0
    refused = 0
    try:
        env, approved, signed = build_stand_ins(tmp)
        pack = tmp / "pack"
        rows = run_stages(tmp, base, env, approved, signed, pack)
        stages_ok = sum(1 for row in rows if row[2])
        if len(rows) == 6 and stages_ok == 6:
            print("pack holds:", sorted(p.name for p in pack.iterdir()))
            refused = run_negative_arms(tmp, env, pack)
    finally:
        srv.shutdown()
        srv.server_close()
        shutil.rmtree(str(tmp), ignore_errors=True)
    requests = len(HITS)
    cleaned = not tmp.exists()
    if not cleaned:
        print("WARN: temporary folder not removed: %s" % tmp)
    ok = stages_ok == 6 and refused == 3 and requests == EXPECTED_REQUESTS and cleaned
    print("index requests seen on 127.0.0.1:", requests, HITS)
    print("INTAKE-SEAM-TEST stages=%d negative_arms=%d/3 index_requests=%d ok=%s" % (stages_ok, refused, requests, ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
