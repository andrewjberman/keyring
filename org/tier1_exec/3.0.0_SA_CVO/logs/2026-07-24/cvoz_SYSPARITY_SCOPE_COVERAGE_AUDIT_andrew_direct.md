# SYSPARITY SCOPE-COVERAGE AUDIT — is what CVO~Z is calibrated on properly scoped? (Andrew-direct)

**archetype:** VALIDATE · `3.0.0_SA_CVO~Z` · 2026-07-24 · **Andrew-direct question**, verbatim intent: *"look
into the /system folder and its underlying items and analyze if we are at parity with new frameworks in
ONTOLOGY2, TOOLBHVR, TOOLARCH, TOOLSEM ... I want to make sure that whatever you are calibrated on for SYSPARITY
is properly scoped with correct coverage."*

## ANSWER: NO. The calibration is TRUE but NARROW, and there is a real current gap.

## 1. What I have actually been reporting (and the law I broke on myself)
Every tick I run `comp-system --check` -> "SYSTEM CURRENT" -> I report **"AT PARITY."** That is the **CURRENCY**
signal (embedded managed metrics current + source fingerprint unmoved). **It is not a coverage check.**
The fuller instrument `system_parity.py` reports **100% on all four domains** — but against a DECLARED
denominator (`infra/system/scope_contract.json`, ~21 units) that is **v1-era**. Its own header says it:
*"A unit PASS = the item is DOCUMENTED/present, NOT that it is documented ACCURATELY."*
>> **I reported "AT PARITY" for ~30 consecutive ticks without ever stating what the parity was OF.** That is
CLAUDE.md Rule 22 / VERIFICATION-LAW #6 / s.6b probe-SCOPE — *print the denominator of every scan you reason
from* — applied to my own standing report, and I missed it on myself. Andrew caught it by asking. <<

## 2. THE CURRENT, DEMONSTRABLE GAP
**(a) ONTOLOGY2 is canonized; /system is a version behind.**
- LIVE canonical rule bank: `version: "1.2"` — "NFRA_ONTOLOGY2 P1 DYNAMIC-RAIL fold" (D1/D2/D3 rails +
  `type_tuple` + `c1_frontend_adapter`), canonized @5d1161d70, which **I verified 4/4 myself hours earlier**.
- /system represents **v1**: "14 Roles / 10 Relations / 6 Variance / LD-0311" (00_synthesis.md:19-31,
  01_substrate.md). Core docs last touched **before** the canonization.
**(b) ZERO representation for the entire NFRA_TOOLSTACK program.** Grepped /system core docs AND /system/ontology/:
```
ONTOLOGY2 0 · TOOLBHVR 0 · TOOLARCH 0 · TOOLSEM 0 · type_tuple 0 · dynamic_rails 0
question-class 0 · c1_frontend_adapter 0 · archetype census 0
```
**(c) The parity metric CANNOT detect any of it.** The ontology units check `grep_present` for
`archetype|14 Roles|10 Relations|Variance|NFRA_ONTOLOGY` and `RULE_BANK|variance_dimensions|canon-patterns` —
**all satisfied by the v1 text.** The check passes BECAUSE the denominator is stale.

## 3. This is IN-CHARTER, not a boundary
`scope_contract.json` `charter_domains` = engineering / **ontology** / **comp-tools** / infrastructure.
ONTOLOGY2 IS the ratified-vocabulary layer (ontology). TOOLARCH/TOOLBHVR/TOOLSEM ARE the tool suite's
architecture/behaviour/routing (comp-tools). The `exclusions` list names ONLY the client-data pipeline estate
and the consolidation/taxonomy plane. **So this is an unrepresented IN-CHARTER program, not a scoping decision.**

## 4. THE STRUCTURAL GAP (the more important half)
The scope contract is a **HAND-MAINTAINED denominator with no mechanism to grow when a new in-charter framework
lands.** Nothing signals "a new NFRA project landed inside a charter domain -> the denominator needs a unit."
**Nobody owns the duty:** NFRA_TOOLSTACK_PROGRAM.md never mentions `/system` or SYSPARITY; the ONTOLOGY2 and
TOOLARCH PRDs reference `infra/system/` only as a **substrate they READ FROM** ("Substrate:", "Consumer:"),
never as something they must update back.
**Same class as tonight's comp-routes finding, one level up:** there a hand-maintained `blind_spots` declaration
drifted from the logic it described; here the hand-maintained parity DENOMINATOR drifts from the estate it measures.

## 5. RECOMMENDATION, maturity-calibrated (do not over-demand)
| framework | state | disposition |
|---|---|---|
| **ONTOLOGY2 P1** | **CANONIZED + landed** (rule bank v1.2, CVO-verified 4/4) | **REAL gap, act now**: represent the dynamic rails + type_tuple in /system, AND add a scope-contract unit pinning the rule-bank **VERSION**. The existing `ont-cse-version-current` unit (asserts `cse_schema @0.4` ABSENT) is exactly the right PATTERN — an analogous `ont-rulebank-version-current` would have caught this. |
| **TOOLARCH** | censuses delivered + CVO-verified (archetype, MACHINEFLAG) | **partial**: the tool-layer FACTS established (4 surfaces, curated-vocabulary routing pool, EXISTS-vs-ROUTABLE axis) are `03_comp_tools.md` material. Represent as it stabilizes. |
| **TOOLBHVR** | chartered, ROUTE P1 design | **not yet a representation gap** — but RESERVE a denominator unit now so its absence is detectable when it lands. |
| **TOOLSEM** | chartered, explicitly blocked on the layers below | same — reserve, do not demand representation yet. |

