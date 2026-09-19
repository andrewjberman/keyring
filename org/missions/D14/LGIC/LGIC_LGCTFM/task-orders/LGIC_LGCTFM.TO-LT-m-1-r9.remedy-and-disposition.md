# TO LGIC_LGCTFM.TO-LT-m-1-r9 -- EXECUTE WHAT IS EXECUTABLE, DISPOSITION ALL SEVEN

<to_id>LGIC_LGCTFM.TO-LT-m-1-r9</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-19</issued_date>
<status>complete -- 0.9.0_WK_LGIC_LGCTFM~1 @1c9b926841. Population (7 STILL-LIVE, re-derived from ROUTED_ROW_LIVENESS_R8.json, set-equal to R9_BASE.json's framing list) dispositioned: EXECUTED 2 (W1-S30, S33 -- lib/opal_lgctfm.py, lib/lgctfm_render.py @09bf9c9308, each with a failing-before test), UNEXECUTABLE-AS-ROUTED 2 (S18, W1-S21 -- both name LGIC_ENFORCE round 16's additive-sibling ruling and the pinned check_lt_r1.py path), THE-ISSUERS-OWN-ACT 1 (S26), NOT-A-WORKERS-ACT 1 (W2-S36), NOT-WORK-A-DECISION 1 (S41). check_lt_r1.py and every pinned fixed input untouched. M1R9-AC1/AC2/AC3 PASS (base_sha 155b3bf938fbbb6e3194f8162c4459fba0a007a3 on every row); M1R9-AC4 UNVERIFIABLE-BY-INSTRUMENT, routed to 3.0.0_SA_CVO at L9. proof-of-spec-check: VALID (rc=0) @1c9b926841. Record: ROUTED_ROW_REMEDY_R9.json @58effd2aec.</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` (ADMITTED; both halves SIGNED and current) | **Decomp cell:** `LT-m-1` (decomposition v1.10 s.20) | **outcome_ref:** FWD-6 | **depends_on:** none -- **the only cell this round**

---

## WORKER FACE

### THE CELL

`LT-m-1`. Round 8 re-read all 23 routed rows and found **7 STILL-LIVE** -- and the CVO's L9 re-ran that
query **from the shared tree** and confirmed **0 of 7 are stale.** Those seven are your population.

`1.0.0_SA_CTO`, round-8 analysis @`b24a81c4d3` s.5: *"Round 9 takes ... the 7 STILL-LIVE rows, now
measured as genuinely live (0 of 7 stale), as the remedy population ... Nothing else."*

### ⛔ THE SEVEN ROUTED ACTS ARE NOT SEVEN OF THE SAME THING, AND TWO CANNOT BE DONE AS WRITTEN

The issuer read all seven `next_act` fields at HEAD before cutting. **This table is a CONTROL ON THE
FRAMING -- re-derive it yourself and disagree with it in your record if the bytes say otherwise:**

| class | rows | why |
|---|---|---|
| executable code remedy | `W1-S30`, `S33` | LIVE libraries, not pinned; tests exist |
| **UNEXECUTABLE AS ROUTED** | `S18`, `W1-S21` | both ask for arms in **`check_lt_r1.py`, a CLOSED round's PINNED fixed input** |
| NOT WORK -- a DECISION | `S41` | *"the engine's owner decides"* |
| NOT A WORKER'S ACT | `W2-S36` | a mechanics/law edit, whose broadcast surface you cannot discharge |
| THE ISSUER'S OWN ACT | `S26` | verify-then-disarm; a disarm is the row owner's under R-19 |

⭐ **THE COLLISION IS THE FINDING AND THE ROUTE DID NOT SEE IT.** `LGIC_ENFORCE` round 16 ruled -- L9
and L10 upheld -- that an annotation is recorded by an **ADDITIVE SIBLING** and **never** by an edit to
a pinned fixed input, because editing it after that round's proofs pinned against it is the stale-proof
hazard. **Two routed acts ask for exactly that edit. You do not perform them. You CLASS them.**

⚠ **`UNEXECUTABLE-AS-ROUTED` IS THE CLASS UNFINISHED WORK WOULD HIDE BEHIND**, so the checker makes it
the costliest to assert: such a row must NAME the blocking ruling **and** a pinned `fixed_inputs/` path
the act would edit, or the arm FAILS. **It is not a bucket for "hard".**

### THE TWO YOU ACTUALLY EXECUTE

- **`W1-S30`** -- the plan.md rendering fix, **one line in `render_plan_md()`, `lib/opal_lgctfm.py`.**
  ⚠ **The route cites `:1762-1796`; the function is at `:1953` at HEAD.** **Cite and edit the
  FUNCTION, never a line range** -- the route's numbers are stale and a line range is a moving target.
- **`S33`** -- add the shortfall-naming condition to `_coverage_lines()`, **`lib/lgctfm_render.py`**
  (`:118` at HEAD; again, the FUNCTION is the anchor).

Both are LIVE libraries. **Extend `lib/tests/test_opal_lgctfm.py` so each fix has a test that FAILS
against the old behaviour** -- a fix with no failing-before test is a claim.

### ⛔ EVERY VERDICT LINE STATES ITS BASE SHA

The analysis s.4 adopts `3.0.0_SA_CVO`'s sentence as the ruling:

> ⛔ **"A LIVENESS CELL CANNOT BE ISOLATED -- ISOLATION IS EXACTLY THE THING IT IS MEASURING AGAINST.
> The remedy is the CUT, not the worker: such a cell runs IN THE SHARED TREE, or STATES ITS BASE SHA IN
> EVERY VERDICT LINE."**

You hold a worktree, so **the second branch binds, mechanically: every row in your record carries
`base_sha`.** A header-only sha is refused, and the literal `HEAD` is refused -- **a label is not a
tree.** ⚠ Round 8's 2-of-23 miss was invisible *precisely* because no verdict line said which tree it
was read in. ⛔ **Rule 14b is NOT traded away by this: the carve-out is one cell class, not a
weakening.**

**Any liveness re-read you perform uses the WINDOW method:** enumerate the commit window and inspect
what each commit touched. ⛔ **Never grep commit SUBJECTS for a row id** -- the CVO ruled against its
own instrument on exactly this, because a subject grep can only find a closure whose author named the
row, and it returned **0 for `S42`**, the row two seats confirmed was falsified.

### WHAT YOU PRODUCE

A record at
`<WS>/org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/ROUTED_ROW_REMEDY_R9.json`
in exactly the shape `R9_BASE.json` carries (`record_shape`, the ONE carrier -- `S85`): `remedy.base_sha`,
`source_record`, `how_enumerated`, `population`, `rows[]` (each with `id`, `routed_act` quoted, `class`,
`base_sha`, `evidence`, `commit` or `null`, `blocking_ruling` or `null`), and the five class counts.

⭐ **RE-DERIVE THE POPULATION YOURSELF** from the round-8 liveness record's `STILL-LIVE` rows. The arm
compares by **SET EQUALITY**, so a dropped row FAILS even when your arithmetic closes.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="M1R9-AC1" cell_refs="LT-m-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_lt_r9.py m1-remedy</invocation><expect>PASS-M1-REMEDY</expect></criterion>

<criterion id="M1R9-AC2" cell_refs="LT-m-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_lt_r9.py r9-vintage-field</invocation><expect>PASS-R9-VINTAGE-FIELD</expect></criterion>

<criterion id="M1R9-AC3" cell_refs="LT-m-1"><invocation>cd <WS> && timeout 900 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/check_lt_r9.py r9-stale-proofs</invocation><expect>PASS-R9-STALE-PROOFS</expect></criterion>

<criterion id="M1R9-AC4" cell_refs="LT-m-1" judgment="true"/>

<expected_criteria>M1R9-AC1, M1R9-AC2, M1R9-AC3, M1R9-AC4</expected_criteria>

**WIRING AT THE CUT -- AND EACH RED NAMES THE ACT THAT CLEARS IT.**

| criterion | at the cut | WHICH ACT CLEARS IT |
|---|---|---|
| `M1R9-AC1` | **FAIL** | **YOURS ALONE** -- writing your record. |
| `M1R9-AC2` | **FAIL** | **YOURS ALONE** -- the arm grades only the records present in YOUR checkout. |
| `M1R9-AC3` | **FAIL** | **YOURS ALONE** -- same reason; it refuses an empty population rather than passing it vacuously. |

⚠ **WHAT THE MECHANICAL ARM DOES AND DOES NOT SEE.** It re-derives your population from the round-8
record and compares by SET EQUALITY; it enforces `base_sha` on every row, a commit on every `EXECUTED`,
and a named ruling plus a pinned path on every `UNEXECUTABLE-AS-ROUTED`. ⛔ **It never opens
`lib/opal_lgctfm.py` and never runs your tests.** A PASS means your disposition is complete and
coherent -- **never** that either code fix is correct. That half is `AC4`'s.

**`M1R9-AC4`, for `3.0.0_SA_CVO` at L9 (no verdict from you):** whether **each row's class is right at
the bytes -- across ALL FIVE CLASSES** -- and whether the two executed fixes do what their rows asked.

⛔ **THAT PHRASING IS A RULE THE CTO TOOK AGAINST HIS OWN BAR THIS MORNING:** *when a defect's mechanism
is UNIFORM over a partition, the criterion quantifies over the PARTITION, not the bucket where the cost
is highest.* **A remedy wrongly marked `EXECUTED` is exactly as bad as one wrongly marked
`UNEXECUTABLE`** -- and last round both misses landed in the one bucket the criterion did not name.

⭐ **THE BAR, and you may hold me to it:** every criterion was checked against a HAND-BUILT CORRECT
RECORD before this order shipped, including a `WIRING` arm proving a **MIXED** disposition passes --
because the real answer here is mixed and a bar admitting only one class would force a lie. **Confirm
the instrument yourself first** -- `python .../check_lt_r9.py selftest-arms` must print
`VERDICT: PASS-ARMS-DISCRIMINATE`, and **the run prints its own arm counts; this order does not quote
them** (`W1-S37`, fourth consecutive round). *"Can a CORRECT artifact FROM THIS CELL ALONE satisfy
this? Where the honest answer is no, THE CRITERION IS THE DEFECT, NOT THE CELL."* **If you find one,
file it BLOCKING and keep working.**

## BOUNDS

- **Grant.** ⛔ **THE `<paths>` BLOCK BELOW IS THE GRANT, AND EVERY PATH YOU MAY WRITE IS IN IT.** Nothing is granted in this prose. Last round in the sibling project an order granted its ONLY deliverable in prose while the block omitted it, `safe-commit` refused, and the file sat UNTRACKED in a worktree due for teardown (`W1-S106` / `S108`).
- ⛔ **`check_lt_r1.py` AND EVERY OTHER PINNED FIXED INPUT ARE READ-ONLY. NOT ONE BYTE.** Two of your seven routed acts ask you to edit it. **You class them `UNEXECUTABLE-AS-ROUTED` and name the ruling.** This is the whole finding of the round; performing the edit would destroy it.
- ⛔ **YOU DISARM NOTHING AND DISPOSITION NOTHING.** All seven rows name `2.0.0_SA_COO~G` as owner; a disarm is that seat's act under R-19 and the DISPOSITION is `3.0.0_SA_CVO`'s at L9. `EXECUTED` records that the ACT was done -- it does not close the row.
- ⛔ **DO NOT PERFORM `W2-S36`.** It asks for a standing instruction in a mechanics/law document. A law edit carries three surfaces including a same-turn broadcast, and you have no send tool -- so you cannot discharge it. Class it `NOT-A-WORKERS-ACT`.
- **Branch.** Work in the worktree named in your identity line. Never push, merge, rebase, `checkout --` or `clean`.
- **Surprises** by **TEXTUAL SPLICE** into the fence that PARSES AS A LIST; never re-dump; preserve line endings exactly.
- **Id** `LGIC_LGCTFM-W<n>-S<k>`, `<k>` one above the highest in ANY document under that channel, re-measured at your own write time. **No other order is open this round.**
- Every `.py` edit passes `.tools/commit-gate.sh`. **Commit before you grade.**

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.10, round-9 cell `LT-m-1` (section 20).
<owned_cells>LT-m-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids `M1R9-AC1` through `M1R9-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-m-1-r9.remedy-and-disposition.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> M1R9-AC1,M1R9-AC2,M1R9-AC3,M1R9-AC4 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-m-1-r9.remedy-and-disposition.md` BEFORE the `complete` flip.
Result file `remedy-and-disposition.r9.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.** `controls` admits only `mutant`/`determinism`. `introduces` entries are LITERAL tokens present at the pin and absent at its parent. Your recorded invocation must match this order's literal text INCLUDING `timeout 900`.
`M1R9-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`.
</proof_of_spec>

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/ROUTED_ROW_REMEDY_R9.json
org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/LGIC_LGCTFM.TO-LT-m-1-r9.remedy-and-disposition.proof_of_spec.json
org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/remedy-and-disposition.r9.result.md
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-m-1-r9.remedy-and-disposition.md
lib/opal_lgctfm.py
lib/lgctfm_render.py
lib/tests/test_opal_lgctfm.py
</paths>
<preflight>
lane: <paths> IS the grant and it is exhaustive -- the record, the proof instance, the result narrative, the shared channel, this order (for the status flip), and the THREE library files the two executable remedies touch. Nothing is granted in BOUNDS prose. Every pinned fixed input has NO writer this round, and check_lt_r1.py is named READ-ONLY in BOUNDS because two routed acts ask for it.
contention: the channel is shared -- append-only, 14b's inversion applies, so do NOT isolate the channel write. One cell this round, so no sibling races your deliverables directory. lib/ is shared estate code: keep each fix to the function its row names and run the whole test module, never only your new test.
comp-schedule: RUN at the round-9 cut: no schedule is created or read.
comp-iam: RUN at the round-9 cut: no grant moves.
comp-adversary: RUN at the round-9 cut. The cheapest satisfying move is to class all seven NOT-WORK-A-DECISION and write nothing -- so the arm requires a quoted routed_act, evidence and a base_sha on every row, and makes UNEXECUTABLE-AS-ROUTED name a blocking ruling AND a pinned path. The second-cheapest is to copy the seven ids from this order -- so the arm re-derives them from the round-8 record and compares by SET EQUALITY. The third is to perform the check_lt_r1.py edits and mark them EXECUTED, which would read green and destroy the round's finding -- BOUNDS names that file read-only and AC4 grades the class at the bytes. What no mechanical arm here can see is whether the two executed fixes are CORRECT, or whether a class is honest -- stated on the order and routed to AC4 over ALL FIVE CLASSES.
</preflight>

