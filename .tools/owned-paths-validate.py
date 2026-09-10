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
import os
import re
import subprocess
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


# ADHC_OWNPTH.005 (2026-09-04): THE TASK ORDER IS THE WORKER'S GRANT -- Andrew-direct ~04:58Z at the 1.0.0_SA_CTO terminal,
# "recs approved" on /open-calls CALL 1 REC (c), record @9ef9a40aae. A spine-v3 worker 0.9.0_WK_<CODE>~<n> is enumerated in
# NO lane; it is admitted to exactly the paths that a NON-TERMINAL task order under <CODE>, issued_to that serial, names in its
# <paths> block AT HEAD -- and to nothing else. Fifth additive clause, consulted only after enumeration, tilde-strip, the
# home-folder and the tree-deliverables conventions all fail; never revokes. THE SWITCH is the registry's `worker_grant:`
# stanza (0.0.0_AB_MSTR as grantor, SoD): absent, no worker is admitted anywhere; present, the order decides. Reads HEAD, never
# the worktree -- the worker's own commit flips its order to complete in the same commit, and HEAD still carries it open.
# A census that cannot run admits nothing (fail-closed). Rationale, measured: v3's first drain (worker ~2, 2026-09-04
# 03:5xZ) committed both real surfaces its order named through the audited override because no lane admitted it.
_WORKER_SERIAL_RE = re.compile(r"^0\.9\.0_WK_(?P<code>[A-Z0-9_]+?)[~_](?P<n>[0-9]+)$")
# ANCHORED AT LINE START 2026-09-10 (3.0.0_SA_CVO~Z, row Z-S15 graduated at C-S16). The bare
# form was applied with .search(), so it took the FIRST occurrence anywhere in the file --
# INCLUDING INSIDE PROSE. TO-IAM-t-3's text reads "Carries NO <status> tag at all" while
# DESCRIBING A DIFFERENT DOCUMENT, so the gate captured "tag", failed to find it among the
# terminal words, and declared a COMPLETE order non-terminal. The order whose subject is
# whether status tags mean anything is the one misread on its own status tag.
# GENERAL FORM: A FIRST-MATCH READ OF A STRUCTURED FIELD ASSUMES THE FIELD APPEARS BEFORE ANY
# DISCUSSION OF IT. True of most documents; false for exactly the documents that are ABOUT the
# field -- which are the ones this estate writes when it audits its own markup.
# WHY ANCHORED AND NOT PAIRED, MEASURED OVER 208 TASK ORDERS BEFORE CHOOSING:
#   requiring </status>  -> REGRESSES 131 of 208. Most orders never close the tag; the "obvious"
#                          fix would have been far worse than the defect.
#   last-match           -> works, but changes the verdict on 2 files for the benefit of 1.
#   LINE-ANCHORED        -> 0 regressions, and disagrees with the old form on EXACTLY ONE file:
#                          the defective one. A real tag starts its line; a prose mention does not.
# DUPLICATED IN .tools/owned-paths-validate.py AS _TO_STATUS_RE -- two carriers of one pattern,
# fixed identically in the same commit. Naming it because the next edit must move both.
_TO_STATUS_RE = re.compile(r"^\s*<status>\s*([A-Za-z_-]+)", re.I | re.M)
_TO_ISSUED_TO_RE = re.compile(r"<issued_to>\s*([^<\n]+?)\s*</issued_to>", re.I)
# line-anchored (94157 gap (a)): the tag alone on its line opens the block; a prose mention is not the block
_TO_PATHS_RE = re.compile(r"^[ \t]*<paths>[ \t]*\r?\n(.*?)^[ \t]*</paths>[ \t]*$", re.S | re.I | re.M)
_TERMINAL_TO_WORDS = ("complete", "completed", "closed", "done", "superseded", "cancelled", "canceled", "withdrawn")


def _paths_block_entries(text: str) -> list[str]:
    """The <paths> block's entries: one per line, absolute from the repo root, '#' lines ignored, backslashes normalized."""
    m = _TO_PATHS_RE.search(text or "")
    if not m:
        return []
    out = []
    for line in m.group(1).splitlines():
        e = line.strip().strip("`").strip()
        if not e or e.startswith("#"):
            continue
        out.append(e.replace("\\", "/").lstrip("/"))
    return out


def _order_grants(path: str, entries: list[str]) -> bool:
    """PURE. True iff one entry names `path`: exactly, as a glob (fnmatch, only when the entry carries * ? [), or as a
    directory prefix (an entry ending in '/'). Never a prefix by accident: 'org/a' does not grant 'org/ab'."""
    p = path.replace("\\", "/").lstrip("/")
    for e in entries:
        if e == p:
            return True
        if any(ch in e for ch in "*?[") and fnmatch.fnmatch(p, e):
            return True
        if e.endswith("/") and p.startswith(e):
            return True
    return False


