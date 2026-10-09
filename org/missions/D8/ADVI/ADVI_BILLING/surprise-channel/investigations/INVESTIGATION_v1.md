# ADVI_BILLING -- surprise channel, INVESTIGATION v1

**Home:** the project tree's channel; rows are validated by `.tools/surprise-row-gate.py`. A seat's row is `ADVI_BILLING-S<k>`; a worker's is `ADVI_BILLING-W<n>-S<k>`. **Append-only during the round.**

## ADVI_BILLING-D2-W2-S1 -- The order says call the fee-quarter route with the same apiRequest as getPlatinumClientSum

```json
{
  "id": "ADVI_BILLING-D2-W2-S1",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~2",
  "surfaced_at": "2026-10-09T05:42Z",
  "one_line": "The order says call the fee-quarter route with the same apiRequest as getPlatinumClientSummary, but that apiRequest is module-private, so advi-billing.ts carries its own minimal copy.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "portal/src/api/endpoints/advisor-intelligence.ts@2d42e9b7 line 232: 'async function apiRequest<T>' with no export; grep of the file for 'export.*apiRequest' returned nothing",
      "the same file is outside this cell's <paths> (read-only), so exporting it is not mine to do"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "getFeeQuarter calls its route 'exactly as getPlatinumClientSummary calls its route (same apiRequest, same firmId rule)'.",
  "world_is": "apiRequest is not exported and advisor-intelligence.ts is not in the grant. advi-billing.ts holds a local apiRequest with the same GET, bearer token, 30 s abort and the same ?firmId= rule, but without the NaN/Infinity strip and the chain-timestamp cache interceptor. If the issuer wants the shared helper, exporting it from advisor-intelligence.ts and swapping the import is a two-line change at the merge."
}
```

## ADVI_BILLING-D2-W2-S2 -- The order says use formatCurrency, which rounds to 3 significant digits ($4,360.54 prints 

```json
{
  "id": "ADVI_BILLING-D2-W2-S2",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~2",
  "surfaced_at": "2026-10-09T05:42Z",
  "one_line": "The order says use formatCurrency, which rounds to 3 significant digits ($4,360.54 prints as $4.36K), so the panel formats money to the cent with Intl instead.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "bun run on portal/src/lib/universalNumberFormatter.ts@2d42e9b7: formatCurrency(1234.56)='$1.23K', formatCurrency(1250000.45)='$1.25M', formatCurrency(612345.67)='$612K'",
      "a $2.50 platform-fee difference in the fixture cannot be shown if both sides render as '$471'"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "'Use the page's own kit: Panel, PanelHeader, PanelContent from @/ui/components/panels, formatCurrency from @/lib/universalNumberFormatter, HelperTip'.",
  "world_is": "Panel, PanelHeader, PanelContent and HelperTip are used. formatCurrency is not: AdvisorBookFeePanel.tsx formats every dollar value with a local Intl.NumberFormat (two decimals) because the panel's job is a cent-level reconciliation. Swapping to formatCurrency is a one-function change if the issuer prefers the compact form."
}
```

## ADVI_BILLING-D2-W2-S3 -- The contract gives components[].rate no unit and the flow entries no shape; the panel assu

```json
{
  "id": "ADVI_BILLING-D2-W2-S3",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~2",
  "surfaced_at": "2026-10-09T05:42Z",
  "one_line": "The contract gives components[].rate no unit and the flow entries no shape; the panel assumes rate is an annual decimal fraction (0.0085 = 85 bps) and reads flows as {date, amount, note}.",
  "class": "OBSERVATION",
  "hazard_standing": "ARMED",
  "disarm_owner": "2.0.0_SA_COO~B2: before the merge, confirm against org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json (or the AB-t-1 object) that components[].rate is a decimal fraction; if it is already in bps the panel shows 100x too many bps",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "the order's contract block lists 'rate' and 'flows_in_period[]' with no unit or element fields; schedule carries a separate 'basis_points' field, which suggests rate is not in bps",
      "org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json was not present in the worktree at HEAD 57dd6256e1 (ls org/standards | grep ADVI_BILL returned nothing)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The panel shows 'the schedule (rate as bps)' and 'flow adjustment ... when non-zero' from fields the contract lists by name only.",
  "world_is": "Unit of components[].rate and the element shape of flows_in_period are unstated here. The panel multiplies rate by 10000 for display and renders each flow as 'date - signed amount - note', skipping missing keys, so a different shape degrades to fewer words rather than failing. The fixture uses the same assumption, so AB1-3-AC2 does not test it."
}
```

## ADVI_BILLING-D2-W2-S4 -- The commit-time naming gate refused the literal '49financial' in the fixture's firm field,

