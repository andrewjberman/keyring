#!/usr/bin/env python3
"""
comp_toolgraph.py -- NFRA_TOOLGRAPH.TO-1 backend: the comp-tool suite as a quality-annotated graph.

The comp-tools are NODES in the same estate ontology at the DEPTH grain "scanner" -- the brain's
own sensory organs as nodes the brain can reason about. This computes that graph MECHANICALLY:

  C0  the node set        -- the ratified AC-0 is-a-tool universe (63), enriched per node with
                             on-disk / registration / description-source / domain / archetype /
                             susceptible_to[] (archetype/susceptible carry a CLASS + provenance;
                             OBSERVED only where a prior pass exercised it, else INFERRED).
  C1  the edges           -- SHARES_SUBSTRATE (mechanical imports/backend-file overlap across all
                             backends), WRITES (tool -> the marker/manifest/cache/log it mutates),
                             INVOKED_BY (tool -> its gate/hook/CI wiring, or UNWIRED).
  DIFF the load-bearing   -- diff the DECLARED coupling (comp-coverage-map.yaml `distinct_from`
       coupling diff        overlap groups) against the ACTUAL substrate graph. An ACTUAL shared
                             backend that is NOT declared is the finding -- the hidden ripple the
                             map exists to catch. `coupling_diff()` is a PURE function so AC1 can
                             prove it goes RED on a SEEDED undeclared edge (test, not the live tree).
  DENOM  AC-0 reconcile   -- the five unreconciled tool counts folded to ONE printed number with
                             its derivation (NFRA_TOOLCHECK AC-0, folded per LEAD).

MEASURE-ONLY / READ-ONLY on the estate. Computes + reads; edits no enforcer, mutates no served
artifact. The only write is the committed census JSON (`census --write`), a version-controlled
rendering (LEAD-1: a committed path with a vintage, never a gitignored scratchpad citation).

Sovereign boundary: comp-blast's cache carries bd-backed nodes -- this reads node NAMES + edges
only, never the bd data.

Usage:
    comp-toolgraph census [--write] [--json]      # C0 node table (+ write the committed artifact)
    comp-toolgraph edges [--json]                 # C1 edges: SHARES_SUBSTRATE / WRITES / INVOKED_BY
    comp-toolgraph coupling-diff [--json]         # declared-vs-actual; the undeclared-ripple finding
    comp-toolgraph denominator                    # the ONE reconciled tool count + derivation
    comp-toolgraph all [--json]                   # every section
    comp-toolgraph --self-test [--json]           # AC1 go-red proof (seeded undeclared edge) + AC6

Author: 0.8.0_AE_CloudComp (NFRA_TOOLGRAPH.TO-1). 2026-07-10.
Spec: docs/architecture/NFRA_TOOLGRAPH_PRD.md (sec.3 C0/C1/C2, sec.5 AC1/AC6, LEAD-1);
      TO org/projects/NFRA_TOOLGRAPH/task_orders/NFRA_TOOLGRAPH.TO-1.*.md @ 8dfcf1e75.
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.normpath(os.path.join(_HERE, "..", "..", ".."))
TOOLDIR = os.path.join(WS, ".tools")
GRAPHDIR = os.path.join(WS, "org", "modules", "graph")
AC0_PREDICATE = os.path.join(
    WS, "org", "tier1_exec", "3.0.0_SA_CVO", "deliverables",
    "AC-0_tool_universe_predicate_20260710.json")
COVERAGE_MAP = os.path.join(GRAPHDIR, "comp-coverage-map.yaml")
CENSUS_OUT = os.path.join(GRAPHDIR, "comp_toolgraph_census.json")

# The logging shim every bash wrapper calls as a SEPARATE process (`python comp_log_auto.py ...`).
# It is a WRITES edge (tool -> rail log), NOT a SHARES_SUBSTRATE import edge, and it is near-universal.
# Excluded from substrate edges so a universal logging call does not swamp the ripple map; the
# exclusion is DISCLOSED (never silent) in the edges output.
_LOG_SHIM = "comp_log_auto"


# ============================================================================================
# C0 -- the node set (the ratified AC-0 is-a-tool universe, enriched).
# ============================================================================================
def load_universe():
    """The 63 IN nodes from the ratified AC-0 predicate (the authoritative is-a-tool universe).

    Grounds the node set on the committed, CVO-ratified artifact rather than re-deriving it, so
    the denominator cannot drift from the ruling. Returns (names, predicate_dict)."""
    with open(AC0_PREDICATE, "r", encoding="utf-8", errors="replace") as fh:
        pred = json.load(fh)
    names = sorted(r["name"] for r in pred.get("rows", []) if r.get("decision") == "IN")
    return names, pred


# archetype / susceptible_to per node -- fed from PASSCRAFT + prior hand-passes, each carrying a
# CLASS (OBSERVED = a prior pass EXERCISED it; INFERRED = believed/cited but not exercised here)
# and a SOURCE. This is EVIDENCE ANNOTATION, never a pass/fail verdict (TOOLGRAPH computes no
# verdict). A tool absent from this map carries archetype=None -- an honest "not yet passed", never
# a guess. The 12 archetype vocabulary is NFRA_PASSCRAFT sec.3b.
_ARCHETYPE_ANNOTATIONS = {
    "comp-adapter-audit": {"archetype": "mislabelled-control-flow",
        "susceptible_to": ["mislabelled-control-flow", "guard-asymmetry", "test-writes-prod"],
        "class": "OBSERVED", "source": "NFRA_TOOLPASS sec.4 (tool-1, closed 319d1df66): printed "
        "'S3 fetch failed' when S3 was never attempted; D9 manifest-write is load-bearing for the gate"},
    "comp-surface-check": {"archetype": "correct-but-unwired",
        "susceptible_to": ["correct-but-unwired"],
        "class": "OBSERVED", "source": "NFRA_TOOLGRAPH_PRD sec.2 + COMPASSURANCE sec.2: rc=2/CRITICAL "
        "on 3/3 SEV1, invoked by NO gate (safe-commit parent-scoped, portal CI 0/3)"},
    "comp-freshness": {"archetype": "aging-oracle",
        "susceptible_to": ["aging-oracle", "resource-blind", "undiscriminating/constant-gate"],
        "class": "INFERRED", "source": "NFRA_TOOLGRAPH_PRD sec.2 + COMPASSURANCE sec.4b-i: BELIEVED "
        "anti-correlated (reads mtime not the partition date-key) -- not exercised by this TO"},
    "comp-iam": {"archetype": "resource-blind",
        "susceptible_to": ["resource-blind"],
        "class": "INFERRED", "source": "CLAUDE.md 22a: grants() models (action) not (action,resource); "
        "_iam_resource_matches is CVO-certified scoped (6f3751a34) -- mixed, not exercised here"},
    "comp-which": {"archetype": "undiscriminating/constant-gate",
        "susceptible_to": ["undiscriminating/constant-gate", "aging-oracle"],
        "class": "INFERRED", "source": "comp_route.py:362 vetted-offset short-circuit citation "
        "(RV-0046 F-012) -- CONTRADICTED by a live probe (zzqq -> comp-grep FALLBACK, not CONFIDENT); "
        "citation-vs-code declarative drift, INFERRED per CTO~A 193238Z, do NOT re-verify / chase live"},
    "comp-glob": {"archetype": "terminal-honest/artifact-lies",
        "susceptible_to": ["terminal-honest/artifact-lies"],
        "class": "OBSERVED", "source": "COMPASSURANCE_matrix_data: R7 fail -- NO-MATCH hint claimed "
        "16 gitignored, 0 are (331849e80)"},
    "comp-manifest-check": {"archetype": "undiscriminating/constant-gate",
        "susceptible_to": ["undiscriminating/constant-gate"],
        "class": "INFERRED", "source": "NFRA_COMPASSURANCE_PRD sec.7 TO-7: BELIEVED undiscriminating "
        "(its denominator IS the catalog) -- not exercised here"},
    "comp-coverage-check": {"archetype": "vacuous-that-can-block",
        "susceptible_to": ["vacuous-that-can-block"],
        "class": "INFERRED", "source": "NFRA_COMPASSURANCE_PRD sec.7 TO-7: seeded VACUOUS and in "
        "safe-commit's blocking chain -- not exercised here"},
}


def _read_text(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return None


def resolve_backends(tool):
    """The set of backend .py files a tool's wrapper directly runs, ABSOLUTE paths.

    Bash wrapper: every `python "$WORKSPACE/<relpath>.py"` / `python3 ... .py` exec target, minus
    the logging shim. Python wrapper: the wrapper file itself IS the backend. Returns (backends,
    resolved_ok): resolved_ok=False when a wrapper names no runnable backend (DISCLOSED, never
    silently dropped)."""
    path = os.path.join(TOOLDIR, tool)
    txt = _read_text(path)
    if txt is None:
        return [], False
    lines = txt.splitlines()
    backends = []
    # A backend .py named on any exec/python line. Wrappers vary widely in HOW they name it:
    #   python "$WORKSPACE/org/modules/graph/x_cli.py"
    #   exec "${COMP_PYTHON:-python}" "${WORKSPACE_ROOT}/org/modules/graph/x.py"
    #   exec python "$_ws/infra/aws/globgrph/x.py"
    # so match every quoted-or-bare *.py token on an exec/python line, strip any leading shell-var
    # path prefix ($VAR/ | ${VAR}/ | ${VAR:-default}/), and resolve the remainder WS-relative.
    for line in lines:
        s = line.strip()
        if s.startswith("#") or ("exec" not in s and "python" not in s):
            continue
        for m in re.finditer(r'"([^"]*\.py)"|(\S*\.py)\b', line):
            tok = m.group(1) or m.group(2)
            if not tok:
                continue
            rel = re.sub(r'^\$\{?[A-Za-z_][A-Za-z0-9_]*(?::-[^}]*)?\}?/', "", tok)
            if os.path.basename(rel).startswith(_LOG_SHIM):
                continue
            cand = rel if os.path.isabs(rel) else os.path.normpath(os.path.join(WS, rel))
            if os.path.isfile(cand):
                backends.append(cand)
    # de-dup, keep order
    seen, out = set(), []
    for b in backends:
        if b not in seen:
            seen.add(b)
            out.append(b)
    if out:
        return out, "wrapped"                 # a wrapper over a separate .py backend
    return [path], "self"                     # a self-contained tool (bash/python leaf IS its backend)


def _local_module_index():
    """basename(without .py) -> abspath for every .py under org/modules/graph and .tools, so an
    `import X` can be resolved to a LOCAL module (a shared-substrate signal) vs a stdlib/3rd-party."""
    idx = {}
    for d in (GRAPHDIR, TOOLDIR):
        try:
            for fn in os.listdir(d):
                if fn.endswith(".py"):
                    idx.setdefault(fn[:-3], os.path.join(d, fn))
        except OSError:
            continue
    return idx


def parse_local_imports(pyfile, local_idx):
    """The LOCAL modules a backend imports (basenames present in local_idx), via ast when parseable,
    else a regex fallback. Only local modules count as shared substrate (a shared stdlib import is
    not a coupling)."""
    txt = _read_text(pyfile)
    if txt is None:
        return set()
    mods = set()
    try:
        tree = ast.parse(txt)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for a in node.names:
                    mods.add(a.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module and node.level == 0:
                    mods.add(node.module.split(".")[0])
    except SyntaxError:
        for m in re.finditer(r'^\s*(?:import|from)\s+([a-zA-Z_][\w]*)', txt, re.M):
            mods.add(m.group(1))
    return {m for m in mods if m in local_idx and m != _LOG_SHIM}


def tool_substrate(tool, local_idx):
    """A tool's substrate footprint = {its backend files} U {local modules those backends import}.
    Two tools with a non-empty intersection SHARE_SUBSTRATE. Returns (footprint_set, backend_kind).

    A self-contained tool's footprint is its own file, so it shares substrate with another tool only
    if that tool sources/imports it -- correct: a bash leaf couples with nothing by construction."""
    backends, kind = resolve_backends(tool)
    foot = set()
    for b in backends:
        foot.add(os.path.relpath(b, WS).replace("\\", "/"))
        for mod in parse_local_imports(b, local_idx):
            foot.add(mod)
    return foot, kind


def node_registration(name, pred):
    """registration = INDEXED (in tools_index/catalogued) / CONVENTION (comp-* uncatalogued) from
    the AC-0 predicate row's clause: C1=catalogued, C2=comp-* convention-only."""
    for r in pred.get("rows", []):
        if r.get("name") == name:
            clause = r.get("clause", "")
            srcs = r.get("sources", [])
            if "tools_index" in srcs:
                return "INDEXED"
            if clause == "C1":
                return "CATALOGUED"    # in comp-tools.yaml/manifest but not tools_index
            if clause == "C2":
                return "CONVENTION"    # comp-* convention, uncatalogued
            return clause or "?"
    return "?"


