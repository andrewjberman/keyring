"""comp_recognizers_pyfield -- NFRA_PYFIELD.TO-1: `PyFieldRecognizer`, D1-conformant field-grain
FLOWS_TO edges for Python gold/silver scripts, with an honest coverage declaration for everything it
cannot resolve.

WHY THIS EXISTS. `FLOWS_TO` (961 edges) and `PROP_PASSES` (1382) are 100% `layer=portal`. On the aws
and pipeline substrates -- where every gold script lives -- field grain does not exist in the graph at
all. This populates it, so `comp-pipescript` can emit a per-script field IO list and `comp-dataflow`
can walk it BACKWARD: Andrew's migration question, "if I change this field, what breaks downstream"
(Andrew-direct 2026-08-07, "when we do migrations it will be essential to be able to track field
dependencies in pipelines").

>> THE ONE RULE THIS MODULE IS BUILT AROUND: A COVERAGE FIGURE IS UNSTATEABLE WITHOUT BOTH PINS. <<
Both the RESOLVER and the MARKER SET are INSTRUMENT PROPERTIES, measured rather than theorised:
  * the column FLOOR moves 5.5x with the MARKER SET   (MINIMAL 228 / STRICT_DERIVED 1059 / WIDE 1064)
  * binding REACH moves 3.6x with the RESOLVER, on ONE IDENTICAL POPULATION (v1 434 -> v2 1555)
So "the recognizer resolves N% of columns" is not true or false -- it is UNDERSPECIFIED, in the
specific way that lets any number be defended after the fact. `Pins` is therefore a REQUIRED argument,
not an option, and `format_coverage()` raises rather than render a figure without one. A number that
cannot print its own frame is the defect this whole project exists to prevent.

THE FOUR AXES (NFRA_PYFIELD PRD Sec.9 + TO-1 criterion 6 -- all four from the start, not binding-first;
the axes are largely independent, so a binding-only build leaves a cheap signal on the table):
  1. BINDING-side  -- names bound from a pandas CONSTRUCTOR SET, propagated flow-locally to a fixed
                      point. The honest analogue of the portal extractor's TypeChecker.getSymbol.
  2. USAGE-side    -- a pandas method called ON the subscript result proves the base. Fires exactly
                      where binding-side is blind (params, cross-file arrivals, reassignment).
  3. EXCLUSION-side-- DERIVED from the installed pandas API at runtime and VERSION-PINNED.
  4. ITERROWS      -- `for idx, row in df.iterrows(): row['col']` IS a column access (237 sites).

LIFTED, NOT REINVENTED (BUILD LADDER rung 2, TO-1 requirement 2). The resolver mechanism comes from
`4.0.0_SA_CRO`'s TO-0 probe (`org/tier1_exec/4.0.0_SA_CRO/scripts/pyfield_column_probe.py`, self-test
0 failures at lift time): `derive_marker_sets`, `derive_constructors`, `expr_shape`, `dotted`,
`ScopeInfo`, `collect_scopes`, `annotation_is_df`, `summarize_local_returns`, `resolve_df_names`.
v1 is kept selectable so the 3.6x delta is RE-DERIVABLE rather than a claim about a resolver nobody
can run. Neither addition is type inference -- mypy/pyright/pytype/jedi are ALL ABSENT (rung 5 was
run); no dependency is added.

WHAT IS GENUINELY NEW HERE, and it is the one thing CRO's probe does not do: CRO's probe is an
EVIDENCE EXTRACTOR that deliberately emits no verdict. This is the CLASSIFIER + EMITTER -- it decides,
emits D1 edges, and carries the honest-degrade channel. It also adds ITERROWS binding, which the probe
does not attempt (its self-test asserts loop vars do NOT resolve -- correct for a list, wrong for an
`.iterrows()` row).

THE ITERROWS TUPLE-POSITION TRAP, stated because getting it backwards silently mis-calls every site:
`for idx, row in df.iterrows()` yields `(index, Series)`. ONLY element [1] is the row Series. Binding
element [0] would make `idx['x']` read as a column. And a SINGLE-target `for r in df.iterrows()` binds
`r` to the whole TUPLE, where `r['x']` is not a column access at all -- so single-target is NOT bound.
Measured on the corpus: naive both-elements binding yields 237 sites across loop targets that include
`acct`, `k`, `c`, `d`, `e`, `v` -- index variables, not rows.

COVERAGE IS THE PRODUCT, NOT A BYPRODUCT (LAW-1 honest-degrade, TO-1 criterion 3):
  * ZERO UNRESOLVED IS A FAILURE, NOT A PASS. The 491 expr-base sites (`f()["x"]`, `d["a"]["b"]`) are
    UNREACHABLE BY CONSTRUCTION -- a name-keyed mechanism structurally cannot attempt them. A run
    reporting full coverage has lost the honest-degrade channel, which is worse than low coverage
    because it is low coverage that lies.
  * AND THE 491 ARE NEVER SCORED AS MISSES. They are counted in their own `unattemptable` channel. A
    bar that counts them is unpassable by construction.

Design: docs/architecture/NFRA_PYFIELD_PRD.md @004588f9cb (v1.0, AUTHORIZED) Sec.3 (flow-local
inference, option (b), with (c) as mandatory coverage policy), Sec.4 (component spec), Sec.9.
TO: org/tier2_senior/0.8.0_AE_CloudComp/task_orders/NFRA_PYFIELD.TO-1.pyfieldrecognizer.md @f6418f78e7
Author: 0.8.0_AE_CloudComp (NFRA_PYFIELD.TO-1). 2026-08-07.
"""

