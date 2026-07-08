"""comp_recognizers_tsx -- NFRA_COMPILERKIT-P1: compiler #2 (TSGRAPH frontend-TSX extractor) migrated onto
the shared Recognizer SDK. The SECOND half of the parity-oracle PAIR (comp_recognizers_code.py is the
first). Author-DS (0.4.0_DS_ClientPlatform~A, the FlowsToRecognizer) / front-end+wire+parity-AE
(0.8.0_AE_CloudComp~D, this canonical module). Pure-lexical-over-resolved-output (CTO #3): the ts-morph
TypeChecker.getSymbol RESOLUTION is compiler #2's front-end (extractor_full.ts, a RESOLVED_SEMANTIC-tier
producer); this module maps that already-resolved FLOWS_TO output onto the CSE IR + routes it through the
SDK harness, and proves the field-grain lineage survives the generalization (AC2, 961/961).

WHY THIS IS THE "FULL SDK MIGRATION" (P1 objective "refactor compiler #2 onto the SDK", the not-started
project-JSON item): batch-1/2 (compiler #1) already run through the SDK via comp_recognizers_code.py. This
lands the symmetric compiler-#2 path -- a FrontEnd (TsxFlowsToFrontEnd, the whole-project lifecycle
hard-part #2) + the recognizer registered into a live RecognizerRegistry + parity routed through the SDK's
run_recognizers() harness -- so the parity-oracle PAIR is SYMMETRIC and SDK-routed: two distinct artifact
classes (backend/infra bash+python #1, frontend TSX field-lineage #2) reconciled onto ONE framework, each
reproducing its current C1. That symmetry IS the AC2 "the pipeline generalizes across classes" proof.

THE LOAD-BEARING NORMALIZATION (DS~A grounding-catch, ~D-ruled 2026-07-07 to HOLD at this seam): the
extractor emits the kind literal "recompute/guarded" (SLASH); cse_schema 0.2 EdgeKind.RECOMPUTE_GUARDED is
"recompute_guarded" (UNDERSCORE) and the validator REJECTS off-EdgeKind (LAW 1). 482/961 real edges (50%)
would fail-closed without the _KIND_MAP slash->underscore normalization. Ruling: normalize HERE (the
recognizer IS the impedance boundary compiler#2-output <-> CSE IR), NOT at extractor_full.ts:373 -- that
producer is live + CTO-parity-signed; mutating it is live blast-radius for zero functional gain. Unknown
kind literals honest-degrade to Concept(untyped)+low (LAW 1) + the SDK collapse-detector flags a mass-drop,
so a future extractor label change surfaces explicitly rather than silently mis-mapping.

NO FIRM-SCOPING here (unlike compiler #1): tsx refs are `type:portal/<path>#<Type>#<field>` -- the full
file path is already in the ref, portal is a single codebase, so there is no cross-firm basename collision
the way bd/cot gold scripts collide. Firm-scoping is a compiler-#1 concern only.

Design: org/tier2_senior/0.8.0_AE_CloudComp/deliverables/NFRA_COMPILERKIT/COMPILERKIT-P1-FRAMEWORK-DESIGN.md
Recognizer origin: deliverables/COMPILERKIT_recognizer_flowsto.py (cc983b78a) -- re-homed canonical here,
mirroring how comp_recognizers_code.py re-homed batch-1/2 from their deliverables drafts.
Author: 0.8.0_AE_CloudComp~D (NFRA_COMPILERKIT.P1, framework-lead). 2026-07-07.
"""

from __future__ import annotations

import json
import os
import re
import sys
from typing import Iterable

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from comp_recognizer_sdk import (  # noqa: E402
    Recognizer, RecognizerRegistry, FrontEnd, emit_cse, Site, EnrichedTree, EntityRef, RelationshipDelta,
    Provenance, Entity, Relationship, Transformation, FrontEndCapability, run_recognizers,
)
from cse_schema import EdgeKind  # noqa: E402

# The canonical resolved-output artifact compiler #2's front-end (extractor_full.ts, ts-morph PASS-6)
# produces. For the parity-oracle this IS the "current C1" to reproduce -- the already-resolved 961-edge
# FLOWS_TO field-lineage set. Repo-relative so provenance + the runner resolve regardless of CWD.
LIVE_FLOWSTO_REL = "org/modules/graph/tsgraph_spike/out/live_flowsto.json"

