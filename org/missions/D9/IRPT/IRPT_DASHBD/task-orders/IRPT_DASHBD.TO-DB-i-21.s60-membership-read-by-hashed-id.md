# TO IRPT_DASHBD.TO-DB-i-21 -- the S60 membership read: which account moves between the 39 ABSENT NO_START_DATE_AT_SOURCE rows of the landed feed and the 40 null-start accounts of the round-119 roster, and where S60's account sits; sha256 of the id string and counts only

<to_id>IRPT_DASHBD.TO-DB-i-21</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~321</issued_to>
<issued_by>2.0.0_SA_COO~I2</issued_by>
<issued_date>2026-10-19</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>133</round>
<workstream>B-IN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2`, `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-IN_ROUND_132_20261019.md` @14e06e4b55 (msg 10703), ruling 3 and enrichment E2: "The 39-against-40 difference is settled by the S60 membership read. Counts and hashed ids only."

---

## WORKER FACE

Your workspace worktree is the absolute path your prompt names (branch `wk-IRPT_DASHBD-321`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~321/`. Your PRIVATE folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~321/` (create it). Never touch a path outside the `<paths>` block below and your private folder, except to READ the one private file named in step 1.

**Why.** The Scope feed's first landed silver carries 39 accounts as ABSENT `NO_START_DATE_AT_SOURCE`. The round-119 account-record read (cell DB-i-7) counted 40 accounts with a null `accountStartDate` in Orion's active roster. One account is on one side and not the other. Surprise row `IRPT_DASHBD-D2-S60` is an Inflection account that has no Orion Scope group over Q3 or YTD; its record has a null start date, and its sha256 is recorded in the round-119 record as `roles_sha256.missing_sha256`. This cell names the account that moves between 39 and 40, by sha256, and says which class the feed gives S60's account.

**Read first (read only).**
- `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~307/ACCOUNT_RECORD_READ_R119.json`: `roles_sha256.missing_sha256` is S60's account (a sha256 of the account id string); the entry of `gets` whose `kind` is `newportfolio_active` names the roster's id key as `account_id_key`.
- `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~307/account_record_read.py` (`key_of`, `dig`, `find_record`: how an id is turned into the string that is hashed, and how the roster rows are read). Reuse the SAME id-to-string rule, so that your hashes equal the round-119 hash.
- `data/assets/scripts/gold/irpt_reporting/adapters/inflection_account_dim.py` (`InflectionSilverReader`: `list_partitions`, `read_parquet`, `reads`) and `inflection_account_return_daily.py` (`ORION_SILVER`).
- The checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r133/p133_membership.py` (its record whitelist, extract shape and recount ARE the specification; read it first and run `python -I <it> --selftest`).

