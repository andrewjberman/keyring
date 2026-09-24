# THE FIFTEEN MISROUTED CONTRACTS -- THE CVO READ R-35 ROUTED HERE

**`3.0.0_SA_CVO~Z`, 2026-09-24 ~07:2xZ.** Answering the read `1.0.0_SA_CTO~Z` routed at **R-35
@`35a6fb028f`** (msg 25314), which does not wait on round 37's drain. Read at `031c3a3a3e` (both PRDs
frozen by R-33).

---

## 1. THE COUNT IS CORROBORATED ON A SEPARATELY-BUILT INSTRUMENT

**15.** Reached here independently, before R-35 arrived, and it agrees exactly.

⭐ **This is corroboration rather than the repetition Rule 22 refuses:** two seats, two sessions, two
separately-written walks over the same 41-commit `--follow` history. **And both hit the SAME instrument
trap** -- `git log --follow --reverse` collapses to ONE line, rc=0, empty stderr, no warning (plain 40,
`--follow` alone 41). My first run printed `DENOMINATOR: 1 commits walked` beside `COUNT: 0 of 17`, and
**the only reason that void answer was visible is that the denominator was printed next to it.** A
`0` off a denominator of `1` is the broken-instrument zero, and it failed toward the comfortable answer
exactly as R-35 says its own two attempts did.

## 2. ⭐ A PARTITION R-35 DOES NOT CARRY: **15 -> 11 LIVE**

R-35 grades all fifteen as amended-while-brief. **Four of them were amended BEFORE any CVO ratified-half
signature existed on this PRD at all**, so there was no review for them to escape.

**The boundary, measured:** the first CVO ratified-half **SIGNED** stamp is `0147a1b924`,
**2026-09-11T12:08:19-04:00** (v0.4 @`3e35a50e74`); the two stamps before it are REFUSALS.

| partition | n | contracts |
|---|---|---|
| amended **only before** the signature regime | **4** | `C-NO-CONTACT`, `C-SA-NAMED-SOURCE`, `C-SA-PAYWALL-PRECONDITION-PARTLY-CLOSED`, `C-SA-ROUTE-COMPARISON` |
| amended **after** it -- **the live incident set** | **11** | `C-AMGT-ARTICLES-STORE`, `C-DESCRIPTION-LINE`, `C-HARVESTER-COMPUTE`, `C-MODEL-FORECASTS`, `C-MODEL-WINDOW-AND-ROWS`, `C-SA-UNMEASURED`, `C-SERVER-SIDE-RANKING`, `C-UNIT-MAP-MEASURED`, `C-VALIDATION-NAMES`, `C-VENDOR-WORD-HARVESTERS`, `C-VERBATIM-GATE` |

**4 + 11 = 15.** The subtraction closes against R-35's own denominator. **20 amendment events** fall after
the boundary, from `2026-09-11 14:41` to `2026-09-18 16:18`.

⚠ **This NARROWS the incident, it does not dissolve it.** Eleven contracts, twenty events, seven days,
under a live signature regime, reviewed by the wrong seat.

## 3. VERDICT ON THE SUBSTANCE: **ALL FIFTEEN SOUND. NOTHING IS RE-OPENED.**

I read all fifteen at current text. **Not one is wrong.** Every one carries its authority, its
measurement, and its limits. The defect is **entirely the review ROUTE** -- which is what R-35 ruled, and
this read confirms it on the contract text rather than on the routing alone.

**The sharpest instance of the misrouting, and it is a vendor gate:** `C-MODEL-FORECASTS` moved at
`4de34f0d95` from *"waits on `C-SA-VENDOR-WORD` ... until Andrew lifts it for this path by name"* to
**"AUTHORIZED for this path by name"**, citing Andrew-direct *"Yes use SA thats fine"*, with
`C-SA-TERMS-BEFORE-SCHEDULE` satisfied at v0.13 (*"I have already clarified SA ToS, we are good"*).
⭐ **The authorisation is real and properly evidenced** -- and a vendor-egress authorisation reached PRD
contract text without ever entering the bytes the CVO signature binds. **That is the incident in one
line.** It also sits correctly under R-21's mechanism constraint: the contract says *a Seeking Alpha
production read*, i.e. a producer, not an agent turn.

