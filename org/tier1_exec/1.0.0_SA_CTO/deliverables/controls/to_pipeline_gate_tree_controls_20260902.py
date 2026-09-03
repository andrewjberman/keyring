"""Controls for to-pipeline-gate.py TWO-ROOT resolution -- project-tree spec s.7/s.8 prerequisite 5
(Andrew-direct 2026-09-02 ~21:0xZ via 2.0.0_SA_COO @a8d63f097c: "Project tree prereq builds are
mandatory start point ... split up work with CTO"). Grammar from org/standards/PROJECT_TREE.contract.json.

A TEMP ROOT is built with both roots populated (a FLAT project in org/projects/ + seat task_orders/,
and a TREE project under org/missions/D8/ETFS/) and the gate's pure functions are called against it.
Limb 5's staged-index reader is monkeypatched to read the temp root's files, as the limb-5 harness
does. GATE_PATH points the harness at an older gate for red-first (HEAD before the resolver: no
_project_row_rel, discovery blind to task-orders/, the walk-back live).

Written by a non-shell writer only (the heredoc backslash trap is in this estate's memory).
"""
import importlib.util
import json
import os
import re
import shutil
import sys
import tempfile

GATE_PATH = os.environ.get("GATE_PATH", ".tools/to-pipeline-gate.py")
_spec = importlib.util.spec_from_file_location("togate_tree", GATE_PATH)
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)

REAL_PRD = "docs/architecture/ETFS_GUARDRAIL_PRD.md"
TREE = "org/missions/D8/ETFS/ETFS_GUARDRAIL"          # the spec's own water test #2 layout
TREE_TO = TREE + "/task-orders/ETFS_GUARDRAIL.TO-TREE1.md"
TREE_TO_WRONG_FOLDER = "org/missions/D8/ETFS/ETFS_OTHERPRJ/task-orders/ETFS_GUARDRAIL.TO-TREE2.md"
TREE_TO_UNDERSCORE = TREE + "/task_orders/ETFS_GUARDRAIL.TO-TREE3.md"
FLAT_TO = "org/tier1_exec/2.0.0_SA_COO/task_orders/FLATPROJ.TO-FLAT1.md"
WALKBACK_TO = "org/tier1_exec/2.0.0_SA_COO/task_orders/FLATPROJ_SUB.TO-FLAT2.md"   # only FLATPROJ.json exists
TO_BODY = "<decomp_ref>decompositions/round1.md</decomp_ref>\n<preflight>\n</preflight>\n<status>OPEN</status>\n"
TO_DONE = TO_BODY.replace("<status>OPEN</status>", "<status>COMPLETE</status>")


