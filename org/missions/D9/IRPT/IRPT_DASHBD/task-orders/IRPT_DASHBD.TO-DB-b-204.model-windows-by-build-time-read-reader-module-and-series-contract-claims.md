# TO IRPT_DASHBD.TO-DB-b-204 -- the MODEL WINDOWS BY BUILD-TIME READ: the DB-b-199 producer is reworked into a reader of the served model series (renamed, not `market_topic_daily`), the compounded windows carry `source` (key and VersionId) and `data_as_of`, the series contract carries those claim fields, the retired module, tests and contract are removed; nothing is written

<to_id>IRPT_DASHBD.TO-DB-b-204</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~168</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>105</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-105 ANALYSIS section 2 cell 3, on the ruling `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULING_20261014_115xZ_IRPT_DASHBD_MODEL_SERIES_TABLE_AND_HOME.md` ("The raw series gets no gold table and no firm home. The builder reads the served portal-v2 object at build time and lands only the per-household compounded windows in the firm's own gold. The DB-b-199 packet is RETIRED.") | **Rows:** IRPT_DASHBD-D2-W168-S<k> | **Decomp cell:** `DB-b-204` (decomposition section 107) | **outcome_ref:** FWD-21 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-168` (branch `wk-IRPT_DASHBD-168`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~168/`. Never push; never commit the workspace `portal` gitlink.

**Why.** Round 104's cell `DB-b-199` built a producer that would have written the raw Opal model daily series into a firm's gold under the table name `market_topic_daily` (616 date partitions, 1,232 objects). The CTO ruled that wrong on four counts: `market_topic_daily` is the FWD-6 topic table (day by rank: phrase, score, sentiment, source kind), and return columns in it break same grain and one intent; the series is firm-neutral, so a copy under one firm's gold fails tenancy and the cross-firm rule, and a copy per firm duplicates an output path; the estate already serves the series at `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json`; so the builder READS the served object at build time and only the per-household compounded windows (QTD, YTD, 12 months, since the household's first day, cumulative) land in the firm's own gold, beside the household's series, each value carrying `source` (the served key and its VersionId) and `data_as_of` as claim fields. Nothing is applied this round.

