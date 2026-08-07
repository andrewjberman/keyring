# C3.ii — the MACRO REGISTRY is the missing DECLARATION source (and the denominator the harvest lacks)

**Author:** `1.0.0_SA_CTO` (base) · **2026-08-07**
**Origin:** Andrew-direct at the base CTO terminal, 2026-08-07, VERBATIM:

> *"I also want to lock in the strategy for C3.ii generation, I believe that a really useful channel
> for this that is underxplored is going through the Macro Project registry, that should make it
> abundantly clear what the verticals are. We were discussing a deterministic -> AI inferential ->
> human review pipeline for C3.ii generation, 4.0.0_SA_CRO should pick up on that."*

**For:** `4.0.0_SA_CRO` (build owner) + `2.0.0_SA_COO` (TO authoring — this is the shape you said you
would not guess at). **No gate here.** Nothing waits on anyone's approval.

---

## 1. His instinct is right, and the ratified definitions make it stronger than he stated it

`comp-estate --definitions`, reserved_ratified:

> **`C3.ii`** — *SEMANTIC VERTICALS — **DECLARED never discovered**; the **legislated business
> partition** of the chain*
> **`C3.i`** — *DETERMINISTIC STRUCTURES — **DISCOVERED never declared***
> **`vertical`** — *A C3.ii unit — **a named business function** in the legislated semantic partition*

**C3.ii is definitionally a DECLARATION.** So the question "where do vertical names come from?" has a
type answer before it has a data answer: **from a legislated artifact, not from an inference.**

`org/projects/MACRO_CODES.md` is the only artifact in the estate that IS one. Its own first lines:

> *"Canonical 4-character codes for **every surface area** in the Opal Capital system. A surface area
> can be a portal page, a pipeline, a cloud process, or a research topic."*
> *"The macro code identifies the surface area **permanently**."*
> Rule 6: *"New macro codes **must be added here before use**."*

Permanent · legislated · rule-governed · one-to-one with a surface area · carries an OWNER, a POD and
a PIPELINE per row. That is a business partition someone **declared**, which is exactly the object
C3.ii's definition names.

---

## 2. Why this is not "one more source" — the seven existing ones are all the WRONG TYPE

`NFRA_VERTHARVEST_SPEC_20260807.md` §3 Stage 1 harvests from seven sources:

| family | sources |
|---|---|
| portal-facing | `App.tsx` nav labels (15) · `portal/src/pages/*` dirs (15) · `s3://opal-data-portal-v2/json/*` prefixes (21) |
| backend/infra | Lambda names (196) · EventBridge rules (139) · Scheduler (16) · S3 bucket names (30) |

**Every one of the seven is an ARTIFACT NAME.** Each infers *"a business function exists"* from
*"someone named a thing."* That is **discovery** — C3.i's mechanism — pointed at a rung whose own
definition says **declared never discovered**. It works (28 of 29 recall, measured) precisely because
humans name things after business functions, but it is recovering the declaration by inference **when
a written declaration exists and is not being read.**

**MACRO_CODES.md is not in the source list.** That is the gap Andrew found.

---

## 3. The stronger claim: it is not a source, it is the DENOMINATOR

A harvest without a declared set produces a list of candidate names **with no way to tell a NEW
candidate from an ALREADY-DECLARED one.** That is the shape `[[feedback_a_predicate_is_not_a_roster]]`
names, and the spec already measures its cost: the generator's hardcoded `CATALOG_ORDER` carries 25
entries against 29 legislated, contains `attribution` (**retired by naming act**), is missing five
live ones, and **fails SILENTLY** — unknown names are appended alphabetically with no error.

Join the two planes and the cells are individually meaningful. This is Rule 22a's DESIRED-vs-APPLIED
distinction applied to a taxonomy instead of to infrastructure:

| | **APPLIED** (harvest finds live resources) | **NOT APPLIED — RETIRED** | **NOT APPLIED — ASPIRATIONAL** |
|---|---|---|---|
| **DECLARED** (in MACRO_CODES.md) | a **live vertical** — the healthy cell | was applied, deliberately ended by a **naming act**. Correct final resting place — stays here forever. `CENG`/causality (retired 08-05, applied plane measured EMPTY) | declared **ahead of build**, never applied. **Not an end state — a WIP row.** Should MOVE to DECLARED×APPLIED when built; if it never does, *that is a finding*. `TAXX` (TBD), `SSCN` (TBD) |
| **NOT DECLARED** | ⭐ **AN UNDECLARED VERTICAL — the candidate list C3.ii generation EXISTS to produce** | — (invisible by construction; not a defect, a boundary) | — |

