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
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

_HERE = Path(__file__).resolve()
_DEBTSCAN = _HERE.parent          # .../debtscan
_GRAPH_DIR = _HERE.parents[1]     # .../graph
REPO = _HERE.parents[4]           # debtscan -> graph -> modules -> org -> ajb_workspace (matches dup_scan.py)
sys.path.insert(0, str(REPO / ".tools"))
from git_bash_resolver import git_bash  # noqa: E402  canonical python->bash resolver (never bare/WSL bash)

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
    # shutil.which("bash") CAN resolve the System32 WSL stub -> git_bash() first (retires the silent risk).
    bash = os.environ.get("COMP_DRIFT_BASH") or git_bash() or shutil.which("bash") or "bash"
    py = sys.executable or shutil.which("python") or "python"
    try:
        first = tool.read_text(encoding="utf-8", errors="replace").splitlines()[:1]
        interp = py if (first and "python" in first[0]) else bash
    except OSError:
        interp = bash
    return [interp, str(tool)]


# ---- corpus VINTAGE (D1, 2026-09-02) -------------------------------------------------------
# comp-kuzu prints a provenance header BEFORE its JSON payload and _kuzu_json used to discard
# it wholesale -- so every denominator this module emitted was undated. A stale kuzu DB then
# produces a confident, fully-denominated report about an estate that no longer exists: the
# count says how many rows were scanned, and nothing said WHEN. Captured here, disclosed by
# coverage(). CVO finding 2026-09-02 (D1), exercised on the live corpus before landing.
_CORPUS_VINTAGE: dict = {}

_BUILT_RE = re.compile(r"^\s*built:\s*(\S+)(?:\s*\(age:\s*([^)]*)\))?", re.M)
_DBNAME_RE = re.compile(r"^\s*DB:\s*(\S+)", re.M)


def _capture_kuzu_vintage(*streams: str) -> None:
    """Record the vintage from comp-kuzu's provenance header into _CORPUS_VINTAGE.

    ⛔ THE HEADER IS ON **STDERR**, NOT STDOUT. Measured 2026-09-02 with the streams
    separated: stdout carries the bare JSON array (0 `built:` lines), stderr carries the
    provenance block (1). _kuzu_json's docstring says the header "is printed before the JSON
    array", which reads as one stream and is two -- and a first pass at this fix captured
    stdout only, self-tested GREEN, and still rendered UNKNOWN against the live corpus.
    Both streams are searched so a future comp-kuzu that moves it does not silently re-break.

    ⛔ FAILS TOWARD 'ABSENT', LOUDLY -- never toward a fresh-looking value. If the header
    shape changes or is missing, the dict stays empty and coverage() renders UNKNOWN with an
    explicit do-not-trust clause. A vintage that silently defaulted to 'now' would be the
    exact false-green this fix exists to close."""
    for out in streams:
        m = _BUILT_RE.search(out or "")
        if m:
            break
    else:
        return
    db = _DBNAME_RE.search(out or "")
    _CORPUS_VINTAGE.clear()
    _CORPUS_VINTAGE.update({"built": m.group(1),
                            "age": (m.group(2) or "").strip() or None,
                            "db": db.group(1) if db else None,
                            "claim": "measured"})