def build_nodes():
    """C0: the enriched node table."""
    names, pred = load_universe()
    local_idx = _local_module_index()
    nodes = []
    for name in names:
        on_disk = os.path.isfile(os.path.join(TOOLDIR, name))
        foot, kind = tool_substrate(name, local_idx)
        ann = _ARCHETYPE_ANNOTATIONS.get(name, {})
        nodes.append({
            "tool": name,
            "on_disk": on_disk,
            "registration": node_registration(name, pred),
            "backend_kind": kind,
            "domain": _domain_of(name),
            "archetype": ann.get("archetype"),
            "archetype_class": ann.get("class"),
            "susceptible_to": ann.get("susceptible_to", []),
            "archetype_source": ann.get("source"),
            "substrate": sorted(foot),
        })
    return nodes, pred


# domain from the coverage-map surface where declared, else a light heuristic on the backend path.
_DOMAIN_SURFACE = None


def _domain_of(name):
    global _DOMAIN_SURFACE
    if _DOMAIN_SURFACE is None:
        _DOMAIN_SURFACE = {}
        for entry in _coverage_tool_entries():
            if entry.get("tool") and entry.get("surface"):
                _DOMAIN_SURFACE[entry["tool"]] = entry["surface"]
    return _DOMAIN_SURFACE.get(name)


