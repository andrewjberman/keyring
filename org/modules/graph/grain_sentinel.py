"""grain_sentinel — structural identity/grain invariant for compiler-derived graphs.

NFRA_GRAPHS D5 / comp-aws AC-GRAIN (CVO-owned cert-integration, 2026-06-11).

WHY: AC4's `untyped == 0` bar PASSED 23,664 phantom S3_BUCKET nodes that were
S3 OBJECT KEYS mis-typed as buckets (e.g. `arn:aws:s3:::opal-data-inf/gold/x.json`
minted as a "bucket"). They were validly TYPED -> the untyped bar cannot see
WRONG-GRAIN. This sentinel makes wrong-grain a structural FAIL, enforced on every
run (not fixed-once). Reusable across comp-aws derive + comp-graph stitch derive.

Two bars (both hard-fail):
  AC-GRAIN.1  per-class IDENTITY-FORMAT invariant. Each class declares an id-format
              rule; a violation FAILS the run. Anchor invariant = S3_BUCKET.node_id
              MUST NOT contain '/' (an S3 bucket NAME structurally cannot contain
              '/' per AWS naming — a '/' is an object-key-as-bucket = wrong grain).
  AC-GRAIN.2  per-class MAGNITUDE band. Live per-class node count must fall within
              [LO, HI]x of the certified baseline; a 20x spike (wrong-grain
              explosion) or a collapse (accidental dedup) FAILS the run.

Calibrated against the certified-clean unioned stitch graph (kuzu_stitch_db,
2026-06-11): in that baseline S3_BUCKET=34 nodes, 0 with '/'; the phantom
nessie graph had 23,690 S3_BUCKET, 23,656 with '/'. The sentinel FAILs the
latter and PASSes the former.
"""
from __future__ import annotations

from dataclasses import dataclass, field


# AC-GRAIN.1 — per-class identity-format invariants.
# Each entry: node_type -> (predicate(node_id)->bool ok, human-readable rule).
# Only classes whose id-format is STRUCTURALLY known are asserted here; the set is
# deliberately extended conservatively (a wrong invariant would false-fail real data).
# S3_BUCKET no-'/' is the anchor: AWS bucket names cannot contain '/', so a '/' in an
# S3_BUCKET node_id is definitionally an object-key-as-bucket (the 23,664 incident).
IDENTITY_FORMAT_INVARIANTS: dict[str, tuple] = {
    "S3_BUCKET": (lambda nid: "/" not in _bucket_name(nid),
                  "S3_BUCKET node_id bucket-name segment must not contain '/' "
                  "(a '/' = object-key-as-bucket, wrong grain)"),
    "LAMBDA": (lambda nid: "/" not in nid,
               "LAMBDA node_id is a bare function name — no '/'"),
    "SQS_QUEUE": (lambda nid: "/" not in _arn_resource(nid),
                  "SQS_QUEUE resource segment is a bare queue name — no '/'"),
    "SNS_TOPIC": (lambda nid: "/" not in _arn_resource(nid),
                  "SNS_TOPIC resource segment is a bare topic name — no '/'"),
}


def _bucket_name(node_id: str) -> str:
    """Return the bucket-name portion of an S3 node_id (ARN or bare). For a bucket
    ARN `arn:aws:s3:::name` -> `name`; for an object ARN `arn:aws:s3:::name/key`
    the returned segment retains the '/' so the invariant trips."""
    nid = node_id or ""
    if nid.startswith("arn:aws:s3:::"):
        return nid[len("arn:aws:s3:::"):]
    return nid


def _arn_resource(node_id: str) -> str:
    """Return the trailing resource segment of an ARN (after the last ':'), else the id."""
    nid = node_id or ""
    return nid.rsplit(":", 1)[-1] if nid.startswith("arn:") else nid


# AC-GRAIN.2 — magnitude band (multiplicative, vs certified baseline).
MAGNITUDE_LO = 0.4
MAGNITUDE_HI = 2.5


def _nid(n) -> str:
    """Resolve a node's identity string across the comp-aws (`arn`) and comp-graph
    (`node_id`) node shapes."""
    return n.get("node_id") or n.get("id") or n.get("arn") or n.get("name") or ""


@dataclass
class GrainViolation:
    bar: str          # "AC-GRAIN.1" | "AC-GRAIN.2"
    node_type: str
    detail: str
    samples: list = field(default_factory=list)


@dataclass
class GrainResult:
    passed: bool
    violations: list  # list[GrainViolation]

    def render(self) -> str:
        if self.passed:
            return "GRAIN-SENTINEL: PASS (0 identity-format + 0 magnitude violations)"
        out = [f"GRAIN-SENTINEL: FAIL ({len(self.violations)} violation group(s))"]
        for v in self.violations:
            out.append(f"  [{v.bar}] {v.node_type}: {v.detail}")
            for s in v.samples[:3]:
                out.append(f"      e.g. {s}")
        return "\n".join(out)


def check_identity_format(nodes) -> list:
    """AC-GRAIN.1: each node's id must satisfy its class id-format invariant."""
    violations = []
    by_type: dict[str, list] = {}
    for n in nodes:
        by_type.setdefault(n.get("node_type") or n.get("type") or "", []).append(n)
    for ntype, (ok, rule) in IDENTITY_FORMAT_INVARIANTS.items():
        bad = [n for n in by_type.get(ntype, []) if not ok(_nid(n))]
        if bad:
            violations.append(GrainViolation(
                bar="AC-GRAIN.1", node_type=ntype,
                detail=f"{len(bad)}/{len(by_type.get(ntype, []))} nodes violate: {rule}",
                samples=[_nid(n) for n in bad[:3]]))
    return violations


def check_magnitude(nodes, baseline: dict, lo: float = MAGNITUDE_LO,
                    hi: float = MAGNITUDE_HI) -> list:
    """AC-GRAIN.2: per-class live count within [lo,hi]x of baseline count.

    baseline = {node_type: certified_count}. Classes absent from baseline are
    skipped (new class — record it into the next baseline rather than fail)."""
    violations = []
    live: dict[str, int] = {}
    for n in nodes:
        t = n.get("node_type") or n.get("type") or ""
        live[t] = live.get(t, 0) + 1
    for ntype, base in baseline.items():
        if base <= 0:
            continue
        cur = live.get(ntype, 0)
        ratio = cur / base
        if ratio < lo or ratio > hi:
            violations.append(GrainViolation(
                bar="AC-GRAIN.2", node_type=ntype,
                detail=f"count {cur} vs baseline {base} = {ratio:.2f}x "
                       f"(outside [{lo}, {hi}]x band)"))
    return violations


def run_grain_sentinel(nodes, baseline: dict | None = None) -> GrainResult:
    """Run both grain bars. Returns GrainResult(passed, violations).

    nodes: iterable of dicts with node_type/node_id (or type/id).
    baseline: {node_type: count} for AC-GRAIN.2; omit to run AC-GRAIN.1 only."""
    nodes = list(nodes)
    violations = check_identity_format(nodes)
    if baseline:
        violations += check_magnitude(nodes, baseline)
    return GrainResult(passed=(len(violations) == 0), violations=violations)
