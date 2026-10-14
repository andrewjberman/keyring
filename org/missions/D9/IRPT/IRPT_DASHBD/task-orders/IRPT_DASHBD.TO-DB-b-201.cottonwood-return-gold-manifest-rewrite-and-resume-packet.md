# TO IRPT_DASHBD.TO-DB-b-201 -- COTTONWOOD'S RETURN GOLD: who rewrote its manifests on 2026-10-11 (a read), then the RESUME PACKET onto a schedule (the backfill from 2026-06-23 to T-1 by the trading calendar, the schedule, the keys written, the rollback); a read and a packet, nothing is written to AWS

<to_id>IRPT_DASHBD.TO-DB-b-201</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~166</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>104</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-104 ANALYSIS item 4 and the ruling on row W155-S10 ("RESUME, on a schedule. A MANUAL trigger on a gold producer is a production defect ... FIRST explain W160-S5: who rewrote Cottonwood's newest and 2013 manifests on 2026-10-11. Served gold with an unknown writer is not resumed on top of. Then the packet: the backfill from 2026-06-23 to T-1 by the trading calendar, the schedule it moves onto (an EventBridge rule, its owner and cron), the keys written, and the rollback.") | **Rows:** IRPT_DASHBD-D2-W166-S<k> | **Decomp cell:** `DB-b-201` (decomposition section 106) | **outcome_ref:** FWD-21, FWD-2 | **depends_on:** none (round 103's `DB-b-195` read: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~160/COTTONWOOD_RETURN_STALE.json`).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-166` (branch `wk-IRPT_DASHBD-166`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~166/`.

**What is known (round 103's read).** Cottonwood's `account_return_daily` gold is at `s3://opal-data-cottonwood/irpt/cottonwood/gold/account_return_daily/` (3,325 daily `date=` partitions from 2013; schema equal to its contract); its newest partition is `date=2026-06-22`. The producer is the ADVI_COTBKF silver adapter `data/assets/scripts/silver/commonwealth_account_return_daily.py`, which imports the gold writer `data/assets/scripts/gold/irpt_reporting/account_return_daily.py` and calls its `emit_day`; its trigger is MANUAL (no schedule declared, none live); its single input is a Commonwealth snapshot pinned at 2026-06-23 (the only partition under the Commonwealth Cottonwood silver `daily_returns` prefix). The newest and the 2013 `manifest.json` objects both carry a LastModified of 2026-10-11 (07:03 to 07:17 local), while the producer's last mint was earlier: the writer of that rewrite is NOT_ESTABLISHED (row `IRPT_DASHBD-D2-W160-S5`). The 49 Financial gold has an enabled schedule (`irpt-49f-reporting-gold-daily`, a rule on the reporting-gold Lambda); Cottonwood's has none.

**The cell (`DB-b-201`): a READ and a PACKET. Nothing is changed, deployed or written.**
1. **Explain the 2026-10-11 rewrite FIRST.** Establish who or what wrote the newest and the 2013 manifests, from evidence: S3 object VERSIONS of those two keys (`list-object-versions` of the named keys: count the versions, their LastModified and sizes; counts and times only), the `manifest.json` content keys (counts and key names, no figure; any `writer`, `run_id` or `producer` field it carries), CloudTrail or S3 data events if the account records them (named-resource lookups only), the Lambda or Step Functions run history of the reporting-gold and ADVI_COTBKF functions around 2026-10-11 (`describe`/`get`/`filter-log-events` of NAMED resources), the repo's commits of 2026-10-10 and 2026-10-11 touching the producer or the adapter (`git log --since=2026-10-10 --until=2026-10-12 -- <paths>`, names and subjects), and the seat session logs of that day if one names it. Record `manifest_rewrite_2026_10_11` {`established` (bool), `writer` (a seat, a function or a person's role in words, or exactly `NOT_ESTABLISHED`), `evidence` (words: what you read), `versions_read` (an integer: the number of object versions you counted across the two keys)}. If you cannot establish the writer, say so plainly and the packet below must make the resume conditional on it (item 3).
2. **The input.** Find what the resume would read and how far it reaches: the Commonwealth Cottonwood silver input's newest partition (`input_available_through`, ISO) by a named-prefix LIST (the bucket and prefix from the adapter and `lib/opal_naming.address()`, never the registry's bucket field), and whether it covers the backfill to T-1. If it does NOT (the input is pinned at 2026-06-23), the packet says exactly what is missing (`gap_in_words`) and what the resume is blocked on (`resume_blocked_on`: a Commonwealth delivery, a change to the pinned date, a decision): a resume that cannot read newer input is not a resume.
3. **The resume packet.** `COTTONWOOD_RESUME_PACKET.md` in your folder, modelled on `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/NEVER_WIDEN_PACKET_FDRXX_CASH_CLASSIFIER.md`, with the numbered sections the checker looks for: `## 1. The act` (the backfill of `account_return_daily` from 2026-06-23 to T-1 by the trading calendar, `lib/trading_calendar.py` (`backfill_to` is the last trading day on or before the day before the apply; for this packet use 2026-10-12 as the reference end), and the schedule the producer moves onto), `## 2. What moves` (the partition count the backfill writes (`len(trading_days_between(from, to))`, counted by the calendar module), objects per partition (`data.parquet`, `manifest.json`), what pages read this table: say which, and what changes in their figures), `## 3. When and where` (the schedule: an EventBridge rule whose name comes from `lib/opal_naming.py name()`: how you derived it, its owner serial (an AE seat class) and its cron, with the trading-day rule and the 49 Financial rule as the model: read `infra/aws/terraform/investor-reporting/reporting-gold/` for its shape; a rule that needs a registry row is a FINDING row, not a hand-typed name), `## 4b. Writers` (every writer of the target prefix, counted, including the unexplained 2026-10-11 writer), `## 5. Both branches` (the backfill lands; it fails part-way: what a partial range looks like), `## 6. Rollback` (per key: the bucket's versioning state read live, the previous version of each rewritten manifest, deletion of the new partitions; and that NO other key moves), `## 7. Conditions` (ledger first; the unexplained writer explained or ruled; the input available through the backfill end; the trading calendar's fallback state: `pandas_market_calendars` is absent on this box and `lib/trading_calendar.py` answers from its hardcoded NYSE fallback (covers 2010-2027): say whether that is acceptable for the date range; the questions for the CTO's half), `## 8. Not established`. The packet says "never-widen".
4. **Record** `COTTONWOOD_RESUME_PACKET.json` in your folder with exactly: `manifest_rewrite_2026_10_11` (as above); `resume_packet` {`backfill_from` "2026-06-23", `backfill_to` (ISO, 2026-10-12 or later), `trading_days_count` (the checker recomputes it with `lib/trading_calendar.py`, inclusive of both ends), `input_available_through` (ISO), `input_covers_backfill` (bool; true only when `input_available_through` is on or after `backfill_to`), `gap_in_words` and `resume_blocked_on` (required when the input does not cover), `schedule` {`kind` "EVENTBRIDGE", `rule_name`, `owner`, `cron`, `name_source` (how the name comes from `name()`)}, `keys_written` (`[{bucket: "opal-data-cottonwood", prefix: "irpt/cottonwood/gold/account_return_daily/", objects_per_partition: 2}]`), `rollback` (words), `no_other_key_moves` true}; `writes_in_this_cell` false; `packet_file` and `packet_sha256`; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, names, dates and words only: no figure, no account number; a sha256 value is exempt from the digit rule.

<criterion id="DB104-5-AC1" cell_refs="DB-b-201"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r104/p104_round104.py" . DB104-5-AC1</invocation><expect>DB104-5-AC1 PASS</expect></criterion>
`DB104-5-AC1` -- the manifest rewrite states whether the writer is established, the evidence in words, the object versions counted, and the writer or exactly NOT_ESTABLISHED; the resume packet's backfill runs from 2026-06-23 to a date on or after 2026-10-12 with a trading-day count the checker recomputes from lib/trading_calendar.py; the input's availability is an ISO date and input_covers_backfill agrees with it, with the gap and the block named when it does not cover; the schedule is an EventBridge rule with its name source, owner and cron; the keys written lie under irpt/cottonwood/gold/account_return_daily/ in opal-data-cottonwood; the rollback is stated, no other key moves, nothing is written in this cell; the packet file exists, is hashed, says never-widen and carries the eight numbered sections; no write, push or deploy. Base: FAIL (no record).

<expected_criteria>DB104-5-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No write of any kind to AWS** (no S3 put/copy/delete, no DynamoDB write, no Lambda, EventBridge, Terraform or IAM act, no invoke, no run of the producer or the adapter), **no deploy, no push, no vendor call, no secret read.** Reads only: repo files; S3 named-prefix LIST, `list-object-versions` of the two named keys, single-object GETs of the two manifests (counts and key names only); live `describe`/`get`/`filter-log-events` of NAMED resources with the box's existing identity (`.tools/aws`, never bare aws; enumerate through the served graph first). Every bucket from `lib/opal_naming.address()`, never `data/firm_registry.json`'s bucket field. A denial is recorded verbatim, not retried by another route. If the comp-rail hook refuses a call, run what it says next or annotate `# rail-checked: <why>`. Scratch copies of the manifests hold account-level keys: keep none.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Where you cannot establish something say NOT_ESTABLISHED with the reason; never guess. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W166-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~166/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-201.cottonwood-return-gold-manifest-rewrite-and-resume-packet.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 106 (round 104), cell `DB-b-201`.
<owned_cells>DB-b-201</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB104-5-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~166/IRPT_DASHBD.TO-DB-b-201.cottonwood-return-gold-manifest-rewrite-and-resume-packet.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB104-5-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; who or what wrote the 2026-10-11 manifests (or NOT_ESTABLISHED) and the evidence; the input's newest partition and whether it covers the backfill; the trading days of the backfill; the schedule (rule name source, owner, cron); the keys; the rollback; what blocks the resume; row ids. Counts, names, dates and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a packet document; nothing is written, served or deployed; the apply is a later WORLD order under a pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: named-resource reads with the box's existing identity; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule is READ and PROPOSED in the packet, not touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on 4 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>