# ============================================================================================
# C1 -- the edges.
# ============================================================================================
def shares_substrate_edges(nodes):
    """SHARES_SUBSTRATE: unordered tool pairs whose substrate footprints intersect, labelled with
    the shared substrate elements. Deterministic (sorted)."""
    foot = {n["tool"]: set(n["substrate"]) for n in nodes}
    tools = sorted(foot)
    edges = []
    for i in range(len(tools)):
        for j in range(i + 1, len(tools)):
            a, b = tools[i], tools[j]
            shared = foot[a] & foot[b]
            if shared:
                edges.append({"a": a, "b": b, "shared": sorted(shared)})
    return edges


_WRITE_PATTERNS = [
    (r"open\([^)]*['\"][wa]\+?['\"]", "file-write"),
    (r"\.write\(", "file-write"),
    (r"json\.dump\(", "json-write"),
    (r"put_object\(|PutObject|s3\.[^(]*put", "s3-write"),
    (r"put_item\(|update_item\(|PutItem", "ddb-write"),
    (r"subprocess[^\n]*comp_log_auto", "rail-log"),
]


def writes_edges(nodes):
    """WRITES: the marker/manifest/cache/log surfaces a tool mutates, from a grep of its wrapper +
    backends for write operations. Heuristic + DISCLOSED as such; feeds PASSCRAFT's write-surface
    move. rail-log (comp_log_auto via the wrapper) is captured here, where it belongs."""
    out = []
    for n in nodes:
        tool = n["tool"]
        files = [os.path.join(TOOLDIR, tool)]
        backends, _kind = resolve_backends(tool)
        files += backends
        kinds = set()
        wtxt = _read_text(os.path.join(TOOLDIR, tool)) or ""
        if _LOG_SHIM in wtxt:
            kinds.add("rail-log")
        for f in files:
            txt = _read_text(f)
            if not txt:
                continue
            for pat, kind in _WRITE_PATTERNS:
                if re.search(pat, txt):
                    kinds.add(kind)
        if kinds:
            out.append({"tool": tool, "writes": sorted(kinds)})
    return out


