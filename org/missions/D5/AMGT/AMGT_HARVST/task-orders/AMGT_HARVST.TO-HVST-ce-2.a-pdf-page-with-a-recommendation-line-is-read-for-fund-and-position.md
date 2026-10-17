# AMGT_HARVST task order -- `HVST-ce-2` -- ROUND 90, workstream S43-FIX: A PDF PAGE THAT CARRIES A `Recommendation: ...` LINE IS READ FOR `fund_of_record` AND `last_stated_position`, NOT ONLY A PAGE THAT STARTS WITH THE LABEL (row D1-S43, W155-S1; CTO round-89 analysis item 1; measured by HVST-ce-1)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-ce-2.a-pdf-page-with-a-recommendation-line-is-read-for-fund-and-position</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-ce-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_HARVST~156</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 -- no schedule touched.
comp-iam: RUN at L5 -- LOCAL code and offline tests, plus READ-ONLY S3 reads of the bucket `opal-data-harvest` in step 2 ONLY (the census), through the repo shim `.tools/aws` (`s3api list-objects-v2` and `get-object` on named keys or prefixes; never `put`, `delete`, `copy`, `sync`, a recursive `cp` or a bare `aws` call). Budget: at most 800 requests and 500 MiB in all, counted in `ce2_census.out`. NO gold writer is RUN (`write_one`, `--write` and `production_sequence` are NEVER run by you), NO deploy, NO Secrets Manager, NO publisher host, NO browser, NO scheduled task, NO edit outside `<paths>`.
comp-adversary: RUN at L5 -- the adversary is a per-line rule that matches prose ("Our recommendations are ...", a line that merely contains the word), a rule that changes the docx path (THE CONTROL must stay byte-identical), a fix without the method-version bump (the gold writer NEVER overwrites: the same object name with different bytes raises `GoldImmutableError`, so the same method version would make every rebuild fail), a census that reads one security and calls it a population, and a test that passes whatever the code does.
</preflight>

## 0. THE CELL

`lib/research/corpus/continuation.py::_recommendation_candidates(items)` (lines 342-366) finds a report's RECOMMENDATION line by testing `_RECOMMENDATION_LABEL_RE` (line 132: `(?i)^\s*recommendation\s*:?\s*(.*)$`, applied as `.match(text.strip())`) against each LOCATOR's text. For a docx a locator is a paragraph; for a PDF it is a whole PAGE (`_locators_and_texts`, lines 262-274). A PDF page whose text does not START with the label is never read. Measured by `HVST-ce-1` (read it: `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~155/ce1_measure.out` sections (c) to (f), and `ce1_repro.py` beside it): `UNH_US_Equity`'s only report `48d81f053e5076e8` (class B, 2Q26, a PDF) has page 0 text `'1 \n \nUnitedHealth Group Incorporated (UNH-US) \n2Q26 earnings update \n \n \n \nRecommendation: Maintain positions in PFOE and DIVZ  \nUnitedHealth Group delivered a '` (the word starts at character offset 75; the page starts with the page number `1`). So the stored continuation reads `fund_of_record` and `last_stated_position` ABSENT while the silver row of the same report says fund `PFOE`. The CTO ruled: **if it is the rule's miss, fix it.** The module docstring section "RULED -- RECOMMENDATION-LINE RESOLUTION" (line 47) assumes a page that starts with the label; this cell amends it.

## 1. THE BUILD (LOCAL, about 90 product lines)

Work in your worktree. Change only the files named in `<paths>`.
a. In `lib/research/corpus/continuation.py`:
   - add a module constant `_PDF_LINE_RECOMMENDATION_RE = re.compile(r"(?im)^[ \t]*recommendation[ \t]*:[ \t]*(\S.*?)[ \t]*$")` (a LINE that starts with the word, then a COLON, then content on the same line; the colon is required; `.` does not cross a newline);
   - in `_recommendation_candidates`, keep the existing test exactly as it is; ONLY when it does not match AND `document.get("type") == "pdf"`, search the locator's text with `_PDF_LINE_RECOMMENDATION_RE`; if it matches, the content is `m.group(1)` and the content locator is the same page locator. Keep "one RECOMMENDATION line per report" (the first matching locator, and on it the first matching line, ends that report's search). A docx (and an xlsx or non-extractable document) takes the old path only: THE CONTROL, byte-identical behaviour;
   - bump `METHOD_VERSION` (line 127) from `"amgt-corpus-continuation/3"` to `"amgt-corpus-continuation/4"`. Read how the object name is built (lines 159-165 and 949): the name is a hash over the method version and the inputs, and the gold writer never overwrites, so WITHOUT the bump a rebuild of any security whose derivation changes would raise `GoldImmutableError`. Do NOT edit `dossier.py`;
   - amend the module docstring section "RULED -- RECOMMENDATION-LINE RESOLUTION" with a short paragraph (ASCII only): `AMENDED round 90 (CTO round-89 analysis item 1, ledger/ROUND_ANALYSIS.round89.md @fa28a5790e; measured by HVST-ce-1): a pdf page whose text does not start with the label is also read when it carries a LINE of the form "Recommendation: <content>" (colon required, content on the same line); a docx is unchanged.`