> **⬛ THE NOT-APPLIED COLUMN IS SPLIT ON `4.0.0_SA_CRO`'s POSTULATE-(iii) FINDING, and they were right.**
> v1 of this table pooled RETIRED and ASPIRATIONAL into one cell. That is **STATE beside DISPOSITION**
> on one axis — an intent-coherence break — and the two take **opposite remedies**: a retired code
> should never move, an aspirational one should. Pooled, neither signal is readable and *the cell
> quietly accumulates abandoned aspirations that look exactly like healthy retirements.*
> It also sharpens the control below: **CENG's expected cell is RETIRED specifically, not the union.**

**The bottom-left cell is the product.** Everything else is bookkeeping that makes it legible. Without
the declared set you cannot compute that cell at all — you can only produce an undifferentiated name
pile and re-adjudicate the whole thing by hand every run.

---

## 4. ⚠ THE TRAP — adding it naively BREAKS the spec's only natural control

The spec's quality property, in its own words:

> *"THE SINGLE MISS IS `causality` — the vertical Andrew RETIRED 2026-08-05, whose applied plane is
> measured empty. That is not a gap; it is a natural positive control nobody designed: the
> harvester's only blind spot is the one thing that does not exist. Any implementation MUST reproduce
> this property — **a harvest that 'finds' causality is reading the model, not the estate.**"*

**`MACRO_CODES.md` contains `CENG` = CausalityEngine.** So bolting it on as an eighth peer source
would make the harvest "find" causality on day one — **destroying the one control the spec has**, and
destroying it in the direction that looks like improved recall.

**This is not an argument against using it. It is the argument for using it CORRECTLY:**

> **The macro registry enters as the DECLARED PLANE, never as a harvest source. It is joined to the
> applied plane, never unioned with it.** A macro code with an empty applied plane resolves to
> RETIRED-or-ASPIRATIONAL — which is `CENG` landing in the correct cell **as a positive control that
> still fires**, rather than as a false recall win.

The control survives and gets *stronger*: it now discriminates on a join instead of on an absence.

---

## 5. ⚠ A RULE-24 DEFECT IN THE REGISTRY ITSELF — inherited, not introduced

Before anything treats `MACRO_CODES.md` as a clean axis, it fails **postulate (ii) SAME GRAIN** and
arguably **(i) MECE**:

| row | grain |
|---|---|
| `POSN` Positioning | ONE portal page |
| `OPAL` | an **umbrella** — its own row lists SIX projects (`OPAL_ASSETS`, `OPAL_RUNNERS`, `OPAL_TAXSMA`, …) |
| `NFRA` | an **umbrella** — *"NFRA is a MACRO, not a project key"* |
| `ADHC` | **a residual bucket** — *"Ad-hoc (no permanent surface area)"* |

A one-page surface, a six-project umbrella, and an explicit not-a-surface-area residual sit on one
axis. `ADHC` is the sharpest: the file defines macro codes as *permanent surface areas* and then
carries a row whose definition is *no permanent surface area*. **A residual bucket on a MECE axis
absorbs exactly the members the axis failed to model** — so anything landing in `ADHC` is, by
construction, a vertical the taxonomy could not express.

**Its own file records a conformance lag:** the `OPAL` row was added 2026-07-14 *"closing a lag: the
macro had been in REGISTRY use since OPAL_ASSETS with no row here — rule 6 conformance."* So rule 6
("added here before use") has been violated in practice and repaired after the fact. **Treat the
registry as authoritative-but-lagging, not as ground truth** — which is precisely why it joins to the
applied plane rather than replacing it.

**⬛ AMENDED ON CRO'S READ (2026-08-07) — my v1 was correct and INCOMPLETE on two counts:**

- **(i) MECE — I wrote "arguably fails." That is imprecise and the exact statement is worse than
  failing.** A residual bucket makes the axis collectively-exhaustive **BY CONSTRUCTION**, so the CE
  limb still technically holds *and carries ZERO information.* **MECE is not violated here; it is made
  UNFALSIFIABLE** — which is the more damaging condition, because the axis now passes a check it can
  never fail.
- **(iv) STATE COHERENCE — I did not run it, and it FAILS.** The postulate requires naming the state
  axis and asking whether ONE remedy moves every value together. It does not, and (iv) obliges me to
  name which values do not move:

  | value | remedy |
  |---|---|
  | `POSN` + page-grain siblings | **RE-GRAINING** — promote to surface-area grain |
  | `OPAL` / `NFRA` umbrellas | **LEVEL SPLIT** — macro-vs-project is already a two-level system; these rows are the level boundary leaking onto the value axis |
  | `ADHC` | **NEITHER.** A residual bucket is not a mis-grained member, it is *the absence of a member*. It dissolves only by modelling what is inside it — **unbounded work of a different kind** |

  > **So "fix the macro registry axis" presents as ONE workstream and is THREE — and the third has no
  > determinate size.** That is precisely what postulate (iv) exists to surface, and it must be said
  > plainly if this ever becomes a fix proposal to Andrew.

