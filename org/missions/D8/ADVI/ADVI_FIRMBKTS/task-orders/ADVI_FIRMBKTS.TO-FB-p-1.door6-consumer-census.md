# ADVI_FIRMBKTS task order -- `FB-p-1` -- THE LIVE CONSUMER CENSUS OF THE DOOR 6 MARKER KEY

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->
**Flip this order's `<status>` to `complete` in the SAME commit as your proof instance**, only when AC1 passes.

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R9.md</decomp_doc>
<owned_cells>FB-p-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~85</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- the order adds no rule, schedule or cadence; it reads only.
comp-iam: DECLARED-NOT-APPLICABLE -- no grant is added or changed; the order reads one managed policy.
comp-adversary: RUN by the issuer (`compose` on this order, read-vintage 2026-10-16 ~17:5xZ): any cited commit verified; the only absent cited paths are the record and the proof instance the executor creates. At base the record is absent (AC1 FAIL as expected). The grader rejects a wrong key, a call with a write verb, no consumers, an undetermined writer with no note, and zero denominators. Blindness: it proves the record's shape, not that the census is complete; the CTO reads the census before the retirement runs.
EGRESS CLASS, declared: NONE (AWS reads inside the one account, repository reads).
</preflight>

## 1. THE CELL -- `FB-p-1` (round 9, item 1 of the CTO's enrichment list, first half)

Andrew ruled the Inflection done-marker `opal-data-inf/gold/meta/pipeline-complete.json` (bucket `opal-data-inf`, key `gold/meta/pipeline-complete.json`) and its watcher, the EventBridge rule `mdpf-feeder-accelerator`, RETIRED, with no successor marker, "after a no-other-consumer read". The retirement waits on this census. **Print who reads the key and who writes it, with the denominator of everything you scanned.** You change nothing.

What is already known (verify, do not trust): the S3 notification of `opal-data-inf` on prefix `gold/meta/` and suffix `pipeline-complete.json` to `inf-portal-publisher` was REMOVED on 2026-10-15 (the entry no longer exists; the bucket carries the silver entry alone). The rule `mdpf-feeder-accelerator` is ENABLED with the pattern S3 Object Created on that key and the target `mdpf-feeder-trigger`. The marker is 135 bytes and was last modified 2026-10-16T12:56:43Z. The managed policy `opal-assets-one-way-fan-in-fence` carries a Deny statement `DenyInfGoldSentinelAbsolutely` on the marker's ARN, attached to 13 roles. The schedule `mdpf-feeder-backstop-daily` (cron(52 12 * * ? *), ENABLED) also starts `mdpf-feeder-trigger`. Two repository sources, `inf-gold-freshness-guard` and `mdpf-daily-trigger`, name the key and were absent live. NO inventory names the key's WRITER.

### Steps (read-only; record each call you make)

1. **S3 notifications:** `.tools/aws s3api get-bucket-notification-configuration --bucket opal-data-inf`. List every entry (id, events, prefix and suffix filter, target name). Flag any whose filter matches the key. Denominator: the number of entries.
2. **EventBridge:** list the rules of the default event bus and of any other bus (`events list-event-buses` first, count printed). For every rule whose event pattern names the bucket `opal-data-inf`, or the source `aws.s3` without a bucket, print name, state, the key filter and the targets. Flag every rule that can match the key. Denominators: rules listed, rules naming the bucket. Count client-side: a `--query` length over a paginated list counts the page, not the total.
3. **The live AWS plane:** `comp-find --corpus aws 'pipeline-complete'` (it prints its own denominator: nodes scanned). Classify every hit.
4. **The fence:** read `DenyInfGoldSentinelAbsolutely` in `opal-assets-one-way-fan-in-fence` (its action, resource and the count of attached roles). Record it as an `iam_fence` consumer with status `LIVE_OTHER`.
5. **Code readers and writers:** `comp-find 'pipeline-complete'` over `infra/`, `lib/`, `integrations/`, `.tools/`, naming each directory with its printed denominator. Classify each hit as a reader, a WRITER, or a mention. Look for the gold chain's tail step that writes the key (the full gold chain, the dispatch script, the freshness guard); name the file and line.
6. **The backstop and the trigger:** `scheduler get-schedule --name mdpf-feeder-backstop-daily` (state, cron, target). Record it as a consumer of `mdpf-feeder-trigger` with status `LIVE_OTHER` if it is enabled.
7. **Writers:** list the writers you found, each with evidence. If you cannot determine a writer after steps 3 and 5, set `writer_determined` false and write in `writer_note` exactly what you read.

### The record: `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~85/DOOR6_CENSUS.json`

```json
{"order": "FB-p-1", "read_at": "<ISO UTC>", "key": "opal-data-inf/gold/meta/pipeline-complete.json",
 "calls": ["<every aws or comp-find call, as run>"],
 "denominators": {"s3_notification_entries": 0, "eventbridge_rules_listed": 0, "eventbridge_buses": 0, "aws_plane_nodes_scanned": 0, "repo_dirs_scanned": 0},
 "consumers": [{"kind": "eventbridge_rule", "name": "mdpf-feeder-accelerator", "status": "RETIRING", "evidence": "<the read>"}],
 "writers": [{"name": "<file or role>", "evidence": "<file:line or call>"}], "writer_determined": true, "writer_note": "",
 "not_read": ["<what you did not read, and why>"], "claim": "measured"}
```
`kind` is one of `s3_notification`, `eventbridge_rule`, `code_reader`, `iam_fence`, `other`; `status` is `RETIRING` (will go with the retirement), `LIVE_OTHER` (a consumer that is not part of it) or `ABSENT_LIVE`. At least one denominator above zero. Counts of keys, never key names that identify a client.

## 2. BOUNDS

1. READ ONLY. No `put-`, `delete-`, `create-`, `update-`, `enable-`, `disable-`, `start-`, `invoke` or other write call; no copy of the marker. AWS from bash is `.tools/aws`.
2. Print no secret, no client name, no relationship id. A call that fails is recorded as failed, never retried with more privilege.
3. Anything surprising and off-task is ONE row in the project's surprise channel (the file in `<paths>`), then keep working.

## 3. SURFACES

<paths>
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~85/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~85/ADVI_FIRMBKTS.TO-FB-p-1.door6-consumer-census.proof_of_spec.json` (named by this file's whole stem).
  <criterion id="AC1" cell_refs="FB-p-1"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 60 python -I org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round9/checks/r9_checks.py door6census --file org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~85/DOOR6_CENSUS.json</invocation><expect>^DOOR6CENSUS: OK consumers=[0-9]+ live_other=[0-9]+$</expect></criterion>
</proof_of_spec>

AC1 grades the record's shape and read-only discipline, not that the census is complete.

## 5. WHEN YOU ARE DONE

Commit the record FIRST, your rows and the proof instance second. Report once: the consumers by status, the writers found or `writer_determined` false, and the denominators.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Round 9 item 1, first half (CTO analysis @bc6444b8e2). `FB-p-2` is staged behind this census, the CTO's read of it and the recorded decision. The census may find the key's writer undetermined; that is a finding, not a failure, and the retirement then needs the writer named first.

<status>pending</status>
<round>9</round>
<workstream>DOOR6</workstream>
<to_id>ADVI_FIRMBKTS.TO-FB-p-1</to_id>
<slot>~85</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
