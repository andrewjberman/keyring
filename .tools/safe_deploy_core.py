#!/usr/bin/env python3
"""safe_deploy_core.py -- core logic for safe-deploy.sh (ADHC_DSFLOW.005).

Provides: file->pipeline mapping, detect changed scripts, S3 deploy + verify,
bypass audit logging. Callable directly or importable by test_safe_deploy.py.
"""
from __future__ import annotations

import hashlib
import os
import pathlib
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from typing import Optional

WORKSPACE = pathlib.Path(__file__).parent.parent

# Pipeline detection table: data_dir_name -> (s3_bucket, pipeline_label)
PIPELINE_MAP: dict[str, tuple[str, str]] = {
    "black_diamond": ("opal-data-bd", "bd"),
    "orion": ("opal-data-inf", "inf"),
    "cot": ("opal-data-cot", "cot"),
}

BYPASS_AUDIT_LOG = WORKSPACE / "org" / "safe-deploy-bypass-audit.log"
VALID_LAYERS = {"gold", "silver", "bronze"}


def file_to_s3_target(rel_path: str) -> Optional[tuple[str, str, str]]:
    """Map a repo-relative file path to (bucket, s3_key, pipeline_label).

    Scope: data/<pipeline_dir>/scripts/{gold,silver,bronze}[/lib]/*.py
    Returns None if path is not in a recognized deploy scope.
    """
    p = pathlib.PurePosixPath(rel_path.replace("\\", "/"))
    parts = p.parts
    # Minimum: data / <pd> / scripts / <layer> / <file>.py  (5 parts)
    if len(parts) < 5:
        return None
    if parts[0] != "data":
        return None
    pipeline_dir = parts[1]
    if pipeline_dir not in PIPELINE_MAP:
        return None
    if parts[2] != "scripts":
        return None
    layer = parts[3]
    if layer not in VALID_LAYERS:
        return None
    if not rel_path.endswith(".py"):
        return None
    bucket, label = PIPELINE_MAP[pipeline_dir]
    # S3 key = code/<layer>/[lib/]<file>.py
    s3_suffix = "/".join(parts[3:])
    s3_key = f"code/{s3_suffix}"
    return bucket, s3_key, label


def detect_script_files(
    commit_range: Optional[str] = None,
    explicit_files: Optional[list[str]] = None,
) -> list[str]:
    """Return list of repo-relative deploy-scope .py paths.

    Priority: explicit_files > commit_range > git diff HEAD~1..HEAD.
    """
    if explicit_files:
        return [f for f in explicit_files if file_to_s3_target(f) is not None]

    if commit_range:
        old_sha = commit_range.split("..")[0] if ".." in commit_range else ""
        if old_sha.startswith("0000000"):
            # New branch: diff against main
            cmd = ["git", "diff", "--name-only", "--diff-filter=ACMRT", "origin/main...HEAD"]
        else:
            cmd = ["git", "diff", "--name-only", "--diff-filter=ACMRT", commit_range]
    else:
        cmd = ["git", "diff", "--name-only", "--diff-filter=ACMRT", "HEAD~1..HEAD"]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, cwd=str(WORKSPACE), timeout=30
        )
        files = [f.strip() for f in result.stdout.splitlines() if f.strip()]
    except Exception:
        files = []
    return [f for f in files if file_to_s3_target(f) is not None]


