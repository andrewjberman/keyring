#!/usr/bin/env python3
"""summary_corpus -- comp-similar Phase-1 DERIVE-AT-SCAN corpus (NFRA_COMPSIMILAR).

CTO arch-gate PASS @c3aa13d05 (2026-07-17), ruling 1: corpus v1 = DERIVE-AT-SCAN; the
authored `resource_summaries` overlay is the Phase-3 enrichment, NOT a Description fallback.

WHAT THIS IS
------------
comp-dups scores BM25 over a resource's NAME + file-body (what it *is called* / *is made
of*). comp-similar scores BM25 over a resource's SUMMARY (what it *does*). This module builds
that summary corpus WITHOUT waiting on the authoring fan-out or a new table: each resource's
summary document is SYNTHESIZED at scan time from what the graph already holds --
`node_type + layer + arn + its edge neighborhood (producers -> served -> consumers) +
wiring`. Uniform across resource types, no producer change, read-only.

It is the Phase-1 substrate; the `.tools/comp-similar` CLI + the `supersede` heat-join are
Phase 2. This module is table-independent and projection-independent by construction -- it
reads the live graph via comp-kuzu and returns an in-memory {arn -> SummaryDoc} corpus. The
gated pieces (the `resource_summaries` Iceberg table; the Kuzu LEFT-JOIN projection) do NOT
block it: derive-at-scan is the v1 corpus.

THE CONTROLS IT CARRIES (PRD sec.5 -- controls, not care)
---------------------------------------------------------
- CORPUS-COLLAPSE control: the BM25 document EXCLUDES the resource's OWN name -- if the
  summary were derived from the name, comp-similar would just re-run comp-dups. The corpus is
  sourced from the edge neighborhood + type + layer (purpose), never the resource's identity.
  Neighbor names (writers/readers) ARE included -- they are functional context. `--self-test`
  asserts a name-identical / purpose-different pair scores LOW and a name-different /
  purpose-identical pair scores HIGH.
- BLIND-ROW control (UNKNOWN is a band): a resource whose derived summary carries too few
  purpose tokens is THIN=UNKNOWN (no twin *known*), never "unique". Coverage is printed as a
  denominator on every build (scanned N of M; K UNKNOWN-thin).
- NO DESCRIPTION FALLBACK (CTO ruling 1, binding): a thin derived summary stays UNKNOWN-band;
  it is NEVER patched from the AWS Description field (that re-opens the S3/DDB blindness -- the
  comp-iam action-not-resource failure class). Enrichment is the authored overlay, later.
- HOLD-AWARE: resources whose name matches the held/frozen/sovereign class (_HELD_RX, reused
  from comp_debris) are marked held=True so Phase-2 candidate output can exclude them. The
  corpus still carries their summary (a summary is not a reap verdict).

Advisory / read-only. Builds a corpus + scores similarity. NEVER a verdict, NEVER deletes.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

_HERE = Path(__file__).resolve()
_DEBTSCAN = _HERE.parent          # .../debtscan
_GRAPH_DIR = _HERE.parents[1]     # .../graph
REPO = _HERE.parents[4]           # debtscan -> graph -> modules -> org -> ajb_workspace (matches dup_scan.py)

# Reuse the BM25 engine + the comp-kuzu invocation helper (same debtscan family; DRY).
if str(_DEBTSCAN) not in sys.path:
    sys.path.insert(0, str(_DEBTSCAN))
from dup_scan import BM25  # noqa: E402  (the copy-reusable BM25 scorer, PRD sec.4.1)

# hold-aware: reuse comp_debris' held/frozen/sovereign name class verbatim (single source).
_HELD_RX = re.compile(
    r"(inf-gold|inf-canonical|inf-.*(dispatch|freshness|sentinel|guard)|"
    r"pipeline-complete|frozen|freeze|-hold-|sovereign)", re.I)

# A resource is UNKNOWN-thin when its purpose vocabulary (tokens beyond type+layer) is below
# this floor -- the graph could not tell us enough about what it DOES to know a twin.
THIN_PURPOSE_FLOOR = 3

# ---- tokenization -------------------------------------------------------------------------
_SPLIT = re.compile(r"[^a-z0-9]+")
# connective/id noise we never want as BM25 tokens (they carry ~zero purpose signal).
_STOP = frozenset(
    "the and for not from with via aws arn amazonaws com function role name id ok true false "
    "us east west 313476888478 latest current".split())


def _tok(s: str) -> list[str]:
    return [t for t in _SPLIT.split((s or "").lower()) if len(t) > 1 and t not in _STOP and not t.isdigit()]


# node_type -> the PURPOSE words that say what the resource class DOES (not its name). Down-
# weighted automatically by BM25 idf (a token in ~all lambdas carries little discrimination),
# so this is safe context, not a similarity driver. Unknown types fall back to their split id.
_TYPE_WORDS = {
    "S3_BUCKET": ["s3", "bucket", "storage", "object", "data"],
    "DYNAMODB_TABLE": ["dynamodb", "table", "keyvalue", "store", "item"],
    "LAMBDA": ["lambda", "function", "compute", "handler"],
    "LAMBDA_LAYER": ["lambda", "layer", "dependency", "package"],
    "EVENT_RULE": ["eventbridge", "rule", "event", "trigger"],
    "SCHEDULE": ["scheduler", "schedule", "cron", "recurring"],
    "EVENT_SOURCE": ["event", "source", "mapping", "stream"],
    "SNS_TOPIC": ["sns", "topic", "notification", "publish"],
    "SQS_QUEUE": ["sqs", "queue", "message", "buffer"],
    "SECRET": ["secret", "credential", "token", "manager"],
    "KMS_KEY": ["kms", "key", "encryption", "crypto"],
    "IAM_ROLE": ["iam", "role", "identity", "assume"],
    "IAM_POLICY": ["iam", "policy", "permission", "grant"],
    "IAM_USER": ["iam", "user", "principal"],
    "LOG_GROUP": ["cloudwatch", "logs", "loggroup"],
    "CW_ALARM": ["cloudwatch", "alarm", "metric", "threshold"],
    "API_ROUTE": ["api", "route", "gateway", "endpoint"],
    "API_GW": ["api", "gateway", "rest", "http"],
    "EC2_INSTANCE": ["ec2", "instance", "compute", "runner", "vm"],
    "ECS_TASK_DEF": ["ecs", "task", "container", "definition"],
    "ECS_CLUSTER": ["ecs", "cluster", "container"],
    "SSM_DOCUMENT": ["ssm", "document", "command", "automation"],
    "STATE_MACHINE": ["stepfunctions", "statemachine", "workflow", "orchestration"],
    "CODEBUILD": ["codebuild", "build", "ci"],
    "CLOUDFRONT_DISTRIBUTION": ["cloudfront", "cdn", "distribution", "edge"],
    "LOAD_BALANCER": ["loadbalancer", "elb", "traffic"],
    "INSTANCE_PROFILE": ["instance", "profile", "iam"],
    "SECURITY_GROUP": ["security", "group", "firewall", "network"],
    "S3_BUCKET_POLICY": ["s3", "bucket", "policy", "access"],
    "SERVICE_PRINCIPAL": ["service", "principal"],
    "VPC_ENDPOINT": ["vpc", "endpoint", "network"],
    "ROUTE53": ["route53", "dns", "record"],
}

# edge_type -> a functional-relationship word for the summary. WRITES-in = produced-by;
# READS-in = consumed-by; TRIGGERS/INVOKES/SCHEDULES/ORIGIN = wiring.
_EDGE_WORDS = {
    "WRITES": ["writes", "produces"],
    "READS": ["reads", "consumes"],
    "TRIGGERS": ["triggers", "invokes"],
    "INVOKES": ["invokes"],
    "SCHEDULES": ["schedules"],
    "ORIGIN": ["origin", "serves"],
    "USES_OAI": ["access"],
    "PUBLISHES": ["publishes"],
    "SUBSCRIBES": ["subscribes"],
    "ATTACHED_TO": ["attached"],
    "ASSUMES": ["assumes"],
}


def _type_words(node_type: str) -> list[str]:
    if node_type in _TYPE_WORDS:
        return list(_TYPE_WORDS[node_type])
    return [t for t in (node_type or "").lower().split("_") if t]


# ---- graph load (one read; comp-kuzu --json) ----------------------------------------------
def _kuzu_cmd() -> list[str]:
    """argv prefix to invoke .tools/comp-kuzu by its shebang (Windows-safe -- a bare
    subprocess of a shebang bash script fails on Windows). Mirrors grounding_lib._comp_cmd."""
    import os
    import shutil
    tool = REPO / ".tools" / "comp-kuzu"
    bash = os.environ.get("COMP_DRIFT_BASH") or shutil.which("bash") or "bash"
    py = sys.executable or shutil.which("python") or "python"
    try:
        first = tool.read_text(encoding="utf-8", errors="replace").splitlines()[:1]
        interp = py if (first and "python" in first[0]) else bash
    except OSError:
        interp = bash
    return [interp, str(tool)]


def _kuzu_json(query: str, timeout: int = 180) -> list[dict]:
    """Run a comp-kuzu Cypher query, return the parsed JSON rows. The provenance header is
    printed before the JSON array; we parse the first line that opens a JSON array/object.
    A control on the RETRIEVAL, not the pattern: an empty/error result returns [] LOUDLY
    (the caller prints the denominator), never a silent partial."""
    try:
        r = subprocess.run(_kuzu_cmd() + ["--json", query],
                           cwd=str(REPO), capture_output=True, text=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as e:
        sys.stderr.write(f"summary_corpus: comp-kuzu invocation failed: {e}\n")
        return []
    out = r.stdout or ""
    # find the JSON payload -- the header lines precede a line beginning with '['.
    depth_start = out.find("\n[")
    blob = out[depth_start + 1:] if depth_start >= 0 else (out if out.lstrip().startswith("[") else "")
    if not blob:
        # last resort: scan for a bracket line (matches discover_orphans' tolerant parse).
        for line in out.splitlines():
            s = line.strip()
            if s.startswith("[") or s.startswith("{"):
                blob = "\n".join(out.splitlines()[out.splitlines().index(line):])
                break
    try:
        rows = json.loads(blob)
    except (ValueError, TypeError):
        sys.stderr.write("summary_corpus: could not parse comp-kuzu JSON (empty or malformed)\n")
        return []
    return rows if isinstance(rows, list) else []


def load_graph() -> tuple[dict, dict, dict]:
    """Return (nodes, out_edges, in_edges). ONE-read-ish (2 queries): all ARN-bearing nodes,
    all edges between ARN-bearing nodes. Keyed by arn.
      nodes[arn]     = {arn, node_type, name, layer, drift_class, source}
      out_edges[arn] = [ {edge_type, other_type, other_name, other_arn} ...]  (arn -> other)
      in_edges[arn]  = [ {edge_type, other_type, other_name, other_arn} ...]  (other -> arn)
    """
    node_rows = _kuzu_json(
        "MATCH (n:CloudNode) WHERE n.arn <> '' "
        "RETURN n.arn AS arn, n.node_type AS node_type, n.name AS name, n.layer AS layer, "
        "n.drift_class AS drift_class, n.source AS source")
    edge_rows = _kuzu_json(
        "MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) WHERE a.arn <> '' AND b.arn <> '' "
        "RETURN a.arn AS src, e.edge_type AS et, b.arn AS dst, "
        "a.node_type AS st, a.name AS sn, b.node_type AS bt, b.name AS bn")
    nodes: dict[str, dict] = {}
    for row in node_rows:
        arn = row.get("arn")
        if arn:
            nodes[arn] = row
    out_edges: dict[str, list] = {}
    in_edges: dict[str, list] = {}
    for row in edge_rows:
        src, dst, et = row.get("src"), row.get("dst"), row.get("et")
        if not src or not dst:
            continue
        out_edges.setdefault(src, []).append(
            {"edge_type": et, "other_type": row.get("bt"), "other_name": row.get("bn"), "other_arn": dst})
        in_edges.setdefault(dst, []).append(
            {"edge_type": et, "other_type": row.get("st"), "other_name": row.get("sn"), "other_arn": src})
    return nodes, out_edges, in_edges


# ---- the derive-at-scan summary ------------------------------------------------------------
@dataclass
class SummaryDoc:
    arn: str
    node_type: str
    name: str
    tokens: list[str] = field(default_factory=list)   # the BM25 document (name EXCLUDED)
    prose: str = ""                                    # human summary (name INCLUDED)
    thin: bool = False                                 # UNKNOWN-band (blind-row control)
    held: bool = False                                 # hold-aware mark
    n_purpose: int = 0                                 # purpose-token count (coverage signal)
    motifs: list = field(default_factory=list)         # C2: [(class, role_key, label)] that fired


def _edge_phrase(edge: dict, incoming: bool) -> tuple[list[str], str]:
    """Tokens + a prose fragment for one edge, from THIS resource's vantage.
    incoming=True: (other) -[et]-> (self). outgoing=False: (self) -[et]-> (other)."""
    et = edge.get("edge_type") or ""
    words = _EDGE_WORDS.get(et, [et.lower()] if et else [])
    other_name = edge.get("other_name") or ""
    other_type = edge.get("other_type") or ""
    # neighbor NAME tokens are functional context (a migrated twin shares its writers/readers).
    ntoks = _tok(other_name)
    ttoks = _type_words(other_type)[:1]  # one type word for the neighbor (keeps it light)
    tokens = words + ntoks + ttoks
    if incoming:
        rel = {"WRITES": "produced by", "READS": "consumed by"}.get(et, f"{et.lower()} from")
        frag = f"{rel} {other_name}"
    else:
        rel = {"WRITES": "writes to", "READS": "reads from"}.get(et, f"{et.lower()} to")
        frag = f"{rel} {other_name}"
    return tokens, frag


# ---- C2 MOTIF ENRICHMENT (NFRA_COMPSIMILAR PH2) --------------------------------------------
# Splice the canonical MOTIF CLASS + ROLE a node instantiates into its derive_summary output --
# "instantiates <CLASS> as <label>". DETERMINISTIC: the STRUCTURAL position -> role_key mapping
# is code (classify_motif); the spliced LABEL is READ from canon-patterns.yaml's per-class
# `roles:` field (CTO-owned CLOSED vocab) -- a position with NO blessed label emits NO clause
# (the no-invented-token governance control, CTO 20260718T021711Z). Because it enriches
# derive_summary's OUTPUT it lands in --describe (and later --neighbors) with zero surface change.
#
# SERVED_LINEAGE_CANON is the first class (roles: blessed @ddfe05ae9). Its role predicates are
# GROUNDED on the LIVE graph topology (verified 2026-07-18), which DRIFTS from the canon motif
# PROSE (prose: (Field)-[SERVED_FROM]->(ServedURL); live: ServedURL-[SERVED_FROM]->S3_BUCKET_POLICY,
# Endpoint-[READS_URL]->ServedURL, JSXRender-[RENDERS]->Field, CLOUDFRONT-[ORIGIN]->S3_BUCKET).
# The blessed role KEYS anchor on node_type, so the drift does not block the mapping; the one role
# needing a STRUCTURAL (not type-only) predicate is `s3` -- only a CloudFront-served bucket is an
# "S3 tail", never a pure pipeline/data bucket. DEPLOY/AUTH/PIPELINE roles + C3/Twin/Fork-Shadow
# are OUT OF SCOPE here (their instance-grain source is unwired / held to NFRA_ONTOLOGY LD-0310).
_CANON_PATTERNS = _GRAPH_DIR / "canon-patterns.yaml"
_CANON_ROLES_CACHE: dict | None = None


def _load_canon_roles() -> dict:
    """Return {class_id -> {role_key -> label}} from canon-patterns.yaml's per-pattern `roles:`
    field (CTO-owned CLOSED vocab). Cached. GRACEFUL: any read/parse failure or an absent field
    returns {} -> NO motif clauses splice (the mechanism ships + degrades cleanly, never crashes,
    never invents a label). Read-from-file, NEVER a hardcoded label dict (governance)."""
    global _CANON_ROLES_CACHE
    if _CANON_ROLES_CACHE is not None:
        return _CANON_ROLES_CACHE
    roles: dict[str, dict] = {}
    try:
        import yaml  # PyYAML present in the graph-module runtime (manifest_check_cli.py:41)
        with open(_CANON_PATTERNS, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh) or {}
        for pat in doc.get("patterns", []) or []:
            if isinstance(pat, dict) and pat.get("id") and isinstance(pat.get("roles"), dict):
                roles[pat["id"]] = {str(k): str(v) for k, v in pat["roles"].items()}
    except (OSError, ImportError, ValueError, TypeError):
        roles = {}
    _CANON_ROLES_CACHE = roles
    return roles


# structural node_type -> SERVED_LINEAGE role_key (type-anchored; the FE-stitch types ARE
# served-lineage members by construction). `s3` is handled separately (structural, below).
_SERVED_LINEAGE_TYPE_ROLE = {
    "ServedURL": "served_url",
    "DataFetch": "data_fetch",
    "JSXRender": "jsx_render",
    "Field": "gold_field",
}


def classify_motif(node: dict, in_edges: list, out_edges: list) -> list[tuple[str, str]]:
    """Deterministic per-node structural matcher over the LOCAL neighborhood (the SAME
    {node_type, in_edges, out_edges} derive_summary already loads -- no new full-corpus scan).
    Returns [(CLASS, role_key) ...] for every canonical motif position the node occupies. PURE
    (no graph, no file) -> offline-testable. role_key is a code-internal STRUCTURAL id; the canon
    LABEL is looked up separately (governance: nothing spliced is invented here)."""
    node_type = node.get("node_type") or ""
    matches: list[tuple[str, str]] = []

    # SERVED_LINEAGE_CANON -- the first blessed class. FE-stitch types are members by type; the
    # S3 tail is STRUCTURAL: only a CloudFront-served bucket (an incoming ORIGIN edge from a
    # CLOUDFRONT_DISTRIBUTION), NEVER a pure pipeline/data bucket -> no mislabel, no guess.
    if node_type in _SERVED_LINEAGE_TYPE_ROLE:
        matches.append(("SERVED_LINEAGE_CANON", _SERVED_LINEAGE_TYPE_ROLE[node_type]))
    elif node_type == "S3_BUCKET":
        if any((e.get("edge_type") == "ORIGIN"
                and (e.get("other_type") in ("CLOUDFRONT_DISTRIBUTION", "") or not e.get("other_type")))
               for e in in_edges):
            matches.append(("SERVED_LINEAGE_CANON", "s3"))
    return matches


def motif_prose_and_tokens(matches: list, canon_roles: dict) -> tuple[list[str], list[str], list[tuple]]:
    """Turn structural (class, role_key) matches into (prose_clauses, bm25_tokens, fired) by
    reading the LABEL from canon_roles[class][role_key]. A match whose label is ABSENT emits NO
    clause (the no-invented-token control). PURE -> offline-testable with a fake canon_roles."""
    clauses: list[str] = []
    tokens: list[str] = []
    fired: list[tuple] = []
    for cls, role_key in matches:
        label = (canon_roles.get(cls) or {}).get(role_key)
        if not label:
            continue  # unblessed position -> no clause, never a guessed token
        clauses.append(f"instantiates {cls} as {label}")
        tokens += _tok(label)          # the motif membership is a strong similarity signal
        fired.append((cls, role_key, label))
    return clauses, tokens, fired


def derive_summary(arn: str, node: dict, out_edges: list, in_edges: list) -> SummaryDoc:
    """Synthesize a resource's functional summary from the graph. The BM25 document is the
    PURPOSE vocabulary (type + layer + edge neighborhood); the resource's OWN name is kept in
    the prose but NOT in the tokens (the corpus-collapse control). C2: appends canonical motif
    class+role clauses (read from canon-patterns roles:) to the prose and tokens."""
    node_type = node.get("node_type") or ""
    name = node.get("name") or arn
    layer = node.get("layer") or ""

    base_tokens = _type_words(node_type) + ([layer] if layer and layer != "aws" else [])
    purpose_tokens: list[str] = []
    frags: list[str] = []

    for e in in_edges:
        toks, frag = _edge_phrase(e, incoming=True)
        purpose_tokens += toks
        frags.append(frag)
    for e in out_edges:
        toks, frag = _edge_phrase(e, incoming=False)
        purpose_tokens += toks
        frags.append(frag)

    # C2 motif enrichment -- structural class+role, label read from canon-patterns roles:.
    motif_matches = classify_motif(node, in_edges, out_edges)
    motif_clauses, motif_tokens, motif_fired = motif_prose_and_tokens(motif_matches, _load_canon_roles())

    tokens = base_tokens + purpose_tokens + motif_tokens   # name intentionally EXCLUDED
    n_purpose = len(set(purpose_tokens))
    thin = n_purpose < THIN_PURPOSE_FLOOR
    held = bool(_HELD_RX.search(name))

    prose = f"{node_type} '{name}' ({layer})"
    if frags:
        prose += ": " + "; ".join(frags[:8])
        if len(frags) > 8:
            prose += f"; (+{len(frags) - 8} more)"
    else:
        prose += ": no modeled edges (UNKNOWN-thin)"
    if motif_clauses:
        prose += "; " + "; ".join(motif_clauses)

    return SummaryDoc(arn=arn, node_type=node_type, name=name, tokens=tokens, prose=prose,
                      thin=thin, held=held, n_purpose=n_purpose, motifs=motif_fired)


def build_corpus(graph_tuple=None) -> dict[str, SummaryDoc]:
    """Build the {arn -> SummaryDoc} derive-at-scan corpus from the live graph.

    graph_tuple: an optional pre-loaded (nodes, out_edges, in_edges) in the load_graph() contract.
    When provided -- the IN-VPC path, where the store reads graph_nodes/graph_edges DIRECTLY from
    Iceberg (CTO cond-1, 2026-07-18: comp-kuzu + a local Kuzu DB are absent in the derive container)
    -- it is consumed verbatim. When None (the dev-box default, UNCHANGED) load_graph() runs the
    comp-kuzu path. This decouples the corpus TRANSFORM from the graph SOURCE (one job per layer)."""
    nodes, out_edges, in_edges = graph_tuple if graph_tuple is not None else load_graph()
    corpus: dict[str, SummaryDoc] = {}
    for arn, node in nodes.items():
        corpus[arn] = derive_summary(arn, node, out_edges.get(arn, []), in_edges.get(arn, []))
    return corpus


# ---- DESCRIBE: single-resource find + describe (the thin pull-forward) ---------------------
# NFRA_COMPSIMILAR describe surface -- Andrew-direct pull-forward (2026-07-18) AHEAD of the
# KUZUSPLIT-P1 projection. "find an AWS resource + what does it do" for ONE resource, servable
# NOW off the LANDED derive-at-scan engine reading the EXISTING comp-kuzu QUERY path. Decoupled
# from BOTH gates by construction: NO Kuzu summary-property projection (KUZUSPLIT-P1-gated) and
# NO resource_summaries Iceberg table (CTO plan-gated) -- derive-at-scan means there is no
# projected property to survive a refresh, so it sidesteps the exact risk those gates cover.
#
# Cheap: an exact-ARN describe is TWO targeted comp-kuzu queries (the node + its edge
# neighborhood), never the full-corpus build_corpus(). Resolution is LEXICAL (exact ARN ->
# exact name -> substring) -- a FIND convenience, explicitly NOT the BM25 summary-similarity
# ("nearest by purpose") path, which stays KUZUSPLIT-P1 + table gated as comp-similar Phase-2.


def _q_escape(s: str) -> str:
    """Escape a value for embedding in a Kuzu single-quoted string literal. ARNs carry no
    quotes in practice, but escape defensively (backslash-escape backslash then quote)."""
    return (s or "").replace("\\", "\\\\").replace("'", "\\'")


def _partition_edges(rows: list[dict], arn: str) -> tuple[list[dict], list[dict]]:
    """Split a combined (self on either end) edge result into (out_edges, in_edges) from THIS
    resource's vantage -- the same {edge_type, other_type, other_name, other_arn} shape
    load_graph() produces, so derive_summary consumes it unchanged. A self-loop (src==dst==arn)
    is correctly BOTH an out- and an in-edge. Pure (offline-testable)."""
    out_edges: list[dict] = []
    in_edges: list[dict] = []
    for r in rows:
        src, dst = r.get("src"), r.get("dst")
        if src == arn:
            out_edges.append({"edge_type": r.get("et"), "other_type": r.get("bt"),
                              "other_name": r.get("bn"), "other_arn": dst})
        if dst == arn:
            in_edges.append({"edge_type": r.get("et"), "other_type": r.get("st"),
                             "other_name": r.get("sn"), "other_arn": src})
    return out_edges, in_edges


def load_one(arn: str) -> tuple[dict | None, list, list]:
    """Targeted single-ARN load: the node + its in/out edge neighborhood (2 comp-kuzu queries).
    Returns (node|None, out_edges, in_edges). node is None LOUDLY when the ARN is absent from the
    graph -- the caller distinguishes 'not modeled' from 'stale vintage' (positive-control
    doctrine), never a silent empty describe."""
    a = _q_escape(arn)
    node_rows = _kuzu_json(
        f"MATCH (n:CloudNode) WHERE n.arn = '{a}' "
        "RETURN n.arn AS arn, n.node_type AS node_type, n.name AS name, n.layer AS layer, "
        "n.drift_class AS drift_class, n.source AS source LIMIT 1")
    if not node_rows:
        return None, [], []
    edge_rows = _kuzu_json(
        f"MATCH (a:CloudNode)-[e:CloudEdge]->(b:CloudNode) "
        f"WHERE (a.arn = '{a}' OR b.arn = '{a}') AND a.arn <> '' AND b.arn <> '' "
        "RETURN a.arn AS src, e.edge_type AS et, b.arn AS dst, "
        "a.node_type AS st, a.name AS sn, b.node_type AS bt, b.name AS bn")
    out_edges, in_edges = _partition_edges(edge_rows, arn)
    return node_rows[0], out_edges, in_edges


def _is_real_arn(s: str) -> bool:
    """A canonical AWS ARN starts with 'arn:'. Some graph nodes carry a BARE name in their arn
    field (e.g. an S3_BUCKET_POLICY whose arn is literally 'opal-data-bd') -- an attachment node,
    not the primary resource. Real-ARN nodes are preferred when a bare name matches both."""
    return (s or "").startswith("arn:")


def _prefer_resolve(rows: list[dict]) -> tuple[str | None, list[dict]]:
    """rows (each {arn,name,node_type}) -> (arn|None, candidates). PREFER canonical real-ARN
    resources over bare-arn attachment nodes (a bucket over its policy); a genuine tie WITHIN the
    preferred tier -> candidates (no silent guess). PURE -> offline-testable."""
    if not rows:
        return None, []
    real = [r for r in rows if _is_real_arn(r.get("arn") or "")]
    pref = real if real else rows
    if len(pref) == 1:
        return pref[0].get("arn"), []
    return None, pref


def resolve_query(query: str) -> tuple[str | None, list[dict]]:
    """Resolve a describe query to a single ARN. LEXICAL (never BM25):
      - an ARN query ('arn:...') -> exact-ARN match.
      - a BARE-NAME query -> exact-name then substring, PREFERRING a canonical real-ARN resource
        over a bare-arn attachment node (bucket over its policy); ambiguous within the preferred
        tier -> candidates. A bare token that is literally some node's arn is the last resort.
    Returns (arn|None, candidates). (None, []) = nothing matched; (None, [rows]) = ambiguous.
    Fix (2026-07-18, base finding): `--describe opal-data-bd` used to land on the S3_BUCKET_POLICY
    (arn == the bare name 'opal-data-bd') instead of the S3_BUCKET (arn 'arn:aws:s3:::opal-data-bd')
    -- the exact-arn step matched the policy's bare arn first. Now a bare name prefers the resource."""
    q = query or ""
    if _is_real_arn(q):
        exact = _kuzu_json(f"MATCH (n:CloudNode) WHERE n.arn = '{_q_escape(q)}' "
                           "RETURN n.arn AS arn LIMIT 1")
        if exact:
            return q, []
    # one light (arn, name, type) sweep serves exact-name + substring (no Kuzu string-op reliance).
    allrows = _kuzu_json("MATCH (n:CloudNode) WHERE n.arn <> '' "
                         "RETURN n.arn AS arn, n.name AS name, n.node_type AS node_type")
    ql = q.lower()
    name_exact = [r for r in allrows if (r.get("name") or "").lower() == ql]
    if name_exact:
        return _prefer_resolve(name_exact)
    if ql:
        subs = [r for r in allrows
                if ql in (r.get("name") or "").lower() or ql in (r.get("arn") or "").lower()]
        if subs:
            return _prefer_resolve(subs)
    # last resort: a deliberate bare-arn query (a node whose arn IS this bare token).
    if not _is_real_arn(q) and q:
        bare = _kuzu_json(f"MATCH (n:CloudNode) WHERE n.arn = '{_q_escape(q)}' "
                          "RETURN n.arn AS arn LIMIT 1")
        if bare:
            return q, []
    return None, []