from __future__ import annotations

import ast
import json
import os
import sys
from dataclasses import dataclass, field as dc_field
from datetime import datetime, timezone
from typing import Iterable

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from comp_recognizer_sdk import (  # noqa: E402
    Recognizer, Site, EnrichedTree, FrontEndCapability, emit_cse, EntityRef, RelationshipDelta,
    Provenance, Entity, Relationship, Transformation,
)
from cse_schema import EdgeKind  # noqa: E402

__all__ = [
    "PyFieldRecognizer", "Pins", "build_pins", "format_coverage",
    "derive_marker_sets", "derive_constructors", "resolve_df_names", "collect_scopes",
    "analyze_tree", "PROPS_KEYS",
]

# The SEVEN keys the portal FLOWS_TO producer emits. THE TWO SUBSTRATES ARE ONE SCHEMA (PRD Sec.4) --
# this is what lets the semantic-evolution loop see python field grain at all. Verified against the
# live portal artifact (org/modules/graph/tsgraph_spike/out/live_flowsto.json, 961 edges): every edge
# carries exactly {condition, dstField, kind, rename, resolution, srcField, via}.
PROPS_KEYS = ("srcField", "dstField", "kind", "rename", "condition", "via", "resolution")

# Resolver identity. BOTH are shipped and BOTH stay runnable -- the delta between them IS the
# measurement of how much "undecidable" was analyzer weakness rather than corpus ambiguity.
RESOLVER_V1 = "pyfield-flowlocal/v1"   # constructor-seeded floor ONLY
RESOLVER_V2 = "pyfield-flowlocal/v2"   # + DataFrame-typed param annotations + one-hop local returns


# ---------------------------------------------------------------------------
# PINS -- criterion 1. Not optional, not a keyword with a default: a coverage figure without these
# is UNDERSPECIFIED, and this type exists so that fact is enforced by construction rather than
# remembered by an author.
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Pins:
    resolver: str               # RESOLVER_V1 | RESOLVER_V2 -- resolver identity + version
    marker_set: str             # MINIMAL | STRICT_DERIVED | WIDE -- marker-set identity
    pandas_version: str         # the pandas the marker set was DERIVED from
    marker_set_size: int        # how many members that derivation produced
    vintage: str                # measurement vintage, UTC
    trees_swept: tuple = ()     # requirement 4: declared in the SAME sentence as any figure
    trees_unswept: tuple = ()

    def line(self) -> str:
        swept = ", ".join(self.trees_swept) or "(none declared)"
        unswept = ", ".join(self.trees_unswept) or "(none declared)"
        return (f"resolver={self.resolver} marker_set={self.marker_set}"
                f"@pandas-{self.pandas_version}(n={self.marker_set_size}) vintage={self.vintage} "
                f"| SWEPT: {swept} | UNSWEPT: {unswept}")


def build_pins(resolver: str = RESOLVER_V2, marker_set: str = "STRICT_DERIVED",
               trees_swept: tuple = (), trees_unswept: tuple = ()) -> Pins:
    meta, sets = derive_marker_sets()
    if marker_set not in sets:
        raise ValueError(f"unknown marker set {marker_set!r}; derived sets are {sorted(sets)}")
    if resolver not in (RESOLVER_V1, RESOLVER_V2):
        raise ValueError(f"unknown resolver {resolver!r}")
    return Pins(resolver=resolver, marker_set=marker_set, pandas_version=meta["pandas_version"],
                marker_set_size=len(sets[marker_set]),
                vintage=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ"),
                trees_swept=tuple(trees_swept), trees_unswept=tuple(trees_unswept))


# ---------------------------------------------------------------------------
# MARKER SETS + CONSTRUCTORS -- DERIVED from the installed pandas API, never hand-drawn (criterion 5).
# LIFTED from CRO's TO-0 probe. Do NOT lift `_DF_METHODS`: it is hand-drawn, incident-driven, 71 names
# against a real universe of 240 (missing 170 = 70.8%), carries one entry that can never fire
# (`concat` is `pd.concat`, a module function, not a DataFrame attribute), and is not version-pinned.
# It is a roster wearing a predicate's clothing.
# ---------------------------------------------------------------------------
def derive_marker_sets():
    """Return (meta, sets). Every set DERIVED from the installed pandas, never hand-listed."""
    import pandas as pd

    df_attrs = {a for a in dir(pd.DataFrame) if not a.startswith("_")}
    sr_attrs = {a for a in dir(pd.Series) if not a.startswith("_")}
    pandas_attrs = df_attrs | sr_attrs

    def pub(t):
        return {a for a in dir(t) if not a.startswith("_")}

    builtin_attrs = pub(dict) | pub(list) | pub(str) | pub(set) | pub(tuple) | pub(object)
    sets = {
        "MINIMAL": {"value_counts", "nunique", "fillna"},        # no dict has these
        "STRICT_DERIVED": pandas_attrs - builtin_attrs,          # on NO common builtin container
        "WIDE": pandas_attrs - pub(dict),                        # any non-dict method (over-claims)
    }
    return {"pandas_version": pd.__version__, "universe_df_or_series": len(pandas_attrs),
            "sizes": {k: len(v) for k, v in sets.items()}}, sets


