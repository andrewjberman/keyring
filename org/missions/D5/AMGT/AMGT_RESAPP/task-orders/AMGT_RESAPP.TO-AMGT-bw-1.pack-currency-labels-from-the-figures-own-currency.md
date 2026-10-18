# AMGT_RESAPP task order -- `AMGT-bw-1` -- EVERY MONEY FIGURE THE PRINTED PACK LABELS CARRIES THE CURRENCY THE FIGURE ITSELF IS HELD IN, READ THE WAY THE PAGE READS IT: A CENSUS OF EVERY CURRENCY-LABELLED PACK FIELD FIRST, THEN ONE RULE (C-S186)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-bw-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~510</issued_to>
<issued_by>2.0.0_SA_COO~R1</issued_by>
<to_id>AMGT_RESAPP.TO-AMGT-bw-1.pack-currency-labels-from-the-figures-own-currency</to_id>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence; renderer edits, one test file and fixtures.
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call, no read or write path changes.
comp-adversary: RUN at the cut -- the live packs of ICT PM and RIO LN (captured 2026-10-18 ~03:20Z, `deliverables/2.0.0_SA_COO~R1/round115/packs/`) print the labels in the table below; AC1 FAILS at the base (the new test file does not exist, exit 1). AC2 at the base reads `1 failed, 125 passed` (the one failure named below), so its expectation of P at least 132 is unmet there as expected: it is a regression guard plus a count.
EGRESS CLASS, declared: NONE (the tests build packs from committed fixtures; no HTTP, no S3, no Bloomberg).
</preflight>

**Your worktree:** `C:/dev/wk-resapp-510` (branch `wk-AMGT_RESAPP-510`, cut from the issuance commit; its nested portal worktree is cut at PROD `ff611566` and is READ-ONLY for you: the pack tests read the page's fixtures from it). Work and commit only in the outer worktree. The shell's working directory resets between calls: start EVERY shell call with `cd C:/dev/wk-resapp-510`; a call that starts elsewhere resolves `git rev-parse --show-toplevel` to the base checkout and answers about the wrong tree.

## 1. THE CELL -- `AMGT-bw-1` (round 116, decomposition s.125)

The CVO graded FWD-5 NOT MET (`3.0.0_SA_CVO` msg 7886, round 115) on a read of three live printed packs, and the CTO's round-115 analysis item 1 (`ledger/ROUND_ANALYSIS.round115.R1.md`, graduated finding C-S186) is this cell: **the printed pack labels a figure with a currency that is not the figure's own.** Facts the issuer read from the page's served data on 2026-10-18 (`GET /api/scoped/amgt/security/<key>/thesis`, `header_figures`, each figure's own `currency` and `unit`):

