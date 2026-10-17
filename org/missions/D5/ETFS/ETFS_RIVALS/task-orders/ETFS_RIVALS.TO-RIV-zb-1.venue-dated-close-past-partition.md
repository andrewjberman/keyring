# ETFS_RIVALS task order -- `RIV-zb-1` -- A PAST PARTITION'S CLOSE COMES ONLY FROM THE HISTORICAL ANSWER DATED D, NEVER THE 11:00Z SNAPSHOT

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/ETFS/ETFS_RIVALS/decompositions/ETFS_RIVALS_DECOMP.md</decomp_doc>
<owned_cells>RIV-zb-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ETFS_RIVALS~46</issued_to>
<issued_by>2.0.0_SA_COO~RV</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule, cron or trigger is added or moved by this cell
comp-iam: DECLARED-NOT-APPLICABLE no IAM grant, role or policy changes in this cell; no S3 or deploy act
comp-adversary: DECLARED-NOT-APPLICABLE the validator-context composer profiles RETURNED work; at the cut nothing is returned, and the evidence context is this order's check file (dry-run at the base: 4 failed, 2 passed as expected)
</preflight>

**Project:** ETFS_RIVALS (D5/ETFS, fabric dell1) -- *rivalfunds*: a daily research page on rival active ETFs (13 funds, two
peer groups): rankings, buying trend, AI accounts, a security dialog per holding with a price chart, and an audit page.
Code: `data/etfs/scripts/rivalfunds/` (run from `data/etfs/scripts`, package `rivalfunds`); tests:
`data/etfs/scripts/rivalfunds/tests/` (pytest from `data/etfs/scripts`).

## 1. YOUR CELL (inlined verbatim from the decomposition)

