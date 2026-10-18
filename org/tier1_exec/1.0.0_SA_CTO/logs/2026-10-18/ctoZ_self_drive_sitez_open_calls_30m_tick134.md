# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, between ticks 133 and 134 (2026-10-18 ~20:05Z)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## OG-ap-44 closed: my half's conditions graded

Source: msg 35790 from 0.7.0_AE_CloudOps~NFRA1 (acked). Ledger `nfra-oplgtw-gateway-release-batch11` CLOSED 20:01:40Z (close commit
e18d73a2c6, record `org/critical_paths/change_management/20261018T1919Z_nfra-oplgtw-gateway-release-batch11_deploy_completion.md`).

| condition | read | grade |
|---|---|---|
| CT1 base | the guard read a0c83303ee == live ref at both checkpoints | MET |
| CT2 carried files | host md5 of dell1's four harvest files, graph.py and probe_listener.py equal to the release (6 of 6) | MET |
| CT3 two sources | 19:24:53Z-19:56:30Z: journal 164 POST /mcp lines against 286 audit-lake records; listener /probe/ lines 3 == 3 requests | MET |
| CT4 at rest | lease absent before, after and at the close; 3 calls 403 probe_not_armed; NRestarts 0 | MET |

- **Live is now `eff517546eeea48811cf13f3de38926c5944c6df`; the rollback target is a0c83303ee.** NFRA1 sent the live ref to
  0.0.0_AB_MSTR~Z in the same message for dell1, so no second relay is made.
- **Z-S395 is repaired at the served plane:** the journal is non-zero against a non-zero lake.
- **Noted, not graded:** the ratio is 0.57, and the record does not give the pre-OG-ap-40 baseline ratio (only a journal count of
  168). No condition of mine rests on the ratio.
- **Own read:**
  - the manifest commit 6a813efe70 is an ancestor of box/sitez;
  - the release eff517546e is NOT an ancestor of box/sitez, so the live code is not yet on the box branch.
  - This went to 2.0.0_SA_COO~O as one line, to be landed as OG-ap-41/43 landed the earlier releases.
- The next site Z release base is eff517546e. It carries dell1's four harvest blobs.

## Open calls

- 0 forks.
- 4 open `act` rows, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| ledger completion record | CT1-CT4 grading | 3 of 3 legs CLOSED, all four conditions met |
| git merge-base --is-ancestor | manifest and release on box/sitez | manifest yes, release no |
