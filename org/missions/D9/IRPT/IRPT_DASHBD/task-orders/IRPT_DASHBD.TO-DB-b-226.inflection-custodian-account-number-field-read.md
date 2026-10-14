# TO IRPT_DASHBD.TO-DB-b-226 -- the CUSTODIAN ACCOUNT-NUMBER FIELD READ for Inflection: which Orion or Eclipse silver field holds the custodian account number (a string column keyed to the account, stable across dates, unique per account, carrying a digit run of 4 or more), measured in counts only; nothing is changed

<to_id>IRPT_DASHBD.TO-DB-b-226</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~181</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>111</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-111 ANALYSIS section 1 (row "The labels") and section 2 cell 3 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_111_20261014.md`) | **Rows:** IRPT_DASHBD-D2-W181-S<k> | **Decomp cell:** `DB-b-226` (decomposition section 113) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-181` (branch `wk-IRPT_DASHBD-181`); run everything from its root. The portal is not used by this cell. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~181/`. Commit with `.tools/safe-commit.sh` and your author line; never push. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, hashes and words only in the repo, a row or your report. An account number, an account id, a household or client id, a name, and any value or fragment of a value from the silver (a piece of text, a run of digits) is NEVER written down: only column names, table names, counts and shares.

**Why.** The CVO graded the Inflection render FAIL on its account labels: three accounts read "Account ending 4INT" and "Account ending tion (1 of 2)" and "(2 of 2)", because the field the sample builder took for the custodian account number (`accountNumber` in Orion's `fact_positions`) carries text fragments, not a number. The CTO ruled: "ending" prints only before a real digit run of at least 4 digits taken from a field MEASURED to be the custodian account number; otherwise the label is "Account <n> of <N>". This cell measures whether any Orion or Eclipse silver field is that number. If one is found the label switches to it in the round after; if none is, the fallback label stands.

**The grant of the S3 reads (BY PREFIX).** LIST and GET under `s3://opal-data-assets/orion/inflection/silver/` and `s3://opal-data-assets/eclipse/inflection/silver/` and nowhere else, ONLY through the round-108 adapter's GET-only reader (`InflectionSilverReader` in `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_dim.py`, which derives its granted prefixes from the registry row and refuses any other path). The Orion master prefix `orion/4698/` and every other firm's place are NOT granted. No put, copy or delete of any kind. The silver guard reads FAIL (alien partitions of `fact_assets` and `fact_positions` for 2026-08-06 and 2026-09-29, the issuer's own-surplus finding): leave those two dates out of every sample.

**The cell (`DB-b-226`): a READ. Nothing is changed, deployed or written outside your folder and the private folder.**
1. **Read first.** The issuer's check `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r111/p111_acctfield.py` (your criterion: read `check_record`, `check_candidate` and `qualifies` fully; run `python -I <that file> --selftest .` from your root), the round-108 reads `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~172/COVERAGE_READS_R108.json` and `READ_COVERAGE_RUN_R108.json` (the table list and which tables are cumulative), and the adapter above (how it reads a table, its account-key columns, `account_dim`).
2. **The tables.** Orion: `fact_assets`, `fact_positions`, `fact_transactions`, `fact_performance`. Eclipse: its four silver tables (name them from the round-108 record). For each table read the NEWEST dated partition once for the shape (`fact_transactions` and `fact_performance` are cumulative: their newest partition is the whole history; `fact_positions` and `fact_assets` are one as-of date per partition). An unreadable table is recorded with `claim` "absent" and the reason in a row, never as a zero.
3. **Measure every STRING column** of every table's shape partition, in counts and shares only: `distinct_values`, `non_null_values`, `share_values_digit_run_ge4` and `share_values_digit_run_ge8` (the share of non-null values whose longest run of consecutive digits is 4 or more, 8 or more), `share_values_all_digit`, `share_values_alpha_only`. Decide `keyed_to_account`: true when the table has an account key column and the column holds ONE value per account per partition; a table with no account key (for example `fact_performance`, keyed by client) gives false for every column. Over the accounts in scope (the accounts of the round-108 dry-run table `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~171/ACCOUNT_DIM_DRY_RUN.parquet`, or for an Eclipse table the distinct account keys of that table's shape partition: state which in `scope_words`) measure `accounts_with_value`, `share_accounts_digit_run_ge4` (accounts whose value has a digit run of 4 or more, over the accounts in scope) and `share_accounts_unique` (accounts whose value no other account carries, over the accounts with a value).
4. **Stability.** For EVERY string column of `fact_positions` and of the Eclipse positions table, and for any other column that passes the 95 percent digit-run and uniqueness tests in its shape partition, sample up to FIVE dated partitions of its table spread over the last 120 calendar days (the newest plus up to four earlier, never an alien date) and measure `share_accounts_stable`: the share of accounts carrying the SAME value in every sampled partition where the account appears. Record `partitions_sampled` (the shape partition counts as one; a column measured on one partition has `partitions_sampled` 1 and cannot qualify, the checker refuses it).
5. **The rule and the answer.** A column `qualifies` only if `keyed_to_account` is true, `partitions_sampled` is 2 or more, and `share_accounts_digit_run_ge4`, `share_accounts_stable` and `share_accounts_unique` are each at least 0.95 (the checker recomputes the flag from your numbers). `answer.field_found` is true when at least one candidate qualifies (then `answer.table` and `answer.column` name one of them, names only, with `claim` measured), else false (`table` and `column` null, the words say what was closest and why it failed, `claim` measured when every table was read, held or absent when one was not).
6. **A positive control.** Run YOUR same qualification function on two synthetic columns you build in memory: one built as a custodian number (a stable, unique, 8-digit value per account over several dates) and one built as a text fragment (a short word-like value that repeats across accounts); show the first qualifies and the second does not (`positive_control`: `description`, `expected`, `observed` in words; `passed` true; `synthetic_number_qualifies` true; `synthetic_fragment_qualifies` false). A test that cannot tell the two apart measures nothing.
7. **Record** `RD_ACCOUNT_NUMBER_FIELD_R111.json` in your folder with exactly: `answer` {`field_found`, `table`, `column`, `words`, `claim`}; `candidates` (a list, ONE entry per string column examined, each with exactly the keys `firm` ("orion" or "eclipse"), `table`, `column`, `distinct_values`, `non_null_values`, `share_values_digit_run_ge4`, `share_values_digit_run_ge8`, `share_values_all_digit`, `share_values_alpha_only`, `keyed_to_account`, `accounts_with_value`, `share_accounts_digit_run_ge4`, `share_accounts_stable`, `share_accounts_unique`, `partitions_sampled`, `qualifies`, `claim`, `words`: a share is a number from 0 to 1; names are letters, digits and underscores only; `words` is a short sentence with no value in it); `denominator` {`tables_read`, `partitions_read`, `accounts_in_scope`, `scope_words`}; `positive_control`; `reads` {`s3_reads` (integer), `s3_writes` 0, `vendor_calls` 0, `secret_reads` 0, `dynamodb_writes` 0}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Every group that carries a `claim` uses one of `measured`, `inferred`, `held`, `absent`. Counts, shares, names and words only: no run of 8 or more digits anywhere outside a `sha256`, `path`, `file`, `key`, `where`, `vintage` or `scope_words` field, and no value, fragment or number from the data.

