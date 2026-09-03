"""comp_dataflow.py -- comp-dataflow engine (NFRA_MSBEFF.R2, 2026-07-23, 0.8.0_AE_CloudComp~A).

Answers the question the estate could not previously ask -- Andrew's own charter gap, verbatim:
"does this value come from the CANONICAL source, or from somewhere else?" This is a DEPENDENCY /
LINEAGE question ("where did this come from"), never a data-value question ("is the number right").

THE LAW (docs/doctrine/INTENT_DENOMINATOR_SYNCHRONIZATION.md; the layer-grammar / PSTMRT item-9 form):
  A producer must not read a SERVED artifact as a value SOURCE. A served/platinum/portal-json artifact
  is a client-facing PROJECTION; sourcing new values from it means the value's origin is a serving
  projection with NO canonical per-date source -- the layer grammar running BACKWARDS.
  RF-7, the acceptance target: data/mdpf/scripts/backfill/build_legacy_compat_emit.py reads the 49F
  per-date counts from `platinum/mdpf/aggregate_aua/{date}.json` (a SERVED layer) and writes them into
  the served `json/portfolios/aum-timeseries.json` -- served<-served, no canonical source. Nothing
  detected it; it was found by manual trace.

TWO ENTRY POINTS, ONE TRAVERSAL (the one-family design the R2 TO asked for; PSTMRT item-9's GATE form
is SUBSUMED here, per CTO~Z 185533Z -- base does not double-build it):
  comp-dataflow origin <script.py>   QUERY form: every read source with its LAYER; flag served-origin
                                     reads (non-canonical value provenance). The value-origin trace.
  comp-dataflow gate [path ...]      GATE form (item-9): sweep producers; each served-origin read is a
                                     STRUCTURED finding {id, severity, owner, ref} per TRIGGER_LAYER;
                                     nonzero exit = VERDICT (a real estate finding, not a report line).

WHY A FOCUSED READER, NOT scan_lambda_io (exercised 2026-07-23, grounded -- not asserted):
  scan_lambda_io collapses `Key=f"{PLATINUM_PREFIX}/{iso}.json"` to `{*}/{*}.json`, LOSING the
  layer-bearing constant, and does not resolve function-local key vars (mpa_key/full_key). It is
  STRUCTURALLY BLIND to the RF-7 read. comp-dataflow's reader resolves module-level constants AND
  function-local variables inside f-strings -- exactly what layer classification needs. This IS the
  shared traversal item-9 reuses; it is not a second fork (item-9's traversal did not exist).

BLIND SPOTS (named in the coverage line + COUNTED at run time, never silently skipped -- R1 contract):
  - a fully-dynamic key whose path prefix does not resolve to a module/local constant renders
    UNRESOLVED and is COUNTED (a zero is never printed without its denominator).
  - a value re-imported through a NON-S3 hop (an http fetch, a DB read, a vendored/committed copy) is
    not an S3 read and is invisible to an S3-key layer trace.
  - a cross-module constant import (a prefix imported from another module) resolves only if the
    constant is module-level IN the scanned file.

SIBLING (named, not duplicated -- R2 scope D): output-key collision (2+ producers -> one sink) is
already covered by comp-clobber (clobber_scan.py, static + live etag-lineage). comp-dataflow does not
re-implement it; the write-target index here exists only to establish a producer's OUTPUT layer.

Read-only. No writes, no S3 calls (SOURCE plane -- parsed .py at working-tree HEAD). ASCII only.
Carries the R1R3 output contract (coverage + plane/vintage header, plane=mixed).
"""

from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_WS = _THIS_DIR.parent.parent.parent
if str(_WS) not in sys.path:
    sys.path.insert(0, str(_WS))

try:
    from org.modules.graph import comp_output_contract as _oc
except Exception:  # pragma: no cover
    _oc = None

sys.path.insert(0, str(_WS / ".tools"))
import _compbudget  # noqa: E402  -- RULE T shared carrier (PRD v0.4 s.4.4, NFRA_COMPEFFICACY CE-t-7)