# where a tool is wired as a GATE / HOOK / CI step. Searched across the enforcement surfaces.
_INVOKER_SURFACES = [
    ".tools/safe-commit.sh", ".tools/commit-gate.sh", ".tools/safe-apply.sh",
    ".tools/safe-deploy.sh", ".tools/ds-precommit-check.py",
    ".git/hooks", "portal/.git/hooks", ".github/workflows", "portal/.github/workflows",
    "org/modules/graph/commit_gate_lib.sh",
]


def invoked_by_edges(nodes):
    """INVOKED_BY: for each tool, the enforcement surface(s) that invoke it, or UNWIRED. Mechanical
    grep of the invoker surfaces for the tool name. UNWIRED is the load-bearing state (a correct tool
    invoked by no gate reads as a live control)."""
    # pre-read every invoker surface file's text once
    corpus = {}
    for rel in _INVOKER_SURFACES:
        p = os.path.join(WS, rel)
        if os.path.isfile(p):
            corpus[rel] = _read_text(p) or ""
        elif os.path.isdir(p):
            for root, _dirs, fns in os.walk(p):
                for fn in fns:
                    fp = os.path.join(root, fn)
                    corpus[os.path.relpath(fp, WS).replace("\\", "/")] = _read_text(fp) or ""
    out = []
    for n in nodes:
        tool = n["tool"]
        invokers = sorted({rel for rel, txt in corpus.items()
                           if re.search(r"(?<![\w-])" + re.escape(tool) + r"(?![\w-])", txt)})
        out.append({"tool": tool, "invoked_by": invokers or ["UNWIRED"]})
    return out


