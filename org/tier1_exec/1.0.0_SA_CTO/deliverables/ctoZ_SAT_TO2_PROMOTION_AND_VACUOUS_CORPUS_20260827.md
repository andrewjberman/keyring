# ETFS_SATELLITES.TO-2 -- ISSUER'S DISPOSITION, and the measurement that moved the evidence bar

> ⚠ **THIS FILE'S NAME CONTAINS `VACUOUS_CORPUS`, AND THAT CLAIM IS WITHDRAWN AS OVER-BROAD --
> SEE SECTION 11.** The corpus is NOT vacuous: the predicate's `Opal` token discriminates 18 rows.
> Only the two ANCHORS are unexercised. **NOT RENAMED DELIBERATELY:** this path is cited by commit
> hash in six broadcasts and in `2.0.0_SA_COO~Z`'s and `3.0.0_SA_CVO~Z`'s records, and a rename
> would trade one stale carrier for a set of dangling citations. **A filename is a carrier that
> cannot be amended in place -- which is an argument for naming records after their SUBJECT rather
> than after their FINDING.**

---

# ⛔ READ THIS BLOCK FIRST -- WHAT IS BINDING NOW

**This record has NINE amendments and several WITHDRAW earlier sections. It is chronological, so a
reader who starts at section 1 will meet superseded rulings before their corrections.** This block is
the current state; the sections below are the reasoning and the history.

| # | BINDING NOW | where | superseded |
|---|---|---|---|
| 1 | `TO-1`/`TO-2` are **DELIVERED as a COMPUTATION** -- built, proven, on origin @`dc56a72c21` | §1 | — |
| 2 | A **successor TO IS required** (`TO-5-DS`, cut @`9de78405e8`) for R1-R3 | §7 | §1's "no successor needed" |
| 3 | `satellites_registry.py` is a **CONFORMANCE CHECKER**, not a producer. **USE it; do not convert it** | §10a | §7's "producer missing a step" |
| 4 | The producer is a **NEW file** supplying **S3 FETCH + JOIN + WRITE**; the join is **unwritten code** | §10a | §8/§9's "wire it up" |
| 5 | It must **CALL** `assert_no_drift`, `vintage()`/`FRESHNESS_BASIS`, `assert_no_baked_verdict` -- never reimplement | §10b | — |
| 6 | Wire shape: **`{ books: SatelliteBook[], as_of }`**; injection stays a bare array; adapter unwraps `.books` | §12 / §12a | — |
| 7 | **`as_of` is NON-NULL ALWAYS**, including when `books` is empty -- the pull date, never `null` | §12b | — |
| 8 | **`SatelliteBook.code` = the CANONICAL NAME** verbatim; `model_id` rejected on grain mismatch | §12c | — |
| 9 | `AC4` = **three rows**: real `Core \| Satellite 98` REJECT, synthetic `Opal Satellite 50 + 15% cash` REJECT, synthetic `Opal Satellite 55` **ADMIT** | §4 / §11 | — |
| 10 | **PUBLISH EMPTY, NEVER DELETE.** Since @`24a8435642` there is **no fallback beneath the producer** | §7 / §10c | — |
| 11 | **AMENDED 2026-08-28 ~01:3xZ -- DO *NOT* STRIKE THE SECTION.** Strike its **TITLE** and its **CONCLUSION**; **KEEP the measured sweep** (roster 21 fields; detail 84 files / 121 child nodes / 0 matches / **18 of 18 positive controls resolving**) -- that evidence is what makes Andrew's name-route ruling legible, and a blanket strike destroys it. ⛔ **`:54-58` is ACTIVELY INVERTED against his ~22:5xZ word** ("the canonical name form is wrong and Andrew ruled it so") and must be corrected in the same edit -- a strike would have removed it without anyone noticing it had been wrong. Remedy narrowed because the original row was written before the section was read at line level. Ruling msg 11583, supersession msg 11588. | §2 | supersedes this row's own "Strike" remedy |

**WITHDRAWN, do not cite:** section 3's *"a green run certifies nothing about the design"* (§11 --
the token IS exercised, +18 rows; only the anchors are not) · any sentence of mine calling the
empty-publish hazard *"closed with existing code"* (§12a -- that green result was TO-1's weights
carrier; **`T5DS-AC3` is UNCERTIFIED**).

---

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

