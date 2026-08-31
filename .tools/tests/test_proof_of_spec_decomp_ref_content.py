"""Controls for proof-of-spec-check's CONTENT-not-presence <decomp_ref> branch, the checker-vintage
line and the rc-named verdicts (2026-08-30, 1.0.0_SA_CTO~X on 1.0.0_SA_CTO 87900 items (1a)(1b)(1c)).

Every arm is reachable from a DIFFERENT truth:
  A1  a TO whose <decomp_ref> body reads "NONE -- ..." and whose criteria carry no cell_refs
      -> has_decomp_ref False, the branch reason names NONE (ANNOUNCE)          [the 87900 defect]
  A2  the SAME TO with a real decomp doc in the body -> has_decomp_ref True (ENFORCE) and the
      missing-cell_refs violation FIRES (the positive control that ENFORCE still enforces)
  A3  a NONE-word body that ALSO names a doc -> the doc wins (ENFORCE)
  A4  no <decomp_ref> element at all -> has_decomp_ref False, reason names the ABSENT element
  A5  the legacy presence semantics must not have leaked back: a body of only cell ids (no doc)
      is still ENFORCE (ids are a decomp claim)
  B1  iso_offset_to_utc_z("2026-08-30T01:00:15-04:00") == "2026-08-30T05:00:15Z"  [the 87900 instance]
  B2  a naive timestamp is NOT rendered with a Z
  C1  the verdict strings carry their rc

Run: python .tools/tests/test_proof_of_spec_decomp_ref_content.py   (exit 0 = all arms as expected)
"""
from __future__ import annotations

import importlib.util
import json as _json
import pathlib
import re
import subprocess
import sys
import tempfile

_SRC = pathlib.Path(__file__).resolve().parent.parent / "proof-of-spec-check.py"
_spec = importlib.util.spec_from_file_location("posc", _SRC)
posc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(posc)

results: list[tuple[str, bool, str]] = []


def arm(name: str, ok: bool, detail: str = "") -> None:
    results.append((name, ok, detail))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}  {detail}")


TO_NONE = """<task_order>
<authority>one-branch remediation under its own charter</authority>
<decomp_ref>NONE -- one-branch remediation under its own charter</decomp_ref>
<criteria>
<criterion id="RS-1">the thing</criterion>
<criterion id="RS-2">the other thing</criterion>
</criteria>
</task_order>
"""
TO_DOC = TO_NONE.replace(
    "<decomp_ref>NONE -- one-branch remediation under its own charter</decomp_ref>",
    "<decomp_ref><decomp_doc>workflows/atom_decomposition/runs/x/20260830T0000Z/DECOMP.md</decomp_doc>"
    "<owned_cells>L3S7B-1c16-1</owned_cells></decomp_ref>")
TO_NONE_PLUS_DOC = TO_NONE.replace(
    "<decomp_ref>NONE -- one-branch remediation under its own charter</decomp_ref>",
    "<decomp_ref>NONE at first glance <decomp_doc>workflows/atom_decomposition/runs/x/20260830T0000Z/DECOMP.md</decomp_doc></decomp_ref>")
TO_ABSENT = TO_NONE.replace("<decomp_ref>NONE -- one-branch remediation under its own charter</decomp_ref>\n", "")
TO_IDS_ONLY = TO_NONE.replace(
    "<decomp_ref>NONE -- one-branch remediation under its own charter</decomp_ref>",
    "<decomp_ref>cells L3S7B-1c16-1, L3S7B-1c16-3</decomp_ref>")

print("proof-of-spec-check CONTENT-not-presence / vintage / rc battery")

t = posc._parse_to(TO_NONE)
arm("A1 NONE body -> has_decomp_ref False", t["has_decomp_ref"] is False, repr(t["decomp_ref_branch_reason"]))
arm("A1 NONE body -> declares_none True and present True", t["decomp_ref_declares_none"] and t["decomp_ref_present"])
arm("A1 branch reason names NONE", "NONE" in t["decomp_ref_branch_reason"])
arm("A1 criteria without cell_refs are still REPORTED on the parse (not silently dropped)",
    t["criteria_without_cell_refs"] == ["RS-1", "RS-2"], str(t["criteria_without_cell_refs"]))

t2 = posc._parse_to(TO_DOC)
arm("A2 doc body -> has_decomp_ref True (ENFORCE)", t2["has_decomp_ref"] is True, repr(t2["decomp_ref_branch_reason"]))
arm("A2 doc body -> declares_none False", t2["decomp_ref_declares_none"] is False)
arm("A2 doc parsed", t2["decomp_doc"].endswith("DECOMP.md"), t2["decomp_doc"])

t3 = posc._parse_to(TO_NONE_PLUS_DOC)
arm("A3 NONE-word + doc -> the doc wins (ENFORCE)", t3["has_decomp_ref"] is True and "doc wins" in t3["decomp_ref_branch_reason"],
    repr(t3["decomp_ref_branch_reason"]))

t4 = posc._parse_to(TO_ABSENT)
arm("A4 absent element -> has_decomp_ref False, present False", t4["has_decomp_ref"] is False and t4["decomp_ref_present"] is False)
arm("A4 reason names the ABSENT element", "NO <decomp_ref>" in t4["decomp_ref_branch_reason"], repr(t4["decomp_ref_branch_reason"]))

t5 = posc._parse_to(TO_IDS_ONLY)
arm("A5 ids-only body (no doc) -> still ENFORCE (ids are a claim)", t5["has_decomp_ref"] is True and t5["declared_cells"] == ["L3S7B-1c16-1", "L3S7B-1c16-3"],
    str(t5["declared_cells"]))

