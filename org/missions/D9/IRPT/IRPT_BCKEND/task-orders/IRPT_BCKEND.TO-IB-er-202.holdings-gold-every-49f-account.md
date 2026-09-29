# TO IRPT_BCKEND.TO-IB-er-202 -- Holdings-basis gold for EVERY 49F account, full history, manifest complete (PRD v0.19; CTO ruling 102520)

<to_id>IRPT_BCKEND.TO-IB-er-202</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.4.0_DS_ClientPlatform~E</issued_to>
<issued_by>2.0.0_SA_COO~P</issued_by>
<issued_date>2026-09-29</issued_date>
<status>complete -- E2-AC1 PASS (6,341 silver accounts at 2026-09-24, 7,540 gold rows, 0 missing, 0 duplicated; manifest 6341/6338/3 complete=True) and E2-AC2 PASS (557 of 557 trading days 2024-07-09..2026-09-25, 0 missing), both exit 0 read unpiped. 557 partitions on each gold table, missing 0 / extra 0 by ListObjectsV2; 3,188,339 rows read back from the 557 parquet footers, equal to the producer's tally; 0 empty partitions; every partition complete=True. Completeness mutant FIRED (one held account dropped -> AC1 FAIL with the manifest still claiming complete) and restored. 13 unit tests pass; proof-of-spec VALID rc=0; naming gate PASS 0 REFUSE. Ledger irpt-holdings-gold-all-49f-20260929. No reader switched; the schedule is IB-er-203 and was not built here.</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>seat</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~E</workstream>

**Directive:** D9 | **Fabric:** laptop | **Ordered by:** 1.0.0_SA_CTO ruling 102520 ("~E round 2 = every 49F account,
full history from each account's first holdings day, plus the daily schedule"), on PRD ADDENDUM v0.19 rulings 4, 6, 9,
12 | **Decomp cell:** `IB-er-202` (decomposition section 16) | **outcome_ref:** FWD-3 (49F) | **depends_on:** ~E
round 1 (TO-IB-er-201, complete)

---

## WORKER FACE

### THE CELL

`IB-er-202` -- your producer `data/assets/scripts/gold/irpt_holdings_performance/holdings_performance.py` (round 1,
build 23004aaf98) wrote the gold for ONE account over YTD. This round writes it for EVERY 49F account in the declared
Schwab silver (the `schwab_08335338` entry), for every trading day from the first day a return can exist (the silver's
first partition is 2024-07-08, so the first return day is 2024-07-09) through 2026-09-25. Same method, same addresses
(`address("irpt", "49financial", "gold", "holdings_performance_daily" | "holdings_performance_manifest", "date=...")`).
~P's adapter switch serves only after this manifest reads complete (ruling 102520).

**Build:**
1. Run the producer for all accounts over the full range. An account with no computable return on a day (no prior
   holdings, a price-missing total, a zero account value) gets a row with a NAMED non-OK status, never a figure.
   Every account that held positions on the prior trading day appears exactly once per day.
2. The manifest partition per day carries `accounts_with_prior_holdings`, `computable_count`, `not_computable_count`
   and `complete` (true when computable + not_computable == accounts_with_prior_holdings and every such account has
   its row).
3. Add the manifest fields to the producer's tests.
4. Run it ad hoc for QA, under a deploy ledger opened before the first write. Nothing reads these prefixes yet, so no
   served output moves and no never-widen sign-off is needed.

The daily schedule is a separate cell in this round (IB-er-203, another assignee); do not build it here.
`2.0.0_SA_COO~M` answers Schwab silver questions (row S189 is theirs).

### ACCEPTANCE (run each from the workspace root)

<criterion id="E2-AC1" cell_refs="IB-er-202"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r2e/e2_ac1_all_accounts_manifest.py"</invocation><expect>E2-AC1 PASS</expect></criterion>
`E2-AC1` -- on 2026-09-25, every account holding positions on 2026-09-24 in the declared silver has exactly one gold
row, and the manifest reads complete with matching counts. Base: FAIL (6,341 accounts, 1 row, 6,340 missing, manifest
fields absent).

<criterion id="E2-AC2" cell_refs="IB-er-202"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r2e/e2_ac2_full_history.py"</invocation><expect>E2-AC2 PASS</expect></criterion>
`E2-AC2` -- a non-empty gold partition exists for every trading day 2024-07-09..2026-09-25. Base: FAIL (373 of 557
missing).

<expected_criteria>E2-AC1,E2-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Serves nothing.** No reader is switched; the adapter, the 49F engine and every served table stay untouched.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise
  row, and do not weaken a check to pass.

<paths>
data/assets/scripts/gold/irpt_holdings_performance/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 16 (workstream ~E, round 2), cell `IB-er-202`.
<owned_cells>IB-er-202</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: E2-AC1, E2-AC2. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~E/IRPT_BCKEND.TO-IB-er-202.holdings-gold-every-49f-account.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> E2-AC1,E2-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~P` with the two check lines, the ledger slug and the commit hash; surprise rows
in the investigation file.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- this cell runs ad hoc for QA only; the schedule is IB-er-203.
comp-iam: RUN -- the ad-hoc run writes the same new gold prefixes as round 1 under the DS seat's session role.
comp-blast: DECLARED-NOT-APPLICABLE -- new objects under new prefixes only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- no reader switched.
comp-adversary: RUN -- both checks dry-run at the base: E2-AC1 FAIL (6,341 silver accounts, 1 gold row, manifest fields absent); E2-AC2 FAIL (373 of 557 trading days missing).
lane: 0.4.0_DS_ClientPlatform~E is enumerated in .owned-paths.yaml POD4 for data/*/scripts/gold; the <paths> block is the grant.
</preflight>
