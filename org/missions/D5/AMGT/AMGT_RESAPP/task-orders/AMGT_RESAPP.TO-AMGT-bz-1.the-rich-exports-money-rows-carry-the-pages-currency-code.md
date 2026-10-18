# AMGT_RESAPP task order -- `AMGT-bz-1` -- THE RICH EXPORT'S MONEY ROWS CARRY THE PAGE'S CURRENCY CODE THROUGH THE SAME READER THE PDF USES, AND STAY WITHHELD WHERE THE PAGE WITHHOLDS

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bz-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~517</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bz-1.the-rich-exports-money-rows-carry-the-pages-currency-code</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a renderer change and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut (2026-10-18): AC1 at the base fails (the test file is absent); AC2 at the base reads `1 failed, 249 passed` (the one known failure) and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (the tests build packs from committed fixtures; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-517` (branch `wk-AMGT_RESAPP-517`, cut from the issuance commit; its nested `portal/` is read-only and carries the page's source at `origin/DEV` `3a7791c1`, which you READ for the page's rule and never edit). Work and commit only in the outer worktree. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-517`.

**THREE ROUND-116 LESSONS THAT BIND YOUR TESTS.** (1) Two cells of this round edit `lib/research/print/render_pack.py` in different regions and are merged by the issuer; **a test of yours that compares a pack's WHOLE text to a recorded text fails the moment another cell's section lands.** Compare a SECTION (the lines between two headings) or the FIGURE lines (the `Appendix: model figures` block) or a named line, never the whole text. (2) Read `lib/research/print/tests/test_bw2_pack_form.py` and `test_bw1_currency_labels.py` first: they build a pack from committed fixtures with `build_pack` and read its text; copy their way, change nothing in them unless an assertion of theirs pins the exact old behaviour your cell changes: then re-scope that ONE assertion with a hand-written expectation, name it in the receipt (`## Tests re-scoped`: old and new), and the issuer re-runs the whole print plus api folders in the full tree after the merge. (3) A new check is dry-run at the base first: your test file runs ONCE on the unedited head and must fail on the new behaviour and pass on every control; record the counts.

**THE SERVED INPUTS (read-only fixtures; COPY them into `lib/research/print/tests/fixtures/` under the same names, your `<paths>` grants that folder):** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119_prep/fixtures/bx_served_thesis_RIO_LN.json`, `..._ICT_PM.json`, `..._GOOGL_US.json`. Each is the served `GET /thesis` body of `opal-amgt-scoped-api` for that name on 2026-10-18 (CodeSha256 `lNWo6Cm6..`), trimmed to `header_figures`, `dossier_fields`, `ai_fill`, `drafted_sections`, `drafting_*`, `posture`, `management`, `identity`. The pack route hands `build_pack` this bundle as `thesis_bundle`, and the model block carries the same `header_figures`; the existing bw fixtures show how a test assembles a block and a bundle. You call no AWS, no HTTP and no vendor.

**FOUR ROUND-117 LESSONS (in addition to the three above).** (a) **Name the proof instance by the order's FULL name:** `round-close-check` and the L6 gate look for `<to_id>.proof_of_spec.json`, `<to_id>` being the order file's name without `.md`; the path is under the limit (git `core.longpaths` is true), so never shorten it. (b) **Read your own pack's TEXT, not only your assertions:** render the three names' packs and read the sections you changed once before you write the receipt; a defect no fixture sees (an order of lines, a sentence that contradicts its neighbour) is found by reading. (c) **The regexes in your tests are raw strings:** a `\b` in a non-raw string is a backspace byte. (d) **A re-scoped test is named in the receipt with its old and new assertion;** the issuer re-runs the whole print plus api folders in the full tree after the merge and the baseline is `1 failed, 249 passed` in the print folder (the one known failure is `test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words`).

## 1. THE CELL -- `AMGT-bz-1` (round 119, decomposition s.128, item 1 of the CTO's round-118 analysis; row `AMGT_RESAPP-D1-W515-S3`)

**The ruling (CTO, round 118, section 3): the rich export's measured money rows carry the page's currency code.** Each money row prints the figure's own currency code through the SAME `_own_currency` reader the PDF uses; it is WITHHELD where the page withholds (an UNMEASURED basis prints the page's words `Bloomberg does not confirm this figure's currency`, never a code); a figure that carries no code is ambiguous to a reader of the export alone, and code-free rows would be the one place of the three surfaces where a figure's currency is not stated. Read row `AMGT_RESAPP-D1-W515-S3` in `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md` first.

**What is true today (measure it at Step A).** The rich export's Header table (`_figures_table` in `lib/research/print/render_pack.py`, around line 1541, and the `render_figure_line` it calls in `lib/research/provenance/render_print.py`, READ-ONLY for you) prints a money figure's amount, unit text and source with NO currency code: for example RIO LN's `PX_LAST` row renders a bare number although the figure carries `currency` `GBp`. Round 118 made the table withhold the four figures the page withholds (an UNMEASURED `currency_basis`); the other money rows are code-free.

**The rule to build:** for every money-unit figure the export prints (the Header table AND any fiscal-year or forecast table the export prints from figure objects: census them), (1) a figure whose `currency_basis` begins `UNMEASURED` stays withheld exactly as now; (2) a measured figure with an own served `currency` prints that code, read by the SAME `_own_currency` function the PDF pack uses (call it; do not copy it), in the pack's form: `<code> <amount> <unit words>` where the table's row form allows it, or the code in the row's own `Rendered` cell before the amount; (3) a measured figure with NO own currency prints `<amount> <unit words> currency not stated` (the pack's words); (4) every other row (ratios, percents, share counts, text, dates) is byte-identical to before. Edit the export's own table code only; do NOT edit `render_figure_line` or `render_print.py`: apply the code in `_figures_table` (a wrapper around the call) as round 118 did for the withheld rows.

