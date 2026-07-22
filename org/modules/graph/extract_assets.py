"""extract_assets -- monolith (opal-data-assets) silver-artifact graph pass.

Bundle item 5 (CTO 20260722T210151Z item (5), class-widened per census G2 approval
@e7952ccba): comp-blast returned NOT-FOUND on monolith silver artifacts because no
extraction pass minted them. The monolith's consumer reads are DYNAMIC-KEY
(``silver_table(s3, "fact_x", date)``), so the hardcoded-path extractors never see
them -- and a NOT-FOUND was being read as no-blast on exactly the surface
MDPF_3FIRMS lives on (DS 3F-S4 @4d58357d5 SS5).

GRAIN RULING (deliberate, not accidental): silver table nodes are NAME-grain
(``s3:assets-silver/fact_x``), not path-grain. DS's 3F-S4 contract binds a consumer
to a table by NAME + empirically verified schema at a vintage -- scope and date ride
dynamic key construction and are not stable node identity. Blast semantics at name
grain: "what breaks if fact_x changes" = every consumer naming it + every producer
emitting it. Where one name exists under several {source}/{scope} paths, the node
deliberately aggregates them; the blast answer is the UNION (lower-bound-safe: a
consumer of any path instance is included).

EDGES ARE DERIVED LIVE AT EVERY BUILD from source string literals -- never a frozen
seed list. A seeded edge list is the stale-danger-map class (census G1): an
authoritative answer on silently-aged input. DS's S4 column map validated this
derivation; it does not feed it.

Extraction is AST string-constant based (not raw-text regex over source): the
constructed-identifier lesson (comp-grep blindness, retracted "28 roles" finding)
cuts both ways -- comments and identifiers are NOT evidence a table exists, but a
string literal carrying ``fact_x`` in producer or consumer code is a real coupling.

KNOWN LOWER-BOUND (stated, not silent): schwab table names are CONSTRUCTED at
runtime (``silver_registry._fact_table``: "fact_" + feed.lower() + optional _s{N}),
so producer-side attribution for schwab rides docstring/test literals in the
vendored lambda dir. A converter whose table name appears in NO string literal
anywhere is invisible to this pass -- the blast output's existing lower-bound NOTE
covers the class.
"""
from __future__ import annotations

import ast
import re
from pathlib import Path

# A fact_ token inside a string constant. Lowercase snake only -- the house naming
# law (silver_registry.py:59-80, Andrew-direct dictionary v0.4).
_FACT_TOKEN = re.compile(r"\bfact_[a-z0-9_]+\b")

# String literals that carry the fact_ prefix but are NOT silver tables.
# fact_rows: the conversion-manifest per-projection parity FIELD
#            (conversion_manifest.py SS7e "rows == fact_rows"), a counter name.
_NOT_TABLES = {"fact_rows"}

# Where producers live: one vendored dir per silver converter lambda. The dir name
# IS the lambda name -- deployed attribution, no filename-matching inference.
_LAMBDA_ROOT = Path("infra") / "aws" / "lambda" / "opal-assets"

# Where consumers live: the monolith's own gold tree + the mdpf gold/feeder trees
# (DS 3F-S4 SS3 maps consumers in both; mdpf gold nodes already exist in the graph
# from build_mdpf_dag, so edges attach rather than duplicate).
_CONSUMER_DIRS = (
    Path("data") / "assets" / "scripts" / "gold",
    Path("data") / "mdpf" / "scripts" / "gold",
    Path("data") / "mdpf" / "scripts" / "feeders",
)

_SILVER_NODE_PREFIX = "s3:assets-silver/"


def _accept_from_string(s: str) -> set:
    """Tokens accepted from ONE string constant, by USAGE FORM -- not bare mention.

    The first cut accepted any fact_* token in any string and minted phantoms of
    the FALSE-PRESENCE class (worse than absence): a dict key ("fact_writer"), a
    docstring prose mention (fact_table), and -- the sharpest instance -- tables a
    docstring explicitly said were NEVER DECLARED (etf_schemas.py:17 fact_quotes/
    fact_funds: a negative mention minted a positive node). Accepted forms, each
    pinned to a live consumer/producer spelling in the estate:

      A PATH   .../fact_x or silver/fact_x or fact_x/...   (mdpf f-string reads,
               full-path literals, key grammars)
      C ENUM   "fact_a, fact_b, fact_c" -- a comma list that is ONLY fact names
               (silver_registry docstring enumeration of constructed names)
      D ARROW  "-> fact_x" / "-> silver/fact_x" (converter-header pipeline
               notation declaring outputs)

    Form B (exact-string arg to a silver_table(...) call) needs the CALL node and
    lives in _fact_names_in_strings' Call walk, not here.
    """
    out: set = set()
    toks = [t for t in _FACT_TOKEN.findall(s)
            if not t.endswith("_") and t not in _NOT_TABLES]
    if not toks:
        return out
    # C ENUM: a comma list that is ONLY fact names -- the whole string, or a
    # parenthesized group inside it ("... RULED (fact_acc, fact_rps, fact_trn...)"
    # in silver_registry's docstring: the only textual trace CONSTRUCTED names
    # leave, which is precisely the class raw search loses).
    candidates = [s] + [m.group(1) for m in re.finditer(r"\(([^)]*)\)", s)]
    for cand in candidates:
        parts = [p.strip().rstrip(".") for p in cand.split(",")]
        if len(parts) >= 2 and all(_FACT_TOKEN.fullmatch(p) for p in parts):
            out |= {p for p in parts
                    if not p.endswith("_") and p not in _NOT_TABLES}
    for tok in set(toks):
        for m in re.finditer(re.escape(tok), s):
            before = s[:m.start()]
            after = s[m.end():m.end() + 1]
            if before.endswith("/") or after == "/":            # A PATH
                out.add(tok)
                break
            if re.search(r"->\s*(silver/)?$", before):           # D ARROW
                out.add(tok)
                break
    return out


