# TO IRPT_DASHBD.TO-DB-b-238 -- the BALANCE-LAG READ (round 120, workstream B-49F): the custodian balance source (`dim_balance`) against the custodian position source (`dim_position`) for the 943 accounts the guard disagreed on at 2026-04-21, over 2026-04-20 to 04-21, 04-21 to 04-22 and 04-20 to 04-22, and the same shape on the other five dates; which source moves with which, whether the positions' quantities changed, whether the next day catches up; counts only; nothing written

<to_id>IRPT_DASHBD.TO-DB-b-238</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~192</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>120</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 120 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-120 ANALYSIS (B-49F) section 2 ruling 2 and section 3 cell 2 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_120_20261015.md @5e358b0a8f`: "Yes to the balance READ: `dim_balance` (`net_mv_plus_cash`, `margin_balance`) against the positions for 2026-04-20, 04-21 and 04-22, for the 943 accounts. It asks which partition lags and by how much, whether 04-22 catches up, and whether any of the other five dates has the same shape. Counts and shares only. No repair") | **Rows:** IRPT_DASHBD-D2-W192-S<k> | **Decomp cell:** `DB-b-238` (decomposition section 118) | **outcome_ref:** FWD-2, FWD-21 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-192` (branch `wk-IRPT_DASHBD-192`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~192/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~192/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.**

**Why.** Round 119 found that on 2026-04-21 the position-based price return agrees with the holdings gold for 894 of 929 flagged accounts and with the account value for none (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~190/RD_PRICE_READ_0421_R119.json`). The issuer's own recount of the custodian sources suggests the answer is not a lag of one source: the balance file's positions component (`net_mv_positions`) and the position file's own market value agree with EACH OTHER for about 927 of 929 accounts on that interval, both disagree with the price-only return at the previous day's quantities for all but about 10, and the quantities of every flagged account changed between 04-20 and 04-21 (a rebalance day for the cohort); on 04-21 to 04-22 all the figures agree again. This cell makes that a record the checker recounts to the unit, and answers the CTO's three questions. A READ: nothing is changed, deployed or written outside your folder; any repair is a later round's packet under a never-widen pair.

**The cell (`DB-b-238`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r120/p120_balance.py` (your criterion; the definitions R, dP, dB, dT, Q and the six counts are in its docstring and `interval_counts`, and the checker recomputes the three intervals to the unit); round 119's record and script `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~190/RD_PRICE_READ_0421_R119.json` and `price_read_0421_r119.py` (how the flagged accounts, the custodian position source and the manifest tolerance are read: copy what you need into YOUR script, never import or edit it); `data/assets/scripts/gold/irpt_reporting/sources.json` (the entry carrying `positions_prefix` and `balance_prefix`: read the bucket and both prefixes FROM it, never type them); `lib/opal_naming.py`.
2. **The flagged accounts** are the `GRADED_DISAGREED` accounts of the 49 Financial `account_return_daily` partition of 2026-04-21 (address from `address()`); the tolerance is the 2026-04-21 manifest's `thresholds.tolerance`. Read ONLY: the `dim_position` and `dim_balance` partitions of `date=2026-04-20`, `2026-04-21` and `2026-04-22` (columns: position `account_id, cusip, ticker_symbol, quantity_settled_unsettled, market_value_settled_unsettled, closing_price`; balance `account_id, net_mv_positions, net_mv_plus_cash, margin_balance`), and, for the five other dates, the `dim_position` and `dim_balance` partitions of that date and of its previous trading day (`lib/trading_calendar.py prev_trading_day`) and the `account_return_daily` partition of that date for its flagged set.
3. **The three intervals** (04-20 to 04-21, 04-21 to 04-22, 04-20 to 04-22): the six counts of the checker's docstring, exactly as defined there (`accounts`, `balance_positions_agrees_position_mv`, `position_mv_agrees_price_return`, `balance_positions_agrees_price_return`, `balance_total_agrees_balance_positions`, `accounts_with_quantity_change`).
4. **The other five dates** (2026-07-02, 2026-10-13, 2026-09-22, 2026-10-06, 2026-09-16; in that order): for each, the interval from its previous trading day to it over its own flagged accounts: `accounts_flagged`, `accounts` (those countable), `balance_positions_agrees_position_mv`, `position_mv_agrees_price_return` (the same definitions; the checker grades these for form and bounds, not by recount).
5. **Words.** In one paragraph say what the three intervals show: which sources agree with each other on 2026-04-21, which does not, whether the quantities changed, whether 04-22 restores the agreement, and whether the other five dates have the same shape. Say nothing about a repair.
6. **Write your analysis as a tracked script** `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~192/balance_lag_read_r120.py` (no write call to AWS; names no other firm's place; writes ONLY a private file under your private folder).
7. **Record** `RD_BALANCE_LAG_R120.json` in your folder, counts, dates and words only, with EXACTLY these fields: `date` ("2026-04-21"), `accounts_flagged` (the flagged accounts of 2026-04-21: 943), `tolerance` (a float, the manifest's), `intervals` (a list of exactly 3 in the order of step 3, each {`from`, `to`, `accounts`, `balance_positions_agrees_position_mv`, `position_mv_agrees_price_return`, `balance_positions_agrees_price_return`, `balance_total_agrees_balance_positions`, `accounts_with_quantity_change`, `claim`}), `other_dates` (a list of exactly 5 in the order of step 4, each {`date`, `prior_date`, `accounts_flagged`, `accounts`, `balance_positions_agrees_position_mv`, `position_mv_agrees_price_return`, `claim`}), `source` {`file` ("data/assets/scripts/gold/irpt_reporting/sources.json"), `words` (which entry and which prefixes)}, `words` (step 5), `analysis` {`file` "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~192/balance_lag_read_r120.py", `sha256`, `tracked` true}, `reads` {`s3_reads` (integer), `s3_writes` 0, `dynamodb_writes` 0, `vendor_calls` 0, `secret_reads` 0}, `claim`, `files_in_repo` false, `served_values_changed` false, `pushed` false, `deployed` false. Every `claim` is one of `measured`, `inferred`, `held`, `absent`. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256` or `vintage` field; no account id; no client value.

<criterion id="DB120-2-AC1" cell_refs="DB-b-238"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r120/p120_balance.py" . DB120-2-AC1</invocation><expect>DB120-2-AC1 PASS</expect></criterion>
`DB120-2-AC1` -- `RD_BALANCE_LAG_R120.json` has exactly the form of step 7; `accounts_flagged` equals the flow-guard record's GRADED_DISAGREED rows of 2026-04-21 and the checker's own recount; the tolerance equals the manifest's; each of the three intervals' six counts EQUALS the checker's own recount from the custodian sources (read by the checker, GET only) to the unit and none exceeds its accounts; the five other dates have the right order, a prior date before the date and counts within their bounds; the analysis script is tracked, hashed as recorded, names no other firm's place and holds no write call; every claim is in the four-word set; zero writes, no push or deploy flags, and no run of 8 or more digits outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB120-2-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited, including the producer, every contract, module and test, round 119's script and record, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files; the S3 LIST and GET of the 49 Financial irpt gold prefix `account_return_daily` (the partitions of the six dates, one manifest) derived by `lib/opal_naming.py address()`, and the custodian `dim_position` and `dim_balance` partitions the dates above name, their bucket and prefixes read from `sources.json`. Writes: the repo files of the grant and the private folder. No put, copy or delete of any kind, no deploy, no push, no vendor call, no secret read, no read of another firm's place, no Terraform.
- **Client data.** Counts, dates, hashes and words only; never an account id or a client value.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a partition cannot be read, record the source `absent` with the refusal named, file a BLOCKING row with counts and stop on that point; an unreadable source is never a zero. If an interval's counts differ from the checker's recount, report both numbers in a BLOCKING row; do not adjust either. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W192-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~192/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-238.balance-lag-read-2026-04-20-to-22-custodian-balance-against-positions.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 118 (round 120, workstream B-49F), cell `DB-b-238`.
<owned_cells>DB-b-238</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB120-2-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~192/IRPT_DASHBD.TO-DB-b-238.balance-lag-read-2026-04-20-to-22-custodian-balance-against-positions.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB120-2-AC1` BEFORE the flip; pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: the criterion's last line; for each interval the six counts; the other five dates in one line each; the words of step 5; reads and writes. Counts, dates and words only: no account id and no client value.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a read and a tracked analysis script with a record in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the S3 reads are GET and LIST of prefixes of one firm already read by the producer and the round-111 to round-119 drivers.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms for each clause); its recount was dry-run by the issuer against the real custodian sources in 4.6 seconds.
lane: the <paths> block IS the grant.
</preflight>
