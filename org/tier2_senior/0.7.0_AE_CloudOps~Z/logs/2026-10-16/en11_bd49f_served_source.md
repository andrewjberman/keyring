# OG-en-11 -- which bucket does the 49F Black Diamond adapter read on the live host (0.7.0_AE_CloudOps~Z, 2026-10-16)

- Order msg 35015, commit 565a85e5cb. Read-only; SSM one command per run; nothing written to any bucket or table.
- Run 1 (deployed commit 38fe44d5cb) forgot the from_date/to_date window transactions and fees require (absent_reason window_required); run 2 (deployed commit d14445961d) supplied it. The order said run once; the second run is disclosed in the record's run_note.
- Result: holdings, transactions, allocation and fees each answered absent_reason no_catalog_row (0 source keys, 0 rows, no S3 client created). Resolver: 2 Black Diamond candidates for one last4, read from the opal-data-assets copy of dim_account_xref.
- Cause (read, not run): client_adapter_bd49f._live_prefix -> ctx.prefix(..."49f-live"...) raises no_catalog_row unless the DATA_CATALOG has that exact prefix; the catalog holds only four blackdiamond/49f rows, all opal-data-assets; the build cell's tests plant the -live rows in a fake context.
- Row NFRA_OPLGTW-Z-S293 (BLOCKING). It landed in the CVO's commit 72cf874559 because the CVO's commit swept the shared file. The CVO's row Z-S292 names the NEXT layer: the 49f role's IAM policy explicitly denies opal-data-bd. The served read never got that far.
- en11.AC1 PASS. No account number, name, e-mail or long digit run in any repo file.
