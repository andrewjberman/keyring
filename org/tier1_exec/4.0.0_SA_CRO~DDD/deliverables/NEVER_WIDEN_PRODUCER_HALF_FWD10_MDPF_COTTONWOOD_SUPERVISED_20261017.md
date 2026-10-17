# Never-widen PRODUCER half, 4.0.0_SA_CRO~DDD -- FWD-10 (a): Cottonwood supervised switch on mdpf-gold-lambda

**Author:** 4.0.0_SA_CRO~DDD, 2026-10-17 ~02:2xZ. **For:** 1.0.0_SA_CTO~DELL1 (CTO half), on MDPF_CANON PRD v2.26
@72ef0a649f. **Authority:** Andrew-direct `ANDREW_DIRECT_20261017_015xZ_COTTONWOOD_530M_MDPF_AND_ADVI_CRO_EXECUTES.md`
@aca8db2e43. **Scope:** the MDPF half only. The ADVI half and the insurance-feed ingest (FWD-10 (b)) carry their own.

## The act

1. Upload the package built from pin **f09a6a3adb** to `s3://opal-data-assets/portal/gold/mdpf/_code/mdpf-gold-lambda.zip`.
   The pin is the deployed pin 66ae82d62d plus cherry-pick of 314315a0f9, scratch branch `cro-ddd-fwd10-pkg`. Package sha256
   `9a1073b0aa534ee2afe534a98b6dace3451584f332d54fc15cbc6e1bda443f07`, 1,988,562 B.
2. `safe-apply` mdpf-pipeline with `MDPF_GOLD_COMMIT` = f09a6a3adb (`gold-lambda.tf:381`). Expected plan: 0/1/0, code plus that
   env var only.
3. `safe-deploy` the same file to the EC2 runner copy `s3://opal-data-mdpf/code/scripts/assets_gold/build_cottonwood_mdpf_slice.py`,
   so both writers carry the switch.

**The bytes:** the new zip differs from the live zip (VersionId `uEugT_GkA5lu8esTJqvA1Ubq10QN2vZM`) in exactly two of 46
members, `build_cottonwood_mdpf_slice.py` and `BUILD_MANIFEST.json`. Measured file by file, sha256. `git diff 66ae82d62d f09a6a3adb`
= that one file, 69+/8-.

## The writers of the property moved -- N = 2, both rules read

The property is the Cottonwood total leg (`partner_custody_total` in `gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json`)
and everything derived from it: the Cottonwood Client node, the category-views total, aum_metrics, and the Global fold.
1. **mdpf-gold-lambda** (`mdpf-scheduled-floor`, 13:30Z). With the switch it sums `Market Value` over accounts flagged
   `Account Supervised == "Supervised"`. Partitions without the column (2026-06-09..08-19, 55 of 95) use today's flag per
   account.
2. **EC2 stage 6d** (`mdpf-daily-dispatch.sh:547-556`, ~12:5xZ). It runs the same file from the runner copy. Act 3 gives it
   the same bytes. If 6d still fails upstream at 6a (the 10-03 record), it writes nothing. If it runs, the Lambda rewrites
   the same keys 35 minutes later with identical logic.

## Both branches

