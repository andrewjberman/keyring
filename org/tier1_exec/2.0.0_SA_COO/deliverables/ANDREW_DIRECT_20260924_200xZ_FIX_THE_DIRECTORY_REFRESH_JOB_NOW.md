# ANDREW-DIRECT 2026-09-24 ~20:0xZ -- fix the IRPT directory refresh job now

**Channel:** Andrew at the `2.0.0_SA_COO~M` terminal. **Recorded by:** `2.0.0_SA_COO~M`, same turn.

## Verbatim

> Ok lets fix that job righ tnow

(Typo his, preserved.) The context was row IRPT_BCKEND-S125 @662960f9ba: the scheduled `irpt-directory-refresh` job
has dispatched no directory build since 2026-09-18. Two reasons:
- the same-frontier no-op in `directory/refresh.py:736-761`;
- the no-op manifest keyed by the artifact date, which makes alternate fires read REFRESH_TRIGGER_MISSED.

## What it binds

- 2.0.0_SA_COO~M fixes the scheduled job, the `irpt-directory-refresh` Lambda code, and deploys it under the normal
  rules: deploy ledger, Terraform/safe-apply only, served output named with rollback.
- The file sits on 2.0.0_SA_COO~P's lease surface (`infra/aws/lambda/investor-reporting/directory`). ~M takes that one
  file for this fix and tells ~P.
- Not in scope: any change to the directory runner, the schedule, or the directory's contents beyond what the fixed
  job builds on its own.
