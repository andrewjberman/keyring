#!/usr/bin/env python3
"""~B infra cross-stratum stitchers PRODUCER (NFRA_GRAPHUNI.P1-B).
Emits producers/graphuni/stitchers.json for ~D's ingest_graphuni_producers() fold.

S1 EC2-RUNS->GoldScript (the keystone): gold-runner EC2 -> ~D's pipeline:<firm>:gold:<script>
    nodes (134, ~C-ratified f23932383), by firm from EC2_MANIFEST bindings.
S3 LAMBDA-READS_S3/WRITES_S3->S3Key: lambda IO from the TraceGraph, joined against ~A's
    169 S3Key node-ids (key-suffix match -> ~A's bucket attribution; firm-disambiguate
    collisions). Unmatched (lambda-only keys not yet in ~A's Phase-A set) = deferred to Phase-B.
Read-only; writes only the producer JSON.
"""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

_WS = Path("C:/Users/AndrewBerman/Desktop/ajb_workspace")
if str(_WS) not in sys.path:
    sys.path.insert(0, str(_WS))
from org.modules.graph import trace_graph as T  # noqa: E402

# EC2 instance-id -> (name, firm, role) for the GOLD runners (EC2_MANIFEST.json grounded).
# RUNS edges target each runner's firm GoldScripts. QA runners mirror prod (same scripts).
GOLD_RUNNERS = {
    "i-0ed5afded2ebd4ed4": ("inf-gold-layer-runner", "inf", "gold-layer"),
    "i-04373615f03fbf9a9": ("inf-gold-qa-runner", "inf", "gold-qa"),
    "i-01003b035d2988dfb": ("bd-gold-layer-runner", "bd", "gold-layer"),
    "i-0090b823a4a0997e3": ("bd-gold-qa-runner", "bd", "gold-qa"),
    "i-02448edb624a7a7cf": ("mdpf-daily-runner", "mdpf", "gold-daily"),
}
EC2_ARN = "arn:aws:ec2:us-east-1:313476888478:instance/{}"

FIRM_BUCKET = {"inf": "opal-data-inf", "bd": "opal-data-bd", "cot": "opal-data-cot",
               "mdpf": "opal-data-mdpf"}


def lam_firm(name: str) -> str | None:
    n = name.lower()
    for tok, firm in (("inf", "inf"), ("cot", "cot"), ("mdpf", "mdpf"),
                      ("49f", "bd"), ("bd", "bd"), ("schwab", "bd")):
        if f"-{tok}-" in n or n.startswith(f"opal-{tok}-") or n.startswith(f"{tok}-"):
            return firm
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--scratch", required=True)
    args = ap.parse_args()
    scr = Path(args.scratch)

    gold_ids = set(scr.joinpath("d_goldscript_ids.txt").read_text().split())
    by_firm: dict[str, list[str]] = {}
    for gid in gold_ids:
        firm = gid.split(":")[1]
        by_firm.setdefault(firm, []).append(gid)

    a_ids = [x for x in scr.joinpath("a_s3key_ids.txt").read_text().splitlines() if x]
    # key-suffix -> [full <bucket>/<key> ids]
    key_to_ids: dict[str, list[str]] = {}
    for aid in a_ids:
        slash = aid.find("/")
        key = aid[slash + 1:] if slash > 0 else aid
        key_to_ids.setdefault(key, []).append(aid)

    edges, nodes = [], []

    # ---- S1: EC2 -RUNS-> GoldScript (the keystone) ----
    runs_n = 0
    for iid, (name, firm, role) in GOLD_RUNNERS.items():
        for gid in sorted(by_firm.get(firm, [])):
            edges.append({"source": EC2_ARN.format(iid), "target": gid,
                          "edge_type": "RUNS", "level": "ec2",
                          "stratum_pair": "resource->compute", "producer_by_pair": "~B"})
            runs_n += 1

    # ---- S3: LAMBDA -READS_S3/WRITES_S3-> S3Key (join vs ~A ids) ----
    trace = T.build_graph(_WS)
    s3_match, s3_defer = 0, 0
    deferred_keys = set()
    seen = set()
    for e in trace.edges:
        if e.edge_type not in ("READS_S3", "WRITES_S3"):
            continue
        st, tt = trace.nodes.get(e.source), trace.nodes.get(e.target)
        if not st or not tt:
            continue
        # READS_S3 stored S3->LAMBDA (reversed); WRITES_S3 LAMBDA->S3
        if e.edge_type == "WRITES_S3" and st.node_type == "LAMBDA" and tt.node_type == "S3_ARTIFACT":
            lam_id, key_id = e.source, e.target
        elif e.edge_type == "READS_S3" and st.node_type == "S3_ARTIFACT" and tt.node_type == "LAMBDA":
            lam_id, key_id = e.target, e.source
        elif e.edge_type == "READS_S3" and st.node_type == "LAMBDA" and tt.node_type == "S3_ARTIFACT":
            lam_id, key_id = e.source, e.target
        else:
            continue
        lam = lam_id.split(":", 1)[1] if lam_id.startswith("lambda:") else lam_id
        key = key_id[3:] if key_id.startswith("s3:") else key_id
        key = key.lstrip("/")
        cands = key_to_ids.get(key, [])
        target = None
        if len(cands) == 1:
            target = cands[0]
        elif len(cands) > 1:
            firm = lam_firm(lam)
            b = FIRM_BUCKET.get(firm) if firm else None
            target = next((c for c in cands if b and c.startswith(b + "/")), cands[0])
        if target is None:
            s3_defer += 1
            deferred_keys.add(key)
            continue
        sig = (lam, target, e.edge_type)
        if sig in seen:
            continue
        seen.add(sig)
        edges.append({"source": f"lambda:{lam}", "target": target, "edge_type": e.edge_type,
                      "level": "prefix" if ("*" in target or target.endswith("/")) else "object",
                      "stratum_pair": "resource->object", "producer_by_pair": "~B"})
        s3_match += 1

    producer = {
        "producer": "graphuni-infra-stitchers",
        "lane": "0.8.0_AE_CloudComp~B",
        "phase": "NFRA_GRAPHUNI.P1-B infra+cross-stratum (S1 RUNS keystone + S3 lambda-IO converged-vs-~A)",
        "id_conventions": {
            "RUNS_target": "pipeline:<firm>:gold:<script> (~D GoldScript, ~C-ratified f23932383)",
            "S3Key_target": "<bucket>/<key> (~A storage_s3keys.json node-id)",
        },
        "nodes": nodes,
        "edges": edges,
        "coverage": {
            "S1_runs_edges": runs_n,
            "S1_runners": {n: f for _, (n, f, _r) in [(k, v) for k, v in GOLD_RUNNERS.items()]},
            "S3_converged_edges": s3_match,
            "S3_deferred_lambda_only": s3_defer,
            "total_edges": len(edges),
        },
        "_deferred_keys_sample": sorted(deferred_keys)[:30],
    }
    out = {k: v for k, v in producer.items() if not k.startswith("_")}
    Path(args.out).write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"S1 RUNS edges: {runs_n} (inf x2 + bd x2 + mdpf -> firm GoldScripts)")
    print(f"  by firm: inf={len(by_firm.get('inf',[]))} bd={len(by_firm.get('bd',[]))} mdpf={len(by_firm.get('mdpf',[]))}")
    print(f"S3 lambda-IO: converged-vs-~A={s3_match}  deferred(lambda-only, not in ~A Phase-A)={s3_defer}")
    print(f"  deferred key sample: {sorted(deferred_keys)[:12]}")
    print(f"total edges: {len(edges)}  wrote: {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
