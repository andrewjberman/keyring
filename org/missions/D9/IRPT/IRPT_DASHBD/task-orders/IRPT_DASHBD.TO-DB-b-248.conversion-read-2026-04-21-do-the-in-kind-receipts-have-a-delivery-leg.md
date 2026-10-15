# TO IRPT_DASHBD.TO-DB-b-248 -- the 2026-04-21 CONVERSION READ (round 122, workstream B-49F): for each of the in-kind receipts of the leading security (the `IC|RO` rows on CUSIP 922908736), is there a same-day DELIVERY of another security in the same account of matching value? receipts, position legs and their match within 1 and 5 percent, the other in-kind rows, the legs by security, the unexplained changed pairs by security, and the verdict EXCHANGE_LEGS_PRESENT, CONVERSION_LEG_ABSENT or MIXED; counts only; nothing written and no guard change

<to_id>IRPT_DASHBD.TO-DB-b-248</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~202</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>122</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 122 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-122 ANALYSIS (B-49F) section 2 ruling 2 and section 3 cell 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_122_20261015.md @e690365741`: "For each of the 920 in-kind receipts, is there a same-day DELIVERY of the fund's mutual-fund share class in the same account, of matching value within tolerance? If yes, the pair is an internal EXCHANGE ... If the delivery leg is missing from the source, that is the custodian feed's gap, and the days stay FLOW_UNRECONCILED with the reason CONVERSION_LEG_ABSENT in words. The 12 unexplained pairs are listed by security, as counts") | **Rows:** IRPT_DASHBD-D2-W202-S<k> | **Decomp cell:** `DB-b-248` (decomposition section 120) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-202` (branch `wk-IRPT_DASHBD-202`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~202/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~202/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Round 121 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~198/RD_QTY_CHANGE_0421_R121.json`) found that on 2026-04-21 one security (CUSIP 922908736, ticker VUG) accounts for 920 of the 937 changed accounts, each with one same-day `IC|RO` row whose text names an ETF share class, and that the quantity of the security ROSE in all 920. A share-class conversion would also DELIVER the mutual-fund shares out of the same account the same day; if the custodian feed carries that leg, the pair is an internal exchange and the guard's disagreement is an artifact of reading only the receipt; if it does not, the feed is missing the leg. The issuer's first look: only about 30 of the 920 accounts show ANY quantity fall in another security that day. This cell makes the answer a record the checker recounts. A READ: nothing is written; no guard change is proposed or made.

**The cell (`DB-b-248`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r122/p122_conv.py` (your criterion; every definition and every recounted number is in its docstring, `counts` and `recount`); round 121's script and record `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~198/qty_change_read_r121.py` and `RD_QTY_CHANGE_0421_R121.json` (how the flagged accounts, positions and transactions are read: copy what you need into YOUR script, never import or edit it); `data/assets/scripts/gold/irpt_reporting/sources.json` (the entry with `positions_prefix`, `transactions_prefix`, the account and code columns: read the bucket and prefixes FROM it, never type them); `lib/opal_naming.py`.
2. **Read** (GET and LIST only): the `GRADED_DISAGREED` accounts of the 49 Financial `account_return_daily` partition of 2026-04-21; the custodian `dim_position` partitions of 2026-04-20 and 2026-04-21 (columns `account_id, cusip, ticker_symbol, quantity_settled_unsettled, closing_price`); the custodian `fact_trn` partition of 2026-04-21 (columns `account_id, cusip, ticker_symbol, tr_cd, sb_cd, quantity, price`, and `transaction_detail_description` for the words only).
3. **The numbers**, exactly as the checker's docstring defines them (the leading security is the first entry of round 121's `top_securities`): `receipts`, `receipts_with_leg`, `matched_1pct`, `matched_5pct`, `receipts_with_other_ic_row`, `legs_by_security` (five), `unexplained_by_security` (all of them), and `verdict` by the stated rule. Money is used to compare values inside your script; NO dollar amount is recorded anywhere, only counts.
4. **Words** (the record's `words`, one paragraph): the verdict in plain terms; what the legs by security are (names are public security identifiers; a fund name from the detail text may be quoted); whether the feed shows the mutual-fund shares anywhere on 2026-04-20 in these accounts (a count of accounts holding any security with a mutual-fund or fund-company name in the position file's description columns, if the file has them, else say it does not); what each verdict would mean for the guard (`FLOW_UNRECONCILED` with reason `CONVERSION_LEG_ABSENT`, or an exchange rule under a never-widen pair that counts the served delta per account-day); and the unexplained pairs by security. Do NOT propose or make any change.
5. **Write your analysis as a tracked script** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~202/conversion_read_r122.py` (no write call to AWS; names no other firm's place; writes ONLY a private file under your private folder).
6. **Record** `RD_CONVERSION_READ_R122.json` in your folder with EXACTLY these fields: `date` ("2026-04-21"), `prior_date` ("2026-04-20"), `security` (the leading security), `tolerance_primary` (0.01), `tolerance_secondary` (0.05), the step-3 numbers under their names, `words`, `analysis` {`file`, `sha256`, `tracked` true}, `reads` {`s3_reads` (integer), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, `claim`, `files_in_repo` false, `served_values_changed` false, `pushed` false, `deployed` false. Every `claim` is one of `measured`, `inferred`, `held`, `absent`. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage`, `security`, `legs_by_security` or `unexplained_by_security` field; no account id.

<criterion id="DB122-3-AC1" cell_refs="DB-b-248"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r122/p122_conv.py" . DB122-3-AC1</invocation><expect>DB122-3-AC1 PASS</expect></criterion>
`DB122-3-AC1` -- `RD_CONVERSION_READ_R122.json` has exactly the form of step 6; `security` equals round 121's leading security; every number of step 3 EQUALS the checker's own recount from the custodian sources (read by the checker, GET only) to the unit, the verdict included; the analysis script is tracked, hashed as recorded, names no other firm's place and holds no write call; zero writes, flags false, no long digit run outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB122-3-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the producer, every contract, module and test, round 121's script and record, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the 49 Financial irpt gold prefix `account_return_daily` (the 2026-04-21 partition) derived by `lib/opal_naming.py address()`, and the custodian `dim_position` and `fact_trn` partitions named above, their bucket and prefixes read from `sources.json`. Writes: the repo files of the grant and the private folder. No put, copy or delete of any kind, no deploy, no push, no vendor call, no secret read, no read of another firm's place, no Terraform.
- **Client data.** Counts, dates, public security identifiers and words only; never an account id or a client value, and no dollar amount.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a partition cannot be read, record the source `absent` with the refusal named, file a BLOCKING row with counts and stop on that point. If a count differs from the checker's recount, report both numbers in a BLOCKING row; do not adjust either. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W202-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~202/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-248.conversion-read-2026-04-21-do-the-in-kind-receipts-have-a-delivery-leg.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 120 (round 122, workstream B-49F), cell `DB-b-248`.
<owned_cells>DB-b-248</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB122-3-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~202/IRPT_DASHBD.TO-DB-b-248.conversion-read-2026-04-21-do-the-in-kind-receipts-have-a-delivery-leg.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB122-3-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the numbers of step 3 in one line each; the verdict and the words of step 4; reads and writes. Counts, public security identifiers and words only: no account id, no client value and no dollar amount.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a tracked analysis script with a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; the S3 reads are GET and LIST of prefixes of one firm already read by the producer and the round-111 to round-121 drivers.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its recounts were dry-run by the issuer against the real custodian sources in 2.2 seconds.
lane: the <paths> block IS the grant.
</preflight>
