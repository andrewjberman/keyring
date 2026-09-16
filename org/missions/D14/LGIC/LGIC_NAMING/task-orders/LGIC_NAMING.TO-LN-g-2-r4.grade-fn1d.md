# TO LGIC_NAMING.TO-LN-g-2-r4 -- grade() implements the rule as written

<to_id>LGIC_NAMING.TO-LN-g-2-r4</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.8 @2f554182b6 (ADMITTED; brief half signed @b136cdc308, review @02529e1bce) | **Decomp cell:** `LN-g-2` (round 4, new at v6) | **outcome_ref:** FWD-5 | **depends_on:** LN-g-1 (TO-LN-g-1-r4) and LGIC_ENFORCE EN-r-3 both merged into `lgic-v19-landing` (gate G-V19); spawned from that branch's tip | **slot:** ~2, queue position 1

---

## WORKER FACE

### THE CELL

`LN-g-2` -- `grade()` in `lib/opal_naming.py` implements `GRADING_RULE.md` as written (round-3 analysis s.2 carrier 4 of FN1d and s.3 item 2; LGIC_ENFORCE round-1 analysis C-S11, a two-way coverage check between the rule and `grade()`). Your base carries the rule as LN-g-1 completed it, `NAMING_SCHEMA.json` v1.9, and LGIC_ENFORCE EN-r-3's one-carrier change to the same module. **Edit `lib/opal_naming.py` and `lib/tests/test_opal_naming.py`:**

1. **FN1d.** Wherever a function slot is built through R5 (`_grade_resource`, and any grammar that reuses it), apply ONE subtraction: drop every function token written in the system or scope slot AND every token that is the resource's own kind (`kind.by_type` for its type). If nothing is left, raise `RaiseDefect` with a message beginning `R5`. Today `grade("mdpf-lambda-lambda", "LAMBDA")` returns CONFORMANT; after the edit it raises.
2. **G2 as the rule now states it.** A name in `NAMING_SCHEMA.json` `aws_fixed.by_name` returns `("NOT-GRADED", None)`, read from the schema at run time, never hand-listed. Remove every G2 `RaiseDefect` the rule no longer states.
3. **V-2 as the rule now states it:** a canonical form carries only the placeholders `grade.placeholder` allows.
4. **The two-way step check (C-S11).** Inside the `grade()` region -- from `class RaiseDefect` to `def _segment(` -- every step the rule defines (a bold label such as `**R5**`, or a heading such as `## G3.`) is cited, as its label, in a comment or a `RaiseDefect` message at the code that implements it; and every step label cited there is one the rule defines. A PRD section is cited as `PRD S10`, never bare `S10`. A rule step with no code is implemented; one that cannot apply to `grade(name, type)` is a BLOCKING surprise row -- the rule is LN-g-1's, merged, and you never edit it.
5. **The Terraform-type map is schema data.** `CENSUS_TF_ATTR` (`lib/opal_naming.py` :1433 at the cut) is read from the field 1.0.0_SA_CTO landed in NAMING_SCHEMA v1.9, and no Terraform-type literal such as `"aws_iam_role"` remains in the module.
6. **Tests.** Add tests for FN1d's two RAISEs, `mdpf-lambda-lambda` and `orion-orion-lambda-lambda` (LAMBDA), with `fn1d` in their names, and for NOT-GRADED aws_fixed names. RULING RED: the suite's failing set may not grow. At 7b5331c8c0 it read 75 passed, 0 failed. If your base is red before any edit, file a BLOCKING row naming the failing tests.
7. **The re-grade record.** Write `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r4/g2-regrade.r4.tsv`: one line per attributed name in round 2's record (`org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n4-firm-patterns.md`, the `attributed` object, 68 names), `<name><TAB><the canonical form grade(name, "IAM_ROLE") returns at your tree>`.

