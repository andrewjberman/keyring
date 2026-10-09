# TO ADVI_BILLING.TO-AB-e-5 -- E3: the durable 49 Financial household crosswalk -- Schwab 0833 account to BD account, BD household (portal key) and Opal relationship -- one gold write

<to_id>ADVI_BILLING.TO-AB-e-5</to_id>
<project>ADVI_BILLING</project>
<issued_to>0.9.0_WK_ADVI_BILLING~3</issued_to>
<issued_by>2.0.0_SA_COO~B2</issued_by>
<issued_date>2026-10-09</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>

**Directive:** D8 | **Fabric:** dell2 | **PRD:** v0.2 @d45dc8a52f | **Decomp cell:** `AB-e-5` (decomposition section 3, round 2) | **outcome_ref:** FWD-1 / FWD-3 (E3) | **depends_on:** none.

---

## WORKER FACE

Your worktree is `C:/dev/wk-advi-billing-3`; run everything from its root. Your folder is
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~3/`.

**The cell.** The page addresses a household by Black Diamond's relationship id (z-form, e.g. `z08219260`); billing reads Schwab
master 0833 accounts. Round 1 bridged them through BD fee lines (few accounts). Measured by the issuer's research:
- `s3://opal-data-bd/silver/allocations/<date>.parquet` (134 files, newest 2026-10-02) carries `account_id` (BD z+10), `account_number` and
  `original_account_number` (custodian digits), `relationship_id` (z): 3,146 of 3,353 portal client keys reach a 0833 account; 5,149/5,149
  agreement with the stale xref `s3://opal-data-assets/blackdiamond/49f/silver/dim_account_xref/`.
- `s3://opal-data-bd/gold/dimensions/accounts_dimension_latest.parquet`: the BD account -> relationship spine (no custodian number).
- Schwab universe: `s3://opal-data-assets/schwab/08335338/silver/fact_acc/date=<d>/data.parquet` (`account_id`, 10 digits).
- Opal households: `s3://opal-data-49financial/gold/advi/dimensions/dim_relationship/date=<d>/`.
- Portal client keys: the prefixes under `s3://opal-data-bd/platinum/clients/` (3,353 z-keys).

1. `data/assets/scripts/gold/advi_billing/household_crosswalk.py`: one row per Schwab 0833 account (latest `fact_acc`):
   `schwab_account_number`, `bd_account_id`, `bd_relationship_id`, `opal_relationship_id`, `match_method` (e.g. `allocations_number`,
   `allocations_original_number`, `unmatched`), `claim` (measured | absent). Custodian digits are zero-padded to 10 and must exist in `fact_acc`.
2. Contract `org/standards/ADVI_BILLING_HOUSEHOLD_CROSSWALK_CONTRACT.json` (0.1.0): columns, meanings, the `match_method` enum.
3. ONE write with `--write` to `address("advi","49financial","gold","household_crosswalk","date=<run date>","household_crosswalk.parquet")`,
   under ledger `org/critical_paths/change_management/advi-billing-household-crosswalk-r2-20261009.md` + sentinel
   `org/critical_paths/.open_deploys/advi-billing-household-crosswalk-r2-20261009.json` (`python .tools/deploy_ledger.py --help`; if the tool
   prefixes the md file name with a timestamp, rename it to the granted name and fix the sentinel's `entry_path`).
4. Record `AB_E5_RECORD.json` in your folder: `date`, `s3_key` (the builder's exact output), `coverage` with `schwab_accounts_total`,
   `schwab_accounts_mapped`, `client_keys_total`, `client_keys_mapped`, `allocations_partition` (the partition read and its lag in trading
   days by `lib/trading_calendar.py`). No account number, name or figure in any committed file.

<criterion id="AB2-5-AC1" cell_refs="AB-e-5"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB2-5-AC1</invocation><expect>AB2-5-AC1 PASS</expect></criterion>
`AB2-5-AC1` -- the crosswalk at the builder address carries the contract columns and the record carries both coverage directions. Base: FAIL.

<criterion id="AB2-5-AC2" cell_refs="AB-e-5"><invocation>python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r2/r2_checks.py . AB2-5-AC2</invocation><expect>AB2-5-AC2 PASS</expect></criterion>
`AB2-5-AC2` -- seam probe against the real neighbour: the thread household's BD accounts in the crosswalk equal the served summary's accounts. Base: FAIL.

<expected_criteria>AB2-5-AC1,AB2-5-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited.
- S3 reads; exactly ONE S3 write (the crosswalk object) under its ledger; no overwrite of an existing key; no vendor call.
- **Refusal clause.** An edit outside the grant, a write the face does not name, a vendor call, a secret read, or an account
  number, name or dollar figure in a committed file is a defect: stop and file a row.

<paths>
data/assets/scripts/gold/advi_billing/household_crosswalk.py
org/standards/ADVI_BILLING_HOUSEHOLD_CROSSWALK_CONTRACT.json
org/critical_paths/change_management/advi-billing-household-crosswalk-r2-20261009.md
org/critical_paths/.open_deploys/advi-billing-household-crosswalk-r2-20261009.json
org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~3/
org/missions/D8/ADVI/ADVI_BILLING/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D8/ADVI/ADVI_BILLING/task-orders/ADVI_BILLING.TO-AB-e-5.household-crosswalk.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_BILLING/decompositions/ADVI_BILLING_DECOMP.md</decomp_doc> section 3 (round 2), cell `AB-e-5`.
<owned_cells>AB-e-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AB2-5-AC1, AB2-5-AC2. The instance goes at
`org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~3/ADVI_BILLING.TO-AB-e-5.household-crosswalk.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> AB2-5-AC1,AB2-5-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** commit hashes, each criterion's last line, what the cell measured (counts, classes, masked ids only), and every row id.

---

## RECORD FACE

<preflight>
comp-blast: RUN -- ONE new gold key under a new table; 0 existing readers.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no role is created or changed in this cell.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route changes.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: enrichment cell; no served claim is graded here.
checks dry-run at base: AB2-5-AC1, AB2-5-AC2 FAIL as expected.
lane: the <paths> block IS the grant.
</preflight>
