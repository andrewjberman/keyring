# TO IRPT_DASHBD.TO-DB-i-9 -- the SCOPE HISTORY PROBE: TWO Scope calls (round 117's household A and round 120's household B), inner body, calcGrossOfFees false, Daily, each from the household's earliest Orion account start date to 2026-10-13; the series length of every account, whether the chained daily factors reproduce Orion's own period return, whether each series is as long as the trading days since the account's start, the call time and the response size, and from them the one-time backfill's request, time and size bound for the whole universe; a vendor READ, raw responses private, nothing written to AWS

<to_id>IRPT_DASHBD.TO-DB-i-9</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~309</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>122</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_118_20261015.md` ADDENDUM 2 @b3e3124d72 (msg 8455): "The probe comes first: `~I2`'s 2-call probe, a WORLD read with LOCAL output. It measures the series length and the call time for one household from inception to date, Daily. The backfill's request and time bound comes from that measurement, not from an estimate." | **Rows:** IRPT_DASHBD-D2-W309-S<k> | **Decomp cell:** `DB-i-9` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md` section 8; this issuance is B-IN round 122, on the round-118 addendum 2, not on a new CTO analysis) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-309`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~309/`. Never push. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: the raw Orion responses are client data and stay in your private folder `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~309/` (create it); in the repo, a row or your report put counts, verdict words, digests and timings only: never an account number, a household or client id, a name, a date or a figure (a return, a value, a fee); a household or an account is named only by the sha256 (hex, utf-8) of its id as a string, and a start date only as the sha256 of its ISO string.

**Why.** The Scope account feed `~P2` is building (IB-pr-586) asks Scope for ONE day per call from now on, so the account pages' QTD, YTD, last-12-month and since-inception windows would lack history for months. The CTO ruled a one-time history backfill: one Scope call per household from the household's start to date, Daily. Before that run is written, its request, time and size bound must come from a measurement. This probe takes it on two households. It changes nothing.

**Read first (no call yet).** Your template: round 120's tracked script `deliverables/0.9.0_WK_IRPT_DASHBD~308/second_household_probe.py` (the token loader, the inner-scope body from `orion_selected.requests_for(...)`, the pacing, the saved-body pattern; copy what you need; do not edit it) and the checker `deliverables/2.0.0_SA_COO~I2/checks/r122/p122_hist.py` (it defines every rule below; read it), with `r120/p120_second_hh.py` and `r117/p117_scope.py`. **POST the INNER `scope` only (`requests["scope"]`), as `orion_selected.calculate` does.** `requests_for` already requests the compact Daily breakdown (`returnStyle` Daily, cumulative false); `calcGrossOfFees` stays FALSE.

