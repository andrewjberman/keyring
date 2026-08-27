# ETFS_SATELLITES.TO-2 -- ISSUER'S DISPOSITION, and the measurement that moved the evidence bar

`1.0.0_SA_CTO~Z`, 2026-08-27 ~23:4xZ. Arch-gate ruling. Two broadcasts: msg 11054 (disposition),
msg 11078 (the correction to my own 11054 section 4.1).

---

## 1. DISPOSITION: TO-1 and TO-2 are DELIVERED. No successor TO is needed to BUILD a predicate.

The board read `ACTIVE -- UNBLOCKED; WAITING ON A SEAT.` on both. **MEASURED, not taken from the
producer's self-report:**

```
dc56a72c21  0.4.0_DS_ClientPlatform~W  2026-08-27 14:14:26 -0400
            satellites_registry.py 320L · satellites_weights.py 270L · test_satellites.py 481L
            2 fixtures · TO-1 + TO-2 PROOF_OF_SPEC · 2382 insertions
7f44de8371  proofs re-pinned off PENDING-COMMIT
ON ORIGIN   origin/CLOUD and origin/SITEZ   (git branch -r --contains)
```

STOP: nothing was waiting on a seat. The work was built, proven and pushed roughly five hours before
the panel concluded the critical path had no producer. The producer's own message said
`LOCAL @dc56a72c21`; the branch-contains read says otherwise. **An UNDER-stated push state survives
review exactly as any conservative error does** -- see `conservative-error-passes-its-own-check`.

## 2. Andrew's two rulings are CONSISTENT; the file gave the right expression the wrong JOB.

| ruling | verbatim | what it settles |
|---|---|---|
| ~16:1xZ | "Some SMA that has a blend of a Satellite and Opal Model is not a Satellite, they merely are allocating to a Satellite." | IS-A vs HOLDS-A |
| ~22:5xZ | "it should simply be 'Does it say \"Opal Satellite\" in the name? Add it and track henceforth if so.'" + "if it says 'opal satellite with some other shit' that is not acceptable" + "if it is formatted as the other opal satellites then its fine" | membership is a PREDICATE, and it is ANCHORED-AND-FORMATTED |

`satellites_registry.py:213` already carries `^Opal Satellite <N>$` -- deliberately as a DRIFT ORACLE,
never as a membership test. The later ruling **promotes it**. The act is one decision, not a rebuild.

STOP: **the file's ~40-line "WHY THERE IS NO PREDICATE" section must be STRUCK, not annotated.** It
argues, with swept planes and positive controls, that no predicate can exist -- citing the ~16:1xZ
ruling that ~22:5xZ supersedes. Left standing beside the predicate it forbids, it is a
confidently-wrong mechanism, and those propagate as CITATIONS rather than as gaps
(`a-true-conclusion-without-its-mechanism-is-re-derivable-wrongly`, the mirror). A rule stated next
to its own violation launders the violation.

`:55-58` additionally says a false positive "costs one question" -- true of the oracle job, FALSE of
the predicate job. Promotion raises the correctness bar to exactly the one the file says the
expression does not meet. That sentence goes with the section.

## 3. THE MEASUREMENT THAT MOVED THE BAR -- and it reversed my own ruling section 4.1

I first ruled the negative arm sound because 21 near-miss rows exist in-corpus. Then I tested whether
they DISCRIMINATE. Over `roster_2026-08-27.json`, 65 rows, provenance claim `measured`:

```
FULL    ^Opal Satellite \d+$   (as shipped)  ->  9 matches, 0 false admits
NO TRAILING ANCHOR  ^Opal Satellite \d+      ->  9 matches, 0 false admits
NO LEADING ANCHOR    Opal Satellite \d+$     ->  9 matches, 0 false admits
NEITHER ANCHOR       Opal Satellite \d+      ->  9 matches, 0 false admits
SUBSTRING (naive)    /opal satellite/i       ->  9 matches, 0 false admits   <- RULED OUT BY ANDREW
```

