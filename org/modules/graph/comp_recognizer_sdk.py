"""comp_recognizer_sdk -- NFRA_COMPILERKIT-P1: the shared Recognizer SDK (the framework the 2 production
compilers reconcile onto as a parity-oracle pair).

RECONCILE-NOT-BUILD: the IR is cse_schema.CSE (emission unit) + comp_ladder.Node (fidelity-checkable form
via cse_schema.to_ladder_node); the fidelity gate is comp_ladder.fidelity_check (bound in cse_schema.validate
S3.6); the validator is cse_schema.validate (fail-closed, LAW 1/2). This module adds the SHARED front-end +
recognizer + registry + parity plumbing so a new recognizer is a modular, orthogonal, additive, deterministic
unit that composes with no ordering deps and passes the SAME fidelity + parity gates.

CTO #3 ruling (binds the whole SDK): COMPILERKIT = PURE-LEXICAL provenance ONLY ({source,locus,evidence} =
file:line). Live-AWS recognizers (compiler #1 Pass-8 extract_event_invoke + the live satellites comp_aws_cli /
extract_iam boto leg) RE-HOME to FEDOBS -- NOT this framework. Pass-7 extract_sfn STAYS (pure-Python ASL
walker, boto3 uncalled).

The interface DS~A (recognizer-author) builds against:
  Recognizer  -- subclass with artifact_class + concept + requires; implement iter_sites() + emit();
                 the SDK owns recognize() (capability-gating + LAW-1 honest-degrade + coverage).
  emit_cse    -- construct a VALID CSE (validate_or_raise); a recognizer physically cannot emit an invalid one.
  FrontEnd    -- capability-tiered enriched-tree provider (per-artifact | whole-project lifecycles).
  RecognizerRegistry -- hot-reloadable, keyed (artifact_class, concept); the PROMOTE-seam (named surface).

STATUS (P1): the DECISION-INDEPENDENT core (this file) is landed + self-tested. CTO-decision-dependent parts
are stubbed + flagged: FLOWS_TO KIND+condition (cse_schema version-bump, decision #1) + the PROMOTE-seam
wiring shape (decision #2). The coverage channel (decision #3) is implemented proactively per the design.

Design: org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_COMPILERKIT/COMPILERKIT-P1-FRAMEWORK-DESIGN.md
Author: 0.8.0_AE_CloudComp~D (NFRA_COMPILERKIT.P1, framework-lead). 2026-07-07.
"""

from __future__ import annotations

import hashlib
import os
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Iterable

# Path-robust import of the CSE IR (sibling in org/modules/graph), mirroring cse_schema's own bootstrap.
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
import cse_schema as cse  # noqa: E402
from cse_schema import (  # noqa: E402
    CSE, EntityRef, Provenance, RelationshipDelta, Entity, Relationship, Transformation, Qualifier,
    ProducerKind, SCHEMA_VERSION, LOW_CONFIDENCE_MAX, validate_or_raise,
)

# One import surface for recognizer-authors (DS~A): the CSE-emit vocabulary re-exported from the SDK, so a
# recognizer does `from comp_recognizer_sdk import Recognizer, emit_cse, EntityRef, RelationshipDelta, ...`.
__all__ = [
    "FrontEndCapability", "Site", "Coverage", "EnrichedTree", "FrontEnd", "Recognizer",
    "RecognizerRegistry", "PROMOTE_SEAM", "emit_cse", "run_recognizers", "derive_compiler_emits",
    "locus_at", "locus_span", "detect_collapse",
    # re-exported CSE IR vocabulary (authored against cse_schema; surfaced here for one-import authoring)
    "EntityRef", "RelationshipDelta", "Provenance", "Entity", "Relationship", "Transformation",
    "Qualifier", "ProducerKind", "CSE",
]


