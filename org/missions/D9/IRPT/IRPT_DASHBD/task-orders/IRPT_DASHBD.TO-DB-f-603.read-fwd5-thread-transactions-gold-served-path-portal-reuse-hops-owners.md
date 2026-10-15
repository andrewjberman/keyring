# TO IRPT_DASHBD.TO-DB-f-603 -- the FWD-5 THREAD READ: where the transactions thread stands (a gold table `account_transaction` and its contract, the custodian sources, any served path), what the portal already holds for transactions (the page, the filter, the sort, the export), the hops from the custodian's transactions to a browse-filter-sort-export section with an owner and a risk class each, and a proposed served shape; a read, nothing written

<to_id>IRPT_DASHBD.TO-DB-f-603</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~603</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>119</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2, the parallelization ruling (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_RULING_DELL2_IRPT_PARALLELIZE_WORKSTREAM_ASSIGNMENTS_20261015.md`, Move 2: `~F2` takes FWD-3 and then FWD-5, "transactions browse, filter, sort, export"), on Andrew's go | **Rows:** IRPT_DASHBD-D2-W603-S<k> | **Decomp cell:** `DB-f-603` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R119_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-603` (branch `wk-IRPT_DASHBD-603`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~603/`. Never push; never commit the workspace `portal` gitlink (you have no portal work). This is a READ of repository files and git history: no AWS call of any kind, no network, no vendor call, no secret read. Any real client, household or account id and any client figure is never written in the repo, a row or your report.

**Why.** FWD-5 reads: "A person browses the transactions for any account and window, filters, sorts and exports them. ACCEPT: date, asset, action, type, symbol, units, price, amount and custodian are shown in Opal's own words for the action and type, not the custodian's codes; a long window scrolls without the page stalling" (`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`, FWD-5 and the surface row S11: gold `account_transaction` and its paged platinum files, "unmeasured"). Nobody has started it. What the issuer measured at the cut: a text search of the repository for `account_transaction` finds no contract file under `org/standards/` and no producer under `data/assets/scripts/gold/irpt_reporting/` (only an Inflection transactions pull script, the sample builders' mentions and the PRD), while the sister tables have contracts and producers. This cell finds out exactly where the thread stands and what is missing between a custodian's transactions and a transactions section.

**The cell (`DB-f-603`).**
1. **The gold table.** Is there a contract for `account_transaction` (look under `org/standards/` for `IRPT_DASHBD_*_CONTRACT.json` names; use `comp-find --files '<term>' <folder> --limit 20`, never `head` a census) and a producer or builder? Read the PRD's C-SHAPE row for the eight tables (it names `account_transaction`) and its columns if stated. Answer `applied` (true or false: is any object of this table written) with words and a claim; where only the cloud could answer, the claim is `absent`, the words say what live read would settle it and who owns it (no AWS call by you).
2. **The sources.** The transactions the portal and the pipelines hold today for the three firms: the 49 Financial silver `fact_trn` (the brief `docs/briefs/irpt-holdings-basis-silver-inventory-brief-20260928.md` and the adapter `data/assets/scripts/gold/irpt_reporting/`), Cottonwood's and Inflection's pulls (`data/inf/manual_api/pull_inflection_transactions_rest.py`, the Cottonwood reader). Record the producer file and the line that reads a transaction source (the `producer` field), and in words what the custodian's action and type codes are and where Opal's own vocabulary for them lives or does not (the PRD says "Opal's own words, not the custodian's codes").
3. **The served path.** Does any served file or route carry transactions today (the reporting read route, the publisher, any transactions endpoint of the portal's API client `portal/src/api/endpoints/investor-reporting.ts`)? Record the file and line of the smallest existing route to extend (`served_path`), or say `absent` with what you searched.
4. **The portal's reuse.** What the portal already holds for transactions: a Transactions or Activity tab, a table with a filter, a sort, an export (read `portal/src/pages/InvestorReporting/` file names and the `tabs/` folders; do not read client data). Record the file and the line of the best existing table/filter/sort/export component to reuse (`portal_reuse`) and say what can be reused unchanged.
5. **The hops.** List the hops that carry one account's transactions from the custodian to a browse-filter-sort-export section, in order, each with: `hop` (1, 2, 3 ...), `what` (words), `owner` (a serial or workstream from the files: `2.0.0_SA_COO~D2` for the contract and gold, the route and publisher owner of the serve path, an AE seat for an apply, `2.0.0_SA_COO~F2` for the portal; `UNOWNED` where none can be named), `risk` (`LOCAL` for a code or test change, `SERVED` for a served data path or a PROD promotion, `WORLD` for a deploy, a grant, a key or a schedule) and `exists_today` (true or false). At least 4 hops; the first is the custodian source and the last is the portal section.
6. **A proposed served shape.** One proposal for what the page reads: a paged file per account and window, rows with the PRD's columns (date, asset, action, type, symbol, units, price, amount, custodian) in Opal's own words, with a page size and a total count so a long window scrolls without stalling. State the field names as a list and the words of why this shape lets the page filter, sort and export without a server call per keystroke.
7. **Record** `RD_FWD5_THREAD_R119.json` in your folder with EXACTLY these fields: `as_of` (ISO date of the read); `gold_table` {`applied`, `words`, `claim`}; `producer` {`file`, `line`, `words`, `claim`}; `series_contract` {`carries_class_keys` (here: true if any served file carries transactions, else false), `words`, `claim`}; `served_path` {`file`, `line`, `words`, `claim`}; `portal_reuse` {`file`, `line`, `words`, `claim`}; `proposed_shape` {`words`, `fields` (a non-empty list of field names)}; `hops` (the list of step 5); `reads` {`s3_reads` 0, `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}; and the false flags `files_in_repo`, `served_values_changed`, `pushed`, `deployed`. (The field `series_contract.carries_class_keys` keeps its name from the sister cell's form; it means "a served file carries transactions today".) Every `claim` is one of `measured`, `inferred`, `held`, `absent` (not found or only the cloud could say, with the reason in `words`; never invented). A `file` is an existing repo path with an INTEGER `line` whose text holds the thing the record says it holds (the checker reads that line: the producer line must hold `account_transaction`, `transaction`, `fact_trn` is NOT enough alone so include the word `transaction` in the line you cite; the served-path line `manifest`, `series`, `summary`, `route`, `publish` or `class`; the portal-reuse line one of `asset`, `class`, `order`, `color`, `transaction`, `action`, `filter`, `sort` or `export`). No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage` or `path_template` field.

<criterion id="DBF119-3-AC1" cell_refs="DB-f-603"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r119/p119_fwd3.py" . DBF119-3-AC1</invocation><expect>DBF119-3-AC1 PASS</expect></criterion>
`DBF119-3-AC1` -- `RD_FWD5_THREAD_R119.json` has exactly the form of step 7; each cited file exists and each cited line holds the token class its field names; `hops` has at least 4 entries numbered from 1, each with an owner, a risk class in the set and a boolean `exists_today`; `gold_table` carries a boolean `applied` and words; every claim is in the four-word set; the reads block is all zero, the four flags are false and no run of 8 or more digits stands outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DBF119-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: every code file, every contract, the portal, the issuer's check.
- **A READ.** Nothing is deployed, applied, published, pushed or changed outside your folder; no AWS call; no network. Where only the cloud could answer a question, the answer is `absent` with that reason, never a guess.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a thing is not found, the record says `absent` and what you searched; a zero is never read as "does not exist" without the tool's printed denominator beside it. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W603-S<k>` (D2 is the device coordinate, never F2), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~603/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-603.read-fwd5-thread-transactions-gold-served-path-portal-reuse-hops-owners.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R119_F.md</decomp_doc> round 119, workstream ~F2 (F-SHIP), cell `DB-f-603`.
<owned_cells>DB-f-603</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DBF119-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~603/IRPT_DASHBD.TO-DB-f-603.read-fwd5-thread-transactions-gold-served-path-portal-reuse-hops-owners.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF119-3-AC1` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; whether the gold table exists and is applied (the evidence or why `absent`); the sources and the vocabulary question; the smallest route to extend; what the portal can reuse; the hops in order with owner, risk and `exists_today`; the proposed shape's field names; anything off-task (as row ids). No real id and no client figure.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no AWS call and no grant is changed.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; the cell reads the route's code.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF119-3-AC1 FAILS at base (no record) and the record form is exercised by the checker's self-test.
lane: the <paths> block IS the grant.
</preflight>
