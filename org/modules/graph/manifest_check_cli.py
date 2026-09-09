#!/usr/bin/env python3
"""
comp-manifest-check -- enforce the graph-call manifest at commit time.

NFRA_GRAPHS D6 (PRD docs/architecture/NFRA_GRAPHS.md). Scans a changed file's introduced
graph access and FLAGS any that:

  (A) call a manifest entry whose `status: deprecated`  -> name the `superseded_by` canonical
  (B) REBUILD (comp-aws derive / comp-build / --force) where a QUERY is canonical for the same
      use-case  -> point at the canonical query entry (the "never rebuild to answer a traversal
      a query can answer" rule)
  (C) re-implement / raw-access the graph (build_*_dag(), raw Cypher outside comp-kuzu,
      graph.json opened directly, a kuzu.Connection) instead of the canonical comp-* tool

It mirrors the comp-constants drift gate: a CLI under org/modules/graph/ + a .tools/ wrapper,
folded into ds-commit-gate.sh, with an advisory->blocking ramp controlled by
manifest_check_config.yaml (single `mode` knob).

Exit codes:
    0 -- advisory mode (always), OR blocking mode with no ERROR-class finding
    1 -- blocking mode with >=1 ERROR-class finding
    2 -- usage / config / manifest-load error

Subcommands:
    check [--file PATH ...] [--mode advisory|blocking]   scan file(s)
    list                                                 show detection surface + manifest state
    selfcheck                                            run on a synthetic anti-pattern (AC4)
"""

from __future__ import annotations

import argparse
import ast
import copy as _copy
import datetime as _dt
import json
import re
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - yaml ships in the local runtime
    sys.stderr.write("ERROR: PyYAML required (pip install pyyaml)\n")
    sys.exit(2)

_THIS_DIR = Path(__file__).resolve().parent
_WORKSPACE = _THIS_DIR.parent.parent.parent
_MANIFEST = _THIS_DIR / "graph-call-manifest.yaml"
_CONFIG = _THIS_DIR / "manifest_check_config.yaml"

# --- REGISTERED-IMPLIES-REACHABLE completeness invariant (NFRA_TOOLCHECK P3 follow-on) ----------
# CVO-endorsed 20260709T084324Z; CTO arch-gate 20260709T085322Z option (b); CTO verdict 085827Z:
# b2 (substrate-scoped) + ramp-EXEMPT.
#
# The invariant: every manifest tools_index tool must be routable=True in the capability provider,
# else comp_route.py's candidate filter drops it BEFORE scoring and no curated rule or vocabulary
# can ever surface it (the comp-fedobs + comp-system unreachable class -- both caught only by the
# LIVE oracle AFTER merge).
#
# THE GENERAL PATTERN (CTO, on the record 20260709T090333Z -- reusable beyond this gate):
#
#     A GLOBAL invariant folded into a PER-FILE gate triggers on the files that can INTRODUCE
#     the defect. Complete prevention, bounded blast-radius.
#
# b2 SUBSTRATE-SCOPED is that pattern applied here. The class can be introduced ONLY by editing one
# of the three files below, so scoping loses ZERO prevention (you cannot register an unroutable tool
# without touching one of them) while an unrelated commit never blocks on a break it did not cause.
# The alternative (b1, evaluate unconditionally) buys no extra prevention and adds a fabric-wide-halt
# failure mode -- not hypothetical: comp-coverage-check was RED at HEAD on one agent's unplaced tool
# while every OTHER agent's safe-commit printed its FAIL. Applies directly to the planned
# coverage-map-placement gate (a .tools/ commit must have a map home): same substrate-scoping.
#
# RAMP-EXEMPT: the advisory->blocking ramp exists for HEURISTIC checks with a false-positive class
# to shake out. This is a deterministic structural fact -- a tool is in the router's candidate set
# or it is not. A deterministic gate left on advisory prevents nothing until the flip. Blocks
# immediately, like py_compile.
_ROUTABLE_SUBSTRATE = (
    "org/modules/graph/graph-call-manifest.yaml",    # tools_index -- registers the tool
    "org/modules/graph/comp-coverage-map.yaml",      # tools[]/meta_tools[] -- sets the role
    "org/modules/graph/comp_capability_provider.py",  # _ROUTABLE_META_ROLES -- opts the role in
)

# ---------------------------------------------------------------------------------------------
# THE COMPLETENESS GATE FAMILY (CTO GO 20260709T094832Z; CVO-endorsed; COO~B concur)
#
# Three invariants, one shape: each is introduced only by an identifiable substrate, each was
# previously caught (if at all) only AFTER merge, and each blocks the AUTHOR at the moment they
# introduce it rather than red-bannering every other agent.
#
#   member 1  routable    registered  -> the router CAN score it   (candidate-set membership)
#   member 2  placement   a comp-tool -> has exactly one map home   (no UNPLACED / DOUBLE-PLACED)
#   member 3  self-routes catalogued  -> comp-which actually RETURNS it for its own use_case
#   member 4  existence   registered  -> the tool EXISTS on disk AND is tracked (it actually RUNS)
#
# member 4 exists because members 1+3 together still bind a PROXY. They prove the router names the
# tool; they do not prove the named command exists. On 2026-07-09 comp-system passed member 1 AND
# member 3 -- comp-which returned it RANK-1 for its own use_case -- while .tools/comp-system had
# never existed in the object graph (0 objects, all refs). The rail routed agents to
# `command not found`. "Routable" and "runnable" are different facts; only member 4 asserts the
# second. It also closes the 16-gitignored-tools class at its root (present-for-the-author,
# absent-from-a-fresh-clone), which no member could previously see.
#
# GOVERNING RULE (CTO, verbatim -- do not soften):
#     "every hard-blocking member asserts a DETERMINISTIC fact; anything threshold-shaped REPORTS."
#
# COMPLEMENTARITY, and the reason member 3 exists at all: members 1 and 2 assert NECESSARY
# conditions. A green necessary-check is NOT proof of the property. Membership does not imply
# reachability -- on 2026-07-09 comp-routable-check returned PASS over all 42 tools while the live
# oracle showed three of them unreachable, because vocabulary, not membership, was the defect.
# The family covers the DETERMINISTIC sub-classes; the LIVE ORACLE stays load-bearing for the
# vocabulary sub-class it structurally cannot see. Complementary, never redundant. Do not read a
# green gate as proof that a tool is reachable.
#
# COMMITTING-TREE UNIVERSE (CTO ratified 20260709T094435Z). Every member derives its universe from
# the files being COMMITTED, never from os.listdir of the working directory. We share ONE worktree,
# so a directory listing sees other agents' untracked, mid-authoring files: agent A's half-written
# .tools/comp-foo would block agent B's unrelated commit -- b1's fabric-wide blast radius through
# the back door, crying wolf at everyone except the author. (comp-coverage-check has exactly this
# defect today; fix filed to COO~B.)
# ---------------------------------------------------------------------------------------------

# member 2: only a .tools/comp-* add/rename/modify, or a coverage-map edit that removes a home,
# can create an UNPLACED or DOUBLE-PLACED tool.
_PLACEMENT_MAP = "org/modules/graph/comp-coverage-map.yaml"

# member 3: what the ROUTER scores against. A tools_index `does` edit is only ever the QUERY for
# its own tool, so it bounds to that tool (cost option (i), measured 1357ms/tool). Everything else
# here is part of the CORPUS the router ranks against, so it can move ANY tool's verdict and must
# re-check the full set (~57s). Boundaries read at source, not assumed:
#   * comp-which's fuzzy backstop iterates the manifest's `entries:` key, not tools_index
#   * the capability provider builds its keywords from comp-coverage-map concern text
_SELFROUTE_CORPUS = (
    "org/modules/graph/comp-coverage-map.yaml",       # provider keyword corpus
    "org/modules/graph/comp_capability_provider.py",  # candidate set
    ".tools/comp-which",                              # the router itself
)


# ----------------------------------------------------------------------------- detection surface
# Category B -- REBUILD tokens that have a cheaper QUERY canonical. Each maps to the manifest
# entry id(s) that ARE the canonical query alternative, so the message stays coupled to the
# manifest (validated at load: a referenced id missing from the manifest is reported by `list`).
# Token is matched only on a non-comment code line.
REBUILD_TOKENS = [
    {
        "pattern": re.compile(r"\bcomp-aws\b[^A-Za-z0-9]+derive\b"),
        "note": (
            "comp-aws derive is the 8-min REBUILD write-path. To ANSWER a lookup / reachability "
            "/ blast question, QUERY comp-kuzu instead. comp-aws derive is canonical ONLY for the "
            "scheduled refresh or a staleness-preempt (manifest cloud.derive.refresh)."
        ),
        "query_canonical": [
            "cloud.lookup.nodes_by_type",
            "cloud.reachability.transitive",
            "cloud.blast.what_breaks",
        ],
    },
    {
        "pattern": re.compile(r"\bcomp-build\b(?!.*--check)"),
        "note": (
            "comp-build is the ~9.8s trace-graph REBUILD. To answer a trace/blast query use the "
            "cached comp-trace / comp-blast. comp-build is canonical only after adding files "
            "(manifest trace.rebuild.refresh); comp-build --check verifies without rebuilding."
        ),
        "query_canonical": [
            "trace.walk.dependency_chain",
            "trace.blast.what_breaks",
        ],
    },
    {
        "pattern": re.compile(r"\bcomp-platinum\b.*--force\b"),
        "note": (
            "comp-platinum --force triggers a full per-firm rebuild. Warm comp-platinum is a "
            "cache read (manifest trace.fullstack.component_to_gold). --force only on a "
            "known-stale firm DAG."
        ),
        "query_canonical": ["trace.fullstack.component_to_gold"],
    },
]

