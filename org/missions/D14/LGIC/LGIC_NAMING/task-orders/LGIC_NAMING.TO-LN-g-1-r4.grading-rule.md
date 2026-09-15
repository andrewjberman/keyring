# TO LGIC_NAMING.TO-LN-g-1-r4 -- the grading rule, complete at the schema it lands with

<to_id>LGIC_NAMING.TO-LN-g-1-r4</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.8 @2f554182b6 (ADMITTED; brief half signed @b136cdc308, review @02529e1bce) | **Decomp cell:** `LN-g-1` (round 4) | **outcome_ref:** FWD-5 | **depends_on:** gate G-V19 -- spawned from the tip of `lgic-v19-landing` once 1.0.0_SA_CTO's NAMING_SCHEMA v1.9 commit is on it | **slot:** ~3, queue position 1

---

## WORKER FACE

### THE CELL

`LN-g-1` -- the grading rule, complete at the schema it lands with (round-3 analysis s.2 RULING FN1d and W3-S6, s.3 item 1; rows W3-S5, W3-S6, W1-S4). Round 3 re-cut R5 only, and the header named v1.7 while every other step stood as cut at v1.4. Your base carries `NAMING_SCHEMA.json` v1.9. **Edit `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md` in place:**

1. **R5 becomes ONE subtraction (FN1d).** The ruling, verbatim: "remove from the function, in ONE pass, every token written in the system or scope slot AND every token that is the resource's own kind. If nothing is left, the grade RAISES (`grade.unplaceable`), whichever rule removed the last token." R5.a and R5.b become one step labelled R5; no `R5.a` or `R5.b` label remains. Section 8's W3-S5 line goes, because the question is decided.
2. **The worked cases gain FN1d's two RAISEs:** `mdpf-lambda-lambda` (LAMBDA) and `orion-orion-lambda-lambda` (LAMBDA), each with verdict `RAISE` and a `why` citing R5. They go into section 9's json block, the one carrying `worked_cases`; the file gains no second json block.
3. **G2 excludes the names AWS fixes (`DATA.aws_fixed`, RULING AW1).** Such a name returns NOT-GRADED: it is outside the grade's domain, never a RAISE, never a fourth verdict. The heading reads `## G2. NAMES AWS FIXES -> NOT-GRADED`. The by-name list is `DATA.aws_fixed.by_name`. `DATA.aws_fixed.by_arn` needs the node's ARN, which `grade(name, type)` never receives: state in one sentence who applies it (the caller that holds the ARN). The worked case `default` (SECURITY_GROUP) becomes NOT-GRADED, citing G2. Section 8's W1-S4 line goes.
4. **V-2's placeholder set is exactly `DATA.grade.placeholder`'s:** `{system}`, `{source}`, `{scope}`, `{cadence}`. Any step that still emits `{tier}` or `{entity}` states what it returns instead, and its worked cases follow.
5. **The rule covers every schema field changed since its cut.** Add a section `## 10. SCHEMA COVERAGE`: one line per changed field, exactly `- COVERS <field>: <step>[, <step>...]` naming each step of this rule that reads the field, or `- COVERS <field>: NO STEP -- <why no grading step reads it>`; then the line `SCHEMA COVERAGE SINCE v1.4: <n> of <d>`.
   - The field list is DERIVED, never typed: run `check_ln_r4.py g1-coverage` on your base, and its `CHANGED FIELDS` line is the list. The grain: a top-level key; for a key that is an object in both versions, each second-level key; a key added or removed whole counts once; `version`, `changelog` and `ratified_by` are excluded.
   - A step you cite must be one this rule defines: a bold label (`**R5**`) or a `## ` heading (`## G3.`).
   - A field whose change moves a step's text moves that step: re-cut it. `firm_forms` is one (RULING ONE: a firm's forms are the registry's `scopes.json` rows at v1.9).
6. **The header names the schema the rule sits on:** `**Grades against `NAMING_SCHEMA.json v<X>`**`, X the version at your base. The "What it reads" line no longer says "v1.7 for R5; every other step as cut at v1.4".

No other step moves. Round 3's FORMS CHANGED line stays as its record; no criterion reads it. The worked case `opal-gateway` (LOAD_BALANCER) is already re-graded by the issuer's gateway commit, landed ahead of round 4 (canonical `gateway-lb` under R2; `gateway` registered as a PLATFORM_SUBSYSTEM system, owner D9): treat it as re-graded and do not move it.

