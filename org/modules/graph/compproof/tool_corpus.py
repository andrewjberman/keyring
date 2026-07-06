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
        # CONTROL (expected effective): does comp-freshness reach a usable freshness verdict for a TARGETED
        # single artifact? REACH=yes if the output carries a per-artifact STATUS + age verdict. rc 0 (PASS)
        # and 1 (a FAIL verdict found) are BOTH usable answers (usable_returncodes); only rc 2 (config/AWS
        # error) is a fall-back. This shows comp-freshness IS effective for the targeted-freshness question.
        "question": "Report the freshness STATUS of a single named served artifact.",
        "run": ["comp-freshness", "artifact", "s3://opal-data-bd/silver/prices/canonical_prices.parquet"],
        "answer_terms": ["status", "age_h", "fail_at_h", "warn"],
        "answer_substr": "",
        "reach_threshold": 1,
        "usable_returncodes": [0, 1],
        "usability_timeout_s": 60,
        "expected": "effective",
        "live_estate": True,
    },
    {
        "probe_id": "comp-freshness/full-chain-under-load",
        "tool": "comp-freshness",
        "tool_class": "artifact-freshness",
        # THE FIX-CATCH (grounded LIVE, Rule 22 -- NOT manufactured): the whole-BD-chain freshness scan is
        # a real, heavily-reached-for in-class question, but comp-freshness is TOO-SLOW-UNDER-LOAD for it
        # (observed >120s live -- the ADVI_BREAKS-class latency). Per PRD SS5.2 a correct-but-unusable-
        # under-load tool is a FUNCTIONAL MISS, not EFFECTIVE. usability_timeout_s=90 is the "usable in the
        # moment" SLA bar (an agent needing a freshness answer won't wait 90s+); exceeding it => too-slow
        # => EFFECTIVE=no => a real FIX (optimize/paginate the chain scan). The 90s cap also BOUNDS the
        # probe cost (killed at the SLA bar, never waits the full runtime).
        # NOTE: the earlier MDPF-coverage-gap hypothesis was RETIRED -- `comp-freshness --list` was grounded
        # LIVE 2026-07-02 and now carries 6 mdpf/aggregate_aua entries (added since 0.5.0's 06-25 FREEZE-DX
        # noted none). Rule 22: the doc-era prior was stale; no coverage FIX exists there today.
        "question": "Report the freshness of the entire BD gold chain in one pass (usable in-the-moment).",
        "run": ["comp-freshness", "chain", "bd"],
        "answer_terms": ["status", "pass", "fail", "stale"],
        "answer_substr": "",
        "reach_threshold": 1,
        "usable_returncodes": [0, 1],
        "usability_timeout_s": 90,
        "expected": "fix",
        "live_estate": True,
    },
]


def probes() -> list:
    """All probe dicts (the corpus)."""
    return list(TOOL_PROBES)


def solver_visible_fields() -> tuple:
    """Probe fields the tool-run MAY see. ONLY the question + the invocation -- NEVER the answer or the
    self-test `expected` label. (Mirror of corpus.solver_visible_fields for the B1 isolation invariant.)"""
    return ("probe_id", "tool", "tool_class", "question", "run", "usability_timeout_s", "live_estate")


def sealed_fields() -> tuple:
    """Judge-only fields -- NEVER folded into the tool-run payload (the sealed answer + the self-test
    label). tool_probe.probe_payload proves these do not leak into what the tool sees."""
    return ("answer_terms", "answer_substr", "reach_threshold", "expected")
