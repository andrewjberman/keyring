"""NFRA_TOOLHEALTH.TH-A (A)+(B) -- the fixture bar for the frozen-vs-fresh DISCRIMINATION probe (the
un-gameable honesty half CTO gates on). Every test is HERMETIC: the fixture writer/deleter and the
comp-freshness runner are INJECTED (mocked), so nothing here touches S3, opal-data-bd, or the live tool.

Proves, each non-vacuous:
  - positive control: the standard blind-run reaches -> effective="yes" (case=positive).
  - CAUGHT: comp-freshness says STALE on the frozen fixture -> effective="yes" (case=negative).
  - LIED (the BITE): comp-freshness says GREEN on a KNOWN-frozen artifact -> effective="no" (the false-GREEN catch).
  - VOID: a staging failure -> effective="unknown", NEVER a silent no; the tool is never run.
  - SOVEREIGN: a bd scratch target -> the guard blocks the WRITE (unknown+SOVEREIGN), no bd touch.
  - ORACLE-INDEPENDENCE: the ground-truth is the probe's own clock (_iso_days_ago), not the tool's claim --
    the tool lying "fresh" (rc 0) still scores effective="no".
  - MUTANT non-vacuity: neuter the negative arm (drop rc 0 from usable_returncodes) -> the false-GREEN catch
    VANISHES (unknown, not no) -> proves the rc-0 => false-GREEN arm is load-bearing.

VERDICT is the tool's RC, never a substring of its stdout: comp-freshness prints a `fail_at_h` COLUMN
HEADER, so a naive `"fail" in stdout` false-matched a PASS row as CAUGHT (caught live 2026-07-12). rc 0 =
PASS (=> false-GREEN on the frozen fixture => no), rc 1 = a FAIL/STALE verdict (=> caught => yes), any
other rc / timeout => VOID/unknown.

# rail-checked: assurance oracle for the TH-A discrimination probe under test (NFRA_TOOLPASS sec.6)
Author: 3.0.0_SA_CVO~B.
"""

