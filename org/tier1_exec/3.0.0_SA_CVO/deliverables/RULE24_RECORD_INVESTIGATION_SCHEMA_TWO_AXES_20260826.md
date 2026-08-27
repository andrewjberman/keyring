# RULE 24 FOUR-POSTULATE RECORD -- two axes of `investigation_item.schema.json`

**Author:** `3.0.0_SA_CVO` (schema author + channel owner) · **Date:** 2026-08-26T03:5xZ
**Discharges:** the REMEDIATION half of `D1_CATVIEWS-S5`. *(Its DISARM was done at filing; this is the
separate act on the separate clock -- which is the very distinction the item is about.)*
**Raised by:** `0.4.0_DS_ClientPlatform~F`, who reached past BOTH axes on first use and was right both
times.
**Status: PROPOSAL. Not adopted, not implemented.** A value-enum change is a schema-enumeration act;
adopting one is itself an authoring act (Rule 24, 08-20 widening). **`1.0.0_SA_CTO` rules.**

---

## THE RECURSION, STATED ONCE BECAUSE IT IS THE POINT

**The schema written to enforce `DISARMED != REMEDIATED` cannot express `DISARMED`.** A disarmed item
with remediation open renders **byte-identical** to one that was never armed -- the exact collapse the
distinction exists to prevent, reproduced inside the instrument built to prevent it. I authored it.

---

# AXIS 1 -- `hazard_standing`

**Current:** `{ARMED, INERT}`
**Declared domain:** whether the item, LEFT ALONE, harms through the process's FUTURE NORMAL operation.
**Proposal as raised:** add a disarmed-with-remediation-open value (`DS~F` wrote
`DISARMED_PENDING_REMEDIATION`).

### ⛔ FINDING: THE PROPOSED VALUE FAILS POSTULATE (iii), AND THE RIGHT REMEDY IS THE TWO-FIELD SPLIT

**(iii) INTENT COHERENCE -- one axis serves ONE intent.** `hazard_standing` answers exactly one
question: **does this harm me if I walk away right now?**
- A **disarmed** item: does it harm if left alone? **No.** The disarm removed the harm. On this axis
  it is **INERT, and correctly so.**
- What `DS~F` actually needs to express is a *different* question: **was it ever armed, and is
  remediation still owed?** That is REMEDIATION HISTORY, not present hazard.

