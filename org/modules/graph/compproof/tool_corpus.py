"""
NFRA_TOOLHEALTH.TH-A -- the per-TOOL/per-CLASS EFFECTIVE-probe corpus (the sealed answer-key).

Generalizes the COMPPROOF-B1 per-INCIDENT corpus to per-TOOL: for each comp-tool (or tool-class),
a small set of REPRESENTATIVE blind questions the tool CLAIMS to serve, each with a SEALED expected
answer (the distinctive terms a correct, reached answer must contain). The probe (tool_probe.py) runs
the tool against the LIVE estate with an answer-FREE payload and scores REACH x USABILITY -> EFFECTIVE.

ISOLATION (inherited from B1, HARD): the sealed `answer_terms` / `answer_substr` are NEVER handed to
the tool run -- only `question` + `run` (the invocation) are. tool_probe.probe_payload proves the strip.
A tool that could see its own expected answer = a VOID EFFECTIVE verdict (measures nothing).

Field contract per probe:
  probe_id      : opaque stable id (TOOL/CLASS-NN) -- what the emitted row keys its provenance on.
  tool          : the canonical comp-tool under test (comp-*/pipescript) -- the emit key TH-B reads.
  tool_class    : the CLASS of question the tool claims to serve (routing / freshness / impact / ...).
  question      : the plain-English blind question (solver-visible; carries NO mechanism/answer).
  run           : the argv list actually executed (subprocess) -- the tool invocation, answer-free.
  answer_terms  : distinctive tokens a REACHED answer must contain (>=THRESHOLD present => reach=yes).
  answer_substr : optional exact substring that alone proves reach (case-insensitive) -- OR-ed with terms.
  reach_threshold: how many distinct answer_terms must appear for reach=yes (default 1).
  usability_timeout_s: > this wall-clock (under load) = too-slow => FUNCTIONAL PARTIAL, not EFFECTIVE.
  expected      : self-test label only (effective|fix|unknown) -- NEVER fed to the run, NEVER scored-against.
  live_estate   : True if the run reaches AWS/live estate (needs creds); False = local (graph/cache/router).

Author: 0.8.0_AE_CloudComp~D (NFRA_TOOLHEALTH.TH-A, COO~B GO 2026-07-02). Reuses B1 un-forked.
"""

from __future__ import annotations

import os
import sys

# sovereign_held lives one dir up (compproof -> graph); reach it for the by-construction sovereign assert.
_GRAPH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _GRAPH not in sys.path:
    sys.path.insert(0, _GRAPH)
from sovereign_held import is_held_path, is_held_bucket  # noqa: E402


