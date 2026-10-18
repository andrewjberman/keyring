# AMGT_RESAPP task order -- `AMGT-ca-3` -- THE RICH EXPORT PRINTS THE THESIS-PILLARS PASSAGE WHEREVER THE PDF PACK DOES, THROUGH THE SAME CLEARED-PASSAGE READER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-ca-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~522</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-ca-3.the-export-prints-the-thesis-pillars-passage-wherever-the-pdf-does</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a renderer change and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut (2026-10-18): AC1 at the base fails (the test file is absent); AC2 at the base reads `1 failed, 316 passed` (the one known failure) and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (the tests build packs from committed fixtures; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-522` (branch `wk-AMGT_RESAPP-522`, cut from the issuance commit; its nested `portal/` is read-only and carries the page's source at its `DEV` head at the cut, which you READ for the page's rule and never edit). Work and commit only in the outer worktree. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-522`.

**THREE ROUND-116 LESSONS THAT BIND YOUR TESTS.** (1) Three cells of this round edit `lib/research/print/render_pack.py` in different regions and are merged by the issuer; **a test of yours that compares a pack's WHOLE text to a recorded text fails the moment another cell's section lands.** Compare a SECTION (the lines between two headings) or the FIGURE lines (the `Appendix: model figures` block) or a named line, never the whole text. (2) Read `lib/research/print/tests/test_bw2_pack_form.py` and `test_bw1_currency_labels.py` first: they build a pack from committed fixtures with `build_pack` and read its text; copy their way, change nothing in them unless an assertion of theirs pins the exact old behaviour your cell changes: then re-scope that ONE assertion with a hand-written expectation, name it in the receipt (`## Tests re-scoped`: old and new), and the issuer re-runs the whole print plus api folders in the full tree after the merge. (3) A new check is dry-run at the base first: your test file runs ONCE on the unedited head and must fail on the new behaviour and pass on every control; record the counts.

**THE SERVED INPUTS (read-only fixtures; COPY them into `lib/research/print/tests/fixtures/` under the same names, your `<paths>` grants that folder):** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119_prep/fixtures/bx_served_thesis_RIO_LN.json`, `..._ICT_PM.json`, `..._GOOGL_US.json`. Each is the served `GET /thesis` body of `opal-amgt-scoped-api` for that name on 2026-10-18 (CodeSha256 `lNWo6Cm6..`), trimmed to `header_figures`, `dossier_fields`, `ai_fill`, `drafted_sections`, `drafting_*`, `posture`, `management`, `identity`. The pack route hands `build_pack` this bundle as `thesis_bundle`, and the model block carries the same `header_figures`; the existing bw fixtures show how a test assembles a block and a bundle. You call no AWS, no HTTP and no vendor.

**FOUR ROUND-117 LESSONS (in addition to the three above).** (a) **Name the proof instance by the order's FULL name:** `round-close-check` and the L6 gate look for `<to_id>.proof_of_spec.json`, `<to_id>` being the order file's name without `.md`; the path is under the limit (git `core.longpaths` is true), so never shorten it. (b) **Read your own pack's TEXT, not only your assertions:** render the three names' packs and read the sections you changed once before you write the receipt; a defect no fixture sees (an order of lines, a sentence that contradicts its neighbour) is found by reading. (c) **The regexes in your tests are raw strings:** a `\b` in a non-raw string is a backspace byte. (d) **A re-scoped test is named in the receipt with its old and new assertion;** the issuer re-runs the whole print plus api folders in the full tree after the merge and the baseline is `1 failed, 316 passed` in the print folder (the one known failure is `test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words`).

## 1. THE CELL -- `AMGT-ca-3` (round 120, decomposition s.129, item 3 of the CTO's round-119 analysis; carried from the CTO's `bz-5` half)

**The ruling (CTO, round-119 analysis section 4 item 3, quoted):** *"The thesis-pillars gap: the export prints the thesis-pillars passage wherever the PDF does, through the same cleared-passage reader. Grade: ICT PM, GOOGL US and ICICIBC IN match their PDFs."*

**What is true today (measure it at Step A, cite `path:line`).** The PDF pack prints a `Thesis pillars` section (`render_pack.py` `_print_thesis_pillars`, about line 1071, called at about line 1295) ONLY when `_pillars_gap_open(bundle)` is true AND `_cleared_passage(bundle, "thesis_pillars")` returns a passage: the machine-written block is SERVED, carries text from a served source class, and its validation is CLEARED with verdict PASS and a dated check; it prints the heading, the passage and the caption `_PAGE_CAPTION["thesis_pillars"]` (`Machine-written, not the research team's pillars.`) with its source label. The live rich export carries NO such section for ICT PM, GOOGL US and ICICIBC IN, where the PDF prints it. The export has its own drafted thesis section from the dossier (`build_rich_text`, find it): census what the export prints today for pillars and where.

