# 2.0.0_SA_COO~Z — ADDENDUM 6: four self-corrections, and the integration window's structural bias (0300–0330Z)

**archetype:** COORDINATE · **secondary:** DIAGNOSE, VALIDATE, SCRIBE
Continues `laneZ_addendum5_...md`. **2 further commits (~51 this session).** **Zero crons, whole session.**

---

## 1. ⭐ THE FABRIC SELF-CORRECTED FOUR TIMES IN TWENTY MINUTES AND NOTHING WRONG REACHED THE PAGE

```
AE~Z    finds a real payload defect, TITLES it as a display defect
DE~Z    RENDERS the page on the exact served bytes -> refutes the display half
AE~Z    retracts in 77 seconds: "I PUT THE BOUND IN THE BODY AND THE OVERCLAIM IN THE SUBJECT"
DS~Z    supplies provenance AGAINST THEMSELVES: their own commit invalidated a true constant
CVO~Z   corrects the REPAIR ORDER: fixing the key alone is WORSE THAN THE DEFECT
```
⭐ **DS~Z's framing is the one to keep: `alloc_fixed_income: 0.0` was TRUE BY CONSTRUCTION.**
`ASSET_CLASS_FIXED_INCOME` occurred **zero** times before `@0c03c359f2`; a book could not hold fixed
income, so the literal was a **fact**, not a placeholder. **Nobody hardcoded a lie — a vocabulary
widening invalidated a true constant from a distance.** `alloc_fixed_income` occurs ONCE before and
ONCE after: **no diff on that line exists, so no review could have caught it and no test failed.**

---

## 2. ⛔ MY FOUR DEFECTS THIS STRETCH — AND THEY COME IN TWO OPPOSED PAIRS

| # | defect | caught by |
|---|---|---|
| 24 | **Drafted AC8's invariant as "the buckets sum to 100."** They sum to **99.80 / 99.51** because the HOLDINGS do. **It would have FAILED ON A CORRECT BUILD** — the exact pinned-constant defect DS~Z flagged me for ONE MESSAGE EARLIER | measuring instead of assuming |
| 25 | **Sealed DE~Z's untested REMEDY into `AC9`** four minutes after writing *"an instruction not to re-derive is an instruction not to CHECK"* — in the same document | DS~Z measuring their own input |
| 26 | **Then drafted "route this to Andrew"** — a question he had **already answered** (*"whatever we can get"*) | CTO~Z finding the sentence |
| 27 | **Released the deploy batch on "both halves are in the tree" WITHOUT CHECKING PUSH STATE** — while labelling my OWN commits *"LOCAL, rides integration"* in the same message | DS~Z, re-measured at my seat |

>> **#25 and #26 are one root in both directions: NOT RE-READING WHAT I ALREADY HELD.** `ECONOMY_ORDER`
>> reached me **by name, with its path, at 23:28:39Z** and was re-broadcast with its exact values —
>> **I held the right constant for 3h44m and wrote a criterion around it without opening it**,
>> including the `65/90/95` entries that would have shown in one glance it is not a GICS list.
>> ⭐ **CVO~Z's formulation, and it indicts the COO specifically: *A FACT IN THE CHANNEL IS NOT A FACT
>> IN THE NEXT DECISION.* Making it one is the whole of my job.**

⛔ **AND #26 IS THE HARDER LESSON: OVER-CAUTION IS NOT THE SAFE SIDE.** Escalating a settled question
spends the sovereign's attention and stalls delivery — **and it FEELS like rigour, which is why the
under-cautious version was caught by a peer in four minutes while the over-cautious one survived
three revisions of my own amendment.** *The failure mode with better optics is the one that lasts.*

⛔ **#27's shape: I applied the push-state discipline to the artifacts I AUTHORED and not to the ones
I was AUTHORIZING ACTION ON.**

---

## 3. ⭐⭐ THE FINDING THAT OUTLIVES TONIGHT — THE INTEGRATION WINDOW **BIASES TOWARD PUBLISHING ERRORS**

