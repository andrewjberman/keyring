"""compilerkit_code_recognizers -- NFRA_COMPILERKIT-P1: compiler #1 (code/infra) recognizer set, on the
shared Recognizer SDK (comp_recognizer_sdk). Author-DS (0.4.0_DS_ClientPlatform~A) / commit+wire+parity-AE
(0.8.0_AE_CloudComp~D). Pure-lexical (CTO #3); each recognizer emits CSE C0+C1 with file:line provenance.

Batch-1 (the parity-critical DISPATCH pair -- one body closes the DEBTSCAN reachability FP-block AND is
compiler #1's dispatch recognizer):
  DispatchCatalogRecognizer -- gold-dispatch CATALOG heredoc (the D1-class): dispatch-runner TRIGGERS each
                               catalog gold script. AC2 parity target = today's dispatcher-TRIGGERS C1.
  MdpfDispatchRecognizer    -- MDPF EC2 stage-runner (run_step + *_SCRIPT vars); live-proven (e4eca6c36).

Batch-2 (the S3-key pair, DS~A-authored, adapted from deliverables/COMPILERKIT_recognizers_batch2.py --
already built against this file's live SDK contract, no marker_head adaptation needed this time):
  S3KeyConstRecognizer      -- lib/s3_layout.py constant/key-function catalog (ast Assign+FunctionDef).
  S3KeyReadWriteRecognizer  -- per-script READS/WRITES classification (callee-co-occurrence), vocabulary
                               reused byte-identical from the deployed extract_pipeline.py classifier.

Adapted from DS~A's draft (deliverables/COMPILERKIT_recognizers_batch1.py) to the THREADED marker_head
contract (SDK fix 7af2db209): emit(site, tree, *, marker_head) -- recognize() threads it, no tree.meta hop.

FIRM-SCOPING (CTO ruling 2026-07-07, off AE~D's batch-1 structural parity diff + DS~A's batch-2 confirmed-
live collision find): any subject/target ref that a basename alone would collide across firms (bd/cot both
ship a "gold_dispatch.sh"; ~35 bd/cot gold script FILENAMES are byte-identical) must be firm-scoped, derived
from provenance.source via the SAME safe_deploy_core.PIPELINE_MAP authority DS/DT/AE already commit against
-- never a second hand-maintained map, never guessed. One `_firm_from_source` here (the canonical landed
module) shared by every recognizer in this file, mirroring DS~A's batch-2 helper exactly.
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
# REUSE the deployed extractor's vocabulary (zero-API-call, deterministic) so batch-2's read/write verdict
# is the SAME decision as today's production DAG, not a parallel reimplementation that can drift.
from extract_pipeline import (  # noqa: E402
    _extract_fstring_template, _find_aliases, _WRITE_CALLEES, _READ_CALLEES,
)

_TOOLS = os.path.join(_HERE, "..", "..", "..", ".tools")
if os.path.isdir(_TOOLS):
    sys.path.insert(0, os.path.abspath(_TOOLS))
from safe_deploy_core import PIPELINE_MAP  # noqa: E402


def _firm_from_source(source: str) -> str:
    """Derive the firm label from a repo-relative source path via PIPELINE_MAP (bd/inf/cot) -- never
    guessed. Returns 'unscoped' if source doesn't match a known data/{pipeline}/ prefix -- honest-degrade
    for the ref-scoping question (mirrors LAW 1's never-a-guess spirit without touching CSE confidence)."""
    norm = source.replace("\\", "/")
    for data_dir, (_bucket, label) in PIPELINE_MAP.items():
        if norm.startswith(f"data/{data_dir}/"):
            return label
    return "unscoped"


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
        firm = _firm_from_source(site.source)
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.SERVICE.value, f"dispatch:{firm}:{Path(site.source).stem}"),
            edges=[RelationshipDelta(Relationship.TRIGGERS.value,
                                     EntityRef(Entity.MODULE.value, f"gold:{firm}:{script}"))],
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
        # firm is hardcoded, not derived via _firm_from_source: this recognizer's concept is inherently
        # mdpf-scoped by construction (its one real source is mdpf's own dispatcher, not under any
        # data/{pipeline}/ prefix PIPELINE_MAP would resolve) -- honest, not a guess.
        script = Path(site.payload["relpath"]).stem
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.SERVICE.value, "mdpf-daily-runner"),
            edges=[RelationshipDelta(Relationship.TRIGGERS.value,
                                     EntityRef(Entity.MODULE.value, f"gold:mdpf:{script}"))],
            provenance=prov, confidence=1.0, marker_head=marker_head,
            producer_kind=self.producer_kind, compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )]


