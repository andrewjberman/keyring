# TO IRPT_DASHBD.TO-DB-f-2101 -- the FWD-5 CONTRACT 0.5.1, ONE CELL: the Inflection counts restated on the LATEST SNAPSHOT (the Orion table is cumulative snapshots), the `inflection_table_shape` block, and the FINAL S6 ruling (both legs INTERNAL, reinvestment), the CTO's round-133 analysis and Addendum 2 of the round-134 analysis

<to_id>IRPT_DASHBD.TO-DB-f-2101</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~2101</issued_to>
<issued_by>2.0.0_SA_COO~F2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>LOCAL</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>135</round>
<workstream>~F2</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** F-SHIP (`~F2`) | **Ordered by:** 1.0.0_SA_CTO~DELL2: msg 9625 (every Orion silver `fact_transactions` partition is a cumulative snapshot; restate the counts on the latest snapshot; add the table shape), msg 9669 and Addendum 2 of `org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_F-SHIP_ROUND_134_20261016.md` @5d8adf5722 (S6 final: both legs INTERNAL; the earlier EXTERNAL ruling is WITHDRAWN), msg 9679 (the round-133 analysis: 0.5.1 changes `s6_status` and adds the 96-of-96 criterion; drop "S6 open") | **Rows:** IRPT_DASHBD-D2-W2101-S<k> | **Decomp cell:** `DB-f-2101` (`org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R135_F.md`) | **outcome_ref:** FWD-5 | **depends_on:** none

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-2101` (branch `wk-IRPT_DASHBD-2101`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2101/`. The folders `org/standards`, `lib`, `data/assets/scripts/gold/irpt_reporting`, `data/inf`, `infra/logic` and `org/tier1_exec` are materialized (if one is missing, run `git sparse-checkout add <folder>`: not a grant to edit). Never push; never commit the workspace `portal` gitlink. Offline only. **You have NO AWS in this order: make no AWS call of any kind.** No real client, household or account id, no client figure and no security name anywhere.

**Why.** The contract 0.5.0 states Inflection counts "over every partition". The Orion silver table is not a partition-per-day table: every partition is a CUMULATIVE SNAPSHOT of the whole history, so those counts were snapshot-weighted (about 140 times too large; the ratios held). The issuer re-measured every one on the LATEST snapshot and committed the records (read-only inputs below). 0.5.1 restates them, records the table's shape and the gold run domain, and states the S6 ruling as the CTO finally gave it.

**The inputs (read, never edited).** (a) The contract 0.5.0 on trunk (`org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json`), its generator `deliverables/0.9.0_WK_IRPT_DASHBD~2001/gen_transaction_contract_0_5_0.py` (copy it to `gen_transaction_contract_0_5_1.py` in YOUR folder and change it: never edit the contract by hand), `data/assets/scripts/gold/irpt_reporting/transaction_words.json`; (b) the issuer's records in `deliverables/2.0.0_SA_COO~F2/`: `R135_INFLECTION_SNAPSHOT_CENSUS.json`, `R135_INFLECTION_LATEST_PRICE_CENSUS.json`, `R135_INFLECTION_S6_SIGN_COMBINATIONS.json`, `R135_INFLECTION_S6_CASH_MOVE.json`, `R132_INFLECTION_CENSUS.json`, `R132_INFLECTION_PAIRING_CENSUS.json`, `R132_F49_BUSINESS_DATE_CENSUS.json` (copy values FROM the records, never retype a number); (c) the checker `deliverables/2.0.0_SA_COO~F2/checks/r135/p135_contract.py` (**read it first; it states every rule, its reason lines tell you what to fix; it has a `--selftest`**).

**The cell (`DB-f-2101`), in this order; commit after step 2.**

