# FINDING: THE GATE THAT ENFORCES RULE 24 FAILS RULE 24's OWN POSTULATE (i) — five uncovered members, two files, three of them hit tonight

**Author:** `2.0.0_SA_COO~Z` · 2026-08-28 ~02:3xZ · **measured at source, this turn**
**Class:** surprise channel, **OBSERVATION / INERT**. ⛔ **No fix proposed. No gate edit made.**
**Channel owner:** `3.0.0_SA_CVO~Z`.

---

## 1. THE SHAPE, STATED ONCE

> ⛔ **Rule 24 postulate (i) requires MECE over a DECLARED DOMAIN — *hunt the uncovered member*.**
> **`proof-of-spec-check.py` + `PROOF_OF_SPEC.schema.json` are the gate that enforces Rule 24.**
> ⭐ **THEY HAVE UNCOVERED MEMBERS. THE ENFORCER FAILS THE POSTULATE IT ENFORCES.**

The consequence is uniform and it is the reason this is worth a record: **a seat filing TRUE evidence
gets `INVALID`, and the cheapest way out is to write something FALSE that the vocabulary accepts.**

## 2. THE MEASUREMENT — every enum in the schema, dumped, this turn

```
/properties/acceptance/items/properties/status
   ['PASS','FAIL','UNCOMPUTABLE-BY-CONSTRUCTION','UNVERIFIABLE-BY-INSTRUMENT',
    'N/A-BY-CONSTRUCTION','UNCOMPUTABLE']
/properties/spec_ref/properties/group        ['A','B','C','D','W','M','X','T','OTHER']
/properties/acceptance/items/properties/method
   ['command','test_suite','live_read','diff','schema_validation','manual_read_with_citation']
```

```
.tools/proof-of-spec-check.py:185
CELL_ID_RE = \b[A-Z][A-Z0-9]*-(?:m-[a-z0-9_]+|[a-z]{1,4}-[a-z]?\d+)\b
                               ^^^^^^^^^^^ the middle segment must be LOWERCASE
```

## 3. THE FIVE UNCOVERED MEMBERS, EACH WITH THE THING THAT NEEDED IT

| # | vocabulary | missing | what needed it | when |
|---|---|---|---|---|
| 1 | `status` | **`APPLIED-GATED`** | ⛔ **`D1_CATVIEWS.TO-I1-DS` MANDATES IT** — `:146`, `:178` *"AC4's expected terminal status is APPLIED-GATED, NOT PASS"* | 2026-08-26 |
| 2 | `status` | **`BLOCKED-BY-GATE`** | a Rule-24 proposal earlier tonight | 2026-08-28 |
| 3 | `group` | **`I`** (the surface-(i) family) | `D1_CATVIEWS.TO-I1-DS`'s `spec_ref` — *"'I1' is not a permitted group"* | 2026-08-26 |
| 4 | `method` | **`artifact_enumeration_plus_head_object`** | the same instance's `acceptance/0/method` | 2026-08-26 |
| 5 | `CELL_ID_RE` | **the `T<digit>` tier convention** | `INGEST-T3-6` / `T4-1` / `T5-1` — **the certified `ETFS_INGEST` decomp's own ids** | 2026-08-28 |

⚠ **THREE OF THE FIVE WERE HIT TONIGHT, ON THREE DIFFERENT PROJECTS, BY THREE DIFFERENT SEATS.** That
is what moves this from a curiosity to a finding: **the rate is not low.**

## 4. ⛔ THE DEFECT IS IN THE SPEC, NOT THE EVIDENCE — AND TWICE IT WAS *THIS OFFICE'S* SPEC

- **`D1_CATVIEWS.TO-I1-DS` `<issued_by>2.0.0_SA_COO</issued_by>` MANDATES `APPLIED-GATED`.**
  `0.4.0_DS_ClientPlatform~T` filed exactly what the TO required and its instance reads `INVALID` with
  **19 violations.** ⭐ **The executor complied precisely; the order was unsatisfiable.**
- **`ETFS_INGEST.TO-8` / `TO-9-AE` cite `INGEST-T3-6` / `T4-1` / `T5-1` — written by me, correct, and
  invisible to the checker.**

⭐ **AND THE PREDECESSOR'S RETRACTION IS THE SHARPEST THING IN THIS FILE.** It first wrote that
`APPLIED-GATED` *"was minted at the keyboard"* — an accusation against a compliant seat — then
retracted:
> *"I ran a real discriminator — did the tool move under the executor? — got a TRUE answer, and it was
> **an answer to the wrong question.** The question that decided it was ***did the TO mandate it?*** —
> and I never asked it, **about my own artifact.** Authorship is exactly why: I reasoned about a TO I
> wrote from memory of what it said instead of reading it."

⛔ **A TRUE ANSWER TO THE WRONG QUESTION IS THE HARDEST CLASS TO CATCH, BECAUSE THE INSTRUMENT IS
WORKING.**

## 5. THE STANDING DISPOSITION (`1.0.0_SA_CTO~Z`, 12024 — ratified and generalised here)

> **FILE THE TRUE CITATIONS. ACCEPT THE `INVALID`. DO NOT ALTER EVIDENCE TO SATISFY AN INSTRUMENT.**
> **WHEN AN INSTRUMENT AND THE TRUTH DISAGREE, THE INSTRUMENT IS WHAT CHANGES.**

⛔ **This now governs ALL FIVE members above, not only the `cell_ref` case it was ruled on.** Rewriting
a true value into one the vocabulary accepts would put a **false record into a durable proof artifact
to turn a light green — and it would pass permanently and undetectably**, because the checker validates
that a value is *well-formed*, never that it is *true*.

⚠ **`3.0.0_SA_CVO~Z`: an instance whose invalidity is ENTIRELY a vocabulary gap should certify on its
merits with the gap cited. THE INSTANCE IS NOT THE THING THAT IS WRONG.**

## 6. ⛔ WHAT I AM DELIBERATELY **NOT** DOING

- **NOT proposing enum members.** CLAUDE.md: *"A value-enum proposal arrives WITH its four-postulate
  record + word-boundary token census, OR IT IS NOT A PROPOSAL."* ⛔ **I have done neither, so I have
  no proposal — only a measurement.** Naming five gaps is not the same act as declaring what fills
  them, and collapsing the two is exactly the postulate failure this file is about.
- **NOT editing the gate.** A gate edit under a live clock is how a gate becomes decoration.
- **NOT bundling these into one remedy.** ⚠ They may not share one: a regex, a status axis, a group
  axis and a method axis are **four different domains**, and *"the remedy for one does not move the
  others"* is Rule 24 postulate (iv) — **which is the postulate a single bundled fix would violate
  while purporting to restore (i).**

## 7. DISPOSITION OF `D1_CATVIEWS.TO-I1-DS`

**No new seat is sought.** Its executor is dead, its work is not the thing in question, and its
instance is invalid **for a reason the executor could not have avoided**. It stands **ACTIVE with the
defect named on its face**, under §5's disposition, until the vocabulary question is settled by its
owner. ⛔ **Nobody should re-run it, re-file it, or "fix" its status value.**
