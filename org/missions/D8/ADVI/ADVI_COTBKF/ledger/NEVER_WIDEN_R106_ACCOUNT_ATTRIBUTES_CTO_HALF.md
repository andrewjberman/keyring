# NEVER-WIDEN -- CTO half -- ADVI_COTBKF round 106: the Cottonwood silver run merges account_attributes (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~18:4xZ)

**Binds:** `org/missions/D8/ADVI/ADVI_COTBKF/ledger/NEVER_WIDEN_R106_ACCOUNT_ATTRIBUTES_COO_HALF.md` @7a14b821b4, sha256
`257283f50cac3197ba7dcb3bb733eff5cf0a7e998e5a35e23bda6e5ef4a66f1e` (48 lines), re-hashed by this seat. It also binds that half's section-1
versions, section-3 patch and section-4 forecast. Any edit voids this half.

## Read and accepted

- **The act:** one added line in `cot-pipeline/ssm.tf`, a plan of exactly one change to `aws_ssm_document.cot_silver_run`, one writer of
  the property (N = 1), and per-key rollback (section 2).
- **All four branches are accepted as written.** Branch B (A_00 refuses the build) serves nothing wrong. Its remedy, removing a bad
  partition, is an S3 delete and Andrew's act. This half does not give it.
- **Consumers of the four columns outside the gold scripts: measured, none.** `comp-find '\bportfolio_group\b' --files --all`: 403 hits
  across 121,709 files (12,943 ephemeral, 54 unreadable, 32,559 binary not searched). Cottonwood code reading it: `A_00` (the writer) and
  `D_05` (manual). Every other code hit is the 49 Financial or Black Diamond pipelines, other firms' own data. No portal or gateway reader.
  This closes the half's "not established" line.
- **The early dispatch: NO, as the COO recommends.** Read the organic fire around 2026-10-17 midday, with a dated wait on
  `schedule:cot-silver-run`.

## One added condition (part of this signature)

- **C-1, first-row books.** 122 multi-book accounts take `portfolio_group` from the first row in vendor file order. That value is decided
  by order, not by a rule, and it can flip whenever the vendor reorders the file.
  - It is accepted for now only because nothing serves the column to a reader (above).
  - The close read (b) adds one count: how many of the 122 change `portfolio_group` between the first two consecutive gold builds.
  - If any change, or if any consumer is added before then, the next ADVI_COTBKF round cuts an `A_00` cell first. That cell makes the
    choice deterministic by a stated rule, and the dimension's note says which book a multi-book account shows.

## Signature

**SIGNED** by `1.0.0_SA_CTO~DELL1`, binding sha256 `257283f5...6f1e`, with C-1.

-- 1.0.0_SA_CTO~DELL1
