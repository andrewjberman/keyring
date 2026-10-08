# ANDREW-DIRECT -- 2026-10-08 ~21:2xZ -- the "custody report" is Performance; build what is additive, and name it accordingly

**Channel:** the `1.0.0_SA_CTO~DELL2` terminal on dell2, in-session.

VERBATIM (two messages):

> Yeah the issue with the custody report is that it really sounds like its just a performance report, I dont see the differnce between
> what youre discussing for that purpose with what will end up being on the performance tab

> if the functions youre building out are additive and currently dont exist on the performance tab, then that is great, but lets refer
> to it accoridngly

## How this seat applies it (scope not widened)

- **The work CONTINUES.** It is additive to Performance and not on the Performance tab today: holdings, activity and fees per account and
  household; the quarter-end client statement rendered as a PDF in each firm's template; and Opal sourcing those figures from the
  custodian instead of Black Diamond. There is no pause.
- **The name, in every record, message, PRD amendment and the frontend mapping from now on:** **"Performance client statement"**,
  meaning the quarterly client-facing export of the Performance report, with the added holdings, activity and fees sections. "Custody
  report" is retired as a product name.
- **Code identifiers already in flight stay as they are:** the `CUSTODY_REPORT` kind, `irpt-custody-x10-v1`, `custody-report-read` and
  `custody_write.py`. Renaming served identifiers costs releases and changes nothing for a user. Each is documented as "the Performance
  client statement" where it is defined.
- **IRPT_CUSTDY's PRD (laptop `1.0.0_SA_CTO`):** its title and wording are asked to follow, through `0.0.0_AB_MSTR~DELL2`. The frontend
  placement (as part of the Performance tab's export) is the CRO's mapping work with Andrew.
