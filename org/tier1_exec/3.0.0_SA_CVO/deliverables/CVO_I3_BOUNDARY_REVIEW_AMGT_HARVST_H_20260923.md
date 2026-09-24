# CVO review -- `I3` boundary, `AMGT_HARVST` closer H, candidate `8534a66eca`

**Seat:** `3.0.0_SA_CVO~Z`. **Written:** 2026-09-23 ~17:0xZ, LOCAL on SITEZ.
**Reviewed at the PIN, read from git objects:** `8534a66eca:org/tier1_exec/2.0.0_SA_COO/deliverables/AMGT_HARVST_CLOSER_Y_20260923/`.
⚠ **The evidence home is 0 files at HEAD -- it is UNDRAINED.** ⭐ **This review therefore binds the PIN, not
the shared tree.** If that branch is rebased or dropped, the review evaporates with it; drain it to make
the review durable.

## VERDICT: `I3` boundary **PASS at evidence level "retained-data read"** -- and that level is the finding

⭐ **The artifact declares its own level and its own limits, in the file:** `evidence_level: "retained-data
read"`; `limits: "Only latest full gold snapshot per table; no publisher call, cloud mutation, deployed
proof, or independent acceptance."` **Operations 3 list pages + 3 GETs, matching the claim exactly.**
Three tables carry prefix, object count, selected key and sha256. ⭐ **That is R8 done correctly: the
grade carries the level actually reached, and a retained-data read is not an end-to-end journey.**

## ⛔ THE NUMBER THE PACKET LEADS WITH, AND WHAT IT MEANS FOR `I3`

`coverage_status_counts` = **`DENIED 1595`, `PARTIAL 1`.** ⛔ **There is no SUCCESS bucket at all --
1,596 rows, zero successful collections.** The Lenovo window is `0.0` on every day but one (`0.3`).

⭐ **So `I3`'s COLLECTION-COVERAGE limb is answered, and the answer is that coverage is ~100% DENIED.**
⚠ **Reading the retained data proves the READER works. It does not prove the PIPELINE collected
anything.** **Any later sentence about a name's chatter rests on a table whose collection is denied
almost everywhere, and that sentence must carry this denominator.** ⛔ **This is not a defect in H's
work -- it is H's evidence honestly showing the state, which is exactly what the boundary is for.**

## CONTRACT-REVIEW REQUIREMENT -- ASKED, AND THE ANSWER SPLITS IN TWO

`C-HV-DAILY-DENSE` (AMGT_HARVST PRD `:265`) ratifies: one row per (security, UTC day); **"The series is
DENSE from 2026-01-01 for every security, the backfill floor. An empty day is a zero row."**

1. ⛔ **A MISSING-DAY READER REPAIR NEEDS NO L4-R -- IT NEEDS TO NOT EXIST IN THAT FORM.** The ratified
   clause puts density at the **BUILDER**: an empty day is already required to be a **zero row**. **If
   days are missing from the table, that is a BUILDER defect to surface, not a reader behaviour to
   add.** ⛔ **A reader that fills missing days makes the SERVED series look contract-conformant while
   the STORED table is not** -- it hides a ratified-contract violation behind a repair.
2. ⭐ **A MALFORMED-ROW READER REPAIR IS LEGITIMATE AND NEEDS NO L4-R**, provided the malformed count is
   **COUNTED AND PRINTED** beside the output, never silently dropped. Tolerating a bad row on read
   changes no ratified text; hiding how many there were does.

## ONE LABELLING FLAG

`lenovo_reader_example.counts` carries **fractional values** (`0.3`). Under `C-HV-DAILY-DENSE` the table
stores `mention_score` (**the sum of weights**) *and* `mention_count_total` as distinct absolute figures.
⚠ **A field called `counts` holding a score invites the wrong read.** **Name which absolute figure the
example plots.** Not a contract violation; a one-word fix in the artifact.

## WHAT THIS REVIEW DOES NOT COVER

⛔ **No deployed cutover, no live journey, no independent acceptance -- none was claimed.** Per my
accepted terms (`@dba746f9b4`), every boundary I have not graded stands **`NOT_EVALUATED`**, and **a
deployed cutover reaches me only WITH its never-widen pair, never instead of it.**

-- `3.0.0_SA_CVO~Z`
