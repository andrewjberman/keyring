# WS-C1 -- THE RULE BANK'S CONSUMER SET, ENUMERATED

**CORE-side. Mine, unassigned, not delegated.** Booked as a residual @ff89fb8cd after I renamed
`contract_record.scope` -> `locality` and **could not say who read it**, and after
`0.8.0_AE_CloudComp~C` hit the same rename from the reader side hours later and had a valid
`PERMANENT` declaration silently demoted to `UNDECLARED`.

**This is the MECHANISM half of the lifecycle work and is NOT touched by the Andrew-direct
value-population gate.** It enumerates readers; it populates nothing.

## THE DENOMINATOR, PRINTED

```
python files scanned .................................. 3887
of which NAME the rule bank ...........................   12
of which hardcode a contract_record vocabulary token ..    5
```

## STALE **PYTHON** READERS: ZERO. BOTH APPARENT HITS WERE FALSE POSITIVES, FOR DIFFERENT REASONS

> **HEADING CORRECTED.** This originally read *"STALE READERS FOUND: ZERO."* **That is false outside
> Python** -- see the CORRECTION section below, where ~10 genuinely stale non-Python pins are open
> today. The body was corrected first and this heading was not, which would have left a skimmer the
> exact claim the body retracts.

A token-match on the retired name `scope` flagged two files. **Neither is stale, and the two
failure modes are not the same failure mode:**

| File | Apparent | Actual |
|---|---|---|
| `.tools/tool_index.py` | holds `'scope'` | **Unrelated vocabulary** -- `'scope': 'IN'`, `'follow-on-estate'`, `'excluded-with-reason'`. A tool-registration scope. Pure text-locality. |
| `org/modules/graph/comp_output_contract.py` | holds `'scope'` | **CORRECT AND CURRENT** -- `_VOCAB_FIELDS = ("plane", "grain", "scope")` reads the **type_tuple**, and `/type_tuple/scope` is a live key in the bank. |

## FINDING 1 -- THE BANK CARRIES `scope` IN TWO RAILS, ONE LIVE AND ONE RETIRED

`/type_tuple/scope` is **current**. `contract_record.scope` was **renamed to `locality`**.
**The same token is simultaneously correct and stale depending on which rail a reader is in, and
the token does not carry that context.**

This is exactly the trap `~C` fell into: their `_UNIVERSAL_REQUIRED` held `scope`, which would have
been RIGHT had they been reading the type_tuple.

> **ATTRIBUTION RETRACTED HERE, NOT ONLY AT THE FOOT.** This paragraph originally opened *"I CREATED
> THIS."* `3.0.0_SA_CVO~Z` corrected it -- **A9.1 ruled the two-rail state deliberately** -- and the
> retraction was landed at the bottom of the file while this copy still asserted it. **See ATTRIBUTION
> CORRECTION below. The defect neither of us named is that A TOKEN CANNOT CARRY ITS RAIL.**

**CONSEQUENCE FOR THE PROPOSED OBLIGATION.** `3.0.0_SA_CVO~Z` proposed, and I adopted, that *"a
ratified rename carries an obligation to assert every reader's field list against the bank,
mechanically."* **As stated it is under-specified: assert against WHICH SECTION.** A reader
mirroring its field list against a FLAT UNION of bank names would pass while holding a retired
name, or fail while holding a correct one. **The mirror must be `(section, field)`-keyed, not
`field`-keyed.** `~C`'s C9l is correctly built -- it asserts against
`contract_record.required` specifically, not against a union.

## FINDING 2 -- A BLIND CONSUMER, AND IT IS A KEYSTONE I ARCH-GATE

`org/modules/graph/comp_debt/dormant_guard.py` **holds `revalidate_by` and never names the bank.**

It is not a minor reader. Its own docstring: *"the comp-debt KEYSTONE ... THE governance guard, the
thing that must NEVER false-decommission a deliberate belt,"* and *"CTO arch-gates this
specifically."* It carries:

- **`KEEP-DORMANT`** states (REGISTERED / ANNOTATED / FAILSAFE) -- the same concept as the bank's
  `DORMANT` lifecycle class, where absence or zero traffic is the DECLARED HEALTHY STATE.
- **its own decay rule** -- *"RULING 1: every registry entry carries a `revalidate_by`. An entry
  PAST its window..."* -- the same concept as the bank's `revalidate_by` falsifier decay.

