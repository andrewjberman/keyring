"""
NFRA_COMPPROOF Workstream-B -- corpus-loader + root-cause STRIP + the DIFF-GATE (AC#1, the hard gate).

Binds the pinned top-20 (corpus.py) and, per incident, emits TWO artifacts:
  - SOLVER-VIEW: symptom_as_first_seen + the live-estate access note + the comp-tool surface ONLY.
    NEVER the root cause. This is the blind-solver's entire input.
  - SEALED JUDGE-VIEW: true_root_cause + how_it_was_actually_found + citation. CVO-only (TO-B2).

The isolation is STRUCTURAL (the solver-view is built from solver_visible_fields() ONLY; the sealed
fields are a separate dict never folded in) AND VERIFIED by a DIFF-GATE: for every incident, the
root-cause DISTINCTIVE terms (terms in the root cause but NOT already in the symptom) must NOT appear
in the solver-view, and the full root_cause string must not be a substring of it. Distinctive-term
gating (not naive all-term) avoids false-positives on words the symptom legitimately shares with the
root cause (e.g. "stale", "AUA") while catching REAL leakage of the mechanism. A run where the gate
fails for ANY incident is VOID -- B would measure nothing (arch doc sec 1.2 / AC#1).

Author: 0.8.0_AE_CloudComp~D (NFRA_COMPPROOF.B1, CTO arch 1315f9a03). 2026-07-01.
"""

from __future__ import annotations

import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import corpus  # noqa: E402

ESTATE_ACCESS = ("live graph @ the marker HEAD (comp-kuzu / comp-depth) + the served/live AWS estate "
                 "(read-only) -- the same substrate an on-call agent had at incident time")

# Terms too generic to count as root-cause LEAKAGE (would false-positive the gate).
_STOP = frozenset((
    "the", "a", "an", "and", "or", "but", "of", "to", "in", "on", "for", "with", "is", "was", "are",
    "were", "be", "been", "it", "its", "that", "this", "these", "those", "by", "as", "at", "not",
    "no", "nor", "so", "than", "then", "into", "onto", "from", "up", "out", "off", "over", "under",
    "via", "per", "each", "any", "all", "some", "one", "two", "3x", "twice", "while", "kept",
    "look", "looks", "shows", "show", "seem", "seems", "value", "values", "number", "numbers",
    "data", "served", "live", "healthy", "wrong", "stale", "frozen", "freeze", "froze", "phantom",
    "aua", "nna", "when", "where", "what", "which", "who", "how", "why", "every", "same", "class",
))


def _terms(text: str) -> set:
    """Significant lowercase word/identifier tokens (len>3, non-stopword). Splits on non-alnum but
    keeps snake_case/dotted identifiers together (they are the distinctive mechanism tokens)."""
    toks = re.findall(r"[A-Za-z0-9_.]+", (text or "").lower())
    out = set()
    for t in toks:
        t = t.strip("._")
        if len(t) > 3 and t not in _STOP:
            out.add(t)
    return out


def _case_id(incident: dict) -> str:
    """OPAQUE solver-facing id (B-NN by rank) -- the descriptive incident id leaks mechanism terms."""
    return "B-%02d" % incident["rank"]


def solver_view(incident: dict) -> dict:
    """The blind-solver's ENTIRE input: an OPAQUE case_id + the symptom/date + estate access + tool
    surface. NO descriptive id, NO failure_class, NO answer."""
    view = {"case_id": _case_id(incident)}
    view.update({k: incident[k] for k in corpus.solver_visible_fields() if k in incident})
    view["estate_access"] = ESTATE_ACCESS
    view["tool_surface"] = list(corpus.SOLVER_TOOL_SURFACE)
    view["task"] = ("From the symptom + the live estate + the tools ONLY, reach the TRUE root cause "
                    "via graph traversal + comp-tools. Record your traversal path, your concluded "
                    "root cause, and a self-confidence. You do NOT have the answer.")
    return view


def judge_view(incident: dict) -> dict:
    """The SEALED judge-view (CVO/TO-B2 only): case_id + real id + the sealed fields + citation.
    Never to the solver."""
    jv = {"case_id": _case_id(incident), "id": incident["id"]}
    jv.update({k: incident[k] for k in corpus.sealed_fields() if k in incident})
    jv["citation"] = incident.get("citation")
    return jv


def _view_text(view: dict) -> str:
    """Serialize the solver-view to a single lowercased string for the leak-check."""
    parts = []
    for v in view.values():
        parts.append(" ".join(v) if isinstance(v, (list, tuple)) else str(v))
    return " ".join(parts).lower()


