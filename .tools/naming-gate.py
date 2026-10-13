#!/usr/bin/env python3
"""naming-gate.py -- the naming commit limb (LGIC_ENFORCE cell EN-g-1; PRD candidate E7; DEC-6).

Grades the ADDED lines of a unified diff with lib/opal_naming.py's grade(), and applies DEC-6's matrix:

    NEW and OUT-OF-PATTERN                                               REFUSE
    NEW and ALIAS                                                        REFUSE
    EXISTING, touched, and ALIAS                                         WARN
    EXISTING, in a surface remediations.json gives a live remediation,
      and OUT-OF-PATTERN                                                 REFUSE (unless the diff removes it)
    EXISTING anywhere else and OUT-OF-PATTERN                            WARN
    CONFORMANT                                                           pass
    NO-SYSTEM-ASKED (no system is asked of this kind of name; C-VERDICT)  pass (never refused for lacking a system)
    a hand edit to a GENERATED file (bytes differ from the generator's
      output), or the mark on a file the generator does not produce      REFUSE
    RAISE                                                                printed as a rule or registry defect

A string is NEW when it is absent from the file's pre-image at HEAD; every string of a `--- /dev/null` file is
NEW. A string is graded whole; since the diff removes nothing it grades, "unless the diff removes it" is the
case where the string sits only on removed lines, which are never graded.

THE CONTEXT RULE. A firm or product token is PERMITTED in the registry files (infra/logic/registry/*.json), in
a generated block or file, inside the arguments of a key(), address(), name() or lookup() call (read from the
Python syntax tree), or inside the arguments of a Terraform module whose source is the opal_name module.
Anywhere else a string carrying one is a HAND-KEPT CARRIER: a NEW one is refused, printing the registry
lookup that replaces it; an EXISTING one warns. NOT graded: prose (a string with whitespace, a docstring),
comments, Terraform block labels, and anything under a fixture folder, */tests/* or */test/* (FIXTURE_DIRS; the
generated-file check still runs there).

Inputs: S3 key and bucket literals, resource-name literals, secret paths, log groups, and firm and product
tokens as whole segments. File types: .py .js .mjs .ts .tf .json .yaml .yml. A JSON post-image whose top
level is a `terraform show -json` artifact (format_version and terraform_version present, with
resource_changes or planned_values) is SKIPPED, never graded (round-2 EN-g-1, row W1-S22); an authored JSON
file carrying the same strings is graded exactly as any other JSON file.

BEFORE any grading, the registry is validated (lib/opal_naming.py's validate()): a registry that loads but
that validate refuses is a `NAMING ERROR` naming the refusal, grading nothing (row W2-S9) -- enforcing this
exits 1, WARN mode exits 0, same as any other internal error.

THE TERRAFORM-TYPE MAP (TF_NODE: resource type -> (node type, own-name attribute)) is read from
org/standards/NAMING_SCHEMA.json's tf_type_map (C-S11, v1.9) at import; the limb keeps no map of its own.

Usage:
    python .tools/naming-gate.py --diff FILE [--enforce] [--post-from-index]

ENFORCE is on with --enforce, env NAMING_GATE_ENFORCE=1, or a present org/mcp/naming-gate.enforce: a REFUSE
then exits 1. Otherwise it is WARN mode and exits 0, on an internal error too (`NAMING ERROR <reason>`).
--post-from-index reads each file's post-image from the index (git show :<path>), as safe-commit.sh does;
without it the post-image is the pre-image with the diff's hunks applied.

Output: one `NAMING <verdict> <file>:<line> <string> -> <canonical>` line per graded string (<verdict> is the
grade, RAISE, REFUSE, or SKIP for a plan file), an indented `why:` line under each, then
`NAMING-GATE: <PASS|WARN|REFUSE> <n> graded`. Every verdict line is appended to
org/mcp/naming-gate-verdicts.log (runtime state; gitignored; never committed).

THE PLACEMENT STEP (LGIC_BLANKFIX FWD-6, round 8 BF-w-1; design FWD6_DESIGN_round6.md). For every NEW stored name in a
root, and for every root the diff touches, the commit limb asks lib/opal_naming_rootcheck.py place(), which is the root
check's own decision for the name, on the post-image of the diff:
    a name the canon places as FIX or HOLE in a MAPPED root         REFUSE, printing the name to use or what is owed and to whom
    a NEW wrong name in an UNMAPPED root                            grade()'s REFUSE stands; place()'s text replaces the bare blank
    a root whose HOLE count, post-image against HEAD (both run      REFUSE, printing the new HOLE lines and what each is owed
      now), is larger than at HEAD
    a name outside every root, RIGHT, NOT-ASKED, PATTERN, CARDED    grade() alone
The mode is the switch file org/mcp/naming-place.enforce (beside naming-gate.enforce; this build does not create it):
PRESENT -> the step refuses (rc=1, whatever naming-gate.enforce says, and a `NAMING-PLACE: REFUSE <n>` line is printed before the
summary: safe-commit.sh blocks on that line while the switch is present); ABSENT -> it prints the same lines, marks them
would-refuse and the verdict is unchanged. There is no date and no ramp, and no environment value turns the step off.
A root's files live under infra/aws/ (its .tf folder and its Lambda folders), so a commit with no .tf file and no NEW stored
name under infra/aws/ never loads the placement step; one that does costs about 13 s per root (at most 8 roots are placed).
If the step cannot run it prints NAMING PLACE ERROR and, with the switch present, refuses.

THE PLACEMENT OVERRIDE (LGIC_BLANKFIX FWD-6, round 9 BF-x-4, row W1-S21). While the switch is present a creator whose name the
canon cannot yet place needs a way through. The way is `# naming-place-override: <reason>` as a line of the commit message
(reason required, non-empty), read by .tools/safe-commit.sh ONLY. safe-commit is the ONLY setter of the variable
NAMING_PLACE_OVERRIDE: it first appends one JSON line to org/audit/naming-place-override-audit.jsonl, TRACKED, and stages it into
the SAME commit (round 10 BF-y-1: the landed commit carries its own audit row; the ignored .log of round 9 is no longer written)
(`{"utc","author","id","reason","names":[...],"msg_sha256":"<64 hex>"}`; round 10 BF-y-2: msg_sha256 is the sha256 of the exact
message text safe-commit.sh commits -- the -F file's bytes, or the -m texts joined by a blank line -- written to a temporary file),
then exports the line's `id` and runs this gate once more with `--message-file <that file>`. THE GATE REQUIRES THE AUDIT ROW AND
READS IT FROM THE INDEX (`git show :<path>`, the copy that will land), never from a file on disk only: a PLACE-REFUSE row is printed
as `NAMING OVERRIDDEN <file>:<line> <string> -> <form>` and does not block only when ALL of these hold: the variable names an id for
which the staged audit file holds a row with a non-empty reason; that row's msg_sha256 equals the sha256 of the message file the gate
is handed; that message carries a non-empty `# naming-place-override:` line; and the row's names list holds the row's string. The
600 s age window of round 9 is retired: a row is bound to ONE message, not to a clock, so a row written for another commit (or
pre-written) matches no later message. A variable set by hand, with no such staged row, passes nothing, and neither does a row with
the wrong hash, an empty hash, or a message without the line (`NAMING-PLACE-OVERRIDE: IGNORED <why>` is printed and the refusal
stands). The limit, stated: the file is the trust base -- a seat that can stage a row AND hash its own message can still forge one;
the row is the audit record bound to its commit, not a signature. safe-merge.sh and every other path write no such row, so they
have no override. The older limb's REFUSE is
not affected by the override.

Standard library only. ASCII only.
"""
from __future__ import annotations

import argparse
import ast
import datetime
import hashlib
import importlib.machinery
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOLS_DIR)
OPAL_PATH = os.path.join(REPO, "lib", "opal_naming.py")
SCHEMA_PATH = os.path.join(REPO, "org", "standards", "NAMING_SCHEMA.json")
ENFORCE_FILE = os.path.join(REPO, "org", "mcp", "naming-gate.enforce")
VERDICT_LOG = os.path.join(REPO, "org", "mcp", "naming-gate-verdicts.log")
PLACE_FILE = os.path.join(REPO, "org", "mcp", "naming-place.enforce")  # the placement step's switch: present = refuse
PLACE_PREVIEW = os.environ.get("NAMING_PLACE_PREVIEW") == "1"  # run the step while the switch is absent (its rows only WARN)
OVERRIDE_AUDIT_REL = "org/audit/naming-place-override-audit.jsonl"  # TRACKED; written and staged by safe-commit.sh only
OVERRIDE_LINE_RE = re.compile(r"^[ \t]*#?[ \t]*naming-place-override:[ \t]*(.*?)[ \t\r]*$", re.M)  # the message line, as safe-commit.sh reads it
PLACE_MAP = "infra/logic/registry/root_map.json"
PLACE_PATH_PREFIX = "infra/aws/"
PLACE_ROOT_CAP = 8  # roots placed per commit; each costs about two root-check runs (about 10 s)
REGISTRY_PREFIX = "infra/logic/registry/"
GRADED_EXT = (".py", ".js", ".mjs", ".ts", ".tf", ".json", ".yaml", ".yml")
# THE FIXTURE FOLDERS (CT-ab-9, ruled): a fixture under either spelling is not graded. Matched as WHOLE path segments
# against "/" + path, never as a substring: latest/, contest/ and test_data/ are NOT exempt.
FIXTURE_DIRS = ("/tests/", "/test/")


def _is_fixture(path):
    """True when `path` sits under a FIXTURE_DIRS folder, matched on whole segments ("/" + path)."""
    return any(d in "/" + path for d in FIXTURE_DIRS)
# THE GATE'S DOMAIN (R-11/R-13, round-3 EN-n-1): a resource is MINTED where the applied plane is
# DECLARED, never in a RECORD (proof instances, task orders, deliverables, surprise rows, logs, PRDs,
# project rows). The record trees are the WHOLE of org/** and docs/**; a record tree is never opened
# (no pre-image read, no generated-file check, no literal extraction), regardless of suffix.
RECORD_TREE_PREFIXES = ("org/", "docs/")
# R-35 (1.0.0_SA_CTO, 2026-09-17, on 2.0.0_SA_COO~G's CALL 1, row LGIC_LGCTFM-W2-S1): an ENGINE'S OWN
# MEASURED RUN OUTPUT is a RECORD, exactly like a proof instance under org/**, and R-13 simply did not
# enumerate the tree it lands in. Every prior LGCTFM round wrote only into org/**, so nothing exercised
# this until the first real run -- which the gate then refused wholesale (1719 REFUSE + 49 RAISE measured
# by 0.9.0_WK_LGIC_LGCTFM~2 and confirmed by its issuer at HEAD).
# THE EXEMPTION IS THE RUN DIRECTORY, NEVER THE TREE ABOVE IT. `workflows/legacy_transform/` also holds
# run_home.py -- ENGINE CODE, which mints names and MUST stay graded -- so a prefix exemption on the run
# home's parent would blind the gate to exactly the declarations it exists to grade. The discriminator is
# the run id's own shape, read from its producer (workflows/legacy_transform/run_home.py:7, :46: run_dir =
# <root>/<subject>/<run-id>, run-id = <UTC YYYYMMDDTHHMMSSZ>-<short repo head>), and it is self-limiting:
# nothing hand-authored lives in a directory named by a UTC stamp plus a commit pin, and run_home REFUSES
# a run directory that already exists (`:48`), so the name is minted once by the engine and never reused.
RUN_ARTIFACT_RE = re.compile(r"^workflows/[^/]+/[^/]+/[0-9]{8}T[0-9]{6}Z-[0-9a-f]{7,40}/")
BUILDERS = {"key", "address", "name", "lookup"}
# IRPT-M-LEGACY-READ-02 (1.0.0_SA_CTO @79f316834d, under Andrew's ecf350639a delegation; implementer
# 0.0.0_AB_MSTR per LD-0602/LD-0605). The carrier for the per-case LEGACY-READ waiver. It is consumed
# in EXACTLY ONE place -- judge()'s EXISTING-under-live-remediation branch -- and nowhere else.
LEGACY_READS_REL = "org/standards/NAMING_LEGACY_READS.json"
LEGACY_READS_FILE = os.path.join(REPO, *LEGACY_READS_REL.split("/"))
LEGACY_READ_FIELDS = ("id", "file", "literal", "remediation", "purpose", "authority",
                      "as_of_cutoff", "owner", "read_context")
SITE_FIELDS = ("helper", "helper_body_sha256", "arg_index", "enclosing_function", "bucket_arg", "occurrences")
# The second read_context kind (laptop 1.0.0_SA_CTO msg 102531, landed by 1.0.0_SA_CTO~O): a .tf file may carry an
# EXISTING out-of-pattern literal ONLY as the value of one `locals` entry, referenced exactly N times. A Python site
# keeps the kind-less SITE_FIELDS shape above; a .tf site MUST say kind tf_local.
TF_LOCAL_KIND = "tf_local"
TF_LOCAL_FIELDS = ("kind", "local_name", "occurrences", "reference_count")
TF_LOCAL_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_-]*$")
# The third read_context kind: an R20 DECLARED EXCEPTION (infra/logic/02_DOCTRINE.md R20; Andrew "yes thats fine on
# naming exception", 2026-09-30 ~13:0xZ at 1.0.0_SA_CTO~O, relayed 103235; landed by laptop 1.0.0_SA_CTO). The register
# entry (06_CONFORMANCE_LEDGER.md section 6 row, e.g. X11) is the departure's record; this entry lets the gate HONOUR it.
# It is the ONLY waiver kind that reaches a NEW literal, because a declared exception is exactly the case where a new
# read of a legacy key is the ruled behaviour. It still authorizes ONE literal in ONE file at a declared occurrence
# count, and it advances or closes no remediation. as_of_cutoff is a date or the word PERMANENT (R20 permanent/conditional).
R20_KIND = "r20_exception"
R20_FIELDS = ("kind", "register_ref", "occurrences")
R20_REGISTER_RE = re.compile(r"^[A-Z]{1,3}[0-9]{1,4}$")  # a conformance-ledger row id: X11, X12
R20_PERMANENT = "PERMANENT"
NAMING_MODULE_NAMES = {"opal_naming"}
# A call whose string argument is a numeric spelling, never a name: float("inf") is not the firm inf.
EXEMPT_CALLS = {"float"}
CLOSED_STATUSES = {"closed", "complete", "completed", "cancelled", "canceled", "superseded", "retired", "archived"}


def _load_tf_node():
    """Terraform resource type -> (node type, own-name attribute path). Read from NAMING_SCHEMA.json's
    tf_type_map (C-S11, v1.9): the schema is the one home for this data and the commit limb keeps no map
    of its own (round-2 EN-g-1). A schema that cannot be read or carries no tf_type_map yields an empty
    map: every literal then falls back to classify()'s generic reading, exactly as an unlisted Terraform
    type already does today."""
    try:
        with open(SCHEMA_PATH, "rb") as fh:
            schema = json.loads(fh.read().decode("utf-8"))
    except (OSError, ValueError):
        return {}
    raw = schema.get("tf_type_map")
    if not isinstance(raw, dict):
        return {}
    out = {}
    for tf_type, spec in raw.items():
        if isinstance(spec, dict) and isinstance(spec.get("node_type"), str) and spec["node_type"]:
            out[tf_type] = (spec["node_type"], spec.get("name_attribute"))
    return out


TF_NODE = _load_tf_node()

HUNK_RE = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")
DIFF_HEADERS = ("diff --git ", "index ", "new file mode", "deleted file mode", "old mode", "new mode",
                "similarity index", "dissimilarity index", "rename from", "rename to", "copy from", "copy to",
                "Binary files ", "Index: ", "====")
WORD_CHARS = "A-Za-z0-9_\\-"


class GateError(Exception):
    """The limb cannot run: printed as NAMING ERROR."""


