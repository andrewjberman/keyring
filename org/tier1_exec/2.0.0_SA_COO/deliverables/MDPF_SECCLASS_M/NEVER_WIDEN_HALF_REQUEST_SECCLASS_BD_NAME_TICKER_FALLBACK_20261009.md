# Never-widen half, MDPF_SECCLASS -- Black Diamond's classify_with_identity reads the canonical NAME:: row when a position carries a ticker that has no row (FWD-16, cell SC-e-79, row MDPF_SECCLASS-D1-W66-S3)

**Author:** `0.9.0_WK_MDPF_SECCLASS~69` for `2.0.0_SA_COO~M1`, 2026-10-09. **For:** `1.0.0_SA_CTO`, second half. **Status: COO half UNSIGNED; CTO half UNSIGNED.**
This file is a REQUEST. Nothing in it has been deployed or written to any bucket or table. Spec: PRD `org/missions/D8/MDPF/MDPF_SECCLASS/prd/MDPF_SECCLASS_PRD.md`
FWD-16; trace `org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_UNCLASSIFIED_TRACE_D1S11_20261008.json`; order `MDPF_SECCLASS.TO-SC-e79`.

## What is wrong

Round 15 (SC-e-76) made `classify_with_identity` read `NAME::<normalized name>` for a BLANK-ticker position the identity chain cannot place. A position that carries a ticker
with no row in `etf-classifications` still stopped at hop `ticker-no-row` and served `unclassified`, even when its `NAME::` row exists. Measured 2026-10-09 (read-only get-item):
36 group-A trace securities carry a ticker; 23 have no ticker row and a live `NAME::` row (example: LBSAX, COLUMBIA DIVIDEND INCOME A, `NAME::` row equity); 13 have a ticker row today.

## The fix (staged, LOCAL, not deployed)

