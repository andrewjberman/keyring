# Deploy Completion Record
**Date opened:** 2026-10-14T15:37:30.875419+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T154919Z
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-pc-5: the People view gateway release (opal-gateway 7c558b4e21 -> rel-nfra-mcportal-pc, mcportal 17dcbb2)
**Authored by:** 0.7.0_AE_CloudOps~MQ
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | dashboard bundle build from mcportal 17dcbb28624eab147318052f58bcc39b8eb8029c | dist/index.html and dist/routes.json present, bun cache 77 of 77 | mcportal 17dcbb28624eab147318052f58bcc39b8eb8029c built by deploy-to-ec2.sh (bun cache 77 of 77, 'built in 1.32s', dist/index.html + routes.json present); served routes.json lists /people = 1 on the host | CLOSED 20261014T154918Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts ec2/opal-gateway/ release tarball + latest | git-ref metadata equals the release commit on both keys | s3 opal-313476888478-lambda-artifacts ec2/opal-gateway/opal-gateway-bacec95ccd.tar.gz + -latest uploaded, git-ref bacec95ccd6cafd2201f7433af24ae2748732355; stale-base guard read live ref 7c558b4e21 equal at both reads; rollback key opal-gateway-7c558b4e21.tar.gz untouched | CLOSED 20261014T154918Z |
| L3 | activation | SSM pull and restart of opal-gateway on i-07dccb1615503ac99 | /health 200 within 90 s, new MainPID, host md5 of the PC modules equals the release tree | ssm:4fb2876e-b2e8-472e-9a28-7a2ec8da360e Success 15:43:02-15:43:22Z; /health 200; MainPID 1107125 -> 1110422 since 15:43:20Z; host md5 admin_fabric_gitstate=280c109d856b37e378effe84c5064dfe admin_api=db6cf9c76859b2df55349a15788829a3 admin_people=8c8737de03d502681df690a466417e4e == release tree (base gitstate a5ac99dc is the negative control); tools 70 -> 70, 0 added 0 removed, namesmd5 7b042d201996dd8dc7cc3892b245dbea both sides | CLOSED 20261014T154918Z |
| L4 | git | EC2_MANIFEST.json services.opal-gateway record | deployed_commit, previous_deployed_commit, mcportal_commit, release_note committed on the release branch | EC2_MANIFEST services.opal-gateway deployed_commit bacec95ccd (wrapper c4a09eda42), previous_deployed_commit and release_note corrected in 7a4ea1d997 | CLOSED 20261014T154919Z |
| L1 | activation | dashboard bundle build from mcportal 17dcbb28624eab147318052f58bcc39b8eb8029c | dist/index.html and dist/routes.json present, bun cache 77 of 77 |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts ec2/opal-gateway/ release tarball + latest | git-ref metadata equals the release commit on both keys |  | OPEN |
| L3 | activation | SSM pull and restart of opal-gateway on i-07dccb1615503ac99 | /health 200 within 90 s, new MainPID, host md5 of the PC modules equals the release tree |  | OPEN |
| L4 | git | EC2_MANIFEST.json services.opal-gateway record | deployed_commit, previous_deployed_commit, mcportal_commit, release_note committed on the release branch |  | OPEN |

## Log

- 20261014T153730Z OPENED by 0.7.0_AE_CloudOps~MQ with 4 leg(s)
- 20261014T154918Z LEG L1 closed: mcportal 17dcbb28624eab147318052f58bcc39b8eb8029c built by deploy-to-ec2.sh (bun cache 77 of 77, 'built in 1.32s', dist/
- 20261014T154918Z LEG L2 closed: s3 opal-313476888478-lambda-artifacts ec2/opal-gateway/opal-gateway-bacec95ccd.tar.gz + -latest uploaded, git-ref bacec9
- 20261014T154918Z LEG L3 closed: ssm:4fb2876e-b2e8-472e-9a28-7a2ec8da360e Success 15:43:02-15:43:22Z; /health 200; MainPID 1107125 -> 1110422 since 15:43
- 20261014T154919Z LEG L4 closed: EC2_MANIFEST services.opal-gateway deployed_commit bacec95ccd (wrapper c4a09eda42), previous_deployed_commit and release
- 20261014T154919Z CLOSED -- all 4 legs proven
- PRE-ACT RECORD (census, tests, rollback and its proof, the pair, the live world before): org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/MP-pc-5_PRE_ACT_RECORD.md
