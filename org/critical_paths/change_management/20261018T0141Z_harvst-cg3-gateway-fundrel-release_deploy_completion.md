# Deploy Completion Record
**Date opened:** 2026-10-18T01:41:41.685930+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cg-3: ONE opal-gateway release (service opal-gateway, EC2 i-07dccb1615503ac99, restart about one minute; window to be stated after site Z answers, expected 2026-10-18 01:50Z-03:30Z) carrying exactly 3 paths from b77e08e198 and 290f2e9e6d onto the live commit d077cef043: app/harvest_research.py (ce-3 wording hunk + REPORT_FIELDS gains fund_relation), tests/test_ce3_parts_absent_wording.py, tests/test_cg4_report_fund_relation.py; rollback = redeploy previous_deployed_commit (the live commit's tarball) through safe-ec2-deploy.sh
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | live commit read on three planes (manifest, artifact, instance); tool-name count and health; BEFORE gateway reads KMB, CPA, UNH and one newest silver part's fund_relation column | cg3_before.out |  | OPEN |
| CUT | verify | release rel-amgt-harvst-cg3 cut on the live commit; <merge>^1 equality + md5; three-path and two-hunk diffs; 9 test files pass | cg3_before.out |  | OPEN |
| NOTE | verify | cg3_hostowner_note.out written and the issuer told; no deploy before GO and site Z answer | cg3_hostowner_note.out |  | OPEN |
| DEPLOY | activation | bun cache precheck complete; safe-ec2-deploy.sh opal-gateway with AGENT_NAME and DEPLOY_BASE_REF=live commit; health after; restart window stated | cg3_deploy.out + cg3_after.out |  | OPEN |
| SERVED | verify | reads after: KMB CPA UNH equal to before apart from fund_relation; proof names ADBE SNPS MNST CLX candidate, ML_FP template, UNH holding; tool count and health equal; cg3_served.out four result lines | cg3_served.out |  | OPEN |
| Z | git | proof instance VALID, manifest and ledger close committed, report to the issuer | checker last line + commit hash |  | OPEN |

## Log

- 20261018T014141Z OPENED by 0.7.0_AE_CloudOps~SC1 with 6 leg(s)
