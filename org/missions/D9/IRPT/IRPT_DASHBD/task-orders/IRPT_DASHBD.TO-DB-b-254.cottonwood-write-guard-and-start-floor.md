# TO IRPT_DASHBD.TO-DB-b-254 -- the NO-OVERWRITE GUARD and the START FLOOR of the Cottonwood landing code (round 125, workstream B-49F): `write_day` LISTs the exact day partition under the granted gold prefix and raises with no put if either key exists; the handler's `owed_days` never owes a day before 2026-07-10 and an event naming any day before it raises before any write; both tested with fake clients; LOCAL build, nothing landed or deployed; this is the fix that disarms row IRPT_DASHBD-D2-S79

<to_id>IRPT_DASHBD.TO-DB-b-254</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~207</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>125</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 125 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-124 ANALYSIS (B-49F) section 2 ruling 1 and section 3 cell 1 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_124_20261015.md @4285776c5c`: "(a) a no-overwrite guard in `write_day`: list the exact key under the granted prefix first, and refuse if it exists. A test plants an existing key. (b) a start floor of 2026-07-10 in `owed_days`, so a held gap day is never owed. A test covers the gap ... No event ever names a day on or before 2026-06-22") | **Rows:** IRPT_DASHBD-D2-W207-S<k>; disarms IRPT_DASHBD-D2-S79 | **Decomp cell:** `DB-b-254` (decomposition section 123) | **outcome_ref:** FWD-11, FWD-21 | **depends_on:** none

**Risk class WORLD** is the floor of the paths below (an `infra/` path): this order edits a handler, an adapter and their tests and runs no AWS call and no Terraform command.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-207` (branch `wk-IRPT_DASHBD-207`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~207/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~207/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The Cottonwood gold prefix `irpt/cottonwood/gold/account_return_daily/` is OCCUPIED: 3,325 Commonwealth-era partitions, 2013-04-03 to 2026-06-22 (row `IRPT_DASHBD-D2-S79`, ARMED). The merged adapter's `write_day` puts `data.parquet` and `manifest.json` for any valid ISO day without looking at what is there, so an event naming a day on or before 2026-06-22 would replace a history partition with Black Diamond rows under a different account key; and the merged handler's `owed_days` returns the trading days after the newest landed partition (2026-06-22), the first five of which fall in the Black Diamond silver gap (every one held, nothing landed, the same five owed at every fire). Neither can happen today (the Terraform root is unapplied, the schedule DISABLED, the function undeployed). Both are fixed here, before any landing packet.

**The cell (`DB-b-254`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r125/p125_guard.py` (your three criteria; the two probes in it ARE the behaviour spec, and its docstring states the superseded clause); the adapter `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py` (`gold_prefix`, `build_manifest`, `write_day`, `run_day`) and its test file; the handler `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` (`owed_days`, `newest_landed_day`, `lambda_handler`, `MAX_DAYS_PER_FIRE`, `MAX_BACKFILL_DAYS`) and its test file; the Terraform root's gold list statement `infra/aws/terraform/investor-reporting/account-return-daily/iam.tf` (the role already holds `s3:ListBucket` on the gold bucket under the prefix condition `irpt/<firm>/gold/account_return_daily/*`: the guard needs no new grant).
2. **The adapter guard** (ADDITIVE: at most 8 existing lines may change). In `write_day`, after the existing refusals (bad day, no rows, wrong manifest) and BEFORE any put: ONE call `s3.list_objects_v2(Bucket=bucket, Prefix=base)` where `base` is the day's partition prefix `<gold prefix>date=<day>/` (the same `base` the puts use); if the response lists ANY object (`Contents` non-empty) raise `GoldWriteError` (the message names the day, never an identifier) with NO put. Update the docstring: exactly ONE list call and, when the partition is empty, two puts. `run_day` needs no change (the error propagates; a held day still writes nothing and never reaches `write_day`). The 32 earlier tests keep their meaning: where their fake S3 object lacks `list_objects_v2`, give it one that lists the keys put so far (a small edit to the fakes in the test file, which is in your grant). At least 4 NEW tests: an existing `data.parquet` key refuses with no put; an existing `manifest.json` only refuses with no put; a key of ANOTHER day does not block; `run_day` over an existing partition raises with no put; the list call's `Prefix` is exactly the day partition. The test file holds at least 36 tests and all pass.
3. **The handler floor** (ADDITIVE: at most 12 existing lines may change). A module constant `FLOOR_DAY = "2026-07-10"` with a comment citing the CTO's round-124 ruling 1(b) (the first day after the Commonwealth-era history on which the silver exists). `owed_days(newest_landed, today, max_days=MAX_DAYS_PER_FIRE)`: T-1 as today; the first owed day is the later of (the day after `newest_landed`) and `FLOOR_DAY`; with nothing landed it owes `[T-1]` only when T-1 is on or after `FLOOR_DAY`, else `[]`; still oldest first, still at most `max_days`; it owes nothing while T-1 is before the floor. `lambda_handler`: BEFORE any client is created or any read made, every day named by a `day` or `days` event is validated; any day before `FLOOR_DAY` (including every day on or before 2026-06-22) raises (`ValueError` naming the floor, no day echoed beyond the first) and the WHOLE event is refused, `dry_run` included; the existing real-date and 25-day checks stay. At least 4 NEW tests in the handler test file: the gap (after 2026-06-22 on 2026-07-15 the owed days start at 2026-07-10); nothing owed while T-1 is before the floor; an event naming 2026-06-22, one naming 2026-07-09 and a mixed `days` event are refused with no write; the floor day itself runs; an existing partition raises with no put. The handler test file holds at least 15 tests and all pass.
4. **The facts record** `RD_GUARD_FLOOR_FACTS_R125.json` in your folder with EXACTLY these fields: `adapter` {`file`, `function` ("write_day"), `list_calls_per_write` (1), `list_prefix_form` (words: the form of the Prefix), `words`}; `handler` {`file`, `floor_day` ("2026-07-10"), `floor_applies_to` (a list that includes "owed_days", "day_event", "days_event"), `words`}; `tests` {`adapter_file`, `adapter_new_tests`, `adapter_total`, `handler_file`, `handler_new_tests`, `handler_total`}; `superseded_clause` (one sentence naming `DB121-4-AC2`'s "calls NO other client method" and saying it is superseded by the guard's ONE list call); `files_changed` (the adapter, its test file, the handler and its test file, each {`file`, `sha256` (of the bytes at your final commit), `kind`}); `disarm` {`row` ("IRPT_DASHBD-D2-S79"), `words` (what is now true that the row said was not)}; `words`; `claim`; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256` or `vintage` field.

<criterion id="DB125-1-AC1" cell_refs="DB-b-254"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r125/p125_guard.py" . DB125-1-AC1</invocation><expect>DB125-1-AC1 PASS</expect></criterion>
`DB125-1-AC1` -- the checker's adapter probe (fake S3, run in a child interpreter): a clean day writes exactly two objects after exactly one LIST whose `Prefix` is the day partition in the gold bucket; an existing `data.parquet`, an existing `manifest.json` and an existing history day each raise `GoldWriteError` with NO put; another day's key does not block; `run_day` over an existing partition raises with no put, over a clean day writes two and with `upload=False` writes none; the adapter test file holds at least 36 tests and `pytest` on it passes. Base: FAIL (no list call).
<criterion id="DB125-1-AC2" cell_refs="DB-b-254"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r125/p125_guard.py" . DB125-1-AC2</invocation><expect>DB125-1-AC2 PASS</expect></criterion>
`DB125-1-AC2` -- the checker's STAGED probe (the handler and the source-map entry's members copied to a directory with no repo checkout): `FLOOR_DAY` is 2026-07-10; `owed_days` after 2026-06-22 on 2026-07-15 owes 2026-07-10, 2026-07-13 and 2026-07-14, after 2026-07-10 owes 2026-07-13 and 2026-07-14, with nothing landed owes T-1 only when it is on or after the floor, owes nothing while T-1 is before it, and still caps at `MAX_DAYS_PER_FIRE`; events naming 2026-06-22, 2026-07-09, 2026-06-30 or a `days` list that includes such a day raise before any write (a dry run included); 2026-07-10 and 2026-07-14 write two objects; an existing partition raises with no put; the handler test file holds at least 15 tests and `pytest` on it passes. Base: FAIL (no floor).
<criterion id="DB125-1-AC3" cell_refs="DB-b-254"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r125/p125_guard.py" . DB125-1-AC3</invocation><expect>DB125-1-AC3 PASS</expect></criterion>
`DB125-1-AC3` -- `RD_GUARD_FLOOR_FACTS_R125.json` has exactly the form of step 4 and its files hash as recorded; in the worker's own commits the adapter gains at least 8 lines and loses at most 8, the handler gains at least 10 and loses at most 12, and nothing else under `infra/`, `data/`, `lib/` or `org/standards/` changes (the source map included). Base: FAIL (no record).

<expected_criteria>DB125-1-AC1,DB125-1-AC2,DB125-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the Terraform root, the source map, `lib/`, the registry, the contract, every other adapter, handler and test, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files. The tests and the probes use fake clients; no network, no AWS call, no S3 read or write, no Terraform command, no deploy, no push, no vendor call, no secret read. Writes: the repo files of the grant.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a change to the adapter would break an earlier test in a way that is not just a fake client lacking `list_objects_v2`, or the floor cannot be added without changing a signature the checker calls, file a BLOCKING row with the numbers and stop on that point. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W207-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-15, on worker row W207-S1; gate limb: a modification of an existing order, placeholders NONE, no criterion id, cell or path changes).** Step 3 said the earlier handler tests keep their meaning. One of them cannot: `test_owed_days_three_examples` pins round 122's third example, "newest 2026-06-01 on 2026-07-15 owes five days", and the floor makes that three (2026-07-10, 2026-07-13, 2026-07-14). The floor is the CTO's ruling; the example is superseded. You may change THAT ONE example in THAT ONE test to the cap check on a date where five days fit above the floor (newest 2026-06-01 on 2026-09-15 owes five days, the first being 2026-07-10), and nothing else in it or in any other earlier test beyond the fake S3 list method of step 2. State the change in the facts record's `words`. Resolve row `W207-S1` by an appended OBSERVATION row citing the amendment commit.

<paths>
data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_bd_account_return_daily.py
infra/aws/lambda/investor-reporting/account-return-daily/handler.py
infra/aws/lambda/investor-reporting/account-return-daily/tests/test_handler.py
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~207/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-254.cottonwood-write-guard-and-start-floor.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 123 (round 125, workstream B-49F), cell `DB-b-254`.
<owned_cells>DB-b-254</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB125-1-AC1, DB125-1-AC2, DB125-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~207/IRPT_DASHBD.TO-DB-b-254.cottonwood-write-guard-and-start-floor.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB125-1-AC1,DB125-1-AC2,DB125-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the guard's list call and where it sits in write_day; the floor's effect on owed_days and on the two event shapes; the existing lines you changed; the test counts; whether any earlier test needed more than a fake's list method. Words and counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: an adapter, a handler, their tests and a facts record in a branch; nothing is wired to AWS, landed, scheduled, planned or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written; the guard's one list call uses the list grant the root already declares, and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its probes were validated by the issuer against a scratch reference with the guard and the floor (green) and the merged unguarded adapter (red); its other clauses by its self-test.
lane: the <paths> block IS the grant.
</preflight>
