# TO IRPT_DASHBD.TO-DB-b-195 -- READ why Cottonwood's account_return_daily gold stops at 2026-06-22: its producer, its schedule or trigger (DESIRED against APPLIED), the trading-calendar count of days since, and what a resume needs; read only

<to_id>IRPT_DASHBD.TO-DB-b-195</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~160</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>103</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-102 ANALYSIS item 3 ("name its producer, its schedule or trigger (DESIRED vs APPLIED), and why the newest partition stops at 2026-06-22 (trading calendar); name what a resume needs. A resume that writes served or gold partitions is a later round under a pair. This cell reads only.") | **Rows:** IRPT_DASHBD-D2-W160-S<k> | **Decomp cell:** `DB-b-195` (decomposition section 105) | **outcome_ref:** FWD-21, FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-160` (branch `wk-IRPT_DASHBD-160`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~160/`.

**What is known (the issuer's own read, 2026-10-14).** Cottonwood's gold lives at the `lib/opal_naming.py address()` bucket, NOT the registry's bucket field: `s3://opal-data-cottonwood/irpt/cottonwood/gold/`. It holds `account_return_daily` with 3,325 daily `date=` partitions from 2013, whose schema hash equals its contract's (`org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json`), and `dim_return_method` (method_version 3), `holdings`, `holdings_performance_daily`, `holdings_performance_manifest`, `holdings_qa`, `account_return_daily_blank_reasons`. The previous round's read found the newest `account_return_daily` partition is `date=2026-06-22`. Today is 2026-10-14. Nobody has said why it stops or who or what writes it.

**The cell (`DB-b-195`): a READ. Nothing is changed, deployed or written (outside your folder).**
1. **The producer.** Find what writes Cottonwood's `account_return_daily` (the manifest beside each partition names its writer; read the newest partition's `manifest.json` and one early one by S3 GET, counts and keys only; then the code: start from `data/assets/scripts/gold/irpt_reporting/` and `data/cot/scripts/` with `comp-pipescript io <script>` and `comp-which "cottonwood account return daily"`; the earlier adapter attempt is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~48/` (`adapter_returns.py`, `adapter_source.json`)). Record `producer` {`name`, `entry_file` (an EXISTING repo-relative file)}.
2. **Its schedule or trigger, DESIRED against APPLIED.** DESIRED = what the repo, the dispatch catalog, Terraform or a doc says should run it and when; APPLIED = what is actually live (the EventBridge rule or schedule, S3-event trigger, Lambda, or a manual run) read with live `describe` / `get` calls of named resources (`.tools/aws` shim, never bare aws; enumerate through the served graph first: `comp-find --corpus aws` or `comp-estate --resource <name>`, per the repo's rail). Record `schedule` {`trigger_kind` (one of EVENTBRIDGE, S3_EVENT, MANUAL, NONE, OTHER), `desired` (words), `applied` (words), `evidence` (words: which resource or file you read)}.
3. **Why it stops at 2026-06-22.** Say it from evidence: a last successful run, a disabled rule, a removed trigger, a failing run, a source (Black Diamond silver) that stopped, or a manual-only producer last run then. `why_it_stops` (words, evidence named). `trading_days_since_newest`: the number of NYSE trading days after 2026-06-22 up to and including `read_on` (the ISO date you read it, 2026-10-14 or later), counted with `lib/trading_calendar.py` (`len(trading_days_between("2026-06-22", read_on)) - 1`; the checker recomputes it). Write the address of the prefix as `address` (bucket and prefix without date partitions) and `newest_partition` "2026-06-22" (re-list the newest partitions of that one prefix with named-prefix `aws s3 ls` and confirm; if a newer partition exists, record it and the criterion will fail and the issuer will read why).
4. **What a resume needs.** `resume_needs` (words: the trigger or run, the inputs it reads and whether they are current, the method version, any pair or hold that applies) and `resume_writes_gold` (bool: a resume writes gold partitions, so it is a LATER round under a never-widen pair; you write NOTHING). `recommendation`: one to three sentences.
5. **Record** `COTTONWOOD_RETURN_STALE.json` in your folder with exactly: `producer`; `schedule`; `newest_partition`; `address`; `read_on`; `trading_days_since_newest`; `why_it_stops`; `resume_needs`; `resume_writes_gold`; `recommendation`; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Names, addresses, counts and words only: no figure, no account number, no run of eight or more digits (an `address` value is exempt only under the keys `path`, `file`, `key`: write the address without date partitions).

<criterion id="DB103-3-AC1" cell_refs="DB-b-195"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r103/p103_round103.py" . DB103-3-AC1</invocation><expect>DB103-3-AC1 PASS</expect></criterion>
`DB103-3-AC1` -- the record names the producer with an existing entry file; states the schedule as a trigger kind with the DESIRED and APPLIED states and the evidence in words; states the newest partition (2026-06-22), its address, the read date (2026-10-14 or later) and the trading days since, which the checker recomputes from `lib/trading_calendar.py`; says why it stops and what a resume needs and whether a resume writes gold; a recommendation; no write, push or deploy; no run of 8 or more digits (a sha256 value, and a value under a key named path, commit, file or key, is exempt: the checker's rule). Base: FAIL (no record).

<expected_criteria>DB103-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No write of any kind to AWS** (no S3 put/copy/delete, no DynamoDB write, no Lambda, EventBridge, Terraform or IAM act, no invoke, no run of the producer), **no deploy, no push, no vendor call, no secret read.** Reads only: repo files; S3 named-prefix LIST and single-object GET; live `describe`/`get` of NAMED resources with the box's existing identity. Take every bucket from `lib/opal_naming.py address()`, never from `data/firm_registry.json`'s bucket field. A denial is recorded verbatim, not retried by another route. If the comp-rail hook refuses a call, run what it says next or annotate `# rail-checked: <why>` (audited).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. Where you cannot establish something say `NOT_ESTABLISHED` with the reason; never guess. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W160-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~160/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-195.why-cottonwood-account-return-daily-stops-at-2026-06-22.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 105 (round 103), cell `DB-b-195`.
<owned_cells>DB-b-195</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB103-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~160/IRPT_DASHBD.TO-DB-b-195.why-cottonwood-account-return-daily-stops-at-2026-06-22.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB103-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the producer and its entry file; the trigger kind with DESIRED and APPLIED; why it stops; the trading days since; what a resume needs and whether it writes gold; the recommendation; row ids. Names, counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read; nothing is changed, deployed or written.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: repo reads, S3 named-prefix LIST and GET and live describe of named resources with the box's existing identity; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the schedule is READ here, not touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on 7 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>