# ---------------------------------------------------------------------------------------------------
# LAYER GRAMMAR -- the canonical-source definition (item-9 core; firm_registry aua_source is the
# optional G2b enrichment, null-until-bound, wired as a named future refinement, not a dependency).
# ---------------------------------------------------------------------------------------------------
LAYER_RANK = {"raw": 0, "bronze": 1, "silver": 2, "gold": 3, "platinum": 4, "served": 5}
# Client-facing projections. A producer must never source a VALUE from one of these.
SERVED_LAYERS = {"platinum", "served"}
# Portal serving prefixes + known legacy served artifacts that carry no explicit layer segment.
_SERVED_JSON_PREFIX = "json/"
_LEGACY_SERVED_BASENAMES = {
    "aum-timeseries.json",
    "non_model_assets.json",
    "header_metrics.json",
}


def classify_layer(key: str) -> tuple:
    """(layer_name, is_served, rank). Layer-vocab segment wins; then portal-json / legacy-served hints.
    An unclassifiable key returns ('unknown', False, -1). A key still carrying a leading {*} (no
    resolved layer prefix) is the caller's UNRESOLVED signal, distinct from a resolved 'unknown'."""
    k = key.strip()
    # Strip an s3://bucket/ scheme so the layer segment is the first key segment.
    if k.startswith("s3://"):
        rest = k[len("s3://"):]
        k = rest.split("/", 1)[1] if "/" in rest else ""
    segs = [s for s in k.split("/") if s]
    for s in segs:
        if s in LAYER_RANK:
            return (s, s in SERVED_LAYERS, LAYER_RANK[s])
    if k.startswith(_SERVED_JSON_PREFIX):
        return ("served", True, LAYER_RANK["served"])
    base = segs[-1] if segs else ""
    if base in _LEGACY_SERVED_BASENAMES:
        return ("served", True, LAYER_RANK["served"])
    return ("unknown", False, -1)


# ---------------------------------------------------------------------------------------------------
# PATH RESOLVER -- resolve a read/write path expression against module constants + function locals,
# rendering unresolved dynamic parts as {*} (so a resolved LAYER PREFIX survives even when the date
# suffix is dynamic -- the whole point of the RF-7 case).
# ---------------------------------------------------------------------------------------------------
_DYNAMIC = "{*}"

# boto3 object reads / prefix listers / pandas readers.
_S3_KEY_READ_ATTRS = {"get_object", "head_object", "download_file", "download_fileobj"}
_S3_PREFIX_ATTRS = {"list_objects", "list_objects_v2", "paginate"}
_PANDAS_READ_ATTRS = {"read_parquet", "read_json", "read_csv", "read_table", "read_excel"}
_S3_KEY_WRITE_ATTRS = {"put_object", "upload_file", "upload_fileobj", "copy_object"}


def _resolve_expr(node, scope: dict) -> str | None:
    """Resolve an AST expr to a path string with {*} for dynamic parts. None => not a string-ish
    expression at all (e.g. an io.BytesIO(...) wrapper -> caller treats as 'not a path read')."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name):
        return scope.get(node.id, _DYNAMIC)
    if isinstance(node, ast.JoinedStr):  # f-string
        parts: list[str] = []
        for v in node.values:
            if isinstance(v, ast.Constant) and isinstance(v.value, str):
                parts.append(v.value)
            elif isinstance(v, ast.FormattedValue):
                sub = _resolve_expr(v.value, scope)
                parts.append(sub if (sub is not None and sub != _DYNAMIC) else _DYNAMIC)
            else:
                parts.append(_DYNAMIC)
        return "".join(parts)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = _resolve_expr(node.left, scope)
        right = _resolve_expr(node.right, scope)
        if left is None and right is None:
            return None
        return (left or _DYNAMIC) + (right or _DYNAMIC)
    return None


def _module_constants(tree: ast.Module) -> dict:
    """Module-level `NAME = <string-ish>` constants, resolved in source order."""
    consts: dict = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            val = _resolve_expr(node.value, consts)
            if val is not None:
                consts[node.targets[0].id] = val
    return consts


def _function_scope(fn: ast.FunctionDef, module_consts: dict) -> dict:
    """A function's local string vars, resolved against module consts + earlier locals in the body."""
    scope = dict(module_consts)
    for inner in ast.walk(fn):
        if isinstance(inner, ast.Assign) and len(inner.targets) == 1 and isinstance(inner.targets[0], ast.Name):
            name = inner.targets[0].id
            if name in scope and name not in module_consts:
                continue
            val = _resolve_expr(inner.value, scope)
            if val is not None:
                scope[name] = val
    return scope