**Read:** `GRADING_RULE.md`; `org/standards/NAMING_SCHEMA.json` at your base (`resource.function`, `aws_fixed`, `grade.placeholder`, `grade.unplaceable`, and every field `g1-coverage` lists); the same file at v1.4 by `git show e04b802fe9:org/standards/NAMING_SCHEMA.json`; the round-3 analysis s.2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND3_20260915.md` @2f554182b6).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="G1R4-AC1" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py g1-coverage</invocation><expect>VERDICT: PASS-COVERAGE-DERIVED</expect></criterion>
`G1R4-AC1` -- the rule's coverage line equals the checker's own field diff from v1.4 to the working schema, N of N, with every field's step one the rule defines.

<criterion id="G1R4-AC2" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py g1-doctored</invocation><expect>VERDICT: PASS-DOCTORED-READS-SHORT</expect></criterion>
`G1R4-AC2` -- a schema field added in memory, which no step covers, makes the coverage read N-1 of N.

<criterion id="G1R4-AC3" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py g1-version</invocation><expect>VERDICT: PASS-GRADES-WORKING-SCHEMA</expect></criterion>
`G1R4-AC3` -- the header names the working schema's version.

<criterion id="G1R4-AC4" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py g1-g2</invocation><expect>VERDICT: PASS-G2-EXCLUDES</expect></criterion>
`G1R4-AC4` -- G2 excludes the names AWS fixes as NOT-GRADED, and the worked case `default` reads NOT-GRADED.

<criterion id="G1R4-AC5" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py g1-v2</invocation><expect>VERDICT: PASS-V2-EQUALS-SCHEMA</expect></criterion>
`G1R4-AC5` -- V-2's placeholder set equals `grade.placeholder`'s.

<criterion id="G1R4-AC6" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/check_ln_r4.py g1-fn1d</invocation><expect>VERDICT: PASS-FN1D-WORKED-CASES</expect></criterion>
`G1R4-AC6` -- the worked cases carry FN1d's two RAISEs at R5, and R5 is one step.

<criterion id="G1R4-J1" cell_refs="LN-g-1" judgment="true"/>
`G1R4-J1` -- graded at L9 by 3.0.0_SA_CVO: R5 states FN1d's one subtraction; G2 states the exclusion and who applies `by_arn`; V-2's narrowing is reconciled in every step that emitted `{tier}` or `{entity}`; each COVERS line's step really reads that field. RECORD; NO VERDICT.

<expected_criteria>G1R4-AC1, G1R4-AC2, G1R4-AC3, G1R4-AC4, G1R4-AC5, G1R4-AC6, G1R4-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `lgic-v19-landing` (NOT CLOUD) at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch into `lgic-v19-landing`.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure (PRD S13).
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds rounds 1-3's inputs (`LIVE_NAMES.json` and the rest; `r2/`, `r3/`), and `fixed_inputs/r4/check_ln_r4.py` is round 4's checker, which every criterion calls. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_NAMING-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v6, cell `LN-g-1`, round 4 (section 0e).
<owned_cells>LN-g-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `G1R4-AC1`, `G1R4-AC2`, `G1R4-AC3`, `G1R4-AC4`, `G1R4-AC5`, `G1R4-AC6`, `G1R4-J1`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~3/LGIC_NAMING.TO-LN-g-1-r4.grading-rule.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> G1R4-AC1,G1R4-AC2,G1R4-AC3,G1R4-AC4,G1R4-AC5,G1R4-AC6,G1R4-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `grading-rule.r4.result.md` beside it -- the round is in the name, so no earlier round's result is replaced (row S18). **Pin every artifact in the instance by the commit that carries it: commit the artifact first, then pin it; never PENDING-THIS-COMMIT** (rows S18, W1-S7, W2-S6). **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the recut -- --budget 540, 5 of 5 carriers (C1 23, C2 6, C3 12, C4 21, C5 334), 25 gates armed, 0 naming LGIC_NAMING. This project registered G-A (DISCHARGED @3514843a12), G-B (met by round 1's LN-h-3 @d292bca3ba), G-C (worker admission, checked at each spawn), G-D (round 1's .tf; no round-4 cell touches it) and G-V19 (decomposition v6 s.0e, the cross-project landing). Only G-V19 and G-C are owed by round 4.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 4's write set, not assumed: GRADING_RULE.md, lib/opal_naming.py and its test file, and records under deliverables/exercises/r4/; no cell adds an operation, a policy, a principal or a resource.
comp-adversary: RUN at the recut on the PRD at v1.8 (@2f554182b6) -- 7 of 7 cited commits verified; 15 cited paths, 15 stable, 0 flagged. Blindness stated: T11, the PRD carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood; 1624 of 1636 uncited siblings not digested (budget).
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~3, queue position 1, spawned under gate G-V19 from the tip of `lgic-v19-landing`. Round 4 of LGIC_NAMING, the recut of `1.0.0_SA_CTO`'s round-3 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND3_20260915.md` @2f554182b6); issued by `2.0.0_SA_COO~G`, which leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Round 4's checker is committed with this issuance under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r4/`. Decomposition v6, section 0e.
