# TO IRPT_DASHBD.TO-DB-i-7 -- the ORION ACCOUNT-RECORD READ: Orion's own record for the account Scope leaves out, against the series-less account and one present account of the round-117 household, over the endpoint the estate's pull already uses for accounts (at most 3 paced GETs, read-only); every performance-relevant field compared, the fields that differ named as verdict words only; raw responses private, nothing written to AWS

<to_id>IRPT_DASHBD.TO-DB-i-7</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~307</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>119</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_119_20261015.md` section 'Rulings' item 2 and 'Round-119 cell' (msg 8048): "One cell (`~I2`, WORLD read, cap 3 GETs, paced, no retry): read Orion's own account record for the missing account and for one account that does appear, over the endpoint the estate's pull already uses for accounts. Compare every performance-relevant flag ... Record the flag names and which ones differ, as verdict words only." No vendor contact is made first. | **Rows:** IRPT_DASHBD-D2-W307-S<k> | **Decomp cell:** `DB-i-7` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md` section 6) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-307`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~307/`. Never push. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: the raw Orion responses are client data and stay in your private folder `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~307/` (create it); in the repo, a row or your report put counts, verdict words, digests and FIELD NAMES only: never an account number, a household or client id, a name, a date or a figure (a value, a balance, a return); an account is named only by the sha256 (hex, utf-8) of its id as a string. If a response carries accounts of any other firm, record only the row count, never any content.

**Why.** Round 118 found that over Q3 and YTD, Orion's `Reporting/Scope` returns no Account group for ONE of the five accounts of the round-117 household although it holds positions on 87 days of the quarter, and a group with no series (Q3) for another (the series appears over YTD); the other three are fine, and all five share one account type and registration category. The CTO wants to know, before anyone contacts Orion, whether Orion's own account record for the missing account carries a flag that differs from a present account's (an exclusion or inclusion flag, a status, inception or end dates, a model or managed flag). This cell reads the records and names the differing field names. It changes nothing.

**Read first (no call yet).** `infra/aws/lambda/inf-pipeline/inf-accounts-v2-daily/pull_inflection_new_portfolio.py` (the estate's account pull: `BASE` the API host, `headers(jwt)`, `pull_new_portfolio(jwt, created_date_start, top)` = `GET {BASE}/api/v1/Portfolio/Accounts/NewPortfolio` with params `$top` 50000, `createdDateStart` `01/01/1970`, `isActive` `true`, `newAccountFilter` empty; and the second function that pulls `GET {BASE}/api/v1/Portfolio/Accounts`, the base roster: read its exact params), `infra/aws/lambda/inf-pipeline/inf-performance-daily/jwt_freshness.py` (the token's secret name and the S3 copy) and your template, round 118's tracked script `deliverables/0.9.0_WK_IRPT_DASHBD~306/scope_probe2.py` (the token loader, the pacing, the saved-body pattern; copy what you need; do not edit it), plus the checker `deliverables/2.0.0_SA_COO~I2/checks/r119/p119_acct.py` and its record `deliverables/0.9.0_WK_IRPT_DASHBD~306/SCOPE_PROBE2_R118.json` (they define everything below; read them).

**The cell (`DB-i-7`).**
1. **The three accounts (roles).** From round 118's record `coverage.q3`: `missing` is the account whose digest is in `missing_account_sha256` (no Scope group); `series_less` is the one in `series_less_account_sha256` (a group, no series, in Q3); `present` is the account, among the household's accounts, with the lowest `sha256(str(account_id), utf-8)` hex digest that has a return and a daily series in the flag-false Q3 body `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~306/scope_q3_false.json` (use `groups(...)` from `checks/r117/p117_scope.py`). Map digests to account ids through the private dimension `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~171/ACCOUNT_DIM_DRY_RUN.parquet` (columns `account_id`, `household_id`; keys as strings with no `.0`) for the household whose digest equals round 117's `household_sha256`.
2. **The GETs: at most THREE, strictly paced (at least 5 seconds apart), NO retry of any kind; any 4xx or 5xx stops the cell at once (record it).** The token comes from the estate's own loader exactly as your template does it; NEVER print, log, store or put the token in any file, row or report. The ONLY vendor host is the API host in `BASE`; the ONLY paths are the two named here.
   - **GET 1 (`kind` `newportfolio_active`):** `GET {BASE}/api/v1/Portfolio/Accounts/NewPortfolio` with the pull's own params and headers exactly (`isActive` `true`).
   - **GET 2 (`kind` `newportfolio_inactive`), ONLY if the `missing` account was NOT found in GET 1:** the same request with `isActive` `false` and nothing else changed.
   - **GET 3 (`kind` `accounts_roster`), ONLY if the `missing` account was still NOT found after GET 2:** `GET {BASE}/api/v1/Portfolio/Accounts` with the params the pull uses for that call.
   - **No GET follows a GET that found the `missing` account.** Save each 2xx body verbatim as a private file `get<n>_<kind>.json`; the record carries its path and sha256. A non-2xx is recorded by status only.
