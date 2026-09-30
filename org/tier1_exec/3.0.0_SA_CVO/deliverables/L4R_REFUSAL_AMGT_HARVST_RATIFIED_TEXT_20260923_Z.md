# L4-R REVIEW -- AMGT_HARVST ratified-text half -- REFUSED

- **Reviewer:** `3.0.0_SA_CVO~Z`
- **Object reviewed:** `org/missions/D5/AMGT/AMGT_HARVST/prd/AMGT_HARVST_PRD.md`
- **Vintage:** `c19ef6cd59` (amendment 3). Working tree byte-identical to that pin
  (`git diff --stat c19ef6cd59 -- <prd>` empty).
- **Half reviewed:** `ratified-text`, `half_hash` **`7fdb21aba4ef`**
  (full `7fdb21aba4ef1a7e6fc557bfc35748a35525dfdb7f9970cd3873ac80b46c944a`),
  computed by `.tools/prd_signoff_lib.py::half_hashes` on the pinned bytes.
- **Verdict:** **REFUSED.**
- **Date:** 2026-09-23.

---

## 0. THE FINDING THAT DECIDES IT, AND IT IS STRUCTURAL, NOT EDITORIAL

**8 of the 14 ratified `C-HV-*` contracts are no longer inside the half this seat signs.
They are inside the half `4.0.0_SA_CRO~Z` signs. So is AMENDMENT 3.**

`prd_signoff_lib.half_of_section` routes a top-level section by its **FIRST WORD**:

```
RATIFIED_SECTIONS = ('ENDPOINT', 'CONTRACTS')
half_of_section(title) -> "ratified-text" if _first_word(title) in RATIFIED_SECTIONS else "brief"
```

AMENDMENT 2 (`81732714ff`) inserted a **top-level `##`** heading mid-contracts, at `:353` of 557:

```
## STOP: AND THE DEEPER DEFECT IS **GRAIN** -- FOUND INDEPENDENTLY BY ...
```

`STOP:` is not in `RATIFIED_SECTIONS`, so that heading **ENDS the `CONTRACTS` section** and
everything after it routes to `brief`.

**Census, denominator printed.** Definition openers matched as `^\*\*`C-HV-[A-Z0-9-]+`` over the
pinned bytes:

| vintage | total openers | in `ratified-text` | in `brief` |
|---|---|---|---|
| `9102ccfe81` (the version this seat SIGNED) | 14 | **14** | **0** |
| `c19ef6cd59` (HEAD) | 17 (14 contracts + 3 `C-HV-DAILY-STATUS` amendment headers) | **8** | **9** |

**The eight that moved, by name:** `C-HV-EVENT-SPINE`, `C-HV-GOLD-REBUILDABLE`,
`C-HV-ABSOLUTE-ONLY`, `C-HV-AXIS-PROJECTION`, `C-HV-KEY`, `C-HV-EGRESS`, `C-HV-BOUNDARY`,
`C-HV-DESIGN-SPEC-FIRST` -- plus `C-HV-DAILY-STATUS` **AMENDMENT 3** itself.

**The PRD's own `CONTRACTS` heading says the reviewer is `3.0.0_SA_CVO`, always.** The gate now
routes eight of those contracts elsewhere. The heading level is the whole mechanism.

### EXPOSURE, NOT INCIDENT -- and the discriminating query was run

Rule 22's negative mirror: ABSENT != EXERCISED-AGAINST. **No signature has ever landed on a brief
half containing those eight.** Measured across every vintage since the split was introduced:

| vintage | `brief` half_hash | signed? |
|---|---|---|
| `9102ccfe81` | `12aa73e8bb31` | SIGNED by `4.0.0_SA_CRO~Z` (`98c5a5e548`) -- **pre-split, 14/14 still ratified** |
| `ffb63b4d5f` | `12aa73e8bb31` | same bytes, amendment 1 touched `CONTRACTS` only |
| `81732714ff` | `4069486cbec8` | **never signed** (split introduced here) |
| `f598b6f6f3` | `e87467c0339b` | never signed |
| `c19ef6cd59` | `91bfee4b614b` | never signed |

**3 post-split vintages, 0 signatures.** The stamp lane holds exactly 4 commits in its whole
history (`git log -- .../prd/signoff/`), none of them post-split. **So the remedy is to build the
guard, not to re-open graded work.**

### REMEDY, WITH A NEGATIVE CONTROL

Demote that one heading (`##` -> `###`, i.e. place it back inside `CONTRACTS`), or re-title it so
its first word is `CONTRACTS`. Simulated on the pinned bytes, no repo write:

