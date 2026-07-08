#!/usr/bin/env python3
"""comp_promote_materializer -- NFRA_PROMOTE-P2 / GOV-B: the LIVE hot-registration PRODUCER.

Closes NFRA_SEMCTL.GOV-B end-to-end. The seam has three composing halves:

  consumer half  = RecognizerRegistry (comp_recognizer_sdk.py, landed 6004a91c0) -- the hot-reloadable,
                   surfaced (artifact_class, concept) registry with register/reload/deregister + on_register.
  manifest half  = the git-versioned promote_recognizer_manifest.json (DS~B; ratify-gated write,
                   recognizer:silent-display-fork MATERIALIZED under CTO-PROMOTE-20260708T1521Z).
  THIS (my half) = the LIVE-hot-LOAD: read the git-versioned manifest -> construct a template+params
                   Recognizer (R2: NO code-gen) -> register() it into a RUNNING RecognizerRegistry
                   WITHOUT a redeploy (next-run load; no daemon assumption -- Q1 option-A) -> PROVE it
                   reaches the LIVE dispatch set (exercised via recognizers_for + recognize, NOT a
                   manifest config-read) -> MATERIALIZED CSE. demote() -> deregister() FAIL-LOUD -> DEMOTED CSE.

Arch-ratified design 4d0886493 (CTO ruled all 4 Qs). The 4 refinements, folded:
  R1 -- vintage honesty: "hot" = next-run (a latency); the load stamps a load-marker (content-marker over
        the manifest) and every promoted recognizer is reported "live as-of <load-marker>".
  R2 -- template+params ONLY (a parameterized instance of a KNOWN Recognizer class -- pure-lexical,
        fidelity-checkable by construction). code_gen is HARD-DEFERRED: a code_gen:true entry is REJECTED
        (generated code is a category change needing its own arch-gate + sandbox + security review).
  R3 -- the promoted-recognizer store is a git-versioned NAMED CRITICAL SURFACE (critical-surfaces.yaml
        compilerkit.promote_seam); a write goes through comp-surface-check at commit-time. This loader is
        READ-ONLY over that store (no shared-state contention with DS~B's write-only producer).
  R4 -- MATERIALIZED/DEMOTED emission: a FIRST-CLASS schema-validated CSE via the governed ProducerKind.PROMOTE
        (cse_schema @0.4, landed 995419d28 -- CTO-arch-gated + CVO-re-signed 72d8fa58b + COO SoD). Emitted
        through cse_schema.validate_or_raise (fail-closed) to the inspectable promote_materialize_cse.jsonl
        trail -- RETIRING the pre-@0.4 lifecycle trail-record interim. Design/proof: the deliverables-side
        proposal NFRA_PROMOTE_P2_GOVB_R4_promote_emission_contract.py (12/12, the governed-propose artifact).

CVO NON-NEGOTIABLES, built to from the start (exercised in the self-test red-fixture):
  (1) HOT-REGISTRATION EXERCISED, not config-read: a promoted recognizer register()s LIVE, is returned by
      recognizers_for() (the dispatch function a running compiler calls), AND recognize()s over a tree.
  (2) REVERSIBILITY EXERCISED: an actual deregister rollback (recognizers_for no longer returns it) + an
      exercised fail-loud gate-block (deregister of a not-live key raises KeyError) -- NOT asserted.
  (3) ZERO AUTO-MUTATION proven: materialize_live() is RATIFY-GATED -- no commission_id -> REFUSE before
      any register() call (grep-proof: the gate precedes the write); after a refused call the registry is
      unchanged (exercised). Only state==MATERIALIZED + non-null commission_id entries ever load (DS~B guard).

Usage:
  python comp_promote_materializer.py                 # load the live registry from the manifest + report (GOV-B live)
  python comp_promote_materializer.py --self-test      # the exercised red-fixture (CVO's 3 non-negotiables)
  python comp_promote_materializer.py --demote <cid> --commission <id>   # exercised reversibility (CVO)

Author: 0.8.0_AE_CloudComp~D (NFRA_PROMOTE.P2 GOV-B producer, live-hot-registration). 2026-07-08.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

# Path-robust import of the consumer seam (sibling in org/modules/graph), mirroring the SDK's own bootstrap.
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))

from comp_recognizer_sdk import (  # noqa: E402
    EnrichedTree, EntityRef, Entity, FrontEndCapability, PROMOTE_SEAM, Provenance, Recognizer,
    RecognizerRegistry, Site, Transformation, emit_cse, locus_at,
)
from cse_schema import (  # noqa: E402
    CSE as CSEvent, LOW_CONFIDENCE_MAX, ProducerKind, Qualifier, SCHEMA_VERSION, validate_or_raise,
)

# DS~B's git-versioned manifest (the R3 named critical surface). READ-ONLY here -- DS~B is the sole writer.
MANIFEST = os.path.join(WS, "org", "tier2_senior", "0.4.0_DS_ClientPlatform",
                        "deliverables", "promote_recognizer_manifest.json")
# The runtime "control fires when exercised" trail: every register/reload/deregister is surfaced here,
# never silent (the I3 arm; the commit-time comp-surface-check CLI covers the manifest-write arm -- R3).
SURFACE_EVENT_LOG = os.path.join(_HERE, "promote_surface_events.jsonl")
# The MATERIALIZED/DEMOTED lifecycle CSE trail (R4 -- inspectable; producer_kind label PROMOTE/MATERIALIZER).
MATERIALIZE_CSE_LOG = os.path.join(_HERE, "promote_materialize_cse.jsonl")

# R4 LANDED (@0.4, 995419d28 -- CTO-arch-gated + CVO-re-signed 72d8fa58b + COO SoD): ProducerKind.PROMOTE is
# now a GOVERNED enum value, so the MATERIALIZED/DEMOTED transition emits a FIRST-CLASS schema-validated CSE
# (through cse_schema.validate_or_raise) -- this RETIRES the pre-@0.4 lifecycle trail-record interim. The
# subject is Concept(untyped)+low (a recognizer has no Entity.RECOGNIZER -> honest-degrade, LAW 1). The LOW
# band is the SUBJECT's TYPE-confidence, NOT the promotion EVENT's certainty (CTO arch-gate note) -- FEDOBS
# consumers must not discount a promote CSE for its LOW band.
_PROMOTE_TYPE_CONFIDENCE = 0.2   # low-band (<= LOW_CONFIDENCE_MAX): the Concept subject's type-confidence

# The KNOWN recognizer TEMPLATES (R2: a promoted recognizer is a parameterized instance of one of these,
# NOT generated code). artifact_class = the plane the idiom's detector runs over (frontend TS/TSX).
KNOWN_TEMPLATES = {
    "c2-motif-recognizer": "typescript",   # a recurring frontend co-evolution idiom
    "c3-system-recognizer": "typescript",  # a C3 system of co-evolving idioms
}


# ---------------------------------------------------------------------------
# ManifestRecognizer -- a TEMPLATE+PARAMS recognizer (R2). A parameterized instance of a KNOWN, pure-lexical
# recognizer class: it detects the idiom lexically and emits a Concept (the honest-degrade target -- a motif
# occurrence is a lexical pattern, NOT a typed cloud Entity, so Concept(untyped)+low is its honest form,
# fidelity-checkable by construction). The detector query (the manifest `detector` param, e.g. the TSGRAPH
# D1-D7 shape) is a DETECTOR PLUG-IN keyed off params; the default is a generic idiom-token lexical rule.
# Swapping the plug-in changes WHAT is matched, never the registration/dispatch path this module productionizes.
# ---------------------------------------------------------------------------
class ManifestRecognizer(Recognizer):
    requires = FrontEndCapability.RAW_TEXT      # pure-lexical -> dispatches on any tree (no resolution needed)
    compiler_id = "compilerkit"
    producer_kind = ProducerKind.INFRA.value
    emits = (Entity.CONCEPT.value,)             # a motif occurrence is a Concept, emitted by construction

    def __init__(self, *, artifact_class: str, concept: str, idiom: str, detector: str,
                 recognizer_id: str, warrant: dict, commission_id: str, template: str):
        self.artifact_class = artifact_class
        self.concept = concept
        self.idiom = idiom
        self.detector = detector
        self.recognizer_id = recognizer_id
        self.warrant = warrant
        self.commission_id = commission_id
        self.template = template
        # the generic pure-lexical detector rule: the idiom's tokens must co-occur on a line. A real
        # per-motif TSGRAPH D1-D7 query is a detector plug-in (params.detector) over this same seam.
        self._tokens = [t for t in idiom.replace("_", "-").split("-") if t]

    def iter_sites(self, tree: EnrichedTree):
        text = tree.text or ""
        for i, line in enumerate(text.splitlines(), start=1):
            low = line.lower()
            if self._tokens and all(tok in low for tok in self._tokens):
                yield Site(source=tree.source, locus=locus_at(text, text.find(line)),
                           evidence=line.strip()[:200], payload={"idiom": self.idiom})

    def emit(self, site: Site, tree: EnrichedTree, *, marker_head: str):
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept,
                          evidence=site.evidence or "(no lexical evidence captured)")
        # Concept(untyped)+LOW -- the honest representation of a lexically-recognized motif (LAW 1); a promoted
        # motif recognizer never smuggles a typed cloud Entity. Fidelity-checkable (decompresses to the site).
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.CONCEPT.value, f"concept:{self.concept}@{site.source}:{site.locus}"),
            edges=[], provenance=prov, confidence=LOW_CONFIDENCE_MAX, marker_head=marker_head,
            producer_kind=self.producer_kind, compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )]


# ---------------------------------------------------------------------------
# build_recognizer -- construct a ManifestRecognizer from a manifest ENTRY (R2 gate: reject code-gen).
# ---------------------------------------------------------------------------
def build_recognizer(entry: dict) -> ManifestRecognizer:
    kind = entry.get("kind") or {}
    if kind.get("code_gen") is True:
        raise ValueError(
            "REJECTED -- code_gen:true. Generated recognizer code is HARD-DEFERRED (R2): a category change "
            "needing its own arch-gate (sandbox + fidelity/pure-lexical gate + security review). P2 loads "
            "template+params ONLY.")
    template = kind.get("template")
    if template not in KNOWN_TEMPLATES:
        raise ValueError(f"REJECTED -- unknown template {template!r} (known: {sorted(KNOWN_TEMPLATES)}). A "
                         "promoted recognizer must be a parameterized instance of a KNOWN template, not code.")
    params = kind.get("params") or {}
    idiom = params.get("idiom") or entry.get("from_candidate", "").split(":", 1)[-1]
    if not idiom:
        raise ValueError("REJECTED -- entry has no idiom param to parameterize the template with.")
    return ManifestRecognizer(
        artifact_class=KNOWN_TEMPLATES[template], concept=idiom, idiom=idiom,
        detector=params.get("detector", ""), recognizer_id=entry.get("recognizer_id", f"recognizer:{idiom}"),
        warrant=entry.get("warrant", {}), commission_id=entry.get("commission_id", ""), template=template)


# ---------------------------------------------------------------------------
# The on_register surface hook (S3 / the I3 "a control must fire when exercised" arm). Makes EVERY
# register/reload/deregister NON-SILENT (a structured surface event), so a no-op/collision surfaces.
# ---------------------------------------------------------------------------
def make_surface_hook(sink: list):
    def _hook(seam: str, artifact_class: str, concept: str) -> None:
        ev = {"surface": PROMOTE_SEAM, "seam": seam, "artifact_class": artifact_class, "concept": concept}
        sink.append(ev)
        # persist the surface event on-record too (never silent -> inspectable trail, not just in-memory).
        try:
            with open(SURFACE_EVENT_LOG, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(ev) + "\n")
        except OSError:
            pass   # advisory persistence -- the in-memory sink is the load-bearing surfacing, disk is a bonus
    return _hook


def _load_marker(manifest: dict) -> str:
    """R1 vintage: a deterministic content-marker over the manifest recognizers -- the 'live as-of' stamp.
    (Date.* is unavailable in this runtime; a content-marker is the honest, reproducible vintage anchor.)"""
    body = json.dumps(manifest.get("recognizers", {}), sort_keys=True).encode("utf-8")
    return hashlib.sha1(body).hexdigest()[:16]


def _read_manifest(path: str = MANIFEST) -> dict:
    if not os.path.exists(path):
        return {"recognizers": {}}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def _loadable(entry: dict) -> bool:
    """DS~B guard: hot-load ONLY a MATERIALIZED entry with a non-null commission_id (never a PROPOSED /
    pre-ratify / vanished one). This is the ratify-gate at the load boundary (zero auto-mutation)."""
    return entry.get("state") == "MATERIALIZED" and bool(entry.get("commission_id"))


def _in_dispatch(registry: RecognizerRegistry, r: ManifestRecognizer) -> bool:
    """The EXERCISED dispatch proof: r is returned by recognizers_for() -- the function a running compiler
    actually calls to build its dispatch set -- NOT a manifest field read. Query at the max capability so a
    RAW_TEXT recognizer is never filtered on requires."""
    live = registry.recognizers_for(r.artifact_class, FrontEndCapability.RESOLVED_SEMANTIC)
    return any(x.concept == r.concept and x.artifact_class == r.artifact_class for x in live)


def _has_key(registry: RecognizerRegistry, artifact_class: str, concept: str) -> bool:
    """Public-surface check for an already-live (artifact_class, concept) -- avoids reaching into registry
    internals (register() raises on a dup; reload() replaces -- this picks the right one)."""
    return any(x.artifact_class == artifact_class and x.concept == concept for x in registry.all())


def _build_promote_cse(lifecycle_verb: str, recognizer_id: str, commission_id: str,
                       coupling_ratio, marker: str) -> CSEvent:
    """Build a FIRST-CLASS schema-validated promotion CSE via the governed ProducerKind.PROMOTE (@0.4).
    materialize -> verb create; demote -> verb delete (the exact-inverse transition pair). fail-closed:
    validate_or_raise REJECTS a malformed promote CSE -- the 5th-producer emission-contract, enforced."""
    tverb = Transformation.CREATE.value if lifecycle_verb == "materialize" else Transformation.DELETE.value
    prov = Provenance(
        source="org/tier2_senior/0.4.0_DS_ClientPlatform/deliverables/promote_recognizer_manifest.json",
        locus=recognizer_id, recognizer="promote_materializer",
        evidence=f"commission={commission_id} coupling_ratio={coupling_ratio} (ratified warrant)")
    cse = CSEvent(
        event_id=f"{ProducerKind.PROMOTE.value}:{recognizer_id}:{tverb}",
        schema_version=SCHEMA_VERSION,
        producer={"kind": ProducerKind.PROMOTE.value, "ref": commission_id},
        compiler={"id": "promote-materializer", "artifact_class": "promoted_recognizer", "version": SCHEMA_VERSION},
        # Concept(untyped) subject -> LOW confidence (S3.5): a recognizer has no typed cloud Entity.
        transformation={"verb": tverb, "subject": EntityRef(Entity.CONCEPT.value, recognizer_id), "edges": []},
        provenance=prov,
        execution_meta={"timestamp": "", "actor": "comp_promote_materializer", "run_id": commission_id},
        head={"marker_head": marker},
        qualifiers={Qualifier.CONFIDENCE.value: _PROMOTE_TYPE_CONFIDENCE, Qualifier.SCOPE.value: PROMOTE_SEAM})
    validate_or_raise(cse)   # first-class + schema-validated -- a malformed promote CSE RAISES (fail-closed)
    return cse


def _emit_lifecycle_cse(verb: str, recognizer_id: str, commission_id: str, load_marker: str,
                        detail: str, coupling_ratio=None) -> dict:
    """R4 LANDED (@0.4): emit a FIRST-CLASS schema-validated promotion CSE (ProducerKind.PROMOTE), replacing
    the pre-@0.4 lifecycle trail-record interim. The emission goes through cse_schema.validate_or_raise
    (fail-closed) BEFORE the inspectable trail write -- a malformed promote CSE never reaches the trail."""
    cse = _build_promote_cse(verb, recognizer_id, commission_id, coupling_ratio, load_marker)
    record = {
        "cse_kind": "promotion_materialize",
        "event_id": cse.event_id,
        "schema_version": cse.schema_version,               # 0.4
        "producer_kind": cse.producer["kind"],              # "promote" -- governed ProducerKind.PROMOTE
        "verb": cse.transformation["verb"],                 # create | delete
        "lifecycle_verb": verb,                             # materialize | demote
        "subject_ref": recognizer_id,
        "commission_id": commission_id,
        "confidence": cse.qualifiers[Qualifier.CONFIDENCE.value],
        "provenance": {"source": cse.provenance.source, "locus": cse.provenance.locus,
                       "evidence": cse.provenance.evidence},
        "vintage": {"live_as_of": load_marker},
        "detail": detail,
        "schema_validated": True,   # emitted through cse_schema.validate_or_raise (first-class 5th producer @0.4)
    }
    with open(MATERIALIZE_CSE_LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(record) + "\n")
    return record


# ---------------------------------------------------------------------------
# load_live_registry -- THE hot-load (Q1 option-A: next-run load from the manifest, no redeploy/daemon).
# Reads the git-versioned manifest -> builds + register()s each loadable recognizer into a LIVE registry
# with the surface hook bound -> POST-REGISTER VERIFIES each reaches the dispatch set (LOUD on a no-op).
# Returns (registry, load_marker, report). This is what a running compiler calls at each run to acquire
# newly-promoted recognizers -- "hot" = next run, no code push.
# ---------------------------------------------------------------------------
def load_live_registry(manifest_path: str = MANIFEST, registry: RecognizerRegistry | None = None) -> tuple:
    manifest = _read_manifest(manifest_path)
    load_marker = _load_marker(manifest)
    surfaced: list = []
    if registry is None:
        registry = RecognizerRegistry(on_register=make_surface_hook(surfaced))
    registered, skipped, failed = [], [], []
    for rid, entry in (manifest.get("recognizers") or {}).items():
        if not _loadable(entry):
            skipped.append((rid, entry.get("state"), "not MATERIALIZED-under-commission"))
            continue
        r = build_recognizer(entry)
        if _has_key(registry, r.artifact_class, r.concept):   # already live (a prior load) -> hot-reload, not a dup-raise
            registry.reload(r)
        else:
            registry.register(r)
        # POST-REGISTER VERIFY (exercised, S3): the registration must have TAKEN -- r is in the live dispatch
        # set. A silent no-op (wrong key / dup-swallow) would certify a promotion that never reached dispatch.
        if _in_dispatch(registry, r):
            registered.append({"recognizer_id": r.recognizer_id, "concept": r.concept,
                               "artifact_class": r.artifact_class, "commission_id": r.commission_id,
                               "live_as_of": load_marker})
        else:
            failed.append(rid)
            raise RuntimeError(f"PROMOTION-FAILED (LOUD): {rid} registered but is NOT in the live dispatch "
                               f"set (recognizers_for). A no-op registration must never certify GREEN.")
    report = {"registered": registered, "skipped": skipped, "failed": failed,
              "surfaced_events": surfaced, "load_marker": load_marker, "manifest": manifest_path}
    return registry, load_marker, report


# ---------------------------------------------------------------------------
# demote_live -- REVERSIBILITY (invariant #4): deregister() a live promoted recognizer, FAIL-LOUD on a
# missing key (never a silent no-op), verify it left the dispatch set, emit a DEMOTED CSE.
# ---------------------------------------------------------------------------
def demote_live(concept: str, registry: RecognizerRegistry, *, artifact_class: str = "typescript",
                commission_id: str | None = None, recognizer_id: str | None = None) -> tuple:
    # deregister is fail-loud by contract (KeyError on a missing key) -- let it propagate (the exercised
    # gate-block). Verify the removal actually left the dispatch set.
    registry.deregister(artifact_class, concept)
    still = registry.recognizers_for(artifact_class, FrontEndCapability.RESOLVED_SEMANTIC)
    if any(x.concept == concept for x in still):
        raise RuntimeError(f"DEMOTE-FAILED (LOUD): {concept} deregistered but STILL in the dispatch set.")
    man = _read_manifest()
    marker = _load_marker(man)
    rid = recognizer_id or f"recognizer:{concept}"
    cr = ((man.get("recognizers") or {}).get(rid, {}).get("warrant") or {}).get("coupling_ratio")
    cse = _emit_lifecycle_cse("demote", rid, commission_id or "", marker,
                              "recognizer hot-deregistered from the LIVE registry (exact inverse of load)",
                              coupling_ratio=cr)
    return True, cse, "DEMOTED -> hot-deregistered from the live registry (reversible; fail-loud on absence)"


# ---------------------------------------------------------------------------
# materialize_live -- hot-register ONE ratified recognizer into a live registry. RATIFY-GATED (zero
# auto-mutation): REFUSES without a commission_id BEFORE any register() call. The commission must match the
# entry's ratifier commission (the same CTO ratify that wrote the manifest entry authorizes the live-load).
# ---------------------------------------------------------------------------
def materialize_live(concept: str, registry: RecognizerRegistry | None = None,
                     commission_id: str | None = None, manifest_path: str = MANIFEST) -> tuple:
    if not commission_id:
        # THE anti-auto-mutation gate -- precedes every write (grep-proof: no register() above this return).
        return None, None, ("REFUSED -- no ratifier commission_id. materialize_live() is ratify-gated "
                            "(invariant #3, R3): a recognizer hot-loads LIVE ONLY under an explicit ratify.")
    manifest = _read_manifest(manifest_path)
    rid = f"recognizer:{concept}"
    entry = (manifest.get("recognizers") or {}).get(rid)
    if entry is None or not _loadable(entry):
        return None, None, f"REFUSED -- {rid} is not a MATERIALIZED-under-commission manifest entry."
    if entry.get("commission_id") != commission_id:
        return None, None, (f"REFUSED -- commission mismatch: passed {commission_id!r} != entry ratifier "
                            f"{entry.get('commission_id')!r}. The live-load is authorized by the SAME ratify.")
    surfaced: list = []
    if registry is None:
        registry = RecognizerRegistry(on_register=make_surface_hook(surfaced))
    r = build_recognizer(entry)
    if _has_key(registry, r.artifact_class, r.concept):
        registry.reload(r)
    else:
        registry.register(r)
    if not _in_dispatch(registry, r):
        raise RuntimeError(f"PROMOTION-FAILED (LOUD): {rid} did not reach the live dispatch set.")
    marker = _load_marker(manifest)
    cse = _emit_lifecycle_cse("materialize", rid, commission_id, marker,
                              "recognizer hot-registered LIVE + verified in the dispatch set (exercised)",
                              coupling_ratio=(entry.get("warrant") or {}).get("coupling_ratio"))
    return {"recognizer_id": rid, "concept": r.concept, "artifact_class": r.artifact_class,
            "live_as_of": marker, "registry": registry, "surfaced": surfaced}, cse, \
        "MATERIALIZED -> hot-registered into the LIVE registry (exercised dispatch; reversible)"


# ---------------------------------------------------------------------------
# Default run: load the live registry from the manifest + report GOV-B live.
# ---------------------------------------------------------------------------
def run_report() -> int:
    print("=" * 84)
    print("comp_promote_materializer -- GOV-B LIVE hot-load (manifest -> running RecognizerRegistry)")
    print("=" * 84)
    if not os.path.exists(MANIFEST):
        print("no manifest at %s -- DS~B's ratify-gated producer has not written one yet." % os.path.relpath(MANIFEST, WS))
        return 1
    registry, marker, report = load_live_registry()
    print("\nManifest: %s" % os.path.relpath(MANIFEST, WS))
    print("Load-marker (R1 vintage -- 'live as-of'): %s\n" % marker)
    print("HOT-REGISTERED into the LIVE registry (exercised: in recognizers_for dispatch set):")
    for r in report["registered"]:
        print("  %-34s concept=%-22s artifact_class=%s" % (r["recognizer_id"], r["concept"], r["artifact_class"]))
        print("       commission=%s  live_as_of=%s" % (r["commission_id"], r["live_as_of"]))
    for rid, state, why in report["skipped"]:
        print("  SKIP %-30s state=%s (%s)" % (rid, state, why))
    print("\nSurfaced registration events (I3 -- no silent add): %d" % len(report["surfaced_events"]))
    for ev in report["surfaced_events"]:
        print("  %s  %s/%s" % (ev["seam"], ev["artifact_class"], ev["concept"]))
    print("\n" + "-" * 84)
    print("%d promoted recognizer(s) LIVE in the dispatch set, no redeploy (next-run load, Q1 option-A)." %
          len(report["registered"]))
    print("Reversible: demote_live(concept) -> deregister fail-loud -> DEMOTED CSE. GOV-B producer half CLOSED.")
    return 0


# ---------------------------------------------------------------------------
# SELF-TEST -- the exercised RED-FIXTURE (CVO's 3 non-negotiables, built from the start; each EXERCISED).
# ---------------------------------------------------------------------------
def self_test() -> int:
    print("=== comp_promote_materializer self-test (GOV-B: the 3 CVO non-negotiables, EXERCISED) ===")
    ok = []

    def chk(name, cond):
        ok.append(bool(cond))
        print("  [%s] %s" % ("PASS" if cond else "FAIL", name))

    # ---- NON-NEGOTIABLE 1: HOT-REGISTRATION EXERCISED, not config-read. ----
    # Load the REAL manifest into a fresh live registry; silent-display-fork must (a) register, (b) be
    # returned by recognizers_for (the dispatch fn), and (c) actually recognize() over a tree.
    registry, marker, report = load_live_registry()
    reg_concepts = [r["concept"] for r in report["registered"]]
    chk("1  hot-registration EXERCISED: silent-display-fork loaded from the manifest + registered LIVE",
        "silent-display-fork" in reg_concepts)
    live = registry.recognizers_for("typescript", FrontEndCapability.RESOLVED_SEMANTIC)
    sdf = next((x for x in live if x.concept == "silent-display-fork"), None)
    chk("1a dispatch proof (NOT config-read): recognizers_for() RETURNS the promoted recognizer object",
        sdf is not None)
    # (c) it actually RUNS in the live dispatch path + emits a fidelity-passing Concept CSE.
    tree = EnrichedTree(source="portal/src/pages/ModelPortfolios.tsx", capability=FrontEndCapability.RAW_TEXT,
                        text="// a silent display fork occurrence on this line\nconst x = 1;\n")
    emitted = []
    if sdf is not None:
        cses, cov = sdf.recognize(tree, marker_head=marker)
        emitted = cses
    chk("1b the promoted recognizer RUNS in the live path (recognize -> >=1 Concept CSE)",
        len(emitted) >= 1 and emitted[0].transformation["subject"].etype == Entity.CONCEPT.value)
    fid_ok = False
    if emitted:
        from cse_schema import cse_fidelity_ok as _fid
        fid_ok = _fid(emitted[0])[0]
    chk("1c emitted CSE decompresses to C0 lexical evidence (fidelity, LAW 2)", bool(fid_ok))
    chk("1d surfaced (I3 -- no silent add): the registration fired the on_register hook",
        any(ev["concept"] == "silent-display-fork" for ev in report["surfaced_events"]))
    chk("1e R1 vintage honesty: a load-marker is stamped (live as-of)", bool(marker))

    # ---- NON-NEGOTIABLE 3: ZERO AUTO-MUTATION (test BEFORE demote so the registry is still populated). ----
    # materialize_live without a commission_id REFUSES before any register() -- and mutates nothing.
    fresh = RecognizerRegistry(on_register=make_surface_hook([]))
    res, cse, reason = materialize_live("silent-display-fork", registry=fresh, commission_id=None)
    chk("3  zero-auto-mutation: materialize_live REFUSES without a commission_id (ratify-gated)",
        res is None and "REFUSED" in reason)
    chk("3a proven no mutation: the registry is UNCHANGED after the refused call (nothing registered)",
        len(fresh.all()) == 0)
    # a commission MISMATCH also refuses (the live-load must be authorized by the SAME ratify).
    res2, _, reason2 = materialize_live("silent-display-fork", registry=fresh, commission_id="WRONG-COMMISSION")
    chk("3b commission mismatch REFUSED (load authorized by the entry's ratifier, not any commission)",
        res2 is None and "mismatch" in reason2.lower())
    # R4 positive (@0.4): materialize_live under the REAL ratifier commission hot-registers + emits a
    # FIRST-CLASS schema-validated CREATE promote CSE (through validate_or_raise; the create-verb path).
    real_comm = (_read_manifest().get("recognizers") or {}).get(
        "recognizer:silent-display-fork", {}).get("commission_id")
    fresh2 = RecognizerRegistry(on_register=make_surface_hook([]))
    mres, mcse, _ = materialize_live("silent-display-fork", registry=fresh2, commission_id=real_comm)
    chk("R4b materialize_live (real commission) hot-registers + emits a validated CREATE promote CSE",
        mres is not None and isinstance(mcse, dict) and mcse.get("schema_validated") is True
        and mcse.get("verb") == "create" and mcse.get("producer_kind") == ProducerKind.PROMOTE.value)

    # ---- NON-NEGOTIABLE 2: REVERSIBILITY EXERCISED (actual rollback + fail-loud gate-block). ----
    before = _in_dispatch(registry, sdf) if sdf else False
    _, demote_cse, _ = demote_live("silent-display-fork", registry, artifact_class="typescript",
                                   commission_id="CVO-EXERCISE", recognizer_id="recognizer:silent-display-fork")
    after = any(x.concept == "silent-display-fork"
                for x in registry.recognizers_for("typescript", FrontEndCapability.RESOLVED_SEMANTIC))
    chk("2  reversibility EXERCISED: demote deregisters -> recognizers_for NO LONGER returns it (rollback)",
        before and not after)
    # R4 LANDED (@0.4): the demote emitted a FIRST-CLASS schema-validated ProducerKind.PROMOTE CSE (through
    # validate_or_raise -- a malformed one would have RAISED here), not the pre-@0.4 trail-record interim.
    chk("R4 schema-validated emission (@0.4): demote emits ProducerKind.PROMOTE CSE (validated, verb=delete)",
        isinstance(demote_cse, dict) and demote_cse.get("schema_validated") is True
        and demote_cse.get("producer_kind") == ProducerKind.PROMOTE.value
        and demote_cse.get("schema_version") == "0.4" and demote_cse.get("verb") == "delete")
    # the exercised FAIL-LOUD gate-block: deregister of a not-live key raises (never a silent no-op).
    failed_loud = False
    try:
        demote_live("not-a-live-recognizer", registry, artifact_class="typescript")
    except KeyError:
        failed_loud = True
    chk("2a fail-loud gate-block EXERCISED: demoting a not-live key raises KeyError (never silent no-op)",
        failed_loud)

    # ---- R2: code-gen HARD-DEFERRED (a code_gen:true entry is REJECTED, not loaded). ----
    codegen_rejected = False
    try:
        build_recognizer({"kind": {"template": "c2-motif-recognizer", "params": {"idiom": "x"}, "code_gen": True},
                          "recognizer_id": "recognizer:x", "commission_id": "c", "state": "MATERIALIZED"})
    except ValueError:
        codegen_rejected = True
    chk("R2 code-gen HARD-DEFERRED: a code_gen:true entry is REJECTED (template+params only)", codegen_rejected)
    # an unknown template is also rejected (must be a parameterized instance of a KNOWN class).
    unknown_rejected = False
    try:
        build_recognizer({"kind": {"template": "arbitrary-generated", "params": {"idiom": "x"}, "code_gen": False},
                          "recognizer_id": "recognizer:x", "commission_id": "c", "state": "MATERIALIZED"})
    except ValueError:
        unknown_rejected = True
    chk("R2b an unknown template is REJECTED (only KNOWN parameterizable templates load)", unknown_rejected)

    # ---- DS~B guard: a PROPOSED (pre-ratify) entry must NOT hot-load. ----
    proposed_manifest = os.path.join(_HERE, "_selftest_proposed_manifest.json")
    with open(proposed_manifest, "w", encoding="utf-8") as fh:
        json.dump({"recognizers": {"recognizer:pending": {
            "recognizer_id": "recognizer:pending", "from_candidate": "motif:pending", "state": "PROPOSED",
            "commission_id": None, "kind": {"template": "c2-motif-recognizer",
                                            "params": {"idiom": "pending"}, "code_gen": False}}}}, fh)
    try:
        _, _, prep = load_live_registry(manifest_path=proposed_manifest)
        chk("G  DS~B guard: a PROPOSED / no-commission entry does NOT hot-load (only MATERIALIZED-under-commission)",
            prep["registered"] == [] and len(prep["skipped"]) == 1)
    finally:
        os.remove(proposed_manifest)

    n = sum(1 for x in ok if x)
    print("--- self-test: %d/%d passed (hot-reg exercised + reversible exercised + zero-auto-mutation) ---"
          % (n, len(ok)))
    return 0 if n == len(ok) else 1


def main() -> int:
    for _s in (sys.stdout, sys.stderr):
        try:
            _s.reconfigure(errors="replace")
        except Exception:  # noqa: BLE001
            pass
    args = sys.argv[1:]
    if "--self-test" in args:
        return self_test()
    if "--demote" in args:
        concept = args[args.index("--demote") + 1]
        comm = args[args.index("--commission") + 1] if "--commission" in args else None
        registry, _, _ = load_live_registry()
        _, _, reason = demote_live(concept, registry, commission_id=comm)
        print(reason)
        return 0
    return run_report()


if __name__ == "__main__":
    sys.exit(main())