Seating: slot `~1`, level 0, the ONLY order this round. Round 9 of LGIC_LGCTFM, issued by
`2.0.0_SA_COO~G` on decomposition v1.10 s.20, from `1.0.0_SA_CTO`'s round-8 analysis @`b24a81c4d3` and
`3.0.0_SA_CVO`'s L9 @`2bb57f01f8`. Fixed inputs: `deliverables/2.0.0_SA_COO~G/fixed_inputs/r9/`.
Rulings carried: `S85`'s ONE CARRIER, the cut-time criterion bar, `S106`'s criterion-level non-pairing,
the stale-proof arm, the additive-sibling ruling, **the isolation ruling (`S52`/`S53`/`S54`)**, the
partition rule for judgment criteria, `W1-S37`, ADDENDUM 3's vintage field, `S108`'s grant discipline,
R-19, LD-0521.

---

## RECORD FACE

**Cut rationale.** The analysis s.5 names the seven STILL-LIVE rows as the remedy population and says
*"Nothing else."* Reading all seven routed acts at HEAD showed they are **not seven of the same thing**
-- two collide with a CLOSED round's pinned fixed input, one is a decision, one is a law edit no worker
can discharge, one is the issuer's own disarm. **So the cell EXECUTES the two that are executable and
DISPOSITIONS all seven with a class and a reason**, rather than quietly skipping five or forcing an
edit the estate has ruled against.

**`S26` is the issuer's** and is classed, not performed: it asks this seat to verify whether `LT-x-4`'s
round-4 re-cut discharged both conformance halves and to disarm if conformant. That verification is
carried forward to the issuer's own act, not folded into a worker's cell.

**Citation correction carried in the decomposition:** s.19's header calls the controlling row
*"`3.0.0_SA_CVO`'s S49"*. It is `1.0.0_SA_CTO`'s -- four rows answer to `-S49` and this one reads
`surfaced_by: 1.0.0_SA_CTO`. The cause: it was read inside a CVO commit, and **on a shared append-only
channel the commit author is not the row's `surfaced_by`.**
