# TO LGIC_ENFORCE.TO-EN-r-3-r2 -- one carrier for a firm's forms

<to_id>LGIC_ENFORCE.TO-EN-r-3-r2</to_id>
<project>LGIC_ENFORCE</project>
<issued_to>0.9.0_WK_LGIC_ENFORCE~1</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-15</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_ENFORCE_PRD.md` v1.2 @09bde3126c (ADMITTED; brief half re-signed by 4.0.0_SA_CRO @e848967b3f) | **Decomp cell:** `EN-r-3` (round 2) | **outcome_ref:** FWD-2, FWD-7 | **depends_on:** EN-r-5 (on CLOUD) and gate G-V19a (NAMING_SCHEMA.json v1.9 on `lgic-v19-landing`, met @bf506e53be) | **slot:** ~1, queue position 1

---

## WORKER FACE

### THE CELL

`EN-r-3` -- RULING ONE: one carrier (`1.0.0_SA_CTO`'s round-1 analysis s.2, RULINGS ONE and DEMO, and DEC-1 under row W1-S8). Your worktree is cut from the branch `lgic-v19-landing` (@bf506e53be or later), where `1.0.0_SA_CTO` has committed `org/standards/NAMING_SCHEMA.json` v1.9, ADMITTED there: `firm_forms` is removed, and the Terraform-type-to-node-type map is data. The registry file `infra/logic/registry/scopes.json` is now the ONE home of a firm's forms.

1. **Repoint EVERY reader of `firm_forms`** in `lib/opal_naming.py` to the scope rows. At CLOUD @7b5331c8c0 they are `:248` (the schema read), `:287-290` (`validate`'s FIRM check and its warning), `:347` (the system-key collision map) and `:381` (that refusal's text): `4.0.0_SA_CRO`'s note (b), `1.0.0_SA_CTO` 97200. Re-read the file at your base, which is later. Afterwards no code in the file names `firm_forms`, and a firm row's own short form is its only spelling source.
2. **Generate `infra/aws/terraform/modules/opal_name/tests/opal_name.tftest.hcl`** from the registry's vectors: make it a `generate` target with the GENERATED mark in HCL comment syntax, one run block per vector plus the coverage run, so no count is typed (row W1-S12).
3. **DEC-1:** a scope row carries the REQUIRED fields `validate` names, and a further field only if a generator or `validate` reads it. Remove any field nothing reads (row W1-S8). State the required list in `scopes.json`'s `_about`, and make `_about` name the registry as the one home of a firm's forms (it names `firm_forms` today, in `_about.row_fields`: row S19).
4. **RULING DEMO:** demo's `tenancy` is `DEMO-TENANT` (Andrew card 8, ledger X6 GRANTED; `infra/logic/02_DOCTRINE.md` s.1). Add a `tiers.json` home rule for `DEMO-TENANT`, taking the doctrine's homes for a demo tenant. Demo's note no longer says the doctrine does not define the class; it cites X6. Naming still reads `demo` in the firm slot (RULING DM).
5. **Record the readers** in `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FIRM_FORMS_READERS.md`: prose, then ONE fenced ```json block
   `{"readers": [{"path": "...", "disposition": "repointed|historical-record|another-project", "why": "..."}]}`,
   covering every tracked file that names `firm_forms` at your spawn base or at your tip, by an unscoped `git grep -l firm_forms` (the issuer's instruments under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` are excluded, and R3-AC1 prints the exclusion). A file you did not repoint that still names it is a historical record (a round's record, a review, an adjudication) or another project's. LGIC_NAMING's round-3 fixed inputs read it for their seats: row that for the issuer, and do not edit them.

Do not touch the `("opal", "ingress", None, "lb")` vector shape: `EN-r-5` landed it. The registry's hash moves with this cell, so the generated views' headers go stale until `EN-r-6` regenerates them; that is expected.

**Read:** `org/standards/NAMING_SCHEMA.json` v1.9 at your base; `lib/opal_naming.py`; `infra/logic/registry/`; `opal_name.tftest.hcl`; `infra/logic/02_DOCTRINE.md` s.1.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="R3-AC1" cell_refs="EN-r-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r3-one-carrier</invocation><expect>VERDICT: PASS-ONE-CARRIER</expect></criterion>
`R3-AC1` -- a census (97200): 0 reads of `firm_forms` remain. No code in `lib/opal_naming.py` names it, the schema carries none, and every other tracked file an unscoped search finds naming it is a recorded non-reader; the files scanned are printed.

