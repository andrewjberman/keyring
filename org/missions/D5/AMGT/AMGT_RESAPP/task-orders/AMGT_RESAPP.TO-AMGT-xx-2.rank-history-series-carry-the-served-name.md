# AMGT_RESAPP task order -- `AMGT-xx-2` -- THE RANK-HISTORY SERIES CARRY THE SERVED COMPANY NAME, JOINED SERVER-SIDE

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_RESAPP/decompositions/AMGT_RESAPP_DECOMP.md</decomp_doc>
<owned_cells>AMGT-xx-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_AMGT_RESAPP~174</issued_to>
<issued_by>2.0.0_SA_COO~Z</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: DECLARED-NOT-APPLICABLE for this cell's own acts (local read-only DynamoDB in the checks). The Lambda's `dynamodb:GetItem` on `etf-classifications` is ALREADY granted (round 48); this cell must call nothing else.
comp-adversary: RUN by the issuer at the cut -- AC1 compares each series' name to the table row, reads a ticker the table does not hold, and reads the live axis; AC2 is the API and print suites (the bound).
EGRESS CLASS, declared: NONE beyond read-only DynamoDB on Opal's own tables.
</preflight>

## 1. THE CELL -- `AMGT-xx-2` (round 49, decomposition s.57)

The page's rank-history chart (`portal/src/pages/SecurityAnalysis/components/RankedChart.tsx`, `seriesLabel` at `:112`) labels a
line with `series.name` when the payload serves one, else with the ticker. The payload comes from
`GET /api/scoped/amgt/lead-panel/timeseries/<movement>/<subject>?tickers=...` ->
`lib/research/api/scoped_amgt.py` `read_rank_series(movement, subject, tickers, as_of_date=None, days=None)` (`:885`), whose
`series` entries carry `ticker` and `points` and NO name.

The join already exists for the ranked LIST (round 48): `_classification_for_ticker(ticker)` (`:588`) reads the canonical DynamoDB
table `etf-classifications` (key `ticker` = the BARE ticker: `"BA US"` -> `"BA"`) with ONE `GetItem` and answers
`{"status", "name", "classification", "name_state", "reason"}` (SERVED / ABSENT / READ_FAILED, every value as the table holds it);
`_join_classification(rows)` (`:626`) puts `name`, `classification`, `name_state` on each list row, one read per distinct ticker.

**Build:** each entry of `read_rank_series`' `series` carries `name`, `classification` and `name_state` from
`_classification_for_ticker` -- the SAME helper, one read per distinct ticker, on EVERY return path that returns series entries.
Nothing else in the payload changes: no rank, score, point, date, generation, completeness field or ordering moves; the no-tickers
path keeps its shape. Add tests (a stubbed table) pinning: a held ticker's series carries the table's name; an unheld ticker's
series reads `name_state` ABSENT with a null name; a READ_FAILED read is carried, not raised; points are byte-identical to the
un-joined read.

## 2. BOUNDS

1. **The adapter only.** No page file, no export file, no Terraform, no table write, no new AWS action (only the existing GetItem).
2. No S3 write, no deploy, no server. Standing: no install, no push, no promote, no vendor call. REFUSE, do not rescue.
3. Python from the repo root with `PYTHONPATH="$(pwd)"`.

## 3. SURFACES

<paths>
lib/research/api/scoped_amgt.py
lib/research/api/tests/
org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~174/
org/missions/D5/AMGT/AMGT_RESAPP/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository; DynamoDB `etf-classifications` and the ranking tables `read_rank_series` already reads.

## 4. PROOF OF SPEC (literal; timeout 120)

<proof_of_spec>
  <criterion id="AC1" cell_refs="AMGT-xx-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; PYTHONPATH="$(pwd)" python org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round49/checks/xx-2.AC1.py; echo "exit=$?"</invocation><expect>tickers asked N, series N, name SERVED M (M &gt; 0) and RANK-HISTORY SERIES CARRY THE SERVED NAME: YES -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="AMGT-xx-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; bash org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~Z/round48/checks/api-suite.sh; echo "exit=$?"</invocation><expect>pytest reports N passed and 0 failed (the cut's base passed; plus your new tests) -- and exit=0</expect></criterion>
</proof_of_spec>

AC1 the built behaviour against the real table and the live axis; AC2 the bound.

## 5. WHEN YOU ARE DONE

Instance at `org/missions/D5/AMGT/AMGT_RESAPP/deliverables/0.9.0_WK_AMGT_RESAPP~174/AMGT_RESAPP.TO-AMGT-xx-2.rank-history-series-carry-the-served-name.proof_of_spec.json`. Report once: what you changed and where, the AWS action(s) the code calls (must be GetItem only), how many live series read name_state SERVED, the commit hashes, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-48 analysis s.4 row 2 (@1dfd5c0970; DSGN_AMGTV1 round-4 analysis @177c576c80 s.2 ruling 5). Base: AC1
FAIL (tickers asked 3, series 3, name SERVED 0), AC2 PASS (api-suite rc 0, 61 s). SERVED: reaches the Lambda at xx-4, under a
never-widen pair written against xx-2's landed code; no IAM change (GetItem granted @26113dbc97). Worktree with portal at DEV
`ea248519` (the api suite reads portal harness files; round 48 rows Z-W171-S1/S2).

<status>pending</status>
<round>49</round>
<slot>~174</slot>
<fabric>site-z</fabric>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
