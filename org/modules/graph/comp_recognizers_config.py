"""comp_recognizers_config -- NFRA_COMPILERKIT-P2: the config-artifact compiler (the FIRST non-code class)
on the shared Recognizer SDK. Author-DS (0.4.0_DS_ClientPlatform~A, the recognizers) / front-end+wire+parity-AE
(0.8.0_AE_CloudComp~D, this canonical module + the config FrontEnds). Pure-lexical (CTO #3).

WHY THIS MODULE (P2 framework-lane): the config recognizers were authored+validated against the live SDK in
deliverables/COMPILERKIT_recognizers_P2_config.py (66f7bcd14, 11/11). This lands them in a CANONICAL
org/modules/graph module + adds the two config FrontEnds my P2 framework-review flagged as my lane
(ac72b0399) -- so the config compiler is SDK-ROUTED (front-end -> registry -> run_recognizers) exactly like
compiler #1 (comp_recognizers_code.py), compiler #2 (comp_recognizers_tsx.py), and the ticket compiler
(comp_recognizers_ticket.py). All four artifact compilers now share ONE uniform exercise surface for CVO.

AC4 (config->consumer edges into C1): both recognizers emit a `config:{scope}:{artifact}` ARTIFACT subject
REFERENCES-ing an already-modeled infra entity -- an S3 bucket (an s3:// URI in a YAML value) or a SecretRef
(a *_SECRET_ID pointer in an env file). That REFERENCES edge from a config artifact to the infra it points
at is the config->consumer dimension the code-only graph lacked. A config value that cross-references nothing
modeled honest-degrades to Concept(untyped)+low (LAW 1) -- correct, not a gap (per CTO determinism decision).

NO LIVE GRAPH TO DIFF AGAINST: unlike P1 (which reconciled two EXISTING compilers), config is net-new
extraction -- there is no prior yaml/toml/env extractor in extract_pipeline.py/trace_graph.py. So P2's
acceptance bar is fidelity_check + honest-degrade + the config->consumer edges landing valid (AC4), NOT a
structural parity diff (framework-review item 3, COO/CTO-noted). This module proves those.

SCOPE token (CTO firm-collision ruling, generalized): config BASENAMES collide the same way gold-script
basenames did (gold_freshness_config.yaml byte-identical across data/{bd,inf,cot}/; secret-ids.env identical
across infra/aws/ec2/{bd-49f,bd-cot}-auto-login/). _scope_from_source() = PIPELINE_MAP firm label under
data/{pipeline}/, else the immediate parent dir (the service identity for infra/aws/ec2/{service}/) -- always
derived from provenance.source, never guessed. Generalizes comp_recognizers_code._firm_from_source.

Recognizer origin: deliverables/COMPILERKIT_recognizers_P2_config.py (66f7bcd14) -- re-homed canonical here,
mirroring how comp_recognizers_code.py re-homed batch-1/2 + comp_recognizers_tsx.py re-homed FLOWS_TO.
Author: 0.8.0_AE_CloudComp~D (NFRA_COMPILERKIT.P2, framework-lead). 2026-07-07.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import Iterable

import yaml

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from comp_recognizer_sdk import (  # noqa: E402
    Recognizer, RecognizerRegistry, FrontEnd, emit_cse, Site, EnrichedTree, EntityRef, RelationshipDelta,
    Provenance, Entity, Relationship, Transformation, FrontEndCapability, run_recognizers,
)

_TOOLS = os.path.join(_HERE, "..", "..", "..", ".tools")
if os.path.isdir(_TOOLS):
    sys.path.insert(0, os.path.abspath(_TOOLS))
from safe_deploy_core import PIPELINE_MAP  # noqa: E402


def _ws_root() -> str:
    return os.path.abspath(os.path.join(_HERE, "..", "..", ".."))


def _scope_from_source(source: str) -> str:
    """Deterministic scope token from provenance.source -- PIPELINE_MAP firm label under data/{pipeline}/,
    else the immediate parent directory (the service identity for infra/aws/ec2/{service}/ configs).
    Never guessed; generalizes comp_recognizers_code._firm_from_source for non-data/ sources (config
    artifacts live outside the 3-pipeline data/ tree, unlike gold scripts + s3_layout.py)."""
    norm = source.replace("\\", "/")
    for data_dir, (_bucket, label) in PIPELINE_MAP.items():
        if norm.startswith(f"data/{data_dir}/"):
            return label
    parts = [p for p in norm.split("/") if p]
    if len(parts) >= 2:
        return parts[-2]
    return "unscoped"


_S3_URI_RE = re.compile(r"^s3://([a-z0-9.-]+)(/.*)?$")


class ConfigS3RefRecognizer(Recognizer):
    """YAML config values that are literal s3:// URIs (e.g. gold_freshness_config.yaml's s3_key_prefix).
    LEXICAL_AST tier -- walks a PyYAML compose() node tree (not safe_load: compose() keeps per-node
    start_mark.line for real file:line provenance). The S3 URI embeds the bucket name, so the TARGET ref is
    inherently firm-disambiguated; only the config-artifact SUBJECT ref needs the scope token (identical
    basename across firms). Emits config -[REFERENCES]-> S3Bucket = the config->consumer edge (AC4)."""

    artifact_class = "yaml"
    concept = "config-s3-ref"
    requires = FrontEndCapability.LEXICAL_AST
    compiler_id = "config-compiler"
    emits = (Entity.ARTIFACT.value, Entity.S3BUCKET.value, Relationship.REFERENCES.value)

    def iter_sites(self, tree: EnrichedTree) -> Iterable[Site]:
        root = tree.root if tree.root is not None else yaml.compose(tree.text)
        if root is None:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if isinstance(node, yaml.ScalarNode):
                m = _S3_URI_RE.match(node.value)
                if m:
                    yield Site(source=tree.source, locus=f"L{node.start_mark.line + 1}",
                               evidence=node.value, payload={"uri": node.value})
            elif isinstance(node, yaml.MappingNode):
                for k, v in node.value:
                    stack.append(k)
                    stack.append(v)
            elif isinstance(node, yaml.SequenceNode):
                stack.extend(node.value)

    def emit(self, site: Site, tree: EnrichedTree, *, marker_head: str) -> list:
        scope = _scope_from_source(site.source)
        artifact = f"config:{scope}:{Path(tree.source).stem}"
        target = f"s3:{site.payload['uri'][len('s3://'):]}"
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.ARTIFACT.value, artifact),
            edges=[RelationshipDelta(Relationship.REFERENCES.value, EntityRef(Entity.S3BUCKET.value, target))],
            provenance=prov, confidence=1.0, marker_head=marker_head,
            producer_kind=self.producer_kind, compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )]


# a SECRET-named key whose value isn't a clean secret-id/path token (spaces, empty, not a bare identifier)
# is genuinely UNTYPABLE -- LAW 1 degrades, never guesses a ref.
_CLEAN_TOKEN_RE = re.compile(r"^[A-Za-z0-9_./-]+$")
_ENV_KV_RE = re.compile(r"^([A-Z][A-Z0-9_]*)\s*=\s*(.*)$")


class EnvSecretRefRecognizer(Recognizer):
    """env-file KEY=VALUE lines where KEY names a secret (*_SECRET_ID / *SECRET*) and VALUE is a secret-id
    POINTER (a Secrets Manager name/path, never a secret VALUE per the files' own header contracts). RAW_TEXT
    tier -- line-scoped. A SECRET-named key whose value fails the clean-token shape HONEST-DEGRADES rather
    than emitting a guessed SecretRef (LAW 1). Emits config -[REFERENCES]-> SecretRef = config->consumer (AC4)."""

    artifact_class = "env"
    concept = "config-secret-ref"
    requires = FrontEndCapability.RAW_TEXT
    compiler_id = "config-compiler"
    emits = (Entity.ARTIFACT.value, Entity.SECRETREF.value, Relationship.REFERENCES.value)

    def iter_sites(self, tree: EnrichedTree) -> Iterable[Site]:
        for lineno, line in enumerate(tree.text.splitlines(), start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            m = _ENV_KV_RE.match(stripped)
            if not m:
                continue
            key, value = m.group(1), m.group(2).strip()
            if "SECRET" not in key or not value:
                continue
            yield Site(source=tree.source, locus=f"L{lineno}", evidence=stripped,
                       payload={"key": key, "value": value})

    def emit(self, site: Site, tree: EnrichedTree, *, marker_head: str) -> list:
        value = site.payload["value"]
        if not _CLEAN_TOKEN_RE.match(value):
            return [self.degrade(site, marker_head=marker_head)]
        scope = _scope_from_source(site.source)
        artifact = f"config:{scope}:{Path(tree.source).stem}"
        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept, evidence=site.evidence)
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.ARTIFACT.value, artifact),
            edges=[RelationshipDelta(Relationship.REFERENCES.value,
                                     EntityRef(Entity.SECRETREF.value, f"secret:{value}"))],
            provenance=prov, confidence=1.0, marker_head=marker_head,
            producer_kind=self.producer_kind, compiler_id=self.compiler_id, artifact_class=self.artifact_class,
        )]


# Sovereign hold (bd/schwab): _YAML_SOURCES includes the bd gold_freshness_config.yaml; build_trees
# opens+yaml.compose it. Defensive path-based skip by default (this is a __main__-only parity harness,
# but a __main__ IS agent-runnable); COMP_RECOGNIZERS_INCLUDE_HELD=1 re-enables (DS/parity path). Pure
# str check, never opens the file. (Folds into sovereign_held.py at the C1 consolidation.)
_HELD_MARKERS = ("data/black_diamond/", "data/canonical/schwab/silver/", "schwab/silver/")


def _is_held(rel) -> bool:
    s = str(rel or "").replace("\\", "/")
    return any(m in s for m in _HELD_MARKERS)


def _recognizers_include_held() -> bool:
    return os.environ.get("COMP_RECOGNIZERS_INCLUDE_HELD") == "1"


# ---------------------------------------------------------------------------
# Config FrontEnds (the framework-lane work my P2 review flagged) -- two capability tiers, one per class,
# so the registry's capability-matched dispatch keeps a YAML recognizer from ever seeing an .env tree.
# ---------------------------------------------------------------------------
class ConfigYamlFrontEnd(FrontEnd):
    """YAML config front-end, LEXICAL_AST. Parses each .yaml via yaml.compose() (keeps per-node line marks
    for file:line provenance). Per-artifact lifecycle. scope = an iterable of repo-relative .yaml paths."""

    artifact_class = "yaml"
    capability = FrontEndCapability.LEXICAL_AST
    lifecycle = "per-artifact"

    def build_trees(self, scope) -> Iterable[EnrichedTree]:
        for rel in (scope or []):
            ap = os.path.join(_ws_root(), rel)
            if not os.path.exists(ap):
                continue
            if _is_held(rel) and not _recognizers_include_held():
                continue  # sovereign hold: skip held bd/schwab config (defensive)
            with open(ap, encoding="utf-8") as fh:
                text = fh.read()
            yield EnrichedTree(source=rel, capability=self.capability, text=text, root=yaml.compose(text))


class ConfigEnvFrontEnd(FrontEnd):
    """env/tfvars config front-end, RAW_TEXT (flat KEY=VALUE -- regex is the right tier, no parser). Per-
    artifact lifecycle. scope = an iterable of repo-relative .env paths."""

    artifact_class = "env"
    capability = FrontEndCapability.RAW_TEXT
    lifecycle = "per-artifact"

    def build_trees(self, scope) -> Iterable[EnrichedTree]:
        for rel in (scope or []):
            ap = os.path.join(_ws_root(), rel)
            if not os.path.exists(ap):
                continue
            if _is_held(rel) and not _recognizers_include_held():
                continue  # sovereign hold: skip held bd/schwab config (defensive)
            with open(ap, encoding="utf-8") as fh:
                yield EnrichedTree(source=rel, capability=self.capability, text=fh.read())


CONFIG_RECOGNIZERS = [ConfigS3RefRecognizer, EnvSecretRefRecognizer]


def register_all(registry: RecognizerRegistry) -> None:
    for cls in CONFIG_RECOGNIZERS:
        registry.register(cls())


# REAL config sources (the same real artifacts DS~A's recognizer harness grounds against). bd+cot yaml
# (identical basename, distinct scope) + a real secret-ids.env -- the config->consumer edges land over these.
_YAML_SOURCES = [
    "data/black_diamond/scripts/gold/gold_freshness_config.yaml",
    "data/cot/scripts/gold/gold_freshness_config.yaml",
]
_ENV_SOURCES = [
    "infra/aws/ec2/bd-cot-auto-login/secret-ids.env",
]


def parity_run_config(marker_head: str = "parity") -> dict:
    """AC4 config->consumer materialize -- SDK-routed (front-end -> registry -> run_recognizers) per class.
    Reports the config->consumer REFERENCES edges + fidelity + coverage. No structural-diff (net-new class,
    no prior extractor to reproduce) -- the acceptance bar is valid config->consumer edges + fidelity."""
    import cse_schema as cse

    reg = RecognizerRegistry()
    register_all(reg)
    report = {"classes": {}, "total_config_consumer_edges": 0, "all_fidelity_ok": True, "coverage_unresolved": 0,
              "scope_note": "net-new class -- no live extractor to structural-diff; bar = config->consumer "
                            "edges land valid + fidelity (AC4) + honest-degrade (AC3)"}
    for fe, sources in ((ConfigYamlFrontEnd(), _YAML_SOURCES), (ConfigEnvFrontEnd(), _ENV_SOURCES)):
        out = run_recognizers(reg, fe, scope=sources, marker_head=marker_head)
        cses, cov = out["cses"], out["coverage"]
        edges = [(c.transformation["subject"].ref, c.transformation["edges"][0].rtype,
                  c.transformation["edges"][0].target.ref, c.provenance.source, c.provenance.locus)
                 for c in cses if c.transformation["edges"]]
        fok = all(cse.cse_fidelity_ok(c)[0] for c in cses)
        report["classes"][fe.artifact_class] = {
            "n_cses": len(cses), "n_config_consumer_edges": len(edges), "edges": edges,
            "fidelity_ok": fok, "coverage_unresolved": len(cov.unresolved), "n_trees": out["n_trees"],
        }
        report["total_config_consumer_edges"] += len(edges)
        report["all_fidelity_ok"] = report["all_fidelity_ok"] and fok
        report["coverage_unresolved"] += len(cov.unresolved)
    return report


if __name__ == "__main__":
    rep = parity_run_config()
    print("=== COMPILERKIT-P2 config compiler AC4 -- config->consumer edges (SDK-routed) ===")
    print(f"  SCOPE NOTE: {rep['scope_note']}")
    for ac, cl in rep["classes"].items():
        print(f"\n  artifact_class={ac}: {cl['n_config_consumer_edges']} config->consumer edges "
              f"({cl['n_trees']} trees), fidelity_ok={cl['fidelity_ok']}, unresolved={cl['coverage_unresolved']}")
        for subj, rel, tgt, src, loc in cl["edges"]:
            print(f"      {subj} --{rel}--> {tgt}   ({src}:{loc})")
    print(f"\n  TOTAL config->consumer edges: {rep['total_config_consumer_edges']}; "
          f"all_fidelity_ok={rep['all_fidelity_ok']}")
    ok = (rep["all_fidelity_ok"] and rep["total_config_consumer_edges"] > 0
          and rep["coverage_unresolved"] == 0)
    print(f"\n=== config compiler AC4: {'PASS' if ok else 'FAIL'} "
          f"(config->consumer edges land in C1, fidelity-clean, a dimension the code-only graph lacked) ===")
    sys.exit(0 if ok else 1)
