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


def derive_summary(arn: str, node: dict, out_edges: list, in_edges: list) -> SummaryDoc:
    """Synthesize a resource's functional summary from the graph. The BM25 document is the
    PURPOSE vocabulary (type + layer + edge neighborhood); the resource's OWN name is kept in
    the prose but NOT in the tokens (the corpus-collapse control)."""
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

    tokens = base_tokens + purpose_tokens          # name intentionally EXCLUDED
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

    return SummaryDoc(arn=arn, node_type=node_type, name=name, tokens=tokens, prose=prose,
                      thin=thin, held=held, n_purpose=n_purpose)


def build_corpus() -> dict[str, SummaryDoc]:
    """Build the {arn -> SummaryDoc} derive-at-scan corpus from the live graph."""
    nodes, out_edges, in_edges = load_graph()
    corpus: dict[str, SummaryDoc] = {}
    for arn, node in nodes.items():
        corpus[arn] = derive_summary(arn, node, out_edges.get(arn, []), in_edges.get(arn, []))
    return corpus


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
    return {"total_arn_resources": total, "summarized": total - thin,
            "unknown_thin": thin, "held_marked": held,
            "note": f"scanned {total} ARN resources; {total - thin} with purpose summary; "
                    f"{thin} UNKNOWN-thin (no twin known); {held} hold-marked"}


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

    print(f"=== self-test: {'PASS' if ok else 'FAIL'} (4/4) ===" if ok else "=== self-test: FAIL ===")
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
    ap.add_argument("--samples", type=int, default=6, help="how many sample summaries to print under --build")
    ap.add_argument("--json", action="store_true", help="emit machine JSON")
    args = ap.parse_args(argv)

    if args.self_test:
        return self_test()

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
