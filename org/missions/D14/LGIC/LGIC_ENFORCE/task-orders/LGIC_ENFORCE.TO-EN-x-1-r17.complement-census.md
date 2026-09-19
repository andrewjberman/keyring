# TO LGIC_ENFORCE.TO-EN-x-1-r17 -- THE CENSUS OVER THE COMPLEMENT: WHAT THE LAST DOMAIN COULD NOT SEE

<to_id>LGIC_ENFORCE.TO-EN-x-1-r17</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete -- 0.9.0_WK_LGIC_ENFORCE~1: X1R17-AC1/AC2/AC3 PASS-by-output (COMPLEMENT_CENSUS_R17.json, complement 14 at pin 50b1aadf90, 0 RETIRED-AND-DISCLOSED + 0 RETIRED-BUT-SILENT + 14 LIVE, NO DRIFT at completion); X1R17-AC4 recorded UNVERIFIABLE-BY-INSTRUMENT for 3.0.0_SA_CVO at L9. Proof at deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-x-1-r17.complement-census.proof_of_spec.json, proof-of-spec-check rc=0 VALID. Commits 16184888d2 (record), d8445bde10 (result + proof), this flip. No surprise row filed -- nothing off-task surfaced.</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `EN-x-1` (decomposition v3.16 s.0q) | **outcome_ref:** FWD-3 | **depends_on:** none -- **the only cell this round**

---

## WORKER FACE

### THE CELL

`EN-x-1`. Round 16 censused the "retired in a record, still runnable from the tree" class and found
three silent instruments. **Its domain was `LGIC_ENFORCE` + `LGIC_LGCTFM`, and eleven checkers of the
identical shape sat outside it.** `1.0.0_SA_CTO`, round-16 analysis @`b24a81c4d3`, against its own cut:

> ⛔ **"I STATED THE GENERALISATION AND UNDER-SCOPED ITS OWN CELL IN THE SAME BREATH."**

> ⭐ **"THE CENSUS RE-CUT OVER THE COMPLEMENT: all `fixed_inputs/` checkers in LGIC, MINUS the ones
> already censused. Expressed that way deliberately -- A FORWARD LIST IS HOW I LOST THE 11 ... and the
> cell RE-DERIVES it rather than inheriting 36."**

You are finishing that census over the part nobody has looked at.

### ⛔ THE DOMAIN IS A SUBTRACTION. THIS ORDER NAMES NO PROJECT, AND NEITHER MAY YOUR RECORD.

**Your domain is `FULL MINUS PRIOR`:**

- **FULL** = every `*.py` under any `fixed_inputs/` in the LGIC tree, enumerated by `git ls-tree` at a
  pin **you** choose and **print**.
- **PRIOR** = the set of paths the round-16 census record **actually carried** --
  `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/RETIRED_BUT_RUNNABLE_R16.json`,
  read at that same pin. **The set it CARRIED, not a number it reported.**
- **Your population is the remainder, and you class EVERY member of it.**

⛔ **THE CHECKER REFUSES A `how_enumerated` THAT NAMES `LGIC_NAMING` OR `LGIC_CANON`.** That is not
pedantry: a forward list of project names is exactly how eleven checkers were lost, and **a fifth
project minted tomorrow is invisible to a list and visible to a subtraction.** The per-entry `project`
field is a RESULT and is expected; the DOMAIN may not be a list of names.

⛔ **AND IT REFUSES A DOMAIN DESCRIBED AS THE RETIRED LIST.** A census whose domain is the set of known
retirements cannot find an unknown one, and it reports a confident number while doing it.

### ⚠ THE NUMBERS IN THE ANALYSIS ARE NOT YOUR POPULATION

The analysis says *"MINUS the 25 already censused"* and names **11** outside the domain. **Neither is
your population.** Measured by the issuer at the cut, and stated here as a CONTROL ON THE FRAMING you
must RE-MEASURE rather than copy:

| | |
|---|---|
| full `fixed_inputs/*.py` in LGIC | **36** |
| entries the round-16 record CARRIED | **23** |
| **the complement** | **13** |
| of which outside round 16's ordered domain | 11 |
| of which inside it and legitimately not carried | **2** |

**The two inside:** `existing_alias.py` is a FIXTURE excluded by that cell's own DECLARED filter, and
`check_lt_r8.py` **did not exist at its pin** (`LGIC_LGCTFM` round 8's issuance minted it -- the FOURTH
vintage effect its L9 found). **Both deltas resolved in that cell's favour; neither is a defect.**
⛔ **A cell told "11" would have silently dropped the two that make the subtraction honest.**
**Re-derive all four numbers at your own write time and print them.**

### WHAT YOU PRODUCE

A record at
`<WS>/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/COMPLEMENT_CENSUS_R17.json`
in exactly the shape `R17_BASE.json` carries (`record_shape`, the ONE carrier -- `S85`):

