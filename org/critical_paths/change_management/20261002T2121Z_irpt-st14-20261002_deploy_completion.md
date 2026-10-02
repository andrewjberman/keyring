# Deploy Completion Record
**Date opened:** 2026-10-02T21:21:55.578005+00:00
**Status:** OPEN
**Deploy:** st14 (row S279): the resident and irpt-ycharts-generate at f89fc8e731 -- a fund ticker no longer fails the whole upload
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-ycharts-generate.zip new version at f89fc8e731 | read back by version, sha equal; census vs live E+FqSWwE | irpt-ycharts-generate.zip version y3LRNAoPvGmdWYZSNb5moyTiEDvo8055 (21:23:07Z, 582443 bytes) read back sha256 wjSX3zZoFu2EUintXwZVESW+ac8F+bdRHSWm+YfpmgA= equal; 113 members, staged rows all at f89fc8e731; census vs live E+FqSWwE: identical 99, eol_only 14, changed 13, added 1 (report_owner.py), removed 0 (ST14/census_irpt-ycharts-generate_st14.json); cold-start smoke PASS on 3 routes (ST14/ZIP_COLD_START_SMOKE_ST14_20261002.txt) | CLOSED 20261002T213059Z |
| U2 | s3-prefix | irpt-resident-f89fc8e731-st14.tar.gz and its install script | both keys 404 before, read back by version, sha equal | both keys 404 before; tar irpt-resident-f89fc8e731-st14.tar.gz version 4N3RhbITXo1u1zIsLkPbc0oYYWNCUVYE, 777996 bytes, sha256 4d317c00..; install script version 9GcYA4bLxx_gIvS_Vq4fYf0YX8mL.fVg, 8687 bytes, sha256 430d4172..; both read back by version equal; gate G1-G5 PASS (ST14/GATE_OUTPUT_ST14_20261002.txt) | CLOSED 20261002T213215Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_ycharts_generate.aws_lambda_function.this | CodeSha256 read back equal to the built zip |  | OPEN |
| D2 | activation | resident install via SSM (root f89fc8e731-st14) | running root, member digests, unit active, queue 0/0 |  | OPEN |
| V1 | verify | Y-1 Case A first lookup on st14, spaced, solo gate | IRPT_RESIDENT_RESOLVE_FUNDS matched>=1, NORMALIZED with M:TIMXX; no WAF challenge |  | OPEN |

## Log

- 20261002T212155Z OPENED by 2.0.0_SA_COO~Y with 5 leg(s)
- 20261002T213059Z LEG U1 closed: irpt-ycharts-generate.zip version y3LRNAoPvGmdWYZSNb5moyTiEDvo8055 (21:23:07Z, 582443 bytes) read back sha256 wjSX3zZoFu
- 20261002T213215Z LEG U2 closed: both keys 404 before; tar irpt-resident-f89fc8e731-st14.tar.gz version 4N3RhbITXo1u1zIsLkPbc0oYYWNCUVYE, 777996 bytes, s
