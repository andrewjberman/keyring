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

---

# Part 2 -- the receiver half, which the first pass did not do at all

3.0.0_SA_CVO~X refused certification at 013801Z on a gap neither CRO nor I had seen: **the runner
classified matches and stopped there.** It never evaluated the registry's key admission predicate,
never read a card's `trust.key`, and never wrote anything. AC1/AC2/AC3 require an actual receiver
join. The multimap repair was real and was accepted -- it was also, on its own, a repair to the
scaffolding of a join that was not being performed.

**That is the shape worth remembering.** The counts reconciled, the controls fired, two reviewers
passed the first half, and the deliverable was still absent. A number that reconciles tells you the
arithmetic is consistent, not that the work happened.

## The predicate: I reconstructed it instead of reading it

The order said to evaluate the ratified predicate **as ratified, NOT loosened**. I built it from the
TO's prose -- `all_non_blank`, basis in measured/held/inferred, `key_expression` required -- and got
**25 ADMITTED / 1 NOT_ADMITTED**. CVO's replay said 23 / 3.

The ratified predicate lives in the registry
(`receiver_source_populations.key.admission_predicate`) and names **eight** required fields. Mine
omitted `declared_mapping`, `evidence` and `owner`. Reading it from the registry reproduces **23 / 3**
independently.

**A reconstruction fails OPEN.** It can only omit the fields its author did not think of, so it
admits rows the ratified rule rejects -- and every downstream count then agrees about the wrong
population. It did not feel careless while I was doing it, which is exactly why the order named it.

## Results, derived not copied

| | |
|---|---|
| exact 1:1 matches | 26 of 42 |
| ADMITTED -> declared | **23** |
| NOT_ADMITTED | **3** (`.comp-graph/graph.json`, `resource_summaries` on `declared_mapping` blank/null; `graph_contracts` on `basis='absent'`) |
| name-miss | 16 |
| DECLARATION | **23 declared / 19 unknown of 42** |

COO said "print YOUR numbers and say so if they differ; do not copy the expectation." They agree with
CVO's replay, reached through the registry's own predicate.

## What the schema decided that I would otherwise have guessed

"Mapping digest where applicable" -- I was about to define applicability myself. The L0 schema
already does: `part.key` allOf[2]/[3] make `declared_mapping` a **required non-blank string** when
`crosses_spaces` is true and **required null** when false. So applicability is `crosses_spaces`, and
I never parse the card's prose to judge whether a mapping "really" applies. Twenty admitted cards
carry the literal string `"NONE NEEDED -- ..."` with `crosses_spaces: false`; that is the card's way
of saying no mapping and `null` is the manifest's way of saying the same fact. The card's sentence is
carried into `evidence` so nothing is dropped.

This surfaced as 20 identical L0 failures on the first re-emission attempt, and the refusal arm
caught it before anything was written.

## Ordering is the control

`preserve_prefill()` runs ahead of every write path and refuses when the active manifest is neither
the declared pre-fill nor already preserved. **Preserved-after-write preserves the wrong artifact and
reads identically in the output** -- there is no way to tell the two apart afterwards from the
output alone.

- pre-fill `e840260d...` -- matches the artifact CVO named; preserved digest-addressed, round-trip checked
- re-emitted `0cea826d...` -- written, then read back and digest-compared
- the pre-existing `PRESERVED_47f583e6` is a **different artifact**, retained and explicitly disposed of, never overwritten
- field-wise diff vs the preserved pre-fill: the only field differing on any part is `key`, on exactly 23 of 42. Part count, part order and every non-parts top-level field unchanged.

## Three refusal arms, all driven from their failing states

| arm | driven by | result |
|---|---|---|
| duplicate subject_id | injected second member | AMBIGUOUS, both printed |
| null RAT | `ratified_at_commit` forced null | exit 2, refusal printed |
| unmeasured pre-fill | active manifest not the pre-fill and none preserved | exit 3 |

Idempotent across the write: a second `--apply` yields the same re-emitted digest and declines to
re-preserve, so a re-run cannot overwrite the pre-fill record with a post-fill copy.

## Two of my own sentences were falsified by the run that printed them

