"""Controls for surprise-row-gate.py TWO-ROOT channel paths -- project-tree spec s.7 prerequisite 5.
Grammar from org/standards/PROJECT_TREE.contract.json (surprise_channel_glob). The gate's blob reader
is monkeypatched so a tree file can be graded as STAGED-and-new without staging anything. The row
used is a REAL, schema-valid row from the live corpus with its identity re-pointed at the tree
project, so a refusal here is the new limb's and not a schema accident.

Written by a non-shell writer only.
"""
import importlib.util
import json
import os
import re
import sys

GATE_PATH = os.environ.get("GATE_PATH", ".tools/surprise-row-gate.py")
_spec = importlib.util.spec_from_file_location("srg_tree", GATE_PATH)
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)

TREE = "org/missions/D8/ETFS/ETFS_GUARDRAIL/surprise-channel"
INV = TREE + "/investigations/INVESTIGATION_v1.md"
REM = TREE + "/remediations/REMEDIATION_v1.md"
MISFILED = TREE + "/investigations/REMEDIATION_v1.md"


def _real_row():
    """A live investigation row re-identified as ETFS_GUARDRAIL-S1 / laptop, PLUS the two step-7
    trigger halves the gate requires on a NEW row. MEASURED 2026-09-02: 0 of 191 corpus rows carry
    spec_asserts/world_is -- every one predates the rule that requires them on new rows -- so no
    borrowed row is gate-valid as new on its own. The fixture is therefore real-row + the two
    required-on-new fields, and a refusal below is the new limb's, not a trigger-field accident."""
    txt = open("org/surprise_channel/ADVI_PERFRP/INVESTIGATION_v1.md", encoding="utf-8").read()
    for blk in re.findall(r"```json\s*(.*?)```", txt, re.S):
        try:
            d = json.loads(blk)
        except ValueError:
            continue
        rows = d if isinstance(d, list) else [d]
        for r in rows:
            if isinstance(r, dict) and r.get("id"):
                r = dict(r)
                r["id"] = "ETFS_GUARDRAIL-S1"
                r["project"] = "ETFS_GUARDRAIL"
                r["fabric"] = "laptop"
                r["spec_asserts"] = "the TO said the coverage gate reads one root (org/projects/) for every project"
                r["world_is"] = "the project tree adds a second root and the gate was blind to it until the repoint"
                r["hazard_standing"] = "INERT"   # ARMED would require a disarm_owner; not the property under test
                return r
    raise SystemExit("precondition: no row found in ADVI_PERFRP/INVESTIGATION_v1.md")


def _doc(row):
    return "# INVESTIGATION\n\n```json\n" + json.dumps(row, indent=2) + "\n```\n"


def _line(ok, got, want, name):
    print("  %-7s %-6s->%-6s  %s" % ("OK" if ok else "DEFECT", got, want, name))
    return 0 if ok else 1


def main():
    fails = 0
    # ---- PATH GRAMMAR ----
    for name, rel, want in [
        ("CHANNEL_RE: tree investigations path IS a channel file", INV, True),
        ("CHANNEL_RE: tree remediations path IS a channel file", REM, True),
        ("CHANNEL_RE: flat path still IS a channel file", "org/surprise_channel/ADVI_PERFRP/INVESTIGATION_v1.md", True),
        ("CHANNEL_RE: non-D directive folder is NOT", "org/missions/OPS/ETFS/X/surprise-channel/investigations/INVESTIGATION_v1.md", False),
        ("CHANNEL_RE: a tree file outside surprise-channel/ is NOT", "org/missions/D8/ETFS/X/deliverables/INVESTIGATION_v1.md", False),
    ]:
        got = bool(gate.CHANNEL_RE.search(rel))
        fails += _line(got == want, str(got), str(want), name)
    if not hasattr(gate, "_folder_identity"):
        print("  DEFECT  gate has no _folder_identity -- the path is not read as membership (3 cases)")
        fails += 3
    else:
        for name, rel, want in [
            ("_folder_identity: tree -> (ETFS_GUARDRAIL, INVESTIGATION)", INV, ("ETFS_GUARDRAIL", "INVESTIGATION")),
            ("_folder_identity: tree remediations -> (ETFS_GUARDRAIL, REMEDIATION)", REM, ("ETFS_GUARDRAIL", "REMEDIATION")),
            ("_folder_identity: flat -> (ADVI_PERFRP, None)", "org/surprise_channel/ADVI_PERFRP/INVESTIGATION_v1.md", ("ADVI_PERFRP", None)),
        ]:
            got = gate._folder_identity(rel)
            fails += _line(got == want, str(got), str(want), name)

    # ---- GATE ON A TREE FILE (staged + new) ----
    row = _real_row()
    real_blob = gate._blob
    docs = {}

    def fake_blob(root, ref, rel):
        # Synthetic docs: staged = the text, HEAD = absent (a NEW file). Everything else -- the
        # schemas the gate reads through this same function -- goes to the REAL index reader. The
        # first cut returned ABSENT for the schema too and every case refused "schema unreadable".
        if rel in docs:
            return ("ABSENT", None) if ref == "HEAD" else ("OK", docs[rel])
        return real_blob(root, ref, rel)
    gate._blob = fake_blob
    try:
        root = os.path.abspath(".")
        docs[INV] = _doc(row)
        v, n = gate.check_file(root, INV)
        fails += _line(not v, "PASS" if not v else "REFUSE", "PASS", "tree investigations file, row project == folder -> PASS")
        if v:
            print("           first: %s" % v[0][:140])
        docs[INV] = _doc(dict(row, project="ETFS_OTHERPRJ", id="ETFS_OTHERPRJ-S1"))
        v, n = gate.check_file(root, INV)
        fails += _line(any("folder" in x for x in v), "REFUSE" if v else "PASS", "REFUSE", "tree file whose row says ANOTHER project -> REFUSE naming the folder")
        docs[MISFILED] = _doc(row)
        v, n = gate.check_file(root, MISFILED)
        fails += _line(any("sub-folder" in x for x in v), "REFUSE" if v else "PASS", "REFUSE", "a REMEDIATION file filed under investigations/ -> REFUSE (path kind vs filename kind)")
        flat = "org/surprise_channel/ADVI_PERFRP/INVESTIGATION_v9.md"
        docs[flat] = _doc(dict(row, project="ETFS_GUARDRAIL"))
        v, n = gate.check_file(root, flat)
        fails += _line(any("folder" in x for x in v), "REFUSE" if v else "PASS", "REFUSE", "FLAT file in ADVI_PERFRP/ carrying an ETFS_GUARDRAIL row -> REFUSE (the limb binds both roots)")
    finally:
        gate._blob = real_blob
    print("DEFECTS: %d  (gate under test: %s)" % (fails, GATE_PATH))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