> ⛔ **THE SENTENCE THAT STOOD HERE -- *"a green run certifies nothing about the design"* -- IS
> WITHDRAWN AS OVER-BROAD. SEE SECTION 11.** The five variants above all contain the token `Opal`, so
> their agreement was guaranteed before the run. Per-limb: the TOKEN is EXERCISED (+18 rows), and only
> the two ANCHORS are unexercised (+0). **The numbers in this table are correct; the generalisation
> drawn from them was not.**

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

> ⛔ **THE CAVEAT ABOVE IS FALSIFIED -- SEE SECTION 13. `cottonwood_aua.py` IS NOT A PRODUCER**
> (`get_object` at :118 and :147; `main()` derives and prints; no write call anywhere). I called it a
> producer **without measuring it**, from its name and location. The raising seat's write-verb result
> was CORRECT about this file. **The conclusion of this section -- that the entrypoint and
> pipeline-graph limbs are the load-bearing ones -- stands; only this counterexample is void.**

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

STOP: **the argument is NOT a naming convention** -- ⚠ *the example given here for that, that
`cottonwood_aua.py` is a non-`build_*` producer, is FALSIFIED in section 13: it is a reader. The
`build_*` convention is therefore UNTESTED rather than disproven, and this ruling never rested on
it.* **It is that the module has ZERO I/O-capable imports,
which is exactly what makes the membership predicate certifiable in isolation -- no mocking, no
credentials.** Converting it co-locates the thing that must be VERIFIED with the thing that touches
S3, and the predicate is the part carrying both a sovereign ruling and section 4's vacuous-corpus
problem. **Purity here is not tidiness; it is what keeps the synthetic-fixture arm cheap to run.**

**R1 and R3 unchanged. R2 re-specified: the runnable producer is a NEW file, and
`satellites_registry.py` is a DEPENDENCY of it rather than the subject of it.**

---

## 10. AMENDMENT 4 (FINAL) -- the modules DO NOT COMPOSE, and the CARRIER question is answered at source

### 10a. `3.0.0_SA_CVO~Z` asked the FORWARD question (msg 11138) and it moved R2/R3 again

Five instruments had established what the file ISN'T. Nobody had asked what would produce the R3
ARTIFACT. **Confirmed here on AST rather than by re-running their import-line grep:**

```
registry imports weights?  False       weights imports registry?  False
POSITIVE CONTROL: test_satellites.py imports registry?  True   <- the detection works
```

`satellites_registry.py`'s functions are `canonical_roster_names` / `drift_report` /
`assert_no_drift`, and `drift_report` returns a SYMMETRIC DIFFERENCE whose own docstring says
*"this oracle never decides."* **It is a CONFORMANCE CHECKER by design, not a producer missing rungs.**

**And the API surface shows THREE absent capabilities, not one:**

```
satellites_registry  imports __future__, re, typing                       -> NO I/O AT ALL
satellites_weights   imports __future__, lib.trading_calendar, pathlib,
                             sys, typing                                  -> NO boto3
```

STOP: neither module can fetch from S3 -- `satellites_weights` builds a `bronze_key` and has no
client to spend it on. **The producer must supply S3 FETCH + THE JOIN + THE WRITE. Amend2/amend3
called R2 "wire it up" as though the logic existed. THE JOIN IS UNWRITTEN CODE; R3 is a BUILD.**

### 10b. The other half -- THREE guards already exist. The producer CALLS them.

```
assert_no_drift                        registry   the conformance oracle
assert_fresh + FRESHNESS_BASIS
  + lib.trading_calendar               weights    the TRADING-DAY FRONTIER, already honoured
assert_no_baked_verdict
  + CARRIER_FORBIDDEN_FIELDS           weights    the carrier contract, for the producer's OUTPUT
```

STOP: **the BUILD LADDER binds at rung 2. A producer that re-derives freshness re-opens the
Friday-is-Monday false alarm CLAUDE.md has a standing NEVER rule about.** This is the concrete payoff
of keeping the modules pure in amend3 -- the guards stay callable in isolation.

### 10c. Certification criteria, ADOPTED IN FULL from `3.0.0_SA_CVO~Z`

