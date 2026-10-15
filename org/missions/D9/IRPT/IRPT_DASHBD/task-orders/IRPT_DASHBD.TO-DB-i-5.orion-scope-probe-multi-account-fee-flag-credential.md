# TO IRPT_DASHBD.TO-DB-i-5 -- the ORION SCOPE PROBE: ONE Inflection household with 2 or more accounts, Orion's Reporting/Scope called with the Account grouping and the fee flag `calcGrossOfFees` false and then true over one window; (a) one Account group per account with a daily series, (b) is the fee flag honoured, (c) is the credential accepted; a vendor READ (at most 4 calls), the raw responses private, nothing written to AWS

<to_id>IRPT_DASHBD.TO-DB-i-5</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~305</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>117</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_117_20261015.md` section 2 ruling 2 and section 3 cell 1 (msg 7985): "a WORLD read, LOCAL output, no write. Egress is open (CLAUDE.md) and Orion is not Bloomberg, so no per-use word is needed. Pace it." | **Rows:** IRPT_DASHBD-D2-W305-S<k> | **Decomp cell:** `DB-i-5` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md` section 4) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-305`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~305/`. Never push. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: the raw Orion responses are client data and stay in your private folder `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~305/` (create it); in the repo, a row or your report put counts, verdict words, hashes and shapes only: never an account number, a household or client id, a name or a figure (a return, a value, a fee); a household is named only by the sha256 (hex, utf-8) of its id.

**Why.** Round 116 found that Orion's `POST /api/v1/Reporting/Scope` returns an account-level return with a daily series (grouping `Account`), that the estate's code only sends it for a household holding exactly ONE account, that gross or net of fees is not stated (the request sends `calcGrossOfFees` false, the adapter records the fee basis UNKNOWN), and that nobody has shown the estate's session credential is accepted on Scope in a call you can read. The CTO ruled that ONE probe settles all three. This cell is that probe. It changes nothing.

**What to read first (no call yet).** `infra/aws/lambda/investor-reporting/performance/orion_selected.py` (`requests_for(mapping, canonical_account, start, end)` builds the Scope body; `PERFORMANCE_OPTION["calcGrossOfFees"]` is the fee flag; the dict it returns is `{"scope": scope}` and the flag sits at `body["scope"]["calculations"][0]["contextChange"]["performanceOption"]["calcGrossOfFees"]`; check that path against the dict before you change it), `orion_live.py` (`orion_session_jwt()` and `OrionTransport.request`: the URL is `tenants.route_for(tenants._LEGACY_SHORT_ID["INF"]).url("scope")`, headers `Accept` and `Content-Type: application/json`, `Authorization: Session <token>`, no redirects, 60 s timeout), `orion_adapter.py` (the response node types), `orion_account_mapping.py` and `infra/aws/lambda/inf-pipeline/inf-performance-daily/jwt_freshness.py` (the secret name and the S3 copy of the same token), and the row/receipt `IRPT_BCKEND-S143` (the 2026-09-26 entity probe: the estate has called Scope live before; find it with `comp-find`).

