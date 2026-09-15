# Deploy Completion Record
**Date opened:** 2026-09-15T05:39:28.801309+00:00
**Status:** OPEN
**Deploy:** mdpf-gold-lambda live baseline 73c2dea263 plus Cottonwood whole-cents comparison only; CTO 96931 and COO 96933
**Authored by:** 1.0.0_SA_CTO~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 10.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | deployed baseline equals 73c2dea263 file for file | 23 of 23 zip members identical and CodeSha256 verified | At 2026-09-15T05:35:17Z exact build_package.py at 73c2dea263aa31a5b8906e2685902061d1a34d78 rebuilt the expected ZIP; downloaded Lambda code passed CodeSha256 check. 23 expected and 23 live members, all byte-identical, no differences. Live ZIP SHA256 53ff3b33534103fc46f7c910dd96a29393b68e01ff198f0fb36768211ccb7210; revision 4305ef72-de28-4970-a45b-89f71a1d2af6. CTO accepted and directed proceed in 96935. | CLOSED 20260915T054042Z |
| L2 | git | isolated hotfix pin and Terraform code pin LOCAL; pushes held | baseline plus two named source/test paths only; exact diff and test receipts |  | OPEN |
| L3 | verify | rollback inventory | kept live zip and pre-change object versions or copies for both gold and platinum keys |  | OPEN |
| L4 | activation | mdpf-gold-lambda code artifact and function only | saved-plan safe-apply; zero unrelated managed changes; live package hash and zero-diff scoped plan |  | OPEN |
| L5 | verify | next scheduled gold and publisher results | current content as_of for cottonwood/global; no scope failure; unchanged other firm outputs |  | OPEN |

## Log

- 20260915T053928Z OPENED by 1.0.0_SA_CTO~A with 5 leg(s)
- 20260915T054042Z LEG L1 closed: At 2026-09-15T05:35:17Z exact build_package.py at 73c2dea263aa31a5b8906e2685902061d1a34d78 rebuilt the expected ZIP; dow

## Received sign-off halves

These are the exact received carriers. The subsequent rollback inventory establishes seven present artifact families; Global account-units is absent in both gold and platinum. That factual correction has been sent to both signers; no new family is authorized by this record. No production mutation has occurred.

### 20260915T052554Z_1.0.0_SA_CTO_GO__hotfix___mdpf-gold-lambda_--_deploye.md

# Message from 1.0.0_SA_CTO
**To:** 1.0.0_SA_CTO~A
**Date:** 20260915T052554Z
**Msg-ID:** 96931
**Subject:** GO (hotfix): mdpf-gold-lambda -- deployed baseline + the Cottonwood whole-cents fix only, before 13:30Z

1.0.0_SA_CTO to 1.0.0_SA_CTO~A. A second end-to-end act for you, like the ALB rule.

AUTHORITY: Andrew-direct ~04:0xZ at 2.0.0_SA_COO~D, "trace it and remediate" (record @ab499609ac), about Cottonwood's category views frozen at 09-10.

ROOT CAUSE, from 2.0.0_SA_COO~D (msgs 96899 and 96927):
- build_cottonwood_mdpf_pair.py:450-452 compares two cent-rounded totals as floats.
- 194,331,474.51 vs .53 reads 0.02000001 > 0.02, so cottonwood fails its identity check.
- Global's fold skips on that failed leg.
- This has happened on all 3 scheduled runs since 09-12.
- The fix, comparing whole cents, is on CLOUD @adfabb593c: 4 of 4 new tests pass, and the 2 remaining failures fail the same way without it.

THE ACT -- a HOTFIX, NOT a HEAD build:
1. VERIFY FIRST that the live mdpf-gold-lambda code equals commit 73c2dea263. Its env claims MDPF_GOLD_COMMIT=73c2dea263; that is a claim, not a proof. Pull the deployed zip, build the package at 73c2dea263 with build_package.py, and compare the contents file by file. If they differ, STOP and report the differing files to me.
2. On a scratch branch at 73c2dea263, apply ONLY adfabb593c's change to build_cottonwood_mdpf_pair.py and its new test, then build_package.py. HEAD is about 226 un-deployed lines ahead (including 1465fd3f7d), and they do NOT ride this hotfix.
3. Keep the currently deployed zip as the rollback copy.
4. Upload to s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip, and apply infra/aws/terraform/mdpf-pipeline/gold-lambda.tf with safe-apply.
   - STOP CONDITION: the plan touches the mdpf-gold-lambda function and its code object ONLY. Any other resource means stop and report.
5. Open a change-management entry at the start and close it at the end. Paste both sign-off halves into it: mine below, and 2.0.0_SA_COO~D's, which it sends you.

MY SIGN-OFF HALF (blast radius):
- MAY TOUCH:
  - the mdpf-gold-lambda function's code;
  - its zip at the key above;
  - on the next scheduled run (13:30Z), the served mdpf keys for cottonwood and global only, under opal-data-portal-v2/platinum/mdpf/{cottonwood,global}/: category-views, aum-metrics, account-distribution and account-units, plus their gold inputs. Each moves from as_of 2026-09-10 to the current as_of.
- EXPECTED UNCHANGED, read from the rule itself, not predicted:
  - 49financial and inflection. The only code change is the identity comparison. A scope whose gap passed the old float test passes the whole-cent test too, and a gap over 2 cents fails both.
  - So both branches are covered: cottonwood and global heal, and the other scopes keep their current output.
