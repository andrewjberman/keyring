# THE GOAL'S THIRD CLAUSE, MEASURED OVER THE WHOLE POPULATION -- `1.0.0_SA_CTO~Z`, 2026-09-26 ~05:1xZ

**The clause:** *"followed by complete backfill for all of these securities through the opal-data-harvest
channels."* **Supersedes** `ctoZ_GOAL_CLAUSE3_BACKFILL_MEASUREMENT_20260925T2300Z.md` @`8bf8a4fc77`, which
measured 53 of 94 and left the rest UNKNOWN by name.

**That record's own caveat was: *"Not that 41 names have no data. They have no ROW on this route. Whether raw
landed for them is a separate question."* A caveat is a promise to measure. This is the measurement.**

---

## 1. THE RESULT -- the 41 UNKNOWNs are resolved, and the news is good and bad

| channel | landed | denominator | prior record |
|---|---|---|---|
| **bloomberg** | **95** | **95 (100%)** | 53 of 53 over a 53-name slice |
| **seekingalpha** | **3** | **95 (3%)** | 3 of 53 (6%) |
| **serp** | **0** | **95 (0%)** | 0 of 53 (0%) |

**Channel depth, the number that answers the clause:**

| channels landed | names |
|---|---|
| 1 | **92** |
| 2 | 3 |
| 3 | 0 |
| **0** | **0** |

**Population: 95 folders read fresh; 95 of 95 resolved to a security key; UNRESOLVED 0; ERROR 0.**
Elapsed 49 s, 285 ListObjectsV2 reads, read-only.

### What improved
**No name is dark.** The prior record could not say whether 41 of the 94 had any data at all. **They do --
bloomberg landed for every one of the 95, and the count of names with zero channels is 0.** The instrument's
56% coverage was a property of the `freshness` ROUTE's rows, not of the store.

### What got worse when the denominator was honest
**`seekingalpha` fell from 6% to 3% and `serp` stayed at 0%.** The prior ratios flattered the estate because
their denominator was the 53 names the route happened to carry. **On the true population, 92 of 95 names carry
exactly ONE channel.**

> **So clause 3 is ONE CHANNEL DEEP ACROSS THE ENTIRE POPULATION.** *"Complete backfill ... through the
> opal-data-harvest channelS"* is plural. One channel of three, complete; a second at 3%; a third at zero.
> **The clause is NOT met, and it is not met by a wide margin rather than a rounding error.**

---

## 2. WHY THIS IS NOW ANDREW'S EGRESS LIFT'S LARGEST TARGET

`seekingalpha` and `serp` are **vendor** channels. They are empty for the reason `AMGT_HARVST`'s AC1a was
unexercisable: a per-use vendor word no seat may grant itself.

**At ~03:xxZ that word was given** (`ANDREW_DIRECT_20260926_03xxZ_SELF_DRIVE_SITEZ_DIRECTIVES_AS_A_WHOLE.md`
@`f3b85ff6a5`): *"Egress is permitted for API calls this session -- no per-use word per vendor call, but every
call is ledgered by the seat that makes it."*

**So the lift's value is not one task order. It is 92 names x 2 channels.** That is the single largest
addressable block of the goal remaining, and it is addressable tonight rather than after a card.

**Three constraints the lift does not relax, and a producer that ignores any of them is off-law:**
1. **Mechanism.** The lift is on the AUTHORIZATION. The call runs from a **SCRIPTED PRODUCER**, never inside
   an agent turn.
2. **The ledger.** *"every call is ledgered by the seat that makes it"* is a CONDITION, not a courtesy. A
   producer that cannot write its ledger row does not carry the word.
3. **Session scope.** The word is *"this session"*. A queued backfill that starts after the session loses its
   authorization silently, so a producer either runs inside the window or it is a card -- never a cell that
   quietly expires.

**Not covered, and not asked for here:** spend, contracts, entitlements, hold-lifts.

---

## 3. THE INSTRUMENT, AND WHY IT IS THE PRODUCER'S OWN

Addresses were **not typed**. The measurement imports `lib/research/freshness/build_view.py` and calls its own
three landing functions -- `latest_bloomberg_bronze_stamp`, `latest_seeking_alpha_bronze_stamp`,
`latest_bright_data_serp_stamp` -- so every prefix is the producer's, and `NEVER` is read from the module's own
constant (`:108`) rather than inferred from an empty list.

**This mattered twice today.** Five invented S3 prefixes each returned a confident zero, caught only by a
positive control on a known-good name. And `build_view.security_key_for`'s own docstring records the same class
biting its author: *"The FIRST version of this function omitted the yellow key and so matched NOTHING in the
store even for a correctly-resolved name; invisible while the store was empty, caught once real data landed."*
**A store-shaped zero and a key-shaped zero are indistinguishable until something lands.** Reusing the
producer's key builder is the only cheap defence.

**Two guesses of mine were wrong and cost one crash and one correction:** `load_crosswalk()` returns a
**3-tuple**, not a dict; and a record's folder lives at `source_row.folder`, not `research_folder` or
`folder`. Both were fixed by printing `records[0]`'s real keys instead of guessing again.

**Positive control on the ratios:** bloomberg reads 95 of 95 through the same code path that reads seekingalpha
at 3 and serp at 0. **A reader that could not see the store would have returned 0 for all three**, so the
100% arm is the control that makes the 3% and 0% arms trustworthy.

---

## 4. WHERE CLAUSE 3 SITS AGAINST THE OTHER THREE

| clause | state |
|---|---|
| 1. Visually polished Security Analysis app, all AMGT companies folded in | identity layer **95 of 95**; the render is `AMGT_RESAPP` FWD-21..FWD-26, NOT REALIZED |
| 2. Export, Opal Brand Guidelines, 2pg max or machine-readable rich text | `AMGT_RESAPP` FWD-30; a 95-of-95 served claim landed @`2e4382ecd4` and is **owed a re-grade by this seat** |
| 3. **Complete backfill through the harvest channels** | **ONE CHANNEL DEEP over 95 of 95. The furthest from done.** |
| 4. Close out `AMGT_RESAPP` / `AMGT_CORPUS` + addendums | 3 rounds closed tonight; **0 of 18 projects `status: complete`** |

**Clause 3 is the goal's long pole and it just became the most actionable**, which is an unusual pairing and
the reason this record exists rather than a line in a tick log.

## 5. WHAT THIS RECORD ASKS FOR

**One cell, at the issuer's discretion of shape:** a SCRIPTED producer that lands `seekingalpha` and `serp`
for the 92 names carrying one channel, ledgering every call, inside the session window. **It is not a cell I
cut** -- Rule 27 keeps task orders with the COO -- and the never-widen sign-off still governs any served write
it produces.

## Compiler Tools

The producer's OWN landing functions imported rather than any prefix typed, with `NEVER` read from its
constant -- `records[0]`'s real key names printed after two wrong guesses -- bloomberg's 100% arm used as the
positive control that validates the 3% and 0% arms through the same code path -- `library.list_folders` read
fresh for the denominator, never a transcribed 93/94 -- `crosswalk.load_crosswalk()`'s return shape inspected
by type rather than assumed to be a dict.
