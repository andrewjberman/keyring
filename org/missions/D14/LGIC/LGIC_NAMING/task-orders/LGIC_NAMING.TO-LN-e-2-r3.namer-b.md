# TO LGIC_NAMING.TO-LN-e-2-r3 -- namer B, in a clean-context seat

<to_id>LGIC_NAMING.TO-LN-e-2-r3</to_id>
<project>LGIC_NAMING</project>
<issued_to>0.9.0_WK_LGIC_NAMING~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_NAMING_PRD.md` v1.7 @f0a830c15f (ADMITTED; brief half signed @f0a830c15f, review @cd596cf4a4) | **Decomp cell:** `LN-e-2` (round 3) | **outcome_ref:** FWD-1 | **depends_on:** -- (level 0; spawned at issuance from the same base as the other namer) | **slot:** ~2, queue position 1

---

## WORKER FACE

### THE CELL

`LN-e-2` -- namer B, round 3 (PRD candidate N3; round-2 analysis s.2 and s.5 item 1). **The namer is a clean-context seat, not you.** Two seats name the same 18 NEW resources from `org/standards/NAMING_SCHEMA.json` (v1.7) and the identity registry's three row files (`infra/logic/registry/scopes.json`, `systems.json` and `tiers.json`) alone, without conferring; the outcome is that they write the identical string for every one. Round 2's namers matched 15 of 18. v1.7 rules the function slot (FN1b: a noun-phrase function drops every token already written in the system or scope slot; FN1c: only the resource's OWN kind is barred from its function), and the registry replaces the seed as the briefing's source of rows.

**Your act is to run namer B's seat and prove it.** `python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/blind_seat.py run e2` builds the prompt from the schema, the three registry files and `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/N3_ITEMS.json` at your base -- the two namers' seats receive the byte-identical prompt, and neither is ever given the other's answer -- runs the seat, and writes `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/n3-namer-b.tsv` (`# base <sha>`, `# seat <session>`, then `<item id><TAB><name>`) and the seat's five files under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/seats/`.

A wrong or RAISE name is the outcome's evidence, not a defect to fix. The one item whose ruled name the briefing carries -- i05, because `scopes.json` names the bucket, as a registry should -- is disclosed in row LGIC_NAMING-S15; do nothing about it.

**Read:** the seat's printed line and the files it wrote. Nothing else is needed.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="E2T-AC1" cell_refs="LN-e-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_ln_r3.py e2-seat</invocation><expect>VERDICT: PASS-CLEAN-SEAT</expect></criterion>
`E2T-AC1` -- the seat record proves a clean seat: outside the workspace, in no repository, empty at launch, no CLAUDE.md up its parent chain, no tools, exit 0, the builder's prompt at the recorded base, and the reply and answer file as the session wrote them.

<criterion id="E2T-AC2" cell_refs="LN-e-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_ln_r3.py e2-canary</invocation><expect>VERDICT: PASS-CANARY-BLIND</expect></criterion>
`E2T-AC2` -- the seat's verbatim reply answers both canary questions and carries neither workspace-only fact.

<criterion id="E2T-AC3" cell_refs="LN-e-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_ln_r3.py e2-named</invocation><expect>VERDICT: PASS-ALL-NAMED</expect></criterion>
`E2T-AC3` -- every one of the 18 items has a name, or RAISE, in the answer file.

<criterion id="E2T-AC4" cell_refs="LN-e-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/check_ln_r3.py e2-v17</invocation><expect>VERDICT: PASS-BRIEFED-ON-V17</expect></criterion>
`E2T-AC4` -- the answer file's base carries NAMING_SCHEMA.json v1.7.

<expected_criteria>E2T-AC1, E2T-AC2, E2T-AC3, E2T-AC4</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_NAMING/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Nothing live moves.** No cell of this project renames a live name, writes to AWS, runs Terraform, or calls anything off Opal infrastructure (PRD S13). The fixed inputs are one live pull, at one vintage; read them instead of pulling again.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds round 1's (`N3_ITEMS.json` and the rest), `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/` holds round 2's (`N3_KEY_R2.json`, the key, unchanged in round 3), and `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/` holds round 3's (`check_ln_r3.py`, the checker every criterion calls; `blind_seat.py`, the clean-context seat). Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_NAMING-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **You operate a seat; you are not the blind party.** From your worktree root, run `python org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/blind_seat.py run e2` ONCE, with a Bash timeout of 600000 ms (the seat's own bound is 540 s). It prints `SEAT: OK ...` or `SEAT: ERROR <reason>`. On ERROR, run it once more; a second ERROR is a BLOCKING row and your final report. Never write or edit the prompt, the reply or the answer file by hand, and never run the seat a third time: the checker re-derives the prompt and re-parses the reply, so a hand edit FAILs the seat criterion.
- **Commit everything the seat wrote** -- the answer file and the five files `org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/seats/e2.*` -- with your proof instance.

<paths>
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/n3-namer-b.tsv
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/seats/e2.seat.json
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/seats/e2.prompt.txt
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/seats/e2.raw.json
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/seats/e2.answer.txt
org/missions/D14/LGIC/LGIC_NAMING/deliverables/exercises/r3/seats/e2.canary.txt
org/missions/D14/LGIC/LGIC_NAMING/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_NAMING/decompositions/LGIC_NAMING_DECOMP.md</decomp_doc> v5 @2f8cc63b8e, cell `LN-e-2`, round 3 (section 0d).
<owned_cells>LN-e-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `E2T-AC1`, `E2T-AC2`, `E2T-AC3`, `E2T-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_NAMING/deliverables/0.9.0_WK_LGIC_NAMING~2/LGIC_NAMING.TO-LN-e-2-r3.namer-b.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> E2T-AC1,E2T-AC2,E2T-AC3,E2T-AC4` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `namer-b.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
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

Seating: slot ~2, queue position 1. Round 3 of LGIC_NAMING, the recut of `1.0.0_SA_CTO`'s round-2 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_NAMING_ROUND2_20260915.md` @02f08322af); issued by `2.0.0_SA_COO~G`, which leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Round 3's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_NAMING/deliverables/2.0.0_SA_COO~G/fixed_inputs/r3/`. Decomposition v5 @2f8cc63b8e, section 0d.
