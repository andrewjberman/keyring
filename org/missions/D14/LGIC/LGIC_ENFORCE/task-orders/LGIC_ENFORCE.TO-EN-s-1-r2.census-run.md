# TO LGIC_ENFORCE.TO-EN-s-1-r2 -- census mode, run again

<to_id>LGIC_ENFORCE.TO-EN-s-1-r2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.2 @09bde3126c (ADMITTED; brief half re-signed by 4.0.0_SA_CRO @e848967b3f) | **Decomp cell:** `EN-s-1` (round 2) | **outcome_ref:** FWD-5 | **depends_on:** EN-r-2 and EN-r-4 round 2 (merged) | **slot:** ~2, queue position 1

---

## WORKER FACE

### THE CELL

`EN-s-1` -- census mode, run again (DEC-7), on the registry `EN-r-2` and `EN-r-4` land.

Run `python lib/opal_naming.py census --live --repo --report org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/NAMING_CENSUS_REPORT.md`. The code is round 1's; do not change it. The report is rewritten in place, and round 1's stays at its commit.

**What the counts should show.** Registering `gateway` (`EN-r-5`) re-grades 14 live `opal-gateway-*` names to `gateway-*` canonical forms: a verdict, not a rename (`1.0.0_SA_CTO` 97167). `EN-r-2`'s rows resolve the groups it classed (a), (b) or (c), and `EN-r-4`'s rows fill `{system}` where a name's own tokens resolve none. If a class (d) or undecided group remains, the run stops on it: S1R-AC1 and S1R-AC2 then FAIL by measurement, and the order stays pending. That is a result, not a defect (decomposition v2 s.0b). Never alter the census to skip a RAISE or to file it under a verdict.

**Read:** `lib/opal_naming.py` (census); `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/REGISTRY_TOKEN_CLASSES.md`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="S1R-AC1" cell_refs="EN-s-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py s1-planes</invocation><expect>VERDICT: PASS-BOTH-PLANES</expect></criterion>
`S1R-AC1` -- the report covers the repo and the live plane, with the vintage and denominators printed (round 1's S1-AC1, unchanged).

<criterion id="S1R-AC2" cell_refs="EN-s-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py s1-all-judged</invocation><expect>VERDICT: PASS-ALL-JUDGED</expect></criterion>
`S1R-AC2` -- every nameable live name is judged (round 1's S1-AC2, unchanged).

<criterion id="S1R-AC3" cell_refs="EN-s-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py s1-row-shape</invocation><expect>VERDICT: PASS-ROW-SHAPE</expect></criterion>
`S1R-AC3` -- every row carries current, canonical, verdict, type and plane (round 1's S1-AC3, unchanged).

<criterion id="S1R-AC4" cell_refs="EN-s-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/check_en.py s1-raise-stops</invocation><expect>VERDICT: PASS-RAISE-STOPS</expect></criterion>
`S1R-AC4` -- a RAISE stops the run and prints the string (round 1's S1-AC4, unchanged).

<criterion id="S1R-AC5" cell_refs="EN-s-1"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py s1r-report-at-head</invocation><expect>VERDICT: PASS-REPORT-AT-HEAD-REGISTRY</expect></criterion>
`S1R-AC5` -- the report was written at HEAD's registry.

<expected_criteria>S1R-AC1, S1R-AC2, S1R-AC3, S1R-AC4, S1R-AC5</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `CLOUD` at spawn. Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch.
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds round 1's `check_en.py` and its fixtures; `fixed_inputs/r2/` holds round 2's: `check_en_r2.py` (the checker every round-2 criterion calls), its fixtures under `tests/`, `RAISE_POPULATION.json`, `RESOURCE_GAPS.json` and `gateway_whole.patch`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it, never `PENDING-THIS-COMMIT`: commit the artifact first, then the proof in a later commit (row S18).
- **Nothing live moves in this cell.** The live plane is read through `comp-find --corpus aws`; nothing is written to AWS.

<paths>
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/NAMING_CENSUS_REPORT.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v2.1 @8e0d09e418, cell `EN-s-1`, round 2 (section 0b).
<owned_cells>EN-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `S1R-AC1`, `S1R-AC2`, `S1R-AC3`, `S1R-AC4`, `S1R-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~2/LGIC_ENFORCE.TO-EN-s-1-r2.census-run.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> S1R-AC1,S1R-AC2,S1R-AC3,S1R-AC4,S1R-AC5` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `census-run.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 (carried; not re-run at the recut) -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This round registers G-V19a and G-V19b (decomposition v2 s.0b) and G-C (worker admission, after this issuance). None is owed by this cell.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 2's write set (registry rows, lib/opal_naming.py, the opal_name module's generated files, the two naming limbs, safe-apply.sh, records, read-only plans): no operation, policy, principal or resource is added.
comp-adversary: RUN at the recut on the round-1 analysis @7b5331c8c0 -- 3 of 3 cited commits verified; 1 cited path, stable. Blindness stated: T11, the analysis carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~2, queue position 1. Round 2 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-1 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND1_20260915.md` @7b5331c8c0, msg 97145); issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974) and leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Round 2's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/`. Decomposition v2.1 @8e0d09e418, section 0b.
