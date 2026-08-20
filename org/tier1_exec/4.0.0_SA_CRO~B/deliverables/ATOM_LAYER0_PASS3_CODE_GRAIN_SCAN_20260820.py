#!/usr/bin/env python3
"""Reproduce the ATOM_LAYER0 Pass-3 code-grain receipts from pinned Git objects.

The instrument discovers exact governed tokens in runtime Python syntax. It does
not assign census verdicts: lexical overlap still requires grain/meaning
adjudication (for example comp_toolgraph's local AC-0 clauses named C1/C2).
"""

from __future__ import annotations

import argparse
import ast
import json
import subprocess
from typing import Any

import yaml


ASSESSMENT_COMMIT = "f36d572be864e56b9175caac06b01f62fc141e2a"
POPULATION_COMMIT = "76ba5fec3d"
POPULATION_PATH = (
    "org/tier1_exec/4.0.0_SA_CRO~B/deliverables/"
    "ATOM_LAYER0_RESOLUTION_CENSUS_PASS3_CODE_POPULATION_20260820.yaml"
)
RULE_BANK = "org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml"
CANONICAL = "org/modules/graph/NFRA_ONTOLOGY_C2C3_CANONICAL.yaml"
DEFINITIONS = "infra/system/ontology/SYSTEM_DEFINITIONS.yaml"
CONTROL = "org/modules/graph/comp_legacywriter.py"


def git_bytes(commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"])


def git_text(commit: str, path: str) -> str:
    return git_bytes(commit, path).decode("utf-8")


def git_blob(commit: str, path: str) -> str:
    return subprocess.check_output(
        ["git", "rev-parse", f"{commit}:{path}"], text=True
    ).strip()


def concrete_edge_tokens(rule_bank: dict[str, Any]) -> set[str]:
    tokens = set(rule_bank["non_relation_edges"])
    tokens.update(rule_bank["c1_frontend_adapter"]["determinations"])
    for group in list(rule_bank["relations"].values()) + list(
        rule_bank["relation_composites"].values()
    ):
        if isinstance(group, dict):
            binds = group.get("binds_up", [])
            if isinstance(binds, list):
                tokens.update(str(value) for value in binds)
            also = group.get("also", [])
            if isinstance(also, list):
                tokens.update(str(value) for value in also)
    d1 = rule_bank["dynamic_rails"]["D1_value_grain"]["edge_grain_binding"]
    for group in d1.values():
        if isinstance(group, dict):
            tokens.update(group)
    evidence = rule_bank["dynamic_rails"]["D2_path_flow"]["graph_evidence"]
    tokens.update(evidence["flow_edges"])
    tokens.update(evidence["control_edges"])
    return tokens


def categories(
    definitions: dict[str, Any],
    rule_bank: dict[str, Any],
    canonical: dict[str, Any],
) -> dict[str, set[str]]:
    d3 = rule_bank["dynamic_rails"]["D3_contract_obligation"]
    type_tuple = rule_bank["type_tuple"]
    node_types: set[str] = set(rule_bank["contextual_types"])
    for values in rule_bank["node_bindings"].values():
        if isinstance(values, list):
            node_types.update(str(value) for value in values)
    verticals = canonical["c3_ii_semantic_verticals"]["verticals"]
    if isinstance(verticals, dict):
        vertical_names = set(verticals)
    else:
        vertical_names = {
            str(value.get("name") if isinstance(value, dict) else value)
            for value in verticals
        }
    return {
        "system_terms": set(definitions["terms"]),
        "roles": set(rule_bank["roles"]),
        "abstract_relations": set(rule_bank["relations"])
        | set(rule_bank["relation_composites"]),
        "concrete_edges": concrete_edge_tokens(rule_bank),
        "node_types": node_types,
        "variance_labels": set(rule_bank["variance"]["labels"]),
        "contract_record_fields": set(d3["contract_record"]["required"])
        | set(d3["contract_record"]["optional"]),
        "d1_edge_kinds": set(
            rule_bank["dynamic_rails"]["D1_value_grain"]["edgekind_semantic"]
        ),
        "d3_obligation_types": set(d3["obligation_types"]),
        "lifecycle_class": set(d3["lifecycle"]["enum"]),
        "lifecycle_stage": set(d3["lifecycle"]["stage"]["enum"]),
        "type_rail": set(type_tuple["rail"]["enum"]),
        "type_grain": set(type_tuple["grain"]["enum"]),
        "type_plane": set(type_tuple["plane"]["enum"]),
        "type_scope": set(type_tuple["scope"]["enum"]),
        "c2_families": set(canonical["c2_motif_families"]),
        "c3_i_structures": set(canonical["c3_deterministic_structures"]),
        "c3_ii_verticals": vertical_names,
        "c4_segments": set(canonical["c4_segments"]),
    }


def docstring_node_ids(tree: ast.AST) -> set[int]:
    ids: set[int] = set()
    owners = [tree] + [
        node
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))
    ]
    for owner in owners:
        body = getattr(owner, "body", [])
        if (
            body
            and isinstance(body[0], ast.Expr)
            and isinstance(body[0].value, ast.Constant)
            and isinstance(body[0].value.value, str)
        ):
            ids.add(id(body[0].value))
    return ids