# ============================================================================================
# THE COUPLING DIFF -- the load-bearing move.
# ============================================================================================
def _coverage_tool_entries():
    """The `tools:` list from comp-coverage-map.yaml. yaml if available, else a tolerant mini-parse
    of the specific block shape (a list of `- tool:` records with `surface:` + `distinct_from:`)."""
    txt = _read_text(COVERAGE_MAP)
    if txt is None:
        return []
    try:
        import yaml  # local optional dependency; falls back to the mini-parser if absent
        doc = yaml.safe_load(txt)
        if isinstance(doc, dict) and isinstance(doc.get("tools"), list):
            return [e for e in doc["tools"] if isinstance(e, dict)]
    except Exception:  # fall through to the mini-parser on any yaml/parse failure
        pass
    return _mini_parse_tools(txt)


def _mini_parse_tools(txt):
    """Tolerant fallback: pull `tool:`, `surface:`, and every `{ tool: X, shared_resource: Y }`
    distinct_from record under each entry, without a yaml dep."""
    entries = []
    cur = None
    in_tools = False
    for line in txt.splitlines():
        if re.match(r"^tools:\s*$", line):
            in_tools = True
            continue
        if in_tools and re.match(r"^[a-zA-Z_]", line):   # dedented to a new top-level key
            break
        if not in_tools:
            continue
        m = re.match(r"\s*-\s*tool:\s*(\S+)", line)
        if m:
            if cur:
                entries.append(cur)
            cur = {"tool": m.group(1), "distinct_from": []}
            continue
        if cur is None:
            continue
        ms = re.match(r"\s*surface:\s*(\S+)", line)
        if ms:
            cur["surface"] = ms.group(1)
            continue
        md = re.search(r"tool:\s*([A-Za-z0-9_-]+),\s*shared_resource:\s*([A-Za-z0-9_-]+)", line)
        if md:
            cur["distinct_from"].append({"tool": md.group(1), "shared_resource": md.group(2)})
    if cur:
        entries.append(cur)
    return entries


def declared_coupling():
    """The DECLARED coupling: unordered tool pairs the coverage-map declares as overlapping (via a
    `distinct_from` record naming a sibling + shared_resource). Returns {frozenset({a,b}): [resources]}."""
    pairs = {}
    for entry in _coverage_tool_entries():
        a = entry.get("tool")
        for rec in entry.get("distinct_from", []) or []:
            b = rec.get("tool")
            res = rec.get("shared_resource")
            if a and b:
                key = frozenset({a, b})
                pairs.setdefault(key, set())
                if res:
                    pairs[key].add(res)
    return {k: sorted(v) for k, v in pairs.items()}


def coupling_diff(actual_edges, declared_pairs):
    """PURE. Given ACTUAL substrate edges [{a,b,shared}] and DECLARED coupling {frozenset:[res]},
    return the ACTUAL edges whose pair is NOT in the declared set -- the UNDECLARED shared-backend
    findings (the hidden ripples). Pure + total so AC1 can seed a known undeclared edge and prove
    the diff flags it (go-red), and seed a declared edge and prove it does NOT (the negative control)."""
    undeclared = []
    for e in actual_edges:
        key = frozenset({e["a"], e["b"]})
        if key not in declared_pairs:
            undeclared.append(e)
    return undeclared


def run_coupling_diff(nodes=None):
    """Run the diff on the REAL data: every ACTUAL substrate edge, partitioned into DECLARED-covered
    vs UNDECLARED. Also reports declared pairs with NO actual substrate edge (declared-but-no-code-
    coupling -- the map declaring a semantic overlap that is not a code ripple; informational)."""
    if nodes is None:
        nodes, _ = build_nodes()
    actual = shares_substrate_edges(nodes)
    declared = declared_coupling()
    undeclared = coupling_diff(actual, declared)
    covered = [e for e in actual if frozenset({e["a"], e["b"]}) in declared]
    actual_pairs = {frozenset({e["a"], e["b"]}) for e in actual}
    declared_no_code = sorted(
        ("+".join(sorted(k)) for k in declared if k not in actual_pairs))
    return {
        "actual_substrate_edges": len(actual),
        "declared_overlap_pairs": len(declared),
        "covered": covered,
        "undeclared": undeclared,
        "declared_without_code_coupling": declared_no_code,
    }


