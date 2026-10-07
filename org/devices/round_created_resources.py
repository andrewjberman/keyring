"""round_created_resources.py -- the round-close read (NFRA_CTLPLN PRD v0.14 C-NAMING, cell CT-d-7, AMENDMENT 1).

One read at a round's close: every Terraform resource a range of commits CREATED, each read two ways, N of N
printed. A read at the drain, not a standing checker; no AWS call (the cloud-graph arm reads the estate's served
graph database through comp-find, which changes nothing).

    python org/devices/round_created_resources.py --since <commit> --until <commit> [--root <dir> ...]
        [--registry <file>] [--repo <dir>] [--graph-tool <script>]

For each Terraform root (default: every directory directly under infra/aws/terraform/ with a .tf file changed
between the two commits; --root narrows it) the resource addresses at --until that were not there at --since are
listed. Terraform is read ONLY from `git show <commit>:<file>` (the root's top-level *.tf files), never from the
working tree, so the answer does not depend on what is checked out. The registry file is read from disk.

A name resolves from: a string literal; "${...}" over each.key / each.value / local.X; local.X; and
module.<m>[each.key].name / module.<m>.name for a call of modules/opal_name, formatted as the module formats
(system, -scope SHORT, -function, -qualifier, -kind, .fifo) and cross-checked against lib/opal_naming.py name():
a difference makes the name UNRESOLVED. A for_each over a literal set/list/map literal (or a local holding one)
expands to one address per key.

Each created resource is NAMELESS (a kind with no name of its own: an attachment, a membership, an association),
UNRESOLVED (its name does not resolve as above, or the registry's reader cannot place it: counted, fails ok, never
guessed), or a NAMED resource, which gets two reads.

REGISTRY ARM -- resources.json is not a list of resources: it holds only names whose own tokens resolve no system.
The reader is lib/opal_naming.py's own, called as validate() calls it (_res_tokens then _slots over the name's body,
the .fifo affix removed for an SQS_QUEUE):
    REGISTERED      a row of the --registry file carries that exact name
    SELF-RESOLVING  no row, and the name's own tokens resolve a system: no row is expected and validate() refuses one
    ROW-NEEDED      no row, and the tokens leave the {system} placeholder: a row is owed
The validator's own count line (`python lib/opal_naming.py validate`, last line) is printed once.

CLOUD-GRAPH ARM -- `comp-find --corpus aws '<name>' --all` (the served graph; denominator = nodes scanned, vintage =
the graph's own built line). A node counts as FOUND only when the exact name (optionally with a .fifo suffix, on a
name boundary) is inside the NODE'S NAME or ARN; a hit that matches only in a node's properties is not a node of
that resource and is printed as not counted. Per resource:
    NODE                 found: node_type and drift_class printed
    NO-NODE              measured zero (DEFERRED 0, every hit parsed) and the graph is NOT older than the commit
    NO-NODE-GRAPH-OLDER  measured zero, and the graph's built time is EARLIER than the committer time of the commit
                         in range that first declares the resource (both times printed): not a defect of the resource
    GRAPH-UNREAD         the call failed, timed out, was deferred, or its hits could not all be parsed: counted,
                         never read as NO-NODE

LAST line:
    ROUND-RESOURCES since=<c1> until=<c2> roots=<r,..> created=<n> nameless=<a> named=<m> self_resolving=<s>
        registered=<g> row_needed=<x> unresolved=<u> graph_unread=<w> graph_nodes=<k> no_node=<z>
        no_node_graph_older=<o> graph_built=<vintage> ok=<True|False>
(graph_unread sits beside unresolved so that the CT4d7-AC2 expectation `unresolved=0 graph_unread=0` is one contiguous string)
created = nameless + named + unresolved; named = self_resolving + registered + row_needed = graph_nodes + no_node +
no_node_graph_older + graph_unread (the four graph results are disjoint); ok only when row_needed == 0,
unresolved == 0 and graph_unread == 0.

BLIND: a resource created outside Terraform (console, CLI) is invisible to this read.
"""
from __future__ import annotations

import argparse
import calendar
import importlib.util
import json
import os
import re
import subprocess
import sys
import time

TF_BASE = "infra/aws/terraform"
HERE = os.path.dirname(os.path.abspath(__file__))
SELF_REPO = os.path.dirname(os.path.dirname(HERE))
MODULE_REL = TF_BASE + "/modules/opal_name"

