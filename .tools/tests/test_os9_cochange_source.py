#!/usr/bin/env python3
"""test_os9_cochange_source.py -- NFRA_OUTSET TO-OS-s-9 / criterion O9-AC1.

THE QUESTION: do the report's GROUP B co-change rows come from the TOOL'S PUBLISHED ARTIFACT?

Run at both required grains:
  python .tools/tests/test_os9_cochange_source.py
  python -m pytest -q .tools/tests/test_os9_cochange_source.py

WHAT THIS PROVES, and the RED MUTANT the criterion names is arm B2, EXECUTED not described:
  A  with an OS-s-10 seam prefix configured, _stratum_cochange renders the ARTIFACT's rows,
     the tool's vintage and the tool's denominators -- and the rows are DISTINGUISHABLE from
     anything the host git path can produce, so "it came from the artifact" is falsifiable.
  B2 RED MUTANT: the host-git path RESTORED at source (the seam branch removed from a temp copy
     of the runner) must make arm A's assertion fail. A mutant that changes nothing proves
     nothing.
  C  a FAILED publish reads FAILED, never a clean empty -- absent / not-JSON / foreign-tag /
     stale / future-dated / unmapped-answer-state, each a non-OK stratum carrying its reason.
  D  FWD-6's DECLARATION: with NO seam configured the host copy still renders, and its
     denominator DECLARES what it stands in for. A mutant that strips the declaration fails.
  E  the GRAIN measurement the declaration rests on, re-measured live rather than asserted:
     .tools/comp-cochange answers AGENT-TYPE co-movement, not resource co-change.

NO AWS, NO NETWORK. Arms A-D run against a tempfile directory with an injected loader. Arm E runs
the co-change ENGINE directly under sys.executable -- never a bash launcher -- which sidesteps two
measured host hazards at once: a bare subprocess.run(["bash", ...]) reaches the WSL stub, and a
subprocess timeout= does not bound a shell launcher because the grandchild holds the stdout pipe.
"""
from __future__ import annotations

import datetime as _dt
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "infra" / "aws" / "ec2" / "estate-report-runner" / "estate_report_runner.py"
COCHANGE_ENGINE = ROOT / "org" / "modules" / "graph" / "comp_cochange.py"

# The runner reads six env vars AT IMPORT. Fake values; no arm makes an AWS call.
RUNNER_ENV = {
    "ESTATE_REPORT_BUCKET": "os9-battery-not-a-real-bucket",
    "ESTATE_GITHUB_SECRET_ID": "x", "ESTATE_KIMI_SECRET_ID": "x",
    "ESTATE_KIMI_URL": "http://127.0.0.1:1", "ESTATE_KIMI_MODEL": "x",
    "ESTATE_REPO_URL": "http://127.0.0.1:1/x.git",
}

