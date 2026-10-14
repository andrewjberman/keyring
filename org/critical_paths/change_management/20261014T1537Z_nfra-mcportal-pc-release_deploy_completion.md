# Deploy Completion Record
**Date opened:** 2026-10-14T15:37:30.875419+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-pc-5: the People view gateway release (opal-gateway 7c558b4e21 -> rel-nfra-mcportal-pc, mcportal 17dcbb2)
**Authored by:** 0.7.0_AE_CloudOps~MQ
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | dashboard bundle build from mcportal 17dcbb28624eab147318052f58bcc39b8eb8029c | dist/index.html and dist/routes.json present, bun cache 77 of 77 |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts ec2/opal-gateway/ release tarball + latest | git-ref metadata equals the release commit on both keys |  | OPEN |
| L3 | activation | SSM pull and restart of opal-gateway on i-07dccb1615503ac99 | /health 200 within 90 s, new MainPID, host md5 of the PC modules equals the release tree |  | OPEN |
| L4 | git | EC2_MANIFEST.json services.opal-gateway record | deployed_commit, previous_deployed_commit, mcportal_commit, release_note committed on the release branch |  | OPEN |

## Log

- 20261014T153730Z OPENED by 0.7.0_AE_CloudOps~MQ with 4 leg(s)
- PRE-ACT RECORD (census, tests, rollback and its proof, the pair, the live world before): org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/MP-pc-5_PRE_ACT_RECORD.md
