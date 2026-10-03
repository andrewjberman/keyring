# Research request to 4.0.0_SA_CRO: YCharts direct-API generation, Opal-branded

**From:** 2.0.0_SA_COO~Y (IRPT_BCKEND ~Y Analysis workstream), 2026-10-03 ~17:1xZ
**To:** 4.0.0_SA_CRO (L1 brief owner)
**Ask:** write the L1 brief for this research project from the needs below.

## Andrew's words (verbatim, at the 2.0.0_SA_COO~Y terminal, 2026-10-03 ~17:0xZ)

> It has no need to take 15-20 minutes. this is four api calls and a generation. I honestly feel like we should be able
> to run the api calls, persist and categorize the response shape per api call, and identify from the 3 generation
> types where and how those contracts are materialized in the actual generated export file (via parsing or otherwise).
> then once we assess how that is constructed, we run the generation with our own custom script that uses the same
> endpoints but opal branded. also those outputs have to be bucketed on our side of course.

> i recommend you make a request to run this research project with the needs as listed to CRO

## The needs, as Andrew listed them

1. Run the YCharts API calls; persist each call's response and categorize its shape, per call.
2. For the three generation types, find where and how each call's response contract is materialized in the generated
   export file (by parsing or otherwise). The types: Overview (template 14141822, 0 comparisons), Comparison
   (14141824, 1), Multi (14141847, 2-5) (`infra/aws/lambda/investor-reporting/ycharts/generate/recipe.py:121-146`).
3. Then generate with our own custom script that calls the same endpoints, with Opal branding.
4. Bucket those outputs on our side.
5. The latency goal: "It has no need to take 15-20 minutes."

## Measured context (Y-3 job REQ-329a56182b2668d44a28c8d7, Multi, Cottonwood, READY)

Source: `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_Y/Y3/V1A/V1A2_multicomp_ult_iwm_cottonwood_20261003.log`.

| state | from | span |
|---|---|---|
| QUEUED (K5 POST) | 16:45:31Z | 19 s |
| SUBMITTING (portfolio_create onward) | 16:45:50Z | 15 m 19 s |
| DOWNLOADING (vendor PDF) | 17:01:09Z | 35 s |
| CERTIFYING (retained PDF) | 17:01:44Z | 1 m 30 s |
| READY | 17:03:14Z | total 17 m 43 s |

INFERRED, not measured on this job: most of the SUBMITTING span is our own wait. The read-back takes ONE status GET per
receive and, on a `calculating` answer, keeps the message for the receive's 900 s (`recipe.py:655-665`,
`READ_BACK_POLLS = 1`, `READ_BACK_LEASE_TTL_S = 900`). That rule exists because the YCharts WAF challenged faster status
polling (CTO 101792, 101917, batch 97). The generate POST alone took 26.76 s in the 2026-09-11 live run
(`recipe.py:28-30`). The vendor's true calculation time is the first thing to measure.

## What the estate already has (build ladder, step 2)

- The seven-step request contract: `infra/aws/lambda/investor-reporting/ycharts/generate/recipe.py:1-40`
  (template GET, holdings upload POST, create POST, status/read-back GETs, validate POST, generate POST, signed download),
  plus `/securities/securities_info` for comparison identity (`recipe.py:412`). Templates: `templates.json` beside it.
- Research: `docs/research/investor_reporting_ycharts_cloud_20260911/README.md` ("Exact request contracts established");
  `docs/research/investor_reporting_ycharts_variants_20260911/` (the CRO's live proof of all three recipes);
  `docs/research/investor_reporting_ycharts_20260910/` and `..._auth_20260910/`.
- Retained, certified PDFs of READY reports in the evidence bucket (this job: report RPT-c8c4037aaf09c01cd6d7797eb28cc7f8).

## Constraints the brief must carry

- Vendor egress: every YCharts call needs Andrew's word. His standing word covers Analysis runs one at a time with the
  queue empty (2026-09-27; 2026-10-02 ~18:1xZ). Whether it covers research calls outside the job queue is his to say.
- One session per account: the host now shares Andrew's browser session (row S233). A WAF challenge can cost the session,
  and a sign-in is Andrew's act.
- No cookie, token or credential value in any artifact or commit; responses are persisted with secrets scrubbed.
- New S3 addresses and resource names come from `lib/opal_naming.py` builders (CLAUDE.md rule 30); the cross-firm guard
  applies to client holdings.
- OPEN for Andrew: whether the YCharts subscription terms permit YCharts-computed figures in an Opal-branded document.

## Not paused by this request

The ~Y V1 runs continue in order (CTO 104634): Y-3 READY at 17:03:14Z; Y-5 V1, then Y-4 V1, one at a time and spaced.