# ---------------------------------------------------------------------------------------------------
# UNRESOLVED-REASON classifier (NFRA_COMPEFFICACY CE-t-7): WHY a read renders UNRESOLVED, in the
# tool's own voice, never resolving anything -- SEPARATE and ADDITIVE from the resolver above, which
# stays byte-for-byte unchanged (BOUNDS: the enrichment is on the PRINT, not the classification).
# ---------------------------------------------------------------------------------------------------
def _is_env_access(node) -> bool:
    """STATIC AST shape match for a deploy-time-config read: os.environ.get(...), os.environ[...],
    os.getenv(...). NEVER evaluates the call and NEVER substitutes a value -- this only powers the
    UNRESOLVED-reason LABEL below (BOUNDS: never guess through deploy-time config to resolve a path)."""
    if isinstance(node, ast.Call):
        f = node.func
        if isinstance(f, ast.Attribute) and f.attr in ("get", "getenv"):
            base = f.value
            if isinstance(base, ast.Attribute) and base.attr == "environ":
                return True                                            # os.environ.get(...)
            if f.attr == "getenv" and isinstance(base, ast.Name) and base.id == "os":
                return True                                            # os.getenv(...)
    if isinstance(node, ast.Subscript):
        v = node.value
        if isinstance(v, ast.Attribute) and v.attr == "environ":
            return True                                                # os.environ["KEY"]
    return False


def _env_derived_names(tree: ast.Module) -> set:
    """Names (module-level OR function-local, any function) whose assignment's RHS is a deploy-time-
    config read per _is_env_access(). A SEPARATE pass over the same Assign shapes _module_constants()/
    _function_scope() already walk -- it never changes what those two resolve (both still return None
    for an env-access RHS, so the name still falls through to _DYNAMIC exactly as before); it only
    labels WHY a name that ends up unresolved could not have resolved to anything else."""
    names: set = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            if _is_env_access(node.value):
                names.add(node.targets[0].id)
    return names


UNRESOLVED_REASONS = ("DYNAMIC-PATH", "DEPLOY-TIME-ONLY", "FIRM-TREE-ABSENT", "OTHER")


def _unresolved_reason(path_expr, resolved: str, env_names: set) -> str:
    """WHY a read renders UNRESOLVED, from the read's own STATIC shape alone -- MECE over the domain
    'a read this tool cannot resolve to a canonical-layer path' (Rule 24 record):
      FIRM-TREE-ABSENT  a literal (non-fully-dynamic) prefix DOES resolve, but it carries no
                        recognized layer-vocabulary segment anywhere -- a real, traced path that
                        simply sits outside the layer tree, never an untraced variable.
      DEPLOY-TIME-ONLY  the value is fully dynamic ({*} only) AND at least one Name node driving it
                        is a STATICALLY detected os.environ/os.getenv read (_is_env_access) -- known
                        only by the read's OWN source shape, never by reading the live env var.
      DYNAMIC-PATH      the value is fully dynamic and at least one real Name drives it, but that
                        Name's own assignment could not be traced at all (a loop var, a function
                        parameter, an expression the resolver does not evaluate) -- the docstring's
                        own words: 'a fully-dynamic key whose path prefix does not resolve to a
                        module/local constant'.
      OTHER             the value is fully dynamic and NO Name node drives it at all (a bare call,
                        subscript, or comprehension result the resolver structurally cannot open) --
                        the reserved, always-computed fallback so no unresolved read is ever silently
                        left without a reason (Rule 24 (i), the uncovered-member hunt).
    Never guesses a VALUE for any of the four -- every branch returns a REASON LABEL only.
    """
    stripped = resolved.replace(_DYNAMIC, "").strip("/")
    if stripped:
        return "FIRM-TREE-ABSENT"
    names = {n.id for n in ast.walk(path_expr) if isinstance(n, ast.Name)}
    if names & env_names:
        return "DEPLOY-TIME-ONLY"
    if names:
        return "DYNAMIC-PATH"
    return "OTHER"


def _parent_fn_map(tree: ast.Module) -> dict:
    """node -> innermost enclosing FunctionDef (or None for module scope)."""
    enclosing: dict = {}

    def _walk(node, fn):
        for child in ast.iter_child_nodes(node):
            child_fn = child if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)) else fn
            enclosing[child] = fn  # the fn ENCLOSING this child (a fn's own scope is its parent's)
            _walk(child, child_fn)

    _walk(tree, None)
    return enclosing


