#!/usr/bin/env python3
"""NFRA_CTLPLN round 21, FWD-5 positive arm (cell CT-ak-3 read; built by cell CT-ak-4). READ-ONLY.

Only `aws s3api head-object`, `list-object-versions` and `list-objects-v2` are called, through the
.tools/aws(.cmd) shim; the guard in aws() refuses anything else. Nothing is written anywhere.

Modes:
  python .tools/tests/test_round21_fwd5_positive_read.py                 (default: post-deploy read)
  python .tools/tests/test_round21_fwd5_positive_read.py --pre           (pre-deploy state)
  python .tools/tests/test_round21_fwd5_positive_read.py --docstring-only (AST of the last commit that
                                                                         touched the script vs its parent)

LAST lines:
  default: FWD5-POSITIVE versions=<n> etag_equals_repo_md5=<True|False> other_changed=<n> audit_actor=<serial|NONE-WRITTEN|UNKNOWN> ok=<True|False>
  --pre:   FWD5-PRE target=diag_sleeve_fix.py versions=<n> repo_blob=<10 hex> repo_md5=<hex> s3_etag=<hex> differs=<True|False> others_differ=<n> ok=<True|False>
  --docstring-only: DOCSTRING-ONLY docstring_only=<True|False>

Repository side is read from git objects at HEAD (a file in the worktree is never trusted for the md5).
Pagination is explicit: --no-paginate plus the continuation/marker token, looped until IsTruncated is false,
and every row is counted client-side with the page count printed.

default ok = versions == 2 AND etag_equals AND other_changed == 0 (other_changed is -1 while the ledger
entry is unreadable, which makes ok False). audit_actor is reported, not graded.
--pre ok = the target differs from S3 AND others_differ == 0 (a multipart ETag is 'skipped', not a difference;
an absent object is a difference).
"""
import ast
import hashlib
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
ROOT = TOOLS.parent
BUCKET = "opal-data-bd"
TARGET = "diag_sleeve_fix.py"
KEY = "code/gold/" + TARGET
PREFIX = "code/gold/"
REPO_DIR = "data/black_diamond/scripts/gold"
REPO_PATH = REPO_DIR + "/" + TARGET
SENTINEL_REL = "org/critical_paths/.open_deploys/ctlpln-r21-fwd5-one-script-20261015.json"
AUDIT_REL = "org/safe-deploy-bypass-audit.log"
AWS = str(TOOLS / "aws.cmd") if os.name == "nt" else str(TOOLS / "aws")
READ_OPS = ("head-object", "list-object-versions", "list-objects-v2")
DOC_NODES = (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)


def aws(*args):
    """One read-only aws s3api call. Returns (rc, stdout, stderr)."""
    if len(args) < 2 or args[0] != "s3api" or args[1] not in READ_OPS:
        raise SystemExit("REFUSED: not a read-only s3api call: %r" % (args,))
    try:
        p = subprocess.run([AWS, *args, "--output", "json"], capture_output=True, text=True,
                           encoding="utf-8", errors="replace", stdin=subprocess.DEVNULL, timeout=120)
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"
    return p.returncode, p.stdout, p.stderr


def git_bytes(*args):
    p = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, stdin=subprocess.DEVNULL)
    return p.returncode, p.stdout


def head_blob_bytes(path):
    rc, out = git_bytes("cat-file", "blob", "HEAD:" + path)
    if rc != 0:
        raise SystemExit("ERROR: git cat-file blob HEAD:%s rc=%s" % (path, rc))
    return out


def head_blob_sha(path):
    rc, out = git_bytes("rev-parse", "HEAD:" + path)
    return out.decode("ascii").strip() if rc == 0 else "UNKNOWN"


def read_repo_file(rel):
    """Worktree copy when the sparse checkout holds it, else the HEAD blob; None when neither exists."""
    f = ROOT / rel
    if f.exists():
        return f.read_text(encoding="utf-8", errors="replace"), "worktree"
    rc, out = git_bytes("cat-file", "blob", "HEAD:" + rel)
    if rc == 0:
        return out.decode("utf-8", errors="replace"), "HEAD"
    return None, "absent"


def list_all_versions(key):
    """Every version row whose Key is exactly `key`. Returns (rows, pages) or (None, pages) on error."""
    rows, pages, km, vm = [], 0, None, None
    while True:
        args = ["s3api", "list-object-versions", "--bucket", BUCKET, "--prefix", key, "--no-paginate"]
        if km:
            args += ["--key-marker", km]
        if vm:
            args += ["--version-id-marker", vm]
        rc, out, err = aws(*args)
        if rc != 0:
            print("ERROR: list-object-versions rc=%s: %s" % (rc, err.strip()[:200]))
            return None, pages
        d = json.loads(out or "{}")
        pages += 1
        rows += [v for v in d.get("Versions", []) if v.get("Key") == key]
        if not d.get("IsTruncated"):
            return rows, pages
        km, vm = d.get("NextKeyMarker"), d.get("NextVersionIdMarker")
        if not km:
            print("ERROR: list-object-versions truncated without NextKeyMarker")
            return None, pages


