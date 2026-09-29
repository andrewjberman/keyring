# TO IRPT_BCKEND.TO-IB-m26-261 -- Holdings serves per-security aggregates and per-class totals (W2-11, W2-15)

<to_id>IRPT_BCKEND.TO-IB-m26-261</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~84</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>26</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-261`
(`decompositions/IRPT_BCKEND_DECOMP_R26_M.md`) | **outcome_ref:** FWD-5 (Holdings) | **depends_on:** IB-mr-251

---

## WORKER FACE

### THE CELL

`IB-mr-261` -- 1.0.0_SA_CTO DECISION 103025 on the walk-2 state table
(`org/missions/D13/DSGN/DSGN_IRPTV1/deliverables/2.0.0_SA_COO~D/walk-v2-state-table-20260929.md`, rows W2-11 and
W2-15): "W2-11 fold is NOT legal -- the server serves the aggregate"; "~M: W2-11 per-security aggregate and W2-15
per-class weights, both served". The Holdings tab never sums (F7-AC4; CTO 102522: it prints only producer-served
totals), so the portal cannot fold one security's rows across accounts, and it cannot print a class total, unless the
producer serves them.

This order runs AFTER IRPT_BCKEND.TO-IB-m25-251 in the same worktree. The aggregates carry the classes 251 now serves
(etf-classifications), so build on 251's `holdings_snapshot.py`, never on the pre-251 classifier.

**Build (LOCAL build + record -- no upload, no mint, no deploy):**
0. **Repair first (amendment 1, row IRPT_BCKEND-W84-S2).** 251's refuse-on-unknown classifier breaks 37 existing test
   functions in four other files under `data/assets/scripts/gold/investor_reporting/tests/`, because they use the
   synthetic ticker `'AAA'`, which etf-classifications does not hold. Give those tests a stubbed etf-classifications
   table (a fixture that holds their synthetic tickers), the way `test_holdings_etf_classifications.py` stubs it. The
   refusal stays exactly as 251 built it; no test is deleted, skipped or loosened. Afterwards
   `python -m pytest data/assets/scripts/gold/investor_reporting/tests -q -p no:cacheprovider` passes whole: report
   that line.
1. **Contract.** Add two OPTIONAL top-level properties to the HoldingsSnapshot schema, identically in all three tracked
   copies (listed in `<paths>`; the schema is `additionalProperties: false`, so an unlisted field fails validation):
   - `security_aggregates`: an array, one item per security identity in the snapshot's scope. Each item carries the
     identity (`security_id`, the same `{namespace, value}` object the security nodes carry), the display
     (symbol/description as the nodes carry them), the served class (`asset_class`, `sub_asset_class`), the summed
     `amount` (same shape as a node's amount), `weight` (the share of the scope total), and `account_count`.
   - `class_totals`: an array, one item per asset class, carrying `asset_class`, the summed `amount`, and `weight`.
   Every description names this cell and CTO 103025, as the neighbouring properties name their rulings.
2. **Producer.** In `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py`, compute both blocks from the
   built nodes, after classification and weights, for every firm path (49financial, inflection, cottonwood). Identity
   is the node's `security_id`: the portal keys a security as `namespace:value` of that field
   (`portal/src/pages/InvestorReporting/contracts/adapt.ts:568-570,1053`; its fold is
   `tabs/holdings/HoldingsTreemap.tsx:257-277`; read both, edit neither). A security node with no `security_id` stays
   its own aggregate and is never merged by name. Holdout or unassigned mass is never dropped. Either it is its own
   class total, or the census names it as `held_out_weight`. Name the grain: the aggregates cover the snapshot's
   scope as the tab prints it, and if one scope unit holds several clients, the census and the half say so.
3. **Tests** in `data/assets/scripts/gold/investor_reporting/tests/test_holdings_aggregates.py`, on built node
   fixtures. One security held in two accounts gives ONE aggregate whose amount is the sum. Weights sum to 1 with the
   holdouts. Class totals equal the class sums. A security with no identity is not merged. The built document
   validates against the contract.
4. **Census** from REAL local builds at all three firms (the method 251 used). Write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R26_AGGREGATES_CENSUS_20260929.json` as
   `{"firms": [{"firm", "as_of", "valid", "grain", "security_aggregates", "distinct_identities",
   "security_weight_sum", "class_totals", "class_weight_sum", "class_amount_sum", "custody_total",
   "held_out_weight", "largest_fold": {"security_id", "account_count", "amount"}}]}`.