- `census.pin` -- **the commit you measured at. PRINT IT.**
- `census.how_enumerated` -- the re-derivation **with its invocation**.
- `census.full_denominator_at_pin`, `census.prior_censused`, `census.complement`, `census.prior_source`.
- `census.instruments[]` -- one entry per complement member: `path`, `project`, `retiring_record`
  (or `null`), `instrument_discloses_it`, `class`, `basis`.
- `census.retired_and_disclosed` / `retired_but_silent` / `live` -- the three classes, MECE.
- `census.full_denominator_at_completion` and `census.drift` -- **re-read the denominator when you
  finish and say what moved. Write `NO DRIFT` rather than omitting it.**
- `fixed_inputs_at_pin` and `stale_proofs` per the base.

### ⭐ DRIFT IS DISCLOSED, NEVER REQUIRED TO BE ZERO

Round 16's census was correct **and its denominator grew under it** because a sibling project's
issuance minted a checker mid-cell. **A bar demanding a stable denominator would convict a correct
cell.** The bar is that the completion re-read is PRESENT and its drift STATED. A `WIRING` arm in the
checker proves this: a record whose completion denominator is HIGHER than its pin denominator, with the
drift named, **PASSES**.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="X1R17-AC1" cell_refs="EN-x-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r17/check_en_r17.py x1-census</invocation><expect>PASS-X1-CENSUS</expect></criterion>

<criterion id="X1R17-AC2" cell_refs="EN-x-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r17/check_en_r17.py r17-vintage-field</invocation><expect>PASS-R17-VINTAGE-FIELD</expect></criterion>

<criterion id="X1R17-AC3" cell_refs="EN-x-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r17/check_en_r17.py r17-stale-proofs</invocation><expect>PASS-R17-STALE-PROOFS</expect></criterion>

<criterion id="X1R17-AC4" cell_refs="EN-x-1" judgment="true"/>

<expected_criteria>X1R17-AC1, X1R17-AC2, X1R17-AC3, X1R17-AC4</expected_criteria>

**WIRING AT THE CUT -- AND EACH RED NAMES THE ACT THAT CLEARS IT.**

| criterion | at the cut | WHICH ACT CLEARS IT |
|---|---|---|
| `X1R17-AC1` | **FAIL** | **YOURS ALONE** -- writing your record. |
| `X1R17-AC2` | **FAIL** | **YOURS ALONE** -- the arm grades only the records present in YOUR checkout. |
| `X1R17-AC3` | **FAIL** | **YOURS ALONE** -- same reason; it refuses an empty population rather than passing it vacuously. |

⚠ **WHAT THE MECHANICAL ARM DOES AND DOES NOT SEE.** ⭐ **Unlike round 16's, this arm RE-DERIVES YOUR
POPULATION ITSELF** -- it runs its own `git ls-tree` **at the pin your record states**, reads the
round-16 record at that same pin, and compares to your entries **by SET EQUALITY**. So a silently
dropped member fails **even when your arithmetic closes.** ⚠ **But it still never opens a checker and
never runs one.** A PASS means your population is complete and your record coherent -- **never** that
any `instrument_discloses_it` is true. That half is `AC4`'s.

