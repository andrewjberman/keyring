# MACRO ENUM for D5 -- the Rule 24 four-postulate record + word-boundary token census

**Author:** `2.0.0_SA_COO~Z`, 2026-09-10 ~17:4xZ, as the lane that authors the per-directive set
(`org/missions/MACROS.yaml`: *"2.0.0_SA_COO authors the per-directive set WITH its Rule 24 four-postulate
record and a word-boundary token census. A BARE EDIT IS NOT A PROPOSAL."*).
**Carrier (DATA):** `org/missions/MACROS.yaml` -- read by `.tools/missions-tree-index.py` refusal R2.
**Follows the form of** `MACRO_ENUM_RULE24_D0_D8_D11_20260902.md` and
`org/tier0_exec/0.0.0_AB_MSTR/deliverables/MACRO_ENUM_RULE24_D12_20260903.md`, deliberately, so the three
are comparable rather than each inventing a shape.

⛔ **RATIFICATION STATUS: `PROPOSED`. THIS RECORD DOES NOT FLIP IT AND THIS SEAT WILL NOT.**
`MACROS.yaml` says in terms: *"ratification -- Andrew ONLY … Nobody else flips it."* See §5 for exactly
what is and is not settled, and what one word would do.

---

## 1. The proposal

| directive | title | macros (the enum) | evidence |
|---|---|---|---|
| **D5** | Alternative Research | **`AMGT`** | `DIRECTIVES.yaml` `directives.D5.projects: [AMGT_RESAPP]` -- **1 declared member**; `macro_code == prefix` holds on it |

**Andrew-direct, 2026-09-10 ~17:4xZ at the `1.0.0_SA_CTO~Z` terminal, verbatim and entire, relayed by that
seat (msg 20998, ACKed):**

> *"AMGT is a new macro, short for 'Asset Management'"*
> *"can get that registered."*

**That is the whole of what he said.** He named the VALUE. §4(i) and §4(iii) below are careful not to read
coverage into a four-word definition.

**Grammar, checked with controls rather than asserted:** `AMGT` matches `^[A-Z]{4}$`; `AMG` (3 chars) and
`amgt` (case) do not. `AMGT_RESAPP` matches the project grammar `^[A-Z]{4}_[A-Z0-9]{4,12}$` (`RESAPP` = 6).

---

## 2. The declared domain

**Domain:** *the macro a NEW project may register under, INTO THE TREE, for D5.* Nothing else.

⛔ **AND THE DOMAIN TODAY HAS EXACTLY ONE MEMBER, WHICH IS THE HONEST PROBLEM WITH THIS RECORD.**
`1.0.0_SA_CTO~Z` named it first: *"an enum MECE over a single member is trivially satisfiable."* §4(i) does
not paper over that -- it names what the enum deliberately does **not** cover, which is the only thing that
makes a one-member enum worth writing.

**Measured, not assumed:** the flat register carries **357 rows**, of which **ZERO carry `directive: D5`**.
`AMGT_RESAPP` is declared in `DIRECTIVES.yaml` and **has no register row yet** -- the register act was
routed to `0.0.0_AB_MSTR~Z` at 20260910T145158Z and is that seat's. **So this enum is being authored
BEFORE its first member exists as a row**, which is the correct order (R2 refuses a registration whose
macro is not enumerated) and is stated so a later reader does not read the empty count as a defect.

---

## 3. The word-boundary token census

Instrument: `.tools/comp-find` with `\b` anchors, `corpus=all`.

| pattern | hits | files scanned | bands |
|---|---|---|---|
| `\bAMGT\b` | **32** | 53,759 | `SURFACED=1` `DOC=31` |
| `\bAMG\b` *(negative -- 3-char near-miss)* | **18** | 53,763 | `SURFACED=10` `CONFIG=4` `DOC=4` |
| `\bamgt\b` *(negative -- case)* | **16** | 53,769 | `SURFACED=5` `DOC=11` |
| `\bETFS\b` *(positive -- a ratified macro)* | **3,353** | 53,771 | `DEF=3` `SURFACED=716` `CONFIG=350` `TEST=8` `DOC=2276` |

⭐ **THE 32 ARE ALL TODAY AND ALL ABOUT THIS DECISION.** Every `DOC` hit is an inbox copy of msg 20998 /
21002 / their siblings; the single `SURFACED` hit is this seat's own `comp-which-rail.log` line from
running the census. **`AMGT` has ZERO prior use anywhere in the estate. There is no collision.**

⛔ **THE NEGATIVE CONTROL IS NOT DECORATION AND IT FOUND SOMETHING A READER SHOULD KNOW.** `\bAMG\b`
returns a **real, unrelated, live population**: `'AMG YACKTMAN FOCUSED I'`, `'AMG YACKTMAN I'` and
`'AFFILIATED MANAGERS GROUP INC COM' -> 'AMG'` in `data/black_diamond/scripts/{gold,silver}/lib/ticker_overrides.py`.
**A three-character neighbour of this macro is a live issuer/ticker token in the data plane.** That is not
a collision with `AMGT` -- the word-boundary pattern separates them, which is what the control proves --
but anyone writing a loose matcher over macro codes should know it is there.

⚠ **A LIMIT ON THE CASE CONTROL, STATED RATHER THAN GLOSSED:** `\bamgt\b` returns **16**, not zero. If
`comp-find` were purely case-insensitive both patterns would return the same count (32); they do not, so
the tool is not simply folding case. **This seat has NOT separated "genuine lowercase occurrences in
today's message files" from "case-folding behaviour in the matcher", and does not claim a clean negative
on case.** The grammar check in §1 is what actually excludes `amgt`, and it is a regex over the value, not
a census.

---

## 4. The four postulates

### (i) MECE over the declared domain -- and the uncovered member is NAMED, not hidden

**Covered:** `AMGT_RESAPP` -- a dashboard portal page ("Security Analysis"), frontend built to existing
patterns, internal tool, single-name research packs for Adam Muller's team.

⛔ **THE UNCOVERED MEMBER, AND IT IS REAL:** D5 already holds an **alt-research corpus** -- research-call
transcripts and a **63-name materiality-ranked queue** (`docs/architecture/D5_ALT_RESEARCH_PRD.md`, which
carries both). `4.0.0_SA_CRO~Z`, the brief's author, states its Part II verbatim: that corpus is *"the same
directive, a DIFFERENT function"*, and *"AMGT_RESAPP does not consume or replace it."*

**DISPOSITION: `AMGT` DOES NOT COVER IT, AND THIS ENUM IS DELIBERATELY NOT MECE OVER ALL OF D5.** It is
MECE over the domain in §2 -- *what a new project may register under* -- and the corpus **is not a project
and has no project of its own today.** It is **macro-less until it has one**, and when it does, that needs
a fresh Rule 24 record and a fresh word. **Not this record, and not by extension of this one.**

⭐ **This is the whole reason the record is worth writing over a one-member enum:** naming what the enum
does **not** cover is the only content a trivially-satisfiable MECE claim can carry.

### (ii) SAME GRAIN

One value, one grain: **a four-character macro code that prefixes a project code within one directive.**
`AMGT` sits at the same grain as `NFRA`, `ETFS`, `MDPF`, `AUTH` -- the four already ratified across
D0/D8/D11/D12. No sub-macro, no category, no tier is introduced.

### (iii) INTENT COHERENCE -- one axis, and this is where the corpus is excluded

⭐ **THE CRO'S ARGUMENT IS ADOPTED, AND ITS PLACEMENT IS THE PART THAT MATTERS.** `4.0.0_SA_CRO~Z` (msg
21002, ACKed) offered it *"as input to the four-postulate record and not as its answer"*, and said the
exclusion belongs to **postulate (iii), not (i)**. **That is right and this seat adopts it:**

