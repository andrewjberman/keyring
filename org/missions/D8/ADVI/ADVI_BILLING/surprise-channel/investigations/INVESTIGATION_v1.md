# ADVI_BILLING -- surprise channel, INVESTIGATION v1 (round 1, laptop fabric)

**Home:** the project tree's channel; the gate `.tools/surprise-row-gate.py` validates every NEW row (schema
`org/surprise_channel/schemas/investigation_item.schema.json`). Lane `ANY`. A worker's row is `ADVI_BILLING-W<n>-S<k>`.
**Append-only during the round.** Never edit an existing row.

## ADVI_BILLING-W1-S1 -- The crosswalk rel_to_z_mapping.json that the AB-t-1 household rule and the page's client_key depend on exists 

```json
{
  "id": "ADVI_BILLING-W1-S1",
  "project": "ADVI_BILLING",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~1",
  "surfaced_at": "2026-10-09T06:05Z",
  "one_line": "The crosswalk rel_to_z_mapping.json that the AB-t-1 household rule and the page's client_key depend on exists on no durable plane, so no client_key can be resolved and the one permitted S3 write was not made.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "data/assets/scripts/gold/runners_49f/d05_client_detail.py:72 reads Path(xwalk_dir)/'rel_to_z_mapping.json' and :74 bd_map.parquet beside it; --xwalk-dir is an operator argument (:202), runners_49f/d_publisher_port.py:379 only passes it through, chain_49f_entrypoint.py carries no xwalk reference",
      "org/tier2_senior/0.4.0_DS_ClientPlatform~A/deliverables/OPAL_ADVIPOINTERS_P1_CLOSE_49F_BACKFILL_PRICED_CARD_20260818.md:37 'xwalk harvest (rel_to_z_mapping.json + bd_map.parquet; d05/d14) MEASURED zero on every durable plane (repo + S3 staging prefixes)' -- re-harvest from the served detail family",
      "comp-find --name rel_to_z_mapping . : 0 hits across 70361 files (corpus=all); comp-find content 'rel_to_z_mapping' : hits only in d05, d14, docs and audit logs, no data file",
      "aws s3 ls --recursive key census, rc 0, grep xwalk|rel_to_z|bd_map = 0 matches: opal-data-49financial 50,502 keys; opal-data-bd 131,284; opal-data-harvest 47,120; opal-data-security 17,235; opal-data-irpt 485; opal-runner-shared 6; opal-313476888478-yang-qa-scratch 0; opalinvest-portal ListBucket AccessDenied for this principal; opal-data-assets not enumerated (top level + gold/ + portal/gold/ read, no such prefix)",
      "find over /c/Users/Test and /c/dev depth 6 for rel_to_z*, bd_map.parquet, aligned_value_parity.json: 0 files"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AB-t-1 step 2 and the known-list: pick a household with an EXACT row in rel_to_z_mapping.json; find the crosswalk's location from d05's --xwalk-dir and its runner; the page addresses a household by its rel_z client_key.",
  "world_is": "No runner supplies --xwalk-dir and no copy of rel_to_z_mapping.json exists in the repo, any bucket this principal can enumerate, or the local disk; the file is a session-local QA artifact re-harvested from the served gold/entities/clients/{z}/detail.json family. Without it relationship_id cannot be mapped to a rel_z client_key. The worker built the builder to read the crosswalk from --xwalk-dir and did NOT invent a key or write the object; AB1-1-AC1/AC2/AC3 remain FAIL. Issuer options: supply the crosswalk file (or re-harvest it), or rule that the thread client_key is the dim_relationship relationship_id."
}
```

## ADVI_BILLING-W1-S2 -- The single ADVISOR rate 0.003175 reproduces almost none of the 07-07 TPFEE debits: the implied annual rate (de

```json
{
  "id": "ADVI_BILLING-W1-S2",
  "project": "ADVI_BILLING",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~1",
  "surfaced_at": "2026-10-09T06:15Z",
  "one_line": "The single ADVISOR rate 0.003175 reproduces almost none of the 07-07 TPFEE debits: the implied annual rate (debit / (value x 64/251)) clusters near 0.0099 across the book, so most accounts will grade DIFFERS against a constant schedule.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3://opal-data-assets/schwab/08335338/silver/fact_trn/date=2026-07-07: 5,469 customer-account TPFEE DEBIT rows (one per account) plus one collector account carrying 5,469 CREDIT rows; fact_rps value summed per account at 2026-06-30, 07-01, 07-02, 07-06",
      "ADVISOR estimate at 0.003175 x 64/251 equals the debit to within 0.01 USD for 1-2 of ~5,310 joined accounts per candidate date and within 1 USD for 34-35; median debit/estimate ratio 3.14-3.17 (about 0.01/0.003175)",
      "implied annual rate over 5,263 accounts with value > 1,000 USD: modal 0.0099 (value-date drift spreads it 0.0098-0.0100), second cluster 0.0124 (~84 accounts); accounts within 2e-5 of 0.003175: 1-2 per date"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AB-t-1 step 4/5 and the known-list: Q3 2026 ADVISOR rate 0.003175 (debited as TPFEE on 2026-07-07) applied as value x rate x 64 / 251.",
  "world_is": "The book's TPFEE debits imply a per-account annual rate (modal about 1.00 percent, a second cluster near 1.24 percent), so 0.003175 is one account class's rate, not the book's. The builder carries the order's rate as the schedule constant (schedule_claim measured, as ordered) and a household's DIFFERS reasons name the rate gap; per-account rates exist in jd2 dim_advisor_fee_role annual_fee_bps (read by d05) and in Black Diamond silver/fees basis_points, which AB-t-1 does not use as the schedule."
}
```