# ---------------------------------------------------------------------------
# Capability tiers -- a recognizer declares the MINIMUM front-end resolution it needs to be HONEST.
# Ordered so `tree.capability >= recognizer.requires` is the dispatch gate (hard-part #1).
# ---------------------------------------------------------------------------
class FrontEndCapability(IntEnum):
    RAW_TEXT = 0           # line/regex over source text (TF jsonencode, heredoc dispatch)
    LEXICAL_AST = 1        # python `ast` -- coarse, single-file, no cross-file resolution
    RESOLVED_SEMANTIC = 2  # ts-morph TypeChecker.getSymbol -- cross-file RESOLVED edges


# ---------------------------------------------------------------------------
# Site -- one located lexical match a recognizer found; carries the file:line provenance the CSE needs.
# ---------------------------------------------------------------------------
@dataclass
class Site:
    source: str                                  # repo-relative file
    locus: str                                   # "L{n}" or "L{a}-{b}"
    evidence: str                                # the LITERAL bytes at that locus (comp_ladder C0 style)
    payload: dict = field(default_factory=dict)  # recognizer-local extracted data


# ---------------------------------------------------------------------------
# Coverage -- the no-silent-Unknown channel (hard-part #5 / decision #3). EVERY recognize() returns one,
# so a weak recognizer cannot silently under-report while the parity gate passes. Adopts compiler #2's model.
# ---------------------------------------------------------------------------
@dataclass
class Coverage:
    attempted: int = 0
    resolved: int = 0
    unresolved: list = field(default_factory=list)   # [(locus, reason)] -- never a silent drop

    def merge(self, other: "Coverage") -> "Coverage":
        self.attempted += other.attempted
        self.resolved += other.resolved
        self.unresolved.extend(other.unresolved)
        return self


# COLLAPSE-DETECTOR (CTO decision #3, the third mandated coverage arm): a recognizer that suddenly resolves
# FAR FEWER sites than its baseline = a silent regression (a parser broke, a source moved) even though the
# CSEs it DID emit still pass fidelity + parity. Parity only checks emitted edges; this catches the ones
# silently dropped. Flags when resolved < baseline * threshold (default half).
def detect_collapse(current: "Coverage", baseline_resolved: int, threshold: float = 0.5) -> tuple:
    """Return (collapsed: bool, detail). No baseline (0/None) -> never collapsed (first run establishes it)."""
    if not baseline_resolved:
        return (False, "no baseline (first run)")
    if current.resolved < baseline_resolved * threshold:
        return (True, f"COLLAPSE: resolved {current.resolved} < {threshold:.0%} of baseline "
                      f"{baseline_resolved} -- a recognizer silently stopped resolving (regression)")
    return (False, f"ok: resolved {current.resolved} vs baseline {baseline_resolved}")


# ---------------------------------------------------------------------------
# EnrichedTree -- a normalized parsed artifact from a front-end, carrying its capability tier + the raw
# text (for locus computation). `root` is the front-end's representation (ast.Module | text | ts handle).
# ---------------------------------------------------------------------------
@dataclass
class EnrichedTree:
    source: str
    capability: FrontEndCapability
    text: str = ""
    root: object = None
    meta: dict = field(default_factory=dict)     # front-end extras (e.g. changed-set, project handle)


class FrontEnd(ABC):
    """A capability-tiered enriched-tree provider. Two lifecycles (hard-part #2): 'per-artifact'
    (compiler #1 -- parse each file/TF, then authoritative-map assembly) and 'whole-project'
    (compiler #2 -- persistent ts-morph Project + incremental 1-level dependent closure). The registry
    iterates build_trees(scope); incrementality (the changed-set) is the front-end's concern."""

    capability: FrontEndCapability = FrontEndCapability.RAW_TEXT
    lifecycle: str = "per-artifact"

    @abstractmethod
    def build_trees(self, scope) -> Iterable[EnrichedTree]:
        ...


