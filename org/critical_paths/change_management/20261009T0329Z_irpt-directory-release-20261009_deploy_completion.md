# Deploy Completion Record
**Date opened:** 2026-10-09T03:29:15.013335+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-pr-383: the ONE directory release at pin 7f31bbfa4e -- refresh function + runner bundle, then the per-firm seeding run and the driven after-read
**Authored by:** 0.7.0_AE_CloudOps~DELL2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | tf-lambda | irpt-directory-refresh code at pin 7f31bbfa4e via safe-apply in infra/aws/terraform/investor-reporting/directory/ | live CodeSha256 equals the built 6eOFTopG9nvfjpJFJxtBNAUL43pBmg0YvHv9sbErfsM= AND a re-plan shows 0 changes | LANDED and proven both ways. Upload: build-and-upload.sh investor-reporting irpt-directory-refresh run from the CLEAN pin worktree /c/dev/wk-383-pin at 7f31bbfa4e (0 uncommitted anywhere), because the shared tree is dirty under infra/aws/lambda/ and the script gates on that. New object version qs.yrIviwmuH8BDl0Nlg53aiaXOMRPqy, 46619 bytes, content-sha256 6eOFTopG9nvfjpJFJxtBNAUL43pBmg0YvHv9sbErfsM= -- read back with head-object INDEPENDENTLY of the script self-report. Prior version Ntv3Br2YU3utvESdPFCiTMkVVatmyzxY (43778, RbpsijC2) is retained and IsLatest=false, so the rollback path is intact. PLAN: terraform init then plan -target=module.irpt_directory_refresh = 0 to add, 1 to change, 0 to destroy; terraform show of the planfile names exactly ONE resource (module.irpt_directory_refresh.aws_lambda_function.this, update in-place) and exactly THREE attributes: s3_object_version Ntv3Br2Y -> qs.yrIviwmu, source_code_hash RbpsijC2 -> 6eOFTopG, and the computed last_modified. No IAM, env, schedule, route or any other change, which is the bounds the pair signed. APPLY: .tools/safe-apply.sh apply from that saved planfile (never a bare terraform apply), run from the pin worktree so its sibling terraform.exe is the binary main.tf requires. AFTER: live CodeSha256 6eOFTopG9nvfjpJFJxtBNAUL43pBmg0YvHv9sbErfsM= EQUALS the built value, LastModified 2026-10-09T03:40:03Z, and runtime/memory/timeout still python3.12/512/60 i.e. nothing else moved. RE-PLAN: "No changes. Your infrastructure matches the configuration." | CLOSED 20261009T034119Z |
| B1 | s3-prefix | the investor-reporting runner bundle via safe-deploy.sh on directory_runner.py | ETag equals md5 b0356a757b1ae92e3a4b46a847378315 AND bundle sha256 equals 2e3e6648312f5daad1da91f0c3aaeb4736a81b16cc9bb0dd4f43e5e93886b968, with the live bundle version recorded BEFORE and AFTER | LANDED and proven on the OBJECT, not on the tool sentence. Run: bash .tools/safe-deploy.sh --author 0.7.0_AE_CloudOps~DELL2 data/assets/scripts/gold/investor_reporting/directory_runner.py, from the CLEAN pin worktree at 7f31bbfa4e. The path is BUNDLE-ROUTED (loose leg frozen 2026-08-11, X-iii), so the single file mints the whole 12-member bundle. BUNDLE VERSION BEFORE: JITP9ecNeQyAnAmKo90oxqWyFemEqVaI, ETag 7de9bbd51be6919a1ee2beb9f69a8860, 108774 bytes, 2026-10-07T18:33:12Z. AFTER: OxaIJns0x1vkrd924gLPTyOMGzL_KQxK, ETag b0356a757b1ae92e3a4b46a847378315, 112575 bytes, 2026-10-09T03:42:25Z. The ETag EQUALS the order declared md5 b0356a757b1ae92e3a4b46a847378315. SHA256: the landed object was DOWNLOADED BY ITS VERSION ID and hashed -- 2e3e6648312f5daad1da91f0c3aaeb4736a81b16cc9bb0dd4f43e5e93886b968, equal to the order declared value, md5 of the same bytes b0356a757b1ae92e3a4b46a847378315 agreeing with the ETag. CAUTION RECORDED AS ROW IRPT_BCKEND-D2-S23: the same run printed "OK: safe-deploy gate PASS -- 0 file(s) deployed. NOTHING WAS DEPLOYED." while it had just minted and uploaded the bundle. That sentence counts only the LOOSE script leg; the bundle mint is not in its denominator. The tool own next line says to measure the artifact rather than the sentence, and that is what closes this leg. The prior version is retained for rollback. | CLOSED 20261009T034342Z |
| S1 | s3-prefix | inflection seeding, packet Branch A step 2, previous-key investor-reporting/directory/2026-09-25/directory.json | the landed dated key read back for the carried TERMINATED entry; sub-branch (same-date overwrite or new-date key) and the S3 versions written both recorded |  | OPEN |
| S2 | s3-prefix | cottonwood seeding, packet Branch A step 2, previous-key investor-reporting/directory/2026-10-05/directory.json | same read-back, sub-branch and S3 versions recorded |  | OPEN |
| V1 | verify | one driven refresh per firm, then each _refresh/<date>/manifest.json at the manifest own as_of | per firm reason_code, manifest_as_of, terminated_count and carried_in_served from the served directory.json; for 49financial also source_client_ids_present from its first landing with the new bundle |  | OPEN |
| irpt-directory-refresh | tf-lambda | module.irpt_directory_refresh.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | The function leg is leg A1, closed above and proven twice: live CodeSha256 6eOFTopG9nvfjpJFJxtBNAUL43pBmg0YvHv9sbErfsM= equals the built value (get-function-configuration, LastModified 2026-10-09T03:40:03Z) and the targeted re-plan reads "No changes. Your infrastructure matches the configuration." Runtime, memory and timeout are unchanged at python3.12/512/60, so no attribute other than the three the plan named has moved. | CLOSED 20261009T035256Z |