<criterion id="R3-AC2" cell_refs="EN-r-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r3-validate-clean</invocation><expect>VERDICT: PASS-VALIDATE-CLEAN</expect></criterion>
`R3-AC2` -- validate reads 0 refusals and no warning but the inferred-owner ones.

<criterion id="R3-AC3" cell_refs="EN-r-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r3-new-firm-clean</invocation><expect>VERDICT: PASS-NEW-FIRM-CLEAN</expect></criterion>
`R3-AC3` -- one new FIRM row, in a scratch copy, draws no warning.

<criterion id="R3-AC4" cell_refs="EN-r-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r3-short-moves</invocation><expect>VERDICT: PASS-ONE-CHANGE-MOVES-BOTH</expect></criterion>
`R3-AC4` -- one change to a firm's short form moves `name()` and `fence_patterns()` together.

<criterion id="R3-AC5" cell_refs="EN-r-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r3-tftest-generated</invocation><expect>VERDICT: PASS-TFTEST-GENERATED</expect></criterion>
`R3-AC5` -- the tftest is generated, one run per vector, and `generate` reproduces it.

<criterion id="R3-AC6" cell_refs="EN-r-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r3-dec1-fields</invocation><expect>VERDICT: PASS-EVERY-FIELD-READ</expect></criterion>
`R3-AC6` -- every scope-row field is named by the module.

<criterion id="R3-AC7" cell_refs="EN-r-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r3-about-one-home</invocation><expect>VERDICT: PASS-ABOUT-NAMES-ONE-HOME</expect></criterion>
`R3-AC7` -- `scopes.json`'s `_about` names no second list (row S19).

<criterion id="R3-AC8" cell_refs="EN-r-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r3-demo-tenant</invocation><expect>VERDICT: PASS-DEMO-TENANT</expect></criterion>
`R3-AC8` -- demo's tenancy is DEMO-TENANT, with a home rule and a note citing X6.

<criterion id="R3-AC9" cell_refs="EN-r-3"><invocation>cd <WS> && timeout 120 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r3-reader-census</invocation><expect>VERDICT: PASS-READERS-CENSUSED</expect></criterion>
`R3-AC9` -- every file that named `firm_forms` at the base carries a disposition, and none marked repointed still names it.

<criterion id="R3-AC10" cell_refs="EN-r-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/check_en_r2.py r3-tests</invocation><expect>VERDICT: PASS-NO-NEW-LIB-TEST-FAILURE</expect></criterion>
`R3-AC10` -- `lib/tests/test_opal_naming.py` has no new failure against the base's failing set (RULING RED).

<criterion id="R3-J1" cell_refs="EN-r-3" judgment="true"/>
`R3-J1` -- graded at L9 by 3.0.0_SA_CVO: every reader's disposition holds, and DEC-1's required list is the one `validate` enforces. RECORD; NO VERDICT.

<expected_criteria>R3-AC1, R3-AC2, R3-AC3, R3-AC4, R3-AC5, R3-AC6, R3-AC7, R3-AC8, R3-AC9, R3-AC10, R3-J1</expected_criteria>

`<WS>` is your worktree's absolute path, given in your identity line.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/<your serial>/` and this order's own file (for the `<status>` flip). Nothing else. A path you need that is not named is a BLOCKING surprise row on that criterion -- never an override.
- **Branch.** You work in the worktree named in your identity line, on its branch, cut from `lgic-v19-landing`'s tip at spawn (gate G-V19a; v1.9 is ADMITTED there @bf506e53be). Never push, merge, rebase, `checkout --` or `clean`. The COO drains your branch into `lgic-v19-landing`, never into CLOUD; the one-carrier group reaches CLOUD in one merge (gate G-V19b).
- **Fixed inputs are read-only.** `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/` holds round 1's `check_en.py` and its fixtures; `fixed_inputs/r2/` holds round 2's: `check_en_r2.py` (the checker every round-2 criterion calls), its fixtures under `tests/`, `RAISE_POPULATION.json`, `RESOURCE_GAPS.json` and `gateway_whole.patch`. Never edit any of them.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, id `LGIC_ENFORCE-W<n>-S<k>` (`<n>` your slot), per the worker definition. Keep working after filing.
- **The preloaded context.** Every worker in this fabric starts with the workspace CLAUDE.md and the user's auto-memory in context (row LGIC_NAMING-S12 @3d671ff59c). Judge from the files this order names, and cite them, never the preloaded text.
- **Numbers** in this order are context, never acceptance values, except where a criterion prints one.
- **Pins by commit.** Every artifact your proof instance cites names the commit that carries it, never `PENDING-THIS-COMMIT`: commit the artifact first, then the proof in a later commit (row S18).
- **Nothing live moves in this cell.** It writes nothing to AWS and runs no Terraform apply.

