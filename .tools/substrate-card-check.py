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
# KNOWN LIMIT, carried IN THE TOOL rather than only in the message that found it (0.7.0_AE_CloudOps~X,
# 2026-08-30, answering this arm's landing): RULE 2 matches the SYNTAX "`<key>` is `<token>`", not the
# CLAIM, so it cannot separate a LIVE ASSERTION from QUOTED HISTORY. A card narrating its own correction
# in the matched form -- "`mutation_policy` is `editable` in the earlier version" -- would trip a rule
# that is right about the syntax and wrong about the claim. The collision is LIKELY rather than
# hypothetical, because this face actively REWARDS narrating your own corrections: measured across the 17
# tracked cards, 2 sites already narrate a superseded value and neither trips RULE 2 only because neither
# happens to use the matched form ("REMOVED ... from `composes`", "read `held`"). NOT PRE-EMPTIVELY
# WIDENED -- arming for a case that has never occurred is the same error in the other direction, and the
# discriminator (a past-tense narration cue in the preceding clause) is cheap to add IF it ever fires.
# The limit prints in the violation text, so the gate teaches it at violation time rather than in a
# message that scrolls. Same shape as the ASSERTED-vs-DESCRIBED class this seat spent the evening
# stopping in the 7A certification predicate: structure proves well-formedness, never authorship.
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
                           "different things. LIMIT OF THIS ARM: it matches SYNTAX, not CLAIM, and "
                           "cannot separate a LIVE ASSERTION from QUOTED HISTORY -- if this sentence "
                           "is narrating a superseded value ('`%s` is `%s` in the earlier version'), "
                           "THE FIRST HYPOTHESIS IS THE ARM, NOT THE CARD."
                           % (pointer, key, claimed, section, key, actual, key, claimed))
    return out



# RULE 3 -- A NULL VALUE CANNOT CARRY A NON-NULL BASIS. The mechanical half of the prose/basis class
# 3.0.0_SA_CVO~X found on card 7 (basis `measured` beside a value whose own text said UNMEASURED).
# The consuming half is the whole mechanism: a consumer that rejects on `basis != measured` ACCEPTS a
# field whose entire value is the word `unmeasured`, which is the one case the vocabulary exists to
# stop. Censused at pin 47954ef3de: 12 of 102 basis-carrying cards, across four seats, 8 of them
# declaring `measured` -- and every one passes this checker today, so the arm adds coverage rather
# than restating one.
# COST: one dict lookup per string leaf, no new I/O, no network -- it rides the walk RULE 2 already does.
# NON-APPLICATION, stated so the rule cannot ratchet: (a) it does NOT bind a value of `unmeasured`
# beside basis `absent`/`unmeasured` -- that pairing is CORRECT and is the certified `code_heat_snap`
# case in the header above, which is this arm's negative control; (b) it does NOT bind prose that
# merely CONTAINS an unmeasured clause under a stronger basis -- 12 further fields at the same pin --
# because separating a live disclosure from QUOTED HISTORY needs a reader, and a mechanical arm there
# would manufacture defects in accepted work, which is exactly how RULE 2's first version failed.
# That half stays a human read on purpose; this half needs no judgment at all.
NULL_VALUE_TOKENS = frozenset({"unmeasured", "not measured"})
BASIS_RANK = {"absent": 0, "unmeasured": 0, "held": 1, "inferred": 2, "measured": 3}


def null_value_basis_violations(card: dict) -> list:
    """A field whose VALUE is the null token, while its basis_by_field entry claims better."""
    out: list = []
    leaves = dict(_leaves(card))
    for pointer, value in leaves.items():
        if not isinstance(value, str) or "/basis_by_field/" in pointer:
            continue
        section, key = pointer.rsplit("/", 1)
        if value.strip().rstrip(".").lower() not in NULL_VALUE_TOKENS:
            continue
        basis = leaves.get(section + "/basis_by_field/" + key)
        if basis is None:
            continue
        rank = BASIS_RANK.get(str(basis).strip().lower())
        if rank is not None and rank > 0:
            out.append("%s: the VALUE is `%s` but %s/basis_by_field/%s is `%s` -- a consumer "
                       "rejecting on the basis field ACCEPTS a field that carries no measurement. "
                       "Floor the basis to `absent`, or replace the value with what was measured."
                       % (pointer, value.strip(), section, key, basis))
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
    # RULE 3 -- a null VALUE under a non-null basis. See the header for cost + non-application.
    for line in null_value_basis_violations(card):
        v.append("null-value/basis: " + line)
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
