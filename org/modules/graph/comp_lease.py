#!/usr/bin/env python3
"""comp_lease -- NFRA_EPISTEMY COMPONENT 4: the FOUR-STATE LEASE SERVICE + Eligibility_Evaluation.

"Invalidation against real support identities, not names" (PRD sec.1 row 4). A lease is not a lock.
"FAILURE TO REEVALUATE NEVER PRESERVES VALIDITY" is the component's whole point, and it is enforced
STRUCTURALLY: the lease state is a READ-TIME COMPUTATION over re-read support identities, never a
stored field a stale writer can leave behind.

SOURCES OF RECORD (cited, never copied): PRD sec.2.5 (Eligibility_Evaluation -- separate, dated,
attested object over an IMMUTABLE assessment; the invalidation pipeline coarse-intersection ->
exclusion replay -> residual -> policy; one-evaluation-per-(assessment, scope); "a new member is
never covered by an old enumerated waiver") + sec.1 row 4 + sec.3 law 7 (a regen is not a review);
Knowledge_Basis 0.1.1 @151eaf7e4c (CONSUMED -- five fixed slots, null = UNRATIFIED_BASIS, any null
member CAPS the axes it governs at UNKNOWN); C3 Support_Closures (the support-identity substrate --
a lease binds the closure's VINTAGE COORDINATES as identities, never names); CTO Note 2 via COO
64063 (the record carries BOTH effect_as_recorded AND effect_as_evaluated; the UNCOMPUTED ->
EXPANDING collapse is one-way and auditable only with the pair).

THE DIGEST DERIVATION HAS ONE NORMATIVE HOME AND IT IS CONSUMED, NEVER RE-IMPLEMENTED:
precondition_token.py _request_hash (0.7.0 C10-PRECOND). ANY OTHER SERIALIZATION IS NON-CONFORMANT
EVEN IF THE DIGEST PATTERN MATCHES (the clause that converts a silent serializer divergence into a
rule violation).

THE FOUR-STATE AXIS (Rule-24 record routed to base 64100) is a TWO-LEVEL PARTITION TREE -- MECE
without ordering language (the C3 lesson applied in advance; a precedence rule is the tell of fused
axes):
  LEVEL 1  does the minting evaluation still BIND?
           (no support identity moved since it ran AND its validity window is open)
     NO -> EXPIRED   (the last result is OUT OF SCOPE, not out-ranked)
     YES -> LEVEL 2  the evaluation's result:
           supported -> VALID | unsupported -> INVALID | undeterminable -> UNKNOWN
NEVER_EVALUATED is unreachable BY CONSTRUCTION: a Lease exists only as the product of an evaluation
(the constructor requires it). A retrieval failure during the state read is UNKNOWN, never VALID.

Objects are PROPOSED shape (base cert pending, msg 64100); instances carry object_status. Bounds:
read-only live AWS; nothing armed; registry acts through 4.0.0_SA_CRO base; sec.2.9 untouched.
Author: 0.8.0_AE_CloudComp (NFRA_EPISTEMY.C4-LEASE, COO GO 64063).
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
_PRECOND_DIR = os.path.join(WS, "org", "tier2_senior", "0.7.0_AE_CloudOps", "deliverables",
                            "NFRA_EPISTEMY.C10-PRECOND")
KB_DIR = os.path.join(WS, "org", "tier1_exec", "4.0.0_SA_CRO", "deliverables", "NFRA_EPISTEMY")
OUT_DIR = os.path.join(WS, "org", "tier2_senior", "0.8.0_AE_CloudComp", "deliverables",
                       "NFRA_EPISTEMY.C4-LEASE", "leases")
INSTRUMENT = {"id": "comp-lease", "version": "0.1.0"}
OBJECT_STATUS = "PROPOSED shape per the C4 route (0.8.0 sketch 64100; base cert + CTO gate pending)"
STATES = ("VALID", "INVALID", "UNKNOWN", "EXPIRED")            # partition-tree leaves, no ordering
RESULTS = ("ELIGIBLE", "INELIGIBLE", "UNKNOWN")
SUPPORT_MEMBER_IDS = ("source_map_updated", "artifact_sha256", "live_code_sha256",
                      "last_deployed_commit", "repo_head")


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


# ---------------------------------------------------------------------------------------------
# CONSUMED homes: the normative digest (C10) + the envelope (C1) + the closure side-readers (C3).
# ---------------------------------------------------------------------------------------------
def _normative_hash():
    if _PRECOND_DIR not in sys.path:
        sys.path.insert(0, _PRECOND_DIR)
    import precondition_token  # noqa: PLC0415
    return precondition_token._request_hash  # noqa: SLF001 -- the TO names this exact home normative


def _comp_closure():
    if _HERE not in sys.path:
        sys.path.insert(0, _HERE)
    import comp_closure  # noqa: PLC0415
    return comp_closure


def _obs(env, *, request, status, plane, substrate, population, count, grain, process, value,
         reason, pointers, invalidation=None):
    return env.build_record(
        instrument_id=INSTRUMENT["id"], instrument_version=INSTRUMENT["version"], request=request,
        status=status, plane=plane, substrate=substrate, population_predicate=population,
        denominator_count=count, denominator_grain=grain, denominator_process=process,
        substantive_value=value, unknown_reason=reason, observed_at=_now(),
        support_pointers=list(pointers), traversal_residue=[], control_references=[],
        discrimination_certificate_ref=None, invalidation_predicates=list(invalidation or []))


# ---------------------------------------------------------------------------------------------
# Knowledge_Basis: consume base's minted instance when it exists; a LOCAL FIXTURE otherwise --
# clearly labelled, never presented as a mint. Five nulls is the honest first state (UNRATIFIED_BASIS)
# and every null member CAPS the axes it governs at UNKNOWN.
# ---------------------------------------------------------------------------------------------
NULL_MEMBERS = {"hypothesis_space": None, "normal_form": None, "compatibility_policy": None,
                "scope_ontology": None, "outcome_vocabulary": None}


def load_basis() -> dict:
    """Consume base's minted instance, found by CONTENT (basis_id + members + digest), never by
    filename -- the mint landed as KB_FIRST_BASIS_INSTANCE.json (@053b83f414), and a filename-glob
    reader would have silently fallen back to the fixture: the filename-resolved class again.
    The mint's digest MUST reproduce through the normative home over its members -- consuming a
    non-reproducing mint silently would be the exact serializer-divergence defect 0.1.1 closed."""
    rh = _normative_hash()
    for name in sorted(os.listdir(KB_DIR)):
        if not name.endswith(".json"):
            continue
        try:
            b = json.load(open(os.path.join(KB_DIR, name), encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        if isinstance(b, dict) and isinstance(b.get("basis_id"), str) and b["basis_id"].startswith("kb-") \
                and "members" in b and "digest" in b and not b.get("fixture"):
            reproduced = rh(b["members"])
            if reproduced != b["digest"]:
                raise Refused("REFUSED: minted basis %s digest does NOT reproduce through the normative home "
                              "(recorded %s, reproduced %s) -- a conforming-looking digest from a non-conforming "
                              "serializer is indistinguishable from a real basis change; not consuming it"
                              % (name, b["digest"][:24], reproduced[:24]))
            b["_source"] = "MINTED (base): %s @053b83f414; digest reproduced via the normative home" % name
            return b
    members = dict(NULL_MEMBERS)
    return {"basis_id": "kb-fixture-000000", "members": members, "digest": rh(members),
            "minted_at": None, "minted_by": None, "predecessor_basis_id": None,
            "change": None, "fixture": True,
            "_source": "LOCAL FIXTURE -- five nulls (UNRATIFIED_BASIS); base's mint pending (ask in 64100); "
                       "digest via the normative home over members; NEVER a mint"}


def null_capped_axes(basis: dict) -> list:
    """The axes governed by null members: each caps its axes at UNKNOWN (schema 0.1.1 absence law)."""
    return sorted(k for k, v in (basis.get("members") or {}).items() if v is None)


# ---------------------------------------------------------------------------------------------
# Support-side readers: live (reuses C3's LiveReader + RepoIndex -- one instrument, rung 2) or a
# fixture dict for the offline battery. Reads return (value|None, ok) -- a retrieval failure is
# NEVER a value (it lands the state read at UNKNOWN, not at VALID).
# ---------------------------------------------------------------------------------------------
class LiveSides:
    def __init__(self):
        cc = _comp_closure()
        self._cc = cc
        self._smap = json.load(open(cc.SOURCE_MAP, encoding="utf-8"))
        self._reader = cc.LiveReader()
        self._repo = cc.RepoIndex()

    def read(self, subject_ref: str) -> dict:
        entry = self._smap.get("functions", {}).get(subject_ref) or {}
        fn, _st = self._reader.get_function(subject_ref)
        cfg = ((fn or {}).get("Configuration") or {})
        return {"source_map_updated": self._smap.get("_updated"),
                "artifact_sha256": entry.get("artifact_sha256"),
                "live_code_sha256": cfg.get("CodeSha256") if fn else None,
                "last_deployed_commit": entry.get("last_deployed_commit"),
                "repo_head": self._repo.head(),
                "_retrieval_ok": {"live_code_sha256": fn is not None}}


class FixtureSides:
    def __init__(self, values: dict, fail_keys=()):
        self.values, self.fail = dict(values), set(fail_keys)

    def read(self, subject_ref: str) -> dict:  # noqa: ARG002
        out = {k: (None if k in self.fail else self.values.get(k)) for k in SUPPORT_MEMBER_IDS}
        out["_retrieval_ok"] = {k: (k not in self.fail) for k in SUPPORT_MEMBER_IDS}
        return out


# ---------------------------------------------------------------------------------------------
# The Eligibility_Evaluation (PRD sec.2.5) -- the pipeline in the spec's order, refusals typed.
# ---------------------------------------------------------------------------------------------
class Refused(ValueError):
    """A typed refusal: the pipeline declines to produce a record, loudly."""


_SEEN_EVALUATIONS: set = set()      # (assessment_digest, scope, basis_digest, support_digest)


def _support_digest(rh, identities: dict) -> str:
    return rh({k: identities.get(k) for k in SUPPORT_MEMBER_IDS})


def evaluate(closure_path: str, sides, env, basis: dict | None = None, *,
             declared_coordinates=None, exclusion_proofs=None, waivers=None,
             basis_change=None, scope=None) -> tuple:
    """Run ONE Eligibility_Evaluation over an IMMUTABLE assessment (a committed C3 closure) and,
    when the result licenses it, mint the Lease. Returns (evaluation, lease|None, observations)."""
    rh = _normative_hash()
    basis = basis or load_basis()
    raw = open(closure_path, "rb").read()
    closure = json.loads(raw.decode("utf-8"))
    assessment_digest = "sha256:" + hashlib.sha256(raw).hexdigest()   # immutability by digest
    subject = closure["subject"]["ref"]
    scope = scope or "%s:%s" % (closure["subject"].get("kind", "SUPPORT_CLOSURE"), subject)
    vintage = {k: closure.get("vintage", {}).get(k) for k in SUPPORT_MEMBER_IDS}

    # ---- STAGE 1: COARSE COORDINATE INTERSECTION -- OVER-include by construction (m2) ----------
    full_coordinates = list(SUPPORT_MEMBER_IDS) + ["knowledge_basis"]
    declared = list(declared_coordinates) if declared_coordinates is not None else list(full_coordinates)
    missing = [c for c in full_coordinates if c not in declared]
    if missing:
        raise Refused("REFUSED (m2): declared coarse intersection UNDER-includes -- missing coordinate(s) %s; "
                      "the pipeline over-includes by construction and recomputes the full set" % missing)
    current = sides.read(subject)
    ok_map = current.get("_retrieval_ok", {})
    obs = [_obs(env, request={"op": "support_side_read", "subject": subject, "coords": list(SUPPORT_MEMBER_IDS)},
                status={"acquisition": "PRESENT" if all(ok_map.values()) else "FAILED",
                        "transport": "SUCCEEDED", "enumeration": "SUCCEEDED", "parse": "SUCCEEDED"},
                plane="APPLIED", substrate="aws",
                population="the five support-member identities of one closure", count=len(SUPPORT_MEMBER_IDS),
                grain="support member", process="source-map + get-function + git HEAD re-read (C3 side-readers)",
                value={k: current.get(k) for k in SUPPORT_MEMBER_IDS} if all(ok_map.values()) else None,
                reason="one or more side reads failed to retrieve",
                pointers=[closure_path], invalidation=["any side moves"])]
    changed = [k for k in SUPPORT_MEMBER_IDS
               if ok_map.get(k, True) and vintage.get(k) is not None and current.get(k) != vintage.get(k)]
    unreadable = [k for k in SUPPORT_MEMBER_IDS if not ok_map.get(k, True)]
    intersecting = sorted(set(changed) | set(unreadable))   # OVER-include: unreadable counts as intersecting

    # ---- STAGE 2: EXCLUSION-PROOF REPLAY -- typed only; untyped silence REFUSED (m5) ------------
    replayed = []
    for p in (exclusion_proofs or []):
        if not isinstance(p, dict) or p.get("kind") not in ("ATTESTED_ABSENCE", "RULED_OUT_BY_EVIDENCE") or not p.get("ref"):
            raise Refused("REFUSED (m5): untyped silence is never an exclusion proof -- a proof carries "
                          "{kind: ATTESTED_ABSENCE | RULED_OUT_BY_EVIDENCE, ref}; got %r" % (p,))
        covered = p.get("excludes")
        if covered in intersecting:
            replayed.append(p)
            intersecting = [c for c in intersecting if c != covered]

    # ---- WAIVER LAW (m3): a NEW member is never covered by an old ENUMERATED waiver -------------
    waived = []
    for c in list(intersecting):
        for w in (waivers or []):
            if w.get("kind") == "ENUMERATED":
                if c in (w.get("members") or []):
                    if w.get("minted_before_member", False):
                        raise Refused("REFUSED (m3): member %r claims coverage by an ENUMERATED waiver older than "
                                      "itself -- a new member is never covered by an old enumerated waiver" % c)
                    waived.append((c, "ENUMERATED"))
                    intersecting.remove(c)
                    break
            elif w.get("kind") == "RATIFIED_PREDICATE":
                pred = w.get("scope_predicate") or (lambda _x: False)
                if pred(c):
                    waived.append((c, "RATIFIED_PREDICATE:%s" % w.get("ref")))
                    intersecting.remove(c)
                    break

    # ---- STAGE 3: RESIDUAL RECOMPUTATION --------------------------------------------------------
    capped = null_capped_axes(basis)
    residual_before = sorted(set(changed) | set(unreadable))
    residual_after = sorted(intersecting)

    # ---- STAGE 4: POLICY APPLICATION ------------------------------------------------------------
    if any(c in residual_after for c in unreadable):
        result, why = "UNKNOWN", "a support identity could not be read -- a retrieval failure is never support"
    elif residual_after:
        result, why = "INELIGIBLE", "support identity(ies) %s moved since the assessment's vintage and no typed proof or ratified predicate covers them" % residual_after
    elif capped:
        result, why = ("ELIGIBLE",
                       "no support identity moved; basis members %s are null (UNRATIFIED_BASIS) and CAP their governed axes at UNKNOWN -- eligibility here binds ONLY the support-identity axes" % capped)
    else:
        result, why = "ELIGIBLE", "no support identity moved; all basis members ratified"

    # ---- CTO Note 2: the effect PAIR, one-way collapse, auditable only together -----------------
    eff_recorded = (basis_change or {}).get("effect") if basis_change is not None else None
    eff_evaluated = eff_recorded if eff_recorded is not None else ("EXPANDING" if basis_change is not None else None)

    # ---- one-evaluation-per (m4): the SAME question is never adjudicated twice ------------------
    support_dig = _support_digest(rh, current)
    key = (assessment_digest, scope, basis["digest"], support_dig)
    if key in _SEEN_EVALUATIONS:
        raise Refused("REFUSED (m4): an evaluation for this (assessment, scope) at this basis digest and support "
                      "state already exists -- cite it; a changed basis or support state is a NEW evaluation")
    _SEEN_EVALUATIONS.add(key)

    evaluation = {"object": "Eligibility_Evaluation", "object_status": OBJECT_STATUS,
                  "evaluation_id": "ee-%s" % rh({"a": assessment_digest, "s": scope, "b": basis["digest"], "v": support_dig})[7:19],
                  "assessment_ref": {"path": os.path.relpath(closure_path, WS).replace("\\", "/"),
                                     "digest": assessment_digest,
                                     "note": "IMMUTABLE -- metadata about a record is not the record"},
                  "scope": scope,
                  "prior_basis": None,      # S6: null = first evaluation, no predecessor -- declared
                  "current_basis": {"basis_id": basis["basis_id"], "digest": basis["digest"],
                                    "source": basis.get("_source", "")},
                  "pipeline_order": ["coarse_coordinate_intersection", "exclusion_proof_replay",
                                     "residual_recomputation", "policy_application"],
                  "coordinates_declared": declared, "coordinates_full": full_coordinates,
                  "intersecting_changes": sorted(set(changed) | set(unreadable)),
                  "exclusion_proofs": replayed, "waivers_applied": waived,
                  "residual_before": residual_before, "residual_after": residual_after,
                  "basis_null_capped_axes": capped,
                  "policy_predicate": "residual-empty AND sides-readable -> ELIGIBLE; moved-uncovered -> INELIGIBLE; unreadable -> UNKNOWN",
                  "effect_as_recorded": eff_recorded if basis_change is not None else "NO_BASIS_CHANGE_IN_SCOPE",
                  "effect_as_evaluated": eff_evaluated if basis_change is not None else "NO_BASIS_CHANGE_IN_SCOPE",
                  "result": result, "result_basis": why,
                  "evaluated_at": _now(), "evaluator": "0.8.0_AE_CloudComp/comp-lease",
                  "observation_record_refs": [o["request_hash"] for o in obs]}
    validate_effect_pair(evaluation)

    lease = None
    if result in ("ELIGIBLE", "UNKNOWN"):
        lease = {"object": "Lease", "object_status": OBJECT_STATUS,
                 "lease_id": "lease-%s" % evaluation["evaluation_id"][3:],
                 "subject": {"kind": closure["subject"].get("kind"), "ref": subject,
                             "closure_path": evaluation["assessment_ref"]["path"],
                             "closure_digest": assessment_digest},
                 "support_members": [{"member_id": k, "identity": current.get(k)} for k in SUPPORT_MEMBER_IDS],
                 "support_state_digest": support_dig,
                 "knowledge_basis": {"basis_id": basis["basis_id"], "digest": basis["digest"]},
                 "minted_by_evaluation": evaluation["evaluation_id"],   # NEVER_EVALUATED unreachable
                 "granted_at": _now(),
                 "validity": {"window_hours": 24, "note": "and every invalidation predicate below"},
                 "invalidation_predicates": closure.get("invalidation_predicates", []),
                 "basis_null_capped_axes": capped,
                 "notes": ["state is a READ-TIME COMPUTATION (comp-lease state) -- never a stored verdict; "
                           "failure to reevaluate never preserves validity"]}
    return evaluation, lease, obs


def validate_effect_pair(evaluation: dict) -> None:
    """L1's binding law: a record carrying only one of the pair FAILS."""
    has_r = "effect_as_recorded" in evaluation
    has_e = "effect_as_evaluated" in evaluation
    if not (has_r and has_e):
        raise Refused("REFUSED (CTO Note 2): the evaluation record must carry BOTH effect_as_recorded AND "
                      "effect_as_evaluated -- with only the evaluated value, an audit of authority-expanding "
                      "edits silently counts the UNCOMPUTED ones")
    r, e = evaluation["effect_as_recorded"], evaluation["effect_as_evaluated"]
    if r is None and e != "EXPANDING":
        raise Refused("REFUSED: the UNCOMPUTED -> EXPANDING collapse is ONE-WAY and fail-toward-the-higher-bar; "
                      "recorded null must evaluate as EXPANDING, got %r" % e)


