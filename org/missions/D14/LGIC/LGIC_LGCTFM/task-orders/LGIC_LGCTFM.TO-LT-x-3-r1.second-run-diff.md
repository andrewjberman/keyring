# TO LGIC_LGCTFM.TO-LT-x-3-r1 -- the second run after a practice wave, and the diff a reader can use without opening either run

<to_id>LGIC_LGCTFM.TO-LT-x-3-r1</to_id>
<project>LGIC_LGCTFM</project>
<issued_to>0.9.0_WK_LGIC_LGCTFM~2</issued_to>
<issued_by>2.0.0_SA_COO~G</issued_by>
<issued_date>2026-09-17</issued_date>
<status>complete</status>

**Directive:** D14 | **Fabric:** laptop | **PRD:** `../prd/LGIC_LGCTFM_PRD.md` v1.4 (ADMITTED; both halves current) | **Decomp cell:** `LT-x-3` (decomposition v1.1) | **outcome_ref:** FWD-8 | **depends_on:** LT-x-1 (same slot; the second run needs a first)

---

## WORKER FACE

### THE CELL

`LT-x-3` (PRD T12, DEC-12). **You write a second run under `workflows/legacy_transform/blackdiamond-49financial/` and its `DIFF.md`, and file one row per OPENED tension in ADVI_FIRMBKTS's channel.** You edit no code.

1. **A practice wave** (Rule 27: never waited for): in a scratch linked worktree on a scratch branch, never pushed, make one small change that a migration would make and that the walk can see (for example a DECLARE: a declaration entry that closes a LIVE-no-DECLARED tension; or a mark), and produce the second run there with `python lib/opal_lgctfm.py run ...`. Copy that run directory into the subject directory here; delete the scratch worktree.
2. **The diff.** `python workflows/legacy_transform/run_home.py diff <first run dir> <second run dir>` -> commit its output verbatim as `DIFF.md` inside the second run directory. It must show at least one CLOSED or OPENED tension -- a wave that moves nothing exercises nothing.
3. **A NEW tension is a row (DEC-12):** for each OPENED tension, append one row to `org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md` in that channel's own row shape, id `ADVI_FIRMBKTS-W<n>-S<k>` with the same one-above-the-highest rule.

**Read:** `org/missions/D14/LGIC/LGIC_LGCTFM/prd/LGIC_LGCTFM_PRD.md` DEC-12 and T12; `workflows/legacy_transform/README.md`; the ADVI_FIRMBKTS channel's existing rows (for the shape).

### ACCEPTANCE

<placeholders>WS</placeholders>

<criterion id="X3R1-AC1" cell_refs="LT-x-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x3-two-runs</invocation><expect>PASS-X3-TWO-RUNS-ON-ONE-SUBJECT</expect></criterion>

<criterion id="X3R1-AC2" cell_refs="LT-x-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x3-diff</invocation><expect>PASS-X3-COMMITTED-DIFF-REPRODUCES</expect></criterion>

<criterion id="X3R1-AC3" cell_refs="LT-x-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x3-nontrivial</invocation><expect>PASS-X3-WAVE-MOVED-SOMETHING</expect></criterion>

<criterion id="X3R1-AC4" cell_refs="LT-x-3"><invocation>cd <WS> && timeout 300 python org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/check_lt_r1.py x3-filed</invocation><expect>PASS-X3-OPENED-ROWS-FILED</expect></criterion>

<criterion id="X3R1-AC5" cell_refs="LT-x-3" judgment="true"/>

<expected_criteria>X3R1-AC1, X3R1-AC2, X3R1-AC3, X3R1-AC4, X3R1-AC5</expected_criteria>

**Every mechanical criterion above reads FAIL at the cut** (its input does not exist yet) **except where the issuance commit message records otherwise.** **X3R1-AC5, for `3.0.0_SA_CVO` at L9 (no verdict from you):** a reader who opens neither run learns from `DIFF.md` what closed, opened and stayed; the practice wave is described in the result file with the one change it made.

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
workflows/legacy_transform/blackdiamond-49financial/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D14/LGIC/LGIC_LGCTFM/decompositions/LGIC_LGCTFM_DECOMP.md</decomp_doc> v1.1, round-1 cell `LT-x-3` (sections 3 and 10).
<owned_cells>LT-x-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: `X3R1-AC1`, `X3R1-AC2`, `X3R1-AC3`, `X3R1-AC4`, `X3R1-AC5`. Instance at
`org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/0.9.0_WK_LGIC_LGCTFM~2/LGIC_LGCTFM.TO-LT-x-3-r1.second-run-diff.proof_of_spec.json`
(phase `BUILD-GENERAL`, firm `FABRIC`, spec_ref.group `OTHER`), validated with
`python .tools/proof-of-spec-check.py <instance> X3R1-AC1,X3R1-AC2,X3R1-AC3,X3R1-AC4,X3R1-AC5 --governing-order org/missions/D14/LGIC/LGIC_LGCTFM/task-orders/LGIC_LGCTFM.TO-LT-x-3-r1.second-run-diff.md` BEFORE the `complete` flip.
Result file `second-run-diff.r1.result.md` beside it. **Commit the artifact first, then pin it; never PENDING-THIS-COMMIT.**
`X3R1-AC5` is JUDGMENT: record `UNVERIFIABLE-BY-INSTRUMENT` with a `status_reason` naming `3.0.0_SA_CVO`; a PASS or FAIL there is invalid.
</proof_of_spec>

**REPORT:** your FINAL MESSAGE, once, in the `WORKER REPORT` shape. You cannot send or receive messages; anything you would ask is a surprise row.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the round-1 cut: read-only trigger reads, as LT-x-1.
comp-iam: DECLARED-NOT-APPLICABLE -- the practice wave is a repository change in a scratch worktree; no principal moves.
comp-adversary: DECLARED-NOT-APPLICABLE -- no external citation; the inputs are this estate's own records.
lane: the <paths> block is the grant (RULING 1 shape c); deliverables/<serial>/ is granted by the tree convention.
contention: ADVI_FIRMBKTS's investigations file is append-only and lane ANY; no other open order names it at the cut.
</preflight>

Seating: slot ~2, level 6. Round 1 of LGIC_LGCTFM, the first issuance on decomposition v1.1 (v1 @686d196fa1 plus s.10), issued by `2.0.0_SA_COO~G`. Fixed inputs: `org/missions/D14/LGIC/LGIC_LGCTFM/deliverables/2.0.0_SA_COO~G/fixed_inputs/r1/` (check_lt_r1.py, PLANTED_CONTRACT.json, FORK_CONTROLS.json v1.1, SUBJECT_CONTROL.json). Rulings carried: R-16, R-17, R-24.