| name | figure | served value | own `currency` | `unit` | what the live PACK prints today |
|---|---|---|---|---|---|
| ICT PM | `CRNCY` (the trading currency) | `PHP` | none | TEXT | |
| ICT PM | `EQY_FUND_CRNCY` (the reporting currency) | `USD` | none | TEXT | |
| ICT PM | `CUR_MKT_CAP` | 1,735,465,117,700 | `PHP` | ABSOLUTE | prints a PHP figure |
| ICT PM | `CRNCY_ADJ_MKT_CAP` | 1,735,465.1177 | `PHP` | MILLIONS | **`Market value, currency-adjusted: USD 1,735,465.1 million`** (a PHP number labelled USD: it states USD 1.7 trillion; the page's own What Changed row reads PHP 1.74T) |
| ICT PM | `CURR_ENTP_VAL` | 33,087.5 | `USD` | MILLIONS | |
| ICT PM | `PX_LAST` | 860.0 | `PHP` | PRICE | |
| RIO LN | `CRNCY` | `GBp` (pence) | none | TEXT | |
| RIO LN | `EQY_FUND_CRNCY` | `USD` | none | TEXT | |
| RIO LN | `PX_LAST` | 6,816.0 | `GBp` | PRICE | |
| RIO LN | `CUR_MKT_CAP` | 115,578,925,918 | **none** | ABSOLUTE | **`Market cap: GBp 115,578.9 million`** (pence on a value whose figure carries no currency; the CVO read it as a USD value) |
| RIO LN | `CURR_ENTP_VAL` | 173,616.0 | none | MILLIONS | |
| RIO LN | `CRNCY_ADJ_MKT_CAP` | 115,578.9 | none | MILLIONS | |
| GOOGL US | `CRNCY` | `USD` | none | TEXT | |
| GOOGL US | `CUR_MKT_CAP` | 4,143,539,940,000 | `USD` | ABSOLUTE | clean (the control) |
| GOOGL US | `CRNCY_ADJ_MKT_CAP` | 4,143,539.94 | `USD` | MILLIONS | clean |

**The mechanism you will confirm by reading** (`lib/research/print/render_pack.py`): `build_pack` derives `trading_cur = _currency_of(header_figs, "CRNCY", "EQY_FUND_CRNCY")` and `reporting_cur = _currency_of(header_figs, "EQY_FUND_CRNCY", "CRNCY")` ONCE and passes them to `_header_print_lines`, `_plain_figure_line`, `_description_line` and `_format_figure_value`, which print every monetary figure with one of those two codes (`_money`: `"{currency or 'local currency'} {amount}{tail}"`) instead of the code the FIGURE carries. The page does the opposite: each header tile reads its OWN served `currency` (`portal/src/pages/SecurityAnalysis/priceCurrency.ts` `currencyCodeOf` and `priceCurrencyOf`; `components/StatTile.tsx` `formatStatValue`; `components/HeaderCards.tsx`), and a figure that carries none prints the page's `CURRENCY_UNCONFIRMED_WORDS` ("currency ... not confirmed": read the exact words in `StatTile.tsx`), never a guessed code. **Read those four page files first** (`portal/` in your worktree is a read-only PROD checkout) and mirror their rule exactly in Python: the label is the currency the figure's own served field carries, read through ONE helper, never typed per field.

**Step A, the census FIRST (a deliverable: the receipt's `## Currency census` section and a committed fixture `lib/research/print/tests/fixtures/bw1_currency_fields.json`).** List EVERY field `build_pack` (PDF/txt) prints with a currency label or a money amount, as `{function, line, mnemonic or field, the code it prints today and how it is chosen, the figure's own served currency (or none), disposition}` where disposition is `own_currency` (already right), `fixed_here` (the label now reads the figure's own code), `no_own_currency` (the figure carries none: it prints the page's unconfirmed words) or `not_money` (no currency is printed). Method: read `_format_figure_value`, `_plain_figure_line`, `_header_print_lines`, `_header_figures_for_print`, `_description_line`, `_money`, `_currency_of` and the lines in `build_pack` that call them; read each in context. Print the denominator (functions read, fields listed). Also report (read only) whether the `format=rich` path (`render_print.render_figure_line`) labels currencies the same wrong way: name it, do not edit it.

**Step B, the rule.** In `render_pack.py` ONLY: (1) a figure's printed currency code is its OWN served `currency` field (the block's figure dict key the page reads: confirm its name in the model-block fixtures and in `lib/research/provenance/render_print.py`), trimmed (a padded code prints trimmed: round 114's lesson); (2) a money figure whose own `currency` is absent prints the page's unconfirmed words in place of a code, never `trading_cur` or `reporting_cur`; (3) `CRNCY` and `EQY_FUND_CRNCY` stay what they are (text fields, printed as their value); (4) **"currency-adjusted" is printed ONLY if a conversion actually happened and then it names its rate**: read how the page labels `CRNCY_ADJ_MKT_CAP` (`CRNCY_ADJ_MKT_CAP` is the market cap "in the requested currency"): when the figure's own currency equals the trading currency no conversion happened and the label must NOT say "currency-adjusted"; the pack carries no rate, so a converted figure prints its own currency code and the words "converted, rate not carried" (state in the receipt which of the three names, if any, has a converted figure: from the served data above none of the three does). Display only: no served value, sort key or comparison changes. Do not reword any sentence beyond the labels; do not edit `render_print.py`, `scoped_amgt.py` or the page.

**The grade is on the RENDERED text.** The new test `lib/research/print/tests/test_bw1_currency_labels.py` (YOURS: create it; build the three packs on the pattern of `test_bu3_pack_long_dates.py` and `test_bv2_rich_dates_and_quotes.py`, which build from `lib/research/print/tests/fixtures/bu3_block_RIO_LN.json` and its siblings; add your OWN synthetic header-figure fixtures for ICT PM, RIO LN and GOOGL US carrying exactly the currency, value and unit facts of the table above, labelled synthetic) checks, each named: C1 ICT PM: `CRNCY_ADJ_MKT_CAP` prints `PHP 1,735,465.1 million` (the figure's own code, no `currency-adjusted` wording, no `USD` on that line) and `CURR_ENTP_VAL` prints `USD 33,087.5 million`; C2 RIO LN: `CUR_MKT_CAP` and `CRNCY_ADJ_MKT_CAP` print no `GBp` and no invented code: they print the page's unconfirmed words with the amount, and `PX_LAST` prints `GBp 6,816`; C3 GOOGL US (control): its lines are UNCHANGED from the base text (record the base text BEFORE the edit; compare after normalising `\r\n` to `\n` on both sides: row S58); C4 EVERY printed money line of the three packs equals the fixture figure in currency and magnitude (a hand-written expected table from the facts above, never computed by the code under test: print each line you compared); C5 a padded own code (`' PHP '`) prints trimmed; C6 the census fixture exists, its printed denominator equals its entry count, and no entry reads `printed code is not the figure's own` after the fix; C7 the base-text lines for ICT PM and RIO LN differ from the edited text ONLY on lines carrying a money label (the issuer's no-collateral-change control: record the base text first). Expected strings are written by hand; use `pypdf` or `fitz` for the PDF text where one imports and say which, else the renderer's pre-PDF line list.

