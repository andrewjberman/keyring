# AMGT_RESAPP task order -- `AMGT-bu-3` -- EVERY DATE THE PRINTED PACK SHOWS FROM A SERVED ISO DAY PRINTS IN THE HOUSE LONG FORM, THROUGH THE ESTATE'S ONE PYTHON HELPER `long_day`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bu-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~506</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bu-3.pack-dates-in-long-form</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one renderer edit and one test file.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut -- the printed PDFs of RIO LN and ICT PM (read 2026-10-17, `deliverables/2.0.0_SA_COO~R1/round113/READS_ITEM4.md`) carry 51 lines each with an ISO day; AC1 FAILS at the base (the new test file does not exist, exit 1). AC2 at the base reads the baseline below (9 failed, 1148 passed), so it is a REGRESSION guard (it PASSES at the base as expected).
EGRESS CLASS, declared: NONE (the tests build the pack from committed fixtures; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-506` (branch `wk-AMGT_RESAPP-506`, cut from the issuance commit; its nested portal worktree is cut at PROD `d1bed0fb` because the print tests read the portal fixture). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-506`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers about the wrong tree.

## 1. THE CELL -- `AMGT-bu-3` (round 114, decomposition s.123)

The CTO's ruling (round-113 analysis, item 2): ONE date rule for the page and its printed pack: every date a reader sees passes through the house long form (`September 28th, 2026`; ISO stays only in data fields no one reads). The page half is `AMGT-bu-2`. This cell is the PACK half. A read of two printed PDFs (RIO LN, ICT PM) found 51 lines each carrying an ISO day, in these shapes: `Printed 2026-10-17` (page 1); per-figure source lines such as `... - period ending 2026-12-31 - Bloomberg` (consensus estimates and forecasts, many per name); header and model figure lines ending `<ISO day> - Bloomberg`; and the earnings-dates line `latest <ISO day>; <N> dates on record` (`render_pack.py` around line 452). Your census may find more or fewer shapes: it is the authority.

**Step A, the census (a deliverable: the receipt's `## Date census` section and a committed fixture `lib/research/print/tests/fixtures/bu3_date_sites.json`).** Read `lib/research/print/render_pack.py` whole (1675 lines) and list EVERY place it formats or passes through a date or day for a reader: for each, the function and line, the served field it reads, whether it prints the served string directly (`bypass: true`) or already goes through a long-form helper, and its disposition (`fixed_here`, or `no_date_shown` with why). Print the denominator: the number of functions read and the number of sites. Read `lib/research/freshness/long_day.py` (the estate's one Python long-form helper: `long_day('2026-09-22')` returns `September 22nd, 2026`; a value that is not a date is returned as it came) and `lib/research/print/tests/test_ay1_dated_figures_and_served_thesis.py` (how a test builds a pack and reads the dated lines).

**Step B, the fix.** In `render_pack.py` ONLY (plus the new test and its fixtures): import `long_day` from `lib.research.freshness.long_day` (match how `render_pack.py` imports its other `lib.research` modules) and route EVERY `bypass: true` site through it, so no printed line carries a bare ISO day. A value that is not a bare day prints as it came. Display only: no served value, no sort key, no comparison and no `max(...)` over dates changes (the latest-earnings-date pick compares ISO strings and prints the long form of the winner). Do not reword any existing sentence; do not touch the rich-text export (`format=rich`) or any other module: report (do not edit) whether `lib/research/provenance/render_print.py`, `lib/research/api/scoped_amgt.py` or the `format=rich` path print an ISO day to a reader; name what you read.

**Existing tests that pin ISO text.** Some tests in `lib/research/print/tests/` and `lib/research/api/tests/` may assert an ISO day in the pack text. You update ONLY those, naming each in your report; a test you cannot explain as pinning a printed ISO day you do not touch.

**The grade is on the RENDERED pack text.** The new test `lib/research/print/tests/test_bu3_pack_long_dates.py` (YOURS: create it; model the pack build and the text read on `test_ay1_dated_figures_and_served_thesis.py`; read the PDF text with `fitz` (PyMuPDF) or `pypdf` where one imports and otherwise through the renderer's own pre-PDF line list, and say which in the report) checks, each named: T1 the rendered pack text of the committed ICT PM fixture contains NO match of `\d{4}-\d{2}-\d{2}` anywhere; T2 the same for the RIO LN fixture; T3 the page-1 `Printed` line reads `Printed <long form of run_date>` for a given `run_date` of `2026-10-17` (`Printed October 17th, 2026`); T4 a `period ending` source line and the earnings-dates line read their long forms exactly (expected strings written BY HAND from the fixture, never by importing `long_day` into the expectation); T5 a value that is not a bare day (for example `n/a`) in a dated slot prints as it came; T6 CONTROL: the pack text with every long-form date mapped back to ISO by a hand-written inverse (month name to number, strip the ordinal) equals the pack text RECORDED AT THE BASE HEAD, line for line: record the base text as `lib/research/print/tests/fixtures/bu3_pack_text_base_ICT_PM.txt` and `..._RIO_LN.txt` BEFORE the product edit (compare after normalising `\r\n` to `\n` on both sides: row S58); T7 the census fixture exists, its printed denominator equals its entry count, and no entry reads `bypass: true` with a disposition other than `fixed_here`. Fixtures: use the committed print-test fixtures for RIO LN and ICT PM if the existing tests have them; otherwise build them from `lib/research/print/tests/conftest.py`'s builders and say so.

**Do this in order.** (1) `cd C:/dev/wk-resapp-506` and confirm `git log -1 --format=%h` and `git status --short` (clean). (2) Write the census (Step A). (3) Create the test file FIRST with the base text fixtures and run it ONCE on the unedited head: it must fail on T1, T2, T3, T4 and pass on T5 and T6 (T7 passes only once the census holds no unfixed bypass: say how it reads); record that run. (4) Make the Step B edit. (5) Run AC1 and AC2. (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~506/BU3_RECEIPT.md` with the sections `## Date census`, `## What changed` (every path, with line counts), `## Tests that pinned ISO text` (each, or `none`) and `## Not verified` (the deployed Lambda serves the old renderer until `AMGT-bu-7`; a pack is not looked at here).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W506-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`.
2. `render_pack.py` is the only product file you edit. Standing: no S3 delete, no push of shared branches.
3. Commit nothing under `portal/` or `org/devices/`.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~506/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bu-3"><invocation>cd C:/dev/wk-resapp-506 &amp;&amp; timeout 300 python -m pytest lib/research/print/tests/test_bu3_pack_long_dates.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `7 passed` or more with 0 failed and 0 skipped, T1 to T7 each present by name, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bu-3"><invocation>cd C:/dev/wk-resapp-506 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests lib/research/api/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>the FAILED lines are exactly these nine, in any order, and no other: test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words; test_feed_and_names_an3.py::test_a_failed_gold_read_is_incomplete_never_an_empty_feed; test_fiscal_scope_contract.py::test_fiscal_figure_count_is_183_and_not_zero; test_fiscal_scope_contract.py::test_every_fiscal_figure_gets_a_check_and_none_is_dropped; test_generation_and_pool_routes.py::test_11_coverage_is_P1_over_the_association_keys_newest_first; test_generation_and_pool_routes.py::test_15_the_model_slice_is_the_landed_blocks_own_fiscal_rows; test_price_windows_route.py::test_the_30_day_and_default_reads_are_unchanged_beside_window_generations; test_r82_reason_and_mentions.py::test_4_feed_items_carry_mentions_order_and_membership_unchanged; test_r82_reason_and_mentions.py::test_5_a_name_with_no_count_keeps_the_absent_basis (measured by the issuer at the base: 9 failed, 1148 passed); and the summary reads `9 failed, P passed` with P at least 1155</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~506 <0.9.0_WK_AMGT_RESAPP~506@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~506/AMGT_RESAPP.TO-AMGT-bu-3.pack-dates-in-long-form.proof_of_spec.json`. Run `python .tools/proof-of-spec-check.py <instance>` on the committed bytes and report its verdict line. Do not stage `portal`.

Report once:
- the commit hash and the base;
- the test run at the unedited head (the line and the failing checks) and the run after;
- AC1's and AC2's output lines;
- the receipt's `## Date census` and `## Tests that pinned ISO text` sections, verbatim;
- what you read in `render_print.py`, `scoped_amgt.py` and the `format=rich` path;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-113 analysis for the R1 track (`ledger/ROUND_ANALYSIS.round113.R1.md`, msg 7763) item 2, pack half. LOCAL code cell (worker class `worker`); the pack is SERVED only through `AMGT-bu-7` (the `opal-amgt-scoped-api` redeploy: a CloudOps order under a never-widen pair, CLAUDE.md section 5; precedent gg-6 then gg-7), placed and cut after this cell merges. The baseline (9 failed, 1148 passed) was measured by the issuer on the shared tree at `27a3bc95f5`; the print folder alone reads 1 failed, 113 passed. `long_day` may not be in the Lambda's packaged closure: the bu-7 content-diff names it. Disjoint write surface from bu-1, bu-2 and bu-4 (all portal).

<status>pending</status>
<round>114</round>
<slot>0.9.0_WK_AMGT_RESAPP~506</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
