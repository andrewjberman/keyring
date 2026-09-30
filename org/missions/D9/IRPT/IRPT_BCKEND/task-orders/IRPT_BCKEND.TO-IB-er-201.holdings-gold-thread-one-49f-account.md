# TO IRPT_BCKEND.TO-IB-er-201 -- Holdings-basis gold, the thread: one invested 49F account, YTD (PRD v0.19 rulings 1-11)

<to_id>IRPT_BCKEND.TO-IB-er-201</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.4.0_DS_ClientPlatform~E</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-28</issued_date>
<status>complete -- E1-AC1 PASS against the amended check @5e273c614f (recompute 0.004612117916 == gold, excluded 0) and E1-AC2 PASS (184 of 184 trading days, 0 missing, chained YTD 0.058285), both exit 0 read unpiped; 184 partitions landed and listing-verified under the builder addresses (missing 0, extra 0 on both gold tables); planted mutant FIRED and restored; 9 unit tests pass; proof-of-spec VALID rc=0; naming gate PASS 3 graded 0 REFUSE. Row S191 (the check-vs-naming-limb contradiction) ruled by 2.0.0_SA_COO~P msg 102514 and dispositioned by row S192: the declaration is keyed by custody source and the firm scope is registry-derived, no override taken. Rows S189, S190 open for their owners. Ledger irpt-holdings-gold-thread-49f-20260928. No reader switched; c02_twr_engine.py and every served table untouched.</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>~E</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** PRD `org/missions/D9/IRPT/IRPT_BCKEND/prd/IRPT_BCKEND_PRD.md` ADDENDUM
v0.19 (@82e1700237) rulings 10-11, on Andrew-direct 2026-09-28 ~22:2xZ call 3 and ~22:4xZ (records
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_222xZ_OPEN_CALLS_1_2_APPROVED_3_HOLDINGS_BASED_PERFORMANCE.md`,
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_224xZ_HOLDINGS_BASED_PERFORMANCE_ALL_FIRMS_SILVER_TO_ONE_GOLD.md`);
L1 brief `docs/briefs/irpt-holdings-basis-silver-inventory-brief-20260928.md` | **Decomp cell:** `IB-er-201`
(decomposition section 14) | **outcome_ref:** FWD-3 (thread) | **depends_on:** none

---

## WORKER FACE

### THE CELL

`IB-er-201` -- the first hop of the FWD-3 thread: one invested 49 Financial Schwab account (account_id `0010498003`),
year to date, computed from end-of-day holdings into the consolidated gold. The adapter switch that reads this gold is
~P's own later cell; this order builds the gold only.

**The method (fixed; Andrew-direct call 3, PRD v0.19 rulings 2-5):** the day-t return of an account is
`sum over included holdings of v_i(t-1) * r_i(t) / (sum over included holdings of v_i(t-1) + cash(t-1))`, where:
- `v_i` is the holding's end-of-day market value (a cusip's lots summed);
- `r_i = price(t) / price(t-1) - 1` on a positive price both days;
- cash is the firm's declared cash balance, with a zero return;
- a holding without a positive price on both days is EXCLUDED, and the row carries `excluded_count` and
  `excluded_weight` (never priced at zero, never silent);
- there is NO inflow/outflow term;
- the day axis is `lib/trading_calendar.py` (a calendar-day partition folds to its trading day; a missing trading day
  is ABSENT).

**Build** (paths from the workspace root):
1. `data/assets/scripts/gold/irpt_holdings_performance/sources.json` -- the source declaration as data (ruling 1). The
   `49financial` entry holds: `bucket` (`opal-data-assets`), `positions_prefix` (`schwab/08335338/silver/dim_position/`),
   `balance_prefix` (`schwab/08335338/silver/dim_balance/`), `cash_columns` (the dim_balance column list you declare as
   cash held outside positions -- name them from the data, and say why in a comment field), and the key, date, value and
   price columns.
