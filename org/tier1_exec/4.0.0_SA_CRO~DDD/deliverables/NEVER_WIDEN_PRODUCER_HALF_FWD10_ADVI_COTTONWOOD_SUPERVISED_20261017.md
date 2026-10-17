# Never-widen PRODUCER half, 4.0.0_SA_CRO~DDD -- FWD-10 on ADVI: Cottonwood supervised switch in C_03

**Author:** 4.0.0_SA_CRO~DDD, 2026-10-17 ~02:3xZ. **For:** 1.0.0_SA_CTO~DELL1 (CTO half). **Authority:** Andrew-direct
`ANDREW_DIRECT_20261017_015xZ_COTTONWOOD_530M_MDPF_AND_ADVI_CRO_EXECUTES.md` @aca8db2e43 ("it has to be done for ADVI Advisor
Intelligence page too"). **Code:** @9a3a0e5605.

## The act

`safe-deploy --tree cot` two files to `s3://opal-data-cot/code/gold/`. The cot-exporter box syncs that prefix at every gold run
(`infra/aws/terraform/cot-pipeline/ssm.tf:350`).
- `C_03.account_performance.py`. The prior VersionId `TK2zSqSpzPTYacdKpWI94MjxPPsctOhS` is byte-equal to git before this
  change (CRLF-normalised diff empty), so only the switch moves.
- `lib/supervised_scope.py`, a new key. It is inert unless imported.

## The writer of the property moved -- N = 1

The property is `gold/timeseries/account_performance.parquet` (opal-data-cot). Its only writer is C_03 in the SSM chain
`opal-cot-gold-run` (`ssm.tf:304-410`), which runs after bronze (07:30 ET) and silver. Every Cottonwood AUA total on the
ADVI page derives from it:
- `D_00` -> header_metrics, clients_tab, dashboard, clients-tab-slim, client_directory, leaderboard;
- `D_00b` -> timeseries_overview and cumulative_chart;
- `D_01`/`D_04` -> partner_analytics and the advisor and client summaries.

## Both branches

- **(a) The flag is present.** The latest partition carries `account_supervised`. The 98 older partitions (04-22..08-19)
  use today's flag per account. Dry run of C_03's snapshot loader (no write):
  - 10/15: total_aua 554,580,722.69 over 1,004 accounts -> **521,509,653.07 over 864**;
  - 10/14: 520,505,622.94;
  - 8/19: 449,733,561.36, equal to MDPF's supervised 8/19.
  - Account and client counts fall to supervised accounts only. NNA follows, since flows merge onto the kept accounts.
- **(b) No partition carries the flag.** `supervised_scope.today_flags` raises SystemExit, C_03 writes nothing, and the
  served artifacts stay at the prior run's whole-book values. The run reads red.

## Not covered (declared)

- **Mix leaves.** `mix_summary` / composition (D_03) is lane `MDPF_SECCLASS_FAST_M_BD_MIX`, live with 2.0.0_SA_COO~M1. I
  did not edit it. The same three-line `supervised_scope.filter_supervised` call goes there on that lane's word.
- **C_06 mix trend.** It is incremental, so history stays whole-book until a full rebuild.
- **The ~$8.86M carrier-feed accounts.** They are $0 at the 07:30 pull and need the same-day re-pull (findings
  ADDENDUM 2). Until then the page reads ~521.5M, not 530.42M.

## Collisions

- **R106.** No silver write; C_03 writes gold only.
- **MDPF.** Independent bucket and code path. The MDPF half is closed (ledger
  `mdpf-gold-fwd10-cottonwood-supervised-20261017`).

## Rollback per key

- Re-upload C_03 VersionId `TK2zSqSpzPTYacdKpWI94MjxPPsctOhS` as current. Alternatively, upload `lib/supervised_scope.py`
  with `SUPERVISED_ONLY = False`.
- The next gold run rewrites `account_performance.parquet` and its platinum descendants whole-book.

## Producer half: SIGNED by 4.0.0_SA_CRO~DDD for the act and bytes above (@9a3a0e5605). Awaiting the CTO half.
