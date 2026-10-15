# TO IRPT_DASHBD.TO-DB-i-2 -- the TWO MISSING Orion `fact_positions` DAYS (2026-07-01 and 2026-09-28): which Orion layers hold them, whether each is a trading day, how many accounts a bridge across the gap would touch and how many of those had an external flow in the gap, and the producer and schedule that write the Orion silver; a read, counts and words only; nothing written

<to_id>IRPT_DASHBD.TO-DB-i-2</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~302</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>114</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (B-IN is this workstream); row `IRPT_DASHBD-D2-W174-S2` | **Rows:** IRPT_DASHBD-D2-W302-S<k> | **Decomp cell:** `DB-i-2` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md` section 1) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-302`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~302/`. Never push. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, hashes and words only in the repo, a row or your report; an account number, a household or client id, a name or a figure is never recorded. Your private folder, if you need one, is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~302/`.

**Why.** Round 109's tie-out read found that Orion's `fact_positions` silver has NO partition for two NYSE trading days, 2026-07-01 and 2026-09-28 (row `IRPT_DASHBD-D2-W174-S2`, BLOCKING). A daily time-weighted return needs an end-of-day value for every trading day of its window, so the year-to-date, last-12-month and since-inception windows of every Inflection household read "not comparable" and the account pages cannot show those windows. Before the CTO rules what to do (re-pull the day, bridge across it, or leave the windows absent), he needs four facts. This cell reads them. It repairs nothing and bridges nothing.

**The cell (`DB-i-2`).**
1. **Layers.** List the Orion silver tables under `s3://opal-data-assets/orion/inflection/silver/` (the common prefixes, through the reader). For EACH table and for EACH of the two dates, record whether the partition `date=<ISO date>` exists. Then look under the rest of the granted Orion prefix `s3://opal-data-assets/orion/inflection/` for any other layer (for example a bronze or raw prefix next to `silver/`): list its top-level prefixes, and for every layer that carries date-keyed objects or partitions, record for each of the two dates how many objects exist (a LIST count; open nothing). Name each layer you checked and the prefix you listed in the record (`bronze_checks`).
2. **Calendar.** For each date record whether it is a trading day per `lib/trading_calendar.py` `is_trading_day`.
3. **Neighbours.** For `fact_positions` record the partition dates immediately before and after each missing date (the nearest existing partitions), so the gap's width in calendar days is known.
4. **Bridge exposure (counts only).** Use the private cache `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~174/work/positions_daily_cache.parquet` (one row per account per positions partition day; columns `acc`, `date` ISO string, `v_all`, others) and the newest `fact_transactions` partition read through the reader (the reader only). For each missing date `G`, with `P` the last partition day before it and `N` the first partition day after it: `accounts_valued_before` is the number of accounts with a `v_all` row on `P` that is positive; `accounts_with_external_flow_in_gap` is how many of those have at least one EXTERNAL flow dated after `P` and up to and including `N`. External flows are those the module `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_return_daily.py` classifies EXTERNAL (import and call its `flows_of(frame, accounts)`; READ-ONLY; do not re-derive the classification). A count of accounts only; no account id and no flow figure is recorded.
5. **Owner.** Find the producer that writes the Orion silver `fact_positions` table (use `comp-estate --resource orion` or `comp-pipescript io <script>`, and read the file): record the repo path of the producer (`owner.producer_file`), its schedule or trigger in words (`owner.schedule_words`: what fires it, how often, which days, DESIRED versus what the live trigger reads if you can read the live trigger with a describe/get of one resource), and in words anything the repo shows about why those two days were never written (`owner.unrecorded_cause_words`: say "none found" if the repo shows nothing; never guess). An AWS read is a describe or get of one named resource, never an enumeration the served graph holds.
6. **Record** `DATE_GAP_READ_R114.json` in your folder with exactly: `dates` {`2026-07-01` and `2026-09-28`, each {`trading_day` (true or false), `partition_present` {one boolean per silver table you listed, keyed by the table name}, `bronze_present` {one integer per `bronze_checks` entry, the object count}, `nearest_before`, `nearest_after` (the nearest existing `fact_positions` partition dates, ISO strings), `claim` "measured"}}; `silver_tables` (the list of Orion silver table names you found, sorted; a fresh LIST by the checker must equal it); `bronze_checks` (a list of {`prefix`, `layer_words`}); `bridge` {`claim` "inferred" (the flow classification is the round-109 module's), and for each date {`accounts_valued_before`, `accounts_with_external_flow_in_gap`}}; `owner` {`producer_file`, `schedule_words`, `unrecorded_cause_words`}; `basis_words` (words: what you listed, what you counted, what you could not read and why; no figure); `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `s3_reads` (integer: the reader's `reads` count plus any other S3 call you made)}; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, paths, hashes and words only: no account or household id, no run of 8 or more digits except in a `sha256` value or a `path`, `file`, `key`, `prefix` or `where` field.

<criterion id="DBI114-2-AC1" cell_refs="DB-i-2"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r114/p114_bin.py" . DBI114-2-AC1</invocation><expect>DBI114-2-AC1 PASS</expect></criterion>
`DBI114-2-AC1` -- the record is complete and carries no identifier and no write is recorded; the checker re-LISTs the Orion silver prefix and finds `silver_tables` equal to it; for each of the two dates and each table a fresh LIST finds the recorded partition presence true or false exactly; `trading_day` equals `lib/trading_calendar.is_trading_day`; the bridge counts are integers with the flow count not above the valued count; the owner's producer file is a repo file and the schedule words are present; nothing is written to AWS; no push or deploy. Base: FAIL (no record).

<expected_criteria>DBI114-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the module, the reader, the cache, every contract and every issuer check.
- **Reads and writes.** Reads: repo files; the private cache named above; S3 LIST and GET under `s3://opal-data-assets/orion/inflection/` ONLY through the round-108 reader `InflectionSilverReader` (`data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_dim.py`, GET-only, grant-enforcing; a LIST of a non-silver layer under the same granted prefix may use the reader's client through its `_api()` with `list_objects_v2`, under the granted prefix only); a describe or get of ONE named AWS resource for the schedule. Writes: the record in your folder and your private folder. No write to AWS of any kind, no deploy, no push, no vendor call, no secret read, no read of any other firm's place.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A layer you cannot list is named in `basis_words` with the error; a producer you cannot find is `producer_file` of the nearest repo file that names the Orion silver and a row saying so. Never re-pull, back-fill or write a day.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W302-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~302/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-2.inflection-two-missing-positions-days-layers-bridge-exposure-owner.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 1, cell `DB-i-2`.
<owned_cells>DB-i-2</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI114-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~302/IRPT_DASHBD.TO-DB-i-2.inflection-two-missing-positions-days-layers-bridge-exposure-owner.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI114-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; per date whether it is a trading day and in which layers it exists (names and counts); the nearest partitions before and after; the two bridge counts per date; the producer file and the schedule in one line; the number of S3 reads; row ids. No account number, household or client id, name or figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read record; nothing is read by served code, wired or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 LIST and GET of the Inflection-scoped Orion prefix; one describe or get of a named schedule resource; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: the order READS a producer's trigger and changes none.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI114-2-AC1 FAILS at base (no record) and the checker's LIST-recount arms are exercised on the worker's record.
</preflight>
