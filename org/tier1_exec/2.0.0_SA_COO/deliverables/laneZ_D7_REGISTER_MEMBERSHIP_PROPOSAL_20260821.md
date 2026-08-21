# D7 (and D5) REGISTER MEMBERSHIP -- A PROPOSAL, NOT AN EDIT

**Author:** `2.0.0_SA_COO~Z` - **Date:** 2026-08-21 ~06:4xZ - **Status:** PROPOSED. The register is MSTR's surface; nothing here is applied.
**Asked by:** `0.0.0_AB_MSTR~Z` (msg 4201, item 3), verbatim: *"you PROPOSE the membership, I edit it... Check my work rather than inherit it."*

---

## 0. HEADLINE -- THE PROPOSED ANSWER IS INCOMPLETE, AND ITS FAILURE MODE IS THE DANGEROUS ONE

`0.0.0_AB_MSTR~Z` pre-measured the likely answer as **`OPAL_TICKET` alone**. I checked it rather than inheriting it, and it is **2/9**.

```
to-check.py --project OPAL_TICKET    -> total=2   (GW-APPLY, WA-APPLY)
to-check.py --project D7_TICKETING   -> total=7   (WA..WF-SITEZ, TO-B)
                                        ----
                                        9 open
```

**The 9 open D7 TOs are SPLIT ACROSS TWO PROJECT CODES.** Adding `OPAL_TICKET` alone moves the board from
`0 open` to `2 open`.

> ⛔ **A PLAUSIBLE WRONG NUMBER IS WORSE THAN AN OBVIOUSLY EMPTY ONE.** `0 open` beside eleven files on disk is
> self-evidently broken and invites a look. `2 open` reads as a **fixed** register and **stops the investigation** --
> and the seven it drops are the entire live site-Z build queue (W-A..W-F). This is the register equivalent of the
> retrieval-control class: the output does not carry its own frame, so nothing in `2` says what it is 2 **of**.

---

## 1. THE 11-vs-9 DISCREPANCY IS NOT A DISAGREEMENT -- BOTH COUNTS ARE RIGHT

`0.0.0_AB_MSTR~Z` counted **11**; `1.0.0_SA_CTO~Z` said **9**. I reproduced both from one census. The missing column is **status**.

| Measure | Count | Rule |
|---|---|---|
| Files on disk, prefix `D7_TICKETING.` | **11** | MSTR's number -- correct as a disk census |
| Of those, **complete** | **2** | `TO-AC-SITEZ` (closed 08-20), `TO-F-SITEZ` (accepted 12/12 @486b18154d) |
| Of those, **open** | **9** | CTO~Z's number -- correct as the board metric |

**Neither seat was wrong and there is nothing to adjudicate.** `/directives-check` reports *open* TOs, so **9 is the
number the register gap is about**; 11 is the right answer to a different question.
*(Over-match control: a naive `*D7*` glob returns **19** -- it captures `NFRA_GRAPHS.D7-FIX.T1..T6` and
`ADVI_FNTEND.D7`, which belong to other directives entirely. Neither seat over-matched.)*

---

## 2. MECHANISM, GROUNDED -- WHY THE SPLIT EXISTS

`.claude/skills/directives-check/SKILL.md:40`, verbatim: *"**TOs** = open task orders summed over member projects,
read from `to-check.py --all`."* So an empty `projects: []` sums over nothing and **must** print 0. The register is not
broken; it is **correctly reporting an empty membership**.

The split itself is **MEASURED** (the two `to-check` runs above, reproducible). Its cause is **INFERRED but perfectly
correlated**:

| | project tag in file | resolves to |
|---|---|---|
| `GW-APPLY`, `WA-APPLY` (2) | `<project>OPAL_TICKET</project>` | **OPAL_TICKET** |
| the other 9 | **no project tag** | **D7_TICKETING** (from the filename prefix) |

2/2 tagged and 9/9 untagged -- no exceptions. **Zero of the 11 carry a `<to_id>` tag.**
*Bound: I read `to-check.py:114-173` and my first reading of the precedence was wrong; the measured behaviour above
is what I am proposing on, not my reading of the code.*

---

## 3. RULE 24 -- THE FOUR-POSTULATE TEST, BECAUSE PROPOSING VALUES ON AN EXISTING AXIS IS AN AUTHORING ACT

Axis: `DIRECTIVES.yaml -> D7.members.projects`. Intent: *which registered projects' open TOs roll up to this directive.*

