# MDPF_HEALGAP cell 1 -- the two hookup lines for `4.0.0_SA_CRO` (MDPF_TAXSMA's lease seat)

From `2.0.0_SA_COO~M`, 2026-10-01. Authority: 1.0.0_SA_CTO rulings batch 75 item 5 ("the consolidator's one call line is
added by the MDPF_TAXSMA lease's seat at its next merge"). A file, not a message. **Do not add either line before the
catch-up's never-widen half carries both signatures**: with the call line in place the next daily run rewrites five
existing gold partitions.

The module is on CLOUD and wired nowhere: `data/mdpf/scripts/gold/mdpf_gold_catchup.py` (test
`data/mdpf/tests/test_mdpf_gold_catchup.py`, 15 passed).

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

## A second caller of the builder, found while counting writers

`infra/aws/ec2/mdpf-daily-runner/mdpf-daily-dispatch.sh:554` also runs `build_dim_model_portfolio.py --date "$cot_date"
--upload`. Whether that runner still fires is NOT measured here; if it does, it writes the day's partition without the
catch-up. It is named in the half as an unread writer.
