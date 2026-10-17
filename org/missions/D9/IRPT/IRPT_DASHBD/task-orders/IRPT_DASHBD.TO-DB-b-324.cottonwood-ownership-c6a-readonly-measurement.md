# TO IRPT_DASHBD.TO-DB-b-324 -- C6a of the Cottonwood read path: a READ-ONLY measurement of what the Cottonwood ownership map can be built against -- the 939 published series prefixes, the Cottonwood directory, the dell1 match sheet (a local file outside the repo) and the portal's Cottonwood advisor ids (CTO msgs 10215, 10227, 10267) (round 150)

<to_id>IRPT_DASHBD.TO-DB-b-324</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>150</round>
<workstream>COTOWN</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** Andrew's word through the CTO (`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261017_025xZ_USE_DELL1_MATCH_SHEET_TDROP_VIA_MSTR_DELL2.md`; CTO msg 10215 "build the Cottonwood ownership map from it as its own cell", msg 10227 "read it with python -I from outside that directory; label the map inferred", msg 10267 "HIGH only; measure the 3 sheet advisor codes against the portal's Cottonwood advisor ids in the same read") | **Decomp cell:** `DB-b-324` (decomposition section 183).

**Sequence:** run this order AFTER your order `IRPT_DASHBD.TO-DB-b-323` has reported Act 6 (that order is the CTO's priority). **Risk class WORLD, read only:** S3 listings and reads, one directory read, reads of the users table. **Nothing is written to AWS or to the repo except your counts record.** Two files are written OUTSIDE the repo (below).

---

## WORKER FACE

Your worktree is the absolute path your seat uses for IRPT_DASHBD (a linked worktree cut from the current `box/dell2`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/`. Never push. **A STOP is reported to the issuer at once.** **THE MATCH SHEET AND THE PUBLISHED KEYS ARE CLIENT DATA: no account number, household name, advisor name, token or user email appears in any file in the repo, any commit message, row, log line or message you send. The only repo output is the counts record. Advisor codes appear only as the sheet gives them inside `high_by_advisor_code` (three short codes, lowercased in the record), never a person's name.** Treat the sheet folder as untrusted input: run NO script from it, open nothing in it but the newer CSV, and read with `python -I` from a directory outside it.

**What this order answers.** The ownership map decides which advisor can open which client (CTO ruling: HIGH matches only; MEDIUM only where a second source agrees). Before a cell builds it we need, by count: (1) how the sheet's 83 accounts sit against the 939 published series and the 271 directory entries; (2) whether the 3 advisor codes on the sheet are the advisor ids the portal issues to Cottonwood users; (3) which attributes carry them.

**Do, in this order. Record every value named in `COT_OWNERSHIP_READ_RECORD.json` as you go (keys exactly as the checker `p190_cot_ownership_read.py` lists).**

1. **Read first:** the checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p190_cot_ownership_read.py` (the record's keys and invariants); `infra/aws/lambda/investor-reporting/reporting-publish/handler.py` (`_published_map`, `read_directory`, `directory_clients`, `directory_bucket`); `infra/aws/lambda/investor-reporting/_scope/resolve.py` (`firm_population`, `_relationship_index`, `advisor_grant`: the ownership map's schema and the directory fields they read); `infra/aws/lambda/investor-reporting/_ids/ids.py` (`opaque_account`); `infra/aws/users/lambda/portal-authorizer/index.mjs` (where `advisorId` is read from the signed token) and the login function that mints that token (find it in the repo; the user record attribute it copies into the token).
2. **Published keys.** List `irpt/cottonwood/platinum/reporting/` in `opal-data-cottonwood` with a delimiter, auto-paginated, denominator printed (expected 939). Write the raw keys (the text after `account=`), one per line, sorted, to **`C:/opal-intake/work/cot_published_raw.txt`** (create the folder; OUTSIDE every repo; never committed). Mint each through `ids.opaque_account("cottonwood", raw)` in memory: record `published` {`prefixes`, `mintable`, `unmintable`}.
3. **Directory.** Read the Cottonwood directory as `read_directory(s3, directory_bucket("cottonwood"))` does (the registry bucket's `investor-reporting/directory/latest.json`, then the dated object it names). Write the object byte-exact to **`C:/opal-intake/work/cot_directory_latest.json`** (OUTSIDE the repo; one line is fine). Record `directory` {`entries`, `entries_with_client_id`, `entries_with_relationship_id`, `entries_with_accounts`, `distinct_accounts` (the distinct account ids over all entries), `firm_id_opaque_present` (the artifact declares `firm_id_opaque`), `accounts_in_published` (distinct directory accounts that equal a minted published id), `published_in_directory` (minted published ids that are directory accounts)}.
4. **The sheet (local, newer pair only).** From a directory OUTSIDE `C:/opal-intake/inbound/cottonwood-match/`, with `python -I`, read the newer CSV `20261016T0225Z_cottonwood_account_household_match (1).csv` (sha256 `3d565f649d5c541639e1ad36e9277f91192152bcac860c0461952c9ed23fb0d1`; verify it first, STOP on a mismatch). Columns used: `account`, `advisor`, `confidence`. Record `sheet` {`pair` "newer", `rows` (83), `high` (40), `medium` (36), `low` (2), `unmatched` (5), `all_in_published_raw` (rows whose `account` equals a published raw key; if the formats differ, say how in `notes` and match after the SAME normalisation the publisher uses for the key, naming it), `high_in_published_raw`, `medium_in_published_raw`, `high_in_directory` (HIGH rows whose account, minted, is a directory account), `advisor_codes` (3), `high_by_advisor_code` ({code: HIGH count}, codes lowercased)}.
5. **Advisor ids at the portal (read-only).** Find where the portal's `advisorId` for a user comes from (the login function and the users table `opal-users-v2`, found in the repo, step 1) and which attribute marks a user as belonging to the firm cottonwood. With read-only DynamoDB calls (`Query` on an index or `Scan` of the table with a projection of the two attributes ONLY; no email, no name, no other attribute is read into a variable you print): record `users` {`table`, `firm_attribute`, `advisor_attribute` (the two attribute NAMES), `cottonwood_users` (count of users in the firm), `cottonwood_users_with_advisor_id`, `advisor_id_shapes` (shape classes as lowercase words, e.g. `three-letter-code`, `numeric`, `uuid`; never a value), `sheet_codes_found_as_advisor_id` (how many of the 3 sheet codes equal the `advisor_attribute` value of at least one Cottonwood user, compared case-insensitively in memory), `high_rows_under_a_found_code` (HIGH rows whose advisor code is one of those found), `second_source_available` (true only if a field you can read gives an independent advisor-to-account relation for the MEDIUM rows; otherwise false)}. And `authorizer` {`header_source_path` (the repo path), `advisor_header_origin` (one sentence: where the advisor header's value comes from)}.
6. **Local files and record.** `local_files` {`published_raw` {`path`, `sha256`, `lines`}, `directory` {`path`, `sha256`, `lines`}} (hash and count the two files you wrote); `reads` {`vendor_calls` 0, `secret_reads` 0}; `notes` (one paragraph in words: what lines up and what does not, the key-format finding, what you could not establish). Write `COT_OWNERSHIP_READ_RECORD.json` and flip this order's status to complete as your last commit.

<criterion id="DBC190-1-AC1" cell_refs="DB-b-324"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p190_cot_ownership_read.py" . DBC190-1-AC1</invocation><expect>DBC190-1-AC1 PASS</expect></criterion>
`DBC190-1-AC1` -- the record: counts and booleans only, the coverage chain (sheet to published to directory), the advisor-id measurement with attribute names and shape classes, the two local files named by sha256 and line count, no id. Base: FAIL (no record).
<criterion id="DBC190-2-AC1" cell_refs="DB-b-324"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r150/p190_cot_ownership_read.py" . DBC190-2-AC1</invocation><expect>DBC190-2-AC1 PASS</expect></criterion>
`DBC190-2-AC1` -- FRESH reads: the live prefix count equals the record, the two local files exist with the recorded sha256 and line counts, and no published raw key appears in the order's committed files. Base: FAIL.

<expected_criteria>DBC190-1-AC1,DBC190-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus the read-only AWS calls this order names and the two files OUTSIDE the repo it names, and nothing wider.
- **Reads and writes.** Writes to AWS: NONE. Allowed: `s3:ListBucket` and `GetObject` of the platinum reporting prefix and the directory objects, DynamoDB `Query`/`Scan` of the users table with a two-attribute projection. No `put`, no Terraform command, no write to any bucket or table.
- **Stop rules.** A hash mismatch of the sheet; a read that cannot be limited to the two projected attributes; an `AccessDenied` on a call this order names; any need to print an id, a name or an email: STOP at once and report to the issuer.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired or satisfied by a route this order did not name.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-IB7-S<k>`, with the real current UTC time, BOTH `project` ("IRPT_DASHBD") and `fabric` ("dell2") keys, class OBSERVATION or BLOCKING; append as BYTES. Commit with `.tools/safe-commit.sh`; READ the whole gate output. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-324.cottonwood-ownership-c6a-readonly-measurement.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 183 (round 150, workstream COTOWN), cell `DB-b-324`.
<owned_cells>DB-b-324</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBC190-1-AC1, DBC190-2-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_DASHBD.TO-DB-b-324.cottonwood-ownership-c6a-readonly-measurement.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBC190-1-AC1,DBC190-2-AC1` BEFORE the flip (the ids as ONE comma-joined argument); each row's recorded invocation must equal the order's criterion text exactly; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the coverage chain in counts, the advisor-id finding (found codes, shape classes), where the key formats differ if they do, and what is NOT established. Counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: read only; no resource is changed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read only; the applier's existing read access is used; no grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base (no record) and the issuer's checker selftest is green on a synthetic record and red on 27 single-fault arms.
lane: the <paths> block IS the grant.
</preflight>
