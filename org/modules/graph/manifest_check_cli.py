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
            "hit the canonical persisted Kuzu DB (manifest cloud.* / xlayer.*)."
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
def load_yaml(path: Path) -> dict:
    if not path.exists():
        sys.stderr.write(f"ERROR: not found: {path}\n")
        sys.exit(2)
    with path.open(encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


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
def cmd_check(args: argparse.Namespace) -> int:
    manifest = load_manifest()
    cfg = load_config()
    mode = args.mode or cfg.get("mode", "advisory")
    if mode not in ("advisory", "blocking"):
        sys.stderr.write(f"ERROR: invalid mode '{mode}' (advisory|blocking)\n")
        return 2
    dep_sigs = deprecated_signatures(manifest)

    files = args.file or []
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

    args = parser.parse_args()
    if not getattr(args, "cmd", None):
        parser.print_help()
        return 2
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
