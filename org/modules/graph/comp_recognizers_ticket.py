"""compilerkit_ticket_recognizers -- NFRA_COMPILERKIT-P3: the ticket compiler (org-intent -> code bridge),
on the shared Recognizer SDK (comp_recognizer_sdk). Author+wire+parity: 0.8.0_AE_CloudComp. Pure-lexical
(CTO #3, same as compiler #1/#2): no LLM interpretation of intent, only a deterministic lexical match.

Front-end: this estate's "ticket system" is the Task Order (TO) XML-in-markdown files under
org/tier1_exec/*/task_orders/*.md -- each carries one or more `<requirement id="N">...</requirement>`
blocks (the org-intent unit). RAW_TEXT capability (regex over the file text) is sufficient and honest --
no ast/ts-morph resolution needed for this front-end shape.

TicketRequirementImplementsRecognizer (PRD 4.3/AC5 -- the first cross-plane edge class):
  1. Emits a Requirement Entity per `<requirement id="N">` block, file:line provenance (source=TO path,
     locus=the requirement tag's line, evidence=the literal requirement text) -- this alone satisfies
     req#1's "recognizers emit Requirement entities" half regardless of whether a Component resolves.
  2. When the requirement text lexically names a real on-disk code artifact (a `.py`/`.sh`/`.yaml`/`.yml`/
     `.tsx`/`.ts` path-shaped token that a workspace-relative `os.path.exists` check CONFIRMS is real --
     never a guess, LAW 1), also emits a Requirement -[IMPLEMENTS]-> Component edge. req#3
     ("decompressible to lexical evidence on both ends"): the Requirement end decompresses via its own
     Provenance; the Component end decompresses because the matched literal substring is a real, existing
     path -- any reader can grep the exact bytes in Provenance.evidence AND stat the file. A requirement
     naming no real path emits the Requirement entity alone (edges=[]) -- honest under-resolution, not a
     silent drop (the SDK's coverage channel records it as unresolved).
"""

from __future__ import annotations

import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from comp_recognizer_sdk import (  # noqa: E402
    Recognizer, RecognizerRegistry, emit_cse, Site, EnrichedTree, EntityRef, RelationshipDelta,
    Provenance, Entity, Relationship, Transformation, FrontEndCapability, ProducerKind, locus_at,
)

_WS = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))

# A requirement names a real code artifact via a path-shaped token ending in one of these extensions.
# Deliberately excludes .md (a TO referencing another TO/doc is not a code Component per the PRD's
# org-to-CODE framing) and .json (config data, not a compiled artifact in this pass).
_COMPONENT_PATH_RE = re.compile(r'[\w./-]+\.(?:py|sh|ya?ml|tsx?)\b')

_REQUIREMENT_BLOCK_RE = re.compile(r'<requirement id="(\d+)">(.*?)</requirement>', re.DOTALL)


def _resolve_component_path(candidate: str, ticket_source: str) -> str | None:
    """A path-shaped token in requirement text is a real Component IFF it resolves to a real file --
    tried workspace-root-relative first (the common case, e.g. 'comp_recognizer_sdk.py' style bare
    basenames resolved via a repo-wide basename search would be a GUESS; we only accept it if the exact
    relative path exists), then relative to the ticket's own directory (a TO referencing a sibling file).
    Returns the workspace-relative path (str) if real, else None -- never invented."""
    for base in (_WS, os.path.dirname(os.path.join(_WS, ticket_source))):
        ap = os.path.join(base, candidate)
        if os.path.isfile(ap):
            return os.path.relpath(ap, _WS).replace("\\", "/")
    # bare-basename fallback: a requirement often names just the file (e.g. "comp_recognizer_sdk.py")
    # without its directory. A basename-only match is accepted ONLY if it is UNIQUE across the known
    # org/modules/graph + .tools trees (the estate's compiler/tool homes) -- an ambiguous basename is a
    # coverage gap (honest-degrade), never a coin-flip guess.
    base_name = os.path.basename(candidate)
    if base_name == candidate:  # only for bare basenames, not path-shaped candidates (those already tried above)
        hits = []
        for root_dir in (os.path.join(_WS, "org", "modules", "graph"), os.path.join(_WS, ".tools")):
            if not os.path.isdir(root_dir):
                continue
            for fn in os.listdir(root_dir):
                if fn == base_name:
                    hits.append(os.path.relpath(os.path.join(root_dir, fn), _WS).replace("\\", "/"))
        if len(hits) == 1:
            return hits[0]
    return None


