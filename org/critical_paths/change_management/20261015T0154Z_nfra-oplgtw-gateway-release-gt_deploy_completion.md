# Deploy Completion Record
**Date opened:** 2026-10-15T01:54:35.879081+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-ap-18: the ten G1 typed harvest tools + lib/ as a new artifact member (v3, all three halves signed at 047f11aa99; Z-S133 ruled route (a), so the /yearinreview page ships in its LF form)
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | the deploy source is the signed release: C:/tmp/og-rel-gt3 HEAD = 047f11aa991e5c7ed188876f07a8599447cf2849 and its parent = live deployed_commit bf7ffb62f4 | both hashes read at the act, plus the artifact's own git-ref metadata as a second instrument |  | OPEN |
| L2 | activation | safe-ec2-deploy lands the 17-file release and the service comes back | the deploy output plus GET /health on 127.0.0.1:8080 |  | OPEN |
| L3 | ec2-baked-asset | the RUNNING path carries the release bytes AND /opt/opal-gateway/lib/trading_calendar.py appears for the first time | SSM md5 over app/, deploy/, dashboard/ equal to the release, plus the host md5 of lib/trading_calendar.py equal to the DEPLOY TREE's copy 3de6a337 (A6(2)), not trunk's 6596e52f |  | OPEN |
| L4 | verify | all ten typed tools serve for an Opal principal and refuse a non-Opal one with zero S3 calls, the registry moves 46 -> 56, and a numeric trading_days_behind_t1 closes Z-S125 | W/GT_SERVED.json with per-tool opal_served / non_opal_refused / s3_calls_on_refusal, registry_before and registry_count, and the harvest_search_articles read through mcp.opalinvest.dev inside the ALB's 60 s |  | OPEN |
| L5 | verify | the /yearinreview page moves to its LF form by the issuer's A8 ruling (route (a)), identical content, and nothing else about that page changes | the host's page md5 recorded as yearinreview_md5 in W/GT_SERVED.json, equal to 3bbd5ab2d325657020357003c3ea387d, with the data date still present and the gate arms unchanged |  | OPEN |

## Log

- 20261015T015435Z OPENED by 0.7.0_AE_CloudOps~Z with 5 leg(s)
