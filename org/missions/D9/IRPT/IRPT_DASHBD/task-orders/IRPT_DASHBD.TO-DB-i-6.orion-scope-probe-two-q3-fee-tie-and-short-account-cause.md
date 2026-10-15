# TO IRPT_DASHBD.TO-DB-i-6 -- the SECOND ORION SCOPE PROBE: the SAME five-account household as round 117, the quarter that ended 2026-09-30, the fee flag false then true, the INNER scope body (at most 4 calls, a second pair only if the Q3 pair holds no fee): (i) do the missing account and the series-less group appear over the longer span, (ii) does the true-minus-false gap tie to the summed feeAmount, (iii) the cause class of each short account; a vendor READ, raw responses private, nothing written to AWS

<to_id>IRPT_DASHBD.TO-DB-i-6</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~306</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>118</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_118_20261015.md` section 2 ruling 2 and section 3 cell 1 (msg 8034): "a WORLD read, cap 4 calls, paced, no retry: the same household over the quarter that ended 2026-09-30, with the flag false then true ... Counts and verdict words only. The order states the inner-`scope` body (the round-117 lesson)." | **Rows:** IRPT_DASHBD-D2-W306-S<k> | **Decomp cell:** `DB-i-6` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md` section 5) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-306`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~306/`. Never push. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: the raw Orion responses are client data and stay in your private folder `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~306/` (create it); in the repo, a row or your report put counts, verdict words, hashes and categories only: never an account number, a household or client id, a name or a figure (a return, a value, a fee); a household or an account is named only by the sha256 (hex, utf-8) of its id as a string.

**Why.** Round 117's probe (record `deliverables/0.9.0_WK_IRPT_DASHBD~305/SCOPE_PROBE_R117.json`, script `scope_probe.py` in that folder, tracked) showed Orion's `POST /api/v1/Reporting/Scope` accepts the estate's credential and returns Account groups for a five-account household, but over 2026-10-01 to 2026-10-13 it returned 4 groups for 5 accounts, only 3 with a return and a daily series, although all five accounts hold positions on all 13 days; and the fee flag `calcGrossOfFees` raised the return on 3 of 3 accounts while `feeAmount` summed to zero (no fee fell in that window). This probe repeats it over the quarter that ended 2026-09-30, to see whether the short accounts appear and whether a fee gap ties. It changes nothing.

**What to read first (no call yet).** `deliverables/0.9.0_WK_IRPT_DASHBD~305/scope_probe.py` (your template: copy what you need into your own script; it loads the token, builds the body, paces the calls and saves the bodies; do not edit it), its record `SCOPE_PROBE_R117.json`, and the checker `deliverables/2.0.0_SA_COO~I2/checks/r118/p118_scope2.py` plus `r117/p117_scope.py` (they define every verdict below; read them). The round-117 lesson: `orion_selected.requests_for(...)` returns `{"scope": scope}`; **POST the INNER `scope` only (`requests["scope"]`), exactly as `orion_selected.calculate` does at line 147.** The fee flag for the inner dict sits at `scope["calculations"][0]["contextChange"]["performanceOption"]["calcGrossOfFees"]` (check the path on the dict).