# ---------------------------------------------------------------------------
# Locus helper (the provenance UPLIFT for compiler #1 -- its Node has file_path+sha but NO line; the CSE
# contract needs file:line). Template = extract_iam's content[:pos].count("\n")+1. Recognizers call this
# in iter_sites so every Site carries a real locus.
# ---------------------------------------------------------------------------
def locus_at(text: str, char_pos: int) -> str:
    """1-based line number at a character offset -> 'L{n}'. The compiler-#1 provenance uplift primitive."""
    return f"L{text[:max(0, char_pos)].count(chr(10)) + 1}"


def locus_span(text: str, start: int, end: int) -> str:
    a = text[:max(0, start)].count(chr(10)) + 1
    b = text[:max(0, end)].count(chr(10)) + 1
    return f"L{a}" if a == b else f"L{a}-{b}"


# ---------------------------------------------------------------------------
# emit_cse -- the ONE way to produce a CSE. validate_or_raise means a recognizer physically cannot emit an
# invalid (off-enum / provenance-less / non-decompressible) CSE. event_id is DETERMINISTIC (a hash of the
# provenance + subject) so re-running a recognizer over unchanged source yields the same id (parity-stable).
# ---------------------------------------------------------------------------
def emit_cse(*, verb: str, subject: EntityRef, edges: list, provenance: Provenance,
             confidence: float, marker_head: str, producer_kind: str, compiler_id: str,
             artifact_class: str, timestamp: str = "", actor: str = "", run_id: str = "",
             scope: str = "", extra_qualifiers: dict | None = None) -> CSE:
    """Build + fail-closed-validate one CSE. edges = list[RelationshipDelta]. Off-enum values must already
    be honest-degraded by the caller (subject=Concept(untyped)+low) -- validate_or_raise enforces it."""
    ev_seed = f"{provenance.source}|{provenance.locus}|{provenance.recognizer}|{subject.etype}|{subject.ref}"
    event_id = hashlib.sha1(ev_seed.encode("utf-8")).hexdigest()[:16]  # deterministic, reproducible
    quals = {Qualifier.CONFIDENCE.value: confidence}
    if scope:
        quals[Qualifier.SCOPE.value] = scope
    if extra_qualifiers:
        quals.update(extra_qualifiers)
    cse_obj = CSE(
        event_id=event_id,
        schema_version=SCHEMA_VERSION,
        producer={"kind": producer_kind, "ref": provenance.source},
        compiler={"id": compiler_id, "artifact_class": artifact_class, "version": "p1"},
        transformation={"verb": verb, "subject": subject, "edges": edges or []},
        provenance=provenance,
        execution_meta={"timestamp": timestamp, "actor": actor, "run_id": run_id},
        head={"marker_head": marker_head},
        qualifiers=quals,
    )
    validate_or_raise(cse_obj)   # fail-closed: off-enum/provenance-less/non-decompressible -> raise
    return cse_obj


