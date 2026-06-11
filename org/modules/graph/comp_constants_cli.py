#!/usr/bin/env python3
"""
comp-constants — constant-drift indexer + drift gate + discovery surface.

ADHC_COMPIL_V4.003 — AE 0.7.0 2026-05-08.

Subcommands:
  check [--file PATH]    Drift detection. Exit 1 on drift, 0 on clean.
  index                  Re-scan + rewrite sites[] in config from current AST scan.
  new                    Discover ALL_CAPS_SNAKE constants in scan but not in config.
  list                   Print current config (debug surface).

AST extraction (Python only; JS/TS deferred to v2):
  ast.parse() per file -> walk module-level ast.Assign + ast.AnnAssign nodes ->
  match Name(id ALL_CAPS) targets -> extract value via ast.literal_eval for
  str/int/float/list/set/frozenset/dict literals. For os.environ.get(name, default),
  record env_backed=True and the default literal.
"""
from __future__ import annotations

import argparse
import ast
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml


WORKSPACE_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_CONFIG_PATH = WORKSPACE_ROOT / "comp-constants.config.yaml"

# Constant name pattern: must start with capital, all caps + underscores + digits.
ALL_CAPS_RE = re.compile(r"^[A-Z][A-Z0-9_]+$")

# Utility-blacklist: skip these in `new` discovery (they are infra knobs, not marker constants).
UTILITY_BLACKLIST_PATTERNS = [
    r"^(BUFFER|RETRY|TIMEOUT|MAX|MIN|DEFAULT|TEST|SAMPLE)_",
    r"^(LOG|CONFIG|API|HTTP|HTTPS|JSON|YAML|TLS|SSL)_",
    r"_(LIMIT|SIZE|COUNT|TIMEOUT|RETRIES|INTERVAL|DELAY)$",
    r"^(VERSION|VERSION_INFO|__VERSION__|__ALL__)$",
    r"^_+",
]


def _is_utility_constant(name: str) -> bool:
    return any(re.match(p, name) for p in UTILITY_BLACKLIST_PATTERNS)


@dataclass
class Site:
    file: str
    line: int
    value: str
    env_backed: bool = False
    drift: bool = False

    def to_dict(self) -> dict:
        d: dict = {"file": self.file, "line": self.line, "value": self.value}
        if self.env_backed:
            d["env_backed"] = True
        if self.drift:
            d["drift"] = True
        return d


def _value_repr(node: ast.AST) -> str | None:
    """Return repr of literal at node, or None if not a literal we extract."""
    try:
        v = ast.literal_eval(node)
        return repr(v)
    except (ValueError, TypeError, SyntaxError):
        return None


def _extract_env_default(node: ast.Call) -> str | None:
    """If node is os.environ.get(name, default), return repr(default); else None."""
    func = node.func
    is_env_get = (
        isinstance(func, ast.Attribute)
        and func.attr == "get"
        and isinstance(func.value, ast.Attribute)
        and func.value.attr == "environ"
        and isinstance(func.value.value, ast.Name)
        and func.value.value.id == "os"
    )
    if not is_env_get:
        return None
    if len(node.args) >= 2:
        return _value_repr(node.args[1])
    return None


def _site_for(file_path: Path, line: int, value: str, env_backed: bool) -> Site:
    try:
        rel = file_path.relative_to(WORKSPACE_ROOT)
    except ValueError:
        rel = file_path
    return Site(
        file=str(rel).replace("\\", "/"),
        line=line,
        value=value,
        env_backed=env_backed,
    )


def extract_constants(file_path: Path) -> list[tuple[str, Site]]:
    """Walk file's module-level assigns; return [(name, Site), ...] for each ALL_CAPS const."""
    try:
        source = file_path.read_text(encoding="utf-8", errors="replace")
        tree = ast.parse(source, filename=str(file_path))
    except (SyntaxError, OSError):
        return []

    out: list[tuple[str, Site]] = []

    for node in tree.body:
        # Plain assignment: NAME = value or NAME = NAME2 = value
        if isinstance(node, ast.Assign):
            value_repr = _value_repr(node.value)
            env_backed = False
            if value_repr is None and isinstance(node.value, ast.Call):
                default = _extract_env_default(node.value)
                if default is not None:
                    value_repr = default
                    env_backed = True
            if value_repr is None:
                continue
            for target in node.targets:
                if isinstance(target, ast.Name) and ALL_CAPS_RE.match(target.id):
                    out.append((
                        target.id,
                        _site_for(file_path, node.lineno, value_repr, env_backed),
                    ))
        # Annotated assignment: NAME: type = value
        elif isinstance(node, ast.AnnAssign):
            if node.value is None:
                continue
            target = node.target
            if not isinstance(target, ast.Name) or not ALL_CAPS_RE.match(target.id):
                continue
            value_repr = _value_repr(node.value)
            env_backed = False
            if value_repr is None and isinstance(node.value, ast.Call):
                default = _extract_env_default(node.value)
                if default is not None:
                    value_repr = default
                    env_backed = True
            if value_repr is None:
                continue
            out.append((
                target.id,
                _site_for(file_path, node.lineno, value_repr, env_backed),
            ))

    return out


