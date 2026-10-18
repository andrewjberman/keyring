# Deploy Completion Record
**Date opened:** 2026-10-18T19:19:28.873905+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261018T200140Z
**Deploy:** NFRA_OPLGTW OG-ap-44 Phase B: the round-43 tenth batched gateway release eff517546eeea48811cf13f3de38926c5944c6df (the access-log repair OG-pr-5, UNARMED ONLY, no SSM write), cut on a0c83303ee48c95c16a61c0d5e8bd186b1083b66; rollback tarball opal-gateway-a0c83303ee.tar.gz 914681 bytes sha256 77236429527690cd47483769f45493bf1a141ca4f1074a6ed981c3e81226e1a9
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| deploy | ec2-baked-asset | the release deployed from C:/tmp/og-rel-batch11 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=a0c83303ee48c95c16a61c0d5e8bd186b1083b66 under the stale-base guard, no HALT_OVERRIDE | proof: DEPLOYMENT COMPLETE, the guard equal at both checkpoints, an SSM md5 walk of the host equal to the release blobs, 65 env keys, health 200, the marker equal to the release sha, the four harvest files and graph.py equal to the release's | DEPLOYMENT COMPLETE 2026-10-18T19:24:03Z rc=0, base guard a0c83303ee == live ref at both checkpoints, no HALT_OVERRIDE; SSM md5 walk 141 of 141 equal to release blobs eff517546e; 65 env keys; health 200; marker == eff517546eeea48811cf13f3de38926c5944c6df; host md5 of dell1's four harvest files, graph.py and probe_listener.py equal to the release's (6 of 6) | CLOSED 20261018T200139Z |
| served-read | verify | the served read UNARMED ONLY (lease parameter absent before and after, three listener calls answering 403 probe_not_armed, armings 0), the 27-tool read under the hard guard, the host clock and systemctl --failed read BEFORE the close, and the 30-minute read-back with the journal POST /mcp count AND the audit-lake count for the same window | proof: W/CODE11_SERVED.json, NRestarts 0, the lease parameter absent, the journal non-zero against the non-zero lake | W/CODE11_SERVED.json: 27 of 27 under rlimit guard; UNARMED ONLY: lease parameter absent before, after and at the close (19:57:55Z), no SSM write, three calls answered 403 probe_not_armed, listener on 127.0.0.1 and the service PID, PID unchanged NRestarts 0; ACCESS LOG BACK over the same 19:24:53Z-19:56:30Z window: journal 164 POST /mcp lines vs 286 audit-lake records (ratio 0.57; baseline window before OG-ap-40 168), listener /probe/ lines 3 == 3 requests made; read-back 32 probes 0 triggers NRestarts 0; clock Leap Normal synchronised and systemctl --failed 0 read before the close | CLOSED 20261018T200139Z |
| standing-clauses | git | runbook 7.2 names the new live release; EC2_MANIFEST deployed_commit and file_checksums come from the release blobs; the CLOSED time and the final live sha go to 1.0.0_SA_CTO~Z and 0.0.0_AB_MSTR~Z in one message | proof: the commit hash carrying both, checksums cross-checked against the host md5 | commit 6a813efe70 (merged to box/sitez): manifest deployed_commit eff517546e previous a0c83303ee, file_checksums 10 of 10 cross-checked against host md5 (none moves); runbook 7.2 names the live release and rollback target a0c83303ee | CLOSED 20261018T200139Z |

## Log

- 20261018T191928Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261018T200139Z LEG deploy closed: DEPLOYMENT COMPLETE 2026-10-18T19:24:03Z rc=0, base guard a0c83303ee == live ref at both checkpoints, no HALT_OVERRIDE; 
- 20261018T200139Z LEG served-read closed: W/CODE11_SERVED.json: 27 of 27 under rlimit guard; UNARMED ONLY: lease parameter absent before, after and at the close (
- 20261018T200139Z LEG standing-clauses closed: commit 6a813efe70 (merged to box/sitez): manifest deployed_commit eff517546e previous a0c83303ee, file_checksums 10 of 1
- 20261018T200140Z CLOSED -- all 3 legs proven