def diff_gate(incident: dict) -> dict:
    """The STRIP proof for ONE incident: assert the root cause did not leak into the solver-view.
    Returns {id, passed, leaked_terms, full_string_leak}. passed iff NEITHER the distinctive
    root-cause terms NOR the full root_cause string appear in the solver-view."""
    # Check the INCIDENT-SPECIFIC solver content only (case_id + date + symptom). The fixed
    # scaffolding (estate_access / tool_surface / task) is identical boilerplate for all 20 -- the
    # solver has it regardless of the incident, so a scaffolding word coinciding with a sealed term
    # (comp-freshness ~ 'freshness'; "marker HEAD" ~ 'head'; task "symptom/path/self") is NOT an
    # incident-mechanism leak. The gate's job: does THIS incident's symptom reveal the mechanism?
    sv = solver_view(incident)
    incident_text = " ".join(str(sv.get(k, "")) for k in ("case_id", "date", "symptom_as_first_seen")).lower()
    sv_tokens = {t.strip("._") for t in re.findall(r"[A-Za-z0-9_.]+", incident_text)}
    rc = incident.get("true_root_cause", "")
    # distinctive = mechanism terms across ALL sealed fields (root cause + how-found + failure_class)
    # but NOT already in the symptom. Exact-token match (no substring false-positives).
    sealed_text = " ".join(str(incident.get(f, "")) for f in corpus.sealed_fields())
    symptom_terms = _terms(incident.get("symptom_as_first_seen", ""))
    distinctive = _terms(sealed_text) - symptom_terms
    leaked = sorted(t for t in distinctive if t in sv_tokens)
    full_leak = bool(rc) and rc.lower() in incident_text
    return {"id": incident["id"], "passed": (not leaked and not full_leak),
            "leaked_terms": leaked, "full_string_leak": full_leak}


def diff_gate_all(incidents=None) -> dict:
    """Run the DIFF-GATE for ALL incidents. Returns {passed, n, results, violations}. passed iff every
    incident's strip holds (AC#1: root_cause NOT-IN solver_view for ALL 20)."""
    incidents = corpus.INCIDENTS if incidents is None else incidents
    results = [diff_gate(i) for i in incidents]
    violations = [r for r in results if not r["passed"]]
    return {"passed": not violations, "n": len(results), "results": results, "violations": violations}


def scaffolding_fields() -> tuple:
    """Solver-view fields that are FIXED boilerplate (incident-AGNOSTIC) -- estate_access + tool_surface
    + task. The diff-gate EXCLUDES these (they are identical for all 20, so they cannot leak an
    incident's mechanism). See assert_scaffolding_invariant."""
    return ("estate_access", "tool_surface", "task")


def assert_scaffolding_invariant(incidents=None) -> dict:
    """CTO arch-lead GUARD (B1 review 141311Z): the diff-gate's exclude-the-scaffolding scoping is
    sound ONLY while the scaffolding stays IDENTICAL across all 20 solver-views (incident-agnostic).
    If it is ever PARAMETERIZED per-incident (a custom tool-hint / per-incident estate-scope / task-
    framing), it COULD then carry a mechanism leak -> the diff-gate MUST widen to cover it. This guard
    asserts the invariant; a False return is the signal to widen the gate. Returns
    {invariant_holds, divergent_fields}."""
    incidents = corpus.INCIDENTS if incidents is None else incidents
    ref, divergent = None, set()
    for inc in incidents:
        sv = solver_view(inc)
        scaf = {k: sv.get(k) for k in scaffolding_fields()}
        if ref is None:
            ref = scaf
        else:
            for k in scaffolding_fields():
                if scaf.get(k) != ref.get(k):
                    divergent.add(k)
    return {"invariant_holds": not divergent, "divergent_fields": sorted(divergent)}


def load(incident_id: str = None):
    """Load one incident (by id) or all -- returning (solver_view, judge_view) pairs. The pair is the
    unit the spawner (solver-view) + the judge (judge-view) consume; the strip is gate-verified first."""
    idx = {i["id"]: i for i in corpus.INCIDENTS}
    if incident_id is not None:
        inc = idx[incident_id]
        return solver_view(inc), judge_view(inc)
    return [(solver_view(i), judge_view(i)) for i in corpus.INCIDENTS]


def main() -> int:
    gate = diff_gate_all()
    print("=== NFRA_COMPPROOF B corpus-loader -- STRIP DIFF-GATE (root_cause NOT-IN solver_view) ===")
    print("  incidents: %d" % gate["n"])
    for r in gate["results"]:
        tag = "OK  " if r["passed"] else "LEAK"
        extra = "" if r["passed"] else "  leaked=%s full=%s" % (r["leaked_terms"][:5], r["full_string_leak"])
        print("  [%s] %s%s" % (tag, r["id"], extra))
    print("  DIFF-GATE: %s (%d/%d strip-clean)" % (
        "PASS" if gate["passed"] else "FAIL -- VOID", gate["n"] - len(gate["violations"]), gate["n"]))
    inv = assert_scaffolding_invariant()
    print("  SCAFFOLDING-INVARIANT: %s%s" % (
        "HOLDS (diff-gate exclude-scaffolding scoping sound)" if inv["invariant_holds"]
        else "DIVERGED -> WIDEN THE DIFF-GATE", "" if inv["invariant_holds"] else " %s" % inv["divergent_fields"]))
    return 0 if (gate["passed"] and inv["invariant_holds"]) else 2


if __name__ == "__main__":
    sys.exit(main())
