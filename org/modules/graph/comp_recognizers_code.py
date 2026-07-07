"""compilerkit_code_recognizers -- NFRA_COMPILERKIT-P1: compiler #1 (code/infra) recognizer set, on the
shared Recognizer SDK (comp_recognizer_sdk). Author-DS (0.4.0_DS_ClientPlatform~A) / commit+wire+parity-AE
(0.8.0_AE_CloudComp~D). Pure-lexical (CTO #3); each recognizer emits CSE C0+C1 with file:line provenance.

Batch-1 (the parity-critical DISPATCH pair -- one body closes the DEBTSCAN reachability FP-block AND is
compiler #1's dispatch recognizer):
  DispatchCatalogRecognizer -- gold-dispatch CATALOG heredoc (the D1-class): dispatch-runner TRIGGERS each
                               catalog gold script. AC2 parity target = today's dispatcher-TRIGGERS C1.
  MdpfDispatchRecognizer    -- MDPF EC2 stage-runner (run_step + *_SCRIPT vars); live-proven (e4eca6c36).

Adapted from DS~A's draft (deliverables/COMPILERKIT_recognizers_batch1.py) to the THREADED marker_head
contract (SDK fix 7af2db209): emit(site, tree, *, marker_head) -- recognize() threads it, no tree.meta hop.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from comp_recognizer_sdk import (  # noqa: E402
    Recognizer, RecognizerRegistry, emit_cse, Site, EnrichedTree, EntityRef, RelationshipDelta,
    Provenance, Entity, Relationship, Transformation, FrontEndCapability, locus_at,
)


class DispatchCatalogRecognizer(Recognizer):
    """Compiler #1 recognizer #2 -- the gold-dispatch CATALOG heredoc (the D1-class). A dispatch runner
    TRIGGERS each catalog-listed gold script. AC2 parity target = today's dispatcher-TRIGGERS-script C1."""

    artifact_class = "bash"
    concept = "gold-dispatch-catalog"
    requires = FrontEndCapability.RAW_TEXT
    compiler_id = "code-compiler"

    _CATALOG = re.compile(r"read -r -d '' CATALOG << 'CATALOG_END'(.*?)CATALOG_END", re.DOTALL)
    _ROW = re.compile(r"^\s*(\S+)\|(\S+\.py)\|", re.MULTILINE)   # ID|filename|flags

    def iter_sites(self, tree):
        cat = self._CATALOG.search(tree.text)
        if not cat:
            return
        body, base = cat.group(1), cat.start(1)
        for m in self._ROW.finditer(body):
            # locus at the ROW CONTENT (group-1 start), not m.start() -- `\s*` eats the leading newline so
            # m.start() would point at the prior line (DS~A verify-don't-trust off-by-one catch).
            yield Site(source=tree.source, locus=locus_at(tree.text, base + m.start(1)),
                       evidence=m.group(0).strip(),
                       payload={"script_id": m.group(1), "filename": m.group(2)})

    def emit(self, site, tree, *, marker_head):
        script = Path(site.payload["filename"]).stem
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.SERVICE.value, f"dispatch:{Path(site.source).stem}"),
            edges=[RelationshipDelta(Relationship.TRIGGERS.value,
                                     EntityRef(Entity.MODULE.value, f"gold:{script}"))],
            provenance=prov, confidence=1.0, marker_head=marker_head,
            producer_kind=self.producer_kind, compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )]


class MdpfDispatchRecognizer(Recognizer):
    """DEBTSCAN root-fix + COMPILERKIT #1 -- the MDPF EC2 stage-runner. `run_step LABEL <relpath>.py` + a few
    `*_SCRIPT="${SCRIPTS_DIR}/<relpath>.py"` vars. Live-proven (0.8.0 wired the parse e4eca6c36, 7 edged)."""

    artifact_class = "bash"
    concept = "mdpf-ec2-dispatch"
    requires = FrontEndCapability.RAW_TEXT
    compiler_id = "code-compiler"

    _RUN_STEP = re.compile(r"run_step\s+\S+\s+(\S+\.py)\b")
    _VAR = re.compile(r'\w+_SCRIPT="\$\{SCRIPTS_DIR\}/(\S+\.py)"')

    def iter_sites(self, tree):
        for pat in (self._RUN_STEP, self._VAR):
            for m in pat.finditer(tree.text):
                yield Site(source=tree.source, locus=locus_at(tree.text, m.start()),
                           evidence=m.group(0).strip(), payload={"relpath": m.group(1)})

    def emit(self, site, tree, *, marker_head):
        script = Path(site.payload["relpath"]).stem
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.SERVICE.value, "mdpf-daily-runner"),
            edges=[RelationshipDelta(Relationship.TRIGGERS.value,
                                     EntityRef(Entity.MODULE.value, f"gold:{script}"))],
            provenance=prov, confidence=1.0, marker_head=marker_head,
            producer_kind=self.producer_kind, compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )]


