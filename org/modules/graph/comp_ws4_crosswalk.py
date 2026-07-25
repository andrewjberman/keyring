"""
NFRA_TOOLUNIFY WS-4 -- the SOURCE<->DEPLOYED crosswalk for the four shared entities
(LAMBDA, S3_ARTIFACT/S3Key, COMPONENT/Component, ENDPOINT/Endpoint).

SOURCE plane = .comp-graph/graph.json (local working-tree scan, trace_graph.py schema, cli.py-backed).
DEPLOYED plane = kuzu marker-head canonical (Nessie-Iceberg-backed, comp-kuzu / comp_marker_read.py).

VINTAGE SEMANTICS -- declared explicitly, per WS-4's currency constraint (CANON2 triage):
  SOURCE is a self-healing local cache: source_sha = sha256(bytes)[:12] of the file at index time
    (NOT a git blob hash -- no LOCAL<->COMMITTED drift capability). A SHA-drift on read triggers a
    full local rebuild. It carries no independent currency signal beyond "was this file re-scanned."
  DEPLOYED is the kuzu marker-head projection off the Nessie lakehouse: built via a scheduled full
    re-derive (02:00Z) plus an event-driven CloudTrail incremental; its own provenance header states
    BEHIND/current explicitly (comp_marker_read.load_marker_head_graph, auto-refresh on HEAD-advance).
  A join across these two planes compares two INDEPENDENTLY-vintage artifacts. MATCHED means "both
  sides currently believe this entity exists under this id" -- not same-instant truth. ABSENT means
  "not found under this id, this run" -- a currency/coverage finding, never asserted as permanent
  non-existence (NEVER-rule #1 discipline).

Every join function returns a JoinResult:
  MATCHED    -- source id resolves to exactly one deployed id, found present this run
  ABSENT     -- resolves to exactly one candidate deployed id, not present on deployed side this run
  UNRESOLVED -- the join is genuinely ambiguous, or a required attribution signal is missing --
                never guessed, never silently defaulted (mirrors extract_gold_compute.py's own
                coverage.unresolved precedent for the same S3 firm-bucket problem)
  OUT_OF_SCOPE -- the source node does not qualify as an instance of this join at all (e.g. an
                  ENDPOINT node whose extractor swept in a co-located non-fetch utility function --
                  this is NOT a missing join, the source classification itself was over-broad)

M1 TOTALITY (adapter-mutant-spec discipline, fa8a9533ec): every one of the 4 entity types is handled
by an explicit branch in `join`; an unrecognized type raises, never falls through to a default.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_WORKSPACE_ROOT = _HERE.parent.parent.parent
_TOOLS_DIR = _WORKSPACE_ROOT / ".tools"
sys.path.insert(0, str(_TOOLS_DIR))


class Verdict(Enum):
    MATCHED = "MATCHED"
    ABSENT = "ABSENT"
    UNRESOLVED = "UNRESOLVED"
    OUT_OF_SCOPE = "OUT_OF_SCOPE"


@dataclass(frozen=True)
class JoinResult:
    verdict: Verdict
    source_id: str
    deployed_id: str | None
    reason: str


ENTITY_TYPES = ("LAMBDA", "S3_ARTIFACT", "COMPONENT", "ENDPOINT")

# Firm-directory -> deployed-bucket attribution for S3_ARTIFACT join. Confirmed live for the two
# firms sampled this pass (black_diamond, inf); 'assets'/'mdpf' are the repo's own two other
# data/<firm>/ trees and are NOT independently bucket-confirmed here -- an unmapped firm segment
# resolves UNRESOLVED, never guessed (same discipline extract_gold_compute.py already applies).
FIRM_BUCKET_MAP = {
    "black_diamond": "opal-data-bd",
    "inf": "opal-data-inf",
}


def _normalize_lambda_label(label: str) -> str:
    return re.sub(r"[-_]", "", label).lower()


def join_lambda(source_label: str, live_or_registry_names: set[str]) -> JoinResult:
    """WS-4 LAMBDA join: label-normalized (strip -/_, lowercase) match against the union of
    {live Lambda function names, lambda-source-map.json registry keys}. Fully pre-characterized by
    A_lambda_enumeration.json (333 source nodes: 208 canonical / 19 alias-excess / 82 phantom / 24
    residual) -- this function implements only the canonical MATCHED/ABSENT axis; alias/phantom/
    residual classification is a source-side census concern, not this join's job."""
    source_id = "lambda:%s" % source_label
    norm = _normalize_lambda_label(source_label)
    normalized_targets = {_normalize_lambda_label(n): n for n in live_or_registry_names}
    hit = normalized_targets.get(norm)
    if hit is not None:
        return JoinResult(Verdict.MATCHED, source_id, hit, "label-normalized match")
    return JoinResult(
        Verdict.ABSENT, source_id, None,
        "no live/registry name normalizes to '%s'" % norm,
    )


