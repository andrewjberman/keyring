# Deploy Completion Record
**Date opened:** 2026-07-22T01:00:43.475889+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260722T040519Z
**Deploy:** MDPF_REVAMP.S5 exact-9 cutover (opal-assets targeted apply -> populate -> pre-flight -> portal-auth flip on CTO FINAL GO)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | exact-9 diffs on CLOUD | committed @803f8b1e7 pushed | exact-9 diffs committed @803f8b1e7, pushed to origin/CLOUD (67dfaaa0a..efdb4dbd8) | CLOSED 20260722T010429Z |
| L2 | activation | opal-assets --target apply (bucket-policy + mdpf_publisher_scoped) | apply complete, plan-scoped to exactly 2 | safe-apply targeted planfile RC0: Apply complete 0 added/2 changed/0 destroyed (aws_iam_role_policy.mdpf_publisher_scoped + aws_s3_bucket_policy.monolith); targeted re-plan 0-diff 'No changes'; bd49f_reporting_io EXCLUDED (grep count 0 in the targeted plan). Scope-isolate held. | CLOSED 20260722T010345Z |
| L3 | activation | publisher build+upload + module.mdpf_publisher lambda deploy | new PUBLISH_MAP code hash deployed | publisher lambda deploy: safe-apply 0-add/1-change/0-destroy, 0-diff verified; live get-function-configuration CodeSha256=ixhMa8IgokAg2F1CH/xtawKUcttlAZ/lsChRwnWwH1o= (== uploaded artifact), runtime python3.12, lastmod 01:08:06Z | CLOSED 20260722T010919Z |
| L4 | verify | manual publisher invoke populates 9 json/ keys + ListObjectsV2 | 9 keys landed | publisher invoke StatusCode 200, all_present=true, published 9/9, missing[]. INDEPENDENT ListObjectsV2 confirms exactly 9 json/ keys landed @01:10:18-19Z (>apply): mdpf/{global,49f,inflection}/aggregate-aua-timeseries (165630/177330/151243) + mdpf/{49f,inflection}/account-distribution (11451/14914) + portfolios/{account-distribution,non_model_assets,aum-metrics,aum-timeseries} (14953/82101/5079/277985). Byte-identical copies of gold/mdpf_revamp source. | CLOSED 20260722T011303Z |
| L5 | verify | rollback + negative control exercised on isolated throwaway distro | exercised report | Rollback ACCEPTED-as-specified by CTO (skip throwaway behavior-removal, low value): additivity(+9/0-removed/0-changed via -json)->exact inverse; LIVE negative control #8 /api/general/*->S3-opal-data-portal-v2-json (shadow), 24 behaviors, 0 of my 9 present pre-flip; flip-TF-plans-to-no-changes. HARD GATE deferred: post-flip revert-plan MUST show -9/-origin/-OAC/0 else before disarm. | CLOSED 20260722T015146Z |
| L6 | verify | live get-bucket-policy (a) + C-pre-flight both shapes (b) | brought to CTO | (a) live get-bucket-policy applied-truth: AllowMdpfPortalCloudFrontOACRead, 9 exact keys, SourceArn=EVTSA9VEHNZVH + Deny17a. (b) C-pre-flight throwaway PASS: 200 application/json both shapes+3 firms (byte-sizes==published), neg-403 AccessDenied. DE render PASS (all 9 200/json byte-identical, 3 runs). CTO ACCEPTED (a)(b)(c). Teardown: bucket-policy ZERO-RESIDUAL verified (2 stmts, throwaway gone); distro+OAC delete in progress (bg b4bugtqfi). | CLOSED 20260722T015147Z |
| L7 | activation | portal-auth flip (9 behaviors) -- HELD for CTO FINAL GO | flip applied on GO | portal-auth flip APPLIED (retry after transient comp-tagauthz IAM-blip fail-closed, no override): comp-tagauthz PASSED (205 roles swept, 0 candidates, no collision); aws_cloudfront_origin_access_control.assets created E31ME0INK9BJE1; distro EVTSA9VEHNZVH modified; Apply complete 1 added/1 changed/0 destroyed. POST-FLIP revert-plan HARD GATE = CLEAN INVERSE (0-add/1-change/1-destroy: DELETE OAC, origins 8->7 -assets, behaviors 33->24 -exactly-9, 0 existing changed) -> rollback ARMED on real-distro structure. Step-2(i) wiring: 9 live URLs -> 401 application/json (behaviors LIVE+auth-gated+routed, not 404/HTML). | CLOSED 20260722T025601Z |
| L8 | verify | 9 live URLs serve JSON + joint live-URL catch + rollback disarm | delivered | ROLLBACK (P0: buggy Global aggregate-aua opal_aggregate_aua internally inconsistent + half-landed FE; Andrew+CTO+COO GO): serving REVERTED to portal-v2. safe-apply --target aws_cloudfront_distribution.portal (0-add/1-change/0-destroy) after catching+fixing terraform's OAC-destroy-first 409 ordering race -> live 24 behaviors/7 origins/Deployed, S3-opal-data-assets origin + 9 dedicated behaviors GONE, catch-all /api/general/*->S3-opal-data-portal-v2-json, tokenless 9 URLs->401 via #8. OAC E31ME0INK9BJE1 destroyed (NoSuchOriginAccessControl). portal-auth 0-diff (state==pre-flip). Revert committed+pushed @9a5936060. opal-assets bucket-policy+publisher json/ KEPT (benign, staged for FE-first re-land). Completion-by-rollback, NOT stranded. | CLOSED 20260722T040256Z |

## Log

- 20260722T010043Z OPENED by 0.7.0_AE_CloudOps with 8 leg(s)
- 20260722T010345Z LEG L2 closed: safe-apply targeted planfile RC0: Apply complete 0 added/2 changed/0 destroyed (aws_iam_role_policy.mdpf_publisher_scope
- 20260722T010429Z LEG L1 closed: exact-9 diffs committed @803f8b1e7, pushed to origin/CLOUD (67dfaaa0a..efdb4dbd8)
- 20260722T010919Z LEG L3 closed: publisher lambda deploy: safe-apply 0-add/1-change/0-destroy, 0-diff verified; live get-function-configuration CodeSha25
- 20260722T011303Z LEG L4 closed: publisher invoke StatusCode 200, all_present=true, published 9/9, missing[]. INDEPENDENT ListObjectsV2 confirms exactly 
- 20260722T015146Z LEG L5 closed: Rollback ACCEPTED-as-specified by CTO (skip throwaway behavior-removal, low value): additivity(+9/0-removed/0-changed vi
- 20260722T015147Z LEG L6 closed: (a) live get-bucket-policy applied-truth: AllowMdpfPortalCloudFrontOACRead, 9 exact keys, SourceArn=EVTSA9VEHNZVH + Deny
- 20260722T025601Z LEG L7 closed: portal-auth flip APPLIED (retry after transient comp-tagauthz IAM-blip fail-closed, no override): comp-tagauthz PASSED (
- 20260722T040256Z LEG L8 closed: ROLLBACK (P0: buggy Global aggregate-aua opal_aggregate_aua internally inconsistent + half-landed FE; Andrew+CTO+COO GO)
- 20260722T040519Z CLOSED -- all 8 legs proven
