"""
Gold artifact invariant validator.

Checks declared invariants from gold_validate_config.yaml against a
local artifact file (JSON or parquet) before it is uploaded to S3.

Usage (via validate_cli.py):
    comp-validate D_04 --artifact /tmp/leaderboard.json
    comp-validate D_00 --artifact /tmp/timeseries_chart.json
    comp-validate --list   # show all configured checks

Check types supported:
    key_present       -- top-level JSON key must exist (and be non-null, non-empty)
    count_min         -- array at path must have >= min_count elements
    field_nonzero     -- field at path must be > 0 (with optional filter on another field)
    sum_approx        -- two numeric values must be within tolerance_pct of each other
    no_null_numeric   -- no null/NaN values in numeric fields at path
    threshold_pct     -- at least pct% of array entries must satisfy a simple condition
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class CheckResult:
    name: str
    severity: str        # ERROR, WARN, INFO
    status: str          # PASS, FAIL, SKIP, ERROR
    message: str = ""
    detail: str = ""


@dataclass
class ValidateConfig:
    """Loaded configuration for one script's checks."""
    script_id: str
    primary_artifact: str | None
    checks: list[dict] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Config loader
# ---------------------------------------------------------------------------

def load_validate_config(workspace_root: Path) -> dict[str, ValidateConfig]:
    """Load gold_validate_config.yaml from the gold scripts directory."""
    config_file = workspace_root / "data" / "black_diamond" / "scripts" / "gold" / "gold_validate_config.yaml"
    if not config_file.exists():
        return {}

    try:
        import yaml
        raw = yaml.safe_load(config_file.read_text(encoding="utf-8"))
    except ImportError:
        # Fallback: minimal YAML parser for our specific structure
        raw = _parse_simple_yaml(config_file.read_text(encoding="utf-8"))
    except Exception:
        return {}

    configs = {}
    for script_id, data in (raw.get("scripts") or {}).items():
        if not data:
            continue
        configs[script_id] = ValidateConfig(
            script_id=script_id,
            primary_artifact=data.get("primary_artifact"),
            checks=data.get("checks") or [],
        )
    return configs


def _parse_simple_yaml(text: str) -> dict:
    """Minimal YAML parser for the specific gold_validate_config.yaml structure.
    Handles: scripts: { D_00: { primary_artifact: ..., checks: [...] } }
    Falls back gracefully -- returns empty dict on any ambiguity."""
    try:
        import yaml
        return yaml.safe_load(text)
    except ImportError:
        pass

    # Very minimal: just try to load as JSON if someone accidentally used JSON
    try:
        return json.loads(text)
    except Exception:
        pass

    return {}


# ---------------------------------------------------------------------------
# JSON path resolver
# ---------------------------------------------------------------------------

def _resolve_path(obj: Any, path: str) -> list[Any]:
    """Resolve a dot-notation path with optional [*] array iteration.

    Supports:
        "geo_drill"               -> obj["geo_drill"]
        "windows[0].entries"      -> obj["windows"][0]["entries"]
        "windows[*].entries"      -> [obj["windows"][i]["entries"] for each i]
        "windows[0].entries[*].fee_paying.aua" -> list of all fee_paying.aua values
    """
    results = [obj]

    # Split on dots, but preserve bracketed index parts
    # e.g. "windows[0].entries[*].aua" -> ["windows[0]", "entries[*]", "aua"]
    parts = re.split(r'\.(?![^\[]*\])', path)

    for part in parts:
        if not part:
            continue

        # Check for array index: "entries[0]" or "entries[*]"
        m = re.match(r'^(\w+)\[(\d+|\*)\]$', part)
        if m:
            key = m.group(1)
            idx = m.group(2)
            new_results = []
            for r in results:
                if not isinstance(r, dict) or key not in r:
                    continue
                val = r[key]
                if idx == '*':
                    if isinstance(val, list):
                        new_results.extend(val)
                elif isinstance(val, list):
                    i = int(idx)
                    if i < len(val):
                        new_results.append(val[i])
            results = new_results
        else:
            # Plain key access
            new_results = []
            for r in results:
                if isinstance(r, dict) and part in r:
                    new_results.append(r[part])
                elif isinstance(r, list):
                    # Implicit iteration over list elements
                    for item in r:
                        if isinstance(item, dict) and part in item:
                            new_results.append(item[part])
            results = new_results

    return results


# ---------------------------------------------------------------------------
# Check runners
# ---------------------------------------------------------------------------