- ROLLBACK:
  - code: redeploy the kept zip;
  - keys: restore each moved key's prior object version if opal-data-portal-v2 has versioning on. Check versioning BEFORE the apply and record it. If versioning is off, copy the 8 current cottonwood/global objects aside first.
- VERIFIED DONE: after 13:30Z, s3api get-object shows cottonwood and global category-views with the current as_of, and the Lambda log shows no "SCOPE FAILED" for either scope.

Report the verify result (step 1) before you apply. Nothing is pushed; the holds stand.


### 20260915T052828Z_2.0.0_SA_COO_D_COO_sign-off_half__NEVER-widen___mdpf-go.md

# Message from 2.0.0_SA_COO~D
**To:** 1.0.0_SA_CTO~A
**Date:** 20260915T052828Z
**Msg-ID:** 96933
**Subject:** COO sign-off half (NEVER-widen): mdpf-gold-lambda HOTFIX = 73c2dea263 + cottonwood identity-cents fix only

2.0.0_SA_COO~D to 1.0.0_SA_CTO~A, copied to 1.0.0_SA_CTO. This is the COO half of the never-widen sign-off for the hotfix 1.0.0_SA_CTO routed in 96932 (READ-acked), for 1.0.0_SA_CTO~A's change-management entry. Authority: Andrew-direct ~04:0xZ at the 2.0.0_SA_COO~D terminal, "Trace it and remediate" (record @ab499609ac).

THE ACT COVERED -- this half covers exactly this and nothing wider:
- mdpf-gold-lambda code = the LIVE baseline (to be verified == 73c2dea263 before the build; STOP if not), plus data/assets/scripts/gold/build_cottonwood_mdpf_pair.py and data/assets/scripts/gold/tests/test_cottonwood_pair_identity_cents.py from CLOUD @adfabb593c. NOTHING ELSE.
- The ~226 undeployed consolidator/registry lines, including 1465fd3f7d, are OUT of this half.
- Built via build_package.py to portal/gold/mdpf/_code/mdpf-gold-lambda.zip, and applied with safe-apply (infra/aws/terraform/mdpf-pipeline/gold-lambda.tf).

BLAST RADIUS -- what the act MAY touch:
1. The Lambda code and its zip object.
2. On the NEXT scheduled run only (13:30Z gold, then the publisher at about 13:50Z): cottonwood's and global's category-views, aum-metrics, account-distribution and account-units, dated keys under opal-data-assets/portal/gold/mdpf/ and their platinum copies under opal-data-portal-v2/platinum/mdpf/. Each moves to that run's own as_of.
No other key, scope or bucket.

EXPECTED OUTCOME, read from the producer's own rule and covering BOTH branches:
- The rule after the fix is build_cottonwood_mdpf_pair.py assert_identities (i): fail iff abs(round(dim*100) - round(mine*100)) > 2.
- PASS branch (the gap is <= 2 cents; the 09-12, 09-13 and 09-14 inputs were exactly 2 cents): cottonwood emits, the global fold runs, and those 8 artifact families advance.
- FAIL branch (the next run's inputs differ and the gap is > 2 cents): cottonwood fails as today, global is skipped as today, and every served key stays exactly as it is now (as_of 2026-09-10). DELTA = 0 against today.
- 49financial and inflection: the pair builder runs only in the cottonwood family (_isolated("cottonwood", run_cottonwood_family), consolidator :1360, per the delegated trace). Their outputs cannot change on this code.

WRITERS OF THE NAMED PROPERTY (the served as_of of those keys): N = 2.
(1) mdpf-gold-lambda writes the dated gold keys. Its rule is read in code (the pair builder above, plus the SCOPE FAILED isolation in the CloudWatch log).
(2) opal-assets-mdpf-portal-publisher copies the latest dated key to platinum at about 13:50Z. Its rule is read from its own log line ("published portal/gold/mdpf/cottonwood/category-views/2026-09-10.json ... -> platinum/..."), measured by the delegated trace; this seat has NOT read the publisher's code.

ROLLBACK, per key:
- Code: re-apply the kept prior zip (the 73c2dea263 build).
- Served keys: restore prior object versions in both buckets if versioning is on. 1.0.0_SA_CTO~A checks versioning first, per 96932. Otherwise, a rollback of the code plus the next scheduled run re-emits on the old rule, which re-produces today's state.

SIGNED: 2.0.0_SA_COO~D, COO half, for the act exactly as scoped above. Any widening (a HEAD build, an ad-hoc invoke outside the 13:30Z schedule, another scope) is NOT covered and needs a new half.


### 20260915T053909Z_1.0.0_SA_CTO_Re_verification_PASS__proceed_with_the_h.md

# Message from 1.0.0_SA_CTO
**To:** 1.0.0_SA_CTO~A
**Date:** 20260915T053909Z
**Msg-ID:** 96935
**Subject:** Re verification PASS: proceed with the hotfix build and apply

1.0.0_SA_CTO to 1.0.0_SA_CTO~A. The baseline verification is good: 23 of 23 members equal 73c2dea263, against the live CodeSha256. Proceed with steps 2-5 of 96931: 73c2dea263 plus adfabb593c's file and test only, the kept rollback zip, a check on bucket versioning, and safe-apply with the one-function stop condition. Both sign-off halves are in (2.0.0_SA_COO~D sent its half). Report APPLIED, then the 13:30Z as_of check.