```json
{
  "id": "ADVI_BILLING-D2-W2-S4",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~2",
  "surfaced_at": "2026-10-09T05:55Z",
  "one_line": "The commit-time naming gate refused the literal '49financial' in the fixture's firm field, so the fixture carries firm 'example-firm' instead of the contract's example value.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit in the portal worktree, 2026-10-09: 'NAMING REFUSE src/pages/AdvisorIntelligence/_shared/__fixtures__/adviBillingFeeQuarter.json:3 49financial -> lookup(...)  why: NEW hand-kept carrier (context rule)'",
      "after the change the same commit passed: 'NAMING-GATE: PASS 0 graded'; the AB1-3-AC2 validator checks only that the key 'firm' is present, so it still passes on the fixture",
      "the portal worktree repo also has no committer identity configured (fatal: unable to auto-detect email address); the commit used GIT_COMMITTER_NAME and GIT_COMMITTER_EMAIL set for that call only"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "The contract lists firm (\"49financial\") and the fixture is 'an example object of the contract'.",
  "world_is": "A hand-typed '49financial' in a new portal file is refused by the naming limb (LGIC_ENFORCE). The fixture's firm value is 'example-firm'; nothing in the panel reads it. The real object from AB-t-1 carries the registered value."
}
```

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

## ADVI_BILLING-W1-S6 -- The partners relationship platinum-summary route applies no per-advisor book check and its pseudonymizer is a retired no-op; the read route reuses exactly that

```json
{
  "id": "ADVI_BILLING-W1-S6",
  "project": "ADVI_BILLING",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~1",
  "surfaced_at": "2026-10-09T07:10Z",
  "one_line": "The order asks that the viewer be scoped to the firm, the advisor's book and pseudonymization as opal-partners-data scopes its relationship routes, but that route's code checks the firm only (is_authorized) and pseudonymize_response returns the body unchanged (needs_pseudonymization is False).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/lambda_function.py:1816-1870: for /scoped/partners/books/relationship/{id}/platinum-summary the checks are the authorizer allowedFirmIds, is_authorized(firm_id), get_firm_bucket, _validate_entity_id, then _pseudonymize_s3_response; the L1 advisor-path check (:1685-1697) applies to '/advisors/' and '/books/advisor/' paths only",
      "infra/aws/lambda/v2_portal/partners/lambdas/opal-partners-data/pseudonymizer.py:66-75 needs_pseudonymization() returns False ('Pseudonymization retired 2026-04-15 per Andrew'); pseudonymize_response returns the body unchanged",
      "infra/aws/lambda/advi/billing-read/entry.py at this commit: 401 for no authorizer context, a firm outside allowedFirmIds, or any firm other than the one served; 400 for a bad clientKey or quarter; all before any S3 read (tests test_refused_*)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AB-t-2 'Who may read': scope the viewer exactly as opal-partners-data scopes its relationship routes -- firm from the claims (49 Financial only), the advisor's book, pseudonymization of PII; a viewer outside the firm or outside the household's book gets a refusal and NO S3 read.",
  "world_is": "The cited code does the firm check and the (no-op) pseudonymization; it has no check that the viewer's advisor owns the household, so none is applied here either and an in-firm viewer of any advisor can read any household's fee object. The coordinator's instruction to scope exactly as that route was followed. A book check would need the household's advisor attribution (the platinum summary's team_attribution advisor ids, a different prefix the role does not read) and is the issuer's call."
}
```

## ADVI_BILLING-W1-S7 -- The page's clientKey is the Black Diamond relationship_id (z-form), not rel_; the route accepts both forms

```json
{
  "id": "ADVI_BILLING-W1-S7",
  "project": "ADVI_BILLING",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~1",
  "surfaced_at": "2026-10-09T07:10Z",
  "one_line": "The order's clientKey pattern ^rel_[A-Za-z0-9_]+$ would 400 the AB-t-1 household (client_key z08219260); the route accepts ^(rel_|z)[A-Za-z0-9_]+$.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BILLING/deliverables/0.9.0_WK_ADVI_BILLING~1/AB_T1_RECORD.json: client_key z08219260, relationship_id rel_542a59c41291e9",
      "coordinator message after AB-t-1: 'the page's clientKey is the Black Diamond relationship_id (z-form)'",
      "infra/aws/lambda/advi/billing-read/tests/test_billing_read.py test_refused_bad_path_parameters_400_no_s3_read: path-traversal and off-pattern keys 400, the z-form key is served"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AB-t-2: clientKey must match ^rel_[A-Za-z0-9_]+$; anything else is 400.",
  "world_is": "The object is keyed by the BD z-form relationship_id (AMENDMENT 1 A1), which the stated pattern refuses. The accepted pattern keeps the character class (no slash or dot) so a key cannot leave the quarter prefix."
}
```

## ADVI_BILLING-W1-S8 -- The criterion check parses un-coloured pytest output, and this box exports FORCE_COLOR=3, so AB1-2-AC1 fails on correct tests until a conftest turns colour off

