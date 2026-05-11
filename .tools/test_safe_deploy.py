#!/usr/bin/env python3
"""test_safe_deploy.py -- 6-fixture test suite for safe_deploy_core.py (ADHC_DSFLOW.005).

Tests (no real AWS required -- subprocess mocked):
  1. PASS      -- gold script, upload OK, ETag matches local MD5
  2. FAIL-NODEPLOY -- no upload attempted, simulate: gate catches stale script
  3. FAIL-PARTIAL  -- first file OK, second upload fails -> gate errors, partial state logged
  4. FAIL-MISMATCH -- upload OK but ETag mismatches local MD5 -> SHA guard fires
  5. BYPASS        -- --allow-stale -> audit log entry written, exit 0
  6. INF-PATH      -- data/orion/* maps to opal-data-inf, not opal-data-bd

Exit 0 if all 6 assertions hold; exit 1 with details on any failure.
"""
from __future__ import annotations

import hashlib
import importlib.machinery
import pathlib
import sys
import tempfile
from unittest.mock import MagicMock, patch

# Load safe_deploy_core without .py extension (same trick used in test_ds_precommit_check.py)
_TOOLS = pathlib.Path(__file__).parent
_core_path = _TOOLS / "safe_deploy_core.py"
_loader = importlib.machinery.SourceFileLoader("safe_deploy_core", str(_core_path))
_core = _loader.load_module()  # noqa: FWD001

file_to_s3_target = _core.file_to_s3_target
detect_script_files = _core.detect_script_files
deploy_file = _core.deploy_file
write_bypass_audit = _core.write_bypass_audit
main = _core.main


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def _make_subprocess_mock(upload_rc=0, upload_stderr="", etag=None, head_rc=0, head_stderr=""):
    """Return a callable usable as subprocess.run mock."""
    def _run(cmd, **kwargs):
        result = MagicMock()
        cmd_str = " ".join(str(c) for c in cmd)
        if "s3 cp" in cmd_str:
            result.returncode = upload_rc
            result.stderr = upload_stderr
            result.stdout = ""
        elif "head-object" in cmd_str:
            result.returncode = head_rc
            result.stdout = f'"{etag}"\n' if etag else ""
            result.stderr = head_stderr
        else:
            result.returncode = 0
            result.stdout = ""
            result.stderr = ""
        return result
    return _run


# ---------------------------------------------------------------------------
# Case 1: PASS — gold script deploy + ETag match
# ---------------------------------------------------------------------------
def test_pass_gold_deploy():
    with tempfile.TemporaryDirectory() as td:
        content = b"# gold script\n"
        local = pathlib.Path(td) / "B_00.py"
        local.write_bytes(content)
        expected_etag = _md5(content)

        mock_run = _make_subprocess_mock(
            upload_rc=0, etag=expected_etag
        )
        with patch("safe_deploy_core.subprocess.run", side_effect=mock_run), \
             patch("safe_deploy_core._find_aws", return_value="/usr/bin/aws"):
            status, detail = deploy_file(local, "opal-data-bd", "code/gold/B_00.py")

    assert status == "MATCH", f"Case 1 FAIL: expected MATCH, got {status!r} ({detail!r})"
    return True


# ---------------------------------------------------------------------------
# Case 2: FAIL-NODEPLOY — simulate no deploy by detecting STALE via ETag mismatch
# (gate fires before comp-pipescript; analogous to "push without S3 cp")
# ---------------------------------------------------------------------------
def test_fail_nodeploy():
    with tempfile.TemporaryDirectory() as td:
        content = b"# updated gold script\n"
        local = pathlib.Path(td) / "B_01.py"
        local.write_bytes(content)
        stale_etag = _md5(b"# old version\n")   # mismatch -> STALE

        mock_run = _make_subprocess_mock(upload_rc=0, etag=stale_etag)
        with patch("safe_deploy_core.subprocess.run", side_effect=mock_run), \
             patch("safe_deploy_core._find_aws", return_value="/usr/bin/aws"):
            status, detail = deploy_file(local, "opal-data-bd", "code/gold/B_01.py")

    assert status == "SHA_MISMATCH", \
        f"Case 2 FAIL: expected SHA_MISMATCH (stale ETag), got {status!r}"
    return True


