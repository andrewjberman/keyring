# Deploy Completion Record
**Date opened:** 2026-10-02T13:58:17.281364+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS BD thread r3 RE-LAND (r4): every class in the mix + the identity read; half blob f926b46157, CTO batches 156/161/173
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| P | verify | portal PROD carries eb90f2ad (precondition, Andrew's promote) | ls-remote PROD + merge-base with positive and negative control | 13:56:40Z ls-remote origin refs/heads/PROD = f76b02acb684613699f9fe076c33a0e07c15e056 (tag portal-v2.1.194, Andrew's promote record @0abef798f7, CTO 104283 batch 173); merge-base --is-ancestor eb90f2ad f76b02acb6 = true; positive control old PROD b3a1d8a638 ancestor = true; negative control ed40c8ee (local-only commit) ancestor = false. | CLOSED 20261002T135905Z |
| M | git | safe-merge coo-m-bd-mix-classes into CLOUD + SERVE-RELEASE-ACK commit removing the four DEPLOY-SERVE-HELD lines; stop: merged tree differs from CLOUD only in the ten branch files | merge hash + tree check + release commit | Release commit b3442d6ea1 on the branch (SERVE-RELEASE-ACK line present, 1; four one-line hold blocks removed; 87 tests passed). Branch pre-merged with CLOUD at 66e2d3a9f7 (branch-own files vs merge-base f3a03263a6 = 10). Drain: safe-merge coo-m-bd-mix-classes -> CLOUD ac44b6aaaf 14:0xZ; tree check 'branch needed 10 file(s), dropped 0, foreign 0'; --verify-merge ac44b6aaaf same; git diff ac44b6aaaf^1..ac44b6aaaf = exactly the ten files the half names (stop condition holds). DEPLOY-SERVE-HELD count at HEAD 0 in C_06, D_03, D_04, lib/etf_classifier.py, lib/mix_views.py; each equals the branch bytes. Push state LOCAL. | CLOSED 20261002T140918Z |
| G | s3-prefix | safe-deploy C_06, D_03, D_04, lib/etf_classifier.py, lib/mix_views.py to opal-data-bd code/gold; prior VersionIds recorded first | comp-pipescript deployed MATCH rows + prior VersionIds | safe-deploy (HALT_ACK=1 on stale notices) 14:15-14:16Z rc 0: 'OK: safe-deploy gate PASS -- all 5 file(s) deployed and verified'; VERIFY OK comp-pipescript deployed for C_06, D_03, D_04, lib/etf_classifier.py, lib/mix_views.py. Prior -> new (VersionId, ETag): C_06 IHqg0qnU.. 8b1f012c -> fPhpkwlC.. 0095fc95; D_03 w8SLmmCx.. 346e7b0f -> 0nTag.d0.. 84f9bf8e; D_04 _WpGGia_.. a4b867d4 -> 45UVFc7X.. 816a77e9; lib/etf_classifier.py 4o.XQapb.. 884889c0 -> xXOwa2fz.. ed99af06; lib/mix_views.py yNVmq8qB.. d4467d4a -> i5Gk6rlV.. 2c8dbfd7 (rollback copies = the prior VersionIds, as the half names). ALSO SHIPPED (CODE_TREES shipped artifacts, not named in the half): code/gold/lib/_shared/ etf_classifications_dynamodb.py 181e1902 -> 4cc11d3e (classify_holdings KeyError fix, no call site), etf_classification_scheduled.py 6957dcc9 -> 61701 5f8 (write key list + two model fields; a scheduled item unchanged), etf_classification.py 58bfdb97 -> 4d63e303 (seed dict additions only; imported by neither runtime client). Prior VersionIds YM_emTRl.., pxHIiBNg.., 14g9k2TX.. -- surprise row filed. | CLOSED 20261002T142859Z |
| W | verify | C_06 watermark keys set back one partition (both keys), prior versions recorded | before/after watermark reads | 14:35:27Z copy-object (metadata COPY), opal-data-bd, runner i-01003b035d2988dfb stopped: gold/meta/client_timeseries_watermark.json <- EFUyS5MLWlZEmQQq_uiMfz9.CX4Ei30g (06:24Z version, data_as_of 2026-09-29), new VersionId 2SBjJiwYCWbcZnZEMi7MzAGuP1mgIQEK; gold/client_timeseries/_watermark.json <- P7l4aOgJoqTbbeuIm8yFeKZItEjb9rJA, new 0vjZhd5MZl9gq20wBa6WnAdbVcjLbmf8. Prior (pre-act) versions for rollback: eZ06TBW6DhNxezfZQh0FO48Yq5fNpzZ3 and gWkjNZCzLGCRhRRv2kO5ykU6O4pJwMuy (both data_as_of 2026-09-30, 07:41:41Z). Readback: both keys read data_as_of 2026-09-29, IsLatest = the new VersionIds. | CLOSED 20261002T143745Z |
| R | verify | ONE ad hoc QA run bd-gold-trigger incremental: mix_summary lists every class, sums to 100, unclassified <= 5.0 pct; identity hop counts in the log; z08327149 VXX structured/Hedge ties | served key reads + run log |  | OPEN |
| S | verify | next scheduled BD gold fire reads the same; one walked 49 Financial page on PROD readers | served key reads + page walk |  | OPEN |

## Log

- 20261002T135817Z OPENED by 2.0.0_SA_COO~M with 6 leg(s)
- 20261002T135905Z LEG P closed: 13:56:40Z ls-remote origin refs/heads/PROD = f76b02acb684613699f9fe076c33a0e07c15e056 (tag portal-v2.1.194, Andrew's pro
- 20261002T140918Z LEG M closed: Release commit b3442d6ea1 on the branch (SERVE-RELEASE-ACK line present, 1; four one-line hold blocks removed; 87 tests 
- 20261002T142859Z LEG G closed: safe-deploy (HALT_ACK=1 on stale notices) 14:15-14:16Z rc 0: 'OK: safe-deploy gate PASS -- all 5 file(s) deployed and ve
- 20261002T143745Z LEG W closed: 14:35:27Z copy-object (metadata COPY), opal-data-bd, runner i-01003b035d2988dfb stopped: gold/meta/client_timeseries_wat
