#!/usr/bin/env python3
"""build_substrate_card_v3_1 -- derive SUBSTRATE_CARD.v3.1.schema.json FROM v3 (never a hand edit).
v3.1 = v3 + ONE narrowing: `trust.key.basis_by_field.key_expression` may be measured | held | absent --
never 'inferred'. A key expression is either exercised on a real member (measured), declared by the owner
unexercised (held), or absent (null + absent); an INFERRED key is a guess about identity, and the KEYFILL
faces prohibited it (certification arm 2) while v3's shared $defs/basis still ACCEPTED it -- measured by
0.8.0_AE_CloudComp~X mutant M6 (2026-08-28 210948Z): five mutants refused, the sixth validated. A
prohibition enforced only by a certifier's read drifts to unpopulated (A_VALUE_MUST_CARRY_ITS_CLAIM: the
consuming half is the whole mechanism). Schema-owner ruling 1.0.0_SA_CTO~X 79171 (no byte under KEYFILL;
v3.1 at the wave boundary, issuer boundary ruling 79178).

RULES this script keeps: v3 is byte-untouched (the KEYFILL freeze; the four fill faces cite it and their
v3 verdicts are never re-read under v3.1); v3.1 supersedes at the boundary the issuer named; the narrowing
is LOCAL to the one field (every other basis_by_field entry keeps the shared enum); absence stays
expressible exactly as v3 defined it (null + 'absent'); nothing else in the contract moves.

Rule-24 record for the narrowed field (four postulates): DOMAIN = the basis a key expression rests on;
GRAIN = one card's key row; INTENT = one (how the expression was arrived at); MECE over the domain --
exercised on a member -> measured; declared by the owner without exercise -> held; no expression ->
absent; 'inferred' has no member here because a key that is reasoned-from-adjacent-evidence is not a key
a consumer can COMPUTE (the field's own definition); STATE -- each value moves by exactly one act
(exercise it; declare it; remove it). Word-boundary census at drafting: 'inferred' on this field = 0 of
72 cards (four lanes' "inferred 0 of N", each an executor assertion under arm 2) -- the narrowing refuses
a value nobody has written and stops anyone writing it.

Run: python build_substrate_card_v3_1.py [--check]      (--check: byte-compare the tree file to the derivation)
Self-test (always): M6 shape (basis_by_field.key_expression='inferred') is ACCEPTED by v3 and REFUSED by
v3.1; a conformant measured card and an absent card PASS both; a null expression with basis_by_field
'measured' is REFUSED by both (v3's own contradiction fixture still fires under v3.1).
"""
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent  # org/standards -- landed at the v3.1 cut (KEYFILL wave boundary, 2026-08-28)
STD = Path(sys.argv[sys.argv.index("--standards") + 1]) if "--standards" in sys.argv else HERE
V3 = STD / "SUBSTRATE_CARD.v3.schema.json"
V31 = STD / "SUBSTRATE_CARD.v3.1.schema.json"
NARROWED = ["measured", "held", "absent"]


def build():
    v3 = json.loads(V3.read_text(encoding="utf-8"))
    v31 = json.loads(json.dumps(v3))
    v31["$id"] = "https://opal.local/standards/SUBSTRATE_CARD.v3.1.schema.json"
    v31["title"] = "Substrate Card v3.1 -- v3 + the key expression's basis may not be inferred"
    v31["description"] = (
        "SUPERSEDES v3 AT THE WAVE BOUNDARY the issuer named (after the fourth KEYFILL fill flips), NOT "
        "MID-FILL. v3 stays the freeze for the four fill faces and their verdicts are never re-read under "
        "v3.1. ONE change: trust.key.basis_by_field.key_expression is narrowed to measured | held | absent "
        "-- 'inferred' is refused by the contract (v3 accepted it; 0.8.0_AE_CloudComp~X mutant M6, "
        "2026-08-28). Everything else is v3 byte-for-byte. Cards re-stamp schema_version 3 -> 3.1 only when "
        "they PASS the narrowed enum; a card that fails is a FINDING to its owner, never silently edited. "
        + v3.get("description", ""))
    v31["properties"]["schema_version"] = {"const": 3.1}
    key = v31["properties"]["trust"]["properties"]["key"]
    # LOCAL narrowing: keep the shared $defs/basis_by_field for every other sub-claim; constrain ONE key.
    key["properties"]["basis_by_field"] = {
        "allOf": [
            {"$ref": "#/$defs/basis_by_field"},
            {
                "description": "v3.1: the key EXPRESSION's own basis may not be 'inferred' -- a key a consumer must be able to COMPUTE is measured (exercised on a real member), held (declared by the owner, unexercised) or absent (null). A reasoned guess about identity is not a basis for a key. Every other sub-claim keeps the shared enum.",
                "properties": {"key_expression": {"enum": NARROWED}},
                "x-rule24": {
                    "domain": "the basis a key expression rests on",
                    "grain": "one card's key row",
                    "intent": "one: how the expression was arrived at",
                    "mece": "measured (exercised) / held (declared) / absent (null) partition the domain; 'inferred' has no member -- an inferred key is not computable by the field's own definition",
                    "state_coherence": "each value moves by exactly one act (exercise, declare, remove); none moves with another",
                    "census_at_narrowing": "'inferred' on this field: 0 of 72 v3 cards (four lanes' arm-2 assertions) -- the narrowing refuses a value nobody wrote and stops anyone writing it",
                    "verdict": "pass",
                },
            },
        ]
    }
    return v31


