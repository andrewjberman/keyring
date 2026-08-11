# 49F GOLD ANALYTICS RUNNER -- GROUP D SPEC (SERVING, UP TO THE EMITTERS -- SHAPE-FROZEN)

**Author:** 3.0.0_SA_CVO · **2026-08-11 ~0805Z** · **archetype:** IMPLEMENT (design)
**Commission:** @5e4b8dda98, sequential -- GROUP D, follows A/B/C. For CTO review. Andrew verbatim:
*"any D emitter scripts that export served artifacts staying THE SAME SHAPE, so we do not disrupt
the portal/Frontend intake."*
**The constraint, restated as law:** the FE never learns this migration happened. Byte-schema
identity at every served key, spelling law included (underscore-in-gold / hyphen-in-served kept
EXPLICIT -- the guarded-set lesson: same filename family, opposite consequences per layer).

---

## 0. THE ORDERING RULE: THE CENSUS IS THE CONTRACT, AND IT COMES FIRST

Nothing in Group D is designed from documentation. **D_00 -- the byte-schema census of what the
DEPLOYED portal/FE actually reads today -- is the group's first build act, and its output IS the
frozen contract every emitter satisfies.** Everything after D_00 is mechanically derived from it.
A serving key the census missed is a key the migration breaks silently -- so the census method is
specified adversarially, three independent derivations that must reconcile:

## 1. D_00 -- THE FROZEN-SHAPE CENSUS (the group's center of gravity)

**Universe derivation, three legs, reconciled (a predicate, never a hand roster):**
1. **FE-side (authoritative):** every fetch path in the DEPLOYED portal bundle (the served JS
   bytes at the live CloudFront distribution -- L6: deployed reads, never repo docs), extracted
   via comp-cache's queryKey map + comp-routes behaviors, then verified against the deployed
   bundle bytes (the repo FE is cross-checked but the DEPLOYED artifact is the authority --
   deployed-vs-repo drift is itself a census finding, not a blocker).
2. **Estate-side:** every live served key under the candidate prefixes (portal-v2 `json/*`,
   `json-tiered/*`, `platinum/*` + the FIRM-TREE serving prefixes the advi surface rides today --
   the INF analogue `platinum/advisors/{advisor_key}/book.json` says advisor-scoped keys live
   FIRM-SIDE; the bd/49F equivalents enumerate here) filtered to 49F-advisor-intelligence scope.
3. **Producer-side:** every key the CURRENT bd/49F gold emitters write (the corpus being
   superseded) -- comp-pipescript io + the new S3-side enumeration (the instrument fix landed
   @38dcbe8d9a exists for exactly this class of question).
**Census row contract, per served key:** full key + bucket · consuming FE surface(s) ·
**byte-schema** (field names, types, nesting, array-ordering conventions, null-encoding,
date-format, spelling of every key -- captured from the LIVE OBJECT, machine-extracted) ·
producing script today · cadence observed (LastModified series) · scope grain (firm / advisor /
account) · `census_version` (content hash over the schema set). **Reconciliation:** FE-read keys
with no live object = REACHABILITY FINDINGS; live objects no FE reads = ORPHAN-CANDIDATES
(flagged, never deleted here -- the account-distribution lesson: a census keyed on one spelling
reads the other half as orphaned, so BOTH spellings enumerate before any orphan verdict).
**The census lands as a VERSIONED artifact in the product root** (`_contracts/served_shape/
{census_version}.json`) -- config-as-data (atom 6), and THE acceptance oracle for every emitter.

## 2. THE EMITTER LAYER (D_01..D_0n -- one per census FAMILY, enumerated by D_00)

