#!/usr/bin/env python3
"""build_substrate_card_v3 -- derive SUBSTRATE_CARD.v3.schema.json FROM v2 (never a hand edit of an
1,100-line contract). v3 = v2 + ONE field, `trust.key.key_expression`, in the vocabulary the L0 manifest
receiver already REQUIRES (L0_GRAPH_SUBSTRATE_MANIFEST.schema.json #/$defs/part/properties/key:
key_expression string|null; null only under an unknown/absent claim).

WHY (D11_SUBSTRATE_ANALYSIS_PRD.md sec 10.2, 2026-08-27): the manifest's `key` receiver requires a
key_expression and the card contract had no slot for it -- "seven properties of an unnamed thing" --
so no card population of any size could ever satisfy the EMISSION gate (0 of 42 parts carrying all four
receivers). A SOURCE gap; "card harder" cannot close it. B1 of the 2026-08-28 runway (Andrew-direct
14:08Z "Lift everything, time to work buddy").

RULES this script keeps: v2 is byte-untouched (it is the wave-1/2/3 FREEZE; in-flight cards stay valid
under it); v3 supersedes at the NEXT wave boundary; the new field reuses the manifest's definition and
x-rule24 record rather than coining a second key vocabulary; absence is EXPRESSIBLE (null + basis_by_field
absent) and never silent. Run: python org/standards/build_substrate_card_v3.py [--check]
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
V2 = HERE / "SUBSTRATE_CARD.v2.schema.json"
V3 = HERE / "SUBSTRATE_CARD.v3.schema.json"
MANIFEST = HERE / "L0_GRAPH_SUBSTRATE_MANIFEST.schema.json"


def build():
    v2 = json.loads(V2.read_text(encoding="utf-8"))
    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    # GRAIN: read the receiver's definition from the manifest schema, never retype it
    recv = man["$defs"]["part"]["properties"]["key"]
    assert "key_expression" in recv["required"], "manifest key receiver no longer requires key_expression"
    recv_ke = recv["properties"]["key_expression"]
    v3 = json.loads(json.dumps(v2))  # deep copy
    v3["$id"] = "https://opal.local/standards/SUBSTRATE_CARD.v3.schema.json"
    v3["title"] = "Substrate Card v3 -- v2 + the key EXPRESSION the L0 manifest receiver requires"
    v3["description"] = (
        "SUPERSEDES v2 AT THE WAVE BOUNDARY, NOT MID-WAVE (the same rule v2 stated for v1). v2 stays the freeze for "
        "waves 1-3 of NFRA_SUBSTRATECARDING; every delivered v2 card stays valid under v2. v3 exists because the L0 "
        "manifest's `key` RECEIVER (L0_GRAPH_SUBSTRATE_MANIFEST.schema.json #/$defs/part/properties/key) REQUIRES a "
        "`key_expression` and v2's trust.key row had no slot for it -- the card could name a key's SPACE, stability "
        "and cross-space standing but not the EXPRESSION that yields a member's key, so no card population could ever "
        "satisfy the manifest's EMISSION gate (D11_SUBSTRATE_ANALYSIS_PRD.md sec 10.2: 0 of 42 parts carrying all four "
        "receivers; a SOURCE gap that 'card harder' cannot close). ONE field added, in the receiver's own vocabulary "
        "(read from the manifest schema by build_substrate_card_v3.py, never retyped): trust.key.key_expression. "
        "Absence is EXPRESSIBLE, never silent: null is legal ONLY with basis_by_field.key_expression = 'absent' (and "
        "therefore the row's floor basis is not 'measured'). Everything else is v2 verbatim. || " + v2["description"]
    )
    v3["properties"]["schema_version"] = {"const": 3}
    key = v3["properties"]["trust"]["properties"]["key"]
    key["required"] = key["required"][:3] + ["key_expression"] + key["required"][3:]
    props = key["properties"]
    new_props = {}
    for k, v in props.items():
        new_props[k] = v
        if k == "identity_space":
            new_props["key_expression"] = {
                "type": recv_ke["type"],
                "description": (
                    "THE EXPRESSION THAT YIELDS A MEMBER'S KEY IN identity_space -- what the L0 manifest's `key` receiver "
                    "consumes (same name, same type, same null semantics as L0_GRAPH_SUBSTRATE_MANIFEST.schema.json "
                    "#/$defs/part/properties/key/properties/key_expression; read from there at build time). A path "
                    "grammar, a column, a derivation ('sha1 of anchor node id'), a declared parse -- stated so a consumer "
                    "can COMPUTE the key, not merely name its space. NULL is STRUCTURAL PAYLOAD ABSENCE, legal only "
                    "when basis_by_field.key_expression is 'absent' -- and then the row cannot read basis 'measured'. "
                    "A card whose key row is 'measured' with a null expression is the contradiction v3 exists to make "
                    "unrepresentable."
                ),
                "x-rule24-record-at": "L0_GRAPH_SUBSTRATE_MANIFEST.schema.json#/$defs/part/properties/key -- legitimate reuse with the record at source, the same pattern as materializer_standing / authority_role / basis.",
            }
    key["properties"] = new_props
    # the enforceable half: a null expression forbids the row's basis being 'measured' and requires the
    # explicit per-field absence; a non-null expression must be non-empty
    key.setdefault("allOf", []).extend([
        {
            "description": "v3: a null key_expression is EXPRESSIBLE ABSENCE -- it requires basis_by_field.key_expression = 'absent' and forbids the row's floor basis 'measured'.",
            "if": {"properties": {"key_expression": {"type": "null"}}, "required": ["key_expression"]},
            "then": {
                "required": ["basis_by_field"],
                "properties": {
                    "basis": {"not": {"const": "measured"}},
                    "basis_by_field": {"required": ["key_expression"], "properties": {"key_expression": {"const": "absent"}}},
                },
            },
        },
        {
            "description": "v3: a present key_expression is a non-empty string.",
            "if": {"properties": {"key_expression": {"type": "string"}}, "required": ["key_expression"]},
            "then": {"properties": {"key_expression": {"minLength": 1}}},
        },
    ])
    return v3


def main():
    v3 = build()
    text = json.dumps(v3, indent=2, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        cur = V3.read_text(encoding="utf-8") if V3.exists() else ""
        same = cur == text
        print(("OK" if same else "STALE") + f": {V3.name} vs derivation from {V2.name} + {MANIFEST.name}")
        sys.exit(0 if same else 1)
    V3.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {V3.name} sha256:{hashlib.sha256(text.encode()).hexdigest()[:16]} (v2 untouched: sha256:{hashlib.sha256(V2.read_bytes()).hexdigest()[:16]})")


if __name__ == "__main__":
    main()