def derive_constructors():
    """DataFrame-producing constructors, seeded from pandas' own API surface. A FLOOR by design."""
    import pandas as pd

    readers = {a for a in dir(pd) if a.startswith("read_")}
    frame_makers = {"DataFrame", "Series", "concat", "merge", "merge_asof", "merge_ordered",
                    "pivot", "pivot_table", "crosstab", "get_dummies", "json_normalize"}
    return readers | (frame_makers & {a for a in dir(pd)}) | {"json_normalize"}


# ---------------------------------------------------------------------------
# AST helpers -- LIFTED from CRO's probe (rung 2).
# ---------------------------------------------------------------------------
def dotted(node) -> str:
    """Render a dotted name for Name/Attribute chains; '<expr>' for anything else."""
    parts = []
    cur = node
    while True:
        if isinstance(cur, ast.Attribute):
            parts.append(cur.attr)
            cur = cur.value
        elif isinstance(cur, ast.Name):
            parts.append(cur.id)
            break
        elif isinstance(cur, ast.Call):
            parts.append("()")
            cur = cur.func
        elif isinstance(cur, ast.Subscript):
            parts.append("[]")
            cur = cur.value
        else:
            parts.append("<expr>")
            break
    return ".".join(reversed(parts))


def expr_shape(node) -> str:
    """A compact, stable, deliberately-lossy descriptor of an expression's SHAPE (evidence, not a type)."""
    if node is None:
        return "none"
    if isinstance(node, ast.Call):
        return "call:" + dotted(node.func)
    if isinstance(node, ast.Dict):
        return "dict-literal"
    if isinstance(node, ast.DictComp):
        return "dict-comprehension"
    if isinstance(node, ast.ListComp):
        return "list-comprehension"
    if isinstance(node, ast.List):
        return "list-literal"
    if isinstance(node, ast.Subscript):
        return "subscript:" + dotted(node.value)
    if isinstance(node, ast.Attribute):
        return "attribute:" + dotted(node)
    if isinstance(node, ast.Name):
        return "name:" + node.id
    if isinstance(node, ast.Constant):
        return "const:" + type(node.value).__name__
    if isinstance(node, ast.BinOp):
        return "binop"
    if isinstance(node, ast.Tuple):
        return "tuple"
    return type(node).__name__.lower()


def annotation_is_df(node) -> bool:
    """True if a type annotation names a pandas frame/series. Sound, free, and often present."""
    if node is None:
        return False
    try:
        txt = ast.unparse(node)
    except Exception:  # noqa: BLE001 -- an unparseable annotation is simply not evidence
        return False
    txt = txt.strip().strip('"').strip("'")
    return ("DataFrame" in txt) or ("pd.Series" in txt) or txt.endswith("Series")


class ScopeInfo:
    """Binding evidence for one lexical scope (module or function)."""

    __slots__ = ("name", "params", "assigns", "loopvars", "withvars", "iterrows_rows", "parent")

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.params = set()
        self.assigns = {}         # name -> [rhs shape, ...]
        self.loopvars = {}        # name -> iterable shape
        self.withvars = {}        # name -> context shape
        self.iterrows_rows = {}   # name -> the df base the .iterrows() was called on (axis 4)

    def lookup(self, ident):
        cur = self
        while cur is not None:
            ev = {}
            if ident in cur.params:
                ev["is_param"] = True
            if ident in cur.assigns:
                ev["assigned_from"] = cur.assigns[ident]
            if ident in cur.loopvars:
                ev["loop_over"] = cur.loopvars[ident]
            if ident in cur.withvars:
                ev["with_from"] = cur.withvars[ident]
            if ident in cur.iterrows_rows:
                ev["iterrows_row_of"] = cur.iterrows_rows[ident]
            if ev:
                ev["found_in_scope"] = cur.name
                return ev
            cur = cur.parent
        return {}

    def iterrows_lookup(self, ident):
        """Walk OUTWARD for an iterrows-row binding, but STOP at the nearest scope that SHADOWS the
        name. Python resolves a name in the innermost binding scope; a parameter or local assignment
        named `row` is NOT the module-level `for _, row in df.iterrows()` row.

        MEASURED over-reach this closes: without the shadow check, a module-level iterrows loop makes
        EVERY function in the file that takes a `row` parameter resolve `row["Records"]` as a
        DataFrame column. That is a false positive that inflates the very axis criterion 4 asks the
        recognizer to state a number for -- and it inflates it silently, because a false resolve
        leaves no trace in the unresolved channel.
        """
        cur = self
        while cur is not None:
            if ident in cur.iterrows_rows:
                return cur.iterrows_rows[ident]
            if ident in cur.params or ident in cur.assigns or ident in cur.loopvars \
               or ident in cur.withvars:
                return None       # shadowed by a nearer binding -- do not inherit the outer row
            cur = cur.parent
        return None


