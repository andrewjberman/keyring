#!/usr/bin/env python3
"""naming-apply-gate.py -- the naming safe-apply limb (LGIC_ENFORCE cell EN-t-2; PRD candidate E8, second half; DEC-6).

TWO MODES, round 2 (row W3-S8, CTO round-1 analysis s.2: an apply has no diff, so whether a resource is being ADDED
is known only to a plan):
  PRE-PLAN (DIR mode, unchanged shape): grades the resource-name attributes of ONE Terraform root (DIR) with
    lib/opal_naming.py grade(), BEFORE any plan runs -- it cannot tell an existing resource from a new one, so it
    NEVER refuses (every bad grade prints, capped at WARN).
  PLAN (--plan-json FILE, new): grades a rendered `terraform show -json` document's resource_changes. A resource
    being ADDED (an action including `create`, or an `update` whose own-name attribute changes) is graded for real
    -- a REFUSE-worthy grade REFUSES, enforcing. Every other resource (no-op, a name-keeping update, a delete) is
    graded too but only ever WARNs: it already exists, so this limb is not the one that gets to block it.
.tools/safe-apply.sh calls DIR mode as one stage right after the halt checkpoint, then renders its own plan and
calls plan mode on it, before any other plan-reading gate (tag-authz, tombstone) and before apply.

WHAT IT GRADES, AND WHY (read from org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/TF_LABEL_CENSUS.md, EN-t-1):
  - The OWN-NAME attribute of every top-level resource block in DIR's *.tf files (the files terraform loads for that
    root; a called module is its own root). That attribute is the string AWS names the object by, so it is the string
    the opal_name module would have to produce. The Terraform-type map is the census's section 3, taken from the
    commit limb's TF_NODE so the two limbs read one map: its 28 graded types (aws_sqs_queue.name,
    aws_lambda_function.function_name, aws_cloudwatch_metric_alarm.alarm_name, aws_instance tags.Name,
    aws_s3_bucket.bucket, ...), plus the census's 2 types whose node type is NOT GRADED (aws_iam_user.name,
    aws_route53_record.name), which print NOT-GRADED and pass.
  - NOT labels. A resource label is the Terraform state address and is never sent to AWS; NAMING_SCHEMA lists labels
    as not_covered, the census grades them only on its order's word and outside the schema's domain (its section 1),
    and it shows no label that is an AWS name.
  - NOT the 30 types that carry an own name but map to no node type (census section 3: aws_ecr_repository.name,
    aws_kms_alias.name, ...). grade() has no node type to grade them as; the census RAISES every one at G1.1.
  - NOT an attribute of a block nested inside a resource, and NOT an argument of a module call: neither is the
    resource's own name.
  - NOT an expression. A value that is not one literal string -- a reference (module.<x>.<y>, local.<x>, var.<x>,
    each.<x>), a function call, or a template with ${...} -- has its value only in a plan, and this limb runs before
    plan. Each is listed on an `unresolved` line (one that reads a module whose source is the opal_name module is
    marked module-produced) and none counts as graded.

THE MATRIX, PRE-PLAN (DIR mode). Every graded name is read as the tree states it, since addition status is unknown here:
    OUT-OF-PATTERN, ALIAS or RAISE     WARN, canonical printed (the module would not produce this name; this stage
                                        cannot tell an addition from an existing resource, so it never refuses)
    CONFORMANT, NOT-GRADED             pass
An expression (a reference, a function call, a template with ${...}) has its value only in a plan and is listed on
an `unresolved` line, never graded; the summary line states how many are deferred to plan.

THE MATRIX, PLAN (--plan-json mode). DEC-6 decides NEW against a diff's pre-image; a plan's resource_changes decide
it directly (an action including `create`, or an `update` whose own-name attribute changed, per resource):
    ADDITION, and OUT-OF-PATTERN, ALIAS or RAISE     REFUSE, canonical printed (the module would not produce this
                                                      name; DEC-6's RAISE row: a rule or registry defect refuses like
                                                      any other refusal once enforcing)
    ADDITION, and CONFORMANT or NOT-GRADED           pass
    NOT an addition (no-op, a name-keeping update, a delete)     WARN if the grade would otherwise refuse, else pass
                                                                  -- it already exists; this limb never blocks it

ENFORCE AND OUTPUT are the commit limb's (.tools/naming-gate.py, EN-g-1): ENFORCE is --enforce, env
NAMING_GATE_ENFORCE=1, or a present org/mcp/naming-gate.enforce, and a REFUSE then exits 1. Otherwise it is WARN mode and
exits 0, on an internal error too (`NAMING ERROR <reason>`).
  DIR mode: one `NAMING <verdict> <file>:<line> <string> -> <canonical>` line per graded name (<verdict> is the
    grade, or WARN) with a `why:` line under it, then `NAMING-GATE: <PASS|WARN> <n> graded` (never REFUSE -- see
    above). Every verdict line is appended to org/mcp/naming-gate-verdicts.log (runtime state; gitignored; never
    committed), in mode APPLY-WARN or APPLY-ENFORCE.
  Plan mode: one `NAMING <verdict> <address> <name> -> <canonical>` line per graded name (<verdict> is REFUSE, WARN
    or the grade) with a `why:` line under it, then `NAMING-PLAN: <PASS|WARN|REFUSE> <n> graded`. Logged the same
    way, in mode PLAN-WARN or PLAN-ENFORCE.

Usage:
    python .tools/naming-apply-gate.py DIR [--enforce]
    python .tools/naming-apply-gate.py --plan-json FILE [--enforce]

Standard library only. ASCII only.
"""
from __future__ import annotations

