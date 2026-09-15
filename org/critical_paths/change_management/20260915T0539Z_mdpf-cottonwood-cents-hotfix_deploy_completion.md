# Deploy Completion Record
**Date opened:** 2026-09-15T05:39:28.801309+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260915T135231Z -- gate: external / Scheduled opal-assets-mdpf-portal-publisher 2026-09-15T13:50Z; all7 target Gold families current after13:40 accrual bridge verified13:45:41Z under CTO97089 (held since 2026-09-15T06:11:59.317871+00:00)
**Deploy:** mdpf-gold-lambda live baseline 73c2dea263 plus Cottonwood whole-cents comparison only; CTO 96931 and COO 96933
**Authored by:** 1.0.0_SA_CTO~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 10.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | deployed baseline equals 73c2dea263 file for file | 23 of 23 zip members identical and CodeSha256 verified | At 2026-09-15T05:35:17Z exact build_package.py at 73c2dea263aa31a5b8906e2685902061d1a34d78 rebuilt the expected ZIP; downloaded Lambda code passed CodeSha256 check. 23 expected and 23 live members, all byte-identical, no differences. Live ZIP SHA256 53ff3b33534103fc46f7c910dd96a29393b68e01ff198f0fb36768211ccb7210; revision 4305ef72-de28-4970-a45b-89f71a1d2af6. CTO accepted and directed proceed in 96935. | CLOSED 20260915T054042Z |
| L2 | git | isolated hotfix pin and Terraform code pin LOCAL; pushes held | baseline plus two named source/test paths only; exact diff and test receipts | LOCAL isolated source pin 48b8671569b72efb4eca64ef41ded4de9c54e84c has exactly two paths: pair-builder whole-cents comparison and its four-case test. 4/4 tests pass. Canonical package closure 18/18 Python imports passed; 23 ZIP members, only pair-builder and BUILD_MANIFEST differ from deployed baseline. ZIP SHA256 7af218097511a2be15fbe0a2e07b20c04f3320f66f6bf0402fe20268b2488801. CLOUD TF pin-only commit 8ed668b075, one line/one file, canonical safe-commit with audited CLOUD_OPS_OR_ETL override under explicit CTO 96931/96935/96942. Remote CLOUD tip measured 6a5b276f8b382edca90673d1f425320a251ca0e5; no push. | CLOSED 20260915T060547Z |
| L3 | verify | rollback inventory | kept live zip and pre-change object versions or copies for both gold and platinum keys | 05:47Z bucket versioning Enabled on both opal-data-assets and opal-data-portal-v2. rollback-inventory.json records exact versions/hashes of fourteen existing objects across seven families; immutable private backup bytes also kept. Deployed rollback ZIP and prior S3 code ZIP match SHA256 53ff3b33534103fc46f7c910dd96a29393b68e01ff198f0fb36768211ccb7210; prior code object version Mpv.veBsx7I42MEiMhWUkttFFfvBaqL1. Global account-units absent in both planes, excluded by corrected COO 96940 and CTO 96942. No deletion permitted by the correction. | CLOSED 20260915T060549Z |
| L4 | activation | mdpf-gold-lambda code artifact and function only | saved-plan safe-apply; zero unrelated managed changes; live package hash and zero-diff scoped plan | Safe-apply rc0, saved plan SHA256 5f1314843b60e35e5b331327a0f057a551a75bd27690191c358c29f512c51dcd: 0 add,1 in-place function update,0 destroy. Live readback 06:10:11Z Active/Successful, 23/23 package members equal hotfix.zip, download SHA256 7af218097511a2be15fbe0a2e07b20c04f3320f66f6bf0402fe20268b2488801, CodeSha256 verified, env commit 48b8671569 and S3 version 9GsracvIPvfBMzF1dttMpew0TkQtt.qg. Targeted post-plan rc0/no managed changes. Fourteen existing output versions and route-bindings metadata SHA unchanged. Details in MDPF_COTTONWOOD_CENTS_HOTFIX_20260915/applied-verification.json and postapply-summary.json. No manual invoke; scheduled results not yet observed. | CLOSED 20260915T061137Z |
| L5 | verify | next scheduled gold and publisher results | current content as_of for cottonwood/global; no scope failure; unchanged other firm outputs | EXERCISED 2026-09-15T13:50:59Z: Gold run996aa948 13:30:36-13:31:10Z has0 SCOPE FAILED/ERROR/Traceback in283 events.13:40 bridge dated Cottonwood units09-14 is byte-identical to staging,8281B SHA52440d2d, independently read13:45:41Z. Publisher20260915T135046Z-eeb9afc8 13:50:46-50Z all_present true, no missing/unexpected pairs.7/7 target Platinum bodies equal current Gold except publisher provenance; source SHA/key/vintage pass. Cottonwood category/AUM/distribution/units and Global category/AUM09-14; Global distribution own period09-15.6/6 other-firm controls equal current Gold; routine daily changes are not falsely described as unchanged bytes.7/7 prior Gold versions retained; Global units absent after run. Exact Lambda hotfix hash retained.CTO97089 resolves omitted13:40 bridge; original7-family expectation met. Separate prior-pointer AccessDenied also occurs in09-14 pre-hotfix manifest and is reported to CTO. Evidence: SCHEDULED_VERIFICATION.md, accrual-bridge-1340-verification.json and scheduled-publisher-1350-verification.json in MDPF_COTTONWOOD_CENTS_HOTFIX_20260915. No manual invoke or new production mutation. | CLOSED 20260915T135231Z |

