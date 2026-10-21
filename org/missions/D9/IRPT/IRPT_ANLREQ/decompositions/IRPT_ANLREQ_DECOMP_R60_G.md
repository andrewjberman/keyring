# IRPT_ANLREQ round 60, workstream ~G (ENGINE) -- decomposition: FWD-10 (Core), the Multi-Comp and Comparison reports on Opal's own math

Issuer `2.0.0_SA_COO~G2`, 2026-10-20. PRD v0.25 @b83ce81b5b (both halves SIGNED, CTO msg 11442). Outcome served: **FWD-10**; FWD-12 rides it (a part Opal cannot fill says so in words). FWD-11 (parity) follows once FWD-10 is met and is NOT in this round.

**Input.** PRD C-MODEL-SOURCE and the CTO's R1 (record `deliverables/1.0.0_SA_CTO~DELL2/CTO_RULINGS_MODEL_WEIGHTS_SWAP_AUDIT_20261020.md`, key corrected @b9de1e559d); CRO brief `docs/briefs/irpt-anlreq-report-engine-core-then-parity-brief-20261020.md` O2; trace `0.9.0_WK_IRPT_ANLREQ~304/MODEL_COMPOSITION_TRACE.md`.

## What was measured before the cut (this seat, 2026-10-20, read-only)

- **The model return series exists at the corrected key, the positioning surface at the second.** `opal-data-portal-v2`: `json/benchmarks/model_portfolio_timeseries.json` (plain JSON, 780,910 B, 3,225 rows, codes UST/ST/INT/LT/ULT, inception 2024-04-30, `data_as_of` 2026-10-19) and `json/positioning/positioning_data.json` (**gzip-compressed JSON**, 6,890 B; `portfolios.<code>.allocation` = percent by asset class, `current_holdings.<code>.holdings` weights sum 1.0, `data_as_of` 2026-10-19). The resident has no grant on either (trace Q5).
- **The comparison and multi maps cannot carry FWD-10 as they stand.** They were made from samples with a FIXED number of comparables: the comparison map has one comparison slot, the multi map has TWO (`key_index` 1 and 2 only), and each element label bakes in the sample's comparable name ("Alpha Opal Ultra Long-Term", "Beta iShares Russell 2000 ETF"). A filer may pick up to FIVE comparables (`submission.py:67-72`), and FWD-10's own example is three (two Opal models and one ETF). Re-pointing the map's elements would therefore serve at most two comparables, under the wrong names.
- **Run `produce` already drops every vendor-call and builder-only element** from the report document and counts them in one NOT_SHOWN line (AR-y-408), and appends its own elements after the last page (the three classified elements, the price table). The resident already carries `report_variant` (overview / comparison / multicomp) and refuses a variant with no map binding (`OPAL_MAP_BINDINGS`, `resident_installed.py:74`).

## Design (ruled here, inside this decomposition)

FWD-10 is built as ONE Opal-authored **comparison section**, appended after the last page exactly as the price table is, for every report that has comparables: five elements `opal.compare.window|chart|returns|risk|allocation`, N-comparable-capable (1 to 5), each comparable named from the catalogue entry the filer picked. The YCharts-structured pages of the comparison and multi maps stay as they are (their vendor-call elements are dropped and counted); FWD-11 (parity) is where they are re-pointed. The two maps are already packaged and bound (AR-g-85: `build_resident_package.py` carries `comparison_map.json` and `multi_map.json`; `OPAL_MAP_BINDINGS` has `opal_map_comparison` and `opal_map_multicomp`), and the whole `ycharts/research` directory is a package member, so the new modules ride the next resident release with no manifest edit.

