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

The split itself is **MEASURED** (the two `to-check` runs above, reproducible).

⛔ **THE CAUSE I ORIGINALLY GAVE HERE WAS FALSE AND IS CORRECTED IN FULL -- see the amendment at sec. 4.**
This section asserted *"`GW-APPLY`/`WA-APPLY` carry a `<project>` tag, the other 9 carry none"* and called the
correlation perfect. **NINE of the eleven carry a project tag**, six of them the correct `OPAL_TICKET`, in an
**ATTRIBUTE** form (`<task_order ... project="...">`) that my search shape could not match and that
`to-check.py`'s `_extract_tag` -- `rf"<{tag}>(.*?)</{tag}>"`, child elements only -- structurally cannot read.

| | project tag in file | resolves to |
|---|---|---|
| `GW-APPLY`, `WA-APPLY` (2) | `<project_code>OPAL_TICKET</project_code>` **(child)** | **OPAL_TICKET** |
| `WA`..`WF-SITEZ` (6) | `project="OPAL_TICKET"` **(attribute)** | **D7_TICKETING** -- tag unread |
| `TO-AC`, `TO-F`, `TO-B` (3) | `project="OPAL_TICKETING"` **(attribute, UNREGISTERED CODE)** | **D7_TICKETING** -- tag unread |

**Zero of the 11 carry a `<to_id>` tag** -- that part was and remains true, and it is why the filename-prefix last
resort is reached at all.
*Bound, twice over: my first reading of `to-check.py`'s precedence was wrong, and my second error was searching the
wrong tag SHAPE. Both are corrected against source and against a re-derived census; nothing in this document now
rests on either.*

---

## 3. RULE 24 -- THE FOUR-POSTULATE TEST, BECAUSE PROPOSING VALUES ON AN EXISTING AXIS IS AN AUTHORING ACT

Axis: `DIRECTIVES.yaml -> D7.members.projects`. Intent: *which registered projects' open TOs roll up to this directive.*

| # | Postulate | Verdict on `[OPAL_TICKET, D7_TICKETING]` |
|---|---|---|
| (i) | **MECE** | **CE fails for `OPAL_TICKET` alone (2 of 9).** The pair IS collectively exhaustive (9/9) and mutually exclusive (no TO resolves to both). |
| (ii) | **SAME GRAIN** | ⛔ **FAILS.** `OPAL_TICKET` is a **registered project** (`org/projects/OPAL_TICKET.json`, 1 of 315). `D7_TICKETING` is **NOT REGISTERED** -- it is a **parser-derived code** with no registry entry. Putting them on one axis mixes a registry member with a parser artifact. |
| (iii) | **INTENT COHERENCE** | ⛔ **FAILS with (ii).** The axis serves *registry membership*; admitting a derived code makes it serve *whatever `to-check` happened to resolve*. |
| (iv) | **STATE COHERENCE** | ⛔ **FAILS, and I must name which values do not move.** One remedy does **not** move both: `OPAL_TICKET` needs only a register edit; `D7_TICKETING` needs a **RESOLVER FIX** (`.tools/to-check.py` reading the attribute form) -- *not* the 9 file edits or the new project registration I originally listed here, both of which the sec.-4 amendment supersedes. **They are two workstreams presenting as one, and the postulate holds for a better reason than I first gave: the second remedy is not even in the same repo layer as the first.** |

**So the naive two-value membership is a Rule-24-violating schema and I am not proposing it.**

---

## 4. THE PROPOSAL

## ⛔ AMENDED 2026-08-21 ~0915Z BY THE AUTHOR -- OPTION A IS WITHDRAWN. MY MEASUREMENT STOOD; MY DIAGNOSIS DID NOT.

`0.0.0_AB_MSTR~Z` went to execute Option A as register owner, **stopped before touching anything**, and found the
cause. Re-derived independently at this seat and it is worse than they measured.

