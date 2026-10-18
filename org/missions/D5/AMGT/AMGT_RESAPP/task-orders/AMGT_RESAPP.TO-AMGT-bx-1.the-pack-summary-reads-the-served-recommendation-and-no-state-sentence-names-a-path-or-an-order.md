# AMGT_RESAPP task order -- `AMGT-bx-1` -- THE PACK'S SUMMARY READS THE SERVED RECOMMENDATION WITH ITS CITATION, AND NO STATE SENTENCE OF THE PACK NAMES A STORAGE PATH, A KEY OR AN ORDER

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bx-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~512</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bx-1.the-pack-summary-reads-the-served-recommendation-and-no-state-sentence-names-a-path-or-an-order</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a renderer change and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut (2026-10-18): AC1 at the base fails (the test file is absent); AC2 at the base reads `1 failed, 146 passed` (the one known failure) and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (the tests build packs from committed fixtures; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-512` (branch `wk-AMGT_RESAPP-512`, cut from the issuance commit; its nested `portal/` is read-only and carries the page's source at `origin/DEV` `3a7791c1`, which you READ for the page's rule and never edit). Work and commit only in the outer worktree. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-512`.

**THREE ROUND-116 LESSONS THAT BIND YOUR TESTS.** (1) Two cells of this round edit `lib/research/print/render_pack.py` in different regions and are merged by the issuer; **a test of yours that compares a pack's WHOLE text to a recorded text fails the moment another cell's section lands.** Compare a SECTION (the lines between two headings) or the FIGURE lines (the `Appendix: model figures` block) or a named line, never the whole text. (2) Read `lib/research/print/tests/test_bw2_pack_form.py` and `test_bw1_currency_labels.py` first: they build a pack from committed fixtures with `build_pack` and read its text; copy their way, change nothing in them unless an assertion of theirs pins the exact old behaviour your cell changes: then re-scope that ONE assertion with a hand-written expectation, name it in the receipt (`## Tests re-scoped`: old and new), and the issuer re-runs the whole print plus api folders in the full tree after the merge. (3) A new check is dry-run at the base first: your test file runs ONCE on the unedited head and must fail on the new behaviour and pass on every control; record the counts.

**THE SERVED INPUTS (read-only fixtures; COPY them into `lib/research/print/tests/fixtures/` under the same names, your `<paths>` grants that folder):** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round117_prep/fixtures/bx_served_thesis_RIO_LN.json`, `..._ICT_PM.json`, `..._GOOGL_US.json`. Each is the served `GET /thesis` body of `opal-amgt-scoped-api` for that name on 2026-10-18 (CodeSha256 `lNWo6Cm6..`), trimmed to `header_figures`, `dossier_fields`, `ai_fill`, `drafted_sections`, `drafting_*`, `posture`, `management`, `identity`. The pack route hands `build_pack` this bundle as `thesis_bundle`, and the model block carries the same `header_figures`; the existing bw fixtures show how a test assembles a block and a bundle. You call no AWS, no HTTP and no vendor.

## 1. THE CELL -- `AMGT-bx-1` (round 117, decomposition s.126, items 1 and 2 of the CTO's round-116 analysis)

**What is wrong today (the CVO's read of the live packs, C-S189 and C-S190).** (1) Every pack's `Summary` section prints "No recommendation has been written for this company yet." although the gateway serves a CITED recommendation for all three names: it is the served `dossier_fields.last_stated_position` (and `fund_of_record`) of the `/thesis` body, which the page's Posture tab shows. The pack reads `drafted_sections` (empty for these names) and no other source. (2) The `Positioning` section prints `Posture: ABSENT -- no O-1 posture object under s3://opal-data-harvest/posture/v1/...  -- AMGT-rj-11 has not landed one.`: a storage path and an order id in reader-facing prose.

**The served recommendation (hand-written expectations; each value is in the fixtures):** RIO LN `dossier_fields.last_stated_position.value` = `{fund: IDVZ, size_pct: "2.75", text: "MAINTAIN 2.75% POSITION IN IDVZ"}`, citation = a research report (`report_key` ends `Rio Tinto H1 2026 Earnings Update.docx`), `locator` 2, `passage` `RECOMMENDATION: MAINTAIN 2.75% POSITION IN IDVZ`; ICT PM `{fund: IDVZ, size_pct: "1.75", text: "MAINTAIN 1.75% POSITION IN IDVZ"}`; GOOGL US `{fund: PFOE, line_only: true, size_pct: null, text: "Maintain positions in PFOE and DIVZ"}` (a line-only position: there is no single fund and weight to print beyond the text).

**The rule to build (Summary only):** the `Summary` section prints, in this order, (a) the drafted recommendation sentence and the drafted thesis sentence when `drafted_sections` carries them (unchanged), (b) the served recommendation line from `last_stated_position`: its `text` as served, then, when the position is not `line_only`, the fund and the weight in words (`Fund IDVZ, weight 2.75 per cent of the fund`), then ONE citation line naming the source in plain words: `Source: research report "<report title>", passage <locator>.` where the title is the report file's name without its folder and without its extension (never the key, never `s3://`, never a bucket), and (c) the sentence "No recommendation has been written for this company yet." ONLY when BOTH the drafted recommendation and the served position are absent. A `last_stated_position` whose status is not `SERVED` is absent. Where the served citation is missing a locator or title, print what it carries and nothing invented.

**Positioning and every state sentence (the second half of the cell).** An absent posture prints ONE plain sentence: `No positioning view is on file for this name.` (exactly that text). Then CENSUS EVERY STRING of `render_pack.py` that a pack can print from a served state, reason, status, key, path or id (the posture, management, peers, drafting, what-changed, and any other `reason`-bearing state the file renders) and make each of them free of a storage path, a bucket key, an object name, a cell or order id (`AMGT-...`), a vendor error text (`NoSuchKey`) and an UPPER_SNAKE field code. The Step A census table lists every such print site with its state and what it printed BEFORE and AFTER; a site you leave unchanged names why it carries none of these.

**Do this in order.** (A) `cd C:/dev/wk-resapp-512`; `git log -1 --format=%h`; copy the three fixtures (see above); write `lib/research/print/tests/test_bx1_summary_positioning.py` with the tests below FIRST and run it ONCE on the unedited head (S1 to S5, S7 and S8 must fail, S6 and the controls pass: record the counts). (B) Make the census of state-sentence print sites in `render_pack.py` (grep for `reason`, `status`, `ABSENT`, `s3://`, `posture`, and read the section builders). (C) Build the rule in the Summary and Positioning builders only; re-run. (D) AC1, AC2, then the receipt, instance and proof-of-spec-check.

**Tests (`test_bx1_summary_positioning.py`; each hand-written expectation; models are the bw tests):** S1 RIO LN: the `Summary` section contains `MAINTAIN 2.75% POSITION IN IDVZ`, `IDVZ`, `2.75`, the report title `Rio Tinto H1 2026 Earnings Update`, and the citation locator; S2 ICT PM: `MAINTAIN 1.75% POSITION IN IDVZ` and `1.75`; S3 GOOGL US: `Maintain positions in PFOE and DIVZ`, and NO weight and no `None`; S4 none of the three `Summary` sections contains `No recommendation has been written`; S5 a synthetic bundle whose `last_stated_position` is absent and whose `drafted_sections` is empty prints the absence sentence once in `Summary`, and one with a drafted recommendation prints it AND the served line; S6 CONTROL: the figure lines (the `Appendix: model figures` block) of the three names are equal as a sorted multiset before and after (use your base run's capture, written into a fixture by hand at Step A); S7 the `Positioning` section of an absent-posture bundle is exactly the one sentence `No positioning view is on file for this name.`; S8 the census: the full printed text of the three names (and of a synthetic bundle with every state absent) contains no `s3://`, no `AMGT-`, no `NoSuchKey`, no `bronze`, no `.json`, and no UPPER_SNAKE token.

**Region you own in `render_pack.py`:** the `Summary` builder, the `Positioning` builder and the state-sentence sites the census finds. You do NOT touch the figure-line functions (`_money`, `_format_figure_value`, `_header_figures_for_print`: cell `AMGT-bx-2`) or the `Management` builder and the machine-written passages (cell `AMGT-bx-3`).

**AMENDMENT 1 (issuer, 2026-10-18 ~07:3xZ), after the merge of `bx-1`, `bx-2` and `bx-3` at `3dd98e9a9d`.** The issuer read the merged candidate's packs (this checkout's handler over the live pool, eight names). Your cell worked and merged; the read shows one ordering defect that is MY SPEC's, not yours: the Summary prints `No investment thesis has been written for this company yet.` BEFORE the served recommendation (RIO LN: the thesis absence sentence, then `MAINTAIN 2.75% POSITION IN IDVZ`), because the face asked for (a) the drafted recommendation and thesis sentences, then (b) the served line. A reader meets the recommendation first. **You are the SAME slot re-seated: your branch has been fast-forwarded to the merged tree `3dd98e9a9d`, which CONTAINS your commits (`aa93cada46`, `33b6a0be40`) and the other two cells' work; add NEW commits, never amend.**

**The corrected Summary order (the `Summary` builder `_print_summary` only):** (1) the served recommendation block first (the `last_stated_position` text, the fund and weight line, the one `Source:` citation line, exactly as built); (2) then the drafted recommendation sentence(s) when `drafted_sections` carries them; (3) then the drafted thesis sentence(s), or, when there are none, `No investment thesis has been written for this company yet.`; (4) the no-recommendation sentence stays ONLY when both the drafted recommendation and the served position are absent, and then it leads (it is the first line, as the recommendation's own absence). Everything else of your cell is unchanged. Re-scope ONLY the assertions of your own `test_bx1_summary_positioning.py` that pin the old order, and add one test, S9, named in the output: for RIO LN the first non-heading line of `Summary` is the served recommendation text, and the thesis absence sentence comes after the `Source:` line; for a synthetic bundle with both absent the first line is the no-recommendation sentence. Also add S10: a synthetic bundle with a drafted recommendation AND a served position prints the served block first, then the drafted sentence. No other existing test is edited (if one of the other two cells' tests pins the Summary order, say so in the receipt and leave it: the issuer re-runs the whole print plus api folders in the full tree).

**Steps for this re-seat.** (1) `cd C:/dev/wk-resapp-512`; confirm `git log -1 --format=%h` reads the merged head `3dd98e9a9d` or a commit of the order-file update on top of it. (2) Edit; re-run AC1 (`20 passed` or more) and AC2 (exactly one FAILED line, the av2 base failure, and `1 failed, P passed` with P at least 183). (3) Update the receipt (`## What changed`, `## Tests re-scoped`: old and new assertion) and the proof-of-spec instance as new commits; run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes. Rows continue after S5, each with `disarm_owner` `2.0.0_SA_COO~R1`. Report once.

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/print/render_pack.py` ONLY, and ONLY the region this cell names (two other cells edit other regions of the same file in parallel). Do NOT edit `lib/research/api/scoped_amgt.py`, `render_print.py`, `long_day.py` or the portal.
3. A served state sentence or reason the pack prints never carries a storage path, a bucket key, an object name, an order or cell id (`AMGT-...`) or an UPPER_SNAKE field code: say it in one plain sentence.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~512/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bx-1"><invocation>cd C:/dev/wk-resapp-512 &amp;&amp; timeout 300 python -m pytest lib/research/print/tests/test_bx1_summary_positioning.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `8 passed` or more with 0 failed and 0 skipped, S1 to S8 each present by name, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bx-1"><invocation>cd C:/dev/wk-resapp-512 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 146 passed`), and the summary reads `1 failed, P passed` with P at least 183</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~512 <0.9.0_WK_AMGT_RESAPP~512@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~512/BX1_RECEIPT.md` with the sections `## What changed` (every path, with line counts), `## Census` (the table the cell's Step A asks for, with its denominator), `## Tests re-scoped` (or `none`) and `## Not verified` (the deployed Lambda serves the old renderer until `AMGT-bx-5`; the whole api folder is not run in this sparse worktree: the issuer runs it in the full tree). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~512/AMGT_RESAPP.TO-AMGT-bx-1.the-pack-summary-reads-the-served-recommendation-and-no-stat.proof_of_spec.json` (the invocations are recorded as the order's literal text; a re-run in another tree goes in `output_evidence` and `status_reason`, never in `invocation`). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W512-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate; round 116's rows S7 to S10 omitted it)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the census table; every existing test you re-scoped (old and new assertion); the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Items 1 and 2 of the CTO's round-116 analysis (`ledger/ROUND_ANALYSIS.round116.R1.md`). The served source is read from the live `/thesis` of the three names at ~06:3xZ (`dossier_fields.last_stated_position` SERVED with a cited extract on all three); the gateway's `harvest_get_research` reads the same served field. LOCAL code cell; served only through `AMGT-bx-5`.

<status>pending</status>
<round>117</round>
<slot>0.9.0_WK_AMGT_RESAPP~512</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
