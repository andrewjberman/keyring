# TO IRPT_DASHBD.TO-DB-b-280 -- the COTTONWOOD SERIES PUBLISH HANDLER (round 147): one Lambda handler that reads the Cottonwood gold `account_return_daily` partitions from the floor day, builds each account's series and manifest with the publisher's pure functions and, only when the event says upload is exactly True, writes them at the naming builder's platinum `reporting` address

<to_id>IRPT_DASHBD.TO-DB-b-280</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~226</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>147</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F + contract, round 147 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md ADDENDUM v0.16 item 4 and the CTO boundary ruling msg 8803 ("~D2 owns handler.py, publisher.py, the publish tf root and the sources entry. The first Cottonwood series publish is ~D2's cell, under its own pair and in one drain with the contract field.") | **Decomp cell:** `DB-b-280` (decomposition section 145).

**Risk class WORLD** is the floor of the paths below (an `infra/` path), not a statement that anything is deployed: python files only; no AWS, no deploy, no push, no invoke. The handler is NEW SERVED OUTPUT when it is run by the applier under a never-widen pair; this order runs nothing and writes nothing outside the repo.

**AMENDMENT 1 (issuer 2.0.0_SA_COO~D2, 2026-10-16 ~02:5xZ, on worker row IRPT_DASHBD-D2-W226-S2; gate limb: an existing order modified, placeholders NONE unchanged, no criterion id, cell or path change):** (1) Your branch now CONTAINS the series contract 0.3.0: the issuer merged `wk-IRPT_DASHBD-225` into `wk-IRPT_DASHBD-226` (merge commit 6e56bb47d3), so `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json` on your branch reads 0.3.0 and names `unreported_trading_days` and `unreported_trading_days_basis` in `series.optional`. You still edit NO contract file; `DB147-2-AC1` runs against that 0.3.0 file as written, with no re-pointing. (2) Your row W226-S2 is ruled by this: the order's base lacked the contract the handler's guard reads, a defect of the issuer's order. Resume from your committed handler; write the test file, the facts record and the proof instance, and flip the status to complete last.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-226` (branch `wk-IRPT_DASHBD-226`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~226/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~226/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** No Cottonwood series is published (`irpt/cottonwood/platinum/` holds only holdings), so the Performance page has nothing to read for a Cottonwood account. The 49 Financial function (`reporting-publish/handler.py`) is firm-agnostic through the custody declaration, but it would need a second firm inside it, and the Cottonwood bucket admits only a `-cot-` role. The CTO ruled (msg 8803) that the first Cottonwood publish is the issuer's cell in its own function. The pure functions it needs are `DB-b-279`'s, now in `publisher.py` on your branch.

