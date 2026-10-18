# Deploy Completion Record
**Date opened:** 2026-10-18T02:56:30.486392+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-bv-5: ONE code leg redeploying opal-amgt-scoped-api from release pin d4bba34eb8 (lib/research/print/render_pack.py 60a9f2ddb4f4 -> 8a1f47d8c6cd is the ONLY admitted member); live must read RY998VO4.. first; AMGT_AIFILL_ROOT stays absent; rollback = the bu-7 artifact VersionId pXDgyepp27ULWCB5z9kMRHNjyk.8qIgh by the saved-plan route
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pin d4bba34eb8 (parent 6bb7b23ee5) in a DETACHED worktree; r94_admission_table.py d4bba34eb8 --pin 6bb7b23ee5 prints exactly 1 member; live CodeSha256 RY998VO4.. RevisionId 3c6a52dc.. LastModified 2026-10-18T01:16:17Z read first | outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK TARGET: bu-7 artifact S3 key + VersionId + sha recorded and the live package downloaded and hash-checked; sweep of live worktrees for open deploys on this function | rollback table + sha equality + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed before the build; source-map entry read before and compared with the live function | equal counts + entry fields |  | OPEN |
| L4 | verify | BUILD from the detached worktree at exactly d4bba34eb8; whole content diff vs the live package printed FIRST (CHANGED must be render_pack.py only at 8a1f47d8c6cd) | build sha + content diff + blobs |  | OPEN |
| L5 | verify | IMMEDIATELY before upload: LastModified + CodeSha256 + RevisionId re-read equal to the pre-act print; FRESH BEFORE sets of the eight packs and eight rich exports captured | config read + capture lines |  | OPEN |
| L6 | activation | upload_verified.sh with read-back; plan graded from the plan JSON (code only); safe-apply of the saved plan; CodeSha256 after differs from RY998VO4.. | VersionId, plan denominator, apply output, CodeSha256 after |  | OPEN |
| L7 | verify | post-act: AC1 PACK SAME YES 8 of 8, AC2 RICH COMPARE YES 8 of 8, AC3 config, AC4 pin diff; environment unchanged | AC outputs |  | OPEN |
| L8 | git | record step record-terraform-deploy.sh and the source-map entry printed after | entry after equal to the live CodeSha256 + commit hash |  | OPEN |
| L9 | verify | proof_of_spec instance VALID on committed bytes; report to the issuer once | checker last line + the delivered message |  | OPEN |

## Log

- 20261018T025630Z OPENED by 0.7.0_AE_CloudOps~SC1 with 9 leg(s)
