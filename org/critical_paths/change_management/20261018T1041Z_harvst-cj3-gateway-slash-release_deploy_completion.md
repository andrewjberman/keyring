# Deploy Completion Record
**Date opened:** 2026-10-18T10:41:20.789049+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-cj-3: ONE opal-gateway release on EC2 i-07dccb1615503ac99: the live commit 3b94a83e05 (site Z ap-40) plus exactly seven files from 34fb405b29 (3 M: app/harvest_research.py, harvest_figures.py, harvest_identity.py; 4 A: app/harvest_keys.py, tests/test_cj2_slash_key_one_form.py, tests/test_cj6_slash_key_other_tools.py, tests/fixtures/cj2_continuation_keys.txt); safe-ec2-deploy.sh with DEPLOY_BASE_REF = the live commit; the service restarts about a minute for every principal on every box; window 11:05Z-12:00Z (site Z CLEAR now, deploy before 12:00Z, msgs 7999 and 8000); rollback = redeploy previous_deployed_commit (3b94a83e05 -> read at step 0) through the same script; no S3 object, tools.py, server.py, Terraform, IAM or schedule moves
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | live commit read three ways (EC2_MANIFEST.json, instance, /opt/opal-gateway/.deployed_commit) all 3b94a83e05; tool-name count; /health; previous tarball key; scheduled-task read with control; test_og_gt8 once; BEFORE gateway reads (C-7 controls and the four slash spellings) | cj3_before.out |  | OPEN |
| K1 | verify | release branch rel-amgt-harvst-cj3 cut from the live commit; md5 guard of the three modified files at live; seven carried files by git checkout 34fb405b29; md5 table; git diff --name-status live..release = exactly 7 (3 M, 4 A); 75 tests | cj3_cut.out |  | OPEN |
| H1 | verify | bun cache precheck complete; cj3_hostowner_note.out written (release commit, seven paths, window, rollback) and the issuer told | cj3_bun_precheck.out + cj3_hostowner_note.out |  | OPEN |
| D1 | activation | safe-ec2-deploy.sh opal-gateway from the release branch, AGENT_NAME and DEPLOY_BASE_REF set; health and tool-name count equal; manifest records the new deployed_commit | cj3_deploy.out + cj3_after.out |  | OPEN |
| V1 | verify | the step 0 reads again: controls EQUAL; four slash spellings return dossier_key, continuation_key, ai_fill_key, research_reports and the exec-officer roster; BP consensus equal across spellings; cj3_served.out four result lines | cj3_served.out |  | OPEN |
| Z1 | git | proof instance VALID, release ref and ledger close committed, report to the issuer | checker last line + commit hash |  | OPEN |

## Log

- 20261018T104120Z OPENED by 0.7.0_AE_CloudOps~SC1 with 6 leg(s)