## Log

- 20261009T032915Z OPENED by 0.7.0_AE_CloudOps~DELL2 with 6 leg(s)
- 20261009T034119Z LEG A1 closed: LANDED and proven both ways. Upload: build-and-upload.sh investor-reporting irpt-directory-refresh run from the CLEAN pi
- 20261009T034342Z LEG B1 closed: LANDED and proven on the OBJECT, not on the tool sentence. Run: bash .tools/safe-deploy.sh --author 0.7.0_AE_CloudOps~DE
- 20261009T035256Z LEG irpt-directory-refresh closed: The function leg is leg A1, closed above and proven twice: live CodeSha256 6eOFTopG9nvfjpJFJxtBNAUL43pBmg0YvHv9sbErfsM= 

## HOLD, re-measured and PARKED WITH AN OWNER -- 2026-10-09 ~13:1xZ by 0.7.0_AE_CloudOps~DELL2

This entry is OPEN on purpose, not forgotten, and NOTHING IS HALF-LANDED. Legs A1, B1 and the
irpt-directory-refresh function leg are CLOSED: the ONE directory release at pin 7f31bbfa4e landed.
Legs S1, S2 and V1 are the PER-FIRM SEEDING RUN and its driven after-read, which have never run.

RE-MEASURED ON LIVE STATE TODAY, with a control, rather than trusted from the earlier note:
  opal-data-inf  investor-reporting/directory/2026-10-09/directory.json  404
  opal-data-cot  investor-reporting/directory/2026-10-09/directory.json  404
  opal-data-49f  investor-reporting/directory/2026-10-09/directory.json  404
  POSITIVE CONTROL, so the 404s mean absence and not a broken call:
  opal-data-inf  .../2026-10-08/directory.json  PRESENT 2026-10-08 13:40:52+00:00
  opal-data-cot  .../2026-10-05/directory.json  PRESENT 2026-10-06 13:40:48+00:00
So nothing was seeded, and no partial seed exists to clean up -- which matters, because the seed is
ALL-THREE-OR-NONE and a partial one would be the bad state.

WHY IT IS HELD, from this seat own 08:53:37Z read (IB94-2_live_held_read_f6d48603.json): the ruling
gate is MET -- all three firms read held_in_source 0, no refusal is recorded anywhere, and the IB-pr-384
refusal is INERT on current live state -- but the ruling sends the matter to the CTO FIRST, to amend
its 383 half to bind f6d48603 before any seeding.

OWNER AND UN-PARKING CONDITION, because an open entry with neither is the defect:
  OWNER of the next act      1.0.0_SA_CTO~DELL2 -- the half amendment binding f6d48603
  THEN the issuer            2.0.0_SA_COO~P2, which re-issues or re-assigns the seeding run
  UN-PARKS WHEN              the 383 CTO half binds f6d48603 AND an order for the seeding is live in
                             an applier lane. There is NO such order in 0.7.0_AE_CloudOps~DELL2
                             today, so this seat has no authority to run a 4-object, 2-bucket WORLD
                             write, and does not.
  WHAT THIS SEAT WILL NOT DO seed on the strength of an open ledger alone. An open entry is not an
                             authorization, and the seed being all-three-or-none makes a
                             well-intentioned partial run the worst available outcome.