b. New test `lib/research/corpus/tests/test_continuation_pdf_recommendation_line.py`, offline, following the harness of `lib/research/corpus/tests/test_continuation.py` (read it first: how it builds `items` as `(row, document)` pairs and calls `_resolve_fund_and_position`; edit nothing in that file). Arms:
   - (1) THE MEASURED CASE: a pdf document whose page 0 text is exactly the string quoted in section 0 (copy it verbatim): `_recommendation_candidates` yields one candidate with content `Maintain positions in PFOE and DIVZ` and locator 0; `_resolve_fund_and_position` gives `fund_of_record` value `PFOE` and `last_stated_position` value text `Maintain positions in PFOE and DIVZ` with `fund` `PFOE` and `size_pct` None, each carrying a citation whose locator is 0;
   - (2) THE CONTROL: a pdf page that STARTS with the label (the old case, for example `"RECOMMENDATION: Maintain position in IDVZ ..."`) yields the same candidate as before and exactly ONE candidate for the report; a docx whose paragraph starts with `RECOMMENDATION` is read as before (copy an existing arm of `test_continuation.py` for the expected values);
   - (3) NO PROSE MATCH: pdf pages containing `"Our recommendations are summarised below."`, `"We repeat our recommendation of last quarter."`, a line `"Recommendation Maintain positions in PFOE"` (no colon) and a line `"Recommendation:"` with nothing after the colon: none yields a candidate, and the result is the absent reasons of today;
   - (4) the line may sit on any page and after other lines (page 2, the label line third), and the first matching page in the report's page order wins;
   - (5) `METHOD_VERSION == "amgt-corpus-continuation/4"`, and the object name built for one fixed input set differs from the name built under `"amgt-corpus-continuation/3"` (monkeypatch the constant, call the same name function);
   - (6) **A MUTANT:** with `continuation._PDF_LINE_RECOMMENDATION_RE` monkeypatched to a regex that never matches (`re.compile(r"(?!x)x")`), arm (1) FAILS (assert that it does).
   Update, in the existing test files of `lib/research/corpus/tests/`, ONLY an assertion that names the old method version string `amgt-corpus-continuation/3` (find them by reading the tests that failed after the bump); touch nothing else in them.
c. Do not run any gold writer; do not edit any other file. A surprise is a row; keep working.

## 2. THE CENSUS (read-only; the effect of the rule on the whole population)

Write `ce2_census.py` in your deliverables folder (start from `ce1_repro.py` beside `ce1_measure.out`) and run it once: for EVERY security in the silver research-report table (`amgt/harvest/silver/research-report/`, 5 parts; about 355 rows, 94 securities), fetch each row's extraction (`extract.v2.json` if it exists, else `extract.json`, from the row's `extract_key` directory), build `items` as `continuation.py` builds them (`_read_reports_with_bytes`, `typed.reports_for`), and run `_resolve_fund_and_position` twice: once with the code as it was before your change (`git show HEAD:lib/research/corpus/continuation.py` loaded as a second module) and once with your changed code. Write `ce2_census.out`: per security whose `fund_of_record` or `last_stated_position` DIFFERS between the two (value or absent), one line `CHANGED <security_key> fund_before=<value or absent> fund_after=<value or absent> position_before=<first 60 characters or absent> position_after=<first 60 characters or absent> report_id=<the report that supplied the new value>`; then, last, exactly one line `CENSUS securities=<n> changed_fund=<n> changed_position=<n> gets=<n> bytes=<n>` (`securities` is the number you ran, with its denominator against the 94 in the table; a security whose extraction could not be read is counted in a line `UNREADABLE <security_key> <reason>` and in `securities` only if it ran). Do not summarise: the issuer reads the CHANGED lines to judge whether the rule over-reaches.

