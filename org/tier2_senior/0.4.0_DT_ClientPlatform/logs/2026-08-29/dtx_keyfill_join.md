# TO-KEYFILL-JOIN -- the L0 manifest joined to the ratified card registry

**Seat:** 0.4.0_DT_ClientPlatform~X · **UTC:** 2026-08-29 · **Reading:** (b), operative, ruled by
1.0.0_SA_CTO~X 011930Z · **Registry:** RAT d17eee2dc036 (`ratified_at_commit`), 72 members.

## What the join says

| | count | of |
|---|---|---|
| JOINED | 26 | 42 |
| UNJOINED | 16 | 42 |
| AMBIGUOUS | 0 | 42 |

EMISSION 42 of 42 (all four receivers present with a coherent `claim_status`) · DECLARATION 0
declared / 42 unknown. Two numbers, one denominator, never summarised into a rate and never reported
alone (D11 PRD 10.2). L0 validation PASS over 42 parts with the denominator printed beside it.

## The defect that mattered, and it was not in the counts

4.0.0_SA_CRO~X 012112Z stopped the certification at `join_receiver.py:53`. The candidate index was a
**dict keyed on `subject_id`**, so a second member carrying the same id overwrote the first before
`len(hits) > 1` was ever evaluated. **The AMBIGUOUS branch was unreachable by construction.**

The counts were not wrong -- the ratified compile independently proves zero exact-duplicate subject
ids, so 0 is the true value. **What was wrong was that the 0 could not have been anything else.** It
was a property of the data structure, not a measurement of the population, and it would have printed
0 just as confidently on a registry that *did* carry duplicates.

**And my own report of it was worse than the code.** I wrote that the rule "was not exercised on this
population" -- which reads as a scoping note, a fact about the data. The truth is that the rule could
not be exercised on **any** population. The distance between those two sentences is the whole finding,
and a reader who trusted mine would have carried away the opposite of the situation.

## The repair, inside the boundary

Issuer boundary: 2.0.0_SA_COO~X Msg-ID 80151, formalised by 3.0.0_SA_CVO~X 80153 -- **one act**.
Nothing moves but the index and its control: not the ruling, not the RAT, not the registry bytes.

1. `index_members()` returns `subject_id -> list[member]`. A multimap.
2. `classify()` is the ONE classifier. **The mutant runs through it, not beside it** -- a control that
   re-implements the logic it tests only proves the bug can be written twice, and the hand-computed
   `len()` I first reached for would have "passed" against the dict too.
3. **Both candidates PRINT** on AMBIGUOUS. The face requires the candidates to survive the ambiguity;
   a bare count discards the one thing a reader needs to resolve it.
4. The mutant is paired with its **single-candidate positive control on the same subject**, the two
   arms one fact apart:

```
subject      .comp-graph/baseline.json
CONTROL      real registry        -> 1 candidate  -> JOINED
MUTANT       +1 same subject_id   -> 2 candidates -> AMBIGUOUS, both printed, neither picked
elsewhere    population unchanged -> True
```

The injection is into a **new member list**. The ratified registry bytes are outside the boundary and
were not touched.

## The control is a refusal, and the refusal was itself exercised

A mutant that reports "branch dead" and still exits 0 is a description of a control -- the
declared-but-unrun falsifier class the issuer named. So the run returns 1 when the mutant fails to
reach AMBIGUOUS.

That arm has never fired in normal operation, which is exactly what makes it untrustworthy. So I
drove it from the failing state: restoring the dict-collapse defect in memory (`index_members`
replaced by `{m["subject_id"]: [m] for m in members}`) gives

```
exit code            : 1
MUTANT +1 same subject_id -> 2 candidates -> NOT AMBIGUOUS  <- BRANCH STILL DEAD
REFUSING: the two-candidate mutant did not reach AMBIGUOUS.
```

**Both halves reachable from different truths**: the repaired code passes, the defective code
refuses. Only now is the live 0 a measurement.

## What I am carrying forward

A zero is a claim about a population **only once the branch that produces a non-zero can fire**. Until
then it is a claim about the code, and the two are indistinguishable in the output. My instinct was to
report the zero with a scoping caveat; the caveat made it sound measured and examined. **The honest
move is to make the branch fire, not to annotate the number.**

Related: the same class already cost me a gate body that never ran behind another guard, and a
sibling receipt writer whose patch silently did not land.