```json
{
  "id": "ADVI_BILLING-W1-S8",
  "project": "ADVI_BILLING",
  "fabric": "laptop",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~1",
  "surfaced_at": "2026-10-09T07:10Z",
  "one_line": "r1_checks.py ac_2_1 matches ^PASSED <file>::<test> from pytest -rA, but FORCE_COLOR=3 in the environment wraps those lines in ANSI escapes, so it read passed=[] with pytest rc 0.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "env: FORCE_COLOR=3; python org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/checks/r1/r1_checks.py . AB1-2-AC1 -> 'need a passing test named *real_object* and one named *refused*; passed=[]' with 16 tests passing",
      "after infra/aws/lambda/advi/billing-read/tests/conftest.py (config.option.color = 'no'): AB1-2-AC1 PASS"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AB1-2-AC1 PASS when the local-invoke tests pass, one serving the real object and one refusing an out-of-scope viewer.",
  "world_is": "The check is environment-sensitive. The conftest in the order's own tests directory makes the output plain on any box; any other test directory the same check grades (AB-t-3 uses bun) is unaffected."
}
```

## ADVI_BILLING-D2-S1 -- L9 AB1-3-AC3 MET

```json
{
  "id": "ADVI_BILLING-D2-S1",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T07:44:05Z",
  "one_line": "L9 AB1-3-AC3 MET: on the real-data render (viewed by this seat on dell2, sha256 efc9ee5e... matches the record; not copied anywhere), the 'Fee for 2026Q3' panel alone answers 'why is my fee this number': each account shows its schedule (49F - Flat 1, 100 bps), the value charged, 64 of 251 days, the computed fee, the Schwab debit and the difference, each line labelled 'Differs from Schwab' with a reason; 'How the fee is built' gives value x 0.01 x 64/251 per account and the household sum; the platform fee says plainly its schedule is not held in Opal. The difference reasons are stated as candidates (valuation basis, prior-quarter true-up) with the method marked unknown -- honest, and within FWD-1's ACCEPT branch.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/r1_close/REAL_RUN_FWD1_R1.md @b44766f7ef",
      "C:/dev/advi_billing_private/r1_close/realrun_fee_panel.png (dell2, outside git; this seat's sha256 prefix efc9ee5ed31476a7)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BILLING_ROUND_1_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AB1-3-AC3: an advisor can answer 'why is my fee this number?' from the panel alone.",
  "world_is": "Met; notes in the grade file."
}
```

## ADVI_BILLING-D2-W4-S1 -- The 5 advisorKeys hold no account in any role in the source, so adding them to the map gives them present-but-EMPTY entries: the 'not in ownership map

```json
{
  "id": "ADVI_BILLING-D2-W4-S1",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~4",
  "surfaced_at": "2026-10-09T08:40:00Z",
  "one_line": "The 5 advisorKeys hold no account in any role in the source, so adding them to the map gives them present-but-EMPTY entries: the 'not in ownership map' refusal is cured, a per-household grant is not (and 2 of the 5 are firmRole admin, already bypassing the check)",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "OWNERSHIP_GAP_R2.json (this worker's folder): relationships_per_added_advisor 0 x5; accounts 0 x5",
      "jd2 dim_advisor_fee_role: none of the 5 slugs appears in any role column of any of 53 partitions sampled (first, middle, 2026-09-28)",
      "infra/aws/lambda-edge/auth-validator-edge/index.mjs:469-470 (isAdmin = role admin or firmRole admin) so luke_winskowski and test_regression_49f bypass the check"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO face: the 5 advisors 'are refused their own books'; the fix makes the 5 keys appear and counts their relationships.",
  "world_is": "The advisors own no household in the source (account-team assignment), so 'their own books' is empty. After the fix, dan_wohlgemuth, lizah_okoniewski, test_regression_49f_adv are present with empty lists (still 403 on any relationship, now 'not authorized' rather than 'not in map'). Granting them households needs an account-team assignment in the source, not a producer change. Key format matches (advisorName slug == advisorKey) except the two test_regression keys, which have no name-derived form."
}
```

## ADVI_BILLING-D2-W4-S2 -- The served map is produced by the legacy D_00.portal_aggregates (z-id grammar, 191 advisors, generated today), not by d08; the d08 fix reaches the ser

```json
{
  "id": "ADVI_BILLING-D2-W4-S2",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~4",
  "surfaced_at": "2026-10-09T08:40:00Z",
  "one_line": "The served map is produced by the legacy D_00.portal_aggregates (z-id grammar, 191 advisors, generated today), not by d08; the d08 fix reaches the served map only at the cutover, and D_00 has the same universe law",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "live map generated_at 2026-10-09T05:27Z, 191 advisors, relationship ids z-form; d08 produces rel_ hash ids and 149 advisors on the same day's inputs",
      "data/black_diamond/scripts/gold/D_00.portal_aggregates.py:550-607 _build_advisor_ownership_map (melts the 5 role columns, drops advisors with no account/relationship)",
      "data/assets/scripts/gold/runners_49f/d08_firm_ownership_map.py module docstring: identity-spine divergence declared by design"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO face: 'the map is produced by d08_firm_ownership_map.py' and the issuer regenerates the served map after the fix.",
  "world_is": "d08's output cannot replace the served map as-is: it is on a different id grammar (canonical spine) than the z-ids the edge compares, and every relationship list differs by design. The served map is written by the legacy D_00 builder, which drops a no-account advisor in the same way. The issuer's regeneration must either run D_00 with the same union or apply the 5 empty entries to the served bytes under the never-widen pair; the producer I was granted does not change the served bytes by itself."
}
```