def lease_state(lease: dict, sides, env) -> tuple:
    """THE PARTITION TREE, computed at READ TIME. Returns (state, reasons, observations)."""
    rh = _normative_hash()
    subject = lease["subject"]["ref"]
    current = sides.read(subject)
    ok_map = current.get("_retrieval_ok", {})
    obs = [_obs(env, request={"op": "lease_state_side_read", "subject": subject},
                status={"acquisition": "PRESENT" if all(ok_map.values()) else "FAILED",
                        "transport": "SUCCEEDED", "enumeration": "SUCCEEDED", "parse": "SUCCEEDED"},
                plane="APPLIED", substrate="aws",
                population="the five support-member identities of one lease", count=len(SUPPORT_MEMBER_IDS),
                grain="support member", process="side re-read at state time",
                value={k: current.get(k) for k in SUPPORT_MEMBER_IDS} if all(ok_map.values()) else None,
                reason="side read failed", pointers=[lease["lease_id"]], invalidation=["any side moves"])]
    reasons = []
    # LEVEL 1 -- does the minting evaluation still bind?
    granted = {m["member_id"]: m["identity"] for m in lease["support_members"]}
    moved = [k for k in SUPPORT_MEMBER_IDS if ok_map.get(k, True) and current.get(k) != granted.get(k)]
    unreadable = [k for k in SUPPORT_MEMBER_IDS if not ok_map.get(k, True)]
    granted_at = lease.get("granted_at")
    window_h = (lease.get("validity") or {}).get("window_hours")
    window_lapsed = False
    if granted_at and window_h:
        try:
            t0 = time.mktime(time.strptime(granted_at, "%Y-%m-%dT%H:%M:%SZ"))
            window_lapsed = (time.time() - t0) > window_h * 3600
        except ValueError:
            window_lapsed = True   # an unparseable grant time cannot prove an open window
    if moved or window_lapsed:
        if moved:
            reasons.append("support identity(ies) moved since the minting evaluation: %s (%s)"
                           % (moved, {k: "%s -> %s" % (str(granted.get(k))[:16], str(current.get(k))[:16]) for k in moved}))
        if window_lapsed:
            reasons.append("validity window lapsed")
        reasons.append("the minting evaluation no longer BINDS -- its result is out of scope, not out-ranked; "
                       "failure to reevaluate never preserves validity")
        return ("EXPIRED", reasons, obs)
    if unreadable:
        reasons.append("support identity(ies) unreadable at state time: %s -- a retrieval failure is never support" % unreadable)
        return ("UNKNOWN", reasons, obs)
    # LEVEL 2 -- the evaluation's result (the lease was minted by ELIGIBLE or UNKNOWN)
    if lease.get("basis_null_capped_axes"):
        reasons.append("binds; basis members %s null (UNRATIFIED_BASIS) cap their governed axes -- reliance on "
                       "those axes is UNKNOWN; support-identity axes are VALID" % lease["basis_null_capped_axes"])
        # the SUPPORT-IDENTITY claim is what this lease leases; the capped axes are named, not folded in
    reasons.append("all five support identities equal the minted identities (support_state_digest %s reproduced: %s)"
                   % (lease["support_state_digest"][:18], _support_digest(rh, current) == lease["support_state_digest"]))
    return ("VALID", reasons, obs)


