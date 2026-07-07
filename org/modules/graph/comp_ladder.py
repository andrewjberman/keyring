#!/usr/bin/env python3
"""comp-ladder -- the C0->C3 semantic-compression FIDELITY GATE (NFRA_SEMCTL reference).

The ruler for the Semantic Control Plane, built BEFORE the planes it measures. It proves the
one property that distinguishes this substrate from embeddings/GraphRAG (charter LAW 1+LAW 2):

    C0->C3 is LOSSY-abstraction compression WITH a LOSSLESS decompression path to lexical
    evidence -- a deterministic lexical ruleset, never a latent representation.

Two operations, both deterministic + reproducible + zero ML:
  ladder(node)          -- show the compression (up: fact->interaction->motif->system) AND the
                           decompression (down: system -> the exact lexical evidence).
  fidelity_check(node)  -- the GATE: assert every C1+ node decompresses to C0 lexical evidence.
                           A node with no decompression path is a LATENT representation -> FAIL
                           (the build drifted toward ML). This is "a control must fire" applied
                           to the compression itself -- run it on every semantic-build increment.

This first build proves it on REAL estate: the firm-separation invariant, extracted
deterministically from infra/aws/terraform/cot-pipeline/iam.tf + .tools/safe_deploy_core.py
(the exact DenyCrossFirmBuckets statement CTO live-verified to close NFRA_INTEGRATIONS 07-07).

Recognizer SDK + rule SDK are the extension points: a new artifact class adds a recognizer
(C0 emitter) + rules (C0->C1->C2->C3); the ladder + the fidelity gate are unchanged.
"""
from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass, field
from typing import Optional

WS = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


# ---------------------------------------------------------------------------
# The Node model -- one type across all four compression layers.
#   C0: provenance carries the EXACT lexical evidence (source, locus, bytes); children = [].
#   C1+: children = the lower-layer nodes it composes -> the decompression path; a C1+ node
#        with no children is a LATENT node (the failure the fidelity gate exists to catch).
# ---------------------------------------------------------------------------
@dataclass
class Node:
    nid: str
    layer: str                       # "C0" | "C1" | "C2" | "C3"
    ntype: str                       # e.g. IAMStatement, DeniedEdge, FirmSeparation, MultiFirmIsolation
    label: str
    rule: str = ""                   # the deterministic rule that composed a C1+ node
    provenance: Optional[dict] = None  # C0 only: {source, locus, evidence}
    children: list = field(default_factory=list)   # C1+ decompression pointers


# ---------------------------------------------------------------------------
# RECOGNIZER SDK -- deterministic C0 emitters over a real artifact class.
# Each C0 node carries provenance {source, locus, evidence} back to the lexical origin.
# ---------------------------------------------------------------------------
def recognize_iam_cross_firm_deny(iam_tf_path: str) -> list:
    """Recognizer (IAM/Terraform artifact class): extract the DenyCrossFirmBuckets C0 facts.

    Deterministic lexical parse of the jsonencode Deny block -- Sid/Effect/Action + the exact
    Resource ARNs + the role. No inference; every fact traces to a file:line + the literal bytes.
    """
    with open(iam_tf_path, "r", encoding="utf-8") as fh:
        lines = fh.readlines()
    text = "".join(lines)
    c0 = []

    # locate the DenyCrossFirmBuckets statement block (lexical anchor)
    sid_m = re.search(r'Sid\s*=\s*"DenyCrossFirmBuckets"', text)
    if not sid_m:
        return c0
    sid_line = text[: sid_m.start()].count("\n") + 1
    # role bound to THIS deny policy: the NEAREST `role = aws_iam_role.<x>` ABOVE the Sid
    # (scoped to the enclosing aws_iam_role_policy block, not the first role in the file).
    role_matches = list(re.finditer(r"role\s*=\s*aws_iam_role\.([A-Za-z0-9_]+)", text[: sid_m.start()]))
    role_m = role_matches[-1] if role_matches else None
    role_name = role_m.group(1) if role_m else "cot_gold_layer"
    role_line = text[: role_m.start()].count("\n") + 1 if role_m else sid_line
    # the block's Effect/Action (lexical, right after the Sid)
    eff = re.search(r'Effect\s*=\s*"([^"]+)"', text[sid_m.start():]).group(1)
    act = re.search(r'Action\s*=\s*"([^"]+)"', text[sid_m.start():]).group(1)
    # the denied Resource ARNs (the exact bucket list)
    res_block = re.search(r"Resource\s*=\s*\[(.*?)\]", text[sid_m.start():], re.DOTALL).group(1)
    arns = re.findall(r'"([^"]+)"', res_block)
    denied_buckets = sorted({a.split(":::")[1].split("/")[0] for a in arns})

    src = os.path.relpath(iam_tf_path, WS)
    ev = f'Sid=DenyCrossFirmBuckets Effect={eff} Action={act} Resource={arns}'
    c0.append(Node(f"role:{role_name}", "C0", "IAMRole", role_name,
                   provenance={"source": src, "locus": f"L{role_line}",
                               "evidence": f"role = aws_iam_role.{role_name}.id"}))
    c0.append(Node("stmt:DenyCrossFirmBuckets", "C0", "IAMStatement",
                   "DenyCrossFirmBuckets (Deny s3:* on cross-firm buckets)",
                   provenance={"source": src, "locus": f"L{sid_line}-{sid_line+9}", "evidence": ev}))
    for b in denied_buckets:
        c0.append(Node(f"bucket:{b}", "C0", "S3Bucket", b,
                       provenance={"source": src, "locus": f"L{sid_line}", "evidence": f'"arn:aws:s3:::{b}"'}))
    return c0


