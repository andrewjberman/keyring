# POSN_ASTTAX -- L5 DECOMPOSITION (round 4)

**archetype:** DIAGNOSE-THEN-PRICE
**Owner (L5-L6):** `2.0.0_SA_COO~Z` - **Date:** 2026-09-13 ~05:2xZ - **Directive:** D4 - **Macro:** POSN
**PRD:** `../prd/POSN_ASTTAX_PRD.md` **v0.6** @`ae66157381`, read IN FULL at the moment of cutting.
**Answers:** `1.0.0_SA_CTO~Z`'s round-3 analysis `ledger/ROUND_ANALYSIS.round3.md` @`ae66157381`,
which answers `3.0.0_SA_CVO~Z`'s round-3 slug `surprise-channel/remediations/REMEDIATION_v3.md` @`c89c0e45a2`.
**Gate at cut time:** `prd-signoff.py status POSN_ASTTAX` -> **ADMITTED**, both halves SIGNED and
current (ratified-text `3.0.0_SA_CVO~Z`; brief `4.0.0_SA_CRO~Z`, re-signed 05:1xZ after the v0.6 bump).
Read at the moment of acting, never from memory -- row `Z-S7`.

---

## 0. WHY THIS ROUND EXISTS -- the coverage subtraction, not a theme

The round-3 analysis measured, and this seat re-read at source rather than quoting:

```
DENOMINATOR  15 cut task orders under POSN_ASTTAX
DECLARED      6  FWD-1..FWD-6
COVERED       4
UNCOVERED = declared MINUS covered = { FWD-4, FWD-6 }     <- NOT EMPTY
FWD-1 14 | FWD-2 4 | FWD-3 1 | FWD-4 0 | FWD-5 1 | FWD-6 0
```

**FWD-4 and FWD-6 have never had a cell cut against them in three rounds.** This round covers both.
`FWD-6` is the ASTTAX frontend outcome Andrew named at 03:21:46Z.

## 1. THE CONSTRAINT THAT SHAPES EVERY CELL HERE -- stated first, not as a caveat

⛔ **THE PORTAL IS FROZEN** (Andrew, restated twice inside his 03:21Z work direction). FWD-4 and
FWD-6 are **wholly inside it** -- colour is a screen property; agreement between views is a property
of views. **READING portal source is permitted and is not a write.**

**So s-1 and s-2 are MEASURE-AND-PRICE cells and their `<paths>` grants contain no portal path.**
They produce the surface census and the priced change; they do not change a byte. ⛔ **NO FWD IS
GRADED REALIZED ON MEASUREMENT** -- covering an outcome and serving it are different populations,
which is the exact distinction s.2 of the analysis exists to protect. It would be a poor answer to
that finding to close it with cells that cover without serving, and this decomposition says so at the
cut rather than at the grade.
⚠ The write half is **carded, not cut**, and is in front of Andrew as a RESERVED card (05:14Z via
`0.0.0_AB_MSTR~Z`): his 03:21Z *"I expect frontend for both RESAPP and ASTTAX to be done too"* and his
portal freeze are in tension, and **this seat will not read the first as lifting the second.**

## 1a. THE GRAIN OF s-1/s-2 IS CONTESTED, AND IT IS CUT AT THE NARROWER READING ON PURPOSE

`1.0.0_SA_COO~Z` asked before cutting; `1.0.0_SA_CTO~Z` answered at `d7261cf29c` (ROUND_ANALYSIS.round3
s.7) that **measure-and-price IS NARROWER THAN INTENDED** and that the freeze was never on writes. Its
evidence is NOT an inference from Andrew's sentence and deserves to be recorded in full:

- `AMGT_RESAPP.TO-AMGT-rh-1`, cut by `2.0.0_SA_COO~ZZZ` under the SAME freeze on the SAME night, grants
  WRITE paths inside the submodule (`portal/src/pages/SecurityAnalysis/`, an endpoint file) while its
  own text forbids promote, gitlink move and push, and mechanically asserts the superproject gitlink
  still reads `e85f6eb84f`.
- The boundary already in operation there: **write source YES, commit in the submodule YES, MOVE THE
  GITLINK NO, promote/push/DEV/PROD NO.**
- And the sharpest point, which turns this seat's own argument back on it: **FWD-4 and FWD-6 are
  EXERCISED bars. Measurement cannot approach an EXERCISED bar, so pricing cells are COVERING WITHOUT
  SERVING** -- the exact failure s.2 of the analysis exists to name.

⭐ **THAT ARGUMENT IS ACCEPTED AS ARGUMENT AND IS STILL NOT ACTED ON HERE, FOR ONE REASON.** This
loop's own standing body carries Andrew's constraint verbatim: *"Do NOT edit/build/stage portal
(FROZEN both fabrics **until Andrew names it**); READING portal source is permitted and is not a
write."* **He has not named it.** A peer seat's committed order is evidence of PRACTICE; it is not
Andrew naming the surface, and this seat's rule is to relay a word and never adjudicate it wider --
if wider seems plausible, ASK. Wider is plausible, so it is asked.

**CONSEQUENCE, STATED PLAINLY RATHER THAN HIDDEN IN THE GRAIN:** as cut, `AT4-s-1` and `AT4-s-2`
**COVER FWD-6 and FWD-4 and DO NOT SERVE THEM.** Neither outcome can be graded REALIZED on this
round's evidence, and this decomposition does not pretend otherwise. The question was sharpened and
re-put to Andrew through `0.0.0_AB_MSTR~Z`: *does the freeze forbid portal SOURCE WRITES, or only
promote / gitlink move / push?*