1. **Generator** `gen_transaction_contract_0_5_1.py` writes the contract AND `transaction_words.json`. Output: EXACTLY the top-level keys the checker's `KEYS` lists (0.5.0's keys plus the new `inflection_table_shape`). `contract_version` "0.5.1"; `supersedes` begins "0.5.0"; `authored_by` your serial. The 19 columns and the schema hash do NOT change.
2. **Changes, and only these:**
   - `round_132_censuses`: every Inflection count restated on the latest snapshot, `basis` "latest snapshot <date>" (the date is the record's), from the R135 records; `s6_status` `RULED_INTERNAL_REINVESTMENT`; `offsets_status` as the numbers give.
   - `row_filter.inflection` and `price_rule.inflection`: their counts restated on the same snapshot (the checker names each key); `offset_rule.candidate_rows` is the latest-snapshot figure only.
   - `s6_ruling` replaced by the FINAL ruling: `addendum_number` 2, `pin` "5d8adf5722", `withdrawn_pins` ["1881c0fc01", "a5475b2fdd"]; both legs `INTERNAL` (basis: reinvested inside the account, an equal-amount Buy or Income Reinvested line; claim `inferred`); the sign, cash and reinvestment evidence copied from the R135 records; `release_criterion` saying "N of N events carry an equal-amount line, printed, and any event without one stops the release" with the record's N; a `reason` saying both legs are INTERNAL because the cash drop was a purchase (a reinvestment) inside the account. **Do NOT write the EXTERNAL mapping; it was withdrawn.** The text "S6 open" appears nowhere.
   - `inflection_table_shape` (NEW): `kind` "cumulative_snapshot", the counts from the snapshot record, a `statement` (the table is cumulative snapshots; the earlier reads and counts were snapshot-weighted) and a `gold_run_domain` (a run reads ONE snapshot, the newest partition for the run day, emits lines by trade date, and never treats a partition as that day's transactions).
   - The words file keeps exactly its sections, each equal to the contract's; its `contract_version` is "0.5.1".
   - Unchanged: everything else in 0.5.0 (columns, sources, mapping rows, flow rules, `business_date_rule`, `served` false).
3. **Check.** Run `p135_contract.py . DBF135-1-AC1` until PASS. One mutant, temporary and reverted: write `s6_status` as `RULED_EXTERNAL_PAYOUT`; the checker must FAIL; say which reason line.

<criterion id="DBF135-1-AC1" cell_refs="DB-f-2101" judgment="false"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/checks/r135/p135_contract.py" . DBF135-1-AC1</invocation><expect>DBF135-1-AC1 PASS</expect></criterion>
`DBF135-1-AC1` -- the contract 0.5.1 in one verdict: its form (the keys, version 0.5.1 superseding 0.5.0, 19 columns, the unchanged schema hash), every binding of 0.5.0 that stands, the Inflection counts restated on the latest snapshot from the issuer's records, `inflection_table_shape`, the final S6 ruling (both legs INTERNAL, pin 5d8adf5722, the withdrawn pins, `RULED_INTERNAL_REINVESTMENT`, the N-of-N criterion), and the words file equal to the contract's sections. Base: FAIL (the contract is 0.5.0).

<expected_criteria>DBF135-1-AC1</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited (every producer and test, `lib/`, the censuses and records, the checker).
- **AWS: none.** **NOT WIRED.** Do not edit the handler or any Terraform.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If a checker rule and this order disagree, follow this order and file a row. A neighbouring test that pins a contract version outside the grant is reported as a row, not edited.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W2101-S<k>` (D2 is the device coordinate, never F2), with the real UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait. ASCII only in anything you write. If a commit is refused because the order is `complete`, stop and report.

<paths>
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2101/
org/standards/IRPT_DASHBD_ACCOUNT_TRANSACTION_CONTRACT.json
data/assets/scripts/gold/irpt_reporting/transaction_words.json
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-f-2101.fwd5-contract-0-5-1-inflection-counts-on-the-latest-snapshot-table-shape-and-final-s6.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP_R135_F.md</decomp_doc> round 135, workstream ~F2 (F-SHIP), cell `DB-f-2101`.
<owned_cells>DB-f-2101</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion id: DBF135-1-AC1 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~2101/IRPT_DASHBD.TO-DB-f-2101.fwd5-contract-0-5-1-inflection-counts-on-the-latest-snapshot-table-shape-and-final-s6.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DBF135-1-AC1 --governing-order <this order>` BEFORE the flip; pin each artifact row to the commit that carried it.
</proof_of_spec>

**REPORT:** your final message, once: the checker's last line; the contract's schema hash (must equal 0.5.0's); the mutant and the reason line it produced; anything off-task (as row ids). No real id, no client figure, no security name.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a contract and a data file in a branch; nothing is wired, served or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed; the worker has no AWS access in this order.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run as a tool; DBF135-1-AC1 FAILs at base and the checker's helpers are exercised by its self-test (64 arms).
lane: the <paths> block IS the grant.
</preflight>
