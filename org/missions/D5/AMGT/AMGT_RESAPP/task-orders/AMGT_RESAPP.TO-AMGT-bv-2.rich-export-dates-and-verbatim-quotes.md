# AMGT_RESAPP task order -- `AMGT-bv-2` -- THE RICH EXPORT PRINTS ITS DATES IN THE HOUSE LONG FORM AND THE PACK AND THE EXPORT LEAVE EVERY VERBATIM SOURCE QUOTATION BYTE-FAITHFUL: A QUOTE CENSUS FIRST, THEN BOTH CHANGES, IN ONE RENDERER FILE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bv-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~509</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bv-2.rich-export-dates-and-verbatim-quotes</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; one renderer edit, one test file and fixtures.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut -- the live packs of eight names print no ISO day since round 114's `AMGT-bu-7`, but the `format=rich` export still does (`render_pack.py` `build_rich_text`: the `vintages <ISO timestamp>` Source line, each figure line's `as of <ISO vintage>`, forecast cells, served prose), and the pack's `_wrap` guard rewrites an ISO day inside ANY printed line, including a quoted source passage (BA, HD and KMB print quoted passages in the live packs). AC1 FAILS at the base (the new test file does not exist, exit 1). AC2 at the base reads `1 failed, 120 passed` (the one failure named below) so its expectation of P at least 125 is unmet there as expected: it is a regression guard plus a count.
EGRESS CLASS, declared: NONE (the tests build packs and exports from committed fixtures; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-509` (branch `wk-AMGT_RESAPP-509`, cut from the issuance commit). Work and commit only there. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-509`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers about the wrong tree.

## 1. THE CELL -- `AMGT-bv-2` (round 115, decomposition s.124)

The CTO's round-114 analysis, items 2 and 3 (`W506-S4` and `W506-S5`). Round 114's `AMGT-bu-3` routed every date the PRINTED PACK shows (the PDF and the plain-text pack, built by `build_pack`) through the estate's `long_day` (`lib/research/freshness/long_day.py`: `long_day('2026-09-22')` returns `September 22nd, 2026`; a non-date comes back unchanged) via a helper `_long_days` in `lib/research/print/render_pack.py`, called at eight sites, one of them inside `_wrap` (every printed title, heading and body line passes through it). **Read `lib/research/print/render_pack.py` around those call sites first, and the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~506/BU3_RECEIPT.md` (its `## Date census` and the rich-export table `X01` to `X10`).** Two things remain. (1) **`W506-S4`:** the `format=rich` export (`build_rich_text` and the builders it calls) still prints ISO days (the `vintages <ISO timestamp>` Source line and `thesis_bundle.generated_at`, each figure and forecast cell's `as of <vintage>` and `observed` segment from `render_print.render_figure_line` printed verbatim, and served prose). (2) **`W506-S5`:** the pack's `_wrap` guard rewrites an ISO day inside any printed line, including a VERBATIM SOURCE QUOTATION (a filing excerpt or an evidence passage the system prints as the source's own words). The CTO's ruling: rewriting the date format in system-served prose is in scope; a block printed as a verbatim quotation of a source stays BYTE-FAITHFUL, in the pack AND in the rich export.