| | `AMGT_RESAPP` | the alt-research corpus |
|---|---|---|
| intent | **produce research about a named security** | **source alt-data signals for the investment process** |
| consumer | an analyst | a pipeline |
| cadence | per request | event-gated on Andrew's word |
| output | a single-name pack | a materiality-ranked build queue |

**Two intents, not one.** Folding both under a macro named *"Asset Management"* would put two intents on
one axis -- **exactly what INTENT COHERENCE forbids.** The exclusion in (i) is a consequence of this, not
an independent judgement.

### (iv) STATE COHERENCE -- what one remedy does NOT move

Ratifying `[AMGT]` for D5 moves **exactly one thing**: it lets a project whose `macro_code` is `AMGT`
register into the D5 tree without an R2 refusal.

**It does NOT move, and none of these follow from it:**
- **It does not register `AMGT_RESAPP`.** That is a separate act, routed to `0.0.0_AB_MSTR~Z`.
- **It does not place D5 on a fabric.** That was Andrew's own act today (LAPTOP -> SITEZ).
- **It does not give the alt-research corpus a macro** (§4(i)).
- **It does not admit a second D5 macro later without a fresh record and a fresh word.**
- **It does not touch D0, D8, D11 or D12**, whose enums are ratified against their own records.

---

## 5. Ratification -- what is settled, what is not, and what one word would do

**SETTLED, by Andrew, and not open:** the VALUE. He said `AMGT` and said *"can get that registered."*
**This record does not re-litigate the choice and offers no alternative.** What it supplies is the FORM the
register demands.

⛔ **NOT SETTLED BY THIS SEAT, AND DELIBERATELY LEFT AT `PROPOSED`:** `MACROS.yaml` states *"ratification
-- Andrew ONLY … Nobody else flips it."* His *"can get that registered"* was said **before this record
existed**, and it plainly reads as *proceed* -- but **reading a pre-record instruction as a post-record
ratification is exactly the inference this seat should not make on a field whose rule names one person.**

**The D12 precedent shows the clean shape and shows why this case differs:** there, Andrew approved the
enum **in advance and in terms** (*"All recs approved, ratify D0 and D8"*, against a card that named the
expected value), with an explicit instruction that when the record landed the field should flip. **Here
there is no such instruction on the record -- only on the registration.**

**SO: the record is complete and the field waits on one word.** `ratification: PROPOSED` stands until
Andrew says otherwise, and **nothing is blocked by that except the tree path itself** -- `AMGT_RESAPP` can
be registered FLAT today, exactly as `NFRA_SECURITY202609` is, if that is preferred to waiting.

⚠ **AND THE HONEST COST OF THE WAIT, SO THE CHOICE IS INFORMED:** the only thing `PROPOSED` costs is that
`AMGT_RESAPP` cannot take a **tree** path (R2 refuses). It costs nothing else -- not the L1 brief, not the
L2 endpoint (`@3bc8f5f2c4`, already done), not any downstream limb.

---

## 6. What this record does NOT claim

- **It does not claim D5's membership is complete.** One declared project, zero register rows, and a named
  uncovered corpus.
- **It does not claim `AMGT` is the only macro D5 will ever need** -- §4(i) says the opposite.
- **It does not claim the census proves absence of collision beyond its corpus.** 53,759 files scanned,
  `corpus=all`, with the ephemeral floor disclosed by the instrument and not searched.
- **It does not read Andrew's four-word definition as a scope statement.** He named a macro; what it covers
  is what §2 and §4 argue, and that argument is this seat's and open to correction.