def _iterrows_base(iter_node):
    """If `iter_node` is a `<base>.iterrows()` call, return the dotted base; else None."""
    if isinstance(iter_node, ast.Call) and isinstance(iter_node.func, ast.Attribute) \
       and iter_node.func.attr == "iterrows":
        return dotted(iter_node.func.value)
    return None


def collect_scopes(tree, modname):
    """Build a scope tree with binding evidence. Returns (root, node->scope map).

    AXIS 4 (iterrows) is bound HERE, and the tuple position is load-bearing:
    `for idx, row in df.iterrows()` yields `(index, Series)`, so ONLY elts[1] is the row.
    A single-target `for r in df.iterrows()` binds the whole TUPLE and is NOT bound.
    """
    root = ScopeInfo(modname)
    node_scope = {}

    def targets_of(t):
        if isinstance(t, ast.Name):
            return [t.id]
        if isinstance(t, (ast.Tuple, ast.List)):
            out = []
            for e in t.elts:
                out.extend(targets_of(e))
            return out
        return []

    def bind_iterrows(scope, target, iter_node):
        base = _iterrows_base(iter_node)
        if base is None:
            return
        # ONLY the second element of a 2-tuple target is the row Series. Anything else -- a bare
        # name (the whole tuple), a 1-tuple, a 3+-tuple -- is NOT a row and is deliberately not bound.
        if isinstance(target, (ast.Tuple, ast.List)) and len(target.elts) == 2 \
           and isinstance(target.elts[1], ast.Name):
            scope.iterrows_rows[target.elts[1].id] = base

    def walk(node, scope):
        node_scope[id(node)] = scope
        for child in ast.iter_child_nodes(node):
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                sub = ScopeInfo(f"{scope.name}.{child.name}", scope)
                a = child.args
                for arg in list(a.args) + list(a.posonlyargs) + list(a.kwonlyargs):
                    sub.params.add(arg.arg)
                    if annotation_is_df(arg.annotation):
                        sub.assigns.setdefault(arg.arg, []).append("annotation:DataFrame")
                if a.vararg:
                    sub.params.add(a.vararg.arg)
                if a.kwarg:
                    sub.params.add(a.kwarg.arg)
                node_scope[id(child)] = scope
                walk(child, sub)
            elif isinstance(child, ast.ClassDef):
                sub = ScopeInfo(f"{scope.name}.{child.name}", scope)
                node_scope[id(child)] = scope
                walk(child, sub)
            else:
                if isinstance(child, ast.Assign):
                    shape = expr_shape(child.value)
                    for t in child.targets:
                        for nm in targets_of(t):
                            scope.assigns.setdefault(nm, []).append(shape)
                elif isinstance(child, (ast.AugAssign, ast.AnnAssign)):
                    if isinstance(child.target, ast.Name):
                        scope.assigns.setdefault(child.target.id, []).append(
                            expr_shape(getattr(child, "value", None)))
                elif isinstance(child, (ast.For, ast.AsyncFor)):
                    shape = expr_shape(child.iter)
                    for nm in targets_of(child.target):
                        scope.loopvars.setdefault(nm, shape)
                    bind_iterrows(scope, child.target, child.iter)
                elif isinstance(child, (ast.With, ast.AsyncWith)):
                    for item in child.items:
                        if item.optional_vars is not None:
                            shape = expr_shape(item.context_expr)
                            for nm in targets_of(item.optional_vars):
                                scope.withvars.setdefault(nm, shape)
                elif isinstance(child, ast.comprehension):
                    shape = expr_shape(child.iter)
                    for nm in targets_of(child.target):
                        scope.loopvars.setdefault(nm, shape)
                    bind_iterrows(scope, child.target, child.iter)
                walk(child, scope)

    walk(tree, root)
    return root, node_scope


def summarize_local_returns(tree, constructors):
    """ONE-HOP return summary: which local `def`s return a DataFrame. Iterated to a fixed point so
    helper->helper chains resolve. Flow-local per body; NOT type inference, does not cross files."""
    funcs = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            funcs[node.name] = node

    df_funcs = set()
    for name, fn in funcs.items():
        if annotation_is_df(fn.returns):
            df_funcs.add(name)

    changed, passes = True, 0
    while changed and passes < 6:
        changed = False
        passes += 1
        for name, fn in funcs.items():
            if name in df_funcs:
                continue
            sub = ScopeInfo(name)
            for arg in list(fn.args.args) + list(fn.args.posonlyargs) + list(fn.args.kwonlyargs):
                sub.params.add(arg.arg)
                if annotation_is_df(arg.annotation):
                    sub.assigns.setdefault(arg.arg, []).append("call:pd.DataFrame")
            for ch in ast.walk(fn):
                if isinstance(ch, ast.Assign):
                    for t in ch.targets:
                        if isinstance(t, ast.Name):
                            sub.assigns.setdefault(t.id, []).append(expr_shape(ch.value))
            bound = resolve_df_names(sub, constructors, df_funcs)
            for ch in ast.walk(fn):
                if isinstance(ch, ast.Return) and ch.value is not None:
                    sh = expr_shape(ch.value)
                    head = sh.split(":", 1)[1].split(".")[0] if ":" in sh else ""
                    if (sh.startswith("call:") and (sh.split(":", 1)[1].split(".")[-1] in constructors
                                                    or head in bound or head in df_funcs)) \
                       or (sh.startswith(("subscript:", "attribute:", "name:")) and head in bound):
                        df_funcs.add(name)
                        changed = True
                        break
    return df_funcs