# Category C -- raw / re-implemented graph access bypassing the canonical comp-* tool.
# Matched only on non-comment code lines (a docstring/comment showing the anti-pattern as a
# "don't" example must not trip the gate).
ADHOC_PATTERNS = [
    {
        "id": "build_dag_call",
        "pattern": re.compile(r"\bbuild_\w*_dag\s*\("),
        "note": (
            "calls a graph-DAG builder directly. The canonical query path is comp-pipescript "
            "(pipeline DAG) or comp-kuzu (cross-layer) -- manifest trace.pipeline.gold_dag / "
            "xlayer.fullstack.firm_component_to_bucket. Re-implementing a use-case the manifest "
            "covers."
        ),
    },
    {
        "id": "derive_graph_call",
        "pattern": re.compile(r"\b(derive_cloud_graph|derive_aws_graph)\s*\("),
        "note": (
            "calls the cloud-graph derive internals directly. Query comp-kuzu against the "
            "persisted graph (manifest cloud.*); the derive write-path is comp-aws derive "
            "(scheduled/staleness-preempt only)."
        ),
    },
    {
        "id": "raw_cypher",
        "pattern": re.compile(r"""['"]\s*MATCH\s*\("""),
        "note": (
            "embeds raw Cypher outside comp-kuzu. Route graph queries through comp-kuzu so they "
            "hit the SERVED graph projection through the thin client (manifest "
            "cloud.lookup.nodes_by_type / cloud.read.served_vintage / "
            "xlayer.fullstack.firm_component_to_bucket); the local persisted Kuzu DB is RETIRED "
            "(NFRA_CLDGRPH CG-s-8)."
        ),
    },
    {
        "id": "graph_json_open",
        "pattern": re.compile(r"""(open\s*\(|Path\s*\([^)]*\)\s*\.\s*(read_text|open))[^\n]*graph\.json"""),
        "note": (
            "reads graph.json (the trace-graph cache) directly. Query via the cached comp-trace "
            "/ comp-blast instead of parsing the cache file (manifest trace.*)."
        ),
    },
    {
        "id": "kuzu_connection",
        "pattern": re.compile(r"\bkuzu\.(Database|Connection)\s*\("),
        "note": (
            "opens a Kuzu connection directly. Use comp-kuzu, which owns the canonical DB path + "
            "load freshness (manifest cloud.* / xlayer.*)."
        ),
    },
]

_COMMENT_PREFIXES = ("#", "//", "*", '"""', "'''")


def _is_comment_line(stripped: str) -> bool:
    return stripped.startswith(_COMMENT_PREFIXES)


# ------------------------------------------------------------------------------------ load layer
# PER-PROCESS YAML CACHE (3.0.0_SA_CVO 2026-07-28, Andrew-direct, /seams-validated).
#
# WHY: cProfile on the live module -- cmd_check on ONE file = 3.048s, of which
# _completeness_invariants 2.728s (90%) and yaml.safe_load x12 = 2.683s (88%). The gate re-parsed
# the same YAMLs a dozen times per file check. Same reparse tax measured on comp-which (10 parses,
# ~97% of its runtime) -- a second instance of one class, not a one-off.
#
# WHY deepcopy AND NOT a bare cached reference -- THIS LINE IS LOAD-BEARING, NOT DEFENSIVE:
# load_config() MUTATES what load_yaml returns (5 x setdefault at :254-265 below). Handing every
# caller the same object would make those mutations shared state. The deepcopy preserves the
# existing contract exactly: each caller still gets its OWN mutable dict. Measured: deepcopy 0.7ms
# vs parse 95.5ms for the 133KB manifest, so the copy is not the cost.
#
# LIFETIME IS THE PROCESS -- and that is the correct scope here: commit_gate_runner is ONE process
# per commit, so the cache spans every file in that commit (the compounding win) and dies with it.
# THE ASSUMPTION THIS RESTS ON: no YAML the gate reads is REWRITTEN mid-run. True today (the gate
# reads what it is handed and writes no YAML). If that ever changes, this cache serves a stale parse
# silently -- the failure mode would be invisible, so change this deliberately, never incidentally.
#
# VALIDATED BEFORE LANDING (/seams 2340Z, all 3 axes PASS): parity harness ran the LIVE module at
# its real path in both arms with ONLY caching differing -- stdout/stderr/exit-code BYTE-IDENTICAL
# across 3 cases; load_config mutability probe confirmed independent objects + isolated mutation on
# both arms. Measured 1.6x (1 file) -> 2.3x (3 files); it grows with commit size.
_YAML_CACHE: dict[str, dict] = {}

# C-ACCELERATED PARSER (0.8.0_AE_CloudComp 2026-07-28, the post-cache remainder of the same
# Andrew-direct thread). cProfile on the CACHED module: yaml parsing was STILL 1.99s of 2.29s for a
# .tools-touching file, because (a) the cold first-parse of each YAML is paid through SafeLoader
# (133KB manifest = ~118ms), and (b) two call sites bypassed the cache entirely (_section_pair's
# HEAD-vs-worktree parses, _placement_invariant's raw open). CSafeLoader (libyaml) parses the same
# manifest in ~9ms and was verified PARSE-EQUAL (parsed-doc ==) on all 5 YAMLs the gate reads.
# The getattr fallback keeps the gate correct on a Python built without libyaml -- slower, never
# wrong. safe_load == load(Loader=SafeLoader), so both branches are the SAFE loader family.
_YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def load_yaml(path: Path) -> dict:
    if not path.exists():
        sys.stderr.write(f"ERROR: not found: {path}\n")
        sys.exit(2)
    _key = str(path)
    if _key not in _YAML_CACHE:
        with path.open(encoding="utf-8") as fh:
            _YAML_CACHE[_key] = yaml.load(fh, Loader=_YAML_LOADER) or {}
    return _copy.deepcopy(_YAML_CACHE[_key])


def load_manifest() -> dict:
    data = load_yaml(_MANIFEST)
    entries = {e["id"]: e for e in data.get("entries", []) if isinstance(e, dict) and e.get("id")}
    return entries


def load_config() -> dict:
    cfg = load_yaml(_CONFIG)
    cfg.setdefault("mode", "advisory")
    cfg.setdefault(
        "severity",
        {
            "A_deprecated_call": "error",
            "C_adhoc_reimplementation": "error",
            "B_rebuild_when_query": "warn",
        },
    )
    cfg.setdefault("exempt_path_substrings", [])
    cfg.setdefault("exempt_basename_prefixes", [])
    cfg.setdefault("tally_log", "org/modules/graph/.manifest_check_advisory_tally.jsonl")
    return cfg


def append_tally(findings: list[Finding], mode: str, cfg: dict) -> None:
    """Best-effort: append every finding to the advisory-hit tally (D6 ramp evidence engine).

    The advisory->blocking flip earns its block with empirical evidence, not faith
    (CTO ramp ruling 2026-06-11): >= ~10 commits flow through advisory with 0 false-positives
    (an advisory firing on a CORRECT canonical call is a precision bug to fix BEFORE flipping).
    Each row: ts + file + lineno + category + severity + matched line + mode. NEVER disrupts the
    gate -- any write error is swallowed.
    """
    if not findings:
        return
    rel = cfg.get("tally_log") or ""
    if not rel:
        return
    path = rel if Path(rel).is_absolute() else (_WORKSPACE / rel)
    try:
        ts = _dt.datetime.now().isoformat(timespec="seconds")
        with Path(path).open("a", encoding="utf-8") as fh:
            for f in findings:
                fh.write(json.dumps({
                    "ts": ts, "mode": mode, "file": f.file, "lineno": f.lineno,
                    "category": f.category, "severity": f.severity, "line": f.line,
                }) + "\n")
    except (OSError, UnicodeError):
        pass


# ----------------------------------------------------------------------------------- exemptions
def is_exempt(path: Path, cfg: dict) -> bool:
    try:
        rel = path.resolve().relative_to(_WORKSPACE).as_posix()
    except ValueError:
        rel = path.as_posix()
    rel = rel.replace("\\", "/")
    for sub in cfg.get("exempt_path_substrings", []):
        if sub in rel:
            return True
    base = path.name
    for pre in cfg.get("exempt_basename_prefixes", []):
        if base.startswith(pre):
            return True
    return False


# ------------------------------------------------------------------------------------- deprecated
def deprecated_signatures(manifest: dict) -> list[dict]:
    """Build detection signatures for every status: deprecated manifest entry.

    Forward-correct: the manifest has 0 deprecated entries today (all 33 are canonical + 1
    planned), but when a use-case is deprecated in favour of a faster canonical, this catches
    code still calling the old path and names the superseded_by replacement -- fully
    manifest-driven, no code change needed to add a new deprecated detection.
    """
    sigs = []
    for eid, entry in manifest.items():
        if entry.get("status") != "deprecated":
            continue
        tool = entry.get("tool", "")
        # Primary detection token: the tool name (e.g. an old comp-foo) -- the cheapest robust
        # signal that the deprecated path is being invoked.
        token = tool.strip()
        if not token:
            continue
        sigs.append(
            {
                "id": eid,
                "pattern": re.compile(r"\b" + re.escape(token) + r"\b"),
                "superseded_by": entry.get("superseded_by", "(unspecified)"),
                "canonical_call": "",
            }
        )
    return sigs


# ----------------------------------------------------------------------------------------- scan
class Finding:
    __slots__ = ("category", "severity", "file", "line", "lineno", "note")

    def __init__(self, category: str, severity: str, file: str, lineno: int, line: str, note: str):
        self.category = category
        self.severity = severity
        self.file = file
        self.lineno = lineno
        self.line = line.strip()
        self.note = note


def scan_file(path: Path, manifest: dict, cfg: dict, dep_sigs: list[dict]) -> list[Finding]:
    findings: list[Finding] = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except (OSError, UnicodeError):
        return findings
    rel = _relpath(path)
    sev = cfg.get("severity", {})

    for i, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if not stripped:
            continue
        is_comment = _is_comment_line(stripped)

        # (A) deprecated-entry calls -- manifest-driven. Code lines only.
        if not is_comment:
            for s in dep_sigs:
                if s["pattern"].search(raw):
                    findings.append(
                        Finding(
                            "A_deprecated_call",
                            sev.get("A_deprecated_call", "error"),
                            rel,
                            i,
                            raw,
                            f"deprecated graph-call ({s['id']}); canonical is "
                            f"{s['superseded_by']}. {s['canonical_call']}".strip(),
                        )
                    )

        # (B) rebuild-when-query. Code lines only.
        if not is_comment:
            for tok in REBUILD_TOKENS:
                if tok["pattern"].search(raw):
                    qids = ", ".join(tok["query_canonical"])
                    findings.append(
                        Finding(
                            "B_rebuild_when_query",
                            sev.get("B_rebuild_when_query", "warn"),
                            rel,
                            i,
                            raw,
                            f"{tok['note']} Canonical query entry: {qids}.",
                        )
                    )

        # (C) ad-hoc re-implementation / raw access. Code lines only.
        if not is_comment:
            for pat in ADHOC_PATTERNS:
                if pat["pattern"].search(raw):
                    findings.append(
                        Finding(
                            "C_adhoc_reimplementation",
                            sev.get("C_adhoc_reimplementation", "error"),
                            rel,
                            i,
                            raw,
                            pat["note"],
                        )
                    )
    return findings


def _relpath(path: Path) -> str:
    try:
        return path.resolve().relative_to(_WORKSPACE).as_posix()
    except ValueError:
        return path.as_posix()


# --------------------------------------------------------------------------------------- render
def render(findings: list[Finding], mode: str) -> None:
    label = "MANIFEST-ADVISORY" if mode == "advisory" else "MANIFEST-CHECK"
    for f in findings:
        tag = f.severity.upper()
        print(f"{label} [{tag}] {f.file}:{f.lineno} ({f.category})")
        print(f"    > {f.line}")
        print(f"    {f.note}")


