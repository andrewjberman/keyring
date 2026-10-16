"""MDPF_DEMQUE round 9, DQ-t-73 criterion AC3 (read-only, no network): every queued Bloomberg request carries its surface tag.
Rule (by the request's `page` text): 'client performance' -> B; 'rival funds' -> C; 'research' -> D; 'Positioning' or 'production daily pulls' -> A.
TAGS-OK when every requests/*.json (not *.quote*.json) with vendor bloomberg carries `surface` equal to that rule, no other request file carries one,
no quote file carries one, every file still parses. Else TAGS-BAD <why>. Run from the worktree root."""
from __future__ import annotations

import glob
import json
import os
import sys

REQ = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "requests")
RULE = (("client performance", "B"), ("rival funds", "C"), ("research", "D"), ("Positioning", "A"), ("production daily pulls", "A"))


def want(page: str):
    for prefix, s in RULE:
        if (page or "").startswith(prefix):
            return s
    return None


def main() -> int:
    files = sorted(glob.glob(os.path.join(REQ, "*.json")))
    if not files:
        print("TAGS-BAD no request files under " + REQ)
        return 1
    n_bbg = 0
    for f in files:
        name = os.path.basename(f)
        try:
            d = json.load(open(f, encoding="utf-8"))
        except ValueError as exc:
            print("TAGS-BAD %s does not parse: %s" % (name, exc))
            return 1
        if ".quote" in name:
            if isinstance(d, dict) and "surface" in d:
                print("TAGS-BAD the quote file %s carries a surface" % name)
                return 1
            continue
        if not isinstance(d, dict):
            continue
        if d.get("vendor") == "bloomberg":
            n_bbg += 1
            w = want(d.get("page"))
            if w is None:
                print("TAGS-BAD %s: page %r matches no surface rule" % (name, (d.get("page") or "")[:60]))
                return 1
            if d.get("surface") != w:
                print("TAGS-BAD %s: surface is %r, the rule says %r" % (name, d.get("surface"), w))
                return 1
        elif "surface" in d:
            print("TAGS-BAD %s is not a Bloomberg request and carries a surface" % name)
            return 1
    print("TAGS-OK %d Bloomberg requests tagged" % n_bbg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
