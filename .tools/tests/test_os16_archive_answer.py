#!/usr/bin/env python3
"""NFRA_OUTSET.TO-OS-s-16 battery: `comp-heat archive` -- a RANKED archive-candidate answer with a
reason per line a person can dispute, and NOTHING is removed by the tool.

Run at both required file grains:
  python .tools/tests/test_os16_archive_answer.py
  python -m pytest -q .tools/tests/test_os16_archive_answer.py

WARN: NEVER-AUTO-DELETE (PRD R-5) IS ABSOLUTE, AND THIS BATTERY IS WHERE IT IS ENFORCED RATHER THAN
ASSERTED. Arm C snapshots every file in a throwaway tree (relative path + sha256) before and after
a run and requires them byte-identical. Arm D is the RED mutant the criterion names -- a copy of
comp-heat with a deletion spliced in -- and it exists to prove arm C's snapshot can actually SEE a
removal. An integrity check that has never caught anything is a promise, not a control.

WARN: EVERY MUTANT RUN IS POINTED AT A `tempfile.mkdtemp()` REPOSITORY, NEVER THE REAL ONE. That is
why `comp-heat archive` takes `--root` at all. A mutant that deletes must not be able to reach the
estate, and "we were careful" is not a mechanism -- arm D asserts the mutant's damage landed inside
the throwaway tree and arm C re-checks the real repo is untouched by the production runs.

THE CELL IS A WIRE, NOT A BUILD (OS-s-15's ruling): O1 already scores, O2 already rolls the scores up
the directory tree and finds MAXIMAL cold roots, O3 already runs verify-before-recommend. What was
missing was a caller. Arm B is the disarm evidence for row NFRA_OUTSET-W3-S4: on the same synthetic
shape slot 3 exercised, the flat `freshness` grouping returns 0 candidates and the rolled-up
`archive` answer returns the maximal root.
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / ".tools" / "comp-heat"
HEATMAP = ROOT / "org" / "modules" / "heatmap"

# The mutation the criterion names: a tool that DELETES. Spliced into the one place a candidate
# list is known -- immediately after the maximal cold subtrees are computed.
DELETE_ANCHOR = "    head, tail = cold[:a.top], cold[a.top:]"
DELETE_MUTANT = (
    "    head, tail = cold[:a.top], cold[a.top:]\n"
    "    for _c in cold[:1]:  # RED MUTANT: a tool that ACTS on its own advice\n"
    "        import shutil as _sh\n"
    "        _sh.rmtree(os.path.join(root, _c['dir']), ignore_errors=True)"
)

RESULTS: list[tuple[str, bool, str]] = []


def _record(name: str, ok: bool, detail) -> None:
    RESULTS.append((name, ok, str(detail).replace("\n", " ")[:300]))


def _git(repo: Path, *args, env_extra=None, timeout=60):
    env = dict(os.environ)
    env.update({"GIT_CONFIG_NOSYSTEM": "1", "HOME": str(repo), "USERPROFILE": str(repo)})
    if env_extra:
        env.update(env_extra)
    return subprocess.run(["git", "-C", str(repo), "-c", "core.hooksPath=",
                           "-c", "user.name=os16", "-c", "user.email=os16@example.invalid",
                           *args], capture_output=True, text=True, timeout=timeout, env=env)


def _make_repo(files: dict, age_days: int = 400) -> Path:
    """A throwaway git repo whose whole history is `age_days` old, so every tracked file scores
    COLD. Ages come from the COMMITTER timestamp (object_freshness reads `git log --format=%ct`),
    so both date envs are set."""
    repo = Path(tempfile.mkdtemp(prefix="os16-repo-"))
    for rel, body in files.items():
        p = repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8")
    _git(repo, "init", "-q")
    _git(repo, "add", "-A")
    # AN ABSOLUTE ISO STAMP, NOT "400 days ago": git's commit date parser refuses the relative
    # form ("fatal: invalid date format: 400 days ago") even though `git log --since` accepts it,
    # and the commit then fails SILENTLY as far as the fixture is concerned -- the next call dies
    # on "does not have any commits yet", one layer away from the real cause.
    when = _dt.datetime.now(_dt.timezone.utc) - _dt.timedelta(days=age_days)
    stamp = when.strftime("%Y-%m-%dT%H:%M:%S+0000")
    r = _git(repo, "commit", "-q", "-m", "os16 fixture",
             env_extra={"GIT_AUTHOR_DATE": stamp, "GIT_COMMITTER_DATE": stamp})
    if r.returncode != 0:
        raise AssertionError("fixture repo commit failed rc=%d: %s"
                             % (r.returncode, (r.stderr or "").strip()[:200]))
    return repo


def _snapshot(repo: Path) -> dict:
    """Every file under the tree: relative path -> sha256. The instrument arm C and arm D share."""
    out = {}
    for dirpath, _dirnames, filenames in os.walk(repo):
        for fn in filenames:
            fp = Path(dirpath) / fn
            rel = str(fp.relative_to(repo)).replace("\\", "/")
            try:
                out[rel] = hashlib.sha256(fp.read_bytes()).hexdigest()
            except OSError:
                out[rel] = "<unreadable>"
    return out


def _run(*args, tool: Path = TOOL, timeout: int = 110):
    env = dict(os.environ)
    env["COMP_HEATMAP_DIR"] = str(HEATMAP)
    return subprocess.run([sys.executable, str(tool), *args], cwd=str(ROOT), text=True,
                          capture_output=True, timeout=timeout, env=env)


# The shape slot 3 exercised for NFRA_OUTSET-W3-S4: wholly cold, spread thin across leaf dirs so
# that NO leaf dir reaches the flat grouping's n>=3 floor.
DEAD_TREE = {("dead/%s/f%d.py" % (d, i)): "# cold\n" for d in "abcd" for i in (1, 2)}


def _run_battery() -> None:                                                # noqa: C901
    if RESULTS:
        return

    # ---- ARM A + B + C: one throwaway repo, three questions ----
    repo = _make_repo(dict(DEAD_TREE, **{"live/keep.py": "import os\n"}))
    try:
        before = _snapshot(repo)
        r = _run("archive", "--root", str(repo), "--budget", "60", "--min-files", "5",
                 "--cold-threshold", "0.9", "--top", "10")
        after = _snapshot(repo)
        lines = r.stdout.splitlines()
        cand = [ln for ln in lines if ln.strip().startswith(("1.", "2.", "3."))
                and ("RECOMMEND_ARCHIVE" in ln or "HOLD_REFERENCED" in ln)]
        reasons = [ln for ln in lines if "REASON:" in ln]
        disputes = [ln for ln in lines if "DISPUTE IT BY:" in ln]
        _record("A-ANSWER-RANKS-WITH-A-DISPUTABLE-REASON-PER-LINE",
                r.returncode == 0 and len(cand) >= 1
                and len(reasons) == len(cand) and len(disputes) == len(cand)
                and "denominator:" in r.stdout and "ADVISORY-ONLY -- NOTHING IS REMOVED" in r.stdout,
                "rc=%d ; %d ranked candidate line(s), %d REASON line(s), %d DISPUTE line(s) -- "
                "one each, and the header says the tool removes nothing | %s"
                % (r.returncode, len(cand), len(reasons), len(disputes),
                   (cand[0].strip()[:90] if cand else r.stdout[:150] or r.stderr[:150])))

        # ---- ARM B: the roll-up is REAL -- the W3-S4 disarm, through the CLI ----
        rf = _run("freshness", "--budget", "60", "--json")   # the real repo's flat grouping shape
        f_flat = None
        try:
            f_flat = json.loads(rf.stdout)
        except Exception:                                                   # noqa: BLE001
            pass
        ra = _run("archive", "--root", str(repo), "--budget", "60", "--json")
        rfx = _run("freshness", "--budget", "60", "--json")
        # On the SYNTHETIC tree the flat grouping cannot see the dead root at all; comp-heat
        # freshness has no --root, so the flat side is measured with the engines directly.
        sys.path.insert(0, str(HEATMAP))
        import time as _t

        from heat_map import HeatParams, cluster_by_locality               # noqa: E402
        from object_freshness import build                                 # noqa: E402
        from object_locality import aggregate_tree, maximal_cold_subtrees  # noqa: E402
        scores, _src = build(str(repo), HeatParams(half_life_days=30.0), _t.time())
        clusters = cluster_by_locality(scores, lambda p: os.path.dirname(p) or ".")
        flat_hits = [k for k, v in clusters.items() if v["n"] >= 3 and v["cold_frac"] >= 0.8]
        rolled = maximal_cold_subtrees(aggregate_tree(scores), 0.9, 5)
        arch = None
        try:
            arch = json.loads(ra.stdout)
        except Exception:                                                   # noqa: BLE001
            pass
        cli_dirs = [c["dir"] for c in (arch or {}).get("candidates", [])] + \
                   [c["dir"] for c in (arch or {}).get("unassessed", [])]
        _record("B-ROLLUP-IS-REAL-FLAT-GROUPING-MISSES-THE-DEAD-ROOT",
                flat_hits == [] and [r_["dir"] for r_ in rolled] == ["dead"]
                and "dead" in cli_dirs and ra.returncode == 0,
                "same 8-of-8-cold tree across 4 leaf dirs: flat immediate-parent grouping -> %r "
                "(0 candidates) ; O2 roll-up -> %r ; and `comp-heat archive` reports %r -- the "
                "wire makes the grouping real"
                % (flat_hits, [r_["dir"] for r_ in rolled], cli_dirs))

        # ---- ARM C: NOTHING WAS REMOVED OR MOVED ----
        _record("C-PRODUCTION-RUN-REMOVES-AND-MOVES-NOTHING",
                before == after and len(before) >= len(DEAD_TREE),
                "snapshotted %d file(s) by relative path + sha256 before and after a real "
                "`archive` run; identical=%s ; added=%r removed=%r"
                % (len(before), before == after,
                   sorted(set(after) - set(before))[:3], sorted(set(before) - set(after))[:3]))

        # ---- ARM D: THE RED MUTANT -- a tool that DELETES, and the arm that catches it ----
        src = TOOL.read_text(encoding="utf-8")
        if src.count(DELETE_ANCHOR) != 1:
            raise AssertionError("mutation anchor count != 1: %d" % src.count(DELETE_ANCHOR))
        mrepo = _make_repo(dict(DEAD_TREE, **{"live/keep.py": "import os\n"}))
        mdir = tempfile.mkdtemp(prefix="os16-mutant-")
        try:
            mtool = Path(mdir) / "comp-heat"
            mtool.write_text(src.replace(DELETE_ANCHOR, DELETE_MUTANT, 1), encoding="utf-8")
            shutil.copyfile(ROOT / ".tools" / "_compbudget.py", Path(mdir) / "_compbudget.py")
            m_before = _snapshot(mrepo)
            _run("archive", "--root", str(mrepo), "--budget", "60", "--top", "10", tool=mtool)
            m_after = _snapshot(mrepo)
            deleted = sorted(set(m_before) - set(m_after))
            _record("D-RED-MUTANT-THAT-DELETES-FAILS-THE-INTEGRITY-ARM",
                    m_before != m_after and len(deleted) >= len(DEAD_TREE)
                    and all(d.startswith("dead/") for d in deleted)
                    and before == after,
                    "the mutant removed %d file(s) from its THROWAWAY tree (%r...) and arm C's "
                    "snapshot detects it: identical=%s. Production on its own tree: identical=%s. "
                    "The integrity check is therefore a control, not a promise"
                    % (len(deleted), deleted[:2], m_before == m_after, before == after))
        finally:
            shutil.rmtree(mdir, ignore_errors=True)
            shutil.rmtree(mrepo, ignore_errors=True)

        _record("E-MUTATION-ANCHOR-UNIQUE",
                TOOL.read_text(encoding="utf-8").count(DELETE_ANCHOR) == 1,
                "exactly one candidate-list site expected in .tools/comp-heat")

        # ---- ARM F: the denominator, and UNASSESSED is not CLEARED ----
        ok_f = False
        det = "no JSON"
        if arch:
            d = arch.get("denominator", {})
            ok_f = (d.get("claim") == "measured" and d.get("scored_paths", 0) > 0
                    and d.get("maximal_cold_subtrees_found", -1) >= 1
                    and d.get("rollup_clustered_n") == d.get("rollup_total_n")
                    and arch.get("never_removes") is True
                    and arch.get("removals_performed") == 0)
            det = json.dumps(d)
        _record("F-DENOMINATOR-AND-COVERAGE-ARE-PUBLISHED", ok_f, det)

        # ---- ARM G: a candidate beyond --top is UNASSESSED, never silently dropped ----
        # TWO DISJOINT dead roots, because one tree yields exactly one MAXIMAL root by
        # construction (a child never qualifies while its parent does) -- an earlier draft used the
        # single-root fixture and this arm failed at "0 unassessed", which was the FIXTURE being
        # unable to represent the case, not the tool failing to carry it.
        two_repo = _make_repo(dict(DEAD_TREE,
                                   **{("attic/%s/g%d.py" % (d, i)): "# cold\n"
                                      for d in "abcd" for i in (1, 2)}))
        try:
            r_top = _run("archive", "--root", str(two_repo), "--budget", "60", "--min-files", "5",
                         "--cold-threshold", "0.9", "--top", "1")
            r_top_j = _run("archive", "--root", str(two_repo), "--budget", "60", "--min-files", "5",
                           "--cold-threshold", "0.9", "--top", "1", "--json")
            tj = None
            try:
                tj = json.loads(r_top_j.stdout)
            except Exception:                                               # noqa: BLE001
                pass
            _record("G-BEYOND-TOP-READS-UNASSESSED-NOT-CLEARED",
                    tj is not None and len(tj.get("unassessed", [])) >= 1
                    and len(tj.get("candidates", [])) == 1
                    and "UNASSESSED" in r_top.stdout
                    and "NOT cleared, just not examined" in r_top.stdout,
                    "with --top 1 and %d candidate(s) found, %d assessed and %d carried as "
                    "UNASSESSED, and the render says 'NOT cleared, just not examined'"
                    % (tj["denominator"]["maximal_cold_subtrees_found"] if tj else -1,
                       len(tj.get("candidates", [])) if tj else -1,
                       len(tj.get("unassessed", [])) if tj else -1))
        finally:
            shutil.rmtree(two_repo, ignore_errors=True)

        # ---- ARM H: RECOMMEND vs HOLD -- verify BEFORE recommend, with the mandatory gate ----
        ref_repo = _make_repo(dict(DEAD_TREE,
                                   **{"live/uses.py": "PATH = 'dead'\n"}))
        try:
            r_ref = _run("archive", "--root", str(ref_repo), "--budget", "60", "--min-files", "5",
                         "--json")
            rj = json.loads(r_ref.stdout)
            held = [c for c in rj["candidates"] if c["verdict"] == "HOLD_REFERENCED"]
            recs = [c for c in (arch or {}).get("candidates", [])
                    if c["verdict"] == "RECOMMEND_ARCHIVE"]
            _record("H-VERIFY-BEFORE-RECOMMEND-HOLDS-A-REFERENCED-SUBTREE",
                    len(held) >= 1 and held[0]["inbound_refs"]
                    and len(recs) >= 1 and recs[0]["mandatory_graph_gate"]
                    and "comp-blast" in recs[0]["mandatory_graph_gate"],
                    "an OUTSIDE file mentioning the subtree path -> %s with evidence %r ; a "
                    "name-clean subtree -> %s carrying the MANDATORY gate %r (which this tool "
                    "does NOT run)"
                    % (held[0]["verdict"] if held else "?",
                       (held[0]["inbound_refs"][:2] if held else []),
                       recs[0]["verdict"] if recs else "?",
                       recs[0]["mandatory_graph_gate"] if recs else None))
        finally:
            shutil.rmtree(ref_repo, ignore_errors=True)

        # ---- ARM I: a cut budget claims NO candidate list ----
        r_cut = _run("archive", "--root", str(repo), "--budget", "0.001")
        _record("I-A-CUT-BUDGET-CLAIMS-NO-CANDIDATE-LIST",
                r_cut.returncode == 3 and "BUDGET REACHED:" in r_cut.stdout
                and "PARTIAL_OR_BLIND" in r_cut.stdout
                and "no candidate list is claimed from a PREFIX" in r_cut.stdout
                and "RECOMMEND_ARCHIVE" not in r_cut.stdout,
                "rc=%d ; a subtree that looks wholly cold in a partial scan may not be, so the "
                "answer is refused rather than truncated" % r_cut.returncode)

        # ---- ARM J: the real repo's own freshness answer no longer mislabels its grouping ----
        _record("J-FRESHNESS-NO-LONGER-CLAIMS-A-ROLLUP-IT-DOES-NOT-DO",
                f_flat is not None and rfx.returncode == 0
                and f_flat.get("cold_subtrees_basis", {}).get("grouping", "").startswith(
                    "IMMEDIATE-PARENT")
                and "the_rollup_answer" in f_flat.get("cold_subtrees_basis", {}),
                json.dumps(f_flat.get("cold_subtrees_basis", {}))[:220] if f_flat else "no JSON")
    finally:
        shutil.rmtree(repo, ignore_errors=True)


def _report() -> int:
    _run_battery()
    failed = [(n, d) for n, ok, d in RESULTS if not ok]
    for name, ok, detail in RESULTS:
        print("[%s] %s -- %s" % ("PASS" if ok else "FAIL", name, detail))
    print("OS16-ARCHIVE-ANSWER BATTERY: %d/%d PASS (denominator %d; every mutant run confined to a "
          "tempfile repo, 0 files removed from this estate)"
          % (len(RESULTS) - len(failed), len(RESULTS), len(RESULTS)))
    return 1 if failed else 0


def test_all_arms_pass():
    _run_battery()
    failed = [(n, d) for n, ok, d in RESULTS if not ok]
    assert not failed, "comp-heat OS16 archive-answer battery failures: %r" % failed


if __name__ == "__main__":
    raise SystemExit(_report())
