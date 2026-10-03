# Deploy Completion Record
**Date opened:** 2026-10-03T02:31:20.064502+00:00
**Status:** OPEN
**Deploy:** Y-4 the check gate: the resident (st16 -> st17), irpt-ycharts-generate at 828c37c6f7, and the runner role's read of the estate Kimi key (ledger opened 02:3xZ, AFTER the U1 upload: the first open was refused on an invalid leg kind and the build proceeded -- recorded, not hidden)
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-ycharts-generate.zip at 828c37c6f7 from an autocrlf=false checkout | read back; members equal git; census vs live aug0YyWc; cold-start smoke | irpt-ycharts-generate.zip version w2yfeweDcOFLnVFLFidK1_VCv5EFPCmb (02:28:23Z, 588963 bytes) sha256 fD2R6OFrT2N086C9Go3e1aA9RKZCP/vfnZCaHCloJTs=; LF checkout: 114 members, 113 equal git show 828c37c6f7 by the census + kimi_port.py (newly registered in files[], parity check ADHC_DRIFTD.002) byte-equal by direct read; 0 CRLF; vs live aug0YyWc: identical 110, changed 3 (resident_worker, upload_resolution, uploads), added kimi_port.py; cold-start smoke PASS on 3 routes | CLOSED 20261003T023120Z |
| U2 | s3-prefix | irpt-resident-828c37c6f7-st17.tar.gz and its install script | both keys 404 before, read back; gate G1-G5 | both keys 404 before; tar irpt-resident-828c37c6f7-st17.tar.gz version HvfsVMjjD9_YdfKgEXXevpjBDiR321Ux 787331 bytes sha256 213c2ebd..; script version uyayvbDZy_BZXx5rUoshEVXp2knZ6jeq 8683 bytes sha256 d1f7f89d..; both read back equal; gate G1-G5 PASS, G5 vs running st16: changed 5, added 2 (kimi_port.py, upload_suggestions.py), removed 0 | CLOSED 20261003T023357Z |
| D3 | activation | ONE targeted safe-apply of aws_iam_role_policy.runner_resident (Sid ReadTheEstateKimiKey) | policy read back with the one statement |  | OPEN |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_ycharts_generate.aws_lambda_function.this | CodeSha256 read back |  | OPEN |
| D2 | activation | resident install via SSM (root 828c37c6f7-st17) | running root, digests, unit active, queue 0/0 |  | OPEN |
| V1 | verify | after option A: the typo file from the page | row 2 APPL offered AAPL (verified); accepted -> NORMALIZED; READY |  | OPEN |

## Log

- 20261003T023120Z OPENED by 2.0.0_SA_COO~Y with 6 leg(s)
- 20261003T023120Z LEG U1 closed: irpt-ycharts-generate.zip version w2yfeweDcOFLnVFLFidK1_VCv5EFPCmb (02:28:23Z, 588963 bytes) sha256 fD2R6OFrT2N086C9Go3e
- 20261003T023357Z LEG U2 closed: both keys 404 before; tar irpt-resident-828c37c6f7-st17.tar.gz version HvfsVMjjD9_YdfKgEXXevpjBDiR321Ux 787331 bytes sha
