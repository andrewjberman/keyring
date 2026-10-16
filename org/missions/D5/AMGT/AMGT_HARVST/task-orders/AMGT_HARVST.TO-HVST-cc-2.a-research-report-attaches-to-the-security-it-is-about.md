# AMGT_HARVST task order -- `HVST-cc-2` -- ROUND 88, workstream S29-ATTRIB: A RESEARCH REPORT ATTACHES TO THE SECURITY IT IS ABOUT, NOT THE FOLDER IT WAS FILED IN (D1-S29 defect 2; CTO round-87 analysis section 1 and ERRATUM 1 @74515c1f4a)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cc-2.a-research-report-attaches-to-the-security-it-is-about</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cc-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~151</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and tests, plus READ-ONLY S3 reads of the bucket `opal-data-harvest` in step 1 ONLY, through the repo shim `.tools/aws` (`s3api list-objects-v2` and `get-object` on named keys or prefixes; never `put`, `delete`, `copy`, `sync`, a recursive `cp` or a bare `aws` call). Budget: at most 150 GET requests and 60 MiB in all, counted in `measure.out`. NO deploy, NO Secrets Manager, NO publisher host, NO browser, NO scheduled task, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a guard written against an ASSUMED header shape instead of the measured one (so it never fires on the real report), a guard that fires on correct reports (a false positive that hides a real research list), a measurement of one security read as a census, and a test whose fixture is invented instead of copied from the measured header.
</preflight>

## 0. THE CELL

`harvest_get_research("KMB_US_Equity")` serves a report (`report_id` `fbd50086c4065785`, "Kimberly Clark Mexico Q2 2026 Earnings Update.docx", it carries "MAINTAIN 2.25% POSITION IN IDVZ") on KMB's list, so KMB reads as an IDVZ holding. The report is about Kimberly-Clark de Mexico (Bloomberg ticker `KIMBERA MM`), a different security. Mapped by a read-only agent: the report was filed in the library folder "Kimberly Clark KMB"; `lib/research/corpus/ingest.py::ingest` (line 135) takes `security_key = record["security_key"]` from the folder and stores every file in a RESOLVED folder under it; `lib/research/corpus/typed.py::record` (lines 403-462; `security_key` at 438) copies the bronze partition key into silver; `typed.reports_for` (576-582) and the gateway `infra/aws/ec2/opal-gateway/app/harvest_research.py::_research_reports` (lines 193-212, the filter at line 200) match on `security_key` alone. Nothing compares the report's own identity to the key. The harvest universe does NOT hold `KIMBERA MM` (live `harvest_resolve_security("KIMBERA MM")` answers `none`; 243 securities). The CTO ruled: **a research report attaches to a security by its exchange-qualified ticker, never by a name or ticker prefix; KMB's research list holds no KIMBERA report.** (ERRATUM 1: "KIMBERA MM's list holds it" cannot be tested, that security is not held; the report is recorded as MISFILED instead.)

## 1. THE WORK (LOCAL code and tests; step 1 reads S3, read-only)

Work in your worktree. Change only the files named in `<paths>`.
**Step 1 - MEASURE before you build (write `measure.out` in your deliverables folder).**
a. Read `harvest_research.py` lines 215-313 to find the exact S3 prefix of the silver `research_report` table and the fields a row carries (the issuer does not know them: find them, print the field list).
b. Print, for `KMB_US_Equity`, every silver research_report row for `report_id` `fbd50086c4065785`: ALL its stored fields, with any text field cut to 600 characters. Then print the same for 4 other KMB reports that are correctly KMB's.
c. A CENSUS over ALL securities: list the table prefix, read the parts (within the budget; if the whole table does not fit, read the newest partitions first and print what fraction you read as `parts_read` of `parts_total`), and for each row take the report's own identity from whatever the row stores (title, header text, fund, an exchange-qualified ticker such as `ABC US` or `KIMBERA MM`, matched by `\b[A-Z0-9]{1,8}\s(?:US|MM|LN|GY|FP|NA|JP|HK|CN|SW|IM|SM|AU|CH|KS|TT|SS|SP|BZ|SJ)\b`). End `measure.out` with ONE line, exact form: `MEASURE rows_scanned=<n> with_header_ticker=<n> mismatched=<n> parts_read=<n> parts_total=<n> gets=<n> bytes=<n>`, where `mismatched` counts rows whose header ticker is present and differs from the ticker of the row's `security_key`. Print the first 10 mismatched rows' ids so the reader can check them.
**Step 2 - BUILD the guard from what step 1 measured.**
d. In `lib/research/corpus/typed.py` (`record`) add a field `identity_check` with the value `"match"` (the report's own header ticker equals the key's ticker), `"mismatch"` (a header ticker is present and differs) or `"unknown"` (no header ticker found), computed by ONE pure function you define (name it `report_identity_check(security_key, header_text_or_fields)`) using the rule step 1 shows works on the measured headers; a mismatch also records `detected_ticker`. `reports_for` returns rows with `identity_check != "mismatch"` by default and a keyword `include_misfiled=True` returns all.
e. In `infra/aws/ec2/opal-gateway/app/harvest_research.py::_research_reports` skip a row whose `identity_check` is `"mismatch"`; if the silver rows carry the header/title fields (step 1 shows), ALSO compute the check on the fly with a copy of the same pure function when the row has no `identity_check` (so no silver rebuild is needed to fix what is served); if they do not carry them, do the stored-field check only and say in your note that a silver rebuild is owed. Add the skipped count to the tool's existing miss/note mechanism (read how `run.note` and `run.miss` are used) so a skipped report is NAMED, never silent: the served `research_reports` absence note reads e.g. `1 misfiled report(s) excluded (identity mismatch)`.
f. New tests (offline; no network): `lib/research/corpus/tests/test_cc2_report_identity.py` and `infra/aws/ec2/opal-gateway/tests/test_cc2_research_misfiled.py` (gateway fixtures follow `tests/test_og_gt4.py`; edit nothing in that file). Fixture header text is COPIED from `measure.out` (trim to what the rule reads, at most 400 characters; no invented header). Arms: (1) the measured Kimberly-Clark de Mexico report on `KMB_US_Equity` -> `mismatch` with `detected_ticker` `KIMBERA MM`, and the gateway KMB list excludes it with the exclusion named; (2) at least 5 correctly attributed measured headers -> `match` or `unknown`, NEVER `mismatch` (the false-positive control, from different securities); (3) an `unknown` row (no header ticker) is served, not dropped; (4) a row stored before this cell (no `identity_check`) and carrying a mismatching header is excluded by the on-the-fly check, and one carrying no header fields is served; (5) **A MUTANT:** with `report_identity_check` monkeypatched to always return `"match"`, arm (1) FAILS (assert that it does).
g. Do not write to S3 or run a deploy; do not edit any other file. A surprise is a row; keep working. If step 1 shows that the report's own text does NOT carry an identity the guard can read (no stored header, no ticker), STOP step 2, write that into `measure.out` and your final report, and file a row: that is a finding, not a failure.