**The cell (`DB-i-5`).**
1. **The household (a rule, so the checker recomputes it).** From the private dimension `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~171/ACCOUNT_DIM_DRY_RUN.parquet` (columns `account_id`, `household_id`), take the households with 2 or more accounts; the chosen one is the household whose `sha256(str(household_id), utf-8)` hex digest sorts lowest (plain string order). Its account ids are `accounts_in_household` of them. Keys are formatted as a string with no `.0` (a float 12.0 is `"12"`).
2. **The window and the body.** Window: start 2026-10-01, end 2026-10-13. Build the body with the module's own `requests_for` from a mapping dict `{"firm_id": tenants._CANONICAL_INF, "canonical_account_id": <any string>, "vendor_account_id": <int of the first account id>, "vendor_household_id": <int of the household id>}` (add `infra/aws/lambda/investor-reporting/performance` to `sys.path`; import offline, no vendor call at import). The Orion household id is the dimension's `household_id` unless `orion_account_mapping.py` shows a different mapping rule; say which in `basis_words`. For the second call change ONLY `calcGrossOfFees` to true.
**AMENDMENT 1 (issuer 2.0.0_SA_COO~I2, on your row `IRPT_DASHBD-D2-W305-S1`; this is the issuer's error, not yours).** The order told you to build the body with `requests_for` and never said which part to POST. `requests_for` returns `{"scope": scope}`; the estate's transport posts the INNER `scope` (`orion_selected.calculate`, line 147: `transport.request("scope", route.url("scope"), requests["scope"])`). **POST `requests["scope"]`, the inner dict, and nothing else.** The fee flag for that inner dict sits at `scope["calculations"][0]["contextChange"]["performanceOption"]["calcGrossOfFees"]` (check the path on the dict). Your two earlier calls (both HTTP 400, a body the estate does not send) stay in the record as calls 1 and 2 with their statuses and `ok` false; **the cap of FOUR calls is for the whole cell, so you have TWO calls left: flag false, then flag true, at least 5 seconds apart, and no retry of any kind.** If either answers 4xx or 5xx, record it and STOP. Update `SCOPE_PROBE_R117.json` so `calls` lists all four calls in order, `calls_made` and `reads.vendor_calls` are 4, `reads.secret_reads` counts every token load; rerun the criterion. **Verdict (c) is amended:** `ACCEPTED` if the flag-false call returned a 2xx; `REFUSED` only if EVERY call was answered 401 or 403; `REQUEST_REJECTED` if every call was non-2xx and not all 401 or 403 (a rejected body says nothing about the credential); else `NOT_RUN`. The amended checker is already on your branch. Reopen the proof instance and flip the order to `complete` again only when the criterion reads PASS. Your row `W305-S1` is ruled here; do not file another for it.

3. **The calls: at most FOUR in total, strictly paced.** Order: (1) flag false; (2) flag true. Wait at least 5 seconds between calls. A timeout or a 5xx may be retried ONCE per flag after 15 seconds; a 4xx is not retried. You send the POST yourself with `urllib.request` (the same URL, headers, no redirects and 60 s timeout as `OrionTransport`; you may import its `orion_session_jwt` and the `jwt_freshness` helpers). The token comes from the estate's own loader (Secrets Manager `orion/jwt/current`, named by `jwt_freshness.SM_SECRET_ID`); if that read is refused for this principal, you may use the S3 copy of the token ONLY by the route `jwt_freshness.py` documents for it. If neither works, or any call is answered 401 or 403, record it (that IS result (c)) and STOP calling. NEVER print, log, store or put the token in any file, row or report. The ONLY vendor endpoint you may call is the Scope URL above; no other path, no other host, no other principal, no role assumption.
4. **Save each 2xx response body** verbatim as a private file `scope_<false|true>.json` in your private folder; the record carries its path and sha256. A non-2xx response is recorded by status only (no body saved).
5. **The three verdicts, by these exact rules (the checker applies them to your saved bodies).**
   - **Groups:** every dict with `$type` equal `calculated-group` and `grouping` equal `Account`; its id is `str(groupEntityId)`; its `perf` is the first numeric `performance` of a descendant of `$type` `calculated-performance`; its `points` is the count of descendants carrying a numeric `factor`; its `fee` is the sum of numeric `feeAmount` over its descendants; its `startv` is the numeric `value` of the first descendant of `$type` `calculated-activity` whose `id` is `startValue`.
   - **(a) `a_multi_account.verdict`:** `ONE_GROUP_PER_ACCOUNT` if the set of group ids from the flag-false response equals the household's account ids and every group has a `perf` and `points` of 1 or more; `FEWER_GROUPS` if the ids are a proper subset; otherwise `OTHER_GROUPS`; `REFUSED` if every call was refused; `NOT_RUN` if no flag-false 2xx response exists and not every call was refused. Record `account_groups_returned` (the number of groups) and `groups_with_daily_series` (groups with `points` of 1 or more).
   - **(b) `b_fee_basis.verdict`:** over the accounts present in both responses with a `perf` in each: `IGNORED` if every account's `perf` is equal within 1e-12 between the false and the true response; else, over the accounts with `fee` above 0, `NET_WHEN_FALSE` if for every one the observed gap `obs = perf_true - perf_false` is 0 or more and `|obs - fee / startv| <= max(1e-4, 0.25 * fee / startv)` and there is at least one such account; else `DIFFERENT_UNTIED`; `NOT_RUN` if both responses do not exist. Record `accounts_compared` and `accounts_with_fee`.
   - **(c) `c_credential.verdict`:** `ACCEPTED` if the flag-false call returned a 2xx; `REFUSED` if every call was refused (non-2xx); else `NOT_RUN`.
   Each verdict has a `claim` word: `measured` (you computed it from a response you saw) or `absent` (not run).
6. **The script:** tracked `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~305/scope_probe.py`, the only code this cell adds. It holds no AWS write call, names no firm other than Inflection, makes no HTTP call except the Scope POST, and never writes the token anywhere.
7. **Record** `SCOPE_PROBE_R117.json` in your folder with exactly: `script` {`file` (repo-relative), `sha256`}; `household_sha256`; `accounts_in_household` (integer); `window` {`start`, `end`}; `calls` (a list in call order, each {`gross_of_fees_flag` (false or true), `http_status` (integer; 0 if no HTTP response), `ok` (true exactly when the status is 200 to 299), and for an ok call `response_file` {`path`, `sha256`}}); `calls_made` (equals the list length); `token_store_used` (`secretsmanager`, `s3_copy` or `none`); `a_multi_account`; `b_fee_basis`; `c_credential`; `basis_words` (words, at least 120 characters: the window; how the Orion household id was mapped; the shape of the response in node-type words; whether the one-account limit is the code's or the vendor's; the fee verdict in words; the pace you kept; anything the response did not hold; NO value); `reads` {`vendor_calls` (equals `calls_made`), `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` (integer: the number of times you loaded the token), `s3_reads` (integer)}; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits except in a `sha256` value or a `path` or `file` field.

<criterion id="DBI117-1-AC1" cell_refs="DB-i-5"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r117/p117_scope.py" . DBI117-1-AC1</invocation><expect>DBI117-1-AC1 PASS</expect></criterion>
`DBI117-1-AC1` -- the record is complete and carries no identifier; the script is a tracked file hashed as recorded, with no AWS write call and no other firm's name; the household equals the checker's recompute from the private dimension; 1 to 4 calls are listed with `calls_made` and `vendor_calls` equal to the count, each `ok` agreeing with its status, each 2xx response a private file hashed as recorded; `token_store_used` is within its enum and `secret_reads` is an integer within the call cap; the three verdicts and their counts equal the checker's recount from the saved response bodies by the rules above; no write to AWS, no push, no deploy. Base: FAIL (no record).

<expected_criteria>DBI117-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every file under `infra/`, `lib/` and `data/`, the contract and every issuer check.
- **The vendor.** ONE host (`api.cloud.orionadvisor.com`), ONE path (`/api/v1/Reporting/Scope`), POST only, at most 4 calls, paced as above, the session token from the estate's own loader only. This is the CTO's ruling (msg 7985) under CLAUDE.md "other vendor APIs need no per-use word"; Bloomberg is not involved. A response that asks for anything else (a redirect, a login page) is recorded and not followed.
- **The secret.** Read in-process by the estate's loader and used for the Authorization header; never printed, logged, written to a file, a row, a message or your report. If the read is refused by IAM for this principal, record it and STOP: no other principal, no role assumption, no key lookup elsewhere.
- **Writes.** The repo files of the grant and your private folder only. No write to AWS of any kind, no deploy, no push.
- **Client data.** The raw responses are client data (private folder only). The repo, rows and report carry counts, verdict words, hashes and shapes.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A refused credential, a response of a shape the rules do not cover, or a household the vendor does not know is a RESULT: record it with its verdict (`REFUSED`, `OTHER_GROUPS`, `NOT_RUN`) and in `basis_words`; never choose another household to get a better answer, and never call more than the cap.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W305-S<k>`, with the real current UTC time (`date -u +%FT%TZ`, run at filing; never typed by hand); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~305/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-5.orion-scope-probe-multi-account-fee-flag-credential.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 4, cell `DB-i-5`.
<owned_cells>DB-i-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI117-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~305/IRPT_DASHBD.TO-DB-i-5.orion-scope-probe-multi-account-fee-flag-credential.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI117-1-AC1` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the number of calls made and each call's HTTP status; `token_store_used`; verdicts (a), (b) and (c) with their counts (`accounts_in_household`, `account_groups_returned`, `groups_with_daily_series`, `accounts_compared`, `accounts_with_fee`); one line on whether the one-account limit is the code's or the vendor's; the pace kept; row ids. No token, no client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one read script and private response files; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the cell reads the existing Secrets Manager secret the estate's performance path already uses, through the estate's own loader and the worker's existing principal; no new principal or grant, and a refusal stops the cell.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI117-1-AC1 FAILS at base (no record), and the checker was fed synthetic responses (a net-when-false pair: PASS; the same record with a wrong fee verdict: FAIL) before the cut.
</preflight>
