# Deploy Completion Record
**Date opened:** 2026-10-03T03:49:22.282056+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261003T043039Z
**Deploy:** irpt-status: W2-06 include=composition (CTO batch 165) with the Y-5 ops/status.py correction words attributed (CTO batch 198), code at ONE commit
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | s3-prefix | irpt-status.zip at the W2-06 pin from an autocrlf=false checkout | read back by version; members equal git; census vs live; cold-start smoke | s3 version 4CQOSM.R8WDlZQ.ts0HCSiH2JkA6jqQ8, 338660 bytes, read back by version with sha256 6VQejBfsI/P3mfAVSFjLt/ythlcxXxi12cy9hxXhKNg= equal to the build; built from an autocrlf=false checkout at ac1a847617 (row repin 2be7ff7a54); census vs live h7H7KgX1: 41 identical, 6 changed, 0 added, 0 removed, 0 differ from the pin, 0 CRLF; cold-start smoke PASS on 3 routes plus the owner-refusal arm (W206_STATUS/) | CLOSED 20261003T040841Z |
| D1 | tf-lambda | ONE targeted safe-apply of module.irpt_status.aws_lambda_function.this (ops root) | CodeSha256 read back; live empty-headers invoke | CTO half batch 204 (msg 104536) on blob 30daf0f28b; before-read 04:24:50Z h7H7KgX1, key latest 4CQOSM; re-plan 1 change; safe-apply rc=0; CodeSha256 6VQejBfsI/P3mfAVSFjLt/ythlcxXxi12cy9hxXhKNg= Successful 04:28:06Z; live empty-headers invoke 200, no FunctionError, CONTRACT_VERSION (W206_STATUS/D1_READBACK_20261003.txt) | CLOSED 20261003T043010Z |
| V1 | verify | live owned reads: plain unchanged, include=comparisons unchanged, include=composition answers the frozen request | reads recorded | w206_read_proof.py --compare on REQ-a69e5751.. and REQ-a1d9abc0.. (tenant cottonwood): plain and include=comparisons equal to before (4 of 4); include=composition and include=comparisons,composition answer with composition, 9 keys within AnalysisSubmissionRequest, required present, sha256 equal across the two reads per request; include=composition,composition still INVALID_INPUT (W206_STATUS/READS_AFTER_W206_20261003.json, V1_KEYS_VS_CONTRACT_20261003.txt) | CLOSED 20261003T043010Z |

## Log

- 20261003T034922Z OPENED by 2.0.0_SA_COO~Y with 3 leg(s)
- 20261003T040841Z LEG U1 closed: s3 version 4CQOSM.R8WDlZQ.ts0HCSiH2JkA6jqQ8, 338660 bytes, read back by version with sha256 6VQejBfsI/P3mfAVSFjLt/ythlcx
- 20261003T043010Z LEG D1 closed: CTO half batch 204 (msg 104536) on blob 30daf0f28b; before-read 04:24:50Z h7H7KgX1, key latest 4CQOSM; re-plan 1 change;
- 20261003T043010Z LEG V1 closed: w206_read_proof.py --compare on REQ-a69e5751.. and REQ-a1d9abc0.. (tenant cottonwood): plain and include=comparisons equ
- 20261003T043039Z CLOSED -- all 3 legs proven
