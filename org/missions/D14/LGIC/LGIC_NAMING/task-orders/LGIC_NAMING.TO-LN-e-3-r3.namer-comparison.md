# TO LGIC_NAMING.TO-LN-e-3-r3 -- the namers' comparison

<to_id>LGIC_NAMING.TO-LN-e-3-r3</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~6</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.7 @f0a830c15f (ADMITTED; brief half signed @f0a830c15f, review @cd596cf4a4) | **Decomp cell:** `LN-e-3` (round 3) | **outcome_ref:** FWD-1 | **depends_on:** LN-e-1 and LN-e-2, round 3 (both merged before this slot is spawned) | **slot:** ~6, queue position 1

---

## WORKER FACE

### THE CELL

`LN-e-3` -- the namers' comparison, round 3 (PRD candidate N3). **You compare; you do not name.**

Run the two mechanical criteria below and write `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/n3-compare.md`: the checker's output verbatim, then one line per DIFFERS item giving both names, the item's ruled name from the round-1 analysis's s.2 table (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND1_20260914.md` @de52d3db04), and which namer, if either, wrote it. Mark item i05 as disclosed by row LGIC_NAMING-S15 (the registry's `scopes.json` names the bucket). A difference is the outcome's evidence, not a defect to fix.

**Read:** `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/n3-namer-a.tsv`, `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/n3-namer-b.tsv`, the two seat records under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/seats/`, the round-1 analysis's s.2 table.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="E3T-AC1" cell_refs="LN-e-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_ln_r3.py e3-identical</invocation><expect>VERDICT: PASS-IDENTICAL</expect></criterion>
`E3T-AC1` -- the two namers' answer files are identical on every item.

<criterion id="E3T-AC2" cell_refs="LN-e-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_ln_r3.py e3-blind</invocation><expect>VERDICT: PASS-NAMERS-UNCONFERRED</expect></criterion>
`E3T-AC2` -- the two seats received the identical prompt, in two different sessions and folders.

<expected_criteria>E3T-AC1, E3T-AC2</expected_criteria>

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
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/n3-compare.md
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v5 @2f8cc63b8e, cell `LN-e-3`, round 3 (section 0d).
<owned_cells>LN-e-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `E3T-AC1`, `E3T-AC2`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~6/LGIC_NAMING.TO-LN-e-3-r3.namer-comparison.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> E3T-AC1,E3T-AC2` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `namer-comparison.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~6, queue position 1. Round 3 of LGIC_NAMING, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND2_20260915.md` @02f08322af); issued by `2.0.0_SA_COO~G`, which leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Round 3's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/`. Decomposition v5 @2f8cc63b8e, section 0d.