def describe(query: str) -> dict:
    """Find + describe ONE resource from the live graph. Advisory / read-only; NEVER a verdict."""
    arn, candidates = resolve_query(query)
    if arn is None:
        return {"query": query, "resolved": None, "candidates": candidates}
    node, out_edges, in_edges = load_one(arn)
    if node is None:
        return {"query": query, "resolved": arn, "node_absent": True}
    doc = derive_summary(arn, node, out_edges, in_edges)

    def _rel(edges, incoming):
        seen = []
        for e in edges:
            et = e.get("edge_type") or ""
            seen.append(f"{et} <- {e.get('other_type')} '{e.get('other_name')}'" if incoming
                        else f"{et} -> {e.get('other_type')} '{e.get('other_name')}'")
        return seen

    return {
        "query": query, "resolved": arn, "arn": arn,
        "node_type": doc.node_type, "name": doc.name,
        "layer": node.get("layer") or "", "drift_class": node.get("drift_class") or "",
        "source": node.get("source") or "",
        "band": "UNKNOWN-thin" if doc.thin else "summarized",
        "held": doc.held, "n_purpose": doc.n_purpose,
        "prose": doc.prose,
        "motifs": [{"class": c, "role_key": rk, "label": lb} for (c, rk, lb) in doc.motifs],
        "produced_by": _rel(in_edges, incoming=True),
        "consumes_or_serves": _rel(out_edges, incoming=False),
        "n_in": len(in_edges), "n_out": len(out_edges),
    }


