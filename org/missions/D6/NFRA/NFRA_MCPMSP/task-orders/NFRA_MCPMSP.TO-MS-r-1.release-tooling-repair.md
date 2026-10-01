# NFRA_MCPMSP task order -- `MS-r-1` -- ROUND 2, E5: batch repair of the gateway release tooling (R-4, R-5)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-r-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~5</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant.
comp-adversary: DECLARED-NOT-APPLICABLE -- tooling; AC2 runs only behind its own safety guard.
EGRESS CLASS, declared: none (no deploy is run; git reads of the nested mcportal repo only).
</preflight>

## 1. THE CELL -- `MS-r-1` (decomposition v2, R2.2)

Two defects that stopped round 1's release:
1. **R-4 (`infra/aws/ec2/opal-gateway/deploy-to-ec2.sh` `:146-176`):** the dashboard is built from
   `$WORKSPACE_ROOT/mcportal` at ITS checked-out HEAD, but the workspace `mcportal` gitlink is `fa1ff9693b` (README
   only) while `infra/aws/ec2/EC2_MANIFEST.json` `services.opal-gateway.mcportal_commit` is `a3bff71ffa`. Fix: resolve
   the manifest's `mcportal_commit`; if the workspace checkout's HEAD is not it (or has no `package.json`), build from a
   detached checkout of that commit (`git -C <mcportal repo> worktree add --detach <tmp> <commit>`, removed afterwards)
   -- fail closed if the commit is absent. Add **`MCPORTAL_RESOLVE_ONLY=1`**: resolve, print exactly one line
   `MCPORTAL-RESOLVED: <dir> @<commit>`, and `exit 0` BEFORE any build, `aws`, `ssh`, `scp` or upload line (the check
   refuses to execute the script unless that exit sits before the first such line).
2. **R-5 (new `infra/aws/ec2/opal-gateway/tests/run_release_suites.sh`):** runs the named gateway suites (`$@`, pytest
   paths) with `AUDIT_PATH` pointed at a fresh temp file, so a narrow release tree (whose `tests/conftest.py` lacks the
   temp-audit fixture) never dirties the TRACKED `audit.jsonl`; exits with pytest's code.

## 2. BOUNDS

1. Write surface: those two files. Change no other deploy behaviour; `deploy-to-ec2.sh`'s `.env` printf is MS-d-2's.
2. NEVER run `deploy-to-ec2.sh` without `MCPORTAL_RESOLVE_ONLY=1` -- that would deploy. No push, no vendor call
   (no `bun install` here). REFUSE a criterion you cannot meet.

## 3. SURFACES

<paths>
infra/aws/ec2/opal-gateway/deploy-to-ec2.sh
infra/aws/ec2/opal-gateway/tests/run_release_suites.sh
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~5/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/ec2/EC2_MANIFEST.json`, `mcportal` (nested repo, git reads only),
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W5-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-r-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/r1.AC1.sh; echo "exit=$?"</invocation><expect>suite (tests/test_mcpmsp_asker_firm.py, --noconftest): N passed (N >= 1), 0 failed; tracked audit.jsonl unchanged=yes -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-r-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/r1.AC2.sh; echo "exit=$?"</invocation><expect>resolve line: MCPORTAL-RESOLVED: dir @a3bff71ffa... (count=1, rc=0); manifest mcportal_commit matches; build/upload lines=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~5/NFRA_MCPMSP.TO-MS-r-1.release-tooling-repair.proof_of_spec.json`.
Report once, with: the two check lines; the commit hash; any row. Then STOP: this slot continues with MS-d-2.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 issuance (E5, batch repair; worker-light per report 2 C7). Sibling check at the cut: no open
order of another project names `deploy-to-ec2.sh` or `tests/run_release_suites.sh`. Checks dry-run at base: AC1 FAIL
as expected (script absent); AC2 FAIL as expected (flag undeclared, NOT executed -- the guard held).

<status>complete</status>
<round>2</round>
<slot>~5</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
