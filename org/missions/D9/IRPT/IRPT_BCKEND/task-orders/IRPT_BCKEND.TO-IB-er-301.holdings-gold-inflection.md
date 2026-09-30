# TO IRPT_BCKEND.TO-IB-er-301 -- Holdings-basis gold for EVERY Inflection account, full history, manifest complete (PRD v0.19 rulings 1-6, 9, 11)

<to_id>IRPT_BCKEND.TO-IB-er-301</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.4.0_DS_ClientPlatform~E</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~E</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ROUND-19 ANALYSIS (`ledger/ROUND_ANALYSIS.round19.md`
section 6 item 1: "then Inflection and Cottonwood on the holdings gold, in that order (ruling 11)"), on PRD ADDENDUM v0.19
rulings 1-6, 9, 11 | **Decomp cell:** `IB-er-301` (decomposition section 17) | **outcome_ref:** FWD-3 (INF) |
**depends_on:** ~E round 2 (TO-IB-er-202, complete)

---

## WORKER FACE

### THE CELL

**AMENDMENT 1 (2026-09-29 ~05:4xZ, issuer, on 1.0.0_SA_CTO RULING 102611 = PRD ADDENDUM v0.20 @613bfc6ecf
rulings 13-17, and 4.0.0_SA_CRO's refused half @eca8083ad2, row IRPT_BCKEND-S195): DO STEP 0 FIRST.**

**Step 0 -- fix the producer for v0.20 and re-emit the 49F gold.** Measured by the CRO:
- `holdings_performance.py:273` keys the day-t price by cusip alone. 41 `dim_position` rows per day carry cusip '' across
  33 accounts, all priced under one key, so 18 accounts read about +1e57 YTD.
- Four OK rows read r <= -1 over a near-zero net base (a margin debit).
- Base census (E3-AC4 at the cut): 2,846 OK rows at |r| >= 1 and 4,061 at |r| > 0.5 across 557 days; no `leveraged` column.

The v0.20 rules, verbatim in substance:
- (13) a position is keyed by (account, identifier), where the identifier is the first non-empty of cusip, symbol and
  description; a row with none is UNIDENTIFIED.
- (14) an UNIDENTIFIED row priced 1.00 with quantity == value is cash (ruling 3); every other UNIDENTIFIED row is
  excluded (ruling 4), its count and weight on the row.
- (15) the basket is the LONG holdings: weights over the sum of POSITIVE prior-day values (positive cash included); a
  negative balance is outside the basket; the row carries `leveraged` (true/false) and the excluded negative value.
- (16) an account day at or below -100% or at or above +100% is NOT COMPUTABLE with its reason named in the manifest.
- (17) every day's manifest carries the four completeness keys.

Re-emit all 557 49F partitions and manifests. Add unit tests: two cusip-less positions at different prices; a
cusip-less cash row; a margin-debit account; and a +/-100% day. Print the |r| > 0.5 census before and after in your
proof. The same rules then govern the Inflection slice below.

`IB-er-301` -- your producer `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` writes the
49F gold from `sources.json` (round 2: every 49F account, 2024-07-09..2026-09-25, manifest complete). This round adds
INFLECTION as a second declared source, with the same method, rules and manifest, through the declaration and never
through a code branch (the declaration's own doc line: "A new firm channel is a new entry here").

**The source (PRD v0.19 ruling 1, measured at the cut):**
- positions: `s3://opal-data-assets/orion/inflection/silver/fact_positions/date=YYYY-MM-DD/data.parquet`. There is
  a partition per CALENDAR day from 2020-04-24 (2,343 partitions); 960 accounts on 2026-09-24.
- columns: `accountId` (the account key; the gold's `account_id` is `str(accountId)`), `currentPrice`,
  `currentValue`, `currentShares`, `isCustodialCash`, `ticker`, `productId`.

**The rules:**
- Account value is the sum of the holdings' end-of-day `currentValue` (ruling 2). There is no separate cash balance:
  custodial cash is a position.
- A position with `isCustodialCash` true is a holding in the weights with a ZERO daily return, unless it carries its
  own positive price on both days (ruling 3).
- A non-cash position without a positive `currentPrice` on both days is excluded from that day's return, and the row
  carries the excluded count and weight (ruling 4).
- The day axis is `lib/trading_calendar.py` (ruling 5): a weekend or holiday partition is not a trading day, and a
  trading day whose partition, or whose prior trading day's partition, is missing is ABSENT (no gold row for that day).
- Since inception is the account's first landed day (ruling 6).

**Build:**
1. Add the Inflection entry to `sources.json`, keyed by its custody source the way `schwab_08335338` is. The firm comes
   from the registry, never typed; the gold address is builder output:
   `address("irpt", "inflection", "gold", "holdings_performance_daily" | "holdings_performance_manifest", "date=...")`
   (today `s3://opal-data-inflection/irpt/inflection/gold/...`).
2. Run it for every INF account over every computable trading day 2020-04-27..2026-09-25. An account with no
   computable return on a day gets a row with a NAMED non-OK status. Each manifest carries
   `accounts_with_prior_holdings`, `computable_count`, `not_computable_count` and `complete`, exactly as 49F's do.
3. Add the INF declaration and the cash and price rules to the producer's tests. The 49F tests still pass, unchanged.
4. Run it ad hoc for QA under a deploy ledger opened before the first write. Nothing reads these prefixes yet, so no
   served output moves. The daily schedule's runner is NOT changed here: its role is scoped to one firm, and widening
   it is a later cell.

**Vendor egress:** none is needed; every input above is landed silver. Andrew-direct 2026-09-29 (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_044xZ_OPEN_CALLS_APPROVED_SESSION_EGRESS.md`) covers
a vendor call the work genuinely needs this session; name any such call in your report.

### ACCEPTANCE (run each from the workspace root)

<criterion id="E3-AC1" cell_refs="IB-er-301"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r3e/e3_ac1_inf_all_accounts_manifest.py"</invocation><expect>E3-AC1 PASS</expect></criterion>
`E3-AC1` -- on 2026-09-25, every INF account holding positions on 2026-09-24 has exactly one gold row, and the manifest
reads complete with matching counts. Base: FAIL (960 accounts, 0 rows, manifest absent).

<criterion id="E3-AC2" cell_refs="IB-er-301"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r3e/e3_ac2_inf_full_history.py"</invocation><expect>E3-AC2 PASS</expect></criterion>
`E3-AC2` -- a non-empty gold partition exists for every computable trading day 2020-04-27..2026-09-25 (the check
prints the 4 non-computable days it excludes). Base: FAIL (1,609 of 1,609 missing).

<criterion id="E3-AC4" cell_refs="IB-er-301"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r3e/e3_ac4_49f_reemit_v020.py"</invocation><expect>E3-AC4 PASS</expect></criterion>
`E3-AC4` (amendment 1) -- over all 557 49F days: 0 OK rows at |daily_return| >= 1, a `leveraged` column on every day,
and every manifest complete. Base: FAIL (2,846 OK rows at |r| >= 1; `leveraged` absent on 557 days).

<expected_criteria>E3-AC1,E3-AC2,E3-AC4</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Serves nothing.** No reader is switched; the adapter, the runner Lambda and every served table stay untouched.
- **Refusal clause.** If a criterion cannot be met as written (for example the INF bucket's firm fence refuses your
  write, or a registry row is missing), stop, write the reason in your report and a surprise row, and do not weaken a
  check to pass.

<paths>
data/assets/scripts/gold/irpt_holdings_performance/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 17 (workstream ~E, round 3), cell `IB-er-301`.
<owned_cells>IB-er-301</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: E3-AC1, E3-AC2, E3-AC4. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~E/IRPT_BCKEND.TO-IB-er-301.holdings-gold-inflection.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> E3-AC1,E3-AC2,E3-AC4` BEFORE the flip.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~P` with the two check lines, the ledger slug and the commit hash; surprise rows
in the investigation file.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell runs ad hoc for QA only; the runner's firm scope widens in a later cell.
comp-iam: RUN -- the ad-hoc run writes the new INF gold prefixes under the DS seat's session role; 0 roles changed; the INF bucket's firm fence is named in the refusal clause.
comp-blast: DECLARED-NOT-APPLICABLE -- new objects under new prefixes only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no reader switched.
comp-adversary: RUN -- amendment 1: E3-AC4 dry-run at the base FAIL (2,846 OK rows |r|>=1, 4,061 |r|>0.5, `leveraged` absent 557 days, manifests 557/557). Original checks dry-run at the base: E3-AC1 FAIL (960 silver accounts, 0 gold rows, manifest absent); E3-AC2 FAIL (1,609 of 1,609 computable days missing, 4 non-computable).
lane: 0.4.0_DS_ClientPlatform~E is enumerated in .owned-paths.yaml POD4 for data/*/scripts/gold; the <paths> block is the grant.
</preflight>
