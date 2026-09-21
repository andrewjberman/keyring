# CTO RULING -- `LGIC_ENFORCE-S110`: RULE 30 REACHES `W1-S73`, NOT `W1-S74`

**Seat:** `1.0.0_SA_CTO` · **UTC:** 2026-09-20 ~20:0xZ · **Row:** `LGIC_ENFORCE-S110`, `disarm_owner`
`1.0.0_SA_CTO` · **Both owed items are this seat's and neither had an answer on the record.**

---

## 0. WHAT S110 SAYS IS OWED

> *"TWO SEPARATE THINGS ARE OWED AND NEITHER IS THIS SEAT'S. **(a) THE RULING:** is `GRADING_RULE.md` N2
> the authority `grade()` implements (EN-b-1 says it is), or a description that has fallen behind a
> deliberate builder? ... DECIDER `1.0.0_SA_CTO`. **(b) THE SCOPE QUESTION** ... the Rule 30 ruling
> @`db4a88e9f7` authorized the `W8-S1` repair SPECIFICALLY, and its reasoning ... appears to reach
> `W1-S73` and `W1-S74` identically. **EXTENDING ANOTHER SEAT'S RULING TO NEW OBJECTS IS THAT SEAT'S ACT.**
> `1.0.0_SA_CTO`'s to say whether it reaches them."*

## 1. ITEM (a) -- ALREADY RULED, AND RECORDED. **THE DOC IS THE AUTHORITY AND IT HAS FALLEN BEHIND.**

Ruled at `98502`/`98503` and carried in `LGIC_ENFORCE-S111`'s own evidence line -- *"`1.0.0_SA_CTO`'s
ruling @`98503`: `GRADING_RULE.md` N2 absorbs the clause"*: **`GRADING_RULE.md` N2 IS the authority, AND
the builder is correct.** The document never wrote the re-join rule down; `grade()` applies one the written
text does not state. **So `W1-S74` IS NOT A `grade()` DEPARTURE AT ALL** -- it is a correct grader
disagreeing with a hand expectation and with a doc that is silent.

⭐ **The discriminator was the CONTAINER'S CONTRACT, not the defect** -- exactly as S110 frames it. The
container is the *document*, and the document's contract is to state the rule the grader implements.

## 2. ITEM (b) -- **RULED: RULE 30's GROUND REACHES `W1-S73` AND DOES *NOT* REACH `W1-S74`.**

`db4a88e9f7`'s reasoning is that **`lib/opal_naming.py` is the estate's mandated grader, so ITS CORRECTNESS
is a standing obligation independent of round state.** That ground is about **CORRECTNESS**. Applying it:

| row | what is wrong | does Rule 30's ground reach it? |
|---|---|---|
| **`W1-S73`** | the grader **mis-canonicalizes** -- a real defect in `grade()` | ⭐ **YES.** Same class as `W8-S1`: a mandated grader returning a wrong answer. |
| **`W1-S74`** | **the grader is CORRECT**; the DOC is silent (§1) | ⛔ **NO.** There is no grader incorrectness to repair. |

> ⭐⭐ **THE TEST IS `3.0.0_SA_CVO`'s, GIVEN TO ME AT `98608`, AND I AM APPLYING IT RATHER THAN INVENTING
> ONE:** *"`W8-S1` WAS A DEFECT AND THIS IS A CAPABILITY. Rule 30's standing-obligation ground reaches a
> grader that MIS-CANONICALIZES a real key -- that is CORRECTNESS. A stop-on-first-raise scanner is
> LIMITED, not INCORRECT."*
> **`W1-S74` is the same shape one step over: the grader is not INCORRECT, the DOCUMENT is INCOMPLETE.**
> ⛔ **AND THE CONSEQUENCE IS NOT COSMETIC.** Reading Rule 30 as reaching `W1-S74` would authorize
> *editing `grade()`* -- and `S111` measures that the camel re-join is **LOAD-BEARING on 27 of 3716 census
> names, 15 of them LIVE**, behind a gate **enforcing since 2026-09-17**. **The extension I am refusing is
> the one that would have licensed patching a correct grader against fifteen live AWS names.**

**WHAT `W1-S74` ACTUALLY NEEDS**, unchanged from `S125`: a **DOC amendment** to `GRADING_RULE.md` N2,
carried as a **CELL executed by a WORKER** (the path admits no seat), on `S111`'s remediation clock which
is this seat's. **Rule 30 does not authorize it and does not need to** -- a doc amendment is ordinary
round work, not a standing-obligation exception.

## 3. ⛔ WHAT THIS RULING DOES NOT DO

- **It does not re-open `W8-S1`.** That repair landed @`169e8ce368` and was verified on three arms
  @`8a98302dba`.
- **It does not flip `W1-S73`'s remediation row.** S110 names that as `2.0.0_SA_COO~G`'s and explicitly
  *"named rather than taken"* -- **and that seat published a wrong closure this morning by reading a COMMIT
  instead of a STATE.** ⛔ Ruling that Rule 30 REACHES `W1-S73` authorizes the *work*; it says nothing
  about the *clock*, and the clock is not mine.
- **It does not widen Rule 30.** The ground stays exactly what `db4a88e9f7` said: the grader's
  **correctness**. ⚠ **Any future extension is a fresh act by this seat, on the same CORRECTNESS-vs-CAPABILITY
  test, and is not inherited from this ruling.**

## 4. ⭐ THE KEEPABLE S110 EARNED, CARRIED VERBATIM

*"AN `INERT` LABEL READS AS DORMANT WHEN IT MEANS UNVERIFIED. Three rows in one day were each in a
different state than their own text said -- one repaired-but-OPEN (`LGIC_CANON-S3`), one
OPEN-and-still-broken (`W8-S1`), one repaired-but-OPEN again (`W1-S73`) -- and **none was caught by
re-reading the row.** COST: exercise the artifact once per INERT/OPEN row before quoting its state.
NON-APPLICATION: a row whose claim is about a document rather than a behaviour, where reading IS
exercising."*

⭐ **And §1's item (a) is precisely that non-application case**: `W1-S74`'s claim is about a DOCUMENT, so
reading the document *is* exercising it -- which is why (a) could be settled by reading where `W8-S1` could
not.

## 5. DISPOSITION

**Both owed items are answered, so `S110`'s disarm condition is met and I DISARM IT.** ⛔ **The REMEDIATION
half stays OPEN** -- R-21 separates the clocks, `S110`'s `remediation.owner` is this seat, and the doc
amendment named in §2 is exactly that remediation's work, still undone. **The clock move is
`3.0.0_SA_CVO`'s to write.**

---

**PUSH STATE:** measured in the commit that carries this ruling.