**THE 2-vs-7 SPLIT IS REAL AND REPRODUCES. THE REASON I GAVE FOR IT IS FALSE.** I wrote that only two files carry a
project tag. **Nine of eleven do -- in an ATTRIBUTE form my search could not match.** `to-check.py`'s `_extract_tag`
is `rf"<{tag}>(.*?)</{tag}>"` (source-read): it matches **CHILD ELEMENTS ONLY** and structurally cannot see
`project="..."`, so those files fall through to the filename-prefix last resort at `:171-173` and resolve
`D7_TICKETING`.

```
attr project="OPAL_TICKET"      6   WA WB WC WD WE WF-SITEZ   correct value, INVISIBLE to the tool
attr project="OPAL_TICKETING"   3   TO-AC, TO-F, TO-B         WRONG SPELLING, NOT A REGISTERED PROJECT
child <project_code>OPAL_TICKET  2   GW-APPLY, WA-APPLY        visible to the tool
                                --
                                11
```

> **THE SIX ALREADY CARRY THE CORRECT VALUE. OPTION A WOULD HAVE WRITTEN `OPAL_TICKET` INTO A SECOND LOCATION ON
> FILES THAT ALREADY SAY `OPAL_TICKET`, BECAUSE THE READER IGNORES THE FIRST.**

⛔ **AND IT WOULD HAVE DESTROYED THE EVIDENCE OF THE ONE THING WORTH FINDING.** `OPAL_TICKETING` is a **third
spelling and is NOT a registered project** (control: `OPAL_TICKET` is). A blanket re-tag would have silently
overwritten it, and nobody would have learned that TOs were authored against a project code that does not exist.
**`0.0.0_AB_MSTR~Z` measured that on ONE file; it is on THREE** -- and two of the three (`TO-AC`, `TO-F`) are the
COMPLETE ones, so the wrong spelling spans closed and open work alike.

**THE CLASS, AND IT IS THE NIGHT'S, ONCE MORE: AN ABSENCE PRODUCED BY SEARCHING THE WRONG *SHAPE*.** Not a wrong
pattern and not a wrong case -- my `grep -o '<project[_code]*>'` requires the closing `>` and therefore **cannot**
match an attribute. It returned a clean, confident, well-formed zero. `0.0.0_AB_MSTR~Z` made the identical error
first and caught it by accident from an unrelated header.

### ⭐ AMENDED RECOMMENDATION -- FIX THE RESOLVER, NOT THE INSTANCES

**ONE file in `.tools/`, ONE lane**, and it repairs every attribute-form TO ever authored plus every future one.
Option A was nine files across THREE lanes -- one of them a laptop seat -- and would have left the next
attribute-form TO broken identically. **Build-ladder rung 2 points at the resolver.**
**SEPARATELY AND NOT AS PART OF IT:** the three `OPAL_TICKETING` files need a triage decision (correct the spelling,
or register the code) -- **a decision, not a sweep**, and `TO-B` sits in a laptop lane.
⛔ **DO NOT SET THE REGISTER MEMBERSHIP BEFORE THE RESOLVER IS FIXED.** The value `[OPAL_TICKET]` is still right,
but setting it today moves the board `0 -> 2` -- **which is exactly the failure this proposal was written to prevent:
a partial fix that looks complete and stops the investigation.** My own argument, turned against my own remedy.
*(Tool-behaviour change -> `1.0.0_SA_CTO~Z`'s gate. Resolver fix put to Andrew by `0.0.0_AB_MSTR~Z`, pending.)*

---

### ❌ OPTION A -- RE-TAG THE TOs, THEN `projects: [OPAL_TICKET]` *(WITHDRAWN, see the amendment above)*

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
- **It re-tags no TO file, and re-tagging is no longer recommended at all** -- Option A is **WITHDRAWN** (sec. 4
  amendment). The amended recommendation is a **resolver fix** in `.tools/`, which is one file in one lane and is
  `1.0.0_SA_CTO~Z`'s gate to route, not mine to execute.
- **It changes no `project=` tag**, including the three carrying the unregistered `OPAL_TICKETING` spelling -- those
  are a triage DECISION (correct, or register), and one of them sits in a laptop lane.
- **It manufactures no gate.** No approval step is created by this document.
- **It claims nothing about D1/D3** beyond their empty membership.
