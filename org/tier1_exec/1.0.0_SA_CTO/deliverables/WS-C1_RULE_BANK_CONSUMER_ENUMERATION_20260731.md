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

## STALE READERS FOUND: ZERO. BOTH APPARENT HITS WERE FALSE POSITIVES, FOR DIFFERENT REASONS

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

**I CREATED THIS.** I renamed in one rail while the name stayed live in the other. That is exactly
the trap `~C` fell into: their `_UNIVERSAL_REQUIRED` held `scope`, which would have been RIGHT had
they been reading the type_tuple.

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

>> **SO THE ENUMERATION CANNOT FIND, IN THE GENERAL CASE, THE THING IT WAS BUILT TO FIND.** It
closes the STALE-READER class (a reader holding an OLD name I once published) and does NOT close the
FORKED-VOCABULARY class (a reader that never used my names). Those are different classes and only
the first is now covered. <<

**Residual, stated rather than resolved:** `.sh` readers = 0 measured; `.md` references are prose
and unenforceable; a reader reaching the bank through an intermediary is uncounted. The
FORKED-VOCABULARY class has no instrument and I am not claiming one.