def join_component(source_id: str) -> JoinResult:
    """WS-4 COMPONENT join: LITERAL id identity. Both planes independently key a file-grain
    component node as 'component:<repo-relative-path>' (deployed props carry {"coarse": true,
    "path": ...}, confirming this IS the coarse anchor, not the finer ReactComponent symbol-grain
    decomposition -- ReactComponent nodes carry an explicit coarseKey back-reference to this same
    id and are OUT OF SCOPE for this join, a different grain source does not model). Exercised at
    full population 2026-07-25: 22/24 (91.7%) match; the 2 misses are confirmed NOT source
    staleness (both files live in git well before today) -- a deployed-side coverage gap, cause
    not diagnosed further by this module."""
    if not source_id.startswith("component:"):
        return JoinResult(Verdict.OUT_OF_SCOPE, source_id, None, "not a component: id")
    return JoinResult(Verdict.MATCHED, source_id, source_id, "literal id identity (unverified until queried)")


_URL_LIKE = re.compile(r"^/")


def join_endpoint(source_id: str, urls: list[str]) -> JoinResult:
    """WS-4 ENDPOINT join. Source-side extractor (extract_api.py:134-141) creates an ENDPOINT node
    for EVERY exported function in portal/src/api/endpoints/*.ts, with no guard on whether a fetch
    URL was actually found in its body -- confirmed at source, not inferred. Exercised at full
    population 2026-07-25 (138 source nodes): only 83/138 (60.1%) match a deployed id; of the 55
    misses, 33 carry empty urls[] and 12 carry only non-path template-literal false-positive
    matches (both OUT_OF_SCOPE -- the source classification itself over-swept, this was never a
    real endpoint), and 10 carry a genuine '/'-prefixed fetch URL yet are still ABSENT on deployed
    side -- a real coverage/currency gap, not a pollution artifact. The predicate below is the
    OUT_OF_SCOPE filter; a source id that passes it still needs the deployed-side presence check
    (query_deployed) to land MATCHED vs ABSENT."""
    if not any(_URL_LIKE.match(u) for u in urls):
        return JoinResult(
            Verdict.OUT_OF_SCOPE, source_id, None,
            "no '/'-prefixed fetch URL in metadata.urls -- extractor swept a non-fetch export",
        )
    return JoinResult(Verdict.MATCHED, source_id, source_id, "literal id identity (unverified until queried)")


def firm_for_gold_script_path(file_path: str) -> str | None:
    parts = file_path.split("/")
    if len(parts) >= 2 and parts[0] == "data":
        return parts[1]
    return None


def join_s3_artifact(source_id: str, incident_gold_script_file_paths: list[str]) -> JoinResult:
    """WS-4 S3_ARTIFACT join. Source ids are bucket-AGNOSTIC ('s3:<key>'); deployed S3Key ids are
    bucket-QUALIFIED ('<bucket>/<key>', confirmed via live sample: node_id='opal-data-inf/bronze/
    orion-api/*/assets.csv'). The bucket is attributed via the firm segment of the GOLD_SCRIPT
    node(s) connected to this S3_ARTIFACT by a READS_S3/WRITES_S3 edge (data/<firm>/scripts/...),
    mirroring extract_gold_compute.py's own documented 'Per-edge firm-bucket resolution;
    genuinely-ambiguous targets are surfaced in coverage.unresolved' convention -- NOT reinvented,
    reused. A source key touched by GOLD_SCRIPTs from more than one firm, or from a firm not yet in
    FIRM_BUCKET_MAP, is UNRESOLVED -- never guessed."""
    if not source_id.startswith("s3:"):
        return JoinResult(Verdict.OUT_OF_SCOPE, source_id, None, "not an s3: id")
    key = source_id[len("s3:"):]
    firms = {firm_for_gold_script_path(fp) for fp in incident_gold_script_file_paths}
    firms.discard(None)
    if len(firms) == 0:
        return JoinResult(Verdict.UNRESOLVED, source_id, None, "no incident GOLD_SCRIPT edge to attribute a firm")
    if len(firms) > 1:
        return JoinResult(
            Verdict.UNRESOLVED, source_id, None,
            "ambiguous firm attribution: %s" % sorted(firms),
        )
    firm = next(iter(firms))
    bucket = FIRM_BUCKET_MAP.get(firm)
    if bucket is None:
        return JoinResult(
            Verdict.UNRESOLVED, source_id, None,
            "firm '%s' has no confirmed bucket in FIRM_BUCKET_MAP" % firm,
        )
    deployed_id = "%s/%s" % (bucket, key)
    return JoinResult(Verdict.MATCHED, source_id, deployed_id, "firm-attributed bucket qualification")


