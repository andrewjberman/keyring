# AMGT_RESAPP task order -- `AMGT-by-1` -- EVERY SERVED REASON THE PRINTED PACK CAN PRINT GOES THROUGH ONE PLAIN-SENTENCE MAPPER, AND AN UNKNOWN REASON PRINTS A FIXED SENTENCE, NEVER THE RAW TEXT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-by-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~515</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-by-1.every-served-reason-the-pack-prints-goes-through-one-plain-sentence-mapper</to_id>
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

## 1. THE CELL -- `AMGT-by-1` (round 118, decomposition s.127, item 1 of the CTO's round-117 analysis)

**What is open (two armed rows).** Round 117 made the pack's state sentences free of a storage path, a bucket key, an order id and a vendor error ONLY for the three names the CVO read, by changing the individual sites that print them (`AMGT-bx-1`). Two sites still print a served reason RAW if a served reason carried a path: row `AMGT_RESAPP-D1-W512-S2` (the posture arm: a `None` posture prints the old `No analyst posture is on file ...` sentence, which an api test pins) and row `AMGT_RESAPP-D1-W512-S3` (the `Management` builder's CEO-profile sentence prints the reading's reason verbatim; the CTO's analysis names `render_pack.py:897-898`). The CTO's rule for this round: **every site in `render_pack.py` that can print a served reason goes through ONE plain-sentence mapper; an unknown reason prints a fixed sentence, never the raw text.** Read the rows (in `org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md`, ids above) first.

**The mapper to build (one function in `render_pack.py`, name it `_plain_reason`):** `_plain_reason(reason, fixed)` returns the served `reason` text ONLY when it is plain words, and otherwise returns the site's own `fixed` sentence. A reason is NOT plain words when it contains ANY of: `s3://`, a `/` between word characters that looks like a key or path, `.json`, `.docx`, `bronze` or `gold` as a path part, an `AMGT-` cell id, an order or row id of the form `<LETTERS>-<letters>-<digits>` (for example `AMGT-rj-11`, `D1-S54`), an UPPER_SNAKE token, an underscore in a word, a vendor or Python error name (`NoSuchKey`, `ClientError`, `RuntimeError`, `TypeError`, `KeyError`, `Traceback`, `botocore`), a `:` followed by a bucket-looking token, or the words `NOT_SERVED` and `READ_FAILED`; a reason that is empty, not a string, or longer than 300 characters is also not plain. Every site passes its OWN fixed sentence (the ones round 117 wrote stay: `No positioning view is on file for this name.`, `No peer set is on file for this company yet.`, `No positioning call was made for this name.`; new ones in the same plain register for the others). The fixed sentence is hand-written by you per site and says WHY the content is missing in one plain clause when the site knows why.

**Do this in order.** (A) `cd C:/dev/wk-resapp-515`; `git log -1 --format=%h`; copy the three fixtures (see above); write `lib/research/print/tests/test_by1_reason_mapper.py` FIRST (tests below) and run it ONCE on the unedited head: record the counts. (B) THE CENSUS: read `render_pack.py` end to end for every site that can print text taken from a served `reason`, `status`, `state`, `error`, `absent_because`, `source` or `basis` field (the builders `_print_summary`, `_print_drafted`, `_print_passage`, `_print_thesis_pillars`, `_print_management`, `_print_positioning`, `_print_peers`, the what-changed block, the drafting-reason lines, the company-description fallbacks, and the helpers they call), and the rich-markdown helpers too (`_drafted_section_markdown`, `_model_cases_markdown`, `build_rich_text`: list them with surface `rich` and DO NOT edit them: the next cell `AMGT-by-2` takes them). The census table (receipt `## Census`, denominator printed) has one row per site: function and line, the surface (`pdf` or `rich`), the served field it reads, what it printed BEFORE for a served reason carrying `s3://opal-data-harvest/x/y.json` and for one carrying `AMGT-rj-11 has not landed one`, what it prints AFTER, and the fixed sentence. (C) Build `_plain_reason` and route EVERY `pdf` site through it; the `None`-posture arm of row S2 is in the Positioning builder: make it print the same one sentence as an absent posture, and RE-SCOPE the one api test that pins the old sentence (`lib/research/api/tests/test_bw4_print_pack_degrades.py` D3 and any other test that asserts `No analyst posture is on file`; the grant covers `lib/research/api/tests/`): name each in the receipt with its old and new assertion. (D) AC1, AC2, then read the three names' packs once, then the receipt, instance and proof-of-spec-check.