def resolve_df_names(scope: ScopeInfo, constructors, df_funcs=frozenset()) -> set:
    """Flow-local fixed point: which names in this scope are bound to a DataFrame. A FLOOR by
    construction -- it cannot see cross-file arrivals or reassignment through an unrecognised call."""
    bound = set()
    changed, passes = True, 0
    while changed and passes < 8:
        changed = False
        passes += 1
        for nm, shapes in scope.assigns.items():
            if nm in bound:
                continue
            for sh in shapes:
                hit = False
                if sh.startswith("call:"):
                    callee = sh[5:]
                    tail, head = callee.split(".")[-1], callee.split(".")[0]
                    if tail in constructors and head in ("pd", "pandas", tail):
                        hit = True
                    elif head in bound:
                        hit = True                      # df.merge(...) / df.groupby(...).agg(...)
                    elif "." not in callee and callee in df_funcs:
                        hit = True                      # a local helper VERIFIED to return a DataFrame
                elif sh.startswith("subscript:"):
                    hit = sh.split(":", 1)[1].split(".")[0] in bound      # df[mask] / df[cols]
                elif sh.startswith("attribute:"):
                    hit = sh.split(":", 1)[1].split(".")[0] in bound
                elif sh.startswith("name:"):
                    hit = sh[5:] in bound
                elif sh == "annotation:DataFrame":
                    hit = True                          # declared by the author, not inferred
                if hit:
                    bound.add(nm)
                    changed = True
                    break
    return bound


# ---------------------------------------------------------------------------
# THE CLASSIFIER -- the genuinely new half. CRO's probe extracts evidence and deliberately emits no
# verdict; this decides, and records WHICH AXIS decided so a coverage figure can be attributed.
# ---------------------------------------------------------------------------
@dataclass
class ColumnRef:
    base: str            # the resolved DataFrame-ish base name
    col: str             # the column name
    line: int
    axis: str            # binding | usage | iterrows -- WHICH axis proved it
    src_line: str = ""


@dataclass
class FlowSite:
    """One `dst_base[dst_col] = <expr involving src columns>` assignment -- a real field-grain flow."""
    dst: ColumnRef
    srcs: list
    line: int
    condition: str = ""
    rhs_is_bare_read: bool = False
    src_text: str = ""


@dataclass
class TreeAnalysis:
    flows: list = dc_field(default_factory=list)
    attempted: int = 0            # name-based string-literal subscripts (the attemptable population)
    unattemptable: list = dc_field(default_factory=list)   # <expr> bases -- NEVER scored as misses
    unresolved: list = dc_field(default_factory=list)      # name-based but no axis resolved it
    resolved_cols: int = 0
    by_axis: dict = dc_field(default_factory=dict)


def _enclosing_conditions(tree):
    """Map id(stmt) -> the nearest enclosing `if` test, unparsed. Populates `condition` (portal
    defect #3: the portal producer leaves this 4.8% populated; we do better where it is cheap)."""
    out = {}

    def walk(node, cond):
        for child in ast.iter_child_nodes(node):
            newcond = cond
            if isinstance(node, ast.If) and child in node.body:
                try:
                    newcond = ast.unparse(node.test)
                except Exception:  # noqa: BLE001
                    newcond = cond
            out[id(child)] = newcond
            walk(child, newcond)
    walk(tree, "")
    return out


