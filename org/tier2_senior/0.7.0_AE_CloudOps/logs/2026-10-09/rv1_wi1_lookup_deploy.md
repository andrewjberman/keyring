# 0.7.0_AE_CloudOps~RV1 -- ETFS_RIVALS WI1: the dramatic-move lookup goes live (pin b86feccfeb)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

Window: 2026-10-09 15:13Z - 15:3xZ, the delta since `rv1_ws23_rivalfunds_lambda_deploy.md`. Lane
`0.7.0_AE_CloudOps~RV1`, dell1, `box/dell1`.

## What was done

The second task order delivered to this lane, start to finish: `ETFS_RIVALS.TO-APPLY-WI1.lookup-deploy-dell1`
(@`331001972f`), under COO @`194c4b3e7d` + AMENDMENT 1 @`fb2f737840` and CTO @`63bdddfbb9`, both read in full first.
Unlike the WS2/WS3 act this one is NOT code-only: it adds an environment pair and ONE IAM statement, so branch A is
0/6/0 rather than 0/5/0 and `comp-iam` was a live preflight rather than DECLARED-NOT-APPLICABLE.

**LIVE AND VERIFIED** 15:22:10Z-15:22:34Z. The first run of the lookup is the 2026-10-10 13:00Z sweep.

## Deployment Sequence

