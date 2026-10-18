# Deploy Completion Record
**Date opened:** 2026-10-18T11:05:01.253914+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-by-5: ONE code leg redeploying opal-amgt-scoped-api from release pin d4c6f1c533 (TWO members only: lib/research/print/render_pack.py 004bafd2338f -> 5f4cffc172ba and lib/research/api/scoped_amgt.py 472df817702c -> 1fcf51f05afc); live must read Rycs0LVa.. first; AMGT_AIFILL_ROOT stays absent; rollback = the bx-5 artifact VersionId 2TBErsoGd68qZqe3kUnuh0PFFYreDnLO by the saved-plan route; the issuer reads both routes (pdf and rich) after the apply (over 20 s = rollback)
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pin d4c6f1c533 (parent 9ab6d36305) in a DETACHED worktree; r94_admission_table.py d4c6f1c533 --pin 9ab6d36305 prints exactly 2 members; live CodeSha256 Rycs0LVa.. RevisionId 05fed159.. LastModified 2026-10-18T08:51:36Z read first | outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK TARGET: bx-5 artifact S3 key + VersionId + sha recorded and the live package downloaded and hash-checked; sweep of live worktrees for open deploys on this function | rollback table + sha equality + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed before the build; source-map entry read before and compared with the live function | equal counts + entry fields |  | OPEN |
| L4 | verify | BUILD from the detached worktree at exactly d4c6f1c533; whole content diff vs the live package printed FIRST (CHANGED must be the two members only at 5f4cffc172ba and 1fcf51f05afc) | build sha + content diff + blobs |  | OPEN |
| L5 | verify | IMMEDIATELY before upload: LastModified + CodeSha256 + RevisionId re-read equal to the pre-act print; FRESH BEFORE set of the eight packs captured | config read + capture lines |  | OPEN |
| L6 | activation | upload_verified.sh with read-back; plan graded from the plan JSON (code only); safe-apply of the saved plan; CodeSha256 after differs from Rycs0LVa.. | VersionId, plan denominator, apply output, CodeSha256 after |  | OPEN |
| L7 | verify | post-act: AC1 PACK CAPTURE 8 of 8 and PACK FORM YES 8 of 8, AC2 MONEY VS PAGE YES, AC3 config, AC4 pin diff; environment unchanged | AC outputs |  | OPEN |
| L8 | git | record step record-terraform-deploy.sh and the source-map entry printed after | entry after equal to the live CodeSha256 + commit hash |  | OPEN |
| L9 | verify | issuer read of both routes (pdf and rich) under 20 s, leak scan and rich exports awaited; proof_of_spec instance VALID on committed bytes; report to the issuer once | issuer word + checker last line + the delivered message |  | OPEN |

## Log

- 20261018T110501Z OPENED by 0.7.0_AE_CloudOps~SC1 with 9 leg(s)