# compiler-#2 kind literal -> governed EdgeKind value. The "recompute/guarded"->"recompute_guarded" entry
# is the load-bearing slash->underscore normalization (482/961 real edges depend on it). Single seam.
_KIND_MAP = {
    "passthrough": EdgeKind.PASSTHROUGH.value,
    "rename": EdgeKind.RENAME.value,
    "recompute/guarded": EdgeKind.RECOMPUTE_GUARDED.value,
}

# "via" carries the mapping-site provenance: e.g. "mapping portal/src/components/Foo.tsx:354".
_VIA_RE = re.compile(r"mapping\s+(?P<file>\S+):(?P<line>\d+)\s*$")


class FlowsToRecognizer(Recognizer):
    """Consumes compiler #2's emitted FLOWS_TO edges (extractor_full.ts PASS-6 output, the live_flowsto.json
    shape) and emits one CSE per edge: subject = source Field, edge = FLOWS_TO -> dst Field carrying the
    governed EdgeKind + the (optional) lexical guard condition. RESOLVED_SEMANTIC tier -- the getSymbol
    cross-file field resolution was done by the ts-morph front-end; this recognizer maps its resolved
    output, it does not re-resolve. A kind literal outside _KIND_MAP honest-degrades (LAW 1)."""

    artifact_class = "tsx"
    concept = "field-flows-to"
    requires = FrontEndCapability.RESOLVED_SEMANTIC
    compiler_id = "tsx-compiler"
    emits = (Entity.FIELD.value, Relationship.FLOWS_TO.value,
             EdgeKind.PASSTHROUGH.value, EdgeKind.RENAME.value, EdgeKind.RECOMPUTE_GUARDED.value)

    def iter_sites(self, tree: EnrichedTree) -> Iterable[Site]:
        # front-end delivers the resolved FLOWS_TO edges via meta["flowsto_edges"] (list of the
        # {src, dst, props} dicts) -- the whole-project ts-morph lifecycle (hard-part #2) already ran.
        for edge in tree.meta.get("flowsto_edges", []):
            props = edge.get("props")
            props = json.loads(props) if isinstance(props, str) else (props or {})
            # locus/source from the mapping-site "via" (real file:line); fall back to the tree source.
            m = _VIA_RE.search(props.get("via", "") or "")
            source = m.group("file") if m else tree.source
            locus = f"L{m.group('line')}" if m else "L0"
            yield Site(source=source, locus=locus,
                       evidence=f"{props.get('srcField', edge.get('src'))} "
                                f"-FLOWS_TO({props.get('kind')})-> {props.get('dstField', edge.get('dst'))}",
                       payload={"src": edge.get("src"), "dst": edge.get("dst"),
                                "kind": props.get("kind"), "condition": props.get("condition") or ""})

    def emit(self, site: Site, tree: EnrichedTree, *, marker_head: str) -> list:
        mapped = _KIND_MAP.get(site.payload["kind"])
        if mapped is None:
            # unknown compiler-#2 kind literal -> LAW 1 honest-degrade, never a guessed EdgeKind.
            return [self.degrade(site, marker_head=marker_head)]
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.FIELD.value, site.payload["src"]),
            edges=[RelationshipDelta(Relationship.FLOWS_TO.value,
                                     EntityRef(Entity.FIELD.value, site.payload["dst"]),
                                     kind=mapped, condition=site.payload["condition"])],
            provenance=prov, confidence=1.0, marker_head=marker_head,
            producer_kind=self.producer_kind, compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )]


