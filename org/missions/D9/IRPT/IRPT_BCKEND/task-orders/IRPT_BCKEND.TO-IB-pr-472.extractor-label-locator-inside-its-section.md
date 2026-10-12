# TO IRPT_BCKEND.TO-IB-pr-472 -- BUILD ONLY: the extractor locates a field label inside its OWN section's bounds on a page (two sections that share a label no longer land on one printed row)

<to_id>IRPT_BCKEND.TO-IB-pr-472</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~327</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>165</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6476 (PRD ADDENDUM v0.49 @6bed773b76, section 2 row D2-W324-S2 and section 3 item 4) | **Decomp cell:** `IB-pr-472` (decomposition section 157) | **outcome_ref:** FWD-4

---

## WORKER FACE

Root: `C:/dev/wk-irpt-bckend-327/` (bash `/c/dev/wk-irpt-bckend-327`). Work only there; `git rev-parse HEAD` before your first
commit is `base_commit` (state it).

**HARD BOUNDS.** BUILD ONLY. No AWS call, no vendor request, no sign-in, no Lambda invoked. Nothing is deployed. Every page, word and value in a test is
SYNTHETIC; no real report, client name or figure is read or written.

**Why.** `infra/aws/lambda/investor-reporting/ycharts/extract/extract.py`, function `extract` (about lines 655-668): for each census field row it
searches the census's hinted pages first, calls `_find_label(page["words"], row["field"])` and stops at the FIRST hit that has candidate values.
The census (`docs/briefs/sources/YCHARTS_COMPARISON_REPORT_FIELD_SCRAPE_20260909.json`) has S15 (title "Risk Info", page 10) and S16 (title
"Risk/Reward", page 10) each carrying a field "Standard Deviation". Both rows search page 10 for the same word run and each stops at its first
hit, so both can land on the SAME printed row and emit two section ids (`S15.standard_deviation.c<n>`, `S16.standard_deviation.c<n>`) for one
printed row, while the other printed row is never read. This is read from the source and the census only (row IRPT_BCKEND-D2-W324-S2); it
was not measured on a vendor PDF.

