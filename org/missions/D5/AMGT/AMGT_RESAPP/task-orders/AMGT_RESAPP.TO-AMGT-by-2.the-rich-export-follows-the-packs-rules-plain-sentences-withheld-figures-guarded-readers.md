# AMGT_RESAPP task order -- `AMGT-by-2` -- THE RICH EXPORT FOLLOWS THE PACK'S RULES IN FULL: PLAIN SENTENCES, THE FIGURES THE PAGE WITHHOLDS WITHHELD, AND EVERY READER GUARDED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-by-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~515</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-by-2.the-rich-export-follows-the-packs-rules-plain-sentences-withheld-figures-guarded-readers</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a renderer change and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut (2026-10-18): AC1 at the base fails (the test file is absent); AC2 at the base reads `1 failed, 189 passed` (the one known failure) and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (the tests build packs from committed fixtures; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-515` (branch `wk-AMGT_RESAPP-515`, cut from the issuance commit; its nested `portal/` is read-only and carries the page's source at `origin/DEV` `3a7791c1`, which you READ for the page's rule and never edit). Work and commit only in the outer worktree. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-515`.

**THREE ROUND-116 LESSONS THAT BIND YOUR TESTS.** (1) Two cells of this round edit `lib/research/print/render_pack.py` in different regions and are merged by the issuer; **a test of yours that compares a pack's WHOLE text to a recorded text fails the moment another cell's section lands.** Compare a SECTION (the lines between two headings) or the FIGURE lines (the `Appendix: model figures` block) or a named line, never the whole text. (2) Read `lib/research/print/tests/test_bw2_pack_form.py` and `test_bw1_currency_labels.py` first: they build a pack from committed fixtures with `build_pack` and read its text; copy their way, change nothing in them unless an assertion of theirs pins the exact old behaviour your cell changes: then re-scope that ONE assertion with a hand-written expectation, name it in the receipt (`## Tests re-scoped`: old and new), and the issuer re-runs the whole print plus api folders in the full tree after the merge. (3) A new check is dry-run at the base first: your test file runs ONCE on the unedited head and must fail on the new behaviour and pass on every control; record the counts.

**THE SERVED INPUTS (read-only fixtures; COPY them into `lib/research/print/tests/fixtures/` under the same names, your `<paths>` grants that folder):** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round117_prep/fixtures/bx_served_thesis_RIO_LN.json`, `..._ICT_PM.json`, `..._GOOGL_US.json`. Each is the served `GET /thesis` body of `opal-amgt-scoped-api` for that name on 2026-10-18 (CodeSha256 `lNWo6Cm6..`), trimmed to `header_figures`, `dossier_fields`, `ai_fill`, `drafted_sections`, `drafting_*`, `posture`, `management`, `identity`. The pack route hands `build_pack` this bundle as `thesis_bundle`, and the model block carries the same `header_figures`; the existing bw fixtures show how a test assembles a block and a bundle. You call no AWS, no HTTP and no vendor.

**FOUR ROUND-117 LESSONS (in addition to the three above).** (a) **Name the proof instance by the order's FULL name:** `round-close-check` and the L6 gate look for `<to_id>.proof_of_spec.json`, `<to_id>` being the order file's name without `.md`; the path is under the limit (git `core.longpaths` is true), so never shorten it. (b) **Read your own pack's TEXT, not only your assertions:** render the three names' packs and read the sections you changed once before you write the receipt; a defect no fixture sees (an order of lines, a sentence that contradicts its neighbour) is found by reading. (c) **The regexes in your tests are raw strings:** a `\b` in a non-raw string is a backspace byte. (d) **A re-scoped test is named in the receipt with its old and new assertion;** the issuer re-runs the whole print plus api folders in the full tree after the merge and the baseline is `1 failed, 189 passed` in the print folder (the one known failure is `test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words`).

## 1. THE CELL -- `AMGT-by-2` (round 118, decomposition s.127, item 2 of the CTO's round-117 analysis; STARTS AFTER `AMGT-by-1` IS MERGED)

**The ruling (CTO, round 117, section 2):** the rich export is the same document in another format and follows the pack's rules in full: (1) no storage path, key, order id or vendor error in any line; every served reason goes through the ONE plain-sentence mapper `_plain_reason` that `AMGT-by-1` built (it is in your tree: read it first and reuse it; build no second one); (2) currency by the page's rule: a header money figure the page withholds (a served `currency_basis` beginning `UNMEASURED`) prints the page's words `Bloomberg does not confirm this figure's currency` and NO amount in the export's Header figure table (row `AMGT_RESAPP-D1-W513-S1`: the table renders `render_figure_line` verbatim and prints the raw amount); (3) every reader the rich route calls is guarded: a raising reader is an absent input, one warning line is logged through the module's channel, and the section prints its absence sentence (row `AMGT_RESAPP-D1-W511-S9`: the `format=rich` branch of `scoped_amgt.py` `_print_pack` reads the thesis bundle, the peer set and the posture unguarded, so a raising reader fails the whole export). Row `AMGT_RESAPP-D1-W512-S4` is the same family: the census of round 117 found the export printing served reasons with storage paths and vendor error text, and its pinned tests are outside round 117's re-scope. Read the four rows (ids above, in `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md`) first.

**Your tree** is the merged head (it carries `AMGT-by-1`'s `_plain_reason` and census, your branch was cut from it). The rich export is `build_rich_text` and its helpers in `render_pack.py` (`_figures_table`, `_drafted_section_markdown`, `_model_cases_markdown`, ...), the route is `format=rich` in `scoped_amgt.py` `_print_pack` (the PDF branch was guarded in round 116: copy its way, read how it reports a failed reader), and `render_figure_line` in `lib/research/provenance/render_print.py` renders a figure line (READ-ONLY for you: do not edit `render_print.py`; withhold in the export's own table code, before the call).