# --------------------------------------------------------------------------- loading
def load_opal():
    if not os.path.isfile(OPAL_PATH):
        raise GateError("lib/opal_naming.py is absent at %s" % OPAL_PATH)
    loader = importlib.machinery.SourceFileLoader("opal_naming_gate", OPAL_PATH)
    spec = importlib.util.spec_from_loader("opal_naming_gate", loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


def git(*args):
    p = subprocess.run(["git"] + list(args), cwd=REPO, capture_output=True)
    return p.returncode, p.stdout, p.stderr


def text_of(raw):
    return raw.decode("utf-8", errors="replace").replace("\r\n", "\n")


# --------------------------------------------------------------------------- the diff
def _diff_path(s):
    s = s.split("\t")[0].rstrip()
    if s.startswith('"') and s.endswith('"') and len(s) >= 2:
        s = s[1:-1].encode("latin-1", errors="replace").decode("unicode_escape").encode("latin-1", errors="replace").decode("utf-8", errors="replace")
    if s == "/dev/null":
        return None
    if s.startswith(("a/", "b/")):
        s = s[2:]
    return s


def parse_diff(text):
    """[{old, new, hunks: [(old_start, old_count, new_start, new_count, body)]}]. Raises GateError on anything
    that is not a unified diff."""
    lines = text.replace("\r\n", "\n").split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    files, cur, i = [], None, 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("--- ") and i + 1 < len(lines) and lines[i + 1].startswith("+++ "):
            cur = {"old": _diff_path(ln[4:]), "new": _diff_path(lines[i + 1][4:]), "hunks": []}
            files.append(cur)
            i += 2
            continue
        m = HUNK_RE.match(ln)
        if m:
            if cur is None:
                raise GateError("not a unified diff: a hunk header at diff line %d comes before any ---/+++ header" % (i + 1))
            os_, oc = int(m.group(1)), int(m.group(2)) if m.group(2) is not None else 1
            ns, nc = int(m.group(3)), int(m.group(4)) if m.group(4) is not None else 1
            body, o, n, at = [], 0, 0, i + 1
            i += 1
            while (o < oc or n < nc) and i < len(lines):
                b = lines[i]
                tag = b[:1]
                if tag == "\\":
                    body.append(b)
                elif tag == " " or b == "":
                    o, n = o + 1, n + 1
                    body.append(b)
                elif tag == "-":
                    o += 1
                    body.append(b)
                elif tag == "+":
                    n += 1
                    body.append(b)
                else:
                    raise GateError("not a unified diff: line %d inside the hunk at diff line %d: %r" % (i + 1, at - 1, b[:60]))
                i += 1
            if o != oc or n != nc:
                raise GateError("not a unified diff: the hunk at diff line %d ends early (%d/%d old, %d/%d new)" % (at - 1, o, oc, n, nc))
            while i < len(lines) and lines[i].startswith("\\"):
                body.append(lines[i])
                i += 1
            cur["hunks"].append((os_, oc, ns, nc, body))
            continue
        if ln == "":
            i += 1
            continue
        if ln.startswith(DIFF_HEADERS):
            if ln.startswith("diff --git "):
                cur = None
            i += 1
            continue
        raise GateError("not a unified diff: diff line %d: %r" % (i + 1, ln[:60]))
    return files


def apply_hunks(pre_text, hunks):
    """(post-image lines, {post line number: text} for added lines)."""
    pre = pre_text.split("\n")
    if pre and pre[-1] == "":
        pre.pop()
    out, added, p = [], {}, 0
    for os_, oc, _ns, _nc, body in hunks:
        start = os_ if oc == 0 else os_ - 1
        start = max(p, min(start, len(pre)))
        out.extend(pre[p:start])
        p = start
        for b in body:
            if b.startswith("\\"):
                continue
            tag, txt = (b[:1], b[1:]) if b else (" ", "")
            if tag == " ":
                out.append(txt)
                p += 1
            elif tag == "-":
                p += 1
            else:
                out.append(txt)
                added[len(out)] = txt
    out.extend(pre[p:])
    return out, added


# --------------------------------------------------------------------------- string extraction
class Lit:
    __slots__ = ("value", "raw", "line", "hint", "permitted", "label", "block", "built", "live_held")

    def __init__(self, value, raw, line, hint=None):
        self.value, self.raw, self.line, self.hint = value, raw, line, hint
        self.permitted, self.label, self.block, self.built = False, False, None, False
        self.live_held = False  # set by the live limb (FWD-8): the census LIVE plane holds this exact name, so it is not a placement candidate


def _call_name(func):
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        return func.attr
    return None


def _naming_module_call(func):
    return isinstance(func, ast.Attribute) and isinstance(func.value, ast.Name) and func.value.id in NAMING_MODULE_NAMES


def py_literals(src, added):
    """String literals of a Python post-image whose lines meet the added set, outside every permitted context."""
    tree = ast.parse(src)
    out = []
    stack = [(tree, False)]
    while stack:
        node, skip = stack.pop()
        if isinstance(node, ast.Expr) and isinstance(node.value, (ast.Constant, ast.JoinedStr)):
            continue  # a docstring or a bare string statement: prose
        if isinstance(node, ast.Call):
            fn = _call_name(node.func)
            inner = skip or fn in BUILDERS or fn in EXEMPT_CALLS or _naming_module_call(node.func)
            stack.append((node.func, skip))
            stack.extend((a, inner) for a in node.args)
            stack.extend((k.value, inner) for k in node.keywords)
            continue
        if isinstance(node, ast.JoinedStr):
            if not skip and _meets(node, added):
                parts = []
                for v in node.values:
                    parts.append(v.value if isinstance(v, ast.Constant) and isinstance(v.value, str) else "{x}")
                seg = ast.get_source_segment(src, node) or ""
                out.append(Lit("".join(parts), seg, _first_added(node, added)))
            continue
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if not skip and _meets(node, added):
                out.append(Lit(node.value, node.value, _first_added(node, added)))
            continue
        stack.extend((c, skip) for c in ast.iter_child_nodes(node))
    return out


def _meets(node, added):
    lo = getattr(node, "lineno", 0)
    hi = getattr(node, "end_lineno", lo) or lo
    return any(lo <= n <= hi for n in added)


def _first_added(node, added):
    lo = getattr(node, "lineno", 0)
    hi = getattr(node, "end_lineno", lo) or lo
    return min((n for n in added if lo <= n <= hi), default=lo)


def _read_string(text, i, q, lang):
    """(value, raw, end index, newlines consumed, ok) for the string opening at text[i]."""
    n = len(text)
    j, out, nl = i + 1, [], 0
    multiline = q == "`"
    while j < n:
        ch = text[j]
        if ch == "\\" and j + 1 < n:
            nxt = text[j + 1]
            out.append(nxt if nxt in "\\\"'/`" else ch + nxt)
            j += 2
            continue
        if ch == "\n" and not multiline:
            return None, None, j, nl, False  # an unterminated single-line string: dropped, resume at the newline
        if ch == q:
            return "".join(out), text[i + 1:j], j + 1, nl, True
        if ch in "$%" and j + 1 < n and text[j + 1] == "{" and (lang == "tf" or (multiline and ch == "$")):
            depth, k = 0, j + 1
            while k < n:
                c2 = text[k]
                if c2 == "{":
                    depth += 1
                elif c2 == "}":
                    depth -= 1
                    if depth == 0:
                        break
                elif c2 == "\n":
                    nl += 1
                elif c2 in "\"'":
                    e = text.find(c2, k + 1)
                    k = e if e > 0 and "\n" not in text[k:e] else k
                k += 1
            out.append("{x}")
            j = k + 1
            continue
        if ch == "\n":
            nl += 1
        out.append(ch)
        j += 1
    return None, None, n, nl, False


def scan(text, lang):
    """Tokens (kind, value, raw, line) of a JS/TS or Terraform post-image: str, word, sym, nl. Comments dropped."""
    line_comments = ("#", "//") if lang == "tf" else ("//",)
    quotes = "\"" if lang == "tf" else "\"'`"
    toks, i, n, line = [], 0, len(text), 1
    while i < n:
        c = text[i]
        if c == "\n":
            toks.append(("nl", None, None, line))
            line += 1
            i += 1
            continue
        if text.startswith("/*", i):
            j = text.find("*/", i + 2)
            j = n if j < 0 else j + 2
            line += text.count("\n", i, j)
            i = j
            continue
        if text.startswith(line_comments, i):
            j = text.find("\n", i)
            i = n if j < 0 else j
            continue
        if c in quotes:
            val, raw, j, nl, ok = _read_string(text, i, c, lang)
            if ok:
                toks.append(("str", val, raw, line))
            line += nl
            i = j
            continue
        if c.isalnum() or c == "_":
            j = i
            while j < n and (text[j].isalnum() or text[j] in "_-"):
                j += 1
            toks.append(("word", text[i:j], None, line))
            i = j
            continue
        if c in "{}[]()=,:":
            toks.append(("sym", c, None, line))
        i += 1
    return toks


# --------------------------------------------------------------------------- built names (row LGIC_BLANKFIX-D1-W2-S9)
# A name built at a call site (an `opal_name` module block, a Python `name(...)` call) carries its arguments as permitted
# builder input, so the literals are skipped. Without a replacement the built name -- the string that is actually minted --
# was graded by nothing and the gate printed `PASS 0 graded` (ABSENT, not EXERCISED). These extractors read the ARGUMENTS
# of each such site; grade_built composes the name with lib/opal_naming.py name() and grades it like any other literal, or
# prints BUILT-NOT-GRADED with the reason. Result rows: (line, args dict or None, why or None).
BUILT_ARGS = ("system", "scope", "function", "kind", "qualifier", "fifo")
_NONLIT = object()


def py_built(src, added):
    """name(...) builder calls of a Python post-image that meet the added set: the bare name() (four or more arguments, the
    builder's shape) or opal_naming.name(). All-literal arguments give a dict for name(**args); otherwise None and why."""
    out = []
    for node in ast.walk(ast.parse(src)):
        if not isinstance(node, ast.Call) or not _meets(node, added):
            continue
        qualified = _naming_module_call(node.func) and node.func.attr == "name"
        bare = isinstance(node.func, ast.Name) and node.func.id == "name" and len(node.args) + len(node.keywords) >= 4
        if not (qualified or bare):
            continue
        line = _first_added(node, added)
        args, bad = {}, []
        if len(node.args) > len(BUILT_ARGS) or any(isinstance(a, ast.Starred) for a in node.args) \
                or any(k.arg is None for k in node.keywords):
            out.append((line, None, "name() call with *args/**kwargs or too many positional arguments"))
            continue
        pairs = list(zip(BUILT_ARGS, node.args)) + [(k.arg, k.value) for k in node.keywords]
        for key, val in pairs:
            if isinstance(val, ast.Constant) and (val.value is None or isinstance(val.value, (str, bool))):
                args[key] = val.value
            else:
                bad.append(key)
        if bad:
            out.append((line, None, "name() call with non-literal argument(s): %s" % ", ".join(bad)))
        else:
            out.append((line, args, None))
    return out


def tf_built(src, added):
    """`module "x" { source = ".../opal_name" ... }` blocks of a Terraform post-image that meet the added set. A block that
    passes none of system/function/kind is a registry-map reader and names nothing: skipped."""
    toks = scan(src, "tf")
    out, i, n = [], 0, len(toks)

    def is_sym(t, ch):
        return t[0] == "sym" and t[1] == ch

    while i < n:
        t = toks[i]
        if not (t[0] == "word" and t[1] == "module" and i + 2 < n and toks[i + 1][0] == "str" and is_sym(toks[i + 2], "{")):
            i += 1
            continue
        start, attrs, cur, depth, bracket, end = t[3], {}, [], 1, 0, t[3]
        i += 3

        def finish():
            if len(cur) >= 2 and cur[0][0] == "word" and is_sym(cur[1], "="):
                rest = cur[2:]
                if len(rest) == 1 and rest[0][0] == "str" and "${" not in rest[0][1] and "%{" not in rest[0][1]:
                    attrs[cur[0][1]] = rest[0][1]
                elif len(rest) == 1 and rest[0][0] == "word" and rest[0][1] in ("null", "true", "false"):
                    attrs[cur[0][1]] = {"null": None, "true": True, "false": False}[rest[0][1]]
                else:
                    attrs[cur[0][1]] = _NONLIT

        while i < n:
            t = toks[i]
            i += 1
            end = t[3]
            if t[0] == "nl":
                if depth == 1 and bracket == 0:
                    finish()
                    cur = []
                continue
            if t[0] == "sym":
                if t[1] == "{":
                    depth += 1
                elif t[1] == "}":
                    depth -= 1
                    if depth == 0:
                        finish()
                        break
                elif t[1] in "[(":
                    bracket += 1
                elif t[1] in "])":
                    bracket = max(0, bracket - 1)
            if depth >= 1:
                cur.append(t)
        src_val = attrs.get("source")
        if not (isinstance(src_val, str) and "opal_name" in src_val):
            continue
        hit = [ln for ln in added if start <= ln <= end]
        if not hit or not any(k in attrs for k in ("system", "function", "kind")):
            continue
        bad = [k for k in BUILT_ARGS if attrs.get(k) is _NONLIT]
        if bad:
            out.append((min(hit), None, "opal_name module block with non-literal argument(s): %s" % ", ".join(bad)))
        else:
            args = dict((k, attrs[k]) for k in BUILT_ARGS if k in attrs)
            args.setdefault("scope", None)  # the module's own default: null is a shared resource (S5)
            out.append((min(hit), args, None))
    return out


def js_literals(src, added):
    return [Lit(v, r, ln) for kind, v, r, ln in scan(src, "js") if kind == "str" and ln in added]


def tf_literals(src, added):
    """Terraform string literals on added lines, each with its block context: a label is marked, a string in a
    module block whose source is the opal_name module is permitted, and a resource's own-name attribute gives
    the node type as the hint.

    THE HCL LOOKUP CONTEXT (2026-09-23, 0.0.0_AB_MSTR, on 1.0.0_SA_CTO's 22:29Z routing of P's retained.tf):
    the Python side permits a literal inside a lookup() call (BUILDERS); this is its Terraform twin. A literal
    is permitted when it is the key of `lookup(local.X, "<key>")` or of `local.X["<key>"]` AND local.X is fed,
    in the same file, from jsondecode(file(".../logic/registry/<name>.json")) -- the canonical registry the
    Python lookup() reads. A local fed from a hand-typed map, or a lookup over anything else, stays graded:
    the same rule as the Python branch, no new permission class."""
    toks = scan(src, "tf")
    blocks, stmt, attr, bracket, out = [], [], None, 0, []
    registry_locals, ctxs = set(), []
    for kind, v, raw, ln in toks:
        if kind == "nl":
            if bracket == 0:
                stmt, attr = [], None
            continue
        if kind == "sym":
            if v == "{":
                has_eq = any(t[0] == "sym" and t[1] in "=:" for t in stmt)
                if stmt and stmt[0][0] == "word" and not has_eq:
                    labels = [t for t in stmt[1:] if t[0] == "lit"]
                    for t in labels:
                        t[1].label = True
                    blocks.append({"block": True, "kind": stmt[0][1], "labels": [t[1].value for t in labels], "opal": False})
                else:
                    blocks.append({"block": False, "map_attr": attr})
                stmt, attr, bracket = [], None, 0
                continue
            if v == "}":
                if blocks:
                    blocks.pop()
                stmt, attr, bracket = [], None, 0
                continue
            if v in "[(":
                bracket += 1
            elif v in "])":
                bracket = max(0, bracket - 1)
            elif v in "=:" and stmt and bracket == 0:
                last = stmt[-1]
                if last[0] == "word":
                    attr = last[1]
                elif last[0] == "lit":
                    attr = last[1].value
            stmt.append(("sym", v))
            continue
        if kind == "word":
            stmt.append(("word", v))
            continue
        lit = Lit(v, raw, ln)
        lit.block = list(blocks)
        ctxs.append((lit, [(k, x if k != "lit" else None) for k, x in stmt[-5:]]))
        stmt.append(("lit", lit))
        inner = blocks[-1] if blocks else None
        if inner and inner.get("block") and inner.get("kind") == "module" and attr == "source" and "opal_name" in v:
            inner["opal"] = True
        if _TF_REGISTRY_FILE.search(v) and any(b.get("block") and b.get("kind") == "locals" for b in blocks):
            local_name = inner.get("map_attr") if inner and not inner.get("block") else attr
            if local_name:
                registry_locals.add(local_name)
        lit.hint = _tf_hint(blocks, attr)
        if ln in added:
            out.append(lit)
    for lit in out:
        if any(b.get("block") and b.get("kind") == "module" and b.get("opal") for b in lit.block):
            lit.permitted = True
    for lit, ctx in ctxs:
        if lit.permitted or lit not in out:
            continue
        if (len(ctx) >= 5 and ctx[-5:-1] == [("word", "lookup"), ("sym", "("), ("word", "local"), ("word", ctx[-2][1])]
                and ctx[-1] == ("sym", ",") and ctx[-2][1] in registry_locals):
            lit.permitted = True  # lookup(local.X, "<key>") over a registry-fed local
        elif len(ctx) >= 3 and ctx[-3] == ("word", "local") and ctx[-1] == ("sym", "[") and ctx[-2][1] in registry_locals:
            lit.permitted = True  # local.X["<key>"] over a registry-fed local
    return [lit for lit in out if not lit.label]


_TF_REGISTRY_FILE = re.compile(r"(^|/)logic/registry/[A-Za-z0-9_.-]+\.json$")


def _tf_hint(blocks, attr):
    for k in range(len(blocks) - 1, -1, -1):
        b = blocks[k]
        if b.get("block"):
            if b.get("kind") != "resource" or not b.get("labels"):
                return None
            spec = TF_NODE.get(b["labels"][0])
            path = ".".join([m.get("map_attr") or "" for m in blocks[k + 1:]] + [attr or ""])
            return spec[0] if spec and path == spec[1] else None
    return None


_JSON_STR = re.compile(r'"((?:[^"\\]|\\.)*)"')
_YAML_QUOTED = re.compile(r'"((?:[^"\\]|\\.)*)"|\'((?:[^\']|\'\')*)\'')
PLAN_KEYS = ("format_version", "terraform_version")


def is_plan_artifact(post_text):
    """True when a JSON post-image is a `terraform show -json` artifact: its top level carries
    format_version and terraform_version, with resource_changes or planned_values (round-2 EN-g-1,
    row W1-S22: a machine-written plan file is not graded at commit -- an authored JSON file carrying
    the same string is graded exactly as today)."""
    try:
        obj = json.loads(post_text)
    except ValueError:
        return False
    if not isinstance(obj, dict) or any(k not in obj for k in PLAN_KEYS):
        return False
    return "resource_changes" in obj or "planned_values" in obj


def json_literals(added):
    out = []
    for ln, txt in sorted(added.items()):
        for m in _JSON_STR.finditer(txt):
            try:
                val = json.loads('"%s"' % m.group(1))
            except ValueError:
                val = m.group(1)
            out.append(Lit(val, m.group(1), ln))
    return out


def yaml_literals(added):
    out = []
    for ln, txt in sorted(added.items()):
        body = _strip_yaml_comment(txt)
        quoted = list(_YAML_QUOTED.finditer(body))
        if quoted:
            for m in quoted:
                val = m.group(1) if m.group(1) is not None else m.group(2).replace("''", "'")
                out.append(Lit(val, val, ln))
            continue
        m = re.match(r"^\s*(?:-\s+)?(?:[^:#]+:\s+)?(\S.*?)\s*$", body)
        if m and not body.rstrip().endswith(":"):
            out.append(Lit(m.group(1), m.group(1), ln))
    return out


def _strip_yaml_comment(s):
    q = None
    for i, c in enumerate(s):
        if q:
            if c == q:
                q = None
        elif c in "\"'":
            q = c
        elif c == "#" and (i == 0 or s[i - 1] in " \t"):
            return s[:i]
    return s


# --------------------------------------------------------------------------- the grade side
class Naming:
    """What the matrix reads from lib/opal_naming.py and the registry."""

    def __init__(self, mod):
        self.mod = mod
        self.v = mod._vocab()
        reg = mod._registry()
        self.reg = reg
        self.mark_re = re.compile(re.escape(mod.MARK) + r"[0-9a-f]{16}")
        self.targets = [x[0] for x in mod.VIEWS] + [mod.LOCALS_PATH, mod.VECTORS_PATH]
        self.firm_seg, self.firm_whole, self.product_whole = {}, {}, {}
        systems = {s.get("key") for s in reg["systems"].get("systems", [])}
        for row in reg["scopes"].get("scopes", []):
            cls = row.get("class")
            if cls not in ("FIRM", "PRODUCT"):
                continue
            for sp in mod._spellings(row):
                if cls == "FIRM":
                    if sp in systems:
                        continue
                    self.firm_whole[sp] = row["long"]
                    if re.match(r"^[A-Za-z0-9]+$", sp):
                        self.firm_seg[sp] = row["long"]
                else:
                    self.product_whole[sp] = row["long"]
        # v3 already carries the refused token (lib/opal_naming.py _Vocab), so only the reserved system is added
        self.first_vocab = self.v.v1 | self.v.v2 | self.v.v3 | {"opal"}
        self.acct_bucket = re.compile(r"^opal-%s-" % re.escape(self.v.account))
        self._surfaces = None

    # -- classification: the node type a literal is graded as, or None
    def classify(self, s, hint=None):
        if hint:
            return hint, s
        if not s or len(s) < 2 or not s.isascii() or re.search(r"\s", s):
            return None, s
        v = self.v
        if s.startswith("s3://"):
            rest = s[5:]
            if "/" in rest.rstrip("/"):
                return "S3Key", rest
            return ("S3_BUCKET", rest.rstrip("/")) if rest.strip("/") else (None, s)
        if s.startswith("arn:") or "://" in s:
            return None, s
        if "/" in s:
            if s.startswith("/aws/"):
                # a bare prefix such as /aws/ or /aws/lambda/ names no resource: not a log group
                return ("LOG_GROUP", s) if len([x for x in s.split("/") if x]) >= 3 else (None, s)
            segs = s.split("/")
            first = segs[0]
            real = [x for x in segs if x]
            if not first or len(real) < 1:
                return None, s
            if first in v.buckets or first.startswith("opal-data-") or self.acct_bucket.match(first):
                return "S3Key", s
            if (first in v.tiers or first == "code") and len(real) >= 2:
                return "S3Key", s
            if first in v.v1:
                if any(x in v.tiers for x in segs[1:4]) or s.endswith("/"):
                    return "S3Key", s
                if 2 <= len(real) <= 3 and "." not in real[-1]:
                    return "SECRET", s
            return None, s
        if s in v.buckets or self.acct_bucket.match(s) or (s.startswith("opal-data-") and len(s) > len("opal-data-")):
            return "S3_BUCKET", s
        # an all-capitals string (a node-type constant such as LAMBDA_LAYER) is never an AWS resource name
        if re.match(r"^[A-Za-z0-9]+([-_.][A-Za-z0-9]+)+$", s) and not s.isupper():
            body = s[:-5] if s.endswith(".fifo") else s
            toks = re.split(r"[-_.]", body.lower())
            if toks[0] in self.first_vocab:
                owners = [t for t, ks in v.kinds_by_type.items() if toks[-1] in ks]
                if len(owners) == 1:
                    return owners[0], s
        return None, s

    # -- the context rule: the firm or product token a hand-kept literal carries, or None
    def carrier(self, s):
        if not s or re.search(r"\s", s):
            return None
        if s in self.firm_whole:
            return s, self.firm_whole[s]
        if s in self.product_whole:
            return s, self.product_whole[s]
        for seg in re.split(r"[-_/.:=@]+", s):
            if seg in self.firm_seg:
                return seg, self.firm_seg[seg]
        return None

    # -- remediations.json: is this S3 literal inside a live remediation's surface
    def surfaces(self):
        if self._surfaces is None:
            out = []
            for r in self.reg["remediations"].get("remediations", []):
                live, basis = self._live(r)
                if live:
                    out += [(r.get("project"), sf, basis) for sf in r.get("surfaces", [])]
            self._surfaces = out
        return self._surfaces

    def _live(self, r):
        m = re.search(r"(org/missions/\S+?/project\.json)", str(r.get("register", "")))
        if not m:
            return True, "no register path: read as live"
        try:
            with open(os.path.join(REPO, *m.group(1).split("/")), "rb") as fh:
                status = str(json.loads(text_of(fh.read())).get("status", "")).lower()
        except (OSError, ValueError) as exc:
            return True, "register unreadable (%s): read as live" % type(exc).__name__
        return status not in CLOSED_STATUSES, "%s status %s" % (m.group(1), status or "absent")

    def remediation_of(self, typ, s):
        if typ not in ("S3Key", "S3_BUCKET", "S3_BUCKET_POLICY"):
            return None
        bucket, key = None, ""
        if typ in ("S3_BUCKET", "S3_BUCKET_POLICY"):
            bucket = s
        else:
            first, _, rest = s.partition("/")
            if first in self.v.buckets or first.startswith("opal-data-"):
                bucket, key = first, rest
            else:
                key = s
        for project, sf, _basis in self.surfaces():
            if sf.get("kind") == "bucket-alias" and bucket and bucket == sf.get("alias"):
                return project
            if sf.get("kind") == "s3-prefix" and (bucket is None or bucket == sf.get("bucket")):
                pre = sf.get("prefix", "")
                if pre and (key.startswith(pre) or (key + "/").startswith(pre)):
                    return project
        return None

    def grade(self, typ, s):
        try:
            verdict, canon = self.mod.grade(s, typ)
            return verdict, canon, None
        except self.mod.RaiseDefect as exc:
            return "RAISE", None, str(exc)


# --------------------------------------------------------------------------- generated files
def generated_ranges(lines, nm):
    """[(lo, hi)] 1-based line ranges inside BEGIN/END generated blocks; [(1, len)] for a whole generated file."""
    ranges, begin = [], None
    ends = [i for i, ln in enumerate(lines) if "END GENERATED [" in ln]
    marks = [i for i, ln in enumerate(lines) if nm.mark_re.search(ln)]
    if marks and not ends:
        return [(1, len(lines))]
    for i, ln in enumerate(lines):
        if begin is None and nm.mark_re.search(ln):
            begin = i
        elif begin is not None and "END GENERATED [" in ln:
            ranges.append((begin + 1, i + 1))
            begin = None
    return ranges


def _nested_portal_path(path):
    """A commit made inside the nested portal repo (safe-commit runs `git diff --cached` from its cwd) names its
    files portal-relative, while generator targets are workspace-relative (`portal/src/...`). Only then is the
    `portal/` prefix restored; any other cwd returns the path unchanged."""
    portal = os.path.normcase(os.path.join(REPO, "portal"))
    cwd = os.path.normcase(os.path.abspath(os.getcwd()))
    if cwd == portal or cwd.startswith(portal + os.sep):
        return "portal/" + path
    return path


def _diff_repo():
    """The repo the diff's paths are relative to: the nested portal repo when the commit runs inside it (see
    _nested_portal_path), else the workspace. HEAD:/index reads of a diff path must run there, or a modified
    portal file reads no pre-image and its post-image is rebuilt from hunks alone (a partial file)."""
    portal = os.path.join(REPO, "portal")
    cwd = os.path.normcase(os.path.abspath(os.getcwd()))
    if cwd == os.path.normcase(portal) or cwd.startswith(os.path.normcase(portal) + os.sep):
        return portal
    return REPO


def git_in(repo, *args):
    p = subprocess.run(["git"] + list(args), cwd=repo, capture_output=True)
    return p.returncode, p.stdout, p.stderr


def generator_output(nm, path, post_text):
    """The generator's output for a generated target whose post-image is post_text (the carrier's hand-kept
    bytes are read from the post-image, as generate() reads them from the working tree)."""
    mod = nm.mod
    target = os.path.normcase(os.path.abspath(os.path.join(mod.REPO, *path.split("/"))))
    real_read = mod._read_text

    def read_post(p):
        if os.path.normcase(os.path.abspath(p)) == target:
            return post_text
        return real_read(p)

    tmp = tempfile.mkdtemp(prefix="naming-gate-")
    mod._read_text = read_post
    try:
        mod.generate(tmp, [path])
        with open(os.path.join(tmp, *path.split("/")), "rb") as fh:
            return text_of(fh.read())
    finally:
        mod._read_text = real_read
        shutil.rmtree(tmp, ignore_errors=True)


# --------------------------------------------------------------------------- the domain (R-11/R-13)
def _is_record_tree(path):
    return path.startswith(RECORD_TREE_PREFIXES) or _is_run_artifact(path)


def _is_run_artifact(path):
    """An engine's own measured output inside a minted run directory (R-35). See RUN_ARTIFACT_RE."""
    return RUN_ARTIFACT_RE.match(path) is not None


def _is_gitattributes(path):
    return path == ".gitattributes" or path.endswith("/.gitattributes")


_RESOLVE_CACHE = {}


def _resolves_to_tracked(value):
    """A path-shaped value is a CITATION, not a mint, when it resolves to a tracked file at HEAD (R-11).
    A path-shaped value that does NOT resolve (a typo, an invented file) is still graded and still refuses."""
    if value in _RESOLVE_CACHE:
        return _RESOLVE_CACHE[value]
    ok = False
    if (value and "/" in value and not value.startswith("/") and "://" not in value
            and not value.startswith("arn:") and ".." not in value.split("/")):
        rc, _out, _err = git("cat-file", "-e", "HEAD:%s" % value)
        ok = rc == 0
    _RESOLVE_CACHE[value] = ok
    return ok


_CARRIED_CACHE = {}


def _carried_at_head(value, path):
    """The first DECLARATION-TREE file at HEAD, other than `path`, that carries `value` byte for byte (fixed
    string); '' when none. One git grep per distinct value, cached for the run.

    Declaration tree only (LD-0611-ARM-01, 1.0.0_SA_CTO 99852): a hit under a record tree (org/**, docs/**, a
    minted run directory) or in a file the gate does not grade is NOT a carrier. A key first typed into a
    ledger, a message record or a log must not make its later copy in code read EXISTING -- and the ledger
    naming this rule's own negative arm made that arm vacuous one commit after it was measured."""
    if not value or len(value) < 4:
        return ""
    if value not in _CARRIED_CACHE:
        rc, out, _err = git("grep", "-l", "-F", "--", value, "HEAD")
        hits = []
        if rc == 0:
            for line in text_of(out).splitlines():
                hit = line.split(":", 1)[1] if line.startswith("HEAD:") else line
                if (hit and hit != path and not _is_record_tree(hit) and hit.endswith(GRADED_EXT)
                        and hit != ".tools/naming-gate.py" and not _is_fixture(hit)):
                    hits.append(hit)  # never the gate's own bytes or a fixture under a FIXTURE_DIRS folder
        _CARRIED_CACHE[value] = sorted(hits)
    hits = [h for h in _CARRIED_CACHE[value] if h != path]
    return hits[0] if hits else ""


def _packaged_citations(post_text):
    """The `packaged_as` names of a packaging manifest whose `repo_path` resolves to a tracked file at HEAD
    (2026-09-23, 0.0.0_AB_MSTR, on 2.0.0_SA_COO~P 99805: lambda-source-map.json rows such as
    {"repo_path": ".../performance/bd_live.py", "packaged_as": "bd_live.py"} and the member lists that
    repeat those names). The packaged name is the in-zip spelling of a file already committed under its
    repo_path, so it is the same citation R-11 already recognises for the repo_path itself -- renaming it
    would break the module's imports and mints nothing. A row whose repo_path does NOT resolve cites nothing,
    and its packaged_as stays graded. Any other JSON string is unaffected."""
    try:
        doc = json.loads(post_text)
    except ValueError:
        return set()
    out, stack = set(), [doc]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            rp, pk = node.get("repo_path"), node.get("packaged_as")
            if isinstance(rp, str) and isinstance(pk, str) and _resolves_to_tracked(rp):
                out.add(pk)
            stack.extend(node.values())
        elif isinstance(node, list):
            stack.extend(node)
    return out


SOURCE_MAP_PATH = "infra/aws/lambda/ci/lambda-source-map.json"
_SOURCE_MAP_NAME_FIELDS = ("function_name", "iam_role")


def _source_map_name_position(line_text, value):
    """True iff `value` sits in a RESOURCE-NAME position on this source-map line: a row key (`"<value>": {`) or the value of
    `function_name`, `iam_role` or a key ending `_name` / `_role`. A free-text field (`_build_note`, notes) is never one."""
    q = re.escape(json.dumps(value))
    if re.match(r'^\s*%s\s*:\s*\{' % q, line_text):
        return True
    m = re.match(r'^\s*"([^"]+)"\s*:\s*%s\s*,?\s*$' % q, line_text)
    if not m:
        return False
    key = m.group(1)
    return key in _SOURCE_MAP_NAME_FIELDS or key.endswith("_name") or key.endswith("_role")


def _builder_reproduces(mod, value):
    """True iff lib/opal_naming.py name() reproduces `value` byte for byte from registry rows: {system}-{scope}-{function}
    [-{qualifier}]-{kind}, with the scope read through lookup() (or no scope, a shared resource). Any refusal by the builder is
    a miss, never an error, so a literal the builder cannot reproduce stays graded."""
    toks = value.split("-")
    if len(toks) < 3:
        return False
    system, kind = toks[0], toks[-1]

    def _firm(tok):
        try:
            return (mod.lookup(tok) or {}).get("class") == "FIRM"
        except Exception:  # noqa: BLE001
            return False

    try:
        row = mod.lookup(toks[1])
    except Exception:  # noqa: BLE001
        row = None
    if row is not None:
        # the second token IS a scope: only the scoped reading counts, so a firm token cannot ride in as a function name
        if len(toks) < 4:
            return False
        candidates = [(row.get("long") or toks[1], toks[2:-1])]
    elif any(_firm(t) for t in toks[1:-1]):
        return False  # an unscoped reading that carries a firm token is a mint, never a citation
    else:
        candidates = [(None, toks[1:-1])]
    for scope, mid in candidates:
        for k in range(len(mid), 0, -1):
            fn, qual = "-".join(mid[:k]), ("-".join(mid[k:]) or None)
            try:
                if mod.name(system, scope, fn, kind, qual) == value:
                    return True
            except Exception:  # noqa: BLE001
                continue
    return False


def _tf_block_source(tf_text, module_name):
    """The `source` string of `module "<module_name>"` in tf_text, or None (no such block, or no source in it)."""
    m = re.search(r'^\s*module\s+"%s"\s*\{' % re.escape(module_name), tf_text, re.M)
    if not m:
        return None
    depth, i = 1, m.end()
    while i < len(tf_text) and depth:
        depth += {"{": 1, "}": -1}.get(tf_text[i], 0)
        i += 1
    s = re.search(r'^\s*source\s*=\s*"([^"]+)"', tf_text[m.end():i], re.M)
    return s.group(1) if s else None


def _tf_address_cited(tf_file, address):
    """3.0.0_SA_CVO follow-on ruling (msg 104877): a source-map `tf_resource` CITES `module.<m>.<type>.<name>` iff (a) tf_file declares
    `module "<m>"` at HEAD and (b) that module's local `source` declares `resource "<type>" "<name>"` at HEAD. A nested, indexed or
    remote-source address, or any git read that fails, is a miss, so the literal stays graded."""
    parts = address.split(".")
    if len(parts) != 4 or parts[0] != "module" or not tf_file or any(c in address for c in '["]'):
        return False
    _m, mname, rtype, rname = parts
    rc, out, _err = git("show", "HEAD:%s" % tf_file)
    if rc != 0:
        return False
    src = _tf_block_source(text_of(out), mname)
    if not src or not src.startswith(("./", "../")):
        return False
    mdir = os.path.normpath(os.path.join(os.path.dirname(tf_file), src)).replace("\\", "/")
    rc, out, _err = git("ls-tree", "--name-only", "HEAD", mdir + "/")
    if rc != 0:
        return False
    pat = re.compile(r'^\s*resource\s+"%s"\s+"%s"\s*\{' % (re.escape(rtype), re.escape(rname)), re.M)
    for f in text_of(out).splitlines():
        if f.endswith(".tf"):
            rc2, body, _e = git("show", "HEAD:%s" % f)
            if rc2 == 0 and pat.search(text_of(body)):
                return True
    return False


def _row_tf_file(post_text, line_no):
    """The `tf_file` of the source-map row that holds line `line_no` (1-based): the nearest row key above it, read from the parsed
    document's `functions` map. None when the row cannot be placed."""
    lines = post_text.split("\n")
    for i in range(min(line_no, len(lines)) - 1, -1, -1):
        m = re.match(r'^ {4}"([^"]+)"\s*:\s*\{', lines[i])
        if m:
            try:
                row = json.loads(post_text).get("functions", {}).get(m.group(1), {})
            except (ValueError, AttributeError):
                return None
            tf = row.get("tf_file") if isinstance(row, dict) else None
            return tf if isinstance(tf, str) else None
    return None


_CHANGELOG_RE = re.compile(r"^infra/aws/terraform/[^/]+/CHANGELOG\.json$")
_CHANGELOG_ARRAYS = ("functions_updated", "functions_with_source_changes")


def _changelog_name_position(post_lines, line_no, value):
    """True iff `value` on line `line_no` (1-based) is an element of `functions_updated[]` or `functions_with_source_changes[]`, or
    the value of a `function` key. Any other position (commits[].message and all free text) is not one."""
    if not (1 <= line_no <= len(post_lines)):
        return False
    q = re.escape(json.dumps(value))
    line = post_lines[line_no - 1]
    if re.match(r'^\s*"function"\s*:\s*%s\s*,?\s*$' % q, line):
        return True
    if not re.match(r'^\s*%s\s*,?\s*$' % q, line):
        return False
    for i in range(line_no - 2, -1, -1):
        prev = post_lines[i]
        m = re.match(r'^\s*"([^"]+)"\s*:\s*\[\s*$', prev)
        if m:
            return m.group(1) in _CHANGELOG_ARRAYS
        if re.match(r'^\s*"[^"]*"\s*,?\s*$', prev):
            continue  # another bare element of the same array
        return False
    return False


_SOURCE_MAP_FUNCS = []


def _source_map_functions():
    """The `functions` keys of lambda-source-map.json at HEAD (the deployed functions it already records); empty when unreadable,
    so nothing extra passes. 1.0.0_SA_CTO ruling on 0.0.0_AB_MSTR msg 107746 (4.0.0_SA_CRO's proposal,
    AMGT_RESAPP_D1S6_ANSWER_20261009.md): a changelog that names such a function cites it and mints nothing."""
    if not _SOURCE_MAP_FUNCS:
        names = set()
        try:
            p = subprocess.run(["git", "show", "HEAD:" + SOURCE_MAP_PATH], cwd=REPO, capture_output=True)
            if p.returncode == 0:
                names = set((json.loads(p.stdout.decode("utf-8")).get("functions") or {}).keys())
        except Exception:  # noqa: BLE001 -- unreadable = no extra citations
            names = set()
        _SOURCE_MAP_FUNCS.append(names)
    return _SOURCE_MAP_FUNCS[0]


def _changelog_name_citations(mod, path, lits, post_text):
    """3.0.0_SA_CVO ruling (msg 104898, appended to CVO_RULING_NAMING_LIMB_SOURCE_MAP_CITATION_NOT_MINT_20261004.md, on 2.0.0_SA_COO~P
    104894 / row W115-S1): in infra/aws/terraform/*/CHANGELOG.json (record-terraform-deploy.sh's generated record), a literal in
    `functions_updated[]`, `functions_with_source_changes[]` or a `function` key passes iff name() reproduces it. commits[].message
    and other free text stay graded. COST: a few builder calls per added changelog literal. NON-APPLICATION: every other file."""
    if not _CHANGELOG_RE.match(path or ""):
        return
    post_lines = (post_text or "").split("\n")
    root_folder = path.split("/")[3]
    for lit in lits:
        if lit.permitted:
            continue
        if _changelog_name_position(post_lines, lit.line, lit.value) \
                and (_builder_reproduces(mod, lit.value) or lit.value in _source_map_functions()):
            lit.permitted = True  # the builder's name, or (1.0.0_SA_CTO, msg 107746) a function the source map already holds
        elif lit.value == root_folder and 1 <= lit.line <= len(post_lines) and re.match(
                r'^\s*"_pipeline"\s*:\s*%s\s*,?\s*$' % re.escape(json.dumps(lit.value)), post_lines[lit.line - 1]):
            lit.permitted = True  # (1.0.0_SA_CTO, msg 107746) `_pipeline` naming the changelog's own root folder cites it


def _source_map_name_citations(mod, path, added, lits, post_text=""):
    """3.0.0_SA_CVO ruling @7b38f056ca (CVO_RULING_NAMING_LIMB_SOURCE_MAP_CITATION_NOT_MINT_20261004.md, on 2.0.0_SA_COO~P 104859 /
    row W114-S1): in lambda-source-map.json ONLY, a literal in a resource-name position passes iff name() reproduces it byte for
    byte. Such a string CITES a resource Terraform minted through the builder; it mints nothing (Rule 30's existing-pipeline
    non-application). Free-text fields get no carve-out, and a literal the builder does not reproduce stays refused. COST: a few
    builder calls per added source-map literal. NON-APPLICATION: every other file."""
    if path != SOURCE_MAP_PATH:
        return
    for lit in lits:
        if lit.permitted:
            continue
        line_text = added.get(lit.line, "")
        if _source_map_name_position(line_text, lit.value) and _builder_reproduces(mod, lit.value):
            lit.permitted = True
        elif re.match(r'^\s*"tf_resource"\s*:\s*%s\s*,?\s*$' % re.escape(json.dumps(lit.value)), line_text) \
                and _tf_address_cited(_row_tf_file(post_text, lit.line), lit.value):
            lit.permitted = True  # the follow-on ruling: a tf_resource whose module and resource are declared at HEAD


_GITATTR_BINARY_TOKENS = ("binary", "-diff")


def _judge_gitattributes_line(path, ln, txt):
    """A5-A6: a `binary` or `-diff` attribute on a declaration-tree path needs a same-line reason
    comment (text after `#` on the same line) or the gate refuses it. A target inside a RECORD tree is
    never graded here (measured at the cut: all 3 existing binary lines sit in record trees)."""
    left, _sep, tail = txt.partition("#")
    reason = tail.strip()
    tokens = left.split()
    if not tokens:
        return None
    pattern, attrs = tokens[0], tokens[1:]
    if not any(a in _GITATTR_BINARY_TOKENS for a in attrs):
        return None
    if _is_record_tree(pattern.lstrip("/")):
        return None
    if reason:
        return ("PASS", path, ln, txt.strip(), "-",
                "binary/-diff attribute on a declaration-tree path carries a same-line reason: %r" % reason, "PASS")
    return ("REFUSE", path, ln, txt.strip(), "<same-line reason comment, e.g. '# why'>",
            "a binary/-diff attribute on a declaration-tree path with no same-line reason comment (A-6)", "REFUSE")


def _grade_gitattributes(f):
    path = f["new"]
    pre_text = None
    if f["old"] is not None:
        rc, out, _err = git("show", "HEAD:%s" % f["old"])
        if rc == 0:
            pre_text = text_of(out)
        elif os.path.isfile(os.path.join(REPO, *f["old"].split("/"))):
            with open(os.path.join(REPO, *f["old"].split("/")), "rb") as fh:
                pre_text = text_of(fh.read())
    _post_lines, added = apply_hunks(pre_text or "", f["hunks"])
    rows = []
    for ln, txt in sorted(added.items()):
        row = _judge_gitattributes_line(path, ln, txt)
        if row:
            rows.append(row)
    return rows


def domain_meta(files):
    """DENOMINATOR (Rule 24(i) subtraction: domain = total MINUS EXCLUDED record trees) and COVERAGE
    (S42: the paths in that domain the gate cannot see, by extension) for the whole run.

    The EXCLUSION SET IS PRINTED, never implied (R-35): the subtraction names every limb it subtracts on
    and counts each separately, so a tree added to the exemption later cannot land on the wrong side of
    this line unnoticed -- the counts disagree before the reader does."""
    total, record, run_record, seen = 0, 0, 0, 0
    for f in files:
        path = f["new"] if f["new"] is not None else f["old"]
        if path is None:
            continue
        total += 1
        if _is_record_tree(path):
            record += 1
            if _is_run_artifact(path):
                run_record += 1
            continue
        if path.endswith(GRADED_EXT) or _is_gitattributes(path):
            seen += 1
    domain = total - record
    unseen = domain - seen
    excluded_spec = "%s, run-artifact dirs %s" % (", ".join(RECORD_TREE_PREFIXES), RUN_ARTIFACT_RE.pattern)
    return [
        "DENOMINATOR: %d path(s) in this diff; declaration-tree domain = %d MINUS EXCLUDED(%s) %d = %d path(s)"
        " [of the excluded, %d are run artifacts and %d are org//docs/]"
        % (total, total, excluded_spec, record, domain, run_record, record - run_record),
        "COVERAGE: %d path(s) in the declaration domain the gate could not see (extension outside its graded"
        " set and not .gitattributes); %d seen" % (unseen, seen),
    ]


# --------------------------------------------------------------------------- the LEGACY-READ waiver
# IRPT-M-LEGACY-READ-02's N2 refinement, verbatim: "a write-verb denylist is insufficient. Positively
# recognize the exact authorized read use and its relevant call/helper context; unknown, indirect or
# ambiguous use remains REFUSE."
#
# SO THIS RECOGNIZER IS AN ALLOWLIST OF SYNTAX, NOT A DENYLIST OF VERBS. It authorizes a literal only
# when EVERY occurrence of that exact string in the post-image is a DIRECT argument of a call to a
# NAMED helper the carrier declares, AND each declared helper's body still hashes to the bytes the
# carrier was approved against. Anything else -- an assignment to a variable, an f-string, a method
# call, a helper reached through an alias, one extra occurrence anywhere in the file -- leaves the
# REFUSE standing.
#
# WHAT IT DOES NOT CLAIM, stated because the ruling explicitly declines to require it: this is not
# Python dataflow analysis and proves nothing about what a helper does at runtime. It proves that the
# literal reaches only the helpers named at approval time and that those helpers' SOURCE HAS NOT
# CHANGED. A helper edited to write fails the hash and the waiver disappears -- which is the property
# the ruling asks for ("a changed read helper that now writes"), obtained without dataflow.
def _norm_body(src):
    return "\n".join(ln.rstrip() for ln in src.replace("\r\n", "\n").split("\n")).strip()


FULL_PIN_RE = re.compile(r"^[0-9a-f]{40}$")


def _binds_of(node, name):
    """EVERY binding of `name` under `node`, by ANY construct -- [(kind, ast node)].

    NOTE: COUNTING ast.Assign IS NOT COUNTING BINDINGS, and 1.0.0_SA_CTO's review of candidate ec40acbf
    broke the first version of this recognizer on exactly that gap: a `for bucket in ...` rebinds the
    name without ever producing an Assign, so a simple-assignment census reads "bound once" on a
    name the loop reassigns on every iteration. The same hole admits a walrus, a with-as, an
    except-as, a comprehension target, an import alias, a parameter and a del.
    NOTE: So this enumerates the binding FORMS Python has, and anything it does not recognise is not
    silently permitted -- the callers require an exact count and refuse otherwise.
    """
    out = []
    for n in ast.walk(node):
        if isinstance(n, ast.Assign):
            for t in n.targets:
                out += [("assign", n) for x in ast.walk(t)
                        if isinstance(x, ast.Name) and x.id == name and isinstance(x.ctx, ast.Store)]
        elif isinstance(n, (ast.AnnAssign, ast.AugAssign)):
            t = n.target
            if isinstance(t, ast.Name) and t.id == name:
                out.append(("annassign" if isinstance(n, ast.AnnAssign) else "augassign", n))
        elif isinstance(n, ast.NamedExpr):
            if isinstance(n.target, ast.Name) and n.target.id == name:
                out.append(("walrus", n))
        elif isinstance(n, (ast.For, ast.AsyncFor)):
            out += [("for-target", n) for x in ast.walk(n.target)
                    if isinstance(x, ast.Name) and x.id == name]
        elif isinstance(n, (ast.With, ast.AsyncWith)):
            for item in n.items:
                if item.optional_vars is not None:
                    out += [("with-as", n) for x in ast.walk(item.optional_vars)
                            if isinstance(x, ast.Name) and x.id == name]
        elif isinstance(n, ast.ExceptHandler):
            if n.name == name:
                out.append(("except-as", n))
        elif isinstance(n, (ast.comprehension,)):
            out += [("comprehension", n) for x in ast.walk(n.target)
                    if isinstance(x, ast.Name) and x.id == name]
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if n.name == name:
                out.append(("def", n))
        elif isinstance(n, (ast.Import, ast.ImportFrom)):
            for a in n.names:
                if (a.asname or a.name.split(".")[0]) == name:
                    out.append(("import", n))
        elif isinstance(n, (ast.Global, ast.Nonlocal)):
            if name in n.names:
                out.append(("global/nonlocal", n))
        elif isinstance(n, ast.Delete):
            out += [("del", n) for t in n.targets for x in ast.walk(t)
                    if isinstance(x, ast.Name) and x.id == name]
        # NOTE: A match/case PATTERN BINDS THROUGH A PLAIN STRING FIELD, NOT AN ast.Name. MatchAs and
        # MatchStar carry `name`, and MatchMapping carries `rest`; none of them is a Name node, so a
        # census built on Name/Store walks straight past them. 1.0.0_SA_CTO defeated the previous
        # version three ways on exactly this (`case bucket:`, `case _latest_date_partition:`,
        # `case {**bucket}:`). This is ordinary syntactic binding, not the accepted dataflow limit.
        # Guarded by getattr because these node types do not exist before Python 3.10 and this file
        # is linted at py39.
        for attr, field in (("MatchAs", "name"), ("MatchStar", "name"), ("MatchMapping", "rest")):
            node_type = getattr(ast, attr, None)
            if node_type is not None and isinstance(n, node_type) and getattr(n, field, None) == name:
                out.append(("match-pattern", n))
        # NOTE: EVERY ast.arguments UNDER THE SCOPE IS A BINDING SITE -- a nested def, an async def and a
        # lambda all bind their parameter names, and 2.0.0_SA_COO~G's G-1 defeated the previous
        # version on exactly that: `def _probe(bucket): return <approved call>` then
        # `_probe("any-other-bucket")` read as "bucket bound once" while the call could reach ANY
        # bucket through the one approved literal. Counting only Lambda params, and only the
        # enclosing function's own params, left nested defs invisible.
        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
            kind = "lambda-param" if isinstance(n, ast.Lambda) else "nested-param"
            if name in _params_of(n):
                out.append((kind, n))
    return out


def _params_of(fn):
    a = fn.args
    named = list(a.posonlyargs) + list(a.args) + list(a.kwonlyargs)
    named += [x for x in (a.vararg, a.kwarg) if x is not None]
    return {x.arg for x in named}


def _decorated(node):
    return bool(getattr(node, "decorator_list", []))


def authority_ok(auth, entry_id):
    """(True, note) only when the pin RESOLVES and the pinned record CONTAINS this entry's ruling id.

    NOTE: "authority prose alone is not a grant" (IRPT-M-LEGACY-READ-02/03), made mechanical. A record
    path and a ruling id are just strings until something reads the object they name -- so the gate
    reads it: a FULL 40-hex pin (an abbreviation can become ambiguous as the repo grows), the blob at
    that pin, and the ruling id present in those bytes. Anything else refuses the ENTRY, not the file.
    """
    if not isinstance(auth, dict):
        return False, "authority is not an object"
    record, pin = auth.get("record"), auth.get("pin")
    if not isinstance(record, str) or not isinstance(pin, str):
        return False, "authority needs a record path and a full pin"
    if not FULL_PIN_RE.match(pin):
        return False, "authority pin %r is not a full 40-hex commit id" % pin
    rc, _out, _err = git("cat-file", "-e", "%s^{commit}" % pin)
    if rc != 0:
        return False, "authority pin %s does not resolve to a commit in this repository" % pin[:12]
    rc, out, _err = git("show", "%s:%s" % (pin, record))
    if rc != 0:
        return False, "%s is not present at pin %s" % (record, pin[:12])
    if not isinstance(entry_id, str) or not entry_id:
        return False, "entry has no id to look for"
    # NOTE: WORD-BOUNDED, NEVER A SUBSTRING. 2.0.0_SA_COO~G's G-4: an unanchored match let the ids
    # "LEGACY" and "IRPT-M-LEGACY-READ-0" both resolve against the real record, so a truncated or
    # deliberately shortened id would have been accepted as the authority for the full one.
    if not re.search(r"(?<![0-9A-Za-z_-])%s(?![0-9A-Za-z_-])" % re.escape(entry_id), text_of(out)):
        return False, ("the record at pin %s does not contain the ruling id %r as a whole token"
                       % (pin[:12], entry_id))
    return True, "pin %s resolves and its %s carries %s" % (pin[:12], record.rsplit("/", 1)[-1], entry_id)


def load_legacy_reads():
    """[(entry, None)] for usable entries, [(raw, reason)] for refused ones. Never raises.

    NOTE: THE CARRIER IS READ FROM COMMITTED HEAD, NEVER FROM DISK OR THE INDEX (2.0.0_SA_COO~G's
    pre-review, adopted as IRPT-M-LEGACY-READ-03). Reading it from the worktree would let the very
    commit being graded carry the entry that authorizes it -- a SELF-GRANT, and the gate would have
    no way to see it. Reading HEAD forces an entry to land in an earlier, separately reviewed commit.
    """
    rc, out, _err = git("show", "HEAD:%s" % LEGACY_READS_REL)
    if rc != 0:
        return [], []  # absent at HEAD: no waiver anywhere, which is the safe default
    try:
        doc = json.loads(text_of(out))
    except ValueError as exc:
        return [], [(None, "carrier at HEAD unreadable (%s): no waiver" % type(exc).__name__)]
    if not isinstance(doc, dict) or not isinstance(doc.get("entries"), list):
        return [], [(None, "carrier malformed (no entries list): no waiver")]
    good, bad, keys = [], [], {}
    # NOTE: AMBIGUITY IS COUNTED ON THE RAW ENTRIES, BEFORE ANY VALIDITY FILTER. The first version
    # counted duplicates only among entries that had already passed validation, so a VALID entry
    # beside a MALFORMED twin for the same file+literal left exactly one usable entry -- the
    # malformed one was discarded and its ambiguity with it. 1.0.0_SA_CTO's LR-02 broke ec40acbf on
    # precisely that. Two records claiming the same key is ambiguous whatever either one says.
    raw_keys = {}
    for raw in doc["entries"]:
        if isinstance(raw, dict) and isinstance(raw.get("file"), str) and isinstance(raw.get("literal"), str):
            raw_keys.setdefault((raw["file"], raw["literal"]), 0)
            raw_keys[(raw["file"], raw["literal"])] += 1
    raw_dup = {k for k, n in raw_keys.items() if n > 1}
    for raw in doc["entries"]:
        if not isinstance(raw, dict):
            bad.append((raw, "entry is not an object"))
            continue
        missing = [f for f in LEGACY_READ_FIELDS if f not in raw]
        extra = [k for k in raw if k not in LEGACY_READ_FIELDS]
        if missing or extra:
            bad.append((raw, "entry %r malformed (missing %s, unknown %s)"
                        % (raw.get("id"), missing or "-", extra or "-")))
            continue
        rc = raw.get("read_context")
        if isinstance(rc, dict) and rc.get("kind") == R20_KIND:
            # R20 DECLARED EXCEPTION: fields exactly R20_FIELDS, a ledger row id, a count, a date or PERMANENT cutoff,
            # and the same authority read as every other entry (a pinned record carrying this entry's id).
            occ, reg = rc.get("occurrences"), rc.get("register_ref")
            if sorted(rc) != sorted(R20_FIELDS):
                bad.append((raw, "entry %r r20_exception read_context is not exactly %s" % (raw.get("id"), list(R20_FIELDS))))
                continue
            if (not isinstance(reg, str) or not R20_REGISTER_RE.match(reg)
                    or not isinstance(occ, int) or isinstance(occ, bool) or occ < 1):
                bad.append((raw, "entry %r r20_exception read_context is malformed (register_ref a ledger row id like X11,"
                                 " occurrences an int >= 1)" % raw.get("id")))
                continue
            cutoff = raw.get("as_of_cutoff")
            if cutoff != R20_PERMANENT and not _cutoff_parses(cutoff):
                bad.append((raw, "entry %r as_of_cutoff must be a YYYY-MM-DD date or PERMANENT" % raw.get("id")))
                continue
            ok_auth, why_auth = authority_ok(raw.get("authority"), raw.get("id"))
            if not ok_auth:
                bad.append((raw, "entry %r authority refused: %s" % (raw.get("id"), why_auth)))
                continue
            keys.setdefault((raw["file"], raw["literal"]), []).append(raw)
            good.append(raw)
            continue
        if isinstance(rc, dict) and "kind" in rc:
            # tf_local is the ONLY other named kind; any other kind value refuses the entry.
            if rc.get("kind") != TF_LOCAL_KIND or sorted(rc) != sorted(TF_LOCAL_FIELDS):
                bad.append((raw, "entry %r read_context kind %r is not exactly %s"
                            % (raw.get("id"), rc.get("kind"), list(TF_LOCAL_FIELDS))))
                continue
            occ, refs = rc.get("occurrences"), rc.get("reference_count")
            if (not isinstance(rc.get("local_name"), str) or not TF_LOCAL_NAME_RE.match(rc.get("local_name"))
                    or not isinstance(occ, int) or isinstance(occ, bool) or occ != 1
                    or not isinstance(refs, int) or isinstance(refs, bool) or refs < 1):
                bad.append((raw, "entry %r tf_local read_context is malformed (local_name an identifier,"
                                 " occurrences exactly 1, reference_count an int >= 1)" % raw.get("id")))
                continue
            ok_auth, why_auth = authority_ok(raw.get("authority"), raw.get("id"))
            if not ok_auth:
                bad.append((raw, "entry %r authority refused: %s" % (raw.get("id"), why_auth)))
                continue
            keys.setdefault((raw["file"], raw["literal"]), []).append(raw)
            good.append(raw)
            continue
        if not isinstance(rc, dict) or sorted(rc) != sorted(SITE_FIELDS):
            bad.append((raw, "entry %r read_context is not exactly %s" % (raw.get("id"), list(SITE_FIELDS))))
            continue
        ba = rc.get("bucket_arg")
        if (not isinstance(rc.get("helper"), str) or not isinstance(rc.get("helper_body_sha256"), str)
                or not isinstance(rc.get("arg_index"), int) or isinstance(rc.get("arg_index"), bool)
                or not isinstance(rc.get("enclosing_function"), str)
                or not isinstance(rc.get("occurrences"), int) or isinstance(rc.get("occurrences"), bool)
                or not isinstance(ba, dict) or sorted(ba) != ["name", "value"]
                or not isinstance(ba.get("name"), str) or not isinstance(ba.get("value"), str)):
            bad.append((raw, "entry %r read_context is malformed" % raw.get("id")))
            continue
        ok_auth, why_auth = authority_ok(raw.get("authority"), raw.get("id"))
        if not ok_auth:
            bad.append((raw, "entry %r authority refused: %s" % (raw.get("id"), why_auth)))
            continue
        keys.setdefault((raw["file"], raw["literal"]), []).append(raw)
        good.append(raw)
    # A DUPLICATE AUTHORITY IS AMBIGUOUS, AND AMBIGUOUS IS REFUSE: both copies are dropped, never
    # resolved by order, because "the first one wins" is a rule nobody wrote down.
    dup = {k for k, v in keys.items() if len(v) > 1} | raw_dup
    if dup:
        good = [e for e in good if (e["file"], e["literal"]) not in dup]
        # keep the file+literal on the refusal so the denial reason can reach the verdict line
        bad += [({"file": dup_file, "literal": dup_lit},
                 "duplicate authority for this file and literal: both entries dropped, ambiguity is never"
                 " resolved by order") for (dup_file, dup_lit) in sorted(dup)]
    return good, bad


def _cutoff_parses(value):
    """True only for a YYYY-MM-DD string. The R20 kind also admits the word PERMANENT, checked by its caller."""
    if not isinstance(value, str):
        return False
    try:
        datetime.datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return False
    return True


def _expired(entry, now):
    """True when the waiver is not in force. The cutoff date is INCLUSIVE; it dies at 00:00:00Z the next day."""
    try:
        day = datetime.datetime.strptime(str(entry["as_of_cutoff"]), "%Y-%m-%d").replace(
            tzinfo=datetime.timezone.utc)
    except (ValueError, TypeError):
        return True  # an unparseable cutoff is an expired cutoff, never an open one
    return now >= day + datetime.timedelta(days=1)


def legacy_read_ok(entry, post_text):
    """(True, note) only for the ONE approved call site, with the approved bucket and an unchanged helper.

    NOTE: THIS IS AN ALLOWLIST OF ONE SITE, not a read/write classifier. Six conditions, every one of
    which must hold; each is also one of the ruling's named refusals:
      1. the whole literal occurs EXACTLY the approved number of times in the post-image
         -> a new duplicate occurrence anywhere refuses
      2. that occurrence is a POSITIONAL argument at the approved index of a direct Call to the
         approved helper NAME -> an alias, a method call, a keyword form or a variable refuses
      3. the call sits lexically inside the approved enclosing function -> the same call moved
         elsewhere refuses
      4. the bucket argument is the approved NAME, assigned EXACTLY ONCE inside that function, to the
         approved constant -> a second assignment, a parameter or a computed bucket refuses
      5. the helper is defined in this file and its normalized source hashes to the REVIEWED bytes
         -> a helper edited to write refuses, and the approved edit in the candidate is what was hashed
      6. anything unparseable or unfound refuses
    NOTE: An ALTERNATE read helper is NOT authorized: _read_parquet reading the same key refuses, because
    the grant is this site, not this string.
    """
    try:
        tree = ast.parse(post_text)
    except SyntaxError as exc:
        return False, "post-image does not parse (%s)" % exc.__class__.__name__
    want = entry["literal"]
    rc = entry["read_context"]
    helper, want_sha = rc["helper"], rc["helper_body_sha256"]
    idx, encl = rc["arg_index"], rc["enclosing_function"]
    bname, bvalue = rc["bucket_arg"]["name"], rc["bucket_arg"]["value"]

    total = sum(1 for n in ast.walk(tree)
                if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value == want)
    if total != rc["occurrences"]:
        return False, ("the whole literal occurs %d time(s), approved %d: a moved or duplicated"
                       " occurrence is not authorized" % (total, rc["occurrences"]))

    encl_binds = _binds_of(tree, encl)
    if len(encl_binds) != 1 or encl_binds[0][0] != "def":
        return False, ("the enclosing name %r is bound %d time(s) in this module (%s), approved exactly one"
                       " function definition" % (encl, len(encl_binds), ", ".join(k for k, _ in encl_binds) or "none"))
    fn = encl_binds[0][1]
    if not isinstance(fn, ast.FunctionDef):
        return False, "the enclosing name %r is not a plain function definition" % encl

    # NOTE: THE HELPER NAME MUST BE BOUND EXACTLY ONCE IN THE WHOLE MODULE, AND THAT BINDING MUST BE THE
    # DEF WE HASH. A second def wins at runtime (Python binds the LAST one) while a naive first-match
    # hashes the FIRST -- so the reviewed bytes and the called bytes can differ with nothing to see.
    # A local rebinding inside the enclosing function defeats the hash the same way.
    hbinds = _binds_of(tree, helper)
    if len(hbinds) != 1 or hbinds[0][0] != "def":
        return False, ("the read helper name %r is bound %d time(s) in this module (%s), approved exactly one"
                       " function definition" % (helper, len(hbinds), ", ".join(k for k, _ in hbinds) or "none"))
    hdef = hbinds[0][1]
    if not isinstance(hdef, ast.FunctionDef):
        return False, "the read helper name %r is not a plain function definition" % helper
    if helper in _params_of(fn) or any(k != "def" for k, _ in _binds_of(fn, helper)):
        return False, "the read helper name %r is rebound inside %s" % (helper, encl)
    # NOTE: A DECORATOR IS OUTSIDE THE HASHED BYTES. ast.get_source_segment(FunctionDef) starts at `def`,
    # so decorator_list never reaches the hash -- and a decorator can replace the helper outright or
    # make it write, with the reviewed hash unchanged (G-2/G-3). Both the helper and the enclosing
    # function must therefore be undecorated; this is a refusal, not an attempt to hash decorators,
    # because "which decorators are safe" is a judgment no gate should be making.
    if _decorated(hdef):
        return False, "the read helper %r carries a decorator, which is outside the reviewed bytes" % helper
    if _decorated(fn):
        return False, "%s carries a decorator, which is outside the reviewed bytes" % encl
    seg = ast.get_source_segment(post_text, hdef)
    if seg is None:
        return False, "cannot read the source of helper %r" % helper
    got = hashlib.sha256(_norm_body(seg).encode("utf-8")).hexdigest()
    if got != want_sha:
        return False, ("read helper %r is not the REVIEWED text (sha256 %s, approved %s)"
                       % (helper, got[:12], str(want_sha)[:12]))

    # the bucket name must be bound EXACTLY ONCE inside the enclosing function, by a plain assignment,
    # to the approved constant -- and never as a parameter, a loop target, a walrus, a with-as, an
    # import alias or anything else _binds_of recognises.
    bbinds = _binds_of(fn, bname)
    if bname in _params_of(fn):
        return False, "%r is a parameter of %s: its value is not fixed by this file" % (bname, encl)
    if len(bbinds) != 1:
        return False, ("%r is bound %d time(s) in %s (%s), approved exactly 1: an ambiguous bucket is not"
                       " authorized" % (bname, len(bbinds), encl, ", ".join(k for k, _ in bbinds) or "none"))
    kind, node = bbinds[0]
    if kind != "assign":
        return False, "%r in %s is bound by %s, not a plain assignment" % (bname, encl, kind)
    if not (isinstance(node.value, ast.Constant) and node.value.value == bvalue):
        return False, "%r in %s is not assigned the approved constant %r" % (bname, encl, bvalue)

    # NOTE: AND THE APPROVED FUNCTION CARRIES NO match STATEMENT AT ALL. Enumerating the three known
    # pattern binders above fixes the cases measured; refusing the statement outright is what makes
    # the recognizer safe against pattern node types this code has never seen. The approved case
    # contains no match, so this costs the authorized read nothing.
    match_type = getattr(ast, "Match", None)
    if match_type is not None and any(isinstance(n, match_type) for n in ast.walk(fn)):
        return False, ("%s contains a match statement; pattern-matching syntax is not supported for this"
                       " narrow approved case" % encl)

    # NOTE: THE APPROVED CALL MUST SIT DIRECTLY IN THE ENCLOSING FUNCTION'S OWN BODY, never inside a
    # nested def, lambda or class. ast.walk descends into them, so without this the site could be
    # parameterised out of the approved bucket (G-1's D2/D3) while every count still read 1.
    nested = [n for n in ast.walk(fn)
              if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)) and n is not fn]
    for scope in nested:
        for n in ast.walk(scope):
            if isinstance(n, ast.Constant) and isinstance(n.value, str) and n.value == want:
                return False, ("the approved literal appears inside a nested %s within %s; only the"
                               " function's own body is authorized" % (type(scope).__name__, encl))

    # the single occurrence must be the approved positional argument of the approved call, inside fn
    hits = 0
    for n in ast.walk(fn):
        if not isinstance(n, ast.Call) or not isinstance(n.func, ast.Name) or n.func.id != helper:
            continue
        if any(isinstance(kw.value, ast.Constant) and kw.value.value == want for kw in n.keywords):
            return False, "the literal is passed as a KEYWORD argument; only the approved positional form is authorized"
        if len(n.args) <= idx:
            continue
        a = n.args[idx]
        if isinstance(a, ast.Constant) and a.value == want:
            if not (len(n.args) > 1 and isinstance(n.args[1], ast.Name) and n.args[1].id == bname):
                return False, "the call's bucket argument is not the approved name %r" % bname
            hits += 1
    if hits != 1:
        return False, ("%d call(s) match the approved site (helper %s, arg %d, inside %s), approved exactly 1"
                       % (hits, helper, idx, encl))
    return True, ("the single occurrence is positional arg %d of %s(%s=...) inside %s, helper text as reviewed"
                  % (idx, helper, bname, encl))


