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
