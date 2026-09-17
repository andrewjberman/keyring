# TO LGIC_LGCTFM.TO-LT-h-1-r1 -- the run home and the diff, keyed on row identity

<to_id>LGIC_LGCTFM.TO-LT-h-1-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>pending</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-h-1` (decomposition v1.1) | **outcome_ref:** FWD-8 | **depends_on:** none -- level 0 (independent of the schema); LT-p-1 continues on this slot

---

## WORKER FACE

### THE CELL

`LT-h-1` (PRD T8, DEC-12). **You write `workflows/legacy_transform/run_home.py` and `workflows/legacy_transform/README.md`.**

**THE INTERFACE, fixed so the criteria can grade it** (stdlib, ASCII):
```
python workflows/legacy_transform/run_home.py new --root <dir> --subject <key> --repo-head <sha> --graph-built <iso> --registry-hash <h> [--run-id <id>]
    creates <root>/<subject>/<run-id>/ with VINTAGE.json {repo_head, graph_built, registry_hash, run_id}; prints the path.
    run-id defaults to <UTC YYYYMMDDTHHMMSSZ>-<short repo head>. A run directory that EXISTS is REFUSED (non-zero exit)
    and left byte-identical: runs are never overwritten.
python workflows/legacy_transform/run_home.py manifest --root <dir> --subject <key>
    writes <root>/<subject>/MANIFEST.md listing every run with its run-id and its three vintage values (compile-on-view).
python workflows/legacy_transform/run_home.py diff <runA dir> <runB dir>
    reads each run's contract.json `tensions[]` and prints exactly three sections, each a heading line then one line per
    tension, indented two spaces:
      CLOSED: <n>      (in A, not in B)
      OPENED: <n>      (in B, not in A)
      UNCHANGED: <n>   (in both)
    A tension's identity is the string  <row_id>|<axis>|<kind>|<deciding_rules sorted, comma-joined>  -- never prose, so a
    changed note on an unchanged tension stays UNCHANGED.
```
`<root>` defaults to `workflows/legacy_transform`. The README follows `workflows/atom_decomposition/README.md`'s convention.

**Read:** `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` DEC-12; `workflows/atom_decomposition/README.md`; `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/PLANTED_CONTRACT.json` (the checker plants runs from it in a temporary root).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="H1R1-AC1" cell_refs="LT-h-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py h1-headings</invocation><expect>PASS-H1-DIFF-CLOSED-OPENED-UNCHANGED</expect></criterion>

<criterion id="H1R1-AC2" cell_refs="LT-h-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py h1-identity</invocation><expect>PASS-H1-DIFF-KEYED-ON-IDENTITY</expect></criterion>

<criterion id="H1R1-AC3" cell_refs="LT-h-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py h1-no-overwrite</invocation><expect>PASS-H1-SECOND-RUN-NEVER-OVERWRITES</expect></criterion>

<criterion id="H1R1-AC4" cell_refs="LT-h-1"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py h1-manifest</invocation><expect>PASS-H1-MANIFEST-LISTS-EVERY-RUN</expect></criterion>

<criterion id="H1R1-AC5" cell_refs="LT-h-1" judgment="true"/>

<expected_criteria>H1R1-AC1, H1R1-AC2, H1R1-AC3, H1R1-AC4, H1R1-AC5</expected_criteria>

**Every mechanical criterion above reads FAIL at the cut** (its input does not exist yet) **except where the issuance commit message records otherwise.** **H1R1-AC5, for `3.0.0_SA_CVO` at L9 (no verdict from you):** the manifest is compiled from the tree (no wall clock in its bytes) and the README states the never-overwrite rule and the identity key.

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
workflows/legacy_transform/run_home.py
workflows/legacy_transform/README.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.1, round-1 cell `LT-h-1` (sections 3 and 10).
<owned_cells>LT-h-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `H1R1-AC1`, `H1R1-AC2`, `H1R1-AC3`, `H1R1-AC4`, `H1R1-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-h-1-r1.run-home-diff.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> H1R1-AC1,H1R1-AC2,H1R1-AC3,H1R1-AC4,H1R1-AC5 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-h-1-r1.run-home-diff.md` BEFORE the `complete` flip.
Result file `run-home-diff.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`H1R1-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
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

Seating: slot ~2, level 0. Round 1 of LGIC_LGCTFM, the first issuance on decomposition v1.1 (v1 @686d196fa1 plus s.10), issued by `2.0.0_SA_COO~G`. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py, PLANTED_CONTRACT.json, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json). Rulings carried: R-16, R-17, R-24.
