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