# ---------------------------------------------------------------------------------------------
# Self-test: m1-m5 + the UNCOMPUTED pair case + determinism. Offline, fixtures only.
# ---------------------------------------------------------------------------------------------
def self_test() -> int:  # noqa: PLR0915
    import copy  # noqa: PLC0415
    import tempfile  # noqa: PLC0415
    cc = _comp_closure()
    env = cc._envelope()  # noqa: SLF001 -- same package consumption as comp_closure itself
    rh = _normative_hash()
    ok = []

    def chk(name, cond):
        ok.append(bool(cond))
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))

    d = tempfile.mkdtemp(prefix="comp_lease_st_")
    vint = {"source_map_updated": "v1", "artifact_sha256": "aaa", "live_code_sha256": "LLL",
            "last_deployed_commit": "c1", "repo_head": "H1"}
    closure = {"object": "Support_Closure", "subject": {"kind": "LAMBDA_RUNS_CODE", "ref": "fn-x"},
               "vintage": dict(vint), "invalidation_predicates": ["source map entry changes"]}
    cp = os.path.join(d, "fn-x.closure.json")
    json.dump(closure, open(cp, "w", encoding="utf-8"))
    sides = FixtureSides(vint)
    basis = load_basis()
    chk("0 the consumed basis is honest: %s; five members, digest via the NORMATIVE home (reproduced: %s)"
        % ("MINTED" if not basis.get("fixture") else "LOCAL FIXTURE (declared)", basis["digest"] == rh(basis["members"]) if basis.get("fixture") else "n/a"),
        set(basis["members"].keys()) == set(NULL_MEMBERS) and (not basis.get("fixture") or basis["digest"] == rh(basis["members"])))
    ev, lease, obs = evaluate(cp, sides, env, basis)
    chk("1 first evaluation over an unchanged closure -> ELIGIBLE with the null-cap stated; lease minted BY the evaluation "
        "(NEVER_EVALUATED unreachable); both effect fields present; observations envelope-valid",
        ev["result"] == "ELIGIBLE" and lease is not None and lease["minted_by_evaluation"] == ev["evaluation_id"]
        and "effect_as_recorded" in ev and "effect_as_evaluated" in ev
        and ev["basis_null_capped_axes"] == sorted(NULL_MEMBERS) and all(env.validate_record(o) == [] for o in obs))
    st, why, _o = lease_state(lease, sides, env)
    chk("1b state on unchanged sides -> VALID via the partition tree (binds + supported), capped axes NAMED in the reasons",
        st == "VALID" and any("UNRATIFIED_BASIS" in r for r in why))
    # m1 -- a support member changes and the lease is NOT re-evaluated
    moved_sides = FixtureSides({**vint, "live_code_sha256": "MMM"})
    st1, why1, _o = lease_state(lease, moved_sides, env)
    chk("m1 support member changed, NO re-evaluation -> EXPIRED, never VALID ('failure to reevaluate never preserves validity')",
        st1 == "EXPIRED" and any("no longer BINDS" in r for r in why1))
    st1b, _w, _o = lease_state(lease, FixtureSides(vint, fail_keys=("live_code_sha256",)), env)
    chk("m1b a side UNREADABLE at state time -> UNKNOWN, never VALID (a retrieval failure is never support)", st1b == "UNKNOWN")
    # m2 -- an under-including coarse intersection
    try:
        evaluate(cp, sides, env, basis, declared_coordinates=["artifact_sha256", "repo_head"], scope="m2-scope")
        m2 = False
    except Refused as e:
        m2 = "m2" in str(e) and "UNDER-includes" in str(e)
    chk("m2 a declared coarse intersection that UNDER-includes -> REFUSED (over-include by construction)", m2)
    # m3 -- waiver law, both directions
    moved2 = FixtureSides({**vint, "artifact_sha256": "bbb"})
    try:
        evaluate(cp, moved2, env, basis, scope="m3-old-waiver",
                 waivers=[{"kind": "ENUMERATED", "members": ["artifact_sha256"], "minted_before_member": True}])
        m3a = False
    except Refused as e:
        m3a = "m3" in str(e)
    ev3, _l3, _o = evaluate(cp, moved2, env, basis, scope="m3-predicate",
                            waivers=[{"kind": "RATIFIED_PREDICATE", "ref": "policy:artifact-repin@v1",
                                      "scope_predicate": lambda c: c == "artifact_sha256"}])
    chk("m3 a NEW member on an OLD enumerated waiver -> REFUSED; a ratified predicate whose declared scope includes it -> covers "
        "(both directions)", m3a and ev3["result"] == "ELIGIBLE" and ev3["waivers_applied"])
    # m4 -- one evaluation per (assessment, scope, basis, support-state)
    try:
        evaluate(cp, sides, env, basis)   # identical to test 1's key
        m4 = False
    except Refused as e:
        m4 = "m4" in str(e)
    ev4b, _l, _o = evaluate(cp, moved_sides, env, basis)   # changed support state -> legitimately NEW
    chk("m4 the SAME (assessment, scope, basis, support-state) evaluated twice -> REFUSED; a CHANGED support state is a "
        "legitimately new evaluation (INELIGIBLE here: the identity moved uncovered)", m4 and ev4b["result"] == "INELIGIBLE")
    # m5 -- untyped silence as an exclusion proof
    try:
        evaluate(cp, moved2, env, basis, scope="m5-scope", exclusion_proofs=[{"note": "we did not see it change"}])
        m5 = False
    except Refused as e:
        m5 = "m5" in str(e)
    chk("m5 untyped silence offered as an exclusion proof -> REFUSED (typed ATTESTED_ABSENCE/RULED_OUT_BY_EVIDENCE only)", m5)
    ev5, _l, _o = evaluate(cp, moved2, env, basis, scope="m5-typed",
                           exclusion_proofs=[{"kind": "RULED_OUT_BY_EVIDENCE", "ref": "control-run@x", "excludes": "artifact_sha256"}])
    chk("m5b a TYPED proof covering the moved member -> replayed, residual empty, ELIGIBLE", ev5["result"] == "ELIGIBLE" and ev5["exclusion_proofs"])
    # CTO Note 2: the UNCOMPUTED case + the pair law
    ev6, _l, _o = evaluate(cp, sides, env, basis, scope="uncomputed-case", basis_change={"effect": None})
    chk("6 a Basis_Change with effect UNCOMPUTED (null) -> effect_as_recorded null + effect_as_evaluated EXPANDING (one-way, "
        "auditable as the PAIR)", ev6["effect_as_recorded"] is None and ev6["effect_as_evaluated"] == "EXPANDING")
    bad = copy.deepcopy(ev6)
    del bad["effect_as_recorded"]
    try:
        validate_effect_pair(bad)
        pair = False
    except Refused:
        pair = True
    chk("6b a record carrying only the evaluated value -> FAIL (the audit law)", pair)
    # determinism: same inputs -> same evaluation modulo timestamps/ids derived from them
    _SEEN_EVALUATIONS.clear()
    e1, l1, _ = evaluate(cp, sides, env, basis)
    _SEEN_EVALUATIONS.clear()
    e2, l2, _ = evaluate(cp, sides, env, basis)

    def strip(x):
        return json.dumps({k: v for k, v in x.items() if k not in ("evaluated_at", "granted_at")}, sort_keys=True, default=str)
    chk("7 determinism: two evaluations of the same inputs agree on every field but timestamps (ids are digest-derived and equal)",
        strip(e1) == strip(e2) and (l1 is None) == (l2 is None) and strip(l1) == strip(l2))
    chk("8 no ordering language on the objects: state is computed by the partition tree, never stored; no 'precedence' anywhere",
        "precedence" not in json.dumps(e1).lower() and "state" not in l1)
    import shutil  # noqa: PLC0415
    shutil.rmtree(d, ignore_errors=True)
    n = sum(1 for x in ok if x)
    print("--- comp-lease self-test: %d/%d passed ---" % (n, len(ok)))
    return 0 if n == len(ok) else 1


