# TO IRPT_DASHBD.TO-DB-b-244 -- the 2026-04-21 QUANTITY READ (round 121, workstream B-49F): what moved the quantities of the 943 accounts the flow guard disagreed on, by security, by event word and by the presence of a same-day transaction row; whether a corporate-action or share-class-conversion source exists; counts by security and by event word only; nothing written and no guard change

<to_id>IRPT_DASHBD.TO-DB-b-244</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~198</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>121</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 121 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-121 ANALYSIS (B-49F) section 2 ruling 3 and section 3 cell 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_121_20261015.md @9d4bd6adf3`: "READ what moved the quantities of the 929 accounts on 2026-04-21: the transaction and activity words for that day; any corporate-action or share-class-conversion record; whether one security accounts for most of the cohort. Counts by security and by event word. No guard change until it lands") | **Rows:** IRPT_DASHBD-D2-W198-S<k> | **Decomp cell:** `DB-b-244` (decomposition section 119) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-198` (branch `wk-IRPT_DASHBD-198`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~198/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~198/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Round 120's balance-lag read (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~192/RD_BALANCE_LAG_R120.json`) showed that on 2026-04-21 the custodian's account value and positions agree with each other while the price-only return at the previous day's quantities agrees with neither, because every flagged account changed quantity that day with no external-flow word. This cell reads WHAT the change was. The issuer's first look at the custodian transaction source (`fact_trn`, 2026-04-21) for the flagged accounts: one security (a public CUSIP, 922908736) appears in about 920 changed accounts and in about 920 rows coded `IC|RO`, whose detail text names a fund and an ETF share class; the other 34 changed securities are small. That is the issuer's reading, not a finding: you produce the counts, and the words say what they show.

**The cell (`DB-b-244`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r121/p121_qty.py` (your criterion; every definition and every recounted number is in its docstring, `counts` and `recount`); round 120's script `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~192/balance_lag_read_r120.py` (how the flagged accounts and the custodian position source are read: copy what you need into YOUR script, never import or edit it); `data/assets/scripts/gold/irpt_reporting/sources.json` (the entry carrying `positions_prefix`, `transactions_prefix`, `account_column`, `cash_code_column`, `inkind_code_value`, `detail_column`: read the bucket and prefixes FROM it, never type them); the CRO classification table `org/tier1_exec/4.0.0_SA_CRO/deliverables/SCHWAB_TRANSACTION_CODE_CLASSIFICATION_20260811.json` (a list of rows with `tr_cd`, `sb_cd`, `rule`, `category`, `desc`); `lib/opal_naming.py`.
2. **Read** (GET and LIST only): the `GRADED_DISAGREED` accounts of the 49 Financial `account_return_daily` partition of 2026-04-21 (the address from `address()`); the custodian `dim_position` partitions of 2026-04-20 and 2026-04-21 (columns `account_id, cusip, ticker_symbol, quantity_settled_unsettled`); the custodian `fact_trn` partition of 2026-04-21 (columns `account_id, cusip, ticker_symbol, tr_cd, sb_cd`, and `transaction_detail_description` for the words only).
3. **The numbers**, exactly as the checker's docstring defines them: `pairs_changed`, `securities_changed`, `accounts_with_change`, `top_securities` (five), `top1_share`, `trn_rows`, `trn_accounts`, `by_code` (keyed `"tr_cd|sb_cd"`), `code_rules` (per key, the sorted distinct `rule` values of the CRO table rows with those codes), `same_day_row_pairs`, `changed_pairs_without_row`, `ic_by_security` (five). A security is the CUSIP, else the ticker; a pair held on one day only is changed.
4. **Event words and sources.** Beyond the counts: (a) for the security with the most changed accounts, read the `transaction_detail_description` text of its `fact_trn` rows (counts of distinct texts, the text itself is a fund name and may be quoted) and say in the words what the day's event looks like (a conversion, a transfer, a trade, a split: say only what the texts and codes support, and say what they do NOT settle); (b) look for a corporate-action or share-class-conversion SOURCE in the repo and the custodian prefixes you may read (`sources.json` entries, the classification table's rules named `corp-actions`, the Black Diamond or security-master surfaces the repo documents), and record `corporate_action_source` {`found` (boolean), `where` (the path or prefix when found, else ""), `words`}; do not guess a source that you did not open.
5. **Write your analysis as a tracked script** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~198/qty_change_read_r121.py` (no write call to AWS; names no other firm's place; writes ONLY a private file under your private folder).
6. **Record** `RD_QTY_CHANGE_0421_R121.json` in your folder with EXACTLY these fields: `date` ("2026-04-21"), `prior_date` ("2026-04-20"), `accounts_flagged` (943, equal to the flow-guard record's `rows_graded_disagreed`), the step-3 numbers under their names, `corporate_action_source` (step 4b), `words` (one paragraph: which security accounts for most of the change and its share, which event codes carry it, how many changed pairs have no same-day row and what that leaves unexplained, whether a corporate-action source exists, and what a guard that read these rows would have to do; do NOT propose or make a guard change), `analysis` {`file`, `sha256`, `tracked` true}, `reads` {`s3_reads` (integer), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, `claim`, `files_in_repo` false, `served_values_changed` false, `pushed` false, `deployed` false. Every `claim` is one of `measured`, `inferred`, `held`, `absent`. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage`, `security`, `by_code` or `code_rules` field; no account id.

<criterion id="DB121-3-AC1" cell_refs="DB-b-244"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r121/p121_qty.py" . DB121-3-AC1</invocation><expect>DB121-3-AC1 PASS</expect></criterion>
`DB121-3-AC1` -- `RD_QTY_CHANGE_0421_R121.json` has exactly the form of step 6; `accounts_flagged` equals the flow-guard record's and the checker's recount; every number of step 3 EQUALS the checker's own recount from the custodian sources (read by the checker, GET only) to the unit, including the five top securities in order, the code counts and the rule words; `corporate_action_source` is well formed; the analysis script is tracked, hashed as recorded, names no other firm's place and holds no write call; zero writes, flags false, no long digit run outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB121-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the producer, every contract, module and test, round 120's script and record, the CRO table, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the 49 Financial irpt gold prefix `account_return_daily` (the 2026-04-21 partition and its manifest) derived by `lib/opal_naming.py address()`, and the custodian `dim_position` and `fact_trn` partitions named above, their bucket and prefixes read from `sources.json`. Writes: the repo files of the grant and the private folder. No put, copy or delete of any kind, no deploy, no push, no vendor call, no secret read, no read of another firm's place, no Terraform.
- **Client data.** Counts, dates, public security identifiers and words only; never an account id or a client value.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a partition cannot be read, record the source `absent` with the refusal named, file a BLOCKING row with counts and stop on that point; an unreadable source is never a zero. If a count differs from the checker's recount, report both numbers in a BLOCKING row; do not adjust either. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W198-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~198/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-244.quantity-read-2026-04-21-what-moved-the-quantities-of-the-flagged-accounts.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 119 (round 121, workstream B-49F), cell `DB-b-244`.
<owned_cells>DB-b-244</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB121-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~198/IRPT_DASHBD.TO-DB-b-244.quantity-read-2026-04-21-what-moved-the-quantities-of-the-flagged-accounts.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB121-3-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the numbers of step 3 in one line each (the top five securities and the code counts included); the words of step 6; reads and writes. Counts, public security identifiers and words only: no account id and no client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a tracked analysis script with a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; the S3 reads are GET and LIST of prefixes of one firm already read by the producer and the round-111 to round-120 drivers.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its recounts were dry-run by the issuer against the real custodian sources in 2.1 seconds.
lane: the <paths> block IS the grant.
</preflight>
