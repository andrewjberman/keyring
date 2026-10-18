"""test_proof_instance_select.py -- newest-instance-only selection for the two proof gates (CVO~Z verdict 35689, CTO msg 35690).

Throwaway git repos with controlled commit dates. Arms:
  (a) UNARMED the selector returns its input unchanged, in its own order;
  (b) armed: the latest commit time wins, even over the larger ~N;
  (c) armed, same commit time: the numeric ~N breaks the tie (~10 beats ~9, which a name sort gets wrong);
  (d) armed: an uncommitted new instance is the newest; so is a committed one modified in the tree;
  (e) armed with one instance: unchanged;
  (f) the flag file arms; PROOF_NEWEST_INSTANCE=0 forces off over the file; =1 arms without the file;
  (g) to-pipeline-gate _proof_instance_candidates: a tagged single instance still wins; unarmed lists every instance, armed lists one;
  (h) round-close-check proof_state: an older VALID instance masks a newer FAILING one unarmed (the defect), and does not armed.
"""
import importlib.util
import json
import os
import pathlib
import subprocess

TOOLS = pathlib.Path(__file__).resolve().parent.parent


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, TOOLS / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sel = _load("proof_instance_select_t", "proof_instance_select.py")

STEM = "PROJ.TO-1.thing"
DELIV = "org/missions/D0/T/PROJ/deliverables"


def _git(repo, *args, env=None):
    e = dict(os.environ)
    e.update({"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"})
    if env:
        e.update(env)
    r = subprocess.run(["git", "-C", str(repo)] + list(args), capture_output=True, text=True, env=e)
    assert r.returncode == 0, (args, r.stderr)
    return r.stdout


def _repo(tmp_path):
    _git(tmp_path, "init", "-q")
    return tmp_path


def _commit(repo, rel, content, when):
    p = pathlib.Path(repo) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    _git(repo, "add", "--", rel)
    d = "@%d +0000" % when
    _git(repo, "commit", "-q", "-m", "c", env={"GIT_AUTHOR_DATE": d, "GIT_COMMITTER_DATE": d})


def _inst(n):
    return "%s/0.9.0_WK_PROJ~%s/%s.proof_of_spec.json" % (DELIV, n, STEM)


def _abs(repo, rel):
    return str(pathlib.Path(repo) / rel)


def test_a_unarmed_returns_input_unchanged(tmp_path, monkeypatch):
    monkeypatch.delenv("PROOF_NEWEST_INSTANCE", raising=False)
    repo = _repo(tmp_path)
    paths = []
    for n, t in (("2", 1000), ("10", 2000), ("9", 3000)):
        _commit(repo, _inst(n), "{}", t)
        paths.append(_abs(repo, _inst(n)))
    assert not sel.armed(str(repo))
    assert sel.select(str(repo), paths) == paths


def test_b_armed_latest_commit_time_wins_over_larger_suffix(tmp_path, monkeypatch):
    monkeypatch.setenv("PROOF_NEWEST_INSTANCE", "1")
    repo = _repo(tmp_path)
    for n, t in (("10", 1000), ("2", 5000), ("9", 3000)):      # ~2 committed LAST
        _commit(repo, _inst(n), "{}", t)
    paths = [_abs(repo, _inst(n)) for n in ("10", "2", "9")]
    assert sel.select(str(repo), paths) == [_abs(repo, _inst("2"))]


def test_c_same_commit_time_breaks_on_numeric_suffix(tmp_path, monkeypatch):
    monkeypatch.setenv("PROOF_NEWEST_INSTANCE", "1")
    repo = _repo(tmp_path)
    for n in ("9", "10", "2"):
        _commit(repo, _inst(n), "{}", 7000)                    # one second, every instance
    paths = [_abs(repo, _inst(n)) for n in ("2", "9", "10")]
    assert sorted(paths)[-1].replace("\\", "/").endswith("~9/" + STEM + ".proof_of_spec.json")   # the name sort would pick ~9
    assert sel.select(str(repo), paths) == [_abs(repo, _inst("10"))]          # the numeric tie-break picks ~10


def test_d_uncommitted_instance_is_newest(tmp_path, monkeypatch):
    monkeypatch.setenv("PROOF_NEWEST_INSTANCE", "1")
    repo = _repo(tmp_path)
    _commit(repo, _inst("1"), "{}", 1000)
    _commit(repo, _inst("2"), "{}", 9000)
    fresh = pathlib.Path(_abs(repo, _inst("3")))
    fresh.parent.mkdir(parents=True)
    fresh.write_text("{}", encoding="utf-8")                   # untracked, no commit at all
    paths = [_abs(repo, _inst(n)) for n in ("1", "2", "3")]
    assert sel.select(str(repo), paths) == [str(fresh)]
    fresh.unlink()
    pathlib.Path(_abs(repo, _inst("1"))).write_text('{"edited": true}', encoding="utf-8")   # oldest, modified in the tree
    assert sel.select(str(repo), paths[:2]) == [_abs(repo, _inst("1"))]


