# Deploy Completion Record
**Date opened:** 2026-10-03T04:54:47.714630+00:00
**Status:** OPEN
**Deploy:** Y-4 enrichment (CTO batch 199): the check gate's per-upload total (240 s) on the resident (st17 -> st18) and the runner's exact Kimi secret resource
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U2 | s3-prefix | resident tar and install script for root <pin>-st18 | both keys 404 before, read back by version; gate G1-G5 | both keys 404 before (04:59:03Z); irpt-resident-a6f6e7165e-st18.tar.gz VersionId UnePbYDlYpd7nsLpRd8Lpi4WqJ8rUzOV 790317 bytes sha256 ff1ce55b..; resident_host_install_a6f6e7165e-st18.sh VersionId g6Lx_XPK5_QL3qwUNmVI4.37nsFqUGxt 8685 bytes sha256 a44b5579..; both read back by version equal; gate G1-G5 PASS (Y4E/GATE_OUTPUT_Y4E_RESIDENT_20261003.txt) | CLOSED 20261003T050117Z |
| D3 | activation | ONE targeted safe-apply of aws_iam_role_policy.runner_resident (ReadTheEstateKimiKey resource narrowed) | policy read back; IAM simulation: exact secret allowed, a sibling name denied |  | OPEN |
| D2 | activation | resident install via SSM (root <pin>-st18) | running root, digests equal git, unit active, queue 0/0 |  | OPEN |
| V1 | verify | journal and IAM after D2+D3 | the installed worker carries the new SUGGEST line; the live typo run rides irpt-y4-20261003 V1 after option A |  | OPEN |

## Log

- 20261003T045447Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20261003T050117Z LEG U2 closed: both keys 404 before (04:59:03Z); irpt-resident-a6f6e7165e-st18.tar.gz VersionId UnePbYDlYpd7nsLpRd8Lpi4WqJ8rUzOV 790317