# ============================================================================================
# AC-0 DENOMINATOR RECONCILIATION -- one number, its derivation.
# ============================================================================================
def reconcile_denominator():
    """Fold the unreconciled tool counts to ONE number with its derivation. The ONE number is the
    ratified AC-0 is-a-tool universe (63); every other figure is a DIFFERENT question, stated with
    what it counts, so no figure is left as 'a number without its rule' (CLAUDE.md Git-section)."""
    names, pred = load_universe()
    disk_all = sorted(os.path.basename(p) for p in
                      _glob(os.path.join(TOOLDIR, "comp-*")) if os.path.isfile(p))
    disk_on = [n for n in names if os.path.isfile(os.path.join(TOOLDIR, n))]
    indexed = [n for n in names if node_registration(n, pred) == "INDEXED"]
    convention = [n for n in names if node_registration(n, pred) == "CONVENTION"]
    excluded = pred.get("excluded_count")
    return {
        "THE_ONE_NUMBER": pred.get("universe_count"),
        "what_it_counts": "the ratified AC-0 is-a-tool universe (invokable AND catalogued-or-comp-* "
                          "convention); the authoritative node set of this graph",
        "source": "AC-0_tool_universe_predicate_20260710.json (CVO-ratified) universe_count",
        "derivation": [
            ("AC-0 is-a-tool universe (THE node set)", pred.get("universe_count")),
            ("  of which INDEXED (in tools_index)", len(indexed)),
            ("  of which comp-* CONVENTION (uncatalogued)", len(convention)),
            ("  of which OTHER (catalogued non-index)",
             pred.get("universe_count") - len(indexed) - len(convention)),
            (".tools/comp-* files on disk (incl. impl-twins/tests/non-tools)", len(disk_all)),
            ("  of the 63 universe, files present on disk", len(disk_on)),
            ("AC-0 EXCLUDED candidates (with a named excluding clause)", excluded),
            ("union scanned (universe + excluded)",
             (pred.get("universe_count") or 0) + (excluded or 0)),
        ],
        "prior_unreconciled_figures": {
            "67 disk": "all .tools/comp-* regular files (includes .py impl-twins, -test harnesses, "
                       "non-comp meta) -- a SHAPE count, not the is-a-tool property",
            "~42-44 tools_index": "catalogued-and-routable subset (the router does not index the "
                                  "router: comp-which/comp-grep/comp-glob absent)",
            "29 yaml / 40 matrix": "test-file / matrix-render denominators over different bases",
            "~30 / ~55 described": "CLAUDE.md prose counts, minted without a control",
        },
        "note": "These are answers to DIFFERENT questions (shape / catalogue / test-coverage / "
                "prose), not five estimates of one quantity. THE node-set denominator is 63.",
    }


def _glob(pat):
    import glob
    return glob.glob(pat)


# ============================================================================================
# Rendering + CLI
# ============================================================================================
def _census_payload():
    nodes, pred = build_nodes()
    return {
        "artifact": "NFRA_TOOLGRAPH.TO-1 comp-tool graph census (C0 nodes)",
        "author": "0.8.0_AE_CloudComp",
        "generated_by": "org/modules/graph/comp_toolgraph.py (comp-toolgraph census)",
        "universe_source": "AC-0_tool_universe_predicate_20260710.json (CVO-ratified, 63 IN)",
        "universe_count": pred.get("universe_count"),
        "note": "MEASURE-ONLY. archetype/susceptible_to carry a CLASS (OBSERVED/INFERRED) + source; "
                "None = not yet passed (honest, never a guess). A committed rendering (LEAD-1).",
        "nodes": nodes,
    }