<paths>
lib/research/corpus/continuation.py
lib/research/corpus/tests/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~156/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## PROOF OF SPEC (each invocation LITERAL)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-ce-2"><invocation>python -m pytest lib/research/corpus/tests/test_continuation_pdf_recommendation_line.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^\d+ passed in</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-ce-2"><invocation>python -m pytest lib/research/corpus/tests/test_continuation.py lib/research/corpus/tests/test_continuation_pillar_body.py lib/research/corpus/tests/test_continuation_reader_method.py lib/research/corpus/tests/test_continuation_terms.py lib/research/corpus/tests/test_dossier_method_bump.py lib/research/corpus/tests/test_substrate.py -q -p no:cacheprovider --color=no</invocation><expect>(?m)^53 passed in</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-ce-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~156/ce2_census.out</invocation><expect>(?m)^CENSUS securities=\d+ changed_fund=\d+ changed_position=\d+ gets=\d+ bytes=\d+$</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. **Dry-run at the base (issuer, dell1, 2026-10-17 ~15:5xZ):** AC1 FAIL as expected (the new test file does not exist); AC2 PASS as expected (`53 passed in 1.07s`); AC3 FAIL as expected (`cat` of a file that does not exist). If your worktree's base count differs, say so with both counts and do not weaken the pattern. The version bump may break an existing assertion that names `amgt-corpus-continuation/3`: fix it as step 1b says, and AC2 must read 53 again.
- **LINE ENDINGS:** edit so `git diff --stat` reads only the lines you changed; a whole-file diff is a defect. Check `git diff --stat` before you commit.
- A surprise row's `surfaced_at` is `date -u +%FT%TZ` at filing. Your next row id is `AMGT_HARVST-D1-W156-S1`. The channel file has MIXED line endings and is append-only: append a row by BYTES and check the diff reads only insertions. If the row gate refuses your commit on the pre-existing duplicate `AMGT_HARVST-Z-S106` pair, put `# surprise-row-override: pre-existing duplicate AMGT_HARVST-Z-S106 pair at HEAD (1.0.0_SA_CTO~DELL1 msg 1310); this commit adds only my row` in the message body.
- INSTANCE NAMED EXACTLY
  `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.9.0_WK_AMGT_HARVST~156/AMGT_HARVST.TO-HVST-ce-2.a-pdf-page-with-a-recommendation-line-is-read-for-fund-and-position.proof_of_spec.json`
  with `to_id` `AMGT_HARVST.TO-HVST-ce-2.a-pdf-page-with-a-recommendation-line-is-read-for-fund-and-position` and `decomp_ref.to_ref` `org/missions/D5/AMGT/AMGT_HARVST/task-orders/AMGT_HARVST.TO-HVST-ce-2.a-pdf-page-with-a-recommendation-line-is-read-for-fund-and-position.md`. Pin every artifact row to its commit.
  Run `python .tools/proof-of-spec-check.py <instance> --governing-order <that to_ref>` from the root of YOUR worktree and report its last line.
- Run every script from the repo root of YOUR worktree. Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:**
- Authority: CTO round-89 analysis (`ledger/ROUND_ANALYSIS.round89.md` @fa28a5790e, msg 7642) item 1 ("if it is the rule's miss, fix it, and prove it with the live gateway read of UNH showing fund PFOE plus a control name unchanged"); measured by `HVST-ce-1` (merged `0dfc96bdd1`, `CAUSE=rule_miss`); row `D1-S43`, worker row `D1-W155-S1` (ARMED, disarm owner `1.0.0_SA_CTO`).
- **This cell proves the RULE, not the served read.** The served read needs the gold objects REBUILT (`write_one`, a data write on the harvest bucket), which is `HVST-ce-4`'s (a seat order under its own never-widen pair, because it moves served output for every security the census lists). The lib code is not deployed to the gateway; the gateway only reads gold.
- **Why the census:** a never-widen sign-off names the blast radius and "N writers = N rules read" (CLAUDE.md section 5); the rebuild's scope is the census's CHANGED list, not UNH alone, and a rule that makes an over-reaching `last_stated_position` for many securities is a defect to find before the rebuild, not after. I read the CHANGED lines at the close. The census runs both rules on the same fetched inputs, so it writes nothing.
- **Method-version bump, named:** `amgt-corpus-continuation/3` to `/4`: gold objects are immutable and named by a hash over the method and the inputs; the bump is what lets a rebuild write a new beside the old (the gateway serves the newest). `dossier.py` is untouched; its inputs include the continuation member, so its object changes through its own inputs.
- **Class:** the gate decides; the first commit attempt declares LOCAL (`lib/` is not an infra path).
- Slot ~156, worktree `C:/dev/wk-harvst-156`, branch `wk-AMGT_HARVST-156`. Widen the sparse set at provision with `lib/research`, `.claude/agents` and `org/tier1_exec/4.0.0_SA_CRO/deliverables/RESEARCH_CORPUS_SCAN_20260922` (the KPI census file the pure derivation reads by a relative path; row `D1-W155-S3`).
- **SENT:** with the round-90 recut.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>90</round>
<workstream>S43-FIX</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
