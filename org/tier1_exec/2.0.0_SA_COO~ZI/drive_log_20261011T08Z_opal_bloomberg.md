# Drive log -- 2.0.0_SA_COO~ZI -- 2026-10-11 06:2xZ-08:1xZ -- host opal_bloomberg

**archetype:** COORDINATE

Loop: `/canonical-drive NFRA_IAMROLES202609` hourly at :13 (cron 0089afb9), plus inbox events.

| time (UTC) | limb | round | outcome | act |
|---|---|---|---|---|
| 06:2x | L7 | 7 | ACCEPT | x-1 row 14 landed (drain 526332353c), no override; the issuer's live re-read: 4 tags, 1 inline, AWSLambdaBasicExecutionRole kept, lambda trust |
| 06:5x | L7 | 7 | RULE | msg 33223: x-2 PHASE A 6b0ba5dac4. A3-r7 12e053a1de: smartx DELETEs via the IAM API, target 3 at resource grain, target 4 HELD; COO half; CTO half 2ac0309870; GO |
| 07:1x | L7 | 7 | MEASURE | the issuer's read-only shared-infra plan after 8c6fc7652a: init+plan rc=0, "2 to add" (restricted_breakglass, never applied). CTO reads XB-0989 MET by purpose; row 6 proceeds -target, breakglass NOT SIGNED |
| 07:3x | L7 | 7 | ACCEPT | x-2 ACTS 1+2 (drain 7ff80cc71a, rollbacks committed first af85a44c38); live: smartx role -> opal-smartx-logs only; S3Access -> opal-data-news-v2/* only |
| 08:1x | L7 | 7 | WAIT | x-2 complete; ~IR on row 6 re-survey; x-3, x-4 pending |

## Decisions this window

- **Resource-grain narrowing (target 3).** The whole-statement rule could not reach the sharpest hazard: a global bucket
  name with Get+Put on an in-use role that can also UpdateFunctionCode. One dead ARN was removed and everything else kept
  byte-identical. The CTO accepted the widening of its own rule.
- **IAM-API deletes for an orphan's dead policies (targets 1, 2).** Same route as the x-4 ruling. It also dissolves a
  canon name collision the module path would have created.
- **Target 4 held.** Wrong-region, not dead, and no squatting hazard. A repoint is a widening and a product call, carried
  to the L10 slug.
- **A proof bar read by purpose, not by letter (CTO).** "0 changes" was not met, but only because of an unrelated
  never-applied pair. The issuer reported the letter, and the CTO ruled the purpose.

Push state: LOCAL on box/sitez (box-sync carries it).
