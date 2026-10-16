# TO IRPT_DASHBD.TO-DB-f-702 -- the FWD-3 PRODUCER GAP READ: where the existing `account_class_daily` producer meets the CTO's acceptance (the classes sum to the account on every day, by test; the classification is a dated read of `etf-classifications`, claim `held`), whether the reporting-gold function still emits it, how the swap snapshot reads the same table, and on which days the table cannot be MEASURED; a read of code and tests, nothing written

<to_id>IRPT_DASHBD.TO-DB-f-702</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~702</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>120</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-119 analysis for F-SHIP ruling 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_119_20261016.md`: "FWD-3, the class-daily gold producer: Owner `2.0.0_SA_COO~F2` ... Acceptance: classes sum to the account on every day, by test. It reads `etf-classifications` through the same path as the swap snapshot (a dated read, claim `held`), never hand-typed.") and the row `IRPT_DASHBD-D2-S102` | **Rows:** IRPT_DASHBD-D2-W702-S<k> | **Decomp cell:** `DB-f-702` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R120_F.md`) | **outcome_ref:** FWD-3 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-702` (branch `wk-IRPT_DASHBD-702`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~702/`. The folders `data/`, `infra/aws/lambda/`, `infra/aws/terraform/` and `org/critical_paths/` are materialized in your worktree for reading (if one is missing, run `git sparse-checkout add <folder>` for it: that is not a grant to edit). Never push; never commit the workspace `portal` gitlink. This is a READ of repository files and git history: no AWS call of any kind, no network, no vendor call, no secret read. Any real client, household or account id and any client figure is never written in the repo, a row or your report.

**Why.** The CTO ruled that `~F2` owns the FWD-3 class-daily gold producer with the acceptance above. Round 119's read found the table ALREADY has a producer (`data/assets/scripts/gold/irpt_reporting/account_class_daily.py`), a contract, tests and an applied release (class rows logged landed for 2026-10-07 and 2026-10-08); the row `IRPT_DASHBD-D2-S102` carries the open question (move, extend or another table) to the CTO. Whatever the answer, the work needs the same measurement first: how far the EXISTING producer already meets the acceptance. This cell measures that from code and tests only.

**The cell (`DB-f-702`).**
1. **The producer.** Read `data/assets/scripts/gold/irpt_reporting/account_class_daily.py` and its tests (`data/assets/scripts/gold/irpt_reporting/tests/test_account_class_daily.py`) and the contract `org/standards/IRPT_DASHBD_ACCOUNT_CLASS_DAILY_CONTRACT.json` (`method`, `class_source`, `coverage`). Record the file and the line of the class mapping (`producer`).
2. **The handler.** Read `infra/aws/lambda/investor-reporting/reporting-gold/handler.py` and the Terraform root under `infra/aws/terraform/investor-reporting/reporting-gold/`: does the function emit the class table today in its daily pass (`emits_class_table` true or false) and on what schedule (cite the file and line that decides it: `handler`). Where only the live function could say (the deployed bytes), the claim is `absent` and the words say so.
3. **The sum to the account.** Is there a test that the classes of one account-day sum to the account's value (and, on a measured day, that the daily contributions sum to the account's daily return)? Record `exists` (true or false), and if true the test file and the line (`sum_test`); if false say in words where the sum is enforced instead (the producer's own `CLASS_VALUES_DO_NOT_SUM_TO_ACCOUNT` coverage value or similar) and whether a day that fails it is written with a null return.
4. **The classification read.** Read how the producer reads `etf-classifications` (the contract's `class_source`: one GetItem per identifier at run time) and answer whether the read is DATED (a snapshot with a date and a claim `held`, as the swap snapshot's is) or LIVE (`dated` true or false; `classification_read` with the file and the line of the read).
5. **The swap snapshot.** Find how the swap snapshot reads the same table (`comp-find --files 'etf-classifications' data infra --limit 20` and `comp-find --files 'swap' data/assets/scripts --limit 20`; print the denominators you cite): record the file and the line of its dated read and in words how it dates and labels it (`swap_snapshot_read`).
6. **Days it cannot be measured.** From the contract's `coverage` enum and the producer's code, list in words each situation in which a day's class figures are not MEASURED and what the table then holds (`failing_days_words`, a non-empty list of strings, one per coverage value or situation).
7. **Record** `RD_FWD3_PRODUCER_GAP_R120.json` in your folder with EXACTLY these fields: `as_of` (ISO date); `producer` {`file`, `line`, `words`, `claim`} (the line must hold `account_class_daily`, `class_return_daily` or `asset_class`); `handler` {`file`, `line`, `emits_class_table` (boolean), `words`, `claim`} (the line must hold `account_class_daily`, `class` or `emit`); `sum_test` {`exists` (boolean), `file`, `line` (when `exists` is true: the line must hold `sum`, `account` or `class`; when false, give the nearest enforcing file and line and say so in `words`), `words`, `claim`}; `classification_read` {`file`, `line`, `dated` (boolean), `words`, `claim`} (the line must hold `etf`, `classif`, `getitem` or `table`); `swap_snapshot_read` {`file`, `line`, `words`, `claim`} (the line must hold `etf`, `classif`, `snapshot`, `swap` or `table`); `failing_days_words` (the list); `reads` {`s3_reads` 0, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}; and the false flags `files_in_repo`, `served_values_changed`, `pushed`, `deployed`. Every `claim` is one of `measured`, `inferred`, `held`, `absent` (with the reason in the words; never invented). No run of 8 or more digits outside a `path`, `file`, `key`, `where` or `vintage` field.

<criterion id="DBF120-2-AC1" cell_refs="DB-f-702"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r120/p120_reads.py" . DBF120-2-AC1</invocation><expect>DBF120-2-AC1 PASS</expect></criterion>
`DBF120-2-AC1` -- `RD_FWD3_PRODUCER_GAP_R120.json` has exactly the form of step 7; each cited file exists and each cited line holds a token its field names; `handler.emits_class_table`, `sum_test.exists` and `classification_read.dated` are booleans with words; `failing_days_words` is a non-empty list of strings; every claim is in the four-word set; the reads block is all zero, the four flags are false and no run of 8 or more digits stands outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DBF120-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every code file, the contract, the Terraform, the tests, the issuer's check.
- **A READ.** Nothing is deployed, applied, published, pushed or changed outside your folder; no AWS call; no network. A fact only the live function or bucket could answer is `absent` with that reason, never a guess.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A zero is never read as "does not exist" without the tool's printed denominator beside it. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W702-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~702/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-702.read-fwd3-existing-class-producer-gap-sum-to-account-and-the-dated-classification-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R120_F.md</decomp_doc> round 120, workstream ~F2 (F-SHIP), cell `DB-f-702`.
<owned_cells>DB-f-702</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF120-2-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~702/IRPT_DASHBD.TO-DB-f-702.read-fwd3-existing-class-producer-gap-sum-to-account-and-the-dated-classification-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF120-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; whether the handler emits the class table and on what schedule; whether a sum-to-account test exists; whether the classification read is dated; how the swap snapshot dates its read; the situations in which a day is not measured; anything off-task (as row ids). No real id and no client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the schedule is read from code and Terraform.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF120-2-AC1 FAILS at base (no record) and the record form is exercised by the checker's self-test.
lane: the <paths> block IS the grant.
</preflight>