# ---------------------------------------------------------------------------
# Recognizer base -- DS~A subclasses this. She implements iter_sites() + emit(); the SDK owns recognize()
# (capability-gating + LAW-1 honest-degrade + coverage). This is the interface handed off for the build.
# ---------------------------------------------------------------------------
class Recognizer(ABC):
    artifact_class: str = ""
    concept: str = ""
    requires: FrontEndCapability = FrontEndCapability.RAW_TEXT

    # the emitting compiler id + producer kind (a recognizer is authored for one compiler)
    compiler_id: str = "compilerkit"
    producer_kind: str = ProducerKind.INFRA.value

    # emits: the CSE algebra primitive VALUES this recognizer declares it can emit -- a tuple of
    # Entity/Relationship/EdgeKind values (e.g. (Entity.FIELD.value, Relationship.FLOWS_TO.value)). This is
    # the SDK-DECLARED source that replaces a hand-maintained coverage-sweep compiler_emits() (NFRA_CSE.P2
    # seam, DS~B): derive_compiler_emits() reads these declarations so the sweep is drift-proof + auto-current
    # as producers are SDK-refactored. Entity.CONCEPT is NOT listed here -- every recognizer emits it BY
    # CONSTRUCTION (the LAW-1 honest-degrade target), so derive_compiler_emits() adds it for every compiler.
    # A declaration must be TRUE: a recognizer declaring an emit it cannot actually produce is exactly the
    # I1/I3 dishonesty comp-honesty flags -- so an emits value must correspond to a real emit path.
    emits: tuple = ()

    @abstractmethod
    def iter_sites(self, tree: EnrichedTree) -> Iterable[Site]:
        """Yield each located lexical match as a Site (source, locus=file:line, evidence=literal bytes)."""

    @abstractmethod
    def emit(self, site: Site, tree: EnrichedTree, *, marker_head: str) -> list:
        """Emit CSE(s) for a site via emit_cse: a C0 typed Entity subject + C1 Relationship edges, each
        with file:line provenance. Pass `marker_head` straight into emit_cse (it is the GLOBGRPH marker-HEAD
        at emission -- required per AC6; the SDK threads it here so emit() never has to source it). Off-enum
        -> degrade() (LAW 1), NEVER a guess. Return [] if the site does not resolve (the SDK records it as
        unresolved -- honest, not silent)."""

    def degrade(self, site: Site, *, marker_head: str) -> CSE:
        """LAW-1 honest-degrade: an unrecognizable/under-resolved site becomes Concept(untyped)+low, never
        a downgraded guess. Still fully provenance-bound (decompresses to the lexical site)."""
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept,
                          evidence=site.evidence or "(degraded: no lexical evidence captured)")
        return emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.CONCEPT.value, f"concept:{self.concept}@{site.source}:{site.locus}"),
            edges=[], provenance=prov, confidence=LOW_CONFIDENCE_MAX,
            marker_head=marker_head, producer_kind=self.producer_kind,
            compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )

    def recognize(self, tree: EnrichedTree, *, marker_head: str) -> tuple:
        """THE SDK-owned entry: capability-gate + honest-degrade + coverage. Returns (list[CSE], Coverage)."""
        cov = Coverage()
        out: list = []
        for site in self.iter_sites(tree):
            cov.attempted += 1
            if tree.capability < self.requires:
                out.append(self.degrade(site, marker_head=marker_head))
                cov.unresolved.append((site.locus, f"capability {tree.capability.name} < requires "
                                                    f"{self.requires.name} (honest-degrade)"))
                continue
            cses = self.emit(site, tree, marker_head=marker_head)
            if cses:
                cov.resolved += 1
                out.extend(cses)
            else:
                cov.unresolved.append((site.locus, "emit returned no CSE (unresolved, not silent)"))
        return out, cov


# ---------------------------------------------------------------------------
# RecognizerRegistry -- hot-reloadable, keyed (artifact_class, concept).
# THE PROMOTE-SEAM (CTO decision #2, ruled 2026-07-07): this registry is the COMPILERKIT side of the seam
# to NFRA_PROMOTE (the semantic-plane promotion/DIRECTIVE engine -- NOT COMPROUTE's TH-C, a different
# promotion). When NFRA_PROMOTE materializes a promoted recognizer (a MOTIF pattern promoted to a
# first-class recognizer), the LIVE compiler picks it up via this hot-reload registry WITHOUT a redeploy.
# COMPILERKIT owns the registry (consumer) side; NFRA_PROMOTE owns the materializer (producer) side.
# ADD-ON (also CTO-ruled): the hot-register entrypoint is a NAMED critical-surface (comp-surface-check +
# /seams) so a silent no-op registration (a promoted recognizer that fails to take) is CAUGHT -- "a
# control must fire when exercised" applied to hot-registration. The on_register hook surfaces every add.
# ---------------------------------------------------------------------------
PROMOTE_SEAM = "compilerkit.recognizer.hot_register"   # registry <-> NFRA_PROMOTE-materializer; surfaced


