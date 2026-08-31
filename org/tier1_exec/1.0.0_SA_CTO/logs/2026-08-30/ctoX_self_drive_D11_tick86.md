# /self-drive D11 -- tick 86 (21:17Z measured, written 21:33Z)

**archetype:** VALIDATE
**secondary_archetypes:** COORDINATE, SCRIBE

- seat: `1.0.0_SA_CTO~X` (design lane) -- cron **31950a5f**, 60m at :11; paired with `/drive D11 @ 2.0.0_SA_COO~X`
  (+15m). ticks covered: 86. state: **ARMED**. The log was DEFERRED past the tick's own measurements to complete
  the card-6 design read first -- the work, then the record.

## Steps (tick 86)

- Step 0 register: 12 live directives; D11 -> 2 members, both `active` / `EXECUTING`; claims scan 342 JSONs, 1
  PRD-path claim (a member); **open TOs 2**; `to-check` scanned 2224. 2 of 2 REACHABLE.
- Step 1 /open-calls scoped D11: **2 CARRIED at Andrew, 0 BLOCKING**, unchanged. Step 2: no pitch, no adjudicable
  call opened; both certifier seats LIVE. Step 3: 0 CVO verdicts in the loop sense; ledger 21 rows, 0 unconsumed.
  Step 4: **NOT DONE -- 0 of 2** `complete` (denominator 2).
- ⛔ **THE CARRIED HELD-ITEMS LIST IS EMPTY AND STAYS EMPTY.** The standing invocation still names four design-lane
  held items; all four were measured DISCHARGED at tick 85 and are NOT re-transcribed. The owed list below is
  DERIVED from measured state, per the correction at 89204.

## Delta since tick 85 (21:10Z -> 21:33Z)

1. **CARD 6 `19f0a0d69f`: I READ IT "NO FINDING", `4.0.0_SA_CRO~X` STOPPED IT, AND THE STOP WAS RIGHT.** Four
   carriers assert an unscoped LIFETIME claim -- `/subject/declared_domain` "never again",
   `/process/methodology/evidence` "not run again", `/process/cadence/actual_trigger` "then nothing",
   `/verdict/why` "never touched again" -- against `/process/cadence/evidence`, which correctly says the lifetime
   count needs the snapshot HISTORY and is UNMEASURED. **4 of 4 confirmed at the pin, 76 string leaves scanned.**
   ⛔ **HOW I MISSED IT IS THE INVERSE OF THE LESSON I RECORDED THIS MORNING.** That one says: a defect confirmed
   in one field means census EVERY field for that class. **I did the mirror image -- found the scoping done
   CORRECTLY in one field and generalised it to the card.** Finding something done RIGHT in one field and
   generalising is the same error as finding something WRONG in one field and stopping, and it is more seductive
   because it feels like verification rather than a shortcut.
   ⛔ **AND MY OWN CENSUS NEARLY FILED A WRONG COUNT AGAINST THE CERTIFIER'S.** It flagged `/verdict/why` as
   CO-SCOPED because the field contains a "QUALIFIED" list -- I was one send from replying "4 assert it, 1 is
   already scoped, so the set is 3." **I opened the field instead of quoting the regex: those qualifications
   govern the MATERIALIZER and the KEY row, not the lifetime claim. PROXIMITY IS NOT GOVERNANCE.**
2. ⛔ **THE SAME DEFECT WAS IN CARD 5 `0db07bb687` -- CLOSED, CERTIFIED BY BOTH SEATS, COUNTED AND ON ORIGIN.**
   `0.7.0_AE_CloudOps~X` found it by CENSUSING THE CLAIM ACROSS ITS OTHER CARDS BEFORE REPAIRING THE ONE IT WAS
   TOLD ABOUT, and disclosed it unprompted. `4.0.0_SA_CRO~X` withdrew its card-5 certification half and reopened
   that joint close narrowly; the wave count is **PROVISIONAL 4-of-7**, not 5-of-7.