### `RIV-zb-1` -- a PAST partition's price group comes only from the historical request dated D, asked for the price fields alone; the reference PX_LAST is never filed under a past partition (rows Z-S85, D1-S21; CTO msg 7376) -- APPENDED 2026-10-17, revision 1.34
- Placement: Z-S85 measured that the daily pull files PX_LAST taken at about 11:00Z under NYSE T-1 for every venue (Asian closes one trading day late, European values not a close; 2026-10-15: 391 of 760 rows).
- Measured (2026-10-17, live S3 read-only): the 2026-10-15 daily object `market-20261016T110918Z-9d4d85356022.parquet` has 579 rows, `as_of_source_counts` {"historical": 0, "pull": 579}. Cause, in `_market_pull` (about line 648): the historical request asks `MARKET_HIST_FIELDS` (every market field but the name: the seven GICS fields, PX_LAST, CRNCY and total return) and accepts a security only when EVERY one of them is non-missing; the history service does not return the GICS fields, so no security is ever accepted and every row is the current-value (reference) snapshot.
- Interface: (1) `MARKET_HIST_FIELDS` becomes `["PX_LAST", "DAY_TO_DAY_TOT_RETURN_GROSS_DVDS"]` (the price group the history service serves). (2) For a past partition D: one historical request per batch for `MARKET_HIST_FIELDS`, start = end = D; a security whose answer dated D carries a non-missing PX_LAST is HISTORICAL: `px_close` and `total_return_index` from that answer, `price_date` = D, `as_of` = D, `as_of_source` "historical", `source` `MARKET_SOURCE_HIST`. (3) The reference (current-value) request is sent for EVERY security of a past partition, and every row takes its descriptive fields (`MARKET_MAP` less PX_LAST and total return: GICS levels, CRNCY, the name, and the parsekey for an identifier-keyed request) from it. (4) A security with no historical PX_LAST dated D (no answer, an answer dated otherwise, or a failed historical request) lands with `px_close` and `total_return_index` NULL -- never the reference PX_LAST or total return -- labelled as today (`as_of` = the run date, `as_of_source` "pull", `source` `MARKET_SOURCE_LIVE`). (5) `as_of_source_counts` and `historical_request_failures` keep their meaning; a reference failure behaves as today (PARTIAL/FAILED); the all-empty refusal (RIV-eg-1) counts a row with descriptors as usable, as today. (6) A run-date partition (D = the run date) is unchanged: no historical request, the reference PX_LAST stands. (7) `daily` mode reaches the same `_market_pull`, so it takes the same rule.
- Out of bounds: `_market_range`, `_history_owed`, `_held_tr`, the dividends pull, every reader and stage, `bbg_budget.py` and its config, any S3 write outside a LocalSink, any vendor call, Terraform and the Lambda.
- Checks: `round33/checks/zb1_venue_dated_close_check.py` (AC1 the past partition's price group and descriptors, two tests; AC2 a misdated or failed historical answer, two tests; AC3 the run-date partition and daily mode, two tests; base 4 failed, 2 passed). The existing `tests/test_r5s6_as_of_guard.py` pins the old rule (a PX_LAST-only answer is "not historical"; a past partition files the reference PX_LAST): the worker amends exactly those assertions to the new rule and reports each. J1: none (a LOCAL cell; the vehicle update and the re-sourcing are each their own pair, `SERVED` paths).

## 2. WHAT YOU NEED TO KNOW (measured at the cut, base box/dell1)

- Read the check before you build: `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round33/checks/zb1_venue_dated_close_check.py`. At the base it reads 4 failed, 2 passed (the descriptor test and the run-date test pass already and must stay green); do not edit it. It stubs `e._blp_historical_data`, `e._blp_reference_data` and `e._run_date_et`, and (for daily mode) `e._daily_dividends`.
- `MARKET_HIST_FIELDS` is defined at about line 166 of `enrichment_bloomberg.py`; `_market_pull` starts at about line 629. Its past-partition branch is about lines 647-660 (the historical request and the every-field acceptance), the reference batches about 661-678, the identifier-keyed parsekey-only request about 679-693, and the labels/rows about 699-713. Today a security the historical request accepts is NOT sent to the reference request; under the new rule every security of a past partition is sent to it (for descriptors), and the historical answer supplies only the price group. Keep the RIV-pk-1 split (identifier-keyed requests also ask PARSEKYABLE_DES) on that one reference pass; the separate parsekey-only pass for historical identifier-keyed securities is then no longer needed.
- `market_rows(data, date, source, provenance, as_of_source, labels)` builds one row per security from a {security: {field: value}} map and a per-security label (as_of, as_of_source, source). Build each security's field map as: the reference body with PX_LAST and DAY_TO_DAY_TOT_RETURN_GROSS_DVDS removed, plus (historical only) the historical PX_LAST and total return; set `price_date` = D on the historical rows after `market_rows`, as `_history_owed` does.
- Three test files compare a stub's `fields` argument to `eb.MARKET_HIST_FIELDS` (`test_r27tw1_history_owed_leg.py`, `test_r28tc1_topup_currency_and_page_day.py`, `test_r12pk1_parsekey_join.py`); they read the constant, so they follow the new value. `tests/test_r5s6_as_of_guard.py` pins the old rule; amend only the assertions that the new rule changes, and list each with its reason in your report.
- Regression net: `cd data/etfs/scripts && python -m pytest -q rivalfunds/tests`; report its final line. Two failures predate this cell (`test_r15bf1_market_range.py::test_budget_remainder_refuses_and_check_points_names_it`, `test_r9cb1_bbg_budget.py::test_shipped_config_keeps_a_reserve_below_the_measured_exhaustion`: they read the committed budget config); report any other failure.

## 3. SURFACES AND BOUNDS

You READ (never edit): every file not in your `<paths>`, including `lib/`, `integrations/`, Terraform, the decomposition and
the PRD `org/missions/D5/ETFS/ETFS_RIVALS/prd/ETFS_RIVALS_PRD.md`.

You WRITE only the `<paths>` below (plus `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~46/`).
NEVER: any S3 read or write outside a LocalSink or memory sink, any deploy, gateway release or Terraform, any vendor call
(Bloomberg, OpenAI, Bright Data or any live web search), any Secrets Manager call, any environment gate flip outside a test.
A row you file goes in the investigation file below with id `ETFS_RIVALS-D1-W46-S<k>`, `"fabric": "dell1"`, `surfaced_at` = `date -u +%FT%TZ` at filing.

<paths>
data/etfs/scripts/rivalfunds/enrichment_bloomberg.py
data/etfs/scripts/rivalfunds/tests/test_r5s6_as_of_guard.py
data/etfs/scripts/rivalfunds/tests/test_riv_zb1_venue_dated_close.py
data/etfs/scripts/rivalfunds/tests/test_r10eg1_refuse_empty.py
data/etfs/scripts/rivalfunds/tests/test_r12pk1_parsekey_join.py
data/etfs/scripts/rivalfunds/tests/test_r27tw1_history_owed_leg.py
data/etfs/scripts/rivalfunds/tests/test_r28tc1_topup_currency_and_page_day.py
data/etfs/scripts/rivalfunds/tests/test_r7nm2_security_name.py
org/missions/D5/ETFS/ETFS_RIVALS/surprise-channel/investigations/INVESTIGATION_v1.dell1.md
</paths>

## 4. PROOF OF SPEC (each invocation LITERAL, run from the repository root)

- **AC1** -- a past partition's price group is the historical answer dated D; descriptors come from the reference request for every security.
- **AC2** -- a historical value dated otherwise, or a failed historical request, never prices the partition; descriptors still land.
- **AC3** -- a run-date partition still takes the current pull and asks no history; daily mode takes the same past-partition rule.
<proof_of_spec>
  <criterion id="AC1" cell_refs="RIV-zb-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round33/checks/zb1_venue_dated_close_check.py -k ac1</invocation><expect>2 passed</expect></criterion>
  <criterion id="AC2" cell_refs="RIV-zb-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round33/checks/zb1_venue_dated_close_check.py -k ac2</invocation><expect>2 passed</expect></criterion>
  <criterion id="AC3" cell_refs="RIV-zb-1"><invocation>cd data/etfs/scripts; python -m pytest -q -p no:cacheprovider ../../../org/missions/D5/ETFS/ETFS_RIVALS/deliverables/2.0.0_SA_COO~RV/round33/checks/zb1_venue_dated_close_check.py -k ac3</invocation><expect>2 passed</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Add `rivalfunds/tests/test_riv_zb1_venue_dated_close.py`: one test per behaviour you added that the check file does not pin (for example an identifier-keyed security on a past partition still carries its parsekey, and the manifest's `as_of_source_counts`). Run the rivalfunds suite (`python -m pytest -q rivalfunds/tests` from `data/etfs/scripts`) and report its final line.
Write the instance at `org/missions/D5/ETFS/ETFS_RIVALS/deliverables/0.9.0_WK_ETFS_RIVALS~46/ETFS_RIVALS.TO-RIV-zb-1.venue-dated-close-past-partition.proof_of_spec.json` with `to_id` `ETFS_RIVALS.TO-RIV-zb-1.venue-dated-close-past-partition`. Report once: each criterion's verdict line with the output above it;
files written; every existing test assertion you changed and why; rows filed (id + one line); anything the issuer must do at
the merge. Leave the `<status>` flip to the issuer.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES (L6, 2.0.0_SA_COO~RV):** Round 33, ONE issuance, one cell, on `1.0.0_SA_CTO~DELL1` msg 7376 (ruled on this seat's recommendation) and msg 7379 (order 3 act 3 waits on this fix). Decomposition revision 1.34. `fanout: 1 of 1 chains, cap 8`. Check file dry-run at the base before the cut: 4 failed, 2 passed (the two controls). At the drain: merge; the 10-15 misdated-row count before (391 of 760, Z-S85) and after; the re-sourcing units file (non-US securities' daily "pull" rows over the 365-day window) and its held-tr run at site Z under a never-widen pair; the site-Z working-tree update so the 11:00Z vehicle runs this code, under its own pair; then the order-3 replay re-run and act 3's pair.

**AMENDMENT 1 (2.0.0_SA_COO~RV, 2026-10-17 ~07:0xZ):** `<paths>` gains five test files the worker's rows ETFS_RIVALS-D1-W46-S1..S4 name (test_r10eg1, test_r12pk1, test_r27tw1, test_r28tc1, test_r7nm2): each pins the old past-partition rule (a reference PX_LAST under a past partition, a ten-field historical request, the parsekey-only pass, a history answer carrying CRNCY). The worker amends exactly the assertions and fixtures the new rule changes. The issuer's premise in section 2 that three files only read the constant was wrong; five encode the rule. Criteria unchanged. Gate: none of `.tools/to-pipeline-gate.py`'s limbs grades a modification of an order that declares no `<placeholders>` (LIMB 6 fires on a NEWLY-ADDED order only); this amendment was graded by none.

<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<status>pending</status>
<round>33</round>
<workstream>1</workstream>
<slot>~46</slot>
<fabric>dell1</fabric>
