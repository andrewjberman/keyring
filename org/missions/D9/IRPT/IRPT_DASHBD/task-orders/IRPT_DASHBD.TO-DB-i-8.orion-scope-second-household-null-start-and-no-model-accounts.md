# TO IRPT_DASHBD.TO-DB-i-8 -- the SECOND-HOUSEHOLD SCOPE PROBE: ONE other Inflection household chosen by a rule the checker recomputes (it holds an account with a NULL accountStartDate, an account with a start date and NO modelName, and no account outside Orion's active roster); Orion's Reporting/Scope called twice, inner-scope body, calcGrossOfFees false: Q3 and YTD; does the null-start account have no Scope group, is the no-model account short, is every other account present with a series; a vendor READ (2 calls), raw responses private, nothing written to AWS

<to_id>IRPT_DASHBD.TO-DB-i-8</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~308</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>120</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_120_20261015.md` ruling 2 and 'Round-120 cell' (msg 8081): "The second-household probe runs (`~I2`, a WORLD read, cap 2 Scope calls, paced, no retry, inner-scope body). It covers one household that holds one account with a null start date and one with no model. Both are chosen by a rule the checker recomputes." | **Rows:** IRPT_DASHBD-D2-W308-S<k> | **Decomp cell:** `DB-i-8` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md` section 7) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-308`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~308/`. Never push. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: the raw Orion responses are client data and stay in your private folder `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~308/` (create it); in the repo, a row or your report put counts, verdict words and digests only: never an account number, a household or client id, a name, a date or a figure; a household or an account is named only by the sha256 (hex, utf-8) of its id as a string.

**Why.** Round 119 found that the one Inflection account Orion's `Reporting/Scope` omits has, in Orion's own account record, a null `accountStartDate` and `accountStartValue` and no `modelName`, while the account that got a group but no series over Q3 has a start date and no model; the account with all three is fine. That is an inference from one household. This probe tests it on a second household chosen by a rule fixed BEFORE any call. **The prediction, written before the call:** the null-start account has NO Scope group in both windows; the no-model account is not `GROUP_WITH_SERIES` in Q3; every other account of the household is `GROUP_WITH_SERIES` in both windows. Report what the data show; whatever happens, do not change the rule or the household.

**Read first (no call yet).** Round 118's tracked script `deliverables/0.9.0_WK_IRPT_DASHBD~306/scope_probe2.py` (your template: the token loader, the inner-scope body, the pacing, the saved-body pattern; copy what you need; do not edit it), round 117's `scope_probe.py` in `~305`, and the checker `deliverables/2.0.0_SA_COO~I2/checks/r120/p120_second_hh.py` (it defines the household rule, the states and every verdict below; read it), with `r117/p117_scope.py` (`groups`, `key_of`). The round-117 lesson stands: `orion_selected.requests_for(...)` returns `{"scope": scope}`; **POST the INNER `scope` only (`requests["scope"]`), as `orion_selected.calculate` does.** The fee flag for the inner dict is `scope["calculations"][0]["contextChange"]["performanceOption"]["calcGrossOfFees"]` and stays FALSE in both calls.