def _worker_orders(root: str, code: str):
    """[(to_path, issued_to, entries)] for the project's NON-TERMINAL tree task orders at HEAD; None when git could not
    answer (the caller fails closed). Terminal orders grant nothing: a finished order is not a standing permission."""
    try:
        ls = subprocess.run(["git", "ls-files", "--", "org/missions/D*/*/%s/task-orders/*.md" % code], cwd=root,
                            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    except Exception as exc:  # noqa: BLE001
        print("WARN: worker-grant census raised %s -- admitting nothing" % exc, file=sys.stderr)
        return None
    if ls.returncode != 0:
        print("WARN: worker-grant census git ls-files rc=%d -- admitting nothing" % ls.returncode, file=sys.stderr)
        return None
    orders = []
    for p in [x.strip().replace("\\", "/") for x in ls.stdout.splitlines() if x.strip()]:
        try:
            show = subprocess.run(["git", "show", "HEAD:%s" % p], cwd=root, capture_output=True, text=True,
                                  encoding="utf-8", errors="replace", timeout=60)
        except Exception as exc:  # noqa: BLE001
            print("WARN: worker-grant census git show raised %s on %s -- admitting nothing" % (exc, p), file=sys.stderr)
            return None
        if show.returncode != 0:
            continue   # a task order staged but absent at HEAD grants nothing yet
        text = show.stdout
        sm = _TO_STATUS_RE.search(text)
        if sm and sm.group(1).lower() in _TERMINAL_TO_WORDS:
            continue
        im = _TO_ISSUED_TO_RE.search(text)
        if not im:
            continue
        orders.append((p, im.group(1).strip(), _paths_block_entries(text)))
    return orders


def _owns_task_order_paths(agent: str, path: str, grant, root: str | None, cache: dict | None = None) -> bool:
    """ADHC_OWNPTH.005. True iff `grant` is the registry's worker_grant stanza (source task-order-paths), `agent` matches its
    serial_glob and parses as 0.9.0_WK_<CODE>~<n>, and a non-terminal task order under <CODE> at HEAD, issued_to that serial,
    names `path` in its <paths> block. `cache` (per process) keeps the census to one read per project."""
    if not isinstance(grant, dict) or grant.get("source") != "task-order-paths" or not root:
        return False
    glob_ = str(grant.get("serial_glob") or "")
    if not glob_ or not (fnmatch.fnmatch(agent, glob_) or fnmatch.fnmatch(_normalize_serial(agent), glob_)):
        return False
    m = _WORKER_SERIAL_RE.match(agent.strip())
    if not m:
        return False
    code = m.group("code")
    if cache is None:
        cache = {}
    if code not in cache:
        cache[code] = _worker_orders(root, code)
    orders = cache[code]
    if orders is None:
        return False
    agent_norm = _normalize_serial(agent)
    for _to, issued_to, entries in orders:
        if _normalize_serial(issued_to) != agent_norm:
            continue
        if _order_grants(path, entries):
            return True
    return False


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
                paths_config: dict[str, Any], grant=None, root: str | None = None,
                cache: dict | None = None) -> bool:
    """Return True if agent is permitted to commit to path. `grant`/`root`/`cache` feed ADHC_OWNPTH.005 (the
    worker_grant stanza; the repo root for the HEAD read); the three older callers pass none and lose nothing."""
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
        # ADHC_OWNPTH.005 (2026-09-04, Andrew-direct "recs approved" @9ef9a40aae): the task order is the worker's
        # grant -- 5th clause, same additive-after posture. See _owns_task_order_paths.
        if _owns_task_order_paths(agent, path, grant, root, cache):
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
    grant = data.get("worker_grant")
    root = os.path.dirname(os.path.abspath(yaml_path))
    cache: dict = {}
    is_worker = bool(_WORKER_SERIAL_RE.match(agent.strip()))

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
        if not check_agent(agent, path, lanes, paths_config, grant, root, cache):
            lane = lanes.get(lane_name, {})
            desc = lane.get("description", "")
            why = ""
            if is_worker:
                why = (" -- WORKER: no worker_grant stanza in the registry" if not isinstance(grant, dict) else
                       " -- WORKER: no NON-TERMINAL task order at HEAD issued_to this serial names this path in its <paths> block"
                       " (ADHC_OWNPTH.005: the order is the grant; a missing path is a cut defect, never an override)")
            violations.append(
                f"VIOLATION: {path} -- lane={lane_name} ({desc}); "
                f"agent={agent} not in permitted_agents{why}"
            )

    for v in violations:
        print(v)

    return 1 if violations else 0