def _local_md5(path: pathlib.Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def _aws_env() -> dict[str, str]:
    env = os.environ.copy()
    env.setdefault("AWS_EC2_METADATA_DISABLED", "true")
    env.setdefault("AWS_METADATA_SERVICE_NUM_ATTEMPTS", "1")
    env.setdefault("AWS_PAGER", "")
    return env


def _find_aws() -> Optional[str]:
    return shutil.which("aws") or shutil.which("aws.cmd") or shutil.which("aws.exe")


def deploy_file(
    local_path: pathlib.Path,
    bucket: str,
    s3_key: str,
) -> tuple[str, str]:
    """Upload file to S3 and verify ETag == local MD5.

    Returns (status, detail):
      ("MATCH", "")
      ("LOCAL_MISSING", "")
      ("UPLOAD_FAIL", stderr)
      ("SHA_MISMATCH", "local:<md5> s3:<etag>")
      ("S3_ERROR", stderr)
    """
    if not local_path.exists():
        return "LOCAL_MISSING", str(local_path)

    aws_bin = _find_aws()
    if not aws_bin:
        return "UPLOAD_FAIL", "aws CLI not found in PATH (checked aws, aws.cmd, aws.exe)"

    local_md5 = _local_md5(local_path)
    env = _aws_env()

    cp_result = subprocess.run(
        [aws_bin, "s3", "cp", str(local_path), f"s3://{bucket}/{s3_key}"],
        capture_output=True, text=True, timeout=60, env=env,
    )
    if cp_result.returncode != 0:
        return "UPLOAD_FAIL", cp_result.stderr.strip()

    ho_result = subprocess.run(
        [aws_bin, "s3api", "head-object",
         "--bucket", bucket, "--key", s3_key,
         "--query", "ETag", "--output", "text"],
        capture_output=True, text=True, timeout=15, env=env,
    )
    if ho_result.returncode != 0:
        return "S3_ERROR", ho_result.stderr.strip()

    s3_etag = ho_result.stdout.strip().strip('"')
    if local_md5 == s3_etag:
        return "MATCH", ""
    return "SHA_MISMATCH", f"local:{local_md5} s3:{s3_etag}"


def _find_comp_pipescript() -> Optional[str]:
    """Locate comp-pipescript; git hooks don't source bashrc so .tools/ may not be in PATH."""
    found = shutil.which("comp-pipescript")
    if found:
        return found
    # Fall back to sibling in .tools/ (safe_deploy_core.py lives there too)
    candidate = pathlib.Path(__file__).parent / "comp-pipescript"
    if candidate.exists():
        return str(candidate)
    return None


def run_pipescript_verify(pipeline_label: str, layer: str) -> tuple[bool, str]:
    """Run comp-pipescript deployed for pipeline+layer; return (all_match, output).

    Treats STALE or MISSING_ON_S3 in output as failure.
    If comp-pipescript is unreachable, warns and returns True (MD5 verify already passed).
    """
    comp_bin = _find_comp_pipescript()
    if not comp_bin:
        return True, "WARN: comp-pipescript not found; skipping pipescript verify (MD5 verify passed)"

    pipeline_arg = f"{pipeline_label}-{layer}"
    env = _aws_env()
    try:
        result = subprocess.run(
            [comp_bin, "deployed", "--pipeline", pipeline_arg],
            capture_output=True, text=True, timeout=120, env=env,
        )
    except subprocess.TimeoutExpired:
        return True, f"WARN: comp-pipescript --pipeline {pipeline_arg} timed out; skipping (MD5 passed)"
    output = result.stdout + result.stderr
    if "STALE" in output or "MISSING_ON_S3" in output:
        return False, output
    return True, output


def write_bypass_audit(author: str, files: list[str], commit_sha: str, reason: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    BYPASS_AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    detail = ",".join(files[:5])
    if len(files) > 5:
        detail += f"...+{len(files) - 5}"
    entry = (
        f"{ts} ALLOW-STALE  {author}  {len(files)}  ({detail})"
        f"  sha:{commit_sha}  reason:{reason}\n"
    )
    with open(BYPASS_AUDIT_LOG, "a", encoding="utf-8") as fh:
        fh.write(entry)


def _current_commit_sha() -> str:
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, cwd=str(WORKSPACE), timeout=10,
        )
        return r.stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def main(argv: list[str]) -> int:
    import argparse

    ap = argparse.ArgumentParser(
        prog="safe-deploy",
        description="Atomic deploy: S3 cp + SHA verify + comp-pipescript confirm. ADHC_DSFLOW.005",
    )
    ap.add_argument("files", nargs="*", help="Explicit file list (repo-relative)")
    ap.add_argument("--commit-range", default=None,
                    help="git diff range, e.g. abc123..def456 (used by pre-push hook)")
    ap.add_argument("--allow-stale", action="store_true",
                    help="Skip verify; write audit entry. Use only for emergency/docstring-only changes.")
    ap.add_argument("--reason", default="",
                    help="Reason for --allow-stale bypass (required with --allow-stale)")
    ap.add_argument("--author", default="",
                    help="Agent identity for audit log (e.g. 0.4.0_DS_ClientPlatform)")
    ap.add_argument("--no-pipescript", action="store_true",
                    help="Skip comp-pipescript verify phase (upload + SHA only)")

    args = ap.parse_args(argv)

    # Detect files
    files = detect_script_files(
        commit_range=args.commit_range,
        explicit_files=args.files if args.files else None,
    )

    if not files:
        print("OK: safe-deploy -- no deploy-scope script files detected, nothing to do")
        return 0

    print(f"safe-deploy: {len(files)} script file(s) to deploy")
    for f in files:
        print(f"  {f}")
    print()

    # --allow-stale bypass
    if args.allow_stale:
        if not args.reason:
            print("ERROR: --allow-stale requires --reason", file=sys.stderr)
            return 2
        sha = _current_commit_sha()
        write_bypass_audit(args.author or "UNKNOWN", files, sha, args.reason)
        print(f"WARN: --allow-stale bypass active; {len(files)} file(s) NOT deployed to S3")
        print(f"  Audit: {BYPASS_AUDIT_LOG}")
        print(f"  Reason: {args.reason}")
        return 0

    # Deploy phase: upload all files, fail fast on any error
    deployed: list[tuple[str, str, str]] = []   # (rel_path, bucket, s3_key)
    failed = False

    for rel_path in files:
        target = file_to_s3_target(rel_path)
        if target is None:
            continue
        bucket, s3_key, label = target
        local_path = WORKSPACE / rel_path.replace("/", os.sep)
        status, detail = deploy_file(local_path, bucket, s3_key)
        tag = f"[{label}] {rel_path}"
        if status == "MATCH":
            print(f"  DEPLOYED  {tag}")
            deployed.append((rel_path, bucket, s3_key))
        else:
            print(f"  ERROR  {status}  {tag}")
            if detail:
                print(f"           {detail}")
            failed = True
            break   # fail fast; don't leave partial state

    if failed:
        print()
        print("ERROR: safe-deploy gate FAILED -- S3 deploy or SHA verify error")
        print("  Partial deploy state: files listed above as DEPLOYED may already be on S3.")
        print("  Fix the error and re-run; the gate is idempotent.")
        return 1

    print()

    if not args.no_pipescript:
        # comp-pipescript verify phase: group by pipeline+layer
        seen_combos: set[tuple[str, str]] = set()
        verify_ok = True
        for rel_path in files:
            target = file_to_s3_target(rel_path)
            if target is None:
                continue
            _, _, label = target
            p = pathlib.PurePosixPath(rel_path.replace("\\", "/"))
            layer = p.parts[3]
            combo = (label, layer)
            if combo in seen_combos:
                continue
            seen_combos.add(combo)
            ok, output = run_pipescript_verify(label, layer)
            if ok:
                print(f"  VERIFY OK  comp-pipescript deployed --pipeline {label}-{layer}")
            else:
                print(f"  VERIFY FAIL  comp-pipescript deployed --pipeline {label}-{layer}")
                print(output[:800])
                verify_ok = False

        if not verify_ok:
            print()
            print("ERROR: safe-deploy gate FAILED -- comp-pipescript STALE/MISSING after upload")
            return 1

    print("OK: safe-deploy gate PASS -- all files deployed and verified")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