def analyze_tree(tree_ast, text, source, *, resolver=RESOLVER_V2, marker_set="STRICT_DERIVED",
                 constructors=None, sets=None) -> TreeAnalysis:
    """Run all four axes over one parsed module. Pure; no emission. Returns a TreeAnalysis."""
    if constructors is None:
        constructors = derive_constructors()
    if sets is None:
        _meta, sets = derive_marker_sets()
    markers = sets[marker_set]

    root, node_scope = collect_scopes(tree_ast, os.path.basename(source))

    if resolver == RESOLVER_V1:
        # Strip the v2-only evidence so the two resolvers are cleanly separable and the delta is real.
        for sc in set(node_scope.values()):
            for k in list(sc.assigns):
                sc.assigns[k] = [s for s in sc.assigns[k] if s != "annotation:DataFrame"]
                if not sc.assigns[k]:
                    del sc.assigns[k]
        df_funcs = frozenset()
    else:
        df_funcs = summarize_local_returns(tree_ast, constructors)

    df_names_cache = {}

    def scope_df(sc):
        if id(sc) not in df_names_cache:
            df_names_cache[id(sc)] = resolve_df_names(sc, constructors, df_funcs)
        return df_names_cache[id(sc)]

    parent = {}
    for node in ast.walk(tree_ast):
        for child in ast.iter_child_nodes(node):
            parent[id(child)] = node

    conds = _enclosing_conditions(tree_ast)
    lines = text.splitlines()
    an = TreeAnalysis()
    an.by_axis = {"binding": 0, "usage": 0, "iterrows": 0}
    resolved_nodes = {}   # id(Subscript) -> ColumnRef

    # ---- pass 1: classify every string-literal subscript through the axes ----
    for node in ast.walk(tree_ast):
        if not isinstance(node, ast.Subscript):
            continue
        sl = node.slice
        if not (isinstance(sl, ast.Constant) and isinstance(sl.value, str)):
            continue
        locus = f"L{node.lineno}"
        src_line = lines[node.lineno - 1].strip() if node.lineno - 1 < len(lines) else ""

        if not isinstance(node.value, ast.Name):
            # UNREACHABLE BY CONSTRUCTION -- a name-keyed mechanism cannot attempt an <expr> base.
            # Counted in its OWN channel and NEVER scored as a recognizer miss (criterion 3).
            an.unattemptable.append((locus, f"expr-base `{dotted(node.value)}[{sl.value!r}]` -- "
                                            f"unreachable by construction (name-keyed mechanism)"))
            continue

        an.attempted += 1
        base_name = node.value.id
        sc = node_scope.get(id(node), root)

        axis = None
        if sc.iterrows_lookup(base_name) is not None:
            axis = "iterrows"                                    # axis 4
        elif base_name in scope_df(sc):
            axis = "binding"                                     # axis 1
        else:
            par = parent.get(id(node))                           # axis 2 (usage-side)
            if isinstance(par, ast.Attribute) and par.value is node and par.attr in markers:
                axis = "usage"

        if axis is None:
            an.unresolved.append((locus, f"base `{base_name}` not proven a DataFrame by any axis "
                                         f"(resolver={resolver}, marker_set={marker_set})"))
            continue
        an.resolved_cols += 1
        an.by_axis[axis] += 1
        resolved_nodes[id(node)] = ColumnRef(base=base_name, col=sl.value, line=node.lineno,
                                             axis=axis, src_line=src_line)

    # ---- pass 2: field-grain FLOWS_TO -- a resolved column WRITTEN from resolved column read(s) ----
    for node in ast.walk(tree_ast):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        tgt = node.targets[0]
        dst = resolved_nodes.get(id(tgt))
        if dst is None:
            continue
        srcs = [resolved_nodes[id(ch)] for ch in ast.walk(node.value) if id(ch) in resolved_nodes]
        if not srcs:
            continue
        bare = isinstance(node.value, ast.Subscript) and id(node.value) in resolved_nodes
        an.flows.append(FlowSite(
            dst=dst, srcs=srcs, line=node.lineno, condition=conds.get(id(node), "") or "",
            rhs_is_bare_read=bare,
            src_text=(lines[node.lineno - 1].strip() if node.lineno - 1 < len(lines) else "")))
    return an


def _edge_kind(flow: FlowSite, src: ColumnRef) -> tuple:
    """(EdgeKind value, rename bool). passthrough = a bare read of the same column name; rename = a
    bare read under a different name; anything computed or guarded = recompute_guarded."""
    if flow.condition:
        return EdgeKind.RECOMPUTE_GUARDED.value, (src.col != flow.dst.col)
    if flow.rhs_is_bare_read and len(flow.srcs) == 1:
        if src.col == flow.dst.col:
            return EdgeKind.PASSTHROUGH.value, False
        return EdgeKind.RENAME.value, True
    return EdgeKind.RECOMPUTE_GUARDED.value, (src.col != flow.dst.col)


