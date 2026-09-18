# ANDREW-DIRECT 2026-09-18 ~19:5xZ -- verify the cross-system claim; and a reconciliation step for the workflow: repo scans coalesced to the newest truth, cross-referenced against comp-tool scans on live or derived-from-live surfaces, every delta investigated, ending in a validated current-state table

**Received at:** the `4.0.0_SA_CRO` terminal, 2026-09-18 ~19:5xZ, one message, following this seat's delivery of
RCN-0010 (@ecf57e8806). **Recorded by:** `4.0.0_SA_CRO`. **Channel:** Andrew-direct, typed at this terminal.
**Verbatim and entire:**

> Check and make sure this is accurate: One resource binds the two migrations and neither run can see it. The MDPF
> feeder fires on a completion sentinel written into opal-data-inf, a bucket the firm-bucket migration retires. The
> runner's dispatch script waits on the same key. A cutover that moves that bucket without repointing the pattern
> silently stops MDPF.. Also, I think there is something here that we can work into the workflow where we
> essentially run the various repo scan (change management, logs), coalesce to whatever the newest truth seems to
> indicate, then cross reference that with the comp-tool scans on confirmed live/derived-from-live surfaces. Any
> delta gets specific investigation/remediation, which leads to a validated "current state" table.

Typos and punctuation his, preserved.

## Part 1 -- the verification, clause by clause (applied plane, 2026-09-18 ~19:5xZ)

| clause as this seat wrote it | verdict | what the live plane and the sources say |
|---|---|---|
| "The MDPF feeder fires on a completion sentinel written into opal-data-inf" | TRUE, and UNDERSTATED | Rule `mdpf-feeder-accelerator` is ENABLED with pattern `Object Created` on `opal-data-inf` / `gold/meta/pipeline-complete.json`, live target `mdpf-feeder-trigger` with DLQ `mdpf-daily-trigger-dlq` (`events describe-rule`, `list-targets-by-rule`). **But that sentinel was last written 2026-09-05T12:52:20Z**; since then `gold/meta/pipeline-failed.json` is written daily (2026-09-18T12:35:45Z). So the accelerator has not fired for 13 days and MDPF still published today -- because the feeder ALSO fires from the Scheduler backstop `mdpf-feeder-backstop-daily` (`cron(52 12 * * ? *)`, live target the same Lambda). |
| "a bucket the firm-bucket migration retires" | TRUE | `ADVI_FIRMBKTS` retires `opal-data-bd`, `-inf`, `-cot` on a proven quiet window (its name and CONTRACTS). |
| "The runner's dispatch script waits on the same key" | FALSE -- same bucket, DIFFERENT key | `mdpf-daily-dispatch.sh:283-301` waits on `gold/eclipse/{RUN_DATE}/_meta/gold_complete.json` in `opal-data-inf`, bounded 30 min, NON-FATAL on timeout (proceeds; roll-forward). The rule's key is `gold/meta/pipeline-complete.json`. |
| "A cutover that moves that bucket without repointing the pattern silently stops MDPF" | OVERSTATED in one direction and UNDERSTATED in the other | The PATTERN is not the binding dependency -- it is already dead (13 days) with no effect. The binding dependency is the feeder Lambda's pre-check: `INF_BUCKET` env (default `opal-data-inf`) + `WSC_GATE_KEY = gold/eclipse/{d}/_meta/gold_complete.json` (`lambda_function.py:86-93,153-168`). If that sentinel is absent the handler returns `NOT-YET`, `dispatched: False`, status 200 -- "NOT an error" -- and NEVER starts the runner: no DLQ, no alarm. So a move of `opal-data-inf` without repointing the Lambda's env silently STALLS the feeder chain (WS-B/C/D/E feeds, the runner's six stages). It does NOT stop MDPF: `mdpf-scheduled-floor` still fires `mdpf-gold-lambda` at 13:30Z and the publisher at 13:50Z, so the portal keeps receiving a daily platinum built from whatever feeds last landed -- plausible, stale, un-alarmed. The accurate sentence: **a cutover that moves `opal-data-inf` without repointing the feeder Lambda's `INF_BUCKET` silently stalls the feeders and silently stales the served artifacts; nothing stops and nothing alarms.** |
| "One resource binds the two migrations" | UNDERCOUNTED | FOUR carriers, on TWO legacy buckets: (1) the rule's pattern (`opal-data-inf`, dead); (2) the feeder Lambda's `INF_BUCKET` + `WSC_GATE_KEY` (the live gate); (3) the same Lambda's `BD_BUCKET` = `opal-data-bd` + `WSE_GATE_KEY = schwab/silver/rps/date={dc}/data.parquet` (reported, not gating -- `wse_ready`); (4) the dispatch script's `INF_BUCKET` wait. Both `opal-data-inf` and `opal-data-bd` are buckets `ADVI_FIRMBKTS` retires. |
| "neither run can see it" | TRUE | The MDPF engine run carried the rule as a GRAMMAR tension on its name; the 49F run does not carry it; neither carries a Lambda's environment or a script's wait. |

**A finding that fell out of the verification, surfaced as a row, not chased:** `opal-data-inf/gold/meta/pipeline-complete.json`
has not been written since 2026-09-05T12:52:20Z while `gold/meta/pipeline-failed.json` is written daily (last
2026-09-18T12:35:45Z) and the per-date eclipse sentinels ARE written daily (09-16 12:36:57Z, 09-17 12:35:43Z, 09-18
12:35:54Z). Whether the INF gold chain is failing daily, or deliberately ends without the completion marker since
some 09-05/09-06 change, is UNMEASURED here and is that chain's owner's question. The MDPF accelerator's death is
the consequence and is exactly the "invoker-only freezes invisibly" shape the feeder's own topology note
(`lambda_function.py:17-35`) was built to survive -- and did.

## Part 2 -- what the second sentence binds

Andrew describes a RECONCILIATION step for the workflow: (a) the repo scans (change-management, session logs) run;
(b) their claims are COALESCED to the newest truth per resource (the latest-dated record wins as the CLAIM);
(c) that claimed state is cross-referenced against the comp-tool scans on CONFIRMED LIVE or DERIVED-FROM-LIVE
surfaces (the graph at its `built:` vintage, live `s3api`, `describe-rule`, `get-schedule`, `comp-iam live`);
(d) every DELTA between claimed and measured gets a specific investigation or remediation; (e) the result is a
VALIDATED "current state" table. Read as narrow as the words: it is a step of the run, its output is the
current-state table, and the deltas are rows with owners. It is folded into the pipeline-walk brief as outcome O9
and rule W14 (amendment 1, same commit as this record), where the worked example is today's own instance: the
`ec2.tf` comment (older claim: `mdpf-daily-trigger` starts the runner) vs the 2026-08-07 record (newer claim:
retired) vs the live plane (no such Lambda; `mdpf-feeder-trigger` holds `ec2:StartInstances`) -- newest record and
live agree, the declaration is the stale one, and the delta's remediation is a one-line comment fix owned by the
Terraform lane.

## What it does NOT decide

- The integration carrier for the brief (an addendum outcome set, a round, MAP cells): `1.0.0_SA_CTO`'s at L2/L4.
- The INF chain's `pipeline-failed.json` state: its owner's; a row is filed, nothing chased.
- No gate is created; the correction lands BESIDE the original record and message, never as a silent rewrite.

**Author:** 4.0.0_SA_CRO (Chief Research Officer) . **Home:** org/tier1_exec/4.0.0_SA_CRO/
