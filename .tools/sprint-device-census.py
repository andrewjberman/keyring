#!/usr/bin/env python
"""sprint-device-census.py -- one device's commit census for the daily sprint (NFRA_SPRINTWIN H1).

The cloud run of the daily sprint clones the PUSHED history, so work a device has committed and not
pushed is outside its population. This script publishes what ONE device holds, so the run can count
the union of the pushed history and every device's census, once per commit (PRD C-CENSUS, C-UNION).

Usage (the scheduled task runs the copy on origin/CLOUD, never the working tree -- PRD C-CENSUS):
    git -C <repo> show origin/CLOUD:.tools/sprint-device-census.py > %TEMP%/sprint-device-census.py
    python %TEMP%/sprint-device-census.py --root <repo>
Options: --no-upload (write --out only), --out <file>, --day YYYY-MM-DD (the New York day the key is
filed under; default: today in New York).

What one file holds (C-CENSUS, brief D3a): `device`, `generated_at`, the local `head`, the
`origin_cloud` this device last fetched, and `commits` from
    git log --all --no-merges --since=<now - 8 days> --name-only
with exactly git's %H %aI %cI %an %ae %s per row plus its files, so a device row classifies exactly
as the same commit read from the cloud's clone. Commit metadata only: no file content, no client data.
`notes` is daily_reports/notes/<day>.md when present. `script_blob` is the git blob id of the bytes
that ran, so a reader can tell the pinned copy from a working-tree edit (FWD-7).

Where it goes: lib/opal_naming.py address('sprint', 'global', 'bronze', 'device_census',
'date=<day>', '<device>.json') -- builder output, never a typed path (CLAUDE.md rule 30), from the
builder and registry AS PUBLISHED at origin/CLOUD (pinned_address), not the working tree's. The put is
verified by read-back (size + MD5 ETag); the upload's return code is never the proof.

boto3 is an already-installed dependency on both devices (the local /daily-sprint publisher uses it);
it replaces a subprocess to the aws CLI, whose argv crosses the MSYS boundary.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys

LOOKBACK_DAYS = 8          # C-WINDOW's 7-day cap plus one (PRD v0.2, CVO~Z finding 2)
SCHEMA = "sprint-device-census-v1"
SEP = "\x1e"               # record separator: never in a subject or a path


def _git(root, *args):
    out = subprocess.run(["git", "-C", root] + list(args), capture_output=True, text=True,
                         encoding="utf-8", errors="replace")
    if out.returncode != 0:
        raise SystemExit("ERROR: git %s failed rc=%d: %s" % (" ".join(args[:3]), out.returncode,
                                                            out.stderr.strip()[-500:]))
    return out.stdout


def device_name(root):
    """`device:` from .tools/agentbus-sqs.sh device -- the fabric's one device resolver."""
    sys.path.insert(0, os.path.join(root, ".tools"))
    from git_bash_resolver import git_bash
    bash = git_bash()
    if not bash:
        raise SystemExit("ERROR: no Git Bash found; refusing to guess the device")
    out = subprocess.run([bash, os.path.join(root, ".tools", "agentbus-sqs.sh"), "device"],
                         capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=root)
    for line in out.stdout.splitlines():
        if line.startswith("device:"):
            dev = line.split(":", 1)[1].strip()
            if dev and dev != "UNKNOWN":
                return dev
    raise SystemExit("ERROR: agentbus-sqs.sh device did not resolve this device (rc=%d): %s"
                     % (out.returncode, (out.stdout + out.stderr).strip()[-500:]))


def commits_since(root, since):
    """Every non-merge commit on every local ref since `since`, in git's own formats.

    The flags match daily_reports/scripts/{commit,project}_census.py (--all --no-merges
    --name-only), so a commit's file list here is byte-identical to the one the cloud's clone gives."""
    fmt = SEP + "%H%x00%aI%x00%cI%x00%an%x00%ae%x00%s"
    txt = _git(root, "log", "--all", "--no-merges", "--since=" + since, "--date=iso-strict",
               "--format=" + fmt, "--name-only")
    rows = []
    for rec in txt.split(SEP)[1:]:
        lines = rec.split("\n")
        sha, a_time, c_time, a_name, a_mail, subject = lines[0].split("\x00", 5)
        rows.append({"sha": sha, "author_time": a_time, "commit_time": c_time, "author_name": a_name,
                     "author_email": a_mail, "subject": subject,
                     "files": [ln.strip() for ln in lines[1:] if ln.strip()]})
    return rows