- **Common window (stated on the page).** START = the latest first observation among the portfolio and every comparable that has a series (a model's first observation is no earlier than its inception, 2024-04-30); END = the earliest last observation among them. A comparable with no series is left out of the window and reads `not available for <name>: <reason>` (FWD-12). All lines are rebased to 100 at START.
- **Periodic total returns** (1m, 3m, YTD, 1y, 3y, 5y, 10y) are computed on the rebased common-window path; a period longer than the window reads `n/a` for every row.
- **Risk figures** (standard deviation, Sharpe, Sortino, max drawdown, alpha, beta) are monthly-return statistics over ONE period for all rows: N whole years = min(5, floor(window years)); N < 1 -> every risk figure reads `not available: the common window is shorter than 1 year`. Reference: benchmark SPY (alpha, beta) and risk-free BIL (alpha, Sharpe, Sortino), the same series and wording as the Overview.
- **Asset allocation, side by side.** Portfolio: the existing `ALLOCATION_ASSET_CLASS` weights. Opal model: `portfolios.<code>.allocation` of the positioning surface, **dated on the page** with that file's `data_as_of`. ETF: 100 percent in its classified asset class (the classifier row), stated in words.
- **Prices.** An ETF comparable is priced through the existing chain (`price_source.resolve_prices`: estate, yfinance, ycharts) over the same window; a model comparable reads `model_source`. No new vendor call. R8: no vendor name on the page.
- **Which comparables.** From the accepted request's frozen configuration (`comparison_keys` resolved through `comparison_catalog`, the same guarded read the vendor job uses: `frozen_worker.py:95`), never from the browser. A catalogue key maps to a model code ONLY through the committed `model_code_map.json` (no display-name matching).

## The frozen contracts (every cell builds to these; they are inlined in each order)

**K1 `ycharts/research/model_source.py`** (pure; the bytes are injected):
`BUCKET="opal-data-portal-v2"`, `SERIES_KEY="json/benchmarks/model_portfolio_timeseries.json"`, `POSITIONING_KEY="json/positioning/positioning_data.json"`, `CODES=("UST","ST","INT","LT","ULT")`, `class ModelSourceRefused(ValueError)`;
`code_for_key(catalogue_key) -> code | None`; `read_series(get_bytes) -> {"as_of","inception","series":{code:[[epoch_ms, level],...]}}` (level 100.0 on a code's first date, every later date multiplies by 1 + model_return, ms = UTC midnight); `read_allocation(get_bytes) -> {"as_of","allocation":{code:{"Cash","Fixed Income","Equity","Hedge","Structured","Commodities","Alternatives": percent}}}`. `get_bytes(key) -> bytes` (gzip detected by magic bytes). A missing key, a non-JSON body or a changed shape raises `ModelSourceRefused`.
**K2 `ycharts/research/comparables.py`** (pure): `build_compare(portfolio, comparables, benchmark, risk_free) -> record`; `build_allocation(portfolio_classes, rows) -> table`. `portfolio = {"name","series":[[ms,level]...]}`; each comparable `{"key","name","kind":"model"|"ticker","series":[[ms,level]...]|None,"reason":str|None}`; benchmark / risk_free `[[ms,level]...]|None`. Record: `{"window":{"start","end","years","rule"},"rows":[{"name","key","kind","status":"VALUE"|"NOT_AVAILABLE","reason","path":[[ms,level]...],"returns":{"1m","3m","ytd","1y","3y","5y","10y"},"risk":{"years","std_dev","sharpe","sortino","max_drawdown","alpha","beta"}}]}`, row 0 the portfolio. Allocation table: `{"classes":[...],"rows":[{"name","weights":{class:percent},"as_of":str|None,"basis":str}]}`.
**K3 layout** (`layout_overview.py`): computed methods `COMPARE_WINDOW`, `COMPARE_CHART`, `COMPARE_RETURNS`, `COMPARE_RISK`, `COMPARE_ALLOCATION`; `compute_all(..., compare=None)` and `compute_element(..., compare=None)` take `{"record": K2 record, "allocation": K2 table}`; with pricing off each reads NOT_AVAILABLE / NOT_IN_THIS_VERSION; the HTML names every row and prints `not available for <name>: <reason>` for a NOT_AVAILABLE row.
**K4 stores** (`opal_producer.produce`): `stores["comparables"]` = the ordered list of catalogue entries (`key`, `label`, `ticker` or None); `stores["model_bytes"]` = `callable(key) -> bytes`. Compare elements are appended only when `comparables` is non-empty AND pricing is on.

## Cells (this cut)

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-171` | K1 `model_source.py`, the committed `model_code_map.json`, tests | those three files | WORLD (resident package member) |
| `AR-g-172` | the Terraform read grant: GetObject on the two keys, resident role, plan only | `ycharts/iam.tf`, the changelog, the worker folder | WORLD |
| `AR-g-173` | K2 `comparables.py` with its tests | those two files | WORLD |
| `AR-g-174` | K3 the five computed methods, their HTML, `compare=` plumbing, tests | `layout_overview.py`, one test file | WORLD |
| `AR-g-175` | K4 the producer stage, the resident's comparables and model-bytes ports, tests | `opal_producer.py`, `resident_worker.py`, `resident_installed.py`, tests | WORLD |

## Edges and chains

Real data dependencies: 173 consumes the K1 series shape; 174 consumes the K2 record; 175 consumes K1, K2 and K3. 172 is independent of all. Two chains: **chain A** = AR-g-171 -> AR-g-173 -> AR-g-174 -> AR-g-175 (one worker queue, in that order; the contracts above are frozen so each order tests against fixtures); **chain B** = AR-g-172 (its own worker). `fanout: 2 of 2 chains, cap 8`.

## After the drain (not cells; the issuer's steps)

The never-widen pair for the grant (COO + CTO halves), the Terraform apply (CloudOps `safe-apply`), the FWD-10 resident release (the next `r34*` under its own pair), then the one real run: a Multi-Comp filed on the live product (two Opal models and one ETF) read page by page against the independent arithmetic. A real-data control on the two source objects is run at the drain (the checker's fixtures are synthetic).

## Four-postulate record

(i) Domain: the FIVE elements FWD-10's DONE WHEN names (window, chart, returns, risk, allocation) over up to five comparables; the denominator of comparables is the filer's list (1 to 5), printed on the page; the maps' vendor-call counts (Comparison 351, Multi 144) are NOT this round's domain (FWD-11). (ii) One grain per element: a row per portfolio or comparable. (iii) One intent: a reader answers "did this portfolio beat each model I picked, and with how much risk". (iv) What this cut does NOT move: the Overview, the price pages, the maps' vendor-call elements, the Ticket Center, the resident's Overview binding.

fanout: 2 of 2 chains, cap 8, reason: chain A is a data-dependency chain of four cells on frozen contracts; chain B is the independent infrastructure grant.

## Addendum 2026-10-20 (issuer, after the chain A drain at 51e86c27cd0): the release cell and one stale test

These two orders are one second issuance of round 60 and carry their own `<workstream>~GREL</workstream>` (the TO gate keys one issuance to round x workstream). The decomposition's "after the drain" step, the FWD-10 resident release, is cut as a cell so a worker builds and proves it; the issuer rules inside its own decomposition. Y2 ruled (msg 11518) that this seat builds the next resident release (r34o) and that it carries 2.0.0_SA_COO~Y2's audit wiring (AR-y-467, AR-y-469) as well. Measured at pin `3f1961ceab12c934b2510e2047589351ba3539e6` by a rehearsal build outside the repository: against the running r34n the release moves 11 members and adds 6 (323 members), import smoke 86 of 86. Two of the movers are not this round's work and ride the pin: `ycharts/research/overview_map.json` (the round-57 price pages' map) with the layout and producer that read it, and `lib/trading_calendar.py` (an additive function by another seat). They are named in the never-widen packet, not decided here.

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-176` | the r34o tarball, package sums and four host scripts from the pin, a build record and a proof (BUILD ONLY, stage folder outside the repository) | the worker folder `r61/` | LOCAL |
| `AR-g-177` | the stale NOT_IN_THIS_VERSION assertion of `test_opal_thread_ready_end_to_end` (AR-y-408 removed those sections) | that one test file | WORLD (the gate's floor for an infrastructure path, though only a test file moves) |

Chains: AR-g-176 and AR-g-177 are independent of each other and of the earlier cells (all merged). Checker for 176: `checks/ar_release_checks.py` (record, tree, scripts), calibrated on the rehearsal with mutants. Then the issuer's steps: the never-widen pair for r34o (COO and CTO halves), the CloudOps apply, and the one real run (`deliverables/2.0.0_SA_COO~G2/FWD10_ONE_REAL_RUN_PLAN_20261020.md`).

fanout: 2 of 2 chains, cap 8, reason: the release build and the stale-test fix are independent single-cell chains.

## Addendum 2 2026-10-20 (issuer): cell AR-g-178, the r34o rebuild with the audit registry file

Read from the shipped AR-g-176 tree: `analysis_audit.audit_address` raised AddressRefused, because the packaged `infra/logic/registry/reporting_policies.json` (r34n's) lacks the ANALYSIS_AUDIT family, so the audit wiring of 2.0.0_SA_COO~Y2 would have been dormant (a failed audit put is non-fatal, the attach stands). With the pinned file the address resolves to `s3://opal-data-irpt/irpt/<firm>/platinum/analysis_audit/`. The CTO agreed (msg 11544) and re-signs on the new packet blob. Measured by a rehearsal at pin `480ceeae884ad29b0dc40c29003c8f519e71f9e6` (tarball sha256 df070b09230f...): 12 members change, 6 are added, 323 members, smoke 86 of 86.

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-178` | the r34o v2 tarball, sums and four host scripts at the new pin into stage `C:/dev/irpt-release-r34o-g3` (BUILD ONLY), a record and a proof; the AR-g-176 stage `r34o-g2` is superseded and left in place | the worker folder `r62/` | LOCAL |

AR-g-178 carries `<workstream>~GREL2</workstream>` (a third issuance of round 60; the gate keys one issuance to round x workstream).

fanout: 1 of 1 chains, cap 8, reason: one build cell.

## Addendum 3 2026-10-20 (issuer): cell AR-g-179, the filing instrument for FWD-10's live read

r34o is live (IB2 ledger irpt-resident-r34o-20261020 CLOSED, V2S OK). The CTO (msg 11622) asked for one synthetic Multi-Comp filing after Y2's Overview. Two measured gaps in the filing instrument of runs 7b to 7e: it never ticks a comparable (it only counts the form's five Opal-model checkboxes), and its holdings use `SYNTH-*` tickers that no price tier knows, so a comparison built from them could only read "not available". Also measured: the live comparison catalogue holds only the five Opal models (no ETF entry; the form takes an ETF through the Other ETFs chip input), so the live run is a Multi-Comp of Opal models; the ETF comparable stays proved offline by AR-g-175. The run plan (`FWD10_ONE_REAL_RUN_PLAN_20261020.md`) is amended accordingly in the run order.

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-179` | a copy of the instrument with `--comparables`, the closed request line and a real-ticker holdings CSV, proved offline against a portal build at the PROD tip | the worker folder | LOCAL |

AR-g-179 carries `<workstream>~GREL3</workstream>`.

fanout: 1 of 1 chains, cap 8, reason: one instrument cell.

## Addendum 4 2026-10-21 (issuer): cell AR-g-180, the r34p build (r34o minus the registry change)

Run 7e (Y2's Overview filing) stopped at P4 on r34o with RetentionRefused where run 7d passed on r34n. Measured lead (this seat, msg 11637): r34o's one non-code change, `infra/logic/registry/reporting_policies.json`, moved the policy_sha256 of `irpt-anlreq-x10-v1` (8edbe84b05765c36 to cfed04bb8c2f1982) and `irpt-dashbd-x10-v1`; retention.py:147 refuses any row whose stored hash differs from its revision's current hash. CTO ruling (A), msg 11639: r34p = r34o minus that file; a revision that has rows is never edited; ANALYSIS_AUDIT returns later as a NEW revision. Measured by a rehearsal at pin `919bb891fa72dd706493f094c9b4412503fcf42a`: against r34o the release moves 3 members (SHA256SUMS, the registry file, the bindings provenance) and adds none; the checker also requires every policy hash to equal r34n's.

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-180` | the r34p tarball, sums and four host scripts into stage `C:/dev/irpt-release-r34p-g2` (BUILD ONLY), a record and a proof | the worker folder `r63/` | LOCAL |

AR-g-180 carries `<workstream>~GREL4</workstream>`.

fanout: 1 of 1 chains, cap 8, reason: one build cell.

## Addendum 5 2026-10-21 (issuer): cell AR-g-181, the r34q build (r34p plus the S245 admission fix, the tickets_table binding and the audit revision)

Run 7H (the Multi-Comp filing on r34p) was refused at the resident's replay of the frozen composition (row S245, CLOSED_COMPOSITION_REQUIRED): the packaged `ycharts/generate/submission.py` lacks `commentary_requested`. Measured by `checks/ar_admission_replay.py` on the run's retained synthetic composition: r34o and r34p tarballs fail at step 3, the same tarball with trunk's `submission.py` passes all five steps. r34q also ships 2.0.0_SA_COO~Y2's tickets_table binding (AR-y-483/484) and the registry file with the NEW revision `irpt-anlreq-audit-x10-v1` (ACTIVE since msg 11816). Measured by a rehearsal at pin `21cb4e857df85da3e0d3e14c83cb4c78c9a94b83`: against r34p the release moves 7 members and adds none: 323 members, tarball sha256 `f757171891f3924458123168abe2ccbba87d4b5bc12821cfa0f59b0f38b9266b`. The one policy hash that moved against r34n is `irpt-dashbd-x10-v1` (PENDING_ENFORCEMENT in both trees, 0 retention rows possible); the checker tolerates that revision alone.

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-181` | the r34q tarball, sums and four host scripts into stage `C:/dev/irpt-release-r34q-g2` (BUILD ONLY), a record and a proof | the worker folder `r64/` | LOCAL |

AR-g-181 carries `<workstream>~GREL5</workstream>`.

fanout: 1 of 1 chains, cap 8, reason: one build cell.

## Addendum 6 2026-10-21 (issuer): cells AR-g-182 and AR-g-183, the S249 fix and the retained-line lead token

Run 7I (the Multi-Comp filing on r34q) passed admission (the S245 fix held) and stopped at the next hop: `retained_for_retry class=RecipeRefused code=-` three times (row S249, IB2 msg 11887; CTO msg 11890). Measured by replaying 7I's retained synthetic composition (`checks/fixtures/composition_7i_synthetic.json`) through the r34q modules: `FrozenCompositionWorker.prepare` -> `prepare_normalized_upload` raised `RecipeRefused: holdings row has no provider receipt` (the run's four ETF holdings are YFINANCE_HISTORY checks with no vendor receipt). The Opal comparison path never uploads to the vendor. A second defect sits behind it: `_opal_comparables` reads `key`, `label`, `ticker` off catalogue entries that carry `name`, `security_type`, `source_id`, `vendor_id` (no key; the key is the catalogue's dict key), so the producer would have received key None for every model. My AR-g-175 tests faked `frozen` with the wrong shape.

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-182` | `prepare(upload=False)` plus `comparison_keys`; `_opal_comparables` on the real catalogue shape; tests | `frozen_worker.py`, `resident_worker.py`, `test_frozen_worker.py`, `test_compare_ports.py` | WORLD (infrastructure path floor) |
| `AR-g-183` | `retained_reason` carries `lead=<token>` for our own Refused/Attention classes (CTO item 2); tests | `resident_main.py`, `test_resident_main.py` | WORLD (infrastructure path floor) |

Both carry `<workstream>~GREL6</workstream>`; they share no file and no edge (two chains). Checkers `checks/ar_prepare_checks.py` (arms frozen, worker, tests) and `checks/ar_reason_checks.py` (arms reason, tests) were calibrated against reference fixes in a scratch tree and eleven mutants. Then, after Y2's ticket-read chain (live) and under the CTO's pair, the release r34r (AR-g-184) carries both fixes plus Y2's `ticket_audit_source.py` projection (trunk 11fb915f82d).

fanout: 2 of 2 chains, cap 8, reason: two independent cells with disjoint write sets.

## Addendum 7 2026-10-21 (issuer): cell AR-g-184, the r34r build (r34q plus the S249 fix, the retained-line lead token and the audit source projection)

AR-g-182 (merged 6422a8dc359) and AR-g-183 (merged c02fdd2fd64) are verified on the full tree (frozen, worker, tests 27; reason, tests 51; ruff clean), and 2.0.0_SA_COO~Y2's AR-y-487 (`ticket_audit_source.py`, trunk 11fb915f82d) is under the pin. Measured by a rehearsal at pin `32bb8d5a673d3e0dd3c6efc933b7f0db5206533a`: against r34q the release moves 6 members (SHA256SUMS, the bindings provenance, `frozen_worker.py`, `resident_main.py`, `resident_worker.py`, `ticket_audit_source.py`) and adds none: 323 members, tarball sha256 `77ec08f5a591de5584abb71787eb74c86bcbd3167416f2b411befc750140b828`, smoke 86 of 86, gate dry runs 0, 31, 0, 33. The registry file and the `tickets_table` binding do not move. The checker `checks/ar_release_r_checks.py` (calibrated: record OK, tree OK, scripts OK on the rehearsal; tree FAIL on the r34q tarball) also runs the S249 and lead-token checks on the tarball's own extracted modules.

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-184` | the r34r tarball, sums and four host scripts into stage `C:/dev/irpt-release-r34r-g2` (BUILD ONLY), a record and a proof | the worker folder `r65/` | LOCAL |

AR-g-184 carries `<workstream>~GREL7</workstream>`.

fanout: 1 of 1 chains, cap 8, reason: one build cell.

## Addendum 8 2026-10-21 (issuer): cells AR-g-185 and AR-g-186, the fixes of the 7J read

Run 7J (Multi-Comp on r34r, PASS: packager ATTACHED, audit AUDIT_WRITTEN, 60 pages) was read page by page (`deliverables/2.0.0_SA_COO~G2/FWD10_READ_RUN7J_20261021.md`). The Opal model rows reproduce exactly; the PORTFOLIO row does not (YTD 10.66 page against 8.83; 1Y 13.37 against 11.12; drawdown -15.94 against -13.60). Cause measured by exact reproduction (page to three decimals): the filed amounts are applied at the start of the 10-year price window (`PRICE_HISTORY_YEARS`, 2016-10-20) and the path is cut and rebased at the common window start (2024-04-30), by which date the filed SPY 44 percent has drifted to 60.1 percent. The 7f Overview sample reproduces exactly under the same formula (its caption states the semantics), so FWD-9's figures are not defective on this test. Also found: a false sentence "Not available: no row of this section has a value." under three tables of a report whose rows all carry values, the 3Y, 5Y and 10Y n/a cells unexplained in words, a stranded heading, and a raw `{portfolio_name}` in Overview labels. My AR-g-175 tests used price histories that began at the models' first observation, so the drift could not appear (the third premise gap of the fake-shape kind this round).

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-185` | `buy_and_hold_from`; `_price_stage` returns its series and amounts; `_compare_stage` re-applies the amounts at the common window start; tests | `portfolio_series.py`, `opal_producer.py`, `test_portfolio_series.py`, `test_compare_producer.py` | WORLD (infrastructure path floor) |
| `AR-g-186` | no false gap sentence; the n/a periods explained in words; `.cmp` keep-together; no raw placeholder; tests | `layout_overview.py`, `test_layout_overview.py`, `test_compare_elements.py` | WORLD (infrastructure path floor) |

Both carry `<workstream>~GREL8</workstream>` (one issuance); they share no file and no edge. Checkers `checks/ar_window_checks.py` (arms portfolio, tests) and `checks/ar_gapnote_checks.py` (arms gaps, placeholder, tests) were calibrated against reference fixes in scratch worktrees and seven mutants. Then the release r34s (AR-g-188) carries both under the CTO's pair, and run 7K reads the result.

fanout: 2 of 2 chains, cap 8, reason: two independent cells with disjoint write sets.

## Addendum 9 2026-10-21 (issuer): cell AR-g-187, the re-pin after AR-g-186's one CSS rule

AR-g-185 (merged 44240238b9f) and AR-g-186 (merged 8faec6ba970) are verified on the full tree (window portfolio OK and tests 76; gapnote gaps OK, placeholder OK, tests 85; ruff clean). The issuer's drain run of the whole `ycharts/research/tests` directory (708 tests) found two failures outside the workers' paths: `test_layout_commentary.py::test_a_no_commentary_is_byte_identical_to_today` and `test_commentary_standalone_pdf.py::test_b_build_is_byte_identical_to_base_with_and_without_the_commentary_keyword`, which pin the sha256 of the fixture Overview's HTML. Measured: the one added `.cmp` page-style line is the ONLY difference (removing it restores both old pinned hashes exactly, 475b060b6e2b and 790d953d59fb); the new values are 3d6dfd48d3a4... (no commentary) and a9d38267d285... (with commentary). Worker 359's AR186-g-AC3 read FAIL in its sparse worktree (a shared module, `v2_portal/_shared/etf_classifications_dynamodb.py`, outside the cone: row W359-S1, the issuer's sparse-cone gap); on the full tree it reads `AR-GAPNOTE-tests-OK passed=85` (`deliverables/2.0.0_SA_COO~G2/AR186_AC3_ISSUER_REGRADE_20261021.md`).

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-187` | the three pinned hashes of two tests move to the measured values | `test_layout_commentary.py`, `test_commentary_standalone_pdf.py` | WORLD (infrastructure path floor) |

AR-g-187 carries `<workstream>~GREL9</workstream>`. Then the release r34s (AR-g-188) carries AR-g-185, AR-g-186 and AR-g-187.

fanout: 1 of 1 chains, cap 8, reason: one test-pin cell.

## Addendum 10 2026-10-21 (issuer): cell AR-g-188, the r34s build (r34r plus the Multi-Comp portfolio path and the report presentation fixes)

AR-g-185 (44240238b9f), AR-g-186 (8faec6ba970) and AR-g-187 (5fd1e793f2f) are merged and verified on the full tree; the drain run of `ycharts/research/tests`, `test_compare_ports.py`, `test_resident_main.py` and `test_frozen_worker.py` reads 741 passed. Measured by a rehearsal at pin `5fd1e793f2fe7e3eabdac88d178c411c3d51ab0b`: against r34r the release moves 5 members (SHA256SUMS, the bindings provenance.package_pin only, `layout_overview.py`, `opal_producer.py`, `portfolio_series.py`) and adds none: 323 members, tarball sha256 `fa950681774268d2108eb7ca141ec150213d0d6e482dad498d13870a90d87b14`. The registry file, the `tickets_table` binding and the files-from list (50 lines) do not move. The checker `checks/ar_release_s_checks.py` (calibrated: record OK, tree OK, scripts OK on the rehearsal; tree FAIL on the r34r tarball) also checks that the shipped source carries `buy_and_hold_from`, its caller and the `.cmp` rule.

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-188` | the r34s tarball, sums and four host scripts into stage `C:/dev/irpt-release-r34s-g2` (BUILD ONLY), a record and a proof | the worker folder `r66/` | LOCAL |

AR-g-188 carries `<workstream>~GREL10</workstream>` (worker slot 365: branch 364 is a drain helper branch).

fanout: 1 of 1 chains, cap 8, reason: one build cell.

## Addendum 11 2026-10-21 (issuer): cells AR-g-189 and AR-g-190, the CTO's FWD-10 enrichment (msg 11977, round analysis @e1ed2d1914)

The round analysis grades FWD-10 realized as written (one ETF) and names two enrichments: (1) measure read-only on r34s whether an ETF typed in the form's "Other ETFs" field reaches `_compare_stage` as a priced comparable; no -> one wiring cell, failing-first, in the next release, then run 7M; (2) page 60 prints each model's own as-of date, in the same release. Measured (`deliverables/2.0.0_SA_COO~G2/ETF_TYPED_PATH_MEASUREMENT_20261021.md`, commit b452a85c42, instrument `checks/etf_typed_measure.py`): the door admits a classified ETF but drops the entry's `key`, so `_opal_comparables` yields ticker None and `_compare_stage` takes the empty "other" branch. The AR-g-182 tests (and `ar_prepare_checks.py`'s worker arm, a fourth premise-gap of the fake-shape kind) handed in an ETF entry carrying a `key` the door never retains; the new checker `checks/ar_enrich_checks.py` runs the REAL door.

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-189` | `_opal_comparables` takes an ETF's ticker from the catalogue key; tests on the door's real entry shape | `resident_worker.py`, `reports/tests/test_compare_ports.py` | WORLD (infrastructure path floor) |
| `AR-g-190` | `read_allocation` returns each model's own `data_as_of` (`as_of_by_code`); `_compare_stage` uses it; tests | `model_source.py`, `opal_producer.py`, `test_model_source.py`, `test_compare_producer.py` | WORLD (infrastructure path floor) |

Both carry `<workstream>~GREL11</workstream>` (one issuance); they share no file and no edge. `checks/ar_enrich_checks.py` (arms etfkey, asof, tests189, tests190) was dry-run at the base (all four FAIL) and calibrated against the reference fixes in a sparse scratch worktree (etfkey OK, asof OK) and six mutants (ticker never, ticker on every entry, file date always, no fallback to the file date, producer ignoring the per-code date; one equivalent mutant, ticker from `vendor_id`, reads OK by design). `opal_producer.py` is also in Y2's `AR-y-494` write set (a different function, `_swap_stage`); the merges are the issuer's drain. Then the release r34t (AR-g-191) carries both, and run 7M (two Opal models plus one typed ETF) reads the result.

fanout: 2 of 2 chains, cap 8, reason: two independent cells with disjoint write sets.

## Addendum 12 2026-10-21 (issuer): cells AR-g-191 and AR-g-192, the CTO's rulings on run 7L (msg 11980)

AR-g-189 (merged 7f1b3f4424c) and AR-g-190 (merged f3db0c52634) are verified on the full tree: the four checker arms read OK (`ar_enrich_checks.py` etfkey, asof, tests189 7, tests190 75) and the drain run of `ycharts/research/tests`, `test_resident_main.py`, `test_frozen_worker.py` and `test_compare_ports.py` reads 791 passed. The CTO read run 7L (`OVERVIEW_READ_RUN7L_20261021.md`) and ruled (msg 11980): (1) a kept row left out of the figures is named on the page, ticker and reason only, in the Overview and the Multi-Comp; (2) page 21's six "The kept answer is not a readable table." lines are a FWD-9 defect, found and fixed failing-first; both go in r34t. Measured causes: (1) the swap pass already records each left-out holding in `run_doc["swaps"]` (`status`, `why`, no amount); the layout prints nothing about it; (2) the Overview map's six Risk Info elements (p7.e02, e03, e05, e06, e07, e08) are tables that name both `columns` and a `statistic`, and `_compute_own_series` returns the first column's scalar for them (the column path is taken only without a statistic); a scalar is not a table. Reproduced offline with the real map (5 of the 6 print the sentence on a ten-year history; the sixth, Monthly VaR, differs in the fixture).

| cell | what is produced | write set | risk |
|---|---|---|---|
| `AR-g-191` | `_excluded_line` and its one line on the Top 10 Holdings page; a new test file | `layout_overview.py`, `test_layout_excluded_line.py` | WORLD (infrastructure path floor) |
| `AR-g-192` | table elements with columns take the column path; the one test that read a scalar is updated; two new tests | `layout_overview.py`, `test_layout_overview.py`, `test_layout_own_series_columns.py` | WORLD (infrastructure path floor) |

Both carry `<workstream>~GREL12</workstream>` and one worker (slot 382, queue 191 then 192): they share `layout_overview.py` (the dispatch write-set rule). `checks/ar_enrich2_checks.py` (arms excl, p21, tests191, tests192) was dry-run at the base (all FAIL) and calibrated against the reference fixes in a sparse scratch worktree (excl OK, p21 OK) and five mutants, each of which fails. The scratch run of the whole research test directory with the reference fixes showed one test broken by AR-g-192's rule (`test_wired_statistics_compute_from_the_kept_benchmark_and_the_held_yield`, now named in the cell) and none by AR-g-191. Then the release r34t (AR-g-193) carries AR-g-189 to AR-g-192 and Y2's swap leg (AR-y-494, drained 3dac9960e2b); run 7M reads the result.

fanout: 1 of 1 chains, cap 8, reason: two cells sharing layout_overview.py are one chain for one worker.
