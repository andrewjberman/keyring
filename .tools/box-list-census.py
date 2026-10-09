#!/usr/bin/env python3
"""box-list-census.py -- which files under .tools, lib and org/devices still LIST boxes by hand (NFRA_CTLPLN FWD-2, CT-t-3).

A box is named once, in the device register org/devices/DEVICES.json, read through lib/devices.py. This census finds every file
that names TWO OR MORE DISTINCT boxes in one literal list, tuple, set, dict, regex alternation, shell `case`/`for ... in` list,
PowerShell ValidateSet or YAML list. The box tokens are the register's names and aliases (an alias shorter than 3 characters is
dropped: it is a lane letter, not a name); NO box is typed in this file. A box named in prose or a comment is not a list and is
not counted. A python file is read by AST (a string constant is a token only when it EQUALS one; a dict's values count only when
none of its keys is a field name, because a record's field naming a box is data); every other text file by a
bracket scan with comments removed. Tests (a path under /tests/ or a name starting test_) are not counted and are listed apart.
The register itself is the one place that may list boxes and is skipped, by name in the output. It writes nothing.

    python .tools/box-list-census.py [--root DIR] [--register FILE] [--dirs a,b,c]

LAST line: BOX-LIST-CENSUS scanned=<n> hand_listed=<k> files=<comma list or ->
"""
from __future__ import annotations

import argparse
import ast
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT = os.path.dirname(HERE)
DEFAULT_DIRS = (".tools", "lib", "org/devices")
SKIP_DIRS = {"__pycache__", ".git", "node_modules", ".scratch"}
MAX_BYTES = 2 * 1024 * 1024
HASH_COMMENT_EXT = {".py", ".ps1", ".psm1", ".sh", ".bash", ".yaml", ".yml", ".toml", ".cfg", ".ini", ".txt", ".md", ""}
OPEN, CLOSE = "([{", ")]}"


