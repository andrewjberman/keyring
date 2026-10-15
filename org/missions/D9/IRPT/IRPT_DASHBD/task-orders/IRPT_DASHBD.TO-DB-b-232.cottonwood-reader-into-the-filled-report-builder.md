# TO IRPT_DASHBD.TO-DB-b-232 -- the COTTONWOOD READER cut into the filled-report builder: an adapter that reads ONLY the Cottonwood gold prefixes and refuses any other firm's prefix, the contract's Cottonwood members (0.5.3), and two LOCAL QA runs (at the source's frontier and after it) in the private folder; a field with no Cottonwood source is the absent form, never zero and never partial; nothing is deployed

<to_id>IRPT_DASHBD.TO-DB-b-232</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~185</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>118</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ANALYSIS ANSWERING ROUND 113 section 2 ruling 3 and section 3 cell 3 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ANSWERING_ROUND_113_20261015.md` @5934ffcedc: "The Cottonwood reader is cut into the builder, per `~C2`'s ask (msg 7949). It reads only the Cottonwood gold prefixes and adds a negative test that refuses a foreign firm's prefix. Any member whose source is not yet written reads ABSENT with words, never zero") and `2.0.0_SA_COO~C2`'s ask `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~C2/ASK_D2_COTTONWOOD_MEMBER_SOURCES_R115.md` | **Rows:** IRPT_DASHBD-D2-W185-S<k> | **Decomp cell:** `DB-b-232` (decomposition section 116) | **outcome_ref:** FWD-2, FWD-11, FWD-21 (Andrew's P1: the performance reporting tab functional for all clients at all firms) | **depends_on:** `DB-b-230` (the same queue: this order starts after DB-b-230 is complete; the module `filled_report_values.py` and the contract 0.5.2 are its output)

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-185` (branch `wk-IRPT_DASHBD-185`, the same one as `DB-b-230`: you continue on it); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~185/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row or your report; a household or account id, a name and a figure that is a client value is never recorded outside the private folder. Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~185/`.

**Why.** No served or scheduled code reads a Cottonwood gold prefix, so a Cottonwood account page cannot show a return. The Cottonwood gold in bucket `opal-data-cottonwood` (addresses from `lib/opal_naming.py address("irpt", "cottonwood", "gold", <table>, "date=<D>", ...)`) holds four tables: `account_dim` (the household key: `household_id`; the account's `first_data_date` is not computed there), `account_return_daily` (3,325 partitions, 2013-04-03 to 2026-06-22: no input after 2026-06-22 until a Commonwealth delivery), `holdings_performance_daily` (ends 2026-09-25; no report member reads it) and `holdings_performance_manifest`. Cottonwood has NO gold for the account activity, lot or class tables that other report members read. `DB-b-230` built the firm-neutral gold script `filled_report_values.py` with its source-ends rule (a member whose figure needs a day after the newest partition of its source is the absent form SOURCE_BREAK naming the frontier date) and a loader `adapter_for(firm)` that loads `adapters/<firm>_report_reader.py` by file path. This cell is that file for Cottonwood, plus the contract's Cottonwood members, plus two private QA runs.

**The cell (`DB-b-232`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r118/p118_cottonwood.py` (your criteria; its docstring and clauses are the spec; it RECOMPUTES the Cottonwood frontier and grades both QA runs with DB-b-230's table clauses); the ask file above; `data/assets/scripts/gold/irpt_reporting/filled_report_values.py` (your own DB-b-230 output: the `FirmAdapter` interface, the 49 Financial adapter and `adapter_for`) and its tests; `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_account_dim.py` and `adapters/inflection_account_dim.py` (how a firm's gold is read and addressed); the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` at 0.5.2 (the 8 members that carry `firm_sources.inflection` show the entry form: `input, grain, table, field, fold, claim`); `org/standards/IRPT_DASHBD_ACCOUNT_DIM_CONTRACT.json`; `lib/opal_naming.py`.
2. **Write the reader** `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_report_reader.py` exposing `adapter()` (the interface of `filled_report_values.py`). It reads ONLY the Cottonwood irpt gold prefixes of the four tables above, every address from `address()` (never type a bucket or a prefix), and holds ONE guard function that REFUSES (raises) any address that is not one of those four Cottonwood tables' prefixes, called before every list and get. Households: the newest `account_dim` partition's `household_id` groups the accounts (an account with a null `household_id` belongs to no household). `account_return_daily` is read as the 49 Financial adapter reads it (the same column set and folds: this is the firm-generic table). Every member whose sibling table Cottonwood does not have (account activity, lots, class) is the absent form `NO_SOURCE_YET` with words naming the missing table; the 13 ABSENT-sourced members stay `NO_SOURCE_YET`; the model benchmark members stay firm-neutral as the builder fills them. The module names no other firm and holds no S3 or DynamoDB write.
3. **Tests** `data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_report_reader.py`: at least 8 tests, no network: at least TWO whose names start with `test_refuses_` (the guard refuses an address built from `address("irpt", "49financial", ...)` and one built from `address("irpt", "inflection", ...)`, and refuses a Cottonwood bucket with a table outside the four); the guard admits each of the four Cottonwood tables; households come from `household_id` and a null key belongs to none; a synthetic Cottonwood table whose frontier is before `as_of` gives SOURCE_BREAK naming the frontier for every account-return member and no figure; the missing sibling tables read NO_SOURCE_YET with words; `adapter_for("cottonwood")` returns this adapter; no write call in the module.
4. **The contract 0.5.3.** For EACH of the 36 members whose `source.contract` is the account-return contract add `firm_sources.cottonwood` = {`input` "account_return_daily", `grain` "account", `table` (the Cottonwood account_return_daily address form `s3://opal-data-cottonwood/irpt/cottonwood/gold/account_return_daily/date=<as_of>`; it must contain `cottonwood` and `account_return_daily`), `field` (the member's own field as its generic source names it), `fold` (the member's generic fold text, then the sentence: `The source ends at its newest partition date (the frontier); a window that needs a later day is absent, kind SOURCE_BREAK, words naming the frontier date.`), `claim` (words that begin with one of measured, inferred, held or absent)}; add a top-level `firm_households` = {`cottonwood`: {`table` "account_dim", `field` "household_id", `words`}}; add a top-level `unread_inputs` = a list holding {`table` "holdings_performance_daily", `reason` (words: no report member reads it)} and the same for `holdings_performance_manifest`; set `contract_version` to "0.5.3"; append to `lineage` the entry {`contract_version` "0.5.2", `sha256` (the sha256 of the COMMITTED 0.5.2 bytes: `git show HEAD:org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` hashed as bytes, taken BEFORE you edit), `reason` words}. Change NOTHING else: `members` (ids and every other key), `document`, `gold_table`, the 8 `firm_sources.inflection` entries stay byte-for-byte.
5. **Two QA runs, LOCAL, in the private folder:** run 1 with `as_of` equal to the Cottonwood frontier (the newest `account_return_daily` partition date, found by listing the `date=` prefixes: 2026-06-22) and run 2 with `as_of` 2026-10-13, each over at most 25 households (the lowest sha256 of `household_ref`), all members, written by the `filled_report_values.py` entry for `--firm cottonwood` to `cottonwood_run1.parquet` and `cottonwood_run2.parquet` in your private folder. Run 2 must hold every account-return member as the absent form SOURCE_BREAK naming the frontier date and no figure for any of them; run 1 must hold measured account-return members.
6. **Record** `RD_COTTONWOOD_QA_R118.json` in your folder, counts, dates and words only, with EXACTLY these fields: `firm` ("cottonwood"), `frontier_date` (ISO, the newest partition date you listed), `partitions_listed` (the count of `date=` prefixes you listed), `households_source` (words), `runs` (a list of exactly 2: run 1 then run 2, each {`as_of`, `households` (1 to 100), `rows`, `measured_rows`, `text_rows`, `absent_rows` (the three add to `rows`), `private_parquet` {`path` (under your private folder), `sha256`, `rows`}}), `analysis` {`file` "data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_report_reader.py", `sha256`, `tracked` true}, `reads` {`s3_reads` (integer), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, `claim` (one of measured, inferred, held, absent), `files_in_repo` false, `served_values_changed` false, `pushed` false, `deployed` false. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256` or `vintage` field; no household or account id; no client value.

<criterion id="DB118-3-AC1" cell_refs="DB-b-232"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r118/p118_cottonwood.py" . DB118-3-AC1</invocation><expect>DB118-3-AC1 PASS</expect></criterion>
`DB118-3-AC1` -- the reader and its test file are tracked; the test file passes with at least 8 tests including at least two `test_refuses_*` negatives (the checker runs `pytest` on it); the reader uses `address(`, types no bucket, names no other firm (no 49 Financial, no Inflection, no shared assets bucket) and holds no S3 or DynamoDB write. Base: FAIL (no reader).
<criterion id="DB118-3-AC2" cell_refs="DB-b-232"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r118/p118_cottonwood.py" . DB118-3-AC2</invocation><expect>DB118-3-AC2 PASS</expect></criterion>
`DB118-3-AC2` -- the contract reads 0.5.3; all 36 account-return members carry a complete `firm_sources.cottonwood` (the six keys, the Cottonwood account_return_daily address form, a fold that states the source-ends rule); `firm_households.cottonwood` names `account_dim.household_id`; `unread_inputs` records `holdings_performance_daily` with a reason; the 117 member ids, `gold_table` and the 8 Inflection sources are unchanged (hashed); and the lineage ends with the 0.5.2 entry whose sha256 is the committed 0.5.2 bytes' hash (the checker finds those bytes in git). Base: FAIL (version 0.5.2).
<criterion id="DB118-3-AC3" cell_refs="DB-b-232"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r118/p118_cottonwood.py" . DB118-3-AC3</invocation><expect>DB118-3-AC3 PASS</expect></criterion>
`DB118-3-AC3` -- both private QA parquets pass DB-b-230's table clauses for firm cottonwood; the record's frontier date and partition count equal the checker's own LIST of the Cottonwood `account_return_daily` prefixes (read by the checker, LIST only); run 1 is at the frontier and holds measured account-return members; run 2 is after the frontier and holds EVERY account-return member as the absent form SOURCE_BREAK whose words name the frontier date, with no figure; the record has exactly the form of step 6, its hashes and counts equal the files', and its flags are false. Base: FAIL (no record).

<expected_criteria>DB118-3-AC1,DB118-3-AC2,DB118-3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `filled_report_values.py` and its tests (`DB-b-230`'s; if the reader needs a change there it is a row and a stop, never an edit), every other adapter and test, `sources.json`, the producers, every other contract, `lib/`, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the Cottonwood irpt gold prefixes of the four tables above and nothing else, every one derived by `lib/opal_naming.py address()`, plus the served model series object `filled_report_values.py` already reads. Writes: the repo files of the grant and the private folder named above. No put, copy or delete of any kind, no deploy, no schedule, no push, no vendor call, no secret read, no read of another firm's place, no Terraform.
- **Client data.** The Cottonwood gold and the QA parquets are client data: counts, hashes and words only in the repo, a row or your report; never a household or account id.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a Cottonwood source cannot be read, record it `absent` with the refusal named, file a BLOCKING row with counts and stop on that point; an unreadable source is never a zero. A column the Cottonwood gold lacks is a row (the producer's surface is `2.0.0_SA_COO~C2`'s, never yours). An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W185-S<k>` (the next free number: read the file's last id first), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_report_reader.py
data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_report_reader.py
org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~185/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-232.cottonwood-reader-into-the-filled-report-builder.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 116 (round 118), cell `DB-b-232`.
<owned_cells>DB-b-232</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB118-3-AC1, DB118-3-AC2, DB118-3-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~185/IRPT_DASHBD.TO-DB-b-232.cottonwood-reader-into-the-filled-report-builder.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB118-3-AC1` (and AC2, AC3) BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the Cottonwood frontier date and the partitions listed; for each run the households, rows and the measured, text and absent counts; the test count and the names of the `test_refuses_*` tests; the contract version and the lineage hash; which sibling tables Cottonwood lacks; reads and writes. Counts, dates and words only: no household or account id and no client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a new adapter file, its tests, a contract text and private runs in a branch; nothing is wired, scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the S3 reads are GET and LIST of the Cottonwood irpt gold prefixes already read by the Cottonwood adapters and the round-114 reader read (DB-c-3).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the Cottonwood producer schedule is workstream B-CW's.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB118-3-AC1 to AC3 FAIL at base (no reader, version 0.5.2, no record) and the checker's clauses are exercised by its self-test (a green run arm, ten red run arms and four red module arms); the checker's frontier recount was dry-run by the issuer against the real gold (2026-06-22, 3,325 partitions).
lane: the <paths> block IS the grant.
</preflight>