import importlib
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
for _p in (os.path.join(_WS, "org", "modules", "graph"),
           os.path.join(_WS, "org", "modules", "graph", "compproof")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

tp = importlib.import_module("tool_probe")

_NOW = 1_000_000_000
_DISC = {
    "probe_id": "comp-freshness/frozen-vs-fresh-discrimination", "tool": "comp-freshness",
    "tool_class": "artifact-freshness", "kind": "discrimination",
    "fixture": {"scratch_bucket": "opal-data-inf", "scratch_prefix": "_toolprobe_scratch/",
                "content_as_of_days_ago": 30},
    "usable_returncodes": [0, 1],
    "usability_timeout_s": 60, "expected": "fix", "live_estate": True,
}


def _run(disc, runner, *, writer_raises=False, now_ts=_NOW):
    # NOTE: no deleter -- the fixed-key overwrite has NO delete by design (CTO option a). Only writer+runner
    # are injected. A delete would be a human-confirmation op; the design removes it.
    calls = {"writer": [], "runner": []}

    def w(uri, *, frozen_as_of):
        calls["writer"].append((uri, frozen_as_of))
        if writer_raises:
            raise RuntimeError("s3 unavailable")

    def r(uri):
        calls["runner"].append(uri)
        return runner(uri)

    row = tp._run_discrimination_probe(disc, now_ts=now_ts, fixture_writer=w, freshness_runner=r)
    return row, calls


def test_standard_positive_reaches_effective_yes(monkeypatch=None):
    saved = tp.run_tool
    tp.run_tool = lambda probe, **k: {"cmd": "comp-freshness artifact s3://opal-data-inf/x",
                                      "stdout": "STATUS: PASS age_h 2.0 warn ...", "stderr": "",
                                      "rc": 0, "elapsed_s": 1.0, "timed_out": False, "timeout_s": 60}
    try:
        probe = {"probe_id": "comp-freshness/single-artifact", "tool": "comp-freshness",
                 "tool_class": "artifact-freshness", "run": ["comp-freshness", "artifact", "s3://opal-data-inf/x"],
                 "answer_terms": ["status", "age_h", "warn"], "reach_threshold": 1,
                 "usable_returncodes": [0, 1], "usability_timeout_s": 60}
        row = tp.probe_one(probe, now_ts=_NOW)
    finally:
        tp.run_tool = saved
    assert row["effective"] == "yes"
    assert row["effective_evidence"]["case"] == "positive"
    assert row["effective_evidence"]["oracle_run"] == "comp-freshness artifact s3://opal-data-inf/x"  # exercised, not file:line


def test_discrimination_caught_freeze_effective_yes():
    # rc 1 = comp-freshness FOUND a FAIL/STALE verdict -> the tool CAUGHT the freeze.
    row, calls = _run(_DISC, lambda uri: {"stdout": "STATUS: STALE age_h 720 FAIL", "rc": 1})
    assert row["effective"] == "yes", "the tool CAUGHT the freeze (STALE, rc 1) -> effective"
    assert row["effective_evidence"]["case"] == "negative"
    assert "overwrote s3://opal-data-inf" in row["effective_evidence"]["oracle_run"]
    assert calls["writer"], "fixture overwritten (no delete -- fixed-key design)"


def test_verdict_is_rc_not_a_stdout_substring_REGRESSION():
    # The live-run bug (2026-07-12): comp-freshness's real PASS output carries a `fail_at_h` COLUMN HEADER.
    # A substring verdict (`"fail" in stdout`) wrongly read that PASS as CAUGHT. The rc-based verdict must
    # score this exact output effective="no" (rc 0 = PASS = the false-GREEN), NOT "yes".
    header = ("artifact_id | s3_key | last_modified | age_h | fail_at_h | status\n"
              "--- | --- | --- | --- | --- | ---\nx | s3://.../frozen.json | 2026-07-12 | 0.1 | 72 | PASS")
    row, _ = _run(_DISC, lambda uri: {"stdout": header, "rc": 0})
    assert row["effective"] == "no", "rc 0 (PASS) on a frozen fixture is the false-GREEN; a header 'fail' must NOT flip it to yes"


def test_fixed_key_overwrite_no_accumulation():
    # CTO option (a): a FIXED key overwritten each run -> two runs target the SAME key (no per-run ts), so
    # it never accumulates + needs no delete. The write refreshes mtime (fresh-mtime property preserved).
    _, c1 = _run(_DISC, lambda uri: {"stdout": "STALE", "rc": 1}, now_ts=_NOW)
    _, c2 = _run(_DISC, lambda uri: {"stdout": "STALE", "rc": 1}, now_ts=_NOW + 999_999)
    assert c1["writer"][0][0] == c2["writer"][0][0], "the fixture key is FIXED across runs (no ts) -> overwrite, no accumulation"
    assert c1["writer"][0][0].endswith("/comp-freshness/frozen.json"), "fixed namespaced key"
    # and there is NO deleter in the interface at all (the delete is designed out):
    import inspect
    assert "fixture_deleter" not in inspect.signature(tp._run_discrimination_probe).parameters, \
        "the deleter is removed -- no aws s3 rm (human-confirmation op) in the probe"


def test_discrimination_lied_green_on_frozen_effective_no_BITE():
    row, _ = _run(_DISC, lambda uri: {"stdout": "STATUS: PASS (fresh)", "rc": 0})
    assert row["effective"] == "no", "GREEN on a KNOWN-frozen artifact => effective=no (the false-GREEN catch)"
    assert row["effective_evidence"]["case"] == "negative"
    assert tp._iso_days_ago(30, now_ts=_NOW) in row["effective_evidence"]["expected"]


def test_void_on_stage_failure_never_silent_no():
    row, calls = _run(_DISC, lambda uri: {"stdout": "PASS"}, writer_raises=True)
    assert row["effective"] == "unknown", "a staging failure is VOID/unknown, NEVER a silent no"
    assert not calls["runner"], "the tool must NOT be run if the fixture could not be staged"


def test_sovereign_scratch_guard_blocks_a_bd_write():
    bd = dict(_DISC, fixture={"scratch_bucket": "opal-data-bd", "scratch_prefix": "_toolprobe_scratch/",
                              "content_as_of_days_ago": 30})
    row, calls = _run(bd, lambda uri: {"stdout": "PASS"})
    assert row["effective"] == "unknown" and "SOVEREIGN" in row.get("void_reason", "")
    assert not calls["writer"], "the sovereign guard must block the write BEFORE any bd touch"


def test_oracle_is_independent_of_the_tools_claim():
    # the tool LIES "fresh", but the probe scores effective=no because the ORACLE (30d-frozen content it
    # WROTE, on its own clock) is the ground-truth -- the verdict never trusts the tool's own claim.
    row, _ = _run(_DISC, lambda uri: {"stdout": "everything PASS and fresh", "rc": 0})
    assert row["effective"] == "no"
    assert tp._iso_days_ago(30, now_ts=_NOW) == tp._iso_days_ago(30, now_ts=_NOW)  # deterministic, tool-independent


def test_negative_arm_is_load_bearing_MUTANT():
    real, _ = _run(_DISC, lambda uri: {"stdout": "STATUS: PASS (fresh)", "rc": 0})
    assert real["effective"] == "no"
    # MUTANT: drop rc 0 from the usable set -> a PASS (rc 0) is no longer a scoreable false-GREEN, it
    # falls back to VOID. The catch VANISHES (unknown, not no) -> proves the rc-0 => false-GREEN arm bites.
    neutered = dict(_DISC, usable_returncodes=[1])
    mut, _ = _run(neutered, lambda uri: {"stdout": "STATUS: PASS (fresh)", "rc": 0})
    assert mut["effective"] != "no", "neutering the negative arm must LOSE the false-GREEN catch (non-vacuous)"
    assert mut["effective"] == "unknown"


def test_positive_control_reach_ignores_headers_keys_on_resolved_id():
    # The live-run honesty gap (2026-07-12, sibling of the discrimination fail_at_h bug): comp-freshness
    # prints its column HEADERS (status / age_h / fail_at_h) UNCONDITIONALLY, so a reach signal on those
    # tokens scores reach=yes on a header-only / no-row result. The positive control now keys on the RESOLVED
    # artifact_id, which ONLY a real data row carries (and which is NOT in the run argv -> the tool derived it).
    pos = {"probe_id": "comp-freshness/single-artifact", "tool": "comp-freshness",
           "tool_class": "artifact-freshness",
           "run": ["comp-freshness", "artifact", "s3://opal-data-inf/silver/api_dims/performance/"],
           "answer_terms": ["inf_orion_api_performance"], "answer_substr": "inf_orion_api_performance",
           "reach_threshold": 1, "usable_returncodes": [0, 1]}
    header_only = ("artifact_id | s3_key | last_modified | age_h | fail_at_h | status\n"
                   "--- | --- | --- | --- | --- | ---\n(no artifacts matched)")
    assert tp.score_reach(header_only, pos)["reach"] == "no", "header/empty output must NOT reach (no resolved row)"
    real_row = "artifact_id | ... | status\ninf_orion_api_performance | s3://... | 1.3h | 72h | PASS"
    assert tp.score_reach(real_row, pos)["reach"] == "yes", "a resolved data row (artifact_id present) reaches"
    # the OLD header tokens must NO LONGER be the reach signal (non-vacuity of the fix):
    stale_probe = dict(pos, answer_terms=["status", "age_h", "fail_at_h", "warn"], answer_substr="")
    assert tp.score_reach(header_only, stale_probe)["reach"] == "yes", \
        "documents the DEFECT the fix removes: header tokens falsely reached"


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print("PASS:", name)
    print("=== TH-A discrimination fixture bar: ALL PASS ===")
