#!/usr/bin/env python3
"""Doc-similarity scan on available workspace documents -> engine -> blinded harness.

Andrew-direct reset (via CTO~Z, 2026-07-20): "this should just be for doc similarity and scanning with the
documents available." So this is a REAL run on real documents (the workspace's own .md/.py/.yaml/.tf/.ts/.sh
across distinct subsystems), NOT a proxy for anything. FACTUAL property (informs the rule, not an excuse):
this corpus is technical prose = constrained vocabulary / little synonymy. ASYMMETRIC rule still stands:
semantic RECOVERS coherent bm25-missed pairs -> SHIP; semantic redundant -> INCONCLUSIVE, do NOT drop on
constrained vocab. bm25 clearing the blinded sheet = apparatus + baseline validation. STORAGE care: never
commit raw client-document text to git (N/A here -- corpus is repo's own files).

Run from the workspace root: python org/tier1_exec/3.0.0_SA_CVO/deliverables/content_prototype_run.py
Emits: the per-axis engine summary + recovery cross-tab + the semantic_only_RECOVERED pairs + a blinded
sheet per axis (for CVO~Z rating) and the key to content_prototype_key.json (revealed only after rating).
"""
from __future__ import annotations

import importlib.util
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
for _ in range(8):
    if os.path.exists(os.path.join(ROOT, "infra", "system", "ontology")):
        break
    ROOT = os.path.dirname(ROOT)

# corpus: {subsystem_label: [relpaths]} -- 5 genuinely distinct subsystems, cross-filetype where real
CORPUS = {
    "auth": [
        "infra/aws/opalinvest_dev/lambda/auth-handler/src/auth.ts",
        "infra/aws/opalinvest_dev/lambda/auth-handler/src/password.ts",
        "infra/aws/opalinvest_dev/lambda/auth-handler/src/throttle.ts",
        "infra/aws/opalinvest_dev/lambda/auth-handler/src/breached-passwords.ts",
        "docs/architecture/PORTAL_AUTHHARD_PRD.md",
    ],
    "ontology": [
        "infra/system/ontology/README.md",
        "infra/system/ontology/CONTENT_MODULE_DESIGN.md",
        "infra/system/01_substrate.md",
        "infra/system/ontology/content_relate_prototype.py",
        "org/modules/graph/iam_cli.py",
        "org/modules/graph/canon-patterns.yaml",
        "infra/system/00_synthesis.md",
        "infra/system/03_comp_tools.md",
    ],
    "comms": [
        "org/mcp/server.py",
        "org/mcp/inbox-watch.sh",
        "docs/architecture/AGENT_COMMS_ARCHITECTURE.md",
    ],
    "pipeline": [
        "data/canonical/schwab/silver/_canonical_silver_lib.py",
        "data/canonical/schwab/silver/build_dim_account.py",
        "data/canonical/schwab/silver/build_dim_advisor_fee.py",
        "lib/trading_calendar.py",
    ],
    "terraform": [
        "infra/aws/iam/github-actions/gha-oidc-role.tf",
        "infra/aws/terraform/astn-pipeline/iam.tf",
        "infra/aws/terraform/bd-49f-auto-login/iam.tf",
        "docs/deployment/TERRAFORM_PROTOCOL.md",
        "docs/deployment/LAMBDA_DEPLOYMENT_PROTOCOL.md",
    ],
}
MAXCHARS = 1500  # bound semantic PPMI-SVD vocab/runtime (O(vocab^3) x 26 pooled-null runs); ~1st page/intro per doc


def load_corpus():
    corpus, filetypes, folders, missing = {}, {}, {}, []
    for sub, paths in CORPUS.items():
        for p in paths:
            ap = os.path.join(ROOT, p)
            if not os.path.exists(ap):
                missing.append(p)
                continue
            try:
                with open(ap, encoding="utf-8", errors="ignore") as fh:
                    text = fh.read()[:MAXCHARS]
            except Exception as e:  # noqa: BLE001
                missing.append("%s (%s)" % (p, e))
                continue
            did = p  # doc_id = relpath (informative but the sheet shows basename+snippet)
            corpus[did] = text
            filetypes[did] = p.rsplit(".", 1)[-1] if "." in p else "?"
            folders[did] = sub
    return corpus, filetypes, folders, missing