def cmd_census(args):
    payload = _census_payload()
    if args.write:
        with open(CENSUS_OUT, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2)
        print("OK: wrote committed census -> %s (%d nodes)"
              % (os.path.relpath(CENSUS_OUT, WS).replace("\\", "/"), len(payload["nodes"])))
    if args.json:
        print(json.dumps(payload, indent=2))
        return 0
    print("=" * 100)
    print("C0 -- COMP-TOOL GRAPH NODE CENSUS  (universe=%d, ratified AC-0)" % payload["universe_count"])
    print("=" * 100)
    print("| tool | disk | registration | domain | archetype (class) | backend |")
    print("|------|------|--------------|--------|-------------------|---------|")
    for n in payload["nodes"]:
        atag = ("%s (%s)" % (n["archetype"], n["archetype_class"])) if n["archetype"] else "-"
        print("| %s | %s | %s | %s | %s | %s |" % (
            n["tool"], "yes" if n["on_disk"] else "NO", n["registration"],
            n["domain"] or "-", atag, n["backend_kind"]))
    selfc = [n["tool"] for n in payload["nodes"] if n["backend_kind"] == "self"]
    print("\n  self-contained tools (no separate .py backend -- their own file IS the backend): %d %s"
          % (len(selfc), selfc))
    tagged = [n["tool"] for n in payload["nodes"] if n["archetype"]]
    print("  archetype-tagged (from prior passes / PASSCRAFT): %d %s" % (len(tagged), tagged))
    return 0


def cmd_edges(args):
    nodes, _ = build_nodes()
    sub = shares_substrate_edges(nodes)
    wr = writes_edges(nodes)
    inv = invoked_by_edges(nodes)
    if args.json:
        print(json.dumps({"shares_substrate": sub, "writes": wr, "invoked_by": inv}, indent=2))
        return 0
    print("=" * 100)
    print("C1 -- EDGES")
    print("=" * 100)
    print("\nSHARES_SUBSTRATE (%d edges; logging shim %s excluded + disclosed):" % (len(sub), _LOG_SHIM))
    for e in sub:
        print("  %s <-> %s   [%s]" % (e["a"], e["b"], ", ".join(e["shared"])))
    print("\nWRITES (%d tools with a write surface):" % len(wr))
    for e in wr:
        print("  %-24s -> %s" % (e["tool"], ", ".join(e["writes"])))
    unwired = [e["tool"] for e in inv if e["invoked_by"] == ["UNWIRED"]]
    print("\nINVOKED_BY (TEXTUAL invocation on an enforcement surface -- NOT effective enforcement):")
    print("  a tool textually wired to a gate may still run ADVISORY/nullified (comp-surface-check is")
    print("  wired to safe-commit.sh yet cannot block -- 'correct-but-unwired' lives on the SEMANTIC")
    print("  axis, a hand-run judgment this tool does not compute). UNWIRED is the normal state for a")
    print("  query tool; it is only a smell for a tool that CLAIMS to guard.")
    print("  %d textually-wired, %d UNWIRED" % (len(inv) - len(unwired), len(unwired)))
    for e in inv:
        if e["invoked_by"] != ["UNWIRED"]:
            print("  %-24s <- %s" % (e["tool"], ", ".join(e["invoked_by"])))
    print("  UNWIRED (%d): %s" % (len(unwired), unwired))
    return 0


def cmd_coupling_diff(args):
    res = run_coupling_diff()
    if args.json:
        print(json.dumps(res, indent=2))
        return 0
    print("=" * 100)
    print("COUPLING DIFF -- declared (coverage-map) vs actual (import graph)")
    print("=" * 100)
    print("  actual substrate edges ......... %d" % res["actual_substrate_edges"])
    print("  declared overlap pairs ......... %d" % res["declared_overlap_pairs"])
    print("  actual edges COVERED by a declared overlap ... %d" % len(res["covered"]))
    print("  actual edges UNDECLARED (the hidden ripples) . %d" % len(res["undeclared"]))
    for e in res["undeclared"]:
        print("      %s <-> %s   [shares: %s]" % (e["a"], e["b"], ", ".join(e["shared"])))
    print("\n  declared overlaps with NO code coupling (semantic-only): %d" %
          len(res["declared_without_code_coupling"]))
    print("\n  NOTE: a verdict on any pair is a hand-run judgment (NFRA_TOOLPASS sec.0); this diff "
          "SURFACES undeclared code coupling, it does not adjudicate redundancy.")
    return 0


def cmd_denominator(args):
    d = reconcile_denominator()
    if args.json:
        print(json.dumps(d, indent=2))
        return 0
    print("=" * 100)
    print("AC-0 DENOMINATOR RECONCILIATION -- THE ONE NUMBER = %s" % d["THE_ONE_NUMBER"])
    print("=" * 100)
    print("  counts: %s" % d["what_it_counts"])
    print("  source: %s" % d["source"])
    print("\n  derivation:")
    for label, val in d["derivation"]:
        print("    %-52s %s" % (label, val))
    print("\n  prior unreconciled figures (each a DIFFERENT question):")
    for k, v in d["prior_unreconciled_figures"].items():
        print("    %-22s %s" % (k, v))
    print("\n  %s" % d["note"])
    return 0


