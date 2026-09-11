# MACRO ENUM -- Rule 24 four-postulate record for **D4 "Positioning"**

**archetype:** SCRIBE

**Author:** `2.0.0_SA_COO~Z` · **Date:** 2026-09-11 ~03:5xZ · **Fabric:** site-z
**Authority to author:** `org/missions/MACROS.yaml` header -- *"proposal: 2.0.0_SA_COO authors the
per-directive set WITH its Rule 24 four-postulate record and a word-boundary token census. A bare edit
is not a proposal."*
**Seating:** `1.0.0_SA_CTO~Z` msg 21150, on Andrew-direct 2026-09-11 VERBATIM **"do it"**.
**Ratification:** ANDREW ONLY. This document is a PROPOSAL. Nothing in it flips `ratification:`.

> ## ⭐ RECOMMENDATION: **`D4: [POSN, ETFS]`**
>
> ⛔ **THIS DIFFERS FROM THE PROPOSAL I WAS HANDED, AND THE DIFFERENCE IS THE POINT OF THE RECORD.**
> `1.0.0_SA_CTO~Z` proposed `D4: [POSN]` and asked this seat to adjudicate the second member as *"the
> real four-postulate question"*. I adjudicated it and land on **two members, not one.** The reason is
> one measured fact, given in full at §3.

---

## 1. The DECLARED DOMAIN, and its falsification

**Domain:** the projects of directive D4, per `org/missions/DIRECTIVES.yaml` `D4.members.projects`.

**⛔ THE DOMAIN IS FALSIFIED BEFORE THE SUBTRACTION RUNS (rule 24(i), the domain-choice clause).**
Choosing the domain is itself a claim, so it is tested by an UNSCOPED read rather than trusted:

```
UNSCOPED  every flat register row whose "directive" == "D4"
          DENOMINATOR: 360 org/projects/*.json parsed, 0 unparseable
          rows carrying directive D4: 6

UNSCOPED minus DECLARED : (none -- the domain holds every D4 row)
DECLARED minus UNSCOPED : (none)
VERDICT                 : domain HOLDS -- the subtraction below is valid
```

⚠ **MY FIRST RUN OF THIS PROBE WAS BROKEN AND SAID THE OPPOSITE.** It split paths on `/` on a Windows
filesystem, so every basename read `projects\ETFS_CANON`, no name matched the declared set, and the
probe reported **all six rows OUTSIDE the domain -- i.e. "the subtraction is VOID."** That is a
finding-shaped output from an instrument defect, and it would have been the most dramatic line in this
record. It is disclosed rather than quietly corrected, because the class matters: *a broken probe
produces a confident verdict in whichever direction its bug points.* Re-run with `os.path.basename`,
the answer inverted to the one above.

**The six members, measured at authorship (register rows, not prose):**

| project | status | dep_stage | code conforms `^[A-Z]{4}_[A-Z0-9]{3,18}$` |
|---|---|---|---|
| ASSETCLASS_TAXONOMY | **active** | REGISTERED | ⛔ **REFUSED** (10-char head) |
| ETFS_CANON | **scoping** | -- | ✅ CONFORMS |
| ETFS_INGEST | complete | EXECUTING | ✅ CONFORMS |
| ETFS_POSITIONING | complete | EXECUTING | ✅ CONFORMS |
| ETFS_SATELLITES | complete | CLOSED | ✅ CONFORMS |
| POSN_TENANCY | complete | PRD | ✅ CONFORMS |

**Grammar read from `org/standards/PROJECT_TREE.contract.json`, never from prose** (the D12 census in
MACROS.yaml is a standing warning about quoting a bound from prose): `levels[1].regex ^[A-Z]{4}$`,
`levels[2].regex ^[A-Z]{4}_[A-Z0-9]{3,18}$`. **POSN CONFORMS. ETFS CONFORMS. POSN_ASTTAX CONFORMS.**

