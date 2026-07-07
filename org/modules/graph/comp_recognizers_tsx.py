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


TSX_RECOGNIZERS = [FlowsToRecognizer]


def register_all(registry: RecognizerRegistry) -> None:
    """Wire compiler #2's recognizer(s) into a registry (the SDK hot-register seam)."""
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
    register_all(reg)
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
    print(f"\n=== compiler #2 parity-oracle: {'PASS' if ok else 'FAIL'} "
          f"(961/961 field-flows reproduced onto the CSE IR through the SDK) ===")
    sys.exit(0 if ok else 1)