class TypeDeclRecognizer(Recognizer):
    """0.3 TYPE emission (cse_schema 0.3, Entity.TYPE first-class; 42b569a52). Emits one Entity.TYPE node per
    distinct DECLARING type in compiler #2's resolved FLOWS_TO field refs -- a `type:file#Type#field` field
    ref decomposes to the declaring `type:file#Type`, which is a first-class TYPE in 0.3. Each TYPE node
    CONTAINS-> the fields it declares (the field refs that appear in real FLOWS_TO edges), so the graph gets
    Type -CONTAINS-> Field -FLOWS_TO-> Field -- a coherent field-lineage. GROUNDED: every emitted TYPE appears
    as the declaring scope of a field in a REAL FLOWS_TO edge, with the real via file:line as provenance.

    NO Entity.SYMBOL here (LAW 1): live_flowsto.json carries ZERO symbol: refs (only type:/out:), so any SYMBOL
    claim from this artifact would be a guess. symbol:->Entity.SYMBOL is a code-extractor (extract_api) concern
    outside the TSX FLOWS_TO artifact -- surfaced to COO/DS~B as a coverage boundary, never fake-emitted.

    Additive + orthogonal: this does NOT touch the certified FLOWS_TO parity oracle (parity_run_tsx registers
    ONLY FlowsToRecognizer). It is the 0.3-governance follow-on so DS~B's req#3 coverage-sweep clears TYPE."""

    artifact_class = "tsx"
    concept = "tsx-type-decl"
    requires = FrontEndCapability.RESOLVED_SEMANTIC
    compiler_id = "tsx-compiler"
    emits = (Entity.TYPE.value, Entity.FIELD.value, Relationship.CONTAINS.value)

    def iter_sites(self, tree: EnrichedTree) -> Iterable[Site]:
        by_type: dict = {}
        for edge in tree.meta.get("flowsto_edges", []):
            props = edge.get("props")
            props = json.loads(props) if isinstance(props, str) else (props or {})
            m = _VIA_RE.search(props.get("via", "") or "")
            for ref in (edge.get("src"), edge.get("dst")):
                if not ref or not ref.startswith("type:") or ref.count("#") < 2:
                    continue
                decl = "#".join(ref.split("#")[:2])   # type:file#Type -- the declaring TYPE
                rec = by_type.setdefault(decl, {"fields": set(), "via": None})
                rec["fields"].add(ref)
                if rec["via"] is None and m:
                    rec["via"] = (m.group("file"), m.group("line"))
        for decl, rec in by_type.items():
            tname = decl.split("#")[-1]
            file = decl.split(":", 1)[1].split("#")[0]
            src, loc = (rec["via"][0], f"L{rec['via'][1]}") if rec["via"] else (file, "L0")
            yield Site(source=src, locus=loc,
                       evidence=f"type {tname} (declares {len(rec['fields'])} field(s) in the TSX FLOWS_TO lineage)",
                       payload={"decl": decl, "fields": sorted(rec["fields"])})

    def emit(self, site: Site, tree: EnrichedTree, *, marker_head: str) -> list:
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        edges = [RelationshipDelta(Relationship.CONTAINS.value, EntityRef(Entity.FIELD.value, f))
                 for f in site.payload["fields"]]
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.TYPE.value, site.payload["decl"]),
            edges=edges, provenance=prov, confidence=1.0, marker_head=marker_head,
            producer_kind=self.producer_kind, compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )]


class TsxFlowsToFrontEnd(FrontEnd):
    """Compiler #2's front-end, whole-project lifecycle (SDK hard-part #2). In production the persistent
    ts-morph Project resolves TSX field flows via TypeChecker.getSymbol and emits the FLOWS_TO edge set;
    for the parity-oracle that resolution is ALREADY done + persisted as live_flowsto.json, so this
    front-end loads that resolved artifact and presents it as ONE RESOLVED_SEMANTIC EnrichedTree carrying
    meta['flowsto_edges']. The ts-morph resolution stays in extractor_full.ts (owned by 0.8.0~D); this is
    the SDK boundary that hands its resolved output to the registry -- exactly the per-artifact vs
    whole-project split the FrontEnd ABC models."""

    artifact_class = "tsx"
    capability = FrontEndCapability.RESOLVED_SEMANTIC
    lifecycle = "whole-project"

    def __init__(self, flowsto_path: str = "") -> None:
        self._path = flowsto_path or os.path.join(_ws_root(), LIVE_FLOWSTO_REL)

    def build_trees(self, scope) -> Iterable[EnrichedTree]:
        # scope may override the resolved-output path (e.g. an incremental re-extract); default = live.
        path = scope if (isinstance(scope, str) and scope) else self._path
        with open(path, encoding="utf-8") as fh:
            edges = json.load(fh)
        yield EnrichedTree(source=LIVE_FLOWSTO_REL, capability=self.capability,
                           meta={"flowsto_edges": edges})


def _ws_root() -> str:
    return os.path.abspath(os.path.join(_HERE, "..", "..", ".."))


TSX_RECOGNIZERS = [FlowsToRecognizer, TypeDeclRecognizer]   # TypeDecl added for 0.3 TYPE emission (additive)


def register_all(registry: RecognizerRegistry) -> None:
    """Wire compiler #2's recognizers into a registry (the SDK hot-register seam) -- the FULL TSX compiler
    (FLOWS_TO field-lineage + 0.3 TYPE declarations)."""
    for cls in TSX_RECOGNIZERS:
        registry.register(cls())