class S3KeyConstRecognizer(Recognizer):
    """Batch-2 (DS~A) -- compiler #1's ast mechanism over lib/s3_layout.py's constant assignments
    (ACCOUNTS_DIMENSION = '...') AND key-generating functions (def advisor_fee_detail_key(...) ->
    f'...{}...'). Mirrors extract_pipeline._parse_s3_layout's two ast.walk branches exactly. Emits a C0
    S3Bucket entity per key -- no edges; read/write EDGES are S3KeyReadWriteRecognizer's job."""
    artifact_class = "python"
    concept = "s3-key-const"
    requires = FrontEndCapability.LEXICAL_AST
    compiler_id = "code-compiler"

    def iter_sites(self, tree: EnrichedTree):
        import ast
        mod = tree.root if isinstance(tree.root, ast.Module) else ast.parse(tree.text)
        for node in ast.walk(mod):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and isinstance(node.value, ast.Constant):
                        name, value = target.id, node.value.value
                        if isinstance(value, str) and "/" in value and name.isupper():
                            yield Site(source=tree.source, locus=f"L{node.lineno}",
                                       evidence=f"{name} = {value!r}",
                                       payload={"name": name, "value": value, "kind": "const"})
            if isinstance(node, ast.FunctionDef):
                if node.name.startswith("legacy_") or node.name.startswith("_"):
                    continue
                for child in ast.walk(node):
                    if isinstance(child, ast.Return) and child.value:
                        template = _extract_fstring_template(child.value)
                        if template and "/" in template:
                            yield Site(source=tree.source, locus=f"L{node.lineno}",
                                       evidence=f"def {node.name}(...): return {template!r}",
                                       payload={"name": node.name, "value": template, "kind": "func"})
                            break

    def emit(self, site: Site, tree: EnrichedTree, *, marker_head: str):
        firm = _firm_from_source(site.source)
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.S3BUCKET.value, f"s3key:{firm}:{site.payload['value']}"),
            edges=[], provenance=prov, confidence=1.0, marker_head=marker_head,
            producer_kind=self.producer_kind, compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )]


class S3KeyReadWriteRecognizer(Recognizer):
    """Batch-2 (DS~A) -- compiler #1's callee-co-occurrence mechanism: per-script classification of each
    imported S3-key constant as READ or WRITE. Needs tree.meta['s3_constants'] = {const_name: s3_path}
    threaded in by the caller (the front-end's authoritative-map-assembly step -- see parity_run_batch2).
    KNOWN GAP (DS~A-flagged, not silent): does not port extract_pipeline's multi-line-call collapse or the
    Key=/Prefix=/f-string special-case matchers (lines 400-421) -- base callee-name+alias-on-one-line
    co-occurrence only (the dominant case)."""
    artifact_class = "python"
    concept = "s3-key-read-write"
    requires = FrontEndCapability.RAW_TEXT
    compiler_id = "code-compiler"

    def iter_sites(self, tree: EnrichedTree):
        consts = tree.meta.get("s3_constants", {})
        if not consts:
            return
        alias_map = {name: _find_aliases(name, tree.text) | {name} for name in consts}
        for lineno, line in enumerate(tree.text.splitlines(), start=1):
            stripped = line.strip()
            if stripped.startswith(("#", "from ", "import ")):
                continue
            for name, s3_path in consts.items():
                if not any(a in line for a in alias_map[name]):
                    continue
                kind = None
                for callee in _WRITE_CALLEES:
                    if callee in line and re.search(rf"{re.escape(callee)}\s*\(", line):
                        kind = "write"
                        break
                if kind is None:
                    for callee in _READ_CALLEES:
                        if callee in line and re.search(rf"{re.escape(callee)}\s*\(", line):
                            kind = "read"
                            break
                if kind:
                    yield Site(source=tree.source, locus=f"L{lineno}", evidence=stripped,
                               payload={"const": name, "s3_path": s3_path, "kind": kind})

    def emit(self, site: Site, tree: EnrichedTree, *, marker_head: str):
        rel = Relationship.WRITES.value if site.payload["kind"] == "write" else Relationship.READS.value
        firm = _firm_from_source(site.source)
        script = Path(tree.source).stem
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.MODULE.value, f"gold:{firm}:{script}"),
            edges=[RelationshipDelta(rel, EntityRef(Entity.S3BUCKET.value, f"s3key:{firm}:{site.payload['s3_path']}"))],
            provenance=prov, confidence=1.0, marker_head=marker_head,
            producer_kind=self.producer_kind, compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )]