**Build (one thing).** A field's label is located INSIDE ITS OWN SECTION'S BOUNDS on a page: from the top of that section's heading (the census
section's `title`, found on that page as a word run, with the same normalisation `_find_label` uses) down to the top of the next section's heading on
that page, or the page bottom. Read `census_field_rows`, `classify_sections`, `_find_label` and the tests under
`infra/aws/lambda/investor-reporting/ycharts/extract/tests/` before you design it. Rules:
- If a section's heading cannot be found on a page, fall back to today's whole-page search for that section on that page, and COUNT the
  fallbacks (the record's `heading_fallbacks`). Never drop a field because its heading was not found.
- A label is located once per census row, as today. The page order (hinted pages first), the value rules (`_row_values`), the date rules and the
  section id format are UNCHANGED.
- The OUTPUT for every existing fixture under `ycharts/extract/fixtures/` (and any fixture a test builds) must be BYTE-IDENTICAL before and after
  (the section lists and unlocated lists). Measure it: hash the JSON-serialised result of `extract.extract(...)` over each existing fixture
  at `base_commit` and again after your change, with `sort_keys=True`; the two lists are in the record. If a fixture's output must change,
  STOP on that fixture, file a row and report; do not edit a fixture to make it match.

**Tests (the build's own):** `infra/aws/lambda/investor-reporting/ycharts/extract/tests/test_label_locator_sections.py`, at least THREE tests,
over a synthetic page built as a word list (no PDF is needed for these): (1) two sections that share a label on one page: each census row lands
on its own section's printed row, with the right column values; (2) a section whose heading is not on the page falls back to the whole page and
the fallback is counted; (3) the difference control: with the section bounds switched off (a module flag or the old call), the two rows land on the
SAME printed row. The fixture page's description is `both_labels_fixture` in the record: a path to the file in the tests folder that builds it
(or the fixture file itself). The folder reads `39 passed` at base; after, no failure and at least 42 passed.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~327/IB165-2_label_locator_record.json`: `{base_commit, files_changed,
section_bounds_rule (in words, at least a sentence), heading_fallbacks (a count over the existing fixtures), both_labels_fixture,
before_after: {fixtures_compared (an integer >= 1), before_sha256: [...], after_sha256: [...]} (equal lists of that length), hash_pins: [every place in the repo that pins a hash
of a file you changed, with what you did about it], request_sent: false, deployed: false}`. Package reach: the extractor ships inside a Lambda package; say which package
carries `extract.py` (read `infra/aws/lambda/ci/lambda-source-map.json` and the build manifest) in `host_reach`; nothing is built here.

<criterion id="IB165-2-AC1" cell_refs="IB-pr-472"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-2-AC1</invocation><expect>IB165-2-AC1 PASS</expect></criterion>
<criterion id="IB165-2-AC2" cell_refs="IB-pr-472"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-2-AC2</invocation><expect>IB165-2-AC2 PASS</expect></criterion>
<criterion id="IB165-2-AC3" cell_refs="IB-pr-472"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r165/p165_cells.py" . IB165-2-AC3</invocation><expect>IB165-2-AC3 PASS</expect></criterion>

<expected_criteria>IB165-2-AC1, IB165-2-AC2, IB165-2-AC3</expected_criteria>

What the checks grade: AC1 your new test file exists and at least 3 of its tests pass; AC2 the whole extract folder (`pytest infra/aws/lambda/investor-reporting/ycharts/extract`) reads no failure and at least 42 passed;
AC3 the record's form, that the before and after hash lists are equal, that the both-labels fixture exists, and that nothing outside the extract folder and your deliverables changed.

## BOUNDS

- **Grant:** the `<paths>` block and nothing else. No change to the census file, the font maps, the certifier or the publication module unless a test under your grant needs a read of them.
- **Refusal clause:** if the section bounds cannot be derived from the words a page carries, or an existing fixture's output must change, STOP, file a row and report; do not weaken a test or the hashes. Never weaken a check; do not edit `p165_cells.py`.
- **Row ids** are `IRPT_BCKEND-D2-W327-S<k>`; `surfaced_at` is `date -u +%FT%TZ` at filing; `grounding.status` is `GROUNDED` or `INFERRED`; append only, keeping the channel file's line endings byte for byte; check the id is free before you commit.
- **Commit with** `GIT_COMMITTER_NAME="0.9.0_WK_IRPT_BCKEND~327" GIT_COMMITTER_EMAIL="0.9.0_WK_IRPT_BCKEND~327@opal.agent" bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~327 <0.9.0_WK_IRPT_BCKEND~327@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool, OUTSIDE the worktree; do NOT pre-`git add`. ASCII only. Do not push.

<paths>
infra/aws/lambda/investor-reporting/ycharts/extract/extract.py
infra/aws/lambda/investor-reporting/ycharts/extract/tests/
infra/aws/lambda/investor-reporting/ycharts/extract/fixtures/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~327/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-472.extractor-label-locator-inside-its-section.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 157 (round 165, workstream ~P), cell `IB-pr-472`.
<owned_cells>IB-pr-472</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB165-2-AC1, IB165-2-AC2, IB165-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~327/IRPT_BCKEND.TO-IB-pr-472.extractor-label-locator-inside-its-section.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

**REPORT:** in your final message: the base; the section-bounds rule in a sentence; the three arms and the difference control; the number of existing fixtures compared and that the hash lists are equal; the heading fallbacks counted;
the extract suite's last line before and after; each criterion's last line; the proof checker's result; commit hashes; row ids.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell changes one extractor module and its tests in the repo; nothing is deployed, uploaded or invoked.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p165_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~18:0xZ: IB165-2 AC1 FAIL (the new test is absent), AC2 FAIL (39 passed, need >= 42), AC3 FAIL (no record); commit-gate clean. Measured by the issuer at base: pytest ycharts/extract reads 39 passed. The row's claim is from source and census only; whether a vendor PDF shows the double landing is unmeasured by the issuer.
lane: the <paths> block IS the grant. Class WORLD by the L6 floor (an infra path); nothing is deployed.
</preflight>
