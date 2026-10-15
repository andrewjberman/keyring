# TO IRPT_DASHBD.TO-DB-b-251 -- the IN-KIND-AS-FLOW READ (round 123, workstream B-49F): do the 920 `IC|RO` receipts of CUSIP 922908736 on 2026-04-21, counted as external in-kind INFLOWS, reconcile the holdings guard within its tolerance? the counts that agree before and after, the improvement, the direction control (as outflows), where the rest fall, and the verdict; counts only; nothing written; no classification change is made or proposed

<to_id>IRPT_DASHBD.TO-DB-b-251</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~205</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>123</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 123 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-123 ANALYSIS (B-49F) section 2 ruling 2 and section 3 cell 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_123_20261015.md @1ffd4f5afb`: "With no exchange leg, the receipts may be EXTERNAL in-kind transfers into the account (an ACAT-style contribution), which the flow ledger should count as a flow. Read: for the 920 accounts, does adding each `IC|RO` receipt's market value as an external flow on 2026-04-21 reconcile the guard within its tolerance? Counts only. If it does, the classification of `IC|RO` ... is a DESIGN FORK: this seat asks the CRO for the estate's precedent. If it does not, `CONVERSION_LEG_ABSENT` stands") | **Rows:** IRPT_DASHBD-D2-W205-S<k> | **Decomp cell:** `DB-b-251` (decomposition section 121) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-205` (branch `wk-IRPT_DASHBD-205`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~205/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~205/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Round 122 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~202/RD_CONVERSION_READ_R122.json`) found no same-day delivery leg for the 920 in-kind receipts of CUSIP 922908736 (verdict CONVERSION_LEG_ABSENT). The producer (`data/assets/scripts/gold/irpt_reporting/account_return_daily.py`) classifies `IC|RO` under the CRO table's `corp-actions` rule and does not count it as an external flow; a flagged account's served `total_return_daily` is null and its guard state is GRADED_DISAGREED. If the receipts are really contributions in kind, the account's value rose by the receipt without a market move, and counting the receipt as an inflow in the producer's own return formula should bring the return back to the holdings price return. The issuer's first recount says it does for nearly all of them. This cell makes that a record the checker recounts. A READ: nothing is written; no classification, guard or served value is changed or proposed.

**The cell (`DB-b-251`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r123/p123_flow.py` (your criterion; every definition and every recounted number is in its docstring, `counts` and `recount`); the producer's return and guard code (`compute_range` around the single valuation chain, `guard_state_of`, the line that computes `_guard_diff`) so that you understand the formula the checker uses; round 122's script `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~202/conversion_read_r122.py` (how the receipts are read: copy what you need into YOUR script, never import or edit it); `data/assets/scripts/gold/irpt_reporting/sources.json`; `lib/opal_naming.py`.
2. **Read** (GET and LIST only): the 49 Financial `account_return_daily` partitions of 2026-04-20 and 2026-04-21 (columns `account_id, market_value_eod, external_flow, income_return, holdings_price_return, guard_state, carried_days`) and the 2026-04-21 manifest's `thresholds.tolerance`; the custodian `fact_trn` partition of 2026-04-21 (columns `account_id, cusip, ticker_symbol, tr_cd, sb_cd, quantity, price`).
3. **The numbers**, exactly as the checker's docstring defines them (the security is the first entry of round 121's `top_securities`): `receipt_accounts`, `cohort`, `agree_before`, `agree_after_inflow`, `agree_after_outflow`, `improved_after_inflow`, `diff_buckets_after_inflow` (the four counts of diff/tolerance: at most 1x, 2x, 10x, over 10x), and `verdict` by the stated rule. Money is used inside your script only; NO dollar amount is recorded, only counts.
4. **Words** (the record's `words`, one paragraph): the verdict in plain terms; what the direction control shows; where the accounts that do not reconcile fall (counts by bucket; do not look them up by identifier); what it means for the CTO's question (the receipts behave as external in-kind inflows; the `IC|RO` classification is then a design fork for the CRO) and what it does NOT show (that the transfers are ACAT contributions rather than a custodian's re-registration of the same holdings, which the feed cannot say). Do NOT propose or make any change.
5. **Write your analysis as a tracked script** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~205/inkind_flow_read_r123.py` (no write call to AWS; names no other firm's place; writes ONLY a private file under your private folder).
6. **Record** `RD_INKIND_FLOW_READ_R123.json` in your folder with EXACTLY these fields: `date` ("2026-04-21"), `prior_date` ("2026-04-20"), `security` (the leading security), `tolerance` (a float, the manifest's), `formula` (one line: the return formula you used), the step-3 numbers under their names, `words`, `analysis` {`file`, `sha256`, `tracked` true}, `reads` {`s3_reads` (integer), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, `claim`, `files_in_repo` false, `served_values_changed` false, `pushed` false, `deployed` false. Every `claim` is one of `measured`, `inferred`, `held`, `absent`. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage` or `security` field; no account id.

<criterion id="DB123-2-AC1" cell_refs="DB-b-251"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r123/p123_flow.py" . DB123-2-AC1</invocation><expect>DB123-2-AC1 PASS</expect></criterion>
`DB123-2-AC1` -- `RD_INKIND_FLOW_READ_R123.json` has exactly the form of step 6; `security` equals round 121's leading security; the tolerance equals the manifest's; every number of step 3 EQUALS the checker's own recount from the gold and the custodian transactions (read by the checker, GET only) to the unit, the verdict included; the analysis script is tracked, hashed as recorded, names no other firm's place and holds no write call; zero writes, flags false, no long digit run outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB123-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the producer, every contract, module and test, round 121's and 122's scripts and records, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the 49 Financial irpt gold prefix `account_return_daily` (two partitions and one manifest) derived by `lib/opal_naming.py address()`, and the custodian `fact_trn` partition named above, its bucket and prefix read from `sources.json`. Writes: the repo files of the grant and the private folder. No put, copy or delete of any kind, no deploy, no push, no vendor call, no secret read, no read of another firm's place, no Terraform.
- **Client data.** Counts, dates, public security identifiers and words only; never an account id or a client value, and no dollar amount.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a partition cannot be read, record the source `absent` with the refusal named, file a BLOCKING row with counts and stop on that point. If a count differs from the checker's recount, report both numbers in a BLOCKING row; do not adjust either. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W205-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~205/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-251.in-kind-receipts-as-external-flows-do-they-reconcile-the-04-21-guard.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 121 (round 123, workstream B-49F), cell `DB-b-251`.
<owned_cells>DB-b-251</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB123-2-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~205/IRPT_DASHBD.TO-DB-b-251.in-kind-receipts-as-external-flows-do-they-reconcile-the-04-21-guard.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB123-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; the numbers of step 3 in one line each; the verdict and the words of step 4; reads and writes. Counts, public security identifiers and words only: no account id, no client value and no dollar amount.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a tracked analysis script with a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; the S3 reads are GET and LIST of prefixes of one firm already read by the producer and the round-111 to round-122 drivers.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its recounts were dry-run by the issuer against the real gold and custodian sources in 1.6 seconds.
lane: the <paths> block IS the grant.
</preflight>
