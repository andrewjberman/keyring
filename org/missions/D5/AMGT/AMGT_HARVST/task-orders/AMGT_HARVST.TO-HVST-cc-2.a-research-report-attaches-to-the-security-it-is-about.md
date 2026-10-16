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

## AMENDMENT 1 (issuer, 2026-10-16T16:08:57Z; CTO ERRATUM 2 on `ledger/ROUND_ANALYSIS.round87.md`): STEP 1 IS DONE; STEP 2 IS A NAMED EXCLUSION LIST, NOT A TICKER GUARD

A prior pass of this order (worker `0.9.0_WK_AMGT_HARVST~151`, branch `wk-AMGT_HARVST-151`, commit `42a6ff937c`, which you inherit: read `deliverables/0.9.0_WK_AMGT_HARVST~151/measure.out` and the session log there first) MEASURED over all 355 silver research rows (5 of 5 parts, 94 securities, 11 GETs, 142,139 bytes) and found: a stored row carries NO ticker and NO header text, only `source_relpath` (`Kimberly Clark KMB/Kimberly Clark Mexico Q2 2026 Earnings Update.docx`), a `fund` and `fund_evidence`; a strict title-ticker rule would flag 22 rows that are other listings of ONE issuer (for example `PBR_US` against `PETR3 BZ`); the extraction body names Kimberly-Clark de Mexico SAB (KCM), not `KIMBERA MM`; KMB has a second row with the same title as a `.pdf` (`report_id` `1a3b56044db679a5`). So a ticker-attach guard cannot be built from what a stored row carries. **The CTO ruled (ERRATUM 2): serve a named exclusion list.** The list carries `(security_key, report_id, reason, optional correct_security_key)`; the gateway EXCLUDES a listed report from that security and NAMES it with its reason, so it is never silently dropped; where `correct_security_key` names a security in the universe, the report attaches there. KMB gets both Mexico files. No `typed.py` change and no silver rebuild: the rows stay as stored.

## 1. THE WORK (LOCAL code and tests; no S3 call at all in this pass)

