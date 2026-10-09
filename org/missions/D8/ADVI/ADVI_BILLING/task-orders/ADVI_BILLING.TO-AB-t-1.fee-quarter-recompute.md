# TO ADVI_BILLING.TO-AB-t-1 -- FWD-1 hops 1-2: one 49 Financial household's Q3 2026 advisory fee recomputed from Opal's Schwab data, written as one gold object, compared once with what Schwab debited

<to_id>ADVI_BILLING.TO-AB-t-1</to_id>
<project>ADVI_BILLING</project>
<issued_to>0.9.0_WK_ADVI_BILLING~1</issued_to>
<issued_by>2.0.0_SA_COO~B2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>

**Directive:** D8 | **Fabric:** dell2 | **PRD:** v0.2 @d45dc8a52f (ADMITTED) | **Decomp cell:** `AB-t-1` (decomposition section 2) | **outcome_ref:** FWD-1 | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-advi-billing-1`; run everything from its root. Your folder is
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~1/`. After this order you will be handed
`ADVI_BILLING.TO-AB-t-2` (the read route over the object you write), so leave the object in place.

**The outcome (FWD-1).** For one 49 Financial household and one quarter already billed, the advisory fee is worked out from
Opal's own Schwab values, an advisor reads it in Opal, and it equals what Schwab debited, or the difference is shown with
its reason. This cell builds the calculation and the one comparison. A one-time check, never a standing comparator.

**What is known (measured by the issuer at the cut; do not re-derive, do verify where you read):**
- 49 Financial is billed by SMArtX, IN ADVANCE, one row per account allocation. SMArtX's formula: fee = valuation x rate x
  `Days in Period` / 251, where Days in Period counts trading days (64 for Q3 2026, Jul 1 - Sep 30). Q3 2026 rates:
  ADVISOR 0.003175 (debited by Schwab as `tran_srcde = TPFEE`, "TO ADVISOR", on 2026-07-07) and PLATFORM (SMArtX) 0.0004395
  (debited as `SMFEE`, on 2026-07-21). The 07-07 debit also carries a prior-quarter TRUE-UP whose method is not known.
  Source: SharePoint `Shared/Documents/Billing/49F/` SMArtX statements and `Opal Billing Master.xlsx` (you cannot read them;
  write `schedule_source` as `SMArtX 49F Fee Statement / Deficit Report 2026Q3 (SharePoint Shared/Documents/Billing/49F), rates
  read by 2.0.0_SA_COO~B2 2026-10-09` and `schedule_claim` as `measured`).
- Schwab master 0833 silver: `s3://opal-data-assets/schwab/08335338/silver/fact_{acc,rps,trn,fam}/date=YYYY-MM-DD/data.parquet`
  (2024-07-08 .. 2026-10-07). Value: `fact_rps.market_value_settled_unsettled` by `account_id` (10-digit) and `business_date`.
  Debits: `fact_trn` `tran_srcde`, amount in `gross_amount`. 07-07: 10,938 TPFEE rows, 0 SMFEE. 07-21: 5,864 SMFEE, 33 TPFEE.
- Households: `s3://opal-data-49financial/gold/advi/dimensions/dim_relationship/date=.../` (`data/assets/scripts/gold/runners_49f/a01_dim_relationship.py`).
  The page addresses a household by its portal `client_key` (`rel_z...`): the EXACT rows of `rel_to_z_mapping.json`, read by
  `data/assets/scripts/gold/runners_49f/d05_client_detail.py:72-84` (find the crosswalk's location from that script's
  `--xwalk-dir` and its runner).
- Flows: gold `s3://opal-data-49financial/gold/advi/canonical/flow_ledger/` (`runners_49f/c00_flow_ledger.py`).
- Black Diamond's fee line (`s3://opal-data-bd/silver/fees/<date>.parquet`; bridge `s3://opal-data-bd/schwab/silver/account_xref/date=20260629/`,
  which may carry master 0824 only) is a SECONDARY reference: print it beside the account where the bridge reaches it, record a
  miss, never block on it.

**Build.**
1. `data/assets/scripts/gold/advi_billing/fee_quarter.py` (with `__init__.py` if needed): arguments `--quarter 2026Q3
   --client-key <rel_z...> [--write]`. Without `--write` it prints the object; with it, it writes ONE object to the address
   `lib/opal_naming.py` returns: `address("advi","49financial","gold","advi_billing","quarter=2026Q3","<client_key>.json")`
   (= `s3://opal-data-49financial/advi/49financial/gold/advi_billing/quarter=2026Q3/<client_key>.json`). Never type a bucket or key; read inputs by the live keys above.
2. Pick the thread household by rule and record it: 1-4 accounts, an EXACT crosswalk row, every account with a TPFEE row on
   2026-07-07. Prefer the smallest such household.
3. Valuation date: SMArtX's "Current Period Estimate Valuation" date is unknown. Test the candidates 2026-06-30, 2026-07-01 and
   the last business day before 2026-07-07; record per candidate the absolute difference of the ADVISOR estimate from the debit;
   choose the one that reproduces the debits best and say how well.