**The cell (`DB-i-9`).**
1. **The two households (the rules; the checker recomputes them).** **A** is round 117's household: the household with 2 or more accounts whose `sha256(str(household_id), utf-8)` hex digest sorts lowest in the private dimension `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~171/ACCOUNT_DIM_DRY_RUN.parquet` (columns `account_id`, `household_id`; keys as strings with no `.0`). **B** is round 120's household: `select(...)` in `checks/r120/p120_second_hh.py` applied to the dimension and the round-119 roster body `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~307/get1_newportfolio_active.json` (a list of rows; the account id key is `id`; the start-date field is `accountStartDate`).
2. **The window.** For each household the window START is the earliest non-null `accountStartDate` (its first 10 characters, an ISO date) among the household's accounts that have a roster row; the END is 2026-10-13. Record the start only as `sha256` of its ISO string (`window_start_sha256`).
3. **The calls: exactly TWO, strictly paced (at least 5 seconds apart), NO retry of any kind.** (1) household A; (2) household B. Any answer 4xx or 5xx stops the cell at once (record it; call 2 is then not made if call 1 failed). The POST timeout is **180 seconds** (a multi-year daily series is larger than the 60 s the live transport allows for a one-day call; say in `basis_words` if a call hit it). Read at most 64 MB of a response: more is recorded as oversize (status and byte count) and the cell stops. Time each call from just before the POST to the end of the body read with a monotonic clock (`elapsed_s`) and record `response_bytes`. The token comes from the estate's own loader exactly as your template does it; NEVER print, log, store or put the token in any file, row or report. The ONLY vendor endpoint is `POST https://api.cloud.orionadvisor.com/api/v1/Reporting/Scope`; no other path, host or principal. Save each 2xx body verbatim as private `hist_A.json` / `hist_B.json`; the record carries its path and sha256.
4. **Per-account measurements (the checker applies these exact rules to your saved bodies).** For each household, for EACH of its accounts, in order of `account_sha256`: `state` is `GROUP_WITH_SERIES` (an Account group whose `perf` is present and which has 1 or more series points, as `groups(...)` in `p117_scope.py`), `GROUP_NO_SERIES` or `NO_GROUP`; `points` the number of numeric `factor` values among the group's descendants (0 for no group); `chain_matches` true iff the product of those factors minus 1 equals the group's `perf` (the summary decimal fraction) within 1e-6; `complete` true iff the account has a roster `accountStartDate` and `points` is within 1 of the number of NYSE trading days from that date to 2026-10-13 inclusive (`lib/trading_calendar.trading_days_between`). The household entry is `{household_sha256, window_start_sha256, accounts: [ {account_sha256, state, points, chain_matches, complete} ]}`.
5. **The verdicts and the bound.** `verdict`: `all_accounts_with_series` true iff every account of every household called has state `GROUP_WITH_SERIES`; `chain_matches_all` true iff every account with a series has `chain_matches`; `series_complete_all` true iff every account with a series is `complete`. `bound`: `households_in_universe` = the number of households of the private dimension that have at least one account with a roster row (id key `id`); `requests` = the same number (one call per household); `seconds_max` = `requests` times the slowest `elapsed_s` of your ok calls (a SERIAL upper bound); `bytes_max` = `requests` times the largest `response_bytes`. A failed call has no entry in `households` and no timing; the bound is then from the ok call only.
6. **The script:** tracked `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~309/scope_history_probe.py`, the only code this cell adds. It holds no AWS write call, names no firm other than Inflection, makes no HTTP call except the Scope POSTs, and never writes the token anywhere.
7. **Record** `SCOPE_HISTORY_PROBE_R122.json` in your folder with exactly: `script` {`file`, `sha256`}; `calls` (in order, each {`household` `A` or `B`, `gross_of_fees_flag` false, `http_status` (0 if no response), `ok`, and for an ok call `elapsed_s`, `response_bytes`, `response_file` {`path`, `sha256`}}); `calls_made` (equals the list length and `reads.vendor_calls`); `token_store_used`; `households` {`A`, `B` as in step 4, only for an ok call}; `verdict`; `bound`; `c_credential` {`verdict` `ACCEPTED` if any call was 2xx, `REFUSED` if every call was 401 or 403, else `REQUEST_REJECTED`; `claim`}; `basis_words` (words, at least 200 characters: the series length per account as counts and how it compares with the trading days since each start; the call times and the byte sizes and whether the longest call came near the 180 s timeout; whether the chained factors reproduced Orion's period return; any account missing or short and the visible reason from its roster nulls; what the bound means (a serial upper bound for one full run) and what it does not (no parallelism assumed, no retry, the rate-limit headroom unmeasured); NO value and NO date); `reads` {`vendor_calls`, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` (the token loads), `s3_reads`}; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits except in a `sha256` value or a `path` or `file` field.

<criterion id="DBI122-1-AC1" cell_refs="DB-i-9"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r122/p122_hist.py" . DBI122-1-AC1</invocation><expect>DBI122-1-AC1 PASS</expect></criterion>
`DBI122-1-AC1` -- the record is complete and carries no identifier; the script is a tracked file hashed as recorded with no AWS write call and no other firm's name; the two households and their window-start hashes equal the checker's recompute; 1 or 2 calls are listed (A then B, no call after a failed one), each `ok` agreeing with its status, each 2xx a private file hashed as recorded whose size equals `response_bytes`; every account's state, points, chain check and completeness equal the checker's recompute from the saved bodies and the roster; the verdict fields, the credential verdict and the universe bound (requests, seconds_max, bytes_max) equal the recount; no write to AWS, no push, no deploy. Base: FAIL (no record).

<expected_criteria>DBI122-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every file under `infra/`, `lib/` and `data/`, the template scripts and every issuer check.
- **The vendor.** POST only, exactly 2 calls, at least 5 s apart, no retry of any kind, the inner-scope body, the session token from the estate's own loader only. CTO ruling msg 8455 under CLAUDE.md "other vendor APIs need no per-use word"; Bloomberg is not involved. A redirect or login page is recorded and not followed.
- **The secret.** Read in-process by the estate's loader and used for the Authorization header only; never printed, logged, written to a file, a row, a message or your report. If the read is refused by IAM, record it and STOP; no other principal, no role assumption.
- **Writes.** The repo files of the grant and your private folder only. No write to AWS, no deploy, no push.
- **Client data.** The raw responses and the roster are client data (private folder only). The repo, rows and report carry counts, verdict words, digests and timings.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A 4xx or 5xx, a timeout, an oversize response, a shape the rules do not cover or a series shorter than expected is a RESULT: record it with its verdict and in `basis_words`; never choose another household or window, never call more than twice, never retry.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W309-S<k>`, with the real current UTC time (`date -u +%FT%TZ`, run at filing; never typed by hand); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~309/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-9.orion-scope-history-probe-series-length-call-time-and-bound.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 8, cell `DB-i-9`.
<owned_cells>DB-i-9</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI122-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~309/IRPT_DASHBD.TO-DB-i-9.orion-scope-history-probe-series-length-call-time-and-bound.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI122-1-AC1` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the calls made and each one's HTTP status, `elapsed_s` and `response_bytes`; `token_store_used`; per household the count of accounts by state and, for accounts with a series, the min and max `points` and whether every one was complete and chained; the three verdict fields; the bound (requests, seconds_max, bytes_max); whether any call came near the 180 s timeout; row ids. No token, no client value, no account or household id, no date.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one read script and private response files; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the cell reads the existing Secrets Manager secret the estate's pull and performance path already use, through the estate's own loader and the worker's existing principal (rounds 117 to 120 loaded it without a refusal); no new principal or grant, and a refusal stops the cell.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI122-1-AC1 FAILS at base (no record), and the checker was fed synthetic history bodies for the two households (a record built from them: PASS; the same record with a wrong time bound: FAIL) before the cut.
</preflight>