def tf_local_ok(entry, post_text):
    """(True, note) only when a .tf file carries the literal as the value of ONE `locals` entry, referenced N times.

    NOTE: THE tf_local KIND (laptop 1.0.0_SA_CTO msg 102531). Four conditions, every one must hold, each refusal
    naming which: (a) the literal occurs in the file text exactly `occurrences` (== 1) times; (b) that occurrence is
    the value of exactly one line `<local_name> = "<literal>"` inside a top-level `locals {` block; (c) the local
    is assigned nowhere else in the file; (d) `local.<local_name>` is referenced exactly `reference_count` times.
    Any structure the brace scan cannot follow refuses: could-not-parse is never a pass.
    """
    rc = entry["read_context"]
    want, name = entry["literal"], rc["local_name"]
    occ, nrefs = rc["occurrences"], rc["reference_count"]
    total = post_text.count(want)
    if total != occ:
        return False, ("tf_local: the literal occurs %d time(s) in the file text, approved %d: a duplicated or"
                       " inlined occurrence is not authorized" % (total, occ))
    assign_re = re.compile(r'^\s*%s\s*=\s*"%s"\s*(?:#.*|//.*)?$' % (re.escape(name), re.escape(want)))
    any_assign_re = re.compile(r'^\s*%s\s*=' % re.escape(name))
    lines = post_text.splitlines()
    depth, block, assign_lines, other_assigns = 0, None, [], []
    for no, line in enumerate(lines, 1):
        code = re.sub(r'"(?:[^"\\]|\\.)*"', '""', line)  # braces inside strings never move the depth
        code = re.split(r"#|//", code, maxsplit=1)[0]
        if depth == 0:
            head = code.strip()
            block = "locals" if re.match(r"^locals\s*\{", head) else ("other" if "{" in head else None)
        if assign_re.match(line):
            assign_lines.append((no, depth, block))
        elif any_assign_re.match(line):
            other_assigns.append(no)
        depth += code.count("{") - code.count("}")
        if depth < 0:
            return False, "tf_local: the brace scan went negative at line %d: unparseable, refused" % no
    if depth != 0:
        return False, "tf_local: the brace scan ends at depth %d: unparseable, refused" % depth
    if len(assign_lines) != 1:
        return False, ("tf_local: %d line(s) assign %s = the literal, approved exactly one"
                       % (len(assign_lines), name))
    ano, adepth, ablock = assign_lines[0]
    if ablock != "locals" or adepth != 1:
        return False, ("tf_local: the assignment at line %d is not a direct entry of a top-level locals block"
                       % ano)
    if other_assigns:
        return False, ("tf_local: %s is assigned again at line(s) %s: exactly one assignment is authorized"
                       % (name, ", ".join(str(n) for n in other_assigns)))
    refs = len(re.findall(r"(?<![0-9A-Za-z_.-])local\.%s(?![0-9A-Za-z_-])" % re.escape(name), post_text))
    if refs != nrefs:
        return False, ("tf_local: local.%s is referenced %d time(s), approved %d" % (name, refs, nrefs))
    return True, ("the single occurrence is the value of locals.%s (line %d), referenced %d time(s) as reviewed"
                  % (name, ano, refs))


