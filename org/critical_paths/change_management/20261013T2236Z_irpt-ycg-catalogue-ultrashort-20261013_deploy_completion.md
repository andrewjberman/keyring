# Deploy Completion Record
**Date opened:** 2026-10-13T22:36:49.598520+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-pr-520: move irpt-ycharts-generate to the signed built digest xP47NQDnZNZ8Lui1XQKUxUtTMTasR8Cj/A1sQnRDZYY= (hex c4fe3b35..): templates.json (adds Opal Ultra Short-Term, five models in canonical order, Long-Term moves first to fourth for every firm on Andrew's word) and maintained_sources.py (its one pin line) change, 102 of 104 members identical; function irpt-ycharts-generate ONLY (the seven sibling functions staging maintained_sources.py are not moved); Branch B = S3 version ennO07toFOYlPWM64JC4MS9g.bVRr7fW of investor-reporting/irpt-ycharts-generate.zip (live hpNfkhLtLRl0e9TFL+Vdr5kilZ1W8bN3GKMhlzmVXgg=, hex 86935f92..); pair IB-pr-518 packet sha256 7439728602c6, COO @d06ee1f0fc + CTO @f7bd0b5b7e signed; the CTO's after-read is a person's, so this ledger is closed only on the issuer's word
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | gates by the artifact: packet sha256, both halves signed, ledgers naming the function (56 read, 0 open), markers over every worktree (stale views named, 0 with an open trunk ledger), live CodeSha256 hpNfkhLtLRl0..; Branch B version named and hash-matched | the reads in the apply record |  | OPEN |
| L2 | s3-prefix | source-map row edited (pin 0642c9d0.. to 0d0e9e12.., sha256 29c35dbf.. to 74c262b6..), BUILD_ONLY digest equals xP47NQDnZNZ8Lui1XQKUxUtTMTasR8Cj/A1sQnRDZYY=, then the same build uploaded and verified by head-object | printed digest, new VersionId |  | OPEN |
| L3 | verify | terraform plan to a planfile (module irpt_ycharts_generate, s3_object_version and source_code_hash only): 1 to change, 0 to add, 0 to destroy | plan summary line |  | OPEN |
| L4 | activation | bash .tools/safe-apply.sh on the planfile; live CodeSha256 equals the built digest, re-plan 0 changes, exactly templates.json and maintained_sources.py differ from the pre-apply zip with the signed member hashes; source-map row committed with the release | apply line, digest, re-plan line, member diff, commit |  | OPEN |
| L5 | verify | health proof with NO invoke, read at least 10 minutes after the apply: Invocations and Errors metrics, log-group error signatures with START lines as the positive control | window, invocation count, error count |  | OPEN |
| L6 | verify | THE CTO's AFTER-READ, A PERSON'S: the served catalogue returns the five labels in canonical order for one permitted firm, the Analysis Request form on DEV lists Ultra Short-Term; stays OPEN for the issuer | the issuer's read |  | OPEN |

## Log

- 20261013T223649Z OPENED by 0.7.0_AE_CloudOps~IB2 with 6 leg(s)
