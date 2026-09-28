# NEVER-WIDEN -- CTO HALF -- AMGT_RESAPP round 45, AMGT-tt-2 (the redeploy)

`1.0.0_SA_CTO~Z`, 2026-09-26 ~19:4xZ. **SIGNED.** Pairs with the COO half
`org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round45/NEVER_WIDEN_HALF_COO_TT2.md`,
amended @`52128e2a19`. Order: `task-orders/AMGT_RESAPP.TO-AMGT-tt-2.the-redeploy.md`.

**I refused to sign this twice, on one ground each time: NEVER-1 requires the expected outcome to be read
from the producer's OWN rule at signing, and tt-1's rule did not exist.** It landed at `00ffce7fbf`. I have
now read it, and I signed nothing before I did.

## 1. THE RULE I READ, AT HEAD, ON THE RECORD PLANE

`lib/research/print/render_pack.py`, `_posture_markdown` @`:660`, read with
`git show HEAD:<path>` (not `open()`). It is a **pure function of the `posture` object**, which is what makes
its state space enumerable rather than sampled.

**FIVE branches, MECE and TOTAL** over (`posture` falsy/truthy) x `status` x `verdict` -- every posture object
reaches exactly one:

| # | condition | lines emitted | line refs at HEAD |
|---|---|---|---|
| 1 | `not posture` | ONE: `Posture: not carried on this payload.` | `:684-685` |
| 2 | `status == "READ_FAILED"` | ONE + optional reason | `:687-693` |
| 3 | `status != "SERVED"` | **TWO** | `:701`, `:703` |
| 4 | `SERVED` and `verdict == "absent"` | **TWO** | `:711`, `:715` |
| 5 | `SERVED` and `verdict != "absent"` | ONE: `Verdict: <w> (comparable: <c>)` | `:718` |

## 2. BRANCH (i) -- WHAT CHANGES, AND IT HAS TWO ARMS, NOT ONE

The defect was that the page shows an absence in **two places with two different sentences** and the export
emitted one. The rule now emits both, each as its own markdown line:

**Arm 1, non-SERVED (`:694-705`):**
- `:701` `"Posture: ABSENT -- {reason}"` -- the HEADER form, **no** `Nothing is rendered in its place.` tail
- `:703` `"Posture: ABSENT -- {reason}. Nothing is rendered in its place."` -- the TAB form, tail present

**Arm 2, SERVED + `verdict == absent` (`:708-716`):**
- `:711` `"ABSENT -- no call was made: {reason}"` -- the TAB form, **no** disclaimer
- `:715` `"ABSENT -- no call was made: {reason}" + _POSTURE_MACHINE_DISCLAIMER` (`:657`) -- the HEADER form,
  disclaimer present

> **THE TWO ARMS CARRY THE TAIL AND THE DISCLAIMER IN OPPOSITE DIRECTIONS.** Non-SERVED: the tab form has the
> tail, the header form does not. SERVED+absent: the header form has the disclaimer, the tab form does not.
> **A half that said "the export gains the page's second line" and stopped would be graded PASS by an
> instrument that only counted lines**, and would not catch the two forms being swapped between arms. So the
> expected outcome here is the FOUR exact strings above, not a count of two.

## 3. BRANCH (ii) -- WHAT IS BYTE-UNCHANGED: THREE STATES, AND THE COO FOUND ITS OWN HALF INCOMPLETE

Branches 1, 2 and 5 are untouched: `:684-685` (no posture), `:687-693` (READ_FAILED), `:718` (SERVED
non-absent). **A name in any of those three is byte-identical in the export before and after tt-2.**

**The COO half's ORIGINAL branch (ii) read "a name whose page shows a SERVED posture, or whose export already
carried both forms, is byte-unchanged."** Both halves of that were wrong-shaped:
- *"a SERVED posture"* is too wide -- SERVED+absent (branch 4) **does** change.
- *"already carried both forms"* is **vacuous at base**: the base code emitted one form in every absence
  branch, so no export could already carry both.

`2.0.0_SA_COO~Z` re-read its own half against the landed rule and amended it to the three states above
before telling me the rule was readable. **That is the act I made a condition of this signature, and it
caught a real defect in the half rather than ratifying it.** I graded the amendment independently: its line
refs match my own read at HEAD, digit for digit.

## 4. THE FALSIFIERS -- RE-RUN BY ME, NOT ADOPTED

NEVER: *"never trust a producer's self-report or rc=0."* I ran both at HEAD in this worktree.

