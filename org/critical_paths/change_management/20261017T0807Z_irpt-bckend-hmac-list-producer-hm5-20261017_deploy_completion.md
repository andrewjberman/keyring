# Deploy Completion Record
**Date opened:** 2026-10-17T08:07:28.346951+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND TO-IB-hm-5 (cell IB-hm-5, FWD-21): the HMAC list producer pair in the investor-reporting directory root: the runner bundle s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz FIRST (Branch B: live version W2WragrP5.., ETag 5547fa5e), then the refresh Lambda irpt-directory-refresh zip (Branch B: the prior S3 version whose content equals the live CodeSha256, named before any write) and the directory root apply (3 add 1 change 0 destroy), then the one secret value put to irpt/hmac-list/key, then ONE QA run. Census 97 worktrees, 0 open legs on the root, the function or the bundle; one describe-task-definition sweep (denominator printed in the record).
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | the runner bundle re-minted through safe-deploy (12 members, all equal to HEAD after the mint); Branch B version W2WragrP52i8M7MfL22oXVPuHsTjyVLO named | version before and after, 12 of 12 | bundle re-minted through safe-deploy: version W2WragrP5.. -> 7ywFHFyM.. (128452 bytes); 12 of 12 members equal git show HEAD; trading_calendar tests 27 passed before the mint; Branch B = W2WragrP5.. (ETag 5547fa5e) | CLOSED 20261017T083753Z |
| L2 | s3-prefix | the refresh Lambda zip: built digest equals the pin I7T8wRYm.., uploaded and head-object verified; Branch B zip version named | digest, head-object | BUILD_ONLY digest I7T8wRYmv11nytYpD7i+4XCwwvy6JUaB3fdsgtHyXmA= equals the pin; uploaded, write VERIFIED (size 47627); Branch B zip version = the pre-upload latest whose content equals the old CodeSha256 6eOFTopG.. (1 of 39 versions matched) | CLOSED 20261017T083753Z |
| L3 | tf-lambda | ONE safe-apply of the directory root, plan 3 add 1 change 0 destroy at the named addresses, clean re-plan, three new environment keys | plan counts, replan, key names | plan 3 add 1 change 0 destroy at the four named addresses, ONE safe-apply, replan No changes; live CodeSha256 = I7T8wRYm..; env keys IRPT_HMAC_LIST_URI_MAP, IRPT_HMAC_ROLE_ARN, IRPT_HMAC_SECRET_ID present | CLOSED 20261017T083754Z |
| L4 | verify | the simulation battery: two allowed arms and five denied arms | simulation table | simulation battery on irpt-hmac-list-stage-role: get_the_one_secret allowed, put_each_of_the_three_list_keys allowed; get_object, list_bucket, delete_object, put_on_a_neighbouring_key, get_any_other_secret all implicitDeny | CLOSED 20261017T083754Z |
| L5 | activation | the secret value put ONCE (never printed), version count 1 | put count | secret value put once (secrets.token_hex(32), in-process SDK call, never printed or written); version count 0 -> 1 | CLOSED 20261017T083754Z |
| L6 | verify | ONE QA run, four checks PASS, the assume fact recorded | qa block |  | OPEN |
| L7 | git | the record, proof and ledger committed with explicit paths | commit ids |  | OPEN |

## Log

- 20261017T080728Z OPENED by 0.7.0_AE_CloudOps~IB2 with 7 leg(s)
- 20261017T083753Z LEG L1 closed: bundle re-minted through safe-deploy: version W2WragrP5.. -> 7ywFHFyM.. (128452 bytes); 12 of 12 members equal git show 
- 20261017T083753Z LEG L2 closed: BUILD_ONLY digest I7T8wRYmv11nytYpD7i+4XCwwvy6JUaB3fdsgtHyXmA= equals the pin; uploaded, write VERIFIED (size 47627); Br
- 20261017T083754Z LEG L3 closed: plan 3 add 1 change 0 destroy at the four named addresses, ONE safe-apply, replan No changes; live CodeSha256 = I7T8wRYm
- 20261017T083754Z LEG L4 closed: simulation battery on irpt-hmac-list-stage-role: get_the_one_secret allowed, put_each_of_the_three_list_keys allowed; ge
- 20261017T083754Z LEG L5 closed: secret value put once (secrets.token_hex(32), in-process SDK call, never printed or written); version count 0 -> 1

## Carried notes (hand-written lines kept across re-renders)

- 20261017T0850Z NOTE L6 (QA) stays OPEN for the issuer by ruling (2.0.0_SA_COO~P2 msg 10432, AMENDMENT 1 of IB-hm-5): step 8 is STRUCK, no manual invoke of irpt-directory-refresh (it has no one-firm payload; a manual invoke would refresh all three firms). The QA is Monday 2026-10-19 13:30Z's scheduled fire, read by the issuer. Applier made 0 Lambda invokes.