⛔ **AND THE WIDENING PATH IS CHEAP AND PRE-DECLARED, so nothing is lost by asking first:** on his
word, `AT4-s-1` and `AT4-s-2` are AMENDED to carry write grants under
`portal/src/...` -- a MODIFICATION, which `to-pipeline-gate.py` LIMB 6 does not refuse (row `Z-S7`) --
and the workers continue in place. **No re-cut, no re-issuance, no second round.** The cost of asking
is one amendment; the cost of widening wrongly is a worker inside a frozen surface on an inference.

⚠ **COORDINATION POINT RAISED BY `1.0.0_SA_CTO~Z` AND RECORDED HERE:** AMGT_RESAPP round 9 is live in
`portal/src/pages/SecurityAnalysis/` while POSN round 4 would head for Positioning and Philosophy/CMA
-- **two projects writing inside ONE submodule with ONE HEAD.** The paths are disjoint; the HEAD is
not. That sequencing is the two COO lanes' and is named now rather than discovered at a conflicted
drain. It does not bite while POSN writes nothing there.

## 2. ⭐ THE GRAIN CORRECTION THAT MAKES FWD-6 CUTTABLE AT ALL

**FWD-6 must NOT be graded on "do the views agree."** They agree TODAY -- because each carries its
own copy of the same wrong two-class list. **An outcome graded on agreement reads PASS on a broken
system** (measured in this seat's brief for Andrew @`4ad3184c0a`). The analysis sharpens the same
point from the other side: S3 is defined as *"The two surfaces"* while the world holds at least
three readers, and **a surface row scoped to two cannot generate a cell that checks three.**

>> **THE BAR IS THEREFORE: EACH READER CAN DISPLAY ALL FIVE RATIFIED CLASSES.** That fails in
   today's world and passes only when the world is fixed -- which is what a criterion is for. <<

## 3. CELLS -- four, and the rectangle

| cell | serves | what it settles | write surface |
|---|---|---|---|
| `AT4-s-1` | **FWD-6** | DERIVE the reader set (never inherit S3's two) and grade each against the five-class bar | none (read-only) |
| `AT4-s-2` | **FWD-4** | one colour per class, the same across every reader s-1 derived | none (read-only) |
| `AT4-s-3` | FWD-5, FWD-1 | durability: extend preserve-don't-clobber to `seed_canonical_securities.py` (`W14-S3`) | POSN-owned seed script |
| `AT4-s-4` | FWD-1 | settle the retag member set at **ELEVEN**, by subtraction over a printed denominator | none (record only) |

**DEPENDENCY EDGES:** `AT4-s-1 -> AT4-s-2` (the colour census needs the reader set as its
denominator; enumerating colour over a guessed surface list is the wrong-domain failure this project
has already banked twice). `AT4-s-3` and `AT4-s-4` are INDEPENDENT.

**`fanout: 3 of 3 chains, cap 8`** -- wave 1 spawns `s-1`, `s-3`, `s-4` in parallel; `s-2` follows
`s-1`'s census.

## 4. WHAT THIS ROUND DELIBERATELY DOES NOT CUT

- **`Z-S42`'s disclosure obligation is DISCHARGED, not a cell.** `1.0.0_SA_CTO~Z` landed it as item 4
  of PRD v0.6. Cutting it would double-issue work already done -- checked at source before cutting.
- **The retag (`TO-T6-1`) stays NO-GO and unspawned**, and the four carried orders (`TO-S2-1`,
  `TO-S3-1`, `TO-T6-1`, `TO-T7-1`) are NOT re-cut. They are carried on Andrew's LD-0562 word.
- **No deploy cell.** The positioning deploy is approved conditional on the two-seat never-widen
  sign-off; it is Terraform-owned and is not a worker's act.
- **Nothing under `portal/` is written.**

## 5. ⚠ CARRIED INTO THIS ISSUANCE: ROUND 4 CAN BE CUT BUT NOT CLOSED ON TODAY'S TERMS

Row `POSN_ASTTAX-Z-S46` @`569b885a62`, named at the cut rather than discovered at L10. The round-3
L10 exception in `.tools/surprise-row-gate.py` is pinned to `total != 15`; cutting this round raises
the project's task-order total above 15, so that exception can never match again -- fail-closed, the
safe direction. At round 4's close the SAME four carried orders are still non-terminal, so
`_open_tos_for_project` returns 4 open and the round-4 slug is refused by the same limb.
**Nothing inside round 4 terminates them.** This is a KNOWN OPEN ITEM from the moment of the cut; the
gate is `1.0.0_SA_CTO~Z`'s and this seat proposes no change to it.

## 6. Four-postulate record (Rule 24)

- **(i) MECE by SUBTRACTION over a declared domain:** the domain is the PRD v0.6 header's
  `endpoint_outcomes`, denominator 6; covered = 4 measured from the 15 cut orders' `cell_refs`;
  uncovered = the remainder, `{FWD-4, FWD-6}`. Written as denominator-minus-covered, never as a
  forward list of what this seat thought of.
- **(ii) SAME GRAIN:** every cell is one measurable question with one owner and one artifact.
- **(iii) INTENT COHERENCE:** one axis -- close the two never-served outcomes to the limit the freeze
  permits, plus the two durability items round 3 left in no triple.
- **(iv) STATE COHERENCE:** s-1/s-2 move nothing and are explicitly NOT realization; s-3 changes
  APPLIED state in a POSN-owned script; s-4 changes a RECORD only. **What no cell here moves:** the
  served artifact, the deployed bytes, anything under `portal/`, and the retag.
