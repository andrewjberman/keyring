# TO IRPT_DASHBD.TO-DB-b-233 -- CONTRACT 0.5.4 AND THE MODULE TOGETHER (round 119, workstream B-49F): the ten activity and net-gain members print the SAME folds as the value-summary members DB-b-202 ruled they equal; the contract says so (member sources, equivalences, version 0.5.4) and `filled_report_values.py` fills them from their counterparts, so no member is absent for a reason the contract created; one private QA run for 49 Financial; nothing is deployed

<to_id>IRPT_DASHBD.TO-DB-b-233</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~187</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>119</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 119 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-119 ANALYSIS (B-49F) section 2 ruling 1 and section 3 cell 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_119_20261015.md` @d856067e84: "The contract repair goes FIRST: contract 0.5.4. The `act.*` and `hold.net_gain_*` members print the same value-summary folds that DB-b-202 ruled. No table is scheduled or cloud-written until 0.5.4 lands. Today 527 rows are absent for a reason the contract created, not the data. D2-S56 is its ARMED carrier") | **Rows:** IRPT_DASHBD-D2-W187-S<k> | **Decomp cell:** `DB-b-233` (decomposition section 117) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-187` (branch `wk-IRPT_DASHBD-187`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~187/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row or your report; never a household or account id or a client value. Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~187/` (create it if absent).

**Why.** Round 105 (`TO-DB-b-202`, part d) ruled that the report's figures agree across tables: the last-12-month figures of the activity members are the SAME folds the value summaries print, and the holdings overview's net gains are the value summaries' net gains. The sample builder printed them that way; the contract text kept sourcing them to the account activity table, and round 118's gold-table module followed the contract text. Result: in the QA table all 402 `act.*` rows and all 125 `hold.net_gain_*` rows of 25 households are absent (INSUFFICIENT_HISTORY, the activity table holds 5 trading days), where the value-summary members beside them are measured. This cell repairs the contract and the module together. Nothing is scheduled, written to the cloud or deployed.

**The ten pairs** (the member that must equal it, then the value-summary member it equals): `act.beginning_value.household` = `pvs.last_12_months.beginning_value`; `act.beginning_value.account` = `avs.last_12_months.beginning_value`; `act.net_gain.household` = `pvs.last_12_months.net_gain`; `act.net_gain.account` = `avs.last_12_months.net_gain`; `act.ending_value.household` = `pvs.last_12_months.ending_value`; `act.ending_value.account` = `avs.last_12_months.ending_value`; `hold.net_gain_last_12_months` = `pvs.last_12_months.net_gain`; `hold.net_gain_ytd` = `pvs.ytd.net_gain`; `hold.net_gain_qtd` = `pvs.qtd.net_gain`; `hold.net_gain_since_inception` = `pvs.since_inception.net_gain`.

**The cell (`DB-b-233`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r119/p119_actequiv.py` (the pairs, every clause, the hashes: your criteria run it); the order `org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-202.absent-kind-carrier-a-contract-042-builder-and-the-cross-table-rule.md` (the round-105 ruling); the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` at 0.5.3 (`members`, `equivalences`, `lineage`); `data/assets/scripts/gold/irpt_reporting/filled_report_values.py` and `tests/test_filled_report_values.py` (your predecessor's work: 21 tests; the member fill, the activity and holdings branches).
2. **The contract 0.5.4.** For each of the ten members replace `source` with {`contract` "org/standards/IRPT_DASHBD_ACCOUNT_RETURN_DAILY_CONTRACT.json", `field` (the counterpart's `source.field`), `fold` (the sentence `Same fold as member <counterpart id> (round 105, DB-b-202 part d: the report's figures agree across tables); ` then the counterpart's own fold text)}. Keep every other key of the ten members (`id`, `section`, `baseline`, `label`, `unit` and any `unit_scale`). Make sure each pair is named by an equivalence: the two `ENDING_VALUE_*` groups already hold the ending-value pairs; add one new equivalence per remaining pair group (each {`id`, `meaning` (words), `entity` ("household" or "account"), `members` (both ids; for the household net gain over the last 12 months put `pvs.last_12_months.net_gain`, `act.net_gain.household` and `hold.net_gain_last_12_months` in ONE group)}), at least these ids: `BEGINNING_VALUE_HOUSEHOLD_LAST_12_MONTHS`, `BEGINNING_VALUE_ACCOUNT_LAST_12_MONTHS`, `NET_GAIN_HOUSEHOLD_LAST_12_MONTHS`, `NET_GAIN_ACCOUNT_LAST_12_MONTHS`, `NET_GAIN_HOUSEHOLD_YTD`, `NET_GAIN_HOUSEHOLD_QTD`, `NET_GAIN_HOUSEHOLD_SINCE_INCEPTION`. Set `contract_version` to "0.5.4" and append to `lineage` the entry {`contract_version` "0.5.3", `sha256` (the sha256 of the COMMITTED 0.5.3 bytes: `git show HEAD:org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` hashed as bytes, taken BEFORE you edit), `reason` (words)}. Change NOTHING else: the other 107 members, `document`, `gold_table`, the Inflection and Cottonwood `firm_sources` stay byte-for-byte (the checker hashes them).
3. **The module** `filled_report_values.py`: the member fill for the ten members takes the figure, text or absent form (kind and words included) of its counterpart for the same household and the same row key, and does not recompute it from the activity table; the activity table stays the source of every member that names it and is not one of the ten. Add the test `test_activity_members_equal_value_summary_members` to `tests/test_filled_report_values.py` (a synthetic household where the ten pairs are equal, including one household whose value-summary members are absent so their counterparts are absent with the same kind); keep the 21 tests that exist (the checker requires four named tests and at least 22 in all).
4. **The QA run** (49 Financial, one date, the same entry as before): `python -I data/assets/scripts/gold/irpt_reporting/filled_report_values.py . "C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~187" --firm 49financial --households 25` writes `filled_report_values_qa.parquet` (25 households, the newest `as_of`; run it in the background, it reads about 600 partitions, and wait for it).
5. **Record** `RD_ACT_EQUIV_R119.json` in your folder, counts, dates and words only, with EXACTLY these fields: `firm` ("49financial"), `as_of` (ISO), `contract_version` ("0.5.4"), `households` (1 to 100), `households_basis` (words), `rows`, `measured_rows`, `text_rows`, `absent_rows` (the three add to `rows`), `pairs` (a list of exactly 10, in the order of the ten pairs above, each {`member` (the repaired member id), `counterpart` (the value-summary member id), `households_both_measured`, `households_both_absent`, `households_differing` (0), `claim`}: counts over every household and every row key, the pair rows counted), `private_parquet` {`path` (under your private folder), `sha256`, `rows`}, `analysis` {`file` "data/assets/scripts/gold/irpt_reporting/filled_report_values.py", `sha256`, `tracked` true}, `reads` {`s3_reads` (integer), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, `claim` (one of measured, inferred, held, absent), `files_in_repo` false, `served_values_changed` false, `pushed` false, `deployed` false. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256` or `vintage` field; no household or account id; no client value.

<criterion id="DB119-1-AC1" cell_refs="DB-b-233"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r119/p119_actequiv.py" . DB119-1-AC1</invocation><expect>DB119-1-AC1 PASS</expect></criterion>
`DB119-1-AC1` -- the private QA parquet passes DB-b-230's table clauses (13 columns, one form per row, every contract member per household, no duplicate key, NO_SOURCE_YET for the ABSENT-sourced members); in every household each of the ten pairs is EQUAL (a figure within 0.005, or both absent with the same kind) and no member is absent everywhere while its counterpart is measured for some household; the record has exactly the form of step 5 and its pair counts equal the checker's own recount from the table. Base: FAIL (no record).
<criterion id="DB119-1-AC2" cell_refs="DB-b-233"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r119/p119_actequiv.py" . DB119-1-AC2</invocation><expect>DB119-1-AC2 PASS</expect></criterion>
`DB119-1-AC2` -- the contract reads 0.5.4; the ten members source the account return contract and their fold text names their counterparts; each pair is named by an equivalence; the other 107 members, the `document`, `gold_table` and the Inflection sources are unchanged (hashed by the checker); the lineage carries the 0.5.3 entry whose sha256 is the committed 0.5.3 bytes' hash (the checker finds those bytes in git). Base: FAIL (version 0.5.3).
<criterion id="DB119-1-AC3" cell_refs="DB-b-233"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r119/p119_actequiv.py" . DB119-1-AC3</invocation><expect>DB119-1-AC3 PASS</expect></criterion>
`DB119-1-AC3` -- the module and its test file are tracked; the test file has the four named tests (`test_activity_members_equal_value_summary_members`, `test_households_come_from_the_adapter`, `test_missing_sibling_table_is_no_source_yet`, `test_empty_lot_source_is_absent_not_zero`) and at least 22 tests pass (the checker runs `pytest`); the module uses `address(`, types no bucket, names no other firm, holds no S3 or DynamoDB write. Base: FAIL (the pair test is missing).

<expected_criteria>DB119-1-AC1,DB119-1-AC2,DB119-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the other sibling contracts, `adapters/cottonwood_report_reader.py` and its tests (another order's), `account_return_daily.py`, `sources.json`, the sample builders, `lib/`, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET the QA entry makes for the firm 49 Financial (the same prefixes `filled_report_values.py` reads, every one derived by `lib/opal_naming.py address()`), and the served model series object it already reads. Writes: the repo files of the grant and the private folder named above. No put, copy or delete of any kind, no deploy, no schedule, no push, no vendor call, no secret read, no read of another firm's place, no Terraform. The module holds NO S3 write.
- **Client data.** The gold partitions and the QA parquet are client data: counts, hashes and words only in the repo, a row or your report; never a household or account id.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a counterpart member of a pair is missing from the contract, or two members of a pair carry different grains (one household, one account), file a BLOCKING row naming both ids and stop on that pair; never invent an equivalence. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W187-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/filled_report_values.py
data/assets/scripts/gold/irpt_reporting/tests/test_filled_report_values.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~187/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-233.contract-054-and-module-activity-members-equal-value-summary.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 117 (round 119, workstream B-49F), cell `DB-b-233`.
<owned_cells>DB-b-233</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB119-1-AC1, DB119-1-AC2, DB119-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~187/IRPT_DASHBD.TO-DB-b-233.contract-054-and-module-activity-members-equal-value-summary.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB119-1-AC1,DB119-1-AC2,DB119-1-AC3` (the three ids as ONE comma-joined argument) BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the QA run's households, rows and the measured, text and absent counts; for each of the ten pairs the households both measured and both absent; the test count; the contract version and the lineage hash; also re-run `DB118-1-AC1`, `DB118-1-AC2` and `DB118-1-AC3` and `DB118-3-AC1`, `DB118-3-AC2` (`checks/r118/`) and report their last lines; reads and writes. Counts, dates and words only: no household or account id and no client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a contract text, a module, its tests and a private run in a branch; nothing is wired, scheduled, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the S3 reads are GET and LIST of prefixes of one firm already read by the module's first QA run.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the table's schedule and first cloud write go to 0.7.0_AE_CloudOps~DB2 after this cell lands (CTO ruling 1).
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB119-1-AC1 to AC3 FAIL at base (no record, version 0.5.3, the pair test missing) and the checker's clauses are exercised by its self-test (a green and four red pair arms, the contract arms).
lane: the <paths> block IS the grant.
</preflight>