Measured, `git branch -r --contains`, two artifact classes, one hour:
```
CODE   4c234af208  WRONG sector order    remote=1  PUBLIC   |  3e8739832d  its fix        remote=0  PRIVATE
SPEC   f447257f56  my DEFECTIVE AC9      remote=1  PUBLIC   |  8ba66cba88  its retraction remote=0  PRIVATE
```
>> **A CORRECTION IS ALWAYS YOUNGER THAN THE THING IT CORRECTS. Under a batched integrator-only push,
>> THE ERROR CATCHES A WINDOW ITS FIX MISSES — systematically, not by luck. The window does not merely
>> DELAY corrections; it makes errors MORE LIKELY TO BE PUBLIC THAN THEIR REMEDIES.** <<
⛔ **The SPEC instance is the worse one: a criterion is an INSTRUCTION. Any seat pulling `origin` read
`ETFS-TO1-AC9` in its defective form — the version that would have them revert a possibly-correct
commit toward something unbuildable — and found no retraction.** **Publishing an instruction while
withholding its cancellation is worse than publishing neither.** This is CLAUDE.md's own third-surface
clause (LD-0367) firing **on the file that documents it.**

---

## 4. WHAT I VERIFIED MYSELF, AND WHAT I EXPLICITLY DID NOT

✅ **Measured on the served bytes (122,825 B @02:50:38Z):** `alloc_cash` **IS**
`sum(weight WHERE asset_class IN {Fixed Income, Cash})` **to the cent on all four books** — which made
the post-fix expected values a TABLE, not a derivation. **A real `Cash` class exists on PFDE (+0.03)
and PFOE (−0.02), one NEGATIVE** — so zeroing `alloc_cash` would swap one literal for another.
✅ **Verified in SOURCE that the binding repair order held** — all three sums on `asset_class`, both
halves in ONE commit, so the "weight lands nowhere" regression cannot occur at any intermediate state.
⛔ **STATED PLAINLY IN THE RELEASE: I did NOT run the exercise. A source read cannot discharge an
EXERCISED criterion, including mine.**

⚠ **NEW OBSERVATION-CLASS ITEM (not blocking, carded):** `:785` — the **third** aggregation
(`sector[...]` map) is **still keyed on the raw `is_cash` flag** while `cash_w`/`eq_w` moved to
`asset_class`. **It is right TODAY only because `Ultra Short Duration` is not a GICS sector — right by
COINCIDENCE, not by intent.** A future row with `is_cash=False` and a non-GICS `sub_asset_class` enters
`segment.sector` and breaks DE~Z's axis silently. **Unchanged by tonight's commits, so no regression.**

---

## 5. STATE FOR A SUCCESSOR

```
DEPLOY #7   COMPLETE 03:24:21Z. Byte-identity acceptance (54,674 B, b80f8af6a942ce50) -- AE~Z chose
            this over a token census deliberately: a token list only proves the tokens you thought to
            name. Ledger opened + closed.
PUBLISH     *** NOT DONE. Served key still 122,825 B @02:50:38Z, ETag 46c7322e. ***
            DEPLOYED != PUBLISHED. Owner NAMED: 0.4.0_DS_ClientPlatform~Z, item 1 of the routing.
PUSH        3e8739832d + 8ba66cba88 remote=0. Requested of 0.0.0_AB_MSTR~Z. NOT a hold on anyone;
            DS~Z's local-HEAD deploy path is available and was used.
```
**ANDREW'S TWO NEW ASKS (~03:2xZ), sequenced — and TWO OF THREE NEED NO BLOOMBERG CALL:**
```
1  PUBLISH                          delivers the sector order HE reported          DS~Z, now
2  ASK 2 sub-asset-class weights     pure holdings arithmetic, no deps             DS~Z
3  ASK 1a bbg-testpull plumbing      PFDE 97% / PFOE 92% -- 5.6yr of daily data
                                     ALREADY IN OUR BUCKET that load_history()
                                     has NEVER READ. Absorbs smoke item 2.         DS~Z
4  ASK 1b DIVZ/IDVZ backfill         *** CARD AT ANDREW -- VENDOR EGRESS ***       not work
```
⛔ **Item 4 does not start: "he asked for the outcome" is NOT his word on the egress.**
⚠ **Item 3 is a COLUMN BRIDGE, not a schema match, and CTO~Z explicitly said to VERIFY the 08-20/08-21
abutment rather than inherit it** — a relayed measurement in a spec stops being a claim and becomes an
instruction.

**Still open, unchanged:** 11:00Z ADR pre-check · 13:00Z `ETFS-TO5-AC7` (**discriminate on
`run_class: scheduled`, NOT on the artifact existing** — an ad-hoc `date=2026-08-24` gold run is
already in the prefix) · `:1375` partition key · yield coverage · TPG `2602335D`.
