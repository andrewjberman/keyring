# TO IRPT_DASHBD.TO-DB-b-214 -- the INFLECTION SAMPLE (data half of the first Inflection render): one household built in memory from Inflection's own silver by the round-108 adapter, the household return from Orion's client-keyed performance with its source, the household ending value, account returns and lots in plain words, a sample that passes the whole-document rule, and the Orion guard state named

<to_id>IRPT_DASHBD.TO-DB-b-214</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~173</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>109</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-109 ANALYSIS section 3 cell 2 and the ruling on row D2-S34 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_109_20261014.md`) | **Rows:** IRPT_DASHBD-D2-W173-S<k> | **Decomp cell:** `DB-b-214` (decomposition section 111) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** `DB-b-213` (the issuer's read gate: DONE, the four alien objects are Inflection's own surplus). The next order of your queue, `DB-b-215` (the render), reads what you build; it stays `staged` until this one is complete.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-173` (branch `wk-IRPT_DASHBD-173`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~173/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, hashes and words only in the repo, a row or your report; an account number, a household or client id, a name or a figure is never recorded (an account's last four digits are `####`).

**Why.** The 49 Financial default report is complete except for its disclosure page. FWD-2 and FWD-21 need the SAME report for another firm, so round 109 renders one Inflection household. Round 108 built Inflection's `account_dim` and household key (980 accounts, 320 households) and measured two coverage facts (Orion's returns include dividends; Eclipse has no tax lots). This order builds the SAMPLE the render reads: the filled report (the contract's 117 members) for ONE household, from Inflection's own silver, in memory (nothing is written to S3). Where Inflection's silver gives a figure directly it fills; where it does not the member reads its true absent kind in plain words. You do not DERIVE returns here: a sibling worker derives the account returns and ties them out; until the CTO rules a tolerance on that read, an Inflection account return reads NO_SOURCE_YET.

**The grant of the S3 reads (BY PREFIX).** You may LIST and GET under `s3://opal-data-assets/orion/inflection/` and `s3://opal-data-assets/eclipse/inflection/` and nowhere else, ONLY through the round-108 adapter's GET-only reader (`InflectionSilverReader` in `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_dim.py`, which refuses any other path) and the served model series reader (`model_series_windows.read_served_series`, one GET of `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json`, the firm-neutral object `~169` already reads). The Orion master prefix `orion/4698/` and every other firm's place are NOT granted. No put, copy or delete of any kind. Orion's `fact_transactions` and `fact_performance` hold the FULL history in their NEWEST dated partition (row `W172-S1`): read the newest partition of those two and never walk every date; `fact_positions` and `fact_assets` are one as-of date each. The Orion silver guard reads FAIL (expected 4997, landed 5001, alien 4: `fact_assets` and `fact_positions` for 2026-08-06 and 2026-09-29, Inflection's own surplus): name that state in your record (below); do not read those two dates.

**The cell (`DB-b-214`).**
1. **Read first.** The issuer's check file `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r109/p109_round109.py` (your criterion: read `check_sample`, `pick_household`, `ACCT_WORDS`, `LOTS_WORDS`), the 49 Financial builder `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~169/build_sample.py` (its header states every rule: the filled-report shape, the units, the absent forms with kinds, the model benchmark path; copy its SHAPE and its firm-neutral parts, not its 49 Financial reads), the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` (0.4.3: 117 members, `absent_kinds`, `unheld_rule`), the Inflection adapter and record (`data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_dim.py`, `deliverables/0.9.0_WK_IRPT_DASHBD~171/ACCOUNT_DIM_R108.json`), the coverage record `~172/COVERAGE_READS_R108.json`, the guard record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/ALIEN_READ_R109.json` (its `result.guard_state_for_render_record` is the state you copy), and the CTO's round-109 analysis (the file above).
2. **The builder.** Copy `~169/build_sample.py` to `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~173/build_sample_inflection.py` and edit YOUR copy only (`git add` it: it must be tracked). It names no other firm's bucket, prefix or master id and holds no write-call name; it USES the Inflection adapter (`build_account_dim` and the GET-only reader) for the account dimension and the household key.
3. **The household.** Choose it by the deterministic rule the checker recomputes: among the households of the adapter's `account_dim` table with 2 or more accounts, the one whose sha256 of its household id (utf-8, hex digest) sorts lowest; record that digest as `household_ref_sha256` (never the id). The sample's `household` block is `{household_ref, as_of, first_data_date, accounts}` as the contract shape requires: `household_ref` a one-way token you derive (never the raw id), `as_of` the newest `fact_positions` date, one entry per account of that household (`account_id` in the custodian form the shape requires, `last4`, `first_data_date`, `window_status` for the four windows), the accounts in `account_id` order. State in `household_return_source.words` how you took each account's first data date.
4. **What fills, and from where (fill only what a source gives directly).** (a) `pvs.<w>.ending_value` for all four windows, `hold.ending_value`, `act.ending_value.household` and `act.ending_value.account` take the SAME figure: the market value of the household's positions at `as_of` from `fact_positions` (per account for the account grain; the sum for the household), so the whole-document rule finds them one figure; (b) `pvs.<w>.return_cumulative` (QTD, YTD, last 12 months, since inception) for the HOUSEHOLD take Orion's client-keyed `fact_performance`, read as the index level the row `W172-S3` states, converted to percent points to one decimal as the contract says, for the windows the series opens on, and absent with a true kind where it does not; (c) `hold.allocation` takes each asset class's share of the household's positions at `as_of` when `fact_positions` carries an asset class you can place in Opal's seven classes (say in `household_return_source.words` how you mapped them), else every entry is absent `NO_SOURCE_YET`; a class the household holds none of is the text `UNHELD`; (d) the 32 model benchmark members and the 12-month chart fill from the served model series through `model_series_windows` exactly as `~169` does (firm-neutral; the household's first day opens since-inception); (e) `cover.as_of_date` and `convention.inception_per_household_and_account` fill if a source gives them, else absent with a kind; (f) EVERYTHING ELSE is absent with its true kind by the round-105 rules (`NO_SOURCE_YET` where Opal has no source, `INSUFFICIENT_HISTORY` where a source is too short, `SOURCE_BREAK` where a source is broken). THREE groups have fixed words the checker reads: every account return (`avs.<w>.return_cumulative`, each by_row entry) is `{"absent": "Account-level returns are not available for this firm yet.", "kind": "NO_SOURCE_YET"}`; every lot member (`trgl.*` and `glr.*`, each by_row entry) is `NO_SOURCE_YET` with a reason that BEGINS "Lot-level detail is not available for this account yet." (the coverage member NO_LOTS); the six split members (`act.contributions.*`, `act.withdrawals.*`, `act.income.*` at household and account grain) stay `NO_SOURCE_YET` as for 49 Financial.
5. **Build the sample.** Run `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~173/build_sample_inflection.py . --out C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~173/` (run it in the background and wait for its summary; the builder's header names its flags). It writes `HOUSEHOLD_SAMPLE.json` there. The sample must pass the issuer's `check_sample_shape_k` and kind rules and the WHOLE-DOCUMENT rule (0 conflicts, 0 disagreements, 0 unmapped): import the check file by path and call `whole_document_scan(sample["values"], accounts_of(sample))` to read its denominator.
6. **Record** `BUILD_R109.json` in your folder with exactly: `sample` {`path` (the private path), `sha256`, `contract_sha256`}; `whole_document` {`cells_scanned`, `absent_cells`, `keys`, `unmapped` 0, `conflicts` 0} (the checker recomputes them); `household_ref_sha256`; `household_return_windows` (the list of the pvs return windows that fill, in the order qtd, ytd, last_12_months, since_inception); `household_return_source` {`source` (words naming the Orion table: it must contain `fact_performance`), `data_as_of` (ISO), `words` (how you read the index level, took first data dates and mapped classes; no figure)}; `orion_guard` (an exact copy of `result.guard_state_for_render_record` in the guard record); `builder` {`file`, `sha256`, `tracked` true}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `s3_reads` (integer)}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, paths, hashes and words only; no run of 8 or more digits except in a `sha256` value or a `path`, `file` or `key` field.

