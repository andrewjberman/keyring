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
tokens as whole segments. File types: .py .js .mjs .ts .tf .json .yaml .yml.

Usage:
    python .tools/naming-gate.py --diff FILE [--enforce] [--post-from-index]

ENFORCE is on with --enforce, env NAMING_GATE_ENFORCE=1, or a present org/mcp/naming-gate.enforce: a REFUSE
then exits 1. Otherwise it is WARN mode and exits 0, on an internal error too (`NAMING ERROR <reason>`).
--post-from-index reads each file's post-image from the index (git show :<path>), as safe-commit.sh does;
without it the post-image is the pre-image with the diff's hunks applied.

Output: one `NAMING <verdict> <file>:<line> <string> -> <canonical>` line per graded string (<verdict> is the
grade, RAISE, or REFUSE), an indented `why:` line under each, then `NAMING-GATE: <PASS|WARN|REFUSE> <n> graded`.
Every verdict line is appended to org/mcp/naming-gate-verdicts.log (runtime state; gitignored; never committed).

Standard library only. ASCII only.
"""
from __future__ import annotations

import argparse
import ast
import datetime
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
ENFORCE_FILE = os.path.join(REPO, "org", "mcp", "naming-gate.enforce")
VERDICT_LOG = os.path.join(REPO, "org", "mcp", "naming-gate-verdicts.log")
REGISTRY_PREFIX = "infra/logic/registry/"
GRADED_EXT = (".py", ".js", ".mjs", ".ts", ".tf", ".json", ".yaml", ".yml")
BUILDERS = {"key", "address", "name", "lookup"}
NAMING_MODULE_NAMES = {"opal_naming"}
# A call whose string argument is a numeric spelling, never a name: float("inf") is not the firm inf.
EXEMPT_CALLS = {"float"}
CLOSED_STATUSES = {"closed", "complete", "completed", "cancelled", "canceled", "superseded", "retired", "archived"}

# Terraform resource type -> (node type, own-name attribute path). The same reading as the EN-t-1 census
# (deliverables/0.9.0_WK_LGIC_ENFORCE~3/instrument/census.py TF_NODE), restricted to the graded types.
TF_NODE = {
    "aws_lambda_function": ("LAMBDA", "function_name"),
    "aws_iam_role": ("IAM_ROLE", "name"),
    "aws_iam_policy": ("IAM_POLICY", "name"),
    "aws_iam_role_policy": ("IAM_POLICY", "name"),
    "aws_iam_user_policy": ("IAM_POLICY", "name"),
    "aws_iam_instance_profile": ("INSTANCE_PROFILE", "name"),
    "aws_security_group": ("SECURITY_GROUP", "name"),
    "aws_api_gateway_rest_api": ("API_GW", "name"),
    "aws_apigatewayv2_api": ("API_GW", "name"),
    "aws_dynamodb_table": ("DYNAMODB_TABLE", "name"),
    "aws_sqs_queue": ("SQS_QUEUE", "name"),
    "aws_sns_topic": ("SNS_TOPIC", "name"),
    "aws_cloudwatch_metric_alarm": ("CW_ALARM", "alarm_name"),
    "aws_lambda_layer_version": ("LAMBDA_LAYER", "layer_name"),
    "aws_instance": ("EC2_INSTANCE", "tags.Name"),
    "aws_codebuild_project": ("CODEBUILD_PROJECT", "name"),
    "aws_ssm_document": ("SSM_DOCUMENT", "name"),
    "aws_ecs_task_definition": ("ECS_TASK_DEFINITION", "family"),
    "aws_sfn_state_machine": ("STATE_MACHINE", "name"),
    "aws_lb": ("LOAD_BALANCER", "name"),
    "aws_ecs_cluster": ("ECS_CLUSTER", "name"),
    "aws_cloudwatch_event_rule": ("EVENT_RULE", "name"),
    "aws_scheduler_schedule": ("SCHEDULE", "name"),
    "aws_cloudwatch_log_group": ("LOG_GROUP", "name"),
    "aws_s3_bucket": ("S3_BUCKET", "bucket"),
    "aws_s3_bucket_policy": ("S3_BUCKET_POLICY", "bucket"),
    "aws_s3_object": ("S3Key", "key"),
    "aws_secretsmanager_secret": ("SECRET", "name"),
}

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


# --------------------------------------------------------------------------- the matrix
def judge(nm, path, lit, pre_text):
    """(line verdict, canonical, why, counts-as) for one literal, or None when it is not graded."""
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
        return "REFUSE", canon, ("EXISTING and OUT-OF-PATTERN as %s in a surface remediations.json assigns to the live"
                                 " remediation %s: REFUSE unless the diff removes it%s" % (typ, rem, carr_txt)), "REFUSE"
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
        lits = json_literals(added)
    else:
        lits = yaml_literals(added)
    seen = set()
    for lit in lits:
        if lit.permitted or any(lo <= lit.line <= hi for lo, hi in gen_ranges):
            continue
        if (lit.line, lit.value) in seen:
            continue
        seen.add((lit.line, lit.value))
        j = judge(nm, path, lit, pre_text)
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
        nm = Naming(load_opal())
    except GateError:
        raise
    except Exception as exc:
        raise GateError("lib/opal_naming.py or the registry cannot be loaded: %s: %s" % (type(exc).__name__, exc)) from None
    rows = []
    for f in files:
        rows += grade_file(nm, f, args.post_from_index)
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(prog="naming-gate.py", description="the naming commit limb (LGIC_ENFORCE DEC-6)")
    ap.add_argument("--diff", help="a unified diff; its ADDED lines are graded")
    ap.add_argument("--enforce", action="store_true", help="a REFUSE exits 1 (also NAMING_GATE_ENFORCE=1 or org/mcp/naming-gate.enforce)")
    ap.add_argument("--post-from-index", action="store_true", help="read each post-image from the index (safe-commit.sh)")
    args = ap.parse_args(argv)
    enforce = enforcing(args.enforce)
    mode = "ENFORCE" if enforce else "WARN"
    try:
        rows = run(args)
    except Exception as exc:
        line = "NAMING ERROR %s" % (str(exc) if isinstance(exc, GateError) else "%s: %s" % (type(exc).__name__, exc))
        print(line)
        log_lines([line], mode)
        if not enforce:
            print("  (WARN window: the limb's own error never blocks a commit; enforce is off)")
        return 1 if enforce else 0
    rows.sort(key=lambda r: (r[1], r[2], r[3]))
    verdict_lines = []
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