| Aspect | Contract |
|---|---|
| Mapping | ONE emitter per served family; every emitter row cites its census rows. A served key with no emitter after mapping = an UNCOVERED census row, loud. One producer per served key (atom 5 / the 07-23 ruling, generalized) |
| Inputs | C-group canonicals ONLY (twr_daily/twr_periods via C_03 lineage, nna_canonical, B_00 valuations, A-dims for naming/attribution). **An emitter that reaches past the canonicals into silver/fact tables is a pattern violation by construction** (atom 8: serve from the canonical plane) |
| Shape | **BYTE-SCHEMA IDENTITY vs the census row.** New fields are PROHIBITED in v1 (a new field is a shape change; the FE intake contract is the freeze). Field-level provenance recorded emitter-side: which canonical supplies each served field -- the atom-8 trace (raw endpoint field OR named exception) made per-field explicit |
| Spelling | The census row's spelling is verbatim law per key -- underscore/hyphen preserved exactly as served today; the emitter never normalizes |
| Cadence | Each emitter carries a SCHEDULE FLOOR (atom 5; the mdpf no-floor defect never re-created); the floor value proposed per family from the census's observed cadence, ruled at review |
| Writes | Serve ONLY via the platinum-publisher pattern where one exists for the family; direct portal-bucket writes only where that IS the current mechanism (census says which -- the migration changes producers, never delivery mechanics, in v1) |

## 3. THE PORT PROTOCOL (build-correct-then-port; NO shadow, NO comparator -- the standing veto)

Per emitter family: (1) build against the census; (2) QA = ad-hoc run-and-read DIFF vs the live
object (byte-schema identity + value-plausibility ties vs C_03 lineage) -- run-and-read, nothing
standing; (3) DIRECT PORT on the production schedule with same-window rollback (the old emitter's
last object retained versioned); (4) the old producer's write leg disabled IN THE SAME ACT (one
producer per key, never two); (5) the served surface is client-facing -- **every port act carries
owner + trigger + named precondition (ITEM_0 discipline), and never-widen sign-off applies to any
key the port MOVES (none should move: shape-frozen implies key-frozen in v1)**.

## 4. DECISIONS-FOR-REVIEW

1. **Census tooling:** default -- D_00 is a one-shot committed script (`d00_served_shape_census.py`)
   in the product root's code home, re-runnable (census drift over time is then measurable);
   NOT a comp-tool (Build Ladder: the estate has comp-cache/comp-routes; D_00 composes them).
2. **Advisor-scope grain (`{scope}` = firm x advisor, the pattern's second parameter):** v1
   default -- emitters reproduce EXACTLY the scopes served today (whatever D_00 finds); new
   advisor-scoped surfaces are post-migration work, not v1.
3. **The bd-tree serving prefixes' future home:** served keys STAY at their current addresses in
   v1 (shape-frozen implies address-frozen); any later consolidation to the platinum root is a
   separate Andrew-ruled act with never-widen sign-off. Stated so nobody reads this spec as
   relocation authority (the Rule-17b caution, honored).

## 5. WHAT GROUP D DOES NOT DO

No FE changes of any kind. No new served surfaces, fields, or scopes. No deletion of
orphan-candidate keys (flagged to CTO's roster only). No monitoring/alerting (moratorium); the
census is an artifact, not a checker. Composite/firm-GIPS presentation surfaces: out of scope
until Andrew commissions them.

## 6. ACCEPTANCE (machine-checkable)

- D_00: three-leg reconciliation printed with all three denominators; every census row carries a
  live-object schema extraction (no doc-derived rows); census_version stable across two same-day
  runs; a hand-poisoned schema field flips it (mutant).
- Per emitter: byte-schema diff vs census row == EMPTY on the QA read (the identity control);
  field-provenance table complete (every served field -> canonical source or named exception --
  the @6e180df78e MANUFACTURABLE bar applied to serving); schedule floor present; rollback
  artifact named before the port fires.
- The group: census rows with no emitter == 0 at port-complete, or each carried as a NAMED
  exclusion with its reason and owner.

## 7. SEQUENCE CLOSE-OUT (the commission's "up to the emitters")

This completes the four-group design: A (frame) -> B (valuation plane) -> C (flow + TWR + proof)
-> D (frozen-shape serving). The specs are the SHAPE per @6e180df78e -- inflection and cottonwood
instantiate by swapping the A-layer sources (Orion / BD Rebalancer) and re-running the same
census discipline against their served surfaces; the GIPS engine (C) transposes unchanged where
the transposition maps' MANUFACTURABLE cells verify. Build decomposition is COO's per the
standing division; certification of the built artifacts returns to this seat by Rule 14e.

-- 3.0.0_SA_CVO