class TicketRequirementImplementsRecognizer(Recognizer):
    """Compiler #3 (ticket compiler) recognizer #1 -- Requirement entities + the first org-to-code
    cross-plane edge class (Requirement -implements-> Component), per NFRA_COMPILERKIT PRD AC5."""

    artifact_class = "ticket"
    concept = "ticket-requirement-implements"
    requires = FrontEndCapability.RAW_TEXT
    compiler_id = "ticket-compiler"
    producer_kind = ProducerKind.TICKET.value

    def iter_sites(self, tree: EnrichedTree):
        for m in _REQUIREMENT_BLOCK_RE.finditer(tree.text):
            req_id, req_text = m.group(1), m.group(2)
            yield Site(
                source=tree.source,
                locus=locus_at(tree.text, m.start()),
                evidence=m.group(0).strip(),
                payload={"req_id": req_id, "req_text": req_text},
            )

    def emit(self, site: Site, tree: EnrichedTree, *, marker_head: str):
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        req_ref = EntityRef(Entity.REQUIREMENT.value, f"requirement:{site.source}#{site.payload['req_id']}")

        edges = []
        for candidate in _COMPONENT_PATH_RE.findall(site.payload["req_text"]):
            resolved = _resolve_component_path(candidate, site.source)
            if resolved:
                edges.append(RelationshipDelta(
                    rtype=Relationship.IMPLEMENTS.value,
                    target=EntityRef(Entity.COMPONENT.value, f"component:{resolved}"),
                ))
        # dedup (a requirement can mention the same real path twice)
        seen = set()
        uniq_edges = []
        for e in edges:
            if e.target.ref not in seen:
                seen.add(e.target.ref)
                uniq_edges.append(e)

        return [emit_cse(
            verb=Transformation.CREATE.value, subject=req_ref, edges=uniq_edges, provenance=prov,
            confidence=1.0 if uniq_edges else 0.5,  # a Requirement w/ no resolved Component is real but thin
            marker_head=marker_head, producer_kind=self.producer_kind,
            compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )]


BATCH1 = [TicketRequirementImplementsRecognizer]


def register_all(registry: RecognizerRegistry) -> None:
    for cls in BATCH1:
        registry.register(cls())


# ---------------------------------------------------------------------------
# AC5 parity/proof runner -- run the recognizer over REAL TO files (not synthetic self-test input) and
# report every emitted Requirement -implements-> Component edge, proving the first org-to-code cross-plane
# edge class on genuine org-intent content.
# ---------------------------------------------------------------------------
def _iter_real_to_files():
    root = os.path.join(_WS, "org", "tier1_exec")
    for dirpath, _dirnames, filenames in os.walk(root):
        if "task_orders" not in dirpath.replace("\\", "/").split("/"):
            continue
        for fn in filenames:
            if fn.endswith(".md"):
                yield os.path.relpath(os.path.join(dirpath, fn), _WS).replace("\\", "/")


def parity_run(marker_head: str = "parity") -> dict:
    import cse_schema as cse
    r = TicketRequirementImplementsRecognizer()
    report = {"n_to_files": 0, "n_requirements": 0, "n_implements_edges": 0, "all_fidelity_ok": True,
              "edges": []}
    for rel_path in sorted(_iter_real_to_files()):
        ap = os.path.join(_WS, rel_path)
        with open(ap, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        if "<requirement" not in text:
            continue
        report["n_to_files"] += 1
        tree = EnrichedTree(source=rel_path, capability=FrontEndCapability.RAW_TEXT, text=text)
        cses, _cov = r.recognize(tree, marker_head=marker_head)
        for c in cses:
            report["n_requirements"] += 1
            fok = c.cse_fidelity_ok(c)[0] if hasattr(c, "cse_fidelity_ok") else cse.cse_fidelity_ok(c)[0]
            report["all_fidelity_ok"] = report["all_fidelity_ok"] and fok
            for e in c.transformation["edges"]:
                report["n_implements_edges"] += 1
                report["edges"].append({
                    "requirement": c.transformation["subject"].ref,
                    "implements": e.target.ref,
                    "source": c.provenance.source,
                    "locus": c.provenance.locus,
                })
    return report


if __name__ == "__main__":
    import json
    rep = parity_run()
    print(json.dumps({k: v for k, v in rep.items() if k != "edges"}, indent=2))
    print(f"\n{len(rep['edges'])} Requirement-implements-Component edge(s) over "
          f"{rep['n_to_files']} real TO file(s) / {rep['n_requirements']} requirement(s):")
    for e in rep["edges"]:
        print(f"  {e['requirement']} -[IMPLEMENTS]-> {e['implements']}  ({e['source']}:{e['locus']})")
    ok = rep["all_fidelity_ok"] and rep["n_implements_edges"] > 0
    print(f"\n{'PASS' if ok else 'FAIL'}: AC5 (>=1 cross-plane edge, all fidelity-ok)")
    sys.exit(0 if ok else 1)
