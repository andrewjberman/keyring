# ANDREW-DIRECT 2026-09-25 ~15:2xZ -- Portfolio Management PFOE upload stalls on a 500; routed to the CTO

**Channel:** the 4.0.0_SA_CRO terminal. **Recorded by:** 4.0.0_SA_CRO, same turn. All times US Eastern unless
marked Z.

## Verbatim

> Check my teams with Lauren Harmon, seems to be an issue with trade submission, see if you can find any execution ids
> or associated records from failed uploads via trade submission in the last hour.

> route the instruction to CTO and have them manaage its completion and ping you back when its done

## What Lauren reported

Lauren Harmon wrote in Teams at 10:35 AM ET:

> hey! I'm having trouble submitting a PFOE trade through the portal, I'm trying to upload the file to the portfolio
> management page (new Vident format) but it's not going anywhere once I upload

The Teams chat reader returns a Graph 500 on any window wider than two messages in this thread, so earlier messages
were not read.

## The cause (measured 2026-09-25 14:5xZ-15:2xZ)

1. **The page's saved-state read returns 500 for PFOE and PFDE.**
   - Route: `GET /api/private/portfolio/autosave/{fund}/{account}` on REST API `opal-portal-api` (`f61h681z9g`, stage
     `prod`).
   - Handler: Lambda `opal-portfolio-autosave-get`, source `infra/aws/lambda/portfolio_autosave_get/lambda_function.py`.
   - Stage `prod` served 17 requests between 10:33 AM and 11:08 AM ET, and 15 of them returned 5xx. There were 0 4xx.
     (These are the API Gateway per-minute metrics, read through 11:08 AM.)
   - The handler's own log shows 17 AccessDenied failures through 11:12 AM ET (listed below). The two non-5xx
     requests at 10:33 AM line up with `funds-list` and `versions-list`, one invocation each.
2. **The error.** Verbatim from the log:
   > An error occurred (AccessDenied) when calling the GetObject operation: User:
   > arn:aws:sts::313476888478:assumed-role/lambda-execution-role/opal-portfolio-autosave-get is not authorized to
   > perform: s3:ListBucket on resource: "arn:aws:s3:::opal-data-portal-v2" because no identity-based policy allows the
   > s3:ListBucket action
3. **Why.** The object the handler reads does not exist, and the role cannot list the bucket.
   - The keys are `portfolio-management/autosaves/PFOE/current.json` and `.../PFDE/current.json`. A read with list
     rights returns **404** for both.
   - The only autosaves present are January's `PDFE` and `PDOE` (2026-01-30). That is INFERRED to be a fund-code change.
   - When the caller lacks `s3:ListBucket`, S3 answers a missing key with AccessDenied rather than NoSuchKey.
   - The handler maps NoSuchKey to `200 {"exists": false}` (`lambda_function.py:68-73`), but any other exception falls
     through to `500` (`:75-77`).
   - So any fund with no saved state yet cannot open, and the upload flow behind it stalls.
4. **Nothing else was called.** The upload routes `parse-pickle` (`opal-portfolio-pickle-parser`) and `upload-urls`
   (`opal-pm-upload-urls`), and `autosave-put`, have 0 invocations in the window.
   - The trade-pipeline path (`/api/general/trades/submit`, `trade-submission-handler`) has 0 invocations and 0 rows in
     `opal-trade-submissions` today.
   - So no trade record or execution id exists for this attempt.

## The 17 failed request ids (opal-portfolio-autosave-get, ET)

```
10:33:09 PFDE aa912ed9-1267-4552-b81a-992bc31cb80a
10:33:10 PFDE c1b9c31b-adca-4047-8b03-62e5f926477c
10:33:13 PFDE fe921e3b-3afe-4ea3-9d84-3877df8b8cbf
10:33:14 PFOE 3ffc7610-a184-4749-89ad-972265727c80
10:33:15 PFOE d732250c-d5c2-4aea-b2aa-f2b8feecd9e8
10:33:18 PFOE 10e51fda-9880-4068-a58b-c258f9b28e60
10:33:22 PFOE 80cfc908-aa0c-49c3-81cc-05be2ede81bf
10:33:23 PFOE 03c0f9bf-58af-4bbd-b76a-c0d0bdf98cd2
10:33:25 PFOE e992bd0c-3b1e-48d8-9e6b-96413ce5b7af
10:33:58 PFOE 1590961f-df71-44bd-99e5-ebb5b7997caa
10:33:59 PFOE 8811d3d9-bfdd-45ae-a174-f8e3b1fbb7b6
10:34:02 PFOE a11440e9-f35a-424d-89cc-99bb6f701773
11:08:19 PFOE 0cf37ac8-24ce-4276-bd75-24e3064c3c0b
11:08:21 PFOE 5f63d019-34b2-4ee1-9a75-82e9e68b8dac
11:08:23 PFOE 44f68e3b-f0ea-41e8-8078-87e67c9e7786
11:12:25 PFOE 8cdb02e6-bcce-42b8-bb29-c58814373e1a
11:12:26 PFOE ae068856-8898-44a9-bafa-ec2f35eafa22
```

## Fix options (the CTO chooses; this seat does not act)

- **(a) IAM.** Grant `lambda-execution-role` (or a role scoped to this function) `s3:ListBucket` on
  `opal-data-portal-v2` with a `s3:prefix` condition of `portfolio-management/autosaves/`.
  - S3 then returns NoSuchKey, and the existing code returns `exists:false`.
  - This is a WORLD act: Terraform through `safe-apply`, with a ledger entry.
- **(b) Code.** In `lambda_function.py`, treat a `ClientError` whose code is `AccessDenied` / `403` / `404` on the
  get as not-found.
  - The handler was last changed at `a2c88e77ae` by `0.7.0_AE_CloudOps~Z` on 09-03.
  - It deploys through Terraform, never through `update-function-code`.
- **(c) Data, only if the code change is intended.** Carry the January `PDFE` / `PDOE` autosaves forward under
  `PFDE` / `PFOE`.

**Done when:** Lauren opens PFOE on the Portfolio Management page, the autosave read returns 200, and her Vident upload
proceeds. Then 1.0.0_SA_CTO messages 4.0.0_SA_CRO that it is done, per Andrew.
