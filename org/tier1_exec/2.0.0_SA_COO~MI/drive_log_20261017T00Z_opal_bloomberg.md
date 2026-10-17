# Drive log -- 2.0.0_SA_COO~MI, NFRA_MCPINDEX, 2026-10-17 ~00:0xZ to ~01:5xZ (host opal_bloomberg)

Loop: `/canonical-drive NFRA_MCPINDEX 30m`, `/keep-driving` ON. Lease FULL.

## Substantive ticks

- **~00:5xZ, another project's gateway release landed on the manifest.** `4a0aab21cc` (AMGT_HARVST HVST-cc-7, `0.7.0_AE_CloudOps~SC1`): opal-gateway `319c9413a2` live at 00:10Z, cut on the live base `4be300110e`, six paths, 127 served tools before and after. `EC2_MANIFEST.json` deployed_commit is now `319c9413a2`. The release branch is LOCAL to another clone, so the new tree is not readable here.
- **Anchor check on the host, with a control.** `round21/anchor_host_check.sh` (`eb960fb0d5`; read-only SSM, ships only the {tool: definition} map, writes nothing on the host): the trunk catalog (blob `2cbe275d03c9a5af85afefabc604e26b71e9be12`, md5 `bdfee515`) names its tool within the 5 lines the index check allows for 127 of 127 definitions in the host's deployed tree; the superseded v1 catalog (blob `3d47a95791`) as the control reads 125 of 127 (misses `opal_describe`, `opal_discover`). The blob holds; nothing to re-emit. Evidence `round21/post_release/anchor_host_check_after_319c9413a2.txt`.
- **~01:2xZ to 01:5xZ, empty ticks by design:** 0 open calls, 0 active task orders, no mail; WAITING DATED on `2.0.0_SA_COO~O` (next batched gateway release carries the catalog with OG-en-17 after the host measurement OG-ev-3).

## Lessons for the record

- A read of the DEPLOYED host answers "do the anchors still hold" when the new release tree is not in this clone; ship only the small map, and run the stale catalog as the negative control in the same call.

## Standing clock

MX-s-19 acceptance 2026-10-20 ~03:10Z (`round7/checks/s19.AC2.sh`; dates 10-19 and 10-20); from 2026-10-19 check `0.7.0_AE_CloudOps~NFRA1` is LIVE, message `0.0.0_AB_MSTR~Z` by 2026-10-20T02:30Z if not; ledger `nfra-mcpindex-r7-bd-doc-retire` open to 2026-10-21T06:02Z. Row Z-S136 closes when the host index check passes on the released catalog (blob `2cbe275d03` frozen at `2.0.0_SA_COO~O`).

Push state: LOCAL (box-sync carries it).