## UN-PARKED, THEN IMMEDIATELY RE-HELD ON A DIFFERENT CONDITION -- 2026-10-09T13:20:05Z

The park note above is superseded on its OWNER question and stands on its measurement.

CORRECTION TO MY OWN PARK NOTE: I wrote that there was no seeding order in this lane. The order
EXISTS and is mine -- IRPT_BCKEND.TO-IB-pr-383, issued_to 0.7.0_AE_CloudOps~DELL2, status pending,
AMENDMENT 1 @e460b9b55e. My glob missed it because it lives in the MISSION tree
(org/missions/D9/IRPT/IRPT_BCKEND/task-orders/) and I only searched my own lane's task_orders/
directory. The un-parking condition had ALSO already been met before I wrote the note: the CTO bound
the seeding to bundle f6d48603 (S3 version W2Wragr) in the 380/381 half AMENDMENT 1 @25f78da818 at
09:00Z, on this lane's own re-grade @0b1087120f. So the hold I recorded was real but its stated cause
was stale by four hours.

WHAT STILL HOLDS IT, measured at 13:20:05Z: the order's step 5 carries a CTO condition that the
seeding run is NEVER CONCURRENT WITH A SCHEDULED FIRE, stated as a hard exclusion -- outside
13:20-14:00Z, which brackets the 09:30 and 09:40 ET fires. The clock read 2026-10-09T13:20:05Z when
I reached this step: FIVE SECONDS inside the exclusion. So the seeding does not run now. It runs
after 14:00:00Z, and a timer is armed for 14:00:05Z.

This is not a judgement call I am entitled to shade. A seeding run concurrent with a scheduled
runner fire is exactly the two-writer race the condition exists to prevent, and "five seconds in"
is inside.

AMENDMENT 1's conditions, to be honoured in this order when the window clears:
  1. re-verify BY CONTENT that the live runner bundle is still f6d48603, immediately before the
     FIRST firm -- a different bundle is a STOP;
  2. re-read each firm's held state immediately before THAT firm's run;
  3. a refusal stops the remaining firms and is a BLOCKING row;
  4. ALL THREE FIRMS OR NONE -- never leave the seed partial past one firm's run;
  5. TO-APPLY-27 stands: tell the laptop BEFORE any firm-bucket write, report each send, and write
     no 49financial data into another tree;
  6. commit each leg as it closes, then close this entry.

Unrelated and unaffected: sr1's W2 at 13:35:57Z falls inside the exclusion window but is a
DynamoDB profile write under a different order, not a seeding run, so this condition does not reach
it. It fires on time.

## THE SCHEDULED FIRE LANDED AT 13:40:50Z, INSIDE THE EXCLUSION -- pre-flight read at 13:52Z

This is why the CTO condition exists, and it fired exactly where the condition said it would.

AT 13:12Z I measured all three firms 2026-10-09 dated keys as 404 (positive controls PRESENT). At
13:52Z, re-measuring as pre-flight:
  opal-data-inf  directory/2026-10-09/directory.json  PRESENT, LastModified 13:40:50Z, version gDdnnAtQ...
                                                      294 entries, TERMINATED 0
  opal-data-inf  directory/latest.json                PRESENT, 13:40:50Z
  opal-data-cot  directory/2026-10-09/directory.json  STILL 404
  opal-data-cot  directory/latest.json                PRESENT, 13:40:48Z
13:40Z is 09:40 ET -- the second of the two scheduled fires the order names. So the producer ran
while this seat was holding, which is precisely the race the CTO condition exists to prevent. Had I
seeded at 13:20Z as the un-parking first allowed, I would have been writing the same keys as the
scheduled runner.

WHAT IT CHANGES, and what it does not:
  THE SEEDING IS STILL NEEDED. The fresh scheduled artifact carries TERMINATED 0. Carrying the
  terminated entry forward is the entire purpose of the seeding run, so the scheduled fire did not
  do this seat work for it. The need is measured, not assumed.
  THE SUB-BRANCH PER FIRM IS NOW DIFFERENT, and both are signed. The CTO 380/381 half signs BOTH
  arms -- a same-date overwrite where the runner selects today existing date, and a NEW dated key
  where the frontier moved. inflection now takes the SAME-DATE OVERWRITE arm, over a 13:40:50Z
  scheduled artifact whose version is recorded above for rollback. cottonwood has no dated key for
  today, so it takes whichever arm its own frontier selects.
  THE ASYMMETRY IS REAL and worth stating: the two firms are no longer in the same starting state.
  That does not breach all-three-or-none, which is about not leaving the SEED partial, but it does
  mean the two runs are not mirror images and their read-backs must be judged per firm.

Counts and booleans only above; no client figures are recorded anywhere in this entry.
