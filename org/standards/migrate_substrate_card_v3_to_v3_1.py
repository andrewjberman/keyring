#!/usr/bin/env python3
"""migrate_substrate_card_v3_to_v3_1 -- the SETTLED-CARD REVALIDATION / MIGRATION RECEIPT for v3.1
(issuer boundary ruling 79178 step 2): over every v3 card, REPORT first, re-stamp only what PASSES.

REPORT-ONLY by default (the receipt). Per card it prints:
  enum            PASS | REFUSED   -- basis_by_field.key_expression under the narrowed v3.1 enum
  delta_prose     STALE | clean | n/a -- the v2->v3 delta pass appended "|| v3 delta pass: key_expression
                                       ABSENT ... row basis lowered" to trust.key.evidence; on a card whose
                                       key_expression is now NON-NULL that sentence is FALSE (0.8.0_AE_CloudComp~Y
                                       210441Z). Reported as a FINDING to the card's owner -- never stripped here.
  floor_basis     lowered-with-declared-expression | ok -- the delta pass lowered trust.key.basis to 'inferred'
                                       on absent rows; a filled row whose sub-claims are all measured/held may
                                       carry a higher scalar; the floor rule is the OWNER's to re-derive.
--apply re-stamps schema_version 3 -> 3.1 ONLY on cards that PASS v3.1 (validated after the stamp; a card
that would not validate is left byte-untouched and counted refused). Nothing else is edited. A failing
card is a FINDING to its owner (carded_by), printed with the file path -- never silently edited.
Denominator printed: cards seen / v3 / already v3.1 / PASS / REFUSED (by enum | by other) / stale prose /
lowered floor, and the per-owner breakdown.

Run: python migrate_substrate_card_v3_to_v3_1.py --standards org/standards [--apply] <card.json | dir> ...
"""
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

DELTA_SENTENCE = "v3 delta pass: key_expression ABSENT on this card"
# the stable marker a retain-and-discharge card carries in the SAME evidence field (CCY's form, CVO-read)
DISCHARGE_MARKER = "DISCHARGED"


RANK = {"measured": 3, "held": 2, "inferred": 1, "absent": 0}
SUBCLAIMS = ("identity_space", "key_expression", "key_is_stable", "crosses_spaces", "declared_mapping")


def true_floor(key):
    """The CONFIRMED floor predicate (schema owner 1.0.0_SA_CTO~X 79274, on issuer 79253): MIN over ALL sub-claims
    PRESENT in the key row; a sub-claim carrying a value with no basis_by_field entry enters at 'inferred'.
    Returns (true_min_rank_or_None, unbased_subclaims)."""
    bbf_map = key.get("basis_by_field") or {}
    unbased = [s for s in SUBCLAIMS if key.get(s) is not None and s not in bbf_map]
    ranks = [RANK[v] for v in bbf_map.values() if v in RANK] + [RANK["inferred"]] * len(unbased)
    return (min(ranks) if ranks else None), unbased


def declared_only_floor(key):
    """The REJECTED reading, kept ONLY as the falsifier's other arm -- never used for a verdict."""
    bbf_map = key.get("basis_by_field") or {}
    ranks = [RANK[v] for v in bbf_map.values() if v in RANK]
    return min(ranks) if ranks else None