def render_describe(result: dict) -> str:
    """Human render of a describe() result (ASCII-only; CloudWatch/charmap safe)."""
    q = result.get("query")
    if result.get("resolved") is None:
        cands = result.get("candidates") or []
        lines = [f"comp-describe: '{q}' did NOT resolve to a single resource."]
        if cands:
            lines.append(f"  {len(cands)} candidate(s) (LEXICAL substring/name match -- NOT similarity):")
            for c in cands[:20]:
                lines.append(f"    {c.get('arn')}   {c.get('node_type')} '{c.get('name')}'")
            if len(cands) > 20:
                lines.append(f"    (+{len(cands) - 20} more -- refine the query)")
            lines.append("  Pass the exact ARN, or a more specific name. (Nearest-BY-PURPOSE is")
            lines.append("  comp-similar, KUZUSPLIT-P1-gated -- describe is exact/lexical find only.)")
        else:
            lines.append("  0 matches (exact ARN, exact name, or lexical substring). If you expected a")
            lines.append("  hit, the local graph may be BEHIND -- `comp-kuzu-inc` to refresh then retry --")
            lines.append("  or this ARN is not modeled in the graph. (Broken retrieval != absent resource.)")
        return "\n".join(lines)
    if result.get("node_absent"):
        return (f"comp-describe: '{q}' resolved to {result.get('resolved')} but the node vanished "
                f"between resolve and load (concurrent refresh?) -- retry.")
    flags = (" [HELD]" if result.get("held") else "")
    lines = [
        f"=== comp-describe: {result['arn']} ===",
        f"  RESOURCE : {result['node_type']} '{result['name']}'  layer={result['layer'] or '-'}  "
        f"band={result['band']}{flags}",
        f"  SUMMARY  : {result['prose']}",
    ]
    if result.get("motifs"):
        lines.append("  MOTIF    : " + "; ".join(
            f"{m['class']} as {m['label']}" for m in result["motifs"]))
    if result.get("produced_by"):
        lines.append(f"  PRODUCED BY / inbound ({result['n_in']}): " + "; ".join(result["produced_by"][:10]))
    if result.get("consumes_or_serves"):
        lines.append(f"  CONSUMES / outbound ({result['n_out']}): " + "; ".join(result["consumes_or_serves"][:10]))
    if result.get("drift_class"):
        lines.append(f"  drift_class={result['drift_class']}  source={result.get('source') or '-'}  "
                     f"purpose_tokens={result.get('n_purpose')}")
    lines.append("  provenance: derive-at-scan over the live comp-kuzu graph (no projected "
                 "property, no resource_summaries table).")
    return "\n".join(lines)