# The RED MUTANT the criterion names: restore the host-git path by deleting the seam branch, so
# a configured prefix is ignored and GROUP B is computed on the host again.
# RE-POINTED by NFRA_OUTSET OS-s-11, which added `reproduce=_outset_trace(r, src)` to this
# same return. The anchor's uniqueness assert REFUSED rather than mutating nothing -- which
# is the W2-S17 failure mode (a mutant that silently stops falsifying) caught by design.
# The anchor is deliberately the WHOLE branch, so any future edit to it breaks loudly here.
# RE-POINTED A SECOND TIME by NFRA_OUTSET OS-s-14, which replaced this branch with a DECLARED
# SOURCE PRECEDENCE (comp_cochange.json then comp_fedobs_coevolution.json, where only ABSENCE
# advances the search). The uniqueness assert refused again, exactly as NFRA_OUTSET-W2-S19
# predicted on the face of this very order -- a re-point job, not a break. The mutant's INTENT
# is unchanged: ignore any configured prefix so the host-git path is restored.
SEAM_BRANCH_ANCHOR = '''    prefix = OUTSET_SEAM_PREFIX if prefix is ... else prefix
    if prefix:
        rd = loader or _outset_loader
        rnow = now or datetime.now(timezone.utc)
        age = OUTSET_SEAM_MAX_AGE_HOURS if max_age_hours is None else max_age_hours
        tried = []
        for key, grain, grain_note in OUTSET_GROUP_B_SOURCES:
            src = prefix.rstrip("/") + "/" + key
            r = _outset_read(src, rd, rnow, age)
            tried.append(key)
            if r["status"] != "OK" and r.get("absent"):
                continue          # ONLY absence advances the search -- see OUTSET_GROUP_B_SOURCES
            den = r["denominator"]
            vin = "%s @%s" % (r["vintage"], pin)
            if grain_note:
                den = "%s -- %s" % (den, grain_note)
                vin = "%s [grain=%s, NOT resource-grain]" % (vin, grain)
            return _stratum("B_relationships", GROUP_QUESTIONS["B"], r["rows"], vin, den,
                            status=r["status"], error=r["error"],
                            reproduce=_outset_trace(r, src))
        # Every declared source was ABSENT. A prefix IS configured, so a publish was expected:
        # this is a FAILED stratum carrying what it looked for, never a silent fall-through to
        # the host stand-in (which would render a host number under a "seam configured" run and
        # tell the reader nothing about the missing publishes).
        return _stratum(
            "B_relationships", GROUP_QUESTIONS["B"], [],
            "UNREAD (seam configured at %s) @%s" % (prefix, pin),
            "UNREAD -- no GROUP B seam artifact is published under this prefix",
            status="INSTRUMENT_FAILED",
            error="every declared GROUP B seam source is ABSENT under a CONFIGURED prefix: "
                  "%s. Each was looked for and none was published. A configured-and-empty "
                  "prefix is a FAILED publish, not a reason to quietly compute a host "
                  "number instead." % ", ".join(tried),
            reproduce=_trace(
                "comp-cochange (resource grain) or comp-fedobs coevolution (file-pair grain)",
                ["python .tools/comp-fedobs coevolution --json",
                 "# then publish through org/modules/heatmap/outset_seam.py as "
                 "<prefix>/" + OUTSET_FEDOBS_KEY],
                "no artifact @%s" % pin, "not-reproducible",
                "nothing was read, so there is nothing to re-run: the recipe here is what WOULD "
                "make this stratum reproducible. Neither producer is registered in "
                "SEAM_PRODUCERS (NFRA_OUTSET-W2-S15)."))
'''
SEAM_BRANCH_MUTANT = '''    prefix = None   # RED MUTANT: seam ignored, host-git path restored
'''

# The arm-D mutant: the declaration silently emptied AT ITS DEFINITION, so BOTH host-path exits
# lose it at once. An earlier version of this mutant stripped only the computed exit's use of the
# constant, and D3 passed while the git-FAILED exit still carried the declaration -- a mutant that
# leaves a second live carrier does not falsify the arm it is pointed at.
DECL_ANCHOR = 'COCHANGE_STANDS_IN_FOR = ('
DECL_MUTANT = ('COCHANGE_STANDS_IN_FOR = ""   # RED MUTANT: declaration emptied' + chr(10)
               + '_OS9_DEAD = (')

RESULTS: list[tuple[str, bool, str]] = []


def _record(name: str, ok: bool, detail) -> None:
    RESULTS.append((name, bool(ok), str(detail).replace("\n", " ")[:300]))


def _load(path, name):
    """Import a runner copy under fake env, restoring the environment afterwards."""
    keep = {}
    for k, v in RUNNER_ENV.items():
        keep[k] = os.environ.get(k)
        os.environ[k] = v
    # Never let a real seam prefix from the ambient environment leak into an arm.
    keep["ESTATE_OUTSET_SEAM_PREFIX"] = os.environ.pop("ESTATE_OUTSET_SEAM_PREFIX", None)
    try:
        spec = importlib.util.spec_from_file_location(name, str(path))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    finally:
        for k, v in keep.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