def test_e_one_instance_is_unchanged_even_armed(tmp_path, monkeypatch):
    monkeypatch.setenv("PROOF_NEWEST_INSTANCE", "1")
    repo = _repo(tmp_path)
    _commit(repo, _inst("1"), "{}", 1000)
    assert sel.select(str(repo), [_abs(repo, _inst("1"))]) == [_abs(repo, _inst("1"))]
    assert sel.select(str(repo), []) == []


def test_f_flag_file_env_override_both_ways(tmp_path, monkeypatch):
    repo = _repo(tmp_path)
    monkeypatch.delenv("PROOF_NEWEST_INSTANCE", raising=False)
    assert not sel.armed(str(repo))
    flag = pathlib.Path(repo) / "org" / "mcp" / "proof-newest-instance.enforce"
    flag.parent.mkdir(parents=True)
    flag.write_text("armed by the test\n", encoding="utf-8")
    assert sel.armed(str(repo))
    monkeypatch.setenv("PROOF_NEWEST_INSTANCE", "0")
    assert not sel.armed(str(repo))                            # =0 forces OFF over the file
    flag.unlink()
    monkeypatch.setenv("PROOF_NEWEST_INSTANCE", "1")
    assert sel.armed(str(repo))                                # =1 arms with no file


def _order_md(tagged_path=None):
    block = "<proof_of_spec>\nthe instance is `%s`\n</proof_of_spec>\n" % tagged_path if tagged_path else "<proof_of_spec>\nsee schema\n</proof_of_spec>\n"
    return "# TO\n<to_id>PROJ.TO-1</to_id>\n<status>complete</status>\n" + block


def test_g_gate_candidates(tmp_path, monkeypatch):
    gate = _load("to_pipeline_gate_t", "to-pipeline-gate.py")
    repo = _repo(tmp_path)
    for n, t in (("1", 1000), ("2", 2000), ("3", 3000)):
        _commit(repo, _inst(n), "{}", t)
    rel = "org/missions/D0/T/PROJ/task-orders/%s.md" % STEM
    monkeypatch.delenv("PROOF_NEWEST_INSTANCE", raising=False)
    got, err = gate._proof_instance_candidates(str(repo), rel, _order_md())
    assert err is None and len(got) == 3                       # unarmed: every instance, as before
    monkeypatch.setenv("PROOF_NEWEST_INSTANCE", "1")
    got, _ = gate._proof_instance_candidates(str(repo), rel, _order_md())
    assert got == [os.path.join(str(repo), *_inst("3").split("/"))] or [os.path.normpath(g) for g in got] == [
        os.path.normpath(os.path.join(str(repo), *_inst("3").split("/")))]
    tag = _inst("1")                                           # a block pinning exactly one instance still wins
    got, _ = gate._proof_instance_candidates(str(repo), rel, _order_md(tag))
    assert [os.path.normpath(g) for g in got] == [os.path.normpath(os.path.join(str(repo), *tag.split("/")))]


def test_h_round_close_older_valid_no_longer_masks_newer_failing(tmp_path, monkeypatch):
    rcc = _load("round_close_check_t", "round-close-check.py")
    repo = _repo(tmp_path)
    good = {"to_id": "PROJ.TO-1", "acceptance": [{"criterion_id": "AC1", "status": "PASS"}]}
    bad = {"to_id": "PROJ.TO-1", "acceptance": [{"criterion_id": "AC1", "status": "FAIL"}]}
    _commit(repo, _inst("1"), json.dumps(good), 1000)          # older, VALID
    _commit(repo, _inst("2"), json.dumps(bad), 2000)           # newer, FAILING
    order = {"stem": STEM, "id": "PROJ.TO-1", "criteria": [{"id": "AC1"}], "seat_dir": None}
    proj = os.path.join(str(repo), "org", "missions", "D0", "T", "PROJ")
    src = rcc.WorkTree(str(repo))
    monkeypatch.delenv("PROOF_NEWEST_INSTANCE", raising=False)
    ok, why = rcc.proof_state(src, order, proj, str(repo), False)
    assert ok is True, why                                     # the defect, reproduced: the old valid one passes the order
    monkeypatch.setenv("PROOF_NEWEST_INSTANCE", "1")
    ok, why = rcc.proof_state(src, order, proj, str(repo), False)
    assert ok is False and "FAIL" in why                       # armed: the newest (failing) instance is the one graded


def test_i_helper_missing_falls_back_to_old_behaviour(tmp_path, monkeypatch):
    """A gate script copied away from .tools (an existing test's mutant control does this) must not crash: it grades as before.
    The copy is simulated by pointing each module's __file__ at a directory that holds no proof_instance_select.py."""
    monkeypatch.setenv("PROOF_NEWEST_INSTANCE", "1")
    rcc = _load("rcc_lone", "round-close-check.py")
    gate = _load("gate_lone", "to-pipeline-gate.py")
    found = ["a/~1/x.json", "a/~2/x.json"]
    for mod in (rcc, gate):
        monkeypatch.setattr(mod, "__file__", str(tmp_path / "copied-gate.py"))
        assert mod._newest_instance_only(str(tmp_path), list(found)) == found