5. **Half.** Write `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_AGGREGATES_20260929.md`
   (`## The act`, `## Blast radius`, `Rollback per key`), covering both branches and every reader of the Holdings
   document, from the census (portal adapter, the holdings lambda's contract copy, exports). Name the release order:
   the three contract copies with the holdings lambda's deploy first, then the Holdings re-mint, after 251's release.
   Trace which reader validates against which copy, so that no served document can carry a field its reader's copy
   refuses.

### ACCEPTANCE

<criterion id="IBM26-261-AC1" cell_refs="IB-mr-261"><invocation>python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_holdings_aggregates.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`IBM26-261-AC1` -- one aggregate per security identity, weights and class totals that reconcile, and no merge by name.

<criterion id="IBM26-261-AC2" cell_refs="IB-mr-261"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R26_CHECKS/r26_aggregates_census.py</invocation><expect>AGG-CENSUS</expect></criterion>
`IBM26-261-AC2` -- real local builds at all three firms validate against the contract, and their aggregates and class
totals reconcile to the scope and custody totals.

<criterion id="IBM26-261-AC3" cell_refs="IB-mr-261"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_AGGREGATES_20260929.md</invocation><expect>HALF-READY</expect></criterion>
`IBM26-261-AC3` -- the half, with its census, readers and release order, is written for the issuer to sign and send.

<expected_criteria>IBM26-261-AC1,IBM26-261-AC2,IBM26-261-AC3</expected_criteria>

Dry-run at the base 2026-09-29 20:4xZ (@b9680cfe86): AC1 "no tests ran", AC2 NOT-CENSUSED (census absent), AC3
NOT-READY (half absent) -- FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** No upload, no mint, no deploy, no lambda change beyond its contract copy. The local builds
  READ the firm buckets.
- **Portal files are read-only.** The front half (W2-11 rows, W2-15 totals) is 2.0.0_SA_COO~D's.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W84-S<k>`), and do not weaken the test to pass.

<paths>
data/assets/scripts/gold/investor_reporting/
docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json
infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json
infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R26_AGGREGATES_CENSUS_20260929.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_AGGREGATES_20260929.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R26_M.md</decomp_doc> (round 26, workstream ~M), cell `IB-mr-261`.
<owned_cells>IB-mr-261</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM26-261-AC1, IBM26-261-AC2, IBM26-261-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~84/IRPT_BCKEND.TO-IB-m26-261.holdings-served-aggregates.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM26-261-AC1,IBM26-261-AC2,IBM26-261-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the two contract properties as written (and the three copies byte-equal), where the producer computes
them, the grain, the census per firm (aggregates/identities, weight sums, the largest fold), the readers and which
copy each validates against, the pytest line, the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change; the served move rides a later Holdings re-mint under this cell's half.
comp-iam: DECLARED-NOT-APPLICABLE -- no policy change; the local builds read with the operator's credentials, as 251's do.
comp-adversary: RUN -- 1 contract read (HoldingsSnapshot top level additionalProperties:false; required scope/source_set_revision/clocks/custody_totals/nodes/coverage; three tracked copies), 1 portal identity read (adapt.ts:568-570,1053 namespace:value of node.security_id; HoldingsTreemap.tsx:257-277 fold), 1 served read (three firms' headers for 2026-09-28 carry no source_vendor_keys); BLIND: the scope grain (one client or several per snapshot scope) is unread at the cut (step 2 names it), and which reader validates against which contract copy is untraced (step 5 traces it).
lane: the <paths> block IS the grant; ~M owns the Holdings producer and, by precedent (IB-mr-203 source_vendor_keys), its contract fields.
</preflight>

Source: 1.0.0_SA_CTO DECISION 103025 (walk-2 backend placed); state table @f80d019a6c; Andrew 3054ca47ec.