**The cell (`DB-b-280`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p148_cothandler.py` (your three criteria; its fixture and fake S3 are the behavioural spec and name the constants and keys you must use); `infra/aws/lambda/investor-reporting/reporting-publish/handler.py` (the 49 Financial function: the listing, the parallel reads, the puts; read only, NOT imported); `infra/aws/lambda/investor-reporting/reporting-gold-cot/handler.py` (the Cottonwood report-build function: how `FIRM`, the floor and the path to the repo root are written; read only); `infra/aws/lambda/investor-reporting/reporting-publish/publisher.py` (your branch's version, with `build_series(rows, present_dates, calendar)`, `UNREPORTED_KEYS`, `validate_against_contract`).
2. **One new file** `infra/aws/lambda/investor-reporting/reporting-publish-cot/handler.py` (and its `tests/`). Module constants named EXACTLY: `FIRM = opal_naming.lookup("cottonwood")["key"]` (the registry, the one place the firm token appears, as the report-build handler does); `FLOOR_DAY = "2026-07-10"` (the landing and the report-build functions' floor; no earlier partition is listed for reading or read); `CONTRACT_REL = "org/standards/IRPT_DASHBD_SERIES_CONTRACT.json"`; and `_ROOT` (the bundle root: `_HERE` when `_HERE / "lib" / "trading_calendar.py"` exists, else `_HERE.parents[4]`; the same two lines as the report-build handler). Put `_ROOT / "infra/aws/lambda/investor-reporting/reporting-publish"` and `_ROOT / "lib"` on `sys.path` and import `opal_naming`, `publisher` and `trading_calendar` from there.
3. **`lambda_handler(event, context=None, s3=None)`**:
   - `upload = event.get("upload") is True` (the string "true" and 1 are NOT an upload: the default is a DRY RUN that reads and builds and writes nothing); `accounts` = an optional list of account-id strings in the event (restricts the set; ids not in the data are ignored).
   - FIRST read the contract at `_ROOT / CONTRACT_REL` and raise `SystemExit("REFUSED: ...")` BEFORE any S3 call when its `series.optional` does not name both `UNREPORTED_KEYS` (the Cottonwood series is never built against a contract that cannot carry the statement).
   - Create the S3 client (`boto3.client("s3", region_name="us-east-1")`) only when `s3` is None. The ONLY S3 calls are `get_paginator("list_objects_v2")`, `get_object`, `put_object(Bucket, Key, Body, ContentType)` and `head_object`.
   - List the gold table's objects under the prefix derived from `opal_naming.address("irpt", FIRM, "gold", "account_return_daily", "date=0000-00-00")` (the prefix is that key up to `/date=`), keep only `.parquet` objects in `date=YYYY-MM-DD` partitions with the day >= `FLOOR_DAY`; none -> `SystemExit("REFUSED: ...")`. Read the kept partitions on a bounded thread pool (12 workers), the columns `publisher.GOLD_COLUMNS` only, with pyarrow imported lazily inside the function. Group rows by `str(account_id)`; a row whose account id is null is counted (`skipped_null_account`) and never grouped.
   - For each named account: `series = publisher.build_series(rows, present_dates=<the sorted ISO dates of the kept partitions>, calendar=trading_calendar)`; `gz, _ = publisher.series_bytes(series)`; `manifest = publisher.build_manifest(account, FIRM, series, len(gz))`; `publisher.validate_against_contract(series, manifest, contract)` (a non-empty list is a `PublishRefused`). A `PublishRefused` is COUNTED by its reason text cut to 60 characters (the reason names no account) and the account is skipped; it never stops the run.
   - With `upload`: `put_object` the series (`publisher.SERIES_OBJECT`, `application/gzip`) and the manifest (`publisher.MANIFEST_OBJECT`, `application/json`) at `opal_naming.address("irpt", FIRM, "platinum", "reporting", "account=<id>", <object>)` (split into bucket and key; no key or bucket is typed anywhere), then `head_object` the series and raise `SystemExit("REFUSED: ...")` if its `ContentLength` differs from `len(gz)`. Without `upload` nothing is written and `head_object` is not called.
   - Return (and print once, as JSON, WITHOUT the `unreported_trading_days` list) exactly these keys: `ok` (true), `uploaded`, `floor`, `partitions`, `first`, `last`, `accounts_seen`, `accounts_named`, `published`, `refused`, `refusals` (reason text -> whole-number count), `skipped_null_account`, `unreported_trading_days` (the trading days from `FLOOR_DAY` to the last partition with no partition, ISO, sorted), `seconds`. NO account id is printed or logged anywhere: counts only.
   - Imports: the standard library, `boto3`, `pyarrow`, `opal_naming`, `publisher` and `trading_calendar` and nothing else (no pandas). No string literal in the file is a bucket name, an `s3://` uri or a key prefix; the word for the firm appears only as the argument of `lookup(...)`.
4. **Tests** `infra/aws/lambda/investor-reporting/reporting-publish-cot/tests/test_handler.py`, at least ten passing tests over a fake S3 and synthetic parquet only: the floor (a pre-floor partition is never read), the dry run (no put for an event with no `upload`, `False`, "true" or 1), the upload (exactly the series and manifest of each account that builds, at the builder's address), income null in the stored series, the unreported day listed, a refused account counted without its id, a null account id skipped, the account filter, the contract guard before any S3 call, the size read-back, and the summary keys. Name no real account or client value; use ids like `A0000000001`.
5. **Facts record** `RD_COT_PUBLISH_HANDLER_FACTS_R147.json` in your folder with EXACTLY these fields: `floor_day` ("2026-07-10"); `dry_run_default` (true); `upload_switch` ("event upload is exactly True"); `summary_keys` (the list of the keys in step 3); `reads_only_from_floor` (true); `tests` (the count of passing tests of your test file); `words` (one paragraph, 80 to 1800 characters: what the handler does, that a dry run is the default, and what is NOT proven: that it has run against the real bucket, which is a pair-gated act).

<criterion id="DB147-2-AC1" cell_refs="DB-b-280"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p148_cothandler.py" . DB147-2-AC1</invocation><expect>DB147-2-AC1 PASS</expect></criterion>
`DB147-2-AC1` -- on a fake S3 holding synthetic Cottonwood gold the two pre-floor partitions are never read; no event but `upload` exactly True writes; an upload writes exactly the series and manifest of the two accounts that build, at the builder's address; the stored income is null; the unreported day is listed; the account filter, the contract guard (before any S3 call) and the summary hold.
<criterion id="DB147-2-AC2" cell_refs="DB-b-280"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p148_cothandler.py" . DB147-2-AC2</invocation><expect>DB147-2-AC2 PASS</expect></criterion>
`DB147-2-AC2` -- every import is standard library, boto3, pyarrow, the publisher, the naming builder or the calendar; no string literal is a bucket, an `s3://` uri or a key prefix; the firm word appears only inside `lookup()`; the upload switch is tested with `is True`; no print names an account identifier.
<criterion id="DB147-2-AC3" cell_refs="DB-b-280"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r147/p148_cothandler.py" . DB147-2-AC3</invocation><expect>DB147-2-AC3 PASS</expect></criterion>
`DB147-2-AC3` -- your test file holds at least ten passing tests, the worker's commits change only the handler, its test file, the folder, the investigation file and task-order files, and the facts record equals the handler and the landing function's floor.

<expected_criteria>DB147-2-AC1,DB147-2-AC2,DB147-2-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: `publisher.py` (DB-b-279's, on your branch), the 49 Financial handler, the report-build handler, the contract, the issuer's check files.
- **Reads and writes.** Reads: repo files. No network, no AWS call, no deploy, no push, no invoke. Writes: the repo files of the grant and your private folder.
- **Client data.** None is involved; fixtures are synthetic.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker clause is wrong rather than your handler, file a BLOCKING row naming the clause and stop on it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W226-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/lambda/investor-reporting/reporting-publish-cot/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~226/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-280.cottonwood-series-publish-handler.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 145 (round 147, workstream B-49F + contract), cell `DB-b-280`.
<owned_cells>DB-b-280</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB147-2-AC1, DB147-2-AC2, DB147-2-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~226/IRPT_DASHBD.TO-DB-b-280.cottonwood-series-publish-handler.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB147-2-AC1,DB147-2-AC2,DB147-2-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the summary keys in one line; the test count; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a python file and its tests in a branch; nothing is deployed, invoked or served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; no AWS is read or written and no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its behaviour and discipline clauses were validated by the issuer against a scratch reference handler on a fake S3 (green) and 16 single-fault mutants of it (all red), and its grant and facts clauses by the self-test.
lane: the <paths> block IS the grant.
</preflight>