class RecognizerRegistry:
    def __init__(self, on_register=None):
        self._by_key: dict = {}
        self._on_register = on_register   # the PROMOTE-seam surfacing hook (decision #2)

    def register(self, r: Recognizer) -> None:
        key = (r.artifact_class, r.concept)
        if key in self._by_key:
            raise ValueError(f"recognizer {key} already registered (dup -- hot-reload replaces via reload())")
        self._by_key[key] = r
        if self._on_register:                          # PROMOTE-seam: surface the registration (no silent add)
            self._on_register(PROMOTE_SEAM, r.artifact_class, r.concept)

    def reload(self, r: Recognizer) -> None:
        """Hot-reload: replace an existing (artifact_class, concept) without restart (CVO gap #8)."""
        self._by_key[(r.artifact_class, r.concept)] = r
        if self._on_register:
            self._on_register(PROMOTE_SEAM + ".reload", r.artifact_class, r.concept)

    def deregister(self, artifact_class: str, concept: str) -> None:
        """Hot-de-register (NFRA_SEMCTL.GOV-B req#3 -- reversibility): remove a promoted recognizer
        without restart. Fail-loud on a missing key (never a silent no-op -- a de-register call that
        targeted the wrong key must be visible, not swallowed) and surface the removal through the SAME
        PROMOTE-seam hook as register()/reload() (no silent remove, mirroring no silent add)."""
        key = (artifact_class, concept)
        if key not in self._by_key:
            raise KeyError(f"recognizer {key} not registered -- cannot de-register what isn't live")
        del self._by_key[key]
        if self._on_register:
            self._on_register(PROMOTE_SEAM + ".deregister", artifact_class, concept)

    def recognizers_for(self, artifact_class: str, capability: FrontEndCapability) -> list:
        """Capability-matched dispatch set: recognizers for this artifact_class whose requires <= capability.
        A recognizer needing more resolution than the tree offers is NOT dispatched here -- it would only
        honest-degrade (that path is exercised when a recognizer runs on a lower-tier tree deliberately)."""
        return [r for (ac, _), r in self._by_key.items()
                if ac == artifact_class and r.requires <= capability]

    def all(self) -> list:
        return list(self._by_key.values())


# ---------------------------------------------------------------------------
# Parity-oracle harness (AC2) -- run a front-end's trees through its recognizers, collect CSEs + coverage.
# Full parity = materialize the CSEs to CloudNode/CloudEdge and structurally diff vs the CURRENT graph
# (needs a live-graph export -- the diff half is the next build slice; cse_schema.parity_check proves the
# MAPPING-totality precondition here). P1 scope = in-memory materialize+diff, NOT a persistent writer (#4).
# ---------------------------------------------------------------------------
def run_recognizers(registry: RecognizerRegistry, front_end: FrontEnd, scope, *, marker_head: str) -> dict:
    """Run every capability-matched recognizer over the front-end's trees. Returns
    {cses: [...], coverage: Coverage, n_trees: int}. Deterministic + side-effect-free (advisory emit)."""
    all_cses: list = []
    cov = Coverage()
    n = 0
    for tree in front_end.build_trees(scope):
        n += 1
        for r in registry.recognizers_for(front_end.artifact_class if hasattr(front_end, "artifact_class")
                                           else "", tree.capability):
            cses, c = r.recognize(tree, marker_head=marker_head)
            all_cses.extend(cses)
            cov.merge(c)
    return {"cses": all_cses, "coverage": cov, "n_trees": n}


