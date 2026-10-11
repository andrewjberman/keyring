# Deploy Completion Record
**Date opened:** 2026-10-11T03:26:44.514708+00:00
**Status:** OPEN
**Deploy:** NFRA_TRNSPT.TO-APPLY-ra22 AMENDMENT 2: Teams pull refused-read + refused-listing fix. Pin pull.py blob 8aef45f2fc026aa231dc48ba93bf7c5fe43293c2 (drain 5ae3b3ddd9, build commits 12c64f3c1f and 2e86e331ad); built from box/dell2 d29ccddb17083f5339af74fc46af6210724fcd1d, on which NONE of the packet's 12 files -- indeed no bundled path at all -- differs from 5ae3b3ddd9 (git diff --name-only over every build.sh input: 0 changed; working tree clean on all of them). ONE zip feeds THREE functions in root infra/aws/terraform/transcripts: teams-global-transcripts-pull-lambda MOVES (the target); outlook-global-transcripts-pull-lambda MUST NOT MOVE (stays VGIq85Xxm5KVLCnv16BASS63RsPMHScMEwZJP5SuMNY=); outlook-global-commentary-draft-lambda MUST NOT BE CREATED (stays ResourceNotFound). Pair: COO packet @eb2d9e5451 ADDENDUM 1, CTO FRESH HALF @ee82091502 section F2. Rollback: rebuild pull.py at 0096e67747, same target, proof sha back at taFbGTCUAOhM+97EVJi3AfqqeBCV+FIUSLZ8Z4Ge6HA=.
**Authored by:** 0.7.0_AE_CloudOps~TR2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | Rebuild infra/aws/lambda/transcripts-pull/dist/transcripts-pull.zip via build.sh from the pinned tree | the new zip's base64 sha256, printed |  | OPEN |
| L2 | activation | safe-apply in infra/aws/terraform/transcripts TARGETED at aws_lambda_function.pull ONLY | one-resource plan line, the apply result, and the three post-apply sha reads (pull equals the zip hash; mail pull unchanged; commentary absent) |  | OPEN |
| L3 | verify | ONE invoke of teams-global-transcripts-pull-lambda (empty event), graded against packet A4 both ways | no errorMessage, 4 series entries, per-series listed/held/landed/read_refused/refused, state_key, and run record plus listing snapshot objects exist |  | OPEN |

## Log

- 20261011T032644Z OPENED by 0.7.0_AE_CloudOps~TR2 with 3 leg(s)
