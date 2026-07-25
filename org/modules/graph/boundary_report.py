"""boundary_report -- THE BOUNDARY-REPORT TYPE (NFRA_TOOLSTACK sensor layer).

The common type every sensor emits so sixty tools do not produce sixty incommensurable
lists. Finalized 2026-07-24 against the three open questions, Andrew-answered.

>> THIS IS A SEMANTIC COMMITMENT: unverifiable, latent errors, inherited by everything
   downstream. Get it wrong and a dimension is mis-shaped across the whole fleet. Every
   design decision below is therefore recorded WITH its reason. <<

THE THREE SETTLED QUESTIONS
---------------------------
1. ADDRESS PORTABILITY -> native address + a REQUIRED `address_space` tag. NOT a lossy
   common scheme.
   WHY: forcing a DAG node id into a YAML-key-path shape is VOCABULARY POVERTY (orthogonal
   shape #4) -- coercing an outcome the vocabulary cannot represent into the nearest
   expressible one. That would commit shape #4 INSIDE THE TYPE BUILT TO DETECT IT. The
   aggregation difficulty is real and it is the RIGHT difficulty: these addresses genuinely
   are not commensurable, and making aggregation easy by lying about commensurability is
   worse than aggregation being hard.
   CONSEQUENCE: aggregate on what IS shared -- cell, method, tool, head. NEVER compare paths.

2. METHOD is REQUIRED and is an ENUM, never free text.
   WHY: mention-derived and traversal-derived carry different confidence AND different
   failure DIRECTIONS (mention UNDER-reports; traversal is exact). Left as a string it drifts
   into prose within a month and the corpus becomes unaggregatable. The failure direction is
   carried in the enum itself so an aggregate can reason about its own denominator.

3. APPLICABILITY: N/A and 0 ARE DIFFERENT VALUES.
   WHY: this is the MACHINEFLAG arc's `AN ABSENT RESULT IS NOT A RESULT` law arriving in a
   new place. A DAG has no prose plane, so its `doc_only` cell is NOT-APPLICABLE, not zero.
   Summing nineteen N/As as zeros manufactures a FALSE DENOMINATOR. An aggregate must be able
   to say "of 60 tools, 41 have a doc plane, 19 do not" -- which is impossible if N/A renders
   as 0.
   ENFORCED: applicable=false <-> count IS NULL, both directions, as a hard conformance rule.

ASCII-only. No I/O. Pure type + validator.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# CLOSED ENUMS
# ---------------------------------------------------------------------------

#: HOW coverage was established. CLOSED -- a new method is a type change, reviewed.
#: `under_reports` / `over_reports` are the FAILURE DIRECTION, carried so an aggregate can
#: state the bias of its own denominator instead of blending silently.
METHODS = {
    "traversal": {
        "confidence": "exact",
        "under_reports": False,
        "over_reports": False,
        "meaning": "the tool actually walked the unit -- observed, not inferred",
    },
    "mention": {
        "confidence": "inferred",
        "under_reports": True,
        "over_reports": False,
        "meaning": "a name appears in consumer text; evidence of reference, NOT proof of traversal",
    },
    "declared": {
        "confidence": "asserted",
        "under_reports": False,
        "over_reports": True,
        "meaning": "a consumer DECLARES it walks this; a claim that can drift from reality",
    },
}

#: The four cells of the boundary map. CLOSED.
CELLS = {
    "covered": "mechanically accounted -- Route A territory",
    "member": "a row under a KNOWN axis -- Route A territory",
    "doc_only": "named in prose, no code walks it -- THE BOUNDARY",
    "orphan": "nothing downstream knows it exists -- Route C territory",
}

#: Address spaces. INTENTIONALLY NOT CLOSED -- new shapes will appear, and a closed set
#: here would be the frozen-enumeration defect. Unknown spaces are ALLOWED but REPORTED
#: (BR008), so a new space is visible rather than silent.
#:
#: ROUND-2 ITEM 5 REWORK (2026-07-25, design read @0a26851db, CVO~Z-sharpened): the set
#: -> a STATUSED dict, because the flat set carried the both-directions filter drift in
#: the type's OWN vocabulary (8 declared / 5 live-emitted / intersection 1), and two
#: declared terms were NEAR-MISSES for live ones -- rewarding the precisely-wrong term
#: with silence while flagging the accurately-novel one with BR008.
#: STATUSES:
#:   LIVE              -- measured emitted by a conformant sensor report (named).
#:   ANTICIPATED       -- declared for a NAMED sensor not yet emitting; MUST carry
#:                        owner + trigger (the L0b RESEMANT-deferral shape: an
#:                        ANTICIPATED with no trigger is a forgotten term with better
#:                        branding). Grep-provable: every ANTICIPATED entry carries
#:                        "owner:" and "trigger:" in its note.
#:   RETIRED-CANDIDATE -- no nameable owner/trigger exists; naming one would be
#:                        invention. Kept declared (mark, don't prune -- the design
#:                        read's ruling) pending the program owner's retire call.
#: Near-miss pairs are disambiguated IN-PLACE, at the term, where the mistake is made.
#:
#: >> METRIC WARNING (carry this wherever vocabulary health is measured): BR008's rate
#: is a BIASED ESTIMATOR of vocabulary health. It counts accurate-NOVEL emissions and
#: structurally CANNOT count precise-WRONG ones -- a near-miss declared term produces a
#: clean report about the wrong address space, silently. False-accepts are SILENT while
#: false-rejects are LOUD; loud errors self-correct, silent ones compound. Do NOT adopt
#: the BR008 rate as the health metric. <<
KNOWN_ADDRESS_SPACES = {
    # -- LIVE (measured, per the 5-report conformant corpus 2026-07-25) ------------------
    "dag_edge_type": {
        "status": "LIVE", "note": "an edge's KIND (e.g. CALLS); emitter: comp-blast sensor-3"},
    "code_call_site": {
        "status": "LIVE", "note": "a call site 'path:line:callee' in code text; emitter: "
        "comp-cache sensor-2. NOT code_branch_id (an if/else branch is not a call site)"},
    "dag_node_type": {
        "status": "LIVE", "note": "a node's KIND (e.g. LAMBDA); emitter: comp-blast "
        "sensor-3. NOT dag_node_id (identity, e.g. lambda:opal-foo, is a different space)"},
    "lambda_env_key": {
        "status": "LIVE", "note": "an env-var NAME on a Lambda's flat Variables map; "
        "emitter: item-1b env sensor"},
    "kuzu_schema_element": {
        "status": "LIVE", "note": "'table:<T>' / 'column:<T>.<c>' of a live Kuzu schema; "
        "emitter: item-1b kuzu sensor"},
    # -- ANTICIPATED: NONE. yaml_key_path was proposed here and RULED invention-by-
    #    citation at verify (CVO~Z 161223Z): SENSOR_CONTRACT s8.3 SEQUENCES comp-residue's
    #    emission but names neither an owner nor a trigger, and comp-residue is already
    #    recorded as a named NON-EMITTER in L2's coverage-of-itself -- "anticipated" and
    #    "known not to emit" cannot be asserted about the same tool simultaneously.
    #    0 ANTICIPATED + 7 RETIRED-CANDIDATE is the honest split: this vocabulary was
    #    declared ahead of its sensors and none of it arrived. -------------------------
    # -- RETIRED-CANDIDATE (no nameable owner/trigger; kept declared pending the
    #    program owner's retire ruling -- marked, not pruned) ---------------------------
    "yaml_key_path": {
        "status": "RETIRED-CANDIDATE", "note": "dotted dict-key path of a schema source "
        "(comp-residue's shape -- a sensor that exists and is a recorded NON-EMITTER; "
        "SENSOR_CONTRACT s8.3 sequences its emission but names no owner and no trigger, "
        "so ANTICIPATED would be invention-by-citation -- CVO~Z ruling 20260725T161223Z)"},
    "json_key_path": {
        "status": "RETIRED-CANDIDATE", "note": "no sensor names this shape; no owner/"
        "trigger nameable without invention"},
    "dag_node_id": {
        "status": "RETIRED-CANDIDATE", "note": "a node's IDENTITY (lambda:opal-foo). "
        "NOT dag_node_type (the KIND) -- the live near-miss: a node-KIND report emitted "
        "under this term would be precisely wrong and silent. No identity-addressed "
        "sensor exists or is named; no owner/trigger nameable without invention"},
    "code_branch_id": {
        "status": "RETIRED-CANDIDATE", "note": "an if/else branch in a router. NOT "
        "code_call_site (the live near-miss). The CODE-BRANCHES shape is real "
        "(shared-advisor-router, platform-or-pattern read) but no branch-addressed "
        "sensor exists or is named; no owner/trigger nameable without invention"},
    "cf_behavior_ordinal": {
        "status": "RETIRED-CANDIDATE", "note": "CloudFront behavior ordering -- a real "
        "shape with no named sensor; no owner/trigger nameable without invention"},
    "tf_resource_address": {
        "status": "RETIRED-CANDIDATE", "note": "a real shape with no named sensor; no "
        "owner/trigger nameable without invention"},
    "s3_prefix": {
        "status": "RETIRED-CANDIDATE", "note": "a real shape with no named sensor; no "
        "owner/trigger nameable without invention"},
}

REQUIRED_TOP = ("tool", "source", "address_space", "head", "surface_total", "cells")


class Violation:
    """A conformance violation. `code` is stable; message is human."""

    __slots__ = ("code", "where", "message")

    def __init__(self, code: str, where: str, message: str) -> None:
        self.code, self.where, self.message = code, where, message

    def __repr__(self) -> str:  # pragma: no cover - debug aid
        return "Violation(%s at %s: %s)" % (self.code, self.where, self.message)

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Violation)
            and (self.code, self.where) == (other.code, other.where)
        )


def _is_int(value) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def validate(report) -> list:
    """Validate a boundary report against the type. Returns a list of Violation.

    An EMPTY list means conformant. This validator is a CERTIFIER for SHAPE only -- it says
    nothing about whether the counts are true, only that the report cannot silently
    misrepresent N/A, method, or its own denominator.
    """
    out = []
    if not isinstance(report, dict):
        return [Violation("BR000", "<root>", "report must be a mapping")]

    for field in REQUIRED_TOP:
        if field not in report or report[field] in (None, ""):
            out.append(Violation("BR001", field, "required field missing or empty"))

    space = report.get("address_space")
    if isinstance(space, str) and space:
        if space not in KNOWN_ADDRESS_SPACES:
            out.append(Violation(
                "BR008", "address_space",
                "unknown address space %r -- ALLOWED but reported so a new shape is visible" % space))
    elif "address_space" not in [v.where for v in out]:
        out.append(Violation("BR006", "address_space",
                             "address_space is REQUIRED -- addresses are native and never coerced"))

    cells = report.get("cells")
    applicable_sum = 0
    if not isinstance(cells, dict):
        out.append(Violation("BR001", "cells", "cells must be a mapping of cell -> record"))
    else:
        for name, rec in cells.items():
            where = "cells.%s" % name
            if name not in CELLS:
                out.append(Violation("BR005", where, "unknown cell %r; closed set is %s"
                                     % (name, sorted(CELLS))))
                continue
            if not isinstance(rec, dict):
                out.append(Violation("BR001", where, "cell record must be a mapping"))
                continue

            applicable = rec.get("applicable")
            count = rec.get("count", "__missing__")
            if not isinstance(applicable, bool):
                out.append(Violation("BR003", where,
                                     "`applicable` must be an explicit bool -- absence is not false"))
                continue
            if count == "__missing__":
                out.append(Violation("BR001", where, "`count` required (int when applicable, null when not)"))
                continue

            # >> THE LOAD-BEARING INVARIANT: N/A and 0 are DIFFERENT VALUES. <<
            if applicable is False and count is not None:
                out.append(Violation(
                    "BR003", where,
                    "applicable=false MUST carry count=null, got %r -- rendering N/A as a number "
                    "manufactures a false denominator (AN ABSENT RESULT IS NOT A RESULT)" % (count,)))
            elif applicable is True and count is None:
                out.append(Violation(
                    "BR003", where,
                    "applicable=true MUST carry an integer count, got null -- 'I could not "
                    "measure' is not the same claim as 'this does not apply'"))
            elif applicable is True and not _is_int(count):
                out.append(Violation("BR003", where, "count must be an int when applicable, got %r" % (count,)))
            elif applicable is True:
                applicable_sum += count

            method = rec.get("method")
            if applicable is True:
                if method not in METHODS:
                    out.append(Violation("BR002", where + ".method",
                                         "method must be one of %s (ENUM, never free text), got %r"
                                         % (sorted(METHODS), method)))
            elif method is not None:
                out.append(Violation("BR002", where + ".method",
                                     "a non-applicable cell must carry method=null, got %r" % (method,)))

    total = report.get("surface_total")
    if _is_int(total) and isinstance(cells, dict):
        # Accounting is over APPLICABLE cells ONLY -- summing N/A cells is the false denominator.
        if applicable_sum != total:
            out.append(Violation(
                "BR004", "surface_total",
                "accounting does not balance: applicable cells sum to %d, surface_total=%d"
                % (applicable_sum, total)))

    for idx, item in enumerate(report.get("items") or []):
        where = "items[%d]" % idx
        if not isinstance(item, dict):
            out.append(Violation("BR001", where, "item must be a mapping"))
            continue
        if item.get("cell") not in CELLS:
            out.append(Violation("BR007", where + ".cell", "item cell %r not in the closed set"
                                 % (item.get("cell"),)))
        if item.get("method") not in METHODS:
            out.append(Violation("BR002", where + ".method",
                                 "item method must be an ENUM member, got %r" % (item.get("method"),)))
        if not item.get("address"):
            out.append(Violation("BR001", where + ".address",
                                 "address required, in the SOURCE's OWN address space (never coerced)"))
    return out


def denominator_note(reports) -> str:
    """The line an aggregate MUST print: applicability, never a sum of zeros.

    Answers "of N tools, how many even HAVE this cell?" -- the question that is impossible
    once N/A has been rendered as 0.
    """
    per_cell = {}
    for cell in sorted(CELLS):
        applicable = sum(1 for r in reports
                         if isinstance(r.get("cells", {}).get(cell), dict)
                         and r["cells"][cell].get("applicable") is True)
        per_cell[cell] = (applicable, len(reports))
    return " | ".join("%s: %d/%d tools applicable" % (c, a, n) for c, (a, n) in per_cell.items())


def vocabulary_denominators(reports) -> str:
    """BOTH vocabulary denominators, never one ratio (round-2 item 5, CVO~Z's addition).

    declared N / live-emitted M / intersection K -- because over-declared (N >> K) and
    under-conforming (M >> K) have OPPOSITE remedies (prune-or-mark vs fix-the-emitters)
    and a single ratio picks neither. Also prints the per-status composition so
    'declared for a named future sensor' is distinguishable from 'declared and
    forgotten' from the outside.
    """
    declared = set(KNOWN_ADDRESS_SPACES)
    emitted = {r.get("address_space") for r in reports if r.get("address_space")}
    inter = declared & emitted
    by_status = {}
    for term, meta in KNOWN_ADDRESS_SPACES.items():
        by_status.setdefault(meta["status"], []).append(term)
    status_part = " | ".join("%s: %d (%s)" % (s, len(ts), ", ".join(sorted(ts)))
                             for s, ts in sorted(by_status.items()))
    return ("address_space vocabulary: declared %d / live-emitted %d / intersection %d "
            "(undeclared-but-emitted: %s) || %s"
            % (len(declared), len(emitted), len(inter),
               ", ".join(sorted(emitted - declared)) or "none", status_part))
