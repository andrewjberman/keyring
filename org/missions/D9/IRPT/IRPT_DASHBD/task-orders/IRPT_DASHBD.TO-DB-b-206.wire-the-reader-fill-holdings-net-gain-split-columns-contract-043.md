# TO IRPT_DASHBD.TO-DB-b-206 -- the DATA HALF of round 106: the DB-b-204 model-windows reader wired into the sample builder (the count of the 32 benchmark members filled printed), the holdings household Net Gain filled from the figure the value summary prints, the split columns NO_SOURCE_YET, contract 0.4.3 (text only), and a sample that passes the whole-document absent-vs-printed rule

<to_id>IRPT_DASHBD.TO-DB-b-206</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~169</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>106</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-106 ANALYSIS section 2 cells 1 and 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_106_20261014.md`) on the CVO's grade `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_105_L9_GRADE_20261014.md` | **Rows:** IRPT_DASHBD-D2-W169-S<k> | **Decomp cell:** `DB-b-206` (decomposition section 108) | **outcome_ref:** FWD-21 | **depends_on:** none. The next order of your queue, `DB-b-207` (the render remedy), reads what you build; it stays `staged` until this one is complete.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-169` (branch `wk-IRPT_DASHBD-169`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~169/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, hashes and words only in the repo, a row or your report. Write an account's last four digits as `####` anywhere a sentence is recorded, never the digits.

**Why.** The CVO graded round 105's judgment criterion FAIL on two instances. (1) The Holdings Overview's household row reads "Not available yet" for Net Gain in four windows, under a note that says the figure "needs more history", while the Portfolio Value Summary prints the household Net Gain for the same four windows: the member `hold.net_gain_<window>` is absent while `pvs.<window>.net_gain` is filled, and they are the SAME figure. (2) Two chart notes claim a reason for charts whose values print elsewhere (the view half is your next order). The CTO also ruled the split columns (Contributions, Withdrawals, Income) are `NO_SOURCE_YET`, not `INSUFFICIENT_HISTORY` (Net Additions, their sum, prints; Opal does not split it yet), that the DB-b-204 reader replaces `~159`'s model-series code in the builder, and that a window the account did not span is words and never the dash (the contract text says otherwise today). Round 105's six-pair rule missed (1) because it was a hand-picked list; the issuer replaced it with a rule over EVERY absent cell, keyed (measure, entity, window), which finds exactly the four hold.net_gain conflicts on the round-105 sample and prints its denominator.

**The cell (`DB-b-206`).**
1. **Read first.** The issuer's check file `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r106/p106_round106.py` (your criterion: read `check_build`, `whole_document_scan`, `figure_key`; run `python -I <that file> --selftest .` from your root to see the rule's arms; you may import it by path and call `whole_document_scan(sample["values"], accounts_of(sample))` on your sample), the previous builder `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~167/build_sample.py` (its header states every rule and every read; do not change a rule not named here), the previous record `~167/KIND_CARRIER_R105.json` (its `kind_sites`), the contract `org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json` at 0.4.2, and the reader `data/assets/scripts/gold/irpt_reporting/adapters/model_series_windows.py` with its tests (`read_served_series`, `windows_from_series`, `source_claim`; READ-ONLY here: it belongs to a closed order; if it lacks something you need, file a row and stop on that point). The previous sample is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~167/HOUSEHOLD_SAMPLE.json` (read-only client data).
2. **Contract 0.4.3 (text only; the contract is YOURS to edit; no other file under `org/standards/`).** Set `contract_version` to `0.4.3`; add the 0.4.2 bytes to `lineage` the way the existing entries are written (`{"contract_version": "0.4.2", "sha256": "e9c389b75c1981bfe8a2aee9ebb8b0b21f45c686071b75950bb5db2e806e151d", ...}`); in `document.absent_rule` replace ONLY the clause that says a window the account did not span "prints the not-held dash" with one saying a window the account did not span (NOT_SPANNED) carries INSUFFICIENT_HISTORY and prints words, never the dash, and that the dash means only that the household holds none of the asset class (UNHELD) (the rule must contain the phrases `did not span` and `words` and must no longer contain `not-held dash`); change nothing else: every member stays byte-for-byte the 0.4.2 member, `absent_kinds` and `unheld_rule` stay. Valid JSON, ASCII.
3. **The builder.** Copy `~167/build_sample.py` to `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~169/build_sample.py` and edit YOUR copy only (`git add` it: it must be tracked). (a) WIRE THE READER: the builder imports the module `model_series_windows` from `data/assets/scripts/gold/irpt_reporting/adapters/` by file path (importlib), reads the served series through `read_served_series` with a reader whose only method is a GET (`get_object(bucket, key)` returning `(bytes, version_id)`; the builder's reader stays GET and LIST only), and takes EVERY model benchmark window value from `windows_from_series(series, as_of, household_first_day)` (as_of the builder's R, the household first day as it uses today). Delete `def model_series(` and any helper only it used (`compound`, `model_lo`, `bench_value`) once nothing calls them; the 12-month chart may keep a local cumulative-points helper fed by the series the module returned. A `None` window becomes an absent form with its words and its kind: INSUFFICIENT_HISTORY when the series does not open on the window's first day, SOURCE_BREAK when the series misses a trading day of the window. Drop the old `--model-series` private-file flag (the served object is the input). The claim from `read_served_series` (source: the key and its VersionId; data_as_of) goes to your record and the build counts, never into the sample. (b) FILL, do not re-explain: `hold.net_gain_last_12_months`, `hold.net_gain_ytd`, `hold.net_gain_qtd` and `hold.net_gain_since_inception` take the VALUE of `pvs.<window>.net_gain` (the same fold, no second derivation); `hold.net_gain_mtd` and every `hold.return_*` stay absent with their true kind. (c) THE SPLIT COLUMNS: every absent form of `act.contributions.*`, `act.withdrawals.*` and `act.income.*` (household and account) has kind `NO_SOURCE_YET` and reason words that say Opal does not split net additions into contributions, withdrawals and income yet. (d) Change nothing else. After your edits the whole-document rule must report 0 conflicts, 0 disagreements and 0 unmapped on your sample.
4. **Build the sample.** Run `python -I org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~169/build_sample.py . --out C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~169/` (the builder's header names its flags; the default firm is 49financial; run it in the background and wait for its summary: it LISTs and GETs S3 as `~167` did plus the one GET of the served series, nothing more). It writes `HOUSEHOLD_SAMPLE.json` there.
5. **Record** `BUILD_R106.json` in your folder with exactly: `contract` {`version` "0.4.3", `sha256`}; `sample` {`path` (the private path), `sha256`, `contract_sha256` (the contract's sha256 at the time of the build)}; `whole_document` {`cells_scanned`, `absent_cells`, `keys`, `unmapped` 0, `conflicts` 0} (the checker recomputes every figure; they must equal its own denominator); `absent_by_kind` {`NO_SOURCE_YET`, `INSUFFICIENT_HISTORY`, `SOURCE_BREAK`: integer counts over EVERY absent form of the sample, members and by_row entries}; `model_windows` {`source` (the served key and its VersionId), `data_as_of` (ISO), `members_total` 32, `members_filled` (the count of the 32 benchmark members that fill; print it in your report), `reader_module` (the repo path of the module)}; `builder` {`file`, `sha256`, `tracked` true}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `s3_reads` (integer)}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, paths, hashes and words only: no client name, account number or figure; no run of 8 or more digits except in a `sha256` value or a `path`, `file`, `key` or `commit` field.

<criterion id="DB106-1-AC1" cell_refs="DB-b-206"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r106/p106_round106.py" . DB106-1-AC1</invocation><expect>DB106-1-AC1 PASS</expect></criterion>
`DB106-1-AC1` -- the contract is 0.4.3 with the 0.4.2 bytes in its lineage, an `absent_rule` that says a window the account did not span prints words and never the not-held dash, every member byte-for-byte the 0.4.2 member (compared with the 0.4.2 version in git history); the private sample exists outside the repo, is bound to its sha256 and to the contract's, passes the kind-aware shape rule and the kind rules; the WHOLE-DOCUMENT rule keys every non-chart cell (measure, entity, window), reports 0 conflicts, 0 disagreements and 0 unmapped, its denominator equals the record's, and a planted conflict on a copy of your sample is caught; `hold.net_gain_<window>` is filled and equals `pvs.<window>.net_gain` for last 12 months, YTD, QTD and since inception; every absent form of the six split members is NO_SOURCE_YET; `absent_by_kind` equals the checker's count; `members_filled` equals the checker's count of the 32 benchmark members and the claim names the served key, its VersionId and an ISO date; the builder is the tracked copy in your folder, hashed, imports `model_series_windows` and no longer defines `model_series()`; no write, push or deploy. Base: FAIL (no record).

<expected_criteria>DB106-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including `~167/build_sample.py`, the reader module and its tests, every other contract, every portal file and the issuer's check files.
- **Reads and writes.** Reads: repo files and the S3 GET and LIST the `~167` builder's header lists, plus the one GET of `s3://opal-data-portal-v2/json/benchmarks/model_portfolio_timeseries.json` through the reader (a denial is recorded verbatim, not retried by another route). Writes: the repo files of the grant and the private folder named above. No write to AWS of any kind, no deploy, no push, no vendor call, no secret read, no `bun install`.
- **Client data.** The sample is client data: counts only in the repo, a row or your report; an account's last four digits are `####`.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A pair of cells that GENUINELY disagree (both filled, different values) is a finding: file a row naming the key and stop on that point; never plug a value. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W169-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~169/
org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-206.wire-the-reader-fill-holdings-net-gain-split-columns-contract-043.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 108 (round 106), cell `DB-b-206`.
<owned_cells>DB-b-206</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB106-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~169/IRPT_DASHBD.TO-DB-b-206.wire-the-reader-fill-holdings-net-gain-split-columns-contract-043.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB106-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the contract change (version, lineage, the absent_rule sentence); the whole-document denominator (cells scanned, absent cells, keys) and that it reports 0 conflicts; how the reader is wired and what you deleted from the builder; the claim (key, VersionId, data_as_of) and HOW MANY of the 32 benchmark members fill (and which windows are absent, if any); the count of absent forms by kind; any pair that genuinely differed; row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a contract text edit, a private builder copy and a private sample; nothing is read by served code, wired or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 GET and LIST by the same builder `~167` ran, plus one GET of the served series object the `~168` reader reads; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB106-1-AC1 FAILS at base (no record); the whole-document rule is exercised by the checker's self-test (13 arms, green and red), by a planted mutant inside the criterion, and by a real red arm on the round-105 sample (exactly the CVO's four conflicts, 0 unmapped).
lane: the <paths> block IS the grant.
</preflight>
