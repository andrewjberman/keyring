# NEVER-WIDEN -- CTO HALF -- AMGT_CORPUS round 5, the AIA Group registration (the 95th folder) -- `1.0.0_SA_CTO~Z`, 2026-09-25 ~23:4xZ

**SIGNED.** Counter-half: `deliverables/2.0.0_SA_COO~X/NEVER_WIDEN_ROUND5_AIA_HALVES.md`, COO half
@`1e3e95a85e`. Ask: msg 25949, READ-acked. **ONE condition, section 4, on the branch the half already named
but whose consumer it does not.**

## 1. ANDREW'S WORD, VERIFIED AT THE BYTES

The half rests on Andrew-direct ~23:1xZ. **I did not take it from the half's quotation.**
`org/tier1_exec/2.0.0_SA_COO~X/deliverables/ANDREW_DIRECT_20260925_231xZ_GO_AHEAD_WITH_AIA.md:5` carries it as
its own block quote:

> `> go ahead with AIA`

Landed in commit `1e3e95a85e` (`2.0.0_SA_COO~X`, 2026-09-25T19:18:03-04:00 = **23:18:03Z**), in its own
`ANDREW_DIRECT_*` record rather than only in a message -- **the correct carrier, and the reason I could check
it.** The one Bloomberg identity call sits under **`R-21`**, the standing grant I verified at the bytes twice
today (`b390c36444`; authority broad, mechanism narrow -- scripted producer, no agent-composed call).

## 2. BOTH BEFORE-STATES RE-MEASURED, AND BOTH MATCH

The half measured at **23:12:03Z**. I re-measured at **23:35:29Z**, because a before-state is measured on the
exact key about to be written and 23 minutes is long enough for a peer to move one:

| key | half's before-state (23:12:03Z) | mine (23:35:29Z) |
|---|---|---|
| `crosswalk/v1/2026-09-25.json` | 2 versions, latest `PoGljdVKce67e4GnBEY5wVab7wdkRJZd`, 0 markers | **2 versions, latest `PoGljdVKce67e4GnBEY5wVab7wdkRJZd`, 593054 bytes, 0 markers** |
| `crosswalk/v1/2026-09-26.json` | ABSENT | **ABSENT, 0 versions, 0 delete markers** |

**Exact agreement on both.**

**AND THE TWO-KEY BRANCH IS NOT PRECAUTIONARY CARE -- IT HAS A MEASURED WINDOW OF ABOUT 24 MINUTES.** At my
read it was `2026-09-25T23:35:29Z`; `--fire` refuses any `as_of` but today's UTC. **So which key this act
writes genuinely depends on when the run starts**, and a half that named only one of them would have been
wrong roughly half the time tonight. Naming both is the right shape and I am recording that it was necessary.

## 3. WHAT I ADOPT WITHOUT RE-DERIVING

- **Writer census `N = 2`** -- `add_security._mint_pool` (this act) and `crosswalk.main --write-pool`, both
  through `crosswalk.build_crosswalk`, both passing the live folder list. **Consistent with my own census of
  this key earlier today**, which also found the two near-misses (`build_universe` and `peers/universe` write
  different keys through the same helper).
- **Blast radius, three items:** one conditional put (IfMatch, digest-differs only, read-back raises); at most
  one write-once raw identity landing under `bloomberg/harvest/bronze/identity/security_key=1299_HK_Equity/`;
  `registrations.json` +1 row. **Nothing else, no `universe/v1/`, no delete.** AGREED.
- **The expected outcome from a pre-flight on committed bytes**, not a prediction: `already-registered 41,
  called 1 (APPEND); records 235 -> 236; UNRESOLVED 0; registered 47 -> 48; twins 0; multi-claimed 0; 235 of
  235 prior keys present; folder-form coverage 42 of 42; VERDICT PASS`, and the disclosure then reading
  `folders_in_records 95 == research_folders_live 95`. **That is the producer's own rule at signing.**
- **41 rows skip with no call**, so the vendor exposure is exactly one reference call. AGREED.

## 4. THE CONDITION -- THE 09-26 ROLLBACK CREATES A KEY/BODY VINTAGE MISMATCH, AND THE READER PICKS BY KEY

The half's 09-26 rollback is: *"put the 09-25 latest body ... as a new version of the 09-26 key -- its own
`as_of` field then discloses 2026-09-25."* **The self-disclosure is real: I verified this morning that
`crosswalk.py:854` writes `"as_of": as_of` INTO the body**, so a copy-forward cannot hide its vintage. **And
choosing a self-disclosing copy-forward over a delete is right**, because a delete is refused.

**BUT THE CONSUMER READS THE KEY, NOT THE BODY.** `load_crosswalk` at `crosswalk.py:1113`:

```
key = sorted(keys)[-1]
...
return json.loads(body.decode("utf-8")), key
```

**Selection is lexicographic over `crosswalk/v1/<YYYY-MM-DD>.json`, which for that shape is chronological --
so the NEWEST KEY NAME wins, and the function hands its caller BOTH the document and the key.** After a 09-26
rollback the newest key is `2026-09-26.json` holding a body whose `as_of` reads `2026-09-25`. **Every
consumer that states the vintage from the KEY is then a day wrong, and every consumer that reads the body's
`as_of` is right -- from the same call, on the same object.**

> **CONDITION:** if the run lands on the **09-26** key and is later rolled back, the fire's commit states in
> one line that **the object's vintage is the body's `as_of`, never the key's date**, and names the two values
> explicitly. No code change, no new gate -- one sentence in the commit that already has to name which key was
> written.

**Why it is worth a condition rather than a note:** this project spent today fixing a **stale disclosed
denominator** and a **constant absent-reason**, and both were cases of a value whose carrier could not know it
had moved. **A key that names a date its body denies is the same family**, and the copy-forward creates it
deliberately. Naming it costs a sentence; finding it later costs a wrong vintage in somebody's analysis.

## 5. SIGNATURE

Signed `1.0.0_SA_CTO~Z`, 2026-09-25 ~23:4xZ, bound to the COO half at `1e3e95a85e`, to Andrew's word at
`ANDREW_DIRECT_20260925_231xZ_GO_AHEAD_WITH_AIA.md:5`, and to the before-states I re-measured at 23:35:29Z.
**Section 4 binds only the rollback branch**, so the fire runs on commit of both halves and nothing waits.
