# TO IRPT_DASHBD.TO-DB-c-4 -- the PRODUCER READ: what wrote Cottonwood's `holdings_performance_daily` gold up to 2026-09-25 (a function, a host job or an ad-hoc run), its code path and last run; the 2026-06-09 prior-day input; the rewrite times of the silver partitions 2026-09-23 to 2026-09-25 against the gold objects of those dates; a read; words, counts and instants only; nothing written

<to_id>IRPT_DASHBD.TO-DB-c-4</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~403</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>115</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-CW_ROUND_115_20261015.md` @d514312c6d section 2 and 3 item 1 | **Rows:** IRPT_DASHBD-D2-W403-S<k> | **Decomp cell:** `DB-c-4` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 2) | **outcome_ref:** FWD-2, FWD-11 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-403`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~403/`. Never push. Counts, dates, instants, paths and words only in the repo, a row or your report; an account number, a client or household id, a name or a figure is never recorded. A raw `aws s3` or `aws s3api` listing in a shell call is denied by the repo's rail; do every S3 read from a short Python script (boto3, your own identity) kept in your private folder `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~403/` and not committed. A Python `import` of the checker's library is fine: `lib/opal_naming.py address()` and `lib/trading_calendar.py` give the tables' prefixes and the calendar.

**Why.** The CTO ruled that the Cottonwood `holdings_performance_daily` schedule needs a function to call, and that the read of what produced the gold up to 2026-09-25 comes first: a function that exists is adopted by Terraform import, otherwise a build cell makes one. He also asked that two oddities be read before anything is re-run: the first silver day 2026-06-09 has no gold, and the silver partitions 2026-09-23 to 2026-09-25 hold objects last written on 2026-09-28. This cell reads all three. It changes nothing.

**Facts the issuer measured at the cut (re-read each; state if it moved).** The Cottonwood gold table is `lib/opal_naming.py address("irpt","cottonwood","gold","holdings_performance_daily","date=2000-01-03")` with the partition tail cut (bucket `opal-data-cottonwood`); its manifest table is `holdings_performance_manifest`, one `manifest.json` per date. The gold partitions end at 2026-09-25 (75 partitions). The Black Diamond silver (`s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/date=D/`) holds 93 partitions, 2026-06-09 to 2026-10-13. The 2026-09-25 manifest's top-level keys include `source_pipeline`, `declaration`, `method`, `schema_version`, `calendar_source`, `prior_business_date` and `landed`. The producer code is `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` (the prior-day rule is in `_frame_for`, about lines 983 to 987) and its scheduled wrapper is `infra/aws/lambda/investor-reporting/holdings-performance/handler.py`.

**The cell (`DB-c-4`).**
1. **What produced the gold.** Read the newest gold manifest (2026-09-25) and one earlier manifest (any date at least 20 trading days before it that has gold): record the sorted top-level key names of each in `manifests.by_date` (a map from the ISO date to the list of key names). From the manifests' `source_pipeline`, `declaration` and `method` fields and from the repo, decide `producer.verdict`: `FUNCTION` (a Lambda wrote it: name the function and read it with ONE `get-function` of that named resource), `HOST_JOB` (the daily-runner host or another job wrote it: name the script, the dispatcher and the schedule that fires it), `AD_HOC` (a manual run: say what shows it), or `NOT_ESTABLISHED`. `producer.words` is the evidence in words (which manifest field, which repo file, which describe/get of one named resource, and what the last run was: the instant of the newest gold object, and for a Lambda its `LastModified` and, if you can read the log group's last event time with one describe of the one named log group, that instant); `producer.code_path` is the repo path of the code that produced it (required unless `NOT_ESTABLISHED`); `producer.claim` is `measured` only for what you read, otherwise `inferred`. Never enumerate AWS with a command the served graph answers (`comp-find --corpus aws --help`).
2. **2026-06-09.** `date_0609` = {`prior_trading_day` (the library calendar's `prev_trading_day` of 2026-06-09, ISO), `prior_day_silver_present` (a fresh LIST of the silver partitions: true or false), `rule_file` (the repo path), `rule_words` (what the prior-day rule in `_frame_for` does), `can_compute_words` (in words: whether the producer's own rule can compute 2026-06-09 from the silver that exists; do NOT run the producer), `claim`}.
3. **The rewrite.** For each of 2026-09-23, 2026-09-24 and 2026-09-25: `silver_latest_lm_utc` (the latest `LastModified` among the objects under that silver date, `YYYY-MM-DDTHH:MM:SSZ`), `silver_versions` (the count of object versions under that silver date prefix from `list_object_versions`; if the bucket is not versioned the count equals the number of objects), `gold_latest_lm_utc` (the latest `LastModified` among the objects under that gold date prefix, the daily table), and `gold_after_silver` (true when the gold instant is later than the silver instant). `rewrite.words` says what that shows: whether the gold was written after the last silver write, and whether a LIST can separate a rewrite from a first write here.
4. **Record** `PRODUCER_READ_R115.json` in your folder with exactly: `claim` ("measured"); `producer` {`verdict`, `words`, `code_path`, `claim`}; `manifests` {`by_date`}; `date_0609`; `rewrite` {`dates` {the three dates, each {`silver_latest_lm_utc`, `silver_versions`, `gold_latest_lm_utc`, `gold_after_silver`}}, `words`}; `basis_words` (words); `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `aws_writes` 0, `s3_reads` (integer)}; `pushed` false; `deployed` false.

<criterion id="DBC115-1-AC1" cell_refs="DB-c-4"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r115/p115_bcw.py" . DBC115-1-AC1</invocation><expect>DBC115-1-AC1 PASS</expect></criterion>
`DBC115-1-AC1` -- the record is complete; the verdict is in the enum and, unless NOT_ESTABLISHED, its code_path exists in the repo; each recorded manifest key set equals a fresh read of that manifest and two manifests are given; the prior trading day equals the library calendar's and its silver presence equals a fresh LIST; for each of the three dates the silver and gold instants equal fresh reads, the version count equals a fresh count, and `gold_after_silver` is the comparison of the two instants; no write is recorded. Base: FAIL (no record).

<expected_criteria>DBC115-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the checkers, every contract and every Terraform file.
- **Reads and writes.** Reads: repo files; S3 LIST, HEAD and version LIST under the Black Diamond silver prefix and the two Cottonwood gold table prefixes; a GET of the `manifest.json` objects of the manifest table only; ONE `get-function` and at most ONE describe of one named log group if a function is named; no other AWS call. Writes: the record in your folder and your private folder. No write to AWS, no invoke, no deploy, no push, no vendor call, no secret read, no read of any other firm's place.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A read you cannot make is named in `basis_words` with the error. Never run the producer.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W403-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~403/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-4.cottonwood-gold-producer-read-prior-day-input-and-rewrite-times.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 2, cell `DB-c-4`.
<owned_cells>DB-c-4</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC115-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~403/IRPT_DASHBD.TO-DB-c-4.cottonwood-gold-producer-read-prior-day-input-and-rewrite-times.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC115-1-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the producer verdict, its code path and its last run in one line; whether 2026-06-09's prior day exists in silver and what the rule means for it; for each of the three dates whether the gold was written after the silver; the number of S3 reads; row ids. No account number, client or household id, name or figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read record; nothing is wired, changed or deleted.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 LIST, HEAD, version LIST and manifest GET under the Cottonwood-scoped prefixes, and at most one get-function and one log-group describe of named resources; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the order READS what produced the gold and changes no schedule.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC115-1-AC1 FAILS at base (no record) and its fresh-read recount arms are exercised on the worker's record.
</preflight>