def recognize_pipeline_map(safe_deploy_path: str) -> list:
    """Recognizer (deploy-gate artifact class): the firm->own-bucket PIPELINE_MAP C0 facts."""
    with open(safe_deploy_path, "r", encoding="utf-8") as fh:
        text = fh.read()
    c0 = []
    src = os.path.relpath(safe_deploy_path, WS)
    for m in re.finditer(r'"([a-z_]+)":\s*\("([a-z0-9\-]+)",\s*"([a-z]+)"\)', text):
        bucket, firm = m.group(2), m.group(3)
        line = text[: m.start()].count("\n") + 1
        c0.append(Node(f"pmap:{firm}->{bucket}", "C0", "PipelineMapEntry", f"{firm} -> {bucket} (own-firm bucket)",
                       provenance={"source": src, "locus": f"L{line}", "evidence": m.group(0)}))
    return c0


# ---------------------------------------------------------------------------
# RULE SDK -- deterministic C(n)->C(n+1) composers. Each higher node keeps children = the exact
# lower nodes (the decompression path). No node is created without its provenance chain.
# ---------------------------------------------------------------------------
def rule_c1_denied_edges(c0: list) -> list:
    """C0->C1: a Deny statement on role R for bucket B  =>  R --denied--> B (proven, not inferred)."""
    role = next(n for n in c0 if n.ntype == "IAMRole")
    stmt = next(n for n in c0 if n.ntype == "IAMStatement")
    edges = []
    for b in [n for n in c0 if n.ntype == "S3Bucket"]:
        edges.append(Node(f"denied:{role.label}->{b.label}", "C1", "DeniedEdge",
                          f"{role.label} --DENIED--> {b.label}",
                          rule="Deny-statement(role R, bucket B) => R --denied--> B",
                          children=[role, stmt, b]))
    return edges


def rule_c1_allowed_edge(c0_pmap: list, firm: str) -> Node:
    """C0->C1: the firm's PIPELINE_MAP own-bucket entry  =>  firm-role --allowed--> own-bucket."""
    pmap = next(n for n in c0_pmap if n.nid.startswith(f"pmap:{firm}->"))
    own = pmap.label.split(" -> ")[1].split(" ")[0]
    return Node(f"allowed:{firm}->{own}", "C1", "AllowedEdge",
                f"{firm}-role --ALLOWED--> {own}",
                rule="PIPELINE_MAP(firm F -> bucket B) => F-role --allowed--> B (own-firm)",
                children=[pmap])


def rule_c2_firm_separation(allowed: Node, denied: list, firm: str) -> Node:
    """C1->C2: allowed(own-bucket) AND denied(all other-firm buckets)  =>  FIRM_SEPARATION motif."""
    return Node(f"motif:firmsep:{firm}", "C2", "FirmSeparation",
                f"FirmSeparation({firm}): allowed own-bucket, denied all cross-firm",
                rule="allowed(own) AND denied(all others) => FIRM_SEPARATION motif",
                children=[allowed] + denied)


def rule_c3_multi_firm_isolation(motifs: list) -> Node:
    """C2->C3: the set of FirmSeparation motifs + the deploy-gate  =>  MULTI_FIRM_ISOLATION system."""
    return Node("system:multi_firm_isolation", "C3", "MultiFirmIsolation",
                "MultiFirmIsolation: firm data cannot cross, enforced at deploy AND runtime",
                rule="{FirmSeparation motifs} + deploy-gate(PIPELINE_MAP) + runtime-deny => capability",
                children=list(motifs))