# The compiler-#1 recognizer set (batch-1). register_all() wires them into a registry (the SDK hot-register
# seam). More recognizers append here as DS~A lands them (S3-key-const, read/write-classifier, ...).
BATCH1 = [DispatchCatalogRecognizer, MdpfDispatchRecognizer]


def register_all(registry: RecognizerRegistry) -> None:
    for cls in BATCH1:
        registry.register(cls())


# ---------------------------------------------------------------------------
# AC2 parity runner -- run the recognizers over the REAL dispatch source + report the TRIGGERS edge set.
# This is the materialize half of the parity-oracle (recognizer -> CSE -> the dispatcher->gold-script edges).
# The full structural diff vs the LIVE extract_pipeline output is the next parity slice (needs the graph
# export); this proves the recognizers reproduce the dispatch C1 on REAL input, not synthetic self-test.
# ---------------------------------------------------------------------------
_REAL_SOURCES = {
    "gold-dispatch-catalog": [
        "data/inf/scripts/gold/orion-gold-dispatch.sh",
        "data/black_diamond/scripts/gold/gold_dispatch.sh",
        "data/cot/scripts/gold/gold_dispatch.sh",
    ],
    "mdpf-ec2-dispatch": ["infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh"],
}


def _edges_for(recognizer: Recognizer, rel_path: str, marker_head: str) -> tuple:
    ws = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
    ap = os.path.join(ws, rel_path)
    if not os.path.exists(ap):
        return ([], None)
    with open(ap, encoding="utf-8", errors="replace") as fh:
        text = fh.read()
    tree = EnrichedTree(source=rel_path, capability=FrontEndCapability.RAW_TEXT, text=text)
    cses, cov = recognizer.recognize(tree, marker_head=marker_head)
    edges = [(c.transformation["subject"].ref, c.transformation["edges"][0].target.ref, c.provenance.locus)
             for c in cses]
    return (edges, cov)


def parity_run(marker_head: str = "parity") -> dict:
    import cse_schema as cse
    report = {"recognizers": {}, "total_edges": 0, "all_fidelity_ok": True}
    for cls in BATCH1:
        r = cls()
        rec = {"sources": {}, "n_edges": 0, "fidelity_ok": True, "coverage_unresolved": 0}
        for src in _REAL_SOURCES.get(r.concept, []):
            edges, cov = _edges_for(r, src, marker_head)
            # re-run to fidelity-check the emitted CSEs
            ws = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
            ap = os.path.join(ws, src)
            fok = True
            if os.path.exists(ap):
                with open(ap, encoding="utf-8", errors="replace") as fh:
                    tree = EnrichedTree(source=src, capability=FrontEndCapability.RAW_TEXT, text=fh.read())
                cses, _ = r.recognize(tree, marker_head=marker_head)
                fok = all(cse.cse_fidelity_ok(c)[0] for c in cses)
            rec["sources"][src] = {"n_edges": len(edges), "edges": edges,
                                   "unresolved": (len(cov.unresolved) if cov else 0)}
            rec["n_edges"] += len(edges)
            rec["coverage_unresolved"] += (len(cov.unresolved) if cov else 0)
            rec["fidelity_ok"] = rec["fidelity_ok"] and fok
        report["recognizers"][r.concept] = rec
        report["total_edges"] += rec["n_edges"]
        report["all_fidelity_ok"] = report["all_fidelity_ok"] and rec["fidelity_ok"]
    return report


if __name__ == "__main__":
    rep = parity_run()
    print("=== COMPILERKIT-P1 batch-1 AC2 parity run (recognizers over REAL dispatch source) ===")
    for concept, rec in rep["recognizers"].items():
        print(f"\n  {concept}: {rec['n_edges']} TRIGGERS edges, fidelity_ok={rec['fidelity_ok']}, "
              f"unresolved={rec['coverage_unresolved']}")
        for src, s in rec["sources"].items():
            print(f"    {src}: {s['n_edges']} edges")
            for subj, tgt, loc in s["edges"][:6]:
                print(f"        {subj} --TRIGGERS--> {tgt}  @{loc}")
            if s["n_edges"] > 6:
                print(f"        ... +{s['n_edges'] - 6} more")
    print(f"\n  TOTAL: {rep['total_edges']} edges; all_fidelity_ok={rep['all_fidelity_ok']}")
    print("  NOTE: full structural diff vs the live extract_pipeline dispatch C1 = the next parity slice.")
    sys.exit(0 if rep["all_fidelity_ok"] and rep["total_edges"] > 0 else 1)