STOP: **every variant scores identically, including the one the sovereign explicitly rejected.**
A green run certifies nothing about the design.

**Why, and it is subtler than "the blend row is missing":** the blend rows ARE present --
`Blended Opal / Satellite 50`, `Opal - Cash + Satellite 50`, `Opal Sat 50+ 15% cash`,
`Opal UST/Sat 80 33/67`, `Core | Satellite 98`, and 16 more. But **not one of the 21 contains the
contiguous string `Opal Satellite`.** Every one fails at the FIRST discriminator, so the leading
anchor and the trailing `$` are never reached.

> **21 near-misses that all miss the same way are ONE test run 21 times.**

`2.0.0_SA_COO~Z`'s stated fact (the blend row is absent) is refuted; their INSTINCT -- that a green
run on this corpus would look like proof -- is correct for a reason neither of us had named.

**My error class, and it recurs:** I validated on the axis I had searched (*do near-miss rows
exist?*) rather than the axis the question was about (*would a WRONG predicate score differently?*).
See `i-validate-on-the-axis-i-searched-not-the-axis-asked` and
`a-criterion-that-cannot-fail-over-its-own-window`. A row set that exists is not a control set.

## 4. BINDING ACCEPTANCE CRITERION -- synthetic fixtures, not optional

The real corpus is structurally incapable of exercising the design, so the fixture must carry:

```
MUST REJECT   Opal Satellite 50 + 15% cash   Andrew's named hazard; the ONLY probe separating
                                             the shipped form from no-trailing-anchor
MUST REJECT   Opal Satellite 50 Tax-Free     same limb, different tail
MUST ADMIT    Opal Satellite 55              proves the path DERIVES; a hardcoded list FAILS it
```

STOP: **`Opal Satellite 55` is the load-bearing row and it is a POSITIVE probe.** No negative can
distinguish a derived predicate from the old declared list -- the nine members pass under BOTH
mechanisms, which is exactly how a declared registry looks when nothing has changed. Only an admit
the list does not contain can separate them.

## 5. Constraints that travel with the promotion

1. The 21 non-canonical rows may be asserted, but they are NOT the discrimination evidence (section 3).
2. `REGISTRY_CLAIM` moves `held` -> `measured` only on the genuinely derived path; the nine hand rows
   become the POSITIVE FIXTURE and are not themselves proof -- a fixture drawn from the same 65 rows
   the predicate reads cannot discriminate.
3. **PUBLISH EMPTY, NEVER DELETE** (PT-c-2): a firm deriving zero members writes an empty set. A 404
   carries no reason, so absence must remain recoverable.
4. `RENDER_ZERO_ACCOUNT_MEMBERS` survives unchanged. `Opal Satellite 90` has zero accounts, matches
   the anchor, and IS a member. Membership is the name; rendering is not a membership question. A
   derived path that quietly drops it re-introduces the account-count heuristic Andrew disowned.

## 6. Record corrections owed by the registry owner (`2.0.0_SA_COO~Z`)

- `TO-1`, `TO-2` -> **DELIVERED**. Neither is waiting on a seat.
- The project `Blocking:` field still reads *"OPEN CALL AT ANDREW ... WHO MAINTAINS THE SATELLITE
  MEMBERSHIP REGISTRY?"* -- **DISSOLVED** by the ~22:5xZ derived ruling. A derived set has no
  maintainer; the predicate is the maintainer. That field is the last carrier still showing it open.

---

## 7. AMENDMENT 1 (same session, ~23:5xZ) -- A SUCCESSOR TO **IS** REQUIRED. I ruled the predicate and never ruled the PUBLISH rung.

Raised by `0.7.0_AE_CloudOps~Y` (msg 11088). **Upheld, and re-derived on a different instrument than
theirs, which made the finding larger.**

STOP: **section 1's "no successor TO is needed" is true of BUILDING THE PREDICATE and false as a
disposition.** The publish rung was already in my carried record as DS-lane and unowned, and I did
not rule it.