**The cell (`DB-i-8`).**
1. **The household and the two accounts (the rule; the checker recomputes it).** From the private dimension `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~171/ACCOUNT_DIM_DRY_RUN.parquet` (columns `account_id`, `household_id`; keys as strings with no `.0`) and the round-119 roster body `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~307/get1_newportfolio_active.json` (a list of rows; the account id key is `id`): classify each account `NO_START` (a roster row whose `accountStartDate` is null or empty), `NO_MODEL` (a start date, `modelName` null or empty), `FULL`, or `NOT_IN_ROSTER` (no roster row). Candidates are the households OTHER than round 117's (`household_sha256` in `SCOPE_PROBE_R117.json`) with at least one `NO_START`, at least one `NO_MODEL` and NO `NOT_IN_ROSTER` account. The household is the candidate whose `sha256(str(household_id), utf-8)` hex digest sorts lowest; its `NO_START` account and `NO_MODEL` account are the lowest-digest account of each class. Use the Orion household id mapping your template uses.
2. **The calls: exactly TWO, strictly paced (at least 5 seconds apart), NO retry of any kind.** (1) window `q3` (start 2026-07-01, end 2026-09-30), flag false; (2) window `ytd` (start 2026-01-01, end 2026-09-30), flag false. Any answer 4xx or 5xx stops the cell at once (record it; call 2 is then not made if call 1 failed). The token comes from the estate's own loader exactly as your template does it; NEVER print, log, store or put the token in any file, row or report. The ONLY vendor endpoint is `POST https://api.cloud.orionadvisor.com/api/v1/Reporting/Scope`; no other path, host or principal. Save each 2xx body verbatim as a private file `scope_<q3|ytd>.json`; the record carries its path and sha256.
3. **States and verdicts (the checker applies these exact rules to your saved bodies).** For each window with a 2xx body and each account of the household, the state is `GROUP_WITH_SERIES` (a group whose `perf` is present and `points` is 1 or more, as `groups(...)` in `p117_scope.py` computes them), `GROUP_NO_SERIES` (a group, no `perf` or no points) or `NO_GROUP`. Record `states` {window: {account sha256: state}}. Then `verdict`: `no_start_confirmed` true iff, in every window run, the `NO_START` account's state is `NO_GROUP`; `no_model_confirmed` true iff `q3` was run and the `NO_MODEL` account's `q3` state is not `GROUP_WITH_SERIES`; `others_all_present` true iff every OTHER account is `GROUP_WITH_SERIES` in every window run; `others_short_cells` the number of (window, other account) cells that are not; `claim_upgrade_allowed` true iff all three are true AND both windows were run; `claim` `measured`. A window not run has no entry in `states`, and then `claim_upgrade_allowed` is false.
4. **The script:** tracked `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~308/second_household_probe.py`, the only code this cell adds. It holds no AWS write call, names no firm other than Inflection, makes no HTTP call except the Scope POSTs, and never writes the token anywhere.
5. **Record** `SECOND_HOUSEHOLD_PROBE_R120.json` in your folder with exactly: `script` {`file`, `sha256`}; `household_sha256`; `accounts_in_household`; `account_classes` {account sha256: class word}; `no_start_account_sha256`; `no_model_account_sha256`; `calls` (in order, each {`window`, `gross_of_fees_flag` false, `http_status` (0 if no response), `ok`, and for an ok call `response_file` {`path`, `sha256`}}); `calls_made` (equals the list length and `reads.vendor_calls`); `token_store_used`; `states`; `verdict`; `c_credential` {`verdict` `ACCEPTED` if any call was 2xx, `REFUSED` if every call was 401 or 403, else `REQUEST_REJECTED`; `claim`}; `basis_words` (words, at least 160 characters: the household rule and its candidate count; the Orion household id mapping; the prediction and which parts held; the pace; anything the responses did not hold; NO value); `reads` {`vendor_calls`, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` (the token loads), `s3_reads`}; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits except in a `sha256` value or a `path` or `file` field.

<criterion id="DBI120-1-AC1" cell_refs="DB-i-8"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r120/p120_second_hh.py" . DBI120-1-AC1</invocation><expect>DBI120-1-AC1 PASS</expect></criterion>
`DBI120-1-AC1` -- the record is complete and carries no identifier; the script is a tracked file hashed as recorded with no AWS write call and no other firm's name; the household, its account classes and the two chosen accounts equal the checker's recompute from the private dimension and the round-119 roster body; 1 or 2 calls are listed in the order q3 then ytd, each `ok` agreeing with its status, each 2xx a private file hashed as recorded, no call after a failed one; the states, the four verdict fields and the credential verdict equal the checker's recompute from the saved bodies; no write to AWS, no push, no deploy. Base: FAIL (no record).

<expected_criteria>DBI120-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every file under `infra/`, `lib/` and `data/`, the template scripts and every issuer check.
- **The vendor.** POST only, exactly 2 calls, at least 5 s apart, no retry of any kind, the inner-scope body, the session token from the estate's own loader only. CTO ruling msg 8081 under CLAUDE.md "other vendor APIs need no per-use word"; Bloomberg is not involved. A redirect or login page is recorded and not followed.
- **The secret.** Read in-process by the estate's loader and used for the Authorization header only; never printed, logged, written to a file, a row, a message or your report. If the read is refused by IAM, record it and STOP; no other principal, no role assumption.
- **Writes.** The repo files of the grant and your private folder only. No write to AWS, no deploy, no push.
- **Client data.** The raw responses and the roster are client data (private folder only). The repo, rows and report carry counts, verdict words and digests.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A 4xx or 5xx, a shape the rules do not cover, or a prediction that does not hold is a RESULT: record it with its verdict and in `basis_words`; never choose another household or window, never call more than twice.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W308-S<k>`, with the real current UTC time (`date -u +%FT%TZ`, run at filing; never typed by hand); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~308/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-8.orion-scope-second-household-null-start-and-no-model-accounts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 7, cell `DB-i-8`.
<owned_cells>DB-i-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI120-1-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~308/IRPT_DASHBD.TO-DB-i-8.orion-scope-second-household-null-start-and-no-model-accounts.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI120-1-AC1` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the calls made and each one's HTTP status; `token_store_used`; the household's account count and class counts; per window the count of accounts in each state; the four verdict fields; which parts of the prediction held; the pace; row ids. No token, no client value, no account or household id.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one read script and private response files; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: the cell reads the existing Secrets Manager secret the estate's pull and performance path already use, through the estate's own loader and the worker's existing principal (rounds 117 to 119 loaded it without a refusal); no new principal or grant, and a refusal stops the cell.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI120-1-AC1 FAILS at base (no record), and the checker was fed synthetic Scope bodies for the selected household (a record built from them with the prediction holding: PASS; the same record with a wrong claim-upgrade verdict: FAIL) before the cut.
</preflight>