# ---------------------------------------------------------------------------
# AC2 parity-oracle -- compiler #2, SDK-ROUTED (through run_recognizers over the FrontEnd + registry).
# The STRUCTURAL reproduction proof: the multiset of (src, dst, mapped_kind) the input edges normalize to
# (via _KIND_MAP) must EQUAL the multiset of (subject.ref, target.ref, edge.kind) the emitted CSEs carry
# -- i.e. every input edge is reproduced 1:1 with the correct governed EdgeKind, nothing extra, nothing
# dropped. That is the "reproduces its current C1" bar for compiler #2 (AC2), not merely a count match.
# ---------------------------------------------------------------------------
def parity_run_tsx(marker_head: str = "parity", flowsto_path: str = "") -> dict:
    import collections
    import cse_schema as cse

    fe = TsxFlowsToFrontEnd(flowsto_path)
    reg = RecognizerRegistry()
    reg.register(FlowsToRecognizer())   # FLOWS_TO-ONLY: this is the CERTIFIED 961/961 oracle -- TypeDecl is
    # a separate additive capability (type_decl_run), never perturbing the closed FLOWS_TO structural proof.
    out = run_recognizers(reg, fe, scope=flowsto_path or None, marker_head=marker_head)
    cses, cov = out["cses"], out["coverage"]

    # ground-truth the INPUT edge set independently from the raw resolved artifact (not from the CSEs).
    path = flowsto_path or os.path.join(_ws_root(), LIVE_FLOWSTO_REL)
    with open(path, encoding="utf-8") as fh:
        raw = json.load(fh)
    expected = collections.Counter()
    src_kind_dist = collections.Counter()
    n_conditions_in = 0
    n_unknown_kind = 0
    for e in raw:
        props = e.get("props")
        props = json.loads(props) if isinstance(props, str) else (props or {})
        klit = props.get("kind")
        src_kind_dist[klit] += 1
        if props.get("condition"):
            n_conditions_in += 1
        mapped = _KIND_MAP.get(klit)
        if mapped is None:
            n_unknown_kind += 1
            continue   # a real unknown would honest-degrade (Concept), not appear in the FLOWS_TO multiset
        expected[(e.get("src"), e.get("dst"), mapped)] += 1

    # the emitted FLOWS_TO edge multiset (skip any degrade CSE -- a degrade has no FLOWS_TO edge).
    produced = collections.Counter()
    n_conditions_out = 0
    for c in cses:
        edges = c.transformation["edges"]
        if not edges or edges[0].rtype != Relationship.FLOWS_TO.value:
            continue
        ed = edges[0]
        produced[(c.transformation["subject"].ref, ed.target.ref, ed.kind)] += 1
        if ed.condition:
            n_conditions_out += 1

    all_fid = all(cse.cse_fidelity_ok(c)[0] for c in cses)
    out_kind_dist = collections.Counter(
        c.transformation["edges"][0].kind for c in cses
        if c.transformation["edges"] and c.transformation["edges"][0].rtype == Relationship.FLOWS_TO.value)

    return {
        "n_input_edges": len(raw),
        "n_cses": len(cses),
        "n_flowsto_edges": sum(produced.values()),
        "structural_parity": produced == expected,
        "only_input": list((expected - produced).elements()),
        "only_output": list((produced - expected).elements()),
        "src_kind_dist": dict(src_kind_dist),
        "out_kind_dist": dict(out_kind_dist),
        "n_conditions_in": n_conditions_in,
        "n_conditions_out": n_conditions_out,
        "n_unknown_kind_degraded": n_unknown_kind,
        "coverage_attempted": cov.attempted,
        "coverage_resolved": cov.resolved,
        "coverage_unresolved": len(cov.unresolved),
        "all_fidelity_ok": all_fid,
        "n_trees": out["n_trees"],
    }


def type_decl_run(marker_head: str = "types", flowsto_path: str = "") -> dict:
    """0.3 TYPE emission proof -- SDK-routed TypeDeclRecognizer over the resolved TSX artifact. Reports the
    Entity.TYPE nodes emitted (one per distinct declaring type), their CONTAINS->field edges, fidelity, and
    that every subject is Entity.TYPE + validates under schema 0.3. This is what clears DS~B's req#3
    coverage-sweep for TYPE from the TSX compiler. Separate registry from parity_run_tsx (never perturbs the
    certified FLOWS_TO oracle)."""
    import cse_schema as cse

    fe = TsxFlowsToFrontEnd(flowsto_path)
    reg = RecognizerRegistry()
    reg.register(TypeDeclRecognizer())
    out = run_recognizers(reg, fe, scope=flowsto_path or None, marker_head=marker_head)
    cses, cov = out["cses"], out["coverage"]
    return {
        "n_type_nodes": len(cses),
        "all_subject_is_TYPE": all(c.transformation["subject"].etype == Entity.TYPE.value for c in cses),
        "n_contains_edges": sum(len(c.transformation["edges"]) for c in cses),
        "all_fidelity_ok": all(cse.cse_fidelity_ok(c)[0] for c in cses),
        "schema_version": cse.SCHEMA_VERSION,
        "coverage_resolved": cov.resolved,
        "coverage_unresolved": len(cov.unresolved),
    }


