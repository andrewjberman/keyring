# Holdings as a scheduled daily producer -- the plan (CTO R4)

`2.0.0_SA_COO~M`, 2026-09-25 ~16:0xZ. Owner by ruling: `org/tier1_exec/1.0.0_SA_CTO/deliverables/RULINGS_IRPT_20260925.md`
@75156f2b18 R4 (msg 100947). This plan replaces the four steps of `HOLDINGS_SCHEDULED_PRODUCER_ROUTING_REQUEST_20260925.md`
with what the code and the live estate actually require. Each line below is measured, with its source; nothing is
built yet except step 1.

## What a scheduled run IS

`holdings_snapshot.py --firms <firm> --upload` is a full publication, not a file drop:
- `run_firm` (`:2522-2576`) builds, validates, reconciles and runs the holdout difference control;
- `land` (`:2480-2520`) publishes through `HoldingsPublication`: it captures the index, writes immutable
  gold/platinum objects, and advances the accepted row by compare-and-set.

So every fire moves served holdings at 3 firms. That is step 4's never-widen half, and it covers both branches: a
publish, or a REFUSED build that leaves the prior revision served.

## Prerequisites, measured

| # | Prerequisite | State today | Owner |
|---|---|---|---|
| 1 | The producer code on CLOUD (classification members, the 49F master names, the INF Orion names) | DONE: CLOUD @f606108549, 6c54a74490, d02defe228; suite 270 passed | ~M |
| 2 | A dispatch target that runs the script | The resident runner REJECTS a holdings message (~P msg 100955: `resident_worker.py:262-270` routes resolve_upload only; each fire would be a poison message ending in the DLQ). The schedule `irpt-holdings-snapshot` stays DISABLED | ~M (retarget) |
| 3 | A package carrying the runner's closure | The served `investor_reporting` bundle has 10 of the 12 files the runner opens at import (re-arm test: IF-ENABLED-NOW FAIL). One bundle of 17 members needs 2,440 bytes of S3 user metadata against the 2,048 cap, so the mint would refuse. The runtime also opens `docs/contracts/investor-reporting/v1/CurrencyAuthorities.json` (`currency_authority.py:21-25`), which no bundle carries | ~M |
| 4 | Host IAM | `mdpf-pipeline/iam.tf:567+` grants the directory chain's 11 prefixes "and NOTHING wider". Holdings reads Schwab/SmartX (opal-data-assets), Orion/Eclipse (opal-data-inf) and COT sources, scans DynamoDB `bd-securities` for the classification, and writes 3 firms' holdings publication prefixes | infra lane (AE/DT), under the cross-firm guard |
| 5 | Retained inputs | 49F needs `IRPT_49F_TAX_MEMBERSHIP_SNAPSHOT` and INF needs `IRPT_INF_ECLIPSE_MEMBERSHIP_SNAPSHOT`. Both are LOCAL files today (`.runtime/cro-m-taxsma-20260923/...`, `.runtime/codex-seats/4.0.0_SA_CRO/eclipse_membership/...`), and the builds REFUSE without them. A host cannot read a laptop file | the captures' producers (Tax SMA workbook; Eclipse membership) |
| 6 | Currency attestation for a 49F/INF upload | ATTESTED at HEAD for all 3 firms (`bind_report_currency`, read 2026-09-25); needs only the JSON aboard (row 3) | -- |
| 7 | The enable | never-widen half to 1.0.0_SA_CTO | ~M asks, the CTO signs |

## Recommended shape

- **Dispatch:** the directory refresh's own mechanism, which is live and proven. An SSM `send-command` to the
  mdpf-daily-runner, triggered by a schedule and not by upstream success (the scheduling law). It fires after the
  directory refresh (09:30 America/New_York) inside the host's up window (12:52Z-16:41Z): for example 10:15 ET,
  MON-FRI. The candidate is a sibling function beside `irpt-directory-refresh`, reusing its `SsmBuildDispatcher`
  rather than a second copy.
- **Package:** a separate holdings bundle, whose metadata sits under the cap (12 or 13 members). Its S3 address is
  `lib/opal_naming.py address()` output (rule 30), or it is a registry row to add. The existing bundle keeps its 10
  members, so the directory runner's bytes do not move.
- **Retained inputs:** each capture lands in S3 under its producer, and the build reads the latest object at or
  before its cutoff. Until then a scheduled fire REFUSES 49F and INF by the builders' own rule, and publishes COT
  only.

## Order

1. Rows 3 and 5 first. They are the only ones whose absence makes a fire fail rather than wait.
2. Row 4 (IAM) under a ledger entry and `safe-apply`.
3. Row 2: the dispatch function and its schedule, created DISABLED.
4. One ad-hoc QA fire with `--qa` (the QA prefix), read back.
5. The never-widen half, then the enable.

## Not decided here

- The Tax SMA and Eclipse capture cadences, and their owners' willingness to land them in S3.
- Whether the infra lane takes row 4 as one change with row 2.

Both are asks, made one at a time.

## ADDENDUM 2026-09-25 ~17:5xZ -- rows 2 and 4, concrete (measured against the directory chain)