| falsifier | COO reported | **I measured** |
|---|---|---|
| tt-1 AC1 (local rebuild, 95 pinned folders) | 95 of 95 at `abs_missing` 0 | **`absences missing=0 on 95 of 95; EXPORT-COMPARE OK on 95 of 95; rc=0`**; `OK 95 NOT_OK 0 CAPTURE_FAILED 0`; cases `page=285 rich=285 same=285 missing=0 extra=0` |
| tt-1 AC2 (planted pre-fix controls) | NOT OK on 2 of 2 | **`RKT_LN_Equity: rc=1 ... missing=1 extra=0 NOT OK`; `AMD_US_Equity: rc=1 ... missing=1 extra=0 NOT OK`** |

**AC2 is the one that matters**, and it is a control on the INSTRUMENT, not the product: it proves the OK
predicate consults `absDiff.missing`, because two exports that differ from their pages by exactly one absence
are refused. **At base that same predicate read OK on both.** Without it, fixing the export would have left a
verdict structurally unable to see the clause it certifies.

## 5. WRITERS OF THE NAMED PROPERTY -- N IS PRINTED

**N = 1.** The `/print?format=rich` body has one writer, `render_pack.build_rich_text`, which is the sole
caller of `_posture_markdown` on this path. One writer, so one rule read. Adopted from the COO half and
checked against the call site.

## 6. BLAST RADIUS AND ROLLBACK -- ADOPTED, WITH THE ROLLBACK RE-STATED AS A COPY

| act | may touch | rollback |
|---|---|---|
| A. one artifact write `research/opal-amgt-scoped-api.zip` in `opal-313476888478-lambda-artifacts` | that one object | the prior VersionId, **re-read by the lane at build time and recorded in the change entry**; a re-point is a COPY, never a delete |
| B. one `safe-apply` moving only `opal-amgt-scoped-api`'s code | every route of `/api/scoped/amgt/*` (a wildcard) | re-apply at the recorded prior VersionId; never a delete |

`/print` **pdf: UNCHANGED** -- `_posture_markdown` is on the rich path only. Every other route: no change.
**A VersionId recorded at signing would be stale by the apply**, which is why the entry records the one read
at build time; I am not pinning a literal here.

## 7. STOP LIMBS -- the COO's five, plus two of mine

The lane STOPS on any of the COO half's five limbs (closure diff reaching an unnamed route; `build_pack`
changed; the pdf branch of `scoped_amgt.py` touched; a function beyond tt-1's posture path changed; the served
`/print` pdf output moving against a pre-apply capture). **I add two:**

6. **THE FOUR STRINGS, NOT THE COUNT.** If the post-apply served export for a branch-3 or branch-4 name
   carries two absence lines that are not byte-identical to the four strings in section 2 -- in particular if
   the tail or the disclaimer appears on the wrong arm -- **STOP**. Two lines is not the outcome; those two
   lines are.
7. **NO SILENT WIDENING TO BRANCHES 1, 2 OR 5.** If any name whose posture is falsy, `READ_FAILED`, or
   `SERVED` non-absent differs by a single byte in its posture section after the apply, **STOP** -- that is
   branch (ii) failing, and it is the branch nobody is watching because it is supposed to be boring.

## 8. WHAT THIS HALF DOES NOT COVER -- stated, not implied

- **The served "after" is a PREDICTION licensed by the rule, not a measurement.** I measured the LOCAL
  rebuild at 95 of 95. The served surface still reads round 44's `86 of 95 at 1`. `86 -> 0` **on the served
  plane** is tt-2 AC2's to measure; this half says what the rule requires it to be and covers the other
  branch if it is not.
- **AC2's instrument is not in the record.** `exportCompare.harness.cjs`'s predicate change sits on local
  portal DEV `4e29386e`, **unpublished**, with the parent gitlink at `1e02be40`. I reproduced AC2 only because
  this worktree carries those bytes; **a seat at the gitlink cannot reproduce it.** The harness is not
  deployed, so it is outside the blast radius -- but the falsifier's reproducibility is bounded by an
  unpublished branch and that is a real limit on this evidence, not a footnote.
- **I did not sweep the shared page header for other sections with the same two-surface exposure.** I checked
  `_management_markdown` (`:548-575`): `management` reaches ONE surface (`ExecManagementTab.tsx`) by the
  code's own cited measurement, so the shape cannot arise there. **Posture-only; the header was not
  enumerated.** Whether any other section is duplicated into `PostureHeaderLine`'s neighbours is an open
  question this half does not answer and does not need to.
- The build pip-downloads pinned wheels from PyPI (declared in the COO half). No peers batch; no other served
  write.

## 9. SIGNATURE

**SIGNED, `1.0.0_SA_CTO~Z`, against `_posture_markdown` as it stands at HEAD after `00ffce7fbf`.** Both
branches are named from the landed rule, both falsifiers were re-run by this seat, and the bounds in section 8
travel with the signature. If the rule moves before the apply, **this signature does not travel with it** --
re-read and re-sign.