**TWO CONVERGENT VOCABULARIES FOR ONE CONCEPT, IN TWO TOOLS I GATE, NEITHER REFERENCING THE OTHER.**

**WHAT I AM NOT CLAIMING:** that this is a defect, or that the two should be merged. They may be
deliberately separate registries. **What IS established is that the coupling is invisible in both
directions** -- a bank rename cannot reach `dormant_guard`, and `dormant_guard`'s RULING 1 cannot
reach the bank. **If they are one vocabulary, the estate has a silent fork; if they are two, nothing
records that decision.** Routed to the WS-C1 round-2 design decision, which is already mine.

## THE BOUND ON THIS ENUMERATION ITSELF -- AND IT IS SEVERE

**This method is TOKEN-based. It finds a consumer only if that consumer SPELLS a name the bank also
spells.**

**I found `dormant_guard` by luck.** It shares exactly ONE token with the bank (`revalidate_by`).
Its `KEEP-DORMANT` states share the CONCEPT with `DORMANT` and share no token at all. **A fully
forked vocabulary -- same concepts, different words -- is INVISIBLE to this instrument, and a
vocabulary fork is precisely the thing whose words have diverged.**

>> **SO THE ENUMERATION CANNOT FIND, IN THE GENERAL CASE, THE THING IT WAS BUILT TO FIND.** It does
not close the FORKED-VOCABULARY class (a reader that never used my names). <<

## CORRECTION -- MY CLASS CLAIM WAS ONE WORD TOO WIDE. `3.0.0_SA_CVO~Z`, VERIFIED.

I originally wrote that this "closes the STALE-READER class." **It does not. It closes it FOR
PYTHON.** I bounded the METHOD (token-based) and never bounded the CORPUS. **I asked CVO~Z to
verify the bound rather than the findings; the bound is where the defect was.**

```
POSITIVE CONTROL   .py naming the bank ...............  12   (matches the original scan)
NON-PYTHON naming the bank, excl. .md ................  28   (CVO~Z's count, reproduced exactly)
NON-PYTHON naming the bank, incl. .md ................ 116
      .md 88   |   .yaml 18   |   .json 10
```

**THE NON-PYTHON READERS OUTNUMBER THE PYTHON ONES 28-to-12** -- and this is a **SCOPE blindness in
the denominator**, sitting *inside* the class I claimed to close, not the forked-vocabulary blindness
I did declare. My original residual line waved at this (*".md references are prose and
unenforceable"*) and **the hand-wave concealed it: the live instances are `.yaml` and `.json`
configs, not prose.**

### AND A SECOND DISCRIMINATION THE RAW COUNT DOES NOT MAKE

The bank is at **v1.8**. A scan for older pins returns ~40 hits, and **most are NOT stale readers:**

- **A LOG, HANDOFF, INBOX MESSAGE or TASK ORDER pinning `v1.7` is a CORRECT HISTORICAL RECORD** --
  it was true when written, and "correcting" it would falsify the record. Counting these as stale
  readers would be the same could-map-therefore-does error the `scope` false positives already were.
- **A TENANT CONFIG or ONTOLOGY DEFINITION pinning `v1.2` IS a stale reader** -- it is meant to be
  current. Live instances, confirming CVO~Z's counterexample: `infra/system/sdk/**` (6 `.yaml`
  + `gensdk/scaffold.py`, all `v1.2`), `infra/system/ontology/SYSTEM_DEFINITIONS.yaml` (`v1.4`),
  `infra/system/ontology/{C0_C1_C2_C3_C4_SYSTEM_LAYERS,DOMAIN_AND_PREDICATE_ERROR_CLASSES}.md`
  (`v1.2`).

>> **DISCRIMINATING A RECORD FROM A READER IS ITSELF UNAUTOMATED, AND IT IS NOT A DETAIL** -- an
instrument that flags every version mention produces ~40 findings of which most are correct-as-written.
**That failure mode does not under-report, it FLOODS -- and a flooding instrument gets ignored, which
is how the ~10 real ones stay open.** No instrument is claimed for this discrimination. <<

### CORRECTED CLASS CLAIM

> **The enumeration closes the STALE-READER class FOR PYTHON CONSUMERS ONLY.** It does not close it
> for non-Python consumers (28 non-`.md` files name the bank, with ~10 genuinely stale pins open
> today), and it does not close the FORKED-VOCABULARY class in any language.

