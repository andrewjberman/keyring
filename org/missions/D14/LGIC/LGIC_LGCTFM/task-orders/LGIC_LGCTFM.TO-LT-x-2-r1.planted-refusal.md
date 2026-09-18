# TO LGIC_LGCTFM.TO-LT-x-2-r1 -- the planted refusal -- an added use of a marked location is stopped, a removal passes

<to_id>LGIC_LGCTFM.TO-LT-x-2-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>complete -- 0.9.0_WK_LGIC_LGCTFM~3, 2026-09-17: X2R1-AC1..AC3 PASS-by-output (check_lt_r1.py x2-adding/x2-removing/x2-flag, rc=0 each); X2R1-AC4 UNVERIFIABLE-BY-INSTRUMENT (judgment, for 3.0.0_SA_CVO at L9); proof-of-spec-check VALID rc=0 @1b45fb4d55</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-x-2` (decomposition v1.1) | **outcome_ref:** FWD-7 | **depends_on:** LT-x-1 (drained on slot ~2; the planted refusal needs a MARK to violate) and LT-d-1 (same slot)

---

## WORKER FACE

### THE CELL

`LT-x-2` (PRD T11, DEC-9). **You write only records in your deliverables folder.** The estate-wide `org/mcp/naming-gate.enforce` flag is NOT yours and is never created, edited or removed on your branch.

1. **In a practice checkout** (a linked worktree on a scratch branch, never pushed; a sparse checkout is enough) with `org/mcp/naming-gate.enforce` present IN THAT WORKTREE ONLY, stage a change that ADDS one more hand-kept use of a location LT-x-1 marked under ADVI_FIRMBKTS, in a declaration tree the gate grades (never under `org/` or `docs/`); write `git diff --cached` to a file and run `python .tools/naming-gate.py --diff <that file>` there (enforcement comes from the flag present in that worktree): it must be refused and the refusal must name ADVI_FIRMBKTS. Then stage the change that REMOVES one such use and run the gate the same way: it must pass. Never commit either change. Delete the practice worktree.
2. **Keep the two diffs** as `deliverables/<your serial>/PLANTED_REFUSAL/add.diff` and `remove.diff` and write what you ran and saw to `PLANTED_REFUSAL/RECORD.md`.

The checker re-exercises both diffs itself with `.tools/naming-gate.py --diff <file> --enforce` -- a different path to the same gate -- so the refusal is measured, not reported.

**Read:** `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` DEC-9 and T11; `.tools/naming-gate.py` (`--diff`, `--enforce`, the DEC-6 matrix); `infra/logic/registry/remediations.json` (the ADVI_FIRMBKTS surfaces LT-x-1 appended).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="X2R1-AC1" cell_refs="LT-x-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x2-adding</invocation><expect>PASS-X2-ADDED-USE-REFUSED</expect></criterion>

<criterion id="X2R1-AC2" cell_refs="LT-x-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x2-removing</invocation><expect>PASS-X2-REMOVED-USE-PASSES</expect></criterion>

<criterion id="X2R1-AC3" cell_refs="LT-x-2"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x2-flag</invocation><expect>PASS-X2-ESTATE-FLAG-UNTOUCHED</expect></criterion>

<criterion id="X2R1-AC4" cell_refs="LT-x-2" judgment="true"/>

<expected_criteria>X2R1-AC1, X2R1-AC2, X2R1-AC3, X2R1-AC4</expected_criteria>

**Every mechanical criterion above reads FAIL at the cut** (its input does not exist yet) **except where the issuance commit message records otherwise.** **X2R1-AC4, for `3.0.0_SA_CVO` at L9 (no verdict from you):** the planted addition is a genuine hand-kept use a person would write, not a string shaped only to trip the gate.

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
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.1, round-1 cell `LT-x-2` (sections 3 and 10).
<owned_cells>LT-x-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `X2R1-AC1`, `X2R1-AC2`, `X2R1-AC3`, `X2R1-AC4`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/LGIC_LGCTFM.TO-LT-x-2-r1.planted-refusal.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> X2R1-AC1,X2R1-AC2,X2R1-AC3,X2R1-AC4 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-x-2-r1.planted-refusal.md` BEFORE the `complete` flip.
Result file `planted-refusal.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`X2R1-AC4` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository code and records only; no schedule is created or read as a trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal, policy or resource is created or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; the inputs are this estate's own records.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: writes only this slot's deliverables folder; the practice worktree is untracked and deleted before report.
</preflight>

Seating: slot ~3, level 6. Round 1 of LGIC_LGCTFM, the first issuance on decomposition v1.1 (v1 @686d196fa1 plus s.10), issued by `2.0.0_SA_COO~G`. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py, PLANTED_CONTRACT.json, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json). Rulings carried: R-16, R-17, R-24.
