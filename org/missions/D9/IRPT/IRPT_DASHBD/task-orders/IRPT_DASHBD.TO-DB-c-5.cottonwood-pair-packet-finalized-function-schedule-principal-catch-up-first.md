# TO IRPT_DASHBD.TO-DB-c-5 -- the PAIR PACKET, finalized on `DB-c-4`: the function (adopted or to build), the schedule at 08:15 New York with the input-frontier check, the principal's write-only grants on the two gold tables, the catch-up first and the schedule ENABLED only after its after-read, both branches, rollback per key, the CTO's questions; a packet; nothing is applied

<to_id>IRPT_DASHBD.TO-DB-c-5</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~403</issued_to>
<issued_by>2.0.0_SA_COO~C2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>115</round>
<workstream>B-CW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-CW_ROUND_115_20261015.md` @d514312c6d section 2 (the pair) and 3 item 2 | **Rows:** IRPT_DASHBD-D2-W403-S<k> | **Decomp cell:** `DB-c-5` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md` section 2) | **outcome_ref:** FWD-2, FWD-11 | **depends_on:** `DB-c-4` (this worker's previous order; its record `PRODUCER_READ_R115.json` is your input, and the order is handed to you only after it is terminal).

---

## WORKER FACE

Your workspace worktree and folder are those of your previous order (`deliverables/0.9.0_WK_IRPT_DASHBD~403/`). Never push. Counts, dates, names, keys and words only in the repo, a row or your report; an account number, a client or household id, a name or a figure is never recorded. Every S3 read is from a short Python script (boto3, LIST and HEAD only) kept in your private folder.

**Why.** The CTO accepted the fire time 08:15 New York and ruled the shape of the one never-widen pair: it covers the function (adopted if one exists, built if not), the schedule, the principal's grants (write only the two gold tables' prefixes), and the catch-up, with the keys read absent first; the schedule starts ENABLED only after the catch-up's after-read, so the first scheduled fire lands on a gold frontier at T-1; and the producer, at fire time, checks its input: if T-1's silver partition is absent it HOLDS, logs the absence and writes nothing, never stamping a stale day. This cell rewrites the round-114 packet (`deliverables/0.9.0_WK_IRPT_DASHBD~401/NEVER_WIDEN_PACKET_DB-c-2_R114.md`) to that shape on `DB-c-4`'s read. It applies nothing.