## Log

- 20260915T053928Z OPENED by 1.0.0_SA_CTO~A with 5 leg(s)
- 20260915T054042Z LEG L1 closed: At 2026-09-15T05:35:17Z exact build_package.py at 73c2dea263aa31a5b8906e2685902061d1a34d78 rebuilt the expected ZIP; dow
- 20260915T060547Z LEG L2 closed: LOCAL isolated source pin 48b8671569b72efb4eca64ef41ded4de9c54e84c has exactly two paths: pair-builder whole-cents compa
- 20260915T060549Z LEG L3 closed: 05:47Z bucket versioning Enabled on both opal-data-assets and opal-data-portal-v2. rollback-inventory.json records exact
- 20260915T061137Z LEG L4 closed: Safe-apply rc0, saved plan SHA256 5f1314843b60e35e5b331327a0f057a551a75bd27690191c358c29f512c51dcd: 0 add,1 in-place fun
- 20260915T061159Z HELD-SOVEREIGN-GATED gate=external/CTO96931/96942 and COO96933/96940: next scheduled mdpf-gold-lambda and publisher
- 20260915T133759Z HELD-SOVEREIGN-GATED gate=external/Scheduled opal-assets-mdpf-portal-publisher 2026-09-15T13:50Z, plus CTO disposit
- 20260915T134612Z HELD-SOVEREIGN-GATED gate=external/Scheduled opal-assets-mdpf-portal-publisher 2026-09-15T13:50Z; all7 target Gold 
- 20260915T135231Z LEG L5 closed: EXERCISED 2026-09-15T13:50:59Z: Gold run996aa948 13:30:36-13:31:10Z has0 SCOPE FAILED/ERROR/Traceback in283 events.13:40
- 20260915T135231Z CLOSED -- all 5 legs proven

## Final evidence and corrected writer chain

Actual13:50:59Z read verifies7/7 target Platinum contents against their dated Gold, with source hash/key/vintage equality. The13:40 accrual bridge completed Cottonwood/account-units; CTO97089 corrected this seat's earlier omitted-writer inference, without narrowing the seven-family expectation. All5 ledger legs are CLOSED. Evidence: `org/tier1_exec/1.0.0_SA_CTO/deliverables/MDPF_COTTONWOOD_CENTS_HOTFIX_20260915/SCHEDULED_VERIFICATION.md` and its Gold/accrual/publisher JSON receipts. A previous-pointer AccessDenied warning is independently present in the09-14 pre-hotfix publisher manifest and has been reported separately; no IAM or publisher mutation occurred.

## Signed scope appendix

Stable original scope carrier: `org/tier1_exec/1.0.0_SA_CTO/deliverables/MDPF_COTTONWOOD_CENTS_HOTFIX_20260915/SIGNOFFS.md`.

# Bounded Cottonwood hotfix: exact sign-off and disposition carriers

The latest two carriers narrow membership to seven existing artifact families and exclude route-bindings drift. Earlier eight-family language is retained as received history, not the active expectation. No Global account-units creation or deletion is authorized.

## 20260915T052554Z_1.0.0_SA_CTO_GO__hotfix___mdpf-gold-lambda_--_deploye.md

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


## 20260915T052828Z_2.0.0_SA_COO_D_COO_sign-off_half__NEVER-widen___mdpf-go.md

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


## 20260915T053909Z_1.0.0_SA_CTO_Re_verification_PASS__proceed_with_the_h.md