def r20_exception_ok(entry, post_text):
    """(True, note) only when the file text carries the literal EXACTLY `occurrences` times.

    NOTE: THE R20 KIND GRADES NAMING, NOT ACCESS. The register row and Andrew's acknowledgement say the departure is
    read-only; a gate cannot prove that from bytes (the N2 refinement: a write-verb denylist is insufficient), so it
    does not pretend to. What it CAN hold is the count: a second occurrence, in any file type, is a new site the
    register did not declare and it refuses by count. Any file type is admitted because the declared exception is
    about a key, not a language.
    """
    if not isinstance(post_text, str):
        return False, "r20_exception: no post-image text to count in"
    want, occ = entry["literal"], entry["read_context"]["occurrences"]
    total = post_text.count(want)
    if total != occ:
        return False, ("r20_exception: the literal occurs %d time(s) in the file text, declared %d: an undeclared"
                       " occurrence is not covered by register entry %s" % (total, occ, entry["read_context"]["register_ref"]))
    return True, ("%d occurrence(s) as declared by register entry %s" % (total, entry["read_context"]["register_ref"]))


def waivers_for(path, post_text, now=None):
    """{literal: (entry, note)} for this file: the waivers that are IN FORCE and RECOGNIZED here.

    The checker is picked by the file's suffix: a .py site is graded by legacy_read_ok and must carry the
    kind-less read_context; a .tf site is graded by tf_local_ok and must carry kind tf_local. A mismatch is
    a DENIED waiver, with the reason.
    """
    now = now or datetime.datetime.now(datetime.timezone.utc)
    good, bad = load_legacy_reads()
    out, denied = {}, {}
    for raw, reason in bad:
        if isinstance(raw, dict) and raw.get("file") == path and isinstance(raw.get("literal"), str):
            denied[raw["literal"]] = reason
    for entry in good:
        if entry["file"] != path:
            continue
        is_r20 = entry["read_context"].get("kind") == R20_KIND
        if not (is_r20 and entry.get("as_of_cutoff") == R20_PERMANENT) and _expired(entry, now):
            denied[entry["literal"]] = "expired: cutoff %s inclusive UTC" % entry.get("as_of_cutoff")
            continue
        if is_r20:
            ok, note = r20_exception_ok(entry, post_text)
            if ok:
                out[entry["literal"]] = (entry, note)
            else:
                denied[entry["literal"]] = note
            continue
        is_tf_kind = entry["read_context"].get("kind") == TF_LOCAL_KIND
        if path.endswith(".tf"):
            if not is_tf_kind:
                denied[entry["literal"]] = "a .tf site needs read_context kind tf_local; this entry is a Python call site"
                continue
            ok, note = tf_local_ok(entry, post_text)
        else:
            if is_tf_kind:
                denied[entry["literal"]] = "a tf_local read_context authorizes a .tf file only, never %s" % path
                continue
            ok, note = legacy_read_ok(entry, post_text)
        if ok:
            out[entry["literal"]] = (entry, note)
        else:
            denied[entry["literal"]] = note
    if denied:
        out["__denied__"] = denied
    return out


