# TO IRPT_DASHBD.TO-DB-b-168 -- build, offline, the day-grain read of the 7 UNEXPLAINED segments: a tracked module with a plan, a live runner the issuer alone runs, an analysis and a self-test; the worker makes no vendor call and reads no credential

<to_id>IRPT_DASHBD.TO-DB-b-168</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~134</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>90</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 6986, ROUND-90 ANALYSIS @d573cb1cb8 section 3 item 2 | **Rows:** NONE | **Decomp cell:** `DB-b-168` (decomposition section 92) | **outcome_ref:** FWD-8 | **depends_on:** DB-b-167 (drained @b70da0aa6a).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-134` (branch `wk-IRPT_DASHBD-134`); run everything from its root. Your folder is
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~134/`. Your private folder (client data lives only here, outside the repo) is
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~134/` (create it).

**Why.** Round 89 gave a stated reason to 5 of the 12 segments that neither flow convention closes; 7 stay UNEXPLAINED, one in each of 7 accounts. The stored tables hold Black Diamond at segment grain, so they cannot show which DAY differs. The CTO's
ruling: read Black Diamond's daily figures for those 7 accounts over those 7 segments through IRPT's existing per-account call, list the days that differ, and give each a reason. **You build the instrument; the issuer runs the one live read; another worker reads the result.**
You make NO vendor call and read NO credential: the live mode below is yours to WRITE and never yours to RUN.

**The cell (`DB-b-168`).** ONE new tracked module `org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_day_read.py` (ASCII, passes `bash .tools/commit-gate.sh`), invoked `python -I tieout_day_read.py <repo_root> <mode> [--go]`, with exactly these four modes:
1. **`plan`** (OFFLINE; set `DRY_RUN=1` before importing the estate's client, which then refuses any network call; S3 GET/LIST of the cross-reference table `s3://opal-data-assets/blackdiamond/49f/silver/dim_account_xref/` only). Select the 7 UNEXPLAINED segments by
   reproducing `tieout_neither_reasons.py`'s selection (import it by path, do not edit it; assert 7 segments in 7 accounts, else stop); map each account to its Black Diamond internal id by the tier-1 rule of `0.9.0_WK_IRPT_DASHBD~6/bd_population_pull_e3.py` (`load_xref`, `map_account`, imported
   by path); build ONE `performanceSeries` request body per account for that account's segment `[start, end]` with the estate's own helper (the series body is built where the estate builds it: read `infra/aws/lambda/investor-reporting/performance/bd_adapter.py` (`adapt`, `parse_series`), `tenants.py` for the route, and
   `infra/aws/lambda/opal-assets/opal-assets-bd49f-reporting-pull/lambda_function.py` for the body helper; a LOCAL RESTATEMENT of a request body is refused by the adapter's own docstring). **ISSUER'S RULING (amendment, after row IRPT_DASHBD-D2-W134-S1): the estate has exactly one definition of the series body, inline in `bd_selected.requests_for` (line 61 onward), behind a Cottonwood-only mapping guard.** Build the 49F body from
   `bd_adapter.build_period_request(vendor_id, start, end, start, int(end[:4]))` by THE SAME TRANSFORMATION that function applies (the `series` dict: `perfFrequency` 0, `groupings` ["Account"], `dateRange` {start, end, excludeHistoryRanges false}, the period body's `dataPointOptions` minus `asOfDatePoints` and `dateRangePoints`, empty `benchmarks`, a deep copy of `benchmarkLevelDisplay`), with `accountFilters.accounts` = [vendor_id].
   You do NOT call `requests_for` for production and you do NOT hand it a Cottonwood mapping to get past its guard. Instead `selftest` PROVES the parity: it imports `bd_selected` by path and asserts that, for one synthetic input (a synthetic Cottonwood-shaped mapping used only inside the test, with no network and no session), your builder's body equals `bd_selected.requests_for(...)["performanceSeries"]` exactly,
   and it prints `SELFTEST PASS` only when that holds. State in the module's docstring that the transformation is a re-derivation guarded by that parity test. Add `series_body_parity_with_estate_test`: true to the record's `runner` object (the checker ignores the key; the issuer reads it). If the parity test cannot be made to pass, file a row and stop. Write the plan to your PRIVATE folder
   (`DAY_READ_PLAN.json`: request bodies, mapping, the 7 segments; it holds account ids and never enters the repo) and print COUNTS ONLY: `requests`, `daily_ranges`, `vendor_calls` 0, `plan_sha256` (of the canonical bodies).
2. **`pull --go`** (LIVE, the issuer's, NEVER run by you). Model it on `~6/bd_population_pull_e3.py`'s `refusal_checks` and `pull` and `~25/bd_split_pull.py`. Refuses (exit non-zero, message naming `--go`) unless: `--go` is given; the private plan exists; the plan rebuilt from scratch equals the written plan (hash); NO pull record exists
   (no second pull); then lifts `DRY_RUN`, mints the session once through the estate's helpers (`load_bd_session`, `get_clientview_token`), sends each account exactly once at 1 request per second, one transient retry, aborts on the first non-transient error, and writes each raw response and a pull record
   ONLY under `<your private folder>/pull/` (no S3 write, no landing, no copy anywhere else). A credential, cookie, bearer or response body is never printed and never written outside that folder. It prints counts only (`requests`, `http_ok`, `http_failed`, and whether each response's last cumulative equals the stored window return: a bool per request, in plan order).
3. **`analyze`** (OFFLINE). Reads the private `pull/` responses and the stored tables (`0.9.0_WK_IRPT_DASHBD~108`, read-only), and for each of the 7 builds the daily table PRIVATELY: for each date, our served daily return and Black Diamond's daily return (from the ratio of consecutive cumulatives), the difference in pp, and whether it exceeds the day-differs line
   `DAY_DIFFERS_PP = 0.01`. It prints counts only (days, days differing). The reason assignment is NOT yours: it is the next cell's, under its own rule file.
4. **`selftest`** (OFFLINE; reads no private table, calls no network, loads no session). A synthetic fixture you write into the module: a window whose daily returns differ on a few days, whose uncorrected window misses 0.35 pp, whose correction of one named cause re-closes it, plus a negative arm where a window with no correctable cause stays open.
   Prints `SELFTEST PASS` only when all of that holds.
5. **Run `plan` once, offline** and `selftest`. Do NOT run `pull`. Do NOT run anything that loads a session. If `plan` cannot be completed offline, file a row and report what is missing.
6. **Record** `DAY_READ_BUILD.json` in your folder, exactly these keys: `tolerance_pp` 0.35; `code` {`file`: "org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_day_read.py", `sha256` (of its committed bytes), `tracked`: true}; `population` {`unexplained_segments`: 7, `accounts`: 7}; `plan` {`requests`: 7, `daily_ranges`: 7, `vendor_calls`: 0, `dry_run`: 1,
   `plan_sha256`, `kept_private`: true}; `runner` {`modes`: ["plan", "pull", "analyze", "selftest"], `refuses_without_go`: true, `refuses_second_pull`: true, `writes_only_private`: true, `plan_equals_rebuilt_plan_check`: true, `credential_logged`: false} (each of these claims is a property of the code you wrote, which you read back before you write it true); `reads` {`vendor_calls`: 0, `secret_reads`: 0,
   `s3_writes`: 0}; `served_values_changed`: false; `limits`. NO account id, client name, amount or run of eight or more digits in the record or your report.

<criterion id="DB90-1-AC1" cell_refs="DB-b-168"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r90/p90_round90.py" . DB90-1-AC1</invocation><expect>DB90-1-AC1 PASS</expect></criterion>
`DB90-1-AC1` -- the record exists with the keys above; the module is tracked and hashes to the stated sha256; the plan is 7 requests over 7 daily ranges with zero vendor calls; the module's `pull` without `--go` refuses; its `selftest` prints `SELFTEST PASS`; no credential logged, no S3 write; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB90-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited. `tieout_neither_reasons.py`, `tieout_flow_timing.py`, `bd_adapter.py` and every stored table are READ ONLY.
- **No vendor call, no credential read, no session load.** You never run `pull`, never call `load_bd_session`, `get_clientview_token` or any network function, never read a cookie or credential file, never open a browser. Reading the estate's CODE that does these things (to model your runner on it) is allowed and is not running it.
- **No served write.** No S3 put, copy or delete; no Lambda, Terraform or IAM act; no deploy; no push. S3 GET/LIST only of the cross-reference prefix named above.
- **No client data in what you write.** Counts and booleans only in the repo; plan, bodies, ids and responses live only in your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only. Commit with `.tools/safe-commit.sh` as your definition says.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W134-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES, never re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~134/
org/missions/D9/IRPT/IRPT_DASHBD/tieout/tieout_day_read.py
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-168.day-grain-read-of-the-seven-built-offline.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 92 (round 90), cell `DB-b-168`.
<owned_cells>DB-b-168</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB90-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~134/IRPT_DASHBD.TO-DB-b-168.day-grain-read-of-the-seven-built-offline.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB90-1-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the module's commit; the four modes and how `pull` refuses; the plan's counts; how `selftest` is built; anything about the series request the issuer must know before running `pull --go` (the body's range, the response's shape, whether a last-cumulative equals the stored window return is checkable); any row ids. Counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; the worker builds an instrument and runs nothing live; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS write or grant; the plan reads one cross-reference prefix; the live runner is the issuer's later act.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record, no module) and its refusal limb runs the module's `pull` without `--go`.
lane: the <paths> block IS the grant.
</preflight>