def _validate(schema, inst):
    import jsonschema  # type: ignore
    errs = sorted(jsonschema.Draft202012Validator(schema).iter_errors(inst), key=str) if "2020-12" in schema.get("$schema", "") \
        else sorted(jsonschema.Draft7Validator(schema).iter_errors(inst), key=str)
    return [e.message for e in errs]


def self_test(v3, v31, seed_card):
    """Arms reachable from different truths. seed_card: a real v3 card (dict) that PASSES v3."""
    ok = True

    def arm(name, cond, detail=""):
        nonlocal ok
        ok &= bool(cond)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}{('  -- ' + detail) if detail and not cond else ''}")

    base = json.loads(json.dumps(seed_card))
    arm("seed card PASSES v3", not _validate(v3, base), str(_validate(v3, base))[:200])
    # A: the M6 shape -- inferred on the key expression, with a present expression
    m6 = json.loads(json.dumps(base))
    k = m6["trust"]["key"]
    k["key_expression"] = k.get("key_expression") or "path: <declared for the test>"
    k.setdefault("basis_by_field", {})["key_expression"] = "inferred"
    if k.get("basis") == "measured":
        k["basis"] = "inferred"  # respect the floor rule so ONLY the narrowed enum discriminates
    arm("M6 shape ACCEPTED by v3 (the finding)", not _validate(v3, m6), str(_validate(v3, m6))[:200])
    e = _validate(v31, m6)
    arm("M6 shape REFUSED by v3.1 on the narrowed field", any("inferred" in x or "enum" in x for x in e), str(e)[:200])
    # B: conformant measured card passes both
    good = json.loads(json.dumps(base))
    k = good["trust"]["key"]
    k["key_expression"] = k.get("key_expression") or "path: <declared for the test>"
    k.setdefault("basis_by_field", {})["key_expression"] = "measured"
    good["schema_version"] = 3
    arm("measured card PASSES v3", not _validate(v3, good), str(_validate(v3, good))[:200])
    good31 = json.loads(json.dumps(good))
    good31["schema_version"] = 3.1
    arm("measured card PASSES v3.1 (re-stamped 3.1)", not _validate(v31, good31), str(_validate(v31, good31))[:200])
    # C: absent card passes both
    ab = json.loads(json.dumps(base))
    k = ab["trust"]["key"]
    k["key_expression"] = None
    k.setdefault("basis_by_field", {})["key_expression"] = "absent"
    if k.get("basis") == "measured":
        k["basis"] = "inferred"
    ab31 = json.loads(json.dumps(ab))
    ab31["schema_version"] = 3.1
    arm("absent card PASSES v3", not _validate(v3, ab), str(_validate(v3, ab))[:200])
    arm("absent card PASSES v3.1", not _validate(v31, ab31), str(_validate(v31, ab31))[:200])
    # D: v3's contradiction fixture still fires under v3.1 (null + measured)
    bad = json.loads(json.dumps(ab31))
    bad["trust"]["key"]["basis_by_field"]["key_expression"] = "measured"
    arm("null + 'measured' REFUSED by v3.1 (v3 contradiction fixture retained)", bool(_validate(v31, bad)))
    # E: version discrimination -- a 3-stamped card does not pass v3.1
    arm("schema_version 3 card REFUSED by v3.1 (re-stamp is required, not implied)", bool(_validate(v31, good)))
    return ok


def main():
    v3 = json.loads(V3.read_text(encoding="utf-8"))
    v31 = build()
    text = json.dumps(v31, indent=2, ensure_ascii=False) + "\n"
    seed = json.loads(Path(sys.argv[sys.argv.index("--seed") + 1]).read_text(encoding="utf-8")) if "--seed" in sys.argv else None
    if seed is None:
        sys.exit("REFUSED: --seed <real v3 card.json> is required so the self-test runs on a real shape, not a fixture of the author's own making")
    print("self-test:")
    if not self_test(v3, v31, seed):
        sys.exit("SELF-TEST FAILED -- nothing written")
    if "--check" in sys.argv:
        cur = V31.read_text(encoding="utf-8") if V31.exists() else ""
        same = cur == text
        print(("OK" if same else "STALE") + f": {V31.name} vs derivation (sha256 {hashlib.sha256(text.encode()).hexdigest()[:12]})")
        sys.exit(0 if same else 1)
    if "--write" in sys.argv:
        V31.write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {V31} (sha256 {hashlib.sha256(text.encode()).hexdigest()[:12]}); v3 untouched (sha256 {hashlib.sha256(V3.read_bytes()).hexdigest()[:12]})")
    else:
        print(f"derived v3.1 (sha256 {hashlib.sha256(text.encode()).hexdigest()[:12]}); dry -- pass --write to land, --check to compare")


if __name__ == "__main__":
    main()