def _call_attr(node: ast.Call) -> str | None:
    if isinstance(node.func, ast.Attribute):
        return node.func.attr
    if isinstance(node.func, ast.Name):
        return node.func.id
    return None


def _kw(node: ast.Call, name: str):
    for kw in node.keywords:
        if kw.arg == name:
            return kw.value
    return None


def trace_file(path: Path) -> dict:
    """Parse one producer script and return its resolved reads (with layer) + output-layer context.
    reads: [{line, kind, raw, layer, is_served, resolved, exempt, exempt_reason, unresolved_reason}].
    unresolved_reason is one of UNRESOLVED_REASONS when resolved=False, else None -- ADDITIVE
    (NFRA_COMPEFFICACY CE-t-7): it never changes is_unresolved/resolved/layer, only labels WHY."""
    try:
        src = path.read_text(encoding="utf-8")
    except Exception as e:
        return {"script": str(path), "error": f"unreadable: {e}", "reads": [], "write_layers": []}
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return {"script": str(path), "error": f"syntax: {e}", "reads": [], "write_layers": []}

    src_lines = src.splitlines()
    module_consts = _module_constants(tree)
    env_names = _env_derived_names(tree)
    fn_scopes: dict = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            fn_scopes[node] = _function_scope(node, module_consts)
    enclosing = _parent_fn_map(tree)

    def scope_for(call: ast.Call) -> dict:
        fn = enclosing.get(call)
        while fn is not None and not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            fn = enclosing.get(fn)
        return fn_scopes.get(fn, module_consts)

    def exempt_for(lineno: int) -> str | None:
        # inline `# dataflow-exempt: <reason>` on the read line or the line directly above.
        for ln in (lineno, lineno - 1):
            if 1 <= ln <= len(src_lines):
                txt = src_lines[ln - 1]
                marker = "# dataflow-exempt:"
                if marker in txt:
                    return txt.split(marker, 1)[1].strip() or "(no reason given)"
        return None

    reads: list = []
    write_layers: set = set()

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        attr = _call_attr(node)
        if attr is None:
            continue
        scope = scope_for(node)
        path_expr = None
        kind = None

        if attr in _S3_KEY_READ_ATTRS:
            kind = "s3-get"
            path_expr = _kw(node, "Key")
            if path_expr is None and attr in ("download_file", "download_fileobj") and len(node.args) >= 2:
                path_expr = node.args[1]  # (Bucket, Key, Filename)
        elif attr in _S3_PREFIX_ATTRS:
            kind = "s3-list"
            path_expr = _kw(node, "Prefix")
        elif attr in _PANDAS_READ_ATTRS:
            kind = "pandas-read"
            path_expr = node.args[0] if node.args else _kw(node, "path")
        elif attr in _S3_KEY_WRITE_ATTRS:
            wexpr = _kw(node, "Key")
            if wexpr is None and attr in ("upload_file", "upload_fileobj") and len(node.args) >= 3:
                wexpr = node.args[2]
            if wexpr is not None:
                wkey = _resolve_expr(wexpr, scope)
                if wkey:
                    layer, _served, _rank = classify_layer(wkey)
                    if layer != "unknown":
                        write_layers.add(layer)
            continue
        else:
            continue

        if path_expr is None:
            continue
        resolved = _resolve_expr(path_expr, scope)
        if resolved is None:
            continue  # not a string path (e.g. read_parquet(io.BytesIO(...))) -- the real read is elsewhere
        layer, is_served, rank = classify_layer(resolved)
        # A pandas read that resolves to a non-layer, non-s3 string is a local/buffer path -> not lineage.
        if kind == "pandas-read" and layer == "unknown" and not resolved.startswith("s3://"):
            continue
        is_unresolved = layer == "unknown" and _DYNAMIC in resolved
        ex = exempt_for(getattr(node, "lineno", 0))
        reads.append({
            "line": getattr(node, "lineno", 0),
            "kind": kind,
            "raw": resolved,
            "layer": layer,
            "is_served": is_served,
            "resolved": not is_unresolved,
            "exempt": ex is not None,
            "exempt_reason": ex,
            "unresolved_reason": (_unresolved_reason(path_expr, resolved, env_names)
                                   if is_unresolved else None),
        })

    reads.sort(key=lambda r: r["line"])
    return {"script": str(path), "error": None, "reads": reads, "write_layers": sorted(write_layers)}


