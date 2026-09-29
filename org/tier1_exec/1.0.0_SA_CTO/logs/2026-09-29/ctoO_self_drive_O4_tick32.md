# /self-drive O4 -- ticks 31-32 (1.0.0_SA_CTO~O, site Z, 2026-09-29 14:13Z)

- **state:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_SELF_DRIVE_O_FABRIC_FOUR_PROJECTS.md` @7612f001c4
- **Cron:** 0eef1ea2

## Measured (14:13Z)

- **Inbox:** 0 unread.
- **Sequence check:** no flags on any of the 4 projects.
- **Open TOs:** 13 of 180.

  | project | open | total |
  |---|---|---|
  | OPLGTW | 5 | 54 |
  | OPALAI | 4 | 35 |
  | MCPORTAL | 2 | 18 |
  | MCPINDEX | 2 | 73 |

- **Completion test:** 0 of 4 complete; 4 REACHABLE.
- **origin/CLOUD:** 15655f4a25.

## Since tick 30

**1. The ETF blocker, re-located.**
- Laptop 1.0.0_SA_CTO msg 102824, relayed by 0.0.0_AB_MSTR~Z at 13:50Z: the patch reached 4.0.0_SA_CRO at 08:27Z.
- The CRO's apply condition is that 41ba3f747f (the ETFS_CANON re-entry) is an ancestor of laptop CLOUD. At 13:4xZ the
  laptop could not resolve that object.
- So MX-t-10 waits on the site Z push reaching laptop CLOUD, not on the CRO.
- Site Z pushes are held on Andrew's word. This seat put the push to Andrew with a REC to release it (14:0xZ).
  MSTR~Z says it is asking him too.

**2. Andrew proposed opalbloomberg@opalinvest.com as the G-C test identity. This seat measured it; it is not admissible.**
- `deploy-to-ec2.sh:197` writes `WRITE_CAPABLE_EMAILS=alyssa@opalinvest.com,opalbloomberg@opalinvest.com`. The live
  gateway still decides the tier by email (row S61; OG-t-2 is not deployed), so GCG1-AC2 FAILS on this identity.
- That address is also a production identity: the Teams concierge, the Analyst's gateway sign-in, and the only admitted
  client of `opal_data_refresh_upload` (`identity_tool_allowlist.txt:19`). A Schwab test grant on it would reach the
  production Analyst once schwab is enabled.
- Answered to Andrew with the REC unchanged: a brand-new unprivileged user.
- Relayed to 2.0.0_SA_COO~O this tick so OG-g-1's blocking row stays accurate.

## Calls

No open calls in scope (ticks 31-32).

## Andrew acts (cited)

- **Release the site Z push:** the hold is his (shared-branch push only on his word).
- **G-C:** create one new unprivileged M365 user (tenant admin plus a licence). Not opalbloomberg@, per item 2 above.
- **G-ACCT:** step 5, the setup-token sign-in, and step 6, one MFA.
- **MCPORTAL G-2ND:** the second sign-in.
- **MCPORTAL G-CLOSE and OPLGTW G-D:** the person-operated runs.