## ADVI_BILLING-D2-W4-S3 -- The shape differ in d_publisher_base has no empty-list tolerance (an empty id list reads as type 'empty' != census 'string'), so an advisor served wit

```json
{
  "id": "ADVI_BILLING-D2-W4-S3",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~4",
  "surfaced_at": "2026-10-09T08:40:00Z",
  "one_line": "The shape differ in d_publisher_base has no empty-list tolerance (an empty id list reads as type 'empty' != census 'string'), so an advisor served with empty lists is REFUSED by the shape check; d08 grades the populated advisors and asserts the empty shape itself",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "d_publisher_base.py _schema_of/_diff_schema: empty list -> {'__array__':'empty'} compared to census 'string' -> diff",
      "before the workaround: SHAPE CHECK REFUSED with diffs on /advisors/<key>/accounts and /relationships for the 5 keys",
      "after: d08 _shape_view leaves only the exact {accounts:[],relationships:[]} entries out of the census grade; SHAPE CHECK PASS diffs=0, TAMPER GUARD PASS 149 advisors"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "Wanted: the fix passes the census shape check without editing the base or the census (both outside the grant).",
  "world_is": "d08 asserts the empty entry's exact keys itself and withholds only those entries from the census grade. A durable fix is empty-list tolerance in the base differ (an empty list satisfies any element contract, as an empty map already does)."
}
```

## ADVI_BILLING-D2-W5-S1 -- The order says write to the builder's address, but the naming gate refuses the scope literal in a gateway file

```json
{
  "id": "ADVI_BILLING-D2-W5-S1",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~5",
  "surfaced_at": "2026-10-09T08:50Z",
  "one_line": "The order says write to the builder's address, but the naming gate REFUSES a hand-kept copy of the scope segment in any committed gateway file, so the module takes the destination ROOT from the environment (ADVI_FEE_STATEMENT_S3_ROOT) and the deploy must set it from address() output.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit.sh naming limb output 2026-10-09: NAMING REFUSE site_to_s3.py (and a generated fee_statement_location.json) -- a NEW hand-kept carrier of the firm scope key outside every permitted context: read it through lookup(); .tools/naming-gate.py judge() at line 1720",
      "app/gen_rivalfunds_location.py precedent does not transfer: its scope is not a carrier, and a generated file must be a lib/opal_naming.py generate target (naming-gate.py ~1851), which is outside this grant",
      "the gateway host carries no lib/ (app/gen_rivalfunds_location.py docstring), so the module cannot call address() at run time"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AB-e-3 item 1: the module writes to EXACTLY lib/opal_naming.py address(<smartx>,<scope>,'bronze','fee_statement','quarter=<q>','<name>.xlsx'); 'read how the gateway imports the builder (or vendors it) and follow that'.",
  "world_is": "The module holds no bucket or prefix literal. destination_root() reads ADVI_FEE_STATEMENT_S3_ROOT = the builder's address for the table without the partition, refuses (fail closed, before any Graph read) when it is unset or not shaped s3://<bucket>/<prefix>/bronze/fee_statement/, and appends only quarter=<q>/<sanitized name>.xlsx. The tests set the variable from address() and assert the written key equals the builder's full address. The issuer must set the variable at deploy from builder output (Terraform opal_name/address), the same step that adds the s3:PutObject grant; a configured value that is wrong is the one way the destination can differ from the builder, so the deploy proof should print the variable beside address()."
}
```

## ADVI_BILLING-D2-W3-S1 -- The commit-time naming gate refuses the column names the AB-e-5 order itself mandates (bd_account_id, bd_relationship_id) as string literals in the builder

```json
{
  "id": "ADVI_BILLING-D2-W3-S1",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~3",
  "surfaced_at": "2026-10-09T08:38Z",
  "one_line": "safe-commit's naming limb REFUSED household_crosswalk.py 5 times on the literals bd_account_id, bd_relationship_id and an internal bd_rel (hand-kept carrier of 'bd'), though AB-e-5 and r2_checks CROSSWALK_COLS require those exact column names; the builder now reads its column list from the contract JSON under org/, which the gate excludes.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "safe-commit output: NAMING REFUSE data/assets/scripts/gold/advi_billing/household_crosswalk.py:39, :110, :118, :129 -> lookup('49financial'); NAMING-GATE: REFUSE 5 graded",
      "data/assets/scripts/gold/advi_billing/household_crosswalk.py @d690b478cb: COLUMNS = list(CONTRACT['columns']); committed clean"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AB-e-5 item 1 names the output columns bd_account_id and bd_relationship_id; the order's bounds say addresses come from lib/opal_naming.py and legacy input URIs are passed as arguments.",
  "world_is": "The gate treats the token 'bd' inside a column-name literal as a hand-kept carrier of the firm. A later builder or reader that types these column names (AB-e-6 reads them) meets the same refusal and should take the names from the contract, as this builder does."
}
```