def _kuzu_json(query: str, timeout: int = 180) -> list[dict]:
    """Run a comp-kuzu Cypher query, return the parsed JSON rows. The provenance header goes to
    STDERR (measured 2026-09-02 -- this line used to say only "printed before the JSON array",
    which reads as one stream); STDOUT carries the payload, and we parse the first line that
    opens a JSON array/object.
    A control on the RETRIEVAL, not the pattern: an empty/error result returns [] LOUDLY
    (the caller prints the denominator), never a silent partial."""
    try:
        r = subprocess.run(_kuzu_cmd() + ["--json", query],
                           cwd=str(REPO), capture_output=True, text=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as e:
        sys.stderr.write(f"summary_corpus: comp-kuzu invocation failed: {e}\n")
        return []
    out = r.stdout or ""
    # D1: keep the header's vintage. It rides STDERR (measured) -- stdout is checked too so a
    # future comp-kuzu that moves the header does not silently reintroduce the UNKNOWN.
    _capture_kuzu_vintage(r.stderr or "", out)
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
    membership: dict = field(default_factory=dict)     # C3: {"c2":[(id,class)],"c3":[(id,class)]} member-of
    variance: dict = field(default_factory=dict)        # C3/Twin: firm-variance verdict {kind,dim,of_name(s)}


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


# ---- C3/Twin: per-ARN C2/C3 MEMBERSHIP clause (NFRA_COMPSIMILAR PH2, contract @4fe909153) --------
# The long-HELD COMPSIMILAR C3 clause, now concrete on the materialized A+B layer (13 motifs / 3
# systems). For each ARN the summary gains a SIBLING clause listing every C2 motif + C3 system the
# node is a MEMBER of. TWO strictly separate reads (the no-feedback governance line, CTO arch-gate
# @214500Z / NFRA_ONTOLOGY_LLM_CLASSIFICATION sec.1a):
#   1. MEMBERSHIP RESOLUTION is DETERMINISTIC -- reverse the materialized CONTAINS edges (a node's
#      motifs = the C2Motifs whose CONTAINS points at it; its systems = the C3Systems whose CONTAINS
#      points at ANY of those motifs). It NEVER reads an llm_* attribute. ("motif/system membership
#      resolution" is on the FORBIDDEN-llm-consumer list precisely because it must stay structural;
#      this keeps it structural -- a class value can never change the membership SET.)
#   2. The CLASS LABEL is the ADDITIVE readability overlay -- read from the motif/system node's
#      llm_class attribute FOR DISPLAY ONLY (a summary is a human/agent read = the PERMITTED consumer,
#      "~D consumes freely"). Absent (not yet emitted -- the attach rides the OWNS-bump) -> the BARE
#      id, no guess. When the governed emit lands llm_class in the node props the "(class)" parens
#      appear with ZERO code change. NEVER a BM25 token (class must not drive similarity) and NEVER
#      folded into the C2 motif-role splice -- a PARALLEL sibling clause (same shape as variance_verdict).
_MEMBERSHIP_HASH = re.compile(r":[0-9a-f]{6,}$")


def _membership_id(node_id: str) -> str:
    """Display id from a C2Motif/C3System node_id: strip the 'motif:'/'system:' prefix and a trailing
    ':<hash>' discriminator -- 'system:object-data:ff0f4d26' -> 'object-data'; 'motif:a-store' ->
    'a-store'. PURE. The ':<hash>$' anchor requires the ':' separator, so a bare id is never truncated."""
    s = node_id or ""
    for pre in ("motif:", "system:"):
        if s.startswith(pre):
            s = s[len(pre):]
            break
    return _MEMBERSHIP_HASH.sub("", s)


def _llm_class_from_props(props) -> str | None:
    """Read the ADDITIVE llm_class overlay from a node's props (JSON string or dict). None when the
    attr is absent (unemitted) -> the caller renders the bare id (no-guess). GRACEFUL: any parse
    failure -> None. This is the ONLY llm_* read in the membership path, and it is DISPLAY-ONLY."""
    if not props:
        return None
    try:
        d = json.loads(props) if isinstance(props, str) else (props if isinstance(props, dict) else {})
    except (ValueError, TypeError):
        return None
    c = d.get("llm_class") if isinstance(d, dict) else None
    return str(c) if c else None


def _assemble_membership(c2_rows: list, c3_rows: list) -> dict:
    """PURE core: raw CONTAINS-edge rows -> {'c2': [(id, class|None)...], 'c3': [(id, class|None)...]}.
      c2_rows: motif-CONTAINS->node rows for ONE node -- {mid, mprops}.
      c3_rows: system-CONTAINS->motif rows (any)      -- {sid, sprops, mid}.
    Membership is DETERMINISTIC (the node's motifs = the mids in c2_rows; its systems = the systems
    whose CONTAINS points at any of THOSE motifs -- so the c3 set filters c3_rows by this node's
    motifs). The class is looked up separately per (2). De-duped by display id + sorted (determinism).
    Offline-testable (no graph, no file)."""
    sys_by_motif: dict[str, dict] = {}
    for r in c3_rows:
        mid, sid = r.get("mid"), r.get("sid")
        if not mid or not sid:
            continue
        sys_by_motif.setdefault(mid, {})[_membership_id(sid)] = _llm_class_from_props(r.get("sprops"))
    c2: dict[str, str | None] = {}
    c3: dict[str, str | None] = {}
    for r in c2_rows:
        mid = r.get("mid")
        if not mid:
            continue
        c2[_membership_id(mid)] = _llm_class_from_props(r.get("mprops"))
        for sdisp, scls in sys_by_motif.get(mid, {}).items():
            c3[sdisp] = scls
    return {"c2": sorted(c2.items()), "c3": sorted(c3.items())}


def membership_prose(membership: dict) -> str:
    """Render a membership dict as a one-line clause, or '' when the node is in no motif (no-guess):
    'member of C2 [a-store(object-storage), b-io] C3 [object-data(data-platform), pipeline]'. An entry
    with no class label renders as the bare id (the class rides the attachment). PURE -> testable."""
    if not membership:
        return ""
    c2 = membership.get("c2") or []
    c3 = membership.get("c3") or []
    if not c2 and not c3:
        return ""

    def _fmt(entries):
        return ", ".join(f"{mid}({cls})" if cls else mid for mid, cls in entries)

    segs = []
    if c2:
        segs.append(f"C2 [{_fmt(c2)}]")
    if c3:
        segs.append(f"C3 [{_fmt(c3)}]")
    return "member of " + " ".join(segs)


def load_memberships() -> dict:
    """{arn -> {'c2': [...], 'c3': [...]}} for every ARN-bearing node that is a motif member. TWO
    graph reads (all motif-CONTAINS->arn edges; all system-CONTAINS->motif edges). The motif source
    node has arn='' so these edges sit OUTSIDE load_graph()'s (arn<>'' on BOTH ends) edge set BY
    DESIGN -- this is a SEPARATE read. Empty {} LOUDLY on a comp-kuzu absence/error -> the caller just
    emits no membership clause (graceful)."""
    c2_rows = _kuzu_json(
        "MATCH (m:CloudNode)-[e:CloudEdge]->(b:CloudNode) "
        "WHERE m.node_type = 'C2Motif' AND e.edge_type = 'CONTAINS' AND b.arn <> '' "
        "RETURN b.arn AS arn, m.node_id AS mid, m.props AS mprops")
    c3_rows = _kuzu_json(
        "MATCH (s:CloudNode)-[e:CloudEdge]->(m:CloudNode) "
        "WHERE s.node_type = 'C3System' AND e.edge_type = 'CONTAINS' AND m.node_type = 'C2Motif' "
        "RETURN s.node_id AS sid, s.props AS sprops, m.node_id AS mid")
    by_arn: dict[str, list] = {}
    for r in c2_rows:
        arn = r.get("arn")
        if arn:
            by_arn.setdefault(arn, []).append(r)
    return {arn: _assemble_membership(rows, c3_rows) for arn, rows in by_arn.items()}


# ---- C3/Twin: the VARIANCE clause (NFRA_ONTOLOGY variance mechanism @f904033ea; contract @1f258ee21) --
# The declared-dimension SYMMETRY test, realized for the `firm` dimension. Per ARN, a sibling clause naming
# how this instance relates to its firm-siblings (bd/cot/inf parallel replicas): Twin / Canonical / Fork-Shadow.
# STRUCTURE = the C2 motif-membership SET this module already computes -- NO separate producer (the light-gate
# framing). The compare is SET-symmetry across firm-siblings sharing a position_key (name-minus-firm-token).
#
# GOVERNANCE (no-feedback, contract sec.2.6 + bank sec.1a): the verdict is DETERMINISTIC from the membership
# SET (structure), NEVER from an llm_* attribute -- a class value can never change a verdict. Same discipline
# as the membership clause. Direction is strictly structure -> verdict. Display-only; graceful-degrades to no
# clause. The dimension catalog + the clause PHRASING are READ-FROM-FILE (variance_dimensions.yaml, GOVERNED,
# exec-landed like canon-patterns.yaml) -- NEVER hardcoded strings. Absent catalog -> no verdict (graceful).
#
# v1 SCOPE (firm dimension): Twin / Canonical (alphabetically-first modal-matcher) / Fork-Shadow (of the MODAL
# ref -- NOT a fixed firm, so a divergence OF the ref-firm is still detectable; base 234142Z) / no-unique-modal
# -> flag-all "no canonical majority". DEFERRED: Orphan (needs consumer-edge semantics), Superseded (needs a
# supersede edge), Variant (unreachable for firm -- allowed_facets=[]). Singleton (no firm-sibling) -> no clause.
_VARIANCE_DIMS = _GRAPH_DIR / "variance_dimensions.yaml"
_VARIANCE_CACHE: tuple | None = None


def _load_variance_catalog() -> tuple:
    """Return (dimensions, phrasing, fork_shadow_disposition) from variance_dimensions.yaml (GOVERNED,
    read-from-FILE -- mirrors _load_canon_roles). Cached. GRACEFUL: any absence/parse failure -> ({}, {}, {})
    -> no verdict + no clause. `fork_shadow_disposition` is the v2 advisory-conditional suffix map (CTO
    013249Z); absent on a v1 catalog -> the enricher's disposition branch is a no-op (backward-compatible)."""
    global _VARIANCE_CACHE
    if _VARIANCE_CACHE is not None:
        return _VARIANCE_CACHE
    dims: dict = {}
    phrasing: dict = {}
    disposition: dict = {}
    try:
        import yaml
        with open(_VARIANCE_DIMS, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh) or {}
        if isinstance(doc, dict):
            dims = doc.get("dimensions") if isinstance(doc.get("dimensions"), dict) else {}
            phrasing = doc.get("phrasing") if isinstance(doc.get("phrasing"), dict) else {}
            disposition = doc.get("fork_shadow_disposition") if isinstance(doc.get("fork_shadow_disposition"), dict) else {}
    except (OSError, ImportError, ValueError, TypeError):
        dims, phrasing, disposition = {}, {}, {}
    _VARIANCE_CACHE = (dims, phrasing, disposition)
    return _VARIANCE_CACHE


def _firm_values(dims: dict) -> list:
    """The declared firm value-tokens ([bd, cot, inf]) from the catalog; [] when absent (no verdicts)."""
    firm = dims.get("firm") if isinstance(dims, dict) else None
    vals = firm.get("values") if isinstance(firm, dict) else None
    return [str(v) for v in vals] if isinstance(vals, list) else []


def _firm_aliases(dims: dict) -> dict:
    """{firm_value: [client-alias tokens]} from the catalog's firm_aliases map; {} when absent (no strip,
    graceful). An ALIAS is a client-name token that appears at a firm-identity position in a resource NAME
    REDUNDANTLY with the firm VALUE token -- e.g. bd's '49f' in 'bd-49f-etf-ownership-daily'. It is GOVERNED
    (variance_dimensions.yaml firm_aliases), never inferred. It NEVER creates a firm match on its own (the
    value token identifies the firm); it only lets _position_key strip a residual so a firm's two identity
    tokens collapse to one '{firm}'. Absent map -> {} -> _position_key returns the pre-fix value-only key."""
    firm = dims.get("firm") if isinstance(dims, dict) else None
    al = firm.get("firm_aliases") if isinstance(firm, dict) else None
    if not isinstance(al, dict):
        return {}
    return {str(k): [str(t) for t in v] for k, v in al.items() if isinstance(v, list)}


def _position_key(name: str, firm_values: list, firm_aliases: dict | None = None) -> tuple:
    """(position_key, firm_value) -- `name` with the firm identity collapsed to '{firm}': the FIRST declared
    firm VALUE token (at an alnum word boundary) -> '{firm}', then any REDUNDANT same-firm client-ALIAS token
    (governed firm_aliases, e.g. bd's '49f') stripped with its separator debris. (name, None) when no firm
    VALUE token matches -> no firm dimension -> no verdict (counted, never guessed). Structure is NOT in the
    key (the load-bearing Q1 fix). The firm is identified by the VALUE token ONLY (case-sensitive, as the
    estate names them) -- an alias NEVER creates a firm match, it only removes a residual after the value has
    matched, so NOTHING is newly firm-keyed (a name lacking a bd/cot/inf value token is untouched). PURE.
    firm_aliases None/{} (catalog omits the map, or the value-only path) -> the pre-fix value-only key.
      opal-data-bd -> (opal-data-{firm}, bd); opal-data-demo -> (opal-data-demo, None)
      bd-49f-etf-ownership-daily + {bd:[49f]} -> ({firm}-etf-ownership-daily, bd)  [now keys with cot/inf]
      bd-49f-runner              + {bd:[49f]} -> ({firm}-runner, bd)."""
    s = name or ""
    for v in firm_values:
        if not v:
            continue
        new, n = re.subn(r"(?<![A-Za-z0-9])" + re.escape(v) + r"(?![A-Za-z0-9])", "{firm}", s, count=1)
        if n:
            aliases = (firm_aliases or {}).get(v) or []
            stripped = False
            for a in sorted(aliases, key=len, reverse=True):   # longest-first: strip '49financial' before '49f'
                if a:
                    new, cnt = re.subn(r"(?<![A-Za-z0-9])" + re.escape(a) + r"(?![A-Za-z0-9])", "", new)
                    stripped = stripped or bool(cnt)
            if stripped:
                # clean ONLY the separator debris an actual alias removal left: collapse an internal run
                # ('{firm}--etf' -> '{firm}-etf') + trim a trailing residue (alias at the name end). NEVER trim a
                # LEADING separator -- a '/aws/lambda/...' log group legitimately starts with '/', and the firm
                # identity can never be the leading char as debris (it became '{firm}'), so leading debris cannot
                # occur. Guarded on `stripped`: a name with NO alias removed is byte-identical to the value-only
                # key (e.g. /aws/lambda/bd-pipeline-trigger stays /aws/lambda/{firm}-pipeline-trigger).
                new = re.sub(r"([-_/. ])[-_/. ]+", r"\1", new)
                new = re.sub(r"[-_/. ]+$", "", new)
            return new, v
    return s, None


def _variance_verdict(this_firm: str, group: dict) -> dict | None:
    """PURE verdict for one instance. group = {firm_value: (name, structure_frozenset, arn)} for the PRESENT
    firms sharing a position_key. ref = the MODAL membership-SET among present (strict plurality; NOT a fixed
    firm -- a fixed ref inverts on a ref-firm divergence, base 234142Z). Canonical = alphabetically-first
    modal-matcher (a LABEL badge, not the ref STRUCTURE). NEVER reads a class label -- structure is the
    membership SET only (the no-feedback line). Returns the verdict dict or None (singleton / this_firm absent)."""
    if this_firm not in group:
        return None
    present = sorted(group)
    if len(present) < 2:
        return None  # singleton -> no firm-sibling; Orphan/Superseded deferred v1
    this_struct = group[this_firm][1]
    counts = Counter(group[f][1] for f in present)
    max_c = max(counts.values())
    modal_sets = [s for s, c in counts.items() if c == max_c]
    others = sorted(group[f][0] for f in present if f != this_firm)
    if len(modal_sets) != 1 or max_c < 2:
        # tie for plurality (all-distinct / even split) -> NO canonical majority; flag all, never pick a ref.
        return {"kind": "Fork-Shadow", "dim": "firm", "of_names": others, "note": "no canonical majority"}
    modal = modal_sets[0]
    if not modal:
        return None  # all-empty modal -> no meaningful structural reference (e.g. attachment/policy nodes)
    canonical_firm = sorted(f for f in present if group[f][1] == modal)[0]
    if this_struct == modal:
        if this_firm == canonical_firm:
            return {"kind": "Canonical", "dim": "firm", "of_names": others}
        return {"kind": "Twin", "dim": "firm", "of_name": group[canonical_firm][0], "of": group[canonical_firm][2]}
    return {"kind": "Fork-Shadow", "dim": "firm", "of_name": group[canonical_firm][0], "of": group[canonical_firm][2]}


def variance_prose(verdict: dict | None, phrasing: dict, disposition_map: dict | None = None,
                   dims: dict | None = None) -> str:
    """Render a verdict via the GOVERNED phrasing catalog (NEVER hardcoded). '' when verdict is None or its
    `kind` has no blessed phrasing (governance -> no clause, same control as the motif no-invented-token).
    Fills <D>/<of_name>/<of_names>/<by_name>. FORK-SHADOW DISPOSITION (CTO 013249Z render-honesty, v2): the
    <disposition> suffix is ADVISORY-CONDITIONAL -- keyed on the dimension's grounding (allowed_facets EMPTY
    -> the disposition-NEUTRAL 'advisory' string; POPULATED -> the 'grounded' string, e.g. '(debt)'), read
    from `disposition_map` (governed, no hardcode). A 'no canonical majority' note nests before the
    disposition. NO hardcoded '(debt)' in this function -- the disposition string is ALWAYS the catalog's
    (the render-honesty full-denominator invariant, CTO NEXT-3). PURE."""
    if not verdict:
        return ""
    tmpl = (phrasing or {}).get(verdict.get("kind"))
    if not tmpl:
        return ""
    of_names = verdict.get("of_names") or []
    of_name = verdict.get("of_name")
    if of_name is None and of_names:
        of_name = "/".join(of_names)
    disposition = ""
    if verdict.get("kind") == "Fork-Shadow" and "<disposition>" in str(tmpl):
        dim = verdict.get("dim", "")
        af = (dims.get(dim) or {}).get("allowed_facets") if isinstance(dims, dict) else None
        disp_key = "grounded" if af else "advisory"   # populated allowed_facets = grounded; [] / absent = advisory
        base_disp = (disposition_map or {}).get(disp_key, "")
        note = "-- no canonical majority " if verdict.get("note") == "no canonical majority" else ""
        disposition = (note + str(base_disp)).strip()
    s = (str(tmpl)
         .replace("<D>", verdict.get("dim", ""))
         .replace("<of_names>", "/".join(of_names))
         .replace("<of_name>", of_name or "")
         .replace("<by_name>", verdict.get("by_name", ""))
         .replace("<disposition>", disposition))
    return s.strip()


def _compute_variances(nodes: dict, memberships: dict, firm_values: list,
                       firm_aliases: dict | None = None) -> dict:
    """{arn -> verdict|None} for the whole corpus (the FREE build_corpus path -- the sibling groups are the
    already-loaded set). Groups by (NODE_TYPE, position_key); structure = the C2 membership SET (reuse
    memberships). The node_type in the key keeps a resource's twin the SAME KIND -- an S3_BUCKET's firm-twin
    is a bucket, NOT the same-named S3_BUCKET_POLICY (whose bare arn holds no motif membership; colliding them
    inverted the verdict). Within a (type,firm) slot a real-ARN node wins over a bare-arn one. Empty firm_values
    (catalog absent) -> {}. Graph-free given its inputs.

    OVER-MERGE GUARD (CTO arch-gate cond.2): firm-alias normalization (firm_aliases) collapses a firm's
    redundant identity tokens (bd-49f-* -> {firm}-*) so a resource keys with its cross-firm twins. That could,
    in principle, collapse two GENUINELY-DISTINCT same-firm resources (bd-49f-x and a bare bd-x both -> {firm}-x)
    and silently drop one. The guard is a two-pass detect-then-revert: if >=2 DISTINCT value-only keys among
    REAL-ARN nodes land in one (node_type, firm, normalized_key) slot, the strip merged distinct resources ->
    revert those to their value-only (pre-alias) key so they stay apart (never guess which is the twin). Grounded
    ZERO real collisions in the live estate (2026-07-19); the guard is a safety net, not a live corrector. With
    firm_aliases None/{} every normalized key == its value-only key -> the guard is inert and this is the pre-fix
    behavior byte-for-byte."""
    if not firm_values:
        return {}
    firm_aliases = firm_aliases or {}
    # pass 1: per surviving node, the normalized key (nk, alias-stripped) + value-only key (vk, over-merge oracle)
    recs: list = []
    for arn, node in nodes.items():
        name = node.get("name") or arn
        nk, firm = _position_key(name, firm_values, firm_aliases)
        if firm is None:
            continue
        vk, _ = _position_key(name, firm_values)          # value-only key == pre-alias-strip behavior
        recs.append((arn, node, name, nk, vk, firm))
    # detect over-merge: a (node_type, firm, nk) slot holding >=2 distinct value-only keys among real ARNs
    vk_by_slot: dict = {}
    for arn, node, name, nk, vk, firm in recs:
        if _is_real_arn(arn):
            vk_by_slot.setdefault(((node.get("node_type") or ""), firm, nk), set()).add(vk)
    overmerged = {slot for slot, vks in vk_by_slot.items() if len(vks) > 1}
    # pass 2: group; over-merged slots fall back to the value-only key (distinct resources stay distinct)
    groups: dict = {}
    node_firm: dict = {}
    for arn, node, name, nk, vk, firm in recs:
        ntype = node.get("node_type") or ""
        use_key = vk if (ntype, firm, nk) in overmerged else nk
        key = (ntype, use_key)
        struct = frozenset(i for (i, _) in (memberships.get(arn, {}).get("c2") or []))
        slot = groups.setdefault(key, {})
        prev = slot.get(firm)
        if prev is None or (_is_real_arn(arn) and not _is_real_arn(prev[2])):
            slot[firm] = (name, struct, arn)
        node_firm[arn] = (firm, key)
    return {arn: _variance_verdict(firm, groups.get(key, {})) for arn, (firm, key) in node_firm.items()}


def load_one_variance(arn: str, node_name: str, node_type: str, this_membership: dict,
                      firm_values: list, firm_aliases: dict | None = None) -> dict | None:
    """Single-ARN variance (the --describe path): find the SAME-node_type firm-siblings sharing this node's
    position_key and compute the verdict. None when the catalog is absent (firm_values=[]) or the node carries
    no firm dimension. node_type is part of the sibling identity -- a bucket's firm-twin is a bucket, not the
    same-named policy. Cost = at most TWO TARGETED comp-kuzu queries (no full-graph sweep): sibling names are
    the position_key with '{firm}' substituted back per declared value (that IS the sibling model), fetched by
    an exact name-IN + node_type filter; then ONE BATCHED motif-membership read for all sibling ARNs.

    ALIAS-NORMALIZE (firm_aliases): the forward key is now LOSSY (bd-49f-* collapsed the '49f'), so a bare
    value-substitution ('{firm}'->'bd') would MISS the real bd-49f-* sibling. Over-generate the candidate names
    per firm -- the bare value AND value+alias forms (fused + common separators) -- so the name-IN query finds
    the real sibling however it is spelled. Over-generation is SAFE (phantom candidates match no node). If TWO
    DISTINCT real-ARN siblings match one firm (the over-merge case), it is ambiguous which is the twin -> drop
    that firm from the group (never guess), mirroring _compute_variances' guard on the corpus path."""
    if not firm_values:
        return None
    firm_aliases = firm_aliases or {}
    pk, firm = _position_key(node_name or arn, firm_values, firm_aliases)
    if firm is None:
        return None
    this_struct = frozenset(i for (i, _) in (this_membership.get("c2") or []))
    # reconstruct each firm-sibling's candidate NAME(s): '{firm}' -> the value AND value+alias forms (lossy
    # forward key -> over-generate the inverse). name_to_firm maps every candidate spelling back to its firm.
    name_to_firm: dict = {}
    for v in firm_values:
        forms = {v}
        for a in firm_aliases.get(v, []):
            if a:
                forms.add(v + a)                        # fused (bd49f)
                for sep in ("-", "_"):
                    forms.add(v + sep + a)              # value-sep-alias (bd-49f / bd_49f)
        for form in forms:
            name_to_firm[pk.replace("{firm}", form)] = v
    name_list = ", ".join("'" + _q_escape(n) + "'" for n in name_to_firm)
    rows = _kuzu_json(
        f"MATCH (n:CloudNode) WHERE n.arn <> '' AND n.node_type = '{_q_escape(node_type or '')}' "
        f"AND n.name IN [{name_list}] RETURN n.arn AS arn, n.name AS name")
    group = {firm: (node_name or arn, this_struct, arn)}   # self, membership already in hand
    sib_arn_by_firm: dict = {}
    ambiguous_firms: set = set()
    for r in rows:
        rarn, rname = r.get("arn"), r.get("name") or ""
        rfirm = name_to_firm.get(rname)
        if not rarn or rarn == arn or rfirm is None or rfirm == firm:
            continue
        prev = sib_arn_by_firm.get(rfirm)               # prefer a real-ARN sibling over a bare-arn one
        if prev is not None and prev != rarn and _is_real_arn(prev) and _is_real_arn(rarn):
            ambiguous_firms.add(rfirm)                  # over-merge: 2 distinct real siblings -> can't pick
            continue
        if prev is None or (_is_real_arn(rarn) and not _is_real_arn(prev)):
            sib_arn_by_firm[rfirm] = rarn
            group[rfirm] = (rname, None, rarn)           # placeholder; structure filled from the batch read
    for f in ambiguous_firms:                            # drop ambiguous firms entirely (never guess the twin)
        sib_arn_by_firm.pop(f, None)
        group.pop(f, None)
    sib_arns: list = list(sib_arn_by_firm.values())
    if sib_arns:
        arn_list = ", ".join("'" + _q_escape(a) + "'" for a in sib_arns)
        mrows = _kuzu_json(
            f"MATCH (m:CloudNode)-[e:CloudEdge]->(b:CloudNode) "
            f"WHERE m.node_type = 'C2Motif' AND e.edge_type = 'CONTAINS' AND b.arn IN [{arn_list}] "
            "RETURN b.arn AS arn, m.node_id AS mid")
        struct_by_arn: dict = {}
        for mr in mrows:
            a2, mid = mr.get("arn"), mr.get("mid")
            if a2 and mid:
                struct_by_arn.setdefault(a2, set()).add(_membership_id(mid))
        for f, (n, s, a) in list(group.items()):
            if s is None:
                group[f] = (n, frozenset(struct_by_arn.get(a, set())), a)
    return _variance_verdict(firm, group)


def derive_summary(arn: str, node: dict, out_edges: list, in_edges: list,
                   membership: dict | None = None, variance: dict | None = None) -> SummaryDoc:
    """Synthesize a resource's functional summary from the graph. The BM25 document is the
    PURPOSE vocabulary (type + layer + edge neighborhood); the resource's OWN name is kept in
    the prose but NOT in the tokens (the corpus-collapse control). C2: appends canonical motif
    class+role clauses (read from canon-patterns roles:) to the prose and tokens. C3: appends the
    per-ARN C2/C3 MEMBERSHIP sibling clause (deterministic reverse-CONTAINS, passed in via
    `membership`) to the prose ONLY -- NOT the tokens (the class overlay must not drive similarity).
    C3/Twin: appends the firm-VARIANCE verdict clause (passed in via `variance`, phrasing read from the
    governed catalog) to the prose ONLY -- a relative verdict must not cluster in BM25 (prose, no token)."""
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

    # C3 membership sibling clause (deterministic reverse-CONTAINS; class = display-only overlay).
    # Prose ONLY (readability) -- deliberately NOT added to `tokens` (keeps the llm_class overlay out
    # of the BM25 similarity computation, and keeps membership resolution structurally separate).
    memb = membership or {}
    memb_clause = membership_prose(memb)
    if memb_clause:
        prose += "; " + memb_clause

    # C3/Twin firm-variance verdict clause (deterministic sibling-symmetry; phrasing from the governed
    # catalog). Prose ONLY -- a per-sibling verdict is a relative fact, never a BM25 similarity driver.
    _var_dims, _var_phrasing, _var_disp = _load_variance_catalog()
    var_clause = variance_prose(variance, _var_phrasing, _var_disp, _var_dims)
    if var_clause:
        prose += "; " + var_clause

    return SummaryDoc(arn=arn, node_type=node_type, name=name, tokens=tokens, prose=prose,
                      thin=thin, held=held, n_purpose=n_purpose, motifs=motif_fired, membership=memb,
                      variance=variance or {})


def build_corpus(graph_tuple=None, memberships=None, variances=None) -> dict[str, SummaryDoc]:
    """Build the {arn -> SummaryDoc} derive-at-scan corpus from the live graph.

    graph_tuple: an optional pre-loaded (nodes, out_edges, in_edges) in the load_graph() contract.
    When provided -- the IN-VPC path, where the store reads graph_nodes/graph_edges DIRECTLY from
    Iceberg (CTO cond-1, 2026-07-18: comp-kuzu + a local Kuzu DB are absent in the derive container)
    -- it is consumed verbatim. When None (the dev-box default, UNCHANGED) load_graph() runs the
    comp-kuzu path. This decouples the corpus TRANSFORM from the graph SOURCE (one job per layer).

    memberships: an optional {arn -> {'c2','c3'}} membership map. When None on the DEV-BOX path
    (graph_tuple None) it is loaded via load_memberships() (comp-kuzu). On the IN-VPC path (graph_tuple
    given, comp-kuzu absent) it defaults to {} -- no comp-kuzu call, so the membership clause is simply
    omitted there until the caller threads a membership source in (graceful, symmetric with graph_tuple)."""
    nodes, out_edges, in_edges = graph_tuple if graph_tuple is not None else load_graph()
    if memberships is None:
        memberships = {} if graph_tuple is not None else load_memberships()
    if variances is None:
        # in-VPC (graph_tuple) has no motif/variance substrate -> {}; dev-box computes from memberships.
        _vc_dims = _load_variance_catalog()[0]
        variances = {} if graph_tuple is not None else _compute_variances(
            nodes, memberships, _firm_values(_vc_dims), _firm_aliases(_vc_dims))
    corpus: dict[str, SummaryDoc] = {}
    for arn, node in nodes.items():
        corpus[arn] = derive_summary(arn, node, out_edges.get(arn, []), in_edges.get(arn, []),
                                     membership=memberships.get(arn), variance=variances.get(arn))
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


def load_one_membership(arn: str) -> dict:
    """Targeted single-ARN membership (the describe path): the C2 motifs that CONTAIN this arn + the
    C3 systems that CONTAIN those motifs. Returns {'c2': [...], 'c3': [...]} -- {'c2': [], 'c3': []}
    when the node is in no motif (no-guess). The system->motif edge set is tiny (a handful), so it is
    read whole and _assemble_membership filters it to THIS node's motifs. NEVER reads llm_* to resolve
    membership (structural); llm_class rides along only as the display overlay (see _assemble_membership)."""
    a = _q_escape(arn)
    c2_rows = _kuzu_json(
        f"MATCH (m:CloudNode)-[e:CloudEdge]->(b:CloudNode) "
        f"WHERE m.node_type = 'C2Motif' AND e.edge_type = 'CONTAINS' AND b.arn = '{a}' "
        "RETURN m.node_id AS mid, m.props AS mprops")
    if not c2_rows:
        return {"c2": [], "c3": []}
    c3_rows = _kuzu_json(
        "MATCH (s:CloudNode)-[e:CloudEdge]->(m:CloudNode) "
        "WHERE s.node_type = 'C3System' AND e.edge_type = 'CONTAINS' AND m.node_type = 'C2Motif' "
        "RETURN s.node_id AS sid, s.props AS sprops, m.node_id AS mid")
    return _assemble_membership(c2_rows, c3_rows)


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
    memb = load_one_membership(arn)
    dims, var_phrasing, var_disp = _load_variance_catalog()
    var = load_one_variance(arn, node.get("name") or "", node.get("node_type") or "", memb,
                            _firm_values(dims), _firm_aliases(dims))
    doc = derive_summary(arn, node, out_edges, in_edges, membership=memb, variance=var)

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
        "membership": {
            "c2": [{"id": i, "class": c} for (i, c) in (doc.membership.get("c2") or [])],
            "c3": [{"id": i, "class": c} for (i, c) in (doc.membership.get("c3") or [])],
        },
        "variance": doc.variance or {},
        "variance_clause": variance_prose(doc.variance, var_phrasing, var_disp, dims),
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
    memb = result.get("membership") or {}
    if memb.get("c2") or memb.get("c3"):
        def _fmt_memb(entries):
            return ", ".join(f"{e['id']}({e['class']})" if e.get("class") else e["id"] for e in entries)
        parts = []
        if memb.get("c2"):
            parts.append(f"C2 [{_fmt_memb(memb['c2'])}]")
        if memb.get("c3"):
            parts.append(f"C3 [{_fmt_memb(memb['c3'])}]")
        lines.append("  MEMBERSHIP: " + " ".join(parts))
    if result.get("variance_clause"):
        lines.append("  VARIANCE : " + result["variance_clause"])
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
    memb_matched = sum(1 for d in corpus.values()                 # C3: >=1 C2/C3 membership
                       if (d.membership or {}).get("c2") or (d.membership or {}).get("c3"))
    var_verdicts = sum(1 for d in corpus.values() if d.variance)  # C3/Twin: a firm-variance verdict fired
    fork_shadows = sum(1 for d in corpus.values()
                       if (d.variance or {}).get("kind") == "Fork-Shadow")
    # D1 -- THE DENOMINATOR SAYS HOW MANY, THE VINTAGE SAYS WHEN. Both or neither.
    # The vintage is ALWAYS disclosed; its VALUE may be unknown, and unknown says so.
    v = dict(_CORPUS_VINTAGE) or {"claim": "absent"}
    if v.get("claim") == "measured":
        vintage_note = (f"corpus built: {v['built']}"
                        + (f" (age: {v['age']})" if v.get("age") else "")
                        + (f", DB {v['db']}" if v.get("db") else ""))
    else:
        vintage_note = ("corpus built: UNKNOWN -- vintage undisclosed by the retrieval; "
                        "DO NOT read this denominator as current")
    return {"total_arn_resources": total, "summarized": total - thin,
            "unknown_thin": thin, "held_marked": held,
            "motif_matched": motif_matched, "motif_unmatched": total - motif_matched,
            "membership_matched": memb_matched, "membership_unmatched": total - memb_matched,
            "variance_verdicts": var_verdicts, "fork_shadows": fork_shadows,
            "corpus_built": v.get("built"), "corpus_age": v.get("age"),
            "corpus_db": v.get("db"), "corpus_vintage_claim": v.get("claim", "absent"),
            "vintage_note": vintage_note,
            "note": f"{vintage_note}\nscanned {total} ARN resources; {total - thin} with purpose summary; "
                    f"{thin} UNKNOWN-thin (no twin known); {held} hold-marked; "
                    f"{motif_matched} matched >=1 canonical motif, {total - motif_matched} unmatched (no motif clause); "
                    f"{memb_matched} carry a C2/C3 membership clause, {total - memb_matched} in no canonical motif; "
                    f"{var_verdicts} carry a firm-variance verdict ({fork_shadows} fork-shadow(s))"}


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

    # M9 C3 MEMBERSHIP control (offline; the contract @4fe909153 shape + the no-feedback separation).
    # Fake CONTAINS rows mirroring the LIVE opal-data-bd membership (verified on the graph 2026-07-18):
    # motifs {a-store,a-access,a-serve,b-io}; systems object-data (all 4) + pipeline (via the b-io overlap);
    # compute-orchestration (a-event/a-orch) must NOT appear (the node is in neither). b-io has NO class ->
    # bare id (the class rides the attachment). Then MUTATE every class value: the membership SET must be
    # INVARIANT (membership resolution is structural, never reads llm_* -- the forbidden-consumer line).
    bd_c2 = [
        {"mid": "motif:a-store", "mprops": '{"llm_class": "object-storage"}'},
        {"mid": "motif:a-access", "mprops": '{"llm_class": "compute-object-access"}'},
        {"mid": "motif:a-serve", "mprops": '{"llm_class": "content-serving"}'},
        {"mid": "motif:b-io", "mprops": "{}"},                       # no class -> bare id (no-guess)
    ]
    all_c3 = [
        {"sid": "system:object-data:ff0f4d26", "sprops": '{"llm_class": "data-platform"}', "mid": "motif:a-store"},
        {"sid": "system:object-data:ff0f4d26", "sprops": '{"llm_class": "data-platform"}', "mid": "motif:a-access"},
        {"sid": "system:object-data:ff0f4d26", "sprops": '{"llm_class": "data-platform"}', "mid": "motif:a-serve"},
        {"sid": "system:object-data:ff0f4d26", "sprops": '{"llm_class": "data-platform"}', "mid": "motif:b-io"},
        {"sid": "system:pipeline:d944eb81", "sprops": '{"llm_class": "data-pipeline"}', "mid": "motif:b-struct"},
        {"sid": "system:pipeline:d944eb81", "sprops": '{"llm_class": "data-pipeline"}', "mid": "motif:b-run"},
        {"sid": "system:pipeline:d944eb81", "sprops": '{"llm_class": "data-pipeline"}', "mid": "motif:b-io"},
        {"sid": "system:compute-orchestration:7628b54d", "sprops": '{"llm_class": "orchestration-platform"}', "mid": "motif:a-event"},
    ]
    mem = _assemble_membership(bd_c2, all_c3)
    c2_ids = [i for (i, _) in mem["c2"]]
    c3_ids = [i for (i, _) in mem["c3"]]
    m9a = c2_ids == ["a-access", "a-serve", "a-store", "b-io"] and c3_ids == ["object-data", "pipeline"]
    c2_cls = dict(mem["c2"])
    m9b = c2_cls.get("a-store") == "object-storage" and c2_cls.get("b-io") is None  # class overlay + bare-id
    clause = membership_prose(mem)
    m9c = ("member of C2 [" in clause and "a-store(object-storage)" in clause
           and "C3 [" in clause and "object-data(data-platform)" in clause and "pipeline" in clause)
    # no-feedback exercise: MUTATE every class -> membership SET unchanged (class never drives membership).
    mut_c2 = [dict(r, mprops='{"llm_class": "MUTANT"}') for r in bd_c2]
    mut_c3 = [dict(r, sprops='{"llm_class": "MUTANT"}') for r in all_c3]
    mem_mut = _assemble_membership(mut_c2, mut_c3)
    m9d = ([i for (i, _) in mem_mut["c2"]] == c2_ids and [i for (i, _) in mem_mut["c3"]] == c3_ids)
    # id derivation (prefix + hash strip) + no-motif -> empty clause (no-guess).
    m9e = (_membership_id("system:object-data:ff0f4d26") == "object-data"
           and _membership_id("motif:a-store") == "a-store"
           and _assemble_membership([], all_c3) == {"c2": [], "c3": []}
           and membership_prose({"c2": [], "c3": []}) == "")
    m9 = m9a and m9b and m9c and m9d and m9e
    ok &= m9
    print(f"  M9 C3 membership (bd-shape[4motif/2sys,b-io-overlap]={m9a}, class-overlay+bare-id={m9b}, "
          f"prose={m9c}, SET-invariant-under-class-mutation={m9d}, id-derivation+no-guess={m9e}): "
          f"{'PASS' if m9 else 'FAIL'}")

    # M10 C3/Twin VARIANCE control (offline; contract @1f258ee21 sec.3 worked examples). Verdict is PURE over
    # the membership-SETs -- no graph, no catalog, NO class read (no-feedback by construction: _variance_verdict
    # takes no llm_* input). FULL = the bd/cot/inf shared set; PART = a diverging set.
    FULL = frozenset({"a-access", "a-serve", "a-store", "b-io"})
    PART = frozenset({"a-store", "a-access"})
    FV = ["bd", "cot", "inf"]
    # firm-alias map (mirrors variance_dimensions.yaml firm_aliases) -- the client-alias tokens _position_key
    # strips once the VALUE token matched (offline fixture; the live catalog is read via _firm_aliases).
    FA = {"bd": ["49financial", "blackdiamond", "bd49f", "49f"], "cot": ["cottonwood"], "inf": ["inflection"]}

    def _grp(**kw):  # firm -> (name, structure, arn)
        return {f: (f"opal-data-{f}", s, f"arn:{f}") for f, s in kw.items()}

    # (a) position_key: strip the firm VALUE token at a boundary; no-firm -> None (denominator, no guess).
    #   value-only path (no alias map) is UNCHANGED / graceful; the alias path collapses bd-49f-* -> {firm}-*.
    m10a = (_position_key("opal-data-bd", FV) == ("opal-data-{firm}", "bd")
            and _position_key("opal-data-demo", FV) == ("opal-data-demo", None)
            and _position_key("bd-49f-runner", FV) == ("{firm}-49f-runner", "bd")          # value-only: unchanged
            # ALIAS-STRIP (the @c2a0cd66b fix): 49f collapses so bd keys WITH cot/inf --------------------------
            and _position_key("bd-49f-etf-ownership-daily", FV, FA) == ("{firm}-etf-ownership-daily", "bd")
            and _position_key("cot-etf-ownership-daily", FV, FA) == ("{firm}-etf-ownership-daily", "cot")
            and _position_key("bd-49f-runner", FV, FA) == ("{firm}-runner", "bd")
            and _position_key("opal-data-bd", FV, FA) == ("opal-data-{firm}", "bd")          # no alias residual
            # LEADING-SEP REGRESSION (the cleanup must NOT eat a leading '/' of a log-group name): WITH an alias
            # removed, the slash survives + collapses debris -> keys 3-way; WITHOUT an alias, byte-identical to
            # value-only (the cleanup is guarded on an actual strip).
            and _position_key("/aws/lambda/bd-49f-etf-ownership-daily", FV, FA) == ("/aws/lambda/{firm}-etf-ownership-daily", "bd")
            and _position_key("/aws/lambda/bd-pipeline-trigger", FV, FA) == ("/aws/lambda/{firm}-pipeline-trigger", "bd")
            and _position_key("/aws/lambda/bd-pipeline-trigger", FV) == _position_key("/aws/lambda/bd-pipeline-trigger", FV, FA)  # no-alias: alias-path == value-only
            # SCOPE GUARD: case-sensitive VALUE-token match -> 'Inflection Models' is NOT firm-keyed (no verdict)
            and _position_key("Inflection Models", FV, FA) == ("Inflection Models", None))

    # (b) TWIN case: all three identical -> bd=Canonical (alpha-first), cot/inf=Twin of bd.
    gt = _grp(bd=FULL, cot=FULL, inf=FULL)
    vb, vc, vi = _variance_verdict("bd", gt), _variance_verdict("cot", gt), _variance_verdict("inf", gt)
    m10b = (vb["kind"] == "Canonical" and set(vb["of_names"]) == {"opal-data-cot", "opal-data-inf"}
            and vc["kind"] == "Twin" and vc["of_name"] == "opal-data-bd"
            and vi["kind"] == "Twin" and vi["of_name"] == "opal-data-bd")

    # (c) FORK-SHADOW (inf diverges): bd/cot=modal, inf differs -> inf=Fork-Shadow of bd; bd=Canonical, cot=Twin.
    gi = _grp(bd=FULL, cot=FULL, inf=PART)
    m10c = (_variance_verdict("inf", gi)["kind"] == "Fork-Shadow"
            and _variance_verdict("inf", gi)["of_name"] == "opal-data-bd"
            and _variance_verdict("bd", gi)["kind"] == "Canonical"
            and _variance_verdict("cot", gi)["kind"] == "Twin")

    # (d) FORK-SHADOW (BD diverges -- the case a FIXED ref=bd would have HIDDEN, base 234142Z): cot/inf=modal,
    # bd differs -> bd=Fork-Shadow of cot (alpha-first modal-matcher); cot=Canonical, inf=Twin. Modal ref detects it.
    gb = _grp(bd=PART, cot=FULL, inf=FULL)
    m10d = (_variance_verdict("bd", gb)["kind"] == "Fork-Shadow"
            and _variance_verdict("bd", gb)["of_name"] == "opal-data-cot"
            and _variance_verdict("cot", gb)["kind"] == "Canonical"
            and _variance_verdict("inf", gb)["kind"] == "Twin")

    # (e) NO unique modal (all distinct) -> flag ALL "no canonical majority", never pick a ref.
    gn = _grp(bd=frozenset({"a-store"}), cot=frozenset({"a-access"}), inf=frozenset({"b-io"}))
    nb = _variance_verdict("bd", gn)
    m10e = (nb["kind"] == "Fork-Shadow" and nb.get("note") == "no canonical majority"
            and set(nb["of_names"]) == {"opal-data-cot", "opal-data-inf"})

    # (f) PROSE for the NON-Fork-Shadow kinds (Canonical/Twin) from a fake governed catalog + absent phrasing
    # -> no clause. Fork-Shadow disposition rendering (both regimes) is m10i. NO '(debt)' fixture here: the v2
    # catalog is canonical, so the obsolete v1 literal-'(debt)' backward-compat path was removed (CTO NEXT-3
    # render-honesty full-denominator -- the only legit '(debt)' is a GROUNDED-dimension render, m10i).
    ph = {"Canonical": "canonical <D>-twin (reference) of <of_names>",
          "Twin": "canonical <D>-twin of <of_name>"}
    m10f = (variance_prose(vb, ph) == "canonical firm-twin (reference) of opal-data-cot/opal-data-inf"
            and variance_prose(vc, ph) == "canonical firm-twin of opal-data-bd"
            and variance_prose(vb, {}) == "")  # catalog absent -> no clause (graceful, no hardcode)

    # (g) singleton -> None (no firm-sibling; Orphan deferred); this_firm absent -> None.
    m10g = _variance_verdict("bd", _grp(bd=FULL)) is None and _variance_verdict("xx", gt) is None

    # (h) EMPTY-modal suppression: an all-empty group (attachment/policy nodes -- no motif membership) -> None,
    # NOT a spurious "empty twin". But a node EMPTY against a NON-empty modal is a real divergence -> Fork-Shadow.
    m10h = (_variance_verdict("bd", _grp(bd=frozenset(), cot=frozenset(), inf=frozenset())) is None
            and _variance_verdict("inf", _grp(bd=FULL, cot=FULL, inf=frozenset()))["kind"] == "Fork-Shadow"
            and _variance_verdict("bd", _grp(bd=FULL, cot=FULL, inf=frozenset()))["kind"] == "Canonical")

    # (i) v2 ADVISORY-CONDITIONAL disposition (CTO 013249Z render-honesty): a v2 template with <disposition>
    # renders the disposition-NEUTRAL 'advisory' suffix for an UNGROUNDED dim (allowed_facets=[]) and '(debt)'
    # ONLY for a GROUNDED dim (allowed_facets populated) -- read from the catalog map, never hardcoded. This is
    # the "cot must not say (debt)" fix: firm is advisory today, so a firm Fork-Shadow is a candidate string.
    ph2 = {"Fork-Shadow": "divergent fork-shadow of <of_name> <disposition>"}
    disp = {"advisory": "(candidate -- advisory, pending adjudication)", "grounded": "(debt)"}
    fk = _variance_verdict("inf", gi)   # Fork-Shadow of opal-data-bd
    m10i = (variance_prose(fk, ph2, disp, {"firm": {"allowed_facets": []}})
            == "divergent fork-shadow of opal-data-bd (candidate -- advisory, pending adjudication)"
            and variance_prose(fk, ph2, disp, {"firm": {"allowed_facets": ["memory_size"]}})
            == "divergent fork-shadow of opal-data-bd (debt)"
            and "-- no canonical majority (candidate -- advisory"
            in variance_prose(nb, ph2, disp, {"firm": {"allowed_facets": []}}))

    # (j) ALIAS-FIX end-to-end via _compute_variances: 3-way grouping (the @c2a0cd66b fix) + the OVER-MERGE
    # GUARD (CTO arch-gate cond.2). All nodes share ONE identical membership so GROUPING (not structure) is
    # what is exercised. Real ARNs so the guard's real-ARN test engages.
    def _n(nm):   # (arn, node) -- a real-ARN LAMBDA node named nm
        return f"arn:aws:lambda:us-east-1:0:function:{nm}", {"name": nm, "node_type": "LAMBDA"}

    def _arn(nm):
        return f"arn:aws:lambda:us-east-1:0:function:{nm}"

    # (j1) THE FIX: bd-49f-y groups 3-way with cot-y/inf-y (no bare bd-y) -> all three verdict, bd=Canonical.
    n1 = dict([_n("bd-49f-y"), _n("cot-y"), _n("inf-y")])
    m1 = {a: {"c2": [("a-x", "")], "c3": []} for a in n1}
    r1 = _compute_variances(n1, m1, FV, FA)
    m10j1 = (r1[_arn("bd-49f-y")] is not None and r1[_arn("cot-y")] is not None
             and r1[_arn("inf-y")] is not None and r1[_arn("bd-49f-y")]["kind"] == "Canonical"
             and r1[_arn("cot-y")]["kind"] == "Twin" and r1[_arn("inf-y")]["kind"] == "Twin")
    # (j2) THE GUARD: bd-49f-z AND a bare bd-z both alias-normalize to {firm}-z -> ambiguous which is cot-z's
    # twin -> revert to value-only keys so they stay DISTINCT (never silently drop one). bd-z pairs with cot-z;
    # bd-49f-z is a singleton -> None. Nothing merged. (Grounded: this collision does NOT occur in the estate.)
    n2 = dict([_n("bd-49f-z"), _n("bd-z"), _n("cot-z")])
    m2 = {a: {"c2": [("a-x", "")], "c3": []} for a in n2}
    r2 = _compute_variances(n2, m2, FV, FA)
    m10j2 = (r2[_arn("bd-49f-z")] is None                       # kept apart -- NOT merged into the group
             and r2[_arn("bd-z")] is not None and r2[_arn("cot-z")] is not None)  # the genuine {firm}-z pair survives
    m10j = m10j1 and m10j2

    m10 = m10a and m10b and m10c and m10d and m10e and m10f and m10g and m10h and m10i and m10j
    ok &= m10
    print(f"  M10 C3/Twin variance (posn-key+alias={m10a}, twin={m10b}, fork-inf={m10c}, "
          f"fork-BD[modal-ref-detects]={m10d}, no-majority={m10e}, prose-nonfork={m10f}, "
          f"singleton->none={m10g}, empty-modal-suppressed={m10h}, v2-advisory-disposition={m10i}, "
          f"alias-3way+overmerge-guard={m10j}): {'PASS' if m10 else 'FAIL'}")

    print(f"=== self-test: {'PASS' if ok else 'FAIL'} (10/10) ===" if ok else "=== self-test: FAIL ===")
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