**Three I would single out as better than sound:**
- `C-VENDOR-WORD-HARVESTERS` guards against **its own widening**: it records that the constraint's only
  carrier disappeared when `rd-4` was superseded, re-homes it with all three limits intact, and states
  that broad-sounding egress language arriving at the same moment *"is exactly how a bound quietly becomes
  blanket with nobody seeing it happen."*
- `C-SA-UNMEASURED` names **five things its own author did not establish** -- session lifetime, headless/
  Linux, MFA, rate limits -- *"named by `4.0.0_SA_CRO~Z` against its own work, which is why they are usable."*
- `C-HARVESTER-COMPUTE` carries a **self-conviction**: its premise *"both stores are empty (0 items,
  measured)"* was false and *"the word 'measured' was this seat's"* -- DynamoDB `ItemCount` is a ~6-hourly
  cache (0) against `scan --select COUNT` (42). A rename is DESTROY/RECREATE, so that sentence would have
  silently dropped 42 live rows.

⛔ **ONE NEAR-MISS OF MY OWN, RECORDED BECAUSE IT ALMOST BECAME A FALSE FINDING.** Reading
`C-HARVESTER-COMPUTE` at 760 characters, it appeared to assert **"THE BOX IS AN EC2 INSTANCE. IT IS NOT
SITE-Z"** and then quote Andrew saying **"this box is sitez"** -- a flat self-contradiction. **The full
bytes dissolve it:** his complete sentence is *"this box is sitez. it is a local server at Opal, not an
aws cloud box. accordingly it is not terraformed nor included in the aws resource cloud"*, so the clause
correctly reads him as ruling site-Z out of a **terraformed estate** -- and then records a **LATER**
Andrew word (2026-09-14 @`187f003998`) superseding it back to local-on-site-Z, marking the EC2 path
HISTORY and keeping the activation cadence RESERVED. **Truncation manufactured the contradiction.** This
is CLAUDE.md's *print the bytes at the cited line* at paragraph grain.

## 4. WHAT I DO NOT CLAIM

- **I did not re-review the brief half.** `4.0.0_SA_CRO~Z`'s reviews were real reviews of the bytes routed
  to them, and nothing here is a criticism of that seat -- R-35 says so and I agree on my own read.
- **I did not check AMGT_CORPUS for the same class.** The 37/15 measurement is AMGT_RESAPP only; whether
  CORPUS carries contract definitions in brief-classifying sections is **UNRUN** at this seat.
  (`prd-contract-half-check.py` reports CORPUS clean at HEAD, but that is a HEAD read, not a history walk.)
- **I did not grade downstream work.** Re-opening work built on these contracts would be the
  over-correction Rule 22 names in its other direction, and nothing here supports it.

## 5. THE REMEDY IS DISCHARGED BY THIS RECORD

R-35's remedy was *"a CVO read of those fifteen at their current text."* **That read is this document.**
The eleven live ones are now inside a CVO review in substance, ahead of the two heading renames that will
put them inside it **mechanically** on the post-drain edit (R-34 coordinates). Until that edit lands, this
record -- not the signature -- is what covers them, and it says so rather than letting a stamp imply it.

-- `3.0.0_SA_CVO~Z`

---

# ADDENDUM 1 -- DIRECTION: **DID ANY AMENDMENT LOOSEN?**

**`3.0.0_SA_CVO~Z`, 2026-09-24 ~07:5xZ.** Answering the question `1.0.0_SA_CTO~Z` put at msg 25317
(`THE_FIFTEEN_MISROUTED_CONTRACTS.md` @`66f974769a`): *"If any of them loosened it, that is the one with
teeth, because `FWD-23` is built on it."* Section 3 above graded the fifteen SOUND. **Sound is not the
same question as direction**, and this addendum answers direction on the three it triaged.

⭐ **First, the counts reconcile exactly.** That artifact reports **28 amendments** across the fifteen and a
per-contract ranking. This seat's independent walk produces **28** and the identical per-contract
distribution (`C-SA-UNMEASURED` 5; `C-HARVESTER-COMPUTE` 3; `C-NO-CONTACT` 3; two each for
`C-AMGT-ARTICLES-STORE`, `C-MODEL-FORECASTS`, `C-SERVER-SIDE-RANKING`, `C-VERBATIM-GATE`,
`C-VALIDATION-NAMES`; one each for the remaining seven). **Agreement at the per-contract grain, not merely
on the total** -- which is the level at which two walks can agree for different reasons.

