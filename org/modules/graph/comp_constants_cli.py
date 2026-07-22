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
from pathlib import Path, PurePosixPath

import yaml

# NFRA_TOOLPASS C7: SOVEREIGN_HELD_MARKERS is derived from sovereign_held (the canonical leaf) instead of
# a local literal tuple. Dual import (relative in package context, else add own dir + bare) -- comp-constants
# runs standalone (python comp_constants_cli.py, incl. the subprocess-based fixtures) and as a package.
try:
    from .sovereign_held import HELD_PATH_MARKERS as _HELD_PATHS, HELD_BUCKET_PREFIXES as _HELD_BUCKETS
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from sovereign_held import HELD_PATH_MARKERS as _HELD_PATHS, HELD_BUCKET_PREFIXES as _HELD_BUCKETS


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


def _declared_file_lane(file_path: Path, config: dict) -> str | None:
    """Resolve a lane for a file that no search_surface glob matched, from the
    config's `file_lanes:` block ({lane: [glob, ...]}).

    WHY THIS EXISTS: a file in a SHARED tree (e.g. data/assets/scripts/gold/, which
    holds producers for several firms) has no lane derivable from its directory --
    a directory rule there would be actively WRONG, silently re-homing one firm's
    producer under another firm's canonical. Such a file's lane must be DECLARED.
    Firm onboarding is an explicit registration step, not an inference.
    """
    try:
        rel = str(file_path.relative_to(WORKSPACE_ROOT)).replace("\\", "/")
    except ValueError:
        rel = str(file_path).replace("\\", "/")
    for lane, patterns in (config.get("file_lanes") or {}).items():
        for pat in patterns or []:
            if PurePosixPath(rel).match(str(pat).replace("\\", "/")):
                return lane
    return None


