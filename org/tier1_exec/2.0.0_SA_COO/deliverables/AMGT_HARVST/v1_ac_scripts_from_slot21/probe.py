"""Probe (not a criterion): where do empty mappings sit in the two held listing payloads?"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd()))

from lib.opal_data_harvest import silver_from_bronze  # noqa: E402

HELD = Path("C:/Users/Opal Bloomberg/Desktop/ajb_workspace/.runtime/opal-data-harvest/harvest_listing")
CASES = [
    ("sa", HELD / "sa_p1_990943eddbd5a172.json"),
    ("wsj", HELD / "wsj_p1_45058f937f5eff24.html"),
    ("wsj", HELD / "wsj_p2_bfec5a47fe3ed50b.html"),
]


def walk(value, path, out):
    if isinstance(value, dict):
        if not value:
            out.append(path)
        for k, v in value.items():
            walk(v, "%s.%s" % (path, k), out)
    elif isinstance(value, list):
        for i, v in enumerate(value):
            walk(v, "%s[%d]" % (path, i), out)


for publisher, path in CASES:
    body = path.read_bytes()
    rows = silver_from_bronze.listing_hit_rows(
        publisher, body, "probe query", 1, "bronze/probe.key",
        "2026-09-25T00:00:00Z", "live", "20260925T000000Z",
    )
    empties = []
    for i, row in enumerate(rows):
        walk(row, "row[%d]" % i, empties)
    depth0 = [e for e in empties if e.count(".") == 1 and "[" not in e.split(".", 1)[1]]
    print("%s %s: rows=%d  empty-mappings=%d  top-level-empty=%d"
          % (publisher, path.name, len(rows), len(empties), len(depth0)))
    print("   top-level empty fields: %s" % sorted({e.split(".", 1)[1] for e in depth0}))
    nested = [e for e in empties if e not in depth0]
    print("   nested empty paths (first 5 of %d): %s" % (len(nested), nested[:5]))
    if rows:
        print("   row[0] keys: %s" % sorted(rows[0].keys()))
