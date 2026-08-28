#!/usr/bin/env python3
"""migrate_substrate_card_v2_to_v3 -- the DELTA PASS for B1: re-stamp delivered v2 cards as v3 with
`trust.key.key_expression` as an EXPLICIT ABSENCE (null + basis_by_field.key_expression='absent', and the
row's floor basis lowered from 'measured' if it was), so the gap the manifest's EMISSION gate sees reads
"N of M cards declare a key expression" per card instead of living in the contract.

THIS TOOL INVENTS NOTHING: it never writes an expression. A carding lane fills key_expression from the
subject (a knowledge claim, with its own basis/evidence) in a later delta; this pass only makes the
absence expressible and countable. Idempotent. Every card validates against v2 BEFORE and v3 AFTER, or
the file is left untouched and named.

Run: python org/standards/migrate_substrate_card_v2_to_v3.py [--dry-run] <card.json | dir> ...
Prints the denominator: cards seen / migrated / already v3 / declared-expression / refused.
"""
import json
import sys
from pathlib import Path

import jsonschema

HERE = Path(__file__).resolve().parent
V2 = json.loads((HERE / "SUBSTRATE_CARD.v2.schema.json").read_text(encoding="utf-8"))
V3 = json.loads((HERE / "SUBSTRATE_CARD.v3.schema.json").read_text(encoding="utf-8"))


def migrate(card):
    key = card["trust"]["key"]
    if "key_expression" not in key:
        # rebuild the dict so the field sits beside identity_space (readability only; JSON order is not semantics)
        new = {}
        for k, v in key.items():
            new[k] = v
            if k == "identity_space":
                new["key_expression"] = None
        key = new
        card["trust"]["key"] = key
    if key["key_expression"] is None:
        bbf = key.get("basis_by_field") or {}
        bbf["key_expression"] = "absent"
        key["basis_by_field"] = bbf
        if key.get("basis") == "measured":
            key["basis"] = "inferred"  # the floor rule: a row with an absent sub-claim is not 'measured'
            key["evidence"] = key.get("evidence", "") + " || v3 delta pass: key_expression ABSENT on this card (not yet declared by the carding lane); row basis lowered from measured to the floor."
    card["schema_version"] = 3
    return card


def main():
    dry = "--dry-run" in sys.argv
    targets = [Path(a) for a in sys.argv[1:] if not a.startswith("--")]
    files = []
    for t in targets:
        files += sorted(t.rglob("*.json")) if t.is_dir() else [t]
    seen = migrated = already = declared = refused = 0
    for f in files:
        try:
            card = json.loads(f.read_text(encoding="utf-8"))
        except ValueError:
            continue
        if not (isinstance(card, dict) and "schema_version" in card and "trust" in card):
            continue
        seen += 1
        sv = card.get("schema_version")
        if sv == 3:
            already += 1
            if card["trust"]["key"].get("key_expression"):
                declared += 1
            continue
        if sv != 2:
            refused += 1
            print(f"REFUSED {f}: schema_version {sv!r} is not 2")
            continue
        try:
            jsonschema.validate(card, V2)
        except jsonschema.ValidationError as e:
            refused += 1
            print(f"REFUSED {f}: not v2-valid before migration: {e.message[:120]}")
            continue
        new = migrate(json.loads(json.dumps(card)))
        try:
            jsonschema.validate(new, V3)
        except jsonschema.ValidationError as e:
            refused += 1
            print(f"REFUSED {f}: not v3-valid after migration: {e.message[:120]}")
            continue
        if new["trust"]["key"].get("key_expression"):
            declared += 1
        if not dry:
            f.write_text(json.dumps(new, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        migrated += 1
    print(f"cards seen {seen} | migrated {migrated}{' (dry-run)' if dry else ''} | already v3 {already} | "
          f"key_expression DECLARED {declared} of {seen} | refused {refused}")
    sys.exit(1 if refused else 0)


if __name__ == "__main__":
    main()