# The ENFORCE limb must still fire on missing cell_refs: exercise alignment_check's branch text through
# the parse contract it reads. (The full alignment battery with a sealed workspace is
# test_proof_of_spec_alignment.py; this arm pins only the discriminator's polarity.)
arm("A2' ENFORCE would be asked to check cell_refs on the doc TO", t2["has_decomp_ref"] and t2["criteria_without_cell_refs"] == ["RS-1", "RS-2"])

arm("B1 -04:00 offset -> UTC Z", posc.iso_offset_to_utc_z("2026-08-30T01:00:15-04:00") == "2026-08-30T05:00:15Z",
    posc.iso_offset_to_utc_z("2026-08-30T01:00:15-04:00"))
arm("B1' +00:00 offset -> same instant with Z", posc.iso_offset_to_utc_z("2026-08-30T05:00:15+00:00") == "2026-08-30T05:00:15Z")
arm("B2 naive timestamp is NOT rendered with a Z", not posc.iso_offset_to_utc_z("2026-08-30T01:00:15").endswith("Z"),
    posc.iso_offset_to_utc_z("2026-08-30T01:00:15"))
arm("B2' garbage -> unparsed, not a crash", "unparsed" in posc.iso_offset_to_utc_z("not a date"))
v = posc.checker_vintage()
arm("B3 checker_vintage() renders `<hash10> <...Z>` or an UNREAD sentinel",
    bool(re.fullmatch(r"[0-9a-f]{10} \d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ(\+DIRTY\([^)]+\))?", v)) or v.startswith("UNREAD"), v)

# B4 (3.0.0_SA_CVO 88184): the vintage line must be true of the RUNNING bytes -- a dirty worktree copy of
# the checker carries +DIRTY(<n> lines); a clean one carries nothing. Exercised on a sealed temp repo file,
# never by dirtying the live checker.
with tempfile.TemporaryDirectory(prefix="posc_v_") as _td:
    _repo = pathlib.Path(_td)
    _g = lambda *a: subprocess.run(["git", *a], cwd=str(_repo), capture_output=True, text=True, check=True).stdout.strip()  # noqa: E731
    _g("init", "-q")
    _g("config", "user.email", "t@t")
    _g("config", "user.name", "t")
    (_repo / "tool.py").write_text("a\nb\n", encoding="utf-8")
    _g("add", ".")
    _g("commit", "-q", "-m", "A")
    arm("B4 clean worktree -> no DIRTY suffix", posc.worktree_dirty_suffix(_repo / "tool.py", _repo) == "", repr(posc.worktree_dirty_suffix(_repo / "tool.py", _repo)))
    (_repo / "tool.py").write_text("a\nb\nc\nd\n", encoding="utf-8")
    _s = posc.worktree_dirty_suffix(_repo / "tool.py", _repo)
    arm("B4' modified worktree -> +DIRTY(2 lines)", _s == "+DIRTY(2 lines)", _s)
    _s2 = posc.worktree_dirty_suffix(_repo / "nope.py", _repo)
    arm("B4'' untracked/absent path -> no false DIRTY (nothing to diff against HEAD)", _s2 == "", repr(_s2))
_live = posc.checker_vintage()
arm("B5 live vintage line is `<hash10> <Z>` optionally followed by +DIRTY(...) -- and says which",
    bool(re.fullmatch(r"[0-9a-f]{10} \d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ(\+DIRTY\([^)]+\))?", _live)) or _live.startswith("UNREAD"), _live)

src = _SRC.read_text(encoding="utf-8")
arm("C1 verdict lines name their rc", 'print("INVALID (rc=1)")' in src and 'print("VALID (rc=0)")' in src
    and 'USAGE-ERROR (rc=2)' in src and 'READ-ERROR (rc=2)' in src)

# D1 CORPUS ARM (2026-08-30): every cell id of the sec-7b certified rectangle at its pin must be harvestable.
# Before the L3S7B hex branch, 14 of 21 were invisible (the 7 m-cells matched through the legacy branch).
_R = "workflows/atom_decomposition/runs/nfra-c3materialize-L3/20260830T0852Z/rectangle.final.certified.json"
_o = subprocess.run(["git", "show", "391cd500e5:" + _R], capture_output=True)
if _o.returncode == 0:
    _ids = [c["cell_id"] for c in _json.loads(_o.stdout)["cells"]]
    _hit = [i for i in _ids if posc.CELL_ID_RE.fullmatch(i)]
    arm("D1 all 21 sec-7b cell ids at 391cd500e5 match CELL_ID_RE", len(_hit) == len(_ids) == 21, f"{len(_hit)} of {len(_ids)}")
    arm("D1' the harvest over the whole rectangle text finds exactly the 21 (no manufactured ids)",
        sorted(set(posc.CELL_ID_RE.findall(_o.stdout.decode("utf-8", "replace")))) == sorted(set(_ids)),
        str(sorted(set(posc.CELL_ID_RE.findall(_o.stdout.decode("utf-8", "replace"))) - set(_ids))[:3]))
else:
    arm("D1 corpus arm: pin 391cd500e5 not in this object store -- UNRUN (not a pass)", False, "pin absent")

failed = [r for r in results if not r[1]]
print(f"RESULT: {len(results) - len(failed)} of {len(results)} arms as expected; failed {len(failed)}")
sys.exit(1 if failed else 0)