<paths>
lib/research/corpus/typed.py
lib/research/corpus/tests/test_cc2_report_identity.py
infra/aws/ec2/opal-gateway/app/harvest_research.py
infra/aws/ec2/opal-gateway/tests/test_cc2_research_misfiled.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~151/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cc-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~151/measure.out</invocation><expect>(?m)^MEASURE rows_scanned=\d+ with_header_ticker=\d+ mismatched=\d+ parts_read=\d+ parts_total=\d+ gets=\d+ bytes=\d+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cc-2"><invocation>python -m pytest lib/research/corpus/tests/test_cc2_report_identity.py infra/aws/ec2/opal-gateway/tests/test_cc2_research_misfiled.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cc-2"><invocation>python -m pytest lib/research/corpus/tests/test_ingest.py lib/research/corpus/tests/test_backlog.py lib/research/corpus/tests/test_typed.py infra/aws/ec2/opal-gateway/tests/test_og_gt4.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. At the base AC1 and AC2 FAIL (the files do not exist). AC3 is the regression set (**issuer base count: 47 passed**, dell1, main tree, 2026-10-16 ~15:5xZ): run it BEFORE your change and record the passed count, then AFTER; both counts are in your final report and the passed count must not fall. (AC2 is run from the repo root with `python -m pytest`; the gateway test imports `app.*` the way `tests/test_og_gt4.py` does, so copy its `sys.path` lines. If a gateway test cannot run that way from the root, say so and run it with `bash infra/aws/ec2/opal-gateway/tests/run_release_suites.sh tests/test_cc2_research_misfiled.py ...` and put the output in your report.)
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W151-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. Its commit needs `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~151/AMGT_HARVST.TO-HVST-cc-2.a-research-report-attaches-to-the-security-it-is-about.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-cc-2.a-research-report-attaches-to-the-security-it-is-about` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-cc-2.a-research-report-attaches-to-the-security-it-is-about.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-87 analysis item 2 (b) as corrected by ERRATUM 1 (msg 6780). Close condition (REMEDIATION_v19): the surfacing seat reads KMB's research on the SERVED tool; this cell is LOCAL (plus read-only measurement), the deploy is `HVST-cc-7` (staged).
- **Why measure first (taxonomy law, rule 24(i)):** the issuer does not know what header fields a stored research row carries, nor how many securities have the same misfile; a guard written against an assumed shape would pass its own test and never fire on the real report. The worker's S3 reads are read-only and budgeted (150 GETs, 60 MiB) well under the 5 GiB-per-cycle egress bar of the runner (a different plane).
- **Mapped by a read-only agent** (2026-10-16 ~15:0xZ; not re-read line by line by the issuer except `harvest_identity.py` for cc-3): the folder "Kimberly Clark KMB" is in `lib/research/identity/data/universe_landed.json` line 1201; `crosswalk.harvester_key` (line 267) uses a substring match but the five pilots do not include Kimberly, so it is not the cause; no existing test covers a misfiled report.
- **NOT in this cell:** a silver REBUILD of any key; moving the KIMBERA report anywhere; adding `KIMBERA MM` to the universe (a universe decision, not this cell). The misfiled report stays in bronze under KMB's partition and is only excluded from KMB's served list and named.
- **Class (gate, spine v3.19 L6):** `<paths>` names `infra/aws/ec2/opal-gateway/app/...`, an infrastructure path, so the floor is WORLD and the order is declared WORLD (the first commit attempt declared LOCAL and was REFUSED by `to-pipeline-gate`). The worker's acts stay LOCAL (code and offline tests, no deploy); the deploy is `HVST-cc-7`. It is not a direct act: it takes the full limbs and its close is the issuer's real run, `HVST-cc-7`'s served read.
- Slot ~151, worktree `C:/dev/wk-harvst-151`, branch `wk-AMGT_HARVST-151`. Widen the sparse set at provision with `org/tier1_exec/4.0.0_SA_CRO/scripts`, `infra/aws/ec2/opal-gateway` and `lib/research`.
- **SENT:** with the round-88 issuance.

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>88</round>
<workstream>S29-ATTRIB</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
