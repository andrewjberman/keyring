#!/usr/bin/env python3
"""test_round_close_decomp_round.py -- round-close-check scopes an order to the round its decomposition names (CT-af-2).

Standard library only. Every fixture is a temporary directory under the system temp; no AWS, no network, no git.
Arms (each prints PASS or FAIL):
  a  a tree order tagged <round>3</round> whose <decomp_doc> names ...round15.md is counted by --round 15, not --round 3
  b  a tree order with no <decomp_ref> and <round>3</round> is still counted by --round 3 (fallback to the tag)
  c  a tree order whose decomp file name has no roundN falls back to its tag (counted by --round 3, not 15)
  d  a seat-folder order with no <round> tag is counted in every round and named untagged
  e  two tree orders of different decomposition rounds are each counted only in their own round
  f  the new TREE line prints "0 ()" for a round with no decomposition-scoped tree order

    python .tools/tests/test_round_close_decomp_round.py

LAST line (always): ROUND-CLOSE-DECOMP-ROUND arms=<k>/<n> ok=<True|False>
"""
import importlib.util
import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
CHECK = os.path.join(TOOLS, "round-close-check.py")
SEAT = os.path.join(TOOLS, "seat-list.py")
CODE = "TEST_PROJ"
BASE = "org/missions/D0/TEST/TEST_PROJ"
THIS_BOX = "TESTBOX"
DECOMP_DIR = BASE + "/decompositions/"


def load_mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rcc = load_mod("rcc_decomp_round_test", CHECK)
sl = load_mod("seat_list_decomp_round_test", SEAT)
KIND_OF = sl.kind_resolver()


def write(root, rel, text):
    path = os.path.join(root, rel.replace("/", os.sep))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def order(to, tag=None, decomp=None, issued_by="2.0.0_SA_COO~C"):
    parts = ["# TO", "<to_id>%s.TO-%s</to_id>" % (CODE, to), "<issued_to>0.9.0_WK_TEST_PROJ~1</issued_to>"]
    if issued_by:
        parts.append("<issued_by>%s</issued_by>" % issued_by)
    parts.append("<status>issued</status>")
    if tag is not None:
        parts.append("<round>%s</round>" % tag)
    if decomp is not None:
        parts.append("<decomp_ref>")
        parts.append("<decomp_doc>%s</decomp_doc>" % decomp)
        parts.append("<owned_cells>X</owned_cells>")
        parts.append("</decomp_ref>")
    return "\n".join(parts) + "\n"


def build(root):
    write(root, BASE + "/project.json", '{"project_code": "TEST_PROJ", "macro_code": "TEST"}')
    write(root, "org/mcp/liveness.json", "{}")
    tree = BASE + "/task-orders/"
    write(root, tree + "TEST_PROJ.TO-A.a.md", order("A", tag="3", decomp=DECOMP_DIR + "TEST_PROJ_DECOMP.round15.md"))
    write(root, tree + "TEST_PROJ.TO-B.b.md", order("B", tag="3"))
    write(root, tree + "TEST_PROJ.TO-C.c.md", order("C", tag="3", decomp=DECOMP_DIR + "TEST_PROJ_DECOMP.final.md"))
    write(root, tree + "TEST_PROJ.TO-E.e.md", order("E", tag="2", decomp=DECOMP_DIR + "TEST_PROJ_DECOMP.round7.md"))
    write(root, tree + "TEST_PROJ.TO-F.f.md", order("F", tag="2", decomp=DECOMP_DIR + "TEST_PROJ_DECOMP.round9.md"))
    # a seat-folder order with NO <round> tag and no decomposition: the untagged rule (counted in every round, named)
    write(root, "org/tier2/0.7.0_AE_TEST~Y/task_orders/TEST_PROJ.TO-D.d.md", order("D", tag=None, issued_by=None))