def _expand_search_surfaces(config: dict) -> dict[str, set[Path]]:
    """Return {lane: set(paths)} from per-lane glob patterns. Python only."""
    by_lane: dict[str, set[Path]] = {}
    surfaces = config.get("search_surfaces", {}) or {}
    for lane, patterns in surfaces.items():
        lane_paths: set[Path] = set()
        for pat in patterns or []:
            if not (pat.endswith(".py") or "*.py" in pat):
                continue
            for p in WORKSPACE_ROOT.glob(pat):
                if p.is_file() and p.suffix == ".py":
                    lane_paths.add(p)
        by_lane[lane] = lane_paths
    return by_lane


def _path_lane(path_norm: str, lane_paths: dict[str, set[Path]]) -> str | None:
    """Determine which lane a file belongs to based on lane_paths membership."""
    for lane, paths in lane_paths.items():
        for p in paths:
            try:
                rel = str(p.relative_to(WORKSPACE_ROOT)).replace("\\", "/")
            except ValueError:
                rel = str(p).replace("\\", "/")
            if rel == path_norm:
                return lane
    return None


def scan_all(config: dict, only_file: Path | None = None) -> dict[tuple[str, str | None], list[Site]]:
    """Scan all configured search_surfaces; return {(name, lane): [Site, ...]}.

    Lane is determined by which search_surfaces glob the site file matched.
    If only_file is given, lane is None (caller filters).
    """
    lane_paths = _expand_search_surfaces(config)
    file_to_lane: dict[Path, str] = {}
    for lane, paths in lane_paths.items():
        for p in paths:
            file_to_lane[p] = lane

    by_key: dict[tuple[str, str | None], list[Site]] = {}
    if only_file is not None:
        files = [only_file] if only_file.is_file() and only_file.suffix == ".py" else []
    else:
        files = sorted(file_to_lane.keys())

    for fp in files:
        lane = file_to_lane.get(fp)  # may be None for --file outside any surface
        for name, site in extract_constants(fp):
            by_key.setdefault((name, lane), []).append(site)
    return by_key


_COMMA_INT_RE = re.compile(r"^\s*\d+(\s*,\s*\d+)+\s*$")


def _to_normalized_set(v: object) -> frozenset[str] | None:
    """Normalize a collection or comma-string-of-ints to frozenset of str element reprs.

    Returns None if v is not a collection/comma-string (caller falls back to ==).
    """
    if isinstance(v, (set, frozenset, list, tuple)):
        return frozenset(str(x) for x in v)
    if isinstance(v, str) and _COMMA_INT_RE.match(v):
        return frozenset(p.strip() for p in v.split(","))
    return None


def _values_equivalent(a: str, b: str) -> bool:
    """Compare two value reprs, normalizing for set/frozenset/list/comma-string semantics.

    Equivalent IF:
      - Direct == on literal_eval values, OR
      - Both reduce to same frozenset of stringified element reprs (handles type-form drift:
        {3,6} <-> [3,6] <-> '3,6' <-> {'3','6'} all normalize to frozenset({'3','6'})).
    """
    try:
        va = ast.literal_eval(a)
        vb = ast.literal_eval(b)
    except (ValueError, SyntaxError, TypeError):
        return a.strip() == b.strip()
    # Direct equality first
    try:
        if va == vb:
            return True
    except (TypeError, ValueError):
        pass
    # Set-semantics normalization (catches int-set vs str-set vs list vs comma-string)
    na = _to_normalized_set(va)
    nb = _to_normalized_set(vb)
    if na is not None and nb is not None:
        return na == nb
    return False


def _load_config(path: Path) -> dict:
    if not path.exists():
        sys.stderr.write(f"ERROR: config not found: {path}\n")
        sys.exit(2)
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------

def cmd_check(args: argparse.Namespace, config: dict) -> int:
    """Drift detection. Exit 1 on drift, 0 on clean. Lane-aware.

    ADHC_COMPIL_V4.021 Cat 3.4: --lane filter restricts to one lane (bd/inf/multifirm).
    """
    only_file = None
    if getattr(args, "file", None):
        fp = Path(args.file)
        if not fp.is_absolute():
            fp = (WORKSPACE_ROOT / fp).resolve()
        only_file = fp

    only_lane = getattr(args, "lane", None)

    scanned = scan_all(config, only_file=only_file)

    drifts: list[tuple[str, Site, str]] = []
    for c in config.get("constants", []):
        name = c["name"]
        canonical_value = c.get("canonical_value")
        lane = c.get("lane")
        if canonical_value is None:
            continue
        if only_lane is not None and lane != only_lane:
            continue
        # Pull only sites scanned under this constant's lane
        sites_for_const = scanned.get((name, lane), [])
        # If --file specified, only_file's lane-key is None (it bypasses surface filter)
        if only_file is not None:
            sites_for_const = scanned.get((name, None), []) + sites_for_const
        for s in sites_for_const:
            if not _values_equivalent(s.value, canonical_value):
                drifts.append((name, s, canonical_value))

    if not drifts:
        if only_file is None:
            scope = f" (lane={only_lane})" if only_lane else ""
            print(f"OK: no drift detected across {len(config.get('constants', []))} constant(s){scope}")
        return 0

    print(f"DRIFT: {len(drifts)} site(s) diverge from canonical_value\n")
    for name, s, canonical in drifts:
        print(f"  {s.file}:{s.line} :: {name}")
        print(f"    actual:    {s.value}")
        print(f"    canonical: {canonical}")
    return 1


