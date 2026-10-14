# TO IRPT_DASHBD.TO-DB-b-194 -- the model benchmark windows: the builder reads the dated daily model series as an input, compounds QTD, YTD, 12 months and since the household's first day cumulatively, fills the 32 benchmark members and the 12-month chart, and the contract states the new source; nothing else moves

<to_id>IRPT_DASHBD.TO-DB-b-194</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~159</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>103</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-102 ANALYSIS item 2 and ruling msg 7511 ("the builder may read model_portfolio_timeseries.json as an input ... Compute QTD, YTD, 12M and since the household's first day, all cumulative, by compounding that daily series, and drop the period object.") | **Rows:** IRPT_DASHBD-D2-W159-S<k> | **Decomp cell:** `DB-b-194` (decomposition section 105) | **outcome_ref:** FWD-21 | **depends_on:** none (the previous round's read: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~157/BENCHMARK_SOURCE_READ.json`).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-159` (branch `wk-IRPT_DASHBD-159`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~159/`.

**What exists.** The default performance report's filled sample is built by `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~154/build_sample.py` (read its header in full: the household rule, the window folds, the units, `firm_adapter`), run as `python -I build_sample.py --firm 49financial --out <private_out_dir> <repo_root>` or as its header states. The current filled sample (client data, read-only, sha256 `c8075558c155ebc5034127dc4abf03c8391b31d63fbdac0b32737b533535bd71`) is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~154/HOUSEHOLD_SAMPLE.json`. Its 32 benchmark members (the contract ids containing `benchmark`: four stems `benchmark_ultra_short_term`, `benchmark_short_term`, `benchmark_intermediate_term`, `benchmark_long_term` in each of the four windows `qtd`, `ytd`, `last_12_months`, `since_inception`, in both the `avs.*` account value summary and the `pvs.*` portfolio value summary) are ABSENT because the contract (`org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json`, version 0.3.0, sha256 `ca633614a32e85f4caa4ee07fdc08923d8398fd287adfc31c7f532efae89b574`) sources them ABSENT ("Opal holds no benchmark return series"), and so is the 12-month chart member `overview.chart.portfolio_performance_last_12_months`. The previous round's read found the source: Opal's model benchmark returns are produced by MDPF's `yang-model-portfolio-benchmarks` and served as JSON; a dated DAILY series is served at `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json` (the period object `model_portfolio_benchmarks.json` is NOT used). The CTO ruled the builder reads that dated series as an INPUT and compounds every window from it. The model returns are Opal's own product, not client data.

**The cell (`DB-b-194`).**
1. **Read the source.** Read `~157/BENCHMARK_SOURCE_READ.json` and the served dated series by ONE S3 GET (`aws s3 cp s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json <scratch>`; the bucket comes from the record, never from the registry's bucket field; if the comp-rail hook refuses, run what it says next or annotate `# rail-checked: <why>`). Read its shape (stems, dates, the value kind: daily return, or level, or cumulative index) WITHOUT writing any figure into the repo or a row. Map its four model series to the four stems with the served names (`Ultra-Short Term`, `Short Term`, `Intermediate Term`, `Long Term`). Write the normalised series to the private file `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~159/MODEL_SERIES_DAILY.json` as exactly `{"stems": {"benchmark_ultra_short_term": [["YYYY-MM-DD", daily_return_decimal], ...], "benchmark_short_term": [...], "benchmark_intermediate_term": [...], "benchmark_long_term": [...]}}` with ONE daily return per trading day as a decimal (0.0012 = 0.12 percent). If the source gives levels or an index, convert to daily returns and say so in `source.return_basis`; if it gives returns in percent, divide by 100. Each stem must hold more than 400 days.
2. **The contract states the source (the contract is YOURS to edit in this cell; no other file under `org/standards/`).** Bump `contract_version` to `0.4.0`; add the 0.3.0 bytes to `lineage` as `{"contract_version": "0.3.0", "sha256": "ca633614a32e85f4caa4ee07fdc08923d8398fd287adfc31c7f532efae89b574", ...}` the way the existing lineage entries are written; for each of the 32 benchmark members AND the member `overview.chart.portfolio_performance_last_12_months` replace `"source": "ABSENT"` (and drop its `reason`) with a source OBJECT in the shape other sourced members use, carrying `"input": "model_portfolio_timeseries"` (the input name must contain `timeseries`), the served object address, the stem's served name, and a `"fold"` that states in words the cumulative compounding and the window starts below. Every OTHER member stays byte-identical (the checker compares each to the 0.3.0 version in git history). Update the contract's `open_changes` text where it says the benchmark members are ABSENT. The contract's `document`, `sections` and every other key stay as they are.
3. **The builder.** Copy `~154/build_sample.py` into YOUR folder and change your copy; it keeps `--firm` and `firm_adapter`, and the benchmark input lives behind ONE function (a firm-neutral model input, not a firm adapter): `model_series()` that reads the private series file or the served object. Fill the 32 members as CUMULATIVE returns by compounding: window return = (product over the window's days of (1 + r)) - 1, as a percent number rounded to 1 dp (the report's percent unit: the value `1.5` means 1.5 percent). Window days are the series' dates `d` with `lo <= d <= R`, where R is the household's `as_of`, and `lo` is: `qtd` the first calendar day of R's quarter; `ytd` January 1 of R's year; `last_12_months` one calendar year before R plus one day; `since_inception` the day AFTER the account's first data date (account rows, `avs.*` by-row members, use each account's own `first_data_date` from the sample's household block) or after the household's first data date (`pvs.*` members). These starts are the checker's formulas: state the four household-level starts in the record's `window_starts` (the since_inception entry is the household's `first_data_date`) and make your account windows follow the same starts as the account return windows the builder already uses (say in a row if they differ). A member whose window cannot open on the series (the series starts after `lo`) or whose account is not spanned stays the absent form WITH the reason the builder gives; never zero. Per-account members keep the `{"by_row": {...}}` form with the account ids exactly as the builder already writes them.
4. **The 12-month chart.** Fill `overview.chart.portfolio_performance_last_12_months` as a list of `{name, points}` series (point = `{date, value}`), one per model benchmark named with the served name, drawing the cumulative return from `last_12_months`' start to R day by day (value = the cumulative percent at that day, rounded to 1 dp; 100 or more points per series; the last point equals the 12-month window figure). The household's own series stays absent (not in this cell); the chart carries the four benchmark lines only.
5. **Rebuild the SAME household** into the NEW private path `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~159/HOUSEHOLD_SAMPLE.json` (this exact path is checked; the earlier sample stays untouched). Every member other than the 32 benchmark members and the 12-month chart must equal the prior sample's value exactly (the checker compares them all); the `household` block is unchanged. S3 GET and LIST only. Print how many of the 32 benchmark members fill (`filled_of_32`) and which remain absent and why, in your report.
6. **Record** `BENCHMARK_FILL.json` in your folder with exactly: `prior_sample_sha256` (the prior sample's sha256 above); `sample_sha256` (of the new sample); `series_sha256` (of the private series file); `source` {`served_object` ("opal-data-portal-v2 json/benchmarks/model_portfolio_timeseries.json"), `data_as_of` (the series' as-of date, ISO; the claim every figure carries), `return_basis` (words: what the served series is and how you derived daily returns)}; `window_starts` {`qtd`, `ytd`, `last_12_months`, `since_inception`: ISO dates per the formulas}; `filled_of_32`; `benchmark_members` (each of the 32 ids -> "filled" or "absent"); `builder_sha256` (of your folder's `build_sample.py`); `firm_branches_outside_adapter` 0; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, ids, dates and words only: no benchmark figure and no client figure in the repo or a row.
7. Run `bash .tools/commit-gate.sh <file>` on your builder (a `.py` file), and validate the edited contract is valid JSON (`python -c "import json,sys; json.load(open(...))"`).

<criterion id="DB103-2-AC1" cell_refs="DB-b-194"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r103/p103_round103.py" . DB103-2-AC1</invocation><expect>DB103-2-AC1 PASS</expect></criterion>
`DB103-2-AC1` -- the contract is above 0.3.0 with the 0.3.0 bytes in its lineage, the 32 benchmark members and the 12-month chart are sourced from the model series, and no other member changed (compared with the 0.3.0 version in git history); the prior sample is untouched and the new one conforms to the filled-report shape with the same household and every other member unchanged; the private series file hashes as recorded with four stems of more than 400 days, and every filled benchmark figure equals the checker's own compounding of that file over the recorded window starts (the formulas above) within 0.06; the 12-month chart carries four series of 100 or more points; `filled_of_32` equals the sample's; the source claim carries its as-of date; no write, push or deploy; no run of 8 or more digits in the record (a sha256 value, and a value under a key named path, commit, file or key, is exempt: the checker's rule). Base: FAIL (no record).

<expected_criteria>DB103-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `~154/build_sample.py`, the prior sample and every other contract.
- **No write of any kind to AWS** (no S3 put/copy/delete, no DynamoDB write, no Lambda, Terraform or IAM act), **no deploy, no push, no vendor call (no YCharts call), no secret read.** Reads only: repo files; S3 LIST and GET with the box's existing identity (the one served object and the gold tables the builder already reads). Landing the series in gold is a LATER round under a pair; this cell writes nothing to gold. A denial is recorded verbatim, not retried by another route.
- **Client data.** The samples live ONLY under `C:/dev/_irpt_private_evidence_20261009/`. The model series is Opal's own data but stays in the private folder too: no figure of either goes in the repo, a row, a message or your report.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the served series cannot give daily returns for a stem, or starts after a window's start, record it and leave those members absent in words; do not interpolate. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W159-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~159/
org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-194.model-benchmark-windows-compounded-from-the-dated-series.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 105 (round 103), cell `DB-b-194`.
<owned_cells>DB-b-194</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB103-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~159/IRPT_DASHBD.TO-DB-b-194.model-benchmark-windows-compounded-from-the-dated-series.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB103-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the shape of the served series and how you derived daily returns; `filled_of_32` and which of the 32 stay absent and why; the window starts used; the chart's series; the contract change (version, lineage, members); any difference between the account windows and the benchmark windows; row ids. Counts, names and words only: no figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a builder copy, a contract edit and a private sample; nothing is served, wired or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 LIST and GET with the box's existing identity; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB103-2-AC1 FAILS at base (no record) and is dry-run on 12 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>