if __name__ == "__main__":
    rep = parity_run_tsx()
    print("=== COMPILERKIT-P1 compiler #2 (TSGRAPH-TSX) AC2 parity-oracle -- SDK-routed ===")
    print(f"  front-end trees: {rep['n_trees']} (whole-project lifecycle)")
    print(f"  input FLOWS_TO edges (live_flowsto.json): {rep['n_input_edges']}")
    print(f"  emitted CSEs: {rep['n_cses']}  (FLOWS_TO edges: {rep['n_flowsto_edges']})")
    print(f"  kind distribution: in {rep['src_kind_dist']}  ->  out {rep['out_kind_dist']}")
    print(f"  guard conditions carried: in {rep['n_conditions_in']}  ->  out {rep['n_conditions_out']}")
    print(f"  coverage: attempted={rep['coverage_attempted']} resolved={rep['coverage_resolved']} "
          f"unresolved={rep['coverage_unresolved']} unknown-kind-degraded={rep['n_unknown_kind_degraded']}")
    print(f"  all_fidelity_ok: {rep['all_fidelity_ok']}")
    print(f"  STRUCTURAL PARITY (input edge multiset == output edge multiset): {rep['structural_parity']}")
    if not rep["structural_parity"]:
        print(f"    only-input (dropped): {len(rep['only_input'])}  only-output (spurious): {len(rep['only_output'])}")
        for t in rep["only_input"][:5]:
            print(f"      DROPPED: {t}")
        for t in rep["only_output"][:5]:
            print(f"      SPURIOUS: {t}")

    ok = (rep["structural_parity"] and rep["all_fidelity_ok"]
          and rep["n_flowsto_edges"] == rep["n_input_edges"] == 961
          and rep["coverage_unresolved"] == 0 and rep["coverage_resolved"] == 961
          and rep["n_conditions_out"] == rep["n_conditions_in"] == 23
          and rep["out_kind_dist"].get("recompute_guarded") == 482
          and "recompute/guarded" not in rep["out_kind_dist"])
    print(f"\n=== compiler #2 FLOWS_TO parity-oracle: {'PASS' if ok else 'FAIL'} "
          f"(961/961 field-flows reproduced onto the CSE IR through the SDK) ===")

    # 0.3 governance follow-on: Entity.TYPE emission (additive; does NOT touch the FLOWS_TO oracle above)
    trep = type_decl_run()
    print("\n=== COMPILERKIT compiler #2 -- 0.3 Entity.TYPE emission (TypeDeclRecognizer, SDK-routed) ===")
    print(f"  Entity.TYPE nodes emitted: {trep['n_type_nodes']}  (CONTAINS->field edges: {trep['n_contains_edges']})")
    print(f"  every subject is Entity.TYPE: {trep['all_subject_is_TYPE']} | schema_version: {trep['schema_version']}")
    print(f"  all_fidelity_ok: {trep['all_fidelity_ok']} | coverage resolved={trep['coverage_resolved']} "
          f"unresolved={trep['coverage_unresolved']}")
    print("  NOTE: NO Entity.SYMBOL emitted -- live_flowsto.json has zero symbol: refs (LAW 1, not faked); "
          "SYMBOL is a code-extractor concern surfaced to COO/DS~B, not fake-cleared here.")
    tok = (trep["n_type_nodes"] == 136 and trep["all_subject_is_TYPE"] and trep["all_fidelity_ok"]
           and trep["coverage_unresolved"] == 0 and trep["schema_version"] == "0.3")
    print(f"=== 0.3 TYPE emission: {'PASS' if tok else 'FAIL'} "
          f"(136 declaring types -> Entity.TYPE, CONTAINS->field, fidelity-clean, validates @0.3) ===")
    sys.exit(0 if (ok and tok) else 1)
