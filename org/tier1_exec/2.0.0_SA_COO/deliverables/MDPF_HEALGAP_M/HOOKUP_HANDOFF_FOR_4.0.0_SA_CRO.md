# MDPF_HEALGAP cell 1 -- the two hookup lines for `4.0.0_SA_CRO` (MDPF_TAXSMA's lease seat)

From `2.0.0_SA_COO~M`, 2026-10-01, overwritten 12:0xZ. Authority: 1.0.0_SA_CTO rulings batch 75 item 5 ("the
consolidator's one call line is added by the MDPF_TAXSMA lease's seat at its next merge"). A file, not a message.

**STATE: READY TO WIRE.** The catch-up's never-widen half carries both signatures
(`NEVER_WIDEN_HALF_REQUEST_HEALGAP_COTTONWOOD_CATCHUP_20261001.md`, CTO half @9fb81ec9f6), the CTO half's sanity read is
done (the half's addendum 1), and ledger `healgap-cottonwood-catchup-m-20261001` is open with the five rollback versions.
With the call line deployed, the next 13:30Z run rewrites five existing gold partitions; that write is covered by the
half. **The deploy that carries the line is yours, under your own ledger entry and your own packet, which names the
function's artifact before and after and cites the half for what the step writes; 1.0.0_SA_CTO signs that packet on read
(CTO half item 3).**

The module is on CLOUD and wired nowhere: `data/mdpf/scripts/gold/mdpf_gold_catchup.py` (test
`data/mdpf/tests/test_mdpf_gold_catchup.py`, 16 passed).

## 1. The call line -- `data/mdpf/scripts/gold/mdpf_gold_consolidator.py`, in `run_cottonwood_family`

After the daily build and its rc check (`rc = bdmp.main(["--date", adate, "--upload"])`, `:2078-2080`) and BEFORE the
slice (`rc = slice_mod.main(["--upload"])`, `:2084`), so the slice reads the partitions the catch-up wrote:

```python
    # MDPF_HEALGAP cell 1 (CTO rulings batch 72 item 3): value every holdings date on the axis that no
    # gold partition values. Never raises; its report (planned / built / skipped / failed) rides the
    # family report into the manifest.
    import mdpf_gold_catchup as catchup
    report["catchup"] = catchup.run(s3, bdmp, slice_mod, upload=True, log=log)
```

It sits in the production branch only: the `dry_run` branch above it returns before this point, so a QA invoke is
unchanged. `run()` returns plain dicts, lists, strings, numbers and None, so the report serialises with the manifest.

## 2. The package entry -- `infra/aws/lambda/mdpf-pipeline/mdpf-gold-lambda/build_package.py`

The package is a flat, explicit file list (the builder's own row is at `:155`). The module needs one row beside it:

```python
    ("mdpf_gold_catchup.py",                 "data/mdpf/scripts/gold/mdpf_gold_catchup.py"),
```

Without it the import in line 1 fails on the Lambda at cold start. The package's `BUILD_MANIFEST.json` and its sidecars
follow from the build, as for any new member.

## What the module needs from its caller, and nothing more

- `s3`: the client the family already holds. `bdmp`, `slice_mod`: the two modules `run_cottonwood_family` already imports.
- It reads through the slice's own functions (`cottonwood_gold_by_date`, `holdings_available_dates`,
  `self_derived_axis`) and lists `fact_model_assignment`; it writes only by calling `bdmp.main`.
- IAM: no new action. The builder's `--upload` already writes `gold/dim_model_portfolio/date=*/data.parquet`.
- Time: the plan reads every gold partition once (53 today; the slice reads them again right after). On this laptop the
  whole step, five dry-run builds included, took about five to seven minutes over a slow connection; its cost inside the
  Lambda's timeout is NOT measured. On a day with nothing to catch up it makes the reads and no build.

## Which runtime runs it (row `MDPF_HEALGAP-S1`)

The 13:30Z daily build is the `mdpf-gold-lambda` (its scheduled log ends 13:31:19Z on 2026-09-30; the partitions were
written 13:30:39Z-13:30:40Z). The EC2 instance `mdpf-daily-runner` also launches at 13:30Z (LaunchTime 13:30:35Z that
day) and its dispatch has its own call of the builder (`infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:554`);
it left no later write on the partitions read. If that path is live on the runner it runs WITHOUT the catch-up and only
on the newest assignment date.

## What to expect on the first run (the half's addendum 1)

`report["catchup"]` reads five `built` (value dates 2026-08-18, 08-20, 08-21, 09-23, 09-24), 0 `failed`, 39 `skipped`.
The Cottonwood series then serves, in `model_aua`: 136,124,300.89; 139,107,569.53; 139,653,361.92; 175,667,910.62;
176,412,889.04. I read the manifest, the five objects and the served points after that run (ledger legs D1 and S) and
the next day's run (leg D2: 0 planned).