<criterion id="DB109-1-AC1" cell_refs="DB-b-214"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r109/p109_round109.py" . DB109-1-AC1</invocation><expect>DB109-1-AC1 PASS</expect></criterion>
`DB109-1-AC1` -- the private sample exists outside the repo, bound to its sha256 and to the contract's, passes the kind-aware shape and kind rules; the WHOLE-DOCUMENT rule keys every non-chart cell, reports 0 conflicts, 0 disagreements and 0 unmapped, its denominator equals the record's, and a planted conflict on a copy is caught; the household is the one the checker recomputes from the round-108 dry run (the lowest sha256 among households of 2 or more accounts) and the sample's accounts are exactly its accounts; every account return reads NO_SOURCE_YET with the fixed words, every lot member NO_SOURCE_YET with words that begin with the fixed lots sentence, the six split members stay NO_SOURCE_YET; at least one household return window fills and `household_return_windows` lists them; the household ending value fills in the four windows and `hold.ending_value`; `household_return_source` names `fact_performance` with an ISO date; `orion_guard` equals the issuer's read-gate state; the builder is the tracked copy in your folder, hashed, uses the Inflection adapter, names no other firm's place and holds no write call; no write, push or deploy. Base: FAIL (no record).

<expected_criteria>DB109-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the Inflection adapter and its tests, `~169/build_sample.py`, the reader module `model_series_windows.py`, every contract, every portal file and the issuer's check files.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the two granted Inflection prefixes ONLY through the adapter's GET-only reader; the one served-series GET through `model_series_windows`. Writes: the repo files of the grant and the private folder named above. No write to AWS of any kind, no deploy, no push, no vendor call, no secret read, no read of any other firm's place.
- **Client data.** The silver and the sample are client data: counts, hashes and words only in the repo, a row or your report.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A pair of cells that GENUINELY disagree is a finding: file a row naming the key and stop on that point; never plug a value. If a member's source does not exist in Inflection's silver, it is absent with its true kind, never a guess. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W173-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~173/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-214.inflection-sample-one-household-in-memory-from-silver.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 111 (round 109), cell `DB-b-214`.
<owned_cells>DB-b-214</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB109-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~173/IRPT_DASHBD.TO-DB-b-214.inflection-sample-one-household-in-memory-from-silver.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB109-1-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the household's account count and which windows of the household return fill (counts and words only); which members fill from a source and which are absent (by kind, as counts); how you took the account first data dates and mapped asset classes; the whole-document denominator (cells scanned, absent cells, keys); the guard state named; the number of S3 reads; any pair that genuinely differed; row ids. No account number, household or client id, name or figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a private builder copy and a private sample; nothing is read by served code, wired or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 LIST and GET of two Inflection-scoped prefixes through the round-108 adapter's grant-enforcing reader, plus the one served-series GET `~169` already makes; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB109-1-AC1 FAILS at base (no record) and the checker's household rule, whole-document rule and planted conflict are exercised by its self-test (9 arms) and the round-106 self-test (13 arms).
lane: the <paths> block IS the grant.
</preflight>