**AMENDMENT 1 (issuer, 2026-10-18 ~04:4xZ), after the first worker's report.** The first worker (slot ~510) committed the rule at `78c948c919` and the receipt, instance and rows at `4ba739b81e` on this branch, and stopped on row W510-S1: once the labels read each figure's own currency, `CRNCY_ADJ_MKT_CAP` prints the SAME text as `CUR_MKT_CAP` on all three names, so the existing same-value dedup in `_header_figures_for_print` (the second `Market value, currency-adjusted` line is kept only when its printed text DIFFERS from the primary `Market cap` line) drops it, and the order's C1 and C2 (which require the alias line to print) fail on their alias-count clause (`assert 1 == 2`). **The issuer rules: the dedup STAYS** (it is the existing rule, GOOGL's control C3 depends on it, and it is right: a second line carrying the same figure in the same currency is a duplicate, and "currency-adjusted" is printed only after a real conversion). **The order's C1 and C2 were wrong to require the alias line, and are corrected here.** You are the SAME slot re-seated; your first commits are INHERITED STATE: add new commits, never amend or rewrite them.

**The corrected expectations (change ONLY the alias-count clauses of your own `test_bw1_currency_labels.py`):** C1 ICT PM: the `Market cap` line prints `PHP 1,735,465.1 million`; there is NO `Market value, currency-adjusted` line (the dedup drops it) and NO line printing a market value in `USD`; `Enterprise value` prints `USD 33,087.5 million`. C2 RIO LN: `Market cap` carries no currency code and prints the page's words for a valued amount with no currency (your row S2: `currency not stated`, read from the page's `StatTile.tsx`); there is NO `Market value, currency-adjusted` line and no `GBp` on a money line other than `PX_LAST`, which prints `GBp 6,816.00`; `Enterprise value` and `Net debt` carry no code either (their own `currency` is none: the same words). C3 GOOGL is unchanged. Also add one assertion, C8-alias, named in the output: a block whose `CRNCY_ADJ_MKT_CAP` value genuinely DIFFERS from `CUR_MKT_CAP` (a synthetic converted figure with its own `currency` `USD` and a trading currency `PHP`) keeps the second line, labelled `Market value, currency-adjusted` with its own code `USD` and the words `converted, rate not carried` (order rule (4)). Then run AC1: all of C1 to C8 pass (11 or more tests) and AC2: exactly ONE FAILED line (the `test_av2_export_equals_page.py` one) and `1 failed, P passed` with P at least 132.