**Step A, the quote census FIRST (a deliverable: the receipt's `## Quote census` section and a committed fixture `lib/research/print/tests/fixtures/bv2_quote_blocks.json`).** List EVERY block that `build_pack` (PDF and txt) AND `build_rich_text` print as a verbatim quotation of a source, as opposed to the system's own words or a served data field: for each, the function and line, what it prints, the served field it reads, whether it is a verbatim source quotation (`verbatim_source_quote: true` or `false` with the one-line reason), and `exempt` (true only for a verbatim source quotation). Method: read `_drafted_section_markdown` (around line 998: "block-quoted evidence passage per citation (verbatim passage text, its accession line)" and the `evidence`/`passage` reads around lines 1023-1033), `_print_drafted` and the pack's evidence printing, the officer, peer and posture builders, and every place a served `passage`, `quote`, `excerpt` or evidence text is printed; read each in context. Print the denominator (functions read, blocks listed). If the census finds NO verbatim source quotation, say so, change nothing for (2) and the row closes as not a defect; the live packs of BA, HD and KMB are known to print quoted passages, so expect some.

**Step B, the quote exemption (only for blocks the census marks `exempt: true`).** In `render_pack.py` ONLY: make the pack path and the rich export print an exempt block exactly as served (no `_long_days` over it), for example by routing the printing of those blocks around the `_wrap` rewrite with an explicit parameter (`verbatim=True` on the one call that prints them) and by never calling `_long_days` on their text in the rich builders. The rewrite stays on for everything else. Display only: no served value, sort key or comparison changes.

**Step C, the rich export's dates.** Route every date the rich export shows in a NON-quote line through `_long_days` (a bare day, a day inside served prose; a timestamp keeps its day only, as `_long_days` already does): the Source line's vintages and `generated_at`, `render_figure_line` output (do NOT edit `lib/research/provenance/render_print.py`: apply `_long_days` to its returned text inside `render_pack.py`), forecast cells, served reasons and descriptions. Do not reword any existing sentence. Report what `lib/research/api/scoped_amgt.py` does with the rich text (read only).

**The grade is on the RENDERED text.** The new test `lib/research/print/tests/test_bv2_rich_dates_and_quotes.py` (YOURS: create it; model the pack and export builds on `test_bu3_pack_long_dates.py`, which builds from the committed fixtures `lib/research/print/tests/fixtures/bu3_block_RIO_LN.json` and the ICT PM block it uses) checks, each named: Q1 the rich export of the committed RIO LN fixture contains NO match of `\d{4}-\d{2}-\d{2}` outside the blocks the census marks exempt; Q2 a fixture whose evidence passage embeds an ISO day (add it to your own fixture: for example the passage `... guidance for 2026-03-01 ...`) prints that passage BYTE-FAITHFUL in the PDF text, the txt pack and the rich export, while a system-served sentence beside it prints the long form; Q3 CONTROL for the export: the rich export text with every long-form date mapped back to ISO by a hand-written inverse (month name to number, strip the ordinal) equals the export RECORDED AT THE BASE HEAD, line for line after collapsing whitespace: record the base export as `lib/research/print/tests/fixtures/bv2_rich_text_base_RIO_LN.txt` BEFORE the product edit (compare after normalising `\r\n` to `\n` on both sides: row S58); Q4 CONTROL for the pack: `test_bu3_pack_long_dates.py` still passes when spawned by yours (7 passed); Q5 the census fixture exists, its printed denominator equals its entry count, and every entry with `exempt: true` has `verbatim_source_quote: true`. Expected strings are written by hand from the fixture, never by importing `long_day`. Use `fitz` (PyMuPDF) or `pypdf` for the PDF text where one imports, and say which; otherwise the renderer's own pre-PDF line list.

**Do this in order.** (1) `cd C:/dev/wk-resapp-509` and confirm `git log -1 --format=%h` and `git status --short` (clean apart from the `portal` link). (2) Write the census (Step A). (3) Create the test file FIRST with the base export fixture and run it ONCE on the unedited head: it must fail on Q1 and Q2 and pass on Q3, Q4 and (once the census file exists) Q5; record that run. (4) Make the Step B and Step C edits. (5) Run AC1 and AC2. (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~509/BV2_RECEIPT.md` with the sections `## Quote census`, `## What changed` (every path, with line counts), `## What scoped_amgt does with the rich text` and `## Not verified` (the deployed Lambda serves the old renderer until `AMGT-bv-5`; no live export is looked at here).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W509-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1` (a null `disarm_owner` is refused by the surprise-row gate).

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`.
2. `render_pack.py` is the only product file you edit; do NOT edit `lib/research/provenance/render_print.py`, `lib/research/freshness/long_day.py` or `scoped_amgt.py`. Standing: no S3 delete, no push of shared branches.
3. Commit nothing under `portal/` or `org/devices/`.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~509/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bv-2"><invocation>cd C:/dev/wk-resapp-509 &amp;&amp; timeout 300 python -m pytest lib/research/print/tests/test_bv2_rich_dates_and_quotes.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `5 passed` or more with 0 failed and 0 skipped, Q1 to Q5 each present by name, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bv-2"><invocation>cd C:/dev/wk-resapp-509 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 120 passed`), and the summary reads `1 failed, P passed` with P at least 125</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~509 <0.9.0_WK_AMGT_RESAPP~509@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~509/AMGT_RESAPP.TO-AMGT-bv-2.rich-export-dates-and-verbatim-quotes.proof_of_spec.json`. Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Report once:
- the commit hash and the base;
- the test run at the unedited head (the line and the failing checks) and the run after;
- AC1's and AC2's output lines;
- the receipt's `## Quote census` section, verbatim;
- what `scoped_amgt.py` does with the rich text;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-114 analysis for the R1 track (`ledger/ROUND_ANALYSIS.round114.R1.md`, msg 7824) items 2 and 3, in ONE cell because both change `render_pack.py` and the quote exemption interacts with the rich dates (disjoint write surface from `bv-1`, a portal candidate). LOCAL code cell (worker class `worker`); the exemption and the export are SERVED only through `AMGT-bv-5` (the `opal-amgt-scoped-api` redeploy: a CloudOps order under a never-widen pair, as `bu-7`), placed. AC2 is limited to the print test folder because a sparse worktree cannot run the whole api folder (row W506-S1); the issuer re-runs the combined print and api folders in the full tree at the drain (the baseline there is 9 failed, 1155 passed at 8225380445, the nine named in `bu-3`'s order). Q2 is the CTO's exemption made testable on a synthetic passage because no committed block carries a quoted passage with a date.

<status>complete -- worker ~509 (merged 6d4b263da2): lib/research/print/render_pack.py: the rich export's non-quote dates through _long_days, a _Verbatim line type so a source's own words are never rewritten, the day pattern digit-bounded (an accession number carries a day-shaped run); a quote census (37 functions, 30 blocks, 6 exempt: the filing-sentence blocks K05, K08, K10, K12 on the pack path and X06, X09 in the export) and the committed fixture bv2_quote_blocks.json. AC1 5 passed (worker); AC2 in the worker's sparse tree read 1 failed, 125 passed; THE ISSUER RE-RAN THE COMBINED print plus api folders in the full shared tree after the merge: exactly the nine named failures and 1160 passed (1155 plus the five new tests). FINDINGS: the pack path prints NO evidence passage (only the export does, X09), so the CTO's premise that the live packs of BA, HD and KMB print quoted passages is partly wrong: what they print is filing-sentence blocks (the filing's own sentence), which the census marks exempt as well; the base export's timestamps reduce to days, so its control compares days on both sides (row W509-S2); an accession number carries a day-shaped run, caught and fixed (row W509-S3). Not looked at: a live export or pack (the deployed Lambda serves the old renderer until AMGT-bv-5).</status>
<round>115</round>
<slot>0.9.0_WK_AMGT_RESAPP~509</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