# kind -> attribute that carries the resource's own name. Mirrors org/standards/NAMING_SCHEMA.json tf_type_map and
# tf_unmapped_own_name for the common kinds, plus aws_iam_group (IAM_GROUP), which that map lacks.
NAME_ATTR = {
    "aws_lambda_function": "function_name", "aws_iam_role": "name", "aws_iam_policy": "name",
    "aws_iam_role_policy": "name", "aws_iam_user_policy": "name", "aws_iam_instance_profile": "name",
    "aws_iam_user": "name", "aws_iam_group": "name", "aws_security_group": "name",
    "aws_api_gateway_rest_api": "name", "aws_apigatewayv2_api": "name", "aws_dynamodb_table": "name",
    "aws_sqs_queue": "name", "aws_sns_topic": "name", "aws_cloudwatch_metric_alarm": "alarm_name",
    "aws_lambda_layer_version": "layer_name", "aws_codebuild_project": "name", "aws_ssm_document": "name",
    "aws_ecs_task_definition": "family", "aws_sfn_state_machine": "name", "aws_lb": "name",
    "aws_ecs_cluster": "name", "aws_cloudwatch_event_rule": "name", "aws_scheduler_schedule": "name",
    "aws_cloudwatch_log_group": "name", "aws_s3_bucket": "bucket", "aws_secretsmanager_secret": "name",
    "aws_dynamodb_table_item": None,
}
OTHER_ATTRS = ("name", "function_name", "bucket", "queue_name", "table_name")
NAMELESS_KIND_RE = re.compile(r"(_attachment|_membership|_association)$")


def git(repo, *args):
    p = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True, encoding="utf-8", errors="replace")
    return p.returncode, p.stdout


def git_show(repo, commit, path):
    rc, out = git(repo, "show", "%s:%s" % (commit, path))
    return out if rc == 0 else None


# ---------------------------------------------------------------- HCL reading (the small subset these roots use)

def strip_comments(text):
    out, i, n, in_str = [], 0, len(text), False
    while i < n:
        ch = text[i]
        if in_str:
            out.append(ch)
            if ch == "\\" and i + 1 < n:
                out.append(text[i + 1])
                i += 2
                continue
            if ch == '"':
                in_str = False
            i += 1
            continue
        if ch == '"':
            in_str = True
            out.append(ch)
        elif ch == "#" or text.startswith("//", i):
            while i < n and text[i] != "\n":
                i += 1
            continue
        elif text.startswith("/*", i):
            j = text.find("*/", i + 2)
            i = n if j < 0 else j + 2
            continue
        else:
            out.append(ch)
        i += 1
    return "".join(out)


def match_brace(text, start):
    """text[start] == '{'; return the index of its matching '}' (string aware), or -1."""
    depth, i, n, in_str = 0, start, len(text), False
    while i < n:
        ch = text[i]
        if in_str:
            if ch == "\\":
                i += 2
                continue
            if ch == '"':
                in_str = False
        elif ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


BLOCK_RE = re.compile(r'^[ \t]*(resource|module|locals)\b[ \t]*((?:"[^"]*"[ \t]*)*)\{', re.M)


def parse_blocks(text):
    """-> list of (kind, labels, line, body) for each top-level resource/module/locals block."""
    text = strip_comments(text)
    blocks, pos = [], 0
    while True:
        m = BLOCK_RE.search(text, pos)
        if not m:
            break
        open_at = m.end() - 1
        close = match_brace(text, open_at)
        if close < 0:
            break
        labels = re.findall(r'"([^"]*)"', m.group(2))
        blocks.append((m.group(1), labels, text.count("\n", 0, m.start()) + 1, text[open_at + 1:close]))
        pos = close + 1
    return blocks


def top_attrs(body):
    """Top-level `name = expr` statements of a block body -> {name: expr text}."""
    attrs, i, n = {}, 0, len(body)
    while i < n:
        j = body.find("\n", i)
        line_end = n if j < 0 else j
        line = body[i:line_end]
        m = re.match(r"^\s*([A-Za-z_][\w-]*)\s*=(?!=)\s*(.*)$", line)
        if m:
            key, expr_start = m.group(1), i + m.start(2)
            depth, k, in_str = 0, expr_start, False
            while k < n:
                ch = body[k]
                if in_str:
                    if ch == "\\":
                        k += 2
                        continue
                    if ch == '"':
                        in_str = False
                elif ch == '"':
                    in_str = True
                elif ch in "{[(":
                    depth += 1
                elif ch in "}])":
                    depth -= 1
                elif ch == "\n" and depth <= 0:
                    break
                k += 1
            attrs[key] = body[expr_start:k].strip()
            i = k + 1
            continue
        if "{" in line:  # a nested block: skip it whole
            open_at = body.find("{", i)
            close = match_brace(body, open_at)
            i = n if close < 0 else close + 1
            continue
        i = line_end + 1
    return attrs


