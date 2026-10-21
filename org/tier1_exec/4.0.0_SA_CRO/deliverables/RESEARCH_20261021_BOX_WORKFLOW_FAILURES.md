# RESEARCH 2026-10-21 -- the box/* GitHub Actions failures (lambda-deploy.yml, ec2-deploy.yml)

**Seat:** 4.0.0_SA_CRO (laptop) | **Asked by:** the human at the dell1 terminal, relayed by 0.0.0_AB_MSTR msg 110123 (record
`org/tier0_exec/0.0.0_AB_MSTR/logs/2026-10-21/relayed_ask_dell1_terminal_cro_box_workflow_failures_1456Z.md`, msg 110124).
Read-only: nothing was disabled, edited or deleted.

## Answer

The two workflows fail because GitHub cannot parse them. The DEV branch is not the cause. Each declares both `paths:` and
`paths-ignore:` under the same `push` event, and GitHub rejects that pair. A workflow file that does not parse produces a failed,
zero-job run on every push to every branch: the `branches: [DEV]` filter is never evaluated, so the failures land on CLOUD and
every box/*, not only box/*.

## Measured (gh CLI and API, 2026-10-21 ~15:0xZ)

- Newest lambda-deploy.yml run, 39621316334 (box/dell2): "This run likely failed because of a workflow file issue". The run is
  named by its file path, not by its `name:`, and has 0 jobs.
- Static lint of all 9 files in `.github/workflows/`: exactly these two carry `paths` together with `paths-ignore`
  (`lambda-deploy.yml:19-34`, `ec2-deploy.yml:15-25`). The other seven parse.
- Runs 11:00Z-14:10Z today: lambda-deploy 101 and ec2-deploy 101. The relay says 98 each between 11:04Z and 14:09Z; the window
  edges differ.
- Last 1,000 ec2-deploy runs: all failure, 2026-10-20 05:21Z to 2026-10-21 14:56Z. By branch: CLOUD 198, box/dell1 236,
  box/sitez 220, box/laptop 180, box/dell2 164, other 2.
- Totals:

| Workflow | Runs ever | Successes ever | Last success |
|---|---|---|---|
| ec2-deploy.yml | 27,791 | 0 | never |
| lambda-deploy.yml | 27,777 | 12 | 2026-02-21, on DEV |

- The pair dates from c3474bf157c (2026-02-20, "Tighten CI/CD workflow triggers"), the day the estate went Terraform-only
  (ac285c3984, "kill CI/CD auto-deploy").
- Origin has no DEV, PROD or main branch; CLOUD is the only trunk. Even a parseable file would never fire on DEV.

## Correction to the relay's inference

"They burn Actions minutes": a run that fails at parse starts no job, so it runs no runner. Inferred, not measured on the billing
page. The real cost is noise: a red X on every push to every branch, which hides real failures.

## Recommendation

1. **Now, and reversible:** `gh workflow disable lambda-deploy.yml` and `gh workflow disable ec2-deploy.yml`. This is a
   repo-wide setting; it stops the runs at once and touches no branch.
2. **Then delete both files on CLOUD.** They are obsolete:
   - both trigger only on a DEV branch that does not exist;
   - ec2-deploy has never succeeded;
   - deploys have been Terraform and ledger only since 2026-02-20.
   Do NOT "fix" ec2-deploy.yml by retargeting it to CLOUD: once parseable, it would deploy to EC2 over SSM on every CLOUD push,
   outside safe-apply and the deploy ledger.

## Separate finding: six other workflows fail for real (CLOUD only)

These parse, run and fail in a step. Their owners need to look; no row was filed.

| Workflow | Last success | Failing step |
|---|---|---|
| comp-tool-tests | 2026-07-11 | the scoped comp-tool test suite |
| shared-infra-drift | 2026-07-11 | the resource-map drift check |
| lib-vendored-copies-parity | 2026-08-03 | vendored copy == canonical lib/ |
| inf-pipeline-lib-parity | never | lib parity, and bronze write-key == read-key |
| trigger-map-drift | never | two-service census |
| stitch-source-push | 2026-10-19 | portal checkout; 10 of its last 20 runs failed |