# ---------------------------------------------------------------------------------------------------
# OWNER inference (TRIGGER_LAYER: a finding carries an owner). Firm-tree -> routing note.
# ---------------------------------------------------------------------------------------------------
def _owner_for(script_path: str) -> str:
    p = script_path.replace("\\", "/")
    for firm, owner in (
        ("/mdpf/", "mdpf producer lane (route MDPF findings via 1.0.0_SA_CTO~Z first)"),
        ("/black_diamond/", "bd producer lane"),
        ("/inf/", "inf producer lane"),
        ("/cot/", "cot producer lane"),
        ("/canonical/", "canonical/schwab producer lane"),
    ):
        if firm in p:
            return owner
    return "producer lane (unresolved firm tree)"


def _served_findings(trace: dict) -> list:
    """One structured finding per UNEXEMPTED served-origin read (the item-9 violation class)."""
    out = []
    for r in trace["reads"]:
        if r["is_served"] and not r["exempt"]:
            out.append({
                "id": f"DATAFLOW-SERVED-ORIGIN::{Path(trace['script']).name}::L{r['line']}",
                "severity": "blocking",
                "owner": _owner_for(trace["script"]),
                "ref": f"{trace['script']}:{r['line']}",
                "served_read": r["raw"],
                "read_layer": r["layer"],
                "producer_writes": trace["write_layers"],
                "why": "producer reads a SERVED artifact as a value source (layer grammar backwards; "
                       "value origin is a serving projection with no canonical per-date source)",
            })
    return out


# ---------------------------------------------------------------------------------------------------
# OUTPUT-CONTRACT header (R1R3) + per-run denominator
# ---------------------------------------------------------------------------------------------------
def _emit_contract(sub: str) -> None:
    if _oc is None:
        print("COVERAGE: UNKNOWN (output-contract helper unavailable); coverage NOT asserted",
              file=sys.stderr)
        print("PLANE: mixed | VINTAGE: parsed producer .py at working-tree HEAD", file=sys.stderr)
        return
    print(_oc.coverage_line("comp-dataflow", sub), file=sys.stderr)
    print(_oc.plane_header("comp-dataflow", sub), file=sys.stderr)


def _denominator(traces: list) -> dict:
    scanned = sum(len(t["reads"]) for t in traces)
    unresolved = sum(1 for t in traces for r in t["reads"] if not r["resolved"])
    served = sum(1 for t in traces for r in t["reads"] if r["is_served"] and not r["exempt"])
    exempt = sum(1 for t in traces for r in t["reads"] if r["exempt"])
    # ENRICHED (NFRA_COMPEFFICACY CE-t-7): the unresolved count's OWN reason-class breakdown, always
    # printed with all four members even at 0 -- a class reading 0 is a MEASURED zero over this
    # sweep, never an omitted member (Rule 24 (i): a zero row is not a zero denominator).
    by_reason = {rc: 0 for rc in UNRESOLVED_REASONS}
    for t in traces:
        for r in t["reads"]:
            if not r["resolved"]:
                by_reason[r["unresolved_reason"]] = by_reason.get(r["unresolved_reason"], 0) + 1
    return {"files": len(traces), "reads_scanned": scanned, "reads_unresolved": unresolved,
            "reads_unresolved_by_reason": by_reason,
            "served_origin_unexempted": served, "exempted": exempt}


# ---------------------------------------------------------------------------------------------------
# COMMANDS
# ---------------------------------------------------------------------------------------------------
_LAYER_TAG = {True: "SERVED", False: "ok"}


