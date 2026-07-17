# Andrew-direct instruction record — DataRefresh UI scope adds

**archetype:** SCRIBE
**Channel:** direct into 0.2.0_DE_PortfolioAnalytics live session (this terminal), 2026-07-17 ~13:5xZ,
mid TO_PORTALREFRESH_FE_01 build.
**Broadcast:** MCP to CTO (20260717T140121Z), COO (20260717T140126Z), MSTR (20260717T140130Z) — same turn.

## Verbatim (the phrasing IS the ruling)

> "Additionally, I want you to get rid of the "Time Machine" panel on the History tab of the Data
> Refresh page, that feature is no longer in production. Furthermore, I want you to add a new tab in
> the Data Refresh portal page so that it is a lot easier for non-technical people to address in the
> event of an issue. Specificaly, I believe this is a user interface design task. I believe that there
> should be a tab called "Emergency Rollback" which includes a simple panel with a single button that
> runs the process to the last upload, including an animation similar to the upload tab, and similar
> panel structure in general to that upload tab, albeit designed round this Emergency Rollback
> concept. I want you to sketch it out for me in ascii in this chat so i can see some options,
> essentially /draw some options and Ill approve one for your implementation."

## Execution disposition (surfaced, not adjudicated)

1. Time Machine panel removal from HistoryTab — immediate, rides the FE_01 DEV commit.
2. "Emergency Rollback" tab — SKETCH-FIRST: ASCII options presented in-session; Andrew's approval of
   one option gates implementation. Reuses FE_01 confirm/lockout/progress machinery against the
   existing rollback endpoint, targeted at the most recent successful upload.
