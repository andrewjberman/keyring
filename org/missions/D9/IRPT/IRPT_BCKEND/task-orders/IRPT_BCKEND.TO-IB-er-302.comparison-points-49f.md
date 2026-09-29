# TO IRPT_BCKEND.TO-IB-er-302 -- FWD-13 for 49F: one comparison row per landed Black Diamond performance file (PRD v0.19 rulings 7, 8, 9)

<to_id>IRPT_BCKEND.TO-IB-er-302</to_id>
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
section 6 item 4: "FWD-13 comparison points for 49F (4 landed Black Diamond pulls)"), on PRD ADDENDUM v0.19 rulings 7-9 |
**Decomp cell:** `IB-er-302` (decomposition section 17) | **outcome_ref:** FWD-13 (49F) | **depends_on:** ~E round 2
(TO-IB-er-202, complete: the 49F gold covers 2024-07-09..2026-09-25)

---

## WORKER FACE

### THE CELL

`IB-er-302` -- FWD-13: an analyst compares Opal's holdings-basis figure against the vendor's official figure at
pre-set points, with both bases stated. It is a bounded check at defined points, never a standing comparator. For 49F
the landed points are Black Diamond's reporting_performance pulls (PRD v0.19 ruling 8).

**The source (measured at the cut, BRONZE, never converted):**
`s3://opal-data-assets/blackdiamond/49f/bronze/reporting_performance/<pull date>/reporting_performance_<id>_<as-of>.json`
- 4 pull dates: 2026-07-17 (1 file, as-of 2026-06-30); 2026-08-30 (5), 2026-08-31 (3) and 2026-09-01 (5,309), all
  as-of 2026-08-28.
- 5,318 files. Each file is one Black Diamond level with its `accounts` list (accountId, accountNumber), `startDate`,
  `dataAsOfDate` and its performance figures.

**Build** -- a comparison script beside the producer, in the same gold-script home:
1. For every bronze file, write ONE row to
   `address("irpt", "49financial", "gold", "holdings_performance_comparison", "date=<as-of>")` (builder output; today
   `s3://opal-data-49financial/irpt/49financial/gold/holdings_performance_comparison/date=...`). Each row carries:
   - `source_key` (the bronze key);
   - `vendor_return` (Black Diamond's own time-weighted return for the file's period) and `vendor_field` (the JSON
     path you read it from);
   - `opal_return` (the holdings-basis return over the SAME period, from the 49F gold);
   - `period_start`, `period_end` and `difference`;
   - the two bases stated: `vendor_basis` (Black Diamond TWR, flows included) and `opal_basis` (end-of-day holdings,
     prior-day weights, no flow term).
2. **Composition (ruling 7):** a level with several accounts is the union of their holdings, weighted by value on the
   prior trading day, computed from the gold's `daily_return` and `account_value`. Map a Black Diamond account to the
   gold's raw 10-digit `account_id` by its `accountNumber`.
3. When a row cannot be compared (an account not in the gold, a period before the gold's first day, no vendor figure
   in the file), write it with a non-empty `not_comparable_reason` instead of the figures. Never drop a file, and
   never invent a figure.
4. Tests for the composition, the period selection and each named reason.
5. Run it ad hoc for QA under a deploy ledger opened before the first write. Nothing reads this table, so no served
   output moves.

**Vendor egress:** none is needed; the inputs are landed bronze and your own gold. Andrew-direct 2026-09-29 (record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260929_044xZ_OPEN_CALLS_APPROVED_SESSION_EGRESS.md`) covers
a vendor call the work genuinely needs this session; name any such call in your report.

### ACCEPTANCE (run from the workspace root)

<criterion id="E3-AC3" cell_refs="IB-er-302"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P/checks/r3e/e3_ac3_49f_comparison_points.py"</invocation><expect>E3-AC3 PASS</expect></criterion>
`E3-AC3` -- for each as-of date, the comparison partition has exactly one row per bronze file carrying that as-of, and
every row carries both figures and the period or a named reason, with no duplicate source_key. Base: FAIL (1 and 5,317
files, 0 rows).

<expected_criteria>E3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below, plus your deliverables folder and this order's file.
- **Serves nothing.** No reader, page or schedule changes.
- **Refusal clause.** If a criterion cannot be met as written (for example the files carry no period your rules can
  select), stop, write the reason in your report and a surprise row, and do not weaken a check to pass.

<paths>
data/assets/scripts/gold/irpt_holdings_performance/
org/critical_paths/change_management/
org/critical_paths/.open_deploys/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 17 (workstream ~E, round 3), cell `IB-er-302`.
<owned_cells>IB-er-302</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: E3-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.4.0_DS_ClientPlatform~E/IRPT_BCKEND.TO-IB-er-302.comparison-points-49f.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> E3-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** one message to `2.0.0_SA_COO~P` with the check lines per as-of date, the ledger slug and the commit hash;
surprise rows in the investigation file.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a bounded check at defined points (PRD v0.19 FWD-13), run ad hoc; no schedule, no standing comparator.
comp-iam: RUN -- the ad-hoc run writes one new 49F gold prefix under the DS seat's session role; 0 roles changed.
comp-blast: DECLARED-NOT-APPLICABLE -- new objects under a new prefix only.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-cache: DECLARED-NOT-APPLICABLE -- nothing reads the table.
comp-adversary: RUN -- E3-AC3 dry-run at the base: FAIL (as-of 2026-06-30: 1 bronze file, 0 rows; as-of 2026-08-28: 5,317 files, 0 rows).
lane: 0.4.0_DS_ClientPlatform~E is enumerated in .owned-paths.yaml POD4 for data/*/scripts/gold; the <paths> block is the grant.
</preflight>
