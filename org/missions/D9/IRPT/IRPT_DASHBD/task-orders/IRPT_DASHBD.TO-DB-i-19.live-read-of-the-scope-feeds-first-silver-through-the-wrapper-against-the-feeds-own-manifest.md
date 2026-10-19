# TO IRPT_DASHBD.TO-DB-i-19 -- the LIVE READ: the Scope feed's first landed silver run through the round-127 wrapper into a PRIVATE directory (the first real run), each landed day's bronze manifest read through the GET-only reader, rows counted against that manifest, trading days from lib/trading_calendar.py; Inflection only; counts and verdict words only

<to_id>IRPT_DASHBD.TO-DB-i-19</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~319</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>132</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_131_20261016.md` (msg 8916 and erratum @b81e9bc3c4: "Inflection only"; open call 2d0b): "ONE read cell: the live silver and wrapper output for that day, rows counted against the feed's own manifest, with the trading-calendar fix as its criterion."

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-319`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~319/`. Your PRIVATE folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~319/` (create it). Never touch a path outside the `<paths>` block below and your private folder.

**Why.** The Scope feed (IB-pr-596) has landed its first silver partition. Rounds 123 to 131 built and tested the adapter, the wrapper and the run script on fixtures. This cell is the FIRST RUN ON REAL ROWS: it runs the round-129 run script on the landed silver into a private directory and checks the result against the feed's own manifest, so that what the wrapper writes is graded against what the feed says it wrote. It is read-only against AWS (GET and LIST) and writes only to your private folder.

**Read first (read only).**
- `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~316/run_scope_feed_real.py` (`run_real`, `main`, `TABLE_URI`): you import `run_real` from it by path and do not edit it.
- `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_dim.py` (`InflectionSilverReader`: `list_partitions`, `read_parquet`, `_split`, `_api`, `reads`; `build_account_dim`; `FIRM`) and `inflection_account_return_daily.py` (`ORION_SILVER`).
- `data/inf/manual_api/pull_inflection_scope_account_returns.py` (the bronze envelope: `feed_addresses`, `calls[].row_count`, `universe_rows`, `households_failed`, `households_without_id`; the bronze object is `scope.json.gz`, gzip JSON).
- `lib/trading_calendar.py` (`trading_days_between`).
- The checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r132/p132_live.py` (its record whitelist, extract shape and recounts ARE the specification; read it first and run `python -I <it> --selftest`).

**The cell (`DB-i-19`).**
1. **The script:** tracked `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~319/live_read.py`, the only code this cell adds. It builds `reader = iad.InflectionSilverReader()`, imports `run_real` from the round-129 script, takes trading days from `lib.trading_calendar` (`trading_days_between` returning ISO strings), and defines NO weekday helper of its own. It holds no write call, no vendor call, no credential and no `s3://` literal (addresses from `feed_addresses` / `TABLE_URI`).
2. **The real run.** `dim_ids` = `iad.build_account_dim(<latest fact_positions frame>, <latest fact_assets frame>).column("account_id").to_pylist()` (as in the round-129 script's `main`). Call `run_real(reader, <private out dir>, dim_ids, <trading-days function>, iad.FIRM, 0)` with the output directory INSIDE your private folder and not yet existing. Its return value is the `run` record. If its status is `NO_SILVER_YET` or `STOPPED_AT_CAP`, STOP: write the record with that status (the checker will read FAIL, which is the right answer: the cell was cut too early or the cap is too low) and report; do not widen the cap and do not retry.
3. **The manifest read.** For each landed day (the `date=<day>` partitions of the silver table), read that day's bronze envelope through the same reader (list the bronze table prefix with `list_partitions`, read `date=<day>/scope.json.gz` with `reader._api().get_object(...)` after `reader._split(<uri>)`, count each GET in your own read counter; the grant check of `_split` is the guard) and keep ONLY: `universe_rows`, the length of `households_failed`, the list of `calls[].row_count`, and the length of `households_without_id`. Never keep a response body. Silver rows per day = the length of that day's silver frame.
4. **The private extract** `live_extract.json` in your private folder: `{"days": {"<iso day>": {"silver_rows": int, "universe_rows": int, "households_failed": int, "call_row_counts": [int, ...], "households_without_id": int}}}`.
5. **The record** `SCOPE_LIVE_READ_R132.json` in your folder with EXACTLY the keys the checker's `REC_KEYS` names: `script` {`file`, `sha256`}; `extract` {`path` (absolute, private), `sha256`}; `run` (the `run_real` return value, unchanged); `days_total`, `days_manifest_agree`, `days_manifest_disagree`, `days_with_failed_households`, `trading_days_in_window` (recount from the extract; the checker recomputes them); `expected_rows` (accounts_in_feed x trading_days_in_window); `rows_accounted` (rows_present + rows_absent); `verdict` (`MANIFEST_AGREES` when every day agrees, else `MANIFEST_DISAGREES`); `reads` {`s3_reads` (your counter plus `run["s3_reads"]`), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false; `basis_words` (words, at least 200 characters: how many days landed, how the silver row counts compare with the manifest, which days disagree and by how many rows (as counts, never dates), how many ABSENT rows per reason class, what the boundary measure read (pairs, pairs equal, the maximum relative difference in basis points) and the chain check's status, and what this does not establish; NO value, NO date, NO account or household id). No run of 8 or more digits except in a `sha256` value or a `path` / `file` field; no date and no partition name anywhere in the record.
6. **Do not fix.** If the wrapper refuses the real silver, or the manifest disagrees, or the boundary measure reads a large difference, that IS the result: record it with its verdict and a surprise row; never edit the wrapper, the run script or the feed, never choose another window, never retry with a changed rule.

