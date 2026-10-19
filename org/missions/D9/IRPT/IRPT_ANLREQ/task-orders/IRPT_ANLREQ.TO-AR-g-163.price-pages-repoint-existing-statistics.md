# TO-AR-g-163 -- the Opal-built report's price pages, part 1: eight map elements re-pointed to the statistics the layout already has (row 3c22; CTO msgs 10729, 10734, 10743)

<to_id>IRPT_ANLREQ.TO-AR-g-163</to_id>
<project>IRPT_ANLREQ</project>
<issued_to>0.9.0_WK_IRPT_ANLREQ~301</issued_to>
<issued_by>2.0.0_SA_COO~G2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>57</round>
<workstream>~G</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** ~G (ENGINE) | **Decomp cell:** `AR-g-163` (`decompositions/IRPT_ANLREQ_DECOMP_R57_G.md`) |
**outcome_ref:** FWD-7 | **depends_on:** none. Nothing is deployed by this cell; it reaches the served report only through a later resident release under its own never-widen pair.

---

## WORKER FACE

You are `0.9.0_WK_IRPT_ANLREQ~301`.
- **Worktree:** `C:/dev/wk-irpt-anlreq-301` (branch `wk-IRPT_ANLREQ-301`), provisioned by the issuer. Work only there. First confirm `org/` and `.tools/` exist in it.
- Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_ANLREQ~301 <0.9.0_WK_IRPT_ANLREQ~301@opal.agent>" -F <msgfile> -- <paths>`. Write the message file with the Write tool. Do not pre-`git add`. The worktree may show ` M portal` and a modified `.parquet` fixture: never commit either.
- A row id has the form `IRPT_ANLREQ-D2-W301-S<k>` (take the next free `<k>`; check the channel file for `W301` first); `surfaced_at` of any row = `date -u +%FT%TZ` at filing.
- Python 3.9 syntax, ruff clean, ASCII only. Do not touch anything outside the `<paths>` block. Run Python with plain `python` (the producer's tests need `pypdf`, which `python -I` cannot see).

### THE CELL (`AR-g-163`, inlined)

**AMENDMENT 1 (issuer, 2026-10-19, on worker ~302's row IRPT_ANLREQ-D2-W302-S1; gate limb: none graded, an in-decomposition amendment of a grant):** `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py` line 754 pins the number of `OWN_SERIES` elements of the real map: `assert len(res) == len(series) == 9`. Your cell adds 8, so it must read `17` on YOUR branch (the three round-57 cells that add `OWN_SERIES` elements each move it by their own delta, 163 by 8, 164 by 5, 165 by 4; the issuer reconciles the line to 26 at the merge). That file is now in your `<paths>`. Change ONLY that number (and, if the line wraps, nothing else); do not weaken the assertion, do not touch any other line of the file. Then re-run AC3.

**AMENDMENT 2 (issuer, 2026-10-19, on worker ~301's BLOCKING row IRPT_ANLREQ-D2-W301-S1):** the same file has a SECOND stale pin from your cell: moving Beta (5Y) and Alpha (5Y) off `OPAL_HELD` takes that count from 158 to 156, so lines 623 (`assert len(held) == 158 and ...`) and 625 (`assert len(got) == 158`) must read `156`. Change those two numbers and the line-754 number (9 to 17) and nothing else in the file; do not weaken any assertion. (`ycharts/research/tests/test_runner.py` line 943 also holds a `158`; it is not in your regress set, the issuer fixes it at the merge. Do not touch it.) Then re-run AC3.

File: `org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json` (a pretty-printed JSON file, one `"elements": [...]` list). Eight elements read NOT_IN_THIS_VERSION with pricing on because their `source` names a vendor call or a held-data group. The layout (`ycharts/research/layout_overview.py`) ALREADY computes the statistics they need from the buy-and-hold level series (`_STATS`: total_return incl. `ytd`; std_dev; beta and alpha over 1y/3y/5y/10y/15y). Change ONLY each element's `source` object (and, if you wish, its `note`); do not change its `id`, `page`, `kind`, `label` or `claim`, and do not touch `layout_overview.py`.

The shape to copy is the existing element `p7.e05` (one statistic) and `p2.e13` (a column list):

    "source": {"call": "portfolio_level_series", "columns": [...], "computed": "OWN_SERIES",
               "field": "$.chart_data[0][0].raw_data", "sleeve": null, "statistic": "<one statistic or null>"}

With a `statistic` set, `columns` is ignored; with `statistic: null` and a `columns` list, a table gets `{label: value}` (labels like `Total return 1Y`, `Std dev 5Y`) and a chart gets the list of values. Make exactly these changes:

| element | kind | source after |
|---|---|---|
| `p2.e14` Key Stats: YTD Total Returns | number | `statistic: "total_return_ytd"`, `columns: []` |
| `p2.e11` Key Stats: Beta (5Y) | number | `statistic: "beta_5y"`, `columns: []` |
| `p2.e15` Key Stats: Alpha (5Y) | number | `statistic: "alpha_5y"`, `columns: []` |
| `p7.e04` Risk Info: Standard Deviation | table | `statistic: null`, `columns: ["std_dev_1y","std_dev_3y","std_dev_5y","std_dev_10y"]` |
| `p7.e13` Risk/Reward: Standard Deviation | table | the same four `std_dev` columns |
| `p7.e12` Risk/Reward chart 2 of 2 | chart | the same four `std_dev` columns (the bars of the p7.e13 row) |
| `p7.e10` Risk/Reward: Return | table | `statistic: null`, `columns: ["total_return_1y","total_return_3y","total_return_5y","total_return_10y"]` |
| `p7.e11` Risk/Reward chart 1 of 2 | chart | the same four `total_return` columns (the bars of the p7.e10 row) |

Not built, on purpose: the vendor tables also carry All Time and 15Y; the price window is 10 years and `total_return_all` is not a statistic, so those columns are left out (the packet names them).

Then add ONE new test file `infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_pages_repoint.py` (pytest) that runs the shipped Opal producer over the REAL map and asserts, for the eight ids: with pricing on every one reads VALUE with method `OWN_SERIES`; the YTD element equals the `Total return YTD` cell of `p2.e13`; the p7.e10 row equals the 1Y/3Y/5Y/10Y cells of `p2.e13`; p7.e11 is the list of p7.e10's values in column order; p7.e04 equals p7.e13 and p7.e12 is the list of its values in column order; with pricing off every one reads NOT_AVAILABLE / NOT_IN_THIS_VERSION. Use the harness the sibling tests use (`import test_opal_producer as tp`, `import test_opal_producer_prices as tpp`, `tp.make_stores(map=<the real map>, pricing=True, as_of="2026-10-14", price_readers=<readers>)`, `tpp.op.produce(tp.REQ, tp.FIRM, stores)`). The sibling fixture serves only 27 months, too short for 3Y/5Y/10Y; serve your OWN deterministic 133 monthly points per ticker (2015-10-14 to 2026-10-14, one level per month on the 14th) for AAA, BBB, CCC and the benchmark proxy `SPY` and the risk-free proxy `BIL`, each reader returning only rows with `start <= date <= end`, and AAA/SPY/BIL on tier `estate`, BBB on `yfinance`, CCC on `ycharts`.

1. Edit the map; write the test; run your test and the three criteria. 2. Commit the map and the test (code first), then the proof and the status flip as separate commits. 3. **Report** the commit hashes and the three criterion outputs.

### ACCEPTANCE (worktree root, after your last commit)

<criterion id="AR163-g-AC1" cell_refs="AR-g-163"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 163 build</invocation><expect>^AR-PRICE-163-OK</expect></criterion>

<criterion id="AR163-g-AC2" cell_refs="AR-g-163"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 163 guard</invocation><expect>^AR-PRICE-163-OK</expect></criterion>

<criterion id="AR163-g-AC3" cell_refs="AR-g-163"><invocation>python org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/2.0.0_SA_COO~G2/checks/ar_price_checks.py 163 regress</invocation><expect>^AR-PRICE-163-REGRESS-OK</expect></criterion>

<expected_criteria>AR163-g-AC1,AR163-g-AC2,AR163-g-AC3</expected_criteria>

- AC1: the eight elements are VALUE with pricing on, method `OWN_SERIES`, with the cross-element agreements above (YTD equals the p2.e13 YTD cell; the p7.e10 row equals p2.e13's; p7.e11 and p7.e12 are the bars of their rows; p7.e04 equals p7.e13). At base it FAILs.
- AC2: with pricing off every element of the map reads exactly as at the base; with pricing on nothing outside the 17 round-57 elements moves and the nine base VALUE elements are byte-equal. At base it PASSes.
- AC3: runs six existing producer and layout test files on their own, then that the branch changed only your files, your folder, the order and the channel file. At base it PASSes.

## BOUNDS

- **Grant.** The `<paths>` block only. `layout_overview.py`, `opal_producer.py` and every other file are read only.
- **Refusal clause.** If a step cannot be done as written, or a commit is refused as another lane: stop, file a row with the refusal text, report what is committed and what is not, and do not weaken a check or force a commit.
- **Rows.** APPEND a `## <id>` heading plus one fenced json block at the END of the channel file below; gate: `python .tools/surprise-row-gate.py --check <path>`.

<paths>
org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_price_pages_repoint.py
org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~301/
org/missions/D9/IRPT/IRPT_ANLREQ/task-orders/IRPT_ANLREQ.TO-AR-g-163.price-pages-repoint-existing-statistics.md
org/missions/D9/IRPT/IRPT_ANLREQ/surprise-channel/investigations/INVESTIGATION_v1.md
infra/aws/lambda/investor-reporting/ycharts/research/tests/test_layout_overview.py
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_ANLREQ/decompositions/IRPT_ANLREQ_DECOMP_R57_G.md</decomp_doc> round 57, workstream ~G, cell `AR-g-163`.
<owned_cells>AR-g-163</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AR163-g-AC1, AR163-g-AC2, AR163-g-AC3. Instance at
`org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~301/IRPT_ANLREQ.TO-AR-g-163.price-pages-repoint-existing-statistics.proof_of_spec.json`.
- Set its `to_id` to exactly `IRPT_ANLREQ.TO-AR-g-163`, and its `decomp_ref` to the order's `<decomp_ref>` block (the proof gate requires it).
- Each acceptance entry's `invocation` is the criterion's text EXACTLY (put any `timeout` bound in the evidence line, not in the invocation).
- In `artifacts_produced`, name each file with the hash of the commit that holds it, never a placeholder: the map and the test first, then the proof and the status flip.
- In each acceptance entry, `output_evidence` BEGINS with the check's OK line.
- Validate with `python .tools/proof-of-spec-check.py <instance> AR163-g-AC1,AR163-g-AC2,AR163-g-AC3` BEFORE the flip to complete.
- Shape: `org/missions/D9/IRPT/IRPT_ANLREQ/deliverables/0.9.0_WK_IRPT_ANLREQ~282/IRPT_ANLREQ.TO-AR-g-161.pricing-as-of-calendar-frontier.proof_of_spec.json`.
</proof_of_spec>

**REPORT (final message):** as step 3.

---

## RECORD FACE

<preflight>
comp-blast: RUN (by reading) -- one map file and one new test; no deploy, no AWS call, no network. The map is a `--opal-map` member of the resident package, so the change reaches the served report only through a later resident release under its own never-widen pair: eight elements move from NOT_IN_THIS_VERSION to VALUE when the binding has pricing on (r34k does), which is a served-output change the release's pair must cover on both branches (pricing on and off).
comp-iam: DECLARED-NOT-APPLICABLE -- no AWS call and no policy change. comp-routes: DECLARED-NOT-APPLICABLE. comp-cache: DECLARED-NOT-APPLICABLE.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule or trigger.
comp-adversary: RUN -- `ar_price_checks.py` was dry-run at the base (build FAIL, guard PASS, regress PASS; `calibrate` OK: the checker's own YTD and max-drawdown arithmetic agrees with the shipped elements). Traps: the sibling fixture serves 27 months (3Y/5Y/10Y windows would read SERIES_TOO_SHORT), so the checker serves its own 133; `python -I` cannot import `pypdf` (a user-site package), so the criteria run plain `python`; All Time and 15Y are not statistics of the engine. NOT seen (blind): the rendered PDF of the pages (this reads run.json entries and sections, not pixels); a reference fix was NOT dry-run (the cell is a data edit; the base arms bound it).
</preflight>

- Cut on the CTO's rulings (msgs 10729, 10734, 10743) by the issuer inside its own decomposition. Risk WORLD: the floor of an infrastructure path (a resident package member). Base: AR163-g-AC1 FAILs, AR163-g-AC2 PASSes, AR163-g-AC3 PASSes.
