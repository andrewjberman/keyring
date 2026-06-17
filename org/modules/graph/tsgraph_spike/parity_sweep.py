"""
NFRA_TSGRAPH.P1 Leg C -- comp-types parity recall sweep (broaden the probe before cutover).

For each sample type: compare the regex `comp-types index` consumers vs the semantic REFERENCES_TYPE
consumer set (from the local extractor graph -- same content that ingests to Nessie->Kuzu).

RECALL  = does the semantic set cover every regex IMPORT + TYPE-ANNOTATION file (the high-confidence
          true positives)? A miss = a recall regression that blocks cutover.
PRECISION (illustrative) = the regex's reference/default-fallback noise files that semantic correctly
          EXCLUDES (the substring false-positives).

Run: python parity_sweep.py   (needs .tools on PATH)
"""
from __future__ import annotations

import json
import os
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
GRAPH = json.load(open(os.path.join(HERE, "out", "portal_full.graph.json"), encoding="utf-8"))

nodes_by_id = {n["id"]: n for n in GRAPH["nodes"]}
ref_by_type: dict[str, set[str]] = {}
for e in GRAPH["edges"]:
    if e["label"] != "REFERENCES_TYPE":
        continue
    t = nodes_by_id.get(e["dst"])
    if not t:
        continue
    ref_by_type.setdefault(t["attrs"].get("name"), set()).add(e["src"].replace("module:", ""))

TYPEDECLS = {n["attrs"].get("name") for n in GRAPH["nodes"] if n["label"] == "TypeDecl"}
SAMPLE = [t for t in [
    "BenchmarkModelData", "ModelPortfolioBenchmarksResponse", "BenchmarkPeriodReturn",
    "ModelPortfolioData", "BenchmarkHeatmapProps", "ModelPortfolioPeriodReturn",
] if t in TYPEDECLS]

TRUE_CATS = {"import", "type-annotation"}
NOISE_CATS = {"reference", "default-fallback"}


def regex_consumers(t: str) -> tuple[set[str], set[str]]:
    # read a pre-captured `comp-types index <t>` output (out/regex_<t>.txt) -- the bash-launcher
    # comp-types isn't resolvable from a Windows python subprocess, so we capture via Bash first.
    p = os.path.join(HERE, "out", f"regex_{t}.txt")
    out = open(p, encoding="utf-8", errors="replace").read() if os.path.exists(p) else ""
    true_f, noise_f = set(), set()
    for line in out.splitlines():
        low = line.strip()
        if not (low.startswith("portal\\src") or low.startswith("portal/src")):
            continue
        toks = low.split()
        f = toks[0].replace("\\", "/")
        cat = next((c for c in (TRUE_CATS | NOISE_CATS) if c in toks), None)
        if cat in TRUE_CATS:
            true_f.add(f)
        elif cat in NOISE_CATS:
            noise_f.add(f)
    return true_f, noise_f


print(f"{'TYPE':<34} {'regex-true':>10} {'sem':>5} {'RECALL':>8} {'noise-killed':>12}")
print("-" * 76)
all_pass = True
for t in SAMPLE:
    rtrue, rnoise = regex_consumers(t)
    sem = ref_by_type.get(t, set())
    # recall: every regex true-positive file is in the semantic set
    missed = rtrue - sem
    recall = "PASS" if not missed else f"MISS {len(missed)}"
    if missed:
        all_pass = False
    noise_killed = len(rnoise - sem)  # regex noise files the semantic set excludes
    print(f"{t:<34} {len(rtrue):>10} {len(sem):>5} {recall:>8} {noise_killed:>12}")
    if missed:
        for m in missed:
            print(f"    MISSED true-positive: {m}")

print("-" * 76)
print(f"SWEEP VERDICT: {'RECALL PARITY across all sampled types (semantic covers every regex true-positive)' if all_pass else 'RECALL GAP on some type -- see MISSED above'}")
print(f"(precision: semantic excludes the regex reference/default-fallback substring noise -- noise-killed column)")