def string_literal(expr):
    m = re.fullmatch(r'"((?:[^"\\]|\\.)*)"', expr.strip())
    return m.group(1) if m else None


def literal_keys(expr):
    """Keys of a for_each literal: toset([...]) / [...] of strings, or a {k = v} map. None if not a literal."""
    e = expr.strip()
    m = re.fullmatch(r"toset\((.*)\)", e, re.S)
    if m:
        e = m.group(1).strip()
    if e.startswith("[") and e.endswith("]"):
        items = re.findall(r'"((?:[^"\\]|\\.)*)"', e)
        stripped = re.sub(r'"(?:[^"\\]|\\.)*"|[\s,\[\]]', "", e)
        return items if not stripped else None
    if e.startswith("{") and e.endswith("}"):
        keys = list(top_attrs(e[1:-1]).keys())
        keys += [k for k in re.findall(r'^\s*"([^"]+)"\s*=', e[1:-1], re.M)]
        return keys or None
    return None


class Root:
    """One Terraform root at one commit: its resources, locals and module calls."""

    def __init__(self, repo, commit, rel):
        self.repo, self.commit, self.rel = repo, commit, rel
        self.resources, self.modules, self.locals = [], {}, {}
        rc, out = git(repo, "ls-tree", "--name-only", commit, rel + "/")
        for path in out.splitlines() if rc == 0 else []:
            if not path.endswith(".tf"):
                continue
            text = git_show(repo, commit, path)
            if text is None:
                continue
            for kind, labels, line, body in parse_blocks(text):
                if kind == "resource" and len(labels) == 2:
                    self.resources.append({"kind": labels[0], "label": labels[1], "file": path, "line": line,
                                           "attrs": top_attrs(body)})
                elif kind == "module" and len(labels) == 1:
                    self.modules[labels[0]] = top_attrs(body)
                elif kind == "locals":
                    self.locals.update(top_attrs(body))

    # -- expansion and name resolution
    def instance_keys(self, res):
        """-> (keys or [None], resolved_bool). [None] means no for_each."""
        fe = res["attrs"].get("for_each")
        if fe is None:
            return [None], True
        expr = fe.strip()
        m = re.fullmatch(r"local\.(\w+)", expr)
        if m and m.group(1) in self.locals:
            expr = self.locals[m.group(1)]
        keys = literal_keys(expr)
        return (keys, True) if keys is not None else ([], False)

    def scalar(self, expr, key):
        """Resolve an expression to a python value (str / bool / None) or raise ValueError."""
        e = expr.strip()
        if e in ("true", "false"):
            return e == "true"
        if e == "null":
            return None
        if e in ("each.key", "each.value") and key is not None:
            return key
        m = re.fullmatch(r"local\.(\w+)", e)
        if m and m.group(1) in self.locals:
            return self.scalar(self.locals[m.group(1)], key)
        lit = string_literal(e)
        if lit is not None:
            def sub(mm):
                inner = mm.group(1).strip()
                if inner in ("each.key", "each.value") and key is not None:
                    return key
                mm2 = re.fullmatch(r"local\.(\w+)", inner)
                if mm2 and mm2.group(1) in self.locals:
                    v = self.scalar(self.locals[mm2.group(1)], key)
                    if isinstance(v, str):
                        return v
                raise ValueError("cannot resolve ${%s}" % inner)
            if "%{" in lit:
                raise ValueError("template directive")
            return re.sub(r"\$\{([^}]*)\}", sub, lit)
        raise ValueError("cannot resolve %r" % e[:60])

    def scope_short(self, scope):
        text = git_show(self.repo, self.commit, MODULE_REL + "/generated_locals.tf")
        if text is None:
            raise ValueError("opal_name generated_locals.tf not at %s" % self.commit)
        m = re.search(r"scope_short\s*=\s*\{(.*?)\n\s*\}", text, re.S)
        pairs = dict(re.findall(r'"([^"]+)"\s*=\s*"([^"]+)"', m.group(1))) if m else {}
        if scope not in pairs:
            raise ValueError("scope %r not in opal_name scope_short" % scope)
        return pairs[scope]

    def module_name(self, mod_label, key):
        args = self.modules.get(mod_label)
        if args is None:
            raise ValueError("module.%s is not declared in this root" % mod_label)
        if not str(string_literal(args.get("source", "")) or "").endswith("/modules/opal_name"):
            raise ValueError("module.%s is not modules/opal_name" % mod_label)
        if "for_each" in args:
            mkeys = literal_keys(self.locals.get(re.sub(r"^local\.", "", args["for_each"].strip()), args["for_each"]))
            if mkeys is None or key not in mkeys:
                raise ValueError("module.%s for_each does not cover key %r" % (mod_label, key))
        val = {a: self.scalar(args[a], key) for a in ("system", "scope", "function", "kind", "qualifier", "fifo") if a in args}
        if not (val.get("system") and val.get("function") and val.get("kind")):
            raise ValueError("module.%s lacks system, function or kind" % mod_label)
        scope = val.get("scope")
        name = "%s%s-%s%s-%s%s" % (
            val["system"], "-" + self.scope_short(scope) if scope else "", val["function"],
            "-" + val["qualifier"] if val.get("qualifier") else "", val["kind"], ".fifo" if val.get("fifo") else "")
        built = builder_name(val["system"], scope, val["function"], val["kind"], val.get("qualifier"), bool(val.get("fifo")))
        if built != name:
            raise ValueError("module-formatted %r differs from lib/opal_naming.py name() %r" % (name, built))
        return name

    def resolve_name(self, res, key):
        attrs = res["attrs"]
        want = NAME_ATTR.get(res["kind"], "name")
        attr = want if want in attrs else next((a for a in OTHER_ATTRS if a in attrs), None)
        if attr is None:
            raise ValueError("no name attribute (%s) declared" % (want or "none"))
        expr = attrs[attr].strip()
        m = re.fullmatch(r"module\.(\w+)(?:\[[^\]]*\])?\.name", expr)
        if m:
            return self.module_name(m.group(1), key)
        return self.scalar(expr, key)