def scan_all(config: dict, only_file: Path | None = None) -> dict[tuple[str, str | None], list[Site]]:
    """Scan all configured search_surfaces; return {(name, lane): [Site, ...]}.

    Lane is determined by which search_surfaces glob the site file matched, falling
    back to an explicit `file_lanes:` declaration. A file matching neither keys under
    lane None -- UNRESOLVED, which cmd_check reports rather than comparing (comparing
    an unresolved file against every lane is what produced the false-drift class).
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
        lane = file_to_lane.get(fp)
        if lane is None:
            lane = _declared_file_lane(fp, config)  # shared-tree files declare their lane
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
    checked_sites = 0          # CC1: how many tracked-constant sites we actually compared
    checked_names: set[str] = set()
    for c in config.get("constants", []):
        name = c["name"]
        canonical_value = c.get("canonical_value")
        lane = c.get("lane")
        if canonical_value is None:
            continue
        if only_lane is not None and lane != only_lane:
            continue
        # Pull only sites scanned under this constant's lane.
        #
        # The removed line here was `if only_file is not None: sites += scanned[(name, None)]`.
        # A --file target outside every search_surface resolved to lane None, and that line fanned
        # its sites against EVERY lane's canonical for that name -- so with FIRM_ID registered in
        # bd/inf/cot, any single file necessarily "drifted" from the two firms it is not. It reported
        # DRIFT: 2 on a CORRECT file and, with >=2 canonicals, could not do otherwise: a genuinely
        # new firm was unrepresentable. Unresolved sites are now REPORTED (below), never compared.
        sites_for_const = scanned.get((name, lane), [])
        for s in sites_for_const:
            checked_sites += 1
            checked_names.add(name)
            if not _values_equivalent(s.value, canonical_value):
                drifts.append((name, s, canonical_value))

    # UNRESOLVED-LANE census. A file matching no search_surface and no file_lanes declaration has an
    # undetermined lane, so NO canonical applies to it. That is a COVERAGE gap ("I did not check this"),
    # NOT a drift finding ("I checked and it is wrong") -- conflating the two in either direction is the
    # bug this replaced. It is therefore LOUD but NON-BLOCKING: 57 files estate-wide are in this state,
    # so blocking would wedge the commit gate, while silence would report unchecked as clean.
    #
    # WRITTEN TO STDERR ON PURPOSE: commit_gate_runner._comp_constants_check captures stdout and prints
    # it ONLY when rc != 0, so a stdout advisory would be swallowed at the one place it must be seen.
    tracked = {c["name"] for c in config.get("constants", []) if c.get("canonical_value") is not None}
    unresolved = [(n, s) for (n, ln), sites in scanned.items() if ln is None and n in tracked
                  for s in sites]
    if unresolved:
        sys.stderr.write(
            "UNRESOLVED-LANE: %d tracked constant-site(s) NOT CHECKED -- no search_surface or "
            "file_lanes declaration resolves a lane for them, so no canonical applies:\n" % len(unresolved))
        for n, s in sorted(unresolved, key=lambda t: (t[1].file, t[1].line)):
            sys.stderr.write(f"  {s.file}:{s.line} :: {n} = {s.value}\n")
        sys.stderr.write(
            "  -> declare the file's lane under `file_lanes:` in the config to bring it under the gate.\n")

    if not drifts:
        if only_file is None:
            scope = f" (lane={only_lane})" if only_lane else ""
            print(f"OK: no drift detected across {len(config.get('constants', []))} constant(s){scope}")
        elif checked_sites:
            # CC1: --file previously printed NOTHING on a clean result, so rc0 was silently
            # ambiguous between "checked, all clean" and "no tracked constant here". Disambiguate.
            suffix = f"; {len(unresolved)} site(s) UNRESOLVED, not checked" if unresolved else ""
            print(f"OK: no drift -- checked {checked_sites} tracked constant-site(s) "
                  f"({len(checked_names)} constant(s)) in {args.file}{suffix}")
        elif unresolved:
            # NOT "no tracked constants found" -- they were found, they were just not CHECKABLE.
            # Saying "nothing to check" here would report an unresolved file as a clean one, which is
            # the same did-not-look-rendered-as-looked-and-fine collapse this whole change removes.
            print(f"UNCHECKED: {len(unresolved)} tracked constant-site(s) found in {args.file} but "
                  f"NOT checked -- lane unresolved (see UNRESOLVED-LANE on stderr). This is a coverage "
                  f"gap, not a clean result.")
        else:
            print(f"OK: no tracked constants found in {args.file} -- "
                  f"0 of {len(config.get('constants', []))} config constant(s) appear here, nothing to check")
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


# ---------------------------------------------------------------------------
# CC2 sovereign-held-surface guard (NFRA_TOOLPASS).
#
# comp-constants ast-parses EVERY file in EVERY search_surface on any full run
# (bare `check`, `--lane`, `new`, `index`). `--lane` scopes the COMPARISON
# (cmd_check filters constants by lane), never the SCAN -- scan_all(only_file=None)
# globs+parses all surfaces. So a config whose search_surfaces include a
# sovereign-held path (e.g. data/black_diamond/) makes this tool a LATENT
# bd-scanner for ANY caller. This guard makes the hold STRUCTURAL: it REFUSES
# (exit 3) any full-scan invocation that would ast-parse a held surface, and any
# `check --file` whose target is itself under a held path. `check --file <non-held>`
# stays allowed (only_file scopes the scan to that one file). Override:
# --allow-held-scan (loud stderr WARN; the wrapper logs the command string).
# ---------------------------------------------------------------------------
# C7: derived from sovereign_held (path markers + bucket prefixes) -- preserves the historical CONFLATED
# set (comp_constants matches both path + bucket substrings). Superset of the old 4 (adds the more-specific
# data/canonical/schwab/silver/, redundant with schwab/silver/) -> behavior-preserving.
#
# LIFTED 2026-07-22 (0.8.0_AE_CloudComp), executing the Andrew-direct retraction of 2026-07-14 ~03:3xZ to
# COO, verbatim: "Oh that is retarded, 49 is back on the menu now, take the sovereign block off completely,
# that is no excuse to not verify the work."  The tuple below WAS the 2026-07-09 49F/Schwab/bd sovereign
# block; it lifts with it. This mirrors .tools/_comprail.py:230 (HELD_PREFIXES = ()), which 1.0.0_SA_CTO
# lifted on 2026-07-14 -- that file's own comment names "the comp-constants CC2 guard" as its mirror, and
# the mirror was missed, so this guard kept enforcing a dead prohibition for 8 days. It refused EVERY
# full-scan mode (bare check, --lane <any>, new, index) for ALL lanes -- bd's 12 and inf's 11 registered
# constants had no working drift gate, and `index`/`new` were dead. Only `check --file` survived, which is
# why the commit gate kept working and nobody noticed.
#
# THE GUARD MACHINERY STAYS: a future hold is a one-line re-add here (re-point at the retained tuple), and
# --allow-held-scan / the REFUSE paths keep working unchanged. The INF-chain hold is a SEPARATE mechanism
# (frozen individual FILES + Door 5/6) and is deliberately not expressible here. Firm separation
# (NEVER#2 / Rule 13) is a DIFFERENT control, gate- and IAM-enforced, and is untouched by this lift.
_RETRACTED_20260709_MARKERS = tuple(_HELD_PATHS) + tuple(_HELD_BUCKETS)  # retained for re-arm; NOT enforced
SOVEREIGN_HELD_MARKERS: tuple[str, ...] = ()


def _active_held_markers(config: dict) -> tuple[str, ...]:
    """The markers this invocation enforces. A config may DECLARE a hold via
    `sovereign_held_markers:`; otherwise the module default applies (currently ()
    -- retracted 2026-07-14, see SOVEREIGN_HELD_MARKERS above).

    This is the re-arm surface: it keeps the guard MACHINERY exercisable (and
    testable) after the 2026-07-09 hold was lifted, so a future hold is a
    declaration rather than a rebuild. A guard you cannot re-arm is not a fix."""
    declared = config.get("sovereign_held_markers")
    if declared:
        return tuple(str(m) for m in declared)
    return SOVEREIGN_HELD_MARKERS


def _held_surface_hits(config: dict) -> list[tuple[str, str]]:
    """Return [(lane, glob_pattern), ...] for every search_surface glob naming a
    sovereign-held path. Pure STRING check on the config patterns -- it does NOT
    glob or read any file, so calling it never touches a held path."""
    markers = _active_held_markers(config)
    hits: list[tuple[str, str]] = []
    for lane, patterns in (config.get("search_surfaces") or {}).items():
        for pat in patterns or []:
            norm = str(pat).replace("\\", "/")
            if any(m in norm for m in markers):
                hits.append((lane, str(pat)))
    return hits


def _held_path_hit(path_norm: str, config: dict | None = None) -> str | None:
    """Return the first held marker that path_norm falls under, else None."""
    for m in _active_held_markers(config or {}):
        if m in path_norm:
            return m
    return None


def _refuse(msg: str) -> "None":
    """Emit a refusal on BOTH streams, then exit 3. NEVER returns.

    STDOUT IS NOT OPTIONAL HERE. This previously wrote to stderr only, leaving stdout EMPTY -- so
    `out=$(comp-constants check --lane cot)` and any `2>/dev/null` caller received a clean-empty
    result from a scan that never ran, and a REFUSAL rendered as a PASS. Same class as the CLAUDE.md
    `git show <bad-ref> 2>/dev/null` mangle: the failure signal is discarded and the absence reads as
    success. A refusal must be distinguishable from a clean result on EVERY channel a caller might
    read -- exit code (3, vs 0 clean / 1 drift), stdout, and stderr. (CTO GO, 2026-07-22.)"""
    print(msg)                     # stdout: a stdout-only caller must never see empty-means-clean
    sys.stderr.write(msg + "\n")   # stderr: preserves the existing loud-operator channel
    sys.exit(3)


def _sovereign_guard(args: argparse.Namespace, config: dict) -> None:
    """REFUSE (exit 3) any invocation that would ast-parse a sovereign-held surface,
    UNLESS --allow-held-scan is passed. Makes the bd hold structural, not procedural.

    Runs BEFORE any scan, and decides purely from the config patterns + the --file
    argument -- so a refusal never touches a held path itself."""
    if getattr(args, "allow_held_scan", False):
        held = _held_surface_hits(config)
        if held:
            sys.stderr.write(
                "WARN: OVERRIDE -- sovereign-held-surface guard bypassed via --allow-held-scan; "
                "scanning held surface(s): %s\n" % ", ".join(f"{ln}:{p}" for ln, p in held))
        return
    cmd = getattr(args, "cmd", "check") or "check"
    if cmd == "list":
        return  # config-only, no ast.parse
    only_file = getattr(args, "file", None)
    if cmd == "check" and only_file:
        # scan is scoped to this one file; refuse only if the file itself is held.
        norm = str(Path(only_file)).replace("\\", "/")
        m = _held_path_hit(norm, config)
        if m:
            _refuse(
                "REFUSE: SOVEREIGN-HELD -- --file target is under held path '%s'. comp-constants "
                "will not ast-parse it. Pass --allow-held-scan to override (audited)." % m)
        return  # non-held --file: scan is scoped to this one file, so the surface check below
                # must NOT apply. Dropping this return makes every `check --file` refuse whenever
                # ANY surface is held -- caught by test_check_file_non_held_is_allowed.
    # full-scan modes (bare check / --lane / new / index): scan_all globs+parses ALL surfaces.
    held = _held_surface_hits(config)
    if held:
        surfaces = ", ".join(f"{ln}:{p}" for ln, p in held)
        _refuse(
            "REFUSE: SOVEREIGN-HELD -- comp-constants '%s' would ast-parse sovereign-held "
            "search_surface(s): %s. Only `check --file <non-held>` is permitted under the hold. "
            "Pass --allow-held-scan to override (audited)." % (cmd, surfaces))


def main() -> int:
    parser = argparse.ArgumentParser(prog="comp-constants")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG_PATH))
    parser.add_argument("--allow-held-scan", action="store_true",
                        help="override the sovereign-held-surface guard (AUDITED -- logged by the wrapper)")
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
    _sovereign_guard(args, config)
    return args.func(args, config)


if __name__ == "__main__":
    sys.exit(main())
