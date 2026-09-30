# /self-drive NFRA four -- ticks 42-44: Plan A closed, R20 authority written, laptop merge refused (1.0.0_SA_CTO~O, site Z, 2026-09-30 15:2xZ-16:5xZ)

- **state:** ARMED
- **Arming record:** `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_182xZ_SELF_DRIVE_O_NFRA_FOUR_PROJECTS_POSTCRASH.md` @680afc11fd
- **Cron:** 625c63e4
- **Previous log:** tick 41 @90b8760.

## Since tick 41

1. **Plan A is complete.**
   - Host: 2.0.0_SA_COO~RV restored 4ce7946426 at 15:23:02Z (msg 27229). Host equals the ref 80 of 80,
     `/rivalfunds` answers 401 with the route present, schwab is off, and `FIRM_ROLE_ARNS` is kept.
   - IAM: 2.0.0_SA_COO~MI rolled back at 15:5xZ (msg 27244). `dim_transaction` reads explicitDeny on both masters,
     and the targeted re-plan reads "No changes".
   - Ledgers CLOSED: `nfra-mcpindex-r5-rollback-4ce7946` @4b14925ac4 and `nfra-mcpindex-r5-schwab-enable` ROLLED-BACK
     @0c79bc5c0b. Row Z-S68 is ARMED @1d03eb4130; its disarm is v3 plus the guard.
   - The served outage of `/rivalfunds` ran from 14:41:23Z to 15:23:02Z, about 42 minutes.
2. **Amendment to the v3 base guard (to COO~MI):** compare the live base by REF, meaning the artifact commit or
   manifest. The ETag is secondary: a re-deploy of the same ref gave a new ETag (4a302c0e became da7b3c9d).
   - MX-r-6 A6 v3 re-cut is in progress @4f7032da3b.
3. **R20 authority** `R20_AUTHORITY_MX-t-10_MX-t-13_20260930.md` @15ae6304a7 authorizes entries NFRA-MCPINDEX-R20-01..08.
   - COO~MI computed them @b9d1b053bc against the frozen bytes.
   - They are READ-ONLY, with a cutoff of 2026-10-07, and remediations ETFS_CANON (X11) and ADVI_FIRMBKTS (X12).
   - The entries land after the site-Z merge.
4. **The laptop merge was REFUSED** (msg 27271). The merged-index row gate rejected laptop row IRPT_BCKEND-S219
   (809398f85d, a worker `surfaced_by` with no W id). NOTHING was merged, and a merge has no override path.
   - The fix is routed to laptop COO~P and the gate owner. MSTR~Z retries once the fix is on origin.
5. **Intake received:** laptop mail-tool branches for OPLGTW order 4 (msg 27232):
   - `gw-mail-tools-int` @6a7b9e78fa;
   - `gw-f1-read-email-fields` @5ec089b9a1;
   - `gw-f2-email-filtered` @15ef03f0bc;
   - `gw-f3-inspect-attachment` @6c61ac531b.
   They go into the OPLGTW addendum as adopt-or-supersede inputs.

## Measured (16:49Z)

- **Inbox:** 0 unread.
- **Completion:** 0 of 4. 1 REACHABLE (MCPINDEX), 3 UNREACHABLE.
- **Held on the merge:**
  - MX-t-10, MX-t-13 and MX-r-7 (the R20 entries);
  - the NFRA_OPLGTW addendum for NFRA_TRNSPT;
  - the 2.0.0_SA_COO~O seat.

## Calls

No open calls in the four projects (ticks 42-44).

## Acts only Andrew can do (each cited)

- **Unchanged:**
  - G-ACCT step 5 and step 6 MFA (his login and MFA);
  - MCPORTAL G-2ND and G-CLOSE;
  - OPLGTW G-D and Part D;
  - NFRA_MCPMSP G-ADVISOR, G-USER, G-IT-INF, G-FIRM and G-KEY.

## Compiler Tools

- `git merge-base --is-ancestor 410818259a HEAD` (the merge state).
- Last-tag `<status>` census.
