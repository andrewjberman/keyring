"""
NFRA_AKPIPE -- build the PINNED profile artifact (phrases + frozen idf).

Author: 4.0.0_SA_CRO (Chief Research Officer)

WHY THIS EXISTS. The dev scorer computes idf over whatever corpus it is scoring, which
makes a score CORPUS-DEPENDENT: a stored paper's value would silently change as new papers
arrive. That breaks two contracts at once -- lossless (the row is no longer the row that
was written) and independently recomputable (a reader cannot reproduce a stored score).

So production scores against a FROZEN idf table, versioned with the profile. This script
builds that artifact from a reference corpus (the harvested substrate), and the Lambda
FAILS LOUD if the artifact is missing rather than falling back to corpus idf.

Usage:  python build_profile.py <substrate.jsonl> <out.json>
Then:   aws s3 cp <out.json> s3://<bucket>/_profile/akpipe-profile-v3.json

ASCII-only.
"""

from __future__ import annotations

import json
import math
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "scripts"))
from akpipe_scorer import PROFILE_PHRASES, PROFILE_VERSION, normalize, tokenize  # noqa: E402


def main() -> int:
    src, out = sys.argv[1], sys.argv[2]
    rows = [json.loads(line) for line in open(src, encoding="utf-8")]
    texts = [f"{r.get('title','')} {r.get('abstract','')}" for r in rows]
    N = len(texts)
    print(f"[profile] reference corpus N={N} (DENOMINATOR)")

    pats = {p: re.compile(r"\b" + re.escape(normalize(p)) + r"(?:s|es)?\b")
            for p in PROFILE_PHRASES}
    lowered = [normalize(t) for t in texts]

    df = {p: 0 for p in PROFILE_PHRASES}
    for low in lowered:
        for p in PROFILE_PHRASES:
            if pats[p].search(low):
                df[p] += 1

    idf = {p: max(0.0, math.log((N - df[p] + 0.5) / (df[p] + 0.5) + 1.0))
           for p in PROFILE_PHRASES}
    avgdl = sum(max(1, len(tokenize(t))) for t in texts) / max(1, N)

    artifact = {
        "profile_version": PROFILE_VERSION,
        "reference_corpus_n": N,
        "phrases": PROFILE_PHRASES,
        "df": df,
        "idf": idf,
        "avgdl": avgdl,
        "note": ("FROZEN idf. Production scores against this, never the day's harvest, so a "
                 "stored paper's score never changes as the corpus grows. Rebuilding this "
                 "artifact MUST bump profile_version -- scores across versions are not "
                 "comparable, and silently mixing them would be a vintage error."),
    }
    with open(out, "w", encoding="utf-8") as f:
        json.dump(artifact, f, indent=1)

    hit = sum(1 for p in PROFILE_PHRASES if df[p] > 0)
    print(f"[profile] {hit}/{len(PROFILE_PHRASES)} phrases occur at least once in the reference corpus")
    print(f"[profile] avgdl={avgdl:.1f}  -> wrote {out}")
    dead = [p for p in PROFILE_PHRASES if df[p] == 0]
    if dead:
        print(f"[profile] NOTE {len(dead)} phrases never occur (max idf, fire only when they do): "
              f"{', '.join(dead[:12])}{' ...' if len(dead) > 12 else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
