#!/usr/bin/env python3
"""Blinded negative-control acceptance harness for the content-relatedness prototype.

CVO~Z-owned (BUILD GO 2026-07-20). Implements the PRE-REGISTERED protocol in
CONTENT_PROTOTYPE_NEGCONTROL_PREREG_20260720.md. The engine (CTO~Z) emits corpus + pairs + candidate
clusters; THIS harness builds the negative controls, the blinded rating sheet, the null-anchored threshold,
and scores human ratings against the LOCKED pass bar.

Determinism: all randomness is seeded and the seed is stamped into every output (the C-1 discipline applied
to the harness's own RNG -- a decoy set you cannot reproduce is not a control). stdlib only.

The harness is itself an instrument that MUST be able to fail: `--self-test` runs a known-SIGNAL fixture
(must PASS) and a known-NOISE fixture (must FAIL). If the noise fixture ever PASSES, the harness is broken
and no verdict it emits can be trusted.
"""
from __future__ import annotations

import argparse
import json
import random
import statistics
import sys
from collections import defaultdict

# --- the PRE-REGISTERED pass bar (mirrors the committed prereg doc s.3; LOCKED) --------------------
BAR_REAL_MINUS_DECOY = 2.0     # real median coherence must exceed decoy median by >= this
BAR_REAL_MINUS_BASE = 1.0      # ... and exceed the folder-colocation baseline by >= this
BAR_DECOY_FP_MAX = 0.20        # fraction of decoys rated >=4 must be <= this
BAR_RANK_SEP_MIN = 0.70        # fraction of reals rated strictly above the decoy median must be >= this
COHERENT_RATING = 4            # a rating >= this counts as "reader called it a coherent topic"
N_UNDERPOWERED = 8             # < this many real clusters -> verdict UNDERPOWERED, never a PASS
THRESHOLD_ALPHA = 0.01         # promotion threshold = (1-alpha) quantile of the null = p99


# --- negative-control construction -----------------------------------------------------------------
def _filetype_multiset(items: list[dict], ids: list[str]) -> tuple:
    by_id = {it["item_id"]: it for it in items}
    return tuple(sorted(by_id[i]["filetype"] for i in ids if i in by_id))


def build_decoys(corpus: list[dict], clusters: list[dict], rng: random.Random) -> list[dict]:
    """For each real cluster, a RANDOM cluster matched on size AND filetype multiset (>=2 types),
    members drawn at random from the corpus. Structure identical -> only topical coherence differs."""
    by_ft: dict[str, list[str]] = defaultdict(list)
    for it in corpus:
        by_ft[it["filetype"]].append(it["item_id"])
    decoys = []
    for c in clusters:
        want = list(_filetype_multiset(corpus, c["members"]))  # exact filetype composition to match
        members: list[str] = []
        ok = True
        for ft in want:
            pool = [i for i in by_ft.get(ft, []) if i not in members]
            if not pool:
                ok = False
                break
            members.append(rng.choice(pool))
        if ok:
            decoys.append({"cluster_id": "decoy_" + c["cluster_id"], "members": members,
                           "filetypes": sorted(set(want)), "arm": "decoy", "matched_real": c["cluster_id"]})
    return decoys


def build_folder_baseline(corpus: list[dict], clusters: list[dict], rng: random.Random) -> list[dict]:
    """Random members drawn from within ONE folder, matched on size + >=2 filetypes. Tests whether RRF
    beats the FREE `contains` (folder) structural edge (review #4 confound)."""
    by_folder: dict[str, list[dict]] = defaultdict(list)
    for it in corpus:
        by_folder[it["folder_path"]].append(it)
    baseline = []
    for c in clusters:
        size = len(c["members"])
        # folders that hold >= size items spanning >= 2 filetypes
        cand = [f for f, its in by_folder.items()
                if len(its) >= size and len({i["filetype"] for i in its}) >= 2]
        if not cand:
            continue
        its = by_folder[rng.choice(cand)]
        # draw `size` items ensuring >=2 filetypes
        picks: list[dict] = []
        for _ in range(200):
            picks = rng.sample(its, size)
            if len({p["filetype"] for p in picks}) >= 2:
                break
        if len({p["filetype"] for p in picks}) < 2:
            continue
        baseline.append({"cluster_id": "base_" + c["cluster_id"],
                         "members": [p["item_id"] for p in picks],
                         "filetypes": sorted({p["filetype"] for p in picks}),
                         "arm": "baseline", "matched_real": c["cluster_id"]})
    return baseline


