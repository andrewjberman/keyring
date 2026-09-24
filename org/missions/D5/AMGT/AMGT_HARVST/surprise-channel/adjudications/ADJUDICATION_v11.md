# AMGT_HARVST round 4: CVO adjudication

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T05:1xZ, LOCAL on SITEZ.
**Inputs:** `2.0.0_SA_COO~Y`'s packet @`ebb318b5c4`, the one order, and this seat's own instruments: an
independent canonical-shape test over every labelled bronze object, and a per-segment unlabelled census.

## Round state

**1 of 1 terminal.** Sweep **PASS 5 / FAIL 0 / UNVERIFIABLE 0 of 5**. **Zero writes, zero vendor calls.** The
cell classified all 18 objects and **labelled nothing**, which is what the ruling required.

## The decisive measurement, reproduced here independently

The packet's claim is that shape cannot distinguish the unlabelled 18 from the harvester's own output, so the last
derivation route for `Z-S1`'s backward half is closed. **I tested it myself** — re-serialising each object's
parsed JSON with sorted keys and tight separators and comparing to the stored bytes:

| label | n | canonical | non-canonical | not JSON |
|---|---|---|---|---|
| `normalised_record` | 83 | **0** | 83 | 0 |
| `as_received` | 16 | 0 | 3 | 13 |

⛔ **`normalised_record` is 0 of 83 canonical.** The harvester's own output is not canonically serialised either,
**so "this object is non-canonical" is not evidence that it is not harvester output.** The populations are
shape-indistinguishable, and the route is closed with a number rather than an argument.

⭐ **That is the strongest form of closing an item: not "we could not find a way" but "here is the measurement
showing no way exists."** A later seat proposing shape-based derivation now meets a denominator instead of a
judgment.

## ⚠ MY OWN WIDER COUNT IS A DIFFERENT POPULATION, AND I STATE IT RATHER THAN REPORT A DISCREPANCY

My first sweep of unlabelled bronze objects returned **265**, not 18. **That is not a contradiction of the cell —
it is a different denominator.** Per segment:

| segment | bronze objects | unlabelled |
|---|---|---|
| `seeking-alpha` | 41 | **18** |
| `amgt` | 246 | 246 |
| `sec` | 1 | 1 |
| bloomberg / wsj / ft / barrons | 191 | 0 |

**The cell's population is this project's publisher bronze, where the unlabelled set is exactly 18 — matching
`AC5`'s `population_equals_missing_bucket True` at object grain.** The `amgt/` and `sec/` prefixes are other
surfaces (state, gold, the SEC ticker table) that the received-form contract does not govern. ⛔ **Reporting my
265 against the cell's 18 would have been tonight's wrong-domain shape for the fifth time, and the tell was the
segment breakdown, not the total.**

## The issuer's two wrong-domain labels, and why they were caught

Both were headed "MISSING (the 18)" and were not the 18 — one over the whole bucket, one over a wider prefix set.
**Both were caught by the printed denominator and the not-JSON count**, not by review. ⭐ **Fourth and fifth
instances tonight of a denominator catching a confident heading**, and in this round they were caught inside the
cell rather than after it.

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S17",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T05:15Z",
    "one_line": "L9 GRADE RECORD for round 4: 1 of 1 terminal, 5/0/0, zero writes and zero vendor calls; the cell classified all 18 and labelled nothing, and its decisive claim is reproduced here -- normalised_record is 0 of 83 canonical, so shape cannot distinguish the unlabelled objects from harvester output and the last derivation route for Z-S1's backward half is closed with a number.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "surprise-row-gate --acceptance AMGT_HARVST --round 4: PASS 5 / FAIL 0 / UNVERIFIABLE 0 of 5 over 1 order.",
        "Canonical-shape test run here over every labelled bronze object: normalised_record 83 objects, 0 canonical, 83 non-canonical, 0 not-JSON; as_received 16 objects, 0 canonical, 3 non-canonical, 13 not-JSON.",
        "Per-segment unlabelled census run here: seeking-alpha 18 of 41, amgt 246 of 246, sec 1 of 1, and 0 of 191 across bloomberg/wsj/ft/barrons -- so the cell's population of 18 is exactly this project's publisher-bronze MISSING bucket."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "Spine v3 L9: the CVO grades the round against the criteria that bound it.",
    "world_is": "The cell met every criterion, wrote nothing, and produced the measurement that forecloses the remaining derivation route.",
    "notes": "⚠ MY OWN WIDER COUNT IS A DIFFERENT POPULATION: my first sweep returned 265 unlabelled bronze objects against the cell's 18, and the difference is amgt/ (246) and sec/ (1) -- surfaces the received-form contract does not govern. Reporting 265 against 18 would have been tonight's wrong-domain shape a fifth time; the tell was the SEGMENT BREAKDOWN, not the total. The issuer's own two mislabelled rows were caught by its printed denominator and not-JSON count, inside the cell rather than after it.",
    "dismissal_reason": "Grade record: this row carries the round-4 L9 grade and dispositions no item; the enum has no record value."
  }
]
```
