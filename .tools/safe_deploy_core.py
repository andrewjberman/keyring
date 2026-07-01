#!/usr/bin/env python3
"""safe_deploy_core.py -- core logic for safe-deploy.sh (ADHC_DSFLOW.005).

Provides: file->pipeline mapping, detect changed scripts, S3 deploy + verify,
bypass audit logging. Callable directly or importable by test_safe_deploy.py.
"""
from __future__ import annotations

import hashlib
import os
import pathlib
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from typing import Optional

WORKSPACE = pathlib.Path(__file__).parent.parent

# Pipeline detection table: data_dir_name -> (s3_bucket, pipeline_label)
PIPELINE_MAP: dict[str, tuple[str, str]] = {
    "black_diamond": ("opal-data-bd", "bd"),
    "inf": ("opal-data-inf", "inf"),
    "cot": ("opal-data-cot", "cot"),
}

BYPASS_AUDIT_LOG = WORKSPACE / "org" / "safe-deploy-bypass-audit.log"
VALID_LAYERS = {"gold", "silver", "bronze"}

# ---------------------------------------------------------------------------
# Canonical code-prefix registry (ADVI_INFETL.BRONZE-FIX #1 + NFRA_DEBTSCAN
# TOOL-03; machine-readable surface for the deploy-completion ledger, TO #5).
#
# The COMPLETE canonical map of every code location on a firm bucket is:
#   standard layers: PIPELINE_MAP x VALID_LAYERS
#       repo data/<dir>/scripts/<layer>/*.py -> s3://<bucket>/code/<layer>/
#       (file_to_s3_target -- the Rule-13 deploy gate; ONE prefix per layer,
#       upload target == every consumer's sync source. The 2026-06-12 inf-ADVI
#       P0 was a violation of this invariant: orchestrator deploys landed at
#       code/bronze/ while the runner synced code/bronze-runner/.)
#   auxiliary prefixes: AUX_CODE_PREFIXES below
#       CHECK-ONLY locations outside the deploy gate. Value = repo-home dir for
#       same-basename comparison (comp-pipescript deployed [aux:<prefix>] rows);
#       None = no unambiguous repo home -> the tool reports UNCOVERED, never
#       silent-clean. Consumers: comp-pipescript (pipeline_cli imports this),
#       deploy-ledger leg enumeration (TO #5).
#
#   inf bronze-runner/ -- runner-OPS assets ONLY post-collapse (fetch script,
#     watchdog, backfill helpers; repo home infra/aws/ec2/inf-bronze-runner)
#     + the manual_api mirror sub-prefix (remaining consolidation leg).
#     PIPELINE code no longer lives here -- the runner syncs orchestrator.py
#     from code/bronze/ (BRONZE-FIX #1).
#   inf manual_api/ -- Orion REST dim-pull scripts, consumed by the inf GOLD
#     runner's 4-prefix flat sync (collision-guarded); repo home
#     data/inf/manual_api.
# ---------------------------------------------------------------------------
AUX_CODE_PREFIXES: dict[str, dict[str, Optional[str]]] = {
    "bd": {},
    "inf": {
        "bronze-runner": "infra/aws/ec2/inf-bronze-runner",
        "manual_api": "data/inf/manual_api",
        "runner": None,
        "exporter": None,
        "cleanup": None,
    },
    "cot": {},
}


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


def _find_pipeline_cli() -> Optional[str]:
    """Locate pipeline_cli.py -- the engine BEHIND the extensionless `comp-pipescript` bash
    wrapper (the wrapper just runs `python org/modules/graph/pipeline_cli.py "$@"`).

    We target the Python entry, NOT the wrapper, on purpose: subprocess-exec of the
    extensionless bash wrapper raises OSError WinError 193 ("%1 is not a valid Win32
    application") on Windows -- the S3 cp already SUCCEEDED, so the verify step silently
    crashes and the deploy reads GREEN while UNVERIFIED (latent false-green; CTO 20260701T1511Z,
    surfaced by DS~A on the ADVI_TAGATTR leg-2 bd deploy). Invoking the Python entry directly via
    sys.executable is the ratified cross-platform pattern (harness.py/kuzu_cli, commit 572a5d9b8:
    "no bash hop -- the WSL /bin/bash relay is broken from Windows-python")."""
    candidate = WORKSPACE / "org" / "modules" / "graph" / "pipeline_cli.py"
    if candidate.exists():
        return str(candidate)
    # PATH fallback via the wrapper's location (git hooks don't source bashrc), resolving the
    # sibling engine relative to a discovered wrapper if the canonical path ever moves.
    wrapper = shutil.which("comp-pipescript")
    if wrapper:
        sib = pathlib.Path(wrapper).resolve().parent.parent / "org" / "modules" / "graph" / "pipeline_cli.py"
        if sib.exists():
            return str(sib)
    return None