# ---------------------------------------------------------------------------
# THE RECOGNIZER -- the ONE new component (PRD Sec.3: "Nothing else is new").
# ---------------------------------------------------------------------------
class PyFieldRecognizer(Recognizer):
    """Emit D1-conformant field-grain FLOWS_TO edges for Python gold/silver scripts.

    One CSE per (src column -> dst column) flow: subject = the source Field, edge = FLOWS_TO -> the
    destination Field, carrying the governed EdgeKind and the lexical guard condition. `props` carries
    the SAME SEVEN KEYS as the portal producer, so the two substrates are ONE SCHEMA.

    LEXICAL_AST tier: this recognizer resolves flow-locally from the AST. It does NOT claim
    cross-file resolution -- that is RESOLVED_SEMANTIC, and Python has no getSymbol equivalent
    (mypy/pyright/pytype/jedi all absent; no dependency added).
    """

    artifact_class = "python"
    concept = "py-field-flows-to"
    requires = FrontEndCapability.LEXICAL_AST
    compiler_id = "code-compiler"
    emits = (Entity.FIELD.value, Relationship.FLOWS_TO.value,
             EdgeKind.PASSTHROUGH.value, EdgeKind.RENAME.value, EdgeKind.RECOMPUTE_GUARDED.value)

    def __init__(self, pins: Pins = None, *, resolver: str = RESOLVER_V2,
                 marker_set: str = "STRICT_DERIVED"):
        # Pins are REQUIRED to publish a figure; the recognizer builds a default set if not given so
        # it stays constructible in a registry, but `format_coverage` still refuses an absent one.
        self.pins = pins or build_pins(resolver=resolver, marker_set=marker_set)
        self.resolver = self.pins.resolver
        self.marker_set = self.pins.marker_set
        self._constructors = derive_constructors()
        _meta, self._sets = derive_marker_sets()
        self.last_analysis = None
        self.edge_records = []     # the {src, dst, props} artifact -- symmetric with live_flowsto.json

    # -- the resolution string, carrying its own pins. The python analogue of the portal producer's
    # -- "getSymbol on field-read prop access -> declaring type (TypeChecker)".
    def _resolution(self, axis: str) -> str:
        return (f"flow-local {axis}-axis inference on LEXICAL_AST -> DataFrame column "
                f"({self.resolver}, markers={self.marker_set}@pandas-{self.pins.pandas_version})")

    def iter_sites(self, tree: EnrichedTree) -> Iterable[Site]:
        root = tree.root if isinstance(tree.root, ast.Module) else None
        if root is None:
            try:
                root = ast.parse(tree.text)
            except SyntaxError:
                return   # parse failure -> no sites; the runner counts the file (PRD Sec.4)
        an = analyze_tree(root, tree.text, tree.source, resolver=self.resolver,
                          marker_set=self.marker_set, constructors=self._constructors,
                          sets=self._sets)
        self.last_analysis = an
        for flow in an.flows:
            for src in flow.srcs:
                yield Site(
                    source=tree.source,
                    locus=f"L{flow.line}",
                    evidence=flow.src_text or f"{src.base}[{src.col!r}] -> {flow.dst.base}[{flow.dst.col!r}]",
                    payload={"src": src, "dst": flow.dst, "flow": flow})

    def emit(self, site: Site, tree: EnrichedTree, *, marker_head: str) -> list:
        src: ColumnRef = site.payload["src"]
        dst: ColumnRef = site.payload["dst"]
        flow: FlowSite = site.payload["flow"]
        kind, renamed = _edge_kind(flow, src)

        src_ref = f"field:{tree.source}#{src.base}#{src.col}"
        dst_ref = f"field:{tree.source}#{dst.base}#{dst.col}"

        props = {
            "srcField": f"{src.base}.{src.col}",
            "dstField": dst.col,
            "kind": kind,
            "rename": renamed,
            "condition": flow.condition or None,
            "via": f"mapping {tree.source}:{flow.line}",
            "resolution": self._resolution(src.axis),
        }
        # Machine-checkable criterion 2: the seven keys, exactly. A hard raise, NOT an `assert` --
        # `python -O` strips asserts, and a control a flag can disable is not a control.
        if set(props) != set(PROPS_KEYS):
            raise ValueError(f"props key drift: got {sorted(props)}, require {sorted(PROPS_KEYS)} "
                             f"-- the two substrates are ONE SCHEMA (PRD Sec.4)")
        self.edge_records.append({"src": src_ref, "dst": dst_ref, "props": json.dumps(props, sort_keys=True)})

        prov = Provenance(source=site.source, locus=site.locus, recognizer=self.concept,
                          evidence=site.evidence)
        return [emit_cse(
            verb=Transformation.CREATE.value,
            subject=EntityRef(Entity.FIELD.value, src_ref),
            edges=[RelationshipDelta(Relationship.FLOWS_TO.value,
                                     EntityRef(Entity.FIELD.value, dst_ref),
                                     kind=kind, condition=flow.condition or "")],
            provenance=prov, confidence=1.0, marker_head=marker_head,
            producer_kind=self.producer_kind, compiler_id=self.compiler_id,
            artifact_class=self.artifact_class,
        )]


# ---------------------------------------------------------------------------
# COVERAGE RENDERING -- criterion 1 enforced by construction. This function RAISES rather than render
# a figure without its pins. "the recognizer resolves N% of columns" is FORBIDDEN: it is not true or
# false, it is underspecified, and it is underspecified in a way that lets any number be defended.
# ---------------------------------------------------------------------------
def format_coverage(totals: dict, pins: Pins) -> str:
    if not isinstance(pins, Pins):
        raise ValueError("REFUSED: a coverage figure without BOTH pins (resolver + marker set) is "
                         "UNDERSPECIFIED -- criterion 1. Pass a Pins.")
    att = totals["attempted"]
    res = totals["resolved"]
    unattempt = totals["unattemptable"]
    unres = totals["unresolved"]
    pct = (100.0 * res / att) if att else 0.0
    ax = totals.get("by_axis", {})
    return (
        f"PIN: {pins.line()}\n"
        f"  DENOMINATOR (attemptable, name-based string-literal Subscript NODES): {att}\n"
        f"  resolved as DataFrame column : {res}  ({pct:.1f}% of {att})\n"
        f"    by axis: binding={ax.get('binding', 0)} usage={ax.get('usage', 0)} "
        f"iterrows={ax.get('iterrows', 0)}\n"
        f"  unresolved (attempted, no axis proved it): {unres}\n"
        f"  UNATTEMPTABLE by construction (<expr> bases): {unattempt}"
        f"   <- NOT scored as misses (criterion 3)\n"
        f"  total string-literal subscripts = {att + unattempt}\n"
        f"  GRAIN: AST Subscript NODES, never lines. A comp-find count is LINES and is not a "
        f"denominator here."
    )