3. **RULING (mine, asked for): SUCCESSOR, NOT ERRATUM.** Three reasons in order of weight -- (a) the CARD is what
   consumers read and an erratum lives elsewhere, which is tonight's carrier lesson four times over; (b)
   CERTIFICATION ATTACHES TO BYTES, so an erratum leaves both passes on an artifact that contradicts itself;
   (c) the cost is one cut and ZERO re-measurement, so "a ruling that resets a correct candidate is a bad ruling"
   does not apply -- the candidate is not correct and its own evidence says so. Concurred with the provisional
   count: a count resting on a withdrawn certification half should read provisional rather than hold on momentum.
4. **FABRIC-WIDE CENSUS BEFORE RULING -- 1,439 string leaves across ALL 18 tracked v3.1 cards.** Card 5: 5
   carriers. Card 6: 4. **A THIRD card nobody had named -- `fedobs_coverage_snap`, also CLOSED -- at 1 carrier.**
   **15 of 18 CLEAN.** ⛔ **I did NOT collapse the third into the same finding:** cards 5 and 6 are INTERNALLY
   CONTRADICTORY; on `fedobs_coverage_snap` I looked for a contradicting carrier and found none, so it is
   uniformly unscoped rather than self-contradictory -- a different shape, surfaced to the certifiers as their
   call on their own closed card, not asserted as the same defect. **`0.7.0_AE_CloudOps~X` split it on better
   grounds than mine:** its claim rests on a NAMED PARK RECORD carried as HELD plus a three-plane trigger census,
   **not on surviving snapshots alone** -- what the sentence is ENTITLED to say, rather than whether another
   sentence disagrees.
5. **7A `ff645d8de1`: CVO PASSED IT, I PASSED IT 21/21, `4.0.0_SA_CRO~X` STOPPED IT, AND THE STOP WAS RIGHT.**
   Full-file equality was TAUTOLOGICAL: `body` comes from the same regex under test, so
   `stripped == OPEN + body + CLOSE` reconstructs the file whenever it starts with an open and ends with a close.
   Measured: 2 open tags, 1 close, `findall` -> 1 block, equality True. **I reproduced it and found a second
   placement (extra open INSIDE the body).** My PASS is WITHDRAWN.
   ⛔ **MY 21 ARMS WERE DERIVED FROM THE CONTRACT -- THE RIGHT CORRECTION -- AND STILL MISSED IT.** The clause
   reads "exactly one **well-formed** top-level receipt / no narrative wrapper / no second block"; I armed
   *exactly one* with two blocks and *no wrapper* with PROSE, and never armed *well-formed*. **I decomposed the
   clause along the axis THE LAST DEFECT USED.** Malformed markup did not occur to me because nothing had yet
   failed that way -- which is the definition of the axis that bites. **Enumerating a clause's WORDS is not
   enumerating its FAILURE SURFACE.**
6. **7A `8b6fef871f`: DESIGN PASS on 21 arms.** Tag cardinality COUNTED OVER RAW COMMITTED BYTES BEFORE the regex
   runs. Three tag positions armed separately (prefixed open, body-internal open, the mirror extra close) plus a
   control; 9-arm contract regression holds; and I hunted a fifth position in four directions and found none --
   FIELD cardinality (duplicate `<subject>`, `<subject_blob_oid>`, `<kind>`, `<certifier>`), ENCODING (BOM, an
   attribute on the tag), and the file's **git MODE** (a committed SYMLINK receipt -> REFUSED, fail-safe).
   ⛔ **AND I RETRACTED MY OWN FRAMING:** I gave the fabric a "container test" (corpus -> directory -> file), and
   that was the WRONG AXIS. The four positions are four places where **THE CHECK CONSULTED SOMETHING DERIVED FROM
   THE INPUT IT WAS CHECKING.** Tag cardinality differs not by being smaller but by **refusing to consult the
   parse at all.** The invariant to carry: *is any part of the expected value computed from the thing under test?*
   The issuer's own sentence is the keeper: **"an equality whose right-hand side is rebuilt from its left-hand
   side is not a check, it is a restatement."**
   ⭐ **Its GENERATED matrix fired on its own author for the first time** -- a single-quoted arm name against a
   double-quote scanner meant the arm RAN AND PASSED while reading MISSING in the join: 51/51 green and a NONZERO
   matrix in the same breath. A typed completeness claim survives that; a generated one cannot.
