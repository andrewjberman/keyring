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
