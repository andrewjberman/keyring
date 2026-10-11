"""MDPF_HEALGAP round 3, HG-t-11 criterion (b): the opal-bd-asset-dim-download SSM document skips the download on a
complete day and runs it on anything else (CTO ruling 3411: option (d), the guard lives in the document).

  --ssm [DOC]   Runs the document's own shell, with the instance's tools stubbed, in two arms:
                  GUARD READ OK  (the stubbed head_object exits 0)  -> the pull is NOT started, the shutdown IS armed, rc 0.
                  GUARD READ FAILED (the stubbed read exits 1 or 2) -> the pull IS started (a failed read is never taken
                                                                      as 'exists').
                Also: the document is valid JSON and the guard sits AFTER the staging copies and BEFORE the pull.
                Last line: SSMGUARD-OK or SSMGUARD-BAD <reasons>. At the base (no guard) this prints SSMGUARD-BAD.

Stubs (on PATH ahead of the real tools): aws, runuser, shutdown, python3 (exit code taken from $STUB_GUARD_RC when its
argument text contains head_object; prints a date when it contains prev_trading_day), chown. The script's
`cd /opt/bd-exporter` is rewritten to a temp dir. Nothing touches AWS.
"""
from __future__ import annotations

import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

DOC = Path(os.environ.get("HG_T11_DOC") or "infra/aws/ssm/opal-bd-asset-dim-download.json")


def _bash() -> str:
    for cand in (shutil.which("bash"), r"C:\Program Files\Git\bin\bash.exe", "/bin/bash"):
        if cand and Path(cand).exists():
            return cand
    return "bash"


def _stub(d: Path, name: str, body: str) -> None:
    p = d / name
    p.write_text("#!/bin/bash\n" + body + "\n", encoding="utf-8", newline="\n")
    p.chmod(p.stat().st_mode | stat.S_IEXEC)


def _arm(lines: list[str], guard_rc: int) -> dict:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        work, bindir, calls = root / "work", root / "bin", root / "calls.log"
        work.mkdir()
        bindir.mkdir()
        calls.write_text("", encoding="utf-8")
        _stub(bindir, "aws", 'echo "AWS $*" >> "$CALLS"; exit 0')
        _stub(bindir, "runuser",
              'case "$*" in\n'
              '  *hg_guard.py*) echo "GUARD-READ rc=$STUB_GUARD_RC" >> "$CALLS"; exit "$STUB_GUARD_RC";;\n'
              'esac\n'
              'echo "RUNUSER $*" >> "$CALLS"; echo "OUTPUT_KEY=s3://opal-data-bd/bronze/stub.parquet"; exit 0')
        _stub(bindir, "shutdown", 'echo "SHUTDOWN $*" >> "$CALLS"; exit 0')
        _stub(bindir, "chown", "exit 0")
        _stub(bindir, "python3",
              'case "$*" in\n'
              '  *prev_trading_day*) echo "10/09/2026"; exit 0;;\n'
              'esac\nexit 0')
        script = "\n".join(lines)
        script = script.replace("cd /opt/bd-exporter", 'cd "$WORK"')
        script = script.replace("chown -R ec2-user:ec2-user /opt/bd-exporter", "true")
        path = root / "run.sh"
        path.write_text(script + "\n", encoding="utf-8", newline="\n")
        env = dict(os.environ, WORK=str(work).replace("\\", "/"), CALLS=str(calls).replace("\\", "/"),
                   STUB_GUARD_RC=str(guard_rc), PATH=str(bindir).replace("\\", "/") + os.pathsep + os.environ.get("PATH", ""))
        r = subprocess.run([_bash(), str(path).replace("\\", "/")], env=env, capture_output=True, text=True, timeout=90)
        log = calls.read_text(encoding="utf-8")
        return {"rc": r.returncode, "calls": log, "out": r.stdout + r.stderr}


def ssm() -> int:
    if not DOC.is_file():
        print(f"SSMGUARD-BAD no document {DOC}")
        return 1
    try:
        doc = json.loads(DOC.read_text(encoding="utf-8"))
        lines = doc["mainSteps"][0]["inputs"]["runCommand"]
    except Exception as exc:  # noqa: BLE001
        print(f"SSMGUARD-BAD document does not parse as the expected SSM shape: {type(exc).__name__}: {exc}")
        return 1
    bad = []
    pull_i = next((i for i, ln in enumerate(lines) if "pull_bd_asset_dim_rest.py pull" in ln), None)
    stage_i = max((i for i, ln in enumerate(lines) if "_asset_dim_rest_pin.py" in ln and "aws s3 cp" in ln), default=None)
    guard_i = next((i for i, ln in enumerate(lines) if "hg_guard.py" in ln and "runuser" in ln), None)
    body = "\n".join(lines)
    if guard_i is not None and "head_object" not in body:
        bad.append("the guard script never calls head_object")
    if pull_i is None or stage_i is None:
        bad.append("document lost its pull or its staging lines")
    elif guard_i is None:
        bad.append("no 'runuser ... hg_guard.py' guard line")
    elif not (stage_i < guard_i < pull_i):
        bad.append(f"guard line {guard_i} is not between staging ({stage_i}) and the pull ({pull_i})")
    if bad:
        print("SSMGUARD-BAD " + "; ".join(bad))
        return 1

    def _pull_started(calls: str) -> bool:
        # the PULL is a `runuser ... pull_bd_asset_dim_rest.py pull` call; the staging `aws s3 cp` lines name the same
        # file and are present in every arm, so a bare substring test cannot tell skip from run (worker ~8, row W8-S1).
        return any(ln.startswith("RUNUSER") and "pull_bd_asset_dim_rest.py pull" in ln for ln in calls.splitlines())

    skip = _arm(lines, 0)
    if _pull_started(skip["calls"]):
        bad.append("guard read OK but the pull still ran")
    if "SHUTDOWN" not in skip["calls"]:
        bad.append("guard read OK but the shutdown was not armed (the instance would be stranded)")
    if skip["rc"] != 0:
        bad.append(f"guard read OK, script rc={skip['rc']}, want 0")
    for rc in (1, 2):
        run = _arm(lines, rc)
        if not _pull_started(run["calls"]):
            bad.append(f"guard read FAILED (rc {rc}) but the pull did not run (a failed read was taken as 'exists')")
    if bad:
        print("SSMGUARD-BAD " + "; ".join(bad))
        return 1
    print("SSMGUARD-OK guard between staging and pull; exists -> skip + shutdown armed; read failed (rc 1,2) -> download runs")
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--ssm"]:
        if len(a) > 1:
            DOC = Path(a[1])
        sys.exit(ssm())
    print(__doc__)
    sys.exit(2)
