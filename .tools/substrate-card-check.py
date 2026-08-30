#!/usr/bin/env python3
"""substrate-card-check -- validate a SUBSTRATE CARD (v3.1) against its schema AND the one rule the
schema only DESCRIBES.

Usage: substrate-card-check <card.json> [<card.json> ...]
Exit 0 = every card VALID. Exit 1 = at least one INVALID (every violation printed, per card).
Exit 2 = usage / read error.

WHY THIS EXISTS (2026-08-30, 1.0.0_SA_CTO~X, schema author; surfaced by 0.4.0_DS_ClientPlatform~V via
2.0.0_SA_COO~X 85311): org/standards/SUBSTRATE_CARD.v3.1.schema.json says of forward_disposition.set_by
"MUST NOT be the carding lane for its own subject -- describing and deciding are different acts and the
carding seat has a stake in the second" -- and JSON Schema cannot compare two fields, so that sentence
was a protection that existed only as a description. The sibling rule (inference_detail REQUIRED when
determinism is inferential) IS enforced, by if/then. This tool is the consuming half for set_by: a card
whose adjudicator is its own carding seat is INVALID here, whatever the schema says.

The schema file is NOT modified -- the carding faces cite its sha256, and a byte change there would
re-open every certified card. Layered like proof-of-spec-check: jsonschema for structure (degrades
LOUDLY if the package is absent), then the conditional rule, ALWAYS run.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "org" / "standards" / "SUBSTRATE_CARD.v3.1.schema.json"

# RULE 2 (2026-08-30, 1.0.0_SA_CTO~X): PROSE THAT ASSERTS A STRUCTURED VALUE MUST EQUAL THE FIELD.
# Measured on W4-COX card 5 @4a5e165fbf: `mutation_policy` was repaired to `append_only` in the field
# while its own evidence sentence still read "`mutation_policy` is `append_only_but_droppable`" -- a
# value the builder had already retracted and which is not in the v3.1 enum. A consumer rejecting on
# the field and a human reading the sentence beside it learn DIFFERENT things, which is the exact
# failure "a value must carry its claim in a field a consumer can reject on" exists to prevent.
# Another cross-field rule JSON Schema cannot express, which is this tool's whole purpose.
#
# THE BASIS/VALUE BRANCH IS 0.7.0_AE_CloudOps~X's, and it is load-bearing: "`<key>` is `<token>`" is
# AMBIGUOUS between a claim about that key's VALUE and a claim about its BASIS. Its first version of
# this arm FIRED ON A CERTIFIED CARD (code_heat_snap: prose "live_matches_declared is `absent`" is a
# BASIS claim agreeing with basis_by_field, while the VALUE is `unmeasured`) -- it opened the card,
# found the card right and the ARM wrong, and branched instead of reporting a defect in certified work.
# An arm that cannot tell a basis claim from a value claim manufactures defects in accepted artifacts.
BASIS_VOCAB = frozenset({"measured", "inferred", "held", "absent", "unmeasured"})


def _leaves(node, path: str = ""):
    """Every scalar leaf of the card as (pointer, value)."""
    if isinstance(node, dict):
        for key, val in node.items():
            yield from _leaves(val, path + "/" + key)
    elif isinstance(node, list):
        for i, val in enumerate(node):
            yield from _leaves(val, "%s[%d]" % (path, i))
    else:
        yield path, node


def prose_field_violations(card: dict) -> list:
    """Prose in a section asserting a value for one of THAT section's structured keys must equal it.

    Scoped to the section deliberately: a card legitimately discusses other sections' fields, and a
    whole-card scan would flag those. The comparison is exact on the token the prose quotes.
    """
    out: list = []
    leaves = dict(_leaves(card))
    keys = sorted({p.rsplit("/", 1)[-1] for p in leaves})
    for pointer, text in leaves.items():
        if not isinstance(text, str) or len(text) < 80:
            continue
        section = pointer.rsplit("/", 1)[0]
        for key in keys:
            hit = re.search(r"`?\b" + re.escape(key) + r"\b`?\s+is\s+`([^`]+)`", text)
            if not hit:
                continue
            claimed = hit.group(1)
            actual = leaves.get(section + "/" + key)
            if actual is None:
                continue
            basis = leaves.get(section + "/basis_by_field/" + key)
            if claimed.lower() in BASIS_VOCAB and basis is not None:
                if claimed != str(basis):
                    out.append("%s: prose says `%s` is `%s` but %s/basis_by_field/%s is `%s`"
                               % (pointer, key, claimed, section, key, basis))
            elif claimed != str(actual):
                out.append("%s: prose says `%s` is `%s` but the structured field %s/%s is `%s` "
                           "-- a consumer rejecting on the field and a reader of the sentence learn "
                           "different things" % (pointer, key, claimed, section, key, actual))
    return out


def check_card(card: dict, schema: dict) -> tuple[list[str], str]:
    """Return (violations, structural_mode)."""
    v: list[str] = []
    try:
        import jsonschema  # type: ignore

        for err in sorted(jsonschema.Draft7Validator(schema).iter_errors(card), key=str):
            v.append(f"schema: {'/'.join(str(p) for p in err.absolute_path) or '<root>'}: {err.message}")
        mode = "jsonschema"
    except ImportError:
        mode = "FALLBACK (jsonschema not installed -- structural coverage PARTIAL; install for full)"
        for k in schema.get("required", []):
            if k not in card:
                v.append(f"schema-fallback: missing required key '{k}'")
    # THE RULE THE SCHEMA ONLY DESCRIBES. NULL set_by = undecided, legal. Equality to the carding seat
    # is the self-adjudication the description forbids. Compared as exact serial strings -- a lane
    # serial (~K) is a different seat from its base, and the description binds the LANE that carded.
    fd = card.get("forward_disposition")
    if isinstance(fd, dict):
        set_by = fd.get("set_by")
        carded_by = card.get("carded_by")
        if set_by is not None and carded_by is not None and str(set_by) == str(carded_by):
            v.append("forward_disposition.set_by == carded_by (%r): the carding seat adjudicated its own subject "
                     "-- REFUSED; describing and deciding are different acts (schema description, now enforced)"
                     % set_by)
    # RULE 2 -- prose/structure divergence on a value the card itself types. See the header.
    for line in prose_field_violations(card):
        v.append("prose/structure: " + line)
    return v, mode


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        print(f"READ-ERROR: schema {SCHEMA_PATH}: {exc}")
        return 2
    rc = 0
    for arg in sys.argv[1:]:
        try:
            card = json.loads(Path(arg).read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            print(f"READ-ERROR: {arg}: {exc}")
            return 2
        violations, mode = check_card(card, schema)
        print(f"substrate-card-check | {arg} | structural={mode} | violations={len(violations)}")
        for line in violations:
            print(f"  VIOLATION: {line}")
        print("  " + ("INVALID" if violations else "VALID"))
        rc = rc or (1 if violations else 0)
    return rc


if __name__ == "__main__":
    sys.exit(main())