_BUILDER = []


def builder_module():
    """lib/opal_naming.py, loaded by path from this script's own repo."""
    if not _BUILDER:
        spec = importlib.util.spec_from_file_location("opal_naming_builder", os.path.join(SELF_REPO, "lib", "opal_naming.py"))
        mod = importlib.util.module_from_spec(spec)
        sys.modules["opal_naming_builder"] = mod
        spec.loader.exec_module(mod)
        _BUILDER.append(mod)
    return _BUILDER[0]


def builder_name(system, scope, function, kind, qualifier, fifo):
    """lib/opal_naming.py name() -- the builder."""
    return builder_module().name(system, scope, function, kind, qualifier, fifo)


def is_nameless(res):
    kind = res["kind"]
    if kind in NAME_ATTR and NAME_ATTR[kind] is None:
        return True
    return bool(NAMELESS_KIND_RE.search(kind))


def addresses(root):
    """-> {address: (resource, key, resolved)} for one Root."""
    out = {}
    for res in root.resources:
        keys, ok = root.instance_keys(res)
        if not ok:
            out["%s.%s[*]" % (res["kind"], res["label"])] = (res, None, False)
            continue
        for k in keys:
            addr = "%s.%s" % (res["kind"], res["label"]) + ('["%s"]' % k if k is not None else "")
            out[addr] = (res, k, True)
    return out


def changed_roots(repo, since, until):
    rc, out = git(repo, "diff", "--name-only", since, until, "--", TF_BASE)
    roots = set()
    for path in out.splitlines() if rc == 0 else []:
        parts = path.split("/")
        if path.endswith(".tf") and len(parts) > 4:
            roots.add("/".join(parts[:4]))
    return sorted(roots)


def intro_commit(repo, since, until, rel, address, cache):
    rc, out = git(repo, "rev-list", "--reverse", "%s..%s" % (since, until), "--", rel)
    for c in out.split() if rc == 0 else []:
        if (c, rel) not in cache:
            cache[(c, rel)] = set(addresses(Root(repo, c, rel)))
        if address in cache[(c, rel)]:
            return c
    return None


