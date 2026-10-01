# TO IRPT_BCKEND.TO-IB-m25-251 -- Holdings classifies from etf-classifications (one canonical security table)

<to_id>IRPT_BCKEND.TO-IB-m25-251</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~84</issued_to>
<issued_by>2.0.0_SA_COO~M</issued_by>
<issued_date>2026-09-29</issued_date>
<status>superseded</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>25</round>
<workstream>~M</workstream>

**Directive:** D9 | **Fabric:** laptop | **Workstream:** ~M | **Decomp cell:** `IB-mr-251`
(`decompositions/IRPT_BCKEND_DECOMP_R25_M.md`) | **outcome_ref:** FWD-5 (Holdings classes) | **depends_on:** IB-mr-222 Part 1

---

## WORKER FACE

### THE CELL

`IB-mr-251` -- Andrew-direct 2026-09-29 ~17:4xZ: one canonical per-security table for all holdings, the DynamoDB table
`etf-classifications` (the table that feeds Positioning). The CTO placed two items with ~M
(`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_PLACEMENT_20260929_182xZ_ONE_CANONICAL_SECURITY_TABLE.md`, @c3c3f414dc):

(a) `data/assets/scripts/gold/investor_reporting/holdings_snapshot.py` (~:828-873: `canonical_classifier()`,
`_classifier_basis()`, `classify_security()`) stops classifying through `bd-securities` (the loader of
`data/black_diamond/scripts/gold/lib/etf_classifier.py`) and reads `etf-classifications` through the EXISTING client
`infra/aws/lambda/v2_portal/_shared/etf_classifications_dynamodb.py` (it `get_item`s by `ticker` and `query`s an index).
No third client copy. The classifier's `hedge -> alternatives` fold (`etf_classifier.py:99,108`) does NOT apply on this
path. The Black Diamond cash line (`CASH -- CASH` -> cash, CTO 101547) and every existing refusal stay as they are.
(b) Andrew authorised a PHYS row: add it to the seed source `infra/aws/lambda/v2_portal/_shared/etf_classification.py`
(where GLD sits: `'GLD': 'commodities'`, sub-asset `'Metals'`, exposure `'Gold'`), so the table stays reproducible from
source. It is written to the table only by the seed path, never by a hand `put-item` -- and NOT in this order.

This moves served figures (GLD/PHYS to commodities/Metals, VXX to structured/Hedge), so it is a never-widen act.

**Build (LOCAL build + record -- no upload, no seed write, no terraform apply):**
1. Implement (a) in `holdings_snapshot.py`, importing the existing client from its home (add its directory to the
   import path the way the module already does for other homes; do not copy the file). A security the table does not
   know refuses loudly by name, never a guessed class. Tests in
   `data/assets/scripts/gold/investor_reporting/tests/test_holdings_etf_classifications.py` with a stubbed table:
   GLD -> commodities/Metals, VXX -> structured/Hedge (no fold), an unknown ticker refuses, the cash line unchanged.
2. Implement (b): the PHYS row in `etf_classification.py`, matching GLD's fields.
3. The Holdings closure: add the client file (and anything it imports at load) to `_IRPT_HOLDINGS_CLOSURE` in
   `.tools/safe_deploy_core.py`, re-traced with a real build (the amendment-1 method of TO-IB-m19-2). The directory
   bundle does not import holdings_snapshot at load, but run
   `python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R24_CHECKS/r24_directory_bundle_imports.py` and report
   its line.
4. IAM (desired, not applied): the Holdings firm principals read the table through `get_item`/`query`. In
   `infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf` (today a `dynamodb:Scan` grant per listed
   table, ~:132) add `dynamodb:GetItem` and `dynamodb:Query` on `etf-classifications` and its index ARN(s). Run
   `terraform fmt` and `terraform validate` only. Name the plan-to-be in the half.
