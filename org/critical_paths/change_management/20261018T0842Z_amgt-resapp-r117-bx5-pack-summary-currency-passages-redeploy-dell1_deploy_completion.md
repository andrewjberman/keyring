# Deploy Completion Record
**Date opened:** 2026-10-18T08:42:48.871795+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP AMGT-bx-5: ONE code leg redeploying opal-amgt-scoped-api from release pin 9ab6d36305 (ONE member only: lib/research/print/render_pack.py 7f5c5bb94a18 -> 004bafd2338f); live must read lNWo6Cm6.. first; AMGT_AIFILL_ROOT stays absent; rollback = the bw-5 artifact VersionId EVD2sGd8Bb.DGRU1XjvuhPJ6cOJo.otg by the saved-plan route; issuer times the print route after the apply (over 20 s = rollback); run between the pairs of the cj-4 dossier write (W1 msg 7972), whose writes are paused for the pre-act capture, the apply and the post-act reads
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pin 9ab6d36305 (parent fe04d740bf) in a DETACHED worktree; r94_admission_table.py 9ab6d36305 --pin fe04d740bf prints exactly 1 member; live CodeSha256 lNWo6Cm6.. RevisionId 2eecd7e1.. LastModified 2026-10-18T05:52:41Z read first | outputs printed whole |  | OPEN |
| L2 | verify | ROLLBACK TARGET: bw-5 artifact S3 key + VersionId + sha recorded and the live package downloaded and hash-checked; sweep of live worktrees for open deploys on this function | rollback table + sha equality + sweep denominators |  | OPEN |
| L3 | verify | wheel folder re-hashed before the build; source-map entry read before and compared with the live function | equal counts + entry fields |  | OPEN |
| L4 | verify | BUILD from the detached worktree at exactly 9ab6d36305; whole content diff vs the live package printed FIRST (CHANGED must be render_pack.py only at 004bafd2338f) | build sha + content diff + blobs |  | OPEN |
| L5 | verify | IMMEDIATELY before upload: LastModified + CodeSha256 + RevisionId re-read equal to the pre-act print; FRESH BEFORE set of the eight packs captured | config read + capture lines |  | OPEN |
| L6 | activation | upload_verified.sh with read-back; plan graded from the plan JSON (code only); safe-apply of the saved plan; CodeSha256 after differs from lNWo6Cm6.. | VersionId, plan denominator, apply output, CodeSha256 after |  | OPEN |
| L7 | verify | post-act: AC1 PACK CAPTURE 8 of 8 and PACK FORM YES 8 of 8, AC2 MONEY VS PAGE YES, AC3 config, AC4 pin diff; environment unchanged | AC outputs |  | OPEN |
| L8 | git | record step record-terraform-deploy.sh and the source-map entry printed after | entry after equal to the live CodeSha256 + commit hash |  | OPEN |
| L9 | verify | issuer latency read (KMB US, RIO LN, GOOGL US under 20 s) awaited; proof_of_spec instance VALID on committed bytes; report to the issuer once | issuer word + checker last line + the delivered message |  | OPEN |

## Log

- 20261018T084248Z OPENED by 0.7.0_AE_CloudOps~SC1 with 9 leg(s)
