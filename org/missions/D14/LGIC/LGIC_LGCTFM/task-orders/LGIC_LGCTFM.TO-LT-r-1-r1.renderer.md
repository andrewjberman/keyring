# TO LGIC_LGCTFM.TO-LT-r-1-r1 -- the renderer -- two flow diagrams drawn from the contract, never by hand

<to_id>LGIC_LGCTFM.TO-LT-r-1-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~3</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-r-1` (decomposition v1.1) | **outcome_ref:** FWD-5 | **depends_on:** LT-s-1 (drained; the renderer reads a contract) and LT-s-2 (same slot)

---

## WORKER FACE

### THE CELL

`LT-r-1` (PRD T7, DEC-7). **You write `lib/lgctfm_render.py`** (stdlib, ASCII).

**THE INTERFACE:**
```
python lib/lgctfm_render.py render <contract.json> --out <dir>   writes <dir>/flow.current.md and <dir>/flow.desired.md
python lib/lgctfm_render.py check  <contract.json> --out <dir>   exit 0 iff a fresh render equals both files byte for byte;
                                                                 otherwise non-zero, printing STALE and the file
```
In the `/draw` house style (`.claude/skills/draw/SKILL.md`): triggers left, compute centre, tiers right, serving routes reading them. `flow.current.md` is drawn from `rows[].current` and `edges[]`; `flow.desired.md` from `rows[].desired` and `edges[]`, and it must NOT depend on any `current.*` cell -- so an edit to a row's `current.name` changes `flow.current.md` only on the lines that carry that name, and leaves `flow.desired.md` byte-identical. Deterministic: every set sorted where it is built, no wall clock.

The checker renders `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/PLANTED_CONTRACT.json` in temporary directories: twice (identical), once with `rows[0].current.name` edited, once with a hand edit appended to `flow.current.md` (check must fail), once untouched (check must pass).

**Read:** `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` DEC-7; `.claude/skills/draw/SKILL.md`; `infra/logic/11_LGCTFM_CONTRACT_SCHEMA_RECORD.md` s.6 (the edge types).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="R1R1-AC1" cell_refs="LT-r-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py r1-identical</invocation><expect>PASS-R1-TWO-RENDERS-BYTE-IDENTICAL</expect></criterion>

<criterion id="R1R1-AC2" cell_refs="LT-r-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py r1-edit</invocation><expect>PASS-R1-EDIT-CHANGES-ONLY-ITS-ROW</expect></criterion>

<criterion id="R1R1-AC3" cell_refs="LT-r-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py r1-hand-edit</invocation><expect>PASS-R1-HAND-EDIT-FAILS-CHECK</expect></criterion>

<criterion id="R1R1-AC4" cell_refs="LT-r-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py r1-fresh</invocation><expect>PASS-R1-FRESH-RENDER-PASSES-CHECK</expect></criterion>

<criterion id="R1R1-AC5" cell_refs="LT-r-1" judgment="true"/>

<expected_criteria>R1R1-AC1, R1R1-AC2, R1R1-AC3, R1R1-AC4, R1R1-AC5</expected_criteria>

**Every mechanical criterion above reads FAIL at the cut** (its input does not exist yet) **except where the issuance commit message records otherwise.** **R1R1-AC5, for `3.0.0_SA_CVO` at L9 (no verdict from you):** the two pictures read as the /draw house style and show what fires what, what writes where and what serves it for the planted contract.

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
lib/lgctfm_render.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.1, round-1 cell `LT-r-1` (sections 3 and 10).
<owned_cells>LT-r-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `R1R1-AC1`, `R1R1-AC2`, `R1R1-AC3`, `R1R1-AC4`, `R1R1-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~3/LGIC_LGCTFM.TO-LT-r-1-r1.renderer.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> R1R1-AC1,R1R1-AC2,R1R1-AC3,R1R1-AC4,R1R1-AC5 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-r-1-r1.renderer.md` BEFORE the `complete` flip.
Result file `renderer.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`R1R1-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- repository code and records only; no schedule is created or read as a trigger.
comp-iam: DECLARED-NOT-APPLICABLE -- no principal, policy or resource is created or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; the inputs are this estate's own records.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: written by this cell alone in round 1.
</preflight>

Seating: slot ~3, level 1. Round 1 of LGIC_LGCTFM, the first issuance on decomposition v1.1 (v1 @686d196fa1 plus s.10), issued by `2.0.0_SA_COO~G`. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py, PLANTED_CONTRACT.json, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json). Rulings carried: R-16, R-17, R-24.
