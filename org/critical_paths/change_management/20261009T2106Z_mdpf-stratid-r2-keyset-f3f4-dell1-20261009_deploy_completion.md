# Deploy Completion Record
**Date opened:** 2026-10-09T21:06:06.650424+00:00
**Status:** OPEN
**Deploy:** MDPF_STRATID.TO-APPLY-R2 forward fix F3/F4 @5a961c8bf2: rebuild mdpf-gold-lambda at 88e974ca10 (apply_sma_sleeve_overlay pads unidentified_strategies on every scope), targeted apply, qa_local 16 of 16 errors []
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| F3 | s3-prefix | data/mdpf/scripts/gold/mdpf_gold_consolidator.py at 88e974ca10 -- blob 8582352ca70251a1055276069865357e95696af5, sha256 2cd88dc41ce6a0bbfc4ca8495a20a868ad7e9a55117e22172d35ec602e45460f -- NAMED on this entry for the next push to the runner's code prefix, per 2.0.0_SA_COO~S1 msg 3180 | the pushed blob equals the named blob id at the pushed rev (deploy-ledger-names.py:32-51 reads the sentinel), and the gate reads LEDGERED rather than HELD |  | OPEN |
| F4-BUILD | s3-prefix | opal-data-assets portal/gold/mdpf/_code/mdpf-gold-lambda.zip -- the package rebuilt at pin 88e974ca10, which CONTAINS F2 79e30151a6 and 55c3cc4642 (both measured by merge-base) | the zip carries the padded consolidator (its member bytes equal git show 88e974ca10 of the path) and opal_unidentified.py; the served object reads back equal to the local build |  | OPEN |
| F4-VERIFY | verify | the gold Lambda's qa_local read of the padded build | 16 of 16 A4 objects with errors [] -- the arms the 20:15:26Z and 20:37:11Z runs failed, each for a different reason; plus zero writes measured as a pre/post set difference with the denominator printed |  | OPEN |
| mdpf-gold-lambda | tf-lambda | aws_lambda_function.mdpf_gold | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261009T210606Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 4 leg(s)
