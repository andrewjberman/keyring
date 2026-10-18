# Deploy Completion Record
**Date opened:** 2026-10-18T16:01:21.751931+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-ca-5: ONE code leg redeploying opal-amgt-scoped-api from release pin 107fae40e9 (TWO members: lib/research/print/render_pack.py ce54affc8f87 -> 2f60c311f595; lib/research/api/scoped_amgt.py 1fcf51f05afc -> b98964fa97fa); live must read VQ9zM6r4.. first; AMGT_AIFILL_ROOT stays absent; rollback = the bz-5 artifact VersionId w598xCQmxV1B4o2_1bI6DjlDYOfObJdu by the same saved-plan route; no close before the issuer's KEEP word
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pin 107fae40e9 (parent 2771164d0d) in a DETACHED worktree; r94_admission_table.py prints exactly 2 members; live CodeSha256 VQ9zM6r4.. RevisionId 8d9ebc77.. LastModified 2026-10-18T13:11:57Z read first | outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK TARGET: bz-5 artifact S3 key + VersionId + sha recorded and the live package downloaded and hash-checked; sweep of live worktrees for open deploys on this function | rollback table + sha equality + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed before the build; source-map entry read before and compared with the live function | equal counts + entry fields |  | OPEN |
| L4 | verify | BUILD from the detached worktree at exactly 107fae40e9; whole content diff vs the live package printed FIRST (CHANGED must be render_pack.py and scoped_amgt.py only, at 2f60c311f595 and b98964fa97fa) | build sha + content diff + blobs |  | OPEN |
| L5 | verify | IMMEDIATELY before upload: LastModified + CodeSha256 + RevisionId re-read equal to the pre-act print; FRESH BEFORE set of the eight packs captured | config read + capture lines |  | OPEN |
| L6 | activation | upload_verified.sh with read-back; plan graded from the plan JSON (code only); safe-apply of the saved plan; CodeSha256 after differs from VQ9zM6r4.. | VersionId, plan denominator, apply output, CodeSha256 after |  | OPEN |
| L7 | verify | post-act: AC1 PACK CAPTURE 8 of 8 and PACK FORM YES 8 of 8, AC2 MONEY VS PAGE YES, AC3 config, AC4 pin diff; environment unchanged | AC outputs |  | OPEN |
| L8 | git | record step record-terraform-deploy.sh and the source-map entry printed after | entry after equal to the live CodeSha256 + commit hash |  | OPEN |
| L9 | verify | issuer reads (both routes under 20 s, leak scan, cross-surface, rich exports, the reading words per name) and the issuer's KEEP word; proof_of_spec instance VALID on committed bytes; report to the issuer once | issuer word + checker last line + the delivered message |  | OPEN |

## Log

- 20261018T160121Z OPENED by 0.7.0_AE_CloudOps~SC1 with 9 leg(s)
