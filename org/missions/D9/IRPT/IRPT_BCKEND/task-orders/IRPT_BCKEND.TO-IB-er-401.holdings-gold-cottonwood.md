# TO IRPT_BCKEND.TO-IB-er-401 -- Holdings-basis gold for EVERY Cottonwood account, full history, manifest complete (PRD v0.19 rulings 1-9, 11; v0.20 rulings 13-17)

<to_id>IRPT_BCKEND.TO-IB-er-401</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.4.0_DS_ClientPlatform~E</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~E</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO RULING S200 (102669, PRD v0.21 ruling 18) for step 0; 1.0.0_SA_CTO ROUND-19 ANALYSIS section 6 item 1 ("then Inflection
and Cottonwood ... in that order (ruling 11)"); PRD ADDENDUM v0.19 rulings 1-9 and 11, v0.20 rulings 13-17 |
**Decomp cell:** `IB-er-401` (decomposition section 19) | **outcome_ref:** FWD-3 (COT) | **depends_on:** ~E round 3
(TO-IB-er-301, complete: the producer carries v0.20)

---

## WORKER FACE

### THE CELL

**STEP 0 FIRST -- PRD v0.21 ruling 18** (1.0.0_SA_CTO RULING S200, 102669, on 4.0.0_SA_CRO row S200 @131c55fcf1):
the trading day that FOLLOWS a NOT COMPUTABLE day (status `IMPLAUSIBLE-RETURN`, ruling 16) is itself NOT COMPUTABLE,
with the reason "follows a price discontinuity". Ruling 16 voids the glitch day but not its reversion.
- Measured at the cut: 2 `IMPLAUSIBLE-RETURN` rows in the 49F gold, both followed by an OK day. The accounts are
  ..4714 (2025-12-12) and ..0090 (2025-12-17), which would serve 1Y -69.8% and -91.5%.
- Implement the rule in the producer and re-emit the 49F and Inflection gold; COT below is built with it.
- Add a unit test for a glitch-then-reversion pair.
- The adapter switch to the 49F gold waits on this re-emit.

`IB-er-401` -- Your producer `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` now writes
49F and Inflection under v0.20 (round 3, @eee6a7a721). Cottonwood is the third firm, added through a declaration entry
in `sources.json` and never through a code branch.

**The source (PRD v0.19 ruling 1, measured at the cut):**
- positions: `s3://opal-data-assets/blackdiamond/cottonwood/silver/fact_holdings/date=YYYY-MM-DD/data.parquet`, 81
  partitions from 2026-06-09 through 2026-09-25; 984 accounts on 2026-09-24.
- columns: `AccountID` (the account key; the gold's `account_id` is `str(AccountID)`), `Market Value`, `Units`,
  `CUSIP`, `Symbol`, `Asset Name`, `Cash Equivalent`.

**The rules:**
- COT price = `Market Value` / `Units` where `Units` is present and non-zero; an absent `Units` is price-missing
  (ruling 4).
- `Cash Equivalent` rows are cash: in the weights, at zero return unless priced (ruling 3).
- The identifier is the first non-empty of CUSIP, Symbol and Asset Name (ruling 13; ruling 14 for cusip-less cash).
- The basket is the long holdings; a negative value sits outside it and the row carries `leveraged` (ruling 15).
- A day at or beyond +/-100% is NOT COMPUTABLE (ruling 16).
- Every day's manifest carries the four completeness keys (ruling 17).
- The day after a NOT COMPUTABLE day is NOT COMPUTABLE (v0.21 ruling 18, step 0).
- The gold address is builder output: `address("irpt", "cottonwood", "gold", "holdings_performance_daily" |
  "holdings_performance_manifest", "date=...")` (today `s3://opal-data-cottonwood/irpt/cottonwood/gold/...`).

**Build:** the declaration entry and any rule the COT columns need; run every COT account over every computable
trading day 2026-06-10..2026-09-25; tests for the Market Value / Units price and the absent-Units case. Run it ad hoc
for QA under a deploy ledger opened before the first write. Nothing reads these prefixes yet.

**Vendor egress:** none needed (landed silver). The Andrew-direct session-egress record of 2026-09-29 is on file; name
any vendor call in your report.

### ACCEPTANCE (run each from the workspace root)

<criterion id="E4-AC1" cell_refs="IB-er-401"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r4e/e4_ac1_cot_all_accounts_manifest.py"</invocation><expect>E4-AC1 PASS</expect></criterion>
`E4-AC1` -- on 2026-09-25, every COT account holding positions on 2026-09-24 has exactly one gold row, and the
manifest reads complete with matching counts. Base: FAIL (984 accounts, 0 rows).

<criterion id="E4-AC2" cell_refs="IB-er-401"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r4e/e4_ac2_cot_full_history.py"</invocation><expect>E4-AC2 PASS</expect></criterion>
`E4-AC2` -- a non-empty gold partition exists for every computable trading day 2026-06-10..2026-09-25. Base: FAIL (75
of 75 missing).

<criterion id="E4-AC3" cell_refs="IB-er-401"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r4e/e4_ac3_ruling18_follow_day.py"</invocation><expect>E4-AC3 PASS</expect></criterion>
`E4-AC3` (step 0) -- in the re-emitted 49F and INF gold, no account's next row after an IMPLAUSIBLE-RETURN day is OK;
the check prints ..0090 and ..4714's 1Y chains. Base: FAIL (2 violations, the two S200 accounts).

<expected_criteria>E4-AC1,E4-AC2,E4-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Serves nothing.** No reader, runner or schedule changes.
- **Refusal clause.** If a criterion cannot be met as written (a firm fence or a missing registry row), stop, write the
  reason in your report and a surprise row, and do not weaken a check to pass.

<paths>
data/assets/scripts/gold/irpt_holdings_performance/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 19 (workstream ~E, round 4), cell `IB-er-401`.
<owned_cells>IB-er-401</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: E4-AC1, E4-AC2, E4-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~E/IRPT_BCKEND.TO-IB-er-401.holdings-gold-cottonwood.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> E4-AC1,E4-AC2,E4-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~P` with the two check lines, the ledger slug and the commit hash.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- ad hoc QA only; the runner's firm scope widens in a later cell.
comp-iam: RUN -- the ad-hoc run writes new COT gold prefixes under the DS seat's session role; 0 roles changed; the COT bucket fence is named in the refusal clause.
comp-blast: DECLARED-NOT-APPLICABLE -- new objects under new prefixes only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no reader switched.
comp-adversary: RUN -- E4-AC3 dry-run at the base FAIL (49F: 2 IMPLAUSIBLE-RETURN rows, 2 follow-day OK violations ..4714 2025-12-12 and ..0090 2025-12-17; INF 0 and 0). E4-AC1/AC2 dry-run at the base: E4-AC1 FAIL (984 accounts, 0 gold rows); E4-AC2 FAIL (75 of 75 computable days missing).
lane: 0.4.0_DS_ClientPlatform~E is enumerated in .owned-paths.yaml POD4 for data/*/scripts/gold; the <paths> block is the grant.
</preflight>