def self_test():
    """CRO~X 215229Z / CCY~Y 79304: v3.1 must carry an INCOMPLETE-MAP FALSIFIER. A card with a valued
    declared_mapping and NO basis entry for it: the confirmed floor reads 'inferred'; the declared-only reading
    reads the other sub-claims' MIN ('measured'). An implementation returning the second is the bug. Both arms
    must be reachable from different truths: the complete-map card must read the SAME under both."""
    ok = True
    incomplete = {"identity_space": "path", "key_expression": "x", "key_is_stable": "stable", "crosses_spaces": False,
                  "declared_mapping": "m", "basis": "inferred",
                  "basis_by_field": {"identity_space": "measured", "key_expression": "measured", "key_is_stable": "measured", "crosses_spaces": "measured"}}
    tm, unb = true_floor(incomplete)
    ok &= tm == RANK["inferred"] and unb == ["declared_mapping"]
    ok &= declared_only_floor(incomplete) == RANK["measured"]  # the rejected reading errs UPWARD, on the card with LESS evidence
    complete = dict(incomplete, basis_by_field=dict(incomplete["basis_by_field"], declared_mapping="held"))
    tm2, unb2 = true_floor(complete)
    ok &= tm2 == RANK["held"] and unb2 == [] and declared_only_floor(complete) == tm2  # complete map: both agree
    print("self-test:", "PASS -- incomplete-map falsifier discriminates (confirmed=inferred vs declared-only=measured); complete map agrees under both" if ok else "FAIL")
    return ok


