# Deploy Completion Record
**Date opened:** 2026-10-20T06:18:15.039445+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T070552Z
**Deploy:** NFRA_OPLGTW OG-rz-2 Phase B: resize the gateway host i-07dccb1615503ac99 from t4g.small to t4g.large (in place, targeted safe-apply, main.tf blob 1cf3c199cb2c, an Elastic IP is attached), THEN one batched release 13917ef993207bee6b8df0124eec5444da4d62cd (OG-rz-1 memory limits 5600M/6400M, OG-ms-1 Schwab master 08403355), cut on 6d1b5dcb64b945deb98664c6ae078d8f1e8a6c5c; window 2026-10-20 06:00Z-06:45Z, abort /health 200 by 06:30Z; callers in the window (audit lake, three previous days): two sign-in identities, one Teams poller on four tools at a steady 1 to 11 s cadence and one occasional research and whoami caller, no gateway- or MCP-named schedule fires; SAFE rollback order: tarball opal-gateway-6d1b5dcb64b.tar.gz 922315 bytes sha256 e7cd9de1617a FIRST, THEN t4g.small (and revoke the OG-ms-2 grant first if it landed)
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| instance | ec2-baked-asset | aws_instance.gw instance_type t4g.small -> t4g.large applied through safe-apply targeted at aws_instance.gw from branch rz2-instance-type-nfra1 (plan 0 to add, 1 to change, 0 to destroy, in place); the instance reads running, the target group healthy, /health 200, the marker unchanged, memory total at least 7000 MB, the Elastic IP still associated; the downtime in seconds recorded | proof: W/rz2_pb/apply.json and W/rz2_pb/resize_wait.json and the downtime interval in W/RZ2_SERVED.json | proof: safe-apply of a saved targeted plan from branch rz2-instance-type-nfra1 (main.tf blob 1cf3c199cb2c): Apply complete, 0 added 1 changed 0 destroyed (W/rz2_pb/apply.json); stop 06:22:54Z, t4g.large running 06:23:25Z, SSM online 06:23:35Z, /health 200 and the marker unchanged and host memory 7813 MB and the target group healthy and the Elastic IP associated at 06:24:29Z (W/rz2_pb/resize_wait.json); public-endpoint downtime 44 s (W/RZ2_SERVED.json) | CLOSED 20261020T070551Z |
| release | ec2-baked-asset | the release 13917ef993 deployed from C:/tmp/og-rel-batch15 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=6d1b5dcb64b945deb98664c6ae078d8f1e8a6c5c under the stale-base guard, no HALT_OVERRIDE, ONLY AFTER the instance leg held | proof: DEPLOYMENT COMPLETE, the marker equal to the release sha, an SSM md5 walk of the host equal to the release blobs, 65 env keys, unit limits 5600M and 6400M, tools/list 103 | proof: DEPLOYMENT COMPLETE at about 06:29Z from C:/tmp/og-rel-batch15 (release 13917ef993) through safe-ec2-deploy.sh with DEPLOY_BASE_REF=6d1b5dcb64, stale-base guard equal, no HALT_OVERRIDE, only after the instance leg held; marker equals the release sha, host md5 walk 143 of 143 equal to the release blobs, 65 env keys, unit limits 5600M and 6400M (live systemctl), tools/list 103 (W/rz2_pb/host_md5_after.json, step1_after.json, limits.txt) | CLOSED 20261020T070551Z |
| read-back | verify | the 30-minute UNARMED-only read-back: health 200, 27 of 27 under the hard guard, NRestarts 0 after the deploy's restart, host memory total at least 7000 MB, the dual count and audit_failure_counter 0, the host clock and systemctl --failed read BEFORE the close, and the two large replies (mdpf_get_aggregate_aua, opal_discover) ONE at a time each completing with the peak below MemoryHigh | proof: W/RZ2_SERVED.json, rz2.AC2 | proof: W/RZ2_SERVED.json (commit 75aa992c57): 31 probes 06:30Z-07:00Z health 200 each, one PID, NRestarts 0; 27 of 27 under the hard guard; UNARMED ONLY (403 probe_not_armed x3, lease absent before, after and at the close, no SSM write); dual count 418 journal lines (192 sampler probes of this seat) against 311 lake records, listener lines 3 equal 3 requests; audit WARN 0 counter 0; host clock Normal and 0 failed units read 07:01Z before the close; the two large replies one at a time (743469 and 585084 characters) completed, service memory about 131 to 132 MB against MemoryHigh 5600 | CLOSED 20261020T070552Z |

## Log

- 20261020T061815Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
- 20261020T070551Z LEG instance closed: proof: safe-apply of a saved targeted plan from branch rz2-instance-type-nfra1 (main.tf blob 1cf3c199cb2c): Apply comple
- 20261020T070551Z LEG release closed: proof: DEPLOYMENT COMPLETE at about 06:29Z from C:/tmp/og-rel-batch15 (release 13917ef993) through safe-ec2-deploy.sh wi
- 20261020T070552Z LEG read-back closed: proof: W/RZ2_SERVED.json (commit 75aa992c57): 31 probes 06:30Z-07:00Z health 200 each, one PID, NRestarts 0; 27 of 27 un
- 20261020T070552Z CLOSED -- all 3 legs proven
