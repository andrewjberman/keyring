# NFRA_MCPORTAL task order -- `MP-pc-1` -- WORKSTREAM PC ROUND 1: the git-state refusal field reads three states (G1, gateway half)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-pc-1</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-pc-1</to_id>
<issued_to>0.9.0_WK_NFRA_MCPORTAL~20</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a request handler; no cron, alarm or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the handler's one S3 get per box is unchanged.
comp-adversary: DECLARED-NOT-APPLICABLE -- the three state tests and the unchanged bound test are the adversary arms.
EGRESS CLASS, declared: none. Every store read in a test is a fake client.
</preflight>

## 1. THE CELL -- `MP-pc-1` (workstream PC round 1, decomposition sections PC.1 and PC.2)

Your worktree is `C:/tmp/mp-pc-20` (branch `wk-NFRA_MCPORTAL-pc-20`). Work and commit only there.

The Control Plane's Git state panel shows, per box, whether the box's newest integrate pass was refused. The handler
`infra/aws/ec2/opal-gateway/app/admin_fabric_gitstate.py` reads ONE pointer object per box,
`box=<B>/last_integrate.json` = `{"at", "rc", "note"}`, in `_refused(client, box)` (about `:173-182`). Today rc == 0 and
"no pointer" both read the string "not recorded", so a box whose newest integrate pass SUCCEEDED looks the same as a box
with no record at all. That is the defect (row Z-C-S31). A parallel cell changes the page to match, so build exactly this
shape and do not rename a field.

Change `_refused` and the per-box basis so each box reads one of three states:

| pointer | `integration_refused` | `integration_refused_basis` |
|---|---|---|
| present, rc != 0 | `{"refused": true, "at": "<at>", "note": "<note>"}` | `"refused: the box's newest integrate pass, read from its last_integrate.json pointer, failed with rc <rc>."` |
| present, rc == 0 | `{"refused": false, "at": "<at>"}` | `"no: the box's newest integrate pass, read from its last_integrate.json pointer, succeeded."` |
| absent (404 / NoSuchKey) | `"not recorded"` | `"not recorded: no integrate pass has been recorded for this box since the pointer began on 2026-10-13."` |

- `integration_refused_basis` is PER BOX: it is set beside `integration_refused` in both places the box dict is built
  (about `:241-242` and `:256-257`), and it names the state that applies to THAT box. Replace the one module-level
  `_REFUSED_BASIS` string with what the table needs.
- A read failure other than absent still raises to the module's existing 503 arm. Do not catch it.
- Keep the bound: exactly ONE get per box, and no history key read. The existing tests
  `test_refused_fetch_count_equals_box_count_at_1x_and_10x` and `test_refused_reads_no_window_body` must still pass.
- Update the module docstring's lines that describe the old two-state rule (about `:14-16`).
- In `infra/aws/ec2/opal-gateway/tests/test_admin_fabric_gitstate.py`: the existing tests
  `test_pointer_rc_nonzero_reads_at_and_note` and `test_pointer_rc_zero_or_absent_reads_not_recorded` assert the old
  shape. Change them to the new shape (rc != 0 now carries `"refused": true`; rc == 0 now reads `{"refused": false,
  "at": ...}`). Add these four tests, by these exact names:
  - `test_refused_rc_zero_reads_no_with_at`: a planted pointer with rc 0 reads `{"refused": false, "at": "<its at>"}`.
  - `test_refused_rc_nonzero_reads_refused_with_at_and_note`: rc 3 reads `{"refused": true, "at", "note"}`, the note
    carried through.
  - `test_refused_no_pointer_reads_not_recorded`: no pointer object reads the string `"not recorded"`.
  - `test_refused_basis_names_the_state_that_applies`: three boxes, one per state, in ONE response. Each box's
    `integration_refused_basis` starts with `"refused:"`, `"no:"` or `"not recorded:"` respectively, and the refused
    box's basis names its rc.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. Do not change any other `app/` module, `app/admin_api.py` included,
   Terraform, the manifest, the producer `.tools/fabric-gitstate.py`, or anything in `mcportal/`. Make no deploy and no
   AWS call.
2. Standing rules: no push and no vendor call. Commit via `.tools/safe-commit.sh` with your serial as author (CLAUDE.md
   14a). If you cannot meet a criterion as written, REFUSE it with its measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/app/admin_fabric_gitstate.py
infra/aws/ec2/opal-gateway/tests/test_admin_fabric_gitstate.py
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~20/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: every other `infra/aws/ec2/opal-gateway/app/` module, `.tools/fabric-gitstate.py` (the pointer's
writer, for its shape), and `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-W20-S<k>` (the next free k for W20). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an
ARMED row is `2.0.0_SA_COO~MP`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-pc-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/pc/checks/pc1.AC1.sh; echo "exit=$?"</invocation><expect>gitstate three states: 0 failed; named tests PASSED 5 of 5 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.9.0_WK_NFRA_MCPORTAL~20/NFRA_MCPORTAL.TO-MP-pc-1.gitstate-three-states.proof_of_spec.json`.
Report once, with:
- the check output;
- the commit hash;
- the old tests you changed, and how;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the PC issuance (decomposition v9) from the C17 round-2 analysis @d0dd3f0964 ruling 1 (row
Z-C-S31) and PRD v0.8 @7da54894cf. Check dry-run at base 9be88c9134: AC1 FAIL (named tests PASSED 1 of 5; the one
existing bound test passes, which is the control that the file runs). One criterion: the cell is the built behaviour; the
seam to the page is the fixed PC.2 shape, graded at the release. Lives through MP-pc-5.

<status>pending</status>
<round>1</round>
<workstream>PC</workstream>
<slot>~20</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
