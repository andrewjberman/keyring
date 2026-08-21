#!/usr/bin/env python3
"""Typed Observation_Record construction and non-invasive comp-tool wrappers.

Shared-object source of record:
docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md sec.2.1 @ bf88ff55c6.
This module implements that record; it does not own or widen its fields.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover
    raise RuntimeError("jsonschema>=4 is required") from exc


PACKAGE_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = PACKAGE_ROOT / "schemas" / "observation_record.schema.json"
SOURCE_OF_RECORD = (
    "docs/architecture/PRD_EPISTEMIC_MECHANIZATION_20260820.md sec.2.1 @ bf88ff55c6"
)
STAGE_SUCCESS = {
    "acquisition": "PRESENT",
    "transport": "SUCCEEDED",
    "enumeration": "SUCCEEDED",
    "parse": "SUCCEEDED",
}


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode(
        "ascii"
    )


def request_hash(request: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(request)).hexdigest()


def _statuses_succeeded(status: dict[str, str]) -> bool:
    return all(status.get(stage) == expected for stage, expected in STAGE_SUCCESS.items())


def build_record(
    *,
    instrument_id: str,
    instrument_version: str,
    request: Any,
    status: dict[str, str],
    plane: str,
    substrate: str,
    population_predicate: str,
    denominator_count: int | None,
    denominator_grain: str,
    denominator_process: str,
    substantive_value: Any,
    unknown_reason: str,
    observed_at: str,
    support_pointers: list[str],
    traversal_residue: list[str] | None = None,
    control_references: list[str] | None = None,
    discrimination_certificate_ref: str | None = None,
    invalidation_predicates: list[str] | None = None,
) -> dict[str, Any]:
    """Construct an envelope; callers cannot force a known result through a failed stage."""
    known = _statuses_succeeded(status)
    result = (
        {"state": "KNOWN", "value": copy.deepcopy(substantive_value), "reason": None}
        if known
        else {
            "state": "UNKNOWN",
            "value": None,
            "reason": unknown_reason or "one or more acquisition-pipeline stages did not succeed",
        }
    )
    return {
        "instrument": {"id": instrument_id, "version": instrument_version},
        "request_hash": request_hash(request),
        "status": copy.deepcopy(status),
        "plane": plane,
        "substrate": substrate,
        "population_predicate": population_predicate,
        "denominator": {
            "count": denominator_count,
            "grain": denominator_grain,
            "generated_by": denominator_process,
        },
        "traversal_residue": list(traversal_residue or []),
        "substantive_result": result,
        "control_references": list(control_references or []),
        "discrimination_certificate_ref": discrimination_certificate_ref,
        "observed_at": observed_at,
        "support_pointers": list(support_pointers),
        "invalidation_predicates": list(invalidation_predicates or []),
    }


def validate_record(record: dict[str, Any]) -> list[str]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    errors = [
        f"schema {'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in sorted(validator.iter_errors(record), key=lambda item: list(item.absolute_path))
    ]
    if not errors:
        succeeded = _statuses_succeeded(record["status"])
        result = record["substantive_result"]
        if not succeeded and (result["state"] != "UNKNOWN" or result["value"] is not None):
            errors.append("failed/absent/unknown/not-attempted stage must force UNKNOWN with null value")
    return errors


def _repo_commit(repo_root: Path) -> str:
    proc = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=repo_root, capture_output=True, text=True
    )
    return proc.stdout.strip() if proc.returncode == 0 and proc.stdout.strip() else "UNRESOLVED"


def _file_version(repo_root: Path, path: Path) -> str:
    try:
        rel = path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return "UNRESOLVED"
    proc = subprocess.run(
        ["git", "rev-parse", f"HEAD:{rel}"], cwd=repo_root, capture_output=True, text=True
    )
    if proc.returncode == 0 and proc.stdout.strip():
        return proc.stdout.strip()
    if path.is_file():
        return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()
    return "UNRESOLVED"


def _run_python_tool(tool: Path, args: list[str], repo_root: Path) -> tuple[int, str, str]:
    if not tool.is_file():
        raise FileNotFoundError(str(tool))
    proc = subprocess.run(
        [sys.executable, str(tool)] + args,
        cwd=repo_root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return proc.returncode, proc.stdout, proc.stderr


def wrap_comp_find(
    repo_root: Path,
    pattern: str,
    pathspec: list[str],
    observed_at: str,
    tool_path: Path | None = None,
) -> dict[str, Any]:
    tool = tool_path or repo_root / ".tools" / "comp-find"
    request = {"pattern": pattern, "pathspec": pathspec, "mode": "content"}
    support = [f"{tool.as_posix()} @ {_repo_commit(repo_root)}"]
    base = dict(
        instrument_id="comp-find",
        instrument_version=_file_version(repo_root, tool),
        request=request,
        plane="DESIRED",
        substrate="codebase",
        population_predicate="gitignore-aware readable files within the declared pathspec",
        denominator_grain="readable file scanned",
        denominator_process="comp-find gitignore-aware file enumerator; unreadable residue printed separately",
        observed_at=observed_at,
        support_pointers=support,
        control_references=["comp-find graded denominator contract"],
        invalidation_predicates=["comp-find blob changes", "pathspec population changes"],
    )
    try:
        rc, stdout, stderr = _run_python_tool(tool, [pattern] + pathspec + ["--limit", "3"], repo_root)
    except FileNotFoundError as exc:
        return build_record(
            **base,
            status={"acquisition": "ABSENT", "transport": "NOT_ATTEMPTED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"},
            denominator_count=None,
            substantive_value=0,
            unknown_reason=f"comp-find acquisition absent: {exc}",
            traversal_residue=[str(exc)],
        )
    if rc != 0:
        return build_record(
            **base,
            status={"acquisition": "PRESENT", "transport": "SUCCEEDED", "enumeration": "FAILED", "parse": "NOT_ATTEMPTED"},
            denominator_count=None,
            substantive_value=0,
            unknown_reason=f"comp-find returned rc={rc}",
            traversal_residue=[stderr.strip() or stdout.strip() or "no diagnostic text"],
        )
    if not stdout.strip():
        return build_record(
            **base,
            status={"acquisition": "PRESENT", "transport": "FAILED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"},
            denominator_count=None,
            substantive_value=[],
            unknown_reason="comp-find returned empty stdout with rc=0",
            traversal_residue=[stderr.strip()] if stderr.strip() else [],
        )
    match = re.search(
        r"DENOMINATOR:\s+(\d+) hit\(s\) across (\d+) file\(s\) scanned in scope(?:\s+\|\s+(\d+) UNREADABLE)?",
        stdout,
    )
    if not match:
        return build_record(
            **base,
            status={"acquisition": "PRESENT", "transport": "SUCCEEDED", "enumeration": "UNKNOWN", "parse": "FAILED"},
            denominator_count=None,
            substantive_value="PASS",
            unknown_reason="comp-find denominator contract was not parseable",
            traversal_residue=["stdout_digest=sha256:" + hashlib.sha256(stdout.encode()).hexdigest()],
        )
    hits, scanned, unreadable = (int(match.group(1)), int(match.group(2)), int(match.group(3) or 0))
    return build_record(
        **base,
        status={"acquisition": "PRESENT", "transport": "SUCCEEDED", "enumeration": "SUCCEEDED", "parse": "SUCCEEDED"},
        denominator_count=scanned,
        substantive_value={
            "hits": hits,
            "files_scanned": scanned,
            "stdout_digest": "sha256:" + hashlib.sha256(stdout.encode()).hexdigest(),
        },
        unknown_reason="",
        traversal_residue=[f"unreadable_files={unreadable}"] if unreadable else [],
    )


def wrap_comp_estate(
    repo_root: Path,
    args: list[str],
    observed_at: str,
    tool_path: Path | None = None,
) -> dict[str, Any]:
    tool = tool_path or repo_root / ".tools" / "comp-estate"
    engine = repo_root / "org" / "modules" / "graph" / "opal_estate_infrastructure.py"
    request = {"argv": args}
    base = dict(
        instrument_id="comp-estate",
        instrument_version=_file_version(repo_root, engine),
        request=request,
        plane="DESIRED",
        substrate="codebase",
        population_predicate="C3.ii verticals and their live-derived chain population selected by comp-estate argv",
        denominator_grain="C2-motif chain instance",
        denominator_process="comp-estate engine enumeration with its verdict-preserving footer",
        observed_at=observed_at,
        support_pointers=[f"{tool.as_posix()} @ {_repo_commit(repo_root)}", f"{engine.as_posix()} @ {_repo_commit(repo_root)}"],
        control_references=["comp-estate --self-test", "comp-estate --head verdict-preserving contract"],
        invalidation_predicates=["comp-estate engine blob changes", "estate snapshot or producer source changes"],
    )
    try:
        rc, stdout, stderr = _run_python_tool(tool, args, repo_root)
    except FileNotFoundError as exc:
        return build_record(
            **base,
            status={"acquisition": "ABSENT", "transport": "NOT_ATTEMPTED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"},
            denominator_count=None,
            substantive_value=0,
            unknown_reason=f"comp-estate acquisition absent: {exc}",
            traversal_residue=[str(exc)],
        )
    if rc != 0:
        return build_record(
            **base,
            status={"acquisition": "PRESENT", "transport": "SUCCEEDED", "enumeration": "FAILED", "parse": "NOT_ATTEMPTED"},
            denominator_count=None,
            substantive_value=[],
            unknown_reason=f"comp-estate returned rc={rc}",
            traversal_residue=[stderr.strip() or stdout.strip() or "no diagnostic text"],
        )
    if not stdout.strip():
        return build_record(
            **base,
            status={"acquisition": "PRESENT", "transport": "FAILED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"},
            denominator_count=None,
            substantive_value="PASS",
            unknown_reason="comp-estate returned empty stdout with rc=0",
            traversal_residue=[],
        )
    heading = re.search(r"comp-estate - (\d+) C3\.ii semantic verticals / (\d+) chains", stdout)
    if heading:
        verticals, chains = int(heading.group(1)), int(heading.group(2))
    else:
        thread = re.search(r"comp-estate C3\.ii vertical .*? - (\d+) chains", stdout)
        verticals, chains = (1, int(thread.group(1))) if thread else (0, -1)
    if chains < 0:
        return build_record(
            **base,
            status={"acquisition": "PRESENT", "transport": "SUCCEEDED", "enumeration": "UNKNOWN", "parse": "FAILED"},
            denominator_count=None,
            substantive_value=0,
            unknown_reason="comp-estate denominator contract was not parseable",
            traversal_residue=["stdout_digest=sha256:" + hashlib.sha256(stdout.encode()).hexdigest()],
        )
    return build_record(
        **base,
        status={"acquisition": "PRESENT", "transport": "SUCCEEDED", "enumeration": "SUCCEEDED", "parse": "SUCCEEDED"},
        denominator_count=chains,
        substantive_value={
            "verticals": verticals,
            "chains": chains,
            "stdout_digest": "sha256:" + hashlib.sha256(stdout.encode()).hexdigest(),
        },
        unknown_reason="",
        traversal_residue=[stderr.strip()] if stderr.strip() else [],
    )


def _load_census_module(path: Path):
    spec = importlib.util.spec_from_file_location("nfra_epistemy_census_substrate", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def wrap_census_substrate(
    repo_root: Path,
    descriptor: str,
    observed_at: str,
    runner: Callable[[list[str]], tuple[int, str, str]] | None = None,
    module_path: Path | None = None,
) -> dict[str, Any]:
    module_file = module_path or repo_root / "org" / "modules" / "graph" / "census_substrate.py"
    request = {"descriptor": descriptor, "operation": "build_descriptor_census"}
    base = dict(
        instrument_id="census_substrate",
        instrument_version=_file_version(repo_root, module_file),
        request=request,
        plane="APPLIED",
        substrate="aws",
        population_predicate=f"all items returned by descriptor {descriptor}'s declared inventory operation",
        denominator_grain="descriptor item",
        denominator_process="census_substrate descriptor table plus transport; count materialized items after read",
        observed_at=observed_at,
        support_pointers=[f"{module_file.as_posix()} @ {_repo_commit(repo_root)}"],
        control_references=["org/modules/graph/tests/test_census_substrate.py"],
        invalidation_predicates=["descriptor row changes", "transport implementation changes", "provider response vintage changes"],
    )
    if not module_file.is_file():
        return build_record(
            **base,
            status={"acquisition": "ABSENT", "transport": "NOT_ATTEMPTED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"},
            denominator_count=None,
            substantive_value=0,
            unknown_reason=f"census_substrate module absent: {module_file}",
            traversal_residue=[str(module_file)],
        )
    try:
        module = _load_census_module(module_file)
        census = module.build_descriptor_census(
            descriptor, tool="NFRA_EPISTEMY.C1-ENVELOPE", _runner=runner
        )
    except KeyError as exc:
        return build_record(
            **base,
            status={"acquisition": "ABSENT", "transport": "NOT_ATTEMPTED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"},
            denominator_count=None,
            substantive_value=[],
            unknown_reason=f"descriptor acquisition absent: {exc}",
            traversal_residue=[str(exc)],
        )
    except Exception as exc:  # typed source exceptions are mapped by their declared class name
        name = type(exc).__name__
        if name == "CliNotFound":
            status = {"acquisition": "ABSENT", "transport": "NOT_ATTEMPTED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"}
        elif name == "CliCallFailed":
            status = {"acquisition": "FAILED", "transport": "NOT_ATTEMPTED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"}
        elif name == "CliEmptyStdout":
            status = {"acquisition": "PRESENT", "transport": "FAILED", "enumeration": "NOT_ATTEMPTED", "parse": "NOT_ATTEMPTED"}
        elif isinstance(exc, json.JSONDecodeError):
            status = {"acquisition": "PRESENT", "transport": "SUCCEEDED", "enumeration": "NOT_ATTEMPTED", "parse": "FAILED"}
        else:
            status = {"acquisition": "UNKNOWN", "transport": "UNKNOWN", "enumeration": "UNKNOWN", "parse": "UNKNOWN"}
        return build_record(
            **base,
            status=status,
            denominator_count=None,
            substantive_value="PASS",
            unknown_reason=f"census_substrate {name}: {exc}",
            traversal_residue=[f"{name}: {exc}"],
        )
    count = census.get("summary", {}).get("item_count")
    if not isinstance(count, int) or count < 0:
        return build_record(
            **base,
            status={"acquisition": "PRESENT", "transport": "SUCCEEDED", "enumeration": "FAILED", "parse": "SUCCEEDED"},
            denominator_count=None,
            substantive_value=0,
            unknown_reason="census summary lacks a non-negative item_count",
            traversal_residue=[],
        )
    items_digest = "sha256:" + hashlib.sha256(canonical_bytes(census.get("items", []))).hexdigest()
    return build_record(
        **base,
        status={"acquisition": "PRESENT", "transport": "SUCCEEDED", "enumeration": "SUCCEEDED", "parse": "SUCCEEDED"},
        denominator_count=count,
        substantive_value={"summary": census["summary"], "meta": census.get("_meta", {}), "items_digest": items_digest},
        unknown_reason="",
        traversal_residue=[],
    )
