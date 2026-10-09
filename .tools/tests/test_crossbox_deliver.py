#!/usr/bin/env python3
"""test_crossbox_deliver.py -- NFRA_GATSCP GS-e-3: crossbox delivery is gated on origin, an order to another box opens a file,
and a manager sends what is admitted.

Everything runs in a throwaway directory: a work repo with a BARE origin beside it, a copy of the device register, and a fake
send command. No network, no real bus, nothing outside the temp dir is written. It runs the tool at its own path
(.tools/crossbox-call.py) as a subprocess with --root pointing at the throwaway repo.

LAST line:  XBOX-DELIVER ok=<True|False> cases=<passed>/<total>
"""
from __future__ import annotations

import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL_ROOT = HERE.parent.parent
TOOL = TOOL_ROOT / ".tools" / "crossbox-call.py"
REGISTER = TOOL_ROOT / "org" / "devices" / "DEVICES.json"
MSTR = "0.0.0_AB_MSTR~DELL1"
WORKER = "0.9.0_WK_NFRA_GATSCP~4"
ISSUER = "2.0.0_SA_COO~N1"
UTC_RE = re.compile(r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
GIT_ID = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid", "GIT_COMMITTER_NAME": "t",
          "GIT_COMMITTER_EMAIL": "t@example.invalid"}


def clean_env(extra=None) -> dict:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_") and k not in (
        "OPAL_AGENT_SERIAL", "CLAUDE_CODE_SESSION_ID", "CROSSBOX_SEND_CMD", "OPAL_DEVICE_REGISTER", "AGENTBUS_DEVICE")}
    env.update(GIT_ID)
    env.update(extra or {})
    return env


def git(cwd, *args, check=True):
    p = subprocess.run(["git", "-c", "core.hooksPath=" + os.devnull, "-c", "commit.gpgsign=false", "-c", "core.autocrlf=false",
                        "-C", str(cwd), *args], capture_output=True, text=True, encoding="utf-8", errors="replace",
                       env=clean_env(), timeout=60)
    if check and p.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), p.stderr.strip()[:200]))
    return p.stdout.strip()


def rmtree_force(path) -> None:
    def onerr(func, target, _exc):
        os.chmod(target, stat.S_IWRITE)
        func(target)
    shutil.rmtree(path, onerror=onerr)


class World:
    def __init__(self, tmp: Path):
        self.tmp = tmp
        self.origin = tmp / "origin.git"
        self.box = tmp / "box"
        self.register = tmp / "DEVICES.json"
        shutil.copy(REGISTER, self.register)
        subprocess.run(["git", "init", "-q", "--bare", str(self.origin)], check=True, capture_output=True, env=clean_env())
        self.box.mkdir()
        git(self.box, "init", "-q")
        git(self.box, "remote", "add", "origin", str(self.origin))
        self.calls = tmp / "send_calls.log"
        self.fake = tmp / "fake_send.py"
        self.fake.write_text(
            "import sys\n"
            "open(%r, 'a', encoding='utf-8').write(repr(sys.argv[1:]) + '\\n')\n"
            "print('SENT to ' + sys.argv[1] + ': MessageId=0a1b2c3d-0000-4000-8000-0000000000aa')\n" % self.calls.as_posix(),
            encoding="utf-8")

    def write(self, rel: str, text: str) -> None:
        p = self.box / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8", newline="\n")

    def commit(self, *rels) -> None:
        git(self.box, "add", "--", *rels)
        git(self.box, "commit", "-q", "-m", "step")

    def push(self) -> None:
        git(self.box, "push", "-q", "origin", "HEAD:refs/heads/main")

    def run(self, *args, serial=None, send_cmd=None, extra=None):
        extra_env = {"OPAL_DEVICE_REGISTER": str(self.register)}
        if serial:
            extra_env["OPAL_AGENT_SERIAL"] = serial
        if send_cmd:
            extra_env["CROSSBOX_SEND_CMD"] = send_cmd
        extra_env.update(extra or {})
        p = subprocess.run([sys.executable, str(TOOL), "--root", str(self.box), "--device", "laptop", *args], capture_output=True,
                           text=True, encoding="utf-8", errors="replace", env=clean_env(extra_env), timeout=120)
        return p.returncode, (p.stdout + p.stderr)

    def files(self) -> list:
        d = self.box / "org" / "devices" / "crossbox"
        return sorted(d.glob("XB-*.json")) if d.is_dir() else []

    def doc(self, xb_id: str) -> dict:
        return json.loads((self.box / "org" / "devices" / "crossbox" / (xb_id + ".json")).read_text(encoding="utf-8"))

    def send_calls(self) -> list:
        return self.calls.read_text(encoding="utf-8").splitlines() if self.calls.is_file() else []