**Read:** `lib/opal_naming.py` (`grade` :1236, `_grade_resource` :958, `_slots` :897, `CENSUS_TF_ATTR` :1433 at the cut); `lib/tests/test_opal_naming.py`; `GRADING_RULE.md` at your base; `org/standards/NAMING_SCHEMA.json` at your base; the round-3 analysis s.2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND3_20260915.md` @2f554182b6).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="G2R4-AC1" cell_refs="LN-g-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py g2-fn1d</invocation><expect>VERDICT: PASS-FN1D-RAISES-IN-CODE</expect></criterion>
`G2R4-AC1` -- `grade()` raises at R5 on both FN1d cases.

<criterion id="G2R4-AC2" cell_refs="LN-g-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py g2-regrade</invocation><expect>VERDICT: PASS-REGRADE-UNCHANGED</expect></criterion>
`G2R4-AC2` -- round 2's 68 attributed forms re-grade, as the record states, with no change beyond a `{system}` fill.

<criterion id="G2R4-AC3" cell_refs="LN-g-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py g2-aws</invocation><expect>VERDICT: PASS-AWS-FIXED-NOT-GRADED</expect></criterion>
`G2R4-AC3` -- every `aws_fixed.by_name` probe returns NOT-GRADED.

<criterion id="G2R4-AC4" cell_refs="LN-g-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py g2-twoway</invocation><expect>VERDICT: PASS-STEPS-TWO-WAY</expect></criterion>
`G2R4-AC4` -- every rule step is cited in the `grade()` region, and every step label cited there is a rule step.

<criterion id="G2R4-AC5" cell_refs="LN-g-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py g2-typemap</invocation><expect>VERDICT: PASS-TYPEMAP-IN-SCHEMA</expect></criterion>
`G2R4-AC5` -- the Terraform-type map is read from the schema, and the module keeps no copy.

<criterion id="G2R4-AC6" cell_refs="LN-g-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py g2-suite</invocation><expect>VERDICT: PASS-SUITE-NO-NEW-FAILURE</expect></criterion>
`G2R4-AC6` -- the suite, which carries the FN1d tests, fails nothing the base did not.

<expected_criteria>G2R4-AC1, G2R4-AC2, G2R4-AC3, G2R4-AC4, G2R4-AC5, G2R4-AC6</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. `GRADING_RULE.md` and `NAMING_SCHEMA.json` are NOT yours. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `lgic-v19-landing` (NOT CLOUD) at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch into `lgic-v19-landing`.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure (PRD S13). Every `.py` you touch passes `.tools/commit-gate.sh` (safe-commit runs it).
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds rounds 1-3's inputs, and `fixed_inputs/r4/check_ln_r4.py` is round 4's checker, which every criterion calls. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_NAMING-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
lib/opal_naming.py
lib/tests/test_opal_naming.py
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r4/g2-regrade.r4.tsv
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v6, cell `LN-g-2`, round 4 (section 0e).
<owned_cells>LN-g-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `G2R4-AC1`, `G2R4-AC2`, `G2R4-AC3`, `G2R4-AC4`, `G2R4-AC5`, `G2R4-AC6`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~2/LGIC_NAMING.TO-LN-g-2-r4.grade-fn1d.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> G2R4-AC1,G2R4-AC2,G2R4-AC3,G2R4-AC4,G2R4-AC5,G2R4-AC6` BEFORE the `complete` flip.
Result file `grade-fn1d.r4.result.md` beside it -- the round is in the name, so no earlier round's result is replaced (row S18). **Pin every artifact in the instance by the commit that carries it: commit the artifact first, then pin it; never PENDING-THIS-COMMIT** (rows S18, W1-S7, W2-S6). **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the recut -- --budget 540, 5 of 5 carriers (C1 23, C2 6, C3 12, C4 21, C5 334), 25 gates armed, 0 naming LGIC_NAMING. This project registered G-A (DISCHARGED @3514843a12), G-B (met by round 1's LN-h-3 @d292bca3ba), G-C (worker admission, checked at each spawn), G-D (round 1's .tf; no round-4 cell touches it) and G-V19 (decomposition v6 s.0e, the cross-project landing). This cell is gated by G-V19 and G-C.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 4's write set, not assumed: GRADING_RULE.md, lib/opal_naming.py and its test file, and records under deliverables/exercises/r4/; no cell adds an operation, a policy, a principal or a resource.
comp-adversary: RUN at the recut on the PRD at v1.8 (@2f554182b6) -- 7 of 7 cited commits verified; 15 cited paths, 15 stable, 0 flagged. Blindness stated: T11, the PRD carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood; 1624 of 1636 uncited siblings not digested (budget).
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). lib/ holds LGIC_ENFORCE's module; within this round its one writer at a time is fixed by G-V19 (EN-r-3 merges first).
</preflight>

Seating: slot ~2, queue position 1, spawned from the tip of `lgic-v19-landing` after LN-g-1 and EN-r-3 are merged into it; not LN-g-1's worker (decomposition v6 s.0e: the two-way check measures that the code implements the rule as written, which a worker who wrote both could make agree by construction). Round 4 of LGIC_NAMING, the recut of `1.0.0_SA_CTO`'s round-3 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND3_20260915.md` @2f554182b6); issued by `2.0.0_SA_COO~G`, which leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Decomposition v6, section 0e.