def _self_test():
    """AC1 (go-red, EXERCISED) + AC6 (class-agnostic), as a PURE-function control on coupling_diff.

    AC1: seed a KNOWN undeclared edge into the ACTUAL set with a declared edge present; the diff MUST
    flag the undeclared one (go-red) AND MUST NOT flag the declared one (the negative control). A diff
    that is merely green on the live tree has not been shown able to fire; this proves it can."""
    checks = []

    def ck(name, ok, detail=""):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})
        return ok

    declared = {frozenset({"comp-aws", "comp-iam"}): ["IAM"]}
    actual = [
        {"a": "comp-aws", "b": "comp-iam", "shared": ["iam_lib"]},        # DECLARED -> must NOT flag
        {"a": "comp-seedX", "b": "comp-seedY", "shared": ["seed_backend"]},  # SEEDED undeclared -> MUST flag
    ]
    undeclared = coupling_diff(actual, declared)
    keys = {frozenset({e["a"], e["b"]}) for e in undeclared}
    ck("AC1.go_red_flags_seeded_undeclared",
       frozenset({"comp-seedX", "comp-seedY"}) in keys,
       "seeded undeclared edge appears in the diff")
    ck("AC1.negative_control_declared_not_flagged",
       frozenset({"comp-aws", "comp-iam"}) not in keys,
       "a DECLARED overlap is NOT flagged as undeclared")
    ck("AC1.impossible_value_all_declared_is_empty",
       coupling_diff([actual[0]], declared) == [],
       "a set of only-declared edges yields ZERO findings (the value the diff must produce if "
       "measuring the intended quantity -- R6 on the diff)")

    # AC6 (class-agnostic): the node/edge model admits a NON-comp scanner with no schema fork.
    foreign = {"tool": "org-recognizer-X", "on_disk": True, "registration": "CONVENTION",
               "backend_kind": "self", "domain": "org", "archetype": "resource-blind",
               "archetype_class": "INFERRED", "susceptible_to": ["resource-blind"],
               "archetype_source": "hypothetical", "substrate": ["org_recognizer_lib"]}
    foreign2 = dict(foreign, tool="org-recognizer-Y")
    fe = shares_substrate_edges([foreign, foreign2])
    ck("AC6.non_comp_node_admits_no_fork",
       len(fe) == 1 and fe[0]["shared"] == ["org_recognizer_lib"],
       "two non-comp scanners sharing a substrate produce a SHARES_SUBSTRATE edge via the same model")

    ok = all(c["pass"] for c in checks)
    return ok, checks


def cmd_self_test(args):
    ok, checks = _self_test()
    if args.json:
        print(json.dumps({"pass": ok, "checks": checks}, indent=2))
    else:
        print("=== comp-toolgraph --self-test (AC1 go-red + AC6 class-agnostic) ===")
        for c in checks:
            print("  [%s] %s%s" % ("PASS" if c["pass"] else "FAIL", c["check"],
                                   ("   (%s)" % c["detail"]) if c["detail"] else ""))
        print("\n%s" % ("OK: all checks pass" if ok else "ERROR: one or more checks FAILED"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="comp-toolgraph -- the comp-tool suite as a graph "
                                             "(NFRA_TOOLGRAPH.TO-1, measure-only)")
    sub = ap.add_subparsers(dest="cmd")
    pc = sub.add_parser("census")
    pc.add_argument("--write", action="store_true")
    pc.add_argument("--json", action="store_true")
    for name in ("edges", "coupling-diff", "denominator", "all"):
        sub.add_parser(name).add_argument("--json", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return cmd_self_test(args)
    if args.cmd == "census":
        return cmd_census(args)
    if args.cmd == "edges":
        return cmd_edges(args)
    if args.cmd == "coupling-diff":
        return cmd_coupling_diff(args)
    if args.cmd == "denominator":
        return cmd_denominator(args)
    if args.cmd == "all":
        shim = argparse.Namespace(json=args.json, write=False)
        for fn in (cmd_census, cmd_edges, cmd_coupling_diff, cmd_denominator):
            fn(shim)
            print()
        return 0
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
