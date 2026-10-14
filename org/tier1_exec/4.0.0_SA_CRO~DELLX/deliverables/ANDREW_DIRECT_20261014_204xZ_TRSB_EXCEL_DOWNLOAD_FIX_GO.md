# ANDREW_DIRECT 2026-10-14 ~20:4xZ -- Trade Submission "Download Excel" fix, go

Channel: Claude Code session with `4.0.0_SA_CRO~DELLX` (dell1), in the terminal.

## Verbatim

First message:

> I need you to look into the following fix on "Trade Submission" page of the opalinvest.dev dashboard. Specifically,
> this modal popup does not actually download the excel upon user's clicking it: [Image #1]. It is in the "History"
> tab. I believe we have all of this information in the cloud regardless of whether its in approval/execution/historic
> stage, so we just need to make sure those download excel buttons are functional, starting with the history tab. This
> should be a relatively small edit, and I will likely have you do it directly and go out with the next promote within
> the hour. Just look into it, let me know where the break is, if its a server-side issue where the lambda isnt set up
> for that, or if the UI is not connected client-side, or what.

Second message, after the diagnosis:

> go ahead, make the fix

## What it authorizes

The client-side fix on portal feature branch `cand/dell1/trsb-history-excel-download` (portal commit `040b152f`), its
approval for DEV, and its inclusion in the next promote. Class: opal-internal (the API admits internal callers only).

## Diagnosis it rests on

`trade-dashboard-api` `get_excel_download` returns `download_url`
(`infra/aws/lambda/trade-pipeline/trade-dashboard-api/src/dashboard_api.py:193`; deployed code, LastModified
2026-10-11T19:30:58Z, matches). The portal read `response.presigned_url`
(`portal/src/api/endpoints/trade-submission.ts`), which never exists, so the button did nothing on every tab.