## ADVI_BILLING-D2-W3-S2 -- AB-e-6 says .scratch/ is gitignored in the worktree; it is not, and the dry-run object carries client figures

```json
{
  "id": "ADVI_BILLING-D2-W3-S2",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~3",
  "surfaced_at": "2026-10-09T08:56Z",
  "one_line": "AB-e-6 item 3 saves the dry-run object (client figures) to .scratch/advi_billing/AB_E6_DRYRUN.json 'in the worktree root (gitignored)', but git check-ignore on that path prints nothing and git status lists .scratch/ as untracked, so only the explicit-path commits keep it out of history.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "git check-ignore -v .scratch/advi_billing/AB_E6_DRYRUN.json -> no output (rc 1) in C:/dev/wk-advi-billing-3",
      "git status --short -> '?? .scratch/'; every commit by this worker named its paths, none staged .scratch/"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AB-e-6 item 3: the dry-run object is saved under .scratch/ (gitignored; it carries client figures and is never committed).",
  "world_is": "The path is untracked, not ignored. Nothing was committed from it. A later 'git add -A' or 'git add .scratch' in this worktree would stage client figures; the drain merges commits, not the working tree, so the merged branch is clean."
}
```

## ADVI_BILLING-D2-W3-S3 -- The platform rate's composition (UMA + APM + Model) and the value-weighting of rates over allocations are this worker's reading; no real SMArtX statement exists to test either

```json
{
  "id": "ADVI_BILLING-D2-W3-S3",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~3",
  "surfaced_at": "2026-10-09T08:57Z",
  "one_line": "AB-e-6 says each account's ADVISOR and PLATFORM rates come from the silver statement 'summed over the account's allocations'; rates are fractions that do not add across sleeves, so fee_quarter.smartx_by_account value-weights rates by Current Period Estimate Valuation and sums only the true-ups, and it defines the PLATFORM rate as UMA + APM + Model rate (Client Fee Rate unused) -- neither is tested against a real statement.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "INFERRED",
    "evidence": [
      "data/assets/scripts/gold/advi_billing/fee_quarter.py @9492f23e7d smartx_by_account(); org/standards/ADVI_BILLING_FEE_QUARTER_CONTRACT.json 0.2.0 scope_note says the composition is an assumption",
      "the dry run for the thread household found no silver partition (smartx_statement.used false), so the SMArtX path ran on synthetic fixtures only (test_fee_quarter_v2.py)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "AB-e-6 item 1: each account's ADVISOR and PLATFORM rates and the SmartX/Advisor true-up come from the silver partition, summed over the account's allocations.",
  "world_is": "When the first real statement lands, a PLATFORM component built from UMA + APM + Model may not equal Net SmartX Fee / (valuation x days / year) and would show as DIFFERS with a reason that blames the valuation or the true-up. Nothing serves a v2 object today (no --write ran), so this is INERT; before any write that serves a v2 object that used a statement, compare each allocation's Net SmartX Fee less its true-up with valuation x (UMA + APM + Model) x days / year on the real file and amend smartx_by_account if they differ."
}
```

## ADVI_BILLING-D2-S2 -- TO-AB-e-1 item 2 names opal_auth SECRET_ID as the human-token SIGNING secret, but that constant is the PUBLIC verification key and cannot sign

```json
{
  "id": "ADVI_BILLING-D2-S2",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~AB2",
  "surfaced_at": "2026-10-09T09:11:38Z",
  "one_line": "The order says mint with 'the shared human-token signing secret (infra/aws/lambda/shared/opal_auth/__init__.py SECRET_ID)'; that constant is SECRET_ID = 'opal/auth/jwt-public-key', the VERIFIER's secret, which cannot produce a signature. The five tokens were minted with 'opal/auth/jwt-private-key' (auth-handler jwt.ts:8), the only secret whose RS256 signature the edge's verifyWithSlots accepts.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/lambda/shared/opal_auth/__init__.py:33 SECRET_ID = 'opal/auth/jwt-public-key'; its only consumer is get_public_key() at :131-144 on the VALIDATE path",
      "infra/aws/opalinvest_dev/lambda/auth-handler/src/jwt.ts:8 JWT_PRIVATE_KEY_SECRET_ID = 'opal/auth/jwt-private-key'; generateAccessToken (:165-192) signs with getJwtPrivateKey()",
      "the five probes returned 200/403/200/403/403, so the minted signatures verified at the edge -- the private id is the one that works (AB_E1_PROBES.json)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-AB-e-1 item 2: mint the five tokens with the shared human-token signing secret, infra/aws/lambda/shared/opal_auth/__init__.py SECRET_ID.",
  "world_is": "That SECRET_ID is the public key id. Minting read opal/auth/jwt-private-key once (one GetSecretValue, 2026-10-09T09:00:50Z, actor 0.7.0_AE_CloudOps~AB2); no key byte was stored, logged or committed. Both ids are named in AB_E1_PROBES.json (signing_secret_id, verifier_secret_id) so the order's text and the act that satisfied it are both readable. A future order that cites SECRET_ID for a MINT is unexecutable as written."
}
```

