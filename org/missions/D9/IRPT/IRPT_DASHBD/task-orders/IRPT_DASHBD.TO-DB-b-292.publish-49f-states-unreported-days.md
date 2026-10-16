# TO IRPT_DASHBD.TO-DB-b-292 -- the 49 FINANCIAL series publisher states its unreported trading days (round 149, CTO ruling msg 9224): the handler passes the gold's partition dates and the trading calendar to the publisher, the manifest names the calendar, and the bundle's source-map entry gains the calendar as a pinned member

<to_id>IRPT_DASHBD.TO-DB-b-292</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~235</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>149</round>
<workstream>PUB49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** PUB49F, round 149 | **Ordered by:** 1.0.0_SA_CTO~DELL2, msg 9224 ("the 49 Financial publisher writes unreported_trading_days, an empty list where the gold has no absent trading day, plus its basis and calendar_source. It lands in one drain with any contract touch, then a republish of the 6,949 series under the 49 Financial publish pair") | **Decomp cell:** `DB-b-292` (decomposition section 153).

**Risk class WORLD** is the floor of the paths below (`infra/` paths): python and one JSON edit in a branch, no Terraform command, no AWS write, no build for upload, no push. The build, the upload, the apply and the republish are a later signed pair and the applier's.

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-16 ~09:5xZ, on worker rows IRPT_DASHBD-D2-W235-S1, S2 and S3; gate limb: GATE (viii), an existing order modified with placeholders NONE unchanged; no criterion id or cell change, one path added):** S2 is a DEFECT OF THE ISSUER'S CHECKER, ruled here: the bundle does NOT package the series contract (the lambda path passes none, S3 below), so the unpacked step of AC2 now grades the unpacked handler against the REPO's contract; the checker `p160_pub49f.py` is fixed (in your tree via the carry commit); you add nothing to the entry's `files` beyond the calendar. S1 is ruled: the two existing union tests stub `_publish_one` with a six-parameter lambda and the new call passes two more arguments, so step 3 gains a sub-step: in `infra/aws/lambda/investor-reporting/reporting-publish/tests/test_publisher_account_union.py` change ONLY the signatures of the two stubs (lines 59 and 71: `lambda s3, firm, a, rows, up, c: ...` becomes `lambda s3, firm, a, rows, up, c, dates=None, source=None: ...`); nothing else in that file; the file is added to the grant. AC3 now also runs the WHOLE `reporting-publish/tests` directory, which must pass. S3 stands as written: the deployed path passes no contract today; it is the decomposition's decision (a) and not this cell's to change. Re-run AC2 and AC3 after the edit, then finish the record, the proof instance and the flip.

**AMENDMENT 2 (issuer 2.0.0_SA_COO~D2, 2026-10-16 ~10:1xZ, on worker rows IRPT_DASHBD-D2-W235-S4 and S5; gate limb: GATE (viii), an existing order modified with placeholders NONE unchanged; no criterion id, cell or path change):** both rows are DEFECTS OF THE ISSUER. S4: the checker handed the unpacked step a RELATIVE root; it now resolves it to an absolute path (`p160_pub49f.py`, via the carry commit). S5: Amendment 1 named the stub's two new parameters `dates=None, source=None`, which do not accept your handler's keywords; the names are the handler's own: change the two stub signatures (lines 59 and 71) to `lambda s3, firm, a, rows, up, c, present_dates=None, calendar_source=None: ...`. Nothing else changes; re-run AC1 to AC3, finish the record, the proof instance and the flip.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-235` (branch `wk-IRPT_DASHBD-235`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~235/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value. Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~235/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** A 49 Financial series carries no `unreported_trading_days`, so the page cannot tell "no trading day is missing" from "not measured". The publisher module already derives the pair (`publisher.build_series(rows, present_dates=..., calendar=...)` writes `unreported_trading_days` and its basis text) and `publisher.build_manifest(..., calendar_source=...)` writes the calendar's name; the Cottonwood handler passes them. The 49 Financial handler passes neither. The CTO ruled that the 49 Financial series STATE their unreported days, as an EXPLICIT EMPTY LIST where the gold holds no absent trading day (under the claim law an absent field means "not measured"; a measured "none missing" is a written empty list).