def registry_rows(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return [r for r in data.get("resources", []) if isinstance(r, dict) and "name" in r]


_NODE_TYPE_OVERRIDE = {"aws_iam_group": "IAM_GROUP"}  # NAMING_SCHEMA tf_type_map lacks the group; kind.by_type has it


def node_type_of(kind):
    """The NAMING_SCHEMA node type of a Terraform kind, or None."""
    if kind in _NODE_TYPE_OVERRIDE:
        return _NODE_TYPE_OVERRIDE[kind]
    row = builder_module().load_schema().get("tf_type_map", {}).get(kind)
    return row.get("node_type") if isinstance(row, dict) else None


def registry_class(name, kind, rows):
    """-> REGISTERED | SELF-RESOLVING | ROW-NEEDED; ValueError when the registry's reader cannot place the name.

    The reader is lib/opal_naming.py's own, called as validate() calls it (its resources.json limb): the name's body
    through _res_tokens, then _slots with nm=None; a name whose tokens leave the {system} placeholder resolves no
    system on its own. grade() cannot stand in: it returns NOT-GRADED for IAM_USER and does not report the slot."""
    if any(r["name"] == name for r in rows):
        return "REGISTERED"
    typ = node_type_of(kind)
    if typ is None:
        raise ValueError("kind %s has no node type in NAMING_SCHEMA tf_type_map" % kind)
    mod = builder_module()
    body = name[:-5] if typ == "SQS_QUEUE" and name.endswith(".fifo") else name
    try:
        vocab = mod._vocab()
        _sysv, _out, _scope, placeholder = mod._slots(None, mod._res_tokens(body, vocab, "a resource name"), typ, vocab)
    except (mod.RaiseDefect, IndexError) as exc:
        raise ValueError("the registry's reader cannot place %r: %s" % (name, exc)) from None
    return "ROW-NEEDED" if placeholder else "SELF-RESOLVING"


def validator_count_line():
    """The last line of `python lib/opal_naming.py validate`, with its exit code."""
    try:
        p = subprocess.run([sys.executable, os.path.join(SELF_REPO, "lib", "opal_naming.py"), "validate"], cwd=SELF_REPO,
                           capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
    except (subprocess.TimeoutExpired, OSError) as exc:
        return "VALIDATOR UNREAD (%s)" % type(exc).__name__
    lines = [ln for ln in p.stdout.splitlines() if ln.strip()]
    return "VALIDATOR rc=%d %s" % (p.returncode, lines[-1] if lines else "(no output)")


# ---------------------------------------------------------------- the cloud-graph arm

GRAPH_TIMEOUT = 60
_HIT_NODE = re.compile(r"^ {4}(\S+)\s+drift=(\S+)")
_HIT_TYPE = re.compile(r"^ {2}\[([A-Z0-9_]+)\]\s*$")
_VINTAGE_AT = re.compile(r"as of (\d{4}-\d\d-\d\d) (\d\d:\d\d:\d\d) UTC")


def default_graph_tool():
    return os.path.join(SELF_REPO, ".tools", "comp-find")


def graph_vintage_epoch(text):
    """Epoch seconds of the graph's built time in a VINTAGE line (UTC), or None."""
    m = _VINTAGE_AT.search(text or "")
    if not m:
        return None
    return calendar.timegm(time.strptime(m.group(1) + " " + m.group(2), "%Y-%m-%d %H:%M:%S"))


def graph_read(tool, name):
    """One `comp-find --corpus aws <name> --all` call -> dict(state, nodes, scanned, vintage, loose, why).

    state is READ (every hit parsed, none deferred) or UNREAD. nodes = [(node_type, node_name, drift, arn, how)] where
    the exact name is inside the node's name or ARN; loose = hits that match only in properties."""
    out = {"state": "UNREAD", "nodes": [], "scanned": None, "vintage": "", "loose": 0, "why": ""}
    pat = name.replace(".", r"\.")
    try:
        p = subprocess.run([sys.executable, tool, "--corpus", "aws", pat, "--all", "--budget", "50"], capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=GRAPH_TIMEOUT)
    except subprocess.TimeoutExpired:
        out["why"] = "timeout %ds" % GRAPH_TIMEOUT
        return out
    except OSError as exc:
        out["why"] = "cannot run the tool: %s" % exc
        return out
    text = p.stdout
    if p.returncode != 0:
        out["why"] = "rc=%d %s" % (p.returncode, (p.stderr.strip() or text.strip())[-160:])
        return out
    vint = re.search(r"^\s*VINTAGE:\s*(.*)$", text, re.M)
    out["vintage"] = vint.group(1).strip() if vint else ""
    den = re.search(r"DENOMINATOR:\s*(\d+) hit\(s\) across (\d+) aws node\(s\) scanned", text)
    dfr = re.search(r"DEFERRED:\s*(\d+) of (\d+)", text)
    if not den or not dfr or not vint:
        out["why"] = "no DENOMINATOR / DEFERRED / VINTAGE line in the response"
        return out
    if int(dfr.group(1)) != 0 or "BUDGET REACHED" in text:
        out["why"] = "the pull was deferred or hit its budget"
        return out
    hits, out["scanned"] = int(den.group(1)), int(den.group(2))
    lines = text.splitlines()
    exact = re.compile(r"(?<![\w.-])" + re.escape(name) + r"(?:\.fifo)?(?![\w-])")
    parsed, cur_type = 0, None
    for i, ln in enumerate(lines):
        mt = _HIT_TYPE.match(ln)
        if mt:
            cur_type = mt.group(1)
            continue
        mn = _HIT_NODE.match(ln)
        if mn and cur_type:
            parsed += 1
            arn = lines[i + 1].strip() if i + 1 < len(lines) and lines[i + 1].startswith(" " * 6) else ""
            if exact.search(mn.group(1)):
                out["nodes"].append((cur_type, mn.group(1), mn.group(2), arn, "name"))
            elif exact.search(arn):
                out["nodes"].append((cur_type, mn.group(1), mn.group(2), arn, "arn"))
            else:
                out["loose"] += 1
    if parsed != hits:
        out["why"] = "parsed %d of %d hits" % (parsed, hits)
        return out
    out["state"] = "READ"
    return out


def commit_epoch(repo, commit):
    rc, out = git(repo, "show", "-s", "--format=%ct", commit)
    try:
        return int(out.strip()) if rc == 0 else None
    except ValueError:
        return None


def iso(epoch):
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(epoch)) if epoch is not None else "UNREAD"


def graph_result(tool, name, intro_full, repo, state):
    """-> (label, text). state carries the per-run vintage and a per-name cache; label is one of NODE, NO-NODE,
    NO-NODE-GRAPH-OLDER, GRAPH-UNREAD."""
    if name not in state["cache"]:
        state["cache"][name] = graph_read(tool, name)
    g = state["cache"][name]
    if g["vintage"] and not state["vintage"]:
        state["vintage"] = g["vintage"]
    if g["state"] != "READ":
        return "GRAPH-UNREAD", "GRAPH-UNREAD (%s)" % g["why"]
    scanned = "scanned=%s" % g["scanned"]
    loose = " props-only-hits-not-counted=%d" % g["loose"] if g["loose"] else ""
    if g["nodes"]:
        shown = "; ".join("NODE node_type=%s drift_class=%s matched-in-%s=%s" % (t, d, how, nm if how == "name" else arn)
                          for t, nm, d, arn, how in g["nodes"])
        return "NODE", "%s %s%s" % (shown, scanned, loose)
    built = graph_vintage_epoch(g["vintage"])
    commit_t = commit_epoch(repo, intro_full) if intro_full else None
    if built is not None and commit_t is not None and built < commit_t:
        return "NO-NODE-GRAPH-OLDER", "NO-NODE-GRAPH-OLDER graph_built=%s < intro_commit_time=%s %s%s" % (
            iso(built), iso(commit_t), scanned, loose)
    cmp_text = ("graph_built=%s >= intro_commit_time=%s" % (iso(built), iso(commit_t))
                if built is not None and commit_t is not None else "the two times could not both be read")
    return "NO-NODE", "NO-NODE (%s) %s%s" % (cmp_text, scanned, loose)


def run(repo, since, until, roots, registry, graph_tool=None):
    rc1, c1 = git(repo, "rev-parse", "--short=10", since + "^{commit}")
    rc2, c2 = git(repo, "rev-parse", "--short=10", until + "^{commit}")
    if rc1 or rc2:
        raise SystemExit("REFUSED: cannot resolve --since/--until to commits in %s" % repo)
    c1, c2 = c1.strip(), c2.strip()
    rows = registry_rows(registry)
    tool = graph_tool or default_graph_tool()
    roots = roots if roots else changed_roots(repo, c1, c2)
    lines, cache = [], {}
    gstate = {"cache": {}, "vintage": ""}
    cnt = dict(nameless=0, self_resolving=0, registered=0, row_needed=0, unresolved=0, nodes=0, no_node=0, older=0, unread=0)
    for rel in roots:
        rel = rel.strip("/")
        before = set(addresses(Root(repo, c1, rel)))
        after = addresses(Root(repo, c2, rel))
        root = Root(repo, c2, rel)
        for addr in sorted(a for a in after if a not in before):
            res, key, expanded = after[addr]
            where = "%s:%d" % (res["file"], res["line"])
            intro_full = intro_commit(repo, c1, c2, rel, addr, cache)
            intro = " intro=%s" % (intro_full[:10] if intro_full else "?")
            if is_nameless(res):
                cnt["nameless"] += 1
                lines.append("%-14s %s name=- decl=%s%s" % ("NAMELESS", addr, where, intro))
                continue
            if not expanded:
                cnt["unresolved"] += 1
                lines.append("%-14s %s name=for_each not a literal set decl=%s%s" % ("UNRESOLVED", addr, where, intro))
                continue
            try:
                name = root.resolve_name(res, key)
                if not isinstance(name, str) or not name:
                    raise ValueError("resolved to %r" % (name,))
                cls = registry_class(name, res["kind"], rows)
            except ValueError as exc:
                cnt["unresolved"] += 1
                lines.append("%-14s %s name=%s decl=%s%s" % ("UNRESOLVED", addr, exc, where, intro))
                continue
            cnt[cls.lower().replace("-", "_")] += 1
            label, text = graph_result(tool, name, intro_full, repo, gstate)
            cnt[{"NODE": "nodes", "NO-NODE": "no_node", "NO-NODE-GRAPH-OLDER": "older", "GRAPH-UNREAD": "unread"}[label]] += 1
            lines.append("%-14s %s name=%s type=%s decl=%s%s | graph: %s" % (cls, addr, name, node_type_of(res["kind"]), where, intro, text))
    created = len(lines)
    named = cnt["self_resolving"] + cnt["registered"] + cnt["row_needed"]
    ok = cnt["row_needed"] == 0 and cnt["unresolved"] == 0 and cnt["unread"] == 0
    lines.append("GRAPH-VINTAGE %s" % (gstate["vintage"] or "UNREAD (no call returned a vintage line)"))
    lines.append(validator_count_line())
    built_epoch = graph_vintage_epoch(gstate["vintage"])
    lines.append("ROUND-RESOURCES since=%s until=%s roots=%s created=%d nameless=%d named=%d self_resolving=%d registered=%d "
                 "row_needed=%d unresolved=%d graph_unread=%d graph_nodes=%d no_node=%d no_node_graph_older=%d graph_built=%s ok=%s"
                 % (c1, c2, ",".join(roots) if roots else "-", created, cnt["nameless"], named, cnt["self_resolving"],
                    cnt["registered"], cnt["row_needed"], cnt["unresolved"], cnt["unread"], cnt["nodes"], cnt["no_node"],
                    cnt["older"], iso(built_epoch), ok))
    return lines


def main(argv=None):
    ap = argparse.ArgumentParser(description="every resource a range of commits created in Terraform: its registry class and its cloud-graph node")
    ap.add_argument("--since", required=True)
    ap.add_argument("--until", required=True)
    ap.add_argument("--root", action="append", default=[], help="a Terraform root directory (repeatable)")
    ap.add_argument("--registry", default=None, help="resources.json (default: the repo's infra/logic/registry/resources.json)")
    ap.add_argument("--repo", default=None, help="the git repository (default: the repository holding this script)")
    ap.add_argument("--graph-tool", default=None, help="the comp-find script the cloud-graph arm calls (default: .tools/comp-find); a test points it at a recorder")
    a = ap.parse_args(argv)
    repo = os.path.abspath(a.repo) if a.repo else SELF_REPO
    registry = a.registry or os.path.join(repo, "infra", "logic", "registry", "resources.json")
    if not os.path.isfile(registry):
        print("REFUSED: registry file not found: %s" % registry)
        return 2
    for line in run(repo, a.since, a.until, a.root, registry, a.graph_tool):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
