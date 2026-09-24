"""test_direct_act_order.py -- pytest arms for .tools/direct-act-order.py (AMGT_RESAPP AMGT-rk-58).

Pure-function arms over the same functions the tool's own --self-test exercises, plus ONE
end-to-end --dry-run mint inside a temporary git repository this test builds itself. No arm
touches the real project tree, S3, DynamoDB or a broker.
"""
import importlib.util
import os
import subprocess
import sys

import pytest

_HERE = os.path.dirname(os.path.abspath(__file__))
_TOOL_PATH = os.path.join(_HERE, "..", "direct-act-order.py")

_spec = importlib.util.spec_from_file_location("direct_act_order", _TOOL_PATH)
dao = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(dao)


# ---------------------------------------------------------------------------
# Pure grammar arms
# ---------------------------------------------------------------------------

def test_leading_slash_refused():
    ok, reason = dao.validate_path_grammar("/abs/path")
    assert ok is False
    assert "leading slash" in reason


def test_parent_traversal_refused():
    ok, reason = dao.validate_path_grammar("a/../b")
    assert ok is False
    assert ".." in reason


def test_bracket_not_glob_refused():
    ok, reason = dao.validate_path_grammar("a/{b,c}/d")
    assert ok is False
    assert "bracket" in reason


def test_valid_glob_admitted():
    ok, _reason = dao.validate_path_grammar("infra/aws/terraform/harvest/scoped-amgt-api.tf")
    assert ok is True
    ok2, _r2 = dao.validate_path_grammar("data/*/scripts/gold/*.py")
    assert ok2 is True


def test_path_subset_refusal():
    coo = "alpha beta gamma"
    cto = "delta epsilon"
    assert dao.path_named_by_either("alpha", coo, cto) is True
    assert dao.path_named_by_either("delta", coo, cto) is True
    assert dao.path_named_by_either("zzz-not-here", coo, cto) is False


def test_section_heading_present_and_missing():
    text = "# NEVER-WIDEN CO-SIGN. The `scores/v1/` read grant.\nbody\n"
    assert dao.section_heading_present(text, "scores/v1/") is True
    assert dao.section_heading_present("no heading at all here\n", "scores/v1/") is False


def test_extract_section_bounds_to_next_heading():
    text = ("# TOP. The `x/y` thing.\nbody one\n## sub\nmore\n# NEXT TOP\nother body\n")
    section = dao.extract_section(text, "x/y")
    assert section is not None
    assert "body one" in section
    assert "more" in section
    assert "other body" not in section


def test_issuer_is_coo():
    assert dao.issuer_is_coo("2.0.0_SA_COO~Z") is True
    assert dao.issuer_is_coo("2.0.0_SA_COO") is True
    assert dao.issuer_is_coo("0.9.0_WK_FOO~1") is False
    assert dao.issuer_is_coo("") is False


def test_preflight_run_no_digit_refused():
    bad = ("comp-schedule: RUN -- (no digit here)\n"
           "comp-iam: DECLARED-NOT-APPLICABLE fine\n"
           "comp-adversary: DECLARED-NOT-APPLICABLE fine\n")
    v = dao.check_preflight_text(bad)
    assert len(v) >= 1


def test_preflight_declared_not_applicable_needs_reason():
    bad = ("comp-schedule: DECLARED-NOT-APPLICABLE\n"
           "comp-iam: RUN -- (fixture: 1 of 1)\n"
           "comp-adversary: DECLARED-NOT-APPLICABLE fine\n")
    v = dao.check_preflight_text(bad)
    assert len(v) >= 1


def test_preflight_good_shape_clean():
    good = ("comp-schedule: DECLARED-NOT-APPLICABLE fixture -- no schedule\n"
            "comp-iam: RUN -- (fixture: 13 of 13 entries per limb read)\n"
            "comp-adversary: DECLARED-NOT-APPLICABLE fixture -- a specification\n")
    v = dao.check_preflight_text(good)
    assert v == []


def test_two_invocation_criterion_refused():
    bad = ("<criterion id=\"X1\" cell_refs=\"C-1\"><invocation>a</invocation>"
           "<invocation>b</invocation><expect>c</expect></criterion>")
    v, _ids = dao.check_criteria_text(bad, "C-1")
    assert len(v) >= 1


