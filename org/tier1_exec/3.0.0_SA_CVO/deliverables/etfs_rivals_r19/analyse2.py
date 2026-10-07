"""CVO~RV: each frame of r19grade.py's result against its chart object (ETFS_RIVALS rounds 15-19).

Usage: python analyse2.py <layer dir> <r19grade result json>

Prints denominators for: frames against object keys; no-currency frames (nc-1); currency named (pc-1); the trade list
against the object's markers (tl-1); the month strip against the markers' year-months inside the strip's span (ml-1);
the range buttons (pd-2).
"""
import collections
import json
import pathlib
import re
import sys

LAYER = pathlib.Path(sys.argv[1])
RES = json.load(open(sys.argv[2], encoding="utf-8"))
OBJS = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in (LAYER / "charts").glob("*.json")}
PAGE_YEAR, PAGE_MONTH = 2026, 10


def strip_months(n_cells):
    """The year-months of an n-cell strip counted back from the page month, oldest first."""
    out = []
    year, month = PAGE_YEAR, PAGE_MONTH
    for _ in range(n_cells):
        out.append("%04d-%02d" % (year, month))
        month -= 1
        if month == 0:
            month = 12
            year -= 1
    return out[::-1]


def list_agrees(text, n_markers):
    lines = len(re.findall(r"(?:Bought|Sold) (?:on|between) ", text))
    more = re.search(r"and (\d+) earlier trade", text)
    if n_markers == 0:
        return "No trades in the last 365 days" in text and lines == 0
    if n_markers <= 20:
        return lines == n_markers and not more
    return lines == 20 and bool(more) and int(more.group(1)) == n_markers - 20


def main():
    count = collections.Counter()
    examples = []
    keys = sum(len(o["securities"]) for o in OBJS.values())
    print("frames", len(RES["frames"]), "object keys", keys, "page errors", len(RES["pageerrors"]))
    for frame in RES["frames"]:
        sec = OBJS[frame["fund"]]["securities"][frame["key"]]
        markers = sec["markers"]
        currency = sec.get("currency")
        if currency is None:
            count[("no currency", "svg" if frame["svg"] else "no svg", frame["status"])] += 1
        else:
            count[("has currency", "svg" if frame["svg"] else "NO SVG")] += 1
            if currency != "USD":
                count[("non-USD frame prints its currency", currency in frame["text"])] += 1
        text = " ".join(frame["trades"] or [])
        ok = list_agrees(text, len(markers))
        count[("trade list agrees with markers", ok)] += 1
        if not ok:
            examples.append(("tl", frame["fund"], frame["key"], len(markers), text[:80]))
        count[("range buttons", tuple(frame["buttons"]))] += 1
        if frame["strip"]:
            span = strip_months(len(frame["strip"]))
            lit = {span[i] for i, cell in enumerate(frame["strip"]) if cell[1] in ("u", "d")}
            ends = {m["end"][:7] for m in markers}
            inside = {m for m in ends if m in span}
            count[("strip cells", len(span))] += 1
            count[("strip last label", frame["strip"][-1][0])] += 1
            count[("strip == marker months inside its span", lit == inside)] += 1
            if lit != inside:
                examples.append(("ml", frame["fund"], frame["key"], sorted(lit - inside), sorted(inside - lit)))
            if len(span) == 12 and "2025-10" in ends:
                count["year strips with an October 2025 marker (no cell)"] += 1
    for key, n in sorted(count.items(), key=str):
        print(n, key)
    for ex in examples:
        print("  ", ex)


if __name__ == "__main__":
    main()