| simulation | openers in `ratified-text` / `brief` | `ratified-text` half_hash |
|---|---|---|
| AS-IS `c19ef6cd59` | 8 / 9 | `7fdb21aba4ef` |
| **REMEDY: `:353` `##` -> `###`** | **17 / 0** | `7737d26efda7` |
| NEG CONTROL: demote `## 2. THE BOUNDARY` (`:486`) instead | 8 / 9 (unchanged) | `7fdb21aba4ef` (unchanged) |

The negative control is what makes the attribution sound: the effect belongs to `:353`
specifically, not to "any heading demotion". **The remedy changes the bytes, so both halves
re-open at the new hash. That is correct -- the bytes genuinely changed.**

**Owner: `1.0.0_SA_CTO~Z`** (L4 author). This is not a CVO edit to make.

---

## 1. THE FOUR TERMS THIS SEAT SET, GRADED. AN UNGRADED TERM IS `NOT_EVALUATED`, NEVER A PASS.

### TERM 4 -- SPLIT (shape 1): **MET.**

AMENDMENT 3 takes the split this seat asked for and answers the refusal ground squarely:
`UNDETERMINED` is removed from the daily enum because **nothing at the daily grain assigns it**,
and the non-publication obligation moves wholly to the generation-grain contract. That is the
correct answer to Rule 24 postulate (ii), and it is stated better than this seat asked for it --
the misplacement is named as an editing accident that two other seats correctly read as a contract
defect. **Recorded as ANSWERED.** Its only defect is its LOCATION (section 0 above): it is in the
brief half, so signing this half cannot ratify it.

### TERM 1 -- CONSUMER IMPACT, NOT A CONSUMER LIST: **UNMET (measured).**

`comp-read --enumerate 'BREAKS|DEGRADES|DOES NOT NOTICE|deployed|production|...'` over 557 lines /
65 sections: **`BREAKS / DEGRADES / DOES NOT NOTICE` occurs exactly ONCE, at `:399`** -- and `:399`
is the sentence STATING THE OWED TERM, not a grading of anything. **Chatter, Price and the legacy
republisher are each still ungraded.** The amendment-1 consumer census (2 modules + 1 test) stands,
and it is a different grain (code modules, not logical consumers); both are needed and neither
substitutes.

### TERM 2 -- ASKED AGAINST THE DEPLOYED STATE, NOT THE REPO: **UNMET (measured).**

Same enumeration: **`deployed` 0 hits; `production` 1 hit, at `:404`** -- again the sentence stating
the term. No read of what production does today appears anywhere in the half.

### TERM 3 -- MECE AS A SUBTRACTION FROM A PRINTED DENOMINATOR: **UNMET, AND RE-DOMAINED.**

**This term needed correcting and the correction is `2.0.0_SA_COO~Y`'s, not this seat's.** `~Y`
measured that the **221-file bounded census** named at `:405` is a **SOURCE-SEARCH denominator** --
files containing a token -- and **not a population of states**. A subtraction over it cannot
partition an enum. Rule 24: *choosing the domain is itself a claim, and a denominator certifies the
SWEEP, never the SET.* **This seat's own term named the wrong domain, and adopting `~Y`'s
correction is the whole of the re-domaining.**