def main():
    if "--self-test" in sys.argv:
        sys.exit(0 if self_test() else 1)
    if not self_test():
        sys.exit("REFUSED: self-test failed; nothing read")
    if "--standards" not in sys.argv:
        sys.exit("REFUSED: --standards <dir holding SUBSTRATE_CARD.v3.schema.json and v3.1> is required")
    std = Path(sys.argv[sys.argv.index("--standards") + 1])
    v31 = json.loads((std / "SUBSTRATE_CARD.v3.1.schema.json").read_text(encoding="utf-8"))
    import jsonschema  # type: ignore
    V = jsonschema.Draft202012Validator if "2020-12" in v31.get("$schema", "") else jsonschema.Draft7Validator
    val = V(v31)
    apply = "--apply" in sys.argv
    skip = {"--apply", "--standards", str(std)}
    targets = [Path(a) for a in sys.argv[1:] if a not in skip and not a.startswith("--")]
    files = []
    for t in targets:
        files += sorted(t.rglob("*.json")) if t.is_dir() else [t]
    c = Counter()
    per_owner = defaultdict(Counter)
    findings = []
    for f in files:
        try:
            card = json.loads(f.read_text(encoding="utf-8"))
        except ValueError:
            continue
        if not (isinstance(card, dict) and "schema_version" in card and "trust" in card):
            continue
        c["seen"] += 1
        sv = card.get("schema_version")
        owner = str(card.get("carded_by", "?"))
        if sv == 3.1:
            c["already_v3.1"] += 1
            per_owner[owner]["already"] += 1
            continue
        if sv != 3:
            c["not_v3"] += 1
            per_owner[owner]["not_v3"] += 1
            continue
        c["v3"] += 1
        key = card.get("trust", {}).get("key", {})
        ke = key.get("key_expression")
        ev = str(key.get("evidence", ""))
        present = ke is not None and DELTA_SENTENCE in ev
        # 0.8.0_AE_CloudComp~Y 79201 / CVO 212444Z: PRESENCE is not LIVENESS. A card may retain the sentence as
        # the on-card record that the migration happened, provided the SAME evidence field carries an explicit
        # discharge marking it historical. Two predicates, reported separately: present; present AND undischarged.
        discharged = present and DISCHARGE_MARKER in ev.upper()
        stale = present and not discharged  # LIVE false claim -- the only one that is a finding
        # 0.8.0_AE_CloudComp~X 79234: "scalar inferred beside a declared expression" OVER-COUNTS rows whose floor is
        # legitimately set by a weaker sibling (key_is_stable 'inferred' on 19 of CCX's 30). SCHEMA-OWNER RULING
        # (1.0.0_SA_CTO~X, confirming the issuer's 79253): the floor is MIN over ALL sub-claims PRESENT in the row,
        # rank measured > held > inferred > absent, and a sub-claim carrying a VALUE with NO declared basis_by_field
        # entry enters the MIN at no stronger than 'inferred' -- A VALUE MUST CARRY ITS CLAIM: it cannot be counted
        # measured or held, and it is not absent. (A declared-only MIN would let a row raise its floor by leaving a
        # basis undeclared -- the exact drift the field exists to stop.) The row UNDERSTATES only when
        # rank(scalar) < rank(true MIN). The undeclared value is ALSO its own finding: declare its basis.
        true_min, unbased = true_floor(key)  # ONE implementation, the self-tested one -- never a second copy in the loop
        scalar_rank = RANK.get(key.get("basis"))
        lowered = ke is not None and true_min is not None and scalar_rank is not None and scalar_rank < true_min
        trial = json.loads(json.dumps(card))
        trial["schema_version"] = 3.1
        errs = sorted(val.iter_errors(trial), key=str)
        enum_fail = any("key_expression" in "/".join(str(p) for p in e.absolute_path) and ("enum" in e.message or "inferred" in e.message) for e in errs)
        status = "PASS" if not errs else ("REFUSED-enum" if enum_fail else "REFUSED-other")
        c[status] += 1
        per_owner[owner][status] += 1
        if present:
            c["delta_prose_present"] += 1
            per_owner[owner]["prose_present"] += 1
        if discharged:
            c["delta_prose_discharged"] += 1
            per_owner[owner]["prose_discharged"] += 1
        if stale:
            c["stale_delta_prose_LIVE"] += 1
            per_owner[owner]["prose_LIVE"] += 1
            findings.append((owner, str(f), "delta-pass sentence in trust.key.evidence is a LIVE false claim on a filled row (no discharge marker in the field) -- owner strips it or discharges it in place"))
        if lowered:
            c["lowered_floor_with_declared_expression"] += 1
            per_owner[owner]["lowered_floor"] += 1
            inv = {v: k for k, v in RANK.items()}
            findings.append((owner, str(f), f"trust.key.basis '{key.get('basis')}' UNDERSTATES the true floor '{inv[true_min]}' (MIN over the declared basis_by_field map) -- owner re-derives the scalar from the card's own map"))
        if unbased and ke is not None:
            c["unbased_subclaim"] += 1
            per_owner[owner]["unbased"] += 1
            findings.append((owner, str(f), f"sub-claim(s) {unbased} carry a value but no basis_by_field entry -- declare the basis (the scalar is MIN over declared entries; an unbased sub-claim is not folded into it)"))
        if errs:
            findings.append((owner, str(f), f"{status}: {errs[0].message[:140]}"))
        prose_word = 'LIVE' if stale else ('disch' if discharged else ('clean' if ke is not None else 'n/a'))
        print(f"{status:14s} prose={prose_word:5s} floor={'lowered' if lowered else 'ok':7s} {owner:28s} {f}")
        if apply and not errs:
            f.write_text(json.dumps(trial, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
            c["restamped"] += 1
    print("\nRECEIPT: seen %d | v3 %d | already v3.1 %d | not v3 %d | PASS %d | REFUSED-enum %d | REFUSED-other %d | delta prose present %d (discharged in place %d, LIVE false claim %d) | scalar UNDERSTATES true-MIN floor %d | unbased valued sub-claim %d%s"
          % (c["seen"], c["v3"], c["already_v3.1"], c["not_v3"], c["PASS"], c["REFUSED-enum"], c["REFUSED-other"], c["delta_prose_present"], c["delta_prose_discharged"], c["stale_delta_prose_LIVE"], c["lowered_floor_with_declared_expression"], c["unbased_subclaim"], f" | RE-STAMPED {c['restamped']}" if apply else " | report only (no byte written)"))
    for o in sorted(per_owner):
        print(f"  owner {o}: {dict(per_owner[o])}")
    if findings:
        print(f"\nFINDINGS to owners ({len(findings)}):")
        for o, p, why in findings:
            print(f"  [{o}] {p}: {why}")
    sys.exit(0 if c["REFUSED-enum"] == 0 and c["REFUSED-other"] == 0 else 1)


if __name__ == "__main__":
    main()