def order_text(num: str, to: str) -> str:
    return ("# TO NFRA_GATSCP.TO-X-%s -- a throwaway order | with a pipe\n\n<to_id>NFRA_GATSCP.TO-X-%s</to_id>\n<issued_to>%s</issued_to>\n"
            "<issued_by>%s</issued_by>\n<status>pending</status>\n" % (num, num, to, ISSUER))


def main() -> int:
    results = []

    def rec(name, ok, detail=""):
        results.append((name, bool(ok), str(detail).replace("\n", " | ")[:220]))

    tmp = Path(tempfile.mkdtemp(prefix="xbox-deliver-"))
    try:
        w = World(tmp)
        w.write("docs/body.md", "a body\n")
        w.write("orders/to_sitez.md", order_text("1", "0.7.0_AE_CloudOps~ZQ"))
        w.write("orders/to_local.md", order_text("2", "0.7.0_AE_CloudOps~Q1"))
        w.write("orders/to_override.md", order_text("3", "0.7.0_AE_CloudOps~Q1"))
        w.commit("docs/body.md", "orders/to_sitez.md", "orders/to_local.md", "orders/to_override.md")

        # (a) line: refused while local-only, admitted after the push (difference control)
        rc, out = w.run("open", "--kind", "ORDER", "--to-device", "sitez", "--to-serial", "0.7.0_AE_CloudOps~ZQ", "--from-serial", ISSUER,
                        "--subject", "pushed item", "--body", "docs/body.md")
        m = re.search(r"OPENED (XB-\d{8}T\d{6}Z-[0-9a-f]{4})", out)
        xb1 = m.group(1) if m else ""
        rec("a0-open-writes-the-crossbox-file", rc == 0 and bool(xb1), out)
        w.commit("org/devices/crossbox/%s.json" % xb1)
        rc, out = w.run("line", "--id", xb1)
        rec("a1-line-refused-while-the-commit-is-local-only", rc == 3 and "REFUSED: commit " in out and "is not on origin yet" in out, "rc=%d %s" % (rc, out))
        w.push()
        rc, out = w.run("line", "--id", xb1)
        rec("a2-line-admitted-after-the-push-to-origin", rc == 0 and out.startswith("CROSSBOX %s ORDER for 0.7.0_AE_CloudOps~ZQ" % xb1)
            and re.search(r" @[0-9a-f]{7,40}$", out.strip()) is not None, "rc=%d %s" % (rc, out))

        # (b) issue
        rc, out = w.run("issue", "--order", "orders/to_sitez.md")
        m = re.search(r"^XBOX-ISSUE opened (XB-\d{8}T\d{6}Z-[0-9a-f]{4}) sitez 0\.7\.0_AE_CloudOps~ZQ$", out, re.M)
        xb2 = m.group(1) if m else ""
        d = w.doc(xb2) if xb2 else {}
        rec("b1-issue-to-a-Z-lane-serial-opens-a-file-to-sitez", rc == 0 and bool(xb2) and d.get("to_device") == "sitez" and d.get("kind") == "ORDER"
            and d.get("from_serial") == ISSUER and d.get("to_serial") == "0.7.0_AE_CloudOps~ZQ" and d.get("body_path") == "orders/to_sitez.md"
            and d.get("subject", "").startswith("NFRA_GATSCP.TO-X-1 -- a throwaway order / with a pipe"), "rc=%d %s %s" % (rc, out, d))
        before = len(w.files())
        rc, out = w.run("issue", "--order", "orders/to_local.md")
        rec("b2-issue-to-a-serial-with-no-lane-letter-is-local-and-opens-nothing", rc == 0 and "XBOX-ISSUE local 0.7.0_AE_CloudOps~Q1" in out
            and "opened" not in out and len(w.files()) == before, "rc=%d %s files %d->%d" % (rc, out, before, len(w.files())))
        rc, out = w.run("issue", "--order", "orders/to_override.md", "--to-device", "dell2")
        rec("b3-issue-with-to-device-overrides-the-lane-rule", rc == 0 and re.search(r"^XBOX-ISSUE opened XB-\S+ dell2 0\.7\.0_AE_CloudOps~Q1$", out, re.M) is not None
            and len(w.files()) == before + 1, "rc=%d %s" % (rc, out))
        w.write("orders/uncommitted.md", order_text("4", "0.7.0_AE_CloudOps~ZQ"))
        rc, out = w.run("issue", "--order", "orders/uncommitted.md")
        rec("b4-issue-refuses-an-uncommitted-order", rc == 3 and "REFUSED" in out and len(w.files()) == before + 1, "rc=%d %s" % (rc, out))

        # (c) send-pending: xb1 is pushed (admitted); xb2 is committed locally only (held); the b3 file is uncommitted (held)
        w.commit("org/devices/crossbox/%s.json" % xb2)
        fake = "%s %s" % (Path(sys.executable).as_posix(), w.fake.as_posix())
        rc, out = w.run("send-pending", serial=WORKER, send_cmd=fake)
        rec("c1-send-pending-refused-for-a-non-MSTR-serial-and-records-nothing", rc == 3 and "REFUSED" in out and w.doc(xb1)["sent"]["bus_message_id"] is None
            and not w.send_calls(), "rc=%d %s calls=%d" % (rc, out, len(w.send_calls())))
        rc, out = w.run("send-pending", send_cmd=fake)
        rec("c2-send-pending-refused-with-no-acting-serial", rc == 3 and "REFUSED" in out and not w.send_calls(), "rc=%d %s" % (rc, out))
        rc, out = w.run("send-pending", "--dry-run", serial=MSTR, send_cmd=fake)
        rec("c3-dry-run-sends-nothing-and-says-what-it-would-send", rc == 0 and ("WOULD SEND %s to sitez" % xb1) in out and ("HELD %s " % xb2) in out
            and not w.send_calls() and w.doc(xb1)["sent"]["bus_message_id"] is None, "rc=%d %s" % (rc, out))
        rc, out = w.run("send-pending", serial=MSTR, send_cmd=fake)
        d1, d2 = w.doc(xb1), w.doc(xb2)
        calls = w.send_calls()
        rec("c4-send-pending-sends-the-pushed-item-and-records-sent-with-a-UTC-time",
            rc == 0 and d1["sent"]["bus_message_id"] == "0a1b2c3d-0000-4000-8000-0000000000aa" and bool(UTC_RE.match(str(d1["sent"]["at"])))
            and len(calls) == 1 and ("'sitez', '%s', 'CROSSBOX %s ORDER for" % (ISSUER, xb1)) in calls[0], "rc=%d %s sent=%s calls=%s" % (rc, out, d1["sent"], calls))
        rec("c5-send-pending-holds-the-local-only-item-and-records-nothing-for-it", ("HELD %s " % xb2) in out and "is not on origin yet" in out
            and d2["sent"] == {"at": None, "bus_message_id": None}, "%s sent=%s" % (out, d2["sent"]))
        rc, out = w.run("send-pending", serial=MSTR, send_cmd=fake)
        rec("c6-a-second-run-does-not-resend-the-sent-item", rc == 0 and len(w.send_calls()) == 1 and "WOULD" not in out and ("SENT %s" % xb1) not in out, "rc=%d %s" % (rc, out))
        # the session serial file is the fallback for the acting serial
        sess = w.box / "org" / "mcp" / "sessions"
        sess.mkdir(parents=True)
        (sess / "s1.serial").write_text(MSTR + "\n", encoding="utf-8")
        rc, out = w.run("send-pending", "--dry-run", extra={"CLAUDE_CODE_SESSION_ID": "s1"})
        rec("c7-the-session-serial-file-is-the-fallback-acting-serial", rc == 0 and "SEND-PENDING DRY-RUN" in out, "rc=%d %s" % (rc, out))

        # (a3) the body's own commit must be on origin too: edit the body, commit locally, push nothing
        w.commit("org/devices/crossbox/%s.json" % xb1)   # the recorded `sent`
        w.push()
        w.write("docs/body.md", "a body, edited\n")
        w.commit("docs/body.md")
        rc, out = w.run("line", "--id", xb1)
        rec("a3-line-refused-when-only-the-body-commit-is-local", rc == 3 and "is not on origin yet" in out and "docs/body.md" in out, "rc=%d %s" % (rc, out))
        w.push()
        rc, out = w.run("line", "--id", xb1)
        rec("a4-line-admitted-once-the-body-commit-is-pushed", rc == 0 and out.startswith("CROSSBOX %s" % xb1), "rc=%d %s" % (rc, out))
    except Exception as exc:   # a harness that cannot run is a failed test, never a pass
        rec("harness-ran", False, "%s: %s" % (type(exc).__name__, exc))
    finally:
        rmtree_force(tmp)
    for name, ok, detail in results:
        print("%s %s%s" % ("ok  " if ok else "FAIL", name, "" if ok or not detail else "  -- " + detail))
    good = sum(1 for _, ok, _ in results if ok)
    allok = bool(results) and good == len(results)
    print("XBOX-DELIVER ok=%s cases=%d/%d" % (allok, good, len(results)))
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main())
