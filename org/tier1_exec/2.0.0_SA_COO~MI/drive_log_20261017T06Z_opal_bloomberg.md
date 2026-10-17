# Drive log -- 2.0.0_SA_COO~MI, NFRA_MCPINDEX, 2026-10-17 ~02:0xZ to ~06:2xZ (host opal_bloomberg)

Loop: `/canonical-drive NFRA_MCPINDEX 30m`, `/keep-driving` ON. Lease FULL.

## Substantive ticks

- **~02:2xZ, a rollback on the gateway host by another project.** `586e9703f8` (`0.7.0_AE_CloudOps~NFRA1`, OG-ap-32): the round-40 release `b124377b41` deployed 01:53Z and rolled back 02:02Z (host memory 87.1 percent during its read-back); manifest deployed_commit `d3ae88be46`. `anchor_host_check.sh` re-run on the host: 127 of 127, blob `2cbe275d03` holds (`8323c1d419`).
- **~04:0xZ to 05:5xZ, empty ticks by design:** 0 open calls, 0 active task orders, no mail; WAITING DATED on `2.0.0_SA_COO~O`.
- **~06:10Z, the catalog is SERVED.** `2.0.0_SA_COO~O` (msg 35398): release `9d5b712557` deployed 05:19:28Z (ledger `nfra-oplgtw-gateway-release-batch5` CLOSED, `ap34.AC2` PASS, host md5 walk 139 of 139) carries blob `2cbe275d03c9a5af85afefabc604e26b71e9be12` and MX-c-24. Issuer host checks (`round21/post_release/*_after_batch5.txt`): `r13.AC2` PASS (definitions located 127 of 127), anchors 127 of 127, `r13.AC3` monotone PASS (37 equal, 2 behind and tolerated; answer-time 17 of 17), `discover_buckets_host.sh` 8 of 8 echo. Row Z-S136 dispositioned by Z-S138; post-release note `round21/L8_POST_RELEASE_NOTE_20261017.md` to `3.0.0_SA_CVO~Z` (`8ea7b24fed`).
- **~06:30Z, CVO served-catalog grade** `f29e49148b` (ADJUDICATION_v18, row Z-C-S68): the host serves the signed blob with depth_kind latest 33 and series_start 6, equal to the v17 classification; the kind-keyed catalog is REALIZED and MX-c-24's echo served 8 of 8. Carried: MX-s-19 acceptance 10-20, r7 ledger to 10-21; `/opt/opal-gateway/.deployed_commit` is absent on the host, so release identity there is read by blob and md5 walk. Awaiting the CTO's L10 answer.

## Lessons for the record

- When the host's `.deployed_commit` marker is absent (the CVO measured it, and my anchor check printed `commit=` empty throughout), identify a release by blob, md5 walk and ledger; a check that compares the marker reads an empty string.

## Standing clock

`NFRA_MCPINDEX.TO-MX-s-19` acceptance 2026-10-20 ~03:10Z (`round7/checks/s19.AC2.sh`; dates 10-19 and 10-20); from 2026-10-19 check `0.7.0_AE_CloudOps~NFRA1` is LIVE, message `0.0.0_AB_MSTR~Z` by 2026-10-20T02:30Z if not; ledger `nfra-mcpindex-r7-bd-doc-retire` open to 2026-10-21T06:02Z.

Push state: LOCAL (box-sync carries it).
