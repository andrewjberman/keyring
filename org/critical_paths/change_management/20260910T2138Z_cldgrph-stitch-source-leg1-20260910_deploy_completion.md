# Deploy Completion Record
**Date opened:** 2026-09-10T21:38:43.418768+00:00
**Status:** OPEN
**Deploy:** NFRA_CLDGRPH Act B via ROUTE B-1 (the committed route, per the handoff's own recommendation): provision the PORTAL_REPO_PAT repo secret the stitch-source-push workflow has always needed, then workflow_dispatch it on CLOUD so the stitch source zip is published by the mechanism the estate intends, WITH portal files AND the portal_sha vintage record. Andrew-direct 2026-09-10 ~20:2xZ 'Rec (a) for call 1' authorizes the deploy; Andrew-direct 2026-09-10 ~21:3xZ answers the two open calls -- use the existing estate-report/github-token, and LEAVE the push: trigger as committed. Handoff: org/tier1_exec/2.0.0_SA_COO~A/deliverables/HANDOFF_CLDGRPH_DEPLOY_20260910T2040Z.md s.5
**Authored by:** 0.8.0_AE_CloudComp
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | Set repo secret PORTAL_REPO_PAT on Opal-Capital/ajb_workspace from Secrets Manager estate-report/github-token (verified: reads Opal-Capital/portal AND the pinned gitlink 5907cbca98) | gh secret list showing PORTAL_REPO_PAT, plus a run that gets PAST the Checkout portal step that has killed 833 runs |  | OPEN |
| L2 | activation | workflow_dispatch stitch-source-push.yml on CLOUD -- the first correct publish by the committed route in 856 runs | gh run view --json conclusion == success, read from the API not from the dispatch return |  | OPEN |
| L3 | verify | The SERVED s3://opal-313476888478-globgrph/stitch-source/source.zip carries portal/src AND portal_sha.txt -- the portal vintage record the hand route has never written | ranged central-directory read of the served object, before/after |  | OPEN |

## Log

- 20260910T213843Z OPENED by 0.8.0_AE_CloudComp with 3 leg(s)