NOW = _dt.datetime(2026, 9, 5, 12, 0, 0, tzinfo=_dt.timezone.utc)


def _artifact(rows, *, produced=None, state="OK", tag="NFRA_OUTSET/OS-s-10"):
    return {
        "schema_version": 1,
        "seam": tag,
        "tool": "comp-cochange (resource grain)",
        "question": "Which resources change together?",
        "argv": ["comp-cochange", "matrix", "--json"],
        "rc": 0,
        "answer_state": state,
        "answer_state_claim": "measured",
        "denominators": {"pairs_observed": 2, "tool_scalars": {"commits": 41}},
        "vintage": {"answer_produced_utc": (produced or NOW - _dt.timedelta(hours=2)).strftime(
            "%Y-%m-%dT%H:%M:%SZ"), "tool_reported": "repo @deadbeef", "claim": "measured"},
        "rows": rows,
        "error": None,
        "payload_excerpt": None,
    }


# A row shape no host git walk can ever emit: the host builds "<a> <-> <b>" from chain labels
# resolved out of the live repo, so a sentinel token makes provenance FALSIFIABLE rather than
# merely plausible.
SENTINEL = "OS9-SENTINEL-PAIR-NOT-FROM-GIT"
ARTIFACT_ROWS = [{"pair": SENTINEL, "co_commits": 99, "each_total": [99, 99]},
                 {"pair": "second <-> row", "co_commits": 7, "each_total": [7, 7]}]


def _write(d: Path, doc) -> str:
    d.mkdir(parents=True, exist_ok=True)
    p = d / "comp_cochange.json"
    p.write_text(json.dumps(doc), encoding="utf-8")
    return str(d)


def _loader(source: str) -> str:
    with open(source, encoding="utf-8") as fh:
        return fh.read()


def _call(mod, prefix, maps=None, now=None, max_age=None):
    return mod._stratum_cochange("/nonexistent-repo", NOW, maps or {}, "PIN",
                                 prefix=prefix, loader=_loader, now=now or NOW,
                                 max_age_hours=26.0 if max_age is None else max_age)


# =============================================================================================
def arm_a_artifact_is_the_source(mod, tmp):
    s = _call(mod, _write(tmp / "ok", _artifact(ARTIFACT_ROWS)))
    from_artifact = (s["status"] == "OK"
                     and [r.get("pair") for r in s["rows"]] == [r["pair"] for r in ARTIFACT_ROWS]
                     and SENTINEL in json.dumps(s["rows"]))
    _record("A1 rows ARE the artifact's rows", from_artifact,
            "status=%s row_count=%s first_pair=%r" %
            (s["status"], s["row_count"], s["rows"][0].get("pair") if s["rows"] else None))
    _record("A2 vintage names the TOOL, not the host",
            "comp-cochange" in s["vintage"] and "host git" not in s["vintage"],
            s["vintage"])
    _record("A3 denominator carries the TOOL's denominators",
            "pairs_observed=2" in s["denominator"] and "commits=41" in s["denominator"],
            s["denominator"])
    return s


def arm_b_red_mutant(tmp):
    """The RED MUTANT the criterion names: host-git path restored AT SOURCE."""
    src = RUNNER.read_text(encoding="utf-8")
    assert src.count(SEAM_BRANCH_ANCHOR) == 1, "seam-branch anchor not unique"
    mpath = tmp / "runner_hostgit_mutant.py"
    mpath.write_text(src.replace(SEAM_BRANCH_ANCHOR, SEAM_BRANCH_MUTANT), encoding="utf-8")
    mod = _load(mpath, "os9_runner_mutant")
    s = _call(mod, _write(tmp / "mut", _artifact(ARTIFACT_ROWS)))
    # Under the mutant the configured prefix is ignored: the sentinel CANNOT appear, and the
    # host path is reached (it fails on the nonexistent repo, which is itself a non-OK stratum).
    broke = SENTINEL not in json.dumps(s["rows"])
    _record("B2 RED MUTANT (host-git path restored) breaks arm A", broke,
            "status=%s rows=%d sentinel_present=%s" %
            (s["status"], len(s["rows"]), not broke))
    return broke