def test_criterion_cell_refs_mismatch_refused():
    bad = ("<criterion id=\"X1\" cell_refs=\"WRONG-CELL\"><invocation>a</invocation>"
           "<expect>c</expect></criterion>")
    v, _ids = dao.check_criteria_text(bad, "C-1")
    assert len(v) >= 1


def test_criterion_clean_shape_no_violations():
    good = ("<criterion id=\"AC1\" cell_refs=\"C-1\"><invocation>echo hi</invocation>"
            "<expect>prints hi</expect></criterion>")
    v, ids = dao.check_criteria_text(good, "C-1")
    assert v == []
    assert ids == ["AC1"]


def test_judgment_criterion_no_children_clean():
    good = "<criterion id=\"J1\" cell_refs=\"C-1\" judgment=\"true\"/>"
    v, ids = dao.check_criteria_text(good, "C-1")
    assert v == []
    assert ids == ["J1"]


def test_make_slug_shape():
    slug = dao.make_slug("scores prefix grant fixture")
    assert slug == "scores-prefix-grant-fixture"
    words = slug.split("-")
    assert 2 <= len(words) <= 5


# ---------------------------------------------------------------------------
# ONE end-to-end --dry-run mint, entirely inside a temp git repository this test builds.
# ---------------------------------------------------------------------------

def _run(cmd, cwd, env):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=60, env=env)