**This is CRO's instrument.** Rule 24 is their authorship; the four postulates are the right lens; and
a taxonomy defect found at AUTHORING time is a defect, not a style note. *They checked this document
rather than inheriting it — which is what I asked for — and found a control of mine that could not
fail. Both corrections above are theirs, adopted in full.*

---

## 6. What this does NOT decide

- **It does not decide inherit-vs-fresh.** `1.0.0_SA_CTO~C` authored `NFRA_VERTHARVEST_SPEC_20260807.md`
  off Andrew's own 08-06 word at their terminal, and it has survived two CVO falsification rounds. It
  already implements his stated pipeline shape — `HARVEST -> NORMALIZE+CLUSTER -> CONDENSE(AI) ->
  RATIFY(Andrew/CVO)` is **deterministic -> AI inferential -> human review**, byte for byte. My
  recommendation to Andrew is that CRO takes it forward as build owner rather than authoring a second
  spec; that call is his and is pending at the time of writing.
- **It does not auto-name anything.** The spec's non-goal stands unchanged and this document does not
  touch it: *naming remains sovereign; the loop SURFACES candidates, only a naming act admits one.*
  The macro registry is a record of naming acts already performed — using it is reading Andrew's prior
  decisions, not substituting for his next one.
- **It proposes no gate, no monitor, no alarm, no checker.**

## 7. The concrete delta

1. **Add the declared plane.** `org/projects/MACRO_CODES.md` (~30 rows) parsed to
   `{code, surface_area, owner, pod, pipeline}` — plus `org/projects/REGISTRY.md` +
   `org/projects/{PROJECT_CODE}.json` for the project layer beneath each macro.
2. **Join, do not union.** Produce the 2x2 of §3. Ship the **NOT-DECLARED × APPLIED** cell as the
   candidate list into Stage 2/3.
3. **Preserve the control — AND PAIR IT, because on its own it CANNOT FAIL.**
   ⛔ **v1 of this item said only "assert `CENG` lands in DECLARED × NOT-APPLIED." That control is
   UNDISCHARGEABLE and `4.0.0_SA_CRO` caught it.** Run the Rule-22a question against it — *could this
   have said otherwise?* **No.** If the applied-plane measurement returns nothing at all — broken
   query, wrong prefix, empty credential, a harvest that silently no-ops — then `CENG` lands in
   NOT-APPLIED **trivially, the assertion PASSES, and it passes MORE cleanly the more completely the
   instrument is dead.** That is the anti-correlated shape of Rule 22b, and **the control I wrote to
   protect the harvest had the exact defect the harvest's own control had.** *(The old absence oracle
   shared it: a harvest that finds nothing also "does not find causality." Neither version can tell a
   healthy instrument from a dead one.)*
   **THE FIX, one line of spec: assert a PAIR.** Name a macro code that **MUST** land in
   DECLARED × APPLIED — `MDPF` or `ADVI`, both live with a measurable applied plane — and assert both
   limbs **from the same measurement, in the same pass**. `CENG`-empty is informative ONLY when
   something else is simultaneously non-empty. A dead applied plane then fails the **positive** limb
   instead of silently satisfying the negative one.
   *CRO's own framing of why the join beats the absence oracle, worth carrying verbatim:*
   **"AN ABSENCE ORACLE PASSES FOR MANY REASONS AND A POSITION ORACLE FAILS FOR ONE."** Absence tells
   you nothing about *why* a thing is missing; cell membership is a claim that can be wrong in a
   specific, informative way.
4. **Print the denominator on every cell** — declared N, applied M, and each cell's count with a
   measurement vintage. Two of the numbers in this space have already moved under their authors today
   (a 5.5× marker-set swing and a 3.6× resolver swing on NFRA_PYFIELD); a cell count with no frame is
   the same hazard.
5. **State the Rule-24 verdict on the registry axis** (§5) as a finding in its own right, with the
   grain violation named per postulate. Fixing it is a separate act and is Andrew's, not a
   precondition for the harvest.

---

**Grounding:** `comp-estate --definitions` (C3/C3.i/C3.ii/vertical/substrate, reserved_ratified) ·
`org/projects/MACRO_CODES.md` read in full at HEAD · `org/tier1_exec/1.0.0_SA_CTO/deliverables/NFRA_VERTHARVEST_SPEC_20260807.md`
§1–§3 · `org/tier1_exec/1.0.0_SA_CTO/logs/2026-03-05/macro_project_code_system.md` (the two-level
system's origin, `3d5fc658`). **Not exercised:** I have not run the harvest, not parsed
MACRO_CODES.md programmatically, and not measured the applied plane per macro code. Every count in
§5 is a read of the file, and the 2x2's cell sizes are **unmeasured by construction** — measuring
them is the work.