def make_blinded_sheet(clusters: list[dict], decoys: list[dict], baseline: list[dict],
                       corpus: list[dict], rng: random.Random) -> tuple[list[dict], dict]:
    """Interleave + shuffle + strip the arm label. Displayed filetypes are derived UNIFORMLY from the
    corpus for every arm, so real and decoy are presented identically (no arm leak). Returns
    (sheet_for_rater, provenance_key)."""
    ft_by_id = {it["item_id"]: it["filetype"] for it in corpus}
    reals = [{**c, "arm": "real"} for c in clusters]
    combined = reals + decoys + baseline
    order = list(range(len(combined)))
    rng.shuffle(order)
    sheet, key = [], {}
    for display_idx, src_idx in enumerate(order):
        c = combined[src_idx]
        token = "C%03d" % display_idx
        fts = sorted({ft_by_id.get(m, "?") for m in c["members"]})
        sheet.append({"token": token, "members": c["members"], "filetypes": fts})
        key[token] = {"arm": c["arm"], "cluster_id": c["cluster_id"]}
    return sheet, key


# --- null-anchored threshold (review #2) -----------------------------------------------------------
def _quantile(sorted_vals: list[float], q: float) -> float:
    if not sorted_vals:
        return float("nan")
    idx = min(len(sorted_vals) - 1, max(0, int(round(q * (len(sorted_vals) - 1)))))
    return sorted_vals[idx]


def threshold_from_null(pairs: list[dict], cluster_member_ids: set[str], score_key: str = "rrf") -> dict:
    """Promotion threshold = p99 of the NULL = RRF of NON-cluster (random background) pairs. Reports
    sensitivity at p95/p99/p995 so the verdict cannot ride one knob."""
    null_scores = sorted(p[score_key] for p in pairs
                         if not (p["a"] in cluster_member_ids and p["b"] in cluster_member_ids))
    return {"null_n": len(null_scores),
            "p95": _quantile(null_scores, 0.95),
            "p99": _quantile(null_scores, 1 - THRESHOLD_ALPHA),
            "p995": _quantile(null_scores, 0.995)}


# --- scoring the ratings against the LOCKED bar ----------------------------------------------------
def score(sheet: list[dict], key: dict, ratings: dict[str, int]) -> dict:
    """ratings: token -> 1..5 coherence. Computes the per-run verdict against the pre-registered bar."""
    by_arm: dict[str, list[int]] = defaultdict(list)
    for tok, r in ratings.items():
        by_arm[key[tok]["arm"]].append(r)
    reals, decoys, base = by_arm.get("real", []), by_arm.get("decoy", []), by_arm.get("baseline", [])
    if len(reals) < N_UNDERPOWERED:
        return {"verdict": "UNDERPOWERED", "n_real": len(reals),
                "note": "fewer than %d real clusters -- insufficient to accept" % N_UNDERPOWERED}
    real_med = statistics.median(reals)
    decoy_med = statistics.median(decoys) if decoys else float("nan")
    base_med = statistics.median(base) if base else float("nan")
    decoy_fp = (sum(1 for r in decoys if r >= COHERENT_RATING) / len(decoys)) if decoys else float("nan")
    rank_sep = (sum(1 for r in reals if r > decoy_med) / len(reals)) if decoys else 0.0
    checks = {
        "real_vs_decoy": real_med - decoy_med >= BAR_REAL_MINUS_DECOY,
        "real_vs_baseline": real_med - base_med >= BAR_REAL_MINUS_BASE,
        "decoy_fp": decoy_fp <= BAR_DECOY_FP_MAX,
        "rank_sep": rank_sep >= BAR_RANK_SEP_MIN,
    }
    return {"verdict": "PASS" if all(checks.values()) else "FAIL",
            "checks": checks, "real_median": real_med, "decoy_median": decoy_med,
            "baseline_median": base_med, "decoy_fp_rate": decoy_fp, "pct_real_above_decoy_median": rank_sep,
            "n_real": len(reals), "n_decoy": len(decoys), "n_baseline": len(base)}


