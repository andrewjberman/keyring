#!/usr/bin/env python3
"""comp_promote_lifecycle -- NFRA_PROMOTE-P1: the promotion CONTRACT + LIFECYCLE + 5-INVARIANT GATE.

The plane's spine (PRD S4.2/S4.3), GENERALIZED from the two loops already forming (PRD S7 -- do not
greenfield): TH-C clause-A (comp_tool_health_gate.commission_for -- verdict -> TYPED ADVISORY
commission -> human ratifier -> zero auto-mutation) and the COMPLEARN-activation charter
(observe -> measure -> validate -> promote). This module is the machine BETWEEN a MOTIF candidate
(motif_promote_candidates.json) and the P2 materializers (comp_promote_materializer et al.): it
mints nothing into the substrate -- it produces the RATIFIED COMMISSION the materializers are
already gated on (comp_promote_materializer.materialize_live REFUSES without one), and refuses
every advance that violates an invariant.

THE STATE MACHINE (PRD S4.3; every transition CSE-logged -- promotion observes itself):

  CANDIDATE -> MEASURED -> PROPOSED -> RATIFIED  -> MATERIALIZED -> MONITORED -> SUSTAINED
      |           |                 -> REJECTED                        |     <-      |
      |           -> PARKED (below-threshold: a measured negative,     -> DEGRADED -> DEMOTED
      |              not a failure)
      -> DROPPED (absorbed @cb6a86177, DS~B lineage: no MEANINGFUL measure even AFTER coverage --
         de-candidated, not zombie-held; re-candidacy on NEW evidence only)

THE FIVE INVARIANTS (PRD S4.2 -- each a GATE that RAISES, never a doc):
  1 MEASURE-BEFORE-PROMOTE  -> MEASURED needs a real, non-pending measured effect (a correlation is
                               a candidate; a measured effect is the warrant). A PENDING measure
                               REFUSES -- "do NOT fake a measurement" (the P1 TO's honest gate).
  2 ANTI-GOODHART           -> PROPOSED needs a structural/generalizing attestation AND a
                               MEANINGFUL measurement (the absorbed DS~B floor: focused ratio >=
                               FEDOBS_RATIO_FLOOR, legacy co_sessions floor fallback) -- a
                               meaningless-but-well-formed measure never reaches the ratifier.
  3 HUMAN-RATIFY            -> RATIFIED needs the ROUTED ratifier's own record + THEIR commission_id.
                               This module NEVER self-mints a commission (zero auto-mutation:
                               grep-proof -- no substrate write exists in this file; the only writes
                               are its OWN manifest snapshot + CSE trail).
  4 REVERSIBLE              -> MATERIALIZED needs a declared demotion path + an EXERCISED
                               materializer receipt; DEMOTED needs an exercised demotion receipt.
  5 INSPECTABLE             -> every record carries its decompression chain; every transition
                               carries evidence + why; every transition emits a schema-validated
                               ProducerKind.PROMOTE CSE (@0.4, validate_or_raise, fail-closed).

RATIFY-OWNER ROUTING (PRD S8: cross-plane -> CTO; the four S4.1 classes are all cross-plane):
see PROMOTION_CLASSES. The commission builder generalizes clause-A's shape: verdict-equivalent
(the candidate + warrant), grounding (evidence the ratifier reads, not the label), proposed_to
(typed action + ratifier), auto_mutates: False -- always.

Storage (event-log-vs-state-snapshot separation, mirroring DS~B's manifest design):
  promote_lifecycle_manifest.json  -- the STATE snapshot {promotions: {candidate_id: record}}
  promote_lifecycle_cse.jsonl      -- the append-only transition CSE trail
Both are THIS plane's own files (additive). DS~B's promote_recognizer_manifest.json (the R3 named
critical surface) is NOT written here -- ever. The lifecycle hands a ratified commission TO the
materializer lane; the manifest write stays with its sole producer.

Usage:
  python comp_promote_lifecycle.py                  # report: every promotion + state + next gate
  python comp_promote_lifecycle.py --self-test      # the exercised red-fixture (all 5 invariants)

Author: 0.8.0_AE_CloudComp~Z (NFRA_PROMOTE.P1 build side, per the 2026-07-14 sovereign redirect
@14c2aeeba). Ratify roles unchanged: 1.0.0_SA_CTO (~Z lane holds them this session). 2026-07-14.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))

from cse_schema import (  # noqa: E402
    CSE as CSEvent, Entity, EntityRef, ProducerKind, Provenance, Qualifier,
    SCHEMA_VERSION, Transformation, validate_or_raise,
)

MANIFEST = os.path.join(_HERE, "promote_lifecycle_manifest.json")
CSE_TRAIL = os.path.join(_HERE, "promote_lifecycle_cse.jsonl")
CANDIDATES = os.path.join(WS, "org", "tier2_senior", "0.4.0_DS_ClientPlatform",
                          "deliverables", "motif_promote_candidates.json")

# The Concept-subject type-confidence (the SUBJECT's honest-low band, NOT the event's certainty --
# same CTO arch-gate note as comp_promote_materializer._PROMOTE_TYPE_CONFIDENCE).
_LIFECYCLE_TYPE_CONFIDENCE = 0.2
SCOPE = "promote.lifecycle"

# =============================================================================================
# ABSORBED from 0.4.0_DS_ClientPlatform~B's NFRA_PROMOTE_P1_promotion_engine.py per the CTO~Z
# convergence ruling @cb6a86177 (canonical = THIS module; DS~B's engine retires WITH PROVENANCE
# in the same change as the P3 monitor rewire, after the CVO delta re-cert). Lineage preserved:
#
# THE ANTI-GOODHART MEASUREMENT FLOOR -- "a single coincidental co-occurrence is NOT a warrant"
# (CTO ratify-ruling condition 2026-07-08: the 7 candidates were RATIFIED-AS-CANDIDATES with
# promotion WITHHELD -- the gate firing). meaningless-but-well-formed must not REACH the ratifier.
MEANINGFUL_CO_OCCURRENCE_FLOOR = max(2, int(os.environ.get("PROMOTE_ANTI_GOODHART_FLOOR", "2")))
# FEDOBS_RATIO_FLOOR=0.12: the CTO re-calibrated floor for the FOCUSED coupling measure (mid-gap
# of the natural split 0.094 -> 0.151; threshold-INSENSITIVE, chosen for robustness NOT outcome;
# the SEMCTL.FINALIZE focused_coupling_ratio@0.12 flip lineage). A PRE-FILTER only: the owner's
# promotion-ratify stays the FINAL meaningfulness gate (CTO note: 0.12 lets a modest-but-genuine
# coupling REACH the ratify rather than auto-rejecting). HOMED HERE ONCE (ruling term (c)) --
# promote_monitor and every other consumer import it from this module.
try:
    FEDOBS_RATIO_FLOOR = float(os.environ.get("FEDOBS_RATIO_FLOOR", "0.12"))
except ValueError:
    FEDOBS_RATIO_FLOOR = 0.12


def measurement_meaningful(m: dict) -> tuple:
    """Invariant-2's MEASUREMENT arm (DS~B's inv2_anti_goodhart, absorbed): gate on the FOCUSED
    coupling ratio (breadth-weighted -- discounts broad-commit/sweep inflation), falling back to
    the raw coupling_ratio (legacy), then to the co_sessions floor (oldest measures). The raw
    ratio is carried alongside in the reason for transparency. Returns (ok, why)."""
    m = m or {}
    focused, raw = m.get("focused_coupling_ratio"), m.get("coupling_ratio")
    signal = focused if focused is not None else raw
    if signal is None:
        co = m.get("co_sessions", 0)
        return (co >= MEANINGFUL_CO_OCCURRENCE_FLOOR,
                "co_sessions=%s vs floor %d (legacy: no coupling_ratio)"
                % (co, MEANINGFUL_CO_OCCURRENCE_FLOOR))
    label = "focused_coupling_ratio" if focused is not None else "coupling_ratio(raw-fallback)"
    alongside = "" if (raw is None or focused is None) else " (raw=%.3f, transparency)" % raw
    if signal >= FEDOBS_RATIO_FLOOR:
        return True, "%s=%.3f >= floor %.2f%s" % (label, signal, FEDOBS_RATIO_FLOOR, alongside)
    return False, ("%s=%.3f < floor %.2f -- weak/sweep-inflated, NOT a warrant%s"
                   % (label, signal, FEDOBS_RATIO_FLOOR, alongside))

# ---------------------------------------------------------------------------------------------
# The four promotion classes (PRD S4.1) -> target plane + ROUTED ratify owner + materializer lane.
# All four are cross-plane => CTO ratifies (PRD S8). The routing is DATA so a domain class added
# later routes to a domain owner without touching the gate.
# ---------------------------------------------------------------------------------------------
PROMOTION_CLASSES = {
    "COMPILER_RULE": {
        "target_plane": "NFRA_COMPILERKIT (RecognizerRegistry hot-registration seam)",
        "ratifier": "1.0.0_SA_CTO",
        "materializer": "comp_promote_materializer.materialize_live (GOV-B, exercised dispatch)",
    },
    "ALGEBRA_PRIMITIVE": {
        "target_plane": "NFRA_CSE (governed cse_schema version-bump migration)",
        "ratifier": "1.0.0_SA_CTO",
        "materializer": "governed schema migration (version-owner-signed; DS share of P2)",
    },
    "ROUTING_DIRECTIVE": {
        "target_plane": "comp_route (EXPLICIT heuristic -- never a latent affinity weight)",
        "ratifier": "1.0.0_SA_CTO",
        "materializer": "comp_route explicit-directive change (surface_prior class; DS share of P2)",
    },
    "KNOWLEDGE_NODE": {
        "target_plane": "globgrph graph (C3 system -> named governed capability node)",
        "ratifier": "1.0.0_SA_CTO",
        "materializer": "graph materializer (node_type SSOT is a CTO arch-gate; DS share of P2)",
    },
}

STATES = ("CANDIDATE", "MEASURED", "PARKED", "PROPOSED", "RATIFIED", "REJECTED",
          "MATERIALIZED", "MONITORED", "SUSTAINED", "DEGRADED", "DEMOTED", "DROPPED")

# The closed transition table (S4.3). Anything not listed is ILLEGAL and refuses loudly.
# DROPPED (absorbed, DS~B): a candidate with no MEANINGFUL measure even AFTER coverage is
# de-candidated -- not zombie-held at CANDIDATE forever. Distinct from PARKED (measured, below
# promote bar, re-measurable in place): DROPPED asserts the coverage was ATTEMPTED and the
# candidate is off the active queue; re-candidacy requires NEW EVIDENCE (ruling term (a)).
LEGAL = {
    "CANDIDATE": ("MEASURED", "DROPPED"),
    "MEASURED": ("PROPOSED", "PARKED", "DROPPED"),
    "PARKED": ("MEASURED", "DROPPED"),          # re-measure can un-park; exhausted coverage can drop
    "PROPOSED": ("RATIFIED", "REJECTED"),
    "RATIFIED": ("MATERIALIZED",),
    "REJECTED": (),                             # terminal; a measured negative, kept on the record
    "MATERIALIZED": ("MONITORED",),
    "MONITORED": ("SUSTAINED", "DEGRADED"),
    "SUSTAINED": ("MONITORED",),                # the standing re-measure cycle (P3)
    "DEGRADED": ("DEMOTED",),
    "DEMOTED": (),                              # terminal; reversal complete, evidence kept
    "DROPPED": ("CANDIDATE",),                  # re-candidacy on NEW evidence only -- never silent
}


class InvariantViolation(Exception):
    """A promotion-invariant gate refusing an advance. Fail-closed: the record does NOT move."""


# ---------------------------------------------------------------------------------------------
# The invariant checks. Each is PURE (record, to_state, evidence) -> list of violations (empty =
# clear). gate_check composes them; advance() RAISES on any violation BEFORE any mutation.
# ---------------------------------------------------------------------------------------------
def _real_measurement(m: dict | None, label: str) -> list:
    """Invariant 1's definition of a REAL measured effect: present, NOT pending, carries a numeric
    effect + basis + source + vintage (vintage may honestly be 'unknown' -- disclosed, not absent)."""
    v: list = []
    if not isinstance(m, dict) or not m:
        return [f"invariant-1 MEASURE-BEFORE-PROMOTE: {label} missing -- a correlation is a "
                "candidate, a measured effect is the warrant"]
    if m.get("pending"):
        v.append(f"invariant-1: {label} is PENDING -- a pending measure is NOT a measure "
                 "(do NOT fake a measurement; park the candidate instead)")
    eff = m.get("effect")
    if not isinstance(eff, (int, float)) or isinstance(eff, bool):
        v.append(f"invariant-1: {label}.effect must be a real number (got {eff!r})")
    for fld in ("basis", "source", "vintage"):
        if not str(m.get(fld, "") or "").strip():
            v.append(f"invariant-1: {label}.{fld} missing -- an unattributed number is not evidence")
    return v


def gate_check(record: dict, to_state: str, evidence: dict) -> list:
    """The 5-invariant gate, pure. Returns every violation (never just the first -- the proposer
    fixes the whole list, not one round-trip per defect)."""
    v: list = []
    cls = record.get("promotion_class")
    routed = (PROMOTION_CLASSES.get(cls) or {}).get("ratifier")
    if cls not in PROMOTION_CLASSES:
        v.append(f"promotion_class {cls!r} unknown (known: {sorted(PROMOTION_CLASSES)})")
    # invariant 5 floor on EVERY transition: a why + the record's decompression chain intact.
    if not str(evidence.get("why", "") or "").strip():
        v.append("invariant-5 INSPECTABLE: evidence.why missing -- an unexplained transition "
                 "cannot be promoted (LAW 2)")
    if not record.get("decompression_chain"):
        v.append("invariant-5: record.decompression_chain empty -- no lexical origin, no promotion")

    if to_state == "MEASURED":
        v += _real_measurement(evidence.get("measured_effect"), "measured_effect")
    elif to_state == "PARKED":
        if not str(evidence.get("park_reason", "") or "").strip():
            v.append("PARKED needs park_reason (a measured negative is a RESULT -- record it)")
    elif to_state == "PROPOSED":
        v += _real_measurement(record.get("measured_effect"), "record.measured_effect")
        # invariant-2 MEASUREMENT arm (absorbed per cb6a86177): meaningless-but-well-formed must
        # not REACH the ratifier -- the floor pre-filters; the owner's ratify stays the final gate.
        m_ok, m_why = measurement_meaningful(record.get("measured_effect") or {})
        if not m_ok:
            v.append("invariant-2 MEASUREMENT FLOOR: " + m_why +
                     " (a single coincidental co-occurrence is not a warrant -- CTO ratify-ruling)")
        ag = evidence.get("anti_goodhart") or {}
        if not str(ag.get("structural_rationale", "") or "").strip():
            v.append("invariant-2 ANTI-GOODHART: structural_rationale missing -- the warrant must "
                     "be structural/generalizing, not fixture-fit")
        if ag.get("not_tuned_to_own_metric") is not True:
            v.append("invariant-2: not_tuned_to_own_metric must be explicitly attested True")
        if not str(ag.get("generalizes_beyond_fixture", "") or "").strip():
            v.append("invariant-2: generalizes_beyond_fixture missing (name the out-of-fixture case)")
        if (record.get("recurrence") or 0) < 2:
            v.append("invariant-2: recurrence < 2 -- a single occurrence cannot be structural")
    elif to_state == "RATIFIED":
        r = evidence.get("ratify") or {}
        if not str(r.get("commission_id", "") or "").strip():
            v.append("invariant-3 HUMAN-RATIFY: ratify.commission_id missing -- the RATIFIER mints "
                     "it; this machine never self-mints")
        if r.get("ratifier") != routed:
            v.append(f"invariant-3: ratifier {r.get('ratifier')!r} != routed owner {routed!r} "
                     "for this promotion class (ratify-owner routing is part of the contract)")
        if not str(r.get("ref", "") or "").strip():
            v.append("invariant-3: ratify.ref missing (the ratifier's own record -- message id / "
                     "commit / verbatim -- the paper the ratification IS)")
    elif to_state == "REJECTED":
        rj = evidence.get("reject") or {}
        if not str(rj.get("reason", "") or "").strip() or not str(rj.get("ratifier", "") or "").strip():
            v.append("REJECTED needs reject.{ratifier,reason} -- a decline with reason is itself "
                     "an observation (PRD S4.3)")
    elif to_state == "MATERIALIZED":
        mr = evidence.get("materialize_receipt") or {}
        if mr.get("exercised") is not True:
            v.append("invariant-4 REVERSIBLE + Rule-22a: materialize_receipt.exercised must be True "
                     "-- a config-read materialization is INFERRED, not landed")
        if not str(mr.get("receipt_ref", "") or "").strip():
            v.append("invariant-4: materialize_receipt.receipt_ref missing (the materializer's own "
                     "trail entry / registry proof)")
        if not str(mr.get("demotion_path", "") or "").strip():
            v.append("invariant-4: demotion_path missing -- a promotion with no reversal path "
                     "does not materialize, ever")
    elif to_state == "MONITORED":
        if not str((evidence.get("monitor") or {}).get("monitor_ref", "") or "").strip():
            v.append("MONITORED needs monitor.monitor_ref (the P3 standing measure -- "
                     "promote_monitor wiring)")
    elif to_state in ("SUSTAINED", "DEGRADED"):
        v += _real_measurement(evidence.get("post_measure"), "post_measure")
        want = "sustained" if to_state == "SUSTAINED" else "degraded"
        if (evidence.get("post_measure") or {}).get("verdict") != want:
            v.append(f"{to_state} needs post_measure.verdict == {want!r} (the measurement decides, "
                     "not the caller)")
    elif to_state == "DEMOTED":
        dr = evidence.get("demotion_receipt") or {}
        if dr.get("exercised") is not True or not str(dr.get("ref", "") or "").strip():
            v.append("invariant-4: demotion_receipt.{exercised:true, ref} required -- reversal is "
                     "EXERCISED (deregister/rollback receipt), never asserted")
    elif to_state == "DROPPED":
        dp = evidence.get("drop") or {}
        if not str(dp.get("coverage_ref", "") or "").strip():
            v.append("DROPPED needs drop.coverage_ref -- de-candidation asserts the measure was "
                     "ATTEMPTED (coverage evidence); dropping unlooked-at is a silent absence")
        if not str(dp.get("reason", "") or "").strip():
            v.append("DROPPED needs drop.reason (no meaningful measure AFTER coverage -- state it)")
    elif to_state == "CANDIDATE":
        # only reachable from DROPPED (the closed table): re-candidacy needs NEW evidence.
        if not str((evidence.get("new_evidence") or {}).get("ref", "") or "").strip():
            v.append("re-candidacy from DROPPED needs new_evidence.ref -- a dropped candidate "
                     "returns on NEW evidence, never silently")
    return v


# ---------------------------------------------------------------------------------------------
# The typed advisory commission (clause-A GENERALIZED: comp_tool_health_gate.commission_for's
# shape, applied to any promotion class). ADVISORY -- names the action + consumer + ratifier;
# NEVER performs it. auto_mutates is structurally False.
# ---------------------------------------------------------------------------------------------
def build_commission(record: dict) -> dict:
    cls = record["promotion_class"]
    spec = PROMOTION_CLASSES[cls]
    return {
        "kind": "promotion-commission",
        "candidate_id": record["candidate_id"],
        "promotion_class": cls,
        "verdict": "PROPOSE",
        "value_anchor": {  # clause-A: the value citation, never a raw count
            "measured_effect": record.get("measured_effect"),
            "recurrence": record.get("recurrence"),
        },
        "grounding": {   # the ratifier reads EVIDENCE, not the label (TH-C CTO ask, generalized)
            "decompression_chain": record.get("decompression_chain"),
            "anti_goodhart": record.get("anti_goodhart"),
            "warrant": record.get("warrant"),
        },
        "proposed_to": {
            "kind": f"materialize-{cls.lower().replace('_', '-')}",
            "target_plane": spec["target_plane"],
            "materializer": spec["materializer"],
            "ratifier": spec["ratifier"],
            "title": f"PROMOTE {record['candidate_id']} -> {cls} into {spec['target_plane']}",
        },
        "auto_mutates": False,
    }


# ---------------------------------------------------------------------------------------------
# Persistence + CSE emission.
# ---------------------------------------------------------------------------------------------
def load_manifest(path: str = MANIFEST) -> dict:
    if not os.path.exists(path):
        return {"surface": "promote_lifecycle_manifest (P1 state snapshot; event trail = "
                           "promote_lifecycle_cse.jsonl)", "promotions": {}}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def save_manifest(manifest: dict, path: str = MANIFEST) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1, sort_keys=True)
        fh.write("\n")


def _record_marker(record: dict) -> str:
    """Deterministic content-marker over the record's transitions (the honest vintage anchor --
    same approach as comp_promote_materializer._load_marker)."""
    body = json.dumps(record.get("transitions", []), sort_keys=True).encode("utf-8")
    return hashlib.sha1(body).hexdigest()[:16]


def _emit_transition_cse(record: dict, frm: str, to: str, why: str, trail_path: str) -> dict:
    """Every transition is a FIRST-CLASS schema-validated ProducerKind.PROMOTE CSE (@0.4,
    fail-closed): open -> create, everything after -> reclassify (a state is a classification).
    cse_kind promotion_lifecycle -- distinct from the materializer's promotion_materialize
    (that one is the substrate receipt; this one is the lifecycle record)."""
    verb = Transformation.CREATE.value if frm == "" else Transformation.RECLASSIFY.value
    commission = (record.get("ratify") or {}).get("commission_id", "")
    prov = Provenance(
        source=os.path.relpath(MANIFEST, WS).replace(os.sep, "/"),
        locus=record["candidate_id"], recognizer="promote_lifecycle",
        evidence=f"{frm or 'OPEN'}->{to} commission={commission or '(pre-ratify)'} why={why[:160]}")
    cse = CSEvent(
        event_id=f"{ProducerKind.PROMOTE.value}:{record['candidate_id']}:{frm or 'OPEN'}->{to}",
        schema_version=SCHEMA_VERSION,
        producer={"kind": ProducerKind.PROMOTE.value, "ref": commission or record["candidate_id"]},
        compiler={"id": "promote-lifecycle", "artifact_class": "promotion_record",
                  "version": SCHEMA_VERSION},
        transformation={"verb": verb,
                        "subject": EntityRef(Entity.CONCEPT.value,
                                             f"promotion:{record['candidate_id']}"),
                        "edges": []},
        provenance=prov,
        execution_meta={"timestamp": "", "actor": "comp_promote_lifecycle",
                        "run_id": commission or record["candidate_id"]},
        head={"marker_head": _record_marker(record)},
        qualifiers={Qualifier.CONFIDENCE.value: _LIFECYCLE_TYPE_CONFIDENCE,
                    Qualifier.SCOPE.value: SCOPE})
    validate_or_raise(cse)   # fail-closed -- a malformed lifecycle CSE never reaches the trail
    row = {
        "cse_kind": "promotion_lifecycle", "event_id": cse.event_id,
        "schema_version": cse.schema_version, "producer_kind": cse.producer["kind"],
        "verb": verb, "from": frm, "to": to, "subject_ref": f"promotion:{record['candidate_id']}",
        "commission_id": commission, "why": why,
        "provenance": {"source": prov.source, "locus": prov.locus, "evidence": prov.evidence},
        "marker": _record_marker(record), "schema_validated": True,
    }
    with open(trail_path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(row) + "\n")
    return row


# ---------------------------------------------------------------------------------------------
# open_candidate + advance -- the only two mutators, and they mutate ONLY this plane's own files.
# ---------------------------------------------------------------------------------------------
def open_candidate(candidate: dict, manifest: dict, *, promotion_class: str,
                   trail_path: str = CSE_TRAIL, now_ts: float | None = None) -> dict:
    """Admit one MOTIF candidate record (motif_promote_candidates.json shape) as CANDIDATE."""
    cid = candidate.get("candidate_id")
    if not cid:
        raise InvariantViolation("candidate has no candidate_id")
    if cid in manifest["promotions"]:
        raise InvariantViolation(f"{cid} already open (state="
                                 f"{manifest['promotions'][cid]['state']}) -- one record per "
                                 "candidate; advance it, do not re-open")
    if promotion_class not in PROMOTION_CLASSES:
        raise InvariantViolation(f"promotion_class {promotion_class!r} unknown")
    chain = candidate.get("decompression_chain") or {}
    if not chain:
        raise InvariantViolation("invariant-5: candidate carries no decompression_chain -- "
                                 "no lexical origin, no admission (LAW 2)")
    record = {
        "candidate_id": cid, "promotion_class": promotion_class, "state": "CANDIDATE",
        "recurrence": candidate.get("recurrence"), "warrant": candidate.get("warrant") or
        {k: candidate.get(k) for k in ("motif_type", "tier", "stable", "fidelity_pass")},
        "decompression_chain": chain, "measured_effect": None, "anti_goodhart": None,
        "commission": None, "ratify": None,
        "opened_at": time.time() if now_ts is None else now_ts, "transitions": [],
    }
    _emit_transition_cse(record, "", "CANDIDATE", f"admitted from MOTIF ({candidate.get('kind')})",
                         trail_path)
    record["transitions"].append({"from": "", "to": "CANDIDATE",
                                  "at": record["opened_at"], "actor": "comp_promote_lifecycle",
                                  "why": "admitted from MOTIF candidates"})
    manifest["promotions"][cid] = record
    return record


def advance(record: dict, to_state: str, *, evidence: dict, manifest: dict, actor: str,
            trail_path: str = CSE_TRAIL, now_ts: float | None = None) -> dict:
    """THE gate. Checks legality + all five invariants; RAISES InvariantViolation (fail-closed --
    the record does not move, nothing is written) before ANY mutation."""
    frm = record["state"]
    if to_state not in STATES:
        raise InvariantViolation(f"unknown state {to_state!r}")
    if to_state not in LEGAL.get(frm, ()):
        raise InvariantViolation(f"ILLEGAL transition {frm} -> {to_state} (legal from {frm}: "
                                 f"{list(LEGAL.get(frm, ())) or 'none -- terminal'})")
    violations = gate_check(record, to_state, evidence)
    if violations:
        raise InvariantViolation(f"{frm} -> {to_state} REFUSED ({len(violations)} violation(s)): "
                                 + " | ".join(violations))
    # gate clear -- stamp the evidence into the record, THEN emit (emission validates fail-closed).
    if to_state == "MEASURED":
        record["measured_effect"] = evidence["measured_effect"]
    elif to_state == "PROPOSED":
        record["anti_goodhart"] = evidence["anti_goodhart"]
        record["commission"] = build_commission(record)
    elif to_state == "RATIFIED":
        record["ratify"] = evidence["ratify"]
    elif to_state == "REJECTED":
        record["reject"] = evidence["reject"]
    elif to_state == "MATERIALIZED":
        record["materialize_receipt"] = evidence["materialize_receipt"]
    elif to_state == "PARKED":
        record["park_reason"] = evidence["park_reason"]
    elif to_state in ("SUSTAINED", "DEGRADED"):
        record.setdefault("post_measures", []).append(evidence["post_measure"])
    elif to_state == "DEMOTED":
        record["demotion_receipt"] = evidence["demotion_receipt"]
    elif to_state == "DROPPED":
        record.setdefault("drops", []).append(evidence["drop"])
    elif to_state == "CANDIDATE":
        record.setdefault("recandidacies", []).append(evidence["new_evidence"])
    why = evidence.get("why", "")
    _emit_transition_cse(record, frm, to_state, why, trail_path)
    record["transitions"].append({"from": frm, "to": to_state,
                                  "at": time.time() if now_ts is None else now_ts,
                                  "actor": actor, "why": why})
    record["state"] = to_state
    manifest["promotions"][record["candidate_id"]] = record
    return record


# ---------------------------------------------------------------------------------------------
# Report -- every promotion, its state, and the NEXT gate it is waiting on.
# ---------------------------------------------------------------------------------------------
def run_report() -> int:
    manifest = load_manifest()
    promos = manifest.get("promotions", {})
    print("=" * 84)
    print("comp_promote_lifecycle -- NFRA_PROMOTE P1 (contract + state machine + 5-invariant gate)")
    print("=" * 84)
    if not promos:
        print("no open promotions. Admit one: open_candidate(<motif record>, manifest, "
              "promotion_class=...)")
        print("MOTIF candidates available: %s" % os.path.relpath(CANDIDATES, WS))
        return 0
    for cid, r in sorted(promos.items()):
        nxt = LEGAL.get(r["state"], ())
        print("  %-38s %-12s class=%-18s next: %s" % (
            cid, r["state"], r["promotion_class"],
            (" | ".join(nxt) if nxt else "(terminal)")))
        if r.get("commission") and r["state"] == "PROPOSED":
            print("       AWAITING RATIFY by %s -- commission title: %s" % (
                r["commission"]["proposed_to"]["ratifier"],
                r["commission"]["proposed_to"]["title"]))
    print("(%d promotion(s); trail: %s)" % (len(promos), os.path.relpath(CSE_TRAIL, WS)))
    return 0


# ---------------------------------------------------------------------------------------------
# SELF-TEST -- the exercised red-fixture: every invariant FIRES (negative) and CLEARS (positive),
# fail-closed proven (a refused advance mutates nothing), zero-auto-mutation proven (DS~B's
# manifest byte-identical across the whole run), CSE trail validated per transition.
# ---------------------------------------------------------------------------------------------
def self_test() -> int:
    print("=== comp_promote_lifecycle self-test (P1: 5 invariants, each EXERCISED both ways) ===")
    ok: list = []

    def chk(name, cond):
        ok.append(bool(cond))
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))

    def refused(fn, *a, **k):
        try:
            fn(*a, **k)
            return None
        except InvariantViolation as e:
            return str(e)

    tmp_trail = os.path.join(_HERE, "_selftest_lifecycle_trail.jsonl")
    ds_manifest_path = os.path.join(WS, "org", "tier2_senior", "0.4.0_DS_ClientPlatform",
                                    "deliverables", "promote_recognizer_manifest.json")
    ds_before = open(ds_manifest_path, "rb").read() if os.path.exists(ds_manifest_path) else b""
    try:
        # a REAL candidate record (not synthetic): the first MOTIF candidate on the record.
        cand = json.load(open(CANDIDATES, encoding="utf-8"))["candidates"][0]
        man = {"surface": "selftest", "promotions": {}}

        rec = open_candidate(cand, man, promotion_class="COMPILER_RULE", trail_path=tmp_trail)
        chk("open: a REAL MOTIF candidate admits as CANDIDATE (chain carried)",
            rec["state"] == "CANDIDATE" and bool(rec["decompression_chain"]))
        chk("open: re-open REFUSED (one record per candidate)",
            refused(open_candidate, cand, man, promotion_class="COMPILER_RULE",
                    trail_path=tmp_trail) is not None)

        # ---- invariant 1: measure-before-promote ----
        r1 = refused(advance, rec, "MEASURED", evidence={
            "why": "t", "measured_effect": {"pending": True, "effect": None, "basis": "",
                                            "source": "", "vintage": ""}},
            manifest=man, actor="t", trail_path=tmp_trail)
        chk("inv1 NEGATIVE: a PENDING measurement REFUSES (do not fake a measurement)",
            r1 is not None and "invariant-1" in r1)
        chk("inv1 fail-closed: the refused record did NOT move (state still CANDIDATE)",
            rec["state"] == "CANDIDATE" and rec["measured_effect"] is None)
        measured = {"pending": False, "effect": 45.0, "co_sessions": 45,
                    "basis": "co_sessions over the FEDOBS coevolution signal",
                    "source": "fedobs_observations.json signals.coevolution",
                    "vintage": "computed_at 07-08 (marker_head unknown -- pre-pin artifact, "
                               "disclosed)"}
        advance(rec, "MEASURED", evidence={"why": "FEDOBS-measured co-occurrence",
                                           "measured_effect": measured},
                manifest=man, actor="t", trail_path=tmp_trail)
        chk("inv1 POSITIVE: a real measured effect advances CANDIDATE -> MEASURED",
            rec["state"] == "MEASURED")

        # ---- invariant 2: anti-Goodhart ----
        r2 = refused(advance, rec, "PROPOSED", evidence={"why": "t", "anti_goodhart": {}},
                     manifest=man, actor="t", trail_path=tmp_trail)
        chk("inv2 NEGATIVE: PROPOSED without a structural attestation REFUSES",
            r2 is not None and "invariant-2" in r2)
        ag = {"structural_rationale": "the motif recurs across 3 unrelated pages (structural, "
                                      "not fixture-local)",
              "not_tuned_to_own_metric": True,
              "generalizes_beyond_fixture": "detector fires on pages outside the discovery set"}
        advance(rec, "PROPOSED", evidence={"why": "warrant + attestation complete",
                                           "anti_goodhart": ag},
                manifest=man, actor="t", trail_path=tmp_trail)
        chk("inv2 POSITIVE: MEASURED -> PROPOSED; typed commission BUILT",
            rec["state"] == "PROPOSED" and rec["commission"] is not None)
        chk("clause-A shape: commission routes to the CLASS ratifier + auto_mutates False",
            rec["commission"]["proposed_to"]["ratifier"] == "1.0.0_SA_CTO"
            and rec["commission"]["auto_mutates"] is False)

        # ---- invariant 3: human-ratify ----
        r3 = refused(advance, rec, "RATIFIED", evidence={
            "why": "t", "ratify": {"ratifier": "0.8.0_AE_CloudComp~Z",
                                   "commission_id": "SELF-MINTED", "ref": "x"}},
            manifest=man, actor="t", trail_path=tmp_trail)
        chk("inv3 NEGATIVE: a NON-ROUTED ratifier (the builder itself) REFUSES",
            r3 is not None and "invariant-3" in r3)
        r3b = refused(advance, rec, "RATIFIED", evidence={
            "why": "t", "ratify": {"ratifier": "1.0.0_SA_CTO", "commission_id": "", "ref": "x"}},
            manifest=man, actor="t", trail_path=tmp_trail)
        chk("inv3 NEGATIVE: an empty commission_id REFUSES (the ratifier mints it)",
            r3b is not None and "commission_id" in r3b)
        advance(rec, "RATIFIED", evidence={
            "why": "fixture ratify (test-scoped)",
            "ratify": {"ratifier": "1.0.0_SA_CTO", "commission_id": "CTO-PROMOTE-TEST-FIXTURE",
                       "ref": "selftest-fixture (not a real ratification)"}},
            manifest=man, actor="t", trail_path=tmp_trail)
        chk("inv3 POSITIVE: the routed ratifier's record advances PROPOSED -> RATIFIED",
            rec["state"] == "RATIFIED")

        # ---- invariant 4: reversible ----
        r4 = refused(advance, rec, "MATERIALIZED", evidence={
            "why": "t", "materialize_receipt": {"exercised": True, "receipt_ref": "r",
                                                "demotion_path": ""}},
            manifest=man, actor="t", trail_path=tmp_trail)
        chk("inv4 NEGATIVE: MATERIALIZED without a demotion_path REFUSES",
            r4 is not None and "demotion_path" in r4)
        r4b = refused(advance, rec, "MATERIALIZED", evidence={
            "why": "t", "materialize_receipt": {"exercised": False, "receipt_ref": "r",
                                                "demotion_path": "demote_live"}},
            manifest=man, actor="t", trail_path=tmp_trail)
        chk("inv4 NEGATIVE: a NON-EXERCISED (config-read) receipt REFUSES (Rule 22a)",
            r4b is not None and "exercised" in r4b)
        advance(rec, "MATERIALIZED", evidence={
            "why": "materializer receipt (fixture)",
            "materialize_receipt": {"exercised": True,
                                    "receipt_ref": "promote_materialize_cse.jsonl#fixture",
                                    "demotion_path": "comp_promote_materializer.demote_live"}},
            manifest=man, actor="t", trail_path=tmp_trail)
        chk("inv4 POSITIVE: exercised receipt + demotion path -> MATERIALIZED",
            rec["state"] == "MATERIALIZED")

        # ---- the monitored tail + demotion (P3's states, gate-checked here) ----
        advance(rec, "MONITORED", evidence={"why": "standing monitor",
                                            "monitor": {"monitor_ref": "promote_monitor.py"}},
                manifest=man, actor="t", trail_path=tmp_trail)
        pm = {"pending": False, "effect": -0.3, "basis": "post-promotion coevolution delta",
              "source": "fedobs", "vintage": "t", "verdict": "degraded"}
        advance(rec, "DEGRADED", evidence={"why": "post-measure shows degradation",
                                           "post_measure": pm},
                manifest=man, actor="t", trail_path=tmp_trail)
        advance(rec, "DEMOTED", evidence={
            "why": "reversal exercised",
            "demotion_receipt": {"exercised": True, "ref": "demote_live deregister receipt"}},
            manifest=man, actor="t", trail_path=tmp_trail)
        chk("tail: MONITORED -> DEGRADED -> DEMOTED (the reversibility loop closes)",
            rec["state"] == "DEMOTED")
        chk("terminal: advancing a DEMOTED record REFUSES (closed table)",
            refused(advance, rec, "MONITORED", evidence={"why": "t"},
                    manifest=man, actor="t", trail_path=tmp_trail) is not None)

        # ---- illegal jump + the REJECTED and PARKED paths on fresh records ----
        cand2 = dict(cand, candidate_id="motif:selftest-2")
        rec2 = open_candidate(cand2, man, promotion_class="ROUTING_DIRECTIVE",
                              trail_path=tmp_trail)
        chk("illegal: CANDIDATE -> MATERIALIZED direct jump REFUSES",
            refused(advance, rec2, "MATERIALIZED", evidence={
                "why": "t", "materialize_receipt": {"exercised": True, "receipt_ref": "r",
                                                    "demotion_path": "d"}},
                manifest=man, actor="t", trail_path=tmp_trail) is not None)
        advance(rec2, "MEASURED", evidence={"why": "t", "measured_effect": dict(
            measured, effect=0.4)}, manifest=man, actor="t", trail_path=tmp_trail)
        advance(rec2, "PARKED", evidence={"why": "below threshold",
                                          "park_reason": "effect 0.4 below the promote bar"},
                manifest=man, actor="t", trail_path=tmp_trail)
        chk("PARKED: a below-threshold measure parks (a measured negative is a RESULT)",
            rec2["state"] == "PARKED")

        # ---- ABSORBED DS~B DELTAS (cb6a86177) -- each exercised both ways, matching the CVO
        # delta re-cert checks: planted-below-floor refused / DROPPED both ways / floor identity.
        cand3 = dict(cand, candidate_id="motif:selftest-3")
        rec3 = open_candidate(cand3, man, promotion_class="COMPILER_RULE", trail_path=tmp_trail)
        weak = {"pending": False, "effect": 0.05, "basis": "focused coupling", "source": "fedobs",
                "vintage": "t", "focused_coupling_ratio": 0.05, "coupling_ratio": 0.30}
        advance(rec3, "MEASURED", evidence={"why": "weak-but-well-formed measure",
                                            "measured_effect": weak},
                manifest=man, actor="t", trail_path=tmp_trail)
        rF = refused(advance, rec3, "PROPOSED", evidence={"why": "t", "anti_goodhart": ag},
                     manifest=man, actor="t", trail_path=tmp_trail)
        chk("absorb(b) NEGATIVE: a PLANTED below-floor well-formed measurement never reaches the "
            "ratifier (focused 0.05 < 0.12 rules; raw 0.30 alongside for transparency)",
            rF is not None and "MEASUREMENT FLOOR" in rF and "raw=0.300" in rF)
        ok2, why2 = measurement_meaningful({"focused_coupling_ratio": 0.18,
                                            "coupling_ratio": 0.05})
        chk("absorb(b) POSITIVE: focused 0.18 >= 0.12 is meaningful (focused wins over weak raw)",
            ok2 and "raw=0.050" in why2)
        r_dropA = refused(advance, rec3, "DROPPED", evidence={
            "why": "t", "drop": {"coverage_ref": "", "reason": "x"}},
            manifest=man, actor="t", trail_path=tmp_trail)
        chk("absorb(a) NEGATIVE: DROPPED without coverage evidence REFUSES (never drop-unlooked-at)",
            r_dropA is not None and "coverage_ref" in r_dropA)
        advance(rec3, "DROPPED", evidence={
            "why": "no meaningful measure after coverage",
            "drop": {"coverage_ref": "fedobs coevolution sweep (full candidate coverage)",
                     "reason": "focused 0.05 < floor 0.12 after coverage -- de-candidated"}},
            manifest=man, actor="t", trail_path=tmp_trail)
        chk("absorb(a) POSITIVE: MEASURED -> DROPPED with coverage evidence (not zombie-held)",
            rec3["state"] == "DROPPED" and rec3.get("drops"))
        r_rc = refused(advance, rec3, "CANDIDATE", evidence={"why": "t"},
                       manifest=man, actor="t", trail_path=tmp_trail)
        chk("absorb(a) NEGATIVE: re-candidacy without NEW evidence REFUSES",
            r_rc is not None and "new_evidence" in r_rc)
        advance(rec3, "CANDIDATE", evidence={
            "why": "new coupling surfaced at a later vintage",
            "new_evidence": {"ref": "fedobs_observations.json coevolution row @ new marker"}},
            manifest=man, actor="t", trail_path=tmp_trail)
        chk("absorb(a) POSITIVE: DROPPED -> CANDIDATE on new_evidence (re-candidacy recorded)",
            rec3["state"] == "CANDIDATE" and rec3.get("recandidacies"))
        chk("absorb(c): FEDOBS_RATIO_FLOOR homed in THIS module (0.12 default / env-overridable) "
            "-- the one import target for the lifecycle AND promote_monitor",
            isinstance(FEDOBS_RATIO_FLOOR, float)
            and (os.environ.get("FEDOBS_RATIO_FLOOR") is not None or FEDOBS_RATIO_FLOOR == 0.12))

        # ---- CSE trail: one validated row per transition, all schema_validated ----
        rows = [json.loads(ln) for ln in open(tmp_trail, encoding="utf-8")]
        n_transitions = (len(rec["transitions"]) + len(rec2["transitions"])
                         + len(rec3["transitions"]))
        chk("inv5: trail rows == transitions (%d) and ALL schema_validated @0.4"
            % n_transitions,
            len(rows) == n_transitions and all(
                r["schema_validated"] is True and r["schema_version"] == SCHEMA_VERSION
                for r in rows))

        # ---- the control can fail: a provenance-less CSE RAISES inside the emitter ----
        blank = dict(rec, candidate_id="")   # empty locus/subject tail -> validator must reject
        control_fired = False
        try:
            _emit_transition_cse(blank, "A", "B", "", tmp_trail)
        except Exception:  # noqa: BLE001 -- CSEValidationError or ValueError both prove the gate
            control_fired = True
        chk("control-can-fail: a malformed lifecycle CSE RAISES (validate_or_raise is load-bearing)",
            control_fired)

        # ---- ZERO AUTO-MUTATION: DS~B's manifest is byte-identical across the whole run ----
        ds_after = open(ds_manifest_path, "rb").read() if os.path.exists(ds_manifest_path) else b""
        chk("zero-auto-mutation: promote_recognizer_manifest.json BYTE-IDENTICAL (this plane "
            "never writes the substrate)", ds_before == ds_after)
        src = open(os.path.abspath(__file__), encoding="utf-8").read()
        needle = "import " + "comp_promote_materializer"   # split so the probe never matches itself
        chk("grep-proof: this module never imports the materializer (handoff by commission, "
            "not by call)", needle not in src)
    finally:
        if os.path.exists(tmp_trail):
            os.remove(tmp_trail)

    n = sum(1 for x in ok if x)
    print("--- self-test: %d/%d passed (5 invariants exercised both ways; fail-closed proven) ---"
          % (n, len(ok)))
    return 0 if n == len(ok) else 1


def main() -> int:
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(errors="replace")
        except Exception:  # noqa: BLE001
            pass
    if "--self-test" in sys.argv[1:]:
        return self_test()
    return run_report()


if __name__ == "__main__":
    sys.exit(main())
