# AMGT_RESAPP task order -- `AMGT-bz-2` -- THE RICH EXPORT READS THE CEO PROFILE FROM THE SAME INPUT AS THE PDF, AND THE CAUSE OF `COULD NOT BE READ` IS NAMED

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bz-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~518</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bz-2.the-rich-export-reads-the-ceo-profile-from-the-same-input-as-the-pdf</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a renderer change and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut (2026-10-18): AC1 at the base fails (the test file is absent); AC2 at the base reads `1 failed, 249 passed` (the one known failure) and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (the tests build packs from committed fixtures; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-518` (branch `wk-AMGT_RESAPP-518`, cut from the issuance commit; its nested `portal/` is read-only and carries the page's source at `origin/DEV` `3a7791c1`, which you READ for the page's rule and never edit). Work and commit only in the outer worktree. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-518`.

**THREE ROUND-116 LESSONS THAT BIND YOUR TESTS.** (1) Two cells of this round edit `lib/research/print/render_pack.py` in different regions and are merged by the issuer; **a test of yours that compares a pack's WHOLE text to a recorded text fails the moment another cell's section lands.** Compare a SECTION (the lines between two headings) or the FIGURE lines (the `Appendix: model figures` block) or a named line, never the whole text. (2) Read `lib/research/print/tests/test_bw2_pack_form.py` and `test_bw1_currency_labels.py` first: they build a pack from committed fixtures with `build_pack` and read its text; copy their way, change nothing in them unless an assertion of theirs pins the exact old behaviour your cell changes: then re-scope that ONE assertion with a hand-written expectation, name it in the receipt (`## Tests re-scoped`: old and new), and the issuer re-runs the whole print plus api folders in the full tree after the merge. (3) A new check is dry-run at the base first: your test file runs ONCE on the unedited head and must fail on the new behaviour and pass on every control; record the counts.

**THE SERVED INPUTS (read-only fixtures; COPY them into `lib/research/print/tests/fixtures/` under the same names, your `<paths>` grants that folder):** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119_prep/fixtures/bx_served_thesis_RIO_LN.json`, `..._ICT_PM.json`, `..._GOOGL_US.json`. Each is the served `GET /thesis` body of `opal-amgt-scoped-api` for that name on 2026-10-18 (CodeSha256 `lNWo6Cm6..`), trimmed to `header_figures`, `dossier_fields`, `ai_fill`, `drafted_sections`, `drafting_*`, `posture`, `management`, `identity`. The pack route hands `build_pack` this bundle as `thesis_bundle`, and the model block carries the same `header_figures`; the existing bw fixtures show how a test assembles a block and a bundle. You call no AWS, no HTTP and no vendor.

**FOUR ROUND-117 LESSONS (in addition to the three above).** (a) **Name the proof instance by the order's FULL name:** `round-close-check` and the L6 gate look for `<to_id>.proof_of_spec.json`, `<to_id>` being the order file's name without `.md`; the path is under the limit (git `core.longpaths` is true), so never shorten it. (b) **Read your own pack's TEXT, not only your assertions:** render the three names' packs and read the sections you changed once before you write the receipt; a defect no fixture sees (an order of lines, a sentence that contradicts its neighbour) is found by reading. (c) **The regexes in your tests are raw strings:** a `\b` in a non-raw string is a backspace byte. (d) **A re-scoped test is named in the receipt with its old and new assertion;** the issuer re-runs the whole print plus api folders in the full tree after the merge and the baseline is `1 failed, 249 passed` in the print folder (the one known failure is `test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words`).

## 1. THE CELL -- `AMGT-bz-2` (round 119, decomposition s.128, item 2 of the CTO's round-118 analysis; the CVO's finding C-S195)

**The finding (CVO, round 118).** On 8 of 8 names the rich export's management section says `CEO public-profile reading: the object could not be read`, while the PDF pack prints HD US's reading (`CEO public profile (EDWARD P. DECKER): The CEO web search returned 10 url(s), none of them ...`) and, for the other names, its own sentence (`CEO public profile: no public profile is on file yet.`). The two routes do not read the same input for the same name. **The CTO's grade: name WHY the export reads `could not be read` today; make the rich export read management and the CEO profile through the SAME reader and input as the PDF route; the eight names' export management lines then EQUAL their PDF's, and HD US prints its reading in both.**

**What the served data shows (a starting hypothesis you must VERIFY at cited lines, never assume):** the served `management` object of each of the eight names (fixtures) carries TWO CEO-profile fields: `ceo_public_profile` (null for RIO LN, ICT PM, GOOGL US, ICICIBC IN, KMB US, TSM US; a dict `{url, title, snippet, status: ABSENT, basis: "The CEO web search returned 10 url(s), none of them ..."}` for HD US and BA US) and `ceo_profile_reading` (the SAME value on all eight names: `{reading: "UNREADABLE_OBJECT", reading_basis: "the object is not a dict" or "status=ABSENT query=set absence_class=None", reason: null or the web-search sentence, urls_returned: null}`). The PDF's `_ceo_profile_sentence(management)` in `render_pack.py` (around line 936) builds its line from the management dict; the rich export prints `CEO public-profile reading: ...` from a reading word (`UNREADABLE_OBJECT` mapped to `the object could not be read`). Whether the export reads `ceo_profile_reading` while the PDF reads `ceo_public_profile`, or the export reads the reading WORD where the PDF reads the basis sentence, or the rich route in `scoped_amgt.py` hands `build_rich_text` a different management input than the PDF branch hands `build_pack`: that is your Step A finding. **Cite the line of each reader on both routes.**

**The rule to build:** the rich export's management lines (the roster, the CEO profile, the management passages the pack prints) are produced by the SAME function and from the SAME input as the PDF's: the cleanest form is that `build_rich_text` calls the pack's own `_ceo_profile_sentence` (and the other pack management helpers it can reuse) with the management object, instead of formatting its own reading; where the rich export legitimately differs in FORM (markdown, a table) it differs only in markup, never in the words or the fields read. A served reading word that is not plain words (`UNREADABLE_OBJECT`) never prints: the PDF's sentence, through `_plain_reason`, is the words. If your Step A shows the two routes already read the same input and differ only in wording, say so and make the words equal.

**Do this in order.** (A) `cd C:/dev/wk-resapp-518`; `git log -1 --format=%h`; copy the eight fixtures; write `lib/research/print/tests/test_bz2_rich_management_equals_pdf.py` and `lib/research/api/tests/test_bz2_rich_route_management_input.py` FIRST (tests below) and run them ONCE on the unedited head: record the counts. (B) THE FINDING: read both routes end to end for the management and CEO-profile lines (`render_pack.py` `_ceo_profile_sentence`, `_print_management`, the rich management section in `build_rich_text` and its helpers, and `scoped_amgt.py` `_print_pack`'s pdf and rich branches and the reader functions they call); write the receipt section `## Cause` naming WHY the export reads `could not be read` today with a `path:line` citation for every claim, and a table of the eight names with what each route prints today. (C) Build the rule; re-run. (D) AC1 to AC3, read the eight names' management lines in both formats once, then the receipt, instance (named by the order's FULL name) and proof-of-spec-check.

**Tests.** `test_bz2_rich_management_equals_pdf.py`: M1 for each of the eight names (a parametrised case per name), the management lines of the rich export, with markdown markup stripped, EQUAL the management lines of the PDF text (compare the CEO-profile line exactly and the roster lines as sorted multisets); M2 HD US: the export prints `CEO public profile (EDWARD P. DECKER)` and the web-search sentence, as the PDF does; M3 BA US the same for its reading; M4 no export carries the words `could not be read` or the token `UNREADABLE_OBJECT` for any of the eight; M5 CONTROL: the PDF pack text of the eight names is byte-identical before and after. `test_bz2_rich_route_management_input.py` (model `test_by2_rich_route_degrades.py`): M6 the `rich` route and the `pdf` route hand the builder the SAME management object for the same name (monkeypatch the readers, compare the objects the two builders receive); M7 with the management reader raising, both routes print the same absence sentence.

**Region you own:** the rich export's management section and helpers in `render_pack.py`, the `rich` branch of `_print_pack` and the reader plumbing for management in `scoped_amgt.py`, and the tests above. You do NOT edit the pack (`pdf`) builders (read-only here: the PDF is the reference and must stay byte-identical), `_figures_table` (`AMGT-bz-1`) or the appendix figure-line sites (`AMGT-bz-3`).

**THE SERVED INPUTS for round 119 (read-only fixtures; COPY into `lib/research/print/tests/fixtures/` under the same names, your `<paths>` grants that folder):** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round119_prep/fixtures/bz_served_thesis_<NAME>.json` for `RIO_LN`, `ICT_PM`, `GOOGL_US`, `ICICIBC_IN`, `HD_US`, `BA_US`, `KMB_US` and `TSM_US` (the eight names the CVO reads), each the served `GET /thesis` body of `opal-amgt-scoped-api` for that name on 2026-10-18 ~11:4xZ (CodeSha256 `H3dCSGL..`), trimmed to `header_figures`, `dossier_fields`, `ai_fill`, `drafted_sections`, `drafting_*`, `posture`, `management`, `identity`. The existing `bx_served_thesis_*.json` fixtures (round 117) are the same shape for three of them.

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
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~518/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bz-2"><invocation>cd C:/dev/wk-resapp-518 &amp;&amp; timeout 500 python -m pytest lib/research/print/tests/test_bz2_rich_management_equals_pdf.py lib/research/api/tests/test_bz2_rich_route_management_input.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `7 passed` or more with 0 failed and 0 skipped (M1 once per name, M2 to M7 present by name), and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bz-2"><invocation>cd C:/dev/wk-resapp-518 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 249 passed`), and the summary reads `1 failed, P passed` with P at least 253</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~518 <0.9.0_WK_AMGT_RESAPP~518@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~518/BZ2_RECEIPT.md` with the sections `## What changed` (every path, with line counts), `## Census` (the table the cell's Step A asks for, with its denominator), `## Tests re-scoped` (or `none`) and `## Not verified` (the deployed Lambda serves the old renderer until `AMGT-bx-5`; the whole api folder is not run in this sparse worktree: the issuer runs it in the full tree). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~518/AMGT_RESAPP.TO-AMGT-bz-2.the-rich-export-reads-the-ceo-profile-from-the-same-input-as-the-pdf.proof_of_spec.json` (the invocations are recorded as the order's literal text; a re-run in another tree goes in `output_evidence` and `status_reason`, never in `invocation`). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W518-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate; round 116's rows S7 to S10 omitted it)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the census table; every existing test you re-scoped (old and new assertion); the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Item 2 of the CTO's round-118 analysis and the CVO's finding C-S195. The issuer's own reading, from the served `management` objects of the eight names (fixtures): `ceo_profile_reading` is `UNREADABLE_OBJECT` on all eight, and `ceo_public_profile` is a dict only for HD US and BA US: the hypothesis the face gives the worker to verify, not a conclusion. The rich route's reader is a `scoped_amgt.py` region granted here, as in `by-2`. LOCAL code cell.

<status>pending</status>
<round>119</round>
<slot>0.9.0_WK_AMGT_RESAPP~518</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