**The cell (`DB-c-5`).**
1. **Inputs.** Read your `PRODUCER_READ_R115.json`, the round-114 packet and its facts record `deliverables/0.9.0_WK_IRPT_DASHBD~401/PACKET_FACTS_R114.json`, and the 49 Financial model files `infra/aws/terraform/investor-reporting/holdings-performance/schedule.tf` and `iam.tf` and `infra/aws/lambda/investor-reporting/holdings-performance/handler.py`.
2. **Names.** Schedule and principal names come from `lib/opal_naming.py name(...)`; record the exact arguments (`schedule_builder_args`, `principal_builder_args`) and the builder's output or its refusal text (`<key>_builder_refusal`), exactly as the round-114 facts record does. The round-114 names (`irpt-cot-holdings-performance-daily`, `irpt-cot-holdings-performance-role`) are the expected result; confirm by calling the builder.
3. **The function.** From `DB-c-4`'s verdict (the issuer read it as `AD_HOC`, claim inferred: no function or schedule names the Cottonwood source, and the gold manifests carry schema 1.1 while HEAD emits 1.2, so a HEAD-built function would write 1.2 beside 1.1; the packet states that and asks the CTO's half to rule it, row `IRPT_DASHBD-D2-W403-S2`): `function.mode` is `ADOPT` when the verdict is `FUNCTION` (then `function.name` is that function's name; the Terraform act is an import) and `BUILD` otherwise (then say in the packet what the build cell must make: the function, its package and its Terraform, modelled on the 49 Financial one; `function.name` may be the builder's name or null with the refusal). `function.words` says what you read.
4. **The catch-up.** `catch_up.as_of_date` is the newest silver partition date at the moment you write (a fresh LIST); `catch_up.dates` is every silver partition date up to and including it that is a trading day per the library calendar and has no gold partition in `holdings_performance_daily`, ascending, MINUS `catch_up.excluded`: a list of `{date, reason}` for each such date whose prior trading day has no silver partition (the producer's own rule has no base for it; `DB-c-4` read that 2026-06-09 is one: its prior day 2026-06-08 is not in silver and the source declares no gap link). An excluded date gets no key and is listed in the packet's questions; `keys_written` is, per such date, `address("irpt","cottonwood","gold","holdings_performance_daily","date=D","data.parquet")` and `address("irpt","cottonwood","gold","holdings_performance_manifest","date=D","data.parquet")` and `...,"manifest.json")`, in order, `keys_written.dates` the same dates, `keys_written.count` three per date. A fresh LIST must find none of them present.
5. **The grants.** `principal_write_prefixes` is exactly the two gold tables' prefixes, each as `s3://<bucket>/<prefix>` where the bucket and prefix come from `address(...)` for `holdings_performance_daily` and `holdings_performance_manifest` with the partition tail cut (the principal can write nothing else); `principal_read_prefixes` is exactly two prefixes: `"s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/"` and the daily gold table's prefix from `address(...)` (a list-and-read grant on the principal's OWN daily table, because the scheduled path lists it to find the newest landed day, as the 49 Financial principal's `ListTheOwnDailyGoldPrefixForCatchUp` statement does; worker row `IRPT_DASHBD-D2-W403-S4`, ruled by the issuer).
6. **Packet** `NEVER_WIDEN_PACKET_DB-c-5_R115.md` (5,000 characters or more) with these `## ` headings, in this order: `## Change set` (the desired schedule entry as text and a code block modelled on the 49 Financial one: `cron(15 8 ? * MON-FRI *)` in `America/New_York`, the trigger input naming source `blackdiamond_z09`, the input-frontier hold written as the function's behaviour: absent T-1 silver means hold, log, write nothing; the principal with the exact prefixes; every name from the builder); `## Function` (adopt or build, from `DB-c-4`, with the evidence); `## Catch-up first` (the order of acts: the pair signed; the function adopted or built; the principal created; the catch-up run one date at a time through the handler event {date, source}, stopping at the first non-zero return; the AFTER-READ that the dates and objects exist and the frontier is T-1; ONLY THEN the schedule created ENABLED, so the first scheduled fire lands on a gold frontier at T-1); `## Keys written` (the as-of date, the count, the dates, three objects per date, the statement that no other key moves, and that a fresh LIST found none present); `## Both branches` (what the portal path reads if the run succeeds; what it reads if the run fails midway: which dates exist, which do not; what a held fire does); `## Rollback` (per key, and for the schedule, the principal and the function); `## Questions for the CTO's half` (at least: who applies, which AE lane `0.0.0_AB_MSTR~DELL2` names; the principal's grants against the bucket policy, which is not read here; whether 2026-06-09 and the three rewritten partitions, per `DB-c-4`, change the catch-up set; that both halves sign before any apply; the Andrew word the rollback deletes need); `## Not in this packet` (what you did not establish). The packet states it is UNSIGNED and carries no signature.
7. **Facts record** `PACKET_FACTS_R115.json` with exactly: `claim` ("measured"); `schedule_name`, `schedule_builder_args`, `schedule_builder_refusal`; `principal_name`, `principal_builder_args`, `principal_builder_refusal`; `fire_time_et` ("08:15"); `frontier_check` (true); `start_state` ("DISABLED_UNTIL_CATCHUP_AFTER_READ"); `function` {`mode`, `name`, `words`}; `principal_write_prefixes`; `principal_read_prefixes`; `catch_up` {`as_of_date`, `dates`, `excluded`}; `keys_written` {`dates`, `keys`, `count`}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `aws_writes` 0, `terraform_apply` 0}; `pushed` false; `deployed` false.

<criterion id="DBC115-2-AC1" cell_refs="DB-c-5"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/checks/r115/p115_bcw.py" . DBC115-2-AC1</invocation><expect>DBC115-2-AC1 PASS</expect></criterion>
`DBC115-2-AC1` -- the facts record is complete; both names equal a fresh builder call (or the recorded refusal is the builder's); the fire time is 08:15 with the frontier check true and the start state disabled until the catch-up's after-read; a FUNCTION verdict is adopted, not rebuilt; the principal's write prefixes are exactly the two gold tables and its read prefixes are exactly the Black Diamond silver prefix and the daily gold table's prefix; the catch-up dates equal silver trading days to the as-of date minus gold minus the excluded dates (each excluded date has no prior-day silver partition and a reason), and the keys equal the builder's addresses, three per date; the packet holds the eight headings in order, is 5,000 characters or more, says it is unsigned and claims no signature; no write is recorded. Base: FAIL (no record).

<expected_criteria>DBC115-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the checkers, every contract, every Terraform file and every IAM file: the desired entries are TEXT in the packet.
- **Reads and writes.** Reads: repo files; S3 LIST and HEAD under the Cottonwood gold prefixes and the Black Diamond silver prefix. Writes: the packet and the facts record in your folder. No write to AWS, no Terraform plan or apply, no deploy, no push, no vendor call, no secret read.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A section you cannot fill is written as "not established" with the reason.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W403-S<k>` (continue after your last), with the real current UTC time; append as BYTES. Commit with `.tools/safe-commit.sh`. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~403/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-c-5.cottonwood-pair-packet-finalized-function-schedule-principal-catch-up-first.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-CW.md</decomp_doc> section 2, cell `DB-c-5`.
<owned_cells>DB-c-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC115-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~403/IRPT_DASHBD.TO-DB-c-5.cottonwood-pair-packet-finalized-function-schedule-principal-catch-up-first.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC115-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the two names (or refusals); the function mode and name; the as-of date, the catch-up count and keys; whether any key already exists; the packet's length; the number of S3 reads; row ids. No account number, client or household id, name or figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a packet; no resource is changed, wired or deleted.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the principal is described in text; no grant is created. The CTO's half reads the described grants.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the order DESCRIBES a schedule; none is created or changed.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBC115-2-AC1 FAILS at base (no record) and its builder-recompute arms are exercised on the worker's record.
</preflight>