## ADVI_BILLING-W1-S3 -- The PLATFORM rate 0.0004395 fits the 07-21 SMFEE debits no better: the implied annual rate is modal 0.0039 (ab

```json
{
  "id": "ADVI_BILLING-W1-S3",
  "project": "ADVI_BILLING",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~1",
  "surfaced_at": "2026-10-09T06:35Z",
  "one_line": "The PLATFORM rate 0.0004395 fits the 07-21 SMFEE debits no better: the implied annual rate is modal 0.0039 (about nine times the schedule constant), so no account in the book is expected to grade MATCH on either component.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "s3://opal-data-assets/schwab/08335338/silver/fact_trn/date=2026-07-21: 5,864 SMFEE rows, all DEBIT, one per account; fact_rps value on 2026-07-06 summed per account",
      "5,630 accounts with value > 1,000 USD: implied annual rate debit/(value x 64/251) = 0.0039 for 3,330, 0.0040 for 440, 0.0038 for 440, 0.0041 for 159; accounts within 5 percent of 0.0004395: 1; |estimate - debit| <= 0.01 USD: 0; <= 1 USD: 22",
      "the dry-run of data/assets/scripts/gold/advi_billing/fee_quarter.py on one single-account household (synthetic crosswalk in .scratch, nothing written) graded both components DIFFERS with implied rates 0.00990 and 0.00386"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AB-t-1 known-list: PLATFORM (SMArtX) 0.0004395 debited as SMFEE on 2026-07-21, same formula and Days in Period.",
  "world_is": "The SMFEE debits imply about 0.0039 annually. The sum of the two order constants is 0.0036145, still not 0.0039, so neither the labels nor the constants are established as this book's per-account rates; the SMArtX statement (SharePoint, not readable by the worker) is the authority and the issuer's rate read may be one allocation row. The builder carries the order's constants and names the rate gap per component; it also means the valuation-date test (step 3) is dominated by the rate gap and separates the candidates by under 1 percent."
}
```

## ADVI_BILLING-W1-S4 -- Amendment 1's pick rule is met by no household when every account's fee line must fall in July 2026; the thread household uses the latest earlier fee line for one account

```json
{
  "id": "ADVI_BILLING-W1-S4",
  "project": "ADVI_BILLING",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~1",
  "surfaced_at": "2026-10-09T06:45Z",
  "one_line": "BD fee lines are sparse (201 lines in the 31 July 2026 partitions), so no 1-4 account served summary has a July 2026 bps>0 line on every account; four households meet the rule only by reading an account's latest earlier 2026 line.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "python data/assets/scripts/gold/advi_billing/fee_quarter.py --pick (run at ef273b0404+ base bab1baa62f): 'rule ... 0 households with every account's fee line in 2026-07, 4 accepting the latest earlier line'",
      "silver/fees/2026-07-*.parquet: 31 partitions, 201 lines, 36 with basis_points > 0; silver/fees/2026-*.parquet up to 07-31: 212 partitions, 228,369 lines",
      "the four households (accounts): z08219260 (2), z08351415 (2), z08132190 (3), z08361443 (3); thread household z08219260: ...8814 has a July line (partition 2026-07-25, '49F - Flat 1', 100 bps), ...3738 has none in July (latest earlier line carries the same label and 100 bps)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 1 A2 pick rule: 1-4 accounts, EVERY account with a July 2026 BD fee line with basis_points > 0 and a TPFEE row on 2026-07-07; the issuer measured candidates meeting it.",
  "world_is": "No household of 1-4 accounts meets the rule as worded. The builder accepts, for an account with no July line, its latest earlier 2026 fee line (same schedule label), emits that account's schedule_claim as inferred (not measured) and names the partition in schedule_source. The thread household (z08219260, the first by fewest accounts then id) therefore carries one measured and one inferred account. The issuer decides whether the rule is to be read this way or the wording amended."
}
```

## ADVI_BILLING-W1-S5 -- The contract gains a component-level schedule_claim, and the household debited_fee is like-for-like with the computed fee

```json
{
  "id": "ADVI_BILLING-W1-S5",
  "project": "ADVI_BILLING",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~1",
  "surfaced_at": "2026-10-09T06:45Z",
  "one_line": "A3 asks for a null PLATFORM rate with 'schedule_claim absent', but schedule_claim is an account-level field that stays measured/inferred for the ADVISOR schedule; the contract adds schedule_claim to each component, and the household debited_fee sums only components that have a computed fee.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json at bab1baa62f: components[].schedule_claim (additive, enum measured|inferred|held|absent); household.debited_fee meaning",
      "org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r1/r1_checks.py validate_contract_shape: checks required keys only, so the extra key passes AB1-1-AC1"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AMENDMENT 1 A3: rate and computed_fee null only when schedule_claim is absent; household computed totals sum the non-null components. The contract field list carries one schedule_claim per account.",
  "world_is": "With a null PLATFORM rate beside an account whose schedule_claim is measured, the contract's null-only-when-absent rule cannot be read off the account field, so each component carries its own schedule_claim (ADVISOR = the account's, PLATFORM = absent). The amendment is silent on the household debited total; summing the SMFEE debits against a computed total that excludes the platform portion would put a number in difference that means nothing, so the household compares the ADVISOR components with their own TPFEE debits and says so in steps. AB-t-3's fixture and AB-t-2's reader must carry the added key or ignore it."
}
```