_USAGE = """comp-lease -- NFRA_EPISTEMY C4: four-state lease service + Eligibility_Evaluation. Usage:
  comp-lease evaluate <closure.json> [--out DIR]   run ONE evaluation over a committed C3 closure; mint the lease it licenses
  comp-lease state <lease.json>                    compute the lease's state NOW (read-time partition tree; live side re-read)
  comp-lease --self-test                           offline battery m1-m5 + effect-pair + determinism (fixtures, never AWS)
  comp-lease --help | -h                           this usage (never writes)
States: VALID | INVALID | UNKNOWN | EXPIRED (a partition tree, no ordering). Unknown arguments REFUSE (rc 2)."""


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or "--help" in args or "-h" in args:
        print(_USAGE)
        return 0
    if "--self-test" in args:
        return self_test()
    cmd = args[0]
    if cmd not in ("evaluate", "state"):
        print("comp-lease: UNKNOWN argument %r -- REFUSED (rc 2).\n%s" % (cmd, _USAGE), file=sys.stderr)
        return 2
    flags = [a for a in args[1:] if a.startswith("-") and a != "--out"]
    if flags or len(args) < 2:
        print("comp-lease: UNKNOWN/missing argument(s) %s -- REFUSED (rc 2)." % (flags or ["<target>"]), file=sys.stderr)
        return 2
    try:
        cc = _comp_closure()
        env = cc._envelope()  # noqa: SLF001
        sides = LiveSides()
        out = args[args.index("--out") + 1] if "--out" in args else OUT_DIR
        os.makedirs(out, exist_ok=True)
        if cmd == "evaluate":
            ev, lease, obs = evaluate(args[1], sides, env)
            bad = [e for o in obs for e in env.validate_record(o)]
            if bad:
                print("comp-lease: envelope validation FAILED: %s" % bad[:3], file=sys.stderr)
                return 1
            base = os.path.join(out, ev["evaluation_id"])
            json.dump(ev, open(base + ".evaluation.json", "w", encoding="utf-8"), indent=1)
            json.dump(obs, open(base + ".observations.json", "w", encoding="utf-8"), indent=1)
            line = "comp-lease evaluate %s: result=%s (basis %s; capped axes %s)" % (
                ev["scope"], ev["result"], ev["current_basis"]["basis_id"], ev["basis_null_capped_axes"])
            if lease:
                json.dump(lease, open(base + ".lease.json", "w", encoding="utf-8"), indent=1)
                line += " | lease %s minted by this evaluation" % lease["lease_id"]
            print(line)
            print("  result_basis: %s" % ev["result_basis"])
            print("  wrote %s.*.json" % base)
            return 0
        lease = json.load(open(args[1], encoding="utf-8"))
        st, reasons, _obs = lease_state(lease, sides, env)
        print("comp-lease state %s: %s" % (lease["lease_id"], st))
        for r in reasons:
            print("  - %s" % r)
        return 0
    except Refused as e:
        print("comp-lease: %s" % e, file=sys.stderr)
        return 2
    except Exception as e:  # noqa: BLE001 -- a service that cannot evaluate is an ERROR, never a clean lease
        print("comp-lease: ERROR (%s: %s)" % (type(e).__name__, e), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
