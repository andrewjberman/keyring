# ANDREW-DIRECT 2026-10-09 ~06:0xZ -- the Holdings lane (IRPT_BCKEND workstream M) is done; Analysis and Performance are not ~M2's

Channel: dell2 terminal of 2.0.0_SA_COO~M2, in-session.

VERBATIM:

> I dont see any of your work in the endpoints here. Your workstream was just covering holdings. It seems to me that all holdings
> data and UI are done at this point. if the only question really is just a multi-tenant access RBAC thing, that should be as simple
> as clarifying that we have the standard multi-tenant api/scoped/ layout for global and firm-scoped as we do for Model Portfolios,
> which i believe we already have anyway. The work on "Analysis" and "Performance Reporting" and so on are not your jobn.

Preceded by (~05:4xZ): "Ok this seems like we can close this project out. Ask CRO if we can close this, what actually remains on
endpoints here that arent finished? i can eyeball it and probably just close it".

## Measured by this seat on his RBAC point (2026-10-09 ~06:0xZ)

- The Holdings route is `GET /api/scoped/investor-reporting/holdings/{accountSetId}`
  (`docs/contracts/investor-reporting/v1/routes.json`, operation `holdings-snapshot`, handler `irpt-holdings`): the `/api/scoped/` layout.
- The handler serves the firm's landed snapshot projected to the resolved scope's permitted accounts through `guard()` + `FirmBinding`;
  `irpt-holdings` is Active (last modified 2026-10-06T01:44:23Z, CodeSha256 `SRANzIGz...`).
- Not measured here: a side-by-side of Model Portfolios' global/firm route pair. The comparison stands on his word.

## Effect

- Workstream M's share of FWD-5 is REALIZED (CTO msg 890); the lane closes.
- The UB-20261009T052107Z-32d8 acts (the S392 dry-run pre-read, the D1-S8 trace, the Holdings-tab walk) are NOT run: the lane is done.
- Kept until the CTO says otherwise, because they guard served output under signed halves: the S392 per-fire NO-WORSE read (the
  10:03 / 10:43 ET crons) and the COO never-widen half when dell1 ships the e56 fix.