# --------------------------------------------------------------------------- the matrix
_PATTERN_CACHE = {}


def _per_firm_rulings():
    """{key: row} of the registry's per-firm key rulings (a stored-file prefix the code fills per firm), or the load error text."""
    if "rows" not in _PATTERN_CACHE:
        try:
            rows = _rootcheck().load_key_rulings()
            _PATTERN_CACHE["rows"] = dict((r["key"], r) for r in rows.values() if r.get("bucket_per") and r.get("canonical"))
        except Exception as exc:
            _PATTERN_CACHE["rows"] = "%s: %s" % (type(exc).__name__, exc)
    return _PATTERN_CACHE["rows"]


def _pattern_root(rcm, value):
    """The root-map key that holds `value` (the longest map key equal to it or a path prefix of it), or None."""
    try:
        keys = list((rcm.opal_naming_rootmap.load_map(rcm.DEFAULT_MAP).get("roots") or {}))
    except Exception:
        return None
    hit = [k for k in keys if value == k or value.startswith(k + "/")]
    return max(hit, key=len) if hit else None


def _pattern_row(lit, rulings=None, place_fn=None, path="?"):
    """The judge() result (verdict, canonical, why, counts-as) of a literal the first-segment classifier left untyped but which IS the key of a per-firm key ruling, or
    None. place() decides: PATTERN prints (counts PASS: a code pattern is never refused, never silent); any other kind WARNs with
    place()'s own text. With no root to ask, or the diff not in this checkout, the ruling itself is the answer (a per-firm row
    is a PATTERN in decide())."""
    rows = _per_firm_rulings() if rulings is None else rulings
    if isinstance(rows, str):
        return ("RAISE", "(rule or registry defect)", "the key rulings could not be read: %s" % rows, "WARN")
    row = rows.get(lit.value)
    if row is None:
        return None
    canon = row["canonical"]
    res, root = None, None
    try:
        if place_fn is not None:
            root, res = "-", place_fn(lit.value, "S3Key", "-")
        elif _diff_repo() == REPO:
            rcm = _rootcheck()
            root = _pattern_root(rcm, lit.value)
            if root:
                res = rcm.place(lit.value, "S3Key", root, where="%s:%d" % (path, lit.line))
    except Exception as exc:
        return ("RAISE", canon, "place() could not answer for the per-firm key: %s: %s" % (type(exc).__name__, exc), "WARN")
    if res is None:
        return ("PATTERN", canon,
                "a per-firm stored-file prefix (key ruling, bucket_from %s); no root to ask place(), so the ruling answers: the code fills {scope} per firm"
                % row.get("bucket_from"), "PASS")
    if res["kind"] == "PATTERN":
        return ("PATTERN", canon, "place() in root %s: %s" % (root, res["detail"]), "PASS")
    return (res["kind"], res.get("form") or canon,
            "place() in root %s says %s, not PATTERN: %s: WARN" % (root, res["kind"], res["detail"]), "WARN")


# --------------------------------------------------------------------------- the round-23 limbs (LGIC_ENFORCE FWD-8)
# Limb (a): a staged RENAME is graded against its SOURCE's HEAD bytes. safe-commit diffs the staged path alone, so an R100
# rename reads as an added file; the source's deletion is outside that pathspec. Limb (b): a literal whose exact name the
# census LIVE plane holds is EXISTING (an adoption declares a resource already running). EXISTING is never CONFORMANT.
LIVE_BUDGET = 300  # seconds: census_live's budget for the running-name read
_RENAMES = {}  # the whole index's {dest: source} renames, read once per run (limb a); a test may replace "map"
_LIVE = {"read": None, "done": False, "nodes": {}, "vintage": "", "error": ""}  # limb b, once per run; read None = limb off


class _LiveFailed(Exception):
    """The live read failed or printed no vintage: the caller leaves `new` as it is (fail closed to today's behaviour)."""


def _rename_map(raw):
    """{dest: source} of the R rows of `git diff --cached -M --name-status -z` output (raw bytes). -z keeps paths unquoted."""
    fields = raw.decode("utf-8", errors="replace").split("\0")
    out, i = {}, 0
    while i < len(fields):
        st = fields[i]
        if not st:
            i += 1
        elif st[:1] == "R" and i + 2 < len(fields):
            out[fields[i + 2]] = fields[i + 1]
            i += 3
        else:
            i += 2
    return out


def _staged_renames():
    """The whole index's renames (not the staged pathspec: the source is outside it). A failed git call is no renames."""
    if "map" not in _RENAMES:
        rc, out, _err = git_in(_diff_repo(), "diff", "--cached", "-M", "--name-status", "-z")
        _RENAMES["map"] = _rename_map(out) if rc == 0 else {}
    return _RENAMES["map"]


def _head_bytes(repo, rel):
    """The HEAD bytes of `rel` as text, or None when HEAD carries no such file or the git call fails."""
    rc, out, _err = git_in(repo, "show", "HEAD:%s" % rel)
    return text_of(out) if rc == 0 else None


def _live_read_plane(nm):
    """(nodes, vintage, command) of the census LIVE plane, through lib/opal_naming.py census_live (the one reader)."""
    return nm.mod.census_live(budget=LIVE_BUDGET)


def _live_reset(reader):
    """Install `reader` as the live plane for this run (None = the limb is off) and clear the once-per-run cache."""
    _LIVE.update(read=reader, done=False, nodes={}, vintage="", error="")


def _live_holder(nm, value, typ):
    """(node type, vintage) when the live plane holds the exact name `value` as a node of the declared type `typ` (any type
    when the literal has none: a hand-kept carrier), None when it runs nowhere as that type. A node of another type that
    shares the name does not make a declaration of `typ` EXISTING. Raises _LiveFailed when the read fails or cannot print
    its vintage. The read runs once per run; a failure is cached and raised every time."""
    if not _LIVE["done"]:
        _LIVE["done"] = True
        try:
            nodes, vintage, _shown = _LIVE["read"](nm)
            if not vintage or not str(vintage).strip() or "UNREAD" in str(vintage):
                raise ValueError("the live read printed no vintage")
            _LIVE["vintage"] = str(vintage).strip()
            for nd in nodes:
                _LIVE["nodes"].setdefault(nd["name"], []).append(nd["type"])
        except Exception as exc:  # any failure of the read: fail closed, never a zero
            _LIVE["error"] = " ".join(("%s: %s" % (type(exc).__name__, exc)).split())
    if _LIVE["error"]:
        raise _LiveFailed(_LIVE["error"])
    same = [t for t in _LIVE["nodes"].get(value, []) if typ is None or t == typ]
    return None if not same else (same[0], _LIVE["vintage"])


