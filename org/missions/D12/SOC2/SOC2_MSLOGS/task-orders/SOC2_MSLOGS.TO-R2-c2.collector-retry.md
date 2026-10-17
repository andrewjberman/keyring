# TO SOC2_MSLOGS.TO-R2-c2 -- the collector's async retry is 0

<to_id>SOC2_MSLOGS.TO-R2-c2</to_id>
<project>SOC2_MSLOGS</project>
<issued_to>0.9.0_WK_SOC2_MSLOGS~11</issued_to>
<issued_by>2.0.0_SA_COO~S1</issued_by>
<issued_date>2026-10-17</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Risk note:** WORLD only by the gate's path floor (a Terraform file is in `<paths>`); the cell applies nothing. The release applies it.

**Directive:** D12 | **Fabric:** dell1 | **Decomp cell:** `SM-c-2` (`decompositions/SOC2_MSLOGS_DECOMP_R2.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`SM-c-2`. An asynchronous Lambda invoke that fails or times out is retried by the service (twice by default) with the SAME event, which re-runs it on whatever code is then deployed. Round 1 saw a timed-out collector fire re-invoked five times on old code. The collector is invoked
asynchronously by EventBridge (hourly) and by the door's `recollect` (`InvocationType="Event"`), so both paths are covered by one function-level setting. A missed fire is repaired by the next hourly fire and by `recollect`; a silent re-run on old code is not wanted.

READ first: `infra/aws/terraform/trino/collector.tf` (the `aws_lambda_function.collector` resource and the file's header).

BUILD: add to `collector.tf`
```
resource "aws_lambda_function_event_invoke_config" "collector" {
  function_name          = aws_lambda_function.collector.function_name
  maximum_retry_attempts = 0
}
```
with a two-line comment above it saying why (a timed-out or failed asynchronous fire is never re-run on old code; the next hourly fire and `recollect` repair it). No `qualifier` (it covers the unqualified function). Nothing else in the file changes. DESIRED only: you apply nothing.

### ACCEPTANCE

<criterion id="R2-c2-AC1" cell_refs="SM-c-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py retry</invocation><expect>R2-RETRY-OK</expect></criterion>
`R2-c2-AC1` -- `collector.tf` carries an event invoke config for the collector with `maximum_retry_attempts = 0` and no qualifier.

<criterion id="R2-c2-AC2" cell_refs="SM-c-2"><invocation>python org/tier1_exec/2.0.0_SA_COO~S1/deliverables/SOC2_MSLOGS_R2_CHECKS/s1_check_r2.py tfvalidate</invocation><expect>R2-TFVALIDATE-OK</expect></criterion>
`R2-c2-AC2` -- `terraform validate` succeeds on a scratch copy of the trino root (the round-1 dependency cycle between the door and the collector came through an unvalidated Terraform cell). This check PASSES at the base and must still pass.

<expected_criteria>R2-c2-AC1,R2-c2-AC2</expected_criteria>

Dry-run at the base 2026-10-17 ~06:2xZ: AC1 `R2-RETRY-REFUSED collector.tf has no aws_lambda_function_event_invoke_config ...` FAIL as expected; AC2 `R2-TFVALIDATE-OK` PASS as expected (a control). Run from the repository (worktree) root; AC2 takes about 10 seconds and needs `terraform` on the path.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else you READ and never edit.
- **NOTHING is applied and NOTHING is called live.** No `terraform apply`, no `terraform plan` against the account, no AWS call. The check's `terraform init -backend=false` and `validate` run on a scratch copy in a temp directory.
- `access.tf`, `main.tf`, `identity.tf` are not yours.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id `SOC2_MSLOGS-D1-W11-S<k>`, `surfaced_at` = `date -u +%FT%TZ`), and do not weaken a check to pass it.
- Commit only through `.tools/safe-commit.sh` with `--author "0.9.0_WK_SOC2_MSLOGS~11 <0.9.0_WK_SOC2_MSLOGS~11@opal.agent>"`, `-F` a message file you write with the Write tool, and `-- <paths>`.

<paths>
infra/aws/terraform/trino/collector.tf
org/missions/D12/SOC2/SOC2_MSLOGS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D12/SOC2/SOC2_MSLOGS/decompositions/SOC2_MSLOGS_DECOMP_R2.md</decomp_doc> (round 2), cell `SM-c-2`.
<owned_cells>SM-c-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: R2-c2-AC1, R2-c2-AC2. Instance at `org/missions/D12/SOC2/SOC2_MSLOGS/deliverables/0.9.0_WK_SOC2_MSLOGS~11/SOC2_MSLOGS.TO-R2-c2.collector-retry.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> R2-c2-AC1,R2-c2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two check lines, `terraform fmt -check infra/aws/terraform/trino/collector.tf` rc, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the schedule is unchanged; the live retry setting is read back at the release.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- one Terraform resource with no principal or data path; the regex and validate checks grade it.
lane: the <paths> block IS the grant.
</preflight>

Source: the CTO's round-1 analysis section 3 item 4 (@843819d1ab) and section 2 (`terraform validate` as a standing criterion); decomposition round 2 cell SM-c-2.
