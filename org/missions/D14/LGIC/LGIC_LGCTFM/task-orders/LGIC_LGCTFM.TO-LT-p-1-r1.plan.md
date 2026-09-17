# TO LGIC_LGCTFM.TO-LT-p-1-r1 -- the plan -- ATOM_DECOMP packages in R19's order, and the run verb that assembles a run

<to_id>LGIC_LGCTFM.TO-LT-p-1-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-p-1` (decomposition v1.1) | **outcome_ref:** FWD-6 | **depends_on:** LT-e-3 (drained on slot ~1; the plan is ordered by the tension set) and LT-h-1 (same slot)

---

## WORKER FACE

### THE CELL

`LT-p-1` (PRD T6, DEC-8). **You edit `lib/opal_lgctfm.py`** -- after slot ~1's LT-e-3 has drained; you are its fourth and last round-1 writer.

**TWO VERBS:**
```
python lib/opal_lgctfm.py plan <run dir>
    reads <run dir>/contract.json; writes <run dir>/plan.json and <run dir>/plan.md; deterministic (a re-run on a copy is
    byte-equal).
python lib/opal_lgctfm.py run --subject <key> --run-home-subject <directory name> --seed <bucket> [...] --root <dir>
    allocates a run directory <root>/<directory name>/<run-id>/ through workflows/legacy_transform/run_home.py `new`, walks, computes desired, forks and
    tensions into contract.json, calls plan, renders flow.current.md and flow.desired.md through lib/lgctfm_render.py
    `render` (LGIC_LGCTFM LT-r-1), and refreshes MANIFEST.md. It writes nothing outside that run directory and MANIFEST.md.
```
**`plan.json`** = `{"executed": false, "packages": [...]}`; each package carries the eight ATOM_DECOMP fields `objective`, `dependencies`, `reads`, `writes`, `acceptance_proof`, `rollback`, `owner`, `replacement_obligation`, plus `package_id`, `step` (one of MAP, CLASSIFY, RULE, PORT, REPOINT, PROVE -- packages emitted in that order), `status: PLANNED`, and -- for every package whose `writes` names a client-facing row (by `row_id` or by that row's `arn_or_path`) -- `never_widen_signoff_owed: true` and `signoff_owners` naming `1.0.0_SA_CTO` and `2.0.0_SA_COO`. **No package is executed; the plan signs nothing.**

**THE GRADED PLAN:** copy slot ~1's `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~1/walk/contract.json` to `deliverables/<your serial>/plan_r1/contract.json` and run `plan` on that directory.

**Read:** `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` DEC-8; `infra/logic/02_DOCTRINE.md` R19; `projects/ATOM_DECOMP/skill/atomic-decomposition/` (the package fields); `workflows/legacy_transform/run_home.py`.

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="P1R1-AC1" cell_refs="LT-p-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py p1-fields</invocation><expect>PASS-P1-EIGHT-FIELDS-EVERY-PACKAGE</expect></criterion>

<criterion id="P1R1-AC2" cell_refs="LT-p-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py p1-r19</invocation><expect>PASS-P1-R19-ORDER</expect></criterion>

<criterion id="P1R1-AC3" cell_refs="LT-p-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py p1-served</invocation><expect>PASS-P1-SERVED-KEYS-OWE-SIGNOFF</expect></criterion>

<criterion id="P1R1-AC4" cell_refs="LT-p-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py p1-not-executed</invocation><expect>PASS-P1-NOTHING-EXECUTED</expect></criterion>

<criterion id="P1R1-AC5" cell_refs="LT-p-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py p1-regenerates</invocation><expect>PASS-P1-PLAN-REGENERATES-BYTE-EQUAL</expect></criterion>

<criterion id="P1R1-AC6" cell_refs="LT-p-1" judgment="true"/>

<expected_criteria>P1R1-AC1, P1R1-AC2, P1R1-AC3, P1R1-AC4, P1R1-AC5, P1R1-AC6</expected_criteria>

**Every mechanical criterion above reads FAIL at the cut** (its input does not exist yet) **except where the issuance commit message records otherwise.** **P1R1-AC6, for `3.0.0_SA_CVO` at L9 (no verdict from you):** a COO lane could cut a decomposition from `plan.json` without re-deriving the inventory: each package's reads, writes and acceptance proof name real rows.

`<WS>` is your worktree's absolute path, given in your identity line. Every invocation above runs from your worktree root; the checker reads the tree it is run in.

## BOUNDS

- **Grant.** Your write surface is the `<paths>` block below, plus `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/<your serial>/` and this order's own file. Nothing else. A path you need that is not named is a BLOCKING row on that criterion -- never an override.
- **Branch.** Work in the worktree named in your identity line, on its branch. Never push, merge, rebase, `checkout --` or `clean`.
- **Fixed inputs are read-only**, everything under `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/`. If you believe a criterion's checker is wrong, file a BLOCKING row naming the arm and the evidence; never work around it and never edit it.
- **Surprises** go to `org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md` as ONE row each, appended to the last JSON array in the file, id `LGIC_LGCTFM-W<n>-S<k>` (`<n>` your slot; `<k>` ONE ABOVE the highest `LGIC_LGCTFM-W<n>-S` id already present in ANY document under `org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/`). Keep working after filing. A row's `disarm_owner` is never a worker serial.
- **Judge from the files this order names and cite them** (`path:line @commit`), never the CLAUDE.md or memory text every worker starts with.
- **Numbers in this order are CONTEXT, measured by the issuer at the cut, never acceptance values** -- except where a criterion prints one. Re-measure at your own tree.
- **Commit before you grade.** The checker reads the tree it runs in; commit your artifact, then run every criterion, then write the proof instance.
- **Nothing live moves (DEC-13).** Every instrument you call is read-only against AWS; the portal is read, never written. No Terraform apply, no AWS write, no deploy, no rename of a live resource.
- **Disk on this box is tight.** Keep scratch small; delete any temporary worktree you create before you report.

<paths>
org/missions/D14/LGIC/LGIC_LGCTFM/surprise-channel/investigations/INVESTIGATION_v1.md
lib/opal_lgctfm.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.1, round-1 cell `LT-p-1` (sections 3 and 10).
<owned_cells>LT-p-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `P1R1-AC1`, `P1R1-AC2`, `P1R1-AC3`, `P1R1-AC4`, `P1R1-AC5`, `P1R1-AC6`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-p-1-r1.plan.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> P1R1-AC1,P1R1-AC2,P1R1-AC3,P1R1-AC4,P1R1-AC5,P1R1-AC6 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-p-1-r1.plan.md` BEFORE the `complete` flip.
Result file `plan.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`P1R1-AC6` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository code and records only; no schedule is created or read as a trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal, policy or resource is created or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; the inputs are this estate's own records.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: lib/opal_lgctfm.py: four sequenced writers (decomposition v1.1 s.10); this cell is the last and starts only after LT-e-3 drains.
</preflight>

Seating: slot ~2, level 4. Round 1 of LGIC_LGCTFM, the first issuance on decomposition v1.1 (v1 @686d196fa1 plus s.10), issued by `2.0.0_SA_COO~G`. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py, PLANTED_CONTRACT.json, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json). Rulings carried: R-16, R-17, R-24.