def _live_limb(nm, lit, typ, note):
    """Limb (b) for one NEW literal: the value of `new` after the live read (False = the plane holds the name as the declared
    type). The one-line why text goes into `note` ('held' on a hit, 'failed' on a failed read; judge() prints 'failed' on
    REFUSE rows only)."""
    try:
        hit = _live_holder(nm, lit.value, typ)
    except _LiveFailed as exc:
        note["failed"] = "LIVE-READ-FAILED: %s" % str(exc)[:120]
        return True
    if hit is None:
        return True
    lit.live_held = True
    note["held"] = ("RUNNING-LIVE %s '%s' read from the live plane, %s: EXISTING, not minted by this diff"
                    % (hit[0], lit.value, hit[1]))
    return False


def judge(nm, path, lit, pre_text, waivers=None):
    """(line verdict, canonical, why, counts-as) for one literal, or None when it is not graded. The live limb's one line
    joins the why text: RUNNING-LIVE on any row of a name the plane holds; LIVE-READ-FAILED on a REFUSE row only."""
    note = {}
    j = _judge(nm, path, lit, pre_text, waivers, note)
    if j is None:
        return None
    extra = []
    if "held" in note:
        extra.append(note["held"])
    if "failed" in note and j[3] == "REFUSE":
        extra.append(note["failed"])
    if not extra:
        return j
    return (j[0], j[1], "%s; %s" % (j[2], "; ".join(extra)), j[3])


def _judge(nm, path, lit, pre_text, waivers, note):
    """The verdict of judge() (its body is the DEC-6 matrix); `note` collects the live limb's text."""
    if _resolves_to_tracked(lit.value):
        return None  # a value resolving to a tracked path at HEAD is a CITATION (R-11), not a mint
    typ, graded_as = nm.classify(lit.value, lit.hint)
    # a name BUILT by name() carries its firm as the builder's short form: the builder is the permitted route, not a hand-kept carrier
    carr = None if lit.built else nm.carrier(lit.value)
    if typ is None and carr is None:
        # Row LGIC_ENFORCE-D1-W2-S152: classify() types a "/" string only by its first segment (a bucket, a tier, a
        # registered system), so a per-firm stored-file prefix such as a code default is typed None and fell out here
        # ungraded; the gate then read PASS 0 graded. The registry's per-firm key rulings are the other way to know it is a key.
        return None if lit.built or lit.hint else _pattern_row(lit, path=path)
    new = pre_text is None or not _in_pre(lit, pre_text)
    # Limb (b), LAZY: read the live plane only for a NEW literal that the branches below would REFUSE (a hand-kept carrier, or
    # an OUT-OF-PATTERN / ALIAS name). A CONFORMANT or NOT-GRADED name is never refused, so it never pays for the read.
    if new and _LIVE["read"] is not None and (carr or (typ is not None and nm.grade(typ, graded_as)[0] in ("OUT-OF-PATTERN", "ALIAS"))):
        new = _live_limb(nm, lit, typ, note)
    carr_txt = ""
    if carr:
        carr_txt = "; hand-kept carrier of %r outside every permitted context: read it through lookup(%r)" % (carr[0], carr[1])
    # THE ONE CONSUMPTION POINT OF THE R20 DECLARED EXCEPTION. It sits ABOVE the NEW branches on purpose: a declared
    # exception is the one case where a NEW read of a legacy key is the ruled behaviour, and it is admitted only from a
    # HEAD-committed entry whose pinned record carries its id (authority_ok) and whose count holds (r20_exception_ok).
    r20_hit = (waivers or {}).get(lit.value)
    if r20_hit and isinstance(r20_hit[0], dict) and r20_hit[0].get("read_context", {}).get("kind") == R20_KIND:
        e = r20_hit[0]
        return ("DECLARED-EXCEPTION", "R20 %s" % e["read_context"]["register_ref"],
                "%s literal graded as %s is a DECLARED EXCEPTION under R20 register entry %s (waiver %s, owner %s, cutoff %s):"
                " %s. The register row carries the departure; this diff moves no key: WARN%s"
                % ("NEW" if new else "EXISTING", typ or "hand-kept carrier", e["read_context"]["register_ref"], e["id"],
                   e["owner"], e.get("as_of_cutoff"), r20_hit[1], carr_txt), "WARN")
    r20_denial = (waivers or {}).get("__denied__", {}).get(lit.value)
    new_deny_txt = "; a waiver entry exists for this literal and was NOT applied: %s" % r20_denial if (new and r20_denial) else ""
    if typ is None:
        canon = "lookup(%r)" % carr[1]
        if new:
            return "REFUSE", canon, "NEW hand-kept carrier (context rule)%s%s" % (carr_txt, new_deny_txt), "REFUSE"
        return "OUT-OF-PATTERN", canon, "EXISTING hand-kept carrier (context rule): WARN%s" % carr_txt, "WARN"
    verdict, canon, defect = nm.grade(typ, graded_as)
    if verdict == "RAISE":
        why = "RAISE as %s: rule or registry defect, not a refusal: %s" % (typ, defect)
        if new:
            # A literal the grammar cannot place is NEW to this file but may already be carried, byte for
            # byte, elsewhere at HEAD (2026-09-23, 1.0.0_SA_CTO 99842 on 2.0.0_SA_COO~M's "smartx/platform/silver/",
            # K3 "'platform' is not a tier": a pre-LGIC layout the retained build already reads). Copying an
            # existing pre-LGIC key into a new file mints nothing; under CLAUDE.md Rule 30 that layout reaches
            # conformance through its own migration project, never through this diff. So: EXISTING, WARN, with
            # the RAISE reason and the carrying path printed. A raising literal carried NOWHERE at HEAD keeps
            # the branches below unchanged.
            where = _carried_at_head(lit.value, path)
            if where:
                return ("RAISE-EXISTING", "(pre-LGIC key; conformance via its migration project, Rule 30)",
                        why + "; the same literal is already carried at HEAD in %s, so this copy mints nothing: WARN%s"
                        % (where, carr_txt), "WARN")
        if new and carr:
            return "REFUSE", "lookup(%r)" % carr[1], why + carr_txt + new_deny_txt, "REFUSE"
        return "RAISE", "(rule or registry defect)", why + carr_txt, "WARN"
    if verdict == "NOT-GRADED":
        return "NOT-GRADED", "-", "%s is outside the grade's domain (G1.2)" % typ, "PASS"
    if verdict == "NO-SYSTEM-ASKED":
        # The fourth verdict (LGIC_BLANKFIX BF-t-2): no system is asked of this kind of name, so no remedy is owed and
        # nothing here refuses it for lacking one. The hand-kept-carrier context rule is a different question and
        # still binds, exactly as for CONFORMANT.
        if new and carr:
            return "REFUSE", canon, "NO-SYSTEM-ASKED as %s, but a NEW%s" % (typ, carr_txt[1:]), "REFUSE"
        if carr:
            return verdict, canon, "NO-SYSTEM-ASKED as %s; EXISTING%s: WARN" % (typ, carr_txt[1:]), "WARN"
        return verdict, canon, "NO-SYSTEM-ASKED as %s: no system is asked of this kind of name" % typ, "PASS"
    rem = nm.remediation_of(typ, graded_as) if verdict == "OUT-OF-PATTERN" and not new else None
    if new and verdict in ("OUT-OF-PATTERN", "ALIAS"):
        return "REFUSE", canon, "NEW and %s as %s: REFUSE%s%s" % (verdict, typ, carr_txt, new_deny_txt), "REFUSE"
    if rem:
        # THE ONE CONSUMPTION POINT OF THE LEGACY-READ WAIVER (IRPT-M-LEGACY-READ-02). It sits BELOW
        # the NEW branch above, which is why a NEW or CHANGED literal can never reach it -- that
        # property is structural, not a check anyone has to remember.
        hit = (waivers or {}).get(lit.value)
        if hit and hit[0].get("remediation") == rem:
            return ("WAIVED-READ", canon,
                    "EXISTING and OUT-OF-PATTERN as %s under the live remediation %s, WAIVED as an authorized"
                    " LEGACY READ by %s (owner %s, cutoff %s inclusive UTC): %s. The remediation stays LIVE and"
                    " this waiver does not advance it%s"
                    % (typ, rem, hit[0]["id"], hit[0]["owner"], hit[0]["as_of_cutoff"], hit[1], carr_txt), "WARN")
        # NOTE: A DENIED WAIVER MUST SAY WHY IT WAS DENIED. Without this the refusal is byte-identical
        # whether no entry exists, the entry expired, the helper changed, or the call site moved --
        # and the author is left guessing which. Measured while building the controls: three arms
        # refused for the RIGHT reason and printed the WRONG one, so the control could not tell a
        # working recognizer from a waiver that never loaded.
        denial = (waivers or {}).get("__denied__", {}).get(lit.value)
        if hit and not denial:
            denial = ("the entry is written against remediation %r, but this literal resolves to %r"
                      % (hit[0].get("remediation"), rem))
        deny_txt = "; LEGACY-READ waiver NOT applied: %s" % denial if denial else ""
        return "REFUSE", canon, ("EXISTING and OUT-OF-PATTERN as %s in a surface remediations.json assigns to the live"
                                 " remediation %s: REFUSE unless the diff removes it%s%s"
                                 % (typ, rem, carr_txt, deny_txt)), "REFUSE"
    if verdict in ("OUT-OF-PATTERN", "ALIAS"):
        return verdict, canon, "EXISTING, touched, and %s as %s: WARN%s" % (verdict, typ, carr_txt), "WARN"
    if new and carr:
        return "REFUSE", canon, "CONFORMANT as %s, but a NEW%s" % (typ, carr_txt[1:]), "REFUSE"
    if carr:
        return "CONFORMANT", canon, "CONFORMANT as %s; EXISTING%s: WARN" % (typ, carr_txt[1:]), "WARN"
    return "CONFORMANT", canon, "CONFORMANT as %s" % typ, "PASS"


def _in_pre(lit, pre_text):
    for s in {lit.value, lit.raw}:
        if s and re.search(r"(?<![%s])%s(?![%s])" % (WORD_CHARS, re.escape(s), WORD_CHARS), pre_text):
            return True
    return False


def grade_file(nm, f, post_from_index):
    """[(verdict, path, line, string, canonical, why, counts-as)] for one file of the diff."""
    path = f["new"]
    if path is None:
        return []  # a deletion grades nothing
    if _is_record_tree(path):
        return []  # a RECORD tree is never opened (R-11/R-13): no pre-image read, no literal extraction
    if _is_gitattributes(path):
        return _grade_gitattributes(f)
    if not path.endswith(GRADED_EXT):
        return []
    pre_text = None
    diff_repo = _diff_repo()
    if f["old"] is not None:
        rc, out, _err = git_in(diff_repo, "show", "HEAD:%s" % f["old"])
        if rc == 0:
            pre_text = text_of(out)
        elif os.path.isfile(os.path.join(diff_repo, *f["old"].split("/"))):
            with open(os.path.join(diff_repo, *f["old"].split("/")), "rb") as fh:
                pre_text = text_of(fh.read())
    base_text = pre_text if f["old"] is not None else ""  # the hunks of an add are relative to nothing, renamed or not
    if f["old"] is None:
        # Limb (a): a staged RENAME destination is graded against its SOURCE's HEAD bytes as the pre-image.
        src = _staged_renames().get(path)
        if src:
            pre_text = _head_bytes(diff_repo, src)  # None when HEAD has no such source: today's NEW reading
    post_lines, added = apply_hunks(base_text or "", f["hunks"])
    if not added:
        return []
    post_text = "\n".join(post_lines) + "\n"
    if post_from_index:
        rc, out, _err = git_in(diff_repo, "show", ":%s" % path)
        if rc == 0:
            post_text = text_of(out)
            post_lines = post_text.split("\n")
            if post_lines and post_lines[-1] == "":
                post_lines.pop()
    first_added = min(added)
    _note_file(path, pre_text, post_text)
    rows = []

    # the generated-file check: before every exclusion, so a generated file under */tests/* is checked too
    marked = bool(nm.mark_re.search(post_text)) or bool(pre_text and nm.mark_re.search(pre_text))
    gen_ranges = []
    if marked:
        tag = "<generated-file-edit>"
        target = path if path in nm.targets else _nested_portal_path(path)
        if target not in nm.targets:
            return [("REFUSE", path, first_added, tag,
                     "not produced by lib/opal_naming.py generate (known targets: %d)" % len(nm.targets),
                     "the file carries the GENERATED mark but the generator does not produce it", "REFUSE")]
        try:
            expected = generator_output(nm, target, post_text)
        except Exception as exc:  # the generator cannot run: a registry defect, never a refusal
            return [("RAISE", path, first_added, tag, "(rule or registry defect)",
                     "the generator could not produce %s: %s: %s" % (path, type(exc).__name__, exc), "WARN")]
        if expected.rstrip("\n") != post_text.rstrip("\n"):
            exp_lines = expected.split("\n")
            diff_at = next((k + 1 for k, (a, b) in enumerate(zip(post_lines, exp_lines)) if a != b),
                           min(len(post_lines), len(exp_lines)) + 1)
            return [("REFUSE", path, diff_at, tag,
                     "python lib/opal_naming.py generate --out <dir> --target %s" % path,
                     "a hand edit to a GENERATED file: its bytes differ from the generator's output from line %d" % diff_at,
                     "REFUSE")]
        gen_ranges = generated_ranges(post_lines, nm)

    # the literal grade
    if path.startswith(REGISTRY_PREFIX):
        return rows  # the registry files: every token is permitted there
    if _is_fixture(path):
        return rows  # fixtures under a FIXTURE_DIRS folder (*/tests/* or */test/) are not graded
    if path.endswith(".py"):
        try:
            lits = py_literals(post_text, added)
        except SyntaxError:
            lits = []
            for ln, txt in sorted(added.items()):
                try:
                    lits += [Lit(x.value, x.raw, ln) for x in py_literals(txt.strip(), {1})]
                except SyntaxError:
                    lits += [Lit(v2, r2, ln) for kind, v2, r2, _l in scan(txt, "js") if kind == "str"]
    elif path.endswith((".js", ".mjs", ".ts")):
        lits = js_literals(post_text, added)
    elif path.endswith(".tf"):
        lits = tf_literals(post_text, added)
    elif path.endswith(".json"):
        if is_plan_artifact(post_text):
            return [("SKIP", path, first_added, "<machine-written plan file>", "-",
                     "top level carries format_version, terraform_version and resource_changes or"
                     " planned_values (a terraform show -json artifact): not graded", "PASS")]
        lits = json_literals(added)
        cited = _packaged_citations(post_text)
        for lit in lits:
            if lit.value in cited:
                lit.permitted = True  # the packaged name of a tracked source: a citation (R-11), not a mint
        _source_map_name_citations(nm.mod, path, added, lits, post_text)  # a builder-reproduced name cites, never mints
        _changelog_name_citations(nm.mod, path, lits, post_text)  # the recorder's changelog: the same live names
    else:
        lits = yaml_literals(added)
    waivers = waivers_for(path, post_text) if isinstance(post_text, str) else {}
    seen = set()
    for lit in lits:
        if lit.permitted or any(lo <= lit.line <= hi for lo, hi in gen_ranges):
            continue
        if (lit.line, lit.value) in seen:
            continue
        seen.add((lit.line, lit.value))
        j = judge(nm, path, lit, pre_text, waivers)
        if j:
            rows.append((j[0], path, lit.line, lit.value, j[1], j[2], j[3]))
            _note_place(nm, path, lit, pre_text, j)
    rows += grade_built(nm, path, post_text, pre_text, added, gen_ranges, waivers)
    return rows


def _built_sites(path, src, added):
    """[(line, args, why)] of the builder sites of one post-image; a Python fragment that does not parse is read line by line."""
    if path.endswith(".tf"):
        return tf_built(src, added)
    if not path.endswith(".py"):
        return []
    try:
        return py_built(src, added)
    except SyntaxError:
        out = []
        for ln, txt in sorted(added.items()):
            try:
                out += [(ln, a, w) for _l, a, w in py_built(txt.strip(), {1})]
            except SyntaxError:
                pass
        return out


def grade_built(nm, path, post_text, pre_text, added, gen_ranges, waivers):
    """Rows for the names BUILT at a call site of the added lines: compose with name() and grade like any literal, or say why not."""
    sites = _built_sites(path, post_text, added)
    if not sites:
        return []
    pre_built = set()
    if pre_text:
        for _ln, a, _w in _built_sites(path, pre_text, dict((k, "") for k in range(1, pre_text.count("\n") + 2))):
            if a is not None:
                try:
                    pre_built.add(nm.mod.name(**a))
                except Exception:  # a pre-image site name() refused is not a name that existed
                    pass
    # a built name sits in no text, so the NEW test (_in_pre) reads the pre-image plus the names its sites built
    pre_aug = None if pre_text is None else pre_text + "\n" + "\n".join(sorted(pre_built))
    rows, seen = [], set()
    for line, args, why in sites:
        if any(lo <= line <= hi for lo, hi in gen_ranges):
            continue
        built = None
        if args is not None:
            try:
                built = nm.mod.name(**args)
            except Exception as exc:  # name() refuses its arguments: say so, never grade a guess
                why = "name() refused the literal arguments %r: %s: %s" % (args, type(exc).__name__, exc)
        if built is None:
            rows.append(("BUILT-NOT-GRADED", path, line, why, "-", why, "PASS"))
            continue
        if (line, built) in seen:
            continue
        seen.add((line, built))
        try:
            hint = nm.mod._type_of_kind(args.get("kind"), nm.mod._schema())
        except Exception:
            hint = None
        lit = Lit(built, built, line, hint)
        lit.built = True
        j = judge(nm, path, lit, pre_aug, waivers)
        if j is None:
            why = "name() built %s but the gate could not classify it as a resource name" % built
            rows.append(("BUILT-NOT-GRADED", path, line, why, "-", why, "PASS"))
            continue
        rows.append((j[0], path, line, built, j[1], "built by name() at the call site: " + j[2], j[3]))
        _note_place(nm, path, lit, pre_aug, j)
    return rows


# --------------------------------------------------------------------------- the placement step (FWD-6)
_PLACE = {"cands": [], "files": {}}
_NOT_A_NAME_VERDICTS = ("DECLARED-EXCEPTION", "BUILT-NOT-GRADED", "NOT-GRADED", "RAISE", "RAISE-EXISTING", "WAIVED-READ", "SKIP")


def place_enforcing():
    """True while the switch file is present. There is no environment value and no argument that turns the step off."""
    return os.path.exists(PLACE_FILE)


def _place_reset():
    _PLACE["cands"] = []
    _PLACE["files"] = {}


def _note_file(path, pre_text, post_text):
    _PLACE["files"][path] = (pre_text, post_text)


def _note_place(nm, path, lit, pre_text, j):
    """Remember a NEW stored name that was graded as a name (not a carrier, not a declared exception) for the step."""
    if j is None or j[0] in _NOT_A_NAME_VERDICTS or lit.live_held or (not lit.built and nm.carrier(lit.value)):
        return  # a name the live plane holds is EXISTING, not minted by this diff: no placement candidate (FWD-8)
    typ, _graded_as = nm.classify(lit.value, lit.hint)
    if typ is None:
        return
    if pre_text is None or not _in_pre(lit, pre_text):
        _PLACE["cands"].append({"path": path, "line": lit.line, "value": lit.value, "typ": typ})


def _rootcheck():
    lib = os.path.join(REPO, "lib")
    if lib not in sys.path:
        sys.path.insert(0, lib)
    import opal_naming_rootcheck as rcm
    return rcm