def arm_c_failed_publish_reads_failed(mod, tmp):
    cases = []
    d = tmp / "absent"
    d.mkdir(parents=True, exist_ok=True)
    cases.append(("ABSENT", _call(mod, str(d)), "ABSENT"))
    d = tmp / "notjson"
    d.mkdir(parents=True, exist_ok=True)
    (d / "comp_cochange.json").write_text("{not json", encoding="utf-8")
    cases.append(("UNREADABLE/not-JSON", _call(mod, str(d)), "not JSON"))
    cases.append(("FOREIGN TAG",
                  _call(mod, _write(tmp / "tag", _artifact(ARTIFACT_ROWS, tag="SOMEONE/ELSE"))),
                  "not an"))
    cases.append(("STALE",
                  _call(mod, _write(tmp / "stale",
                                    _artifact(ARTIFACT_ROWS,
                                              produced=NOW - _dt.timedelta(hours=80)))),
                  "STALE"))
    cases.append(("FUTURE-DATED",
                  _call(mod, _write(tmp / "future",
                                    _artifact(ARTIFACT_ROWS,
                                              produced=NOW + _dt.timedelta(hours=9)))),
                  "FUTURE"))
    cases.append(("UNMAPPED answer_state",
                  _call(mod, _write(tmp / "unmapped",
                                    _artifact(ARTIFACT_ROWS, state="NOT_A_DECLARED_STATE"))),
                  "outside the seam's declared domain"))
    n_ok = 0
    for label, s, token in cases:
        good = (s["status"] != "OK" and s["rows"] == [] and s["row_count"] is None
                and s["instrument_error"] and token.lower() in s["instrument_error"].lower())
        n_ok += good
        _record("C %s -> non-OK with its reason" % label, good,
                "status=%s err=%s" % (s["status"], (s["instrument_error"] or "")[:110]))
    _record("C ALL failure modes are non-OK and non-empty-clean", n_ok == len(cases),
            "%d of %d" % (n_ok, len(cases)))


def arm_d_declaration(tmp):
    """FWD-6: if the host copy stays it DECLARES which tool it stands in for."""
    mod = _load(RUNNER, "os9_runner_decl")
    decl = mod.COCHANGE_STANDS_IN_FOR
    needed = ["STAND-IN", "comp-cochange", "grain", "OS-s-10", "claim=host-computed"]
    missing = [t for t in needed if t.lower() not in decl.lower()]
    _record("D1 declaration names the tool, the grain and the seam key", not missing,
            "missing=%s len=%d" % (missing, len(decl)))
    # It must reach the RENDERED stratum on BOTH host-path exits, not just live in a constant.
    # The FAILURE exit matters most: without the declaration a reader sees GROUP B
    # INSTRUMENT_FAILED and concludes a TOOL failed, when no tool was ever called.
    s_fail = _call(mod, None)                       # /nonexistent-repo -> the git-FAILED exit
    ok_fail = decl in s_fail["denominator"] and "STAND-IN" in s_fail["vintage"]
    _record("D2a declaration reaches the rendered stratum on the git-FAILED exit", ok_fail,
            "status=%s vintage=%s" % (s_fail["status"], s_fail["vintage"][:90]))
    s_ok = mod._stratum_cochange(str(ROOT), _dt.datetime.now(_dt.timezone.utc),
                                 {"lambda_prefixes": [], "ec2_prefixes": [],
                                  "producer_paths": [], "prod_to_thread": {}},
                                 "PIN", prefix=None)
    ok_live = decl in s_ok["denominator"] and "STAND-IN" in s_ok["vintage"]
    _record("D2b declaration reaches it on the COMPUTED exit (live repo)", ok_live,
            "status=%s rows=%s vintage=%s" %
            (s_ok["status"], s_ok["row_count"], s_ok["vintage"][:90]))
    # RED MUTANT: strip the declaration from the denominator -> D2's assertion must fail.
    src = RUNNER.read_text(encoding="utf-8")
    assert src.count(DECL_ANCHOR) == 1, "declaration anchor not unique"
    mpath = tmp / "runner_nodecl_mutant.py"
    mpath.write_text(src.replace(DECL_ANCHOR, DECL_MUTANT), encoding="utf-8")
    m2 = _load(mpath, "os9_runner_nodecl")
    s2_fail = _call(m2, None)
    s2_ok = m2._stratum_cochange(str(ROOT), _dt.datetime.now(_dt.timezone.utc),
                                 {"lambda_prefixes": [], "ec2_prefixes": [],
                                  "producer_paths": [], "prod_to_thread": {}},
                                 "PIN", prefix=None)
    gone = (m2.COCHANGE_STANDS_IN_FOR == ""
            and decl not in s2_fail["denominator"] and decl not in s2_ok["denominator"])
    _record("D3 RED MUTANT (declaration emptied) breaks D2a AND D2b", gone,
            "mutant constant=%r; declaration still in failed-exit=%s computed-exit=%s"
            % (m2.COCHANGE_STANDS_IN_FOR, decl in s2_fail["denominator"],
               decl in s2_ok["denominator"]))