**The cell (`DB-b-204`).**
1. **Read first.** The ruling (the file above, all of it), the producer you rework `data/assets/scripts/gold/irpt_reporting/adapters/model_series_market_topic_daily.py` and its tests `data/assets/scripts/gold/irpt_reporting/tests/test_model_series_market_topic_daily.py`, its contract `org/standards/IRPT_DASHBD_MARKET_TOPIC_DAILY_CONTRACT.json` (the three to remove), the previous packet `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~164/MODEL_SERIES_GOLD_PACKET.md` and the rows `IRPT_DASHBD-D2-W164-S1` to `S3` in `org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md`, the existing compounding code you move here: `model_series`, `model_lo`, `compound`, `bench_value` in `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~159/build_sample.py` (lines about 232 to 300; read-only; its rules are the rules), the series contract `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` (version 0.1.0), and the issuer's check file `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r105/p105_round105.py` (`check_reader` is your criterion: read every clause; you may run its `--selftest`).
2. **The module.** `git mv` the producer to `data/assets/scripts/gold/irpt_reporting/adapters/model_series_windows.py` and rework it (the old name is retired; nothing named `market_topic_daily` remains in the module, its tests or its contract). It exposes exactly these three public functions, with these behaviours (the checker imports the module and calls them):
   - `read_served_series(reader)` returns `(series, claim)`: `reader` is an object with ONE method `get_object(bucket, key)` that returns `(bytes, version_id)`; the module GETs `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json` through it (a reader class with NO put, copy or delete method, as `~159`'s `Reader`, plus the version id from `get_object`'s `VersionId`), reads the `index_benchmark_return` column for the four model codes (UST, ST, INT, LT, which fill the stems `benchmark_ultra_short_term`, `benchmark_short_term`, `benchmark_intermediate_term`, `benchmark_long_term`), keeps trading days of `lib/trading_calendar.py`, and returns `series` = `{stem: [(datetime.date, daily decimal return), ...] sorted by date}` and `claim` = `source_claim(key, version_id, data_as_of)` with `data_as_of` the last date of the series read (the live vintage: W164-S2 found it newer than the cited one).
   - `windows_from_series(series, as_of, household_first_day)` returns `{stem: {"qtd": x, "ytd": x, "last_12_months": x, "since_inception": x}}`, `as_of` a `datetime.date`, `household_first_day` an ISO string or a date; each `x` is the CUMULATIVE PERCENT in percent points rounded to 1 decimal (the product of (1 + daily return) over the window's trading days, minus 1, times 100), or `None` when the series does not open on the window's first day or lacks a return on any trading day of the window (never interpolated, never zero). The windows open as `~159`'s `model_lo` defines them: QTD on the first calendar day of `as_of`'s quarter, YTD on January 1, last 12 months on the day after the date one calendar year before `as_of`, since inception on the day after `household_first_day`.
   - `source_claim(key, version_id, data_as_of)` returns `{"source": <a string that contains both the key and the version id>, "data_as_of": <the ISO date>}`.
   The module writes NOTHING and has no upload path; no firm is named in it (it is firm-neutral, as `~159`'s `model_series`).
3. **Tests.** `git mv` the old test file to `data/assets/scripts/gold/irpt_reporting/tests/test_model_series_windows.py` and rework it: at least 4 offline tests with a synthetic served document and a fake reader (the windows equal an independent compounding; a gap day gives `None`; the claim carries the key and the version id; the reader refuses a document that lacks a model code), run with `python -I -m pytest -q <file>`; ONE temporary mutant (for example drop the gap check) that a test catches, then reverted.
4. **Series contract.** Edit `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` (yours in this cell; no other file under `org/standards/`): bump `contract_version` above 0.1.0 (0.2.0), add a `lineage` list holding the 0.1.0 bytes (`{"contract_version": "0.1.0", "sha256": "40cef6203cbfa109cae26209a9d241b82d6b1071f316c9f71f39d16913853e94", ...}`), and add a `model_windows` section: the four stems by the four windows (cumulative percent points, one decimal, `null` never written as a figure), the claim fields `source` (the served key and VersionId) and `data_as_of` on every value, the rule that the windows land in the firm's OWN gold beside the household's series (never the raw series, never a general table), and that the apply is a later round under a never-widen pair. The existing 0.1.0 content stays unchanged. Valid JSON, ASCII. `git rm` `org/standards/IRPT_DASHBD_MARKET_TOPIC_DAILY_CONTRACT.json`.
5. **One live read.** Run the module's reader ONCE against the served object (one S3 GET of that one key; nothing else; read-only) from a small script of your own in your folder, and record: the VersionId, `data_as_of`, and `members_filled` = how many of the performance report contract's 32 benchmark members (`org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json`: the members whose id ends in one of the four stems, under `pvs.<window>.` and `avs.<window>.`) would fill for the household window opened by the contract's own sample (use the `as_of` and `first_data_date` of `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~159/HOUSEHOLD_SAMPLE.json`, read-only client data: dates only). Print that count in your report. The series itself is NOT copied anywhere.
6. **Record** `MODEL_WINDOWS_READER.json` in your folder with exactly: `module` {`file`, `sha256`, `tracked` true}; `tests` {`file`, `passed`, `failed` 0, `mutant_failed` true}; `live_read` {`version_id`, `data_as_of` (ISO), `members_total` 32, `members_filled`}; `writes_in_this_cell` false; `no_other_key_moves` true; `note` (one plain sentence: what lands where, and that the apply is a later round); `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, paths, hashes and words only: no run of 8 or more digits except in a `sha256` value or a `path`, `file`, `key` or `commit` field.

<criterion id="DB105-3-AC1" cell_refs="DB-b-204"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r105/p105_round105.py" . DB105-3-AC1</invocation><expect>DB105-3-AC1 PASS</expect></criterion>
`DB105-3-AC1` -- the retired module, test file and contract are gone; the new module is a tracked file hashed as recorded; its test file has 4 or more passing tests and passes when the checker runs it, with a failing mutant; the series contract is above 0.1.0 with the 0.1.0 bytes in its lineage and carries `source` and `data_as_of`; the checker calls `windows_from_series` on a synthetic four-stem series and the result equals its own independent compounding for every stem and window, a series missing a trading day inside the windows gives `None` for each such window, and `source_claim` returns the key and the version id and the ISO date; the live read records a version id, an ISO `data_as_of`, 32 members and how many fill; nothing is written; no write, push or deploy. Base: FAIL (no record).

<expected_criteria>DB105-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `~159/build_sample.py`, every other contract and every portal file.
- **Reads and writes.** The one live read of step 5 is one S3 GET of the served object and nothing else; no write to AWS of any kind, no deploy, no push, no vendor call, no secret read. A denial is recorded verbatim, not retried by another route. The series is never copied into the repo, a row or your report.
- **Client data.** The sample of step 5 is client data: dates only.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W168-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~168/
data/assets/scripts/gold/irpt_reporting/adapters/model_series_windows.py
data/assets/scripts/gold/irpt_reporting/adapters/model_series_market_topic_daily.py
data/assets/scripts/gold/irpt_reporting/tests/test_model_series_windows.py
data/assets/scripts/gold/irpt_reporting/tests/test_model_series_market_topic_daily.py
org/standards/IRPT_DASHBD_SERIES_CONTRACT.json
org/standards/IRPT_DASHBD_MARKET_TOPIC_DAILY_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-204.model-windows-by-build-time-read-reader-module-and-series-contract-claims.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 107 (round 105), cell `DB-b-204`.
<owned_cells>DB-b-204</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB105-3-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~168/IRPT_DASHBD.TO-DB-b-204.model-windows-by-build-time-read-reader-module-and-series-contract-claims.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB105-3-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the module's three functions and what each returns; the series contract change (version, lineage, the model_windows section); the live read (VersionId, `data_as_of`, how many of the 32 benchmark members fill, and which windows are `None` if any); the files removed; row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a module rework, a contract edit and one read-only GET; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: one read-only S3 GET of an object the `~159` builder already reads; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB105-3-AC1 FAILS at base (no record) and its compounding arms are exercised by the checker's own self-test (green and red).
lane: the <paths> block IS the grant.
</preflight>
