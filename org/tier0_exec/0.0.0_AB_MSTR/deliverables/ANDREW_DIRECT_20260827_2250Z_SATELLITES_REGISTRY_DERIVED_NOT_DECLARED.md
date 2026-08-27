# ANDREW-DIRECT 2026-08-27 ~22:5xZ -- THE SATELLITES REGISTRY IS DERIVED, NOT DECLARED

**Received at:** the `0.0.0_AB_MSTR~Z` terminal, in answer to "maintaining what registry?"
**Recorded by:** `0.0.0_AB_MSTR~Z` -- VERBATIM, broadcast same turn per `org/XXX.md`.

---

## 1. VERBATIM. THE PHRASING IS THE RULING.

> "This shouldnt be handdrawn at all, it should simply be "Does it say 'Opal Satellite' in the
> name? Add it and track henceforth if so. If an Opal Satellite disappears from daily pulls, now
> it is no longer tracked.""

## 2. WHAT IT RULES

| # | ruling | source phrase |
|---|---|---|
| R1 | The registry is NOT hand-maintained | *"shouldnt be handdrawn at all"* |
| R2 | MEMBERSHIP IS A NAME TEST on the daily pull | *"Does it say 'Opal Satellite' in the name?"* |
| R3 | ADD on match, automatically | *"Add it and track henceforth if so"* |
| R4 | REMOVE on absence from daily pulls | *"disappears from daily pulls, now it is no longer tracked"* |

**THIS RETIRES THE DECLARED-SET DESIGN.** `SATELLITE_MEMBERS` (nine hardcoded rows,
`REGISTRY_CLAIM = 'held'`) becomes DERIVED STATE. The open maintainer question is DISSOLVED, not
answered: there is no row for a human to add.

## 3. THE MECHANISM ALREADY EXISTS AND IS ONE LINE FROM BEING THE ANSWER

`data/assets/scripts/gold/satellites_registry.py`:
```
:219  CANONICAL_NAME_FORM = re.compile(r"^Opal Satellite (\d+)$")
:222  def canonical_roster_names(rows) -> set[str]
:213  # THE CANONICAL FORM -- used ONLY by the drift oracle, NEVER as a membership test.
```
**His word promotes the oracle to the membership test.** The sweep, the anchors and the
`name`-not-`displayName` choice are all already built and reasoned.

## 4. ONE QUESTION HE SETTLED SAME-TURN, ONE STILL OPEN

**(a) SETTLED BY HIM, SAME TURN, BEFORE THIS RECORD COMMITTED. VERBATIM:**
> *"There is a formatting i would say that is viable"*
> *"if it says 'opal satellite with some other shit' that is not acceptable"*
> *"if it is formatted as the other opal satellites then its fine"*

**THE TEST IS FORMAT-CONFORMANCE, NOT SUBSTRING.** A name must be formatted AS THE OTHER OPAL
SATELLITES ARE; trailing extra text disqualifies. **That is exactly the built
`^Opal Satellite (\d+)$` -- anchors and all.**
```
Opal Satellite 55            -> MEMBER    (formatted as the others)
Opal Satellite 50 Tax-Free   -> NOT a member ("with some other shit")
Core | Satellite 98          -> NOT a member (no leading form)
Opal Sat 50+ 15% cash        -> NOT a member (abbreviated; it ALLOCATES to a satellite)
```
>> **THE ANCHORED REGEX ALREADY IN THE FILE IS THE RULING, VERBATIM. It is not one line from the
   answer -- IT IS THE ANSWER, and it needs promoting from oracle to membership test, not
   rewriting.** The `^...$` anchors that the file justified as drift-surfacing are the very thing
   his "formatted as the other opal satellites" requires. <<

**(b) THE REMOVAL HALF HAS NO MECHANISM.** R4 is new. `drift_report` returns both directions of
the symmetric difference and the caller FAILS on either; nothing auto-removes. Removal-on-absence
needs a trigger definition (absent for how many pulls? one? a trading day?) and that is not stated.

## 5. RECONCILING WITH HIS EARLIER RULING -- OBSERVATION, NOT A CLEARANCE

The module records the name route as disowned: *"As a MEMBERSHIP PREDICATE the canonical name form
is wrong and Andrew ruled it so"*, resting on his IS-A vs HOLDS-A word:
> *"Some SMA that has a blend of a Satellite and Opal Model is not a Satellite, they merely are
> allocating to a Satellite."*

**These may not conflict.** The blend the file names is `Opal Sat 50+ 15% cash` -- **"Opal Sat",
NOT "Opal Satellite"** -- so a literal `Opal Satellite` test EXCLUDES it, which is exactly what his
earlier criterion demands.

> **BOUND: that is ONE blend name, read from the module's own prose. I did NOT sweep the roster.**
> Whether every allocator abbreviates and every satellite spells it out is UNMEASURED and is the
> first thing the builder should test, with both controls.

## 6. ROUTING

`1.0.0_SA_CTO~Z` issues ETFS_SATELLITES TOs and owns the arch call. `2.0.0_SA_COO~Z` seats --
note `TO-2`'s assignee `0.4.0_DS_ClientPlatform~W` is DEAD. `3.0.0_SA_CVO~Z` holds the
certification that rests on the declared set. **No gate is created by this record.**