## ADVI_BILLING-D2-S3 -- The other_firm probe was refused at the missing-identity-claims arm, which fires before any firm or bucket resolution -- the CROSS-FIRM arm is ABSENT, not EXERCISED-AGAINST

```json
{
  "id": "ADVI_BILLING-D2-S3",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.7.0_AE_CloudOps~AB2",
  "surfaced_at": "2026-10-09T09:11:38Z",
  "one_line": "other_firm (firmId mockadv, role user, firmRole user, and no advisorId, exactly as the order specifies the class) returned 403 'Advisor scoping: missing identity claims' -- index.mjs:478-492, failure mode 1, which runs BEFORE getOwnershipMap resolves a firm to a bucket. The status met the stated expectation (401 or 403) while exercising the identity-gap arm, not cross-firm containment.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "AB_E1_PROBES.json probes[3]: status 403, error_head {\"error\":\"Advisor scoping: missing identity claims\"}",
      "infra/aws/lambda-edge/auth-validator-edge/index.mjs:478-492 -- the !payload.advisorId || !payload.firmId branch returns forbidden() before the getOwnershipMap call at :490",
      "index.mjs:45-46 and :173-174: FIRM_BUCKET_MAP maps mockadv to opal-data-bd and the key is platinum/<firmId>/ownership_map.json, so a mockadv token WITH an advisorId would read platinum/mockadv/ownership_map.json -- a path this probe never reached"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-AB-e-1 item 2: other_firm = firmId mockadv, role user, firmRole user; expectation 401 or 403, read in the cell as the live edge refusing a caller from another firm.",
  "world_is": "The refusal is the identity-gap arm. Nothing in this round establishes what the edge does with a mockadv token that CARRIES an advisorId -- advisor_not_in_ownership_map (403), ownership_map_fetch_failed (503, if platinum/mockadv/ownership_map.json does not exist) and a map hit are all still open. Reaching it needs a sixth probe, which this order's refusal clause forbids, so it belongs to a later cell: one GET with firmId mockadv plus an advisorId, and a head-object on platinum/mockadv/ownership_map.json to predict which of the three arms should fire."
}
```

## ADVI_BILLING-D2-S4 -- FWD-3 NOT REALIZED on real data (flows and exclusions unexercised)

```json
{
  "id": "ADVI_BILLING-D2-S4",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T09:29:06Z",
  "one_line": "FWD-3 graded NOT REALIZED on the real render (E4): of its ACCEPT, the value charged on, the schedule (flat, so no tiers), days, per-account and household steps, and the 'why' are shown on real data; but 'any adjustment for money moved in or out during the quarter' and 'anything left out' are shown only on the invented-data render. For household z08219260 the panel neither shows a flow or exclusion nor states there was none, and the one flow-like mechanism -- SMArtX's prior-quarter true-up under advance billing -- is printed as 'method not known to this round'. ABSENT is not EXERCISED-AGAINST.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/r1_close/REAL_RUN_FWD1_R1.md @b44766f7ef",
      "C:/dev/advi_billing_private/r1_close/realrun_fee_panel.png (dell2, private; re-read by this seat, the fee panel section)",
      "org/missions/D8/ADVI/ADVI_BILLING/prd/ADVI_BILLING_PRD.md:45-50 (FWD-3)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BILLING_ROUND_2_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-3 ACCEPT: the value charged on, the schedule and tiers, any adjustment for money moved in or out during the quarter, and anything left out; they can answer 'why is my fee this number?'.",
  "world_is": "Four of the six clauses shown on real data; the flow-adjustment and left-out clauses unexercised on real data. FWD-3 realizes when one real household's panel shows a flow adjustment (or states 'no money moved in or out this quarter') and an exclusion (or 'nothing left out'), with the true-up read from a SMArtX statement (E2)."
}
```

## ADVI_BILLING-D2-W7-S1 -- copy_site_file_to_s3 is registered but UNCLASSIFIED: destructive_ops.py and data_entitlement.py are outside this order's grant

