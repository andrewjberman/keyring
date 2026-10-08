#!/usr/bin/env python3
"""Battery for .tools/seat-rules-check.py: the checker must fail on a planted false rule.

Cases: a rule with two holders is refused; a kind x area pair with no rule fails; a GATE rule with no probe fails;
a probe that expects a refusal and gets an admit FAILS (planted: a rule claiming a manager is refused on a path the
lane table admits it on, with a control that the same probe passes on a path the manager really is refused on); a
pending probe is counted pending; exercise leaves the tree as it found it.
LAST line: SEAT-RULES-TEST cases=<k>/<n> ok=<True|False>
"""
from __future__ import annotations

import copy
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE)).replace("\\", "/")


def load_checker():
    spec = importlib.util.spec_from_file_location("seat_rules_check", os.path.join(ROOT, ".tools", "seat-rules-check.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


CK = load_checker()
ALL8 = list(CK.KINDS)
OPV = ".tools/owned-paths-validate.py"
MSTR = "0.0.0_AB_MSTR"
TASK_ORDER_PATH = "org/missions/D0/NFRA/NFRA_CTLPLN/task-orders/NFRA_CTLPLN.TO-ZZ-1.probe.md"


def rule(rid, area, holder="LAUNCHER", kinds=None, probe=None, built_by="existing", path=".tools/ajb.ps1",
         entry="Get-AgentLoopDirective", **extra):
    out = {"id": rid, "area": area, "kinds": kinds or list(ALL8), "rule": "A test rule.", "holder": holder,
           "mechanism": {"path": path, "entry": entry}, "probe": probe, "built_by": built_by, "needs_andrew": False}
    out.update(extra)
    return out


def base_doc():
    return {"schema": "seat-rules/1", "rules": [rule("R-GITOPS-1", "GITOPS"), rule("R-AWSDEVOPS-1", "AWSDEVOPS"),
                                                 rule("R-WORKFLOW-1", "WORKFLOW")]}


def opv_probe(serial, path, expect, rc=1, label="lane"):
    return {"label": label, "tool": OPV,
            "argv": ["{PY}", "{ROOT}/" + OPV, "--check-agent", "{SERIAL}", "{ROOT}/.owned-paths.yaml"],
            "stdin": path + "\n", "serials": [serial], "expect": expect, "expect_rc": rc}


def gate(rid, probe, area="WORKFLOW", kinds=("MSTR",), built_by="existing", path=OPV, entry="def _cmd_check_agent"):
    return rule(rid, area, "GATE", list(kinds), probe, built_by, path, entry)


def run_one(r):
    doc = {"schema": "seat-rules/1", "rules": [r]}
    results, _elapsed = CK.exercise(doc, ROOT)
    return results


def git_status():
    return subprocess.run(["git", "status", "--porcelain"], cwd=ROOT, capture_output=True, text=True).stdout


CASES = []


def case(fn):
    CASES.append(fn)
    return fn


def has(problems, needle):
    return any(needle in p for p in problems)


@case
def real_table_validates():
    doc, errs = CK.load_table(os.path.join(ROOT, "org", "ref", "SEAT_RULES.json"))
    problems, stats = CK.validate(doc, ROOT)
    return not errs and not problems and len(stats["pairs"]) == 24, "problems=%s" % problems[:3]


@case
def real_table_needs_andrew_have_questions():
    doc, _ = CK.load_table(os.path.join(ROOT, "org", "ref", "SEAT_RULES.json"))
    needs = [r for r in doc["rules"] if r["needs_andrew"]]
    return len(needs) == 3 and all(r.get("question") for r in needs), "needs=%d" % len(needs)


@case
def base_doc_is_valid():
    problems, stats = CK.validate(base_doc(), ROOT)
    return not problems and len(stats["pairs"]) == 24, str(problems[:2])


@case
def two_holders_refused():
    doc = base_doc()
    doc["rules"][0]["holder"] = ["GATE", "SKILL"]
    problems, _ = CK.validate(doc, ROOT)
    return has(problems, "exactly one holder"), str(problems[:2])


@case
def same_id_twice_refused():
    doc = base_doc()
    twin = copy.deepcopy(doc["rules"][0])
    twin["holder"] = "SKILL"
    twin["mechanism"] = {"path": ".claude/skills/integrate/SKILL.md", "entry": "/integrate"}
    doc["rules"].append(twin)
    problems, _ = CK.validate(doc, ROOT)
    return has(problems, "id used twice"), str(problems[:2])


@case
def pair_with_no_rule_fails():
    doc = base_doc()
    doc["rules"][1]["kinds"] = [k for k in ALL8 if k != "CLOUDOPS"]
    problems, stats = CK.validate(doc, ROOT)
    return has(problems, "PAIR-MISSING CLOUDOPS x AWSDEVOPS") and len(stats["pairs"]) == 23, str(problems[:2])


@case
def gate_without_probe_fails():
    doc = base_doc()
    doc["rules"][0] = gate("R-GITOPS-1", None, area="GITOPS", kinds=ALL8)
    problems, _ = CK.validate(doc, ROOT)
    return has(problems, "GATE rule has no probe"), str(problems[:2])


@case
def non_gate_with_probe_refused():
    doc = base_doc()
    doc["rules"][0]["probe"] = opv_probe(MSTR, "CLAUDE.md", "VIOLATION")
    problems, _ = CK.validate(doc, ROOT)
    return has(problems, "only a GATE rule carries a probe"), str(problems[:2])


@case
def unknown_key_refused():
    doc = base_doc()
    doc["rules"][0]["why"] = "x"
    problems, _ = CK.validate(doc, ROOT)
    return has(problems, "unknown key"), str(problems[:2])


@case
def launcher_and_skill_paths_checked():
    doc = base_doc()
    doc["rules"][0]["mechanism"]["path"] = ".tools/safe-commit.sh"
    doc["rules"][1]["holder"] = "SKILL"
    problems, _ = CK.validate(doc, ROOT)
    return has(problems, "LAUNCHER rule names") and has(problems, "SKILL rule names a file under .claude/skills/"), str(problems[:3])


@case
def needs_andrew_requires_question():
    doc = base_doc()
    doc["rules"][0]["needs_andrew"] = True
    problems, _ = CK.validate(doc, ROOT)
    return has(problems, "no question is given"), str(problems[:2])


@case
def entry_must_exist_in_file_and_path_must_exist():
    doc = base_doc()
    doc["rules"][0]["mechanism"]["entry"] = "no-such-function-xyzzy"
    doc["rules"][1]["mechanism"]["path"] = "org/ref/NO_SUCH_FILE.json"
    doc["rules"][1]["holder"] = "LAUNCHER"
    problems, _ = CK.validate(doc, ROOT)
    return has(problems, "does not occur in") and has(problems, "NO_SUCH_FILE.json does not exist"), str(problems[:3])


@case
def path_built_by_another_cell_is_allowed_absent():
    doc = base_doc()
    doc["rules"][0]["mechanism"] = {"path": "org/ref/NO_SUCH_FILE.json", "entry": "MSTR"}
    problems, _ = CK.validate(doc, ROOT)
    refused_when_existing = has(problems, "NO_SUCH_FILE.json does not exist")
    doc["rules"][0]["built_by"] = "CT-s-1"
    problems2, stats2 = CK.validate(doc, ROOT)
    return (refused_when_existing and not problems2 and stats2["pending_paths"] == ["R-GITOPS-1"]),         "existing_refused=%s pending=%s" % (refused_when_existing, stats2["pending_paths"])


@case
def non_ascii_refused():
    doc = base_doc()
    doc["rules"][0]["rule"] = "caf\u00e9"
    problems, _ = CK.validate(doc, ROOT)
    return has(problems, "non-ASCII"), str(problems[:2])


@case
def probe_serials_must_cover_the_kinds_claimed():
    doc = base_doc()
    doc["rules"][0] = gate("R-GITOPS-1", opv_probe(MSTR, "CLAUDE.md", "VIOLATION"), area="GITOPS", kinds=["MSTR", "CTO"])
    problems, _ = CK.validate(doc, ROOT)
    return has(problems, "no serial of kind CTO"), str(problems[:2])


@case
def planted_false_rule_fails_and_control_passes():
    # the lane table ADMITS a manager on a project's task-orders/ file; a rule claiming it is refused there is false.
    false_probe = opv_probe(MSTR, TASK_ORDER_PATH, "VIOLATION", rc=1, label="planted-false")
    true_probe = opv_probe(MSTR, "org/tier0/STAKES_MATRIX.md", "VIOLATION: org/tier0/STAKES_MATRIX.md", rc=1, label="control")
    bad = run_one(gate("R-WORKFLOW-1", false_probe))
    good = run_one(gate("R-WORKFLOW-2", true_probe))
    ok = bad[0]["status"] == "FAIL" and good[0]["status"] == "PASS"
    return ok, "false=%s control=%s" % (bad[0]["status"], good[0]["status"])


@case
def a_hook_that_admits_where_a_refusal_is_claimed_fails():
    hook_probe = {"label": "mutant-admits", "tool": ".tools/hooks/never-rules-gate.sh",
                  "argv": ["bash", "{ROOT}/.tools/hooks/never-rules-gate.sh"],
                  "stdin_json": {"tool_input": {"command": "git status --short"}, "cwd": "{CWD}"},
                  "serials": ["1.0.0_SA_CTO"], "stands_for_all_kinds": True,
                  "expect": "\"permissionDecision\":\"deny\"", "expect_rc": 0}
    res = run_one(gate("R-GITOPS-1", hook_probe, area="GITOPS", kinds=ALL8, path=".tools/hooks/never-rules-gate.sh",
                       entry="GATE 1"))
    return res[0]["status"] == "FAIL", res[0]["status"] + ": " + res[0]["detail"][:80]


@case
def pending_probe_is_counted_pending_not_failed():
    pr = {"label": "later", "tool": ".tools/no-such-tool-yet.py", "argv": ["{PY}", "{ROOT}/.tools/no-such-tool-yet.py"],
          "stands_for_all_kinds": True, "expect": "verdict=REFUSED"}
    pending = run_one(gate("R-AWSDEVOPS-1", pr, area="AWSDEVOPS", kinds=["CTO"], built_by="CT-s-3",
                           path=".tools/no-such-tool-yet.py", entry="APPLY-WHO"))
    existing = run_one(gate("R-AWSDEVOPS-2", pr, area="AWSDEVOPS", kinds=["CTO"], built_by="existing",
                            path=".tools/no-such-tool-yet.py", entry="APPLY-WHO"))
    line, ok = CK.summary_line({"rules": []}, {"pairs": set()}, [], pending)
    return (pending[0]["status"] == "PENDING" and existing[0]["status"] == "FAIL" and "probes_pending=1" in line
            and "probes_fail=0" in line), "%s / %s / %s" % (pending[0]["status"], existing[0]["status"], line[-60:])


@case
def summary_line_format_and_ok_logic():
    doc = {"rules": [{"holder": "GATE", "needs_andrew": True}, {"holder": "SKILL", "needs_andrew": False}]}
    full = {"pairs": {(k, a) for k in CK.KINDS for a in CK.AREAS}}
    good, ok_good = CK.summary_line(doc, full, [], [{"status": "PASS"}, {"status": "PENDING"}])
    bad, ok_bad = CK.summary_line(doc, full, [], [{"status": "FAIL"}])
    short, ok_short = CK.summary_line(doc, {"pairs": set()}, [], [{"status": "PASS"}])
    pat = re.compile(r"^SEAT-RULES rules=\d+ gate=\d+ skill=\d+ launcher=\d+ pairs_covered=\d+/24 probes_pass=\d+ "
                     r"probes_pending=\d+ probes_fail=\d+ needs_andrew=\d+ ok=(True|False)$")
    return bool(pat.match(good) and ok_good and not ok_bad and not ok_short and pat.match(bad)), good[-70:]


@case
def exercise_leaves_the_tree_as_it_found_it():
    doc, _ = CK.load_table(os.path.join(ROOT, "org", "ref", "SEAT_RULES.json"))
    keep = {"R-GITOPS-1", "R-GITOPS-6", "R-WORKFLOW-8", "R-AWSDEVOPS-2"}
    sub = {"schema": doc["schema"], "rules": [r for r in doc["rules"] if r["id"] in keep]}
    before = git_status()
    results, _elapsed = CK.exercise(sub, ROOT)
    after = git_status()
    stat = {}
    for r in results:
        stat[r["status"]] = stat.get(r["status"], 0) + 1
    ok = before == after and stat.get("FAIL", 0) == 0 and stat.get("PASS", 0) >= 3
    return ok, "status=%s same_tree=%s" % (stat, before == after)


def main():
    passed = 0
    for fn in CASES:
        try:
            ok, detail = fn()
        except Exception as exc:  # noqa: BLE001
            ok, detail = False, "raised %s: %s" % (type(exc).__name__, exc)
        passed += 1 if ok else 0
        print("  %s  %s  %s" % ("PASS" if ok else "FAIL", fn.__name__, str(detail)[:150]))
    total = len(CASES)
    print("SEAT-RULES-TEST cases=%d/%d ok=%s" % (passed, total, passed == total))
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