def assignment_name(node: ast.AST) -> str:
    if isinstance(node, ast.Assign) and node.targets:
        target = node.targets[0]
    elif isinstance(node, ast.AnnAssign):
        target = node.target
    else:
        return "<expression>"
    if isinstance(target, ast.Name):
        return target.id
    if isinstance(target, ast.Attribute):
        return target.attr
    return "<complex-target>"


def scan_source(path: str, source: str, blob: str, groups: dict[str, set[str]]) -> dict[str, Any]:
    tree = ast.parse(source, filename=path)
    doc_ids = docstring_node_ids(tree)
    runtime = [
        (node.lineno, node.value)
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and id(node) not in doc_ids
    ]
    hits: dict[str, list[dict[str, Any]]] = {}
    for name, values in groups.items():
        exact = sorted((line, value) for line, value in runtime if value in values)
        if exact:
            hits[name] = [
                {"line": line, "value": value} for line, value in exact
            ]

    clusters: list[dict[str, Any]] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            value_node = node.value
            label = assignment_name(node)
        elif isinstance(node, ast.Compare):
            value_node = node
            label = "<comparison>"
        else:
            continue
        if value_node is None:
            continue
        literals = {
            child.value
            for child in ast.walk(value_node)
            if isinstance(child, ast.Constant) and isinstance(child.value, str)
        }
        if len(literals) < 2:
            continue
        for group, values in groups.items():
            overlap = sorted(literals & values)
            if len(overlap) >= 2:
                clusters.append(
                    {
                        "line": node.lineno,
                        "binding": label,
                        "authority_group": group,
                        "members": overlap,
                    }
                )

    pointer_tokens = (
        "NFRA_ONTOLOGY_RULE_BANK.yaml",
        "NFRA_ONTOLOGY_C2C3_CANONICAL.yaml",
        "SYSTEM_DEFINITIONS.yaml",
        "comp-coverage-map.yaml",
        "cse_schema",
    )
    pointers = [token for token in pointer_tokens if token in source]
    return {
        "path": path,
        "blob": blob,
        "line_count": len(source.splitlines()),
        "ast_parse": "PASS",
        "authority_pointers": pointers,
        "governed_runtime_hits": hits,
        "literal_clusters": clusters,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--assessment-commit", default=ASSESSMENT_COMMIT)
    parser.add_argument("--population-commit", default=POPULATION_COMMIT)
    args = parser.parse_args()

    population = yaml.safe_load(git_bytes(args.population_commit, POPULATION_PATH))
    definitions = yaml.safe_load(git_bytes(args.assessment_commit, DEFINITIONS))
    rule_bank = yaml.safe_load(git_bytes(args.assessment_commit, RULE_BANK))
    canonical = yaml.safe_load(git_bytes(args.assessment_commit, CANONICAL))
    groups = categories(definitions, rule_bank, canonical)

    receipts = []
    for engine in population["engines"]:
        path = engine["path"]
        blob = git_blob(args.assessment_commit, path)
        if blob != engine["blob"]:
            raise RuntimeError(f"population blob mismatch: {path}")
        receipts.append(scan_source(path, git_text(args.assessment_commit, path), blob, groups))

    control_blob = git_blob(args.assessment_commit, CONTROL)
    control = scan_source(
        CONTROL, git_text(args.assessment_commit, CONTROL), control_blob, groups
    )
    result = {
        "instrument": "ATOM_LAYER0_PASS3_CODE_GRAIN_SCAN",
        "assessment_commit": args.assessment_commit,
        "population_commit": args.population_commit,
        "population_count": len(receipts),
        "ast_parse_pass": sum(r["ast_parse"] == "PASS" for r in receipts),
        "receipts": receipts,
        "positive_type_control": control,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
