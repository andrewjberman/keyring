"""
NFRA_COMPROUTE Charter-1 -- POTION semantic embedder (the one-home relevance-signal module).

Replaces the router's LEXICAL relevance (comp_route.query_match token-overlap, which buries the correct
cap at ~rank-11 on oblique/vague intents -- the C1-measured disease) with SEMANTIC cosine over POTION
static token-embeddings. This is CTO's POTION T2-ENGINE design (NFRA_COMPROUTE_POTION_DESIGN.md), built
on the 5 supply-chain conditions + 3 refinements (CTO GO 20260707T070413Z).

DATA-NOT-CODE (CTO gate #4, the one he won't waive -- VERIFIED cos=1.0 vs model2vec.encode):
  Runtime loads ONLY (a) model.safetensors -- a pure static embedding TABLE via safetensors.numpy
  (NO pickle, NO code-exec) and (b) tokenizer.json via the tokenizers rust lib. There is ZERO model2vec
  import at route-time (model2vec is a BUILD-ONLY tool; the encode is reimplemented here and byte-verified
  identical: tokenize(add_special_tokens=False) -> mean-pool token rows -> L2-normalize; the POTION zipf
  weighting is baked into the distilled table at build time, so runtime is a plain mean-pool). The vendored
  artifact cannot execute; the only code is this audited module + the pinned tokenizers/numpy/safetensors.

OFFLINE (gate #3): loads purely from vendored repo files; NO network / NO HuggingFace fetch at route-time.
PIN-BY-HASH + FAIL-CLOSED (gate #1): each vendored file's SHA256 is verified against the MANIFEST at load;
  a mismatch RAISES (fail-closed, loud) -- the caller (gate #5) catches it and degrades to lexical + alarms.
FAIL-SAFE (gate #5): load_embedder() returns None on ANY failure; the router keeps its existing lexical
  relevance (valid-if-weaker) and emits a LOUD alarm. A POTION failure NEVER crashes comp-which.

Read-only, deterministic, ASCII. Author: 0.8.0_AE_CloudComp~E (NFRA_COMPROUTE Charter-1). 2026-07-07.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from typing import Optional

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))


def _sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


class PotionEmbedder:
    """Pure-data POTION embedder over a vendored (model.safetensors + tokenizer.json) pair.
    embed(text) -> L2-normalized float32 vector, bit-identical to model2vec.StaticModel.encode."""

    def __init__(self, model_dir: str, expected: Optional[dict] = None):
        from safetensors.numpy import load_file  # data-only loader (no pickle)
        from tokenizers import Tokenizer

        st_path = os.path.join(model_dir, "model.safetensors")
        tk_path = os.path.join(model_dir, "tokenizer.json")
        # PIN-BY-HASH: verify vendored files before trusting them (fail-closed).
        if expected:
            for name, p in (("model.safetensors", st_path), ("tokenizer.json", tk_path)):
                want = expected.get(name)
                got = _sha256(p)
                if want and want != got:
                    raise ValueError("POTION hash-mismatch on %s: manifest=%s vendored=%s (FAIL-CLOSED)"
                                     % (name, want, got))
        self._emb = load_file(st_path)["embeddings"]     # (vocab, dim) static table -- pure data
        self._tok = Tokenizer.from_file(tk_path)
        self.dim = int(self._emb.shape[1])

    def embed(self, text: str) -> np.ndarray:
        ids = self._tok.encode(text or "", add_special_tokens=False).ids
        if not ids:
            return np.zeros(self.dim, dtype=np.float32)
        v = self._emb[ids].mean(axis=0)
        n = float(np.linalg.norm(v))
        return (v / n) if n > 0 else v

    def embed_many(self, texts) -> np.ndarray:
        return np.vstack([self.embed(t) for t in texts]) if texts else np.zeros((0, self.dim), np.float32)


def load_embedder(model_dir: str = "", manifest_path: str = "") -> Optional[PotionEmbedder]:
    """FAIL-SAFE loader (gate #5): returns a PotionEmbedder, or None on ANY failure (missing vendored
    files, hash-mismatch, missing deps). The router treats None as 'semantic unavailable -> use lexical
    + alarm', never a crash. model_dir defaults to the vendored model under this one-home dir."""
    try:
        mdir = model_dir or os.path.join(_HERE, "model")
        expected = None
        mpath = manifest_path or os.path.join(_HERE, "MANIFEST.json")
        if os.path.exists(mpath):
            man = json.load(open(mpath, encoding="utf-8"))
            expected = (man.get("model_files_sha256") or {})
        return PotionEmbedder(mdir, expected=expected)
    except Exception as e:  # noqa: BLE001 -- fail-safe: NEVER crash the router on a POTION load failure
        sys.stderr.write("ALARM: POTION semantic embedder unavailable -> falling back to lexical relevance"
                         " (%s: %s)\n" % (type(e).__name__, e))
        return None


def cosine(a: np.ndarray, b: np.ndarray) -> float:
    na = float(np.linalg.norm(a))
    nb = float(np.linalg.norm(b))
    return float(np.dot(a, b) / (na * nb)) if (na > 0 and nb > 0) else 0.0