# ---- BM25 over the corpus ------------------------------------------------------------------
class SimilarityIndex:
    """Wrap the reused BM25 engine over a summary corpus. Non-thin docs only carry twin
    claims; thin docs are indexed but their neighbors are UNKNOWN-band (blind-row control)."""

    def __init__(self, corpus: dict[str, SummaryDoc]):
        self.arns = list(corpus.keys())
        self.corpus = corpus
        self.docs = [corpus[a].tokens for a in self.arns]
        self.pos = {a: i for i, a in enumerate(self.arns)}
        self.bm = BM25(self.docs)

    def neighbors(self, arn: str, top: int = 8, min_norm: float = 0.15) -> list[dict]:
        if arn not in self.pos:
            return []
        i = self.pos[arn]
        ceil = self.bm.self_score(i) or 1.0
        out = []
        for score, j in self.bm.neighbors(i, top=top * 2, min_score=0.0):
            b = self.corpus[self.arns[j]]
            norm = round(score / ceil, 3)
            if norm < min_norm:
                continue
            out.append({"arn": b.arn, "name": b.name, "node_type": b.node_type,
                        "norm": norm, "thin": b.thin, "held": b.held})
            if len(out) >= top:
                break
        return out

    def score(self, a: str, b: str) -> float:
        """Normalized (0..1) summary similarity of two arns (0 if either absent)."""
        if a not in self.pos or b not in self.pos:
            return 0.0
        ia, ib = self.pos[a], self.pos[b]
        ceil = self.bm.self_score(ia) or 1.0
        return round(self.bm._score(self.docs[ia], ib) / ceil, 3)