# The probe corpus. Kept SMALL + representative (per-tool, per-class) -- this is a RECURRING probe, not
# an exhaustive test suite; each entry is one class-representative question the tool claims to answer.
TOOL_PROBES = [
    {
        "probe_id": "comp-which/routing-01",
        "tool": "comp-which",
        "tool_class": "tool-routing",
        # Clean isolation: the question names NO tool + shares NO token with the sealed answer "comp-blast".
        "question": "Which comp-tool tells me what downstream breaks if I change a gold-script function?",
        "run": ["comp-which", "what downstream depends on a gold-script function I want to change"],
        "answer_terms": ["comp-blast"],
        "answer_substr": "comp-blast",
        "reach_threshold": 1,
        "usability_timeout_s": 60,
        "expected": "effective",
        "live_estate": False,
    },
    {
        "probe_id": "comp-which/routing-02",
        "tool": "comp-which",
        "tool_class": "tool-routing",
        # "stale" deliberately avoids the token "fresh(ness)" so the sealed answer "comp-freshness" does
        # NOT leak into the payload (isolation-clean per the strip gate). Unambiguous freshness intent
        # (no "platinum" token, which biases the router toward comp-platinum).
        "question": "Which comp-tool checks whether served gold data has gone stale?",
        "run": ["comp-which", "how do I check whether served gold data is stale"],
        "answer_terms": ["comp-freshness"],
        "answer_substr": "comp-freshness",
        "reach_threshold": 1,
        "usability_timeout_s": 60,
        "expected": "effective",
        "live_estate": False,
    },
    {
        "probe_id": "comp-freshness/single-artifact",
        "tool": "comp-freshness",
        "tool_class": "artifact-freshness",
        # POSITIVE control (expected effective): does comp-freshness reach a usable freshness verdict for a
        # TARGETED single artifact? REACH keys on the RESOLVED artifact_id `inf_orion_api_performance` --
        # NOT the column headers (status/age_h/fail_at_h), which comp-freshness prints UNCONDITIONALLY (even
        # a header-only / no-row result would false-match them; found live 2026-07-12, same class as the
        # discrimination fail_at_h bug). The id is NOT in the run argv (which carries only the s3 PATH), so
        # its presence PROVES the tool resolved config -> a real data row; a header/empty output never
        # contains it. rc 0 (PASS) and 1 (a FAIL verdict) are BOTH usable (usability gate); rc 2 = fall-back.
        # opal-data-inf is IN-SCOPE (sovereign hold 2026-07-09); corpus sovereign-safe BY CONSTRUCTION below.
        "question": "Report the freshness STATUS of a single named served artifact.",
        "run": ["comp-freshness", "artifact", "s3://opal-data-inf/silver/api_dims/performance/"],
        "answer_terms": ["inf_orion_api_performance"],   # the RESOLVED-row id, not a header token
        "answer_substr": "inf_orion_api_performance",
        "reach_threshold": 1,
        "usable_returncodes": [0, 1],
        "usability_timeout_s": 60,
        "expected": "effective",
        "live_estate": True,
    },
    {
        "probe_id": "comp-freshness/frozen-vs-fresh-discrimination",
        "tool": "comp-freshness",
        "tool_class": "artifact-freshness",
        "kind": "discrimination",
        # THE HONESTY KEYSTONE (the un-gameable NEGATIVE case; replaces the bd latency FIX-catch with a
        # false-GREEN catch -- a stronger, honester FIX-signal). A REACH x USABILITY probe is a SOFT exit-0
        # proxy for a PLAUSIBLE-BUT-WRONG answer, so it CANNOT catch the paradigm lie: comp-freshness saying
        # FRESH on a frozen-content / fresh-mtime artifact (its as_of/partition-key reader is ANTI-CORRELATED,
        # test_freshness_partition_key_anticorrelated.py). This probe STAGES that exact lie: write a synthetic
        # artifact with a FROZEN content date + a FRESH mtime to an IN-SCOPE scratch prefix, run comp-freshness
        # on it, and score effective by whether the tool CAUGHT the freeze (STALE => yes) or LIED (GREEN =>
        # no). The ORACLE = the content date the probe WROTE (grounded OTHER than comp-freshness, which reads
        # mtime) -- the anti-Goodhart anchor. Guaranteed cleanup; sovereign-safe scratch target. CTO gate
        # 2026-07-12: B1 per-run fixture (a committed fixture's mtime AGES; the per-run write IS the fresh mtime).
        "question": "Does comp-freshness catch a KNOWN-FROZEN artifact (content 30d old) whose S3 mtime is fresh?",
        "fixture": {
            "scratch_bucket": "opal-data-inf",          # IN-SCOPE only (asserted); never bd/schwab
            "scratch_prefix": "_toolprobe_scratch/",     # dedicated + namespaced; never a served/canonical key
            "content_as_of_days_ago": 30,                # the FROZEN content date = the independent oracle ground-truth
        },
        # VERDICT is the RC, not a substring (a `fail_at_h` header would false-match a "fail" term). comp-
        # freshness single-artifact: rc 0 = PASS (=> false-GREEN on the frozen fixture => effective=no),
        # rc 1 = a FAIL/STALE verdict (=> CAUGHT => yes), rc 2 = config/AWS error (=> VOID/unknown).
        "usable_returncodes": [0, 1],
        "usability_timeout_s": 60,
        "expected": "fix",   # self-test label: PRE-fix the discrimination catches comp-freshness's false-GREEN
        "live_estate": True,
    },
    {
        "probe_id": "comp-freshness/partition-key-frozen-vs-fresh",
        "tool": "comp-freshness",
        "tool_class": "artifact-freshness",
        "kind": "pk-discrimination",
        # SENSOR-COMPLETENESS (CTO D2, 2026-07-12). The keystone discrimination probe above measures the
        # AD-HOC `artifact`-mode MTIME-only miss (defect a; cmd_artifact:1058 permissive-default, no
        # _pk_check). This case measures the SIBLING partition-key miss (defect b): comp-freshness's
        # PARTITION-KEY mode reads _max_partition_date, whose `_DATE_KEY_RE.search(line)` (:347) takes the
        # FIRST date on an `aws s3 ls` line = the LastModified column, NOT the filename date-key -- so a
        # silver/<t>/<STALE-date>.parquet rewritten with a FRESH mtime reads GREEN (the FIX-TO defect,
        # 23a7be2a1). GREY-BOX BY NECESSITY: comp-freshness has NO config-override / partition-key CLI flag,
        # so the ad-hoc CLI cannot reach partition-key mode for a scratch fixture -- the probe stages a real
        # in-scope partition-keyed S3 fixture and exercises the REAL _check_artifact (partition-key path),
        # scoring on its computed STATUS (not a substring). The ORACLE = the FROZEN date-key filename the
        # probe WROTE (2001-01-01), independent of comp-freshness (which reads LastModified). VALIDATED live
        # 2026-07-12: the fixture reads status=PASS, partition_as_of=<today> (the mtime) -> effective="no".
        # POST the FIX-TO land, _max_partition_date reads 2001 -> status=FAIL -> effective="yes" (the loop
        # closes on defect b). FIXED date-key -> object never accumulates (overwrite, no delete).
        "question": "Does comp-freshness's PARTITION-KEY mode catch a frozen date-key (silver/<t>/<stale>.parquet) whose S3 mtime is fresh?",
        "fixture": {
            "scratch_bucket": "opal-data-inf",                    # IN-SCOPE only (asserted); never bd/schwab
            "scratch_prefix": "_toolprobe_scratch/pk/silver/toolprobe/",  # a silver/<table>/ shape; dedicated
            "frozen_date_key": "2001-01-01",                      # FIXED old date-key = the oracle; no accumulation
            "warn_age_hours": 30, "fail_age_hours": 48, "severity": "ERROR",
        },
        # VERDICT is comp-freshness's computed result["status"] (from _check_artifact), NOT a substring:
        # PASS => false-GREEN on a frozen date-key => effective="no"; WARN/FAIL/ESCALATED => CAUGHT => "yes";
        # a partition-UNCHECKED / MISSING / ERROR / staging failure => VOID/unknown (never a silent no).
        "usability_timeout_s": 60,
        "expected": "fix",   # self-test label: PRE-fix the partition-key mode false-GREENs the frozen date-key
        "live_estate": True,
    },
]


