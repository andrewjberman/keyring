# Deploy Completion Record
**Date opened:** 2026-10-20T06:18:15.039445+00:00
**Status:** OPEN
**Deploy:** NFRA_OPLGTW OG-rz-2 Phase B: resize the gateway host i-07dccb1615503ac99 from t4g.small to t4g.large (in place, targeted safe-apply, main.tf blob 1cf3c199cb2c, an Elastic IP is attached), THEN one batched release 13917ef993207bee6b8df0124eec5444da4d62cd (OG-rz-1 memory limits 5600M/6400M, OG-ms-1 Schwab master 08403355), cut on 6d1b5dcb64b945deb98664c6ae078d8f1e8a6c5c; window 2026-10-20 06:00Z-06:45Z, abort /health 200 by 06:30Z; callers in the window (audit lake, three previous days): two sign-in identities, one Teams poller on four tools at a steady 1 to 11 s cadence and one occasional research and whoami caller, no gateway- or MCP-named schedule fires; SAFE rollback order: tarball opal-gateway-6d1b5dcb64b.tar.gz 922315 bytes sha256 e7cd9de1617a FIRST, THEN t4g.small (and revoke the OG-ms-2 grant first if it landed)
**Authored by:** 0.7.0_AE_CloudOps~NFRA1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| instance | ec2-baked-asset | aws_instance.gw instance_type t4g.small -> t4g.large applied through safe-apply targeted at aws_instance.gw from branch rz2-instance-type-nfra1 (plan 0 to add, 1 to change, 0 to destroy, in place); the instance reads running, the target group healthy, /health 200, the marker unchanged, memory total at least 7000 MB, the Elastic IP still associated; the downtime in seconds recorded | proof: W/rz2_pb/apply.json and W/rz2_pb/resize_wait.json and the downtime interval in W/RZ2_SERVED.json |  | OPEN |
| release | ec2-baked-asset | the release 13917ef993 deployed from C:/tmp/og-rel-batch15 through safe-ec2-deploy.sh with DEPLOY_BASE_REF=6d1b5dcb64b945deb98664c6ae078d8f1e8a6c5c under the stale-base guard, no HALT_OVERRIDE, ONLY AFTER the instance leg held | proof: DEPLOYMENT COMPLETE, the marker equal to the release sha, an SSM md5 walk of the host equal to the release blobs, 65 env keys, unit limits 5600M and 6400M, tools/list 103 |  | OPEN |
| read-back | verify | the 30-minute UNARMED-only read-back: health 200, 27 of 27 under the hard guard, NRestarts 0 after the deploy's restart, host memory total at least 7000 MB, the dual count and audit_failure_counter 0, the host clock and systemctl --failed read BEFORE the close, and the two large replies (mdpf_get_aggregate_aua, opal_discover) ONE at a time each completing with the peak below MemoryHigh | proof: W/RZ2_SERVED.json, rz2.AC2 |  | OPEN |

## Log

- 20261020T061815Z OPENED by 0.7.0_AE_CloudOps~NFRA1 with 3 leg(s)