**The rule to build.** The rich export prints a `## Thesis pillars` section, after the export's own summary section and before its risks section (the position the PDF has: Summary, Thesis pillars, Risks and considerations), whenever the PDF pack prints one: it calls the SAME `_pillars_gap_open` and `_cleared_passage` (and the pack's passage-label helper `_print_passage` or the function that builds its label lines: reuse it, do not copy it) with the SAME `thesis_bundle`, and prints the passage and its caption with their labels exactly as the PDF's words, in markdown (a heading, the passage as text, the caption line). Where the PDF prints no such section (the gap is not open, the block is not cleared, or the text is null), the export prints NOTHING for it: no heading, no placeholder. The export's existing drafted sections and tables are byte-identical to before.

**Do this in order.** (A) `cd C:/dev/wk-resapp-522`; `git log -1 --format=%h`; copy the eight fixtures; write `lib/research/print/tests/test_ca3_export_thesis_pillars.py` FIRST (tests below) and run it ONCE on the unedited head: record the counts. (B) THE CENSUS (receipt `## Census`, denominator printed): for each of the eight names, `_pillars_gap_open` (y/n), the `thesis_pillars` block's `status`, `source_class`, `validation.state`/`verdict`/`checked_at` and whether the PDF prints the section, and what the export prints for pillars today. (C) Build the rule; re-run. (D) AC1 and AC2, then READ the export of ICT PM, GOOGL US and ICICIBC IN once, then the receipt, instance (named by the order's FULL name) and proof-of-spec-check.

**Tests (`test_ca3_export_thesis_pillars.py`; hand-written expectations; build the PDF text with `build_pack` and the export with `build_rich_text` from the same fixture bundle, as `test_bz2_rich_management_equals_pdf.py` does):** P1 for ICT PM, GOOGL US and ICICIBC IN the export carries a `Thesis pillars` heading and the passage text and the caption line the PDF's `Thesis pillars` section carries (compare the PASSAGE and CAPTION text, markup stripped, never a whole text; a case per name); P2 for the five other names (RIO LN, KMB US, HD US, BA US, TSM US) neither the export nor the PDF carries a `Thesis pillars` heading (CONTROL, a case per name); P3 a copy of a printing name's bundle whose `thesis_pillars` block validation is not CLEARED prints no pillars section in the export and none in the PDF; P4 a copy whose block text is null the same; P5 CONTROL: the export's text outside the new section is unchanged: remove the new section's lines from the after text and the remainder equals the base text of the section list (record the base export of the three names by hand at Step A as fixtures); P6 the passage printed in the export is the one `_cleared_passage` returns (the test calls `_cleared_passage` and compares).