# -------------------------------------------------------------------------------------- commands
def _load_routable_engine():
    """Import .tools/comp-routable-check (extensionless -> load by path).

    IMPORTED, never reimplemented: exactly ONE definition of the invariant. A forked copy would
    drift from the engine agents run directly, and a completeness gate that disagrees with its
    own tool is worse than no gate.
    """
    import importlib.machinery
    import importlib.util

    path = _WORKSPACE / ".tools" / "comp-routable-check"
    loader = importlib.machinery.SourceFileLoader("comp_routable_check", str(path))
    spec = importlib.util.spec_from_loader("comp_routable_check", loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


def _touches_routable_substrate(files) -> bool:
    norm = {str(f).replace("\\", "/") for f in (files or [])}
    return any(any(n.endswith(s) for s in _ROUTABLE_SUBSTRATE) for n in norm)


def _routable_invariant(files) -> int:
    """0 = invariant holds, or not applicable to these files. 1 = BLOCK.

    b2: only a commit touching the manifest / coverage-map / provider can introduce the defect.
    Ramp-exempt: blocks regardless of advisory|blocking mode.
    Fail-closed: an unevaluable invariant is not a passing one.
    """
    if not _touches_routable_substrate(files):
        return 0
    try:
        rc = _load_routable_engine()
        _targets, unreachable, _uncatalogued, exempted = rc.check()
    except Exception as e:  # fail-closed -- a gate that cannot evaluate must not read as "passed"
        print(
            f"\nBLOCKED: the routable-invariant could not be evaluated ({e}).\n"
            f"  An unevaluable completeness gate does not read as 'passed'. The capability "
            f"provider's load-robustness is commit-critical by design."
        )
        return 1

    for tool, reason in exempted:
        print(f"  routable-exempt: {tool} -- {reason}")

    if not unreachable:
        return 0

    print(f"\nBLOCKED: {len(unreachable)} registered tool(s) are UNREACHABLE via comp-which:")
    for tool, why, kind in unreachable:
        print("  - %-22s %s%s" % (tool, why, f" (kind={kind})" if kind else ""))
    print(
        "  A tools_index tool with routable=False is dropped by comp_route.py's candidate filter\n"
        "  BEFORE scoring -- no curated rule or vocabulary can surface it. FIX: add its\n"
        "  coverage-map role to comp_capability_provider._ROUTABLE_META_ROLES, or declare\n"
        "  `routing_exempt: <reason>` on its coverage-map entry. Then re-run\n"
        "  `python .tools/comp-which-routing-test.py`."
    )
    return 1


def _norm(files):
    return [str(f).replace("\\", "/") for f in (files or [])]


def _committed_comp_tools(files):
    """member 2's universe: comp-tool names named by the COMMIT itself (never os.listdir).

    DELETION-AWARE (2026-07-30, 3.0.0_SA_CVO): a committed path whose .tools/<file> no longer
    exists in the committing tree is a RETIREMENT, not an unplaced tool. Before this filter,
    requiring a map home for a deleted tool made the registries' own delete-together orders
    (delete the tool + its coverage-map row in ONE commit) structurally uncommittable -- the
    exact shape the comp-semantic-estates/comp-opalbizsem retirement hit. A deletion needs no
    home; the map_touched branch still catches a map edit that strands a live tool."""
    tools = set()
    for f in _norm(files):
        if "/.tools/" in "/" + f and "/" not in f.split(".tools/", 1)[-1]:
            fname = f.split(".tools/", 1)[-1]
            name = fname.rsplit(".", 1)[0] if "." in fname else fname
            if (name.startswith("comp-") or name == "pipescript") and \
                    (_WORKSPACE / ".tools" / fname).exists():
                tools.add(name)
    return tools


_HEAD_PAIR_CACHE: dict[str, tuple] = {}
_HEAD_ABSENT = ("__HEAD_ABSENT__",)


def _section_pair(path, section):
    """(old, new) value of `section` -- old from HEAD, new from the working tree. (None, None)
    when HEAD has no such file (a brand-new file: the caller must treat it as 'everything').

    BOTH SIDES ARE DECODED AS UTF-8 AND NEWLINE-NORMALIZED, deliberately. Two ways this silently
    breaks, both found by the verification matrix rather than by reading:
      * ENCODING -- `git show` with text=True decodes via the LOCALE codec (cp1252 here), while the
        working file is UTF-8. The manifest contains an em-dash, so a byte-identical file compared
        unequal on every run.
      * NEWLINES -- `git show` emits LF; the working tree is CRLF under autocrlf.
    Either one makes a CLEAN tree read as "everything changed", so the per-tool bound silently
    degrades to the full ~57s sweep while the gate still reports green. The bound would have been
    a claim, not a fact. (Observed: a clean manifest touch cost 33.8s instead of ~0.)

    THE PARSED (old_doc, new_doc) PAIR IS CACHED PER PATH: three members diff the SAME manifest
    (selfroute x2 sections, subcommand-declaration, and any future _dict_diff_keys caller), and
    each un-cached call re-ran `git show` + re-parsed the 133KB doc TWICE -- 0.80s of the 2.29s
    post-cache profile in ONE member alone. Same lifetime + same no-mid-run-rewrite assumption as
    _YAML_CACHE above. Sections are returned as deepcopies (0.7ms) so the mutability contract is
    identical to load_yaml's -- no caller can corrupt the cached docs.
    """
    docs = _HEAD_PAIR_CACHE.get(path)
    if docs is None:
        import subprocess as _sp
        old = _sp.run(["git", "show", f"HEAD:{path}"], capture_output=True,
                      cwd=str(_WORKSPACE)).stdout
        if not old:
            docs = _HEAD_ABSENT
        else:
            def _norm_text(b):
                s = b.decode("utf-8", "replace") if isinstance(b, bytes) else b
                return s.replace("\r\n", "\n").replace("\r", "\n")
            with open(_WORKSPACE / path, "rb") as fh:
                new_raw = fh.read()
            old_doc = yaml.load(_norm_text(old), Loader=_YAML_LOADER) or {}
            new_doc = yaml.load(_norm_text(new_raw), Loader=_YAML_LOADER) or {}
            docs = (old_doc, new_doc)
        _HEAD_PAIR_CACHE[path] = docs
    if docs is _HEAD_ABSENT:
        return None, None
    old_doc, new_doc = docs
    return _copy.deepcopy(old_doc.get(section)), _copy.deepcopy(new_doc.get(section))


def _dict_diff_keys(path, section):
    """Keys of a MAPPING section whose value changed vs HEAD. None = unbounded (new file, or the
    section is not a mapping -- e.g. `entries:` is a LIST, so it has no per-key bound)."""
    o, n = _section_pair(path, section)
    if o is None and n is None:
        return None
    if not isinstance(o, dict) or not isinstance(n, dict):
        return None
    return {k for k in set(o) | set(n) if o.get(k) != n.get(k)}


def _section_changed(path, section):
    """True if a section changed vs HEAD, for ANY shape (list or mapping). True on a new file."""
    o, n = _section_pair(path, section)
    if o is None and n is None:
        return True
    return o != n


def _placement_invariant(files) -> int:
    """member 2 -- a comp-tool has exactly ONE map home. UNPLACED and DOUBLE-PLACED both block."""
    norm = _norm(files)
    tools = _committed_comp_tools(files)
    map_touched = any(f.endswith(_PLACEMENT_MAP) for f in norm)
    if not tools and not map_touched:
        return 0
    try:
        sys.path.insert(0, str(_THIS_DIR))
        import comp_coverage_check as ccc

        # via the process cache (deepcopy'd, so ccc mutating it cannot corrupt the cached doc) --
        # this was the third cache-bypassing raw parse the post-cache profile found.
        led = load_yaml(_WORKSPACE / _PLACEMENT_MAP)
        if map_touched:
            # a map edit can REMOVE a home -> the commit's own file list cannot name the victim.
            for section in ("tools", "meta_tools"):
                changed = _dict_diff_keys(_PLACEMENT_MAP, section)
                if changed is None:
                    tools |= {t.get("tool") for t in (led.get(section) or []) if t.get("tool")}
        if not tools:
            return 0
        problems = ccc._check_inventory_completeness(led, inventory=set(tools))
    except Exception as e:  # fail-closed
        print(f"\nBLOCKED: the placement invariant could not be evaluated ({e}).")
        return 1
    if not problems:
        return 0
    print("\nBLOCKED: comp-tool placement (each tool needs exactly ONE coverage-map home):")
    for p in problems:
        print("  - %s" % p)
    print("  FIX: add the tool to comp-coverage-map.yaml tools[] (surface-homed) or meta_tools[]")
    print("  (cross-surface/tooling-layer), never both.")
    return 1


def _selfroute_invariant(files) -> int:
    """member 3 -- a catalogued tool must SURFACE for its own use_case.

    HARD-BLOCK on MISS (deterministic, role-invariant, margin-free). WARN on NEARTIE (the tool
    surfaces only inside comp-which's within-margin list -- threshold-shaped, so reporting only).

    HARD-BLOCK on UNEVALUABLE too (NFRA_TOOLARCH.GATEBOUND Stage A, 0.8.0_AE_CloudComp~D
    2026-07-25): `self_route_verdicts` now bounds its warm call on a watchdog deadline (comp-
    which:1201's fallback subprocess has no timeout of its own and caused an 84-minute hang here
    before this landed) and reports UNEVALUABLE, never MISS, when a call does not finish in time
    -- that call's real routing status is UNKNOWN, not "confirmed absent." Treating UNKNOWN as a
    pass would let a commit land on top of an unverified router-surfacing guarantee for exactly
    the tool the watchdog could not check; treating it the same as MISS would misreport what was
    actually found. So it gets its own printed line and the same hard-block MISS gets -- a bounded
    UNKNOWN is still an UNKNOWN, and this gate's whole reason to exist is not shipping past one.
    """
    norm = _norm(files)
    corpus_touched = any(f.endswith(s) for s in _SELFROUTE_CORPUS for f in norm)
    manifest_touched = any(f.endswith("org/modules/graph/graph-call-manifest.yaml") for f in norm)
    if not corpus_touched and not manifest_touched:
        return 0
    # EVERYTHING that can raise lives inside the guard -- a fail-closed gate whose scope
    # computation can throw is fail-OPEN in disguise (it crashes with a traceback instead of a
    # verdict). Found by the verification matrix, not by reading.
    try:
        MAN = "org/modules/graph/graph-call-manifest.yaml"
        targets = None  # None = the full set
        if manifest_touched and not corpus_touched:
            # `entries:` is the fuzzy-backstop CORPUS (a LIST) -> an edit there can move ANY tool's
            # verdict, so it is unbounded. `tools_index[t].does` is only ever the QUERY for tool t
            # -> bounded to the changed tools (cost option (i), ~1357ms per tool).
            if not _section_changed(MAN, "entries"):
                changed = _dict_diff_keys(MAN, "tools_index")
                if changed is not None:
                    targets = sorted(changed)
        if targets == []:
            return 0  # manifest touched, but no tools_index entry actually changed

        import importlib.machinery
        import importlib.util

        import yaml as _yaml
        p = _WORKSPACE / ".tools" / "comp-which-routing-test.py"
        loader = importlib.machinery.SourceFileLoader("cwrt", str(p))
        spec = importlib.util.spec_from_loader("cwrt", loader)
        mod = importlib.util.module_from_spec(spec)
        loader.exec_module(mod)
        with open(_WORKSPACE / MAN, encoding="utf-8") as fh:
            manifest = _yaml.safe_load(fh)
        verdicts = mod.self_route_verdicts(manifest, tools=targets)
    except Exception as e:  # fail-closed
        print(f"\nBLOCKED: the self-route invariant could not be evaluated ({e}).")
        return 1

    misses = sorted(t for t, (v, _r, _q) in verdicts.items() if v == "MISS")
    nearties = sorted(t for t, (v, _r, _q) in verdicts.items() if v == "NEARTIE")
    unevaluable = sorted(t for t, (v, _r, _q) in verdicts.items() if v == "UNEVALUABLE")
    for t in nearties:
        print("  self-route WARN: %s surfaces only inside comp-which's near-tie list (never rank-1)" % t)
    if not misses and not unevaluable:
        return 0
    if unevaluable:
        deadline = getattr(mod, "WARM_DEADLINE_S", None)
        print("\nBLOCKED: %d catalogued tool(s) could NOT be evaluated (watchdog deadline%s):"
              % (len(unevaluable), (", %.0fs" % deadline) if deadline is not None else ""))
        for t in unevaluable:
            print("  - %-22s comp-which's warm call did not finish -- status UNKNOWN, not MISS" % t)
        print("  Route status unknown is not a pass. Re-run once the underlying slowness/hang is")
        print("  understood; do not re-run blindly hoping it clears -- see NFRA_TOOLARCH.GATEBOUND.")
    if not misses:
        return 1
    print("\nBLOCKED: %d catalogued tool(s) do NOT surface for their own use_case:" % len(misses))
    for t in misses:
        print("  - %-22s comp-which returns nothing naming it" % t)
    print("  A tool the mandated router cannot return is undiscoverable, however well it is")
    print("  catalogued. FIX: give it distinctive curated vocabulary in .tools/comp-which, and do")
    print("  NOT let its catalog text name a sibling tool -- a description is routing input, and")
    print("  naming a sibling hands it your intent. Then: python .tools/comp-which-routing-test.py")
    return 1


# member 4: only a tools_index edit (registers a tool) or a `.tools/comp-*` delete/rename (removes
# the executable) can create a REGISTERED-BUT-ABSENT tool.
_EXISTENCE_SUBSTRATE = (
    "org/modules/graph/graph-call-manifest.yaml",
)


def _tool_path_status(tool: str, tracked_basenames: set) -> tuple:
    """(on_disk, in_git) for a registered tool name. A tool ships as `.tools/<name>` or, for the
    python-shebang tools, `.tools/<name>.py` / `.tools/<name>.sh`."""
    on_disk = in_git = False
    for suffix in ("", ".py", ".sh"):
        cand = f"{tool}{suffix}"
        if (_WORKSPACE / ".tools" / cand).exists():
            on_disk = True
        if cand in tracked_basenames:
            in_git = True
    return on_disk, in_git


def _existence_invariant(files) -> int:
    """0 = invariant holds, or not applicable. 1 = BLOCK.

    REGISTERED-IMPLIES-EXISTS. member 1 asserts a registered tool is a live ROUTING TARGET
    (candidate-set membership in the capability provider). Nothing asserted that the tool is a
    live EXECUTABLE. Those are different properties, and on 2026-07-09 they diverged: comp-system
    was registered in all three routable-substrate registries, passed member 1, and comp-which
    returned it RANK-1 for its own use_case -- while `.tools/comp-system` had never existed in the
    repo's object graph (0 objects across all refs). An agent following the Rule-21 rail got
    `command not found`. Routability bound a PROXY (presence in the provider) for the PROPERTY
    (the command runs).

    TWO conditions, because `.gitignore:183` ignores `.tools/` wholesale and every tool there is
    force-added:
      on_disk  -- the author's own tree can run it
      in_git   -- a FRESH CLONE can run it (the 16-gitignored-tools class, at its root)
    A tool present-but-untracked is the more dangerous half: it works for the author and for
    nobody else, so it passes every check the author runs.

    DETERMINISTIC (CTO's hard-block bar: "every hard-blocking member asserts a DETERMINISTIC fact").
    Universe is derived from the files being COMMITTED, never os.listdir -- we share one worktree.
    Ramp-exempt. Fail-closed: an unevaluable invariant is not a passing one.
    """
    norm = _norm(files)
    manifest_touched = any(f.endswith(s) for s in _EXISTENCE_SUBSTRATE for f in norm)
    tools_touched = any("/.tools/" in "/" + f for f in norm)
    if not manifest_touched and not tools_touched:
        return 0

    try:
        MAN = "org/modules/graph/graph-call-manifest.yaml"
        # NOT load_manifest() -- that returns the `entries:` list keyed by id, not the raw doc.
        # Reading tools_index off it yields None -> an empty universe -> a gate that sweeps nothing
        # and exits 0. (Caught by the legible-PASS line printing "0 registered tool(s)": a mute
        # green would have shipped this. The gate that binds nothing is the defect this family
        # exists to prevent, and it appeared first inside the member built to prevent it.)
        registered = sorted((load_yaml(_MANIFEST).get("tools_index") or {}).keys())

        # Bound to the tools_index keys this commit actually changed. A `.tools/` touch (a delete
        # or rename can orphan ANY registered tool) is unbounded by construction.
        targets = registered
        if manifest_touched and not tools_touched:
            changed = _dict_diff_keys(MAN, "tools_index")
            if changed is not None:
                targets = sorted(changed)
        if not targets:
            return 0

        import subprocess as _sp
        r = _sp.run(["git", "ls-files", ".tools/"], capture_output=True, text=True,
                    cwd=str(_WORKSPACE))
        if r.returncode != 0:
            raise RuntimeError(f"git ls-files failed: {r.stderr.strip()[:120]}")
        tracked = {Path(p).name for p in r.stdout.split()}
    except Exception as e:  # fail-closed
        print(
            f"\nBLOCKED: the existence-invariant could not be evaluated ({e}).\n"
            f"  An unevaluable completeness gate does not read as 'passed'."
        )
        return 1

    missing, untracked = [], []
    for tool in targets:
        if not tool.startswith("comp-"):
            continue  # `pipescript` and friends are not `.tools/comp-*`-shaped
        on_disk, in_git = _tool_path_status(tool, tracked)
        if not on_disk:
            missing.append(tool)
        elif not in_git:
            untracked.append(tool)

    if not missing and not untracked:
        return 0

    print("\nBLOCKED: registered tool(s) do not EXIST as a runnable, tracked executable:")
    for tool in missing:
        print(f"  - {tool:<22} registered in tools_index, but .tools/{tool} is NOT ON DISK")
    for tool in untracked:
        print(f"  - {tool:<22} on disk but NOT TRACKED by git -- absent from a fresh clone")
    print(
        "  comp-which will route an agent to this tool and the call will fail. Registration is\n"
        "  not shipping. FIX: create the launcher (see .tools/comp-manifest-check for the shim\n"
        "  shape) and force-add it -- `.gitignore` ignores .tools/ wholesale, so a plain `git add`\n"
        "  silently no-ops. safe-commit.sh stages with `git add -f` for an explicit FILE pathspec."
    )
    return 1


# member 5: only a `.tools/comp-*` add/rename or a registry edit can create a
# DISK-BUT-UNREGISTERED tool.
_REGISTRATION_SUBSTRATE = (
    "org/modules/graph/graph-call-manifest.yaml",
    "org/modules/graph/comp-coverage-map.yaml",
)


def _registration_invariant(files) -> int:
    """0 = invariant holds, or not applicable. 1 = BLOCK.

    DISK-IMPLIES-REGISTERED (NFRA_COMPCLOSE 2026-07-14) -- the INVERSE of member 4. Member 4
    asserts a registered tool exists as a runnable executable; nothing asserted that an existing
    executable is REGISTERED. Those diverged for weeks: comp-whoread / comp-deadgrant /
    comp-tool-health (+11 more) were tracked, runnable, and absent from tools_index AND the
    excluded list -- so comp-which could never route to them, and agents logged "no comp-tool
    answers this" for questions those exact tools answer. A TOOL NOBODY CAN FIND IS
    INDISTINGUISHABLE FROM A TOOL THAT WAS NEVER BUILT; this member makes the drift a commit-time
    fact instead of a quarterly archaeology find.

    THE INVARIANT, two legs, each with its denominator PRINTED (a filter whose complement you did
    not enumerate is a filter you have not tested):
      manifest leg -- every tracked `.tools/comp-*` executable is a tools_index key, OR in
                      excluded_not_graph_use_cases (with its reason), OR the `tool:` of at least
                      one `entries:` row (comp-which itself is accounted this way).
      ledger leg   -- every such executable appears in the coverage map's union(tools[],
                      meta_tools[]) -- the registry the posterior router actually routes on.

    Universe = git-TRACKED `.tools/comp-*` (fresh-clone truth, same rationale as member 4) PLUS
    any comp-* executable in THIS commit's pathspec (a brand-new tool registers in the same
    commit). Never os.listdir -- we share one worktree and scratch files are not commitments.
    Extensionless names only (the launchers); .py/.sh implementation siblings ride along
    unregistered by design. DETERMINISTIC; ramp-exempt; fail-closed.
    """
    norm = _norm(files)
    touched = (any(f.endswith(s) for s in _REGISTRATION_SUBSTRATE for f in norm)
               or any("/.tools/" in "/" + f for f in norm))
    if not touched:
        return 0

    try:
        import subprocess as _sp
        r = _sp.run(["git", "ls-files", ".tools/"], capture_output=True, text=True,
                    cwd=str(_WORKSPACE))
        if r.returncode != 0:
            raise RuntimeError(f"git ls-files failed: {r.stderr.strip()[:120]}")
        universe = {Path(p).name for p in r.stdout.split()}
        committed_names = {Path(f).name for f in norm if "/.tools/" in "/" + f}
        universe |= committed_names
        # DELETION-AWARE (2026-07-30, 3.0.0_SA_CVO, same principle as _committed_comp_tools): a
        # name the COMMIT ITSELF touches whose .tools file is absent from the committing tree is
        # a staged RETIREMENT riding this commit. git ls-files reads the index/HEAD, which
        # carries the file until this very commit lands -- so without this subtraction a
        # delete-together retirement (tool + registry rows in ONE commit) is structurally
        # uncommittable. Scoped to commit-named paths ONLY: a tracked-but-missing file the
        # commit does NOT name still blocks (fresh-clone truth preserved for everything else).
        universe = {t for t in universe
                    if not (t in committed_names and not (_WORKSPACE / ".tools" / t).exists())}
        universe = sorted(t for t in universe if t.startswith("comp-") and "." not in t)

        raw = load_yaml(_MANIFEST)
        ti = set((raw.get("tools_index") or {}).keys())
        exc = set(raw.get("excluded_not_graph_use_cases") or [])
        entry_tools = {str(e.get("tool", "")).split()[0] for e in (raw.get("entries") or [])
                       if isinstance(e, dict)}
        led = load_yaml(_WORKSPACE / "org" / "modules" / "graph" / "comp-coverage-map.yaml")
        ledger = ({t.get("tool") for t in (led.get("tools") or []) if isinstance(t, dict)}
                  | {t.get("tool") for t in (led.get("meta_tools") or []) if isinstance(t, dict)})
    except Exception as e:  # fail-closed
        print(
            f"\nBLOCKED: the registration-invariant could not be evaluated ({e}).\n"
            f"  An unevaluable completeness gate does not read as 'passed'."
        )
        return 1

    unaccounted = [t for t in universe if t not in ti and t not in exc and t not in entry_tools]
    unledgered = [t for t in universe if t not in ledger]

    if not unaccounted and not unledgered:
        print(f"  [manifest-check] registration-invariant PASS: {len(universe)} tracked+committed "
              f"comp-* executable(s) all accounted (tools_index {len(ti)} + excluded {len(exc)} + "
              f"entries-tools {len(entry_tools)}) and ledgered (coverage-map {len(ledger)}).")
        return 0

    print(f"\nBLOCKED: comp-* executable(s) on disk are NOT REGISTERED "
          f"(universe {len(universe)} tracked+committed; tools_index {len(ti)}, excluded {len(exc)}, "
          f"entries-tools {len(entry_tools)}, coverage-map {len(ledger)}):")
    for t in unaccounted:
        print(f"  - {t:<22} in NEITHER tools_index NOR excluded_not_graph_use_cases NOR any entries: row")
    for t in unledgered:
        print(f"  - {t:<22} absent from comp-coverage-map.yaml union(tools[], meta_tools[]) -- the "
              f"posterior router cannot see it")
    print(
        "  A tool nobody can find is indistinguishable from a tool that was never built. FIX:\n"
        "  register it (tools_index + an entries: row with agent-phrasing use_case + a coverage-map\n"
        "  home with an explicit routable:), or add it to excluded_not_graph_use_cases WITH a reason."
    )
    return 1


_OUTPUT_CONTRACT_FILE = "org/modules/graph/comp-output-contracts.yaml"


def _output_contract_invariant(files) -> int:
    """0 = invariant holds / not applicable. 1 = BLOCK.

    THE OUTPUT-CONTRACT REGISTRATION INVARIANT (NFRA_MSBEFF.R1R3 condition a, 2026-07-23). A tool cannot
    register/re-register in tools_index without declaring its output contract (coverage + plane + exit
    semantics) -- else the shared output contract (org/modules/graph/comp-output-contracts.yaml) silently
    UNDER-COVERS a new tool, and the M3 verdict-set derivation reverts to the frozen-list failure mode it
    retired. This is the INVERSE-mate of DISK-IMPLIES-REGISTERED: that member makes an on-disk tool prove it
    is routable; this one makes a routable tool prove it declares what it can/cannot see and how its exits
    classify.

    THE INVARIANT (denominator PRINTED -- a filter whose complement you did not enumerate is untested):
      every tools_index tool appears in comp-output-contracts.yaml under EITHER `contracts:` (full
      declaration) OR `pending_declaration:` (explicitly awaiting one -> renders LOUD UNKNOWN at run time,
      condition b). A tool in NEITHER is an unregistered output contract: BLOCK.

    Migration-safe by construction: the pending list makes the undeclared tail VISIBLE and bounded, so the
    tail can never grow silently -- a NEW tools_index tool with no contract-or-pending entry fails HERE, at
    the same commit that registers it. Fires only when the registration substrate OR the contract file OR a
    `.tools/comp-*` executable is touched (registration-time), so it never taxes unrelated commits.
    DETERMINISTIC; ramp-exempt; fail-closed.
    """
    norm = _norm(files)
    touched = (any(f.endswith(s) for s in _REGISTRATION_SUBSTRATE for f in norm)
               or any(f.endswith(_OUTPUT_CONTRACT_FILE) for f in norm)
               or any("/.tools/" in "/" + f for f in norm))
    if not touched:
        return 0

    try:
        man = load_yaml(_MANIFEST)
        registered = sorted((man.get("tools_index") or {}).keys())
        doc = load_yaml(_WORKSPACE / "org" / "modules" / "graph" / "comp-output-contracts.yaml")
        declared = set((doc.get("contracts") or {}).keys())
        pending = set(doc.get("pending_declaration") or [])
    except Exception as e:  # fail-closed
        print(
            f"\nBLOCKED: the output-contract invariant could not be evaluated ({e}).\n"
            f"  An unevaluable completeness gate does not read as 'passed'."
        )
        return 1

    covered = declared | pending
    missing = [t for t in registered if t not in covered]

    if not missing:
        print(f"  [manifest-check] output-contract invariant PASS: {len(registered)} tools_index tool(s) "
              f"all declare an output contract (declared {len(declared & set(registered))} + pending "
              f"{len(pending & set(registered))}); {len(declared - set(registered))} extra declaration(s) "
              f"for non-tools_index emitters.")
        return 0

    print(f"\nBLOCKED: tools_index tool(s) with NO output contract "
          f"(registered {len(registered)}; declared {len(declared)}, pending {len(pending)}):")
    for t in missing:
        print(f"  - {t:<22} in NEITHER contracts: NOR pending_declaration: of comp-output-contracts.yaml")
    print(
        "  A tool that cannot state its coverage/plane renders UNKNOWN, loudly -- but it must SAY SO in the\n"
        "  contract file. FIX: add a full `contracts:` block (coverage + blind_spots + plane + vintage +\n"
        "  exit_codes), or list it under `pending_declaration:` (renders LOUD UNKNOWN until declared)."
    )
    return 1


_RULE_BANK_REL = "org/modules/graph/NFRA_ONTOLOGY_RULE_BANK.yaml"


def _stage2_vocab_invariant(files) -> int:
    """0 = holds / dormant / not applicable. 1 = BLOCK.

    STAGE-2 of the output contract (NFRA_MSBEFF.R1R3 <-> NFRA_ONTOLOGY2, CTO~Z two-stage ruling 184541Z;
    ~C canonized the (rail,grain,plane,scope) type_tuple @5d1161d70). STAGE 1 (the output-contract member)
    enforces PRESENCE of a declaration; THIS enforces that declared VALUES are in the CANONICAL vocabulary --
    an out-of-vocab rail/grain/plane/scope renders a LOUD gate fail, never a silent parallel term (the
    denominator-is-its-own-config class, closed at the value layer). The vocabulary is read from the rule
    bank canonical_source, so it tracks ontology law automatically; DORMANT (pass) if the type_tuple is
    absent (pre-canonization) so it never false-blocks. Fires when the contract file or the rule bank is
    touched. DETERMINISTIC; ramp-exempt; fail-closed."""
    norm = _norm(files)
    touched = (any(f.endswith(_OUTPUT_CONTRACT_FILE) for f in norm)
               or any(f.endswith(_RULE_BANK_REL) for f in norm)
               or any("/.tools/" in "/" + f for f in norm)
               or any(f.endswith(s) for s in _REGISTRATION_SUBSTRATE for f in norm))
    if not touched:
        return 0

    try:
        import importlib
        import sys as _sys
        if str(_WORKSPACE) not in _sys.path:
            _sys.path.insert(0, str(_WORKSPACE))
        oc = importlib.import_module("org.modules.graph.comp_output_contract")
        oc.canon_vocab_strict.cache_clear()
        # A GATE reads STRICT. The lenient canon_vocab() returns {} on a read failure, which silently
        # DISARMED this member (CVO~Z 221805Z, test specified by ~C): the empty dict arrived before any
        # exception, so the fail-closed handler below never fired and a missing/moved rule bank printed a
        # benign "DORMANT" line and returned PASS. Read failure now PROPAGATES and blocks.
        try:
            vocab = oc.canon_vocab_strict()
        except oc.CanonVocabUnavailable as e:
            print(f"\nBLOCKED: the ONTOLOGY2 canonical_source could not be READ -- {e}.\n"
                  f"  This is a DISARMED stage-2 axis, NOT a dormant one: with no vocabulary the gate\n"
                  f"  validates nothing, so it must FAIL rather than pass silently. FIX the path/file\n"
                  f"  (or update _RULE_BANK if ONTOLOGY2 moved it); do not bypass.")
            return 1
        if not vocab:
            # THE DORMANCY RATIONALE EXPIRED AT @5d1161d70. Pre-canonization an absent type_tuple was
            # legitimate; ~C canonized it, so post-canonization a readable rule bank with NO type_tuple
            # means RATIFIED VOCABULARY WAS REMOVED. The disarmed state is no longer distinguishable
            # from a legitimate state that still exists -- because that state no longer exists.
            print("\nBLOCKED: the rule bank READ FINE but carries NO `type_tuple` section.\n"
                  "  ONTOLOGY2 canonized the (rail,grain,plane,scope) vocabulary @5d1161d70, so its\n"
                  "  absence means ratified vocabulary was REMOVED -- stage-2 would validate nothing.\n"
                  "  FIX: restore type_tuple, or route a deliberate vocabulary retirement through ~C\n"
                  "  (LAW-2 explicit promotion) and amend this member with it.")
            return 1
        violations = oc.validate_all_declarations()
    except Exception as e:  # fail-closed
        print(f"\nBLOCKED: the stage-2 vocab invariant could not be evaluated ({e}).\n"
              f"  An unevaluable value-validation gate does not read as 'passed'.")
        return 1

    if not violations:
        print(f"  [manifest-check] stage-2 vocab invariant PASS: {len(oc.declared_tools())} declared "
              f"tool(s), all rail/grain/plane/scope values in the canon enums "
              f"({', '.join(sorted(vocab))}).")
        return 0

    print("\nBLOCKED: output-contract declaration(s) carry OUT-OF-CANON vocabulary "
          "(ONTOLOGY2 type_tuple @ rule bank canonical_source):")
    for tool, vs in violations.items():
        for v in vs:
            print(f"  - {v}")
    print("  FIX: use a token from the canon enum, or (if the vocabulary must grow) extend the rule bank\n"
          "  type_tuple.<field>.enum via LAW-2 explicit-promotion-with-a-printed-denominator (~C's lane).")
    return 1


_ROUTING_SURFACE_HUD = ".tools/hooks/comp-tool-hud.sh"


def _retired_alias_decision(ti, exc, entry_tools, cov, retired, surface_refs, scanned=0,
                            tombstoned=0):
    """THE RETIRED-ALIAS INVARIANT, pure decision (unit-testable). (rc, lines); rc=1 blocks.

    NFRA_MSBEFF.R6 (2026-07-23). retired_aliases is the THIRD name-authority section (dead names).
    Two integration guardrails (base 0.8.0, shared-surface owner) + one routing-surface check:
      A. every retired name is disjoint from tools_index AND excluded -- a name that is both LIVE
         and RETIRED is a contradiction (the ledger cannot claim a live tool is dead).
      B. every declared `successor` is null OR a name in the live universe -- a dangling pointer.
      C. no committed operational ROUTING surface (HUD/prompt/skill) may CITE a declared-retired
         name -- that routes agents to a dead tool. KEYED ON THE CLOSED retired SET, never an open
         comp-* prose scan, so it cannot storm on the ~330 design-doc PROPOSAL names or on
         concept/skill/file tokens (TRIGGER_LAYER: lint the structured field, not mentions).

    live universe = ti | exc | entry_tools | cov. retired = {name: {successor, ...}}.
    surface_refs = {retired_name: [files]} -- declared-retired names found in committed surfaces.
    scanned = HOW MANY routing surfaces check C actually read. PRINT THE DENOMINATOR: check C is
    scope-predicated, so `scanned == 0` means it DID NOT RUN, and a PASS line that says "none
    cited" in that state asserts an estate-wide fact off an empty read. Measured 2026-08-06: the
    commit path's substrate contains no routing surface at all, so C ran on zero files on every
    commit while this line reported clean -- and 7 live citations of a retired name sat unseen.
    A silent false NEGATIVE outlives the loud false POSITIVE this same gate threw the same day,
    precisely because nothing it does is visible.
    """
    live = set(ti) | set(exc) | set(entry_tools) | set(cov)
    contradiction = sorted(n for n in retired if n in ti or n in exc)
    dangling = sorted(n for n, v in retired.items()
                      if (v or {}).get("successor") and (v or {}).get("successor") not in live)
    routed = {n: fs for n, fs in surface_refs.items() if n in retired}
    if not contradiction and not dangling and not routed:
        citation = (f"none cited across the {scanned} routing surface(s) in scope" if scanned
                    else "citation check (C) DID NOT RUN -- no routing surface in scope")
        tomb = f" ({tombstoned} tombstoned mention(s) exempted)" if tombstoned else ""
        return 0, [f"  [manifest-check] retired-alias invariant PASS: {len(retired)} retired name(s) "
                   f"declared, all disjoint from live+excluded ({len(live)} live), successors valid; "
                   f"{citation}{tomb}."]
    lines = [f"\nBLOCKED: retired-alias invariant (retired {len(retired)}; live universe {len(live)}):"]
    for n in contradiction:
        lines.append(f"  - {n:<24} declared RETIRED but is ALSO in tools_index/excluded -- a name is in EXACTLY ONE section")
    for n in dangling:
        s = (retired[n] or {}).get("successor")
        lines.append(f"  - {n:<24} successor '{s}' is not a live name -- dangling retirement pointer")
    for n, fs in sorted(routed.items()):
        s = (retired[n] or {}).get("successor") or "(no 1:1 successor -- see its `why`)"
        lines.append(f"  - {n:<24} RETIRED but CITED in committed routing surface(s) {fs} -- repoint to {s}")
    lines.append("  FIX: a retired name lives in retired_aliases ONLY (not tools_index/excluded); its successor\n"
                 "  is a live name or null; and no HUD/prompt/skill may route to it -- repoint or delete the citation.")
    return 1, lines


_RETIRED_SUBSTRATE = (
    "org/modules/graph/graph-call-manifest.yaml",
    "org/modules/graph/comp-coverage-map.yaml",
    _ROUTING_SURFACE_HUD,
)


def _routing_surfaces() -> list:
    """EVERY routing surface `_is_routing_surface` recognises, estate-wide, repo-relative.

    FOR THE HUMAN-FACING SUBCOMMAND ONLY. The commit path stays commit-scoped and is NOT widened
    here: doing that would block every skill/prompt commit fabric-wide on citations that already
    exist, which is a new gate on work nobody asked for.

    WHY THE SWEEP HAS TO EXIST SOMEWHERE. A commit-scoped citation check can only ever catch a
    citation added AFTER a name is retired, in a file somebody happens to commit -- so at the
    instant of retirement every EXISTING citation becomes permanently invisible to it. Retirement
    day is exactly when the estate-wide read is needed, and it was the one read nothing performed.
    """
    out = [_ROUTING_SURFACE_HUD]
    out += [str(p.relative_to(_WORKSPACE)).replace("\\", "/")
            for p in sorted(_WORKSPACE.glob("org/**/prompt.md"))]
    skills = _WORKSPACE / ".claude" / "skills"
    if skills.is_dir():
        out += [str(p.relative_to(_WORKSPACE)).replace("\\", "/")
                for p in sorted(skills.rglob("*")) if p.is_file()]
    return out


def _retired_alias_invariant(files) -> int:
    """0 = holds / not applicable. 1 = BLOCK. Substrate-scoped; deterministic; fail-closed.
    Fires when the manifest / coverage-map / an operational routing surface is committed."""
    # DEDUPE, order-preserving: `scanned` is a REPORTED DENOMINATOR now, and a file reachable by
    # two callers (the HUD is both _RETIRED_SUBSTRATE and a routing surface) would inflate it and
    # double-list its own citations. A denominator you did not dedupe is not a count.
    norm = list(dict.fromkeys(_norm(files)))

    def _is_routing_surface(f):
        return (f.endswith(_ROUTING_SURFACE_HUD) or f.endswith("/prompt.md")
                or "/.claude/skills/" in "/" + f)

    touched = (any(f.endswith(s) for s in _RETIRED_SUBSTRATE for f in norm)
               or any(_is_routing_surface(f) for f in norm))
    if not touched:
        return 0
    try:
        import re as _re
        raw = load_yaml(_MANIFEST)
        ti = set((raw.get("tools_index") or {}).keys())
        exc = set(raw.get("excluded_not_graph_use_cases") or [])
        entry_tools = {str(e.get("tool", "")).split()[0] for e in (raw.get("entries") or [])
                       if isinstance(e, dict)}
        led = load_yaml(_WORKSPACE / "org" / "modules" / "graph" / "comp-coverage-map.yaml")
        cov = ({t.get("tool") for t in (led.get("tools") or []) if isinstance(t, dict)}
               | {t.get("tool") for t in (led.get("meta_tools") or []) if isinstance(t, dict)})
        retired = raw.get("retired_aliases") or {}
        # Scan committed routing surfaces for DECLARED-RETIRED names (closed set -> no prose storm).
        surface_refs = {}
        scanned = 0
        tombstoned = 0
        for f in norm:
            if not _is_routing_surface(f):
                continue
            p = _WORKSPACE / f
            if not p.exists():
                continue
            txt = p.read_text(encoding="utf-8", errors="replace")
            scanned += 1
            # A TOMBSTONE IS THE CURE, NOT THE DISEASE. This check text-matches a NAME, so it
            # cannot tell "run this tool" from "this tool is RETIRED, do not run it" -- and the
            # second is exactly what a strike note must say. Without an exemption the invariant
            # forbids DOCUMENTING the retirements it exists to police: the only way to satisfy it
            # is to delete the explanation, leaving a silent hole where the reason used to be.
            # Same shape as the comment-blind _ADD_PARSER regex this same gate threw today, one
            # layer up; the estate's idiom for "I know, and here is why" is an audited inline
            # marker (cf. `# never-override:`, `# rail-checked:`), so this uses one.
            #   retired-tombstone: <name>     <- that name's mentions in THIS file are documentation
            # NEVER SILENT: tombstones are COUNTED and REPORTED. An exemption nobody can see is a
            # second blind spot wearing the first one's fix as a disguise.
            tomb = set(_re.findall(r"retired-tombstone:\s*([A-Za-z0-9_-]+)", txt))
            for name in retired:
                if _re.search(r"(?<![A-Za-z0-9_-])" + _re.escape(name) + r"(?![A-Za-z0-9_-])", txt):
                    if name in tomb:
                        tombstoned += 1
                        continue
                    surface_refs.setdefault(name, []).append(f)
    except Exception as e:  # fail-closed
        print(f"\nBLOCKED: the retired-alias invariant could not be evaluated ({e}).\n"
              f"  An unevaluable completeness gate does not read as 'passed'.")
        return 1
    rc, lines = _retired_alias_decision(ti, exc, entry_tools, cov, retired, surface_refs, scanned,
                                        tombstoned)
    for ln in lines:
        print(ln)
    return rc


_SUBCOMMAND_TOKEN = re.compile(r"^[a-z][a-z0-9-]*$")
# A launcher line that runs the engine. Group 1 = engine path, group 2 = the rest of the line, which
# for a PINNED wrapper carries a hardcoded subcommand literal before "$@" (e.g. `cli.py blast "$@"`).
_LAUNCHER_RUN = re.compile(r"""python\s+"?\$\{?WORKSPACE\}?/([^"\s]+\.py)"?\s*(.*)$""")


def _add_parser_names(src: str) -> set | None:
    """The subcommand literals an engine ACTUALLY registers -- read from the AST, never from text.

    Returns None when the source will not parse (the caller renders that UNKNOWN, which never
    blocks). An EMPTY SET means "parsed fine, registers nothing" -- a different fact from "could
    not tell", and the caller keeps them distinct.

    WHY AST, AND NOT A REGEX OR A COMMENT-STRIP. This replaced
        _ADD_PARSER = re.compile(r"add_parser\\(\\s*['\\\"]([a-z][a-z0-9-]*)['\\\"]")
    which matched FILE TEXT and so could not tell code from prose. Measured consequence
    2026-08-06: drift_cli.py:296 is the COMMENT
        # reconcile is ESTATE-WIDE: iam_cli.py add_parser('reconcile') takes NO positional
    -- a remark ABOUT A DIFFERENT TOOL. It was the ONLY match in the entire file, so comp-drift's
    "actual exposed derivation surface" was one string harvested from a comment, and this gate
    BLOCKED a correct commit while demanding that `reconcile` be declared into comp-which's routing
    map. comp-drift has no subparsers at all (no add_subparsers call; only a positional `target`).
    Writing that declaration would have pointed agents at a command that does not exist -- strictly
    worse than the undeclared derivation the invariant exists to prevent.

    A comment-strip would have fixed that ONE case and left the class open one layer down: a
    DOCSTRING is not a comment, so `\"\"\"... add_parser('x') ...\"\"\"` survives the strip. Under AST both
    close BY CONSTRUCTION -- a comment is not a node at all, and a string literal is a Constant, not
    a Call. Estate precedent for the same move: extract_iam.py's AST tracer (Rule 22a).

    NO REGEX FALLBACK ON A PARSE ERROR. Falling back would restore the defect precisely when the
    file is least trustworthy, and it would do so silently. Unparseable -> UNKNOWN -> never blocks.

    KNOWN AND DELIBERATE LIMIT, unchanged from the regex: a dynamically-built subparser
    (`for n in NAMES: sub.add_parser(n)`) has no string literal to read, so neither the old regex nor
    this sees it. That is a false NEGATIVE on a gate whose UNKNOWN branch never blocks -- the safe
    direction -- but it is a limit, not a guarantee, and it is recorded here rather than implied.
    """
    try:
        tree = ast.parse(src)
    except (SyntaxError, ValueError, RecursionError):
        return None
    names = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        if not (isinstance(fn, ast.Attribute) and fn.attr == "add_parser"):
            continue
        if not node.args:
            continue                                     # argparse's form is positional; no name here
        first = node.args[0]
        if isinstance(first, ast.Constant) and isinstance(first.value, str):
            if _SUBCOMMAND_TOKEN.match(first.value):      # same token grammar the regex enforced
                names.add(first.value)
    return names


def _declared_subcommands(entry: dict) -> set:
    """CONSTRAINT 2 -- the DECLARED-SIDE GRAMMAR. The tools_index `subcommands:` field mixes real
    subcommands with FLAGS ('--json') and USAGE FORMS ('<cypher>', 'sync ROW=N', 'who-can-reach <arn>').
    Without a grammar the gate compares apples to prose. Rule: take the FIRST whitespace token of each
    entry and keep it only if it is a bare lowercase word -- that promotes 'sync ROW=N' -> 'sync' and
    'who-can-reach <arn>' -> 'who-can-reach', while dropping '--json' and '<cypher>' entirely."""
    out = set()
    for raw in (entry.get("subcommands") or []):
        head = str(raw).strip().split()[0] if str(raw).strip() else ""
        if _SUBCOMMAND_TOKEN.match(head):
            out.add(head)
    return out


def _established_subcommands(tool: str):
    """The tool's ACTUAL exposed derivation surface, or None when it is NOT ESTABLISHABLE.
    Returns (subcommands:set|None, pinned:bool, why:str).

    STATIC extraction from the engine source -- never `<tool> --help`. For the auto-refresh family the
    measurement instrument would itself be a MUTATION (comp-kuzu auto-refreshes canonical on invocation),
    so a gate that ran tools to learn about them would mutate the estate to check it. Same reason ~B's
    census extracts statically.

    CONSTRAINT 1 -- PINNED WRAPPERS: a launcher that hardcodes one subcommand of a shared engine
    (`cli.py blast "$@"`) legitimately exposes exactly ONE derivation. Compare against what the WRAPPER
    exposes, not the engine's whole set, or all 5 pinned wrappers false-positive."""
    launcher = _WORKSPACE / ".tools" / tool
    if not launcher.exists():
        return None, False, "no launcher on disk"
    try:
        text = launcher.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return None, False, f"launcher unreadable ({type(e).__name__})"

    engine_rel = pinned = None
    for line in text.splitlines():
        if "comp_log_auto" in line:
            continue                                    # the telemetry appender, not the engine
        m = _LAUNCHER_RUN.search(line)
        if m:
            engine_rel = m.group(1)
            tail = (m.group(2) or "").strip()
            first = tail.split()[0] if tail.split() else ""
            if _SUBCOMMAND_TOKEN.match(first):          # a literal before "$@" == PINNED
                pinned = first
            break
    if not engine_rel:
        return None, False, "engine not resolvable from launcher"
    if pinned:
        return {pinned}, True, f"pinned wrapper -> exposes only '{pinned}'"

    engine = _WORKSPACE / engine_rel
    if not engine.exists():
        return None, False, f"engine {engine_rel} absent"
    try:
        src = engine.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        return None, False, f"engine unreadable ({type(e).__name__})"
    subs = _add_parser_names(src)
    if subs is None:
        return None, False, f"engine {engine_rel} does not parse as Python (AST)"
    if not subs:
        return None, False, "no subparsers found (flag-driven or single-derivation)"
    return subs, False, "static add_parser extraction (AST)"


def _subcommand_declaration_invariant(files) -> int:
    """0 = holds / not applicable. 1 = BLOCK.

    DECLARED SUBCOMMANDS vs THE ACTUAL SURFACE (CTO~Z arch-gate 220731Z, on ~B's LATENCY census +
    my measurement). The tools_index `subcommands:` field was populated on 65/65 tools and enforced on
    NONE -- perfect camouflage: a field present on every row and gated on none READS complete while it
    drifts. Measured drift 16 of 24 apples-to-apples tools, and the omissions include derivations
    CLAUDE.md MANDATES: comp-iam `simulate` (Rule 22a's spine) + `reconcile` (the only APPLIED-plane
    overlay), comp-pipescript `postdeps`, comp-registry `sync`. THE ROUTER CANNOT ROUTE TO THE CALLS THE
    LAW REQUIRES -- the registration invariant's own reasoning ("a tool nobody can find is
    indistinguishable from a tool that was never built") one grain down, at the DERIVATION level.

    CONSTRAINT 3 -- UNKNOWN, NEVER FAIL, where the surface is not ESTABLISHABLE. 36 of 65 tools are
    flag-driven / engine-unresolved; a gate that fired on what it cannot know would teach --no-verify,
    and a bypassed gate is worse than none. Those render UNKNOWN in the denominator and never block.

    SCOPE -- BLOCKS ONLY ON A REGISTRATION THIS COMMIT TOUCHES. Pre-existing drift is REPORTED loud but
    does not block, because a whole-universe block would freeze the fabric on 16 known-drifted tools
    before the backfill lands. This is the same shape as the output-contract invariant's condition (a):
    you cannot register/re-register a tool with a wrong subcommand declaration; the standing backlog is
    cleared by the backfill behind the gate (CTO~Z: gate FIRST, then backfill).
    DETERMINISTIC; ramp-exempt; fail-closed."""
    norm = _norm(files)
    if not (any(f.endswith(s) for s in _REGISTRATION_SUBSTRATE for f in norm)
            or any("/.tools/" in "/" + f for f in norm)):
        return 0

    try:
        raw = load_yaml(_MANIFEST)
        ti = raw.get("tools_index") or {}
        MAN = "org/modules/graph/graph-call-manifest.yaml"
        # the registrations THIS commit touches. None = UNBOUNDED (new file / not a mapping) -> treat
        # every tool as touched, the fail-closed direction: an unbounded scope must not silently narrow
        # to zero and let a drifted registration through.
        changed = _dict_diff_keys(MAN, "tools_index")
        if changed is None:
            changed = set(ti)
    except Exception as e:  # fail-closed
        print(f"\nBLOCKED: the subcommand-declaration invariant could not be evaluated ({e}).\n"
              f"  An unevaluable completeness gate does not read as 'passed'.")
        return 1

    drifted, unknown, checked = {}, [], 0
    for tool, entry in sorted(ti.items()):
        if not isinstance(entry, dict):
            continue
        actual, pinned, why = _established_subcommands(tool)
        if actual is None:
            unknown.append((tool, why))
            continue
        checked += 1
        missing = sorted(actual - _declared_subcommands(entry))
        if missing and not pinned:
            drifted[tool] = missing

    blocking = {t: m for t, m in drifted.items() if t in changed}
    print(f"  [manifest-check] subcommand-declaration: {checked} of {len(ti)} tools_index tool(s) "
          f"ESTABLISHABLE ({len(unknown)} UNKNOWN -- flag-driven/unresolved, never failed); "
          f"{len(drifted)} drifted, {len(blocking)} in THIS commit's registrations.")
    if drifted and not blocking:
        print(f"  [manifest-check] STANDING DRIFT (reported, not blocking -- backfill pending): "
              f"{', '.join(f'{t}(+{len(m)})' for t, m in sorted(drifted.items())[:8])}"
              f"{' ...' if len(drifted) > 8 else ''}")
    if not blocking:
        return 0

    print("\nBLOCKED: tools_index registration(s) in THIS commit declare an INCOMPLETE subcommand set "
          "-- comp-which cannot route an agent to an undeclared derivation:")
    for tool, missing in sorted(blocking.items()):
        print(f"  - {tool:<22} UNDECLARED: {', '.join(missing)}")
    print("  A derivation nobody can find is indistinguishable from one that was never built. FIX: add "
          "the missing subcommand(s) to this tool's tools_index `subcommands:` list.")
    return 1


def _completeness_invariants(files) -> int:
    """The family. Any member blocking blocks the commit. See the design comment above."""
    for member in (_routable_invariant, _placement_invariant, _selfroute_invariant,
                   _existence_invariant, _registration_invariant, _output_contract_invariant,
                   _stage2_vocab_invariant, _retired_alias_invariant,
                   _subcommand_declaration_invariant):
        if member(files):
            return 1
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    manifest = load_manifest()
    cfg = load_config()
    mode = args.mode or cfg.get("mode", "advisory")
    if mode not in ("advisory", "blocking"):
        sys.stderr.write(f"ERROR: invalid mode '{mode}' (advisory|blocking)\n")
        return 2
    dep_sigs = deprecated_signatures(manifest)

    files = args.file or []
    # Completeness family FIRST: deterministic + ramp-exempt. A registered-but-unreachable tool,
    # an unplaced tool, or a tool the router cannot return must never merge -- regardless of what
    # the heuristic scanners below do or do not find, and regardless of advisory|blocking mode.
    #
    # skip_completeness / completeness_only let commit_gate_runner dispatch the family ONCE per
    # commit (batched over the whole substrate) instead of once per source file -- member-3's
    # 42-tool sweep must not run N times. Absent both flags (the standalone CLI), behaviour is
    # unchanged: run the family, then the heuristic scan.
    if not getattr(args, "skip_completeness", False):
        if _completeness_invariants(files):
            return 1
    if getattr(args, "completeness_only", False):
        return 0

    all_findings: list[Finding] = []
    for f in files:
        p = Path(f)
        if not p.is_absolute():
            p = (_WORKSPACE / f).resolve()
        if not p.exists() or p.is_dir():
            continue
        if is_exempt(p, cfg):
            continue
        if p.suffix not in (".py", ".sh"):
            continue
        all_findings.extend(scan_file(p, manifest, cfg, dep_sigs))

    if not all_findings:
        return 0

    render(all_findings, mode)
    append_tally(all_findings, mode, cfg)
    errors = [f for f in all_findings if f.severity == "error"]
    if mode == "advisory":
        print(
            f"\nMANIFEST-ADVISORY: {len(all_findings)} graph-access finding(s) "
            f"({len(errors)} would block in blocking mode). Advisory -- not blocking. "
            f"See org/modules/graph/graph-call-manifest.yaml."
        )
        return 0
    # blocking
    if errors:
        print(
            f"\nBLOCKED: {len(errors)} ERROR-class graph-access finding(s). "
            f"Use the canonical manifest call, or justify the exception."
        )
        return 1
    print(
        f"\nMANIFEST-CHECK: {len(all_findings)} WARN-class finding(s), 0 blocking. "
        f"(blocking mode -- WARN is advisory)."
    )
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    manifest = load_manifest()
    cfg = load_config()
    statuses: dict[str, int] = {}
    for e in manifest.values():
        st = e.get("status", "?")
        statuses[st] = statuses.get(st, 0) + 1
    print("comp-manifest-check -- detection surface\n")
    print(f"mode (config): {cfg.get('mode')}")
    print(f"manifest: {len(manifest)} entries  " + ", ".join(f"{k}={v}" for k, v in sorted(statuses.items())))
    print("\n(A) deprecated-entry calls (manifest-driven):")
    dep = deprecated_signatures(manifest)
    if not dep:
        print("    none (0 deprecated entries in the manifest today; forward-correct when added)")
    for s in dep:
        print(f"    {s['id']} -> superseded_by {s['superseded_by']}")
    print("\n(B) rebuild-when-query tokens:")
    for t in REBUILD_TOKENS:
        qids = ", ".join(t["query_canonical"])
        missing = [q for q in t["query_canonical"] if q not in manifest]
        flag = f"  [WARN: manifest missing {missing}]" if missing else ""
        print(f"    /{t['pattern'].pattern}/ -> {qids}{flag}")
    print("\n(C) ad-hoc re-implementation patterns:")
    for p in ADHOC_PATTERNS:
        print(f"    {p['id']}: /{p['pattern'].pattern}/")
    print(f"\nexempt path substrings: {cfg.get('exempt_path_substrings')}")
    print(f"exempt basename prefixes: {cfg.get('exempt_basename_prefixes')}")
    return 0


_SYNTHETIC = """#!/usr/bin/env python3
# synthetic anti-pattern fixture for comp-manifest-check selfcheck (AC4)
import subprocess

# (B) REBUILD to answer a query -- should be flagged WARN
subprocess.run(["comp-aws", "derive", "--out", "/tmp/g"])

# (C) re-implements the gold DAG instead of comp-pipescript -- should be flagged ERROR
dag = build_firm_gold_dag(firm="bd")

# (C) raw Cypher outside comp-kuzu -- should be flagged ERROR
q = "MATCH (n:CloudNode) RETURN n.id"

# a normal line that must NOT be flagged
total = sum(range(10))
"""


def cmd_selfcheck(args: argparse.Namespace) -> int:
    manifest = load_manifest()
    cfg = load_config()
    dep_sigs = deprecated_signatures(manifest)
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as tf:
        tf.write(_SYNTHETIC)
        tmp = Path(tf.name)
    try:
        findings = scan_file(tmp, manifest, cfg, dep_sigs)
    finally:
        try:
            tmp.unlink()
        except OSError:
            pass

    cats = {f.category for f in findings}
    errors = [f for f in findings if f.severity == "error"]
    print("comp-manifest-check selfcheck (AC4 synthetic anti-pattern)\n")
    render(findings, "blocking")
    ok = (
        "B_rebuild_when_query" in cats
        and "C_adhoc_reimplementation" in cats
        and len(errors) >= 1
    )
    # the benign `total = sum(...)` line must not produce a finding -> exactly 3 expected
    benign_clean = len(findings) == 3
    print()
    if ok and benign_clean:
        print(f"PASS: {len(findings)} finding(s) (B + C present, {len(errors)} ERROR-class), 0 false-positive.")
        return 0
    print(f"FAIL: cats={sorted(cats)} errors={len(errors)} total={len(findings)} (expected 3: 1 B + 2 C).")
    return 1


def cmd_tally(args: argparse.Namespace) -> int:
    """Summarize the advisory-hit tally -> the D6 advisory->blocking ramp evidence.

    Reads the jsonl tally and reports total hits, by-category, by-file, and the distinct
    matched lines for human FP review (CTO+DS read whether any hit fired on a CORRECT
    canonical call = a precision bug to fix before flipping).
    """
    cfg = load_config()
    rel = cfg.get("tally_log") or ""
    path = rel if Path(rel).is_absolute() else (_WORKSPACE / rel)
    p = Path(path)
    if not p.exists():
        print(f"tally: empty (no findings logged yet) -- {rel}")
        return 0
    rows = []
    for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    if not rows:
        print(f"tally: empty -- {rel}")
        return 0
    by_cat: dict[str, int] = {}
    by_file: dict[str, int] = {}
    for r in rows:
        by_cat[r.get("category", "?")] = by_cat.get(r.get("category", "?"), 0) + 1
        by_file[r.get("file", "?")] = by_file.get(r.get("file", "?"), 0) + 1
    ts_first = min(r.get("ts", "") for r in rows)
    ts_last = max(r.get("ts", "") for r in rows)
    print(f"comp-manifest-check advisory-hit tally -- {rel}")
    print(f"  {len(rows)} finding(s) logged  ({ts_first} -> {ts_last})")
    print("  by category: " + ", ".join(f"{k}={v}" for k, v in sorted(by_cat.items())))
    print(f"  by file: {len(by_file)} distinct file(s)")
    for fpath, n in sorted(by_file.items(), key=lambda kv: -kv[1])[:15]:
        print(f"    {n:>3}  {fpath}")
    print("\n  FP review (each line: is this a REAL anti-pattern, or did the gate fire on a CORRECT canonical call?):")
    seen = set()
    for r in rows:
        key = (r.get("file"), r.get("lineno"), r.get("category"))
        if key in seen:
            continue
        seen.add(key)
        print(f"    [{r.get('category')}] {r.get('file')}:{r.get('lineno')}  > {r.get('line')}")
    print("\n  RAMP BAR: >= ~10 commits with 0 false-positives + B/C precision agreement -> flip config mode advisory->blocking.")
    return 0


def _report(member: str, rc: int) -> int:
    """On-demand surface only: make a GREEN legible. rc passes through untouched.

    A blocking member prints its own diagnosis, so a non-zero rc is already loud. It is the PASS
    that was mute -- and a mute pass reads exactly like a member that no-op'd out on its scope
    predicate. Name the universe that was actually swept, so the reader can tell the difference.
    """
    if rc:
        return rc
    n = len(load_yaml(_MANIFEST).get("tools_index") or {})
    scope = {
        "routable": f"{n} registered tool(s) are live routing targets",
        "existence": f"{n} registered tool(s) exist on disk AND are git-tracked",
        "placement": "every committed comp-tool has exactly one coverage-map home",
        "self-routes": f"{n} catalogued tool(s) self-route via comp-which",
        "completeness": (f"routable + placement + self-routes + existence, "
                         f"over {n} registered tool(s)"),
    }.get(member, member)
    print(f"PASS: {scope}.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="comp-manifest-check")
    sub = parser.add_subparsers(dest="cmd")

    p_check = sub.add_parser("check", help="scan file(s) for non-canonical graph access")
    p_check.add_argument("--file", action="append", help="file to check (repeatable)")
    p_check.add_argument("--mode", choices=["advisory", "blocking"], help="override config mode")
    p_check.set_defaults(func=cmd_check)

    p_list = sub.add_parser("list", help="show detection surface + manifest state")
    p_list.set_defaults(func=cmd_list)

    p_self = sub.add_parser("selfcheck", help="run on a synthetic anti-pattern (AC4)")
    p_self.set_defaults(func=cmd_selfcheck)

    p_tally = sub.add_parser("tally", help="summarize the advisory-hit tally (D6 ramp evidence)")
    p_tally.set_defaults(func=cmd_tally)

    # On-demand evaluation, independent of a changed-file list (pass the substrate so the b2 scope
    # predicate always matches). The commit path reaches it via `check`.
    #
    # ON-DEMAND IS LOUD ON PASS; the commit path stays silent. A standalone green that prints
    # NOTHING is indistinguishable from a member that no-op'd out on its scope predicate -- the
    # operator running `comp-manifest-check completeness` to answer AC1 ("a coverage check confirms
    # no orphan tool/use-case") cannot tell "swept 42 tools, all green" from "did nothing, exit 0".
    # The commit path must stay quiet (it runs on every commit); the human-facing surface must not.
    p_routable = sub.add_parser(
        "routable", help="assert every tools_index tool is a live routing target")
    p_routable.set_defaults(func=lambda _a: _report(
        "routable", _routable_invariant(_ROUTABLE_SUBSTRATE)))

    p_exist = sub.add_parser(
        "existence", help="assert every tools_index tool exists on disk AND is git-tracked")
    p_exist.set_defaults(func=lambda _a: _report(
        "existence", _existence_invariant(list(_EXISTENCE_SUBSTRATE) + [".tools/"])))

    p_comp = sub.add_parser(
        "completeness",
        help="run the completeness family (routable + placement + self-routes + existence)")
    p_comp.add_argument("--only",
                        choices=["routable", "placement", "self-routes", "existence"],
                        help="run a single member")
    p_comp.set_defaults(func=lambda a: _report(a.only or "completeness", (
        _routable_invariant(_ROUTABLE_SUBSTRATE) if a.only == "routable"
        else _placement_invariant([_PLACEMENT_MAP]) if a.only == "placement"
        else _selfroute_invariant([".tools/comp-which"]) if a.only == "self-routes"
        else _existence_invariant(list(_EXISTENCE_SUBSTRATE) + [".tools/"]) if a.only == "existence"
        else _completeness_invariants(
            list(_ROUTABLE_SUBSTRATE) + [".tools/comp-which", ".tools/"]))))

    p_retired = sub.add_parser(
        "retired-alias",
        help="assert retired_aliases coherence (disjoint sections + valid successors) and that no "
             "committed routing surface cites a declared-retired name (NFRA_MSBEFF.R6)")
    p_retired.set_defaults(func=lambda _a: _report(
        "retired-alias",
        _retired_alias_invariant(list(_RETIRED_SUBSTRATE) + _routing_surfaces())))

    args = parser.parse_args()
    if not getattr(args, "cmd", None):
        parser.print_help()
        return 2
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