def _run_check(check: dict, artifact: Any, artifact_path: str) -> CheckResult:
    """Run a single check against the artifact. Returns CheckResult."""
    name = check.get("name", "unnamed")
    severity = check.get("severity", "WARN").upper()
    check_type = check.get("type", "")
    why = check.get("why", "")

    try:
        if check_type == "key_present":
            return _check_key_present(name, severity, check, artifact)

        elif check_type == "count_min":
            return _check_count_min(name, severity, check, artifact)

        elif check_type == "field_nonzero":
            return _check_field_nonzero(name, severity, check, artifact)

        elif check_type == "sum_approx":
            return _check_sum_approx(name, severity, check, artifact)

        elif check_type == "no_null_numeric":
            return _check_no_null_numeric(name, severity, check, artifact)

        elif check_type == "threshold_pct":
            return _check_threshold_pct(name, severity, check, artifact)

        elif check_type == "script_check":
            # Source-level check -- skipped at runtime (handled by comp-pipescript)
            return CheckResult(name=name, severity=severity, status="SKIP",
                               message="Source-level check (use comp-pipescript io for this)")

        else:
            return CheckResult(name=name, severity=severity, status="SKIP",
                               message=f"Unknown check type: {check_type}")
    except Exception as e:
        return CheckResult(name=name, severity=severity, status="ERROR",
                           message=f"Check runner error: {e}")


def _check_key_present(name, severity, check, artifact) -> CheckResult:
    """Check that a JSON key exists and is non-null/non-empty."""
    path = check.get("path", "")
    vals = _resolve_path(artifact, path)
    if not vals:
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"Key absent: '{path}' not found in artifact",
                           detail=check.get("why", ""))
    val = vals[0]
    if val is None or val == {} or val == []:
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"Key present but empty: '{path}' = {val!r}",
                           detail=check.get("why", ""))
    return CheckResult(name=name, severity=severity, status="PASS",
                       message=f"Key '{path}' present ({type(val).__name__})")


def _check_count_min(name, severity, check, artifact) -> CheckResult:
    """Check that array at path has >= min_count elements."""
    path = check.get("path", "")
    min_count = check.get("min_count", 1)
    vals = _resolve_path(artifact, path)
    if not vals:
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"Path not found: '{path}'",
                           detail=check.get("why", ""))
    target = vals[0]
    if not isinstance(target, list):
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"Path '{path}' is not a list (got {type(target).__name__})")
    count = len(target)
    if count < min_count:
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"Count {count} < min {min_count} at '{path}'",
                           detail=check.get("why", ""))
    return CheckResult(name=name, severity=severity, status="PASS",
                       message=f"Count {count} >= {min_count} at '{path}'")


def _check_field_nonzero(name, severity, check, artifact) -> CheckResult:
    """Check that numeric field > 0, optionally filtering on another field >= threshold."""
    path = check.get("path", "")
    filter_field = check.get("filter_field", "")
    filter_threshold = check.get("filter_threshold", 0)

    values = _resolve_path(artifact, path)
    numeric_values = [v for v in values if isinstance(v, (int, float))]

    if not numeric_values:
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"No numeric values found at '{path}'",
                           detail=check.get("why", ""))

    if filter_field:
        # Get filter values and zip with target values
        filter_values = _resolve_path(artifact, filter_field)
        filter_nums = [v for v in filter_values if isinstance(v, (int, float))]
        if len(filter_nums) == len(numeric_values):
            filtered = [(v, f) for v, f in zip(numeric_values, filter_nums)
                        if f >= filter_threshold]
            if not filtered:
                return CheckResult(name=name, severity=severity, status="SKIP",
                                   message=f"No entries pass filter {filter_field} >= {filter_threshold}")
            zeros = [v for v, _ in filtered if v == 0]
            total = len(filtered)
        else:
            zeros = [v for v in numeric_values if v == 0]
            total = len(numeric_values)
    else:
        zeros = [v for v in numeric_values if v == 0]
        total = len(numeric_values)

    if zeros:
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"{len(zeros)}/{total} values are zero at '{path}'",
                           detail=check.get("why", ""))
    return CheckResult(name=name, severity=severity, status="PASS",
                       message=f"All {total} values > 0 at '{path}'")


def _check_sum_approx(name, severity, check, artifact) -> CheckResult:
    """Check that two numeric values are within tolerance_pct of each other."""
    path_a = check.get("path_a", "")
    path_b = check.get("path_b", "")
    tolerance_pct = check.get("tolerance_pct", 1.0)

    vals_a = _resolve_path(artifact, path_a)
    vals_b = _resolve_path(artifact, path_b)

    if not vals_a or not vals_b:
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"Path not found: a='{path_a}' ({len(vals_a)} vals), b='{path_b}' ({len(vals_b)} vals)")

    a = vals_a[0] if isinstance(vals_a[0], (int, float)) else None
    b = vals_b[0] if isinstance(vals_b[0], (int, float)) else None

    if a is None or b is None:
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"Non-numeric values: a={vals_a[0]!r}, b={vals_b[0]!r}")

    if b == 0:
        if a == 0:
            return CheckResult(name=name, severity=severity, status="PASS",
                               message="Both values are zero")
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"b=0 but a={a} (division by zero in tolerance check)")

    pct_diff = abs(a - b) / abs(b) * 100
    if pct_diff > tolerance_pct:
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"{path_a}={a:,.0f} vs {path_b}={b:,.0f}: {pct_diff:.1f}% difference > {tolerance_pct}% tolerance",
                           detail=check.get("why", ""))
    return CheckResult(name=name, severity=severity, status="PASS",
                       message=f"{path_a} vs {path_b}: {pct_diff:.2f}% difference (within {tolerance_pct}% tolerance)")