def cmd_index(args: argparse.Namespace, config: dict) -> int:
    """Re-scan + rewrite sites[] in config; preserve notes/canonical_value/lane.

    Lane-aware: only considers sites within the constant's lane's search_surfaces.
    """
    scanned = scan_all(config)
    updated_constants = []
    for c in config.get("constants", []):
        name = c["name"]
        canonical = c.get("canonical_value")
        lane = c.get("lane")
        new_sites = sorted(scanned.get((name, lane), []), key=lambda s: (s.file, s.line))
        site_dicts = []
        for s in new_sites:
            d = s.to_dict()
            if canonical is not None and not _values_equivalent(s.value, canonical):
                d["drift"] = True
            site_dicts.append(d)
        c_out = {**c, "sites": site_dicts}
        updated_constants.append(c_out)
    config["constants"] = updated_constants

    path = Path(args.config)
    path.write_text(
        yaml.safe_dump(config, sort_keys=False, allow_unicode=True, width=200),
        encoding="utf-8",
    )
    print(f"OK: rewrote sites for {len(updated_constants)} constant(s) in {path}")
    return 0


def cmd_new(args: argparse.Namespace, config: dict) -> int:
    """Discover ALL_CAPS_SNAKE constants in scan but NOT in config (per-lane)."""
    scanned = scan_all(config)
    # known_per_lane[lane] = set(names)
    known_per_lane: dict[str, set[str]] = {}
    for c in config.get("constants", []):
        known_per_lane.setdefault(c.get("lane", ""), set()).add(c["name"])

    candidates: dict[tuple[str, str], list[Site]] = {}
    for (name, lane), sites in scanned.items():
        if lane is None:
            continue
        if name in known_per_lane.get(lane, set()):
            continue
        if _is_utility_constant(name):
            continue
        candidates[(name, lane)] = sites

    if not candidates:
        print("No new candidates found.")
        return 0

    print(f"DISCOVERED: {len(candidates)} candidate constant(s) not in config:\n")
    for (name, lane), sites in sorted(candidates.items()):
        print(f"  [{lane}] {name}  ({len(sites)} site(s))")
        for s in sites[:3]:
            print(f"    {s.file}:{s.line} = {s.value}")
        if len(sites) > 3:
            print(f"    ... and {len(sites) - 3} more")
    return 0


def cmd_list(args: argparse.Namespace, config: dict) -> int:
    """Print current config summary (debug)."""
    print(f"Config: {args.config}")
    surfaces = config.get("search_surfaces", {}) or {}
    surface_count = sum(len(v or []) for v in surfaces.values())
    print(f"Search surfaces: {surface_count} pattern(s) across {len(surfaces)} lane(s)")
    constants = config.get("constants", []) or []
    print(f"Constants: {len(constants)}")
    for c in constants:
        sites = c.get("sites", []) or []
        drift_count = sum(1 for s in sites if s.get("drift"))
        marker = f" ({drift_count} drift)" if drift_count else ""
        lane = c.get("lane", "?")
        print(f"  [{lane:9s}] {c['name']:32s} {len(sites)} site(s){marker}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="comp-constants")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH))
    sub = parser.add_subparsers(dest="cmd")

    p_check = sub.add_parser("check", help="drift detection (default)")
    p_check.add_argument("--file", help="only check sites in this file")
    p_check.add_argument("--lane", choices=["bd", "inf", "cot", "multifirm"],
                         help="filter to one lane (V4.021 Cat 3.4; cot added NFRA_DTAFLP TO-4)")
    p_check.set_defaults(func=cmd_check)

    p_index = sub.add_parser("index", help="rewrite sites[] in config")
    p_index.set_defaults(func=cmd_index)

    p_new = sub.add_parser("new", help="discover unindexed constants")
    p_new.set_defaults(func=cmd_new)

    p_list = sub.add_parser("list", help="print current config")
    p_list.set_defaults(func=cmd_list)

    args = parser.parse_args()

    if not args.cmd:
        args.cmd = "check"
        args.file = None
        args.lane = None
        args.func = cmd_check

    config = _load_config(Path(args.config))
    return args.func(args, config)


if __name__ == "__main__":
    sys.exit(main())