```json
{
  "id": "ADVI_BILLING-D2-W7-S1",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~7",
  "surfaced_at": "2026-10-09T10:05:00Z",
  "one_line": "The order registers copy_site_file_to_s3 in tools.py only; the gateway also classifies every tool in app/destructive_ops.py (TOOL_WRITE_CLASS, DESTRUCTIVE_OPS) and app/data_entitlement.py (NATIVE_TOOLS), both outside this grant, so the new write tool is fail-closed: a call returns confirm_required (blast_cap) and write_class UNCLASSIFIED denies every tier.",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/opal-gateway/app/destructive_ops.py classify()/write_class(): a tool in neither SAFE_TOOLS nor DESTRUCTIVE_OPS gets _UNKNOWN_TAG and write_class 'UNCLASSIFIED' (a class no tier is entitled to)",
      "measured in this worktree: tools.copy_site_file_to_s3 under a signed-in fake principal returned {'confirm_required': True, 'code': 'confirm_on_irreversible', 'message': 'copy_site_file_to_s3 is an UNCLASSIFIED write tool (fail-closed...)'} until blast_cap.evaluate was stubbed in test_bad_quarter_is_refused_with_refused_flag",
      "infra/aws/ec2/opal-gateway/app/data_entitlement.py NATIVE_TOOLS / TOOL_CLASSES lists the native tools the Gateway registered and has no entry for the new tool",
      "the precedent rows are upload_text_to_site and save_email_attachment_to_site in destructive_ops.py DESTRUCTIVE_OPS and TOOL_WRITE_CLASS ('write_files')"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-AB-r-3 item 1: register copy_site_file_to_s3 in app/tools.py, kept out of any read-only/safe tool set; the post-deploy proof is one refused call on a bad quarter.",
  "world_is": "Registration alone yields a tool that is listed and not safe, which the criterion measures, but not one that reaches the module: the unclassified-write gate answers first. The release needs, in a cell whose grant names app/destructive_ops.py and app/data_entitlement.py: a DESTRUCTIVE_OPS entry (WRITE_REVERSIBLE, never-overwrite conditional put, native_undo = delete the key) plus TOOL_WRITE_CLASS['copy_site_file_to_s3'] = 'write_files', and the name added to data_entitlement.NATIVE_TOOLS. RELEASE_PACKET_E2.md names these as a required carry. NOT done here (outside the grant)."
}
```

## ADVI_BILLING-D2-W7-S2 -- The gateway env is rendered by a printf in deploy-to-ec2.sh, not a file under deploy/

```json
{
  "id": "ADVI_BILLING-D2-W7-S2",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~7",
  "surfaced_at": "2026-10-09T10:05:00Z",
  "one_line": "The gateway reads env from /opt/opal-gateway/.env (opal-gateway.service EnvironmentFile=), and that file is generated by one printf in infra/aws/ec2/opal-gateway/deploy-to-ec2.sh (outside this grant; deploy/ holds only the unit file), so the env line is a packet diff for the owners.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/ec2/opal-gateway/deploy/opal-gateway.service line 10: EnvironmentFile=/opt/opal-gateway/.env",
      "infra/aws/ec2/opal-gateway/deploy-to-ec2.sh line 417: one printf piped to tee ${REMOTE_DIR}/.env writes every key (ENABLED_INTEGRATIONS, FIRM_ROLE_ARNS, ...) and rewrites the whole file each deploy",
      "a hand-added line on the host would be erased by the next deploy"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-AB-r-3 item 3: name the exact place the gateway reads env (a systemd unit or env file under deploy/) and do not edit the deployed config unless it lives in the repo and only the new line changes.",
  "world_is": "The place the gateway READS env is /opt/opal-gateway/.env (unit line 10); the place it is WRITTEN is deploy-to-ec2.sh line 417, a repo file outside the grant. Nothing under deploy/ carries it, so nothing was edited; the packet carries the one-key diff (a new ADVI_FEE_STATEMENT_S3_ROOT pair and its argument) for the owners."
}
```

## ADVI_BILLING-D2-W7-S3 -- The full opal-gateway root cannot be planned from this device; the saved plan is the -target plan of the one new resource