**Tests (`test_by1_reason_mapper.py`; hand-written expectations; models are the bw and bx tests):** Y1 `_plain_reason` returns a plain served reason unchanged (for example `No peer set has been compiled for this name.`) and returns the fixed sentence for each of at least twelve NOT-plain shapes (an `s3://` URL, a bucket key, a `.json` name, an `AMGT-rj-11` id, a `D1-S54` row id, an UPPER_SNAKE token, a `NoSuchKey` error text, a Python traceback line, an empty string, `None`, a number, a 400-character string); Y2 each `pdf` site of your census, driven with a served reason carrying `s3://opal-data-harvest/posture/v1/X/y.json` and `AMGT-rj-11 has not landed one`, prints its fixed sentence and neither string (one parametrised case per site, named by the site); Y3 CONTROL: for RIO LN, ICT PM and GOOGL US (the fixtures) the `Positioning`, `Management`, `Peers` and `Summary` sections are byte-identical before and after for the plain reasons the fixtures carry (use your base run's capture of the four sections, written into a fixture by hand at Step A); Y4 a posture of `None` and a posture of status ABSENT print the SAME one sentence in `Positioning`; Y5 the figure lines (the `Appendix: model figures` block) of the three names are equal as a sorted multiset before and after; Y6 NEGATIVE CONTROL: a deliberately plain reason that merely contains the word `bronze` in prose (`the bronze medal sentence`) is NOT replaced (state in the test how your rule tells a path part from a word: the rule is a TOKEN rule, not a substring rule), and a reason with an underscore inside a word IS replaced.

**Region you own in `render_pack.py`:** the pack's (`pdf`) reason-printing sites and the new mapper. You do NOT edit the rich-markdown helpers (`by-2`), the figure-line functions, the `ai_fill` passage builders' wording or `build_pack`'s section order.

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/print/render_pack.py` ONLY, and ONLY the region this cell names (two other cells edit other regions of the same file in parallel). Do NOT edit `lib/research/api/scoped_amgt.py`, `render_print.py`, `long_day.py` or the portal.
3. A served state sentence or reason the pack prints never carries a storage path, a bucket key, an object name, an order or cell id (`AMGT-...`) or an UPPER_SNAKE field code: say it in one plain sentence.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~515/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-by-1"><invocation>cd C:/dev/wk-resapp-515 &amp;&amp; timeout 300 python -m pytest lib/research/print/tests/test_by1_reason_mapper.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `20 passed` or more with 0 failed and 0 skipped, Y1 to Y6 each present by name (Y2 once per site), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-by-1"><invocation>cd C:/dev/wk-resapp-515 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 189 passed`), and the summary reads `1 failed, P passed` with P at least 197</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~515 <0.9.0_WK_AMGT_RESAPP~515@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~515/BY1_RECEIPT.md` with the sections `## What changed` (every path, with line counts), `## Census` (the table the cell's Step A asks for, with its denominator), `## Tests re-scoped` (or `none`) and `## Not verified` (the deployed Lambda serves the old renderer until `AMGT-bx-5`; the whole api folder is not run in this sparse worktree: the issuer runs it in the full tree). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~515/AMGT_RESAPP.TO-AMGT-by-1.every-served-reason-the-pack-prints-goes-through-one-plain-sentence-mapper.proof_of_spec.json` (the invocations are recorded as the order's literal text; a re-run in another tree goes in `output_evidence` and `status_reason`, never in `invocation`). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W515-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate; round 116's rows S7 to S10 omitted it)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the census table; every existing test you re-scoped (old and new assertion); the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Item 1 of the CTO's round-117 analysis (`ledger/ROUND_ANALYSIS.round117.R1.md`, msg 7986). Disarms rows W512-S2 and W512-S3 (disarm owner this seat). The rich-markdown sites are listed in the census and left to `by-2`, which starts after this cell merges (it reuses `_plain_reason`; one worker slot, ~515, runs both in order). LOCAL code cell; served only through `AMGT-by-5`.

<status>complete</status>
<round>118</round>
<slot>0.9.0_WK_AMGT_RESAPP~515</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