def amend_row(row, res, on):
    """The row of a NEW name after place() answered `res`. row = (verdict, path, line, string, canonical, why, counts-as).
    FIX or HOLE in a MAPPED root: a REFUSE row naming the form and what is owed; counts-as PLACE-REFUSE while the switch is
    present, else WARN (an old REFUSE keeps its own counts-as). In an UNMAPPED root only an old REFUSE is amended, with the
    text, and keeps its counts-as unless the switch is present. Any other kind leaves the row as it is."""
    verdict, path, line, s, canon, why, counts = row
    if res["kind"] not in ("FIX", "HOLE"):
        return row
    old_refuse = counts == "REFUSE"
    if not res["mapped"] and not old_refuse:
        return row
    form, text = _rootcheck().refusal_text(res)
    if on:
        new_counts = "PLACE-REFUSE"
    else:
        new_counts = counts if old_refuse else "WARN"
    return ("REFUSE", path, line, s, form, "%s [grade() said: %s]" % (text, why), new_counts)


def ratchet_row(root_res, on):
    """The row of a root whose HOLE count grew."""
    return ("REFUSE", root_res["root"], 0, "<hole-count-ratchet>", "-", _rootcheck().ratchet_text(root_res),
            "PLACE-REFUSE" if on else "WARN")


def decide_exit(rows, enforce):
    """(summary, refused, warned, place_refused, exit code) of the graded rows. A PLACE-REFUSE row exits 1 whatever the older
    switch says; a REFUSE row exits 1 only while the older switch is on."""
    refused = sum(1 for r in rows if r[6] == "REFUSE")
    place_ref = sum(1 for r in rows if r[6] == "PLACE-REFUSE")
    warned = sum(1 for r in rows if r[6] == "WARN")
    overridden = sum(1 for r in rows if r[6] == "OVERRIDDEN")
    if (refused and enforce) or place_ref:
        summary = "REFUSE"
    elif refused or warned or overridden:
        summary = "WARN"
    else:
        summary = "PASS"
    return summary, refused, warned, place_ref, 1 if ((refused and enforce) or place_ref) else 0


def _audit_text_from_index(repo, rel):
    """The staged (index) copy of `rel` in `repo`, or (None, why). A path absent from the index is a reason, not an error."""
    try:
        p = subprocess.run(["git", "-C", repo, "show", ":" + rel], capture_output=True)
    except OSError as exc:
        return None, "git could not run (%s)" % exc
    if p.returncode != 0:
        return None, "no staged copy of %s (the row must be in the commit it permits)" % os.path.basename(rel)
    return p.stdout.decode("utf-8", "replace"), ""


def message_binding(message_path):
    """(sha256 hex, reason, why): the digest of the exact bytes of the message file the gate was handed and the reason on its first
    `# naming-place-override:` line ('' when the line is absent or empty), or (None, '', why) when no message can be read."""
    if not message_path:
        return None, "", "no commit message was handed to the gate (safe-commit.sh passes --message-file)"
    try:
        with open(message_path, "rb") as fh:
            raw = fh.read()
    except OSError:
        return None, "", "the message file %s cannot be read" % os.path.basename(message_path)
    m = OVERRIDE_LINE_RE.search(raw.decode("utf-8", "replace"))
    return hashlib.sha256(raw).hexdigest(), (m.group(1).strip() if m else ""), ""


def override_valid(ident, audit_path=None, repo=None, message_path=None):
    """(names, why): names is the set of refused names the audit row for `ident` covers, or None with the reason it passes
    nothing. BF-y-2: the row must exist, carry a non-empty reason, and its msg_sha256 must equal the sha256 of the message file
    handed in `message_path`, which must carry a non-empty `# naming-place-override:` line. There is no age window: the row is
    bound to ONE message. With no `audit_path` the row is read from the INDEX copy of OVERRIDE_AUDIT_REL in `repo` (default:
    this checkout), so the row honoured is the one that will land; `audit_path` (a file on disk) is for tests only."""
    if not ident or not ident.strip():
        return None, "the variable is empty"
    if audit_path:
        try:
            with open(audit_path, "r", encoding="utf-8") as fh:
                text = fh.read()
        except OSError:
            return None, "no audit log %s" % os.path.basename(audit_path)
    else:
        text, why = _audit_text_from_index(repo or REPO, OVERRIDE_AUDIT_REL)
        if text is None:
            return None, why
    for ln in text.splitlines():
        try:
            row = json.loads(ln)
        except ValueError:
            continue
        if not isinstance(row, dict) or str(row.get("id", "")) != ident.strip():
            continue
        if not str(row.get("reason", "")).strip():
            return None, "the audit row for %s carries an empty reason" % ident
        digest, msg_reason, why_msg = message_binding(message_path)
        if digest is None:
            return None, why_msg
        if not msg_reason:
            return None, "the commit message handed to the gate carries no non-empty `# naming-place-override:` line"
        want = str(row.get("msg_sha256", "")).strip().lower()
        if not want or want != digest:
            return None, "the audit row for %s is bound to a different message (msg_sha256 %s, this message %s)" % (
                ident, (want[:12] + "...") if want else "empty", digest[:12] + "...")
        names = row.get("names", [])
        if not isinstance(names, list):
            return None, "the audit row for %s has a names field that is not a list" % ident
        return set(str(n) for n in names if str(n)), ""
    return None, "no audit row has id %s (safe-commit.sh is the only setter of this variable)" % ident


def apply_override(rows, names):
    """The rows with every PLACE-REFUSE row whose string the audit row names turned into an OVERRIDDEN row (counts OVERRIDDEN)."""
    out = []
    for r in rows:
        if r[6] == "PLACE-REFUSE" and r[3] in names:
            out.append(("OVERRIDDEN", r[1], r[2], r[3], r[4], "%s [placement refusal overridden, audited]" % r[5], "OVERRIDDEN"))
        else:
            out.append(r)
    return out


def place_step(rows, meta):
    """Ask place() for the NEW names of the diff and run the ratchet on the roots it touches. Returns the amended rows; notice
    lines go to `meta`. Never raises: a step that cannot run adds an error row (refusing only while the switch is present)."""
    if not any(p.startswith(PLACE_PATH_PREFIX) and (p.endswith(".tf") or any(c["path"] == p for c in _PLACE["cands"]))
               for p in _PLACE["files"]):
        return rows
    on = place_enforcing()
    if not on and not PLACE_PREVIEW:
        # Row LGIC_BLANKFIX-W1-S22 (1.0.0_SA_CTO ruling 2026-10-09): with the switch absent the step's rows can only WARN, and the
        # root census costs ~13 s per root on every seat's .tf commit; skip it. NAMING_PLACE_PREVIEW=1 runs it anyway (FWD-6 arm G).
        meta.append("NAMING PLACE-NOTICE placement step skipped: org/mcp/naming-place.enforce is absent (NAMING_PLACE_PREVIEW=1 runs it)")
        return rows
    try:
        if _diff_repo() != REPO:
            return rows
        rcm = _rootcheck()
        by_root, order = {}, []
        for path in sorted(_PLACE["files"]):
            wants = [c for c in _PLACE["cands"] if c["path"] == path]
            if not path.startswith(PLACE_PATH_PREFIX) or (not wants and not path.endswith(".tf")):
                continue  # a root's files (its .tf folder, its Lambda folders) live under infra/aws/: nothing else pays the census
            root = rcm.root_of_path(path)
            if root is None:
                continue
            if root not in by_root:
                by_root[root] = []
                order.append(root)
            by_root[root] += wants
        post_texts = dict((p, t[1]) for p, t in _PLACE["files"].items())
        head_texts = dict((p, t[0] if t[0] is not None else "") for p, t in _PLACE["files"].items())
        index = dict(((r[1], r[2], r[3]), i) for i, r in enumerate(rows))
        extra = []
        if len(order) > PLACE_ROOT_CAP:
            meta.append("NAMING PLACE-NOTICE %d roots touched; the first %d were placed, these were NOT: %s"
                        % (len(order), PLACE_ROOT_CAP, ", ".join(order[PLACE_ROOT_CAP:])))
        for root in order[:PLACE_ROOT_CAP]:
            wants = [(c["value"], c["typ"], "%s:%d" % (c["path"], c["line"])) for c in by_root[root]]
            rr = rcm.place_root(root, PLACE_MAP, wants, post_texts, head_texts, ratchet=True)
            for c, res in zip(by_root[root], rr["results"]):
                k = (c["path"], c["line"], c["value"])
                if k in index:
                    rows[index[k]] = amend_row(rows[index[k]], res, on)
            if rr["mapped"] and rr["head_holes"] is not None and rr["post_holes"] > rr["head_holes"]:
                extra.append(ratchet_row(rr, on))
            elif not rr["mapped"] and rr["names_head"] is not None:
                meta.append("NAMING PLACE-NOTICE UNMAPPED %s names=%d (HEAD %d); an unmapped root is not ratcheted"
                            % (rr["root"], rr["names_post"], rr["names_head"]))
        return rows + extra
    except Exception as exc:  # the step never raises into the gate: it says so, and refuses only while the switch is present
        line = "NAMING PLACE ERROR the placement step could not run: %s: %s" % (type(exc).__name__, exc)
        meta.append(line)
        return rows + [("REFUSE", "<placement-step>", 0, "<error>", "-", line, "PLACE-REFUSE" if on else "WARN")]


# --------------------------------------------------------------------------- output
def _stamp():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def log_lines(lines, mode):
    try:
        os.makedirs(os.path.dirname(VERDICT_LOG), exist_ok=True)
        serial = os.environ.get("OPAL_AGENT_SERIAL", "unset")
        with open(VERDICT_LOG, "a", encoding="utf-8", newline="\n") as fh:
            for ln in lines:
                fh.write("%s %s %s %s\n" % (_stamp(), serial, mode, ln))
    except OSError as exc:
        print("WARN: naming-gate could not append to %s: %s" % (VERDICT_LOG, exc), file=sys.stderr)


def enforcing(flag):
    return bool(flag) or os.environ.get("NAMING_GATE_ENFORCE") == "1" or os.path.exists(ENFORCE_FILE)


def run(args):
    if not args.diff:
        raise GateError("no --diff FILE given")
    try:
        with open(args.diff, "rb") as fh:
            diff_text = text_of(fh.read())
    except OSError as exc:
        raise GateError("cannot read the diff %s: %s" % (args.diff, exc)) from None
    files = parse_diff(diff_text)
    try:
        mod = load_opal()
        refusals, _warnings = mod.validate()
    except GateError:
        raise
    except Exception as exc:
        raise GateError("lib/opal_naming.py or the registry cannot be loaded: %s: %s" % (type(exc).__name__, exc)) from None
    if refusals:
        where, field, reason = refusals[0]
        raise GateError("the registry is refused by validate (%d refusal(s)): %s.%s: %s"
                         % (len(refusals), where, field, reason))
    try:
        nm = Naming(mod)
    except GateError:
        raise
    except Exception as exc:
        raise GateError("lib/opal_naming.py or the registry cannot be loaded: %s: %s" % (type(exc).__name__, exc)) from None
    rows = []
    _place_reset()
    _RENAMES.clear()  # the renames of THIS index, read once for this run
    _live_reset(_live_read_plane)  # the live limb is on for a graded commit; self-test arms keep it off unless they inject a plane
    for f in files:
        rows += grade_file(nm, f, args.post_from_index)
    meta = domain_meta(files)
    rows = place_step(rows, meta)
    return rows, meta


def place_self_test():
    """The placement step's arms on plain data (no root check is run): what each answer of place() does to a row, the exit, the
    ratchet row and the switch. Prints one line per arm; returns True when all hold."""
    import tempfile
    fix = {"kind": "FIX", "detail": "irpt-x-daily", "form": "irpt-x-daily", "mapped": True, "owed": [],
           "fills": ['the cadence word "daily" is read from the schedule (b)']}
    hole = {"kind": "HOLE", "detail": "partial form {system}-x-lambda; could not fill {system}: no map entry for this root",
            "form": "{system}-x-lambda", "mapped": True, "fills": [],
            "owed": [("4.0.0_SA_CRO", "a root-map entry for the root a/b (infra/logic/registry/root_map.json)")]}
    right = {"kind": "RIGHT", "detail": "x", "form": None, "mapped": True, "fills": [], "owed": []}
    good_row = ("CONFORMANT", "f.tf", 3, "x", "x", "CONFORMANT as LAMBDA", "PASS")
    bad_row = ("REFUSE", "f.tf", 3, "x", "x-{cadence}", "NEW and OUT-OF-PATTERN as SCHEDULE: REFUSE", "REFUSE")
    on_fix, off_fix = amend_row(good_row, fix, True), amend_row(good_row, fix, False)
    on_hole = amend_row(good_row, hole, True)
    um = dict(hole, mapped=False)
    um_bad_off, um_good = amend_row(bad_row, um, False), amend_row(good_row, um, True)
    grew = {"root": "infra/aws/terraform/a/b", "post_holes": 2, "head_holes": 1,
            "new_holes": [("SCHEDULE", "s", "partial form s-{cadence}; could not fill {cadence}: minute field 0/7: not a single minute", "a/b/x.tf:1")]}
    saved = globals()["PLACE_FILE"]
    sw_on = sw_off = env_ignored = None
    try:
        with tempfile.TemporaryDirectory(prefix="naming_gate_selftest_") as td:
            globals()["PLACE_FILE"] = os.path.join(td, "switch")
            sw_off = not place_enforcing()
            with open(globals()["PLACE_FILE"], "w") as fh:
                fh.write("x")
            sw_on = place_enforcing()
            saved_env = os.environ.get("NAMING_PLACE_ENFORCE")
            os.environ["NAMING_PLACE_ENFORCE"] = "0"
            env_ignored = place_enforcing()
            if saved_env is None:
                del os.environ["NAMING_PLACE_ENFORCE"]
            else:
                os.environ["NAMING_PLACE_ENFORCE"] = saved_env
    finally:
        globals()["PLACE_FILE"] = saved
    arms = [
        ("FIX in a mapped root, switch present -> REFUSE, PLACE-REFUSE, names the form",
         on_fix[0] == "REFUSE" and on_fix[6] == "PLACE-REFUSE" and on_fix[4] == "irpt-x-daily" and "Owed: use irpt-x-daily" in on_fix[5]),
        ("the same, switch absent -> same text, counts WARN (verdict unchanged)",
         off_fix[6] == "WARN" and off_fix[4] == on_fix[4] and off_fix[5] == on_fix[5]),
        ("HOLE, switch present -> REFUSE naming the owner and the row owed",
         on_hole[6] == "PLACE-REFUSE" and "4.0.0_SA_CRO" in on_hole[5] and "root-map entry" in on_hole[5]),
        ("RIGHT -> the row is untouched", amend_row(good_row, right, True) == good_row),
        ("unmapped root, a name the matrix already refuses -> text added, counts REFUSE kept, switch absent",
         um_bad_off[6] == "REFUSE" and "4.0.0_SA_CRO" in um_bad_off[5]),
        ("unmapped root, a well-formed name -> untouched even with the switch present", um_good == good_row),
        ("exit: PLACE-REFUSE exits 1 without the older switch; a would-refuse WARN row and an old REFUSE row exit 0 without it",
         decide_exit([on_fix], False)[4] == 1 and decide_exit([off_fix], False)[4] == 0 and decide_exit([bad_row], False)[4] == 0
         and decide_exit([bad_row], True)[4] == 1 and decide_exit([good_row], False)[4] == 0),
        ("ratchet row: grown count -> REFUSE, PLACE-REFUSE present / WARN absent, names the new HOLE line and its owner",
         ratchet_row(grew, True)[6] == "PLACE-REFUSE" and ratchet_row(grew, False)[6] == "WARN"
         and "2 HOLE line(s) now, 1 at HEAD" in ratchet_row(grew, True)[5] and "minute field 0/7" in ratchet_row(grew, True)[5]),
        ("switch: absent file -> off, present file -> on, an environment value of 0 does not turn it off",
         sw_off is True and sw_on is True and env_ignored is True),
    ]
    ok = True
    for label, held in arms:
        ok = ok and bool(held)
        print("SELF-TEST place arm %s: %s" % (label, "ok" if held else "FAIL"))
    return ok


