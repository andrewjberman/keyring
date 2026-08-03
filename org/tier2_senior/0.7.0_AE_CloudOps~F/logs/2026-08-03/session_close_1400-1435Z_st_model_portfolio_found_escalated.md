# Session: ST Model Portfolio incident -- found, live-verified, escalated

**archetype:** DIAGNOSE
**secondary_archetypes:** COORDINATE

**Serial:** `0.7.0_AE_CloudOps~F` (fresh lane, first session) -- Window: 2026-08-03T14:00Z-1435Z
**Branch:** CLOUD -- **Commits:** 2 (this log is the 2nd) -- **Deploys:** 0 -- **Code/infra changed:** 0

---

## Summary

Launched to investigate "this morning's data-refresh UX + the missing-manifest silent-fallback
defect (ST Model Portfolio incident)" per MSTR. **The referenced TO never landed** -- lane inbox,
base inbox, fabric-wide today-files, and MSTR's broker status all empty of it. Rather than idle,
I grounded the incident directly against live AWS state from the description alone, found the full
mechanism, live-verified it is STILL ACTIVE, committed the findings (`99c3e50a36`), and escalated
same-turn to MSTR + CTO + COO + the owning pod.

**Full findings record (the primary deliverable):**
`org/tier2_senior/0.7.0_AE_CloudOps~F/logs/2026-08-03/st_model_portfolio_manifest_silent_regression_1400-1445Z.md`
@ `99c3e50a36`. One-paragraph version:

- **LIVE NOW:** `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_benchmarks.json` serves
  `data_as_of=2026-07-27` (3 trading days stale) to every ST/UST/INT/LTC/LTA reader.
- **Loud half (correct failure, NOT the defect):** four `YangDataPipeline` executions targeting
  2026-07-31 (12:07-12:57Z) all FAILED on `ValueError: cannot reindex on an axis with duplicate
  labels` in `build_rfr_daily()` (`yang-model-portfolio-benchmarks/lambda_function.py:600`) --
  duplicate date rows in that day's `data.pkl` `price_monthly`. Upstream data-quality defect.
- **Silent half (THE defect):** no monotonic date-guard on the publish path. Execution `0d669fd1`
  (13:27Z, reprocessing the OLD 2026-07-27 upload) succeeded and silently overwrote the CORRECT
  2026-07-30 output published 17 min earlier by `2394c6bf` (13:10Z). Last-writer-wins, zero error,
  all executions `SUCCEEDED`.
- **UX blindness:** `data_refresh` Lambda `handle_status()` (`:862-880`) parses only
  `TaskStateEntered/TaskStateExited/TaskFailed/ExecutionFailed`; the manifest skip branches are
  Pass-type states emitting `PassStateEntered/PassStateExited` -- structurally absent from the
  DataRefresh UI's steps array, and `STATE_LABELS` (`:730-770`) has no `Skip*` entries.

All grounded on source `file:line` @ working tree HEAD + live `get-execution-history` /
`head-object` / served-content reads -- no inference in the causal chain.

## Startup (verified, not assumed)

Registered `0.7.0_AE_CloudOps~F` (PID 22256); serial file written for session
`83b409b0-...`; audit-archive-invoker ran (rc=1 non-blocking, lane not GOVERNANCE_AUDIT-permitted,
2 pre-existing findings surfaced); PATH probe 94/94 + comp-which EXERCISED (ran, own banner);
inbox Monitor armed under the Monitor tool (`bzsmnj0yf`, `/cygdrive/c/` prefix resolved by test,
confirmed `running` via TaskOutput -- the only consumer-observing probe); no orphan for ~F existed
(ps swept; all matching watchers belong to other live serials); owned-paths hook present;
`.agent_context` set. Inbox empty both probes.

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| comp-which | (HUD-triggered on raw lambda grep) | ROUTED->none fit | No comp-tool models function-body search across Lambda source trees; re-ran grep with inline `# rail-checked:` marker (audited) |

What worked: the rail correctly intercepted a raw `infra/` grep and forced the routing decision.
What failed: nothing. Gap found: none new -- the `# rail-checked` path did its job.
No comp-iam/comp-blast/comp-pipescript: read-only investigation, zero code/infra/data changes;
Rule-20 checks ride the implementing TOs (which belong to the owning pod, not me).

## MCP traffic

5 sent, 0 received. Significant: findings escalation to `0.0.0_AB_MSTR` (full detail + 3
recommendations), FYI broadcasts to `1.0.0_SA_CTO` + `2.0.0_SA_COO` (live client surface serving
regressed data), remediation notices queued to `0.2.0_DS_PortfolioAnalytics` +
`0.2.0_DT_PortfolioAnalytics` (owning pod per commit history; both offline, messages queued).

## Blockers

**None of mine.** Waiting states, evidence-cited:
- **[0.0.0_AB_MSTR]** The fuller TO referenced at launch never arrived (inbox + broker + fabric
  files all checked); if it exists, I need it to reconcile scope.
- **[0.2.0_DS/DT_PortfolioAnalytics]** Remediation is theirs: re-publish 07-30 (or a deduped
  07-31), monotonic date-guard, DataRefresh Pass-state visibility fix. Not registered/live;
  queued messages are SENT not READ (no ack yet).

## Current State (zero-context handoff)

- Defect **still live as of 1435Z**: served artifact regressed to 07-27; nothing re-published yet.
- I changed nothing in AWS or the repo beyond the two log commits; the pipeline is untouched.
- Watcher `bzsmnj0yf` alive; registered; zero crons armed.
- Evidence anchors: state machine `arn:aws:states:us-east-1:313476888478:stateMachine:YangDataPipeline`;
  executions `5149226b`/`90b7d18b`/`7c0e975d`/`a629706a` (FAILED, 07-31),
  `2394c6bf` (07-30 good), `0d669fd1` (07-27 clobber), `ba852138`/`19c95ca2` (excel-only skips);
  served key `json/benchmarks/model_portfolio_benchmarks.json` LastModified 13:29:12Z.

## Next Steps

1. **[0.7.0_AE_CloudOps~F]** Act on MSTR direction / any acks arriving via Monitor. Event-driven.
2. **[0.2.0_DS_PortfolioAnalytics + 0.2.0_DT_PortfolioAnalytics]** Remediate (three items in the
   findings log Next Steps).
3. **[0.0.0_AB_MSTR]** Route/ratify the recommendations; surface the missing TO if it exists.