3. **Find the records.** For each 2xx body, the rows are the list the body is (or holds). Read the row field names and choose the one that holds the account id (`account_id_key`; state it in `basis_words`); a row is a role's when `str(row[account_id_key])` (no `.0`) equals the account id. Record per GET `presence` {`missing`, `series_less`, `present`} (booleans) and `rows` (the row count). A role's record is the row from the FIRST GET that holds it.
4. **The comparisons (the checker applies these exact rules to your saved bodies).** For `missing` against `present`, and `series_less` against `present`: flatten each record to field paths (nested dict keys joined with `.`, list items with `[i]`); `differing_paths_total` is the number of paths (in either record) whose value differs or is present in only one; `relevant_paths` is the sorted list of differing paths that match, case-insensitively, the regular expression `perf|report|exclud|includ|status|inception|start|end|clos|terminat|activ|model|managed|billing|composite|benchmark|hidden|suppress|skip`; `exclusion_type_paths` is the sorted subset of those that match `exclud|includ|suppress|hidden|skip|notreport|noreport|reportable`; `bool_values` maps each relevant differing path whose two values are both booleans or null to `[missing_or_series_less_value, present_value]`; `verdict` is `FLAG_DIFFERS` if `exclusion_type_paths` is not empty, else `STATUS_OR_DATE_DIFFERS` if `relevant_paths` is not empty, else `NONE_VISIBLE`; a comparison whose role record was not found reads `NOT_AVAILABLE` with the other fields empty or zero as the checker's rule gives. Field NAMES and booleans are recorded; a date, a string or a number VALUE never is.
5. **The script:** tracked `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~307/account_record_read.py`, the only code this cell adds. It holds no AWS write call, names no firm other than Inflection, makes no HTTP call except the GETs above, and never writes the token anywhere.
6. **Record** `ACCOUNT_RECORD_READ_R119.json` in your folder with exactly: `script` {`file`, `sha256`}; `household_sha256`; `roles_sha256` {`missing_sha256`, `series_less_sha256`, `present_sha256`}; `gets` (in order, each {`kind`, `http_status` (0 if no response), `ok`, `rows` (integer), `account_id_key`, `presence` {`missing`, `series_less`, `present`}, `response_file` {`path`, `sha256`} for an ok get}; a failed get carries only `kind`, `http_status`, `ok`); `gets_made` (the list length; equals `reads.vendor_calls`); `comparisons` {`missing_vs_present`, `series_less_vs_present`, each {`differing_paths_total`, `relevant_paths`, `exclusion_type_paths`, `bool_values`, `verdict`}}; `missing_account_found` (boolean); `c_credential` {`verdict` `ACCEPTED` if any get was 2xx, `REFUSED` if every get was 401 or 403, else `REQUEST_REJECTED`; `claim`}; `basis_words` (words, at least 160 characters: which GETs ran and why the later ones did or did not; the id key; whether the missing account was found and in which; which differing field names are exclusion-type and what the booleans read; whether a flag explains the omission, in words; what the records did not show; NO value); `reads` {`vendor_calls`, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` (the token loads), `s3_reads`}; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits except in a `sha256` value or a `path` or `file` field.

<criterion id="DBI119-1-AC1" cell_refs="DB-i-7"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r119/p119_acct.py" . DBI119-1-AC1</invocation><expect>DBI119-1-AC1 PASS</expect></criterion>
`DBI119-1-AC1` -- the record is complete and carries no identifier; the script is a tracked file hashed as recorded with no AWS write call and no other firm's name; the household and the three role digests equal the checker's recompute from round 118's record and the private Q3 body; 1 to 3 gets are listed in the order above, each a 2xx saved as a private file hashed as recorded (a failed get only as the last), `gets_made` and `vendor_calls` equal to the count, and a later get only while the missing account was still not found; each get's presence flags equal the checker's recount from the saved body with the recorded id key; each comparison (path counts, relevant and exclusion-type path lists, boolean values, verdict) equals the checker's recompute from the records found in the saved bodies; `missing_account_found` and the credential verdict equal the recount; no write to AWS, no push, no deploy. Base: FAIL (no record).

<expected_criteria>DBI119-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every file under `infra/`, `lib/` and `data/`, the template script and every issuer check.
- **The vendor.** GET only, at most 3, at least 5 s apart, no retry of any kind, the session token from the estate's own loader only, exactly the two paths named; a read, not a vendor contact. CTO ruling msg 8048 under CLAUDE.md "other vendor APIs need no per-use word"; Bloomberg is not involved. A redirect or login page is recorded and not followed.
- **The secret.** Read in-process by the estate's loader and used for the Authorization header only; never printed, logged, written to a file, a row, a message or your report. If the read is refused by IAM, record it and STOP; no other principal, no role assumption.
- **Writes.** The repo files of the grant and your private folder only. No write to AWS, no deploy, no push.
- **Client data.** The raw responses (a whole-firm roster) are client data: private folder only, never committed. The repo, rows and report carry counts, verdict words, digests and field names.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A 4xx or 5xx, a missing account that no GET finds, or a record that shows nothing different is a RESULT: record it with its verdict and in `basis_words`; never call more than the cap, and never read another account's record to get a better answer.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W307-S<k>`, with the real current UTC time (`date -u +%FT%TZ`, run at filing; never typed by hand); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~307/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-7.orion-account-record-read-missing-vs-present-account-flags.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 6, cell `DB-i-7`.
<owned_cells>DB-i-7</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI119-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~307/IRPT_DASHBD.TO-DB-i-7.orion-account-record-read-missing-vs-present-account-flags.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI119-1-AC1` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the GETs made and each one's HTTP status and row count; the account id key; per GET which roles were present; whether the missing account was found, and in which GET; per comparison the verdict, `differing_paths_total`, the exclusion-type field names and the boolean values; the pace; row ids. No token, no client value, no account or household id.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one read script and private response files; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the cell reads the existing Secrets Manager secret the estate's pull and performance path already use, through the estate's own loader and the worker's existing principal (rounds 117 and 118 loaded it without a refusal); no new principal or grant, and a refusal stops the cell.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI119-1-AC1 FAILS at base (no record), and the checker was fed synthetic roster bodies (GET 1 without the missing account, GET 2 with it and an exclusion flag: PASS; the same record with a follow-on GET after the account was found: FAIL) before the cut.
</preflight>