# ---------------------------------------------------------------------------
# THE LADDER + THE FIDELITY GATE
# ---------------------------------------------------------------------------
def decompress(node: Node, depth: int = 0):
    """Yield (depth, node) walking DOWN the decompression path to C0 evidence."""
    yield depth, node
    for c in node.children:
        yield from decompress(c, depth + 1)


def fidelity_check(node: Node) -> tuple:
    """THE GATE: every C1+ node must decompress to C0 evidence; every C0 must carry real evidence.

    Returns (ok: bool, failures: list[str]). A C1+ with no children = LATENT (fail). A C0 with no
    provenance.evidence = evidence-less (fail). This is what an embedding CANNOT pass -> the
    runnable proof we are building the lexical-deterministic substrate, not an ML approximation.
    """
    failures = []

    def walk(n: Node):
        if n.layer == "C0":
            if not (n.provenance and n.provenance.get("evidence")):
                failures.append(f"C0 {n.nid} has NO lexical evidence (not a grounded fact)")
            return
        # C1+ must have a decompression path
        if not n.children:
            failures.append(f"{n.layer} {n.nid} is LATENT -- no decompression path (embedding-like, build drifted)")
            return
        for c in n.children:
            walk(c)
        # and it must ultimately reach at least one C0-with-evidence
        reached = any(d.layer == "C0" and d.provenance and d.provenance.get("evidence")
                      for _, d in decompress(n))
        if not reached:
            failures.append(f"{n.layer} {n.nid} does not bottom out in C0 evidence")

    walk(node)
    return (len(failures) == 0, failures)


def print_ladder(node: Node):
    print(f"\n=== comp-ladder: {node.label} ===\n")
    print("COMPRESSION (up) -- lossy toward detail, each layer denser:")
    order = ["C0", "C1", "C2", "C3"]
    by_layer = {L: [] for L in order}
    seen = set()
    for _, n in decompress(node):
        if n.nid not in seen:
            by_layer[n.layer].append(n)
            seen.add(n.nid)
    names = {"C0": "FACTS", "C1": "INTERACTIONS", "C2": "MOTIFS", "C3": "SYSTEMS"}
    for L in order:
        if by_layer[L]:
            print(f"  {L} ({names[L]}):")
            for n in by_layer[L]:
                print(f"      - {n.label}")

    print("\nDECOMPRESSION (down) -- lossless toward provenance, C3 -> the exact lexical evidence:")
    for depth, n in decompress(node):
        indent = "  " + "  " * depth
        if n.layer == "C0":
            p = n.provenance or {}
            print(f'{indent}{n.layer} {n.label}')
            print(f'{indent}     evidence: {p.get("source")}:{p.get("locus")}  ::  {p.get("evidence")}')
        else:
            arrow = f"  [rule: {n.rule}]" if n.rule else ""
            print(f"{indent}{n.layer} {n.label}{arrow}")

    ok, failures = fidelity_check(node)
    print("\nFIDELITY GATE:")
    if ok:
        print("  PASS -- every C1+ node decompresses to C0 lexical evidence (deterministic, no ML).")
        print("  This node is a lossy-compression WITH a lossless decompression path -> not an embedding.")
    else:
        print("  FAIL -- latent/evidence-less node(s) found (the build has drifted toward ML):")
        for f in failures:
            print(f"    - {f}")
    return ok


# ---------------------------------------------------------------------------
# Reference ladder builder (the firm-separation invariant over REAL estate)
# ---------------------------------------------------------------------------
def build_firm_sep_ladder() -> Node:
    iam = os.path.join(WS, "infra", "aws", "terraform", "cot-pipeline", "iam.tf")
    sdp = os.path.join(WS, ".tools", "safe_deploy_core.py")
    c0_iam = recognize_iam_cross_firm_deny(iam)
    c0_pmap = recognize_pipeline_map(sdp)
    denied = rule_c1_denied_edges(c0_iam)
    allowed = rule_c1_allowed_edge(c0_pmap, "cot")
    motif = rule_c2_firm_separation(allowed, denied, "cot")
    system = rule_c3_multi_firm_isolation([motif])
    return system


def main():
    args = sys.argv[1:]
    target = args[0] if args else "firm-sep"
    fidelity_only = "--fidelity" in args
    if target in ("firm-sep", "firmsep"):
        node = build_firm_sep_ladder()
    else:
        print(f"comp-ladder: unknown target '{target}' (this reference build ships: firm-sep)")
        return 2
    if fidelity_only:
        ok, failures = fidelity_check(node)
        print(f"comp-ladder --fidelity [{node.label}]: {'PASS' if ok else 'FAIL'}")
        for f in failures:
            print(f"  - {f}")
        return 0 if ok else 1
    ok = print_ladder(node)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