def list_all_objects(prefix):
    """Every object under `prefix`, paginated by continuation token. Returns (objects, pages) or (None, pages)."""
    objs, pages, token = [], 0, None
    while True:
        args = ["s3api", "list-objects-v2", "--bucket", BUCKET, "--prefix", prefix, "--no-paginate"]
        if token:
            args += ["--continuation-token", token]
        rc, out, err = aws(*args)
        if rc != 0:
            print("ERROR: list-objects-v2 rc=%s: %s" % (rc, err.strip()[:200]))
            return None, pages
        d = json.loads(out or "{}")
        pages += 1
        objs += d.get("Contents", [])
        if not d.get("IsTruncated"):
            return objs, pages
        token = d.get("NextContinuationToken")
        if not token:
            print("ERROR: list-objects-v2 truncated without NextContinuationToken")
            return None, pages


def head(key):
    """('ok', body) | ('absent', None) | ('error', message)."""
    rc, out, err = aws("s3api", "head-object", "--bucket", BUCKET, "--key", key)
    if rc == 0:
        return "ok", json.loads(out or "{}")
    if "404" in err or "NotFound" in err or "Not Found" in err:
        return "absent", None
    return "error", err.strip()[:200]


def etag_of(body):
    return body["ETag"].strip('"')


def is_multipart(etag):
    return "-" in etag


def mode_pre():
    rows, pages = list_all_versions(KEY)
    n_versions = len(rows) if rows is not None else -1
    print("versions: %d exact-key version(s) of %d page(s) for key %s" % (n_versions, pages, KEY))
    repo_md5 = hashlib.md5(head_blob_bytes(REPO_PATH)).hexdigest()
    blob = head_blob_sha(REPO_PATH)
    st, body = head(KEY)
    if st != "ok":
        print("ERROR: head-object %s: %s" % (KEY, st if body is None else body))
        s3_etag, differs = "UNREAD", False
    else:
        s3_etag = etag_of(body)
        differs = (not is_multipart(s3_etag)) and s3_etag != repo_md5
        print("target: s3 ETag %s  repo(HEAD) md5 %s  s3 bytes %s" % (s3_etag, repo_md5, body.get("ContentLength")))

    rc, out = git_bytes("ls-tree", "--name-only", "HEAD", REPO_DIR + "/")
    names = []
    for line in out.decode("utf-8", errors="replace").splitlines():
        rest = line[len(REPO_DIR) + 1:]
        if "/" not in rest and rest.endswith(".py") and rest != TARGET:
            names.append(rest)
    print("others: %d top-level .py file(s) under %s at HEAD (target excluded)" % (len(names), REPO_DIR))

    def check(name):
        md5 = hashlib.md5(head_blob_bytes(REPO_DIR + "/" + name)).hexdigest()
        st2, body2 = head(PREFIX + name)
        if st2 == "absent":
            return name, "DIFFERS-ABSENT", md5, None
        if st2 == "error":
            return name, "DIFFERS-UNREADABLE", md5, body2
        et = etag_of(body2)
        if is_multipart(et):
            return name, "SKIPPED-MULTIPART", md5, et
        return name, ("EQUAL" if et == md5 else "DIFFERS"), md5, et

    with ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(check, names))
    tally = {}
    for name, verdict, md5, et in results:
        tally[verdict] = tally.get(verdict, 0) + 1
        if verdict != "EQUAL":
            print("  %s %s repo_md5=%s s3_etag=%s" % (verdict, name, md5, et))
    print("others tally: " + " ".join("%s=%d" % (k, v) for k, v in sorted(tally.items())) +
          " (denominator %d)" % len(results))
    others_differ = sum(v for k, v in tally.items() if k.startswith("DIFFERS"))

    ok = differs and others_differ == 0
    print("FWD5-PRE target=%s versions=%d repo_blob=%s repo_md5=%s s3_etag=%s differs=%s others_differ=%d ok=%s"
          % (TARGET, n_versions, blob[:10], repo_md5, s3_etag, differs, others_differ, ok))
    return 0 if ok else 1