**The rules to build.** (1) Every site of `by-1`'s census marked surface `rich` (read the receipt `deliverables/0.9.0_WK_AMGT_RESAPP~515/BY1_RECEIPT.md`, `## Census`) goes through `_plain_reason` with its own fixed sentence. (2) The Header figure table of the export withholds exactly the figures the PAGE withholds: a figure whose `currency_basis` begins `UNMEASURED` and whose unit is a money unit prints `<label>: Bloomberg does not confirm this figure's currency` with no amount, in the table's own row form; every other row is unchanged (the pack already has the one withheld test: reuse it). (3) Guard each of the three reads in the `rich` branch separately, as the PDF branch does. (4) The export's currency-labelled text (`_model_cases_markdown` and the table) names no currency code the figure does not carry.

**Do this in order.** (A) `cd C:/dev/wk-resapp-515`; confirm `git log -1 --format=%h` is the merged head; copy the three fixtures; write `lib/research/print/tests/test_by2_rich_export_rules.py` and `lib/research/api/tests/test_by2_rich_route_degrades.py` FIRST and run them ONCE on the unedited head: record the counts. (B) The census of the export: every line shape the export prints from a served reason, status or error, and every money figure line, before and after (receipt `## Census`, denominator printed). (C) Build rules (1) to (4). The two print test files that pin the export's old wording (the AMGT-av and AMGT-rl tests the earlier row named): re-scope ONLY the assertions that pin a raw reason or a raw withheld amount, each with a hand-written expectation, and name each in the receipt (`## Tests re-scoped`, old and new). (D) AC1 to AC3, read the three names' exports once, then the receipt, instance and proof-of-spec-check.

**Tests.** `test_by2_rich_export_rules.py`: R1 RIO LN: the export's Header table has NO line carrying the amounts `115,578.9`, `14,512.0` or `173,616.0` (or their raw forms) and the three lines `Market cap`, `Net debt`, `Enterprise value` read the page's words; R2 ICT PM: `Net debt` withheld, `Market cap` prints `PHP`, `Enterprise value` prints `USD`; R3 GOOGL US CONTROL: every money row is byte-identical to the base; R4 a bundle whose reasons carry `s3://opal-data-harvest/x/y.json` and `AMGT-rj-11 has not landed one` yields an export with neither string, in every section; R5 the export of each of the three names has no `s3://`, no `AMGT-`, no `NoSuchKey`, no ISO day and no UPPER_SNAKE token outside a figure's own `mnemonic` column (state which columns of the table legitimately carry a mnemonic and test that); R6 CONTROL: the pack PDF text of the three names is byte-identical before and after (this cell changes the export only). `test_by2_rich_route_degrades.py` (model `test_bw4_print_pack_degrades.py`): R7 with `read_thesis_bundle` raising, the rich route still returns the markdown (status 200) and the thesis-fed section reads an absence sentence; R8 the same with `read_peer_set` raising, R9 the same with `read_posture` raising, R10 with all three raising the export's figure table equals the all-served export's, R11 a raising reader is logged once through the module's channel, R12 CONTROL: all served, the export equals `build_rich_text` with the same objects.

**Region you own:** the rich-markdown helpers in `render_pack.py`, the `rich` branch of `_print_pack` in `scoped_amgt.py`, and the tests above. You do NOT edit the pack (`pdf`) builders, `_plain_reason`, `render_print.py` or any other function of `scoped_amgt.py`.

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/print/render_pack.py` ONLY, and ONLY the region this cell names (two other cells edit other regions of the same file in parallel). Do NOT edit `lib/research/api/scoped_amgt.py`, `render_print.py`, `long_day.py` or the portal.
3. A served state sentence or reason the pack prints never carries a storage path, a bucket key, an object name, an order or cell id (`AMGT-...`) or an UPPER_SNAKE field code: say it in one plain sentence.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/api/scoped_amgt.py
lib/research/print/tests/
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~515/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-by-2"><invocation>cd C:/dev/wk-resapp-515 &amp;&amp; timeout 500 python -m pytest lib/research/print/tests/test_by2_rich_export_rules.py lib/research/api/tests/test_by2_rich_route_degrades.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `12 passed` or more with 0 failed and 0 skipped, R1 to R12 each present by name, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-by-2"><invocation>cd C:/dev/wk-resapp-515 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 189 passed`), and the summary reads `1 failed, P passed` with P at least 203</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~515 <0.9.0_WK_AMGT_RESAPP~515@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~515/BY2_RECEIPT.md` with the sections `## What changed` (every path, with line counts), `## Census` (the table the cell's Step A asks for, with its denominator), `## Tests re-scoped` (or `none`) and `## Not verified` (the deployed Lambda serves the old renderer until `AMGT-bx-5`; the whole api folder is not run in this sparse worktree: the issuer runs it in the full tree). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~515/AMGT_RESAPP.TO-AMGT-by-2.the-rich-export-follows-the-packs-rules-plain-sentences-withheld-figures-guarded-readers.proof_of_spec.json` (the invocations are recorded as the order's literal text; a re-run in another tree goes in `output_evidence` and `status_reason`, never in `invocation`). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W515-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate; round 116's rows S7 to S10 omitted it)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the census table; every existing test you re-scoped (old and new assertion); the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Item 2 of the CTO's round-117 analysis and its section-2 ruling. Depends on `AMGT-by-1` (the mapper): the one worker slot ~515 runs `by-1`, the issuer merges it, then the same slot is re-seated for this order on the merged tree. The rich export is read by the CVO at L9 after `by-5`. LOCAL code cell.

<status>pending</status>
<round>118</round>
<slot>0.9.0_WK_AMGT_RESAPP~515</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
