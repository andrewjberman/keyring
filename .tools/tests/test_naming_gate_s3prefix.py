"""NFRA_OPLGTW OG-ng-1 (round 37, workstream NAMING-S3PREFIX; the order's A1 read against the laptop CTO's seven conditions,
RULING_20261015_064xZ_NAMING_GATE_IAM_PREFIX_CLAUSE_CONDITIONS.md @bf9198273e): the naming gate's S3PREFIX clause.

OFFLINE. Each test builds a THROWAWAY git repo in a temp directory: a copy of .tools/naming-gate.py (which takes its REPO from its
own path, so the copy grades the temp repo), lib/opal_naming.py, the schema, and the registry directory, with a legacy_addresses.json
COMMITTED at HEAD of that temp repo. The real repo's HEAD is only read (git show HEAD:...), never written. The gate runs as a
subprocess from the temp repo, so each verdict line is the gate's own CLI output.

The probe diffs put their .tf under infra/probe/ (not infra/aws/, which would load the placement step) and carry one file under
org/missions/D9/NFRA/NFRA_OPLGTW/ so the committing project is derivable (NFRA_OPLGTW). A test that wants NO derivable project omits it.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GATE = os.path.join(ROOT, ".tools", "naming-gate.py")
LIB = os.path.join(ROOT, "lib", "opal_naming.py")
LIB_DIR = os.path.join(ROOT, "lib")
SERVED_PATHS_REL = "org/missions/D14/LGIC/LGIC_NAMING/deliverables/LEGACY_SERVED_PATHS.json"
SCHEMA = os.path.join(ROOT, "org", "standards", "NAMING_SCHEMA.json")
DIRECTIVES = os.path.join(ROOT, "org", "missions", "DIRECTIVES.yaml")
REGISTRY_DIR = os.path.join(ROOT, "infra", "logic", "registry")
LEGACY_REL = "infra/logic/registry/legacy_addresses.json"
PROJECT_PATH = "org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/probe.md"
TF_PATH = "infra/probe/s3prefix.tf"
BUCKET = "opal-data-etfs"
VERDICT_RE = re.compile(r"^NAMING (\S+) (\S+):(\d+) (.*?) -> ")
IAM_RE = re.compile(r"^IAM-PREFIX-ADMITTED n=(\d+) bucket=(\S+) prefixes=\[(.*)\] registry_head=([0-9a-f]{12})$")

# The rows the four OG-ap-20 ETF prefixes rest on: committed at HEAD by f636989b97 (reader NFRA_OPLGTW, bucket opal-data-etfs).
REAL_ETF_PREFIXES = ["gold/book/*", "gold/holding/*", "platinum/reports/*", "silver/holdings/*"]


def _git(repo, *args, check=True):
    p = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True, encoding="utf-8")
    if check and p.returncode != 0:
        raise AssertionError("git %s rc=%d: %s" % (" ".join(args), p.returncode, p.stderr.strip()))
    return p


def _real_head_legacy_doc():
    """The legacy_addresses.json COMMITTED at the real repo's HEAD (read only), as a dict."""
    p = _git(ROOT, "show", "HEAD:" + LEGACY_REL)
    return json.loads(p.stdout)


def _fixture_row(key, template, reader, bucket=BUCKET, shape="prefix"):
    return {"key": key, "bucket": bucket, "template": template, "shape": shape, "params": [], "reader": reader,
            "evidence": "fixture of the NFRA_OPLGTW OG-ng-1 S3PREFIX tests (offline; no AWS read)",
            "note": "test fixture for the naming gate's s3:prefix clause; not a real address"}


