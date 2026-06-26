#!/usr/bin/env python3
"""BM25 dup/dead-twin scanner -- PROTOTYPE (CVO, Andrew-direct via CTO 2026-06-26).

Classifier = BM25 (lexical-twin) x firm/partner (suppress expected cross-firm twins) x
graph-reachability (one-side-dead = dead-duplicate). Advisory ONLY: ranked candidate ledger,
never auto-removes; "dead" is INFERRED until the graph confirms zero-consumers (Rule 22).

This prototype covers two NAME-level classes (the two live cases CTO cited):
  A) TF resource-label twins   -- the comp-iam `aws_iam_role "orchestrator"` collision class
  B) filename twins            -- the D3 UPPER/lower .md clobber class (case-insensitive FS)
"""
from __future__ import annotations

import math
import re
import subprocess
from collections import defaultdict
from pathlib import Path

# repo root: this file lives at org/tier1_exec/3.0.0_SA_CVO/deliverables/ -> parents[4]
REPO = Path(__file__).resolve().parents[4]

# ---- firm detection (cross-firm same-name = expected architecture -> SUPPRESS) -------------
_FIRMS = ["49f", "bd", "cot", "inf", "mdpf", "yang", "schwab", "astn", "etfs", "smartx", "news", "nna"]

def _firm_of(path: str) -> str | None:
    p = path.lower()
    for f in _FIRMS:
        if re.search(rf"(^|[/_-]){re.escape(f)}([/_-]|$|\b)", p):
            return f
    return None


# ---- tokenization -------------------------------------------------------------------------
_SPLIT = re.compile(r"[^a-z0-9]+")

def _tok(s: str) -> list[str]:
    return [t for t in _SPLIT.split(s.lower()) if t and len(t) > 1]


# ---- BM25 over a corpus of short "documents" ----------------------------------------------
class BM25:
    def __init__(self, docs: list[list[str]], k1: float = 1.5, b: float = 0.75):
        self.docs = docs
        self.k1, self.b = k1, b
        self.N = len(docs)
        self.avgdl = sum(len(d) for d in docs) / max(self.N, 1)
        self.df: dict[str, int] = defaultdict(int)
        self.postings: dict[str, list[int]] = defaultdict(list)
        for i, d in enumerate(docs):
            for t in set(d):
                self.df[t] += 1
                self.postings[t].append(i)
        self.idf = {t: math.log(1 + (self.N - n + 0.5) / (n + 0.5)) for t, n in self.df.items()}

    def neighbors(self, i: int, top: int = 5, min_score: float = 0.0):
        q = self.docs[i]
        cand: set[int] = set()
        for t in set(q):
            cand.update(self.postings[t])
        cand.discard(i)
        scored = []
        for j in cand:
            scored.append((self._score(q, j), j))
        scored.sort(reverse=True)
        return [(s, j) for s, j in scored[:top] if s > min_score]

    def _score(self, q: list[str], j: int) -> float:
        d = self.docs[j]
        dl = len(d)
        tf: dict[str, int] = defaultdict(int)
        for t in d:
            tf[t] += 1
        s = 0.0
        for t in set(q):
            if t not in tf:
                continue
            idf = self.idf.get(t, 0.0)
            num = tf[t] * (self.k1 + 1)
            den = tf[t] + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
            s += idf * num / den
        return s


# ---- corpus A: TF resource labels ---------------------------------------------------------
_TF_RES = re.compile(r'resource\s+"([^"]+)"\s+"([^"]+)"')

def _tf_resources() -> list[dict]:
    out = []
    for tf in REPO.glob("infra/aws/**/*.tf"):
        if ".terraform" in tf.parts:
            continue
        try:
            txt = tf.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        rel = str(tf.relative_to(REPO)).replace("\\", "/")
        for m in _TF_RES.finditer(txt):
            rtype, label = m.group(1), m.group(2)
            out.append({
                "id": f"{rtype}.{label}",
                "type": rtype,
                "label": label,
                "module": str(Path(rel).parent),
                "path": rel,
                "doc": _tok(label) + _tok(rtype.replace("aws_", "")),
                "firm": _firm_of(rel) or _firm_of(label),
            })
    return out