def coverage(corpus: dict[str, SummaryDoc]) -> dict:
    total = len(corpus)
    thin = sum(1 for d in corpus.values() if d.thin)
    held = sum(1 for d in corpus.values() if d.held)
    motif_matched = sum(1 for d in corpus.values() if d.motifs)   # C2: >=1 motif clause fired
    return {"total_arn_resources": total, "summarized": total - thin,
            "unknown_thin": thin, "held_marked": held,
            "motif_matched": motif_matched, "motif_unmatched": total - motif_matched,
            "note": f"scanned {total} ARN resources; {total - thin} with purpose summary; "
                    f"{thin} UNKNOWN-thin (no twin known); {held} hold-marked; "
                    f"{motif_matched} matched >=1 canonical motif, {total - motif_matched} unmatched (no motif clause)"}


# ---- self-test (offline; the registration invariant's regression gate) --------------------
def self_test() -> int:
    """Offline mutant gate -- runs with NO graph. Proves the corpus is BM25-consumable and the
    two named controls hold. Exit 0 = PASS."""
    print("=== summary_corpus --self-test (offline mutants) ===")
    ok = True

    def mkdoc(arn, name, tokens, thin=False):
        return SummaryDoc(arn=arn, node_type="S3_BUCKET", name=name, tokens=tokens,
                          prose="", thin=thin, n_purpose=len(set(tokens)))

    # M1 CORPUS-COLLAPSE control: name-identical, purpose-DIFFERENT -> LOW.
    # (names are excluded from tokens by construction; disjoint purpose vocab must score LOW.)
    corp1 = {
        "arn:a": mkdoc("arn:a", "opal-data-inf", ["writes", "accounts", "positions", "custody", "schwab"]),
        "arn:b": mkdoc("arn:b", "opal-data-inf", ["reads", "benchmarks", "returns", "ycharts", "advisory"]),
    }
    idx1 = SimilarityIndex(corp1)
    s1 = idx1.score("arn:a", "arn:b")
    m1 = s1 < 0.25
    ok &= m1
    print(f"  M1 corpus-collapse (name-same/purpose-diff -> LOW): score={s1} {'PASS' if m1 else 'FAIL'}")

    # M2 FUNCTIONAL-TWIN detection: name-DIFFERENT, purpose-IDENTICAL -> HIGH.
    corp2 = {
        "arn:old": mkdoc("arn:old", "opal-data-inf", ["writes", "produces", "accounts", "positions", "inf", "daily"]),
        "arn:new": mkdoc("arn:new", "opal-data-assets", ["writes", "produces", "accounts", "positions", "inf", "daily"]),
        "arn:noise": mkdoc("arn:noise", "opal-secret-x", ["secret", "credential", "orion", "jwt"]),
    }
    idx2 = SimilarityIndex(corp2)
    s2 = idx2.score("arn:old", "arn:new")
    m2 = s2 >= 0.6
    ok &= m2
    print(f"  M2 functional-twin (name-diff/purpose-same -> HIGH): score={s2} {'PASS' if m2 else 'FAIL'}")

    # M3 BLIND-ROW control: a doc below the purpose floor is thin=UNKNOWN, never a twin claim.
    thin_doc = derive_summary("arn:thin", {"node_type": "S3_BUCKET", "name": "lonely", "layer": "aws"}, [], [])
    m3 = thin_doc.thin and thin_doc.n_purpose < THIN_PURPOSE_FLOOR
    ok &= m3
    print(f"  M3 blind-row (no edges -> UNKNOWN-thin): thin={thin_doc.thin} n_purpose={thin_doc.n_purpose} "
          f"{'PASS' if m3 else 'FAIL'}")

    # M4 NAME-EXCLUSION control: the resource's own name never enters its tokens.
    d = derive_summary("arn:x", {"node_type": "S3_BUCKET", "name": "opal-data-uniquename", "layer": "aws"},
                       [], [{"edge_type": "WRITES", "other_type": "LAMBDA", "other_name": "some-writer", "other_arn": "arn:w"}])
    m4 = "uniquename" not in d.tokens and "opal" not in d.tokens
    ok &= m4
    print(f"  M4 name-exclusion (own name absent from tokens): tokens={d.tokens} {'PASS' if m4 else 'FAIL'}")

    # M5 DESCRIBE edge-partition control (offline; the describe pull-forward's pure core): a
    # combined edge result splits correctly into out/in from the resource's vantage, and a
    # self-loop is BOTH. Guards the single-ARN load's partition against a src/dst swap.
    rows = [
        {"src": "arn:self", "dst": "arn:down", "et": "WRITES", "st": "LAMBDA", "sn": "w",
         "bt": "S3_BUCKET", "bn": "bucket"},                                   # self -> down (out)
        {"src": "arn:up", "dst": "arn:self", "et": "TRIGGERS", "st": "EVENT_RULE", "sn": "rule",
         "bt": "LAMBDA", "bn": "self"},                                        # up -> self (in)
        {"src": "arn:self", "dst": "arn:self", "et": "ASSUMES", "st": "T", "sn": "self",
         "bt": "T", "bn": "self"},                                            # self-loop (both)
    ]
    out_e, in_e = _partition_edges(rows, "arn:self")
    m5 = (len(out_e) == 2 and len(in_e) == 2
          and {e["other_arn"] for e in out_e} == {"arn:down", "arn:self"}
          and {e["other_arn"] for e in in_e} == {"arn:up", "arn:self"})
    ok &= m5
    print(f"  M5 describe edge-partition (out={len(out_e)} in={len(in_e)}, self-loop both): "
          f"{'PASS' if m5 else 'FAIL'}")

    # M6 C2 MOTIF no-invented-token / determinism control (offline; the binding governance test):
    # (a) an ABSENT canon label -> NO clause; (b) a blessed label -> the clause splices and the
    # spliced token is EXACTLY the canon label; (c) an OFF-CANON role_key never splices.
    fake_absent: dict = {}
    fake_blessed = {"SERVED_LINEAGE_CANON": {"s3": "S3 tail"}}
    cl_absent, tk_absent, _ = motif_prose_and_tokens([("SERVED_LINEAGE_CANON", "s3")], fake_absent)
    cl_bless, tk_bless, fired_bless = motif_prose_and_tokens([("SERVED_LINEAGE_CANON", "s3")], fake_blessed)
    cl_off, _, _ = motif_prose_and_tokens([("SERVED_LINEAGE_CANON", "not_a_real_role")], fake_blessed)
    m6a = cl_absent == [] and tk_absent == []
    m6b = any("S3 tail" in c for c in cl_bless) and "s3" in " ".join(tk_bless).lower() and len(fired_bless) == 1
    m6c = cl_off == []
    m6 = m6a and m6b and m6c
    ok &= m6
    print(f"  M6 C2 no-invented-token (absent->no-clause={m6a}, blessed->splices={m6b}, "
          f"off-canon->no-clause={m6c}): {'PASS' if m6 else 'FAIL'}")

    # M7 classify_motif STRUCTURAL control: a CloudFront-served S3 bucket -> s3 role; a pure
    # data/pipeline bucket (no ORIGIN in-edge) -> NO s3 role (no mislabel of a data store).
    served = classify_motif({"node_type": "S3_BUCKET", "name": "b"}, [{"edge_type": "ORIGIN", "other_type": "CLOUDFRONT_DISTRIBUTION"}], [])
    data_b = classify_motif({"node_type": "S3_BUCKET", "name": "b"}, [{"edge_type": "WRITES", "other_type": "LAMBDA"}], [])
    fe = classify_motif({"node_type": "ServedURL", "name": "u"}, [], [])
    m7 = (("SERVED_LINEAGE_CANON", "s3") in served
          and ("SERVED_LINEAGE_CANON", "s3") not in data_b
          and ("SERVED_LINEAGE_CANON", "served_url") in fe)
    ok &= m7
    print(f"  M7 classify_motif structural (served-s3={('SERVED_LINEAGE_CANON','s3') in served}, "
          f"data-s3-excluded={('SERVED_LINEAGE_CANON','s3') not in data_b}, fe-type={('SERVED_LINEAGE_CANON','served_url') in fe}): "
          f"{'PASS' if m7 else 'FAIL'}")

    # M8 resolve preference (base finding): a bare name matching a REAL-ARN resource AND its
    # bare-arn attachment (bucket vs policy) resolves to the RESOURCE, not the attachment; a tie
    # between two real resources -> candidates (no silent guess).
    bucket_vs_policy = [
        {"arn": "arn:aws:s3:::opal-data-bd", "name": "opal-data-bd", "node_type": "S3_BUCKET"},
        {"arn": "opal-data-bd", "name": "opal-data-bd", "node_type": "S3_BUCKET_POLICY"},
    ]
    two_real = [
        {"arn": "arn:aws:iam::x:role/foo", "name": "foo", "node_type": "IAM_ROLE"},
        {"arn": "arn:aws:lambda:x:function:foo", "name": "foo", "node_type": "LAMBDA"},
    ]
    r_arn, r_cand = _prefer_resolve(bucket_vs_policy)
    t_arn, t_cand = _prefer_resolve(two_real)
    m8 = (r_arn == "arn:aws:s3:::opal-data-bd" and r_cand == []
          and t_arn is None and len(t_cand) == 2)
    ok &= m8
    print(f"  M8 resolve-prefer (bucket-over-policy={r_arn=='arn:aws:s3:::opal-data-bd'}, "
          f"two-real->candidates={t_arn is None and len(t_cand)==2}): {'PASS' if m8 else 'FAIL'}")

    print(f"=== self-test: {'PASS' if ok else 'FAIL'} (8/8) ===" if ok else "=== self-test: FAIL ===")
    return 0 if ok else 1


