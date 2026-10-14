# TO IRPT_DASHBD.TO-DB-b-186 -- READ how the Black Diamond lots whose ticker is CASH classify: the canonical row, the gold classifier's answer, and the class the Advisor Intelligence and Investor Reporting pages serve for them; read only

<to_id>IRPT_DASHBD.TO-DB-b-186</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~151</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>100</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7422 ("read how the 11 CASH lots classify, served class per lot and per page. Andrew's 'Cash as a ticker should be CASH' lives near there.") | **Rows:** IRPT_DASHBD-D2-W151-S<k> | **Decomp cell:** `DB-b-186` (decomposition section 102) | **outcome_ref:** FWD-8 class label | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-151` (branch `wk-IRPT_DASHBD-151`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~151/`.

**What is known (the issuer's own read, 2026-10-14).** The newest Black Diamond lot snapshot, `s3://opal-data-bd/gold/timeseries/holdings_lots/2026-10-09.parquet`, holds 1,314,777 lot rows; the column `ticker` carries the value `CASH` on exactly 11 of them (the synthetic ticker `CASH_USD` on none). Black Diamond's own cash line is named by the ticker `CASH` and the description `CASH` (the Investor Reporting snapshot builder treats that pair specially: `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, function `classify_security`, about line 966). The gold ETF classifier (`data/black_diamond/scripts/gold/lib/etf_classifier.py`) answers a ticker from the canonical table `etf-classifications` (DynamoDB, us-east-1, key `ticker`), and now serves the class `cash` for a row typed Cash by `sub_asset_class`. Andrew's smoke note reads: "Cash as a ticker should be CASH". Nobody has read how these 11 lots are classified or what each page serves for them.

**The cell (`DB-b-186`): a READ. Nothing is changed, deployed or written.**
1. **The lots.** Read the snapshot's `ticker` column (and `description` or the asset-name column if one exists; list the column names you used in `lots.columns_used`) with pyarrow from a script file under `python -I`, by one S3 GET of that one key. Record `lots` {`snapshot` "2026-10-09", `rows_scanned` (the file's row count), `cash_stem_ticker_lots` (rows whose ticker equals `CASH`, exact, upper-cased), `accounts` (distinct accounts among them, by count only), `distinct_tickers` (distinct tickers containing the stem `CASH` among all rows, a count), `lots_with_description_cash` (of those lots, how many have a description or asset name equal to `CASH` after trimming and upper-casing), `open_lots`, `closed_lots` (use the snapshot's own open/closed or quantity/status columns; say in `lots.open_closed_rule` how you decided), `columns_used`, `open_closed_rule`}. Counts only: no account id, no value, no name.
2. **The canonical row.** One DynamoDB `get_item` on `etf-classifications` for the key `CASH` (read-only, the box's existing identity): `canonical_row` {`exists`, and when true `asset_class` and `sub_asset_class` as stored, `read_from` "etf-classifications get_item"}. Also `get_item` for the key `CASH_USD` and say in `canonical_row.cash_usd_row_exists` whether it has a row.
3. **The gold classifier.** Instantiate `ETFClassifier` with a stub client that returns the row you just read (a test seam; no AWS from the classifier; see the existing tests under `data/black_diamond/scripts/gold/tests/` for the stub) and record `gold_classifier` {`classify` (the class `classify('CASH')` returns; an empty string means unclassified), `classify_with_identity_class` (first element of `classify_with_identity('CASH', 'CASH')`), `basis` (one sentence: canonical row, name path, or none)}.
4. **The pages.** For each of the two pages record one entry in `served_per_page`: `{page, established, store, served_class, read_from, positions_seen}`.
   - `advisor_intelligence`: the served per-advisor positions files `opal-data-49financial advi/49financial/platinum/advisors/{id}/positions.json` (round 96's count read them; S3 GET and LIST only; enumerate through `comp-pipescript io` first). `positions_seen` counts the positions whose ticker is `CASH` and `served_class` is the class string they carry (or `mixed` with the counts in the words, or `NOT_ESTABLISHED`).
   - `investor_reporting`: the page reads a published holdings snapshot; trace its store from `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` and `infra/aws/lambda/investor-reporting/holdings/snapshot.py` (round 98's record names the hops: `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~149/IR_HOLDINGS_CLASS_SOURCE.json`), and if a published object is readable under your identity read it (counts and the class string only); else say `NOT_ESTABLISHED` with `reason`. Record `investor_reporting_special_case` {`rule_at` (file and line), `requires_ticker_and_description_both_cash` (bool), `lots_that_meet_it` (from step 1)}.
   An entry you cannot establish has `established` false, `served_class` exactly `NOT_ESTABLISHED`, and a `reason`.
5. **Say it in words.** `what_the_page_shows_in_words`: for each page, what a reader of the 11 lots sees in the class column today and why; and whether "Cash as a ticker should be CASH" is a class label (asset class reads `cash`), a ticker label, or a display mapping (look at the portal's class-to-label mapping: `portal/src/pages/InvestorReporting/tabs/holdings/assetClass.ts` and the Advisor Intelligence equivalent, read only). `recommendation`: one or two sentences: what, if anything, must change (which file, which rule), without writing it.
6. **Record** `CASH_LOTS_CLASS_READ.json` in your folder with exactly: `lots`; `canonical_row`; `gold_classifier`; `served_per_page`; `investor_reporting_special_case`; `what_the_page_shows_in_words`; `recommendation`; `reads` {`dynamodb_writes` 0, `s3_writes` 0, `vendor_calls` 0, `secret_reads` 0}; `deployed` false; `pushed` false; `served_values_changed` false. Counts and words only: no account id, no client name, no figure, no run of eight or more digits (a path, key or file under a key named `path`, `key` or `file` is exempt).

<criterion id="DB100-1-AC1" cell_refs="DB-b-186"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r100/p100_round100.py" . DB100-1-AC1</invocation><expect>DB100-1-AC1 PASS</expect></criterion>
`DB100-1-AC1` -- the record reads the 2026-10-09 snapshot at 1,314,777 rows with 11 lots whose ticker is CASH (the issuer's own anchor), counts accounts, open and closed lots and the lots meeting the Investor Reporting special case; states the canonical row (exists or not) and where it was read; states what the gold classifier returns; holds one entry for each of the two pages, each established or NOT_ESTABLISHED with a reason; says in words what each page shows and gives a recommendation; no write, deploy or push; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB100-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. You edit no product, portal or classifier file.
- **No write of any kind to AWS** (no DynamoDB put/update/delete, no S3 put/copy/delete, no Lambda, Terraform or IAM act), **no deploy, no push, no vendor call, no secret read.** Reads only: S3 GET/LIST, two DynamoDB `get_item` calls, repo files. A denial is recorded verbatim, not retried by another route. If the comp-rail hook refuses a raw S3 call, run what it says next, or annotate `# rail-checked: <why>` (audited).
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If your count of CASH lots differs from 11, record yours with the reason and file a row; the criterion will fail and the issuer will read why. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W151-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~151/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-186.cash-ticker-lots-class-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 102 (round 100), cell `DB-b-186`.
<owned_cells>DB-b-186</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB100-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~151/IRPT_DASHBD.TO-DB-b-186.cash-ticker-lots-class-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB100-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the lot counts (rows, CASH lots, accounts, open, closed, those meeting the IR special case); the canonical row; what the gold classifier returns; for each page the served class (or NOT_ESTABLISHED and why); what Andrew's note most likely means in one sentence; the recommendation; any row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read; nothing is changed, deployed or written.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 GET/LIST and two DynamoDB get_item calls with the box's existing identity; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on 16 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>
