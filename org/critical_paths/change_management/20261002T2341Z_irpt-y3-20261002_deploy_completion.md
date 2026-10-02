# Deploy Completion Record
**Date opened:** 2026-10-02T23:41:35.136765+00:00
**Status:** OPEN
**Deploy:** Y-3 (ruling 4) + S284 journal: the resident (st14 -> st15) and irpt-ycharts-generate at 9bbb38f7a0 -- a named ETF as a comparison key
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-ycharts-generate.zip new version at 9bbb38f7a0 | read back by version, sha equal; census vs live wjSX3zZo; cold-start smoke | irpt-ycharts-generate.zip version jFLj0wX5E0cybH52ZTxSVdVApAoNIypy (23:45:00Z, 584914 bytes) read back sha256 VZvhvWRMqD6mdaF8COT5JcUcnMxdvzCJe82Gs/9cnRk= equal; staged rows all at 9bbb38f7a0; census vs live wjSX3zZo: identical 104, changed 9 (Y-3's six + security_resolution gated + HoldingsSnapshot schema + report.pdf EOL), added 0, removed 0 (Y3/census_irpt-ycharts-generate_y3.json); cold-start smoke PASS on 3 routes | CLOSED 20261002T234754Z |
| U2 | s3-prefix | irpt-resident-9bbb38f7a0-st15.tar.gz and its install script | both keys 404 before, read back by version, sha equal; gate G1-G5 | both keys 404 before; tar irpt-resident-9bbb38f7a0-st15.tar.gz version Cs1gMHYpJVcbzk2X3fP7cDdree7b5y89 782217 bytes sha256 af49e702..; script version ELQvAnfndlcYl6Z.I4o1JnBHGq3iuKFC 8683 bytes sha256 1a282fd4..; both read back equal; gate G1-G5 PASS, G5 vs running st14: changed 10, added 0, removed 0 (Y3/GATE_OUTPUT_Y3_RESIDENT_20261002.txt) | CLOSED 20261002T234953Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_ycharts_generate.aws_lambda_function.this | CodeSha256 read back equal to the built zip |  | OPEN |
| D2 | activation | resident install via SSM (root 9bbb38f7a0-st15) | running root, member digests, unit active, queue 0/0 |  | OPEN |
| V1 | verify | a Multi-Comp vs ULT + IWM on a fund-free upload, solo gate | submission admits IWM; one identity read verified; READY naming IWM |  | OPEN |

## Log

- 20261002T234135Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261002T234754Z LEG U1 closed: irpt-ycharts-generate.zip version jFLj0wX5E0cybH52ZTxSVdVApAoNIypy (23:45:00Z, 584914 bytes) read back sha256 VZvhvWRMqD
- 20261002T234953Z LEG U2 closed: both keys 404 before; tar irpt-resident-9bbb38f7a0-st15.tar.gz version Cs1gMHYpJVcbzk2X3fP7cDdree7b5y89 782217 bytes sha
