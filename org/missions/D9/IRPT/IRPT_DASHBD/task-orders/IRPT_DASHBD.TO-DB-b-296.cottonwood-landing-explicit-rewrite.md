# TO IRPT_DASHBD.TO-DB-b-296 -- the COTTONWOOD LANDING'S EXPLICIT REWRITE EVENT (round 149, CTO ruling on fork e6ef, msg 9264, route (c)): the handler overwrites already-landed days with the derived history_scope when an event names them, capped and landed-days-only; the no-overwrite guard stays everywhere else

<to_id>IRPT_DASHBD.TO-DB-b-296</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~239</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>HSRW</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** HSRW, round 149 | **Ordered by:** 1.0.0_SA_CTO~DELL2, msg 9264 ("Fork e6ef: I accept (c). The landing handler gets an explicit rewrite event, capped at MAX_BACKFILL_DAYS and limited to already-landed days, mirroring the 49 Financial backfill. The versioned bucket keeps prior versions and nothing is deleted. The scheduled path keeps its no-overwrite guard. Cut the code cell.") | **Decomp cell:** `DB-b-296` (decomposition section 157).

**Risk class WORLD** is the floor of the paths below (`infra/` path): python in a branch, no Terraform command, no AWS write, no build for upload, no run against S3, no push. The code update and the rewrite of the 65 landed days are a later signed pair and the applier's.

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-16 ~11:0xZ, on worker row IRPT_DASHBD-D2-W239-S1; gate limb: GATE (viii), an existing order modified with placeholders NONE unchanged; one path added to the grant, no criterion id or cell change):** the row is a DEFECT OF THE ISSUER'S GRANT: `DB-b-294`'s test `test_history_scope_derivation.py` (carried into your tree) spies on `run_day` with a signature that does not accept the new `rewrite` keyword the handler now passes. It joins the grant for ONE purpose: change ONLY the signature of that spy (add `rewrite=False` or `**kw`, as its other parameters do) so it accepts the keyword; nothing else in that file. Then finish AC3, the record (the facts record's `tests` is your new file's count), the proof instance and the flip.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-239` (branch `wk-IRPT_DASHBD-239`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~239/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value. Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~239/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The 65 Cottonwood gold days already landed carry the old `history_scope` constant. Your tree already carries cell `DB-b-294` (as file copies): the adapter derives the scope from the floor-day partition (`run_day(..., floor_day=...)`) and the landing handler passes `FLOOR_DAY`. But `write_day` REFUSES to write a partition that already holds objects, so a landed day can never take the derived value. The CTO ruled an explicit, signed rewrite event: it changes only days that are already landed, at most `MAX_BACKFILL_DAYS` per event, deletes nothing (the bucket is versioned, so every prior version stays), and leaves the guard in force on the scheduled path and on the named-day path.

**The cell (`DB-b-296`).** Two code edits and one test file; nothing else.
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p164_cot_rewrite.py` (your three criteria; `check_adapter` and `check_handler` are the exact spec, down to the names `rewrite`, `landed_days` and `_rewrite`); `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py` (`write_day`, `run_day`, `GoldWriteError`, `gold_prefix`); `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` (`newest_landed_day`, `_run`, `lambda_handler`, `_day`, `_above_floor`, `MAX_BACKFILL_DAYS`, `FLOOR_DAY`); `infra/aws/lambda/investor-reporting/reporting-gold/handler.py` (its `backfill` mode, the precedent).
2. **The adapter (`cottonwood_bd_account_return_daily.py`).** (a) `write_day(s3, day, table, manifest, rewrite=False)`: after the one LIST of the day's partition: with `rewrite` true and NO object listed, raise `GoldWriteError` (a rewrite changes a landed day only) before any put; with `rewrite` false and an object listed, raise `GoldWriteError` exactly as today; with `rewrite` true and objects listed, put the two objects (same keys, same order) and delete nothing. The client still has only `put_object` and `list_objects_v2`. (b) `run_day(reader, s3, day, upload=True, floor_day=None, rewrite=False)` passes `rewrite` to `write_day`; and when `rewrite` is true and the day's table does not carry the claim column (no `floor_day`, or no floor partition) it raises `GoldWriteError` before any put (a rewrite writes the derived scope or nothing).
3. **The landing handler (`handler.py`).** (a) Split `newest_landed_day` into `landed_days(s3, bucket, key_prefix)` (every ISO `date=` partition name, sorted; the same LIST with Delimiter and pagination) and `newest_landed_day` calling it (same answer as today). (b) `_run(s3, reader, days, upload, rewrite=False)` passes `rewrite` to `cbd.run_day(..., floor_day=FLOOR_DAY, rewrite=rewrite)`. (c) A new function `_rewrite(event, upload, s3, reader)`, called from `lambda_handler` as soon as `upload` is known when `"rewrite" in event`: it refuses with `ValueError`, before any write, when the event also carries `day` or `days`, when the spec is not an object with EXACTLY the keys `start` and `end`, when a date is not an ISO calendar date (`_day`), when start is after end, when start is before `FLOOR_DAY` (`_above_floor`), when the range holds no trading day (`tc.trading_days_between`), or when any trading day of the range is not among `landed_days` (name the first); it refuses with `SystemExit` (as the named-day path does) when the range holds more than `MAX_BACKFILL_DAYS` trading days; otherwise it runs `_run(..., rewrite=True)` over exactly those days and returns `{"ok": True, "rewrite": True, "days": days, "results": results, "held": held}`. With `dry_run` true nothing is written. The scheduled path, the `day` path and the `days` path are unchanged and keep the guard.
4. **The tests** `data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_rewrite.py` (new, at least 10 passing tests, self-contained: a fake reader and a fake writer with `put_object` and `list_objects_v2` only, no AWS, no private data). They assert at least: `write_day` with rewrite on a landed day puts the same two keys and creates no other; with rewrite on an empty partition raises before any put; without rewrite on a landed day raises as today; `run_day` rewrite derives the 21-column table; `run_day` rewrite with no floor partition and with no floor day raises before any put; `landed_days` and `newest_landed_day` over a paginated listing; the event rewrites two landed days (four existing keys, nothing else); every refusal of step 3 (one test each or parametrised) writes nothing; a dry-run rewrite writes nothing; the `day` and `days` paths still refuse a landed day.
5. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p164_cot_rewrite.py" . DB164-1-AC1`, then AC2, then AC3 (AC3 runs the whole gold tests directory and the landing handler's tests). One test in the gold directory, `test_account_activity_lots.py::test_the_calendar_itself_raises_before_2010_and_the_index_never_asks_it`, was red BEFORE your edit; the checker deselects it; do not touch it.
6. **Record** `RD_COT_REWRITE_FACTS_R149.json` in your folder with EXACTLY these fields: `event` ({"rewrite": {"start": "YYYY-MM-DD", "end": "YYYY-MM-DD"}}); `cap` (25); `landed_days_only` (true); `guard_unchanged` (true); `deletes` (0); `tests` (the count of passing tests of your new file); `words` (one paragraph, 80 to 1800 characters: what changed and why, that nothing is deleted and prior versions stay, and what is NOT proven: nothing ran against S3, the function is not updated, and the rewrite of the 65 days is a separate signed pair).