def build(root, day=None):
    from zoneinfo import ZoneInfo
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    day = day or now.astimezone(ZoneInfo("America/New_York")).date().isoformat()
    since = (now - dt.timedelta(days=LOOKBACK_DAYS)).isoformat()
    notes_path = os.path.join(root, "daily_reports", "notes", day + ".md")
    notes = None
    if os.path.exists(notes_path):
        with open(notes_path, encoding="utf-8") as f:
            notes = f.read()
    with open(os.path.abspath(__file__), "rb") as f:
        body = f.read()
    blob = hashlib.sha1(b"blob %d\x00" % len(body) + body).hexdigest()
    try:
        origin_cloud = _git(root, "rev-parse", "origin/CLOUD").strip()
    except SystemExit:
        origin_cloud = None
    commits = commits_since(root, since)
    return {
        "schema": SCHEMA,
        "device": device_name(root),
        "generated_at": now.isoformat().replace("+00:00", "Z"),
        "day": day,
        "head": _git(root, "rev-parse", "HEAD").strip(),
        "origin_cloud": origin_cloud,
        "since": since.replace("+00:00", "Z"),
        "lookback_days": LOOKBACK_DAYS,
        "script_blob": blob,
        "commit_count": len(commits),
        "commits": commits,
        "notes": notes,
    }


def pinned_address(root, rev, *args):
    """lib/opal_naming.py address() as it stands at `rev` (origin/CLOUD), never the working tree's.

    The script itself runs pinned (PRD C-CENSUS), but it used to import the builder and its registry
    from the WORKING TREE -- measured 2026-10-04 20:56Z on the laptop: a tree 80 commits behind
    origin lacked the `sprint` row and the run failed "source sprint is not a systems.json key".
    The builder, its schema and the registry are exported from `rev` into a temporary tree, so the
    key a device writes is the one the published code names, whatever state the checkout is in."""
    import importlib.util
    import shutil
    import tempfile
    reg = [p for p in _git(root, "ls-tree", "--name-only", rev, "infra/logic/registry/").split() if p.endswith(".json")]
    need = ["lib/opal_naming.py", "org/standards/NAMING_SCHEMA.json", "org/missions/DIRECTIVES.yaml"] + reg
    tmp = tempfile.mkdtemp(prefix="sprint-naming-")
    try:
        for rel in need:
            out = subprocess.run(["git", "-C", root, "show", "%s:%s" % (rev, rel)], capture_output=True)
            if out.returncode != 0 or not out.stdout:
                raise SystemExit("ERROR: %s:%s unreadable (rc=%d): %s" % (rev, rel, out.returncode,
                                                                          out.stderr.decode("utf-8", "replace")[-300:]))
            dst = os.path.join(tmp, *rel.split("/"))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with open(dst, "wb") as f:
                f.write(out.stdout)
        spec = importlib.util.spec_from_file_location("opal_naming_pinned", os.path.join(tmp, "lib", "opal_naming.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.address(*args)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def upload(root, census, data):
    rev = census["origin_cloud"]
    if not rev:
        raise SystemExit("ERROR: this checkout has no origin/CLOUD; the census key comes from the published builder")
    url = pinned_address(root, rev, "sprint", "global", "bronze", "device_census", "date=" + census["day"],
                         census["device"] + ".json")
    bucket, key = url[len("s3://"):].split("/", 1)
    import boto3
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket, Key=key, Body=data, ContentType="application/json")
    head = s3.head_object(Bucket=bucket, Key=key)
    ok = (head.get("ContentLength") == len(data)
          and head.get("ETag", "").strip('"') == hashlib.md5(data).hexdigest())
    print("%s: %s size=%s/%d etag=%s" % ("OK" if ok else "ERROR", url, head.get("ContentLength"),
                                          len(data), "MATCH" if ok else "MISMATCH"))
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("--root", help="the repository (default: the git toplevel of the current directory)")
    ap.add_argument("--day", help="the New York day the file is filed under (default: today)")
    ap.add_argument("--out", help="also write the census JSON here")
    ap.add_argument("--no-upload", action="store_true", help="write --out only; put nothing")
    a = ap.parse_args(argv)
    root = a.root or subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                                    text=True).stdout.strip()
    if not root or not os.path.isdir(os.path.join(root, ".git")) and not os.path.isfile(os.path.join(root, ".git")):
        raise SystemExit("ERROR: --root %r is not a git working tree" % root)
    census = build(root, a.day)
    data = json.dumps(census, ensure_ascii=True, separators=(",", ":")).encode("utf-8")
    print("OK: census %s day %s: %d commits since %s, %d bytes, notes %s, script_blob %s"
          % (census["device"], census["day"], census["commit_count"], census["since"], len(data),
             "present" if census["notes"] is not None else "absent", census["script_blob"][:12]))
    if a.out:
        with open(a.out, "wb") as f:
            f.write(data)
    if a.no_upload:
        return 0
    return 0 if upload(root, census, data) else 1


if __name__ == "__main__":
    sys.exit(main())