4. Per account: billable value, schedule (`label`, `rate_type`, `basis_points`, `flat_fee`, `tiers` = []), both components
   (ADVISOR/TPFEE, PLATFORM/SMFEE) with `computed_fee`, `debited_fee` (sum of that code's `gross_amount` for the account on that
   component's `debit_date`, as a positive number), `difference`, `reconcile_class`. Household totals the accounts.
5. `reconcile_class`: `NO_DEBIT` (no row for that code on its debit date; `debit_date` then null), `MATCH` (|difference| <=
   0.01 USD), `DIFFERS` (larger). `difference_reason` is required on DIFFERS and null otherwise. Name the true-up as the reason
   when the residual looks like it. Re-debits (07-21 TPFEE) and low-cash failures are reasons too.
6. `steps[]`: at least 3 plain-English lines an advisor reads to answer "why is my fee this number?".
7. Write `org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json` (`contract_version` "0.1.0"): every field below with type and
   meaning, the `reconcile_class` enum with its rule-24 record (domain = one account|household x quarter after the fee is
   computed; members NO_DEBIT / MATCH / DIFFERS from {debit present?} x {|diff| <= 0.01}; one axis = agreement with Schwab, not
   which side is right; a schedule fix moves `computed_fee`, never `debited_fee`), and the claim fields' enum
   (measured | inferred | held | absent). Fields:
   ```
   contract_version, firm ("49financial"), relationship_id, client_key, quarter, billing_convention (ADVANCE|ARREARS|UNRESOLVED),
   billing_convention_claim, period_start, period_end, valuation_date, as_of,
   accounts[]: { account_id, billable_value, value_source, schedule{label,rate_type,basis_points,flat_fee,tiers[]},
                 schedule_claim, schedule_source, flow_adjustment, flows_in_period[], excluded_value, exclusion_reason,
                 days_in_period, days_in_year,
                 components[]: { portion (ADVISOR|PLATFORM), rate, debit_code (TPFEE|SMFEE), computed_fee, debited_fee,
                                 debit_date, difference, reconcile_class, difference_reason } },
   household: { billable_value, computed_fee, debited_fee, difference, reconcile_class, difference_reason },
   steps[]
   ```
8. Run it once with `--write` for the thread household. Open the ledger first and close it after the write:
   `org/critical_paths/change_management/advi-billing-fee-quarter-49f-r1-20261009.md` with its sentinel
   `org/critical_paths/.open_deploys/advi-billing-fee-quarter-49f-r1-20261009.json` (use `python .tools/deploy_ledger.py --help`).
9. Record `AB_T1_RECORD.json` in your folder: `relationship_id`, `client_key`, `quarter`, `s3_key` (the builder's exact output),
   `valuation_date_candidates` (list of {date, advisor_abs_diff_class}), `valuation_date_chosen`, `household_selection_rule`,
   `bd_reference` (reached | bridge-miss), class counts. **No dollar figure, client name or full account number in any
   committed file**: figures live only in the S3 object; records carry classes, counts and masked ids (last 4).

<criterion id="AB1-1-AC1" cell_refs="AB-t-1"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r1/r1_checks.py . AB1-1-AC1</invocation><expect>AB1-1-AC1 PASS</expect></criterion>
`AB1-1-AC1` -- the object at the builder address conforms to the contract. Base: FAIL.

<criterion id="AB1-1-AC2" cell_refs="AB-t-1"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r1/r1_checks.py . AB1-1-AC2</invocation><expect>AB1-1-AC2 PASS</expect></criterion>
`AB1-1-AC2` -- seam probe against the real neighbour: every component's `debited_fee` equals Schwab 0833 `fact_trn` on its debit date. Base: FAIL.

<criterion id="AB1-1-AC3" cell_refs="AB-t-1"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r1/r1_checks.py . AB1-1-AC3</invocation><expect>AB1-1-AC3 PASS</expect></criterion>
`AB1-1-AC3` -- the contract file carries every field at 0.1.0, and the valuation-date test is recorded. Base: FAIL.

<expected_criteria>AB1-1-AC1,AB1-1-AC2,AB1-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- **AWS:** S3 reads; exactly ONE S3 write, the object in step 8, under its ledger. No vendor call (Black Diamond, SMArtX, Schwab),
  no secret read, no deploy, no delete.
- **Refusal clause.** A second S3 write, a write to any existing key, a vendor call, an edit outside the grant, or a dollar
  figure, client name or full account number in a committed file is a defect: stop and file a row.

<paths>
data/assets/scripts/gold/advi_billing/
org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json
org/critical_paths/change_management/advi-billing-fee-quarter-49f-r1-20261009.md
org/critical_paths/.open_deploys/advi-billing-fee-quarter-49f-r1-20261009.json
org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~1/
org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_BILLING/task-orders/ADVI_BILLING.TO-AB-t-1.fee-quarter-recompute.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BILLING/decompositions/ADVI_BILLING_DECOMP.md</decomp_doc> section 2 (round 1), cell `AB-t-1`.
<owned_cells>AB-t-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AB1-1-AC1, AB1-1-AC2, AB1-1-AC3. The instance goes at
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~1/ADVI_BILLING.TO-AB-t-1.fee-quarter-recompute.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AB1-1-AC1,AB1-1-AC2,AB1-1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, the household rule and masked ids, the chosen valuation date and how
well each candidate reproduced the debits, the class counts per component, the BD reference result, the ledger, and every row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one NEW gold key under a NEW prefix (advi/49financial/gold/advi_billing/); 0 existing readers.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: S3 reads and one write from this box's credentials; no role is created or changed in this cell.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: thread round; no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: thread round; the lens runs on the enrichment round that touches its surface.
checks dry-run at base: AB1-1-AC1/AC2/AC3 FAIL as expected; validator GREEN arm '' and RED arm (DIFFERS without reason) refused.
lane: the <paths> block IS the grant.
</preflight>