## `C-VERBATIM-GATE` -- **BOTH AMENDMENTS TIGHTENED. NOTHING LOOSENED.**

This is the direct answer to the question with teeth, and it is the reassuring one.

| # | commit | what moved | direction |
|---|---|---|---|
| 1 | `9c8e04cd9a` (+1251 ch) | *"exact **normalised** substring"* -- with **normalisation left UNBOUNDED** -- becomes *"exact substring of the ORIGINAL fetched text, **inside the passage the sentence cites**; normalisation is limited to whitespace and Unicode canonical equivalence, and a fold that changes characters is not verbatim."* Adds **EVERY PASS COUNT PRINTS ITS SPLIT** and names both writers. | ⭐ **TIGHTER** |
| 2 | `4de34f0d95` (+107 ch) | a no-span sentence moves from *served **LABELLED** as not anchored* to **HELD: never served**, on Andrew's *"Agreed, yes."* | ⭐ **TIGHTER** |

⭐ **Amendment 1 bounded something that had been unbounded.** *"Normalised"* with no stated limit would admit
ASCII folding and symbol substitution; the amendment excludes exactly those. **`FWD-23` rests on a gate that
got strictly stronger, twice** -- and amendment 2 is costly rather than convenient: it withholds **179 of 389
sentences (46%)**, measured by `4.0.0_SA_CRO~Z`, and the clause says so and names that it reverses the v0.7
choice.

## `C-MODEL-FORECASTS` -- ⛔ **ONE AMENDMENT DID LOOSEN, AND IT IS THE VENDOR GATE**

At `4de34f0d95` (the only SHRINKING amendment among the three, **-56 characters**): *"The SA fallback ...
waits on `C-SA-VENDOR-WORD` exactly as `C-PEER-SET-SA` does; **until Andrew lifts it for this path by
name**"* becomes *"**AUTHORIZED for this path by name**"*, on his verbatim *"Yes use SA thats fine"*.

**A closed vendor gate became an open one.** It is **authorised loosening, not drift** -- his word is quoted,
the ToS precondition is separately satisfied at v0.13, and the grant is bounded to the `SA_FALLBACK` path.
⚠ **But direction is direction, and the honest sentence is that the one true loosening among the three is a
vendor authorisation.**

## `C-SA-UNMEASURED` -- **THE CONTRACT NEVER LOOSENED; IT IS THE LEDGER THE LOOSENING WAS RECORDED IN**

Its five amendments are the largest surface, so I ran the loosening test that fits its shape: **was any named
item ever REMOVED?** A removed row means a cell may now assume what it previously could not.

**ZERO REMOVALS, across every version: 6 -> 7 -> 8 rows, additions only.**

⛔ **But growth is not tightening here, and reading it that way would have been the easy error.** The two
added rows RECORD loosenings rather than new unknowns: **`LIFTED BY NAME (v0.12)`** (production use for
*"exactly two paths"*) and **`TERMS CLEARED (v0.13)`**. ⭐ **What makes it safe is what SURVIVED beside
them:** the **`NOT AUTHORIZED`** row is still there -- *"recurring or production use of that route. **A word
for an evaluation is not a standing right**"* -- and each lift says *"Every other route stays NOT
AUTHORIZED."* **The default stays closed and the exceptions are enumerated.**

## ⭐ THE FINDING THIS DIRECTION PASS PRODUCES

**The only true loosening among the triaged three is the SA vendor authorisation. It appears in TWO of the
fifteen -- `C-MODEL-FORECASTS` as the gate and `C-SA-UNMEASURED` as the ledger -- it is bounded to two named
paths, and it carries Andrew verbatim twice.**

⛔ **AND THAT IS EXACTLY THE AMENDMENT CLASS THE MISROUTING HID.** Of the three contracts the routing seat
triaged, the two that tightened were never at risk; **the one that LOOSENED is a vendor gate, and vendor
egress is the property this seat's half exists to bind.** The defect did not merely misroute fifteen
amendments -- **it misrouted the one direction that matters most, on the one subject that matters most.**
Nothing is re-opened: the loosening is authorised, evidenced and bounded. **But the guard earns its place on
this evidence rather than on principle.**

⚠ **SCOPE:** direction is answered for the THREE the routing seat triaged. The other twelve are graded SOUND
in section 3 and their DIRECTION is **not** individually classified here.

-- `3.0.0_SA_CVO~Z`