# ---------------------------------------------------------------------------
# derive_compiler_emits -- the SDK-DECLARED replacement for a hand-maintained coverage-sweep compiler_emits()
# (NFRA_CSE.P2 req#3 seam, DS~B). Reads each REGISTERED recognizer's `emits` declaration + compiler_id and
# produces {compiler_id: {entities, relationships, edge_kinds}} -- the exact shape the sweep consumes -- so
# the "which compiler emits which primitive" registry is derived from the framework, drift-proof + auto-
# current as producers are SDK-refactored (no second hand-maintained map). Entity.CONCEPT is added for every
# compiler (the LAW-1 honest-degrade target, emitted by construction). A declared value is classified into
# its family by enum membership. This is ADDITIVE over the sweep's estate-derivation: it covers the
# SDK-refactored compilers; a primitive whose only producer is not-yet-SDK-refactored stays the sweep's
# explicit attribution (e.g. Entity.SYMBOL -> the live extract_api extractor) until that producer is
# refactored + declares it here. That incremental replacement IS the seam-migration (DS~B line 112-113).
# ---------------------------------------------------------------------------
def derive_compiler_emits(registry: RecognizerRegistry) -> dict:
    out: dict = {}
    for r in registry.all():
        slot = out.setdefault(r.compiler_id, {"entities": set(), "relationships": set(), "edge_kinds": set()})
        slot["entities"].add(Entity.CONCEPT.value)   # honest-degrade target, emitted by construction
        for v in getattr(r, "emits", ()) or ():
            if v in cse._ENTITY_VALUES:
                slot["entities"].add(v)
            elif v in cse._REL_VALUES:
                slot["relationships"].add(v)
            elif v in getattr(cse, "_EDGEKIND_VALUES", frozenset()):
                slot["edge_kinds"].add(v)
            else:
                raise ValueError(f"recognizer {r.compiler_id}/{r.concept} declares emits value {v!r} that is "
                                 f"not a known Entity/Relationship/EdgeKind value (a false/typo'd declaration "
                                 f"-- the I1/I3 dishonesty the honesty bar forbids)")
    return out


# ---------------------------------------------------------------------------
# SELF-TEST -- proves the interface end-to-end on a sample lexical recognizer (the shape DS~A builds).
#   python comp_recognizer_sdk.py         # runs + prints every assertion; exit 0 iff all PASS.
# ---------------------------------------------------------------------------
class _SampleS3KeyConstRecognizer(Recognizer):
    """A minimal example of the DS~A shape: a LEXICAL_AST recognizer that recognizes an S3-key constant
    assignment and emits a C0 S3Bucket Entity with file:line provenance. Demonstrates the contract; the
    real compiler-#1 recognizers are DS~A-authored."""
    artifact_class = "python"
    concept = "s3-key-const"
    requires = FrontEndCapability.LEXICAL_AST
    compiler_id = "code-compiler"
    producer_kind = ProducerKind.INFRA.value
    emits = (Entity.S3BUCKET.value,)

    def iter_sites(self, tree: EnrichedTree):
        import re
        for m in re.finditer(r'([A-Z_]+)\s*=\s*"(s3://[^"]+)"', tree.text):
            yield Site(source=tree.source, locus=locus_at(tree.text, m.start()),
                       evidence=m.group(0), payload={"const": m.group(1), "uri": m.group(2)})

    def emit(self, site: Site, tree: EnrichedTree, *, marker_head: str):
        bucket = site.payload["uri"].split("://", 1)[1].split("/")[0]
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.S3BUCKET.value, f"s3:{bucket}"),
            edges=[], provenance=prov, confidence=1.0, marker_head=marker_head,
            producer_kind=self.producer_kind, compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )]


class _SampleResolvedRecognizer(Recognizer):
    """A RESOLVED_SEMANTIC recognizer -- used to prove capability-gating: run on a LEXICAL_AST tree it must
    honest-degrade to Concept(untyped)+low (LAW 1), never emit its typed claim."""
    artifact_class = "python"
    concept = "cross-file-flows-to"
    requires = FrontEndCapability.RESOLVED_SEMANTIC
    compiler_id = "code-compiler"
    emits = (Entity.FUNCTION.value, Relationship.FLOWS_TO.value)

    def iter_sites(self, tree: EnrichedTree):
        if "flows" in tree.text:
            yield Site(source=tree.source, locus="L1", evidence="flows", payload={})

    def emit(self, site, tree, *, marker_head: str):
        # would emit a FLOWS_TO edge if it had resolution; never reached on a low-tier tree
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        return [emit_cse(verb=Transformation.CREATE.value,
                         subject=EntityRef(Entity.FUNCTION.value, "fn:x"), edges=[], provenance=prov,
                         confidence=1.0, marker_head=marker_head, producer_kind=self.producer_kind,
                         compiler_id=self.compiler_id, artifact_class=self.artifact_class)]


