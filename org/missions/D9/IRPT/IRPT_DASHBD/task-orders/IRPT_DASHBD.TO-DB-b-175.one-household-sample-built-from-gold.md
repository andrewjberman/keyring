# TO IRPT_DASHBD.TO-DB-b-175 -- one 49 Financial household of several accounts built into the performance-report contract's shape by a tracked builder that reads gold and writes nothing served; unsourced figures read ABSENT, never zero; the proof read is the balance identities

<to_id>IRPT_DASHBD.TO-DB-b-175</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~141</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>94</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msgs 7181 and 7192, ROUND-94 ANALYSIS item 2 (PRD v0.14, FWD-21) | **Rows:** NONE | **Decomp cell:** `DB-b-175` (decomposition section 96) | **outcome_ref:** FWD-21 | **depends_on:** DB-b-174 (the contract; this order is spawned after it drains).

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-141` (branch `wk-IRPT_DASHBD-141`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~141/`. Your private folder (client data lives only here, outside the repo) is
`C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~141/` (create it).

**Why.** FWD-21's contract (`org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json`, written by the previous cell: read it first, with its `document` layout and its `members`, each of which names an Opal gold source in a sibling contract of `org/standards/` or is ABSENT) is only real once one actual household has been built into it from gold. The CTO asks for one 49 Financial household of several accounts, built by a
builder that reads gold and writes nothing served, with every unsourced figure reading ABSENT and never zero. This sample feeds the tab and the export renders (which use SYNTHETIC fixtures in the repo; yours is the real shape, kept private).

**The cell (`DB-b-175`).**
1. **The builder.** ONE new tracked module `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~141/build_sample.py` (ASCII, passes `bash .tools/commit-gate.sh`; run under `python -I`; usage `python -I build_sample.py <repo_root> <private_out_dir>`). It reads the contract; for each member with a `source` it reads that sibling contract's field from the gold address the sibling documents (its `address`), for the chosen household; for each ABSENT member it writes
   `{"absent": "<the member's reason in words>"}` and never a number. It writes the filled report, in the contract's `document` layout, ONLY to `<private_out_dir>/HOUSEHOLD_SAMPLE.json`. It reads S3 with GET and LIST only (the gold and platinum stores of firm 49 Financial named in the sibling contracts' addresses, e.g. `s3://opal-data-49financial/irpt/49financial/gold/...`); no put, copy or delete; no vendor call; no secret read.
2. **The household.** **ISSUER'S RULING (amendment, after your rows W141-S1 and W141-S2): the grouping comes from the household crosswalk.** The ADVI household crosswalk (`org/standards/ADVI_BILLING_HOUSEHOLD_CROSSWALK_CONTRACT.json`: `s3://opal-data-49financial/advi/49financial/gold/household_crosswalk/date=<run date>/household_crosswalk.parquet`, one row per custodian account, `schwab_account_number` in the same 10-digit form as the IRPT gold `account_id`, with `opal_relationship_id` as the household-level key) is GRANTED for S3 GET and LIST, that one prefix and nothing else under `advi/`, newest `date=` partition. A household is the set of accounts that share an `opal_relationship_id`. The issued-id versus custodian-id gap of the client summary stays as it is: you do NOT use the client summary or the investor-reporting directory (still not granted);
   the accounts and every figure come from the custodian-keyed gold tables. Choose, by a rule you write in the module's docstring BEFORE you look at any figure (for example: a client with at least 3 published accounts and at least 12 months of history in the return table, the lowest hashed id), ONE household. Record only `household_ref_sha256` (the hash of its `opal_relationship_id`) and its account count; never the id, a name or an account number.
