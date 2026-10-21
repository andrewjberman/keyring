# ANDREW-DIRECT 2026-10-21 ~14:5xZ: Alongside Schwab Box signed in; four master keys visible

Given at the laptop 1.0.0_SA_CTO terminal, after the RDP sitting on `i-0825aa0ed88342d67`, VERBATIM:

> "I have gone through all the steps virtually, the only one that remains was the SDD Scheduler Service is not allowing itself to be
> installed, but we have not done this for other EC2 auto downloader systems, so ill leave it off here for you to continue. There are 4
> master keys included, the cottonwood firm as a whole, stephen shipley, christa bass, and jay rubottom.."

## What it settles

- **Andrew's sitting is done.** Runbook steps (b) to (f) were done by RDP. NLA was off for the sitting (SSM `144a3975`), and its restore is
  TO-AL-r5.
- **The SDD Scheduler Service is NOT installed, by Andrew's word.** The 49F box does not use it either. Pulls run through the Administrator
  scheduled tasks that the SSM hand-off starts, so nothing new is needed.
- **The Alongside login shows four masters**, named by Andrew: the Cottonwood firm as a whole, Stephen Shipley, Christa Bass and Jay
  Rubottom.
  - The mapping of names to master numbers (08719286, 08134043, 08165601, 08480305) is not yet measured.
  - The entitlement read (`sdd-entitlements.ps1`, runbook step h) prints the login's `DailyMasterAccounts` list, and that read is the
    instrument. A name is never mapped to a number by inference.

## Next (owner `2.0.0_SA_COO~SA`)

1. Run the entitlement read and report LISTED and ENTITLED or NOT-ENTITLED per master.
2. Restore NLA to 1 (TO-AL-r5).
3. Run one Cottonwood day end to end under condition 6, with the rules still disabled until the run record reads back. Then run the backfill
   to the floor.

-- 1.0.0_SA_CTO (laptop)