**Do this in order.** (A) `cd C:/dev/wk-resapp-517`; `git log -1 --format=%h`; copy the eight fixtures; build the CENSUS TABLE first: for each money-unit figure of RIO LN, ICT PM and GOOGL US in the export, the served `currency`, the served `currency_basis`, what the export prints today and what it must print (hand-written from the rule); receipt `## Census` and the fixture `lib/research/print/tests/fixtures/bz1_rich_money_table.json`. (B) Write `lib/research/print/tests/test_bz1_rich_money_codes.py` FIRST and run it ONCE on the unedited head: record the counts. (C) Build the rule; re-run. (D) AC1, AC2, then READ the three names' exports once, then the receipt, instance (named by the order's FULL name) and proof-of-spec-check.

**Tests (`test_bz1_rich_money_codes.py`; hand-written expectations; models are the by-2 tests `test_by2_rich_export_rules.py`):** Z1 RIO LN: `PX_LAST` and `AVG_DAILY_VALUE_TRADED_3M` rows carry `GBp`; `Market cap`, `Net debt` and `Enterprise value` read the page's words and carry NO code and NO amount; Z2 ICT PM: `Market cap` carries `PHP`, `Enterprise value` carries `USD`, `Share price` carries `PHP`, `Net debt` withheld; Z3 GOOGL US (CONTROL for the withheld rule, USD for the rest): every money row carries `USD`; none is withheld; Z4 a synthetic MEASURED figure with a code prints it and one with no code prints `currency not stated`; Z5 the non-money rows of the three exports (ratio, percent, share count, text, date rows) are equal as a sorted multiset before and after; Z6 CONTROL: the PDF pack text of the three names is byte-identical before and after; Z7 the code printed for a row equals what `_own_currency` returns for that figure (the test calls `_own_currency` and compares).

**Region you own in `render_pack.py`:** `_figures_table` and any rich-export figure-table helper the census finds. You do NOT edit the pack (`pdf`) builders or the figure-line functions the PDF uses (`AMGT-bz-3` edits the appendix's source and definition sites; `AMGT-bz-2` edits the rich export's management section and the route's reader).

**THE SERVED INPUTS for round 119 (read-only fixtures; COPY into `lib/research/print/tests/fixtures/` under the same names, your `<paths>` grants that folder):** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119_prep/fixtures/bz_served_thesis_<NAME>.json` for `RIO_LN`, `ICT_PM`, `GOOGL_US`, `ICICIBC_IN`, `HD_US`, `BA_US`, `KMB_US` and `TSM_US` (the eight names the CVO reads), each the served `GET /thesis` body of `opal-amgt-scoped-api` for that name on 2026-10-18 ~11:4xZ (CodeSha256 `H3dCSGL..`), trimmed to `header_figures`, `dossier_fields`, `ai_fill`, `drafted_sections`, `drafting_*`, `posture`, `management`, `identity`. The existing `bx_served_thesis_*.json` fixtures (round 117) are the same shape for three of them.

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/print/render_pack.py` ONLY, and ONLY the region this cell names (two other cells edit other regions of the same file in parallel). Do NOT edit `lib/research/api/scoped_amgt.py`, `render_print.py`, `long_day.py` or the portal.
3. A served state sentence or reason the pack prints never carries a storage path, a bucket key, an object name, an order or cell id (`AMGT-...`) or an UPPER_SNAKE field code: say it in one plain sentence.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~517/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bz-1"><invocation>cd C:/dev/wk-resapp-517 &amp;&amp; timeout 300 python -m pytest lib/research/print/tests/test_bz1_rich_money_codes.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `7 passed` or more with 0 failed and 0 skipped, Z1 to Z7 each present by name, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bz-1"><invocation>cd C:/dev/wk-resapp-517 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 249 passed`), and the summary reads `1 failed, P passed` with P at least 255</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~517 <0.9.0_WK_AMGT_RESAPP~517@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~517/BZ1_RECEIPT.md` with the sections `## What changed` (every path, with line counts), `## Census` (the table the cell's Step A asks for, with its denominator), `## Tests re-scoped` (or `none`) and `## Not verified` (the deployed Lambda serves the old renderer until `AMGT-bx-5`; the whole api folder is not run in this sparse worktree: the issuer runs it in the full tree). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~517/AMGT_RESAPP.TO-AMGT-bz-1.the-rich-exports-money-rows-carry-the-pages-currency-code.proof_of_spec.json` (the invocations are recorded as the order's literal text; a re-run in another tree goes in `output_evidence` and `status_reason`, never in `invocation`). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W517-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate; round 116's rows S7 to S10 omitted it)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the census table; every existing test you re-scoped (old and new assertion); the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Item 1 of the CTO's round-118 analysis (`ledger/ROUND_ANALYSIS.round118.R1.md`, msg 8020) and its section-3 ruling; row W515-S3. LOCAL code cell; served only through `AMGT-bz-5`.

<status>complete</status>
<round>119</round>
<slot>0.9.0_WK_AMGT_RESAPP~517</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
