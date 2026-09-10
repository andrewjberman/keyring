# Andrew-direct: YCharts sensitivity intake and serving brief

**Seat:** 4.0.0_SA_CRO. **Date:** September 10, 2026. **Parent:** Lightweight Investor Reporting, WS3.

The instruction below is preserved with one explicit credential omission: the password Andrew supplied in the conversation is not copied into this repository record. Credential values belong in AWS Secrets Manager, not a brief, log or commit.

## Direction, verbatim except the marked password omission

> "C:\Users\AndrewBerman\Desktop\YCharts Transcripts" Now we are ready to move to the next item, which should also be a new brief under the investor reporting group. in this folder we have all the information that exists thus far for building the ycharts sensitivity analysis function. there are some items that are missing and not clarified in here but the whole generation flow, both in transcripts for each of the three types and associated three hars tracking are all in here. this way you can design a script for the retrieval of these items (or at least write very explicit instructions in the brief), the manifest.json has the input fields as well. a lot here to explore to design the ycharts serving tab. The one aspect it does not cover is ingestion. We are going to basically pull emails to the opalbloomberg@opalinvest.com email (sitez email) via a forwarder email (requests@opalinvest.com). Part of the brief should be describing a poller that runs on that email (preferably cloud-based) maybe every 15 minutes during working hours 8a ET naive to midnight. Part of our work will be setting up that poller and some kind of analyzer to address the relevant inputs for the flow, which i really hope we can do entirely programmatically. we should include the login credentials for ycharts in AWS Secrets Manager as alyssakeith@opalinvest.com and [PASSWORD SUPPLIED IN CONVERSATION; OMITTED FROM REPOSITORY]. For the cookie bundle storage, I think there should be a lib for this in the cloud just like how we do it for Black Diamond for Cot and Orion for Inflection, same style of pattern. I would have a bucket for all this (encrypted of course) opal-data-ycharts with a bucketing structure for keeping records of the generations. Let me know if you have additional questions as there is a lot to cover on this and want to make sure its sequenced correctly and i fill in any gaps as needed.

## Clarifications in the same active turn

In response to questions about every-day versus weekday polling and sharing the single YCharts login:

> Every day. We will just kick alyssa off and she can just kick us off.

In response to whether forwarded requests contain actual holdings attachments or merely SharePoint/Teams links:

> yes it will have the holdings attachments

Andrew then specified the existing runner pattern:

> Yeah i would use the same pattern as BDAPI with Kimi

> use the exact same style of runner, that strategy works very well. I don't believe they send OTP so dont need that part

## Scope to carry

Create a separate citable WS3 brief under the existing Investor Reporting umbrella, with explicit generation/retrieval instructions, email attachment intake, Analysis-tab serving, encrypted generation records and cloud session reuse. Poll every day at quarter-hour intervals from 08:00 through 23:45 America/New_York; midnight ends the requested window. Automatic login takeover and interruption by Alyssa are accepted; resumable jobs must prevent duplicate portfolios/reports. The packet's earlier manual-session scheduling preferences do not override this current direction. Actual holdings attachments are the intake contract.

Retain captured evidence separately from handoff prose and proposed implementation. Do not silently substitute the packet's separate non-YCharts analytics engine for the requested YCharts-backed product. No analyst/recipient email is authorized merely by reading this direction; any future distribution behavior belongs in the product specification and its source-supported review flow.
