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
comments, Terraform block labels, and anything under */tests/* (the generated-file check still runs there).

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
REGISTRY_PREFIX = "infra/logic/registry/"
GRADED_EXT = (".py", ".js", ".mjs", ".ts", ".tf", ".json", ".yaml", ".yml")
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
    __slots__ = ("value", "raw", "line", "hint", "permitted", "label", "block")

    def __init__(self, value, raw, line, hint=None):
        self.value, self.raw, self.line, self.hint = value, raw, line, hint
        self.permitted, self.label, self.block = False, False, None


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


def js_literals(src, added):
    return [Lit(v, r, ln) for kind, v, r, ln in scan(src, "js") if kind == "str" and ln in added]


def tf_literals(src, added):
    """Terraform string literals on added lines, each with its block context: a label is marked, a string in a
    module block whose source is the opal_name module is permitted, and a resource's own-name attribute gives
    the node type as the hint."""
    toks = scan(src, "tf")
    blocks, stmt, attr, bracket, out = [], [], None, 0, []
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
        stmt.append(("lit", lit))
        inner = blocks[-1] if blocks else None
        if inner and inner.get("block") and inner.get("kind") == "module" and attr == "source" and "opal_name" in v:
            inner["opal"] = True
        lit.hint = _tf_hint(blocks, attr)
        if ln in added:
            out.append(lit)
    for lit in out:
        if any(b.get("block") and b.get("kind") == "module" and b.get("opal") for b in lit.block):
            lit.permitted = True
    return [lit for lit in out if not lit.label]


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


def waivers_for(path, post_text, now=None):
    """{literal: (entry, note)} for this file: the waivers that are IN FORCE and RECOGNIZED here."""
    now = now or datetime.datetime.now(datetime.timezone.utc)
    good, bad = load_legacy_reads()
    out, denied = {}, {}
    for raw, reason in bad:
        if isinstance(raw, dict) and raw.get("file") == path and isinstance(raw.get("literal"), str):
            denied[raw["literal"]] = reason
    for entry in good:
        if entry["file"] != path:
            continue
        if _expired(entry, now):
            denied[entry["literal"]] = "expired: cutoff %s inclusive UTC" % entry.get("as_of_cutoff")
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
def judge(nm, path, lit, pre_text, waivers=None):
    """(line verdict, canonical, why, counts-as) for one literal, or None when it is not graded."""
    if _resolves_to_tracked(lit.value):
        return None  # a value resolving to a tracked path at HEAD is a CITATION (R-11), not a mint
    typ, graded_as = nm.classify(lit.value, lit.hint)
    carr = nm.carrier(lit.value)
    if typ is None and carr is None:
        return None
    new = pre_text is None or not _in_pre(lit, pre_text)
    carr_txt = ""
    if carr:
        carr_txt = "; hand-kept carrier of %r outside every permitted context: read it through lookup(%r)" % (carr[0], carr[1])
    if typ is None:
        canon = "lookup(%r)" % carr[1]
        if new:
            return "REFUSE", canon, "NEW hand-kept carrier (context rule)%s" % carr_txt, "REFUSE"
        return "OUT-OF-PATTERN", canon, "EXISTING hand-kept carrier (context rule): WARN%s" % carr_txt, "WARN"
    verdict, canon, defect = nm.grade(typ, graded_as)
    if verdict == "RAISE":
        why = "RAISE as %s: rule or registry defect, not a refusal: %s" % (typ, defect)
        if new and carr:
            return "REFUSE", "lookup(%r)" % carr[1], why + carr_txt, "REFUSE"
        return "RAISE", "(rule or registry defect)", why + carr_txt, "WARN"
    if verdict == "NOT-GRADED":
        return "NOT-GRADED", "-", "%s is outside the grade's domain (G1.2)" % typ, "PASS"
    rem = nm.remediation_of(typ, graded_as) if verdict == "OUT-OF-PATTERN" and not new else None
    if new and verdict in ("OUT-OF-PATTERN", "ALIAS"):
        return "REFUSE", canon, "NEW and %s as %s: REFUSE%s" % (verdict, typ, carr_txt), "REFUSE"
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
    if f["old"] is not None:
        rc, out, _err = git("show", "HEAD:%s" % f["old"])
        if rc == 0:
            pre_text = text_of(out)
        elif os.path.isfile(os.path.join(REPO, *f["old"].split("/"))):
            with open(os.path.join(REPO, *f["old"].split("/")), "rb") as fh:
                pre_text = text_of(fh.read())
    post_lines, added = apply_hunks(pre_text or "", f["hunks"])
    if not added:
        return []
    post_text = "\n".join(post_lines) + "\n"
    if post_from_index:
        rc, out, _err = git("show", ":%s" % path)
        if rc == 0:
            post_text = text_of(out)
            post_lines = post_text.split("\n")
            if post_lines and post_lines[-1] == "":
                post_lines.pop()
    first_added = min(added)
    rows = []

    # the generated-file check: before every exclusion, so a generated file under */tests/* is checked too
    marked = bool(nm.mark_re.search(post_text)) or bool(pre_text and nm.mark_re.search(pre_text))
    gen_ranges = []
    if marked:
        tag = "<generated-file-edit>"
        if path not in nm.targets:
            return [("REFUSE", path, first_added, tag,
                     "not produced by lib/opal_naming.py generate (known targets: %d)" % len(nm.targets),
                     "the file carries the GENERATED mark but the generator does not produce it", "REFUSE")]
        try:
            expected = generator_output(nm, path, post_text)
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
    if "/tests/" in "/" + path:
        return rows  # fixtures under */tests/* are not graded
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
    else:
        lits = yaml_literals(added)
    waivers = waivers_for(path, post_text) if path.endswith(".py") else {}
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
    return rows


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
    for f in files:
        rows += grade_file(nm, f, args.post_from_index)
    return rows, domain_meta(files)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="naming-gate.py", description="the naming commit limb (LGIC_ENFORCE DEC-6)")
    ap.add_argument("--diff", help="a unified diff; its ADDED lines are graded")
    ap.add_argument("--enforce", action="store_true", help="a REFUSE exits 1 (also NAMING_GATE_ENFORCE=1 or org/mcp/naming-gate.enforce)")
    ap.add_argument("--post-from-index", action="store_true", help="read each post-image from the index (safe-commit.sh)")
    args = ap.parse_args(argv)
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
    for ln in meta:
        print(ln)
    rows.sort(key=lambda r: (r[1], r[2], r[3]))
    verdict_lines = list(meta)
    for verdict, path, line, s, canon, why, _counts in rows:
        vl = "NAMING %s %s:%d %s -> %s" % (verdict, path, line, s, canon)
        verdict_lines.append(vl)
        print(vl)
        print("  why: %s" % why)
    refused = sum(1 for r in rows if r[6] == "REFUSE")
    warned = sum(1 for r in rows if r[6] == "WARN")
    if refused and enforce:
        summary = "REFUSE"
    elif refused or warned:
        summary = "WARN"
    else:
        summary = "PASS"
    if refused and not enforce:
        print("  (WARN window: %d REFUSE verdict(s) did not block; ENFORCE is --enforce, NAMING_GATE_ENFORCE=1 or"
              " org/mcp/naming-gate.enforce)" % refused)
    last = "NAMING-GATE: %s %d graded" % (summary, len(rows))
    print(last)
    log_lines(verdict_lines + [last], mode)
    return 1 if (refused and enforce) else 0


if __name__ == "__main__":
    sys.exit(main())
