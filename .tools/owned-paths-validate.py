#!/usr/bin/env python3
"""
ADHC_OWNPTH.002 -- Owned-paths path resolver and YAML validator.

Parses .owned-paths.yaml (PRD §6.1) and resolves file paths to
ownership lanes using longest-match-wins glob semantics.

CLI modes:
  owned-paths-validate.py <yaml>
      Validate YAML structure; exit 0 if valid, 1 with errors.

  owned-paths-validate.py --check-agent <agent> <yaml>
      Read file paths from stdin (one per line). For each path, resolve
      its lane and check if <agent> is in permitted_agents. Print
      VIOLATION: lines for unauthorized paths. Exit 0 if no violations,
      1 if any violations found.
"""
from __future__ import annotations

import fnmatch
import sys
from typing import Any

try:
    import yaml as _yaml
    def _load_yaml(path: str) -> dict:
        with open(path, encoding="utf-8") as f:
            return _yaml.safe_load(f) or {}
except ImportError:
    def _load_yaml(path: str) -> dict:
        raise SystemExit(
            "ERROR: PyYAML is required. Install: pip install pyyaml"
        )


def load_yaml(yaml_path: str) -> dict[str, Any]:
    return _load_yaml(yaml_path)


def resolve_lane(path: str, paths_config: dict[str, Any]) -> str | None:
    """
    Longest-match-wins glob resolution.

    Normalizes path separators, then iterates patterns sorted by length
    descending (longer = more specific). Returns lane name or None if
    no pattern matches.
    """
    path = path.replace("\\", "/").lstrip("/")

    # Longest pattern first = most specific match wins
    sorted_patterns = sorted(paths_config.keys(), key=len, reverse=True)
    for pattern in sorted_patterns:
        norm_pattern = pattern.replace("\\", "/")
        if fnmatch.fnmatch(path, norm_pattern):
            entry = paths_config[pattern]
            if isinstance(entry, dict):
                return entry.get("lane")
    return None


def check_agent(agent: str, path: str, lanes: dict[str, Any],
                paths_config: dict[str, Any]) -> bool:
    """Return True if agent is permitted to commit to path."""
    lane_name = resolve_lane(path, paths_config)
    if lane_name is None:
        return False  # unmapped path

    lane = lanes.get(lane_name, {})
    permitted = lane.get("permitted_agents", [])

    if permitted == "*":
        return True

    if isinstance(permitted, list):
        return agent in permitted

    return False


def validate_yaml(yaml_path: str) -> list[str]:
    """
    Validate .owned-paths.yaml structure.
    Returns list of error strings (empty list = valid).
    """
    errors: list[str] = []
    try:
        data = load_yaml(yaml_path)
    except Exception as exc:
        return [f"YAML parse error: {exc}"]

    if not isinstance(data, dict):
        return ["Top-level YAML value is not a mapping"]

    lanes = data.get("lanes") or {}
    paths = data.get("paths") or {}

    if not lanes:
        errors.append("No lanes defined under 'lanes:'")

    if not paths:
        errors.append("No paths defined under 'paths:'")

    # Verify all path entries reference a known lane
    for pattern, config in paths.items():
        if not isinstance(config, dict):
            errors.append(f"Path '{pattern}': expected mapping, got {type(config).__name__}")
            continue
        lane_name = config.get("lane")
        if lane_name is None:
            errors.append(f"Path '{pattern}': missing 'lane' key")
        elif lane_name not in lanes:
            errors.append(f"Path '{pattern}': unknown lane '{lane_name}' (not in lanes section)")

    return errors


def _cmd_validate(yaml_path: str) -> int:
    errors = validate_yaml(yaml_path)
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1
    data = load_yaml(yaml_path)
    n_lanes = len(data.get("lanes") or {})
    n_paths = len(data.get("paths") or {})
    print(f"OK: {yaml_path} -- {n_lanes} lanes, {n_paths} path rules, all lane refs resolve")
    return 0


def _cmd_check_agent(agent: str, yaml_path: str) -> int:
    """
    Read file paths from stdin (one per line). Print VIOLATION: for each
    path the agent is not permitted to touch. Exit 1 if any violations.
    """
    errors = validate_yaml(yaml_path)
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1

    data = load_yaml(yaml_path)
    lanes = data.get("lanes") or {}
    paths_config = data.get("paths") or {}

    violations: list[str] = []
    for line in sys.stdin:
        path = line.strip()
        if not path:
            continue
        lane_name = resolve_lane(path, paths_config)
        if lane_name is None:
            violations.append(
                f"VIOLATION: {path} -- UNDEFINED (no matching path rule; agent={agent})"
            )
            continue
        if not check_agent(agent, path, lanes, paths_config):
            lane = lanes.get(lane_name, {})
            desc = lane.get("description", "")
            violations.append(
                f"VIOLATION: {path} -- lane={lane_name} ({desc}); "
                f"agent={agent} not in permitted_agents"
            )

    for v in violations:
        print(v)

    return 1 if violations else 0


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print(
            f"Usage: {sys.argv[0]} <yaml>  |  "
            f"{sys.argv[0]} --check-agent <agent> <yaml>",
            file=sys.stderr,
        )
        sys.exit(1)

    if args[0] == "--check-agent":
        if len(args) < 3:
            print(
                f"Usage: {sys.argv[0]} --check-agent <agent> <yaml>",
                file=sys.stderr,
            )
            sys.exit(1)
        agent = args[1]
        yaml_path = args[2]
        sys.exit(_cmd_check_agent(agent, yaml_path))
    else:
        yaml_path = args[0]
        sys.exit(_cmd_validate(yaml_path))


if __name__ == "__main__":
    main()