7. **CARDS 5+6 SUCCESSORS `ec96549fcd` -- repair CONFIRMED.** Blast radius exactly 3 paths; both identities
   reproduce; my census: card 5 **2 carriers / 0 unscoped** (was 5), card 6 **1 / 0** (was 4). ⛔ **I DISCLOSED
   THAT MY INSTRUMENT IS NOT INDEPENDENT** -- I used the +/-250-char proximity window, which is THAT SEAT'S fix
   adopted from its own post-mortem, so this is its corrected predicate re-run in different code rather than a
   second method. **Its `refuse_unscoped_lifetime_claim()` is the first arm on this face comparing PROSE TO
   PROSE**; both prior arms compare a sentence to a STRUCTURED FIELD and were blind BY CONSTRUCTION, which is why
   a note could not have closed this. Its v1 FALSE-NEGATIVED on the exact carrier the STOP named (a scope word
   ~300 chars away, about a different claim), and it reported that plus three census false positives rather than
   only the shipped result.

## Scope state (denominators printed)

| project | status | dep_stage | open TOs | reachable |
|---|---|---|---|---|
| NFRA_C3MATERIALIZE | active | EXECUTING | 1 (7A at `8b6fef871f`, design PASS, awaiting both certifiers) | YES |
| NFRA_SUBSTRATECARDING | active | EXECUTING | 1 of 9 carding faces open; **count PROVISIONAL 4-of-7**, cards 5+6 successors presented, card 7 gated | YES |

Completion test: **NOT DONE, 0 of 2**. RESERVED cards at Andrew: 2, both CARRIED, neither blocking.
**Owed by this seat (DERIVED, not carried):** the design read of the 7A successor if a certifier stops
`8b6fef871f`; the determination instance against declarations 1-4 when the unit is delivered; Addendum 1p
Amendment 1's narrowed clause; and the two Addendum 1r bindings falling due at the DELIVERING cut (fixture-only
disclosure) and BEFORE the consumer cut (module extraction) -- both owed by the issuer, tracked here.

## Push state (measured 21:33Z)

origin/CLOUD = **`b85904f20e`** (unchanged since 20:53Z). `26a124e480` (tick-85 log), `8b6fef871f` and
`ec96549fcd` all read **LOCAL as measured 21:33Z -- perishable**; null control `ffffffffff` ABSENT. No window is
open (last frame CLOSED 20:53Z), so nothing is held.

## Compiler Tools

| tool | result |
|---|---|
| `python .tools/directives-check.py --json` | 12 live; D11 2 members, open TOs 2 |
| `python .tools/to-check.py --all --project ...` | 1 + 1 PENDING, scanned 2224 |
| lifetime-claim census over 18 tracked cards (1,439 string leaves) | 3 cards flagged, 15 clean; third card a DIFFERENT shape |
| `gate_state()` on committed fixtures in temp git repos (v7, v8) | tautology reproduced in 2 placements; 21 arms on the successor |
| field-cardinality / encoding / git-MODE probes | no fifth position found in four directions (a negative, not a proof) |
| `.tools/substrate-card-check.py` | this lane 6 of 6, whole corpus 18 of 18 VALID rc=0 |
| `git merge-base --is-ancestor` + `cat-file -e` (3-state) | placements as stated, null control ABSENT |
