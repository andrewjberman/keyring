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
    set_subset_check  -- ADHC_COMPIL_V4.009: artifact field's distinct values must contain
                         all elements of canonical set; supports symbolic $CONSTANT_NAME
                         resolution via comp-constants.config.yaml at config-load time
"""

from __future__ import annotations

import ast
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Symbolic-rule resolver (ADHC_COMPIL_V4.009 Phase 3)
# Supports $CONSTANT_NAME references in check rule param values; resolved at
# config-load time via comp-constants.config.yaml lookup.
# ---------------------------------------------------------------------------

_SYMBOLIC_TOKEN_RE = re.compile(r"^\$([A-Z][A-Z0-9_]+)$")


class SymbolicResolutionError(Exception):
    """Raised when $CONSTANT_NAME cannot be resolved (constant not in comp-constants config)."""

    def __init__(self, name: str, sites: list[str] | None = None):
        self.name = name
        self.sites = sites or []
        super().__init__(f"Symbolic constant ${name} not found in comp-constants.config.yaml")


def _load_comp_constants_canonical(workspace_root: Path) -> dict[str, Any]:
    """Load {name: parsed_canonical_value} from comp-constants.config.yaml.

    Returns empty dict if config absent (rule resolution will then raise on first $<NAME>).
    """
    cfg_path = workspace_root / "comp-constants.config.yaml"
    if not cfg_path.exists():
        return {}
    try:
        import yaml
        raw = yaml.safe_load(cfg_path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}
    out: dict[str, Any] = {}
    for c in raw.get("constants", []) or []:
        name = c.get("name")
        canonical = c.get("canonical_value")
        if not name or canonical is None:
            continue
        # canonical is stored as a Python repr; parse via ast.literal_eval
        try:
            out[name] = ast.literal_eval(canonical)
        except (ValueError, SyntaxError, TypeError):
            # Fall back to raw string
            out[name] = canonical
    return out


def _resolve_symbolic(value: Any, canonical_map: dict[str, Any]) -> Any:
    """Recursively resolve $CONSTANT_NAME tokens in value.

    Only resolves exact-match tokens (`$NAME` as a complete string value). Embedded
    references (e.g., `prefix-$NAME-suffix`) are NOT resolved per CTO ruling Q3
    (param values only; prose/free-text strings unchanged).

    Raises SymbolicResolutionError if a referenced constant is absent from the map
    (CTO ruling Q2: missing canonical -> ERROR, never silent drift).
    """
    if isinstance(value, str):
        m = _SYMBOLIC_TOKEN_RE.match(value)
        if not m:
            return value
        name = m.group(1)
        if name not in canonical_map:
            raise SymbolicResolutionError(name)
        return canonical_map[name]
    if isinstance(value, list):
        return [_resolve_symbolic(v, canonical_map) for v in value]
    if isinstance(value, dict):
        return {k: _resolve_symbolic(v, canonical_map) for k, v in value.items()}
    return value


def _resolve_check_symbolics(check: dict, canonical_map: dict[str, Any]) -> dict:
    """Resolve symbolic refs in check params; preserve `why:` and `name:` (prose) verbatim.

    Per CTO ruling Q3: symbolic resolution applies to param values only, not prose fields.
    """
    PROSE_KEYS = {"name", "why", "comment"}
    out = {}
    for k, v in check.items():
        if k in PROSE_KEYS:
            out[k] = v
        else:
            out[k] = _resolve_symbolic(v, canonical_map)
    return out


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

def load_validate_config(
    workspace_root: Path,
    config_file: Path | None = None,
) -> dict[str, ValidateConfig]:
    """Load gold_validate_config.yaml for BD (default) or INF pipeline.

    Pass config_file explicitly to load the INF config:
        load_validate_config(ws, ws / "data/orion/scripts/gold/gold_validate_config.yaml")
    Omit or pass None to load the BD config (backward-compatible default).
    """
    if config_file is None:
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

    # Load comp-constants canonical map for symbolic-rule resolution (ADHC_COMPIL_V4.009 Phase 3)
    canonical_map = _load_comp_constants_canonical(workspace_root)

    configs = {}
    for script_id, data in (raw.get("scripts") or {}).items():
        if not data:
            continue
        # Resolve $CONSTANT_NAME tokens in check param values; if a constant is missing,
        # tag the check with a sentinel so the runner can emit a clear ERROR (Q2 ruling).
        resolved_checks: list[dict] = []
        for c in (data.get("checks") or []):
            try:
                resolved_checks.append(_resolve_check_symbolics(c, canonical_map))
            except SymbolicResolutionError as e:
                resolved_checks.append({
                    **c,
                    "_symbolic_error": str(e),
                    "_symbolic_missing": e.name,
                })
        configs[script_id] = ValidateConfig(
            script_id=script_id,
            primary_artifact=data.get("primary_artifact"),
            checks=resolved_checks,
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

    # Symbolic-resolution failure surfaced from config-load (CTO Q2: ERROR-class)
    if check.get("_symbolic_error"):
        return CheckResult(
            name=name, severity="ERROR", status="ERROR",
            message=f"Symbolic constant ${check['_symbolic_missing']} not found in "
                    f"comp-constants.config.yaml — cannot evaluate this rule",
            detail="Add the constant to comp-constants.config.yaml, or remove the symbolic reference.",
        )

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

        elif check_type == "set_subset_check":
            return _check_set_subset(name, severity, check, artifact)

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


def _check_set_subset(name, severity, check, artifact) -> CheckResult:
    """Check that distinct values at path contain (superset) the canonical set.

    ADHC_COMPIL_V4.009 Phase 3 — supports symbolic $CONSTANT_NAME resolution
    (already substituted at config-load by _resolve_check_symbolics).

    Config schema:
        type: set_subset_check
        path: artifact.json.path[*].field
        canonical_set: $INFLECTION_REP_IDS  # or [3, 6, 11, 12] literal
        mode: superset    # default; artifact >= canonical (extras allowed)
              equal       # artifact == canonical exactly
        normalize: int    # cast each artifact value to int before comparing (handles str rep_ids)
    """
    path = check.get("path", "")
    canonical_set = check.get("canonical_set")
    mode = check.get("mode", "superset")
    normalize = check.get("normalize")

    if canonical_set is None:
        return CheckResult(name=name, severity="ERROR", status="ERROR",
                           message="set_subset_check missing canonical_set parameter")

    # Normalize canonical to a Python set
    canonical = set(canonical_set) if isinstance(canonical_set, (list, tuple, set, frozenset)) else {canonical_set}

    vals = _resolve_path(artifact, path)
    if not vals:
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"Path not found: '{path}'",
                           detail=check.get("why", ""))

    # Flatten + collect distinct values from artifact path
    actual: set = set()
    for v in vals:
        if isinstance(v, (list, tuple, set, frozenset)):
            actual.update(v)
        else:
            actual.add(v)

    # Apply normalize transform
    if normalize == "int":
        normalized: set = set()
        for v in actual:
            try:
                normalized.add(int(v))
            except (ValueError, TypeError):
                pass
        actual = normalized

    if mode == "equal":
        if actual == canonical:
            return CheckResult(name=name, severity=severity, status="PASS",
                               message=f"distinct values at '{path}' = canonical set ({len(canonical)} elements)")
        missing = canonical - actual
        extra = actual - canonical
        msg_parts = []
        if missing:
            msg_parts.append(f"missing {sorted(missing)}")
        if extra:
            msg_parts.append(f"extra {sorted(extra)}")
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"set diverges (mode=equal): {'; '.join(msg_parts)}",
                           detail=check.get("why", ""))
    else:  # superset (default)
        missing = canonical - actual
        if not missing:
            return CheckResult(name=name, severity=severity, status="PASS",
                               message=f"distinct values at '{path}' contain canonical set ({len(canonical)} elements)")
        return CheckResult(name=name, severity=severity, status="FAIL",
                           message=f"missing canonical elements: {sorted(missing)}",
                           detail=check.get("why", ""))


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
