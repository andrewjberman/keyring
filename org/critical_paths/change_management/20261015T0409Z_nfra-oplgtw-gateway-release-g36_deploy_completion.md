# Deploy Completion Record
**Date opened:** 2026-10-15T04:09:03.731317+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-19: the eight G3 portal tools, the five G6 news tools, their TWO read grants and the gateway release (all three halves signed at ee23dd004c on ask sha256 cdefc9a139a4)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the deploy source is the signed release: C:/tmp/og-rel-g36 HEAD = ee23dd004c985c46d479908db46d2ad9b4f3b1c8, parent = live deployed_commit 047f11aa99, worktree clean, and no other gateway RELEASE in flight | both hashes read at the act plus the artifact's git-ref metadata as a second instrument; the one other open oplgtw sentinel named and shown to be a runner ledger rather than a release |  | OPEN |
| L2 | activation | the G6 grant applied ALONE through safe-apply: aws_iam_role_policy.gw_news_read on opal-gateway-role, dynamodb Query/GetItem on three tables and one index | safe-apply output plus get-role-policy read back from IAM BEFORE the second policy is touched |  | OPEN |
| L3 | activation | the G3 grant applied ALONE through safe-apply: aws_iam_role_policy.portal_tiered_read on gateway-global-internal-reader-role, s3:GetObject on json-tiered/market-overview/* only | safe-apply output plus get-role-policy read back from IAM, with the pre-existing gateway-global-internal-reader-policy proven untouched |  | OPEN |
| L4 | activation | safe-ec2-deploy lands the 16-file release and the service comes back | the deploy output plus GET /health on 127.0.0.1:8080 |  | OPEN |
| L5 | ec2-baked-asset | the RUNNING path carries the release bytes, including app/typed_scope.py and the three NEWS_* .env key NAMES | SSM md5 over app/, deploy/, dashboard/ and lib/ equal to the release, plus the three NEWS_* key names present where they were absent before |  | OPEN |
| L6 | verify | all thirteen tools serve an Opal principal and refuse a non-Opal one with zero reads, the registry moves 56 -> 69 on ONE named instrument, and a numeric trading_days_behind_t1 appears where a tool states freshness | W/G36_SERVED.json with per-tool opal_served / non_opal_refused / reads_on_refusal, the registry delta on one instrument, and the CVO's condition: the thirteen read through mcp.opalinvest.dev against the 60 s ALB, a failing tool pulled alone |  | OPEN |

## Log

- 20261015T040903Z OPENED by 0.7.0_AE_CloudOps~Z with 6 leg(s)
