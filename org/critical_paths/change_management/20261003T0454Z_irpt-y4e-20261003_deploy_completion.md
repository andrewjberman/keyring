# Deploy Completion Record
**Date opened:** 2026-10-03T04:54:47.714630+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261003T051930Z
**Deploy:** Y-4 enrichment (CTO batch 199): the check gate's per-upload total (240 s) on the resident (st17 -> st18) and the runner's exact Kimi secret resource
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | resident tar and install script for root <pin>-st18 | both keys 404 before, read back by version; gate G1-G5 | both keys 404 before (04:59:03Z); irpt-resident-a6f6e7165e-st18.tar.gz VersionId UnePbYDlYpd7nsLpRd8Lpi4WqJ8rUzOV 790317 bytes sha256 ff1ce55b..; resident_host_install_a6f6e7165e-st18.sh VersionId g6Lx_XPK5_QL3qwUNmVI4.37nsFqUGxt 8685 bytes sha256 a44b5579..; both read back by version equal; gate G1-G5 PASS (Y4E/GATE_OUTPUT_Y4E_RESIDENT_20261003.txt) | CLOSED 20261003T050117Z |
| D3 | activation | ONE targeted safe-apply of aws_iam_role_policy.runner_resident (ReadTheEstateKimiKey resource narrowed) | policy read back; IAM simulation: exact secret allowed, a sibling name denied | ROLLED BACK per CTO half batch 206's condition: D3 applied 05:1xZ (Resource read back astn/kimi/api-key-??????) but the after-simulation read the sibling name ALLOWED, matched by iam.tf ReadYChartsAndSharedVisionSecrets (local.kimi_secret_arn = astn/kimi/api-key-*, inline policy irpt-ycharts-runner). Rollback: targeted safe-apply rc=0 restoring *, read back 05:18:31Z; simulation equals the before-read (Y4E/D3_ROLLBACK_READBACK_20261003.txt) | CLOSED 20261003T051929Z |
| D2 | activation | resident install via SSM (root <pin>-st18) | running root, digests equal git, unit active, queue 0/0 | NOT LANDED: the half is both-or-neither and D3 rolled back; running root read 828c37c6f7-st17 at 05:18Z, queue 0/0; the st18 tar and script stay in S3 unused | CLOSED 20261003T051929Z |
| V1 | verify | journal and IAM after D2+D3 | the installed worker carries the new SUGGEST line; the live typo run rides irpt-y4-20261003 V1 after option A | NOT RUN: nothing landed; the state equals the before-read (policy *, root st17). Re-packet routed to 1.0.0_SA_CTO | CLOSED 20261003T051930Z |

## Log

- 20261003T045447Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20261003T050117Z LEG U2 closed: both keys 404 before (04:59:03Z); irpt-resident-a6f6e7165e-st18.tar.gz VersionId UnePbYDlYpd7nsLpRd8Lpi4WqJ8rUzOV 790317
- 20261003T051929Z LEG D3 closed: ROLLED BACK per CTO half batch 206's condition: D3 applied 05:1xZ (Resource read back astn/kimi/api-key-??????) but the 
- 20261003T051929Z LEG D2 closed: NOT LANDED: the half is both-or-neither and D3 rolled back; running root read 828c37c6f7-st17 at 05:18Z, queue 0/0; the 
- 20261003T051930Z LEG V1 closed: NOT RUN: nothing landed; the state equals the before-read (policy *, root st17). Re-packet routed to 1.0.0_SA_CTO
- 20261003T051930Z CLOSED -- all 4 legs proven
