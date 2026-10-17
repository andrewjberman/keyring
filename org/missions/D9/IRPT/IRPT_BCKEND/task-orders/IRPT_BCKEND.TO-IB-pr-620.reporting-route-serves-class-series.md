# TO IRPT_BCKEND.TO-IB-pr-620 -- BUILD: the reporting route serves `which=class_series` (the contract 0.4.0 `class_object` file, one gzip object per account beside the series file), with the series file's gzip header; code and tests only, no deploy

<to_id>IRPT_BCKEND.TO-IB-pr-620</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~482</issued_to>
<issued_by>2.0.0_SA_COO~S2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>11</round>
<workstream>~PS</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `2.0.0_SA_COO~D2`'s msg 10645 (the series contract 0.4.0 is cut: `org/standards/IRPT_DASHBD_SERIES_CONTRACT.json`, section `class_object`, `files.class_series`, commit `a29424b8e9`), the un-park condition of my parked cell (drive log `org/tier1_exec/2.0.0_SA_COO~S2/drive_log_20261017T17Z_desktop-n8rjv0a.md`).

---

## WORKER FACE

**Cell `IB-pr-620` (inlined).** The reporting route `GET /api/scoped/investor-reporting/reporting/{account_id}/{which}` (function `irpt-49f-reporting-read-lambda`, code `infra/aws/lambda/investor-reporting/reporting/entry.py`) serves two members today, `series` (`series.json.gz`) and `manifest` (`manifest.json`), both from the platinum object `account=<raw id>/<name>` through `OBJECTS`. The contract 0.4.0 adds a third file written beside them by a later publisher cell: `class_series.json.gz`, gzip like the series file. Add it as the third member. **The scope test, the opaque-id mapping, the NOT_READY handling and every other line stay exactly as they are**; the IAM read grant already covers the whole prefix, so nothing outside this file and its tests changes.

**Edit `infra/aws/lambda/investor-reporting/reporting/entry.py`, two places, by exact string replacement (STOP and report if an old text is not found verbatim):**

1. OLD (one line, near line 88): `OBJECTS = {"series": "series.json.gz", "manifest": "manifest.json"}`
   NEW (three lines):
   `# class_series: the contract 0.4.0 class_object file (org/standards/IRPT_DASHBD_SERIES_CONTRACT.json, files.class_series), one gzip`
   `# object per account beside the series file, written by a later publisher cell; until it exists the member answers NOT_READY.`
   `OBJECTS = {"series": "series.json.gz", "manifest": "manifest.json", "class_series": "class_series.json.gz"}`
2. OLD (two lines, near line 299): `    elif which == "series":` followed by `        headers["Content-Encoding"] = "gzip"`
   NEW: `    elif which in ("series", "class_series"):` followed by the same `        headers["Content-Encoding"] = "gzip"` line.

Nothing else in `entry.py` changes: not `_check_version` (a `version_id` stays `series` only, so it is refused for `class_series`), not the docstrings, not any other route.

**Tests: add ONE new file `infra/aws/lambda/investor-reporting/reporting/tests/test_reporting_class_series.py`** (do not edit the existing three test files). Follow the pattern of `tests/test_reporting_entry.py` (read it: its `FakeS3`, `_key`, `_opaque`, `_call` helpers; copy what you need into the new file, do not import from it). At least 6 test functions, each named for what it proves, covering: (a) `serve_series(RAW, {RAW}, "class_series")` returns the stored bytes and its key ends `/account=<raw>/class_series.json.gz`; (b) the served operation answers 200 with `Content-Encoding: gzip`, the ETag and `Content-Type: application/json` and the body; (c) an uncovered account is refused (`AccountNotCovered`) with NO storage call; (d) `version_id` on `class_series` is refused (`ReportingBadRequest`); (e) a covered account with no `class_series` object is `ReportingNotReady`; (f) `manifest` still has no `Content-Encoding` and `series` still has gzip; (g) an unknown `which` is refused and the message lists `class_series`.