def _build_repo(head_rows=(), wt_rows=(), index_rows=()):
    """A temp git repo with the gate, its library and registry; legacy_addresses.json = the real HEAD rows + head_rows COMMITTED.
    wt_rows are written to the working tree only; index_rows are written and staged, NOT committed."""
    tmp = tempfile.mkdtemp(prefix="ng1_s3prefix_")
    os.makedirs(os.path.join(tmp, ".tools"))
    os.makedirs(os.path.join(tmp, "lib"))
    os.makedirs(os.path.join(tmp, "org", "standards"))
    os.makedirs(os.path.join(tmp, "org", "missions"))
    shutil.copy(GATE, os.path.join(tmp, ".tools", "naming-gate.py"))
    for name in sorted(os.listdir(LIB_DIR)):  # every top-level library module the gate's readers import (no tests folder)
        if name.endswith(".py"):
            shutil.copy(os.path.join(LIB_DIR, name), os.path.join(tmp, "lib", name))
    served_dir = os.path.dirname(os.path.join(tmp, *SERVED_PATHS_REL.split("/")))
    os.makedirs(served_dir)
    shutil.copy(os.path.join(ROOT, *SERVED_PATHS_REL.split("/")), os.path.join(tmp, *SERVED_PATHS_REL.split("/")))
    shutil.copy(SCHEMA, os.path.join(tmp, "org", "standards", "NAMING_SCHEMA.json"))
    shutil.copy(DIRECTIVES, os.path.join(tmp, "org", "missions", "DIRECTIVES.yaml"))
    shutil.copytree(REGISTRY_DIR, os.path.join(tmp, "infra", "logic", "registry"))
    base = _real_head_legacy_doc()
    base["legacy_addresses"] = list(base["legacy_addresses"]) + list(head_rows)
    legacy = os.path.join(tmp, *LEGACY_REL.split("/"))

    def write(doc):
        with open(legacy, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(doc, fh, indent=1)
            fh.write("\n")

    write(base)
    _git(tmp, "init", "-q")
    _git(tmp, "config", "user.email", "ng1-fixture@test.invalid")
    _git(tmp, "config", "user.name", "ng1-fixture")
    _git(tmp, "add", "-A")
    _git(tmp, "commit", "-q", "-m", "fixture HEAD: real legacy rows plus the head_rows")
    if index_rows:
        # the index carries the extra rows, the working tree does not: write, stage, then restore the working tree
        write(dict(base, legacy_addresses=base["legacy_addresses"] + list(index_rows)))
        _git(tmp, "add", LEGACY_REL)
        write(base)
    if wt_rows:
        write(dict(base, legacy_addresses=base["legacy_addresses"] + list(wt_rows)))
    return tmp


def _statement(value, bucket=BUCKET, key="s3:prefix", resource=None):
    res = resource if resource is not None else "arn:aws:s3:::%s" % bucket
    return ['    {', '      Effect = "Allow", Action = ["s3:ListBucket"], Resource = ["%s"],' % res,
            '      Condition = { StringLike = { "%s" = ["%s"] } }' % (key, value), '    },']


def _tf_file(statements, path=TF_PATH):
    """One .tf whose policy carries one statement per entry of `statements` (each a list of lines from _statement)."""
    body = ['resource "aws_iam_role_policy" "probe" {', '  policy = jsonencode({', '    Statement = [']
    for st in statements:
        body += st
    body += ['    ]', '  })', '}']
    return path, body


def _diff(files, with_project=True):
    parts = []
    for path, lines in files:
        parts.append("diff --git a/%s b/%s\nnew file mode 100644\n--- /dev/null\n+++ b/%s\n@@ -0,0 +1,%d @@\n%s\n"
                     % (path, path, path, len(lines), "\n".join("+" + ln for ln in lines)))
    if with_project:
        parts.append("diff --git a/%s b/%s\nnew file mode 100644\n--- /dev/null\n+++ b/%s\n@@ -0,0 +1,1 @@\n+probe\n"
                     % (PROJECT_PATH, PROJECT_PATH, PROJECT_PATH))
    return "".join(parts)


def _run_gate(repo, diff_text):
    d = tempfile.mkdtemp(prefix="ng1_diff_")
    dp = os.path.join(d, "probe.diff")
    with open(dp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(diff_text)
    p = subprocess.run([sys.executable, os.path.join(repo, ".tools", "naming-gate.py"), "--diff", dp],
                       cwd=repo, capture_output=True, text=True, encoding="utf-8", timeout=100)
    shutil.rmtree(d, ignore_errors=True)
    return p.returncode, p.stdout


def _verdicts(out):
    """{(path, string): verdict} of the gate's NAMING verdict lines (one per graded string)."""
    got = {}
    for ln in out.splitlines():
        m = VERDICT_RE.match(ln)
        if m:
            got[(m.group(2).split(":")[0], m.group(4))] = m.group(1)
    return got


def _iam_line(out):
    for ln in out.splitlines():
        m = IAM_RE.match(ln)
        if m:
            return m
    return None


def _admitted_values(out):
    m = _iam_line(out)
    if not m:
        return []
    return re.findall(r"'([^']*)'", m.group(3))


def _cleanup(repo):
    shutil.rmtree(repo, ignore_errors=True)


def _statements_for(values, bucket=BUCKET):
    return [_statement(v, bucket=bucket) for v in values]


# ---------------------------------------------------------------------------------------------------------------------------
def test_ng1_ac01():
    """AC01: a registered prefix with exactly one trailing '*', on the registered bucket, grades CONFORMANT (the four OG-ap-20 values)."""
    repo = _build_repo()
    try:
        path, lines = _tf_file(_statements_for(REAL_ETF_PREFIXES))
        rc, out = _run_gate(repo, _diff([(path, lines)]))
        v = _verdicts(out)
        for p in REAL_ETF_PREFIXES:
            assert v.get((TF_PATH, p)) == "CONFORMANT", "expected CONFORMANT for %r, got %r\n%s" % (p, v.get((TF_PATH, p)), out)
        assert sorted(_admitted_values(out)) == sorted(REAL_ETF_PREFIXES), out
    finally:
        _cleanup(repo)


def test_ng1_ac02():
    """AC02: the same value WITHOUT the trailing '*' is not admitted BY THIS CLAUSE (A1: "not admitted by this clause").
    Recorded, not hidden: at HEAD the MX-c-9 precedent already grades the bare key part CONFORMANT for its own reader (the
    verdict's why names that precedent, not this clause). This test asserts the clause's admission only."""
    repo = _build_repo()
    try:
        path, lines = _tf_file(_statements_for(["gold/book/"]))
        rc, out = _run_gate(repo, _diff([(path, lines)]))
        assert "gold/book/" not in _admitted_values(out), out
        assert not any("S3PREFIX clause" in ln for ln in out.splitlines()
                       if ln.startswith("  why:") and "gold/book/" in ln), out
    finally:
        _cleanup(repo)


# AC03 near misses, each REFUSED as the amended order states. The tier-first ones REFUSE at HEAD. A bare '*' (empty key part) and
# a non-tier-first unregistered prefix are NOT GRADED at HEAD (no verdict line; PASS, 0 graded): the gate refuses them only if a
# refusal is added, which the cell's bounds forbid. They stay in the list as stated; the test is RED on them until the issuer rules.
AC03_NEAR_MISSES = [
    "gold/book/**",       # a doubled wildcard
    "gold/*/book/*",      # a mid-path '*'
    "gold/book/?",        # a '?'
    "gold/book*",         # a prefix missing its trailing slash
    "gold/book/x/*",      # a prefix one segment longer
    "gold/*",             # a prefix one segment shorter
    "gold/nope/*",        # an unregistered tier-first prefix
    "*",                  # a bare '*' (empty key part)
    "nope/zzz/*",         # an unregistered, non-tier-first prefix
]


def test_ng1_ac03():
    """AC03: near misses are not admitted; the tier-first ones REFUSE, the bare and non-tier-first ones are not graded (status quo)."""
    repo = _build_repo()
    try:
        path, lines = _tf_file(_statements_for(AC03_NEAR_MISSES))
        rc, out = _run_gate(repo, _diff([(path, lines)]))
        v = _verdicts(out)
        assert _admitted_values(out) == [], out
        for value in AC03_NEAR_MISSES:
            got = v.get((TF_PATH, value))
            assert got == "REFUSE", "%r: expected REFUSE, got %r (no verdict line = not graded)\n%s" % (value, got, out)
    finally:
        _cleanup(repo)


def test_ng1_ac04():
    """AC04: a registered row whose reader is ANOTHER project does not admit the value (REFUSE)."""
    repo = _build_repo(head_rows=[_fixture_row("test-other-project-gold", "gold/other/", "NFRA_MCPINDEX")])
    try:
        path, lines = _tf_file(_statements_for(["gold/other/*"]))
        rc, out = _run_gate(repo, _diff([(path, lines)]))
        assert _verdicts(out).get((TF_PATH, "gold/other/*")) == "REFUSE", out
        assert _admitted_values(out) == [], out
    finally:
        _cleanup(repo)


def test_ng1_ac05():
    """AC05: a row present only in the working tree, or only in the index, admits nothing (HEAD only); the same row COMMITTED admits."""
    row = _fixture_row("test-own-late", "gold/late/", "NFRA_OPLGTW")
    path, lines = _tf_file(_statements_for(["gold/late/*"]))
    # control: committed at HEAD -> admitted
    repo = _build_repo(head_rows=[row])
    try:
        rc, out = _run_gate(repo, _diff([(path, lines)]))
        assert _verdicts(out).get((TF_PATH, "gold/late/*")) == "CONFORMANT", "control (committed) not admitted:\n" + out
    finally:
        _cleanup(repo)
    # working tree only
    repo = _build_repo(wt_rows=[row])
    try:
        rc, out = _run_gate(repo, _diff([(path, lines)]))
        assert _verdicts(out).get((TF_PATH, "gold/late/*")) == "REFUSE", "working-tree row admitted:\n" + out
        assert _admitted_values(out) == [], out
    finally:
        _cleanup(repo)
    # index only (staged, not committed)
    repo = _build_repo(index_rows=[row])
    try:
        rc, out = _run_gate(repo, _diff([(path, lines)]))
        assert _verdicts(out).get((TF_PATH, "gold/late/*")) == "REFUSE", "index-only row admitted:\n" + out
        assert _admitted_values(out) == [], out
    finally:
        _cleanup(repo)


def test_ng1_ac06():
    """AC06: the same string as a resource ARN, as a Resource, as a code literal, or under a key other than s3:prefix is not admitted
    and is graded as before: the bare value REFUSES as a Resource, as a code literal and under another key."""
    repo = _build_repo()
    try:
        arn_file = ("infra/probe/arn_probe.tf", ['resource "x" "y" {', '  policy = jsonencode({', '    Statement = [{',
                    '      Effect = "Allow", Action = ["s3:ListBucket"], Resource = ["arn:aws:s3:::opal-data-etfs/gold/book/*"],',
                    '      Condition = { StringLike = { "prefix" = ["zz-not-a-registered-value"] } }', '    }]', '  })', '}'])
        res_file = ("infra/probe/res_probe.tf", ['resource "x" "y" {', '  policy = jsonencode({', '    Statement = [{',
                    '      Effect = "Allow", Action = ["s3:ListBucket"], Resource = ["gold/book/*"],',
                    '      Condition = { StringLike = { "prefix" = ["zz-not-a-registered-value"] } }', '    }]', '  })', '}'])
        key_file = ("infra/probe/key_probe.tf", _tf_file([_statement("gold/book/*", key="prefix")])[1])
        py_file = ("infra/probe/literal_probe.py", ['PREFIX = "gold/book/*"'])
        rc, out = _run_gate(repo, _diff([arn_file, res_file, key_file, py_file]))
        v = _verdicts(out)
        assert v.get(("infra/probe/res_probe.tf", "gold/book/*")) == "REFUSE", "bare Resource: expected REFUSE\n" + out
        assert v.get(("infra/probe/key_probe.tf", "gold/book/*")) == "REFUSE", "other key: expected REFUSE\n" + out
        assert v.get(("infra/probe/literal_probe.py", "gold/book/*")) == "REFUSE", "code literal: expected REFUSE\n" + out
        assert _admitted_values(out) == [], out
    finally:
        _cleanup(repo)


def test_ng1_ac07():
    """AC07: a registered prefix granted on a DIFFERENT bucket (the statement's Resource ARN) REFUSES."""
    repo = _build_repo()
    try:
        path, lines = _tf_file([_statement("silver/holdings/*", bucket="opal-data-portal-v2")])
        rc, out = _run_gate(repo, _diff([(path, lines)]))
        assert _verdicts(out).get((TF_PATH, "silver/holdings/*")) == "REFUSE", out
        assert _admitted_values(out) == [], out
    finally:
        _cleanup(repo)


def test_ng1_ac08():
    """AC08: a commit that uses the clause prints IAM-PREFIX-ADMITTED n=<k> bucket=<b> prefixes=<list> registry_head=<sha> (HEAD's short sha)."""
    repo = _build_repo()
    try:
        path, lines = _tf_file(_statements_for(["gold/book/*"]))
        rc, out = _run_gate(repo, _diff([(path, lines)]))
        m = _iam_line(out)
        assert m is not None, "no IAM-PREFIX-ADMITTED line:\n" + out
        assert m.group(1) == "1" and m.group(2) == BUCKET and m.group(3) == "'gold/book/*'", out
        head = _git(repo, "rev-parse", "--short=12", "HEAD").stdout.strip()
        assert m.group(4) == head, "registry_head %s != HEAD %s" % (m.group(4), head)
    finally:
        _cleanup(repo)