def cmd_origin(args) -> int:
    """QUERY form: value-origin trace of one script -- every read with its layer, served flagged."""
    _emit_contract("origin")
    path = Path(args.target)
    if not path.exists() or not path.is_file() or path.suffix != ".py":
        print(f"REFUSE: '{args.target}' did not resolve to a producer .py file -- nothing traced, "
              f"nothing concluded (input-resolution refusal, NOT a clean 'no served reads')")
        return 3
    trace = trace_file(path)
    if trace["error"]:
        print(f"REFUSE: {trace['error']} -- nothing traced")
        return 3
    if args.json:
        print(json.dumps({"trace": trace, "findings": _served_findings(trace),
                          "denominator": _denominator([trace])}, indent=2))
    else:
        print(f"ORIGIN TRACE: {trace['script']}")
        print(f"  producer output layer(s): {', '.join(trace['write_layers']) or '(none extracted)'}")
        if not trace["reads"]:
            print("  reads: (none extracted)")
        for r in trace["reads"]:
            tag = "EXEMPT" if r["exempt"] else ("SERVED-ORIGIN <<< FLAG" if r["is_served"]
                                                else ("UNRESOLVED" if not r["resolved"] else "ok"))
            print(f"  L{r['line']:<5} [{r['layer']:<8}] {tag:<22} {r['raw']}")
            if r["exempt"]:
                print(f"          exemption: {r['exempt_reason']}")
            # ENRICHED UNRESOLVED PRINT (NFRA_COMPEFFICACY CE-t-7): the reason class on the line, so
            # a reader can tell WHY without opening the producer -- never resolved by guessing, only
            # LABELLED from the read's own static shape (UNRESOLVED_REASONS, see _unresolved_reason).
            if not r["resolved"]:
                print(f"          reason: {r['unresolved_reason']}")
        d = _denominator([trace])
        by_reason = ", ".join(f"{k}={v}" for k, v in d["reads_unresolved_by_reason"].items())
        print(f"  DENOMINATOR: {d['reads_scanned']} reads scanned, {d['reads_unresolved']} unresolved-dynamic "
              f"(blind) [{by_reason}], {d['served_origin_unexempted']} served-origin flagged, {d['exempted']} exempt")
    return 1 if _served_findings(trace) else 0


def _iter_producers(paths: list) -> list:
    """Resolve the sweep population: explicit .py files, or gold/silver producers under a dir tree."""
    out: list = []
    for raw in paths:
        p = Path(raw)
        if p.is_file() and p.suffix == ".py":
            out.append(p)
        elif p.is_dir():
            for sub in sorted(p.rglob("*.py")):
                sp = str(sub).replace("\\", "/")
                if "/scripts/gold/" in sp or "/scripts/silver/" in sp or "/scripts/backfill/" in sp:
                    out.append(sub)
    return out


def cmd_gate(args) -> int:
    """GATE form (item-9): sweep producers, file a structured finding per served-origin read.

    RULE T (NFRA_COMPEFFICACY CE-t-7, PRD v0.4 s.4.4): the ONLY corpus-width loop in this tool --
    tracing N producer files -- carries a caller-settable wall-clock ceiling via the ONE shared
    .tools/_compbudget.py (carrier: --budget > env COMP_BUDGET_S > default 90s). `origin` has no
    such loop (always exactly one file) and exposes no --budget flag at all -- a declared
    non-application, not an omission: there is no unit to bound there.
    """
    _emit_contract("gate")
    population = _iter_producers(args.paths)
    if not population:
        print(f"REFUSE: no producer .py files resolved under {args.paths} -- nothing swept, "
              f"nothing concluded (NOT a clean pass)")
        return 3
    try:
        budget_s, budget_source = _compbudget.resolve_budget(args.budget)
    except ValueError as exc:
        print(f"comp-dataflow: ERROR: --budget {exc}")
        return 2

    units = sorted({str(p).replace("\\", "/") for p in population})  # deterministic scan order
    total_units = len(units)
    if args.cursor:
        if args.cursor in units:
            units = [u for u in units if u > args.cursor]
        else:
            print(f"comp-dataflow: WARNING: --cursor {args.cursor!r} does not match any resolved "
                  f"producer -- running the full requested set (no units skipped).")

    clock = _compbudget.Clock(budget_s)
    by_unit: dict = {}
    completed: list = []
    deferred_reasons: list = []
    for u in units:
        remaining = clock.remaining()
        if remaining is not None and remaining <= 0:
            deferred_reasons.append(f"{u}: budget exhausted before this unit could start")
            continue
        by_unit[u] = trace_file(Path(u))
        completed.append(u)

    traces = list(by_unit.values())
    findings = [f for t in traces for f in _served_findings(t)]
    d = _denominator(traces)
    n, N, n_deferred = len(completed), total_units, len(deferred_reasons)
    used_s = round(clock.elapsed(), 2)

    if args.json:
        print(json.dumps({"findings": findings, "denominator": d,
                          "budget": {"scanned": n, "total": N, "deferred": n_deferred,
                                     "budget_s": budget_s, "source": budget_source, "used_s": used_s}},
                         indent=2))
    else:
        print(f"comp-dataflow GATE (layer-grammar / PSTMRT item-9): {len(findings)} finding(s)")
        for f in findings:
            print(f"  [{f['severity']}] {f['id']}")
            print(f"      ref:   {f['ref']}")
            print(f"      read:  {f['served_read']}  (layer={f['read_layer']})")
            print(f"      owner: {f['owner']}")
        by_reason = ", ".join(f"{k}={v}" for k, v in d["reads_unresolved_by_reason"].items())
        print(f"  DENOMINATOR: {d['files']} producer files swept, {d['reads_scanned']} reads scanned, "
              f"{d['reads_unresolved']} unresolved-dynamic (blind) [{by_reason}], {d['exempted']} exempt")
        if n == N:
            print("  " + _compbudget.within_budget_line(n, N, "producer_file", budget_s, budget_source,
                                                         used_s))
        elif completed:
            args_repr = "comp-dataflow " + " ".join(sys.argv[1:])
            print("  " + _compbudget.budget_reached_line(budget_s, budget_source, n, N, "producer_file",
                                                          args_repr, completed[-1]))
        else:
            print(f"  BUDGET REACHED: {_compbudget.fmt(budget_s)} s ({budget_source}); scanned 0 of "
                  f"{N} producer_file(s); results are a PREFIX, not the answer; NO CURSOR YET: no "
                  f"file completed before the budget hit, so there is no last-processed unit to "
                  f"resume from; resume: re-run with a larger --budget.")
        for line in _compbudget.deferred_bucket(n_deferred, N, "producer_file", deferred_reasons):
            print("  " + line)
    return 1 if findings else 0


