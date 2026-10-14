# Deploy Completion Record
**Date opened:** 2026-10-14T12:52:04.653506+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-bm-3: ONE code leg redeploying opal-amgt-scoped-api from the MERGED pin 3818736e6b carrying the forward P/E withhold: scoped_amgt.py 1f5de89912e5 -> a75ab14fd16d is the ONLY admitted packaged member (eight lib/research/aifill members differ in the tree and must NOT be packaged); live must read 0pWc69Vd.. first; AMGT_AIFILL_ROOT hold stays; first request after the apply driven alone; rollback is a REBUILD of code from 0447f2df38 applied with Terraform that carries the hold (C1)
**Authored by:** 0.7.0_AE_CloudOps~RA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pin 3818736e6b read in a DETACHED worktree; r94_admission_table.py 3818736e6b --pin 0447f2df38 prints EXACTLY the nine members at the half blobs; live CodeSha256 read first equal to 0pWc69Vd..; environment carries the hold | outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK: rebuild from live pin 0447f2df38, blob table printed BEFORE the apply, live package downloaded and hash-checked as a reference; C1 hold-carrying Terraform for the rollback; sweep of every live worktree open deploys | blob table + sha equality + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed BEFORE the build; source-map entry read BEFORE and compared with the live function | equal counts + entry fields |  | OPEN |
| L4 | verify | BUILD from the detached worktree at EXACTLY the pin, whole content diff printed FIRST (CHANGED must be scoped_amgt.py only at a75ab14fd16d, no aifill member in the zip); r94_naming_replay.py --pin 0447f2df38 on the BUILT ZIP with its denominator | build sha + content-diff + blobs + replay |  | OPEN |
| L5 | verify | PRE-ACT CAPTURE immediately before the apply: r106_fwd_pe_deployed.py capture to .scratch_bm3/thesis_pre.json, 95 names, no other reader | capture line |  | OPEN |
| L6 | activation | upload with read-back, plan graded from the plan JSON (code only; environment, role, layers, memory, timeout EQUAL), safe-apply of the saved plan; CodeSha256 after differs from 0pWc69Vd.. | VersionId, plan denominator, apply output, CodeSha256 after |  | OPEN |
| L7 | verify | THE FIRST ACT AFTER THE APPLY: r102_first_cold_request.py driven alone for ASML_NA_Equity: RECORDED or NOT COLD (not repeated) | request id handler time Init |  | OPEN |
| L8 | verify | AC1 r106_fwd_pe_deployed.py verify against the pre capture: YES 7 of 7 | verify output |  | OPEN |
| L9 | verify | AC2 r94_name_census --where deployed YES; AC3 r104_split_table on the first cold request | census and table lines |  | OPEN |
| L10 | git | record step record-terraform-deploy.sh and the source-map entry printed after | entry after equal to the live CodeSha256 + commit hash |  | OPEN |
| L11 | verify | report to the issuer with the first cold request id handler time Init; hold released; pin worktree left | the delivered message |  | OPEN |

## Log

- 20261014T125204Z OPENED by 0.7.0_AE_CloudOps~RA1 with 11 leg(s)
