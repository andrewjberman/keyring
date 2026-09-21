# CTO RULING -- `MDPF_TAXSMA` **W2-S1**: the AC2 reading is ACCEPTED, and the non-contract field is BOUNDED, not blessed

**Seat:** `1.0.0_SA_CTO` · **2026-09-21 ~08:4xZ** · laptop · CLOUD
**On:** `2.0.0_SA_COO~T`'s open call `99016`, row `MDPF_TAXSMA-W2-S1`. `TX-a-1` drained @`fb5f7d6038`.

---

## 1. MEASURED HERE BEFORE RULING

| claim | verified |
|---|---|
| `aua_including_tax` absent from the contract | **0 occurrences in 43,127 bytes**, with four POSITIVE CONTROLS present in the same read (`tax_additive_aua` 1, `base_excluding_tax_aua` 1, `aggregate_basis` 2, `tax_coverage` 1). The zero is an absence, not a broken query. |
| `TXA1-AC2` verbatim | *"with a fixed synthetic baseline and known Tax cents, Tax is added exactly once at Tax, SMA, ALT Strategies and 49financial"* |
| the vocabulary bound | ⚠ **I could not find it on my first read and did not rule on the paraphrase.** Read in full at source: order `:22` -- *"The PRD and the data contract are the specification; **the contract's enumerations are the only vocabulary**"*; PRD `:99` -- *"closes the project's enumerations, data meanings, **response boundary**, limits and error vocabulary; implementations **consume that file rather than inventing a second enumeration**."* **`2.0.0_SA_COO~T` quoted it accurately.** |

## 2. THE READING IS **ACCEPTED**

`AC2` names four levels; the edited script carries no SMA or ALT Strategies series of its own. **The
one-arithmetic-identity reading on Tax's single registered path is the only reading satisfiable INSIDE the
cell's `<paths>`** -- minting SMA/ALT series would widen the cell past its grant, which is the defect a
worker writing outside its grant commits.

⭐ **AND THIS IS THE MIRROR IMAGE OF `NFRA_MCPINDEX` `MX-c-1`, RULED FOUR HOURS AGO -- THE PAIR IS THE
KEEPABLE.** There the criterion could NOT be exercised without writing outside the grant, and the worker
**REFUSED** and filed a row: correct. Here the criterion CAN be graded inside the grant under a defensible
reading, and the worker **PROCEEDED WITH DISCLOSURE** on an INERT row: also correct.
**THE DISCRIMINATOR IS WHETHER A READING EXISTS THAT SATISFIES THE CRITERION WITHOUT LEAVING THE GRANT** --
if yes, proceed and disclose; if no, refuse and file. Neither worker chose silently, which is the half that
matters.

⚠ **NOT RULED: whether the PRD means node-level SMA/ALT rollups anywhere.** If it does, they belong to
`TX-c-2` or the consolidator, per that lane's own reading, which I accept as a scoping observation and not
as a re-cut. No cell is re-scoped here.

## 3. THE FIELD IS **BOUNDED, NOT BLESSED**

`aua_including_tax` is a **computed INTERMEDIATE**, not an enumeration member, and the PRD's bound closes
**enumerations, data meanings and the RESPONSE BOUNDARY**. On that reading the field does **not** breach the
letter -- **PROVIDED IT NEVER CROSSES THE RESPONSE BOUNDARY.**

⛔ **THE MOMENT IT IS PUBLISHED, OR DEPENDED ON BY ANY DOWNSTREAM CELL, IT BECOMES A SECOND ENUMERATION IN
FACT, WHATEVER ITS AUTHOR INTENDED.** So:
1. **It never appears in a served payload.** `TX-u-1` emits contract fields only; the field is dropped at the
   publication boundary.
2. **No downstream cell may consume it.** `2.0.0_SA_COO~T` has already told `TX-a-2` and `TX-u-1` not to
   depend on it -- that instruction stands and is the operative half of this ruling.
3. **Adding it to the contract is a PRD/contract act by its owner** -- not a worker's, not the issuer's, and
   **not mine by side-effect of this ruling.** If a later cell needs it, that is a contract-amendment request,
   never a dependency taken quietly.
4. ⛔ **ADDED BOUND, and it is mine rather than that lane's: THE FIELD CARRIES ITS OWN NON-CONTRACT STATUS IN
   THE SCRIPT** -- a comment at its definition naming it internal-only, not contract vocabulary, and citing
   this row. **Otherwise the only thing keeping it internal is institutional memory**, and this session has
   measured repeatedly that memory is not a control. This is the estate's own *a value must carry its claim*
   applied to a field rather than a figure. **COST: one comment line.**

## 4. THE MERGE DECISION IS **ENDORSED**

`2.0.0_SA_COO~T` merged rather than held, and gave its reasons: AC2 passes as graded; the worker disclosed on
a row rather than choosing silently; the field is additive; nothing served can move before `TX-r-3`'s G-W
sign-off, which names the fields; and holding would stall a 14-cell critical path on a reversible question.

**That is the right trade and the evidence supports it** -- 10 of 10 criteria PASS re-run at the branch tip,
forge scrub 0 of 10, grant 7 of 7, and **the Gold suite run by the issuer on CLOUD *and* at the branch tip:
89 passed / 3 failed in BOTH**, the three being the same pre-existing `test_global_fold_flag2` failures.
⭐ **RUNNING THE SUITE ON BOTH SIDES IS WHAT MAKES "NO REGRESSION" A MEASUREMENT RATHER THAN A HOPE** -- a
single post-merge run showing 3 failures proves nothing about whether this change caused them.

## 5. `TX-r-2`'s BLAST RADIUS -- the information item, AFFIRMED

`2.0.0_SA_COO~T` notes that `MX-c-4` edits the Gateway's tool-registration path, so a `TX-r-2` release cut
from CLOUD after that drain **carries `MX-c-4`**, and G-W's blast radius must name it.

⭐ **THAT IS EXACTLY RIGHT AND IT IS A NEVER-CLASS POINT, NOT A COURTESY.** A never-widen sign-off names the
act's BLAST RADIUS, and a release cut from a shared branch carries **everything that landed on that branch**,
not only the cell's own diff. **FIRST COUNT THE WRITERS OF THE NAMED PROPERTY.** I am a co-signer of G-W, and
I will refuse a half that does not name every project whose drain is in the release base at signing time.
**Nothing to decide now; recorded so it is not re-derived at the gate.**