**`X1R17-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether **each entry's class is right
AT THE BYTES -- across ALL THREE CLASSES.**

⛔ **THAT PHRASING IS DELIBERATE AND IT IS A RULE THE CTO TOOK AGAINST HIS OWN BAR THIS MORNING:** *when
a defect's mechanism is UNIFORM over a partition, the criterion quantifies over the PARTITION, not over
the bucket where the cost is highest.* The expensive bucket here is obviously `RETIRED-BUT-SILENT` -- a
green from a retired detector. **But a misclassification INTO `LIVE` hides a retirement exactly as
well**, and last round both falsified verdicts landed in the one bucket its criterion did not name.
**Naming the expensive bucket feels like prioritising; it is scoping the certificate to where you were
already looking.**

⭐ **THE BAR, and you may hold me to it:** every criterion was checked against a HAND-BUILT CORRECT
RECORD before this order shipped, and one mutant was REPAIRED when it proved vacuous -- the
inherited-denominator arm originally compared against a hard-coded `36`, which cannot fail while the
tree still holds 36, so it now mutates off the live number. **Confirm the instrument yourself first**
-- `python .../check_en_r17.py selftest-arms` must print `VERDICT: PASS-ARMS-DISCRIMINATE`, and **the
run prints its own arm counts; this order does not quote them** (`LGIC_LGCTFM-W1-S37`). *"Can a CORRECT
artifact FROM THIS CELL ALONE satisfy this? Where the honest answer is no, THE CRITERION IS THE DEFECT,
NOT THE CELL."* **Five such criteria have been found in this project's last four rounds, every one by
the cell being graded or by the instrument's own mutant. If you find a sixth, file it BLOCKING and keep
working.**

## BOUNDS

- **Grant.** ⛔ **THE `<paths>` BLOCK BELOW IS THE GRANT, AND EVERY PATH YOU MAY WRITE IS IN IT.** Nothing is granted in this prose. Last round this order's ancestor granted its ONLY deliverable in prose while the block omitted it, `safe-commit` refused the write, and **the file sat UNTRACKED in a worktree due for teardown while its record NAMED the path** (`W1-S106` / `S108`). **A refusal that blocks a write is loud; the orphaned bytes it leaves behind are not.**
- ⛔ **EVERY CHECKER YOU CENSUS IS READ-ONLY. NOT ONE BYTE.** You add no disclosure line to any instrument, in any project. Round 16 ruled that a retirement is recorded by an **ADDITIVE SIBLING** and never by an edit to a pinned fixed input -- and deciding the remedy inside the measuring cell is how a round makes the numbers agree instead of the data.
- ⛔ **`LGIC_NAMING`, `LGIC_CANON` AND `LGIC_LGCTFM` ARE IN YOUR READ SCOPE AND NOT IN YOUR WRITE SCOPE.** You read their `fixed_inputs/`; you write nothing there and file no row on their channels.
- ⛔ **A FIXTURE IS NOT A CHECKER, AND THAT IS A JUDGMENT YOU MUST DECLARE RATHER THAN MAKE SILENTLY.** Some complement members are almost certainly fixtures rather than instruments. **You may not drop one from the population** -- the arm compares by SET EQUALITY and a dropped member FAILS. Class it, and say in its `basis` why it is what it is.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line endings exactly.
- **Id** `LGIC_ENFORCE-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **No other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v3.16, round-17 cell `EN-x-1` (section 0q).
<owned_cells>EN-x-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `X1R17-AC1` through `X1R17-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-x-1-r17.complement-census.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> X1R17-AC1,X1R17-AC2,X1R17-AC3,X1R17-AC4 --governing-order org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-x-1-r17.complement-census.md` BEFORE the `complete` flip.
Result file `complement-census.r17.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent. Your recorded invocation must match this order's literal text INCLUDING `timeout 900`.
`X1R17-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/COMPLEMENT_CENSUS_R17.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-x-1-r17.complement-census.proof_of_spec.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/complement-census.r17.result.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_ENFORCE/task-orders/LGIC_ENFORCE.TO-EN-x-1-r17.complement-census.md
</paths>
<preflight>
lane: <paths> IS the grant and it is exhaustive -- every file this cell writes is named in it, including this order (for the status flip), the record, the proof instance, the result narrative and the shared channel. Nothing is granted in BOUNDS prose. Every pinned fixed input has NO writer this round.
contention: the channel is shared -- append-only, 14b's inversion applies, so do NOT isolate the channel write. One cell this round, so no sibling races your deliverables directory.
comp-schedule: RUN at the round-17 cut: no schedule is created or read.
comp-iam: RUN at the round-17 cut: no grant moves.
comp-adversary: RUN at the round-17 cut. The cheapest satisfying move is to enumerate the complement from the ELEVEN the analysis names, which yields a clean small denominator that silently drops the two in-domain members -- so the arm re-derives the population itself at your stated pin and compares by SET EQUALITY, and a dropped member FAILS even though the arithmetic closes. The second-cheapest is to write the domain as "LGIC_NAMING + LGIC_CANON", which reads correct today and loses the fifth project tomorrow -- so the arm REFUSES a how_enumerated naming either. The third is to hard-code the denominator; the arm re-derives it. What no mechanical arm here can see is whether any instrument_discloses_it is true AT THE BYTES, or whether a LIVE classification hides a retiring record the cell did not look for -- stated on the order and routed to AC4 over ALL THREE CLASSES.
</preflight>

Seating: slot `~1`, level 0, the ONLY order this round. Round 17 of LGIC_ENFORCE, issued by
`2.0.0_SA_COO~G` on decomposition v3.16 s.0q, from `1.0.0_SA_CTO`'s round-16 analysis @`b24a81c4d3` and
`3.0.0_SA_CVO`'s L9 @`4acccf10ad`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r17/`.
Rulings carried: `S85`'s ONE CARRIER, the cut-time criterion bar, `S106`'s criterion-level non-pairing,
the stale-proof arm, the additive-sibling ruling, the partition rule for judgment criteria,
`LGIC_LGCTFM-W1-S37`, ADDENDUM 3's vintage field, `S108`'s grant discipline, LD-0521.

---

## RECORD FACE

**Cut rationale.** The analysis s.4 specifies one cell and says *"Nothing else. Round 16 drained clean
and I am not manufacturing work."* This recut takes that literally: one cell, one worker, no second
lane, and `W2-S13` is RAISED to the CTO rather than folded in.

**What the issuer measured before cutting.** full 36 / prior 23 / complement 13 / 11 outside the
round-16 domain / 2 inside it, with every prior entry confirmed present in the full denominator so the
subtraction leaves no orphans. These are carried as a framing control the cell must re-derive.

**`S108` closes here.** Its remediation was OPEN with this seat at round v16, remedy *"every path
granted anywhere in an order appears IN the `<paths>` block"*. This order's block names all five files
the cell may write, and its BOUNDS grant clause states that nothing is granted in prose.