def load_devices():
    spec = importlib.util.spec_from_file_location("opal_devices_for_census", os.path.join(DEFAULT_ROOT, "lib", "devices.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def box_tokens(reg: dict) -> dict:
    """lower-case token -> canonical box name, from the register's names and aliases (aliases under 3 characters dropped)."""
    out = {}
    for d in reg["devices"]:
        for t in [d["name"]] + list(d.get("aliases", [])):
            if len(t) >= 3 or t == d["name"]:
                out[t.lower()] = d["name"]
    return out


def alternation_re(tokens: dict):
    alt = "|".join(re.escape(t) for t in sorted(tokens, key=len, reverse=True))
    word = r"(?<![A-Za-z0-9_])(?:%s)(?![A-Za-z0-9_])" % alt
    return (re.compile(r"%s(?:\s*\|\s*%s)+" % (word, word), re.I),
            re.compile(r"\bin\s+(?:[\"']?%s[\"']?\s+)+[\"']?%s" % (word, word), re.I),
            re.compile(r"^\s*-\s*[\"']?%s[\"']?\s*$" % word, re.I | re.M))


def distinct(strings, tokens: dict) -> set:
    return {tokens[s.strip().lower()] for s in strings if isinstance(s, str) and s.strip().lower() in tokens}


# ---------------------------------------------------------------- python: by AST

def py_hits(src: str, tokens: dict, alt_res) -> list:
    """[(line, why)] for one python source. A container holding two distinct box tokens as direct string elements, a string
    constant that is a regex alternation of two, a `for x in a b` is not python. Docstrings are prose and are skipped."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return text_hits(src, ".sh", tokens, alt_res)
    doc_ids = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = getattr(node, "body", [])
            if body and isinstance(body[0], ast.Expr) and isinstance(getattr(body[0], "value", None), ast.Constant):
                doc_ids.add(id(body[0].value))
    hits = []
    for node in ast.walk(tree):
        elts = None
        if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
            elts = node.elts
        elif isinstance(node, ast.Dict):
            elts = [k for k in node.keys if k is not None]
            fields = [k for k in elts if isinstance(k, ast.Constant) and isinstance(k.value, str)
                      and re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", k.value)]
            if not fields:   # a lookup table's values are a list of boxes; a record's field values are data about one message
                elts += list(node.values)
        if elts is not None:
            found = distinct([e.value for e in elts if isinstance(e, ast.Constant)], tokens)
            if len(found) >= 2:
                hits.append((node.lineno, "literal list/dict of %s" % ",".join(sorted(found))))
        elif isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in doc_ids:
            m = alt_res[0].search(node.value)
            if m:
                hits.append((node.lineno, "regex alternation %r" % m.group(0)[:60]))
    return hits


# ---------------------------------------------------------------- everything else: bracket scan

def strip_comments(text: str, ext: str) -> str:
    if ext not in HASH_COMMENT_EXT:
        return text
    out, i, n, quote = [], 0, len(text), ""
    while i < n:
        c = text[i]
        if quote:
            out.append(c)
            if c == "\\" and i + 1 < n and quote == '"':
                out.append(text[i + 1])
                i += 1
            elif c == quote:
                quote = ""
        elif c in "\"'":
            quote = c
            out.append(c)
        elif c == "#" and (i == 0 or text[i - 1] in " \t\r\n;(,"):
            while i < n and text[i] != "\n":
                i += 1
            continue
        else:
            out.append(c)
        i += 1
    return "".join(out)


def text_hits(text: str, ext: str, tokens: dict, alt_res) -> list:
    clean = strip_comments(text, ext)
    hits = []
    for rx, why in ((alt_res[0], "alternation"), (alt_res[1], "shell for-in list")):
        for m in rx.finditer(clean):
            hits.append((clean.count("\n", 0, m.start()) + 1, "%s %r" % (why, m.group(0)[:60])))
    seen = []
    for m in alt_res[2].finditer(clean):
        seen.append((m.group(0).strip().lstrip("-").strip(" \"'").lower(), clean.count("\n", 0, m.start()) + 1))
    for k in range(len(seen) - 1):
        if seen[k][0] in tokens and seen[k + 1][0] in tokens and tokens[seen[k][0]] != tokens[seen[k + 1][0]] \
                and seen[k + 1][1] == seen[k][1] + 1:
            hits.append((seen[k][1], "yaml list"))
    stack, i, n, line = [(set(), 1, "")], 0, len(clean), 1
    while i < n:
        c = clean[i]
        if c == "\n":
            line += 1
        elif c in "\"'":
            j = i + 1
            while j < n and clean[j] != c and clean[j] != "\n":
                j += 2 if clean[j] == "\\" else 1
            body = clean[i + 1:j]
            if j < n and clean[j] == c and body.strip().lower() in tokens:
                is_key = re.match(r"\s*[:=]", clean[j + 1:j + 12]) is not None
                if stack[-1][2] != "{" or is_key:   # in braces only a KEY counts: a field's value naming a box is data
                    stack[-1][0].add(tokens[body.strip().lower()])
            i = j
        elif c in OPEN:
            stack.append((set(), line, c))
        elif c in CLOSE and len(stack) > 1:
            found, at, _open = stack.pop()
            if len(found) >= 2:
                hits.append((at, "bracketed list of %s" % ",".join(sorted(found))))
        i += 1
    return hits


def is_test(rel: str) -> bool:
    parts = rel.split("/")
    return "tests" in parts[:-1] or parts[-1].startswith("test_")


def census(root: str, register_file: str | None = None, dirs=DEFAULT_DIRS) -> dict:
    devices = load_devices()
    reg_path = register_file or str(devices.register_path())
    reg = devices.load(__import__("pathlib").Path(reg_path))
    tokens = box_tokens(reg)
    alt_res = alternation_re(tokens)
    reg_real = os.path.realpath(reg_path)
    scanned, listed, tests, skipped_register, unread = 0, {}, {}, [], []
    for d in dirs:
        base = os.path.join(root, *d.split("/"))
        for cur, subs, names in os.walk(base):
            subs[:] = sorted(s for s in subs if s not in SKIP_DIRS)
            for name in sorted(names):
                path = os.path.join(cur, name)
                rel = os.path.relpath(path, root).replace(os.sep, "/")
                if os.path.realpath(path) == reg_real:
                    skipped_register.append(rel)
                    continue
                try:
                    if os.path.getsize(path) > MAX_BYTES:
                        unread.append(rel)
                        continue
                    with open(path, "rb") as fh:
                        data = fh.read()
                except OSError:
                    unread.append(rel)
                    continue
                if b"\0" in data[:8192]:
                    continue
                scanned += 1
                text = data.decode("utf-8", "replace")
                ext = os.path.splitext(name)[1].lower()
                hits = py_hits(text, tokens, alt_res) if ext == ".py" else text_hits(text, ext, tokens, alt_res)
                if hits:
                    (tests if is_test(rel) else listed)[rel] = sorted(set(hits))
    return {"scanned": scanned, "listed": listed, "tests": tests, "register": skipped_register, "unread": unread,
            "tokens": sorted(tokens), "register_path": reg_path}


def main(argv: list) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=DEFAULT_ROOT)
    ap.add_argument("--register", default=None, help="a register file other than the live one (fixtures and proofs only)")
    ap.add_argument("--dirs", default=",".join(DEFAULT_DIRS))
    a = ap.parse_args(argv)
    try:
        res = census(os.path.abspath(a.root), a.register, tuple(x for x in a.dirs.split(",") if x))
    except Exception as exc:  # noqa: BLE001
        print("ERROR: census could not read the register (%s)" % exc, file=sys.stderr)
        return 3
    print("register: %s  tokens (%d): %s" % (res["register_path"], len(res["tokens"]), ", ".join(res["tokens"])))
    print("register file skipped (the one place a list is allowed): %s" % (", ".join(res["register"]) or "-"))
    if res["unread"]:
        print("UNREAD (over %d bytes or unreadable): %s" % (MAX_BYTES, ", ".join(res["unread"])))
    for rel, hits in sorted(res["tests"].items()):
        print("TEST (not counted): %s  %s" % (rel, "; ".join("L%d %s" % h for h in hits[:3])))
    for rel, hits in sorted(res["listed"].items()):
        for ln, why in hits:
            print("HAND-LISTED %s:%d  %s" % (rel, ln, why))
    files = sorted(res["listed"])
    print("tests_with_lists=%d (listed apart)" % len(res["tests"]))
    print("BOX-LIST-CENSUS scanned=%d hand_listed=%d files=%s" % (res["scanned"], len(files), ",".join(files) or "-"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
