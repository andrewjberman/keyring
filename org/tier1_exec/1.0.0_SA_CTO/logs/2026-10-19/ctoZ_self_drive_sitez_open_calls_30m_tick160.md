# 1.0.0_SA_CTO~Z -- /self-drive 30m sitez open calls, ticks 159-160 (2026-10-19 06:58Z to 08:0xZ)

**archetype:** COORDINATE

Arming record: `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261016_024xZ_SELF_DRIVE_30M_SITEZ_BOX_OPEN_CALLS.md` @b155c4c03a.
Session cron e6b088c9. **state: ARMED**

## OG-ap-48 closed: my half's conditions graded

- **Source:** 2.0.0_SA_COO~O, msg 35914 (acked). Ledger `nfra-oplgtw-gateway-release-batch13` CLOSED 07:44:53Z.
  - Record: `org/critical_paths/change_management/20261019T0658Z_nfra-oplgtw-gateway-release-batch13_deploy_completion.md`.
  - Plus `CODE13_SERVED.json` @444568e38f.

| condition | read | grade |
|---|---|---|
| CT1 base | "base guard e09c30c3f0 == live ref at both checkpoints, no HALT_OVERRIDE" | MET |
| CT2 carried files | md5 walk 143 of 143 equal to release blobs 6b1a9bd292 | MET |
| CT3 three counts | window 07:07Z-07:37Z: journal 149 `POST /mcp`, lake 270 (0.552), `audit-lake WARN` lines 0, counter 0 | MET |
| CT4 nothing else moves | tools/list 103 = 103; 27 of 27; NRestarts 0; unarmed | MET |

- **Live is now `6b1a9bd292855841826e194d0bddf9ac79bc8337`.** The lake leg is bounded and audible; its first read shows 0 failures.
- **One check I made myself, because the counts repeated.**
  - CODE13 and CODE12 report the identical 149 and 270, for windows three hours apart (04:16Z-04:46Z and 07:07Z-07:37Z).
  - The journal totals differ (1,113 and 1,105), so the read was redone.
  - **I counted the lake myself:** `s3api list-objects-v2` on `audit/dt=2026-10-19/` gives 5,991 objects, with exactly **270 in
    each window**. Hourly counts are about 410 (00h 414, 01h 412, 03h 407, 05h 408, 06h 426).
  - The traffic is that periodic, so the repeat is real, not a copied value.
- **Noted, not graded:** hour 02 holds 2,896 lake objects, about 7 times baseline. It overlaps OG-ev-11's body reads and the
  re-spawns. Its cause is unread; it is a candidate for OG-ev-12's journal read.

## Box state

- Commit free 33,709 MB at 07:27Z; 8 claude.exe alive.
- **Bloomberg sign-in:** the 09:00Z cutoff stands (ruled 04:10Z).

## Open calls

- 0 forks.
- 4 open `act` rows, which only Andrew can do: f0d2, 8ed7, def4 (postponed by Andrew) and 5b35.
- Plus the Bloomberg Terminal sign-in, which has the 09:00Z cutoff.

## Compiler Tools

| tool | used for | result |
|---|---|---|
| grep (batch13 completion record) | CT1-CT3 | base guard, md5 143/143, counts |
| python json walk (CODE12 vs CODE13) | repeated counts | windows differ, totals differ |
| aws s3api list-objects-v2 (opal-mcp-audit, one day prefix) | independent lake count | 270 and 270; 5,991 objects in the day |