def join(entity_type: str, **kwargs) -> JoinResult:
    """The M1 totality dispatcher -- every ENTITY_TYPES member is an explicit branch; an
    unrecognized type raises rather than defaulting through (adapter-mutant-spec discipline)."""
    if entity_type == "LAMBDA":
        return join_lambda(kwargs["source_label"], kwargs["live_or_registry_names"])
    if entity_type == "COMPONENT":
        return join_component(kwargs["source_id"])
    if entity_type == "ENDPOINT":
        return join_endpoint(kwargs["source_id"], kwargs["urls"])
    if entity_type == "S3_ARTIFACT":
        return join_s3_artifact(kwargs["source_id"], kwargs["incident_gold_script_file_paths"])
    raise ValueError("unhandled entity_type %r -- WS-4 covers exactly %s" % (entity_type, ENTITY_TYPES))


# ---------------------------------------------------------------------------
# Live-plane query helpers (network/subprocess boundary -- kept separate from the pure join logic
# above so the join functions themselves are unit-testable with zero live dependency).
# ---------------------------------------------------------------------------

def _git_bash() -> str:
    from git_bash_resolver import git_bash  # noqa: WPS433 -- deliberate: only needed on this path
    bash = git_bash()
    if not bash:
        raise RuntimeError("no Git Bash found; refusing to fall back to bare 'bash' (WSL-stub trap)")
    return bash


def query_deployed_ids(cypher: str, timeout: int = 180) -> list[dict]:
    """Run a Cypher query against the deployed plane via comp-kuzu --json. Raises loudly on a
    non-JSON response rather than returning an empty list (a silent empty list here would be
    indistinguishable from a real zero-result query -- the exact class this module's own docstring
    warns against for ABSENT vs a broken retrieval)."""
    bash = _git_bash()
    r = subprocess.run(
        [bash, str(_TOOLS_DIR / "comp-kuzu"), "--json", cypher],
        capture_output=True, text=True, timeout=timeout, cwd=str(_WORKSPACE_ROOT),
    )
    out = r.stdout
    if "[" not in out:
        raise RuntimeError(
            "comp-kuzu produced no JSON array (rc=%s): stdout=%r stderr=%r"
            % (r.returncode, out[:500], r.stderr[:500])
        )
    return json.loads(out[out.index("["):])


def query_deployed_ids_present(ids: list[str], timeout: int = 180) -> set[str]:
    if not ids:
        return set()
    quoted = ",".join("'%s'" % i.replace("\\", "\\\\").replace("'", "\\'") for i in ids)
    rows = query_deployed_ids(
        "MATCH (n:CloudNode) WHERE n.node_id IN [%s] RETURN n.node_id" % quoted, timeout=timeout
    )
    return {r["n.node_id"] for r in rows}


def load_source_graph() -> dict:
    graph_path = _WORKSPACE_ROOT / ".comp-graph" / "graph.json"
    with open(graph_path, encoding="utf-8") as f:
        return json.load(f)


def resolve_join(entity_type: str, result: JoinResult, timeout: int = 180) -> JoinResult:
    """Take a JoinResult whose verdict is provisionally MATCHED (candidate deployed id computed,
    not yet checked for live presence) and resolve it against the deployed plane: MATCHED stands
    only if the candidate id is actually present this run; otherwise it downgrades to ABSENT.
    UNRESOLVED/OUT_OF_SCOPE pass through unchanged -- there is nothing to query for those."""
    if result.verdict is not Verdict.MATCHED or result.deployed_id is None:
        return result
    present = query_deployed_ids_present([result.deployed_id], timeout=timeout)
    if result.deployed_id in present:
        return result
    return JoinResult(
        Verdict.ABSENT, result.source_id, result.deployed_id,
        "candidate id computed (%s) but not present on deployed side this run" % result.reason,
    )