def override_self_test():
    """The override's arms on plain data in a temporary audit log: the audited id passes a placement row and is logged as
    OVERRIDDEN; no row, an empty reason, a row bound to a different message, an empty hash, a message with no override line, an
    uncovered name and the empty variable pass nothing (BF-y-2: no age window). True when all hold."""
    import tempfile
    now = datetime.datetime.now(datetime.timezone.utc)
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    new = now.strftime(fmt)
    msg_a = b"build(x): a\n\n# naming-place-override: the canon has no row yet\n"
    msg_b = b"build(x): b\n\n# naming-place-override: the canon has no row yet\n"
    msg_nol = b"build(x): c\n\nno override line here\n"

    def sha(raw):
        return hashlib.sha256(raw).hexdigest()

    rows = [("REFUSE", "f.tf", 3, "irpt-x-newjob", "irpt-x-newjob-daily", "owed", "PLACE-REFUSE"),
            ("REFUSE", "g.tf", 4, "other-name", "-", "owed", "PLACE-REFUSE")]
    def jrow(ident, reason, when, names=("irpt-x-newjob",), digest=None):
        return json.dumps({"utc": when, "author": "a <a@x>", "id": ident, "reason": reason, "names": list(names),
                           "msg_sha256": sha(msg_a) if digest is None else digest}, separators=(",", ":")) + "\n"

    with tempfile.TemporaryDirectory(prefix="naming_gate_override_selftest_") as td:
        audit = os.path.join(td, "audit.jsonl")
        with open(audit, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(jrow("good", "the canon has no row yet", new))
            fh.write(jrow("blank", "", new))
            fh.write(jrow("forged", "r", "2020-01-01T00:00:00Z", digest=sha(msg_b)))  # a valid-looking row for ANOTHER message
            fh.write(jrow("nohash", "r", new, digest=""))
            fh.write(jrow("nolinemsg", "r", new, digest=sha(msg_nol)))
        mfiles = {}
        for key, raw in (("a", msg_a), ("nol", msg_nol)):
            mfiles[key] = os.path.join(td, "msg_%s.txt" % key)
            with open(mfiles[key], "wb") as fh:
                fh.write(raw)
        good, _w = override_valid("good", audit, message_path=mfiles["a"])
        missing, why_missing = override_valid("handset", audit, message_path=mfiles["a"])
        blank, _w2 = override_valid("blank", audit, message_path=mfiles["a"])
        forged, why_forged = override_valid("forged", audit, message_path=mfiles["a"])
        nohash, _w3 = override_valid("nohash", audit, message_path=mfiles["a"])
        nolinemsg, why_noline = override_valid("nolinemsg", audit, message_path=mfiles["nol"])
        nomsg, _w3b = override_valid("good", audit)
        empty, _w4 = override_valid("", audit, message_path=mfiles["a"])
        nolog, _w5 = override_valid("good", os.path.join(td, "absent.jsonl"), message_path=mfiles["a"])
        # the index-read arm: a temporary repository; the row on disk only, then staged, then the disk copy edited
        repo = os.path.join(td, "repo")
        os.makedirs(os.path.join(repo, "org", "audit"))
        idx_ok = True
        try:
            subprocess.run(["git", "-C", repo, "init", "-q"], check=True, capture_output=True)
            disk_copy = os.path.join(repo, *OVERRIDE_AUDIT_REL.split("/"))
            with open(disk_copy, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(jrow("idx", "staged row", new))
            disk_only, why_disk = override_valid("idx", repo=repo, message_path=mfiles["a"])
            subprocess.run(["git", "-C", repo, "add", "-f", "--", OVERRIDE_AUDIT_REL], check=True, capture_output=True)
            staged, _w6 = override_valid("idx", repo=repo, message_path=mfiles["a"])
            with open(disk_copy, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(jrow("idx", "", new))  # disk now differs from the index: the index copy is the one honoured
            from_index, _w7 = override_valid("idx", repo=repo, message_path=mfiles["a"])
        except (OSError, subprocess.CalledProcessError):
            idx_ok = False
            disk_only, why_disk, staged, from_index = 0, "", None, None
    through = apply_override(rows, good or set())
    refused = apply_override(rows, set())
    arms = [
        ("an audited id: the row it names is OVERRIDDEN, exits 0 and is not refused; the row it does not name stays refused",
         through[0][0] == "OVERRIDDEN" and through[1][6] == "PLACE-REFUSE" and decide_exit(through[:1], False)[4] == 0
         and decide_exit(through[:1], False)[0] == "WARN" and decide_exit(through, False)[4] == 1),
        ("the same rows with no names (the difference control): both stay PLACE-REFUSE and exit 1",
         refused == rows and decide_exit(refused, False)[4] == 1),
        ("a variable set by hand (no audit row for its id) passes nothing", missing is None and "no audit row" in why_missing),
        ("an audit row with an empty reason passes nothing", blank is None),
        ("a FORGED row (valid-looking, the hash of another message, a different time) passes nothing",
         forged is None and "bound to a different message" in why_forged),
        ("a row with an empty hash, and a row with the right hash whose message has no override line, pass nothing",
         nohash is None and nolinemsg is None and "no non-empty" in why_noline),
        ("no message handed to the gate passes nothing, though the row is otherwise good", nomsg is None),
        ("an empty variable and a missing audit log pass nothing", empty is None and nolog is None),
        ("the index-read arm: a row on disk and not staged passes nothing; once staged it passes; a later disk edit does not "
         "change what the index holds", idx_ok and disk_only is None and "no staged copy" in why_disk
         and staged == {"irpt-x-newjob"} and from_index == {"irpt-x-newjob"}),
    ]
    ok = True
    for label, held in arms:
        ok = ok and bool(held)
        print("SELF-TEST override arm %s: %s" % (label, "ok" if held else "FAIL"))
    return ok


def built_self_test(nm):
    """The built-name arms (row LGIC_BLANKFIX-D1-W2-S9): an opal_name module block and a Python name() call with literal
    arguments are graded as the name they build; a site that is not all literals, or that name() refuses, prints
    BUILT-NOT-GRADED; a hand-typed literal beside them is graded exactly as before. Returns True when all hold."""
    want = "ir" + "pt-co" + "t-reporting-gold-scheduler-role"  # split: this file must not hand-type a firm token
    tf_ok = ('module "r" {\n  source = "../modules/opal_name"\n  system = "irpt"\n  scope = "cottonwood"\n'
             '  function = "reporting-gold"\n  kind = "role"\n  qualifier = "scheduler"\n}\n')
    tf_var = tf_ok.replace('scope = "cottonwood"', 'scope = var.firm')
    tf_reader = 'module "m" {\n  source = "../modules/opal_name"\n}\n'
    py_ok = 'ROLE = name("irpt", "cottonwood", "reporting-gold", "role", "scheduler")\n'
    py_kw = 'ROLE = opal_naming.name(system="irpt", scope="cottonwood", function="reporting-gold", kind="role", qualifier="scheduler")\n'
    py_var = 'ROLE = name("irpt", firm, "reporting-gold", "role", "scheduler")\n'
    py_bad = 'ROLE = name("irpt", "cottonwood", "reporting-gold", "no-such-kind")\n'
    py_typed = 'ROLE = "' + want + '"\n'  # the same name typed by hand keeps its firm token: graded as ever
    arms = (("tf-module-literal", "m.tf", tf_ok, "graded", want), ("py-call-literal", "m.py", py_ok, "graded", want),
            ("py-call-keywords", "m.py", py_kw, "graded", want), ("tf-module-var", "m.tf", tf_var, "not-graded", None),
            ("tf-registry-reader", "m.tf", tf_reader, "none", None), ("py-call-var", "m.py", py_var, "not-graded", None),
            ("py-call-refused", "m.py", py_bad, "not-graded", None), ("py-hand-typed-control", "m.py", py_typed, "typed", None))
    ok = True
    for label, path, src, expect, name_want in arms:
        added = set(range(1, src.count("\n") + 1))
        if expect == "typed":
            lits = py_literals(src, added)
            got = [judge(nm, path, x, None) for x in lits]
            arm = len(got) == 1 and got[0] is not None
            shown = "typed literal graded %s" % (got[0][0] if got and got[0] else None)
        else:
            rows = grade_built(nm, path, src, None, added, [], {})
            if expect == "graded":
                arm = len(rows) == 1 and rows[0][3] == name_want and rows[0][0] != "BUILT-NOT-GRADED"
            elif expect == "not-graded":
                arm = len(rows) == 1 and rows[0][0] == "BUILT-NOT-GRADED"
            else:
                arm = rows == []
            shown = ", ".join("%s %s" % (r[0], r[3] if r[0] != "BUILT-NOT-GRADED" else "(why printed)") for r in rows) or "no row"
        ok = ok and arm
        print("SELF-TEST arm built %s -> %s: %s" % (label, shown, "ok" if arm else "FAIL"))
    return ok


def pattern_self_test():
    """The PATTERN arm (row LGIC_ENFORCE-D1-W2-S152): a literal that is the key of a per-firm key ruling prints a PATTERN row that
    passes (never silent, never '0 graded'); place() saying something else WARNs; a literal that is no ruling's key is left alone."""
    key = "zz-sample/prefix"
    rulings = {key: {"key": key, "bucket_per": "firm", "bucket_from": "ZZ_SAMPLE_MAP", "canonical": "zz/{scope}/platinum/sample/"}}

    def ask(name, typ, root):
        return {"kind": "PATTERN", "detail": "a code pattern, not a name"}

    def other(name, typ, root):
        return {"kind": "FIX", "detail": "zz/x/", "form": "zz/x/"}

    got = _pattern_row(Lit(key, key, 3), rulings, ask)
    nope = _pattern_row(Lit("zz-sample/other", "zz-sample/other", 3), rulings, ask)
    warn = _pattern_row(Lit(key, key, 3), rulings, other)
    arms = (("pattern-line", got is not None and got[0] == "PATTERN" and got[3] == "PASS"),
            ("not-a-ruling-key", nope is None),
            ("other-kind-warns", warn is not None and warn[0] == "FIX" and warn[3] == "WARN"),
            ("summary-counts-it", decide_exit([(got[0], "f", 3, key, got[1], got[2], got[3])], False)[0] == "PASS"))
    ok = True
    for label, arm in arms:
        ok = ok and arm
        print("SELF-TEST arm pattern %s: %s" % (label, "ok" if arm else "FAIL"))
    return ok


def _added_diff(path, text):
    """A one-file unified diff of an ADDED file (`--- /dev/null`): the shape safe-commit's pathspec diff gives a rename destination."""
    body = text.rstrip("\n").split("\n")
    return "--- /dev/null\n+++ b/%s\n@@ -0,0 +1,%d @@\n%s" % (path, len(body), "".join("+%s\n" % ln for ln in body))


def _grade_added(nm, path, text, name):
    """The gate's rows for the literal `name` in the added file `path` (grade_file on a parsed diff; no git read, no network)."""
    f = parse_diff(_added_diff(path, text))[0]
    return [r for r in grade_file(nm, f, False) if r[3] == name]


def rename_self_test(nm):
    """The RENAME arm (LGIC_ENFORCE round 23, FWD-8 limb a). The destination of a staged rename is graded against its SOURCE's
    HEAD bytes, so a name it carries is EXISTING and is not refused; the same bytes staged as a COPY (no R row) stay NEW and
    are refused. The rename map and the HEAD read are replaced for the arm and restored after."""
    global _head_bytes
    name = "pipeline-chain"
    text = 'resource "aws_iam_policy" "probe" {\n  name = "%s"\n}\n' % name
    src = "infra/aws/terraform/zz-selftest/probe.tf.proposed"
    dst = "infra/aws/terraform/zz-selftest/probe.tf"
    copy = "infra/aws/terraform/zz-selftest/probe_copy.tf"
    saved_map, saved_head = dict(_RENAMES), _head_bytes
    try:
        _RENAMES.clear()
        _RENAMES["map"] = {dst: src}  # the index's one R row: src renamed to dst

        def _arm_head(repo, rel):  # HEAD holds the source with these bytes
            return text if rel == src else None

        _head_bytes = _arm_head
        renamed = _grade_added(nm, dst, text, name)
        copied = _grade_added(nm, copy, text, name)  # no R row names this path: a copy
    finally:
        _RENAMES.clear()
        _RENAMES.update(saved_map)
        _head_bytes = saved_head
        _place_reset()
    ok_rename = len(renamed) >= 1 and not any(r[6] == "REFUSE" for r in renamed)
    shown = ", ".join("%s %s" % (r[0], r[6]) for r in renamed) or "no row"
    print("SELF-TEST arm rename admitted: a staged rename graded against its source's HEAD bytes -> %s: %s"
          % (shown, "ok" if ok_rename else "FAIL"))
    ok_copy = len(copied) >= 1 and all(r[6] == "REFUSE" for r in copied)
    shown = ", ".join("%s %s" % (r[0], r[6]) for r in copied) or "no row"
    print("SELF-TEST arm rename copy control: the same bytes staged as a copy (no R row) -> %s: %s"
          % (shown, "ok" if ok_copy else "FAIL"))
    return ok_rename and ok_copy


def adopt_self_test(nm):
    """The ADOPT arm (LGIC_ENFORCE round 23, FWD-8 limb b). A NEW name the census LIVE plane holds is EXISTING: admitted, with
    RUNNING-LIVE, the node type and the vintage in its why text. A name the plane does not hold is refused as NEW, as today. A
    read that raises, or prints no vintage, is refused with LIVE-READ-FAILED and never RUNNING-LIVE. The plane is replaced
    for each arm (no network) and restored after."""
    name = "pipeline-chain"
    path = "infra/aws/terraform/zz-selftest/adopt.tf"
    text = 'resource "aws_iam_policy" "probe" {\n  name = "%s"\n}\n' % name
    vint = "2026-10-10 00:00:00 UTC (self-test stub)"

    def plane(nodes, vintage=vint):
        return lambda _nm: (nodes, vintage, "self-test stub")

    def unreadable(_nm):
        raise OSError("self-test stub: the live read cannot run\nsecond line")

    held_plane = plane([{"type": "IAM_POLICY", "name": name, "arn": ""}])
    other_plane = plane([{"type": "IAM_ROLE", "name": "self-test-other", "arn": ""}])
    unread_plane = plane([{"type": "IAM_POLICY", "name": name, "arn": ""}], "UNREAD")
    wrong_plane = plane([{"type": "EC2_INSTANCE", "name": name, "arn": ""}])
    saved = dict(_LIVE)
    try:
        _live_reset(held_plane)
        held = _grade_added(nm, path, text, name)
        _live_reset(other_plane)
        absent = _grade_added(nm, path, text, name)
        _live_reset(unreadable)
        failed = _grade_added(nm, path, text, name)
        _live_reset(unread_plane)
        undated = _grade_added(nm, path, text, name)
        _live_reset(wrong_plane)
        wrong = _grade_added(nm, path, text, name)
    finally:
        _LIVE.clear()
        _LIVE.update(saved)
        _place_reset()
    def has(rows, token):  # the token sits in one of the rows' why text
        return any(token in r[5] for r in rows)

    ok_held = (len(held) >= 1 and not any(r[6] == "REFUSE" for r in held)
               and has(held, "RUNNING-LIVE IAM_POLICY '%s' read from the live plane, %s" % (name, vint))
               and not has(held, "LIVE-READ-FAILED"))
    print("SELF-TEST arm adopt held: the plane holds %s as IAM_POLICY -> %s: %s"
          % (name, ", ".join("%s %s" % (r[0], r[6]) for r in held) or "no row", "ok" if ok_held else "FAIL"))
    ok_absent = (len(absent) >= 1 and all(r[6] == "REFUSE" for r in absent) and has(absent, "NEW and")
                 and not has(absent, "RUNNING-LIVE") and not has(absent, "LIVE-READ-FAILED"))
    print("SELF-TEST arm adopt absent control: a name the plane does not hold -> %s: %s"
          % (", ".join("%s %s" % (r[0], r[6]) for r in absent) or "no row", "ok" if ok_absent else "FAIL"))
    ok_failed = (len(failed) >= 1 and all(r[6] == "REFUSE" for r in failed) and has(failed, "LIVE-READ-FAILED")
                 and not has(failed, "RUNNING-LIVE"))
    print("SELF-TEST arm adopt read-failed control: the read raises -> %s: %s"
          % (", ".join("%s %s" % (r[0], r[6]) for r in failed) or "no row", "ok" if ok_failed else "FAIL"))
    ok_undated = (len(undated) >= 1 and all(r[6] == "REFUSE" for r in undated) and has(undated, "LIVE-READ-FAILED")
                  and not has(undated, "RUNNING-LIVE"))
    print("SELF-TEST arm adopt vintage-unreadable control: the read prints UNREAD -> %s: %s"
          % (", ".join("%s %s" % (r[0], r[6]) for r in undated) or "no row", "ok" if ok_undated else "FAIL"))
    ok_wrong = (len(wrong) >= 1 and all(r[6] == "REFUSE" for r in wrong) and has(wrong, "NEW and")
                and not has(wrong, "RUNNING-LIVE") and not has(wrong, "LIVE-READ-FAILED"))
    print("SELF-TEST arm adopt wrong-type control: the plane holds the name only as EC2_INSTANCE -> %s: %s"
          % (", ".join("%s %s" % (r[0], r[6]) for r in wrong) or "no row", "ok" if ok_wrong else "FAIL"))
    return ok_held and ok_absent and ok_failed and ok_undated and ok_wrong


def test_folder_self_test(nm):
    """The TEST-FOLDER arm (CT-ab-9). A fixture under a FIXTURE_DIRS folder (`test/`) is not graded; the same bytes under a
    folder that merely contains the letters (`latest/`) are graded, so the exemption is whole-segment, never a substring."""
    name = "pipeline-chain"
    text = 'resource "aws_iam_policy" "probe" {\n  name = "%s"\n}\n' % name
    exempt = _grade_added(nm, "infra/x/test/fixture.tf", text, name)
    graded = _grade_added(nm, "infra/latest/fixture.tf", text, name)
    ok_exempt = len(exempt) == 0
    print("SELF-TEST arm test-folder: a firm-token fixture under infra/x/test/fixture.tf is not graded -> %s: %s"
          % ("no row" if ok_exempt else ", ".join("%s %s" % (r[0], r[6]) for r in exempt), "ok" if ok_exempt else "FAIL"))
    ok_graded = len(graded) >= 1 and any(r[6] == "REFUSE" for r in graded)
    print("SELF-TEST arm test-folder control: the same token under infra/latest/fixture.tf IS graded (latest/ is not a test folder) -> %s: %s"
          % (", ".join("%s %s" % (r[0], r[6]) for r in graded) or "no row", "ok" if ok_graded else "FAIL"))
    return ok_exempt and ok_graded


def self_test():
    """--self-test: judge() on a NEW group-A name takes the fourth verdict and passes, and (the difference control) a NEW
    group-B name is still refused. Reads no diff, writes no log. Returns 0 when both arms hold."""
    nm = Naming(load_opal())
    ok = True
    for name, typ, want_verdict, want_counts in (("s3-access", "IAM_POLICY", "NO-SYSTEM-ASKED", "PASS"),
                                                  ("pipeline-chain", "IAM_POLICY", "REFUSE", "REFUSE")):
        got = judge(nm, "selftest.tf", Lit(name, name, 1, typ), None)
        arm = got is not None and got[0] == want_verdict and got[3] == want_counts
        ok = ok and arm
        print("SELF-TEST arm %s %s -> %s %s: %s" % (name, typ, got[0] if got else None, got[3] if got else None,
                                                    "ok" if arm else "FAIL"))
    ok = built_self_test(nm) and ok
    ok = pattern_self_test() and ok
    ok = place_self_test() and ok
    ok = override_self_test() and ok
    ok = rename_self_test(nm) and ok
    ok = adopt_self_test(nm) and ok
    ok = test_folder_self_test(nm) and ok
    print("NAMING-GATE-SELF-TEST: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(prog="naming-gate.py", description="the naming commit limb (LGIC_ENFORCE DEC-6)")
    ap.add_argument("--self-test", action="store_true", help="run the gate's own arms (the fourth verdict and its control)")
    ap.add_argument("--diff", help="a unified diff; its ADDED lines are graded")
    ap.add_argument("--enforce", action="store_true", help="a REFUSE exits 1 (also NAMING_GATE_ENFORCE=1 or org/mcp/naming-gate.enforce)")
    ap.add_argument("--post-from-index", action="store_true", help="read each post-image from the index (safe-commit.sh)")
    ap.add_argument("--message-file", help="the exact commit message safe-commit.sh will commit; the placement override passes only a "
                    "staged audit row whose msg_sha256 is this file's sha256 (BF-y-2)")
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    enforce = enforcing(args.enforce)
    mode = "ENFORCE" if enforce else "WARN"
    try:
        rows, meta = run(args)
    except Exception as exc:
        line = "NAMING ERROR %s" % (str(exc) if isinstance(exc, GateError) else "%s: %s" % (type(exc).__name__, exc))
        print(line)
        log_lines([line], mode)
        if not enforce:
            print("  (WARN window: the limb's own error never blocks a commit; enforce is off)")
        return 1 if enforce else 0
    ident = os.environ.get("NAMING_PLACE_OVERRIDE", "")
    if ident and any(r[6] == "PLACE-REFUSE" for r in rows):
        names, why = override_valid(ident, message_path=args.message_file)
        if names is None:
            meta.append("NAMING-PLACE-OVERRIDE: IGNORED %s" % why)
        else:
            rows = apply_override(rows, names)
    for ln in meta:
        print(ln)
    rows.sort(key=lambda r: (r[1], r[2], r[3]))
    verdict_lines = list(meta)
    for verdict, path, line, s, canon, why, _counts in rows:
        if verdict == "BUILT-NOT-GRADED":
            vl = "NAMING BUILT-NOT-GRADED %s:%d %s" % (path, line, s)
        else:
            vl = "NAMING %s %s:%d %s -> %s" % (verdict, path, line, s, canon)
        verdict_lines.append(vl)
        print(vl)
        print("  why: %s" % why)
    summary, refused, warned, place_ref, rc = decide_exit(rows, enforce)
    if refused and not enforce:
        print("  (WARN window: %d REFUSE verdict(s) did not block; ENFORCE is --enforce, NAMING_GATE_ENFORCE=1 or"
              " org/mcp/naming-gate.enforce)" % refused)
    would = sum(1 for r in rows if r[0] == "REFUSE" and r[6] == "WARN")
    if would:
        print("  (placement step: %d would-refuse verdict(s) did not block; the step refuses while org/mcp/naming-place.enforce"
              " exists, and that switch is absent)" % would)
    if place_ref:
        # The placement step's own refusal, told apart from the older limb's REFUSE: safe-commit.sh blocks on this line while
        # org/mcp/naming-place.enforce is present, whatever naming-gate.enforce says (LGIC_BLANKFIX BF-x-3, row W1-S19).
        pline = "NAMING-PLACE: REFUSE %d" % place_ref
        print(pline)
        verdict_lines.append(pline)
    last = "NAMING-GATE: %s %d graded" % (summary, len(rows))
    print(last)
    log_lines(verdict_lines + [last], mode)
    return rc


if __name__ == "__main__":
    sys.exit(main())
