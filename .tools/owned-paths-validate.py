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
import re
import sys
from typing import Any


def _normalize_serial(serial: str) -> str:
    """Bridge tilde-form lane suffix to underscore-form for membership comparison.

    Per memory feedback_author_serial_no_tilde.md, the git author MUST be
    underscore form (e.g. ``0.4.0_DS_ClientPlatform_B``) -- CLAUDE.md restricts
    author fields to alphanumeric/./_/@ -- but YAML config uses tilde form
    (e.g. ``0.4.0_DS_ClientPlatform~B``) for MCP/broker readability. Both refer
    to the same agent identity; normalization bridges the comparison without
    forcing either side to change. ADHC_OWNPTH.009 (2026-04-27).
    """
    return re.sub(r"~([A-Za-z0-9]+)$", r"_\1", serial)


def _home_folder_tier_dirs(paths_config: dict) -> set[str]:
    """Closed set of tier-dirs for the home-folder convention (ADHC_OWNPTH.003).

    Derived from the YAML's OWN path rules at load (single source -- no hardcoded
    drifting copy), gated to tier-prefixed dirs (``^tier\\d``) so the convention can
    ONLY ever apply under a real tier home-dir. This closes the one abuse vector CTO
    flagged (arch-GO 170100Z Q1): an open ``org/*/<serial>/`` wildcard -- a path like
    ``org/EVIL/<serial>/logs`` can never match because EVIL is not a tier-dir the YAML
    enumerates. Returns e.g. {tier0, tier1_exec, tier2_senior, tier3_junior, tier3_rd}.
    """
    dirs: set[str] = set()
    for pattern in paths_config:
        parts = pattern.replace("\\", "/").lstrip("/").split("/")
        if len(parts) >= 2 and parts[0] == "org" and re.match(r"^tier\d", parts[1]):
            dirs.add(parts[1])
    return dirs


def _owns_home_folder(agent_norm: str, agent_base: str, path: str,
                      tier_dirs: set[str]) -> bool:
    """Home-folder convention (ADHC_OWNPTH.003, CTO arch-GO 170100Z).

    True iff `path` is the committer's OWN home folder:
        org/<tier-dir>/<SERIAL>/(logs|task_orders)/**
    where <tier-dir> is in the YAML-derived closed set and <SERIAL> EQUALS the
    committer's base identity (self if a base serial; tilde-stripped base if a ~lane).

    SAFETY (the load-bearing point CTO confirmed): the grant is to the committer's OWN
    folder ONLY -- <SERIAL> must equal the committer's own (stripped) serial, so agent A
    can never reach agent B's folder. Scope is (logs|task_orders) ONLY -- deliverables /
    other subtrees stay enumeration-gated. Relocation-proof: matches the <SERIAL> path
    component, not a fixed tier prefix (tier3_rd -> tier3_junior moves never reopen it).
    """
    p = path.replace("\\", "/").lstrip("/").split("/")
    if not (len(p) >= 4 and p[0] == "org" and p[1] in tier_dirs
            and p[3] in ("logs", "task_orders")):
        return False
    path_serial = p[2]
    # committer IS the home-folder serial (a base committing its own folder), OR
    # is a ~lane of it (stripped base equals the path serial). A true base's stripped
    # form is a non-serial (e.g. 0.3.1_RD) that cannot equal a real <SERIAL>, so the
    # tilde branch never false-permits a base against another agent's folder.
    if path_serial == agent_norm:
        return True
    if agent_base != agent_norm and path_serial == agent_base:
        return True
    return False


_TREE_DELIV_RE = re.compile(r"^org/missions/[^/]+/[^/]+/[^/]+/deliverables/([^/]+)/.+")


def _owns_tree_deliverables(agent_norm: str, agent_base: str, path: str) -> bool:
    """Project-tree deliverables convention (ADHC_OWNPTH.004, 2026-09-02; spec s.6 option ii,
    Andrew-ruled ~20:0xZ "deliverables/{serial}/ sub-folders"; CTO builds it under the COO/CTO
    prerequisite split @a8d63f097c).

    True iff `path` is org/missions/<D>/<MACRO>/<PROJECT>/deliverables/<SERIAL>/** and <SERIAL> is
    the committer's own identity (self, or the tilde-stripped base of a ~lane). The PATH carries the
    owner, so the TO's `to:` value never has to be resolved by a path gate -- the "one hard part" of
    s.6 closed by convention, same posture as the home-folder clause: additive, consulted only after
    enumeration fails, never revokes, and can never reach another serial's folder. A file directly
    under deliverables/ (no serial folder) matches nothing here and stays refused.
    """
    m = _TREE_DELIV_RE.match(path.replace("\\", "/").lstrip("/"))
    if not m:
        return False
    owner = _normalize_serial(m.group(1))
    if owner == agent_norm:
        return True
    return agent_base != agent_norm and owner == agent_base


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
        agent_norm = _normalize_serial(agent)
        permitted_norm = {_normalize_serial(p) for p in permitted}
        if agent_norm in permitted_norm:
            return True
        # RV-0030 F-003 (2026-06-08, ws CTO): tilde/underscore lane-suffix
        # auto-permit. A spawned work lane (e.g. 0.4.0_DE_ClientPlatform~A ->
        # normalized 0.4.0_DE_ClientPlatform_A) is the SAME agent identity as its
        # base serial, so it is permitted wherever the base serial is enumerated.
        # This eliminates the recurring per-session "lane X blocked on its own
        # home-folder logs/**" BLOCK class without unbounded per-lane YAML adds.
        # SAFE BY CONSTRUCTION:
        #   - additive-only: consulted solely AFTER exact match fails, so it can
        #     never REVOKE a previously-allowed commit;
        #   - grants only to a genuine lane of an already-permitted base: enumerated
        #     entries are always full serials, so the stripped form (drop one
        #     trailing _<alnum> lane segment) can equal an enumerated entry ONLY
        #     when the committer is literally <that-base>~<lane> -- no cross-agent
        #     leak (a true base serial strips to a non-serial like 0.4.0_DE that
        #     matches nothing).
        agent_base = re.sub(r"_[A-Za-z0-9]+$", "", agent_norm)
        if agent_base != agent_norm and agent_base in permitted_norm:
            return True
        # ADHC_OWNPTH.003 (2026-06-26, ws CTO arch-GO 170100Z): home-folder convention --
        # 3rd clause, consulted ONLY after exact-match + tilde-strip both fail (additive-
        # after, same posture as RV-0030 F-003: never REVOKES an allow). A serial (base or
        # ~lane) is permitted on its OWN home folder org/<tier>/<SERIAL>/(logs|task_orders)/**
        # by CONVENTION -- ends the enumeration whack-a-mole (a new pod/agent never needs an
        # ANY_POD add to commit its own logs/TOs). SAFE: grants the committer's OWN folder
        # only (<SERIAL> must equal the committer's stripped base); closed YAML-derived
        # tier-dir set (no org/*/ wildcard); scoped to logs+task_orders only.
        if _owns_home_folder(agent_norm, agent_base, path,
                             _home_folder_tier_dirs(paths_config)):
            return True
        # ADHC_OWNPTH.004 (2026-09-02): the project tree's deliverables/<SERIAL>/ convention -- 4th
        # clause, same additive-after posture. See _owns_tree_deliverables.
        if _owns_tree_deliverables(agent_norm, agent_base, path):
            return True
        return False

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