def counted(root, rnd):
    src = rcc.WorkTree(root)
    proj = src.project_dir(CODE)
    return {o["id"].split(".")[-1]: o for o in rcc.read_orders(src, proj, rnd, None)}


def check_lines(root, rnd):
    lines, _last = rcc.check(root, sl, sl.Ctx(root), CODE, rnd, None, THIS_BOX, THIS_BOX, KIND_OF, strict_grades=True)
    return lines


def tree_line(lines):
    hits = [ln.strip() for ln in lines if ln.strip().startswith("TREE orders counted by decomposition round:")]
    return hits[0] if len(hits) == 1 else None


def main():
    root = tempfile.mkdtemp(prefix="rcc_decomp_round_test_")
    arms = []
    try:
        build(root)
        r15, r3, r7, r9, r2 = (str(x) for x in (15, 3, 7, 9, 2))
        c15, c3, c7, c9 = counted(root, r15), counted(root, r3), counted(root, r7), counted(root, r9)
        l15, l3, l2 = check_lines(root, r15), check_lines(root, r3), check_lines(root, r2)

        # (a)
        a = ("TO-A" in c15 and "TO-A" not in c3 and tree_line(l15) == "TREE orders counted by decomposition round: 1 (TO-A)")
        arms.append(("a decomp round15 beats tag 3", a, "15 has TO-A=%s, 3 has TO-A=%s, line=%r" % (
            "TO-A" in c15, "TO-A" in c3, tree_line(l15))))
        # (b)
        b = ("TO-B" in c3 and "TO-B" not in c15)
        arms.append(("b no decomp_ref falls back to tag", b, "3 has TO-B=%s, 15 has TO-B=%s" % ("TO-B" in c3, "TO-B" in c15)))
        # (c)
        cc = ("TO-C" in c3 and "TO-C" not in c15 and tree_line(l3) == "TREE orders counted by decomposition round: 0 ()")
        arms.append(("c decomp name without roundN falls back to tag", cc, "3 has TO-C=%s, 15 has TO-C=%s, line=%r" % (
            "TO-C" in c3, "TO-C" in c15, tree_line(l3))))
        # (d)
        d = all(("TO-D" in c) and c["TO-D"].get("untagged") for c in (c15, c3, c7))
        d = d and any("carry NO <round> tag and are counted in EVERY" in ln for ln in l15)
        arms.append(("d untagged seat-folder order counted in every round and named", d,
                     "in 15/3/7 untagged=%s; named line present=%s" % (
                         [("TO-D" in c and bool(c["TO-D"].get("untagged"))) for c in (c15, c3, c7)],
                         any("carry NO <round> tag and are counted in EVERY" in ln for ln in l15))))
        # (e)
        e = ("TO-E" in c7 and "TO-E" not in c9 and "TO-F" in c9 and "TO-F" not in c7
             and tree_line(check_lines(root, r7)) == "TREE orders counted by decomposition round: 1 (TO-E)"
             and tree_line(check_lines(root, r9)) == "TREE orders counted by decomposition round: 1 (TO-F)")
        arms.append(("e two decomp rounds each counted only in its own", e,
                     "7 has E/F=%s/%s, 9 has E/F=%s/%s" % ("TO-E" in c7, "TO-F" in c7, "TO-E" in c9, "TO-F" in c9)))
        # (f)
        f = tree_line(l2) == "TREE orders counted by decomposition round: 0 ()"
        arms.append(("f round with no decomposition-scoped order prints 0 ()", f, "line for round 2=%r" % tree_line(l2)))
    finally:
        shutil.rmtree(root, ignore_errors=True)
    for name, ok, detail in arms:
        print("%s  %s  (%s)" % ("PASS" if ok else "FAIL", name, detail))
    k = sum(1 for _n, ok, _d in arms if ok)
    ok_all = k == len(arms)
    print("ROUND-CLOSE-DECOMP-ROUND arms=%d/%d ok=%s" % (k, len(arms), ok_all))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
