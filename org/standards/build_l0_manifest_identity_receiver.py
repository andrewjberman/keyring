#!/usr/bin/env python3
"""build_l0_manifest_identity_receiver -- add the `identity` RECEIVER to L0_GRAPH_SUBSTRATE_MANIFEST.schema.json
#/$defs/part, DERIVED in place from the schema's own `key` receiver (same claim_status / null-under-unknown /
basis-evidence-owner shape) and from the ISCK vocab registries (enums read at build time, never retyped).

WHY (WP-3b, 2026-08-28): the manifest's part vocabulary carries none of the five ISCK entity identity fields
(0.4.0_DT_ClientPlatform~X 78074: translated 0 / ERRORED 42, ONE missing-field set); the issuer ruled option (b)
-- the L0 emitter DECLARES the five per part (@7abc9544a2) -- and the design lane ruled the VALUES
(org/standards/isck/ledger/translation/L0_PART_IDENTITY_MAPPING.json @f553dd2b00). `part` is
additionalProperties:false, so without this receiver the declaration pass produces a manifest that fails its
own schema. This is the slot. Idempotent: re-running derives the same receiver; --check compares.

The receiver is OPTIONAL pre-rerun exactly like `key` (its description says so); after the emitter's declaration
pass lands 42/42 it is a candidate for `required`, a separate act. Run:
  python org/standards/build_l0_manifest_identity_receiver.py [--check]
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCHEMA = HERE / "L0_GRAPH_SUBSTRATE_MANIFEST.schema.json"
VOCAB = HERE / "isck" / "vocab"
ISCK = HERE / "isck" / "ISCK_CONTRACT.v0.schema.json"
MAPPING = "org/standards/isck/ledger/translation/L0_PART_IDENTITY_MAPPING.json"


def members(name):
    d = json.loads((VOCAB / f"{name}.json").read_text(encoding="utf-8"))
    out = []
    for m in d["members"]:
        out.append(m.get("id") or m.get("name") if isinstance(m, dict) else m)
    assert out and all(isinstance(x, str) and x for x in out), name
    return out


def build(schema):
    part = schema["$defs"]["part"]
    key = part["properties"]["key"]
    entity_classes = members("entity_classes")
    identity_policies = members("identity_policies")
    isck = json.loads(ISCK.read_text(encoding="utf-8"))
    scopes = isck["$defs"]["entity"]["properties"]["identity_scope"]["enum"]
    fields = ["entity_class", "plane", "entity_grain", "identity_scope", "identity_policy"]
    recv = {
        "type": "object",
        "additionalProperties": False,
        "description": (
            "RECEIVER for a part's ISCK IDENTITY -- the five fields the frozen ISCK entity contract requires "
            "(entity_class, plane, entity_grain, identity_scope, identity_policy) that the manifest's own vocabulary "
            "never carried (WP-3b finding 78074: two schemas never joined). DECLARED per part by the L0 emitter's "
            "declaration pass (issuer ruling @7abc9544a2) applying the design lane's mapping (" + MAPPING + " @f553dd2b00): "
            "entity_class 'part'; entity_grain 'part'; identity_scope 'logical'; plane by home_space onto L1's four "
            "planes (@16cd74c870) with a homeless part carried as 'unplaced'; identity_policy by home_space from the "
            "registry, homeless = held_for_adjudication. basis is 'held' (the mapping is the authority), never "
            "'measured'. Same claim_status / null-under-unknown / basis-evidence-owner shape as the `key` receiver "
            "(derived from it by build_l0_manifest_identity_receiver.py). OMISSION IS A COMPATIBILITY-ONLY PRE-RERUN "
            "STATE, never a third semantic claim; after the declaration pass emits 42/42 this becomes REQUIRED by a "
            "separate act. Enums for entity_class and identity_policy are READ FROM the ISCK vocab registries at "
            "build time -- one estate vocabulary, not a local copy."
        ),
        "required": ["claim_status", "basis", "evidence", "owner", *fields],
        "properties": {
            "claim_status": json.loads(json.dumps(key["properties"]["claim_status"])),
            "entity_class": {"type": ["string", "null"], "enum": [*entity_classes, None],
                             "x-vocab-source": "org/standards/isck/vocab/entity_classes.json (read at build time)"},
            "plane": {"type": ["string", "null"],
                      "description": "One of L1's four canonical planes (symbol | file | arn_resource | chain_motif) or the declared token 'unplaced' for a part with no home (Rule-24 record in the ruling; census 0 at ruling time). A free string in the contract; constrained here to the declared set so a fifth plane is a NAMING act, not a typo.",
                      "enum": ["symbol", "file", "arn_resource", "chain_motif", "unplaced", None]},
            "entity_grain": {"type": ["string", "null"], "description": "'part' for a manifest part (the L0 registry's own grain); a finer grain is a later declaration."},
            "identity_scope": {"type": ["string", "null"], "enum": [*scopes, None],
                               "x-vocab-source": "org/standards/isck/ISCK_CONTRACT.v0.schema.json #/$defs/entity/properties/identity_scope (read at build time)"},
            "identity_policy": {"type": ["string", "null"], "enum": [*identity_policies, None],
                                "x-vocab-source": "org/standards/isck/vocab/identity_policies.json (read at build time)"},
            "basis": json.loads(json.dumps(key["properties"]["basis"])),
            "evidence": json.loads(json.dumps(key["properties"]["evidence"])),
            "owner": json.loads(json.dumps(key["properties"]["owner"])),
            "mapping_digest": {"type": ["string", "null"], "description": "sha256 (git blob or content) of the mapping file the declaration applied; printed by the pass; null only under claim_status unknown."},
        },
        "allOf": [
            {
                "if": {"properties": {"claim_status": {"const": "unknown"}}, "required": ["claim_status"]},
                "then": {"properties": {**{f: {"type": "null"} for f in fields}, "mapping_digest": {"type": "null"}, "basis": {"const": "absent"}}},
            },
            {
                "if": {"properties": {"claim_status": {"const": "declared"}}, "required": ["claim_status"]},
                "then": {
                    "required": ["mapping_digest"],
                    "properties": {**{f: {"type": "string", "minLength": 1} for f in fields},
                                   "mapping_digest": {"type": "string", "minLength": 8},
                                   "basis": {"$ref": "#/$defs/basis_present",
                                             "$comment": "BOUND, not retyped -- the same pattern as the key receiver."}},
                },
            },
        ],
        "x-rule24": {
            "axis": "whether a card-independent DECLARATION of a part's ISCK identity landed on this part",
            "grain": "one receiver on one part",
            "intent": "one -- did the declaration pass populate it; NOT whether the identity is correct (that is the contract's contest mechanism)",
            "mece": "declared = populated from the mapping with basis/evidence; unknown = every other state (no pass yet, or a part the mapping refused). Exhaustive: a receiver either received or did not.",
            "state_coherence": "unknown -> declared by the emitter's pass; declared -> unknown only by explicit retraction; a value change is a mapping_version change (the ruling's contest path), never a re-read.",
        },
    }
    new_props = {}
    for k, v in part["properties"].items():
        new_props[k] = v
        if k == "key":
            new_props["identity"] = recv
    part["properties"] = new_props
    return schema


def main():
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    had = "identity" in schema["$defs"]["part"]["properties"]
    if had:
        schema["$defs"]["part"]["properties"].pop("identity")
    out = build(schema)
    text = json.dumps(out, indent=2, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        cur = SCHEMA.read_text(encoding="utf-8")
        same = cur == text
        print(("OK" if same else "STALE") + f": {SCHEMA.name} identity receiver vs derivation (vocab read at check time)")
        sys.exit(0 if same else 1)
    SCHEMA.write_text(text, encoding="utf-8", newline="\n")
    print(f"wrote {SCHEMA.name} with the identity receiver ({'replaced' if had else 'added'}); sha256:{hashlib.sha256(text.encode()).hexdigest()[:16]}")


if __name__ == "__main__":
    main()
