# TO IRPT_DASHBD.TO-DB-b-181 -- FDRXX to CASH, cell A (local): in the gold ETF classifier a security whose canonical row is typed Cash by sub_asset_class takes the cash asset class, keyed on that type and not on a ticker list; the count of the canonical rows and of the served holdings that move; no deploy, no write

<to_id>IRPT_DASHBD.TO-DB-b-181</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~147</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>issued</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>96</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2 msg 7258 ("Cut one cell so money-market funds classify as CASH in data/black_diamond/scripts/gold/lib/etf_classifier.py:144, keyed on the fund's money-market type, not a ticker list. It moves served classes on the Advisor Intelligence and IR pages, so it goes under a never-widen pair, with a count of the holdings that move.") | **Rows:** IRPT_DASHBD-D2-W144-S2 | **Decomp cell:** `DB-b-181` (decomposition section 98) | **outcome_ref:** FWD-21 (and FWD-8's class label) | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-irpt-dashbd-147` (branch `wk-IRPT_DASHBD-147`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~147/`.

**What Andrew saw.** "FDRXX should be listed as a 'CASH' tagged asset, not Fixed Income." The portal assigns no class by symbol: it shows the served `asset_class`. The class comes from the gold ETF classifier, which returns the canonical table's row verbatim. The issuer read the table: DynamoDB `etf-classifications` (us-east-1, about 11,361 items; the key is `ticker`; fields `asset_class`, `sub_asset_class`, `name`, ...). The row for FDRXX reads `asset_class` `fixed_income` and `sub_asset_class` `Cash`. The classifier's one special case is `CASH_USD`, which returns `fixed_income` (a quirk you read and report; you do not change it unless the issuer's rule below forces it).

**The cell (`DB-b-181`).** This is cell A of two: a code change, its tests and the COUNT. Nothing is deployed, nothing is written.
1. **Read first.** `data/black_diamond/scripts/gold/lib/etf_classifier.py` in full (`classify`, `get_sub_asset_class`, `classify_with_identity`, the name and identity hops), the shared client it uses (`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py`) and the existing tests of the classifier (find them with `comp-find --files 'etf_classifier' --limit 20`; run them before you edit, under python -I from files, and record pass/fail as your base). Find the CONSUMERS of the classifier's class: `comp-pipescript io <script>` and `comp-estate` over the gold and silver scripts that import it (`classify(`, `classify_with_identity(`), and name the pages that read the served class (the issuer's note: the Advisor Intelligence and IR pages). `consumers` in the record lists them in words.
2. **The vocabulary, read-only.** Read the canonical table with one boto3 `scan` (read-only; 11 thousand small items; use paginated scan with a projection of `ticker, asset_class, sub_asset_class`, in a script file under python -I; use the AWS identity this box already has, no new credential). Count: the distinct `asset_class` values with their counts (`vocabulary.asset_class_values_in_table`), the rows whose `sub_asset_class` is `Cash` (compare case-insensitively after trimming; list the distinct spellings you saw as counts), and among those how many already carry the cash class. **Which asset_class value means cash?** If the table already uses one (for example a `cash` class), that is `rule.cash_asset_class_value`. If NO value is a cash class, do not invent one: file a surprise row with the vocabulary counts and stop (the issuer rules the vocabulary). Never print a ticker list in the repo; counts only.
3. **The rule.** In the classifier, after the canonical row is read (in `classify` and in every branch of `classify_with_identity` that returns a canonical row's class), a row whose `sub_asset_class` (trimmed, case-insensitive) is `cash` takes the cash `asset_class` value. It is keyed on the row's TYPE, never on a ticker or a name list (`rule.keyed_on` "sub_asset_class", `ticker_list_used` false). Every other row still returns the table's `asset_class` VERBATIM (no other translation: the module's own contract). `classify` and `classify_with_identity` must give the same class for the same row. Keep the `CASH_USD` special case as it is and say so (`cash_usd_special_case` "unchanged"), unless you find it contradicts the rule on the same input, in which case report it in a row and leave it (`unchanged`).
4. **The tests.** A new test file next to the existing classifier tests, using the client injection seam (a stub with `get_classification(ticker)`; no AWS): (a) a row typed Cash with class `fixed_income` returns the cash class from `classify` AND from `classify_with_identity`; (b) a row typed Cash with the cash class already returns it; (c) an ordinary `fixed_income` row and an `equity` row are returned verbatim; (d) `sub_asset_class` in another case or with spaces is handled; (e) a row with no `sub_asset_class` is returned verbatim. ONE temporary mutant (drop the rule) that the tests catch, then reverted. Run `bash .tools/commit-gate.sh <file>` on every `.py` you touch.
5. **The count of what moves.** (a) `canonical_rows`: `total` (the table's items you scanned), `sub_asset_class_cash`, `cash_rows_already_cash_class`, `would_move` (equal to the Cash-typed rows not already in the cash class; FDRXX is one), and `fdrxx_in_would_move` true. (b) `served_holdings`: the positions in the SERVED holdings store(s) whose ticker is one of the would-move rows and whose served `asset_class` is not the cash class today: find which gold or silver store the consumers read (name it in `stores_read`), read it by S3 GET and LIST only (newest partition per firm, enumerating what the graph holds before you list: `comp-pipescript io`), and count `positions_scanned`, `positions_that_move`, `per_firm` (an object firm -> count, summing to `positions_that_move`) and `accounts_with_a_moving_position`. These counts bind the never-widen pair, so state in `limits` what the count does not see (for example partitions you did not read).
6. **Record** `FDRXX_CASH_CHANGE.json` in your folder with exactly: `rule` {`keyed_on`, `cash_asset_class_value`, `ticker_list_used`}; `vocabulary` {`asset_class_values_in_table` (an object value -> count), `sub_asset_class_spellings` (an object spelling -> count)}; `canonical_rows`; `fdrxx_in_would_move`; `served_holdings`; `consumers` (a list of strings); `code` {`file`: "data/black_diamond/scripts/gold/lib/etf_classifier.py", `sha256` (of its committed bytes), `tracked` true}; `test` {`file`, `mutant_failed` true, `passed`, `failed` 0}; `unchanged_rows_still_verbatim` true; `cash_usd_special_case`; `reads` {`dynamodb_writes` 0, `s3_writes` 0, `vendor_calls` 0, `secret_reads` 0}; `deployed` false; `pushed` false; `served_values_changed` false; `limits`. Counts and words only: no ticker, no account id, no name, no run of eight or more digits.

<criterion id="DB96-2-AC1" cell_refs="DB-b-181"><invocation>python "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r96/p96_round96.py" . DB96-2-AC1</invocation><expect>DB96-2-AC1 PASS</expect></criterion>
`DB96-2-AC1` -- the rule is keyed on the row's sub_asset_class, uses a cash class value the table already has, and uses no ticker list; the canonical-row counts are arithmetic-consistent and include FDRXX; the served-holdings count names its stores, sums per firm and counts accounts; the consumers are named; the classifier is tracked, carries the rule and hashes to the stated sha256; the tests pass (3 or more, none failing) and a mutant fails; unchanged rows stay verbatim; no write of any kind, nothing deployed or pushed; no run of 8 or more digits. Base: FAIL.

<expected_criteria>DB96-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **No write of any kind to AWS** (no DynamoDB put/update/delete, no S3 put/copy/delete, no Lambda, Terraform or IAM act), **no deploy, no push, no vendor call, no secret read.** Reads only: one paginated scan of the canonical table, S3 GET/LIST of the served holdings stores, repo files. A denial is recorded verbatim, not retried by another route.
- **This change moves served classes once it is deployed**, which is cell B (the issuer's, under a never-widen pair with the AE applier). You do not deploy, release, upload or run the gold job.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If no cash class value exists in the table, stop and file the row. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W147-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~147/
data/black_diamond/scripts/gold/lib/etf_classifier.py
data/black_diamond/scripts/gold/tests/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-181.money-market-funds-classify-as-cash-cell-a.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 98 (round 96), cell `DB-b-181`.
<owned_cells>DB-b-181</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB96-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~147/IRPT_DASHBD.TO-DB-b-181.money-market-funds-classify-as-cash-cell-a.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB96-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the vocabulary (the asset_class values and counts) and the cash value you chose; the counts (canonical rows, served positions, per firm, accounts); the consumers; the tests and the mutant; the base test result; what the count does not see; any row ids. Counts and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the change is local and undeployed. The blast radius of cell B (the apply) is what the count measures, and the pair will name it.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only scan and S3 GET/LIST with the box's existing identity; a denial is a result.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched; nothing is released.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criterion FAILS at base (no record) and is dry-run on 29 synthetic arms.
lane: the <paths> block IS the grant.
</preflight>
