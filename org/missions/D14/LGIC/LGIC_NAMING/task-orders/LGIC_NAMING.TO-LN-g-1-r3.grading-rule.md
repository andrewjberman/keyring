# TO LGIC_NAMING.TO-LN-g-1-r3 -- the grading rule, re-cut to v1.7

<to_id>LGIC_NAMING.TO-LN-g-1-r3</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.7 @f0a830c15f (ADMITTED; brief half signed @f0a830c15f, review @cd596cf4a4) | **Decomp cell:** `LN-g-1` (round 3) | **outcome_ref:** FWD-3, FWD-1 | **depends_on:** -- (level 0; spawned at issuance) | **slot:** ~3, queue position 1

---

## WORKER FACE

### THE CELL

`LN-g-1` -- the grading rule, re-cut to NAMING_SCHEMA.json v1.7 (round-2 analysis s.2 RULINGS FN1b and FN1c, s.4 and s.5 item 3; rows C-S14, W4-S2 and W4-S1). Round 1 wrote `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md` at v1.4. v1.7 rules the function slot, and the rule is one of its carriers (analysis s.2, carrier 4). **Edit `GRADING_RULE.md` in place:**

1. **R5 gains FN1b's subtraction.** After R1 and R4 take the system and scope tokens out, every remaining token already written in the system or scope slot is dropped from the function. If that leaves no function token, the grade RAISES (`grade.unplaceable`).
2. **R5 gains the own-kind bar.** The resource's OWN kind (`kind.by_type` for its type) is never written in its function. Another type's kind that names the subject the resource serves stays in the function, as R6 already says; R6 is unchanged.
3. **R5's "free vocabulary" gains its reason:** a grade has no item description, so FN1's word-choice clauses bind the namer only, and the grade keeps a function's words as written and grades the grammar -- slots, spellings and kinds.
4. **R3 states its test as adjacency** to a V4 firm token, never position, in one added sentence (row W4-S1). R3's readings do not change.
5. **The header names `NAMING_SCHEMA.json v1.7`** as the version the rule grades against.
6. **Re-grade every attributed canonical form** in round 2's LN-f-1 record, `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n4-firm-patterns.md`, under the two new steps, and print in `GRADING_RULE.md` one line, exactly `FORMS CHANGED BY THE v1.7 STEPS: <n> of <d>`, with each changed form listed beneath it when `<n>` is not zero. LN-f-1's record is re-graded only if `<n>` is not zero, and that is a later issuance's act, not yours.

No other step moves. The worked cases (section 9) are re-read under the two steps; any whose canonical form changes is corrected and named in your result file.

**Read:** `GRADING_RULE.md`; `org/standards/NAMING_SCHEMA.json` (v1.7) `resource.function` and `kind.by_type`; the round-2 analysis s.2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND2_20260915.md` @02f08322af); `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r2/n4-firm-patterns.md`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="G1T-AC1" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_ln_r3.py g1-count</invocation><expect>VERDICT: PASS-COUNT-RECOMPUTED</expect></criterion>
`G1T-AC1` -- the rule's printed FORMS CHANGED line equals the checker's own recount of the two steps over round 2's attributed forms, numerator and denominator.

<criterion id="G1T-AC2" cell_refs="LN-g-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_ln_r3.py g1-version</invocation><expect>VERDICT: PASS-GRADES-V17</expect></criterion>
`G1T-AC2` -- the rule's header names NAMING_SCHEMA.json v1.7.

<criterion id="G1T-J1" cell_refs="LN-g-1" judgment="true"/>
`G1T-J1` -- graded at L9 by 3.0.0_SA_CVO: R5 states FN1b's subtraction, the own-kind bar and why a function's words are kept; R3 states its test as adjacency, never position; no other step moved. RECORD; NO VERDICT.

<expected_criteria>G1T-AC1, G1T-AC2, G1T-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure (PRD S13). The fixed inputs are one live pull, at one vintage; read them instead of pulling again.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds round 1's (`N3_ITEMS.json` and the rest), `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/` holds round 2's (`N3_KEY_R2.json`, the key, unchanged in round 3), and `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/` holds round 3's (`check_ln_r3.py`, the checker every criterion calls; `blind_seat.py`, the clean-context seat). Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_NAMING-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v5 @2f8cc63b8e, cell `LN-g-1`, round 3 (section 0d).
<owned_cells>LN-g-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `G1T-AC1`, `G1T-AC2`, `G1T-J1`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~3/LGIC_NAMING.TO-LN-g-1-r3.grading-rule.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> G1T-AC1,G1T-AC2,G1T-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `grading-rule.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the recut -- --budget 540, 5 of 5 carriers (C1 276, C2 7, C3 12, C4 21, C5 334), 26 gates armed, none naming LGIC_NAMING. This project registered G-A (DISCHARGED @3514843a12), G-B (LGIC_ENFORCE E9's comparison half; met by round 1's LN-h-3 @d292bca3ba), G-C (worker admission, checked after this issuance) and G-D (the three-writer .tf; round 1's, and no round-3 cell touches the .tf). None is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 3's write set, not assumed: TSV and markdown records under deliverables/exercises/r3/, the seat records beside them, and GRADING_RULE.md; no cell adds an operation, a policy, a principal or a resource, and the seat is a local claude process with no tools, so the lens would receive an empty input.
comp-adversary: RUN at the recut on the PRD at v1.7 (@f0a830c15f) -- 7 of 7 cited commits verified; 14 cited paths, 14 stable, 0 flagged. Blindness stated: T11, the PRD carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~3, queue position 1. Round 3 of LGIC_NAMING, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND2_20260915.md` @02f08322af); issued by `2.0.0_SA_COO~G`, which leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Round 3's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/`. Decomposition v5 @2f8cc63b8e, section 0d.