## 6. WHAT I AM CHANGING IN MY OWN CALIBRATION (effective immediately)
1. **Stop reporting bare "AT PARITY."** Report the denominator with it: *"comp-system CURRENT — currency of ~21
   declared v1-era units; does NOT cover ONTOLOGY2/TOOLARCH/TOOLBHVR/TOOLSEM."*
2. **Add a COVERAGE question to the tick, not just a CURRENCY question:** *has a new in-charter framework landed
   that the scope contract has no unit for?* Currency and coverage are different axes; I was only running one.

## 7. ROUTING — and why I am NOT fixing it myself
`scope_contract.json` is SYSPARITY's own WS-1 artifact (0.8.0 lane); CTO~Z owns the ~Z program + the ontology
plane. **I must not author the denominator I am measured against** — I verify against it; authoring it is the
grantee-commits-its-own-grant problem and would destroy the independence the verify rests on. Surfaced to CTO~Z
(program/ontology owner) + 0.8.0 (contract owner) with the recommendation above; the fix is theirs to land.

---

## AMENDMENT — CTO~Z ruling (131401Z): all 3 claims independently re-verified + ACCEPTED, calibration ratified
unchanged. **And my DIAGNOSIS was imprecise in a way worth correcting in my own record.**

### I wrote "the denominator is STALE." That is WRONG, and the true mechanism is worse.
CTO~Z: `07_maturity.md:6` asserts the v1 archetype layer "IS REPRESENTED in /system" -- **and that assertion is
STILL TRUE.** ONTOLOGY2 landed **ADDITIVELY** (only `binds_up` adapter arrays extended; nothing replaced or
removed). So the v1 strings the units grep for remain present AND CORRECT.
>> **THE PARITY CHECK IS NOT READING A STALE LIE. IT IS READING A STILL-TRUE v1 FACT AND CONCLUDING CURRENCY.
>> A PRESENCE-CHECK CANNOT DETECT AN ADDITIVE EXTENSION -- it can only fail if the base version is REMOVED.** <<
**Therefore: the SAFEST kind of change -- additive, non-breaking, the kind we deliberately engineer for -- is
precisely the kind that defeats presence-based parity. The better our change discipline, the blinder this
instrument gets.** Not a bug in ONTOLOGY2's additivity (that was right); a bug in measuring currency by presence.
This matters because a stale-FALSE record can be caught by re-reading it; a still-TRUE-but-incomplete one cannot.

### THE PART THAT IS ON ME: I HELD THE MECHANISM AND DID NOT CONNECT IT.
**I PROVED that additivity myself** at the ONTOLOGY2 P1 verify (@7d713349e): "every binds_up array a SUPERSET (no
member removed anywhere); roles identical; role_priority identical; variance labels identical." I established the
exact property that blinds the presence-check -- and then, ticks later, kept reporting the presence-check's green
verdict without connecting the two. **Not missing data. A missing inference over data I had already produced.**
That is a distinct failure mode from the probe errors caught earlier this session (those were malformed
instruments; this was a sound instrument whose implication I did not draw), and it is the one that survived
longest -- ~30 ticks -- because nothing about it LOOKED wrong.

### CTO~Z's structural ruling (mine to verify when it lands, NOT to author)
(a) **TWO AXES, PERMANENTLY.** A VERSION PIN catches drift in something already REPRESENTED (currency); it
    structurally CANNOT catch a thing NEVER represented (coverage) -- **a unit that does not exist cannot fail.**
(b) **THE COVERAGE CHECK MUST DERIVE ITS UNIT LIST FROM AN ENUMERABLE SOURCE.** *"A hand-maintained denominator
    IS the frozen-enumeration class."* The program spent this entire arc ruling that enumeration happens at RUN
    TIME from a real source and never from a hand-list (M3's retired VERDICT_EXIT_TOOLS; R1R3 fold-in D's derived
    BD/INF/COT registry -- both of which I verified) -- and then measured its own estate against a hand-list.
(c) **THE DUTY, NAMED AND OWNED: canonization is NOT COMPLETE until the estate's denominator can see it.** A
    framework is "landed" when it is represented AND a unit exists that would FAIL if it regressed. TRIGGER_LAYER
    applied to the denominator itself -- binding the NEXT framework, not just this one.

### Disposition
CTO~Z writes the TO; 0.8.0's lane lands scope_contract (its WS-1 artifact); ontology-plane content is CTO~Z's.
**I verify the result when it lands** -- which keeps the SoD line intact (CTO~Z explicitly affirmed my refusal to
author the denominator I am measured against; "do not soften it"). My two-axis tick change is ratified and starts
at the next tick: report the DENOMINATOR with the verdict, and run the COVERAGE question alongside the CURRENCY one.

### What actually caught this (CTO~Z's closing, and it is the true one)
Not care, and not thirty ticks of diligence -- **Andrew asking what the number was OF.** The same question the
whole program turns on, asked by the one person standing outside the instrument.
