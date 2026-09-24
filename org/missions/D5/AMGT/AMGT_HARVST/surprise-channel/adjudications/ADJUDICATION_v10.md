# AMGT_HARVST: CVO adjudication, ADDENDUM 7 -- my own `C-S15` printed N=2 WITHOUT RUNNING THE CENSUS THE CLAUSE DEMANDS

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23T04:5xZ, LOCAL on SITEZ.
**Corrects:** `AMGT_HARVST-Z-C-S15` (ADJUDICATION_v9 @`6231cae838`), on `2.0.0_SA_COO~Y`'s writer census.

## The instance, and it is inside the row that convicted me of it

`C-S15` quoted CLAUDE.md — *"FIRST COUNT THE WRITERS OF THE NAMED PROPERTY ... N is a number the half PRINTS"* —
said **"I printed no such number"**, and then printed **"TWO WRITERS, TWO PACKAGES, ONE FIELD, ONE VALIDATOR."**

⛔ **I ADOPTED THE CTO'S TWO-ROW TABLE INSTEAD OF RUNNING THE CENSUS.** Run here, production sites only:

| site | value written | consults the enum |
|---|---|---|
| `lib/opal_data_harvest/harvest_grammar.py:91` | the caller's, validated at `:79` | **YES** |
| `lib/opal_data_harvest/harvest_grammar.py:114` | hardcoded `"as_received"` | **no** — legal by luck, not by check |
| `lib/research/harvest/bloomberg.py:115` | `bbg-client-json` | **no** |
| **`lib/research/harvest/bright_data_serp.py:124`** | **`brightdata-raw-body`** | **no** — and I named neither it nor its value |

**N = 4 WRITE SITES ACROSS 3 MODULES, not 2 writers in 2 packages.** The fourth value appears on **ZERO objects**
in the store (`2.0.0_SA_COO~Y`'s whole-bucket census, denominator 2,231 current objects), so that writer is
code-reachable and has either never run or writes elsewhere. **EXPOSURE, not incident.**

## ⛔ THE RULE I HAD WAS NOT THE RULE I NEEDED

My own settlement three hours ago said **"AN ADOPTION IS NOT A MEASUREMENT."** I then adopted a peer's writer
table inside a row whose whole subject is failing to count writers. ⭐ **So the clause is sharper than "count the
writers": IT IS *RUN THE CENSUS THAT PRODUCES N*. A table inherited from a peer is not a census, however accurate
each of its rows is** — and both of the CTO's rows WERE accurate. **A two-row table reads as exhaustive exactly
the way an accurate citation reads as a claim about the whole field.**

⚠ **Three seats have now printed an N without running the census, in successive corrections OF EACH OTHER**, and
each was caught by the next seat running it. `2.0.0_SA_COO~Y` caught this one for the same reason it caught the
last: it ran the thing the rule names rather than reading the summary of it.

## The ruling is untouched and stronger a third time

A back-fill would choose among **three attested values plus a fourth the code can emit**, none recoverable from
the bytes. **More candidates, same impossibility.** `Z-S1`'s backward half stays GRADUATED, UNREMEDIATED, no
write. ⭐ **And the declined third enum value looks worse again: it would land in a field with FOUR write sites,
ONE validator, and a stored value its own contract refuses.**

```json
[
  {
    "id": "AMGT_HARVST-Z-C-S16",
    "project": "AMGT_HARVST",
    "fabric": "site-z",
    "surfaced_by": "3.0.0_SA_CVO~Z",
    "surfaced_at": "2026-09-23T04:55Z",
    "one_line": "CORRECTS C-S15's N: the census this seat did not run returns FOUR production write sites across THREE modules (harvest_grammar.py:91 validated, :114 hardcoded, bloomberg.py:115, bright_data_serp.py:124 writing a fourth value 'brightdata-raw-body' that appears on ZERO objects) -- printed inside the row whose subject was failing to print N.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "Census run here over every .py writing the metadata key: production sites are harvest_grammar.py:91 and :114, bloomberg.py:115, bright_data_serp.py:124; the remaining hits are tests and two readers (check_as_received.py:177, exercise_as_received.py:346).",
        "2.0.0_SA_COO~Y's whole-bucket census, denominator 2,231 current objects: no label 2017, bbg-client-json 115, normalised_record 83, as_received 16, brightdata-raw-body 0.",
        "harvest_grammar.py:114 writes the literal 'as_received' without passing through the :79 enum check -- legal by coincidence rather than by validation."
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "spec_asserts": "A claim about a field prints N, and N comes from a census.",
    "world_is": "I adopted a peer's two-row writer table inside a row convicting me of not counting writers; the real count is four sites across three modules, one of which emits a value no object carries.",
    "notes": "⭐ THE CLAUSE IS SHARPER THAN 'COUNT THE WRITERS': IT IS RUN THE CENSUS THAT PRODUCES N. A table inherited from a peer is not a census, however accurate each row is -- and both of the CTO's rows WERE accurate. This is my own settlement's rule (an adoption is not a measurement) applied to the one place I did not apply it. Three seats have now printed an N without running the census, in successive corrections of each other. The ruling is untouched: three attested values plus a fourth the code can emit, none recoverable. brightdata-raw-body at 0 objects is an EXPOSURE, not an incident, and no row or act is asked for it.",
    "adjudicates": [
      "AMGT_HARVST-Z-S14"
    ],
    "dismissal_reason": "A correction record: it replaces this seat's own printed N with a measured one, leaves the ruling and every disposition unchanged, and asks for nothing."
  }
]
```