class _FakeFrontEnd(FrontEnd):
    artifact_class = "python"
    capability = FrontEndCapability.LEXICAL_AST
    lifecycle = "per-artifact"

    def __init__(self, trees):
        self._trees = trees

    def build_trees(self, scope):
        return iter(self._trees)


def _self_test() -> bool:
    results = []

    def ck(name, cond, detail=""):
        results.append(bool(cond))
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"   ({detail})" if detail and not cond else ""))

    tree = EnrichedTree(source="lib/s3_layout.py", capability=FrontEndCapability.LEXICAL_AST,
                        text='GOLD_KEY = "s3://opal-data-bd/platinum/x.parquet"\nFOO = "s3://opal-data-inf/gold/y"\n')

    # 1. a lexical recognizer emits VALID, fidelity-passing CSEs with file:line provenance.
    r = _SampleS3KeyConstRecognizer()
    cses, cov = r.recognize(tree, marker_head="head1")
    ck("recognizer emits CSEs", len(cses) == 2, f"got {len(cses)}")
    ck("coverage recorded (no silent drop)", cov.attempted == 2 and cov.resolved == 2 and not cov.unresolved,
       f"attempted={cov.attempted} resolved={cov.resolved} unresolved={cov.unresolved}")
    fid_ok = all(cse.cse_fidelity_ok(c)[0] for c in cses)
    ck("every CSE decompresses to C0 lexical evidence (AC6 fidelity)", fid_ok)
    loci = {c.provenance.locus for c in cses}
    ck("provenance is file:line (uplift proven)", loci == {"L1", "L2"}, f"loci={loci}")
    ck("subject resolves to S3Bucket entity", all(
        c.transformation["subject"].etype == Entity.S3BUCKET.value for c in cses))

    # 2. emit_cse fail-closes an invalid CSE (off-enum verb) -- a recognizer cannot emit garbage.
    bad = False
    try:
        emit_cse(verb="frobnicate", subject=EntityRef(Entity.S3BUCKET.value, "s3:x"), edges=[],
                 provenance=Provenance("f", "L1", "t", "e"), confidence=1.0, marker_head="h",
                 producer_kind=ProducerKind.INFRA.value, compiler_id="c", artifact_class="python")
    except cse.CSEValidationError:
        bad = True
    ck("emit_cse fail-closes an off-enum verb (validate_or_raise)", bad)

    # 3. capability-gating: a RESOLVED_SEMANTIC recognizer on a LEXICAL_AST tree HONEST-DEGRADES (LAW 1).
    rr = _SampleResolvedRecognizer()
    dcses, dcov = rr.recognize(EnrichedTree(source="a.py", capability=FrontEndCapability.LEXICAL_AST,
                                            text="flows here"), marker_head="h")
    degraded = len(dcses) == 1 and dcses[0].transformation["subject"].etype == Entity.CONCEPT.value
    low = float(dcses[0].qualifiers[Qualifier.CONFIDENCE.value]) <= LOW_CONFIDENCE_MAX if dcses else False
    ck("under-capability recognizer honest-degrades to Concept+low (LAW 1)", degraded and low
       and len(dcov.unresolved) == 1, f"degraded={degraded} low={low} unresolved={dcov.unresolved}")

    # 4. registry: capability-matched dispatch + the PROMOTE-seam surfacing hook fires.
    surfaced = []
    reg = RecognizerRegistry(on_register=lambda seam, ac, cc: surfaced.append((seam, ac, cc)))
    reg.register(r)
    reg.register(rr)
    matched = reg.recognizers_for("python", FrontEndCapability.LEXICAL_AST)
    ck("registry dispatches only capability-matched recognizers", [x.concept for x in matched] == ["s3-key-const"],
       f"matched={[x.concept for x in matched]}")
    ck("PROMOTE-seam surfaced each registration (no silent add)",
       surfaced == [(PROMOTE_SEAM, "python", "s3-key-const"), (PROMOTE_SEAM, "python", "cross-file-flows-to")],
       f"surfaced={surfaced}")

    # 4b. reversibility (NFRA_SEMCTL.GOV-B req#3): a promoted recognizer can be hot-de-registered, and the
    # removal is surfaced through the same seam (no silent remove) -- proves a bad PROMOTE materialization
    # is reversible. A de-register of a key that isn't live fails LOUD (KeyError), never a silent no-op.
    reg.deregister("python", "s3-key-const")
    matched_after = reg.recognizers_for("python", FrontEndCapability.LEXICAL_AST)
    ck("de-registered recognizer is gone from dispatch (reversible promotion)",
       matched_after == [], f"matched_after={[x.concept for x in matched_after]}")
    ck("de-registration surfaced through the PROMOTE-seam (no silent remove)",
       surfaced[-1] == (PROMOTE_SEAM + ".deregister", "python", "s3-key-const"), f"surfaced={surfaced}")
    degregister_failed_loud = False
    try:
        reg.deregister("python", "not-a-real-concept")
    except KeyError:
        degregister_failed_loud = True
    ck("de-registering an unregistered key fails LOUD, not a silent no-op", degregister_failed_loud)
    reg.register(r)   # restore for the harness step below

    # 5. run_recognizers harness over a front-end.
    out = run_recognizers(reg, _FakeFrontEnd([tree]), scope=None, marker_head="head1")
    ck("harness runs recognizers over front-end trees", len(out["cses"]) == 2 and out["n_trees"] == 1,
       f"cses={len(out['cses'])} trees={out['n_trees']}")

    # 6. collapse-detector (coverage arm 3): a resolved-count far below baseline flags a silent regression.
    collapsed, _d = detect_collapse(Coverage(attempted=10, resolved=2), baseline_resolved=10)
    healthy, _d2 = detect_collapse(Coverage(attempted=10, resolved=9), baseline_resolved=10)
    first, _d3 = detect_collapse(Coverage(attempted=10, resolved=2), baseline_resolved=0)
    ck("collapse-detector flags a silent resolve-drop, not a healthy run / first run",
       collapsed and not healthy and not first, f"collapsed={collapsed} healthy={healthy} first={first}")

    # 7. derive_compiler_emits (NFRA_CSE.P2 seam): SDK-declared `emits` -> the {cid:{entities,relationships,
    # edge_kinds}} shape the coverage-sweep consumes, drift-proof (reads Recognizer.emits, not a hand map);
    # CONCEPT added for every compiler (the honest-degrade target). reg has r (emits S3BUCKET) + rr (emits
    # FUNCTION + FLOWS_TO), both code-compiler.
    emap = derive_compiler_emits(reg)
    cc = emap.get("code-compiler", {})
    ck("derive_compiler_emits: SDK-declared emits -> coverage-sweep seam shape (drift-proof, +CONCEPT)",
       cc.get("entities") == {Entity.S3BUCKET.value, Entity.FUNCTION.value, Entity.CONCEPT.value}
       and cc.get("relationships") == {Relationship.FLOWS_TO.value} and cc.get("edge_kinds") == set(),
       f"code-compiler emits={cc}")
    bad_emit = False
    try:
        class _BadEmit(_SampleS3KeyConstRecognizer):
            emits = ("NotAPrimitive",)
        breg = RecognizerRegistry()
        breg.register(_BadEmit())
        derive_compiler_emits(breg)
    except ValueError:
        bad_emit = True
    ck("derive_compiler_emits REJECTS a false/typo'd emits declaration (I1/I3 honesty on the declaration)",
       bad_emit)

    passed = sum(1 for x in results if x)
    print(f"\n=== comp_recognizer_sdk self-test: {passed}/{len(results)} PASS ===")
    return passed == len(results)


if __name__ == "__main__":
    sys.exit(0 if _self_test() else 1)
