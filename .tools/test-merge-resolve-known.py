"""Arms for .tools/merge-resolve-known.py union_rows / fenced_list. USAGE: python .tools/test-merge-resolve-known.py
Owner 4.0.0_SA_CRO~A."""
import importlib.util
import json
import os
import sys

spec = importlib.util.spec_from_file_location("mrk", os.path.join(os.path.dirname(os.path.abspath(__file__)), "merge-resolve-known.py"))
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def doc(rows, pre="# T\n\n## Row context\n\ntext\n\n", post="\n"):
    body = ",\n".join("    " + json.dumps(r, indent=2).replace("\n", "\n    ") for r in rows)
    return pre + "```json\n  [\n" + body + "\n  ]\n```" + post


def ids(text):
    return [k[0] for k, _, _ in m.fenced_list(text)[2]]


A, B, C = {"id": "P-S1", "v": 1}, {"id": "P-S2", "v": 2}, {"id": "P-S3", "v": 3}
fails = 0
arms = [
    ("identical sides -> unchanged bytes",
     lambda: m.union_rows(doc([A]), doc([A, B]), doc([A, B]))[0] == doc([A, B])),
    ("each side appends a different id -> both kept, base order then ours then theirs",
     lambda: ids(m.union_rows(doc([A]), doc([A, B]), doc([A, C]))[0]) == ["P-S1", "P-S2", "P-S3"]),
    ("one side edits a row, the other appends -> edit taken, append kept",
     lambda: (lambda t: ids(t) == ["P-S1", "P-S3"] and '"v": 9' in t)(
         m.union_rows(doc([A]), doc([dict(A, v=9)]), doc([A, C]))[0])),
    ("DUAL-MINT: the same new id with different content on each side -> both copies, ours then theirs",
     lambda: (lambda r: ids(r[0]) == ["P-S1", "P-S2", "P-S2"] and "dual-mint=P-S2" in r[1])(
         m.union_rows(doc([A]), doc([A, B]), doc([A, dict(B, v=7)])))),
    ("a dual-mint already in the file keys the same on every side -> a later merge resolves",
     lambda: ids(m.union_rows(doc([A, B, dict(B, v=7)]), doc([A, B, dict(B, v=7), C]), doc([A, B, dict(B, v=7)]))[0])
     == ["P-S1", "P-S2", "P-S2", "P-S3"]),
    ("an existing row changed differently on both sides -> UNRESOLVED",
     lambda: m.union_rows(doc([A]), doc([dict(A, v=8)]), doc([dict(A, v=9)]))[0] is None),
    ("the prose around the list changed differently on both sides -> UNRESOLVED",
     lambda: m.union_rows(doc([A]), doc([A], pre="# X\n\n"), doc([A], pre="# Y\n\n"))[0] is None),
    ("a file with TWO json fences is not a row list (the section union keeps it)",
     lambda: m.fenced_list(doc([A]) + "\n```json\n[]\n```\n") is None),
    ("a row with no id -> not a row list",
     lambda: m.fenced_list(doc([{"x": 1}])) is None),
    ("the file is new on both sides (no base), same content -> resolved",
     lambda: m.union_rows(None, doc([A]), doc([A]))[0] == doc([A])),
]
for name, fn in arms:
    try:
        ok = bool(fn())
    except Exception as e:  # noqa: BLE001
        ok, name = False, name + " (raised %r)" % e
    fails += not ok
    print(("PASS  " if ok else "FAIL  ") + name)
print("RESULT: %d of %d failed" % (fails, len(arms)))
sys.exit(1 if fails else 0)