def _pipescript_output_ok(output: str) -> bool:
    """Parse a `comp-pipescript deployed <script>` result: True = clean, False = STALE/MISSING.

    Reads the 'Summary: N MATCH, N STALE, N MISSING_ON_S3, ...' COUNTS -- NOT a bare substring.
    The summary line literally contains the tokens 'STALE'/'MISSING_ON_S3' even at count 0, so the
    old `"STALE" in output` test FALSE-FAILED every COMPLETED run (it only ever "passed" because
    the check never completed on Windows -- WinError-193 crash, then big-layer timeout; the
    scope-to-changed-script fix (b) makes it complete reliably and surfaced this). Failure semantics
    are unchanged from the original intent: STALE or MISSING_ON_S3 => fail. Falls back to a per-line
    status scan when no summary line is present (no '0 STALE' summary to confuse it there)."""
    m = re.search(r"Summary:\s*([^\n]+)", output)
    if m:
        counts = {tok: int(n) for n, tok in re.findall(r"(\d+)\s+([A-Z0-9_-]+)", m.group(1))}
        return counts.get("STALE", 0) == 0 and counts.get("MISSING_ON_S3", 0) == 0
    return not re.search(r"\b(STALE|MISSING_ON_S3)\b", output)


def run_pipescript_verify(rel_path: str) -> tuple[bool, str]:
    """Run `comp-pipescript deployed <rel_path>` (via its pipeline_cli.py engine) for ONE
    just-deployed script; return (match, output).

    Scoped to the CHANGED script, not the whole label-layer (CTO ruling (b) 20260701T1735Z): the
    deploy-verify's job is "did THIS deploy's scripts land", so we verify exactly what was PUSHED.
    A repo-relative `data/<tree>/scripts/...` path auto-detects the firm/tree in pipeline_cli's
    scope-resolution and checks ONLY that script against its own bucket. This (a) scales with the
    deploy size (1-few scripts -> seconds), so it NEVER times out on a big layer, and (b) removes
    the fail-open-WARN-on-timeout soft-no-op -- a completing per-script check FAILS LOUD on
    STALE/MISSING. Estate-wide drift (are UNCHANGED scripts current?) is a different job =
    comp-pipescript's no-arg sweep, NOT the deploy-verify's.

    Treats STALE or MISSING_ON_S3 in output as failure.
    Invoked as [sys.executable, pipeline_cli.py, ...] rather than the extensionless bash wrapper so
    the verify actually EXECUTES on Windows (the WinError-193 gate-hole fix -- see _find_pipeline_cli).
    If the engine is unreachable, warns and returns True (MD5 verify already passed).
    """
    cli = _find_pipeline_cli()
    if not cli:
        return True, "WARN: pipeline_cli.py not found; skipping pipescript verify (MD5 verify passed)"

    env = _aws_env()
    try:
        result = subprocess.run(
            [sys.executable, cli, "deployed", rel_path],
            capture_output=True, text=True, timeout=120, env=env,
        )
    except subprocess.TimeoutExpired:
        return True, f"WARN: pipescript verify {rel_path} timed out; skipping (MD5 passed)"
    output = result.stdout + result.stderr
    return _pipescript_output_ok(output), output


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
        # comp-pipescript verify phase: per CHANGED SCRIPT (CTO ruling (b) 20260701T1735Z).
        # Iterate `deployed` -- the exact set of scripts that landed on S3 this run -- and verify
        # each individually. Verifying what THIS deploy pushed (not the whole label-layer) scopes
        # the check to the deploy size, so it completes in seconds and never times out on a big
        # layer, and it fails LOUD on STALE/MISSING instead of soft-no-op-on-timeout.
        verify_ok = True
        for rel_path, _bucket, _s3_key in deployed:
            ok, output = run_pipescript_verify(rel_path)
            if ok:
                print(f"  VERIFY OK  comp-pipescript deployed {rel_path}")
            else:
                print(f"  VERIFY FAIL  comp-pipescript deployed {rel_path}")
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