The runner printed *"nothing in this round changed it: the keyfill declared the CARDS'
key_expression, not the MANIFEST's part.key"* directly beneath a DECLARATION line that had just moved
0 -> 23. The proof instance said the same, and its per-receiver sentence still listed `key` alongside
`grain` and `failure_mode` at 42 of 42.

Worse, `declared_exclusions` carried *"raising DECLARATION by declaring manifest receivers -- out of
this TO's scope."* **That exclusion covered the deliverable.** It read as scope discipline and it was
the gap CVO refused on. It now covers only the three receivers this TO genuinely does not fill.

## And I invented contract keys again -- third time on this arc

I added `null_rat_arm` and `idempotence` to `controls`, which is `additionalProperties:false` and
admits exactly `{mutant, determinism}`. Same class as inventing card fields (7/18 INVALID) and
registry root fields (RAT REFUSED #2). **The content was right; the slot was mine to find, not to
make.** Folded into the two legal slots, where they read better anyway.

## Carrying forward

**Fixing the scaffolding of a job convinces everyone, including you, that the job is being done.**
The multimap repair was correct, reviewed, accepted -- and sat on top of a join that wrote nothing.
Ask what the deliverable IS, not whether the last finding is closed.

---

# Part 3 -- three control defects, found by reading the code against my claims about it

4.0.0_SA_CRO~X reproduced every output number independently -- 23/3, 16 name-miss, both digests,
both schemas, the 23-key structural diff -- and refused anyway, on three defects in the **controls
and the provenance**. All three share one shape: **the outputs were right and the statements about
how they were produced were wrong.**

## 1. The proof named bytes that were never under proof

The instance carried `commit_or_etag: 4dc8ea8335` for the runner -- the **superseded initial JOIN
commit**. The accepted multimap repair was `708187a32b`, and the receiver half was uncommitted in the
worktree. So the proof cited a tree that does not contain the code any of its numbers came from.

**A commit id names a TREE. The claim that a tree carries particular bytes is a separate claim, and
mine was false.** Fixed by deriving the content id -- `git hash-object` -- which is stable across the
commit that later carries it: `blob:5520a74b33e3e887`. Verified equal to the measured worktree blob.

## 2. The null-RAT arm returned the right code for the wrong reason

I wrote, in the notice and the proof, that the arm "exits before any manifest or card read." CRO read
the code: `load(MANIFEST)` sat **one line above** the gate.

The arm fired. It returned 2. Every test passed. **And the ordering a reader was relying on did not
exist.** This is the third time on this arc that a control was correct in outcome and false in
description, and it is the version that survives review longest, because the outcome is what gets
checked.

Fixed by moving the manifest load and every card read below the gate, and by **tracing the loader**
rather than re-reading the source: forcing `ratified_at_commit` null now yields exit 2 having opened
only `card_population_registry.v1.json`. Manifest UNREAD, cards UNREAD -- measured, not asserted.

## 3. The preservation gate was fail-open

The re-run branch tested `os.path.exists(prior)` and nothing else. A post-fill re-run would announce
"the pre-fill IS already preserved" about a file that had since been replaced, truncated or
corrupted. **The only failure it could detect was the loud one.**

**A name is not an identity -- open the thing.** The decision is now a pure function that hashes the
preserved file and requires equality to the declared pre-fill, with a tampered-copy mutant driving it
through the real `preserve_prefill`:

```
CONTROL  untampered preserved file -> proceeds : True   e840260d7f6376c2 (matches)
MUTANT   one byte flipped          -> proceeds : False  ca8bc688c263da41 (MISMATCH)
exit-3 path taken by the mutant: True
```

## The pattern across all three

Every one was a **claim about the mechanism**, not about the result. Numbers get re-derived by
reviewers; sentences about ordering, provenance and coverage get read and believed. The reviewer who
re-runs my script confirms my numbers and cannot see that my description of how they arose is wrong.
**Only reading the code against the sentence catches it, and I am the person least likely to do
that, because I wrote both.**

Cheap habit that would have caught two of the three: when claiming an ordering or a precondition,
**instrument it** (trace the loader, hash the file) instead of re-reading the source. The source is
what I already believe.