# ---- CLI -----------------------------------------------------------------------------------
def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(
        prog="summary_corpus",
        description="comp-similar Phase-1 derive-at-scan corpus (NFRA_COMPSIMILAR). Advisory; read-only.")
    ap.add_argument("--self-test", action="store_true", help="offline mutant gate (no graph)")
    ap.add_argument("--build", action="store_true", help="build the corpus from the live graph; print coverage + samples")
    ap.add_argument("--neighbors", metavar="ARN", help="summary-similar neighbors of an ARN (proves the corpus is consumable)")
    ap.add_argument("--describe", metavar="ARN_OR_NAME",
                    help="find + describe ONE resource (exact ARN, exact name, or lexical substring); "
                         "cheap 2-query derive-at-scan -- the comp-describe surface")
    ap.add_argument("--samples", type=int, default=6, help="how many sample summaries to print under --build")
    ap.add_argument("--json", action="store_true", help="emit machine JSON")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

    if args.describe:
        result = describe(args.describe)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(render_describe(result))
        # exit 1 when nothing resolved (a describe that finds nothing is a non-zero outcome a
        # caller/script can branch on), 0 on a real description.
        return 0 if result.get("resolved") is not None and not result.get("node_absent") else 1

    if args.build or args.neighbors:
        corpus = build_corpus()
        cov = coverage(corpus)
        if not corpus:
            sys.stderr.write("summary_corpus: EMPTY corpus -- comp-kuzu returned no ARN nodes (broken retrieval, not an empty estate)\n")
            return 2
        if args.neighbors:
            idx = SimilarityIndex(corpus)
            nbrs = idx.neighbors(args.neighbors)
            if args.json:
                print(json.dumps({"arn": args.neighbors, "coverage": cov, "neighbors": nbrs}, indent=2))
            else:
                print(cov["note"])
                self_doc = corpus.get(args.neighbors)
                if self_doc:
                    print(f"\nquery: {self_doc.node_type} '{self_doc.name}'")
                    print(f"  summary: {self_doc.prose}")
                print(f"\nsummary-similar neighbors of {args.neighbors}:")
                for n in nbrs:
                    flags = (" [THIN]" if n["thin"] else "") + (" [HELD]" if n["held"] else "")
                    print(f"  norm={n['norm']:<6} {n['node_type']:<20} {n['name']}{flags}")
                if not nbrs:
                    print("  (none above threshold)")
            return 0
        # --build
        if args.json:
            print(json.dumps({"coverage": cov,
                              "samples": [{"arn": d.arn, "node_type": d.node_type, "name": d.name,
                                           "thin": d.thin, "held": d.held, "prose": d.prose}
                                          for d in list(corpus.values())[:args.samples]]}, indent=2))
        else:
            print("=" * 78)
            print("summary_corpus --build (comp-similar Phase-1 derive-at-scan corpus; advisory)")
            print("=" * 78)
            print(cov["note"])
            print(f"\n=== {args.samples} sample derived summaries ===")
            shown = 0
            for d in corpus.values():
                if d.thin:
                    continue
                flags = (" [HELD]" if d.held else "")
                print(f"\n[{d.node_type}] {d.name}{flags}")
                print(f"  {d.prose}")
                print(f"  tokens({len(set(d.tokens))} distinct): {sorted(set(d.tokens))[:18]}")
                shown += 1
                if shown >= args.samples:
                    break
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