class GoldDirectInvokeRecognizer(Recognizer):
    """Compiler #1 -- the gold_dispatch DIRECT-invoke leg (DEBTSCAN reachability FP-root-fix #2; DS~A-authored
    logic in extract_pipeline.parse_gold_direct_invoke, commit 75d93eaf7, SDK-ported here). Catches the
    `python3 "$SCRIPTS/<x>.py"` invokes OUTSIDE the CATALOG heredoc (the Wed-conditional gldinc_ss4c_weekly
    leg + co-dispatched diagnostics: diag_gold_silver_recon / gold_prof / runner-telemetry) that both the
    CATALOG recognizer AND the daily CHAIN parse miss -> they read isolated (the ss4c-dangle). REPRODUCES the
    current-C1 edges the legacy parse_gold_direct_invoke + inject_pipeline_edges emit, so the parity-oracle no
    longer regresses BD's direct-invoke edges. Disjoint from the CATALOG pattern (a CATALOG row is
    `ID|file.py|flags`, never a `python3 $SCRIPTS/` line) and from the dispatch loop (which invokes via the
    `$filename` VARIABLE, not a literal `.py`) -> no double-count. Same regex as the legacy, byte-for-byte."""

    artifact_class = "bash"
    concept = "gold-direct-invoke"
    requires = FrontEndCapability.RAW_TEXT
    compiler_id = "code-compiler"

    _INVOKE = re.compile(r'python3\s+"?\$\{?SCRIPTS\}?/(\S+?\.py)"?')   # == extract_pipeline.parse_gold_direct_invoke

    def iter_sites(self, tree):
        for m in self._INVOKE.finditer(tree.text):
            yield Site(source=tree.source, locus=locus_at(tree.text, m.start()),
                       evidence=m.group(0).strip(), payload={"relpath": m.group(1)})

    def emit(self, site, tree, *, marker_head):
        script = Path(site.payload["relpath"]).stem
        firm = _firm_from_source(site.source)
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.SERVICE.value, f"dispatch:{firm}:{Path(site.source).stem}"),
            edges=[RelationshipDelta(Relationship.TRIGGERS.value,
                                     EntityRef(Entity.MODULE.value, f"gold:{firm}:{script}"))],
            provenance=prov, confidence=1.0, marker_head=marker_head,
            producer_kind=self.producer_kind, compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )]


# The compiler-#1 recognizer set. register_all() wires them into a registry (the SDK hot-register seam).
BATCH1 = [DispatchCatalogRecognizer, MdpfDispatchRecognizer, GoldDirectInvokeRecognizer]
BATCH2 = [S3KeyConstRecognizer, S3KeyReadWriteRecognizer]


def register_all(registry: RecognizerRegistry) -> None:
    for cls in BATCH1 + BATCH2:
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
    # BD only -- matches the legacy parse_gold_direct_invoke's BD-only scope (what current C1 actually
    # contains). cot's gold_dispatch.sh also has direct invokes (gldinc_p1_shadow + diagnostics) but they
    # are NOT in current C1 (legacy never parsed cot) -> emitting them would be a superset, not a
    # reproduction. cot direct-invoke is a flagged deferred extension (mirrors batch-2's cot deferral).
    "gold-direct-invoke": ["data/black_diamond/scripts/gold/gold_dispatch.sh"],
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


# ---------------------------------------------------------------------------
# Batch-2 AC2 parity runner -- different tree-construction shape than batch-1 (LEXICAL_AST over
# s3_layout.py + the front-end "authoritative-map-assembly" step DS~A's docstring flags: run
# S3KeyConstRecognizer over a firm's s3_layout.py FIRST to build the const->s3_path map, then thread it
# via EnrichedTree.meta["s3_constants"] into that firm's gold-script trees for S3KeyReadWriteRecognizer).
# Scope this pass: BD only (matches DS~A's own validated test scope) -- cot/inf extension is a flagged
# next step, not silently assumed covered.
# ---------------------------------------------------------------------------
_S3_LAYOUT_SOURCES = {
    "bd": "data/black_diamond/scripts/gold/lib/s3_layout.py",
    # cot EXTEND (DS~A-proven GREEN, probe bddd84344; ruling #2 approved): bd-identical central s3_layout.py,
    # firm-scope keeps it distinct (ZERO cot/bd ref overlap despite byte-identical A_00/A_01 basenames), bd
    # baseline UNCHANGED -> purely additive, parity-oracle 1->2 firms.
    "cot": "data/cot/scripts/gold/lib/s3_layout.py",
}
_S3_GOLD_SCRIPT_SOURCES = {
    "bd": [
        "data/black_diamond/scripts/gold/A_00.accounts_dimension.py",
        "data/black_diamond/scripts/gold/A_01.advisor_assignments.py",
    ],
    "cot": [
        "data/cot/scripts/gold/A_00.accounts_dimension.py",
        "data/cot/scripts/gold/A_01.advisor_assignments.py",
    ],
}


