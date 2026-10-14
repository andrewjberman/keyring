# TO IRPT_DASHBD.TO-DB-b-212 -- the TWO READS that decide Inflection's coverage words: whether Orion's returns include dividends (measured against one account's transactions) and whether Eclipse tax lots are populated (else the lots members carry NO_LOTS in plain words); counts and words only; nothing written

<to_id>IRPT_DASHBD.TO-DB-b-212</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~172</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>108</round>
<workstream>B</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** 1.0.0_SA_CTO~DELL2, ROUND-108 ANALYSIS section 3 cell 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_ROUND_108_20261014.md`; PRD line 294: "the Inflection adapter (lots `NO_LOTS` until Eclipse tax lots are shown populated; whether Orion's returns include dividends is measured, not assumed)") | **Rows:** IRPT_DASHBD-D2-W172-S<k> | **Decomp cell:** `DB-b-212` (decomposition section 110) | **outcome_ref:** FWD-2 | **depends_on:** none.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-172` (branch `wk-IRPT_DASHBD-172`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~172/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, hashes and words only in the repo, a row or your report; an account is named only by the sha256 of its id, and no figure is recorded.

**Why.** Inflection's reports will read returns and lots from Orion and Eclipse, and two facts decide the words a client sees: (1) if Orion's performance figure does NOT include dividends, a return the report prints would understate what the client earned, so the report must say so or compute its own; (2) if Eclipse tax lots are not populated, the report's lot-based members (realized and unrealized gain-loss) cannot print and must carry `NO_LOTS` with plain words, not a bare absence. The PRD says both are measured, never assumed. Your cell measures them, read-only, and records the answers.

**The grant of the S3 reads (BY PREFIX).** You may LIST and GET under `s3://opal-data-assets/orion/inflection/` and `s3://opal-data-assets/eclipse/inflection/` and nowhere else. The Orion master prefix `s3://opal-data-assets/orion/4698/` is another place and is NOT granted; no other firm's bucket or prefix is read, named or written (the cross-firm rule). No put, copy or delete of any kind. A denial is recorded verbatim, not retried by another route.

**The cell (`DB-b-212`).**
1. **Read first.** The PRD around line 294 and the sections on coverage (`org/missions/D9/IRPT/IRPT_DASHBD/prd/IRPT_DASHBD_PRD.md`: C-COVERAGE, C-ADAPTERS), the account_dim contract's coverage vocabulary `org/standards/IRPT_DASHBD_ACCOUNT_DIM_CONTRACT.json` (`NO_LOTS`, `FULL`, `PARTIAL_HISTORY`...), and the issuer's check file `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r108/p108_round108.py` (your criterion: read `check_reads`). Your sibling worker `~171` builds the Inflection account_dim adapter in parallel; you do not depend on it and must not edit its files.
2. **Read A: do Orion's returns include dividends?** Under `s3://opal-data-assets/orion/inflection/silver/` the tables are `fact_assets`, `fact_performance`, `fact_positions` and `fact_transactions` (LIST, then GET the newest partition or the partitions you need). Choose ONE account by this deterministic rule: among the accounts with dividend or income transactions in `fact_transactions` (find the transaction-type column that marks dividends and income), the account whose sha256 of its account id (utf-8, hex digest) sorts lowest. Measure, for a window of that account that both tables cover: the return Orion's performance table reports; the return you compute from the account's market values and flows WITHOUT its dividend and income transactions; and the return you compute WITH them. The answer is `YES` when the reported return matches the with-dividends figure and not the without figure (within a tolerance you state in `basis_words`), `NO` when it matches the without figure and not the with figure, and `NOT_ESTABLISHED` when the data cannot tell them apart (for example the account's dividends are too small to separate them, or a needed table or column is absent): `NOT_ESTABLISHED` is an honest answer, never a guess. Record the method in words, the number of transactions you checked, the number of dividend flows among them, and the basis in words (no figure, no percentage). The account is named ONLY by `account_ref_sha256` (the hex digest) and a short non-identifying `account_ref` word such as "the first account by hash".
3. **Read B: are Eclipse tax lots populated?** Under `s3://opal-data-assets/eclipse/inflection/silver/` the tables are `fact_model_composition`, `fact_models`, `fact_portfolios_full` and `fact_portfolios_simple` (and `reconstructed/` and `meta/` hold other material: look, do not assume). Inspect each table's columns and rows for LOT-LEVEL fields: a tax-lot identifier, an acquisition or open date per lot, a per-lot quantity, a per-lot cost basis. Count the rows that carry any such field (non-null). `populated` is true only when rows carry them in earnest (state the threshold in words in `lots_words` or the record's method); when it is false, name `NO_LOTS` as the coverage member and give `lots_words`: ONE plain sentence a client could read ("Lot-level detail is not available for this account yet."), with no code token in it.
4. **The read script.** Put your read code in ONE file in your folder, `read_coverage.py`, tracked, run with `python -I`, whose every `s3://` literal sits under a granted prefix and that holds no write-call name (`put_object`, `upload_file`, `copy_object`, `delete_object`...) and names no other firm. It prints counts and words only.
5. **Record** `COVERAGE_READS_R108.json` in your folder with exactly: `orion_dividends` {`answer` ("YES", "NO" or "NOT_ESTABLISHED"), `method` (words), `transactions_checked` (integer), `dividend_flows` (integer), `basis_words` (words, no figure), `account_ref` (a short non-identifying word), `account_ref_sha256` (the hex digest of the account's id)}; `eclipse_lots` {`populated` (bool), `tables_checked` (a list of the Eclipse table names you inspected), `rows_with_lot_fields` (integer), and, when `populated` is false, `coverage_member` ("NO_LOTS") and `lots_words` (one plain sentence with no code token)}; `script` {`file`, `sha256`, `tracked` true}; `reads` {`vendor_calls` 0, `s3_writes` 0, `dynamodb_writes` 0, `secret_reads` 0, `s3_reads` (integer)}; `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. Counts, hashes and words only: no account number or name, no dollar figure or percentage; no run of 8 or more digits except in `account_ref_sha256`, a `sha256` value or a `file` field.

<criterion id="DB108-2-AC1" cell_refs="DB-b-212"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r108/p108_round108.py" . DB108-2-AC1</invocation><expect>DB108-2-AC1 PASS</expect></criterion>
`DB108-2-AC1` -- `orion_dividends.answer` is YES, NO or NOT_ESTABLISHED, and an answer other than NOT_ESTABLISHED rests on transactions actually checked (a positive count); the method, the basis and the counts are present; the account is named only by a sha256; `eclipse_lots` states populated as a boolean with the tables inspected and the count of rows that carry lot fields, and when not populated names NO_LOTS and carries one plain sentence with no code token in it; the read script is a tracked file hashed as recorded, every `s3://` literal in it sits under a granted Inflection prefix, it holds no write-call name and names no other firm; nothing is written; no push or deploy. Base: FAIL (no record).

<expected_criteria>DB108-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including every contract, every adapter, every portal file and the issuer's check files.
- **Reads and writes.** Reads: repo files and the S3 LIST and GET of the two granted prefixes named above. Writes: the repo files of the grant (and any private scratch under `C:/dev/_irpt_private_evidence_20261009/`). No write to AWS of any kind, no deploy, no push, no vendor call, no secret read, no read of any other firm's place.
- **Client data.** The silver is client data: counts, hashes and words only in the repo, a row or your report; no dollar figure, percentage or account identifier.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a table you need is absent or unreadable, say so in `basis_words` or `lots_words` and answer `NOT_ESTABLISHED` or `populated` false: never infer. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W172-S<k>`, with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~172/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-212.inflection-coverage-reads-orion-dividends-eclipse-lots.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 110 (round 108), cell `DB-b-212`.
<owned_cells>DB-b-212</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB108-2-AC1. The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~172/IRPT_DASHBD.TO-DB-b-212.inflection-coverage-reads-orion-dividends-eclipse-lots.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB108-2-AC1` BEFORE the flip.
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the Orion answer (YES, NO or NOT_ESTABLISHED) with the method in words, the transactions checked and the dividend flows among them; whether Eclipse lots are populated, which tables you inspected, how many rows carry lot fields and (if not) the plain sentence; the prefixes you read and the number of S3 reads; row ids. Counts and words only; no account number, name, dollar figure or percentage.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read script and a record; nothing is read by served code, wired or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: read-only S3 LIST and GET of two Inflection-scoped prefixes of the monolith bucket the estate's other adapters already read; no new principal or grant.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; DB108-2-AC1 FAILS at base (no record) and the checker's helpers are exercised by its 6-arm self-test.
lane: the <paths> block IS the grant.
</preflight>
