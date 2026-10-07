"""Round 8 (~M1) shared helper for the three old-list-writer checks (SC-e-35, SC-e-36, SC-e-37).

Imported by r10_bd_old_list_writers_check.py, r10_cot_old_list_writer_check.py and r10_inf_old_list_writer_check.py.
It edits nothing and calls no AWS service: each script under test runs with invalid credentials and an AWS endpoint
that refuses every connection (127.0.0.1:9), so a script that reaches AWS fails instead of writing.

A retired writer passes when, run as `python <script> --upload` from its own folder, it exits with code 3 and prints a
line starting `RETIRED:` before any AWS or model call.
"""
import os
import re
import subprocess
import sys
import tempfile

RETIRED_RC = 3
TOKEN_RE_CACHE = {}


def repo_root():
    here = os.path.abspath(os.path.dirname(__file__))
    out = subprocess.run(["git", "-C", here, "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=False)
    return out.stdout.strip()


def dead_aws_env():
    env = dict(os.environ)
    for k in list(env):
        if k.startswith(("AWS_", "OPENAI")):
            env.pop(k)
    tmp = tempfile.mkdtemp(prefix="r10_noaws_")
    env.update({
        "AWS_ACCESS_KEY_ID": "AKIAR10RETIREDCHECK0",
        "AWS_SECRET_ACCESS_KEY": "r10-retired-check-not-a-key",
        "AWS_DEFAULT_REGION": "us-east-1",
        "AWS_CONFIG_FILE": os.path.join(tmp, "config"),
        "AWS_SHARED_CREDENTIALS_FILE": os.path.join(tmp, "credentials"),
        "AWS_EC2_METADATA_DISABLED": "true",
        "AWS_ENDPOINT_URL": "http://127.0.0.1:9",
        "AWS_MAX_ATTEMPTS": "1",
        "AWS_RETRY_MODE": "standard",
        "OPENAI_API_KEY": "",
        "PYTHONIOENCODING": "utf-8",
    })
    return env


def run_retired(script_path):
    """Return (ok, detail) for one script run as `--upload`."""
    if not os.path.exists(script_path):
        return False, "absent"
    try:
        r = subprocess.run([sys.executable, os.path.basename(script_path), "--upload"],
                           cwd=os.path.dirname(script_path), env=dead_aws_env(),
                           capture_output=True, text=True, timeout=30, check=False)
    except subprocess.TimeoutExpired:
        return False, "timeout"
    retired = any(line.startswith("RETIRED:") for line in r.stdout.splitlines())
    if r.returncode == RETIRED_RC and retired:
        return True, "rc=3 RETIRED"
    return False, f"rc={r.returncode} retired_line={retired}"


def live_refs(path, token):
    """Count non-comment lines of a shell file that carry `token` as a word."""
    pat = re.compile(rf"(?<![A-Za-z0-9_]){re.escape(token)}(?![A-Za-z0-9_])")
    n = 0
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.lstrip().startswith("#"):
                continue
            if pat.search(line):
                n += 1
    return n


def bash_syntax_ok(path):
    sys.path.insert(0, os.path.join(repo_root(), ".tools"))
    from git_bash_resolver import (
        git_bash,  # never bare 'bash' (WSL shadows it on Windows)
    )
    exe = git_bash() if os.name == "nt" else "bash"
    if not exe:
        return False
    r = subprocess.run([exe, "-n", path], capture_output=True, text=True, timeout=30, check=False)
    return r.returncode == 0