3. **AMENDMENT 2 (issuer 2.0.0_SA_COO~D2, 2026-10-13, after your second seat's rows W141-S3 to S6; gate limb: none graded it, a modification of an existing order).** Measured by your last seat: gold `account_activity_daily` holds FOUR trading days (2026-10-07, 10-08, 10-09, 10-12), so no quarter-to-date, year-to-date, last-12-months or since-inception window can open from it today. That is a finding about the producer's history (the CTO is told), not a reason for this cell to fail. So, in force from now:
   (a) **Households.** The 12-month history test is DROPPED from the household rule. Write a NEW rule in the module's docstring before you read any figure: a household is the accounts sharing an `opal_relationship_id` (newest crosswalk partition) that are present in the newest `account_activity_daily` partition; choose the one with at least 3 such accounts and the lowest sha256 of its relationship id. (You have seen that zero households pass the old 12-month test; the new rule does not depend on any figure.)
   (b) **Windows the gold cannot open are ABSENT IN WORDS**, never zero and never blank: every member whose window needs history the gold does not hold is `{"absent": "history not yet built: gold account_activity_daily holds <N> trading days from <first> to <last>"}` (the day counts and dates are the only dates allowed, and only in the PRIVATE sample file; the record carries only the count N). Members whose own source is outside this cell's grant (the client summary, the fee-basis row for method_version 3) are ABSENT in words naming that reason.
   (c) **The proof read is the DAILY ledger identity.** For each account of the household and for each pair of consecutive trading days present in `account_activity_daily` (and for the household as the sum of its accounts), check the identity the activity contract documents for one day (read its text; if it states none, state in your rule the identity its columns define: ending value minus beginning value equals contributions minus withdrawals plus realized plus unrealized change plus income, with the signs the contract gives) within 1 dollar. Record `identity.checks` (at least 4 are needed), `identity.passed` (equal to checks), `identity.tolerance_dollars` 1 and `identity.basis` "daily_ledger". Where a standard window HAS all four members available, add its window identity to the count; today none does. If fewer than 4 daily checks are possible, file a surprise row and stop.
   The rest of this step below is unchanged where it does not conflict.
   Original step 3: **The proof read** is not a figure print. For the household and for each account, and for each of the four standard windows (quarter to date, year to date, last 12 months, since inception) whose four members (beginning value, net additions, net gain, ending value) are all sourced, check `beginning + net additions + net gain = ending` within 1 dollar. Print and record COUNTS of checks and passes only. If fewer than 4 checks are possible because those members are ABSENT, file a surprise row and stop (the issuer decides).
   You may print the household value summary and the activity summary to the PRIVATE folder's `PROOF_READ.txt` for the issuer to read; they never go in the repo, the record or your report.
4. **Shape.** Validate the written sample against the contract: every member id appears exactly once; every ABSENT member is `{"absent": ...}` and carries no number; every sourced member carries a value or `{"absent": "<reason>"}` where the gold row holds none (a missing gold value is ABSENT in words, never zero). Record `shape_valid_against_contract` and `absent_members_never_zero`.
5. **Record** `HOUSEHOLD_SAMPLE_BUILD.json` in your folder, exactly these keys: `code` {`file`, `sha256` (of its committed bytes), `tracked`: true}; `contract_sha256` (of the contract file's bytes); `household` {`accounts`, `household_ref_sha256`}; `members` {`total` (equal to the contract's member count), `filled`, `absent` (filled + absent = total; absent is at least the contract's own ABSENT count)}; `absent_members_never_zero`; `shape_valid_against_contract`;
   `identity` {`checks`, `passed`, `tolerance_dollars`: 1}; `reads` {`s3_reads` (a count above 0), `s3_writes`: 0, `vendor_calls`: 0, `secret_reads`: 0}; `sample_kept_private`: true; `served_values_changed`: false; `limits`. NO account id, client name, amount or run of eight or more digits in the record or your report.

<criterion id="DB94-2-AC1" cell_refs="DB-b-175"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r94/p94_round94.py" . DB94-2-AC1</invocation><expect>DB94-2-AC1 PASS</expect></criterion>
`DB94-2-AC1` -- the record exists with the keys above; the builder is tracked and hashes to the stated sha256; the record is bound to the contract's bytes; the household has two or more accounts and is referenced by hash; the member counts sum to the contract's total with at least the contract's ABSENT members absent; no absent figure is zero and the sample validates against the contract; at least 4 identity checks were made and all passed within a dollar;
S3 was read and never written; no vendor call, no secret read; no served value changed; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB94-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the contract and every sibling contract.
- **No S3 write, no vendor call, no secret read, no deploy, no push, no portal.** S3 GET and LIST of the gold and platinum stores of `irpt/49financial/` and of the one crosswalk prefix `advi/49financial/gold/household_crosswalk/` only (issuer's grant, amendment 1). A denial is recorded verbatim, not retried by another route.
- **No client data in what you write.** Counts and booleans only in the repo; the sample and the proof read live only in your private folder.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A result you could not establish is NOT_ESTABLISHED with its reason, never guessed. An edit outside the grant is a defect: stop and file a row.
- **Every `.py` edit passes `bash .tools/commit-gate.sh <file>`.** ASCII only. Commit with `.tools/safe-commit.sh` as your definition says.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W141-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES, never re-encode the existing content.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~141/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-175.one-household-sample-built-from-gold.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 96 (round 94), cell `DB-b-175`.
<owned_cells>DB-b-175</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB94-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~141/IRPT_DASHBD.TO-DB-b-175.one-household-sample-built-from-gold.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB94-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the household rule you wrote; the account count; the member counts (filled, absent); the identity checks made and passed; which gold stores the builder read; any figure the contract maps that the gold row did not hold; any row ids. Counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; a private read of gold and a counts-only record; nothing served.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer; S3 GET and LIST of stores earlier tie-out cells read; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record; 60 synthetic arms dry-run).
lane: the <paths> block IS the grant.
</preflight>