2. `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` -- reads the declaration and writes, per
   trading day, `lib/opal_naming.address("irpt", "49financial", "gold", "holdings_performance_daily", "date=YYYY-MM-DD")`
   with columns `account_id, business_date, daily_return, account_value, excluded_count, excluded_weight` (plus any
   lineage columns you add), and the manifest at `address(..., "holdings_performance_manifest", ...)`. Every address comes
   from the builder; none is typed.
3. For this round: run it ad hoc (QA is what ad-hoc runs are for) for the THREAD account over the YTD trading days
   2026-01-02..2026-09-25. A write under these new gold prefixes serves nothing yet (no reader is switched), so it needs
   no never-widen sign-off. Open a deploy ledger (`.tools/deploy_ledger.py`) before the first S3 write, and close it
   with the check lines.
4. Tests beside the script: a trading day with a flow (the flow does not move the return), a full exit (never -100%),
   the price-missing exclusion, and cash at a zero return.

`2.0.0_SA_COO~M` answers source-read questions about the Schwab silver (it reads the same tables for the holdings
snapshot; PRD v0.19 ruling 10). The schedule `irpt-holdings-performance-daily` and all firms are LATER rounds (ruling
11: thread first, then Inflection, then Cottonwood).

### ACCEPTANCE (run each from the workspace root)

<criterion id="E1-AC1" cell_refs="IB-er-201"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r1e/e1_ac1_thread_day_recompute.py"</invocation><expect>E1-AC1 PASS</expect></criterion>
`E1-AC1` -- the thread account's gold daily_return for 2026-09-25 equals an independent recompute from the declared
silver within 1e-9, with the same excluded_count. Base: FAIL (no declaration, no gold).

<criterion id="E1-AC2" cell_refs="IB-er-201"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r1e/e1_ac2_thread_ytd_coverage.py"</invocation><expect>E1-AC2 PASS</expect></criterion>
`E1-AC2` -- every trading day 2026-01-02..2026-09-25 carries the thread account's row, and the chained YTD is finite
and above -1. Base: FAIL (184 of 184 days missing).

<expected_criteria>E1-AC1,E1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Serves nothing.** No reader is switched in this round; the adapter, the 49F engine (`c02_twr_engine.py`) and every
  served table stay untouched. The old engine retires only in the window FWD-3 turns REALIZED (ruling 12).
- **Refusal clause.** If a criterion cannot be met as written (for example, the declared silver lacks a price for most
  held positions), stop, write the reason in your report and a surprise row, and do not weaken a check to pass.

<paths>
data/assets/scripts/gold/irpt_holdings_performance/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 14 (workstream ~E, round 1), cell `IB-er-201`.
<owned_cells>IB-er-201</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: E1-AC1, E1-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~E/IRPT_BCKEND.TO-IB-er-201.holdings-gold-thread-one-49f-account.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> E1-AC1,E1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~P` with the two check lines, the ledger slug and the commit hash; surprise rows
in the investigation file (id `IRPT_BCKEND-S<next>`).

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this round runs ad hoc for QA only; the daily schedule is a later round (PRD v0.19 ruling 9).
comp-iam: RUN -- the ad-hoc run writes new gold prefixes under opal-data-49financial; the DS seat's session role is the writer; any refusal is a surprise row, never a widened grant.
comp-blast: DECLARED-NOT-APPLICABLE -- new prefixes only; no existing object is moved or deleted.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface; no reader switched.
comp-adversary: RUN -- both checks dry-run at the base: AC1 FAIL (no declaration), AC2 FAIL (184 of 184 trading days missing). Builder addresses resolve: s3://opal-data-49financial/irpt/49financial/gold/holdings_performance_daily/date=... and .../holdings_performance_manifest/...
lane: 0.4.0_DS_ClientPlatform~E is enumerated in .owned-paths.yaml POD4 for data/*/scripts/gold (MSTR 102458); the <paths> block is the grant.
</preflight>
