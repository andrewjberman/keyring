# AMGT_RESAPP task order -- `AMGT-ca-2` -- A FIGURE WITH NO SERVED SOURCE, A BLANK ONE OR A BARE QUESTION MARK PRINTS `SOURCE NOT STATED`, IN THE APPENDIX AND IN THE EXPORT'S TABLES

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ca-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~521</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ca-2.a-blank-or-question-mark-source-reads-source-not-stated</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a renderer change and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut (2026-10-18): AC1 at the base fails (the test file is absent); AC2 at the base reads `1 failed, 316 passed` (the one known failure) and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (the tests build packs from committed fixtures; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-521` (branch `wk-AMGT_RESAPP-521`, cut from the issuance commit; its nested `portal/` is read-only and carries the page's source at its `DEV` head at the cut, which you READ for the page's rule and never edit). Work and commit only in the outer worktree. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-521`.

**THREE ROUND-116 LESSONS THAT BIND YOUR TESTS.** (1) Three cells of this round edit `lib/research/print/render_pack.py` in different regions and are merged by the issuer; **a test of yours that compares a pack's WHOLE text to a recorded text fails the moment another cell's section lands.** Compare a SECTION (the lines between two headings) or the FIGURE lines (the `Appendix: model figures` block) or a named line, never the whole text. (2) Read `lib/research/print/tests/test_bw2_pack_form.py` and `test_bw1_currency_labels.py` first: they build a pack from committed fixtures with `build_pack` and read its text; copy their way, change nothing in them unless an assertion of theirs pins the exact old behaviour your cell changes: then re-scope that ONE assertion with a hand-written expectation, name it in the receipt (`## Tests re-scoped`: old and new), and the issuer re-runs the whole print plus api folders in the full tree after the merge. (3) A new check is dry-run at the base first: your test file runs ONCE on the unedited head and must fail on the new behaviour and pass on every control; record the counts.

**THE SERVED INPUTS (read-only fixtures; COPY them into `lib/research/print/tests/fixtures/` under the same names, your `<paths>` grants that folder):** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119_prep/fixtures/bx_served_thesis_RIO_LN.json`, `..._ICT_PM.json`, `..._GOOGL_US.json`. Each is the served `GET /thesis` body of `opal-amgt-scoped-api` for that name on 2026-10-18 (CodeSha256 `lNWo6Cm6..`), trimmed to `header_figures`, `dossier_fields`, `ai_fill`, `drafted_sections`, `drafting_*`, `posture`, `management`, `identity`. The pack route hands `build_pack` this bundle as `thesis_bundle`, and the model block carries the same `header_figures`; the existing bw fixtures show how a test assembles a block and a bundle. You call no AWS, no HTTP and no vendor.

**FOUR ROUND-117 LESSONS (in addition to the three above).** (a) **Name the proof instance by the order's FULL name:** `round-close-check` and the L6 gate look for `<to_id>.proof_of_spec.json`, `<to_id>` being the order file's name without `.md`; the path is under the limit (git `core.longpaths` is true), so never shorten it. (b) **Read your own pack's TEXT, not only your assertions:** render the three names' packs and read the sections you changed once before you write the receipt; a defect no fixture sees (an order of lines, a sentence that contradicts its neighbour) is found by reading. (c) **The regexes in your tests are raw strings:** a `\b` in a non-raw string is a backspace byte. (d) **A re-scoped test is named in the receipt with its old and new assertion;** the issuer re-runs the whole print plus api folders in the full tree after the merge and the baseline is `1 failed, 316 passed` in the print folder (the one known failure is `test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words`).

## 1. THE CELL -- `AMGT-ca-2` (round 120, decomposition s.129, item 2 of the CTO's round-119 analysis; row `AMGT_RESAPP-D1-W519-S5`)

**The ruling (CTO, round-119 analysis section 4 item 2, quoted):** *"A source that is blank or '?' never prints as a source. The line reads 'source not stated'. Grade: a census of every source line across the 101 names, with any '?' listed."* The 101-name census is the ISSUER's read at the drain on the live pool; yours is the census of every PRINT SITE and the fixtures below. Read row `W519-S5` in `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md` first.

**What is true today (measure it at Step A, cite `path:line`).** A figure that carries NO `source` key (four figures in the eight fixtures: RIO LN `SHORT_INT_RATIO`, ICICIBC IN `CURR_ENTP_VAL` and `SHORT_INT_RATIO`, ICT PM `SHORT_INT_RATIO`) prints a bare `?` as its source in the pack's Appendix. The pack's own `_source_words(fig)` (`render_pack.py` about line 674) already reads a missing or blank source as `source not stated`, so the `?` is produced where the figure line is built: find where (the figure-line functions `_plain_figure_line` about line 563 and `render_figure_line` in `lib/research/provenance/render_print.py`, which is READ-ONLY for you). The rich export's figure tables print a source column: census whether they print `?` too.

**The rule to build.** Every print site of a figure's source, in the PDF Appendix and in the rich export's tables, prints `source not stated` when the figure's source is absent, blank (whitespace only) or exactly `?`. A real source (`Bloomberg`, `bloomberg-dapi`, any plain word) prints exactly as before; the `_plain_reason` mapping `AMGT-bz-3` built is unchanged. If the `?` is produced inside `render_print.py`, do NOT edit it: apply the rule in the pack's own wrapper around the call (hand `render_figure_line` a COPY of the figure whose `source` is the words `source not stated` when the source is absent, blank or `?`), as rounds 118 and 119 did for the withheld rows.

**Do this in order.** (A) `cd C:/dev/wk-resapp-521`; `git log -1 --format=%h`; copy the eight fixtures; write `lib/research/print/tests/test_ca2_source_not_stated.py` FIRST (tests below) and run it ONCE on the unedited head: record the counts. (B) THE CENSUS (receipt `## Census`, denominator printed): every site that prints a figure's source, in `render_pack.py` (PDF Appendix `Header` and every `Fiscal year <Y>` listing, and the rich export's tables): the function and line, what it prints BEFORE for a figure with no `source` key, with `source` `""`, with `?`, and with `Bloomberg`, and AFTER; plus the four named figures' printed line before and after. (C) Build the rule; re-run. (D) AC1 and AC2, then READ the three names' (RIO LN, ICICIBC IN, ICT PM) appendices once, then the receipt, instance (named by the order's FULL name) and proof-of-spec-check.

**Tests (`test_ca2_source_not_stated.py`; hand-written expectations):** S1 the four named figures print `source not stated` in the PDF Appendix and no `?` source (a case per figure); S2 a synthetic figure with `source` absent, one with `""`, one with `"   "` and one with `"?"` each print `source not stated` at EVERY site of the census (a parametrised case per site); S3 a figure with `source` `Bloomberg` and one with `bloomberg-dapi` print as before (CONTROL); S4 CONTROL: for the eight names the `Appendix: model figures` block differs from the base block ONLY on the lines of figures that had no served source (record the base blocks by hand at Step A as fixtures); S5 the rich export's tables print no `?` source for the eight names; S6 no line of the eight names' packs reads ` - ?` or ends in a bare `?` source.

**Region you own in `render_pack.py`:** the figure-line wrapper(s) and source helper(s) the PDF Appendix uses (`_plain_figure_line`, `_source_words`, `_withheld_line` and the source part of the lines they build) and the export's figure-table source column (`_figures_table` and its helpers). You do NOT edit `_ceo_profile_sentence`, the export's management section or the export's thesis-pillars section (`AMGT-ca-1`, `AMGT-ca-3`), `_plain_reason` itself, or `render_print.py`.

**THE SERVED INPUTS for round 120 (read-only fixtures; COPY into `lib/research/print/tests/fixtures/` under the same names if they are not there already, your `<paths>` grants that folder):** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119_prep/fixtures/bz_served_thesis_<NAME>.json` for `RIO_LN`, `ICT_PM`, `GOOGL_US`, `ICICIBC_IN`, `HD_US`, `BA_US`, `KMB_US` and `TSM_US` (the eight names the CVO reads), each the served `GET /thesis` body of `opal-amgt-scoped-api` for that name on 2026-10-18 ~11:4xZ, trimmed to `header_figures`, `dossier_fields`, `ai_fill`, `drafted_sections`, `drafting_*`, `posture`, `management`, `identity`. You call no AWS, no HTTP and no vendor. A synthetic input is built by COPYING a fixture's dict in the test and changing the one field the test is about.

**THE LIVE PACK TODAY (the base you change; CodeSha256 `VQ9zM6r4..`, release pin `2771164d0d`):** the PDF pack and the rich export both read ONE management object. The six names RIO LN, ICT PM, GOOGL US, ICICIBC IN, KMB US and TSM US serve `management.ceo_public_profile` as null, and `management.ceo_profile_reading` as `{reading: "UNREADABLE_OBJECT", reading_basis: "the object is not a dict", reason: null}`; HD US and BA US serve a dict `ceo_public_profile` (`status` ABSENT, a web-search `basis` sentence) read as `UNREADABLE_OBJECT` too. The PDF pack prints the CEO line as `CEO public profile: no public profile is on file yet.` for the six and HD US's own sentence for HD US; the export calls the same sentence builder since round 119.

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/print/render_pack.py` ONLY, and ONLY the region this cell names (two other cells edit other regions of the same file in parallel). Do NOT edit `lib/research/api/scoped_amgt.py`, `render_print.py`, `long_day.py` or the portal.
3. A served state sentence or reason the pack prints never carries a storage path, a bucket key, an object name, an order or cell id (`AMGT-...`) or an UPPER_SNAKE field code: say it in one plain sentence.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~521/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ca-2"><invocation>cd C:/dev/wk-resapp-521 &amp;&amp; timeout 300 python -m pytest lib/research/print/tests/test_ca2_source_not_stated.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `10 passed` or more with 0 failed and 0 skipped (S1 once per named figure, S2 once per census site, S3 to S6 each present by name), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ca-2"><invocation>cd C:/dev/wk-resapp-521 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 316 passed`), and the summary reads `1 failed, P passed` with P at least 322</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~521 <0.9.0_WK_AMGT_RESAPP~521@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~521/CA2_RECEIPT.md` with the sections `## What changed` (every path, with line counts), `## Census` (the table the cell's Step A asks for, with its denominator), `## Tests re-scoped` (or `none`) and `## Not verified` (the deployed Lambda serves the old renderer until `AMGT-ca-5`; the whole api folder is not run in this sparse worktree: the issuer runs it in the full tree). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~521/AMGT_RESAPP.TO-AMGT-ca-2.a-blank-or-question-mark-source-reads-source-not-stated.proof_of_spec.json` (the invocations are recorded as the order's literal text; a re-run in another tree goes in `output_evidence` and `status_reason`, never in `invocation`). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W521-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate; round 116's rows S7 to S10 omitted it)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the census table; every existing test you re-scoped (old and new assertion); the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Item 2 of the CTO's round-119 analysis; row W519-S5 (the `bz-3` worker's). The 101-name census of source lines is the issuer's read at the drain (`ca-4`, the live pool through the candidate handler); a worker's fixtures cannot see the whole pool. LOCAL code cell.

<status>complete</status>
<round>120</round>
<slot>0.9.0_WK_AMGT_RESAPP~521</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