5. Census from REAL local Holdings builds at all three firms, BEFORE (today's classifier) and AFTER (the table): write
   `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R25_ETF_CLASS_CENSUS_20260929.json` as
   `{"after_source": "etf-classifications", "firms": [{"firm", "as_of", "securities", "moved", "moves": [{"symbol",
   "before": {"asset_class", "sub_asset"}, "after": {"asset_class", "sub_asset"}}], "guessed": 0}],
   "positioning_readers": [<every reader of a PHYS row in Positioning, path:line>]}`.
6. Write the half `org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_ETF_CLASSIFICATIONS_20260929.md`
   (`## The act`, `## Blast radius` with the census and the local candidate diff, `Rollback per key`), covering both
   branches and every reader (the portal Holdings allocation bars / treemap / security list, exports, Positioning for
   PHYS). Name the release order: the seed write for PHYS, the IAM apply, then the Holdings re-mint; before the COT
   holdings gold re-point (S173).

### ACCEPTANCE

<criterion id="IBM25-251-AC1" cell_refs="IB-mr-251"><invocation>python -m pytest data/assets/scripts/gold/investor_reporting/tests/test_holdings_etf_classifications.py -q -p no:cacheprovider</invocation><expect>passed</expect></criterion>
`IBM25-251-AC1` -- classes come from the table, with no fold, and an unknown ticker refuses.

<criterion id="IBM25-251-AC2" cell_refs="IB-mr-251"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R25_CHECKS/r25_etf_class_census.py</invocation><expect>CLASS-CENSUS</expect></criterion>
`IBM25-251-AC2` -- real local builds at all three firms, every moved security listed, GLD/PHYS/VXX in their placed classes, nothing guessed, Positioning's PHYS readers named.

<criterion id="IBM25-251-AC3" cell_refs="IB-mr-251"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_CHECKS/r20_half_ready.py org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_ETF_CLASSIFICATIONS_20260929.md</invocation><expect>HALF-READY</expect></criterion>
`IBM25-251-AC3` -- the half, with its census, readers and release order, is written for the issuer to sign and send.

<expected_criteria>IBM25-251-AC1,IBM25-251-AC2,IBM25-251-AC3</expected_criteria>

Dry-run at the base 2026-09-29 18:4xZ: AC1 "no tests ran", AC2 NOT-CENSUSED (census absent), AC3 NOT-READY -- FAIL as
expected.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **LOCAL build + record.** No upload, no mint, no seed write, no `put-item`, no terraform apply or plan against a
  shared state. The local builds READ the firm buckets and the table.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row
  (id `IRPT_BCKEND-W84-S<k>`), and do not weaken the test to pass.

<paths>
data/assets/scripts/gold/investor_reporting/
infra/aws/lambda/v2_portal/_shared/etf_classification.py
infra/aws/terraform/investor-reporting/directory/holdings_refresh.tf
.tools/safe_deploy_core.py
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R25_ETF_CLASS_CENSUS_20260929.json
org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/NEVER_WIDEN_HALF_REQUEST_HOLDINGS_ETF_CLASSIFICATIONS_20260929.md
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP_R25_M.md</decomp_doc> (round 25, workstream ~M), cell `IB-mr-251`.
<owned_cells>IB-mr-251</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBM25-251-AC1, IBM25-251-AC2, IBM25-251-AC3. Instance at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~84/IRPT_BCKEND.TO-IB-m25-251.holdings-etf-classifications.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> IBM25-251-AC1,IBM25-251-AC2,IBM25-251-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the classification path and where it lives, the PHYS row, the closure change, the IAM diff, the census per
firm (moved/securities, the GLD/PHYS/VXX rows), the Positioning readers, the pytest line, the half's path, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule change; the served move rides a later Holdings re-mint under this cell's halves.
comp-iam: RUN -- holdings_refresh.tf ~:132 grants dynamodb:Scan per listed table; the client needs GetItem + Query on etf-classifications, drafted here and applied later under the halves.
comp-adversary: RUN -- 1 call-site read (holdings_snapshot.py canonical_classifier / classify_security, ~:828-873), 1 client read (etf_classifications_dynamodb.py: get_item by ticker, query on an index), 1 seed read (GLD present, PHYS absent); BLIND: the per-firm moved-security count is unmeasured at the cut (step 5 measures it) and the Positioning PHYS readers are untraced (step 5 names them).
lane: the <paths> block IS the grant; ~M owns the Holdings producer; the seed and IAM edits are desired, never applied here.
</preflight>

Source: CTO placement @c3c3f414dc (msg 102974); Andrew-direct 2026-09-29 ~17:4xZ (@099316efdd).

## AMENDMENT (2.0.0_SA_COO~M, 2026-10-01 ~04:4xZ) -- SUPERSEDED, on the CTO's sweep-5 analysis

Issuer act on 1.0.0_SA_CTO's ruling: `org/missions/D9/IRPT/IRPT_BCKEND/ledger/ROUND_ANALYSIS.sweep5.md`
@a50d8207bc section 2 item 4 ("RE-CUT, not drained and not retired"). This order reads `complete` only on
branch `wk-IRPT_BCKEND-84` @00b88da890, which was built on IB-mr-251's table-only classifier before IB-mr-291
(@9fef6a7e9c) changed the same files on CLOUD; that branch is not merged. No criterion of this order is claimed
as passed on CLOUD. The order is superseded, not complete.

**Superseded by:** IB-mr-291 (`IRPT_BCKEND.TO-IB-m29-291`, drained @9fef6a7e9c), the served class source: the
canonical table first with the declared bd-securities fallback. HOLD 103137 is unchanged for a table-only
class source.

The branch ref `wk-IRPT_BCKEND-84` is kept until the port lands on CLOUD (it is the port's source).
Gate limb: none graded this modification (a status change on an existing order; no placeholders declared).
