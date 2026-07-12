#!/usr/bin/env python3
"""test_safe_deploy.py -- 7-fixture test suite for safe_deploy_core.py (ADHC_DSFLOW.005).

Tests (no real AWS required -- subprocess mocked):
  1. PASS      -- gold script, upload OK, ETag matches local MD5
  2. FAIL-NODEPLOY -- no upload attempted, simulate: gate catches stale script
  3. FAIL-PARTIAL  -- first file OK, second upload fails -> gate errors, partial state logged
  4. FAIL-MISMATCH -- upload OK but ETag mismatches local MD5 -> SHA guard fires
  5. BYPASS        -- --allow-stale -> audit log entry written, exit 0
  6. INF-PATH      -- data/inf/* maps to opal-data-inf, not opal-data-bd
  7. PIPESCRIPT-VERDICT -- the verify-output parser is correct on a known-good AND a
     known-bad fixture (ADHC_PREFLT: prove the gate emits the CORRECT verdict, not just
     "fails loud"; regression-guards the "0 STALE"-substring false-fail).

Exit 0 if all 7 assertions hold; exit 1 with details on any failure.
"""
from __future__ import annotations

import contextlib
import hashlib
import importlib.machinery
import io
import os
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
_pipescript_output_ok = _core._pipescript_output_ok
main = _core.main
_serve_held_reason = _core._serve_held_reason


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
                files=["data/inf/scripts/gold/INF_D_04.py"],
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
# Case 6: INF-PATH — data/inf files map to opal-data-inf, not opal-data-bd
# ---------------------------------------------------------------------------
def test_inf_path_resolution():
    cases = [
        ("data/inf/scripts/gold/INF_D_01.py", "opal-data-inf", "code/gold/INF_D_01.py", "inf"),
        ("data/inf/scripts/silver/silver_accounts.py", "opal-data-inf", "code/silver/silver_accounts.py", "inf"),
        ("data/inf/scripts/gold/lib/dtype_coerce.py", "opal-data-inf", "code/gold/lib/dtype_coerce.py", "inf"),
        ("data/black_diamond/scripts/gold/B_00.py", "opal-data-bd", "code/gold/B_00.py", "bd"),
        ("data/black_diamond/scripts/silver/lib/dtype_coerce.py", "opal-data-bd", "code/silver/lib/dtype_coerce.py", "bd"),
        # Out-of-scope paths -> None
        ("data/seeking-alpha/scripts/fetch.py", None, None, None),
        ("infra/aws/terraform/main.tf", None, None, None),
        ("data/inf/scripts/archive/old.py", None, None, None),  # not gold/silver/bronze
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
# Case 7: PIPESCRIPT-VERDICT — the verify-output parser is correct on a KNOWN-GOOD
# and a KNOWN-BAD fixture (ADHC_PREFLT canonical case study, CTO 20260701T1747Z).
# Regression-guards the substring false-fail: `"STALE" in output` matched the summary
# line's "0 STALE" LABEL -> FAIL on every clean deploy. It was invisible until the
# scope-to-changed-script fix (b) made the gate reliably COMPLETE (a never-completing
# gate hides its own verdict-logic bug). This asserts the gate emits the CORRECT
# verdict end-to-end, not merely that it "fails loud".
# ---------------------------------------------------------------------------
def test_pipescript_verdict_parse():
    known_good = "  Summary: 1 MATCH, 0 STALE, 0 MISSING_ON_S3, 0 LOCAL_MISSING, 0 UNCOVERED"
    known_bad_stale = "  [SILVER] foo.py  STALE\n  Summary: 0 MATCH, 1 STALE, 0 MISSING_ON_S3"
    known_bad_missing = "  Summary: 0 MATCH, 0 STALE, 1 MISSING_ON_S3, 0 LOCAL_MISSING"
    nosum_good = "  [SILVER] foo.py                        MATCH"
    nosum_bad = "  [SILVER] foo.py                        STALE"

    # KNOWN-GOOD must PASS (the exact regression the substring bug broke -- "0 STALE" != a real STALE)
    assert _pipescript_output_ok(known_good) is True, \
        "Case 7 FAIL: clean '0 STALE' summary must be OK (the substring-false-fail regression)"
    # KNOWN-BAD must FAIL loud
    assert _pipescript_output_ok(known_bad_stale) is False, "Case 7 FAIL: 1 STALE must fail"
    assert _pipescript_output_ok(known_bad_missing) is False, "Case 7 FAIL: 1 MISSING_ON_S3 must fail"
    # No-summary fallback (per-line status scan)
    assert _pipescript_output_ok(nosum_good) is True, "Case 7 FAIL: no-summary MATCH must be OK"
    assert _pipescript_output_ok(nosum_bad) is False, "Case 7 FAIL: no-summary STALE must fail"
    return True


# ===========================================================================
# Phase-1 serve-gate cases (CTO, Andrew-approved). Drive main() end-to-end with a
# stubbed WORKSPACE (real temp files, so the sentinel read + upload md5 are real)
# and a subprocess mock that emulates git diff / git show / git log / aws.
# ===========================================================================

def _make_main_mock(diff_files, old_blobs, log_body, authors, uploads, sha="abc1234"):
    """subprocess.run stub for a full main() run.

    diff_files : list[str]  -> `git diff --name-only ...` output (candidate set)
    old_blobs  : dict path->str  -> `git show <old>:<path>` content; MISSING key =>
                 file absent in old_ref (rc!=0 with a 'does not exist in' stderr).
    log_body   : str  -> `git log <range> --format=%B` body (WHOLE range; the ACK
                 may sit on ANY commit here -- the peer-sweep vector).
    authors    : dict path->str  -> `git log ... --format=%an -1 -- <path>`
    uploads    : dict  -> recorded {s3_key: md5(local)} so head-object returns MATCH.
    """
    def _run(cmd, **kwargs):
        r = MagicMock()
        argv = [str(c) for c in cmd]
        joined = " ".join(argv)
        prog = os.path.basename(argv[0]).lower()
        r.returncode, r.stdout, r.stderr = 0, "", ""

        if prog.startswith("git"):
            sub = argv[1] if len(argv) > 1 else ""
            if sub == "diff":
                r.stdout = "".join(f"{f}\n" for f in diff_files)
            elif sub == "show":
                ref_path = argv[2]
                path = ref_path.split(":", 1)[1] if ":" in ref_path else ""
                if path in old_blobs:
                    r.stdout = old_blobs[path]
                else:
                    r.returncode = 128
                    r.stderr = f"fatal: path '{path}' does not exist in '{ref_path.split(':', 1)[0]}'"
            elif sub == "log":
                if "--format=%an" in argv:
                    r.stdout = authors.get(argv[-1], "someone") + "\n"
                elif "--format=%B" in argv:
                    r.stdout = log_body
            elif sub == "rev-parse":
                r.stdout = sha + "\n"
            return r

        # aws
        if "s3 cp" in joined:
            src, dst = argv[3], argv[4]
            key = dst.split("/", 3)[3] if dst.startswith("s3://") else dst
            uploads[key] = _md5(pathlib.Path(src).read_bytes())
        elif "head-object" in joined:
            key = argv[argv.index("--key") + 1]
            r.stdout = f'"{uploads.get(key, "")}"\n'
        return r
    return _run


def _run_serve_gate(argv, files_content, diff_files, old_blobs="same",
                    log_body="", authors=None):
    """Set up a temp WORKSPACE, run main(argv), return (rc, stdout, uploads).

    files_content : dict rel_path -> current (working-tree) content, written to temp.
    old_blobs     : dict path->str for `git show <old>:<path>`, or the string "same"
                    meaning "old == current content" (no removal), or "absent" meaning
                    every file is new (rc!=0 in old_ref).
    """
    authors = authors or {}
    with tempfile.TemporaryDirectory() as td:
        ws = pathlib.Path(td)
        for rel, content in files_content.items():
            p = ws / rel.replace("/", os.sep)
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")
        if old_blobs == "same":
            old_blobs = dict(files_content)
        elif old_blobs == "absent":
            old_blobs = {}
        uploads: dict[str, str] = {}
        audit = ws / "org" / "safe-deploy-bypass-audit.log"
        mock = _make_main_mock(diff_files, old_blobs, log_body, authors, uploads)
        buf = io.StringIO()
        with patch.object(_core, "WORKSPACE", ws), \
             patch.object(_core, "BYPASS_AUDIT_LOG", audit), \
             patch("safe_deploy_core.subprocess.run", side_effect=mock), \
             patch("safe_deploy_core._find_aws", return_value="/usr/bin/aws"), \
             contextlib.redirect_stdout(buf):
            rc = main(argv)
        out = buf.getvalue()
        audit_text = audit.read_text(encoding="utf-8") if audit.exists() else ""
    return rc, out, uploads, audit_text


_GOLD = "data/inf/scripts/gold/INF_D_01.py"
_GOLD2 = "data/inf/scripts/gold/INF_D_02.py"
_HELD_LINE = "# DEPLOY-SERVE-HELD: waiting on CTO signoff\n"


# ---------------------------------------------------------------------------
# Case 8 (a): SERVE-HELD sentinel -> file SKIPPED (not in the deploy/upload set)
# ---------------------------------------------------------------------------
def test_serve_held_skip():
    rc, out, uploads, _ = _run_serve_gate(
        ["--no-pipescript", "--commit-range", "old111..new222"],
        files_content={_GOLD: _HELD_LINE + "print('gold')\n"},
        diff_files=[_GOLD],
    )
    assert rc == 0, f"Case 8 FAIL: held-only push should exit 0, got {rc}\n{out}"
    assert "code/gold/INF_D_01.py" not in uploads, \
        f"Case 8 FAIL: HELD file was uploaded (should be skipped): {uploads}"
    assert "SERVE-HELD: data/inf/scripts/gold/INF_D_01.py" in out, \
        f"Case 8 FAIL: SERVE-HELD note not emitted\n{out}"
    return True


# ---------------------------------------------------------------------------
# Case 8b (malformed control): a no-reason / malformed sentinel STILL skips.
# Fail-closed DIRECTION: a parse ambiguity must resolve toward NOT serving.
# ---------------------------------------------------------------------------
def test_serve_held_malformed_still_skips():
    rc, out, uploads, _ = _run_serve_gate(
        ["--no-pipescript", "--commit-range", "old111..new222"],
        files_content={_GOLD: "#DEPLOY-SERVE-HELD\nprint('gold')\n"},  # no space, NO reason
        diff_files=[_GOLD],
    )
    assert rc == 0, f"Case 8b FAIL: malformed-held push should exit 0, got {rc}\n{out}"
    assert "code/gold/INF_D_01.py" not in uploads, \
        f"Case 8b FAIL: malformed/no-reason sentinel was NOT treated as held: {uploads}"
    assert "SERVE-HELD:" in out and "(no reason given)" in out, \
        f"Case 8b FAIL: malformed sentinel note/ reason-fallback missing\n{out}"
    return True


# ---------------------------------------------------------------------------
# Case 9 (b1): removing a sentinel with NO SERVE-RELEASE-ACK -> gate REFUSES
# (non-zero, nothing uploaded).
# ---------------------------------------------------------------------------
def test_serve_release_blocked_no_ack():
    rc, out, uploads, _ = _run_serve_gate(
        ["--no-pipescript", "--commit-range", "base000..tip999"],
        files_content={_GOLD: "print('gold')\n"},              # CURRENT: no sentinel
        diff_files=[_GOLD],
        old_blobs={_GOLD: _HELD_LINE + "print('gold')\n"},     # BASE had the sentinel
        log_body="just a normal commit\nno ack here\n",
    )
    assert rc != 0, f"Case 9 FAIL: removal w/o ACK must refuse (non-zero), got {rc}\n{out}"
    assert not uploads, f"Case 9 FAIL: nothing may deploy on a blocked removal: {uploads}"
    assert "SERVE-RELEASE BLOCKED" in out, f"Case 9 FAIL: BLOCKED note missing\n{out}"
    return True


# ---------------------------------------------------------------------------
# Case 10 (b2): removal WITH `SERVE-RELEASE-ACK: <reason>` on ANY commit in the
# range (peer-sweep: the ack sits on a NON-TIP commit) -> proceeds + audits.
# Proves range-spanning: base-vs-current removal + whole-range ACK scan.
# ---------------------------------------------------------------------------
def test_serve_release_authorized_with_ack():
    peer_sweep_log = (
        "tip commit by another agent -- unrelated sweep\n\n"
        "----\n"
        "release the hold on INF_D_01\n\n"
        "SERVE-RELEASE-ACK: CTO+COO never-widen signoff LD-xxxx\n\n"
        "----\n"
        "base+1 commit\n"
    )
    rc, out, uploads, audit = _run_serve_gate(
        ["--no-pipescript", "--commit-range", "base000..tip999", "--author", "0.4.0_DS_ClientPlatform"],
        files_content={_GOLD: "print('gold')\n"},              # CURRENT: no sentinel
        diff_files=[_GOLD],
        old_blobs={_GOLD: _HELD_LINE + "print('gold')\n"},     # BASE had the sentinel
        log_body=peer_sweep_log,
    )
    assert rc == 0, f"Case 10 FAIL: acked removal should proceed (exit 0), got {rc}\n{out}"
    assert "code/gold/INF_D_01.py" in uploads, \
        f"Case 10 FAIL: acked file was not deployed: {uploads}"
    assert "SERVE-RELEASE authorized" in out, f"Case 10 FAIL: authorized note missing\n{out}"
    assert "SERVE-RELEASE" in audit and "CTO+COO never-widen signoff" in audit, \
        f"Case 10 FAIL: SERVE-RELEASE audit entry (+reason) missing\n{audit!r}"
    return True


# ---------------------------------------------------------------------------
# Case 10b (malformed control): an EMPTY / malformed SERVE-RELEASE-ACK does NOT
# release a removal (the \\s*-crosses-newline fail-OPEN inversion). Fail-closed:
# the reason must be non-empty and on the ACK's own line.
# ---------------------------------------------------------------------------
def test_serve_release_empty_ack_does_not_release():
    empty_ack_log = "removing the hold\n\nSERVE-RELEASE-ACK:\nsome later commit line\n"
    rc, out, uploads, _ = _run_serve_gate(
        ["--no-pipescript", "--commit-range", "base000..tip999"],
        files_content={_GOLD: "print('gold')\n"},
        diff_files=[_GOLD],
        old_blobs={_GOLD: _HELD_LINE + "print('gold')\n"},
        log_body=empty_ack_log,   # ACK token present but EMPTY reason -> must NOT release
    )
    assert rc != 0, f"Case 10b FAIL: empty ACK must NOT release (non-zero), got {rc}\n{out}"
    assert not uploads, f"Case 10b FAIL: empty ACK deployed anyway: {uploads}"
    assert "SERVE-RELEASE BLOCKED" in out, f"Case 10b FAIL: BLOCKED note missing\n{out}"
    return True


# ---------------------------------------------------------------------------
# Case 11 (c): the enumeration notice shows the commit AUTHOR of each file.
# ---------------------------------------------------------------------------
def test_author_enumeration_notice():
    rc, out, uploads, _ = _run_serve_gate(
        ["--no-pipescript", "--commit-range", "base000..tip999"],
        files_content={_GOLD: "print('gold')\n"},
        diff_files=[_GOLD],
        authors={_GOLD: "0.7.0_AE_CloudOps"},
    )
    assert rc == 0, f"Case 11 FAIL: clean push should exit 0, got {rc}\n{out}"
    assert "(authored by 0.7.0_AE_CloudOps)" in out, \
        f"Case 11 FAIL: author not shown in enumeration\n{out}"
    assert "-> code/gold/" in out, f"Case 11 FAIL: target prefix not shown\n{out}"
    return True


# ---------------------------------------------------------------------------
# Case 12 (d): NO-REGRESSION -- a clean deploy-scope change with NO sentinel and
# NO removal deploys EXACTLY as before (same files, same S3 targets, exit 0).
# The load-bearing positive control.
# ---------------------------------------------------------------------------
def test_no_regression_clean_deploy():
    rc, out, uploads, audit = _run_serve_gate(
        ["--no-pipescript", "--commit-range", "base000..tip999"],
        files_content={
            _GOLD: "print('gold one')\n",
            _GOLD2: "print('gold two')\n",
        },
        diff_files=[_GOLD, _GOLD2],
        old_blobs="same",   # base == current -> no sentinel history, no removal
        log_body="ordinary gold refresh\n",
    )
    assert rc == 0, f"Case 12 FAIL: clean push must exit 0, got {rc}\n{out}"
    assert set(uploads.keys()) == {"code/gold/INF_D_01.py", "code/gold/INF_D_02.py"}, \
        f"Case 12 FAIL: deploy set/targets changed: {sorted(uploads)}"
    assert "DEPLOYED  [inf] data/inf/scripts/gold/INF_D_01.py" in out, \
        f"Case 12 FAIL: normal DEPLOYED line missing\n{out}"
    assert "SERVE-HELD" not in out and "SERVE-RELEASE" not in out, \
        f"Case 12 FAIL: a clean push must emit no serve-gate notes\n{out}"
    assert audit == "", f"Case 12 FAIL: clean push must write no audit entry\n{audit!r}"
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
    ("INF-PATH data/inf->opal-data-inf routing", test_inf_path_resolution),
    ("PIPESCRIPT-VERDICT parser known-good/known-bad", test_pipescript_verdict_parse),
    ("SERVE-HELD sentinel skips file", test_serve_held_skip),
    ("SERVE-HELD malformed/no-reason still skips", test_serve_held_malformed_still_skips),
    ("SERVE-RELEASE removal w/o ACK refuses", test_serve_release_blocked_no_ack),
    ("SERVE-RELEASE removal w/ range ACK proceeds+audits", test_serve_release_authorized_with_ack),
    ("SERVE-RELEASE empty ACK does not release", test_serve_release_empty_ack_does_not_release),
    ("AUTHOR enumeration notice shows author", test_author_enumeration_notice),
    ("NO-REGRESSION clean deploy unchanged", test_no_regression_clean_deploy),
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