Progress since the plan:
- Row 5 is DONE: retained inputs landed (1c4ca93511) and read latest-at-or-before D (61f4b25171).
- Row 3's tooling is DONE: manifest stamps (7d3e4255a8) and STANDALONE_BUNDLES irpt_holdings_{49f,inf,cot} with 40
  members each, per-firm code homes from address() (ec48c5d144). The mint from CLOUD is still owed.
- S134 is remedied: a full-firm COT build screens each account (ce64116275).

**Row 2, the dispatch.** Mirror the directory refresh (`infra/aws/lambda/investor-reporting/directory/refresh.py`):
- a scheduled function sends ONE SSM command per firm to the mdpf-daily-runner;
- the host shell is thin: fetch that firm's own package, `sha256sum -c SHA256SUMS`, an import check, then
  `python3 holdings_snapshot.py --firms <firm> --upload`, with no `--as-of`, so the runner's own trading-day walk picks
  the date;
- it runs inside the host window (12:52Z-16:41Z), after the directory's 09:30 ET fire;
- it needs NONE of the directory's previous-state accounting, because the holdings publication is its own
  compare-and-set index. A refused build leaves the prior revision served. The function records each fire's command
  ids, and the next fire reads their outcome, so a failure is visible and not silent.

**Row 4, the principals (R-44).** The directory chain splits its calls BY BUCKET:
- shared buckets on the host session;
- a firm's own bucket through that firm's assumed source principal (`IRPT_DIRECTORY_SOURCE_ROLE_MAP` ->
  `IRPT_SOURCE_READ_ROLE_ARN`; `directory_runner.Firm49F._gold`), because the firm bucket's policy admits only a
  principal carrying the firm's scope.

The holdings runner:
- READS shared or legacy buckets (opal-data-assets Schwab/SmartX/COT silver/retained captures; opal-data-inf Orion and
  Eclipse; DynamoDB bd-securities);
- WRITES each publication into the firm's OWN bucket (opal-data-{49financial,inflection,cottonwood}, index, manifest,
  parts, gold);
- has no principal split today, and every served revision so far was written by an operator's user credentials.

So row 4 is:
- (a) the producer: the publisher's client assumes a firm-scoped principal named by the dispatch (~M, producer code),
  while reads stay on the host session;
- (b) that principal's grants: write the firm's `irpt/<firm>/{gold,platinum}/holdings*` prefixes and read its code
  home, plus the host's reads of the source prefixes above (infra lane, a ledger and safe-apply, under the cross-firm
  guard).

## ADDENDUM 2 2026-09-25 ~18:3xZ -- row 4b, measured: ONE principal per firm, holding that firm's reads and writes

- **The fence** (`directory/principal_49f.tf:1-34`): each firm bucket's policy (shared-infra/s3-<firm>.tf,
  DenyForeignFirmPrincipals) denies every principal whose name lacks the firm's scope slot. The host role
  (`mdpf-daily-runner-ec2-role`) lacks it, and widening it is the cross-firm act CLAUDE.md forbids. So the host cannot
  even fetch a package from a firm's code home. Creating a firm principal is a NEVER-WIDEN-CLASS act (R-44
  condition 2): declared first, applied only after both halves (1.0.0_SA_CTO and a COO) are signed.
- **The design:** one `irpt-<short>-holdings-role` per firm, name from module.opal_name, carrying the scope slot the
  fence admits, trusted only by the host role.
  - The host script assumes it FIRST and runs the fetch and the whole build under it: aws sts assume-role, then
    exported credentials.
  - The host role gains nothing.
  - (The producer's publish_client, 3e1ca981ab, stays for operator runs.)
- **Grants = the build's own receipts**, measured in a real build_snapshot per firm (VersionedInputs, cutoff
  2026-09-24):
  - COT: opal-data-assets/blackdiamond/cottonwood/silver/{fact_allocations,fact_holdings,fact_model_assignment,
    fact_model_blend,fact_model_definition,fact_model_roster}/; opal-data-cot/investor-reporting/directory/.
  - 49F: opal-data-assets/schwab/08335338/silver/{dim_asset,dim_balance,dim_position}/;
    opal-data-assets/smartx/platform/silver/{fact_allocation_account_map,fact_allocation_positions,
    fact_allocation_valuation,fact_model_allocation_roster}/;
    opal-data-assets/gateway/49financial/bronze/taxsma_workbook_projection/; opal-data-bd/investor-reporting/directory/.
  - INF: opal-data-inf/silver/api_dims/{accounts_v2,positions_mv}/; opal-data-inf/silver/eclipse/;
    opal-data-assets/eclipse/inflection/bronze/eclipse_membership_map/; opal-data-inf/investor-reporting/directory/.
  - Every firm, beyond the receipts:
    - s3:ListBucket conditioned on exactly those prefixes (the partition walks);
    - dynamodb:Scan on bd-securities (the classifier);
    - GetObject on its own code-home key;
    - Get/Put on its own irpt/<firm>/{gold,platinum}/holdings prefixes in opal-data-<firm>.
  - COT's mdpf slice and pair modules may read beyond the receipts. They are re-measured with a boto3 call hook
    before the declaration is frozen.
