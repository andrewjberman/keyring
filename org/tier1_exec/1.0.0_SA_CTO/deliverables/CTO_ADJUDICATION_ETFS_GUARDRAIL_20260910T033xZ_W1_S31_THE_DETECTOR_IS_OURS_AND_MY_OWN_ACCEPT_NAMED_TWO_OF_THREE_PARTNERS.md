# CTO ADJUDICATION -- ETFS_GUARDRAIL, row W1-S31: PLACEMENT

**Seat:** `1.0.0_SA_CTO` · **Stamp:** 2026-09-10 ~03:3xZ · **On:** `2.0.0_SA_COO` msg 94940, "FOR PLACEMENT,
outside ETFS_GUARDRAIL's surface" · **Row:** `ETFS_GUARDRAIL-W1-S31`, OBSERVATION/ARMED, drained @`45d6ca6de4`
· **Lands as:** PRD v0.6 (FWD-4 ACCEPT amended, S16 amended, S19 + S20 added, R-EG-2 recorded)

---

## THE CALL

```
+-- CALL 1 of 1 ------------------------------------------------------+
  **Where does W1-S31 go: inside ETFS_GUARDRAIL, or out to a brief?**
  A partner producer writes PRICED values onto non-trading days, and the coverage
  classifier returns class A and `continue`s BEFORE it ever checks whether a slice
  exists -- so the check that protects FWD-4 cannot see FWD-4's violation.
  ----------------------------------------------------------------------
  **REC --** SPLIT IT. The producer is outside; the classifier is ours.
  ----------------------------------------------------------------------
  **RULING -- SPLIT, and the half that is ours is the DETECTOR, not the data.**
+----------------------------------------------------------------------+
```

## 1. THE PLACEMENT

The COO routed this as *"outside ETFS_GUARDRAIL's surface"*. **Half of it is.** The partner producer that
carries priced values forward onto closed days (`daily/inflection/` for 09-05, 09-06, 09-07 -- one value-sha
across those and 09-08, differing from 09-04; `LastModified` three days before the September run, so nothing
this project did wrote them) is not an OWNS surface. s.3 OWNS names the catch-up inside `cot-etf-ownership-daily`
and `bd-49f-etf-ownership-daily`; this producer is neither. Spine v2.4 forbids routing an outside remedy into a
running project, and I am not routing it. **S20 PLACES it so it is not carried: the remedy leaves as a brief to
`4.0.0_SA_CRO` and enters at L1 as its own project.**

**The other half is squarely inside.** s.3 OWNS names *"the coverage classifier"* in as many words, and row S4
is FWD-4's own code row against `data/etfs/scripts/coverage/classifier.py`. I re-read the cited lines with my
own instrument before ruling: at `:122-125` the non-trading-day branch sets class A and `continue`s, ahead of
the presence check at `:128`. The function's own docstring says *"only PRESENCE of a key matters here"* -- and
presence is exactly what that branch never reaches. **A defect in the instrument this project OWNS does not
become an outside matter because the data that exposed it came from elsewhere.** It goes to round 3 as S19.

## 2. THE HALF THAT IS MINE, and it is the one that would have cost a false grade

**FWD-4 was one row away from grading REALIZED on a violation.**

Row S16 is FWD-4's ONLY grading row. It was written and ratified at this seat. Its arms:

| arm | what it reads | what it would have said tonight |
|---|---|---|
| the classifier's class for 2026-09-07 | class A, "market closed" | PASS |
| no slice for **cottonwood or 49financial** | true for both | PASS |
| the date appears in no partner's holes | true | PASS |
| `expected_empty` carries it, holes unaffected | true | PASS |

Every arm passes. And four priced rows sit on that date under **`inflection`** -- the third partner, which the
arm never names -- behind the one classifier branch that cannot see a slice. A closed day is carrying numbers
nobody measured, which is precisely and only what FWD-4 exists to prevent.

This is Rule 22's ordering in a single row: **DISCRIMINATION passing inside a wrong COVERAGE**, with a second
instrument agreeing about the same wrong thing. It is the **fourth instance tonight** of the uncovered member
of a hand-typed domain -- `NFRA_OUTSET-S36`, `NFRA_COMPEFFICACY-W1-S2`, the COO's own arm (d), and this -- and
the first found in an **ACCEPT** rather than in a worker's arm. That is worse, not better: a worker's arm
produces a finding somebody reads, and an accept is the thing a GRADE is read against. Had the round closed on
S16 as written, FWD-4 would carry REALIZED in a grades file and the estate would have a signed statement that a
property is held, at the moment it is broken.

**The law it earns, and it is general:** *a partner list typed by a human is a DECLARED DOMAIN and must be read
from the artifact that owns it.* The COO reached the same rule from its arm (d) and re-cut @`005667015a`. Mine
needed the same cut and now has it.

## 3. WHAT v0.6 CHANGES

- **FWD-4's endpoint ACCEPT** -- "nothing is invented" is measured **on the slice plane across every partner the
  artifact itself lists**, never by the classifier's own class and never against a hand-typed list. A closed day
  carrying priced rows FAILS the outcome even when every classifier arm reads clean.
- **S16** -- enumerates every partner from the artifact's own list, prints that list as its denominator, reads
  each for presence AND for priced rows. The classifier's class-A reading is retained as CONTEXT and is
  explicitly **not** the discriminator.
- **S19 (new, round 3, inside)** -- the classifier reports a closed day carrying a slice DIFFERENTLY from a
  closed day carrying nothing. The shape is the assignee's; the DISCRIMINATION is the bar. Test built from the
  producer's own output on 2026-09-07, not from the docstring. Positive control: a genuinely empty closed day
  still classifies A and still appears in no partner's holes. The ZERO-vs-MISSING contract S4 protects is not
  disturbed.
- **S20 (new, placement only, NOT a cell)** -- the producer's carry-forward, named, with its exit to L1.

Until S19 lands, the condition is **disclosed** rather than repaired, and FWD-4 grades on the disclosure -- never
on the producer's silence.

## 4. WHAT DOES NOT MOVE

Nothing terminal re-opens. No round is rewound. The `aj@` constraint (Andrew-direct ~02:5xZ) is untouched and
unaffected -- S19 and S20 are read-and-classify work that reaches no mailer. This seat's standing hold on any
invocation that can reach the ETF mailer's send path stands exactly as written.

## Push state
LOCAL on commit; `origin/CLOUD` @`c6bcb7b12b` (this seat's `ls-remote`, 03:22Z).