import argparse
import datetime
import importlib.machinery
import importlib.util
import json
import os
import re
import sys

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOLS_DIR)
OPAL_PATH = os.path.join(REPO, "lib", "opal_naming.py")
COMMIT_LIMB = os.path.join(TOOLS_DIR, "naming-gate.py")
ENFORCE_FILE = os.path.join(REPO, "org", "mcp", "naming-gate.enforce")
VERDICT_LOG = os.path.join(REPO, "org", "mcp", "naming-gate-verdicts.log")
# The census's two own-name types whose node type grade() places outside its domain (G1.2): graded, NOT-GRADED, pass.
NOT_GRADED_TYPES = {"aws_iam_user": ("IAM_USER", "name"), "aws_route53_record": ("ROUTE53_RECORD", "name")}
RAISE_CANON = "(rule or registry defect)"
HEREDOC_RE = re.compile(r"<<-?([A-Za-z_][A-Za-z0-9_]*)[ \t]*$")


class GateError(Exception):
    """The limb cannot run: printed as NAMING ERROR."""


def _load(path, modname):
    if not os.path.isfile(path):
        raise GateError("%s is absent" % os.path.relpath(path, REPO).replace("\\", "/"))
    loader = importlib.machinery.SourceFileLoader(modname, path)
    spec = importlib.util.spec_from_loader(modname, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


def enforcing(flag):
    return bool(flag) or os.environ.get("NAMING_GATE_ENFORCE") == "1" or os.path.exists(ENFORCE_FILE)


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
        print("WARN: naming-apply-gate could not append to %s: %s" % (VERDICT_LOG, exc), file=sys.stderr)


# --------------------------------------------------------------------------- reading a tree
def strip_heredocs(text):
    """Blank every heredoc body (line numbers kept) and put the word HEREDOC where it opened: a heredoc is never a
    literal name, and its body (a JSON policy, a user_data script) must not reach the block scanner as Terraform."""
    lines, out, i = text.split("\n"), [], 0
    while i < len(lines):
        ln = lines[i]
        m = HEREDOC_RE.search(ln)
        if m and not ln.lstrip().startswith(("#", "//")):
            out.append(ln[:m.start()] + "HEREDOC")
            marker, i = m.group(1), i + 1
            while i < len(lines) and lines[i].strip() != marker:
                out.append("")
                i += 1
            if i < len(lines):
                out.append("")
                i += 1
            continue
        out.append(ln)
        i += 1
    return "\n".join(out)


def read_tf(scan, text, types):
    """(rows, modules) for one .tf file. rows: one dict per own-name attribute of a top-level resource block whose type
    is in `types`; modules: {module label: source} for the file's top-level module calls."""
    text = strip_heredocs(text)
    src_lines = text.split("\n")
    toks = scan(text, "tf")
    blocks, stmt, bracket, cur = [], [], 0, None
    rows, modules = [], {}

    def finish(c):
        if c is None:
            return
        owner = next((k for k in range(len(c["blocks"]) - 1, -1, -1) if c["blocks"][k].get("block")), None)
        if owner != 0:
            return  # outside any block, or inside a nested block: never a top-level resource's own name
        b = c["blocks"][0]
        path = ".".join([m.get("map_attr") or "" for m in c["blocks"][1:]] + [c["attr"]])
        vals = c["vals"]
        if b["kind"] == "module" and path == "source" and b["labels"]:
            strs = [t for t in vals if t[0] == "str"]
            if strs:
                modules[b["labels"][0]] = strs[0][1]
            return
        if b["kind"] != "resource" or len(b["labels"]) < 2:
            return
        spec = types.get(b["labels"][0])
        if not spec or path != spec[1]:
            return
        literal = None
        if len(vals) == 1 and vals[0][0] == "str" and "${" not in vals[0][2] and "%{" not in vals[0][2]:
            literal = vals[0][1]
        line_txt = src_lines[c["line"] - 1] if 0 < c["line"] <= len(src_lines) else ""
        expr = line_txt.split("=", 1)[1].strip() if "=" in line_txt else line_txt.strip()
        ref = [t[1] for t in vals if t[0] == "word"][:2]
        rows.append({"line": c["line"], "tf_type": b["labels"][0], "label": b["labels"][1], "node_type": spec[0],
                     "attr": path, "value": literal, "expr": expr,
                     "module": ref[1] if len(ref) == 2 and ref[0] == "module" and vals and vals[0] == ("word", "module") else None})

    for kind, v, raw, ln in toks:
        if kind == "nl":
            if bracket == 0:
                finish(cur)
                cur, stmt = None, []
            continue
        if kind == "sym":
            if v == "{":
                has_eq = any(t[0] == "sym" and t[1] in "=:" for t in stmt)
                if stmt and stmt[0][0] == "word" and not has_eq:
                    blocks.append({"block": True, "kind": stmt[0][1], "labels": [t[1] for t in stmt[1:] if t[0] == "str"]})
                else:
                    blocks.append({"block": False, "map_attr": cur["attr"] if cur else None})
                cur, stmt, bracket = None, [], 0
                continue
            if v == "}":
                finish(cur)
                if blocks:
                    blocks.pop()
                cur, stmt, bracket = None, [], 0
                continue
            if v in "[(":
                bracket += 1
            elif v in "])":
                bracket = max(0, bracket - 1)
            elif v in "=:" and cur is None and bracket == 0 and len(stmt) == 1 and stmt[0][0] in ("word", "str"):
                cur = {"attr": stmt[0][1], "line": ln, "blocks": list(blocks), "vals": []}
                stmt.append(("sym", v))
                continue
            stmt.append(("sym", v))
            if cur is not None:
                cur["vals"].append(("sym", v, None))
            continue
        tok = (kind, v) if kind == "word" else ("str", v)
        stmt.append(tok)
        if cur is not None:
            cur["vals"].append((kind, v, raw) if kind == "str" else (kind, v))
    finish(cur)
    return rows, modules


def tree_files(d):
    if not os.path.isdir(d):
        raise GateError("not a directory: %s" % d)
    return sorted(f for f in os.listdir(d) if f.endswith(".tf") and os.path.isfile(os.path.join(d, f)))


def _shown(d, f):
    p = os.path.normpath(os.path.join(d, f)).replace("\\", "/")
    return p


# --------------------------------------------------------------------------- the matrix at apply
def judge(mod, node_type, s):
    """(line verdict, canonical, why, refuses) for one literal name, graded as an ADDITION."""
    try:
        verdict, canon = mod.grade(s, node_type)
    except mod.RaiseDefect as exc:
        return ("REFUSE", RAISE_CANON,
                "RAISE as %s: a rule or registry defect, not a naming verdict: %s. DEC-6: refused like any refusal once"
                " enforcing" % (node_type, exc), True)
    if verdict == "NOT-GRADED":
        return "NOT-GRADED", "-", "%s is outside the grade's domain (G1.2)" % node_type, False
    if verdict in ("OUT-OF-PATTERN", "ALIAS"):
        return ("REFUSE", canon,
                "%s as %s: the module would not produce this name; an apply has no diff and runs this stage before any"
                " plan, so the name is read as the tree states it" % (verdict, node_type), True)
    return "CONFORMANT", canon, "CONFORMANT as %s" % node_type, False


def judge_capped(mod, node_type, s):
    """As judge(), but a REFUSE-worthy grade is capped at WARN, refuses=False -- for a name this limb cannot
    confirm is an ADDITION: a pre-plan literal (DIR mode never sees a plan), or a plan resource that is a
    no-op, a name-keeping update or a delete (EN-t-2 round 2 item 1: 'every other resource ... only WARNs')."""
    verdict, canon, why, refuses = judge(mod, node_type, s)
    if refuses:
        return "WARN", canon, why + " -- not confirmed as an addition here, so this only WARNs", False
    return verdict, canon, why, False


def run(d):
    ng = _load(COMMIT_LIMB, "naming_gate_for_apply")
    types = dict(ng.TF_NODE)
    types.update(NOT_GRADED_TYPES)
    try:
        mod = _load(OPAL_PATH, "opal_naming_for_apply")
    except GateError:
        raise
    except Exception as exc:
        raise GateError("lib/opal_naming.py cannot be loaded: %s: %s" % (type(exc).__name__, exc)) from None
    files = tree_files(d)
    graded, unresolved, modules = [], [], {}
    per_file = []
    for f in files:
        with open(os.path.join(d, f), "rb") as fh:
            text = fh.read().decode("utf-8", errors="replace").replace("\r\n", "\n")
        rows, mods = read_tf(ng.scan, text, types)
        modules.update(mods)
        per_file.append((f, rows))
    for f, rows in per_file:
        for r in rows:
            shown = _shown(d, f)
            if r["value"] is None:
                src = modules.get(r["module"]) if r["module"] else None
                unresolved.append((shown, r, src is not None and "opal_name" in src))
                continue
            # DIR mode cannot tell an existing resource from a new one (item 2), so every literal is graded
            # capped at WARN: a REFUSE-worthy name still prints, it just never blocks (refuses is always False).
            verdict, canon, why, refuses = judge_capped(mod, r["node_type"], r["value"])
            graded.append((verdict, shown, r["line"], r["value"], canon,
                           "%s.%s %s: %s" % (r["tf_type"], r["label"], r["attr"], why), refuses))
    return graded, unresolved, len(files)


# --------------------------------------------------------------------------- plan mode (EN-t-2, round 2)
def _get_path(d, path):
    """Read a dotted attribute path (e.g. 'tags.Name') out of a plan JSON object; None if any hop is missing,
    the value along the way is not a dict, or the leaf is not a string."""
    if not isinstance(d, dict) or not path:
        return None
    cur = d
    for part in path.split("."):
        if not isinstance(cur, dict) or part not in cur:
            return None
        cur = cur[part]
    return cur if isinstance(cur, str) else None


def _is_addition(change, attr):
    """A resource_changes entry is an ADDITION when its actions include `create` (a plain create, or the
    create half of a replace), or when it is an `update` whose own-name attribute's value changed -- a rename
    is a new name even though the resource address is not new (item 1)."""
    actions = (change or {}).get("actions") or []
    if "create" in actions:
        return True
    if "update" in actions:
        return _get_path((change or {}).get("before") or {}, attr) != _get_path((change or {}).get("after") or {}, attr)
    return False


def run_plan(path):
    """graded rows for one `terraform show -json` document's resource_changes: one row per managed resource
    whose Terraform type carries a graded own-name attribute (the schema's map, same as DIR mode and the
    commit limb -- item 4). An ADDITION is graded for real (judge(), may REFUSE); every other resource is
    graded capped at WARN (judge_capped(), item 1's 'every other resource ... only WARNs') -- it already
    exists (or is being removed), and this limb does not get to block it."""
    ng = _load(COMMIT_LIMB, "naming_gate_for_apply_plan")
    types = dict(ng.TF_NODE)
    types.update(NOT_GRADED_TYPES)
    try:
        mod = _load(OPAL_PATH, "opal_naming_for_apply_plan")
    except GateError:
        raise
    except Exception as exc:
        raise GateError("lib/opal_naming.py cannot be loaded: %s: %s" % (type(exc).__name__, exc)) from None
    if not os.path.isfile(path):
        raise GateError("%s is absent" % path)
    try:
        with open(path, "rb") as fh:
            plan = json.loads(fh.read().decode("utf-8"))
    except (OSError, ValueError) as exc:
        raise GateError("cannot parse plan json %s: %s" % (path, exc)) from None
    if not isinstance(plan, dict):
        raise GateError("%s is not a JSON object" % path)
    changes = plan.get("resource_changes")
    if not isinstance(changes, list):
        raise GateError("%s carries no resource_changes array (is it a `terraform show -json` document?)" % path)
    graded = []
    for rc in changes:
        if not isinstance(rc, dict) or rc.get("mode") != "managed":
            continue
        spec = types.get(rc.get("type"))
        if not spec:
            continue
        node_type, attr = spec
        change = rc.get("change") or {}
        after, before = change.get("after"), change.get("before")
        name = _get_path(after, attr) if isinstance(after, dict) else _get_path(before, attr)
        if not name:
            continue
        addition = _is_addition(change, attr)
        address = rc.get("address") or "?"
        if addition:
            verdict, canon, why, refuses = judge(mod, node_type, name)
        else:
            verdict, canon, why, refuses = judge_capped(mod, node_type, name)
        graded.append((verdict, address, name, canon,
                       "%s (%s): %s" % (address, "ADDITION" if addition else "existing", why), refuses))
    return graded


def main(argv=None):
    ap = argparse.ArgumentParser(prog="naming-apply-gate.py", description="the naming safe-apply limb (LGIC_ENFORCE EN-t-2, DEC-6)")
    ap.add_argument("dir", nargs="?", help="the Terraform root safe-apply is about to plan (its -chdir, or .) -- pre-plan mode")
    ap.add_argument("--plan-json", dest="plan_json", metavar="FILE",
                     help="a rendered `terraform show -json` document to grade -- plan mode (EN-t-2 round 2)")
    ap.add_argument("--enforce", action="store_true", help="a REFUSE exits 1 (also NAMING_GATE_ENFORCE=1 or org/mcp/naming-gate.enforce)")
    args = ap.parse_args(argv)
    if bool(args.dir) == bool(args.plan_json):
        ap.error("give exactly one of DIR or --plan-json")
    enforce = enforcing(args.enforce)
    if args.plan_json:
        return _main_plan(args.plan_json, enforce)
    return _main_dir(args.dir, enforce)


def _main_dir(d, enforce):
    mode = "APPLY-ENFORCE" if enforce else "APPLY-WARN"
    try:
        graded, unresolved, nfiles = run(d)
    except Exception as exc:
        line = "NAMING ERROR %s" % (str(exc) if isinstance(exc, GateError) else "%s: %s" % (type(exc).__name__, exc))
        print(line)
        log_lines([line], mode)
        if not enforce:
            print("  (WARN window: the limb's own error never blocks an apply; enforce is off)")
        return 1 if enforce else 0
    graded.sort(key=lambda r: (r[1], r[2], r[3]))
    verdict_lines = []
    for verdict, path, line, s, canon, why, _refuses in graded:
        vl = "NAMING %s %s:%d %s -> %s" % (verdict, path, line, s, canon)
        verdict_lines.append(vl)
        print(vl)
        print("  why: %s" % why)
    for path, r, by_module in sorted(unresolved, key=lambda u: (u[0], u[1]["line"])):
        print("  unresolved before plan: %s:%d %s.%s %s = %s (%s)" % (
            path, r["line"], r["tf_type"], r["label"], r["attr"], r["expr"],
            "module-produced: module.%s sources the opal_name module" % r["module"] if by_module
            else "an expression; its value exists only in a plan"))
    refused = sum(1 for g in graded if g[6])  # always 0: DIR mode grades every literal with judge_capped()
    warned = sum(1 for g in graded if g[0] == "WARN")
    n_deferred = len(unresolved)
    noun = "expression" if n_deferred == 1 else "expressions"
    denom = "NAMING-APPLY: %s: %d .tf file(s), %d resource-name attribute(s): %d graded, %d %s deferred to plan (%d module-produced)" % (
        _shown(d, "."), nfiles, len(graded) + len(unresolved), len(graded), n_deferred, noun,
        sum(1 for u in unresolved if u[2]))
    print(denom)
    if nfiles == 0:
        print("  (0 .tf files in this directory: nothing to grade; is -chdir=DIR correct?)")
    summary = "WARN" if (refused or warned) else "PASS"  # DIR mode NEVER refuses -- it cannot tell ADD from EXISTING
    if warned:
        print("  (pre-plan: %d name(s) would REFUSE if this turns out to be an addition; the plan-time stage"
              " decides that -- this stage never refuses)" % warned)
    last = "NAMING-GATE: %s %d graded" % (summary, len(graded))
    print(last)
    log_lines(verdict_lines + [denom, last], mode)
    return 1 if (refused and enforce) else 0


def _main_plan(path, enforce):
    mode = "PLAN-ENFORCE" if enforce else "PLAN-WARN"
    try:
        graded = run_plan(path)
    except Exception as exc:
        line = "NAMING ERROR %s" % (str(exc) if isinstance(exc, GateError) else "%s: %s" % (type(exc).__name__, exc))
        print(line)
        log_lines([line], mode)
        if not enforce:
            print("  (WARN window: the limb's own error never blocks an apply; enforce is off)")
        return 1 if enforce else 0
    graded.sort(key=lambda r: (r[1], r[2]))
    verdict_lines = []
    for verdict, address, name, canon, why, _refuses in graded:
        vl = "NAMING %s %s %s -> %s" % (verdict, address, name, canon)
        verdict_lines.append(vl)
        print(vl)
        print("  why: %s" % why)
    refused = sum(1 for g in graded if g[5])
    warned = sum(1 for g in graded if g[0] == "WARN")
    denom = "NAMING-PLAN-DENOM: %s: %d resource-name(s) graded" % (path, len(graded))
    print(denom)
    if not graded:
        print("  (0 graded resource-name(s) in this plan: nothing to grade, or nothing this schema's map covers)")
    if refused and enforce:
        summary = "REFUSE"
    elif refused or warned:
        summary = "WARN"
    else:
        summary = "PASS"
    if refused and not enforce:
        print("  (WARN window: %d REFUSE verdict(s) did not block; ENFORCE is --enforce, NAMING_GATE_ENFORCE=1 or"
              " org/mcp/naming-gate.enforce)" % refused)
    last = "NAMING-PLAN: %s %d graded" % (summary, len(graded))
    print(last)
    log_lines(verdict_lines + [denom, last], mode)
    return 1 if (refused and enforce) else 0


if __name__ == "__main__":
    sys.exit(main())
