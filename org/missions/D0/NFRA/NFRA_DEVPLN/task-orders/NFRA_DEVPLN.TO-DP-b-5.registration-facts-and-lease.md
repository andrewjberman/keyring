# TO NFRA_DEVPLN.TO-DP-b-5 -- round 1 THREAD DP-b-5: registration facts (head, commits, DEV-overlap refusal) and the FAST-lease approval row

<to_id>NFRA_DEVPLN.TO-DP-b-5</to_id>
<project>NFRA_DEVPLN</project>
<issued_to>0.9.0_WK_NFRA_DEVPLN~1</issued_to>
<issued_by>2.0.0_SA_COO~DV</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>THREAD</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `DP-b-5` (`decompositions/NFRA_DEVPLN_DECOMP.round1.md`) | **outcome_ref:** FWD-1, FWD-3 |
**depends_on:** `DP-b-1` (same slot, same file; this order starts only after `DP-b-1` has drained and merged)

---

## WORKER FACE

### THE CELL

After `DP-b-1`, `.tools/open-calls.py` can write and read an `approval` row, but `head_sha` and `commits` are `null`, and nothing stops a feature branch that was cut from DEV (carrying every DEV commit
beneath its own) from being registered. A feature must be cut from the last PROD release so it carries only its own commits; the approval binds the branch head. And a live FAST lease's seat must be
able to write its feature's row already approved. Work in the portal repo checked out under `portal/` in your worktree (its `origin/DEV` and `origin/PROD` refs are present; do not fetch).

### BUILD

1. `add --kind approval` takes `--portal <portal repo path>` (required for this kind; without it: `APPROVAL-REGISTER result=REFUSED reason=portal-required`, rc 3). It reads the branch as `origin/<branch>`,
   else the local branch `<branch>`; neither: `reason=branch-not-found`. It computes (never takes as an argument) `head_sha` = the branch tip, `commits` = `git rev-list --count origin/PROD..<branch>`, and
   `overlap` = the number of commits in `origin/PROD..<branch>` that are ALSO in `origin/PROD..origin/DEV`. `commits` of 0 is refused (`reason=empty`). `overlap` above 0 is refused:
   `APPROVAL-REGISTER result=REFUSED reason=dev-overlap overlap=<n> commits=<m>`, rc 3, nothing written. Otherwise it writes the row with `head_sha` and `commits` and prints
   `APPROVAL-REGISTER result=OK row=<id> head_sha=<sha> commits=<n>`.
2. `add --kind approval --check-only ...` runs the same checks, prints the same `APPROVAL-REGISTER ...` line, writes nothing, and accepts any branch name (it skips the `cand/<box>/<slug>` name check).
3. `approval-lease --branch <b> --box ... --purpose ... --pages ... --class ... --how ... --portal <path> --lease-file <path>`: refuses unless the lease JSON has `mode` `FAST`, `expires_epoch` greater than now, and
   `seat` equal to `$OPAL_AGENT_SERIAL` (`APPROVAL-REGISTER result=REFUSED reason=lease-not-live`, rc 3); then the same portal checks as item 1; then writes the row already CLOSED:
   `decision` `approved`, `by` = `FAST lease <lease file basename>`, `ruled_by` `lease`, `ruling` = the lease path. `approval-status` then reads it `APPROVED valid=yes`.

### RULES FOR THIS CELL

Tests run in temporary git repositories and a temporary `--store-dir`, never against the live lists or S3 (use the same cluster-copy skip `DP-b-1` used). The real portal repo is read only, with git read commands. No push,
merge or rebase. No non-ASCII. Python standard library only; `ruff check` clean on the files you edit or add. If a branch name in a test is not `cand/<box>/<slug>`, use `--check-only`.
FOUND SOMETHING ODD OFF-TASK? Append ONE row to the investigation file named in `<paths>` (id `NFRA_DEVPLN-W1-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="DPb5-AC1" cell_refs="DP-b-5"><invocation>python .tools/tests/test_open_calls_register.py</invocation><expect>ok=True</expect></criterion>
`DPb5-AC1` -- you write this test; last line `OPEN-CALLS-REGISTER-TEST cases=<k>/<n> ok=True`. Cases: a branch cut from PROD with 2 own commits registers with `commits=2` and the computed head; a branch cut from DEV
is refused `dev-overlap` and writes nothing; a missing branch is refused; an empty branch is refused; no `--portal` is refused; a live lease for `$OPAL_AGENT_SERIAL` writes an APPROVED row; an expired lease, a lease
for another seat and a lease with `mode` `HOLD` are each refused and write nothing; `--check-only` writes nothing.

<criterion id="DPb5-AC2" cell_refs="DP-b-5"><invocation>python .tools/open-calls.py add --kind approval --check-only --project NFRA_DEVPLN --box dell1 --branch origin/wk-dsgn-irptv1-r25-61-prodcut --purpose x --pages x --class client-facing --how x --portal portal</invocation><expect>APPROVAL-REGISTER result=REFUSED reason=dev-overlap</expect></criterion>
`DPb5-AC2` -- the seam against the REAL portal repo and a real branch (+34 over DEV): refused for the DEV overlap, nothing written.
</proof_of_spec>

<expected_criteria>DPb5-AC1,DPb5-AC2</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`. Write the proof instance to
`org/missions/D0/NFRA/NFRA_DEVPLN/deliverables/0.9.0_WK_NFRA_DEVPLN~1/NFRA_DEVPLN.TO-DP-b-5.registration-facts-and-lease.proof_of_spec.json`, validate it with
`python .tools/proof-of-spec-check.py <instance> DPb5-AC1,DPb5-AC2`, and flip `<status>` to `complete` only when every mechanical criterion passes and the instance is VALID.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_DEVPLN/decompositions/NFRA_DEVPLN_DECOMP.round1.md</decomp_doc>
<owned_cells>DP-b-5</owned_cells>
</decomp_ref>

<paths>
.tools/open-calls.py
.tools/tests/test_open_calls_register.py
org/missions/D0/NFRA/NFRA_DEVPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
comp-iam: DECLARED-NOT-APPLICABLE the cell touches no IAM.
comp-adversary: DECLARED-NOT-APPLICABLE thread round; the lens runs on the enrichment round that touches its surface.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD `prd/NFRA_DEVPLN_PRD.md` v0.2 @d2b7385bee C-FEATURE, C-MERGE-FORWARD (iii), the CVO's refusal point 1 (review @2b616031b1). Issuer rulings R1, R2, R4 in the decomposition. Portal worktree: this order needs `--portal-ref` at the spawn.