def _scratch_uri(p: dict) -> str | None:
    """The scratch write-target a discrimination probe stages its fixture at (for the sovereign assert)."""
    fx = p.get("fixture")
    if not fx:
        return None
    return "s3://%s/%s" % (fx.get("scratch_bucket", ""), fx.get("scratch_prefix", ""))


def assert_sovereign_safe(probe_list: list | None = None) -> None:
    """SOVEREIGN-SAFE BY CONSTRUCTION (CTO 2026-07-12): NO probe may target a held bd/schwab path or bucket
    -- not in its `run` argv, not in its discrimination fixture scratch target. A held target would make the
    recurring probe read opal-data-bd on a re-run. This fails the corpus LOAD (never a silent bd read), and
    is the same canonical sovereign_held predicate the whole estate uses. Vigilance-independent."""
    offenders = []
    for p in (probe_list if probe_list is not None else TOOL_PROBES):
        for tok in list(p.get("run", [])):
            s = str(tok)
            if is_held_path(s) or is_held_bucket(s):
                offenders.append("%s run: %s" % (p.get("probe_id"), s))
        su = _scratch_uri(p)
        if su and (is_held_path(su) or is_held_bucket(su)):
            offenders.append("%s scratch: %s" % (p.get("probe_id"), su))
    if offenders:
        raise ValueError("SOVEREIGN VIOLATION -- probe corpus targets a held bd/schwab path (re-point to "
                         "inf/cot/mdpf):\n  " + "\n  ".join(offenders))


def probes() -> list:
    """All probe dicts (the corpus). Sovereign-asserted on every access -- a held target fails the load."""
    assert_sovereign_safe()
    return list(TOOL_PROBES)


def solver_visible_fields() -> tuple:
    """Probe fields the tool-run MAY see. ONLY the question + the invocation -- NEVER the answer or the
    self-test `expected` label. (Mirror of corpus.solver_visible_fields for the B1 isolation invariant.)"""
    return ("probe_id", "tool", "tool_class", "question", "run", "usability_timeout_s", "live_estate")


def sealed_fields() -> tuple:
    """Judge-only fields -- NEVER folded into the tool-run payload (the sealed answer + the self-test
    label). tool_probe.probe_payload proves these do not leak into what the tool sees. For a discrimination
    probe the tool run is `comp-freshness artifact <fixture s3 uri>` (built dynamically) and the VERDICT is
    the tool's RC (0=PASS => false-GREEN on the frozen fixture; 1=FAIL/STALE => caught) -- so the judge
    criterion is sealed by construction (never in the run argv, and never a substring of the tool's own
    stdout, which would false-match a `fail_at_h` column header); the tool must DERIVE freshness from the
    artifact content, not be told the verdict."""
    return ("answer_terms", "answer_substr", "reach_threshold", "expected")
