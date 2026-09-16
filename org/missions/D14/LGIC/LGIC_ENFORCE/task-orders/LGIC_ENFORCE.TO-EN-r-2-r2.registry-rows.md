# TO LGIC_ENFORCE.TO-EN-r-2-r2 -- the registry rows for the RAISE population

<to_id>LGIC_ENFORCE.TO-EN-r-2-r2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.2 @09bde3126c (ADMITTED; brief half re-signed by 4.0.0_SA_CRO @e848967b3f) | **Decomp cell:** `EN-r-2` (round 2) | **outcome_ref:** FWD-5 | **depends_on:** gate G-V19b (the one-carrier group on CLOUD) | **slot:** ~1, queue position 2

---

## WORKER FACE

### THE CELL

`EN-r-2` -- RULING ROWS (`1.0.0_SA_CTO`'s round-1 analysis s.2; CLAUDE.md Rule 30: a builder refusal is a missing registry row to add, never a hand-typed workaround).

**The population is fixed:** `C:/Users/AndrewBerman/Desktop/ajb_workspace/org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/RAISE_POPULATION.json`. It is every RAISE of both census planes at registry@ba5318901b937130, grouped by the token each RAISE message quotes: **152 groups** (live 115, the analysis's number; repo 134, 37 of them repo-only). Each group carries its count, its rule steps and up to 3 example names. `token:gateway` is subtracted as landed by `EN-r-5` before this round; it is in no group at that registry, and if a later read shows it, it is still `EN-r-5`'s. A `{system}` placeholder is not a RAISE and never a class (a) row here: `EN-r-4` fills it from `resources.json`, after this cell.

1. **Class each group into exactly ONE of:**
   - (a) a system that owes a `systems.json` row (VENDOR, PRODUCT or PLATFORM_SUBSYSTEM);
   - (b) a workstream or project code, which is never a system (S6);
   - (c) a library (R1.e);
   - (d) a rule gap, which stays a loud RAISE;
   - undecided: a group whose class you cannot decide. It goes to `1.0.0_SA_CTO` as a list and is never guessed.

   Classify BY SUBTRACTION from the 152, printing each class's count.
2. **Add the class (a) rows** to `infra/logic/registry/systems.json`: key; class; long and its basis; `owner_directive`, a D-code resolving in `org/missions/DIRECTIVES.yaml`; `owner_claim`, measured or inferred; `owner_basis`. Move each class (a) token out of `unresolved`. Make each class (b) and (c) token one the registry recognizes, so the rule places it (the registry's `refused_keys`, or the list the rule reads for that class), and move it out of `unresolved` too.
3. **Write `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/REGISTRY_TOKEN_CLASSES.md`:** prose, then ONE fenced ```json block
   `{"population": "<the fixed input's path>", "classes": {"a": ["token:..."], "b": [...], "c": [...], "d": [...], "undecided": [...]}, "counts": {"a": <n>, "b": <n>, "c": <n>, "d": <n>, "undecided": <n>}, "for_1.0.0_SA_CTO": ["token:..."], "why": {"token:...": "..."}}`.
   Keys are the population's group keys, verbatim.

The census is not run here; `EN-s-1` runs it after this cell and `EN-r-4` drain. A class (d) or undecided group stops that census, and the decomposition says so (v2 s.0b): class it honestly anyway. A row re-grades names, which is the point; it renames nothing.

**Read:** the population; `infra/logic/registry/systems.json`; `org/missions/D14/LGIC/LGIC_NAMING/deliverables/GRADING_RULE.md` V1 to V3 and R1; `org/missions/DIRECTIVES.yaml`; `infra/logic/02_DOCTRINE.md` s.1.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="R2-AC1" cell_refs="EN-r-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r2-every-group-classed</invocation><expect>VERDICT: PASS-EVERY-GROUP-CLASSED</expect></criterion>
`R2-AC1` -- every group of the population is in exactly one class, and the counts sum to the population less the pre-landed.

<criterion id="R2-AC2" cell_refs="EN-r-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r2-registry-valid</invocation><expect>VERDICT: PASS-R2-REGISTRY-VALID</expect></criterion>
`R2-AC2` -- the registry validates with 0 refusals.

<criterion id="R2-AC3" cell_refs="EN-r-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r2-a-rows</invocation><expect>VERDICT: PASS-A-ROWS-PRESENT</expect></criterion>
`R2-AC3` -- every class (a) group is a `systems.json` row of a ratified class with a D-code owner.

<criterion id="R2-AC4" cell_refs="EN-r-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r2-examples-resolve</invocation><expect>VERDICT: PASS-GROUP-EXAMPLES-RESOLVE</expect></criterion>
`R2-AC4` -- every example of a class (a), (b) or (c) group no longer raises on that group.

<criterion id="R2-AC5" cell_refs="EN-r-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r2-d-still-loud</invocation><expect>VERDICT: PASS-D-STILL-LOUD</expect></criterion>
`R2-AC5` -- every example of a class (d) or undecided group still raises.

<criterion id="R2-AC6" cell_refs="EN-r-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r2-no-token-twice</invocation><expect>VERDICT: PASS-NO-TOKEN-TWICE</expect></criterion>
`R2-AC6` -- no token is both a row and an unresolved or refused token.

<criterion id="R2-J1" cell_refs="EN-r-2" judgment="true"/>
`R2-J1` -- graded at L9 by 3.0.0_SA_CVO: every classification holds, and every class (a) row's owner and basis hold. RECORD; NO VERDICT.

<expected_criteria>R2-AC1, R2-AC2, R2-AC3, R2-AC4, R2-AC5, R2-AC6, R2-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn (after gate G-V19b). Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds round 1's `check_en.py` and its fixtures; `fixed_inputs/r2/` holds round 2's: `check_en_r2.py` (the checker every round-2 criterion calls), its fixtures under `tests/`, `RAISE_POPULATION.json`, `RESOURCE_GAPS.json` and `gateway_whole.patch`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it, never `PENDING-THIS-COMMIT`: commit the artifact first, then the proof in a later commit (row S18).
- **Nothing live moves in this cell.** It writes nothing to AWS and runs no Terraform.

<paths>
infra/logic/registry/systems.json
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/REGISTRY_TOKEN_CLASSES.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v2.1 @8e0d09e418, cell `EN-r-2`, round 2 (section 0b).
<owned_cells>EN-r-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `R2-AC1`, `R2-AC2`, `R2-AC3`, `R2-AC4`, `R2-AC5`, `R2-AC6`, `R2-J1`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-r-2-r2.registry-rows.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> R2-AC1,R2-AC2,R2-AC3,R2-AC4,R2-AC5,R2-AC6,R2-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `registry-rows.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 (carried; not re-run at the recut) -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This round registers G-V19a and G-V19b (decomposition v2 s.0b) and G-C (worker admission, after this issuance). G-V19b is owed before this cell spawns.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 2's write set (registry rows, lib/opal_naming.py, the opal_name module's generated files, the two naming limbs, safe-apply.sh, records, read-only plans): no operation, policy, principal or resource is added.
comp-adversary: RUN at the recut on the round-1 analysis @7b5331c8c0 -- 3 of 3 cited commits verified; 1 cited path, stable. Blindness stated: T11, the analysis carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder, under infra/, lib/, .tools/ or data/ refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~1, queue position 2. Round 2 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-1 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND1_20260915.md` @7b5331c8c0, msg 97145); issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974) and leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). LGIC_NAMING's round-4 re-grade (its cell f-1) is ordered after this cell drains (97137), and after `EN-r-4` (97177). Round 2's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/`. Decomposition v2.1 @8e0d09e418, section 0b.