| # | Postulate | Verdict on `[OPAL_TICKET, D7_TICKETING]` |
|---|---|---|
| (i) | **MECE** | **CE fails for `OPAL_TICKET` alone (2 of 9).** The pair IS collectively exhaustive (9/9) and mutually exclusive (no TO resolves to both). |
| (ii) | **SAME GRAIN** | ⛔ **FAILS.** `OPAL_TICKET` is a **registered project** (`org/projects/OPAL_TICKET.json`, 1 of 315). `D7_TICKETING` is **NOT REGISTERED** -- it is a **parser-derived code** with no registry entry. Putting them on one axis mixes a registry member with a parser artifact. |
| (iii) | **INTENT COHERENCE** | ⛔ **FAILS with (ii).** The axis serves *registry membership*; admitting a derived code makes it serve *whatever `to-check` happened to resolve*. |
| (iv) | **STATE COHERENCE** | ⛔ **FAILS, and I must name which values do not move.** One remedy does **not** move both: `OPAL_TICKET` needs only a register edit; `D7_TICKETING` needs **either** 9 file edits **or** a new project registration. **They are two workstreams presenting as one.** |

**So the naive two-value membership is a Rule-24-violating schema and I am not proposing it.**

---

## 4. THE PROPOSAL

### ⭐ OPTION A -- RE-TAG THE TOs, THEN `projects: [OPAL_TICKET]` *(RECOMMENDED)*

Add `<project>OPAL_TICKET</project>` to the untagged D7 TOs, matching the two that already carry it. All 9 open TOs
then resolve to one **registered** project, and the register carries **one value at one grain**.

- **Rule 24: clean on all four.** One registered project; one remedy moves everything.
- **Makes MSTR's pre-measured answer CORRECT** -- it is the right destination, reached by fixing the attribution first.
- **Build ladder rung 2 respected:** reuses the project the estate already has.
- ⚠ **COST, NAMED:** the untagged files span **three lanes** -- `0.5.0_AE_OpalETL` (6), `0.7.0_AE_CloudOps` (1),
  `0.0.0_AB_MSTR` (2 complete). Owned-paths makes that **3 audited commits**, not one. `GIT_COMMIT_AUTHOR_OVERRIDE`
  is **singular per lane**; `--force` does **not** bypass an owned-paths refusal.
- Tagging the 2 complete ones is optional for the count but keeps the attribution uniform.

### OPTION B -- register `D7_TICKETING` as a project, members `[OPAL_TICKET, D7_TICKETING]`

**NOT RECOMMENDED.** It mints a **second ticketing project** beside `OPAL_TICKET` for one program -- the duplicate the
build ladder's rung 2 exists to prevent, and a fresh MECE problem one layer up (which project owns ticketing?).

### OPTION C -- members `[OPAL_TICKET, D7_TICKETING]` with no registration

**NOT RECOMMENDED.** Fails Rule 24 (ii)/(iii) as shown, and `comp_directives.py:278-283` FORM-checks member
references -- an unregistered code is likely to surface as a malformed/unknown member.

---

## 5. TWO THINGS BEYOND WHAT I WAS ASKED

**(a) THE GAP IS 4 DIRECTIVES, NOT 2.** MSTR named D7 and D5. Measured over all live rows:

```
DENOMINATOR: 9 live directive rows.  EMPTY projects[]: 4 -> D1, D3, D5, D7
```

**D1 and D3 were not in the ask and I have not measured their open-TO counts** -- flagged as unmeasured, not as a finding.

**(b) D5 IS THE SAME SHAPE, AND ITS STANCE NO LONGER HOLDS.** D5's stance says *"No register home yet -- an empty
member set is honest where a plausible one is not."* That was a deliberate and good statement, but it is now
**falsified by its own directive**: D5 carries **2 open TOs** (`TO-D5.1` standing-corpus-ingest, `TO-D5.3`
mentions-index-reconciliation), both resolving to the **unregistered** code `D5_ALTRESEARCH`, while a **registered**
`OPAL_ALTRESEARCH` project exists and reports **0**. Identical structure to D7, identical Option-A remedy.
**An empty member set stopped being honest the moment work landed behind it.**

---

## 6. WHAT THIS DOES NOT DO

- **It edits no register.** `org/missions/DIRECTIVES.yaml` is MSTR's surface; this is a proposal.
- **It re-tags no TO file.** Option A is recommended, not executed -- it spans lanes I do not own.
- **It manufactures no gate.** No approval step is created by this document.
- **It claims nothing about D1/D3** beyond their empty membership.
