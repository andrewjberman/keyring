# Deploy Completion Record
**Date opened:** 2026-10-16T13:16:24.748122+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T133117Z
**Deploy:** NFRA_MCPORTAL MP-pf-9: the bundle-only gateway release (opal-gateway 38fe44d5cb, mcportal 090b9cdc85 -> c66ca82952)
**Authored by:** 0.7.0_AE_CloudOps~MQ
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | dashboard bundle build from mcportal c66ca82952c01575968d16cc736cdabe36606572 | dist/index.html and dist/routes.json present, bun cache 77 of 77 | ssm:eb89810b-21a5-4e21-acfc-b16a98791ea1 executed 13:23:37-13:23:57Z; mcportal c66ca82952 built by deploy-to-ec2.sh (bun cache 77 of 77, 'built in 964ms', 81 modules); dist has index.html, routes.json and assets/index-BRnJX9Mi.css + index-DbObnWYp.js; host dashboard/index.html names exactly those two (sha256 5a6e2eeef8ec0e9d), routes.json e6d4a9ac3ce7d275 unchanged | CLOSED 20261016T133116Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts ec2/opal-gateway/ release tarball + latest | git-ref metadata equals the release commit on both keys | s3 opal-313476888478-lambda-artifacts ec2/opal-gateway/opal-gateway-d14445961d.tar.gz (13:23:32Z) + -latest (13:23:35Z), 883434 B each, ETag ce83561b919f47b82119a79c63efe052 on both, git-ref d14445961dd6d04275ca8186372a4df4c4fcc5cc on both; stale-base guard read live ref 38fe44d5cb equal at both reads; rollback key opal-gateway-38fe44d5cb.tar.gz untouched (883434 B ETag df5cba50) | CLOSED 20261016T133116Z |
| L3 | activation | SSM pull and restart of opal-gateway on i-07dccb1615503ac99 | /health 200 within 90 s, new MainPID, host dashboard index.html names the two new assets, tool names before equal after | ssm:eb89810b-21a5-4e21-acfc-b16a98791ea1 Success 13:23:37-13:23:57Z; read 13:25:19Z ssm:4dba1956-3a1b-4431-82a2-6bf4a79ed9ad: /health 200; unit active; MainPID 1192771 -> 1195428 since 13:23:55Z; no-identity / 401 /gateway 401; tool names 127 before and 127 after, 0 added 0 removed, namesmd5 4f5cf3218d92006fcddfefcdc9369a15 both sides; rollback bound: pull-and-restart 20 s (SSM leg), whole wrapper 102 s | CLOSED 20261016T133116Z |
| L4 | git | EC2_MANIFEST.json services.opal-gateway record | deployed_commit, previous_deployed_commit, mcportal_commit, release_note committed on the release branch | EC2_MANIFEST services.opal-gateway deployed_commit d14445961d (wrapper), previous_deployed_commit 38fe44d5cb, mcportal_commit c66ca82952, release_note committed bddaf03886 on rel-nfra-mcportal-pf | CLOSED 20261016T133116Z |

## Log

- 20261016T131624Z OPENED by 0.7.0_AE_CloudOps~MQ with 4 leg(s)
- 20261016T133116Z LEG L1 closed: ssm:eb89810b-21a5-4e21-acfc-b16a98791ea1 executed 13:23:37-13:23:57Z; mcportal c66ca82952 built by deploy-to-ec2.sh (bun
- 20261016T133116Z LEG L2 closed: s3 opal-313476888478-lambda-artifacts ec2/opal-gateway/opal-gateway-d14445961d.tar.gz (13:23:32Z) + -latest (13:23:35Z),
- 20261016T133116Z LEG L3 closed: ssm:eb89810b-21a5-4e21-acfc-b16a98791ea1 Success 13:23:37-13:23:57Z; read 13:25:19Z ssm:4dba1956-3a1b-4431-82a2-6bf4a79e
- 20261016T133116Z LEG L4 closed: EC2_MANIFEST services.opal-gateway deployed_commit d14445961d (wrapper), previous_deployed_commit 38fe44d5cb, mcportal_c
- 20261016T133117Z CLOSED -- all 4 legs proven
- PRE-ACT RECORD (census, tests, rollback and its proof, the pair, the live world before): org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/MP-pf-9_PRE_ACT_RECORD.md
