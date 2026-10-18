# Deploy Completion Record
**Date opened:** 2026-10-18T13:34:10.564817+00:00
**Status:** OPEN
**Deploy:** AMGT_HARVST HVST-ck-3: opal-gateway union-read release rel-amgt-harvst-ck3 = live 6575999df5 + exactly six files from 5e026fa7f4 (harvest_research.py, harvest_figures.py, harvest_identity.py, harvest_keys.py, test_cj6, new test_ck2); ONE service restart (about a minute) for every principal; DEPLOY WAITS FOR THE ISSUER'S GO AFTER SITE Z; DEPLOY_BASE_REF=6575999df5; rollback = redeploy previous_deployed_commit (the live release 6575999df5, tarball opal-gateway-6575999df5.tar.gz) through the same script; no data written
**Authored by:** 0.7.0_AE_CloudOps~SC1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| S0 | verify | before-state: live commit on manifest, origin/CLOUD manifest, instance and marker; tool-name count; /health; scheduled-task list with control; test_og_gt8 no-change control; BEFORE gateway reads of the controls and the four slash spellings | ck3_before.out |  | OPEN |
| K1 | git | cut rel-amgt-harvst-ck3 on the live commit: md5 guard of the five modified files, six carried paths, name-status diff (5 M 1 A), carried md5 table, 82 tests, bun cache precheck | ck3_cut.out + ck3_bun_precheck.out |  | OPEN |
| H1 | verify | ck3_hostowner_note.out written (release commit, six paths, window, rollback); the CTO condition-2 surprise row filed; issuer told; WAIT for the GO | note + row id + message |  | OPEN |
| D1 | activation | safe-ec2-deploy.sh opal-gateway from the release branch with DEPLOY_BASE_REF=6575999df5 and AGENT_NAME; health and tool-name count after | ck3_deploy.out + ck3_after.out |  | OPEN |
| V1 | verify | ck3_served.out: controls equal before and after, no stored_spelling on them; both spellings of BP and NG return the same peers object, coverage objects and records; research record whole | ck3_served.out ends with four PASS lines |  | OPEN |
| Z1 | git | proof instance VALID on committed bytes; deliverables, manifest record and ledger close committed; issuer told release branch and commit | checker last line + commit hashes |  | OPEN |

## Log

- 20261018T133410Z OPENED by 0.7.0_AE_CloudOps~SC1 with 6 leg(s)