**The warning that came with it is the durable half:** the gap was invisible an hour earlier because
a STATUS FIELD said `waiting on a seat`; it can go invisible again because a RETRACTION says
`built and on origin` -- and the second is harder to see, **because the fabric has just corrected
itself toward "done".** A correction opens a new blind spot on its own far side.

**Re-derived by asking "is it wired to RUN?" rather than "does it write?":**

```
                                    __main__   write-verbs
build_dim_model_portfolio.py            1          2       <- POSITIVE CONTROL
build_dim_taxsma_report.py              1          3       <- POSITIVE CONTROL
cottonwood_aua.py                       1          0       <- see the caveat below
satellites_registry.py                  0          0
satellites_weights.py                   0          0
comp-pipescript io satellites_registry --pipeline cot-gold  ->  "Unknown script in tree"
only non-doc/test reference in the estate: test_satellites.py:24 `import satellites_registry`
```

> **No entrypoint, in no pipeline graph, imported only by its own test. That is a LIBRARY, not a
> producer with a missing step.** Every sibling is an imperative `build_*`; this one is a noun.

STOP: **the ORDER is load-bearing. Adding a write verb to a module nothing invokes ships a file that
still never runs -- and the write-verb census would go GREEN.**

**Caveat owed on the evidence, against the raising seat's own headline:** `cottonwood_aua.py` is a
real sibling producer and **also scores zero write verbs** on that pattern, so *"zero write verbs in
320 lines"* has a demonstrated false-negative and cannot carry the claim. The finding is unaffected
and better supported -- **the load-bearing limbs are the ENTRYPOINT absence and the PIPELINE-GRAPH
absence, both positively controlled**, plus their S3 outcome sweep (4,125 + 6,599 keys,
`IsTruncated=None`, zero hits).

**Ruling -- three rungs, ordered, all DS-lane (Rule 13):**

```
R1  CODE FIRST-MINT   s3://opal-data-mdpf/code/scripts/assets_gold/ -- named OUTSTANDING in TO-1's
                      own proof instance. The script is committed, not deployed.
R2  RUNNABILITY       __main__ + registration in the cot-gold pipeline graph.
R3  PUBLISH           platinum/satellites/registry.json in the FIRM'S bucket (opal-data-cot for
                      Cottonwood). NO firm segment in the key -- the firm IS the bucket.
                      PUBLISH EMPTY, NEVER DELETE. Artifact carries its own as_of (SAT-a-4).
```

STOP: **R3's empty-publish is newly load-bearing through a composition nobody designed.**
`0.7.0_AE_CloudOps~Y` removed the serving layer's synthesised empty @`24a8435642` (it failed AC3
arm 3), so a missing key is now a 403 carrying no reason. **That change and my "publish empty, never
delete" constraint were made independently; together they make the producer's empty write the only
thing between a zero-member firm and an unrecoverable absence.** Neither seat could see it from its
own side -- see [[discharging-one-hazard-can-arm-another]].

**Disposition as amended:** TO-1/TO-2 remain DELIVERED **as a computation**. A successor TO is
required, its subject is R1-R3 rather than the predicate, `2.0.0_SA_COO~Z` cuts it, and the
oracle->predicate promotion of section 2 rides in the same act on the same file.

---

## 8. AMENDMENT 2 -- the two instruments R1-R3 needs, banked so a ZERO-CONTEXT seat can execute it

`0.4.0_DS_ClientPlatform~Z` (msg 11106) stated its lane idle, **declined to self-seat**, and then
argued against its own availability: Rule 27's protected resource is the SEAT'S CONTEXT, and theirs
is several hours deep past a compaction, so a fresh seat starts with more of the thing the rule
exists to protect. **The seating is `2.0.0_SA_COO~Z`'s and this record does not decide it.**

STOP: **what the arch gate CAN do is make the fresh-seat option cheap, and that is the only reason
these two instruments are written down here rather than left in a message.** A fresh seat's
disadvantage is not context volume, it is that the method gets rediscovered. Both were handed over
for free by the seat that stood to be chosen by default.

**R2's runnability oracle -- RESOLVE BY IMPORT, NOT BY TEXT:**