**Prospective scope (spec s.8):** `org/missions/` holds D0, D5, D8, D9, D11, D12 and **NO D4 folder**.
Nothing is in a D4 tree today, so this enum governs only what may ENTER.

## 2. The word-boundary token census -- **run by this seat, not inherited**

`1.0.0_SA_CTO~Z` supplied a census and said not to re-run it. I re-ran it anyway. Not distrust: a
record carries its author's measurement, and the two numbers differ, which is itself the lesson.

```
comp-find '\bPOSN\b' --band HEAD --limit 20
  MINE  (03:4xZ)  108 hits / 55,352 files scanned [corpus=all]  bands SURFACED=11 CONFIG=16 DOC=81
  CTO's (~03:3xZ)  95 hits / 55,345 files scanned [corpus=all]  bands SURFACED=9  CONFIG=16 DOC=70
  band=HEAD -> 0  (no file is NAMED for this token)
  DISCLOSED NOT-SEARCHED: 425,129 ephemeral-floor · 2,272 binary · 1 unreadable
```

**The delta is VINTAGE, not disagreement** -- same instrument, same corpus setting, ~20 minutes apart,
and the estate wrote to itself in between (this session's own traffic included). Recorded because a
future reader finding 95 in one document and 108 in another must not read it as a contradiction.
⛔ **AND NEITHER NUMBER IS RE-USABLE: a census is a measurement at a vintage.** The D8 census in
MACROS.yaml was made false within the hour by an edit to a *different* file; that precedent is why
this line carries its timestamp.

**CONTROLS -- the census means nothing without them:**

| control | result | what it establishes |
|---|---|---|
| POSITIVE `\bETFS\b` | **3,846 hits / 55,137 files**, bands DEF=3 SURFACED=720 CONFIG=564 DOC=2,534 | the instrument returns large non-zero on this corpus; a low count is a measurement, not a dead probe |
| NEGATIVE `\bPOS\b` | **907 hits / 55,122 files**, a WHOLLY UNRELATED LIVE POPULATION (`colorama/ansi.py`, `numpy/f2py/symbolic.py` -- `POS` as a code constant) | a 3-char neighbour of this macro is a live token in the dependency plane, and the word boundary separates it cleanly |
| CASE `\bposn\b` | **134 hits / 55,124 files**, bands **SURFACED=97** CONFIG=9 DOC=28 -- and the surfaced hits are LIVE PRODUCTION SOURCE (`data/cot/scripts/gold/runners_cot/b03_valuation_integrity.py`, `c03_twr_lineage.py`) | ⛔ **THE LOWERCASE FORM IS NOT CLEAN AND THIS RECORD CLAIMS NO CASE-NEGATIVE.** `posn` is a live identifier in the gold runners -- **97 surfaced hits against the uppercase form's 11**, i.e. the lowercase token is the *more* common one in first-party code. It is not a collision for the MACRO because `^[A-Z]{4}$` refuses it, but the exclusion is the GRAMMAR's doing, not the census's, and a reader must not cite this row as "POSN is unused" |

**INTERPRETATION -- and it is the opposite of the usual finding.** `POSN` is **NOT** a clean-slate
token the way `AMGT` (32 hits, all same-day) and `IRPT` (47 hits, all same-day) were. It has **real
prior use**, and that use is **POSITIONING**: `POSN_TENANCY`, positioning columns, D4's own history.
⛔ **THAT IS SUPPORT, NOT COLLISION, AND THE DISTINCTION IS ADJUDICATED HERE RATHER THAN ASSUMED.** A
collision is prior use of the token for a DIFFERENT referent. Every prior use found is the SAME
referent -- positioning -- under a directive Andrew renamed to "Positioning" on 2026-09-10. The token
is being ratified for the meaning it already carries.

## 3. ⛔ THE DECIDING FACT -- why the enum is TWO members

Subtraction over the validated domain, for each candidate enum:

```
[POSN] alone     covers  POSN_TENANCY, ASSETCLASS_TAXONOMY->POSN_ASTTAX     2 of 6
                 UNCOVERED: ETFS_CANON, ETFS_INGEST, ETFS_POSITIONING,
                            ETFS_SATELLITES                                 4 of 6
[POSN, ETFS]     covers  all six                                            6 of 6
                 UNCOVERED:                                                 0 of 6
```

Three of the four uncovered are `complete`/`CLOSED` and prospective scope means an enum owes them
nothing. **ETFS_CANON IS THE ONE THAT DECIDES THIS, AND IT IS NOT COMPLETE.**

1. **ETFS_CANON's register row reads `status: scoping`.** Not complete, not closed.
2. **Its code CONFORMS to the tree grammar today** -- so a macro is the ONLY thing standing between it
   and a tree home.
3. **Andrew set its re-entry condition himself**, carried verbatim in `DIRECTIVES.yaml`
   `D4.members_note`: *"We can revisit ETFS_CANON After INGEST is done."* The note is emphatic that
   this is **"A DEFERRAL, NOT A REMOVAL"** and that *"a reader must not take its absence from the
   completion set as removal from the directive."*
4. **⭐ THAT CONDITION HAS FIRED.** `ETFS_INGEST` reads `status: complete`. The trigger Andrew named
   for revisiting ETFS_CANON is satisfied as of this measurement.

So `[POSN]` alone would, on the day it is ratified, make a **live, conforming, explicitly-deferred
project whose owner-set re-entry condition has already fired** permanently unable to enter its own
directive's tree. **That is a bare prohibition, not a taxonomy** -- and that phrase is not mine: it is
the reason recorded in MACROS.yaml for rejecting the narrow alternative on D8.

⛔ **WHY THE D9 PRECEDENT DOES NOT APPLY, read at its reasoning rather than its shape.** D9 ratified
`[IRPT]` alone and named four uncovered OPAL_* rows. That was correct **because widening would not
have helped them**: they are pre-macro flat rows and *two of the four carry a second underscore and are
unregisterable at ANY macro.* The record says so in terms -- *"the wider enum would not make them
eligible while appearing to."* **D4 inverts on exactly that fact.** ETFS_CANON is eligible the moment
ETFS is listed. Copying D9's ANSWER while ignoring D9's REASON would be the shape-matching this estate
keeps catching.

⚠ **WHAT I AM NOT CLAIMING: that ETFS_CANON WILL enter the tree.** Nobody has said it will, and its
`scoping` status is not a plan. The argument is about **EXPRESSIBILITY, not prediction** -- `[POSN,
ETFS]` leaves a door open without pushing anyone through it, while `[POSN]` welds it shut on day one
and would need a fresh record, a fresh census and a fresh Andrew word to reopen.

⚠ **AND A MACRO UNDER TWO DIRECTIVES IS THE DESIGNED PATTERN, NOT AN ANOMALY.** MACROS.yaml's own
header: *"A macro repeats across directives by design (NFRA under D0 and D11)."* The ETFS charter
ALREADY reads *"ETF satellites products -- positioning, ingest, guardrails ... **(D4, D8)**"*. Ratifying
`[POSN]` alone would leave that charter asserting a D4 span the enum refuses -- a live contradiction
inside one file. Ratifying `[POSN, ETFS]` makes the charter true as written.

## 4. The four postulates, run

**(i) MECE over a DECLARED domain, by SUBTRACTION from a printed denominator.**
Domain declared (§1), falsified by an unscoped read (§1), subtraction printed (§3). `[POSN, ETFS]`
covers 6 of 6, **0 uncovered**. ⛔ **UNCOVERED MEMBER NAMED ANYWAY, because "0 uncovered" is a
measurement at this vintage and not an invariant:** `ASSETCLASS_TAXONOMY` is covered by POSN only
*after* it is renamed -- its current code is **REFUSED by the tree grammar** (10-char head). **The
macro is necessary and NOT sufficient for it**, exactly the two-independent-bars shape the D9 record
found on OPAL_TAXSMA_PT2. Ratifying the enum does not make `ASSETCLASS_TAXONOMY` tree-ready; the
rename to `POSN_ASTTAX` is a second, independent act.

**(ii) SAME GRAIN.** Both members are 4-char macro tokens naming a body of product work under one
directive -- the same grain as NFRA, AMGT, IRPT, MDPF, AUTH. Neither is a project, a phase, or a team.

**(iii) INTENT COHERENCE -- one axis, one intent.** The axis is *what body of work does a D4 project
belong to*. `POSN` = the positioning/taxonomy substrate (how holdings are classified and positioned);
`ETFS` = the ETF satellites products. ⚠ **THE NEAR-MISS IS REAL AND IS NAMED RATHER THAN GLOSSED:**
the ETFS charter's first word is *"positioning"*, so the two members abut. They remain distinct
because ETFS is the **product line** (satellites: canon, ingest, guardrails) and POSN is the
**classification substrate** the products and the model-portfolio surfaces both read. `POSN_ASTTAX`
serves Positioning **and** Philosophy/CMA -- two surfaces, neither an ETF satellite -- which is the
evidence that POSN is not a sub-part of ETFS. **If Andrew reads these as one axis, the answer is
`[ETFS]` with POSN retired, not a merge, and this paragraph is the one to overturn.**

**(iv) STATE COHERENCE -- what this flip does NOT move.** Ratifying D4 moves **D4 only**. It does not
ratify or widen D0/D5/D8/D9/D11/D12. It does not register `POSN_ASTTAX` -- that is `1.0.0_SA_CTO~Z`'s
separate act, and R2 merely stops refusing it. It does not create `org/missions/D4/`. It does not move
`ETFS_GUARDRAIL`, which is D8 and laptop-placed. It does not change D4's placement (SITEZ), its
completion_bar (⛔ still Andrew's un-run smoke test), or its stance. It does not rename
`ASSETCLASS_TAXONOMY`. And it does not touch the 360 flat register rows -- **scope is PROSPECTIVE
ONLY.**

## 5. Alternative named and rejected

**`D4: [POSN]`** -- the proposal handed to this seat. **Rejected on §3**: it bars ETFS_CANON, a live
`scoping` project with a conforming code and a fired re-entry condition, from its own directive's tree
on the day of ratification, and it leaves the ETFS charter's own `(D4, D8)` claim unrealizable. Its
strongest argument is the honest one and is recorded here rather than suppressed: **Andrew named POSN
and named nothing else**, and an enum is a measurement of what is entering rather than a wish list. If
he wants the narrow list, it is one word, this record is what he overrules, and **nothing is lost** --
ETFS can be added later by exactly this process.

**`D4: [POSN, ETFS, MDPF]`** -- not proposed. MDPF is D8's; no D4 row carries it; there is no
measurement supporting it. Named only so the reader sees the enum was bounded by the census rather
than by where I stopped listing.

## 6. What ratification would look like

Andrew's one word on `[POSN, ETFS]` (or on the narrow `[POSN]`). On it, the register owner writes
`directives.D4.macros` and flips `ratification:` quoting this record. **This seat does not flip it and
has not edited `MACROS.yaml`.** `1.0.0_SA_CTO~Z` then completes tree registration per msg 21150.

⛔ **ONE THING THE RATIFY MUST NOT BE READ AS SETTLING:** `ASSETCLASS_TAXONOMY` -> `POSN_ASTTAX` is a
RENAME, and the PRD's own s.7 carries it to Andrew as an open naming call. The macro clears one bar;
the rename is the other. **Both, or the project still cannot enter the tree.**

---

**Push state:** LOCAL at authorship; `0.0.0_AB_MSTR~Z` holds all pushes.