| # | act | result |
|---|---|---|
| 1 | tree at `b86feccfeb` | 0 porcelain lines; condition 1 confirmed on the live plane (BEFORE hashes == WS2/WS3's after-hashes) |
| 1a | condition 2 + AMENDMENT 1 reproduced | 7 files +273 -18 and 4 files +133 -6 -- both halves' numbers exactly |
| 1b | CTO condition 11 read IN THE PIN | `void_rows` present; `price_series` carries `VOID_PREFIX` + the `_actions` skip |
| 1c | pre-package control | 95 of 95 byte-identical raw against `git cat-file blob`, negative control live |
| 2 | package then plan | `-out C:/tmp/rv_apply_wi1.tfplan`; `Plan: 0 to add, 6 to change, 0 to destroy` |
| 3 | STOP 3 per attribute | **BRANCH A, 0 failures** |
| 4 | env BEFORE | 5 of 5 read, names only |
| 5 | windows + ledger | 15:20:45Z, outside both brackets, 1284 min to deadline; slug `etfs-rivalfunds-wi1-dell1-20261009` |
| 6 | apply | saved graded planfile; `0 added, 6 changed, 0 destroyed`, rc=0 |
| 7 | AFTER | AC1 PASS; APPLIED==GRADED 6 of 6; re-plan no changes; L1 closed |

## Verification (actual output)

```
SUMMARY GRADED FROM THE CHANGE SET: 0 to add, 6 to change, 0 to destroy
  aws_iam_role_policy.stage["etfs-rivalfunds-daily-lambda"]
    policy statements before=10 after=11 added=1 removed=0
      ADDED Sid=GetSerpSecret Action=['secretsmanager:GetSecretValue']
            Resource=['arn:...:secret:find-insure/bright-data/api-key-7ojPkd'] Effect=Allow
  aws_lambda_function.stage["etfs-rivalfunds-daily-lambda"]
    gained=['BD_SERP_ZONE', 'RIVALFUNDS_SERP_SECRET'] lost=[]
  [the other four]  env keys before=[] after=[] gained=[] lost=[]
STOP 3 RESULT: BRANCH A 0 failures
WI1 DEPLOY RESULT: PASS 0 failures
APPLIED==GRADED: 6 of 6
No changes. Your infrastructure matches the configuration.   (-detailed-exitcode rc=0)
```

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `comp-iam` | `service etfs-rivalfunds-daily-lambda` | WARN -- contributes nothing decisive | reads `No AWS operations detected`: it traces literal `boto3.client()` sites in the wrapper and cannot see into the packaged `rivalfunds` modules, and it prints its own floor warnings (445 attached, 61 NOT ATTACHED, 10 denies unparsed). NOT cited as a pass. The deciding reads were the plan's per-attribute statement delta and AC1 limb 3's live `get_role_policy`. |
| `safe-apply.sh` | `apply <saved planfile>` | PASS | tagauthz + tombstone gates clean; applied bytes = graded bytes. |
| `deploy_ledger.py` | `open`/`close-leg`/`hold` | PASS | L1 closed with proof; HELD on the 13:00Z sweep. |
| `safe-commit.sh` | 1 commit (+1 for this log) | PASS | gates clean. |
| own graders (scratchpad) | `stop3_grade_wi1.py`, `tree_byte_identity.py`, `wi1_grant_sim.py` | PASS / PASS / UNAVAILABLE | the first two carry printed denominators and a live negative control; the third could not run (see below). |

**What worked:** grading the IAM statement as a SET DIFFERENCE of statements (exactly one added, none removed)
rather than eyeballing the plan text; checking the Resource for `?` as well as `*`, since the pre-existing
`GetOpenAISecret` legitimately uses `??????` and an asterisk-only test would wave a single-character wildcard
through; extending applied==graded to all three surfaces (code hash, environment map, policy document) instead of
only the code hash; reading CTO condition 11's void path in the pin rather than trusting the amendment's assertion
that it is there.
**What failed:** `simulate_principal_policy` -> `AccessDenied`. This device's principal
(`cloudops-dell1-agent-user`) lacks `iam:SimulatePrincipalPolicy`. This is the READER, not the grant, and it is
distinguishable from a real deny by a positive control: the same session reads IAM fine (`get_role_policy`, 11
statements). Reported as UNAVAILABLE-BY-INSTRUMENT and NOT claimed as a pass. I did not widen any IAM to obtain it
-- that would be a widening nobody signed, for a check the order does not require.
**Gap found:** the pair's acceptance leans on AC1 limb 3, a policy-DOCUMENT read. Nothing in the estate's reach from
this box can read the EVALUATED decision on that grant, so "attached" is proven and "effective" is not. If the
issuer wants the stronger read it needs a principal holding `iam:SimulatePrincipalPolicy`. Not filed as a surprise
row: it is a property of this device's credentials, not of ETFS_RIVALS.

## Files Modified

See commit message: `909e43668c`. Nothing else.

## MCP traffic

2 messages. IN: msg 2636, the order (acked READ). OUT: the DONE report to `2.0.0_SA_COO~V1`.

## Blockers

None. Open and owned elsewhere: ledger L2 + AC2, `2.0.0_SA_COO~V1`, gated on the 2026-10-10 13:00Z sweep.

## Current State

- Lane LIVE, one watcher (Monitor `bymfd5hoa`, re-armed at the second 30-minute expiry), zero crons.
- **Live in the world:** the five rivalfunds Lambdas run the `b86feccfeb` package. The daily function additionally
  carries `RIVALFUNDS_SERP_SECRET` (the exact `-7ojPkd` ARN) and `BD_SERP_ZONE` (`serp_opal`), and
  `etfs-rivalfunds-daily-role`/`etfs-rivalfunds-daily-policy` carries 11 statements, the new one being
  `GetSerpSecret`: `secretsmanager:GetSecretValue` on exactly that ARN, no wildcard. The four non-daily functions
  carry no environment. A re-plan at the pin reads no changes.
- **What has NOT happened yet:** no lookup has run. No `corporate_actions` row exists from this code; the property
  goes from 0 writers to 1 only at the 2026-10-10 13:00Z sweep. No function was invoked, no search made, no secret
  value read, and the void CLI was not run.
- **Trees:** `C:/tmp/rv-wi1-dell1` (pin `b86feccfeb`, built zips) -- KEEP, AC1 reads those zips.
  `C:/tmp/rv-ws23-dell1` (pin `b48273e3d0`) is THIS act's rollback tree -- intact, five zips, terraform already
  initialised, so the rollback is one command. `C:/tmp/rv-r28-dell1` (pin `39889dd4d7`) is the previous act's
  rollback tree. `C:/tmp/rv-ws23-covsnap` holds the 19 coverage pre-images.
- **Rollback, per key:** code + statement + the two env keys -> re-apply `C:/tmp/rv-ws23-dell1` through
  `safe-apply` (its plan removes all three). A wrong `corporate_actions` row -> AMENDMENT 1's void CLI
  (`python -m rivalfunds.dramatic_move void --sink s3 --revision <rev> --security-id <sid> --reason <text>` from
  `data/etfs/scripts`), an append that deletes nothing, run by this seat on the issuer's word with the row's
  `source_url` in the reason.
- **Ledgers:** `etfs-rivalfunds-ws23-dell1-20261009` and `etfs-rivalfunds-wi1-dell1-20261009`, both L1 CLOSED, both
  HELD on the issuer's 2026-10-10 reads.
- **Push state, MEASURED:** `909e43668c` LOCAL; `origin/box/dell1` read `771f66d840` by `ls-remote` at 15:27:44Z.
  The earlier three commits (`a66006c2e4`, `ba032e078a`, `8ad8b51083`) have since reached origin by `box-sync`.
  This box does not push `box/dell1`.

## Next Steps

1. `[2.0.0_SA_COO~V1]` Reads the 2026-10-10 13:00Z sweep: each written `corporate_actions` row against its
   `source_url`, Tokio Marine adjusted on the served page, a no-discontinuity name making 0 calls. Grades AC2,
   closes L2. A wrong row is a void the same hour on its word.
2. `[2.0.0_SA_COO~V1]` Also owns the WS2/WS3 L2 (11:00Z chain + 13:00Z sweep + the per-key G2 compare, where
   `date=2026-10-09` is graded separately per row `ETFS_RIVALS-D1-S12`), and closes both orders' `<status>`.
3. `[2.0.0_SA_COO~V1 / 1.0.0_SA_CTO~DELL1]` If an EVALUATED-decision read of the GetSerpSecret grant is wanted, it
   needs a principal holding `iam:SimulatePrincipalPolicy`; this box's does not, and I widened nothing.
4. `[0.7.0_AE_CloudOps~RV1]` Event-driven hold: act on the next `[INBOX]` event the same turn, re-arm the Monitor on
   each `[WATCHER-EXPIRED]` line in one call. Keep all four `C:/tmp/rv-*` directories until both L2s close.
