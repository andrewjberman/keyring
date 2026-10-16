# TO IRPT_DASHBD.TO-DB-f-701 -- the FWD-5 FIELD AND CODE READ: for each of the three firms, the custody transaction source's columns (mapped to the PRD's date, asset, action, type, symbol, units, price, amount, custodian), the custodian's action and type code sets as the code and tracked records hold them, the brief's flow classes, and where an Opal vocabulary for action and type lives or does not; a read of code and tracked records, nothing written

<to_id>IRPT_DASHBD.TO-DB-f-701</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~701</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>120</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the round-119 analysis for F-SHIP ruling 3 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_119_20261016.md`: "FWD-5, transactions: Owner `~F2`, writing a NEW contract file (`IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json`; `~F2` is its sole writer) and its producer, from the custody transaction silver per firm. Its rule-24 record comes with any enum, and the cross-firm fence applies (per-firm prefixes only)") | **Rows:** IRPT_DASHBD-D2-W701-S<k> | **Decomp cell:** `DB-f-701` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R120_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-701` (branch `wk-IRPT_DASHBD-701`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~701/`. The folders `data/`, `infra/aws/lambda/investor-reporting/`, `docs/briefs/` and `org/critical_paths/` are materialized in your worktree for reading (if one is missing, run `git sparse-checkout add <folder>` for it: that is not a grant to edit). Never push; never commit the workspace `portal` gitlink. This is a READ of repository files and git history: no AWS call of any kind, no network, no vendor call, no secret read. Any real client, household or account id and any client figure is never written in the repo, a row or your report.

**Why.** FWD-5 (`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`): a person browses the transactions for any account and window, filters, sorts and exports them; ACCEPT: date, asset, action, type, symbol, units, price, amount and custodian are shown "in Opal's own words for the action and type, not the custodian's codes". There is no `account_transaction` contract and no producer. This seat is the contract's sole writer and must write it from what the three firms' custody transaction sources hold, with any enum under the taxonomy law (a value-enum proposal arrives with its four-postulate record and a word-boundary token census over a printed denominator). A first read (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~603/RD_FWD5_THREAD_R119.json`) found the sources and the gap; this cell builds the DENOMINATOR the contract needs: the fields and the code sets as the repository holds them.

**The cell (`DB-f-701`).**
1. **49 Financial.** Read the custody entry in `data/assets/scripts/gold/irpt_reporting/sources.json` (the transactions prefix), the register brief `docs/briefs/irpt-holdings-basis-silver-inventory-brief-20260928.md` (the `fact_trn` columns), and the code that reads a transaction (`data/assets/scripts/gold/irpt_reporting/account_class_daily.py`, `account_return_daily.py`, `account_activity_lots.py`: where `fact_trn` columns such as `tran_srcde`, `tr_cd`, `sb_cd` are read). Record the column list of the transaction source and, from the code and tracked files, every value of the custodian's transaction code fields that the code names or maps (action and type, with where each is named; a value named by a classification table, a map or a comment counts; use `comp-find --files '<term>' <folder> --limit 20`, never `head` a census, and print each denominator you cite).
2. **Cottonwood.** Read `data/assets/scripts/gold/irpt_reporting/adapters/cottonwood_bd_account_return_daily.py` (about line 79: `fact_transactions`) and the Black Diamond transaction type map the repository holds (`TYPE_CLASS` or its equivalent: find it with `comp-find --files 'TYPE_CLASS' data --limit 10`). Same record: columns and code sets.
3. **Inflection.** Read `data/inf/manual_api/pull_inflection_transactions_rest.py` and the Orion transaction fields it names. Same record.
4. **The brief's flow classes.** The register brief and the PRD name flow classes for transactions (the earlier read counted 7 in the brief against 4 in a flow map): read the brief and the flow map and record the count and the file and line of the list (`brief_flow_classes`).
5. **Opal's vocabulary home.** Say in words whether any file defines Opal's own words for a transaction's action and type (the PRD's ACCEPT), searching `org/standards/`, `docs/`, `portal/src/` (the Holdings and Transactions words) and the IRPT briefs; if none, say so with the denominator of what you searched (`opal_vocab_home`, claim `absent`).
6. **Record** `RD_FWD5_FIELDS_R120.json` in your folder with EXACTLY these fields: `as_of` (ISO date); `firms` (a list of exactly three objects, one per firm: `firm` ("49financial", "cottonwood" or "inflection"), `file` (an existing repo path), `line` (integer; the line that names the source's transaction fields or code fields: the line text must hold one of `transaction`, `trn`, `fact_`, `tran_`, `action` or `type`), `columns` (the list of column names of the transaction source, as the code or brief names them), `action_codes` (the list of the custodian's action code values the repository names, possibly empty with the reason in `vocabulary_where`), `type_codes` (the same for type), `vocabulary_where` (words: where the firm's code meanings live), `claim`); `brief_flow_classes` {`file`, `line`, `count` (integer), `claim`} (the line must hold `flow`, `class`, `action` or `type`); `opal_vocab_home` {`words`, `claim`}; `reads` {`s3_reads` 0, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}; and the false flags `files_in_repo`, `served_values_changed`, `pushed`, `deployed`. Every `claim` is one of `measured` (you read the line), `inferred`, `held`, `absent` (not found, with the reason in the words; never invented). Codes are values of a code field only: no account id, no client figure, no security name. No run of 8 or more digits outside a `path`, `file`, `key`, `where` or `vintage` field.

<criterion id="DBF120-1-AC1" cell_refs="DB-f-701"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r120/p120_reads.py" . DBF120-1-AC1</invocation><expect>DBF120-1-AC1 PASS</expect></criterion>
`DBF120-1-AC1` -- `RD_FWD5_FIELDS_R120.json` has exactly the form of step 6; each cited file exists and each cited line holds a token its field names; three firms are present, each with its column list and its two code lists (possibly empty with the reason in words) and a claim; the flow-class count is an integer; every claim is in the four-word set; the reads block is all zero, the four flags are false and no run of 8 or more digits stands outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DBF120-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **A READ.** Nothing is deployed, applied, published, pushed or changed outside your folder; no AWS call; no network. A value only the data could answer (a code the data holds and no file names) is `absent` with that reason, never a guess.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A zero is never read as "does not exist" without the tool's printed denominator beside it. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W701-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~701/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-701.read-fwd5-per-firm-transaction-fields-and-custodian-code-sets.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R120_F.md</decomp_doc> round 120, workstream ~F2 (F-SHIP), cell `DB-f-701`.
<owned_cells>DB-f-701</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF120-1-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~701/IRPT_DASHBD.TO-DB-f-701.read-fwd5-per-firm-transaction-fields-and-custodian-code-sets.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF120-1-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; per firm the column count and the two code-list lengths with where they live; the brief's flow-class count; whether an Opal vocabulary home exists; anything off-task (as row ids). No real id and no client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF120-1-AC1 FAILS at base (no record) and the record form is exercised by the checker's self-test.
lane: the <paths> block IS the grant.
</preflight>