**The cell (`DB-i-21`).**
1. **The script:** tracked `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~321/member_read.py`, the only code this cell adds. It builds `reader = iad.InflectionSilverReader()`, lists the partitions of the silver table `iar.ORION_SILVER + "scope_account_returns"`, reads the LATEST partition (one GET), and takes each feed account's class: the word in its `reason_class` column when the row is ABSENT, and the word `RETURNED` when its status is RETURNED. It reads the round-119 private roster response, the LOCAL file `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~307/get1_newportfolio_active.json` (read only; it is the file the round-119 record hashed), takes each roster account's id by the key the record names, and whether its `accountStartDate` is null or empty. It computes the sha256 (hex) of each account's id string BEFORE anything is written. It holds no write call, no vendor call, no credential, no `s3://` literal (the address comes from `iar.ORION_SILVER`) and never prints an id.
2. **The private extract** `membership_extract.json` in your private folder: `{"silver_partitions": <int, the number of partitions listed>, "accounts": {"<sha256>": {"roster_null_start": <bool>, "feed_class": "<word>"}}}` for every account in the latest partition (an account of the roster that is not in the feed is not in the extract).
3. **The record** `S60_MEMBERSHIP_R133.json` in your folder with EXACTLY the keys of the checker's `REC_KEYS`: `script` {`file`, `sha256`}; `extract` {`path` (absolute, private), `sha256`}; `silver_partitions`; `feed_accounts`; `roster_null_start` (feed accounts whose roster record has a null start date); `feed_no_start_date` (feed accounts whose class is `NO_START_DATE_AT_SOURCE`); `a_minus_b_sha256` (sorted sha256 of accounts null-start in the roster but NOT classed `NO_START_DATE_AT_SOURCE` by the feed) with `a_minus_b_feed_class` (the feed's class word for each, same order); `b_minus_a_sha256` (classed `NO_START_DATE_AT_SOURCE` by the feed but not null-start in the roster); `s60_account_sha256` (the round-119 `missing_sha256`); `s60_in_roster_null_start`; `s60_feed_class` (its class word, or `NOT_IN_FEED`); `s60_in_difference`; `verdict` (`NO_DIFFERENCE` when both differences are empty, else `DIFFERENCE_SHOWN`); `reads` {`s3_reads` (your counter), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}; `files_in_repo_private` false; `served_values_changed` false; `pushed` false; `deployed` false; `basis_words` (words, at least 200 characters: how many silver partitions and feed accounts; the roster null-start count and the feed `NO_START_DATE_AT_SOURCE` count; the size of each difference; for each account in the first difference its feed class word; where S60's account sits; what this does not establish; NO id, NO date, NO value). No run of 8 or more digits except in a `sha256` value or a `path` / `file` field; no date and no partition name anywhere in the record.
4. **Do not fix.** If the round-119 file is missing or unreadable, or the id key does not match the feed's account ids, that IS the result: record it with a surprise row and stop. Never call the vendor to fill a gap.

<criterion id="DBI133-2-AC1" cell_refs="DB-i-21"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~I2/checks/r133/p133_membership.py" . DBI133-2-AC1</invocation><expect>DBI133-2-AC1 PASS</expect></criterion>
`DBI133-2-AC1` -- the record is complete and carries no identifier or date; the script is a tracked file hashed as recorded with no write, vendor-call or credential token, built on `InflectionSilverReader` and hashing ids; the extract's hash equals the recorded one; every count, both set differences (by sha256), S60's membership and class, and the verdict equal the checker's recount from the extract; S60's sha256 equals the round-119 record's; no write, no push, no deploy. Base: FAIL (no record).

<expected_criteria>DBI133-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below and your private folder. The one private file you may READ outside it is the round-119 roster response named in step 1. Everything else is read, never edited.
- **Reads only.** GET and LIST through `InflectionSilverReader`, plus that one local file. No S3 write, no vendor call, no secret read, no push, no deploy. Read cap: 400.
- **Client data.** The silver, the roster file and your extract are private; the repo, rows and your report carry counts, class words and sha256 values only. Never print an account id or a household id.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W321-S<k>`, `surfaced_at` from `date -u +%FT%TZ` at filing; append as BYTES. Commit with `.tools/safe-commit.sh`. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~321/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-i-21.s60-membership-read-by-hashed-id.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_B-IN.md</decomp_doc> section 19, cell `DB-i-21`.
<owned_cells>DB-i-21</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBI133-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~321/IRPT_DASHBD.TO-DB-i-21.s60-membership-read-by-hashed-id.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBI133-2-AC1` (run the WORKTREE'S OWN copy from inside your worktree) BEFORE the flip; pin each artifact row to the commit that carried it (not PENDING-THIS-COMMIT, unless the instance commit itself carries it).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the counts (silver partitions, feed accounts, roster null-start, feed NO_START_DATE); the size of each difference and the class word of each account in the first; S60's membership and class; the S3 reads made; row ids. No token, no client value, no account or household id, no date.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: one read script and private files; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: GET and LIST of Opal's own Orion silver through the round-108 reader (the granted prefix and principal rounds 108 to 132 used); one local private file; no new principal or grant, no write.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBI133-2-AC1 FAILS at base (no record), and the checker's self-test builds a GOOD record (PASS) and thirteen mutants (a wrong roster count, a wrong feed count, an emptied difference, S60 membership flipped, S60 class changed, a wrong verdict, an S60 hash not the round-119 one, an id-like digit run, a date, an s3 write, a changed extract, a script with an Authorization token, a script that never hashes), each FAIL.
</preflight>
