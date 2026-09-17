# Deploy Completion Record
**Date opened:** 2026-09-16T17:15:01.909202+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260916T173205Z
**Deploy:** AMGT-rk-2 ISSUER AMENDMENT 9 fix-forward (ruling 23463): package lib/research/rules/data/peer_overlap.json + figure_units.json, guard peer.py's read (never crash at import), redeploy opal-amgt-scoped-api and prove a pre/post GET-route non-regression census (AC7) plus a repo-relative packaging census (AC8).
**Authored by:** 0.9.0_WK_AMGT_RESAPP~24
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-deploy GET route census of opal-amgt-scoped-api | AC7 CENSUS_MODE=pre JSON written + printed census, CodeSha256 recorded | pre-deploy census (CENSUS_MODE=pre, before any deploy this session): CodeSha256 9ubWPnhzHs88JSKPwhvemXxpbGdf9PZkz2c1qBxBqSk= LastModified 2026-09-16T16:18:57Z (the co-signed rolled-back state); GET census 7 of 8 200 (/print 500 pre-existing); written to org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~24/rk-2.route_census_pre.json | CLOSED 20260916T173117Z |
| L2 | verify | post-deploy GET route census of opal-amgt-scoped-api | AC7 post-run: sets_equal True, lost empty, gained empty, CodeSha256 changed from pre | post-deploy census: CodeSha256 x3KrEBvZVFmZqZ1KLsuzu6A7fedugZoxfS7+eoJiMUw= LastModified 2026-09-16T17:23:29Z; GET census 7 of 8 200, lost [], gained [] vs pre (sets_equal True); deployed_changed_since_pre True; /print stays pre-existing 500 (AMGT-rk-6's remit), no regression on the 200-set. AC4 (thesis BA_US_Equity): 200 model_status SERVED header_figures 14 fiscal_year_figures 165. AC5 (overlay BA_US_Equity): 200 comparable_name 'Deere & Company' packs dict len 2. | CLOSED 20260916T173147Z |
| opal-amgt-scoped-api | tf-lambda | module.scoped_amgt_api.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | terraform apply (safe-apply.sh, HALT_ACK=1, halt-gate-check rc0, comp-tagauthz PASSED, tombstone-gate CLEAN) targeted at aws_iam_role_policy.scoped_amgt_api_grants + module.scoped_amgt_api.aws_lambda_function.this: Apply complete! Resources: 0 added, 2 changed, 0 destroyed -- matching the co-signed blast radius exactly (IAM policy restores the derived/model_block/* limb on both GetObject and ListBucket StringLike, Lambda source_code_hash/s3_object_version move to the uploaded artifact x3KrEBvZVFmZqZ1K.../X2ZRUM2EXxnSk2vVgtT9JYn6FET9SziA). Verify-on-served = L1+L2 census pair above (sets_equal True) plus AC4/AC5 live invokes. | CLOSED 20260916T173147Z |

## Log

- 20260916T171501Z OPENED by 0.9.0_WK_AMGT_RESAPP~24 with 3 leg(s)
- 20260916T173117Z LEG L1 closed: pre-deploy census (CENSUS_MODE=pre, before any deploy this session): CodeSha256 9ubWPnhzHs88JSKPwhvemXxpbGdf9PZkz2c1qBxB
- 20260916T173147Z LEG L2 closed: post-deploy census: CodeSha256 x3KrEBvZVFmZqZ1KLsuzu6A7fedugZoxfS7+eoJiMUw= LastModified 2026-09-16T17:23:29Z; GET censu
- 20260916T173147Z LEG opal-amgt-scoped-api closed: terraform apply (safe-apply.sh, HALT_ACK=1, halt-gate-check rc0, comp-tagauthz PASSED, tombstone-gate CLEAN) targeted at
- 20260916T173205Z CLOSED -- all 3 legs proven