**Do, in this order. A STOP is reported to the issuer at once and writes nothing further.**
1. Make the two replacements and write the new test file. From `infra/aws/lambda/investor-reporting/reporting/` run `python -I -m pytest -q -p no:cacheprovider tests`: at least 39 passed (33 existed, six or more are new), no failure.
2. Run the three criteria below from the repository root (your worktree `C:/dev/wk-IRPT_BCKEND-482`); record each output and exit code verbatim in `IB251-1_criteria_output.txt` under `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~482/`.
3. Write the proof instance named under proof_of_spec, validate it with `python .tools/proof-of-spec-check.py <instance>`, commit with `.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~482 <0.9.0_WK_IRPT_BCKEND~482@opal.agent>" -F <msgfile> -- <explicit paths>` (the message file written with a file-writing tool), and flip this order to `complete` only if all three criteria PASS. Report once, under 150 words.

**Criteria (run each under `timeout 120` from the repository root):**

<criterion id="IB251-1-AC1" cell_refs="IB-pr-620"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r251/p251_cells.py" . IB251-1-AC1</invocation><expect>IB251-1-AC1 PASS</expect></criterion>
<criterion id="IB251-1-AC2" cell_refs="IB-pr-620"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r251/p251_cells.py" . IB251-1-AC2</invocation><expect>IB251-1-AC2 PASS</expect></criterion>
<criterion id="IB251-1-AC3" cell_refs="IB-pr-620"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~S2/checks/r251/p251_cells.py" . IB251-1-AC3</invocation><expect>IB251-1-AC3 PASS</expect></criterion>

<expected_criteria>IB251-1-AC1, IB251-1-AC2, IB251-1-AC3</expected_criteria>

What the checks grade: AC1 the reporting tests pass (39 or more) and the new test file holds six or more tests; AC2 the behaviour of the third member (key, gzip header, refusal before any storage call, `version_id` refused, NOT_READY, manifest and series unchanged, an unknown `which` refused naming `class_series`); AC3 only `entry.py` and the new test file differ from your branch point among source files, and the same behaviour run against the branch point's `entry.py` FAILS (the difference control).

## BOUNDS

- **Grant:** edit `infra/aws/lambda/investor-reporting/reporting/entry.py` (the two replacements only); create `infra/aws/lambda/investor-reporting/reporting/tests/test_reporting_class_series.py`; read anything in the repo; write your deliverables folder, the surprise channel and this order's status. **NO** other source file, **NO** AWS call, **NO** deploy, **NO** push, **NO** edit of `handler.py`, `publisher.py`, `sources.json`, the contract file or any `reporting-publish` file (they are `~D2`'s).
- **Refusal clause:** STOP and report if an old text is not found verbatim, if the existing 33 tests fail at your start, or if AC3 reports a file outside the two allowed ones.
- **Row ids** `IRPT_BCKEND-D2-W482-S<k>`. `surfaced_at` = `date -u +%FT%TZ` at filing. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~482/
infra/aws/lambda/investor-reporting/reporting/entry.py
infra/aws/lambda/investor-reporting/reporting/tests/test_reporting_class_series.py
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-620.reporting-route-serves-class-series.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 246 (round 11, workstream ~PS), cell `IB-pr-620`.
<owned_cells>IB-pr-620</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB251-1-AC1, IB251-1-AC2, IB251-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~482/IRPT_BCKEND.TO-IB-pr-620.reporting-route-serves-class-series.proof_of_spec.json` (the file stem of this order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a repo-only code and test change to one Lambda source file; no cloud resource is read or changed. The function takes the new code only through a later bundle apply (an IB2 order), which carries its own blast read.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission is changed; the read function's platinum read grant already covers the whole reporting prefix (reporting-read/locals.tf lines 44 to 48, read by the issuer).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is added: `which=class_series` is one more value of the existing route's path parameter.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p251_cells.py IB251-1 dry-run on dell2 2026-10-17 ~18:5xZ at the base: AC1 FAIL (no new test file), AC2 FAIL (OBJECTS has no class_series member); AC3 is graded in the worker's clean worktree (the issuer's tree carries other seats' uncommitted files).
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~482` in its own worktree. Class WORLD by the path floor (an infra/ path); a repo-only change.
</preflight>