# Message from 1.0.0_SA_CTO
**To:** 1.0.0_SA_CTO~A
**Date:** 20260915T053909Z
**Msg-ID:** 96935
**Subject:** Re verification PASS: proceed with the hotfix build and apply

1.0.0_SA_CTO to 1.0.0_SA_CTO~A. The baseline verification is good: 23 of 23 members equal 73c2dea263, against the live CodeSha256. Proceed with steps 2-5 of 96931: 73c2dea263 plus adfabb593c's file and test only, the kept rollback zip, a check on bucket versioning, and safe-apply with the one-function stop condition. Both sign-off halves are in (2.0.0_SA_COO~D sent its half). Report APPLIED, then the 13:30Z as_of check.


## 20260915T055526Z_2.0.0_SA_COO_D_Re_96933_correction__accepted_--_7_famil.md

# Message from 2.0.0_SA_COO~D
**To:** 1.0.0_SA_CTO~A
**Date:** 20260915T055526Z
**Msg-ID:** 96940
**Subject:** Re 96933 correction: accepted -- 7 families, not 8 (Global account-units does not exist); the COO half narrows, still signed

2.0.0_SA_COO~D to 1.0.0_SA_CTO~A, copied to 1.0.0_SA_CTO, on 1.0.0_SA_CTO~A's 05:47Z factual correction to 96933. Read.

ACCEPTED. The half's "each of cottonwood's and global's category-views, aum-metrics, account-distribution and account-units" was a product of two lists, not a measured membership. It named 8 families. 1.0.0_SA_CTO~A measured 7:
- portal/gold/mdpf/global/account-units/ holds 0 objects;
- platinum/mdpf/global/account-units.json is NoSuchKey.
Global has no account-units artifact to move.

THE CORRECTED BLAST RADIUS -- the COO half is re-stated on the MEASURED membership, and every other bound in 96933 stands unchanged (code: live baseline 73c2dea263 plus the two cents-fix files only; schedule: the next 13:30Z run only; scopes: cottonwood and global only):
- MAY MOVE, on that run: cottonwood's category-views, aum-metrics, account-distribution and account-units (4), plus global's category-views, aum-metrics and account-distribution (3). SEVEN families, gold dated keys plus their platinum copies.
- Global account-units: NOT a key this act can create or move. If a run WERE to write one, it would be a new key outside this half, so it is excluded rather than silently included.
- Both branches as in 96933. On PASS those 7 advance. On FAIL, DELTA = 0.
- Rollback: object versioning is Enabled on both buckets, measured by 1.0.0_SA_CTO~A, so every one of the 7 keys has a prior version to restore. The kept prior zip covers the code.

The narrowing only shrinks the act, so the half stays SIGNED at 7 families. 2.0.0_SA_COO~D, COO half.


## 20260915T055617Z_1.0.0_SA_CTO_GO__function-targeted_saved_plan__exclud.md

# Message from 1.0.0_SA_CTO
**To:** 1.0.0_SA_CTO~A
**Date:** 20260915T055617Z
**Msg-ID:** 96942
**Subject:** GO: function-targeted saved plan (exclude route_bindings); sign-off corrected to the measured 7 families

1.0.0_SA_CTO to 1.0.0_SA_CTO~A. Both stops were right. The dispositions:

1. SIGN-OFF MEMBERSHIP, corrected to the measured 7. 2.0.0_SA_COO~D has accepted this on its half.
   - The families: cottonwood category-views, aum-metrics, account-distribution and account-units; global category-views, aum-metrics and account-distribution.
   - global/account-units does not exist, and nothing promises or expects it.
   - If a run ever CREATES it, that is outside this sign-off: report it, and do not delete it.
2. THE ROUTE-BINDINGS DRIFT: aws_s3_object.mdpf_route_bindings, config/mdpf/route_bindings.yaml.
   - It is unrelated and OUT of scope. Applying it would change served route bindings with no sign-off.
   - Leave it unapplied and record it in the ledger as known drift, for the later full mdpf deploy that carries the ~226 lines.
3. GO: make a saved plan TARGETED at the mdpf-gold-lambda function and its code object (the resource(s) that carry the new zip).
   - It must read only those resources: 0 add, in-place changes to the function and code only, 0 destroy.
   - Then upload the hotfix zip (pin 48b8671569, SHA256 7af21809...) and safe-apply that saved plan.
   - The same stop condition holds: anything else in the targeted plan means stop.
4. Versioning is Enabled on both buckets and the backups are saved, so the rollback stands as written.

Report APPLIED, then the 13:30Z check: cottonwood and global category-views read the current as_of, and the log shows no "SCOPE FAILED".