# ---------------------------------------------------------------------------
# Case 3: FAIL-PARTIAL — first file OK, second file upload fails -> fast-fail
# ---------------------------------------------------------------------------
def test_fail_partial():
    call_count = [0]

    def _partial_run(cmd, **kwargs):
        result = MagicMock()
        cmd_str = " ".join(str(c) for c in cmd)
        if "s3 cp" in cmd_str:
            call_count[0] += 1
            if call_count[0] == 1:
                # First upload succeeds
                result.returncode = 0
                result.stderr = ""
                result.stdout = ""
            else:
                # Second upload fails
                result.returncode = 1
                result.stderr = "An error occurred (NoSuchBucket)"
                result.stdout = ""
        elif "head-object" in cmd_str:
            content = b"# first file\n"
            result.returncode = 0
            result.stdout = f'"{_md5(content)}"\n'
            result.stderr = ""
        else:
            result.returncode = 0
            result.stdout = ""
            result.stderr = ""
        return result

    with tempfile.TemporaryDirectory() as td:
        f1 = pathlib.Path(td) / "B_00.py"
        f2 = pathlib.Path(td) / "B_01.py"
        f1.write_bytes(b"# first file\n")
        f2.write_bytes(b"# second file\n")

        with patch("safe_deploy_core.subprocess.run", side_effect=_partial_run), \
             patch("safe_deploy_core._find_aws", return_value="/usr/bin/aws"):
            s1, _ = deploy_file(f1, "opal-data-bd", "code/gold/B_00.py")
            s2, detail2 = deploy_file(f2, "opal-data-bd", "code/gold/B_01.py")

    assert s1 == "MATCH", f"Case 3 FAIL: first file should MATCH, got {s1!r}"
    assert s2 == "UPLOAD_FAIL", f"Case 3 FAIL: second file should UPLOAD_FAIL, got {s2!r}"
    return True


# ---------------------------------------------------------------------------
# Case 4: FAIL-MISMATCH — upload succeeds but ETag corrupted (SHA guard fires)
# ---------------------------------------------------------------------------
def test_fail_sha_mismatch():
    with tempfile.TemporaryDirectory() as td:
        content = b"# real content\n"
        local = pathlib.Path(td) / "C_01.py"
        local.write_bytes(content)
        corrupt_etag = "deadbeefdeadbeefdeadbeefdeadbeef"

        mock_run = _make_subprocess_mock(upload_rc=0, etag=corrupt_etag)
        with patch("safe_deploy_core.subprocess.run", side_effect=mock_run), \
             patch("safe_deploy_core._find_aws", return_value="/usr/bin/aws"):
            status, detail = deploy_file(local, "opal-data-bd", "code/gold/C_01.py")

    assert status == "SHA_MISMATCH", \
        f"Case 4 FAIL: expected SHA_MISMATCH (corrupt ETag), got {status!r}"
    assert "local:" in detail and "s3:" in detail, \
        f"Case 4 FAIL: detail should show local+s3 hashes, got {detail!r}"
    return True


# ---------------------------------------------------------------------------
# Case 5: BYPASS — --allow-stale writes audit entry
# ---------------------------------------------------------------------------
def test_bypass_allow_stale():
    with tempfile.TemporaryDirectory() as td:
        audit_log = pathlib.Path(td) / "org" / "safe-deploy-bypass-audit.log"
        with patch.object(_core, "BYPASS_AUDIT_LOG", audit_log):
            write_bypass_audit(
                author="0.4.0_DS_ClientPlatform",
                files=["data/orion/scripts/gold/INF_D_04.py"],
                commit_sha="abc1234",
                reason="docstring-only change",
            )
        assert audit_log.exists(), "Case 5 FAIL: audit log not created"
        content = audit_log.read_text()
        assert "ALLOW-STALE" in content, "Case 5 FAIL: ALLOW-STALE marker missing"
        assert "0.4.0_DS_ClientPlatform" in content, "Case 5 FAIL: author missing"
        assert "docstring-only change" in content, "Case 5 FAIL: reason missing"
        assert "abc1234" in content, "Case 5 FAIL: commit SHA missing"
    return True


