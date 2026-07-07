# bd-client-detail writer-location trace -- escalates to a LIVE STALE-DATA finding (91 days)

**archetype:** DIAGNOSE
**secondary_archetypes:** TRACE, COORDINATE

**Serial:** 0.4.0_DS_ClientPlatform~B
**Window:** ~1355Z -> ~1415Z 2026-07-07
**Trigger:** CTO ruling (135514Z) on the AC4 bd-client-detail attribution finding -- ruled (b)
relabel READS_S3 + locate the real writer, asked me to run the writer-location trace + file as a
live-graph correction to GLOBGRPH ingestion ownership.

## Writer-location trace (source-grep discipline, per CTO's instruction)

`comp-grep "gold/clients/"` across `data/` + `infra/` (7581 files scanned): **the only producer match
in the ENTIRE repo is `data/black_diamond/archive/fargate/scripts/gold_layer/04_generate_clients.py`
-- an ARCHIVED (legacy Fargate-pipeline) script.** Zero matches in any current, non-archive tree
(`data/black_diamond/*` excluding `archive/`, scanned separately: 929 files, 0 matches). "bd-portal-
advisor-publisher" (the name bd-client-detail's docstring cites as the writer) does not exist under
that name anywhere in the current codebase (`comp-grep "portal-advisor-publisher\|advisor_publisher"`:
0/7581).

The archived script's `save_json()` (L358-377) confirms the exact key shape:
`key = f"gold/clients/{filename}"` -> `s3.put_object(Bucket=S3_BUCKET, Key=key, ...)`, matching
`gold/clients/{relationship_id}.json`. This IS the historical producer; it has been retired
(migrated to `archive/`, per the BD Fargate->Lambda gold-layer migration).

## GROUNDED (comp-freshness, live S3 state -- not source, not self-report)

```
comp-freshness artifact --raw s3://opal-data-bd/gold/clients/
  last_modified: 2026-04-07T04:35:54+00:00   age: 2193.5h (~91.4 days)   RAW (unregistered cadence)
```

**No object under `opal-data-bd/gold/clients/` has been written since 2026-04-07.** bd-client-detail
is a LIVE, currently-deployed, API-Gateway-invoked Lambda (`GET /api/shared/advisor-intelligence/
clients/{clientKey}.json`) serving client-detail responses straight from this prefix via
`s3.get_object`. Combined with the writer-trace: **the archived producer stopped running, nothing
replaced it, and the live-serving endpoint has been reading from a frozen, ~91-day-stale S3 prefix
ever since** -- unless some other current mechanism writes here that this trace didn't find (source-
grep + comp-freshness both ground the negative; I have not confirmed a live consumer-side symptom,
e.g. actually invoking the endpoint or checking portal UI for stale client-detail data).

**This is bigger than the graph-attribution bug CTO asked me to trace.** The live-graph EXTRA_IN_LIVE
edge (WRITES_S3 on a read-only Lambda) is a downstream SYMPTOM of the graph correctly recording no
current writer for this prefix having ever registered under a Lambda -- because there ISN'T one.
The graph isn't just mislabeled; it's pointing at a genuinely abandoned data path that a live
endpoint still serves from.

## Compiler Tools
| Tool | Target | Result | Note |
|---|---|---|---|
| comp-grep | "gold/clients/" across data/ + infra/ | 7 matches / 5 files | only current-tree hit is bd-client-detail itself (docstring+get_object); only PRODUCER hit is the archived Fargate script |
| comp-grep | "portal-advisor-publisher\|advisor_publisher" | 0 matches | the docstring's named producer doesn't exist in the current codebase under that name |
| comp-freshness artifact --raw | s3://opal-data-bd/gold/clients/ | RAW, age=2193.5h | grounds the STATE claim (live S3, not source/self-report) -- confirms zero writes since 2026-04-07 |

**Gap found:** a live-serving portal endpoint (bd-client-detail) reading from a ~91-day-abandoned S3
prefix, with its own docstring citing a producer that no longer exists in the current codebase.
Escalating -- this reads as a genuine production data-quality issue, not just a graph bookkeeping
bug, and is outside my TO scope to fix unilaterally.

## Blockers
None on my Item-1/Item-2 CSE-P2 work (unaffected). This finding is a NEW, separate escalation.

## Next Steps
1. **[1.0.0_SA_CTO / 2.0.0_SA_COO]** disposition + route: (a) confirm whether `gold/clients/*.json`
   is genuinely meant to be live-refreshed (if so, this is a P1/P0 -- portal serving stale client
   detail to advisors) or whether bd-client-detail itself is a retired/unused endpoint that should be
   decommissioned (if the archived Fargate gold-layer's retirement also should have retired this
   Lambda + its API route, and nothing currently depends on it) -- I don't have visibility into
   current portal call volume/usage for this route to make that call myself.
2. **[0.7.0_AE_CloudOps / GLOBGRPH ingestion owner]** the live-graph correction CTO asked routed here:
   bd-client-detail's WRITES_S3 edge should be READS_S3 (source-confirmed); a WRITES_S3 edge for the
   true (now-archived) producer should NOT be added live (it's retired, not a current dependency) --
   recommend the graph instead carry no WRITES_S3 edge into this prefix at all until/unless a current
   producer is identified, OR mark the artifact class explicitly ORPHANED.
3. My AC4 recognizer (`NFRA_CSE_P2_ac4_lambda_writes_s3.py`) correctly continues to report this as
   `extra_in_live` and does NOT silently reconcile -- no code change needed there per CTO's explicit
   instruction to keep the discrepancy visible.

## Addendum -- invocation-count grounding (CTO-flagged, cheap, sizes the escalation)

CTO asked (non-blocking, "flag if you land on it incidentally") for a CloudWatch invocation-count
signal to size live/dead-route severity before their Andrew escalation. Pulled it directly:

```
aws cloudwatch get-metric-statistics --namespace AWS/Lambda --metric-name Invocations \
  --dimensions Name=FunctionName,Value=bd-client-detail --region us-east-1 \
  --start-time 2025-01-01T00:00:00 --end-time 2026-07-07T00:00:00 --period 2592000 --statistics Sum
```
Monthly buckets: Jan 2026: 9 | Feb 2026: 34 | Mar 2026: ~1-5 (tapering) | **Apr/May/Jun/Jul 2026: ZERO**
(no datapoints at all in three full months).

`aws lambda get-function --function-name bd-client-detail`: `LastModified: 2026-04-06T15:08:11Z` --
one day before `gold/clients/` stopped being written (2026-04-07). Reads as a coincident event: a
4/6 redeploy/migration likely retired the Fargate gold-layer producer AND coincides with traffic
dropping to zero on this route.

**Reported to CTO immediately** (before their Andrew escalation): this reframes the finding toward
dead-code/orphaned-route cleanup rather than an active incident serving stale data to live advisors.
Not fully conclusive -- did not check API Gateway access logs or confirm the portal frontend no
longer calls this route, only the Lambda-side invocation metric. Directionally strong.
