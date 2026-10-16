# Deploy Completion Record
**Date opened:** 2026-10-16T13:16:24.748122+00:00
**Status:** OPEN
**Deploy:** NFRA_MCPORTAL MP-pf-9: the bundle-only gateway release (opal-gateway 38fe44d5cb, mcportal 090b9cdc85 -> c66ca82952)
**Authored by:** 0.7.0_AE_CloudOps~MQ
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | dashboard bundle build from mcportal c66ca82952c01575968d16cc736cdabe36606572 | dist/index.html and dist/routes.json present, bun cache 77 of 77 |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts ec2/opal-gateway/ release tarball + latest | git-ref metadata equals the release commit on both keys |  | OPEN |
| L3 | activation | SSM pull and restart of opal-gateway on i-07dccb1615503ac99 | /health 200 within 90 s, new MainPID, host dashboard index.html names the two new assets, tool names before equal after |  | OPEN |
| L4 | git | EC2_MANIFEST.json services.opal-gateway record | deployed_commit, previous_deployed_commit, mcportal_commit, release_note committed on the release branch |  | OPEN |

## Log

- 20261016T131624Z OPENED by 0.7.0_AE_CloudOps~MQ with 4 leg(s)
- PRE-ACT RECORD (census, tests, rollback and its proof, the pair, the live world before): org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/MP-pf-9_PRE_ACT_RECORD.md