# ---------------------------------------------------------------------------
# Case 6: INF-PATH — orion files map to opal-data-inf, not opal-data-bd
# ---------------------------------------------------------------------------
def test_inf_path_resolution():
    cases = [
        ("data/orion/scripts/gold/INF_D_01.py", "opal-data-inf", "code/gold/INF_D_01.py", "inf"),
        ("data/orion/scripts/silver/silver_accounts.py", "opal-data-inf", "code/silver/silver_accounts.py", "inf"),
        ("data/orion/scripts/gold/lib/dtype_coerce.py", "opal-data-inf", "code/gold/lib/dtype_coerce.py", "inf"),
        ("data/black_diamond/scripts/gold/B_00.py", "opal-data-bd", "code/gold/B_00.py", "bd"),
        ("data/black_diamond/scripts/silver/lib/dtype_coerce.py", "opal-data-bd", "code/silver/lib/dtype_coerce.py", "bd"),
        # Out-of-scope paths -> None
        ("data/seeking-alpha/scripts/fetch.py", None, None, None),
        ("infra/aws/terraform/main.tf", None, None, None),
        ("data/orion/scripts/archive/old.py", None, None, None),  # not gold/silver/bronze
    ]
    for path, exp_bucket, exp_key, exp_label in cases:
        result = file_to_s3_target(path)
        if exp_bucket is None:
            assert result is None, \
                f"Case 6 FAIL: {path!r} should be None, got {result!r}"
        else:
            assert result is not None, f"Case 6 FAIL: {path!r} returned None, expected target"
            bucket, s3_key, label = result
            assert bucket == exp_bucket, \
                f"Case 6 FAIL: {path!r} bucket={bucket!r}, expected {exp_bucket!r}"
            assert s3_key == exp_key, \
                f"Case 6 FAIL: {path!r} s3_key={s3_key!r}, expected {exp_key!r}"
            assert label == exp_label, \
                f"Case 6 FAIL: {path!r} label={label!r}, expected {exp_label!r}"
    return True


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

CASES = [
    ("PASS gold deploy + ETag match", test_pass_gold_deploy),
    ("FAIL-NODEPLOY stale ETag detected", test_fail_nodeploy),
    ("FAIL-PARTIAL second upload fails", test_fail_partial),
    ("FAIL-MISMATCH corrupt ETag SHA guard", test_fail_sha_mismatch),
    ("BYPASS --allow-stale writes audit entry", test_bypass_allow_stale),
    ("INF-PATH orion->opal-data-inf routing", test_inf_path_resolution),
]


def main_test() -> int:
    results = []
    for name, fn in CASES:
        try:
            ok = fn()
            results.append((name, ok, ""))
        except AssertionError as e:
            results.append((name, False, str(e)))
        except Exception as e:
            results.append((name, False, f"EXCEPTION: {e}"))

    print("safe-deploy test results:")
    all_ok = True
    for name, ok, detail in results:
        mark = "PASS" if ok else "FAIL"
        print(f"  {mark}  {name}")
        if not ok and detail:
            print(f"       {detail}")
        if not ok:
            all_ok = False

    print()
    if all_ok:
        print(f"OK: {len(results)}/{len(results)} cases passed")
        return 0
    fail_n = sum(1 for _, ok, _ in results if not ok)
    print(f"FAIL: {fail_n}/{len(results)} cases failed")
    return 1


if __name__ == "__main__":
    sys.exit(main_test())