**The cell (`DB-b-292`).** Three edits, nothing else.
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p160_pub49f.py` (your three criteria; `check_behaviour` and `check_entry` are the exact spec); `infra/aws/lambda/investor-reporting/reporting-publish/handler.py` and `publisher.py` (`unreported_days`, `build_series`, `build_manifest`, `CALENDAR_SOURCES`); the Cottonwood handler `infra/aws/lambda/investor-reporting/reporting-publish-cot/handler.py` (`_calendar_source`, and how it passes `present_dates=days` and `calendar=trading_calendar`); `lib/trading_calendar.py` (`calendar_source`, `FALLBACK_FIRST_YEAR`, `FALLBACK_LAST_YEAR`); `infra/aws/lambda/ci/lambda-source-map.json`, the one entry `irpt-49f-reporting-publish-lambda`; `infra/aws/lambda/ci/build-and-upload.sh` (the `BUILD_ONLY` mode; read only).
2. **The handler (`infra/aws/lambda/investor-reporting/reporting-publish/handler.py`).** (a) Import the calendar beside the naming builder: `from lib import trading_calendar  # noqa: E402`. (b) Add `_calendar_source()`: it returns `"pandas_market_calendars"` when `trading_calendar.calendar_source()` starts with `NYSE/pandas_market_calendars`, else `"fallback_%d_%d" % (trading_calendar.FALLBACK_FIRST_YEAR, trading_calendar.FALLBACK_LAST_YEAR)` (the same words as the Cottonwood handler; the contract's allowed values are `publisher.CALENDAR_SOURCES`). (c) `_publish_one` gains two keyword parameters `present_dates=None` and `calendar_source=None`; it calls `publisher.build_series(rows, present_dates=present_dates, calendar=trading_calendar if present_dates is not None else None)` and `publisher.build_manifest(acct, firm, series, len(gz), calendar_source=calendar_source)`. (d) `run` passes the sorted gold partition dates it already holds (`dates`, EVERY partition of the firm's gold table, NOT the account's own days) and `_calendar_source()` into `_publish_one`. Nothing else in the file changes: the summaries pass, the filled-report pass, the fan-out, `lambda_handler`, `main` and every constant stay byte for byte.
3. **The tests (`infra/aws/lambda/investor-reporting/reporting-publish/tests/test_handler_unreported.py`, new, at least 8 tests, self-contained: a fake S3 object holding synthetic gold parquet, no AWS, no private data).** They assert at least: complete gold gives the EXPLICIT empty list (`== []`) with the basis text; a gold missing one trading day lists exactly that day for every account whose window holds it; the list is the GOLD's missing days, not the account's own (an account with no row on a day whose partition exists is NOT listed for it); the manifest's `calendar_source` equals the calendar that answered and is one of `publisher.CALENDAR_SOURCES`; the publisher version is `0.3.0`; the series validates against `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` (`publisher.validate_against_contract`); numeric income writes no `income_claim`; `_publish_one` called WITHOUT the two new arguments still writes the old document (the pair absent, no `calendar_source`); `_calendar_source()` returns the two words for a stubbed calendar.
4. **The source map (`infra/aws/lambda/ci/lambda-source-map.json`, ONE edit, the entry `irpt-49f-reporting-publish-lambda` only).** (a) Add `lib/trading_calendar.py` to the entry's `files` immediately after `lib/opal_naming.py`, and a `staged_from` member right after `lib/opal_naming.py`'s with `repo_path` and `packaged_as` both `lib/trading_calendar.py`, `pin` the full 40-hex commit that last changed it (`git log -1 --format=%H -- lib/trading_calendar.py`; an ancestor of HEAD) and `sha256` the hex sha256 of the file at HEAD (equal to `git show <pin>:lib/trading_calendar.py`). (b) Re-pin every OTHER `staged_from` member whose file at HEAD no longer has the entry's `sha256` (find them by hashing; the build refuses a stale pin): a new full-commit `pin` (the commit that last changed the file) and the new `sha256`, `packaged_as` unchanged. A member that is not stale stays byte for byte. Every other key of the entry (INCLUDING `artifact_sha256`, `deployed_code_sha256`, `last_deployed_commit`, `last_deployed_at`, `recorded_by` and the notes), every other entry and every top-level key stay byte for byte. Commit the file BEFORE running AC2 (the build reads committed source). Re-run your hashing just before your commit: another seat may have edited a pinned file meanwhile.
5. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p160_pub49f.py" . DB160-1-AC1`, then AC2 (this runs the build-only package, the import check against the layer and the behaviour check on the UNPACKED handler; it takes a few minutes), then AC3.
6. **Record** `RD_PUB49F_UNREPORTED_FACTS_R149.json` in your folder with EXACTLY these fields: `entry` ("irpt-49f-reporting-publish-lambda"); `added_member` ("lib/trading_calendar.py"); `repinned` (the repo paths you re-pinned, as a list, possibly empty); `tests` (the number of passing tests in your test file); `words` (one paragraph, 80 to 1800 characters: what changed and why, that no deployed field moved, and what is NOT proven: nothing is uploaded or deployed or republished, the Lambda's calendar answer is the fallback table unless the package is bundled, and a pinned file edited by another seat after your commit makes the entry stale again).

<criterion id="DB160-1-AC1" cell_refs="DB-b-292"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p160_pub49f.py" . DB160-1-AC1</invocation><expect>DB160-1-AC1 PASS</expect></criterion>
`DB160-1-AC1` -- on a fake S3 holding synthetic 49 Financial gold, the handler's series validate against the series contract; with every trading day present each carries the explicit empty unreported list and its basis text; with one day absent each lists exactly that day (the gold's missing days, not the account's own); the manifest names the calendar that answered (publisher 0.3.0); numeric income writes no claim. Base: FAIL (no pair).
<criterion id="DB160-1-AC2" cell_refs="DB-b-292"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p160_pub49f.py" . DB160-1-AC2</invocation><expect>DB160-1-AC2 PASS</expect></criterion>
`DB160-1-AC2` -- the entry gained the calendar (listed once in `files`, pinned in `staged_from` with a sha256 equal to `git show pin:path` and the file at HEAD), stale pins moved and nothing else changed (no deployed field, no other entry); the `BUILD_ONLY` package holds exactly the entry's `files` with every member's bytes equal to its source, its third-party imports are pyarrow plus the runtime's, and the handler UNPACKED from the package passes AC1's behaviour. Base: FAIL.
<criterion id="DB160-1-AC3" cell_refs="DB-b-292"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r149/p160_pub49f.py" . DB160-1-AC3</invocation><expect>DB160-1-AC3 PASS</expect></criterion>
`DB160-1-AC3` -- the worker's test file holds at least 8 passing tests that assert the empty list, a listed day and `calendar_source`; the whole `reporting-publish/tests` directory passes; the worker's commits change only the handler, its test file, the two stub signatures in the union test, the source map, the folder, the investigation file and task-order files; the facts record equals the checker's recount. Base: FAIL.

<expected_criteria>DB160-1-AC1,DB160-1-AC2,DB160-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **Reads and writes.** Reads: repo files, the layer (`aws lambda list-layer-versions` and `get-layer-version`, GET and LIST only, which the checker also makes). Writes: the files in the grant and your private folder. The `BUILD_ONLY` run writes a zip under a temporary directory only. No Terraform command, no AWS write, no upload, no push, no invoke, no S3 read of client data (the tests use synthetic gold in memory).
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W235-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/lambda/investor-reporting/reporting-publish/handler.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_handler_unreported.py
infra/aws/lambda/investor-reporting/reporting-publish/tests/test_publisher_account_union.py
infra/aws/lambda/ci/lambda-source-map.json
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~235/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-292.publish-49f-states-unreported-days.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 153 (round 149, workstream PUB49F), cell `DB-b-292`.
<owned_cells>DB-b-292</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB160-1-AC1, DB160-1-AC2, DB160-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~235/IRPT_DASHBD.TO-DB-b-292.publish-49f-states-unreported-days.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB160-1-AC1,DB160-1-AC2,DB160-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the re-pinned paths; the test count; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: python and one source-map entry in a branch; nothing is built for upload, uploaded, planned, deployed or invoked.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS write and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the behaviour clause was validated by the issuer against a scratch reference handler (green) and 5 injected faults (all red); the entry clause has 10 red arms in the self-test; the package clauses reuse the proven checkers of rounds 147 to 149.
lane: the <paths> block IS the grant.
</preflight>
