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
| L1 | s3-prefix | the runner bundle re-minted through safe-deploy (12 members, all equal to HEAD after the mint); Branch B version W2WragrP52i8M7MfL22oXVPuHsTjyVLO named | version before and after, 12 of 12 |  | OPEN |
| L2 | s3-prefix | the refresh Lambda zip: built digest equals the pin I7T8wRYm.., uploaded and head-object verified; Branch B zip version named | digest, head-object |  | OPEN |
| L3 | tf-lambda | ONE safe-apply of the directory root, plan 3 add 1 change 0 destroy at the named addresses, clean re-plan, three new environment keys | plan counts, replan, key names |  | OPEN |
| L4 | verify | the simulation battery: two allowed arms and five denied arms | simulation table |  | OPEN |
| L5 | activation | the secret value put ONCE (never printed), version count 1 | put count |  | OPEN |
| L6 | verify | ONE QA run, four checks PASS, the assume fact recorded | qa block |  | OPEN |
| L7 | git | the record, proof and ledger committed with explicit paths | commit ids |  | OPEN |

## Log

- 20261017T080728Z OPENED by 0.7.0_AE_CloudOps~IB2 with 7 leg(s)
