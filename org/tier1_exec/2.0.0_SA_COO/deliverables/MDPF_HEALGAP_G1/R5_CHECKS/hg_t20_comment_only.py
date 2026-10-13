"""MDPF_HEALGAP round 5, HG-t-20: the transcripts pull.tf header is corrected, and ONLY comments change. No AWS call.

  python hg_t20_comment_only.py [FILE]

FILE (default infra/aws/terraform/transcripts/pull.tf) is compared with the base blob BASE_BLOB (its bytes at the round-5 cut):
  - every line that is not a comment and not blank is IDENTICAL, in order (so a `terraform plan` can read no change);
  - the header (first 30 lines) names both live rules, teams-global-transcripts-pull-hourly and
    outlook-global-transcripts-pull-daily, states that they are live (the word live or ENABLED), carries the read date
    2026-10-13, and no longer says the file is `DESIRED ONLY` or `never applied`;
  - the file is ASCII only.
Last line: COMMENT-OK or COMMENT-BAD <reasons>. At the base this is COMMENT-BAD (the header still says DESIRED ONLY).
"""
from __future__ import annotations

import re
import subprocess
import sys

BASE_BLOB = "ebabe8dad470cfb6a4ed0e865c13172bef05e12a"
PATH = "infra/aws/terraform/transcripts/pull.tf"


def code_lines(text: str) -> list:
    return [ln.rstrip() for ln in text.splitlines() if ln.strip() and not ln.lstrip().startswith("#")]


def main(path: str) -> int:
    base = subprocess.run(["git", "cat-file", "blob", BASE_BLOB], capture_output=True)
    if base.returncode != 0:
        print(f"COMMENT-BAD the base blob {BASE_BLOB} cannot be read (git cat-file rc {base.returncode})")
        return 1
    try:
        new_bytes = open(path, "rb").read()
    except OSError as exc:
        print(f"COMMENT-BAD cannot read {path}: {exc}")
        return 1
    bad = []
    try:
        new_bytes.decode("ascii")
    except UnicodeDecodeError as exc:
        bad.append(f"non-ASCII byte at {exc.start}")
    new = new_bytes.decode("utf-8", "replace")
    old = base.stdout.decode("utf-8", "replace")
    a, b = code_lines(old), code_lines(new)
    if a != b:
        first = next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), min(len(a), len(b)))
        bad.append("non-comment lines differ (base %d, new %d; first difference at code line %d)" % (len(a), len(b), first + 1))
    header = "\n".join(new.splitlines()[:30])
    for rule in ("teams-global-transcripts-pull-hourly", "outlook-global-transcripts-pull-daily"):
        if rule not in header:
            bad.append(f"the header does not name {rule}")
    if not re.search(r"\b(live|ENABLED)\b", header):
        bad.append("the header does not say the rules are live")
    if "2026-10-13" not in header:
        bad.append("the header carries no read date 2026-10-13")
    if re.search(r"DESIRED ONLY|never applied", header):
        bad.append("the header still says DESIRED ONLY / never applied")
    if bad:
        print("COMMENT-BAD " + "; ".join(bad))
        return 1
    print("COMMENT-OK %d non-comment line(s) identical to the base; header names both live rules, read 2026-10-13" % len(b))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else PATH))