**Remaining steps for the re-seated worker.** (1) `cd C:/dev/wk-resapp-510` and confirm the branch head `4ba739b81e`. (2) Edit your test as above, re-run, record which assertions changed. (3) Update the receipt (`## What changed`, a line on the dedup ruling) and the proof-of-spec instance as new commits (invocations stay the order's literal text); run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes (VALID) and report once. In the report also name every existing test you changed (you listed four in your first report: confirm the list and the reason for each), and say which money lines of the three packs now print the words for a missing currency.

**Do this in order.** (1) `cd C:/dev/wk-resapp-510`; `git log -1 --format=%h` and `git status --short` (clean apart from the `portal` link). (2) Write the census (Step A) and the fixtures. (3) Create the test file FIRST, record the base texts, and run it ONCE on the unedited head: it must fail on C1, C2 and C4 (and C6 if the census records unfixed entries), pass on C3, C5-if-trivially and C7; record that run. (4) Make the Step B edit. (5) Run AC1 and AC2. (6) Write the receipt `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~510/BW1_RECEIPT.md` with the sections `## Currency census`, `## What changed` (every path, with line counts), `## What the rich export does` and `## Not verified` (the deployed Lambda serves the old renderer until the round-116 redeploy `AMGT-bw-5`; no live pack is looked at here).

Stamp any surprise row's `surfaced_at` with `date -u +%FT%TZ` at filing. Rows: id form `AMGT_RESAPP-D1-W510-S<k>`, `disarm_owner` `2.0.0_SA_COO~R1` (a null `disarm_owner` is refused by the surprise-row gate).

## 2. BOUNDS

1. Write only the paths below. No deploy, no Terraform, no store write, no schedule, no SEC, vendor, model or Bloomberg call; no `pip install`, `bun` or `npm`; nothing is fetched from the internet. No push; never touch `DEV` or `PROD`.
2. `render_pack.py` is the only product file you edit (and only its currency-labelling functions: another worker edits `build_pack`'s structure in the same file in this round); do NOT edit `lib/research/provenance/render_print.py`, `lib/research/freshness/long_day.py`, `scoped_amgt.py` or the portal. Standing: no S3 delete, no push of shared branches.
3. Commit nothing under `portal/` or `org/devices/`.
4. **Committed fixtures are SYNTHETIC or the issuer's quoted served values** (the figures this face prints are what the page serves to staff on 2026-10-18); never read a live store, never copy a landed model block into the repository.

## 3. SURFACES

<paths>
lib/research/print/render_pack.py
lib/research/print/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~510/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

## 4. PROOF OF SPEC (literal; each invocation bounded by its own `timeout`; set your shell tool's timeout to 600000 ms)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-bw-1"><invocation>cd C:/dev/wk-resapp-510 &amp;&amp; timeout 300 python -m pytest lib/research/print/tests/test_bw1_currency_labels.py -q -p no:cacheprovider --color=no; echo "exit=$?"</invocation><expect>the pytest summary line reads `7 passed` or more with 0 failed and 0 skipped, C1 to C7 each present by name, and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-bw-1"><invocation>cd C:/dev/wk-resapp-510 &amp;&amp; timeout 580 python -m pytest lib/research/print/tests -q -p no:cacheprovider --color=no 2&gt;&amp;1 | grep -E "^FAILED|passed|failed" | sed "s/ - .*//"</invocation><expect>exactly one FAILED line, `FAILED lib/research/print/tests/test_av2_export_equals_page.py::test_pdf_text_carries_no_field_code_and_names_every_line_in_words` (it fails at the base as well: the base reads `1 failed, 125 passed`), and the summary reads `1 failed, P passed` with P at least 132</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Commit in your worktree via `.tools/safe-commit.sh --author "0.9.0_WK_AMGT_RESAPP~510 <0.9.0_WK_AMGT_RESAPP~510@opal.agent>" -F <msgfile> -- <paths>` (message file written with the Write tool, never a shell heredoc; confirm with `git log -1`). Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~510/AMGT_RESAPP.TO-AMGT-bw-1.pack-currency-labels-from-the-figures-own-currency.proof_of_spec.json` (the invocations are recorded as the order's literal text; any re-run in another tree goes in `output_evidence` and `status_reason`, never in `invocation`). Run `python .tools/proof-of-spec-check.py <instance> --governing-order <this order's path>` on the committed bytes and report its verdict line. Do not stage `portal`.

Report once:
- the commit hash and the base;
- the test run at the unedited head (the line and the failing checks) and the run after;
- AC1's and AC2's output lines;
- the receipt's census section, verbatim;
- any existing test you changed, named, with the reason;
- any row.

The `<status>` flip is the issuer's.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** the CTO's round-115 analysis item 1 (`ledger/ROUND_ANALYSIS.round115.R1.md`, msg 7887), the CVO's FWD-5 read (msg 7886). LOCAL code cell; served only through `AMGT-bw-5` (placed: a never-widen pair cut after this cell and bw-2 merge). Runs in parallel with `bw-2` on the same file in a different region (currency functions, lines ~410-640, against `build_pack`, lines ~689-976); the merge may need one hand resolution. The faces' served-value table was read by the issuer from `/thesis` `header_figures` on 2026-10-18. The issuer's real grade after the redeploy: each currency-labelled figure of the live ICT PM, RIO LN and GOOGL packs against the page's served figure in currency and magnitude.

<status>pending</status>
<round>116</round>
<slot>0.9.0_WK_AMGT_RESAPP~510</slot>
<fabric>dell1</fabric>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