@pytest.fixture()
def temp_repo(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    env = dict(os.environ)
    env["GIT_AUTHOR_NAME"] = "test"
    env["GIT_AUTHOR_EMAIL"] = "test@example.invalid"
    env["GIT_COMMITTER_NAME"] = "test"
    env["GIT_COMMITTER_EMAIL"] = "test@example.invalid"
    _run(["git", "init", "-q"], str(root), env)
    _run(["git", "config", "user.name", "test"], str(root), env)
    _run(["git", "config", "user.email", "test@example.invalid"], str(root), env)

    proj = root / "org" / "missions" / "D9" / "FIX" / "FIXPRJ"
    (proj / "decompositions").mkdir(parents=True)
    (proj / "surprise-channel" / "investigations").mkdir(parents=True)
    (proj / "task-orders").mkdir(parents=True)
    (proj / "ledger").mkdir(parents=True)
    (proj / "deliverables").mkdir(parents=True)

    (proj / "project.json").write_text('{"fabric": "site-z", "dep_stage": "EXECUTING"}\n', encoding="utf-8")
    (proj / "decompositions" / "FIXPRJ_DECOMP.md").write_text(
        "| cell | desc |\n|---|---|\n| FIX-c-1 | the one cell |\n", encoding="utf-8")
    (proj / "surprise-channel" / "investigations" / "INVESTIGATION_v1.md").write_text(
        "```json\n[]\n```\n", encoding="utf-8")

    coo = proj / "ledger" / "NEVER_WIDEN_FIXTURE_COO_HALF.md"
    cto = proj / "ledger" / "NEVER_WIDEN_FIXTURE_CTO_HALF.md"
    coo.write_text("# NEVER-WIDEN CO-SIGN -- COO HALF. The `fixture/thing.py` grant.\n"
                    "body naming fixture/thing.py\n", encoding="utf-8")
    cto.write_text("# NEVER-WIDEN CO-SIGN -- CTO HALF. The `fixture/thing.py` grant.\n"
                    "body naming fixture/thing.py\n", encoding="utf-8")

    _run(["git", "add", "-A"], str(root), env)
    _run(["git", "commit", "-q", "-m", "seed fixture repo"], str(root), env)

    preflight = root / "preflight.txt"
    preflight.write_text("comp-schedule: DECLARED-NOT-APPLICABLE fixture\n"
                          "comp-iam: RUN -- (fixture: 1 of 1)\n"
                          "comp-adversary: DECLARED-NOT-APPLICABLE fixture\n", encoding="utf-8")
    criteria = root / "criteria.txt"
    criteria.write_text("<proof_of_spec>\n"
                         "  <criterion id=\"AC1\" cell_refs=\"FIX-c-1\">"
                         "<invocation>echo hi</invocation><expect>prints hi</expect></criterion>\n"
                         "</proof_of_spec>\n", encoding="utf-8")
    return root, env


def test_end_to_end_dry_run_mint(temp_repo):
    root, env = temp_repo
    env = dict(env)
    env["OPAL_AGENT_SERIAL"] = "2.0.0_SA_COO~test"
    cmd = [sys.executable, _TOOL_PATH, "mint",
           "--code", "FIXPRJ", "--slot", "9", "--cell", "FIX-c-1",
           "--title", "fixture render test",
           "--coo-half", "org/missions/D9/FIX/FIXPRJ/ledger/NEVER_WIDEN_FIXTURE_COO_HALF.md",
           "--cto-half", "org/missions/D9/FIX/FIXPRJ/ledger/NEVER_WIDEN_FIXTURE_CTO_HALF.md",
           "--section", "fixture/thing.py",
           "--path", "fixture/thing.py",
           "--preflight-file", "preflight.txt",
           "--criteria-file", "criteria.txt",
           "--round", "1", "--dry-run"]
    r = _run(cmd, str(root), env)
    out = r.stdout + r.stderr
    assert r.returncode == 0, out
    assert "PAIR: COO sha256=" in out
    assert "---BEGIN ORDER---" in out and "---END ORDER---" in out
    rendered = out.split("---BEGIN ORDER---", 1)[1].split("---END ORDER---", 1)[0]
    assert rendered.count("<invocation>") == 1
    assert rendered.count("<expect>") == 1
    assert "<issued_to>0.9.0_WK_FIXPRJ~9</issued_to>" in rendered
    assert "fixture/thing.py" in rendered
    assert "org/missions/D9/FIX/FIXPRJ/deliverables/0.9.0_WK_FIXPRJ~9/" in rendered
    assert "org/critical_paths/change_management/" in rendered
    assert "org/critical_paths/.open_deploys/" in rendered
    # nothing written on a --dry-run mint
    to_dir = root / "org" / "missions" / "D9" / "FIX" / "FIXPRJ" / "task-orders"
    assert list(to_dir.iterdir()) == []


def test_end_to_end_subset_refusal(temp_repo):
    root, env = temp_repo
    env = dict(env)
    env["OPAL_AGENT_SERIAL"] = "2.0.0_SA_COO~test"
    cmd = [sys.executable, _TOOL_PATH, "mint",
           "--code", "FIXPRJ", "--slot", "9", "--cell", "FIX-c-1",
           "--title", "fixture render test",
           "--coo-half", "org/missions/D9/FIX/FIXPRJ/ledger/NEVER_WIDEN_FIXTURE_COO_HALF.md",
           "--cto-half", "org/missions/D9/FIX/FIXPRJ/ledger/NEVER_WIDEN_FIXTURE_CTO_HALF.md",
           "--section", "fixture/thing.py",
           "--path", "fixture/thing.py",
           "--path", "not/in/either/half.py",
           "--preflight-file", "preflight.txt",
           "--criteria-file", "criteria.txt",
           "--round", "1", "--dry-run"]
    r = _run(cmd, str(root), env)
    out = r.stdout + r.stderr
    assert r.returncode == 2
    assert "REFUSED: path not named by either half: not/in/either/half.py" in out


def test_end_to_end_non_coo_issuer_refusal(temp_repo):
    root, env = temp_repo
    env = dict(env)
    env["OPAL_AGENT_SERIAL"] = "0.9.0_WK_FIXPRJ~1"
    cmd = [sys.executable, _TOOL_PATH, "mint",
           "--code", "FIXPRJ", "--slot", "9", "--cell", "FIX-c-1",
           "--title", "fixture render test",
           "--coo-half", "org/missions/D9/FIX/FIXPRJ/ledger/NEVER_WIDEN_FIXTURE_COO_HALF.md",
           "--cto-half", "org/missions/D9/FIX/FIXPRJ/ledger/NEVER_WIDEN_FIXTURE_CTO_HALF.md",
           "--section", "fixture/thing.py",
           "--path", "fixture/thing.py",
           "--preflight-file", "preflight.txt",
           "--criteria-file", "criteria.txt",
           "--round", "1", "--dry-run"]
    r = _run(cmd, str(root), env)
    out = r.stdout + r.stderr
    assert r.returncode == 2
    assert "does not start with 2.0.0_SA_COO" in out