def parity_run_batch2(marker_head: str = "parity") -> dict:
    import ast
    import cse_schema as cse
    ws = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
    report = {"firms": {}, "total_edges": 0, "all_fidelity_ok": True, "scope_note":
              "bd+cot (inf read/write DEFERRED -- accept-parity per ruling #3: deployed extract_pipeline has "
              "no inf read/write coverage, so matching it IS parity; inf CONST fires but is a C0 node set)"}
    const_rec = S3KeyConstRecognizer()
    rw_rec = S3KeyReadWriteRecognizer()
    for firm, layout_src in _S3_LAYOUT_SOURCES.items():
        ap = os.path.join(ws, layout_src)
        if not os.path.exists(ap):
            continue
        with open(ap, encoding="utf-8", errors="replace") as fh:
            layout_text = fh.read()
        t_layout = EnrichedTree(source=layout_src, capability=FrontEndCapability.LEXICAL_AST,
                                 text=layout_text, root=ast.parse(layout_text))
        const_cses, const_cov = const_rec.recognize(t_layout, marker_head=marker_head)
        # authoritative-map assembly: const name -> s3_path, keyed off the raw payload (not the firm-scoped
        # subject ref) since S3KeyReadWriteRecognizer's alias-matching works off the SOURCE constant name.
        s3_constants = {}
        for site in const_rec.iter_sites(t_layout):
            s3_constants[site.payload["name"]] = site.payload["value"]
        firm_rec = {"const_n_edges": len(const_cses), "const_fidelity_ok":
                    all(cse.cse_fidelity_ok(c)[0] for c in const_cses), "scripts": {}, "rw_n_edges": 0,
                    "rw_fidelity_ok": True}
        for script_src in _S3_GOLD_SCRIPT_SOURCES.get(firm, []):
            sp = os.path.join(ws, script_src)
            if not os.path.exists(sp):
                continue
            with open(sp, encoding="utf-8", errors="replace") as fh:
                script_text = fh.read()
            t_script = EnrichedTree(source=script_src, capability=FrontEndCapability.RAW_TEXT,
                                     text=script_text, meta={"s3_constants": s3_constants})
            rw_cses, rw_cov = rw_rec.recognize(t_script, marker_head=marker_head)
            fok = all(cse.cse_fidelity_ok(c)[0] for c in rw_cses)
            firm_rec["scripts"][script_src] = {
                "n_edges": len(rw_cses), "fidelity_ok": fok,
                "edges": [(c.transformation["subject"].ref, c.transformation["edges"][0].rtype,
                           c.transformation["edges"][0].target.ref, c.provenance.locus) for c in rw_cses],
                "unresolved": len(rw_cov.unresolved),
            }
            firm_rec["rw_n_edges"] += len(rw_cses)
            firm_rec["rw_fidelity_ok"] = firm_rec["rw_fidelity_ok"] and fok
        report["firms"][firm] = firm_rec
        report["total_edges"] += firm_rec["const_n_edges"] + firm_rec["rw_n_edges"]
        report["all_fidelity_ok"] = (report["all_fidelity_ok"] and firm_rec["const_fidelity_ok"]
                                      and firm_rec["rw_fidelity_ok"])
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

    rep2 = parity_run_batch2()
    print("\n=== COMPILERKIT-P1 batch-2 AC2 parity run (S3-key const + read/write over REAL source) ===")
    print(f"  SCOPE NOTE: {rep2['scope_note']}")
    for firm, fr in rep2["firms"].items():
        print(f"\n  firm={firm}: const_edges={fr['const_n_edges']} fidelity_ok={fr['const_fidelity_ok']}")
        for src, s in fr["scripts"].items():
            print(f"    {src}: {s['n_edges']} edges, fidelity_ok={s['fidelity_ok']}, unresolved={s['unresolved']}")
            for subj, rel, tgt, loc in s["edges"]:
                print(f"        {subj} --{rel}--> {tgt}  @{loc}")
    print(f"\n  BATCH-2 TOTAL: {rep2['total_edges']} edges; all_fidelity_ok={rep2['all_fidelity_ok']}")

    all_ok = (rep["all_fidelity_ok"] and rep["total_edges"] > 0
              and rep2["all_fidelity_ok"] and rep2["total_edges"] > 0)
    print("\n  NOTE: full structural diff vs the live extract_pipeline dispatch C1 = done separately "
          "(see NFRA_COMPILERKIT deliverables/P1-batch1-structural-parity-diff-20260707.md).")
    sys.exit(0 if all_ok else 1)