def _w(root, rel, text):
    p = os.path.join(root, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def build_root():
    root = tempfile.mkdtemp(prefix="togate-tree-")
    prd = open(REAL_PRD, encoding="utf-8").read()
    hdr = json.loads(re.search(r"```json\s*(.*?)```", prd, re.S).group(1))
    row_tree = {"project_code": "ETFS_GUARDRAIL", "macro_code": "ETFS", "directive": hdr["directive"],
                "fabric": hdr["fabric"], "dep_stage": "DECOMP", "status": "ACTIVE",
                "prds": [TREE + "/prd/ETFS_GUARDRAIL_PRD.md"]}
    _w(root, TREE + "/project.json", json.dumps(row_tree, indent=2))
    _w(root, TREE + "/prd/ETFS_GUARDRAIL_PRD.md", prd)
    _w(root, TREE_TO, TO_BODY)
    _w(root, TREE_TO_WRONG_FOLDER, TO_BODY)
    _w(root, "org/missions/D8/ETFS/ETFS_OTHERPRJ/project.json", json.dumps(dict(row_tree, project_code="ETFS_OTHERPRJ")))
    # R-iv (CVO review @580c4f72a2): a folder whose ROW claims another project_code
    _w(root, "org/missions/D8/ETFS/ETFS_MISMATCH/project.json", json.dumps(dict(row_tree, project_code="ETFS_OTHERCODE")))
    _w(root, "org/missions/D8/ETFS/ETFS_MISMATCH/task-orders/ETFS_MISMATCH.TO-M.md", TO_BODY)
    _w(root, TREE_TO_UNDERSCORE, TO_BODY)
    _w(root, "org/projects/FLATPROJ.json", json.dumps({"project_code": "FLATPROJ", "dep_stage": "DECOMP",
                                                       "directive": "D8", "fabric": "laptop"}))
    _w(root, FLAT_TO, TO_BODY)
    _w(root, WALKBACK_TO, TO_BODY)
    _w(root, "org/standards/PRD_HEADER.schema.json", open("org/standards/PRD_HEADER.schema.json", encoding="utf-8").read())
    return root


def _line(ok, got, want, name):
    print("  %-7s %-6s->%-6s  %s" % ("OK" if ok else "DEFECT", got, want, name))
    return 0 if ok else 1


def main():
    root = build_root()
    fails = 0
    try:
        # ---- DISCOVERY ----
        for name, rel, want in [
            ("discovery: tree task-orders/ path IS a TO", TREE_TO, True),
            ("discovery: flat task_orders/ path IS a TO", FLAT_TO, True),
            ("discovery: tree prd/ path is NOT a TO", TREE + "/prd/ETFS_GUARDRAIL_PRD.md", False),
            ("discovery: tree path with a non-D directive folder is NOT a tree TO", "org/missions/OPS/ETFS/X/task-orders/X.TO-1.md", False),
        ]:
            got = bool(gate.TO_PATH_RE.search(rel))
            fails += _line(got == want, str(got), str(want), name)

        # ---- RESOLVER ----
        if not hasattr(gate, "_project_row_rel"):
            print("  DEFECT  gate has no _project_row_rel -- one resolver for two roots is absent (4 cases)")
            fails += 4
        else:
            for name, rel, want_json, want_err in [
                ("resolver: tree TO -> ../project.json, derived from the PATH", TREE_TO, TREE + "/project.json", False),
                ("resolver: flat TO -> org/projects/<CODE>.json, exact code", FLAT_TO, "org/projects/FLATPROJ.json", False),
                ("resolver: tree TO filed under ANOTHER project's folder -> identity error", TREE_TO_WRONG_FOLDER, None, True),
                ("resolver: FLATPROJ_SUB resolves to ITS OWN row path, never walked back to FLATPROJ", WALKBACK_TO, "org/projects/FLATPROJ_SUB.json", False),
                ("resolver R-iv: the tree ROW says project_code ETFS_OTHERCODE in folder ETFS_MISMATCH -> identity error",
                 "org/missions/D8/ETFS/ETFS_MISMATCH/task-orders/ETFS_MISMATCH.TO-M.md", None, True),
            ]:
                code, rel_json, err = gate._project_row_rel(root, rel)
                ok = (rel_json == want_json) and (bool(err) == want_err)
                fails += _line(ok, str(rel_json), str(want_json), name)

        # ---- LAYER 3 ----
        for name, rel, want, must_contain in [
            ("L3: tree TO against the tree row -> PASS", TREE_TO, "PASS", ""),
            ("L3: flat TO against the flat row -> PASS", FLAT_TO, "PASS", ""),
            ("L3: walk-back candidate (no FLATPROJ_SUB.json) -> REFUSE, no walk-back", WALKBACK_TO, "REFUSE", "no walk-back"),
            ("L3: tree TO in the wrong project folder -> REFUSE naming the folder", TREE_TO_WRONG_FOLDER, "REFUSE", "tree folder"),
            ("L3: task_orders/ (underscore) INSIDE the tree is read as a flat TO -> REFUSE (no flat row)", TREE_TO_UNDERSCORE, "REFUSE", "org/projects/ETFS_GUARDRAIL.json"),
            ("L3 R-iv: row.project_code != folder -> REFUSE naming both carriers",
             "org/missions/D8/ETFS/ETFS_MISMATCH/task-orders/ETFS_MISMATCH.TO-M.md", "REFUSE", "project_code"),
        ]:
            v = gate.check_project_stage(root, rel)
            got = "PASS" if not v else "REFUSE"
            ok = got == want and (not must_contain or any(must_contain in x for x in v))
            fails += _line(ok, got, want, name)
            if not ok and v:
                print("           first: %s" % v[0][:120])

        # ---- LIMB 4 (ENDPOINT via the tree row's prds) ----
        v, n = gate.check_endpoint_section(root, TREE_TO)
        fails += _line(not v and bool(n), "PASS" if not v else "REFUSE", "PASS", "L4: tree TO -> its PRD (from the tree row) carries the ENDPOINT -> PASS with a note")
        prd_path = os.path.join(root, TREE, "prd", "ETFS_GUARDRAIL_PRD.md")
        prd_txt = open(prd_path, encoding="utf-8").read()
        _w(root, TREE + "/prd/ETFS_GUARDRAIL_PRD.md", prd_txt.replace("## ENDPOINT (step 2, /endpoint --forward)", "## ENDPOINT-REMOVED"))
        v, n = gate.check_endpoint_section(root, TREE_TO)
        fails += _line(bool(v), "REFUSE" if v else "PASS", "REFUSE", "L4: tree PRD with the ENDPOINT heading removed -> REFUSE")
        _w(root, TREE + "/prd/ETFS_GUARDRAIL_PRD.md", prd_txt)

        # ---- LIMB 5 (staged-index read, patched to the temp root) ----
        real = gate._staged_blob

        def from_root(root_, rel_):
            p = os.path.join(root_, rel_)
            return open(p, encoding="utf-8").read() if os.path.isfile(p) else None
        gate._staged_blob = from_root
        try:
            v, n = gate.check_prd_conformance(root, TREE_TO)
            fails += _line(not v and n and "graded 1" in n[0], "PASS" if not v else "REFUSE", "PASS", "L5: tree TO -> tree row (project_code/directive/fabric) vs PRD_HEADER -> graded 1, PASS")

            def drifted(root_, rel_):
                txt = from_root(root_, rel_)
                if rel_.endswith("/project.json") and txt:
                    return json.dumps(dict(json.loads(txt), directive="D9"))
                return txt
            gate._staged_blob = drifted
            v, n = gate.check_prd_conformance(root, TREE_TO)
            fails += _line(any("D9" in x for x in v), "REFUSE" if v else "PASS", "REFUSE", "L5: tree row says D9 (staged), header says D8 -> REFUSE")

            # ---- COMPLETE FLIP: deliverables/<serial>/ (ruled). The flip limb reads the TO from the
            # STAGED index, so it runs under the same patched reader -- outside it the limb returns
            # early as "not a flip" and both cases below read FOUND (the first cut of this harness).
            gate._staged_blob = from_root
            _w(root, TREE_TO, TO_DONE)
            _w(root, TREE + "/deliverables/1.0.0_SA_CTO/ETFS_GUARDRAIL.TO-TREE1.proof_of_spec.json", "{}")
            v = gate.check_complete_flip(root, TREE_TO)
            found = bool(v) and not any("NO proof-of-spec instance" in x for x in v)
            fails += _line(found, "FOUND" if found else "MISSING", "FOUND", "flip: tree TO flips COMPLETE; proof under deliverables/<serial>/ is FOUND (its validation is the next limb, which then reports)")
            os.remove(os.path.join(root, TREE, "deliverables", "1.0.0_SA_CTO", "ETFS_GUARDRAIL.TO-TREE1.proof_of_spec.json"))
            _w(root, TREE + "/deliverables/ETFS_GUARDRAIL.TO-TREE1.proof_of_spec.json", "{}")
            v = gate.check_complete_flip(root, TREE_TO)
            missing = any("NO proof-of-spec instance" in x for x in v)
            fails += _line(missing, "MISSING" if missing else "FOUND", "MISSING", "flip: proof directly under deliverables/ (no serial folder) is NOT found -- the ruled layout is the lookup")
        finally:
            gate._staged_blob = real
    finally:
        shutil.rmtree(root, ignore_errors=True)
    print("DEFECTS: %d  (gate under test: %s)" % (fails, GATE_PATH))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
