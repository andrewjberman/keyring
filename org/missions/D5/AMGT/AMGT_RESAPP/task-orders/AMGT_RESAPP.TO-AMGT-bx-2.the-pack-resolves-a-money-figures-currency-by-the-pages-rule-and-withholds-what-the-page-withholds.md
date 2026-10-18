# AMGT_RESAPP task order -- `AMGT-bx-2` -- THE PACK RESOLVES EACH MONEY FIGURE'S CURRENCY BY THE PAGE'S OWN RULE: THE FIGURE'S OWN CODE, AND THE AMOUNT WITHHELD WHERE THE PAGE WITHHOLDS IT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bx-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~513</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bx-2.the-pack-resolves-a-money-figures-currency-by-the-pages-rule-and-withholds-what-the-page-withholds</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; a renderer change and its tests.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut (2026-10-18): AC1 at the base fails (the test file is absent); AC2 at the base reads `1 failed, 146 passed` (the one known failure) and its floor P is unmet there as expected. EGRESS CLASS, declared: NONE (the tests build packs from committed fixtures; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-513` (branch `wk-AMGT_RESAPP-513`, cut from the issuance commit; its nested `portal/` is read-only and carries the page's source at `origin/DEV` `3a7791c1`, which you READ for the page's rule and never edit). Work and commit only in the outer worktree. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-513`.

**THREE ROUND-116 LESSONS THAT BIND YOUR TESTS.** (1) Two cells of this round edit `lib/research/print/render_pack.py` in different regions and are merged by the issuer; **a test of yours that compares a pack's WHOLE text to a recorded text fails the moment another cell's section lands.** Compare a SECTION (the lines between two headings) or the FIGURE lines (the `Appendix: model figures` block) or a named line, never the whole text. (2) Read `lib/research/print/tests/test_bw2_pack_form.py` and `test_bw1_currency_labels.py` first: they build a pack from committed fixtures with `build_pack` and read its text; copy their way, change nothing in them unless an assertion of theirs pins the exact old behaviour your cell changes: then re-scope that ONE assertion with a hand-written expectation, name it in the receipt (`## Tests re-scoped`: old and new), and the issuer re-runs the whole print plus api folders in the full tree after the merge. (3) A new check is dry-run at the base first: your test file runs ONCE on the unedited head and must fail on the new behaviour and pass on every control; record the counts.

**THE SERVED INPUTS (read-only fixtures; COPY them into `lib/research/print/tests/fixtures/` under the same names, your `<paths>` grants that folder):** `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round117_prep/fixtures/bx_served_thesis_RIO_LN.json`, `..._ICT_PM.json`, `..._GOOGL_US.json`. Each is the served `GET /thesis` body of `opal-amgt-scoped-api` for that name on 2026-10-18 (CodeSha256 `lNWo6Cm6..`), trimmed to `header_figures`, `dossier_fields`, `ai_fill`, `drafted_sections`, `drafting_*`, `posture`, `management`, `identity`. The pack route hands `build_pack` this bundle as `thesis_bundle`, and the model block carries the same `header_figures`; the existing bw fixtures show how a test assembles a block and a bundle. You call no AWS, no HTTP and no vendor.

## 1. THE CELL -- `AMGT-bx-2` (round 117, decomposition s.126, item 3 of the CTO's round-116 analysis)

**What the CVO read (C-S186, narrowed).** After round 116 the pack's money lines carry each figure's OWN served currency, but RIO LN's header prints `Market cap: 115,578.9 million currency not stated`, `Net debt: 14,512.0 million currency not stated` and `Enterprise value: 173,616.0 million currency not stated`, and ICT PM prints `Net debt: 3,648.9 million currency not stated`, where the CTO's grade is that the pack's currency rule be THE PAGE'S rule ("never a per-field guess"; "currency not stated remains only where the page also states none").