**Region you own in `render_pack.py`:** the export's thesis section in `build_rich_text` and one small helper beside it. You do NOT edit the PDF's `_print_thesis_pillars`, `_cleared_passage` or `_pillars_gap_open` (read-only: the PDF is the reference and stays byte-identical, with a control), the export's management section (`AMGT-ca-1`) or its figure tables (`AMGT-ca-2`).

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
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~522/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-ca-3"><invocation>cd C:/dev/wk-resapp-522 &amp;&amp; timeout 300 python -m pytest lib/research/print/tests/test_ca3_export_thesis_pillars.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `13 passed` or more with 0 failed and 0 skipped (P1 once per printing name, P2 once per control name, P3 to P6 each present by name), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-ca-3"><invocation>cd C:/dev/wk-resapp-522 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 316 passed`), and the summary reads `1 failed, P passed` with P at least 322</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~522 <0.9.0_WK_AMGT_RESAPP~522@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~522/CA3_RECEIPT.md` with the sections `## What changed` (every path, with line counts), `## Census` (the table the cell's Step A asks for, with its denominator), `## Tests re-scoped` (or `none`) and `## Not verified` (the deployed Lambda serves the old renderer until `AMGT-ca-5`; the whole api folder is not run in this sparse worktree: the issuer runs it in the full tree). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~522/AMGT_RESAPP.TO-AMGT-ca-3.the-export-prints-the-thesis-pillars-passage-wherever-the-pdf-does.proof_of_spec.json` (the invocations are recorded as the order's literal text; a re-run in another tree goes in `output_evidence` and `status_reason`, never in `invocation`). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W522-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate; round 116's rows S7 to S10 omitted it)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the census table; every existing test you re-scoped (old and new assertion); the proof verdict line; any row. The `<status>` flip is the issuer's.

## 6. AMENDMENT 1 (issuer, 2026-10-18 ~14:5xZ) -- ONE test repair, nothing else

**What happened.** Your merge (`dda778e2f8`) and the other two cells of the round (`ca-1` `a1eb3b86ce`, `ca-2` `f64668f0e8`) are in the shared tree. In the merged tree ONE test of yours fails: `lib/research/print/tests/test_ca3_export_thesis_pillars.py::test_P5_control_export_outside_the_pillars_section_equals_the_base_export[ICICIBC_IN]`. Its `## Header` section differs from your recorded base fixture `lib/research/print/tests/fixtures/ca3_base_export_ICICIBC_IN.md` on the two rows of the figures that carry no served source (`CURR_ENTP_VAL` and `SHORT_INT_RATIO`): the recorded base row ends with the middle dot U+00B7, a space, a question mark and a bar, and the export now prints `source not stated` in its place, which is `AMGT-ca-2`'s intended change (an absent, blank or `?` source prints `source not stated`). Your section edit did not move those rows: a control that compares another cell's region to a recorded base text fails the moment that cell lands (the round-116 lesson (1) above).

**What to do (your `<paths>` already grant the test and its fixtures again: this order is `pending`).** (1) `cd C:/dev/wk-resapp-522` (a NEW worktree cut from the shared head, which already carries all three cells; your earlier commits are inherited state, do not redo them). (2) Run the one failing test and the whole file ONCE and record the counts (expect `1 failed, 25 passed`). (3) Re-scope THAT ONE control with a hand-written expectation: before comparing a section, map each BASE line whose last cell ends with the four characters space, question mark, space, bar, preceded by the middle dot U+00B7 (copy the exact characters from the fixture: do not retype them; build the pattern in Python with `chr(183)`) to the same line with `source not stated` in place of the question mark, through a small named constant `CA2_BASE_TO_NOW_SOURCE` with a comment saying that `AMGT-ca-2` changed it on purpose; compare `now[heading]` to the mapped base. The map is applied to the base side only, to the lines of `## Header` and any other KEPT heading that carries such a row; every other line stays exactly compared. Do NOT edit the fixture, any product file, or any other test. (4) Re-run the file (all 26 pass) and the whole print folder ONCE (`1 failed` the known one, and at least 375 passed). (5) Commit in your worktree, update your receipt `CA3_RECEIPT.md` with a `## Amendment 1` section (old assertion, new assertion, the two counts), refresh your proof instance if its output text changed, run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report the verdict line and the commit.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Item 3 of the CTO's round-119 analysis (carried from the CTO's bz-5 half, `ledger/NEVER_WIDEN_ROUND119_..._CTO_HALF.md`); the gap measured by the issuer in the round-119 packet. The PDF is the reference and must stay byte-identical (P2 and P3 control it). LOCAL code cell.

<status>complete</status>
<round>120</round>
<slot>0.9.0_WK_AMGT_RESAPP~522</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