Work in your worktree. Change only the files named in `<paths>`. Step 1 (the measurement, `measure.out`, AC1) is DONE in the inherited commit: do not redo it and do not call S3.
**Step 2 - BUILD the exclusion list.**
a. In `infra/aws/ec2/opal-gateway/app/harvest_research.py` add a module constant `MISFILED_REPORTS`, a tuple of dicts with the keys `security_key`, `report_id`, `reason` and `correct_security_key` (a string or None). It holds exactly two entries, both `security_key` `KMB_US_Equity` and `correct_security_key` None: `report_id` `fbd50086c4065785` (the `.docx`) and `1a3b56044db679a5` (the `.pdf`), `reason` `"Kimberly-Clark de Mexico SAB (KIMBERA MM) update filed in the 'Kimberly Clark KMB' library folder; KIMBERA MM is not in the harvest universe"`. A small function `_validate_misfiled(entries)` (called at import) raises `ValueError` on a missing key, a non-string `report_id`, an empty `reason`, or a `correct_security_key` that is neither None nor a string matching the module's key shape (`^[A-Za-z0-9_.\-]{1,96}$`).
b. In `_research_reports(run, rows, key)` (the filter at line 200): a row whose `(security_key, report_id)` is listed is NOT served on that security; for each one excluded, add an item to the response field `misfiled_reports_excluded` (a list of `{report_id, reason, correct_security_key}`; present, and `[]`, when none is excluded) AND say it in the tool's existing note mechanism (read how `run.note` and `run.miss` are used in `_research`), e.g. `2 misfiled report(s) excluded from KMB_US_Equity (see misfiled_reports_excluded)`; never silent. Where a listed entry's `correct_security_key` equals the key being served, the report IS served on this security from the ORIGINAL security's silver rows (read those rows the same way `_research` reads this key's rows) and its item carries `attached_from` (the original `security_key`). Keep the 6000-byte `research_reports` budget logic (`RESEARCH_BUDGET`) working: excluded items do not count against it.
c. New test `infra/aws/ec2/opal-gateway/tests/test_cc2_research_misfiled.py` (offline; fixtures follow `tests/test_og_gt4.py`: copy the helpers you need, edit nothing in that file). Arms: (1) a synthetic `KMB_US_Equity` partition holding the two listed report ids and two other reports: the served list holds only the other two, and `misfiled_reports_excluded` names both listed ids with their `reason`; (2) a security with no listed report: `misfiled_reports_excluded` is `[]` and its list is unchanged; (3) a synthetic pair of securities `TSTA_US_Equity` and `TSTB_US_Equity` and a listed entry (patched into `MISFILED_REPORTS` for the test) with `security_key` TSTA and `correct_security_key` TSTB: TSTA's list excludes the report and names it, TSTB's list includes it with `attached_from` `TSTA_US_Equity`; (4) the exclusion is never silent: the note text contains the number excluded and the key; (5) `_validate_misfiled` raises on each of the four bad shapes; (6) **A MUTANT:** with `MISFILED_REPORTS` monkeypatched to an empty tuple, arm (1) FAILS (assert that it does). Fixture ids and keys are synthetic EXCEPT the two real `report_id`s.
d. Do not write to S3 or run a deploy; do not edit any other file. A surprise is a row; keep working.
<paths>
infra/aws/ec2/opal-gateway/app/harvest_research.py
infra/aws/ec2/opal-gateway/tests/test_cc2_research_misfiled.py
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~151/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cc-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~151/measure.out</invocation><expect>(?m)^MEASURE rows_scanned=\d+ with_header_ticker=\d+ mismatched=\d+ parts_read=\d+ parts_total=\d+ gets=\d+ bytes=\d+$</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cc-2"><invocation>bash infra/aws/ec2/opal-gateway/tests/run_release_suites.sh tests/test_cc2_research_misfiled.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cc-2"><invocation>bash infra/aws/ec2/opal-gateway/tests/run_release_suites.sh tests/test_og_gt1.py tests/test_og_gt3.py tests/test_og_gt4.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^(16|18) passed in</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC1 already PASSES at the inherited commit (`MEASURE rows_scanned=355 ...`). **Dry-run at the base (issuer, dell1):** AC2 FAIL as expected (the new test file does not exist); AC3 PASS as expected (`16 passed`; the pattern admits `18` in case this pass's own new tests are collected by the regression command, which they are not: they are a separate file). If your worktree's base count differs, say so and do not weaken the pattern.
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
- **AMENDED 2026-10-16T16:08:57Z (issuer; CTO ERRATUM 2, msg 6843):** the worker stopped at the order's own gate (a stored row carries no ticker; the measurement is in `measure.out`), and the CTO ruled a named exclusion list. Criteria amended by the issuer (gate limb expected: GATE (viii) on a modify). The `typed.py` and corpus-test paths are dropped. The library filing error (the Mexico report filed under KMB) is a row for `4.0.0_SA_CRO~DELL1` (the issuer files it). Re-seat: the first worker is finished, so a fresh worker takes slot ~151 and inherits branch `wk-AMGT_HARVST-151`.
- **SENT:** with the round-88 issuance; re-sent 2026-10-16T16:08:57Z after the amendment.

**COMPLETE 2026-10-16T16:41:26Z (issuer `2.0.0_SA_COO~W1`):**
- **Acts:** worker `0.9.0_WK_AMGT_HARVST~151` (worker, haiku, high), two passes on branch `wk-AMGT_HARVST-151`. Pass 1 (`42a6ff937c`): the read-only measurement (`measure.out`: 355 rows, 94 securities, 5 of 5 parts, 11 GETs, 142,139 bytes; a stored row carries no ticker and no header text; a title-ticker rule would flag 22 rows that are other listings of one issuer) and a stop at the order's own gate. CTO ERRATUM 2 (msg 6843) ruled a named exclusion list; the order was amended by the issuer (`e3f05f3829`). Pass 2 (`cfa61fbc79`, `a312a860f5`), merged `44a1048df9` (safe-merge fast lane on the fourth attempt, after three lost races to other seats' commits and one refusal for an uncommitted foreign append to the channel file; index check 0 of 6 paths differ).
- **Diff read by this seat** (`harvest_research.py`, +85/-10): `MISFILED_REPORTS` holds the two KMB Mexico files (`fbd50086c4065785` docx, `1a3b56044db679a5` pdf) with their reason and `correct_security_key` None; `_validate_misfiled` runs at import; `_research_reports` excludes a listed report from its security, returns the excluded list, and serves a report on its `correct_security_key` from the original security's rows with `attached_from`; `_research` adds the response field `misfiled_reports_excluded`, a distinct absence note when every report of a key is excluded, and a sentence in `denominator_note` naming the number excluded and the key.
- **AC1 PASS:** `MEASURE rows_scanned=355 ... bytes=142139` (inherited). **AC2 PASS:** `6 passed` (worker; this seat re-ran), including the mutant arm (empty list) that fails arm 1. **AC3 PASS:** `16 passed` (re-run here). Proof instance VALID rc 0 (re-run here).
- **Rows:** pass 1 `D1-W151-S1` (BLOCKING, ARMED: the ticker guard cannot be built from a stored row; answered by the ruled exclusion list), `-S2` (the strict rule flags 22 same-issuer rows), `-S3` (ARMED: KMB's second row, the .pdf, now listed); pass 2 `-S4` (the order's next-row-id was stale), `-S5` (`run.note` carries no text, so the exclusion note went to `denominator_note`). The issuer files the dispositions after the round's merges; `D1-S33` names the library filing error for `4.0.0_SA_CRO~DELL1`.
- **What this does NOT prove:** the served tool. The exclusion is merged, not deployed; the served read of KMB's research is `HVST-cc-7`. It is exact and does not generalise: a new misfile is a new list row, and the ticker-attach the first ruling named is not buildable from stored rows. A silver rebuild is not owed (the rows stay as stored).

<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<round>88</round>
<workstream>S29-ATTRIB</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