<paths>
lib/opal_naming.py
lib/tests/test_opal_naming.py
infra/logic/registry/scopes.json
infra/logic/registry/tiers.json
infra/aws/terraform/modules/opal_name/
org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/FIRM_FORMS_READERS.md
org/missions/D14/LGIC/LGIC_ENFORCE/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_ENFORCE/decompositions/LGIC_ENFORCE_DECOMP.md</decomp_doc> v2.1 @8e0d09e418, cell `EN-r-3`, round 2 (section 0b).
<owned_cells>EN-r-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `R3-AC1`, `R3-AC2`, `R3-AC3`, `R3-AC4`, `R3-AC5`, `R3-AC6`, `R3-AC7`, `R3-AC8`, `R3-AC9`, `R3-AC10`, `R3-J1`. Instance at
`org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/0.9.0_WK_LGIC_ENFORCE~1/LGIC_ENFORCE.TO-EN-r-3-r2.one-carrier.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> R3-AC1,R3-AC2,R3-AC3,R3-AC4,R3-AC5,R3-AC6,R3-AC7,R3-AC8,R3-AC9,R3-AC10,R3-J1` BEFORE the `complete` flip.
Every `judgment="true"` criterion is recorded `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO` at L9 -- **a `PASS` or `FAIL` on a judgment row is INVALID.**
Result file `one-carrier.r2.result.md` beside it. **Flip `complete` only when every MECHANICAL criterion PASSES by output** -- a flip while a row is FAIL withdraws your own grant.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at L5 (carried; not re-run at the recut) -- --budget 540, 5 of 5 carriers (C1 230, C2 6, C3 12, C4 21, C5 334), 25 gates armed, none naming LGIC_ENFORCE. This round registers G-V19a and G-V19b (decomposition v2 s.0b) and G-C (worker admission, after this issuance). G-V19a is owed before this cell spawns; this cell is one of G-V19b's members.
comp-iam: DECLARED-NOT-APPLICABLE -- measured on round 2's write set (registry rows, lib/opal_naming.py, the opal_name module's generated files, the two naming limbs, safe-apply.sh, records, read-only plans): no operation, policy, principal or resource is added.
comp-adversary: RUN at the recut on the round-1 analysis @7b5331c8c0 -- 3 of 3 cited commits verified; 1 cited path, stable. Blindness stated: T11, the analysis carries no <decomp_ref>, so filesystem adjacency stands as its neighborhood.
lane: the <paths> block IS the grant (RULING 1, owned-paths-validate.py worker_grant). A path under deliverables/ with no serial folder, under infra/, lib/, .tools/ or data/ refuses by lane and is admitted only by this order's <paths>.
</preflight>

Seating: slot ~1, queue position 1. Round 2 of LGIC_ENFORCE, the recut of `1.0.0_SA_CTO`'s round-1 analysis (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ROUND_ANALYSIS_LGIC_ENFORCE_ROUND1_20260915.md` @7b5331c8c0, msg 97145); issued by `2.0.0_SA_COO~G`, which keeps LGIC_ENFORCE on Andrew-direct ~18:2xZ (96673, record @9240af5974) and leads the sequence on Andrew-direct ~16:3xZ (record @507864b842). Round 2's fixed inputs are committed with this issuance under `org/missions/D14/LGIC/LGIC_ENFORCE/deliverables/2.0.0_SA_COO~G/fixed_inputs/r2/`. Decomposition v2.1 @8e0d09e418, section 0b.
