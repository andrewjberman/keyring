# AMGT_RESAPP task order -- `AMGT-by-4` -- A READ, NO CHANGE: THE PRODUCER STEP THAT LEAVES RIO LN'S PER-FIGURE CURRENCY BASIS UNMEASURED WHILE ITS FUND CURRENCY IS KNOWN

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-by-4</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~516</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-by-4.a-read-of-why-rio-ln-keeps-an-unmeasured-currency-basis-while-the-fund-currency-is-known</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a renderer change and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut (2026-10-18): AC1 at the base fails (the test file is absent); AC2 at the base reads `1 failed, 189 passed` (the one known failure) and AC2 is a REGRESSION control that PASSES at the base as expected (the cell changes no code). EGRESS CLASS, declared: NONE (the tests build packs from committed fixtures; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-516` (branch `wk-AMGT_RESAPP-516`, cut from the issuance commit; its nested `portal/` is read-only and carries the page's source at `origin/DEV` `3a7791c1`, which you READ for the page's rule and never edit). Work and commit only in the outer worktree. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-516`.

**THREE ROUND-116 LESSONS THAT BIND YOUR TESTS.** (1) Two cells of this round edit `lib/research/print/render_pack.py` in different regions and are merged by the issuer; **a test of yours that compares a pack's WHOLE text to a recorded text fails the moment another cell's section lands.** Compare a SECTION (the lines between two headings) or the FIGURE lines (the `Appendix: model figures` block) or a named line, never the whole text. (2) Read `lib/research/print/tests/test_bw2_pack_form.py` and `test_bw1_currency_labels.py` first: they build a pack from committed fixtures with `build_pack` and read its text; copy their way, change nothing in them unless an assertion of theirs pins the exact old behaviour your cell changes: then re-scope that ONE assertion with a hand-written expectation, name it in the receipt (`## Tests re-scoped`: old and new), and the issuer re-runs the whole print plus api folders in the full tree after the merge. (3) A new check is dry-run at the base first: your test file runs ONCE on the unedited head and must fail on the new behaviour and pass on every control; record the counts.

**THE SERVED INPUTS (read-only fixtures; COPY them into `lib/research/print/tests/fixtures/` under the same names, your `<paths>` grants that folder):** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round117_prep/fixtures/bx_served_thesis_RIO_LN.json`, `..._ICT_PM.json`, `..._GOOGL_US.json`. Each is the served `GET /thesis` body of `opal-amgt-scoped-api` for that name on 2026-10-18 (CodeSha256 `lNWo6Cm6..`), trimmed to `header_figures`, `dossier_fields`, `ai_fill`, `drafted_sections`, `drafting_*`, `posture`, `management`, `identity`. The pack route hands `build_pack` this bundle as `thesis_bundle`, and the model block carries the same `header_figures`; the existing bw fixtures show how a test assembles a block and a bundle. You call no AWS, no HTTP and no vendor.

**FOUR ROUND-117 LESSONS (in addition to the three above).** (a) **Name the proof instance by the order's FULL name:** `round-close-check` and the L6 gate look for `<to_id>.proof_of_spec.json`, `<to_id>` being the order file's name without `.md`; the path is under the limit (git `core.longpaths` is true), so never shorten it. (b) **Read your own pack's TEXT, not only your assertions:** render the three names' packs and read the sections you changed once before you write the receipt; a defect no fixture sees (an order of lines, a sentence that contradicts its neighbour) is found by reading. (c) **The regexes in your tests are raw strings:** a `\b` in a non-raw string is a backspace byte. (d) **A re-scoped test is named in the receipt with its old and new assertion;** the issuer re-runs the whole print plus api folders in the full tree after the merge and the baseline is `1 failed, 189 passed` in the print folder (the one known failure is `test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words`).

## 1. THE CELL -- `AMGT-by-4` (round 118, decomposition s.127, item 4 of the CTO's round-117 analysis; A READ: NO PRODUCT CODE CHANGES)

**The question (CTO, round 117; row `AMGT_RESAPP-D1-W513-S2`):** RIO LN's served header carries `EQY_FUND_CRNCY` = `USD` (a text figure, the reporting currency) while its per-figure currencies for `CUR_MKT_CAP`, `NET_DEBT`, `CURR_ENTP_VAL` and `CRNCY_ADJ_MKT_CAP` are none and their `currency_basis` begins `UNMEASURED` (the served text: `UNMEASURED: PX_LAST x EQY_SH_OUT_REAL does not reproduce the market cap, so no read shows its currency (CRPS-aa-1 round-25 census)` for the market cap and its alias; `UNMEASURED: the market-cap currency is not established, so no identity read is computable (CRPS-aa-1 round-25 census)` for net debt and enterprise value). The page withholds those four figures. **Name the PRODUCER STEP that leaves the per-figure basis unmeasured while the fund currency is known**, so the CTO can decide whether a later cell can carry the fund currency onto the figures under the page's rule. **Nothing changes this round; your deliverable is the receipt.**

**What to read (read-only; the served values are in the fixture `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round117_prep/fixtures/bx_served_thesis_RIO_LN.json`, `header_figures`, and `ICT_PM` and `GOOGL_US` beside it as the contrasts: ICT PM's `CUR_MKT_CAP` is `PHP` basis `quote (CRNCY)`, its `CURR_ENTP_VAL` is `USD` basis `reporting (EQY_FUND_CRNCY)`, and GOOGL US's money figures are `USD` basis `reporting (EQY_FUND_CRNCY)`):** (1) find where a header figure's `currency` and `currency_basis` are WRITTEN: search the repository for the string `currency_basis` and for the text `does not reproduce the market cap` (use the native Grep tool or `comp-find`, never a recursive shell grep; the producer is most likely in `lib/research/` under the model-block or provenance code, and the served route copies it in `lib/research/api/scoped_amgt.py`); (2) read the rule that chooses between the basis values you see in the three fixtures (`quote (CRNCY)`, `reporting (EQY_FUND_CRNCY)`, `UNMEASURED: ...`): what condition makes a figure `UNMEASURED`, what inputs it reads (the price, the share count, the market cap, the two currency fields), and where `EQY_FUND_CRNCY` is read or not read; (3) say which of RIO LN's four figures would have a defensible currency if the rule trusted `EQY_FUND_CRNCY` (give each figure's unit and why, from the producer's own words, never your guess), and which would not and why (the market cap in a dual-listed name's quote currency GBp versus the reporting currency USD is the likely trap: a pence quote against a USD fund currency; state what the producer does about it).

**The receipt (`## What changed` says `no product file changed`) has these sections, each citing `path:line` for every claim:** `## Producer step` (the function, the file and line range, and the one sentence a reader would quote), `## The rule` (the condition, its inputs, and a table of the three fixtures' figures with the basis value the rule yields and which branch gave it), `## What carrying the fund currency would need` (for each of the four figures: allowed under the producer's own logic or not, and the evidence), `## What the page does` (the page's `figureBasis` and `isUnmeasuredBasis` in `portal/src/pages/SecurityAnalysis/components/StatTile.tsx`, read-only, one paragraph) and `## Not verified`. A claim you did not read at a cited line is not a claim.

**Do this in order.** (A) `cd C:/dev/wk-resapp-516`; `git log -1 --format=%h`. (B) Read as above, taking notes of every `path:line`. (C) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~516/BY4_RECEIPT.md`. (D) Run the issuer's citation check on it (AC1) and fix every citation it refuses. (E) Instance, proof-of-spec-check, report.

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/print/render_pack.py` ONLY, and ONLY the region this cell names (two other cells edit other regions of the same file in parallel). Do NOT edit `lib/research/api/scoped_amgt.py`, `render_print.py`, `long_day.py` or the portal.
3. A served state sentence or reason the pack prints never carries a storage path, a bucket key, an object name, an order or cell id (`AMGT-...`) or an UPPER_SNAKE field code: say it in one plain sentence.

## 3. SURFACES

<paths>
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~516/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-by-4"><invocation>cd C:/dev/wk-resapp-516 &amp;&amp; timeout 120 python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round118_prep/checks/r118_receipt_cites_check.py org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~516/BY4_RECEIPT.md; echo "exit=$?"</invocation><expect>the last line reads `RECEIPT CITES: YES (N of N citations resolve, 5 of 5 sections present)` with N at least 10, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-by-4"><invocation>cd C:/dev/wk-resapp-516 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 189 passed`), and the summary reads `1 failed, P passed` with P at least 189</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~516 <0.9.0_WK_AMGT_RESAPP~516@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~516/BY4_RECEIPT.md` with the sections `## What changed` (every path, with line counts), `## Census` (the table the cell's Step A asks for, with its denominator), `## Tests re-scoped` (or `none`) and `## Not verified` (the deployed Lambda serves the old renderer until `AMGT-bx-5`; the whole api folder is not run in this sparse worktree: the issuer runs it in the full tree). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~516/AMGT_RESAPP.TO-AMGT-by-4.a-read-of-why-rio-ln-keeps-an-unmeasured-currency-basis-while-the-fund-currency-is-known.proof_of_spec.json` (the invocations are recorded as the order's literal text; a re-run in another tree goes in `output_evidence` and `status_reason`, never in `invocation`). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W516-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate; round 116's rows S7 to S10 omitted it)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the census table; every existing test you re-scoped (old and new assertion); the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Item 4 of the CTO's round-117 analysis: a READ (row W513-S2); it changes no product file and decides whether a later cell can carry the fund currency onto the figures under the page's rule. The issuer's citation check `round118_prep/checks/r118_receipt_cites_check.py` verifies that each `path:line` the receipt cites exists and that the five sections are present; it does not grade whether the reading is right (the CTO reads it). AC2 is a REGRESSION control only: the cell writes no code, so the print folder must read exactly as at the base. LOCAL read cell; `<risk>LOCAL</risk>`.

<status>pending</status>
<round>118</round>
<slot>0.9.0_WK_AMGT_RESAPP~516</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
