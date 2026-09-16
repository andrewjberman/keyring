# TO LGIC_ENFORCE.TO-EN-t-2-r2 -- the apply limb reads the plan

<to_id>LGIC_ENFORCE.TO-EN-t-2-r2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.2 @09bde3126c (ADMITTED; brief half re-signed by 4.0.0_SA_CRO @e848967b3f) | **Decomp cell:** `EN-t-2` (round 2) | **outcome_ref:** FWD-4 | **depends_on:** EN-g-1 round 2 (merged) | **slot:** ~3, queue position 2

---

## WORKER FACE

### THE CELL

`EN-t-2` -- the apply limb reads the plan (`1.0.0_SA_CTO`'s round-1 analysis s.2, RULINGS ADD and PLAN; row W3-S8). An apply has no diff, so whether a resource is being ADDED is known only to a plan. Edit `.tools/naming-apply-gate.py` and `.tools/safe-apply.sh`:

1. **Plan mode, new:** `python .tools/naming-apply-gate.py --plan-json FILE [--enforce]` reads a `terraform show -json` document's `resource_changes`.
   - A resource whose actions include `create`, or an `update` whose own-name attribute changes, is an ADDITION. Its evaluated name (`change.after`'s own-name attribute, from the schema's Terraform-type map) is graded, and one `grade()` does not return CONFORMANT or NOT-GRADED is REFUSED, with its canonical form printed.
   - Every other resource (a no-op, an update that keeps its name, a delete) only WARNs.
   - Output: one `NAMING <verdict> <address> <name> -> <canonical>` line per graded name (`<verdict>` is REFUSE, WARN or the grade), then `NAMING-PLAN: <PASS|WARN|REFUSE> <n> graded`. Enforcing, a REFUSE exits 1; otherwise it exits 0.
2. **The pre-plan mode** (`naming-apply-gate.py DIR`) keeps grading literals but NEVER refuses: it cannot tell an existing resource from a new one. It prints `<n> expressions deferred to plan` for the names that exist only in a plan, and never passes them silently.
3. **`safe-apply.sh` runs the plan mode over the plan it renders,** before any other plan-reading gate can block and before apply. On a REFUSE while enforcing it prints `safe-apply: BLOCKED by the naming plan limb ...` and exits non-zero without applying. WARN mode never changes the exit code, as today.
4. **The own-name attribute per Terraform type comes from the schema's map** (through the commit limb, `EN-g-1`), never from a map of this file's own.

Nothing real is planned in this cell. The criteria run on the fixtures under `fixed_inputs/r2/tests/t2r/` and on a stub terraform; `EN-t-3` reads the real roots.

**Read:** `.tools/naming-apply-gate.py`; `.tools/safe-apply.sh`; `.tools/naming-gate.py` (the map); the fixtures under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/tests/t2r/`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="T2R-AC1" cell_refs="EN-t-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py t2r-create-literal</invocation><expect>VERDICT: PASS-CREATE-REFUSED-WITH-CANONICAL</expect></criterion>
`T2R-AC1` -- a created resource with a wrong literal name is refused with the canonical form `grade()` computes.

<criterion id="T2R-AC2" cell_refs="EN-t-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py t2r-create-expression</invocation><expect>VERDICT: PASS-EXPRESSION-REFUSED-AT-PLAN</expect></criterion>
`T2R-AC2` -- a created resource whose wrong name an expression built is refused at plan with its canonical form.

<criterion id="T2R-AC3" cell_refs="EN-t-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py t2r-rename</invocation><expect>VERDICT: PASS-RENAME-REFUSED</expect></criterion>
`T2R-AC3` -- a rename to a wrong name is refused with its canonical form.

<criterion id="T2R-AC4" cell_refs="EN-t-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py t2r-existing</invocation><expect>VERDICT: PASS-EXISTING-ONLY-WARNS</expect></criterion>
`T2R-AC4` -- existing, name-keeping and deleted resources with wrong names only warn, enforcing.

<criterion id="T2R-AC5" cell_refs="EN-t-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py t2r-correct</invocation><expect>VERDICT: PASS-CORRECT-CREATE-PASSES</expect></criterion>
`T2R-AC5` -- a correct create passes, enforcing.

<criterion id="T2R-AC6" cell_refs="EN-t-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py t2r-deferred</invocation><expect>VERDICT: PASS-DEFERRED-COUNT-PRINTED</expect></criterion>
`T2R-AC6` -- the pre-plan limb prints the deferred-expression count and never refuses, enforcing.

<criterion id="T2R-AC7" cell_refs="EN-t-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py t2r-wired-blocks</invocation><expect>VERDICT: PASS-WIRED-PLAN-LIMB-BLOCKS</expect></criterion>
`T2R-AC7` -- `safe-apply.sh`, enforcing, blocks on the plan limb before apply is invoked.

<criterion id="T2R-AC8" cell_refs="EN-t-2"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py t2r-wired-passes</invocation><expect>VERDICT: PASS-WIRED-PLAN-LIMB-PASSES</expect></criterion>
`T2R-AC8` -- `safe-apply.sh`, enforcing, passes the plan limb on a correct plan.

<expected_criteria>T2R-AC1, T2R-AC2, T2R-AC3, T2R-AC4, T2R-AC5, T2R-AC6, T2R-AC7, T2R-AC8</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds round 1's `check_en.py` and its fixtures; `fixed_inputs/r2/` holds round 2's: `check_en_r2.py` (the checker every round-2 criterion calls), its fixtures under `tests/`, `RAISE_POPULATION.json`, `RESOURCE_GAPS.json` and `gateway_whole.patch`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it, never `PENDING-THIS-COMMIT`: commit the artifact first, then the proof in a later commit (row S18).
- **Nothing live moves in this cell.** No real plan and no apply: the criteria run a stub terraform. Never create `org/mcp/naming-gate.enforce`.
- **Identity for the stub runs.** Export `OPAL_AGENT_SERIAL` (your serial) before running T2R-AC7 and T2R-AC8: `safe-apply.sh`'s halt checkpoint resolves the invoker (row W3-S6).

<paths>
.tools/naming-apply-gate.py
.tools/safe-apply.sh
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v2.1 @8e0d09e418, cell `EN-t-2`, round 2 (section 0b).
<owned_cells>EN-t-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `T2R-AC1`, `T2R-AC2`, `T2R-AC3`, `T2R-AC4`, `T2R-AC5`, `T2R-AC6`, `T2R-AC7`, `T2R-AC8`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~3/LGIC_ENFORCE.TO-EN-t-2-r2.plan-limb.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> T2R-AC1,T2R-AC2,T2R-AC3,T2R-AC4,T2R-AC5,T2R-AC6,T2R-AC7,T2R-AC8` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `plan-limb.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 (carried; not re-run at the recut) -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This round registers G-V19a and G-V19b (decomposition v2 s.0b) and G-C (worker admission, after this issuance). None is owed by this cell; G-F (the live flip) stays outside this round.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 2's write set (registry rows, lib/opal_naming.py, the opal_name module's generated files, the two naming limbs, safe-apply.sh, records, read-only plans): no operation, policy, principal or resource is added.
comp-adversary: RUN at the recut on the round-1 analysis @7b5331c8c0 -- 3 of 3 cited commits verified; 1 cited path, stable. Blindness stated: T11, the analysis carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder, under infra/, lib/, .tools/ or data/ refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~3, queue position 2. Round 2 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-1 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND1_20260915.md` @7b5331c8c0, msg 97145); issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974) and leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Round 2's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/`. Decomposition v2.1 @8e0d09e418, section 0b.