def arm_e_grain_is_measured_not_asserted():
    """The declaration claims comp-cochange answers a DIFFERENT grain. Re-measure it."""
    try:
        p = subprocess.run([sys.executable, str(COCHANGE_ENGINE), "matrix",
                            "--since", "14 days ago", "--json"],
                           cwd=str(ROOT), capture_output=True, text=True, timeout=100)
        doc = json.loads(p.stdout)
    except Exception as exc:                                                # noqa: BLE001
        _record("E grain measurement", False, "could not run the co-change engine: %r" % (exc,))
        return
    tags = doc.get("active_tags") or []
    pairs = [tuple(r.get("pair") or []) for r in (doc.get("pairs") or [])]
    agent_grain = (doc.get("grain") in ("type", "serial")
                   and bool(tags)
                   and all(len(t) <= 3 and t.isupper() for t in tags))
    no_paths = not any("/" in str(x) for pr in pairs for x in pr)
    _record("E1 comp-cochange's own grain is AGENT, not resource",
            agent_grain and no_paths,
            "grain=%r active_tags=%r first_pair=%r pairs=%d" %
            (doc.get("grain"), tags[:8], pairs[0] if pairs else None, len(pairs)))


def main() -> int:
    print("=== OS-s-9 O9-AC1: the report's co-change rows come from the TOOL'S ARTIFACT ===")
    with tempfile.TemporaryDirectory(prefix="os9_") as td:
        tmp = Path(td)
        mod = _load(RUNNER, "os9_runner")
        arm_a_artifact_is_the_source(mod, tmp)
        arm_b_red_mutant(tmp)
        arm_c_failed_publish_reads_failed(mod, tmp)
        arm_d_declaration(tmp)
        arm_e_grain_is_measured_not_asserted()
    for name, ok, detail in RESULTS:
        print("  %s  %s: %s" % ("PASS" if ok else "FAIL", name, detail))
    n_ok = sum(1 for _, ok, _ in RESULTS if ok)
    n = len(RESULTS)
    print("=== test_os9_cochange_source: %s (%d/%d) ===" %
          ("PASS" if n_ok == n else "FAIL", n_ok, n))
    return 0 if n_ok == n else 1


def test_os9_cochange_source():
    """pytest entry point -- the same arms, one assertion."""
    assert main() == 0


if __name__ == "__main__":
    sys.exit(main())
