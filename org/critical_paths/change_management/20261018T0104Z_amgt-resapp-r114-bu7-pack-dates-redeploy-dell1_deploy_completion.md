# Deploy Completion Record
**Date opened:** 2026-10-18T01:04:32.207628+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-bu-7: ONE code leg redeploying opal-amgt-scoped-api from release pin 6bb7b23ee5 (lib/research/print/render_pack.py 8e8266859b7b -> 60a9f2ddb4f4 is the ONLY admitted member); live must read hLW4fD/aGMs.. first; AMGT_AIFILL_ROOT stays absent; rollback = the bp-6 artifact VersionId 3TWvFWWa.qf6mrqKodzvQU3DhV_eCTRd by the saved-plan route
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pin 6bb7b23ee5 (parent 7a8f2bb8e6) in a DETACHED worktree; r94_admission_table.py 6bb7b23ee5 --pin 7a8f2bb8e6 prints exactly 1 member; live CodeSha256 hLW4fD.. RevisionId cf9191fc.. LastModified 2026-10-17T16:34:05Z read first | outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK TARGET: bp-6 artifact S3 key + VersionId + sha recorded and the live package downloaded and hash-checked; sweep of live worktrees for open deploys on this function | rollback table + sha equality + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed before the build; source-map entry read before and compared with the live function | equal counts + entry fields |  | OPEN |
| L4 | verify | BUILD from the detached worktree at exactly 6bb7b23ee5; whole content diff vs the live package printed FIRST (CHANGED must be render_pack.py only at 60a9f2ddb4f4) | build sha + content diff + blobs |  | OPEN |
| L5 | verify | IMMEDIATELY before upload: LastModified + CodeSha256 + RevisionId re-read equal to the pre-act print; FRESH BEFORE set of the eight packs captured to r114-packs-before2 | config read + capture line |  | OPEN |
| L6 | activation | upload_verified.sh with read-back; plan graded from the plan JSON (code only); safe-apply of the saved plan; CodeSha256 after differs from hLW4fD.. | VersionId, plan denominator, apply output, CodeSha256 after |  | OPEN |
| L7 | verify | post-act: AC1 capture+compare YES 8 of 8, AC2 config, AC3 pin diff; environment unchanged (AMGT_AIFILL_ROOT absent, memory 1769, timeout 29) | AC outputs |  | OPEN |
| L8 | git | record step record-terraform-deploy.sh and the source-map entry printed after | entry after equal to the live CodeSha256 + commit hash |  | OPEN |
| L9 | verify | proof_of_spec instance VALID on committed bytes; report to the issuer once | checker last line + the delivered message |  | OPEN |

## Log

- 20261018T010432Z OPENED by 0.7.0_AE_CloudOps~SC1 with 9 leg(s)