<criterion id="DB164-1-AC1" cell_refs="DB-b-296"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p164_cot_rewrite.py" . DB164-1-AC1</invocation><expect>DB164-1-AC1 PASS</expect></criterion>
`DB164-1-AC1` -- the adapter's `run_day` with rewrite overwrites exactly a landed day's two keys with the derived 21-column table (no other key, no delete); a plain landing of a landed day is still refused; a rewrite of an unlanded day, with no floor partition or with no floor day is refused before any put; a dry run writes nothing. Base: FAIL.
<criterion id="DB164-1-AC2" cell_refs="DB-b-296"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p164_cot_rewrite.py" . DB164-1-AC2</invocation><expect>DB164-1-AC2 PASS</expect></criterion>
`DB164-1-AC2` -- the landing handler's rewrite event overwrites the named landed days (the four existing keys, 21 columns with the claim), refuses before any write a day not landed, a combination with day or days, a malformed spec, start after end, a start before the floor, a non-ISO date, a range of no trading day and a range over the cap, writes nothing on a dry run, and the named-day path keeps the no-overwrite guard. Base: FAIL.
<criterion id="DB164-1-AC3" cell_refs="DB-b-296"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p164_cot_rewrite.py" . DB164-1-AC3</invocation><expect>DB164-1-AC3 PASS</expect></criterion>
`DB164-1-AC3` -- the new test file holds at least 10 passing tests; the whole gold tests directory (the one known pre-existing red deselected) and the landing handler's tests pass; the worker's commits change only the adapter, the landing handler, the new test file, the signature of one spy in `DB-b-294`'s test, the folder, the investigation file and task-order files; the facts record equals the checker's recount. Base: FAIL.

<expected_criteria>DB164-1-AC1,DB164-1-AC2,DB164-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the contracts, the publisher, the other producers, the `reporting-gold` handler, the source map, the portal, the issuer's check files.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no run against S3, no deploy, no push. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your edit, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W239-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements). Write files with LF line endings (write bytes).

<paths>
data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py
data/assets/scripts/gold/irpt_reporting/tests/test_cottonwood_rewrite.py
data/assets/scripts/gold/irpt_reporting/tests/test_history_scope_derivation.py
infra/aws/lambda/investor-reporting/account-return-daily/handler.py
infra/aws/lambda/investor-reporting/account-return-daily/tests/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~239/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-296.cottonwood-landing-explicit-rewrite.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 157 (round 149, workstream HSRW), cell `DB-b-296`.
<owned_cells>DB-b-296</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB164-1-AC1, DB164-1-AC2, DB164-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~239/IRPT_DASHBD.TO-DB-b-296.cottonwood-landing-explicit-rewrite.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB164-1-AC1,DB164-1-AC2,DB164-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the changed functions in one line per file; the test count; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: python in a branch; nothing runs against S3 and nothing is deployed, so no served output moves; the rewrite of the 65 landed days is a later signed pair.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS is read or written and no grant changes (the landing function's role already holds the put on the gold prefix; a rewrite adds no action).
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; the scheduled path is unchanged.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the behaviour clauses were validated by the issuer against a scratch reference of the edits (green: AC1 and AC2) and 11 single-fault mutants (all red).
lane: the <paths> block IS the grant.
</preflight>