**THIRD BLINDNESS, named by CVO~Z, class-flagged and NOT asserted as an instance:** a reader that
**constructs field names dynamically** -- from config, or by iterating a schema -- holds no literal
token and is invisible for a third distinct reason. **Neither of us has measured whether one exists.**


## CORPUS EXTENDED TO NON-PYTHON -- AND IT FLOODED, EXACTLY AS L-15 PREDICTED

Discharging L-14 on my own instrument. Scanned `.yaml/.yml/.json/.ts/.js/.sh` for
`contract_record` vocabulary tokens as mapping keys. **50 files hit. The signal after
discrimination is ZERO new stale readers, and the noise is instructive.**

**FALSE POSITIVE, DECISIVE:** `org/modules/graph/potion/model/tokenizer.json` scored **5 of 10
vocabulary tokens** -- the highest non-declaration score in the corpus. It is a **680 KB ML
tokenizer vocabulary**: `"composure": 22625, "cadence": 22626, "seafood": 22627`. Five English
words with integer IDs. **It ranked above every real file.**

**FALSE POSITIVE, REPEAT OF A KNOWN ONE:** `comp-tools.yaml` and `comp-coverage-map.yaml` carry
`scope:` with values `IN` / `follow-on-estate` / `excluded-with-reason` -- **byte-identical in kind
to the `tool_index.py` false positive already recorded above.** The same unrelated axis, found again,
by a scan written after the first one was documented.

>> **AND THE LOCATION PROXY DID NOT SAVE IT.** I tagged files `RECORD-ish` vs `READER-candidate` by
path (`/logs/`, `/inbox/`, `/handoffs/`). **`tokenizer.json` is a `READER-candidate` under that
proxy.** The proxy is not the consumer test and it does not approximate it. **I predicted flooding
in L-15 and then built a flooding instrument in the next increment** -- knowing a failure mode by
name does not immunise you against writing it. <<

### THE DISTINCTION THIS FORCED, AND I HAD BEEN CONFLATING IT

**There are TWO staleness axes here, with different mechanisms and different consequences:**

| | **AXIS A -- STALE FIELD NAME** | **AXIS B -- STALE VERSION PIN** |
|---|---|---|
| Shape | a reader holds `scope` after the rename | a config pins `v1.2` while the bank is `v1.8` |
| Instance | `~C`'s `_UNIVERSAL_REQUIRED` | `infra/system/sdk/**`, `SYSTEM_DEFINITIONS.yaml` |
| Consequence | **silent misresolution** -- a valid `PERMANENT` demoted to `UNDECLARED` | may be **deliberate** (a tenant pinned on purpose) or may mean written-against-old-vocabulary |
| Found by | token scan | version scan |
| Non-Python instances | **ZERO, measured** | **~10, CVO~Z's** |

**CVO~Z's counterexample is AXIS B. My enumeration measures AXIS A.** Both are real; they are not
the same finding, and my accepting "the stale-reader class is not closed" without splitting them
credited my instrument with a miss it did not have and left Axis B unowned. **The corrected claim
stands -- Axis A is closed for Python only -- but the non-Python Axis A population, now measured,
is EMPTY rather than unknown.**

### WHAT THIS MEANS FOR THE DISCRIMINATOR'S PLACEMENT

CVO~Z ruled that record-vs-reader is a **consumer** question and therefore belongs to this
enumeration. **Accepted, and this increment is the evidence for the harder half of it:** a token
scan plus a path heuristic cannot do the job at any corpus size -- `tokenizer.json` proves the token
half fails and the path half fails simultaneously on one file. **The discriminator needs to know what
LOADS a file, which is a dependency-graph question, not a text question.** No such traversal exists
for `.yaml`/`.json` config today and **I am not claiming one, not approximating one, and not shipping
the heuristic under the discriminator's name.**

## ATTRIBUTION CORRECTION -- THE TWO-RAIL COLLISION IS NOT MINE

I wrote *"I created this."* **CVO~Z corrected it and they are right: A9.1 ruled the two-rail state
DELIBERATELY** -- their words, *"leaving `scope` to mean only the ratified denominator boundary."*
I executed a ruling; I did not slip.

**What NEITHER of us named is the actual defect: A TOKEN CANNOT CARRY ITS RAIL.** `scope` is correct
in `type_tuple` and retired in `contract_record`, and nothing in the token says which. **That is a
property of the rename, and the reason the `(section, field)` keying is mandatory rather than tidy.**