def load_engine():
    ep = os.path.join(ROOT, "infra", "system", "ontology", "content_relate_prototype.py")
    spec = importlib.util.spec_from_file_location("content_relate_prototype", ep)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def load_harness():
    hp = os.path.join(HERE, "content_negcontrol_harness.py")
    spec = importlib.util.spec_from_file_location("content_negcontrol_harness", hp)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _base(did):
    return did.split("/")[-1]


def main():
    corpus, filetypes, folders, missing = load_corpus()
    eng, harn = load_engine(), load_harness()
    print("=" * 90)
    print("DOC-SIMILARITY SCAN -- real available workspace documents (Andrew: 'just doc similarity + scanning")
    print("  the documents available'). Technical prose = constrained vocab; ASYMMETRIC rule -> semantic")
    print("  recovers=SHIP, redundant=INCONCLUSIVE-not-drop.")
    print("=" * 90)
    print("corpus: %d docs across %d subsystems; %d missing %s"
          % (len(corpus), len(CORPUS), len(missing), (missing or "")))
    ft_counts = {}
    for f in filetypes.values():
        ft_counts[f] = ft_counts.get(f, 0) + 1
    print("filetype mix:", ft_counts)
    r = eng.run(corpus, filetypes, folders)
    print("\naxis_versions:", r.get("axis_versions"))
    print("recovery cross-tab:", json.dumps(r.get("recovery", {}), indent=1))
    key_out = {}
    for axis in ("bm25", "semantic"):
        per = r.get("per_axis", {}).get(axis)
        if not per:
            continue
        print("\n" + "-" * 90)
        print("AXIS=%s  null_threshold=%s  n_pairs_above_null=%s  cross_filetype_clusters=%d"
              % (axis, per["null_threshold"], per["n_pairs_above_null"], len(per["cross_filetype_clusters"])))
        for c in per["cross_filetype_clusters"]:
            print("  cluster (fts=%s, folder_colocated=%s): %s"
                  % (c["filetypes"], c["folder_colocated"], [_base(m) for m in c["members"]]))
        rng = random.Random(2026)
        sheet, keyd, meta = harn.sheet_from_run(r, corpus, filetypes, folders, axis, rng)
        key_out[axis] = keyd
        print("  BLINDED SHEET (rate each token 1-5 coherence WITHOUT the key):")
        for row in sheet:
            print("    [%s] fts=%s members=%s" % (row["token"], row["filetypes"], [_base(m) for m in row["members"]]))
    # semantic-only recovered pairs -- the ship/drop signal, shown with basenames
    gb = set(eng.gated_pairs(corpus, eng.AXES["bm25"])[0])
    gs = set(eng.gated_pairs(corpus, eng.AXES["semantic"])[0])
    print("\n" + "=" * 90)
    print("SEMANTIC-ONLY RECOVERED pairs (semantic gated, bm25 did NOT) -- coherent=SHIP, noise=INCONCLUSIVE:")
    sem_only = sorted(gs - gb)
    if not sem_only:
        print("  (none) -- semantic recovered ZERO pairs bm25 missed -> INCONCLUSIVE (constrained-vocab bias), NOT drop")
    for a, b in sem_only:
        print("  %s <-> %s  (same_subsystem=%s)" % (_base(a), _base(b), folders.get(a) == folders.get(b)))
    print("bm25-only pairs (bm25 gated, semantic did not): %d ; both: %d" % (len(gb - gs), len(gb & gs)))
    kp = os.path.join(HERE, "content_prototype_key.json")
    with open(kp, "w", encoding="utf-8") as fh:
        json.dump(key_out, fh, indent=1)
    print("\nkey written (reveal AFTER rating):", kp)
    return 0


if __name__ == "__main__":
    sys.exit(main())