```
python -c "import <module>; <module>.<SYMBOL>"     on the artifact under test
+ a deliberately-ABSENT symbol as the negative control
```
> **A grep cannot tell live code from a comment ABOUT deleted code; an attribute lookup can.**
Exercised tonight by `0.7.0_AE_CloudOps~Z` against a re-downloaded deployed zip, where it
discriminated. This is also the direct remedy for section 7's false-negative: the entrypoint claim
should be settled by import, not by pattern.

**R1's acceptance must pin to the ARTIFACT, not to the change that produced it.** R1 is the
DEPLOYED-vs-COMMITTED distinction and TO-1's own proof instance already names the S3 first-mint
OUTSTANDING. **The trap: a criterion whose structural leg was true of an EARLIER commit does not
travel to a later pin.** See [[a-control-pinned-to-a-constant-the-fix-will-move]] and
[[exercising-a-fix-proves-the-code-not-the-input]].

**Cross-reference for whoever writes R3's acceptance:** the empty-publish hazard in section 7 is a
COMPOSITION of two independently-correct changes. It is not discoverable from either file alone, so
it must travel IN THE TO TEXT rather than as a pointer.

---

## 9. AMENDMENT 3 -- R2 IS RE-SPECIFIED. Do NOT convert the library into a script.

Forced by `0.7.0_AE_CloudOps~Y` (msg 11124), who measured **their own** instrument at ~60%
false-positive after catching a `head -60` truncation in their own sweep (reported denominator 60,
true population 385).

**First, a correction on my correction.** Section 7 withdrew `cottonwood_aua.py` as a regex artifact
and said I had over-read my caveat against their evidence. **Their corrected sweep found 64 runnable
producers scoring zero write verbs.**

```
I withdrew              1 counter-example
their corrected sweep  64
```

STOP: **my retraction was a second error in the opposite direction.** I corrected toward being fair
to the measurer and thereby understated a real defect -- **guarding one direction while leaving its
mirror open, in the same message where I named the first.** See
[[guarding-one-direction-leaves-its-mirror-open]] and [[the-check-on-the-check-fails-toward-discrediting-it]].
That seat **declined the rehabilitation** rather than banking it.

**Their classification is the best form of the finding because it is POSITIVE.**
`satellites_registry.py` groups with `__init__.py`, `config.py`, `helpers.py`, `s3_layout.py` --
that says what it IS, where my AST said only what it LACKS. See
[[a-positive-formulation-beats-a-controlled-absence]].

**Independence, not overclaimed:**

```
AST capability + population classification   SAME SUBSTRATE (source tree), different questions
pipeline-graph read "Unknown script in tree" DIFFERENT PLANE (the registry)
S3 sweep, 0 artifacts across 10,724 keys     DIFFERENT PLANE (the world) -- the only OUTCOME limb
```

**THE ARCH CONSEQUENCE.** My R2 said *"`__main__` + pipeline registration"* -- i.e. convert the
module into a script. **If it genuinely groups with the library modules, that is the wrong shape:**

```
DO NOT   add __main__ + boto3 to satellites_registry.py
DO       add a PRODUCER beside it that IMPORTS it; the module stays pure
```

STOP: **the argument is NOT a naming convention** -- `cottonwood_aua.py` is a producer and is not
`build_*`, so that reasoning would not hold. **It is that the module has ZERO I/O-capable imports,
which is exactly what makes the membership predicate certifiable in isolation -- no mocking, no
credentials.** Converting it co-locates the thing that must be VERIFIED with the thing that touches
S3, and the predicate is the part carrying both a sovereign ruling and section 4's vacuous-corpus
problem. **Purity here is not tidiness; it is what keeps the synthetic-fixture arm cheap to run.**

**R1 and R3 unchanged. R2 re-specified: the runnable producer is a NEW file, and
`satellites_registry.py` is a DEPENDENCY of it rather than the subject of it.**

Push state: LOCAL at commit time (`0.0.0_AB_MSTR~Z` is the integrator and pushes).
