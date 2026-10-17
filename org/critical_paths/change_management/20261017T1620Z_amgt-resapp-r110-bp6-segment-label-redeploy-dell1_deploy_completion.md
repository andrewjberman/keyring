# Deploy Completion Record
**Date opened:** 2026-10-17T16:20:27.765083+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-bp-6: ONE code leg redeploying opal-amgt-scoped-api from release pin 7a8f2bb8e6 (segment_served.py cd72ba96223a -> cbf094d0b633 is the ONLY admitted member); live must read UIkRgr9g.. first; AMGT_AIFILL_ROOT stays absent; rollback = the bm-3 artifact VersionId by the saved-plan route
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pin 7a8f2bb8e6 read in a DETACHED worktree; r94_admission_table.py 7a8f2bb8e6 --pin 3818736e6b prints exactly 1 member; live CodeSha256 UIkRgr9g.. first | outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK TARGET: bm-3 artifact S3 key + VersionId + sha recorded; live package downloaded and hash-checked; sweep of live worktrees for open deploys on this function | rollback table + sha equality + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed before the build; source-map entry read before and compared with the live function | equal counts + entry fields |  | OPEN |
| L4 | verify | BUILD from the detached worktree at exactly 7a8f2bb8e6; whole content diff vs the live package printed FIRST (CHANGED must be segment_served.py only at cbf094d0b633) | build sha + content diff + blobs |  | OPEN |
| L5 | verify | IMMEDIATELY before upload: xadj RULED (a) re-read; LastModified + CodeSha256 re-read equal to the pre-act print via r110_bp6_config_and_label.py | xadj state + the two reads |  | OPEN |
| L6 | activation | upload_verified.sh with read-back; plan graded from the plan JSON (code only); safe-apply of the saved plan; CodeSha256 after differs from UIkRgr9g.. | VersionId, plan denominator, apply output, CodeSha256 after |  | OPEN |
| L7 | verify | post-act: AC1 census EQUAL 95, AC2 config + RIO LN label, AC3 pin diff; environment unchanged (AMGT_AIFILL_ROOT absent, memory 1769, timeout 29) | AC outputs |  | OPEN |
| L8 | git | record step record-terraform-deploy.sh and the source-map entry printed after | entry after equal to the live CodeSha256 + commit hash |  | OPEN |
| L9 | verify | proof_of_spec instance VALID on committed bytes; report to the issuer once | checker last line + the delivered message |  | OPEN |

## Log

- 20261017T162027Z OPENED by 0.7.0_AE_CloudOps~SC1 with 9 leg(s)
