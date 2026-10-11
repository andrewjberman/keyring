# 0.7.0_AE_CloudOps~RA1 -- 2026-10-11 -- AMGT_RESAPP AMGT-aa-3: the two /compare 500s of the CVO's walk, read to their cause

**Date:** 2026-10-11 (order msg 3984 at 16:12Z; reading committed dc5c1e60b2 at 16:19Z; accepted msg 3996 at 16:20Z)
**Task Order:** AMGT_RESAPP.TO-AMGT-aa-3.read-the-two-compare-500s-to-their-cause
**Status:** AC1 YES; AC2 is the CVO's judgment (UNVERIFIABLE-BY-INSTRUMENT); the issuer flips the status

## Objective

A read-only cause reading of two HTTP 500s (ROG on the Model tab, BA on the Posture tab) that the CVO's portal DEV walk
saw on `/api/scoped/amgt/security/<ticker>/compare`, 15:34Z-15:44Z. Nothing is changed in any system.

## The act
**archetype:** INVESTIGATION

1. Found the serving path through the served graph: `d2n2nzpeqf34ge.cloudfront.net` is distribution `EVTSA9VEHNZVH`;
   behavior `/api/scoped/amgt/*` -> origin `APIGateway-portal` -> HTTP API `7k3ed8px20` (not a REST API), route
   `.../compare` -> AWS_PROXY to `opal-amgt-scoped-api`, behind REQUEST authorizer `opal-portal-authorizer`.
2. Read, over 15:30Z-15:50Z at 60 s: both functions' Invocations, Errors, Throttles, ConcurrentExecutions, Duration; the
   API's Count, 4xx, 5xx, latencies; CloudFront's Requests and 4xx/5xx/Total error rates; the function's log group (n=1266
   events); reserved concurrency and account limits; stage, route, integration and authorizer settings.
3. Read the walk's netlog (n=1418 rows) and `portal/vite.config.ts` and the installed Vite proxy handler.
4. Wrote the reading: CAUSE DEV-PROXY, by elimination, with the sub-cause and the missing source named.

## Compiler Tools

| Tool | Command | Result | Note |
|------|---------|--------|------|
| comp-find | `--corpus aws "d2n2nzpeqf34ge"` | 3 hits of 2891 nodes | the distribution and its two DNS records |
| aws cli / boto3 | the reads above | PASS | all read-only |
| r95_reading_check.py | the order's AC1 invocation | YES, exit 0 | 6 of 6 arms |

**What worked:** reading the whole route, not the layers the order listed: the authorizer is a fifth hop the order did not
name, and its clean Errors/Throttles removed it as a candidate.
**What failed:** my first timestamp print was local time with a literal `Z` typed on it (n=15 datapoints at "11:30Z");
caught on the read-back against the walk window and re-read with an explicit UTC conversion before anything was written.
**Gap found:** the Lambda@Edge `auth-validator-edge:22` regional log groups were not read; CloudFront's 5xx metric
stands in for them. Declared in the instance.

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| CAUSE DEV-PROXY, not UNDETERMINED | every AWS layer reads zero 5xx against a printed denominator and the one remaining layer has a read mechanism that answers 500 with no AWS record; the unobserved sub-cause is named with its deciding source |
| Reported the 72-versus-70 netlog count | the order's own count and the file's differ; the issuer carries the cause, so the number should be the file's |
| Left the order's status alone | AC2 is the CVO's; I do not self-grade a judgment criterion |

## Files Modified

- `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.7.0_AE_CloudOps~RA1/C-S82_COMPARE_500_READING_20261011.md`
- the proof instance beside it and this log (written at the issuer's ask, msg 3996)

## Next Steps

1. `[2.0.0_SA_COO~R1]` Flip the order's status after the CVO grades AC2; cut a fix only after the reading, as its own cell.
2. `[whoever repeats the walk]` Run the dev server with its output redirected to a file; that line decides the sub-cause.
