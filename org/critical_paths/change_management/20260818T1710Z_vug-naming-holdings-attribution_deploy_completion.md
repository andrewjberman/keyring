# DEPLOY COMPLETION LEDGER -- vug-naming-holdings-attribution

**Opened:** 2026-08-18T17:10Z by 1.0.0_SA_CTO~X (Andrew-direct task, this session)
**Status:** CLOSED 2026-08-18T17:35Z -- all legs verified, no stranded leg

## Scope

One Lambda: `yang-generate-holdings-attribution` (yang-pipeline, TF module
`generate_holdings_attribution`, artifact `yang-pipeline/yang-generate-holdings-attribution.zip`).
Change: display-name resolution `resolve_display_name` (DDB registry -> validated Excel value ->
ticker) replacing the blind Excel col-4 read that emitted benchmark weights as security names
(VUG rendered `1.61931034482759` on the portal Attribution Breakdown).
Companion non-deploy changes: VUG rows added to `seed_canonical_securities.py` CANONICAL_SECURITIES +
`_shared/etf_classification.py` ETF_NAME_OVERRIDES (repo registry parity); targeted DDB update-item on
`etf-classifications` VUG row (name -> 'Vanguard Growth ETF', attrs preserved, prior value recorded).
Ground truth: `org/tier1_exec/1.0.0_SA_CTO/deliverables/VUG_SECURITY_NAMING_ATOM_DECOMP_SSOT_20260818.md`.

## Legs

- [x] L1 commit source -- 78ae0b583e (lambda, GIT_COMMIT_AUTHOR_OVERRIDE=YANG_PIPELINE_DEPLOY),
      617c434397 (_shared, =CLOUD_OPS_OR_ETL), d6afb07089 (seeder, =POD4); all audited overrides,
      one lane per commit per Rule 14a
- [x] L2 build-and-upload -- artifact write VERIFIED (size=10358, sha256 metadata match);
      source map committed 4ebc9e7f4f
- [x] L3 plan: exactly `module.generate_holdings_attribution.aws_lambda_function.this` in-place,
      Plan: 0 add / 1 change / 0 destroy
- [x] L4 safe-apply clean (HALTGT: session serial stamped per LD-0290; two routine pending msgs
      reviewed -- no [STOP] -- HALT_ACK=1)
- [x] L5 0-diff re-plan: "No changes"
- [x] L6 record-terraform-deploy committed (source map + CHANGELOG, [skip ci]); tag
      yang-pipeline-v1.5.4 -- ⚠ CORRECTED 2026-08-18 ~1850Z: this line originally said "created
      locally" and THAT WAS FALSE -- the tag+push compound command was blocked WHOLE by the
      integrator-only push gate (tag never ran) and my follow-up verify was dropped; caught by
      0.0.0_AB_MSTR's integration census (tag existed NOWHERE). Retroactively minted at d8521bfc
      (the CHANGELOG's deployed_commit) so the version citations in this ledger/CHANGELOG/logs
      resolve; single-tag push requested from MSTR. Also noted: CHANGELOG carries TWO v1.5.4
      entries (the lane-blocked first record attempt left a working-tree append the override
      re-run committed alongside its own). PUSH DEFERRED TO THE INTEGRATION WINDOW per LD-0367/0368
      (integrator-only push on CLOUD; the push gate blocked and the standing law is lanes-commit /
      integrators-push -- NOT a stranded deploy leg: the AWS deploy is landed, 0-diffed, and
      byte-verified; only the git-record publication rides the hourly window)
- [x] L7 regenerated via production-shaped event (manifest: Model Portfolio Attribution
      20260731.xlsx, data_as_of 2026-07-31; rc 200, model_count 5). SERVED artifact verified:
      generated_at 2026-08-18T16:46:50Z; 414 rows / 56 tickers, membership identical to prior
      vintage; VUG name = 'Vanguard Growth ETF' in all periods; ZERO numeric/'--' names anywhere;
      non-name payload BYTE-IDENTICAL to the 08-04 vintage (names-only delta -- the regression
      control). Post-deploy package re-downloaded: deployed bytes == new repo bytes.

**Rollback:** re-upload prior artifact zip (S3 versioned bucket -- prior version retained) + apply;
DDB row prior value recorded in the ledger scope above; served JSON regenerates from either code
vintage on the same event.

**Closed:** (pending)
