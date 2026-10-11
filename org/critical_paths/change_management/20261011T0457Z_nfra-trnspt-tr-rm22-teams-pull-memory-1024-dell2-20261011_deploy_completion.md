# Deploy Completion Record
**Date opened:** 2026-10-11T04:57:49.898897+00:00
**Status:** OPEN
**Deploy:** NFRA_TRNSPT.TO-APPLY-rm22 AMENDMENT 1: raise aws_lambda_function.pull memory_size 128 (provider default, never declared) -> 1024. NO REBUILD: the zip is not touched and the pull's CodeSha256 must stay AI4UQD0ME+ABza1X0BrBjGjpqjN7f2fc0Cdxb88aA/I=. Applied from box/dell2 HEAD recorded in leg L1. ONE zip feeds THREE functions in root infra/aws/terraform/transcripts: teams-global-transcripts-pull-lambda MOVES (memory only); outlook-global-transcripts-pull-lambda MUST NOT MOVE (stays VGIq85Xxm5KVLCnv16BASS63RsPMHScMEwZJP5SuMNY=, already at 1024); outlook-global-commentary-draft-lambda MUST NOT BE CREATED (stays ResourceNotFound). Disarms row NFRA_TRNSPT-D2-S19. Pair: COO packet @f6f35a8841, CTO half @16fa3b73b8 section 3. Rollback: remove the memory_size line, re-apply the same target, proof MemorySize 128 with CodeSha256 unchanged.
**Authored by:** 0.7.0_AE_CloudOps~TR2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | The packet's three-line edit to infra/aws/terraform/transcripts/pull.tf, committed under the applier's own author line BEFORE the plan | the commit hash plus a path-scoped git diff HEAD~1 equal to the packet's diff byte for byte, and commit-gate.sh rc=0 |  | OPEN |
| L2 | activation | safe-apply in infra/aws/terraform/transcripts TARGETED at aws_lambda_function.pull ONLY, no rebuild | a plan changing exactly ONE resource and on it exactly ONE attribute, memory_size 128 -> 1024, with NO source_code_hash diff and no reader resource; then MemorySize 1024, the pull's CodeSha256 unchanged, the mail pull unmoved, the commentary function still absent |  | OPEN |
| L3 | verify | ONE invoke of teams-global-transcripts-pull-lambda (empty event), proving the SETTING is live rather than the peak | no errorMessage, 4 series entries with per-series counts, run record and listing snapshot exist, and the REPORT line's Memory Size and Max Memory Used as numbers |  | OPEN |

## Log

- 20261011T045749Z OPENED by 0.7.0_AE_CloudOps~TR2 with 3 leg(s)