# ---------------------------------------------------------------------------
# CORPUS RUNNER -- sweeps a corpus, prints the coverage report WITH ITS PINS, optionally writes the
# {src,dst,props} edge artifact. Tree construction follows the batch-2 inline `ast.parse` pattern the
# sibling `comp_recognizers_code.py` already uses in this address; no new FrontEnd class is added, so
# `PyFieldRecognizer` remains the ONLY new component (PRD Sec.3).
#
# PARSE FAILURES ARE COUNTED, NEVER SILENTLY SKIPPED (PRD Sec.4). A retrieval that fails returns a
# VALUE, and a file that never parsed is indistinguishable from a file with no columns unless the
# skip is counted next to the figure.
# ---------------------------------------------------------------------------
def _iter_py(roots):
    for r in roots:
        if os.path.isfile(r) and r.endswith(".py"):
            yield r
            continue
        for dirpath, _dirs, files in os.walk(r):
            if "__pycache__" in dirpath:
                continue
            for f in sorted(files):
                if f.endswith(".py"):
                    yield os.path.join(dirpath, f)


def run_corpus(roots, *, resolver=RESOLVER_V2, marker_set="STRICT_DERIVED", unswept=(),
               marker_head="pyfield-run", out=None):
    rec = PyFieldRecognizer(pins=build_pins(resolver=resolver, marker_set=marker_set,
                                            trees_swept=tuple(roots), trees_unswept=tuple(unswept)))
    totals = {"attempted": 0, "resolved": 0, "unattemptable": 0, "unresolved": 0,
              "by_axis": {"binding": 0, "usage": 0, "iterrows": 0}}
    files = parse_failures = 0
    all_cses = []
    unresolved_examples, unattemptable_examples = [], []
    for path in _iter_py(roots):
        files += 1
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            root = ast.parse(text)
        except (OSError, SyntaxError):
            parse_failures += 1          # COUNTED, never a silent drop
            continue
        rel = os.path.relpath(path, ".").replace(os.sep, "/")
        tree = EnrichedTree(source=rel, capability=FrontEndCapability.LEXICAL_AST,
                            text=text, root=root)
        cses, _cov = rec.recognize(tree, marker_head=marker_head)
        all_cses.extend(cses)
        an = rec.last_analysis
        totals["attempted"] += an.attempted
        totals["resolved"] += an.resolved_cols
        totals["unattemptable"] += len(an.unattemptable)
        totals["unresolved"] += len(an.unresolved)
        for k in totals["by_axis"]:
            totals["by_axis"][k] += an.by_axis.get(k, 0)
        for loc, reason in an.unattemptable[:2]:
            unattemptable_examples.append(f"{rel}:{loc} {reason}")
        for loc, reason in an.unresolved[:1]:
            unresolved_examples.append(f"{rel}:{loc} {reason}")

    print(format_coverage(totals, rec.pins))
    print(f"  files scanned: {files}   PARSE FAILURES (counted, not dropped): {parse_failures}")
    print(f"  FLOWS_TO edges emitted: {len(rec.edge_records)}   CSEs: {len(all_cses)}")
    print("\n  UNRESOLVED sample (the honest-degrade channel -- zero here would be a FAILURE):")
    for line in unresolved_examples[:5]:
        print(f"    {line}")
    print("  UNATTEMPTABLE sample (<expr> bases, never scored as misses):")
    for line in unattemptable_examples[:5]:
        print(f"    {line}")
    if out:
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(rec.edge_records, fh, indent=1)
        print(f"\n  wrote {len(rec.edge_records)} edge records -> {out}")
    return rec, totals


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="PyFieldRecognizer corpus run (NFRA_PYFIELD.TO-1)")
    ap.add_argument("roots", nargs="*", help="corpus dirs -- NEVER defaulted to the estate")
    ap.add_argument("--resolver", choices=(RESOLVER_V1, RESOLVER_V2), default=RESOLVER_V2)
    ap.add_argument("--marker-set", choices=("MINIMAL", "STRICT_DERIVED", "WIDE"),
                    default="STRICT_DERIVED")
    ap.add_argument("--unswept", nargs="*", default=(), help="trees NOT swept -- declared with the figure")
    ap.add_argument("--out", default=None, help="write the {src,dst,props} edge artifact here")
    a = ap.parse_args()
    if not a.roots:
        ap.error("no corpus given -- this runner never defaults to the estate")
    run_corpus(a.roots, resolver=a.resolver, marker_set=a.marker_set, unswept=a.unswept, out=a.out)