# --- offline self-test: the harness must PASS signal and FAIL noise ---------------------------------
def _fixture(rng: random.Random, coherent_reals: bool) -> dict:
    """Synthetic corpus + clusters + simulated ratings. coherent_reals=True -> reals rate high (signal);
    False -> reals rate like decoys (noise). The harness must PASS the first and FAIL the second."""
    fts = ["docx", "xlsx", "pptx"]
    corpus = [{"item_id": "i%03d" % n, "filetype": fts[n % 3],
               "folder_path": "f%d" % (n % 5), "text_sha": "x"} for n in range(120)]
    clusters = [{"cluster_id": "r%02d" % k,
                 "members": ["i%03d" % (k * 3 + j) for j in range(3)]} for k in range(15)]
    decoys = build_decoys(corpus, clusters, rng)
    baseline = build_folder_baseline(corpus, clusters, rng)
    sheet, keyd = make_blinded_sheet(clusters, decoys, baseline, corpus, rng)
    ratings = {}
    for row in sheet:
        arm = keyd[row["token"]]["arm"]
        if arm == "real" and coherent_reals:
            ratings[row["token"]] = rng.choice([4, 5, 5])
        else:
            ratings[row["token"]] = rng.choice([1, 2, 2, 3])   # decoy/baseline (and noise-reals) = low
    return score(sheet, keyd, ratings)


def self_test() -> int:
    sig = _fixture(random.Random(1), coherent_reals=True)
    noise = _fixture(random.Random(2), coherent_reals=False)
    ok = True
    if sig["verdict"] != "PASS":
        print("FAIL self-test: known-SIGNAL fixture did not PASS -> %s" % sig)
        ok = False
    else:
        print("OK: known-signal fixture PASSED (real=%.1f decoy=%.1f)"
              % (sig["real_median"], sig["decoy_median"]))
    if noise["verdict"] == "PASS":
        print("FAIL self-test: known-NOISE fixture PASSED -> the harness CANNOT FAIL, it is broken: %s" % noise)
        ok = False
    else:
        print("OK: known-noise fixture did NOT pass (verdict=%s) -- the harness can fail on trash" % noise["verdict"])
    # decoy structural-match invariant
    dc = build_decoys([{"item_id": "a", "filetype": "docx", "folder_path": "f", "text_sha": ""},
                       {"item_id": "b", "filetype": "xlsx", "folder_path": "f", "text_sha": ""},
                       {"item_id": "c", "filetype": "docx", "folder_path": "f", "text_sha": ""},
                       {"item_id": "d", "filetype": "xlsx", "folder_path": "f", "text_sha": ""}],
                      [{"cluster_id": "r", "members": ["a", "b"]}], random.Random(3))
    if not dc or sorted(dc[0]["filetypes"]) != ["docx", "xlsx"]:
        print("FAIL self-test: decoy did not match the real's filetype span")
        ok = False
    else:
        print("OK: decoy matched filetype span (%s)" % dc[0]["filetypes"])
    print("\n" + ("OK: all self-test cases pass" if ok else "ERROR: self-test FAILED"))
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="content-relatedness blinded negative-control harness (CVO~Z)")
    ap.add_argument("--self-test", action="store_true", help="run the offline signal/noise fixtures")
    ap.add_argument("--engine-json", help="engine output (run_meta+corpus+pairs+clusters) -> emit blinded sheet")
    ap.add_argument("--seed", type=int, default=20260720)
    args = ap.parse_args(argv)
    if args.self_test:
        return self_test()
    if args.engine_json:
        data = json.load(open(args.engine_json, encoding="utf-8"))
        rng = random.Random(args.seed)
        decoys = build_decoys(data["corpus"], data["clusters"], rng)
        baseline = build_folder_baseline(data["corpus"], data["clusters"], rng)
        sheet, keyd = make_blinded_sheet(data["clusters"], decoys, baseline, data["corpus"], rng)
        member_ids = {m for c in data["clusters"] for m in c["members"]}
        thr = threshold_from_null(data.get("pairs", []), member_ids)
        print(json.dumps({"seed": args.seed, "threshold": thr, "sheet": sheet,
                          "_key_WITHHELD_until_rated": True, "n_real": len(data["clusters"]),
                          "n_decoy": len(decoys), "n_baseline": len(baseline)}, indent=2))
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