<criterion id="DBI132-1-AC1" cell_refs="DB-i-19"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r132/p132_live.py" . DBI132-1-AC1</invocation><expect>DBI132-1-AC1 PASS</expect></criterion>
`DBI132-1-AC1` -- the record is complete and carries no identifier or date; the script is a tracked file hashed as recorded with no write, vendor-call or credential token, built on `InflectionSilverReader`, taking trading days from `lib/trading_calendar.py`; the extract's hash equals the recorded one; the run status is `RAN`; the day count, the per-day agreement of the silver row count with the bronze manifest, the trading-day count from the calendar, accounts x trading days = rows_present + rows_absent and `trading_days_unaccounted` 0 all equal the checker's recompute from the extract; no write, no push, no deploy. Base: FAIL (no record).

<expected_criteria>DBI132-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and your private folder. Everything else is read, never edited, including the adapter, the wrapper, the run script, the feed script, `lib/`, `infra/` and every issuer check.
- **Reads only.** GET and LIST through `InflectionSilverReader` (and its `_api().get_object` for the bronze objects, after `_split`). No S3 write, no vendor call, no secret read, no push, no deploy. Read cap: 400 (LIST pages plus GETs); a cap hit is a recorded result, never widened.
- **Client data.** The silver, the bronze, the wrapper's output and the extract are private; the repo, rows and your report carry counts and verdict words only.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W319-S<k>`, `surfaced_at` from `date -u +%FT%TZ` at filing; append as BYTES. Commit with `.tools/safe-commit.sh`. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~319/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-19.live-read-of-the-scope-feeds-first-silver-through-the-wrapper-against-the-feeds-own-manifest.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 18, cell `DB-i-19`.
<owned_cells>DB-i-19</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI132-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~319/IRPT_DASHBD.TO-DB-i-19.live-read-of-the-scope-feeds-first-silver-through-the-wrapper-against-the-feeds-own-manifest.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI132-1-AC1` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the run status; the number of landed days; days whose silver count agrees with the manifest and days that do not (counts); rows PRESENT and ABSENT and the ABSENT count per reason class; the boundary measure and the chain check status as the run record states them; the S3 reads made; row ids. No token, no client value, no account or household id, no date.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one read script and private files; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: GET and LIST of Opal's own Orion silver and bronze through the round-108 reader (granted prefixes, the principal rounds 108 to 111 and 126 used); no new principal or grant, no write.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI132-1-AC1 FAILS at base (no record), and the checker's self-test builds a GOOD record from the feed's own writer (PASS) and ten mutants (a wrong verdict, a wrong day count, rows not accounted, trading days unaccounted, a run that did not run, an S3 write, a date in the record, a manifest that disagrees in the extract, a put_object script, a script with its own weekday helper): each FAIL.
</preflight>
