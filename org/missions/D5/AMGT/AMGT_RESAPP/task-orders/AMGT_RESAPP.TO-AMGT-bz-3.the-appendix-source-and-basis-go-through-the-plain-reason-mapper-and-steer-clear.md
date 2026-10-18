# AMGT_RESAPP task order -- `AMGT-bz-3` -- THE PACK APPENDIX'S SERVED SOURCE AND BASIS DEFINITION GO THROUGH THE PLAIN-REASON MAPPER, AND THE UNKNOWN-VERDICT SENTENCE READS `STEER CLEAR`

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bz-3</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~519</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bz-3.the-appendix-source-and-basis-go-through-the-plain-reason-mapper-and-steer-clear</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a renderer change and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut (2026-10-18): AC1 at the base fails (the test file is absent); AC2 at the base reads `1 failed, 249 passed` (the one known failure) and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (the tests build packs from committed fixtures; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-519` (branch `wk-AMGT_RESAPP-519`, cut from the issuance commit; its nested `portal/` is read-only and carries the page's source at `origin/DEV` `3a7791c1`, which you READ for the page's rule and never edit). Work and commit only in the outer worktree. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-519`.

**THREE ROUND-116 LESSONS THAT BIND YOUR TESTS.** (1) Two cells of this round edit `lib/research/print/render_pack.py` in different regions and are merged by the issuer; **a test of yours that compares a pack's WHOLE text to a recorded text fails the moment another cell's section lands.** Compare a SECTION (the lines between two headings) or the FIGURE lines (the `Appendix: model figures` block) or a named line, never the whole text. (2) Read `lib/research/print/tests/test_bw2_pack_form.py` and `test_bw1_currency_labels.py` first: they build a pack from committed fixtures with `build_pack` and read its text; copy their way, change nothing in them unless an assertion of theirs pins the exact old behaviour your cell changes: then re-scope that ONE assertion with a hand-written expectation, name it in the receipt (`## Tests re-scoped`: old and new), and the issuer re-runs the whole print plus api folders in the full tree after the merge. (3) A new check is dry-run at the base first: your test file runs ONCE on the unedited head and must fail on the new behaviour and pass on every control; record the counts.

**THE SERVED INPUTS (read-only fixtures; COPY them into `lib/research/print/tests/fixtures/` under the same names, your `<paths>` grants that folder):** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119_prep/fixtures/bx_served_thesis_RIO_LN.json`, `..._ICT_PM.json`, `..._GOOGL_US.json`. Each is the served `GET /thesis` body of `opal-amgt-scoped-api` for that name on 2026-10-18 (CodeSha256 `lNWo6Cm6..`), trimmed to `header_figures`, `dossier_fields`, `ai_fill`, `drafted_sections`, `drafting_*`, `posture`, `management`, `identity`. The pack route hands `build_pack` this bundle as `thesis_bundle`, and the model block carries the same `header_figures`; the existing bw fixtures show how a test assembles a block and a bundle. You call no AWS, no HTTP and no vendor.

**FOUR ROUND-117 LESSONS (in addition to the three above).** (a) **Name the proof instance by the order's FULL name:** `round-close-check` and the L6 gate look for `<to_id>.proof_of_spec.json`, `<to_id>` being the order file's name without `.md`; the path is under the limit (git `core.longpaths` is true), so never shorten it. (b) **Read your own pack's TEXT, not only your assertions:** render the three names' packs and read the sections you changed once before you write the receipt; a defect no fixture sees (an order of lines, a sentence that contradicts its neighbour) is found by reading. (c) **The regexes in your tests are raw strings:** a `\b` in a non-raw string is a backspace byte. (d) **A re-scoped test is named in the receipt with its old and new assertion;** the issuer re-runs the whole print plus api folders in the full tree after the merge and the baseline is `1 failed, 249 passed` in the print folder (the one known failure is `test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words`).

## 1. THE CELL -- `AMGT-bz-3` (round 119, decomposition s.128, items 3 and 4 of the CTO's round-118 analysis; rows `AMGT_RESAPP-D1-W515-S2` and the CTO's by-5 row)

**Item 3 (row `W515-S2`, ARMED, latent).** The pack's Appendix prints a figure's served `source` and a served basis definition AS SERVED (round 118 measured that no live value carries a path today). The CTO's rule: **the appendix's served source and basis definition go through `_plain_reason`, or the appendix's own fixed sentence** (the mapper `by-1` built: `_plain_reason(reason, fixed)` in `render_pack.py`, a token rule: a served text naming `s3://`, a key or path, a `.json` or `.docx` name, an `AMGT-` cell id, an order or row id, an UPPER_SNAKE token, an underscore inside a word, a vendor or Python error name, or longer than 300 characters is not plain words and prints the site's own fixed sentence). The sites are the figure-line functions: `_plain_figure_line` (around line 563), `_plain_label` (410-437), `_withheld_line` and `_source_words` (642-654), and any other appendix print site your census finds. Read row W515-S2 first. **Care:** a figure's normal source is the word `Bloomberg` (and similar one-word provenance) and a normal definition is a plain sentence from the model words: the mapper must leave every such value byte-identical (the appendix of the three names is the control). A FIGURE LABEL or MNEMONIC the line legitimately carries is not a reason: only the served `source` and the served basis definition text are routed.

**Item 4 (the CTO's by-5 row).** `UNKNOWN_VERDICT_SENTENCE` (`render_pack.py` around line 840) reads `The verdict on file is not one of better, worse, hold or steer_clear: no call is shown.`, and `steer_clear` is a field-code spelling the mapper itself treats as not plain words (an underscore inside a word). It must read `steer clear`. Update the tests that pin the old sentence (name them in the receipt with old and new assertion).

**Do this in order.** (A) `cd C:/dev/wk-resapp-519`; `git log -1 --format=%h`; copy the eight fixtures; write `lib/research/print/tests/test_bz3_appendix_plain_and_verdict.py` FIRST (tests below) and run it ONCE on the unedited head: record the counts. (B) THE CENSUS (receipt `## Census`, denominator printed): every print site of the pack's Appendix (the `Header` listing and every `Fiscal year <Y>` listing and any forecast listing): the function and line, the served field it prints (`source`, a basis definition, a label, a value, a unit), what it prints BEFORE for a served value carrying `s3://opal-data-harvest/x/y.json` and for one carrying `AMGT-rj-11 has not landed one`, and AFTER. (C) Route the `source` and basis-definition sites through `_plain_reason` with the site's own fixed sentence; change the verdict sentence; re-run. (D) AC1, AC2, then read the three names' appendices once, then the receipt, instance (named by the order's FULL name) and proof-of-spec-check.

**Tests (`test_bz3_appendix_plain_and_verdict.py`; hand-written expectations):** W1 each census site, driven with a served source or definition carrying `s3://opal-data-harvest/x/y.json` and one carrying `AMGT-rj-11 has not landed one`, prints its fixed sentence and neither string (one parametrised case per site); W2 CONTROL: for the eight names (the fixtures) the whole `Appendix: model figures` block is byte-identical before and after (the served values are plain: record the base block into a fixture by hand at Step A); W3 a plain served source (`Bloomberg`) and a plain definition are NOT replaced; W4 the verdict sentence reads exactly `The verdict on file is not one of better, worse, hold or steer clear: no call is shown.` and contains no underscore; W5 a verdict of `steer_clear` (the served value) still maps to its own sentence as before (the served enum is unchanged: only the fixed words changed); W6 an all-names style control: the pack text of the eight names contains no `s3://`, no `AMGT-` and no UPPER_SNAKE token outside the appendix's mnemonic column.

**Region you own in `render_pack.py`:** the PDF appendix's figure-line functions' `source` and definition parts, the `UNKNOWN_VERDICT_SENTENCE` constant and the tests above. You do NOT edit the rich export (`AMGT-bz-1`, `AMGT-bz-2`), `_plain_reason` itself, or `render_print.py`.

**THE SERVED INPUTS for round 119 (read-only fixtures; COPY into `lib/research/print/tests/fixtures/` under the same names, your `<paths>` grants that folder):** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119_prep/fixtures/bz_served_thesis_<NAME>.json` for `RIO_LN`, `ICT_PM`, `GOOGL_US`, `ICICIBC_IN`, `HD_US`, `BA_US`, `KMB_US` and `TSM_US` (the eight names the CVO reads), each the served `GET /thesis` body of `opal-amgt-scoped-api` for that name on 2026-10-18 ~11:4xZ (CodeSha256 `H3dCSGL..`), trimmed to `header_figures`, `dossier_fields`, `ai_fill`, `drafted_sections`, `drafting_*`, `posture`, `management`, `identity`. The existing `bx_served_thesis_*.json` fixtures (round 117) are the same shape for three of them.

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/print/render_pack.py` ONLY, and ONLY the region this cell names (two other cells edit other regions of the same file in parallel). Do NOT edit `lib/research/api/scoped_amgt.py`, `render_print.py`, `long_day.py` or the portal.
3. A served state sentence or reason the pack prints never carries a storage path, a bucket key, an object name, an order or cell id (`AMGT-...`) or an UPPER_SNAKE field code: say it in one plain sentence.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~519/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bz-3"><invocation>cd C:/dev/wk-resapp-519 &amp;&amp; timeout 300 python -m pytest lib/research/print/tests/test_bz3_appendix_plain_and_verdict.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `10 passed` or more with 0 failed and 0 skipped, W1 (once per site) to W6 each present by name, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bz-3"><invocation>cd C:/dev/wk-resapp-519 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 249 passed`), and the summary reads `1 failed, P passed` with P at least 255</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~519 <0.9.0_WK_AMGT_RESAPP~519@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~519/BZ3_RECEIPT.md` with the sections `## What changed` (every path, with line counts), `## Census` (the table the cell's Step A asks for, with its denominator), `## Tests re-scoped` (or `none`) and `## Not verified` (the deployed Lambda serves the old renderer until `AMGT-bx-5`; the whole api folder is not run in this sparse worktree: the issuer runs it in the full tree). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~519/AMGT_RESAPP.TO-AMGT-bz-3.the-appendix-source-and-basis-go-through-the-plain-reason-mapper-and-steer-clear.proof_of_spec.json` (the invocations are recorded as the order's literal text; a re-run in another tree goes in `output_evidence` and `status_reason`, never in `invocation`). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W519-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate; round 116's rows S7 to S10 omitted it)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the census table; every existing test you re-scoped (old and new assertion); the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Items 3 and 4 of the CTO's round-118 analysis (batched: one region, the pack's appendix figure-line sites and one constant); rows W515-S2 and the CTO's by-5 row. The issuer's measurement behind the 'latent' reading: `r118_leak_scan.py live` over 101 names reads 0 leaking lines. LOCAL code cell.

<status>complete</status>
<round>119</round>
<slot>0.9.0_WK_AMGT_RESAPP~519</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