def _self_test(yaml_path: str) -> int:
    """ADHC_OWNPTH.005 battery: pure arms on the grant resolution, red and green, plus a live parse of a real project's
    orders at HEAD. The registry's stanza is INJECTED for the arms (the real one is 0.0.0_AB_MSTR's to land), so the
    battery grades the limb, not the registry."""
    grant = {"serial_glob": "0.9.0_WK_*", "source": "task-order-paths"}
    root = os.path.dirname(os.path.abspath(yaml_path))
    WK = "0.9.0_WK_X_PRJ~2"
    orders = [("org/missions/D9/X/X_PRJ/task-orders/X_PRJ.TO-1.md", "0.9.0_WK_X_PRJ~2",
               ["org/modules/graph/cli.py", ".tools/tests/test_x_*.py", "docs/x/"])]
    cache = {"X_PRJ": orders}
    own = lambda agent, path, g=grant, c=cache: _owns_task_order_paths(agent, path, g, root, c)  # noqa: E731
    arms = [
        ("entries: exact path granted", lambda: _order_grants("org/modules/graph/cli.py", orders[0][2])),
        ("entries: glob granted; directory prefix granted", lambda: _order_grants(".tools/tests/test_x_battery.py", orders[0][2])
         and _order_grants("docs/x/deep/file.md", orders[0][2])),
        ("entries MUTANT: a sibling file is NOT a prefix match (org/modules/graph/cli.py vs cli.pyc); an unlisted file refused",
         lambda: not _order_grants("org/modules/graph/cli.pyc", orders[0][2]) and not _order_grants("infra/aws/x.tf", orders[0][2])),
        ("block parser: one entry per line, comments and blanks ignored, backticks stripped",
         lambda: _paths_block_entries("x\n<paths>\n  org/a.py\n\n  # note\n  `.tools/b.sh`\n</paths>\ny") == ["org/a.py", ".tools/b.sh"]),
        ("block parser: no block -> no entries (an order without <paths> grants nothing)", lambda: _paths_block_entries("<status>open</status>") == []),
        ("block parser: a prose mention of <paths> before the block is skipped; the block is read (94157 gap (a))",
         lambda: _paths_block_entries("the `<paths>` block names the grant\n<paths>\norg/ok.py\n</paths>\n") == ["org/ok.py"]),
        ("grant: worker ~2 on a path its order names -> admitted", lambda: own(WK, "org/modules/graph/cli.py")),
        ("grant: worker ~2 on a path its order does not name -> refused", lambda: not own(WK, "org/modules/graph/other.py")),
        ("grant MUTANT: worker ~3 (another slot) on ~2's path -> refused", lambda: not own("0.9.0_WK_X_PRJ~3", "org/modules/graph/cli.py")),
        ("grant MUTANT: a seat serial never resolves through the order", lambda: not own("2.0.0_SA_COO", "org/modules/graph/cli.py")),
        ("grant: the underscore author form 0.9.0_WK_X_PRJ_2 resolves to the same worker", lambda: own("0.9.0_WK_X_PRJ_2", "org/modules/graph/cli.py")),
        ("switch: no stanza -> nothing admitted; wrong source -> nothing admitted",
         lambda: not own(WK, "org/modules/graph/cli.py", None) and not own(WK, "org/modules/graph/cli.py", {"serial_glob": "0.9.0_WK_*", "source": "lanes"})),
        ("fail-closed: a census that could not run (None) admits nothing", lambda: not _owns_task_order_paths(WK, "org/modules/graph/cli.py", grant, root, {"X_PRJ": None})),
        ("terminal orders grant nothing (live parse of NFRA_COMPEFFICACY at HEAD returns a list; every order in it is non-terminal)",
         lambda: isinstance(_worker_orders(root, "NFRA_COMPEFFICACY"), list)),
    ]
    failed = 0
    for name, fn in arms:
        ok = False
        try:
            ok = bool(fn())
        except Exception as exc:  # noqa: BLE001
            name += " (raised %s: %s)" % (type(exc).__name__, exc)
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
        failed += 0 if ok else 1
    live = _worker_orders(root, "NFRA_COMPEFFICACY")
    if live is None:
        print("  LIVE  NFRA_COMPEFFICACY census DID NOT RUN")
        failed += 1
    else:
        wk = [(os.path.basename(p), who, len(e)) for p, who, e in live if _WORKER_SERIAL_RE.match(who)]
        print("  LIVE  NFRA_COMPEFFICACY: %d non-terminal order(s) at HEAD; issued to a worker: %d -- %s"
              % (len(live), len(wk), "; ".join("%s -> %s (%d path entries)" % t for t in wk) or "-"))
    data = load_yaml(yaml_path)
    print("  REGISTRY worker_grant stanza: %s" % ("PRESENT (%s)" % data.get("worker_grant") if isinstance(data.get("worker_grant"), dict) else "ABSENT -- no worker admitted anywhere until 0.0.0_AB_MSTR lands it"))
    print("RESULT: %d arm(s) failed of %d (+ live census)" % (failed, len(arms)))
    return 1 if failed else 0


def main() -> None:
    args = sys.argv[1:]

    if args and args[0] == "--self-test":
        sys.exit(_self_test(args[1] if len(args) > 1 else ".owned-paths.yaml"))

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
