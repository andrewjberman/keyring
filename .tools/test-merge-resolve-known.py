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


def blk(items, pre="# T\n\nprose\n\n"):
    """One ```json block per row; each item is (heading or None, row or list of rows)."""
    out = pre
    for head, row in items:
        out += ("## %s -- a row\n\n" % head if head else "") + "```json\n" + json.dumps(row, indent=2) + "\n```\n\n"
    return out


def bids(text):
    return [k[0] for k, _ in m.fence_chunks(text)[1]]


A, B, C = {"id": "P-S1", "v": 1}, {"id": "P-S2", "v": 2}, {"id": "P-S3", "v": 3}
D = {"id": "P-S4", "v": 4}
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
    # ONE JSON BLOCK PER ROW, keyed by the id inside the block (IRPT_BCKEND reuses headings; NFRA_OPLGTW has none).
    ("BLOCKS: two rows under the SAME heading, each side appends a row -> both kept",
     lambda: bids(m.union_fences(blk([("H", A), ("H", B)]), blk([("H", A), ("H", B), ("X", C)]),
                                 blk([("H", A), ("H", B), ("Y", D)]))[0]) == ["P-S1", "P-S2", "P-S3", "P-S4"]),
    ("BLOCKS: no headings at all, each side appends -> both kept",
     lambda: bids(m.union_fences(blk([(None, A)]), blk([(None, A), (None, B)]), blk([(None, A), (None, C)]))[0])
     == ["P-S1", "P-S2", "P-S3"]),
    ("BLOCKS: a batch block (a list of rows) moves as one unit",
     lambda: bids(m.union_fences(blk([(None, [A, B])]), blk([(None, [A, B]), (None, C)]), blk([(None, [A, B])]))[0])
     == ["P-S1+P-S2", "P-S3"]),
    ("BLOCKS: the same new id with different content on each side -> DUAL-MINT, both kept",
     lambda: (lambda r: bids(r[0]) == ["P-S1", "P-S2", "P-S2"] and "dual-mint=P-S2" in r[1])(
         m.union_fences(blk([(None, A)]), blk([(None, A), (None, B)]), blk([(None, A), (None, dict(B, v=7))])))),
    ("BLOCKS: one row changed differently on both sides -> UNRESOLVED",
     lambda: m.union_fences(blk([(None, A)]), blk([(None, dict(A, v=8))]), blk([(None, dict(A, v=9))]))[0] is None),
    # APPEND-ONLY logs (0.0.0_AB_MSTR msgs 107817, 107847): a LINE UNION -- CLOUD's file, then the box-only lines.
    ("APPEND: both sides append, CLOUD is theirs -> CLOUD's file + box-only lines",
     lambda: m.union_append("a\nb\n", "a\nb\nBOX\n", "a\nb\nCLD\n", cloud="theirs")[0] == "a\nb\nCLD\nBOX\n"),
    ("APPEND: both sides append, CLOUD is ours (integrate) -> CLOUD's file + box-only lines",
     lambda: m.union_append("a\n", "a\nCLD\n", "a\nBOX1\nBOX2\n", cloud="ours")[0] == "a\nCLD\nBOX1\nBOX2\n"),
    ("APPEND: CLOUD's copy REORDERED by an earlier hand union (the dell1 HOLD) -> CLOUD's order kept, box-only appended",
     lambda: m.union_append("a\nb\n", "b\na\nC\n", "a\nb\nBOX\n", cloud="ours")[0] == "b\na\nC\nBOX\n"),
    ("APPEND: a CLOUD file with no final newline does not fuse with the box's first line",
     lambda: m.union_append("a\n", "a\nBOX\n", "a\nCLD", cloud="theirs")[0] == "a\nCLD\nBOX\n"),
    ("APPEND: a CRLF copy of a line CLOUD holds is the same line -> not duplicated",
     lambda: m.union_append(None, "a\r\nBOX\r\n", "a\n", cloud="theirs")[0] == "a\nBOX\r\n"),
    ("APPEND: a line the box holds twice and CLOUD once -> one copy added",
     lambda: m.union_append(None, "x\nx\n", "x\n", cloud="theirs")[0] == "x\nx\n"),
    # CROSS-ADJUDICATION records (laptop CTO ruling, MSTR LD-0650): an add/add equal after CRLF->LF and trailing-blank
    # normalisation resolves to CLOUD's copy; ANY other difference HOLDS.
    ("XADJ: add/add, CRLF plus one trailing blank line, CLOUD is theirs -> CLOUD's own bytes",
     lambda: m.resolve_xadj(None, "# X\n\nruled\n", "# X\r\n\r\nruled\r\n\r\n", cloud="theirs")[0] == "# X\r\n\r\nruled\r\n\r\n"),
    ("XADJ: same pair, CLOUD is ours -> CLOUD's (ours) bytes",
     lambda: m.resolve_xadj(None, "# X\r\n\r\nruled\r\n\r\n", "# X\n\nruled\n", cloud="ours")[0] == "# X\r\n\r\nruled\r\n\r\n"),
    ("XADJ: byte-identical copies -> resolved",
     lambda: m.resolve_xadj(None, "a\n", "a\n", cloud="theirs")[0] == "a\n"),
    ("XADJ: ONE CHANGED WORD -> HOLD (never auto-picked)",
     lambda: (lambda r: r[0] is None and "HOLD" in r[1])(m.resolve_xadj(None, "ruled yes\n", "ruled no\n", cloud="theirs"))),
    ("XADJ: a changed word hidden behind the CRLF difference -> still HOLD",
     lambda: m.resolve_xadj(None, "ruled yes\n", "ruled no\r\n", cloud="ours")[0] is None),
    ("XADJ: an extra non-blank line -> HOLD",
     lambda: m.resolve_xadj(None, "a\n", "a\nb\n", cloud="theirs")[0] is None),
    ("XADJ: --cloud not given -> HOLD (an add/add must know which side is CLOUD)",
     lambda: m.resolve_xadj(None, "a\n", "a\n", cloud=None)[0] is None),
    ("XADJ: a base exists (both sides edited) -> HOLD; only an add/add resolves",
     lambda: m.resolve_xadj("a\n", "a\nb\n", "a\nb\n", cloud="theirs")[0] is None),
    ("XADJ: absent on one side -> HOLD",
     lambda: m.resolve_xadj(None, None, "a\n", cloud="theirs")[0] is None),
    ("XADJ: the path class matches cross_adjudication/*.md and nothing else",
     lambda: bool(m.XADJ_RE.match("org/critical_paths/cross_adjudication/20261014T0552Z_XA-x.md"))
     and not m.XADJ_RE.match("org/critical_paths/cross_adjudication/sub/x.md")
     and not m.XADJ_RE.match("org/critical_paths/cross_adjudication/x.json")
     and not m.XADJ_RE.match("org/critical_paths/other/x.md")),
    ("APPEND: nothing is dropped -- every line of either side is in the result",
     lambda: (lambda r: all(x in r.splitlines() for x in ["q", "a", "b", "z"]))(
         m.union_append("a\nb\n", "a\nz\n", "q\na\nb\n", cloud="theirs")[0])),
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