**What the page does (read it, it is the specification):** `portal/src/pages/SecurityAnalysis/components/StatTile.tsx` (`formatStatValue`, `isUnmeasuredBasis`, `figureBasis`, `moneyNoCode`, `CURRENCY_UNCONFIRMED_WORDS`, `moneyPrefix`), `components/HeaderCards.tsx` (`resolveFigure`, `withheldReason`) and `priceCurrency.ts`. In short: a header money figure whose served `currency_basis` begins `UNMEASURED` is NOT SHOWN: the tile body is a dash and the reason rides the hover, the words `Bloomberg does not confirm this figure's currency`; a MEASURED figure prints `<code> <amount>` from its own served `currency`; a measured figure with no own currency prints `<amount> currency not stated`. **The served data of the three names (fixtures; hand-written expectations):** RIO LN `CUR_MKT_CAP`, `NET_DEBT`, `CURR_ENTP_VAL` and `CRNCY_ADJ_MKT_CAP` all carry NO own currency and a `currency_basis` beginning `UNMEASURED` (so the PAGE WITHHOLDS all four; it shows no amount and no currency for them), while `PX_LAST` (GBp) and `AVG_DAILY_VALUE_TRADED_3M` (GBp) are measured; ICT PM `CUR_MKT_CAP` PHP and `CRNCY_ADJ_MKT_CAP` PHP and `CURR_ENTP_VAL` USD and `PX_LAST` PHP are measured, `NET_DEBT` carries no currency and an UNMEASURED basis (withheld); GOOGL US: all USD, measured. **So the issuer's reading is: there is no served USD for RIO LN's market cap, net debt or enterprise value; the pack's correct behaviour is the page's, which is to withhold them.** (If your census finds a served source that gives these figures a currency the page shows, report it as a surprise row with the field and its served value, and build to the page's rule regardless.)

**The rule to build:** a header money figure (the `Header` block and the key figures the pack prints) is printed by the page's rule: (1) basis `UNMEASURED` and a money unit: the amount is NOT printed; the line reads `<label>: Bloomberg does not confirm this figure's currency - <source>` (the page's words, verbatim); (2) measured with an own currency: `<code> <amount> <unit words>` as today; (3) measured with no own currency: `<amount> <unit words> currency not stated` as today. The second market-value line (`Market value, currency-adjusted`) keeps the round-116 dedup and conversion naming, and is withheld the same way when its basis is UNMEASURED. FISCAL-YEAR lines are NOT changed (they carry their own currency on every served row: read the three names' `fiscal_year_figures` only to confirm none carries an UNMEASURED basis; the fixtures here carry the header figures only, so build one synthetic fiscal row per basis class and say so). The figure's `currency_basis` is a served field of every figure object (`basis` is the older alias); read it as the page does.

**Do this in order.** (A) `cd C:/dev/wk-resapp-513`; `git log -1 --format=%h`; copy the three fixtures; build the CENSUS TABLE first: for each money-unit header figure of each of the three names, the served `currency`, the served `currency_basis`, what the PAGE prints (by the rule above; hand-written) and what the PACK prints today (run `build_pack` on the base); write it as the fixture `lib/research/print/tests/fixtures/bx2_page_rule_table.json` and as the receipt's `## Census`. (B) Write `lib/research/print/tests/test_bx2_currency_page_rule.py` FIRST and run it ONCE on the unedited head (K1, K2, K5 must fail; K3, K4, K6 pass: record the counts). (C) Build the rule in the figure-line functions only; re-run. (D) AC1, AC2, then the receipt, instance and proof-of-spec-check.

**Tests (`test_bx2_currency_page_rule.py`; hand-written expectations from the census table; models are the bw tests):** K1 RIO LN: the `Market cap`, `Net debt` and `Enterprise value` lines each equal `<label>: Bloomberg does not confirm this figure's currency - Bloomberg` and carry NO digit of the amount and no currency code; `PX_LAST` still prints `GBp 6,816.00 per share`; K2 ICT PM: `Net debt` is withheld the same way, `Market cap` prints `PHP 1,735,465.1 million`, `Enterprise value` prints `USD 33,087.5 million`, `Share price (last close)` prints `PHP 860.00 per share`; K3 CONTROL GOOGL US: every money line is byte-identical to the base (the table's base column) and none carries the withheld words or `currency not stated`; K4 a synthetic MEASURED figure with a code prints it, and a synthetic MEASURED figure with no code prints `currency not stated`; K5 a synthetic UNMEASURED figure with an own code (the page's rule withholds on the basis alone) is withheld; K6 the fiscal-year lines of the three names (the `Fiscal year` blocks of a pack built from the existing bw fixtures plus your synthetic rows) are equal as a sorted multiset before and after; K7 the page-rule table fixture covers every money-unit header figure of the three names (its denominator equals the count you print) and each printed line agrees with its table row.

**Region you own in `render_pack.py`:** the figure-line functions (`_money`, `_own_currency`, `_format_figure_value`, `_header_figures_for_print`, `_converted` and the header-line printer). You do NOT touch the `Summary`, `Positioning` or `Management` builders or `build_pack`'s section order (cells `AMGT-bx-1` and `AMGT-bx-3`).

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`; commit nothing under `portal/` or `org/devices/`.
2. Product edit: `lib/research/print/render_pack.py` ONLY, and ONLY the region this cell names (two other cells edit other regions of the same file in parallel). Do NOT edit `lib/research/api/scoped_amgt.py`, `render_print.py`, `long_day.py` or the portal.
3. A served state sentence or reason the pack prints never carries a storage path, a bucket key, an object name, an order or cell id (`AMGT-...`) or an UPPER_SNAKE field code: say it in one plain sentence.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~513/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bx-2"><invocation>cd C:/dev/wk-resapp-513 &amp;&amp; timeout 300 python -m pytest lib/research/print/tests/test_bx2_currency_page_rule.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `7 passed` or more with 0 failed and 0 skipped, K1 to K7 each present by name, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bx-2"><invocation>cd C:/dev/wk-resapp-513 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 146 passed`), and the summary reads `1 failed, P passed` with P at least 153</expect></criterion>
  Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~513/AMGT_RESAPP.TO-AMGT-bx-2.the-pack-resolves-a-money-figures-currency-by-the-pages-rule.proof_of_spec.json`.
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~513 <0.9.0_WK_AMGT_RESAPP~513@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~513/BX2_RECEIPT.md` with the sections `## What changed` (every path, with line counts), `## Census` (the table the cell's Step A asks for, with its denominator), `## Tests re-scoped` (or `none`) and `## Not verified` (the deployed Lambda serves the old renderer until `AMGT-bx-5`; the whole api folder is not run in this sparse worktree: the issuer runs it in the full tree). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~513/AMGT_RESAPP.TO-AMGT-bx-2.the-pack-resolves-a-money-figures-currency-by-the-pages-rule.proof_of_spec.json` (the invocations are recorded as the order's literal text; a re-run in another tree goes in `output_evidence` and `status_reason`, never in `invocation`). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W513-S<k>`, **`disarm_owner` `2.0.0_SA_COO~R1` on EVERY row (a row without it is refused by the gate; round 116's rows S7 to S10 omitted it)**.

Report once: the commit hash and the base; the test run at the base and after; AC1 and AC2 output lines; the census table; every existing test you re-scoped (old and new assertion); the proof verdict line; any row. The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** Item 3 of the CTO's round-116 analysis. The CTO's grade text says RIO LN's USD figures should print USD; the issuer's reading of the served data is that the page WITHHOLDS those figures (UNMEASURED basis, no own currency), so the cell builds the page's rule and the issuer reports the divergence to the CTO in the same issuance commit's message. The issuer's own `r116_pack_money_vs_page.py` reads `OK-UNCONFIRMED` for a no-currency figure and does not yet know the withheld rule; the issuer updates it (`AMGT-bx-4`) before the redeploy. LOCAL code cell.

<status>complete</status>
<round>117</round>
<slot>0.9.0_WK_AMGT_RESAPP~513</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