def cmd_self_test(_args) -> int:
    """Grounded self-test: the layer classifier + the RF-7 vs canonical discrimination, no I/O deps."""
    checks = []
    checks.append(("platinum=served", classify_layer("platinum/mdpf/aggregate_aua/{*}.json")[1] is True))
    checks.append(("silver=not-served", classify_layer("silver/eclipse/{*}/portfolios_full.parquet")[1] is False))
    checks.append(("gold=not-served", classify_layer("gold/eclipse/{*}/model_portfolio_accounts.parquet")[1] is False))
    checks.append(("portal-json=served", classify_layer("json/portfolios/aum-timeseries.json")[1] is True))
    checks.append(("bronze=not-served", classify_layer("bronze/rps/x.json")[1] is False))
    checks.append(("legacy-basename=served", classify_layer("header_metrics.json")[1] is True))
    checks.append(("dynamic=unknown", classify_layer("{*}/{*}.json")[0] == "unknown"))
    ok = all(v for _, v in checks)
    for name, v in checks:
        print(f"  {'PASS' if v else 'FAIL'}  {name}")
    print(f"self-test: {'PASS' if ok else 'FAIL'} ({sum(v for _, v in checks)}/{len(checks)})")
    return 0 if ok else 1


def main() -> int:
    # --self-test is a bare flag (argparse subparser names cannot start with '--'), handled first.
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        return cmd_self_test(None)

    ap = argparse.ArgumentParser(
        prog="comp-dataflow",
        description="Value-origin trace + canonical-source assertion (does this value come from the "
                    "canonical source, or from a served/legacy artifact?).")
    sub = ap.add_subparsers(dest="cmd", required=True)

    o = sub.add_parser("origin", help="value-origin trace of one producer script")
    o.add_argument("target", help="a producer .py file")
    o.add_argument("--json", action="store_true")
    o.set_defaults(func=cmd_origin)

    g = sub.add_parser("gate", help="layer-grammar gate (item-9) over a producer tree/files")
    g.add_argument("paths", nargs="+", help="producer .py files or dirs (gold/silver/backfill swept)")
    g.add_argument("--json", action="store_true")
    g.add_argument("--budget", metavar="N", default=None,
                    help="RULE T (PRD s.4.4, shared .tools/_compbudget): wall-clock ceiling in "
                         "seconds for this sweep (carrier: --budget > env COMP_BUDGET_S > default "
                         "%s s); --budget 0 = unbounded. Only 'gate' has this flag -- 'origin' "
                         "traces exactly one file and has no corpus-width loop to bound." % _compbudget.fmt(_compbudget.DEFAULT_BUDGET_S))
    g.add_argument("--cursor", metavar="PATH", default=None,
                    help="resume a budget-limited sweep after producer PATH (named in an earlier "
                         "BUDGET REACHED line's resume command); skips every unit up to and "
                         "including it, in the same sorted scan order.")
    g.set_defaults(func=cmd_gate)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