```json
{
  "id": "ADVI_BILLING-D2-W7-S3",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~7",
  "surfaced_at": "2026-10-09T10:05:00Z",
  "one_line": "terraform init needs a direct provider install (the device CLI config mirrors only aws) and a full plan of infra/aws/terraform/opal-gateway fails at refresh with 6 errors (AccessDenied reads, a missing secret, an external build that wants a deployed commit absent here), so AB_R3_PLAN.txt is the plan with -target=aws_iam_role_policy.advi_billing_gateway_put and drift elsewhere in the root is UNMEASURED.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "device terraform CLI config: provider_installation filesystem_mirror of the kit pack with direct excluded; hashicorp/external and hashicorp/archive are absent from the mirror, so init failed until TF_CLI_CONFIG_FILE=.scratch/tf_direct.rc (direct {}) was set; the repo lock file hashes verified the installs",
      "full plan (-lock=false) errors: ELBv2 DescribeLoadBalancer and DescribeTargetGroups, Glue GetDatabase and Athena GetWorkGroup AccessDenied for the dell2 agent user; Secrets Manager gateway/mail/commassist-bearer not found; data.external.mcportal_grant_writer_stage: build_package.py REFUSED, the deployed_commit does not resolve in this worktree",
      "targeted plan: Plan: 1 to add, 0 to change, 0 to destroy, with only aws_iam_role_policy.advi_billing_gateway_put"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-AB-r-3 item 2: terraform init + plan of infra/aws/terraform/opal-gateway/, text saved; the plan may touch only advi_billing resources; other drift is recorded and the criterion stops with a row.",
  "world_is": "The drift question for the rest of the root is not answerable here: the plan that ran touches only the advi_billing resource and destroys nothing, but it is a target plan, not a whole-root plan. The owners' apply step plans the whole root with their own credentials and the deployed commit; the packet asks them to confirm the whole-root plan adds exactly this one resource before apply. No apply, no state write (-lock=false)."
}
```

## ADVI_BILLING-D2-W7-S4 -- HCL cannot call lib/opal_naming.py address(); the grant joins the registry tier home and the scope, and a test pins the join to address()

```json
{
  "id": "ADVI_BILLING-D2-W7-S4",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "0.9.0_WK_ADVI_BILLING~7",
  "surfaced_at": "2026-10-09T10:05:00Z",
  "one_line": "The opal_name module has no tier-home or key output, so advi_billing_gateway_iam.tf reads infra/logic/registry/tiers.json homes.FIRM.bronze.bucket with file()+jsondecode() (as opal_name reads exemptions.json) and takes the scope from the module's scope_long; test_tf_prefix_equals_builder_address asserts the join equals address().",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "infra/aws/terraform/modules/opal_name/main.tf outputs: name, scope_short, scope_long, scope_class, scope_bucket, fence_patterns, account_id; scope_bucket['49financial'] is the firm's own bucket, not the bronze home",
      "lib/opal_naming.py address(): bucket = _home_bucket(reg, scope, tier, source), read from tiers.json (FIRM bronze -> the shared bucket)",
      "neighbour taxsma_gateway_iam.tf carries a literal bucket local; mcpmsp_*.tf use scope_bucket (right for platinum, wrong for bronze)"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "TO-AB-r-3 item 2: the ARN built from lib/opal_naming.py output the way the root already does; if the root cannot call the builder, say how the neighbouring files carry addresses and follow that.",
  "world_is": "No neighbour reads the tier-home rule; the one pattern for registry-file-as-plan-time-data is opal_name's own file() of exemptions.json, which this follows. The source (smartx) and table (fee_statement) segments are typed in the .tf; a registry change to the FIRM bronze home changes the plan, and the test fails if the join ever diverges from address()."
}
```

## ADVI_BILLING-D2-S5 -- FWD-3 REALIZED on the round-3 real render

```json
{
  "id": "ADVI_BILLING-D2-S5",
  "project": "ADVI_BILLING",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-09T10:15:45Z",
  "one_line": "FWD-3 graded REALIZED on the round-3 real render (portal DEV 6d383958, household z08219260; private PNG on dell2, sha256 8e941d5e... matches the record, viewed by this seat): both accounts now state 'No money moved in or out this quarter' and 'Nothing excluded', backed by the served object's flows_in_period [] and excluded_value 0, beside the value charged on, the flat schedule, days, both components with reasons and the 10 steps. Every FWD-3 ACCEPT clause is shown on real data. Correction to this seat's round-2 remedy (D2-S4): it also asked for the prior-quarter true-up from a SMArtX statement; that true-up sits in Schwab's DEBIT, so it is a reason for the debit difference (FWD-1's comparison, E2), not part of how Opal works out the fee (FWD-3).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "grounding": {
    "status": "GROUNDED",
    "evidence": [
      "org/missions/D8/ADVI/ADVI_BILLING/deliverables/2.0.0_SA_COO~B2/r3_close/DRAIN_END_R3.md @a62249088d",
      "C:/dev/advi_billing_private/r3_close/r3_realrun_fee_panel.png (dell2, private; this seat's sha256 prefix 8e941d5ea9344a60)",
      "org/missions/D8/ADVI/ADVI_BILLING/prd/ADVI_BILLING_PRD.md:45-50 (FWD-3)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_BILLING_ROUND_3_L9_GRADE_20261009.md"
    ]
  },
  "disposition": "UNDER_INVESTIGATION",
  "spec_asserts": "FWD-3 ACCEPT: the value charged on, the schedule and tiers, any adjustment for money moved in or out during the quarter, and anything left out; they can answer 'why is my fee this number?'.",
  "world_is": "REALIZED on real data. The true-up's method remains unknown and is carried by E2 for FWD-1's difference reason."
}
```
