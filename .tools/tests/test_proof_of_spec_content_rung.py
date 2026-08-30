"""Controls for proof-of-spec-check's artifact-resolution CONTENT RUNG (2026-08-30, 1.0.0_SA_CTO~X on
1.0.0_SA_CTO 88109): `introduces` tokens must be PRESENT at the pin and ABSENT at the pin's parent.

A sealed temp git repo (never the live estate) with three commits on one file:
  A  tool.py = "old"                          (no token)
  B  tool.py += "git show :"                  (the fix: token INTRODUCED here)
  C  other.txt touched, tool.py unchanged     (token present at C AND at C~1)
Arms, each from a different truth:
  R1  row pinned at B with introduces -> CONTENT-resolved, 0 violations
  R2  row pinned at A with introduces -> VIOLATION "LACKS the token" (the 88109 class: pin exists, change absent)
  R3  row pinned at C with introduces -> VIOLATION "ALREADY present at the parent ... not introduced here"
  R4  row pinned at B WITHOUT introduces -> PRESENCE-ONLY counted, 0 violations (non-application stated)
  R5  PENDING row whose worktree file has the token and HEAD lacks it -> CONTENT-resolved
  R6  PENDING row whose token is at HEAD too -> VIOLATION not-introduced-here
  R7  malformed introduces (not a list of strings) -> VIOLATION, tokens ignored
  R8  the frame prints both counts with the 88109 label
  S1  the schema accepts `introduces` on a row and still refuses an unknown key

Run: python .tools/tests/test_proof_of_spec_content_rung.py   (exit 0 = all arms as expected)
"""
from __future__ import annotations

import importlib.util
import json
import pathlib
import subprocess
import sys
import tempfile

_SRC = pathlib.Path(__file__).resolve().parent.parent / "proof-of-spec-check.py"
_spec = importlib.util.spec_from_file_location("posc", _SRC)
posc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(posc)

results: list[tuple[str, bool, str]] = []


def arm(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, ok, detail))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}  {detail}")


def git(repo: pathlib.Path, *a: str) -> str:
    return subprocess.run(["git", *a], cwd=str(repo), capture_output=True, text=True, check=True).stdout.strip()


def row(pin: str, introduces=None, path="tool.py") -> dict:
    r = {"path_or_key": path, "kind": "script", "commit_or_etag": pin, "deployed_state": "COMMITTED-NOT-DEPLOY-SCOPE", "deploy_evidence": "test"}
    if introduces is not None:
        r["introduces"] = introduces
    return r


def run(rows: list) -> tuple[list, list]:
    return posc.artifact_resolution_check({"artifacts_produced": rows})


print("proof-of-spec-check CONTENT RUNG battery")
with tempfile.TemporaryDirectory(prefix="posc_cr_") as td:
    repo = pathlib.Path(td)
    git(repo, "init", "-q")
    git(repo, "config", "user.email", "t@t")
    git(repo, "config", "user.name", "t")
    git(repo, "config", "core.autocrlf", "false")
    (repo / "tool.py").write_text("old\n", encoding="utf-8")
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", "A")
    A = git(repo, "rev-parse", "HEAD")
    (repo / "tool.py").write_text("old\ngit show :\n", encoding="utf-8")
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", "B")
    B = git(repo, "rev-parse", "HEAD")
    (repo / "other.txt").write_text("x\n", encoding="utf-8")
    git(repo, "add", ".")
    git(repo, "commit", "-q", "-m", "C")
    C = git(repo, "rev-parse", "HEAD")
    saved = posc._REPO_ROOT
    posc._REPO_ROOT = repo
    try:
        v, f = run([row(B, ["git show :"])])
        arm("R1 pin B + introduces -> CONTENT-resolved, 0 violations", not v and "1 row(s) CONTENT-resolved" in f[-1], str(v)[:120])
        v, f = run([row(A, ["git show :"])])
        arm("R2 pin A + introduces -> VIOLATION 'LACKS the token' (88109 class)", len(v) == 1 and "LACKS the token" in v[0], str(v)[:140])
        v, f = run([row(C, ["git show :"])])
        arm("R3 pin C + introduces -> VIOLATION 'not introduced here'", len(v) == 1 and "not introduced here" in v[0], str(v)[:140])
        v, f = run([row(B)])
        arm("R4 pin B without introduces -> PRESENCE-ONLY, 0 violations", not v and "1 row(s) PRESENCE-ONLY" in f[-1], f[-1][:160])
        # R5: worktree carries a NEW token that HEAD (C) lacks
        (repo / "tool.py").write_text("old\ngit show :\nuploaded: index\n", encoding="utf-8")
        v, f = run([row(posc.PENDING_SENTINEL, ["uploaded: index"])])
        arm("R5 PENDING + token new in worktree -> CONTENT-resolved", not v and "1 row(s) CONTENT-resolved" in f[-1], str(v)[:120])
        v, f = run([row(posc.PENDING_SENTINEL, ["git show :"])])
        arm("R6 PENDING + token already at HEAD -> VIOLATION not-introduced-here", len(v) == 1 and "not introduced here" in v[0], str(v)[:140])
        v, f = run([row(B, "git show :")])
        arm("R7 malformed introduces -> VIOLATION, tokens ignored", len(v) == 1 and "not a list" in v[0], str(v)[:120])
        v, f = run([row(B, ["git show :"]), row(B), row(A, ["git show :"])])
        arm("R8 frame prints both counts with the 88109 label", "1 row(s) CONTENT-resolved" in f[-1] and "1 row(s) PRESENCE-ONLY" in f[-1] and "88109" in f[-1] and len(v) == 1, f[-1][:200])
    finally:
        posc._REPO_ROOT = saved

# S1 schema
schema = json.loads(posc.SCHEMA_PATH.read_text(encoding="utf-8"))
try:
    import jsonschema  # type: ignore
    item = schema["properties"]["artifacts_produced"]["items"]
    ok_row = {"path_or_key": "x", "kind": "script", "commit_or_etag": "abcdef1", "deployed_state": "COMMITTED-NOT-DEPLOY-SCOPE", "deploy_evidence": "e", "introduces": ["tok"]}
    bad_row = dict(ok_row)
    bad_row["introduce"] = ["tok"]
    del bad_row["introduces"]
    e_ok = list(jsonschema.Draft7Validator(item).iter_errors(ok_row))
    e_bad = list(jsonschema.Draft7Validator(item).iter_errors(bad_row))
    e_empty = list(jsonschema.Draft7Validator(item).iter_errors(dict(ok_row, introduces=[])))
    arm("S1 schema accepts `introduces` and refuses an unknown key and an empty list", not e_ok and bool(e_bad) and bool(e_empty), f"{len(e_ok)}/{len(e_bad)}/{len(e_empty)}")
except ImportError:
    arm("S1 schema arm: jsonschema not installed -- UNRUN (not a pass)", False, "install jsonschema")

failed = [r for r in results if not r[1]]
print(f"RESULT: {len(results) - len(failed)} of {len(results)} arms as expected -- failed {len(failed)}")
sys.exit(1 if failed else 0)