def _check_no_null_numeric(name, severity, check, artifact) -> CheckResult:
    """Check that no numeric fields at path contain null/NaN."""
    path = check.get("path", "")
    vals = _resolve_path(artifact, path)

    if not vals:
        return CheckResult(name=name, severity=severity, status="SKIP",
                           message=f"No values found at '{path}'")

    null_count = sum(1 for v in vals if v is None)
    nan_count = sum(1 for v in vals if isinstance(v, float) and v != v)  # NaN check
    total = len(vals)

    if null_count + nan_count > 0:
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"{null_count} null + {nan_count} NaN out of {total} values at '{path}'",
                           detail=check.get("why", ""))
    return CheckResult(name=name, severity=severity, status="PASS",
                       message=f"All {total} values non-null at '{path}'")


def _check_threshold_pct(name, severity, check, artifact) -> CheckResult:
    """Check that at least min_pct% of entries at path satisfy a simple > 0 or != null condition."""
    path = check.get("path", "")
    min_pct = check.get("min_pct", 90.0)
    condition = check.get("condition", "> 0")  # only "> 0" and "!= null" supported

    vals = _resolve_path(artifact, path)
    if not vals:
        return CheckResult(name=name, severity=severity, status="SKIP",
                           message=f"No values found at '{path}'")

    total = len(vals)
    if condition == "> 0":
        passing = sum(1 for v in vals if isinstance(v, (int, float)) and v > 0)
    elif condition == "!= null":
        passing = sum(1 for v in vals if v is not None)
    else:
        return CheckResult(name=name, severity=severity, status="SKIP",
                           message=f"Unsupported condition: {condition}")

    pct = passing / total * 100 if total > 0 else 0
    if pct < min_pct:
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"{pct:.1f}% ({passing}/{total}) satisfy '{condition}' at '{path}', need >= {min_pct}%",
                           detail=check.get("why", ""))
    return CheckResult(name=name, severity=severity, status="PASS",
                       message=f"{pct:.1f}% ({passing}/{total}) satisfy '{condition}' at '{path}'")


# ---------------------------------------------------------------------------
# Main runner
# ---------------------------------------------------------------------------

def run_validate(script_id: str, artifact_path: Path, configs: dict[str, ValidateConfig]) -> list[CheckResult]:
    """Run all checks for script_id against the artifact at artifact_path."""
    config = configs.get(script_id)
    if not config:
        # Try partial match
        matches = [k for k in configs if script_id.upper() in k.upper() or k.upper() in script_id.upper()]
        if len(matches) == 1:
            config = configs[matches[0]]
        elif not matches:
            return [CheckResult(
                name="config_lookup",
                severity="INFO",
                status="SKIP",
                message=f"No validate config found for '{script_id}'. Add checks to gold_validate_config.yaml."
            )]
        else:
            return [CheckResult(
                name="config_lookup",
                severity="INFO",
                status="SKIP",
                message=f"Multiple matches for '{script_id}': {matches}. Be more specific."
            )]

    if not artifact_path.exists():
        return [CheckResult(
            name="artifact_load",
            severity="ERROR",
            status="FAIL",
            message=f"Artifact file not found: {artifact_path}"
        )]

    # Load artifact
    try:
        suffix = artifact_path.suffix.lower()
        if suffix == '.json':
            artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
        elif suffix in ('.parquet', '.pq'):
            try:
                import pyarrow.parquet as pq
                table = pq.read_table(str(artifact_path))
                artifact = table.to_pydict()
            except ImportError:
                return [CheckResult(
                    name="artifact_load",
                    severity="ERROR",
                    status="FAIL",
                    message="pyarrow not installed -- cannot validate parquet files"
                )]
        else:
            return [CheckResult(
                name="artifact_load",
                severity="ERROR",
                status="FAIL",
                message=f"Unsupported artifact format: {suffix} (supported: .json, .parquet)"
            )]
    except Exception as e:
        return [CheckResult(
            name="artifact_load",
            severity="ERROR",
            status="FAIL",
            message=f"Failed to load artifact: {e}"
        )]

    if not config.checks:
        return [CheckResult(
            name="no_checks",
            severity="INFO",
            status="SKIP",
            message=f"No checks declared for {script_id}"
        )]

    results = []
    for check in config.checks:
        result = _run_check(check, artifact, str(artifact_path))
        results.append(result)
    return results