# ---- corpus B: filenames ------------------------------------------------------------------
def _repo_files() -> list[dict]:
    try:
        r = subprocess.run(["git", "ls-files"], cwd=str(REPO), capture_output=True, text=True, timeout=60)
        files = [f for f in r.stdout.splitlines() if f.strip()]
    except Exception:
        files = []
    out = []
    for f in files:
        name = Path(f).name
        stem = Path(f).stem
        out.append({
            "id": f, "name": name, "stem": stem, "path": f,
            "dir": str(Path(f).parent),
            "doc": _tok(stem),
            "firm": _firm_of(f),
        })
    return out


# ---- classifier ---------------------------------------------------------------------------
def classify(a: dict, b: dict, same_label: bool) -> str:
    """BM25-twin x firm. (Graph-reachability folded in a later tier; here NAME-level + firm.)"""
    fa, fb = a.get("firm"), b.get("firm")
    if fa and fb and fa != fb:
        return "BENIGN_CROSS_FIRM"        # expected firm-separation architecture -> suppress
    if same_label and a.get("module") and a.get("module") != b.get("module"):
        return "TF_LABEL_COLLISION"       # the comp-iam orchestrator class -- HIGH value
    return "NEEDS_REVIEW"


def scan_tf():
    res = _tf_resources()
    print(f"\n=== CLASS A: TF resource-label twins ({len(res)} resources scanned) ===")
    # group by type, BM25 within type (a label twin only meaningful within the same resource type)
    by_type: dict[str, list[int]] = defaultdict(list)
    for i, r in enumerate(res):
        by_type[r["type"]].append(i)
    findings = []
    seen_pairs = set()
    for rtype, idxs in by_type.items():
        if len(idxs) < 2:
            continue
        docs = [res[i]["doc"] for i in idxs]
        bm = BM25(docs)
        for li, gi in enumerate(idxs):
            for score, lj in bm.neighbors(li, top=4, min_score=1.0):
                gj = idxs[lj]
                key = tuple(sorted((gi, gj)))
                if key in seen_pairs:
                    continue
                seen_pairs.add(key)
                a, b = res[gi], res[gj]
                same_label = a["label"] == b["label"]
                # require either an exact-label collision OR a strong near-twin
                if not same_label and score < 2.5:
                    continue
                verdict = classify(a, b, same_label)
                findings.append((round(score, 2), verdict, a, b, same_label))
    findings.sort(key=lambda x: (x[1] != "TF_LABEL_COLLISION", -x[0]))
    sup = sum(1 for f in findings if f[1] == "BENIGN_CROSS_FIRM")
    print(f"  {len(findings)} candidate pairs ({sup} cross-firm benign-suppressed)")
    for score, verdict, a, b, same in findings:
        if verdict == "BENIGN_CROSS_FIRM":
            continue
        tag = "[EXACT-LABEL]" if same else "[near]"
        print(f"  {verdict:<20} score={score:<5} {tag} {a['type']} \"{a['label']}\" "
              f"<{a['module']}>  ~  \"{b['label']}\" <{b['module']}>")
    return findings


def scan_files():
    files = _repo_files()
    print(f"\n=== CLASS B: filename twins ({len(files)} tracked files scanned) ===")
    # case-insensitive exact-stem collisions (the D3 clobber class) -- the highest-evidence signal
    by_lower: dict[str, list[int]] = defaultdict(list)
    for i, f in enumerate(files):
        by_lower[f["name"].lower()].append(i)
    ci_collisions = [(k, v) for k, v in by_lower.items() if len(v) > 1 and len({files[i]["name"] for i in v}) > 1]
    print(f"  CASE-INSENSITIVE NAME COLLISIONS (the D3-clobber class): {len(ci_collisions)}")
    for k, idxs in ci_collisions:
        variants = sorted({files[i]["path"] for i in idxs})
        print(f"    !! {k}: " + "  |  ".join(variants))
    # near-name stem twins via BM25 (same dir, near stem) -- broader, noisier; cap output
    return ci_collisions


if __name__ == "__main__":
    scan_tf()
    scan_files()
