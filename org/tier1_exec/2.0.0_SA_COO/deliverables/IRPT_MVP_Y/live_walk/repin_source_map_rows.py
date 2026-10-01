#!/usr/bin/env python3
"""Re-pin EVERY staged member of the named functions' source-map rows to ONE commit (the whole-bundle rule).

    python repin_source_map_rows.py <repo-root> <commit> <function> [<function> ...] [--write]

CTO rulings batch 61 item 3 and batch 62 item 6: a function whose bundle would mix vintages moves as a whole bundle
at one commit. For each named function this sets every `staged_from` entry's `pin` to <commit> and its `sha256` to
the sha256 of `git show <commit>:<repo_path>` (the bytes build-and-upload.sh verifies before it stages a member).

The edit is TEXTUAL and ROW-SCOPED: only the `pin` and `sha256` values inside the named functions' `staged_from`
lists change; every other byte of lambda-source-map.json, every other function's row included, is left as it is
(the lane grant covers these rows only). Without --write it prints what would change and writes nothing.
Prints, per function: entries, entries whose bytes change, entries whose pin alone moves. ASCII only.
"""
import hashlib
import io
import json
import re
import subprocess
import sys

MAP = "infra/aws/lambda/ci/lambda-source-map.json"
ENTRY = re.compile(r"\{[^{}]*\}")


def span_of_list(text, start):
    """(open, close) offsets of the JSON list whose '[' is the first one at or after `start`."""
    i = text.index("[", start)
    depth, j = 0, i
    while True:
        ch = text[j]
        if ch == "[":
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                return i, j + 1
        j += 1


def main(argv):
    write = "--write" in argv
    args = [a for a in argv[1:] if a != "--write"]
    root, commit, functions = args[0], args[1], args[2:]
    commit = subprocess.run(["git", "-C", root, "rev-parse", commit], capture_output=True, text=True,
                            check=True).stdout.strip()
    path = root.rstrip("/\\") + "/" + MAP
    text = io.open(path, encoding="utf-8", newline="").read()
    before = json.loads(text)
    for fn in functions:
        key = '"%s": {' % fn
        if text.count(key) != 1:
            raise SystemExit("ERROR: %d rows named %s" % (text.count(key), fn))
        row_start = text.index(key)
        a, b = span_of_list(text, text.index('"staged_from"', row_start))
        block = text[a:b]
        moved = changed = total = 0

        def repin(match):
            nonlocal moved, changed, total
            entry = json.loads(match.group(0))
            total += 1
            blob = subprocess.run(["git", "-C", root, "show", "%s:%s" % (commit, entry["repo_path"])],
                                  capture_output=True)
            if blob.returncode != 0:
                raise SystemExit("ERROR: %s does not exist at %s" % (entry["repo_path"], commit[:10]))
            digest = hashlib.sha256(blob.stdout).hexdigest()
            out = match.group(0)
            if entry.get("sha256") != digest:
                changed += 1
            if entry.get("pin") != commit:
                moved += 1
            out, n1 = re.subn(r'("pin":\s*")[^"]*(")', lambda m: m.group(1) + commit + m.group(2), out, count=1)
            out, n2 = re.subn(r'("sha256":\s*")[^"]*(")', lambda m: m.group(1) + digest + m.group(2), out, count=1)
            if n1 != 1 or n2 != 1:
                raise SystemExit("ERROR: entry for %s carries no pin or no sha256" % entry["repo_path"])
            return out

        text = text[:a] + ENTRY.sub(repin, block) + text[b:]
        print("%-24s staged entries %d; bytes change in %d; pin moves in %d; all now at %s"
              % (fn, total, changed, moved, commit[:10]))
    after = json.loads(text)
    rows = before.get("functions", before)
    untouched = sum(1 for k in rows if k not in functions and rows[k] == after.get("functions", after)[k])
    print("other rows byte-compared as JSON: %d of %d unchanged" % (untouched, len(rows) - len(functions)))
    for fn in functions:
        b_row, a_row = dict(rows[fn]), dict(after.get("functions", after)[fn])
        b_row.pop("staged_from", None), a_row.pop("staged_from", None)
        if b_row != a_row:
            raise SystemExit("ERROR: a field outside staged_from moved in " + fn)
    if write:
        io.open(path, "w", encoding="utf-8", newline="").write(text)
        print("written:", MAP)
    else:
        print("dry run: nothing written")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