def mode_default():
    versions, etag_eq, other, actor, opened = -1, False, -1, "UNKNOWN", None
    text, src = read_repo_file(SENTINEL_REL)
    try:
        if text is None:
            raise ValueError("entry absent in worktree and HEAD")
        opened = datetime.fromisoformat(json.loads(text)["opened_at"].replace("Z", "+00:00"))
    except Exception as exc:
        print("ERROR: ledger entry %s unreadable: %s" % (SENTINEL_REL, exc))

    rows, pages = list_all_versions(KEY)
    if rows is not None:
        versions = len(rows)
        print("versions: %d exact-key version(s) of %d page(s)" % (versions, pages))
        for v in sorted(rows, key=lambda x: x["LastModified"]):
            print("  version %s etag %s modified %s latest=%s" % (v["VersionId"], v["ETag"], v["LastModified"], v["IsLatest"]))

    repo_md5 = hashlib.md5(head_blob_bytes(REPO_PATH)).hexdigest()
    st, body = head(KEY)
    if st == "ok":
        etag = etag_of(body)
        etag_eq = (not is_multipart(etag)) and etag == repo_md5
        print("etag: s3 %s  repo(HEAD) md5 %s  s3 bytes %s" % (etag, repo_md5, body.get("ContentLength")))
    else:
        print("ERROR: head-object %s: %s" % (KEY, st))

    objs, opages = list_all_objects(PREFIX)
    if objs is not None and opened is not None:
        changed = [o for o in objs if o["Key"] != KEY and
                   datetime.fromisoformat(o["LastModified"].replace("Z", "+00:00")) > opened]
        other = len(changed)
        print("other_changed: %d of %d key(s) under %s (%d page(s), script key excluded) modified after %s"
              % (other, len(objs), PREFIX, opages, opened.strftime("%Y-%m-%dT%H:%M:%SZ")))
        for o in changed:
            print("  CHANGED %s %s" % (o["Key"], o["LastModified"]))

    audit, asrc = read_repo_file(AUDIT_REL)
    if audit is None:
        print("audit: %s unreadable in worktree and HEAD" % AUDIT_REL)
    else:
        lines = [ln for ln in audit.splitlines() if REPO_PATH in ln]
        print("audit (%s): %d row(s) name %s" % (asrc, len(lines), REPO_PATH))
        if lines:
            f = lines[-1].split()
            actor = f[2] if len(f) > 2 else "UNKNOWN"
            print("  last: %s" % lines[-1][:200])
        else:
            actor = "NONE-WRITTEN"

    ok = versions == 2 and etag_eq and other == 0
    print("FWD5-POSITIVE versions=%d etag_equals_repo_md5=%s other_changed=%d audit_actor=%s ok=%s"
          % (versions, etag_eq, other, actor, ok))
    return 0 if ok else 1


def strip_docstrings(tree, broad):
    """strict: the first statement of a module, class or function when it is a string (Python's definition).
    broad: every bare string-expression statement in those bodies (diagnostic only; it is not the verdict)."""
    for node in ast.walk(tree):
        if isinstance(node, DOC_NODES):
            kept = []
            for i, s in enumerate(node.body):
                is_str = isinstance(s, ast.Expr) and isinstance(s.value, ast.Constant) and isinstance(s.value.value, str)
                if is_str and (broad or i == 0):
                    continue
                kept.append(s)
            node.body = kept or [ast.Pass()]
    return tree


def mode_docstring_only():
    rc, out = git_bytes("log", "-1", "--format=%H", "--", REPO_PATH)
    commit = out.decode("ascii").strip()
    if rc != 0 or not commit:
        print("ERROR: no commit touches %s" % REPO_PATH)
        return 1
    rc, out = git_bytes("rev-parse", commit + "^")
    parent = out.decode("ascii").strip()
    rc1, before = git_bytes("cat-file", "blob", parent + ":" + REPO_PATH)
    rc2, after = git_bytes("cat-file", "blob", commit + ":" + REPO_PATH)
    if rc1 != 0 or rc2 != 0:
        print("ERROR: cannot read %s at %s or %s" % (REPO_PATH, parent, commit))
        return 1
    b_src = before.decode("utf-8")
    a_src = after.decode("utf-8")
    strict_eq = ast.dump(strip_docstrings(ast.parse(b_src), False)) == ast.dump(strip_docstrings(ast.parse(a_src), False))
    broad_eq = ast.dump(strip_docstrings(ast.parse(b_src), True)) == ast.dump(strip_docstrings(ast.parse(a_src), True))
    print("compared %s: before=%s (parent) at=%s (last commit touching the file)" % (REPO_PATH, parent[:10], commit[:10]))
    print("INFO bare-string-statements-only equal=%s (diagnostic; not the verdict)" % broad_eq)
    print("DOCSTRING-ONLY docstring_only=%s" % strict_eq)
    return 0 if strict_eq else 1


def main(argv):
    if "--pre" in argv:
        return mode_pre()
    if "--docstring-only" in argv:
        return mode_docstring_only()
    return mode_default()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