```
R1  deployed BYTES vs the BUILD INPUT (Rule 22a), never by filename; pin cited by CONTENT
R2  TWO RUNGS -- (a) LOADS: resolve-by-import on the DEPLOYED artifact + an ABSENT symbol control
                 (b) INVOKED: comp-pipescript io <script> --pipeline cot-gold returning anything
                     other than "Unknown script in tree", positive-controlled
    STOP: (a) passing with (b) absent IS TODAY'S STATE ONE RUNG UP.
R3  certifies at EXERCISED, never APPLIED -- the key exists because a RUN wrote it
    + a ZERO-MEMBER FIRM negative control returning 200 {books: [], as_of}, NOT 403
```

The zero-member arm is load-bearing, not fastidious: since `24a8435642` removed the serving layer's
synthesised empty, **acceptance exercised only on a firm that HAS members ships the failure path
unexercised**, and that path is now the only one where absence is recoverable.

### 10d. `2.0.0_SA_COO~Z` stopped and named the governing question. Answered AT SOURCE.

They asked: *is the satellites registry a published artifact, or a declared frontend constant?* --
raising that `SATELLITE_REGISTRY = []` in `satelliteSet.ts` might be the intended carrier, in which
case their `TO-4-AE` hold waits for an object nothing was meant to emit.

**Refuted by the file's own header, `portal/src/pages/Positioning/shared/satelliteSet.ts:6-13`:**

> THIS FILE DECLARES THE CONTRACT. IT DOES NOT DECLARE THE MEMBERSHIP. ... The member set is
> `ETFS_SATELLITES.TO-2`'s deliverable (DS lane) ... **That TO is the PRIMARY carrier. This file
> ships `SATELLITE_REGISTRY` EMPTY on purpose and consumes TO-2's registry when it lands.**

`[]` is a DECLARED state rendering `SATELLITE_PENDING_NOTICE`, not an unfinished one. The file also
pre-refuses the alternative: typing the nine there *"would create a SECOND durable carrier of one
obligation, and two carriers with no named primary diverge from minute one"* --
[[two-carriers-with-no-named-primary-diverge]].

**Second, independent source -- the sovereign's own word, ~22:5xZ:** *"If an Opal Satellite
disappears from **daily pulls**, now it is no longer tracked."* A frontend constant cannot satisfy
that sentence; it does not see daily pulls and changes only when a human edits it, which is the
hand-drawn registry he was ruling against.

```
membership       DERIVED per pull             Andrew ~22:5xZ
primary carrier  TO-2's output, NOT the TS    satelliteSet.ts:6-13, explicit
delivery form    the SCOPED API PATH          Andrew ~22:1xZ
```

STOP: **the hold is sound and the TO is cuttable.** `TO-4-AE` is not waiting for an unintended
object -- it waits for one that three independent rulings require and that no code was ever written
to produce. **That is a gap, not a category error, and it is the better of the two worlds: nothing
already built is wrong.** `3.0.0_SA_CVO~Z`'s finding survives undiminished -- what it could not
settle from the data tier is whether the artifact was WANTED, and the portal contract answers yes.

### 10e. The corrected frame the successor TO inherits

```
R1-R3 destination      RIGHT from the start
"satellites_registry.py is the producer"   WRONG -- it is a checker
"R2 = wire it up"                          WRONG -- the join is unwritten
"a NEW producer importing it"              RIGHT SHAPE, and it must import BOTH modules and supply
                                           FETCH + JOIN + WRITE, calling the three existing guards
```

---

## 11. AMENDMENT 5 -- section 3's INTERPRETATION is withdrawn. The predicate IS validated; only the ANCHORS are unexercised.

`3.0.0_SA_CVO~Z` retracted a finding of their own (msg 11175, durable @`e021e23f0a`) after
`2.0.0_SA_COO~Z` falsified it, and **their diagnosis convicts this record's section 3 too.**

Their mechanism, verbatim: *"I VARIED THE NOTATION AND HELD THE DISCRIMINATOR (the token `Opal`)
CONSTANT. Both arms were anchored … its agreement was GUARANTEED BEFORE I RAN IT."*

STOP: **all five variants in section 3 contain `Opal`.** The uniform "9" was guaranteed before the
run, for exactly that reason. Section 3's numbers are right; **its generalisation -- *"the corpus
cannot tell the careful rule from the careless one"* -- was too broad and was published as the
headline.** See [[a-guards-corroborating-surfaces-share-its-author]] and
[[a-quantity-both-hypotheses-predict-is-not-evidence]].

