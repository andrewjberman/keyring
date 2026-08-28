#!/usr/bin/env python
"""WP3-1 AC3 -- per-row CARRIER DEPENDENCY, measured against the schema at a cited commit.

PLUS38_ONLY iff every record type a row's arms exercise is in the +38 catalog (the 14 types whose
$defs carry a record_type const at the frozen boundary dcbe214a44). Otherwise
V03_CARRIER_REQUIRED, naming which carrier(s).

⛔ BOTH CATALOGS ARE DERIVED, NEITHER IS TYPED. The +38 catalog is read from the schema AT
dcbe214a44 by walking $defs for a record_type const -- not from a list in this file, which would
be a typed count wearing a different hat (R3-CRO-21 / R3-DT-8). The carriers are the set
difference against the pin's own catalog.

⛔ EVIDENCE IS A CITED READ. Each row reports the record types it exercises AND the
`$defs.<type>.properties.record_type.const` line number at the pin, so the classification can be
re-derived rather than believed.

A row's exercised types are read from the row's OWN cells (responsibility + reject + both arm
columns), matching backticked or bare type names against the pin's catalog -- the row text is the
only statement of what its arms touch.
"""
import json
import re
import subprocess
import sys

BS = chr(92)
ROW_SPLIT = re.compile('(?<!' + re.escape(BS) + ')' + re.escape('|'))
SCHEMA = "org/standards/isck/ISCK_CONTRACT.v0.schema.json"
DESIGN = "org/standards/isck/WP3_LEDGER_DESIGN.md"
PLUS38 = "dcbe214a44"


def blob(commit, path):
    return subprocess.check_output(["git", "show", "%s:%s" % (commit, path)],
                                   stderr=subprocess.PIPE).decode("utf-8", "replace")


def catalog(commit):
    """{record_type: line} -- DERIVED by walking $defs for a record_type const."""
    text = blob(commit, SCHEMA)
    doc = json.loads(text)
    lines = text.splitlines()
    out = {}
    for name, spec in (doc.get("$defs") or {}).items():
        rt = (spec.get("properties") or {}).get("record_type")
        if isinstance(rt, dict) and "const" in rt:
            const = rt["const"]
            ln = next((i + 1 for i, text in enumerate(lines)
                       if '"const"' in text and '"%s"' % const in text), None)
            out[const] = ln
    return out


def rows_at(commit):
    s3 = blob(commit, DESIGN).split("## 3.")[1].split("\n## 4.")[0]
    return [ln for ln in s3.splitlines() if re.match(r'^\|\s*\d+\s*\|', ln)]


def main():
    pin = sys.argv[1]
    plus38 = catalog(PLUS38)
    pin_cat = catalog(pin)
    carriers = sorted(set(pin_cat) - set(plus38))
    result = {}
    for line in rows_at(pin):
        cells = ROW_SPLIT.split(line)
        row = cells[1].strip()
        text = " ".join(cells[2:])
        touched = sorted(t for t in pin_cat if re.search(r'\b%s\b' % re.escape(t), text))
        needed = [t for t in touched if t in carriers]
        result[row] = {
            "exercises": touched,
            "carrier_dependency": "V03_CARRIER_REQUIRED" if needed else "PLUS38_ONLY",
            "carriers_required": needed,
            "evidence": ["%s:%s @ %s ($defs.%s.properties.record_type.const)"
                         % (SCHEMA, pin_cat[t], pin, t) for t in needed] or
                        ["%s @ %s -- every exercised type has a record_type const in the +38 "
                         "catalog read at %s" % (SCHEMA, pin, PLUS38)],
        }
    counted = {
        "plus38_catalog_size": len(plus38),
        "pin_catalog_size": len(pin_cat),
        "carriers_added_by_v03": carriers,
        "rows_counted": len(result),
        "rows_PLUS38_ONLY": sum(1 for v in result.values()
                                if v["carrier_dependency"] == "PLUS38_ONLY"),
        "rows_V03_CARRIER_REQUIRED": sum(1 for v in result.values()
                                         if v["carrier_dependency"] == "V03_CARRIER_REQUIRED"),
    }
    print(json.dumps({"pin": pin, "plus38_boundary": PLUS38,
                      "counted": counted, "rows": result}, indent=2, sort_keys=True))
    print("COUNTED: +38 catalog %d types | pin %d | carriers %s | rows %d = %d PLUS38_ONLY + %d "
          "V03_CARRIER_REQUIRED"
          % (counted["plus38_catalog_size"], counted["pin_catalog_size"], carriers,
             counted["rows_counted"], counted["rows_PLUS38_ONLY"],
             counted["rows_V03_CARRIER_REQUIRED"]), file=sys.stderr)


if __name__ == "__main__":
    main()