`data/black_diamond/scripts/gold/lib/etf_classifier.py` `classify_with_identity`, the `ticker-no-row` branch: it calls the existing `_name_row` (SC-e-76's lookup, no second lookup).
A hit returns the row's class and sub-class with class_source `etf-classifications` and identity_hop `ticker-no-row-name-key`. A miss returns `('', '', 'unclassified', 'ticker-no-row')` as before.
A ticker WITH a row returns that row (never overridden); a chain-placed blank-ticker position and a CASH_USD position are unchanged.
Tests: `data/black_diamond/scripts/gold/tests/test_etf_classifier_name_key.py` (12 pass; the old "ticker with no row stays unclassified even if a NAME:: row exists" test is replaced by the
three SC-e-79 arms: ticker-no-row resolves, ticker-with-row control, ticker-no-row-no-NAME control).

## The act (by the issuer, after both halves sign)

1. Deploy ONLY `data/black_diamond/scripts/gold/lib/etf_classifier.py` to `s3://opal-data-bd/code/gold/lib/etf_classifier.py` with
   `.tools/safe-deploy.sh data/black_diamond/scripts/gold/lib/etf_classifier.py` (the deploy core ships only named files), under a change-management ledger, before a BD gold fire.
   The shipped-bundle members seen on the SC-e-76 deploy (row D1-S12: `_shared/etf_classification_scheduled.py` differs from served) are a signer's call again; this worker did not re-measure them.
2. The next BD gold fire loads the lib in C_06, D_03 and D_04 and classifies the ticker-no-row positions through the name key.
3. Read back (leg G): `platinum/firm/mix_summary.json` unclassified share, beside the candidate diff below.

## Blast radius

**Objects the act writes:** the one code object (the lib). No table, no data key. **Objects the next fire writes:** the set the nightly fire already writes (`gold/entities/clients/{rid}.json`,
`gold/views/mix_daily_summary.json`, `platinum/firm/mix_summary.json`, D_04's `platinum/clients/{rid}/...`); the change is CONTENT only. **Not touched:** `etf-classifications`
(read-only), the COT twin, any position whose ticker has a row, any chain-placed blank-ticker position, any ticker-no-row position without a `NAME::` row.
**Writers of the served BD class counted: N = 3** (C_06, D_03, D_04), each calls `classify_with_identity`.

**Local candidate diff** (this worker ran the new `classify_with_identity` locally over the 36 ticker-carrying group-A trace securities, live read-only get-item, no write):

| new class | securities | market value |
|---|---|---|
| equity | 19 | $790,724 |
| fixed_income | 4 | $175,562 |
| **moves out of unclassified (ticker-no-row, NAME:: row live)** | **23** | **$966,285** |
| unchanged (ticker has a row today; not this change) | 13 | $76,794 |

The 23 that move: LBSAX $365,336 equity; SCGE1 $151,435 equity; SCGN1 $149,834 equity; TWCUX $88,937 fixed_income; SCSI1 $59,242 fixed_income; ASMIY $27,730 equity; BALCX $23,420 equity;
SCGS1 $22,958 equity; SCGG1 $22,773 equity; SCGT1 $15,575 fixed_income; PFF $11,808 fixed_income; SCGL1 $5,586 equity; FBCVX $4,813 equity; CEMVX $4,109 equity; AEMGX $3,973 equity;
VWIGX $3,832 equity; FIADX $2,883 equity; FG $1,534 equity; DJT $390 equity; GLPI $67 equity; SKYQ $33 equity; TDSC $17 equity; BLIAQ $1 equity. Dollars are the trace's 2026-10-06 partition;
a later partition moves the dollars, not the rule. Whole-estate effect is small: $966,285 of $2,019,548,568 (about 0.05 pct).

## Rollback per key

The code object `s3://opal-data-bd/code/gold/lib/etf_classifier.py` is versioned. Read-only `head-object`, 2026-10-09:

| VersionId | LastModified | size | role |
|---|---|---|---|
| `yPda0uV6nypDdrdFVi.0ZW86Mdxk_cI2` | 2026-10-08T19:41:53Z | 17907 | CURRENT served (the SC-e-76 lib), ETag 535378b5e0b01891c3cf685faf1ed653: **the rollback target** |

Code rollback: copy that VersionId back over the key (`s3api get-object --version-id`, then deploy it). That restores the SC-e-76 behaviour (ticker-no-row stays unclassified); it does not
restore mix content a fire already rewrote. Data rollback per key: the issuer records, before the fire, the VersionId of `platinum/firm/mix_summary.json` and `gold/views/mix_daily_summary.json`
and of each `gold/entities/clients/{rid}.json` the fire rewrites; any of them is restored to its pre-fire version. This worker did not enumerate the data VersionIds.

## COO half -- SIGNED, with conditions

`2.0.0_SA_COO~M1`, 2026-10-09 ~09:3xZ, after the round-16 drain (@16d5be89dd). The issuer re-ran AC1 (`resolved=23 of 23`), AC3 (`12 passed`) and AC2 (`HALF-READY`).
- **Writers of the served BD class: N = 3** (C_06, D_03, D_04), all through `classify_with_identity`. Both branches of the new hop were read
  in the lib and the test file: a `NAME::` row present serves its class (hop `ticker-no-row-name-key`), and absent stays `unclassified`
  (hop `ticker-no-row`). A ticker with a row is never overridden (the control arm).
- **The test change is ruled.** The replaced test (`..._ticker_with_no_row_stays_unclassified_even_if_name_row_exists`, row D1-W69-S1)
  asserted the exact behaviour this cell's build step 1 reverses. Replacing it with the three ordered arms is inside the decomposition.
- **Condition 1 (sequencing): the SC-e-83 row write lands FIRST.** The candidate diff serves TWCUX ($88,937) as fixed_income through
  `NAME::AMERICAN CENTURY ULTRA INV`, a row known to be wrong (`NEVER_WIDEN_HALF_REQUEST_SECCLASS_ULTRA_NAME_ROW_20261009.md`). After that
  write the diff reads 20 equity ($879,661) and 3 fixed_income ($86,625).
- **Condition 2 (data rollback):** before the first fire on the new lib, the issuer records the VersionIds of `platinum/firm/mix_summary.json`
  and `gold/views/mix_daily_summary.json` in the ledger entry.
- **Condition 3 (named file):** the deploy names `lib/etf_classifier.py` alone; no `_shared` artifact rides it (named-file rule, CTO msg 107147).

## CTO half -- UNSIGNED