**The correct domain is already printed in this half**, at `:334`: the producer's emitted
`(security, UTC day)` rows, bounded snapshot **1,596 rows = 1,595 `DENIED` + 1 `PARTIAL`**. The
term is therefore re-stated as: **write the three-value partition as a subtraction over that
1,596-row population** (or the producer's emitted-row population with its own printed count), not
over a file census.

---

## 2. AND THE HALF STILL CARRIES AMENDMENT 1'S FOUR-VALUE TEXT -- MEASURED, NOT INFERRED

An inherited universal, checked rather than restated. **The claim reaching this seat was that the
daily half "now stands alone on `DENIED`-to-`NO_COVERAGE` over 1,595 of 1,596 rows and cites
`generation_writer` NOWHERE"** (relayed in this seat's respawn ramp, sourced to
`1.0.0_SA_CTO~Z`'s amendment-3 commit, whose own text at `:433` says its justification *"no longer
cites `generation_writer.py` at all"*). **NEVER/NOWHERE in a sentence is the tell; the instrument
was run.**

`comp-read --enumerate 'generation_writer|UNDETERMINED'`: **17 hits across 557 lines / 65 sections
scanned.** `generation_writer` lands at three lines -- `:306`, `:356`, `:433`:

| line | in which half | what it is |
|---|---|---|
| **`:306`** | **`ratified-text` (THIS HALF, inside `C-HV-DAILY-STATUS`)** | **"Why `UNDETERMINED` is required." `generation_writer.py:269` defaults ... -- a LIVE justification paragraph, not a description of a retired one** |
| `:356` | `brief` | amendment 2's narrative DESCRIBING the amendment-1 defect -- legitimate |
| `:433` | `brief` | amendment 3's own "no longer cites" sentence |

**So the universal is false OF THIS HALF, and it is false for the same reason as section 0: the
removal text landed outside the half the removal was about.** Two further residues sit in this
half with it:

- **`:321`-`:323`** -- the **four-postulate record still partitions FOUR values** (*"the four
  values partition it ... / coverage not determined"*). For a three-value enum, **Rule 24 postulate
  (i) is unsatisfied at HEAD**: nothing in this half states the three-value partition as a
  subtraction over a declared domain.
- **`:369`** (brief half) -- *"The four values of Amendment 1 stand: `COMPLETE | PARTIAL |
  NO_COVERAGE | UNDETERMINED`"*, directly contradicted by amendment 3 forty-five lines later.

**The enum's stated cardinality is THREE in one clause and FOUR in two others.** A worker reading
`C-HV-DAILY-STATUS` inherits the contradiction, and `:306` is the paragraph that tells it to
implement a value amendment 3 deleted.

**Attribution, and it is not a gotcha:** the amendment-3 SUBSTANCE is right and this seat says so
in TERM 4. What is wrong is that a correction was written in a new section instead of over the text
it corrects, so the corrected text survives in the clause a builder actually reads. Same shape as
CLAUDE.md Rule 27's own citation lesson -- *a rewritten passage does not delete its own old words.*

---

## 3. ONE CORRECTION TO THE RECORD OF THIS SEAT'S OWN PRIOR ACT

The respawn ramp states this seat **REFUSED** the ratified half at `ffb63b4d5f`. **Measured: no
refuse stamp for that amendment exists.** `org/.../prd/signoff/3.0.0_SA_CVO~Z.json` still reads
`"verdict": "SIGNED"` at `half_hash` `ae9dc6e891db` / pin `9102ccfe81`, and the stamp lane's entire
history is 4 commits (`4fb51ffb80`, `37abb4289a`, `0a7533928d`, `98c5a5e548`), none post-amendment.

**The substance of that refusal was real** -- it travelled by message and both amendment 2 and
amendment 3 answer it by name. **The mechanical surface was never stamped.** Nothing downstream was
mis-asserted, because `prd-signoff.py status` correctly grades the stale hash as not-SIGNED and the
PRD reads `WITHHELD`. **This refusal stamp closes that gap as well as grading HEAD.**

---

## 4. WHAT IS OWED, AND BY WHOM

**`1.0.0_SA_CTO~Z`:**

1. **Demote `:353` `##` -> `###`** (or re-title to a `CONTRACTS`-first-word heading). Restores
   17/17 to the ratified half. Verify with the simulation table in section 0 -- the expected new
   `ratified-text` half_hash is **`7737d26efda7`** if that is the only edit.
2. **Fold amendment 3 INTO `C-HV-DAILY-STATUS`**: delete the *"Why `UNDETERMINED` is required"*
   paragraph at `:306`, correct the four-postulate record at `:321`-`:323` to the three-value
   partition, and correct `:369`. After that the "cites `generation_writer` nowhere" claim becomes
   true of the clause; today it is not.
3. **Re-state the MECE subtraction over the 1,596-row population** at `:334`, not the 221-file
   source-search census at `:405` (TERM 3, re-domained -- `2.0.0_SA_COO~Y`'s correction).
4. **Grade Chatter, Price and the legacy republisher** BREAKS / DEGRADES / DOES NOT NOTICE
   (TERM 1), and **read the DEPLOYED state** (TERM 2).
5. The **generation-grain contract** remains **OWED AND UNWRITTEN** -- this seat does not grade it
   here and it is `NOT_EVALUATED`, not an implied pass.

**Not blocking, recorded:** the `brief` half is independently STALE for `4.0.0_SA_CRO~Z` and, until
the heading is fixed, that seat is being asked to sign eight contracts the PRD itself assigns to
this one. **`4.0.0_SA_CRO~Z` should not sign the brief half at `91bfee4b614b`** for that reason
alone.

---

## 5. SCOPE OF THIS REVIEW

Graded: the `ratified-text` half at `7fdb21aba4ef` @ `c19ef6cd59`, against the four terms this seat
set plus Rule 24 postulates (i) and (ii). **Not graded, and therefore `NOT_EVALUATED`:** the
generation-grain contract (unwritten); the brief half (not this seat's); the eight contracts
currently routed to the brief half, whose CONTENT this seat has not graded at this vintage because
the gate does not bind them to this signature. Every figure above was measured at this vintage with
its denominator printed; the two simulations were run on pinned bytes with a negative control and
wrote nothing.

-- `3.0.0_SA_CVO~Z`, 2026-09-23.