def _fact_names_in_strings(py_file: Path) -> set:
    """Every fact_* SILVER TABLE NAME evidenced in a python file's strings.

    AST-based: comments and bare identifiers (variables named fact_...) are
    excluded by construction, and string constants are accepted only in the
    usage forms _accept_from_string documents (+ form B here: the exact-token
    argument of a silver_table(...) call, the assets-gold consumer spelling).
    A trailing underscore is a CONCATENATION FRAGMENT ('"fact_model_" + kind'),
    excluded whole -- found live when build_dim_model_portfolio's prefix
    literal minted a phantom s3:assets-silver/fact_model_ node.
    Unparseable file -> empty set (a broken file is the commit gate's problem;
    this pass must never take the graph build down with it).
    """
    try:
        tree = ast.parse(py_file.read_text(encoding="utf-8", errors="replace"))
    except (SyntaxError, OSError):
        return set()
    names: set = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            names |= _accept_from_string(node.value)
        elif isinstance(node, ast.Call):                         # B CALL-ARG
            fn = node.func
            fn_name = fn.attr if isinstance(fn, ast.Attribute) else \
                getattr(fn, "id", "")
            if fn_name == "silver_table":
                for arg in list(node.args) + [k.value for k in node.keywords]:
                    if (isinstance(arg, ast.Constant)
                            and isinstance(arg.value, str)
                            and _FACT_TOKEN.fullmatch(arg.value)
                            and not arg.value.endswith("_")
                            and arg.value not in _NOT_TABLES):
                        names.add(arg.value)
    return names


def _scan_dir(root: Path) -> dict:
    """{py_file: fact-name set} for every top-level *.py under root (non-recursive
    for consumer dirs by convention -- tests/ and lib subdirs are not consumers)."""
    out = {}
    if not root.is_dir():
        return out
    for py in sorted(root.glob("*.py")):
        if py.name.startswith("__"):
            continue
        names = _fact_names_in_strings(py)
        if names:
            out[py] = names
    return out


def _scan_lambda_dirs(ws: Path) -> dict:
    """{lambda_name: fact-name set} over the vendored opal-assets silver converters."""
    out = {}
    root = ws / _LAMBDA_ROOT
    if not root.is_dir():
        return out
    for d in sorted(root.glob("opal-assets-silver-*")):
        if not d.is_dir():
            continue
        names: set = set()
        for py in sorted(d.glob("*.py")):
            names |= _fact_names_in_strings(py)
        if names:
            out[d.name] = names
    return out


def inject_assets_silver_artifacts(g, workspace_root: Path) -> int:
    """Mint NAME-grain monolith silver table nodes + producer/consumer edges.

    Returns edges added. Node/edge idiom mirrors inject_pipeline_edges exactly
    (S3_ARTIFACT nodes, READS_S3/WRITES_S3 verbs) so every downstream consumer of
    the graph (blast formatting, kuzu projection, debtscan reachability) sees a
    familiar shape rather than a new vocabulary.
    """
    from .trace_graph import Node, Edge

    producers = _scan_lambda_dirs(workspace_root)          # lambda -> names
    consumers = {}                                         # gold stem -> (names, file)
    for cdir in _CONSUMER_DIRS:
        for py, names in _scan_dir(workspace_root / cdir).items():
            consumers[py.stem] = (names, py)

    # A node is minted only for a name seen on the PRODUCER side or read by a
    # CONSUMER -- the union is the live coupling surface. (Producer-only = a table
    # nothing reads yet; consumer-only = a read of a table this pass cannot
    # attribute -- both are real, both belong in blast.)
    all_names: set = set()
    for names in producers.values():
        all_names |= names
    for names, _ in consumers.values():
        all_names |= names

    edges_added = 0
    existing_edges = {(e.source, e.target, e.edge_type) for e in g.edges}

    def _add_edge(src: str, tgt: str, verb: str) -> None:
        nonlocal edges_added
        if (src, tgt, verb) in existing_edges:
            return
        g.add_edge(Edge(source=src, target=tgt, edge_type=verb,
                        metadata={"source": "assets_silver_literals",
                                  "derivation": "live-per-build"}))
        existing_edges.add((src, tgt, verb))
        edges_added += 1

    for name in sorted(all_names):
        node_id = _SILVER_NODE_PREFIX + name
        if node_id not in g.nodes:
            g.add_node(Node(
                id=node_id, node_type="S3_ARTIFACT",
                label=("assets-silver/" + name
                       + " (name-grain: every {source}/{scope}/silver/" + name
                       + " partition)"),
            ))

    for lambda_name, names in producers.items():
        lam_id = "lambda:" + lambda_name
        if lam_id not in g.nodes:
            g.add_node(Node(id=lam_id, node_type="LAMBDA", label=lambda_name))
        for name in sorted(names):
            _add_edge(lam_id, _SILVER_NODE_PREFIX + name, "WRITES_S3")

    for stem, (names, py) in consumers.items():
        script_id = "gold:" + stem
        if script_id not in g.nodes:
            g.add_node(Node(
                id=script_id, node_type="GOLD_SCRIPT", label=stem,
                file_path=str(py.relative_to(workspace_root)).replace("\\", "/"),
            ))
        for name in sorted(names):
            _add_edge(_SILVER_NODE_PREFIX + name, script_id, "READS_S3")

    return edges_added
