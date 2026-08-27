#!/usr/bin/env python
"""GATE: no value token means two different things across two enum domains (pass finding F4).

Two jobs:
  1. ACCEPTANCE on F4's remedy -- entity_status renames candidate->provisional and held->contested,
     eliminating the two DIFFERENT-meaning collisions with registry_standing.
  2. STANDING GATE on DT-3's registered vocabularies -- every vocabulary addition is a fresh
     collision risk, and Rule 24's addition gate needs a mechanical half.

WHY A COLLISION IS A DEFECT AND NOT AN AESTHETIC: `candidate` in entity_status meant a cross-fabric
mint awaiting reconciliation; `candidate` in registry_standing meant a parse-generated row awaiting
evidence. A consumer filtering on a bare status token silently merges two populations, and no
schema can catch it because each value is legal in its own field. Same shape as the firm-blind
token `gold` resolving to three different pipelines.

ALLOWLIST, NOT SUPPRESSION: a collision is permitted only when both tokens genuinely mean the SAME
thing, and it must be declared here with its reason. An undeclared collision fails the gate.

Origin: 3 collisions over 43 values at the frozen v0 target @8ba18439dd
(2.0.0_SA_COO~X, ISCK adversarial pass round 1, finding F4 -- UPHELD).

Usage:
    check_enum_collisions.py [path/to/ISCK_CONTRACT.v0.schema.json]   exit 0 = no undeclared collision
"""
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_SCHEMA = os.path.join(HERE, "ISCK_CONTRACT.v0.schema.json")

# Deliberate, ruled collisions: token -> why both uses mean the same thing.
# 1.0.0_SA_CTO~X, F4 disposition: `retired` is kept in both because both mean "was live, now
# closed", and renaming entity retirement would fight the ruled succession table (1->0 = Retirement).
# THE ALLOWED LIST IS READ FROM THE DOCTRINE, NEVER HARDCODED HERE.
# ISCK_CONTRACT.md section 3.16 is the source of truth; this gate CONSUMES it. A second copy in
# this file would put the declaration and its enforcement in two artifacts that drift apart --
# the exact defect the contract exists to kill, rebuilt inside the contract's own gate.
DOC = os.path.join(HERE, "ISCK_CONTRACT.md")


def load_allowed(doc_path):
    """Parse backticked tokens out of the doctrine's 'ALLOWED at vX:' clause."""
    if not os.path.exists(doc_path):
        return None, "doctrine not found at %s" % doc_path
    with io.open(doc_path, "r", encoding="utf-8") as fh:
        text = fh.read()
    m = re.search(r"ALLOWED at v[0-9.]+:(.*?)(?:ELIMINATED|\n\n)", text, re.S)
    if not m:
        return None, "no 'ALLOWED at vX:' clause in the doctrine"
    return set(re.findall(r"`([a-z_]+)`", m.group(1))), None


# A value that MUST resolve to exactly one enum. If this ever resolves to zero or many, the
# instrument is broken and its silence about collisions means nothing.
CONTROL_TOKEN = "admitted"


def load_enums(schema_path):
    with open(schema_path, "r", encoding="utf-8") as fh:
        defs = json.load(fh)["$defs"]
    out = {}
    for name, node in defs.items():
        if isinstance(node, dict) and "enum" in node:
            out[name] = list(node["enum"])
    # Inline enums declared on a record's own property (not hoisted to $defs) count too --
    # a collision does not care whether the domain was given a name.
    for rec, node in defs.items():
        if not isinstance(node, dict) or "properties" not in node:
            continue
        for prop, pnode in node["properties"].items():
            if isinstance(pnode, dict) and "enum" in pnode:
                out.setdefault("%s.%s" % (rec, prop), list(pnode["enum"]))
    return out


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SCHEMA
    if not os.path.exists(path):
        print("ERROR: schema not found: %s" % path)
        return 2
    allowed, err = load_allowed(DOC)
    if err:
        print("ERROR: cannot read the ALLOWED list -- %s" % err)
        print("       Refusing to judge collisions against a hardcoded copy. INSTRUMENT FAILURE,")
        print("       not a clean run.")
        return 2

    enums = load_enums(path)
    if not enums:
        print("ERROR: parsed 0 enums -- schema restructured, NOT a clean run")
        return 2

    owners = {}
    total = 0
    for enum_name, values in enums.items():
        for v in values:
            total += 1
            owners.setdefault(v, []).append(enum_name)

    print("CROSS-ENUM TOKEN COLLISION CENSUS -- %s" % os.path.basename(path))
    print("DENOMINATOR: %d enums | %d values | %d distinct tokens"
          % (len(enums), total, len(owners)))
    print("ALLOWED (read from doctrine 3.16): %d token(s) -- %s"
          % (len(allowed), ", ".join(sorted(allowed)) or "NONE"))

    # CONTROL FIRST. Without it, "0 collisions" is indistinguishable from "the map is empty".
    ctl = owners.get(CONTROL_TOKEN, [])
    if len(ctl) != 1:
        print("ERROR: control token '%s' resolved to %d enum(s), expected exactly 1."
              % (CONTROL_TOKEN, len(ctl)))
        print("       The map does not discriminate; a clean result would be meaningless.")
        return 2
    print("CONTROL: '%s' resolves to exactly one enum (%s) -- map discriminates" % (CONTROL_TOKEN, ctl[0]))
    print("")

    shared = {v: es for v, es in owners.items() if len(es) > 1}
    undeclared = []
    for v, es in sorted(shared.items()):
        if v in allowed:
            print("OK:   %-14s in %s -- ALLOWED by doctrine 3.16" % (v, es))
        else:
            print("FAIL: %-14s in %s -- undeclared collision" % (v, es))
            undeclared.append(v)

    print("")
    print("collisions: %d total, %d allowed, %d undeclared"
          % (len(shared), len(shared) - len(undeclared), len(undeclared)))

    if undeclared:
        print("")
        print("GATE FAILED: a token means two things across two domains.")
        print("  Either rename it in one enum, or add it to ALLOWED with the reason both uses")
        print("  genuinely mean the same thing. Suppressing without a reason is how the defect")
        print("  becomes permanent.")
        return 1

    print("OK: no undeclared cross-domain token collision.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