### The per-limb measurement neither seat had run -- drop ONE limb, count EXTRA admits

```
drop the token `Opal`   -> /satellite/i          admits +18   EXERCISED
drop leading anchor ^   -> Opal Satellite \d+$   admits  +0   UNEXERCISED
drop trailing anchor $  -> ^Opal Satellite \d+   admits  +0   UNEXERCISED
```

**`3.0.0_SA_CVO~Z` is right and their apology to `0.4.0_DS_ClientPlatform~W` is warranted:** the
predicate does real work -- 18 rows, the entire `Core | Satellite *` family, and `Core | Satellite 98`
sits in the corpus beside `Opal Satellite 98`, which is `SAT-b-4`'s adversarial pair. The module's
author had already done the thing both of us implied was undone.

### But their §5 withdrawal is one step too broad, and it would retire a live gate

They withdrew *"any suggestion that … the corpus lacks a negative case."*

STOP: **the corpus lacks a negative case FOR THE TRAILING ANCHOR -- measured +0 -- and that is the
limb guarding the exact hazard Andrew named** (*"if it says 'opal satellite with some other shit'
that is not acceptable"*; *"they may do some stupid shit like that again"*).

```
Opal Satellite 50 + 15% cash   in corpus? NO   shipped REJECTS   no-$ ADMITS  <- the only separator
Opal Satellite 50 Tax-Free     in corpus? NO   shipped REJECTS   no-$ ADMITS
```

**The corrected statement, narrower than mine AND than their withdrawal:**

```
the PREDICATE        VALIDATED  -- the token carries 18 rows of discrimination  (their correction)
the TRAILING ANCHOR  UNEXERCISED -- +0 rows, and it guards the named future     (STANDS)
```

**Section 4's binding synthetic-fixture criterion STANDS unchanged**, and `Opal Satellite 55`
(MUST ADMIT) stands with it -- no negative separates a derived predicate from the declared list it
replaces.

### The class, and it is the new one

> ⛔ **A RETRACTION CASCADE CAN RETIRE A VALID CRITERION, and it is harder to catch than the false
> finding was -- a withdrawal reads as humility, so nobody audits its SCOPE.**

The instrument that catches both halves: **vary ONE limb at a time and count the rows it moves.** A
variant set that changes several things at once cannot attribute its own result.
`0.4.0_DS_ClientPlatform~Z` reached the same "too broad by one anchor" conclusion independently.

---

## 12. AMENDMENT 6 -- the WIRE SHAPE is ruled, and it was already settled by a criterion nobody noticed had answered it

`0.7.0_AE_CloudOps~Y` (msg 11214) swept every `TO-5-DS` clause making a claim about their own work,
**printed the denominator (3 of 4 accurate)**, and found a third staleness at `:73-74`: *"do NOT
design the served shape -- it is TO-4-AE's"* points at a file that, since `24a8435642`, defines only
an error envelope. **The instruction is right and the pointer is wrong** -- the shape is at
`satelliteSet.ts:52/:66`, ratified by `2.0.0_SA_COO~Z`'s SAT-a-4 ruling at 18:21Z.

They then left one detail open and assigned it to the executor: **where `as_of` rides on the wire**,
given `satelliteSet.ts:93` types the injection as a bare `readonly SatelliteBook[]` which cannot
carry one.

STOP: **that is not the executor's call, and not theirs either.**

```
PRODUCER   0.4.0_DS_ClientPlatform~L   writes it
CARRIER    0.7.0_AE_CloudOps~Y         passes through; takes no position since 24a8435642
CONSUMER   satelliteSet.ts / DE lane   injects a BARE ARRAY at four call sites
```

**A shape spanning three lanes is an architecture decision.** Left unspecified, the producer picks
one envelope and the fetch layer expects another -- **and that divergence surfaces at integration,
after both halves are green.**

### It was already ruled, by a criterion this record adopted in section 10c

`3.0.0_SA_CVO~Z`'s zero-member negative control: **a zero-member firm returns
`200 {books: [], as_of: <ts>}`, not 403.**

> ⛔ **THAT IS THE ENVELOPE, STATED AS AN ACCEPTANCE CRITERION BEFORE ANYONE ASKED THE SHAPE
> QUESTION.** A bare array cannot express `{books: [], as_of}`. The wire shape was settled the moment
> that control was adopted; **nobody noticed it had answered a second question.**

```
WIRE / ARTIFACT   { books: SatelliteBook[], as_of: <ts> }   carries its own as_of (SAT-a-4)
INJECTION SEAM    readonly SatelliteBook[]                  UNCHANGED -- four call sites intact
FETCH LAYER       unwraps `.books` before injecting         the only new seam
```

`satelliteSet.ts:93`'s bare array is not a conflict: two layers, and the unwrap is where they meet.
**Ruled, not proposed.**

### Third staleness, one cause, and a cheap remedy

All three defects were written while that seat's envelope existed and went stale when they removed
it. Their own diagnosis is the actionable half: *"I only found these by checking after the GO rather
than announcing the fix into the TOs that cite me."*

> ⛔ **A FIX CARRIES A NOTIFICATION OBLIGATION TO EVERY SPEC THAT CITES THE DEFECT, AND THE FIXER IS
> THE ONLY PARTY WHO KNOWS THAT CITATION LIST.**

A two-minute sweep at fix time against three post-GO corrections here. See
[[fixing-a-defect-doesnt-reach-whoever-quoted-it]].

### 12a. The shape is CONFIRMED, and amend6's own justification was the weakest of three

A collision surfaced twenty minutes after amend6: `3.0.0_SA_CVO~Z` named
`satellites_weights.payload()` as "the producer's write shape", whose keys are
`satellites`/`rows`, not `books`. **Three arguments settled it, and they are not equally strong:**

```
MINE    constituent_rows / unresolved_count are weights VOCABULARY     from NAMING
CVO's   the module docstring -- "TO-1 WEIGHTS ... WRITES nothing.
        This module DERIVES; it does not publish."                     from AUTHORSHIP  (self-corrected
                                                                       by that seat before being asked)
DS~L's  payload().satellites is a LIST OF NAME STRINGS (:200, :331);
        SatelliteBook is an OBJECT with nested constituents (:52,:66)  from STRUCTURE
```

> **A RENAME PRODUCES A LIST OF STRINGS WHERE THE RATIFIED CONTRACT REQUIRES OBJECTS. That is not a
> disagreement about a key -- it is a proof the two cannot be one artifact.**

STOP: **mine could have been answered by renaming a key; the structural one cannot be answered at
all.** My framing of the collision as *"they disagree on the key name"* was the weakest available
form of a correct suspicion, and **this section exists so the record carries the argument that
settles it rather than the one that raised it** -- the same reason section 9 required a mechanism
beside a true conclusion.

**Confirmed and building on:** REGISTRY -> `{ books: SatelliteBook[], as_of }`; the weights block is
a different artifact; and **the DESIGN transfers even though the STRUCTURE does not** -- facts-only
payload, no baked verdict, vintage computed at read time. That last distinction is what keeps "reuse
what exists" (build ladder rung 2) from becoming "copy the dict".

⚠ **`T5DS-AC3` is UNCERTIFIED and uncertifiable until the registry builder exists.** An earlier
sentence of mine called that hazard "closed with existing code" -- **withdrawn**: the exercised-green
result was on TO-1's weights carrier and the two guards, not on the registry.

### 12b. The shape gains ONE CLAUSE: `as_of` is NON-NULL always, including on the empty

```
{ books: SatelliteBook[], as_of: <the partition date the producer RAN> }
                                  ^^^ NON-NULL ALWAYS, INCLUDING WHEN books IS EMPTY
```

Measured by `3.0.0_SA_CVO~Z`:

```
read({as_of: "2026-08-27", rows: []})  -> OK      vintage.state='FRESH'
read({as_of: null,         rows: []})  -> RAISES  ValueError: Invalid isoformat string: 'None'
read({                     rows: []})  -> RAISES  KeyError: 'as_of'
```

> ⛔ **THE NATURAL SHAPE TO REACH FOR, FOR AN EMPTY ARTIFACT, IS THE ONE THAT BREAKS.**

**The distinction that makes this a rule rather than a gotcha** (`0.7.0_AE_CloudOps~Y`):

```
NO ARTIFACT EXISTS       as_of: null was CORRECT -- nothing was published, so there is no data
                         as-of, and stamping a read time would MANUFACTURE a freshness signal
PUBLISHED, ZERO MEMBERS  as_of MUST be the pull date -- a pull HAPPENED and found nothing
```

**ZERO MEMBERS IS A MEASUREMENT WITH A DATE, NOT AN ABSENCE OF ONE.** STOP: the failure lands
precisely on the criterion's purpose -- **an empty artifact with a null `as_of` is indistinguishable
from a never-published one, at exactly the moment `AC3` exists to make those two distinguishable.**
The bug would not merely break a read; it would silently undo what publish-empty is for.

⚠ **LIFT HAZARD:** `{books: [], as_of: null}` was in the tree hours ago and **still appears in
`0.7.0_AE_CloudOps~Y`'s proof-of-spec and measurement record.** It is the most citable-looking
precedent for this exact case and it is wrong for it. *A deleted shape that survives in records is a
live carrier -- the code is gone and the example is not.*

**Adopted as an architecture preference, from that seat's own framing:**

> **"REMOVED RATHER THAN NARROWED left nothing behind to be copied. A narrowed converter would still
> have carried `as_of: null` in the tree for someone to lift."**

⛔ **A NARROWED DEFECT LEAVES A CITABLE EXAMPLE; A DELETED ONE DOES NOT.** Where the behaviour is
genuinely unwanted and deletion is available, prefer it -- **the residue of a narrowing is a
precedent, and precedents get lifted by readers who never read the narrowing condition.**

### 12c. `SatelliteBook.code` IS THE CANONICAL NAME -- non-collision PROVABLE, not conventional

Raised by `0.4.0_DS_ClientPlatform~L`: `satelliteSet.ts:66` requires `code: string` and calls it
*"the column identity (never the display name)"*, but **no file in the consumer defines its form** --
every hit consumes a code, none specifies one.

```
SatelliteBook.code         =  the CANONICAL NAME, verbatim     e.g. "Opal Satellite 50"
SatelliteBook.displayName  =  free to differ; unconstrained by this ruling
```

**Three reasons, strongest first:**

```
1 PROVABLE NON-COLLISION  MODEL_BOOKS = UST/ST/INT/LT/ULT ; ETF books DIVZ/IDVZ/PFDE/PFOE.
                          NONE matches ^Opal Satellite \d+$ -- measured, positive control passing.
                          A 3-5 char mnemonic CANNOT equal an anchored three-token form.
2 IT IS ALREADY THE KEY   MEMBER_NAMES is a frozenset of exactly these and the predicate matches
                          on this field. Any other choice creates a SECOND identity space plus a
                          mapping -- see [[two-carriers-with-no-named-primary-diverge]].
3 NO NEW TABLE            build ladder rung 1/2: a convention is code nobody has to write.
```

STOP: **`model_id` REJECTED on a GRAIN MISMATCH, not taste** -- a book would be a MEMBER by NAME but
KEYED by an id the membership predicate never validated. **The value that decides membership and the
value that identifies the column must be the same, or a book can pass one test and be absent from the
other.** Numeric suffix rejected: it discards the anchor protection reason 1 rests on.

**Premise correction owed to the raiser, which does not touch the correctness of raising it.** Both
hazards they cited are already closed: `bookSet.ts:167`'s model-notes collision is guarded by
`HEADER_TRIGGER.satellites = 'none'`, and `:131`'s models-keyed-feed defect by
`SUBCATEGORY_SOURCE.satellites = 'current_holdings'`. **Both comments describe what the OLD TERNARY
did; the MODE-TOTAL declarations beside them are the remedy.** ⭐ **The escalation was still correct
on their SECOND ground -- the choice binds producer, adapter, grid and a fourth namespace, and that
reason survives intact.** *Reading a comment that describes a pre-fix world as live is the exact
stale-carrier class this record has hit four times; it was the reasonable act, not an error.*

**`AC4`/`AC5` accepted at the gate:** 9 of 65 derived, `derived == declared` with both difference
directions empty, `Opal Ultra Short Term` correctly excluded, all five blends rejected, all three
amended `AC4` rows green -- and **the per-limb ablation RE-DERIVED rather than quoted.** That is
corroboration rather than repetition, and reusing `CANONICAL_NAME_FORM` instead of reimplementing it
is the build ladder applied correctly.

---

## 13. AMENDMENT 11 -- a FAILED CONTROL falsified my `cottonwood_aua.py` claim, in BOTH directions

`0.4.0_DS_ClientPlatform~L` named `cottonwood_aua.py` a POSITIVE control for producer-ness in
`T5DS-AC1`, exercised it, **and it refused.** Measured at source: boto3 client `:106`, `get_object`
at `:118` and `:147`, `main()` at `:217` derives and **prints**. **No `put_object`, no upload, no
file write anywhere. It is a READER.**

**Both of my passes on this file were wrong, in opposite directions:**

```
PASS 1 (grep, §7)   write-verbs=0, __main__=1
                    I wrote "a real sibling PRODUCER scores zero -> false-negative in the pattern"
                    STOP: "PRODUCER" WAS NEVER MEASURED -- inferred from name and location.
PASS 2 (AST, §7)    it imports boto3 + json
                    I wrote "it IS write-capable; my regex missed its call form" -> caveat withdrawn
                    STOP: boto3 COVERS READS. An import proves it can TALK to S3, never that it WRITES.
```

> **My "write-capable imports" column could not distinguish a reader from a writer, and I used it to
> overturn someone else's finding.** The conclusion of pass 2 was right -- the counterexample had to
> go -- and **the mechanism was wrong**, which is the class recorded in section 9 and committed again
> here. `0.7.0_AE_CloudOps~Y`'s write-verb result was **correct about this file**; their instrument's
> real weakness rests on their own 385-file sweep (64 genuine counterexamples), not on mine.

**The diagnosis is the raiser's and it is the durable half:**

> *"HAD IT PASSED AS A POSITIVE CONTROL, THAT WOULD HAVE MEANT MY INSTRUMENT SAYS YES TO A NON-WRITER
> -- i.e. that it cannot distinguish a producer from a consumer at all, which is the one property AC1
> exists to establish. The control failing is what tells you the instrument works."*

**A CONTROL THAT FAILS IS A RESULT.** Four seats tonight treated a passing control as confirmation;
this is the first time one failed and **the failure was the finding**.

**And the corrected control set is stronger than the one I specified:**

```
NEGATIVE  satellites_registry.py  refuses on the EASY signal (no write-capable imports at all)
          cottonwood_aua.py       HAS boto3, HAS main, HAS the guard -- and still REFUSES
```

**The discovered negative is the better one: it separates "LOOKS like a producer" from "IS one",
which the designed negative cannot.** *A negative control that fails for an obvious reason tests less
than one that fails for the reason you actually care about.*

---

## 14. AMENDMENT 12 -- my import census was RIGHT BY LUCK, and my unmeasured label cost the fabric its only behavioural instrument

`3.0.0_SA_CVO~Z` (msg 11303) disclosed something only they could have caught, **because only they ran
it and only they discarded it.**

### 14a. The concession, stated plainly

```
AST import census on satellites_registry.py   boto3 ABSENT  -> "not a producer"   TRUE
AST import census on cottonwood_aua.py        boto3 PRESENT -> "write-capable"    FALSE (it reads)
                                              SAME instrument, same night
```

> ⛔ **THE DIFFERENCE WAS A PROPERTY OF THE FILES, NOT OF THE INSTRUMENT. HAD THE REGISTRY MODULE
> IMPORTED `boto3` FOR A READ, THIS RECORD'S CENTRAL CONCLUSION WOULD HAVE INVERTED.**

**WITHDRAWN:** my claims that the import census was *"immune to the false-negative that weakened both
earlier passes"* and that the question was *"closed, not merely unrefuted."* **It measures
CAPABILITY; the question was BEHAVIOUR.** It was right by which file it was pointed at -- the
formulation `0.7.0_AE_CloudOps~Y` used against themselves at 23:51Z, which I quoted approvingly and
then earned.

### 14b. The causal chain, and it starts with my unmeasured adjective

```
1  I call cottonwood_aua.py "a real sibling PRODUCER"       never measured; inferred from the name
2  3.0.0_SA_CVO~Z adopts it as a POSITIVE CONTROL            inherits my classification
3  their write-SINK AST scan reports NONE for it             THE INSTRUMENT IS CORRECT
4  the control "fails" -> they discard the instrument         "Discarding that limb."
5  three seats spend an hour approximating "does it write?"  while the one instrument that measures
                                                             BEHAVIOUR sits discarded
```

> ⭐ **A POSITIVE CONTROL INHERITS THE CLASSIFICATION OF ITS SUBJECT. A FAILING POSITIVE CONTROL MEANS
> *EITHER* THE INSTRUMENT IS BROKEN *OR* THE SUBJECT WAS MISLABELLED -- AND THE TWO ARE
> INDISTINGUISHABLE FROM INSIDE THE RUN.**

They picked the first reading; **the second was mine to have prevented by measuring before
labelling.** And their second observation is why it stayed buried: **DISCARDING AN INSTRUMENT LOOKS
LIKE RIGOUR.** *Nobody audits a measurement its author decided not to trust -- a discard removes
evidence while reading as care.*

### 14c. The instrument ladder -- the reusable artefact

```
write-verb grep         CALL-FORM PATTERN   magnitude UNSETTLED -- see 14d
AST import census       CAPABILITY          says boto3=Y for a READER            <- mine
pipeline-graph absence  REGISTRATION        silent on producer-ness
write-SINK AST scan     BEHAVIOUR           correct, discarded on a borrowed error, now restored
```

> ⛔ **THE `~60% false-positive` FIGURE THAT STOOD IN THIS CELL IS WITHDRAWN -- SEE 14d.** Its author
> retracted it as inflated ~60x, and I had repeated it as a measured fact. **The ladder's ORDERING is
> unaffected: it rests on WHAT each instrument measures, not on that magnitude.**

STOP: **three of the four measure PROXIES, and all three agreed.** That is the *N seats, one rung*
shape wearing four hats -- **agreement among proxies is not convergence on the property.** See
[[three-seats-one-rung-is-not-triangulation]].

**No verdict moves.** `satellites_registry.py` is not a producer -- now established on the instrument
that measures the right property rather than on three that approximate it. **Section 7's "load-bearing
limbs are the ENTRYPOINT and PIPELINE-GRAPH absences" is downgraded accordingly: those are proxies
too, and the write-sink scan is the limb that answers the question directly.**

### 14d. I relayed a peer's SELF-CRITICISM as a measured fact, and I have that banked as a rule

The `~60% false-positive` figure came from `0.7.0_AE_CloudOps~Y`'s criticism of their own instrument.
**They retracted it as inflated ~60x.** `3.0.0_SA_CVO~Z` had put it in a comparison table; **so had
I, in this record, ninety seconds before the retraction arrived.** Neither of us asked its
denominator.

> ⛔ **A SELF-CRITICISM ARRIVES PRE-AUTHENTICATED. Running against the speaker's interest reads as
> costly, and costly reads as true -- so it is the one class of claim nobody audits.**

I hold [[a-self-criticism-is-never-asked-for-its-denominator]] as a caution about **authoring** one.
**This is the RECEIVING side of the same rule, and it is the side that propagates:** every other
figure in that ladder I measured myself; **the one I did not test is the one that came with a
confession attached.**

**What IS independently established** (`3.0.0_SA_CVO~Z`'s own sweep, different population, so the
magnitudes are not comparable): of **496** runnable gold scripts, **170 write nothing** -- ~34%.
**The MECHANISM stands: "RUNNABLE" IS NOT "PRODUCES", so scoring `has __main__ but no write verb` as
instrument failure compares against the wrong population.** The direction and mechanism are
confirmed; **the magnitude is unsettled and belongs to nobody's measurement yet.**

**And the tally of this one question:**

```
my original caveat                      OVER-stated -- cottonwood_aua is a READER
my retraction of it                     ALSO wrong  -- a boto3 import covers reads
0.7.0_AE_CloudOps~Y's "64 of 107"       wrong in the OPPOSITE direction, self-retracted
my + CVO's relay of that figure         wrong for a THIRD reason -- denominator never asked
satellites_registry.py                  STILL not a producer, on four independent grounds
```

⚠ **Four seats, four errors, one unmoved conclusion. That is either a robust finding or a question
nobody could get wrong, and it cannot be told apart from inside.**

⭐ **The single most useful observation of the night, from `2.0.0_SA_COO~Z`:** *"running the reader
caught 2 of 5 field defects, re-reading caught 0 of 5."* **Every defect tonight that changed a spec
was found by EXERCISING something** -- a control that failed, a payload that raised, a producer that
was run. **Not one came from a careful re-read**, this record's twelve amendments included.

Push state: LOCAL at commit time (`0.0.0_AB_MSTR~Z` is the integrator and pushes).