<criterion id="DB111-3-AC1" cell_refs="DB-b-226"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r111/p111_acctfield.py" . DB111-3-AC1</invocation><expect>DB111-3-AC1 PASS</expect></criterion>
`DB111-3-AC1` -- the record lists at least one candidate column with exactly the required keys, each share between 0 and 1, names only, a claim in the four-word set; each candidate's `qualifies` flag equals the checker's recomputation (keyed to the account, 2 or more partitions sampled, 95 percent of accounts with a digit run of 4 or more, stable and unique); `answer.field_found` agrees with the candidates (true names a qualifying candidate with claim measured or inferred; false has null table and column and no qualifying candidate); the denominator is printed and consistent with the candidates; a passed positive control that qualifies the synthetic number and refuses the synthetic fragment; zero writes, vendor calls and secret reads; the false flags; no run of 8 or more digits outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB111-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the Inflection adapters and their tests, every contract, every portal file, every other worker's folder and the issuer's check files.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the two Inflection silver prefixes above ONLY through the adapter's GET-only reader; the private dry-run table named in step 3. Writes: the repo files of the grant and the private folder `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~181/` (scratch only). No write to AWS of any kind, no deploy, no push, no vendor call, no secret read, no read of any other firm's place.
- **Client data.** The silver and the dry-run table are client data: column names, table names, counts and shares only in the repo, a row or your report. Nothing you read is copied: not an account number, a name, a text fragment or a digit run.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a table cannot be read through the reader, record it `absent` with the reason and file a row; never count it as zero and never read it by another route. If no column qualifies the answer is `field_found` false: that is a finding, not a block. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W181-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~181/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-226.inflection-custodian-account-number-field-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 113 (round 111), cell `DB-b-226`.
<owned_cells>DB-b-226</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB111-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~181/IRPT_DASHBD.TO-DB-b-226.inflection-custodian-account-number-field-read.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB111-3-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; whether a field qualifies (names only); the number of string columns examined, tables and partitions read, and S3 reads; per table how many columns were examined and how many passed the digit-run test alone (counts only); the positive control's result; row ids. No account number, account or household id, name, fragment or value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read-only measurement of two granted Inflection silver prefixes and one record file; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 LIST and GET of two Inflection-scoped prefixes of the monolith bucket through the round-108 adapter's grant-enforcing reader; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB111-3-AC1 FAILS at base (no record) and the rule's recomputation, the answer-versus-candidates agreement and the zero-effect clauses are exercised by the checker's self-test (10 refusal arms, 2 passing).
lane: the <paths> block IS the grant.
</preflight>