- **(a) The flag is present (every partition since 2026-08-20; today's map covers the older ones).** Dry run at
  314315a0f9 (no write), all gates PASS:
  - 10/15: total 554,632,228.45 -> **521,561,158.83**; excluded unsupervised 33,071,069.62; unflagged 0.00.
  - 8/19: excluded 30,322,927.42 (the 2026-08-25 figure).
  - Models (205,049,392.06) and SMA (8,224,501.41) do not move: 0 of 130 unsupervised accounts carries a model.
  - Cottonwood Client: 341,358,334.98 -> 308,287,265.36.
- **(b) No partition carries the flag.** The slice raises `SystemExit` before any write. Served bytes stay at the prior
  run's output, and the run reads red.

## Joint expected Global for the 2026-10-17 13:30Z fire (collision 1, for 2.0.0_SA_COO~D1)

`Global(fire) = 2,237.50M (CN-s-1 V2 prediction) - U_cot(d*)`
- d* is the Global headline's date. U_cot(d*) is the `meta.total_scope.latest.excluded_unsupervised` the new slice prints
  for d*.
- On 10/15 data U = 33,071,069.62, so Global = **~2,204.43M**. If d* = 10/16, U(10/16) is read from the fire. The prior two
  days were 33.07M and 33.16M.
- Only the Cottonwood leg moves. 49financial and Inflection are untouched.

## Collision 2 (R106, for 2.0.0_SA_COO~C1)

This act writes **no Cottonwood silver**. It reads `blackdiamond/cottonwood/silver/fact_holdings` and writes gold and
platinum only. The ingest widen (FWD-10 (b)) is the act that writes silver, and it waits for C1's written agreement after the
R106 read.

## Blast radius and rollback per key

- **Keys that move at the next gold+publisher run:** Cottonwood `aggregate_aua_timeseries.json`, `category-views.json`,
  aum_metrics, and Global's aggregate and category views. The platinum mirrors follow the publisher.
- **Rollback:** re-upload the prior zip VersionId `uEugT_GkA5lu8esTJqvA1Ubq10QN2vZM` as the head version, `safe-apply` with
  `MDPF_GOLD_COMMIT` = 66ae82d62d, restore the runner copy to VersionId `Ua5Br0jiXdTNyRlZG2PgUBMUkvFElgDS`, then one gold run
  and one publisher run.

## Producer half: SIGNED by 4.0.0_SA_CRO~DDD for the act and bytes above. Awaiting the CTO half.

## ADDENDUM B (2026-10-17 ~04:3xZ) -- the pair half of the switch: the AUM BY MODEL donut

**Why.** Andrew-direct, on a page screenshot (~04:2xZ): "its good but radial needs to be correct as well". After the 10/15
restatement the headline reads 530.42M, but the AUM BY MODEL donut reads $564M. That is aum-metrics `total.aum`, the pair's
`firm_total`, which summed the whole book: 563,559,897.67.

**The act.**
1. Package pin **d2f734fbac**: the live pin f09a6a3adb plus @ee1caa9f31 `_supervised_values` in
   `build_cottonwood_mdpf_pair.py`, one file, +24. Zip sha256 `7c05d9e2074b3eca597a9c6647d27c97705f2513a4a6960ec9fdea0b6740778d`.
   Upload it with metadata content-sha256 and `safe-apply` mdpf-pipeline with MDPF_GOLD_COMMIT = d2f734fbac.
   `safe-deploy` the runner copy of the pair file.
2. The dated Cottonwood 10/15 aum-metrics key (and account-distribution, if the QA run shows it business-different) will
   A8-conflict. Its restatement is a delete marker the laptop CloudOps lane places (dell1 is denied), then one gold run and
   one publish.

**Dry run (no write), assignment 2026-10-16 x value 2026-10-15.**
- firm aum 563,559,897.67 -> **530,421,988.14** (864 of 1,004 accounts; excluded 33,137,909.52).
- model 268,523,373.04, unchanged. non_model 261,898,615.10.
- Identities (i)-(iii) PASS; bridge 391/391.
- The CLIENT HOLDINGS distribution covers model accounts only (378 funded) and does not move.

**Branches.** (a) The flag is present: as above. (b) The flag is absent: `_supervised_values` raises SystemExit, the pair
scope fails isolated, and the served bytes stay.

**Rollback.** The package goes back to VersionId Fug5LxhL9UE3.vbgRA6vHnriMrbFJqJW with MDPF_GOLD_COMMIT f09a6a3adb. The
laptop-placed marker on aum-metrics 10/15 is removed by its VersionId.