**The cell (`DB-i-6`).**
1. **The household** is round 117's: the household with 2 or more accounts whose `sha256(str(household_id), utf-8)` hex digest sorts lowest in the private dimension `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~171/ACCOUNT_DIM_DRY_RUN.parquet` (columns `account_id`, `household_id`; keys as strings with no `.0`). Its digest must equal round 117's `household_sha256`. Use the same Orion household mapping as your template.
2. **Windows.** `q3`: start 2026-07-01, end 2026-09-30. `ytd` (only if needed, see step 3): start 2026-01-01, end 2026-09-30.
3. **The calls: at most FOUR in total, strictly paced, NO retry of any kind.** Order: (1) `q3`, flag false; (2) `q3`, flag true; wait at least 5 seconds between calls. After call 2, run the fee check on the two bodies (step 5 rule (b)). **Only if the `q3` pair compared NO account with a fee above 0** (`accounts_with_fee` 0, or a pair that did not both return 2xx is NOT a reason: stop instead), make calls (3) `ytd`, flag false and (4) `ytd`, flag true. Any answer 4xx or 5xx stops the cell at once (record it). The token comes from the estate's own loader exactly as your template does it (Secrets Manager `orion/jwt/current`, the S3 copy only by the route `jwt_freshness.py` documents); NEVER print, log, store or put the token in any file, row or report. The ONLY vendor endpoint is `POST https://api.cloud.orionadvisor.com/api/v1/Reporting/Scope`; no other path, host or principal.
4. **Save each 2xx body** verbatim as a private file `scope_<q3|ytd>_<false|true>.json` in your private folder; the record carries its path and sha256. A non-2xx response is recorded by status only.
5. **The verdicts, by these exact rules (the checker applies them to your saved bodies).**
   - **Groups, per body:** as in `p117_scope.py` `groups`: every dict of `$type` `calculated-group` with `grouping` `Account`; id `str(groupEntityId)`; `perf` the first numeric `performance` of a descendant `calculated-performance`; `points` the count of descendants with a numeric `factor`; `fee` the sum of numeric `feeAmount` over descendants; `startv` the numeric `value` of the first `calculated-activity` descendant with `id` `startValue`.
   - **(i) coverage, per window run, from the flag-false body:** `account_groups_returned`; `groups_with_series` (groups with a `perf` and `points` of 1 or more); `missing_account_sha256` (the household's accounts with NO group, as digests); `series_less_account_sha256` (accounts with a group but no `perf` or `points` under 1, as digests); `verdict` `ALL_COVERED` if both lists are empty, else `SHORT`; a window with no flag-false 2xx reads `NOT_RUN`.
   - **(ii) `b_fee_basis`, from ONE pair:** `pair` is `q3`, or `ytd` when a ytd pair exists; `verdict` is `IGNORED` if every compared account's `perf` is equal (within 1e-12) between the false and true bodies; else over the accounts with `fee` above 0 in the false body: `NET_WHEN_FALSE` if for every one `obs = perf_true - perf_false` is 0 or more and `|obs - fee / startv| <= max(1e-4, 0.25 * fee / startv)` (and there is at least one); `NO_FEE_IN_WINDOW` if the returns differ and no compared account has a fee above 0; else `DIFFERENT_UNTIED`; `NOT_RUN` if no pair exists. Record `accounts_compared` and `accounts_with_fee`.
   - **(c) `c_credential.verdict`:** `ACCEPTED` if a flag-false call returned a 2xx; `REFUSED` only if EVERY call was answered 401 or 403; `REQUEST_REJECTED` if every call was non-2xx and not all 401 or 403; else `NOT_RUN`.
   Each verdict has a `claim` word: `measured` or `absent` (not run).
6. **(iii) the short accounts (the `q3` window's short list, missing plus series-less).** For each, record: `account_sha256`; `role` (`NO_GROUP` or `GROUP_NO_SERIES`); `position_days_in_window` (the number of rows of the private cache `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~174/work/positions_daily_cache.parquet`, columns `acc`, `date`, for that account with `date` from 2026-07-01 to 2026-09-30 inclusive; the checker recounts it); `account_type_class` and `registration_class`: CATEGORIES only (at most 40 characters, from the newest `fact_positions` partition of `s3://opal-data-assets/orion/inflection/silver/fact_positions/` read through the GET-only reader `InflectionSilverReader` in `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_dim.py`: read the partition's column list, take a column that holds an account TYPE or a REGISTRATION CODE class (a short coded category), and NEVER a column that holds a person's or entity's name or an account number; if no such column exists the value is `ABSENT`); `cause_class` (`NO_POSITIONS_IN_WINDOW` if `position_days_in_window` is 0; `ACCOUNT_CLASS_EXCLUDED_BY_VENDOR` if the account has positions in the window AND its (type, registration) class differs from every account of the household that DID return a series, so a class-based exclusion is the visible pattern; else `NOT_DETERMINED`); `claim` (`inferred`); `words` (one or two sentences, no value). If the `q3` window returned no short account, `short_accounts` is the empty list.
7. **The script:** tracked `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~306/scope_probe2.py`, the only code this cell adds. It holds no AWS write call, names no firm other than Inflection, makes no HTTP call except the Scope POST, and never writes the token anywhere.
8. **Record** `SCOPE_PROBE2_R118.json` in your folder with exactly: `script` {`file`, `sha256`}; `household_sha256`; `accounts_in_household`; `windows` {`q3` {`start`, `end`} and, only when run, `ytd` {`start`, `end`}}; `calls` (in order, each {`window`, `gross_of_fees_flag`, `http_status` (0 if no HTTP response), `ok`, and for an ok call `response_file` {`path`, `sha256`}}); `calls_made` (equals the list length; 2 without a ytd pair, 4 with one); `token_store_used`; `coverage` {one entry per window run: {`account_groups_returned`, `groups_with_series`, `missing_account_sha256`, `series_less_account_sha256`, `verdict`}}; `b_fee_basis` {`verdict`, `pair`, `accounts_compared`, `accounts_with_fee`, `claim`}; `c_credential` {`verdict`, `claim`}; `short_accounts`; `basis_words` (words, at least 160 characters: the windows and pairs run and why; how the Orion household id was mapped; whether the short accounts appeared over the quarter; the fee verdict in words, and whether false is shown to be net; the cause class read and its evidence in words; the pace; what the response did not hold; NO value); `reads` {`vendor_calls` (equals `calls_made`), `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` (integer: the token loads), `s3_reads` (integer)}; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits except in a `sha256` value or a `path` or `file` field.

<criterion id="DBI118-1-AC1" cell_refs="DB-i-6"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r118/p118_scope2.py" . DBI118-1-AC1</invocation><expect>DBI118-1-AC1 PASS</expect></criterion>
`DBI118-1-AC1` -- the record is complete and carries no identifier; the script is a tracked file hashed as recorded with no AWS write call and no other firm's name; the household equals round 117's rule; 1 to 4 calls are listed (a ytd pair only after a `q3` pair that compared no account with a fee), each `ok` agreeing with its status, each 2xx response a private file hashed as recorded; the credential verdict, each window's coverage counts and short-account digests, the fee verdict with its pair and counts, the short-account list with its roles and `position_days_in_window` all equal the checker's recount from the saved bodies and the cache; the category fields are short strings; no write to AWS, no push, no deploy. Base: FAIL (no record).

<expected_criteria>DBI118-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every file under `infra/`, `lib/` and `data/`, the template script and every issuer check.
- **The vendor.** ONE host, ONE path, POST only, at most 4 calls in total, at least 5 s apart, no retry of any kind, the inner-scope body, the session token from the estate's own loader only. CTO ruling msg 8034 under CLAUDE.md "other vendor APIs need no per-use word"; Bloomberg is not involved. A redirect or login page is recorded and not followed.
- **The secret.** Read in-process by the estate's loader and used for the Authorization header only; never printed, logged, written to a file, a row, a message or your report. If the read is refused by IAM, record it and STOP; no other principal, no role assumption.
- **Reads.** Repo files; the private cache and dimension; the newest `fact_positions` partition through the GET-only reader (a category column only; never a name or number).
- **Writes.** The repo files of the grant and your private folder only. No write to AWS, no deploy, no push.
- **Client data.** The raw responses and the cache are client data (private folder only). The repo, rows and report carry counts, verdict words, digests and categories.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A refused credential, a 4xx or 5xx, a shape the rules do not cover, or a short account the vendor omits is a RESULT: record it with its verdict and in `basis_words`; never choose another household or window to get a better answer, and never call more than the cap.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W306-S<k>`, with the real current UTC time (`date -u +%FT%TZ`, run at filing; never typed by hand); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~306/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-6.orion-scope-probe-two-q3-fee-tie-and-short-account-cause.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 5, cell `DB-i-6`.
<owned_cells>DB-i-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI118-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~306/IRPT_DASHBD.TO-DB-i-6.orion-scope-probe-two-q3-fee-tie-and-short-account-cause.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI118-1-AC1` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the calls made and each call's HTTP status; `token_store_used`; per window run the coverage counts (`account_groups_returned`, `groups_with_series`, missing and series-less counts); the fee verdict with its pair and counts and one line on whether false is shown to be net; each short account's role, `position_days_in_window` and `cause_class`; the pace; row ids. No token, no client value, no account or household id.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one read script and private response files; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the cell reads the existing Secrets Manager secret the estate's performance path already uses, through the estate's own loader and the worker's existing principal (round 117 loaded it without a refusal); no new principal or grant, and a refusal stops the cell.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI118-1-AC1 FAILS at base (no record), and the checker was fed synthetic Q3 responses (a record built from them: PASS; the same record with a wrong position-days count: FAIL) before the cut.
</preflight>