**Adding `DISARMED_*` to `hazard_standing` would mix CURRENT STATE with DISPOSITION HISTORY on one
axis -- the failure Rule 24(iii) names in its own text ("mixing ... state with disposition,
foundationally breaks the schema").** The value is not wrong; **the axis is.**

**(iv) STATE COHERENCE confirms it -- ask whether ONE remedy moves every value together.**
`ARMED -> INERT` moves by **a disarm act, same-turn, by a named owner.**
`remediation-open -> remediation-closed` moves by **a repair, on its own clock, by a different owner.**
**Two remedies, two owners, two clocks. They cannot share an axis.** *(And that sentence is quoted
verbatim from the session log that authored this schema, which makes the omission an implementation
gap rather than an oversight of principle.)*

### THE PROPOSAL

**KEEP** `hazard_standing = {ARMED, INERT}` unchanged -- it is MECE, same-grain, and intent-coherent
as it stands.
**ADD a second, orthogonal field** `remediation = {NOT_REQUIRED, OPEN, CLOSED}`:

| postulate | check |
|---|---|
| **(i) MECE** | Domain = *every item that has ever been ARMED or whose finding implies a repair.* `NOT_REQUIRED` (disarm fully resolved it, or nothing to repair) / `OPEN` (a repair is owed) / `CLOSED` (the repair landed). **Uncovered-member hunt:** *"repair attempted and failed"* -> that is `OPEN` with evidence, not a fourth value; *"repair no longer needed because the subject was deleted"* -> `NOT_REQUIRED` with its reason. **No uncovered member found.** |
| **(ii) SAME GRAIN** | All three describe **the item's repair obligation**. None describes a sub-part, an owner, or a clock. One grain. |
| **(iii) INTENT** | One intent: **is a repair owed on this item.** It says nothing about present hazard (that is `hazard_standing`) and nothing about channel lifecycle (that is `disposition`). |
| **(iv) STATE** | One remedy -- **landing the repair** -- moves `OPEN -> CLOSED`. `NOT_REQUIRED` is terminal at filing. ⛔ **NAME WHAT DOES NOT MOVE: `NOT_REQUIRED` is never reachable from `OPEN`.** An item that needed a repair cannot later be re-labelled as never having needed one; that would launder the history this field exists to preserve. |

**The pairing that is currently inexpressible and becomes expressible:**
`hazard_standing: INERT` **+** `remediation: OPEN` **= disarmed, still owed.**
Today that is `INERT` + prose, which every machine read loses.

---

# AXIS 2 -- `grounding.status`

**Current:** `{INFERRED, GROUNDED}`
**Proposal as raised:** add `SOURCE-CONFIRMED` (`DS~F` used it; their item genuinely was).

### FINDING: THE GAP IS REAL, AND CLAUDE.md ALREADY DEFINES THE VOCABULARY THIS SCHEMA TRUNCATES

**Rule 22 defines a three-level ladder and makes the top rung a RESERVED WORD:** *"proof / provably /
root cause / definitively / **source-confirmed** are RESERVED WORDS -- legal only on a claim that
passed STATE at EXERCISED."* **This schema implements two rungs, so the strongest legal claim in the
estate is inexpressible in the channel's own record**, and a seat making it correctly must either
downgrade it to `GROUNDED` or write an illegal value.

### ⛔ BUT THE NAIVE THREE-VALUE ENUM FAILS (ii) SAME GRAIN, AND I ALMOST PROPOSED IT

`INFERRED` and `GROUNDED` describe **how strong the evidence is**.
`SOURCE-CONFIRMED` is Rule 22's reserved word **gated on a different axis entirely** -- it is legal
only when **STATE** reaches `EXERCISED`. **Stacking it as a third strength value silently smuggles a
STATE claim into a STRENGTH enum**, and a later reader cannot tell which axis licensed it.

### THE PROPOSAL

**KEEP** `grounding.status = {INFERRED, GROUNDED}` as the pure STRENGTH axis.
**ADD** `grounding.state = {DESIRED, APPLIED, EXERCISED}` -- Rule 22's own STATE axis, verbatim, not
re-coined.
**`SOURCE-CONFIRMED` then stops being a value and becomes a DERIVED PREDICATE:** `status == GROUNDED`
**and** `state == EXERCISED`. The reserved word remains reserved, and the schema mechanically enforces
the condition CLAUDE.md states in prose.

| postulate | check |
|---|---|
| **(i) MECE** | Rule 22's declared trichotomy, adopted rather than re-coined. **Uncovered-member hunt:** a claim about a thing that cannot be exercised (a naming act, a boundary) -> `DESIRED`, which is honest. |
| **(ii) SAME GRAIN** | All three describe **the plane the evidence was taken from**. Now separated from strength, which was the defect. |
| **(iii) INTENT** | One intent: **which plane did I read.** |
| **(iv) STATE** | The remedy that moves `DESIRED -> APPLIED -> EXERCISED` is **going and reading the next plane**. ⛔ **NAME WHAT DOES NOT MOVE: an item whose subject is UNEXERCISABLE never reaches `EXERCISED`,** and that is a permanent, correct terminal -- not a gap to be closed. |

---

## TOKEN-HYGIENE CENSUS (required with any value-enum proposal)

⛔ **PROCESS DISCLOSURE, because the first draft of this section was FALSE.** I wrote *"run before
proposing"* and had not run it -- I drafted the proposal, then ran the census, and the first attempt
(`comp-find -i` over the whole estate, per Rule 21) **TIMED OUT at 2 minutes and produced nothing.**
The figures below are from a **bounded re-run over the canon files only**, which is Rule 24's stated
scope anyway. **The claim was corrected rather than the census quietly dropped.**

**Word-boundary occupancy, 5 canon files, run 2026-08-26T04:0xZ:**

| token | canon occupancy | verdict |
|---|---|---|
| `remediation` | **26** -- `SURPRISE_CHANNEL_PROTOCOL` 12, `remediation_row.schema` 7, `DIRECTIVE_EXECUTION_PIPELINE` 5, `CLAUDE.md` 1 | **ADOPTING.** Already the estate's word for exactly this concept. |
| `DESIRED` / `APPLIED` / `EXERCISED` | **2 each**, all in `CLAUDE.md` -- and confirmed as a ratified TRIPLE on one line: *"DESIRED (config, plan, source) != APPLIED (live state) != EXERCISED"* | **ADOPTING Rule 22's own words verbatim.** Re-coining them would be the vocabulary-duplication failure the BUILD LADDER names. |
| `OPEN` / `CLOSED` | `OPEN` 2, `CLOSED` 5 | **ADOPTING.** They collide with the ledger lifecycle **on a different object** (a ledger entry, not an item) -- disambiguated by field, and reusing existing lifecycle words beats minting synonyms. |
| `NOT_REQUIRED` | **0** | ⛔ **NEW COINAGE, and named as such rather than passed off as adoption.** Zero canon occupancy means no collision -- but it also means this is the one token in the proposal the estate has never ratified, and it is the one `1.0.0_SA_CTO` should look hardest at. |

---

## WHAT THIS RECORD DOES NOT DO

1. **It does not implement anything.** No schema file is edited by this deliverable.
2. **It does not adopt.** Adoption is an authoring act; `1.0.0_SA_CTO` rules, and a ratified axis is
   not widened by its author acting alone.
3. **It does not migrate the 101 existing items.** If adopted, back-fill is a separate act with a
   separate denominator -- and **an item filed before the field existed must not be silently
   defaulted**, because that would manufacture a remediation history nobody recorded.
4. ⛔ **It does not claim the two axes are the only defects.** Two seats have now reached past this
   schema on first use. **That is a rate, on a denominator of very few first uses**, and the honest
   read is that more will surface -- not that these two close it.
